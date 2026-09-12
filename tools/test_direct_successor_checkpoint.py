"""Small mocked fixtures; never execute historical checks, TeX or Git writes."""
from copy import deepcopy
import json
import os
from pathlib import Path
from unittest.mock import Mock, patch
import unittest

if __package__:
    from . import direct_successor_checkpoint as c
else:
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
            patch.object(c, "verify_historical_semantic", return_value=({"commit": "old-semantic"}, [], [])),
            patch.object(c, "verify_current_ega", return_value=({"status": "PASS_CURRENT_PUBLIC_EGA_PRESERVED"}, []))]
        self.mocks = [p.start() for p in self.patches]
        self.addCleanup(lambda: [p.stop() for p in reversed(self.patches)])

    def load(self, live=True):
        return c._load_at(self.build, self.source, "validation/old-checkpoint.json", self.checkpoint,
                          self.composition, "actual-build-commit", live=live)

    def test_semantic_parent_remains_its_actual_inherited_source(self):
        binding, _, _ = self.load()
        self.assertEqual(binding["schema"], c.SCHEMA)
        self.assertEqual(binding["post_content"]["head_commit"], "actual-build-commit")
        self.assertEqual(self.mocks[2].call_args.args[2:4], ("prior-public", "actual-build-commit"))
        self.assertEqual(self.mocks[2].call_args.args[4], {
            "composition_source_commit": "old-source", "composition_base_commit": "old-base"})
        self.assertEqual(binding["canonical_composition"]["composition_source_commit"], "new-source")
        self.assertEqual(binding["inherited_composition"]["commit"], "prior-public")
        self.assertEqual(binding["semantic_successor"]["commit"], "old-semantic")
        self.assertEqual(binding["current_ega_successor"]["status"], "PASS_CURRENT_PUBLIC_EGA_PRESERVED")
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


