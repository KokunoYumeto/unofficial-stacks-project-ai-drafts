#!/usr/bin/env python3
"""Independent post-commit replay for the frozen D1029 source admission."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
FTG = Path(r"user\Documents\stacks-ftg")
FINAL = ROOT / "production" / "p188_fix1"
LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
SCRIPT = FTG / "tmp" / "d1029_source_repair_toolchain" / "source_admission.py"
SCRIPT_EXPECTED = (15175, "36AC1C07D311285065E784C7C9362E8E0F7BE1B89C0846E0131D60801C5EDE3D")
CHECK_EXPECTED = (4625, "52D174E72E44BE1DC5E6EE25A405B8C971EA4434F10BA7753F10CA1491851CF6")
LEDGER_PRE = (212239, "31E8894E57B355383B49BB403FAE65B935C81B4C1DAC65C17B20C3C7A6E70439")
LEDGER_POST = (213247, "F2DE702681CF4150C87FDC9C9051A105E94CBD681219ADC600DB9049B1E1E4B1")
IMMUTABLE_ROWS = {
    "TOH-P188-COR-001": (497, "FC20E82A11B21FCC91F24583BA5E1F0AE2D55F0BC6226B4C97A348CA51481704"),
    "TOH-SRC-P188-001": (495, "E0FE1A8B9EE41A4D8BCBA190B0D9BF7508840A486C9F33D2AD3F880D4CC7A7A4"),
    "TOH-SRC-P188-002": (515, "2824E87DCF9DF4C0802723BE4AB971C60B939C7C62E67AE253D01556914C267A"),
}


class ReplayError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise ReplayError(f"{label}: invalid path")
    data = path.read_bytes()
    if (len(data), sha(data)) != expected:
        raise ReplayError(f"{label}: identity drifted: {(len(data), sha(data))}")
    return data


def selected_row(data: bytes, decision_id: str) -> bytes:
    needle = f'"decision_id":"{decision_id}"'.encode()
    rows = [row for row in data.splitlines(keepends=True) if needle in row]
    if len(rows) != 1:
        raise ReplayError(f"{decision_id}: occurrence count {len(rows)}")
    return rows[0]


def main() -> int:
    script = exact(SCRIPT, SCRIPT_EXPECTED, "frozen source-admission script")
    check_data = exact(FINAL / "check.json", CHECK_EXPECTED, "source-admission receipt")
    check = json.loads(check_data.decode("utf-8"))
    if check.get("status") != "PASS" or check.get("errors") != []:
        raise ReplayError("source-admission receipt semantics drifted")
    if check.get("decision_id") != "TOH-P188-COR-002" or check.get("source_correction_id") != "TOH-SRC-P188-003":
        raise ReplayError("source-admission IDs drifted")
    if check.get("script") != {"path": str(SCRIPT), "bytes": len(script), "sha256": sha(script)}:
        raise ReplayError("receipt does not bind the frozen source-admission script")

    files = check.get("files", {})
    if set(files) != {
        "decisions.jsonl", "targets.csv", "reuse.txt",
        "tex/fr_diplomatic/p188.tex", "tex/fr_corrected/p188.tex", "tex/en/p188.tex",
    }:
        raise ReplayError("source-successor file surface drifted")
    payloads: dict[str, bytes] = {}
    for name, record in files.items():
        payloads[name] = exact(FINAL / Path(name), (record["bytes"], record["sha256"]), f"source-successor {name}")

    ledger = exact(LEDGER, LEDGER_POST, "source-correction ledger postimage")
    append_record = check["append_records"]["root_ledger"]
    appended = selected_row(ledger, "TOH-SRC-P188-003")
    if (len(appended), sha(appended)) != (append_record["bytes"], append_record["sha256"]):
        raise ReplayError("TOH-SRC-P188-003 row identity drifted")
    if not ledger.endswith(appended):
        raise ReplayError("TOH-SRC-P188-003 is not the exact final append")
    prefix = ledger[:-len(appended)]
    if (len(prefix), sha(prefix)) != LEDGER_PRE:
        raise ReplayError("source ledger predecessor prefix is not byte-exact")

    family = selected_row(payloads["decisions.jsonl"], "TOH-P188-COR-002")
    family_record = check["append_records"]["family"]
    if (len(family), sha(family)) != (family_record["bytes"], family_record["sha256"]):
        raise ReplayError("TOH-P188-COR-002 row identity drifted")
    for decision_id, expected in IMMUTABLE_ROWS.items():
        container = payloads["decisions.jsonl"] if decision_id.startswith("TOH-P188") else prefix
        old = selected_row(container, decision_id)
        if (len(old), sha(old)) != expected:
            raise ReplayError(f"immutable predecessor row changed: {decision_id}")

    dip = payloads["tex/fr_diplomatic/p188.tex"]
    fr = payloads["tex/fr_corrected/p188.tex"]
    en = payloads["tex/en/p188.tex"]
    if (len(dip), sha(dip)) != (3890, "0C9D3A1133C014C9BB6687580DCFBDE40A87B7FE21E98838BFD820983334D9FF"):
        raise ReplayError("diplomatic French changed")
    if fr.count(b"sur $\\Gamma(O^\\natural)$") != 1 or en.count(b"over $\\Gamma(O^\\natural)$") != 1:
        raise ReplayError("corrected scalar-ring phrase multiplicity drifted")
    if b"sur le centre de $\\Gamma(O)$" in fr or b"over the center of $\\Gamma(O)$" in en:
        raise ReplayError("false scalar-ring phrase survives corrected layer")

    result = {
        "schema": "tohoku-p188-ext-center-source-replay-v1",
        "status": "PASS_COMMITTED_AND_REPLAYED",
        "errors": [],
        "source_admission_script": {"path": str(SCRIPT), "bytes": len(script), "sha256": sha(script)},
        "source_admission_receipt": {"path": str(FINAL / "check.json"), "bytes": len(check_data), "sha256": sha(check_data)},
        "source_ledger": {"path": str(LEDGER), "bytes": len(ledger), "sha256": sha(ledger), "predecessor_prefix_exact": True},
        "immutable_predecessor_rows": {key: {"bytes": value[0], "sha256": value[1], "byte_identical": True} for key, value in IMMUTABLE_ROWS.items()},
        "diplomatic_french_byte_identical": True,
        "corrected_layer_delta_exact": True,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        raise SystemExit(1)
