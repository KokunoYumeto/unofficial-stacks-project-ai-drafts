#!/usr/bin/env python3
"""Specialize the audited r61 transaction engine for D1018/r62."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import sys
import types
from pathlib import Path
from typing import Any, Mapping


SCRIPT_PATH = Path(__file__).resolve()
ROOT = SCRIPT_PATH.parent.parent
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r61.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r62_contract.json"
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

ENGINE_IDENTITY = (40313, "37D3CBB4C5E940F98F57F7AD9DF93CBCDC54F0E432E35EA18331FB05D1DD78EB")
CONTRACT_ID = "D1018-r62-D001042-v1"
EXPECTED_R61_RECEIPT = (10568, "D882C7AE62252BC94DA8D7D442A84507FCFC9F5E8E4C77CA988399E7EB835B80")
EXPECTED_R61_FILES = {
    "STATUS.md": (1162, "5001F1B33BF3C2FA12A4E9926755E35B9D2A681C6AF88D211793399FFAC85526"),
    "cfg.json": (5151, "7EA53BF72EA7BBCD5649DFF6598C802C503F355918A4DC11EB1C508ACEBB5CD2"),
    "check.json": (82634, "D5C19A9DEC66679F9AC616A0BDFB994A7334355F057D75B8648B774E57474AC9"),
    "dec.csv": (384781, "59D2C244243088BF6C0537088C7A8DD2F4FE37DBF1FCAA3FF3F3C821C1518B3F"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (484839, "5A4D3DA8211DB34DAD2F2717BFA07452A33E69811092190174AA0D5EFECEACC5"),
    "mcheck.json": (72461, "035737169ACAB848C67F88C47E163808E375C21A36085B026DD95138C84CA356"),
    "stx.csv": (5287716, "8AF5DD35D91AF45EC6DACE5F3DDC03213992D9EB6316353DC0FEABC7A9B23427"),
    "tcand.csv": (489256, "B7481F3F3FB7F5DDF59F6646B3DB440452751D760C21519D53619EB7510C4B13"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (82634, "DBDF93ADC67E74D8FBEB74C5147E714A24BB04E7B39EC32846C3210DC297EDD0"),
    "stx.csv": (5287716, "8AF5DD35D91AF45EC6DACE5F3DDC03213992D9EB6316353DC0FEABC7A9B23427"),
    "tcand.csv": (489256, "B7481F3F3FB7F5DDF59F6646B3DB440452751D760C21519D53619EB7510C4B13"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_PROJECTED = {
    "dec.csv": (385413, "9FF41BD33E9AC15FC6512BC4FD4B7E8C1F1804F4C3FDA8111AF55C1D8610DE9C"),
    "issues.csv": EXPECTED_R61_FILES["issues.csv"],
    "map.csv": (485159, "37CD0C823E7F3F6F3286D727EF6A312E5DC00EF7CA108A004FC46C617B7B6DA5"),
}
EXPECTED_DECISION_APPEND = (632, "AE79E3EF4A25DB9D75E813184A3761EEA65024FAF7FA03727B6B57D823906BC6")
EXPECTED_PREDECESSOR_MAP_ROW = (429, "E03DD2209A9CA224E5D3F6F6FB2193D60F01D231336AE6F3301FA45B65465CC3")
EXPECTED_SUCCESSOR_MAP_ROW = (749, "B1738F2E2413E2C267860C63D8674DEDA40C08CF1BBBE38524BB9D5683B71EA2")
EXPECTED_AUDIT = (6699, "A74F649A0AF0F1EE393145BD857D3C71442EC010CEF17BDDDF378DC6C5A6CA81")
EXPECTED_DESIGN = (6317, "9A309C2905D5A8A1CBE0E03E0F0A52728D0E4BFCA09FF8102304E05AFB7AFE21")
EXPECTED_REVIEW = (4760, "96FDDE23299B87B80E8BA2E50FFFAE4CDE3A4476F5EC937A01728F8403AAED25")

DECISION = {
    "decision_id": "D001042",
    "unit_id": "tohoku:definition:sheaf-hom-o",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "modules-definition-hom-left-modules;modules-lemma-sheaf-hom-left-modules",
    "rationale": "The D1017 noncommutative left-module definition gives Hom on every subspace by inverse image. For V contained in U, inverse-image functoriality supplies the natural restriction. The following lemma proves that the open-set rule is already a sheaf and identifies its sections with subspace Hom. Thus it gives the complete corrected source definition; equations (4.1.1)--(4.1.2) and the center-sheaf remark remain separate source units.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000407",
}
EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1042,
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
        "existing_equivalent": 385,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 6,
        "structural_only": 424,
    },
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r61 dossier is preserved exactly; D001042 closes the separate p.185 sheaf-Hom definition as a bounded mapping-only successor.\n"
    "- The D1017 arbitrary-ring-sheaf left-module definition supplies Hom on every subspace and canonical restriction; its lemma proves the open rule is a sheaf and identifies its sections with subspace Hom.\n"
    "- D001042 does not absorb equations (4.1.1)--(4.1.2), the center-module remark, or the preceding scalar-ring correction into this source unit.\n"
    "- The corrected p.185 source, reader v068c3r20, QA v68r42, sem/r21, modules.tex/modules.pdf, D1018 design, and independent review are bound byte-exactly; no new TeX, PDF, source repair, issue, or semantic successor is required.\n"
    "- The scanner indexes the exact 119 top-level TeX files with 22,103 labels, 675 warnings, and no errors.\n"
    "- There are 1,042 decisions, 679 decided units, 32 resolved source issues, and 24 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the reported VPN/security review; local work continues and no GitHub or Git operation is attempted.\n"
    "- No Ext construction, GAGA comparison, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.\n"
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
    "p185_dip": ("build/v068c3r20/src/dip/p185.tex", 3964, "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A"),
    "p185_fr": ("build/v068c3r20/src/fr/p185.tex", 4298, "EBE37CBFBE00FA4CA72C21CC4C542D60603A61E92EE446D15C941FA136B20847"),
    "p185_en": ("build/v068c3r20/src/en/p185.tex", 4178, "9F3F8C932149B3F2ECC9A25C4D4C2D010A48A2CFE6B621CE12BE178CC4DADE60"),
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
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r61 transaction engine identity drift")
    module = types.ModuleType("tohoku_r62_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r61 transaction engine changed during load")
    return module


E = load_engine()


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r62 contract missing or unsafe")
    raw = CONTRACT_PATH.read_bytes()
    contract = json.loads(raw.decode("utf-8"))
    require(contract.get("schema") == "tohoku-r62-transaction-contract-v1", "r62 contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "r62 contract ID mismatch")
    spec = contract.get("script")
    require(isinstance(spec, dict) and spec.get("path") == "srcmap/build_tohoku_r62.py", "r62 script pin missing")
    require(identity_from_bytes(SCRIPT_PATH.read_bytes()) == (spec.get("bytes"), spec.get("sha256")), "r62 script identity mismatch")
    engine = contract.get("engine")
    require(isinstance(engine, dict) and (engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r62 engine contract mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r61/r61-check.json", "bytes": EXPECTED_R61_RECEIPT[0], "sha256": EXPECTED_R61_RECEIPT[1]}, "r62 predecessor contract mismatch")
    require(contract.get("target") == "tohoku_r62", "r62 target contract mismatch")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r62.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r62_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r61.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    cfg = E.strict_json(E.SOURCE / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r61", "r61 cfg dossier drift")
    cfg["dossier_id"] = "tohoku_r62"
    data = E.json_bytes(cfg)
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "Projected r62 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1041, "r61 decision schema/count drift")
    require(rows[-1]["decision_id"] == "D001041", "r61 decision tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, [DECISION], header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001042 append-row drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "Projected r62 decisions drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "Inherited r62 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r61 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r61 map schema/count drift")
    selected = E.one_row(rows, "unit_id", DECISION["unit_id"], "r61 map")
    require(selected["decision_id"] == "D000407" and selected["disposition"] == "existing_weaker", "r61 D1018 target state drift")
    require(selected["stacks_labels"] == "modules-section-internal-hom" and selected["stacks_tags"] == "01CM", "r61 D1018 predecessor labels/tags drift")
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
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "Projected r62 map drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r61-check.json"
    E.require_identity(receipt, EXPECTED_R61_RECEIPT, "r61 receipt")
    for name, expected in EXPECTED_R61_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r61/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r61-v1", "r61 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r61 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 25, "r61 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R61_FILES), "r61 receipt inventory drift")
    replay = {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records}
    require(replay == EXPECTED_R61_FILES, "r61 receipt file identities drift")
    require(E.line_identity(E.SOURCE / "map.csv", 351) == EXPECTED_PREDECESSOR_MAP_ROW, "r61 target map row drift")
    return {"receipt": E.record(receipt, "tohoku_r61/r61-check.json")}


def read_spec(root: Path, spec: tuple[str, int, str], label: str) -> tuple[Path, bytes]:
    path = root / spec[0]
    return path, E.require_identity(path, (spec[1], spec[2]), label)


def verify_external() -> dict[str, Any]:
    execution = load_contract()
    predecessor = verify_predecessor()
    audit_path = ROOT / "D1018_MAPPING_CHECK.json"
    design_path = ROOT / "tmp" / "d1018_p185_mapping_design.json"
    review_path = ROOT / "tmp" / "d1018_independent_review_r1.json"
    E.require_identity(audit_path, EXPECTED_AUDIT, "D1018 audit")
    E.require_identity(design_path, EXPECTED_DESIGN, "D1018 design")
    E.require_identity(review_path, EXPECTED_REVIEW, "D1018 review")
    audit = E.strict_json(audit_path)
    design = E.strict_json(design_path)
    review = E.strict_json(review_path)
    require(audit.get("status") == "STRICT_PASS_R62_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1018 audit state drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("decision") == DECISION, "D1018 decision authorization drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1018 append classification drift")
    require(design.get("status") == "STRICT_DESIGN_PASS_MAPPING_ONLY", "D1018 design state drift")
    require(design.get("mapping_projection", {}).get("decision_id") == "D001042", "D1018 design decision drift")
    require(review.get("status") == "STRICT_PASS_MAPPING_ONLY" and review.get("final_verdict") == "STRICT_PASS_NO_LIVE_SOURCE_CHANGE", "D1018 review state drift")
    require(review.get("predicate_summary") == {"total": 8, "passed": 8, "failed": 0}, "D1018 review predicate summary drift")

    stacks = {
        "audit": E.record(audit_path, "D1018_MAPPING_CHECK.json"),
        "design": E.record(design_path, "tmp/d1018_p185_mapping_design.json"),
        "review": E.record(review_path, "tmp/d1018_independent_review_r1.json"),
        "candidate": E.record(ROOT / "tmp" / "d1017_noncommutative_internal_hom_candidate.tex", "tmp/d1017_noncommutative_internal_hom_candidate.tex"),
        "modules_tex": E.record(ROOT / "modules.tex", "modules.tex"),
        "modules_pdf": E.record(ROOT / "modules.pdf", "modules.pdf"),
    }
    require((stacks["candidate"]["bytes"], stacks["candidate"]["sha256"]) == (5063, "FB6278770580656A6904DC4505A7E69DAB222710D62633937125C557A2E75190"), "D1017 candidate drift")
    require((stacks["modules_tex"]["bytes"], stacks["modules_tex"]["sha256"]) == (232828, "EF800D241EBA37CE7099F9B09440228969710988903EE393261C866F902A12F5"), "modules.tex drift")
    require((stacks["modules_pdf"]["bytes"], stacks["modules_pdf"]["sha256"]) == (767323, "A35B4D3FDD5A8A106A24570FA6E8890BACF45E83BD01B2F949A838F33D311638"), "modules.pdf drift")
    require((ROOT / "modules.tex").read_bytes().count((ROOT / "tmp" / "d1017_noncommutative_internal_hom_candidate.tex").read_bytes()) == 1, "D1017 block insertion drift")

    canonical: dict[str, Any] = {}
    values: dict[str, Any] = {}
    page_bytes: dict[str, bytes] = {}
    for role, spec in CANONICAL_INPUTS.items():
        path, data = read_spec(CANONICAL_ROOT, spec, role)
        canonical[role] = E.record(path, spec[0])
        if spec[0].endswith(".json"):
            values[role] = json.loads(data.decode("utf-8"))
        if role.startswith("p185_"):
            page_bytes[role.removeprefix("p185_")] = data
    require(values["source_receipt"].get("status") == "PASS", "p185 source receipt drift")
    require(values["reader_receipt"].get("status") == "PASS" and values["reader_receipt"].get("revision") == "v068c3r20", "reader receipt drift")
    require(values["qa_receipt"].get("status") == "PASS" and values["qa_receipt"].get("qa_revision") == "v68r42", "QA receipt drift")
    require(values["sem_r21_manifest"].get("schema") == "tohoku-semantic-local-successor-manifest-v21", "sem/r21 manifest drift")
    require(values["sem_r21_validation"].get("status") == "PASS", "sem/r21 validation drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 351) == (704, "D57BC824E2828791245220CAD081447037640BAF36200495B7F4B2863234B15C"), "sem/r18 D1018 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 351) == (704, "D57BC824E2828791245220CAD081447037640BAF36200495B7F4B2863234B15C"), "sem/r21 D1018 row drift")
    segment_expected = {
        "dip": (341, "96F198E48170B81CDAF6F35BFF3DD965D55105F43FD55F3CDFB5113F5C2CAAD8"),
        "fr": (341, "C2F07807B17FFB7D3F87E95AA18BA40ABD9F52767E36A346C16EF8DD9705F7AE"),
        "en": (319, "7028A96F2FCA91F8A1299EA4673C773AB0C525C1356C8FFC3A6B5A9200767EB7"),
    }
    for layer, data in page_bytes.items():
        segment = layer_segment(data, "tohoku:definition:sheaf-hom-o")
        require(identity_from_bytes(segment) == segment_expected[layer], f"D1018 {layer} segment drift")
    return {
        "execution": execution,
        "predecessor": predecessor,
        "stacks": stacks,
        "canonical": canonical,
    }


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing or unsafe r62 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r62-check.json"} if receipt_mode else set()), "r62 output surface drift")
    require(not any(path.is_dir() for path in root.iterdir()), "Unexpected r62 output subdirectory")
    require((root / "cfg.json").read_bytes() == E.expected_cfg_bytes(), "r62 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"Inherited r62 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r62 decision append drift")
    require((root / "map.csv").read_bytes() == E.expected_map_bytes(), "r62 map replacement drift")
    require((root / "STATUS.md").read_bytes() == E.STATUS_BYTES, "r62 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R61_FILES["ucand.csv"], "r62/ucand.csv")
    E.verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r62 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r62 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 675, "r62 warning propagation drift")

    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1043)], "r62 decision sequence drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r62 issue sequence drift")
    require(decisions[-1] == DECISION, "r62 final decision row drift")
    selected = E.one_row(mapping, "unit_id", DECISION["unit_id"], "r62 map")
    require(selected["decision_id"] == "D001042" and selected["disposition"] == "existing_equivalent", "r62 target decision/disposition drift")
    require(selected["review_state"] == DECISION["review_state"], "r62 review state drift")
    require(selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "", "r62 labels/tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:351", "r62 source locator drift")
    require(E.line_identity(root / "map.csv", 351) == EXPECTED_SUCCESSOR_MAP_ROW, "r62 target map row identity drift")
    deltas = E.map_row_delta()
    require(len(deltas) == 6 and {row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r62 map delta cardinality/scope drift")
    require({row["field"] for row in deltas} == {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"}, "r62 map changed-field set drift")
    gap_dispositions = {"existing_weaker", "extend_existing", "new_section", "new_statement"}
    remaining = sum(1 for row in mapping if row["disposition"] in gap_dispositions)
    require(remaining == 24, "r62 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1042,
        "decisions_appended": ["D001042"],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**E.EXPECTED_SCAN_COUNTS, "warnings": 675, "errors": 0},
        "remaining_gap_class_dispositions": 24,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 6, "unchanged_units": 990},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1018_MAPPING_ONLY_NO_LIVE_SOURCE_CHANGE",
        "scanner_payload_change": "R62_NAMESPACE_ONLY",
    }
    if receipt_mode:
        receipt = E.strict_json(root / "r62-check.json")
        require(receipt == receipt_payload(root, result), "r62 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = E.verify_oracles()
    return {
        "schema": "tohoku-stacks-mapping-successor-r62-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalization": {
            **external["stacks"],
            "change_class": "mapping_only_no_live_source_or_pdf_change",
        },
        "source_chain": {
            "source_admission": external["canonical"]["source_receipt"],
            "reader_receipt": external["canonical"]["reader_receipt"],
            "qa_receipt": external["canonical"]["qa_receipt"],
            "sem_r21_manifest": external["canonical"]["sem_r21_manifest"],
            "sem_r21_validation": external["canonical"]["sem_r21_validation"],
            "sem_r21_nodes": external["canonical"]["sem_r21_nodes"],
        },
        "scanner_oracle": oracles["oracle"],
        "scanner_replay": oracles["replay"],
        "external_constraints": {
            "github": {
                "status": "temporarily_unavailable",
                "reason": "Account security suspension reported after VPN use; support ticket filed.",
                "action": "Continue local production and QA; defer GitHub-only actions; no Git or GitHub operation is attempted.",
            }
        },
        "deltas": dict(deltas),
        "files": E.output_records(root),
        "nonclaims": [
            "D001042 closes the separately selected restriction-and-sheaf definition only.",
            "Equations (4.1.1)--(4.1.2), the center-module remark, and Ext remain separate source units.",
            "No source repair, issue, semantic successor, TeX edit, PDF build, GAGA comparison, release, publication, DOI, remote-freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink(), "r62 scanner oracle is missing or unsafe")
    require(E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "r62 scanner replay is missing or unsafe")
    E.verify_scan(E.ORACLE, oracle_surface=True)
    E.verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in E.EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"Scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1018_r62_scan_oracle/{name}") for name in sorted(E.EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1018_r62_scan_replay/{name}") for name in sorted(E.EXPECTED_SCAN)},
    }


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r62 target or stage already exists")
    external = verify_external()
    oracles = E.verify_oracles()
    projection = {
        "cfg.json": identity_from_bytes(E.expected_cfg_bytes()),
        "dec.csv": identity_from_bytes(expected_decision_bytes()),
        "issues.csv": identity_from_bytes(expected_issue_bytes()),
        "map.csv": identity_from_bytes(E.expected_map_bytes()),
        "STATUS.md": identity_from_bytes(E.STATUS_BYTES),
    }
    print(
        json.dumps(
            {
                "schema": "tohoku-r62-static-input-audit-v1",
                "status": "PASS",
                "errors": [],
                "external": external,
                "scanner_oracles": oracles,
                "projection": projection,
                "decision": "D001042",
                "issue": None,
                "remaining_gaps": 24,
            },
            indent=2,
            sort_keys=True,
        )
    )


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r61"
    E.TARGET = ROOT / "tohoku_r62"
    E.STAGE = ROOT / ".tohoku-r62-txn"
    E.ORACLE = ROOT / "tmp" / "d1018_r62_scan_oracle"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1018_r62_scan_replay"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R61_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R61_FILES
    E.EXPECTED_SCAN = EXPECTED_SCAN
    E.EXPECTED_PROJECTED = EXPECTED_PROJECTED
    E.EXPECTED_APPEND_ROWS = {"decision": EXPECTED_DECISION_APPEND}
    E.EXPECTED_PREDECESSOR_MAP_ROW = EXPECTED_PREDECESSOR_MAP_ROW
    E.EXPECTED_SUCCESSOR_MAP_ROW = EXPECTED_SUCCESSOR_MAP_ROW
    E.EXPECTED_D1017_AUDIT = EXPECTED_AUDIT
    E.DECISION = DECISION
    E.EXPECTED_COUNTS = EXPECTED_COUNTS
    E.STATUS_BYTES = STATUS_BYTES
    E.STACKS_INPUTS = {
        "modules_tex": ("modules.tex", 232828, "EF800D241EBA37CE7099F9B09440228969710988903EE393261C866F902A12F5")
    }
    E.load_contract = load_contract
    E.expected_cfg_bytes = expected_cfg_bytes
    E.expected_decision_bytes = expected_decision_bytes
    E.expected_issue_bytes = expected_issue_bytes
    E.expected_map_bytes = expected_map_bytes
    E.verify_predecessor = verify_predecessor
    E.verify_external = verify_external
    E.verify_oracles = verify_oracles
    E.verify_stage = verify_stage
    E.receipt_payload = receipt_payload


configure_engine()


def generate_oracles() -> None:
    load_contract()
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r62 target or stage already exists")
    if E.ORACLE.exists():
        E.verify_scan(E.ORACLE, oracle_surface=True)
    else:
        E.build_oracle_dir(E.ORACLE)
    if E.ORACLE_REPLAY.exists():
        E.verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    else:
        E.build_oracle_dir(E.ORACLE_REPLAY)
    for name in E.EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"Scanner replay differs: {name}")
    print(
        json.dumps(
            {
                "schema": "tohoku-r62-scanner-oracle-v1",
                "status": "PASS",
                "errors": [],
                "oracle": {name: E.record(E.ORACLE / name) for name in sorted(E.EXPECTED_SCAN)},
                "replay": {name: E.record(E.ORACLE_REPLAY / name) for name in sorted(E.EXPECTED_SCAN)},
                "counts": {**E.EXPECTED_SCAN_COUNTS, "warnings": 675, "errors": 0},
            },
            indent=2,
            sort_keys=True,
        )
    )


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r62 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    receipt = receipt_payload(E.STAGE, deltas)
    E.exclusive_write(E.STAGE / "r62-check.json", E.json_bytes(receipt))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r62 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("Post-promotion r62 replay failed; target rolled back") from exc
    print(
        json.dumps(
            {
                "schema": "tohoku-r62-transaction-result-v1",
                "status": "PASS_COMMITTED",
                "errors": [],
                "target": "tohoku_r62",
                "receipt": E.record(E.TARGET / "r62-check.json"),
                "remaining_gaps": 24,
            },
            indent=2,
            sort_keys=True,
        )
    )


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink(), "r62 target missing or unsafe")
    require(not E.STAGE.exists(), "r62 stage unexpectedly exists")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(
        json.dumps(
            {
                "schema": "tohoku-r62-replay-v1",
                "status": "PASS_REPLAY",
                "errors": [],
                "receipt": E.record(E.TARGET / "r62-check.json"),
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
            generate_oracles()
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
