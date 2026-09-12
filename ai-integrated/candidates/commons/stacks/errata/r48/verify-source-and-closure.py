"""Read-only, dynamic two-source checks for a future root-issued R48 candidate.

Mechanical checks do not replace mathematical or visual decisions. The sealed
mode requires actual independent and per-chapter visual review artifacts.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def sha(data):
    return hashlib.sha256(data).hexdigest().upper()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-root", type=Path, required=True)
    parser.add_argument("--ai-root", type=Path, required=True)
    parser.add_argument("--stage", choices=("source", "sealed", "admitted"), default="source")
    args = parser.parse_args()
    root, ai = args.candidate_root.resolve(), args.ai_root.resolve()
    def bound(row):
        path = (root / row["path"]).resolve()
        require(path.is_relative_to(root) and path.is_file(), "Evidence path escapes candidate")
        data = path.read_bytes()
        require(sha(data) == row["sha256"] and ("bytes" not in row or len(data) == row["bytes"]), "Bound evidence bytes changed: " + row["path"])
        return path
    config = load(root / "candidate.config.json")
    require(config == load(root / "candidate.config.input.json"), "Config regeneration input drift")
    require(config["candidate_id"] == "stacks-errata-a04446e-r48", "Wrong candidate")
    spec = load(root / "operation-spec.json")
    units = load(root / "stable-units.json")["units"]
    source_map = [json.loads(line) for line in (root / "source-map.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    operations = spec["operations"]
    ids = [u["id"] for u in units]
    require(ids == config["expected_unit_ids"] and len(set(ids)) == len(ids) == config["accepted"], "Unit identity closure drift")
    require([r["unit_id"] for r in source_map] == ids, "Source-map unit order mismatch")
    require(len(operations) == spec["operation_count"] == config["operation_count"], "Operation count drift")
    require({op["operation_id"] for op in operations} == {oid for unit in units for oid in unit["operation_ids"]}, "Unit operation closure mismatch")
    require(len({op["operation_id"] for op in operations}) == len(operations), "Operation ID collision")
    require(sorted(json.dumps(op, sort_keys=True) for op in operations) == sorted(json.dumps(op, sort_keys=True) for row in source_map for op in row["operations"]), "Mapped operations differ")
    source_results = {}
    for stem, expected in config["stems"].items():
        authority = (root / f"authority/source/{stem}.tex").read_bytes()
        payload = (root / f"payload/{stem}.tex").read_bytes()
        require(sha(authority) == expected["authority_sha256"] and sha(payload) == expected["payload_sha256"], "Source identity drift")
        selected = sorted([op for op in operations if op["source"] == stem + ".tex"], key=lambda x: x["start_byte"])
        require(selected and all(a["end_byte_exclusive"] <= b["start_byte"] for a, b in zip(selected, selected[1:])), "Source operation overlap")
        result = authority
        for op in reversed(selected):
            old, new = op["old_text"].encode("utf-8"), op["replacement_text"].encode("utf-8")
            require(sha(old) == op["old_sha256"] and sha(new) == op["replacement_sha256"], "Operation payload drift")
            require(authority[op["start_byte"]:op["end_byte_exclusive"]] == old, "Exact operation preimage mismatch")
            result = result[:op["start_byte"]] + new + result[op["end_byte_exclusive"]:]
        require(result == payload, "Unlisted payload change")
        source_results[stem] = dict(operations=len(selected), exact_replay=True, payload_sha256=sha(payload))
    if args.stage != "source":
        from jsonschema import Draft202012Validator
        from pypdf import PdfReader
        manifest = load(root / "candidate.manifest.json")
        Draft202012Validator(load(ai / "schemas/candidate-manifest.schema.json")).validate(manifest)
        require(manifest["independent_replay"] == "passed" and manifest["review_state"] == "performed", "Final review states missing")
        require(manifest["candidate_id"] == config["candidate_id"] and manifest["writer_task"] == config["writer_task"] and manifest["lease_id"] == config["lease_id"], "Manifest ownership mismatch")
        references = manifest["source_authorities"] + manifest["builds"] + [manifest[k] for k in ("stable_unit_manifest", "source_map", "decision_ledger", "rejection_ledger", "formula_diagram_inventory")]
        declared = [r["path"] for r in references]
        require(len(set(declared)) == len(declared), "Manifest duplicates")
        for row in references:
            bound(row)
        actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and p.name != "candidate.manifest.json" and p.suffix != ".pyc" and "__pycache__" not in p.parts}
        require(set(declared) == actual, "Manifest file closure differs")
        final_stage = load(root / "replay/FINAL_STAGE.json")
        independent = load(root / "replay/FINAL_INDEPENDENT_REVIEW.json")
        require(independent["passed"] is True and independent["candidate_id"] == config["candidate_id"], "No independent final PASS")
        require(independent["final_stage_sha256"] == sha((root / "replay/FINAL_STAGE.json").read_bytes()), "Independent review snapshot mismatch")
        for row in final_stage["snapshot_inventory"]:
            bound(row)
        build = load(root / "builds/build-receipt.json")
        deterministic = load(root / "builds/deterministic-replay.json")
        mutex = load(root / "builds/TEX_MUTEX_RECEIPT.json")
        require(build["passed"] and deterministic["passed"] and deterministic["fresh_builds_compared"] == 2, "Build/reproducibility gate missing")
        require(mutex["passed"] and mutex["acquired"] and mutex["released"] and mutex["mutex_name"] == "Global\\InterlanguageTeXSlotV1", "TeX mutex gate missing")
        require(deterministic["recorder_fls_closures_compared"] == 2 * len(config["stems"]), "Incomplete per-chapter FLS comparison")
        require({c["stem"] for c in build["chapters"]} == set(config["stems"]), "Build chapters incomplete")
        for stem in config["stems"]:
            page_count = len(PdfReader(root / f"builds/{stem}.pdf").pages)
            visual = load(root / f"replay/PAGE_COMPLETE_VISUAL_ADJUDICATION-{stem}.json")
            page_map = load(root / f"builds/source-page-map-{stem}.json")
            require(visual["candidate_id"] == config["candidate_id"] and visual["passed"] is True and not visual["blocking_findings"], "Chapter visual PASS missing")
            require(visual["scope"]["covered_pages"] == list(range(1, page_count + 1)) and visual["scope"]["unreviewed_pages"] == [], "Chapter visual coverage incomplete")
            require(set(page_map["unique_pages"]).issubset(visual["scope"]["high_resolution_pages"]), "Correction-sensitive pages not reviewed at high resolution")
            bound(visual["render_manifest"])
        if args.stage == "admitted":
            registry = load(ai / "registry/overlays.json")
            matches = [e for e in registry["registered_entries"] if e["id"] == config["candidate_id"]]
            require(len(matches) == 1 and matches[0]["stable_ids"] == ids, "Registry admission does not match candidate")
            require(matches[0]["manifest_sha256"] == sha((root / "candidate.manifest.json").read_bytes()), "Admitted manifest hash mismatch")
    print(json.dumps(dict(passed=True, stage=args.stage, source_replays=source_results, units=len(units), operations=len(operations), writes=False, fresh_visual_review_performed=False)))

if __name__ == "__main__":
    main()
