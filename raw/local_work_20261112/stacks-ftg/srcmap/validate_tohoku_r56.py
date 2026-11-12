#!/usr/bin/env python3
"""Independent bounded validator for the no-overwrite Tohoku r56 successor."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import os
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r55"
TARGET = ROOT / "tohoku_r56"
STAGE = ROOT / ".tohoku-r56-txn"
AUDIT = ROOT / "D1012_FORMALIZATION_CHECK.json"
DESIGN = ROOT / "tmp" / "d1012_mapping_design.json"
SCAN_ORACLE = ROOT / "tmp" / "d1012_formalization_scan"
PYTHON = Path(r"user\miniconda3\python.exe")
PYTHON_IDENTITY = (104264, "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264")
EXPECTED_AUDIT = (25581, "A24BDE77551C6C7EED8217C7D7C43A9B36D89006FED790B4A0A0B5B2F55AEFD6")
EXPECTED_DESIGN = (30870, "257F4C5677CCCF5DDD88991FF5AE262CD9531CE6DDCBEFB1321C51E9D5FA7FE7")
EXPECTED_R55_RECEIPT = (51881, "710219F6C9B79B9448E73209F2C3C129FB8D63FEDE134D12FA42643C78B9360B")
EXPECTED_R55_CORE = {
    "cfg.json": (5151, "3F8EC62FEA5C2EEA711FBF93F73BC95052E3B69594F9712D115DDCA8DC56A68F"),
    "dec.csv": (378984, "CBA7EB96B1EF1E61A1E1AE824EB40BF54B4B8D6388E31EE88DC20DF3860E3B45"),
    "issues.csv": (31413, "C9E2B573A63D834205AC8B2714A0E32230309AFBDD22FA0764F9A8831DF65503"),
    "map.csv": (482243, "0EAAF30DD6AC08B21E6C7156FD9C7FA92A5033D20AED7F172A564A491FA1503B"),
}
EXPECTED_OUTPUTS = {
    "cfg.json": (5151, "4720F5E9FDC2A1B1BC995D415BD50CCA153D5CA4475B0076334A84FB0C9A5D6A"),
    "dec.csv": (381639, "5680E5911F51D5A583FD184BFA954618C9E45D73A32192F3D9AC824C57F6BDFA"),
    "issues.csv": (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"),
    "map.csv": (483640, "0F06BCBBCAE7ED210C382BF60DE8B998D6598B9130D99E96071CB48B752DCD91"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "stx.csv": (5285098, "482E66727415B51142F25FA6FA7035C5E00BE068D72606FE3A117D4E2AAF69B2"),
    "tcand.csv": (488966, "D68B56C26F8046DBF3AF94C01A6AA8AAAD9E62FC179FD5B4659B89F8CB80D9AD"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "check.json": (81523, "B2D6E35F8C97D756AC252CF2D49F2265BD6CCEC09AC70691E4513DE1FBDD82A1"),
}
EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "decisions": 1036,
    "source_issues": 31,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "graph_corrections": 0,
    "review_units": 0,
    "unit_candidates": 0,
    "units": 991,
    "dispositions": {
        "example_or_remark": 84, "existing_equivalent": 380,
        "existing_stronger": 41, "existing_weaker": 6,
        "extend_existing": 12, "historical_reference": 33,
        "new_section": 4, "new_statement": 7, "structural_only": 424,
    },
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22093, "official_tags_joined": 21437, "tex_files": 119,
    "topic_candidates": 1286, "topic_coverage": {"direct": 13}, "topics": 13,
}
RUNTIME = {
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
}
PAYLOAD = {"cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv", "issues.csv",
           "check.json", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
           "mcheck.json", "STATUS.md"}

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r55 dossier is preserved exactly; D001032--D001036 are the five D1012 replacements and I000031 is the resolved source issue.\n"
    "- The admitted p. 179 cross-cover trace repair is bound to TOH-P179-COR-002 and TOH-SRC-P179-009; diplomatic French remains byte-stable.\n"
    "- The D1012 formalization, reader v068c3r19, QA v68r41, sem/r20, fixed-point PDF, and scanner replay are sealed locally.\n"
    "- The scanner indexes the same exact 119 top-level TeX files; the six new labels and six corresponding missing-official-tag warnings are isolated.\n"
    "- There are 1036 decisions, 679 decided units, 31 source issues (none active), 665 scanner warnings, no errors, and 29 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the current VPN/security review; no GitHub or Git operation is attempted.\n"
    "- No selector, release, publication, remote-freshness, DOI, rights, or whole-paper completion claim is made.\n"
).encode("utf-8")

NONCLAIMS = [
    "No Git or GitHub operation is executed by this successor.",
    "The transaction is limited to the sealed r55 dossier and the exact five D1012 replacements plus I000031.",
    "No source correction beyond the already admitted TOH-P179-COR-002 and TOH-SRC-P179-009 is appended.",
    "No official Stacks tag is claimed for the six new local labels.",
    "No publication, upload, DOI, remote-freshness, cleanup, archive, watcher, or whole-paper completion claim is made.",
]

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()

def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)

def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha}

def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)

def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require(path.is_file() and not path.is_symlink(), f"Expected plain file: {path}")
    require(identity(path) == expected, f"Identity drift: {path}")

def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")

def no_dupes(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        require(key not in out, f"Duplicate JSON key: {key}")
        out[key] = value
    return out

def strict_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    require(b"\r" not in raw and raw.endswith(b"\n"), f"Noncanonical JSON: {path}")
    value = json.loads(raw.decode("utf-8"), object_pairs_hook=no_dupes)
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value

def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    raw = path.read_text(encoding="utf-8-sig", newline="")
    reader = csv.DictReader(io.StringIO(raw, newline=""))
    require(reader.fieldnames is not None, f"Missing CSV header: {path}")
    return list(reader.fieldnames), [dict(row) for row in reader]

def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")

def b64_row(value: str, expected_bytes: int, expected_sha: str) -> bytes:
    raw = base64.b64decode(value)
    require((len(raw), digest(raw)) == (expected_bytes, expected_sha), "Design row identity drift")
    return raw

def load_design() -> dict[str, Any]:
    require_identity(DESIGN, EXPECTED_DESIGN)
    d = strict_json(DESIGN)
    require(d.get("schema") == "tohoku-stacks-d1012-r56-mapping-design-v1", "D1012 mapping schema drift")
    require(d.get("status") == "STRICT_DESIGN_PASS_CONTINGENT", "D1012 mapping design status drift")
    require([r.get("decision_id") for r in d["planned_decisions"]] == ["D001032", "D001033", "D001034", "D001035", "D001036"], "Decision sequence drift")
    require(d["planned_issue"]["issue_id"] == "I000031" and d["planned_issue"]["status"] == "resolved", "Issue design drift")
    require(d["projected_counts"]["remaining_gap_class_dispositions_after"] == 29, "Gap projection drift")
    return d

def verify_audit() -> dict[str, Any]:
    require_identity(AUDIT, EXPECTED_AUDIT)
    a = strict_json(AUDIT)
    require(a.get("schema") == "tohoku-stacks-d1012-formalization-check-v1", "D1012 audit schema drift")
    require(a.get("formalization_id") == "D1012" and a.get("overall_result") == "STRICT_PASS", "D1012 audit status drift")
    preds = a.get("predicates", [])
    require([p.get("id") for p in preds] == [f"P{i:03d}" for i in range(1, 13)], "D1012 predicate sequence drift")
    require(all(p.get("result") == "PASS" and p.get("expected") == p.get("observed") for p in preds), "D1012 predicate replay drift")
    require(a.get("predicate_summary") == {"total": 12, "passed": 12, "failed": 0, "rule": "overall_result is STRICT_PASS iff every predicate replays PASS from the bound live files"}, "D1012 predicate summary drift")
    live = Path(a["formalization_artifacts"]["live_source"]["path"])
    require_identity(live, (909844, "B686159DD380301A5A7752C389A93E27734672545CCC6F719806175DD688423B"))
    pdf = Path(a["fixed_point_build"]["pdf"]["path"])
    require_identity(pdf, (1995257, "6F237865D0E46546CF18F24D3F153846135AD2DBDF95F2D6B3DA3A0A240D7B5E"))
    manifest = Path(a["pdf_and_log_qa"]["visual_audit"]["manifest_path"])
    require_identity(manifest, (850, "4797908ECB87DDBF384CCE29225DB814970B6FF4AC9E82ABE74ECCC85C63E52D"))
    scan_check = Path(a["scanner_oracle"]["final"]["path"]) / "check.json"
    require_identity(scan_check, EXPECTED_OUTPUTS["check.json"])
    require(a["scope"]["external_constraints"]["github"]["status"] == "temporarily_unavailable", "GitHub constraint missing")
    return a

def verify_predecessor() -> dict[str, Any]:
    require(SOURCE.is_dir() and not SOURCE.is_symlink(), f"Missing predecessor: {SOURCE}")
    for name, expected in EXPECTED_R55_CORE.items():
        require_identity(SOURCE / name, expected)
    receipt = SOURCE / "r55-check.json"
    require_identity(receipt, EXPECTED_R55_RECEIPT)
    r = strict_json(receipt)
    require(r.get("schema") == "tohoku-stacks-mapping-successor-r55-v1" and r.get("status") == "PASS" and r.get("errors") == [], "r55 receipt not PASS")
    require(r.get("deltas", {}).get("remaining_gap_class_dispositions") == 34, "r55 gap count drift")
    require(r.get("deltas", {}).get("source_repairs_appended") == 0, "r55 source repair count drift")
    return {"receipt": record(receipt, "tohoku_r55/r55-check.json"), "core": {k: record(SOURCE / k, f"tohoku_r55/{k}") for k in sorted(EXPECTED_R55_CORE)}, "remaining_gaps": 34, "decisions": 1031, "issues": 30}

def verify_external() -> dict[str, Any]:
    audit = verify_audit()
    design = load_design()
    require_identity(ROOT / "tmp/d1012_formalization_scan/check.json", EXPECTED_OUTPUTS["check.json"])
    require_identity(ROOT / "tmp/d1012_formalization_scan/stx.csv", EXPECTED_OUTPUTS["stx.csv"])
    require_identity(ROOT / "tmp/d1012_formalization_scan/tcand.csv", EXPECTED_OUTPUTS["tcand.csv"])
    require_identity(ROOT / "tmp/d1012_formalization_scan/tmap.csv", EXPECTED_OUTPUTS["tmap.csv"])
    sem_root = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r20")
    require_identity(sem_root / "manifest.json", (33263, "A5ADE906B63382C3071F8EE4908546F010A3F08ED7DC1F6FD8D2C84D9713782D"))
    require_identity(sem_root / "validation.json", (10529, "AF76F4B6A8263586F178D2AA82A0E781590F9824F62BF9A8868A8B87406CF863"))
    return {"formalization_audit": record(AUDIT, "D1012_FORMALIZATION_CHECK.json"), "mapping_design": record(DESIGN, "tmp/d1012_mapping_design.json"), "scanner_oracle": {n: record(SCAN_ORACLE / n, f"tmp/d1012_formalization_scan/{n}") for n in ("check.json", "stx.csv", "tcand.csv", "tmap.csv")}, "semantic": {"revision": "sem/r20", "manifest": record(sem_root / "manifest.json", "sem/r20/manifest.json"), "validation": record(sem_root / "validation.json", "sem/r20/validation.json")}, "github": audit["scope"]["external_constraints"]["github"]}

def expected_decision_bytes() -> bytes:
    d = load_design()
    block = d["canonical_encodings"]["decision_block"]
    suffix = b64_row(block["base64"], int(block["bytes"]), str(block["sha256"]))
    source = (SOURCE / "dec.csv").read_bytes()
    out = source + suffix
    require((len(out), digest(out)) == (381639, "5680E5911F51D5A583FD184BFA954618C9E45D73A32192F3D9AC824C57F6BDFA"), "Projected dec.csv drift")
    return out

def expected_issue_bytes() -> bytes:
    d = load_design()
    row = d["canonical_encodings"]["issue_row"]
    suffix = b64_row(row["base64"], int(row["bytes"]), str(row["sha256"]))
    out = (SOURCE / "issues.csv").read_bytes() + suffix
    require((len(out), digest(out)) == (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"), "Projected issues.csv drift")
    return out

def expected_map_bytes() -> bytes:
    d = load_design()
    fields, old_rows = load_csv(SOURCE / "map.csv")
    require(len(old_rows) == 991 and fields == d["canonical_encodings"]["map_schema"], "Map schema drift")
    replacements: dict[str, dict[str, str]] = {}
    for item in d["canonical_encodings"]["map_replacement_rows"]:
        raw = b64_row(item["base64"], int(item["bytes"]), str(item["sha256"]))
        rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""), fieldnames=fields))
        require(len(rows) == 1, "Replacement row cardinality drift")
        row = rows[0]
        require(row["unit_id"] == item["unit_id"] and row["decision_id"] == item["decision_id"], "Replacement row ID drift")
        replacements[row["unit_id"]] = row
    require(set(replacements) == {"tohoku:theorem:3.9.1", "tohoku:corollary:3.9.1:1", "tohoku:corollary:3.9.1:2", "tohoku:corollary:3.9.1:3", "tohoku:section:3.9"}, "Replacement unit set drift")
    out_rows = [replacements.get(row["unit_id"], row) for row in old_rows]
    out = csv_bytes(fields, out_rows)
    require((len(out), digest(out)) == (483640, "0F06BCBBCAE7ED210C382BF60DE8B998D6598B9130D99E96071CB48B752DCD91"), "Projected map.csv drift")
    return out

def expected_cfg_bytes() -> bytes:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r56"
    out = json_bytes(cfg)
    require((len(out), digest(out)) == EXPECTED_OUTPUTS["cfg.json"], "Projected cfg drift")
    return out

def normalize_namespace(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("tohoku_r56/", "tohoku_r51/")
    if isinstance(value, list):
        return [normalize_namespace(v) for v in value]
    if isinstance(value, dict):
        return {k.replace("tohoku_r56/", "tohoku_r51/"): normalize_namespace(v) for k, v in value.items()}
    return value

def verify_scan(root: Path) -> None:
    for name, expected in EXPECTED_OUTPUTS.items():
        if name in {"cfg.json", "dec.csv", "issues.csv", "map.csv", "mcheck.json", "STATUS.md", "check.json"}:
            continue
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    require(normalize_namespace(stage_check) == normalize_namespace(oracle_check), "r56 scanner check differs from sealed oracle beyond namespace")
    require(stage_check.get("status") == "PASS" and stage_check.get("errors") == [], "r56 scanner status drift")
    counts = stage_check.get("counts", {})
    require(counts == EXPECTED_SCAN_COUNTS, "r56 scanner count drift")
    require(len(stage_check.get("warnings", [])) == 665, "r56 warning count drift")
    require(stage_check.get("tex_sha256", {}).get("cohomology.tex") == "B686159DD380301A5A7752C389A93E27734672545CCC6F719806175DD688423B", "r56 source scanner hash drift")

def verify_stage(root: Path, receipt_mode: bool) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing stage: {root}")
    names = {p.name for p in root.iterdir() if p.is_file()}
    require(names == PAYLOAD | ({"r56-check.json"} if receipt_mode else set()), "r56 output surface drift")
    require(not any(p.is_dir() for p in root.iterdir()), "Unexpected r56 subdirectory")
    require_identity(root / "cfg.json", EXPECTED_OUTPUTS["cfg.json"])
    for name in ("intake.json", "units.csv", "topics.csv", "ucand.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"Inherited payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r56 decision append drift")
    require((root / "issues.csv").read_bytes() == expected_issue_bytes(), "r56 issue append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r56 map replacement drift")
    verify_scan(root)
    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r56 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r56 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 665, "r56 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r56 STATUS drift")
    _, decisions = load_csv(root / "dec.csv")
    _, issues = load_csv(root / "issues.csv")
    require([r["decision_id"] for r in decisions] == [f"D{n:06d}" for n in range(1, 1037)], "r56 decision sequence drift")
    require([r["issue_id"] for r in issues] == [f"I{n:06d}" for n in range(1, 32)], "r56 issue sequence drift")
    result: dict[str, Any] = {
        "status": "PASS", "errors": [], "decisions": 1036,
        "decisions_appended": ["D001032","D001033","D001034","D001035","D001036"],
        "issues_appended": ["I000031"], "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 665, "errors": 0},
        "remaining_gap_class_dispositions": 29, "source_repairs_appended": 1,
        "map_delta": {"changed_units": 5, "unchanged_units": 986},
        "semantic_generation": "sem/r20", "inherited_unit_inventory": "BYTE_IDENTICAL_R55",
        "source_change": "ADMITTED_P179_REPAIR_ONLY", "scanner_payload_change": "D1012_LABELS_ONLY",
    }
    if receipt_mode:
        receipt = strict_json(root / "r56-check.json")
        require(receipt == receipt_payload(root, result), "r56 receipt replay mismatch")
    return result

def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]

def receipt_payload(root: Path, deltas: dict[str, Any]) -> dict[str, Any]:
    external = verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r56-v1",
        "status": "PASS", "errors": [], "predecessor": verify_predecessor(),
        "formalization_audit": external["formalization_audit"], "mapping_design": external["mapping_design"],
        "scanner_oracle": external["scanner_oracle"], "semantic": external["semantic"],
        "external_constraints": {"github": external["github"]}, "deltas": deltas,
        "files": output_records(root), "nonclaims": NONCLAIMS,
    }

def external_input_paths() -> list[Path]:
    sem_root = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r20")
    return [AUDIT, DESIGN, ROOT / "srcmap/scan.py", ROOT / "srcmap/map.py",
            ROOT / "tohoku_r55/r55-check.json", *[SOURCE / n for n in EXPECTED_R55_CORE],
            *[SCAN_ORACLE / n for n in ("check.json","stx.csv","tcand.csv","tmap.csv")],
            sem_root / "manifest.json", sem_root / "validation.json"]

def expected_runtime() -> dict[str, tuple[int, str]]:
    return dict(RUNTIME)

def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R56_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if raw:
        expected = json.loads(raw)
        require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator attestation drift")
        return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r56.py", "bytes": actual[0], "sha256": actual[1]}
    return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r56.py", "bytes": actual[0], "sha256": actual[1]}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not TARGET.exists() and not STAGE.exists(), "r56 target or stage already exists")
        ext = verify_external()
        print(json.dumps({"schema":"tohoku-r56-static-input-audit-v1","status":"PASS","errors":[],"attestation":attestation,"external":ext,"projected":{"cfg":record_bytes(expected_cfg_bytes()),"dec":record_bytes(expected_decision_bytes()),"issues":record_bytes(expected_issue_bytes()),"map":record_bytes(expected_map_bytes()),"remaining_gaps":29}}, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(json.dumps({"schema":"tohoku-r56-stage-validation-v1","attestation":attestation, **verify_stage(args.stage.resolve(), args.receipt)}, ensure_ascii=True, indent=2, sort_keys=True))
    return 0

def record_bytes(data: bytes) -> dict[str, object]:
    return {"bytes": len(data), "sha256": digest(data)}

if __name__ == "__main__":
    raise SystemExit(main())
