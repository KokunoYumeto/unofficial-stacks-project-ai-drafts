#!/usr/bin/env python3
"""Independent bounded validator for the append-only Tohoku r59 successor."""

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
SOURCE = ROOT / "tohoku_r58"
TARGET = ROOT / "tohoku_r59"
STAGE = ROOT / ".tohoku-r59-txn"
AUDIT = ROOT / "D1015_FORMALIZATION_CHECK.json"
DESIGN = ROOT / "tmp" / "d1015_p209_formalization_design.json"
REVIEW = ROOT / "tmp" / "d1015_independent_review_r1.json"
CANDIDATE = ROOT / "tmp" / "d1015_closed_equivariant_cech_candidate.tex"
SCAN_ORACLE = ROOT / "tmp" / "d1015_formalization_scan"
REPLAY_SCAN = ROOT / "tmp" / "d1015_formalization_scan_replay"
RENDER_MANIFEST = ROOT / "tmp" / "d1015_render" / "D1015_RENDER_MANIFEST.txt"
FIXED_POINT_DIR = ROOT / "tmp" / "d1015_fixed_point_replay"
FIXED_POINT_REPLAY = FIXED_POINT_DIR / "D1015_FIXED_POINT_REPLAY.json"
TEX = ROOT / "cohomology.tex"
PDF = ROOT / "cohomology.pdf"
LOG = ROOT / "cohomology.log"
AUX = ROOT / "cohomology.aux"
OUT = ROOT / "cohomology.out"
TOC = ROOT / "cohomology.toc"
PYTHON = Path(r"user\miniconda3\python.exe")

