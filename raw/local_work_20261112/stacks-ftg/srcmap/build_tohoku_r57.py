#!/usr/bin/env python3
"""Atomic no-overwrite builder for the Tohoku r57 mapping successor."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r56"
TARGET = ROOT / "tohoku_r57"
STAGE = ROOT / ".tohoku-r57-txn"
VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r57.py"
PYTHON = Path(r"user\miniconda3\python.exe")
PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv", "issues.csv",
    "check.json", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
    "mcheck.json", "STATUS.md",
}


def identity(path: Path) -> tuple[int, str]:
    raw = path.read_bytes()
    return len(raw), hashlib.sha256(raw).hexdigest().upper()


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def exclusive_write(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    require(path.read_bytes() == data, f"Write readback mismatch: {path}")


def verify_attestation() -> dict[str, object]:
    require(Path(sys.executable).resolve() == PYTHON.resolve(), "Python executable drift")
    att = globals().get("EXECUTION_ATTESTATION")
    require(isinstance(att, dict) and set(att) == {"driver", "bootstrap", "builder", "validator"}, "Execution attestation missing")
    expected = {
        "driver": ("srcmap/start_build_tohoku_r57.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
        "bootstrap": ("srcmap/start_build_tohoku_r57.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
        "builder": ("srcmap/build_tohoku_r57.py", "read_hash_compile_and_exec_same_payload"),
        "validator": ("srcmap/validate_tohoku_r57.py", "independent_same_bytes_stage_and_receipt_replay"),
    }
    for role, (path, contract) in expected.items():
        item = att[role]
        require(set(item) == {"path", "bytes", "sha256", "contract"} and item["path"] == path and item["contract"] == contract, f"{role} attestation drift")
        require(identity(ROOT / path) == (int(item["bytes"]), str(item["sha256"])), f"{role} disk identity drift")
    require(identity(Path(__file__)) == (int(att["builder"]["bytes"]), str(att["builder"]["sha256"])), "Builder same-bytes drift")
    return att


def load_validator(attestation: dict[str, object]):
    payload = VALIDATOR.read_bytes()
    require(identity(VALIDATOR) == (int(attestation["validator"]["bytes"]), str(attestation["validator"]["sha256"])), "Validator payload drift")
    module = types.ModuleType("tohoku_r57_validator_contract")
    module.__file__ = str(VALIDATOR)
    exec(compile(payload, str(VALIDATOR), "exec"), module.__dict__)
    return module


def run_validator(module, path: Path, receipt: bool = False) -> dict:
    expected = identity(VALIDATOR)
    env = os.environ.copy()
    env["TOHOKU_R57_VALIDATOR_EXPECTED"] = json.dumps({"bytes": expected[0], "sha256": expected[1]}, separators=(",", ":"))
    cmd = [str(PYTHON), "-I", "-B", str(VALIDATOR), "--stage", str(path)]
    if receipt:
        cmd.append("--receipt")
    done = subprocess.run(cmd, cwd=ROOT, env=env, check=True, capture_output=True, text=True, encoding="utf-8")
    value = json.loads(done.stdout)
    require(value.get("status") == "PASS" and value.get("errors") == [], "r57 validator did not PASS")
    return {key: item for key, item in value.items() if key not in {"schema", "attestation"}}


def run_tool(module, relative: str, stage: Path) -> None:
    expected = module.expected_runtime()[relative]
    tool = ROOT / relative
    require(identity(tool) == tuple(expected), f"Runtime identity drift: {relative}")
    subprocess.run([str(PYTHON), "-I", "-B", str(tool), str(stage)], cwd=ROOT, check=True)
    require(identity(tool) == tuple(expected), f"Runtime changed: {relative}")


def promote(module, stage: Path) -> dict:
    require(not TARGET.exists(), f"No-overwrite target appeared: {TARGET}")
    os.rename(stage, TARGET)
    try:
        final = run_validator(module, TARGET, receipt=True)
    except BaseException as exc:
        if TARGET.exists() and not stage.exists():
            os.rename(TARGET, stage)
        raise RuntimeError(f"Post-promotion r57 replay failed; target rolled back to {stage}") from exc
    return final


def main() -> int:
    attestation = verify_attestation()
    module = load_validator(attestation)
    if TARGET.exists():
        final = run_validator(module, TARGET, receipt=True)
        print(json.dumps(final, ensure_ascii=True, indent=2, sort_keys=True))
        return 0
    if STAGE.exists():
        module.verify_external()
        receipt_path = STAGE / "r57-check.json"
        if receipt_path.exists():
            try:
                result = run_validator(module, STAGE, receipt=True)
            except BaseException:
                receipt_path.unlink()
                result = run_validator(module, STAGE)
        else:
            result = run_validator(module, STAGE)
        if not receipt_path.exists():
            exclusive_write(receipt_path, module.json_bytes(module.receipt_payload(STAGE, result)))
        run_validator(module, STAGE, receipt=True)
        require({p.name for p in STAGE.iterdir() if p.is_file()} == PAYLOAD | {"r57-check.json"}, "r57 resumed stage surface drift")
        final = promote(module, STAGE)
        print(json.dumps(final, ensure_ascii=True, indent=2, sort_keys=True))
        return 0
    module.verify_external()
    STAGE.mkdir()
    exclusive_write(STAGE / "cfg.json", module.expected_cfg_bytes())
    for name in ("intake.json", "units.csv", "topics.csv", "ucand.csv"):
        exclusive_write(STAGE / name, (SOURCE / name).read_bytes())
    exclusive_write(STAGE / "dec.csv", module.expected_decision_bytes())
    exclusive_write(STAGE / "issues.csv", (SOURCE / "issues.csv").read_bytes())
    run_tool(module, "srcmap/scan.py", STAGE)
    exclusive_write(STAGE / "map.csv", module.expected_map_bytes())
    run_tool(module, "srcmap/map.py", STAGE)
    exclusive_write(STAGE / "STATUS.md", module.STATUS_BYTES)
    result = run_validator(module, STAGE)
    exclusive_write(STAGE / "r57-check.json", module.json_bytes(module.receipt_payload(STAGE, result)))
    run_validator(module, STAGE, receipt=True)
    require({p.name for p in STAGE.iterdir() if p.is_file()} == PAYLOAD | {"r57-check.json"}, "r57 stage surface drift")
    final = promote(module, STAGE)
    print(json.dumps(final, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
