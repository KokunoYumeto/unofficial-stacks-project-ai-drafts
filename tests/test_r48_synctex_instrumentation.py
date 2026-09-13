"""Instrumenter lifecycle tests use only harmless synthetic test files."""
from contextlib import ExitStack
import gzip
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools import instrument_r48_synctex as tool

m = tool.mapping


class FakeMutex:
    last = None

    def __init__(self, *args):
        self.owned = False
        self.process_tree_receipts = []
        FakeMutex.last = self

    def __enter__(self):
        self.owned = True
        return self

    def __exit__(self, *args):
        self.owned = False

    def receipt_details(self):
        return {"released": not self.owned}


def sidecar(path, stem):
    with gzip.open(path, "wb") as stream:
        stream.write(("SyncTeX Version:1\nInput:1:" + stem + ".tex\nContent:\n{1\n}1\nPostamble:\nCount:2\n").encode())


class InstrumentationTests(unittest.TestCase):
    def fixture(self, root):
        stems = [*m.STEMS, "unchanged"]
        artifacts = {}
        for stem in stems:
            for suffix in (".pdf", ".aux"):
                (root / (stem + suffix)).write_bytes((stem + suffix).encode())
            artifacts[stem] = {**m.identity(root / (stem + ".pdf")), "diagnostics": {}, "external_references": {}}
        return {"build": {"stems": stems}, "environment": {"source_date_epoch": "1"}}, artifacts

    def run_fixture(self, root, build, artifacts, mutation=None,
                    timestamp_offset_ns=1_000_000_000):
        calls = []
        # Synthetic launches must not depend on filesystem timestamp rounding
        # or on how quickly the runner executes this harmless file fixture.
        clock = {"now": 1_700_000_000_000_000_000}
        def time_ns():
            clock["now"] += 2_000_000_000
            return clock["now"]
        def run(command, source, env, mutex):
            self.assertTrue(mutex.owned)
            self.assertEqual(source, root)
            self.assertEqual(env["SOURCE_DATE_EPOCH"], "1")
            stem = Path(command[-1]).stem
            calls.append(stem)
            sidecar_path = root / (stem + ".synctex.gz")
            sidecar(sidecar_path, stem)
            modified_ns = clock["now"] + timestamp_offset_ns
            os.utime(sidecar_path, ns=(modified_ns, modified_ns))
            capture = root / (stem + "-capture.json")
            capture.write_text("test", encoding="utf-8")
            mutex.process_tree_receipts.append({"path": capture.name, **m.identity(capture)})
            if mutation:
                mutation(root, stem)
        def scan(*args):
            self.assertTrue(FakeMutex.last.owned)
            return {}, {}
        with ExitStack() as stack:
            stack.enter_context(patch.object(tool.time, "time_ns", side_effect=time_ns))
            stack.enter_context(patch.object(m, "recheck_inputs"))
            stack.enter_context(patch.object(m, "check_captures"))
            stack.enter_context(patch.object(tool.builder, "external_reference_labels", return_value={}))
            stack.enter_context(patch.object(tool.builder, "WindowsNamedMutex", FakeMutex))
            stack.enter_context(patch.object(tool.builder, "run", side_effect=run))
            stack.enter_context(patch.object(tool.builder, "scan_tex_diagnostics", side_effect=scan))
            result = tool.instrument(build, artifacts, root, {})
        return result, calls

    def test_exact_two_instrumentations_and_full_profile_preservation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build, artifacts = self.fixture(root)
            (rows, mutex, captures, before, after), calls = self.run_fixture(root, build, artifacts)
            self.assertEqual(calls, list(m.STEMS))
            self.assertEqual(len(rows), len(captures))
            self.assertEqual(before, after)
            self.assertIn("unchanged", before)
            self.assertTrue(mutex["released"])
            self.assertTrue(all(row["tex_mutex_owned_through_immediate_checks"] for row in rows))
            self.assertTrue(all(row["started_ns"] < row["synctex_mtime_ns"]
                                < row["completed_ns"] for row in rows))

    def test_stale_sidecar_timestamp_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build, artifacts = self.fixture(root)
            with self.assertRaisesRegex(ValueError, "sidecar freshness not proved"):
                self.run_fixture(root, build, artifacts, timestamp_offset_ns=-1_000_000_000)
            self.assertFalse(FakeMutex.last.owned)

    def test_future_sidecar_timestamp_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build, artifacts = self.fixture(root)
            with self.assertRaisesRegex(ValueError, "sidecar freshness not proved"):
                self.run_fixture(root, build, artifacts, timestamp_offset_ns=3_000_000_000)
            self.assertFalse(FakeMutex.last.owned)

    def test_changed_other_profile_aux_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build, artifacts = self.fixture(root)
            with self.assertRaisesRegex(ValueError, "another profile artifact"):
                self.run_fixture(root, build, artifacts, lambda root, stem: (root / "unchanged.aux").write_bytes(b"changed"))
            self.assertFalse(FakeMutex.last.owned)

    def test_changed_instrumented_pdf_fails_inside_mutex(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build, artifacts = self.fixture(root)
            with self.assertRaisesRegex(ValueError, "fixed-point bytes changed"):
                self.run_fixture(root, build, artifacts, lambda root, stem: (root / (stem + ".pdf")).write_bytes(b"changed"))
            self.assertFalse(FakeMutex.last.owned)

    def test_existing_sidecar_fails_before_launch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build, artifacts = self.fixture(root)
            sidecar(root / "groupoids.synctex.gz", "groupoids")
            with patch.object(tool.builder, "run") as run, self.assertRaisesRegex(ValueError, "existing sidecar"):
                self.run_fixture(root, build, artifacts)
            run.assert_not_called()

    def test_missing_unaffected_aux_also_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            build, artifacts = self.fixture(root)
            (root / "unchanged.aux").unlink()
            with self.assertRaisesRegex(ValueError, "PDF/AUX missing"):
                self.run_fixture(root, build, artifacts)

    def test_malformed_gzip_or_wrong_source_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "test.gz"
            sidecar(path, "groupoids")
            self.assertGreater(tool.valid_sidecar(path, "groupoids")["decompressed_bytes"], 0)
            with self.assertRaises(ValueError):
                tool.valid_sidecar(path, "spaces-perfect")
            path.write_bytes(b"not-gzip")
            with self.assertRaises(gzip.BadGzipFile):
                tool.valid_sidecar(path, "groupoids")


if __name__ == "__main__":
    unittest.main()
