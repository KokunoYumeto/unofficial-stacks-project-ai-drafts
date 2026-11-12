#!/usr/bin/env python3
"""Specialize the sealed r64 transaction surface for D1021/r65."""

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
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r64.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r65_contract.json"
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

ENGINE_IDENTITY = (41390, "F1FAAABFB4C633ED87F6E1AC04E409E8B8C16F772DB2EE5A3E68FFBF2DFFA513")
CONTRACT_ID = "D1021-r65-D001045-v1"
EXPECTED_R64_RECEIPT = (10148, "2133F7D0C6CC875A196394308233C5DF1FC120AB764C8AB45D2999AE7FCC7E93")
EXPECTED_R64_FILES = {
    "STATUS.md": (1159, "2B7448B8A01B2B806EBF5E3063A1ED75B0AE9BEB7404520CB11E343F3303C481"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83022, "CA4BD4D6C25E995CF422795472D17E039CBD260F1D17B16915DF5245B4CB272E"),
    "dec.csv": (386884, "744676FA92F8508F4A14B3271F1B22016AA751B6606A4C560BCEB035531D4115"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (485864, "28B10AF238AFB630F03D5F23460EED96C95A68BC3FE33736598FA6678C403A52"),
    "mcheck.json": (72849, "862214979642885CB9EA48BD3AF598D233B2DBD56A1AE6BC448EB791E9B60ABA"),
    "stx.csv": (5288663, "01C9089B9AF31597C7FD787C37D31C7FCB5A052DED324EDB3648FEEAC083DAEC"),
    "tcand.csv": (489256, "73C6BFD919058171C14E2CDEC94F47DDBFF389636BDA7250BE4B6BBE7BC29357"),
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
    "dec.csv": (387550, "FA8E7CB9875CD48EE12CD1F71BBF02A3E49CEC59AC84B0C2D632F0AD57C82988"),
    "issues.csv": EXPECTED_R64_FILES["issues.csv"],
    "map.csv": (486207, "3EE354983BE9A38A36E921E26E3966B9022DE3F29516AAC968A0AD0F16090936"),
}
EXPECTED_DECISION_APPEND = (666, "0C67FBD9F0A63BCC636BB314D493CB5007F5BC03F3D7BE86A1C6AC4FC7E18D39")
EXPECTED_PREDECESSOR_MAP_ROW = (441, "69B76A64CA7578CCF175FF4CDB5FD0C48BBF246A76FC03770CAC457D33F73C88")
EXPECTED_SUCCESSOR_MAP_ROW = (784, "48C63DE57645BEB7B3DFFAE93568CECC5CE853CA692623B956EA039C73199D96")
EXPECTED_AUDIT = (7654, "234CC49BE26F082727A66CC7859668351BD7D7BEBC7DB6867242E44CB59EE940")
EXPECTED_MAPPING_REVIEW = (4585, "BAC136EED314E3E1A07CD7A1154D33E79B413A83A746E3A1460AF2D14ECFA8B6")
EXPECTED_ORIGINATING_AUDIT = (14789, "E03C0BDB19BB564CEC782124367D6CD053624551F847F64885E6ECC1A7E4B083")
EXPECTED_COHOMOLOGY_TEX = (927351, "934223B83092E38F7184DE6B739569002BFCBE9F934A5AA9212EBF78AD8424CA")
EXPECTED_BIBLIOGRAPHY = (220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE")
EXPECTED_COHOMOLOGY_PDF = (2020550, "4B55BF958522964140AD364EF911F71DEA72455DA709E80176AC707381786C2E")

DECISION = {
    "decision_id": "D001045",
    "unit_id": "tohoku:equivalence:holomorphic-bundles-locally-free-sheaves",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-holomorphic-vector-bundles-locally-free-analytic-modules",
    "rationale": "Stacks now proves the natural equivalence between rank-n holomorphic vector bundles and analytic O_X-modules locally isomorphic to O_X^n, proves that these modules are coherent, and identifies the inverse bundle fibre as L_x tensor_{O_{X,x}} C through the residue or evaluation map. Equivariance, extension classification and H^1, quotient descent, compactness, finite dimensionality, and GAGA are separate units and are not mapped here.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000615",
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
    "decisions": 1045,
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
        "existing_equivalent": 388,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 3,
        "structural_only": 424,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1045,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 388,
    "new_statement": 3,
    "remaining_gap_class_dispositions": 21,
    "source_repairs_appended": 0,
    "mapping_closures": 1,
    "changed_map_rows": 1,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r64 dossier is preserved exactly; D001045 closes the p.219 nonequivariant holomorphic-bundle equivalence in a no-overwrite r65 successor.\n"
    "- The already sealed D1020 lemma proves the exact bundle/module equivalence, coherence, and residue-field fibre formula; the equivariant unit remains separately mapped by D001044.\n"
    "- The D1021 audit, mapping review, originating D1020 audit, bibliography, cohomology source, and cohomology PDF are bound byte-exactly.\n"
    "- No live source, PDF, bibliography, scanner, issue, or source-repair change is made; the inherited cfg and scanner payload are preserved exactly.\n"
    "- The scanner indexes 119 top-level TeX files with 22,106 labels, 678 warnings, and no errors.\n"
    "- There are 1,045 decisions, 679 decided units, 32 resolved source issues, and 21 gap-class dispositions remain.\n"
    "- GitHub availability was restored by direct user update; this bounded local transaction requires no Git or GitHub operation.\n"
    "- No claim is made for equivariant extension classification, H^1, quotient descent, compactness, finite dimensionality, GAGA, release, publication, DOI, remote-freshness, rights, or whole-paper completion.\n"
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
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r64 transaction engine identity drift")
    module = types.ModuleType("tohoku_r65_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r64 transaction engine changed during load")
    return module


M = load_engine()
E = M.E


def contract_bindings() -> dict[str, Any]:
    return {
        "audit": {"path": "D1021_CHECK.json", "bytes": EXPECTED_AUDIT[0], "sha256": EXPECTED_AUDIT[1]},
        "mapping_review": {"path": "tmp/d1021_mapping_review.json", "bytes": EXPECTED_MAPPING_REVIEW[0], "sha256": EXPECTED_MAPPING_REVIEW[1]},
        "originating_audit": {"path": "D1020_CHECK.json", "bytes": EXPECTED_ORIGINATING_AUDIT[0], "sha256": EXPECTED_ORIGINATING_AUDIT[1]},
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
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r65 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r65-transaction-contract-v1", "r65 contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "r65 contract ID mismatch")
    spec = contract.get("script")
    require(isinstance(spec, dict) and spec.get("path") == "srcmap/build_tohoku_r65.py", "r65 script pin missing")
    require(identity_from_bytes(SCRIPT_PATH.read_bytes()) == (spec.get("bytes"), spec.get("sha256")), "r65 script identity mismatch")
    engine = contract.get("engine")
    require(isinstance(engine, dict) and engine.get("path") == "srcmap/build_tohoku_r64.py", "r65 engine path mismatch")
    require((engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r65 engine contract mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r64/r64-check.json", "bytes": EXPECTED_R64_RECEIPT[0], "sha256": EXPECTED_R64_RECEIPT[1]}, "r65 predecessor contract mismatch")
    require(contract.get("frozen_prerequisite") == contract_bindings()["audit"], "r65 audit contract mismatch")
    require(contract.get("bound_inputs") == contract_bindings(), "r65 bound-input contract mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r65 scanner contract mismatch")
    require(contract.get("decision") == AUTHORIZED_DECISION, "r65 decision contract mismatch")
    require(contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r65 projected-count contract mismatch")
    require(contract.get("target") == "tohoku_r65", "r65 target contract mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r64" and transaction.get("stage") == ".tohoku-r65-txn", "r65 transaction paths mismatch")
    require(transaction.get("no_overwrite") is True and transaction.get("atomic_directory_rename") is True and transaction.get("post_promotion_replay") is True, "r65 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r65.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r65_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r64.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    cfg = json.loads(data.decode("utf-8"))
    require(cfg.get("dossier_id") == "tohoku_r62", "inherited cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "Inherited r65 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1044, "r64 decision schema/count drift")
    require(rows[-1]["decision_id"] == "D001044", "r64 decision tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, [DECISION], header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001045 append-row drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "Projected r65 decisions drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "Inherited r65 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r64 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r64 map schema/count drift")
    selected = E.one_row(rows, "unit_id", DECISION["unit_id"], "r64 map")
    require(selected["decision_id"] == "D000615" and selected["disposition"] == "new_statement", "r64 D1021 target state drift")
    require(selected["review_state"] == "reviewed_new_statement", "r64 D1021 review-state drift")
    require(selected["stacks_labels"] == "" and selected["stacks_tags"] == "", "r64 D1021 predecessor labels/tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:562", "r64 D1021 source locator drift")
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
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "Projected r65 map drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r64-check.json"
    E.require_identity(receipt, EXPECTED_R64_RECEIPT, "r64 receipt")
    for name, expected in EXPECTED_R64_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r64/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r64-v1", "r64 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r64 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 22, "r64 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R64_FILES), "r64 receipt inventory drift")
    replay = {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records}
    require(replay == EXPECTED_R64_FILES, "r64 receipt file identities drift")
    require(E.line_identity(E.SOURCE / "map.csv", 562) == EXPECTED_PREDECESSOR_MAP_ROW, "r64 target map row drift")
    return {"receipt": E.record(receipt, "tohoku_r64/r64-check.json")}


def read_spec(root: Path, spec: tuple[str, int, str], label: str) -> tuple[Path, bytes]:
    path = root / spec[0]
    return path, E.require_identity(path, (spec[1], spec[2]), label)


def verify_external() -> dict[str, Any]:
    execution = load_contract()
    predecessor = verify_predecessor()
    paths = {
        "audit": ROOT / "D1021_CHECK.json",
        "mapping_review": ROOT / "tmp" / "d1021_mapping_review.json",
        "originating_audit": ROOT / "D1020_CHECK.json",
        "cohomology_tex": ROOT / "cohomology.tex",
        "bibliography": ROOT / "my.bib",
        "cohomology_pdf": ROOT / "cohomology.pdf",
    }
    bindings = contract_bindings()
    for role, path in paths.items():
        spec = bindings[role]
        E.require_identity(path, (spec["bytes"], spec["sha256"]), f"D1021 {role}")

    audit = E.strict_json(paths["audit"])
    review = E.strict_json(paths["mapping_review"])
    originating = E.strict_json(paths["originating_audit"])
    require(audit.get("schema") == "tohoku-stacks-d1021-check-v1", "D1021 audit schema drift")
    require(audit.get("formalization_id") == "D1021", "D1021 audit formalization drift")
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R65_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1021 audit state drift")
    require(audit.get("change_class") == "mapping_only_from_already_sealed_d1020_formalization", "D1021 change class drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("status") == "AUTHORIZED_FOR_NO_OVERWRITE_R65_TRANSACTION", "D1021 authorization state drift")
    require(authorization.get("predecessor") == "tohoku_r64" and authorization.get("successor") == "tohoku_r65", "D1021 authorization lineage drift")
    require(authorization.get("decision") == AUTHORIZED_DECISION, "D1021 decision authorization drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1021 append classification drift")
    require(authorization.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "D1021 authorized counts drift")
    replacement = authorization.get("map_replacement", {})
    require(replacement.get("physical_line") == 562 and replacement.get("source_locator_preserved") == "sem/r18/nodes.csv:562", "D1021 map replacement locator drift")
    require(replacement.get("only_fields_changed") == ["decision_id", "disposition", "review_state", "stacks_labels", "official_tags", "rationale"], "D1021 authorized changed fields drift")
    sealed = audit.get("sealed_predecessor", {})
    require(sealed.get("status") == "PASS" and sealed.get("path") == "tohoku_r64", "D1021 sealed predecessor state drift")
    require(sealed.get("receipt") == {"path": "tohoku_r64/r64-check.json", "bytes": EXPECTED_R64_RECEIPT[0], "sha256": EXPECTED_R64_RECEIPT[1]}, "D1021 sealed receipt drift")
    require(sealed.get("post_promotion_replays") == 2 and sealed.get("post_promotion_replay_status") == "PASS_REPLAY" and sealed.get("stage_absent") is True, "D1021 predecessor replay gate drift")
    evidence = audit.get("formalization_evidence", {})
    require(evidence.get("target_label") == DECISION["stacks_labels"] and evidence.get("official_tag") == "", "D1021 formalization label drift")
    require((evidence.get("live_tex", {}).get("bytes"), evidence.get("live_tex", {}).get("sha256")) == EXPECTED_COHOMOLOGY_TEX, "D1021 live TeX evidence drift")
    require((evidence.get("live_pdf", {}).get("bytes"), evidence.get("live_pdf", {}).get("sha256")) == EXPECTED_COHOMOLOGY_PDF, "D1021 live PDF evidence drift")
    require(evidence.get("originating_d1020_audit", {}).get("bytes") == EXPECTED_ORIGINATING_AUDIT[0] and evidence.get("originating_d1020_audit", {}).get("sha256") == EXPECTED_ORIGINATING_AUDIT[1], "D1021 originating audit evidence drift")
    for gate in ("new_source_edit_required", "new_pdf_build_required", "new_visual_render_required", "new_scanner_run_required"):
        require(evidence.get(gate) is False, f"D1021 unexpected production gate: {gate}")

    require(review.get("schema") == "tohoku-d1021-mapping-review-v1", "D1021 mapping review schema drift")
    require(review.get("formalization_id") == "D1021" and review.get("status") == "STRICT_PASS_CONDITIONAL_ON_BYTE_IDENTICAL_R64_PREIMAGE" and review.get("errors") == [], "D1021 mapping review state drift")
    require(review.get("source_review", {}).get("verdict") == "PASS" and review.get("mathematical_review", {}).get("verdict") == "PASS", "D1021 mapping review verdict drift")
    require(review.get("mathematical_review", {}).get("target_label") == DECISION["stacks_labels"], "D1021 review label drift")
    conditional = review.get("conditional_mapping", {})
    require(conditional.get("decision_id") == "D001045" and conditional.get("supersedes") == "D000615", "D1021 review mapping lineage drift")
    require(conditional.get("disposition") == "existing_equivalent" and conditional.get("stacks_labels") == DECISION["stacks_labels"] and conditional.get("official_tags") == "", "D1021 review mapping labels drift")
    require(conditional.get("issue_append") is None and conditional.get("source_repair_append") is None, "D1021 review append drift")
    require(originating.get("schema") == "tohoku-stacks-d1020-check-v1" and originating.get("status") == "STRICT_PASS_PREREQUISITES_R64_MAPPING_AUTHORIZED" and originating.get("errors") == [], "D1020 originating audit drift")

    source_bytes = paths["cohomology_tex"].read_bytes()
    require(source_bytes.count(b"\\label{lemma-holomorphic-vector-bundles-locally-free-analytic-modules}") == 1, "D1021 target raw-label count drift")
    lemma_block = b"".join(source_bytes.splitlines(keepends=True)[20275:20341])
    require(identity_from_bytes(lemma_block) == (2807, "8640B3C62049EFC5B4BC868DFEFCF3160152475467C02C089C436F7BEC82C14D"), "D1021 lemma block drift")
    require(E.line_identity(E.SOURCE / "stx.csv", 3629) == (315, "386B6923A5C3B9A4801AEF64A1F5CA9512A131A2A1A839121D794C321FD91A44"), "D1021 sealed scanner label row drift")
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
    semantic_row = (900, "2A09FF0387AB16F0E32F39A03C8854446228E63BE9D2D65F17E4D61576094CE6")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 562) == semantic_row, "sem/r18 D1021 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 562) == semantic_row, "sem/r21 D1021 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/occ.csv", 984) == (559, "4F5DB366A98DF2B434B5A5A9DF27D67FB5295F707E19E16E6F09805099BCE712"), "sem/r18 D1021 occurrence drift")
    segment_expected = {
        "dip": (517, "3F09D73C2B8428B8C3146448BAE88712932792975A24B135BC96A8A0E1120610"),
        "fr": (518, "3613A370EF22582612BFBD33365D66C00ABBD06F3020D39AA609742C65BB36D9"),
        "en": (482, "B5CA96ACFE5D5A2B367D784BEABDD185A7B542DC2C328BE7768EF61D1D7DBBE0"),
    }
    for layer, data in page_bytes.items():
        require(identity_from_bytes(layer_segment(data, DECISION["unit_id"])) == segment_expected[layer], f"D1021 {layer} segment drift")
    stacks = {role: E.record(path, bindings[role]["path"]) for role, path in paths.items()}
    return {"execution": execution, "predecessor": predecessor, "stacks": stacks, "canonical": canonical}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == E.ORACLE_PAYLOAD, f"Scanner oracle surface drift: {root}")
        require(not any(path.is_dir() for path in root.iterdir()), f"Unexpected scanner oracle subdirectory: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "r65 scanner not PASS")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r65 scanner count drift")
    require(len(check.get("warnings", [])) == 678, "r65 scanner warning count drift")
    require(check.get("tex_sha256", {}).get("cohomology.tex") == EXPECTED_COHOMOLOGY_TEX[1], "r65 scanner cohomology.tex binding drift")
    _, rows = E.load_csv(root / "stx.csv")
    expected_rows = {
        "cohomology-lemma-holomorphic-vector-bundles-locally-free-analytic-modules": ("20277", "0D6D69B427976C318544F4D967CB82A6A6E8EED3F138133AFB2B155B12F66467"),
        "cohomology-lemma-equivariant-holomorphic-vector-bundles-locally-free-modules": ("20343", "B32D66309690486FC9B82F267349A762086309A106EF486F83039515D6B029E0"),
        "cohomology-lemma-discontinuous-analytic-invariant-direct-image-coherent": ("20395", "AC355C08869E0130D3D39C0C93260B80ECE1D696540E554393352C568CB9C028"),
    }
    for label, (line, text_hash) in expected_rows.items():
        row = E.one_row(rows, "full_label", label, f"r65 scanner {label}")
        require(row["file"] == "cohomology.tex" and row["line"] == line and row["tag"] == "", f"r65 scanner row drift: {label}")
        require(row["text_sha256"] == text_hash, f"r65 scanner text drift: {label}")
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
    require(root.is_dir() and not root.is_symlink(), f"Missing or unsafe r65 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r65-check.json"} if receipt_mode else set()), "r65 output surface drift")
    require(not any(path.is_dir() for path in root.iterdir()), "Unexpected r65 output subdirectory")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r65 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"Inherited r65 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r65 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r65 map replacement drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r65 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R64_FILES["ucand.csv"], "r65/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r65 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r65 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 678, "r65 warning propagation drift")

    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1046)], "r65 decision sequence drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r65 issue sequence drift")
    require(decisions[-1] == DECISION, "r65 final decision row drift")
    selected = E.one_row(mapping, "unit_id", DECISION["unit_id"], "r65 map")
    require(selected["decision_id"] == "D001045" and selected["disposition"] == "existing_equivalent", "r65 target decision/disposition drift")
    require(selected["review_state"] == DECISION["review_state"], "r65 review state drift")
    require(selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "", "r65 labels/tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:562", "r65 source locator drift")
    require(E.line_identity(root / "map.csv", 562) == EXPECTED_SUCCESSOR_MAP_ROW, "r65 target map row identity drift")
    deltas = E.map_row_delta()
    require(len(deltas) == 5 and {row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r65 map delta cardinality/scope drift")
    require({row["field"] for row in deltas} == {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"}, "r65 map changed-field set drift")
    gap_dispositions = {"existing_weaker", "extend_existing", "new_section", "new_statement"}
    remaining = sum(1 for row in mapping if row["disposition"] in gap_dispositions)
    require(remaining == 21, "r65 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1045,
        "decisions_appended": ["D001045"],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 678, "errors": 0},
        "remaining_gap_class_dispositions": 21,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 5, "unchanged_units": 990},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1021_MAPPING_ONLY_NO_LIVE_SOURCE_PDF_OR_BIBLIOGRAPHY_CHANGE",
        "scanner_payload_change": "R65_INHERITED_BYTE_IDENTICAL_SCANNER_PAYLOAD",
    }
    if receipt_mode:
        receipt = E.strict_json(root / "r65-check.json")
        require(receipt == receipt_payload(root, result), "r65 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    stacks = external["stacks"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r65-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": stacks["audit"],
            "mapping_review": stacks["mapping_review"],
            "originating_d1020_audit": stacks["originating_audit"],
            "bibliography": stacks["bibliography"],
            "live_source": stacks["cohomology_tex"],
            "live_pdf": stacks["cohomology_pdf"],
            "change_class": "mapping_only_from_already_sealed_d1020_formalization",
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
            "D001045 closes only the p.219 nonequivariant holomorphic-bundle equivalence.",
            "The equivariant unit remains separately mapped by D001044; extension classification, H^1, quotient descent, compactness, and finite dimensionality remain separate.",
            "No issue, source repair, semantic successor, GAGA comparison, release, publication, DOI, remote-freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r64"
    E.TARGET = ROOT / "tohoku_r65"
    E.STAGE = ROOT / ".tohoku-r65-txn"
    E.ORACLE = ROOT / "tmp" / "d1020_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1020_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R64_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R64_FILES
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r65 target or stage already exists")
    oracles = verify_oracles()
    print(
        json.dumps(
            {
                "schema": "tohoku-r65-scanner-oracle-v1",
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r65 target or stage already exists")
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
                "schema": "tohoku-r65-static-input-audit-v1",
                "status": "PASS",
                "errors": [],
                "external": external,
                "scanner_oracles": oracles,
                "projection": projection,
                "decision": "D001045",
                "issue": None,
                "source_repair": None,
                "remaining_gaps": 21,
            },
            indent=2,
            sort_keys=True,
        )
    )


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r65 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    receipt = receipt_payload(E.STAGE, deltas)
    E.exclusive_write(E.STAGE / "r65-check.json", E.json_bytes(receipt))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r65 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("Post-promotion r65 replay failed; target rolled back") from exc
    print(
        json.dumps(
            {
                "schema": "tohoku-r65-transaction-result-v1",
                "status": "PASS_COMMITTED",
                "errors": [],
                "target": "tohoku_r65",
                "receipt": E.record(E.TARGET / "r65-check.json"),
                "remaining_gaps": 21,
            },
            indent=2,
            sort_keys=True,
        )
    )


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink(), "r65 target missing or unsafe")
    require(not E.STAGE.exists(), "r65 stage unexpectedly exists")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(
        json.dumps(
            {
                "schema": "tohoku-r65-replay-v1",
                "status": "PASS_REPLAY",
                "errors": [],
                "receipt": E.record(E.TARGET / "r65-check.json"),
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
