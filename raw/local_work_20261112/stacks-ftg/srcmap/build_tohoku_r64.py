#!/usr/bin/env python3
"""Specialize the sealed r63 transaction surface for D1020/r64."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
import types
from pathlib import Path
from typing import Any, Mapping


SCRIPT_PATH = Path(__file__).resolve()
ROOT = SCRIPT_PATH.parent.parent
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r63.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r64_contract.json"
DOCUMENTS = ROOT.parent
CANONICAL_ROOT = (
    DOCUMENTS
    / "interlanguage"
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "03_working_translations"
    / "tohoku_bilingual_canonical_stacks_20260804_r1"
)

ENGINE_IDENTITY = (40798, "1E9A7181BC25D5797794D80EB68D63150AE9C5673EDE666A3A082F358DA46CF4")
CONTRACT_ID = "D1020-r64-D001044-v1"
EXPECTED_R63_RECEIPT = (10116, "0785CDEC7D385B8BDA435F37C05A169101C59F402C56B9610DD40683FD6ADE72")
EXPECTED_R63_FILES = {
    "STATUS.md": (1184, "F214B696C3490AA3C73662CE516E6AF5A6E5D0AC07E699E53B48F35AB7351390"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (82761, "57643A9EE276EC4ABE1ECD8955E4FAC84FFB52504CBA0C5D60992986811F0726"),
    "dec.csv": (386189, "2ECE3DF81EB51B54E2BE11A9B60B7DB10A216F40CAA978C7AAF76D18E7E6EED6"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (485515, "ED83B6A2879F06162978CD69B15BA9EAA7367F875B87CB46ABA63167DAAF76FA"),
    "mcheck.json": (72588, "4C18D9D76606B87E689180BCEEB89FE9897BFD63E9CF9C0B5D89871B644C2E5E"),
    "stx.csv": (5288027, "681364D9AFF58762102B89B5DFA018A3D38F8012C59DFA33544DBF7DC94B7542"),
    "tcand.csv": (489256, "00D7DA1CBFFE74EC58F7149CB9EB335FF6CE1DBA05BED1EEFCED9921D5047101"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83022, "CA4BD4D6C25E995CF422795472D17E039CBD260F1D17B16915DF5245B4CB272E"),
    "stx.csv": (5288663, "01C9089B9AF31597C7FD787C37D31C7FCB5A052DED324EDB3648FEEAC083DAEC"),
    "tcand.csv": (489256, "73C6BFD919058171C14E2CDEC94F47DDBFF389636BDA7250BE4B6BBE7BC29357"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22106,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1286,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_PROJECTED = {
    "dec.csv": (386884, "744676FA92F8508F4A14B3271F1B22016AA751B6606A4C560BCEB035531D4115"),
    "issues.csv": EXPECTED_R63_FILES["issues.csv"],
    "map.csv": (485864, "28B10AF238AFB630F03D5F23460EED96C95A68BC3FE33736598FA6678C403A52"),
}
EXPECTED_DECISION_APPEND = (695, "5B5E8C873DC7ED5C09B212BE297BA86F97C67DB03B4311B8B87EF8D4D92C5973")
EXPECTED_PREDECESSOR_MAP_ROW = (464, "E27526FEF71B946D33D28AB53EFDB099FCF89446DCA68931D70CF34E29AE8252")
EXPECTED_SUCCESSOR_MAP_ROW = (813, "C09ABAF49E7C2D6565B26062C7838F8B4F1C0A90A8F381F09844E54C751BBAA0")
EXPECTED_AUDIT = (14789, "E03C0BDB19BB564CEC782124367D6CD053624551F847F64885E6ECC1A7E4B083")
EXPECTED_CANDIDATE = (4937, "CBF6FA0EE8451F0CBC8793EBDE2C2D7377696E92A2ABCBF39B4595734C34CF3E")
EXPECTED_DESIGN = (7209, "E83A9DD2C0C3F8D82371330F214BB2804D0B44D8CB3C2CB33C7127568B65AFF6")
EXPECTED_REVIEW = (2630, "25DF060091E9E63EF795DD862152877D2D3964510E41B3F13B71B164FBA13567")
EXPECTED_COHOMOLOGY_TEX = (927351, "934223B83092E38F7184DE6B739569002BFCBE9F934A5AA9212EBF78AD8424CA")
EXPECTED_BIBLIOGRAPHY = (220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE")
EXPECTED_COHOMOLOGY_PDF = (2020550, "4B55BF958522964140AD364EF911F71DEA72455DA709E80176AC707381786C2E")

DECISION = {
    "decision_id": "D001044",
    "unit_id": "tohoku:equivalence:equivariant-holomorphic-bundles",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-equivariant-holomorphic-vector-bundles-locally-free-modules",
    "rationale": "The analytic vector-bundle/locally-free-module equivalence and its equivariant restriction are now proved in Stacks. Compatible holomorphic fibrewise-linear G-actions correspond exactly to semilinear G-O_X-module structures on locally free analytic modules, with full faithfulness and essential surjectivity. The adjacent nonequivariant source unit D000615, extension classification, H^1, quotient descent, compactness, finite dimensionality, and GAGA are not mapped here.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000614",
}
AUTHORIZED_DECISION = {
    "decision_id": DECISION["decision_id"],
    "unit_id": DECISION["unit_id"],
    "action": DECISION["action"],
    "disposition": DECISION["disposition"],
    "stacks_labels": DECISION["stacks_labels"],
    "official_tags": "",
    "rationale": DECISION["rationale"],
    "review_state": DECISION["review_state"],
    "supersedes": DECISION["supersedes"],
}
EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1044,
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
        "existing_equivalent": 387,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 4,
        "structural_only": 424,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1044,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 387,
    "new_statement": 4,
    "remaining_gap_class_dispositions": 22,
    "source_repairs_appended": 0,
    "mapping_closures": 1,
    "changed_map_rows": 1,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r63 dossier is preserved exactly; D001044 closes the p.219 equivariant holomorphic-bundle equivalence in a no-overwrite r64 successor.\n"
    "- The new equivariant lemma proves the equivalence with semilinear locally free analytic modules; the adjacent nonequivariant source unit D000615 remains separate.\n"
    "- The D1020 audit, candidate, design, independent review, bibliography, cohomology source, and cohomology PDF are bound byte-exactly.\n"
    "- No issue or source-repair row is appended; the inherited cfg namespace is retained and the scanner is rebound to the exact live source bytes.\n"
    "- The scanner indexes 119 top-level TeX files with 22,106 labels, 678 warnings, and no errors.\n"
    "- There are 1,044 decisions, 679 decided units, 32 resolved source issues, and 22 gap-class dispositions remain.\n"
    "- GitHub availability was restored by direct user update; this bounded local transaction requires no Git or GitHub operation.\n"
    "- No claim is made for D000615, extension classification, H^1, quotient descent, compactness, finite dimensionality, GAGA, release, publication, DOI, remote-freshness, rights, or whole-paper completion.\n"
).encode("utf-8")

CANONICAL_INPUTS = {
    "authority_pdf": ("authority_snapshot/jstage_part_II_9_3_185.pdf", 3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
    "source_receipt": ("production/p185_fix2/check.json", 5291, "E54AE998A9D8AB863652521E329731789727DD064B48E6A52CAB83584C802EEA"),
    "reader_receipt": ("build/v068c3r20/build.json", 22216, "BA5D7BFDEA8F733CBA65703C5DA017E26A3FEB417297A975EBCAEFEA41D2BEA1"),
    "qa_receipt": ("qa/v68r42/check.json", 5375, "C3D039B399FDA3A2232F07A0D33ABB3E07ADEA431182FCEC26F3C8A9DFD703D0"),
    "sem_r18_nodes": ("sem/r18/nodes.csv", 585012, "3A3C9B6C22B0FA5E16466C264205D97CCA6041FF785F555A4C28F9639A50550D"),
    "sem_r21_nodes": ("sem/r21/nodes.csv", 586416, "C0DD26F979C17DA1DA8E09CAD83FEAA44BA8644DB0625D693C3D20A8B82CCBCA"),
    "sem_r21_manifest": ("sem/r21/manifest.json", 32119, "38275B0B2BB116467B3848F2E7EB1740F3692551E531E4130E72279F47F98C59"),
    "sem_r21_validation": ("sem/r21/validation.json", 9395, "D15C85751526EA144BFA02AFBB580540C93620C7AC12A6656D1C895EEA5A8BDB"),
    "p219_dip": ("build/v068c3r20/src/dip/p219.tex", 4809, "53B23B8B039FA4BD34EB83A6F5E02B18758614E17A5737723A854F72C3A225B1"),
    "p219_fr": ("build/v068c3r20/src/fr/p219.tex", 4814, "0B11034BB5735A95DD5849B9FDCD6277A47D6A5E2AB57B25A54B8C87A0BC3FAE"),
    "p219_en": ("build/v068c3r20/src/en/p219.tex", 4520, "96C843642C094D827A66D6B154198C5B8E9E25F2EAB96E516F8F6CB9BF9A6088"),
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
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r63 transaction engine identity drift")
    module = types.ModuleType("tohoku_r64_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r63 transaction engine changed during load")
    return module


M = load_engine()
E = M.E


def contract_bindings() -> dict[str, Any]:
    return {
        "audit": {"path": "D1020_CHECK.json", "bytes": EXPECTED_AUDIT[0], "sha256": EXPECTED_AUDIT[1]},
        "candidate": {"path": "tmp/d1020_equivariant_holomorphic_bundles_candidate.tex", "bytes": EXPECTED_CANDIDATE[0], "sha256": EXPECTED_CANDIDATE[1]},
        "design": {"path": "tmp/d1020_equivariant_holomorphic_bundles_design.json", "bytes": EXPECTED_DESIGN[0], "sha256": EXPECTED_DESIGN[1]},
        "review": {"path": "tmp/d1020_independent_review_r1.json", "bytes": EXPECTED_REVIEW[0], "sha256": EXPECTED_REVIEW[1]},
        "cohomology_tex": {"path": "cohomology.tex", "bytes": EXPECTED_COHOMOLOGY_TEX[0], "sha256": EXPECTED_COHOMOLOGY_TEX[1]},
        "bibliography": {"path": "my.bib", "bytes": EXPECTED_BIBLIOGRAPHY[0], "sha256": EXPECTED_BIBLIOGRAPHY[1]},
        "cohomology_pdf": {"path": "cohomology.pdf", "bytes": EXPECTED_COHOMOLOGY_PDF[0], "sha256": EXPECTED_COHOMOLOGY_PDF[1]},
    }


def scanner_contract() -> dict[str, Any]:
    return {
        "oracle_path": "tmp/d1020_scan_probe_r1",
        "replay_path": "tmp/d1020_scan_probe_replay_r1",
        "files": {name: {"bytes": expected[0], "sha256": expected[1]} for name, expected in EXPECTED_SCAN.items()},
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 678, "errors": 0},
    }


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r64 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r64-transaction-contract-v1", "r64 contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "r64 contract ID mismatch")
    spec = contract.get("script")
    require(isinstance(spec, dict) and spec.get("path") == "srcmap/build_tohoku_r64.py", "r64 script pin missing")
    require(identity_from_bytes(SCRIPT_PATH.read_bytes()) == (spec.get("bytes"), spec.get("sha256")), "r64 script identity mismatch")
    engine = contract.get("engine")
    require(isinstance(engine, dict) and engine.get("path") == "srcmap/build_tohoku_r63.py", "r64 engine path mismatch")
    require((engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r64 engine contract mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r63/r63-check.json", "bytes": EXPECTED_R63_RECEIPT[0], "sha256": EXPECTED_R63_RECEIPT[1]}, "r64 predecessor contract mismatch")
    require(contract.get("frozen_prerequisite") == contract_bindings()["audit"], "r64 audit contract mismatch")
    require(contract.get("bound_inputs") == contract_bindings(), "r64 bound-input contract mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r64 scanner contract mismatch")
    require(contract.get("decision") == AUTHORIZED_DECISION, "r64 decision contract mismatch")
    require(contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r64 projected-count contract mismatch")
    require(contract.get("target") == "tohoku_r64", "r64 target contract mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r63" and transaction.get("stage") == ".tohoku-r64-txn", "r64 transaction paths mismatch")
    require(transaction.get("no_overwrite") is True and transaction.get("atomic_directory_rename") is True and transaction.get("post_promotion_replay") is True, "r64 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r64.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r64_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r63.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    cfg = json.loads(data.decode("utf-8"))
    require(cfg.get("dossier_id") == "tohoku_r62", "inherited cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "Inherited r64 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1043, "r63 decision schema/count drift")
    require(rows[-1]["decision_id"] == "D001043", "r63 decision tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, [DECISION], header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001044 append-row drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "Projected r64 decisions drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "Inherited r64 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r63 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r63 map schema/count drift")
    selected = E.one_row(rows, "unit_id", DECISION["unit_id"], "r63 map")
    require(selected["decision_id"] == "D000614" and selected["disposition"] == "new_statement", "r63 D1020 target state drift")
    require(selected["review_state"] == "reviewed_new_statement", "r63 D1020 review-state drift")
    require(selected["stacks_labels"] == "groupoids-definition-equivariant-module", "r63 D1020 predecessor labels drift")
    require(selected["stacks_tags"] == "03LF", "r63 D1020 predecessor tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:561", "r63 D1020 source locator drift")
    replacement = selected.copy()
    replacement.update(
        {
            "decision_id": DECISION["decision_id"],
            "disposition": DECISION["disposition"],
            "review_state": DECISION["review_state"],
            "stacks_labels": DECISION["stacks_labels"],
            "stacks_tags": "",
            "rationale": DECISION["rationale"],
        }
    )
    data = E.csv_bytes(fields, [replacement if row["unit_id"] == DECISION["unit_id"] else row for row in rows])
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "Projected r64 map drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r63-check.json"
    E.require_identity(receipt, EXPECTED_R63_RECEIPT, "r63 receipt")
    for name, expected in EXPECTED_R63_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r63/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r63-v1", "r63 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r63 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 23, "r63 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R63_FILES), "r63 receipt inventory drift")
    replay = {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records}
    require(replay == EXPECTED_R63_FILES, "r63 receipt file identities drift")
    require(E.line_identity(E.SOURCE / "map.csv", 561) == EXPECTED_PREDECESSOR_MAP_ROW, "r63 target map row drift")
    return {"receipt": E.record(receipt, "tohoku_r63/r63-check.json")}


def read_spec(root: Path, spec: tuple[str, int, str], label: str) -> tuple[Path, bytes]:
    path = root / spec[0]
    return path, E.require_identity(path, (spec[1], spec[2]), label)


def verify_external() -> dict[str, Any]:
    execution = load_contract()
    predecessor = verify_predecessor()
    paths = {
        "audit": ROOT / "D1020_CHECK.json",
        "candidate": ROOT / "tmp" / "d1020_equivariant_holomorphic_bundles_candidate.tex",
        "design": ROOT / "tmp" / "d1020_equivariant_holomorphic_bundles_design.json",
        "review": ROOT / "tmp" / "d1020_independent_review_r1.json",
        "cohomology_tex": ROOT / "cohomology.tex",
        "bibliography": ROOT / "my.bib",
        "cohomology_pdf": ROOT / "cohomology.pdf",
    }
    bindings = contract_bindings()
    for role, path in paths.items():
        spec = bindings[role]
        E.require_identity(path, (spec["bytes"], spec["sha256"]), f"D1020 {role}")

    audit = E.strict_json(paths["audit"])
    design = E.strict_json(paths["design"])
    review = E.strict_json(paths["review"])
    require(audit.get("schema") == "tohoku-stacks-d1020-check-v1", "D1020 audit schema drift")
    require(audit.get("formalization_id") == "D1020", "D1020 audit formalization drift")
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R64_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1020 audit state drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("status") == "AUTHORIZED_FOR_NO_OVERWRITE_R64_TRANSACTION", "D1020 authorization state drift")
    require(authorization.get("predecessor") == "tohoku_r63" and authorization.get("successor") == "tohoku_r64", "D1020 authorization lineage drift")
    require(authorization.get("decision") == AUTHORIZED_DECISION, "D1020 decision authorization drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1020 append classification drift")
    require(authorization.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "D1020 authorized counts drift")
    replacement = authorization.get("map_replacement", {})
    require(replacement.get("physical_line") == 561 and replacement.get("source_locator_preserved") == "sem/r18/nodes.csv:561", "D1020 map replacement locator drift")
    require(replacement.get("only_fields_changed") == ["decision_id", "disposition", "review_state", "stacks_labels", "official_tags", "rationale"], "D1020 authorized changed fields drift")
    require(audit.get("scanner_probe", {}).get("status") == "PASS_BYTE_IDENTICAL_REPLAY", "D1020 scanner authorization drift")
    require(audit.get("scanner_probe", {}).get("files") == scanner_contract()["files"], "D1020 scanner file pins drift")
    require(audit.get("scanner_probe", {}).get("counts") == {
        "tex_files": 119,
        "labels": 22106,
        "official_tags_joined": 21437,
        "topics": 13,
        "topic_candidates": 1286,
        "direct_topic_coverage": 13,
        "warnings": 678,
        "errors": 0,
    }, "D1020 scanner counts drift")
    require(audit.get("stacks_edit", {}).get("postimage") == {"bytes": EXPECTED_COHOMOLOGY_TEX[0], "sha256": EXPECTED_COHOMOLOGY_TEX[1]}, "D1020 source postimage drift")
    require(audit.get("pdf_build", {}).get("postimage", {}).get("bytes") == EXPECTED_COHOMOLOGY_PDF[0], "D1020 PDF byte authorization drift")
    require(audit.get("pdf_build", {}).get("postimage", {}).get("sha256") == EXPECTED_COHOMOLOGY_PDF[1], "D1020 PDF hash authorization drift")
    require(audit.get("visual_qa", {}).get("status") == "STRICT_PASS_INDEPENDENTLY_CONFIRMED" and audit.get("visual_qa", {}).get("defects") == [], "D1020 visual QA drift")

    require(design.get("schema") == "tohoku-d1020-equivariant-holomorphic-bundles-design-v1", "D1020 design schema drift")
    require(design.get("status") == "DRAFT_READY_FOR_INDEPENDENT_REVIEW" and design.get("errors") == [], "D1020 design state drift")
    require(design.get("candidate", {}).get("bytes") == EXPECTED_CANDIDATE[0] and design.get("candidate", {}).get("sha256") == EXPECTED_CANDIDATE[1], "D1020 design candidate binding drift")
    projection = design.get("conditional_mapping_projection", {})
    require(projection.get("decision_id") == "D001044" and projection.get("supersedes") == "D000614", "D1020 design mapping lineage drift")
    require(projection.get("disposition") == "existing_equivalent" and projection.get("stacks_labels") == DECISION["stacks_labels"] and projection.get("official_tags") == "", "D1020 design mapping labels drift")
    require(projection.get("issue_append") is None and projection.get("source_repair_append") is None, "D1020 design append drift")

    require(review.get("schema") == "tohoku-d1020-independent-review-v1", "D1020 review schema drift")
    require(review.get("formalization_id") == "D1020" and review.get("status") == "STRICT_PASS_FOR_LIVE_INSERTION_AND_BUILD" and review.get("errors") == [], "D1020 review state drift")
    for role, expected in (("candidate", EXPECTED_CANDIDATE), ("design", EXPECTED_DESIGN)):
        item = review.get(role, {})
        require((item.get("bytes"), item.get("sha256")) == expected, f"D1020 review {role} binding drift")
    require(all(item.get("verdict") == "PASS" for item in review.get("reviews", [])) and len(review.get("reviews", [])) == 2, "D1020 review verdict drift")
    require(review.get("predicate_summary") == {"total": 10, "passed": 10, "failed": 0}, "D1020 review predicate summary drift")

    candidate_bytes = paths["candidate"].read_bytes()
    source_bytes = paths["cohomology_tex"].read_bytes()
    anchor_tail = b"\\label{remark-equivariant-extension-classes-analytic-boundary}\n\\end{remark}\n\n"
    following = b"\n\\begin{lemma}[Coherence on a discontinuous analytic quotient]"
    require(source_bytes.count(anchor_tail + candidate_bytes + following) == 1, "D1020 candidate placement drift")
    require(source_bytes.count(candidate_bytes) == 1, "D1020 candidate insertion count drift")
    require(source_bytes.count(b"\\label{lemma-holomorphic-vector-bundles-locally-free-analytic-modules}") == 1, "D1020 nonequivariant raw-label count drift")
    require(source_bytes.count(b"\\label{lemma-equivariant-holomorphic-vector-bundles-locally-free-modules}") == 1, "D1020 equivariant raw-label count drift")
    require(source_bytes.count(b"\\label{lemma-discontinuous-analytic-invariant-direct-image-coherent}") == 1, "D1019 following raw-label count drift")
    bib_bytes = paths["bibliography"].read_bytes()
    require(bib_bytes.count(b"@ARTICLE{Grauert-direct-image,") == 1, "Grauert bibliography key drift")

    canonical: dict[str, Any] = {}
    values: dict[str, Any] = {}
    page_bytes: dict[str, bytes] = {}
    for role, spec in CANONICAL_INPUTS.items():
        path, data = read_spec(CANONICAL_ROOT, spec, role)
        canonical[role] = E.record(path, spec[0])
        if spec[0].endswith(".json"):
            values[role] = json.loads(data.decode("utf-8"))
        if role.startswith("p219_"):
            page_bytes[role.removeprefix("p219_")] = data
    require(values["source_receipt"].get("status") == "PASS", "p185 source receipt drift")
    require(values["reader_receipt"].get("status") == "PASS" and values["reader_receipt"].get("revision") == "v068c3r20", "reader receipt drift")
    require(values["qa_receipt"].get("status") == "PASS" and values["qa_receipt"].get("qa_revision") == "v68r42", "QA receipt drift")
    require(values["sem_r21_manifest"].get("schema") == "tohoku-semantic-local-successor-manifest-v21", "sem/r21 manifest drift")
    require(values["sem_r21_validation"].get("status") == "PASS", "sem/r21 validation drift")
    semantic_row = (686, "0E7D595BB3F19DB020B5EE3D524C70744C02E3EA61115D498BF2CEC9AD98C038")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 561) == semantic_row, "sem/r18 D1020 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 561) == semantic_row, "sem/r21 D1020 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/occ.csv", 985) == (541, "6E61E9247F0E2760D18E1809D8A38DDC2C89215D0B35656F003D336B91288692"), "sem/r18 D1020 occurrence drift")
    segment_expected = {
        "dip": (256, "9DA42E0BC883F6AB9D74DD4A2ECF5EE602FBB175AA50F4701D15F2F1D52FF583"),
        "fr": (256, "9DA42E0BC883F6AB9D74DD4A2ECF5EE602FBB175AA50F4701D15F2F1D52FF583"),
        "en": (231, "B72FEE68B2ACE24B4D07ECA6E4D24CB9F3043C7F61EAD909FDFFF0A9753A9C52"),
    }
    for layer, data in page_bytes.items():
        require(identity_from_bytes(layer_segment(data, DECISION["unit_id"])) == segment_expected[layer], f"D1020 {layer} segment drift")
    stacks = {role: E.record(path, bindings[role]["path"]) for role, path in paths.items()}
    return {"execution": execution, "predecessor": predecessor, "stacks": stacks, "canonical": canonical}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == E.ORACLE_PAYLOAD, f"Scanner oracle surface drift: {root}")
        require(not any(path.is_dir() for path in root.iterdir()), f"Unexpected scanner oracle subdirectory: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "r64 scanner not PASS")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r64 scanner count drift")
    require(len(check.get("warnings", [])) == 678, "r64 scanner warning count drift")
    require(check.get("tex_sha256", {}).get("cohomology.tex") == EXPECTED_COHOMOLOGY_TEX[1], "r64 scanner cohomology.tex binding drift")
    _, rows = E.load_csv(root / "stx.csv")
    expected_rows = {
        "cohomology-lemma-holomorphic-vector-bundles-locally-free-analytic-modules": ("20277", "0D6D69B427976C318544F4D967CB82A6A6E8EED3F138133AFB2B155B12F66467"),
        "cohomology-lemma-equivariant-holomorphic-vector-bundles-locally-free-modules": ("20343", "B32D66309690486FC9B82F267349A762086309A106EF486F83039515D6B029E0"),
        "cohomology-lemma-discontinuous-analytic-invariant-direct-image-coherent": ("20395", "AC355C08869E0130D3D39C0C93260B80ECE1D696540E554393352C568CB9C028"),
    }
    for label, (line, text_hash) in expected_rows.items():
        row = E.one_row(rows, "full_label", label, f"r64 scanner {label}")
        require(row["file"] == "cohomology.tex" and row["line"] == line and row["tag"] == "", f"r64 scanner row drift: {label}")
        require(row["text_sha256"] == text_hash, f"r64 scanner text drift: {label}")
    return check


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink(), "D1020 scanner oracle is missing or unsafe")
    require(E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "D1020 scanner replay is missing or unsafe")
    verify_scan(E.ORACLE, oracle_surface=True)
    verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"Scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1020_scan_probe_r1/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1020_scan_probe_replay_r1/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing or unsafe r64 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r64-check.json"} if receipt_mode else set()), "r64 output surface drift")
    require(not any(path.is_dir() for path in root.iterdir()), "Unexpected r64 output subdirectory")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r64 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"Inherited r64 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r64 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r64 map replacement drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r64 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R63_FILES["ucand.csv"], "r64/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r64 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r64 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 678, "r64 warning propagation drift")

    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1045)], "r64 decision sequence drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r64 issue sequence drift")
    require(decisions[-1] == DECISION, "r64 final decision row drift")
    selected = E.one_row(mapping, "unit_id", DECISION["unit_id"], "r64 map")
    require(selected["decision_id"] == "D001044" and selected["disposition"] == "existing_equivalent", "r64 target decision/disposition drift")
    require(selected["review_state"] == DECISION["review_state"], "r64 review state drift")
    require(selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "", "r64 labels/tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:561", "r64 source locator drift")
    require(E.line_identity(root / "map.csv", 561) == EXPECTED_SUCCESSOR_MAP_ROW, "r64 target map row identity drift")
    deltas = E.map_row_delta()
    require(len(deltas) == 6 and {row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r64 map delta cardinality/scope drift")
    require({row["field"] for row in deltas} == {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"}, "r64 map changed-field set drift")
    gap_dispositions = {"existing_weaker", "extend_existing", "new_section", "new_statement"}
    remaining = sum(1 for row in mapping if row["disposition"] in gap_dispositions)
    require(remaining == 22, "r64 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1044,
        "decisions_appended": ["D001044"],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 678, "errors": 0},
        "remaining_gap_class_dispositions": 22,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 6, "unchanged_units": 990},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1020_LIVE_SOURCE_AND_PDF_PREREQUISITES_ALREADY_ADMITTED_NO_BIB_CHANGE",
        "scanner_payload_change": "D1020_LIVE_SOURCE_REBIND_WITH_INHERITED_CFG",
    }
    if receipt_mode:
        receipt = E.strict_json(root / "r64-check.json")
        require(receipt == receipt_payload(root, result), "r64 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    stacks = external["stacks"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r64-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": stacks["audit"],
            "candidate": stacks["candidate"],
            "design": stacks["design"],
            "independent_review": stacks["review"],
            "bibliography": stacks["bibliography"],
            "live_source": stacks["cohomology_tex"],
            "live_pdf": stacks["cohomology_pdf"],
            "change_class": "admitted_live_source_and_pdf_no_bibliography_change_plus_mapping_successor",
        },
        "source_chain": {
            "source_admission": external["canonical"]["source_receipt"],
            "reader_receipt": external["canonical"]["reader_receipt"],
            "qa_receipt": external["canonical"]["qa_receipt"],
            "sem_r18_nodes": external["canonical"]["sem_r18_nodes"],
            "sem_r21_manifest": external["canonical"]["sem_r21_manifest"],
            "sem_r21_validation": external["canonical"]["sem_r21_validation"],
            "sem_r21_nodes": external["canonical"]["sem_r21_nodes"],
        },
        "scanner_oracle": oracles["oracle"],
        "scanner_replay": oracles["replay"],
        "external_constraints": {
            "github": {
                "status": "available_by_direct_user_update",
                "reason": "GitHub availability was restored by direct user update.",
                "action": "This bounded local transaction requires no Git or GitHub operation.",
            }
        },
        "deltas": dict(deltas),
        "files": E.output_records(root),
        "nonclaims": [
            "D001044 closes only the p.219 equivariant holomorphic-bundle equivalence.",
            "The adjacent nonequivariant D000615 unit, extension classification, H^1, quotient descent, compactness, and finite dimensionality remain separate.",
            "No issue, source repair, semantic successor, GAGA comparison, release, publication, DOI, remote-freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r63"
    E.TARGET = ROOT / "tohoku_r64"
    E.STAGE = ROOT / ".tohoku-r64-txn"
    E.ORACLE = ROOT / "tmp" / "d1020_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1020_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R63_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R63_FILES
    E.EXPECTED_SCAN = EXPECTED_SCAN
    E.EXPECTED_SCAN_COUNTS = EXPECTED_SCAN_COUNTS
    E.EXPECTED_PROJECTED = EXPECTED_PROJECTED
    E.EXPECTED_APPEND_ROWS = {"decision": EXPECTED_DECISION_APPEND}
    E.EXPECTED_PREDECESSOR_MAP_ROW = EXPECTED_PREDECESSOR_MAP_ROW
    E.EXPECTED_SUCCESSOR_MAP_ROW = EXPECTED_SUCCESSOR_MAP_ROW
    E.DECISION = DECISION
    E.EXPECTED_COUNTS = EXPECTED_COUNTS
    E.STATUS_BYTES = STATUS_BYTES
    E.STACKS_INPUTS = {"cohomology_tex": ("cohomology.tex", EXPECTED_COHOMOLOGY_TEX[0], EXPECTED_COHOMOLOGY_TEX[1])}
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r64 target or stage already exists")
    oracles = verify_oracles()
    print(
        json.dumps(
            {
                "schema": "tohoku-r64-scanner-oracle-v1",
                "status": "PASS_REPLAY",
                "errors": [],
                "scanner_oracles": oracles,
                "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 678, "errors": 0},
            },
            indent=2,
            sort_keys=True,
        )
    )


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r64 target or stage already exists")
    external = verify_external()
    oracles = verify_oracles()
    projection = {
        "cfg.json": identity_from_bytes(expected_cfg_bytes()),
        "dec.csv": identity_from_bytes(expected_decision_bytes()),
        "issues.csv": identity_from_bytes(expected_issue_bytes()),
        "map.csv": identity_from_bytes(expected_map_bytes()),
        "STATUS.md": identity_from_bytes(STATUS_BYTES),
    }
    print(
        json.dumps(
            {
                "schema": "tohoku-r64-static-input-audit-v1",
                "status": "PASS",
                "errors": [],
                "external": external,
                "scanner_oracles": oracles,
                "projection": projection,
                "decision": "D001044",
                "issue": None,
                "source_repair": None,
                "remaining_gaps": 22,
            },
            indent=2,
            sort_keys=True,
        )
    )


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r64 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    receipt = receipt_payload(E.STAGE, deltas)
    E.exclusive_write(E.STAGE / "r64-check.json", E.json_bytes(receipt))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r64 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("Post-promotion r64 replay failed; target rolled back") from exc
    print(
        json.dumps(
            {
                "schema": "tohoku-r64-transaction-result-v1",
                "status": "PASS_COMMITTED",
                "errors": [],
                "target": "tohoku_r64",
                "receipt": E.record(E.TARGET / "r64-check.json"),
                "remaining_gaps": 22,
            },
            indent=2,
            sort_keys=True,
        )
    )


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink(), "r64 target missing or unsafe")
    require(not E.STAGE.exists(), "r64 stage unexpectedly exists")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(
        json.dumps(
            {
                "schema": "tohoku-r64-replay-v1",
                "status": "PASS_REPLAY",
                "errors": [],
                "receipt": E.record(E.TARGET / "r64-check.json"),
                "deltas": result,
            },
            indent=2,
            sort_keys=True,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("oracle", "preflight", "execute", "replay"))
    args = parser.parse_args()
    try:
        if args.mode == "oracle":
            verify_scanner_oracles()
        elif args.mode == "preflight":
            preflight()
        elif args.mode == "execute":
            execute()
        else:
            replay()
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
