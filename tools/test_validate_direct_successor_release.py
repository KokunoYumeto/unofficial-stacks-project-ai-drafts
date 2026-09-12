"""In-memory release-contract tests. No TeX, network, or production writes."""
from copy import deepcopy
import io
import json
import os
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile

import validate_direct_successor_release as v

TOOL_ROOT = Path(os.environ.get("DIRECT_SUCCESSOR_TEST_TOOLS", str(Path(__file__).resolve().parent)))
sys.path.insert(0, str(TOOL_ROOT))
import validate_unified_repository as old
import compare_fixed_point_builds as compare
import tex_process_public_receipt as public_guard


def raw(document):
    return (json.dumps(document, sort_keys=True) + "\n").encode()


def ref(path, data):
    return {"path": path, **v.identity(data)}


def mutex(second=False):
    minute = "02" if second else "00"
    return {"schema": old.TEX_MUTEX_RECEIPT_SCHEMA, "status": "PASS", "name": old.TEX_MUTEX_NAME,
            "namespace": "Windows Global", "held_scope": old.TEX_MUTEX_HELD_SCOPE,
            "release_result": "released_in_finally", "acquisition_timeout_ms": old.TEX_MUTEX_TIMEOUT_MS,
            "ownership_acquired": True, "wait_result_code": "0x00000000", "wait_result": "acquired",
            "abandoned_mutex_recovered": False, "wait_started_utc": f"2026-09-12T10:{minute}:00Z",
            "acquired_utc": f"2026-09-12T10:{minute}:00Z", "released_utc": f"2026-09-12T10:{minute}:50Z",
            "wait_duration_ms": 0.0, "held_duration_ms": 50000.0}


def captures(guard, run):
    rows = []
    for number in range(12):
        second = run == "second"
        pid = 1000 + number + (100 if second else 0)
        minute = "02" if second else "00"
        private = {"schema": public_guard.RECEIPT_SCHEMA, **public_guard.LIFECYCLE_CONSTANTS,
                   "started_utc": f"2026-09-12T10:{minute}:{number + 1:02d}Z",
                   "finished_utc": f"2026-09-12T10:{minute}:{number + 1:02d}.5Z",
                   "root_identity": {"pid": pid, "creation_filetime_100ns": 100000 + pid},
                   "initial_accounting": {"active_processes": 1, "total_processes": 1, "total_terminated_processes": 0},
                   "final_accounting": {"active_processes": 0, "total_processes": 1, "total_terminated_processes": 0},
                   "cwd": "C:/Users/private-machine/PRIVATE_WORKTREE",
                   "command": ["C:/PRIVATE_TOOL/pdflatex.exe", "private-source.tex"],
                   "resolved_executable": "C:/PRIVATE_TOOL/pdflatex.exe"}
        document = public_guard.public_capture_receipt(raw(private))
        data = public_guard.canonical_public_capture_bytes(document)
        rows.append({"path": f"tex-process-tree/launch-{number + 1:06d}.json", "bytes": len(data), "sha256": v.identity(data)["sha256"],
                     "raw_text": data.decode(), "receipt": document})
    return {"schema": "unofficial-ai-integrated-stacks-tex-process-tree-build/v1", "guard": guard,
            "launch_count": len(rows), "launches": rows}


capture_check = public_guard.validate_public_capture_receipt


