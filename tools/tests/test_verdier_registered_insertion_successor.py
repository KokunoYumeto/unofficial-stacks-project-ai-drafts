"""Focused non-TeX tests for the Verdier registered-insertion successor."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import build_fixed_point as build
import compare_fixed_point_builds as compare
import compose_registered_insertion as composer
import direct_successor_checkpoint as checkpoint
import validate_verdier_registered_insertion_successor as release
import verdier_registered_insertion_successor as verdier


ROOT = Path(__file__).resolve().parents[2]


def ident(path: str = "fixture") -> dict[str, object]:
    return {"path": path, "bytes": 1, "sha256": "A" * 64, "git_blob": "a" * 40}


class ExactPublicPrefixTests(unittest.TestCase):
    """Exercise the real immutable prefix only; no build, write, or network."""

    def test_inherited_verdier_receipt_and_fixed_prefix(self):
        git = verdier.Git(ROOT)
        previous, protected = verdier._validate_inherited(git)
        rows, issue = verdier._validate_fixed_prefix(git)
        self.assertEqual(previous["schema"], verdier.SCHEMA)
        self.assertEqual(tuple(previous["required_build_stems"]), verdier.EXPECTED_STEMS)
        self.assertIn("simplicial.tex", protected)
        self.assertEqual([row["kind"] for row in rows], [
            "lease_issue", "candidate_authoring", "failed_closed_build_root_repair",
            "candidate_build_and_visual_validation",
        ])
        self.assertEqual({row["path"] for row in rows[0]["paths"]}, {verdier.LEASES})
        for row in rows[1:]:
            self.assertTrue(all(path["path"].startswith(verdier.CANDIDATE_DIR + "/")
                                for path in row["paths"]))
        self.assertEqual(issue["event_id"], verdier.ISSUE_EVENT)
        self.assertNotIn("supersedes_event_id", issue)


class PureContractTests(unittest.TestCase):
    def test_composer_counts_exact_label_declarations_not_references(self):
        label = "lemma-nested-quotients"
        payload = (
            "\\label{lemma-nested-quotients}\n"
            "See Lemma \\ref{lemma-nested-quotients}.\n"
        ).encode("utf-8")
        declaration = composer.label_declaration_bytes(label)
        self.assertEqual(payload.count(declaration), 1)
        self.assertEqual(payload.count(label.encode("utf-8")), 2)

    def test_manifest_closure_repair_is_two_dotfiles_only(self):
        correction = json.loads((ROOT / verdier.CLOSURE_CORRECTION_RECEIPT).read_text(
            encoding="utf-8"))
        self.assertEqual(correction["status"],
                         "PASS_MANIFEST_GIT_OBJECT_CLOSURE_CORRECTED")
        self.assertEqual(
            {Path(row["path"]).name
             for row in correction["closure_correction"]["added_paths"]},
            {".gitattributes", ".gitignore"},
        )
        self.assertEqual(correction["closure_correction"]["candidate_subtree"],
                         verdier.FINAL_CANDIDATE_SUBTREE)
        self.assertEqual(set(verdier.FINAL_VALIDATOR_PATHS), {
            verdier.CLOSURE_CORRECTION_RECEIPT,
            "tools/verdier_registered_insertion_successor.py",
            "tools/tests/test_verdier_registered_insertion_successor.py",
        })
        self.assertEqual(set(verdier.COMPOSER_REPAIR_PATHS), {
            "tools/compose_registered_insertion.py",
            "tools/verdier_registered_insertion_successor.py",
            "tools/tests/test_verdier_registered_insertion_successor.py",
        })

    def test_append_one_rejects_header_mutation(self):
        before = {"schema": "x", "events": [{"event_id": "one"}]}
        after = {"schema": "y", "events": [{"event_id": "one"}, {"event_id": "two"}]}
        with self.assertRaisesRegex(ValueError, "header changed"):
            verdier._append_one(before, after, "events", "fixture")

    def test_append_one_returns_only_new_row(self):
        before = {"schema": "x", "events": [{"event_id": "one"}]}
        new = {"event_id": "two"}
        after = {"schema": "x", "events": [*before["events"], new]}
        self.assertEqual(verdier._append_one(before, after, "events", "fixture"), new)

    def test_review_binds_authority_source_units(self):
        review = {
            "schema": "mathematics-commons-stacks-independent-review/v1",
            "candidate_id": verdier.OVERLAY_ID,
            "status": "PASS",
            "passed": True,
            "review_state": "performed",
            "independent_replay": "passed",
            "unresolved_defects": [],
            "authority": {"source_units": [{"unit_id": value} for value in verdier.STABLE_IDS]},
        }
        verdier._validate_review(review, "replay/independent-review.json")
        review["authority"]["source_units"].pop()
        with self.assertRaisesRegex(ValueError, "stable-ID"):
            verdier._validate_review(review, "replay/independent-review.json")

    def test_binding_normalization_has_build_contract(self):
        receipt = {
            "registry": {
                "cutoff_commit": "1" * 40, "cutoff_tree": "2" * 40,
                "registered_overlays": 60, "registered_stable_ids": 1683,
                "last_admitted_overlay": verdier.OVERLAY_ID,
                "overlays_path": verdier.OVERLAYS, "overlays_git_blob": "3" * 40,
                "overlays_sha256": "B" * 64,
                "leases_path": verdier.LEASES, "leases_git_blob": "4" * 40,
                "leases_sha256": "C" * 64,
            },
            "composition": {
                "mode": verdier.MODE, "base_commit": "1" * 40, "base_tree": "2" * 40,
                "source_commit": "5" * 40, "source_tree": "6" * 40,
                "affected_sources": {"derived.tex": {}},
            },
            "previous_cutoff": {
                "public_main_head": verdier.PREVIOUS_PUBLIC,
                "public_main_tree": verdier.PREVIOUS_PUBLIC_TREE,
                "registry_commit": "7" * 40,
                "last_admitted_overlay": "stacks-verdier-a04446e-1-3-6-r1",
                "source_blobs": {"derived.tex": {}}, "receipt": {},
            },
            "new_overlays": [{"candidate_commit": "8" * 40,
                              "lease_issue_commit": verdier.LEASE_ISSUE_COMMIT,
                              "admission_commit": "1" * 40}],
            "transport": {},
            "projection_verifier": {"report": {"status": "PASS"}},
            "inherited_ai_source_correction": {"scope": {"correction_id": "x"},
                                                 "source_commit": "9" * 40,
                                                 "source_tree": "0" * 40,
                                                 "validation_head": "8" * 40,
                                                 "validation_tree": "7" * 40},
            "correction_protected_inputs": {"simplicial.tex": {"bytes": 1,
                "sha256": "A" * 64, "git_blob": "a" * 40}},
            "verdier_registered_insertion_scope": {"candidate_id": verdier.OVERLAY_ID},
        }
        fake_git = Mock()
        fake_git.ident.return_value = {"bytes": 10, "sha256": "D" * 64, "git_blob": "d" * 40}
        with patch.object(verdier, "protected_tools", return_value={"tools/x.py": {
                "bytes": 1, "sha256": "A" * 64, "git_blob": "a" * 40}}):
            binding = verdier.normalize_binding(fake_git, "f" * 40, receipt)
        self.assertEqual(binding["schema"], verdier.SCHEMA)
        self.assertEqual(binding["required_build_stems"], list(verdier.EXPECTED_STEMS))
        self.assertEqual(binding["affected_source_stems"], ["derived"])
        self.assertEqual(binding["new_overlay_ids"], [verdier.OVERLAY_ID])
        self.assertEqual(binding["inherited_ai_source_commit"], "9" * 40)
        self.assertEqual(binding["inherited_ai_validation_head"], "8" * 40)
        self.assertEqual(binding["inherited_ai_validation_tree"], "7" * 40)


class ConsumerDispatchTests(unittest.TestCase):
    def test_repro_comparator_accepts_exact_verdier_ega_inheritance_status(self):
        scope = {
            "corrected_source_commit": "a" * 40,
            "corrected_source_tree": "b" * 40,
            "manifest": ident("validation/manifest.json"),
            "sealed_predecessor_receipt_sha256": "A" * 64,
        }
        review = ident("validation/review.json")
        checker = ident("illusie_volume_I/verify.py")
        current_source_sha256 = "A" * 64
        protected = {
            row["path"]: {key: row[key] for key in ("bytes", "sha256", "git_blob")}
            for row in (scope["manifest"], review, checker)
        }
        protected.update({
            "validation/direct-successor-r48-composition.json": {
                "bytes": 1, "sha256": "A" * 64, "git_blob": "a" * 40,
            },
            "simplicial.tex": {
                "bytes": 1, "sha256": current_source_sha256, "git_blob": "a" * 40,
            },
        })
        receipt = {
            "source": {"commit": "c" * 40},
            "composition": {
                "schema": compare.VERDIER_REGISTERED_INSERTION_SCHEMA,
                "inherited_ai_validation_head": "d" * 40,
                "correction_protected_inputs": protected,
            },
            "source_checkpoint": {
                "historical_anchor": {"status": "PASS"},
                "semantic_successor": {
                    "validated_at_own_head": True, "fresh_import_cache": True,
                },
                "current_ega_successor": {
                    "schema": "unofficial-stacks-project-ai-drafts-historical-current-ega-join/v1",
                    "status": compare.VERDIER_EGA_INHERITED_STATUS,
                    "current_commit": "c" * 40,
                },
                "current_illusie_successor": {
                    "schema": "unofficial-stacks-project-ai-drafts-current-illusie-correction-binding/v1",
                    "status": "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND",
                    "current_commit": "c" * 40,
                    "composition_source_commit": "a" * 40,
                    "composition_source_tree": "b" * 40,
                    "scope": scope,
                    "review": review,
                    "checker": checker,
                    "checker_result": {
                        "status": "PASS", "current_source_sha256": current_source_sha256,
                    },
                    "manifest_validation_revision": "d" * 40,
                    "regression_tests": {
                        "status": "PASS", "tests_run": 5,
                        "modules": ["illusie_volume_I.test_composition", "illusie_volume_I.test_ez"],
                    },
                },
            },
        }
        compare.validate_correction_semantics(receipt, scope, "fixture")
        receipt["source_checkpoint"]["current_illusie_successor"][
            "manifest_validation_revision"
        ] = "e" * 40
        with self.assertRaisesRegex(ValueError, "exact current Illusie binding"):
            compare.validate_correction_semantics(receipt, scope, "fixture")
        receipt["source_checkpoint"]["current_illusie_successor"][
            "manifest_validation_revision"
        ] = "d" * 40
        receipt["composition"]["schema"] = compare.AI_CORRECTION_SCHEMA
        with self.assertRaisesRegex(ValueError, "preserved historical/current EGA semantics"):
            compare.validate_correction_semantics(receipt, scope, "fixture")

    def test_repro_comparator_uses_inherited_ai_endpoint_for_verdier_wrapper(self):
        scope = {"correction_id": "fixture"}
        receipt = {
            "composition": {
                "schema": compare.VERDIER_REGISTERED_INSERTION_SCHEMA,
                "inherited_ai_source_commit": "a" * 40,
                "inherited_ai_source_tree": "b" * 40,
                "composition_source_commit": "c" * 40,
                "composition_source_tree": "d" * 40,
                "ai_source_correction_scope": scope,
            },
            "source_checkpoint": {
                "schema": compare.AI_CORRECTION_CHECKPOINT_SCHEMA,
                "status": compare.AI_CORRECTION_CHECKPOINT_STATUS,
                "ai_source_correction": scope,
            },
        }
        with patch("ai_source_correction_composition.validate_ai_source_correction_scope") \
                as validate_scope, \
             patch.object(compare, "validate_correction_semantics") as validate_semantics:
            self.assertIs(compare.ai_source_correction_scope(receipt, "fixture"), scope)
        validate_scope.assert_called_once_with(
            scope, source_commit="a" * 40, source_tree="b" * 40)
        validate_semantics.assert_called_once_with(receipt, scope, "fixture")

    def test_repro_comparator_requires_exact_inherited_ai_endpoint(self):
        scope = {"correction_id": "fixture"}
        receipt = {
            "composition": {
                "schema": compare.VERDIER_REGISTERED_INSERTION_SCHEMA,
                "inherited_ai_source_commit": "a" * 40,
                "ai_source_correction_scope": scope,
            },
            "source_checkpoint": {
                "schema": compare.AI_CORRECTION_CHECKPOINT_SCHEMA,
                "status": compare.AI_CORRECTION_CHECKPOINT_STATUS,
                "ai_source_correction": scope,
            },
        }
        with self.assertRaisesRegex(ValueError, "exact corrected composition source"):
            compare.ai_source_correction_scope(receipt, "fixture")

    def test_build_loader_dispatches_new_schema(self):
        expected = ({"schema": verdier.SCHEMA}, verdier.EXPECTED_STEMS, ("derived",))
        fake = SimpleNamespace(load_verdier_registered_insertion_successor=Mock(return_value=expected))
        with tempfile.TemporaryDirectory(prefix="verdier-dispatch-") as temporary:
            root = Path(temporary)
            target = root / verdier.RECEIPT
            target.parent.mkdir(parents=True)
            target.write_text(json.dumps({"schema": verdier.SCHEMA}), encoding="utf-8")
            with patch.dict(sys.modules, {"verdier_registered_insertion_successor": fake}), \
                 patch.object(build, "require_clean_path"), \
                 patch.object(build, "git", return_value="a" * 40):
                observed = build.load_composition_receipt(root, Path(verdier.RECEIPT))
        self.assertEqual(observed, expected)
        fake.load_verdier_registered_insertion_successor.assert_called_once()

    def test_recheck_dispatches_new_schema(self):
        calls: list[tuple] = []
        fake = SimpleNamespace(recheck_verdier_successor_tools=lambda *args: calls.append(args))
        binding = {"schema": verdier.SCHEMA}
        with patch.dict(sys.modules, {"verdier_registered_insertion_successor": fake}):
            build.require_direct_tools_unchanged(Path("fixture"), binding)
        self.assertEqual(calls, [(Path("fixture"), binding)])

    def test_index_scope_carries_both_inherited_and_new_scopes(self):
        binding = {
            "composition_source_commit": "a" * 40,
            "registry_cutoff_commit": "b" * 40,
            "new_overlay_ids": [verdier.OVERLAY_ID],
            "ai_source_correction_scope": {"correction_id": "old"},
            "verdier_registered_insertion_scope": {"candidate_id": verdier.OVERLAY_ID},
        }
        self.assertEqual(release._index_scope(binding), {
            "source_commit": "a" * 40,
            "registry_cutoff_commit": "b" * 40,
            "new_overlay_ids": [verdier.OVERLAY_ID],
            "ai_source_correction": {"correction_id": "old"},
            "verdier_registered_insertion": {"candidate_id": verdier.OVERLAY_ID},
        })

    def test_full_profile_is_mandatory(self):
        binding = {"ai_source_correction_scope": {}}
        receipt = {
            "schema": "unofficial-ai-integrated-stacks-fixed-point-build/v1",
            "status": "PASS",
            "composition": binding,
            "source_checkpoint": {
                "schema": release.AI_CHECKPOINT_SCHEMA,
                "status": release.AI_CHECKPOINT_STATUS,
                "ai_source_correction": {},
                "current_ega_successor": {"status": "PASS_CURRENT_PUBLIC_EGA_PRESERVED"},
                "current_illusie_successor": {"status": "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND"},
            },
            "pdfs_committed": False,
            "build": {
                "strategy": "sequential-prime-bibtex-global-state-sweeps",
                "fixed_point_suffixes": list(release.common.SUFFIXES),
                "stem_selection": "composition_receipt",
                "stems": list(verdier.EXPECTED_STEMS[:-1]),
                "chapter_count": 35,
                "pdfinfo_readable": 35,
                "worktree_kind": "linked",
                "primary_worktree_override": False,
                "global_fixed_point_sweep": 3,
            },
        }
        with self.assertRaisesRegex(ValueError, "36-chapter"):
            release._check_build_shape(receipt, binding, verdier.EXPECTED_STEMS, lambda *args: None)


class CheckpointSchemaTests(unittest.TestCase):
    def setUp(self):
        self.source = Path("fixture-only")
        self.build = Mock()
        self.build.require_commit_object.side_effect = lambda source, value, label: value
        self.build.git.side_effect = lambda source, *args: (
            "schemes.tex\nderived.tex\nsimplicial.tex\nstyle.sty" if args[0] == "ls-tree" else "tree-actual"
        )
        self.build.committed_file_identity.side_effect = lambda source, commit, path: ident(path)
        self.build.working_file_identity.side_effect = lambda source, path: ident(path)
        self.build.committed_regular_files.return_value = []
        self.build.EGA_PRECONTENT_TOOL_ROLES = []
        self.build.EGA_SHARED_BUILD_SUFFIXES = {".sty"}
        self.build.EGA_NON_WORKTREE_PROTECTED_ROLES = {"historical_checkpoint_input"}
        self.build.protected_input.side_effect = lambda role, commit, row: {"role": role, "commit": commit, **row}
        self.build.canonical_tuple_sha256.return_value = "B" * 64
        self.build.parse_json_blob.return_value = {
            "schema": checkpoint.AI_COMPOSITION_SCHEMA,
            "status": "PASS",
            "composition": {"source_commit": "old-ai-source", "base_commit": "old-ai-base"},
        }
        self.composition = {
            "schema": checkpoint.VERDIER_COMPOSITION_SCHEMA,
            "previous_public_main_head": "prior-public",
            "composition_source_commit": "new-derived-source",
            "composition_source_tree": "new-derived-tree",
            "receipt": verdier.RECEIPT,
            "receipt_git_blob": "c" * 40,
            "receipt_sha256": "C" * 64,
            "ai_source_correction_scope": {"correction_id": "old"},
            "inherited_ai_source_commit": "old-ai-source",
            "inherited_ai_source_tree": "old-ai-tree",
            "inherited_ai_validation_head": "old-ai-validation-head",
            "inherited_ai_validation_tree": "old-ai-validation-tree",
            "correction_protected_inputs": {},
            "direct_validation_tools": {},
            "verdier_registered_insertion_scope": {"candidate_id": verdier.OVERLAY_ID},
        }
        self.checkpoint = {"content": {"commit": "old-content"}}

    def test_new_schema_uses_direct_loader_and_accepts_ai_predecessor(self):
        ega = Mock(return_value=(
            {"status": "PASS_CURRENT_PUBLIC_EGA_INHERITED_WITH_LATER_PUBLIC_ERRATA"}, []))
        patches = [
            patch.object(checkpoint, "receipt_anchor", return_value="real-anchor"),
            patch.object(checkpoint, "verify_historical", return_value=(
                {"post_content": {"head_tree": "anchor-tree"}, "external_authority_inputs": []}, ())),
            patch.object(checkpoint, "verify_historical_semantic", return_value=(
                {"commit": "old-semantic"}, [], [])),
            patch.object(checkpoint, "verify_current_ega", ega),
            patch.object(checkpoint, "verify_current_illusie", return_value={
                "status": "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND"}),
            patch.object(checkpoint, "historical_semantic_composition", return_value=(
                {"composition_source_commit": "old-ai-source",
                 "composition_base_commit": "old-ai-base"},
                {"commit": "prior-public", **ident("validation/composition-current.json")})),
        ]
        with patches[0], patches[1], patches[2], patches[3], patches[4], patches[5]:
            binding, _, _ = checkpoint._load_at(
                self.build, self.source, "validation/old-checkpoint.json", self.checkpoint,
                self.composition, "actual-build-commit", live=True)
        self.assertEqual(binding["schema"], checkpoint.SCHEMA_AI)
        self.assertEqual(binding["verdier_registered_insertion"],
                         self.composition["verdier_registered_insertion_scope"])
        self.assertEqual(binding["inherited_composition"]["commit"], "prior-public")
        self.build.require_source_checkpoint_unchanged.assert_called_once()
        ega.assert_called_once_with(
            self.build, self.source, "prior-public", "actual-build-commit",
            replay_current_checker=False)

    def test_semantic_owner_follows_inherited_ai_previous_cutoff(self):
        inherited = {
            "schema": checkpoint.AI_COMPOSITION_SCHEMA,
            "status": "PASS",
            "previous_cutoff": {
                "public_main_head": "semantic-owner",
                "receipt": ident("validation/composition-current.json"),
            },
            "composition": {"source_commit": "later-ai", "base_commit": "later-base"},
        }
        owner = {
            "schema": checkpoint.direct_successor_composition._helper.SCHEMA,
            "status": "PASS",
            "composition": {"source_commit": "semantic-source",
                            "base_commit": "semantic-base"},
        }
        self.build.committed_file_identity.return_value = ident(
            "validation/composition-current.json")
        self.build.require_commit_object.return_value = "semantic-owner"
        self.build.parse_json_blob.return_value = owner
        binding, receipt = checkpoint.historical_semantic_composition(
            self.build, self.source, "prior-public", inherited,
            verdier_successor=True)
        self.assertEqual(binding, {
            "composition_source_commit": "semantic-source",
            "composition_base_commit": "semantic-base",
        })
        self.assertEqual(receipt["commit"], "semantic-owner")
        self.build.require_ancestor.assert_called_once_with(
            self.source, "semantic-owner",
            "historical semantic composition owner to immediate predecessor",
            "prior-public")

    def test_semantic_owner_unwraps_verdier_then_ai(self):
        receipt_ref = ident("validation/composition-current.json")
        inherited = {
            "schema": checkpoint.VERDIER_COMPOSITION_SCHEMA,
            "status": "PASS",
            "previous_cutoff": {
                "public_main_head": "ai-owner",
                "receipt": receipt_ref,
            },
            "composition": {"source_commit": "later-verdier",
                            "base_commit": "later-verdier-base"},
        }
        ai_wrapper = {
            "schema": checkpoint.AI_COMPOSITION_SCHEMA,
            "status": "PASS",
            "previous_cutoff": {
                "public_main_head": "direct-owner",
                "receipt": receipt_ref,
            },
            "composition": {"source_commit": "later-ai", "base_commit": "later-ai-base"},
        }
        direct = {
            "schema": checkpoint.direct_successor_composition._helper.SCHEMA,
            "status": "PASS",
            "composition": {"source_commit": "semantic-source",
                            "base_commit": "semantic-base"},
        }
        self.build.committed_file_identity.return_value = receipt_ref
        self.build.require_commit_object.side_effect = lambda source, value, label: value
        self.build.parse_json_blob.side_effect = [ai_wrapper, direct]
        binding, receipt = checkpoint.historical_semantic_composition(
            self.build, self.source, "prior-public", inherited,
            verdier_successor=True)
        self.assertEqual(binding, {
            "composition_source_commit": "semantic-source",
            "composition_base_commit": "semantic-base",
        })
        self.assertEqual(receipt["commit"], "direct-owner")
        self.assertEqual(self.build.require_ancestor.call_count, 2)

    def test_verdier_surface_compares_current_public_not_historical_anchor(self):
        self.assertEqual(
            checkpoint.historical_surface_comparison_commit(
                self.composition, "historical-anchor"),
            "prior-public",
        )
        ordinary = {"schema": checkpoint.AI_COMPOSITION_SCHEMA,
                    "previous_public_main_head": "prior-public"}
        self.assertEqual(
            checkpoint.historical_surface_comparison_commit(ordinary, "historical-anchor"),
            "historical-anchor",
        )

    def test_verdier_illusie_manifest_uses_sealed_validation_head(self):
        self.assertEqual(
            checkpoint.illusie_manifest_validation_revision(
                self.composition, "nonlinear-verdier-head"),
            "old-ai-validation-head",
        )
        ordinary = {"schema": checkpoint.AI_COMPOSITION_SCHEMA,
                    "previous_public_main_head": "prior-public"}
        self.assertEqual(
            checkpoint.illusie_manifest_validation_revision(
                ordinary, "linear-ai-head"),
            "linear-ai-head",
        )


if __name__ == "__main__":
    unittest.main()
