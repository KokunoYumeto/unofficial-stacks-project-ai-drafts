"""Receipt-only correction/repro tests. No TeX, Git, network, or source writes.

Set DIRECT_SUCCESSOR_TEST_TOOLS to an existing dependency tools directory when
running the staged comparator before its production integration.
"""
from copy import deepcopy
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

STAGED_TOOLS = Path(__file__).resolve().parents[1]
if os.environ.get("DIRECT_SUCCESSOR_TEST_TOOLS"):
    sys.path.insert(0, os.environ["DIRECT_SUCCESSOR_TEST_TOOLS"])
# The sibling loader/checkpoint drafts live one level above staged tools. After
# integration this path is merely the repository root, with tools still first.
sys.path.insert(0, str(STAGED_TOOLS.parent))
sys.path.insert(0, str(STAGED_TOOLS))

import compare_fixed_point_builds as compare
import validate_unified_repository as old


def mutex(second=False):
    minute = "02" if second else "00"
    return {
        "schema": old.TEX_MUTEX_RECEIPT_SCHEMA, "status": "PASS",
        "name": old.TEX_MUTEX_NAME, "namespace": "Windows Global",
        "held_scope": old.TEX_MUTEX_HELD_SCOPE,
        "release_result": "released_in_finally",
        "acquisition_timeout_ms": old.TEX_MUTEX_TIMEOUT_MS,
        "ownership_acquired": True, "wait_result_code": "0x00000000",
        "wait_result": "acquired", "abandoned_mutex_recovered": False,
        "wait_started_utc": f"2026-09-13T10:{minute}:00Z",
        "acquired_utc": f"2026-09-13T10:{minute}:00Z",
        "released_utc": f"2026-09-13T10:{minute}:50Z",
        "wait_duration_ms": 0.0, "held_duration_ms": 50000.0,
    }


def correction_scope():
    return {
        "correction_id": "illusie-I-chain-comparison-localization-20260908",
        "candidate_commit": "4c3647f926f32a0edade647ebb52adce05d24a8e",
        "candidate_tree": "a" * 40,
        "manifest": {
            "path": "validation/direct-successor-r48-illusie-correction-manifest-2026-09-13.json", "bytes": 1024,
            "sha256": "B" * 64, "git_blob": "b" * 40,
        },
        "corrected_source_commit": "ea606e202707d215f38e050be2621d0c83cadef0",
        "corrected_source_tree": "c" * 40,
        "sealed_predecessor_commit": "1c7fa79a3d8fdb24a9ec45ba65e65ce1fd8867c2",
        "sealed_predecessor_receipt_sha256": "546206C486E7722D9086B9E4ADF979CCA11DC8587D3E28CCFEA551C700606ADE",
    }


