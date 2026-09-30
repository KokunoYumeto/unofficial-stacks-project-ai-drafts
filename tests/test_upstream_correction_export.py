"""Small exporter regression checks without building or touching source files."""
import dataclasses
import io
import zipfile
from types import SimpleNamespace
import unittest
from tools import export_upstream_corrections as e


def unit(name, index=1, source="algebra.tex", start=0, end=3):
    return SimpleNamespace(overlay_index=index, source=source,
        operations=[SimpleNamespace(operation_id=name, start_byte=start, end_byte_exclusive=end)])


class ExportTests(unittest.TestCase):
    def test_editorial_completion_stays_out_of_corrections_only(self):
        value = SimpleNamespace(source='more-algebra.tex', defect_class='editorial_proof_completion')
        self.assertEqual(e.correction_exclusion_reason(value), 'excluded_editorial_proof_completion')

    def test_source_proof_correction_remains_exportable(self):
        value = SimpleNamespace(source='more-algebra.tex', defect_class='mathematical_source_correction')
        self.assertIsNone(e.correction_exclusion_reason(value))

    def test_fork_tag_exclusion_remains(self):
        value = SimpleNamespace(source='tags/tags', defect_class='copyedit')
        self.assertEqual(e.correction_exclusion_reason(value), 'excluded_fork_tag_allocation')

    def test_missing_summary_locus_uses_exact_operation_lines(self):
        ops = [SimpleNamespace(source_start_line=a, source_end_line=b) for a, b in [(596,596),(592,592),(594,594)]]
        self.assertEqual(e.review_locus(SimpleNamespace(locus=''), ops), '592, 594, 596')

    def test_missing_all_locators_fails(self):
        with self.assertRaises(ValueError):
            e.review_locus(SimpleNamespace(locus=''), [])

    def test_exact_successor_removes_only_predecessor(self):
        owners, removed = e.active_operations([unit("old"), unit("new", 2)], {"new": "old"})
        self.assertEqual(removed, {"old"})
        self.assertEqual(set(owners), {"old", "new"})

    def test_supersession_in_multi_operation_unit_preserves_other_edits(self):
        earlier = unit("earlier", source="derived.tex", start=4, end=8)
        later = unit("unrelated", 2, source="derived.tex", start=12, end=15)
        later.operations.append(SimpleNamespace(operation_id="replacement", start_byte=4, end_byte_exclusive=8))
        owners, removed = e.active_operations([earlier, later], {"replacement":"earlier"})
        self.assertEqual(removed, {"earlier"})
        self.assertEqual({name for name in owners if name not in removed}, {"unrelated", "replacement"})

    def test_unknown_predecessor_fails(self):
        with self.assertRaisesRegex(ValueError, "unknown"):
            e.active_operations([unit("new", 2)], {"new": "absent"})

    def test_different_path_cannot_supersede(self):
        with self.assertRaisesRegex(ValueError, "invalid"):
            e.active_operations([unit("old"), unit("new", 2, "modules.tex")], {"new": "old"})

    def test_disjoint_locus_cannot_supersede(self):
        with self.assertRaisesRegex(ValueError, "invalid"):
            e.active_operations([unit("old"), unit("new", 2, start=4, end=6)], {"new": "old"})

    def test_duplicate_id_fails(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            e.active_operations([unit("same"), unit("same", 2)], {})

    def test_source_scope(self):
        for name in ("tags/tags", "../algebra.tex", "new/theorem.tex", "README.md"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                e.source_path(name)

    def test_diff_only_named_chapter(self):
        patch = e.make_patch("algebra.tex", b"before\n", b"after\n")
        self.assertIn(b"diff --git a/algebra.tex b/algebra.tex", patch)
        self.assertIn(b"-before\n+after\n", patch)

    def test_missing_newline_fails(self):
        with self.assertRaises(ValueError):
            e.make_patch("algebra.tex", b"before", b"after")

    def test_zip_deterministic(self):
        self.assertEqual(e.archive_bytes({"a.patch": b"one"}), e.archive_bytes({"a.patch": b"one"}))

    def test_zip_platform_and_compressor_independent(self):
        with zipfile.ZipFile(io.BytesIO(e.archive_bytes({"a.patch": b"one"}))) as archive:
            entry = archive.getinfo("a.patch")
            self.assertEqual(entry.create_system, 3)
            self.assertEqual(entry.compress_type, zipfile.ZIP_STORED)
            self.assertEqual(entry.date_time, (2026, 9, 22, 0, 0, 0))

    def test_zip_escape_fails(self):
        with self.assertRaises(ValueError):
            e.archive_bytes({"../a.patch": b"one"})


if __name__ == "__main__":
    unittest.main()
