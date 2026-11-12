#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r39 mapping builder."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r39.py"
EXPECTED = (
    60833,
    "45061719495AB03DBE25CA3E1367D9B89EB11B18BBFA39E78481C8247A19486D",
)


def main() -> int:
    if os.environ.pop("TOHOKU_R39_ENVELOPE", "") != "tohoku-r39-same-bytes-envelope-v1":
        raise RuntimeError("Run through start_build_tohoku_r39.ps1")
    payload = BUILDER.read_bytes()
    actual = (len(payload), hashlib.sha256(payload).hexdigest().upper())
    if actual != EXPECTED:
        raise RuntimeError(f"Builder identity drift: {actual}")
    namespace = {
        "__name__": "tohoku_r39_same_bytes_builder",
        "__file__": str(BUILDER),
        "EXECUTION_ATTESTATION": {
            "bootstrap": {
                "path": "srcmap/start_build_tohoku_r39.py",
                "contract": "read_once_then_execute_builder_same_bytes",
            },
            "builder": {
                "path": "srcmap/build_tohoku_r39.py",
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
