from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "candidate.manifest.json"
SHA256_RE = re.compile(r"[0-9A-F]{64}")
SINGLED = {
    "stable_unit_manifest": "stable-units.json",
    "source_map": "source-map.jsonl",
    "decision_ledger": "decisions.jsonl",
    "rejection_ledger": "rejections.jsonl",
    "formula_diagram_inventory": "formula-diagram-inventory.json",
}


class ManifestError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ManifestError(message)


def ai_root() -> Path:
    for directory in ROOT.parents:
        if (
            (directory / "schemas" / "candidate-manifest.schema.json").is_file()
            and (directory / "registry" / "leases.json").is_file()
            and (directory / "upstream" / "stacks.lock.json").is_file()
        ):
            return directory.resolve()
    raise ManifestError("cannot resolve the bounded ai-integrated root")


AI_ROOT = ai_root()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ManifestError(f"cannot parse {path.name}: {exc}") from exc
    require(isinstance(value, dict), f"{path.name} must contain one JSON object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise ManifestError(f"cannot read {path.name}: {exc}") from exc
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ManifestError(f"invalid JSONL at {path.name}:{number}: {exc}") from exc
        require(isinstance(row, dict), f"non-object JSONL row at {path.name}:{number}")
        rows.append(row)
    return rows


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def validate_datetime(value: Any, locus: str) -> None:
    require(isinstance(value, str) and value, f"{locus} is empty")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ManifestError(f"{locus} is not ISO-8601") from exc
    require(parsed.tzinfo is not None, f"{locus} lacks a timezone")


def validate_evidence(row: Any, locus: str) -> dict[str, str]:
    require(isinstance(row, dict), f"{locus} is not an object")
    allowed = {"path", "bytes", "sha256", "source_url", "accessed_at_utc"}
    require({"path", "sha256"} <= set(row) <= allowed, f"{locus} has missing or extra fields")
    logical = row.get("path")
    digest = row.get("sha256")
    require(isinstance(logical, str) and logical and "\\" not in logical, f"{locus}.path is invalid")
    require(not Path(logical).is_absolute(), f"{locus}.path is absolute")
    require(isinstance(digest, str) and SHA256_RE.fullmatch(digest) is not None, f"{locus}.sha256 is invalid")
    if "accessed_at_utc" in row:
        validate_datetime(row["accessed_at_utc"], f"{locus}.accessed_at_utc")
    path = (ROOT / logical).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ManifestError(f"{locus}.path escapes the candidate") from exc
    require(path != MANIFEST.resolve() and path.is_file(), f"manifest reference is absent or recursive: {logical}")
    if "bytes" in row:
        require(row["bytes"] == path.stat().st_size, f"manifest byte count mismatch: {logical}")
    require(sha256(path) == digest, f"manifest hash mismatch: {logical}")
    return {"path": logical, "sha256": digest}


def public_files() -> list[str]:
    files: list[str] = []
    stack = [ROOT]
    while stack:
        directory = stack.pop()
        with os.scandir(directory) as entries:
            ordered = sorted(entries, key=lambda entry: entry.name)
        for entry in ordered:
            if entry.is_dir(follow_symlinks=False):
                if entry.name in {".work", ".git", "__pycache__"}:
                    continue
                stack.append(Path(entry.path))
            elif entry.is_file(follow_symlinks=False):
                path = Path(entry.path)
                if path.name != MANIFEST.name:
                    files.append(path.relative_to(ROOT).as_posix())
    return sorted(files)


def main() -> int:
    try:
        manifest = load_json(MANIFEST)
        config = load_json(ROOT / "candidate.config.json")
        pointer = load_json(ROOT / "LEASE.json")
        stable = load_json(ROOT / "stable-units.json")
        source_rows = load_jsonl(ROOT / "source-map.jsonl")
        inventory = load_json(ROOT / "formula-diagram-inventory.json")

        required = {
            "schema", "candidate_id", "lease_id", "namespace", "writer_task", "upstream",
            "source_authorities", "source_closure", "stable_unit_manifest", "source_map",
            "decision_ledger", "rejection_ledger", "formula_diagram_inventory", "builds",
            "rights_state", "review_state", "independent_replay", "unresolved_defects",
            "stop_conditions", "generated_at_utc",
        }
        require(frozenset(manifest) in {frozenset(required), frozenset(required | {"$schema"})}, "manifest top-level shape is invalid")
        require(manifest["schema"] == "mathematics-commons-stacks-candidate-manifest/v1", "wrong manifest schema")
        expected_schema = Path(os.path.relpath(AI_ROOT / "schemas" / "candidate-manifest.schema.json", ROOT)).as_posix()
        if "$schema" in manifest:
            require(manifest["$schema"] == expected_schema, "manifest uses the wrong local schema path")
        patterns = {
            "candidate_id": r"[a-z0-9][a-z0-9._-]*",
            "lease_id": r"stacks-lease-[0-9]{6}-[a-z0-9-]+",
            "namespace": r"commons/stacks/[a-z0-9][a-z0-9/-]*",
            "writer_task": r"[0-9a-f-]{36}",
        }
        for field, pattern in patterns.items():
            require(isinstance(manifest[field], str) and re.fullmatch(pattern, manifest[field]) is not None, f"invalid manifest {field}")
        validate_datetime(manifest["generated_at_utc"], "generated_at_utc")
        require(isinstance(manifest["rights_state"], str) and manifest["rights_state"].strip(), "rights state is empty")
        require(isinstance(manifest["unresolved_defects"], list) and all(isinstance(item, str) for item in manifest["unresolved_defects"]), "unresolved defects is invalid")
        require(isinstance(manifest["stop_conditions"], list) and manifest["stop_conditions"] and all(isinstance(item, str) for item in manifest["stop_conditions"]), "stop conditions are invalid")

        expected_ids = config.get("expected_unit_ids")
        require(isinstance(expected_ids, list) and expected_ids, "config has no expected stable-unit IDs")
        count = len(expected_ids)
        units = stable.get("units")
        require(isinstance(units, list) and stable.get("unit_count") == len(units) == count, "stable-unit count mismatch")
        unit_ids = [row.get("id") for row in units]
        require(unit_ids == expected_ids and len(unit_ids) == len(set(unit_ids)), "stable-unit identity/order mismatch")
        require([row.get("unit_id") for row in source_rows] == unit_ids, "source map does not close over stable units")
        require(inventory.get("unit_count") == inventory.get("classified_unit_count") == count, "formula inventory count mismatch")
        closure = manifest["source_closure"]
        require(isinstance(closure, dict) and set(closure) == {"enumerated", "expected_units", "manifested_units", "complete"}, "source closure shape is invalid")
        require(closure == {"enumerated": True, "expected_units": count, "manifested_units": count, "complete": True}, "source closure is incomplete")

        upstream = manifest["upstream"]
        require(isinstance(upstream, dict) and set(upstream) == {"lock", "commit", "tree"}, "upstream object is invalid")
        require(upstream["lock"] == config["upstream"]["lock"] == "upstream/stacks.lock.json", "upstream lock mismatch")
        for field in ("commit", "tree"):
            require(upstream[field] == config["upstream"][field] and re.fullmatch(r"[0-9a-f]{40}", upstream[field]) is not None, f"upstream {field} mismatch")
        registry = load_json(AI_ROOT / pointer["lease_registry"])
        events = [row for row in registry.get("events", []) if isinstance(row, dict) and row.get("lease_id") == pointer.get("lease_id")]
        issued = next((row for row in events if row.get("event") == "issued"), None)
        require(issued is not None and events[-1].get("state") in {"active", "released"}, "lease is absent or invalid")
        require(issued.get("candidate_path") == ROOT.relative_to(AI_ROOT).as_posix(), "lease candidate path mismatch")
        for field in ("lease_id", "namespace", "writer_task"):
            require(manifest[field] == config[field] == pointer[field] == issued[field], f"identity mismatch: {field}")
            if field in events[-1]:
                require(events[-1][field] == manifest[field], f"terminal lease event mismatch: {field}")
        require(manifest["candidate_id"] == config["candidate_id"], "candidate ID mismatch")
        lock = load_json(AI_ROOT / "upstream" / "stacks.lock.json")
        require(upstream["commit"] == issued.get("upstream_commit") == lock.get("commit"), "upstream commit/lease mismatch")
        require(upstream["tree"] == issued.get("upstream_tree") == lock.get("tree"), "upstream tree/lease mismatch")

        references: list[dict[str, str]] = []
        for key in ("source_authorities", "builds"):
            rows = manifest[key]
            require(isinstance(rows, list) and rows, f"{key} is empty")
            references.extend(validate_evidence(row, f"{key}[{index}]") for index, row in enumerate(rows))
        require(all(row["path"].startswith("authority/") for row in manifest["source_authorities"]), "source-authority classification mismatch")
        require(all(not row["path"].startswith("authority/") for row in manifest["builds"]), "build classification includes authority")
        for key, expected in SINGLED.items():
            require(manifest[key].get("path") == expected, f"{key} points to the wrong file")
            references.append(validate_evidence(manifest[key], key))
        referenced = [row["path"] for row in references]
        require(len(referenced) == len(set(referenced)), "manifest repeats a file")
        actual = public_files()
        require(sorted(referenced) == actual, f"manifest file closure mismatch; unreferenced={sorted(set(actual)-set(referenced))}; nonexistent={sorted(set(referenced)-set(actual))}")
        for required_path in ("builds/build-receipt.json", "builds/validation.json", "builds/visual-qa.json", "builds/tex-mutex.json"):
            require(required_path in referenced, f"manifest omits required receipt: {required_path}")

        replay_path = ROOT / "replay" / "independent-review.json"
        if replay_path.exists():
            replay = load_json(replay_path)
            passed = replay.get("passed") is True and replay.get("status") == "PASS"
            require(manifest["review_state"] == config.get("review_state") == "performed", "present replay lacks performed review state")
            require(manifest["independent_replay"] == config.get("independent_replay") == ("passed" if passed else "failed"), "replay lifecycle mismatch")
            require((not passed) or manifest["unresolved_defects"] == [], "passing replay leaves unresolved defects")
        else:
            require(manifest["review_state"] == config.get("review_state") == "partial", "absent replay review state mismatch")
            require(manifest["independent_replay"] == config.get("independent_replay") == "not_performed", "absent replay is overstated")
            require(bool(manifest["unresolved_defects"]), "absent replay is not recorded as unresolved")

        print(json.dumps({"passed": True, "references": len(referenced), "stable_units": count, "manifest_sha256": sha256(MANIFEST)}, sort_keys=True))
        return 0
    except (ManifestError, OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"MANIFEST CHECK FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
