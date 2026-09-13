"""Bounded additive consumer tests; fixture objects only, no TeX/network."""
from copy import deepcopy
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile

import validate_direct_successor_release as v
import build_fixed_point as builder
import validate_unified_repository as entrypoint


CORRECTION_SCOPE = {
    "correction_id": "illusie-volume-i-grading-eilenberg-zilber-i1-4-20260913",
    "candidate_commit": "4c3647f926f32a0edade647ebb52adce05d24a8e",
    "candidate_tree": "a" * 40,
    "manifest": {"path": "validation/direct-successor-illusie-correction-manifest.json",
                 "bytes": 123, "sha256": "A" * 64, "git_blob": "b" * 40},
    "corrected_source_commit": "ea606e202707d215f38e050be2621d0c83cadef0",
    "corrected_source_tree": "3a0e1ee6f7c575a261a254e1f4701a982e8c12a6",
    "sealed_predecessor_commit": "1c7fa79a3d8fdb24a9ec45ba65e65ce1fd8867c2",
    "sealed_predecessor_receipt_sha256": "546206C486E7722D9086B9E4ADF979CCA11DC8587D3E28CCFEA551C700606ADE",
}


def fixture_binding():
    return {"schema": v.AI_SCHEMA, "composition_source_commit": CORRECTION_SCOPE["corrected_source_commit"],
            "composition_source_tree": CORRECTION_SCOPE["corrected_source_tree"],
            "registry_cutoff_commit": "54cb855d7f499c885020efb7aebd24959cda5120",
            "new_overlay_ids": ["stacks-errata-a04446e-r48"], "ai_source_correction_scope": deepcopy(CORRECTION_SCOPE),
            "correction_protected_inputs": {CORRECTION_SCOPE["manifest"]["path"]:
                                            deepcopy(CORRECTION_SCOPE["manifest"])}}


def fake_scope_validator(scope, *, source_commit=None, source_tree=None):
    # This is the narrowly mocked composition dependency, not a claim to test
    # its mathematical/historical verifier. Production calls its real export.
    v.require(set(scope) == set(CORRECTION_SCOPE), "scope keys")
    v.require(scope["corrected_source_commit"] == source_commit
              and scope["corrected_source_tree"] == source_tree, "scope source")
    v.require(scope["manifest"] == CORRECTION_SCOPE["manifest"], "scope manifest")


