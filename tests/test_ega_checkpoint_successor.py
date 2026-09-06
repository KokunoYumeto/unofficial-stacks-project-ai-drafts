from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import verify_ega_checkpoint_successor as successor


class AppendTests(unittest.TestCase):
    def setUp(self):
        self.before = b"id,state\nD1,active\n"
        self.after = self.before + b"D2,active\n"
        self.record = {}
        for raw, size, sha in ((self.before, "prefix_bytes", "prefix_sha256"),
                              (self.after[len(self.before):], "append_bytes", "append_sha256"),
                              (self.after, "bytes", "sha256")):
            self.record[size] = len(raw)
            self.record[sha] = hashlib.sha256(raw).hexdigest().upper()

    def test_exact_append(self):
        successor.verify_append_bytes(self.before, self.after, self.record, "ega/dec.csv")

    def test_rewritten_prefix(self):
        with self.assertRaisesRegex(RuntimeError, "rewrites prior bytes"):
            successor.verify_append_bytes(self.before, b"x" + self.after[1:], self.record, "p")

    def test_each_size_is_checked_and_bool_not_accepted(self):
        for key in ("prefix_bytes", "append_bytes", "bytes"):
            for value in (True, 0, self.record[key] + 1):
                with self.subTest(key=key, value=value):
                    row = {**self.record, key: value}
                    with self.assertRaisesRegex(RuntimeError, "semantic ledger exact"):
                        successor.verify_append_bytes(self.before, self.after, row, "p")

    def test_each_hash_is_checked(self):
        for key in ("prefix_sha256", "append_sha256", "sha256"):
            with self.subTest(key=key):
                row = {**self.record, key: "0" * 64}
                with self.assertRaisesRegex(RuntimeError, "semantic ledger exact"):
                    successor.verify_append_bytes(self.before, self.after, row, "p")

    def test_missing_binding(self):
        row = copy.deepcopy(self.record)
        del row["append_sha256"]
        with self.assertRaises(RuntimeError):
            successor.verify_append_bytes(self.before, self.after, row, "p")


class AnchorTests(unittest.TestCase):
    def setUp(self):
        self.build = mock.Mock()
        self.build.git.return_value = "anchor\nlater"
        self.path = "validation/checkpoint.json"
        self.build.committed_path_changes.return_value = {self.path: ("100644", "100644", "0"*40, "b"*40, "A")}
        self.build.committed_file_identity.return_value = {"path": self.path, "sha256": "f" * 64}

    def call(self):
        return successor.receipt_anchor(self.build, Path("repo"), "content", "head", self.path)

    def test_exact_anchor_is_first_parent_child_not_current_head(self):
        self.assertEqual(self.call(), "anchor")
        self.build.require_single_parent.assert_called_once_with(Path("repo"), "anchor", "historical receipt", "content")
        self.build.require_ancestor.assert_called_once_with(Path("repo"), "content", "historical checkpoint content", "head")

    def test_missing_receipt_child(self):
        self.build.git.return_value = ""
        with self.assertRaisesRegex(RuntimeError, "no committed receipt child"):
            self.call()

    def test_foreign_ancestry(self):
        self.build.require_ancestor.side_effect = RuntimeError("not an ancestor")
        with self.assertRaisesRegex(RuntimeError, "not an ancestor"):
            self.call()

    def test_merge_or_wrong_parent_rejected(self):
        self.build.require_single_parent.side_effect = RuntimeError("wrong parent")
        with self.assertRaisesRegex(RuntimeError, "wrong parent"):
            self.call()

    def test_unrelated_anchor_change_rejected(self):
        self.build.committed_path_changes.return_value["schemes.tex"] = ("100644", "100644", "a", "b", "M")
        with self.assertRaisesRegex(RuntimeError, "exact receipt-only child"):
            self.call()

    def test_modified_instead_of_added_receipt_rejected(self):
        self.build.committed_path_changes.return_value[self.path] = ("100644", "100644", "a", "b", "M")
        with self.assertRaisesRegex(RuntimeError, "exact receipt-only child"):
            self.call()

    def test_sealed_receipt_tampering_rejected(self):
        self.build.committed_file_identity.side_effect = [{"sha256": "old"}, {"sha256": "new"}]
        with self.assertRaisesRegex(RuntimeError, "changed in the successor"):
            self.call()


