#!/usr/bin/env python3
"""Build and seal the audited D1024/r68 mapping successor."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import types
from pathlib import Path
from typing import Any, Mapping


SCRIPT_PATH = Path(__file__).resolve()
ROOT = SCRIPT_PATH.parent.parent
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r67.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r68_contract.json"
CANONICAL_ROOT = (
    ROOT.parent
    / "interlanguage"
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "03_working_translations"
    / "tohoku_bilingual_canonical_stacks_20260804_r1"
)

ENGINE_IDENTITY = (43355, "A7D24094EE6AC30A455BFEDD813B1B65D362534D5AA512E059969C7EC3A5AACA")
CONTRACT_ID = "D1024-r68-D001048-v1"
EXPECTED_R67_RECEIPT = (11772, "5D30FF47BEA933E78FE4A6D2C8F08266475DC51009E6715E5A22D892718EC051")
EXPECTED_R67_FILES = {
    "STATUS.md": (1222, "4603500A802F817639B2E72147C5BFE2C2CADE3D50446C2712CDE57C4D0E555C"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83497, "1AA4000FB3ABF3010601723CEB492D4601EBF6248F3D4628D2158F7397ED818A"),
    "dec.csv": (389259, "F96B147AD9EBDBF386B41A4400CA132967003BF976E75311B81DA9CA3D77107E"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (487180, "7D99ADBD373B8D8D251BAA4D7E8A258AE50358F5FEBEF147D07B13B6DE63750F"),
    "mcheck.json": (73324, "016FC8B129F8B61E31DFDDDF289A69F58FEEB9D9ABBA5B2D5C97F0FF22CA76C3"),
    "stx.csv": (5289847, "3D30F990EEB11B7C509AFF9E92EAB2A94CDCCE9352535B98CEA4D91FD0951D1B"),
    "tcand.csv": (489711, "881583ED4E0390FDB6FCE4DDCB918396B947F0CA4E3EDD113EF47DB1B113FA7D"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83599, "ED5922F42855AB0D7615B7BDB5FC30A91338E5F321F4E25B1D8664387A69D775"),
    "stx.csv": (5290078, "485B3A4687F56842E778833D87ADA152A0CD10116F7144A7C9AE7F6F6931399D"),
    "tcand.csv": (489711, "2F3C060F11449AC76848A7810F8B0742291C9784A3561CA7FC245721164A59A5"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22111,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1287,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_PROJECTED = {
    "dec.csv": (390012, "0532BAB5CD37951A0885E841EF4881CBAF6A6F8C4C010F2289AFA1A03BB1DBC6"),
    "issues.csv": EXPECTED_R67_FILES["issues.csv"],
    "map.csv": (487490, "1EDF4CFB722D6EFFC601FA64E1EB3E801BF2C63D8CC973B6467FA68C647E5ED2"),
}
EXPECTED_DECISION_APPEND = (753, "D9C106CB8D4F6E18B0A819861EB66BF91F5DD2F6AFB3998E7900FB1394F50B0F")
EXPECTED_PREDECESSOR_MAP_ROW = (561, "94144CB69E919AF52E64260DB3943D1D24D9FA28DE9160BCD04FEE2BD8BAB4FE")
EXPECTED_SUCCESSOR_MAP_ROW = (871, "C21C6D567CF381DF7CC6CFAC9221045BFA9777D4BB45CC518CBD8F89AAF5A0BF")

DECISION = {
    "decision_id": "D001048",
    "unit_id": "tohoku:section:1.1:p1",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "categories-definition-category;categories-remark-category-convention-boundary",
    "rationale": "Stacks gives the shared category axioms and now records the exact convention boundary: Tohoku requires a nonempty possibly proper object class and pairwise-disjoint Hom sets, whereas the default Stacks convention is set-sized and permits the empty category. The tagged-arrow construction proves that the disjoint-Hom convention is implemented by an explicitly isomorphic category without changing the mathematical content. Selected big categories remain governed by the existing Stacks universe convention; no unrestricted proper-class foundation is claimed.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000070",
}
AUTHORIZED_DECISION = {
    "decision_id": DECISION["decision_id"],
    "unit_id": DECISION["unit_id"],
    "action": DECISION["action"],
    "disposition": DECISION["disposition"],
    "stacks_labels": DECISION["stacks_labels"],
    "official_tags": "0014",
    "rationale": DECISION["rationale"],
    "review_state": DECISION["review_state"],
    "supersedes": DECISION["supersedes"],
}
EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1048,
    "decided_units": 679,
    "source_issues": 32,
    "active_source_issues": 0,
    "review_units": 0,
    "candidate_units": 0,
    "unit_candidates": 0,
    "graph_corrections": 0,
    "active_graph_corrections": 0,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 391,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 9,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 2,
        "structural_only": 424,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1048,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 391,
    "extend_existing": 9,
    "new_statement": 2,
    "remaining_gap_class_dispositions": 18,
    "source_repairs_appended": 0,
    "mapping_closures": 1,
    "changed_map_rows": 1,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r67 dossier is preserved exactly; D001048 closes the p.122 category-convention unit in a no-overwrite r68 successor.\n"
    "- The admitted D1024 source records the exact nonempty/object-size/disjoint-Hom convention boundary and an explicitly isomorphic tagged-arrow category.\n"
    "- The D1024 audit, design, candidate, independent review, live categories TeX/PDF build, supporting build files, visual rasters, source evidence, and scanner replay are bound byte-exactly.\n"
    "- No issue or source-repair row is appended; only the authorized D000070 map row is replaced.\n"
    "- The scanner indexes 119 top-level TeX files with 22,111 labels, 683 warnings, and no errors.\n"
    "- There are 1,048 decisions, 679 decided units, 32 resolved source issues, and 18 gap-class dispositions remain.\n"
    "- GitHub availability was restored by direct user update; this bounded local transaction requires no Git or GitHub operation.\n"
    "- No unrestricted proper-class foundation, GAGA comparison, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.\n"
).encode("utf-8")

ROOT_BINDINGS = {
    "audit": ("D1024_CHECK.json", 14147, "C8D485A865FA74A7C4DC9350F2693F0F38A2DC6A6AA68B51C65A4F328F5B0070"),
    "design": ("tmp/d1024_category_convention_design.json", 3701, "F28E465DFB998786D7E3DCA31FA58CACC5B877B992CFE0BBD70BD5B13CAD2CAC"),
    "candidate": ("tmp/d1024_category_convention_candidate.tex", 1634, "8AA72971AB351F6C90D49E161D9E13F993C5F53327CCD170B7F0353D67A05EF8"),
    "review": ("tmp/d1024_independent_review_r1.json", 1250, "19EAB5440D9B678EDFB405AE9B4BB87BE89E70505964E681F9ABBBE344CE2909"),
    "categories_tex": ("categories.tex", 377883, "985DF3DBDABAC4FDF1CD9378F41406B6620B577469F403EAE7C7323D459589C3"),
    "bibliography": ("my.bib", 220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE"),
    "categories_pdf": ("categories.pdf", 1099993, "6CF58B0E153E5007F60587F943F799B7757D6F7D4A64DFE4E884787D35A5BD41"),
    "categories_aux": ("categories.aux", 31606, "93FA4AAC8F6C2B730B056AAAA6B0E30148A700BA5E826213530F5C729EA04A0D"),
    "categories_bbl": ("categories.bbl", 1482, "2D97AA0E9A1E329ADA1C2953203946178AD79D9577324891735B4DAA8F54C6F1"),
    "categories_blg": ("categories.blg", 1024, "FA3CA43F69ADEBFE9760E51A66109F5256BEF5645332B20965F2CE3D7236F185"),
    "categories_log": ("categories.log", 38413, "E11EFD348A8CBF4BF1BBD0D07138DF67831C1729261C34DC19D094B9A51C6E41"),
    "page_001": ("tmp/d1024_pdf_qa/page-001.png", 184814, "746357CADB8A62F4D29FBB10342BA6785BBAC2143364A1B54DD4A835639BC635"),
    "page_002": ("tmp/d1024_pdf_qa/page-002.png", 289465, "277670BD8A1925B38BAFBAB65D943D12F58ADD3C5A05935A65624E756E528518"),
    "page_003": ("tmp/d1024_pdf_qa/page-003.png", 320154, "5E472FEA60D664C1FFF4575F2A57FC14E487B15A09A871DCBA19C4A203C08C86"),
    "page_004": ("tmp/d1024_pdf_qa/page-004.png", 333703, "6E42C450C298E87C9DB614D344AFFE210109E36E591BD8043A830E67F87767B2"),
    "page_005": ("tmp/d1024_pdf_qa/page-005.png", 302774, "FD7A2A607F705091305F71CDD219EE48B464130E7C1166FEA58A2384AD12B342"),
}
CANONICAL_INPUTS = {
    "authority_pdf": ("authority_snapshot/jstage_part_I_9_2_119.pdf", 7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "reader_receipt": ("build/v068c3r20/build.json", 22216, "BA5D7BFDEA8F733CBA65703C5DA017E26A3FEB417297A975EBCAEFEA41D2BEA1"),
    "qa_receipt": ("qa/v68r42/check.json", 5375, "C3D039B399FDA3A2232F07A0D33ABB3E07ADEA431182FCEC26F3C8A9DFD703D0"),
    "sem_r18_nodes": ("sem/r18/nodes.csv", 585012, "3A3C9B6C22B0FA5E16466C264205D97CCA6041FF785F555A4C28F9639A50550D"),
    "sem_r18_occ": ("sem/r18/occ.csv", 515084, "54E545121F4D108E5C88B7039C39E3814F71F03332592C3F3965BD49B7FACED5"),
    "sem_r21_nodes": ("sem/r21/nodes.csv", 586416, "C0DD26F979C17DA1DA8E09CAD83FEAA44BA8644DB0625D693C3D20A8B82CCBCA"),
    "sem_r21_manifest": ("sem/r21/manifest.json", 32119, "38275B0B2BB116467B3848F2E7EB1740F3692551E531E4130E72279F47F98C59"),
    "sem_r21_validation": ("sem/r21/validation.json", 9395, "D15C85751526EA144BFA02AFBB580540C93620C7AC12A6656D1C895EEA5A8BDB"),
    "p122_dip": ("build/v068c3r20/src/dip/p122.tex", 4812, "9629B3BCE2EFF1ACA9C2A7AC5792FF6B264D6B5CF9A8AF361A556F5F513D553E"),
    "p122_fr": ("build/v068c3r20/src/fr/p122.tex", 4876, "ABB819A581B205FCA96CCA16B05E7D0F23B2400C5BB04FA596AC3F56BD69DBDF"),
    "p122_en": ("build/v068c3r20/src/en/p122.tex", 4588, "1B8FE10730454E3751DB746F1A5EA3745B7284F45ECC1C0989D0C8A47BEB7ACE"),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity_from_bytes(data: bytes) -> tuple[int, str]:
    return len(data), digest(data)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def layer_segment(page_bytes: bytes, semantic_id: str) -> bytes:
    marker = f"\\LayerTarget{{{semantic_id}}}".encode("utf-8")
    require(page_bytes.count(marker) == 1, f"{semantic_id}: LayerTarget count is not one")
    start = page_bytes.index(marker) + len(marker)
    end = page_bytes.find(b"\\LayerTarget{", start)
    return page_bytes[start:] if end < 0 else page_bytes[start:end]


def load_engine() -> types.ModuleType:
    payload = ENGINE_PATH.read_bytes()
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r67 transaction engine identity drift")
    module = types.ModuleType("tohoku_r68_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r67 transaction engine changed during load")
    return module


M = load_engine()
E = M.E


def contract_bindings() -> dict[str, Any]:
    return {role: {"path": spec[0], "bytes": spec[1], "sha256": spec[2]} for role, spec in ROOT_BINDINGS.items()}


def scanner_contract() -> dict[str, Any]:
    return {
        "oracle_path": "tmp/d1024_scan_probe_r1",
        "replay_path": "tmp/d1024_scan_probe_replay_r1",
        "files": {name: {"bytes": value[0], "sha256": value[1]} for name, value in EXPECTED_SCAN.items()},
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 683, "errors": 0},
    }


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r68 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r68-transaction-contract-v1" and contract.get("contract_id") == CONTRACT_ID, "r68 contract identity mismatch")
    script = contract.get("script", {})
    require(script.get("path") == "srcmap/build_tohoku_r68.py" and identity_from_bytes(SCRIPT_PATH.read_bytes()) == (script.get("bytes"), script.get("sha256")), "r68 script pin mismatch")
    engine = contract.get("engine", {})
    require(engine.get("path") == "srcmap/build_tohoku_r67.py" and (engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r68 engine pin mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r67/r67-check.json", "bytes": EXPECTED_R67_RECEIPT[0], "sha256": EXPECTED_R67_RECEIPT[1]}, "r68 predecessor contract mismatch")
    require(contract.get("frozen_prerequisite") == contract_bindings()["audit"] and contract.get("bound_inputs") == contract_bindings(), "r68 bound inputs mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r68 scanner contract mismatch")
    require(contract.get("decision") == AUTHORIZED_DECISION and contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r68 authorized decision/count mismatch")
    require(contract.get("target") == "tohoku_r68", "r68 target mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r67" and transaction.get("stage") == ".tohoku-r68-txn", "r68 transaction paths mismatch")
    require(transaction.get("no_overwrite") is True and transaction.get("atomic_directory_rename") is True and transaction.get("post_promotion_replay") is True, "r68 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r68.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r68_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r67.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    require(json.loads(data.decode("utf-8")).get("dossier_id") == "tohoku_r62", "inherited cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "inherited r68 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1047 and rows[-1]["decision_id"] == "D001047", "r67 decision schema/count/tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, [DECISION], header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001048 append row drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "projected r68 decision bytes drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "inherited r68 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r67 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r67 map schema/count drift")
    selected = E.one_row(rows, "unit_id", DECISION["unit_id"], "r67 map")
    require(selected["decision_id"] == "D000070" and selected["disposition"] == "extend_existing" and selected["review_state"] == "reviewed_gap", "r67 D1024 target state drift")
    require(selected["stacks_labels"] == "categories-definition-category" and selected["stacks_tags"] == "0014", "r67 D1024 predecessor label/tag drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:861", "r67 D1024 source locator drift")
    replacement = selected.copy()
    replacement.update({
        "decision_id": DECISION["decision_id"],
        "disposition": DECISION["disposition"],
        "review_state": DECISION["review_state"],
        "stacks_labels": DECISION["stacks_labels"],
        "stacks_tags": AUTHORIZED_DECISION["official_tags"],
        "rationale": DECISION["rationale"],
    })
    data = E.csv_bytes(fields, [replacement if row["unit_id"] == DECISION["unit_id"] else row for row in rows])
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "projected r68 map bytes drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r67-check.json"
    E.require_identity(receipt, EXPECTED_R67_RECEIPT, "r67 receipt")
    for name, expected in EXPECTED_R67_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r67/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r67-v1" and value.get("status") == "PASS" and value.get("errors") == [], "r67 receipt state drift")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 19, "r67 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R67_FILES), "r67 receipt inventory drift")
    require({row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records} == EXPECTED_R67_FILES, "r67 receipt file identities drift")
    require(E.line_identity(E.SOURCE / "map.csv", 861) == EXPECTED_PREDECESSOR_MAP_ROW, "r67 target map row drift")
    return {"receipt": E.record(receipt, "tohoku_r67/r67-check.json")}


def read_spec(root: Path, spec: tuple[str, int, str], label: str) -> tuple[Path, bytes]:
    path = root / spec[0]
    return path, E.require_identity(path, (spec[1], spec[2]), label)


def verify_external() -> dict[str, Any]:
    execution = load_contract()
    predecessor = verify_predecessor()
    bindings = contract_bindings()
    paths = {role: ROOT / spec["path"] for role, spec in bindings.items()}
    for role, path in paths.items():
        spec = bindings[role]
        E.require_identity(path, (spec["bytes"], spec["sha256"]), f"D1024 {role}")
    audit = E.strict_json(paths["audit"])
    design = E.strict_json(paths["design"])
    review = E.strict_json(paths["review"])
    require(audit.get("schema") == "tohoku-stacks-d1024-check-v1" and audit.get("formalization_id") == "D1024", "D1024 audit identity drift")
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R68_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1024 audit state drift")
    selection = audit.get("selection", {})
    require(selection.get("unit") == DECISION["unit_id"] and selection.get("source_locator") == "sem/r18/nodes.csv:861", "D1024 selection drift")
    require(selection.get("predecessor_decision") == "D000070" and selection.get("predecessor_dossier") == "tohoku_r67", "D1024 predecessor selection drift")
    require(selection.get("predecessor_map_row_with_lf") == {"physical_line": 861, "bytes": EXPECTED_PREDECESSOR_MAP_ROW[0], "sha256": EXPECTED_PREDECESSOR_MAP_ROW[1]}, "D1024 predecessor row binding drift")
    require(audit.get("source_claim", {}).get("source_repair_required") is False and audit.get("source_claim", {}).get("transcription_or_translation_repair_required") is False, "D1024 unexpected source repair")
    evidence = audit.get("design_and_independent_review", {})
    for key, role in (("design", "design"), ("candidate", "candidate"), ("independent_review", "review")):
        value = evidence.get(key, {})
        require(value.get("path") == ROOT_BINDINGS[role][0] and (value.get("bytes"), value.get("sha256")) == ROOT_BINDINGS[role][1:], f"D1024 {key} binding drift")
    require(evidence.get("post_live_mathematical_review", {}).get("status") == "STRICT_PASS" and evidence.get("post_live_source_and_mapping_review", {}).get("status") == "STRICT_PASS", "D1024 post-live review drift")
    require(evidence.get("post_live_source_and_mapping_review", {}).get("replace_only") == "D000070", "D1024 post-live map scope drift")
    edit = audit.get("stacks_edit", {})
    require((edit.get("postimage", {}).get("bytes"), edit.get("postimage", {}).get("sha256")) == ROOT_BINDINGS["categories_tex"][1:], "D1024 live TeX evidence drift")
    require(edit.get("new_block") == {"lines": "117--152", "crlf_bytes": 1670, "crlf_sha256": "EFE81A677512F30772E94B1B074751AEAF3252FDD37C3041B666A1090CEC7CFD", "lf_normalized_bytes": 1634, "lf_normalized_sha256": "8AA72971AB351F6C90D49E161D9E13F993C5F53327CCD170B7F0353D67A05EF8", "byte_identical_to_lf_candidate_after_normalization": True}, "D1024 block evidence drift")
    require(edit.get("new_raw_label") == {"label": "remark-category-convention-boundary", "line": 118, "occurrences": 1}, "D1024 raw-label evidence drift")
    require(edit.get("source_citation_occurrences") == 1 and edit.get("unrelated_live_source_files_changed_by_insertion") == 0, "D1024 insertion scope drift")
    pdf = audit.get("pdf_build", {})
    require((pdf.get("postimage", {}).get("bytes"), pdf.get("postimage", {}).get("sha256")) == ROOT_BINDINGS["categories_pdf"][1:], "D1024 live PDF evidence drift")
    require(pdf.get("postimage", {}).get("pages") == 107 and pdf.get("postimage", {}).get("pdf_version") == "1.5" and pdf.get("final_driver_exit_code") == 0, "D1024 PDF gate drift")
    diagnostics = pdf.get("diagnostics", {})
    require(all(diagnostics.get(key) == 0 for key in ("fatal_tex_errors", "latex_errors", "undefined_control_sequences", "undefined_references", "undefined_citations", "rerun_requests", "bibtex_warnings", "inserted_line_interval_overfull_findings")), "D1024 PDF diagnostic drift")
    require(diagnostics.get("preexisting_or_unrelated_global_overfull_findings") == 4, "D1024 preexisting diagnostic count drift")
    for key, role in (("aux", "categories_aux"), ("bbl", "categories_bbl"), ("blg", "categories_blg"), ("log", "categories_log")):
        value = pdf.get("supporting_files", {}).get(key, {})
        require((value.get("bytes"), value.get("sha256")) == ROOT_BINDINGS[role][1:], f"D1024 {key} binding drift")
    visual = audit.get("visual_qa", {})
    require(visual.get("status") == "STRICT_PASS" and visual.get("defects") == [] and visual.get("inspected_pdf_pages") == [1, 2, 3, 4, 5], "D1024 visual QA drift")
    require(len(visual.get("rasters", [])) == 5, "D1024 raster count drift")
    for row, page in zip(visual.get("rasters", []), range(1, 6)):
        role = f"page_{page:03d}"
        require(row.get("path") == ROOT_BINDINGS[role][0] and (row.get("bytes"), row.get("sha256")) == ROOT_BINDINGS[role][1:], f"D1024 page {page} raster drift")
    probe = audit.get("scanner_probe", {})
    require(probe.get("status") == "PASS_BYTE_IDENTICAL_REPLAY" and probe.get("oracle_path") == scanner_contract()["oracle_path"] and probe.get("replay_path") == scanner_contract()["replay_path"], "D1024 scanner audit state/path drift")
    require(probe.get("files") == scanner_contract()["files"], "D1024 scanner file identities drift")
    require(probe.get("counts") == {"tex_files": 119, "labels": 22111, "official_tags_joined": 21437, "topics": 13, "topic_candidates": 1287, "direct_topic_coverage": 13, "warnings": 683, "errors": 0}, "D1024 scanner counts drift")
    require(probe.get("complete_inventory") == {"files": 6, "bytes": 5873416, "surface_bytes": 483, "surface_sha256": "C8D7C2ACD286802639CE873EF5B614B458281F0CE841ABD2509409AABAB34AFC"}, "D1024 scanner inventory drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("status") == "AUTHORIZED_FOR_NO_OVERWRITE_R68_TRANSACTION" and authorization.get("predecessor") == "tohoku_r67" and authorization.get("successor") == "tohoku_r68", "D1024 mapping authorization lineage drift")
    require(authorization.get("decision") == AUTHORIZED_DECISION and authorization.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "D1024 authorized decision/count drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1024 append authorization drift")
    replacement = authorization.get("map_replacement", {})
    require(replacement.get("physical_line") == 861 and replacement.get("source_locator_preserved") == "sem/r18/nodes.csv:861", "D1024 map locator drift")
    require(set(replacement.get("only_fields_changed", [])) == {"decision_id", "disposition", "review_state", "stacks_labels", "official_tags", "rationale"}, "D1024 authorized field set drift")
    require(design.get("schema") == "tohoku-stacks-d1024-design-v1" and design.get("formalization_id") == "D1024" and design.get("status") == "STRICT_PASS_READY_FOR_LIVE_INSERTION_AFTER_R67_SEALS", "D1024 design state drift")
    projection = design.get("projected_mapping", {})
    require(projection.get("expected_decision_after_D1023") == "D001048" and projection.get("replace_only") == "D000070", "D1024 design map lineage drift")
    require(projection.get("stacks_labels") == DECISION["stacks_labels"] and projection.get("official_tags") == "0014" and projection.get("issue_append") is None and projection.get("source_repair_append") is None, "D1024 design mapping drift")
    require(review.get("schema") == "tohoku-stacks-d1024-independent-review-v1" and review.get("formalization_id") == "D1024" and review.get("status") == "STRICT_PASS_FOR_LIVE_INSERTION_AFTER_R67_SEALS" and review.get("errors") == [], "D1024 review state drift")
    require(review.get("mathematical_review", {}).get("status") == "STRICT_PASS" and review.get("source_and_mapping_review", {}).get("status") == "STRICT_PASS", "D1024 independent review verdict drift")
    require(review.get("source_and_mapping_review", {}).get("replace_only") == "D000070" and review.get("source_and_mapping_review", {}).get("projected_labels") == DECISION["stacks_labels"] and review.get("source_and_mapping_review", {}).get("projected_tag") == "0014", "D1024 independent mapping drift")
    source_bytes = paths["categories_tex"].read_bytes()
    block = b"".join(source_bytes.splitlines(keepends=True)[116:152])
    candidate = paths["candidate"].read_bytes()
    require(block == candidate, "D1024 candidate/live block mismatch")
    require(
        identity_from_bytes(block.replace(b"\n", b"\r\n"))
        == (1670, "EFE81A677512F30772E94B1B074751AEAF3252FDD37C3041B666A1090CEC7CFD"),
        "D1024 constructed CRLF block identity drift",
    )
    raw_label = b"\\label{remark-category-convention-boundary}"
    citation = b"\\cite[Chapter I, Section 1.1, p. 122]{Tohoku}"
    require(source_bytes.count(raw_label) == 1 and block.count(raw_label) == 1 and source_bytes.count(citation) == 1 and block.count(citation) == 1, "D1024 label/citation cardinality drift")
    require(paths["bibliography"].read_bytes().count(b"@ARTICLE{Tohoku,") == 1, "Tohoku bibliography key drift")
    require(paths["categories_aux"].read_bytes().count(pdf.get("new_label_aux_record", "").encode("utf-8")) == 1, "D1024 aux record drift")
    canonical: dict[str, Any] = {}
    values: dict[str, Any] = {}
    page_bytes: dict[str, bytes] = {}
    for role, spec in CANONICAL_INPUTS.items():
        path, data = read_spec(CANONICAL_ROOT, spec, role)
        canonical[role] = E.record(path, spec[0])
        if spec[0].endswith(".json"):
            values[role] = json.loads(data.decode("utf-8"))
        if role.startswith("p122_"):
            page_bytes[role.removeprefix("p122_")] = data
    require(values["reader_receipt"].get("status") == "PASS" and values["reader_receipt"].get("revision") == "v068c3r20", "reader receipt drift")
    require(values["qa_receipt"].get("status") == "PASS" and values["qa_receipt"].get("qa_revision") == "v68r42", "QA receipt drift")
    require(values["sem_r21_manifest"].get("schema") == "tohoku-semantic-local-successor-manifest-v21" and values["sem_r21_validation"].get("status") == "PASS", "sem/r21 receipt drift")
    semantic_row = (820, "254395E1D5A5D0EE45F6BE6178B316AB6C7924DAAC9F7B0072A5351BF5982265")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 861) == semantic_row and E.line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 861) == semantic_row, "D1024 semantic row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/occ.csv", 71) == (475, "37B2459004875B04A61AADB7FB3EA359C9C75A971227D0383FB79D99B6E3377A"), "D1024 occurrence drift")
    segments = {
        "dip": (1078, "6B3CB609486A78966DFC2B784FC37DF3A625870E2BE644A900D7E47C183BC9C2"),
        "fr": (1078, "6B3CB609486A78966DFC2B784FC37DF3A625870E2BE644A900D7E47C183BC9C2"),
        "en": (987, "3EB75C8F12BB187861B4BEF8A2BB5DDF46466F1984F3EE7F2B431CD35754D065"),
    }
    for layer, data in page_bytes.items():
        require(identity_from_bytes(layer_segment(data, DECISION["unit_id"])) == segments[layer], f"D1024 {layer} segment drift")
    stacks = {role: E.record(path, bindings[role]["path"]) for role, path in paths.items()}
    return {"execution": execution, "predecessor": predecessor, "stacks": stacks, "canonical": canonical}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == E.ORACLE_PAYLOAD and not any(path.is_dir() for path in root.iterdir()), f"scanner oracle surface drift: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [] and check.get("counts") == EXPECTED_SCAN_COUNTS and len(check.get("warnings", [])) == 683, "r68 scanner state/count drift")
    require(check.get("tex_sha256", {}).get("categories.tex") == ROOT_BINDINGS["categories_tex"][2], "r68 scanner categories binding drift")
    label = "categories-remark-category-convention-boundary"
    _, rows = E.load_csv(root / "stx.csv")
    row = E.one_row(rows, "full_label", label, "r68 scanner new label")
    require(row["file"] == "categories.tex" and row["line"] == "118" and row["tag"] == "" and row["text_sha256"] == "6723C70817DBA81D95349E21EBA26DE6CEE3E283295ED5F83AA1A556925CDD7C", "r68 scanner new-label row drift")
    require(E.line_identity(root / "stx.csv", 2228) == (228, "6110B54463DFFF5EA0EBBF339339188F4B30D7425ED80EBFA361ED0542EF1B82"), "r68 scanner new-label row identity drift")
    return check


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink() and E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "D1024 scanner oracle/replay missing or unsafe")
    verify_scan(E.ORACLE, oracle_surface=True)
    verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"D1024 scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1024_scan_probe_r1/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1024_scan_probe_replay_r1/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"missing or unsafe r68 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r68-check.json"} if receipt_mode else set()) and not any(path.is_dir() for path in root.iterdir()), "r68 output surface drift")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r68 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"inherited r68 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes() and (root / "map.csv").read_bytes() == expected_map_bytes(), "r68 decision/map drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r68 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R67_FILES["ucand.csv"], "r68/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [] and mcheck.get("counts") == EXPECTED_COUNTS and len(mcheck.get("warnings", [])) == 683, "r68 mapping state/count drift")
    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1049)] and decisions[-1] == DECISION, "r68 decision sequence/tail drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r68 issue sequence drift")
    selected = E.one_row(mapping, "unit_id", DECISION["unit_id"], "r68 map")
    require(selected["decision_id"] == "D001048" and selected["disposition"] == "existing_equivalent" and selected["review_state"] == DECISION["review_state"], "r68 target state drift")
    require(selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "0014" and selected["source_loc"] == "sem/r18/nodes.csv:861", "r68 target label/tag/locator drift")
    require(E.line_identity(root / "map.csv", 861) == EXPECTED_SUCCESSOR_MAP_ROW, "r68 target map row identity drift")
    deltas = E.map_row_delta()
    require(len(deltas) == 5 and {row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r68 map delta cardinality/scope drift")
    require({row["field"] for row in deltas} == {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"}, "r68 actual changed-field set drift")
    remaining = sum(1 for row in mapping if row["disposition"] in {"existing_weaker", "extend_existing", "new_section", "new_statement"})
    require(remaining == 18, "r68 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1048,
        "decisions_appended": ["D001048"],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 683, "errors": 0},
        "remaining_gap_class_dispositions": 18,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 5, "unchanged_units": 990, "authorized_but_value_preserved": ["stacks_tags"]},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1024_ADMITTED_CATEGORIES_TEX_AND_PDF_NO_BIBLIOGRAPHY_CHANGE",
        "scanner_payload_change": "D1024_ONE_NEW_CATEGORY_LABEL_WITH_LINE_ONLY_CANDIDATE_SHIFTS",
    }
    if receipt_mode:
        require(E.strict_json(root / "r68-check.json") == receipt_payload(root, result), "r68 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    stacks = external["stacks"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r68-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": stacks["audit"],
            "design": stacks["design"],
            "candidate": stacks["candidate"],
            "independent_review": stacks["review"],
            "bibliography": stacks["bibliography"],
            "live_source": stacks["categories_tex"],
            "live_pdf": stacks["categories_pdf"],
            "build_support": {key: stacks[key] for key in ("categories_aux", "categories_bbl", "categories_blg", "categories_log")},
            "visual_rasters": [stacks[f"page_{page:03d}"] for page in range(1, 6)],
            "change_class": "admitted_live_source_and_pdf_no_bibliography_change_plus_mapping_successor",
        },
        "source_chain": {
            "authority_pdf": external["canonical"]["authority_pdf"],
            "reader_receipt": external["canonical"]["reader_receipt"],
            "qa_receipt": external["canonical"]["qa_receipt"],
            "sem_r18_nodes": external["canonical"]["sem_r18_nodes"],
            "sem_r18_occ": external["canonical"]["sem_r18_occ"],
            "sem_r21_manifest": external["canonical"]["sem_r21_manifest"],
            "sem_r21_validation": external["canonical"]["sem_r21_validation"],
            "sem_r21_nodes": external["canonical"]["sem_r21_nodes"],
        },
        "scanner_oracle": oracles["oracle"],
        "scanner_replay": oracles["replay"],
        "external_constraints": {"github": {"status": "available_by_direct_user_update", "action": "No Git or GitHub operation was required or attempted."}},
        "deltas": dict(deltas),
        "files": E.output_records(root),
        "nonclaims": [
            "D001048 closes only the p.122 category-convention boundary unit.",
            "The tagged-arrow construction does not provide an unrestricted foundation for arbitrary proper-class categories.",
            "No issue, source repair, semantic successor, GAGA comparison, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r67"
    E.TARGET = ROOT / "tohoku_r68"
    E.STAGE = ROOT / ".tohoku-r68-txn"
    E.ORACLE = ROOT / "tmp" / "d1024_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1024_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R67_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R67_FILES
    E.EXPECTED_SCAN = EXPECTED_SCAN
    E.EXPECTED_SCAN_COUNTS = EXPECTED_SCAN_COUNTS
    E.EXPECTED_PROJECTED = EXPECTED_PROJECTED
    E.EXPECTED_APPEND_ROWS = {"decision": EXPECTED_DECISION_APPEND}
    E.EXPECTED_PREDECESSOR_MAP_ROW = EXPECTED_PREDECESSOR_MAP_ROW
    E.EXPECTED_SUCCESSOR_MAP_ROW = EXPECTED_SUCCESSOR_MAP_ROW
    E.DECISION = DECISION
    E.EXPECTED_COUNTS = EXPECTED_COUNTS
    E.STATUS_BYTES = STATUS_BYTES
    E.STACKS_INPUTS = {"categories_tex": ("categories.tex", ROOT_BINDINGS["categories_tex"][1], ROOT_BINDINGS["categories_tex"][2])}
    E.load_contract = load_contract
    E.expected_cfg_bytes = expected_cfg_bytes
    E.expected_decision_bytes = expected_decision_bytes
    E.expected_issue_bytes = expected_issue_bytes
    E.expected_map_bytes = expected_map_bytes
    E.verify_predecessor = verify_predecessor
    E.verify_external = verify_external
    E.verify_scan = verify_scan
    E.verify_oracles = verify_oracles
    E.verify_stage = verify_stage
    E.receipt_payload = receipt_payload


configure_engine()


def verify_scanner_oracles() -> None:
    load_contract()
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r68 target or stage already exists")
    print(json.dumps({"schema": "tohoku-r68-scanner-oracle-v1", "status": "PASS_REPLAY", "errors": [], "scanner_oracles": verify_oracles(), "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 683, "errors": 0}}, indent=2, sort_keys=True))


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r68 target or stage already exists")
    external = verify_external()
    oracles = verify_oracles()
    projection = {
        "cfg.json": identity_from_bytes(expected_cfg_bytes()),
        "dec.csv": identity_from_bytes(expected_decision_bytes()),
        "issues.csv": identity_from_bytes(expected_issue_bytes()),
        "map.csv": identity_from_bytes(expected_map_bytes()),
        "STATUS.md": identity_from_bytes(STATUS_BYTES),
    }
    print(json.dumps({"schema": "tohoku-r68-static-input-audit-v1", "status": "PASS", "errors": [], "external": external, "scanner_oracles": oracles, "projection": projection, "decision": "D001048", "issue": None, "source_repair": None, "remaining_gaps": 18}, indent=2, sort_keys=True))


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r68 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    E.exclusive_write(E.STAGE / "r68-check.json", E.json_bytes(receipt_payload(E.STAGE, deltas)))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r68 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("post-promotion r68 replay failed; target rolled back") from exc
    print(json.dumps({"schema": "tohoku-r68-transaction-result-v1", "status": "PASS_COMMITTED", "errors": [], "target": "tohoku_r68", "receipt": E.record(E.TARGET / "r68-check.json"), "remaining_gaps": 18}, indent=2, sort_keys=True))


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink() and not E.STAGE.exists(), "r68 target/stage state invalid")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(json.dumps({"schema": "tohoku-r68-replay-v1", "status": "PASS_REPLAY", "errors": [], "receipt": E.record(E.TARGET / "r68-check.json"), "deltas": result}, indent=2, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("oracle", "preflight", "execute", "replay"))
    args = parser.parse_args()
    try:
        {"oracle": verify_scanner_oracles, "preflight": preflight, "execute": execute, "replay": replay}[args.mode]()
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
