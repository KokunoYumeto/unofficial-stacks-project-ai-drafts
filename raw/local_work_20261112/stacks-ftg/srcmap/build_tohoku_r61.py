#!/usr/bin/env python3
"""Build, validate, promote, and replay the bounded Tohoku r61 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


SCRIPT_PATH = Path(__file__).resolve()
ROOT = SCRIPT_PATH.parent.parent
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
SOURCE = ROOT / "tohoku_r60"
TARGET = ROOT / "tohoku_r61"
STAGE = ROOT / ".tohoku-r61-txn"
ORACLE = ROOT / "tmp" / "d1017_r61_scan_oracle"
ORACLE_REPLAY = ROOT / "tmp" / "d1017_r61_scan_replay"
CONTRACT_PATH = ROOT / "srcmap" / "tohoku_r61_contract.json"

CONTRACT_ID = "D1017-r61-D001041-I000032-v1"
PAYLOAD = {
    "cfg.json",
    "intake.json",
    "units.csv",
    "topics.csv",
    "dec.csv",
    "issues.csv",
    "check.json",
    "stx.csv",
    "tcand.csv",
    "tmap.csv",
    "map.csv",
    "ucand.csv",
    "mcheck.json",
    "STATUS.md",
}
ORACLE_PAYLOAD = {"cfg.json", "topics.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv"}

RUNTIME = {
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
}
EXPECTED_R60_RECEIPT = (8055, "88952DD37BD81F11DF463BA351C779C68EEFD7270CA3D0AE94420A784C7446F0")
EXPECTED_R60_FILES = {
    "STATUS.md": (999, "7C02435EAA8B55D17EA1F26C452D99020CFA079DDED2B00FAC1F844321BAB61B"),
    "cfg.json": (5151, "E3C1117E4DC42A902A13DB823B146F01A1DE2B62066C75BD683B4BF50DA66AF8"),
    "check.json": (82451, "921E55104276A9C583124115733882F87A96D806F54C50F6082639F7E8CD804C"),
    "dec.csv": (384155, "7BAA5693242F7A809B5534164BE64FC9BA8C56BFAC21CD70CC0B7B75ACB5C235"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (32866, "D882954C9D55F7AB93F2910CE99D86FA1D107F6EFE7008B26722F012F50BC2BC"),
    "map.csv": (484523, "99A6754134043E3434541A1E9CE1D62B18E1BC40B020080EA13BF06280849872"),
    "mcheck.json": (72278, "3C45D6E42EB080C2D04A3076BE0ADA782B3B9921121FDA7234588B3AD9D3CB3C"),
    "stx.csv": (5287297, "C4224C4D2D5D51E4E9079F9FBA070A0A5BB5D6B8ECF37CE07DFC662F3A84829E"),
    "tcand.csv": (489256, "ACDCA4D86FEEB1A27D1E46D8869B6C340D6DFEB1057161B8F872D848B089DA29"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SCAN = {
    "cfg.json": (5151, "7EA53BF72EA7BBCD5649DFF6598C802C503F355918A4DC11EB1C508ACEBB5CD2"),
    "check.json": (82634, "D5C19A9DEC66679F9AC616A0BDFB994A7334355F057D75B8648B774E57474AC9"),
    "stx.csv": (5287716, "8AF5DD35D91AF45EC6DACE5F3DDC03213992D9EB6316353DC0FEABC7A9B23427"),
    "tcand.csv": (489256, "B7481F3F3FB7F5DDF59F6646B3DB440452751D760C21519D53619EB7510C4B13"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
}
EXPECTED_PROJECTED = {
    "dec.csv": (384781, "59D2C244243088BF6C0537088C7A8DD2F4FE37DBF1FCAA3FF3F3C821C1518B3F"),
    "issues.csv": (34015, "2D60F1DB762808C5EFCD62AAB74394D8772C190DCB3150F3F82984DE3B9D7EB1"),
    "map.csv": (484839, "5A4D3DA8211DB34DAD2F2717BFA07452A33E69811092190174AA0D5EFECEACC5"),
}
EXPECTED_APPEND_ROWS = {
    "decision": (626, "EC7E40AEDECE8103D2B843E6F91EDF4C86DB97DE3123C9557A02FCDC608AE5A2"),
    "issue": (1149, "4FA57A4C3AF9AFF324A04008CCB5FDBE49275ACD0AEDC554D7ADDB7B33AA311E"),
}
EXPECTED_PREDECESSOR_MAP_ROW = (473, "401AC64FB3F40FB5BA9F710311A042FE59379707E3FC5125D6B33B6010B4E54E")
EXPECTED_SUCCESSOR_MAP_ROW = (789, "CF7EF7C45CDC794E2D3FA5834552318423349BECBAA993CA87CFAE086D17E03B")

EXPECTED_D1017_AUDIT = (14707, "28978CA9E62B68FB66934649F023E75F2B17F79EF0C1BD43411D5DA0BBBFCAD8")
STACKS_INPUTS = {
    "design": ("tmp/d1017_p185_formalization_design.json", 8424, "C1E54BDFB4F52D6761248992D8C669CFB43FB21976A2539063FD893BDEAF43DC"),
    "review": ("tmp/d1017_stacks_independent_review_r1.json", 12100, "E446CBFC413104F7D0D888F795DDB9C3100C87E615CBC1845667E4830A2A15BC"),
    "candidate": ("tmp/d1017_noncommutative_internal_hom_candidate.tex", 5063, "FB6278770580656A6904DC4505A7E69DAB222710D62633937125C557A2E75190"),
    "modules_tex": ("modules.tex", 232828, "EF800D241EBA37CE7099F9B09440228969710988903EE393261C866F902A12F5"),
    "modules_pdf": ("modules.pdf", 767323, "A35B4D3FDD5A8A106A24570FA6E8890BACF45E83BD01B2F949A838F33D311638"),
}
CANONICAL_INPUTS = {
    "authority_pdf": ("authority_snapshot/jstage_part_II_9_3_185.pdf", 3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
    "source_receipt": ("production/p185_fix2/check.json", 5291, "E54AE998A9D8AB863652521E329731789727DD064B48E6A52CAB83584C802EEA"),
    "source_decisions": ("production/p185_fix2/decisions.jsonl", 3493, "BB7813EA38AD72B878C4AE825141A82FEF092F8A99FEDDD7397AE705A56D4D4B"),
    "source_ledger": ("SOURCE_CORRECTIONS.jsonl", 212239, "31E8894E57B355383B49BB403FAE65B935C81B4C1DAC65C17B20C3C7A6E70439"),
    "reader_receipt": ("build/v068c3r20/build.json", 22216, "BA5D7BFDEA8F733CBA65703C5DA017E26A3FEB417297A975EBCAEFEA41D2BEA1"),
    "reader_fr": ("output/pdf/fr-p119-221-v068c3r20.pdf", 1417551, "91EE76111A240E36AC107FCAC9605A5E32E9E9796AAE86AAB495D5F36DB3AFB8"),
    "reader_en": ("output/pdf/en-p119-221-v068c3r20.pdf", 1381128, "3E78467B441F801DE742584CA9FBE906A886B4B9DD6AA4585315DB9482175AA1"),
    "qa_receipt": ("qa/v68r42/check.json", 5375, "C3D039B399FDA3A2232F07A0D33ABB3E07ADEA431182FCEC26F3C8A9DFD703D0"),
    "qa_structural": ("qa/v68r42/structural.json", 7900, "06EBFDCE2E77644BADB3A38606662FEBA4B518AECC99A84BEEE70DA930E71171"),
    "sem_r18_nodes": ("sem/r18/nodes.csv", 585012, "3A3C9B6C22B0FA5E16466C264205D97CCA6041FF785F555A4C28F9639A50550D"),
    "sem_r18_manifest": ("sem/r18/manifest.json", 38138, "40596FD03A707CF8AC3C1D825D0FEAD4447663F6A57E7BD16735021F14B520AB"),
    "sem_r18_validation": ("sem/r18/validation.json", 6102, "2972E56494357AD0ABDB765057E20CA99777E6A6AA73B5AF7571EA1F715AA3D4"),
    "sem_r21_catalog": ("sem/r21/catalog.csv", 772, "7726735ABA05D9F5791DBE143EB27D25CBBD9161ABE8F82ABF40FE1D8B489180"),
    "sem_r21_nodes": ("sem/r21/nodes.csv", 586416, "C0DD26F979C17DA1DA8E09CAD83FEAA44BA8644DB0625D693C3D20A8B82CCBCA"),
    "sem_r21_occ": ("sem/r21/occ.csv", 515088, "637CA9EF1382846C88408D6FF0CBF45F785758EE469C10D60B84943685136833"),
    "sem_r21_manifest": ("sem/r21/manifest.json", 32119, "38275B0B2BB116467B3848F2E7EB1740F3692551E531E4130E72279F47F98C59"),
    "sem_r21_validation": ("sem/r21/validation.json", 9395, "D15C85751526EA144BFA02AFBB580540C93620C7AC12A6656D1C895EEA5A8BDB"),
}

MAP_FIELDS = [
    "unit_id",
    "item",
    "unit_type",
    "parent_id",
    "source_start",
    "source_end",
    "source_loc",
    "authority_sha256",
    "source_topics",
    "topic_evidence_labels",
    "topic_evidence_tags",
    "decision_id",
    "disposition",
    "review_state",
    "stacks_labels",
    "stacks_tags",
    "rationale",
]
DEC_FIELDS = ["decision_id", "unit_id", "action", "disposition", "stacks_labels", "rationale", "review_state", "supersedes"]
ISSUE_FIELDS = ["issue_id", "unit_id", "status", "kind", "claim", "evidence_labels", "evidence", "control", "resolution_decision"]
DECISION = {
    "decision_id": "D001041",
    "unit_id": "tohoku:definition:hom-o-and-local-hom",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "modules-definition-hom-left-modules;modules-lemma-sheaf-hom-left-modules",
    "rationale": "Stacks now gives the arbitrary-ring-sheaf left-module global Hom group, arbitrary-subspace local Hom groups, their restriction maps and sheaf property, and the canonical action by Gamma(X,Z_O). This is equivalent to the corrected sem/r21 source statement. The diplomatic printed Z(Gamma(X,O)) scalar claim is preserved as a source error and is not asserted; the following sheaf-Hom unit remains separate.",
    "review_state": "integrated_source_repair_semantic_stacks_and_independent_review",
    "supersedes": "D000404",
}
ISSUE = {
    "issue_id": "I000032",
    "unit_id": "tohoku:definition:hom-o-and-local-hom",
    "status": "resolved",
    "kind": "global_center_does_not_restrict_to_local_centers",
    "claim": "The printed p. 185 sentence makes Hom_O(A,B) a module over Z(Gamma(X,O)), but a globally central section can restrict to a noncentral local section, so its multiplication need not be O-linear. The canonical scalar ring is Gamma(X,Z_O)=Gamma(O^natural).",
    "evidence_labels": "modules-definition-hom-left-modules;modules-lemma-sheaf-hom-left-modules",
    "evidence": "Official Part II SHA-256 8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53, printed p. 185. On the Sierpinski space take O(X)=Q[t], O(U)=M_2(Q), with t restricting to e_11: t is globally central but e_11 is not locally central. D1017 formalizes the correct Gamma(X,Z_O)-action, and production/p185_fix2, reader v068c3r20, QA v68r42, and sem/r21 bind the repaired source statement.",
    "control": "Preserve the printed scalar-ring sentence in diplomatic French. Use TOH-P185-COR-002 and TOH-SRC-P185-002 only in corrected French and English; bind the exact reader, visual QA, semantic successor, and final D1017 prerequisite audit before replacing D000404. Do not merge the following sheaf-Hom source unit.",
    "resolution_decision": "D001041",
}
EXPECTED_COUNTS = {
    "units": 991,
    "decisions": 1041,
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
        "existing_equivalent": 384,
        "existing_stronger": 41,
        "existing_weaker": 4,
        "extend_existing": 11,
        "historical_reference": 33,
        "new_section": 4,
        "new_statement": 6,
        "structural_only": 424,
    },
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22103,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1286,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r60 dossier is preserved exactly; D001041 and I000032 form the bounded corrected p.185 Hom scalar-ring successor.\n"
    "- D001041 is existing_equivalent only for the corrected sem/r21 statement: Stacks gives left-module global and arbitrary-subspace local Hom, restriction and sheaf structure, and the Gamma(X,Z_O)-action.\n"
    "- The diplomatic printed Z(Gamma(X,O)) claim remains preserved as a recorded source error; the following sheaf-Hom source unit remains separate.\n"
    "- Source admission p185_fix2, reader v068c3r20, QA v68r42, sem/r21, the D1017 Stacks build, and independent review are bound byte-exactly.\n"
    "- The scanner indexes the exact 119 top-level TeX files with 22,103 labels, 675 warnings, and no errors.\n"
    "- There are 1,041 decisions, 679 decided units, 32 resolved source issues, and 25 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the reported VPN/security review; local work continues and no GitHub or Git operation is attempted.\n"
    "- No claim is made for the separate following source unit, GAGA comparison, release, publication, DOI, remote freshness, rights, or whole-paper completion.\n"
).encode("utf-8")


class ContractError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity_from_bytes(data: bytes) -> tuple[int, str]:
    return len(data), digest(data)


def identity(path: Path) -> tuple[int, str]:
    return identity_from_bytes(path.read_bytes())


def record(path: Path, name: str | None = None) -> dict[str, Any]:
    size, sha = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha}


def require_identity(path: Path, expected: tuple[int, str], label: str | None = None) -> bytes:
    require(path.is_file() and not path.is_symlink(), f"Expected plain file: {label or path}")
    data = path.read_bytes()
    require(identity_from_bytes(data) == expected, f"Identity drift: {label or path}")
    return data


def strict_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    require(b"\r" not in raw and raw.endswith(b"\n"), f"Noncanonical JSON: {path}")
    value = json.loads(raw.decode("utf-8"))
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, f"Missing CSV header: {path}")
        rows = [dict(row) for row in reader]
    require(all(None not in row for row in rows), f"Surplus CSV fields: {path}")
    return list(reader.fieldnames), rows


def csv_bytes(fields: Sequence[str], rows: Iterable[Mapping[str, str]], header: bool = True) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(fields), lineterminator="\n")
    if header:
        writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def line_identity(path: Path, line_number: int) -> tuple[int, str]:
    lines = path.read_bytes().splitlines(keepends=True)
    require(1 <= line_number <= len(lines), f"Line outside file: {path}:{line_number}")
    return identity_from_bytes(lines[line_number - 1])


def one_row(rows: Sequence[Mapping[str, str]], key: str, value: str, label: str) -> dict[str, str]:
    matches = [dict(row) for row in rows if row.get(key) == value]
    require(len(matches) == 1, f"{label}: expected one {key}={value}")
    return matches[0]


def exclusive_write(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    require(path.read_bytes() == data, f"Write readback mismatch: {path}")


def load_contract() -> dict[str, Any]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "r61 contract missing or unsafe")
    contract_bytes = CONTRACT_PATH.read_bytes()
    contract = json.loads(contract_bytes.decode("utf-8"))
    require(contract.get("schema") == "tohoku-r61-transaction-contract-v1", "r61 contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "r61 contract ID mismatch")
    spec = contract.get("script")
    require(isinstance(spec, dict), "r61 script pin missing")
    require(spec.get("path") == "srcmap/build_tohoku_r61.py", "r61 script path mismatch")
    require(identity_from_bytes(SCRIPT_PATH.read_bytes()) == (spec.get("bytes"), spec.get("sha256")), "r61 script identity mismatch")
    require(contract.get("predecessor") == {"path": "tohoku_r60/r60-check.json", "bytes": EXPECTED_R60_RECEIPT[0], "sha256": EXPECTED_R60_RECEIPT[1]}, "r61 predecessor contract mismatch")
    require(contract.get("target") == "tohoku_r61", "r61 target contract mismatch")
    return {
        "script": record(SCRIPT_PATH, "srcmap/build_tohoku_r61.py"),
        "contract": record(CONTRACT_PATH, "srcmap/tohoku_r61_contract.json"),
        "python": record(Path(sys.executable).resolve(), "python.exe"),
    }


def expected_cfg_bytes() -> bytes:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r61"
    data = json_bytes(cfg)
    require(identity_from_bytes(data) == EXPECTED_SCAN["cfg.json"], "Projected r61 cfg drift")
    return data


def expected_append(fields: Sequence[str], row: Mapping[str, str], expected: tuple[int, str], label: str) -> bytes:
    data = csv_bytes(fields, [row], header=False)
    require(identity_from_bytes(data) == expected, f"Projected {label} append row drift")
    return data


def expected_decision_bytes() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    require(fields == DEC_FIELDS and len(rows) == 1040, "r60 decision schema/count drift")
    require(rows[-1]["decision_id"] == "D001040", "r60 decision tail drift")
    append = expected_append(DEC_FIELDS, DECISION, EXPECTED_APPEND_ROWS["decision"], "decision")
    data = (SOURCE / "dec.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["dec.csv"], "Projected r61 decisions drift")
    return data


def expected_issue_bytes() -> bytes:
    fields, rows = load_csv(SOURCE / "issues.csv")
    require(fields == ISSUE_FIELDS and len(rows) == 31, "r60 issue schema/count drift")
    require(rows[-1]["issue_id"] == "I000031", "r60 issue tail drift")
    append = expected_append(ISSUE_FIELDS, ISSUE, EXPECTED_APPEND_ROWS["issue"], "issue")
    data = (SOURCE / "issues.csv").read_bytes() + append
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["issues.csv"], "Projected r61 issues drift")
    return data


def expected_map_bytes() -> bytes:
    fields, rows = load_csv(SOURCE / "map.csv")
    require(fields == MAP_FIELDS and len(rows) == 991, "r60 map schema/count drift")
    selected = one_row(rows, "unit_id", DECISION["unit_id"], "r60 map")
    require(selected["decision_id"] == "D000404" and selected["disposition"] == "existing_weaker", "r60 target map state drift")
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
    data = csv_bytes(fields, [replacement if row["unit_id"] == DECISION["unit_id"] else row for row in rows])
    require(identity_from_bytes(data) == EXPECTED_PROJECTED["map.csv"], "Projected r61 map drift")
    return data


def verify_predecessor() -> dict[str, Any]:
    receipt = SOURCE / "r60-check.json"
    require_identity(receipt, EXPECTED_R60_RECEIPT, "r60 receipt")
    for name, expected in EXPECTED_R60_FILES.items():
        require_identity(SOURCE / name, expected, f"r60/{name}")
    value = strict_json(receipt)
    require(value.get("schema") == "tohoku-stacks-mapping-successor-r60-v1", "r60 receipt schema drift")
    require(value.get("status") == "PASS" and value.get("errors") == [], "r60 receipt not PASS")
    require(value.get("deltas", {}).get("remaining_gap_class_dispositions") == 26, "r60 gap count drift")
    records = value.get("files")
    require(isinstance(records, list) and len(records) == len(EXPECTED_R60_FILES), "r60 receipt inventory drift")
    replay = {row.get("name"): (row.get("bytes"), row.get("sha256")) for row in records}
    require(replay == EXPECTED_R60_FILES, "r60 receipt file identities drift")
    require(line_identity(SOURCE / "map.csv", 344) == EXPECTED_PREDECESSOR_MAP_ROW, "r60 target map row drift")
    return {"receipt": record(receipt, "tohoku_r60/r60-check.json")}


def read_spec(root: Path, spec: tuple[str, int, str], label: str) -> tuple[Path, bytes]:
    path = root / spec[0]
    return path, require_identity(path, (spec[1], spec[2]), label)


def verify_external() -> dict[str, Any]:
    execution = load_contract()
    predecessor = verify_predecessor()
    audit_path = ROOT / "D1017_CHECK.json"
    require_identity(audit_path, EXPECTED_D1017_AUDIT, "D1017 frozen audit")
    audit = strict_json(audit_path)
    require(audit.get("status") == "STRICT_PASS_PREREQUISITES_R61_MAPPING_AUTHORIZED", "D1017 audit status drift")
    require(audit.get("errors") == [], "D1017 audit errors drift")
    authorization = audit.get("mapping_authorization", {})
    require(authorization.get("decision") == DECISION, "D1017 decision authorization drift")
    require(authorization.get("issue") == ISSUE, "D1017 issue authorization drift")
    require(authorization.get("successor") == "tohoku_r61", "D1017 successor authorization drift")

    stacks_records: dict[str, Any] = {}
    stacks_bytes: dict[str, bytes] = {}
    for role, spec in STACKS_INPUTS.items():
        path, data = read_spec(ROOT, spec, role)
        stacks_records[role] = record(path, spec[0])
        stacks_bytes[role] = data
    design = json.loads(stacks_bytes["design"].decode("utf-8"))
    review = json.loads(stacks_bytes["review"].decode("utf-8"))
    require(design.get("formalization_id") == "D1017", "D1017 design ID drift")
    require(design.get("mapping_plan", {}).get("planned_decision") == "D001041", "D1017 design mapping decision drift")
    require(review.get("status") == "STRICT_PASS_STACKS_FORMALIZATION", "D1017 review status drift")
    require(stacks_bytes["modules_tex"].count(stacks_bytes["candidate"]) == 1, "D1017 candidate insertion drift")

    canonical_records: dict[str, Any] = {}
    canonical_values: dict[str, Any] = {}
    for role, spec in CANONICAL_INPUTS.items():
        path, data = read_spec(CANONICAL_ROOT, spec, role)
        canonical_records[role] = record(path, spec[0])
        if spec[0].endswith(".json"):
            canonical_values[role] = json.loads(data.decode("utf-8"))
    source = canonical_values["source_receipt"]
    reader = canonical_values["reader_receipt"]
    qa = canonical_values["qa_receipt"]
    sem_manifest = canonical_values["sem_r21_manifest"]
    sem_validation = canonical_values["sem_r21_validation"]
    require(source.get("status") == "PASS" and source.get("decision_id") == "TOH-P185-COR-002", "p185 source admission drift")
    require(source.get("source_correction_id") == "TOH-SRC-P185-002", "p185 source correction drift")
    require(reader.get("status") == "PASS" and reader.get("revision") == "v068c3r20", "reader r20 receipt drift")
    require(qa.get("status") == "PASS" and qa.get("stable_id") == "tohoku:reader-qa:v68r42:v068c3r20", "QA r42 receipt drift")
    require(sem_manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v21", "sem/r21 manifest schema drift")
    require(sem_manifest.get("version") == "local-v068c3r20-sem-r21" and sem_manifest.get("errors") == [], "sem/r21 manifest state drift")
    require(sem_validation.get("status") == "PASS" and sem_validation.get("errors") == [], "sem/r21 validation state drift")
    require(sem_validation.get("manifest_sha256") == CANONICAL_INPUTS["sem_r21_manifest"][2], "sem/r21 validation/manifest drift")
    require(sem_validation.get("delta_summary", {}).get("changed_existing_fields") == 12, "sem/r21 delta drift")
    require(sem_validation.get("delta_summary", {}).get("appended_rows") == 0, "sem/r21 row-allocation drift")
    require(line_identity(CANONICAL_ROOT / "sem/r18/nodes.csv", 344) == (853, "9AB3886434AC3C9B98EF5BC7F942492C3C4E08C081E83B57EBA2FAFB450CDC79"), "sem/r18 target row drift")
    require(line_identity(CANONICAL_ROOT / "sem/r21/nodes.csv", 344) == (1255, "D207F5B6BB2F6C61051D10837D7045661D419C7BC772F153C1C61983262DC882"), "sem/r21 target row drift")
    return {
        "execution": execution,
        "predecessor": predecessor,
        "audit": record(audit_path, "D1017_CHECK.json"),
        "stacks": stacks_records,
        "canonical": canonical_records,
    }


def run_tool(relative: str, out: Path) -> None:
    tool = ROOT / relative
    payload = require_identity(tool, RUNTIME[relative], relative)
    runner = (
        "import hashlib,sys\n"
        "path=sys.argv[1]; expected=int(sys.argv[2]); sha=sys.argv[3]; out=sys.argv[4]\n"
        "payload=sys.stdin.buffer.read()\n"
        "if len(payload)!=expected or hashlib.sha256(payload).hexdigest().upper()!=sha: raise RuntimeError('runtime payload drift')\n"
        "sys.argv=[path,out]\n"
        "ns={'__name__':'__main__','__file__':path}\n"
        "exec(compile(payload,path,'exec'),ns)\n"
    )
    subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            "-c",
            runner,
            str(tool),
            str(len(payload)),
            RUNTIME[relative][1],
            str(out),
        ],
        cwd=ROOT,
        check=True,
        input=payload,
    )
    require(identity(tool) == RUNTIME[relative], f"Runtime changed during execution: {relative}")


def verify_scan(root: Path, oracle_surface: bool = False) -> dict[str, Any]:
    expected_names = ORACLE_PAYLOAD if oracle_surface else None
    if expected_names is not None:
        require({path.name for path in root.iterdir() if path.is_file()} == expected_names, f"Scanner oracle surface drift: {root}")
        require(not any(path.is_dir() for path in root.iterdir()), f"Unexpected scanner oracle subdirectory: {root}")
    for name, expected in EXPECTED_SCAN.items():
        require_identity(root / name, expected, f"{root.name}/{name}")
    check = strict_json(root / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "r61 scanner not PASS")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r61 scanner count drift")
    require(len(check.get("warnings", [])) == 675, "r61 scanner warning count drift")
    require(check.get("tex_sha256", {}).get("modules.tex") == STACKS_INPUTS["modules_tex"][2], "r61 scanner modules.tex binding drift")
    _, rows = load_csv(root / "stx.csv")
    definition = one_row(rows, "full_label", "modules-definition-hom-left-modules", "scanner definition")
    lemma = one_row(rows, "full_label", "modules-lemma-sheaf-hom-left-modules", "scanner lemma")
    require(definition["tag"] == "" and lemma["tag"] == "", "new D1017 labels unexpectedly have official tags")
    return check


def build_oracle_dir(path: Path) -> None:
    require(not path.exists(), f"Oracle path already exists: {path}")
    path.mkdir(parents=False)
    exclusive_write(path / "cfg.json", expected_cfg_bytes())
    exclusive_write(path / "topics.csv", (SOURCE / "topics.csv").read_bytes())
    run_tool("srcmap/scan.py", path)
    verify_scan(path, oracle_surface=True)


def generate_oracles() -> None:
    load_contract()
    require(not TARGET.exists() and not STAGE.exists(), "r61 target or stage already exists")
    if ORACLE.exists():
        verify_scan(ORACLE, oracle_surface=True)
    else:
        build_oracle_dir(ORACLE)
    if ORACLE_REPLAY.exists():
        verify_scan(ORACLE_REPLAY, oracle_surface=True)
    else:
        build_oracle_dir(ORACLE_REPLAY)
    for name in EXPECTED_SCAN:
        require((ORACLE / name).read_bytes() == (ORACLE_REPLAY / name).read_bytes(), f"Scanner replay differs: {name}")
    print(
        json.dumps(
            {
                "schema": "tohoku-r61-scanner-oracle-v1",
                "status": "PASS",
                "errors": [],
                "oracle": {name: record(ORACLE / name) for name in sorted(EXPECTED_SCAN)},
                "replay": {name: record(ORACLE_REPLAY / name) for name in sorted(EXPECTED_SCAN)},
                "counts": {**EXPECTED_SCAN_COUNTS, "warnings": 675, "errors": 0},
            },
            indent=2,
            sort_keys=True,
        )
    )


def verify_oracles() -> dict[str, Any]:
    require(ORACLE.is_dir() and ORACLE_REPLAY.is_dir(), "r61 scanner oracles are missing")
    verify_scan(ORACLE, oracle_surface=True)
    verify_scan(ORACLE_REPLAY, oracle_surface=True)
    for name in EXPECTED_SCAN:
        require((ORACLE / name).read_bytes() == (ORACLE_REPLAY / name).read_bytes(), f"Scanner replay differs: {name}")
    return {
        "oracle": {name: record(ORACLE / name, f"tmp/d1017_r61_scan_oracle/{name}") for name in sorted(EXPECTED_SCAN)},
        "replay": {name: record(ORACLE_REPLAY / name, f"tmp/d1017_r61_scan_replay/{name}") for name in sorted(EXPECTED_SCAN)},
    }


def map_row_delta() -> list[dict[str, str]]:
    before_fields, before_rows = load_csv(SOURCE / "map.csv")
    require(before_fields == MAP_FIELDS, "r60 map fields drift")
    after_data = expected_map_bytes()
    reader = csv.DictReader(io.StringIO(after_data.decode("utf-8"), newline=""))
    after_rows = [dict(row) for row in reader]
    require([row["unit_id"] for row in before_rows] == [row["unit_id"] for row in after_rows], "map key order drift")
    deltas: list[dict[str, str]] = []
    for old, new in zip(before_rows, after_rows):
        for field in MAP_FIELDS:
            if old[field] != new[field]:
                deltas.append({"unit_id": old["unit_id"], "field": field, "before": old[field], "after": new[field]})
    return deltas


def verify_stage(root: Path, receipt_mode: bool = False) -> dict[str, Any]:
    require(root.is_dir() and not root.is_symlink(), f"Missing or unsafe r61 output: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    require(names == PAYLOAD | ({"r61-check.json"} if receipt_mode else set()), "r61 output surface drift")
    require(not any(path.is_dir() for path in root.iterdir()), "Unexpected r61 output subdirectory")
    require((root / "cfg.json").read_bytes() == expected_cfg_bytes(), "r61 cfg drift")
    for name in ("intake.json", "units.csv", "topics.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"Inherited payload drift: {name}")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r61 decision append drift")
    require((root / "issues.csv").read_bytes() == expected_issue_bytes(), "r61 issue append drift")
    require((root / "map.csv").read_bytes() == expected_map_bytes(), "r61 map replacement drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r61 STATUS drift")
    require_identity(root / "ucand.csv", EXPECTED_R60_FILES["ucand.csv"], "r61/ucand.csv")
    verify_scan(root)

    mcheck = strict_json(root / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r61 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_COUNTS, "r61 mapping counts drift")
    require(len(mcheck.get("warnings", [])) == 675, "r61 warning propagation drift")

    _, decisions = load_csv(root / "dec.csv")
    _, issues = load_csv(root / "issues.csv")
    _, mapping = load_csv(root / "map.csv")
    require([row["decision_id"] for row in decisions] == [f"D{n:06d}" for n in range(1, 1042)], "r61 decision sequence drift")
    require([row["issue_id"] for row in issues] == [f"I{n:06d}" for n in range(1, 33)], "r61 issue sequence drift")
    require(decisions[-1] == DECISION, "r61 final decision row drift")
    require(issues[-1] == ISSUE, "r61 final issue row drift")
    selected = one_row(mapping, "unit_id", DECISION["unit_id"], "r61 map")
    require(selected["decision_id"] == "D001041", "r61 map decision drift")
    require(selected["disposition"] == "existing_equivalent", "r61 map disposition drift")
    require(selected["review_state"] == DECISION["review_state"], "r61 map review state drift")
    require(selected["stacks_labels"] == DECISION["stacks_labels"] and selected["stacks_tags"] == "", "r61 map label/tag drift")
    require(selected["source_loc"] == "sem/r18/nodes.csv:344", "r61 source locator drift")
    require(line_identity(root / "map.csv", 344) == EXPECTED_SUCCESSOR_MAP_ROW, "r61 target map row identity drift")

    deltas = map_row_delta()
    require(len(deltas) == 6, "r61 map changed-field count drift")
    require({row["unit_id"] for row in deltas} == {DECISION["unit_id"]}, "r61 changed a non-target map row")
    require(
        {row["field"] for row in deltas}
        == {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
        "r61 map changed-field set drift",
    )
    gap_dispositions = {
        "existing_weaker",
        "extend_existing",
        "new_section",
        "new_statement",
    }
    remaining_gaps = sum(1 for row in mapping if row["disposition"] in gap_dispositions)
    require(remaining_gaps == 25, "r61 remaining-gap projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1041,
        "decisions_appended": ["D001041"],
        "issues_appended": ["I000032"],
        "mapping_counts": EXPECTED_COUNTS,
        "scan_counts": {**EXPECTED_SCAN_COUNTS, "warnings": 675, "errors": 0},
        "remaining_gap_class_dispositions": 25,
        "source_repairs_appended": 1,
        "mapping_closures_appended": 1,
        "map_delta": {"changed_units": 1, "changed_fields": 6, "unchanged_units": 990},
        "semantic_inventory_generation": "sem/r18",
        "corrected_semantic_authority": "sem/r21",
        "source_change": "D1017_P185_FIX2_R20_R42_SEM21",
        "scanner_payload_change": "D1017_MODULES_TEX_PLUS_R61_NAMESPACE",
    }
    if receipt_mode:
        receipt = strict_json(root / "r61-check.json")
        require(receipt == receipt_payload(root, result), "r61 receipt replay mismatch")
    return result


def output_records(root: Path) -> list[dict[str, Any]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def receipt_payload(root: Path, deltas: Mapping[str, Any]) -> dict[str, Any]:
    external = verify_external()
    oracles = verify_oracles()
    return {
        "schema": "tohoku-stacks-mapping-successor-r61-v1",
        "status": "PASS",
        "errors": [],
        "execution": external["execution"],
        "predecessor": external["predecessor"],
        "formalization": {
            "audit": external["audit"],
            "design": external["stacks"]["design"],
            "independent_review": external["stacks"]["review"],
            "candidate": external["stacks"]["candidate"],
            "live_source": external["stacks"]["modules_tex"],
            "live_pdf": external["stacks"]["modules_pdf"],
            "change_class": "source_repair_reader_semantic_and_mapping_successor",
        },
        "source_chain": {
            "source_admission": external["canonical"]["source_receipt"],
            "source_decisions": external["canonical"]["source_decisions"],
            "source_ledger": external["canonical"]["source_ledger"],
            "reader_receipt": external["canonical"]["reader_receipt"],
            "reader_french_pdf": external["canonical"]["reader_fr"],
            "reader_english_pdf": external["canonical"]["reader_en"],
            "qa_receipt": external["canonical"]["qa_receipt"],
            "qa_structural": external["canonical"]["qa_structural"],
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
        "files": output_records(root),
        "nonclaims": [
            "The source locator and frozen 991-unit inventory remain sem/r18; sem/r21 is bound as the corrected authority for this one replacement.",
            "The diplomatic printed Z(Gamma(O)) claim is preserved and is not asserted as true.",
            "The following sheaf-Hom source unit is not merged into D001041.",
            "No GAGA comparison, release, publication, DOI, remote-freshness, rights, or whole-paper completion is claimed.",
        ],
    }


def build_stage() -> None:
    require(not STAGE.exists(), "r61 stage already exists")
    verify_external()
    verify_oracles()
    STAGE.mkdir()
    exclusive_write(STAGE / "cfg.json", expected_cfg_bytes())
    for name in ("intake.json", "units.csv", "topics.csv"):
        exclusive_write(STAGE / name, (SOURCE / name).read_bytes())
    exclusive_write(STAGE / "dec.csv", expected_decision_bytes())
    exclusive_write(STAGE / "issues.csv", expected_issue_bytes())
    run_tool("srcmap/scan.py", STAGE)
    verify_scan(STAGE)
    run_tool("srcmap/map.py", STAGE)
    exclusive_write(STAGE / "STATUS.md", STATUS_BYTES)


def preflight() -> None:
    require(not TARGET.exists() and not STAGE.exists(), "r61 target or stage already exists")
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
                "schema": "tohoku-r61-static-input-audit-v1",
                "status": "PASS",
                "errors": [],
                "external": external,
                "scanner_oracles": oracles,
                "projection": projection,
                "decision": DECISION["decision_id"],
                "issue": ISSUE["issue_id"],
                "remaining_gaps": 25,
            },
            indent=2,
            sort_keys=True,
        )
    )


def execute() -> None:
    if TARGET.exists():
        replay()
        return
    require(not STAGE.exists(), "r61 stage already exists")
    build_stage()
    deltas = verify_stage(STAGE)
    receipt = receipt_payload(STAGE, deltas)
    exclusive_write(STAGE / "r61-check.json", json_bytes(receipt))
    verify_stage(STAGE, receipt_mode=True)
    require(not TARGET.exists(), "r61 target appeared before promotion")
    STAGE.rename(TARGET)
    try:
        verify_stage(TARGET, receipt_mode=True)
    except BaseException as exc:
        if TARGET.exists() and not STAGE.exists():
            TARGET.rename(STAGE)
        raise ContractError("Post-promotion r61 replay failed; target rolled back") from exc
    print(
        json.dumps(
            {
                "schema": "tohoku-r61-transaction-result-v1",
                "status": "PASS_COMMITTED",
                "errors": [],
                "target": "tohoku_r61",
                "receipt": record(TARGET / "r61-check.json"),
                "remaining_gaps": 25,
            },
            indent=2,
            sort_keys=True,
        )
    )


def replay() -> None:
    require(TARGET.is_dir() and not TARGET.is_symlink(), "r61 target missing or unsafe")
    require(not STAGE.exists(), "r61 stage unexpectedly exists")
    result = verify_stage(TARGET, receipt_mode=True)
    print(
        json.dumps(
            {
                "schema": "tohoku-r61-replay-v1",
                "status": "PASS_REPLAY",
                "errors": [],
                "receipt": record(TARGET / "r61-check.json"),
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
