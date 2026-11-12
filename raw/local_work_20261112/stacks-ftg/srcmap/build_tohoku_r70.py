#!/usr/bin/env python3
"""Build, validate, atomically promote, and replay the audited D1028/r70 successor."""

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
ENGINE_PATH = ROOT / "srcmap" / "build_tohoku_r69.py"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r70_contract.json"
CANONICAL_ROOT = (
    ROOT.parent
    / "interlanguage"
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "03_working_translations"
    / "tohoku_bilingual_canonical_stacks_20260804_r1"
)

ENGINE_IDENTITY = (42776, "FC60E705F1F0878D2E8217F63176CD92C39C02A5E5DD8F5A9045A9601513E630")
CONTRACT_ID = "D1028-r70-D001052-D001062-v1"
EXPECTED_R69_RECEIPT = (14442, "81987ECCB8D7020484FCE74B286D51DE374D8F18727CCDB237EA382F1ED8BBAD")
EXPECTED_R69_FILES = {
    "STATUS.md": (1118, "C15E759CE489CE20DDE44B06A56ECE416947A0EDF8367D1E86465B67D1970C24"),
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83727, "C65DA64B135E1A17179F8DED6880226DE9ECEA62E149B00C8FEE79CB354F343E"),
    "dec.csv": (391385, "E7AA26C9073717E418FCB2BC0ADC20E1AE89762BEF55D69C260A0BE3909FD837"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (487554, "0427AEA97444BC58E7C3823B91FDFCD84CC531DAB4D6C93F38C8EE9D52BB3A00"),
    "mcheck.json": (73553, "EA9CD78E7C851FEAC7997E017CC6990C06B241508DFC68747B0C33BF02E8868D"),
    "stx.csv": (5290391, "3083041A38A704D6A8815B21D42AC8E617AFA8D404B289586A820D1C80AE3346"),
    "tcand.csv": (489720, "69156C767922272E47416C2471DD2EC5B9A905B4E1964B56806145892A7FECC9"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "2C1917E032CAE4B174E89319E4BC860D4CB04967899F1B0679C0527B95E952D7"),
    "check.json": (83847, "07C5D80259067698B473D2D9A0B7EE95FCAA10081F8F2258BE73BC83AA7C3258"),
    "stx.csv": (5290688, "86D4B13F8189D71ABC67EB7C40A79EE6F1AC86D564812F120506A2F4321C01DC"),
    "tcand.csv": (489828, "6811DEB4478A0EDCEF25B6742920E9DC65878BDAD7436D79D419E0D7CF1B2320"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22113,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1287,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_TOTAL_BYTES = 5874391
EXPECTED_PROJECTED = {
    "dec.csv": (406725, "2D8D386A770F9FCF46009647B46B9F05F7AC8B0C91213F83930147CD216F1E15"),
    "issues.csv": EXPECTED_R69_FILES["issues.csv"],
    "map.csv": (499089, "FC5B419371E2551296FD3D4A91DB7278C5C4B90D6C06D947A3025E748904F675"),
}
EXPECTED_DECISION_APPEND = (15340, "094C90A389EE02E9A24133B1E6D4854A888E34592F6CBF64B320E10F81D831A6")
EXPECTED_TOOL_MAP = (499089, "282078CFF637852946C8A1E518D59FA3FB4FE83A25525735C9A0FDC03A675DCF")
TOOL_TAG_ORDER_UNITS = {
    "tohoku:section:2.3",
    "tohoku:section:2.4",
    "tohoku:section:3.3",
    "tohoku:section:3.6",
}

DECISION_ORDER = [
    ("D001052", "tohoku:classification:coherent-extension-classes", "audit_d1028"),
    ("D001053", "tohoku:section:1.9", "parent_review_12"),
    ("D001054", "tohoku:section:2.1", "parent_review_12"),
    ("D001055", "tohoku:section:2.2", "parent_review_12"),
    ("D001056", "tohoku:section:2.3", "parent_review_12"),
    ("D001057", "tohoku:section:2.4", "parent_review_12"),
    ("D001058", "tohoku:section:3.3", "parent_review_35"),
    ("D001059", "tohoku:section:3.5", "parent_review_35"),
    ("D001060", "tohoku:section:3.6", "parent_review_35"),
    ("D001061", "tohoku:section:5.2", "parent_review_35"),
    ("D001062", "tohoku:section:5.5", "parent_review_35"),
]

SUCCESSOR_ROWS = {
    "tohoku:classification:coherent-extension-classes": (593, "1E3106D5BFB9F792C066886E2BED96C7B3F1F856083B3B0651899B81E4AD1DBF"),
    "tohoku:section:1.9": (1457, "17D7CB8D6D56FDE4061766E0319212653EF41590530C864180E4A974583C9FCA"),
    "tohoku:section:2.1": (1241, "78F1E65D1CA44697741DAC92AD6B5A83EF83B889DCA0F1876AE9DE52463B7010"),
    "tohoku:section:2.2": (1666, "D06478E797FFD55CE80C073C3B8213C07A9450F38202C50FB8ECE819A64C7CEA"),
    "tohoku:section:2.3": (1766, "761BD4B5FDFBBBC0A44FE622A16C6F3E19F474A9929D138C051362AFE25AA905"),
    "tohoku:section:2.4": (2482, "0D4958D6F08AF802B6E5B3CCCD78880D11D9C2CCB6A9500B345CED84DC93DD39"),
    "tohoku:section:3.3": (1718, "38A9BB3930F94D8443B8F82D1534D0EE2C22E6791BCDF10978B148DFDAFC9A12"),
    "tohoku:section:3.5": (1095, "717853F7E8F0C206FF36339888AE392BC75C6B2066B024C77666406906B24380"),
    "tohoku:section:3.6": (1561, "464F75B63B6A5CC4AA1EC278AA233935BBBC9CAA93DBBB8C58E2C9819B88F46A"),
    "tohoku:section:5.2": (1829, "E51A429435CFBAC819183D75FE561DC6C4A86091EB4993CDAE01FC289EA0E2B7"),
    "tohoku:section:5.5": (2383, "8FAC0F2A8FCF286A01DFECC45FF33FA3B05F71E2293AAC03FAD89E5529847121"),
}

EXPECTED_CHANGED_FIELDS = {
    "tohoku:classification:coherent-extension-classes": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:1.9": {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"},
    "tohoku:section:2.1": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:2.2": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:2.3": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:2.4": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:3.3": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:3.5": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:3.6": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
    "tohoku:section:5.2": {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"},
    "tohoku:section:5.5": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
}

EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1062,
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
        "existing_equivalent": 397,
        "existing_stronger": 41,
        "existing_weaker": 2,
        "historical_reference": 33,
        "new_section": 1,
        "new_statement": 1,
        "structural_only": 432,
    },
}
AUDIT_PROJECTED_COUNTS = {
    "decisions": 1062,
    "decided_units": 679,
    "issues": 32,
    "active_issues": 0,
    "existing_equivalent": 397,
    "existing_weaker": 2,
    "extend_existing": 0,
    "new_section": 1,
    "new_statement": 1,
    "structural_only": 432,
    "remaining_gap_class_dispositions": 4,
    "mapping_closures": 11,
    "changed_map_rows": 11,
}

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r69 dossier is preserved exactly; D001052-D001062 close the audited D1028 unit and ten aggregate parent sections in one no-overwrite r70 successor.\n"
    "- D001052 binds the coherent equivariant analytic extension-class lemma, its successful PDF build, visual QA, independent reviews, and byte-identical scanner replay.\n"
    "- D001053-D001062 aggregate only already sealed direct-child coverage authorized by the two frozen parent reviews; they make no live or source edit.\n"
    "- No issue or source-repair row is appended; only map lines 92, 902, 904, 905, 906, 907, 913, 915, 916, 925, and 928 are replaced.\n"
    "- The scanner indexes 119 top-level TeX files with 22,113 labels, 685 warnings, and no errors.\n"
    "- There are 1,062 decisions, 679 decided units, 32 resolved source issues, and 4 gap-class dispositions remain.\n"
    "- No D1030 or D1031 decision, GAGA comparison, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.\n"
).encode("utf-8")

