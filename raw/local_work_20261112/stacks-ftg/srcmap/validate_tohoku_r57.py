#!/usr/bin/env python3
"""Independent bounded validator for the no-overwrite Tohoku r57 successor."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r56"
TARGET = ROOT / "tohoku_r57"
STAGE = ROOT / ".tohoku-r57-txn"
AUDIT = ROOT / "D1013_FORMALIZATION_CHECK.json"
DESIGN = ROOT / "tmp" / "d1013_mapping_design.json"
SCAN_ORACLE = ROOT / "tmp" / "d1013_formalization_scan"
PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_AUDIT = (11954, "CE386515F4859DB819181B1484D818A1AE71DD7EC6BEEFDBC2B02E11863105E7")
EXPECTED_DESIGN = (7653, "A81BCCEC73766A51B6F678FD01A9E7AB87E4D62533BD238F22594288EF6A92F9")
EXPECTED_R56_RECEIPT = (6894, "A931C701449D33944193E4AB5B4819B1A4CD3912A6ADDB7456DED7B2C514A62D")
EXPECTED_R56_CORE = {
    "cfg.json": (5151, "4720F5E9FDC2A1B1BC995D415BD50CCA153D5CA4475B0076334A84FB0C9A5D6A"),
    "dec.csv": (381639, "5680E5911F51D5A583FD184BFA954618C9E45D73A32192F3D9AC824C57F6BDFA"),
    "issues.csv": (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"),
    "map.csv": (483640, "0F06BCBBCAE7ED210C382BF60DE8B998D6598B9130D99E96071CB48B752DCD91"),
}
EXPECTED_OUTPUTS = {
    "cfg.json": (5151, "A22FEC108C2A932AC2045BE31DC5BF4C0841FA2E56F163D0AD2374B05CA8F596"),
    "dec.csv": (382180, "251D9B4D766624E532C3316544CB1C0C6EB8DFC0BED9FD4D95207CE62AD170BD"),
    "issues.csv": (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"),
    "map.csv": (483757, "829FA7055DCA164F741C3204489FADF441A437A1079085E64B86571D28601B73"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "stx.csv": (5285699, "ADA99020E4B57061BE8EE0ACCF321DDB9EA286E7184AA8520BE0A15A7CF1E748"),
    "tcand.csv": (489175, "917A043875F1966A5E942A5DB9F027D347686B9AF59FCC267FAFDD4810AE1700"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "check.json": (81766, "9D15E5DADC243B5BB225CF6F41CC20E0015926EF91286B6DFE2C03ABE05C6B87"),
}
EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "decisions": 1037,
    "source_issues": 31,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "graph_corrections": 0,
    "review_units": 0,
    "unit_candidates": 0,
    "units": 991,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 380,
        "existing_stronger": 41,
        "existing_weaker": 6,
        "extend_existing": 12,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 7,
        "structural_only": 424,
    },
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22095,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1286,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
RUNTIME = {
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
}
PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv", "issues.csv",
    "check.json", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
    "mcheck.json", "STATUS.md",
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r56 dossier is preserved exactly; D001037 is the bounded p.219 successor for the equivariant extension-class unit.\n"
    "- D001037 remains new_statement: the abstract Ext/Yoneda bridge is recorded, while the analytic bundle correspondence and GAGA boundary remain open.\n"
    "- The D1013 formalization, fixed-point PDF, strict parser, visual render, scanner replay, and independent review are sealed locally.\n"
    "- The scanner indexes the same exact 119 top-level TeX files; two new local labels and two corresponding missing-official-tag warnings are isolated.\n"
    "- There are 1037 decisions, 679 decided units, 31 source issues (none active), 667 scanner warnings, no errors, and 29 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the current VPN/security review; no GitHub or Git operation is attempted.\n"
    "- No analytic/GAGA, selector, release, publication, remote-freshness, DOI, rights, or whole-paper completion claim is made.\n"
).encode("utf-8")
NONCLAIMS = [
    "No Git or GitHub operation is executed by this successor.",
    "The transaction is limited to the sealed r56 dossier and D001037.",
    "The p.219 analytic bundle correspondence, GAGA comparison, descent, and finiteness remain outside this closure.",
    "No official Stacks tag is claimed for the new local label.",
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
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
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
    require(raw.endswith(b"\n"), "Design row lacks LF terminator")
    return raw


def load_design() -> dict[str, Any]:
    require_identity(DESIGN, EXPECTED_DESIGN)
    d = strict_json(DESIGN)
    require(d.get("schema") == "tohoku-stacks-d1013-r57-mapping-design-v1", "D1013 mapping schema drift")
    require(d.get("status") == "STRICT_DESIGN_PASS_CONTINGENT", "D1013 mapping design status drift")
    require([row.get("decision_id") for row in d.get("planned_decisions", [])] == ["D001037"], "D1013 decision sequence drift")
    require(d["planned_decisions"][0]["supersedes"] == "D000565", "D1013 supersession drift")
    require(d["planned_decisions"][0]["disposition"] == "new_statement", "D1013 disposition drift")
    require(d["projected_counts"]["remaining_gap_class_dispositions_after"] == 29, "D1013 gap projection drift")
    return d


def verify_audit() -> dict[str, Any]:
    require_identity(AUDIT, EXPECTED_AUDIT)
    a = strict_json(AUDIT)
    require(a.get("schema") == "tohoku-stacks-d1013-formalization-check-v1", "D1013 audit schema drift")
    require(a.get("formalization_id") == "D1013" and a.get("overall_result") == "STRICT_PASS", "D1013 audit status drift")
    preds = a.get("predicates", [])
    require(len(preds) == 12 and all(p.get("result") == "PASS" for p in preds), "D1013 predicate replay drift")
    require(a.get("predicate_summary") == {"total": 12, "passed": 12, "failed": 0, "rule": "overall_result is STRICT_PASS iff every predicate replays PASS from the bound live files"}, "D1013 predicate summary drift")
    require(a["scope"]["external_constraints"]["github"]["status"] == "temporarily_unavailable", "GitHub constraint missing")
    require_identity(ROOT / "cohomology.tex", (912791, "93A3BCE86198A5A7A453790488E6E56C9B27155BF4748BB5FD045DCBC859EF01"))
    require_identity(ROOT / "cohomology.pdf", (1998117, "F07D8C9125AA3528FD3F5E7FB1DD57A300AF6AF2F7B6AE5F7AFDD6269363F2B8"))
    require_identity(ROOT / "tmp/d1013_render/D1013_RENDER_MANIFEST.txt", (834, "8663874CF67CBD4600C1F97C149D3485A85111A3CBD728D90A2FD5C3311ED6D1"))
    return a


def verify_predecessor() -> dict[str, Any]:
    require(SOURCE.is_dir() and not SOURCE.is_symlink(), f"Missing predecessor: {SOURCE}")
    for name, expected in EXPECTED_R56_CORE.items():
        require_identity(SOURCE / name, expected)
    receipt = SOURCE / "r56-check.json"
    require_identity(receipt, EXPECTED_R56_RECEIPT)
    r = strict_json(receipt)
    require(r.get("schema") == "tohoku-stacks-mapping-successor-r56-v1" and r.get("status") == "PASS" and r.get("errors") == [], "r56 receipt not PASS")
    require(r.get("deltas", {}).get("remaining_gap_class_dispositions") == 29, "r56 gap count drift")
    return {"receipt": record(receipt, "tohoku_r56/r56-check.json"), "core": {k: record(SOURCE / k, f"tohoku_r56/{k}") for k in sorted(EXPECTED_R56_CORE)}, "remaining_gaps": 29, "decisions": 1036, "issues": 31}


def verify_external() -> dict[str, Any]:
    audit = verify_audit()
    design = load_design()
    require_identity(ROOT / "tmp/d1013_formalization_scan/check.json", EXPECTED_OUTPUTS["check.json"])
    require_identity(ROOT / "tmp/d1013_formalization_scan/stx.csv", EXPECTED_OUTPUTS["stx.csv"])
    require_identity(ROOT / "tmp/d1013_formalization_scan/tcand.csv", EXPECTED_OUTPUTS["tcand.csv"])
    require_identity(ROOT / "tmp/d1013_formalization_scan/tmap.csv", EXPECTED_OUTPUTS["tmap.csv"])
    sem_root = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r20")
    require_identity(sem_root / "manifest.json", (33263, "A5ADE906B63382C3071F8EE4908546F010A3F08ED7DC1F6FD8D2C84D9713782D"))
    require_identity(sem_root / "validation.json", (10529, "AF76F4B6A8263586F178D2AA82A0E781590F9824F62BF9A8868A8B87406CF863"))
    return {"formalization_audit": record(AUDIT, "D1013_FORMALIZATION_CHECK.json"), "mapping_design": record(DESIGN, "tmp/d1013_mapping_design.json"), "scanner_oracle": {n: record(SCAN_ORACLE / n, f"tmp/d1013_formalization_scan/{n}") for n in ("check.json", "stx.csv", "tcand.csv", "tmap.csv")}, "semantic": {"revision": "sem/r20", "manifest": record(sem_root / "manifest.json", "sem/r20/manifest.json"), "validation": record(sem_root / "validation.json", "sem/r20/validation.json")}, "github": audit["scope"]["external_constraints"]["github"]}


def expected_decision_bytes() -> bytes:
    d = load_design()
    block = d["canonical_encodings"]["decision_block"]
    suffix = b64_row(block["base64"], int(block["bytes"]), str(block["sha256"]))
    out = (SOURCE / "dec.csv").read_bytes() + suffix
    require((len(out), digest(out)) == EXPECTED_OUTPUTS["dec.csv"], "Projected dec.csv drift")
    return out


def expected_map_bytes() -> bytes:
    d = load_design()
    fields, old_rows = load_csv(SOURCE / "map.csv")
    require(fields == d["canonical_encodings"]["map_schema"] and len(old_rows) == 991, "Map schema drift")
    item = d["canonical_encodings"]["map_replacement_rows"][0]
    raw = b64_row(item["base64"], int(item["bytes"]), str(item["sha256"]))
    replacement = next(csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""), fieldnames=fields))
    require(replacement["unit_id"] == item["unit_id"] and replacement["decision_id"] == "D001037", "Replacement row ID drift")
    out_rows = [replacement if row["unit_id"] == item["unit_id"] else row for row in old_rows]
    require(sum(row["unit_id"] == item["unit_id"] for row in old_rows) == 1, "Target map row cardinality drift")
    out = csv_bytes(fields, out_rows)
    require((len(out), digest(out)) == EXPECTED_OUTPUTS["map.csv"], "Projected map.csv drift")
    return out


def expected_cfg_bytes() -> bytes:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r57"
    out = json_bytes(cfg)
    require((len(out), digest(out)) == EXPECTED_OUTPUTS["cfg.json"], "Projected cfg drift")
    return out


def normalize_namespace(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("tohoku_r57/", "tohoku_common/").replace("tohoku_r56/", "tohoku_common/")
    if isinstance(value, list):
        return [normalize_namespace(v) for v in value]
    if isinstance(value, dict):
        return {k.replace("tohoku_r57/", "tohoku_common/").replace("tohoku_r56/", "tohoku_common/"): normalize_namespace(v) for k, v in value.items()}
    return value


def verify_scan(root: Path) -> None:
    for name, expected in EXPECTED_OUTPUTS.items():
        if name in {"cfg.json", "dec.csv", "issues.csv", "map.csv", "mcheck.json", "STATUS.md", "check.json"}:
            continue
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    require(normalize_namespace(stage_check) == normalize_namespace(oracle_check), "r57 scanner check differs from sealed oracle beyond namespace")
    require(stage_check.get("status") == "PASS" and stage_check.get("errors") == [], "r57 scanner status drift")
    require(stage_check.get("counts") == EXPECTED_SCAN_COUNTS, "r57 scanner count drift")
    require(len(stage_check.get("warnings", [])) == 667, "r57 warning count drift")
    require(stage_check.get("tex_sha256", {}).get("cohomology.tex") == "93A3BCE86198A5A7A453790488E6E56C9B27155BF4748BB5FD045DCBC859EF01", "r57 source scanner hash drift")


def verify_stage(root: Path, receipt_mode: bool) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing stage: {root}")
    names = {p.name for p in root.iterdir() if p.is_file()}
    require(names == PAYLOAD | ({"r57-check.json"} if receipt_mode else set()), "r57 output surface drift")
    require(not any(p.is_dir() for p in root.iterdir()), "Unexpected r57 subdirectory")
    require_identity(root / "cfg.json", EXPECTED_OUTPUTS["cfg.json"])
    for name in ("intake.json", "units.csv", "topics.csv", "ucand.json"):
        if name == "ucand.json":
            continue
    for name in ("intake.json", "units.csv", "topics.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"Inherited payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r57 decision append drift")
    require((root / "issues.csv").read_bytes() == (SOURCE / "issues.csv").read_bytes(), "r57 issue drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r57 map replacement drift")
    verify_scan(root)
    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r57 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r57 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 667, "r57 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r57 STATUS drift")
    _, decisions = load_csv(root / "dec.csv")
    _, issues = load_csv(root / "issues.csv")
    require([r["decision_id"] for r in decisions] == [f"D{n:06d}" for n in range(1, 1038)], "r57 decision sequence drift")
    require([r["issue_id"] for r in issues] == [f"I{n:06d}" for n in range(1, 32)], "r57 issue sequence drift")
    result: dict[str, Any] = {
        "status": "PASS", "errors": [], "decisions": 1037,
        "decisions_appended": ["D001037"], "issues_appended": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 667, "errors": 0},
        "remaining_gap_class_dispositions": 29, "source_repairs_appended": 1,
        "map_delta": {"changed_units": 1, "unchanged_units": 990},
        "semantic_generation": "sem/r20", "inherited_unit_inventory": "BYTE_IDENTICAL_R56",
        "source_change": "D1013_ABSTRACT_P219_BRIDGE_ONLY", "scanner_payload_change": "D1013_TWO_LABELS_ONLY",
    }
    if receipt_mode:
        receipt = strict_json(root / "r57-check.json")
        require(receipt == receipt_payload(root, result), "r57 receipt replay mismatch")
    return result


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def receipt_payload(root: Path, deltas: dict[str, Any]) -> dict[str, Any]:
    external = verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r57-v1",
        "status": "PASS", "errors": [], "predecessor": verify_predecessor(),
        "formalization_audit": external["formalization_audit"], "mapping_design": external["mapping_design"],
        "scanner_oracle": external["scanner_oracle"], "semantic": external["semantic"],
        "external_constraints": {"github": external["github"]}, "deltas": deltas,
        "files": output_records(root), "nonclaims": NONCLAIMS,
    }


def external_input_paths() -> list[Path]:
    sem_root = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r20")
    return [AUDIT, DESIGN, ROOT / "srcmap/scan.py", ROOT / "srcmap/map.py", SOURCE / "r56-check.json", *[SOURCE / n for n in EXPECTED_R56_CORE], *[SCAN_ORACLE / n for n in ("check.json", "stx.csv", "tcand.csv", "tmap.csv")], sem_root / "manifest.json", sem_root / "validation.json"]


def expected_runtime() -> dict[str, tuple[int, str]]:
    return dict(RUNTIME)


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R57_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if raw:
        expected = json.loads(raw)
        require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator attestation drift")
        return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r57.py", "bytes": actual[0], "sha256": actual[1]}
    return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r57.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not TARGET.exists() and not STAGE.exists(), "r57 target or stage already exists")
        ext = verify_external()
        print(json.dumps({"schema": "tohoku-r57-static-input-audit-v1", "status": "PASS", "errors": [], "attestation": attestation, "external": ext, "projected": {"cfg": {"bytes": len(expected_cfg_bytes()), "sha256": digest(expected_cfg_bytes())}, "dec": {"bytes": len(expected_decision_bytes()), "sha256": digest(expected_decision_bytes())}, "map": {"bytes": len(expected_map_bytes()), "sha256": digest(expected_map_bytes())}, "remaining_gaps": 29}}, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(json.dumps({"schema": "tohoku-r57-stage-validation-v1", "attestation": attestation, **verify_stage(args.stage.resolve(), args.receipt)}, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
