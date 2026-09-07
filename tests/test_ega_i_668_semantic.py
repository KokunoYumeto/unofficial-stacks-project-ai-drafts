"""Bounded adverse tests for the three-unit EGA I 6.6.6-6.6.8 candidate."""
import ast
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "a04446e57ec1fbc252a871afcec7752fb2807b14"
CHECKPOINT = ROOT / "validation/ega-i-6.6.6-6.6.8-semantic-checkpoint-2026-09-06.json"


def load_function(name):
    parsed = ast.parse((ROOT / "ega/check.py").read_text(encoding="utf-8"))
    node = next(n for n in parsed.body if isinstance(n, ast.FunctionDef) and n.name == name)
    env = {"hashlib": hashlib, "PINNED_STACKS_COMMIT": UPSTREAM}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(ROOT / "ega/check.py"), "exec"), env)
    return env[name]


class Semantic668Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.verify = staticmethod(load_function("i668_semantic_contract_errors"))
        cls.frozen = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
        cls.frozen_scope = json.loads((ROOT / "ega/scope.json").read_text(encoding="utf-8"))
        cls.frozen_tables = {}
        for entry in cls.frozen["ledgers"]:
            with (ROOT / entry["path"]).open(encoding="utf-8", newline="") as f:
                cls.frozen_tables[entry["path"]] = list(csv.DictReader(f))
        with (ROOT / "ega/units.csv").open(encoding="utf-8", newline="") as f:
            cls.frozen_units = {r["unit_id"]: r for r in csv.DictReader(f)}
        paths = {t["path"] for t in cls.frozen["pinned_targets"]} | {"tags/tags"}
        cls.blobs = {p: subprocess.check_output(["git", "show", UPSTREAM + ":" + p], cwd=ROOT) for p in paths}
        cls.frozen_tags = {line.split(",", 1)[1]: line.split(",", 1)[0]
                           for line in cls.blobs["tags/tags"].decode().splitlines()
                           if line and not line.startswith("#")}

    def setUp(self):
        self.receipt = copy.deepcopy(self.frozen)
        self.scope = copy.deepcopy(self.frozen_scope)
        self.tables = copy.deepcopy(self.frozen_tables)
        self.units = copy.deepcopy(self.frozen_units)
        self.tags = dict(self.frozen_tags)

    def errors(self, loader=None):
        return self.verify(self.receipt, self.scope, self.tables, self.units,
                           loader or (lambda commit, path: self.blobs[path]), self.tags)

    def test_current_candidate_contract(self):
        self.assertEqual(self.errors(), [])

    def test_exact_base_prefixes_and_full_postimages(self):
        for entry in self.receipt["ledgers"]:
            with self.subTest(path=entry["path"]):
                raw = (ROOT / entry["path"]).read_bytes()
                base = subprocess.check_output(["git", "show", self.receipt["starting_content_commit"] + ":" + entry["path"]], cwd=ROOT)
                self.assertTrue(raw.startswith(base))
                self.assertEqual((len(base), hashlib.sha256(base).hexdigest().upper()), (entry["prefix_bytes"], entry["prefix_sha256"]))
                self.assertEqual((len(raw), hashlib.sha256(raw).hexdigest().upper()), (entry["bytes"], entry["sha256"]))

    def test_wrong_next_cursor_is_rejected(self):
        self.receipt["next_semantic_cursor"] = "ega:I.6.6.9"
        self.assertTrue(self.errors())

    def test_every_new_edge_is_exactly_bound(self):
        for row in self.frozen_tables["ega/smap.csv"][-24:]:
            with self.subTest(edge=row["edge_id"]):
                self.setUp()
                target = next(r for r in self.tables["ega/smap.csv"] if r["edge_id"] == row["edge_id"])
                target["evidence"] += " unproved strengthening"
                self.assertTrue(self.errors())

    def test_each_claim_family_cannot_be_removed(self):
        for unit in self.receipt["source_units"]:
            with self.subTest(unit=unit):
                self.setUp()
                self.tables["ega/smap.csv"] = [r for r in self.tables["ega/smap.csv"] if r["source_unit"] != unit]
                self.assertTrue(self.errors())

    def test_duplicate_new_source_edge_rejected(self):
        self.tables["ega/smap.csv"].append(copy.deepcopy(self.tables["ega/smap.csv"][-1]))
        self.assertTrue(self.errors())

    def test_each_residual_disposition_is_bound(self):
        for row in self.frozen_tables["ega/resid.csv"][-10:]:
            with self.subTest(residual=row["residual_id"]):
                self.setUp()
                target = next(r for r in self.tables["ega/resid.csv"] if r["residual_id"] == row["residual_id"])
                target["disposition"] = "all prior visual work complete"
                self.assertTrue(self.errors())

    def test_nonbaseline_0hct_rejected(self):
        target = next(t for t in self.receipt["pinned_targets"] if t["tag"] == "0356")
        target["tag"] = "0HCT"
        self.assertTrue(self.errors())

    def test_changed_pinned_source_rejected(self):
        self.assertTrue(self.errors(lambda commit, path: b"wrong source\n"))

    def test_wrong_official_join_rejected(self):
        target = self.receipt["pinned_targets"][0]
        self.tags[target["label"]] = "ZZZZ"
        self.assertTrue(self.errors())

    def test_discovery_promotion_rejected(self):
        self.units["ega:I.6.6.8"]["authority_state"] = "french_admitted"
        self.assertTrue(self.errors())

    def test_current_counts_cannot_use_old_frontier(self):
        self.scope["statement_review_snapshot"]["file_rows"] = 1266
        self.assertTrue(self.errors())

    def test_source_slice_cannot_be_substituted(self):
        self.scope["reviewed_source_slices"]["ega:I.6.6.8"]["slice_sha256"] = "0" * 64
        self.assertTrue(self.errors())

    def test_inactive_new_decision_rejected(self):
        self.tables["ega/dec.csv"][-1]["state"] = "inactive"
        self.assertTrue(self.errors())

    def test_audit_cannot_claim_build_or_publication(self):
        self.tables["ega/agent.csv"][-1]["writes"] = "schemes.tex"
        self.assertTrue(self.errors())

    def test_historical_665_receipt_is_immutable(self):
        history = self.receipt["historical_checkpoint"]
        raw = (ROOT / history["path"]).read_bytes()
        self.assertEqual((len(raw), hashlib.sha256(raw).hexdigest().upper()), (history["bytes"], history["sha256"]))
        previous = json.loads(raw)
        for entry in previous["ledgers"]:
            raw = (ROOT / entry["path"]).read_bytes()
            prefix = b"".join(raw.splitlines(keepends=True)[:entry["final_rows"] + 1])
            self.assertEqual((len(prefix), hashlib.sha256(prefix).hexdigest().upper()), (entry["bytes"], entry["sha256"]))


if __name__ == "__main__":
    unittest.main()