class ExecutionBoundaryTests(unittest.TestCase):
    def test_historical_execution_never_uses_pyc_loader(self):
        build = mock.Mock()
        build.EGA_PRECONTENT_TOOL_ROLES = [("tools/build_fixed_point.py", "consumer")]
        build.EGA_SOURCE_CHECKPOINT_PATH = "validation/checkpoint.json"
        build.committed_file_identity.return_value = {"bytes": 10, "sha256": "exact"}
        build.working_file_identity.return_value = {"bytes": 10, "sha256": "exact"}
        raw = b'''def committed_file_identity(*args):
    return {"git_blob": "blob", "sha256": "hash"}
def parse_json_blob(*args):
    return {"composition": {"source_commit": "source"}}
def load_source_checkpoint(*args):
    return {"post_content": {"head_commit": "anchor"}}, (), ()
def require_source_checkpoint_unchanged(*args):
    pass
'''
        with mock.patch.object(successor, "historical_worktree", return_value=Path("historical")):
            with mock.patch.object(successor, "raw_git", return_value=raw):
                with mock.patch("importlib.machinery.SourceFileLoader.exec_module",
                                side_effect=AssertionError("must not load cached bytecode")):
                    result, _ = successor.verify_historical(build, Path("repo"), "anchor")
                    self.assertEqual(result["post_content"]["head_commit"], "anchor")

    def test_no_historical_materialization_without_semantic_successor(self):
        build = mock.Mock()
        build.capture_source_revision.return_value = ("head", "tree")
        build.committed_file_identity.return_value = None
        with mock.patch.object(successor, "historical_worktree") as prepare:
            with self.assertRaisesRegex(RuntimeError, "supported committed semantic successor"):
                successor.load_successor(build, Path("repo"), "receipt", {}, {})
            prepare.assert_not_called()

    def test_modified_historical_executable_rejected_before_import(self):
        build = mock.Mock()
        build.EGA_PRECONTENT_TOOL_ROLES = [("tools/build_fixed_point.py", "consumer")]
        build.committed_file_identity.return_value = {"bytes": 10, "sha256": "expected"}
        build.working_file_identity.return_value = {"bytes": 10, "sha256": "changed"}
        with mock.patch.object(successor, "historical_worktree", return_value=Path("historical")):
            with mock.patch.object(successor.importlib.util, "spec_from_file_location") as loader:
                with self.assertRaisesRegex(RuntimeError, "bytes changed before execution"):
                    successor.verify_historical(build, Path("repo"), "anchor")
                loader.assert_not_called()

    def test_existing_foreign_directory_is_never_overwritten(self):
        with tempfile.TemporaryDirectory(prefix="ega-successor-test-") as directory:
            source = Path(directory) / "source"
            source.mkdir()
            target = Path(directory) / "source-ega664-anchor-aaaaaaaaaaaa"
            target.mkdir()
            build = mock.Mock()
            with mock.patch.object(successor, "raw_git") as git:
                with self.assertRaisesRegex(RuntimeError, "not our linked worktree"):
                    successor.historical_worktree(build, source, "a" * 40)
                git.assert_not_called()
                self.assertTrue(target.is_dir())


