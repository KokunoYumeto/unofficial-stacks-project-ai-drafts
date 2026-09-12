"""No TeX, PDF renderer or network is launched by these mapping tests."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools import map_r48_visual_loci as m
from tools import tex_process_public_receipt as public_capture


def operation(start, old, replacement, **extra):
    return {"start_byte": start, "end_byte_exclusive": start + len(old.encode()),
            "old_text": old, "replacement_text": replacement,
            "operation_id": "TEST-OP", "stable_id": "TEST", "source_start_line": 1,
            "authority_start_byte": start, **extra}


class MappingTests(unittest.TestCase):
    def map(self, row, rows, final, pages=10, cache=None):
        return m.mapped_operation(row, rows, final, Path("."), "groupoids.tex", pages, {} if cache is None else cache)

    def test_byte_delta_not_authority_line(self):
        first = operation(0, "one", "one\nextra", operation_id="BEFORE")
        second = operation(4, "two", "TWO", authority_start_byte=0)
        final = b"one\nextra\nTWO\n"
        with patch.object(m, "synctex_pages", return_value=[3]) as query:
            result = self.map(second, [first, second], final)
        self.assertEqual(result["final_cumulative_line"], 3)
        self.assertEqual(result["final_start_byte"], 10)
        self.assertEqual(result["authority_start_byte"], 0)
        self.assertEqual(query.call_args.args[-1], 3)

    def test_multibyte_prefix_counts_bytes(self):
        first = operation(0, "a", "é")
        row = operation(2, "x", "X")
        with patch.object(m, "synctex_pages", return_value=[1]):
            result = self.map(row, [first, row], "é\nX\n".encode())
        self.assertEqual(result["final_start_byte"], 3)

    def test_multiline_replacement_queries_every_line(self):
        row = operation(0, "a", "a\nb\nc\n")
        with patch.object(m, "synctex_pages", side_effect=lambda root, source, line: [line]) as query:
            result = self.map(row, [row], b"a\nb\nc\n")
        self.assertEqual(result["pages"], [1, 2, 3])
        self.assertEqual(query.call_count, 3)

    def test_shared_line_query_cached(self):
        cache = {}
        rows = [operation(0, "a", "A"), operation(2, "b", "B")]
        with patch.object(m, "synctex_pages", return_value=[2]) as query:
            for row in rows:
                self.map(row, rows, b"A B\n", cache=cache)
        self.assertEqual(query.call_count, 1)

    def test_deletion_maps_surviving_context(self):
        row = operation(2, "bad\n", "")
        with patch.object(m, "synctex_pages", return_value=[1]):
            result = self.map(row, [row], b"a\nb\n")
        self.assertTrue(result["deletion"])
        self.assertEqual(result["replacement_bytes"], 0)
        self.assertEqual(result["deletion_context"]["text"], "a\nb\n")

    def test_final_drift_rejected_before_query(self):
        row = operation(0, "a", "A")
        with patch.object(m, "synctex_pages") as query, self.assertRaisesRegex(ValueError, "interval differs"):
            self.map(row, [row], b"B")
        query.assert_not_called()

    def test_invalid_pages_fail_closed(self):
        row = operation(0, "a", "A")
        for pages in ([], [0], [11], [True]):
            with self.subTest(pages=pages), patch.object(m, "synctex_pages", return_value=pages):
                with self.assertRaisesRegex(ValueError, "outside PDF"):
                    self.map(row, [row], b"A")

    def test_manifest_reference_requires_bytes_and_hash(self):
        raw = b"abc"
        valid = {"x": [{"path": "operation-spec.json", "bytes": 3, "sha256": m.sha256(raw)}]}
        m.manifest_bound(valid, "operation-spec.json", raw)
        for field, value in (("bytes", 4), ("sha256", "0" * 64)):
            bad = deepcopy(valid)
            bad["x"][0][field] = value
            with self.assertRaises(ValueError):
                m.manifest_bound(bad, "operation-spec.json", raw)

    def test_duplicate_conflicting_manifest_reference_rejected(self):
        row = {"path": "x", "bytes": 1, "sha256": m.sha256(b"x")}
        with self.assertRaises(ValueError):
            m.manifest_bound([row, {**row, "bytes": 2}], "x", b"x")

    def test_path_escape_rejected(self):
        for path in ("../x", "/x", "C:/x", "a\\b", "a/./b", ""):
            with self.subTest(path=path), self.assertRaises(ValueError):
                m.safe_path(path)

    def test_cross_checkout_tooling_rejected(self):
        before = m.ROOT
        with self.assertRaisesRegex(ValueError, "cross-checkout tooling"):
            m.configure_source(before / "not-the-executing-worktree")
        self.assertEqual(m.ROOT, before)

    def test_capture_window_accounts_for_whole_second_precision(self):
        mutex = {"acquired_utc": "2026-01-01T00:00:00Z", "released_utc": "2026-01-01T00:00:02Z"}
        ns = 1767225600 * 1_000_000_000
        rows = [{"started_ns": ns, "synctex_mtime_ns": ns + 1, "completed_ns": ns + 2}]
        m.validate_capture_window(mutex, rows)
        with self.assertRaises(ValueError):
            m.validate_capture_window(mutex, rows + [{"started_ns": ns, "synctex_mtime_ns": ns, "completed_ns": ns}])

    def test_captured_raw_bytes_and_unique_ids_required(self):
        row, _ = self.public_fixture()
        m.check_captures([row], 1)
        for bad in ({**row, "bytes": 1}, {**row, "receipt": {}}, {**row, "path": "../x"}):
            with self.assertRaises(ValueError):
                m.check_captures([bad], 1)
        with self.assertRaises(ValueError):
            m.check_captures([row, row], 2)
        with self.assertRaisesRegex(ValueError, "invocation reused"):
            m.check_captures([row, {**row, "path": "tex-process-tree/launch-000002.json"}], 2)
        noncanonical = row["raw_text"] + " "
        with self.assertRaisesRegex(ValueError, "not canonical"):
            m.check_captures([{**row, "raw_text": noncanonical, "bytes": len(noncanonical),
                              "sha256": m.sha256(noncanonical.encode())}], 1)

    def public_fixture(self):
        # Synthetic native receipt fixture, explicitly not an execution claim.
        private = {"schema": public_capture.RECEIPT_SCHEMA,
                   **deepcopy(public_capture.LIFECYCLE_CONSTANTS),
                   "started_utc": "2026-01-01T00:00:00Z", "finished_utc": "2026-01-01T00:00:01Z",
                   "root_identity": {"pid": 123, "creation_filetime_100ns": 1},
                   "initial_accounting": {"active_processes": 1, "total_processes": 1, "total_terminated_processes": 0},
                   "final_accounting": {"active_processes": 0, "total_processes": 1, "total_terminated_processes": 1},
                   "cwd": "C:/private-test-directory", "command": ["C:/private-bin/pdflatex", "groupoids.tex"]}
        original = json.dumps(private).encode()
        receipt = public_capture.public_capture_receipt(original)
        raw = public_capture.canonical_public_capture_bytes(receipt)
        row = {"path": "tex-process-tree/launch-000001.json", "raw_text": raw.decode(),
               "receipt": receipt, "bytes": len(raw), "sha256": m.sha256(raw)}
        return row, original

    def test_real_public_projection_validator_without_mock(self):
        row, original = self.public_fixture()
        receipt, raw = row["receipt"], row["raw_text"].encode()
        m.check_captures([row], 1)
        self.assertNotIn(b"private-test-directory", raw)
        self.assertNotIn(b"private-bin", raw)
        self.assertEqual(receipt["provenance"]["private_capture"]["sha256"], m.sha256(original))
        bad = deepcopy(receipt)
        bad["lifecycle"]["final_accounting"]["active_processes"] = 1
        bad_raw = json.dumps(bad).encode()
        with self.assertRaises(ValueError):
            m.check_captures([{**row, "raw_text": bad_raw.decode(), "receipt": bad,
                              "bytes": len(bad_raw), "sha256": m.sha256(bad_raw)}], 1)

    def test_capture_is_bound_to_owning_mutex_window(self):
        row, _ = self.public_fixture()
        mutex = {"acquired_utc": "2026-01-01T00:00:00Z", "released_utc": "2026-01-01T00:00:01Z"}
        m.check_captures([row], 1, mutex)
        with self.assertRaisesRegex(ValueError, "outside owning mutex"):
            m.check_captures([row], 1, {**mutex, "acquired_utc": "2026-01-01T00:00:02Z"})

    def test_final_generated_recheck_catches_prior_stem_drift(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(m, "ROOT", Path(temp)):
            root = Path(temp)
            for name in ("groupoids.pdf", "groupoids.aux", "groupoids.synctex.gz", "unchanged.aux"):
                (root / name).write_bytes(name.encode())
            sources = {"groupoids.tex": {kind: {"path": name, **m.identity(root / name)}
                       for kind, name in (("pdf", "groupoids.pdf"), ("synctex", "groupoids.synctex.gz"))}}
            before = {stem: m.fixed_snapshot(root, stem) for stem in ("groupoids", "unchanged")}
            m.recheck_generated(sources, before)
            (root / "groupoids.pdf").write_bytes(b"changed during later stem query")
            with self.assertRaises(ValueError):
                m.recheck_generated(sources, before)
            (root / "groupoids.pdf").write_bytes(b"groupoids.pdf")
            (root / "unchanged.aux").write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "full-profile"):
                m.recheck_generated(sources, before)

    def test_unplanned_tex_stem_rejected(self):
        with self.assertRaises(ValueError):
            m.tex_command("algebra")

    def test_actual_frozen_r48_replay_27_operations(self):
        # Read-only committed evidence; no build or generated-receipt write.
        m.configure_source(Path(__file__).resolve().parents[1])
        authorities, grouped, inputs = m.frozen_operations(m.COMPOSED)
        self.assertEqual(sum(map(len, grouped.values())), 27)
        self.assertEqual(len({row["path"] for row in inputs}), len(inputs))
        moved = 0
        for source, operations in grouped.items():
            before, final = m.git_blob(m.ADMISSION, source), m.git_blob(m.COMPOSED, source)
            rebased = m.cumulative_operations(authorities[source], before, final, operations, source)
            self.assertEqual(len(rebased), m.EXPECTED_APPLIED[Path(source).stem])
            with patch.object(m, "synctex_pages", return_value=[1]):
                for row in rebased:
                    mapped = m.mapped_operation(row, rebased, final, m.ROOT, source, 100, {})
                    moved += mapped["authority_start_line"] != mapped["final_cumulative_line"]
                    self.assertEqual(final[mapped["final_start_byte"]:mapped["final_end_byte_exclusive"]],
                                     row["replacement_text"].encode())
        self.assertGreater(moved, 0, "test must actually exercise cumulative line offsets")


if __name__ == "__main__":
    unittest.main()