class NewConsumerTests(unittest.TestCase):
    def setUp(self):
        self.binding = fixture_binding()
        self.scope_module = SimpleNamespace(validate_ai_source_correction_scope=fake_scope_validator)
        self.modules = patch.dict(sys.modules, {"ai_source_correction_composition": self.scope_module})
        self.modules.start()
        self.addCleanup(self.modules.stop)
        self.stems = ("schemes", "groupoids", "spaces-perfect", "simplicial") + tuple(f"fixture-{n}" for n in range(32))
        self.build = {"source": {"commit": "f" * 40, "tree": "e" * 40},
                      "source_checkpoint": {"schema": v.AI_CHECKPOINT_SCHEMA, "status": v.AI_CHECKPOINT_STATUS,
                                            "ai_source_correction": deepcopy(CORRECTION_SCOPE)}}

    def test_new_scope_exactly_propagates_to_index(self):
        actual = v.index_composition_scope(self.binding)
        self.assertEqual(actual["ai_source_correction"], CORRECTION_SCOPE)
        self.assertEqual(actual["new_overlay_ids"], ["stacks-errata-a04446e-r48"])

    def test_old_scope_unchanged(self):
        binding = {"schema": v.SCHEMA, "composition_source_commit": "a" * 40,
                   "registry_cutoff_commit": "b" * 40, "new_overlay_ids": ["historical"]}
        self.assertEqual(set(v.index_composition_scope(binding)), {"source_commit", "registry_cutoff_commit", "new_overlay_ids"})

    def test_old_schema_cannot_launder_correction(self):
        self.binding["schema"] = v.SCHEMA
        with self.assertRaisesRegex(ValueError, "untyped AI correction"):
            v.index_composition_scope(self.binding)

    def test_corrected_build_binding_accepts_exact_full_profile(self):
        v.validate_correction_build_binding(self.build, self.binding, self.stems)

    def test_old_r48_build_cannot_certify_correction(self):
        self.build["source"]["commit"] = CORRECTION_SCOPE["sealed_predecessor_commit"]
        with self.assertRaisesRegex(ValueError, "old R48 A/B"):
            v.validate_correction_build_binding(self.build, self.binding, self.stems)

    def test_old_checkpoint_rejected(self):
        self.build["source_checkpoint"]["schema"] = "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-direct-successor/v1"
        with self.assertRaisesRegex(ValueError, "current AI-correction checkpoint"):
            v.validate_correction_build_binding(self.build, self.binding, self.stems)

    def test_wrong_checkpoint_correction_identity_rejected(self):
        self.build["source_checkpoint"]["ai_source_correction"]["candidate_commit"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "current AI-correction checkpoint"):
            v.validate_correction_build_binding(self.build, self.binding, self.stems)

    def test_missing_simplicial_rejected(self):
        with self.assertRaisesRegex(ValueError, "36 cumulative chapters"):
            v.validate_correction_build_binding(self.build, self.binding, self.stems[:3] + self.stems[4:] + ("extra",))

    def test_missing_chapter_rejected(self):
        with self.assertRaisesRegex(ValueError, "36 cumulative chapters"):
            v.validate_correction_build_binding(self.build, self.binding, self.stems[:-1])

    def test_protected_dossier_is_exposed_to_readback(self):
        self.assertEqual(v.correction_inputs(self.binding), self.binding["correction_protected_inputs"])
        self.assertIn("tools/ai_source_correction_composition.py", v.scoped_tools(self.binding))

    def test_empty_protected_dossier_rejected(self):
        self.binding["correction_protected_inputs"] = {}
        with self.assertRaisesRegex(ValueError, "protected-input closure"):
            v.correction_inputs(self.binding)

    def test_unsafe_protected_dossier_path_rejected(self):
        self.binding["correction_protected_inputs"] = {"../private.json": CORRECTION_SCOPE["manifest"]}
        with self.assertRaisesRegex(ValueError, "unsafe relative path"):
            v.correction_inputs(self.binding)

    def test_new_protected_recheck_dispatch(self):
        calls = []
        self.scope_module.recheck_ai_source_correction_tools = lambda *args: calls.append(args)
        builder.require_direct_tools_unchanged(Path("fixture"), self.binding)
        self.assertEqual(calls, [(Path("fixture"), self.binding)])

    def test_new_recheck_failure_propagates(self):
        def failed(*args):
            raise ValueError("current semantic checker failed")
        self.scope_module.recheck_ai_source_correction_tools = failed
        with self.assertRaisesRegex(RuntimeError, "semantic checker failed"):
            builder.require_direct_tools_unchanged(Path("fixture"), self.binding)

    def test_old_recheck_dispatch_unchanged(self):
        calls = []
        with patch.dict(sys.modules, {"direct_successor_composition": SimpleNamespace(
                recheck_direct_validation_tools=lambda *args: calls.append(args))}):
            builder.require_direct_tools_unchanged(Path("fixture"), {"schema": v.SCHEMA})
        self.assertEqual(len(calls), 1)

    def test_new_composition_loader_dispatch(self):
        with tempfile.TemporaryDirectory(prefix="r48-consumer-fixture-") as temporary:
            root = Path(temporary)
            target = root / "validation/composition-current.json"
            target.parent.mkdir()
            target.write_text('{"schema": "' + v.AI_SCHEMA + '", "status": "PASS"}', encoding="utf-8")
            result = (self.binding, self.stems, ("groupoids", "spaces-perfect", "simplicial"))
            self.scope_module.load_ai_source_correction = lambda *args: result
            with patch.object(builder, "require_clean_path"), patch.object(builder, "git", return_value="a" * 40):
                self.assertEqual(builder.load_composition_receipt(root, Path("validation/composition-current.json")), result)

    def test_actual_new_scope_validator(self):
        import importlib.util
        path = Path(__file__).resolve().parents[1] / "ai_source_correction_composition.py"
        if not path.exists():
            path = Path(__file__).with_name("ai_source_correction_composition.py")
        spec = importlib.util.spec_from_file_location("real_ai_correction_scope_for_test", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        scope = deepcopy(CORRECTION_SCOPE)
        scope["correction_id"] = module.CORRECTION_ID
        scope["manifest"]["path"] = module.MANIFEST
        module.validate_ai_source_correction_scope(scope, source_commit=scope["corrected_source_commit"],
                                                  source_tree=scope["corrected_source_tree"])
        scope["candidate_commit"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "scope identity mismatch"):
            module.validate_ai_source_correction_scope(scope)

    def visual_fixture(self):
        affected = ("groupoids", "simplicial", "spaces-perfect")
        units = [{"unit_id": unit, "source": "simplicial.tex", "start_byte": n * 10,
                  "end_byte_exclusive": n * 10 + 5, "sha256": "A" * 64}
                 for n, unit in enumerate(("eilenberg-zilber-and-grading", "i1.4-localization"))]
        build = {"source": self.build["source"], "composition": {**self.binding, "correction_visual_units": units},
                 "build": {"global_fixed_point_sweep": 3}}
        artifacts = [{"stem": stem, "pages": 1, "bytes": 10, "sha256": "B" * 64} for stem in affected]
        ref = {"path": "validation/direct-successor-build-a.json", "bytes": 100, "sha256": "C" * 64}
        visual = {"schema": "unofficial-ai-integrated-stacks-visual-qa/v1", "status": "PASS",
                  "source": build["source"], "build_receipt": {**ref, "status": "PASS", "global_fixed_point_sweep": 3},
                  "scope": {"affected_chapters": list(affected), "ai_source_correction": CORRECTION_SCOPE,
                            "full_page_render_count": 3, "full_page_contact_sheet_review_count": 3,
                            "high_resolution_locus_pages": {stem: [1] for stem in affected}, "high_resolution_locus_page_count": 3},
                  "artifacts": {row["stem"]: {**row, "pdf": row["stem"] + ".pdf", "encrypted": False,
                                                "pages_without_ink": 0, "duplicate_render_hashes": 0} for row in artifacts},
                  "checks": {**{k: True for k in v.VISUAL_TRUE}, **{k: 0 for k in v.VISUAL_ZERO}},
                  "render_protocol": {"renderer": "Poppler fixture", "full_page_dpi": 96,
                                      "high_resolution_dpi": 180, "render_intermediates_published": False},
                  "ai_correction_loci": {"schema": "unofficial-ai-integrated-stacks-ai-correction-visual-loci/v1",
                       "source": build["source"], "mapping_method": "exact-current-source-interval-to-final-pdf",
                       "inspection_performed": True,
                       "pdf": {"path": "simplicial.pdf", "pages": 1, "bytes": 10, "sha256": "B" * 64},
                       "units": [{**unit, "pages": [1]} for unit in units]}}
        return visual, ref, build, artifacts, affected

    def test_loader_sorted_visual_union_supported(self):
        v.validate_visual(*self.visual_fixture())

    def test_visual_correction_identity_cannot_be_omitted(self):
        visual, *args = self.visual_fixture()
        del visual["scope"]["ai_source_correction"]
        with self.assertRaisesRegex(ValueError, "visual correction scope mismatch"):
            v.validate_visual(visual, *args)

    def test_simplicial_cannot_be_omitted_from_visual_union(self):
        visual, ref, build, artifacts, affected = self.visual_fixture()
        with self.assertRaisesRegex(ValueError, "visual union mismatch"):
            v.validate_visual(visual, ref, build, artifacts, ("groupoids", "spaces-perfect"))

    def test_new_release_cannot_omit_correction_scope(self):
        from test_validate_direct_successor_release import Fixture
        f = Fixture()
        binding = {**f.binding, **self.binding}
        release = {"schema": v.RELEASE_SCHEMA, "status": "PUBLICATION_COMPLETE", "repository": v.REPOSITORY,
                   "default_branch": "main", "receipts": {role: f.index["references"][role] for role in v.CORE_ROLES},
                   "scope": {}}
        with self.assertRaisesRegex(ValueError, "release scope mismatch"):
            v.validate_release(f.objects, release, f.index, {}, binding, f.first["artifacts"])

    def readback_fixture(self):
        required = v.release_core_readback_paths(self.binding, {})
        readback = {"status": "PASS", "anonymous": True, "commit": "f" * 40,
                    "checked_paths": [{"path": path, "bytes": 1, "sha256": "A" * 64,
                                       "git_blob": "b" * 40} for path in sorted(required)]}
        return readback, required, "f" * 40

    def test_public_readback_requires_exact_correction_dossier(self):
        args = self.readback_fixture()
        self.assertIn(CORRECTION_SCOPE["manifest"]["path"], args[1])
        v.validate_public_readback_inventory(*args)

    def test_public_readback_omitting_correction_dossier_rejected(self):
        readback, required, head = self.readback_fixture()
        readback["checked_paths"] = [row for row in readback["checked_paths"]
                                     if row["path"] != CORRECTION_SCOPE["manifest"]["path"]]
        with self.assertRaisesRegex(ValueError, "omits required"):
            v.validate_public_readback_inventory(readback, required, head)

    def test_public_readback_omitting_native_source_inventory_rejected(self):
        readback, required, head = self.readback_fixture()
        required.add("validation/direct-successor-native-source-inventory.json")
        with self.assertRaisesRegex(ValueError, "omits required"):
            v.validate_public_readback_inventory(readback, required, head)


class EditionPackagingTests(unittest.TestCase):
    def setUp(self):
        self.artifacts = [{"stem": "chapter-" + str(n), "pages": 2, "bytes": 10, "sha256": "A" * 64}
                          for n in range(36)]
        self.reader = {"name": "01-cumulative-reader.pdf", "role": "cumulative_reader",
                       "cumulative_reader": {"scope": "36-chapter cumulative release, not the full Stacks Project",
                           "chapter_count": 36, "total_pages": 72, "chapters": [
                           {"stem": row["stem"], "title": row["stem"], "start_page": 2 * n + 1,
                            "end_page": 2 * n + 2, "pages": 2,
                            "source_pdf": {"bytes": row["bytes"], "sha256": row["sha256"]}}
                           for n, row in enumerate(self.artifacts)]}}

    def test_cumulative_reader_ranges_and_all36_identity(self):
        self.assertEqual(v.validate_cumulative_reader_descriptor(self.reader, self.artifacts)["total_pages"], 72)

    def test_reader_cannot_be_individual_chapter(self):
        self.reader["name"] = "simplicial.pdf"
        with self.assertRaisesRegex(ValueError, "first release asset"):
            v.validate_cumulative_reader_descriptor(self.reader, self.artifacts)

    def test_reader_missing_chapter_rejected(self):
        self.reader["cumulative_reader"]["chapters"].pop()
        with self.assertRaisesRegex(ValueError, "inventory incomplete"):
            v.validate_cumulative_reader_descriptor(self.reader, self.artifacts)

    def test_reader_range_overlap_rejected(self):
        self.reader["cumulative_reader"]["chapters"][1]["start_page"] = 2
        with self.assertRaisesRegex(ValueError, "range incomplete or overlapping"):
            v.validate_cumulative_reader_descriptor(self.reader, self.artifacts)

    def test_reader_changed_chapter_source_pdf_rejected(self):
        self.reader["cumulative_reader"]["chapters"][0]["source_pdf"]["sha256"] = "B" * 64
        with self.assertRaisesRegex(ValueError, "verified build PDF"):
            v.validate_cumulative_reader_descriptor(self.reader, self.artifacts)

    def zip_fixture(self, omit=False, corrupt=False, unexpected=False):
        data = b"complete native source fixture"
        row = {"archive_path": "current/example.tex", "bytes": len(data), "sha256": v.identity(data)["sha256"]}
        inventory = {"members": [row]}
        raw_inventory = b'{"fixture":"immutable inventory"}'
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as archive:
            archive.writestr("SOURCE-INVENTORY.json", raw_inventory)
            if not omit:
                archive.writestr(row["archive_path"], b"corrupt" if corrupt else data)
            if unexpected:
                archive.writestr("unexpected.txt", b"extra")
        stream.seek(0)
        return stream, inventory, raw_inventory

    def test_native_source_zip_reopens_exact_members(self):
        v.check_native_source_zip(*self.zip_fixture())

    def test_native_source_zip_missing_body_rejected(self):
        with self.assertRaisesRegex(ValueError, "member inventory incomplete"):
            v.check_native_source_zip(*self.zip_fixture(omit=True))

    def test_native_source_zip_corrupt_body_rejected(self):
        with self.assertRaisesRegex(ValueError, "type/size/encryption mismatch"):
            v.check_native_source_zip(*self.zip_fixture(corrupt=True))

    def test_native_source_zip_unexpected_member_rejected(self):
        with self.assertRaisesRegex(ValueError, "member inventory incomplete"):
            v.check_native_source_zip(*self.zip_fixture(unexpected=True))

    def test_native_source_zip_embedded_inventory_drift_rejected(self):
        stream, inventory, raw = self.zip_fixture()
        with self.assertRaisesRegex(ValueError, "inventory member size"):
            v.check_native_source_zip(stream, inventory, raw + b"changed")


class CorrectionVisualLocusTests(unittest.TestCase):
    def setUp(self):
        self.units = [{"unit_id": unit, "source": "simplicial.tex", "start_byte": n * 10,
                       "end_byte_exclusive": n * 10 + 5, "sha256": "A" * 64}
                      for n, unit in enumerate(("eilenberg-zilber-and-grading", "i1.4-localization"))]
        self.build = {"source": {"commit": "f" * 40, "tree": "e" * 40},
                      "composition": {"correction_visual_units": self.units}}
        self.artifacts = {"simplicial": {"bytes": 10, "sha256": "B" * 64, "pages": 78}}
        self.loci = {"simplicial": [49, 50, 51]}
        self.visual = {"ai_correction_loci": {"schema": "unofficial-ai-integrated-stacks-ai-correction-visual-loci/v1",
                       "source": self.build["source"], "mapping_method": "exact-current-source-interval-to-final-pdf",
                       "inspection_performed": True,
                       "pdf": {"path": "simplicial.pdf", **self.artifacts["simplicial"]},
                       "units": [{**unit, "pages": [49 + n]} for n, unit in enumerate(self.units)]}}

    def test_both_distinct_claim_loci_required(self):
        v.validate_correction_visual_loci(self.visual, self.build, self.artifacts, self.loci)

    def test_missing_i14_locus_rejected(self):
        self.visual["ai_correction_loci"]["units"].pop()
        with self.assertRaisesRegex(ValueError, "unit coverage"):
            v.validate_correction_visual_loci(self.visual, self.build, self.artifacts, self.loci)

    def test_uninspected_corrected_page_rejected(self):
        self.visual["ai_correction_loci"]["units"][1]["pages"] = [52]
        with self.assertRaisesRegex(ValueError, "absent from high-resolution"):
            v.validate_correction_visual_loci(self.visual, self.build, self.artifacts, self.loci)

    def test_stale_pdf_identity_rejected(self):
        self.visual["ai_correction_loci"]["pdf"]["sha256"] = "C" * 64
        with self.assertRaisesRegex(ValueError, "current Simplicial"):
            v.validate_correction_visual_loci(self.visual, self.build, self.artifacts, self.loci)


class NativeSourceDescriptorTests(unittest.TestCase):
    """Exact tiny Git-object fixtures; no production scans or Git mutation."""
    def setUp(self):
        from test_validate_direct_successor_release import MemoryObjects
        self.objects = MemoryObjects()
        self.source, self.inventory_commit, self.content = "d" * 40, "b" * 40, "c" * 40
        self.stems = ["chapter-" + str(n) for n in range(36)]
        self.members = []
        for revision, prefix, path, raw in (
                (self.source, "current/", "tools/cumulative-master.json", b'{"fixture":"master"}'),
                (self.source, "current/", "chapter-0.tex", b"current native source"),
                (v.AUTHORITY, "baseline/", "chapter-0.tex", b"printed native witness")):
            self.objects.files[path] = raw
            self.objects.revisions.setdefault(revision, {})[path] = raw
            if revision == self.source:
                self.objects.revisions.setdefault(self.content, {})[path] = raw
            self.members.append({"archive_path": prefix + path, "git_commit": revision,
                                 "git_path": path, **v.identity(raw)})
        self.expected = {row["archive_path"]: deepcopy(row) for row in self.members}
        self.inventory = {"schema": "native-cumulative-source-inventory/v1", "source_commit": self.source,
                          "authority_commit": v.AUTHORITY, "chapter_stems": self.stems,
                          "master_path": "current/tools/cumulative-master.json", "members": self.members,
                          "closure": {"policy": "all-committed-native-inputs-plus-build-support", "checked": True}}
        self.path = "validation/direct-successor-native-source-inventory.json"
        self.asset = {"name": "02-full-cumulative-editable-source.zip", "role": "full_cumulative_editable_source",
                      "source_archive": {"metadata_member": "SOURCE-INVENTORY.json"}}
        self.closure_calls = []
        def derive(*args):
            self.closure_calls.append(args)
            return self.expected
        self.mock_module = patch.dict(sys.modules, {"cumulative_source": SimpleNamespace(expected_source_members=derive)})
        self.mock_module.start()
        self.addCleanup(self.mock_module.stop)
        self.bind_inventory()

    def bind_inventory(self):
        raw = json.dumps(self.inventory, sort_keys=True).encode()
        self.objects.files[self.path] = raw
        self.asset["source_archive"]["source_inventory"] = {
            "path": self.path, "commit": self.inventory_commit, **v.identity(raw)}

    def check(self):
        return v.validate_source_archive_descriptor(self.objects, self.asset, self.content, self.stems, self.source)

    def test_complete_exact_source_closure_accepted(self):
        inventory, raw, path = self.check()
        self.assertEqual(inventory, self.inventory)
        self.assertEqual(path, self.path)
        self.assertEqual(self.closure_calls, [(self.objects.root, self.source, v.AUTHORITY, self.stems)])

    def test_older_build_source_cannot_be_relabelled(self):
        self.inventory["source_commit"] = "e" * 40
        self.bind_inventory()
        with self.assertRaisesRegex(ValueError, "exact fresh build source"):
            self.check()

    def test_missing_body_despite_checked_true_rejected(self):
        self.inventory["members"] = self.members[:1] + self.members[2:]
        self.bind_inventory()
        with self.assertRaisesRegex(ValueError, "recomputed cumulative source closure"):
            self.check()

    def test_unreviewed_content_source_drift_rejected(self):
        self.objects.revisions[self.content]["chapter-0.tex"] = b"unreviewed edit"
        with self.assertRaisesRegex(ValueError, "native source changed before publication"):
            self.check()

    def test_inventory_drift_after_binding_rejected(self):
        self.objects.revisions[self.content][self.path] = b"changed inventory"
        with self.assertRaisesRegex(ValueError, "inventory commit/content identity drift"):
            self.check()

    def test_baseline_current_mix_rejected(self):
        self.inventory["members"][2]["archive_path"] = "current/chapter-0.tex"
        self.bind_inventory()
        with self.assertRaisesRegex(ValueError, "printed witness are not separated"):
            self.check()

    def test_nonprimary_source_zip_role_rejected(self):
        self.asset["role"] = "supplement"
        with self.assertRaisesRegex(ValueError, "second release asset"):
            self.check()

    def test_wrong_closure_policy_rejected(self):
        self.inventory["closure"]["policy"] = "just-the-master"
        self.bind_inventory()
        with self.assertRaisesRegex(ValueError, "closure policy mismatch"):
            self.check()

    def test_numeric_checked_flag_is_not_boolean(self):
        self.inventory["closure"]["checked"] = 1
        self.bind_inventory()
        with self.assertRaisesRegex(ValueError, "closure policy mismatch"):
            self.check()

    def test_float_member_bytes_not_silently_coerced(self):
        self.inventory["members"][0]["bytes"] = float(self.inventory["members"][0]["bytes"])
        self.bind_inventory()
        with self.assertRaisesRegex(ValueError, "member Git identity mismatch"):
            self.check()

    def test_missing_master_rejected(self):
        self.inventory["master_path"] = "current/missing-master.tex"
        self.bind_inventory()
        with self.assertRaisesRegex(ValueError, "cumulative editable master is absent"):
            self.check()


class TopLevelDispatchTests(unittest.TestCase):
    def test_ci_dependency_and_new_suites_are_reachable(self):
        workflow = Path(__file__).resolve().parents[1] / ".github/workflows/validate.yml"
        text = workflow.read_text(encoding="utf-8")
        dependency = "python -m pip install pypdf==6.10.0"
        self.assertEqual(text.count(dependency), 1)
        self.assertLess(text.index(dependency), text.index("python tools/validate_unified_repository.py"))
        self.assertIn("python -m unittest discover -s tools -p 'test_ai_source_correction*.py'", text)
        self.assertIn("python -m unittest discover -s tools/tests -p 'test_*ai_source_correction.py'", text)
        self.assertIn("python -m unittest discover -s tools -p 'test_cumulative_packaging.py'", text)

    def route(self, schema, arguments, with_index=True):
        with tempfile.TemporaryDirectory(prefix="r48-dispatch-fixture-") as temporary:
            root = Path(temporary)
            (root / "validation").mkdir()
            (root / "validation/composition-current.json").write_text(
                json.dumps({"schema": schema}), encoding="utf-8")
            if with_index:
                (root / v.INDEX).write_text(json.dumps({"references": {"build": {
                    "path": "validation/direct-successor-corrected-build.json"}}}), encoding="utf-8")
            with patch.object(entrypoint, "ROOT", root), patch.object(v, "validate_direct_release", return_value=37) as consumer:
                code = entrypoint.main(arguments)
                return code, consumer.call_args_list

    def test_new_top_level_route_uses_current_build_index(self):
        code, calls = self.route(v.AI_SCHEMA, ["--pre-publication"])
        self.assertEqual(code, 37)
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0].args[1:], (Path("validation/direct-successor-corrected-build.json"), True))

    def test_new_top_level_explicit_build_route(self):
        code, calls = self.route(v.AI_SCHEMA, ["--build-receipt", "validation/direct-successor-explicit.json"])
        self.assertEqual(code, 37)
        self.assertEqual(calls[0].args[1:], (Path("validation/direct-successor-explicit.json"), False))

    def test_old_top_level_route_unchanged(self):
        code, calls = self.route(v.SCHEMA, ["--pre-publication"])
        self.assertEqual(code, 37)
        self.assertEqual(len(calls), 1)

    def test_missing_new_index_fails_without_fallback(self):
        from contextlib import redirect_stderr
        with redirect_stderr(io.StringIO()):
            code, calls = self.route(v.AI_SCHEMA, ["--pre-publication"], with_index=False)
        self.assertEqual(code, 1)
        self.assertEqual(calls, [])


if __name__ == "__main__":
    unittest.main()
