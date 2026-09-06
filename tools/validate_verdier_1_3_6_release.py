#!/usr/bin/env python3
"""Validate the Verdier II.1.3.6 candidate's admission and composition.

This is a deliberately bounded, read-only release gate.  It validates one
candidate, its two registry records, and the single insertion into
``derived.tex``.  It does not build TeX, access the network, or write files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


REPORT_SCHEMA = (
    "unofficial-ai-integrated-stacks-verdier-1-3-6-release-validation/v1"
)
MANIFEST_SCHEMA = "mathematics-commons-stacks-candidate-manifest/v1"
REVIEW_SCHEMA = "mathematics-commons-stacks-verdier-independent-review/v1"
OVERLAY_REGISTRY_SCHEMA = "mathematics-commons-stacks-overlay-registry/v1"
LEASE_REGISTRY_SCHEMA = "mathematics-commons-stacks-lease-registry/v1"
COMPOSITION_SCHEMA = "mathematics-commons-stacks-composition-operation/v1"
CORRECTION_RECEIPT_SCHEMA = (
    "mathematics-commons-stacks-verdier-manifest-closure-correction/v1"
)

CANDIDATE_ID = "stacks-verdier-a04446e-1-3-6-r1"
NAMESPACE = "commons/stacks/verdier-ast239-1-3-6-r1"
LEASE_ID = "stacks-lease-000044-verdier-ast239-1-3-6-r1"
WRITER_TASK = "019fca5a-c80e-7890-a46b-4948ff443e6d"
OPERATION_ID = "VDR-STK-COMP-0002"
PROPOSED_LABEL = "lemma-homotopy-category-abelian-split"
AFTER_PROOF_LABEL = "proposition-homotopy-category-triangulated"
BEFORE_ENVIRONMENT_LABEL = "remark-boundedness-conditions-triangulated"
MANIFEST_RIGHTS_STATE = (
    "Source locators and hashes only; payload independently worded; no source "
    "relicense asserted; GFDL compatibility required at composition."
)
OFFICIAL_COMMIT = "a04446e57ec1fbc252a871afcec7752fb2807b14"
OFFICIAL_TREE = "3feeb703b931a6e7259782c10e7d1575adc83e5e"
SOURCE_PATH = "derived.tex"
UNIT_IDS = (
    "verdier:ast239:1.3.6",
    "verdier:ast239:1.3.6:equivalent-conditions",
    "verdier:ast239:1.3.6:proof:i-iff-ii",
    "verdier:ast239:1.3.6:proof:ii-implies-iii",
    "verdier:ast239:1.3.6:construction:hstar-complex",
    "verdier:ast239:1.3.6:claim:hstar-equivalence",
    "verdier:ast239:1.3.6:conclusion:iii-implies-ii",
)
EXPECTED_REFERENCES = frozenset(
    {
        "lemma-when-split",
        "proposition-homotopy-category-triangulated",
        "homology-definition-abelian-category",
        "homology-lemma-map-cohomology-homotopy-cochain",
        "homology-definition-graded",
        "homology-lemma-graded",
    }
)

CANDIDATE_RELATIVE = (
    Path("ai-integrated") / "candidates" / Path(NAMESPACE)
).as_posix()
MANIFEST_RELATIVE = f"{CANDIDATE_RELATIVE}/candidate.manifest.json"
OVERLAYS_RELATIVE = "ai-integrated/registry/overlays.json"
LEASES_RELATIVE = "ai-integrated/registry/leases.json"
VALIDATOR_RELATIVE = "tools/validate_verdier_1_3_6_release.py"
CORRECTION_RECEIPT_RELATIVE = (
    "validation/stacks-verdier-a04446e-1-3-6-r1-"
    "manifest-closure-correction-2026-09-06.json"
)
REVIEW_CANDIDATE_RELATIVE = "replay/independent-review.json"
REVIEW_REGISTRY_RELATIVE = f"candidates/{NAMESPACE}/{REVIEW_CANDIDATE_RELATIVE}"

FROZEN_REVIEW_COMMIT = "52eccb5772831e4bd17f9d4306b1ad0f60dec43f"
FROZEN_REVIEW_TREE = "745bdaf88721effe0839ef8888c1fda967d716c5"
FROZEN_CANDIDATE_SUBTREE = "b1f78050a106d379ac990676dbb64dfed7c706cc"
SEALED_REPLAY_COMMIT = "8f95214f9275cdc698f0c9bf5e7e8e5784772977"
SEALED_REPLAY_TREE = "eee7fe6df32e5d375b3d49bb98d9fb9d91e48f8b"
SEALED_CANDIDATE_SUBTREE = "0dc3108886b01160fe0b049c84fc589373665d27"
ADMISSION_COMMIT = "d78483415a984eb7b46ad57b6056d8f718e3f395"
ADMISSION_TREE = "15c4126b285fb4cd31469c7ec8bc6c7b7563a0f6"
CLOSURE_REPAIR_COMMIT = "85500f2243acb39e24ff16505e3f9f520543c8e1"
CLOSURE_REPAIR_TREE = "e51b3f18e424c97df9915b81e95ecb2dd1efdfd5"
REPAIRED_CANDIDATE_SUBTREE = "40f744e2e748e89433470df2fb050c776a52c403"
INITIAL_MANIFEST_SHA256 = (
    "CDAD13962B90D5ACF574586BBE052B65EDA83F15B2B336C007887DAF23198B4C"
)
FINAL_MANIFEST_SHA256 = (
    "C007BBFB1AB068843B7759FF69ED338BE0071349975EDCE20472876B89F01F2F"
)
CORRECTION_RECEIPT_BYTES = 19781
CORRECTION_RECEIPT_SHA256 = (
    "2FA95B465797EEE9656206993DABB0E66228D66418BE55700F364FB64191102E"
)
CLOSURE_REPAIR_FILES = {
    ".gitattributes": {
        "bytes": 117,
        "sha256": "19A1DCCFFFD90CC9A3FCE89B2D147B1844EE285291736D1245CE061DF6864549",
        "git_blob": "24133845b0f4cf6ce10d832ef8fa6b4e458a920a",
    },
    ".gitignore": {
        "bytes": 26,
        "sha256": "5B561AA9AE36CA5FF408C3A22CE239167F80F4D3B6EF53FF095A6136FB824AA8",
        "git_blob": "eba87b7b2b47f90b03762169a2bd5e61cc60051d",
    },
    "builds/baseline-derived.log": {
        "bytes": 51611,
        "sha256": "285307FCB784CBB447DA375958465A8127BF19E69AD587117C649CFC13B47BB8",
        "git_blob": "9568bc4fd6698f6f2f39e382d5d25a78435ea368",
    },
    "builds/derived.log": {
        "bytes": 51617,
        "sha256": "3907949D2C8BE01837677A4A9726563FB5EB5AB54252F55361D3E76B6662DCE6",
        "git_blob": "2f79caf6f29a81cfeee1e4ab40f525d2785af236",
    },
    "builds/derived.pdf": {
        "bytes": 1251089,
        "sha256": "1B45A53DFDC6394AB795855172915794F20634953361E8596AF17FC2E6F97331",
        "git_blob": "b7eb3e8b5befc4ba5c407959860d1c83aba1f14c",
    },
}

SINGLED_MANIFEST_FIELDS = (
    "stable_unit_manifest",
    "source_map",
    "decision_ledger",
    "rejection_ledger",
    "formula_diagram_inventory",
)
HEX64 = re.compile(r"[0-9A-Fa-f]{64}")
REFERENCE_PATTERN = re.compile(r"\\(?:ref|autoref|pageref)\{([^{}]+)\}")
LABEL_PATTERN = re.compile(r"\\label\{([^{}]+)\}")


class ValidationError(RuntimeError):
    """A deterministic release invariant did not hold."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def git(root: Path, *args: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise ValidationError(detail or f"bounded git query failed: {' '.join(args)}")
    return completed.stdout


def git_text(root: Path, *args: str) -> str:
    return git(root, *args).decode("utf-8", errors="strict").strip()


def commit_bytes(root: Path, revision: str, path: str) -> bytes:
    return git(root, "show", f"{revision}:{path}")


def git_success(root: Path, *args: str) -> bool:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return completed.returncode == 0


def require_commit_identity(
    root: Path, commit: str, tree: str, label: str
) -> None:
    require(
        git_success(root, "cat-file", "-e", f"{commit}^{{commit}}"),
        f"{label} commit is absent",
    )
    require(
        git_text(root, "rev-parse", f"{commit}^{{tree}}") == tree,
        f"{label} tree mismatch",
    )


