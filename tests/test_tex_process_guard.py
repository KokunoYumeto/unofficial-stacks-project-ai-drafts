"""Only harmless Python fixtures; never launch a TeX executable."""

import importlib.util
import json
import os
import signal
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock


MODULE = Path(__file__).resolve().parents[1] / "tools" / "tex_process_guard.py"
spec = importlib.util.spec_from_file_location("tex_process_guard_under_test", MODULE)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


@unittest.skipUnless(os.name == "nt", "native Windows process capture test")
class CapturedTreeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="stacks-tex-guard-test-")
        self.root = Path(self.temp.name)
        self.receipt = self.root / "launch.json"

    def tearDown(self):
        self.temp.cleanup()

    def run_python(self, code, **kwargs):
        return guard.run_captured([sys.executable, "-c", code], cwd=self.root,
                                  caller_holds_tex_mutex=True,
                                  receipt_path=self.receipt, **kwargs)

    def read_receipt(self):
        return json.loads(self.receipt.read_text(encoding="utf-8"))

    def test_stdout_stderr_and_identity(self):
        result = self.run_python("import sys; print('out',flush=True); print('err',file=sys.stderr,flush=True)")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "out\nerr\n")
        receipt = self.read_receipt()
        self.assertEqual(receipt["status"], "PASS")
        self.assertTrue(receipt["created_suspended"])
        self.assertTrue(receipt["assigned_before_resume"])
        self.assertTrue(receipt["observed_empty_tree"])
        self.assertFalse(receipt["breakaway_allowed"])
        self.assertGreater(receipt["root_identity"]["creation_filetime_100ns"], 0)
        self.assertEqual(receipt["final_accounting"]["active_processes"], 0)
        guard.validate_capture_receipt(receipt)

    def test_parent_exit_does_not_release_descendant(self):
        code = ("import subprocess,sys; subprocess.Popen([sys.executable,'-c',"
                "\"import time; time.sleep(0.4); print('descendant-finished',flush=True)\"]); "
                "print('root-finished',flush=True)")
        started = time.monotonic()
        result = self.run_python(code)
        self.assertGreater(time.monotonic() - started, 0.35)
        self.assertIn("descendant-finished", result.stdout)
        receipt = self.read_receipt()
        self.assertTrue(receipt["root_exited_before_tree_empty"])
        # A packaged Python executable may add a launcher process.
        self.assertGreaterEqual(receipt["final_accounting"]["total_processes"], 2)

    def test_nonzero_parent_exit_also_drains(self):
        result = self.run_python("import subprocess,sys; subprocess.Popen([sys.executable,'-c',"
                                 "\"import time; time.sleep(.2); print('done')\"]); sys.exit(7)")
        self.assertEqual(result.returncode, 7)
        self.assertIn("done", result.stdout)
        self.assertTrue(self.read_receipt()["observed_empty_tree"])

    def test_timeout_terminates_whole_job(self):
        marker = self.root / "must-not-appear.txt"
        child = f"import time; from pathlib import Path; time.sleep(3); Path({str(marker)!r}).write_text('bad')"
        code = f"import subprocess,sys,time; subprocess.Popen([sys.executable,'-c',{child!r}]); print('started',flush=True); time.sleep(10)"
        with self.assertRaises(subprocess.TimeoutExpired):
            self.run_python(code, timeout=0.4)
        receipt = self.read_receipt()
        self.assertEqual(receipt["status"], "FAIL")
        self.assertTrue(receipt["job_termination_requested"])
        self.assertTrue(receipt["observed_empty_tree"])
        self.assertEqual(receipt["final_accounting"]["active_processes"], 0)
        self.assertGreaterEqual(receipt["final_accounting"]["total_processes"], 2)
        self.assertFalse(marker.exists())

    def test_assignment_failure_never_executes_child(self):
        marker = self.root / "must-not-appear.txt"
        with mock.patch.object(guard._Job, "assign", side_effect=guard.TexProcessGuardError("injected assignment failure")):
            with self.assertRaisesRegex(guard.TexProcessGuardError, "assignment"):
                self.run_python(f"from pathlib import Path; Path({str(marker)!r}).write_text('bad')")
        self.assertFalse(marker.exists())
        receipt = self.read_receipt()
        self.assertFalse(receipt["resumed"])
        self.assertTrue(receipt["unresumed_root_terminated_and_waited"])
        self.assertTrue(receipt["observed_empty_tree"])

    def test_missing_mutex_flag_refuses_launch(self):
        with self.assertRaisesRegex(guard.TexProcessGuardError, "caller must own"):
            guard.run_captured([sys.executable, "-c", "pass"], cwd=self.root,
                               caller_holds_tex_mutex=False, receipt_path=self.receipt)
        self.assertFalse(self.receipt.exists())

    def test_existing_receipt_refuses_launch(self):
        self.receipt.write_text("preserve", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            self.run_python("raise RuntimeError('must not launch')")
        self.assertEqual(self.receipt.read_text(), "preserve")

    def test_breakaway_creation_denied(self):
        result = self.run_python("import subprocess,sys\ntry:\n subprocess.Popen([sys.executable,'-c','pass'],creationflags=0x01000000)\nexcept OSError as e:\n print('denied',e.winerror)\nelse:\n raise AssertionError('breakaway unexpectedly allowed')")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("denied 5", result.stdout)
        self.assertEqual(self.read_receipt()["final_accounting"]["active_processes"], 0)

    def test_failed_accounting_drains_via_independent_kernel_notification(self):
        actual = guard._Job.accounting
        calls = 0

        def fail_after_initial(job):
            nonlocal calls
            calls += 1
            if calls > 1:
                raise guard.TexProcessGuardError("injected accounting failure")
            return actual(job)

        with mock.patch.object(guard._Job, "accounting", fail_after_initial):
            with self.assertRaisesRegex(guard.TexProcessGuardError, "accounting failure"):
                self.run_python("import time; time.sleep(10)")
        receipt = self.read_receipt()
        self.assertTrue(receipt["observed_empty_tree"])
        self.assertEqual(receipt["empty_tree_evidence"], "job_completion_port_active_process_zero")
        self.assertTrue(receipt["job_termination_requested"])

    def test_transient_termination_failure_does_not_unwind_undrained(self):
        actual = guard._Job.terminate
        calls = 0

        def fail_once(job):
            nonlocal calls
            calls += 1
            if calls == 1:
                raise guard.TexProcessGuardError("injected termination failure")
            return actual(job)

        with mock.patch.object(guard._Job, "terminate", fail_once):
            with self.assertRaises(subprocess.TimeoutExpired):
                self.run_python("import time; time.sleep(10)", timeout=.1)
        receipt = self.read_receipt()
        self.assertEqual(receipt["termination_attempts"], 2)
        self.assertTrue(receipt["observed_empty_tree"])
        self.assertIn("termination failure", " ".join(receipt["cleanup_errors"]))

    def test_cleanup_interruption_is_deferred_until_empty(self):
        actual = guard._Job.terminate

        def interrupt_after_termination(job):
            actual(job)
            raise KeyboardInterrupt("injected cleanup interruption")

        with mock.patch.object(guard._Job, "terminate", interrupt_after_termination):
            with self.assertRaises(subprocess.TimeoutExpired):
                self.run_python("import time; time.sleep(10)", timeout=.1)
        receipt = self.read_receipt()
        self.assertTrue(receipt["observed_empty_tree"])
        self.assertIn("KeyboardInterrupt", " ".join(receipt["cleanup_errors"]))

    def test_validator_rejects_forged_lifecycle_and_failure(self):
        self.run_python("pass")
        receipt = self.read_receipt()
        for key, bad in (("status", "FAIL"), ("observed_empty_tree", False),
                         ("returncode", 7), ("caller_asserted_mutex_owned", False),
                         ("assigned_before_resume", False), ("resumed", False),
                         ("breakaway_allowed", True), ("job_termination_requested", True),
                         ("cleanup_errors", ["bad"]), ("root_identity", {"pid": 1}),
                         ("final_accounting", {"active_processes": 1, "total_processes": 1})):
            with self.subTest(field=key):
                with self.assertRaises(guard.TexProcessGuardError):
                    guard.validate_capture_receipt({**receipt, key: bad})

    def test_real_sigint_at_cleanup_loop_boundary_is_deferred(self):
        boundary = next(i for i, line in enumerate(MODULE.read_text().splitlines(), 1)
                        if line.strip() == 'while not receipt["observed_empty_tree"]:')
        injected = False

        def interrupt_at_boundary(frame, event, arg):
            nonlocal injected
            if not injected and event == "line" and frame.f_code.co_filename == str(MODULE) and frame.f_lineno == boundary:
                injected = True
                signal.raise_signal(signal.SIGINT)
            return interrupt_at_boundary

        previous_handler = signal.getsignal(signal.SIGINT)
        previous_trace = sys.gettrace()
        try:
            sys.settrace(interrupt_at_boundary)
            with self.assertRaises(subprocess.TimeoutExpired):
                self.run_python("import time; time.sleep(10)", timeout=.1)
        finally:
            sys.settrace(previous_trace)
        receipt = self.read_receipt()
        self.assertTrue(injected)
        self.assertTrue(receipt["observed_empty_tree"])
        self.assertEqual(receipt["deferred_keyboard_signals"], [signal.SIGINT])
        self.assertEqual(signal.getsignal(signal.SIGINT), previous_handler)


if __name__ == "__main__":
    unittest.main()
