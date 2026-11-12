#!/usr/bin/env python3
"""Atomic no-overwrite builder for the bounded Tohoku r58 successor."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r57"
TARGET = ROOT / "tohoku_r58"
STAGE = ROOT / ".tohoku-r58-txn"
VALIDATOR_PATH = ROOT / "srcmap" / "validate_tohoku_r58.py"
PYTHON = Path(r"user\miniconda3\python.exe")
PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv", "issues.csv",
    "check.json", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
    "mcheck.json", "STATUS.md",
}
RUNTIME = {
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
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


def load_validator():
    payload = VALIDATOR_PATH.read_bytes()
    spec = importlib.util.spec_from_file_location("tohoku_r58_validator_contract", VALIDATOR_PATH)
    require(spec is not None and spec.loader is not None, "Cannot load r58 validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(identity(VALIDATOR_PATH) == (len(payload), hashlib.sha256(payload).hexdigest().upper()), "Validator identity drift")
    return module


def verify_attestation() -> dict[str, object]:
    require(Path(sys.executable).resolve() == PYTHON.resolve(), "Python executable drift")
    att = globals().get("EXECUTION_ATTESTATION")
    require(isinstance(att, dict) and set(att) == {"driver", "bootstrap", "builder", "validator"}, "Execution attestation missing")
    expected = {
        "driver": ("srcmap/start_build_tohoku_r58.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
        "bootstrap": ("srcmap/start_build_tohoku_r58.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
        "builder": ("srcmap/build_tohoku_r58.py", "read_hash_compile_and_exec_same_payload"),
        "validator": ("srcmap/validate_tohoku_r58.py", "independent_same_bytes_stage_and_receipt_replay"),
    }
    for role, (path, contract) in expected.items():
        item = att[role]
        require(set(item) == {"path", "bytes", "sha256", "contract"} and item["path"] == path and item["contract"] == contract, f"{role} attestation drift")
        require(identity(ROOT / path) == (int(item["bytes"]), str(item["sha256"])), f"{role} disk identity drift")
    require(identity(Path(__file__)) == (int(att["builder"]["bytes"]), str(att["builder"]["sha256"])), "Builder same-bytes drift")
    return att


def run_validator(module, path: Path, receipt: bool = False) -> dict:
    expected = identity(VALIDATOR_PATH)
    env = os.environ.copy()
    env["TOHOKU_R58_VALIDATOR_EXPECTED"] = json.dumps({"bytes": expected[0], "sha256": expected[1]}, separators=(",", ":"))
    cmd = [str(PYTHON), "-I", "-B", str(VALIDATOR_PATH), "--stage", str(path)]
    if receipt:
        cmd.append("--receipt")
    done = subprocess.run(cmd, cwd=ROOT, env=env, check=True, capture_output=True, text=True, encoding="utf-8")
    value = json.loads(done.stdout)
    require(value.get("status") == "PASS" and value.get("errors") == [], "r58 validator did not PASS")
    return value


def run_tool(relative: str, stage: Path) -> None:
    tool = ROOT / relative
    require(identity(tool) == RUNTIME[relative], f"Runtime identity drift: {relative}")
    subprocess.run([str(PYTHON), "-I", "-B", str(tool), str(stage)], cwd=ROOT, check=True)
    require(identity(tool) == RUNTIME[relative], f"Runtime changed: {relative}")


def build_stage(module) -> None:
    module.verify_external()
    STAGE.mkdir()
    exclusive_write(STAGE / "cfg.json", module.expected_cfg_bytes())
    for name in ("intake.json", "units.csv", "topics.csv"):
        exclusive_write(STAGE / name, (SOURCE / name).read_bytes())
    exclusive_write(STAGE / "dec.csv", module.expected_decision_bytes())
    exclusive_write(STAGE / "issues.csv", (SOURCE / "issues.csv").read_bytes())
    run_tool("srcmap/scan.py", STAGE)
    run_tool("srcmap/map.py", STAGE)
    exclusive_write(STAGE / "STATUS.md", module.STATUS_BYTES)


def main() -> int:
    verify_attestation()
    module = load_validator()
    if TARGET.exists():
        run_validator(module, TARGET, receipt=True)
        return 0
    if STAGE.exists():
        run_validator(module, STAGE, receipt=False)
    else:
        build_stage(module)
    result = module.verify_stage(STAGE, receipt_mode=False)
    receipt = module.receipt_payload(STAGE, result)
    receipt_path = STAGE / "r58-check.json"
    if receipt_path.exists():
        require(receipt_path.read_bytes() == module.json_bytes(receipt), "Existing r58 receipt drift")
    else:
        exclusive_write(receipt_path, module.json_bytes(receipt))
    run_validator(module, STAGE, receipt=True)
    require({p.name for p in STAGE.iterdir() if p.is_file()} == PAYLOAD | {"r58-check.json"}, "r58 stage surface drift")
    require(not TARGET.exists(), f"No-overwrite target appeared: {TARGET}")
    os.rename(STAGE, TARGET)
    try:
        run_validator(module, TARGET, receipt=True)
    except BaseException as exc:
        if TARGET.exists() and not STAGE.exists():
            os.rename(TARGET, STAGE)
        raise RuntimeError("Post-promotion r58 replay failed; target rolled back") from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
