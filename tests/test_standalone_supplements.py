"""Bounded tests: no TeX, network calls, or changes to mathematical source."""
import io
import json
import unittest
import zipfile
from tools import validate_standalone_supplements as v


def package(extra=None, altered_source=False):
    body = b"complete source"
    names = {"COPYING": b"license", "tools/tex_process_guard.py": b"guard",
             "pursuing-stacks/build.py": b"builder", "pursuing-stacks/check.py": b"check",
             "pursuing-stacks/REPRODUCE.md": b"instructions", "pursuing-stacks/body.tex": body}
    if extra:
        names[extra] = b"unexpected"
    rows = [{"path": n, "bytes": len(b), "sha256": v.sha(b)} for n, b in names.items()]
    manifest = {"files": rows, "complete_editable_body": "pursuing-stacks/body.tex",
                "reproduction": "pursuing-stacks/REPRODUCE.md"}
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        for name, data in names.items():
            archive.writestr(name, b"changed" if altered_source and name.endswith(".tex") else data)
        archive.writestr("source-package.json", json.dumps(manifest))
    return stream.getvalue(), body


class ProtectionTests(unittest.TestCase):
    def test_exact_document_allowlist(self):
        v.check_changes([("M", "README.md")], v.DOCS)

    def test_root_mathematics_rejected(self):
        with self.assertRaisesRegex(ValueError, "protected"):
            v.check_changes([("M", "categories.tex")], v.DOCS)

    def test_registry_rejected(self):
        with self.assertRaisesRegex(ValueError, "protected"):
            v.check_changes([("M", "ai-integrated/registry/overlays.json")], v.DOCS)

    def test_historical_receipt_and_legacy_tool_rejected(self):
        for name in ("validation/composition-current.json", "tools/validate_direct_successor_release.py"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "protected"):
                v.check_changes([("M", name)], v.DOCS | v.NEW_TOOLS)

    def test_unlisted_supplement_rejected(self):
        with self.assertRaisesRegex(ValueError, "protected"):
            v.check_changes([("A", "pursuing-stacks/unreviewed.tex")], {"pursuing-stacks/" + x for x in v.MODULE_FILES})

    def test_deletion_rejected(self):
        with self.assertRaisesRegex(ValueError, "deletion"):
            v.check_changes([("D", "README.md")], v.DOCS)

    def test_package_complete(self):
        raw, body = package()
        v.check_package(raw, "pursuing-stacks/body.tex", body)

    def test_package_tamper_rejected(self):
        raw, body = package(altered_source=True)
        with self.assertRaisesRegex(ValueError, "byte/hash"):
            v.check_package(raw, "pursuing-stacks/body.tex", body)

    def test_path_escape_rejected(self):
        raw, body = package(extra="../escape")
        with self.assertRaisesRegex(ValueError, "unsafe"):
            v.check_package(raw, "pursuing-stacks/body.tex", body)

    def test_direct_source_mismatch_rejected(self):
        raw, _ = package()
        with self.assertRaisesRegex(ValueError, "direct/archived"):
            v.check_package(raw, "pursuing-stacks/body.tex", b"different")

    def test_both_actual_modules(self):
        read = lambda name: (v.ROOT / name).read_bytes()
        self.assertEqual(v.check_module(read, "")["statements"], 7)
        self.assertEqual(v.check_module(read, "intervals-")["statements"], 8)


if __name__ == "__main__":
    unittest.main()
