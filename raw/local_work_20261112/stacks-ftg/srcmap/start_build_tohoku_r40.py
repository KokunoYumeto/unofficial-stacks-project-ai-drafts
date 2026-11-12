#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r40 mapping builder."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r40.py"
EXPECTED = (
    65722,
    "421647216FF2C3075A1E5BE8C27AE863777547BAABEF00C220D639C482730643",
)


def main() -> int:
    if os.environ.pop("TOHOKU_R40_ENVELOPE", "") != "tohoku-r40-same-bytes-envelope-v1":
        raise RuntimeError("Run through start_build_tohoku_r40.ps1")
    payload = BUILDER.read_bytes()
    actual = (len(payload), hashlib.sha256(payload).hexdigest().upper())
    if actual != EXPECTED:
        raise RuntimeError(f"Builder identity drift: {actual}")
    namespace = {
        "__name__": "tohoku_r40_same_bytes_builder",
        "__file__": str(BUILDER),
        "EXECUTION_ATTESTATION": {
            "bootstrap": {
                "path": "srcmap/start_build_tohoku_r40.py",
                "contract": "read_once_then_execute_builder_same_bytes",
            },
            "builder": {
                "path": "srcmap/build_tohoku_r40.py",
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
