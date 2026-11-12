#!/usr/bin/env python3
"""Build and seal the audited D1023/r67 mapping successor."""

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
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r66.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r67_contract.json"
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

ENGINE_IDENTITY = (44920, "11708EFC7545E664DAF0EA684ECDDF091D8E0D8B79EB7D719CB4F79E0B97E23C")
CONTRACT_ID = "D1023-r67-D001047-v1"
EXPECTED_R66_RECEIPT = (12365, "E9384690C42E1FD5BEBBA440F37A6E4B8F81AF2A256B4370F5CBAADC5B2A53B2")
EXPECTED_R66_FILES = {
    "STATUS.md": (1259, "46953E81513C1AE7881EEB5C064D149FEF00332719B45EC35DF2030F3FC99E14"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83391, "EEE21BF2A81BBD214CF7BC6F8968500229CD00DA19D46EC9EC0C7B70A62A1BDB"),
    "dec.csv": (388554, "63C36B2277BB5F783A691F70A038F08052CCA4B241B8577F72CD09D9C8DCE431"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (486832, "11D626A8F99DC5FD529B3C4CBE31BBDD433EDD8B5DBB84182647037EFCE67765"),
    "mcheck.json": (73218, "23DBDD0ABBFD6D9460443D434BDF29116D7D1285DD4F158433C80755CB07EC0A"),
    "stx.csv": (5289572, "0B1FA83BF876F2C0A508E7E6EE5721E986A105481738143F59AAEB2611F9ECBD"),
    "tcand.csv": (489256, "794FAB6C0346B7A6698E0936348B81310885E092EEC8E33142DDF6301FFCA83E"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83497, "1AA4000FB3ABF3010601723CEB492D4601EBF6248F3D4628D2158F7397ED818A"),
    "stx.csv": (5289847, "3D30F990EEB11B7C509AFF9E92EAB2A94CDCCE9352535B98CEA4D91FD0951D1B"),
    "tcand.csv": (489711, "881583ED4E0390FDB6FCE4DDCB918396B947F0CA4E3EDD113EF47DB1B113FA7D"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22110,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1287,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_PROJECTED = {
    "dec.csv": (389259, "F96B147AD9EBDBF386B41A4400CA132967003BF976E75311B81DA9CA3D77107E"),
    "issues.csv": EXPECTED_R66_FILES["issues.csv"],
    "map.csv": (487180, "7D99ADBD373B8D8D251BAA4D7E8A258AE50358F5FEBEF147D07B13B6DE63750F"),
}
EXPECTED_DECISION_APPEND = (705, "5D03E5FB5A5900D615AEBFC25F3362E9530B7E05D5C7F583011C068177E59342")
EXPECTED_PREDECESSOR_MAP_ROW = (557, "996280C59C4F4F9B75E18AFB1BD5022CFAA9C60F715B38FBA0528A85A286C51B")
EXPECTED_SUCCESSOR_MAP_ROW = (905, "BB240F11649E4971D3FA7888A6A4C9F39FCD09ED4D5510D0B4712D8AB9E97297")
EXPECTED_AUDIT = (12926, "5EC28DB44F5ACAA9E5E76294DF0B838921CA72AD62D7F54B7B74D52D85802158")
EXPECTED_COHOMOLOGY_TEX = (939192, "2B665E090457B701C2BF906517CFA30C6628FD8EA3F1462E2CEA90E54171286A")
EXPECTED_BIBLIOGRAPHY = (220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE")
EXPECTED_COHOMOLOGY_PDF = (2037628, "3016226B78BAED6DA3011AEA66C7838FC27498BD3993645D9AC1F50014E1C54F")

DECISION = {
    "decision_id": "D001047",
    "unit_id": "tohoku:obstruction:cech-not-cohomological",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-cech-cohomology-not-delta-functor",
    "rationale": "Stacks now gives a finite-space realization of the source counterexample. For a short exact sequence of abelian sheaves it computes check H1(G)=0, check H1(H)=Z, and check H2(F)=0 while derived H2(F)=Z. Thus global Cech cohomology cannot in general be a cohomological delta functor, and the canonical degree-two injection need not be surjective. Positive paracompact or acyclic-cover comparison results, the source's circle illustration, and its longer check H1(X,H1(F)) calculation are separate and are not remapped.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000421",
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
    "decisions": 1047,
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
        "existing_equivalent": 390,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 10,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 2,
        "structural_only": 424,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1047,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 390,
    "new_statement": 2,
    "remaining_gap_class_dispositions": 19,
    "source_repairs_appended": 0,
    "mapping_closures": 1,
    "changed_map_rows": 1,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r66 dossier is preserved exactly; D001047 closes the p.174 global-Cech obstruction unit in a no-overwrite r67 successor.\n"
    "- The admitted D1023 source gives a finite-space counterexample proving that global direct-limit Cech cohomology is not generally a cohomological delta functor and that the degree-two comparison need not be surjective.\n"
    "- The D1023 audit, independent review, live TeX/PDF build, supporting build files, visual rasters, source evidence, and scanner oracle/replay are bound byte-exactly.\n"
    "- No issue or source-repair row is appended; only the authorized D000421 map row is replaced.\n"
    "- The scanner indexes 119 top-level TeX files with 22,110 labels, 682 warnings, and no errors.\n"
    "- There are 1,047 decisions, 679 decided units, 32 resolved source issues, and 19 gap-class dispositions remain.\n"
    "- GitHub availability was restored by direct user update; this bounded local transaction requires no Git or GitHub operation.\n"
    "- No claim is made against positive paracompact or acyclic-cover comparisons, for every degree-two comparison, for the separate circle or longer H1 example, GAGA, release, publication, DOI, remote freshness, rights, or whole-paper completion.\n"
).encode("utf-8")

ROOT_BINDINGS = {
    "audit": ("D1023_CHECK.json", 12926, "5EC28DB44F5ACAA9E5E76294DF0B838921CA72AD62D7F54B7B74D52D85802158"),
    "review": ("tmp/d1023_independent_review_r1.json", 1825, "40DF8B9A534013AFF4924C82D8F72DE10A26A7BD04E10F761170575555BDCE38"),
    "cohomology_tex": ("cohomology.tex", 939192, "2B665E090457B701C2BF906517CFA30C6628FD8EA3F1462E2CEA90E54171286A"),
    "bibliography": ("my.bib", 220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE"),
    "cohomology_pdf": ("cohomology.pdf", 2037628, "3016226B78BAED6DA3011AEA66C7838FC27498BD3993645D9AC1F50014E1C54F"),
    "cohomology_aux": ("cohomology.aux", 58430, "D83ABF0160B18481387B7AE599648A215CE1EF9563AFA2A93713B1F5F7367773"),
    "cohomology_bbl": ("cohomology.bbl", 2313, "B549EC2BF6A2D441ABC2587AEB0D81AAB800C65A0F4461EC39573EACB228034A"),
    "cohomology_blg": ("cohomology.blg", 1037, "AD428028D6914435597B90AC92610E926BBA25B968AC3102678A58B633397428"),
    "cohomology_log": ("cohomology.log", 48305, "5CFC1E0075DB59B010476FCB3D11F5FA35405E89343899131811D7D89943F16D"),
    "page_043": ("tmp/d1023_pdf_qa/page-043.png", 295999, "B6619CA5ADAE0B800A48CEEAF611D57B9296C86CC35004DF0C2911D6106490D9"),
    "page_044": ("tmp/d1023_pdf_qa/page-044.png", 273930, "12D0DE2FA737B34A697AE63F813868DE9781FA3401C15A8E9FAD0D77C53DF2EB"),
    "page_045": ("tmp/d1023_pdf_qa/page-045.png", 246202, "6940B2E437590703E1769D21D972F127C9C8DE65075417CB86167CE4F9481835"),
    "page_046": ("tmp/d1023_pdf_qa/page-046.png", 312081, "7E48897510308698E8F3DFBE78FA4E887134E01BBCD42D9721FDF61D66280752"),
    "page_047": ("tmp/d1023_pdf_qa/page-047.png", 303288, "465E3D899E27D3C1133339C3EACE52E113FBDF165D42BB993CE848A4465D50CF"),
    "page_048": ("tmp/d1023_pdf_qa/page-048.png", 300327, "9C24CF5F471E901FE77B7070317862CFD06557B22F0E61A7C2BFB9335315B6E4"),
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
    "p174_dip": ("build/v068c3r20/src/dip/p174.tex", 4016, "0670ADC79E961CF1D48150D1C90BF06B90C80AA72206857D1F5AD69DFEEAFCFB"),
    "p174_fr": ("build/v068c3r20/src/fr/p174.tex", 4031, "130C766F27F6DEAF0E4B3411AD01111817AEFF27FE8AA0DB8714DB4D8764EB4B"),
    "p174_en": ("build/v068c3r20/src/en/p174.tex", 3662, "AD5924DC988327A5D823B511FAD1BF7107495C497F89823F3F9496F34050F58B"),
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
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r66 transaction engine identity drift")
    module = types.ModuleType("tohoku_r67_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r66 transaction engine changed during load")
    return module


M = load_engine()
E = M.E


def contract_bindings() -> dict[str, Any]:
    return {role: {"path": spec[0], "bytes": spec[1], "sha256": spec[2]} for role, spec in ROOT_BINDINGS.items()}


def scanner_contract() -> dict[str, Any]:
    return {
        "oracle_path": "tmp/d1023_scan_probe_r1",
        "replay_path": "tmp/d1023_scan_probe_replay_r1",
        "files": {name: {"bytes": value[0], "sha256": value[1]} for name, value in EXPECTED_SCAN.items()},
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 682, "errors": 0},
    }


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r67 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r67-transaction-contract-v1", "r67 contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "r67 contract ID mismatch")
    script = contract.get("script")
    require(isinstance(script, dict) and script.get("path") == "srcmap/build_tohoku_r67.py", "r67 script pin missing")
    require(identity_from_bytes(SCRIPT_PATH.read_bytes()) == (script.get("bytes"), script.get("sha256")), "r67 script identity mismatch")
    engine = contract.get("engine")
    require(isinstance(engine, dict) and engine.get("path") == "srcmap/build_tohoku_r66.py", "r67 engine path mismatch")
    require((engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r67 engine identity mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r66/r66-check.json", "bytes": EXPECTED_R66_RECEIPT[0], "sha256": EXPECTED_R66_RECEIPT[1]}, "r67 predecessor contract mismatch")
    require(contract.get("frozen_prerequisite") == contract_bindings()["audit"], "r67 frozen prerequisite mismatch")
    require(contract.get("bound_inputs") == contract_bindings(), "r67 bound inputs mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r67 scanner contract mismatch")
    require(contract.get("decision") == AUTHORIZED_DECISION, "r67 decision contract mismatch")
    require(contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r67 projected counts mismatch")
    require(contract.get("target") == "tohoku_r67", "r67 target mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r66" and transaction.get("stage") == ".tohoku-r67-txn", "r67 transaction paths mismatch")
    require(transaction.get("no_overwrite") is True and transaction.get("atomic_directory_rename") is True and transaction.get("post_promotion_replay") is True, "r67 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r67.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r67_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r66.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    require(json.loads(data.decode("utf-8")).get("dossier_id") == "tohoku_r62", "inherited cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "inherited r67 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1046 and rows[-1]["decision_id"] == "D001046", "r66 decision schema/count/tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, [DECISION], header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001047 append row drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "projected r67 decision bytes drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "inherited r67 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r66 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r66 map schema/count drift")
    selected = E.one_row(rows, "unit_id", DECISION["unit_id"], "r66 map")
    require(selected["decision_id"] == "D000421" and selected["disposition"] == "extend_existing", "r66 D1023 target state drift")
    require(selected["review_state"] == "reviewed_gap", "r66 D1023 review state drift")
    require(selected["stacks_labels"] == "cohomology-section-cohomology-LC" and selected["stacks_tags"] == "09V0", "r66 D1023 predecessor label/tag drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:651", "r66 D1023 source locator drift")
    replacement = selected.copy()
    replacement.update({
        "decision_id": DECISION["decision_id"],
        "disposition": DECISION["disposition"],
        "review_state": DECISION["review_state"],
        "stacks_labels": DECISION["stacks_labels"],
        "stacks_tags": "",
        "rationale": DECISION["rationale"],
    })
    data = E.csv_bytes(fields, [replacement if row["unit_id"] == DECISION["unit_id"] else row for row in rows])
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "projected r67 map bytes drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r66-check.json"
    E.require_identity(receipt, EXPECTED_R66_RECEIPT, "r66 receipt")
    for name, expected in EXPECTED_R66_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r66/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r66-v1", "r66 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r66 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 20, "r66 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R66_FILES), "r66 receipt inventory drift")
    replay = {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records}
    require(replay == EXPECTED_R66_FILES, "r66 receipt file identities drift")
    require(E.line_identity(E.SOURCE / "map.csv", 651) == EXPECTED_PREDECESSOR_MAP_ROW, "r66 target map row drift")
    return {"receipt": E.record(receipt, "tohoku_r66/r66-check.json")}


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
        E.require_identity(path, (spec["bytes"], spec["sha256"]), f"D1023 {role}")
    audit = E.strict_json(paths["audit"])
    review = E.strict_json(paths["review"])
    require(audit.get("schema") == "tohoku-stacks-d1023-check-v1" and audit.get("formalization_id") == "D1023", "D1023 audit identity drift")
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R67_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1023 audit state drift")
    selection = audit.get("selection", {})
    require(selection.get("unit") == DECISION["unit_id"] and selection.get("source_locator") == "sem/r18/nodes.csv:651", "D1023 selection drift")
    require(selection.get("predecessor_decision") == "D000421" and selection.get("predecessor_dossier") == "tohoku_r66", "D1023 predecessor selection drift")
    require(selection.get("predecessor_map_row_with_lf") == {"physical_line": 651, "bytes": EXPECTED_PREDECESSOR_MAP_ROW[0], "sha256": EXPECTED_PREDECESSOR_MAP_ROW[1]}, "D1023 predecessor row binding drift")
    require(audit.get("source_claim", {}).get("source_repair_required") is False and audit.get("source_claim", {}).get("transcription_or_translation_repair_required") is False, "D1023 unexpected source repair")
    require(audit.get("independent_review", {}).get("path") == ROOT_BINDINGS["review"][0] and (audit.get("independent_review", {}).get("bytes"), audit.get("independent_review", {}).get("sha256")) == ROOT_BINDINGS["review"][1:], "D1023 review binding drift")
    require(audit.get("independent_review", {}).get("status") == "STRICT_PASS_FOR_R67_MAPPING", "D1023 review status drift")
    edit = audit.get("stacks_edit", {})
    require((edit.get("postimage", {}).get("bytes"), edit.get("postimage", {}).get("sha256")) == EXPECTED_COHOMOLOGY_TEX, "D1023 live TeX evidence drift")
    require(edit.get("new_block") == {"lines": "4465--4597", "bytes_with_terminal_lf": 4658, "sha256_with_terminal_lf": "53D9BD637E14B3079FCB9A5527AAFCBCB2EE5413441B62A34888C52CB90873C1"}, "D1023 block evidence drift")
    require(edit.get("new_raw_label") == {"label": "lemma-cech-cohomology-not-delta-functor", "line": 4466, "occurrences": 1}, "D1023 raw-label evidence drift")
    require(edit.get("source_citation_occurrences") == 1 and edit.get("unrelated_live_source_files_changed_by_insertion") == 0, "D1023 insertion scope drift")
    pdf = audit.get("pdf_build", {})
    require((pdf.get("postimage", {}).get("bytes"), pdf.get("postimage", {}).get("sha256")) == EXPECTED_COHOMOLOGY_PDF, "D1023 live PDF evidence drift")
    require(pdf.get("postimage", {}).get("pages") == 245 and pdf.get("postimage", {}).get("pdf_version") == "1.5" and pdf.get("final_driver_exit_code") == 0, "D1023 PDF gate drift")
    require(all(value == 0 for value in pdf.get("diagnostics", {}).values()), "D1023 PDF diagnostics drift")
    support = {"aux": "cohomology_aux", "bbl": "cohomology_bbl", "blg": "cohomology_blg", "log": "cohomology_log"}
    for key, role in support.items():
        value = pdf.get("supporting_files", {}).get(key, {})
        require((value.get("bytes"), value.get("sha256")) == ROOT_BINDINGS[role][1:], f"D1023 {key} binding drift")
    visual = audit.get("visual_qa", {})
    require(visual.get("status") == "STRICT_PASS" and visual.get("defects") == [] and visual.get("inspected_pdf_pages") == [43, 44, 45, 46, 47, 48], "D1023 visual QA drift")
    require(len(visual.get("rasters", [])) == 6, "D1023 raster count drift")
    for row, page in zip(visual.get("rasters", []), range(43, 49)):
        role = f"page_{page:03d}"
        require(row.get("path") == ROOT_BINDINGS[role][0] and (row.get("bytes"), row.get("sha256")) == ROOT_BINDINGS[role][1:], f"D1023 page {page} raster drift")
    probe = audit.get("scanner_probe", {})
    require(probe.get("status") == "PASS_BYTE_IDENTICAL_REPLAY", "D1023 scanner audit state drift")
    require(probe.get("oracle_path") == scanner_contract()["oracle_path"] and probe.get("replay_path") == scanner_contract()["replay_path"], "D1023 scanner path drift")
    require(probe.get("files") == scanner_contract()["files"], "D1023 scanner file identities drift")
    require(probe.get("counts") == {"tex_files": 119, "labels": 22110, "official_tags_joined": 21437, "topics": 13, "topic_candidates": 1287, "direct_topic_coverage": 13, "warnings": 682, "errors": 0}, "D1023 scanner counts drift")
    require(probe.get("complete_inventory") == {"files": 6, "bytes": 5873083, "surface_bytes": 483, "surface_sha256": "731872A99064E6FD7CEC3110C6AE4C43EDF1D74ECD22AE71025E31AB07652D01"}, "D1023 scanner inventory drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("status") == "AUTHORIZED_FOR_NO_OVERWRITE_R67_TRANSACTION", "D1023 mapping authorization drift")
    require(authorization.get("predecessor") == "tohoku_r66" and authorization.get("successor") == "tohoku_r67", "D1023 authorized lineage drift")
    require(authorization.get("decision") == AUTHORIZED_DECISION, "D1023 authorized decision drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1023 append authorization drift")
    require(authorization.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "D1023 authorized counts drift")
    replacement = authorization.get("map_replacement", {})
    require(replacement.get("physical_line") == 651 and replacement.get("source_locator_preserved") == "sem/r18/nodes.csv:651", "D1023 map replacement locator drift")
    require(set(replacement.get("only_fields_changed", [])) == {"decision_id", "disposition", "review_state", "stacks_labels", "official_tags", "rationale"}, "D1023 authorized changed fields drift")
    require(review.get("schema") == "tohoku-stacks-d1023-independent-review-v1" and review.get("formalization_id") == "D1023", "D1023 review identity drift")
    require(review.get("status") == "STRICT_PASS_FOR_R67_MAPPING" and review.get("errors") == [], "D1023 review state drift")
    require(set(review.get("mathematical_predicates", {}).values()) == {"PASS"}, "D1023 mathematical review drift")
    source_predicates = review.get("source_predicates", {})
    require(source_predicates.get("p174_negative_assertion") == "PASS_EXACT" and source_predicates.get("pp177_179_witness_pattern") == "PASS_FINITE_REALIZATION" and source_predicates.get("citation_scope") == "PASS", "D1023 source review drift")
    recommendation = review.get("mapping_recommendation", {})
    require(recommendation.get("replace_only") == "D000421" and recommendation.get("successor_decision") == "D001047", "D1023 review mapping lineage drift")
    require(recommendation.get("disposition") == "existing_equivalent" and recommendation.get("stacks_labels") == DECISION["stacks_labels"] and recommendation.get("official_tags") == "", "D1023 review label/tag drift")
    require(recommendation.get("review_state") == DECISION["review_state"] and recommendation.get("issue_append") is None and recommendation.get("source_repair_append") is None, "D1023 review append/state drift")
    source_bytes = paths["cohomology_tex"].read_bytes()
    block = b"".join(source_bytes.splitlines(keepends=True)[4464:4597])
    require(identity_from_bytes(block) == (4658, "53D9BD637E14B3079FCB9A5527AAFCBCB2EE5413441B62A34888C52CB90873C1"), "D1023 live block drift")
    raw_label = b"\\label{lemma-cech-cohomology-not-delta-functor}"
    citation = b"\\cite[Chapter III, Section 3.8, pp. 174 and 177--179]{Tohoku}"
    require(source_bytes.count(raw_label) == 1 and block.count(raw_label) == 1, "D1023 raw-label cardinality drift")
    require(source_bytes.count(citation) == 1 and block.count(citation) == 1, "D1023 citation cardinality drift")
    require(paths["bibliography"].read_bytes().count(b"@ARTICLE{Tohoku,") == 1, "Tohoku bibliography key drift")
    require(paths["cohomology_aux"].read_bytes().count(pdf.get("new_label_aux_record", "").encode("utf-8")) == 1, "D1023 aux record drift")
    canonical: dict[str, Any] = {}
    values: dict[str, Any] = {}
    page_bytes: dict[str, bytes] = {}
    for role, spec in CANONICAL_INPUTS.items():
        path, data = read_spec(CANONICAL_ROOT, spec, role)
        canonical[role] = E.record(path, spec[0])
        if spec[0].endswith(".json"):
            values[role] = json.loads(data.decode("utf-8"))
        if role.startswith("p174_"):
            page_bytes[role.removeprefix("p174_")] = data
    require(values["reader_receipt"].get("status") == "PASS" and values["reader_receipt"].get("revision") == "v068c3r20", "reader receipt drift")
    require(values["qa_receipt"].get("status") == "PASS" and values["qa_receipt"].get("qa_revision") == "v68r42", "QA receipt drift")
    require(values["sem_r21_manifest"].get("schema") == "tohoku-semantic-local-successor-manifest-v21", "sem/r21 manifest drift")
    require(values["sem_r21_validation"].get("status") == "PASS", "sem/r21 validation drift")
    semantic_row = (574, "213E758A1B0552B0FED827038A72A6AE449481BF14190CBBC21C081A39116104")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 651) == semantic_row, "sem/r18 D1023 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 651) == semantic_row, "sem/r21 D1023 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/occ.csv", 480) == (520, "F18047D6B60ABA38FB6BE1833E8F8390F8112D0985459406F4CB39A7CD2D2716"), "sem/r18 D1023 occurrence drift")
    segments = {
        "dip": (215, "E58318B505435E68814C6327086BB9EEEDB7B2ED311D61C3E66962389E702AEF"),
        "fr": (215, "E58318B505435E68814C6327086BB9EEEDB7B2ED311D61C3E66962389E702AEF"),
        "en": (190, "F463DB751B57D9FA4FFE4DA13023A6AABB44B5D7AD7C6D69764597AE3C8D310F"),
    }
    for layer, data in page_bytes.items():
        require(identity_from_bytes(layer_segment(data, DECISION["unit_id"])) == segments[layer], f"D1023 {layer} segment drift")
    stacks = {role: E.record(path, bindings[role]["path"]) for role, path in paths.items()}
    return {"execution": execution, "predecessor": predecessor, "stacks": stacks, "canonical": canonical}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == E.ORACLE_PAYLOAD, f"scanner oracle surface drift: {root}")
        require(not any(path.is_dir() for path in root.iterdir()), f"unexpected scanner oracle subdirectory: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "r67 scanner not PASS")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS and len(check.get("warnings", [])) == 682, "r67 scanner count/warning drift")
    require(check.get("tex_sha256", {}).get("cohomology.tex") == EXPECTED_COHOMOLOGY_TEX[1], "r67 scanner TeX binding drift")
    label = "cohomology-lemma-cech-cohomology-not-delta-functor"
    _, rows = E.load_csv(root / "stx.csv")
    row = E.one_row(rows, "full_label", label, "r67 scanner new label")
    require(row["file"] == "cohomology.tex" and row["line"] == "4466" and row["tag"] == "", "r67 scanner label locator/tag drift")
    require(row["text_sha256"] == "1858B2A7DEC8CF48F53582DBA41876D8F0B19A94C5454829EFFACD7D7C558814", "r67 scanner text hash drift")
    require(E.line_identity(root / "stx.csv", 3290) == (272, "B3CC693468DD91727119DFA742AA9B34264CC28F50805EC0B503E803AB97AFCC"), "r67 scanner label row drift")
    _, candidates = E.load_csv(root / "tcand.csv")
    candidate = E.one_row(candidates, "full_label", label, "r67 scanner new candidate")
    require(candidate["topic_id"] == "delta-functor" and candidate["score"] == "92" and candidate["status"] == "lexical_candidate_only", "r67 scanner topic candidate drift")
    require(E.line_identity(root / "tcand.csv", 501) == (452, "42B3115D2E0703263D8AF5E4DF422C26787B53BB2A8008F8D6F7E1E10DE27AAC"), "r67 scanner candidate row drift")
    return check


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink(), "D1023 scanner oracle missing or unsafe")
    require(E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "D1023 scanner replay missing or unsafe")
    verify_scan(E.ORACLE, oracle_surface=True)
    verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1023_scan_probe_r1/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1023_scan_probe_replay_r1/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"missing or unsafe r67 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r67-check.json"} if receipt_mode else set()), "r67 output surface drift")
    require(not any(path.is_dir() for path in root.iterdir()), "unexpected r67 output subdirectory")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r67 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"inherited r67 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r67 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r67 map replacement drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r67 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R66_FILES["ucand.csv"], "r67/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r67 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS and len(mcheck.get("warnings", [])) == 682, "r67 mapping count/warning drift")
    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1048)], "r67 decision sequence drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r67 issue sequence drift")
    require(decisions[-1] == DECISION, "r67 final decision row drift")
    selected = E.one_row(mapping, "unit_id", DECISION["unit_id"], "r67 map")
    require(selected["decision_id"] == "D001047" and selected["disposition"] == "existing_equivalent", "r67 target decision/disposition drift")
    require(selected["review_state"] == DECISION["review_state"] and selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "", "r67 target state/label/tag drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:651", "r67 source locator drift")
    require(E.line_identity(root / "map.csv", 651) == EXPECTED_SUCCESSOR_MAP_ROW, "r67 target map row identity drift")
    deltas = E.map_row_delta()
    require(len(deltas) == 6 and {row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r67 map delta cardinality/scope drift")
    require({row["field"] for row in deltas} == {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"}, "r67 map changed-field set drift")
    remaining = sum(1 for row in mapping if row["disposition"] in {"existing_weaker", "extend_existing", "new_section", "new_statement"})
    require(remaining == 19, "r67 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1047,
        "decisions_appended": ["D001047"],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 682, "errors": 0},
        "remaining_gap_class_dispositions": 19,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 6, "unchanged_units": 990},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1023_ADMITTED_COHOMOLOGY_TEX_AND_PDF_NO_BIBLIOGRAPHY_CHANGE",
        "scanner_payload_change": "D1023_ONE_NEW_COHOMOLOGY_LABEL_AND_TOPIC_CANDIDATE",
    }
    if receipt_mode:
        require(E.strict_json(root / "r67-check.json") == receipt_payload(root, result), "r67 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    stacks = external["stacks"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r67-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": stacks["audit"],
            "independent_review": stacks["review"],
            "bibliography": stacks["bibliography"],
            "live_source": stacks["cohomology_tex"],
            "live_pdf": stacks["cohomology_pdf"],
            "build_support": {key: stacks[key] for key in ("cohomology_aux", "cohomology_bbl", "cohomology_blg", "cohomology_log")},
            "visual_rasters": [stacks[f"page_{page:03d}"] for page in range(43, 49)],
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
            "D001047 closes only the p.174 global-direct-limit-Cech obstruction unit.",
            "Positive paracompact and acyclic-cover comparisons, the separate circle illustration, the longer H1 example, and other degree-two comparisons are not remapped or negated.",
            "No issue, source repair, semantic successor, GAGA comparison, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r66"
    E.TARGET = ROOT / "tohoku_r67"
    E.STAGE = ROOT / ".tohoku-r67-txn"
    E.ORACLE = ROOT / "tmp" / "d1023_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1023_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R66_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R66_FILES
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r67 target or stage already exists")
    print(json.dumps({
        "schema": "tohoku-r67-scanner-oracle-v1",
        "status": "PASS_REPLAY",
        "errors": [],
        "scanner_oracles": verify_oracles(),
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 682, "errors": 0},
    }, indent=2, sort_keys=True))


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r67 target or stage already exists")
    external = verify_external()
    oracles = verify_oracles()
    projection = {
        "cfg.json": identity_from_bytes(expected_cfg_bytes()),
        "dec.csv": identity_from_bytes(expected_decision_bytes()),
        "issues.csv": identity_from_bytes(expected_issue_bytes()),
        "map.csv": identity_from_bytes(expected_map_bytes()),
        "STATUS.md": identity_from_bytes(STATUS_BYTES),
    }
    print(json.dumps({
        "schema": "tohoku-r67-static-input-audit-v1",
        "status": "PASS",
        "errors": [],
        "external": external,
        "scanner_oracles": oracles,
        "projection": projection,
        "decision": "D001047",
        "issue": None,
        "source_repair": None,
        "remaining_gaps": 19,
    }, indent=2, sort_keys=True))


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r67 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    E.exclusive_write(E.STAGE / "r67-check.json", E.json_bytes(receipt_payload(E.STAGE, deltas)))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r67 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("post-promotion r67 replay failed; target rolled back") from exc
    print(json.dumps({
        "schema": "tohoku-r67-transaction-result-v1",
        "status": "PASS_COMMITTED",
        "errors": [],
        "target": "tohoku_r67",
        "receipt": E.record(E.TARGET / "r67-check.json"),
        "remaining_gaps": 19,
    }, indent=2, sort_keys=True))


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink(), "r67 target missing or unsafe")
    require(not E.STAGE.exists(), "r67 stage unexpectedly exists")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(json.dumps({
        "schema": "tohoku-r67-replay-v1",
        "status": "PASS_REPLAY",
        "errors": [],
        "receipt": E.record(E.TARGET / "r67-check.json"),
        "deltas": result,
    }, indent=2, sort_keys=True))


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
