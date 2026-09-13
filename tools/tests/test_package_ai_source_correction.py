"""Typed package input/dispatch tests; no PDF bytes, TeX, Git, or network.

The live composition functions are mocked only in dispatch tests. Receipt shape,
checkpoint checks, the pure correction-scope validator and manifest are real.
"""
from copy import deepcopy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
if os.environ.get("DIRECT_SUCCESSOR_TEST_TOOLS"):
    sys.path.insert(0, os.environ["DIRECT_SUCCESSOR_TEST_TOOLS"])
sys.path.insert(0, str(TOOLS.parent))
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import package_direct_successor_pdfs as package
import validate_direct_successor_release as release
import ai_source_correction_composition as correction
from test_compare_ai_source_correction import fixture as checkpoint_fixture


PUBLIC_PATH = "validation/direct-successor-r48-illusie-correction-build-a-2026-09-13.json"


def fixture(corrected=True):
    receipt, _ = checkpoint_fixture(corrected)
    binding = receipt["composition"]
    binding.update(authority_commit=package.AUTHORITY, authority_tree=package.AUTHORITY_TREE,
                   new_overlay_ids=[package.R48], last_admitted_overlay=package.R48,
                   required_build_stems=list(package.R48_STEMS),
                   affected_source_stems=list(package.CORRECTION_PDFS if corrected else package.DIRECT_PDFS))
    receipt["artifacts"] = [
        {"stem": stem, "pages": 2, "bytes": 123, "sha256": "A" * 64,
         "diagnostics": dict.fromkeys(release.DIAGNOSTICS, 0),
         "external_references": {"count": 0, "sha256": "B" * 64}}
        for stem in package.R48_STEMS
    ]
    receipt["build"].update(
        strategy="sequential-prime-bibtex-global-state-sweeps",
        fixed_point_suffixes=list(release.SUFFIXES), stem_selection="composition_receipt",
        stems=list(package.R48_STEMS), chapter_count=36, pdfinfo_readable=36,
        worktree_kind="linked", primary_worktree_override=False,
        diagnostics=dict.fromkeys(release.DIAGNOSTICS, 0),
        artifact_tuple_set_sha256=release.tuple_hash(receipt["artifacts"]),
    )
    return receipt


def raw(receipt):
    return package.canonical_json(receipt)


def manifest(receipt):
    return package.public_manifest(raw(receipt), receipt, receipt["composition"],
                                   receipt["artifacts"], PUBLIC_PATH, "f" * 40)


