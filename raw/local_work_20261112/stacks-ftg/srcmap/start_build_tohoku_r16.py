#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r16 mapping builder."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r16.py"
EXPECTED = (
    43588,
    "E0F27641B6CA8D55011B67D47D2EFD7F3C0D2407D24072AC5DA386F358747BE0",
)


def main() -> int:
    payload = BUILDER.read_bytes()
    actual = (len(payload), hashlib.sha256(payload).hexdigest().upper())
    if actual != EXPECTED:
        raise RuntimeError(f"Builder identity drift: {actual}")
    namespace = {
        "__name__": "tohoku_r16_same_bytes_builder",
        "__file__": str(BUILDER),
        "EXECUTION_ATTESTATION": {
            "bootstrap": {
                "path": "srcmap/start_build_tohoku_r16.py",
                "contract": "read_once_then_execute_builder_same_bytes",
            },
            "builder": {
                "path": "srcmap/build_tohoku_r16.py",
                "bytes": actual[0],
                "sha256": actual[1],
                "contract": "read_hash_compile_and_exec_same_payload",
            },
        },
    }
    code = compile(payload, str(BUILDER), "exec")
    exec(code, namespace)
    return int(namespace["main"]())


if __name__ == "__main__":
    raise SystemExit(main())