ROOT_BINDINGS = {
    "audit_d1028": ("D1028_CHECK.json", 14287, "82A608B907095F2FBFBBA3BDC2819BFE6AAEBC9294AE474A5A1FF925AFE93BA0"),
    "d1028_design": ("tmp/d1028_coherent_equivariant_extensions_design.json", 7321, "57B79BE0C651531A20CE0BE6F6DEFC234CD4259131B580C358912B41D6BB8AF8"),
    "d1028_candidate": ("tmp/d1028_coherent_equivariant_extensions_candidate.tex", 2708, "77F46B392C42FF7A6C5537F785FF3460907BFC155EB423321F7BA05495CF7509"),
    "d1028_pre_live_review": ("tmp/d1028_independent_review_r1.json", 5538, "5C690E8BAF16D6ABC753124E1EE8E5702C69460B0C53E10E4ABC6EF226F74BFC"),
    "d1028_post_live_review": ("tmp/d1028_post_live_independent_review_r1.json", 6610, "4790CAA71C09A1BCBF0EFEAF9D6ABB63D9254CF757C38D8A39C05D3F654ABD6B"),
    "parent_review_12": ("tmp/d1028_parent_sections_12_review.json", 249846, "5F1806007B0CF4063CE2C263D1CB08B1453BF87132A964744F2C5142939FBF87"),
    "parent_review_35": ("tmp/d1028_parent_sections_35_review.json", 362947, "97CA73C11512296E8559BC482EAD3365FF3673C853F3705475CF9E03F34E3AD2"),
    "cohomology_tex": ("cohomology.tex", 944867, "BDAA9A64E5C0FC52A3B55E57E912624591AD093F8B9933EB8200F08EFC9D7F16"),
    "cohomology_pdf": ("cohomology.pdf", 2046160, "FA395E530DE8AA0C40126D4478384DCDCA7B6FD2B23046AA88E485082A60129D"),
    "cohomology_aux": ("cohomology.aux", 58735, "E45B1F519A78C5398F21234208C02A22664D3B48B3C0BAE7AA301556CF8BB27F"),
    "cohomology_bbl": ("cohomology.bbl", 2313, "B549EC2BF6A2D441ABC2587AEB0D81AAB800C65A0F4461EC39573EACB228034A"),
    "cohomology_blg": ("cohomology.blg", 1037, "AD428028D6914435597B90AC92610E926BBA25B968AC3102678A58B633397428"),
    "cohomology_log": ("cohomology.log", 48473, "31124DECC9DCED08661DB4E8DCAA992CE45EC1BB2B5AF756C2E72A161DF784C7"),
    "cohomology_out": ("cohomology.out", 12725, "E20175BCE90BA5C272D88818F692C70BF698D24E5E04C6CAF200E3D812D62651"),
    "cohomology_toc": ("cohomology.toc", 5574, "CC64D3C6E8621D86AD88B7479A39F11A0FCDF6BE04CF2834B7F07677EB6DCCA5"),
    "bibliography": ("my.bib", 220625, "6502A16A823B313079B50B08563C7400052E753C62C701B8C5650FE66915EABE"),
    "coherent_tex": ("coherent.tex", 365621, "802D88F603D79F9AFC4E098EDD555E86446EC53054D0A3C7BDE70F096B18DF90"),
    "derived_tex": ("derived.tex", 531085, "0568168AA8E3D596D6D42FC782F1EF17091BFA07F5F715807743E99CDA5FB7F5"),
    "etale_cohomology_tex": ("etale-cohomology.tex", 909671, "015F27B1D332CC096B1F323DAEEB855B299BB5A08F43C05131F196D4C183E7BF"),
    "homology_tex": ("homology.tex", 382168, "E9BF2AE74E2F0392A05A37405B12C97E590D12ADA1DA23D3B694E4AD782A30AF"),
    "injectives_tex": ("injectives.tex", 139285, "FEBCC2562AB17FEC850FD5FD88086DC3EB90017C007F348207ED93479895A283"),
    "modules_tex": ("modules.tex", 232828, "EF800D241EBA37CE7099F9B09440228969710988903EE393261C866F902A12F5"),
    "sheaves_tex": ("sheaves.tex", 215623, "78A727DA8893E4FB2362CC6343BD6B2E66FEBD1519328CA84835BF5E2C225B9F"),
    "topology_tex": ("topology.tex", 250729, "86FD4B6E4E0116F8DD6253E8B01BD04F6E270DDA0FCE0628996BEEEF1F24F190"),
    "page_198": ("tmp/d1028_pdf_qa/page-198.png", 399654, "4D438B84EC8E7ADA5399C7A108B424D3A42CC3CDB10227EE1E25FD913A2B28F5"),
    "page_199": ("tmp/d1028_pdf_qa/page-199.png", 367754, "D9717ADE879030B7701F344F9E72A0AC1FA75F562F71638A4304AFE819FCD270"),
    "page_200": ("tmp/d1028_pdf_qa/page-200.png", 348547, "13EC2299AF41968C476A4DEAC854151E1C120A469DCFAFF315208746479D8AC7"),
    "page_201": ("tmp/d1028_pdf_qa/page-201.png", 370333, "9C102742BF00B0A0C9AE58CB944FCD024CDB23EDE5F80594A187A71D16FF7119"),
    "page_245": ("tmp/d1028_pdf_qa/page-245.png", 430958, "F5BBA4B030AF6081F3EB2F17E7B6D3B8FADC786B95D7D438F7A21AD71120C811"),
    "page_246": ("tmp/d1028_pdf_qa/page-246.png", 554801, "7C5AC235B5EA1B76E17A7313805E22E2087F5463E5C99A80E06AE527579E2EDF"),
    "page_247": ("tmp/d1028_pdf_qa/page-247.png", 225677, "2B6438DE266D58266760DE53FFB641901CBCE5EA5EF9E55AF59150C15F92A3DE"),
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
    require(identity_from_bytes(payload) == ENGINE_IDENTITY, "r69 transaction engine identity drift")
    module = types.ModuleType("tohoku_r70_engine")
    module.__file__ = str(ENGINE_PATH)
    exec(compile(payload, str(ENGINE_PATH), "exec"), module.__dict__)
    require(identity_from_bytes(ENGINE_PATH.read_bytes()) == ENGINE_IDENTITY, "r69 transaction engine changed during load")
    return module


M = load_engine()
E = M.E


def read_json(relative: str) -> dict[str, Any]:
    value = json.loads((ROOT / relative).read_bytes().decode("utf-8"))
    require(isinstance(value, dict), f"JSON object required: {relative}")
    return value


def csv_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ";".join(str(item) for item in value)
    return str(value)


def derive_authorization() -> tuple[list[dict[str, str]], dict[str, str], dict[str, dict[str, Any]]]:
    audit = read_json(ROOT_BINDINGS["audit_d1028"][0])
    reviews = {
        role: read_json(ROOT_BINDINGS[role][0])
        for role in ("parent_review_12", "parent_review_35")
    }
    main = dict(audit["mapping_authorization"]["decision"])
    main_tag = str(main.pop("official_tags"))
    decisions: list[dict[str, str]] = [{key: str(value) for key, value in main.items()}]
    tags = {decisions[0]["decision_id"]: main_tag}
    specs: dict[str, dict[str, Any]] = {
        decisions[0]["unit_id"]: {
            "physical_line": 92,
            "source_loc": "sem/r18/nodes.csv:92",
            "predecessor_decision": "D000564",
            "predecessor_disposition": "extend_existing",
            "predecessor_review": "reviewed_gap",
            "predecessor_labels": "stacks-cohomology-lemma-extension-coherent;homology-definition-ext-group;derived-lemma-ext-1",
            "predecessor_tags": "0GRA;010K;06XV",
            "predecessor_row": (612, "BAF87171EF9028F9A235082CE738EBCA2027FCC201A6922925BDAE976A497945"),
            "predecessor_decision_line": 565,
            "predecessor_decision_row": (415, "814D13B3976F0E2D839F963D319F43B6549B45E0E0D7C8A97CA2E4AF4AC83D39"),
        }
    }
    sections = {
        section["unit_id"]: section
        for review in reviews.values()
        for section in review["parent_sections"]
    }
    for decision_id, unit, role in DECISION_ORDER[1:]:
        require(unit in sections and any(item["unit_id"] == unit for item in reviews[role]["parent_sections"]), f"missing parent authorization: {unit}")
        section = sections[unit]
        authorization = section["authorization"]
        decision = {
            "decision_id": decision_id,
            "unit_id": unit,
            "action": authorization["action"],
            "disposition": authorization["disposition"],
            "stacks_labels": authorization["stacks_labels_csv"],
            "rationale": authorization["rationale"],
            "review_state": authorization["review_state"],
            "supersedes": authorization["replaces_only"],
        }
        decisions.append(decision)
        tags[decision_id] = authorization["stacks_tags_csv"]
        predecessor = section["predecessor"]
        specs[unit] = {
            "physical_line": int(section["requested_map_line"]),
            "source_loc": f"sem/r18/nodes.csv:{section['requested_map_line']}",
            "predecessor_decision": predecessor["decision_id"],
            "predecessor_disposition": predecessor["disposition"],
            "predecessor_review": predecessor["review_state"],
            "predecessor_labels": csv_value(predecessor["stacks_labels"]),
            "predecessor_tags": csv_value(predecessor["stacks_tags"]),
            "predecessor_row": (int(predecessor["map_row"]["lf_utf8_bytes"]), predecessor["map_row"]["lf_sha256"]),
            "predecessor_decision_line": int(predecessor["decision_row"]["physical_line"]),
            "predecessor_decision_row": (int(predecessor["decision_row"]["lf_utf8_bytes"]), predecessor["decision_row"]["lf_sha256"]),
        }
    require([(row["decision_id"], row["unit_id"]) for row in decisions] == [(did, unit) for did, unit, _ in DECISION_ORDER], "r70 derived decision order drift")
    for unit, spec in specs.items():
        spec["successor_row"] = SUCCESSOR_ROWS[unit]
    return decisions, tags, specs


DECISIONS, OFFICIAL_TAGS, MAP_SPECS = derive_authorization()
AUTHORIZED_DECISIONS = [{**row, "official_tags": OFFICIAL_TAGS[row["decision_id"]]} for row in DECISIONS]


def bindings(specs: Mapping[str, tuple[str, int, str]]) -> dict[str, Any]:
    return {role: {"path": spec[0], "bytes": spec[1], "sha256": spec[2]} for role, spec in specs.items()}


def scanner_contract() -> dict[str, Any]:
    return {
        "oracle_path": "tmp/d1028_scan_probe_r1",
        "replay_path": "tmp/d1028_scan_probe_replay_r1",
        "files": {name: {"bytes": value[0], "sha256": value[1]} for name, value in EXPECTED_SCAN.items()},
        "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 685, "errors": 0},
        "inventory": {"files": 6, "bytes": EXPECTED_SCAN_TOTAL_BYTES},
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
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r70 contract missing or unsafe")
    contract = json.loads(CONTRACT_PATH.read_bytes().decode("utf-8"))
    require(contract.get("schema") == "tohoku-r70-transaction-contract-v1" and contract.get("contract_id") == CONTRACT_ID, "r70 contract identity mismatch")
    script = contract.get("script", {})
    require(script.get("path") == "srcmap/build_tohoku_r70.py" and identity_from_bytes(SCRIPT_PATH.read_bytes()) == (script.get("bytes"), script.get("sha256")), "r70 script pin mismatch")
    engine = contract.get("engine", {})
    require(engine.get("path") == "srcmap/build_tohoku_r69.py" and (engine.get("bytes"), engine.get("sha256")) == ENGINE_IDENTITY, "r70 engine pin mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r69/r69-check.json", "bytes": EXPECTED_R69_RECEIPT[0], "sha256": EXPECTED_R69_RECEIPT[1]}, "r70 predecessor contract mismatch")
    root = bindings(ROOT_BINDINGS)
    require(contract.get("frozen_prerequisites") == [root[key] for key in ("audit_d1028", "parent_review_12", "parent_review_35")], "r70 frozen prerequisite mismatch")
    require(contract.get("bound_inputs") == root and contract.get("canonical_inputs") == bindings(CANONICAL_BINDINGS), "r70 bound-input mismatch")
    require(contract.get("scanner_probe") == scanner_contract(), "r70 scanner contract mismatch")
    require(contract.get("decision_order") == [row["decision_id"] + ":" + row["unit_id"] for row in DECISIONS], "r70 decision order contract mismatch")
    require(contract.get("decision_append") == {"bytes": EXPECTED_DECISION_APPEND[0], "sha256": EXPECTED_DECISION_APPEND[1]}, "r70 decision append contract mismatch")
    require(contract.get("projected_counts") == AUDIT_PROJECTED_COUNTS, "r70 projected-count contract mismatch")
    require(contract.get("projected_files") == {name: {"bytes": value[0], "sha256": value[1]} for name, value in EXPECTED_PROJECTED.items()}, "r70 projected-file contract mismatch")
    require(contract.get("tool_map_normalization") == {"raw_map": {"bytes": EXPECTED_TOOL_MAP[0], "sha256": EXPECTED_TOOL_MAP[1]}, "field": "stacks_tags", "units": sorted(TOOL_TAG_ORDER_UNITS), "rule": "same unique tag sets; rewrite only to the frozen parent-review order"}, "r70 tool-map normalization contract mismatch")
    require(contract.get("map_rows") == map_contract() and contract.get("target") == "tohoku_r70", "r70 map/target contract mismatch")
    require(contract.get("no_issue_or_source_repair_append") is True, "r70 append-scope contract mismatch")
    transaction = contract.get("transaction", {})
    require(transaction.get("source") == "tohoku_r69" and transaction.get("stage") == ".tohoku-r70-txn", "r70 transaction paths mismatch")
    require(all(transaction.get(key) is True for key in ("no_overwrite", "atomic_directory_rename", "post_promotion_replay", "rollback_on_failed_replay")), "r70 transaction guarantees missing")
    return {
        "script": E.record(SCRIPT_PATH, "srcmap/build_tohoku_r70.py"),
        "contract": E.record(CONTRACT_PATH, "srcmap/tohoku_r70_contract.json"),
        "engine": E.record(ENGINE_PATH, "srcmap/build_tohoku_r69.py"),
        "python": E.record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    data = (E.SOURCE / "cfg.json").read_bytes()
    require(json.loads(data.decode("utf-8")).get("dossier_id") == "tohoku_r62", "inherited cfg dossier drift")
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "inherited r70 cfg drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "dec.csv")
    require(fields == E.DEC_FIELDS and len(rows) == 1051 and rows[-1]["decision_id"] == "D001051", "r69 decision schema/count/tail drift")
    append = E.csv_bytes(E.DEC_FIELDS, DECISIONS, header=False)
    require(identity_from_bytes(append) == EXPECTED_DECISION_APPEND, "D001052-D001062 append rows drift")
    data = (E.SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "projected r70 decision bytes drift")
    return data


def expected_issue_bytes() -> bytes:
    data = (E.SOURCE / "issues.csv").read_bytes()
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "inherited r70 issues drift")
    fields, rows = E.load_csv(E.SOURCE / "issues.csv")
    require(fields == E.ISSUE_FIELDS and len(rows) == 32 and rows[-1]["issue_id"] == "I000032", "r69 issue schema/count drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = E.load_csv(E.SOURCE / "map.csv")
    require(fields == E.MAP_FIELDS and len(rows) == 991, "r69 map schema/count drift")
    replacements: dict[str, dict[str, str]] = {}
    decision_by_unit = {row["unit_id"]: row for row in DECISIONS}
    for unit, spec in MAP_SPECS.items():
        selected = E.one_row(rows, "unit_id", unit, "r69 map")
        require(selected["decision_id"] == spec["predecessor_decision"] and selected["disposition"] == spec["predecessor_disposition"] and selected["review_state"] == spec["predecessor_review"], f"r69 predecessor state drift: {unit}")
        require(selected["stacks_labels"] == spec["predecessor_labels"] and selected["stacks_tags"] == spec["predecessor_tags"] and selected["source_loc"] == spec["source_loc"], f"r69 predecessor label/tag/locator drift: {unit}")
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
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "projected r70 map bytes drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = E.SOURCE / "r69-check.json"
    E.require_identity(receipt, EXPECTED_R69_RECEIPT, "r69 receipt")
    for name, expected in EXPECTED_R69_FILES.items():
        E.require_identity(E.SOURCE / name, expected, f"r69/{name}")
    value = E.strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r69-v1" and value.get("status") == "PASS" and value.get("errors") == [], "r69 receipt state drift")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 15, "r69 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records} == EXPECTED_R69_FILES, "r69 receipt inventory drift")
    for unit, spec in MAP_SPECS.items():
        require(E.line_identity(E.SOURCE / "map.csv", spec["physical_line"]) == spec["predecessor_row"], f"r69 target map row drift: {unit}")
        require(E.line_identity(E.SOURCE / "dec.csv", spec["predecessor_decision_line"]) == spec["predecessor_decision_row"], f"r69 predecessor decision row drift: {unit}")
    return {"receipt": E.record(receipt, "tohoku_r69/r69-check.json")}


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

    audit = E.strict_json(ROOT / ROOT_BINDINGS["audit_d1028"][0])
    require(audit.get("schema") == "tohoku-stacks-d1028-check-v1" and audit.get("formalization_id") == "D1028", "D1028 audit identity drift")
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R70_MAPPING_AUTHORIZED" and audit.get("errors") == [], "D1028 audit state drift")
    selection = audit.get("selection", {})
    require(selection.get("unit") == DECISIONS[0]["unit_id"] and selection.get("predecessor_decision") == DECISIONS[0]["supersedes"] and selection.get("predecessor_dossier") == "tohoku_r69" and selection.get("source_locator") == "sem/r18/nodes.csv:92", "D1028 selection drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("status") == "AUTHORIZED_FOR_BUNDLED_NO_OVERWRITE_R70_TRANSACTION" and authorization.get("predecessor") == "tohoku_r69" and authorization.get("successor") == "tohoku_r70", "D1028 authorization lineage drift")
    require(authorization.get("decision") == AUTHORIZED_DECISIONS[0] and authorization.get("changed_map_rows") == [92], "D1028 decision authorization drift")
    require(authorization.get("issue_append") is None and authorization.get("source_repair_append") is None, "D1028 unexpected append authorization")
    require(authorization.get("projected_counts_after_bundled_r70") == AUDIT_PROJECTED_COUNTS, "D1028 bundled projection drift")
    require(authorization.get("bundled_r70_decision_order") == [did + ":" + unit for did, unit, _ in DECISION_ORDER], "D1028 bundled decision order drift")
    parent_refs = authorization.get("bundled_r70_parent_reviews")
    require(parent_refs == [{"path": ROOT_BINDINGS[key][0], "bytes": ROOT_BINDINGS[key][1], "sha256": ROOT_BINDINGS[key][2], "status": "STRICT_PASS"} for key in ("parent_review_12", "parent_review_35")], "D1028 parent-review references drift")
    source_claim = audit.get("source_claim", {})
    require(source_claim.get("source_repair_required") is False and source_claim.get("transcription_or_translation_repair_required") is False and source_claim.get("issue_append_required") is False, "D1028 source/issue state drift")
    design = audit.get("design_and_independent_review", {})
    for key, role in (("design", "d1028_design"), ("candidate", "d1028_candidate"), ("pre_live_review", "d1028_pre_live_review"), ("post_live_review", "d1028_post_live_review")):
        expected = ROOT_BINDINGS[role]
        require((design[key].get("path"), design[key].get("bytes"), design[key].get("sha256")) == expected, f"D1028 {key} binding drift")
    require(design["pre_live_review"].get("status") == "STRICT_PASS" and design["post_live_review"].get("status") == "STRICT_PASS", "D1028 review status drift")
    edit = audit.get("stacks_edit", {})
    require((edit.get("postimage", {}).get("bytes"), edit.get("postimage", {}).get("sha256")) == ROOT_BINDINGS["cohomology_tex"][1:] and edit.get("new_block", {}).get("byte_identical_to_candidate") is True and edit.get("new_block", {}).get("exact_occurrences") == 1, "D1028 live edit drift")
    pdf = audit.get("pdf_build", {})
    require((pdf.get("postimage", {}).get("bytes"), pdf.get("postimage", {}).get("sha256")) == ROOT_BINDINGS["cohomology_pdf"][1:] and pdf.get("successful_exit_code") == 0, "D1028 PDF build drift")
    require(audit.get("visual_qa", {}).get("status") == "STRICT_PASS" and audit.get("visual_qa", {}).get("defects") == [], "D1028 visual QA drift")
    scanner = audit.get("shared_scanner_probe", {})
    require(scanner.get("status") == "PASS_BYTE_IDENTICAL_REPLAY" and scanner.get("oracle_path") == scanner_contract()["oracle_path"] and scanner.get("replay_path") == scanner_contract()["replay_path"], "D1028 scanner state/path drift")
    require(scanner.get("counts") == {"tex_files": 119, "labels": 22113, "official_tags_joined": 21437, "topics": 13, "topic_candidates": 1287, "direct_topic_coverage": 13, "warnings": 685, "errors": 0} and scanner.get("inventory") == {"files": 6, "bytes_each": EXPECTED_SCAN_TOTAL_BYTES}, "D1028 scanner count/inventory drift")
    require(scanner.get("files") == {name: {"bytes": value[0], "sha256": value[1]} for name, value in EXPECTED_SCAN.items()}, "D1028 scanner file identity drift")
    require(scanner.get("new_label_row") == {"full_label": "cohomology-lemma-coherent-equivariant-analytic-extension-classes", "physical_line": 3633, "source_line": 20529, "row_bytes_with_lf": 297, "row_sha256_with_lf": "F33486888B565CC9B6A47DF23D83E2DFA8B71579DC0142FDE7A21C764485DC6D", "text_sha256": "DC5B7775DD09B49DD737F2E6C9752E962CE1387CF3577E97B57B22369319F55D"}, "D1028 scanner label row drift")

    reviews = {role: E.strict_json(ROOT / ROOT_BINDINGS[role][0]) for role in ("parent_review_12", "parent_review_35")}
    for role, review in reviews.items():
        require(review.get("schema") == "tohoku-parent-section-mapping-only-review-v1" and review.get("status") == "STRICT_PASS", f"{role} state drift")
        expected_units = [unit for _, unit, source_role in DECISION_ORDER if source_role == role]
        sections = review.get("parent_sections")
        require(isinstance(sections, list) and [section.get("unit_id") for section in sections] == expected_units, f"{role} unit order drift")
        for section in sections:
            unit = section["unit_id"]
            spec = MAP_SPECS[unit]
            decision = next(row for row in DECISIONS if row["unit_id"] == unit)
            auth = section.get("authorization", {})
            require(section.get("requested_map_line") == spec["physical_line"] and section.get("verdict") == "MAPPING_ONLY_AUTHORIZED" and section.get("residual_unrepresented_content") is False, f"{unit} parent section verdict drift")
            require(auth.get("new_decision_id") is None and auth.get("action") == "replace" and auth.get("replaces_only") == decision["supersedes"], f"{unit} parent replacement drift")
            require(auth.get("disposition") == decision["disposition"] and auth.get("review_state") == decision["review_state"] and auth.get("stacks_labels_csv") == decision["stacks_labels"] and auth.get("stacks_tags_csv") == OFFICIAL_TAGS[decision["decision_id"]] and auth.get("rationale") == decision["rationale"], f"{unit} parent authorization drift")
            require(auth.get("append_issue") is False and auth.get("append_source_repair") is False and auth.get("source_edit_required") is False, f"{unit} unauthorized append/edit")

    candidate = (ROOT / ROOT_BINDINGS["d1028_candidate"][0]).read_bytes()
    cohomology = (ROOT / "cohomology.tex").read_bytes()
    require(cohomology.count(candidate) == 1 and cohomology.count(b"\\label{lemma-coherent-equivariant-analytic-extension-classes}") == 1, "D1028 candidate/live occurrence drift")
    require((ROOT / "my.bib").read_bytes().count(b"@ARTICLE{Tohoku,") == 1, "Tohoku bibliography key drift")
    return {"execution": execution, "predecessor": predecessor, "root": root_records, "canonical": canonical_records}


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    if oracle_surface:
        require({path.name for path in root.iterdir() if path.is_file()} == set(EXPECTED_SCAN) and not any(path.is_dir() for path in root.iterdir()), f"scanner oracle surface drift: {root}")
    for name, expected in EXPECTED_SCAN.items():
        E.require_identity(root / name, expected, f"{root.name}/{name}")
    check = E.strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [] and check.get("counts") == EXPECTED_SCAN_COUNTS and len(check.get("warnings", [])) == 685, "r70 scanner state/count drift")
    require(check.get("tex_sha256", {}).get("cohomology.tex") == ROOT_BINDINGS["cohomology_tex"][2], "r70 scanner cohomology binding drift")
    _, rows = E.load_csv(root / "stx.csv")
    label = "cohomology-lemma-coherent-equivariant-analytic-extension-classes"
    row = E.one_row(rows, "full_label", label, "r70 scanner D1028 label")
    require(row["file"] == "cohomology.tex" and row["line"] == "20529" and row["tag"] == "" and row["text_sha256"] == "DC5B7775DD09B49DD737F2E6C9752E962CE1387CF3577E97B57B22369319F55D", "r70 D1028 label row drift")
    require(E.line_identity(root / "stx.csv", 3633) == (297, "F33486888B565CC9B6A47DF23D83E2DFA8B71579DC0142FDE7A21C764485DC6D"), "r70 D1028 stx row identity drift")
    labels = {item["full_label"] for item in rows}
    required = {item for decision in DECISIONS for item in decision["stacks_labels"].split(";") if item}
    require(required <= labels, "r70 authorized label missing from scanner")
    old_labels = {item["full_label"] for item in E.load_csv(E.SOURCE / "stx.csv")[1]}
    require(label not in old_labels, "D1028 label unexpectedly present in r69")
    return check