def require_parent(root: Path, commit: str, parent: str, label: str) -> None:
    row = git_text(root, "rev-list", "--parents", "-n", "1", commit).split()
    require(row == [commit, parent], f"{label} is not a single-parent child of {parent}")


def require_ancestor(root: Path, ancestor: str, descendant: str, label: str) -> None:
    require(
        git_success(root, "merge-base", "--is-ancestor", ancestor, descendant),
        f"ancestry check failed: {label}",
    )


def candidate_tree_entries(root: Path, revision: str) -> dict[str, str]:
    prefix = CANDIDATE_RELATIVE + "/"
    lines = git_text(
        root, "ls-tree", "-r", revision, "--", CANDIDATE_RELATIVE
    ).splitlines()
    entries: dict[str, str] = {}
    for line in lines:
        match = re.fullmatch(r"\d+ blob ([0-9a-f]{40})\t(.+)", line)
        require(match is not None, f"invalid candidate tree row at {revision}: {line!r}")
        assert match is not None
        path = match.group(2)
        require(path.startswith(prefix), f"candidate tree row escapes its prefix: {path}")
        relative = path[len(prefix) :]
        require(relative not in entries, f"candidate tree repeats a path: {relative}")
        entries[relative] = match.group(1)
    return entries


def load_json_bytes(data: bytes, label: str) -> dict[str, Any]:
    try:
        value = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid {label}: {exc}") from exc
    require(isinstance(value, dict), f"{label} must contain one JSON object")
    return value


def load_local_json(path: Path, label: str) -> dict[str, Any]:
    try:
        return load_json_bytes(path.read_bytes(), label)
    except OSError as exc:
        raise ValidationError(f"cannot read {label}: {exc}") from exc


def load_single_jsonl_bytes(data: bytes, label: str) -> dict[str, Any]:
    try:
        rows = [
            json.loads(line)
            for line in data.decode("utf-8").splitlines()
            if line.strip()
        ]
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid {label}: {exc}") from exc
    require(
        len(rows) == 1 and isinstance(rows[0], dict),
        f"{label} must contain exactly one JSON object",
    )
    return rows[0]


def require_safe_relative(value: object, label: str) -> str:
    require(isinstance(value, str) and value, f"{label} is empty")
    assert isinstance(value, str)
    path = Path(value)
    require(
        not path.is_absolute()
        and ".." not in path.parts
        and "\\" not in value
        and path.as_posix() == value,
        f"{label} is not a safe POSIX-relative path: {value!r}",
    )
    return value


def require_sha(value: object, label: str) -> str:
    require(
        isinstance(value, str) and HEX64.fullmatch(value) is not None,
        f"{label} is not a SHA-256 identity",
    )
    assert isinstance(value, str)
    return value.upper()


def require_utc(value: object, label: str) -> datetime:
    require(isinstance(value, str) and value, f"{label} is absent")
    assert isinstance(value, str)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"{label} is not an ISO-8601 timestamp") from exc
    require(parsed.tzinfo is not None, f"{label} lacks a timezone")
    require(
        parsed.utcoffset() is not None
        and parsed.utcoffset().total_seconds() == 0,
        f"{label} is not UTC",
    )
    return parsed


def run_candidate_tool(
    candidate: Path, name: str, expected_keys: dict[str, object]
) -> dict[str, Any]:
    path = candidate / name
    require(path.is_file(), f"candidate tool is absent: {name}")
    completed = subprocess.run(
        [sys.executable, "-B", str(path)],
        cwd=candidate,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        timeout=180,
    )
    require(
        completed.returncode == 0,
        f"candidate {name} failed: "
        + (completed.stderr.strip() or completed.stdout.strip()),
    )
    reports: list[dict[str, Any]] = []
    for line in completed.stdout.splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(item, dict):
            reports.append(item)
    require(reports, f"candidate {name} emitted no machine-readable report")
    report = reports[-1]
    require(report.get("passed") is True, f"candidate {name} did not report pass")
    for key, expected in expected_keys.items():
        require(
            report.get(key) == expected,
            f"candidate {name} report mismatch for {key}",
        )
    return report


def validate_local_final_lifecycle(candidate: Path) -> dict[str, Any]:
    """Fail clearly before looking for admission if replay is not final."""
    config = load_local_json(candidate / "candidate.config.json", "candidate config")
    stable = load_local_json(candidate / "stable-units.json", "stable-unit manifest")
    inventory = load_local_json(
        candidate / "formula-diagram-inventory.json", "formula/diagram inventory"
    )
    manifest = load_local_json(candidate / "candidate.manifest.json", "candidate manifest")
    pointer = load_local_json(candidate / "LEASE.json", "candidate lease pointer")

    require(config.get("candidate_id") == CANDIDATE_ID, "candidate config ID mismatch")
    require(manifest.get("candidate_id") == CANDIDATE_ID, "manifest candidate ID mismatch")
    require(manifest.get("schema") == MANIFEST_SCHEMA, "manifest schema mismatch")
    for field, expected in (
        ("lease_id", LEASE_ID),
        ("namespace", NAMESPACE),
        ("writer_task", WRITER_TASK),
    ):
        require(config.get(field) == expected, f"candidate config {field} mismatch")
        require(manifest.get(field) == expected, f"manifest {field} mismatch")
        require(pointer.get(field) == expected, f"lease pointer {field} mismatch")

    require(
        config.get("upstream")
        == {
            "lock": "upstream/stacks.lock.json",
            "commit": OFFICIAL_COMMIT,
            "tree": OFFICIAL_TREE,
        },
        "candidate upstream identity mismatch",
    )
    require(manifest.get("upstream") == config["upstream"], "manifest upstream mismatch")
    require(pointer.get("upstream_commit") == OFFICIAL_COMMIT, "lease pointer upstream mismatch")
    require(
        config.get("expected_unit_ids") == list(UNIT_IDS),
        "candidate stable-ID inventory mismatch",
    )
    units = stable.get("units")
    require(
        isinstance(units, list)
        and stable.get("unit_count") == len(UNIT_IDS)
        and [row.get("id") for row in units if isinstance(row, dict)] == list(UNIT_IDS),
        "stable-unit manifest does not contain the exact seven units",
    )

    require(config.get("review_state") == "performed", "independent review is not final")
    require(config.get("independent_replay") == "passed", "independent replay is not passing")
    require(
        config.get("admission_state") == "not_admitted",
        "candidate-local admission witness must remain not_admitted",
    )
    require(manifest.get("review_state") == "performed", "manifest review is not final")
    require(manifest.get("independent_replay") == "passed", "manifest replay is not passing")
    require(manifest.get("unresolved_defects") == [], "manifest has unresolved defects")
    lifecycle = stable.get("lifecycle")
    require(isinstance(lifecycle, dict), "stable-unit lifecycle is absent")
    require(lifecycle.get("review_state") == "performed", "stable-unit review is not final")
    require(lifecycle.get("independent_replay") == "passed", "stable-unit replay is not passing")
    require(
        lifecycle.get("admission_state") == "not_admitted",
        "stable-unit admission witness must remain not_admitted",
    )
    require(
        inventory.get("independent_review_state") == "performed_passed",
        "formula inventory review is not final",
    )
    require(
        inventory.get("independent_replay") == "passed",
        "formula inventory replay is not passing",
    )
    require(
        inventory.get("admission_state") == "not_admitted",
        "formula inventory admission witness must remain not_admitted",
    )
    return {
        "config": config,
        "stable": stable,
        "inventory": inventory,
        "manifest": manifest,
        "pointer": pointer,
    }


