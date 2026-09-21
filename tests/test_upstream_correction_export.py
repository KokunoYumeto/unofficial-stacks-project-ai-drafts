"""Small exporter regression checks without building or touching source files."""
import dataclasses
from types import SimpleNamespace
import unittest
from tools import export_upstream_corrections as e


def unit(name, index=1, source="algebra.tex", start=0, end=3):
    return SimpleNamespace(overlay_index=index, source=source,
        operations=[SimpleNamespace(operation_id=name, start_byte=start, end_byte_exclusive=end)])


class ExportTests(unittest.TestCase):
    def test_exact_successor_removes_only_predecessor(self):
        owners, removed = e.active_operations([unit("old"), unit("new", 2)], {"new": "old"})
        self.assertEqual(removed, {"old"})
        self.assertEqual(set(owners), {"old", "new"})

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

    def test_zip_escape_fails(self):
        with self.assertRaises(ValueError):
            e.archive_bytes({"../a.patch": b"one"})


if __name__ == "__main__":
    unittest.main()
