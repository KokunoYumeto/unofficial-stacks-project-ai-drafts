#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r18 mapping builder."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r18.py"
EXPECTED = (
    40305,
    "14796865719E5DCC8AD4937333562CDB9A45E7A16394B492A5A551E6344CDC23",
)


def main() -> int:
    payload = BUILDER.read_bytes()
    actual = (len(payload), hashlib.sha256(payload).hexdigest().upper())
    if actual != EXPECTED:
        raise RuntimeError(f"Builder identity drift: {actual}")
    namespace = {
        "__name__": "tohoku_r18_same_bytes_builder",
        "__file__": str(BUILDER),
        "EXECUTION_ATTESTATION": {
            "bootstrap": {
                "path": "srcmap/start_build_tohoku_r18.py",
                "contract": "read_once_then_execute_builder_same_bytes",
            },
            "builder": {
                "path": "srcmap/build_tohoku_r18.py",
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
