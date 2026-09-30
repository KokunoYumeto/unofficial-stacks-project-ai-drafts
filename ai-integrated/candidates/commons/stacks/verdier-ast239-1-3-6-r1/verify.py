from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
SHA256_RE = re.compile(r"[0-9A-F]{64}")


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def repo_root() -> Path:
    for directory in ROOT.parents:
        if (
            (directory / "derived.tex").is_file()
            and (directory / "ai-integrated" / "registry" / "leases.json").is_file()
            and (directory / "ai-integrated" / "upstream" / "stacks.lock.json").is_file()
        ):
            return directory.resolve()
    raise VerificationError("cannot resolve the bounded repository root")


REPO = repo_root()
AI_ROOT = REPO / "ai-integrated"


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError(f"cannot parse {path.name}: {exc}") from exc
    require(isinstance(value, dict), f"{path.name} must contain one JSON object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise VerificationError(f"cannot read {path.name}: {exc}") from exc
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise VerificationError(f"invalid JSONL at {path.name}:{number}: {exc}") from exc
        require(isinstance(value, dict), f"non-object JSONL row at {path.name}:{number}")
        rows.append(value)
    return rows


def sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def git_bytes(*args: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(REPO), *args],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise VerificationError(f"bounded git query failed: {detail}")
    return completed.stdout


def git_text(*args: str) -> str:
    return git_bytes(*args).decode("utf-8", errors="strict").strip()


def validate_authority(config: dict[str, Any]) -> None:
    lock_rel = config.get("authority_lock")
    require(lock_rel == "authority/authority.lock.json", "unexpected authority-lock path")
    lock = load_json(ROOT / lock_rel)
    authority = lock.get("authority")
    require(isinstance(authority, dict), "authority lock has no authority object")
    authority_path = (
        Path.home()
        / "Documents"
        / "Papors"
        / "OS"
        / authority.get("file_name", "")
    )
    require(authority_path.is_file(), "frozen authority PDF is absent")
    require(authority_path.stat().st_size == authority.get("bytes"), "authority PDF byte count mismatch")
    require(sha_file(authority_path) == authority.get("sha256"), "authority PDF hash mismatch")
    pdfinfo = subprocess.run(
        ["pdfinfo", str(authority_path)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(pdfinfo.returncode == 0, "pdfinfo could not inspect the authority PDF")
    match = re.search(rb"(?m)^Pages:\s+(\d+)\s*$", pdfinfo.stdout)
    require(match is not None, "pdfinfo did not report an authority page count")
    require(int(match.group(1)) == authority.get("physical_pages"), "authority PDF page count mismatch")

    project = lock.get("source_project")
    require(isinstance(project, dict), "authority lock has no source-project object")
    relative_root = project.get("workspace_relative_root")
    require(isinstance(relative_root, str) and relative_root, "source-project root is empty")
    require("\\" not in relative_root and not Path(relative_root).is_absolute(), "source-project root is not workspace-relative")
    workspace = Path.home() / "Documents" / "interlanguage"
    source_root = (workspace / relative_root).resolve()
    try:
        source_root.relative_to(workspace.resolve())
    except ValueError as exc:
        raise VerificationError("source-project root escapes the workspace") from exc
    require(source_root.is_dir(), "registered source-project root is absent")

    evidence = lock.get("evidence_files")
    require(isinstance(evidence, list) and evidence, "authority evidence list is empty")
    by_role: dict[str, dict[str, Any]] = {}
    for row in evidence:
        require(isinstance(row, dict), "authority evidence row is not an object")
        role = row.get("role")
        relative = row.get("project_relative_path")
        require(isinstance(role, str) and role not in by_role, "authority evidence role is empty or repeated")
        require(isinstance(relative, str) and relative and "\\" not in relative and not Path(relative).is_absolute(), "invalid authority evidence path")
        path = (source_root / relative).resolve()
        try:
            path.relative_to(source_root)
        except ValueError as exc:
            raise VerificationError("authority evidence path escapes its source project") from exc
        require(path.is_file(), f"authority evidence is absent: {relative}")
        require(path.stat().st_size == row.get("bytes"), f"authority evidence byte count mismatch: {relative}")
        require(sha_file(path) == row.get("sha256"), f"authority evidence hash mismatch: {relative}")
        by_role[role] = row
    require(set(by_role) == {"four_edition_anchor_map", "english_source_page"}, "unexpected authority evidence roles")

    anchor_path = source_root / by_role["four_edition_anchor_map"]["project_relative_path"]
    with anchor_path.open("r", encoding="utf-8-sig", newline="") as stream:
        anchor_rows = list(csv.DictReader(stream))
    by_sequence: dict[int, dict[str, str]] = {}
    for row in anchor_rows:
        try:
            sequence = int(row["sequence"])
        except (KeyError, TypeError, ValueError) as exc:
            raise VerificationError("anchor map has an invalid sequence") from exc
        require(sequence not in by_sequence, "anchor map repeats a sequence")
        by_sequence[sequence] = row
    stable = load_json(ROOT / "stable-units.json")
    units = stable.get("units")
    require(isinstance(units, list), "stable-unit manifest has no units")
    for unit in units:
        require(isinstance(unit, dict), "stable-unit row is not an object")
        sequence = unit.get("anchor_map_sequence")
        require(isinstance(sequence, int) and sequence in by_sequence, "stable-unit anchor sequence is absent from the anchor map")
        row = by_sequence[sequence]
        require(row.get("anchor_id") == unit.get("anchor_id"), "anchor-map anchor ID mismatch")
        require(int(row.get("authority_physical_page", "-1")) == unit.get("physical_page"), "anchor-map physical-page mismatch")
        require(row.get("en_source_path") == unit.get("english_source"), "anchor-map English-source path mismatch")
        require(int(row.get("en_source_line", "-1")) == unit.get("english_lines", {}).get("start"), "anchor-map English-source line mismatch")


def validate_reference_closure(config: dict[str, Any]) -> list[str]:
    payload_path = ROOT / config["payload_artifact"]["path"]
    payload = payload_path.read_text(encoding="utf-8")
    references = sorted(set(re.findall(r"\\(?:ref|autoref|pageref)\{([^{}]+)\}", payload)))
    require(references, "payload contains no checkable references")
    provided = set(re.findall(r"\\label\{([^{}]+)\}", payload))
    target_name = config.get("composition_operation", {}).get("path")
    operations = load_jsonl(ROOT / target_name)
    require(len(operations) == 1, "cannot resolve target file for reference closure")
    target_path = operations[0].get("target", {}).get("path")
    require(isinstance(target_path, str) and target_path, "composition target path is empty")
    for tex_path in sorted(REPO.glob("*.tex"), key=lambda path: path.name):
        labels = set(re.findall(r"\\label\{([^{}]+)\}", tex_path.read_text(encoding="utf-8")))
        if tex_path.name == target_path:
            provided.update(labels)
        else:
            provided.update(f"{tex_path.stem}-{label}" for label in labels)
    missing = sorted(set(references) - provided)
    require(not missing, f"payload has unresolved Stacks references: {missing}")
    return references


def validate_identity(config: dict[str, Any], pointer: dict[str, Any]) -> None:
    registry_rel = pointer.get("lease_registry")
    require(isinstance(registry_rel, str) and registry_rel == "registry/leases.json", "unexpected lease registry")
    registry = load_json(AI_ROOT / registry_rel)
    events = [
        row
        for row in registry.get("events", [])
        if isinstance(row, dict) and row.get("lease_id") == pointer.get("lease_id")
    ]
    require(events, "lease is absent from the registry")
    issued = next((row for row in events if row.get("event") == "issued"), None)
    require(issued is not None, "lease has no issuance event")
    require(events[-1].get("state") in {"active", "released"}, "lease has an invalid terminal state")
    expected_path = ROOT.relative_to(AI_ROOT).as_posix()
    require(issued.get("candidate_path") == expected_path, "lease candidate path mismatch")
    for field in ("lease_id", "namespace", "writer_task"):
        require(config.get(field) == pointer.get(field) == issued.get(field), f"identity mismatch: {field}")
    lock = load_json(AI_ROOT / config["upstream"]["lock"])
    require(config["upstream"]["commit"] == pointer.get("upstream_commit") == issued.get("upstream_commit") == lock.get("commit"), "upstream commit mismatch")
    require(config["upstream"]["tree"] == issued.get("upstream_tree") == lock.get("tree"), "upstream tree mismatch")


def validate_units(config: dict[str, Any]) -> None:
    stable = load_json(ROOT / "stable-units.json")
    maps = load_jsonl(ROOT / "source-map.jsonl")
    inventory = load_json(ROOT / "formula-diagram-inventory.json")
    expected_ids = config.get("expected_unit_ids")
    expected_anchors = config.get("expected_anchor_ids")
    expected_count = config.get("source_scope", {}).get("source_unit_count")
    require(isinstance(expected_count, int) and expected_count > 0, "invalid dynamic source-unit count")
    require(isinstance(expected_ids, list) and len(expected_ids) == expected_count, "expected_unit_ids count mismatch")
    require(isinstance(expected_anchors, list) and len(expected_anchors) == expected_count, "expected_anchor_ids count mismatch")
    units = stable.get("units")
    require(isinstance(units, list) and stable.get("unit_count") == len(units) == expected_count, "stable-unit count mismatch")
    ids = [row.get("id") for row in units if isinstance(row, dict)]
    anchors = [row.get("anchor_id") for row in units if isinstance(row, dict)]
    require(ids == expected_ids and len(ids) == len(set(ids)), "stable-unit IDs differ from config or repeat")
    require(anchors == expected_anchors and len(anchors) == len(set(anchors)), "stable-unit anchors differ from config or repeat")
    require(len(maps) == expected_count, "source-map count mismatch")
    require([row.get("sequence") for row in maps] == list(range(1, expected_count + 1)), "source-map row sequence mismatch")
    require([row.get("unit_id") for row in maps] == ids, "source-map does not cover units in stable order")
    require([row.get("anchor_id") for row in maps] == anchors, "source-map anchor order mismatch")
    require(inventory.get("unit_count") == inventory.get("classified_unit_count") == expected_count, "formula inventory count mismatch")
    classified = []
    for key in ("formula_units", "diagram_units", "prose_only_units"):
        rows = inventory.get(key)
        require(isinstance(rows, list), f"formula inventory {key} is not an array")
        classified.extend(row.get("unit_id") for row in rows if isinstance(row, dict))
    require(sorted(classified) == sorted(ids) and len(classified) == len(set(classified)), "formula/diagram inventory is not an exact partition")
    for ledger in ("decisions.jsonl", "rejections.jsonl"):
        rows = load_jsonl(ROOT / ledger)
        require(rows, f"{ledger} is empty")
        row_ids = [row.get("id") for row in rows]
        require(all(isinstance(value, str) and value for value in row_ids), f"{ledger} has an empty ID")
        require(len(row_ids) == len(set(row_ids)), f"{ledger} repeats an ID")


def validate_composition(config: dict[str, Any]) -> dict[str, Any]:
    rows = load_jsonl(ROOT / config["composition_operation"]["path"])
    require(len(rows) == 1, "composition ledger must contain exactly one row")
    operation = rows[0]
    require(operation.get("operation_id") == config["composition_operation"]["operation_id"], "composition operation ID mismatch")
    require(operation.get("operation") == "insert_bytes" and operation.get("mode") == "insertion_only", "composition is not insertion-only")
    target = operation["target"]
    base_cfg = config["composition_base"]
    for field in ("repository", "commit", "tree"):
        require(target.get(field) == base_cfg.get(field), f"composition base mismatch: {field}")
    commit = target["commit"]
    require(git_text("rev-parse", f"{commit}^{{tree}}") == target["tree"], "composition base tree mismatch")
    require(git_text("rev-parse", f"{commit}:{target['path']}") == target["blob"], "composition target blob mismatch")
    base = git_bytes("show", f"{commit}:{target['path']}")
    require(len(base) == target["bytes"], "composition preimage byte count mismatch")
    require(sha_bytes(base) == target["preimage_sha256"], "composition preimage hash mismatch")
    payload_meta = operation["payload"]
    payload_cfg = config["payload_artifact"]
    payload_path = ROOT / payload_meta["path"]
    payload = payload_path.read_bytes()
    require(payload_meta["path"] == payload_cfg["path"], "payload path mismatch")
    require(len(payload) == payload_meta["bytes"] == payload_cfg["bytes"], "payload byte count mismatch")
    require(sha_bytes(payload) == payload_meta["sha256"] == payload_cfg["sha256"], "payload hash mismatch")
    require(b"\r" not in payload and not payload.startswith(b"\xef\xbb\xbf"), "payload must be BOM-free LF UTF-8")
    payload.decode("utf-8", errors="strict")
    label = payload_meta["proposed_label"]
    require(label == payload_cfg["proposed_label"], "proposed label mismatch")
    label_bytes = f"\\label{{{label}}}".encode("ascii")
    require(payload.count(label_bytes) == 1 and base.count(label_bytes) == 0, "proposed label collision or multiplicity")
    insertion = operation["insertion"]
    start = insertion["context_start_byte"]
    offset = insertion["byte_offset"]
    end = insertion["context_end_byte_exclusive"]
    require(0 <= start <= offset <= end <= len(base), "invalid composition offsets")
    require(end - start == insertion["context_bytes"], "context byte count mismatch")
    require(offset - start == insertion["before_context_bytes"], "before-context byte count mismatch")
    require(sha_bytes(base[start:end]) == insertion["context_sha256"], "context hash mismatch")
    require(sha_bytes(base[start:offset]) == insertion["before_context_sha256"], "before-context hash mismatch")
    require(sha_bytes(base[offset:end]) == insertion["after_context_sha256"], "after-context hash mismatch")
    after_label = f"\\label{{{insertion['after_complete_proof_of_label']}}}".encode("ascii")
    before_label = f"\\label{{{insertion['before_environment_for_label']}}}".encode("ascii")
    required = insertion.get("required_anchor_occurrences", 1)
    require(base.count(after_label) == required and base.count(before_label) == required, "composition anchor multiplicity mismatch")
    post = base[:offset] + payload + base[offset:]
    require(len(post) == target["postimage_bytes"], "composition postimage byte count mismatch")
    require(sha_bytes(post) == target["postimage_sha256"], "composition postimage hash mismatch")
    require(post[:offset] == base[:offset] and post[offset + len(payload):] == base[offset:], "composition changed pre-existing bytes")
    return operation


def validate_lifecycle(config: dict[str, Any]) -> None:
    require(config.get("review_state") in {"not_performed", "partial", "performed"}, "invalid review state")
    require(config.get("independent_replay") in {"not_performed", "passed", "failed"}, "invalid replay state")
    require(config.get("admission_state") in {"not_admitted", "admitted"}, "invalid admission state")
    build_state = config.get("build_state")
    receipts = [ROOT / "builds" / name for name in ("build-receipt.json", "validation.json")]
    if build_state == "not_performed":
        require(not any(path.exists() for path in receipts), "config says build not performed but build receipts exist")
    elif build_state == "validated_pass":
        for path in receipts:
            receipt = load_json(path)
            require(receipt.get("passed") is True and receipt.get("status") == "PASS", f"nonpassing build receipt: {path.name}")
    else:
        raise VerificationError(f"invalid build state: {build_state}")
    replay_path = ROOT / "replay" / "independent-review.json"
    if replay_path.exists():
        replay = load_json(replay_path)
        passed = replay.get("passed") is True or replay.get("status") == "PASS"
        require(config.get("independent_replay") == ("passed" if passed else "failed"), "replay receipt/config mismatch")
        require(config.get("review_state") == "performed", "review receipt exists but review_state is not performed")
    else:
        require(config.get("independent_replay") == "not_performed", "config overstates absent independent replay")


def main() -> int:
    try:
        allowed_arguments = {"--skip-manifest-check"}
        require(set(sys.argv[1:]) <= allowed_arguments, "unsupported verifier argument")
        skip_manifest_check = "--skip-manifest-check" in sys.argv[1:]
        config = load_json(ROOT / "candidate.config.json")
        pointer = load_json(ROOT / "LEASE.json")
        validate_identity(config, pointer)
        validate_authority(config)
        validate_units(config)
        references = validate_reference_closure(config)
        operation = validate_composition(config)
        validate_lifecycle(config)
        manifest = ROOT / "candidate.manifest.json"
        if manifest.exists() and not skip_manifest_check:
            completed = subprocess.run([sys.executable, str(ROOT / "check-manifest.py")], cwd=ROOT, check=False)
            require(completed.returncode == 0, "candidate.manifest.json failed closure checking")
        print(json.dumps({
            "passed": True,
            "candidate_id": config["candidate_id"],
            "lease_id": config["lease_id"],
            "source_units": config["source_scope"]["source_unit_count"],
            "operation_id": operation["operation_id"],
            "payload_sha256": sha_file(ROOT / config["payload_artifact"]["path"]),
            "reference_count": len(references),
            "manifest_present": manifest.exists(),
        }, sort_keys=True))
        return 0
    except (VerificationError, OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"VERIFY FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
