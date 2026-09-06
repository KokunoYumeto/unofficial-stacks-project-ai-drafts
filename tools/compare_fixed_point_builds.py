#!/usr/bin/env python3
"""Compare two fixed-point build receipts and emit a reproducibility receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

if __package__:
    from .validate_unified_repository import (
        normalize_build_for_reproducibility,
        validate_machine_wide_tex_mutex,
    )
else:
    from validate_unified_repository import (
        normalize_build_for_reproducibility,
        validate_machine_wide_tex_mutex,
    )


IDENTICAL_KEYS = (
    "schema",
    "status",
    "source",
    "builder",
    "composition",
    "environment",
    "build",
    "artifacts",
    "pdfs_committed",
    "source_checkpoint",
)

SOURCE_CHECKPOINT_CONTRACTS = {
    "unofficial-stacks-project-ai-drafts-ega-source-checkpoint/v1": "PASS_SOURCE_CHECKPOINT",
    "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-successor/v1": "PASS_SOURCE_CHECKPOINT_SUCCESSOR",
}


def canonical_json(value: object) -> str:
    """Compare JSON types exactly; True, 1, and 1.0 are not interchangeable."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def validate_source_checkpoint(receipt: dict, label: str) -> None:
    checkpoint = receipt.get("source_checkpoint")
    if not isinstance(checkpoint, dict) or not checkpoint:
        raise ValueError(f"{label} lacks the required source_checkpoint binding")
    expected_status = SOURCE_CHECKPOINT_CONTRACTS.get(checkpoint.get("schema"))
    if expected_status is None or checkpoint.get("status") != expected_status:
        raise ValueError(f"{label} has an unsupported or nonpassing source_checkpoint")
    source, post = receipt.get("source"), checkpoint.get("post_content")
    if not isinstance(source, dict) or not isinstance(post, dict) or (
        post.get("head_commit") != source.get("commit")
        or post.get("head_tree") != source.get("tree")
        or not all(isinstance(source.get(key), str)
                   and re.fullmatch(r"[0-9a-f]{40}", source[key])
                   for key in ("commit", "tree"))
    ):
        raise ValueError(f"{label} source_checkpoint does not bind its build source")
    count = checkpoint.get("protected_input_count")
    roles = checkpoint.get("protected_input_roles")
    digest = checkpoint.get("protected_input_tuple_sha256")
    if (type(count) is not int or count < 1 or not isinstance(roles, dict)
            or not roles or any(not isinstance(key, str) or not key
                                or type(value) is not int or value < 1
                                for key, value in roles.items())
            or sum(roles.values()) != count or not isinstance(digest, str)
            or re.fullmatch(r"[0-9A-Fa-f]{64}", digest) is None):
        raise ValueError(f"{label} source_checkpoint lacks an exact protected-input inventory")
    composition = receipt.get("composition")
    bound = checkpoint.get("canonical_composition")
    if not isinstance(composition, dict) or not isinstance(bound, dict) or any(
        not isinstance(composition.get(right), str)
        or not composition[right]
        or bound.get(left) != composition[right]
        for left, right in (("path", "receipt"), ("git_blob", "receipt_git_blob"),
                            ("sha256", "receipt_sha256"),
                            ("composition_source_commit", "composition_source_commit"))
    ):
        raise ValueError(f"{label} source_checkpoint composition binding mismatch")


def compare_receipts(first: dict, second: dict) -> None:
    """Validate each mutex before discarding only its per-invocation fields.

    Source-checkpoint bindings, including all protected-input hashes and EGA
    semantic evidence, remain exact. No process, profile, policy, or environment
    fields outside the mutex's explicitly validated observation set are removed.
    """
    for label, receipt in (("first", first), ("second", second)):
        if any(key not in receipt for key in IDENTICAL_KEYS):
            missing = [key for key in IDENTICAL_KEYS if key not in receipt]
            raise ValueError(f"{label} receipt lacks bound state: {', '.join(missing)}")
        if (receipt.get("schema") != "unofficial-ai-integrated-stacks-fixed-point-build/v1"
                or receipt.get("status") != "PASS"):
            raise ValueError(f"{label} receipt is not a passing fixed-point build")
        build = receipt.get("build")
        if not isinstance(build, dict):
            raise ValueError(f"{label} receipt lacks build state")
        errors: list[str] = []
        validate_machine_wide_tex_mutex(build.get("machine_wide_tex_mutex"), label, errors)
        if errors:
            raise ValueError("; ".join(errors))
        validate_source_checkpoint(receipt, label)
    mismatched = []
    for key in IDENTICAL_KEYS:
        values = first[key], second[key]
        if key == "build":
            values = tuple(normalize_build_for_reproducibility(value) for value in values)
        if canonical_json(values[0]) != canonical_json(values[1]):
            mismatched.append(key)
    if mismatched:
        raise ValueError("fixed-point receipts differ in bound state: " + ", ".join(mismatched))
    if not isinstance(first.get("created_utc"), str) or not isinstance(second.get("created_utc"), str):
        raise ValueError("receipts lack invocation timestamps")
    if first["created_utc"] == second["created_utc"]:
        raise ValueError("receipts do not identify distinct invocations")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def load_receipt(path: Path) -> tuple[bytes, dict[str, object]]:
    data = path.read_bytes()
    def unique_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"duplicate JSON key in build receipt: {key}")
            value[key] = item
        return value

    def reject_constant(value: str) -> None:
        raise ValueError(f"non-finite JSON constant in build receipt: {value}")

    parsed = json.loads(data.decode("utf-8"), object_pairs_hook=unique_keys,
                        parse_constant=reject_constant)
    if not isinstance(parsed, dict):
        raise ValueError(f"receipt is not a JSON object: {path}")
    if (
        parsed.get("schema")
        != "unofficial-ai-integrated-stacks-fixed-point-build/v1"
        or parsed.get("status") != "PASS"
    ):
        raise ValueError(f"receipt is not a passing full fixed-point build: {path}")
    return data, parsed


