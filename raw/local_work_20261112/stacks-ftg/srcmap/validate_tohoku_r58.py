#!/usr/bin/env python3
"""Independent bounded validator for the append-only Tohoku r58 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r57"
TARGET = ROOT / "tohoku_r58"
STAGE = ROOT / ".tohoku-r58-txn"
AUDIT = ROOT / "D1014_FORMALIZATION_CHECK.json"
DESIGN = ROOT / "tmp" / "d1014_formalization_design.json"
REVIEW = ROOT / "tmp" / "d1014_independent_review_r1.json"
SCAN_ORACLE = ROOT / "tmp" / "d1014_formalization_scan"
REPLAY_SCAN = ROOT / "tmp" / "d1014_formalization_scan_replay"
TEX = ROOT / "divisors.tex"
PDF = ROOT / "divisors.pdf"
LOG = ROOT / "divisors.log"
PYTHON = Path(r"user\miniconda3\python.exe")

EXPECTED_R57_RECEIPT = (6781, "51F8DC636DCDE8C29D71928DAC8CA54A358CB6FD8AA4118A87D6A2A6D97A79DB")
EXPECTED_R57_CORE = {
    "cfg.json": (5151, "A22FEC108C2A932AC2045BE31DC5BF4C0841FA2E56F163D0AD2374B05CA8F596"),
    "dec.csv": (382180, "251D9B4D766624E532C3316544CB1C0C6EB8DFC0BED9FD4D95207CE62AD170BD"),
    "issues.csv": (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"),
    "map.csv": (483757, "829FA7055DCA164F741C3204489FADF441A437A1079085E64B86571D28601B73"),
    "check.json": (81766, "F6BC2D7EEF2BB3B90DD1ABE45449372B3E847C6A5532BE9165199DDF333DEB44"),
    "stx.csv": (5285699, "ADA99020E4B57061BE8EE0ACCF321DDB9EA286E7184AA8520BE0A15A7CF1E748"),
    "tcand.csv": (489175, "917A043875F1966A5E942A5DB9F027D347686B9AF59FCC267FAFDD4810AE1700"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
EXPECTED_D1014_SCAN = {
    "check.json": (82090, "1D2BC8124916BD1C3EB33116E58D88F73E51BD391FA711E3097E8160000A5F3E"),
    "stx.csv": (5286399, "FEFDE92F66D71D5B3BEDAB0E939A84931DC351028482254C21412512D36BEF7C"),
    "tcand.csv": (489175, "917A043875F1966A5E942A5DB9F027D347686B9AF59FCC267FAFDD4810AE1700"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
EXPECTED_TEX = (396388, "362CBBFD9653DB1CC18EB05FF7A7C7AB4B7B14AD4B74CB7F2AA3F3B7D43BC569")
EXPECTED_PDF = (1131224, "D8FF702EF09DF45E6A2B0FCB71A8D1C1374AC14F3F78F7533A2F1CA5FA061B7E")
EXPECTED_LOG = (36896, "90AC52B04BBB22A49AE1F1EC8981A851E0C4B007ABEB15CF352EC4FBC1EDDEAF")
EXPECTED_CANDIDATE = (2795, "3BD61D287F0EB4A17FE1931694A8D7FED445009A3E3644CB00731C9D73DD498F")
EXPECTED_DESIGN = (5856, "EA119BD4FC8682DAEAF4A3A9F7BAED0222C9D9A8259437F63FC11262E4C0AB53")
EXPECTED_REVIEW = (3542, "3507EBA6C76902537F1DF8B9838309733AE202F5AB61F5B2330AAE9CCF0FDE95")
EXPECTED_P160_EN = (3760, "EBDEF8E7B5AAFBA3B345F29137ED20A3CCA8B721422B48194B65D1324086D1CA")
EXPECTED_P160_FR = (4214, "179E2429456CA9D0FC13CA75E2D560B0E508CB889C300F14DA4208B5BE995AE6")
EXPECTED_R18_NODES = (585012, "3A3C9B6C22B0FA5E16466C264205D97CCA6041FF785F555A4C28F9639A50550D")
EXPECTED_R20_NODES = (586014, "466A914F3A4881BC4DDE331DE66FDE257AF0BF604DAD904BE21B07A4A88505F8")
EXPECTED_R18_MANIFEST = (38138, "40596FD03A707CF8AC3C1D825D0FEAD4447663F6A57E7BD16735021F14B520AB")
EXPECTED_R18_VALIDATION = (6102, "2972E56494357AD0ABDB765057E20CA99777E6A6AA73B5AF7571EA1F715AA3D4")
EXPECTED_R20_MANIFEST = (33263, "A5ADE906B63382C3071F8EE4908546F010A3F08ED7DC1F6FD8D2C84D9713782D")
EXPECTED_R20_VALIDATION = (10529, "AF76F4B6A8263586F178D2AA82A0E781590F9824F62BF9A8868A8B87406CF863")

MAP_FIELDS = [
    "unit_id", "item", "unit_type", "parent_id", "source_start", "source_end",
    "source_loc", "authority_sha256", "source_topics", "topic_evidence_labels",
    "topic_evidence_tags", "decision_id", "disposition", "review_state",
    "stacks_labels", "stacks_tags", "rationale",
]
DEC_FIELDS = ["decision_id", "unit_id", "action", "disposition", "stacks_labels", "rationale", "review_state", "supersedes"]
DECISION = {
    "decision_id": "D001038",
    "unit_id": "tohoku:construction:divisor-sequence:p1",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "divisors-lemma-meromorphic-quotient-divisor-germs;divisors-section-meromorphic-functions;divisors-section-Weil-divisors",
    "rationale": "The new bounded lemma gives the p.160 quotient-as-locally-principal-germs statement and, under factorial local rings, its identification with the Weil-divisor sheaf. It reuses the already proved locally-UFD exact sequence and does not conflate the p.161 cohomology successor or the analytic lifting boundary.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000249",
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r57 dossier is preserved exactly; D001038 is the bounded p.160 divisor-quotient successor.\n"
    "- D001038 is existing_equivalent for the general locally-principal quotient and its locally factorial Weil-divisor specialization.\n"
    "- The D1014 formalization, fixed-point PDF, strict parser, visual render, scanner replay, and independent review are sealed locally.\n"
    "- The scanner indexes the same exact 119 top-level TeX files; three new local labels and three corresponding missing-official-tag warnings are isolated.\n"
    "- There are 1038 decisions, 679 decided units, 31 source issues (none active), 670 scanner warnings, no errors, and 28 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the current VPN/security review; no GitHub or Git operation is attempted.\n"
    "- No analytic/GAGA, selector, release, publication, remote-freshness, DOI, rights, or whole-paper completion claim is made.\n"
).encode("utf-8")
PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv", "issues.csv",
    "check.json", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
    "mcheck.json", "STATUS.md",
}
EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1038,
    "decided_units": 679,
    "source_issues": 31,
    "active_source_issues": 0,
    "review_units": 0,
    "candidate_units": 0,
    "unit_candidates": 0,
    "graph_corrections": 0,
    "active_graph_corrections": 0,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 381,
        "existing_stronger": 41,
        "existing_weaker": 6,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 7,
        "structural_only": 424,
    },
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22098,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1286,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}


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


def strict_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    require(b"\r" not in raw and raw.endswith(b"\n"), f"Noncanonical JSON: {path}")
    value = json.loads(raw.decode("utf-8"))
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


def expected_decision_bytes() -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=DEC_FIELDS, lineterminator="\n")
    writer.writerow(DECISION)
    out = (SOURCE / "dec.csv").read_bytes() + stream.getvalue().encode("utf-8")
    require(identity_from_bytes(out) == (382743, "D5B83AD16FCE7309ED79B72EED7ED584DE72219094732549D0D1E9EE69EC34EA"), "Projected decision bytes drift")
    return out


def expected_map_bytes() -> bytes:
    fields, rows = load_csv(SOURCE / "map.csv")
    require(fields == MAP_FIELDS and len(rows) == 991, "Predecessor map schema drift")
    selected = [row for row in rows if row["unit_id"] == DECISION["unit_id"]]
    require(len(selected) == 1, "Target map row cardinality drift")
    replacement = selected[0].copy()
    replacement.update({
        "decision_id": DECISION["decision_id"],
        "disposition": DECISION["disposition"],
        "review_state": DECISION["review_state"],
        "stacks_labels": DECISION["stacks_labels"],
        "stacks_tags": "01X1;0BE0",
        "rationale": DECISION["rationale"],
    })
    out = csv_bytes(fields, [replacement if row["unit_id"] == DECISION["unit_id"] else row for row in rows])
    require(identity_from_bytes(out) == (483928, "035CC55B2267F222F28108BD674E77EC2AE67798F2C2479507004D10B6A3C447"), "Projected map bytes drift")
    return out


def expected_cfg_bytes() -> bytes:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r58"
    out = json_bytes(cfg)
    require(identity_from_bytes(out) == (5151, "676C3B2D5DB8894A716EE5B6DD4EA35FA0912F9B5F840837DC3F873403908BB7"), "Projected cfg bytes drift")
    return out


def identity_from_bytes(data: bytes) -> tuple[int, str]:
    return len(data), digest(data)


def normalize_namespace(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("tohoku_r57/", "tohoku_common/").replace("tohoku_r58/", "tohoku_common/")
    if isinstance(value, list):
        return [normalize_namespace(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize_namespace(v) for k, v in value.items()}
    return value


def verify_design_review() -> dict[str, Any]:
    require_identity(DESIGN, EXPECTED_DESIGN)
    require_identity(REVIEW, EXPECTED_REVIEW)
    design = strict_json(DESIGN)
    review = strict_json(REVIEW)
    require(design.get("status") == "STRICT_DESIGN_PASS", "D1014 design status drift")
    require(design["selection"]["unit_id"] == DECISION["unit_id"], "D1014 unit drift")
    require(design["selection"]["planned_disposition"] == "existing_equivalent", "D1014 planned disposition drift")
    require(design["mapping_projection"]["decision_id"] == "D001038", "D1014 decision drift")
    require(design["mapping_projection"]["gap_projection"] == {"before": 29, "after": 28, "reason": "The exact bounded algebraic p.160 unit is now represented; analytic or later lifting claims remain separate."}, "D1014 gap projection drift")
    semantic = design["authority"]["semantic_node"]
    require(semantic["generation"] == "sem/r18" and tuple((semantic["bytes"], semantic["sha256"])) == EXPECTED_R18_NODES, "r18 semantic identity drift")
    require(tuple((semantic["semantic_successor_nodes"]["bytes"], semantic["semantic_successor_nodes"]["sha256"])) == EXPECTED_R20_NODES, "r20 semantic identity drift")
    require(semantic["authority_sha256"] == "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF", "source authority drift")
    require(review.get("status") == "STRICT_PASS" and review["mapping_review"]["disposition"] == "existing_equivalent", "D1014 review status drift")
    require(review["candidate_replay"]["sha256"] == EXPECTED_CANDIDATE[1] and review["candidate_replay"]["bytes"] == EXPECTED_CANDIDATE[0], "D1014 candidate review drift")
    return {"design": record(DESIGN, "tmp/d1014_formalization_design.json"), "review": record(REVIEW, "tmp/d1014_independent_review_r1.json")}


def verify_external() -> dict[str, Any]:
    for name, expected in EXPECTED_R57_CORE.items():
        require_identity(SOURCE / name, expected)
    receipt = SOURCE / "r57-check.json"
    require_identity(receipt, EXPECTED_R57_RECEIPT)
    r = strict_json(receipt)
    require(r.get("status") == "PASS" and r.get("errors") == [], "r57 receipt not PASS")
    require(r.get("deltas", {}).get("remaining_gap_class_dispositions") == 29, "r57 gap count drift")
    design_review = verify_design_review()
    require_identity(TEX, EXPECTED_TEX)
    require_identity(PDF, EXPECTED_PDF)
    require_identity(LOG, EXPECTED_LOG)
    require_identity(ROOT / "tmp/d1014_block_candidate.tex", EXPECTED_CANDIDATE)
    for path, expected in ((ROOT / "tmp/d1014_formalization_scan" / n, v) for n, v in EXPECTED_D1014_SCAN.items()):
        require_identity(path, expected)
    for path, expected in ((ROOT / "tmp/d1014_formalization_scan_replay" / n, v) for n, v in EXPECTED_D1014_SCAN.items()):
        require_identity(path, expected)
    en = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\build\v068c3r19\src\en\p160.tex")
    fr = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\build\v068c3r19\src\fr\p160.tex")
    require_identity(en, EXPECTED_P160_EN)
    require_identity(fr, EXPECTED_P160_FR)
    sem = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem")
    require_identity(sem / "r18/nodes.csv", EXPECTED_R18_NODES)
    require_identity(sem / "r18/manifest.json", EXPECTED_R18_MANIFEST)
    require_identity(sem / "r18/validation.json", EXPECTED_R18_VALIDATION)
    require_identity(sem / "r20/nodes.csv", EXPECTED_R20_NODES)
    require_identity(sem / "r20/manifest.json", EXPECTED_R20_MANIFEST)
    require_identity(sem / "r20/validation.json", EXPECTED_R20_VALIDATION)
    return {"predecessor": {"receipt": record(receipt, "tohoku_r57/r57-check.json")}, "design_review": design_review}


def verify_scan(root: Path) -> None:
    for name, expected in EXPECTED_D1014_SCAN.items():
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    require(normalize_namespace(stage_check) == normalize_namespace(oracle_check), "r58 scanner differs from oracle")
    require(stage_check.get("status") == "PASS" and stage_check.get("errors") == [], "r58 scanner status drift")
    require(stage_check.get("counts") == EXPECTED_SCAN_COUNTS, "r58 scanner count drift")
    require(len(stage_check.get("warnings", [])) == 670, "r58 warning count drift")
    require(stage_check.get("tex_sha256", {}).get("divisors.tex") == EXPECTED_TEX[1], "r58 source scanner hash drift")


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing r58 stage: {root}")
    names = {p.name for p in root.iterdir() if p.is_file()}
    require(names == PAYLOAD | ({"r58-check.json"} if receipt_mode else set()), "r58 output surface drift")
    require(not any(p.is_dir() for p in root.iterdir()), "Unexpected r58 subdirectory")
    require_identity(root / "cfg.json", (5151, "676C3B2D5DB8894A716EE5B6DD4EA35FA0912F9B5F840837DC3F873403908BB7"))
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"Inherited payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r58 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r58 map replacement drift")
    verify_scan(root)
    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r58 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r58 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 670, "r58 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r58 STATUS drift")
    _, decisions = load_csv(root / "dec.csv")
    _, issues = load_csv(root / "issues.csv")
    require([r["decision_id"] for r in decisions] == [f"D{n:06d}" for n in range(1, 1039)], "r58 decision sequence drift")
    require([r["issue_id"] for r in issues] == [f"I{n:06d}" for n in range(1, 32)], "r58 issue sequence drift")
    result: dict[str, Any] = {
        "status": "PASS", "errors": [], "decisions": 1038,
        "decisions_appended": ["D001038"], "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 670, "errors": 0},
        "remaining_gap_class_dispositions": 28, "source_repairs_appended": 1,
        "map_delta": {"changed_units": 1, "unchanged_units": 990},
        "semantic_generation": "sem/r18",
        "inherited_unit_inventory": "BYTE_IDENTICAL_R57",
        "source_change": "D1014_P160_DIVISOR_QUOTIENT_BRIDGE",
        "scanner_payload_change": "D1014_THREE_LABELS_ONLY",
    }
    if receipt_mode:
        receipt = strict_json(root / "r58-check.json")
        require(receipt == receipt_payload(root, result), "r58 receipt replay mismatch")
    return result


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def receipt_payload(root: Path, deltas: dict[str, Any]) -> dict[str, Any]:
    external = verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r58-v1",
        "status": "PASS", "errors": [],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": record(AUDIT, "D1014_FORMALIZATION_CHECK.json"),
            "design": external["design_review"]["design"],
            "independent_review": external["design_review"]["review"],
        },
        "scanner_oracle": {n: record(SCAN_ORACLE / n, f"tmp/d1014_formalization_scan/{n}") for n in EXPECTED_D1014_SCAN},
        "semantic": {"r18_nodes": record(Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r18\nodes.csv"), "sem/r18/nodes.csv"), "r20_nodes": record(Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r20\nodes.csv"), "sem/r20/nodes.csv")},
        "external_constraints": {"github": {"status": "temporarily_unavailable", "reason": "GitHub access is suspended during a VPN/security review; support ticket filed.", "action": "Continue locally; do not attempt GitHub operations."}},
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git or GitHub operation is executed by this successor.",
            "The transaction is limited to the sealed r57 dossier and D001038.",
            "No analytic quotient, GAGA comparison, descent, publication, upload, DOI, remote-freshness, cleanup, archive, watcher, or whole-paper completion claim is made.",
        ],
    }


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R58_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if raw:
        expected = json.loads(raw)
        require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator attestation drift")
        return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r58.py", "bytes": actual[0], "sha256": actual[1]}
    return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r58.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not TARGET.exists() and not STAGE.exists(), "r58 target or stage already exists")
        external = verify_external()
        projected = {"cfg": identity_from_bytes(expected_cfg_bytes()), "dec": identity_from_bytes(expected_decision_bytes()), "map": identity_from_bytes(expected_map_bytes())}
        print(json.dumps({"schema": "tohoku-r58-static-input-audit-v1", "status": "PASS", "errors": [], "attestation": attestation, "external": external, "projected": projected, "remaining_gaps": 28}, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(json.dumps({"schema": "tohoku-r58-stage-validation-v1", "attestation": attestation, **verify_stage(args.stage.resolve(), args.receipt)}, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
