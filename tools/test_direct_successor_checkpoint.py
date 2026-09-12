"""Small mocked fixtures; never execute historical checks, TeX or Git writes."""
from copy import deepcopy
from pathlib import Path
from unittest.mock import Mock, patch
import unittest

import direct_successor_checkpoint as c


def identity(path):
    return {"path": path, "bytes": 1, "sha256": "A" * 64, "git_blob": "a" * 40}


class CheckpointFixture(unittest.TestCase):
    def setUp(self):
        self.source = Path("fixture-only")
        self.build = Mock()
        self.build.require_commit_object.side_effect = lambda source, value, label: value
        self.build.git.side_effect = lambda source, *args: (
            "schemes.tex\ngroupoids.tex\nstyle.sty" if args[0] == "ls-tree" else "tree-actual")
        self.build.committed_file_identity.side_effect = lambda source, commit, path: identity(path)
        self.build.working_file_identity.side_effect = lambda source, path: identity(path)
        self.build.committed_regular_files.return_value = []
        self.build.EGA_PRECONTENT_TOOL_ROLES = []
        self.build.EGA_SHARED_BUILD_SUFFIXES = {".sty"}
        self.build.EGA_NON_WORKTREE_PROTECTED_ROLES = {"historical_checkpoint_input"}
        self.build.protected_input.side_effect = lambda role, commit, row: {"role": role, "commit": commit, **row}
        self.build.canonical_tuple_sha256.return_value = "B" * 64
        self.build.parse_json_blob.return_value = {
            "schema": c.direct_successor_composition._helper.SCHEMA, "status": "PASS",
            "composition": {"source_commit": "old-source", "base_commit": "old-base"}}
        self.composition = {"schema": c.DIRECT_SCHEMA, "previous_public_main_head": "prior-public",
            "composition_source_commit": "new-source", "composition_source_tree": "new-tree",
            "receipt": "validation/composition-current.json", "receipt_git_blob": "c" * 40,
            "receipt_sha256": "C" * 64}
        self.checkpoint = {"content": {"commit": "old-content"}}
        self.patches = [patch.object(c, "receipt_anchor", return_value="real-anchor"),
            patch.object(c, "verify_historical", return_value=({"post_content": {"head_tree": "anchor-tree"},
                                                                   "external_authority_inputs": []}, ())),
            patch.object(c, "verify_semantic", return_value=({"commit": "old-semantic"}, []))]
        self.mocks = [p.start() for p in self.patches]
        self.addCleanup(lambda: [p.stop() for p in reversed(self.patches)])

    def load(self, live=True):
        return c._load_at(self.build, self.source, "validation/old-checkpoint.json", self.checkpoint,
                          self.composition, "actual-build-commit", live=live)

    def test_semantic_parent_remains_its_actual_inherited_source(self):
        binding, _, _ = self.load()
        self.assertEqual(binding["schema"], c.SCHEMA)
        self.assertEqual(binding["post_content"]["head_commit"], "actual-build-commit")
        self.assertEqual(self.mocks[2].call_args.args[3], {
            "composition_source_commit": "old-source", "composition_base_commit": "old-base"})
        self.assertEqual(binding["canonical_composition"]["composition_source_commit"], "new-source")
        self.assertEqual(binding["inherited_composition"]["commit"], "prior-public")
        self.build.require_source_checkpoint_unchanged.assert_called_once()

    def test_exact_old_revision_never_substitutes_current_head(self):
        binding, _, _ = self.load(live=False)
        self.assertEqual(binding["post_content"]["head_commit"], "actual-build-commit")
        self.build.capture_source_revision.assert_not_called()
        self.build.require_source_checkpoint_unchanged.assert_not_called()

    def test_retains_original_receipt_object(self):
        before = deepcopy(self.checkpoint)
        self.load()
        self.assertEqual(before, self.checkpoint)

    def test_rejects_non_direct_composition(self):
        self.composition["schema"] = "invented"
        with self.assertRaisesRegex(RuntimeError, "typed direct"):
            self.load()

    def test_rejects_inherited_semantic_drift(self):
        self.build.committed_file_identity.side_effect = lambda source, commit, path: (
            {**identity(path), "bytes": 2} if commit == "prior-public" and path == "ega/check.py" else identity(path))
        with self.assertRaisesRegex(RuntimeError, "semantic input drifted"):
            self.load()

    def test_rejects_current_source_drift(self):
        self.build.committed_file_identity.side_effect = lambda source, commit, path: (
            {**identity(path), "bytes": 2} if commit == "new-source" and path == "groupoids.tex" else identity(path))
        with self.assertRaisesRegex(RuntimeError, "root source change"):
            self.load()

    def test_rejects_untyped_inherited_composition(self):
        self.build.parse_json_blob.return_value["schema"] = "invented"
        with self.assertRaisesRegex(RuntimeError, "inherited composition"):
            self.load()

    def test_rejects_working_verifier_drift(self):
        self.build.working_file_identity.side_effect = lambda source, path: {**identity(path), "bytes": 2}
        with self.assertRaisesRegex(RuntimeError, "working bytes differ"):
            self.load()


if __name__ == "__main__":
    unittest.main()
