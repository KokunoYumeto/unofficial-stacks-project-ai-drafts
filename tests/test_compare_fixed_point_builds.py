"""Non-TeX adverse tests for exact, mutex-aware checkpoint reproduction."""

import copy
import json
import unittest
from unittest import mock

from tools import compare_fixed_point_builds as comparator
from tools import validate_unified_repository as validator


def mutex(hour=10, abandoned=False):
    return {
        "schema": validator.TEX_MUTEX_RECEIPT_SCHEMA,
        "status": "PASS", "name": validator.TEX_MUTEX_NAME,
        "namespace": "Windows Global",
        "acquisition_timeout_ms": validator.TEX_MUTEX_TIMEOUT_MS,
        "wait_started_utc": f"2026-09-06T{hour}:00:00Z",
        "acquired_utc": f"2026-09-06T{hour}:00:01Z",
        "wait_duration_ms": 1000.0,
        "wait_result_code": "0x00000080" if abandoned else "0x00000000",
        "wait_result": "abandoned_recovered" if abandoned else "acquired",
        "abandoned_mutex_recovered": abandoned,
        "ownership_acquired": True,
        "held_scope": validator.TEX_MUTEX_HELD_SCOPE,
        "released_utc": f"2026-09-06T{hour}:00:03Z",
        "held_duration_ms": 2000.0,
        "release_result": "released_in_finally",
    }


def receipt(hour=10, abandoned=False):
    composition = {
        "receipt": "validation/composition-current.json", "receipt_git_blob": "c" * 40,
        "receipt_sha256": "D" * 64, "composition_source_commit": "e" * 40,
        "registry_cutoff_commit": "f" * 40,
    }
    return {
        "schema": "unofficial-ai-integrated-stacks-fixed-point-build/v1", "status": "PASS",
        "created_utc": f"2026-09-06T{hour}:00:04Z",
        "source": {"commit": "a" * 40, "tree": "b" * 40},
        "builder": {"path": "tools/build_fixed_point.py", "sha256": "1" * 64},
        "composition": composition, "environment": {"source_date_epoch": "1785270512"},
        "build": {"machine_wide_tex_mutex": mutex(hour, abandoned), "chapter_count": 35,
                  "stems": ["schemes", "descent"], "global_fixed_point_sweep": 4,
                  "worktree_kind": "linked", "primary_worktree_override": False},
        "artifacts": [{"stem": "schemes", "pages": 108, "bytes": 100, "sha256": "2" * 64}],
        "pdfs_committed": False,
        "source_checkpoint": {
            "schema": "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-successor/v1",
            "status": "PASS_SOURCE_CHECKPOINT_SUCCESSOR",
            "post_content": {"head_commit": "a" * 40, "head_tree": "b" * 40},
            "protected_input_count": 2,
            "protected_input_roles": {"historical_checkpoint_input": 1, "successor_current_input": 1},
            "protected_input_tuple_sha256": "3" * 64,
            "canonical_composition": {"path": composition["receipt"],
                                      "git_blob": composition["receipt_git_blob"],
                                      "sha256": composition["receipt_sha256"],
                                      "composition_source_commit": composition["composition_source_commit"]},
            "semantic_successor": {"source_unit": "ega:I.6.6.5", "checker": {"errors": []}},
        },
    }


