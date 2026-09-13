"""Regression checks that the new insertion cannot mask unrelated changes."""
from pathlib import Path
import tempfile
import unittest
from illusie_volume_I.verify import composition

ROOT = Path(__file__).resolve().parents[1]

class CompositionIsolation(unittest.TestCase):
    def make_copy(self, folder):
        root = Path(folder)
        (root / "illusie_volume_I").mkdir()
        for name in ("simplicial.tex", "illusie_volume_I/relative-homotopy.tex", "illusie_volume_I/localization.tex"):
            (root / name).write_bytes((ROOT / name).read_bytes())
        return root

    def test_rejects_unrelated_source_change(self):
        with tempfile.TemporaryDirectory(prefix="illusie-composition-") as folder:
            root = self.make_copy(folder)
            path = root / "simplicial.tex"
            path.write_bytes(path.read_bytes().replace(b"Simplicial Methods", b"Changed Methods", 1))
            with self.assertRaisesRegex(AssertionError, "outside the bounded insertion"):
                composition(root)

    def test_rejects_changed_proof_without_matching_root(self):
        with tempfile.TemporaryDirectory(prefix="illusie-composition-") as folder:
            root = self.make_copy(folder)
            path = root / "illusie_volume_I/relative-homotopy.tex"
            path.write_bytes(path.read_bytes().replace(b"bijects homotopies", b"does not biject homotopies", 1))
            with self.assertRaisesRegex(AssertionError, "differs from reviewed snippet"):
                composition(root)

if __name__ == "__main__":
    unittest.main()
