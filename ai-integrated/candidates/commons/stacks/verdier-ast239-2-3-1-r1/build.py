from __future__ import annotations

import ctypes
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
IMPLEMENTATION = ROOT / "_build_impl.py"
MUTEX_NAME = r"Global\InterlanguageTeXSlotV1"
MUTEX_TIMEOUT_MS = 120_000
WAIT_OBJECT_0 = 0x00000000
WAIT_ABANDONED = 0x00000080
WAIT_TIMEOUT = 0x00000102


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


class WindowsNamedMutex:
    def __init__(self) -> None:
        self.kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        self.kernel32.CreateMutexW.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p]
        self.kernel32.CreateMutexW.restype = ctypes.c_void_p
        self.kernel32.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        self.kernel32.WaitForSingleObject.restype = ctypes.c_uint32
        self.kernel32.ReleaseMutex.argtypes = [ctypes.c_void_p]
        self.kernel32.ReleaseMutex.restype = ctypes.c_int
        self.kernel32.CloseHandle.argtypes = [ctypes.c_void_p]
        self.kernel32.CloseHandle.restype = ctypes.c_int
        self.handle: int | None = None
        self.abandoned = False
        self.acquired_at_utc: str | None = None
        self.released_at_utc: str | None = None

    def acquire(self) -> None:
        handle = self.kernel32.CreateMutexW(None, 0, MUTEX_NAME)
        if not handle:
            raise RuntimeError(f"CreateMutexW failed: {ctypes.get_last_error()}")
        self.handle = int(handle)
        result = self.kernel32.WaitForSingleObject(handle, MUTEX_TIMEOUT_MS)
        if result == WAIT_TIMEOUT:
            self.kernel32.CloseHandle(handle)
            self.handle = None
            raise RuntimeError(
                f"timed out after {MUTEX_TIMEOUT_MS} ms acquiring {MUTEX_NAME}; no TeX process launched"
            )
        if result not in (WAIT_OBJECT_0, WAIT_ABANDONED):
            error = ctypes.get_last_error()
            self.kernel32.CloseHandle(handle)
            self.handle = None
            raise RuntimeError(f"WaitForSingleObject failed ({result:#x}, Win32 {error})")
        self.abandoned = result == WAIT_ABANDONED
        self.acquired_at_utc = iso_now()

    def release(self) -> None:
        if self.handle is None:
            return
        handle = ctypes.c_void_p(self.handle)
        release_error: str | None = None
        if not self.kernel32.ReleaseMutex(handle):
            release_error = f"ReleaseMutex failed: {ctypes.get_last_error()}"
        if not self.kernel32.CloseHandle(handle) and release_error is None:
            release_error = f"CloseHandle failed: {ctypes.get_last_error()}"
        self.handle = None
        self.released_at_utc = iso_now()
        if release_error is not None:
            raise RuntimeError(release_error)


def write_mutex_receipt(mutex: WindowsNamedMutex, status: str, child_exit_code: int | None) -> None:
    output = ROOT / "builds" / "tex-mutex.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    value = {
        "schema": "unofficial-ai-integrated-stacks-tex-mutex/v1",
        "status": status,
        "passed": status == "PASS",
        "name": MUTEX_NAME,
        "timeout_ms": MUTEX_TIMEOUT_MS,
        "acquired": mutex.acquired_at_utc is not None,
        "acquired_at_utc": mutex.acquired_at_utc,
        "abandoned_mutex_recovered": mutex.abandoned,
        "released": mutex.released_at_utc is not None,
        "released_at_utc": mutex.released_at_utc,
        "captured_child_exit_code": child_exit_code,
    }
    output.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")
    if status == "PASS":
        receipt_path = ROOT / "builds" / "build-receipt.json"
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["machine_wide_tex_mutex"] = value
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    passthrough = sys.argv[1:]
    if passthrough:
        allowed = {"--resanitize-public-logs", "--restore-preimage-only"}
        if len(passthrough) != 1 or passthrough[0] not in allowed:
            raise RuntimeError(f"unexpected arguments: {passthrough}")
        return subprocess.run([sys.executable, "-B", str(IMPLEMENTATION), *passthrough], cwd=ROOT).returncode

    mutex = WindowsNamedMutex()
    child_exit: int | None = None
    run_error: BaseException | None = None
    try:
        mutex.acquire()
        child_exit = subprocess.run([sys.executable, "-B", str(IMPLEMENTATION)], cwd=ROOT).returncode
        if child_exit:
            run_error = RuntimeError(f"bounded build implementation failed with exit code {child_exit}")
    except BaseException as exc:
        run_error = exc
    finally:
        try:
            mutex.release()
        except BaseException as exc:
            if run_error is None:
                run_error = exc
    status = "PASS" if run_error is None else "FAIL"
    write_mutex_receipt(mutex, status, child_exit)
    if run_error is not None:
        raise run_error
    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
    except Exception as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
    raise SystemExit(exit_code)
