"""Evidence and adverse semantic contracts for EGA I 7.1.4-7.1.9.1."""
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
RECEIPT = ROOT / "validation/ega-i-7.1.4-7.1.9.1-semantic-checkpoint-2026-09-07.json"


class Semantic719Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parsed = ast.parse((ROOT / "ega/check.py").read_text(encoding="utf-8"))
        nodes = [n for n in parsed.body if isinstance(n, ast.FunctionDef)
                 and n.name in {"i719_semantic_contract_errors", "i719_manifest_binding"}]
        env = {"hashlib": hashlib, "PINNED_STACKS_COMMIT": UPSTREAM}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), "ega/check.py", "exec"), env)
        cls.verify = staticmethod(env["i719_semantic_contract_errors"])
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
            cls.frozen_tables[ledger["path"]] = [
                r for r in rows if r[ledger["id_field"]] not in superseded]
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

    def test_complete_existing_coverage_contract(self):
        self.assertEqual(self.errors(), [])

    def test_public_base_prefix_append_and_sealed_postimage(self):
        for ledger in self.receipt["ledgers"]:
            with self.subTest(path=ledger["path"]):
                base = subprocess.check_output(["git", "show",
                    self.receipt["starting_content_commit"] + ":" + ledger["path"]], cwd=ROOT)
                raw = (ROOT / ledger["path"]).read_bytes()
                lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
                prefix = b"".join(lines[:ledger["prefix_rows"] + 1])
                append = b"".join(lines[ledger["prefix_rows"] + 1:ledger["final_rows"] + 1])
                post = prefix + append
                self.assertEqual(prefix, base)
                for block, size, sha in [(prefix, ledger["prefix_bytes"], ledger["prefix_sha256"]),
                                        (append, ledger["append_bytes"], ledger["append_sha256"]),
                                        (post, ledger["bytes"], ledger["sha256"])]:
                    self.assertEqual(len(block), size)
                    self.assertEqual(hashlib.sha256(block).hexdigest().upper(), sha)

    def test_preserved_authority_discovery_visual_issue_and_historical_receipt(self):
        for item in self.receipt["preserved_inputs"]:
            raw = (ROOT / item["path"]).read_bytes()
            self.assertEqual(len(raw), item["bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest().upper(), item["sha256"])

    def test_all_hypothesis_and_nonclaim_mutations_fail(self):
        for key, value in self.frozen["semantic_contract"].items():
            with self.subTest(key=key):
                self.receipt = copy.deepcopy(self.frozen)
                self.receipt["semantic_contract"][key] = not value if isinstance(value, bool) else "ADVERSE"
                self.assertTrue(self.errors())

    def test_source_cursor_cannot_skip_next_unit(self):
        self.receipt["next_semantic_cursor"] = "ega:I.7.1.11"
        self.assertTrue(self.errors())

    def test_each_exact_row_is_required(self):
        for ledger in self.receipt["ledgers"]:
            with self.subTest(path=ledger["path"]):
                self.tables = copy.deepcopy(self.frozen_tables)
                key = ledger["id_field"]
                victim = ledger["rows"][0][key]
                self.tables[ledger["path"]] = [r for r in self.tables[ledger["path"]] if r[key] != victim]
                self.assertTrue(self.errors())

    def test_source_proof_unit_cannot_disappear(self):
        self.receipt["source_proof_units"].pop()
        self.assertTrue(self.errors())

    def test_french_statement_only_scope_drops_complete715_proof_and_tail(self):
        self.receipt["languages"]["fr"]["slices"]["ega:I.7.1.5"]["lf_line_end"] = 93
        self.assertTrue(self.errors())

    def test_parent719_deduction_cannot_be_assigned_to_lemma(self):
        parts = self.receipt["languages"]["fr"]["owned_parts"]
        parts["ega:I.7.1.9.1:deduction"] = parts.pop("ega:I.7.1.9:deduction")
        self.assertTrue(self.errors())

    def test_lemma_final_proof_assertion_cannot_be_truncated(self):
        self.receipt["languages"]["fr"]["owned_parts"]["ega:I.7.1.9.1:proof"]["lf_line_end"] = 188
        self.assertTrue(self.errors())

    def test_english_parent_deduction_cannot_be_omitted(self):
        del self.receipt["languages"]["en"]["owned_parts"]["ega:I.7.1.9:deduction"]
        self.assertTrue(self.errors())

    def test_source_binding_hash_mismatch_fails(self):
        self.scope["reviewed_source_slices"]["ega:I.7.1.8"]["slice_sha256"] = "0" * 64
        self.assertTrue(self.errors())

    def test_manifest_row_not_mutable_public_locator(self):
        self.receipt["french_authority"]["manifest_file_binding"]["manifest_file_row"]["sha256"] = "0" * 64
        self.assertTrue(self.errors())

    def test_discovery_is_not_promoted_to_authority(self):
        self.units["ega:I.7.1.9"]["authority_state"] = "french_admitted"
        self.assertTrue(self.errors())

    def test_full_0bx8_statement_not_equivalent_to_germs(self):
        ledger = next(x for x in self.receipt["ledgers"] if x["path"] == "ega/smap.csv")
        for table in (self.tables["ega/smap.csv"], ledger["rows"]):
            for row in table:
                if row["source_unit"] == "ega:I.7.1.7" and row["official_tag"] == "0BX8":
                    row["coverage_claim"] = "full_statement"
                    row["relation"] = "equivalent"
        self.assertTrue(self.errors())

    def test_negative_total_quotient_target_cannot_become_positive(self):
        self.receipt["pinned_targets"].append(self.receipt["negative_comparison_targets"].pop())
        self.assertTrue(self.errors())

    def test_exact_pinned_tag_join_required(self):
        self.tags["algebra-lemma-localization-colimit"] = "0000"
        self.assertTrue(self.errors())

    def test_pinned_target_block_tampering_fails(self):
        self.assertTrue(self.errors(lambda commit, path: self.blobs[path].replace(
            b"S^{-1}M = \\colim_{f \\in S} M_f", b"S^{-1}M = M_f")))

    def test_valid_hash_of_wrong_block_does_not_bind_target(self):
        target = next(t for t in self.receipt["pinned_targets"] if t["tag"] == "01RS")
        target.update(lf_line_start=1, lf_line_end=1)
        first = self.blobs[target["path"]].split(b"\n")[0] + b"\n"
        target.update(bytes=len(first), sha256=hashlib.sha256(first).hexdigest().upper())
        self.assertTrue(self.errors())

    def test_current_counter_mutation_fails(self):
        self.scope["statement_review_snapshot"]["source_units"] += 1
        self.assertTrue(self.errors())


if __name__ == "__main__":
    unittest.main()
