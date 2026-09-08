"""Evidence contracts for EGA I7.1.15-16; not a formal proof checker."""
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
RECEIPT = ROOT / "validation/ega-i-7.1.15-7.1.16-semantic-checkpoint-2026-09-07.json"


class Semantic711516Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parsed = ast.parse((ROOT / "ega/check.py").read_text(encoding="utf-8"))
        nodes = [node for node in parsed.body if isinstance(node, ast.FunctionDef)
                 and node.name == "i711516_semantic_contract_errors"]
        env = {"hashlib": hashlib, "PINNED_STACKS_COMMIT": UPSTREAM}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), "ega/check.py", "exec"), env)
        cls.verify = staticmethod(env["i711516_semantic_contract_errors"])
        cls.frozen = json.loads(RECEIPT.read_text(encoding="utf-8"))
        cls.frozen_scope = json.loads((ROOT / "ega/scope.json").read_text(encoding="utf-8"))
        for key in ("statement_review_snapshot", "residual_snapshot"):
            cls.frozen_scope[key] = copy.deepcopy(cls.frozen[key])
        cls.frozen_scope["reviewed_source_slices"].update(
            copy.deepcopy(cls.frozen["french_authority"]["source_scopes"]))
        cls.frozen_tables = {}
        for ledger in cls.frozen["ledgers"]:
            raw = (ROOT / ledger["path"]).read_bytes()
            lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
            prefix = b"".join(lines[:ledger["final_rows"] + 1])
            rows = list(csv.DictReader(io.StringIO(prefix.decode(), newline="")))
            superseded = {r.get("supersedes") for r in rows if r.get("supersedes")}
            cls.frozen_tables[ledger["path"]] = [r for r in rows if r[ledger["id_field"]] not in superseded]
        with (ROOT / "ega/units.csv").open(encoding="utf-8", newline="") as f:
            cls.frozen_units = {r["unit_id"]: r for r in csv.DictReader(f)}
        targets = cls.frozen["pinned_targets"] + cls.frozen["negative_comparison_targets"]
        paths = {t["path"] for t in targets} | {"tags/tags"}
        cls.blobs = {p: subprocess.check_output(["git", "show", UPSTREAM + ":" + p], cwd=ROOT)
                     for p in paths}
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

    def mutate_row_in_both(self, path, key, identity, **changes):
        ledger = next(l for l in self.receipt["ledgers"] if l["path"] == path)
        for rows in (ledger["rows"], self.tables[path]):
            for row in rows:
                if row[key] == identity:
                    row.update(changes)

    def test_complete_source_level_existing_coverage(self):
        self.assertEqual(self.errors(), [])

    def test_base_and_upstream_are_ancestors_not_private_candidate_dependencies(self):
        for commit in (UPSTREAM, self.receipt["starting_content_commit"]):
            result = subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT)
            self.assertEqual(result.returncode, 0)
        self.assertEqual(self.receipt["starting_content_commit"],
                         "0a5b707d0be72b497cd7d748ddfead10483bca67")

    def test_exact_base_prefix_append_and_sealed_postimage(self):
        for ledger in self.receipt["ledgers"]:
            with self.subTest(path=ledger["path"]):
                base = subprocess.check_output(["git", "show",
                    self.receipt["starting_content_commit"] + ":" + ledger["path"]], cwd=ROOT)
                raw = (ROOT / ledger["path"]).read_bytes()
                lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
                prefix = b"".join(lines[:ledger["prefix_rows"] + 1])
                append = b"".join(lines[ledger["prefix_rows"] + 1:ledger["final_rows"] + 1])
                self.assertEqual(prefix, base)
                for block, size, digest in [(prefix, ledger["prefix_bytes"], ledger["prefix_sha256"]),
                        (append, ledger["append_bytes"], ledger["append_sha256"]),
                        (prefix + append, ledger["bytes"], ledger["sha256"])]:
                    self.assertEqual(len(block), size)
                    self.assertEqual(hashlib.sha256(block).hexdigest().upper(), digest)

    def test_preserved_inputs_equal_exact_base_bytes(self):
        for item in self.receipt["preserved_inputs"]:
            raw = (ROOT / item["path"]).read_bytes()
            base = subprocess.check_output(["git", "show",
                self.receipt["starting_content_commit"] + ":" + item["path"]], cwd=ROOT)
            self.assertEqual(raw, base)
            self.assertEqual(len(raw), item["bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest().upper(), item["sha256"])

    def test_all_hypothesis_and_nonclaim_mutations_fail(self):
        for key, value in self.frozen["semantic_contract"].items():
            with self.subTest(key=key):
                self.receipt = copy.deepcopy(self.frozen)
                self.receipt["semantic_contract"][key] = not value if isinstance(value, bool) else "ADVERSE"
                self.assertTrue(self.errors())

    def test_next_cursor_includes_section_heading(self):
        self.receipt["next_cursor_starts_with_section_heading"] = False
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt["next_semantic_cursor"] = "ega:I.7.2.2"
        self.assertTrue(self.errors())

    def test_all_next_context_parts_required(self):
        for lang in ("fr", "en"):
            for key in ("heading", "labels", "boundary", "combined"):
                with self.subTest(lang=lang, key=key):
                    self.receipt = copy.deepcopy(self.frozen)
                    del self.receipt["languages"][lang]["next_excluded_context"][key]
                    self.assertTrue(self.errors())

    def test_next_heading_not_absorbed_into_sixteen(self):
        self.receipt["languages"]["fr"]["slices"]["ega:I.7.1.16"]["lf_line_end"] = 290
        self.assertTrue(self.errors())

    def test_complete_ownership_not_replaced_by_environment_only(self):
        for lang in ("fr", "en"):
            for unit in ("ega:I.7.1.15", "ega:I.7.1.16"):
                self.receipt = copy.deepcopy(self.frozen)
                source = self.receipt["languages"][lang]
                source["slices"][unit] = copy.deepcopy(source["numbered_environments"][unit])
                self.assertTrue(self.errors())

    def test_each_introduction_and_full_proof_required(self):
        for lang in ("fr", "en"):
            for owner in self.frozen["languages"][lang]["owned_parts"]:
                self.receipt = copy.deepcopy(self.frozen)
                del self.receipt["languages"][lang]["owned_parts"][owner]
                self.assertTrue(self.errors())

    def test_proof_terminal_line_cannot_be_truncated(self):
        for lang in ("fr", "en"):
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt["languages"][lang]["owned_parts"]["ega:I.7.1.15:proof"]["lf_line_end"] -= 1
            self.assertTrue(self.errors())

    def test_no_invented_sixteen_proof(self):
        self.receipt["source_proof_units"].append("ega:I.7.1.16:proof")
        self.assertTrue(self.errors())

    def test_contiguous_span_cannot_omit_intro(self):
        self.receipt["languages"]["fr"]["combined"]["lf_line_start"] = 263
        self.assertTrue(self.errors())

    def test_source_proof_discovery_unit_required(self):
        self.receipt["english_discovery"]["stable_units"] = [r for r in
            self.receipt["english_discovery"]["stable_units"] if not r["unit_id"].endswith(":proof")]
        self.assertTrue(self.errors())

    def test_discovery_cannot_become_french_authority(self):
        self.units["ega:I.7.1.15"]["authority_state"] = "french_admitted"
        self.assertTrue(self.errors())

    def test_all_appended_rows_required(self):
        for ledger in self.receipt["ledgers"]:
            self.tables = copy.deepcopy(self.frozen_tables)
            key = ledger["id_field"]
            victim = ledger["rows"][0][key]
            self.tables[ledger["path"]] = [r for r in self.tables[ledger["path"]] if r[key] != victim]
            self.assertTrue(self.errors())

    def test_stronger_integral_realization_not_whole_statement_equivalence(self):
        for edge in ("S001369", "S001377"):
            self.setUp()
            self.mutate_row_in_both("ega/smap.csv", "edge_id", edge,
                                    relation="equivalent", coverage_claim="full_statement")
            self.assertTrue(self.errors())

    def test_stronger_relation_not_ordinary_component(self):
        for edge in ("S001369", "S001377"):
            self.setUp()
            self.mutate_row_in_both("ega/smap.csv", "edge_id", edge, relation="split")
            self.assertTrue(self.errors())

    def test_stronger_and_terminology_dispositions_required(self):
        for victim in ("R000884", "R000888", "R000885", "R000890"):
            self.setUp()
            self.mutate_row_in_both("ega/resid.csv", "residual_id", victim, status="covered_derived")
            self.assertTrue(self.errors())

    def test_modern_geometric_and_quotient_point_contrasts_not_positive_coverage(self):
        for tag in ("03PO", "01J9"):
            self.setUp()
            target = next(t for t in self.receipt["negative_comparison_targets"] if t["tag"] == tag)
            self.receipt["negative_comparison_targets"].remove(target)
            self.receipt["pinned_targets"].append(target)
            self.assertTrue(self.errors())

    def test_pinned_target_hash_or_tag_join_tampering_fails(self):
        self.tags["etale-cohomology-definition-geometric-point"] = "0000"
        self.assertTrue(self.errors())
        self.tags = dict(self.frozen_tags)
        target = self.receipt["pinned_targets"][0]
        target["sha256"] = "0" * 64
        self.assertTrue(self.errors())

    def test_wrong_block_with_its_valid_hash_cannot_stand_for_target(self):
        target = self.receipt["pinned_targets"][0]
        first = self.blobs[target["path"]].split(b"\n")[0] + b"\n"
        target.update(lf_line_start=1, lf_line_end=1, bytes=len(first),
                      sha256=hashlib.sha256(first).hexdigest().upper())
        self.assertTrue(self.errors())

    def test_full_hyphenated_filename_prefix_required_for_target_join(self):
        target = next(t for t in self.receipt["negative_comparison_targets"] if t["tag"] == "03PO")
        target["path"] = "schemes.tex"
        self.assertTrue(self.errors())

    def test_unlabelled_support_locus_cannot_be_moved_or_omitted(self):
        self.receipt["supporting_unlabelled_proof_blocks"][0]["lf_line_start"] += 1
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt["supporting_unlabelled_proof_blocks"] = []
        self.assertTrue(self.errors())

    def test_french_scope_and_manifest_row_tampering_fail(self):
        self.scope["reviewed_source_slices"]["ega:I.7.1.15"]["slice_sha256"] = "0" * 64
        self.assertTrue(self.errors())
        self.scope = copy.deepcopy(self.frozen_scope)
        self.receipt["french_authority"]["manifest_file_binding"]["manifest_file_row"]["bytes"] += 1
        self.assertTrue(self.errors())

    def test_current_snapshot_cannot_inflate_coverage(self):
        self.scope["statement_review_snapshot"]["source_units"] += 1
        self.assertTrue(self.errors())


if __name__ == "__main__":
    unittest.main()