def rebind_capture(row):
    data = (json.dumps(row["receipt"], sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode()
    row.update(raw_text=data.decode(), bytes=len(data), sha256=v.identity(data)["sha256"])


class MemoryObjects:
    root = Path("fixture-only")
    def __init__(self):
        self.files = {}
        self.revisions = {}
        self.head = "3" * 40
    def ident(self, revision, path):
        return v.identity(self.blob(revision, path))
    def blob(self, revision, path):
        return self.revisions.get(revision, {}).get(path, self.files[path])
    def clean(self, path):
        return self.files[path]
    def document(self, path):
        return v.parse_json(self.clean(path)), self.clean(path)
    def commit(self, value):
        v.require(isinstance(value, str) and len(value) == 40, "bad fixture commit")
        return value
    def tree(self, commit, expected):
        v.require(expected == "4" * 40, "bad fixture tree")
    def linear(self, base, head):
        pass
    def text(self, *args):
        if args == ("rev-parse", "HEAD"):
            return self.head
        if args[0] == "rev-parse" and str(args[1]).startswith("refs/tags/"):
            return "1" * 40
        raise AssertionError(args)
    def build_inputs(self, commit, stems):
        return {"preamble.tex", "chapters.tex", "my.bib", "some.sty", *(s + ".tex" for s in stems)}


class Fixture:
    def __init__(self):
        self.objects = MemoryObjects()
        self.stems = ("schemes", "groupoids")
        self.affected = ("groupoids",)
        self.binding = {"schema": v.SCHEMA, "receipt": v.COMPOSITION, "receipt_sha256": "A" * 64,
                        "receipt_git_blob": "a" * 40, "composition_source_commit": "0" * 40,
                        "registry_cutoff_commit": "8" * 40, "last_admitted_overlay": "stacks-errata-a04446e-r48",
                        "new_overlay_ids": ["stacks-errata-a04446e-r48"], "new_overlays": [],
                        "registered_overlays": 49, "registered_stable_ids": 2000,
                        "required_build_stems": list(self.stems), "direct_validation_tools": {},
                        "authority_commit": v.AUTHORITY, "authority_tree": v.AUTHORITY_TREE}
        for path in set(v.TOOLS) | set(v.SURFACE) | self.objects.build_inputs("HEAD", self.stems):
            self.objects.files[path] = (path + " fixture\n").encode()
        for name in ("overlays", "leases"):
            path = "ai-integrated/registry/" + name + ".json"
            self.objects.files[path] = raw({"fixture": name})
            self.binding[f"registry_{name}_path"] = path
            for key in ("git_blob", "sha256"):
                self.binding[f"registry_{name}_{key}"] = self.objects.ident("HEAD", path)[key]
        for path in v.TOOLS:
            self.binding["direct_validation_tools"][path] = self.objects.ident("HEAD", path)
        self.objects.files[v.COMPOSITION] = raw({"schema": v.SCHEMA, "status": "PASS"})
        c = self.objects.ident("HEAD", v.COMPOSITION)
        self.binding["receipt_sha256"], self.binding["receipt_git_blob"] = c["sha256"], c["git_blob"]
        cp_path = "validation/ega-i-6.6.4-source-checkpoint-2026-08-31.json"
        self.objects.files[cp_path] = raw({"fixture": "canonical checkpoint"})
        source = {"commit": "1" * 40, "tree": "4" * 40}
        checkpoint = {"schema": "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-successor/v1",
                      "status": "PASS_SOURCE_CHECKPOINT_SUCCESSOR", "receipt": ref(cp_path, self.objects.files[cp_path]),
                      "post_content": {"head_commit": source["commit"], "head_tree": source["tree"]},
                      "protected_input_count": 1, "protected_input_roles": {"fixture": 1},
                      "protected_input_tuple_sha256": "C" * 64,
                      "canonical_composition": {"path": v.COMPOSITION, "git_blob": c["git_blob"],
                                                "sha256": c["sha256"], "composition_source_commit": "0" * 40}}
        self.pdfs = {s: ("%PDF-1.4\nfixture " + s + "\n%%EOF").encode() for s in self.stems}
        artifacts = [{"stem": s, "pages": 2, "bytes": len(self.pdfs[s]), "sha256": v.identity(self.pdfs[s])["sha256"],
                      "diagnostics": dict.fromkeys(v.DIAGNOSTICS, 0),
                      "external_references": {"count": 0, "sha256": "A" * 64}} for s in self.stems]
        self.first = {"schema": "unofficial-ai-integrated-stacks-fixed-point-build/v1", "status": "PASS",
                      "created_utc": "2026-09-12T10:00:51Z", "source": source,
                      "builder": {"path": "tools/build_fixed_point.py", **self.objects.ident("HEAD", "tools/build_fixed_point.py")},
                      "composition": self.binding, "environment": {"fixture": True}, "pdfs_committed": False,
                      "source_checkpoint": checkpoint, "artifacts": artifacts,
                      "build": {"strategy": "sequential-prime-bibtex-global-state-sweeps", "fixed_point_suffixes": list(v.SUFFIXES),
                                "stem_selection": "composition_receipt", "stems": list(self.stems), "chapter_count": len(self.stems),
                                "pdfinfo_readable": len(self.stems), "worktree_kind": "linked", "primary_worktree_override": False,
                                "global_fixed_point_sweep": 3, "machine_wide_tex_mutex": mutex(),
                                "diagnostics": dict.fromkeys(v.DIAGNOSTICS, 0), "artifact_tuple_set_sha256": v.tuple_hash(artifacts)}}
        guard_ref = ref("tools/tex_process_guard.py", self.objects.files["tools/tex_process_guard.py"])
        self.first["tex_process_tree"] = captures(guard_ref, "first")
        self.second = deepcopy(self.first)
        self.second["tex_process_tree"] = captures(guard_ref, "second")
        self.second["created_utc"] = "2026-09-12T10:02:51Z"
        self.second["build"]["machine_wide_tex_mutex"] = mutex(True)
        self.refs = {"composition": ref(v.COMPOSITION, self.objects.files[v.COMPOSITION]),
                     "build": ref("validation/direct-successor-build.json", raw(self.first)),
                     "second_build": ref("validation/direct-successor-second.json", raw(self.second))}
        self.visual = {"schema": "unofficial-ai-integrated-stacks-visual-qa/v1", "status": "PASS", "source": source,
                       "build_receipt": {k: self.refs["build"][k] for k in ("path", "bytes", "sha256")},
                       "scope": {"affected_chapters": list(self.affected), "full_page_render_count": 2,
                                 "full_page_contact_sheet_review_count": 2, "high_resolution_locus_pages": {"groupoids": [1]},
                                 "high_resolution_locus_page_count": 1},
                       "artifacts": {"groupoids": {k: artifacts[1][k] for k in ("pages", "bytes", "sha256")}},
                       "checks": {**dict.fromkeys(v.VISUAL_TRUE, True), **dict.fromkeys(v.VISUAL_ZERO, 0)},
                       "render_protocol": {"renderer": "Poppler pdftoppm", "full_page_dpi": 72,
                                           "high_resolution_dpi": 144, "render_intermediates_published": False}}
        self.visual["build_receipt"].update(status="PASS", global_fixed_point_sweep=3)
        self.visual["artifacts"]["groupoids"].update(pdf="groupoids.pdf", encrypted=False, pages_without_ink=0, duplicate_render_hashes=0)
        self.repro = {"schema": "unofficial-ai-integrated-stacks-clean-build-reproducibility/v1", "status": "PASS",
                      **{k: self.first[k] for k in ("source", "builder", "environment")},
                      "scope": {"admitted_errata": "R1-R48", "registry_cutoff_commit": "8" * 40,
                                "source_commit": source["commit"], "source_tree": source["tree"],
                                "composition_receipt": v.COMPOSITION, "composition_receipt_sha256": c["sha256"]},
                      "method": {"execution_model": "independent_linked_worktrees", "first_worktree_kind": "linked", "second_worktree_kind": "linked",
                                 "builder_path": self.first["builder"]["path"], "builder_git_blob": self.first["builder"]["git_blob"],
                                 "builder_sha256": self.first["builder"]["sha256"]},
                      "runs": {}, "artifacts": [{k: row[k] for k in ("stem", "pages", "bytes", "sha256")} for row in artifacts],
                      "comparison": {"chapter_count": 2, "matched_artifact_count": 2, "different_artifact_count": 0, "different_artifacts": [],
                                     "total_pages_each_run": 4, "total_pdf_bytes_each_run": sum(row["bytes"] for row in artifacts),
                                     "artifact_tuple_set_sha256_each_run": v.tuple_hash(artifacts),
                                     **dict.fromkeys(("all_artifact_identities_exactly_equal", "source_identity_equal", "builder_identity_equal",
                                                      "environment_identity_equal", "fixed_point_sweep_equal", "source_checkpoint_identity_equal"), True)}}
        for role, receipt, bound in (("first", self.first, self.refs["build"]), ("second", self.second, self.refs["second_build"])):
            self.repro["runs"][role] = {"receipt": bound["path"], "bytes": bound["bytes"], "sha256": bound["sha256"],
                                      "status": "PASS", "created_utc": receipt["created_utc"], "global_fixed_point_sweep": 3}
        self.refs["visual_qa"] = ref("validation/direct-successor-visual.json", raw(self.visual))
        self.refs["reproducibility"] = ref("validation/direct-successor-repro.json", raw(self.repro))
        self.index = {"schema": v.INDEX_SCHEMA, "status": "READY_FOR_PUBLICATION", "references": self.refs,
                      "composition_scope": {"source_commit": "0" * 40, "registry_cutoff_commit": "8" * 40,
                                            "new_overlay_ids": self.binding["new_overlay_ids"]}}
        for role, doc in (("build", self.first), ("second_build", self.second), ("visual_qa", self.visual), ("reproducibility", self.repro)):
            self.objects.files[self.refs[role]["path"]] = raw(doc)
        self.objects.files[v.INDEX] = raw(self.index)

    def build(self):
        return v.validate_build(self.objects, self.first, self.binding, self.stems, old.validate_machine_wide_tex_mutex,
                                compare.validate_source_checkpoint, lambda *args: self.first["source_checkpoint"], capture_check)

    def visual_check(self):
        return v.validate_visual(self.visual, self.refs["build"], self.first, self.first["artifacts"], self.affected)

    def repro_check(self):
        return v.validate_repro(self.repro, self.refs["build"], self.refs["second_build"], self.first, self.second,
                                self.first["artifacts"], self.binding, compare.compare_receipts)


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()

    def test_valid_full_build(self):
        self.assertEqual(len(self.f.build()), 2)

    def test_valid_visual(self):
        self.f.visual_check()

    def test_valid_reproduction_uses_real_mutex_comparator(self):
        self.f.repro_check()

    def test_missing_index_fails(self):
        del self.f.objects.files[v.INDEX]
        with self.assertRaises(KeyError):
            v.validate_index(self.f.objects, self.f.refs["build"]["path"], True)

    def test_ready_index_never_means_published(self):
        with self.assertRaisesRegex(ValueError, "not ready"):
            v.validate_index(self.f.objects, self.f.refs["build"]["path"], False)

    def test_index_valid_prepublication(self):
        _, _, docs = v.validate_index(self.f.objects, self.f.refs["build"]["path"], True)
        self.assertEqual(set(docs), set(v.CORE_ROLES))

    def test_complete_prepublication_dispatch_without_network_or_tex(self):
        modules = {
            "direct_successor_composition": SimpleNamespace(load_direct_composition=lambda *args:
                                                              (self.f.binding, self.f.stems, self.f.affected),
                                                              recheck_direct_validation_tools=lambda *args: None),
            "direct_successor_checkpoint": SimpleNamespace(validate_direct_source_checkpoint_at=lambda *args:
                                                             self.f.first["source_checkpoint"]),
        }
        with patch.dict(sys.modules, modules), patch.object(v, "Objects", return_value=self.f.objects), \
                patch.object(v, "public_json") as remote_json, patch.object(v, "public_object") as remote_object, \
                patch("sys.stdout", new=io.StringIO()) as output:
            code = v.validate_direct_release(self.f.objects.root, Path(self.f.refs["build"]["path"]), True)
        self.assertEqual(code, 0)
        self.assertIn("PASS_PRE_PUBLICATION", output.getvalue())
        self.assertNotIn("PUBLICATION_COMPLETE", output.getvalue())
        remote_json.assert_not_called(); remote_object.assert_not_called()

    def test_wrong_build_argument(self):
        with self.assertRaisesRegex(ValueError, "argument"):
            v.validate_index(self.f.objects, "validation/wrong.json", True)

    def test_hash_mismatched_receipt(self):
        self.f.objects.files[self.f.refs["visual_qa"]["path"]] += b" "
        with self.assertRaisesRegex(ValueError, "identity mismatch"):
            v.validate_index(self.f.objects, self.f.refs["build"]["path"], True)

    def test_self_referential_index_rejected(self):
        row = ref(v.INDEX, self.f.objects.files[v.INDEX])
        with self.assertRaisesRegex(ValueError, "namespace"):
            v.reference(self.f.objects, row, "release")

    def test_partial_build_rejected(self):
        self.f.first["status"] = "PASS_PARTIAL"
        with self.assertRaisesRegex(ValueError, "full fixed-point"):
            self.f.build()

    def test_single_sweep_rejected(self):
        self.f.first["build"]["global_fixed_point_sweep"] = 1
        with self.assertRaises(ValueError):
            self.f.build()

    def test_missing_mutex_rejected(self):
        self.f.first["build"].pop("machine_wide_tex_mutex")
        with self.assertRaisesRegex(ValueError, "mutex"):
            self.f.build()

    def test_boolean_count_rejected(self):
        self.f.first["artifacts"][0]["pages"] = True
        with self.assertRaisesRegex(ValueError, "integer"):
            self.f.build()

    def test_omitted_stem_rejected(self):
        self.f.first["artifacts"].pop()
        with self.assertRaisesRegex(ValueError, "coverage"):
            self.f.build()

    def test_build_binding_missing_field_rejected(self):
        self.f.first["composition"] = {"schema": v.SCHEMA}
        with self.assertRaisesRegex(ValueError, "binding mismatch"):
            self.f.build()

    def test_shared_input_drift_rejected(self):
        self.f.objects.revisions["1" * 40] = {"preamble.tex": b"old shared input"}
        with self.assertRaisesRegex(ValueError, "protected input"):
            self.f.build()

    def test_checkpoint_missing_rejected(self):
        self.f.first["source_checkpoint"] = None
        with self.assertRaisesRegex(ValueError, "source_checkpoint"):
            self.f.build()

    def test_exact_head_checkpoint_replay_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, "checkpoint replay mismatch"):
            v.validate_build(self.f.objects, self.f.first, self.f.binding, self.f.stems, old.validate_machine_wide_tex_mutex,
                             compare.validate_source_checkpoint, lambda *args: {}, capture_check)

    def test_missing_process_tree_rejected(self):
        del self.f.first["tex_process_tree"]
        with self.assertRaisesRegex(ValueError, "process-tree"):
            self.f.build()

    def test_private_raw_top_level_capture_rejected(self):
        self.f.first["tex_process_tree"]["private_raw"] = "private machine path"
        with self.assertRaisesRegex(ValueError, "process-tree"):
            self.f.build()

    def test_private_capture_path_rejected(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        for path in ("C:/Users/private-machine/launch.json", "Users/private-machine/launch.json",
                     "capture/private-machine.json", "tex-process-tree/launch-000000.json"):
            with self.subTest(path=path):
                row["path"] = path
                with self.assertRaisesRegex(ValueError, "neutral public"):
                    self.f.build()

    def test_private_capture_json_rejected_even_with_matching_hash(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        row["receipt"]["cwd"] = "C:/Users/private-machine/worktree"
        data = raw(row["receipt"])
        row.update(raw_text=data.decode(), bytes=len(data), sha256=v.identity(data)["sha256"])
        with self.assertRaisesRegex(ValueError, "fixed allowlist"):
            self.f.build()

    def test_raw_capture_schema_rejected(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        row["receipt"]["schema"] = "fixture-private-capture/v1"
        data = raw(row["receipt"])
        row.update(raw_text=data.decode(), bytes=len(data), sha256=v.identity(data)["sha256"])
        with self.assertRaisesRegex(ValueError, "public capture schema"):
            self.f.build()

    def test_private_capture_row_metadata_rejected(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        row["private_receipt_path"] = "C:/Users/private-machine/launch.json"
        with self.assertRaisesRegex(ValueError, "incomplete process-tree"):
            self.f.build()

    def test_unclosed_process_tree_rejected(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        row["receipt"]["lifecycle"]["observed_empty_tree"] = False
        data = raw(row["receipt"])
        row.update(raw_text=data.decode(), bytes=len(data), sha256=v.identity(data)["sha256"])
        with self.assertRaisesRegex(ValueError, "observed_empty_tree"):
            self.f.build()

    def test_reserialized_capture_rejected_even_with_matching_hash(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        row["raw_text"] += " "
        data = row["raw_text"].encode()
        row.update(bytes=len(data), sha256=v.identity(data)["sha256"])
        with self.assertRaisesRegex(ValueError, "noncanonical"):
            self.f.build()

    def test_repeated_private_identity_with_changed_lifecycle_rejected(self):
        rows = self.f.first["tex_process_tree"]["launches"]
        rows[1]["receipt"]["provenance"] = deepcopy(rows[0]["receipt"]["provenance"])
        rebind_capture(rows[1])
        with self.assertRaisesRegex(ValueError, "duplicate process"):
            self.f.build()

    def test_repeated_captured_root_identity_rejected(self):
        rows = self.f.first["tex_process_tree"]["launches"]
        rows[1]["receipt"]["lifecycle"]["root_identity"] = deepcopy(rows[0]["receipt"]["lifecycle"]["root_identity"])
        rebind_capture(rows[1])
        with self.assertRaisesRegex(ValueError, "duplicate process"):
            self.f.build()

    def test_unrelated_mutex_capture_rejected(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        row["receipt"]["lifecycle"].update(started_utc="2026-09-12T09:59:00Z", finished_utc="2026-09-12T09:59:01Z")
        rebind_capture(row)
        with self.assertRaisesRegex(ValueError, "owning build mutex"):
            self.f.build()

    def test_capture_finishes_after_mutex_released_rejected(self):
        row = self.f.first["tex_process_tree"]["launches"][0]
        row["receipt"]["lifecycle"]["finished_utc"] = "2026-09-12T10:00:51Z"
        rebind_capture(row)
        with self.assertRaisesRegex(ValueError, "owning build mutex"):
            self.f.build()

    def test_second_build_reused_root_with_distinct_private_hash_rejected(self):
        self.f.second["tex_process_tree"]["launches"][0]["receipt"]["lifecycle"]["root_identity"] = deepcopy(
            self.f.first["tex_process_tree"]["launches"][0]["receipt"]["lifecycle"]["root_identity"])
        with self.assertRaisesRegex(ValueError, "captured root identity"):
            self.f.repro_check()

    def test_capture_raw_hash_mismatch_rejected(self):
        self.f.first["tex_process_tree"]["launches"][0]["raw_text"] += " "
        with self.assertRaisesRegex(ValueError, "raw identity"):
            self.f.build()

    def test_duplicate_capture_rejected(self):
        rows = self.f.first["tex_process_tree"]["launches"]
        rows[1] = deepcopy(rows[0])
        with self.assertRaisesRegex(ValueError, "duplicate process"):
            self.f.build()

    def test_insufficient_capture_count_rejected(self):
        self.f.first["tex_process_tree"]["launches"].pop()
        with self.assertRaisesRegex(ValueError, "launch inventory"):
            self.f.build()

    def test_reproduction_reused_capture_trace_rejected(self):
        self.f.second["tex_process_tree"] = deepcopy(self.f.first["tex_process_tree"])
        with self.assertRaisesRegex(ValueError, "reuses process"):
            self.f.repro_check()

    def test_visual_missing_page_rejected(self):
        self.f.visual["scope"]["full_page_render_count"] = 1
        with self.assertRaisesRegex(ValueError, "coverage"):
            self.f.visual_check()

    def test_visual_out_of_bounds_locus_rejected(self):
        self.f.visual["scope"]["high_resolution_locus_pages"]["groupoids"] = [3]
        with self.assertRaisesRegex(ValueError, "locus pages"):
            self.f.visual_check()

    def test_visual_defect_rejected(self):
        self.f.visual["checks"]["broken_diagrams"] = 1
        with self.assertRaisesRegex(ValueError, "nonzero"):
            self.f.visual_check()

    def test_visual_no_actual_inspection_rejected(self):
        self.f.visual["checks"]["all_pages_manually_inspected"] = False
        with self.assertRaisesRegex(ValueError, "inspection"):
            self.f.visual_check()

    def test_reproduction_same_invocation_rejected(self):
        self.f.second["created_utc"] = self.f.first["created_utc"]
        with self.assertRaisesRegex(ValueError, "distinct invocations"):
            self.f.repro_check()

    def test_reproduction_different_environment_rejected(self):
        self.f.second["environment"]["fixture"] = False
        with self.assertRaisesRegex(ValueError, "bound state"):
            self.f.repro_check()

    def test_reproduction_mutated_summary_rejected(self):
        self.f.repro["comparison"]["different_artifact_count"] = 1
        with self.assertRaisesRegex(ValueError, "comparison mismatch"):
            self.f.repro_check()

    def test_zip_pdf_hash_exact(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as z:
            z.writestr("pdf/groupoids.pdf", self.f.pdfs["groupoids"])
        stream.seek(0)
        v.check_zip_pdfs(stream, {"pdf/groupoids.pdf": "groupoids"}, {row["stem"]: row for row in self.f.first["artifacts"]})

    def test_zip_pdf_wrong_bytes_rejected(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as z:
            z.writestr("groupoids.pdf", b"bad")
        stream.seek(0)
        with self.assertRaisesRegex(ValueError, "sized"):
            v.check_zip_pdfs(stream, {"groupoids.pdf": "groupoids"}, {row["stem"]: row for row in self.f.first["artifacts"]})

    def test_zip_unsafe_member_rejected(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as z:
            z.writestr("../evil", b"bad")
        stream.seek(0)
        with self.assertRaisesRegex(ValueError, "unsafe"):
            v.check_zip_pdfs(stream, {}, {})

    def test_json_nonfinite_duplicate_rejected(self):
        for data in (b'{"x":1,"x":2}', b'{"x":NaN}'):
            with self.assertRaises(ValueError):
                v.parse_json(data)

    def test_remote_oversize_rejected_without_network(self):
        class Response(io.BytesIO):
            pass
        with patch.object(v, "urlopen", return_value=Response(b"123")):
            with self.assertRaisesRegex(ValueError, "exceeds"):
                v.public_object("https://example.invalid", {"bytes": 2, "sha256": "A" * 64})


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.f = Fixture()
        self.objects = self.f.objects
        self.ready = deepcopy(self.f.index)
        required = {row["path"] for row in self.f.refs.values()} | set(v.TOOLS) | set(v.SURFACE)
        required.update(self.objects.build_inputs("HEAD", self.f.stems))
        required.update(self.f.binding[f"registry_{name}_path"] for name in ("overlays", "leases"))
        required.add("validation/ega-i-6.6.4-source-checkpoint-2026-08-31.json")
        rows = [ref(path, self.objects.files[path]) for path in sorted(required)]
        self.release = {"schema": v.RELEASE_SCHEMA, "status": "PUBLICATION_COMPLETE", "repository": v.REPOSITORY,
                        "default_branch": "main", "receipts": deepcopy(self.f.refs),
                        "scope": {k: self.f.binding[k] for k in ("new_overlay_ids", "registry_cutoff_commit", "registered_overlays",
                                                              "registered_stable_ids", "composition_source_commit")},
                        "content": {"commit": "1" * 40, "tree": "4" * 40}, "validation_head": {"commit": "2" * 40, "tree": "4" * 40},
                        "public_readback": {"status": "PASS", "anonymous": True, "commit": "1" * 40,
                                            "checked_paths": rows, "checked_file_count": len(rows),
                                            "checked_total_bytes": sum(row["bytes"] for row in rows)},
                        "workflow": {"run_id": 101, "name": "Unified repository validation", "head_sha": "2" * 40,
                                     "status": "completed", "conclusion": "success",
                                     "url": f"https://github.com/{v.REPOSITORY}/actions/runs/101"},
                        "github_release": {"tag": "direct-test", "id": 202, "assets": [
                            {"name": stem + ".pdf", "bytes": len(data), "sha256": v.identity(data)["sha256"], "pdf_stem": stem}
                            for stem, data in self.f.pdfs.items()]}}
        release_path = "validation/direct-successor-release.json"
        self.objects.files[release_path] = raw(self.release)
        self.f.index["references"]["release"] = ref(release_path, self.objects.files[release_path])
        self.f.index["status"] = "PUBLICATION_COMPLETE"
        self.objects.files[v.INDEX] = raw(self.f.index)
        self.objects.revisions["2" * 40] = {v.INDEX: raw(self.ready)}
        self.remote = {
            f"https://api.github.com/repos/{v.REPOSITORY}/actions/runs/101": {
                "id": 101, "head_sha": "2" * 40, "name": "Unified repository validation", "status": "completed", "conclusion": "success",
                "html_url": self.release["workflow"]["url"], "repository": {"id": v.REPOSITORY_ID}, "path": ".github/workflows/validate.yml"},
            f"https://api.github.com/repos/{v.REPOSITORY}/releases/tags/direct-test": {
                "draft": False, "tag_name": "direct-test", "id": 202, "assets": [
                    {"name": row["name"], "size": row["bytes"], "state": "uploaded",
                     "browser_download_url": f"https://github.com/{v.REPOSITORY}/releases/download/direct-test/{row['name']}"}
                    for row in self.release["github_release"]["assets"]]},
            f"https://api.github.com/repos/{v.REPOSITORY}/git/ref/tags/direct-test": {"object": {"type": "commit", "sha": "1" * 40}},
            f"https://api.github.com/repos/{v.REPOSITORY}": {"id": v.REPOSITORY_ID, "private": False, "default_branch": "main"},
            f"https://api.github.com/repos/{v.REPOSITORY}/git/ref/heads/main": {"object": {"sha": "3" * 40}}}

    def run_release(self):
        with patch.object(v, "public_json", side_effect=lambda url: self.remote[url]), patch.object(v, "public_object") as download:
            v.validate_release(self.objects, self.release, self.f.index, {}, self.f.binding, self.f.first["artifacts"])
            return download.call_args_list

    def test_public_release_full_contract(self):
        calls = self.run_release()
        urls = [call.args[0] for call in calls]
        self.assertTrue(any("/" + "3" * 40 + "/" + v.INDEX in url for url in urls))
        self.assertTrue(any("/" + "3" * 40 + "/validation/direct-successor-release.json" in url for url in urls))

    def test_ci_index_different_receipts_rejected(self):
        self.ready["references"]["build"]["sha256"] = "F" * 64
        self.objects.revisions["2" * 40][v.INDEX] = raw(self.ready)
        with self.assertRaisesRegex(ValueError, "CI did not validate"):
            self.run_release()

    def test_ci_input_reverted_later_rejected(self):
        self.objects.revisions["2" * 40]["preamble.tex"] = b"different at CI"
        with self.assertRaisesRegex(ValueError, "CI validation lineage"):
            self.run_release()

    def test_remote_tag_differs_rejected(self):
        self.remote[f"https://api.github.com/repos/{v.REPOSITORY}/git/ref/tags/direct-test"]["object"]["sha"] = "9" * 40
        with self.assertRaisesRegex(ValueError, "public tag"):
            self.run_release()

    def test_missing_asset_rejected(self):
        self.remote[f"https://api.github.com/repos/{v.REPOSITORY}/releases/tags/direct-test"]["assets"].pop()
        with self.assertRaisesRegex(ValueError, "inventory count"):
            self.run_release()

    def test_private_repository_rejected(self):
        self.remote[f"https://api.github.com/repos/{v.REPOSITORY}"]["private"] = True
        with self.assertRaisesRegex(ValueError, "public-access"):
            self.run_release()

    def test_wrong_live_main_rejected(self):
        self.remote[f"https://api.github.com/repos/{v.REPOSITORY}/git/ref/heads/main"]["object"]["sha"] = "9" * 40
        with self.assertRaisesRegex(ValueError, "public main"):
            self.run_release()


if __name__ == "__main__":
    unittest.main()
