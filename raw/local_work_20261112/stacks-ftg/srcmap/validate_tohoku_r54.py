#!/usr/bin/env python3
"""Independent bounded validator for the no-overwrite Tohoku r54 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r53"
TARGET = ROOT / "tohoku_r54"
STAGE = ROOT / ".tohoku-r54-txn"
R53_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r53.py"
EXPECTED_R53_VALIDATOR = (
    47440,
    "32A1034F21CA79F5C695339E18BA64449CA6B601670C6561A64AB40112781B81",
)
D1011_AUDIT = ROOT / "D1011_FORMALIZATION_CHECK.json"
# Frozen only after the final audit was sealed. Do not replace this with a
# dynamically discovered identity.
EXPECTED_D1011_AUDIT: tuple[int, str] | None = (
    26909,
    "2681A171FDA816DAC6B96916C51DC705BE596DC00B93C2F943C205F5DA246C38",
)
DESIGN = ROOT / "tmp" / "d1011_mapping_design.json"
EXPECTED_DESIGN = (
    8047,
    "2DAAC51DFD5039C6F1B47B277BED34FECA5D76CEFB44BDE1045FB0365E2DBA4E",
)
DESIGN_AUDIT = ROOT / "tmp" / "d1011_design_audit.json"
EXPECTED_DESIGN_AUDIT = (
    6027,
    "74D76A31F65848F8B995E31CB5221427603EADB5B04A08157527E4DBCC64E327",
)
EXPECTED_D1011_AUDIT_CONTRACT: dict[str, object] | None = {
    "schema": "tohoku-stacks-d1011-formalization-check-v1",
    "formalization_id": "D1011",
    "overall_result": "STRICT_PASS",
    "predicate_ids": [f"P{number:03d}" for number in range(1, 13)],
}
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)

PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r19"
AUTHORITY_PART_I = PROJECT / "authority_snapshot" / "jstage_part_I_9_2_119.pdf"
AUTHORITY_PART_II = PROJECT / "authority_snapshot" / "jstage_part_II_9_3_185.pdf"
EXPECTED_AUTHORITY_PART_I = (
    7305283,
    "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF",
)
EXPECTED_AUTHORITY_PART_II = (
    3984260,
    "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53",
)
SCAN_ORACLE = ROOT / "tmp" / "d1011_scan"

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXECUTION_ROLES = {
    "driver": ("srcmap/start_build_tohoku_r54.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
    "bootstrap": ("srcmap/start_build_tohoku_r54.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
    "builder": ("srcmap/build_tohoku_r54.py", "read_hash_compile_and_exec_same_payload"),
    "validator": ("srcmap/validate_tohoku_r54.py", "independent_same_bytes_stage_and_receipt_replay"),
}

EXPECTED_RUNTIME = {
    "fga/__pycache__/mkidx.cpython-313.pyc": (21123, "A78A1E45C6EB3960139B1D2A8AF42E5B10768034F0A87274448EBA69779BD424"),
    "fga/__pycache__/mkmap.cpython-313.pyc": (26471, "1AA6B79FFE873AB6C2E58FF2A9826DE6FDB6B1DD69A8D3473FD5F56168F2077D"),
    "fga/mkidx.py": (14844, "4425B5D021B3E35371DEBB567881697F88DF6F533ACFC9783A749CE1A5176A6B"),
    "fga/mkmap.py": (22213, "7281F57EC7439E00431F2962DF9A6944779294955A9C4369615FFF04318B0053"),
    "srcmap/intake.py": (9923, "CFD53B71649BEF84A166397AA18E39AC5E4EDF00DD860142B2936F886AB080B1"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "tags/tags": (991506, "C5C7017FB5C50B60295B30801CA1B5BAB8F5B379F61B084D8219441938125FCF"),
}

EXPECTED_SOURCE = {
    "STATUS.md": (1208, "C6D8834BE3F1612EAA0576F05240CEA3D365CEA7A959A7A9E55E8D86E0AEC587"),
    "cfg.json": (5151, "10FC41C2DDE6B23B12B6E816DEA07B72A9D1FFF18AC4A45F55D22FF769E9CE53"),
    "check.json": (80068, "DE603D525A2F84DEC79A18D8044FCEC1F0933D43886720D64BE31052F8CD0CAE"),
    "dec.csv": (375251, "84639B0A99BDDC58980FEEA5E221D249B3B898956DA79F4D41DEFE79297C71D9"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (31413, "C9E2B573A63D834205AC8B2714A0E32230309AFBDD22FA0764F9A8831DF65503"),
    "map.csv": (479894, "7BF8C6794D743ACE1334F5979B820E955C70C14537F0B00A0E6A679376668BAE"),
    "mcheck.json": (69896, "AA378FE65E548E7AC0174F24F8750B89269FF7162AA43E746274B28BB2FB5825"),
    "r53-check.json": (51359, "A8034901EAD767CF98BEE95F28E509539D86EA999FC649C5439981117DA140B6"),
    "stx.csv": (5281636, "A6A16E837DF3B59C348CB88348FA9FC88F6C0703B78AF97FBACFA7B8254CFEC1"),
    "tcand.csv": (489206, "C07DE868C2A467B75DB00C31DE10A6AE5C1AD5F71D629641CF1840B151FDB22A"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SOURCE_SURFACE = (
    15, 7264882,
    "C01A9BD4874F6B772A6056B3710B105F12B2F7FD402CF25A692B6A29A20D4932",
)
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14, 7213523,
    "06EE71F372E5D975E73186C3F39C8EFF4BFDA4BBF70FB8D58C7BE28733F22017",
)

EXPECTED_SEM = {
    "README.md": (2585, "66D4CF92728AF7FF10E82CDFD97AFCD9D26B55CE9FBC985932FFBCD597DD64B4"),
    "bib.csv": (10422, "93F5A934ADDE0CD92BBB21AF70EFD81BA128CCD2EDF51EB19428B83437EC3516"),
    "catalog.csv": (772, "FC0D201FB3BE414D132EC10ED4D00FF2DE16B6F2C90BEADF72213B597113AA20"),
    "edges.csv": (261660, "5B924BF4E9D0E7CAFF51D3C75D0C85045E985AE21152744ABD38929A87E622D5"),
    "idmap.csv": (473, "977D4A8F59A9642D58926DED8BB600079863AE6AF3F1F532806E83A9AB645BEA"),
    "manifest.json": (36480, "CED21E8761F781885600C609683DAA2110232012EEF742C657386655CBC4FAC6"),
    "nodes.csv": (585600, "301172BC3D1DD0D4D518E14B96C6E24A380060F31A09987AAE8EC74812DC80A0"),
    "objects.csv": (106319, "82FF34C19C6D17D80DC3A617FD106ED324099CC9D0F2FE752757D0642ED31999"),
    "occ.csv": (515084, "2F657244FB211F4B5680DFDFC247167BCFD3C011F622930CC409872DEF3370BB"),
    "pages.csv": (23686, "E813C410B0A2AE53B4A787FD6C66A74225021E3A0FE22AD10CA2ED0C29807B0D"),
    "refdec.csv": (2313, "6AC5E23C3D4ADA0ABB1427E0533C3033E13B63C28A654A9C7E74A057A045FFA2"),
    "refs.csv": (161519, "2BB0DC3356C0C4B18E82F7C168334D450DF541586EE89F94FB254C3296ACDE3D"),
    "resid.csv": (6415, "DDF53E58E21C7A5BF60C54ADC5EB9EB420B717246F1C69F294BBA5E358A38430"),
    "stacks.csv": (11777, "E13EFA405B525D69BFF38256601E4AF64D22FA3075F3A95AB3DFB78C15CFD060"),
    "subjects.csv": (2133, "A77A81831F752BA21701B150C13C51325E511B2FD5DFC76EED135FE3EDEEB026"),
    "terms.csv": (325587, "6D93CBBD2D6CF3E354FE90DC51605ACD9C7B0932CEF216FB9D606AD97D666E5D"),
    "validation.json": (5946, "61D05C5E62515F097CDF098412CD93B394CE8F9A9C616943DCB1B1AB7C4302B1"),
    "xwork.csv": (2446, "7BC42D7026C34AD8B1A111353E0810378F1DB9D1284BAD4C5C34D509D57B9EBB"),
}
EXPECTED_SEM_SURFACE = (
    18, 2061217,
    "58DEFA91A60771FB427AB152394CA5BB0D9B289F632F735FD4BE0E68361B649F",
)
EXPECTED_SEM_PAYLOAD_SURFACE = (
    16, 2018791,
    "A0BC270B0F26F9E8E26515FCDDE49E5BBEEEE3D6A370CBEAD275B727A1D6497F",
)

EXPECTED_READER = {
    "build/v068c3r18/build.json": (32685, "287CF9B793BE34598878AD63546B081C27ACEE10C722AF82FBDE03251C92EADB"),
    "qa/v68r40/check.json": (10374, "9969A37D8CDDE716A29C03EF268C5394A13F967BD4C706A0EB8F59CA9695769F"),
    "qa/v68r40/structural.json": (13015, "352C82546CA0E6110267718F5DCC413CCC5099C70B7ACFD4764A2A8EAD664A00"),
    "qa/v68r40/page-inventory.csv": (28257, "CFCBD2BBF9DCCBCFA8C36B802D5266DEB84990E90130A01A06C61AFE90C32AEE"),
    "output/pdf/en-p119-221-v068c3r18.pdf": (1381057, "58A7F14A50D92CA0EAF9EEC04CE3399D4282144FF618C4887318C962CC9A5DB9"),
    "output/pdf/fr-p119-221-v068c3r18.pdf": (1417469, "24EA55FFA0CA94CBD089053B5A0BA2495E2553F798561DB059E77D4F6F724429"),
}

EXPECTED_ORACLE_OUTPUTS = {
    "stx.csv": (5283396, "5E22D3B8B976E5BD845BA0CF69D7AB7685C619D39CDEB53DADCF9A269798BB9D"),
    "tcand.csv": (488729, "4AA8FDD23C221B7663B1FDB5B61F7F6F4B65BEA89346D2881713C5A5AFDB8DAC"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "check.json": (80879, "798607A517735BC50C77356894D9089D9218DC0A2B5D49DB073347C455615EDD"),
}
EXPECTED_STAGE_SCAN_OUTPUTS = {
    **EXPECTED_ORACLE_OUTPUTS,
    "check.json": (80879, "F12E14AF22CC0DFE1BCDD33151E0C3505DC260AAF80D3E65A567C8D968F00F22"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22087,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1286,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1030,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 374,
        "existing_stronger": 41,
        "existing_weaker": 6,
        "extend_existing": 13,
        "historical_reference": 33,
        "new_section": 5,
        "new_statement": 11,
        "structural_only": 424,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 30,
    "unit_candidates": 0,
    "units": 991,
}

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r53 dossier is preserved exactly; D001028 through D001030 are the only ledger appends, and issues.csv is retained byte-for-byte.\n"
    "- The three decisions map the p. 193 neighbourhood-colimit spectral sequences, their conditional stalk comparison, and the completed substantive section 4.3 surface to the exact D1011 labels.\n"
    "- The r53 unit inventory and all 30 resolved source issues remain byte-stable; no issue or source-repair row is appended.\n"
    "- The exact independently audited sem/r19 and reader v068c3r18/QA v68r40 evidence remain bound.\n"
    "- The scanner indexes the same exact 119 top-level TeX files; stx.csv, tcand.csv, and tmap.csv match the D1011 oracle byte-for-byte, and check.json differs only in four dossier-relative r51-to-r54 SHA keys.\n"
    "- There are 1030 decisions, 679 decided units, 659 warnings, no errors, and 35 gap-class dispositions remain.\n"
    "- The quotient spectral sequence uses the admitted Tor_a^R(S,M) repair; no unconditional Ext/filtered-colimit interchange or right-Noetherian variant is claimed.\n"
    "- GitHub is temporarily unavailable under the current direct report; no GitHub or Git operation is attempted.\n"
    "- No selector, release, publication, remote-freshness, DOI, rights, or whole-paper completion claim is made.\n"
).encode("utf-8")

NONCLAIMS = [
    "No Git command, GitHub action, recursive workspace scan, cleanup audit, or watcher is executed by this mapping successor.",
    "The scanner is confined to the exact 119 top-level TeX filenames in the D1011 oracle.",
    "Exactly D001028 through D001030 are appended; the r53 decision prefix is byte-identical.",
    "No issue or source-repair row is appended; r54 issues.csv is byte-identical to r53 issues.csv.",
    "The r53 unit inventory is retained byte-for-byte and sem/r19 is bound as independently sealed semantic evidence.",
    "D1011 does not formalize the p. 193 HLC example or the subsequent failure example.",
    "No unconditional Ext/filtered-colimit interchange is claimed.",
    "The left-Noetherian finite-module specialization is not replaced by a right-sided variant.",
    "The quotient hyper-Ext system is claimed functorially from E2 onward, not from an unconstructed E1 page.",
    "Only the inherited section label cohomology-section-ext carries official tag 0BQP; no official tag is claimed for the two new D1011 lemma labels.",
    "No live selector or pointer is changed.",
    "No release, publication, upload, DOI, Zenodo, rights, remote-freshness, or whole-paper completion claim is made.",
    "35 Tohoku gap-class dispositions remain.",
]

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()

def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)

def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}

def aggregate(records: list[dict[str, object]], case_sensitive: bool = False) -> str:
    key = (lambda value: str(value["name"])) if case_sensitive else (
        lambda value: str(value["name"]).casefold()
    )
    raw = b"".join(
        f"{item['name']}\0{item['bytes']}\0{item['sha256']}\n".encode("utf-8")
        for item in sorted(records, key=key)
    )
    return digest(raw)

def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)

def is_reparse(path: Path) -> bool:
    return os.name == "nt" and bool(path.stat(follow_symlinks=False).st_file_attributes & 0x400)

def require_plain_file(path: Path) -> None:
    require(path.is_file() and not path.is_symlink() and not is_reparse(path), f"Expected plain file: {path}")

def require_plain_directory(path: Path) -> None:
    require(path.is_dir() and not path.is_symlink() and not is_reparse(path), f"Expected plain directory: {path}")

def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require_plain_file(path)
    require(identity(path) == expected, f"Identity drift: {path}")

def no_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result

def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    require(b"\r" not in data and data.endswith(b"\n"), f"Noncanonical JSON: {path}")
    value = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicate_pairs)
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value

def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    raw = path.read_bytes().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(raw, newline=""))
    require(reader.fieldnames is not None, f"Missing CSV header: {path}")
    return list(reader.fieldnames), [dict(row) for row in reader]

def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")

def expected_runtime() -> dict[str, tuple[int, str]]:
    return dict(EXPECTED_RUNTIME)

def load_design() -> dict:
    require_identity(DESIGN, EXPECTED_DESIGN)
    require_identity(DESIGN_AUDIT, EXPECTED_DESIGN_AUDIT)
    design_audit = strict_json(DESIGN_AUDIT)
    require(design_audit.get("schema") == "tohoku-stacks-d1011-design-audit-v1", "D1011 design-audit schema drift")
    require(design_audit.get("status") == "STRICT_PASS" and design_audit.get("errors") == [], "D1011 design audit not STRICT_PASS")
    require(design_audit.get("formalization_id") == "D1011", "D1011 design-audit ID drift")
    design = strict_json(DESIGN)
    require(design.get("schema") == "tohoku-stacks-d1011-mapping-design-v1", "D1011 design schema drift")
    require(design.get("status") == "STRICT_PASS" and design.get("formalization_id") == "D1011", "D1011 design not STRICT_PASS")
    require(design.get("planned_successor") == "tohoku_r54", "D1011 planned successor drift")
    decisions = design.get("planned_decisions")
    require(isinstance(decisions, list) and len(decisions) == 3, "D1011 planned decision count drift")
    require([row.get("decision_id") for row in decisions] == ["D001028", "D001029", "D001030"], "D1011 decision IDs drift")
    require([row.get("supersedes") for row in decisions] == ["D000476", "D000490", "D000332"], "D1011 superseded decisions drift")
    require(all(row.get("action") == "replace" and row.get("disposition") == "existing_equivalent" for row in decisions), "D1011 decision action/disposition drift")
    canonical = json.dumps(decisions, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
    canon_meta = design.get("canonical_decision_rows", {})
    require((len(canonical), digest(canonical)) == (2259, "BAD064FA7667B3F068BBC47B00CAA47680A9C5CB256600761DB978F5D52F6066"), "D1011 canonical decision rows drift")
    require((int(canon_meta.get("bytes", -1)), str(canon_meta.get("sha256"))) == (len(canonical), digest(canonical)), "D1011 canonical decision receipt drift")
    expected_counts = dict(design.get("expected_postsuccessor_counts", {}))
    require(expected_counts.pop("remaining_gap_class_dispositions_before", None) == 38, "D1011 predecessor gap count drift")
    require(expected_counts.pop("remaining_gap_class_dispositions_after", None) == 35, "D1011 projected gap count drift")
    require(expected_counts == EXPECTED_MAPPING_COUNTS, "D1011 projected mapping counts drift")
    require(design.get("expected_map_delta") == {
        "changed_units": 3,
        "unchanged_units": 988,
        "changed_fields_per_unit": ["decision_id", "disposition", "rationale", "review_state", "stacks_labels", "stacks_tags"],
        "tag_behavior": {"D001028": "", "D001029": "", "D001030": "0BQP"},
        "tag_control": "Only D001030 receives official Stacks tag 0BQP; the two new local lemma targets receive no official tag.",
    }, "D1011 projected map delta drift")
    require(design.get("predecessor_projection") == {
        "dossier": "tohoku_r53",
        "dec_csv_bytes": EXPECTED_SOURCE["dec.csv"][0],
        "dec_csv_sha256": EXPECTED_SOURCE["dec.csv"][1],
        "map_csv_bytes": EXPECTED_SOURCE["map.csv"][0],
        "map_csv_sha256": EXPECTED_SOURCE["map.csv"][1],
        "issues_csv_bytes": EXPECTED_SOURCE["issues.csv"][0],
        "issues_csv_sha256": EXPECTED_SOURCE["issues.csv"][1],
        "status_note": "These are frozen r53 projections and become the exact predecessor identities only if the sealed r53 dossier matches them byte for byte.",
    }, "D1011 predecessor projection drift")
    require(design.get("contingent_successor_identities") == {
        "condition": "The sealed r53 dec.csv, map.csv, and issues.csv identities must exactly equal predecessor_projection.",
        "dec_csv_bytes": 377152,
        "dec_csv_sha256": "1B9A6A95DC3C50C04E5754AA7E8890827111D51350E124D6E0220C23FA77B679",
        "map_csv_bytes": 480773,
        "map_csv_sha256": "B6D7482C57477FB8360514487AC16FD2298DD05B3CE1AC76BAC8E5F0220A0F60",
        "issues_csv_bytes": 31413,
        "issues_csv_sha256": "C9E2B573A63D834205AC8B2714A0E32230309AFBDD22FA0764F9A8831DF65503",
        "issues_csv_change": "none",
    }, "D1011 contingent successor identities drift")
    repair = design.get("existing_source_repair", {})
    require(repair.get("new_issue_row_required") is False and repair.get("new_source_repair_required") is False, "D1011 unexpectedly requests issue/source-repair append")
    return design

def decision_rows() -> list[dict[str, str]]:
    return [dict(row) for row in load_design()["planned_decisions"]]

def expected_decision_bytes() -> bytes:
    design = load_design()
    fields, rows = load_csv(SOURCE / "dec.csv")
    require(fields == design["decision_csv_schema"], "r53 decision schema drift")
    require([row["decision_id"] for row in rows] == [f"D{number:06d}" for number in range(1, 1028)], "r53 decision sequence drift")
    suffix = csv_bytes(fields, decision_rows()).split(b"\n", 1)[1]
    meta = design["canonical_decision_rows"]
    require((len(suffix), digest(suffix)) == (int(meta["csv_suffix_bytes"]), str(meta["csv_suffix_sha256"])), "D1011 decision suffix drift")
    output = (SOURCE / "dec.csv").read_bytes() + suffix
    contingent = design["contingent_successor_identities"]
    require((len(output), digest(output)) == (int(contingent["dec_csv_bytes"]), str(contingent["dec_csv_sha256"])), "D1011 projected dec.csv drift")
    return output

def expected_issue_bytes() -> bytes:
    design = load_design()
    fields, rows = load_csv(SOURCE / "issues.csv")
    require([row["issue_id"] for row in rows] == [f"I{number:06d}" for number in range(1, 31)], "r53 issue sequence drift")
    require(design["contingent_successor_identities"]["issues_csv_change"] == "none", "D1011 issue-change contract drift")
    output = (SOURCE / "issues.csv").read_bytes()
    contingent = design["contingent_successor_identities"]
    require((len(output), digest(output)) == (int(contingent["issues_csv_bytes"]), str(contingent["issues_csv_sha256"])), "D1011 projected issues.csv drift")
    return output

def expected_map_rows() -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = load_csv(SOURCE / "map.csv")
    by_unit = {row["unit_id"]: row for row in rows}
    require(len(by_unit) == len(rows) == 991, "r53 map unit surface drift")
    tags = load_design()["expected_map_delta"]["tag_behavior"]
    for decision in decision_rows():
        unit_id = decision["unit_id"]
        old = by_unit[unit_id]
        require(old["decision_id"] == decision["supersedes"], f"Superseded decision drift: {unit_id}")
        replacement = dict(old)
        replacement.update({
            "decision_id": decision["decision_id"],
            "disposition": decision["disposition"],
            "review_state": decision["review_state"],
            "stacks_labels": decision["stacks_labels"],
            "stacks_tags": tags[decision["decision_id"]],
            "rationale": decision["rationale"],
        })
        by_unit[unit_id] = replacement
    projected = [by_unit[row["unit_id"]] for row in rows]
    raw = csv_bytes(fields, projected)
    contingent = load_design()["contingent_successor_identities"]
    require((len(raw), digest(raw)) == (int(contingent["map_csv_bytes"]), str(contingent["map_csv_sha256"])), "D1011 projected map.csv identity drift")
    return fields, projected

def map_delta(new_rows: list[dict[str, str]]) -> dict[str, object]:
    _, old_rows = load_csv(SOURCE / "map.csv")
    old_by = {row["unit_id"]: row for row in old_rows}
    new_by = {row["unit_id"]: row for row in new_rows}
    changed: dict[str, list[str]] = {}
    for unit_id in old_by:
        fields = sorted(key for key in old_by[unit_id] if old_by[unit_id][key] != new_by[unit_id][key])
        if fields:
            changed[unit_id] = fields
    expected_units = {row["unit_id"] for row in decision_rows()}
    require(set(changed) == expected_units, "Unauthorized r54 map mutation")
    required_fields = load_design()["expected_map_delta"]["changed_fields_per_unit"]
    require(all(fields == required_fields for fields in changed.values()), "r54 map changed-field set drift")
    return {"changed_units": 3, "changes": changed, "unchanged_units": 988}

def expected_execution_attestation() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for role, (relative, contract) in EXECUTION_ROLES.items():
        path = ROOT / relative
        require_plain_file(path)
        size, sha256 = identity(path)
        result[role] = {"path": relative, "bytes": size, "sha256": sha256, "contract": contract}
    return result

def verify_predecessor() -> dict[str, object]:
    require_identity(R53_VALIDATOR, EXPECTED_R53_VALIDATOR)
    require_plain_directory(SOURCE)
    entries = list(SOURCE.iterdir())
    require(not any(path.is_dir() for path in entries), "Unexpected r53 predecessor subdirectory")
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r53 predecessor file surface drift")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    complete = (len(records), sum(int(row["bytes"]) for row in records), aggregate(records))
    require(complete == EXPECTED_SOURCE_SURFACE, "r53 predecessor complete aggregate drift")
    payload = [row for row in records if row["name"] != "r53-check.json"]
    payload_surface = (len(payload), sum(int(row["bytes"]) for row in payload), aggregate(payload))
    require(payload_surface == EXPECTED_SOURCE_PAYLOAD_SURFACE, "r53 predecessor payload aggregate drift")
    receipt = strict_json(SOURCE / "r53-check.json")
    require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r53-v1", "r53 receipt schema drift")
    require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r53 receipt not PASS")
    require(receipt.get("files") == [record(SOURCE / name) for name in sorted(PAYLOAD)], "r53 receipt payload records drift")
    deltas = receipt.get("deltas", {})
    require(deltas.get("decisions") == 1027 and deltas.get("remaining_gap_class_dispositions") == 38, "r53 predecessor count drift")
    require(deltas.get("mapping_counts", {}).get("source_issues") == 30, "r53 source-issue count drift")
    return {
        "name": "tohoku_r53",
        "receipt": record(SOURCE / "r53-check.json", "tohoku_r53/r53-check.json"),
        "validator": record(R53_VALIDATOR, "srcmap/validate_tohoku_r53.py"),
        "complete_surface": {"files": complete[0], "bytes": complete[1], "aggregate_sha256": complete[2]},
        "payload_surface": {"files": payload_surface[0], "bytes": payload_surface[1], "aggregate_sha256": payload_surface[2]},
        "decision_count": 1027,
        "source_issue_count": 30,
        "remaining_gap_class_dispositions": 38,
        "independent_sealed_surface_replay": "PASS",
        "historical_live_validator_replay": "NOT_APPLICABLE_AFTER_D1011_TEX_SUCCESSOR",
    }

def verify_runtime() -> dict[str, object]:
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    for relative, expected in sorted(EXPECTED_RUNTIME.items()):
        require_identity(ROOT / relative, expected)
    return {
        "python": record(EXPECTED_PYTHON, str(EXPECTED_PYTHON)),
        "dependencies": {relative: {"bytes": expected[0], "sha256": expected[1]} for relative, expected in sorted(EXPECTED_RUNTIME.items())},
    }

def verify_semantic() -> dict[str, object]:
    require_plain_directory(SEM)
    entries = list(SEM.iterdir())
    require(not any(path.is_dir() for path in entries), "Unexpected sem/r19 subdirectory")
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SEM), "sem/r19 file surface drift")
    records = []
    for name, expected in sorted(EXPECTED_SEM.items()):
        require_identity(SEM / name, expected)
        records.append(record(SEM / name))
    surface = (len(records), sum(int(row["bytes"]) for row in records), aggregate(records, case_sensitive=True))
    require(surface == EXPECTED_SEM_SURFACE, "sem/r19 complete aggregate drift")
    payload = [row for row in records if row["name"] not in {"manifest.json", "validation.json"}]
    payload_surface = (len(payload), sum(int(row["bytes"]) for row in payload), aggregate(payload, case_sensitive=True))
    require(payload_surface == EXPECTED_SEM_PAYLOAD_SURFACE, "sem/r19 payload aggregate drift")
    manifest = strict_json(SEM / "manifest.json")
    validation = strict_json(SEM / "validation.json")
    require(manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v19", "sem/r19 manifest schema drift")
    require(validation.get("schema") == "tohoku-semantic-local-successor-validation-v19", "sem/r19 validation schema drift")
    require(validation.get("status") == "PASS" and validation.get("errors") == [], "sem/r19 validation not PASS")
    require(validation.get("manifest_sha256") == EXPECTED_SEM["manifest.json"][1], "sem/r19 manifest binding drift")
    counts = {
        "nodes": len(load_csv(SEM / "nodes.csv")[1]),
        "occurrences": len(load_csv(SEM / "occ.csv")[1]),
        "edges": len(load_csv(SEM / "edges.csv")[1]),
        "references": len(load_csv(SEM / "refs.csv")[1]),
    }
    require(counts == {"nodes": 991, "occurrences": 1036, "edges": 1479, "references": 440}, "sem/r19 stable counts drift")
    return {
        "generation": "sem/r19", "validation_status": "PASS",
        "file_count": surface[0], "bytes": surface[1], "aggregate_sha256": surface[2],
        "manifest_payload_surface": {"file_count": payload_surface[0], "bytes": payload_surface[1], "aggregate_sha256": payload_surface[2]},
        "stable_node_ids": 991, "stable_surfaces": counts, "files": records,
    }

def _record_path(item: dict, base: Path = ROOT) -> Path:
    path = Path(str(item["path"]))
    return path if path.is_absolute() else base / path

def _require_record(item: dict, path: Path) -> None:
    require_identity(path, (int(item["bytes"]), str(item["sha256"])))


def _strict_jsonl(path: Path) -> list[dict[str, object]]:
    raw = path.read_bytes()
    require(b"\r" not in raw and raw.endswith(b"\n"), f"Noncanonical JSONL: {path}")
    rows: list[dict[str, object]] = []
    for number, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        require(bool(line), f"Blank JSONL line {number}: {path}")
        value = json.loads(line, object_pairs_hook=no_duplicate_pairs)
        require(isinstance(value, dict), f"Expected JSONL object at line {number}: {path}")
        rows.append(value)
    return rows


def _fragment_bytes(item: dict) -> bytes:
    lines = item.get("lines")
    require(isinstance(lines, list) and all(isinstance(line, str) for line in lines), "D1011 fragment lines drift")
    raw = ("\n".join(lines) + "\n").encode("utf-8")
    require((len(raw), digest(raw)) == (int(item["bytes"]), str(item["sha256"])), "D1011 fragment receipt drift")
    return raw


def _audit_referenced_paths(audit: dict) -> list[Path]:
    paths = []
    for key in ("english_p193", "corrected_french_p193"):
        paths.append(_record_path(audit["corrected_source"][key]))
    for key in ("family", "root_corrections"):
        paths.append(_record_path(audit["existing_source_repair"][key]))
    for key in ("design_audit", "mapping_design"):
        paths.append(_record_path(audit["design_inputs"][key]))
    for key in ("revised_candidate", "live_source"):
        paths.append(_record_path(audit["formalization_artifacts"][key]))
    for key in ("aux", "out", "toc", "pdf", "log"):
        paths.append(_record_path(audit["fixed_point_build"][key]))
    paths.extend(_record_path(item) for item in audit["pdf_and_log_qa"]["visual_audit"]["files"])
    for generation in ("baseline", "final"):
        block = audit["scanner_oracle"][generation]
        directory = Path(str(block["path"]))
        paths.extend(directory / name for name in block["files"])
    return paths


def verify_d1011_audit() -> dict[str, object]:
    require(
        EXPECTED_D1011_AUDIT is not None and EXPECTED_D1011_AUDIT_CONTRACT is not None,
        "D1011_FORMALIZATION_CHECK.json is not yet sealed; r54 launch remains blocked",
    )
    require_identity(D1011_AUDIT, EXPECTED_D1011_AUDIT)
    audit = strict_json(D1011_AUDIT)
    contract = EXPECTED_D1011_AUDIT_CONTRACT
    require(audit.get("schema") == contract["schema"], "D1011 audit schema drift")
    require(audit.get("formalization_id") == contract["formalization_id"], "D1011 audit ID drift")
    require(audit.get("overall_result") == contract["overall_result"], "D1011 audit result drift")
    require(audit.get("errors") == [], "D1011 audit errors are not empty")
    require(audit.get("serialization") == {
        "encoding": "UTF-8 without BOM", "line_endings": "LF", "indentation": 2, "terminal_newline": True,
    }, "D1011 audit serialization contract drift")

    predicates = audit.get("predicates")
    require(isinstance(predicates, list), "D1011 predicate ledger missing")
    require([row.get("id") for row in predicates] == contract["predicate_ids"], "D1011 predicate sequence drift")
    require(all(row.get("result") == "PASS" for row in predicates), "D1011 predicate failure")
    require(all(row.get("expected") == row.get("observed") for row in predicates), "D1011 predicate replay mismatch")
    require(audit.get("predicate_summary") == {
        "total": 12,
        "passed": 12,
        "failed": 0,
        "rule": "overall_result is STRICT_PASS iff every predicate replays PASS from the bound live files",
    }, "D1011 predicate summary drift")

    for path in _audit_referenced_paths(audit):
        require_plain_file(path)

    corrected = audit["corrected_source"]
    english = corrected["english_p193"]
    french = corrected["corrected_french_p193"]
    english_path = _record_path(english)
    french_path = _record_path(french)
    _require_record(english, english_path)
    _require_record(french, french_path)
    term = str(corrected["corrected_initial_term"]).encode("utf-8")
    occurrences = {
        "english": english_path.read_bytes().count(term),
        "french": french_path.read_bytes().count(term),
    }
    require(occurrences == corrected["corrected_initial_term_occurrences"] == {"english": 1, "french": 1}, "D1011 corrected term occurrence drift")

    repair = audit["existing_source_repair"]
    family = repair["family"]
    roots = repair["root_corrections"]
    family_path = _record_path(family)
    roots_path = _record_path(roots)
    _require_record(family, family_path)
    _require_record(roots, roots_path)
    family_rows = [row for row in _strict_jsonl(family_path) if row.get("decision_id") == family["decision_id"]]
    require(len(family_rows) == family["exact_id_records"] == 1, "D1011 family repair multiplicity drift")
    require(family_rows[0].get("state") == family["state"] == "active", "D1011 family repair state drift")
    root_rows = _strict_jsonl(roots_path)
    for decision_id in roots["decision_ids"]:
        matches = [row for row in root_rows if row.get("decision_id") == decision_id]
        require(len(matches) == roots["exact_id_records_each"] == 1, f"D1011 root repair multiplicity drift: {decision_id}")
        require(matches[0].get("state") == roots["required_state"] == "active", f"D1011 root repair state drift: {decision_id}")
    require(repair.get("new_source_repair_required") is False, "D1011 unexpected new source repair")

    design = load_design()
    design_inputs = audit["design_inputs"]
    for key, expected_path in (("design_audit", DESIGN_AUDIT), ("mapping_design", DESIGN)):
        item = design_inputs[key]
        require(_record_path(item).resolve() == expected_path.resolve(), f"D1011 {key} path drift")
        _require_record(item, expected_path)
        bound = strict_json(expected_path)
        require(bound.get("schema") == item["schema"] and bound.get("status") == item["status"] == "STRICT_PASS", f"D1011 {key} contract drift")

    artifacts = audit["formalization_artifacts"]
    candidate_item = artifacts["revised_candidate"]
    live_item = artifacts["live_source"]
    candidate_path = _record_path(candidate_item)
    live_path = _record_path(live_item)
    _require_record(candidate_item, candidate_path)
    _require_record(live_item, live_path)
    candidate = candidate_path.read_bytes()
    live = live_path.read_bytes()
    require(candidate.endswith(b"\n") is candidate_item["terminal_lf"], "D1011 candidate terminal LF drift")
    require(live.endswith(b"\n") is live_item["terminal_lf"], "D1011 live terminal LF drift")
    require(len(candidate.splitlines()) == candidate_item["lines"] == 282, "D1011 candidate line count drift")
    require(len(live.splitlines()) == live_item["lines"] == 24283, "D1011 live line count drift")

    revision = design_inputs["layout_only_revision"]
    old_fragment = _fragment_bytes(revision["design_fragment"])
    new_fragment = _fragment_bytes(revision["revised_fragment"])
    require(candidate.count(new_fragment) == revision["revised_fragment_occurrences"] == 1, "D1011 revised fragment multiplicity drift")
    reconstructed = candidate.replace(new_fragment, old_fragment, 1)
    reconstruction = revision["reverse_reconstruction"]
    reconstructed_identity = (len(reconstructed), digest(reconstructed), len(reconstructed.splitlines()))
    require(reconstructed_identity == (reconstruction["bytes"], reconstruction["sha256"], reconstruction["lines"]), "D1011 design candidate reconstruction drift")
    require({"bytes": reconstruction["bytes"], "sha256": reconstruction["sha256"], "lines": reconstruction["lines"]} == design_inputs["design_candidate_identity"], "D1011 design candidate identity binding drift")

    insertion = artifacts["exact_insertion"]
    require(live.count(candidate) == insertion["candidate_occurrences_in_live"] == 1, "D1011 live candidate multiplicity drift")
    offset = live.index(candidate)
    start_line = live[:offset].count(b"\n") + 1
    end_line = start_line + len(candidate.splitlines()) - 1
    require((start_line, end_line) == (insertion["start_line"], insertion["end_line"]) == (15130, 15411), "D1011 insertion line range drift")
    extracted = b"".join(live.splitlines(keepends=True)[start_line - 1:end_line])
    require(extracted == candidate and insertion["extracted_line_array_exact"] is True, "D1011 extracted candidate drift")
    predecessor = live[:offset] + live[offset + len(candidate):]
    predecessor_item = insertion["predecessor_after_exact_removal"]
    require((len(predecessor), digest(predecessor)) == (predecessor_item["bytes"], predecessor_item["sha256"]), "D1011 predecessor reconstruction drift")
    require(len(live) == len(predecessor) + len(candidate) and insertion["live_size_equals_predecessor_plus_candidate"] is True, "D1011 insertion byte arithmetic drift")

    tex_audit = artifacts["tex_audit"]
    candidate_text = candidate.decode("utf-8")
    live_text = live.decode("utf-8")
    labels = re.findall(r"\\label\{([^}]+)\}", candidate_text)
    require(labels == tex_audit["labels"] and len(labels) == tex_audit["labels_count"] == 7, "D1011 candidate label ledger drift")
    require(len(set(labels)) == len(labels) and tex_audit["labels_unique"] is True, "D1011 candidate label uniqueness drift")
    require(all(candidate_text.count(f"\\label{{{label}}}") == tex_audit["candidate_definitions_each"] == 1 for label in labels), "D1011 candidate label definition drift")
    require(all(live_text.count(f"\\label{{{label}}}") == tex_audit["live_definitions_each"] == 1 for label in labels), "D1011 live label definition drift")
    references = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", candidate_text)
    live_labels = set(re.findall(r"\\label\{([^}]+)\}", live_text))
    unresolved = sorted(set(references) - live_labels)
    require((len(references), len(set(references)), len(unresolved)) == (tex_audit["total_references"], tex_audit["unique_references"], tex_audit["unresolved_references"]), "D1011 reference audit drift")
    stack: list[str] = []
    begin_count = end_count = nesting_errors = 0
    for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", candidate_text):
        operation, environment = match.groups()
        if operation == "begin":
            begin_count += 1
            stack.append(environment)
        else:
            end_count += 1
            if not stack or stack.pop() != environment:
                nesting_errors += 1
    nesting_errors += len(stack)
    require((begin_count, end_count, nesting_errors) == (tex_audit["begin_environments"], tex_audit["end_environments"], tex_audit["environment_nesting_errors"]), "D1011 TeX environment audit drift")
    display_count = candidate_text.count("$$")
    require(display_count == tex_audit["display_math_delimiters"] == 32 and display_count % 2 == 0 and tex_audit["display_math_parity_even"] is True, "D1011 display-math audit drift")

    fixed = audit["fixed_point_build"]
    for key in ("aux", "out", "toc", "pdf", "log"):
        _require_record(fixed[key], _record_path(fixed[key]))
    aux_text = _record_path(fixed["aux"]).read_text(encoding="utf-8")
    for label, page in fixed["aux_label_pages"].items():
        match = re.search(rf"^\\newlabel\{{{re.escape(label)}\}}\{{\{{[^}}]*\}}\{{(\d+)\}}", aux_text, re.MULTILINE)
        require(match is not None and int(match.group(1)) == page, f"D1011 AUX page drift: {label}")
    seam = re.search(r"^\\newlabel\{section-cohomology-group-actions\}\{\{[^}]*\}\{(\d+)\}", aux_text, re.MULTILINE)
    require(seam is not None and int(seam.group(1)) == fixed["next_section_page"] == 148, "D1011 adjacent-section seam page drift")
    log_text = _record_path(fixed["log"]).read_text(encoding="utf-8", errors="strict")
    require(log_text.count(fixed["fixed_point_log_evidence"]) == 1, "D1011 fixed-point log evidence drift")

    log_audit = audit["pdf_and_log_qa"]["log_audit"]
    require(len(re.findall(r"LaTeX Warning: Reference .* undefined", log_text)) == log_audit["undefined_references"] == 0, "D1011 undefined-reference audit drift")
    require(len(re.findall(r"LaTeX Warning: Citation .* undefined", log_text)) == log_audit["undefined_citations"] == 0, "D1011 undefined-citation audit drift")
    rerun = len(re.findall(r"Rerun to get|Label\(s\) may have changed|Please \(re\)run", log_text, re.IGNORECASE))
    require(rerun == log_audit["rerun_requests"] == 0, "D1011 rerun audit drift")
    fatal = len(re.findall(r"(?m)^!|Fatal error occurred|Emergency stop", log_text, re.IGNORECASE))
    require(fatal == log_audit["fatal_or_latex_errors"] == 0, "D1011 fatal-log audit drift")
    multiply_defined = len(re.findall(r"multiply defined", log_text, re.IGNORECASE))
    require(multiply_defined == log_audit["multiply_defined"] == 0, "D1011 multiply-defined audit drift")
    box_lines = [line for line in log_text.splitlines() if re.match(r"^(Over|Under)full \\[hv]box", line)]
    overfull = sum(line.startswith("Overfull") for line in box_lines)
    underfull = sum(line.startswith("Underfull") for line in box_lines)
    located: list[tuple[int, int]] = []
    for line in box_lines:
        range_match = re.search(r"at lines (\d+)--(\d+)", line)
        point_match = re.search(r"at line (\d+)", line)
        if range_match:
            located.append((int(range_match.group(1)), int(range_match.group(2))))
        elif point_match:
            point = int(point_match.group(1))
            located.append((point, point))
    audit_range = log_audit["range"]
    intersecting = sum(not (end < audit_range["start"] or start > audit_range["end"]) for start, end in located)
    require((len(box_lines), overfull, underfull, len(located), intersecting) == (
        log_audit["total_box_diagnostics"], log_audit["overfull"], log_audit["underfull"],
        log_audit["source_located_box_diagnostics"], log_audit["d1011_intersecting_box_diagnostics"],
    ), "D1011 box diagnostic audit drift")
    require(log_audit["result"] == "STRICT_PASS", "D1011 log audit not STRICT_PASS")

    parser_audit = audit["pdf_and_log_qa"]["parser"]
    pdf_path = _record_path(fixed["pdf"])
    pdf_raw = pdf_path.read_bytes()
    require(pdf_raw.startswith(str(parser_audit["pdf_header"]).encode("ascii")), "D1011 PDF header drift")
    require(pdf_raw.count(b"%%EOF") == parser_audit["eof_marker_count"] == 1, "D1011 PDF EOF drift")
    require(len(pdf_raw) - (pdf_raw.rfind(b"%%EOF") + len(b"%%EOF")) == parser_audit["trailing_whitespace_bytes"] == 1, "D1011 PDF trailing-byte drift")
    startxref_match = re.search(rb"startxref\s+(\d+)\s+%%EOF\s*$", pdf_raw)
    require(startxref_match is not None and int(startxref_match.group(1)) == parser_audit["startxref"], "D1011 PDF startxref drift")
    require(0 <= parser_audit["startxref"] < len(pdf_raw) and parser_audit["startxref_target_valid"] is True, "D1011 PDF startxref target drift")
    import pypdf
    require(pypdf.__version__ == parser_audit["version"] == "6.12.2", "D1011 pypdf version drift")
    pdf_reader = pypdf.PdfReader(io.BytesIO(pdf_raw), strict=True)
    require(not pdf_reader.is_encrypted and parser_audit["encrypted"] is False, "D1011 PDF encryption drift")
    pages = list(pdf_reader.pages)
    content_lengths = []
    texts = []
    boxes = []
    rotations = []
    for page in pages:
        contents = page.get_contents()
        content_lengths.append(len(contents.get_data()) if contents is not None else 0)
        texts.append(page.extract_text() or "")
        boxes.append([int(value) for value in page.mediabox])
        rotations.append(int(page.rotation or 0))
    require(len(pages) == fixed["pdf"]["pages"] == parser_audit["pages"] == parser_audit["page_tree_count"] == parser_audit["pages_parsed"] == 234, "D1011 PDF page count drift")
    require(len(content_lengths) == parser_audit["content_streams_parsed"] and sum(content_lengths) == parser_audit["content_decoded_bytes"], "D1011 PDF content parse drift")
    require(len(texts) == parser_audit["text_pages_parsed"] and sum(map(len, texts)) == parser_audit["text_chars"] and all(texts) is parser_audit["all_pages_have_text"], "D1011 PDF text parse drift")
    require(all(box == parser_audit["uniform_media_box"] for box in boxes), "D1011 PDF media-box drift")
    require(sorted(set(rotations)) == parser_audit["rotations"] == [0], "D1011 PDF rotation drift")
    require(sum(len(rows) for rows in pdf_reader.xref.values()) == parser_audit["xref_objects_parsed"], "D1011 PDF xref object drift")
    require(sorted(str(key) for key in pdf_reader.trailer.keys()) == parser_audit["trailer_keys"], "D1011 PDF trailer key drift")
    require(int(pdf_reader.trailer["/Size"]) == parser_audit["trailer_size"] and str(pdf_reader.trailer["/Root"]["/Type"]) == parser_audit["root_type"], "D1011 PDF trailer/root drift")
    require(all(parser_audit[key] == 0 for key in ("page_errors", "content_stream_errors", "text_errors", "box_errors", "rotation_errors", "xref_errors")), "D1011 PDF parser error ledger drift")
    require(parser_audit["result"] == "STRICT_PASS", "D1011 PDF parse not STRICT_PASS")

    visual = audit["pdf_and_log_qa"]["visual_audit"]
    render_records = []
    for item in visual["files"]:
        render_path = _record_path(item)
        _require_record(item, render_path)
        render_records.append((render_path.name, int(item["bytes"]), str(item["sha256"])))
    manifest = "\n".join(f"{name},{size},{sha256}" for name, size, sha256 in sorted(render_records)).encode("utf-8")
    require(digest(manifest) == visual["manifest_sha256"], "D1011 visual manifest drift")
    require([item["page"] for item in visual["files"]] == visual["pages"] == [144, 145, 146, 147, 148, 149], "D1011 visual page ledger drift")
    require(sum(size for _, size, _ in render_records) == visual["total_bytes"] and len(render_records) == 6, "D1011 visual render surface drift")
    require((visual["width"], visual["height"], visual["dpi"], visual["corrected_display_page"]) == (1530, 1980, 180, 146), "D1011 visual geometry drift")
    require(all(value == 0 for value in visual["checks"].values()) and visual["result"] == "STRICT_PASS", "D1011 visual audit not STRICT_PASS")

    scanner = audit["scanner_oracle"]
    loaded_checks = {}
    for generation in ("baseline", "final"):
        block = scanner[generation]
        directory = Path(str(block["path"]))
        require_plain_directory(directory)
        for name, item in block["files"].items():
            _require_record(item, directory / name)
        check = strict_json(directory / "check.json")
        loaded_checks[generation] = check
        require(check.get("status") == "PASS" and check.get("errors") == [], f"D1011 {generation} scanner not PASS")
        counts = check["counts"]
        normalized_counts = {
            "labels": counts["labels"], "official_tags_joined": counts["official_tags_joined"],
            "tex_files": counts["tex_files"], "topic_candidates": counts["topic_candidates"],
            "topic_coverage_direct": counts["topic_coverage"]["direct"], "topics": counts["topics"],
            "warnings": len(check["warnings"]), "errors": len(check["errors"]),
        }
        require(normalized_counts == block["counts"], f"D1011 {generation} scanner counts drift")
        require(check["tex_sha256"].get("cohomology.tex") == block["cohomology_tex_sha256"], f"D1011 {generation} cohomology hash drift")
    final_check = loaded_checks["final"]
    baseline_check = loaded_checks["baseline"]
    require(final_check["counts"] == EXPECTED_SCAN_COUNTS and len(final_check["warnings"]) == 659, "D1011 final scanner contract drift")
    for filename, sha256 in final_check["tex_sha256"].items():
        tex_path = ROOT / filename
        require_plain_file(tex_path)
        require(digest(tex_path.read_bytes()) == sha256, f"D1011 final TeX identity drift: {filename}")
    new_warnings = set(final_check["warnings"]) - set(baseline_check["warnings"])
    removed_warnings = set(baseline_check["warnings"]) - set(final_check["warnings"])
    require(new_warnings == set(scanner["new_warnings"]) and removed_warnings == set(scanner["removed_warnings"]) == set(), "D1011 scanner warning-set delta drift")
    require(len(new_warnings) == scanner["deltas"]["warnings"] == 7, "D1011 scanner warning delta count drift")
    _, final_stx = load_csv(Path(str(scanner["final"]["path"])) / "stx.csv")
    _, baseline_stx = load_csv(Path(str(scanner["baseline"]["path"])) / "stx.csv")
    final_labels = [row["full_label"] for row in final_stx]
    baseline_labels = [row["full_label"] for row in baseline_stx]
    require(all(final_labels.count(label) == scanner["new_scanner_label_occurrences_each"] == 1 and baseline_labels.count(label) == 0 for label in scanner["new_scanner_labels"]), "D1011 new scanner label row drift")
    require(len(final_labels) - len(baseline_labels) == scanner["deltas"]["labels"] == 7, "D1011 scanner label delta drift")
    for name in scanner["unchanged_artifacts"]:
        require(identity(Path(str(scanner["baseline"]["path"])) / name) == identity(Path(str(scanner["final"]["path"])) / name), f"D1011 scanner unchanged artifact drift: {name}")
    for key, filename in (("check.json_bytes", "check.json"), ("stx.csv_bytes", "stx.csv"), ("tcand.csv_bytes", "tcand.csv"), ("tmap.csv_bytes", "tmap.csv"), ("topics.csv_bytes", "topics.csv")):
        before = int(scanner["baseline"]["files"][filename]["bytes"])
        after = int(scanner["final"]["files"][filename]["bytes"])
        require(after - before == scanner["deltas"][key], f"D1011 scanner byte delta drift: {filename}")

    closures = audit["intended_mapping_closures"]
    expected_closures = [
        {key: row[key] for key in ("decision_id", "supersedes", "unit_id", "disposition", "stacks_labels")}
        for row in design["planned_decisions"]
    ]
    require(closures == expected_closures, "D1011 audit closures differ from mapping design")
    design_audit = strict_json(DESIGN_AUDIT)
    normalized_planned = []
    for row in design_audit["planned_mapping"]:
        normalized_planned.append({
            "decision_id": row["decision_id"], "supersedes": row["supersedes"],
            "unit_id": row["unit_id"], "disposition": row["disposition"],
            "stacks_labels": row.get("primary_label", row.get("primary_labels")),
        })
    require(normalized_planned == closures, "D1011 design-audit closure drift")

    return {
        "receipt": record(D1011_AUDIT, "D1011_FORMALIZATION_CHECK.json"),
        "schema": audit["schema"],
        "formalization_id": "D1011",
        "status": "STRICT_PASS",
        "predicate_summary": audit["predicate_summary"],
        "predicate_results": {row["id"]: row["result"] for row in predicates},
        "corrected_source": {
            "english_p193": record(english_path, str(english_path)),
            "corrected_french_p193": record(french_path, str(french_path)),
        },
        "candidate": record(candidate_path, str(candidate_path)),
        "live_source": record(live_path, str(live_path)),
        "fixed_point_pdf": {**record(pdf_path, str(pdf_path)), "pages": 234},
        "visual_manifest_sha256": visual["manifest_sha256"],
        "scanner_oracle": {name: record(SCAN_ORACLE / name, f"tmp/d1011_scan/{name}") for name in sorted(EXPECTED_ORACLE_OUTPUTS)},
        "intended_mapping_closures": closures,
        "independent_live_replay": "STRICT_PASS",
    }

def verify_reader() -> dict[str, object]:
    for relative, expected in EXPECTED_READER.items():
        require_identity(PROJECT / relative, expected)
    build = strict_json(PROJECT / "build/v068c3r18/build.json")
    qa = strict_json(PROJECT / "qa/v68r40/check.json")
    structural = strict_json(PROJECT / "qa/v68r40/structural.json")
    require(build.get("status") == "PASS" and build.get("errors") == [], "reader v068c3r18 build not PASS")
    require(qa.get("status") == "PASS" and qa.get("errors") == [], "reader QA v68r40 not PASS")
    require(qa.get("reader_revision") == "v068c3r18" and qa.get("qa_revision") == "v68r40", "reader QA revision drift")
    require(
        structural.get("status") == "STRUCTURAL_PASS_VISUAL_PENDING"
        and structural.get("errors") == [],
        "reader structural QA receipt drift",
    )
    require(qa.get("p220_visual_review", {}).get("status") == "PASS", "reader p220 visual review drift")
    require(qa.get("conclusion", {}).get("reader_successor_accepted") is True, "reader QA conclusion drift")
    for language in ("english", "french"):
        block = qa["p220_visual_review"][language]
        for group in ("predecessor_rasters", "successor_rasters"):
            for row in block[group]:
                item = row["raster"]
                _require_record(item, _record_path(item, PROJECT))
    replay = qa.get("deterministic_build_replay", {})
    for rows in replay.get("logs_replayed", {}).values():
        for item in rows:
            _require_record(item, _record_path(item, PROJECT))
    return {
        "reader_revision": "v068c3r18", "qa_revision": "v68r40",
        "build_receipt": record(PROJECT / "build/v068c3r18/build.json", "build/v068c3r18/build.json"),
        "qa_receipt": record(PROJECT / "qa/v68r40/check.json", "qa/v68r40/check.json"),
        "structural_receipt": record(PROJECT / "qa/v68r40/structural.json", "qa/v68r40/structural.json"),
        "page_inventory": record(PROJECT / "qa/v68r40/page-inventory.csv", "qa/v68r40/page-inventory.csv"),
        "english_pdf": record(PROJECT / "output/pdf/en-p119-221-v068c3r18.pdf", "output/pdf/en-p119-221-v068c3r18.pdf"),
        "french_pdf": record(PROJECT / "output/pdf/fr-p119-221-v068c3r18.pdf", "output/pdf/fr-p119-221-v068c3r18.pdf"),
        "deterministic_build_replay": replay,
        "p220_visual_review": qa["p220_visual_review"],
    }

def verify_external() -> dict[str, object]:
    d1011 = verify_d1011_audit()
    require_identity(AUTHORITY_PART_I, EXPECTED_AUTHORITY_PART_I)
    require_identity(AUTHORITY_PART_II, EXPECTED_AUTHORITY_PART_II)
    runtime = verify_runtime()
    predecessor = verify_predecessor()
    semantic = verify_semantic()
    reader = verify_reader()
    return {
        "predecessor": predecessor,
        "formalization_audit": d1011,
        "scanner": {
            "outputs": {name: record(SCAN_ORACLE / name, f"tmp/d1011_scan/{name}") for name in sorted(EXPECTED_ORACLE_OUTPUTS)},
            "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 659, "errors": 0},
        },
        "semantic": semantic,
        "reader": reader,
        "runtime": runtime,
        "authority_inputs": {
            "part_i": record(AUTHORITY_PART_I, "authority_snapshot/jstage_part_I_9_2_119.pdf"),
            "part_ii": record(AUTHORITY_PART_II, "authority_snapshot/jstage_part_II_9_3_185.pdf"),
        },
    }

def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]

def execution_receipt() -> dict[str, object]:
    return {
        "attestation": expected_execution_attestation(),
        "dependencies": {name: {"name": Path(name).name, "bytes": expected[0], "sha256": expected[1]} for name, expected in sorted(expected_runtime().items())},
        "contract": "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback",
    }

def receipt_payload(root: Path, deltas: dict[str, object]) -> dict[str, object]:
    external = verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r54-v1",
        "status": "PASS", "errors": [],
        "predecessor_dossier": external["predecessor"],
        "semantic_source": external["semantic"],
        "formalization_audit": external["formalization_audit"],
        "scanner_oracle": external["scanner"],
        "reader": external["reader"],
        "runtime": external["runtime"],
        "authority_inputs": external["authority_inputs"],
        "execution": execution_receipt(),
        "git": {
            "inspection_performed": False,
            "status": "temporarily_unavailable",
            "reason": "Direct user report: the account was suspended after VPN use and a support ticket is filed; no Git operation is needed for this bounded local successor.",
            "predecessor_receipt": record(SOURCE / "r53-check.json", "tohoku_r53/r53-check.json"),
            "remote_server_freshness_verified": False,
        },
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": NONCLAIMS,
    }

def verify_stage(root: Path, receipt_mode: bool) -> dict[str, object]:
    require_plain_directory(root)
    entries = list(root.iterdir())
    expected_names = PAYLOAD | ({"r54-check.json"} if receipt_mode else set())
    require(not any(path.is_dir() for path in entries), "Unexpected r54 output subdirectory")
    require({path.name for path in entries if path.is_file()} == expected_names, "r54 output surface drift")
    for path in entries:
        require_plain_file(path)

    cfg = strict_json(root / "cfg.json")
    expected_cfg = strict_json(SOURCE / "cfg.json")
    expected_cfg["dossier_id"] = "tohoku_r54"
    require(cfg == expected_cfg, "r54 cfg differs from r53 beyond dossier ID")
    require_identity(root / "cfg.json", (5151, "A64D8392CC980BD9DA9308B975F0946474D8CEAC73AB1E81065E63058F5E3D6D"))
    for name in ("intake.json", "units.csv", "topics.csv", "ucand.csv"):
        require(identity(root / name) == identity(SOURCE / name), f"Unauthorized inherited payload drift: {name}")
    for name, expected in EXPECTED_STAGE_SCAN_OUTPUTS.items():
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    stage_sha = stage_check.get("sha256", {})
    oracle_sha = oracle_check.get("sha256", {})
    require(isinstance(stage_sha, dict) and isinstance(oracle_sha, dict), "Scanner SHA ledger shape drift")
    stage_only = {f"tohoku_r54/{name}" for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv")}
    oracle_only = {f"tohoku_r51/{name}" for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv")}
    require(set(stage_sha) - set(oracle_sha) == stage_only, "r54 scanner SHA path additions drift")
    require(set(oracle_sha) - set(stage_sha) == oracle_only, "r54 scanner SHA path removals drift")
    normalized = dict(stage_sha)
    for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv"):
        normalized[f"tohoku_r51/{name}"] = normalized.pop(f"tohoku_r54/{name}")
    normalized_check = dict(stage_check)
    normalized_check["sha256"] = normalized
    require(normalized_check == oracle_check, "r54 scanner check differs from D1011 oracle beyond four namespace keys")

    dec_raw = (root / "dec.csv").read_bytes()
    require(dec_raw == expected_decision_bytes(), "r54 decision ledger is not exact append-only successor")
    require(dec_raw[:EXPECTED_SOURCE["dec.csv"][0]] == (SOURCE / "dec.csv").read_bytes(), "r54 decision prefix drift")
    _, decisions = load_csv(root / "dec.csv")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1031)], "r54 decision sequence drift")
    require(decisions[-3:] == decision_rows(), "r54 decision suffix rows drift")

    issue_raw = (root / "issues.csv").read_bytes()
    require(issue_raw == expected_issue_bytes(), "r54 issues ledger must be byte-identical to r53")
    require(issue_raw == (SOURCE / "issues.csv").read_bytes(), "r54 issue prefix/full-file drift")
    _, issues = load_csv(root / "issues.csv")
    require([row["issue_id"] for row in issues] == [f"I{number:06d}" for number in range(1, 31)], "r54 issue sequence drift")

    map_fields, mapped = load_csv(root / "map.csv")
    expected_fields, expected_rows = expected_map_rows()
    require(map_fields == expected_fields and mapped == expected_rows, "r54 map differs from independent three-row projection")
    require_identity(root / "map.csv", (480773, "B6D7482C57477FB8360514487AC16FD2298DD05B3CE1AC76BAC8E5F0220A0F60"))
    delta = map_delta(mapped)
    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("schema") == "historical-source-stacks-map-v1", "r54 mcheck schema drift")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r54 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r54 mapping counts drift")
    require(mcheck.get("warnings") == stage_check.get("warnings") and len(mcheck.get("warnings", [])) == 659, "r54 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r54 status narrative drift")
    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_section", "new_statement"))
    require(gap_count == 35, "r54 gap count projection drift")
    result = {
        "status": "PASS", "errors": [],
        "decisions": 1030,
        "decisions_appended": decision_rows(),
        "issues_appended": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 659, "errors": 0},
        "scanner_check_delta": {"changed_fields": ["sha256"], "namespace_keys_only": 4, "normalized_equal": True},
        "map_delta": delta,
        "remaining_gap_class_dispositions": 35,
        "semantic_generation": "sem/r19",
        "inherited_unit_inventory": "BYTE_IDENTICAL_R53",
        "source_repairs_appended": 0,
    }
    if receipt_mode:
        receipt = strict_json(root / "r54-check.json")
        require(receipt == receipt_payload(root, result), "r54 receipt replay mismatch")
    return result

def external_input_paths() -> list[Path]:
    paths = [
        R53_VALIDATOR, D1011_AUDIT, DESIGN, DESIGN_AUDIT,
        EXPECTED_PYTHON, AUTHORITY_PART_I, AUTHORITY_PART_II,
    ]
    require_identity(D1011_AUDIT, EXPECTED_D1011_AUDIT)
    audit = strict_json(D1011_AUDIT)
    paths.extend(_audit_referenced_paths(audit))
    paths.extend(SOURCE / name for name in EXPECTED_SOURCE)
    paths.extend(ROOT / relative for relative in EXPECTED_RUNTIME)
    paths.extend(SEM / name for name in EXPECTED_SEM)
    paths.extend(SCAN_ORACLE / name for name in EXPECTED_ORACLE_OUTPUTS)
    check = strict_json(SCAN_ORACLE / "check.json")
    paths.extend(ROOT / filename for filename in check["tex_sha256"])
    paths.extend(PROJECT / relative for relative in EXPECTED_READER)
    qa = strict_json(PROJECT / "qa/v68r40/check.json")
    for language in ("english", "french"):
        for group in ("predecessor_rasters", "successor_rasters"):
            paths.extend(_record_path(row["raster"], PROJECT) for row in qa["p220_visual_review"][language][group])
    for rows in qa["deterministic_build_replay"]["logs_replayed"].values():
        paths.extend(_record_path(item, PROJECT) for item in rows)
    return list(dict.fromkeys(paths))

def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R54_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r54.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r54.py", "bytes": actual[0], "sha256": actual[1]}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r54 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r54 transaction exists: {STAGE}")
        external = verify_external()
        _, projection = expected_map_rows()
        result = {
            "schema": "tohoku-r54-static-input-audit-v1",
            "status": "PASS", "errors": [], "attestation": attestation,
            "target_absent": True, "stage_absent": True,
            "predecessor": external["predecessor"],
            "formalization_audit": external["formalization_audit"],
            "scanner_oracle": external["scanner"],
            "semantic_source": external["semantic"],
            "reader": external["reader"],
            "runtime": external["runtime"],
            "authority_inputs": external["authority_inputs"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "projected_map_delta": map_delta(projection),
            "projected_remaining_gap_class_dispositions": 35,
            "projected_dec_csv": {"bytes": len(expected_decision_bytes()), "sha256": digest(expected_decision_bytes())},
            "projected_issues_csv": {"bytes": len(expected_issue_bytes()), "sha256": digest(expected_issue_bytes())},
            "launch_authorized": True,
        }
    else:
        result = {"schema": "tohoku-r54-stage-validation-v1", "attestation": attestation, **verify_stage(args.stage.resolve(), args.receipt)}
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