class SemanticContractTests(unittest.TestCase):
    def setUp(self):
        self.build = mock.Mock()
        self.build.EGA_LEDGER_CONTRACTS = [(p,) for p in (
            "ega/dec.csv", "ega/smap.csv", "ega/resid.csv", "ega/agent.csv")]
        self.scope = b"{}"
        self.semantic = {
            "schema": "ega-i-6.6.5-semantic-checkpoint/v1",
            "status": "LOCAL_SEMANTIC_VALIDATED", "source_unit": "ega:I.6.6.5",
            "next_semantic_cursor": "ega:I.6.6.6", "starting_content_commit": "baseline",
            "ledgers": [{"path": p[0]} for p in self.build.EGA_LEDGER_CONTRACTS],
            "scope_identity": {"bytes": 2, "sha256": hashlib.sha256(self.scope).hexdigest().upper()},
            "validation": {"scaffold_checker": {"result": {"status": "PASS", "errors": []}}},
        }
        self.build.committed_file_identity.return_value = {"bytes": 7, "sha256": "checker"}
        self.build.working_file_identity.return_value = {"bytes": 7, "sha256": "checker"}
        self.build.parse_json_blob.return_value = self.semantic
        self.build.git.return_value = "semantic_commit"
        self.build.commit_parents.return_value = ("source_commit",)
        self.build.require_commit_object.return_value = "baseline"
        self.build.committed_path_changes.return_value = {
            p: ("100644", "100644", "a", "b", "A" if p == successor.SEMANTIC_PATH else "M")
            for p in successor.SEMANTIC_PATHS}
        self.build.strict_json_loads.return_value = {"status": "PASS", "errors": []}

    def run_contract(self):
        with mock.patch.object(successor, "raw_git", return_value=self.scope):
            # Byte append cases are independently tested by AppendTests.
            with mock.patch.object(successor, "verify_append_bytes"):
                with mock.patch.object(successor.subprocess, "run") as execute:
                    self.execution = execute
                    execute.return_value = mock.Mock(returncode=0, stderr="", stdout=json.dumps({"status": "PASS", "errors": []}))
                    result = successor.verify_semantic(
                        self.build, Path("repo"), "head", {"composition_source_commit": "source_commit"})
                    return result

    def test_exact_semantic_contract(self):
        (binding, paths) = self.run_contract()
        self.assertEqual(binding["source_unit"], "ega:I.6.6.5")
        self.assertEqual(set(paths), successor.SEMANTIC_PATHS)

    def test_bad_schema_status_or_cursor(self):
        for key in ("schema", "status", "source_unit", "next_semantic_cursor"):
            previous = self.semantic[key]
            self.semantic[key] = "wrong"
            with self.assertRaisesRegex(RuntimeError, "unsupported or nonpassing"):
                self.run_contract()
            self.semantic[key] = previous

    def test_wrong_composition_parent(self):
        self.build.commit_parents.return_value = ("foreign_source",)
        with self.assertRaisesRegex(RuntimeError, "validated cumulative source"):
            self.run_contract()

    def test_merge_semantic_commit(self):
        self.build.commit_parents.return_value = ("source_commit", "other")
        with self.assertRaisesRegex(RuntimeError, "single-parent"):
            self.run_contract()

    def test_extra_root_change(self):
        self.build.committed_path_changes.return_value["schemes.tex"] = ("100644", "100644", "a", "b", "M")
        with self.assertRaisesRegex(RuntimeError, "exact bounded nine-path delta"):
            self.run_contract()

    def test_missing_changed_path(self):
        del self.build.committed_path_changes.return_value["ega/dec.csv"]
        with self.assertRaisesRegex(RuntimeError, "exact bounded nine-path delta"):
            self.run_contract()

    def test_scope_hash_changed(self):
        self.semantic["scope_identity"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(RuntimeError, "scope hash differs"):
            self.run_contract()

    def test_checker_bytes_rejected_before_execution(self):
        self.build.working_file_identity.return_value = {"bytes": 7, "sha256": "tampered"}
        with self.assertRaisesRegex(RuntimeError, "checker working bytes changed before execution"):
            self.run_contract()
        self.execution.assert_not_called()

    def test_checker_result_mismatch(self):
        self.build.strict_json_loads.return_value = {"status": "PASS", "errors": [], "extra": 1}
        with self.assertRaisesRegex(RuntimeError, "differs from sealed checkpoint"):
            self.run_contract()


if __name__ == "__main__":
    unittest.main()