class CorrectionPackageTests(unittest.TestCase):
    def test_corrected_full_36_build_inputs_pass_real_checks(self):
        receipt = fixture()
        actual, binding, artifacts = package.build_inputs(raw(receipt), PUBLIC_PATH)
        self.assertEqual(actual, receipt)
        self.assertEqual(binding, receipt["composition"])
        self.assertEqual(len(artifacts), 36)

    def test_old_direct_v1_build_inputs_still_pass(self):
        receipt = fixture(False)
        self.assertEqual(package.build_inputs(raw(receipt), PUBLIC_PATH)[0], receipt)

    def test_unknown_composition_variant_rejected(self):
        receipt = fixture()
        receipt["composition"]["schema"] = "untyped"
        with self.assertRaisesRegex(ValueError, "unsupported package composition"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_old_v1_cannot_smuggle_correction_identity(self):
        receipt = fixture(False)
        receipt["composition"]["ai_source_correction_scope"] = fixture()["composition"]["ai_source_correction_scope"]
        with self.assertRaisesRegex(ValueError, "untyped AI correction"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_incomplete_profile_rejected(self):
        receipt = fixture()
        receipt["composition"]["required_build_stems"].remove("simplicial")
        with self.assertRaisesRegex(ValueError, "chapter profile"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_old_two_chapter_affected_scope_rejected_for_correction(self):
        receipt = fixture()
        receipt["composition"]["affected_source_stems"] = list(package.DIRECT_PDFS)
        with self.assertRaisesRegex(ValueError, "chapter profile"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_old_r48_source_cannot_certify_new_package(self):
        receipt = fixture()
        receipt["source"]["commit"] = correction.SEALED
        with self.assertRaisesRegex(ValueError, "old R48 A/B"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_missing_corrected_checkpoint_rejected(self):
        receipt = fixture()
        receipt["source_checkpoint"] = checkpoint_fixture(False)[0]["source_checkpoint"]
        with self.assertRaisesRegex(ValueError, "current AI-correction checkpoint"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_missing_current_illusie_semantics_rejected(self):
        receipt = fixture()
        del receipt["source_checkpoint"]["current_illusie_successor"]
        with self.assertRaisesRegex(ValueError, "current Illusie"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_mismatched_ega_build_head_rejected(self):
        receipt = fixture()
        receipt["source_checkpoint"]["current_ega_successor"]["current_commit"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "historical/current EGA"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_real_build_shape_rejects_artifact_omission(self):
        receipt = fixture()
        receipt["artifacts"].pop()
        with self.assertRaisesRegex(ValueError, "artifact coverage/order"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_real_mutex_check_still_enforced(self):
        receipt = fixture()
        receipt["build"]["machine_wide_tex_mutex"]["ownership_acquired"] = False
        with self.assertRaisesRegex(ValueError, "ownership_acquired"):
            package.build_inputs(raw(receipt), PUBLIC_PATH)

    def test_scope_is_copied_exactly_into_public_manifest(self):
        receipt = fixture()
        value = manifest(receipt)
        self.assertEqual(value["composition"]["schema"], package.AI_CORRECTION_SCHEMA)
        self.assertEqual(value["scope"]["ai_source_correction"], receipt["composition"]["ai_source_correction_scope"])
        self.assertEqual(value["scope"]["affected_chapters"], list(package.CORRECTION_PDFS))
        self.assertEqual(value["composition"]["new_overlay_ids"], [package.R48])
        self.assertEqual(len(value["pdfs"]), 36)

    def test_old_manifest_and_supplemental_pdf_scope_remain_old_shape(self):
        value = manifest(fixture(False))
        self.assertNotIn("ai_source_correction", value["scope"])
        self.assertEqual(value["composition"]["schema"], package.DIRECT_SCHEMA)
        self.assertEqual(value["scope"]["affected_chapters"], list(package.DIRECT_PDFS))
        self.assertEqual(package.direct_pdfs(fixture(False)["composition"]), package.DIRECT_PDFS)

    def test_corrected_simplicial_is_individual_supplement(self):
        self.assertEqual(package.direct_pdfs(fixture()["composition"]), package.CORRECTION_PDFS)
        text = package.readme(manifest(fixture())).decode()
        self.assertIn("`simplicial.pdf`", text)
        self.assertIn("separate from the official-source errata overlay", text)

    def test_public_metadata_does_not_dump_private_build_fields(self):
        receipt = fixture()
        receipt["environment"]["private_path"] = "PRIVATE_MACHINE_PATH_DO_NOT_PUBLISH"
        receipt["tex_process_tree"] = {"private_command": "PRIVATE_COMMAND_DO_NOT_PUBLISH"}
        value = package.canonical_json(manifest(receipt)).decode()
        self.assertNotIn("PRIVATE_MACHINE", value)
        self.assertNotIn("PRIVATE_COMMAND", value)

    def test_actual_loader_and_rechecker_dispatch(self):
        binding = fixture()["composition"]
        with patch.object(correction, "load_ai_source_correction",
                          return_value=(deepcopy(binding), package.R48_STEMS, package.CORRECTION_PDFS)) as loader, \
             patch.object(correction, "recheck_ai_source_correction_tools") as recheck:
            result = package.load_package_correction(Path("fixture-repository"), binding)
            loader.assert_called_once_with(Path("fixture-repository"), Path(binding["receipt"]))
            recheck.assert_called_once_with(Path("fixture-repository"), binding)
            self.assertIs(result, recheck)

    def test_actual_loader_binding_drift_rejected(self):
        binding = fixture()["composition"]
        changed = deepcopy(binding)
        changed["receipt_sha256"] = "0" * 64
        with patch.object(correction, "load_ai_source_correction",
                          return_value=(changed, package.R48_STEMS, package.CORRECTION_PDFS)), \
             patch.object(correction, "recheck_ai_source_correction_tools") as recheck, \
             self.assertRaisesRegex(ValueError, "differs from actual composition"):
            package.load_package_correction(Path("fixture-repository"), binding)
        recheck.assert_not_called()

    def test_live_profile_drift_rejected(self):
        binding = fixture()["composition"]
        with patch.object(correction, "load_ai_source_correction",
                          return_value=(binding, package.R48_STEMS[:-1], package.CORRECTION_PDFS)), \
             self.assertRaisesRegex(ValueError, "live correction package profile"):
            package.load_package_correction(Path("fixture-repository"), binding)

    def test_old_package_does_not_take_correction_loader_route(self):
        with patch.object(correction, "load_ai_source_correction") as loader:
            self.assertIsNone(package.load_package_correction(Path("fixture-repository"), fixture(False)["composition"]))
            loader.assert_not_called()

    def test_package_calls_live_loader_before_pdf_io(self):
        # Only a JSON receipt and an empty temporary directory exist; the
        # deliberately stopped Objects call proves dispatch precedes all PDFs.
        receipt = fixture()
        with tempfile.TemporaryDirectory(prefix="correction-package-test-") as tmp:
            root = Path(tmp)
            receipt_path = root / "receipt.json"
            receipt_path.write_bytes(raw(receipt))
            with patch.object(package, "load_package_correction") as live, \
                 patch.object(package, "Objects", side_effect=RuntimeError("STOP_BEFORE_PDFS")), \
                 patch.object(package, "check_pdf") as pdf_check, \
                 self.assertRaisesRegex(RuntimeError, "STOP_BEFORE_PDFS"):
                package.package(root, root, receipt_path, root / "never-created", "f" * 40, PUBLIC_PATH)
            live.assert_called_once_with(root, receipt["composition"])
            pdf_check.assert_not_called()
            self.assertFalse((root / "never-created").exists())


if __name__ == "__main__":
    unittest.main()
