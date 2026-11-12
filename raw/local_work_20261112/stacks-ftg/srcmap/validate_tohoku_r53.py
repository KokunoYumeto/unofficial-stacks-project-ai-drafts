#!/usr/bin/env python3
"""Independent bounded validator for the no-overwrite Tohoku r53 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r52"
TARGET = ROOT / "tohoku_r53"
STAGE = ROOT / ".tohoku-r53-txn"
R52_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r52.py"
EXPECTED_R52_VALIDATOR = (
    43213,
    "6CB3D35DB2DFDEE1843CCD02B102085BA9C612052764D50DC19C1A1D9554C78C",
)
D1010_AUDIT = ROOT / "D1010_CHECK.json"
EXPECTED_D1010_AUDIT = (
    37425,
    "A73F16F4951CA5E04A6796586D7F522A22343164FC8AC5276CF5E64D4D8AC1E5",
)
DESIGN = ROOT / "tmp" / "d1010_mapping_design.json"
EXPECTED_DESIGN = (
    10091,
    "09990111965AC15BAB4A0855BD1771AB9CB7F2BBF07A1768692EADE46EC9FDFA",
)
FORMALIZATION = ROOT / "tmp" / "d1010_formalization_evidence.json"
EXPECTED_FORMALIZATION = (
    10908,
    "301A3458391FAAC4754DECA03E3C7F5C4B10CB9887B00B0F53FC1144D34994CF",
)
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
SCAN_ORACLE = ROOT / "tmp" / "d1010_scan"

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXECUTION_ROLES = {
    "driver": ("srcmap/start_build_tohoku_r53.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
    "bootstrap": ("srcmap/start_build_tohoku_r53.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
    "builder": ("srcmap/build_tohoku_r53.py", "read_hash_compile_and_exec_same_payload"),
    "validator": ("srcmap/validate_tohoku_r53.py", "independent_same_bytes_stage_and_receipt_replay"),
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
    "STATUS.md": (1320, "20400607D2B4647CD38EDFE10CA78AE2046E0CFA01D9B1F5CD4C3AC5AE5CA076"),
    "cfg.json": (5151, "CB0CEC7B41CA510FE1D19304341C3F26A7D094FBDB26CF90B4F4117A87F5974F"),
    "check.json": (78742, "7D7701B770C6B9B05438D3A1A75B8C561401FEB338465D6F84A67C733BD5D6A0"),
    "dec.csv": (372876, "B3BCF2455FCB0ED4BF94EB6BAC68DD0BB4F4E215E2F562CADC942412DC160024"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (478986, "70D08CFD1899EC0C5337857A8CB07A352FA7C411B6BBE55EA7944796B2D2B0DA"),
    "mcheck.json": (68570, "EAC825E47A29D54BB46F7F67A9AE785EB0C5886A447674EC462A9E846AFAE8F4"),
    "r52-check.json": (26245, "D8E8D6EE5C83ABE8B3ADA89AF34F19EFD5F4BC66B69052280C9B3BBDFEAF3438"),
    "stx.csv": (5278176, "A5535AF7AA7C02780D88DBEAB50417ED0BB7688865AB4A002D7B6656BAD41D14"),
    "tcand.csv": (487516, "7CF3E31793144F7AB87F7A9E79923E7B654E527713C3467823179BA74F224915"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SOURCE_SURFACE = (
    15, 7226917,
    "A0C10FE6A36F40F442841D3C237EB74BFF226DBDF2A506C84CC90C60A301935A",
)
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14, 7200672,
    "AAE89727CE1A5A2D5AFAAFFD7265C0ECED5223928BB285492B99F6C762495661",
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
    "stx.csv": (5281636, "A6A16E837DF3B59C348CB88348FA9FC88F6C0703B78AF97FBACFA7B8254CFEC1"),
    "tcand.csv": (489206, "C07DE868C2A467B75DB00C31DE10A6AE5C1AD5F71D629641CF1840B151FDB22A"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "check.json": (80068, "648438CCAB8D80F28B80E36BFA44378A1655AAB51CD4B0EE347CBA6B2121459B"),
}
EXPECTED_STAGE_SCAN_OUTPUTS = {
    **EXPECTED_ORACLE_OUTPUTS,
    "check.json": (80068, "DE603D525A2F84DEC79A18D8044FCEC1F0933D43886720D64BE31052F8CD0CAE"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22080,
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
    "decisions": 1027,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 371,
        "existing_stronger": 41,
        "existing_weaker": 6,
        "extend_existing": 16,
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
    "- The sealed r52 dossier is preserved exactly; D001024 through D001027 and resolved source issue I000030 are the only ledger appends.\n"
    "- The four decisions map the p. 220 extension-by-zero, filtered spectral-sequence, inductive-system, and filtered-limit comparison units to the two exact D1010 labels at their stated conditional scope.\n"
    "- The r52 unit inventory remains byte-stable, while the exact independently audited sem/r19 complete surface is bound as the semantic successor evidence.\n"
    "- The scanner indexes the same exact 119 top-level TeX files; stx.csv, tcand.csv, and tmap.csv match the D1010 oracle byte-for-byte, and check.json differs only in four dossier-relative r51-to-r53 SHA keys.\n"
    "- All 30 source issues are resolved, 679 units are decided, and 38 gap-class dispositions remain.\n"
    "- The D1010 extension-by-zero acyclicity and paracompactifying-support hypotheses remain explicit; the three group-cohomology criteria do not supply either gate.\n"
    "- GitHub is temporarily unavailable under the current direct report; no GitHub or Git operation is attempted.\n"
    "- No selector, release, publication, remote-freshness, DOI, rights, or whole-paper completion claim is made.\n"
).encode("utf-8")

NONCLAIMS = [
    "No Git command, GitHub action, recursive workspace scan, cleanup audit, or watcher is executed by this mapping successor.",
    "The scanner is confined to the exact 119 top-level TeX filenames in the D1010 oracle.",
    "Exactly D001024 through D001027 are appended; the r52 decision prefix is byte-identical.",
    "Exactly I000030 is appended; the r52 issue prefix is byte-identical.",
    "The r52 unit inventory is retained byte-for-byte and sem/r19 is bound as independently sealed successor evidence.",
    "D1010 remains restricted to abelian G-sheaves and does not claim a module-valued extension.",
    "The neighbourhood hypothesis alone is not claimed to imply extension-by-zero acyclicity or paracompactifying supports.",
    "The three group-cohomology criteria are not claimed to supply either missing derived-functor hypothesis.",
    "No official Stacks tag is claimed for either D1010 decision label.",
    "No live selector or pointer is changed.",
    "No release, publication, upload, DOI, Zenodo, rights, remote-freshness, or whole-paper completion claim is made.",
    "38 Tohoku gap-class dispositions remain.",
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
    design = strict_json(DESIGN)
    require(design.get("schema") == "tohoku-stacks-d1010-mapping-design-v1", "D1010 design schema drift")
    require(design.get("status") == "STRICT_PASS" and design.get("formalization_id") == "D1010", "D1010 design not STRICT_PASS")
    require(design.get("planned_successor") == "tohoku_r53", "D1010 planned successor drift")
    decisions = design.get("planned_decisions")
    require(isinstance(decisions, list) and len(decisions) == 4, "D1010 planned decision count drift")
    require([row.get("decision_id") for row in decisions] == ["D001024", "D001025", "D001026", "D001027"], "D1010 decision IDs drift")
    require([row.get("supersedes") for row in decisions] == ["D000585", "D000648", "D000587", "D000568"], "D1010 superseded decisions drift")
    require(all(row.get("action") == "replace" and row.get("disposition") == "existing_equivalent" for row in decisions), "D1010 decision action/disposition drift")
    canonical = json.dumps(decisions, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
    canon_meta = design.get("canonical_decision_rows", {})
    require((len(canonical), digest(canonical)) == (2852, "7166D021F6B01A9FFDEE2CD47907C34FF98640D49D2F7FD9E6B1AAA8A556643C"), "D1010 canonical decision rows drift")
    require((int(canon_meta.get("bytes", -1)), str(canon_meta.get("sha256"))) == (len(canonical), digest(canonical)), "D1010 canonical decision receipt drift")
    expected_counts = dict(design.get("expected_postsuccessor_counts", {}))
    require(expected_counts.pop("remaining_gap_class_dispositions", None) == 38, "D1010 projected gap count drift")
    require(expected_counts == EXPECTED_MAPPING_COUNTS, "D1010 projected mapping counts drift")
    require(design.get("expected_map_delta") == {
        "changed_units": 4,
        "unchanged_units": 987,
        "changed_fields_per_unit": ["decision_id", "disposition", "rationale", "review_state", "stacks_labels", "stacks_tags"],
    }, "D1010 projected map delta drift")
    issue = design.get("planned_issue_append", {})
    require(issue.get("issue_id") == "I000030" and issue.get("resolution_decision") == "D001024", "D1010 planned issue drift")
    return design


def decision_rows() -> list[dict[str, str]]:
    return [dict(row) for row in load_design()["planned_decisions"]]


def issue_row() -> dict[str, str]:
    item = load_design()["planned_issue_append"]
    fields, _ = load_csv(SOURCE / "issues.csv")
    row = {field: str(item[field]) for field in fields if field in item}
    row["evidence_labels"] = str(item["stacks_labels"])
    require(set(row) == set(fields), "D1010 issue projection schema drift")
    return row


def expected_decision_bytes() -> bytes:
    design = load_design()
    fields, rows = load_csv(SOURCE / "dec.csv")
    require(fields == design["decision_csv_schema"], "r52 decision schema drift")
    require([row["decision_id"] for row in rows] == [f"D{number:06d}" for number in range(1, 1024)], "r52 decision sequence drift")
    suffix = csv_bytes(fields, decision_rows()).split(b"\n", 1)[1]
    meta = design["canonical_decision_rows"]
    require((len(suffix), digest(suffix)) == (int(meta["csv_suffix_bytes"]), str(meta["csv_suffix_sha256"])), "D1010 decision suffix drift")
    output = (SOURCE / "dec.csv").read_bytes() + suffix
    require((len(output), digest(output)) == (int(meta["expected_dec_csv_bytes"]), str(meta["expected_dec_csv_sha256"])), "D1010 projected dec.csv drift")
    return output


def expected_issue_bytes() -> bytes:
    design = load_design()
    fields, rows = load_csv(SOURCE / "issues.csv")
    require([row["issue_id"] for row in rows] == [f"I{number:06d}" for number in range(1, 30)], "r52 issue sequence drift")
    suffix = csv_bytes(fields, [issue_row()]).split(b"\n", 1)[1]
    meta = design["planned_issue_append"]
    require((len(suffix), digest(suffix)) == (int(meta["csv_suffix_bytes"]), str(meta["csv_suffix_sha256"])), "D1010 issue suffix drift")
    output = (SOURCE / "issues.csv").read_bytes() + suffix
    require((len(output), digest(output)) == (int(meta["expected_issues_csv_bytes"]), str(meta["expected_issues_csv_sha256"])), "D1010 projected issues.csv drift")
    return output


def expected_map_rows() -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = load_csv(SOURCE / "map.csv")
    by_unit = {row["unit_id"]: row for row in rows}
    require(len(by_unit) == len(rows) == 991, "r52 map unit surface drift")
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
            "stacks_tags": "",
            "rationale": decision["rationale"],
        })
        by_unit[unit_id] = replacement
    projected = [by_unit[row["unit_id"]] for row in rows]
    raw = csv_bytes(fields, projected)
    meta = load_design()["canonical_decision_rows"]
    require((len(raw), digest(raw)) == (int(meta["expected_map_csv_bytes"]), str(meta["expected_map_csv_sha256"])), "D1010 projected map.csv identity drift")
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
    require(set(changed) == expected_units, "Unauthorized r53 map mutation")
    required_fields = load_design()["expected_map_delta"]["changed_fields_per_unit"]
    require(all(fields == required_fields for fields in changed.values()), "r53 map changed-field set drift")
    return {"changed_units": 4, "changes": changed, "unchanged_units": 987}


def expected_execution_attestation() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for role, (relative, contract) in EXECUTION_ROLES.items():
        path = ROOT / relative
        require_plain_file(path)
        size, sha256 = identity(path)
        result[role] = {"path": relative, "bytes": size, "sha256": sha256, "contract": contract}
    return result


def verify_predecessor() -> dict[str, object]:
    require_identity(R52_VALIDATOR, EXPECTED_R52_VALIDATOR)
    require_plain_directory(SOURCE)
    entries = list(SOURCE.iterdir())
    require(not any(path.is_dir() for path in entries), "Unexpected r52 predecessor subdirectory")
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r52 predecessor file surface drift")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    complete = (len(records), sum(int(row["bytes"]) for row in records), aggregate(records))
    require(complete == EXPECTED_SOURCE_SURFACE, "r52 predecessor complete aggregate drift")
    payload = [row for row in records if row["name"] != "r52-check.json"]
    payload_surface = (len(payload), sum(int(row["bytes"]) for row in payload), aggregate(payload))
    require(payload_surface == EXPECTED_SOURCE_PAYLOAD_SURFACE, "r52 predecessor payload aggregate drift")
    receipt = strict_json(SOURCE / "r52-check.json")
    require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r52-v1", "r52 receipt schema drift")
    require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r52 receipt not PASS")
    require(receipt.get("files") == [record(SOURCE / name) for name in sorted(PAYLOAD)], "r52 receipt payload records drift")
    deltas = receipt.get("deltas", {})
    require(deltas.get("decisions") == 1023 and deltas.get("remaining_gap_class_dispositions") == 42, "r52 predecessor count drift")
    require(deltas.get("mapping_counts", {}).get("source_issues") == 29, "r52 source-issue count drift")
    return {
        "name": "tohoku_r52",
        "receipt": record(SOURCE / "r52-check.json", "tohoku_r52/r52-check.json"),
        "validator": record(R52_VALIDATOR, "srcmap/validate_tohoku_r52.py"),
        "complete_surface": {"files": complete[0], "bytes": complete[1], "aggregate_sha256": complete[2]},
        "payload_surface": {"files": payload_surface[0], "bytes": payload_surface[1], "aggregate_sha256": payload_surface[2]},
        "decision_count": 1023,
        "source_issue_count": 29,
        "remaining_gap_class_dispositions": 42,
        "independent_sealed_surface_replay": "PASS",
        "historical_live_validator_replay": "NOT_APPLICABLE_AFTER_D1010_TEX_AND_SEMANTIC_SUCCESSORS",
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


def verify_formalization() -> dict[str, object]:
    require_identity(FORMALIZATION, EXPECTED_FORMALIZATION)
    evidence = strict_json(FORMALIZATION)
    require(evidence.get("schema") == "tohoku-stacks-d1010-formalization-evidence-v1", "D1010 formalization schema drift")
    require(evidence.get("status") == "STRICT_PASS" and evidence.get("errors") == [], "D1010 formalization not STRICT_PASS")
    require(evidence.get("formalization_id") == "D1010", "D1010 formalization ID drift")
    integration = evidence["integration"]
    for key in ("candidate", "live"):
        item = integration[key]
        _require_record(item, _record_path(item))
    require(integration.get("candidate_byte_sequence_occurrences") == 1, "D1010 candidate multiplicity drift")
    require(integration.get("candidate_and_live_line_arrays_identical") is True, "D1010 line-array replay drift")
    require(integration.get("remove_exact_candidate_reconstructs_predecessor") is True, "D1010 predecessor reconstruction drift")
    labels = evidence.get("labels", [])
    require(len(labels) == 11 and len({row["full_label"] for row in labels}) == 11, "D1010 label surface drift")
    require(evidence.get("mathematical_audit", {}).get("status") == "STRICT_PASS", "D1010 mathematical audit drift")
    build = evidence.get("build_audit", {})
    require(build.get("status") == "STRICT_PASS" and build.get("passes") == 4 and build.get("fixed_point_pass") == 4, "D1010 build/fixed-point audit drift")
    for item in build["artifacts"].values():
        _require_record(item, _record_path(item))
    for item in build["fixed_point_before_after"].values():
        require(item["before_sha256"] == item["after_sha256"], "D1010 fixed-point identity drift")
    pdf = evidence.get("pdf_audit", {})
    require(pdf.get("status") == "STRICT_PASS" and pdf.get("visual_result") == "PASS", "D1010 PDF audit drift")
    require(pdf.get("strict_pages_parsed") == 231 and pdf.get("strict_page_parse_errors") == 0, "D1010 strict PDF parse drift")
    for item in pdf["visual_renders"]:
        _require_record(item, _record_path(item))
    scanner = evidence.get("scanner_audit", {})
    require(scanner.get("status") == "STRICT_PASS" and scanner.get("deterministic_replay_identical") is True, "D1010 scanner audit drift")
    require(scanner.get("counts") == {"labels": 22080, "official_tags_joined": 21437, "tex_files": 119, "topic_candidates": 1286, "topics": 13, "warnings": 652, "errors": 0}, "D1010 scanner counts drift")
    for name, expected in EXPECTED_ORACLE_OUTPUTS.items():
        require_identity(SCAN_ORACLE / name, expected)
        item = scanner["outputs"][name]
        require((int(item["bytes"]), str(item["sha256"])) == expected, f"D1010 scanner receipt drift: {name}")
    check = strict_json(SCAN_ORACLE / "check.json")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "D1010 scanner check counts drift")
    require(check.get("errors") == [] and len(check.get("warnings", [])) == 652, "D1010 scanner warning/error drift")
    tex_hashes = check.get("tex_sha256")
    require(isinstance(tex_hashes, dict) and len(tex_hashes) == 119, "D1010 TeX hash surface drift")
    for filename, sha256 in tex_hashes.items():
        require_identity(ROOT / filename, ((ROOT / filename).stat().st_size, str(sha256)))
    return {
        "receipt": record(FORMALIZATION, "tmp/d1010_formalization_evidence.json"),
        "integration": integration,
        "labels": labels,
        "mathematical_audit": evidence["mathematical_audit"],
        "build_audit": build,
        "pdf_audit": pdf,
        "scanner_audit": scanner,
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


def verify_d1010() -> dict[str, object]:
    require_identity(D1010_AUDIT, EXPECTED_D1010_AUDIT)
    audit = strict_json(D1010_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1010-audit-v1", "D1010 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1010 audit not STRICT_PASS")
    require(audit.get("formalization_id") == "D1010", "D1010 audit ID drift")
    design = load_design()
    mapping = audit.get("mapping", {})
    require(mapping.get("status") == "PENDING_NO_OVERWRITE_SUCCESSOR", "D1010 mapping transaction status drift")
    require(mapping.get("current_mapping_state") == "UNCHANGED_R52", "D1010 current mapping state drift")
    require(mapping.get("planned_successor") == "tohoku_r53", "D1010 audit successor drift")
    require(mapping.get("planned_decisions") == design["planned_decisions"], "D1010 audit planned_decisions differ from exact design")
    audit_canonical = mapping.get("canonical_decision_rows", {})
    design_canonical = design["canonical_decision_rows"]
    require(audit_canonical == {
        key: design_canonical[key]
        for key in (
            "encoding", "bytes", "sha256", "csv_suffix_bytes",
            "csv_suffix_sha256", "expected_dec_csv_bytes",
            "expected_dec_csv_sha256",
        )
    }, "D1010 audit canonical decision receipt drift")
    expected_issue = {"transaction_state": "PENDING_ATOMIC_R53", **design["planned_issue_append"]}
    require(mapping.get("planned_issue_append") == expected_issue, "D1010 audit planned issue differs from exact design")
    require(mapping.get("expected_map_csv") == {
        "bytes": design["canonical_decision_rows"]["expected_map_csv_bytes"],
        "sha256": design["canonical_decision_rows"]["expected_map_csv_sha256"],
    }, "D1010 audit projected map identity drift")
    require(mapping.get("expected_postsuccessor_counts") == design["expected_postsuccessor_counts"], "D1010 audit projected counts drift")
    require(mapping.get("expected_map_delta") == design["expected_map_delta"], "D1010 audit map delta drift")
    return {
        "receipt": record(D1010_AUDIT, "D1010_CHECK.json"),
        "status": "STRICT_PASS",
        "planned_decisions": design["planned_decisions"],
        "planned_issue_append": design["planned_issue_append"],
        "mapping_design": record(DESIGN, "tmp/d1010_mapping_design.json"),
    }


def verify_external() -> dict[str, object]:
    require_identity(AUTHORITY_PART_I, EXPECTED_AUTHORITY_PART_I)
    require_identity(AUTHORITY_PART_II, EXPECTED_AUTHORITY_PART_II)
    runtime = verify_runtime()
    predecessor = verify_predecessor()
    formalization = verify_formalization()
    semantic = verify_semantic()
    reader = verify_reader()
    d1010 = verify_d1010()
    return {
        "predecessor": predecessor,
        "decision_audit": d1010,
        "formalization": formalization,
        "scanner": {
            "outputs": {name: record(SCAN_ORACLE / name, f"tmp/d1010_scan/{name}") for name in sorted(EXPECTED_ORACLE_OUTPUTS)},
            "counts": formalization["scanner_audit"]["counts"],
            "delta_from_d1009": formalization["scanner_audit"]["delta_from_d1009"],
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
        "schema": "tohoku-stacks-mapping-successor-r53-v1",
        "status": "PASS", "errors": [],
        "predecessor_dossier": external["predecessor"],
        "semantic_source": external["semantic"],
        "decision_audit": external["decision_audit"],
        "formalization": external["formalization"],
        "scanner_oracle": external["scanner"],
        "reader": external["reader"],
        "runtime": external["runtime"],
        "authority_inputs": external["authority_inputs"],
        "execution": execution_receipt(),
        "git": {
            "inspection_performed": False,
            "status": "temporarily_unavailable",
            "reason": "Direct user report: the account was suspended after VPN use and a support ticket is filed; no Git operation is needed for this bounded local successor.",
            "predecessor_receipt": record(SOURCE / "r52-check.json", "tohoku_r52/r52-check.json"),
            "remote_server_freshness_verified": False,
        },
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": NONCLAIMS,
    }


def verify_stage(root: Path, receipt_mode: bool) -> dict[str, object]:
    require_plain_directory(root)
    entries = list(root.iterdir())
    expected_names = PAYLOAD | ({"r53-check.json"} if receipt_mode else set())
    require(not any(path.is_dir() for path in entries), "Unexpected r53 output subdirectory")
    require({path.name for path in entries if path.is_file()} == expected_names, "r53 output surface drift")
    for path in entries:
        require_plain_file(path)

    cfg = strict_json(root / "cfg.json")
    expected_cfg = strict_json(SOURCE / "cfg.json")
    expected_cfg["dossier_id"] = "tohoku_r53"
    require(cfg == expected_cfg, "r53 cfg differs from r52 beyond dossier ID")
    require_identity(root / "cfg.json", (5151, "10FC41C2DDE6B23B12B6E816DEA07B72A9D1FFF18AC4A45F55D22FF769E9CE53"))
    for name in ("intake.json", "units.csv", "topics.csv", "ucand.csv"):
        require(identity(root / name) == identity(SOURCE / name), f"Unauthorized inherited payload drift: {name}")
    for name, expected in EXPECTED_STAGE_SCAN_OUTPUTS.items():
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    stage_sha = stage_check.get("sha256", {})
    oracle_sha = oracle_check.get("sha256", {})
    require(isinstance(stage_sha, dict) and isinstance(oracle_sha, dict), "Scanner SHA ledger shape drift")
    stage_only = {f"tohoku_r53/{name}" for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv")}
    oracle_only = {f"tohoku_r51/{name}" for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv")}
    require(set(stage_sha) - set(oracle_sha) == stage_only, "r53 scanner SHA path additions drift")
    require(set(oracle_sha) - set(stage_sha) == oracle_only, "r53 scanner SHA path removals drift")
    normalized = dict(stage_sha)
    for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv"):
        normalized[f"tohoku_r51/{name}"] = normalized.pop(f"tohoku_r53/{name}")
    normalized_check = dict(stage_check)
    normalized_check["sha256"] = normalized
    require(normalized_check == oracle_check, "r53 scanner check differs from D1010 oracle beyond four namespace keys")

    dec_raw = (root / "dec.csv").read_bytes()
    require(dec_raw == expected_decision_bytes(), "r53 decision ledger is not exact append-only successor")
    require(dec_raw[:EXPECTED_SOURCE["dec.csv"][0]] == (SOURCE / "dec.csv").read_bytes(), "r53 decision prefix drift")
    _, decisions = load_csv(root / "dec.csv")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1028)], "r53 decision sequence drift")
    require(decisions[-4:] == decision_rows(), "r53 decision suffix rows drift")

    issue_raw = (root / "issues.csv").read_bytes()
    require(issue_raw == expected_issue_bytes(), "r53 issue ledger is not exact append-only successor")
    require(issue_raw[:EXPECTED_SOURCE["issues.csv"][0]] == (SOURCE / "issues.csv").read_bytes(), "r53 issue prefix drift")
    _, issues = load_csv(root / "issues.csv")
    require([row["issue_id"] for row in issues] == [f"I{number:06d}" for number in range(1, 31)], "r53 issue sequence drift")
    require(issues[-1] == issue_row(), "r53 issue suffix row drift")

    map_fields, mapped = load_csv(root / "map.csv")
    expected_fields, expected_rows = expected_map_rows()
    require(map_fields == expected_fields and mapped == expected_rows, "r53 map differs from independent four-row projection")
    require_identity(root / "map.csv", (479894, "7BF8C6794D743ACE1334F5979B820E955C70C14537F0B00A0E6A679376668BAE"))
    delta = map_delta(mapped)
    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("schema") == "historical-source-stacks-map-v1", "r53 mcheck schema drift")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r53 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r53 mapping counts drift")
    require(mcheck.get("warnings") == stage_check.get("warnings") and len(mcheck.get("warnings", [])) == 652, "r53 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r53 status narrative drift")
    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_section", "new_statement"))
    require(gap_count == 38, "r53 gap count projection drift")
    result = {
        "status": "PASS", "errors": [],
        "decisions": 1027,
        "decisions_appended": decision_rows(),
        "issue_appended": issue_row(),
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 652, "errors": 0},
        "scanner_delta": load_design() and strict_json(FORMALIZATION)["scanner_audit"]["delta_from_d1009"],
        "scanner_check_delta": {"changed_fields": ["sha256"], "namespace_keys_only": 4, "normalized_equal": True},
        "map_delta": delta,
        "remaining_gap_class_dispositions": 38,
        "semantic_generation": "sem/r19",
        "inherited_unit_inventory": "BYTE_IDENTICAL_R52",
        "source_repairs_appended": 1,
    }
    if receipt_mode:
        receipt = strict_json(root / "r53-check.json")
        require(receipt == receipt_payload(root, result), "r53 receipt replay mismatch")
    return result


def external_input_paths() -> list[Path]:
    paths = [R52_VALIDATOR, D1010_AUDIT, DESIGN, FORMALIZATION, EXPECTED_PYTHON, AUTHORITY_PART_I, AUTHORITY_PART_II]
    paths.extend(SOURCE / name for name in EXPECTED_SOURCE)
    paths.extend(ROOT / relative for relative in EXPECTED_RUNTIME)
    paths.extend(SEM / name for name in EXPECTED_SEM)
    paths.extend(SCAN_ORACLE / name for name in EXPECTED_ORACLE_OUTPUTS)
    evidence = strict_json(FORMALIZATION)
    for key in ("candidate", "live"):
        paths.append(_record_path(evidence["integration"][key]))
    paths.extend(_record_path(item) for item in evidence["build_audit"]["artifacts"].values())
    paths.extend(_record_path(item) for item in evidence["pdf_audit"]["visual_renders"])
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
    raw = os.environ.pop("TOHOKU_R53_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r53.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r53.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r53 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r53 transaction exists: {STAGE}")
        external = verify_external()
        _, projection = expected_map_rows()
        result = {
            "schema": "tohoku-r53-static-input-audit-v1",
            "status": "PASS", "errors": [], "attestation": attestation,
            "target_absent": True, "stage_absent": True,
            "predecessor": external["predecessor"],
            "decision_audit": external["decision_audit"],
            "formalization": external["formalization"],
            "scanner_oracle": external["scanner"],
            "semantic_source": external["semantic"],
            "reader": external["reader"],
            "runtime": external["runtime"],
            "authority_inputs": external["authority_inputs"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "projected_map_delta": map_delta(projection),
            "projected_remaining_gap_class_dispositions": 38,
            "projected_dec_csv": {"bytes": len(expected_decision_bytes()), "sha256": digest(expected_decision_bytes())},
            "projected_issues_csv": {"bytes": len(expected_issue_bytes()), "sha256": digest(expected_issue_bytes())},
            "launch_authorized": True,
        }
    else:
        result = {"schema": "tohoku-r53-stage-validation-v1", "attestation": attestation, **verify_stage(args.stage.resolve(), args.receipt)}
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
