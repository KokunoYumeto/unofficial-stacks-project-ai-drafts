#!/usr/bin/env python3
"""Specialize the sealed r62 transaction surface for D1019/r63."""

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
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r62.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r63_contract.json"
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

ENGINE_IDENTITY = (31929, "4283B6FBFE10BF5189C9B6B654467448E0A2F044FA60BCF27F6737C6E96C8D79")
CONTRACT_ID = "D1019-r63-D001043-v1"
EXPECTED_R62_RECEIPT = (9694, "1477CC18698FEEE1CA390319C1771447FA36C38261429F0644FE11978A2EFC73")
EXPECTED_R62_FILES = {
    "STATUS.md": (1236, "4C28D341881E1E129086CCA853E8A7385F7C5C7CD219FD61306B13DF8A3A4211"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (82634, "DBDF93ADC67E74D8FBEB74C5147E714A24BB04E7B39EC32846C3210DC297EDD0"),
    "dec.csv": (385413, "9FF41BD33E9AC15FC6512BC4FD4B7E8C1F1804F4C3FDA8111AF55C1D8610DE9C"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (485159, "37CD0C823E7F3F6F3286D727EF6A312E5DC00EF7CA108A004FC46C617B7B6DA5"),
    "mcheck.json": (72461, "CC03CE9F8F80C94A203F4BF8B7746FDD99A13B1F983104F0C19ACCD7D11525F8"),
    "stx.csv": (5287716, "8AF5DD35D91AF45EC6DACE5F3DDC03213992D9EB6316353DC0FEABC7A9B23427"),
    "tcand.csv": (489256, "B7481F3F3FB7F5DDF59F6646B3DB440452751D760C21519D53619EB7510C4B13"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (82761, "57643A9EE276EC4ABE1ECD8955E4FAC84FFB52504CBA0C5D60992986811F0726"),
    "stx.csv": (5288027, "681364D9AFF58762102B89B5DFA018A3D38F8012C59DFA33544DBF7DC94B7542"),
    "tcand.csv": (489256, "00D7DA1CBFFE74EC58F7149CB9EB335FF6CE1DBA05BED1EEFCED9921D5047101"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22104,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1286,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_PROJECTED = {
    "dec.csv": (386189, "2ECE3DF81EB51B54E2BE11A9B60B7DB10A216F40CAA978C7AAF76D18E7E6EED6"),
    "issues.csv": EXPECTED_R62_FILES["issues.csv"],
    "map.csv": (485515, "ED83B6A2879F06162978CD69B15BA9EAA7367F875B87CB46ABA63167DAAF76FA"),
}
EXPECTED_DECISION_APPEND = (776, "C4512F17CA786E94941516C7B39703C849703ED74CD0FE9ECFDB94F744543A9C")
EXPECTED_PREDECESSOR_MAP_ROW = (534, "6961D6333DAC830C1D896CC675126CD591223A47B36BF131668B0C99D4F9E658")
EXPECTED_SUCCESSOR_MAP_ROW = (890, "F57D131A1B054C9DC809F543B3791A31D17031406B16773B7A8FE27AF2337CAE")
EXPECTED_AUDIT = (12205, "1E22CCF026626318F4CC97CC1E186F6A3633055B5F82A085AA52D5E37F888E07")
EXPECTED_CANDIDATE = (3303, "497B3D12B59EB8DF3D77B0FF6BA4161A20B1D450E735C63CD47A381A700C943A")
EXPECTED_DESIGN = (8307, "86599B850BCE94517AB47464B22EC9364D9F6D4C2B20978DBFAA1CCC4221FB3B")
EXPECTED_REVIEW = (2648, "EFF3B1F16662DABCD9F5F65F7E40BC3644BDB80872351C64C44099EC0ACE662F")
EXPECTED_COHOMOLOGY_TEX = (922413, "AEC4A47B15E55D4BB99267EE03E961FB1288E69F8911A13310C59DA81354653F")
EXPECTED_BIBLIOGRAPHY = (220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE")
EXPECTED_COHOMOLOGY_PDF = (2013727, "167DFFEA7D1B9009B0672714150BE613A9F1C1E5FF5207EBB6C68EF0E67B3EC6")

DECISION = {
    "decision_id": "D001043",
    "unit_id": "tohoku:descent:discontinuous-action-characteristic-zero",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-orbit-space-equivariant-cohomology-stabilizer-orders;cohomology-lemma-discontinuous-analytic-invariant-direct-image-coherent",
    "rationale": "Stacks now proves the characteristic-zero quotient-cohomology comparison for a discontinuous action by the stabilizer-order criterion, and the analytic quotient lemma proves that invariant direct image preserves coherence for coherent analytic modules. Together these give H^1(X;G,L)=H^1(Y,L^G) and coherence of L^G, including O(E^vee tensor F)^G, exactly as in the source. No categorical descent for nontrivial stabilizers, GAGA, compactness, or finite-dimensionality claim is made.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000613",
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
    "decisions": 1043,
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
        "existing_equivalent": 386,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 5,
        "structural_only": 424,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1043,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 386,
    "new_statement": 5,
    "remaining_gap_class_dispositions": 23,
    "source_repairs_appended": 0,
    "mapping_closures": 1,
    "changed_map_rows": 1,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r62 dossier is preserved exactly; D001043 closes the p.219 discontinuous-action characteristic-zero unit in a no-overwrite r63 successor.\n"
    "- The existing stabilizer-order comparison supplies quotient cohomology, and the new analytic quotient lemma supplies coherence of invariant direct image, including the bundle-sheaf instance.\n"
    "- The D1019 audit, candidate, design, independent review, bibliography, cohomology source, and cohomology PDF are bound byte-exactly.\n"
    "- No issue or source-repair row is appended; the inherited cfg namespace is retained and the scanner is rebound to the exact live source bytes.\n"
    "- The scanner indexes 119 top-level TeX files with 22,104 labels, 676 warnings, and no errors.\n"
    "- There are 1,043 decisions, 679 decided units, 32 resolved source issues, and 23 gap-class dispositions remain.\n"
    "- GitHub availability was restored by direct user update; this bounded local transaction requires no Git or GitHub operation.\n"
    "- No categorical descent for nontrivial stabilizers, GAGA comparison, compactness, finite-dimensionality, release, publication, DOI, remote-freshness, rights, or whole-paper completion is claimed.\n"
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
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r62 transaction engine identity drift")
    module = types.ModuleType("tohoku_r63_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r62 transaction engine changed during load")
    return module


M = load_engine()
E = M.E


def contract_bindings() -> dict[str, Any]:
    return {
        "audit": {"path": "D1019_CHECK.json", "bytes": EXPECTED_AUDIT[0], "sha256": EXPECTED_AUDIT[1]},
        "candidate": {"path": "tmp/d1019_analytic_descent_candidate.tex", "bytes": EXPECTED_CANDIDATE[0], "sha256": EXPECTED_CANDIDATE[1]},
        "design": {"path": "tmp/d1019_analytic_descent_design.json", "bytes": EXPECTED_DESIGN[0], "sha256": EXPECTED_DESIGN[1]},
        "review": {"path": "tmp/d1019_independent_review_r2.json", "bytes": EXPECTED_REVIEW[0], "sha256": EXPECTED_REVIEW[1]},
        "cohomology_tex": {"path": "cohomology.tex", "bytes": EXPECTED_COHOMOLOGY_TEX[0], "sha256": EXPECTED_COHOMOLOGY_TEX[1]},
        "bibliography": {"path": "my.bib", "bytes": EXPECTED_BIBLIOGRAPHY[0], "sha256": EXPECTED_BIBLIOGRAPHY[1]},
        "cohomology_pdf": {"path": "cohomology.pdf", "bytes": EXPECTED_COHOMOLOGY_PDF[0], "sha256": EXPECTED_COHOMOLOGY_PDF[1]},
    }


def scanner_contract() -> dict[str, Any]:
    return {
        "oracle_path": "tmp/d1019_scan_probe_r1",
        "replay_path": "tmp/d1019_scan_probe_replay_r1",
        "files": {name: {"bytes": expected[0], "sha256": expected[1]} for name, expected in EXPECTED_SCAN.items()},
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 676, "errors": 0},
    }


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r63 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r63-transaction-contract-v1", "r63 contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "r63 contract ID mismatch")
    spec = contract.get("script")
    require(isinstance(spec, dict) and spec.get("path") == "srcmap/build_tohoku_r63.py", "r63 script pin missing")
    require(identity_from_bytes(SCRIPT_PATH.read_bytes()) == (spec.get("bytes"), spec.get("sha256")), "r63 script identity mismatch")
    engine = contract.get("engine")
    require(isinstance(engine, dict) and engine.get("path") == "srcmap/build_tohoku_r62.py", "r63 engine path mismatch")
    require((engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r63 engine contract mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r62/r62-check.json", "bytes": EXPECTED_R62_RECEIPT[0], "sha256": EXPECTED_R62_RECEIPT[1]}, "r63 predecessor contract mismatch")
    require(contract.get("frozen_prerequisite") == contract_bindings()["audit"], "r63 audit contract mismatch")
    require(contract.get("bound_inputs") == contract_bindings(), "r63 bound-input contract mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r63 scanner contract mismatch")
    require(contract.get("decision") == AUTHORIZED_DECISION, "r63 decision contract mismatch")
    require(contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r63 projected-count contract mismatch")
    require(contract.get("target") == "tohoku_r63", "r63 target contract mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r62" and transaction.get("stage") == ".tohoku-r63-txn", "r63 transaction paths mismatch")
    require(transaction.get("no_overwrite") is True and transaction.get("atomic_directory_rename") is True and transaction.get("post_promotion_replay") is True, "r63 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r63.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r63_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r62.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    cfg = json.loads(data.decode("utf-8"))
    require(cfg.get("dossier_id") == "tohoku_r62", "r62 cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "Inherited r63 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1042, "r62 decision schema/count drift")
    require(rows[-1]["decision_id"] == "D001042", "r62 decision tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, [DECISION], header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001043 append-row drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "Projected r63 decisions drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "Inherited r63 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r62 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r62 map schema/count drift")
    selected = E.one_row(rows, "unit_id", DECISION["unit_id"], "r62 map")
    require(selected["decision_id"] == "D000613" and selected["disposition"] == "new_statement", "r62 D1019 target state drift")
    require(selected["review_state"] == "reviewed_new_statement", "r62 D1019 review-state drift")
    require(selected["stacks_labels"] == "etale-cohomology-section-group-cohomology;stacks-cohomology-lemma-extension-coherent", "r62 D1019 predecessor labels drift")
    require(selected["stacks_tags"] == "0A2H;0GRA", "r62 D1019 predecessor tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:353", "r62 D1019 source locator drift")
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
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "Projected r63 map drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r62-check.json"
    E.require_identity(receipt, EXPECTED_R62_RECEIPT, "r62 receipt")
    for name, expected in EXPECTED_R62_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r62/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r62-v1", "r62 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r62 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 24, "r62 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R62_FILES), "r62 receipt inventory drift")
    replay = {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records}
    require(replay == EXPECTED_R62_FILES, "r62 receipt file identities drift")
    require(E.line_identity(E.SOURCE / "map.csv", 353) == EXPECTED_PREDECESSOR_MAP_ROW, "r62 target map row drift")
    return {"receipt": E.record(receipt, "tohoku_r62/r62-check.json")}


def read_spec(root: Path, spec: tuple[str, int, str], label: str) -> tuple[Path, bytes]:
    path = root / spec[0]
    return path, E.require_identity(path, (spec[1], spec[2]), label)


def verify_external() -> dict[str, Any]:
    execution = load_contract()
    predecessor = verify_predecessor()
    paths = {
        "audit": ROOT / "D1019_CHECK.json",
        "candidate": ROOT / "tmp" / "d1019_analytic_descent_candidate.tex",
        "design": ROOT / "tmp" / "d1019_analytic_descent_design.json",
        "review": ROOT / "tmp" / "d1019_independent_review_r2.json",
        "cohomology_tex": ROOT / "cohomology.tex",
        "bibliography": ROOT / "my.bib",
        "cohomology_pdf": ROOT / "cohomology.pdf",
    }
    bindings = contract_bindings()
    for role, path in paths.items():
        spec = bindings[role]
        E.require_identity(path, (spec["bytes"], spec["sha256"]), f"D1019 {role}")

    audit = E.strict_json(paths["audit"])
    design = E.strict_json(paths["design"])
    review = E.strict_json(paths["review"])
    require(audit.get("schema") == "tohoku-stacks-d1019-check-v1", "D1019 audit schema drift")
    require(audit.get("formalization_id") == "D1019", "D1019 audit formalization drift")
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R63_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1019 audit state drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("status") == "AUTHORIZED_FOR_NO_OVERWRITE_R63_TRANSACTION", "D1019 authorization state drift")
    require(authorization.get("predecessor") == "tohoku_r62" and authorization.get("successor") == "tohoku_r63", "D1019 authorization lineage drift")
    require(authorization.get("decision") == AUTHORIZED_DECISION, "D1019 decision authorization drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1019 append classification drift")
    require(authorization.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "D1019 authorized counts drift")
    replacement = authorization.get("map_replacement", {})
    require(replacement.get("physical_line") == 353 and replacement.get("source_locator_preserved") == "sem/r18/nodes.csv:353", "D1019 map replacement locator drift")
    require(replacement.get("only_fields_changed") == ["decision_id", "disposition", "review_state", "stacks_labels", "official_tags", "rationale"], "D1019 authorized changed fields drift")
    require(audit.get("scanner_probe", {}).get("status") == "PASS_BYTE_IDENTICAL_REPLAY", "D1019 scanner authorization drift")
    require(audit.get("scanner_probe", {}).get("files") == scanner_contract()["files"], "D1019 scanner file pins drift")
    require(audit.get("scanner_probe", {}).get("counts") == {
        "tex_files": 119,
        "labels": 22104,
        "official_tags_joined": 21437,
        "topics": 13,
        "topic_candidates": 1286,
        "direct_topic_coverage": 13,
        "warnings": 676,
        "errors": 0,
    }, "D1019 scanner counts drift")
    require(audit.get("stacks_edit", {}).get("postimage") == {"bytes": EXPECTED_COHOMOLOGY_TEX[0], "sha256": EXPECTED_COHOMOLOGY_TEX[1]}, "D1019 source postimage drift")
    require(audit.get("pdf_build", {}).get("postimage", {}).get("bytes") == EXPECTED_COHOMOLOGY_PDF[0], "D1019 PDF byte authorization drift")
    require(audit.get("pdf_build", {}).get("postimage", {}).get("sha256") == EXPECTED_COHOMOLOGY_PDF[1], "D1019 PDF hash authorization drift")
    require(audit.get("visual_qa", {}).get("status") == "PASS" and audit.get("visual_qa", {}).get("defects") == [], "D1019 visual QA drift")

    require(design.get("schema") == "tohoku-d1019-analytic-descent-design-v1", "D1019 design schema drift")
    require(design.get("status") == "REVISED_READY_FOR_SECOND_INDEPENDENT_REVIEW" and design.get("errors") == [], "D1019 design state drift")
    require(design.get("candidate", {}).get("bytes") == EXPECTED_CANDIDATE[0] and design.get("candidate", {}).get("sha256") == EXPECTED_CANDIDATE[1], "D1019 design candidate binding drift")
    projection = design.get("mapping_projection", {})
    require(projection.get("decision_id") == "D001043" and projection.get("supersedes") == "D000613", "D1019 design mapping lineage drift")
    require(projection.get("disposition") == "existing_equivalent" and projection.get("stacks_labels") == DECISION["stacks_labels"] and projection.get("stacks_tags") == "", "D1019 design mapping labels drift")
    require(projection.get("issue_append") is None and projection.get("source_repair_append") is None, "D1019 design append drift")

    require(review.get("schema") == "tohoku-d1019-independent-review-v2", "D1019 review schema drift")
    require(review.get("formalization_id") == "D1019" and review.get("status") == "STRICT_PASS_FOR_LIVE_INSERTION_AND_BUILD", "D1019 review state drift")
    for role, expected in (("candidate", EXPECTED_CANDIDATE), ("design", EXPECTED_DESIGN), ("bibliography", EXPECTED_BIBLIOGRAPHY)):
        item = review.get(role, {})
        require((item.get("bytes"), item.get("sha256")) == expected, f"D1019 review {role} binding drift")
    require(all(item.get("verdict") == "PASS" for item in review.get("reviews", [])) and len(review.get("reviews", [])) == 3, "D1019 review verdict drift")

    candidate_bytes = paths["candidate"].read_bytes()
    source_bytes = paths["cohomology_tex"].read_bytes()
    anchor_tail = b"\\label{remark-equivariant-extension-classes-analytic-boundary}\n\\end{remark}\n\n"
    require(source_bytes.count(anchor_tail + candidate_bytes) == 1, "D1019 candidate placement drift")
    require(source_bytes.count(candidate_bytes) == 1, "D1019 candidate insertion count drift")
    require(source_bytes.count(b"\\label{lemma-discontinuous-analytic-invariant-direct-image-coherent}") == 1, "D1019 new raw-label count drift")
    require(source_bytes.count(b"\\label{lemma-orbit-space-equivariant-cohomology-stabilizer-orders}") == 1, "D1019 existing comparison-label count drift")
    bib_bytes = paths["bibliography"].read_bytes()
    require(bib_bytes.count(b"@ARTICLE{Cartan-analytic-quotient,") == 1, "Cartan bibliography key drift")
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
    semantic_row = (886, "C70FA78166FA5BDB8EE9D52ECD48D09C18EF13F2F24AE492FBEAA7647FB5A5BE")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 353) == semantic_row, "sem/r18 D1019 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 353) == semantic_row, "sem/r21 D1019 row drift")
    segment_expected = {
        "dip": (418, "4BD311B2F0B0B7071A0C909424D88132A047AE60313BF357A992F459544D071D"),
        "fr": (418, "4BD311B2F0B0B7071A0C909424D88132A047AE60313BF357A992F459544D071D"),
        "en": (354, "95CE63EF6F3AE2056A95CBB1A213627473B512AE66AF7262510AF16D35EF74FA"),
    }
    for layer, data in page_bytes.items():
        require(identity_from_bytes(layer_segment(data, DECISION["unit_id"])) == segment_expected[layer], f"D1019 {layer} segment drift")
    stacks = {role: E.record(path, bindings[role]["path"]) for role, path in paths.items()}
    return {"execution": execution, "predecessor": predecessor, "stacks": stacks, "canonical": canonical}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == E.ORACLE_PAYLOAD, f"Scanner oracle surface drift: {root}")
        require(not any(path.is_dir() for path in root.iterdir()), f"Unexpected scanner oracle subdirectory: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "r63 scanner not PASS")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r63 scanner count drift")
    require(len(check.get("warnings", [])) == 676, "r63 scanner warning count drift")
    require(check.get("tex_sha256", {}).get("cohomology.tex") == EXPECTED_COHOMOLOGY_TEX[1], "r63 scanner cohomology.tex binding drift")
    _, rows = E.load_csv(root / "stx.csv")
    expected_rows = {
        "cohomology-lemma-orbit-space-equivariant-cohomology-stabilizer-orders": ("16865", "130C13A69DD7D36D3E3F14FDA97127CEA510928A36DF7E714E99EF08F630AE6F"),
        "cohomology-lemma-discontinuous-analytic-invariant-direct-image-coherent": ("20277", "AC355C08869E0130D3D39C0C93260B80ECE1D696540E554393352C568CB9C028"),
    }
    for label, (line, text_hash) in expected_rows.items():
        row = E.one_row(rows, "full_label", label, f"r63 scanner {label}")
        require(row["file"] == "cohomology.tex" and row["line"] == line and row["tag"] == "", f"r63 scanner row drift: {label}")
        require(row["text_sha256"] == text_hash, f"r63 scanner text drift: {label}")
    return check


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink(), "D1019 scanner oracle is missing or unsafe")
    require(E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "D1019 scanner replay is missing or unsafe")
    verify_scan(E.ORACLE, oracle_surface=True)
    verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"Scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1019_scan_probe_r1/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1019_scan_probe_replay_r1/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing or unsafe r63 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r63-check.json"} if receipt_mode else set()), "r63 output surface drift")
    require(not any(path.is_dir() for path in root.iterdir()), "Unexpected r63 output subdirectory")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r63 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"Inherited r63 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r63 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r63 map replacement drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r63 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R62_FILES["ucand.csv"], "r63/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r63 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r63 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 676, "r63 warning propagation drift")

    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1044)], "r63 decision sequence drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r63 issue sequence drift")
    require(decisions[-1] == DECISION, "r63 final decision row drift")
    selected = E.one_row(mapping, "unit_id", DECISION["unit_id"], "r63 map")
    require(selected["decision_id"] == "D001043" and selected["disposition"] == "existing_equivalent", "r63 target decision/disposition drift")
    require(selected["review_state"] == DECISION["review_state"], "r63 review state drift")
    require(selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "", "r63 labels/tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:353", "r63 source locator drift")
    require(E.line_identity(root / "map.csv", 353) == EXPECTED_SUCCESSOR_MAP_ROW, "r63 target map row identity drift")
    deltas = E.map_row_delta()
    require(len(deltas) == 6 and {row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r63 map delta cardinality/scope drift")
    require({row["field"] for row in deltas} == {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"}, "r63 map changed-field set drift")
    gap_dispositions = {"existing_weaker", "extend_existing", "new_section", "new_statement"}
    remaining = sum(1 for row in mapping if row["disposition"] in gap_dispositions)
    require(remaining == 23, "r63 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1043,
        "decisions_appended": ["D001043"],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 676, "errors": 0},
        "remaining_gap_class_dispositions": 23,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 6, "unchanged_units": 990},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1019_LIVE_SOURCE_BIBLIOGRAPHY_AND_PDF_PREREQUISITES_ALREADY_ADMITTED",
        "scanner_payload_change": "D1019_LIVE_SOURCE_REBIND_WITH_INHERITED_CFG",
    }
    if receipt_mode:
        receipt = E.strict_json(root / "r63-check.json")
        require(receipt == receipt_payload(root, result), "r63 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    stacks = external["stacks"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r63-v1",
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
            "change_class": "admitted_live_source_bibliography_pdf_plus_mapping_successor",
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
            "D001043 closes only the p.219 discontinuous-action characteristic-zero unit.",
            "The preceding Ext and H^1 units and the following compactness and finite-dimensionality unit remain separate.",
            "No issue, source repair, semantic successor, categorical descent for nontrivial stabilizers, GAGA comparison, release, publication, DOI, remote-freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r62"
    E.TARGET = ROOT / "tohoku_r63"
    E.STAGE = ROOT / ".tohoku-r63-txn"
    E.ORACLE = ROOT / "tmp" / "d1019_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1019_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R62_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R62_FILES
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r63 target or stage already exists")
    oracles = verify_oracles()
    print(
        json.dumps(
            {
                "schema": "tohoku-r63-scanner-oracle-v1",
                "status": "PASS_REPLAY",
                "errors": [],
                "scanner_oracles": oracles,
                "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 676, "errors": 0},
            },
            indent=2,
            sort_keys=True,
        )
    )


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r63 target or stage already exists")
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
                "schema": "tohoku-r63-static-input-audit-v1",
                "status": "PASS",
                "errors": [],
                "external": external,
                "scanner_oracles": oracles,
                "projection": projection,
                "decision": "D001043",
                "issue": None,
                "source_repair": None,
                "remaining_gaps": 23,
            },
            indent=2,
            sort_keys=True,
        )
    )


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r63 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    receipt = receipt_payload(E.STAGE, deltas)
    E.exclusive_write(E.STAGE / "r63-check.json", E.json_bytes(receipt))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r63 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("Post-promotion r63 replay failed; target rolled back") from exc
    print(
        json.dumps(
            {
                "schema": "tohoku-r63-transaction-result-v1",
                "status": "PASS_COMMITTED",
                "errors": [],
                "target": "tohoku_r63",
                "receipt": E.record(E.TARGET / "r63-check.json"),
                "remaining_gaps": 23,
            },
            indent=2,
            sort_keys=True,
        )
    )


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink(), "r63 target missing or unsafe")
    require(not E.STAGE.exists(), "r63 stage unexpectedly exists")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(
        json.dumps(
            {
                "schema": "tohoku-r63-replay-v1",
                "status": "PASS_REPLAY",
                "errors": [],
                "receipt": E.record(E.TARGET / "r63-check.json"),
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
