#!/usr/bin/env python3
"""No-overwrite D1029 p.188 source admission.

Preflight is read-only. Execute creates production/p188_fix1 and atomically
appends one exact row to SOURCE_CORRECTIONS.jsonl. Replay verifies committed
bytes. Diplomatic French and all predecessor rows are immutable.
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
FTG = Path(r"user\Documents\stacks-ftg")
SCRIPT = Path(__file__).resolve(strict=True)
BASE = ROOT / "production" / "p188_r1"
FINAL = ROOT / "production" / "p188_fix1"
STAGE = ROOT / "production" / ".p188_fix1.d1029.stage"
RECOVERY = ROOT / "production" / ".p188_fix1.d1029.recovery"
LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
LEDGER_STAGE = ROOT / ".SOURCE_CORRECTIONS.jsonl.d1029.stage"
LEDGER_ROLLBACK = ROOT / ".SOURCE_CORRECTIONS.jsonl.d1029.rollback.stage"
CANDIDATE = FTG / "tmp" / "d1029_ext_center_actions_candidate.tex"
MATH_AUDIT = FTG / "tmp" / "d1029_ext_center_math_source_audit.json"

BASE_FILES: dict[str, tuple[int, str]] = {
    "decisions.jsonl": (3949, "085F664B32B1EBFA0D08A2BBE9A3215408BAD3778C65DF22FA2A2A11C79600E0"),
    "targets.csv": (613, "A7378FBB1ABEB836C834668C1E84E18A72D0613F2DA546E809B7293386294E01"),
    "reuse.txt": (37, "700C6F75C12D72DCCCAC7166921B065D504DA06B29EABEF868760767FAFA3207"),
    "tex/fr_diplomatic/p188.tex": (3890, "0C9D3A1133C014C9BB6687580DCFBDE40A87B7FE21E98838BFD820983334D9FF"),
    "tex/fr_corrected/p188.tex": (3623, "CB86F66DB892CDA79F1561AE42BFE39BD63BD0BE715F8E981589E19D08A9A212"),
    "tex/en/p188.tex": (3503, "E1F0A1F899A6E042220929DCA498426A3DDD255629C07B9D6D460EE99094A139"),
}
LEDGER_PRE = (212239, "31E8894E57B355383B49BB403FAE65B935C81B4C1DAC65C17B20C3C7A6E70439")
CANDIDATE_EXPECTED = (3189, "6B6566697F349854C1866661952A7AC5487FAFEB473354D4403E27886B3287FA")
MATH_AUDIT_EXPECTED = (14637, "35C3ECBD18B1F06036C58723D0B59E1CAD48BE29890E8E0026C0A99280A3EC64")
IMMUTABLE_ROWS = {
    "TOH-P188-COR-001": (497, "FC20E82A11B21FCC91F24583BA5E1F0AE2D55F0BC6226B4C97A348CA51481704"),
    "TOH-SRC-P188-001": (495, "E0FE1A8B9EE41A4D8BCBA190B0D9BF7508840A486C9F33D2AD3F880D4CC7A7A4"),
    "TOH-SRC-P188-002": (515, "2824E87DCF9DF4C0802723BE4AB971C60B939C7C62E67AE253D01556914C267A"),
}
TIMESTAMP = "2026-08-24T08:00:00Z"
FR_BEFORE = b"sur le centre de $\\Gamma(O)$"
FR_AFTER = b"sur $\\Gamma(O^\\natural)$"
EN_BEFORE = b"over the center of $\\Gamma(O)$"
EN_AFTER = b"over $\\Gamma(O^\\natural)$"
TARGET_RE = re.compile(rb"\\LayerTarget\{([^}]+)\}")
TARGET_ID = b"tohoku:remark:ext-center-modules"


class AdmissionError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def ident(data: bytes) -> dict[str, Any]:
    return {"bytes": len(data), "sha256": sha(data)}


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise AdmissionError(f"{label}: missing, non-regular, symlinked, or redirected")
    data = path.read_bytes()
    if (len(data), sha(data)) != expected:
        raise AdmissionError(f"{label}: identity drifted: {(len(data), sha(data))}")
    return data


def compact_row(value: Mapping[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")


def pretty(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def row_with_id(data: bytes, decision_id: str) -> bytes:
    needle = f'"decision_id":"{decision_id}"'.encode()
    rows = [line for line in data.splitlines(keepends=True) if needle in line]
    if len(rows) != 1:
        raise AdmissionError(f"{decision_id}: expected one exact predecessor row, found {len(rows)}")
    return rows[0]


def segment(data: bytes) -> bytes:
    marker = b"\\LayerTarget{" + TARGET_ID + b"}"
    if data.count(marker) != 1:
        raise AdmissionError("target LayerTarget multiplicity is not one")
    start = data.index(marker) + len(marker)
    end = data.find(b"\\LayerTarget{", start)
    return data[start:] if end < 0 else data[start:end]


def replace_once(data: bytes, before: bytes, after: bytes, label: str) -> bytes:
    if data.count(before) != 1 or data.count(after) != 0:
        raise AdmissionError(f"{label}: exact replacement precondition failed")
    result = data.replace(before, after)
    if result.count(after) != 1 or result.count(before) != 0:
        raise AdmissionError(f"{label}: exact replacement postcondition failed")
    return result


def family_row() -> dict[str, Any]:
    return {
        "decision_id": "TOH-P188-COR-002",
        "timestamp_utc": TIMESTAMP,
        "printed_page": 188,
        "kind": "authorial_correction_family",
        "decision": "Preserve the printed global Ext scalar-ring claim diplomatically; in corrected French and English replace the center of Gamma(O) by Gamma(O^natural), the global sections of the sheaf-theoretic center O^natural.",
        "evidence": "TOH-P188-COR-001 remains active and byte-identical for the earlier equation/article corrections; D1029 audit SHA-256 35C3ECBD18B1F06036C58723D0B59E1CAD48BE29890E8E0026C0A99280A3EC64; candidate SHA-256 6B6566697F349854C1866661952A7AC5487FAFEB473354D4403E27886B3287FA.",
        "state": "active",
    }


def ledger_row() -> dict[str, Any]:
    return {
        "decision_id": "TOH-SRC-P188-003",
        "timestamp_utc": TIMESTAMP,
        "corpus": "tohoku",
        "printed_page": 188,
        "layer": "fr_corrected;en",
        "kind": "source_internal_scalar_ring_correction",
        "source": "the printed sentence makes global Ext a module over the center of Gamma(O)",
        "selected_editorial_correction": "retain the printed sentence diplomatically; in corrected French and English make global Ext a module over Gamma(O^natural)",
        "rationale": "A section central among global sections need not restrict to a central local section. The canonical derived scalar action is by Gamma(X,Z_O)=Gamma(O^natural); the larger center Z(Gamma(X,O)) is recovered only when the canonical inclusion is an equality.",
        "evidence_channel": "TOH-P188-COR-002; D1029 audit SHA-256 35C3ECBD18B1F06036C58723D0B59E1CAD48BE29890E8E0026C0A99280A3EC64; modules-lemma-sheaf-hom-left-modules; cohomology-lemma-ext-center-actions-left-modules candidate SHA-256 6B6566697F349854C1866661952A7AC5487FAFEB473354D4403E27886B3287FA",
        "state": "active",
    }


def derive() -> dict[str, Any]:
    base = {name: exact(BASE / Path(name), spec, f"base {name}") for name, spec in BASE_FILES.items()}
    ledger = exact(LEDGER, LEDGER_PRE, "source ledger preimage")
    candidate = exact(CANDIDATE, CANDIDATE_EXPECTED, "D1029 candidate")
    audit = exact(MATH_AUDIT, MATH_AUDIT_EXPECTED, "D1029 math/source audit")
    if json.loads(audit.decode("utf-8"))["verdict"] != "STRICT_PASS":
        raise AdmissionError("D1029 math/source audit is not STRICT_PASS")
    for decision_id, expected in IMMUTABLE_ROWS.items():
        container = base["decisions.jsonl"] if decision_id.startswith("TOH-P188") else ledger
        old = row_with_id(container, decision_id)
        if (len(old), sha(old)) != expected:
            raise AdmissionError(f"immutable predecessor row drifted: {decision_id}")
    if b'"decision_id":"TOH-P188-COR-002"' in base["decisions.jsonl"] or b'"decision_id":"TOH-SRC-P188-003"' in ledger:
        raise AdmissionError("new D1029 ID is already occupied")
    if not base["decisions.jsonl"].endswith(b"\n") or not ledger.endswith(b"\n"):
        raise AdmissionError("append-only JSONL preimage lacks final LF")

    fr = replace_once(base["tex/fr_corrected/p188.tex"], FR_BEFORE, FR_AFTER, "corrected French")
    en = replace_once(base["tex/en/p188.tex"], EN_BEFORE, EN_AFTER, "English")
    dip = base["tex/fr_diplomatic/p188.tex"]
    for data in (dip, fr, en):
        if [x.decode("utf-8") for x in TARGET_RE.findall(data)].count(TARGET_ID.decode()) != 1:
            raise AdmissionError("target LayerTarget sequence drifted")
    if segment(dip) != segment(base["tex/fr_diplomatic/p188.tex"]):
        raise AdmissionError("diplomatic target segment changed")
    if b"\\Gamma(O^\\natural)" not in segment(fr) or b"\\Gamma(O^\\natural)" not in segment(en):
        raise AdmissionError("corrected scalar ring absent from target segment")

    family = compact_row(family_row())
    source = compact_row(ledger_row())
    decisions = base["decisions.jsonl"] + family
    postledger = ledger + source
    payloads = {
        "decisions.jsonl": decisions,
        "targets.csv": base["targets.csv"],
        "reuse.txt": base["reuse.txt"],
        "tex/fr_diplomatic/p188.tex": dip,
        "tex/fr_corrected/p188.tex": fr,
        "tex/en/p188.tex": en,
    }
    script_data = SCRIPT.read_bytes()
    receipt = {
        "schema": "tohoku-p188-ext-center-source-admission-v1",
        "created_utc": TIMESTAMP,
        "status": "PASS",
        "errors": [],
        "production_predecessor": "production/p188_r1",
        "production_successor": "production/p188_fix1",
        "decision_id": "TOH-P188-COR-002",
        "source_correction_id": "TOH-SRC-P188-003",
        "script": {"path": str(SCRIPT), **ident(script_data)},
        "formalization_bindings": {
            "candidate": {"path": str(CANDIDATE), **ident(candidate)},
            "math_source_audit": {"path": str(MATH_AUDIT), **ident(audit), "verdict": "STRICT_PASS"},
        },
        "immutable_predecessor_rows": {
            key: {"bytes": spec[0], "sha256": spec[1], "byte_identical_in_postimage": True}
            for key, spec in IMMUTABLE_ROWS.items()
        },
        "append_records": {
            "family": {"id": "TOH-P188-COR-002", **ident(family)},
            "root_ledger": {"id": "TOH-SRC-P188-003", **ident(source)},
        },
        "source_ledger": {
            "preimage": {"path": "SOURCE_CORRECTIONS.jsonl", **ident(ledger)},
            "postimage": {"path": "SOURCE_CORRECTIONS.jsonl", **ident(postledger)},
            "predecessor_prefix_exact": True,
        },
        "files": {name: ident(data) for name, data in sorted(payloads.items())},
        "layers": {
            "diplomatic": {**ident(dip), "predecessor_byte_exact": True, "segment": ident(segment(dip))},
            "corrected_french": {**ident(fr), "segment": ident(segment(fr))},
            "english": {**ident(en), "segment": ident(segment(en))},
        },
        "delta": {
            "changed_source_layers": ["tex/en/p188.tex", "tex/fr_corrected/p188.tex"],
            "unchanged_source_layers": ["tex/fr_diplomatic/p188.tex"],
            "exact_replacements": 2,
            "appended_decision_rows": 1,
            "appended_root_ledger_rows": 1,
            "layer_targets_preserved": True,
            "unrelated_source_changes": 0,
        },
        "scope": {"map_dossier_mutated": False, "live_stacks_tex_mutated": False, "git_used": False, "network_used": False},
    }
    check = pretty(receipt)
    return {"base": base, "preledger": ledger, "postledger": postledger, "payloads": payloads, "check": check, "receipt": receipt}


def namespace_check() -> None:
    occupied = [path for path in (FINAL, STAGE, RECOVERY, LEDGER_STAGE, LEDGER_ROLLBACK) if os.path.lexists(path)]
    if occupied:
        raise FileExistsError(f"D1029 no-overwrite namespace occupied: {occupied}")


def write_new(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def verify(derived: Mapping[str, Any]) -> dict[str, Any]:
    for name, data in {**derived["payloads"], "check.json": derived["check"]}.items():
        got = (FINAL / Path(name)).read_bytes()
        if got != data:
            raise AdmissionError(f"committed source payload differs: {name}")
    if LEDGER.read_bytes() != derived["postledger"]:
        raise AdmissionError("committed source ledger differs")
    for decision_id, expected in IMMUTABLE_ROWS.items():
        container = (FINAL / "decisions.jsonl").read_bytes() if decision_id.startswith("TOH-P188") else LEDGER.read_bytes()
        old = row_with_id(container, decision_id)
        if (len(old), sha(old)) != expected:
            raise AdmissionError(f"committed immutable row changed: {decision_id}")
    return {
        "status": "PASS_COMMITTED_AND_REPLAYED",
        "production_successor": str(FINAL),
        "receipt": {"path": str(FINAL / "check.json"), **ident(derived["check"])},
        "source_ledger": {"path": str(LEDGER), **ident(derived["postledger"])},
    }


def execute(derived: Mapping[str, Any]) -> dict[str, Any]:
    namespace_check()
    STAGE.mkdir(exist_ok=False)
    ledger_committed = False
    try:
        all_payloads = {**derived["payloads"], "check.json": derived["check"]}
        dirs = sorted({Path(name).parent for name in all_payloads if Path(name).parent != Path(".")}, key=lambda p: (len(p.parts), p.as_posix()))
        for rel in dirs:
            (STAGE / rel).mkdir(parents=True, exist_ok=False)
        for name, data in sorted(all_payloads.items()):
            write_new(STAGE / Path(name), data)
            if (STAGE / Path(name)).read_bytes() != data:
                raise AdmissionError(f"staged readback differs: {name}")
        write_new(LEDGER_STAGE, derived["postledger"])
        if LEDGER_STAGE.read_bytes() != derived["postledger"]:
            raise AdmissionError("ledger stage readback differs")
        os.replace(LEDGER_STAGE, LEDGER)
        ledger_committed = True
        os.rename(STAGE, FINAL)
        return verify(derived)
    except BaseException:
        if ledger_committed:
            write_new(LEDGER_ROLLBACK, derived["preledger"])
            os.replace(LEDGER_ROLLBACK, LEDGER)
        if STAGE.exists():
            os.rename(STAGE, RECOVERY)
        raise


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--execute", action="store_true")
    mode.add_argument("--replay", action="store_true")
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    derived = derive()
    if args.preflight:
        namespace_check()
        result = {"status": "READY_NOT_EXECUTED", **derived["receipt"]}
    elif args.execute:
        result = execute(derived)
    else:
        result = verify(derived)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
