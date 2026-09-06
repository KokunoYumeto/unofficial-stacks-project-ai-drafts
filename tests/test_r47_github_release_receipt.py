"""Pure local adverse tests for the bounded GitHub-only publication writer."""

import copy
from contextlib import ExitStack
import json
from pathlib import Path
import unittest
from unittest import mock

from tests.test_compare_fixed_point_builds import receipt
from tools import write_r47_github_release_receipt as writer


CONTENT = "c" * 40
METADATA = "d" * 40
TREE = "b" * 40
BUILDER_BYTES = b"# exact committed builder fixture\n"


def workflow():
    return {"name": "Unified repository validation", "head_sha": METADATA,
            "status": "completed", "conclusion": "success", "event": "push",
            "repository": {"id": writer.REPOSITORY_ID, "full_name": writer.REPOSITORY, "private": False},
            "head_commit": {"id": METADATA, "tree_id": TREE}, "id": 123, "run_attempt": 1,
            "html_url": f"https://github.com/{writer.REPOSITORY}/actions/runs/123"}


def readback():
    after = writer.identity("descent.tex", b"new source\n")
    before = writer.identity("removed.txt", b"retained old source\n")
    rows = [
        {**after, "status": "modified", "readback_commit": CONTENT, "status_check": "PASS",
         "base_git_blob": "1" * 40, "head_git_blob": after["git_blob"]},
        {**before, "status": "deleted", "readback_commit": writer.PREVIOUS_PUBLIC,
         "status_check": "PASS", "base_git_blob": before["git_blob"], "head_absence_verified": True},
    ]
    changed = {"status": "PASS", "base_commit": writer.PREVIOUS_PUBLIC, "base_tree": TREE,
               "head_commit": CONTENT, "head_tree": TREE, "changed_paths": rows,
               "changed_path_count": 2, "readback_bytes": sum(row["bytes"] for row in rows),
               "changed_path_tuple_set_sha256": writer.digest(writer.canonical(rows))}
    return {"schema": "unofficial-stacks-github-source-readback/v1", "status": "PASS",
            "authentication": "none", "checked_utc": "2026-09-06T23:00:00Z",
            "github": {"repository": writer.REPOSITORY, "repository_id": writer.REPOSITORY_ID,
                       "repository_public": True, "default_branch": "main", "main_head": METADATA,
                       "main_tree": TREE}, "changed_path_readback": changed}


def refresh_listing(value):
    rows = value["changed_path_readback"]["changed_paths"]
    value["changed_path_readback"].update({"changed_path_count": len(rows),
                                         "readback_bytes": sum(row["bytes"] for row in rows),
                                         "changed_path_tuple_set_sha256": writer.digest(writer.canonical(rows))})


