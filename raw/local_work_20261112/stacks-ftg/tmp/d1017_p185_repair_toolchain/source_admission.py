#!/usr/bin/env python3
"""Frozen, narrow D1017-R001 source-admission transaction.

The default mode is read-only preflight.  ``--execute`` is deliberately
required for any write.  The transaction never mutates production/p185_r1;
it creates the no-overwrite production/p185_fix2 successor and atomically
replaces SOURCE_CORRECTIONS.jsonl by its exact one-row append postimage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SCRIPT = Path(__file__).resolve(strict=True)
BASE = ROOT / "production" / "p185_r1"
FINAL = ROOT / "production" / "p185_fix2"
STAGE = ROOT / "production" / ".p185_fix2.d1017.stage"
RECOVERY_STAGE = ROOT / "production" / ".p185_fix2.d1017.recovery"
SOURCE_LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
LEDGER_STAGE = ROOT / ".SOURCE_CORRECTIONS.jsonl.d1017.stage"
LEDGER_ROLLBACK_STAGE = ROOT / ".SOURCE_CORRECTIONS.jsonl.d1017.rollback.stage"
CHECK_STAGE_NAME = ".check.json.d1017.stage"
R19_SOURCE = ROOT / "build" / "v068c3r19" / "src"

SOURCE_LEDGER_PRE = (211_141, "94F39C3058F24A0E8E43B3D3D98679C4EF265C23873ACE2B075F23F8810C262B")
# Filled from the exact prefix-plus-one serialization below.
SOURCE_LEDGER_POST = (212_239, "31E8894E57B355383B49BB403FAE65B935C81B4C1DAC65C17B20C3C7A6E70439")

BASE_FILES: dict[str, tuple[Path, int, str]] = {
    "decisions.jsonl": (BASE / "decisions.jsonl", 2_717, "7BFEA250C3BA8D14D8D9225B3CE0F4F4B64A4D7ECCA41BCD40CDEBF224F68C63"),
    "targets.csv": (BASE / "targets.csv", 735, "1E9B7D440E52EC56F1BB64563B8A1243556E25CAE8083F24FC5BF08EDF8832BF"),
    "reuse.txt": (BASE / "reuse.txt", 37, "E18934ADECB524EE2605B24D065861B042487811117719A3CD7B919CE5CCE06A"),
    "tex/fr_diplomatic/p185.tex": (BASE / "tex" / "fr_diplomatic" / "p185.tex", 3_964, "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A"),
    "tex/fr_corrected/p185.tex": (BASE / "tex" / "fr_corrected" / "p185.tex", 4_302, "85D04A11FF28F109C9006A850A3D9176A6483C2CAC56AA9B849058934B65C54A"),
    "tex/en/p185.tex": (BASE / "tex" / "en" / "p185.tex", 4_183, "6D15A561E5FCE6D3071672663DE9969249A5D147F08D6DC61A7CD5F3E43A084D"),
}

R19_P185: dict[str, tuple[Path, int, str]] = {
    "dip": (R19_SOURCE / "dip" / "p185.tex", 3_964, "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A"),
    "fr": (R19_SOURCE / "fr" / "p185.tex", 4_302, "85D04A11FF28F109C9006A850A3D9176A6483C2CAC56AA9B849058934B65C54A"),
    "en": (R19_SOURCE / "en" / "p185.tex", 4_183, "6D15A561E5FCE6D3071672663DE9969249A5D147F08D6DC61A7CD5F3E43A084D"),
}
SEAM_FILES: dict[str, tuple[Path, int, str]] = {
    "dip_p183": (R19_SOURCE / "dip" / "p183.tex", 1_895, "78B6E80B3976F53CB2FE192BA697705068660BB36133BE27C1D7D0F104934151"),
    "fr_p183": (R19_SOURCE / "fr" / "p183.tex", 1_912, "E4B5557C680DDE305F01E606D6F73E4D5919FF61E1C4764BAEC27825546DA662"),
    "en_p183": (R19_SOURCE / "en" / "p183.tex", 1_807, "78ACD8361B6528CDCD7E61C40E949CAC5C4CB3AF2AD1DBBD0C745179C54C2842"),
    "dip_p186": (R19_SOURCE / "dip" / "p186.tex", 4_168, "BB9960A3EBAEFC142F18CE93F9CB3AB1D1EE9735F553E0653D912C30C591B355"),
    "fr_p186": (R19_SOURCE / "fr" / "p186.tex", 3_904, "CD2E0A570004B73FEC05C8A8045D721811040275B05B39A2F81A7CC6B3EB3F91"),
    "en_p186": (R19_SOURCE / "en" / "p186.tex", 3_667, "536B9C5C6C23BF8CEB0B783F065B5ED465411BA00EDE11F2B197C7217996013E"),
}

TIMESTAMP = "2026-08-23T21:28:01Z"
FAMILY_ROW = {
    "decision_id": "TOH-P185-COR-002",
    "timestamp_utc": TIMESTAMP,
    "printed_page": 185,
    "kind": "authorial_correction_family",
    "decision": "Preserve the printed scalar-ring claim diplomatically; in corrected French and English replace the center of Gamma(O) by Gamma(O^natural), the global sections of the sheaf-theoretic center O^natural.",
    "evidence": "Printed p.185 diplomatic/FR/EN SHA-256 C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A / 85D04A11FF28F109C9006A850A3D9176A6483C2CAC56AA9B849058934B65C54A / 6D15A561E5FCE6D3071672663DE9969249A5D147F08D6DC61A7CD5F3E43A084D; the immediately following source target states that the sheaf Hom is an O^natural-module sheaf, so its global sections carry the canonical Gamma(O^natural)-action.",
    "state": "active",
}
ROOT_ROW = {
    "decision_id": "TOH-SRC-P185-002",
    "timestamp_utc": TIMESTAMP,
    "corpus": "tohoku",
    "printed_page": 185,
    "layer": "fr_corrected;en",
    "kind": "source_internal_scalar_ring_correction",
    "source": "the printed sentence makes Hom_O(A,B) a module over the center of Gamma(O)",
    "selected_editorial_correction": "retain the printed sentence diplomatically; in corrected French and English make Hom_O(A,B) a module over Gamma(O^natural)",
    "rationale": "A section central among global sections need not commute with every local section, so the center of Gamma(O) does not canonically act on arbitrary sheaf O-module homomorphisms. The following source target identifies sheaf Hom as an O^natural-module sheaf, and global sections therefore give the required Gamma(O^natural)-action.",
    "evidence_channel": "TOH-P185-COR-002; p.185 diplomatic/FR/EN SHA-256 C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A / 85D04A11FF28F109C9006A850A3D9176A6483C2CAC56AA9B849058934B65C54A / 6D15A561E5FCE6D3071672663DE9969249A5D147F08D6DC61A7CD5F3E43A084D; tohoku:remark:sheaf-hom-o:center-module",
    "state": "active",
}

FAMILY_ROW_EXPECTED = (776, "E5DCC58D900A1F5EB80D8CB7FDE543B7F15B306FED5711754FE50AE7D6AC8A7A")
ROOT_ROW_EXPECTED = (1_098, "ED03ED1D5B4597056D798FA1C22624016D5D2A6D568516E000DB38F6BA790B83")
DECISIONS_POST = (3_493, "BB7813EA38AD72B878C4AE825141A82FEF092F8A99FEDDD7397AE705A56D4D4B")
FR_POST = (4_298, "EBE37CBFBE00FA4CA72C21CC4C542D60603A61E92EE446D15C941FA136B20847")
EN_POST = (4_178, "9F3F8C932149B3F2ECC9A25C4D4C2D010A48A2CFE6B621CE12BE178CC4DADE60")
CHECK_EXPECTED = (5_291, "E54AE998A9D8AB863652521E329731789727DD064B48E6A52CAB83584C802EEA")

FR_BEFORE = b"sur le centre de $\\Gamma(O)$"
FR_AFTER = b"sur $\\Gamma(O^\\natural)$"
EN_BEFORE = b"over the center of $\\Gamma(O)$"
EN_AFTER = b"over $\\Gamma(O^\\natural)$"
TARGET_RE = re.compile(rb"\\LayerTarget\{([^}]+)\}")
snapshot_record = globals().get("__verified_script_snapshot__")


class AdmissionError(RuntimeError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(data: bytes) -> dict[str, Any]:
    return {"bytes": len(data), "sha256": digest(data)}


def row_bytes(value: Mapping[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


def pretty_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def require_regular(path: Path, label: str) -> None:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise AdmissionError(f"{label}: missing, non-regular, symlinked, or redirected")


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    require_regular(path, label)
    data = path.read_bytes()
    actual = (len(data), digest(data))
    if actual != expected:
        raise AdmissionError(f"{label}: identity drifted: {actual}")
    return data


def parse_json(data: bytes, label: str) -> dict[str, Any]:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in items:
            if key in out:
                raise AdmissionError(f"{label}: duplicate JSON key {key}")
            out[key] = value
        return out

    value = json.loads(data.decode("utf-8", errors="strict"), object_pairs_hook=pairs)
    if not isinstance(value, dict):
        raise AdmissionError(f"{label}: JSON root is not an object")
    return value


def jsonl_rows(data: bytes, label: str) -> list[dict[str, Any]]:
    lines = data.decode("utf-8", errors="strict").splitlines()
    if not lines or any(not line for line in lines):
        raise AdmissionError(f"{label}: blank or absent JSONL row")
    rows = [parse_json(line.encode("utf-8"), f"{label}:{number}") for number, line in enumerate(lines, 1)]
    ids = [row.get("decision_id") for row in rows]
    if any(not isinstance(value, str) or not value for value in ids) or len(ids) != len(set(ids)):
        raise AdmissionError(f"{label}: invalid or duplicate decision IDs")
    return rows


def replace_once(data: bytes, before: bytes, after: bytes, expected: tuple[int, str], label: str) -> bytes:
    if data.count(before) != 1 or after in data:
        raise AdmissionError(f"{label}: exact replacement precondition failed")
    result = data.replace(before, after)
    if (len(result), digest(result)) != expected:
        raise AdmissionError(f"{label}: projected replacement identity drifted")
    return result


def layer_targets(data: bytes) -> list[str]:
    return [value.decode("utf-8", errors="strict") for value in TARGET_RE.findall(data)]


def receipt() -> dict[str, Any]:
    return {
        "authority": {
            "printed_page_185": {
                "dip": {"bytes": 3_964, "sha256": BASE_FILES["tex/fr_diplomatic/p185.tex"][2]},
                "fr": {"bytes": 4_302, "sha256": BASE_FILES["tex/fr_corrected/p185.tex"][2]},
                "en": {"bytes": 4_183, "sha256": BASE_FILES["tex/en/p185.tex"][2]},
            },
            "seam_pages": {
                name: {"bytes": spec[1], "sha256": spec[2]}
                for name, spec in sorted(SEAM_FILES.items())
            },
            "internal_witness": "tohoku:remark:sheaf-hom-o:center-module",
        },
        "created_utc": TIMESTAMP,
        "decision_id": "TOH-P185-COR-002",
        "decisions": {
            "append": {"bytes": FAMILY_ROW_EXPECTED[0], "sha256": FAMILY_ROW_EXPECTED[1]},
            "appended_id": "TOH-P185-COR-002",
            "appended_id_occurrences": 1,
            "appended_rows": 1,
            "postimage": {"bytes": DECISIONS_POST[0], "path": "production/p185_fix2/decisions.jsonl", "sha256": DECISIONS_POST[1]},
            "predecessor_prefix_exact": True,
            "preimage": {"bytes": 2_717, "path": "production/p185_r1/decisions.jsonl", "sha256": BASE_FILES["decisions.jsonl"][2]},
        },
        "defect_id": "D1017-R001",
        "errors": [],
        "exact_source_delta": {
            "corrected_french_replacements": 1,
            "diplomatic_french_changes": 0,
            "english_replacements": 1,
            "new_layer_targets": 0,
            "other_source_changes": 0,
            "p183_part_boundary_and_p185_p186_seam_stable": True,
            "target_sequence_count": 13,
        },
        "layers": {
            "corrected_french": {"bytes": FR_POST[0], "file": "tex/fr_corrected/p185.tex", "replacement_occurrences": 1, "sha256": FR_POST[1]},
            "diplomatic_french": {"bytes": 3_964, "file": "tex/fr_diplomatic/p185.tex", "predecessor_byte_exact": True, "sha256": BASE_FILES["tex/fr_diplomatic/p185.tex"][2]},
            "english": {"bytes": EN_POST[0], "file": "tex/en/p185.tex", "replacement_occurrences": 1, "sha256": EN_POST[1]},
        },
        "nonclaims": ["No reader build, QA, semantic graph, Stacks source, mapping, Git, GitHub, release, or publication is changed by this source-admission receipt."],
        "printed_page": 185,
        "production_successor": "production/p185_fix2",
        "reader_build_state": "NOT_LAUNCHED",
        "root_controls": {
            "source_corrections_file": {
                "append": {"bytes": ROOT_ROW_EXPECTED[0], "sha256": ROOT_ROW_EXPECTED[1]},
                "appended_id": "TOH-SRC-P185-002",
                "appended_id_occurrences": 1,
                "appended_rows": 1,
                "path": "SOURCE_CORRECTIONS.jsonl",
                "postimage_bytes": SOURCE_LEDGER_POST[0],
                "postimage_sha256": SOURCE_LEDGER_POST[1],
                "predecessor_prefix_exact": True,
                "preimage_bytes": SOURCE_LEDGER_PRE[0],
                "preimage_sha256": SOURCE_LEDGER_PRE[1],
            }
        },
        "schema": "tohoku-p185-sheaf-center-global-sections-source-admission-v1",
        "semantic_state": "UNCHANGED",
        "source_correction_id": "TOH-SRC-P185-002",
        "source_state": "admitted_no_overwrite_successor",
        "source_validation": {
            "continuation_anchor": 186,
            "control_byte_files": sorted(SEAM_FILES),
            "gamma_of_center_occurrences": {"dip": 0, "en": 1, "fr": 1},
            "printed_center_of_gamma_occurrences": {"dip": 1, "en": 0, "fr": 0},
            "jsonl_validation": "PASS",
            "layer_targets": {"dip": 13, "en": 13, "fr": 13},
            "source_page_anchor": 185,
            "target_occurrences": 13,
            "target_parity": "PASS",
        },
        "status": "PASS",
        "support": {
            "decisions": {"bytes": DECISIONS_POST[0], "file": "decisions.jsonl", "sha256": DECISIONS_POST[1]},
            "reuse": {"bytes": 37, "file": "reuse.txt", "sha256": BASE_FILES["reuse.txt"][2]},
            "targets": {"bytes": 735, "file": "targets.csv", "sha256": BASE_FILES["targets.csv"][2]},
        },
    }


def require_snapshot() -> dict[str, Any]:
    record = snapshot_record
    if not isinstance(record, dict) or set(record) != {"path", "bytes", "sha256", "contract"}:
        raise AdmissionError("launch through run.py; verified script snapshot is absent")
    live = SCRIPT.read_bytes()
    if (
        record["path"] != str(SCRIPT)
        or record["contract"] != "contract_json_read_hash_then_exec_same_bytes"
        or (len(live), digest(live)) != (record["bytes"], record["sha256"])
    ):
        raise AdmissionError("verified script snapshot drifted")
    return dict(record)


def derive() -> dict[str, Any]:
    base = {name: exact(path, (size, sha), f"p185 base {name}") for name, (path, size, sha) in BASE_FILES.items()}
    r19 = {name: exact(path, (size, sha), f"r19 p185 {name}") for name, (path, size, sha) in R19_P185.items()}
    seams = {name: exact(path, (size, sha), f"r19 seam {name}") for name, (path, size, sha) in SEAM_FILES.items()}
    if r19 != {
        "dip": base["tex/fr_diplomatic/p185.tex"],
        "fr": base["tex/fr_corrected/p185.tex"],
        "en": base["tex/en/p185.tex"],
    }:
        raise AdmissionError("p185 production and r19 staged preimages differ")

    family = row_bytes(FAMILY_ROW)
    root_row = row_bytes(ROOT_ROW)
    if (len(family), digest(family)) != FAMILY_ROW_EXPECTED or (len(root_row), digest(root_row)) != ROOT_ROW_EXPECTED:
        raise AdmissionError("frozen append-row serialization drifted")
    if ROOT_ROW.get("layer") != "fr_corrected;en":
        raise AdmissionError("root correction layer serialization is not exact")

    decisions = base["decisions.jsonl"] + family
    fr = replace_once(base["tex/fr_corrected/p185.tex"], FR_BEFORE, FR_AFTER, FR_POST, "corrected French p185")
    en = replace_once(base["tex/en/p185.tex"], EN_BEFORE, EN_AFTER, EN_POST, "English p185")
    payloads = {
        "decisions.jsonl": decisions,
        "reuse.txt": base["reuse.txt"],
        "targets.csv": base["targets.csv"],
        "tex/en/p185.tex": en,
        "tex/fr_corrected/p185.tex": fr,
        "tex/fr_diplomatic/p185.tex": base["tex/fr_diplomatic/p185.tex"],
    }
    if (len(decisions), digest(decisions)) != DECISIONS_POST or not decisions.startswith(base["decisions.jsonl"]):
        raise AdmissionError("family decision successor is not the exact prefix-plus-one postimage")
    family_rows = jsonl_rows(decisions, "p185 decisions successor")
    if sum(row.get("decision_id") == "TOH-P185-COR-002" for row in family_rows) != 1:
        raise AdmissionError("family append ID occurrence drifted")

    sequences = {
        "dip": layer_targets(payloads["tex/fr_diplomatic/p185.tex"]),
        "fr": layer_targets(fr),
        "en": layer_targets(en),
    }
    if any(len(value) != 13 for value in sequences.values()) or len({tuple(value) for value in sequences.values()}) != 1:
        raise AdmissionError("p185 LayerTarget inventory/parity drifted")
    for name, data in (("dip", payloads["tex/fr_diplomatic/p185.tex"]), ("fr", fr), ("en", en)):
        text = data.decode("utf-8", errors="strict")
        if text.count("\\SourcePage{185}") != 1 or text.count("\\TohokuContinuation{186}") != 1:
            raise AdmissionError(f"p185 source/seam anchor drifted: {name}")
    dip = payloads["tex/fr_diplomatic/p185.tex"]
    if dip.count(FR_BEFORE) != 1 or dip.count(FR_AFTER) != 0:
        raise AdmissionError("diplomatic scalar-ring wording drifted")
    if fr.count(FR_BEFORE) != 0 or fr.count(FR_AFTER) != 1:
        raise AdmissionError("corrected French scalar-ring wording drifted")
    if en.count(EN_BEFORE) != 0 or en.count(EN_AFTER) != 1:
        raise AdmissionError("English scalar-ring wording drifted")
    _ = seams

    preledger = exact(SOURCE_LEDGER, SOURCE_LEDGER_PRE, "source correction ledger preimage")
    pre_rows = jsonl_rows(preledger, "source correction ledger preimage")
    if (
        len(pre_rows) != 380
        or sum(row.get("decision_id") == "TOH-SRC-P185-001" for row in pre_rows) != 1
        or any(row.get("decision_id") == "TOH-SRC-P185-002" for row in pre_rows)
    ):
        raise AdmissionError("source ledger preimage ID surface drifted")
    postledger = preledger + root_row
    if (len(postledger), digest(postledger)) != SOURCE_LEDGER_POST or not postledger.startswith(preledger):
        raise AdmissionError("root ledger is not the exact prefix-plus-one postimage")
    post_rows = jsonl_rows(postledger, "source correction ledger postimage")
    if len(post_rows) != 381 or sum(row.get("decision_id") == "TOH-SRC-P185-002" for row in post_rows) != 1:
        raise AdmissionError("source ledger successor ID surface drifted")

    check = pretty_bytes(receipt())
    if (len(check), digest(check)) != CHECK_EXPECTED:
        raise AdmissionError("frozen source-admission receipt serialization drifted")
    return {
        "payloads": payloads,
        "preledger": preledger,
        "postledger": postledger,
        "check": check,
        "summary": {
            "status": "READY_NOT_EXECUTED",
            "production_successor": str(FINAL),
            "root_ledger_postimage": {"path": str(SOURCE_LEDGER), **identity(postledger)},
            "files": {name: identity(data) for name, data in sorted(payloads.items())},
            "receipt": {"path": str(FINAL / "check.json"), **identity(check)},
        },
    }


def fsync_write_new(path: Path, data: bytes) -> None:
    with path.open("xb") as output:
        output.write(data)
        output.flush()
        os.fsync(output.fileno())


def verify_final(derived: Mapping[str, Any]) -> dict[str, Any]:
    if not FINAL.is_dir() or FINAL.is_symlink() or FINAL.resolve(strict=True) != FINAL:
        raise AdmissionError("p185_fix2 final directory is invalid")
    expected_names = set(derived["payloads"]) | {"check.json"}
    actual_names: set[str] = set()
    for current, directories, files in os.walk(FINAL, topdown=True, followlinks=False):
        directories.sort()
        files.sort()
        base = Path(current)
        for name in directories:
            path = base / name
            if path.is_symlink() or not path.is_dir():
                raise AdmissionError(f"invalid p185_fix2 directory: {path}")
        for name in files:
            path = base / name
            if path.is_symlink() or not path.is_file():
                raise AdmissionError(f"invalid p185_fix2 file: {path}")
            actual_names.add(path.relative_to(FINAL).as_posix())
    if actual_names != expected_names:
        raise AdmissionError(f"p185_fix2 file surface drifted: {sorted(actual_names)}")
    for name, data in derived["payloads"].items():
        if exact(FINAL / Path(name), (len(data), digest(data)), f"committed {name}") != data:
            raise AdmissionError(f"committed {name} differs")
    check = exact(FINAL / "check.json", CHECK_EXPECTED, "committed p185_fix2 receipt")
    if check != derived["check"] or parse_json(check, "committed p185_fix2 receipt") != receipt():
        raise AdmissionError("committed p185_fix2 receipt readback differs")
    ledger = exact(SOURCE_LEDGER, SOURCE_LEDGER_POST, "committed source ledger")
    if ledger != derived["postledger"]:
        raise AdmissionError("committed source ledger differs from derived postimage")
    return {**derived["summary"], "status": "PASS_COMMITTED"}


def validate_recovery_candidate(derived: Mapping[str, Any]) -> None:
    """Require an exact, task-owned promoted surface before recovery rename."""
    if not FINAL.is_dir() or FINAL.is_symlink() or FINAL.resolve(strict=True) != FINAL:
        raise AdmissionError("cannot recover: promoted p185_fix2 directory is invalid")
    required = set(derived["payloads"])
    allowed = required | {"check.json", CHECK_STAGE_NAME}
    actual: set[str] = set()
    for current, directories, files in os.walk(FINAL, topdown=True, followlinks=False):
        directories.sort()
        files.sort()
        base = Path(current)
        for name in directories:
            path = base / name
            if path.is_symlink() or not path.is_dir():
                raise AdmissionError(f"cannot recover invalid directory: {path}")
        for name in files:
            path = base / name
            if path.is_symlink() or not path.is_file():
                raise AdmissionError(f"cannot recover invalid file: {path}")
            actual.add(path.relative_to(FINAL).as_posix())
    if not required.issubset(actual) or not actual.issubset(allowed):
        raise AdmissionError(f"cannot recover unexpected p185_fix2 surface: {sorted(actual)}")
    for name, data in derived["payloads"].items():
        if exact(FINAL / Path(name), (len(data), digest(data)), f"recovery candidate {name}") != data:
            raise AdmissionError(f"cannot recover drifted source payload: {name}")
    for name in ("check.json", CHECK_STAGE_NAME):
        path = FINAL / name
        if path.exists() and exact(path, CHECK_EXPECTED, f"recovery candidate {name}") != derived["check"]:
            raise AdmissionError(f"cannot recover drifted receipt payload: {name}")


def execute(derived: dict[str, Any]) -> dict[str, Any]:
    if any(os.path.lexists(path) for path in (FINAL, STAGE, RECOVERY_STAGE, LEDGER_STAGE, LEDGER_ROLLBACK_STAGE)):
        raise FileExistsError("fresh source-admission namespace is not empty")
    STAGE.mkdir(exist_ok=False)
    promoted = False
    ledger_committed = False
    try:
        directories = sorted({Path(name).parent for name in derived["payloads"] if Path(name).parent != Path(".")}, key=lambda value: (len(value.parts), value.as_posix()))
        for relative in directories:
            (STAGE / relative).mkdir(parents=True, exist_ok=False)
        for name, data in sorted(derived["payloads"].items()):
            fsync_write_new(STAGE / Path(name), data)
        for name, data in derived["payloads"].items():
            if exact(STAGE / Path(name), (len(data), digest(data)), f"staged {name}") != data:
                raise AdmissionError(f"staged {name} differs")
        fsync_write_new(LEDGER_STAGE, derived["postledger"])
        if exact(LEDGER_STAGE, SOURCE_LEDGER_POST, "staged root ledger") != derived["postledger"]:
            raise AdmissionError("staged root ledger readback differs")

        os.rename(STAGE, FINAL)
        promoted = True
        os.replace(LEDGER_STAGE, SOURCE_LEDGER)
        ledger_committed = True
        if exact(SOURCE_LEDGER, SOURCE_LEDGER_POST, "post-replace root ledger") != derived["postledger"]:
            raise AdmissionError("root ledger post-replace readback differs")
        check_stage = FINAL / CHECK_STAGE_NAME
        fsync_write_new(check_stage, derived["check"])
        if exact(check_stage, CHECK_EXPECTED, "source receipt stage") != derived["check"]:
            raise AdmissionError("source receipt stage readback differs")
        os.rename(check_stage, FINAL / "check.json")
        return verify_final(derived)
    except BaseException:
        if promoted:
            if os.path.lexists(STAGE) or os.path.lexists(RECOVERY_STAGE):
                raise AdmissionError("recovery namespace collision; refusing to move promoted p185_fix2")
            validate_recovery_candidate(derived)
        if ledger_committed:
            if os.path.lexists(LEDGER_ROLLBACK_STAGE):
                raise AdmissionError("ledger rollback namespace collision")
            fsync_write_new(LEDGER_ROLLBACK_STAGE, derived["preledger"])
            os.replace(LEDGER_ROLLBACK_STAGE, SOURCE_LEDGER)
        if promoted:
            os.rename(FINAL, RECOVERY_STAGE)
        raise


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Preflight or execute the frozen D1017-R001 p185 source admission.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--execute", action="store_true")
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    launch = require_snapshot()
    derived = derive()
    result = derived["summary"] if args.preflight else execute(derived)
    result = {**result, "script": launch}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