EXPECTED_R58_RECEIPT = (6037, "BFD429BDDABE4E5898C762795D5CC85D619BB9BE3F8F5E991002604051CE3DC1")
EXPECTED_R58_FILES = {
    "STATUS.md": (943, "1C101065D3C51F82EF3B943B7C749C75701455D2EB529B0004F3DFA3DD678902"),
    "cfg.json": (5151, "676C3B2D5DB8894A716EE5B6DD4EA35FA0912F9B5F840837DC3F873403908BB7"),
    "check.json": (82090, "1D2BC8124916BD1C3EB33116E58D88F73E51BD391FA711E3097E8160000A5F3E"),
    "dec.csv": (382743, "D5B83AD16FCE7309ED79B72EED7ED584DE72219094732549D0D1E9EE69EC34EA"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"),
    "map.csv": (483928, "035CC55B2267F222F28108BD674E77EC2AE67798F2C2479507004D10B6A3C447"),
    "mcheck.json": (71917, "B74F5878EF7FA48942E75A8A8A6ABF16D5741034AF9C8CC8F6D9E2D04B07D6C0"),
    "stx.csv": (5286399, "FEFDE92F66D71D5B3BEDAB0E939A84931DC351028482254C21412512D36BEF7C"),
    "tcand.csv": (489175, "917A043875F1966A5E942A5DB9F027D347686B9AF59FCC267FAFDD4810AE1700"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_D1015_SCAN = {
    "cfg.json": (5151, "EBA7EE8E5082FED88BEE79BC6818F9A2D6C32F6E932365766A37248E4E7ECD69"),
    "check.json": (82451, "A4995BA2329FF941EE534A9DFBFBE2223D6CA65AA3C123824D7D763F6E1A0C19"),
    "stx.csv": (5287297, "C4224C4D2D5D51E4E9079F9FBA070A0A5BB5D6B8ECF37CE07DFC662F3A84829E"),
    "tcand.csv": (489256, "ACDCA4D86FEEB1A27D1E46D8869B6C340D6DFEB1057161B8F872D848B089DA29"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_AUDIT = (15104, "4F819B611DCBF9B2F1DE8C79FEF16C9AF885313E32CA90A870155937C22FF36A")
EXPECTED_TEX = (919109, "81D07AAE646D776C3F0CBAA090EE311100634A2F57EBFC98719C1EC79F4A3082")
EXPECTED_PDF = (2008210, "45398E73CDDFC462413A9EA61D9C2CB33D25E0418ED7599C2C497104A33669CD")
EXPECTED_LOG = (48426, "0B26A515746ED9BC4A4D15F92F2C39D7CBD77663EC1CD381B8CCE6D359814333")
EXPECTED_AUX = (57294, "138AD4A77E4909EDF6E876A0745853D706FDAD9BDABD946F771176BA3F7A8F12")
EXPECTED_OUT = (12725, "E20175BCE90BA5C272D88818F692C70BF698D24E5E04C6CAF200E3D812D62651")
EXPECTED_TOC = (5574, "DE5F077DD607BEB71C275883505AD6B3964D28999393C56B70BD98DD46A49229")
EXPECTED_CANDIDATE = (6317, "9B9054551D83A227717282F4833AC3D7A764CE39F3994E8C3A6191AD6E638A6A")
EXPECTED_DESIGN = (7972, "57EC230D2B2B64190997BD7CC2D930B167FFC94827CF5D5D1BFA6FEEF6A4B07A")
EXPECTED_REVIEW = (3270, "64AC35BB511F3058AF32A2E41527FD2E22D0CDB27A877A665A42271EACC696F0")
EXPECTED_RENDER_MANIFEST = (798, "10A96AC7737A31E97F118925BEAB01F804FEBF34EF97B311FB59DC0D2EAEC484")
EXPECTED_FIXED_POINT_REPLAY = (2555, "C8AF895A57F414D3C5EC25E6334BA7239DEE8E54657052980D9DC9789D96892B")
EXPECTED_REPLAY_PDF = (2008210, "E04F886AE1BE7F7F08E30E42CBFB1734DD1DC6AD76E2E5D3BEDAA96FE1CB400A")
EXPECTED_REPLAY_LOG = (48493, "9267B62F67FAEC1CD7E2FF65858819DD9E0932E145D3A4A91B0B15DA4273D925")
EXPECTED_AUTHORITY_PDF = (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53")
EXPECTED_P209_EN = (3541, "62DD780BB16E8B4EC6ABD61FE3CFC097514B4594E597F12A6379074825B348D7")
EXPECTED_P209_FR = (3989, "1F71BA0E31689B071A44478FDB4B5DB3432ED1012B33D6D0355ADD0A6EB7DB2A")
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
    "decision_id": "D001039",
    "unit_id": "tohoku:corollary:2-theorem-5.5.3",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-definition-equivariant-cech-closed-covering;cohomology-lemma-equivariant-cech-spectral-sequence-closed-covering;cohomology-lemma-equivariant-cech-spectral-sequence-closed-acyclic-cover",
    "rationale": "The new bounded definition and lemma now state the complete p.209 closed finite/locally-finite paracompact G-cover extension of the existing equivariant spectral sequence, including the edge maps; the separately stated acyclic degeneration is its formal Corollary 1 consequence. The ordinary closed-cover lemma supplies the local resolution argument, and no broader cofinality claim is made.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000593",
}
EXPECTED_GAP_PROJECTION = {
    "before": 28,
    "after": 27,
    "reason": "The p.209 closed G-cover corollary is represented as a new bounded statement; unrelated closed-cover and later G-cover gaps remain open.",
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r58 dossier is preserved exactly; D001039 is the bounded p.209 equivariant closed-cover successor.\n"
    "- D001039 is existing_equivalent for finite closed G-coverings and locally finite closed G-coverings on paracompact spaces.\n"
    "- The D1015 formalization, fixed-point PDF, strict parser, visual render, scanner replay, and independent review are sealed locally.\n"
    "- The scanner indexes the same exact 119 top-level TeX files; three new local labels and three corresponding missing-official-tag warnings are isolated.\n"
    "- There are 1039 decisions, 679 decided units, 31 source issues (none active), 673 scanner warnings, no errors, and 27 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the current VPN/security review; no GitHub or Git operation is attempted.\n"
    "- No arbitrary closed-cover cofinality, analytic/GAGA, descent, release, publication, remote-freshness, DOI, rights, or whole-paper completion claim is made.\n"
).encode("utf-8")
PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv", "issues.csv",
    "check.json", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
    "mcheck.json", "STATUS.md",
}
EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1039,
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
        "existing_equivalent": 382,
        "existing_stronger": 41,
        "existing_weaker": 6,
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
    require(identity_from_bytes(out) == (383458, "5FB2064456CE6EB91417DFBE5B4E5D0C10D8C520D005DE567704C7DC8E7B0EF3"), "Projected decision bytes drift")
    return out


def expected_map_bytes() -> bytes:
    fields, rows = load_csv(SOURCE / "map.csv")
    require(fields == MAP_FIELDS and len(rows) == 991, "Predecessor map schema drift")
    selected = [row for row in rows if row["unit_id"] == DECISION["unit_id"]]
    require(len(selected) == 1, "Target map row cardinality drift")
    replacement = selected[0].copy()
    require(replacement["decision_id"] == "D000593" and replacement["disposition"] == "new_statement", "Target predecessor row drift")
    replacement.update({
        "decision_id": DECISION["decision_id"],
        "disposition": DECISION["disposition"],
        "review_state": DECISION["review_state"],
        "stacks_labels": DECISION["stacks_labels"],
        "stacks_tags": "",
        "rationale": DECISION["rationale"],
    })
    out = csv_bytes(fields, [replacement if row["unit_id"] == DECISION["unit_id"] else row for row in rows])
    require(identity_from_bytes(out) == (484334, "776A4553AAC800F8C315EBD13DAFA5F264B814F01783B1945902403CB140978A"), "Projected map bytes drift")
    return out


def expected_cfg_bytes() -> bytes:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r59"
    out = json_bytes(cfg)
    require(identity_from_bytes(out) == EXPECTED_D1015_SCAN["cfg.json"], "Projected cfg bytes drift")
    return out


def normalize_namespace(value: Any) -> Any:
    if isinstance(value, str):
        return value.replace("tohoku_r58/", "tohoku_common/").replace("tohoku_r59/", "tohoku_common/")
    if isinstance(value, list):
        return [normalize_namespace(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize_namespace(v) for k, v in value.items()}
    return value


def verify_audit() -> dict[str, object]:
    require_identity(AUDIT, EXPECTED_AUDIT)
    audit = strict_json(AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1015-formalization-check-v1", "D1015 audit schema drift")
    require(audit.get("formalization_id") == "D1015" and audit.get("overall_result") == "STRICT_PASS", "D1015 audit result drift")
    require(audit.get("errors") == [], "D1015 audit errors drift")
    summary = audit.get("predicate_summary", {})
    require(summary.get("total") == 14 and summary.get("passed") == 14 and summary.get("failed") == 0, "D1015 predicate summary drift")
    predicates = audit.get("predicates", [])
    require(len(predicates) == 14 and [p.get("id") for p in predicates] == [f"P{n:03d}" for n in range(1, 15)], "D1015 predicate inventory drift")
    require(all(p.get("result") == "PASS" for p in predicates), "D1015 predicate result drift")
    mapping = audit.get("mapping_projection", {})
    for key in ("decision_id", "supersedes", "unit_id", "disposition", "review_state", "stacks_labels"):
        require(mapping.get(key) == DECISION[key], f"D1015 audit mapping drift: {key}")
    require(mapping.get("stacks_tags") == "", "D1015 audit tag drift")
    require(mapping.get("gap_projection", {}).get("before") == 28 and mapping.get("gap_projection", {}).get("after") == 27, "D1015 audit gap drift")
    authority = audit.get("source_authority", {}).get("authority_pdf", {})
    require((authority.get("bytes"), authority.get("sha256")) == EXPECTED_AUTHORITY_PDF, "D1015 audit authority PDF drift")
    replay = audit.get("formalization_artifacts", {}).get("fixed_point_build", {}).get("isolated_auxiliary_fixed_point_replay", {})
    require((replay.get("bytes"), replay.get("sha256")) == EXPECTED_FIXED_POINT_REPLAY and replay.get("result") == "PASS", "D1015 audit fixed-point replay drift")
    parser = audit.get("pdf_and_log_qa", {}).get("parser", {})
    require(parser.get("text_aggregation", {}).get("joined_text_length") == 526556 and parser.get("text_aggregation", {}).get("sum_of_page_text_lengths") == 526317, "D1015 parser aggregation drift")
    require("Equivariant Čech complex for a closed covering" in parser.get("required_text_present", []) and "Equivariant Čech spectral sequence for closed coverings" in parser.get("required_text_present", []), "D1015 exact Unicode parser requirements drift")
    require(audit.get("scope", {}).get("external_constraints", {}).get("github", {}).get("status") == "temporarily_unavailable", "D1015 GitHub constraint drift")
    return record(AUDIT, "D1015_FORMALIZATION_CHECK.json")


def verify_design_review() -> dict[str, Any]:
    require_identity(DESIGN, EXPECTED_DESIGN)
    require_identity(REVIEW, EXPECTED_REVIEW)
    require_identity(CANDIDATE, EXPECTED_CANDIDATE)
    design = strict_json(DESIGN)
    review = strict_json(REVIEW)
    require(design.get("status") == "STRICT_DESIGN_PASS", "D1015 design status drift")
    require(design["selection"]["unit_id"] == DECISION["unit_id"], "D1015 unit drift")
    require(design["selection"]["current_decision"] == "D000593" and design["selection"]["planned_disposition"] == "existing_equivalent", "D1015 selection drift")
    projection = design["mapping_projection"]
    for key in ("decision_id", "supersedes", "unit_id", "disposition", "review_state", "stacks_labels", "rationale"):
        require(projection[key] == DECISION[key], f"D1015 design mapping drift: {key}")
    require(projection["stacks_tags"] == "" and projection["gap_projection"] == EXPECTED_GAP_PROJECTION, "D1015 design gap or tag drift")
    semantic = design["authority"]["semantic_node"]
    require(semantic["generation"] == "sem/r18" and tuple((semantic["bytes"], semantic["sha256"])) == EXPECTED_R18_NODES, "r18 semantic identity drift")
    require(tuple((semantic["semantic_successor_nodes"]["bytes"], semantic["semantic_successor_nodes"]["sha256"])) == EXPECTED_R20_NODES, "r20 semantic identity drift")
    require(semantic["authority_sha256"] == "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53", "source authority drift")
    require(review.get("status") == "STRICT_PASS_FINAL_PROOF" and review.get("final_verdict") == "STRICT_PASS", "D1015 review status drift")
    review_scope = review["review_scope"]
    require((review_scope["candidate_bytes"], review_scope["candidate_sha256"]) == EXPECTED_CANDIDATE, "D1015 candidate review drift")
    verdict = review["mapping_verdict"]
    require(verdict["decision_id"] == "D001039" and verdict["supersedes"] == "D000593" and verdict["disposition"] == "existing_equivalent" and verdict["stacks_tags"] == "" and verdict["result"] == "PASS", "D1015 mapping review drift")
    require(verdict["gap_delta"] == "28 to 27", "D1015 review gap drift")
    return {
        "design": record(DESIGN, "tmp/d1015_p209_formalization_design.json"),
        "review": record(REVIEW, "tmp/d1015_independent_review_r1.json"),
        "candidate": record(CANDIDATE, "tmp/d1015_closed_equivariant_cech_candidate.tex"),
    }


def verify_predecessor() -> dict[str, object]:
    receipt = SOURCE / "r58-check.json"
    require_identity(receipt, EXPECTED_R58_RECEIPT)
    for name, expected in EXPECTED_R58_FILES.items():
        require_identity(SOURCE / name, expected)
    value = strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r58-v1", "r58 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r58 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 28, "r58 gap count drift")
    records = value.get("files", [])
    require(isinstance(records, list) and len(records) == len(EXPECTED_R58_FILES), "r58 receipt file inventory drift")
    replay = {r.get("name"): (r.get("bytes"), r.get("sha256")) for r in records}
    require(replay == EXPECTED_R58_FILES, "r58 receipt file identities drift")
    return {"receipt": record(receipt, "tohoku_r58/r58-check.json")}


def verify_external() -> dict[str, Any]:
    predecessor = verify_predecessor()
    audit = verify_audit()
    design_review = verify_design_review()
    for path, expected in (
        (TEX, EXPECTED_TEX), (PDF, EXPECTED_PDF), (LOG, EXPECTED_LOG),
        (AUX, EXPECTED_AUX), (OUT, EXPECTED_OUT), (TOC, EXPECTED_TOC),
        (RENDER_MANIFEST, EXPECTED_RENDER_MANIFEST),
        (FIXED_POINT_REPLAY, EXPECTED_FIXED_POINT_REPLAY),
        (FIXED_POINT_DIR / "cohomology.pdf", EXPECTED_REPLAY_PDF),
        (FIXED_POINT_DIR / "cohomology.log", EXPECTED_REPLAY_LOG),
    ):
        require_identity(path, expected)
    for name, expected in (("cohomology.aux", EXPECTED_AUX), ("cohomology.out", EXPECTED_OUT), ("cohomology.toc", EXPECTED_TOC)):
        require_identity(FIXED_POINT_DIR / name, expected)
    fixed_point = strict_json(FIXED_POINT_REPLAY)
    require(fixed_point.get("status") == "PASS" and fixed_point.get("errors") == [] and fixed_point.get("result", {}).get("fixed_point") is True, "D1015 fixed-point replay result drift")
    for name, expected in EXPECTED_D1015_SCAN.items():
        require_identity(SCAN_ORACLE / name, expected)
        require_identity(REPLAY_SCAN / name, expected)
    en = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\build\v068c3r19\src\en\p209.tex")
    fr = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\build\v068c3r19\src\fr\p209.tex")
    authority_pdf = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\authority_snapshot\jstage_part_II_9_3_185.pdf")
    require_identity(en, EXPECTED_P209_EN)
    require_identity(fr, EXPECTED_P209_FR)
    require_identity(authority_pdf, EXPECTED_AUTHORITY_PDF)
    sem = Path(r"user\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\tohoku_bilingual_canonical_stacks_20260804_r1\sem")
    require_identity(sem / "r18/nodes.csv", EXPECTED_R18_NODES)
    require_identity(sem / "r18/manifest.json", EXPECTED_R18_MANIFEST)
    require_identity(sem / "r18/validation.json", EXPECTED_R18_VALIDATION)
    require_identity(sem / "r20/nodes.csv", EXPECTED_R20_NODES)
    require_identity(sem / "r20/manifest.json", EXPECTED_R20_MANIFEST)
    require_identity(sem / "r20/validation.json", EXPECTED_R20_VALIDATION)
    return {"predecessor": predecessor, "audit": audit, "design_review": design_review}


def verify_scan(root: Path) -> None:
    for name, expected in EXPECTED_D1015_SCAN.items():
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    replay_check = strict_json(REPLAY_SCAN / "check.json")
    require(normalize_namespace(stage_check) == normalize_namespace(oracle_check), "r59 scanner differs from oracle")
    require(normalize_namespace(replay_check) == normalize_namespace(oracle_check), "D1015 scanner replay differs from oracle")
    require(stage_check.get("status") == "PASS" and stage_check.get("errors") == [], "r59 scanner status drift")
    require(stage_check.get("counts") == EXPECTED_SCAN_COUNTS, "r59 scanner count drift")
    require(len(stage_check.get("warnings", [])) == 673, "r59 warning count drift")
    require(stage_check.get("tex_sha256", {}).get("cohomology.tex") == EXPECTED_TEX[1], "r59 source scanner hash drift")


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing r59 stage: {root}")
    names = {p.name for p in root.iterdir() if p.is_file()}
    require(names == PAYLOAD | ({"r59-check.json"} if receipt_mode else set()), "r59 output surface drift")
    require(not any(p.is_dir() for p in root.iterdir()), "Unexpected r59 subdirectory")
    require_identity(root / "cfg.json", EXPECTED_D1015_SCAN["cfg.json"])
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"Inherited payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r59 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r59 map replacement drift")
    verify_scan(root)
    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r59 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r59 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 673, "r59 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r59 STATUS drift")
    _, decisions = load_csv(root / "dec.csv")
    _, issues = load_csv(root / "issues.csv")
    require([r["decision_id"] for r in decisions] == [f"D{n:06d}" for n in range(1, 1040)], "r59 decision sequence drift")
    require([r["issue_id"] for r in issues] == [f"I{n:06d}" for n in range(1, 32)], "r59 issue sequence drift")
    _, mapping = load_csv(root / "map.csv")
    selected = [row for row in mapping if row["unit_id"] == DECISION["unit_id"]]
    require(len(selected) == 1 and selected[0]["decision_id"] == "D001039" and selected[0]["stacks_tags"] == "", "r59 selected map row drift")
    result: dict[str, Any] = {
        "status": "PASS", "errors": [], "decisions": 1039,
        "decisions_appended": ["D001039"], "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 673, "errors": 0},
        "remaining_gap_class_dispositions": 27, "source_repairs_appended": 1,
        "map_delta": {"changed_units": 1, "unchanged_units": 990},
        "semantic_generation": "sem/r18",
        "inherited_unit_inventory": "BYTE_IDENTICAL_R58",
        "source_change": "D1015_P209_EQUIVARIANT_CLOSED_COVER_BRIDGE",
        "scanner_payload_change": "D1015_THREE_LABELS_ONLY",
    }
    if receipt_mode:
        receipt = strict_json(root / "r59-check.json")
        require(receipt == receipt_payload(root, result), "r59 receipt replay mismatch")
    return result


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def receipt_payload(root: Path, deltas: dict[str, Any]) -> dict[str, Any]:
    external = verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r59-v1",
        "status": "PASS", "errors": [],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": external["audit"],
            "design": external["design_review"]["design"],
            "independent_review": external["design_review"]["review"],
            "candidate": external["design_review"]["candidate"],
            "live_source": record(TEX, "cohomology.tex"),
            "fixed_point_pdf": record(PDF, "cohomology.pdf"),
            "fixed_point_replay": record(FIXED_POINT_REPLAY, "tmp/d1015_fixed_point_replay/D1015_FIXED_POINT_REPLAY.json"),
        },
        "scanner_oracle": {n: record(SCAN_ORACLE / n, f"tmp/d1015_formalization_scan/{n}") for n in EXPECTED_D1015_SCAN},
        "scanner_replay": {n: record(REPLAY_SCAN / n, f"tmp/d1015_formalization_scan_replay/{n}") for n in EXPECTED_D1015_SCAN},
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
            "The transaction is limited to the sealed r58 dossier and D001039.",
            "No arbitrary closed-cover cofinality, analytic/GAGA comparison, descent, publication, upload, DOI, remote-freshness, cleanup, archive, watcher, or whole-paper completion claim is made.",
        ],
    }


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R59_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if raw:
        expected = json.loads(raw)
        require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator attestation drift")
        return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r59.py", "bytes": actual[0], "sha256": actual[1]}
    return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r59.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not TARGET.exists() and not STAGE.exists(), "r59 target or stage already exists")
        external = verify_external()
        projected = {"cfg": identity_from_bytes(expected_cfg_bytes()), "dec": identity_from_bytes(expected_decision_bytes()), "map": identity_from_bytes(expected_map_bytes())}
        print(json.dumps({"schema": "tohoku-r59-static-input-audit-v1", "status": "PASS", "errors": [], "attestation": attestation, "external": external, "projected": projected, "remaining_gaps": 27}, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(json.dumps({"schema": "tohoku-r59-stage-validation-v1", "attestation": attestation, **verify_stage(args.stage.resolve(), args.receipt)}, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
