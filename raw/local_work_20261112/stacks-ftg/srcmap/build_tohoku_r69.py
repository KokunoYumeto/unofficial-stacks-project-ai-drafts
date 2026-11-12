#!/usr/bin/env python3
"""Build and seal the audited bundled D1025-D1027/r69 mapping successor."""

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
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r68.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r69_contract.json"
CANONICAL_ROOT = (
    ROOT.parent
    / "interlanguage"
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "03_working_translations"
    / "tohoku_bilingual_canonical_stacks_20260804_r1"
)

ENGINE_IDENTITY = (42291, "38B0A5999438B51BAA0C85B4B14F5393DB17BC26C9D36937E5DF1874FA7049AB")
CONTRACT_ID = "D1025-D1026-D1027-r69-D001049-D001051-v1"
EXPECTED_R68_RECEIPT = (11900, "1FD05FEBBDF081DEF558736D34FDC78846EE5F34F9E5730CE1D34E19B91C671B")
EXPECTED_R68_FILES = {
    "STATUS.md": (1082, "5147C0513C60030BB55D610950A29CE4096402A2C32C2EDE99C54B101E9A69E0"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83599, "ED5922F42855AB0D7615B7BDB5FC30A91338E5F321F4E25B1D8664387A69D775"),
    "dec.csv": (390012, "0532BAB5CD37951A0885E841EF4881CBAF6A6F8C4C010F2289AFA1A03BB1DBC6"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (487490, "1EDF4CFB722D6EFFC601FA64E1EB3E801BF2C63D8CC973B6467FA68C647E5ED2"),
    "mcheck.json": (73425, "C3E0B79D213EE748519E36ADB551B9168B03E3B4858F5ADF08267991AD890BC0"),
    "stx.csv": (5290078, "485B3A4687F56842E778833D87ADA152A0CD10116F7144A7C9AE7F6F6931399D"),
    "tcand.csv": (489711, "2F3C060F11449AC76848A7810F8B0742291C9784A3561CA7FC245721164A59A5"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83727, "C65DA64B135E1A17179F8DED6880226DE9ECEA62E149B00C8FEE79CB354F343E"),
    "stx.csv": (5290391, "3083041A38A704D6A8815B21D42AC8E617AFA8D404B289586A820D1C80AE3346"),
    "tcand.csv": (489720, "69156C767922272E47416C2471DD2EC5B9A905B4E1964B56806145892A7FECC9"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22112,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1287,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_INVENTORY = {
    "files": 6,
    "bytes": 5873866,
    "surface_bytes": 483,
    "surface_sha256": "98CA0B13CC826020BF5A631A8E4B358758202D779649C334B7AA017DACBD2CF2",
}
EXPECTED_PROJECTED = {
    "dec.csv": (391385, "E7AA26C9073717E418FCB2BC0ADC20E1AE89762BEF55D69C260A0BE3909FD837"),
    "issues.csv": EXPECTED_R68_FILES["issues.csv"],
    "map.csv": (487554, "0427AEA97444BC58E7C3823B91FDFCD84CC531DAB4D6C93F38C8EE9D52BB3A00"),
}
EXPECTED_DECISION_APPEND = (1373, "71F0B6DCAB0A56D68495C60DAC5EE034352EBAF9D017629EBD4C6667265A4142")

DECISIONS = [
    {
        "decision_id": "D001049",
        "unit_id": "tohoku:term:category",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "categories-definition-category;categories-remark-category-convention-boundary",
        "rationale": "The derived category term is fully represented by the Stacks category definition together with the source-specific convention-boundary remark; the admitted p. 122 body coordinate supplies the exact source content and no additional live statement is needed.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000003",
    },
    {
        "decision_id": "D001050",
        "unit_id": "tohoku:section:1.1:p3",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "categories-definition-mono-epi;categories-lemma-mono-epi-composition",
        "rationale": "The definition supplies the source cancellation conditions, while the revised bounded history records injective, surjective, and bijective as the source's terminology with explicit guards against underlying-set and balanced-category overclaims.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000072",
    },
    {
        "decision_id": "D001051",
        "unit_id": "tohoku:classification:equivariant-bundle-extensions",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-equivariant-holomorphic-vector-bundle-extension-classes",
        "rationale": "The new lemma proves that the equivariant holomorphic bundle-module equivalence identifies fixed-endpoint bundle extensions with Yoneda Ext^1, preserves Baer sum, and then applies the locally-free edge isomorphism and evaluation to obtain exactly H^1(X;G,O(E^dual tensor F)).",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D001037",
    },
]
OFFICIAL_TAGS = {"D001049": "0014", "D001050": "003B", "D001051": ""}
AUTHORIZED_DECISIONS = [{**decision, "official_tags": OFFICIAL_TAGS[decision["decision_id"]]} for decision in DECISIONS]

MAP_SPECS = {
    "tohoku:term:category": {
        "physical_line": 5,
        "source_loc": "sem/r18/nodes.csv:5",
        "predecessor_decision": "D000003",
        "predecessor_disposition": "extend_existing",
        "predecessor_review": "reviewed_gap",
        "predecessor_labels": "categories-definition-category",
        "tag": "0014",
        "predecessor_row": (585, "03277917DC707D59D2663A36687CD6449F4D1FB9511F07B0E781606D3DF9F8E1"),
        "successor_row": (565, "7A83C4734991CF3DFA36AEAE10EA63D7526EB5DB511F6851A59256B89878E99C"),
    },
    "tohoku:section:1.1:p3": {
        "physical_line": 863,
        "source_loc": "sem/r18/nodes.csv:863",
        "predecessor_decision": "D000072",
        "predecessor_disposition": "extend_existing",
        "predecessor_review": "reviewed_gap",
        "predecessor_labels": "categories-definition-mono-epi",
        "tag": "003B",
        "predecessor_row": (502, "CAA2A54FC4D3D2721457B400F0B76C90224C47FB1007630AB92273361C13393E"),
        "successor_row": (632, "644EF8D32B7C653C59A22DB0C26B997036A6BC91801F680FBEE520A716245D37"),
    },
    "tohoku:classification:equivariant-bundle-extensions": {
        "physical_line": 93,
        "source_loc": "sem/r18/nodes.csv:93",
        "predecessor_decision": "D001037",
        "predecessor_disposition": "new_statement",
        "predecessor_review": "integrated_source_stacks_and_independent_review",
        "predecessor_labels": "cohomology-lemma-equivariant-extension-classes-finite-locally-free;cohomology-lemma-equivariant-ext-locally-free",
        "tag": "",
        "predecessor_row": (715, "F798388A5354116FF750531A1086C5E0BE1DD7B1BA999DABBE189ACB2A80CABA"),
        "successor_row": (669, "E352F297B787B2913E2906751841CAD7D66EB49C8D0AB85A6FCECA66A24EE2EF"),
    },
}

EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1051,
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
        "existing_equivalent": 394,
        "existing_stronger": 41,
        "existing_weaker": 3,
        "extend_existing": 7,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 1,
        "structural_only": 424,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1051,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 394,
    "extend_existing": 7,
    "new_statement": 1,
    "remaining_gap_class_dispositions": 15,
    "source_repairs_appended": 0,
    "mapping_closures": 3,
    "changed_map_rows": 3,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r68 dossier is preserved exactly; D001049-D001051 close three audited units in one no-overwrite r69 successor.\n"
    "- D1025 maps the derived category term to the admitted category definition and convention-boundary remark.\n"
    "- D1026 maps the mono/epi terminology unit to the definition and revised bounded history without underlying-set or balanced-category overclaims.\n"
    "- D1027 maps equivariant holomorphic bundle extensions to the new exact Ext/H^1 classification lemma.\n"
    "- The three frozen audits, live TeX/PDF build evidence, independent reviews, visual rasters, and byte-identical combined scanner replay are bound exactly.\n"
    "- No issue or source-repair row is appended; only D000003, D000072, and D001037 are replaced in the map.\n"
    "- The scanner indexes 119 top-level TeX files with 22,112 labels, 684 warnings, and no errors.\n"
    "- There are 1,051 decisions, 679 decided units, 32 resolved source issues, and 15 gap-class dispositions remain.\n"
    "- No GAGA comparison, higher-Ext classification, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.\n"
).encode("utf-8")

ROOT_BINDINGS = {
    "audit_d1025": ("D1025_CHECK.json", 6779, "C7BE4625A8450E53219125963F5F1453882D171CED2271ED20C6CC8D4797E95A"),
    "audit_d1026": ("D1026_CHECK.json", 9645, "81F74AF01E3271A81E6EEAD6874144AA9C97A36DE2EF9AD8E13A35BA4223D43A"),
    "audit_d1027": ("D1027_CHECK.json", 11415, "C66EAD9B101B117FBE4ABCB3C28C8B78E01A6E56595DAE0D9037FAE374BF6A51"),
    "shared_source_mapping_review": ("tmp/d1025_d1026_source_mapping_review.json", 7625, "3E19B7FF578240254832EC5FE3E6B36B493218FB8F96CB9EFAB753CEC5D9074A"),
    "d1026_design": ("tmp/d1026_mono_epi_terminology_design.json", 7412, "312D7DC106563AF5B5EAD416CB4FCD3E099B4FB6357EE93230D26B3ACDC873C6"),
    "d1026_candidate": ("tmp/d1026_mono_epi_terminology_candidate.tex", 608, "6863D0CC63ECC1019D3169DBBCE6770DBAB72D65E836045A1A68A6E0E73AC5EA"),
    "d1026_post_live_review": ("tmp/d1026_post_live_review_r1.json", 6542, "1B1C1A12EBD46FCEE4DE0D490C50AE63AE900E3AE48B44E132DA94F717FF508E"),
    "d1027_candidate": ("tmp/d1027_equivariant_bundle_extensions_candidate.tex", 2966, "198DC455A69B126F3C0DF9EB21A551316ACBDB09AFA493419011D2CFA99398CC"),
    "d1027_review": ("tmp/d1027_independent_review_r1.json", 9644, "1C8E62B24C02DAC9C83C1AB77952AFFC2ABD7DF4082B2DB9E509359C95570AC2"),
    "categories_tex": ("categories.tex", 378258, "DFAA13F0F29E5DD2AAD961D2C054A4914C1EF6C7BF91D5E05E4D5737D1DE1A39"),
    "categories_pdf": ("categories.pdf", 1099993, "01D6BCA5CFEFF76F17847A5DEB532C1551FA4E0947CE4B2C4651FA09810CA172"),
    "categories_aux": ("categories.aux", 31606, "93FA4AAC8F6C2B730B056AAAA6B0E30148A700BA5E826213530F5C729EA04A0D"),
    "categories_bbl": ("categories.bbl", 1482, "2D97AA0E9A1E329ADA1C2953203946178AD79D9577324891735B4DAA8F54C6F1"),
    "categories_blg": ("categories.blg", 1024, "FA3CA43F69ADEBFE9760E51A66109F5256BEF5645332B20965F2CE3D7236F185"),
    "categories_log": ("categories.log", 38413, "1059D51677274557BAAACAC875D0DDE14B7FC4198F3BE1DA837EA1773CE0F5E0"),
    "cohomology_tex": ("cohomology.tex", 942159, "9468C6AB79D0610AE395AB0E3FC415F43AE4473C7D09DC2808F94E6E7D947D7A"),
    "cohomology_pdf": ("cohomology.pdf", 2042133, "AF8D5785D37BEB7853B77E797CE1EB16F31C20B14A261FD4462AA4EF95F5F482"),
    "cohomology_aux": ("cohomology.aux", 58587, "3F7E39A29A4B0C23DE60D2C1B6B8809F84B7B8E3D2E6C8989EE59CEED31D4E21"),
    "cohomology_bbl": ("cohomology.bbl", 2313, "B549EC2BF6A2D441ABC2587AEB0D81AAB800C65A0F4461EC39573EACB228034A"),
    "cohomology_blg": ("cohomology.blg", 1037, "AD428028D6914435597B90AC92610E926BBA25B968AC3102678A58B633397428"),
    "cohomology_log": ("cohomology.log", 48310, "E18469FCFCBC8DA36DE4F49168C9ACE205FDC80EB9F0FC8A6845ECBCEEC31E99"),
    "bibliography": ("my.bib", 220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE"),
    "d1026_page_013": ("tmp/d1026_pdf_qa/page-013.png", 198391, "C37AF2276828D4780227AB19981C2CEC2D8852BFAAD4C443287DCEFA901C07E9"),
    "d1026_page_014": ("tmp/d1026_pdf_qa/page-014.png", 290703, "D24BF7EFC2AA508F6C1C4B4D915632A2540A86D38C6348FE003A6B0331EE397D"),
    "d1026_page_015": ("tmp/d1026_pdf_qa/page-015.png", 340972, "8B9D61754FBA488D1696EB01AD411EB081D50C6C74D14F1171D01F08D4667548"),
    "d1026_page_016": ("tmp/d1026_pdf_qa/page-016.png", 232002, "D6F48CF6523FC0F90B228B135BF19695EF34126EEE57A2C0025C51822443013B"),
    "d1027_page_196": ("tmp/d1027_pdf_qa/page-196.png", 309907, "55AA5025B978658FDCD652B601FC89B5994B1EC44A0225CF7A32867C8AC9B4E8"),
    "d1027_page_197": ("tmp/d1027_pdf_qa/page-197.png", 297237, "C0D65F5C90A1A9A484530163F7E3C3D2157B1EF0B871366AF697B5A4103316E2"),
    "d1027_page_198": ("tmp/d1027_pdf_qa/page-198.png", 289279, "EC8431B2240E00BD059E8E8E0473AEB4AFBD656F38B4F1BC8890D736E9A208FA"),
    "d1027_page_199": ("tmp/d1027_pdf_qa/page-199.png", 283764, "92DF8E5719882BED628B7CF3C92115AF9555DC3EC639EEE25DC4BE0453C4C5C6"),
    "d1027_page_200": ("tmp/d1027_pdf_qa/page-200.png", 286724, "1BBD39ECC922A568A6D563A0F534D871BDE9F9AA49ADB72405FFD27F7C6D3B49"),
    "d1027_page_201": ("tmp/d1027_pdf_qa/page-201.png", 319438, "A8C7632883269003A72D7765A6A8598F8A879454922713D590CE55F17DFF6F6F"),
}
CANONICAL_BINDINGS = {
    "authority_part_i": ("authority_snapshot/jstage_part_I_9_2_119.pdf", 7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "authority_part_ii": ("authority_snapshot/jstage_part_II_9_3_185.pdf", 3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
    "sem_r18_nodes": ("sem/r18/nodes.csv", 585012, "3A3C9B6C22B0FA5E16466C264205D97CCA6041FF785F555A4C28F9639A50550D"),
    "sem_r18_occ": ("sem/r18/occ.csv", 515084, "54E545121F4D108E5C88B7039C39E3814F71F03332592C3F3965BD49B7FACED5"),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity_from_bytes(data: bytes) -> tuple[int, str]:
    return len(data), digest(data)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_engine() -> types.ModuleType:
    payload = ENGINE_PATH.read_bytes()
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r68 transaction engine identity drift")
    module = types.ModuleType("tohoku_r69_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r68 transaction engine changed during load")
    return module


M = load_engine()
E = M.E


def bindings(specs: Mapping[str, tuple[str, int, str]]) -> dict[str, Any]:
    return {role: {"path": spec[0], "bytes": spec[1], "sha256": spec[2]} for role, spec in specs.items()}


def scanner_contract() -> dict[str, Any]:
    return {
        "oracle_path": "tmp/d1027_scan_probe_r1",
        "replay_path": "tmp/d1027_scan_probe_replay_r1",
        "files": {name: {"bytes": value[0], "sha256": value[1]} for name, value in EXPECTED_SCAN.items()},
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 684, "errors": 0},
        "inventory": EXPECTED_SCAN_INVENTORY,
    }


def map_contract() -> dict[str, Any]:
    return {
        unit: {
            "physical_line": spec["physical_line"],
            "predecessor_row": {"bytes": spec["predecessor_row"][0], "sha256": spec["predecessor_row"][1]},
            "successor_row": {"bytes": spec["successor_row"][0], "sha256": spec["successor_row"][1]},
        }
        for unit, spec in MAP_SPECS.items()
    }


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r69 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r69-transaction-contract-v1" and contract.get("contract_id") == CONTRACT_ID, "r69 contract identity mismatch")
    script = contract.get("script", {})
    require(script.get("path") == "srcmap/build_tohoku_r69.py" and identity_from_bytes(SCRIPT_PATH.read_bytes()) == (script.get("bytes"), script.get("sha256")), "r69 script pin mismatch")
    engine = contract.get("engine", {})
    require(engine.get("path") == "srcmap/build_tohoku_r68.py" and (engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r69 engine pin mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r68/r68-check.json", "bytes": EXPECTED_R68_RECEIPT[0], "sha256": EXPECTED_R68_RECEIPT[1]}, "r69 predecessor contract mismatch")
    root = bindings(ROOT_BINDINGS)
    require(contract.get("frozen_prerequisites") == [root[key] for key in ("audit_d1025", "audit_d1026", "audit_d1027")], "r69 frozen audits mismatch")
    require(contract.get("bound_inputs") == root and contract.get("canonical_inputs") == bindings(CANONICAL_BINDINGS), "r69 bound inputs mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r69 scanner contract mismatch")
    require(contract.get("decisions") == AUTHORIZED_DECISIONS and contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r69 authorized decisions/counts mismatch")
    require(contract.get("projected_files") == {name: {"bytes": value[0], "sha256": value[1]} for name, value in EXPECTED_PROJECTED.items()}, "r69 projected file pins mismatch")
    require(contract.get("map_rows") == map_contract() and contract.get("target") == "tohoku_r69", "r69 map/target contract mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r68" and transaction.get("stage") == ".tohoku-r69-txn", "r69 transaction paths mismatch")
    require(all(transaction.get(key) is True for key in ("no_overwrite", "atomic_directory_rename", "post_promotion_replay", "rollback_on_failed_replay")), "r69 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r69.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r69_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r68.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    require(json.loads(data.decode("utf-8")).get("dossier_id") == "tohoku_r62", "inherited cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "inherited r69 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1048 and rows[-1]["decision_id"] == "D001048", "r68 decision schema/count/tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, DECISIONS, header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001049-D001051 append rows drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "projected r69 decision bytes drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "inherited r69 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r68 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r68 map schema/count drift")
    replacements: dict[str, dict[str, str]] = {}
    decision_by_unit = {row["unit_id"]: row for row in DECISIONS}
    for unit, spec in MAP_SPECS.items():
        selected = E.one_row(rows, "unit_id", unit, "r68 map")
        require(selected["decision_id"] == spec["predecessor_decision"] and selected["disposition"] == spec["predecessor_disposition"] and selected["review_state"] == spec["predecessor_review"], f"r68 predecessor state drift: {unit}")
        require(selected["stacks_labels"] == spec["predecessor_labels"] and selected["stacks_tags"] == spec["tag"] and selected["source_loc"] == spec["source_loc"], f"r68 predecessor label/tag/locator drift: {unit}")
        decision = decision_by_unit[unit]
        replacement = selected.copy()
        replacement.update({
            "decision_id": decision["decision_id"],
            "disposition": decision["disposition"],
            "review_state": decision["review_state"],
            "stacks_labels": decision["stacks_labels"],
            "stacks_tags": OFFICIAL_TAGS[decision["decision_id"]],
            "rationale": decision["rationale"],
        })
        replacements[unit] = replacement
    data = E.csv_bytes(fields, [replacements.get(row["unit_id"], row) for row in rows])
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "projected r69 map bytes drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r68-check.json"
    E.require_identity(receipt, EXPECTED_R68_RECEIPT, "r68 receipt")
    for name, expected in EXPECTED_R68_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r68/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r68-v1" and value.get("status") == "PASS" and value.get("errors") == [], "r68 receipt state drift")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 18, "r68 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records} == EXPECTED_R68_FILES, "r68 receipt inventory drift")
    for unit, spec in MAP_SPECS.items():
        require(E.line_identity(E.SOURCE / "map.csv", spec["physical_line"]) == spec["predecessor_row"], f"r68 target map row drift: {unit}")
    return {"receipt": E.record(receipt, "tohoku_r68/r68-check.json")}


def verify_external() -> dict[str, Any]:
    execution = load_contract()
    predecessor = verify_predecessor()
    root_records: dict[str, Any] = {}
    for role, spec in ROOT_BINDINGS.items():
        path = ROOT / spec[0]
        E.require_identity(path, (spec[1], spec[2]), role)
        root_records[role] = E.record(path, spec[0])
    canonical_records: dict[str, Any] = {}
    for role, spec in CANONICAL_BINDINGS.items():
        path = CANONICAL_ROOT / spec[0]
        E.require_identity(path, (spec[1], spec[2]), role)
        canonical_records[role] = E.record(path, spec[0])
    audits = [E.strict_json(ROOT / ROOT_BINDINGS[f"audit_d102{n}"][0]) for n in (5, 6, 7)]
    for index, (audit, formalization, decision, physical_line) in enumerate(zip(audits, ("D1025", "D1026", "D1027"), AUTHORIZED_DECISIONS, (5, 863, 93))):
        require(audit.get("schema") == f"tohoku-stacks-{formalization.lower()}-check-v1" and audit.get("formalization_id") == formalization, f"{formalization} audit identity drift")
        require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R69_MAPPING_AUTHORIZED" and audit.get("errors") == [], f"{formalization} audit state drift")
        selection = audit.get("selection", {})
        require(selection.get("unit") == decision["unit_id"] and selection.get("predecessor_decision") == decision["supersedes"] and selection.get("predecessor_dossier") == "tohoku_r68", f"{formalization} selection drift")
        require(selection.get("source_locator") == MAP_SPECS[decision["unit_id"]]["source_loc"], f"{formalization} source locator drift")
        authorization = audit.get("mapping_authorization", {})
        require(authorization.get("status") == "AUTHORIZED_FOR_BUNDLED_NO_OVERWRITE_R69_TRANSACTION" and authorization.get("predecessor") == "tohoku_r68" and authorization.get("successor") == "tohoku_r69", f"{formalization} authorization lineage drift")
        require(authorization.get("decision") == decision and authorization.get("changed_map_rows") == [physical_line], f"{formalization} authorized decision drift")
        require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, f"{formalization} unexpected append authorization")
        source_claim = audit.get("source_claim", {})
        require(source_claim.get("source_repair_required") is False and source_claim.get("transcription_or_translation_repair_required") is False, f"{formalization} source-repair state drift")
        scanner = audit.get("shared_scanner_probe", {})
        require(scanner.get("status") == "PASS_BYTE_IDENTICAL_REPLAY" and scanner.get("oracle_path") == scanner_contract()["oracle_path"] and scanner.get("replay_path") == scanner_contract()["replay_path"], f"{formalization} scanner state/path drift")
        require(scanner.get("counts") == {"tex_files": 119, "labels": 22112, "official_tags_joined": 21437, "topics": 13, "topic_candidates": 1287, "direct_topic_coverage": 13, "warnings": 684, "errors": 0} and scanner.get("inventory") == EXPECTED_SCAN_INVENTORY, f"{formalization} scanner counts/inventory drift")
    require(audits[0]["mapping_authorization"]["projected_counts_after_this_decision"] == {"decisions": 1049, "decided_units": 679, "issues": 32, "active_issues": 0, "existing_equivalent": 392, "extend_existing": 8, "new_statement": 2, "remaining_gap_class_dispositions": 17}, "D1025 projection drift")
    require(audits[1]["mapping_authorization"]["projected_counts_after_this_decision"] == {"decisions": 1050, "decided_units": 679, "issues": 32, "active_issues": 0, "existing_equivalent": 393, "extend_existing": 7, "new_statement": 2, "remaining_gap_class_dispositions": 16}, "D1026 projection drift")
    require(audits[2]["mapping_authorization"]["projected_counts_after_bundled_r69"] == AUDIT_PROJECTED_COUNTS, "D1027 bundled projection drift")
    require(audits[2]["mapping_authorization"].get("structural_child") == {"unit_id": "tohoku:equation:holomorphic-equivariant-ext-h1", "treatment": "inherited from parent; no separate decision or changed map row"}, "D1027 structural-child treatment drift")
    review = audits[0]["independent_review"]
    require((review.get("path"), review.get("bytes"), review.get("sha256")) == ROOT_BINDINGS["shared_source_mapping_review"] and review.get("status") == "STRICT_PASS", "D1025 review binding drift")
    design = audits[1]["design_and_reviews"]
    for key, role in (("design", "d1026_design"), ("candidate", "d1026_candidate"), ("source_mapping_review", "shared_source_mapping_review"), ("post_live_independent_review", "d1026_post_live_review")):
        require((design[key].get("path"), design[key].get("bytes"), design[key].get("sha256")) == ROOT_BINDINGS[role], f"D1026 {key} binding drift")
    design = audits[2]["design_and_independent_review"]
    for key, role in (("candidate", "d1027_candidate"), ("independent_math_source_post_live_review", "d1027_review")):
        require((design[key].get("path"), design[key].get("bytes"), design[key].get("sha256")) == ROOT_BINDINGS[role], f"D1027 {key} binding drift")
    categories = (ROOT / "categories.tex").read_bytes()
    cohomology = (ROOT / "cohomology.tex").read_bytes()
    require(categories.count((ROOT / ROOT_BINDINGS["d1026_candidate"][0]).read_bytes()) == 1, "D1026 candidate/live occurrence drift")
    require(cohomology.count((ROOT / ROOT_BINDINGS["d1027_candidate"][0]).read_bytes()) == 1, "D1027 candidate/live occurrence drift")
    require(cohomology.count(b"\\label{lemma-equivariant-holomorphic-vector-bundle-extension-classes}") == 1, "D1027 raw-label cardinality drift")
    require((ROOT / "my.bib").read_bytes().count(b"@ARTICLE{Tohoku,") == 1, "Tohoku bibliography key drift")
    return {"execution": execution, "predecessor": predecessor, "root": root_records, "canonical": canonical_records}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == set(EXPECTED_SCAN) and not any(path.is_dir() for path in root.iterdir()), f"scanner oracle surface drift: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [] and check.get("counts") == EXPECTED_SCAN_COUNTS and len(check.get("warnings", [])) == 684, "r69 scanner state/count drift")
    tex = check.get("tex_sha256", {})
    require(tex.get("categories.tex") == ROOT_BINDINGS["categories_tex"][2] and tex.get("cohomology.tex") == ROOT_BINDINGS["cohomology_tex"][2], "r69 scanner live TeX binding drift")
    _, rows = E.load_csv(root / "stx.csv")
    new_label = "cohomology-lemma-equivariant-holomorphic-vector-bundle-extension-classes"
    row = E.one_row(rows, "full_label", new_label, "r69 scanner D1027 label")
    require(row["file"] == "cohomology.tex" and row["line"] == "20529" and row["tag"] == "" and row["text_sha256"] == "7EB638B91935D0B604E920CF2D1DBD8C0ADCC501DFFA4A553DF037CA4A1E3881", "r69 scanner D1027 label row drift")
    require(E.line_identity(root / "stx.csv", 3633) == (313, "6561D2B4A7093DA49039EE40ECE90752FF17E2657323DD65194AF6E97E6CC540"), "r69 scanner D1027 row identity drift")
    mono = E.one_row(rows, "full_label", "categories-lemma-mono-epi-composition", "r69 scanner D1026 label")
    require(mono["line"] == "1252" and mono["text_sha256"] == "2046B2664D945FB00860CAFB928D82E2C1FC23B5F924AC0746D38327B0263B65", "r69 scanner D1026 label drift")
    require(E.line_identity(root / "stx.csv", 2284) == (216, "67441070172AF4EC7985F4FD0958DE9CE3A8D2E72A157FAB0A374FC9FF43A419"), "r69 scanner D1026 row identity drift")
    old_labels = {item["full_label"] for item in E.load_csv(E.SOURCE / "stx.csv")[1]}
    require(new_label not in old_labels, "D1027 label unexpectedly present in r68")
    require({"categories-definition-category", "categories-remark-category-convention-boundary", "categories-definition-mono-epi", "categories-lemma-mono-epi-composition"} <= old_labels, "D1025/D1026 inherited labels missing from r68")
    return check


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink() and E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "D1027 scanner oracle/replay missing or unsafe")
    verify_scan(E.ORACLE, oracle_surface=True)
    verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"D1027 scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1027_scan_probe_r1/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1027_scan_probe_replay_r1/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"missing or unsafe r69 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r69-check.json"} if receipt_mode else set()) and not any(path.is_dir() for path in root.iterdir()), "r69 output surface drift")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r69 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"inherited r69 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes() and (root / "map.csv").read_bytes() == expected_map_bytes(), "r69 decision/map drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r69 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R68_FILES["ucand.csv"], "r69/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [] and mcheck.get("counts") == EXPECTED_COUNTS and len(mcheck.get("warnings", [])) == 684, "r69 mapping state/count drift")
    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1052)] and decisions[-3:] == DECISIONS, "r69 decision sequence/tail drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r69 issue sequence drift")
    decisions_by_unit = {row["unit_id"]: row for row in DECISIONS}
    for unit, spec in MAP_SPECS.items():
        selected = E.one_row(mapping, "unit_id", unit, "r69 map")
        decision = decisions_by_unit[unit]
        require(selected["decision_id"] == decision["decision_id"] and selected["disposition"] == "existing_equivalent" and selected["review_state"] == decision["review_state"], f"r69 target state drift: {unit}")
        require(selected["stacks_labels"] == decision["stacks_labels"] and selected["stacks_tags"] == spec["tag"] and selected["source_loc"] == spec["source_loc"], f"r69 target label/tag/locator drift: {unit}")
        require(E.line_identity(root / "map.csv", spec["physical_line"]) == spec["successor_row"], f"r69 target map row identity drift: {unit}")
    deltas = E.map_row_delta()
    require(len(deltas) == 14 and {row["unit_id"] for row in deltas} == set(MAP_SPECS), "r69 map delta cardinality/scope drift")
    fields_by_unit = {unit: {row["field"] for row in deltas if row["unit_id"] == unit} for unit in MAP_SPECS}
    require(fields_by_unit["tohoku:term:category"] == {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"}, "D1025 actual changed fields drift")
    require(fields_by_unit["tohoku:section:1.1:p3"] == {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"}, "D1026 actual changed fields drift")
    require(fields_by_unit["tohoku:classification:equivariant-bundle-extensions"] == {"decision_id", "disposition", "stacks_labels", "rationale"}, "D1027 actual changed fields drift")
    remaining = sum(1 for row in mapping if row["disposition"] in {"existing_weaker", "extend_existing", "new_section", "new_statement"})
    require(remaining == 15, "r69 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1051,
        "decisions_appended": [row["decision_id"] for row in DECISIONS],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 684, "errors": 0},
        "remaining_gap_class_dispositions": 15,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 3,
        "map_delta": {"changed_units": 3, "changed_fields": 14, "unchanged_units": 988, "authorized_but_value_preserved": {"all_three": ["stacks_tags"], "D001051": ["review_state"]}},
        "semantic_inventory_generation": "sem/r18",
        "source_change": "D1025_MAPPING_ONLY_PLUS_D1026_ADMITTED_CATEGORIES_HISTORY_PLUS_D1027_ADMITTED_COHOMOLOGY_LEMMA",
        "scanner_payload_change": "COMBINED_D1026_HISTORY_TEXT_AND_D1027_ONE_NEW_LABEL",
    }
    if receipt_mode:
        require(E.strict_json(root / "r69-check.json") == receipt_payload(root, result), "r69 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    records = external["root"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r69-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalizations": {
            "D1025": {"audit": records["audit_d1025"], "independent_review": records["shared_source_mapping_review"], "change_class": "mapping_only_closure"},
            "D1026": {"audit": records["audit_d1026"], "design": records["d1026_design"], "candidate": records["d1026_candidate"], "reviews": [records["shared_source_mapping_review"], records["d1026_post_live_review"]], "live_source": records["categories_tex"], "live_pdf": records["categories_pdf"], "build_support": [records[key] for key in ("categories_aux", "categories_bbl", "categories_blg", "categories_log")], "visual_rasters": [records[f"d1026_page_{page:03d}"] for page in range(13, 17)]},
            "D1027": {"audit": records["audit_d1027"], "candidate": records["d1027_candidate"], "independent_review": records["d1027_review"], "live_source": records["cohomology_tex"], "live_pdf": records["cohomology_pdf"], "build_support": [records[key] for key in ("cohomology_aux", "cohomology_bbl", "cohomology_blg", "cohomology_log")], "visual_rasters": [records[f"d1027_page_{page:03d}"] for page in range(196, 202)]},
            "bibliography": records["bibliography"],
        },
        "source_chain": external["canonical"],
        "scanner_oracle": oracles["oracle"],
        "scanner_replay": oracles["replay"],
        "deltas": dict(deltas),
        "files": E.output_records(root),
        "nonclaims": [
            "D001049-D001051 close only their three named units.",
            "The structural equation child inherits D001051 and receives no separate decision row.",
            "No issue, source repair, semantic successor, GAGA comparison, higher-Ext classification, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r68"
    E.TARGET = ROOT / "tohoku_r69"
    E.STAGE = ROOT / ".tohoku-r69-txn"
    E.ORACLE = ROOT / "tmp" / "d1027_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1027_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R68_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R68_FILES
    E.EXPECTED_SCAN = EXPECTED_SCAN
    E.EXPECTED_SCAN_COUNTS = EXPECTED_SCAN_COUNTS
    E.EXPECTED_PROJECTED = EXPECTED_PROJECTED
    E.EXPECTED_APPEND_ROWS = {"decision": EXPECTED_DECISION_APPEND}
    E.EXPECTED_COUNTS = EXPECTED_COUNTS
    E.STATUS_BYTES = STATUS_BYTES
    E.DECISION = DECISIONS[-1]
    E.STACKS_INPUTS = {
        "categories_tex": ROOT_BINDINGS["categories_tex"],
        "cohomology_tex": ROOT_BINDINGS["cohomology_tex"],
    }
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r69 target or stage already exists")
    print(json.dumps({"schema": "tohoku-r69-scanner-oracle-v1", "status": "PASS_REPLAY", "errors": [], "scanner_oracles": verify_oracles(), "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 684, "errors": 0}}, indent=2, sort_keys=True))


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r69 target or stage already exists")
    external = verify_external()
    oracles = verify_oracles()
    projection = {
        "cfg.json": identity_from_bytes(expected_cfg_bytes()),
        "dec.csv": identity_from_bytes(expected_decision_bytes()),
        "issues.csv": identity_from_bytes(expected_issue_bytes()),
        "map.csv": identity_from_bytes(expected_map_bytes()),
        "STATUS.md": identity_from_bytes(STATUS_BYTES),
    }
    print(json.dumps({"schema": "tohoku-r69-static-input-audit-v1", "status": "PASS", "errors": [], "external": external, "scanner_oracles": oracles, "projection": projection, "decisions": [row["decision_id"] for row in DECISIONS], "issue": None, "source_repair": None, "remaining_gaps": 15}, indent=2, sort_keys=True))


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    require(not E.STAGE.exists(), "r69 stage already exists")
    E.build_stage()
    deltas = verify_stage(E.STAGE)
    E.exclusive_write(E.STAGE / "r69-check.json", E.json_bytes(receipt_payload(E.STAGE, deltas)))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r69 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("post-promotion r69 replay failed; target rolled back") from exc
    print(json.dumps({"schema": "tohoku-r69-transaction-result-v1", "status": "PASS_COMMITTED", "errors": [], "target": "tohoku_r69", "receipt": E.record(E.TARGET / "r69-check.json"), "remaining_gaps": 15}, indent=2, sort_keys=True))


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink() and not E.STAGE.exists(), "r69 target/stage state invalid")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(json.dumps({"schema": "tohoku-r69-replay-v1", "status": "PASS_REPLAY", "errors": [], "receipt": E.record(E.TARGET / "r69-check.json"), "deltas": result}, indent=2, sort_keys=True))


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
