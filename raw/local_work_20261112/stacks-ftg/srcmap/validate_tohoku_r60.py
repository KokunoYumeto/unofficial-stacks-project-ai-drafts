#!/usr/bin/env python3
"""Independent bounded validator for the append-only Tohoku r60 successor."""

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
SOURCE = ROOT / "tohoku_r59"
TARGET = ROOT / "tohoku_r60"
STAGE = ROOT / ".tohoku-r60-txn"
AUDIT = ROOT / "D1016_MAPPING_CHECK.json"
DESIGN = ROOT / "tmp" / "d1016_p210_mapping_design.json"
REVIEW = ROOT / "tmp" / "d1016_independent_review_r1.json"
SCAN_ORACLE = ROOT / "tmp" / "d1016_mapping_scan"
REPLAY_SCAN = ROOT / "tmp" / "d1016_mapping_scan_replay"
TEX = ROOT / "cohomology.tex"
PYTHON = Path(r"user\miniconda3\python.exe")

EXPECTED_R59_RECEIPT = (8587, "68D02635D8DBEB96A3CE2ECDDD11EF7F281F654AB3D8EA9735A476F6133B8D49")
EXPECTED_R59_FILES = {
    "STATUS.md": (978, "78E208A42B32E0B442271D8C512FB68BB64989BF7E49AF786F4C63451429A6CE"),
    "cfg.json": (5151, "EBA7EE8E5082FED88BEE79BC6818F9A2D6C32F6E932365766A37248E4E7ECD69"),
    "check.json": (82451, "A4995BA2329FF941EE534A9DFBFBE2223D6CA65AA3C123824D7D763F6E1A0C19"),
    "dec.csv": (383458, "5FB2064456CE6EB91417DFBE5B4E5D0C10D8C520D005DE567704C7DC8E7B0EF3"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"),
    "map.csv": (484334, "776A4553AAC800F8C315EBD13DAFA5F264B814F01783B1945902403CB140978A"),
    "mcheck.json": (72278, "F0491479E4702DDA117A296403F8A0124E7EF10A6C93D46ADCF68B1325F4E0DC"),
    "stx.csv": (5287297, "C4224C4D2D5D51E4E9079F9FBA070A0A5BB5D6B8ECF37CE07DFC662F3A84829E"),
    "tcand.csv": (489256, "ACDCA4D86FEEB1A27D1E46D8869B6C340D6DFEB1057161B8F872D848B089DA29"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_D1016_SCAN = {
    "cfg.json": (5151, "E3C1117E4DC42A902A13DB823B146F01A1DE2B62066C75BD683B4BF50DA66AF8"),
    "check.json": (82451, "921E55104276A9C583124115733882F87A96D806F54C50F6082639F7E8CD804C"),
    "stx.csv": (5287297, "C4224C4D2D5D51E4E9079F9FBA070A0A5BB5D6B8ECF37CE07DFC662F3A84829E"),
    "tcand.csv": (489256, "ACDCA4D86FEEB1A27D1E46D8869B6C340D6DFEB1057161B8F872D848B089DA29"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_AUDIT = (12250, "AA5DA9A9B8E124E77648CFB9B414FA9E2193B33C6B61AEC80946FAF231852BCA")
EXPECTED_TEX = (919109, "81D07AAE646D776C3F0CBAA090EE311100634A2F57EBFC98719C1EC79F4A3082")
EXPECTED_DESIGN = (7286, "3F26F8427C2B017E9EC0484160898AC3E3B763D1CBD44A32564B3B267D2765D0")
EXPECTED_REVIEW = (4398, "5181B7095E7C8A33A8FA7E1F067D14C8A8082B4FEC149A787B281B22CAEAC262")
EXPECTED_AUTHORITY_PDF = (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53")
EXPECTED_P210_EN = (3827, "58B07E4FC86BEAECC2171136231750A64BD10A5C029844DD54E00E8C89EDDD47")
EXPECTED_P210_FR = (4024, "C459F2FDD52597817AFFA895184F286034F5B24905FB381945AD74850B028A99")
EXPECTED_P210_EN_EXCERPT = (559, "A48613AF83F96E30BE6E141C1CA22319946EDAB096E85850606ED911B39585C5")
EXPECTED_P210_FR_EXCERPT = (557, "12DB368682FF61DB2D26B15026E28B8E62B4D2F84675ABA0DA4B599314BC84D9")
EXPECTED_SEMANTIC_ROW = (781, "757CBEC4E1FB3AE94A650029A76BBBB832D1AFCA10031374891730B85843573B")
EXPECTED_MAP_ROW = (706, "94E31298CBB1988825689242EA9BA82C5C2E323C053BB517DA275448F96D902C")
EXPECTED_OPEN_BLOCK = (728, "8A33199D8B55FD566EE9545D12169D4D997E2956B1B5615146FC827B92C74A4C")
EXPECTED_CLOSED_BLOCK = (842, "8EBECB185A3B5D2EEE5D29FD008E2256B230C360F34A6656F12321E13143D180")
EXPECTED_FREE_INDEX_BLOCK = (2964, "CC3010C8DAF60E918BB5C12958FEE5CF17C8EBFE6AEC7FDEB3C795F465AF8C96")
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
    "decision_id": "D001040",
    "unit_id": "tohoku:corollary:fixed-point-free-g-covering",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-equivariant-cech-spectral-sequence-acyclic-cover;cohomology-lemma-equivariant-cech-free-index;cohomology-lemma-equivariant-cech-spectral-sequence-closed-acyclic-cover",
    "rationale": "Stacks now proves the complete source corollary. The open-cover acyclic comparison and the new closed-cover acyclic comparison cover respectively the open branch and the finite/locally-finite paracompact closed branches, while the fixed-point-free index lemma identifies derived invariants of the nonalternating Cech complex with the cohomology of its invariant subcomplex.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000907",
}
EXPECTED_GAP_PROJECTION = {
    "before": 27,
    "after": 26,
    "reason": "The only deficiency recorded by D000907 was the missing closed-cover comparison, and D1015 has supplied it.",
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r59 dossier is preserved exactly; D001040 is the mapping-only p.210 fixed-point-free G-covering successor.\n"
    "- D001040 is existing_equivalent because the open and new closed acyclic comparisons, together with the free-index lemma, prove the complete source corollary.\n"
    "- The D1016 design, two independent gates, durable review, and deterministic scanner replay are sealed locally; no live TeX or PDF change is required.\n"
    "- The scanner indexes the unchanged exact 119 top-level TeX files with 673 inherited warnings and no errors.\n"
    "- There are 1040 decisions, 679 decided units, 31 source issues (none active), and 26 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the current VPN/security review; no GitHub or Git operation is attempted.\n"
    "- No arbitrary finite non-open/non-closed covering, closed-cover cofinality, analytic/GAGA, descent, release, publication, remote-freshness, DOI, rights, or whole-paper completion claim is made.\n"
).encode("utf-8")
PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv", "issues.csv",
    "check.json", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
    "mcheck.json", "STATUS.md",
}
EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1040,
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
        "existing_equivalent": 383,
        "existing_stronger": 41,
        "existing_weaker": 5,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 6,
        "structural_only": 424,
    },
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22101,
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


def identity_from_bytes(data: bytes) -> tuple[int, str]:
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


def line_slice_identity(path: Path, start: int, end: int) -> tuple[int, str]:
    lines = path.read_bytes().splitlines(keepends=True)
    require(1 <= start <= end <= len(lines), f"Line range outside file: {path}:{start}--{end}")
    return identity_from_bytes(b"".join(lines[start - 1:end]))


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
    require(identity_from_bytes(out) == (384155, "7BAA5693242F7A809B5534164BE64FC9BA8C56BFAC21CD70CC0B7B75ACB5C235"), "Projected decision bytes drift")
    return out


def expected_map_bytes() -> bytes:
    fields, rows = load_csv(SOURCE / "map.csv")
    require(fields == MAP_FIELDS and len(rows) == 991, "Predecessor map schema drift")
    selected = [row for row in rows if row["unit_id"] == DECISION["unit_id"]]
    require(len(selected) == 1, "Target map row cardinality drift")
    replacement = selected[0].copy()
    require(replacement["decision_id"] == "D000907" and replacement["disposition"] == "existing_weaker", "Target predecessor row drift")
    replacement.update({
        "decision_id": DECISION["decision_id"],
        "disposition": DECISION["disposition"],
        "review_state": DECISION["review_state"],
        "stacks_labels": DECISION["stacks_labels"],
        "stacks_tags": "",
        "rationale": DECISION["rationale"],
    })
    out = csv_bytes(fields, [replacement if row["unit_id"] == DECISION["unit_id"] else row for row in rows])
    require(identity_from_bytes(out) == (484523, "99A6754134043E3434541A1E9CE1D62B18E1BC40B020080EA13BF06280849872"), "Projected map bytes drift")
    return out


def expected_cfg_bytes() -> bytes:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r60"
    out = json_bytes(cfg)
    require(identity_from_bytes(out) == EXPECTED_D1016_SCAN["cfg.json"], "Projected cfg bytes drift")
    return out


def normalize_namespace(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("tohoku_r59/", "tohoku_common/").replace("tohoku_r60/", "tohoku_common/")
    if isinstance(value, list):
        return [normalize_namespace(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize_namespace(v) for k, v in value.items()}
    return value


def verify_audit() -> dict[str, object]:
    require_identity(AUDIT, EXPECTED_AUDIT)
    audit = strict_json(AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1016-mapping-check-v1", "D1016 audit schema drift")
    require(audit.get("formalization_id") == "D1016" and audit.get("overall_result") == "STRICT_PASS_NO_LIVE_SOURCE_CHANGE", "D1016 audit result drift")
    require(audit.get("errors") == [], "D1016 audit errors drift")
    summary = audit.get("predicate_summary", {})
    require(summary.get("total") == 12 and summary.get("passed") == 12 and summary.get("failed") == 0, "D1016 predicate summary drift")
    predicates = audit.get("predicates", [])
    require(len(predicates) == 12 and [p.get("id") for p in predicates] == [f"P{n:03d}" for n in range(1, 13)], "D1016 predicate inventory drift")
    require(all(p.get("result") == "PASS" for p in predicates), "D1016 predicate result drift")
    scope = audit.get("scope", {})
    require(scope.get("live_source_change") is False and scope.get("pdf_change") is False, "D1016 audit change-class drift")
    mapping = audit.get("mapping_projection", {})
    for key in ("decision_id", "supersedes", "unit_id", "disposition", "review_state", "stacks_labels", "rationale"):
        require(mapping.get(key) == DECISION[key], f"D1016 audit mapping drift: {key}")
    require(mapping.get("stacks_tags") == "", "D1016 audit tag drift")
    require(mapping.get("gap_projection") == EXPECTED_GAP_PROJECTION, "D1016 audit gap drift")
    authority = audit.get("source_authority", {}).get("authority_pdf", {})
    require((authority.get("bytes"), authority.get("sha256")) == EXPECTED_AUTHORITY_PDF, "D1016 audit authority PDF drift")
    require(audit.get("scanner_oracle", {}).get("replay", {}).get("all_six_output_files_byte_identical_to_final") is True, "D1016 scanner replay claim drift")
    require(scope.get("external_constraints", {}).get("github", {}).get("status") == "temporarily_unavailable", "D1016 GitHub constraint drift")
    return record(AUDIT, "D1016_MAPPING_CHECK.json")


def verify_design_review() -> dict[str, Any]:
    require_identity(DESIGN, EXPECTED_DESIGN)
    require_identity(REVIEW, EXPECTED_REVIEW)
    design = strict_json(DESIGN)
    review = strict_json(REVIEW)
    require(design.get("status") == "STRICT_DESIGN_PASS_NO_TEX_CHANGE", "D1016 design status drift")
    require(design["selection"]["unit_id"] == DECISION["unit_id"], "D1016 unit drift")
    require(design["selection"]["current_decision"] == "D000907" and design["selection"]["planned_decision"] == "D001040" and design["selection"]["planned_disposition"] == "existing_equivalent", "D1016 selection drift")
    projection = design["mapping_projection"]
    for key in ("decision_id", "supersedes", "unit_id", "disposition", "review_state", "stacks_labels", "rationale"):
        require(projection[key] == DECISION[key], f"D1016 design mapping drift: {key}")
    require(projection["stacks_tags"] == "" and projection["gap_projection"] == EXPECTED_GAP_PROJECTION, "D1016 design gap or tag drift")
    semantic = design["authority"]["semantic_node"]
    require(semantic["generation"] == "sem/r18" and tuple((semantic["bytes"], semantic["sha256"])) == EXPECTED_R18_NODES, "r18 semantic identity drift")
    require(semantic["authority_sha256"] == "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53", "source authority drift")
    require(design.get("derivation", {}).get("new_tex_required") is False and design.get("derivation", {}).get("new_pdf_required") is False, "D1016 no-source-change design drift")
    require(review.get("status") == "STRICT_PASS_MAPPING_ONLY" and review.get("final_verdict") == "STRICT_PASS_NO_LIVE_SOURCE_CHANGE", "D1016 review status drift")
    review_scope = review["review_scope"]
    require((review_scope["design_bytes"], review_scope["design_sha256"]) == EXPECTED_DESIGN, "D1016 design review identity drift")
    require(review_scope["new_tex_required"] is False and review_scope["new_pdf_required"] is False, "D1016 review change-class drift")
    verdict = review["mapping_verdict"]
    require(verdict["decision_id"] == "D001040" and verdict["supersedes"] == "D000907" and verdict["disposition"] == "existing_equivalent" and verdict["stacks_labels"] == DECISION["stacks_labels"] and verdict["stacks_tags"] == "" and verdict["result"] == "PASS", "D1016 mapping review drift")
    require(verdict["gap_delta"] == "27 to 26", "D1016 review gap drift")
    return {
        "design": record(DESIGN, "tmp/d1016_p210_mapping_design.json"),
        "review": record(REVIEW, "tmp/d1016_independent_review_r1.json"),
    }


def verify_predecessor() -> dict[str, object]:
    receipt = SOURCE / "r59-check.json"
    require_identity(receipt, EXPECTED_R59_RECEIPT)
    for name, expected in EXPECTED_R59_FILES.items():
        require_identity(SOURCE / name, expected)
    value = strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r59-v1", "r59 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r59 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 27, "r59 gap count drift")
    records = value.get("files", [])
    require(isinstance(records, list) and len(records) == len(EXPECTED_R59_FILES), "r59 receipt file inventory drift")
    replay = {r.get("name"): (r.get("bytes"), r.get("sha256")) for r in records}
    require(replay == EXPECTED_R59_FILES, "r59 receipt file identities drift")
    require(line_slice_identity(SOURCE / "map.csv", 246, 246) == EXPECTED_MAP_ROW, "r59 target map row drift")
    return {"receipt": record(receipt, "tohoku_r59/r59-check.json")}


def verify_external() -> dict[str, Any]:
    predecessor = verify_predecessor()
    audit = verify_audit()
    design_review = verify_design_review()
    require_identity(TEX, EXPECTED_TEX)
    require(line_slice_identity(TEX, 17767, 17788) == EXPECTED_OPEN_BLOCK, "Open acyclic dependency block drift")
    require(line_slice_identity(TEX, 17791, 17880) == EXPECTED_FREE_INDEX_BLOCK, "Free-index dependency block drift")
    require(line_slice_identity(TEX, 17739, 17765) == EXPECTED_CLOSED_BLOCK, "Closed acyclic dependency block drift")
    for name, expected in EXPECTED_D1016_SCAN.items():
        require_identity(SCAN_ORACLE / name, expected)
        require_identity(REPLAY_SCAN / name, expected)
    en = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\build\v068c3r19\src\en\p210.tex")
    fr = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\build\v068c3r19\src\fr\p210.tex")
    authority_pdf = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\authority_snapshot\jstage_part_II_9_3_185.pdf")
    require_identity(en, EXPECTED_P210_EN)
    require_identity(fr, EXPECTED_P210_FR)
    require(line_slice_identity(en, 12, 23) == EXPECTED_P210_EN_EXCERPT, "English p.210 excerpt drift")
    require(line_slice_identity(fr, 13, 24) == EXPECTED_P210_FR_EXCERPT, "French p.210 excerpt drift")
    require_identity(authority_pdf, EXPECTED_AUTHORITY_PDF)
    sem = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem")
    require_identity(sem / "r18/nodes.csv", EXPECTED_R18_NODES)
    require(line_slice_identity(sem / "r18/nodes.csv", 246, 246) == EXPECTED_SEMANTIC_ROW, "sem/r18 p.210 node row drift")
    require_identity(sem / "r18/manifest.json", EXPECTED_R18_MANIFEST)
    require_identity(sem / "r18/validation.json", EXPECTED_R18_VALIDATION)
    require_identity(sem / "r20/nodes.csv", EXPECTED_R20_NODES)
    require_identity(sem / "r20/manifest.json", EXPECTED_R20_MANIFEST)
    require_identity(sem / "r20/validation.json", EXPECTED_R20_VALIDATION)
    return {"predecessor": predecessor, "audit": audit, "design_review": design_review}


def verify_scan(root: Path) -> None:
    for name, expected in EXPECTED_D1016_SCAN.items():
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    replay_check = strict_json(REPLAY_SCAN / "check.json")
    require(normalize_namespace(stage_check) == normalize_namespace(oracle_check), "r60 scanner differs from oracle")
    require(normalize_namespace(replay_check) == normalize_namespace(oracle_check), "D1016 scanner replay differs from oracle")
    require(stage_check.get("status") == "PASS" and stage_check.get("errors") == [], "r60 scanner status drift")
    require(stage_check.get("counts") == EXPECTED_SCAN_COUNTS, "r60 scanner count drift")
    require(len(stage_check.get("warnings", [])) == 673, "r60 warning count drift")
    require(stage_check.get("tex_sha256", {}).get("cohomology.tex") == EXPECTED_TEX[1], "r60 source scanner hash drift")


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing r60 stage: {root}")
    names = {p.name for p in root.iterdir() if p.is_file()}
    require(names == PAYLOAD | ({"r60-check.json"} if receipt_mode else set()), "r60 output surface drift")
    require(not any(p.is_dir() for p in root.iterdir()), "Unexpected r60 subdirectory")
    require_identity(root / "cfg.json", EXPECTED_D1016_SCAN["cfg.json"])
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"Inherited payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r60 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r60 map replacement drift")
    verify_scan(root)
    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r60 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r60 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 673, "r60 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r60 STATUS drift")
    _, decisions = load_csv(root / "dec.csv")
    _, issues = load_csv(root / "issues.csv")
    require([r["decision_id"] for r in decisions] == [f"D{n:06d}" for n in range(1, 1041)], "r60 decision sequence drift")
    require([r["issue_id"] for r in issues] == [f"I{n:06d}" for n in range(1, 32)], "r60 issue sequence drift")
    _, mapping = load_csv(root / "map.csv")
    selected = [row for row in mapping if row["unit_id"] == DECISION["unit_id"]]
    require(len(selected) == 1 and selected[0]["decision_id"] == "D001040" and selected[0]["disposition"] == "existing_equivalent" and selected[0]["stacks_labels"] == DECISION["stacks_labels"] and selected[0]["stacks_tags"] == "", "r60 selected map row drift")
    result: dict[str, Any] = {
        "status": "PASS", "errors": [], "decisions": 1040,
        "decisions_appended": ["D001040"], "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 673, "errors": 0},
        "remaining_gap_class_dispositions": 26, "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "unchanged_units": 990},
        "semantic_generation": "sem/r18",
        "inherited_unit_inventory": "BYTE_IDENTICAL_R59",
        "source_change": "D1016_MAPPING_ONLY_NO_LIVE_SOURCE_CHANGE",
        "scanner_payload_change": "D1016_NAMESPACE_ONLY",
    }
    if receipt_mode:
        receipt = strict_json(root / "r60-check.json")
        require(receipt == receipt_payload(root, result), "r60 receipt replay mismatch")
    return result


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def receipt_payload(root: Path, deltas: dict[str, Any]) -> dict[str, Any]:
    external = verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r60-v1",
        "status": "PASS", "errors": [],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": external["audit"],
            "design": external["design_review"]["design"],
            "independent_review": external["design_review"]["review"],
            "live_source": record(TEX, "cohomology.tex"),
            "change_class": "mapping_only_no_live_source_or_pdf_change",
        },
        "scanner_oracle": {n: record(SCAN_ORACLE / n, f"tmp/d1016_mapping_scan/{n}") for n in EXPECTED_D1016_SCAN},
        "scanner_replay": {n: record(REPLAY_SCAN / n, f"tmp/d1016_mapping_scan_replay/{n}") for n in EXPECTED_D1016_SCAN},
        "semantic": {
            "source_authority_pdf": record(Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\authority_snapshot\jstage_part_II_9_3_185.pdf"), "authority_snapshot/jstage_part_II_9_3_185.pdf"),
            "r18_nodes": record(Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r18\nodes.csv"), "sem/r18/nodes.csv"),
            "r20_nodes": record(Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem\r20\nodes.csv"), "sem/r20/nodes.csv"),
        },
        "external_constraints": {"github": {"status": "temporarily_unavailable", "reason": "GitHub access is suspended during a VPN/security review; support ticket filed.", "action": "Continue locally; do not attempt GitHub operations."}},
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git or GitHub operation is executed by this successor.",
            "The transaction is limited to the sealed r59 dossier and D001040.",
            "No arbitrary finite non-open/non-closed covering, closed-cover cofinality, analytic/GAGA comparison, descent, publication, upload, DOI, remote-freshness, cleanup, archive, watcher, or whole-paper completion claim is made.",
        ],
    }


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R60_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if raw:
        expected = json.loads(raw)
        require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator attestation drift")
        return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r60.py", "bytes": actual[0], "sha256": actual[1]}
    return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r60.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not TARGET.exists() and not STAGE.exists(), "r60 target or stage already exists")
        external = verify_external()
        projected = {"cfg": identity_from_bytes(expected_cfg_bytes()), "dec": identity_from_bytes(expected_decision_bytes()), "map": identity_from_bytes(expected_map_bytes())}
        print(json.dumps({"schema": "tohoku-r60-static-input-audit-v1", "status": "PASS", "errors": [], "attestation": attestation, "external": external, "projected": projected, "remaining_gaps": 26}, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(json.dumps({"schema": "tohoku-r60-stage-validation-v1", "attestation": attestation, **verify_stage(args.stage.resolve(), args.receipt)}, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
