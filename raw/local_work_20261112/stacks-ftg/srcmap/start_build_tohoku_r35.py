#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r35 mapping builder."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r35.py"
EXPECTED = (
    46073,
    "382AE146E371D8DB6FD53FC687EBEE9B6382EBCE1BBC25E83E2A0837168833FB",
)


def main() -> int:
    if os.environ.pop("TOHOKU_R35_ENVELOPE", "") != "tohoku-r35-same-bytes-envelope-v1":
        raise RuntimeError("Run through start_build_tohoku_r35.ps1")
    payload = BUILDER.read_bytes()
    actual = (len(payload), hashlib.sha256(payload).hexdigest().upper())
    if actual != EXPECTED:
        raise RuntimeError(f"Builder identity drift: {actual}")
    namespace = {
        "__name__": "tohoku_r35_same_bytes_builder",
        "__file__": str(BUILDER),
        "EXECUTION_ATTESTATION": {
            "bootstrap": {
                "path": "srcmap/start_build_tohoku_r35.py",
                "contract": "read_once_then_execute_builder_same_bytes",
            },
            "builder": {
                "path": "srcmap/build_tohoku_r35.py",
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
