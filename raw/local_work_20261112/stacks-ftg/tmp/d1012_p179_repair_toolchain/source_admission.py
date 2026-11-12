#!/usr/bin/env python3
"""Frozen, narrow D1012-R001 source-admission transaction.

The default mode is read-only preflight.  ``--execute`` is deliberately
required for any write.  The transaction never mutates production/p179_r1;
it creates the no-overwrite production/p179_fix2 successor and atomically
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
DESIGN = Path(r"user\Documents\stacks-ftg\tmp\d1012_source_repair_design.json")
D1010 = Path(r"user\Documents\stacks-ftg\D1010_CHECK.json")
BASE = ROOT / "production" / "p179_r1"
FINAL = ROOT / "production" / "p179_fix2"
STAGE = ROOT / "production" / ".p179_fix2.d1012.stage"
RECOVERY_STAGE = ROOT / "production" / ".p179_fix2.d1012.recovery"
SOURCE_LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
LEDGER_STAGE = ROOT / ".SOURCE_CORRECTIONS.jsonl.d1012.stage"
CHECK_STAGE_NAME = ".check.json.d1012.stage"
R18_SOURCE = ROOT / "build" / "v068c3r18" / "src"

DESIGN_EXPECTED = (11_812, "9F282268F4496469D2601BE25523EF6276F9CF15722D6F50A71B202F32E80B82")
D1010_EXPECTED = (37_425, "A73F16F4951CA5E04A6796586D7F522A22343164FC8AC5276CF5E64D4D8AC1E5")
SOURCE_LEDGER_PRE = (209_932, "0C9A8424C88DCF4F474ACF5EE7F8C0F8F51D0B1D1F1482E04B57ECD43DC80429")
SOURCE_LEDGER_POST = (211_141, "94F39C3058F24A0E8E43B3D3D98679C4EF265C23873ACE2B075F23F8810C262B")

BASE_FILES: dict[str, tuple[Path, int, str]] = {
    "decisions.jsonl": (BASE / "decisions.jsonl", 3_068, "0832EF49568DAC6A7335E7C8251BC16031C1BD7B065CAF329EE690BA389FA02C"),
    "targets.csv": (BASE / "targets.csv", 775, "A422666287FED6B65180FB6FC41B82E7B6850961741E7BA47014C4AAAC6CBAFF"),
    "reuse.txt": (BASE / "reuse.txt", 19, "C7BD41655D1420B139B0D69E6AA385AA8BDB6800FB99CB71BC16E6A98118B4BD"),
    "tex/fr_diplomatic/p179.tex": (BASE / "tex" / "fr_diplomatic" / "p179.tex", 4_413, "3B4424E98669777F4352A6911DA83D6391DD1412F79FE9C5EE77B8172DB75182"),
    "tex/fr_corrected/p179.tex": (BASE / "tex" / "fr_corrected" / "p179.tex", 4_347, "C3B0470AC85B9A34A0DFAAF5A0325690756C7FB541B12421CC651A29C7410CC7"),
    "tex/en/p179.tex": (BASE / "tex" / "en" / "p179.tex", 4_144, "3CD9D83B12C0B48B94577F0BBDA2E632B8E6EE8E7778B1B9442D5054D8505FE1"),
}

R18_P179: dict[str, tuple[Path, int, str]] = {
    "dip": (R18_SOURCE / "dip" / "p179.tex", 4_413, "3B4424E98669777F4352A6911DA83D6391DD1412F79FE9C5EE77B8172DB75182"),
    "fr": (R18_SOURCE / "fr" / "p179.tex", 4_347, "C3B0470AC85B9A34A0DFAAF5A0325690756C7FB541B12421CC651A29C7410CC7"),
    "en": (R18_SOURCE / "en" / "p179.tex", 4_144, "3CD9D83B12C0B48B94577F0BBDA2E632B8E6EE8E7778B1B9442D5054D8505FE1"),
}
SEAM_FILES: dict[str, tuple[Path, int, str]] = {
    "dip_p178": (R18_SOURCE / "dip" / "p178.tex", 4_772, "4D61949DE06125488FF777D6645F1961A126398A44CF6CE05A354DE1D48B3241"),
    "fr_p178": (R18_SOURCE / "fr" / "p178.tex", 4_855, "F123444D52AD9E31132F12F9F112E30FF767B6CB83E2C4A2AD9CEDCF8860854A"),
    "en_p178": (R18_SOURCE / "en" / "p178.tex", 4_689, "5930F4223C95E7AFDA05959943AD153759D76A24719D934270A2011041393B94"),
    "dip_p180": (R18_SOURCE / "dip" / "p180.tex", 4_626, "8AB7B01C86B798D9E5E9E0ECF7AB3791688EF7C8902A311DBFC0E5C93FED6A31"),
    "fr_p180": (R18_SOURCE / "fr" / "p180.tex", 5_138, "2F68D547A44E47A0F9CA5B602C440454D0244B3CA8EA62430DA0D6AAA9F83D18"),
    "en_p180": (R18_SOURCE / "en" / "p180.tex", 4_928, "F7D39A2F78D45C9CEA5A00360B96EBF6F1A5CBC656A8AB075DDE7B6093735961"),
}

TIMESTAMP = "2026-08-23T01:16:23Z"
FAMILY_ROW = {
    "decision_id": "TOH-P179-COR-002",
    "timestamp_utc": TIMESTAMP,
    "printed_page": 179,
    "kind": "authorial_correction_family",
    "decision": "Preserve the printed self-trace sentence diplomatically; in corrected French and English, quantify a second covering and require its trace on a member of the first covering to remain in the assigned covering family.",
    "evidence": "D1012-R001 design SHA-256 9F282268F4496469D2601BE25523EF6276F9CF15722D6F50A71B202F32E80B82; printed p.180 diplomatic/FR/EN SHA-256 8AB7B01C86B798D9E5E9E0ECF7AB3791688EF7C8902A311DBFC0E5C93FED6A31 / 2F68D547A44E47A0F9CA5B602C440454D0244B3CA8EA62430DA0D6AAA9F83D18 / F7D39A2F78D45C9CEA5A00360B96EBF6F1A5CBC656A8AB075DDE7B6093735961; the induction uses each cross-cover trace R_B^i for i=2,...,k on B in R^1.",
    "state": "active",
}
ROOT_ROW = {
    "decision_id": "TOH-SRC-P179-009",
    "timestamp_utc": TIMESTAMP,
    "corpus": "tohoku",
    "printed_page": 179,
    "layer": "fr_corrected;en",
    "kind": "source_internal_quantifier_correction",
    "source": "the printed setup requires only the trace of a covering on one of its own members to remain in the assigned covering family",
    "selected_editorial_correction": "retain the printed self-trace sentence diplomatically; in corrected French and English quantify R,R' in R(A), take B in R, and require the trace R'_B of R' on B to belong to R(B)",
    "rationale": "The p.180 induction takes B in R^1 and uses the traces R_B^i of different coverings R^i for i=2,...,k. The printed self-trace quantifier does not license those cross-cover traces; the correction supplies exactly the missing quantifier without changing the theorem or proof conclusion.",
    "evidence_channel": "TOH-P179-COR-002; D1012-R001 design SHA-256 9F282268F4496469D2601BE25523EF6276F9CF15722D6F50A71B202F32E80B82; p.180 diplomatic/FR/EN SHA-256 8AB7B01C86B798D9E5E9E0ECF7AB3791688EF7C8902A311DBFC0E5C93FED6A31 / 2F68D547A44E47A0F9CA5B602C440454D0244B3CA8EA62430DA0D6AAA9F83D18 / F7D39A2F78D45C9CEA5A00360B96EBF6F1A5CBC656A8AB075DDE7B6093735961",
    "state": "active",
}

FAMILY_ROW_EXPECTED = (795, "1D77631D3CDB439D20AF6B90ADE7934EAF6D6DFDF1A730FBA80E1AED32A45DE6")
ROOT_ROW_EXPECTED = (1_209, "893306E67DE4D30E642FEA990465EE6EDB3BF7C90A1CB6D7E9BDD2B3E915EA3D")
DECISIONS_POST = (3_863, "4B32C9521442CE2330068147C20ACE804A3D3C097E91FB83F02D501556D0200C")
FR_POST = (4_375, "27C6C84EEE0B74133B6376453801DF451B892FF782B7AC09E72146C4A7834C48")
EN_POST = (4_173, "A7491524DBAC64EA345B36384DE39F503A2F4680B995779DEB826D7C21443D73")
CHECK_EXPECTED = (4_425, "61AD974EC36B4FB525643EEABF7E12F57AC3FB2B80D7267D32DDCC83035D1D27")

FR_BEFORE = (
    "suppose que si $B\\in\\mathbf R\\in\\mathfrak R(A)$, alors la trace\n"
    "$\\mathbf R_B$ de $\\mathbf R$ sur $B$ appartient à $\\mathfrak R(B)$."
).encode("utf-8")
FR_AFTER = (
    "suppose que si $\\mathbf R,\\mathbf R'\\in\\mathfrak R(A)$ et\n"
    "$B\\in\\mathbf R$, alors la trace $\\mathbf R'_B$ de $\\mathbf R'$ sur $B$\n"
    "appartient à $\\mathfrak R(B)$."
).encode("utf-8")
EN_BEFORE = (
    "Assume that if $B\\in\\mathbf R\\in\\mathfrak R(A)$, then the trace\n"
    "$\\mathbf R_B$ of $\\mathbf R$ on $B$ belongs to $\\mathfrak R(B)$."
).encode("utf-8")
EN_AFTER = (
    "Assume that if $\\mathbf R,\\mathbf R'\\in\\mathfrak R(A)$ and\n"
    "$B\\in\\mathbf R$, then the trace $\\mathbf R'_B$ of $\\mathbf R'$ on $B$\n"
    "belongs to $\\mathfrak R(B)$."
).encode("utf-8")
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
            "design": {
                "bytes": DESIGN_EXPECTED[0],
                "path": DESIGN.as_posix(),
                "sha256": DESIGN_EXPECTED[1],
                "status": "DESIGN_PASS_NOT_APPLIED",
            },
            "proof_pages": {
                "dip_p180": {"bytes": 4_626, "sha256": SEAM_FILES["dip_p180"][2]},
                "en_p180": {"bytes": 4_928, "sha256": SEAM_FILES["en_p180"][2]},
                "fr_p180": {"bytes": 5_138, "sha256": SEAM_FILES["fr_p180"][2]},
            },
        },
        "created_utc": TIMESTAMP,
        "decision_id": "TOH-P179-COR-002",
        "decisions": {
            "append": {"bytes": FAMILY_ROW_EXPECTED[0], "sha256": FAMILY_ROW_EXPECTED[1]},
            "appended_id": "TOH-P179-COR-002",
            "appended_id_occurrences": 1,
            "appended_rows": 1,
            "postimage": {"bytes": DECISIONS_POST[0], "path": "production/p179_fix2/decisions.jsonl", "sha256": DECISIONS_POST[1]},
            "predecessor_prefix_exact": True,
            "preimage": {"bytes": 3_068, "path": "production/p179_r1/decisions.jsonl", "sha256": BASE_FILES["decisions.jsonl"][2]},
        },
        "defect_id": "D1012-R001",
        "errors": [],
        "exact_source_delta": {
            "corrected_french_replacements": 1,
            "diplomatic_french_changes": 0,
            "english_replacements": 1,
            "new_layer_targets": 0,
            "other_source_changes": 0,
            "p178_p179_p180_seams_stable": True,
            "target_sequence_count": 13,
        },
        "layers": {
            "corrected_french": {"bytes": FR_POST[0], "file": "tex/fr_corrected/p179.tex", "replacement_occurrences": 1, "sha256": FR_POST[1]},
            "diplomatic_french": {"bytes": 4_413, "file": "tex/fr_diplomatic/p179.tex", "predecessor_byte_exact": True, "sha256": BASE_FILES["tex/fr_diplomatic/p179.tex"][2]},
            "english": {"bytes": EN_POST[0], "file": "tex/en/p179.tex", "replacement_occurrences": 1, "sha256": EN_POST[1]},
        },
        "nonclaims": ["No reader build, QA, semantic graph, Stacks source, mapping, Git, GitHub, release, or publication is changed by this source-admission receipt."],
        "printed_page": 179,
        "production_successor": "production/p179_fix2",
        "reader_build_state": "NOT_LAUNCHED",
        "root_controls": {
            "source_corrections_file": {
                "append": {"bytes": ROOT_ROW_EXPECTED[0], "sha256": ROOT_ROW_EXPECTED[1]},
                "appended_id": "TOH-SRC-P179-009",
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
        "schema": "tohoku-p179-cross-cover-trace-source-admission-v1",
        "semantic_state": "UNCHANGED",
        "source_correction_id": "TOH-SRC-P179-009",
        "source_state": "admitted_no_overwrite_successor",
        "source_validation": {
            "continuation_anchor": 180,
            "control_byte_files": [],
            "cross_cover_trace_text_occurrences": {"dip": 0, "en": 1, "fr": 1},
            "jsonl_validation": "PASS",
            "layer_targets": {"dip": 13, "en": 13, "fr": 13},
            "source_page_anchor": 179,
            "target_occurrences": 13,
            "target_parity": "PASS",
        },
        "status": "PASS",
        "support": {
            "decisions": {"bytes": DECISIONS_POST[0], "file": "decisions.jsonl", "sha256": DECISIONS_POST[1]},
            "reuse": {"bytes": 19, "file": "reuse.txt", "sha256": BASE_FILES["reuse.txt"][2]},
            "targets": {"bytes": 775, "file": "targets.csv", "sha256": BASE_FILES["targets.csv"][2]},
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
    design = parse_json(exact(DESIGN, DESIGN_EXPECTED, "D1012-R001 design"), "D1012-R001 design")
    if design.get("status") != "DESIGN_PASS_NOT_APPLIED" or design.get("defect_id") != "D1012-R001":
        raise AdmissionError("design semantics drifted")
    d1010 = parse_json(exact(D1010, D1010_EXPECTED, "D1010 audit"), "D1010 audit")
    if d1010.get("status") != "STRICT_PASS" or d1010.get("formalization_id") != "D1010":
        raise AdmissionError("D1010 prior-pipeline receipt semantics drifted")

    base = {name: exact(path, (size, sha), f"p179 base {name}") for name, (path, size, sha) in BASE_FILES.items()}
    r18 = {name: exact(path, (size, sha), f"r18 p179 {name}") for name, (path, size, sha) in R18_P179.items()}
    seams = {name: exact(path, (size, sha), f"r18 seam {name}") for name, (path, size, sha) in SEAM_FILES.items()}
    if r18 != {
        "dip": base["tex/fr_diplomatic/p179.tex"],
        "fr": base["tex/fr_corrected/p179.tex"],
        "en": base["tex/en/p179.tex"],
    }:
        raise AdmissionError("p179 production and r18 staged preimages differ")

    family = row_bytes(FAMILY_ROW)
    root_row = row_bytes(ROOT_ROW)
    if (len(family), digest(family)) != FAMILY_ROW_EXPECTED or (len(root_row), digest(root_row)) != ROOT_ROW_EXPECTED:
        raise AdmissionError("frozen append-row serialization drifted")
    if ROOT_ROW.get("layer") != "fr_corrected;en":
        raise AdmissionError("root correction layer serialization is not exact")

    decisions = base["decisions.jsonl"] + family
    fr = replace_once(base["tex/fr_corrected/p179.tex"], FR_BEFORE, FR_AFTER, FR_POST, "corrected French p179")
    en = replace_once(base["tex/en/p179.tex"], EN_BEFORE, EN_AFTER, EN_POST, "English p179")
    payloads = {
        "decisions.jsonl": decisions,
        "reuse.txt": base["reuse.txt"],
        "targets.csv": base["targets.csv"],
        "tex/en/p179.tex": en,
        "tex/fr_corrected/p179.tex": fr,
        "tex/fr_diplomatic/p179.tex": base["tex/fr_diplomatic/p179.tex"],
    }
    if (len(decisions), digest(decisions)) != DECISIONS_POST or not decisions.startswith(base["decisions.jsonl"]):
        raise AdmissionError("family decision successor is not the exact prefix-plus-one postimage")
    family_rows = jsonl_rows(decisions, "p179 decisions successor")
    if sum(row.get("decision_id") == "TOH-P179-COR-002" for row in family_rows) != 1:
        raise AdmissionError("family append ID occurrence drifted")

    sequences = {
        "dip": layer_targets(payloads["tex/fr_diplomatic/p179.tex"]),
        "fr": layer_targets(fr),
        "en": layer_targets(en),
    }
    if any(len(value) != 13 for value in sequences.values()) or len({tuple(value) for value in sequences.values()}) != 1:
        raise AdmissionError("p179 LayerTarget inventory/parity drifted")
    for name, data in (("dip", payloads["tex/fr_diplomatic/p179.tex"]), ("fr", fr), ("en", en)):
        text = data.decode("utf-8", errors="strict")
        if text.count("\\SourcePage{179}") != 1 or text.count("\\TohokuContinuation{180}") != 1:
            raise AdmissionError(f"p179 source/seam anchor drifted: {name}")
    if payloads["tex/fr_diplomatic/p179.tex"].count(b"\\mathbf R'_B") != 0 or fr.count(b"\\mathbf R'_B") != 1 or en.count(b"\\mathbf R'_B") != 1:
        raise AdmissionError("cross-cover trace occurrence contract drifted")
    _ = seams

    preledger = exact(SOURCE_LEDGER, SOURCE_LEDGER_PRE, "source correction ledger preimage")
    pre_rows = jsonl_rows(preledger, "source correction ledger preimage")
    if len(pre_rows) != 379 or any(row.get("decision_id") == "TOH-SRC-P179-009" for row in pre_rows):
        raise AdmissionError("source ledger preimage ID surface drifted")
    postledger = preledger + root_row
    if (len(postledger), digest(postledger)) != SOURCE_LEDGER_POST or not postledger.startswith(preledger):
        raise AdmissionError("root ledger is not the exact prefix-plus-one postimage")
    post_rows = jsonl_rows(postledger, "source correction ledger postimage")
    if len(post_rows) != 380 or sum(row.get("decision_id") == "TOH-SRC-P179-009" for row in post_rows) != 1:
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
        raise AdmissionError("p179_fix2 final directory is invalid")
    expected_names = set(derived["payloads"]) | {"check.json"}
    actual_names: set[str] = set()
    for current, directories, files in os.walk(FINAL, topdown=True, followlinks=False):
        directories.sort()
        files.sort()
        base = Path(current)
        for name in directories:
            path = base / name
            if path.is_symlink() or not path.is_dir():
                raise AdmissionError(f"invalid p179_fix2 directory: {path}")
        for name in files:
            path = base / name
            if path.is_symlink() or not path.is_file():
                raise AdmissionError(f"invalid p179_fix2 file: {path}")
            actual_names.add(path.relative_to(FINAL).as_posix())
    if actual_names != expected_names:
        raise AdmissionError(f"p179_fix2 file surface drifted: {sorted(actual_names)}")
    for name, data in derived["payloads"].items():
        if exact(FINAL / Path(name), (len(data), digest(data)), f"committed {name}") != data:
            raise AdmissionError(f"committed {name} differs")
    check = exact(FINAL / "check.json", CHECK_EXPECTED, "committed p179_fix2 receipt")
    if check != derived["check"] or parse_json(check, "committed p179_fix2 receipt") != receipt():
        raise AdmissionError("committed p179_fix2 receipt readback differs")
    ledger = exact(SOURCE_LEDGER, SOURCE_LEDGER_POST, "committed source ledger")
    if ledger != derived["postledger"]:
        raise AdmissionError("committed source ledger differs from derived postimage")
    return {**derived["summary"], "status": "PASS_COMMITTED"}


def validate_recovery_candidate(derived: Mapping[str, Any]) -> None:
    """Require an exact, task-owned promoted surface before recovery rename."""
    if not FINAL.is_dir() or FINAL.is_symlink() or FINAL.resolve(strict=True) != FINAL:
        raise AdmissionError("cannot recover: promoted p179_fix2 directory is invalid")
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
        raise AdmissionError(f"cannot recover unexpected p179_fix2 surface: {sorted(actual)}")
    for name, data in derived["payloads"].items():
        if exact(FINAL / Path(name), (len(data), digest(data)), f"recovery candidate {name}") != data:
            raise AdmissionError(f"cannot recover drifted source payload: {name}")
    for name in ("check.json", CHECK_STAGE_NAME):
        path = FINAL / name
        if path.exists() and exact(path, CHECK_EXPECTED, f"recovery candidate {name}") != derived["check"]:
            raise AdmissionError(f"cannot recover drifted receipt payload: {name}")


def execute(derived: dict[str, Any]) -> dict[str, Any]:
    if os.path.lexists(FINAL) or os.path.lexists(STAGE) or os.path.lexists(RECOVERY_STAGE) or os.path.lexists(LEDGER_STAGE):
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
                raise AdmissionError("recovery namespace collision; refusing to move promoted p179_fix2")
            validate_recovery_candidate(derived)
        if ledger_committed:
            rollback_stage = ROOT / ".SOURCE_CORRECTIONS.jsonl.d1012.rollback.stage"
            if os.path.lexists(rollback_stage):
                raise AdmissionError("ledger rollback namespace collision")
            if not os.path.lexists(rollback_stage):
                fsync_write_new(rollback_stage, derived["preledger"])
                os.replace(rollback_stage, SOURCE_LEDGER)
        if promoted:
            os.rename(FINAL, RECOVERY_STAGE)
        raise


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Preflight or execute the frozen D1012-R001 p179 source admission.")
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