def fixture(correction=True):
    composition = {
        "schema": "unofficial-ai-integrated-stacks-direct-composition/v1",
        "receipt": "validation/composition-current.json",
        "receipt_git_blob": "e" * 40, "receipt_sha256": "E" * 64,
        "composition_source_commit": "0" * 40,
        "composition_source_tree": "1" * 40,
        "registry_cutoff_commit": "2" * 40,
    }
    source = {"commit": "3" * 40, "tree": "4" * 40}
    checkpoint = {
        "schema": "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-direct-successor/v1",
        "status": "PASS_SOURCE_CHECKPOINT_DIRECT_SUCCESSOR",
        "post_content": {"head_commit": source["commit"], "head_tree": source["tree"]},
        "protected_input_count": 2,
        "protected_input_roles": {"historical_checkpoint_input": 1, "successor_current_input": 1},
        "protected_input_tuple_sha256": "F" * 64,
        "historical_anchor": {"commit": "5" * 40, "verification": {"status": "PASS"}},
        "semantic_successor": {"commit": "6" * 40, "validated_at_own_head": True, "fresh_import_cache": True},
        "current_ega_successor": {
            "schema": "unofficial-stacks-project-ai-drafts-historical-current-ega-join/v1",
            "status": "PASS_CURRENT_PUBLIC_EGA_PRESERVED", "current_commit": source["commit"],
            "counts": {"decisions": 289},
        },
    }
    if correction:
        scope = correction_scope()
        composition.update(
            schema=compare.AI_CORRECTION_SCHEMA,
            composition_source_commit=scope["corrected_source_commit"],
            composition_source_tree=scope["corrected_source_tree"],
            ai_source_correction_scope=scope,
        )
        checkpoint.update(
            schema=compare.AI_CORRECTION_CHECKPOINT_SCHEMA,
            status=compare.AI_CORRECTION_CHECKPOINT_STATUS,
            ai_source_correction=deepcopy(scope),
            current_illusie_successor={
                "schema": "unofficial-stacks-project-ai-drafts-current-illusie-correction-binding/v1",
                "status": "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND",
                "current_commit": source["commit"],
                "composition_source_commit": scope["corrected_source_commit"],
                "composition_source_tree": scope["corrected_source_tree"],
                "scope": deepcopy(scope),
                "review": {"path": "validation/illusie-review.json", "bytes": 123,
                           "sha256": "C" * 64, "git_blob": "c" * 40},
                "checker": {"path": "illusie_volume_I/verify.py", "bytes": 124,
                            "sha256": "D" * 64, "git_blob": "d" * 40},
                "checker_result": {"status": "PASS", "current_source_sha256": "E" * 64, "units": 7},
                "regression_tests": {"status": "PASS", "tests_run": 5,
                                     "modules": ["illusie_volume_I.test_composition", "illusie_volume_I.test_ez"]},
            },
        )
        refs = [scope["manifest"], checkpoint["current_illusie_successor"]["review"],
                checkpoint["current_illusie_successor"]["checker"]]
        composition["correction_protected_inputs"] = {
            ref["path"]: {key: ref[key] for key in ("bytes", "sha256", "git_blob")} for ref in refs
        }
        composition["correction_protected_inputs"].update({
            "simplicial.tex": {"bytes": 999, "sha256": "E" * 64, "git_blob": "e" * 40},
            "validation/direct-successor-r48-composition.json": {
                "bytes": 147071, "sha256": scope["sealed_predecessor_receipt_sha256"], "git_blob": "f" * 40,
            },
            "illusie_volume_I/check.py": {"bytes": 12, "sha256": "A" * 64, "git_blob": "a" * 40},
        })
    checkpoint["canonical_composition"] = {
        "path": composition["receipt"], "git_blob": composition["receipt_git_blob"],
        "sha256": composition["receipt_sha256"],
        "composition_source_commit": composition["composition_source_commit"],
    }
    first = {
        "schema": "unofficial-ai-integrated-stacks-fixed-point-build/v1", "status": "PASS",
        "created_utc": "2026-09-13T10:00:51Z", "source": source,
        "builder": {"path": "tools/build_fixed_point.py", "git_blob": "7" * 40, "sha256": "7" * 64},
        "composition": composition, "environment": {"fixture": True},
        "build": {"global_fixed_point_sweep": 4, "worktree_kind": "linked", "machine_wide_tex_mutex": mutex()},
        "artifacts": [{"stem": "simplicial", "pages": 78, "bytes": 1024, "sha256": "8" * 64}],
        "pdfs_committed": False, "source_checkpoint": checkpoint,
    }
    second = deepcopy(first)
    second["created_utc"] = "2026-09-13T10:02:51Z"
    second["build"]["machine_wide_tex_mutex"] = mutex(True)
    return first, second


