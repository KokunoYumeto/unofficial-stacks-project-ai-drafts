"""Capture one Windows TeX launch and its descendants without an assignment race.

The caller MUST already own Global\\InterlanguageTeXSlotV1 for this entire call.
This helper does not acquire/release that mutex. It uses Windows CPython's
CreateProcess wrapper with CREATE_SUSPENDED, assigns a non-breakaway kill-on-close
job, then resumes the primary thread. Completion means the job, not merely its
root process, has been observed empty. Output is UTF-8, merged stderr/stdout.

The boolean mutex argument is an explicit caller contract, not an independent
Windows mutex-ownership attestation. This is a process-lifetime guard, not a
sandbox: it does not capture work requested through foreign services/brokers.
The hosting process must not concurrently perform unrestricted handle-inheriting
launches while this helper briefly marks its explicit stdio handles inheritable.
"""

from __future__ import annotations

import ctypes
import hashlib
import json
import os
import shutil
import signal
import subprocess
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence


RECEIPT_SCHEMA = "unofficial-stacks-project-ai-drafts-tex-process-tree/v1"
CREATE_SUSPENDED = 0x00000004
CREATE_NO_WINDOW = 0x08000000
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
STILL_ACTIVE = 259
WAIT_OBJECT_0 = 0
WAIT_TIMEOUT = 258
TERMINATION_EXIT_CODE = 124


class TexProcessGuardError(RuntimeError):
    """A launch, capture, receipt, or drain safety check failed."""


class _DeferredInterrupts:
    """Defer actual Ctrl-C/Ctrl-Break until the captured tree has drained.

    Installed before CreateProcess and restored only after handle cleanup. The
    ordinary launch loop notices pending interruption and enters tree cleanup;
    the cleanup loop cannot itself be unwound by a second keyboard interrupt.
    """

    def __init__(self) -> None:
        self.pending = False
        self.signals: list[int] = []
        self.previous: dict[int, object] = {}

    def __enter__(self) -> _DeferredInterrupts:
        if threading.current_thread() is not threading.main_thread():
            raise TexProcessGuardError("captured launch must run on the main thread for interrupt deferral")
        for sig in (signal.SIGINT, signal.SIGBREAK):
            previous = signal.getsignal(sig)
            if previous != signal.SIG_IGN:
                self.previous[sig] = previous
                signal.signal(sig, self._record)
        return self

    def _record(self, signum: int, frame: object) -> None:
        self.pending = True
        if signum not in self.signals:
            self.signals.append(signum)

    def __exit__(self, *args: object) -> None:
        for sig, previous in self.previous.items():
            signal.signal(sig, previous)


def _utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def validate_capture_receipt(receipt: dict[str, object]) -> None:
    """Validate successful build-launch lifecycle evidence, without native APIs."""
    expected = {"schema": RECEIPT_SCHEMA, "status": "PASS", "returncode": 0,
                "mutex": "Global\\InterlanguageTeXSlotV1",
                "caller_asserted_mutex_owned": True, "created_suspended": True,
                "assigned_before_resume": True, "resumed": True,
                "kill_on_close": True, "breakaway_allowed": False,
                "observed_empty_tree": True, "job_termination_requested": False,
                "empty_tree_evidence": "job_accounting_active_processes_zero",
                "handle_inheritance": "explicit stdin/stdout handles only",
                "failure": None, "cleanup_errors": []}
    if not isinstance(receipt, dict):
        raise TexProcessGuardError("capture receipt must be an object")
    for key, value in expected.items():
        if key not in receipt or type(receipt[key]) is not type(value) or receipt[key] != value:
            raise TexProcessGuardError(f"invalid capture receipt field {key}")
    identity = receipt.get("root_identity")
    if not isinstance(identity, dict) or any(type(identity.get(key)) is not int or identity[key] <= 0
                                            for key in ("pid", "creation_filetime_100ns")):
        raise TexProcessGuardError("missing exact captured root process identity")
    for phase, active in (("initial_accounting", 1), ("final_accounting", 0)):
        accounting = receipt.get(phase)
        if not isinstance(accounting, dict) or accounting.get("active_processes") != active:
            raise TexProcessGuardError(f"invalid {phase} empty-tree accounting")
        if type(accounting.get("total_processes")) is not int or accounting["total_processes"] < 1:
            raise TexProcessGuardError(f"invalid {phase} process count")