def verify_oracles() -> dict[str, Any]:
    require(E.ORACLE.is_dir() and not E.ORACLE.is_symlink() and E.ORACLE_REPLAY.is_dir() and not E.ORACLE_REPLAY.is_symlink(), "D1028 scanner oracle/replay missing or unsafe")
    verify_scan(E.ORACLE, oracle_surface=True)
    verify_scan(E.ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((E.ORACLE / name).read_bytes() == (E.ORACLE_REPLAY / name).read_bytes(), f"D1028 scanner replay differs: {name}")
    return {
        "oracle": {name: E.record(E.ORACLE / name, f"tmp/d1028_scan_probe_r1/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: E.record(E.ORACLE_REPLAY / name, f"tmp/d1028_scan_probe_replay_r1/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def verify_tool_stage(root: Path) -> None:
    require(root.is_dir() and not root.is_symlink(), "missing or unsafe raw r70 stage")
    require({path.name for path in root.iterdir() if path.is_file()} == E.PAYLOAD and not any(path.is_dir() for path in root.iterdir()), "raw r70 stage surface drift")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "raw r70 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"raw inherited r70 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "raw r70 decision drift")
    E.require_identity(root / "map.csv", EXPECTED_TOOL_MAP, "raw r70 map-tool output")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "raw r70 STATUS drift")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [] and mcheck.get("counts") == EXPECTED_COUNTS and len(mcheck.get("warnings", [])) == 685, "raw r70 mapping state/count drift")


def normalize_tool_map(root: Path) -> None:
    verify_tool_stage(root)
    fields, raw_rows = E.load_csv(root / "map.csv")
    reader = csv.DictReader(io.StringIO(expected_map_bytes().decode("utf-8"), newline=""))
    expected_rows = [dict(row) for row in reader]
    require(reader.fieldnames == fields and len(raw_rows) == len(expected_rows), "r70 normalization schema drift")
    deltas: list[tuple[str, str, str, str]] = []
    for raw, expected in zip(raw_rows, expected_rows):
        require(raw["unit_id"] == expected["unit_id"], "r70 normalization row-order drift")
        for field in fields:
            if raw[field] != expected[field]:
                deltas.append((raw["unit_id"], field, raw[field], expected[field]))
    require({(unit, field) for unit, field, _, _ in deltas} == {(unit, "stacks_tags") for unit in TOOL_TAG_ORDER_UNITS} and len(deltas) == 4, "r70 normalization delta scope drift")
    for _, _, raw_tags, expected_tags in deltas:
        require(set(raw_tags.split(";")) == set(expected_tags.split(";")) and len(raw_tags.split(";")) == len(set(raw_tags.split(";"))), "r70 normalization tag-set drift")
    temporary = root / ".map-authorized-order.tmp"
    require(not temporary.exists(), "r70 normalization temporary path exists")
    E.exclusive_write(temporary, expected_map_bytes())
    temporary.replace(root / "map.csv")
    E.require_identity(root / "map.csv", EXPECTED_PROJECTED["map.csv"], "normalized r70 map")


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"missing or unsafe r70 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == E.PAYLOAD | ({"r70-check.json"} if receipt_mode else set()) and not any(path.is_dir() for path in root.iterdir()), "r70 output surface drift")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r70 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv"):
        require((root / name).read_bytes() == (E.SOURCE / name).read_bytes(), f"inherited r70 payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes() and (root / "map.csv").read_bytes() == expected_map_bytes(), "r70 decision/map drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r70 STATUS drift")
    E.require_identity(root / "ucand.csv", EXPECTED_R69_FILES["ucand.csv"], "r70/ucand.csv")
    verify_scan(root)
    mcheck = E.strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [] and mcheck.get("counts") == EXPECTED_COUNTS and len(mcheck.get("warnings", [])) == 685, "r70 mapping state/count drift")
    _, decisions = E.load_csv(root / "dec.csv")
    _, issues = E.load_csv(root / "issues.csv")
    _, mapping = E.load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1063)] and decisions[-11:] == DECISIONS, "r70 decision sequence/tail drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r70 issue sequence drift")
    decisions_by_unit = {row["unit_id"]: row for row in DECISIONS}
    for unit, spec in MAP_SPECS.items():
        selected = E.one_row(mapping, "unit_id", unit, "r70 map")
        decision = decisions_by_unit[unit]
        require(selected["decision_id"] == decision["decision_id"] and selected["disposition"] == decision["disposition"] and selected["review_state"] == decision["review_state"], f"r70 target state drift: {unit}")
        require(selected["stacks_labels"] == decision["stacks_labels"] and selected["stacks_tags"] == OFFICIAL_TAGS[decision["decision_id"]] and selected["source_loc"] == spec["source_loc"], f"r70 target label/tag/locator drift: {unit}")
        require(E.line_identity(root / "map.csv", spec["physical_line"]) == spec["successor_row"], f"r70 target map row identity drift: {unit}")
    deltas = E.map_row_delta()
    require(len(deltas) == 64 and {row["unit_id"] for row in deltas} == set(MAP_SPECS), "r70 map delta cardinality/scope drift")
    fields_by_unit = {unit: {row["field"] for row in deltas if row["unit_id"] == unit} for unit in MAP_SPECS}
    require(fields_by_unit == EXPECTED_CHANGED_FIELDS, "r70 changed-field projection drift")
    remaining = sum(1 for row in mapping if row["disposition"] in {"existing_weaker", "extend_existing", "new_section", "new_statement"})
    require(remaining == 4, "r70 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1062,
        "decisions_appended": [row["decision_id"] for row in DECISIONS],
        "issues_appended": [],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 685, "errors": 0},
        "remaining_gap_class_dispositions": 4,
        "source_repairs_appended": 0,
        "mapping_closures_appended": 11,
        "map_delta": {"changed_units": 11, "changed_fields": 64, "unchanged_units": 980},
        "semantic_inventory_generation": "sem/r18",
        "source_change": "D1028_ADMITTED_COHOMOLOGY_LEMMA_PLUS_TEN_MAPPING_ONLY_PARENT_CLOSURES",
        "scanner_payload_change": "D1028_ONE_NEW_UNTAGGED_COHOMOLOGY_LABEL",
    }
    if receipt_mode:
        require(E.strict_json(root / "r70-check.json") == receipt_payload(root, result), "r70 receipt replay mismatch")
    return result


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    records = external["root"]
    return {
        "schema": "tohoku-stacks-mapping-successor-r70-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalization": {
            "D1028": {
                "audit": records["audit_d1028"],
                "design": records["d1028_design"],
                "candidate": records["d1028_candidate"],
                "reviews": [records["d1028_pre_live_review"], records["d1028_post_live_review"]],
                "parent_reviews": [records["parent_review_12"], records["parent_review_35"]],
                "live_source": records["cohomology_tex"],
                "live_pdf": records["cohomology_pdf"],
                "build_support": [records[key] for key in ("cohomology_aux", "cohomology_bbl", "cohomology_blg", "cohomology_log", "cohomology_out", "cohomology_toc")],
                "visual_rasters": [records[f"page_{page}"] for page in (198, 199, 200, 201, 245, 246, 247)],
                "change_class": "one_admitted_live_lemma_plus_ten_mapping_only_parent_closures",
            },
            "parent_live_sources": [records[key] for key in ("coherent_tex", "derived_tex", "etale_cohomology_tex", "homology_tex", "injectives_tex", "modules_tex", "sheaves_tex", "topology_tex")],
            "bibliography": records["bibliography"],
        },
        "source_chain": external["canonical"],
        "scanner_oracle": oracles["oracle"],
        "scanner_replay": oracles["replay"],
        "deltas": dict(deltas),
        "files": E.output_records(root),
        "nonclaims": [
            "D001052 closes only the coherent analytic equivariant extension-class unit.",
            "D001053-D001062 aggregate only the direct-child coverage frozen in the two parent reviews and change no child disposition.",
            "No issue, source repair, D1030 or D1031 decision, GAGA comparison, release, publication, DOI, remote freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def configure_engine() -> None:
    E.SOURCE = ROOT / "tohoku_r69"
    E.TARGET = ROOT / "tohoku_r70"
    E.STAGE = ROOT / ".tohoku-r70-txn"
    E.ORACLE = ROOT / "tmp" / "d1028_scan_probe_r1"
    E.ORACLE_REPLAY = ROOT / "tmp" / "d1028_scan_probe_replay_r1"
    E.CONTRACT_PATH = CONTRACT_PATH
    E.CONTRACT_ID = CONTRACT_ID
    E.EXPECTED_R60_RECEIPT = EXPECTED_R69_RECEIPT
    E.EXPECTED_R60_FILES = EXPECTED_R69_FILES
    E.EXPECTED_SCAN = EXPECTED_SCAN
    E.EXPECTED_SCAN_COUNTS = EXPECTED_SCAN_COUNTS
    E.EXPECTED_PROJECTED = EXPECTED_PROJECTED
    E.EXPECTED_APPEND_ROWS = {"decision": EXPECTED_DECISION_APPEND}
    E.EXPECTED_COUNTS = EXPECTED_COUNTS
    E.STATUS_BYTES = STATUS_BYTES
    E.DECISION = DECISIONS[-1]
    E.STACKS_INPUTS = {"cohomology_tex": ROOT_BINDINGS["cohomology_tex"]}
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
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r70 target or stage already exists")
    print(json.dumps({"schema": "tohoku-r70-scanner-oracle-v1", "status": "PASS_REPLAY", "errors": [], "scanner_oracles": verify_oracles(), "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 685, "errors": 0}}, indent=2, sort_keys=True))


def preflight() -> None:
    require(not E.TARGET.exists() and not E.STAGE.exists(), "r70 target or stage already exists")
    external = verify_external()
    oracles = verify_oracles()
    projection = {
        "cfg.json": identity_from_bytes(expected_cfg_bytes()),
        "dec.csv": identity_from_bytes(expected_decision_bytes()),
        "issues.csv": identity_from_bytes(expected_issue_bytes()),
        "map.csv": identity_from_bytes(expected_map_bytes()),
        "STATUS.md": identity_from_bytes(STATUS_BYTES),
    }
    print(json.dumps({"schema": "tohoku-r70-static-input-audit-v1", "status": "PASS", "errors": [], "external": external, "scanner_oracles": oracles, "projection": projection, "decisions": [row["decision_id"] for row in DECISIONS], "issue": None, "source_repair": None, "remaining_gaps": 4}, indent=2, sort_keys=True))


def execute() -> None:
    if E.TARGET.exists():
        replay()
        return
    if E.STAGE.exists():
        verify_external()
        verify_oracles()
        verify_tool_stage(E.STAGE)
    else:
        E.build_stage()
        verify_tool_stage(E.STAGE)
    normalize_tool_map(E.STAGE)
    deltas = verify_stage(E.STAGE)
    E.exclusive_write(E.STAGE / "r70-check.json", E.json_bytes(receipt_payload(E.STAGE, deltas)))
    verify_stage(E.STAGE, receipt_mode=True)
    require(not E.TARGET.exists(), "r70 target appeared before promotion")
    E.STAGE.rename(E.TARGET)
    try:
        verify_stage(E.TARGET, receipt_mode=True)
    except BaseException as exc:
        if E.TARGET.exists() and not E.STAGE.exists():
            E.TARGET.rename(E.STAGE)
        raise RuntimeError("post-promotion r70 replay failed; target rolled back") from exc
    print(json.dumps({"schema": "tohoku-r70-transaction-result-v1", "status": "PASS_COMMITTED", "errors": [], "target": "tohoku_r70", "receipt": E.record(E.TARGET / "r70-check.json"), "remaining_gaps": 4}, indent=2, sort_keys=True))


def replay() -> None:
    require(E.TARGET.is_dir() and not E.TARGET.is_symlink() and not E.STAGE.exists(), "r70 target/stage state invalid")
    result = verify_stage(E.TARGET, receipt_mode=True)
    print(json.dumps({"schema": "tohoku-r70-replay-v1", "status": "PASS_REPLAY", "errors": [], "receipt": E.record(E.TARGET / "r70-check.json"), "deltas": result}, indent=2, sort_keys=True))


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