class CorrectionReproTests(unittest.TestCase):
    def test_corrected_pair_passes_with_separate_metadata_head(self):
        first, second = fixture()
        self.assertNotEqual(first["source"]["commit"], first["composition"]["composition_source_commit"])
        compare.compare_receipts(first, second)

    def test_all_historical_checkpoint_contracts_still_pass(self):
        for schema, status in compare.SOURCE_CHECKPOINT_CONTRACTS.items():
            if schema == compare.AI_CORRECTION_CHECKPOINT_SCHEMA:
                continue
            with self.subTest(schema=schema):
                first, second = fixture(False)
                for receipt in (first, second):
                    receipt["source_checkpoint"].update(schema=schema, status=status)
                compare.compare_receipts(first, second)

    def test_old_r48_checkpoint_rejected_under_corrected_composition(self):
        first, second = fixture()
        for receipt in (first, second):
            receipt["source_checkpoint"].update(
                schema="unofficial-stacks-project-ai-drafts-ega-source-checkpoint-direct-successor/v1",
                status="PASS_SOURCE_CHECKPOINT_DIRECT_SUCCESSOR",
            )
        with self.assertRaisesRegex(ValueError, "requires a corrected source_checkpoint"):
            compare.compare_receipts(first, second)

    def test_corrected_checkpoint_rejected_under_old_composition(self):
        first, second = fixture()
        for receipt in (first, second):
            receipt["composition"]["schema"] = "unofficial-ai-integrated-stacks-direct-composition/v1"
        with self.assertRaisesRegex(ValueError, "requires typed correction composition"):
            compare.compare_receipts(first, second)

    def test_missing_scope_rejected_even_when_both_runs_omit_it(self):
        first, second = fixture()
        for receipt in (first, second):
            del receipt["composition"]["ai_source_correction_scope"]
            del receipt["source_checkpoint"]["ai_source_correction"]
        with self.assertRaises(ValueError):
            compare.compare_receipts(first, second)

    def test_empty_scope_rejected(self):
        first, second = fixture()
        for receipt in (first, second):
            receipt["composition"]["ai_source_correction_scope"] = {}
            receipt["source_checkpoint"]["ai_source_correction"] = {}
        with self.assertRaises(ValueError):
            compare.compare_receipts(first, second)

    def test_checkpoint_scope_mismatch_rejected(self):
        first, second = fixture()
        first["source_checkpoint"]["ai_source_correction"]["candidate_tree"] = "f" * 40
        with self.assertRaisesRegex(ValueError, "correction identity mismatch"):
            compare.compare_receipts(first, second)

    def test_scope_json_numeric_types_are_not_coerced(self):
        first, second = fixture()
        first["source_checkpoint"]["ai_source_correction"]["manifest"]["bytes"] = 1024.0
        with self.assertRaisesRegex(ValueError, "correction identity mismatch"):
            compare.compare_receipts(first, second)

    def test_scope_corrected_commit_must_equal_composition_endpoint(self):
        first, second = fixture()
        for receipt in (first, second):
            receipt["composition"]["composition_source_commit"] = "9" * 40
            receipt["source_checkpoint"]["canonical_composition"]["composition_source_commit"] = "9" * 40
        with self.assertRaises(ValueError):
            compare.compare_receipts(first, second)

    def test_scope_corrected_tree_must_equal_composition_endpoint(self):
        first, second = fixture()
        for receipt in (first, second):
            receipt["composition"]["composition_source_tree"] = "9" * 40
        with self.assertRaises(ValueError):
            compare.compare_receipts(first, second)

    def test_missing_endpoint_rejected_without_optional_helper_bypass(self):
        for key in ("composition_source_commit", "composition_source_tree"):
            first, second = fixture()
            for receipt in (first, second):
                del receipt["composition"][key]
            with self.subTest(key=key), self.assertRaises(ValueError):
                compare.compare_receipts(first, second)

    def test_old_v1_cannot_carry_untyped_correction_scope(self):
        for location, key in (("composition", "ai_source_correction_scope"),
                              ("source_checkpoint", "ai_source_correction")):
            first, second = fixture(False)
            for receipt in (first, second):
                receipt[location][key] = None
            with self.subTest(location=location), self.assertRaises(ValueError):
                compare.compare_receipts(first, second)

    def test_new_checkpoint_status_must_pass(self):
        first, second = fixture()
        first["source_checkpoint"]["status"] = "PASS_SOURCE_CHECKPOINT_DIRECT_SUCCESSOR"
        with self.assertRaisesRegex(ValueError, "unsupported or nonpassing"):
            compare.compare_receipts(first, second)

    def test_build_source_cannot_be_rebound_to_old_revision(self):
        first, second = fixture()
        first["source"]["commit"] = "1c7fa79a3d8fdb24a9ec45ba65e65ce1fd8867c2"
        with self.assertRaisesRegex(ValueError, "does not bind its build source"):
            compare.compare_receipts(first, second)

    def test_composition_hash_cannot_drift_from_checkpoint(self):
        first, second = fixture()
        first["composition"]["receipt_sha256"] = "A" * 64
        with self.assertRaisesRegex(ValueError, "composition binding mismatch"):
            compare.compare_receipts(first, second)

    def test_exact_historical_ega_current_ega_and_correction_inputs_preserved(self):
        mutations = (
            lambda r: r["source_checkpoint"]["historical_anchor"].update(commit="0" * 40),
            lambda r: r["source_checkpoint"]["semantic_successor"].update(commit="0" * 40),
            lambda r: r["source_checkpoint"]["current_ega_successor"]["counts"].update(decisions=290),
            lambda r: r["composition"]["correction_protected_inputs"]["illusie_volume_I/check.py"].update(sha256="B" * 64),
        )
        for number, mutate in enumerate(mutations):
            first, second = fixture()
            mutate(second)
            with self.subTest(number=number), self.assertRaisesRegex(ValueError, "differ in bound state"):
                compare.compare_receipts(first, second)

    def test_correction_identity_changes_cannot_hide_across_both_fields(self):
        first, second = fixture()
        for location, key in (("composition", "ai_source_correction_scope"),
                              ("source_checkpoint", "ai_source_correction")):
            second[location][key]["manifest"]["sha256"] = "C" * 64
        second["source_checkpoint"]["current_illusie_successor"]["scope"]["manifest"]["sha256"] = "C" * 64
        second["composition"]["correction_protected_inputs"][correction_scope()["manifest"]["path"]]["sha256"] = "C" * 64
        with self.assertRaisesRegex(ValueError, "differ in bound state"):
            compare.compare_receipts(first, second)

    def test_protected_inventory_count_uses_exact_integer_type(self):
        first, second = fixture()
        first["source_checkpoint"]["protected_input_count"] = 2.0
        with self.assertRaisesRegex(ValueError, "exact protected-input inventory"):
            compare.compare_receipts(first, second)

    def test_mutex_is_validated_before_volatile_fields_discarded(self):
        first, second = fixture()
        second["build"]["machine_wide_tex_mutex"]["ownership_acquired"] = False
        with self.assertRaisesRegex(ValueError, "ownership_acquired"):
            compare.compare_receipts(first, second)

    def test_distinct_invocations_required(self):
        first, second = fixture()
        second["created_utc"] = first["created_utc"]
        with self.assertRaisesRegex(ValueError, "distinct invocations"):
            compare.compare_receipts(first, second)

    def test_both_runs_cannot_omit_semantic_evidence(self):
        for key in ("historical_anchor", "semantic_successor", "current_ega_successor", "current_illusie_successor"):
            first, second = fixture()
            for receipt in (first, second):
                del receipt["source_checkpoint"][key]
            with self.subTest(key=key), self.assertRaises(ValueError):
                compare.compare_receipts(first, second)

    def test_current_ega_replay_must_bind_actual_build_head(self):
        first, second = fixture()
        first["source_checkpoint"]["current_ega_successor"]["current_commit"] = "1" * 40
        with self.assertRaisesRegex(ValueError, "historical/current EGA"):
            compare.compare_receipts(first, second)

    def test_current_illusie_replay_must_bind_actual_build_head(self):
        first, second = fixture()
        first["source_checkpoint"]["current_illusie_successor"]["current_commit"] = "1" * 40
        with self.assertRaisesRegex(ValueError, "exact current Illusie"):
            compare.compare_receipts(first, second)

    def test_current_illusie_review_reference_must_be_exact(self):
        for key, value in (("sha256", "bad"), ("bytes", True), ("path", "../private.json")):
            first, second = fixture()
            first["source_checkpoint"]["current_illusie_successor"]["review"][key] = value
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "exact current Illusie"):
                compare.compare_receipts(first, second)

    def test_current_illusie_checker_must_pass(self):
        first, second = fixture()
        first["source_checkpoint"]["current_illusie_successor"]["checker_result"]["status"] = "FAIL"
        with self.assertRaisesRegex(ValueError, "checker result"):
            compare.compare_receipts(first, second)

    def test_current_illusie_regressions_must_be_complete(self):
        for key, value in (("tests_run", 4), ("tests_run", 5.0), ("modules", ["illusie_volume_I.test_ez"]), ("status", "FAIL")):
            first, second = fixture()
            first["source_checkpoint"]["current_illusie_successor"]["regression_tests"][key] = value
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "regression evidence"):
                compare.compare_receipts(first, second)

    def test_current_illusie_full_checker_result_compared_without_dropping_counts(self):
        first, second = fixture()
        second["source_checkpoint"]["current_illusie_successor"]["checker_result"]["units"] = 8
        with self.assertRaisesRegex(ValueError, "differ in bound state: source_checkpoint"):
            compare.compare_receipts(first, second)

    def test_current_illusie_evidence_requires_protected_inventory(self):
        first, second = fixture()
        for receipt in (first, second):
            del receipt["composition"]["correction_protected_inputs"]
        with self.assertRaisesRegex(ValueError, "protected-input identities"):
            compare.compare_receipts(first, second)

    def test_semantic_reference_cannot_disagree_with_protected_inventory(self):
        for key in ("review", "checker"):
            first, second = fixture()
            reference = first["source_checkpoint"]["current_illusie_successor"][key]
            first["composition"]["correction_protected_inputs"][reference["path"]]["sha256"] = "9" * 64
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "not correction-input bound"):
                compare.compare_receipts(first, second)

    def test_checker_source_sha_must_be_bound_to_corrected_simplicial(self):
        first, second = fixture()
        first["source_checkpoint"]["current_illusie_successor"]["checker_result"]["current_source_sha256"] = "9" * 64
        with self.assertRaisesRegex(ValueError, "source or sealed predecessor digest"):
            compare.compare_receipts(first, second)

    def run_cli(self, correction):
        first, second = fixture(correction)
        with tempfile.TemporaryDirectory(prefix="correction-repro-test-") as tmp:
            root = Path(tmp)
            paths = [root / name for name in ("first.json", "second.json", "out.json")]
            for path, document in zip(paths, (first, second)):
                path.write_text(json.dumps(document), encoding="utf-8")
            argv = ["compare_fixed_point_builds.py", "--first", str(paths[0]), "--second", str(paths[1]),
                    "--first-logical-path", "validation/fresh-a.json", "--second-logical-path", "validation/fresh-b.json",
                    "--admitted-errata", "R1-R48", "--output", str(paths[2])]
            with patch.object(sys, "argv", argv), redirect_stdout(io.StringIO()):
                self.assertEqual(compare.main(), 0)
            result = json.loads(paths[2].read_text(encoding="utf-8"))
            with patch.object(sys, "argv", argv), self.assertRaises(FileExistsError):
                compare.main()
            return result, first

    def test_repro_scope_copies_exact_correction_identity(self):
        result, first = self.run_cli(True)
        self.assertEqual(compare.canonical_json(result["scope"]["ai_source_correction"]),
                         compare.canonical_json(first["composition"]["ai_source_correction_scope"]))
        self.assertEqual(result["scope"]["admitted_errata"], "R1-R48")
        self.assertEqual(result["source"], first["source"])
        self.assertEqual(result["comparison"]["source_checkpoint_identity_equal"], True)

    def test_historical_repro_scope_remains_exact_old_six_keys(self):
        result, _ = self.run_cli(False)
        self.assertEqual(set(result["scope"]), {
            "admitted_errata", "registry_cutoff_commit", "source_commit", "source_tree",
            "composition_receipt", "composition_receipt_sha256",
        })


if __name__ == "__main__":
    unittest.main()
