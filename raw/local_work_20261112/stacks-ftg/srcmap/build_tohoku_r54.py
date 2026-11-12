#!/usr/bin/env python3
"""Build the atomic no-overwrite Tohoku r54 mapping successor."""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import subprocess
import sys
import types
from collections.abc import Iterator
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r53"
TARGET = ROOT / "tohoku_r54"
STAGE = ROOT / ".tohoku-r54-txn"
VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r54.py"
BOOTSTRAP = ROOT / "srcmap" / "start_build_tohoku_r54.py"
DRIVER = ROOT / "srcmap" / "start_build_tohoku_r54.ps1"
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)
EXPECTED_VALIDATOR = (
    66617,
    "5C72E15325C031923ABD2BB3F80B1E2348C3C26957B7EC4990049D0EC8D24005",
)

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), hashlib.sha256(data).hexdigest().upper()


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def no_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"Duplicate JSON key: {key}")
        output[key] = value
    return output


def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical JSON: {path}")
    value = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicate_pairs)
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def exclusive_write(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    if path.read_bytes() != data:
        raise RuntimeError(f"Write readback mismatch: {path}")


def is_reparse(path: Path) -> bool:
    return os.name == "nt" and bool(path.stat(follow_symlinks=False).st_file_attributes & 0x400)


def require_plain_file(path: Path) -> None:
    if not path.is_file() or path.is_symlink() or is_reparse(path):
        raise RuntimeError(f"Expected plain file: {path}")


def require_plain_directory(path: Path) -> None:
    if not path.is_dir() or path.is_symlink() or is_reparse(path):
        raise RuntimeError(f"Expected plain directory: {path}")


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require_plain_file(path)
    if identity(path) != expected:
        raise RuntimeError(f"Input identity drift: {path}")


def load_validator_module():
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    payload = VALIDATOR.read_bytes()
    if (len(payload), hashlib.sha256(payload).hexdigest().upper()) != EXPECTED_VALIDATOR:
        raise RuntimeError("Frozen validator payload drift")
    module = types.ModuleType("tohoku_r54_validator_contract")
    module.__file__ = str(VALIDATOR)
    exec(compile(payload, str(VALIDATOR), "exec"), module.__dict__)
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    return module


@contextlib.contextmanager
def deny_write_delete(paths: list[Path]) -> Iterator[None]:
    """Hold Windows read handles that deny writes and deletion."""
    if os.name != "nt":
        raise RuntimeError("This transaction requires Windows file locks")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
        wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    handles: list[object] = []
    invalid = ctypes.c_void_p(-1).value
    try:
        for path in sorted(set(paths), key=lambda item: str(item).casefold()):
            require_plain_file(path)
            handle = create_file(str(path), 0x80000000, 0x00000001, None, 3, 0x00000080, None)
            if handle in (None, invalid):
                raise OSError(ctypes.get_last_error(), f"Cannot lock {path}")
            handles.append(handle)
        yield
    finally:
        for handle in reversed(handles):
            close_handle(handle)


@contextlib.contextmanager
def single_writer_mutex() -> Iterator[None]:
    if os.name != "nt":
        raise RuntimeError("This transaction requires a Windows mutex")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_mutex = kernel32.CreateMutexW
    create_mutex.argtypes = [wintypes.LPVOID, wintypes.BOOL, wintypes.LPCWSTR]
    create_mutex.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    handle = create_mutex(None, False, r"Local\FAC-Tohoku-r54-mapping")
    if not handle:
        raise OSError(ctypes.get_last_error(), "Cannot create Tohoku r54 mutex")
    if ctypes.get_last_error() == 183:
        close_handle(handle)
        raise RuntimeError("Another Tohoku r54 transaction is active")
    try:
        yield
    finally:
        close_handle(handle)


def verify_execution_attestation() -> dict[str, object]:
    if Path(sys.executable).resolve() != EXPECTED_PYTHON.resolve():
        raise RuntimeError("Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    attestation = globals().get("EXECUTION_ATTESTATION")
    if not isinstance(attestation, dict) or set(attestation) != {"driver", "bootstrap", "builder", "validator"}:
        raise RuntimeError("Run through start_build_tohoku_r54.ps1")
    expected_paths = {
        "driver": "srcmap/start_build_tohoku_r54.ps1",
        "bootstrap": "srcmap/start_build_tohoku_r54.py",
        "builder": "srcmap/build_tohoku_r54.py",
        "validator": "srcmap/validate_tohoku_r54.py",
    }
    expected_contracts = {
        "driver": "self_read_hash_then_one_shot_bootstrap_envelope",
        "bootstrap": "one_read_hash_compile_exec_builder_and_pin_validator",
        "builder": "read_hash_compile_and_exec_same_payload",
        "validator": "independent_same_bytes_stage_and_receipt_replay",
    }
    for role, relative in expected_paths.items():
        item = attestation.get(role)
        if not isinstance(item, dict) or set(item) != {"path", "bytes", "sha256", "contract"}:
            raise RuntimeError(f"{role} attestation shape drift")
        if item["path"] != relative or item["contract"] != expected_contracts[role]:
            raise RuntimeError(f"{role} attestation contract drift")
        require_identity(ROOT / relative, (int(item["bytes"]), str(item["sha256"])))
    if (int(attestation["validator"]["bytes"]), str(attestation["validator"]["sha256"])) != EXPECTED_VALIDATOR:
        raise RuntimeError("Frozen validator attestation drift")
    if identity(Path(__file__)) != (int(attestation["builder"]["bytes"]), str(attestation["builder"]["sha256"])):
        raise RuntimeError("Same-bytes builder attestation drift")
    return attestation


def lock_paths(validator, fresh: bool) -> list[Path]:
    paths = [Path(__file__), BOOTSTRAP, DRIVER, VALIDATOR, EXPECTED_PYTHON]
    paths.extend(validator.external_input_paths())
    if not fresh and TARGET.exists():
        paths.extend(path for path in TARGET.iterdir() if path.is_file())
    return list(dict.fromkeys(paths))


def make_config() -> dict:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r54"
    return cfg


def run_tool(validator, name: str, *args: str) -> None:
    relative = f"srcmap/{name}"
    runtime = validator.expected_runtime()
    require_identity(ROOT / relative, runtime[relative])
    subprocess.run([sys.executable, "-I", "-B", str(ROOT / relative), *args], cwd=ROOT, check=True)
    require_identity(ROOT / relative, runtime[relative])


def run_validator(path: Path, receipt: bool = False) -> dict[str, object]:
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    env = os.environ.copy()
    env["TOHOKU_R54_VALIDATOR_EXPECTED"] = json.dumps(
        {"bytes": EXPECTED_VALIDATOR[0], "sha256": EXPECTED_VALIDATOR[1]},
        separators=(",", ":"),
    )
    command = [sys.executable, "-I", "-B", str(VALIDATOR), "--stage", str(path)]
    if receipt:
        command.append("--receipt")
    completed = subprocess.run(
        command, cwd=ROOT, env=env, check=True, capture_output=True,
        text=True, encoding="utf-8",
    )
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    value = json.loads(completed.stdout, object_pairs_hook=no_duplicate_pairs)
    if not isinstance(value, dict) or value.get("status") != "PASS" or value.get("errors") != []:
        raise RuntimeError("Independent r54 validator did not return PASS")
    return value


def core_deltas(validation: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in validation.items() if key not in {"schema", "attestation"}}


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def execution_receipt(attestation: dict[str, object], validator) -> dict[str, object]:
    return {
        "attestation": attestation,
        "dependencies": {
            name: {"name": Path(name).name, "bytes": expected[0], "sha256": expected[1]}
            for name, expected in sorted(validator.expected_runtime().items())
        },
        "contract": "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback",
    }


def receipt_payload(root: Path, attestation: dict[str, object], validator, deltas: dict[str, object]) -> dict[str, object]:
    payload = validator.receipt_payload(root, deltas)
    payload["execution"] = execution_receipt(attestation, validator)
    return payload


def verify_existing(attestation: dict[str, object], validator) -> dict[str, object]:
    require_plain_directory(TARGET)
    validation = run_validator(TARGET, receipt=True)
    deltas = core_deltas(validation)
    receipt = strict_json(TARGET / "r54-check.json")
    expected = receipt_payload(TARGET, attestation, validator, deltas)
    if receipt != expected:
        raise RuntimeError("Existing r54 receipt replay mismatch")
    return receipt


def rollback_promoted_target() -> None:
    if os.path.lexists(STAGE):
        raise RuntimeError("Cannot roll back promoted r54 target: stage path appeared")
    require_plain_directory(TARGET)
    os.rename(TARGET, STAGE)
    require_plain_directory(STAGE)


def main_locked(attestation: dict[str, object], validator) -> int:
    target_entry = os.path.lexists(TARGET)
    stage_entry = os.path.lexists(STAGE)
    if target_entry and stage_entry:
        raise RuntimeError("Target and unresolved r54 transaction coexist")
    if stage_entry:
        raise FileExistsError(f"Unresolved r54 transaction exists: {STAGE}")
    fresh = not target_entry
    with deny_write_delete(lock_paths(validator, fresh)):
        validator.verify_external()
        if target_entry:
            receipt = verify_existing(attestation, validator)
            print(json.dumps(receipt, ensure_ascii=True, indent=2, sort_keys=True))
            return 0

        STAGE.mkdir()
        exclusive_write(STAGE / "cfg.json", json_bytes(make_config()))
        for name in ("intake.json", "units.csv", "topics.csv"):
            exclusive_write(STAGE / name, (SOURCE / name).read_bytes())
        exclusive_write(STAGE / "dec.csv", validator.expected_decision_bytes())
        exclusive_write(STAGE / "issues.csv", validator.expected_issue_bytes())
        run_tool(validator, "scan.py", str(STAGE))
        run_tool(validator, "map.py", str(STAGE))
        exclusive_write(STAGE / "STATUS.md", validator.STATUS_BYTES)

        staged_validation = run_validator(STAGE)
        deltas = core_deltas(staged_validation)
        receipt = receipt_payload(STAGE, attestation, validator, deltas)
        exclusive_write(STAGE / "r54-check.json", json_bytes(receipt))
        run_validator(STAGE, receipt=True)
        if {path.name for path in STAGE.iterdir() if path.is_file()} != PAYLOAD | {"r54-check.json"} or any(path.is_dir() for path in STAGE.iterdir()):
            raise RuntimeError("Staged r54 dossier surface mismatch")

        validator.verify_external()
        if os.path.lexists(TARGET):
            raise FileExistsError(f"No-overwrite target appeared before promotion: {TARGET}")
        os.rename(STAGE, TARGET)
        try:
            with deny_write_delete([path for path in TARGET.iterdir() if path.is_file()]):
                final = verify_existing(attestation, validator)
        except BaseException as replay_error:
            try:
                rollback_promoted_target()
            except BaseException as rollback_error:
                raise RuntimeError(f"Post-promotion replay failed and rollback failed: {rollback_error}") from replay_error
            raise RuntimeError(f"Post-promotion replay failed; exact promoted directory rolled back to {STAGE}") from replay_error
        print(json.dumps(final, ensure_ascii=True, indent=2, sort_keys=True))
        return 0


def main() -> int:
    attestation = verify_execution_attestation()
    validator = load_validator_module()
    with single_writer_mutex():
        return main_locked(attestation, validator)


if __name__ == "__main__":
    raise SystemExit(main())