class ReproductionTests(unittest.TestCase):
    def setUp(self):
        self.first = receipt()
        self.second = receipt(11, abandoned=True)

    def compare(self):
        comparator.compare_receipts(self.first, self.second)

    def test_valid_timing_and_abandoned_acquisition_changes_pass_without_mutation(self):
        before = copy.deepcopy((self.first, self.second))
        self.compare()
        self.assertEqual((self.first, self.second), before)

    def test_every_bound_top_level_key_is_required(self):
        for key in comparator.IDENTICAL_KEYS:
            with self.subTest(key=key):
                broken = copy.deepcopy(self.second)
                del broken[key]
                with self.assertRaisesRegex(ValueError, "lacks bound state"):
                    comparator.compare_receipts(self.first, broken)

    def test_both_missing_checkpoint_is_not_treated_as_equal(self):
        del self.first["source_checkpoint"]
        del self.second["source_checkpoint"]
        with self.assertRaisesRegex(ValueError, "source_checkpoint"):
            self.compare()

    def test_malformed_mutex_is_rejected_before_normalization(self):
        mutations = [
            ("status", "FAIL"), ("name", "Local\\wrong"),
            ("acquisition_timeout_ms", validator.TEX_MUTEX_TIMEOUT_MS + 1),
            ("ownership_acquired", 1), ("release_result", "not_released"),
            ("wait_result_code", "0x00000102"), ("abandoned_mutex_recovered", False),
            ("released_utc", "2026-09-06T09:00:00Z"),
            ("wait_duration_ms", float("nan")), ("held_duration_ms", -1),
            ("held_scope", "one pass only"), ("extra_process_id", 999),
        ]
        for key, value in mutations:
            with self.subTest(key=key):
                broken = copy.deepcopy(self.second)
                broken["build"]["machine_wide_tex_mutex"][key] = value
                with mock.patch.object(comparator, "normalize_build_for_reproducibility") as normalize:
                    with self.assertRaisesRegex(ValueError, "mutex"):
                        comparator.compare_receipts(self.first, broken)
                    normalize.assert_not_called()

    def test_missing_mutex_and_identically_invalid_mutex_fail(self):
        for value in (None, {}, "PASS"):
            with self.subTest(value=value):
                for item in (self.first, self.second):
                    item["build"]["machine_wide_tex_mutex"] = value
                with self.assertRaisesRegex(ValueError, "mutex"):
                    self.compare()

    def test_checkpoint_omission_and_invalid_contract_fail(self):
        for value in (None, {}, {"schema": "invented", "status": "PASS"}):
            with self.subTest(value=value):
                self.second["source_checkpoint"] = value
                with self.assertRaisesRegex(ValueError, "source_checkpoint"):
                    self.compare()

    def test_checkpoint_protected_input_hash_drift_fails(self):
        self.second["source_checkpoint"]["protected_input_tuple_sha256"] = "4" * 64
        with self.assertRaisesRegex(ValueError, "source_checkpoint"):
            self.compare()

    def test_checkpoint_protected_count_and_roles_are_not_optional(self):
        for key, value in (("protected_input_count", True), ("protected_input_count", 3),
                           ("protected_input_roles", {}), ("protected_input_tuple_sha256", "bad")):
            with self.subTest(key=key):
                broken = copy.deepcopy(self.second)
                broken["source_checkpoint"][key] = value
                with self.assertRaisesRegex(ValueError, "protected-input inventory"):
                    comparator.compare_receipts(self.first, broken)

    def test_checkpoint_semantic_evidence_is_exact(self):
        self.second["source_checkpoint"]["semantic_successor"]["source_unit"] = "ega:I.6.6.6"
        with self.assertRaisesRegex(ValueError, "source_checkpoint"):
            self.compare()

    def test_source_and_checkpoint_must_bind_one_another(self):
        self.second["source"]["commit"] = "5" * 40
        with self.assertRaisesRegex(ValueError, "build source"):
            self.compare()

    def test_registry_profile_environment_and_builder_drift_fail(self):
        for key, subkey, value in (
            ("composition", "registry_cutoff_commit", "6" * 40),
            ("build", "stems", ["schemes"]), ("build", "chapter_count", 34),
            ("build", "global_fixed_point_sweep", 5),
            ("environment", "source_date_epoch", "0"),
            ("builder", "sha256", "7" * 64),
        ):
            with self.subTest(key=key, subkey=subkey):
                broken = copy.deepcopy(self.second)
                broken[key][subkey] = value
                with self.assertRaisesRegex(ValueError, "differ in bound state"):
                    comparator.compare_receipts(self.first, broken)

    def test_checkpoint_canonical_composition_drift_fails(self):
        self.second["source_checkpoint"]["canonical_composition"]["sha256"] = "8" * 64
        with self.assertRaisesRegex(ValueError, "composition binding"):
            self.compare()

    def test_source_and_checkpoint_changed_together_still_fail_cross_run(self):
        self.second["source"]["commit"] = "9" * 40
        self.second["source_checkpoint"]["post_content"]["head_commit"] = "9" * 40
        with self.assertRaisesRegex(ValueError, "differ in bound state"):
            self.compare()

    def test_bool_int_substitution_is_not_exact_json_equality(self):
        self.first["source_checkpoint"]["semantic_successor"]["checked"] = True
        self.second["source_checkpoint"]["semantic_successor"]["checked"] = 1
        with self.assertRaisesRegex(ValueError, "source_checkpoint"):
            self.compare()

    def test_same_invocation_rejected(self):
        self.second["created_utc"] = self.first["created_utc"]
        with self.assertRaisesRegex(ValueError, "distinct invocations"):
            self.compare()

    def test_duplicate_json_key_rejected_before_validation(self):
        raw = b'{"status":"FAIL",' + json.dumps(self.first).encode()[1:]
        path = mock.Mock()
        path.read_bytes.return_value = raw
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            comparator.load_receipt(path)

    def test_nonfinite_json_constant_rejected_before_validation(self):
        raw = b'{"unused":NaN,' + json.dumps(self.first).encode()[1:]
        path = mock.Mock()
        path.read_bytes.return_value = raw
        with self.assertRaisesRegex(ValueError, "non-finite JSON constant"):
            comparator.load_receipt(path)


if __name__ == "__main__":
    unittest.main()
