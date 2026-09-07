"""Evidence contracts for EGA I7.1.10-14; not a formal proof checker."""
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
RECEIPT = ROOT / "validation/ega-i-7.1.10-7.1.14-semantic-checkpoint-2026-09-07.json"


class Semantic711014Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parsed = ast.parse((ROOT / "ega/check.py").read_text(encoding="utf-8"))
        nodes = [node for node in parsed.body if isinstance(node, ast.FunctionDef)
                 and node.name == "i711014_semantic_contract_errors"]
        env = {"hashlib": hashlib, "PINNED_STACKS_COMMIT": UPSTREAM}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), "ega/check.py", "exec"), env)
        cls.verify = staticmethod(env["i711014_semantic_contract_errors"])
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

    def test_complete_source_level_existing_coverage(self):
        self.assertEqual(self.errors(), [])

    def test_base_and_upstream_are_ancestors_not_private_candidate_dependencies(self):
        for commit in (UPSTREAM, self.receipt["starting_content_commit"]):
            result = subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT)
            self.assertEqual(result.returncode, 0)

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

    def test_next_cursor_includes_introduction(self):
        self.receipt["next_cursor_starts_with_introduction"] = False
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt["next_semantic_cursor"] = "ega:I.7.1.16"
        self.assertTrue(self.errors())

    def test_next_introduction_not_absorbed_into_fourteen(self):
        self.receipt["languages"]["fr"]["slices"]["ega:I.7.1.14"]["lf_line_end"] = 261
        self.assertTrue(self.errors())

    def test_next_introduction_not_silently_dropped(self):
        for lang in ("fr", "en"):
            self.receipt = copy.deepcopy(self.frozen)
            del self.receipt["languages"][lang]["next_excluded_context"]["introduction"]
            self.assertTrue(self.errors())

    def test_page_marker_and_intro_not_replaced_by_numbered_environments(self):
        for lang in ("fr", "en"):
            for number in ("11", "14"):
                self.receipt = copy.deepcopy(self.frozen)
                source = self.receipt["languages"][lang]
                unit = "ega:I.7.1." + number
                source["slices"][unit] = copy.deepcopy(source["numbered_environments"][unit])
                self.assertTrue(self.errors())

    def test_each_unwrapped_proof_and_prefix_required(self):
        for lang in ("fr", "en"):
            for owner in self.frozen["languages"][lang]["owned_parts"]:
                self.receipt = copy.deepcopy(self.frozen)
                del self.receipt["languages"][lang]["owned_parts"][owner]
                self.assertTrue(self.errors())

    def test_proof_terminal_line_cannot_be_truncated(self):
        for lang in ("fr", "en"):
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt["languages"][lang]["owned_parts"]["ega:I.7.1.14:proof"]["lf_line_end"] -= 1
            self.assertTrue(self.errors())

    def test_source_proof_discovery_unit_required(self):
        self.receipt["source_proof_units"].pop()
        self.assertTrue(self.errors())

    def test_discovery_cannot_become_french_authority(self):
        self.units["ega:I.7.1.13"]["authority_state"] = "french_admitted"
        self.assertTrue(self.errors())

    def test_all_appended_rows_required(self):
        for ledger in self.receipt["ledgers"]:
            self.tables = copy.deepcopy(self.frozen_tables)
            key = ledger["id_field"]
            victim = ledger["rows"][0][key]
            self.tables[ledger["path"]] = [r for r in self.tables[ledger["path"]] if r[key] != victim]
            self.assertTrue(self.errors())

    def test_stronger_injection_cannot_become_whole_statement_equivalence(self):
        ledger = next(l for l in self.receipt["ledgers"] if l["path"] == "ega/smap.csv")
        for rows in (ledger["rows"], self.tables["ega/smap.csv"]):
            for row in rows:
                if row["edge_id"] == "S001350":
                    row["relation"] = "equivalent"
                    row["coverage_claim"] = "full_statement"
        self.assertTrue(self.errors())

    def test_stronger_realization_not_ordinary_component_without_disposition(self):
        ledger = next(l for l in self.receipt["ledgers"] if l["path"] == "ega/smap.csv")
        for rows in (ledger["rows"], self.tables["ega/smap.csv"]):
            for row in rows:
                if row["edge_id"] == "S001352":
                    row["relation"] = "split"
        self.assertTrue(self.errors())

    def test_adverse_square_zero_example_not_positive_coverage(self):
        self.receipt["pinned_targets"].append(self.receipt["negative_comparison_targets"].pop())
        self.assertTrue(self.errors())

    def test_valued_point_and_pair_stronger_components_retain_their_residuals(self):
        for victim in ("R000881", "R000882"):
            self.receipt = copy.deepcopy(self.frozen)
            self.tables = copy.deepcopy(self.frozen_tables)
            ledger = next(l for l in self.receipt["ledgers"] if l["path"] == "ega/resid.csv")
            for rows in (ledger["rows"], self.tables["ega/resid.csv"]):
                for row in rows:
                    if row["residual_id"] == victim:
                        row["status"] = "covered_derived"
            self.assertTrue(self.errors())

    def test_pinned_target_hash_or_tag_join_tampering_fails(self):
        self.tags["morphisms-lemma-rational-map-finite-presentation"] = "0000"
        self.assertTrue(self.errors())
        self.tags = dict(self.frozen_tags)
        self.assertTrue(self.errors(lambda commit, path: self.blobs[path].replace(
            b"If $Y \\to S$ is locally of finite presentation", b"If $Y \\to S$ is locally of finite type")))

    def test_wrong_block_with_its_valid_hash_cannot_stand_for_target(self):
        target = self.receipt["pinned_targets"][0]
        first = self.blobs[target["path"]].split(b"\n")[0] + b"\n"
        target.update(lf_line_start=1, lf_line_end=1, bytes=len(first),
                      sha256=hashlib.sha256(first).hexdigest().upper())
        self.assertTrue(self.errors())

    def test_french_scope_and_manifest_row_tampering_fail(self):
        self.scope["reviewed_source_slices"]["ega:I.7.1.11"]["slice_sha256"] = "0" * 64
        self.assertTrue(self.errors())
        self.scope = copy.deepcopy(self.frozen_scope)
        self.receipt["french_authority"]["manifest_file_binding"]["manifest_file_row"]["bytes"] += 1
        self.assertTrue(self.errors())

    def test_current_snapshot_cannot_inflate_coverage(self):
        self.scope["statement_review_snapshot"]["source_units"] += 1
        self.assertTrue(self.errors())


if __name__ == "__main__":
    unittest.main()
