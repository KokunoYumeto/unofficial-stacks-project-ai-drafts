#!/usr/bin/env python3
"""Append the five independently reviewed Tohoku r9 decision fragments exactly once."""

from __future__ import annotations

import csv
import hashlib
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOSSIER = ROOT / "tohoku_r9"
TARGET = DOSSIER / "dec.csv"
FRAGMENTS = (
    (ROOT / ".review-tohoku-r9-p119-166.csv", 34_716, "B2D20451F2C8586E24CFE7A4630B6A171188DB636CD2E0D4ED86D31EAA8FB940"),
    (ROOT / ".review-tohoku-r9-p167-185.csv", 29_875, "FCCA3E58CFB70CD5698AAC2877A9FB82C13810820E8F1DF4D7E86C1914042F53"),
    (ROOT / ".review-tohoku-r9-p186-203.csv", 32_301, "319CF0A4373CB73EB78FAEE673E4F45C94DE195500B78DFB8294BA1DFB5A9286"),
    (ROOT / ".review-tohoku-r9-p204-220.csv", 31_761, "EC46523CC3E68991D3608B33BFDBF18D1F06C0292449B7E436577900F64A490D"),
    (ROOT / ".review-tohoku-r9-bibliography.csv", 7_509, "54BB94B318C7EC393AD2FCA46259D6BEDB3B8FDBAB64101E6F8633CBB0F7AEF4"),
)
PREIMAGE = (65_376, "A8C5374BFF33BB998BBF7001CC9F4534CF664298D02EB73C1B2E1798493B60BD")
HEADER = (
    "decision_id,unit_id,action,disposition,stacks_labels,rationale,"
    "review_state,supersedes\n"
).encode("utf-8")


def identity(data: bytes) -> tuple[int, str]:
    return len(data), hashlib.sha256(data).hexdigest().upper()


def rows(data: bytes) -> list[dict[str, str]]:
    text = data.decode("utf-8")
    if "\r" in text or not text.endswith("\n"):
        raise ValueError("decision input is not canonical LF text")
    return list(csv.DictReader(text.splitlines()))


def main() -> int:
    before = TARGET.read_bytes()
    if identity(before) != PREIMAGE:
        raise ValueError("dec.csv preimage identity changed")
    old_rows = rows(before)
    fragment_rows: list[dict[str, str]] = []
    suffix = bytearray()
    for path, expected_bytes, expected_hash in FRAGMENTS:
        data = path.read_bytes()
        if identity(data) != (expected_bytes, expected_hash):
            raise ValueError(f"review fragment identity changed: {path.name}")
        if not data.startswith(HEADER):
            raise ValueError(f"unexpected review header: {path.name}")
        fragment_rows.extend(rows(data))
        suffix.extend(data[len(HEADER) :])
    combined = old_rows + fragment_rows
    expected_ids = [f"D{number:06d}" for number in range(1, len(combined) + 1)]
    if [row["decision_id"] for row in combined] != expected_ids:
        raise ValueError("combined decision IDs are not one contiguous prefix")
    unit_ids = [row["unit_id"] for row in combined]
    if len(set(unit_ids)) != len(unit_ids):
        raise ValueError("combined decisions contain duplicate units")
    after = before + bytes(suffix)
    temp = DOSSIER / ".dec.review-append.tmp"
    if temp.exists():
        raise FileExistsError(temp)
    with temp.open("xb") as handle:
        handle.write(after)
        handle.flush()
        os.fsync(handle.fileno())
    if temp.read_bytes() != after:
        raise OSError("decision temporary readback differs")
    temp.replace(TARGET)
    if TARGET.read_bytes() != after:
        raise OSError("decision promotion readback differs")
    size, sha256 = identity(after)
    print(f"decisions={len(combined)} bytes={size} sha256={sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
