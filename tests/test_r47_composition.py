"""Non-TeX regressions for immutable R40-R47 composition evidence."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_fixed_point as builder
import write_r47_composition_receipt as writer

# Frozen public combined-successor import. The writer's old import constant
# remains part of its historical recipe, but is not on the published lineage
# after the source-preserving rebase. Tests must not depend on local-only refs.
REGISTRY_IMPORT_FIXTURE = "3c7408047b09b6cba4c29cc37051c7276e0d4f8a"


class PublicFixtureTests(unittest.TestCase):
    def test_import_fixture_is_in_public_lineage_and_has_exact_registry(self):
        self.assertEqual(builder.git(
            ROOT, "merge-base", REGISTRY_IMPORT_FIXTURE, "HEAD"),
            REGISTRY_IMPORT_FIXTURE)
        self.assertEqual(builder.git(
            ROOT, "rev-parse", f"{REGISTRY_IMPORT_FIXTURE}:ai-integrated/registry/overlays.json"),
            "c2869b04472de311be4b6dc998a797542a453437")
        self.assertEqual(writer.REGISTRY_IMPORT,
                         "396d60f0e4aef8c11c105a24e26c5519386a9f98")


class SavedReceiptTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory(prefix="stacks-r47-receipt-test-")
        self.addCleanup(self.workspace.cleanup)
        root = Path(self.workspace.name)
        self.destinations = {
            root / "composition-current.json": {"status": "PASS", "units": [1, 2]},
            root / "r47-import-composition-receipt.json": {"status": "PASS", "operations": 177},
        }
        writer.verify_or_write_receipts(self.destinations, check_only=False)

    def test_check_only_compares_exact_saved_bytes_without_writing(self):
        expected = {path: path.read_bytes() for path in self.destinations}
        with mock.patch.object(Path, "write_bytes", side_effect=AssertionError("must not write")):
            writer.verify_or_write_receipts(self.destinations, check_only=True)
        self.assertEqual(expected, {path: path.read_bytes() for path in self.destinations})

    def test_missing_receipt_fails_without_recreating_it(self):
        missing = next(iter(self.destinations))
        missing.unlink()
        with self.assertRaisesRegex(ValueError, "missing saved composition receipt"):
            writer.verify_or_write_receipts(self.destinations, check_only=True)
        self.assertFalse(missing.exists())

    def test_stale_second_receipt_fails_without_repairing_either_file(self):
        second = list(self.destinations)[1]
        second.write_bytes(b"{}\n")
        before = {path: path.read_bytes() for path in self.destinations}
        with self.assertRaisesRegex(ValueError, "stale saved composition receipt"):
            writer.verify_or_write_receipts(self.destinations, check_only=True)
        self.assertEqual(before, {path: path.read_bytes() for path in self.destinations})

    def test_generation_is_canonical_utf8_with_one_terminal_lf(self):
        for path, value in self.destinations.items():
            self.assertEqual(
                path.read_bytes(),
                (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
            )


class BuildProfileTests(unittest.TestCase):
    def profile(self, number, explicit=True):
        return builder.required_build_profile(
            {"registry": {"last_admitted_overlay": f"stacks-errata-a04446e-r{number}"}}, explicit)

    def test_historical_profiles_remain_unchanged(self):
        self.assertEqual(self.profile(33, False), builder.LEGACY_DEFAULT_STEMS)
        self.assertEqual(self.profile(38), builder.R39_DEFAULT_STEMS)
        self.assertEqual(self.profile(39), builder.R39_DEFAULT_STEMS)
        self.assertEqual(len(self.profile(39)), 30)

    def test_new_chapters_enter_only_at_their_admitted_cutoff(self):
        self.assertEqual(self.profile(40), (*builder.R39_DEFAULT_STEMS, "descent"))
        self.assertEqual(self.profile(43), self.profile(40))
        self.assertEqual(self.profile(44)[-2:], ("descent", "perfect"))
        self.assertEqual(self.profile(47), builder.DEFAULT_STEMS)
        self.assertEqual(len(self.profile(47)), 35)
        self.assertEqual(len(set(self.profile(47))), 35)


class RegistryMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.row = writer.metadata_row(writer.R40_CLARIFICATION)
        cls.parent = cls.row["parent"]

    def verify(self, rows):
        return builder.validate_registry_metadata_chain(
            ROOT, rows, self.parent, REGISTRY_IMPORT_FIXTURE, writer.REGISTRY_CUTOFF)

    def test_exact_immutable_clarification(self):
        self.assertEqual(self.verify([self.row]), writer.R40_CLARIFICATION)

    def test_empty_chain_preserves_parent(self):
        self.assertEqual(self.verify([]), self.parent)

    def test_rejects_wrong_parent_and_tree(self):
        for field in ("parent", "tree"):
            row = copy.deepcopy(self.row)
            row[field] = "0" * 40
            with self.subTest(field=field), self.assertRaises(RuntimeError):
                self.verify([row])

    def test_rejects_wrong_bytes_hash_and_blob(self):
        for field, value in (("bytes", 1), ("sha256", "0" * 64), ("git_blob", "0" * 40)):
            row = copy.deepcopy(self.row)
            row["paths"][0][field] = value
            with self.subTest(field=field), self.assertRaises(RuntimeError):
                self.verify([row])

    def test_rejects_path_escape_and_nonreceipt_changes(self):
        for path in ("../descent.tex", "registry/overlays.json", "candidates/x.json"):
            row = copy.deepcopy(self.row)
            row["paths"][0]["path"] = path
            with self.subTest(path=path), self.assertRaisesRegex(RuntimeError, "scope"):
                self.verify([row])

    def test_rejects_duplicate_and_reordered_metadata(self):
        with self.assertRaises(RuntimeError):
            self.verify([self.row, self.row])

    def test_rejects_metadata_modification_instead_of_addition(self):
        changes = builder.committed_path_changes(ROOT, self.parent, writer.R40_CLARIFICATION)
        altered = {path: (*raw[:-1], "M") for path, raw in changes.items()}
        with mock.patch.object(builder, "committed_path_changes", return_value=altered):
            with self.assertRaisesRegex(RuntimeError, "additive"):
                self.verify([self.row])

    def test_rejects_wrong_historical_assertion_without_editing_evidence(self):
        original = builder.registry_json
        def tampered(source, commit, path):
            value = original(source, commit, path)
            if path.endswith("r40-clarification-0001.json"):
                value["review_hash_clarification"]["historical_malformed_value"] = "wrong"
            return value
        with mock.patch.object(builder, "registry_json", side_effect=tampered):
            with self.assertRaisesRegex(RuntimeError, "historical assertion"):
                self.verify([self.row])

    def test_final_successor_is_exact_and_additive(self):
        row = writer.metadata_row(writer.REGISTRY_CUTOFF)
        self.assertEqual(builder.validate_registry_metadata_chain(
            ROOT, [row], row["parent"], REGISTRY_IMPORT_FIXTURE, writer.REGISTRY_CUTOFF),
            writer.REGISTRY_CUTOFF)

    def test_rejects_metadata_changed_at_head(self):
        original = builder.verify_registry_reference
        def changed(source, commit, row):
            if commit == "HEAD":
                raise RuntimeError("changed HEAD metadata")
            return original(source, commit, row)
        with mock.patch.object(builder, "verify_registry_reference", side_effect=changed):
            with self.assertRaisesRegex(RuntimeError, "HEAD metadata"):
                self.verify([self.row])

    def test_rejects_missing_mandatory_fresh_checkout_reference(self):
        original = builder.registry_json
        row = writer.metadata_row(writer.REGISTRY_CUTOFF)
        def incomplete(source, commit, path):
            value = original(source, commit, path)
            if path.endswith("r47-fresh-checkout.json"):
                del value["candidate_manifest"]
            return value
        with mock.patch.object(builder, "registry_json", side_effect=incomplete):
            with self.assertRaisesRegex(RuntimeError, "mandatory candidate_manifest"):
                builder.validate_registry_metadata_chain(
                    ROOT, [row], row["parent"], REGISTRY_IMPORT_FIXTURE, writer.REGISTRY_CUTOFF)


class LeasedCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = "3056e01f8a2dd26f52066434d80ff2c59901dea8"
        intake = "7991a0565ba6bd2b5f6e5539fb3bff7e49bdfa98"
        candidate = "9cf902bdd891ac2bd96e5f01b25c26bc7c602c07"
        admission = "c2107a9d5f6f0644abc7af42d739ff741c9dc675"
        cls.entry = writer.document(admission, "registry/overlays.json")["registered_entries"][-1]
        prefix = "candidates/commons/stacks/errata/r42"
        manifest = writer.document(candidate, prefix + "/candidate.manifest.json")
        payloads = [{"path": row["path"], "sha256": row["sha256"]}
                    for row in manifest["builds"] if row["path"].startswith("payload/")]
        cls.overlay = {
            "id": cls.entry["id"], "lease_binding_schema": "unofficial-ai-integrated-stacks-leased-candidate/v1",
            "intake_commit": intake, "intake_parent": cls.parent, "intake_tree": writer.tree(intake),
            "candidate_commit": candidate, "candidate_commits": [candidate], "candidate_tree": writer.tree(candidate),
            "candidate_subtree": writer.git("rev-parse", f"{candidate}:{prefix}"),
            "admission_commit": admission, "admission_parent": candidate, "admission_tree": writer.tree(admission),
            "manifest_sha256": cls.entry["manifest_sha256"], "payloads": payloads,
            "payload_sha256": payloads[0]["sha256"],
            "review_receipt_sha256": writer.identity(candidate, cls.entry["review_receipt"])["sha256"],
            "lease_issue_event": "lease-event-000088", "lease_release_event": "lease-event-000089",
        }

    def verify(self, overlay):
        return builder.validate_bound_leased_candidate(
            ROOT, overlay, self.entry, self.parent, REGISTRY_IMPORT_FIXTURE, writer.REGISTRY_CUTOFF,
            self.entry["source_commit"], self.entry["source_tree"])

    def test_lease_only_intake_and_full_manifest_closure(self):
        self.assertEqual(self.verify(self.overlay), self.overlay["intake_commit"])

    def test_rejects_missing_lifecycle_evidence(self):
        overlay = copy.deepcopy(self.overlay)
        del overlay["lease_binding_schema"]
        with self.assertRaisesRegex(RuntimeError, "lifecycle evidence"):
            self.verify(overlay)

    def test_rejects_fake_candidate_chain_and_subtree(self):
        for key, value in (("candidate_commits", []), ("candidate_subtree", "0" * 40)):
            overlay = copy.deepcopy(self.overlay)
            overlay[key] = value
            with self.subTest(key=key), self.assertRaises(RuntimeError):
                self.verify(overlay)

    def test_rejects_wrong_release_identity(self):
        overlay = copy.deepcopy(self.overlay)
        overlay["lease_release_event"] = "lease-event-000088"
        with mock.patch.object(builder, "verify_registry_references"):
            with self.assertRaisesRegex(RuntimeError, "issue/release identities"):
                self.verify(overlay)

    def test_rejects_entry_writer_or_authority_that_disagrees_with_manifest(self):
        for key in ("writer", "source_commit", "source_tree"):
            entry = copy.deepcopy(self.entry)
            entry[key] = "0" * 40
            with self.subTest(key=key), mock.patch.object(builder, "verify_registry_references"):
                with self.assertRaisesRegex(RuntimeError, "writer/authority"):
                    builder.validate_bound_leased_candidate(
                        ROOT, self.overlay, entry, self.parent, REGISTRY_IMPORT_FIXTURE, writer.REGISTRY_CUTOFF,
                        self.entry["source_commit"], self.entry["source_tree"])

    def test_rejects_incomplete_manifest_build_reference(self):
        original = builder.registry_json
        def incomplete(source, commit, path):
            value = original(source, commit, path)
            if path.endswith("/candidate.manifest.json"):
                del value["builds"][0]["bytes"]
            return value
        with mock.patch.object(builder, "registry_json", side_effect=incomplete):
            with self.assertRaisesRegex(RuntimeError, "incomplete builds"):
                self.verify(self.overlay)


if __name__ == "__main__":
    unittest.main()