def run_identity(
    logical_path: str, data: bytes, receipt: dict[str, object]
) -> dict[str, object]:
    build = receipt.get("build")
    if not isinstance(build, dict):
        raise ValueError("build receipt lacks build state")
    return {
        "receipt": logical_path,
        "created_utc": receipt.get("created_utc"),
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "status": receipt.get("status"),
        "global_fixed_point_sweep": build.get("global_fixed_point_sweep"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first", type=Path, required=True)
    parser.add_argument("--second", type=Path, required=True)
    parser.add_argument("--first-logical-path", required=True)
    parser.add_argument("--second-logical-path", required=True)
    parser.add_argument("--admitted-errata", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    first_path = args.first.resolve()
    second_path = args.second.resolve()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite output: {output}")
    first_bytes, first = load_receipt(first_path)
    second_bytes, second = load_receipt(second_path)

    compare_receipts(first, second)

    artifacts = first.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise ValueError("first receipt lacks artifacts")
    artifact_identities: list[dict[str, object]] = []
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            raise ValueError("invalid artifact row")
        identity = {
            key: artifact.get(key) for key in ("stem", "pages", "bytes", "sha256")
        }
        if (
            not isinstance(identity["stem"], str)
            or not isinstance(identity["pages"], int)
            or not isinstance(identity["bytes"], int)
            or not isinstance(identity["sha256"], str)
        ):
            raise ValueError("invalid artifact identity")
        artifact_identities.append(identity)

    tuple_lines = [
        "|".join(
            (
                str(artifact["stem"]),
                str(artifact["pages"]),
                str(artifact["bytes"]),
                str(artifact["sha256"]),
            )
        )
        for artifact in sorted(artifact_identities, key=lambda item: str(item["stem"]))
    ]
    tuple_set_sha256 = sha256_bytes(
        (("\n".join(tuple_lines)) + "\n").encode("utf-8")
    )

    source = first.get("source")
    builder = first.get("builder")
    composition = first.get("composition")
    environment = first.get("environment")
    build = first.get("build")
    if not all(
        isinstance(item, dict)
        for item in (source, builder, composition, environment, build)
    ):
        raise ValueError("first receipt lacks bound source, builder, or environment state")

    receipt = {
        "schema": "unofficial-ai-integrated-stacks-clean-build-reproducibility/v1",
        "status": "PASS",
        "created_utc": (
            datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        ),
        "source": source,
        "builder": builder,
        "environment": environment,
        "scope": {
            "admitted_errata": args.admitted_errata,
            "registry_cutoff_commit": composition.get("registry_cutoff_commit"),
            "source_commit": source.get("commit"),
            "source_tree": source.get("tree"),
            "composition_receipt": composition.get("receipt"),
            "composition_receipt_sha256": composition.get("receipt_sha256"),
        },
        "method": {
            "execution_model": "independent_linked_worktrees",
            "first_worktree_kind": build.get("worktree_kind"),
            "second_worktree_kind": second.get("build", {}).get("worktree_kind"),
            "builder_path": builder.get("path"),
            "builder_git_blob": builder.get("git_blob"),
            "builder_sha256": builder.get("sha256"),
        },
        "runs": {
            "first": run_identity(
                args.first_logical_path, first_bytes, first
            ),
            "second": run_identity(
                args.second_logical_path, second_bytes, second
            ),
        },
        "artifacts": artifact_identities,
        "comparison": {
            "chapter_count": len(artifact_identities),
            "matched_artifact_count": len(artifact_identities),
            "different_artifact_count": 0,
            "different_artifacts": [],
            "total_pages_each_run": sum(
                int(artifact["pages"]) for artifact in artifact_identities
            ),
            "total_pdf_bytes_each_run": sum(
                int(artifact["bytes"]) for artifact in artifact_identities
            ),
            "artifact_tuple_set_sha256_each_run": tuple_set_sha256,
            "all_artifact_identities_exactly_equal": True,
            "source_identity_equal": True,
            "builder_identity_equal": True,
            "environment_identity_equal": True,
            "fixed_point_sweep_equal": True,
            "source_checkpoint_identity_equal": True,
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, allow_nan=False) + "\n",
                      encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "status": "PASS",
                "matched_artifacts": len(artifact_identities),
                "artifact_tuple_set_sha256": tuple_set_sha256,
                "output": str(output),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
