#!/usr/bin/env python3
"""Build and seal the audited D1022/r66 mapping successor."""

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
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r65.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r66_contract.json"
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

ENGINE_IDENTITY = (40617, "A51A8FDC8BBD4EE4493423B8912482C5D8812BF8CD56C277008F2B78FE2ECF0A")
CONTRACT_ID = "D1022-r66-D001046-v1"
EXPECTED_R65_RECEIPT = (9903, "64DC0F64E5C076917C6306B7EB8124C014AA14A336206672683851879F560CD6")
EXPECTED_R65_FILES = {
    "STATUS.md": (1186, "8E4B988509685DE0CF62AB914EA2CD896A91AF6F251CFD4A457791E8533A5F92"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83022, "CA4BD4D6C25E995CF422795472D17E039CBD260F1D17B16915DF5245B4CB272E"),
    "dec.csv": (387550, "FA8E7CB9875CD48EE12CD1F71BBF02A3E49CEC59AC84B0C2D632F0AD57C82988"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (486207, "3EE354983BE9A38A36E921E26E3966B9022DE3F29516AAC968A0AD0F16090936"),
    "mcheck.json": (72849, "AECBF4C4A6053E69981388F2F4E555BBD2B2BD48DECE38AD1686905149E1EBAC"),
    "stx.csv": (5288663, "01C9089B9AF31597C7FD787C37D31C7FCB5A052DED324EDB3648FEEAC083DAEC"),
    "tcand.csv": (489256, "73C6BFD919058171C14E2CDEC94F47DDBFF389636BDA7250BE4B6BBE7BC29357"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83391, "EEE21BF2A81BBD214CF7BC6F8968500229CD00DA19D46EC9EC0C7B70A62A1BDB"),
    "stx.csv": (5289572, "0B1FA83BF876F2C0A508E7E6EE5721E986A105481738143F59AAEB2611F9ECBD"),
    "tcand.csv": (489256, "794FAB6C0346B7A6698E0936348B81310885E092EEC8E33142DDF6301FFCA83E"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22109,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1286,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_PROJECTED = {
    "dec.csv": (388554, "63C36B2277BB5F783A691F70A038F08052CCA4B241B8577F72CD09D9C8DCE431"),
    "issues.csv": EXPECTED_R65_FILES["issues.csv"],
    "map.csv": (486832, "11D626A8F99DC5FD529B3C4CBE31BBDD433EDD8B5DBB84182647037EFCE67765"),
}
EXPECTED_DECISION_APPEND = (1004, "9BD521ECE4BF6D3D1FA5238380719C43C3FEFE6FACDF8AA1DF57889106DC24CC")
EXPECTED_PREDECESSOR_MAP_ROW = (608, "458DE83AF4821C29C07DB5183FA803CE8926232B2775DB848E3C39D77A2D2266")
EXPECTED_SUCCESSOR_MAP_ROW = (1233, "5DD1A5211F0708B9CC8B4F1AA92F0AF6788EDE9ACAC06F7837EF199F72D7D282")
EXPECTED_AUDIT = (16535, "C73D272C6DF4A9DD2D7B5A51998F97287FC2B5651C62EF91F15C05494A85ED6F")
EXPECTED_COHOMOLOGY_TEX = (934533, "1C801DC6DF9AA5944FEBC6E17A2B16AE2CF297932135FEAE8CF3CB7701A6BCCD")
EXPECTED_BIBLIOGRAPHY = (220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE")
EXPECTED_COHOMOLOGY_PDF = (2031205, "3B909EB03D9B8785A4428472561BE8D075B0A27A8E0D2785A90A8F411BBD2082")

DECISION = {
    "decision_id": "D001046",
    "unit_id": "tohoku:finiteness:compact-quotient-extension-classes",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-compact-analytic-quotient-equivariant-ext-finite-dimensional",
    "rationale": "Stacks now proves finite-dimensional cohomology for coherent analytic sheaves on compact complex analytic spaces and coherence of ordinary analytic sheaf Ext in every degree. For a discontinuous analytic action with compact quotient, finite stabilizer cohomology collapses equivariant sheaf Ext to coherent invariant direct image, and spectral sequence I makes every Ext^n_{O,G}(X;A,B) finite-dimensional. The analytic bundle/module equivalence and finite-locally-free extension-class lemma then identify equivariant holomorphic bundle extensions of E by F with the corresponding finite-dimensional Ext^1 and H^1(Y,q_*^G O(E^vee tensor F)). The following algebraic analogue, noncompact cases, global properness of q, Ext vanishing, moduli, algebraization, and GAGA are excluded.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000617",
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
    "decisions": 1046,
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
        "existing_equivalent": 389,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 2,
        "structural_only": 424,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1046,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 389,
    "new_statement": 2,
    "remaining_gap_class_dispositions": 20,
    "source_repairs_appended": 0,
    "mapping_closures": 1,
    "changed_map_rows": 1,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r65 dossier is preserved exactly; D001046 closes the p.219 compact-quotient equivariant-extension finiteness unit in a no-overwrite r66 successor.\n"
    "- The admitted D1022 source proves finite-dimensional coherent analytic cohomology on compact spaces, coherence of analytic sheaf Ext in every fixed degree, and finite-dimensional equivariant Ext over a compact discontinuous quotient.\n"
    "- The D1022 audit, design, candidate, independent review, live TeX/PDF build, supporting build files, visual rasters, source evidence, and scanner oracle/replay are bound byte-exactly.\n"
    "- No issue or source-repair row is appended; only the authorized D000617 map row is replaced.\n"
    "- The scanner indexes 119 top-level TeX files with 22,109 labels, 681 warnings, and no errors.\n"
    "- There are 1,046 decisions, 679 decided units, 32 resolved source issues, and 20 gap-class dispositions remain.\n"
    "- GitHub availability was restored by direct user update; this bounded local transaction requires no Git or GitHub operation.\n"
    "- No claim is made for the following algebraic analogue, noncompact cases, global properness, Ext vanishing, moduli, algebraization, GAGA, release, publication, DOI, remote freshness, rights, or whole-paper completion.\n"
).encode("utf-8")

ROOT_BINDINGS = {
    "audit": ("D1022_CHECK.json", 16535, "C73D272C6DF4A9DD2D7B5A51998F97287FC2B5651C62EF91F15C05494A85ED6F"),
    "design": ("tmp/d1022_compact_quotient_ext_finiteness_design.json", 8952, "7C69F1BF1EC0EC010F08FA474646B4EC32D247C2FF339FE0A2C3E0E6A06F533B"),
    "candidate": ("tmp/d1022_compact_quotient_ext_finiteness_candidate.tex", 7182, "588852F97DE8FA516791E264A37EB2C77BC7D1E07BB0CF1DC4382A9CEC293D26"),
    "review": ("tmp/d1022_independent_review_r1.json", 3509, "6E97F331C0CEA8B5E264ECA65ACDD673DF81FD4D28EF8BC7B97281B7825572B3"),
    "cohomology_tex": ("cohomology.tex", 934533, "1C801DC6DF9AA5944FEBC6E17A2B16AE2CF297932135FEAE8CF3CB7701A6BCCD"),
    "bibliography": ("my.bib", 220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE"),
    "cohomology_pdf": ("cohomology.pdf", 2031205, "3B909EB03D9B8785A4428472561BE8D075B0A27A8E0D2785A90A8F411BBD2082"),
    "cohomology_aux": ("cohomology.aux", 58342, "30F44117D3DF2B0D4C3BF4526F79EAB3C6BB73CF70091DDE143E691E9940BF5C"),
    "cohomology_bbl": ("cohomology.bbl", 2313, "B549EC2BF6A2D441ABC2587AEB0D81AAB800C65A0F4461EC39573EACB228034A"),
    "cohomology_blg": ("cohomology.blg", 1037, "AD428028D6914435597B90AC92610E926BBA25B968AC3102678A58B633397428"),
    "cohomology_log": ("cohomology.log", 48450, "63068B84D495AE101CE38C27EDA89C94E56EC6348C6F46B698DF76D80AA84484"),
    "page_197": ("tmp/d1022_pdf_qa/page-197.png", 280729, "196485DBB2BE97E7D63642A776D012A1BEFF1154B2860FB3E37FCE2BB8479CA0"),
    "page_198": ("tmp/d1022_pdf_qa/page-198.png", 282615, "1FEC1B60367905644AA2DD12D3AE2D47CA2B04A93DCB8EC9FB7C546D83EEA71A"),
    "page_199": ("tmp/d1022_pdf_qa/page-199.png", 294684, "53DFAFD493F7732494958A1DCB2584B8C91BAD41BFA82BDF0CF300D77D0C404A"),
    "page_200": ("tmp/d1022_pdf_qa/page-200.png", 287674, "D0D6ABCB6AAB4C3198CDF7864F7DA2EB3782288AC9B170A72BA0F213E96FD75E"),
    "page_201": ("tmp/d1022_pdf_qa/page-201.png", 268507, "6D8239CEF5A3929E435B1A5A0F388E06EAA4496882AE6B89AB9C9738F43AB87A"),
    "page_202": ("tmp/d1022_pdf_qa/page-202.png", 271099, "C3B6857145463BD034F743308FA369E2164BB76C13BF34CEF4E3EC35CFAEEA37"),
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
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r65 transaction engine identity drift")
    module = types.ModuleType("tohoku_r66_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r65 transaction engine changed during load")
    return module


M = load_engine()
E = M.E
CANONICAL_INPUTS = M.CANONICAL_INPUTS


def contract_bindings() -> dict[str, Any]:
    return {
        role: {"path": spec[0], "bytes": spec[1], "sha256": spec[2]}
        for role, spec in ROOT_BINDINGS.items()
    }


def scanner_contract() -> dict[str, Any]:
    return {
        "oracle_path": "tmp/d1022_scan_probe_r1",
        "replay_path": "tmp/d1022_scan_probe_replay_r1",
        "files": {
            name: {"bytes": expected[0], "sha256": expected[1]}
            for name, expected in EXPECTED_SCAN.items()
        },
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 681, "errors": 0},
    }


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r66 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r66-transaction-contract-v1", "r66 contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "r66 contract ID mismatch")
    script = contract.get("script")
    require(isinstance(script, dict) and script.get("path") == "srcmap/build_tohoku_r66.py", "r66 script pin missing")
    require(identity_from_bytes(SCRIPT_PATH.read_bytes()) == (script.get("bytes"), script.get("sha256")), "r66 script identity mismatch")
    engine = contract.get("engine")
    require(isinstance(engine, dict) and engine.get("path") == "srcmap/build_tohoku_r65.py", "r66 engine path mismatch")
    require((engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r66 engine identity mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r65/r65-check.json", "bytes": EXPECTED_R65_RECEIPT[0], "sha256": EXPECTED_R65_RECEIPT[1]}, "r66 predecessor contract mismatch")
    require(contract.get("frozen_prerequisite") == contract_bindings()["audit"], "r66 frozen prerequisite mismatch")
    require(contract.get("bound_inputs") == contract_bindings(), "r66 bound-input contract mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r66 scanner contract mismatch")
    require(contract.get("decision") == AUTHORIZED_DECISION, "r66 decision contract mismatch")
    require(contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r66 projected counts mismatch")
    require(contract.get("target") == "tohoku_r66", "r66 target mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r65" and transaction.get("stage") == ".tohoku-r66-txn", "r66 transaction paths mismatch")
    require(transaction.get("no_overwrite") is True and transaction.get("atomic_directory_rename") is True and transaction.get("post_promotion_replay") is True, "r66 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r66.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r66_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r65.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    cfg = json.loads(data.decode("utf-8"))
    require(cfg.get("dossier_id") == "tohoku_r62", "inherited cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "inherited r66 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1045, "r65 decision schema/count drift")
    require(rows[-1]["decision_id"] == "D001045", "r65 decision tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, [DECISION], header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001046 append row drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "projected r66 decision bytes drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "inherited r66 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r65 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r65 map schema/count drift")
    selected = E.one_row(rows, "unit_id", DECISION["unit_id"], "r65 map")
    require(selected["decision_id"] == "D000617" and selected["disposition"] == "new_statement", "r65 D1022 target state drift")
    require(selected["review_state"] == "reviewed_new_statement", "r65 D1022 review state drift")
    require(selected["stacks_labels"] == "homology-definition-ext-group;stacks-cohomology-lemma-extension-coherent", "r65 D1022 predecessor labels drift")
    require(selected["stacks_tags"] == "010K;0GRA", "r65 D1022 predecessor tags drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:590", "r65 D1022 source locator drift")
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
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "projected r66 map bytes drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r65-check.json"
    E.require_identity(receipt, EXPECTED_R65_RECEIPT, "r65 receipt")
    for name, expected in EXPECTED_R65_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r65/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r65-v1", "r65 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r65 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 21, "r65 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R65_FILES), "r65 receipt inventory drift")
    replay = {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records}
    require(replay == EXPECTED_R65_FILES, "r65 receipt file identities drift")
    require(E.line_identity(E.SOURCE / "map.csv", 590) == EXPECTED_PREDECESSOR_MAP_ROW, "r65 target map row drift")
    return {"receipt": E.record(receipt, "tohoku_r65/r65-check.json")}


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
        E.require_identity(path, (spec["bytes"], spec["sha256"]), f"D1022 {role}")

    audit = E.strict_json(paths["audit"])
    design = E.strict_json(paths["design"])
    review = E.strict_json(paths["review"])
    require(audit.get("schema") == "tohoku-stacks-d1022-check-v1" and audit.get("formalization_id") == "D1022", "D1022 audit identity drift")
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R66_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1022 audit state drift")
    selection = audit.get("selection", {})
    require(selection.get("unit") == DECISION["unit_id"] and selection.get("source_locator") == "sem/r18/nodes.csv:590", "D1022 selection drift")
    require(selection.get("predecessor_decision") == "D000617" and selection.get("predecessor_dossier") == "tohoku_r65", "D1022 predecessor selection drift")
    require(selection.get("predecessor_map_row_with_lf") == {"physical_line": 590, "bytes": EXPECTED_PREDECESSOR_MAP_ROW[0], "sha256": EXPECTED_PREDECESSOR_MAP_ROW[1]}, "D1022 predecessor row binding drift")
    require(audit.get("source_claim", {}).get("source_repair_required") is False and audit.get("source_claim", {}).get("transcription_or_translation_repair_required") is False, "D1022 unexpected source repair")
    require(audit.get("design", {}).get("path") == ROOT_BINDINGS["design"][0] and (audit.get("design", {}).get("bytes"), audit.get("design", {}).get("sha256")) == ROOT_BINDINGS["design"][1:], "D1022 design binding drift")
    require(audit.get("candidate", {}).get("path") == ROOT_BINDINGS["candidate"][0] and (audit.get("candidate", {}).get("bytes"), audit.get("candidate", {}).get("sha256")) == ROOT_BINDINGS["candidate"][1:], "D1022 candidate binding drift")
    require(audit.get("independent_review", {}).get("path") == ROOT_BINDINGS["review"][0] and (audit.get("independent_review", {}).get("bytes"), audit.get("independent_review", {}).get("sha256")) == ROOT_BINDINGS["review"][1:], "D1022 review binding drift")
    require(audit.get("independent_review", {}).get("status") == "STRICT_PASS_FOR_LIVE_INSERTION_AND_BUILD", "D1022 review status drift")
    edit = audit.get("stacks_edit", {})
    require((edit.get("postimage", {}).get("bytes"), edit.get("postimage", {}).get("sha256")) == EXPECTED_COHOMOLOGY_TEX, "D1022 live TeX evidence drift")
    require(edit.get("candidate_block_occurrences") == 1 and edit.get("unrelated_live_source_files_changed_by_insertion") == 0, "D1022 insertion cardinality drift")
    expected_labels = [
        ("lemma-compact-complex-analytic-coherent-cohomology-finite-dimensional", 20476),
        ("lemma-coherent-analytic-sheaf-ext", 20501),
        ("lemma-compact-analytic-quotient-equivariant-ext-finite-dimensional", 20531),
    ]
    require([(row.get("label"), row.get("line")) for row in edit.get("new_raw_labels", [])] == expected_labels, "D1022 audit raw-label sequence drift")
    require(all(row.get("occurrences") == 1 for row in edit.get("new_raw_labels", [])), "D1022 audit raw-label count drift")
    pdf = audit.get("pdf_build", {})
    require((pdf.get("postimage", {}).get("bytes"), pdf.get("postimage", {}).get("sha256")) == EXPECTED_COHOMOLOGY_PDF, "D1022 live PDF evidence drift")
    require(pdf.get("postimage", {}).get("pages") == 244 and pdf.get("final_driver_exit_code") == 0, "D1022 PDF build gate drift")
    require(all(value == 0 for value in pdf.get("diagnostics", {}).values()), "D1022 PDF diagnostic drift")
    support_roles = {"aux": "cohomology_aux", "bbl": "cohomology_bbl", "blg": "cohomology_blg", "log": "cohomology_log"}
    for key, role in support_roles.items():
        value = pdf.get("supporting_files", {}).get(key, {})
        require((value.get("bytes"), value.get("sha256")) == ROOT_BINDINGS[role][1:], f"D1022 {key} audit binding drift")
    visual = audit.get("visual_qa", {})
    require(visual.get("status") == "STRICT_PASS_INDEPENDENTLY_CONFIRMED" and visual.get("defects") == [], "D1022 visual QA drift")
    require(visual.get("inspected_pdf_pages") == [197, 198, 199, 200, 201, 202], "D1022 visual page set drift")
    for row, page in zip(visual.get("rasters", []), range(197, 203)):
        role = f"page_{page}"
        require(row.get("path") == ROOT_BINDINGS[role][0] and (row.get("bytes"), row.get("sha256")) == ROOT_BINDINGS[role][1:], f"D1022 page {page} raster binding drift")
    probe = audit.get("scanner_probe", {})
    require(probe.get("status") == "PASS_BYTE_IDENTICAL_REPLAY" and probe.get("oracle_path") == scanner_contract()["oracle_path"] and probe.get("replay_path") == scanner_contract()["replay_path"], "D1022 scanner audit state drift")
    require(probe.get("counts") == {"tex_files": 119, "labels": 22109, "official_tags_joined": 21437, "topics": 13, "topic_candidates": 1286, "direct_topic_coverage": 13, "warnings": 681, "errors": 0}, "D1022 scanner audit counts drift")
    require(probe.get("files") == scanner_contract()["files"], "D1022 scanner audit file identities drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("status") == "AUTHORIZED_FOR_NO_OVERWRITE_R66_TRANSACTION", "D1022 mapping authorization drift")
    require(authorization.get("predecessor") == "tohoku_r65" and authorization.get("successor") == "tohoku_r66", "D1022 authorized lineage drift")
    require(authorization.get("decision") == AUTHORIZED_DECISION, "D1022 authorized decision drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1022 append authorization drift")
    require(authorization.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "D1022 authorized counts drift")
    replacement = authorization.get("map_replacement", {})
    require(replacement.get("physical_line") == 590 and replacement.get("source_locator_preserved") == "sem/r18/nodes.csv:590", "D1022 map replacement locator drift")
    require(set(replacement.get("only_fields_changed", [])) == {"decision_id", "disposition", "review_state", "stacks_labels", "official_tags", "rationale"}, "D1022 authorized changed fields drift")

    require(design.get("schema") == "tohoku-d1022-compact-quotient-ext-finiteness-design-v1", "D1022 design schema drift")
    require(design.get("status") == "DRAFT_READY_FOR_INDEPENDENT_REVIEW" and design.get("errors") == [], "D1022 design state drift")
    require(design.get("formalization", {}).get("id") == "D1022" and design.get("formalization", {}).get("unit") == DECISION["unit_id"], "D1022 design target drift")
    projection = design.get("conditional_mapping_projection", {})
    design_decision_keys = (
        "decision_id",
        "unit_id",
        "action",
        "disposition",
        "stacks_labels",
        "official_tags",
        "review_state",
        "supersedes",
    )
    require(
        {key: projection.get(key) for key in design_decision_keys}
        == {key: AUTHORIZED_DECISION[key] for key in design_decision_keys},
        "D1022 design decision projection drift",
    )
    require(projection.get("predecessor") == "tohoku_r65" and projection.get("successor") == "tohoku_r66", "D1022 design lineage drift")
    require(projection.get("issue_append") is None and projection.get("source_repair_append") is None, "D1022 design append drift")
    require(review.get("schema") == "tohoku-d1022-independent-review-v1", "D1022 review schema drift")
    require(review.get("formalization_id") == "D1022" and review.get("primary_unit") == DECISION["unit_id"], "D1022 review target drift")
    require(review.get("status") == "STRICT_PASS_FOR_LIVE_INSERTION_AND_BUILD" and review.get("errors") == [], "D1022 review state drift")
    require(review.get("source_review", {}).get("verdict") == "PASS" and review.get("source_review", {}).get("revised_design_recheck") == "PASS", "D1022 source review drift")
    require(review.get("mathematical_review", {}).get("verdict") == "PASS", "D1022 mathematical review drift")
    require(review.get("predicate_summary") == {"total": 13, "passed": 13, "failed": 0}, "D1022 predicate count drift")

    source_bytes = paths["cohomology_tex"].read_bytes()
    candidate_bytes = paths["candidate"].read_bytes()
    require(source_bytes.count(candidate_bytes) == 1, "D1022 candidate block not present exactly once")
    for raw, _ in expected_labels:
        require(source_bytes.count(f"\\label{{{raw}}}".encode("utf-8")) == 1, f"D1022 live raw-label count drift: {raw}")
    require(paths["bibliography"].read_bytes().count(b"@ARTICLE{Grauert-direct-image,") == 1, "Grauert bibliography key drift")
    aux_bytes = paths["cohomology_aux"].read_bytes()
    for record in pdf.get("new_label_aux_records", []):
        require(aux_bytes.count(record.encode("utf-8")) == 1, "D1022 aux label record drift")
    require(aux_bytes.count(pdf.get("following_aux_record", "").encode("utf-8")) == 1, "D1022 following aux record drift")

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
    semantic_row = (884, "F6CE83C5D2CCE09E88C38E452412C1A47A7918139E5002D7E1F429BFEF941EBA")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 590) == semantic_row, "sem/r18 D1022 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 590) == semantic_row, "sem/r21 D1022 row drift")
    require(E.line_identity(CANONICAL_ROOT / "sem/r18/occ.csv", 989) == (544, "ED859ED739F74DC83CC74DB374AE45E6B8A135E08CD7A05CA557F7C2D03F022F"), "sem/r18 D1022 occurrence drift")
    segments = {
        "dip": (394, "D95FEF98E467F1E2609142A9F93A6B1EED2111816F8DBDBCC33C501FB0CA56C1"),
        "fr": (393, "86F781806E2410850450B213A02E67F22E6E4765F92D2DE4790E2B1CA2C5B2B8"),
        "en": (389, "50DBA2527159209849CCC0168559EA6133A1F3E903BA1CAFC95256E2C7702D62"),
    }
    for layer, data in page_bytes.items():
        require(identity_from_bytes(layer_segment(data, DECISION["unit_id"])) == segments[layer], f"D1022 {layer} segment drift")
    raster_specs = {
        "authority_raster": ("production/p219_r1/qa/src.png", 5928647, "1B518A5A872E6145F512CCD14CADC31E2D0B075E5AD51DA271ABAC8CC6DCE330"),
        "focused_crop": ("production/p219_r1/qa/hi05_compact_5000.png", 361849, "EF0E7FEB8A9615669623BAD271810DB5ACCCD574A20523B9052B6B604F462827"),
    }
    for role, spec in raster_specs.items():
        path, _ = read_spec(CANONICAL_ROOT, spec, role)
        canonical[role] = E.record(path, spec[0])
    stacks = {role: E.record(path, bindings[role]["path"]) for role, path in paths.items()}
    return {"execution": execution, "predecessor": predecessor, "stacks": stacks, "canonical": canonical}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == E.ORACLE_PAYLOAD, f"scanner oracle surface drift: {root}")
        require(not any(path.is_dir() for path in root.iterdir()), f"unexpected scanner oracle subdirectory: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "r66 scanner not PASS")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r66 scanner count drift")
    require(len(check.get("warnings", [])) == 681, "r66 scanner warning count drift")
    require(check.get("tex_sha256", {}).get("cohomology.tex") == EXPECTED_COHOMOLOGY_TEX[1], "r66 scanner cohomology.tex binding drift")
    _, rows = E.load_csv(root / "stx.csv")
    expected_rows = {
        "cohomology-lemma-compact-complex-analytic-coherent-cohomology-finite-dimensional": (3632, "20476", 329, "52C2B6D86AFC4DFB36A2C9F44B2D90F726BB8E2F32413AA0C7FF001534B64996", "9EC53621CDE0FCF2956B654257769959DEB598CE3B5235171DFB868C9C0480F7"),
        "cohomology-lemma-coherent-analytic-sheaf-ext": (3633, "20501", 257, "522C1AA70EF10B7CD8CAC265EE338CC83E79307899683471BACC1B8C735E4571", "E26BA2AC94ACEE5A6EE2DC395E9E647E80995EDA2DF477B74CD292C965141F7C"),
        "cohomology-lemma-compact-analytic-quotient-equivariant-ext-finite-dimensional": (3634, "20531", 323, "E9029E5827DB95F19C7F6A1FEA4028FC10C6D920A018B5E883DF7D6053B58248", "8591C9C0BA969B92089DF7D2C3DB88D87EF0AFE2B7FBE5152BC6F6AADDBF2175"),
    }
    for label, (physical, line, row_bytes, row_hash, text_hash) in expected_rows.items():
        row = E.one_row(rows, "full_label", label, f"r66 scanner {label}")
        require(row["file"] == "cohomology.tex" and row["line"] == line and row["tag"] == "", f"r66 scanner row drift: {label}")
        require(row["text_sha256"] == text_hash, f"r66 scanner text drift: {label}")
        require(E.line_identity(root / "stx.csv", physical) == (row_bytes, row_hash), f"r66 scanner row identity drift: {label}")
    return check


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink(), "D1022 scanner oracle missing or unsafe")
    require(E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "D1022 scanner replay missing or unsafe")
    verify_scan(E.ORACLE, oracle_surface=True)
    verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1022_scan_probe_r1/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1022_scan_probe_replay_r1/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"missing or unsafe r66 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r66-check.json"} if receipt_mode else set()), "r66 output surface drift")
    require(not any(path.is_dir() for path in root.iterdir()), "unexpected r66 output subdirectory")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r66 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"inherited r66 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r66 decision append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r66 map replacement drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r66 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R65_FILES["ucand.csv"], "r66/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r66 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r66 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 681, "r66 warning propagation drift")
    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1047)], "r66 decision sequence drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r66 issue sequence drift")
    require(decisions[-1] == DECISION, "r66 final decision row drift")
    selected = E.one_row(mapping, "unit_id", DECISION["unit_id"], "r66 map")
    require(selected["decision_id"] == "D001046" and selected["disposition"] == "existing_equivalent", "r66 target decision/disposition drift")
    require(selected["review_state"] == DECISION["review_state"], "r66 target review state drift")
    require(selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "", "r66 target label/tag drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:590", "r66 source locator drift")
    require(E.line_identity(root / "map.csv", 590) == EXPECTED_SUCCESSOR_MAP_ROW, "r66 target map row identity drift")
    deltas = E.map_row_delta()
    require(len(deltas) == 6 and {row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r66 map delta cardinality/scope drift")
    require({row["field"] for row in deltas} == {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"}, "r66 map changed-field set drift")
    gap_dispositions = {"existing_weaker", "extend_existing", "new_section", "new_statement"}
    remaining = sum(1 for row in mapping if row["disposition"] in gap_dispositions)
    require(remaining == 20, "r66 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1046,
        "decisions_appended": ["D001046"],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 681, "errors": 0},
        "remaining_gap_class_dispositions": 20,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 6, "unchanged_units": 990},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1022_ADMITTED_COHOMOLOGY_TEX_AND_PDF_NO_BIBLIOGRAPHY_CHANGE",
        "scanner_payload_change": "D1022_THREE_NEW_COHOMOLOGY_LABELS",
    }
    if receipt_mode:
        receipt = E.strict_json(root / "r66-check.json")
        require(receipt == receipt_payload(root, result), "r66 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    stacks = external["stacks"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r66-v1",
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
            "live_source": stacks["cohomology_tex"],
            "live_pdf": stacks["cohomology_pdf"],
            "build_support": {key: stacks[key] for key in ("cohomology_aux", "cohomology_bbl", "cohomology_blg", "cohomology_log")},
            "visual_rasters": [stacks[f"page_{page}"] for page in range(197, 203)],
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
            "authority_raster": external["canonical"]["authority_raster"],
            "focused_crop": external["canonical"]["focused_crop"],
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
            "D001046 closes only the p.219 compact-quotient equivariant-extension finiteness unit.",
            "The following algebraic analogue, noncompact cases, global properness of q, Ext vanishing, finite projective dimension, moduli, algebraization, and GAGA remain separate or excluded.",
            "No issue, source repair, semantic successor, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r65"
    E.TARGET = ROOT / "tohoku_r66"
    E.STAGE = ROOT / ".tohoku-r66-txn"
    E.ORACLE = ROOT / "tmp" / "d1022_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1022_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R65_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R65_FILES
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r66 target or stage already exists")
    oracles = verify_oracles()
    print(json.dumps({
        "schema": "tohoku-r66-scanner-oracle-v1",
        "status": "PASS_REPLAY",
        "errors": [],
        "scanner_oracles": oracles,
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 681, "errors": 0},
    }, indent=2, sort_keys=True))


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r66 target or stage already exists")
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
        "schema": "tohoku-r66-static-input-audit-v1",
        "status": "PASS",
        "errors": [],
        "external": external,
        "scanner_oracles": oracles,
        "projection": projection,
        "decision": "D001046",
        "issue": None,
        "source_repair": None,
        "remaining_gaps": 20,
    }, indent=2, sort_keys=True))


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r66 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    receipt = receipt_payload(E.STAGE, deltas)
    E.exclusive_write(E.STAGE / "r66-check.json", E.json_bytes(receipt))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r66 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("post-promotion r66 replay failed; target rolled back") from exc
    print(json.dumps({
        "schema": "tohoku-r66-transaction-result-v1",
        "status": "PASS_COMMITTED",
        "errors": [],
        "target": "tohoku_r66",
        "receipt": E.record(E.TARGET / "r66-check.json"),
        "remaining_gaps": 20,
    }, indent=2, sort_keys=True))


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink(), "r66 target missing or unsafe")
    require(not E.STAGE.exists(), "r66 stage unexpectedly exists")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(json.dumps({
        "schema": "tohoku-r66-replay-v1",
        "status": "PASS_REPLAY",
        "errors": [],
        "receipt": E.record(E.TARGET / "r66-check.json"),
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
