#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r17 mapping builder."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r17.py"
EXPECTED = (
    44992,
    "33A70776A24E30B2EF14B3B5428F8029BDB4F39FF4384EC6FC2D789E31A209C4",
)


def main() -> int:
    payload = BUILDER.read_bytes()
    actual = (len(payload), hashlib.sha256(payload).hexdigest().upper())
    if actual != EXPECTED:
        raise RuntimeError(f"Builder identity drift: {actual}")
    namespace = {
        "__name__": "tohoku_r17_same_bytes_builder",
        "__file__": str(BUILDER),
        "EXECUTION_ATTESTATION": {
            "bootstrap": {
                "path": "srcmap/start_build_tohoku_r17.py",
                "contract": "read_once_then_execute_builder_same_bytes",
            },
            "builder": {
                "path": "srcmap/build_tohoku_r17.py",
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
