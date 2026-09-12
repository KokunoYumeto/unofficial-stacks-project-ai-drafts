"""Bounded fixtures only; no production worktree mutations or TeX."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import direct_successor_composition as d


def raw(value):
    return (json.dumps(value, sort_keys=True) + "\n").encode()


class FixtureGit:
    def __init__(self):
        self.root = Path("fixture-only")
        self.commits = {}
        self.parent_map = {}
        self.head = None

    def add(self, name, parent, updates):
        snapshot = dict(self.commits.get(parent, {}))
        for path, value in updates.items():
            if value is None:
                snapshot.pop(path, None)
            else:
                snapshot[path] = value if isinstance(value, bytes) else raw(value)
        self.commits[name], self.parent_map[name], self.head = snapshot, ([] if parent is None else [parent]), name
        return name

    def blob(self, commit, path):
        return self.commits[commit][path]

    def document(self, commit, path):
        return d.parse_json(self.blob(commit, path))

    def ident(self, commit, path):
        return d.identity(self.blob(commit, path))

    def tree(self, commit):
        return hashlib.sha1(raw({p: d.identity(b)["git_blob"] for p, b in self.commits[commit].items()})).hexdigest()

    def parents(self, commit):
        return self.parent_map[commit]

    def linear(self, base, head):
        result, cursor = [], head
        while cursor != base:
            d.require(len(self.parents(cursor)) == 1, "nonlinear or skipped commit")
            result.insert(0, cursor)
            cursor = self.parents(cursor)[0]
        return result

    def changes(self, before, after):
        old, new = self.commits[before], self.commits[after]
        result = {}
        for path in sorted(set(old) | set(new)):
            if old.get(path) != new.get(path):
                result[path] = ("100644" if path in old else "000000",
                                "100644" if path in new else "000000",
                                d.identity(old[path])["git_blob"] if path in old else "0" * 40,
                                d.identity(new[path])["git_blob"] if path in new else "0" * 40,
                                "M" if path in old and path in new else "A" if path in new else "D")
        return result

    def text(self, *args):
        if args == ("rev-parse", "HEAD"):
            return self.head
        if args[:3] == ("ls-tree", "-d", "--name-only"):
            return "fac\nillusie"
        if args[:3] == ("show", "-s", "--format=%ct"):
            return "1785270512"
        if args[:1] == ("rev-parse",):
            commit, path = args[1].split(":", 1)
            values = {p[len(path)+1:]: d.identity(data)["git_blob"]
                      for p, data in self.commits[commit].items() if p.startswith(path + "/")}
            return hashlib.sha1(raw(values)).hexdigest()
        raise AssertionError(args)

    def commit(self, value):
        d.require(value in self.commits, "missing fixture commit")
        return value

    def clean_file(self, commit, path, exact=False):
        d.require(self.blob(commit, path) == self.blob(self.head, path), "fixture working file differs")

    def raw(self, *args, data=None):
        if args[:2] == ("merge-base", "--is-ancestor"):
            self.linear(args[2], args[3])
            return b""
        raise AssertionError(args)


class DirectFixture:
    def __init__(self):
        self.git = FixtureGit()
        self.authority = {"commit": "a" * 40, "tree": "b" * 40}
        self.namespace = "commons/stacks/errata/r48"
        self.directory = "ai-integrated/candidates/" + self.namespace
        self.entry = {"id": "stacks-errata-a04446e-r48", "namespace": self.namespace,
                      "writer": "fixture-writer", "source_commit": "a" * 40, "source_tree": "b" * 40,
                      "stable_ids": ["fixture-unit-1"],
                      "review_receipt": "candidates/" + self.namespace + "/replay/FINAL_INDEPENDENT_REVIEW.json"}
        self.base = "1" * 40
        self.issue_commit, self.candidate, self.admission = "2" * 40, "3" * 40, "4" * 40
        self.old_registry = {"schema": "fixture-registry", "registered_entries": [{"id": "old", "stable_ids": ["old-unit"]}]}
        self.old_leases = {"schema": "fixture-leases", "events": []}
        self.git.add(self.base, None, {d.OVERLAYS: self.old_registry, d.LEASES: self.old_leases,
                                      "groupoids.tex": b"old source\n", "fac/retain": b"FAC\n", "illusie/retain": b"Illusie\n"})
        self.issue = {"event": "issued", "state": "active", "event_id": "lease-event-000001", "lease_id": "fixture-lease",
                      "namespace": self.namespace, "candidate_path": "candidates/" + self.namespace,
                      "writer_task": "fixture-writer", "upstream_commit": "a" * 40, "upstream_tree": "b" * 40,
                      "writer_contract": "candidates/CONTRACT.md"}
        issued = {**self.old_leases, "events": [self.issue]}
        lease_document = {"schema": "mathematics-commons-stacks-candidate-lease/v1", "lease_event": self.issue["event_id"],
                          "lease_id": self.issue["lease_id"], "namespace": self.namespace,
                          "candidate_path": self.issue["candidate_path"], "writer_task": self.issue["writer_task"],
                          "status": "active", "authority_commit": self.authority["commit"], "authority_tree": self.authority["tree"]}
        self.git.add(self.issue_commit, self.base, {d.LEASES: issued, self.directory + "/LEASE.json": lease_document})
        self.review = {"schema": "stacks-r48-final-independent-review/v1", "candidate_id": self.entry["id"], "passed": True,
                       "identity_replay": {"stable_ids": self.entry["stable_ids"], "stable_ids_unique": True, "operation_ids_unique": True},
                       "source_replay": {"operations": 1, "exact_preimages": 1, "semantic_units": 1, "nonoverlapping": True,
                                         "descending_byte_replay_payload_exact": True, "unlisted_byte_changes": 0}}
        files = {"payload/groupoids.tex": b"new source\n", "authority/source/groupoids.tex": b"old source\n",
                 "source-map.jsonl": b"fixture map\n", "decisions.jsonl": b"{}\n", "rejections.jsonl": b"",
                 "stable-units.json": b"[]\n", "formula-diagram-inventory.json": b"[]\n",
                 "operation-spec.json": b"{}\n", "replay/FINAL_INDEPENDENT_REVIEW.json": raw(self.review)}
        refs = {path: {"path": path, "bytes": len(value), "sha256": d.identity(value)["sha256"]} for path, value in files.items()}
        self.manifest = {"candidate_id": self.entry["id"], "namespace": self.namespace, "writer_task": "fixture-writer",
                         "lease_id": "fixture-lease", "upstream": self.authority, "review_state": "performed", "independent_replay": "passed",
                         "source_closure": {"complete": True, "enumerated": True, "expected_units": 1, "manifested_units": 1},
                         "builds": [refs[p] for p in ("payload/groupoids.tex", "operation-spec.json", "replay/FINAL_INDEPENDENT_REVIEW.json")],
                         "source_authorities": [refs["authority/source/groupoids.tex"]],
                         "source_map": refs["source-map.jsonl"], "decision_ledger": refs["decisions.jsonl"],
                         "rejection_ledger": refs["rejections.jsonl"], "stable_unit_manifest": refs["stable-units.json"],
                         "formula_diagram_inventory": refs["formula-diagram-inventory.json"]}
        files["candidate.manifest.json"] = raw(self.manifest)
        self.git.add(self.candidate, self.issue_commit, {self.directory + "/" + p: b for p, b in files.items()})
        self.entry["manifest_sha256"] = d.identity(files["candidate.manifest.json"])["sha256"]
        self.release = {**self.issue, "event": "released", "state": "released", "event_id": "lease-event-000002",
                        "supersedes_event_id": self.issue["event_id"]}
        self.receipt_path = "ai-integrated/registry/admission-receipts/r48.json"
        self.admission_receipt = {"schema": "mathematics-commons-stacks-registry-admission-receipt/v1", "status": "PASS",
                                  "candidate_id": self.entry["id"], "candidate_commit": self.candidate,
                                  "candidate_tree": self.git.tree(self.candidate),
                                  "manifest": {"path": "candidate.manifest.json", "bytes": len(files["candidate.manifest.json"]),
                                               "sha256": self.entry["manifest_sha256"]},
                                  "operation_spec": refs["operation-spec.json"], "source_map": refs["source-map.jsonl"],
                                  "final_review": refs["replay/FINAL_INDEPENDENT_REVIEW.json"],
                                  "stable_ids": self.entry["stable_ids"], "stable_id_count": 1,
                                  "fresh_replay": {"passed": True, "exact_preimages_descending_byte_replay": True, "operations": 1}}
        self.git.add(self.admission, self.candidate,
                     {d.OVERLAYS: {**self.old_registry, "registered_entries": self.old_registry["registered_entries"] + [self.entry]},
                      d.LEASES: {**issued, "events": [self.issue, self.release]}, self.receipt_path: self.admission_receipt})
        self.inventory = {self.entry["id"]: {"operations": 1}}

    def run(self):
        return d.derive_direct_lifecycle(self.git, self.base, self.admission, [self.entry], self.inventory, self.authority)

    def mutate_json(self, commit, path, fn):
        document = self.git.document(commit, path)
        fn(document)
        self.git.commits[commit][path] = raw(document)


class DirectLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.f = DirectFixture()

    def test_valid_direct_chain_has_no_import_fields(self):
        transport, overlays = self.f.run()
        self.assertEqual(transport["kind"], "embedded_direct")
        self.assertEqual([r["kind"] for r in transport["commits"]], ["lease_issue", "candidate", "admission"])
        self.assertEqual(overlays[0]["operations"], 1)
        self.assertNotIn("linear_import_commit", json.dumps(transport))
        self.assertTrue(all(p["path"].startswith("ai-integrated/") for r in transport["commits"] for p in r["paths"]))

    def test_no_admission_fails(self):
        self.f.admission = self.f.candidate
        with self.assertRaisesRegex(ValueError, "admission commit missing"):
            self.f.run()

    def test_root_edit_at_issue_rejected(self):
        self.f.git.commits[self.f.issue_commit]["groupoids.tex"] = b"modified\n"
        with self.assertRaisesRegex(ValueError, "lease scope"):
            self.f.run()

    def test_other_candidate_namespace_rejected(self):
        self.f.git.commits[self.f.candidate]["ai-integrated/candidates/other/file"] = b"bad"
        with self.assertRaisesRegex(ValueError, "candidate namespace"):
            self.f.run()

    def test_delete_candidate_file_rejected(self):
        self.f.git.commits[self.f.candidate].pop(self.f.directory + "/LEASE.json")
        with self.assertRaisesRegex(ValueError, "deletion"):
            self.f.run()

    def test_manifest_hash_tamper_rejected(self):
        self.f.entry["manifest_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "manifest hash"):
            self.f.run()

    def test_reference_tamper_rejected(self):
        self.f.git.commits[self.f.candidate][self.f.directory + "/payload/groupoids.tex"] = b"tamper"
        with self.assertRaisesRegex(ValueError, "reference identity"):
            self.f.run()

    def test_registry_prefix_rewrite_rejected(self):
        self.f.mutate_json(self.f.admission, d.OVERLAYS, lambda x: x["registered_entries"][0].update({"id": "rewritten"}))
        with self.assertRaisesRegex(ValueError, "registered_entries append"):
            self.f.run()

    def test_lease_history_rewrite_rejected(self):
        self.f.mutate_json(self.f.admission, d.LEASES, lambda x: x["events"][0].update({"state": "rewritten"}))
        with self.assertRaisesRegex(ValueError, "events append"):
            self.f.run()

    def test_release_supersession_rejected(self):
        self.f.mutate_json(self.f.admission, d.LEASES, lambda x: x["events"][-1].update({"supersedes_event_id": "wrong"}))
        with self.assertRaisesRegex(ValueError, "event binding"):
            self.f.run()

    def test_candidate_mutation_in_admission_rejected(self):
        self.f.git.commits[self.f.admission][self.f.directory + "/payload/groupoids.tex"] = b"changed"
        with self.assertRaisesRegex(ValueError, "registry-only scope"):
            self.f.run()

    def test_new_root_at_admission_rejected(self):
        self.f.git.commits[self.f.admission]["new.tex"] = b"new"
        with self.assertRaisesRegex(ValueError, "registry-only scope"):
            self.f.run()

    def test_admission_receipt_wrong_tree_rejected(self):
        self.f.mutate_json(self.f.admission, self.f.receipt_path, lambda x: x.update({"candidate_tree": "0" * 40}))
        with self.assertRaisesRegex(ValueError, "candidate binding"):
            self.f.run()

    def test_admission_receipt_wrong_count_rejected(self):
        self.f.mutate_json(self.f.admission, self.f.receipt_path, lambda x: x["fresh_replay"].update({"operations": 2}))
        with self.assertRaisesRegex(ValueError, "count/state"):
            self.f.run()

    def test_boolean_count_rejected(self):
        self.f.mutate_json(self.f.admission, self.f.receipt_path, lambda x: x.update({"stable_id_count": True}))
        with self.assertRaisesRegex(ValueError, "invalid integer"):
            self.f.run()

    def test_review_path_escape_rejected(self):
        self.f.entry["review_receipt"] = "candidates/other/review.json"
        self.f.mutate_json(self.f.admission, d.OVERLAYS, lambda x: x["registered_entries"][-1].update(self.f.entry))
        with self.assertRaisesRegex(ValueError, "review escapes"):
            self.f.run()

    def test_merge_rejected(self):
        self.f.git.parent_map[self.f.candidate].append(self.f.base)
        with self.assertRaisesRegex(ValueError, "nonlinear"):
            self.f.run()

    def test_post_admission_unconsumed_commit_rejected(self):
        extra = "5" * 40
        self.f.git.add(extra, self.f.admission, {"ai-integrated/registry/admission-receipts/extra.json": {}})
        self.f.admission = extra
        with self.assertRaisesRegex(ValueError, "unconsumed registry"):
            self.f.run()

    def test_authority_mismatch_rejected(self):
        self.f.authority = {"commit": "c" * 40, "tree": "b" * 40}
        with self.assertRaisesRegex(ValueError, "authority mismatch"):
            self.f.run()

    def test_multiple_candidate_commits_supported(self):
        middle = "6" * 40
        original = self.f.git.commits[self.f.candidate]
        self.f.git.add(middle, self.f.issue_commit, {self.f.directory + "/scratch.json": {"retained": True}})
        original[self.f.directory + "/scratch.json"] = raw({"retained": True})
        self.f.git.parent_map[self.f.candidate] = [middle]
        self.f.git.commits[self.f.admission][self.f.directory + "/scratch.json"] = raw({"retained": True})
        self.f.mutate_json(self.f.admission, self.f.receipt_path, lambda x: x.update({"candidate_tree": self.f.git.tree(self.f.candidate)}))
        _, overlays = self.f.run()
        self.assertEqual(overlays[0]["candidate_commits"], [middle, self.f.candidate])

    def test_nonsequential_event_ids_rejected(self):
        self.f.mutate_json(self.f.admission, d.LEASES, lambda x: x["events"][-1].update({"event_id": "lease-event-000099"}))
        with self.assertRaisesRegex(ValueError, "global sequential"):
            self.f.run()

    def test_lease_document_wrong_identity_rejected(self):
        for commit in (self.f.issue_commit, self.f.candidate, self.f.admission):
            self.f.mutate_json(commit, self.f.directory + "/LEASE.json", lambda x: x.update({"lease_id": "wrong"}))
        self.f.mutate_json(self.f.admission, self.f.receipt_path, lambda x: x.update({"candidate_tree": self.f.git.tree(self.f.candidate)}))
        with self.assertRaisesRegex(ValueError, "LEASE.json is not bound"):
            self.f.run()

    def test_lease_document_mutation_after_issue_rejected(self):
        for commit in (self.f.candidate, self.f.admission):
            self.f.mutate_json(commit, self.f.directory + "/LEASE.json", lambda x: x.update({"new_field": "added"}))
        self.f.mutate_json(self.f.admission, self.f.receipt_path, lambda x: x.update({"candidate_tree": self.f.git.tree(self.f.candidate)}))
        with self.assertRaisesRegex(ValueError, "LEASE.json changed"):
            self.f.run()


class PureContractTests(unittest.TestCase):
    def test_header_changes_rejected(self):
        with self.assertRaisesRegex(ValueError, "header"):
            d.append_exact({"events": [], "version": 1}, {"events": [{}], "version": 2}, "events")

    def test_exact_append(self):
        self.assertEqual(d.append_exact({"events": [1]}, {"events": [1, 2]}, "events"), [2])

    def test_profile_inherits_order_and_only_adds_new_roots(self):
        self.assertEqual(d._helper.full_profile({"required_build_stems": ["schemes", "groupoids"]},
                                                {"spaces-perfect.tex", "groupoids.tex"}),
                         ["schemes", "groupoids", "spaces-perfect"])

    def test_source_delta_rejects_source_plus_registry(self):
        changes = {"groupoids.tex": ("100644", "100644", "a", "b", "M"), d.OVERLAYS: ("100644", "100644", "a", "b", "M")}
        with self.assertRaisesRegex(ValueError, "source delta"):
            d._helper.source_delta(changes, ["groupoids.tex"])

    def test_source_delta_rejects_deletion(self):
        with self.assertRaisesRegex(ValueError, "deletion"):
            d._helper.source_delta({"groupoids.tex": ("100644", "000000", "a", "0", "D")}, ["groupoids.tex"])

    def test_path_traversal_rejected(self):
        with self.assertRaisesRegex(ValueError, "unsafe"):
            d.safe_path("../other")

    def test_json_duplicate_keys_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            d.parse_json(b'{"a":1,"a":2}')

    def test_schema_is_not_legacy_v3_or_v4(self):
        self.assertNotEqual(d.SCHEMA, d._helper.SCHEMA)
        self.assertNotEqual(d.SCHEMA, "unofficial-ai-integrated-stacks-composition/v4")

    def test_bare_pass_review_rejected(self):
        f = DirectFixture()
        with self.assertRaisesRegex(ValueError, "type/identity/pass"):
            d.final_review_binding({"status": "PASS"}, f.entry, 1)

    def test_contradictory_pass_review_rejected(self):
        f = DirectFixture()
        with self.assertRaisesRegex(ValueError, "type/identity/pass"):
            d.final_review_binding({**f.review, "status": "PASS", "passed": False}, f.entry, 1)

    def test_review_wrong_candidate_rejected(self):
        f = DirectFixture()
        with self.assertRaisesRegex(ValueError, "type/identity/pass"):
            d.final_review_binding({**f.review, "candidate_id": "other"}, f.entry, 1)

    def test_review_missing_source_replay_rejected(self):
        f = DirectFixture()
        with self.assertRaisesRegex(ValueError, "invalid integer"):
            d.final_review_binding({**f.review, "source_replay": {}}, f.entry, 1)


class MetadataSuffixTests(unittest.TestCase):
    def setUp(self):
        self.git = FixtureGit()
        self.base = self.git.add("source", None, {"groupoids.tex": b"unchanged", "validation/historical.json": b"history"})

    def test_empty_suffix(self):
        self.assertEqual(d.validate_metadata_suffix(self.git, self.base, self.base), [])

    def test_tooling_and_new_receipt_allowed(self):
        next_commit = self.git.add("tools", self.base, {"tools/direct_successor_composition.py": b"code"})
        end = self.git.add("metadata", next_commit, {d.RECEIPT: {}, "validation/direct-successor-composition-r48.json": {}})
        self.assertEqual(len(d.validate_metadata_suffix(self.git, self.base, end)), 2)

    def test_changed_root_source_rejected(self):
        end = self.git.add("bad", self.base, {"groupoids.tex": b"changed"})
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            d.validate_metadata_suffix(self.git, self.base, end)

    def test_changed_registry_rejected(self):
        end = self.git.add("bad", self.base, {d.OVERLAYS: {}})
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            d.validate_metadata_suffix(self.git, self.base, end)

    def test_historical_receipt_rewrite_rejected(self):
        end = self.git.add("bad", self.base, {"validation/historical.json": b"rewritten"})
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            d.validate_metadata_suffix(self.git, self.base, end)

    def test_existing_direct_receipt_rewrite_rejected(self):
        first = self.git.add("new", self.base, {"validation/direct-successor-r48-build.json": {"old": True}})
        end = self.git.add("bad", first, {"validation/direct-successor-r48-build.json": {"old": False}})
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            d.validate_metadata_suffix(self.git, self.base, end)

    def test_merge_in_suffix_rejected(self):
        end = self.git.add("bad", self.base, {d.RECEIPT: {}})
        self.git.parent_map[end] = [self.base, "other"]
        with self.assertRaisesRegex(ValueError, "nonlinear"):
            d.validate_metadata_suffix(self.git, self.base, end)


class FullDeriveFixtureTests(unittest.TestCase):
    """Full writer assembly with explicitly mocked fixture projection producer.

    Real composer mathematics is covered by production, not this synthetic test.
    No fixture revision is passed off as an actual admission or public commit.
    """
    def prepare(self):
        f = DirectFixture()
        source = "5" * 40
        authority_commit = f.authority["commit"]
        f.git.commits[authority_commit] = {"groupoids.tex": b"old source\n"}
        f.git.parent_map[authority_commit] = []
        old_source = "7" * 40
        f.git.commits[old_source] = dict(f.git.commits[f.base])
        f.git.parent_map[old_source] = []
        f.git.parent_map[f.base] = [old_source]
        previous = {"schema": d._helper.SCHEMA, "status": "PASS", "authority": f.authority,
                    "registry": {"cutoff_commit": f.base, "cutoff_tree": "filled-below", "last_admitted_overlay": "old"},
                    "composition": {"source_commit": old_source, "base_commit": "8" * 40,
                                    "total_v2_operations": 2, "r1_r3_replacements": 4, "r1_tag_additions": 3},
                    "projection_verifier": {"path": d.COMPOSER, "status": "PASS", "command":
                        "python " + d.COMPOSER + " --existing-rounds 18 --target-rounds 18 19 --base-revision " + "8" * 40 + " --check-revision " + old_source},
                    "required_build_stems": ["groupoids"], "preservation": {}, "known_admitted_metadata_defects": []}
        # This is an in-memory fixture; fixed tree IDs avoid a self-referential
        # test receipt bound at its containing commit. Real Git supplies IDs.
        tree_fn = f.git.tree
        def trees(commit):
            if commit == authority_commit:
                return f.authority["tree"]
            if commit == f.base:
                return "9" * 40
            return tree_fn(commit)
        f.git.tree = trees
        previous["registry"]["cutoff_tree"] = f.git.tree(f.base)
        additions = {d.RECEIPT: raw(previous), "registry/overlays.json": raw(f.old_registry), "registry/leases.json": raw(f.old_leases),
                     d.COMPOSER: b"# mocked fixture composer\n", "tools/verify_overlay_projection.py": b"# fixture helper\n"}
        for commit in (f.base, f.issue_commit, f.candidate, f.admission):
            f.git.commits[commit].update(additions)
        f.mutate_json(f.admission, f.receipt_path, lambda x: x.update({"candidate_tree": f.git.tree(f.candidate)}))
        f.git.add(source, f.admission, {"groupoids.tex": b"new source\n"})
        inventory = {name: {"sources": {"groupoids.tex": 1}, "operations": 1, "stable_ids": 1,
                            "manifest_sha256": "0" * 64}
                     for name in ("stacks-errata-a04446e-r18", "stacks-errata-a04446e-r19", f.entry["id"])}
        inventory[f.entry["id"]]["manifest_sha256"] = f.entry["manifest_sha256"]
        overlays = [{"round": int(name.rsplit("r", 1)[1]), "overlay_id": name,
                     "manifest_sha256": values["manifest_sha256"], "stable_ids": 1,
                     "sources": {"groupoids.tex": {"operations": 1}}} for name, values in inventory.items()]
        before, after = f.git.ident(f.admission, "groupoids.tex"), f.git.ident(source, "groupoids.tex")
        source_row = {**{"before_" + k: v for k, v in before.items()}, **{"composed_" + k: v for k, v in after.items()},
                      "authority_bytes": before["bytes"], "authority_sha256": before["sha256"], "new_operations": 1,
                      "written": False, "matches_target_after": True, "preapplied_operation_ids": [], "semantic_disposition_operation_ids": []}
        projection = {"schema": "unofficial-ai-integrated-stacks-overlay-composition/v1", "status": "PASS",
                      "existing_rounds": [18, 19], "target_rounds": [18, 19, 48], "base_revision": f.admission,
                      "check_revision": source, "write_requested": False, "operations": 3, "new_operations": 1,
                      "preapplied_operation_ids": [], "semantic_dispositions": {"consumed_operation_ids": []},
                      "overlays": overlays, "sources": {"groupoids.tex": source_row}}
        # The lifecycle fixture's placeholder source map is not a real operation
        # map; substituting an empty-object line here affects only this mock test.
        original_blob = f.git.blob
        def source_map_reader(commit, path):
            if path == f.directory + "/source-map.jsonl" and commit == f.admission:
                return b'{}\n'
            return original_blob(commit, path)
        # Lifecycle closure reads the candidate, so its bound fixture map stays exact.
        f.git.blob = source_map_reader
        return f, source, inventory, projection

    def test_full_receipt_assembly_and_read_only_command(self):
        f, source, inventory, projection = self.prepare()
        result = subprocess.CompletedProcess([], 0, stdout=raw(projection), stderr=b"")
        with patch.object(d, "Git", return_value=f.git), patch.object(d._helper, "target_inventory", return_value=inventory), patch.object(d.subprocess, "run", return_value=result) as launch:
            receipt, evidence = d.derive(f.git.root, f.base, f.admission, source)
        self.assertEqual(receipt["schema"], d.SCHEMA)
        self.assertEqual(receipt["composition"]["new_operations"], 1)
        self.assertEqual(receipt["composition"]["total_v2_operations"], 3)
        self.assertEqual(receipt["required_build_stems"], ["groupoids"])
        self.assertNotIn("linear_import_commit", receipt["registry"])
        self.assertFalse(evidence["claims"]["production_validation_run"])
        self.assertEqual(set(evidence["unchanged_extension_trees"]), {"fac", "illusie"})
        command = launch.call_args.args[0]
        self.assertNotIn("--write", command)
        self.assertIn("--check-revision", command)

    def test_source_not_immediate_child_rejected(self):
        f, source, _, _ = self.prepare()
        f.git.parent_map[source] = [f.base]
        with patch.object(d, "Git", return_value=f.git), self.assertRaisesRegex(ValueError, "immediately follow"):
            d.derive(f.git.root, f.base, f.admission, source)

    def test_inherited_registry_mismatch_rejected(self):
        f, source, _, _ = self.prepare()
        f.git.commits[f.base]["registry/overlays.json"] = b"{}"
        with patch.object(d, "Git", return_value=f.git), self.assertRaisesRegex(ValueError, "historical cutoff"):
            d.derive(f.git.root, f.base, f.admission, source)

    def test_post_composer_input_mutation_rejected(self):
        f, source, inventory, projection = self.prepare()
        result = subprocess.CompletedProcess([], 0, stdout=raw(projection), stderr=b"")
        with patch.object(d, "Git", return_value=f.git), patch.object(d._helper, "target_inventory", side_effect=[inventory, {}]), patch.object(d.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(ValueError, "input inventory changed"):
                d.derive(f.git.root, f.base, f.admission, source)


class DirectLoaderTests(unittest.TestCase):
    def setup_loader(self):
        f, source, inventory, projection = FullDeriveFixtureTests().prepare()
        result = subprocess.CompletedProcess([], 0, stdout=raw(projection), stderr=b"")
        with patch.object(d, "Git", return_value=f.git), patch.object(d._helper, "target_inventory", return_value=inventory), patch.object(d.subprocess, "run", return_value=result):
            receipt, evidence = d.derive(f.git.root, f.base, f.admission, source)
        head = "f" * 40
        f.git.add(head, source, {d.RECEIPT: receipt, **{path: b"protected helper\n" for path in d.DIRECT_TOOLS}})
        f.git.root = Path.cwd().resolve()
        return f, receipt, evidence

    def test_loader_returns_typed_binding_and_full_profile(self):
        f, receipt, evidence = self.setup_loader()
        with patch.object(d, "Git", return_value=f.git), patch.object(d, "derive", return_value=(receipt, evidence)):
            binding, stems, affected = d.load_direct_composition(f.git.root)
        self.assertEqual(binding["schema"], d.SCHEMA)
        self.assertEqual(stems, ("groupoids",))
        self.assertEqual(affected, ("groupoids",))
        self.assertEqual(set(binding["direct_validation_tools"]), set(d.DIRECT_TOOLS))
        self.assertNotIn("registry_import_commit", binding)

    def test_loader_rejects_unbound_saved_profile(self):
        f, receipt, evidence = self.setup_loader()
        f.mutate_json(f.git.head, d.RECEIPT, lambda x: x.update({"required_build_stems": ["fake"]}))
        with patch.object(d, "Git", return_value=f.git), patch.object(d, "derive", return_value=(receipt, evidence)), self.assertRaisesRegex(ValueError, "freshly derived"):
            d.load_direct_composition(f.git.root)

    def test_loader_rejects_unsupported_schema(self):
        f, _, _ = self.setup_loader()
        f.mutate_json(f.git.head, d.RECEIPT, lambda x: x.update({"schema": "other"}))
        with patch.object(d, "Git", return_value=f.git), self.assertRaisesRegex(ValueError, "invalid direct"):
            d.load_direct_composition(f.git.root)

    def test_loader_rejects_noncanonical_path(self):
        f, _, _ = self.setup_loader()
        with patch.object(d, "Git", return_value=f.git), self.assertRaisesRegex(ValueError, "canonical receipt"):
            d.load_direct_composition(f.git.root, Path("validation/other.json"))

    def test_tools_recheck_rejects_drift(self):
        f, receipt, evidence = self.setup_loader()
        with patch.object(d, "Git", return_value=f.git), patch.object(d, "derive", return_value=(receipt, evidence)):
            binding, _, _ = d.load_direct_composition(f.git.root)
            f.git.commits[f.git.head][d.DIRECT_TOOLS[0]] = b"changed helper\n"
            with self.assertRaisesRegex(ValueError, "validation tools changed"):
                d.recheck_direct_validation_tools(f.git.root, binding)


class RealGitTests(unittest.TestCase):
    def test_actual_object_ancestry_and_changed_paths(self):
        with tempfile.TemporaryDirectory(prefix="direct-successor-fixture-", dir=Path(__file__).resolve().parent) as temporary:
            root = Path(temporary).resolve()
            self.assertEqual(root.parent, Path(__file__).resolve().parent)
            def git(*args):
                result = subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)
                return result.stdout.decode().strip()
            git("init", "-q")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@example.invalid")
            git("config", "core.autocrlf", "false")
            (root / "groupoids.tex").write_bytes(b"retained source\n")
            git("add", "--", "groupoids.tex")
            git("commit", "-qm", "fixture base")
            base = git("rev-parse", "HEAD")
            lease = root / d.LEASES
            lease.parent.mkdir(parents=True)
            lease.write_bytes(b'{"events":[]}\n')
            git("add", "--", d.LEASES)
            git("commit", "-qm", "fixture registry-only step")
            cutoff = git("rev-parse", "HEAD")
            (root / "groupoids.tex").write_bytes(b"corrected source\n")
            git("add", "--", "groupoids.tex")
            git("commit", "-qm", "fixture source-only step")
            source = git("rev-parse", "HEAD")
            objects = d.Git(root)
            self.assertEqual(objects.linear(base, source), [cutoff, source])
            self.assertEqual(objects.parents(source), [cutoff])
            self.assertEqual(set(objects.changes(base, cutoff)), {d.LEASES})
            d._helper.source_delta(objects.changes(cutoff, source), ["groupoids.tex"])
            self.assertEqual(objects.ident(base, "groupoids.tex"), objects.ident(cutoff, "groupoids.tex"))


class FrozenR48ReviewTests(unittest.TestCase):
    def setUp(self):
        self.entry = {"id": "stacks-errata-a04446e-r48", "stable_ids": ["fixture-only-unit"]}
        self.review = {"schema": "stacks-r48-independent-final-frozen-stage-review/v1",
            "candidate_id": self.entry["id"], "passed": True,
            "status": "PASS_FINAL_FROZEN_STAGE_WITH_DOCUMENTED_LIMITATIONS",
            "failures": [], "blocking_findings": [],
            "scope": {"actual_frozen_stage_review": True, "exact_file_set_and_hashes": True,
                      "source_forward_reverse_replay": True},
            "tests": [{"id": "source_replay", "result": "PASS", "chapters": [
                {"forward_reverse_exact": True, "operations": 1}]}],
            "bound_evidence": [{"path": "fixture-only.json", "bytes": 1, "sha256": "A" * 64}]}

    def test_typed_frozen_stage_with_preserved_limits_is_supported(self):
        d.final_review_binding(self.review, self.entry, 1)

    def test_arbitrary_pass_label_is_not_enough(self):
        self.review["status"] = "PASS"
        with self.assertRaisesRegex(ValueError, "frozen review"):
            d.final_review_binding(self.review, self.entry, 1)

    def test_blocking_findings_are_not_downgraded_to_limits(self):
        self.review["blocking_findings"] = ["fixture blocking problem"]
        with self.assertRaises(ValueError):
            d.final_review_binding(self.review, self.entry, 1)

    def test_exact_replay_count_must_match_admitted_operations(self):
        with self.assertRaisesRegex(ValueError, "all exact source operations"):
            d.final_review_binding(self.review, self.entry, 2)

    def test_review_scope_must_assert_actual_frozen_stage(self):
        self.review["scope"]["actual_frozen_stage_review"] = False
        with self.assertRaisesRegex(ValueError, "actual_frozen_stage_review"):
            d.final_review_binding(self.review, self.entry, 1)

    def test_unreviewed_other_round_cannot_claim_r48_schema(self):
        self.entry["id"] = "stacks-errata-a04446e-r49"
        self.review["candidate_id"] = self.entry["id"]
        with self.assertRaises(ValueError):
            d.final_review_binding(self.review, self.entry, 1)


if __name__ == "__main__":
    unittest.main()
