#!/usr/bin/env python3
"""One-read bootstrap for the no-overwrite Tohoku r51 mapping transaction."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BUILDER = ROOT / "srcmap" / "build_tohoku_r51.py"
VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r51.py"
EXPECTED_BUILDER = (
    20628,
    "0481C1709AE1B5E6B0C30E672AF2E38277687A49437CE1E93515016D20F3D0F2",
)
EXPECTED_VALIDATOR = (
    71750,
    "3ABAA38045E610ADF74087FEC22401F42C50ED957FCB85DAC4D8C08CA3636C63",
)


def identity(data: bytes) -> tuple[int, str]:
    return len(data), hashlib.sha256(data).hexdigest().upper()


def main() -> int:
    if os.environ.pop("TOHOKU_R51_ENVELOPE", "") != "tohoku-r51-one-shot-envelope-v1":
        raise RuntimeError("Run through start_build_tohoku_r51.ps1")
    driver_raw = os.environ.pop("TOHOKU_R51_DRIVER_ATTESTATION", "")
    driver = json.loads(driver_raw)
    if set(driver) != {"path", "bytes", "sha256", "contract"} or driver != {
        "path": "srcmap/start_build_tohoku_r51.ps1",
        "bytes": driver.get("bytes"),
        "sha256": driver.get("sha256"),
        "contract": "self_read_hash_then_one_shot_bootstrap_envelope",
    }:
        raise RuntimeError("Driver self-attestation shape drift")
    if not isinstance(driver["bytes"], int) or driver["bytes"] <= 0:
        raise RuntimeError("Driver byte attestation is invalid")
    if not isinstance(driver["sha256"], str) or len(driver["sha256"]) != 64:
        raise RuntimeError("Driver hash attestation is invalid")

    bootstrap_attestation = globals().get("BOOTSTRAP_ATTESTATION")
    if not isinstance(bootstrap_attestation, dict) or set(bootstrap_attestation) != {
        "path", "bytes", "sha256"
    }:
        raise RuntimeError("PowerShell bootstrap attestation missing")
    bootstrap_path = ROOT / str(bootstrap_attestation["path"])
    bootstrap_disk = bootstrap_path.read_bytes()
    if identity(bootstrap_disk) != (
        bootstrap_attestation["bytes"], bootstrap_attestation["sha256"]
    ):
        raise RuntimeError("Bootstrap disk bytes changed after envelope read")

    builder_payload = BUILDER.read_bytes()
    builder_identity = identity(builder_payload)
    if builder_identity != EXPECTED_BUILDER:
        raise RuntimeError(f"Builder identity drift: {builder_identity}")
    validator_payload = VALIDATOR.read_bytes()
    validator_identity = identity(validator_payload)
    if validator_identity != EXPECTED_VALIDATOR:
        raise RuntimeError(f"Validator identity drift: {validator_identity}")

    attestation = {
        "driver": driver,
        "bootstrap": {
            "path": "srcmap/start_build_tohoku_r51.py",
            "bytes": bootstrap_attestation["bytes"],
            "sha256": bootstrap_attestation["sha256"],
            "contract": "one_read_hash_compile_exec_builder_and_pin_validator",
        },
        "builder": {
            "path": "srcmap/build_tohoku_r51.py",
            "bytes": builder_identity[0],
            "sha256": builder_identity[1],
            "contract": "read_hash_compile_and_exec_same_payload",
        },
        "validator": {
            "path": "srcmap/validate_tohoku_r51.py",
            "bytes": validator_identity[0],
            "sha256": validator_identity[1],
            "contract": "independent_same_bytes_stage_and_receipt_replay",
        },
    }
    namespace = {
        "__name__": "tohoku_r51_same_bytes_builder",
        "__file__": str(BUILDER),
        "EXECUTION_ATTESTATION": attestation,
    }
    code = compile(builder_payload, str(BUILDER), "exec")
    exec(code, namespace)
    return int(namespace["main"]())


if __name__ == "__main__":
    raise SystemExit(main())