def require_clean_committed_scope(root: Path) -> dict[str, Any]:
    paths = (
        CANDIDATE_RELATIVE,
        OVERLAYS_RELATIVE,
        LEASES_RELATIVE,
        SOURCE_PATH,
        CORRECTION_RECEIPT_RELATIVE,
        VALIDATOR_RELATIVE,
    )
    for cached in (False, True):
        command = ["git", "-C", str(root), "diff", "--quiet"]
        if cached:
            command.append("--cached")
        command.extend(["--", *paths])
        completed = subprocess.run(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(
            completed.returncode == 0,
            "release scope has uncommitted changes"
            if completed.returncode == 1
            else "bounded clean-state query failed",
        )
    untracked = git_text(
        root,
        "ls-files",
        "--others",
        "--exclude-standard",
        "--",
        CANDIDATE_RELATIVE,
        CORRECTION_RECEIPT_RELATIVE,
        VALIDATOR_RELATIVE,
    ).splitlines()
    require(not untracked, f"release scope has untracked files: {untracked}")
    for path in (
        MANIFEST_RELATIVE,
        OVERLAYS_RELATIVE,
        LEASES_RELATIVE,
        SOURCE_PATH,
        CORRECTION_RECEIPT_RELATIVE,
        VALIDATOR_RELATIVE,
    ):
        tracked = git_text(root, "ls-files", "--error-unmatch", "--", path)
        require(tracked == path, f"required release path is not tracked: {path}")
    committed = commit_bytes(root, "HEAD", VALIDATOR_RELATIVE)
    worktree = (root / VALIDATOR_RELATIVE).read_bytes()
    require(
        worktree == committed,
        "validator worktree bytes differ from the committed validator",
    )
    return {
        "path": VALIDATOR_RELATIVE,
        "bytes": len(committed),
        "sha256": sha256(committed),
        "git_blob": git_text(root, "rev-parse", f"HEAD:{VALIDATOR_RELATIVE}"),
        "worktree_matches_committed": True,
    }


def manifest_references(
    manifest: dict[str, Any], *, require_review: bool = True
) -> dict[str, str]:
    references: dict[str, str] = {}

    def add(binding: object, label: str) -> None:
        require(isinstance(binding, dict), f"invalid manifest binding: {label}")
        assert isinstance(binding, dict)
        path = require_safe_relative(binding.get("path"), f"{label} path")
        digest = require_sha(binding.get("sha256"), f"{label} hash")
        require(path not in references, f"manifest repeats a path: {path}")
        references[path] = digest

    authorities = manifest.get("source_authorities")
    builds = manifest.get("builds")
    require(isinstance(authorities, list) and authorities, "manifest has no source authority")
    require(isinstance(builds, list) and builds, "manifest has no build bindings")
    for index, binding in enumerate(authorities):
        add(binding, f"source_authorities[{index}]")
    for index, binding in enumerate(builds):
        add(binding, f"builds[{index}]")
    for field in SINGLED_MANIFEST_FIELDS:
        add(manifest.get(field), field)
    if require_review:
        require(
            REVIEW_CANDIDATE_RELATIVE in references,
            "final manifest does not bind the independent replay receipt",
        )
    return references


def validate_committed_candidate(
    root: Path, local: dict[str, Any]
) -> dict[str, Any]:
    manifest_raw = commit_bytes(root, "HEAD", MANIFEST_RELATIVE)
    require(
        manifest_raw == (root / MANIFEST_RELATIVE).read_bytes(),
        "worktree manifest differs from its committed bytes",
    )
    manifest = load_json_bytes(manifest_raw, "committed candidate manifest")
    require(manifest == local["manifest"], "local/committed manifest mismatch")
    require(
        manifest.get("rights_state") == MANIFEST_RIGHTS_STATE,
        "candidate manifest rights statement mismatch",
    )
    references = manifest_references(manifest)
    for path, expected in references.items():
        observed = sha256(
            commit_bytes(root, "HEAD", f"{CANDIDATE_RELATIVE}/{path}")
        )
        require(observed == expected, f"manifest hash mismatch: {path}")

    authority_relative = "authority/authority.lock.json"
    require(authority_relative in references, "manifest omits the authority lock")
    authority = load_json_bytes(
        commit_bytes(root, "HEAD", f"{CANDIDATE_RELATIVE}/{authority_relative}"),
        "committed authority lock",
    )
    require(
        authority.get("rights_boundary")
        == {
            "evidence_mode": "locators_hashes_and_independent_paraphrase_only",
            "verbatim_source_prose_in_candidate": False,
            "source_work_license_assertion": "none_by_candidate",
            "source_relicensed": False,
            "source_public_domain_claimed": False,
            "source_provenance_and_release_terms_remain_controlling": True,
            "payload_requires_independent_wording_and_gfdl_compatibility": True,
        },
        "authority lock rights boundary mismatch",
    )

    committed_files = git_text(
        root, "ls-tree", "-r", "--name-only", "HEAD", "--", CANDIDATE_RELATIVE
    ).splitlines()
    expected_files = sorted(
        [MANIFEST_RELATIVE]
        + [f"{CANDIDATE_RELATIVE}/{path}" for path in references]
    )
    require(
        sorted(committed_files) == expected_files,
        "committed candidate subtree is not exactly manifest-closed",
    )

    review_raw = commit_bytes(
        root, "HEAD", f"{CANDIDATE_RELATIVE}/{REVIEW_CANDIDATE_RELATIVE}"
    )
    require(
        references[REVIEW_CANDIDATE_RELATIVE] == sha256(review_raw),
        "manifest/replay hash mismatch",
    )
    review = load_json_bytes(review_raw, "independent replay receipt")
    require(review.get("schema") == REVIEW_SCHEMA, "independent replay schema mismatch")
    require(review.get("candidate_id") == CANDIDATE_ID, "independent replay candidate mismatch")
    require(review.get("status") == "PASS" and review.get("passed") is True, "independent replay is not passing")
    require(review.get("review_state") == "performed", "independent replay review state mismatch")
    require(review.get("independent_replay") == "passed", "independent replay state mismatch")
    require(review.get("unresolved_defects") == [], "independent replay reports unresolved defects")
    separation = review.get("reviewer_separation")
    require(isinstance(separation, dict), "independent replay lacks reviewer separation")
    require(
        separation.get("producer_writer_task_id") == WRITER_TASK
        and separation.get("reviewer_is_separate_from_producer") is True
        and separation.get("reviewer_participated_in_candidate_authoring") is False
        and separation.get("reviewer_participated_in_candidate_build") is False
        and separation.get("reviewer_participated_in_initial_manifest_sealing") is False
        and separation.get("frozen_candidate_inspected_before_receipt_write") is True
        and separation.get("existing_candidate_files_mutated") is False
        and separation.get("tex_invoked_during_review") is False,
        "independent replay reviewer-separation contract mismatch",
    )
    checks = review.get("commands_and_check_results")
    require(
        isinstance(checks, list)
        and checks
        and all(isinstance(row, dict) and row.get("passed") is True for row in checks),
        "independent replay checks are absent or not all passing",
    )
    for field in (
        "manifest_hash_checks",
        "authority_source_checks",
        "stable_unit_checks",
        "stacks_source_reference_checks",
        "mathematical_proof_checks",
        "composition_replay",
        "build_mutex_visual_checks",
    ):
        section = review.get(field)
        require(
            isinstance(section, dict)
            and section.get("status") == "PASS"
            and section.get("passed") is True,
            f"independent replay section is not passing: {field}",
        )

    frozen = review.get("frozen_candidate")
    require(isinstance(frozen, dict), "independent replay lacks a frozen-candidate binding")
    reviewed_commit = frozen.get("commit")
    require(
        isinstance(reviewed_commit, str)
        and re.fullmatch(r"[0-9a-f]{40}", reviewed_commit) is not None,
        "independent replay has an invalid reviewed commit",
    )
    assert isinstance(reviewed_commit, str)
    reviewed_tree = git_text(root, "rev-parse", f"{reviewed_commit}^{{tree}}")
    require(reviewed_tree == frozen.get("tree"), "independent replay reviewed-tree mismatch")
    require(
        frozen.get("head_matches_frozen_commit") is True
        and frozen.get("head_tree_matches_frozen_tree") is True
        and frozen.get("narrow_candidate_diff_before_receipt_write") == [],
        "independent replay did not inspect a clean frozen candidate",
    )
    ancestry = subprocess.run(
        ["git", "-C", str(root), "merge-base", "--is-ancestor", reviewed_commit, "HEAD"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(ancestry.returncode == 0, "reviewed candidate commit is not an ancestor of HEAD")
    initial = frozen.get("initial_manifest")
    require(isinstance(initial, dict), "independent replay lacks its initial-manifest binding")
    require(initial.get("path") == "candidate.manifest.json", "reviewed manifest path mismatch")
    initial_raw = commit_bytes(root, reviewed_commit, MANIFEST_RELATIVE)
    require(len(initial_raw) == initial.get("bytes"), "reviewed manifest byte count mismatch")
    require(
        sha256(initial_raw) == require_sha(initial.get("sha256"), "reviewed manifest"),
        "reviewed manifest hash mismatch",
    )
    require(
        git_text(root, "rev-parse", f"{reviewed_commit}:{MANIFEST_RELATIVE}")
        == initial.get("git_blob"),
        "reviewed manifest blob mismatch",
    )
    require(
        initial.get("stable_unit_count") == len(UNIT_IDS)
        and initial.get("all_referenced_files_present") is True
        and initial.get("all_referenced_hashes_match") is True
        and initial.get("checker_passed_before_receipt_write") is True,
        "reviewed initial-manifest closure is not passing",
    )
    return {
        "config": local["config"],
        "manifest": manifest,
        "manifest_sha256": sha256(manifest_raw),
        "manifest_references": references,
        "candidate_tree": git_text(root, "rev-parse", f"HEAD:{CANDIDATE_RELATIVE}"),
        "review": review,
        "review_sha256": sha256(review_raw),
    }


def validate_closure_repair_topology(
    root: Path, candidate: dict[str, Any]
) -> dict[str, Any]:
    identities = (
        (FROZEN_REVIEW_COMMIT, FROZEN_REVIEW_TREE, "frozen review"),
        (SEALED_REPLAY_COMMIT, SEALED_REPLAY_TREE, "sealed replay"),
        (ADMISSION_COMMIT, ADMISSION_TREE, "admission"),
        (CLOSURE_REPAIR_COMMIT, CLOSURE_REPAIR_TREE, "closure repair"),
    )
    for commit, tree, label in identities:
        require_commit_identity(root, commit, tree, label)
    require_parent(
        root, SEALED_REPLAY_COMMIT, FROZEN_REVIEW_COMMIT, "sealed replay"
    )
    require_parent(root, ADMISSION_COMMIT, SEALED_REPLAY_COMMIT, "admission")
    require_parent(
        root, CLOSURE_REPAIR_COMMIT, ADMISSION_COMMIT, "closure repair"
    )
    require_ancestor(root, ADMISSION_COMMIT, CLOSURE_REPAIR_COMMIT, "admission to repair")
    require_ancestor(root, CLOSURE_REPAIR_COMMIT, "HEAD", "closure repair to HEAD")

    expected_subtrees = (
        (FROZEN_REVIEW_COMMIT, FROZEN_CANDIDATE_SUBTREE, "frozen review"),
        (SEALED_REPLAY_COMMIT, SEALED_CANDIDATE_SUBTREE, "sealed replay"),
        (ADMISSION_COMMIT, SEALED_CANDIDATE_SUBTREE, "admission"),
        (CLOSURE_REPAIR_COMMIT, REPAIRED_CANDIDATE_SUBTREE, "closure repair"),
        ("HEAD", REPAIRED_CANDIDATE_SUBTREE, "current HEAD"),
    )
    for revision, expected, label in expected_subtrees:
        require(
            git_text(root, "rev-parse", f"{revision}:{CANDIDATE_RELATIVE}")
            == expected,
            f"{label} candidate subtree mismatch",
        )

    initial_manifest_raw = commit_bytes(
        root, FROZEN_REVIEW_COMMIT, MANIFEST_RELATIVE
    )
    initial_manifest = load_json_bytes(initial_manifest_raw, "initial frozen manifest")
    require(
        sha256(initial_manifest_raw) == INITIAL_MANIFEST_SHA256,
        "initial frozen manifest hash mismatch",
    )
    initial_references = manifest_references(initial_manifest, require_review=False)
    final_manifest_raw = commit_bytes(root, SEALED_REPLAY_COMMIT, MANIFEST_RELATIVE)
    final_manifest = load_json_bytes(final_manifest_raw, "sealed final manifest")
    require(
        sha256(final_manifest_raw)
        == candidate["manifest_sha256"]
        == FINAL_MANIFEST_SHA256,
        "sealed final manifest hash mismatch",
    )
    final_references = manifest_references(final_manifest)

    frozen_entries = candidate_tree_entries(root, FROZEN_REVIEW_COMMIT)
    sealed_entries = candidate_tree_entries(root, SEALED_REPLAY_COMMIT)
    admission_entries = candidate_tree_entries(root, ADMISSION_COMMIT)
    repaired_entries = candidate_tree_entries(root, CLOSURE_REPAIR_COMMIT)
    head_entries = candidate_tree_entries(root, "HEAD")
    manifest_name = "candidate.manifest.json"
    expected_missing = sorted(CLOSURE_REPAIR_FILES)
    initial_missing = sorted(set(initial_references) - set(frozen_entries))
    final_missing = sorted(set(final_references) - set(sealed_entries))
    require(
        initial_missing == expected_missing,
        f"initial manifest missing-set mismatch: {initial_missing}",
    )
    require(
        final_missing == expected_missing,
        f"admitted final manifest missing-set mismatch: {final_missing}",
    )
    require(
        set(frozen_entries) == ({manifest_name} | (set(initial_references) - set(expected_missing))),
        "frozen candidate has undeclared files or an incomplete missing-set account",
    )
    require(
        set(sealed_entries) == ({manifest_name} | (set(final_references) - set(expected_missing))),
        "sealed candidate has undeclared files or an incomplete missing-set account",
    )
    require(
        sealed_entries == admission_entries,
        "admission changed the sealed candidate subtree",
    )
    require(
        set(repaired_entries) == ({manifest_name} | set(final_references)),
        "repair commit does not provide exact full manifest closure",
    )
    require(
        head_entries == repaired_entries,
        "current candidate differs from the repaired manifest-closed subtree",
    )

    added = sorted(set(repaired_entries) - set(admission_entries))
    removed = sorted(set(admission_entries) - set(repaired_entries))
    require(added == expected_missing and removed == [], "repair tree delta is not the exact five additions")
    for path, blob in admission_entries.items():
        require(
            repaired_entries.get(path) == blob,
            f"repair changed a pre-existing candidate file: {path}",
        )
    for path, identity in CLOSURE_REPAIR_FILES.items():
        require(path not in admission_entries, f"repair path already existed before repair: {path}")
        require(repaired_entries.get(path) == identity["git_blob"], f"repair blob mismatch: {path}")
        data = commit_bytes(
            root, CLOSURE_REPAIR_COMMIT, f"{CANDIDATE_RELATIVE}/{path}"
        )
        require(len(data) == identity["bytes"], f"repair byte count mismatch: {path}")
        require(sha256(data) == identity["sha256"], f"repair hash mismatch: {path}")
        require(
            initial_references.get(path) == final_references.get(path) == identity["sha256"],
            f"repair bytes were not exactly the bytes declared by both manifests: {path}",
        )

    expected_diff = [
        f"A\t{CANDIDATE_RELATIVE}/{path}" for path in CLOSURE_REPAIR_FILES
    ]
    observed_diff = git_text(
        root,
        "diff-tree",
        "--no-commit-id",
        "--name-status",
        "-r",
        CLOSURE_REPAIR_COMMIT,
    ).splitlines()
    require(observed_diff == expected_diff, "closure-repair commit changed paths beyond the exact five additions")

    for relative in (MANIFEST_RELATIVE, f"{CANDIDATE_RELATIVE}/{REVIEW_CANDIDATE_RELATIVE}"):
        blobs = {
            git_text(root, "rev-parse", f"{revision}:{relative}")
            for revision in (
                SEALED_REPLAY_COMMIT,
                ADMISSION_COMMIT,
                CLOSURE_REPAIR_COMMIT,
                "HEAD",
            )
        }
        require(len(blobs) == 1, f"repair or later history changed {relative}")

    return {
        "frozen_review_commit": FROZEN_REVIEW_COMMIT,
        "sealed_replay_commit": SEALED_REPLAY_COMMIT,
        "admission_commit": ADMISSION_COMMIT,
        "closure_repair_commit": CLOSURE_REPAIR_COMMIT,
        "initial_declared_reference_count": len(initial_references),
        "final_declared_reference_count": len(final_references),
        "prior_complete_missing_set": expected_missing,
        "added_file_count": len(added),
        "preexisting_file_count": len(admission_entries),
        "current_candidate_file_count": len(head_entries),
        "repaired_candidate_subtree": REPAIRED_CANDIDATE_SUBTREE,
    }


def validate_closure_correction_receipt(
    root: Path, candidate: dict[str, Any], topology: dict[str, Any]
) -> dict[str, Any]:
    receipt_raw = commit_bytes(root, "HEAD", CORRECTION_RECEIPT_RELATIVE)
    require(
        len(receipt_raw) == CORRECTION_RECEIPT_BYTES,
        "closure-correction receipt byte count mismatch",
    )
    require(
        sha256(receipt_raw) == CORRECTION_RECEIPT_SHA256,
        "closure-correction receipt hash mismatch",
    )
    require(
        (root / CORRECTION_RECEIPT_RELATIVE).read_bytes() == receipt_raw,
        "worktree closure-correction receipt differs from committed bytes",
    )
    receipt = load_json_bytes(receipt_raw, "manifest-closure correction receipt")
    expected_top_level = {
        "schema",
        "candidate_id",
        "status",
        "passed",
        "audited_at_utc",
        "audit_scope",
        "commit_topology",
        "historical_declared_minus_committed",
        "repair_diff",
        "repaired_blobs",
        "protected_bytes_unchanged",
        "current_manifest_closure",
        "commands_and_results",
        "unresolved_defects",
    }
    require(set(receipt) == expected_top_level, "closure-correction receipt shape mismatch")
    require(receipt.get("schema") == CORRECTION_RECEIPT_SCHEMA, "closure-correction receipt schema mismatch")
    require(receipt.get("candidate_id") == CANDIDATE_ID, "closure-correction candidate mismatch")
    require(
        receipt.get("status") == "PASS" and receipt.get("passed") is True,
        "closure-correction receipt is not passing",
    )
    require(receipt.get("unresolved_defects") == [], "closure-correction receipt reports unresolved defects")
    audited_at = require_utc(receipt.get("audited_at_utc"), "closure-correction audit time")

    scope = receipt.get("audit_scope")
    require(isinstance(scope, dict), "closure-correction audit scope is absent")
    require(
        scope.get("repair_commit") == CLOSURE_REPAIR_COMMIT
        and scope.get("candidate_path") == CANDIDATE_RELATIVE
        and scope.get("repository_wide_status_or_untracked_scan_performed") is False
        and scope.get("tex_invoked") is False
        and scope.get("candidate_or_registry_file_written") is False
        and scope.get("commit_created") is False
        and scope.get("only_write") == CORRECTION_RECEIPT_RELATIVE,
        "closure-correction audit scope mismatch",
    )

    commit_topology = receipt.get("commit_topology")
    require(isinstance(commit_topology, dict), "receipt commit topology is absent")
    require(
        commit_topology.get("linear_chain_verified") is True
        and commit_topology.get("head_is_repair_commit") is True
        and commit_topology.get("frozen_is_ancestor_of_admission") is True
        and commit_topology.get("admission_is_direct_parent_of_repair") is True,
        "receipt commit-topology flags are not passing",
    )
    expected_commits = (
        ("frozen_candidate", FROZEN_REVIEW_COMMIT, "ec0a80d418d8fa44c1b9fa077fcec8fe9f88c9df", FROZEN_REVIEW_TREE),
        ("independent_replay_seal", SEALED_REPLAY_COMMIT, FROZEN_REVIEW_COMMIT, SEALED_REPLAY_TREE),
        ("admission", ADMISSION_COMMIT, SEALED_REPLAY_COMMIT, ADMISSION_TREE),
        ("manifest_closure_repair", CLOSURE_REPAIR_COMMIT, ADMISSION_COMMIT, CLOSURE_REPAIR_TREE),
    )
    rows = commit_topology.get("commits")
    require(isinstance(rows, list) and len(rows) == len(expected_commits), "receipt commit chain length mismatch")
    for row, (role, commit, parent, tree) in zip(rows, expected_commits, strict=True):
        require(
            isinstance(row, dict)
            and row.get("role") == role
            and row.get("commit") == commit
            and row.get("parent") == parent
            and row.get("tree") == tree,
            f"receipt commit identity mismatch: {role}",
        )

    historical = receipt.get("historical_declared_minus_committed")
    require(isinstance(historical, dict), "receipt historical closure section is absent")
    require(
        historical.get("status") == "PASS"
        and historical.get("passed") is True
        and historical.get("complete_missing_set") == topology["prior_complete_missing_set"]
        and historical.get("same_complete_five_path_set_at_frozen_and_immediate_parent") is True
        and historical.get("no_additional_declared_path_was_missing") is True,
        "receipt historical missing-set result mismatch",
    )
    expected_snapshots = {
        "frozen_candidate": {
            "commit": FROZEN_REVIEW_COMMIT,
            "manifest_sha256": INITIAL_MANIFEST_SHA256,
            "manifest_reference_count": 29,
            "committed_candidate_file_count_including_manifest": 25,
            "declared_minus_committed": topology["prior_complete_missing_set"],
        },
        "immediate_pre_repair_admission": {
            "commit": ADMISSION_COMMIT,
            "manifest_sha256": FINAL_MANIFEST_SHA256,
            "manifest_reference_count": 30,
            "committed_candidate_file_count_including_manifest": 26,
            "declared_minus_committed": topology["prior_complete_missing_set"],
        },
        "post_repair": {
            "commit": CLOSURE_REPAIR_COMMIT,
            "manifest_sha256": FINAL_MANIFEST_SHA256,
            "manifest_reference_count": 30,
            "committed_candidate_file_count_including_manifest": 31,
            "declared_minus_committed": [],
        },
    }
    snapshots = historical.get("snapshots")
    require(isinstance(snapshots, list) and len(snapshots) == 3, "receipt closure snapshots are incomplete")
    for snapshot in snapshots:
        require(isinstance(snapshot, dict), "receipt closure snapshot is not an object")
        expected = expected_snapshots.get(snapshot.get("role"))
        require(expected is not None, "receipt contains an unexpected closure snapshot")
        assert expected is not None
        for field, value in expected.items():
            require(snapshot.get(field) == value, f"receipt closure snapshot mismatch: {snapshot.get('role')}/{field}")
        require(
            snapshot.get("declared_minus_committed_count")
            == len(expected["declared_minus_committed"]),
            "receipt closure snapshot missing-count mismatch",
        )

    full_repair_paths = [f"{CANDIDATE_RELATIVE}/{path}" for path in CLOSURE_REPAIR_FILES]
    repair_diff = receipt.get("repair_diff")
    require(isinstance(repair_diff, dict), "receipt repair diff is absent")
    require(
        repair_diff.get("status") == "PASS"
        and repair_diff.get("passed") is True
        and repair_diff.get("whole_commit_changed_path_count") == 5
        and repair_diff.get("all_changes_are_additions") is True
        and repair_diff.get("added_paths") == full_repair_paths
        and repair_diff.get("modified_paths") == []
        and repair_diff.get("deleted_paths") == []
        and repair_diff.get("parent_candidate_entry_count") == 26
        and repair_diff.get("repair_candidate_entry_count") == 31
        and repair_diff.get("modified_preexisting_candidate_entries") == []
        and repair_diff.get("removed_preexisting_candidate_entries") == []
        and repair_diff.get("all_preexisting_candidate_entries_byte_and_mode_identical") is True
        and repair_diff.get("no_path_outside_the_five_file_repair_changed") is True,
        "receipt repair-diff result mismatch",
    )

    repaired_blobs = receipt.get("repaired_blobs")
    require(isinstance(repaired_blobs, dict), "receipt repaired-blob section is absent")
    require(
        repaired_blobs.get("status") == "PASS"
        and repaired_blobs.get("passed") is True
        and repaired_blobs.get("count") == 5
        and all(
            repaired_blobs.get(flag) is True
            for flag in (
                "all_absent_at_frozen_commit",
                "all_absent_at_admission_parent",
                "all_present_at_repair_commit",
                "all_mode_100644",
                "all_match_unchanged_final_manifest_hashes",
                "all_worktree_bytes_match_repair_commit",
            )
        ),
        "receipt repaired-blob flags are not passing",
    )
    blob_rows = repaired_blobs.get("files")
    require(isinstance(blob_rows, list) and len(blob_rows) == 5, "receipt repaired-blob inventory is incomplete")
    observed_paths: list[str] = []
    for row in blob_rows:
        require(isinstance(row, dict), "receipt repaired-blob row is not an object")
        path = row.get("path")
        require(path in CLOSURE_REPAIR_FILES, f"receipt has an unexpected repaired blob: {path!r}")
        assert isinstance(path, str)
        observed_paths.append(path)
        identity = CLOSURE_REPAIR_FILES[path]
        require(
            row.get("mode") == "100644"
            and row.get("git_blob") == identity["git_blob"]
            and row.get("bytes") == identity["bytes"]
            and row.get("sha256") == identity["sha256"]
            and row.get("manifest_hash_matches") is True,
            f"receipt repaired-blob identity mismatch: {path}",
        )
    require(observed_paths == list(CLOSURE_REPAIR_FILES), "receipt repaired-blob order or coverage mismatch")

    protected = receipt.get("protected_bytes_unchanged")
    require(isinstance(protected, dict), "receipt protected-byte section is absent")
    require(
        protected.get("status") == "PASS"
        and protected.get("passed") is True
        and protected.get("comparison") == f"{ADMISSION_COMMIT}..{CLOSURE_REPAIR_COMMIT}",
        "receipt protected-byte comparison mismatch",
    )
    preexisting = protected.get("preexisting_candidate_bytes")
    require(
        isinstance(preexisting, dict)
        and preexisting.get("parent_entry_count") == 26
        and preexisting.get("modified_count") == 0
        and preexisting.get("deleted_count") == 0
        and preexisting.get("all_identical") is True,
        "receipt pre-existing candidate-byte result mismatch",
    )

    protected_paths = (
        ("candidate_manifest", MANIFEST_RELATIVE),
        (
            "independent_replay_receipt",
            f"{CANDIDATE_RELATIVE}/{REVIEW_CANDIDATE_RELATIVE}",
        ),
    )
    for field, path in protected_paths:
        row = protected.get(field)
        require(isinstance(row, dict) and row.get("path") == path, f"receipt protected path mismatch: {field}")
        parent_data = commit_bytes(root, ADMISSION_COMMIT, path)
        repair_data = commit_bytes(root, CLOSURE_REPAIR_COMMIT, path)
        parent_blob = git_text(root, "rev-parse", f"{ADMISSION_COMMIT}:{path}")
        repair_blob = git_text(root, "rev-parse", f"{CLOSURE_REPAIR_COMMIT}:{path}")
        require(
            parent_data == repair_data
            and row.get("parent_blob") == parent_blob
            and row.get("repair_blob") == repair_blob
            and row.get("bytes") == len(parent_data)
            and row.get("sha256") == sha256(parent_data)
            and row.get("byte_identical") is True,
            f"receipt protected-byte identity mismatch: {path}",
        )

    registry_rows = protected.get("registries")
    require(isinstance(registry_rows, list) and len(registry_rows) == 4, "receipt protected registries are incomplete")
    expected_registry_paths = [
        "ai-integrated/registry/leases.json",
        "ai-integrated/registry/locales.json",
        "ai-integrated/registry/overlays.json",
        "ai-integrated/registry/releases.json",
    ]
    require([row.get("path") for row in registry_rows if isinstance(row, dict)] == expected_registry_paths, "receipt protected registry inventory mismatch")
    for row in registry_rows:
        assert isinstance(row, dict)
        path = row["path"]
        parent_data = commit_bytes(root, ADMISSION_COMMIT, path)
        repair_data = commit_bytes(root, CLOSURE_REPAIR_COMMIT, path)
        require(
            parent_data == repair_data
            and row.get("parent_blob") == git_text(root, "rev-parse", f"{ADMISSION_COMMIT}:{path}")
            and row.get("repair_blob") == git_text(root, "rev-parse", f"{CLOSURE_REPAIR_COMMIT}:{path}")
            and row.get("bytes") == len(parent_data)
            and row.get("sha256") == sha256(parent_data)
            and row.get("byte_identical") is True,
            f"receipt protected registry mismatch: {path}",
        )
    require(protected.get("all_registry_bytes_identical") is True, "receipt registry-preservation flag is false")
    derived = protected.get("derived_tex")
    require(isinstance(derived, dict) and derived.get("path") == SOURCE_PATH, "receipt protected derived.tex row is absent")
    admission_source = commit_bytes(root, ADMISSION_COMMIT, SOURCE_PATH)
    repair_source = commit_bytes(root, CLOSURE_REPAIR_COMMIT, SOURCE_PATH)
    require(
        admission_source == repair_source
        and derived.get("parent_blob") == git_text(root, "rev-parse", f"{ADMISSION_COMMIT}:{SOURCE_PATH}")
        and derived.get("repair_blob") == git_text(root, "rev-parse", f"{CLOSURE_REPAIR_COMMIT}:{SOURCE_PATH}")
        and derived.get("bytes") == len(admission_source)
        and derived.get("sha256") == sha256(admission_source)
        and derived.get("byte_identical") is True,
        "receipt protected derived.tex identity mismatch",
    )

    closure = receipt.get("current_manifest_closure")
    require(isinstance(closure, dict), "receipt current manifest-closure section is absent")
    require(
        closure.get("status") == "PASS"
        and closure.get("passed") is True
        and closure.get("commit") == CLOSURE_REPAIR_COMMIT
        and closure.get("manifest_path") == MANIFEST_RELATIVE
        and closure.get("manifest_sha256") == FINAL_MANIFEST_SHA256
        and closure.get("reference_count") == 30
        and closure.get("all_references_committed") is True
        and closure.get("all_committed_bytes_hash_correct") is True
        and closure.get("declared_minus_committed") == []
        and closure.get("checker_passed") is True
        and closure.get("candidate_verifier_passed") is True,
        "receipt current manifest-closure result mismatch",
    )
    final_manifest_data = commit_bytes(root, CLOSURE_REPAIR_COMMIT, MANIFEST_RELATIVE)
    require(
        closure.get("manifest_bytes") == len(final_manifest_data)
        and closure.get("manifest_git_blob")
        == git_text(root, "rev-parse", f"{CLOSURE_REPAIR_COMMIT}:{MANIFEST_RELATIVE}"),
        "receipt current manifest identity mismatch",
    )
    closure_rows = closure.get("references")
    require(isinstance(closure_rows, list) and len(closure_rows) == 30, "receipt current reference inventory is incomplete")
    closure_map: dict[str, dict[str, Any]] = {}
    for row in closure_rows:
        require(isinstance(row, dict) and isinstance(row.get("path"), str), "receipt current reference row is invalid")
        path = row["path"]
        require(path not in closure_map, f"receipt repeats a current reference: {path}")
        closure_map[path] = row
    references = candidate["manifest_references"]
    require(set(closure_map) == set(references), "receipt current reference path set differs from final manifest")
    for path, expected_hash in references.items():
        row = closure_map[path]
        full_path = f"{CANDIDATE_RELATIVE}/{path}"
        data = commit_bytes(root, CLOSURE_REPAIR_COMMIT, full_path)
        require(
            row.get("bytes") == len(data)
            and row.get("sha256") == expected_hash == sha256(data)
            and row.get("git_blob") == git_text(root, "rev-parse", f"{CLOSURE_REPAIR_COMMIT}:{full_path}")
            and row.get("committed") is True
            and row.get("hash_matches") is True,
            f"receipt current reference identity mismatch: {path}",
        )

    commands = receipt.get("commands_and_results")
    require(
        isinstance(commands, list)
        and len(commands) == 9
        and all(
            isinstance(row, dict)
            and row.get("exit_code") == 0
            and row.get("passed") is True
            for row in commands
        ),
        "closure-correction command results are incomplete or not passing",
    )
    return {
        "path": CORRECTION_RECEIPT_RELATIVE,
        "bytes": len(receipt_raw),
        "sha256": sha256(receipt_raw),
        "schema": receipt["schema"],
        "audited_at_utc": audited_at.isoformat().replace("+00:00", "Z"),
        "repaired_file_count": 5,
        "manifest_reference_count": 30,
    }


def validate_registries(
    root: Path, candidate: dict[str, Any]
) -> dict[str, Any]:
    overlays = load_json_bytes(
        commit_bytes(root, "HEAD", OVERLAYS_RELATIVE), "overlay registry"
    )
    leases = load_json_bytes(
        commit_bytes(root, "HEAD", LEASES_RELATIVE), "lease registry"
    )
    require(overlays.get("schema") == OVERLAY_REGISTRY_SCHEMA, "overlay registry schema mismatch")
    require(leases.get("schema") == LEASE_REGISTRY_SCHEMA, "lease registry schema mismatch")

    entries = overlays.get("registered_entries")
    require(isinstance(entries, list), "overlay registry has no entries")
    matches = [
        row
        for row in entries
        if isinstance(row, dict) and row.get("id") == CANDIDATE_ID
    ]
    require(len(matches) == 1, "candidate is not uniquely admitted in the overlay registry")
    entry = matches[0]
    assert isinstance(entry, dict)
    expected_entry = {
        "namespace": NAMESPACE,
        "writer": WRITER_TASK,
        "source_commit": OFFICIAL_COMMIT,
        "source_tree": OFFICIAL_TREE,
        "manifest_sha256": candidate["manifest_sha256"],
        "stable_ids": list(UNIT_IDS),
        "review_receipt": REVIEW_REGISTRY_RELATIVE,
    }
    for field, expected in expected_entry.items():
        observed = entry.get(field)
        if field == "manifest_sha256" and isinstance(observed, str):
            observed = observed.upper()
        require(observed == expected, f"overlay admission mismatch: {field}")
    rights = entry.get("rights_state")
    require(isinstance(rights, str) and rights.strip(), "overlay admission has no rights statement")
    assert isinstance(rights, str)
    rights_lower = rights.lower()
    no_relicense = re.search(
        r"(?:no|not|does not|do not)[^.]{0,120}relicens", rights_lower
    )
    no_official_review = re.search(
        r"(?:no|not)[^.]{0,220}review[^.]{0,80}approv[^.]{0,80}affiliat[^.]{0,80}endorse",
        rights_lower,
    )
    require(
        "independent" in rights_lower
        and (
            "gfdl" in rights_lower
            or "gnu free documentation license" in rights_lower
        )
        and no_relicense is not None
        and "stacks project" in rights_lower
        and no_official_review is not None,
        "overlay rights statement does not preserve the approved rights boundary",
    )
    admitted_at = require_utc(entry.get("admitted_at_utc"), "overlay admission time")

    registered_ids: list[str] = []
    for row in entries:
        require(isinstance(row, dict), "overlay registry contains a non-object entry")
        ids = row.get("stable_ids")
        if isinstance(ids, str):
            ids = ids.split()
        require(
            isinstance(ids, list)
            and ids
            and all(isinstance(value, str) and value for value in ids),
            "overlay registry contains an invalid stable-ID inventory",
        )
        registered_ids.extend(ids)
    require(
        len(registered_ids) == len(set(registered_ids)),
        "overlay registry contains duplicate stable IDs",
    )

    events = leases.get("events")
    require(isinstance(events, list), "lease registry has no events")
    event_ids = [row.get("event_id") for row in events if isinstance(row, dict)]
    require(
        len(event_ids) == len(events)
        and all(isinstance(value, str) and value for value in event_ids)
        and len(event_ids) == len(set(event_ids)),
        "lease registry event IDs are invalid or repeated",
    )
    related = [
        (index, row)
        for index, row in enumerate(events)
        if isinstance(row, dict) and row.get("lease_id") == LEASE_ID
    ]
    require(len(related) == 2, "lease lifecycle must contain exactly issue and release events")
    issued_matches = [item for item in related if item[1].get("event") == "issued"]
    released_matches = [item for item in related if item[1].get("event") == "released"]
    require(
        len(issued_matches) == len(released_matches) == 1,
        "lease lifecycle lacks a unique issue or release event",
    )
    issued_index, issued = issued_matches[0]
    released_index, released = released_matches[0]
    require(issued_index < released_index, "lease release precedes its issuance")
    common = {
        "lease_id": LEASE_ID,
        "namespace": NAMESPACE,
        "candidate_path": f"candidates/{NAMESPACE}",
        "writer_task": WRITER_TASK,
        "upstream_commit": OFFICIAL_COMMIT,
        "upstream_tree": OFFICIAL_TREE,
        "writer_contract": "candidates/CONTRACT.md",
    }
    for field, expected in common.items():
        require(issued.get(field) == expected, f"lease issue mismatch: {field}")
        require(released.get(field) == expected, f"lease release mismatch: {field}")
    require(issued.get("state") == "active", "issued lease is not active")
    require(released.get("state") == "released", "lease is not released")
    require(
        released.get("supersedes_event_id") == issued.get("event_id"),
        "lease release does not supersede its exact issue event",
    )
    issued_at = require_utc(issued.get("issued_at_utc"), "lease issue time")
    release_time_value = released.get("released_at_utc", released.get("issued_at_utc"))
    released_at = require_utc(release_time_value, "lease release time")
    require(issued_at <= released_at, "lease release time precedes issuance")
    require(released_at <= admitted_at, "overlay admission precedes lease release")

    return {
        "overlay_entry": entry,
        "overlay_count": len(entries),
        "registered_stable_id_count": len(registered_ids),
        "issued_event_id": issued["event_id"],
        "released_event_id": released["event_id"],
        "released_at_utc": release_time_value,
    }


def validate_composition(
    root: Path, candidate: dict[str, Any]
) -> dict[str, Any]:
    references = candidate["manifest_references"]
    assert isinstance(references, dict)
    composition_relative = "composition.jsonl"
    payload_relative = "payload/fragments/derived-homotopy-category-abelian-split.tex"
    operation_raw = commit_bytes(
        root, "HEAD", f"{CANDIDATE_RELATIVE}/{composition_relative}"
    )
    payload = commit_bytes(root, "HEAD", f"{CANDIDATE_RELATIVE}/{payload_relative}")
    require(
        references.get(composition_relative) == sha256(operation_raw),
        "manifest/composition binding mismatch",
    )
    require(
        references.get(payload_relative) == sha256(payload),
        "manifest/payload binding mismatch",
    )
    operation = load_single_jsonl_bytes(operation_raw, "composition ledger")
    require(operation.get("schema") == COMPOSITION_SCHEMA, "composition schema mismatch")
    require(operation.get("operation_id") == OPERATION_ID, "composition operation ID mismatch")
    require(
        operation.get("operation") == "insert_bytes"
        and operation.get("mode") == "insertion_only",
        "composition is not insertion-only",
    )
    target = operation.get("target")
    insertion = operation.get("insertion")
    payload_record = operation.get("payload")
    constraints = operation.get("constraints")
    require(
        all(isinstance(value, dict) for value in (target, insertion, payload_record, constraints)),
        "composition contract is incomplete",
    )
    assert isinstance(target, dict)
    assert isinstance(insertion, dict)
    assert isinstance(payload_record, dict)
    assert isinstance(constraints, dict)
    require(
        constraints
        == {
            "existing_target_bytes_changed": 0,
            "delete_bytes": 0,
            "replace_bytes": 0,
            "insert_payload_once": True,
        },
        "composition constraints are not strictly insertion-only",
    )
    require(target.get("path") == SOURCE_PATH, "composition target is not derived.tex")
    composition_base = candidate["config"].get("composition_base")
    require(isinstance(composition_base, dict), "candidate composition base is absent")
    require(
        all(
            target.get(field) == composition_base.get(field)
            for field in ("repository", "commit", "tree")
        ),
        "composition contract differs from the candidate's recorded base",
    )
    frozen_commit = target.get("commit")
    require(
        isinstance(frozen_commit, str) and re.fullmatch(r"[0-9a-f]{40}", frozen_commit),
        "recorded composition base commit is invalid",
    )
    assert isinstance(frozen_commit, str)
    require(
        git_text(root, "rev-parse", f"{frozen_commit}^{{tree}}") == target.get("tree"),
        "recorded composition base tree mismatch",
    )
    base = commit_bytes(root, frozen_commit, SOURCE_PATH)
    require(
        git_text(root, "rev-parse", f"{frozen_commit}:{SOURCE_PATH}") == target.get("blob"),
        "recorded composition base blob mismatch",
    )
    require(len(base) == target.get("bytes"), "recorded composition base byte count mismatch")
    require(
        sha256(base) == require_sha(target.get("preimage_sha256"), "base preimage"),
        "recorded composition base hash mismatch",
    )
    require(payload_record.get("path") == payload_relative, "composition payload path mismatch")
    require(payload_record.get("proposed_label") == PROPOSED_LABEL, "proposed label mismatch")
    require(len(payload) == payload_record.get("bytes"), "payload byte count mismatch")
    payload_sha = sha256(payload)
    require(
        payload_sha == require_sha(payload_record.get("sha256"), "payload"),
        "payload hash mismatch",
    )
    require(b"\r" not in payload and not payload.startswith(b"\xef\xbb\xbf"), "payload is not BOM-free LF UTF-8")
    payload.decode("utf-8", errors="strict")

    integer_fields = (
        "context_start_byte",
        "context_end_byte_exclusive",
        "byte_offset",
        "context_bytes",
        "before_context_bytes",
        "after_context_bytes",
    )
    require(
        all(type(insertion.get(field)) is int for field in integer_fields),
        "composition offsets are invalid",
    )
    start = insertion["context_start_byte"]
    end = insertion["context_end_byte_exclusive"]
    offset = insertion["byte_offset"]
    require(0 <= start <= offset <= end <= len(base), "composition offsets are out of range")
    context = base[start:end]
    before = base[start:offset]
    after = base[offset:end]
    require(len(context) == insertion["context_bytes"], "context byte count mismatch")
    require(len(before) == insertion["before_context_bytes"], "before-context byte count mismatch")
    require(len(after) == insertion["after_context_bytes"], "after-context byte count mismatch")
    require(
        sha256(context) == require_sha(insertion.get("context_sha256"), "context"),
        "context hash mismatch",
    )
    require(
        sha256(before)
        == require_sha(insertion.get("before_context_sha256"), "before context"),
        "before-context hash mismatch",
    )
    require(
        sha256(after)
        == require_sha(insertion.get("after_context_sha256"), "after context"),
        "after-context hash mismatch",
    )
    require(
        insertion.get("required_anchor_occurrences") == 1 and base.count(context) == 1,
        "recorded insertion context is not unique",
    )
    require(
        insertion.get("after_complete_proof_of_label") == AFTER_PROOF_LABEL,
        "unexpected completed-proof anchor label",
    )
    require(
        insertion.get("before_environment_for_label") == BEFORE_ENVIRONMENT_LABEL,
        "unexpected following-environment anchor label",
    )
    after_token = f"\\label{{{AFTER_PROOF_LABEL}}}".encode("ascii")
    before_token = f"\\label{{{BEFORE_ENVIRONMENT_LABEL}}}".encode("ascii")
    require(
        base.count(after_token) == 1 and base.count(before_token) == 1,
        "composition anchor labels are not unique in the base",
    )
    require(
        base.index(after_token) < start <= offset < base.index(before_token) < end,
        "composition anchor labels do not bracket the insertion",
    )
    require(
        base[:offset].endswith(b"\\end{proof}\n\n")
        and base[offset:].startswith(b"\\begin{remark}\n" + before_token + b"\n"),
        "insertion is not exactly between the completed proof and following remark",
    )

    label_token = f"\\label{{{PROPOSED_LABEL}}}".encode("ascii")
    require(base.count(payload) == 0, "payload already occurs in the recorded base")
    require(base.count(label_token) == 0, "proposed label already occurs in the recorded base")
    require(payload.count(label_token) == 1, "payload does not define the proposed label exactly once")
    projected = base[:offset] + payload + base[offset:]
    require(len(projected) == target.get("postimage_bytes"), "recorded postimage byte count mismatch")
    require(
        sha256(projected) == require_sha(target.get("postimage_sha256"), "postimage"),
        "recorded postimage hash mismatch",
    )

    current = commit_bytes(root, "HEAD", SOURCE_PATH)
    require(
        current == projected,
        "current committed derived.tex is not the exact recorded insertion projection",
    )
    require(current.count(payload) == 1, "current derived.tex does not contain the payload exactly once")
    require(current.count(label_token) == 1, "current derived.tex does not contain the proposed label exactly once")
    require(current[:offset] == base[:offset], "bytes before the insertion changed")
    require(
        current[offset + len(payload) :] == base[offset:],
        "bytes after the insertion changed",
    )
    base_labels = Counter(LABEL_PATTERN.findall(base.decode("utf-8", errors="strict")))
    current_labels = Counter(LABEL_PATTERN.findall(current.decode("utf-8", errors="strict")))
    expected_labels = base_labels.copy()
    expected_labels[PROPOSED_LABEL] += 1
    require(
        current_labels == expected_labels,
        "derived.tex label inventory changed by more than the proposed label",
    )
    return {
        "operation_id": OPERATION_ID,
        "source": SOURCE_PATH,
        "base_commit": frozen_commit,
        "base_tree": target["tree"],
        "base_blob": target["blob"],
        "base_bytes": len(base),
        "base_sha256": sha256(base),
        "context_bytes": len(context),
        "context_sha256": sha256(context),
        "insertion_offset": offset,
        "payload_bytes": len(payload),
        "payload_sha256": payload_sha,
        "composed_blob": git_text(root, "rev-parse", f"HEAD:{SOURCE_PATH}"),
        "composed_bytes": len(current),
        "composed_sha256": sha256(current),
        "payload_occurrences": current.count(payload),
        "proposed_label_occurrences": current.count(label_token),
        "preexisting_bytes_unchanged": True,
    }


def validate_reference_closure(root: Path) -> dict[str, Any]:
    payload_path = (
        f"{CANDIDATE_RELATIVE}/payload/fragments/"
        "derived-homotopy-category-abelian-split.tex"
    )
    payload_text = commit_bytes(root, "HEAD", payload_path).decode(
        "utf-8", errors="strict"
    )
    references = frozenset(REFERENCE_PATTERN.findall(payload_text))
    require(references == EXPECTED_REFERENCES, "payload reference inventory changed")

    top_level = git_text(root, "ls-tree", "--name-only", "HEAD").splitlines()
    tex_paths = sorted(path for path in top_level if path.endswith(".tex"))
    require(SOURCE_PATH in tex_paths, "derived.tex is absent from the committed root")
    canonical_labels: Counter[str] = Counter()
    providers: dict[str, list[str]] = {}
    for path in tex_paths:
        text = commit_bytes(root, "HEAD", path).decode("utf-8", errors="strict")
        stem = Path(path).stem
        for local in LABEL_PATTERN.findall(text):
            canonical = local if path == SOURCE_PATH else f"{stem}-{local}"
            canonical_labels[canonical] += 1
            if canonical in references:
                providers.setdefault(canonical, []).append(path)
    missing = sorted(reference for reference in references if canonical_labels[reference] == 0)
    ambiguous = sorted(reference for reference in references if canonical_labels[reference] != 1)
    require(not missing, f"payload has unresolved references: {missing}")
    require(not ambiguous, f"payload references are not uniquely provided: {ambiguous}")
    return {
        "reference_count": len(references),
        "references": sorted(references),
        "providers": {key: providers[key] for key in sorted(providers)},
    }


def validate(root: Path) -> dict[str, Any]:
    root = root.resolve()
    require((root / ".git").exists(), "root is not a Git worktree")
    candidate_path = root / CANDIDATE_RELATIVE
    require(candidate_path.is_dir(), "bounded candidate directory is absent")

    stage = "candidate_tools"
    try:
        verifier = run_candidate_tool(
            candidate_path,
            "verify.py",
            {"candidate_id": CANDIDATE_ID, "source_units": len(UNIT_IDS)},
        )
        checker = run_candidate_tool(
            candidate_path,
            "check-manifest.py",
            {"stable_units": len(UNIT_IDS)},
        )

        stage = "candidate_lifecycle"
        local = validate_local_final_lifecycle(candidate_path)

        stage = "committed_scope"
        validator_identity = require_clean_committed_scope(root)
        committed = validate_committed_candidate(root, local)

        stage = "manifest_closure_correction"
        closure_correction = validate_closure_repair_topology(root, committed)
        correction_receipt = validate_closure_correction_receipt(
            root, committed, closure_correction
        )

        stage = "admission_lifecycle"
        registries = validate_registries(root, committed)

        stage = "composition"
        composition = validate_composition(root, committed)

        stage = "reference_closure"
        references = validate_reference_closure(root)
    except (
        OSError,
        UnicodeError,
        ValueError,
        KeyError,
        TypeError,
        subprocess.TimeoutExpired,
        ValidationError,
    ) as exc:
        exc.add_note(stage)
        raise

    return {
        "schema": REPORT_SCHEMA,
        "status": "PASS",
        "passed": True,
        "candidate_id": CANDIDATE_ID,
        "namespace": NAMESPACE,
        "lease_id": LEASE_ID,
        "candidate_tools": {
            "verify": {
                "passed": verifier["passed"],
                "source_units": verifier["source_units"],
                "operation_id": verifier.get("operation_id"),
                "reference_count": verifier.get("reference_count"),
            },
            "check_manifest": {
                "passed": checker["passed"],
                "stable_units": checker["stable_units"],
                "references": checker.get("references"),
            },
        },
        "candidate": {
            "tree": committed["candidate_tree"],
            "manifest_sha256": committed["manifest_sha256"],
            "manifest_reference_count": len(committed["manifest_references"]),
            "review_sha256": committed["review_sha256"],
            "review_checks": len(
                committed["review"]["commands_and_check_results"]
            ),
        },
        "manifest_closure_correction": {
            **closure_correction,
            "corrective_receipt": correction_receipt,
        },
        "registries": {
            "overlay_count": registries["overlay_count"],
            "registered_stable_id_count": registries[
                "registered_stable_id_count"
            ],
            "issued_event_id": registries["issued_event_id"],
            "released_event_id": registries["released_event_id"],
            "released_at_utc": registries["released_at_utc"],
        },
        "composition": composition,
        "reference_closure": references,
        "validator": validator_identity,
        "read_only": True,
        "tex_run": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository worktree root (default: parent of tools/)",
    )
    args = parser.parse_args(argv)
    try:
        report = validate(args.root)
    except (
        OSError,
        UnicodeError,
        ValueError,
        KeyError,
        TypeError,
        subprocess.TimeoutExpired,
        ValidationError,
    ) as exc:
        notes = getattr(exc, "__notes__", [])
        failed_stage = notes[-1] if notes else "startup"
        report = {
            "schema": REPORT_SCHEMA,
            "status": "FAIL",
            "passed": False,
            "candidate_id": CANDIDATE_ID,
            "failed_stage": failed_stage,
            "error": str(exc),
            "read_only": True,
            "tex_run": False,
        }
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
