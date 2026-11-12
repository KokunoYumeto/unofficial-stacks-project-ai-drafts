#!/usr/bin/env python3
"""Atomic no-overwrite builder for the bounded Tohoku r60 successor."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r59"
TARGET = ROOT / "tohoku_r60"
STAGE = ROOT / ".tohoku-r60-txn"
VALIDATOR_PATH = ROOT / "srcmap" / "validate_tohoku_r60.py"
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


def load_validator(expected: tuple[int, str]):
    payload = VALIDATOR_PATH.read_bytes()
    require((len(payload), hashlib.sha256(payload).hexdigest().upper()) == expected, "Validator bootstrap pin drift")
    module = types.ModuleType("tohoku_r60_validator_contract")
    module.__file__ = str(VALIDATOR_PATH)
    exec(compile(payload, str(VALIDATOR_PATH), "exec"), module.__dict__)
    require(identity(VALIDATOR_PATH) == expected, "Validator identity drift")
    return module


def verify_attestation() -> dict[str, object]:
    require(Path(sys.executable).resolve() == PYTHON.resolve(), "Python executable drift")
    att = globals().get("EXECUTION_ATTESTATION")
    require(isinstance(att, dict) and set(att) == {"driver", "bootstrap", "builder", "validator"}, "Execution attestation missing")
    expected = {
        "driver": ("srcmap/start_build_tohoku_r60.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
        "bootstrap": ("srcmap/start_build_tohoku_r60.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
        "builder": ("srcmap/build_tohoku_r60.py", "read_hash_compile_and_exec_same_payload"),
        "validator": ("srcmap/validate_tohoku_r60.py", "independent_same_bytes_stage_and_receipt_replay"),
    }
    for role, (path, contract) in expected.items():
        item = att[role]
        require(set(item) == {"path", "bytes", "sha256", "contract"} and item["path"] == path and item["contract"] == contract, f"{role} attestation drift")
        require(identity(ROOT / path) == (int(item["bytes"]), str(item["sha256"])), f"{role} disk identity drift")
    require(identity(Path(__file__)) == (int(att["builder"]["bytes"]), str(att["builder"]["sha256"])), "Builder same-bytes drift")
    return att


def run_validator(path: Path, expected: tuple[int, str], receipt: bool = False) -> dict:
    payload = VALIDATOR_PATH.read_bytes()
    require((len(payload), hashlib.sha256(payload).hexdigest().upper()) == expected, "Validator subprocess pin drift")
    env = os.environ.copy()
    env["TOHOKU_R60_VALIDATOR_EXPECTED"] = json.dumps({"bytes": expected[0], "sha256": expected[1]}, separators=(",", ":"))
    runner = (
        "import hashlib,sys\n"
        "path=sys.argv[1]; expected=int(sys.argv[2]); sha=sys.argv[3]; args=sys.argv[4:]\n"
        "payload=sys.stdin.buffer.read()\n"
        "if len(payload)!=expected or hashlib.sha256(payload).hexdigest().upper()!=sha: raise RuntimeError('validator payload drift')\n"
        "sys.argv=[path,*args]\n"
        "ns={'__name__':'__main__','__file__':path}\n"
        "exec(compile(payload,path,'exec'),ns)\n"
    )
    cmd = [str(PYTHON), "-I", "-B", "-c", runner, str(VALIDATOR_PATH), str(expected[0]), expected[1], "--stage", str(path)]
    if receipt:
        cmd.append("--receipt")
    done = subprocess.run(cmd, cwd=ROOT, env=env, check=True, capture_output=True, input=payload)
    require(identity(VALIDATOR_PATH) == expected, "Validator changed during subprocess")
    value = json.loads(done.stdout.decode("utf-8"))
    require(value.get("status") == "PASS" and value.get("errors") == [], "r60 validator did not PASS")
    return value


def run_tool(relative: str, stage: Path) -> None:
    tool = ROOT / relative
    payload = tool.read_bytes()
    require((len(payload), hashlib.sha256(payload).hexdigest().upper()) == RUNTIME[relative], f"Runtime identity drift: {relative}")
    runner = (
        "import hashlib,sys\n"
        "path=sys.argv[1]; expected=int(sys.argv[2]); sha=sys.argv[3]; stage=sys.argv[4]\n"
        "payload=sys.stdin.buffer.read()\n"
        "if len(payload)!=expected or hashlib.sha256(payload).hexdigest().upper()!=sha: raise RuntimeError('runtime payload drift')\n"
        "sys.argv=[path,stage]\n"
        "ns={'__name__':'__main__','__file__':path}\n"
        "exec(compile(payload,path,'exec'),ns)\n"
    )
    subprocess.run(
        [str(PYTHON), "-I", "-B", "-c", runner, str(tool), str(len(payload)), RUNTIME[relative][1], str(stage)],
        cwd=ROOT, check=True, input=payload,
    )
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
    attestation = verify_attestation()
    validator_expected = (int(attestation["validator"]["bytes"]), str(attestation["validator"]["sha256"]))
    module = load_validator(validator_expected)
    if TARGET.exists():
        run_validator(TARGET, validator_expected, receipt=True)
        return 0
    receipt_path = STAGE / "r60-check.json"
    if STAGE.exists():
        run_validator(STAGE, validator_expected, receipt=receipt_path.exists())
    else:
        build_stage(module)
    result = module.verify_stage(STAGE, receipt_mode=receipt_path.exists())
    receipt = module.receipt_payload(STAGE, result)
    if receipt_path.exists():
        require(receipt_path.read_bytes() == module.json_bytes(receipt), "Existing r60 receipt drift")
    else:
        exclusive_write(receipt_path, module.json_bytes(receipt))
    run_validator(STAGE, validator_expected, receipt=True)
    require({p.name for p in STAGE.iterdir() if p.is_file()} == PAYLOAD | {"r60-check.json"}, "r60 stage surface drift")
    require(not any(p.is_dir() for p in STAGE.iterdir()), "Unexpected r60 stage subdirectory")
    require(not TARGET.exists(), f"No-overwrite target appeared: {TARGET}")
    os.rename(STAGE, TARGET)
    try:
        run_validator(TARGET, validator_expected, receipt=True)
    except BaseException as exc:
        if TARGET.exists() and not STAGE.exists():
            os.rename(TARGET, STAGE)
        raise RuntimeError("Post-promotion r60 replay failed; target rolled back") from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