def core():
    evidence = {"build": receipt(), "second": receipt(11, abandoned=True)}
    ids = {key: writer.identity(path, (key + " evidence\n").encode()) for key, path in writer.PATHS.items()}
    stems = ["descent", "groupoids", "more-groupoids", "perfect", "topologies"] + [f"other{i}" for i in range(30)]
    artifacts = [{"stem": stem, "pages": 2, "bytes": 100, "sha256": "2" * 64} for stem in stems]
    tuple_sha = writer.digest(("\n".join("|".join(str(row[key]) for key in ("stem", "pages", "bytes", "sha256"))
                                           for row in sorted(artifacts, key=lambda row: row["stem"])) + "\n").encode())
    for key in ("build", "second"):
        value = evidence[key]
        value["builder"] = {k: v for k, v in writer.identity("tools/build_fixed_point.py", BUILDER_BYTES).items() if k != "bytes"}
        value["composition"].update({"receipt_sha256": ids["composition"]["sha256"],
                                     "receipt_git_blob": ids["composition"]["git_blob"],
                                     "registry_cutoff_commit": writer.CUTOFF})
        value["source_checkpoint"]["canonical_composition"].update({
            "sha256": ids["composition"]["sha256"], "git_blob": ids["composition"]["git_blob"]})
        value["artifacts"] = copy.deepcopy(artifacts)
        value["build"]["artifact_tuple_set_sha256"] = tuple_sha
        value["build"]["stems"] = stems
    evidence["composition"] = {"schema": "unofficial-ai-integrated-stacks-composition/v3", "status": "PASS",
        "composition": {"source_commit": writer.SOURCE_HEAD, "new_operations": 177, "new_byte_edit_operations": 177,
                        "affected_sources": {stem + ".tex": {} for stem in stems[:5]}},
        "registry": {"cutoff_commit": writer.CUTOFF}, "previous_cutoff": {"public_main_head": writer.PREVIOUS_PUBLIC},
        "new_overlays": [{"id": value} for value in writer.OVERLAYS], "required_build_stems": stems}
    build = evidence["build"]
    evidence["visual"] = {"status": "PASS", "source": copy.deepcopy(build["source"]),
        "build_receipt": {key: ids["build"][key] for key in ("path", "bytes", "sha256")}
                         | {"status": "PASS", "global_fixed_point_sweep": 4},
        "scope": {"affected_chapters": sorted(stems[:5]), "full_page_render_count": 10,
                  "full_page_contact_sheet_review_count": 10, "accepted_operation_count": 177,
                  "applied_byte_edit_count": 177, "historical_noop_operation_count": 0},
        "checks": {key: 0 for key in writer.DEFECT_KEYS}
                  | {key: True for key in ("all_pages_rendered", "all_pages_manually_inspected",
                        "all_manifest_bound_locus_pages_inspected_at_high_resolution", "page_dimensions_consistent",
                        "headers_and_page_numbers_consistent", "text_and_formulas_legible", "diagrams_intact")}}
    comparison = {"chapter_count": 35, "matched_artifact_count": 35, "different_artifact_count": 0,
                  "different_artifacts": [], "total_pages_each_run": 70, "total_pdf_bytes_each_run": 3500,
                  "artifact_tuple_set_sha256_each_run": tuple_sha,
                  **{key: True for key in ("all_artifact_identities_exactly_equal", "source_identity_equal",
                      "builder_identity_equal", "environment_identity_equal", "fixed_point_sweep_equal",
                      "source_checkpoint_identity_equal")}}
    runs = {}
    for key, evidence_key in (("first", "build"), ("second", "second")):
        runs[key] = {"receipt": ids[evidence_key]["path"], "created_utc": evidence[evidence_key]["created_utc"],
                     "bytes": ids[evidence_key]["bytes"], "sha256": ids[evidence_key]["sha256"],
                     "status": "PASS", "global_fixed_point_sweep": 4}
    evidence["repro"] = {"status": "PASS", **{key: copy.deepcopy(build[key]) for key in ("source", "builder", "environment")},
                         "runs": runs, "artifacts": copy.deepcopy(artifacts), "comparison": comparison}
    evidence["independent"] = {"status": "PASS_WITH_SEPARATE_RETAINED_INHERITED_FINDINGS",
        "scope": {"composed_source_commit": writer.SOURCE_HEAD, "composed_source_tree": TREE},
        "checks": {key: "PASS" for key in ("import_transport", "manifest_schema_and_closure",
              "independent_replay_of_177_introduced_operations", "all_non_operation_parent_bytes_preserved",
              "prior_cumulative_differences_preserved", "targeted_mathematical_changes_reviewed")}
              | {"introduced_defects_found": 0}}
    return evidence, ids


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tree = mock.patch.object(writer, "tree", return_value=TREE).start()
        self.delta = mock.patch.object(writer, "delta", return_value={}).start()
        self.addCleanup(mock.patch.stopall)

    def test_exact_workflow_passes(self):
        self.assertEqual(writer.validate_workflow(workflow(), METADATA)["head_sha"], METADATA)

    def test_workflow_adverse_identity_status_and_fake_run_fail(self):
        cases = [("head_sha", CONTENT), ("status", "in_progress"), ("conclusion", "failure"),
                 ("event", "pull_request"), ("id", True), ("run_attempt", 0),
                 ("html_url", "https://example.org/fake"), ("name", "Unrelated workflow")]
        for key, value in cases:
            with self.subTest(key=key):
                item = workflow()
                item[key] = value
                with self.assertRaises(ValueError):
                    writer.validate_workflow(item, METADATA)
        for key, value in (("private", True), ("id", 123), ("full_name", "other/repo")):
            with self.subTest(repository=key):
                item = workflow()
                item["repository"][key] = value
                with self.assertRaises(ValueError):
                    writer.validate_workflow(item, METADATA)
        item = workflow()
        item["head_commit"]["tree_id"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "tree"):
            writer.validate_workflow(item, METADATA)

    def check_readback(self, value=None, decisive=None):
        item = readback()
        rows = item["changed_path_readback"]["changed_paths"]
        expected = {"descent.tex": ("modified", "1" * 40, rows[0]["git_blob"]),
                    "removed.txt": ("deleted", rows[1]["git_blob"], "0" * 40)}
        with mock.patch.object(writer, "delta", return_value=expected), mock.patch.object(writer, "blob",
                side_effect=lambda revision, path: b"new source\n" if path == "descent.tex" else b"retained old source\n"):
            return writer.validate_readback(value or item, CONTENT, METADATA, decisive or {"descent.tex"})

    def test_complete_anonymous_readback_passes(self):
        kept, deleted = self.check_readback()
        self.assertEqual([row["path"] for row in kept], ["descent.tex"])
        self.assertEqual([row["path"] for row in deleted], ["removed.txt"])

    def test_sample_not_complete_delta_fails_even_with_rehashed_totals(self):
        item = readback()
        item["changed_path_readback"]["changed_paths"].pop()
        refresh_listing(item)
        with self.assertRaisesRegex(ValueError, "omits changed"):
            self.check_readback(item)

    def test_duplicate_path_fails(self):
        item = readback()
        item["changed_path_readback"]["changed_paths"].append(copy.deepcopy(item["changed_path_readback"]["changed_paths"][0]))
        refresh_listing(item)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.check_readback(item)

    def test_wrong_hash_bytes_blob_revision_status_and_boolean_bytes_fail(self):
        for key, value in (("sha256", "0" * 64), ("bytes", True), ("git_blob", "0" * 40),
                           ("head_git_blob", "0" * 40), ("base_git_blob", "0" * 40),
                           ("readback_commit", writer.PREVIOUS_PUBLIC), ("status_check", "NOT_RUN")):
            with self.subTest(key=key):
                item = readback()
                item["changed_path_readback"]["changed_paths"][0][key] = value
                refresh_listing(item)
                with self.assertRaises(ValueError):
                    self.check_readback(item)

    def test_deleted_old_bytes_do_not_prove_head_absence(self):
        item = readback()
        del item["changed_path_readback"]["changed_paths"][1]["head_absence_verified"]
        refresh_listing(item)
        with self.assertRaisesRegex(ValueError, "absent"):
            self.check_readback(item)

    def test_authentication_private_wrong_main_and_listing_digest_fail(self):
        for mutate in (lambda v: v.update(authentication="token"),
                       lambda v: v["github"].update(repository_public=False),
                       lambda v: v["github"].update(main_head=CONTENT),
                       lambda v: v["changed_path_readback"].update(base_commit=CONTENT),
                       lambda v: v["changed_path_readback"].update(changed_path_tuple_set_sha256="0" * 64),
                       lambda v: v["changed_path_readback"].update(changed_path_count=True)):
            item = readback()
            mutate(item)
            with self.assertRaises(ValueError):
                self.check_readback(item)

    def test_decisive_evidence_cannot_be_omitted(self):
        with self.assertRaisesRegex(ValueError, "decisive"):
            self.check_readback(decisive={"validation/missing-build.json"})

    def test_paths_and_duplicate_json_keys_fail(self):
        for value in ("../source.tex", "C:/source.tex", "a\\b", "/root", "a//b", ".", ""):
            with self.subTest(value=value), self.assertRaises(ValueError):
                writer.relative(value)
        for raw in (b'{"status":"FAIL","status":"PASS"}', b'{"number":NaN}', b'[]'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                writer.parse_json(raw)

    def test_core_passes_with_distinct_mutex_observations(self):
        evidence, ids = core()
        with mock.patch.object(writer, "ancestor"), mock.patch.object(writer, "blob", return_value=BUILDER_BYTES):
            artifacts, sha = writer.validate_core(evidence, ids, CONTENT)
        self.assertEqual(len(artifacts), 35)
        self.assertEqual(len(sha), 64)

    def test_core_rejects_source_registry_code_build_visual_repro_and_checkpoint_drift(self):
        mutations = [
            lambda e: e["composition"]["registry"].update(cutoff_commit="0" * 40),
            lambda e: e["composition"]["composition"].update(new_operations=176),
            lambda e: e["build"]["builder"].update(sha256="0" * 64),
            lambda e: e["build"]["source"].update(tree="0" * 40),
            lambda e: e["build"]["composition"].update(receipt_sha256="0" * 64),
            lambda e: e["second"]["build"]["machine_wide_tex_mutex"].update(release_result="not_released"),
            lambda e: e["second"].pop("source_checkpoint"),
            lambda e: e["second"]["source_checkpoint"].update(protected_input_tuple_sha256="0" * 64),
            lambda e: e["visual"]["scope"].update(full_page_contact_sheet_review_count=9),
            lambda e: e["visual"]["scope"].update(accepted_operation_count=176),
            lambda e: e["visual"]["checks"].update(clipped_content=1),
            lambda e: e["visual"]["checks"].update(all_pages_manually_inspected=False),
            lambda e: e["repro"]["comparison"].update(source_checkpoint_identity_equal=False),
            lambda e: e["repro"]["runs"]["first"].update(sha256="0" * 64),
            lambda e: e["independent"]["checks"].update(introduced_defects_found=True),
            lambda e: e["independent"]["checks"].update(targeted_mathematical_changes_reviewed="FAIL"),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                evidence, ids = core()
                mutate(evidence)
                with mock.patch.object(writer, "ancestor"), mock.patch.object(writer, "blob", return_value=BUILDER_BYTES):
                    with self.assertRaises((ValueError, KeyError)):
                        writer.validate_core(evidence, ids, CONTENT)

    def test_build_to_content_source_or_code_change_fails_without_rebuilding(self):
        for path in ("schemes.tex", "stacks.bib", "preamble.tex", "ega/scope.json", "tags/tags",
                     "ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json",
                     "ai-integrated/registry/overlays.json", "validation/composition-current.json",
                     "tools/compare_fixed_point_builds.py", "tools/validate_unified_repository.py"):
            with self.subTest(path=path):
                evidence, ids = core()
                with mock.patch.object(writer, "ancestor"), mock.patch.object(writer, "blob", return_value=BUILDER_BYTES), \
                     mock.patch.object(writer, "delta", return_value={path: ("modified", "1" * 40, "2" * 40)}):
                    with self.assertRaisesRegex(ValueError, "changed after the build"):
                        writer.validate_core(evidence, ids, CONTENT)

    def test_new_release_writer_and_receipts_do_not_need_a_mathematical_rebuild(self):
        evidence, ids = core()
        changes = {path: ("added", "0" * 40, "2" * 40) for path in
                   ("tools/write_r47_github_release_receipt.py", "tests/test_r47_github_release_receipt.py", writer.PATHS["build"])}
        with mock.patch.object(writer, "ancestor"), mock.patch.object(writer, "blob", return_value=BUILDER_BYTES), \
             mock.patch.object(writer, "delta", return_value=changes):
            self.assertEqual(len(writer.validate_core(evidence, ids, CONTENT)[0]), 35)

    def test_prepublication_validator_is_real_and_failure_prevents_completion(self):
        with mock.patch.object(writer, "git", return_value=METADATA.encode()), \
             mock.patch.object(writer.subprocess, "run", return_value=mock.Mock(returncode=1, stdout=b"FAIL", stderr=b"error")) as run:
            with self.assertRaisesRegex(ValueError, "pre-publication validation failed"):
                writer.validate_repository(METADATA, [])
            args = run.call_args.args[0]
            self.assertIn("--pre-publication", args)
            self.assertIn("tools/validate_unified_repository.py", args)

    def transaction(self, *, corrupt_code=False, fail_validator=False, history=False,
                    same_head_untracked_observations=False):
        """Exercise final receipt assembly; remote observation validators have independent tests."""
        metadata = CONTENT if same_head_untracked_observations else METADATA
        evidence, ids = core()
        raw = {path: (key + " evidence\n").encode() for key, path in writer.PATHS.items()}
        documents = {writer.PATHS[key]: (value, ids[key]) for key, value in evidence.items()}
        raw.update({path: ("# committed " + path + "\n").encode() for path in writer.CODE_PATHS})
        raw["tools/build_fixed_point.py"] = BUILDER_BYTES
        comp = evidence["composition"]
        entries = [{"id": "prior" + str(i), "stable_ids": [str(i)]} for i in range(40)]
        entries += [{"id": overlay, "stable_ids": [overlay]} for overlay in writer.OVERLAYS]
        for path, value in (("ai-integrated/registry/overlays.json", {"registered_entries": entries}),
                            ("ai-integrated/registry/leases.json", {"events": []})):
            raw[path] = writer.canonical(value)
            ident = writer.identity(path, raw[path])
            documents[path] = value, ident
            prefix = "overlays" if "overlays" in path else "leases"
            comp["registry"].update({prefix + "_sha256": ident["sha256"], prefix + "_git_blob": ident["git_blob"]})
        comp["registry"].update(registered_overlays=48, registered_stable_ids=48, cutoff_tree=TREE)
        for path in comp["composition"]["affected_sources"]:
            raw[path] = ("source fixture " + path).encode()
            ident = writer.identity(path, raw[path])
            comp["composition"]["affected_sources"][path] = {"composed_" + key: ident[key]
                                                              for key in ("bytes", "sha256", "git_blob")}
        evidence["visual"]["scope"]["high_resolution_locus_page_count"] = 5
        workflow_value, readback_value = workflow(), readback()
        workflow_value["head_sha"] = metadata
        workflow_value["head_commit"]["id"] = metadata
        readback_value["github"]["main_head"] = metadata
        observation_paths = {"validation/workflow.json", "validation/readback.json"}
        for path, value in (("validation/workflow.json", workflow_value), ("validation/readback.json", readback_value)):
            raw[path] = writer.canonical(value)
            documents[path] = value, writer.identity(path, raw[path])
        history_path = "validation/historical-major-release.json"
        if history:
            value = {"status": "PUBLICATION_COMPLETE", "preservation": {"status": "PUBLIC_READBACK_VERIFIED",
                "zenodo": {"record_id": 22209811, "doi": "10.5281/zenodo.22209811",
                           "concept_doi": writer.CONCEPT_DOI, "access_right": "open"}}}
            raw[history_path] = writer.canonical(value)
            documents[history_path] = value, writer.identity(history_path, raw[history_path])
        with ExitStack() as stack:
            stack.enter_context(mock.patch.object(writer, "commit", side_effect=lambda value: value))
            stack.enter_context(mock.patch.object(writer, "ancestor"))
            stack.enter_context(mock.patch.object(writer, "git", return_value=metadata.encode()))

            def load(path, revision=None):
                if same_head_untracked_observations and path in observation_paths:
                    self.assertIsNone(revision, "untracked observations must not require committed evidence")
                return documents[path]

            def blob(revision, path):
                if same_head_untracked_observations and path in observation_paths:
                    raise AssertionError("untracked observation has no Git blob in C")
                return b"drift" if corrupt_code and path == writer.CODE_PATHS[0] else raw[path]

            loads = stack.enter_context(mock.patch.object(writer, "load", side_effect=load))
            stack.enter_context(mock.patch.object(writer, "blob", side_effect=blob))
            stack.enter_context(mock.patch.object(Path, "read_bytes", autospec=True,
                side_effect=lambda path: raw[path.relative_to(writer.ROOT).as_posix()]))
            kept = [writer.identity(path, raw[path]) for path in comp["composition"]["affected_sources"]]
            stack.enter_context(mock.patch.object(writer, "validate_readback", return_value=(kept, [])))
            stack.enter_context(mock.patch.object(writer, "validate_repository",
                side_effect=ValueError("operational validation failed") if fail_validator else None,
                return_value={"status": "PASS"}))
            result = writer.create_receipt(CONTENT, metadata, "validation/workflow.json", "validation/readback.json",
                                            history_path if history else None)
            if same_head_untracked_observations:
                self.delta.assert_any_call(CONTENT, CONTENT)
                loads.assert_any_call("validation/workflow.json")
                loads.assert_any_call("validation/readback.json")
            return result

    def test_complete_local_transaction_emits_consumer_compatible_github_only_scope(self):
        result = self.transaction()
        self.assertEqual(result["status"], "PUBLICATION_COMPLETE")
        self.assertEqual(result["release"]["published_content_head"], CONTENT)
        self.assertEqual(result["workflow"]["head_sha"], result["release"]["metadata_head"])
        self.assertEqual(result["build"]["chapters"], 35)
        self.assertEqual(result["build"]["pages"], 70)
        self.assertEqual(result["visual_qa"]["defects"], 0)
        self.assertEqual(result["reproducibility"]["matched_artifacts"], 35)
        self.assertEqual(result["zenodo"]["status"], "UNCHANGED_NO_NEW_R47_VERSION")
        self.assertFalse(result["zenodo"]["new_version_created"])
        self.assertNotIn("doi", result["zenodo"])
        self.assertNotIn("tag", result["release"])
        self.assertIn("no new Zenodo", result["publication_scope"])
        self.assertIn("still requires", result["receipt_publication"])

    def test_committed_historical_milestone_is_not_mislabeled_fresh_verification(self):
        result = self.transaction(history=True)
        self.assertEqual(result["zenodo"]["last_major_milestone"]["doi"], "10.5281/zenodo.22209811")
        self.assertFalse(result["zenodo"]["current_access_reverified_by_this_writer"])
        self.assertFalse(result["zenodo"]["new_version_created"])

    def test_same_head_with_untracked_observations_is_non_circular_and_supported(self):
        result = self.transaction(same_head_untracked_observations=True)
        self.assertEqual(result["release"]["published_content_head"], CONTENT)
        self.assertEqual(result["release"]["metadata_head"], CONTENT)
        self.assertEqual(result["workflow"]["head_sha"], CONTENT)
        self.assertEqual(result["public_readback"]["commit"], CONTENT)
        self.assertEqual(result["status"], "PUBLICATION_COMPLETE")
        self.assertIn("still requires", result["receipt_publication"])

    def test_uncommitted_code_or_failed_validator_prevents_receipt(self):
        with self.assertRaisesRegex(ValueError, "uncommitted or drifting implementation"):
            self.transaction(corrupt_code=True)
        with self.assertRaisesRegex(ValueError, "operational validation failed"):
            self.transaction(fail_validator=True)

    def test_missing_and_historical_output_are_not_created_or_overwritten(self):
        with mock.patch.object(Path, "exists", return_value=True), mock.patch.object(writer, "create_receipt") as create:
            self.assertEqual(writer.main(["--content-head", CONTENT, "--metadata-head", METADATA,
                "--workflow-receipt", "validation/workflow.json", "--readback-receipt", "validation/readback.json"]), 1)
            create.assert_not_called()
        self.assertEqual(writer.OUTPUT, "validation/stacks-errata-a04446e-r47-release-2026-09-06.json")


if __name__ == "__main__":
    unittest.main()