class _Job:
    """Private native API adapter; no global process enumeration or PID kills."""

    def __init__(self) -> None:
        from ctypes import wintypes as w

        class BasicLimits(ctypes.Structure):
            _fields_ = [("PerProcessUserTimeLimit", ctypes.c_longlong),
                        ("PerJobUserTimeLimit", ctypes.c_longlong),
                        ("LimitFlags", w.DWORD),
                        ("MinimumWorkingSetSize", ctypes.c_size_t),
                        ("MaximumWorkingSetSize", ctypes.c_size_t),
                        ("ActiveProcessLimit", w.DWORD),
                        ("Affinity", ctypes.c_size_t),
                        ("PriorityClass", w.DWORD),
                        ("SchedulingClass", w.DWORD)]

        class IoCounters(ctypes.Structure):
            _fields_ = [(name, ctypes.c_ulonglong) for name in (
                "ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
                "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]

        class ExtendedLimits(ctypes.Structure):
            _fields_ = [("BasicLimitInformation", BasicLimits),
                        ("IoInfo", IoCounters),
                        ("ProcessMemoryLimit", ctypes.c_size_t),
                        ("JobMemoryLimit", ctypes.c_size_t),
                        ("PeakProcessMemoryUsed", ctypes.c_size_t),
                        ("PeakJobMemoryUsed", ctypes.c_size_t)]

        class Accounting(ctypes.Structure):
            _fields_ = [(name, ctypes.c_longlong) for name in (
                "TotalUserTime", "TotalKernelTime", "ThisPeriodTotalUserTime",
                "ThisPeriodTotalKernelTime")] + [(name, w.DWORD) for name in (
                    "TotalPageFaultCount", "TotalProcesses", "ActiveProcesses",
                    "TotalTerminatedProcesses")]

        self.w, self.Accounting = w, Accounting
        self.k = ctypes.WinDLL("kernel32", use_last_error=True)
        specs = {
            "CreateJobObjectW": ([w.LPVOID, w.LPCWSTR], w.HANDLE),
            "SetInformationJobObject": ([w.HANDLE, ctypes.c_int, w.LPVOID, w.DWORD], w.BOOL),
            "QueryInformationJobObject": ([w.HANDLE, ctypes.c_int, w.LPVOID, w.DWORD, w.LPVOID], w.BOOL),
            "AssignProcessToJobObject": ([w.HANDLE, w.HANDLE], w.BOOL),
            "IsProcessInJob": ([w.HANDLE, w.HANDLE, ctypes.POINTER(w.BOOL)], w.BOOL),
            "ResumeThread": ([w.HANDLE], w.DWORD),
            "TerminateJobObject": ([w.HANDLE, w.UINT], w.BOOL),
            "TerminateProcess": ([w.HANDLE, w.UINT], w.BOOL),
            "CloseHandle": ([w.HANDLE], w.BOOL),
            "GetProcessTimes": ([w.HANDLE] + [ctypes.POINTER(w.FILETIME)] * 4, w.BOOL),
            "CreateIoCompletionPort": ([w.HANDLE, w.HANDLE, ctypes.c_size_t, w.DWORD], w.HANDLE),
            "GetQueuedCompletionStatus": ([w.HANDLE, ctypes.POINTER(w.DWORD),
                                           ctypes.POINTER(ctypes.c_size_t),
                                           ctypes.POINTER(w.LPVOID), w.DWORD], w.BOOL),
        }
        for name, (args, result) in specs.items():
            getattr(self.k, name).argtypes = args
            getattr(self.k, name).restype = result
        self.port = None
        self.handle = self.k.CreateJobObjectW(None, None)
        if not self.handle:
            self._error("CreateJobObjectW")
        try:
            limits = ExtendedLimits()
            limits.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
            if not self.k.SetInformationJobObject(self.handle, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
                self._error("SetInformationJobObject")
            actual = ExtendedLimits()
            if not self.k.QueryInformationJobObject(self.handle, 9, ctypes.byref(actual), ctypes.sizeof(actual), None):
                self._error("QueryInformationJobObject(limits)")
            if actual.BasicLimitInformation.LimitFlags != JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE:
                raise TexProcessGuardError("job limits readback mismatch")
            self.port = self.k.CreateIoCompletionPort(ctypes.c_void_p(-1), None, 0, 1)
            if not self.port:
                self._error("CreateIoCompletionPort")

            class CompletionAssociation(ctypes.Structure):
                _fields_ = [("CompletionKey", ctypes.c_void_p), ("CompletionPort", w.HANDLE)]

            association = CompletionAssociation(1, self.port)
            if not self.k.SetInformationJobObject(self.handle, 7, ctypes.byref(association), ctypes.sizeof(association)):
                self._error("SetInformationJobObject(completion port)")
        except BaseException:
            self.close()
            raise

    @staticmethod
    def _error(operation: str) -> None:
        raise TexProcessGuardError(f"{operation} failed: Win32 error {ctypes.get_last_error()}")

    def assign(self, process: int) -> None:
        if not self.k.AssignProcessToJobObject(self.handle, process):
            self._error("AssignProcessToJobObject(suspended process)")
        member = self.w.BOOL()
        if not self.k.IsProcessInJob(process, self.handle, ctypes.byref(member)):
            self._error("IsProcessInJob")
        if not member.value:
            raise TexProcessGuardError("suspended process is not in captured job")

    def resume(self, thread: int) -> None:
        count = self.k.ResumeThread(thread)
        if count != 1:
            raise TexProcessGuardError(f"ResumeThread expected suspension count 1, got {count}")

    def accounting(self) -> dict[str, int]:
        value = self.Accounting()
        if not self.k.QueryInformationJobObject(self.handle, 1, ctypes.byref(value), ctypes.sizeof(value), None):
            self._error("QueryInformationJobObject(accounting)")
        return {"active_processes": int(value.ActiveProcesses),
                "total_processes": int(value.TotalProcesses),
                "total_terminated_processes": int(value.TotalTerminatedProcesses)}

    def identity(self, process: int, pid: int) -> dict[str, object]:
        times = [self.w.FILETIME() for _ in range(4)]
        if not self.k.GetProcessTimes(process, *(ctypes.byref(t) for t in times)):
            self._error("GetProcessTimes(captured root)")
        created = (times[0].dwHighDateTime << 32) | times[0].dwLowDateTime
        return {"pid": pid, "creation_filetime_100ns": created,
                "identity_kind": "PID plus kernel process creation FILETIME"}

    def empty_notification(self) -> bool:
        """Independent empty-tree evidence if accounting observation fails.

        Notifications are not assumed infallibly delivered; only an actually
        received ACTIVE_PROCESS_ZERO message is accepted as an empty barrier.
        The port belongs to this one job and was attached before root assignment.
        """
        for _ in range(64):
            message, key, process_id = self.w.DWORD(), ctypes.c_size_t(), self.w.LPVOID()
            ok = self.k.GetQueuedCompletionStatus(self.port, ctypes.byref(message),
                                                 ctypes.byref(key), ctypes.byref(process_id), 0)
            if not ok:
                if ctypes.get_last_error() == WAIT_TIMEOUT:
                    return False
                self._error("GetQueuedCompletionStatus(captured job)")
            if key.value != 1:
                raise TexProcessGuardError("unexpected completion key in private job port")
            if message.value == 4:  # JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO
                return True
        return False

    def terminate(self) -> None:
        if not self.k.TerminateJobObject(self.handle, TERMINATION_EXIT_CODE):
            self._error("TerminateJobObject(captured job only)")

    def terminate_suspended(self, process: int) -> None:
        if not self.k.TerminateProcess(process, TERMINATION_EXIT_CODE):
            self._error("TerminateProcess(unresumed captured root only)")

    def close(self) -> None:
        if self.handle:
            if not self.k.CloseHandle(self.handle):
                self._error("CloseHandle(captured kill-on-close job)")
            self.handle = None
        if self.port:
            if not self.k.CloseHandle(self.port):
                self._error("CloseHandle(private completion port)")
            self.port = None


def run_captured(
    command: Sequence[str],
    *,
    cwd: Path | str,
    env: Mapping[str, str] | None = None,
    caller_holds_tex_mutex: bool,
    receipt_path: Path | str,
    timeout: float = 3600.0,
) -> subprocess.CompletedProcess[str]:
    """Run a bounded command; return only after the captured job is empty.

    A unique receipt is mandatory, including for nonzero command exit codes.
    Timeout raises subprocess.TimeoutExpired *after* terminating/draining the
    captured job. Other failures raise after the same cleanup. Unsupported
    platforms, missing ownership, and invalid inputs fail before any launch.
    No environment values are copied into the receipt.
    """
    if caller_holds_tex_mutex is not True:
        raise TexProcessGuardError("caller must own Global\\InterlanguageTeXSlotV1")
    if os.name != "nt":
        raise TexProcessGuardError("Windows Job Object capture is required")
    if threading.current_thread() is not threading.main_thread():
        raise TexProcessGuardError("captured launch must run on the main thread for interrupt deferral")
    if isinstance(command, (str, bytes)) or not command or any(not isinstance(x, str) or "\0" in x for x in command):
        raise ValueError("command must be a nonempty string argv without NUL")
    if not isinstance(timeout, (int, float)) or not 0 < timeout <= 86400:
        raise ValueError("timeout must be finite and in (0, 86400] seconds")
    command = list(command)
    working_directory = Path(cwd).resolve(strict=True)
    if not working_directory.is_dir():
        raise ValueError("cwd must be a directory")
    environment = dict(os.environ if env is None else env)
    if any(not isinstance(k, str) or not isinstance(v, str) or "\0" in k + v for k, v in environment.items()):
        raise ValueError("environment must contain NUL-free strings")
    executable = Path(command[0])
    if executable.is_absolute() or executable.parent != Path("."):
        executable = (working_directory / executable).resolve(strict=True)
    else:
        located = shutil.which(command[0], path=environment.get("PATH", environment.get("Path", "")))
        if not located:
            raise FileNotFoundError(command[0])
        executable = Path(located).resolve(strict=True)
    if executable.suffix.lower() != ".exe" or not executable.is_file():
        raise ValueError("launch requires a directly executable .exe, not a shell script")

    import _winapi
    import msvcrt

    receipt_path = Path(receipt_path).resolve()
    receipt = {"schema": RECEIPT_SCHEMA, "status": "PREPARED", "started_utc": _utc(),
               "command": command, "resolved_executable": str(executable),
               "cwd": str(working_directory), "timeout_seconds": timeout,
               "mutex": "Global\\InterlanguageTeXSlotV1", "caller_asserted_mutex_owned": True,
               "created_suspended": False, "assigned_before_resume": False,
               "resumed": False, "kill_on_close": True, "breakaway_allowed": False,
               "handle_inheritance": "explicit stdin/stdout handles only",
               "root_identity": None, "observed_empty_tree": False,
               "empty_tree_evidence": None,
               "root_exited_before_tree_empty": False, "peak_observed_active_processes": 0,
               "job_termination_requested": False, "cleanup_errors": []}
    # 'x' rejects receipt reuse before any process is created.
    with receipt_path.open("x", encoding="utf-8", newline="\n") as receipt_file:
        def persist() -> None:
            receipt_file.seek(0)
            receipt_file.write(json.dumps(receipt, indent=2) + "\n")
            receipt_file.truncate()
            receipt_file.flush()
            os.fsync(receipt_file.fileno())

        persist()
        job = None
        process = thread = None
        assigned = False
        failure = None
        output = ""
        returncode = None
        start = time.monotonic()
        with tempfile.TemporaryFile() as capture, open(os.devnull, "rb") as stdin, _DeferredInterrupts() as interrupts:
            try:
                job = _Job()
                out_handle = msvcrt.get_osfhandle(capture.fileno())
                in_handle = msvcrt.get_osfhandle(stdin.fileno())
                os.set_handle_inheritable(out_handle, True)
                os.set_handle_inheritable(in_handle, True)
                startup = subprocess.STARTUPINFO()
                startup.dwFlags = subprocess.STARTF_USESTDHANDLES
                startup.hStdInput, startup.hStdOutput, startup.hStdError = in_handle, out_handle, out_handle
                startup.lpAttributeList = {"handle_list": [in_handle, out_handle]}
                try:
                    process, thread, pid, thread_id = _winapi.CreateProcess(
                        str(executable), subprocess.list2cmdline(command), None, None,
                        True, CREATE_SUSPENDED | CREATE_NO_WINDOW, environment,
                        str(working_directory), startup)
                finally:
                    os.set_handle_inheritable(out_handle, False)
                    os.set_handle_inheritable(in_handle, False)
                receipt["created_suspended"] = True
                receipt["root_identity"] = job.identity(process, pid)
                receipt["root_thread_id"] = thread_id
                job.assign(process)
                assigned = True
                receipt["assigned_before_resume"] = True
                receipt["initial_accounting"] = job.accounting()
                if receipt["initial_accounting"]["active_processes"] != 1:
                    raise TexProcessGuardError("new suspended job must contain exactly one process")
                # Persist kernel identity/capture before allowing any child code.
                persist()
                job.resume(thread)
                receipt["resumed"] = True
                while True:
                    if interrupts.pending:
                        raise KeyboardInterrupt("keyboard interruption deferred until captured tree is empty")
                    accounting = job.accounting()
                    active = accounting["active_processes"]
                    receipt["peak_observed_active_processes"] = max(receipt["peak_observed_active_processes"], active)
                    if not active:
                        receipt["observed_empty_tree"] = True
                        receipt["empty_tree_evidence"] = "job_accounting_active_processes_zero"
                        receipt["final_accounting"] = accounting
                        break
                    root_wait = _winapi.WaitForSingleObject(process, 0)
                    if root_wait not in (WAIT_OBJECT_0, WAIT_TIMEOUT):
                        raise TexProcessGuardError(f"unexpected root wait result {root_wait}")
                    if root_wait == WAIT_OBJECT_0:
                        receipt["root_exited_before_tree_empty"] = True
                    if time.monotonic() - start >= timeout:
                        raise subprocess.TimeoutExpired(command, timeout)
                    time.sleep(0.01)
                if _winapi.WaitForSingleObject(process, 0) != WAIT_OBJECT_0:
                    raise TexProcessGuardError("empty job but root process not signaled")
                returncode = _winapi.GetExitCodeProcess(process)
            except BaseException as error:
                failure = error
            finally:
                # Never release caller ownership just because the root exited.
                # On failure, only this job (or its never-resumed root) is killed.
                if process is not None and not receipt["observed_empty_tree"]:
                    def remember_cleanup_error(error: BaseException) -> None:
                        nonlocal failure
                        text = f"{type(error).__name__}: {error}"
                        if text not in receipt["cleanup_errors"] and len(receipt["cleanup_errors"]) < 16:
                            receipt["cleanup_errors"].append(text)
                        failure = failure or error

                    terminated = False
                    termination_attempts = 0
                    # Cleanup cannot unwind to the caller's mutex finally block
                    # before a kernel empty-tree barrier. Cancellation is deferred
                    # here. In a persistent native-API failure this remains
                    # fail-closed, retaining job handles and caller ownership.
                    # Only the same captured job is observed; no new work/retry
                    # worker is launched. Termination attempts are bounded to 3.
                    while not receipt["observed_empty_tree"]:
                        if not terminated and termination_attempts < 3:
                            termination_attempts += 1
                            try:
                                if assigned:
                                    receipt["job_termination_requested"] = True
                                    job.terminate()
                                else:
                                    job.terminate_suspended(process)
                                terminated = True
                            except BaseException as error:
                                remember_cleanup_error(error)
                        if assigned:
                            try:
                                accounting = job.accounting()
                                if not accounting["active_processes"]:
                                    receipt["observed_empty_tree"] = True
                                    receipt["empty_tree_evidence"] = "job_accounting_active_processes_zero"
                                    receipt["final_accounting"] = accounting
                            except BaseException as error:
                                remember_cleanup_error(error)
                            if not receipt["observed_empty_tree"]:
                                try:
                                    if job.empty_notification():
                                        receipt["observed_empty_tree"] = True
                                        receipt["empty_tree_evidence"] = "job_completion_port_active_process_zero"
                                except BaseException as error:
                                    remember_cleanup_error(error)
                        else:
                            try:
                                if _winapi.WaitForSingleObject(process, 0) == WAIT_OBJECT_0:
                                    receipt["observed_empty_tree"] = True
                                    receipt["empty_tree_evidence"] = "unresumed_root_terminated_and_waited"
                                    receipt["unresumed_root_terminated_and_waited"] = True
                            except BaseException as error:
                                remember_cleanup_error(error)
                        if not receipt["observed_empty_tree"]:
                            try:
                                time.sleep(0.05)
                            except BaseException as error:
                                remember_cleanup_error(error)
                    receipt["termination_attempts"] = termination_attempts
                for handle in (thread, process):
                    if handle is not None:
                        try:
                            _winapi.CloseHandle(handle)
                        except OSError as error:
                            receipt["cleanup_errors"].append(str(error))
                            failure = failure or error
                if job is not None:
                    try:
                        job.close()
                    except BaseException as error:
                        receipt["cleanup_errors"].append(str(error))
                        failure = failure or error
                capture.seek(0)
                raw = capture.read()
                output = raw.decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
                if interrupts.pending and failure is None:
                    failure = KeyboardInterrupt("keyboard interruption deferred until captured tree is empty")
                receipt.update({"finished_utc": _utc(), "elapsed_seconds": round(time.monotonic() - start, 6),
                                "returncode": returncode, "stdout_bytes": len(raw),
                                "stdout_sha256": hashlib.sha256(raw).hexdigest().upper(),
                                "status": "PASS" if failure is None else "FAIL",
                                "deferred_keyboard_signals": interrupts.signals,
                                "failure": None if failure is None else f"{type(failure).__name__}: {failure}"})
                persist()
        if failure is not None:
            if isinstance(failure, subprocess.TimeoutExpired):
                failure.output = output
            raise failure
        if not receipt["observed_empty_tree"]:
            raise TexProcessGuardError("refusing success without observed empty tree")
        return subprocess.CompletedProcess(command, returncode, stdout=output, stderr=None)