class SemanticJoinTests(unittest.TestCase):
    def setUp(self):
        self.source = Path("synthetic-current-only")
        self.build = Mock()
        self.build.require_commit_object.side_effect = lambda source, value, label: value
        self.build.require_safe_posix_path.side_effect = lambda value, label: value
        self.build.committed_file_identity.side_effect = lambda source, commit, path: identity(path)
        self.build.git.return_value = "historical-semantic-head"
        self.build.protected_input.side_effect = lambda role, commit, row: {"role": role, "commit": commit, **row}
        self.build.canonical_tuple_sha256.return_value = "B" * 64
        self.build.strict_json_loads.side_effect = lambda text, label: json.loads(text)
        self.build.EGA_SHARED_BUILD_SUFFIXES = {".sty"}
        self.paths = ["ega/check.py", "ega/intake.py", "ega/agent.csv", c.SEMANTIC_PATH,
                      c.CURRENT_EGA_VALIDATION_PATH, "tools/ega_i74_semantic_contract.py"]
        self.expected = {"schema": "ega-stacks-scaffold-check-v1", "status": "PASS", "errors": [],
                         "counts": {"agent.csv": 289}}
        self.validation = {"schema": "ega-i74-root-integration-validation/v1", "status": "PASS",
            "integrated_source_commit": "current-integration", "candidate_files": [identity("ega/check.py")],
            "gates": [{"stage": "ega_checker", "exit_code": 0, "output": json.dumps(self.expected)}]}
        self.build.parse_json_blob.return_value = self.validation

    def current(self, result=None):
        completed = Mock(returncode=0, stdout=json.dumps(self.expected if result is None else result), stderr="")
        with patch.object(c, "ega_dependency_paths", return_value=self.paths), \
             patch.object(c, "require_exact_inputs", return_value=[identity(p) for p in self.paths]), \
             patch.object(c.subprocess, "run", return_value=completed) as runner:
            result = c.verify_current_ega(self.build, self.source, "prior-public", "current-head")
        return result, runner

    def test_current_result_separate_and_bound_to_current_receipt(self):
        (result, paths), runner = self.current()
        self.assertEqual(result["checker"], self.expected)
        self.assertEqual(result["previous_public_commit"], "prior-public")
        self.assertEqual(result["current_commit"], "current-head")
        self.assertTrue(result["historical_semantic_receipt_not_relabelled"])
        self.assertEqual(paths, self.paths)
        self.assertEqual(runner.call_args.kwargs["cwd"], self.source)

    def test_current_dependency_drift_rejected_before_run(self):
        self.build.committed_file_identity.side_effect = lambda source, commit, path: (
            {**identity(path), "bytes": 2} if commit == "current-head" and path == "tools/ega_i74_semantic_contract.py" else identity(path))
        with self.assertRaisesRegex(RuntimeError, "input drifted"):
            self.current()

    def test_current_referenced_receipt_drift_rejected(self):
        self.build.committed_file_identity.side_effect = lambda source, commit, path: (
            {**identity(path), "bytes": 2} if commit == "current-head" and path == c.CURRENT_EGA_VALIDATION_PATH else identity(path))
        with self.assertRaisesRegex(RuntimeError, "input drifted"):
            self.current()

    def test_later_current_input_deletion_rejected(self):
        with patch.object(c, "ega_dependency_paths", side_effect=[self.paths, self.paths[:-1]]):
            with self.assertRaisesRegex(RuntimeError, "inventory changed"):
                c.verify_current_ega(self.build, self.source, "prior", "head")

    def test_old_checker_counts_cannot_replace_current_counts(self):
        with self.assertRaisesRegex(RuntimeError, "differs from already-public"):
            self.current({**self.expected, "counts": {"agent.csv": 259}})

    def test_current_nonpassing_or_empty_gate_rejected(self):
        for bad in ([], [{"stage": "ega_checker", "exit_code": 1, "output": json.dumps(self.expected)}]):
            with self.subTest(gates=bad):
                self.validation["gates"] = bad
                with self.assertRaisesRegex(RuntimeError, "passing checker gate"):
                    self.current()

    def test_current_candidate_artifact_binding_rejected(self):
        self.validation["candidate_files"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(RuntimeError, "candidate binding mismatch"):
            self.current()

    def test_historical_executes_at_own_detached_head(self):
        target = Path("synthetic-historical-worktree")
        semantic = {"commit": "historical-semantic-head", "receipt": identity(c.SEMANTIC_PATH),
                    "checker": {"status": "PASS", "counts": {"agent.csv": 259}}}
        with patch.object(c, "ega_dependency_paths", return_value=self.paths), \
             patch.object(c, "semantic_worktree", return_value=target), \
             patch.object(c, "require_exact_inputs", return_value=[identity(p) for p in self.paths]), \
             patch.object(c, "verify_semantic", return_value=(semantic, self.paths)) as verifier:
            result, _, protected = c.verify_historical_semantic(
                self.build, self.source, "prior-public", "new-head", {"composition_source_commit": "old-source"})
        self.assertEqual(verifier.call_args.args[1:3], (target, "historical-semantic-head"))
        self.assertEqual(result["checker"]["counts"]["agent.csv"], 259)
        self.assertTrue(result["validated_at_own_head"])
        self.assertTrue(all(row["commit"] == "historical-semantic-head" for row in protected))

    def test_historical_receipt_mutation_rejected(self):
        self.build.committed_file_identity.side_effect = lambda source, commit, path: (
            {**identity(path), "bytes": 2} if commit == "prior-public" else identity(path))
        with self.assertRaisesRegex(RuntimeError, "receipt was rewritten"):
            c.verify_historical_semantic(self.build, self.source, "prior-public", "new-head", {})

    def test_historical_input_drift_after_execution_rejected(self):
        semantic = {"commit": "historical-semantic-head", "receipt": identity(c.SEMANTIC_PATH)}
        with patch.object(c, "ega_dependency_paths", return_value=self.paths), \
             patch.object(c, "semantic_worktree", return_value=Path("synthetic-historical")), \
             patch.object(c, "require_exact_inputs", side_effect=[[identity("ega/intake.py")], []]), \
             patch.object(c, "verify_semantic", return_value=(semantic, [])):
            with self.assertRaisesRegex(RuntimeError, "inputs changed"):
                c.verify_historical_semantic(self.build, self.source, "prior", "head", {})

    def test_historical_root_input_is_in_full_byte_inventory(self):
        self.build.git.return_value = "schemes.tex\ngroupoids.tex\nstyle.sty\nREADME.md"
        with patch.object(c, "ega_dependency_paths", return_value=self.paths):
            paths = c.semantic_input_paths(self.build, self.source, "old-head")
        self.assertTrue({"schemes.tex", "groupoids.tex", "style.sty", "tags/tags", "my.bib"} <= set(paths))
        self.build.working_file_identity.side_effect = lambda source, path: (
            {**identity(path), "bytes": 2} if path == "schemes.tex" else identity(path))
        with self.assertRaisesRegex(RuntimeError, "working input differs: schemes.tex"):
            c.require_exact_inputs(self.build, self.source, "old-head", paths)

    def test_isolated_cache_environment_restored(self):
        previous = {key: os.environ.get(key) for key in ("PYTHONPYCACHEPREFIX", "PYTHONDONTWRITEBYTECODE")}
        with c.isolated_checker_import_cache():
            target = Path(os.environ["PYTHONPYCACHEPREFIX"])
            self.assertTrue(target.is_dir())
            self.assertEqual(list(target.iterdir()), [])
            self.assertEqual(os.environ["PYTHONDONTWRITEBYTECODE"], "1")
        self.assertFalse(target.exists())
        self.assertEqual(previous, {key: os.environ.get(key) for key in previous})


if __name__ == "__main__":
    unittest.main()
