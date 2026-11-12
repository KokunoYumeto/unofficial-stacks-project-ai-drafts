#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r57 mapping transaction."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r57.py"
VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r57.py"


def identity(data: bytes) -> tuple[int, str]:
    return len(data), hashlib.sha256(data).hexdigest().upper()


def main() -> int:
    if os.environ.pop("TOHOKU_R57_ENVELOPE", "") != "tohoku-r57-one-shot-envelope-v1":
        raise RuntimeError("Run through start_build_tohoku_r57.ps1")
    driver = json.loads(os.environ.pop("TOHOKU_R57_DRIVER_ATTESTATION", ""))
    if set(driver) != {"path", "bytes", "sha256", "contract"} or driver["path"] != "srcmap/start_build_tohoku_r57.ps1" or driver["contract"] != "self_read_hash_then_one_shot_bootstrap_envelope":
        raise RuntimeError("Driver attestation drift")
    own = globals().get("BOOTSTRAP_ATTESTATION")
    if not isinstance(own, dict) or set(own) != {"path", "bytes", "sha256"}:
        raise RuntimeError("Bootstrap attestation missing")
    if identity(Path(__file__).read_bytes()) != (own["bytes"], own["sha256"]):
        raise RuntimeError("Bootstrap disk identity drift")
    builder_id = identity(BUILDER.read_bytes())
    validator_id = identity(VALIDATOR.read_bytes())
    attestation = {
        "driver": driver,
        "bootstrap": {"path": "srcmap/start_build_tohoku_r57.py", "bytes": own["bytes"], "sha256": own["sha256"], "contract": "one_read_hash_compile_exec_builder_and_pin_validator"},
        "builder": {"path": "srcmap/build_tohoku_r57.py", "bytes": builder_id[0], "sha256": builder_id[1], "contract": "read_hash_compile_and_exec_same_payload"},
        "validator": {"path": "srcmap/validate_tohoku_r57.py", "bytes": validator_id[0], "sha256": validator_id[1], "contract": "independent_same_bytes_stage_and_receipt_replay"},
    }
    namespace = {"__name__": "tohoku_r57_same_bytes_builder", "__file__": str(BUILDER), "EXECUTION_ATTESTATION": attestation}
    exec(compile(BUILDER.read_bytes(), str(BUILDER), "exec"), namespace)
    return int(namespace["main"]())


if __name__ == "__main__":
    raise SystemExit(main())
