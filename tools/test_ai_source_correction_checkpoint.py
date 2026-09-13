"""Mocked corrected-source checkpoint tests; no real checks/builds or Git writes."""
from copy import deepcopy
import json
from pathlib import Path
import unittest
from unittest.mock import Mock, patch

import ai_source_correction_composition as a
import direct_successor_checkpoint as c
import test_direct_successor_checkpoint as baseline
identity = baseline.identity


def scope():
    return {"correction_id": a.CORRECTION_ID, "candidate_commit": a.CANDIDATE, "candidate_tree": "a" * 40,
            "manifest": {"path": a.MANIFEST, "bytes": 1, "sha256": "A" * 64, "git_blob": "a" * 40},
            "corrected_source_commit": a.CORRECTED, "corrected_source_tree": "b" * 40,
            "sealed_predecessor_commit": a.SEALED, "sealed_predecessor_receipt_sha256": a.SEALED_RECEIPT_SHA256}


class AICheckpointTests(unittest.TestCase):
    def setUp(self):
        baseline.CheckpointFixture.setUp(self)
        self.composition.update(schema=c.AI_COMPOSITION_SCHEMA,
            composition_source_commit=a.CORRECTED, composition_source_tree="b" * 40,
            ai_source_correction_scope=scope(), correction_protected_inputs={"illusie_volume_I/verify.py": identity("ignored")},
            direct_validation_tools={"tools/ai_source_correction_composition.py": identity("ignored")})
        self.illusie = {"status": "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND", "current_commit": "actual-build-commit"}
        self.ai_patch = patch.object(c, "verify_current_illusie", return_value=self.illusie)
        self.ai_mock = self.ai_patch.start()
        self.addCleanup(self.ai_patch.stop)

    def load(self, live=True):
        return c._load_at(self.build, self.source, "validation/old-checkpoint.json", self.checkpoint,
                          self.composition, "actual-build-commit", live=live)

    def test_new_schema_binds_current_illusie_and_preserves_old_ega(self):
        binding, paths, protected = self.load()
        self.assertEqual(binding["schema"], c.SCHEMA_AI)
        self.assertEqual(binding["status"], c.STATUS_AI)
        self.assertEqual(binding["ai_source_correction"], self.composition["ai_source_correction_scope"])
        self.assertEqual(binding["current_illusie_successor"], self.illusie)
        self.assertEqual(binding["semantic_successor"]["commit"], "old-semantic")
        self.assertEqual(binding["canonical_composition"]["composition_source_commit"], a.CORRECTED)
        self.assertIn("illusie_volume_I/verify.py", paths)
        self.assertIn("tools/ai_source_correction_composition.py", paths)
        self.assertTrue(any(r["path"] == "illusie_volume_I/verify.py" and r["role"] == "successor_current_input" for r in protected))

    def test_current_semantic_failure_is_not_swallowed(self):
        self.ai_mock.side_effect = RuntimeError("current Illusie failed")
        with self.assertRaisesRegex(RuntimeError, "Illusie failed"):
            self.load()

    def test_old_source_cannot_certify_corrected_root(self):
        self.build.committed_file_identity.side_effect = lambda source, commit, path: (
            {**identity(path), "bytes": 2} if commit == a.CORRECTED and path == "groupoids.tex" else identity(path))
        with self.assertRaisesRegex(RuntimeError, "root source change"):
            self.load()

    def test_original_checkpoint_immutable(self):
        before = deepcopy(self.checkpoint)
        self.load(live=False)
        self.assertEqual(before, self.checkpoint)
        self.build.capture_source_revision.assert_not_called()

    def test_exact_revision_illusie_uses_requested_head(self):
        self.load(live=False)
        self.assertEqual(self.ai_mock.call_args.args[-1], "actual-build-commit")
        self.build.require_source_checkpoint_unchanged.assert_not_called()


class CurrentIllusieTests(unittest.TestCase):
    def setUp(self):
        self.source = Path("fixture-only")
        self.build = Mock()
        self.paths = [a.MANIFEST, "simplicial.tex", "illusie_volume_I/verify.py",
                      "illusie_volume_I/test_composition.py", "illusie_volume_I/test_ez.py"]
        self.protected = {p: {k: v for k, v in identity(p).items() if k != "path"} for p in self.paths}
        self.composition = {"composition_source_commit": a.CORRECTED, "composition_source_tree": "b" * 40,
                            "ai_source_correction_scope": scope(), "correction_protected_inputs": self.protected}
        self.build.committed_file_identity.side_effect = lambda source, head, path: identity(path)
        self.build.working_file_identity.side_effect = lambda source, path: identity(path)
        self.build.strict_json_loads.side_effect = lambda text, label: json.loads(text)
        self.manifest = {"independent_review": identity("validation/direct-successor-reviewed.json")}
        self.git = Mock()
        self.git.document.return_value = self.manifest
        self.result = {"status": "PASS", "scope": "inventory, labels, and composition only", "current_source_sha256": "A" * 64}

    def run_check(self, *, exit_code=0, result=None, tests_return=0, tests_text="\nRan 5 tests in 0.01s\n\nOK\n"):
        runs = [Mock(returncode=exit_code, stdout=json.dumps(self.result if result is None else result), stderr=""),
                Mock(returncode=tests_return, stdout="", stderr=tests_text)]
        with patch.object(a, "Git", return_value=self.git), patch.object(a, "validate_manifest", return_value=self.protected), \
             patch.object(c.subprocess, "run", side_effect=runs) as runner:
            answer = c.verify_current_illusie(self.build, self.source, self.composition, "actual-head")
        return answer, runner

    def test_current_exact_checker_review_and_five_tests(self):
        answer, runner = self.run_check()
        self.assertEqual(answer["status"], "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND")
        self.assertEqual(answer["checker_result"], self.result)
        self.assertEqual(answer["review"], self.manifest["independent_review"])
        self.assertEqual(answer["current_commit"], "actual-head")
        self.assertEqual(answer["regression_tests"]["tests_run"], 5)
        self.assertEqual(runner.call_count, 2)
        self.assertNotIn("--write-check", str(runner.call_args_list))

    def test_wrong_corrected_endpoint(self):
        self.composition["composition_source_commit"] = a.SEALED
        with self.assertRaisesRegex(ValueError, "source commit"):
            self.run_check()

    def test_missing_dossier_checker(self):
        self.protected.pop("illusie_volume_I/verify.py")
        with self.assertRaisesRegex(RuntimeError, "incomplete"):
            self.run_check()

    def test_stale_committed_checker(self):
        self.build.committed_file_identity.side_effect = lambda source, head, path: {**identity(path), "bytes": 2}
        with self.assertRaisesRegex(RuntimeError, "identity mismatch"):
            self.run_check()

    def test_checker_fail(self):
        with self.assertRaisesRegex(RuntimeError, "mechanical check failed"):
            self.run_check(exit_code=1)

    def test_checker_stale_source_hash(self):
        with self.assertRaisesRegex(RuntimeError, "source binding"):
            self.run_check(result={**self.result, "current_source_sha256": "B" * 64})

    def test_regression_tests_fail(self):
        with self.assertRaisesRegex(RuntimeError, "regression tests failed"):
            self.run_check(tests_return=1)

    def test_missing_fifth_test(self):
        with self.assertRaisesRegex(RuntimeError, "regression tests failed"):
            self.run_check(tests_text="Ran 4 tests in 0.01s\n\nOK\n")


if __name__ == "__main__":
    unittest.main()
