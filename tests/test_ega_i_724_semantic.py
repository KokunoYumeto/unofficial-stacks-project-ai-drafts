"""Exact EGA I7.2.1--4 evidence contracts; these do not formally prove mathematics."""
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
BASE = "66b1df8ec9457cffbfae82ae398a983a43606438"
RECEIPT = ROOT / "validation/ega-i-7.2.1-7.2.4-semantic-checkpoint-2026-09-07.json"


class Semantic724Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parsed = ast.parse((ROOT / "ega/check.py").read_text(encoding="utf-8"))
        nodes = [n for n in parsed.body if isinstance(n, ast.FunctionDef)
                 and n.name in {"i724_semantic_contract_errors", "i724_dossier_contract_errors"}]
        env = {"hashlib": hashlib, "PINNED_STACKS_COMMIT": UPSTREAM}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), "ega/check.py", "exec"), env)
        cls.verify = staticmethod(env["i724_semantic_contract_errors"])
        cls.verify_dossier = staticmethod(env["i724_dossier_contract_errors"])
        cls.frozen = json.loads(RECEIPT.read_text(encoding="utf-8"))
        cls.frozen_scope = json.loads((ROOT / "ega/scope.json").read_text(encoding="utf-8"))
        # Preserve this checkpoint's own snapshots when future appends advance.
        for key in ("statement_review_snapshot", "residual_snapshot"):
            cls.frozen_scope[key] = copy.deepcopy(cls.frozen[key])
        cls.frozen_tables = {}
        for ledger in cls.frozen["ledgers"]:
            raw = (ROOT / ledger["path"]).read_bytes()
            lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
            rows = list(csv.DictReader(io.StringIO(b"".join(lines[:ledger["final_rows"] + 1]).decode(), newline="")))
            sup = {r.get("supersedes") for r in rows if r.get("supersedes")}
            cls.frozen_tables[ledger["path"]] = [r for r in rows if r[ledger["id_field"]] not in sup]
        with (ROOT / "ega/units.csv").open(encoding="utf-8", newline="") as handle:
            cls.frozen_units = {r["unit_id"]: r for r in csv.DictReader(handle)}
        paths = {t["path"] for t in cls.frozen["pinned_targets"] + cls.frozen["negative_comparison_targets"]} | {"tags/tags"}
        cls.blobs = {p: subprocess.check_output(["git", "show", UPSTREAM + ":" + p], cwd=ROOT) for p in paths}
        cls.frozen_tags = {line.split(",", 1)[1]: line.split(",", 1)[0]
                           for line in cls.blobs["tags/tags"].decode().splitlines() if line and not line.startswith("#")}

    def setUp(self):
        self.receipt = copy.deepcopy(self.frozen)
        self.scope = copy.deepcopy(self.frozen_scope)
        self.tables = copy.deepcopy(self.frozen_tables)
        self.units = copy.deepcopy(self.frozen_units)
        self.tags = dict(self.frozen_tags)

    def errors(self):
        return self.verify(self.receipt, self.scope, self.tables, self.units,
                           lambda commit, path: self.blobs[path], self.tags)

    def mutate_both(self, path, key, identity, **changes):
        ledger = next(l for l in self.receipt["ledgers"] if l["path"] == path)
        for rows in (ledger["rows"], self.tables[path]):
            for row in rows:
                if row[key] == identity:
                    row.update(changes)

    def test_frozen_candidate_passes(self):
        self.assertEqual(self.errors(), [])

    def test_readable_derivation_is_sealed_even_against_rehashed_prose_mutation(self):
        raw = (ROOT / "ega/i724.md").read_bytes()
        expected = self.receipt["derivation_dossier"]
        self.assertEqual(self.verify_dossier(raw, expected), [])
        damaged = raw.replace(b"D_S(f)=G_m", b"D_S(f)=X")
        self.assertNotEqual(raw, damaged)
        self.assertTrue(self.verify_dossier(damaged, expected))
        rehashed = dict(expected, bytes=len(damaged),
                        sha256=hashlib.sha256(damaged).hexdigest().upper())
        self.assertTrue(self.verify_dossier(damaged, rehashed))

    def test_public_base_and_upstream_reachable_without_private_candidate(self):
        self.assertEqual(self.receipt["starting_content_commit"], BASE)
        for commit in (BASE, UPSTREAM):
            self.assertEqual(subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT).returncode, 0)

    def test_exact_base_prefix_append_and_historical_postimage(self):
        for ledger in self.receipt["ledgers"]:
            base = subprocess.check_output(["git", "show", BASE + ":" + ledger["path"]], cwd=ROOT)
            raw = (ROOT / ledger["path"]).read_bytes()
            lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
            prefix = b"".join(lines[:ledger["prefix_rows"] + 1])
            append = b"".join(lines[ledger["prefix_rows"] + 1:ledger["final_rows"] + 1])
            self.assertEqual(prefix, base)
            for block, size, digest in ((prefix, ledger["prefix_bytes"], ledger["prefix_sha256"]),
                    (append, ledger["append_bytes"], ledger["append_sha256"]),
                    (prefix + append, ledger["bytes"], ledger["sha256"])):
                self.assertEqual(len(block), size)
                self.assertEqual(hashlib.sha256(block).hexdigest().upper(), digest)

    def test_preserved_inputs_are_exact_public_base_bytes(self):
        for item in self.receipt["preserved_inputs"]:
            raw = (ROOT / item["path"]).read_bytes()
            self.assertEqual(raw, subprocess.check_output(["git", "show", BASE + ":" + item["path"]], cwd=ROOT))
            self.assertEqual(len(raw), item["bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest().upper(), item["sha256"])

    def test_all_hypothesis_domain_ownership_and_nonclaim_mutations_fail(self):
        for key, value in self.frozen["semantic_contract"].items():
            with self.subTest(key=key):
                self.receipt = copy.deepcopy(self.frozen)
                self.receipt["semantic_contract"][key] = not value if isinstance(value, bool) else "ADVERSE"
                self.assertTrue(self.errors())

    def test_each_bilingual_owner_cannot_be_omitted_truncated_or_reassigned(self):
        for lang in ("fr", "en"):
            for key in self.frozen["languages"][lang]["owned_parts"]:
                for mode in ("omit", "truncate", "rehash"):
                    with self.subTest(language=lang, key=key, mode=mode):
                        self.receipt = copy.deepcopy(self.frozen)
                        parts = self.receipt["languages"][lang]["owned_parts"]
                        if mode == "omit":
                            del parts[key]
                        elif mode == "truncate":
                            parts[key]["lf_line_end"] -= 1
                        else:
                            parts[key]["sha256"] = "0" * 64
                        self.assertTrue(self.errors())

    def test_parent_consequence_cannot_be_added_to_nested_lemma_proof(self):
        for lang, end in (("fr", 348), ("en", 206)):
            self.receipt = copy.deepcopy(self.frozen)
            parts = self.receipt["languages"][lang]["owned_parts"]
            parts["ega:I.7.2.2.1:proof"]["lf_line_end"] = end
            del parts["ega:I.7.2.2:consequence_and_transition"]
            self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.mutate_both("ega/smap.csv", "edge_id", "S001387", source_unit="ega:I.7.2.2.1:proof")
        self.assertTrue(self.errors())

    def test_next_numbered_boundary_cannot_advance_or_absorb_next_mathematics(self):
        for key, value in (("next_semantic_cursor", "ega:I.7.2.6"),
                           ("next_cursor_starts_with_numbered_environment", False)):
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt[key] = value
            self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt["languages"]["fr"]["combined"]["lf_line_end"] = 378
        self.assertTrue(self.errors())

    def test_numbered_environments_cannot_substitute_for_complete_storage_scopes(self):
        for lang in ("fr", "en"):
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt["languages"][lang]["slices"] = self.receipt["languages"][lang]["numbered_environments"]
            self.assertTrue(self.errors())

    def test_all_reviewed_rows_are_required_and_exact(self):
        for path, key, identity in (("ega/dec.csv", "decision_id", "D000355"),
                ("ega/smap.csv", "edge_id", "S001390"), ("ega/resid.csv", "residual_id", "R000902"),
                ("ega/agent.csv", "run_id", "A000276")):
            self.setUp()
            self.tables[path] = [r for r in self.tables[path] if r[key] != identity]
            self.assertTrue(self.errors())

    def test_no_invented_parent_proof_discovery_or_discovery_promotion(self):
        self.receipt["source_proof_units"].append("ega:I.7.2.2:proof")
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.units["ega:I.7.2.2"]["authority_state"] = "french_admitted"
        self.assertTrue(self.errors())
        self.units = copy.deepcopy(self.frozen_units)
        self.units["ega:I.7.2.2.1:proof"]["review_state"] = "reviewed_existing"
        self.assertTrue(self.errors())

    def test_domain_ambiguities_cannot_be_relabelled_covered_or_missing_math(self):
        for identity in ("R000893", "R000895", "R000899"):
            for status in ("covered_derived", "open_gap", "integrated_local_mirror"):
                self.setUp()
                self.mutate_both("ega/resid.csv", "residual_id", identity, status=status)
                self.assertTrue(self.errors())

    def test_existing_relative_derivations_cannot_be_relabelled_open_gaps(self):
        self.mutate_both("ega/resid.csv", "residual_id", "R000894", status="open_gap")
        self.assertTrue(self.errors())

    def test_0A1Y_cannot_be_promoted_to_literal_arbitrary_base_theorem(self):
        for changes in ({"coverage_claim": "full_statement", "relation": "equivalent"},
                        {"coverage_claim": "covered_derived"}):
            self.setUp()
            self.mutate_both("ega/smap.csv", "edge_id", "S001386", **changes)
            self.assertTrue(self.errors())

    def test_no_component_can_be_promoted_to_whole_statement_equivalence(self):
        for row in self.frozen_tables["ega/smap.csv"][-20:]:
            self.setUp()
            self.mutate_both("ega/smap.csv", "edge_id", row["edge_id"], relation="equivalent", coverage_claim="full_statement")
            self.assertTrue(self.errors())

    def test_doubled_origin_target_is_adverse_only(self):
        self.receipt["pinned_targets"].extend(self.receipt["negative_comparison_targets"])
        self.receipt["negative_comparison_targets"] = []
        self.assertTrue(self.errors())

    def test_target_hash_join_and_valid_wrong_block_tampering_fail(self):
        target = self.receipt["pinned_targets"][0]
        self.tags[target["label"]] = "0000"
        self.assertTrue(self.errors())
        self.tags = dict(self.frozen_tags)
        target["sha256"] = "0" * 64
        self.assertTrue(self.errors())
        first = self.blobs[target["path"]].split(b"\n")[0] + b"\n"
        target.update(lf_line_start=1, lf_line_end=1, bytes=len(first), sha256=hashlib.sha256(first).hexdigest().upper())
        self.assertTrue(self.errors())

    def test_french_scope_manifest_or_combined_rehash_fails(self):
        self.scope["reviewed_source_slices"]["ega:I.7.2.1"]["slice_sha256"] = "0" * 64
        self.assertTrue(self.errors())
        self.setUp()
        self.receipt["french_authority"]["manifest_file_binding"]["manifest_file_row"]["bytes"] += 1
        self.assertTrue(self.errors())
        self.setUp()
        self.receipt["languages"]["fr"]["combined"]["sha256"] = "0" * 64
        self.assertTrue(self.errors())

    def test_current_snapshot_cannot_inflate_coverage(self):
        self.scope["statement_review_snapshot"]["source_units"] += 1
        self.assertTrue(self.errors())


if __name__ == "__main__":
    unittest.main()
