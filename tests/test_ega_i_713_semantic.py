"""Adverse contracts for the immutable EGA I 7.1.1-7.1.3 v1 checkpoint."""
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
CHECKPOINT = ROOT / "validation/ega-i-7.1.1-7.1.3-semantic-checkpoint-2026-09-07.json"


class Semantic713Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parsed = ast.parse((ROOT / "ega/check.py").read_text(encoding="utf-8"))
        node = next(n for n in parsed.body if isinstance(n, ast.FunctionDef)
                    and n.name == "i713_semantic_contract_errors")
        env = {"hashlib": hashlib, "PINNED_STACKS_COMMIT": UPSTREAM}
        exec(compile(ast.Module(body=[node], type_ignores=[]), "ega/check.py", "exec"), env)
        cls.verify = staticmethod(env["i713_semantic_contract_errors"])
        cls.frozen = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
        cls.frozen_scope = json.loads((ROOT / "ega/scope.json").read_text(encoding="utf-8"))
        # Replay v1 metadata without replacing its historical French ranges.
        for key in ("statement_review_snapshot", "residual_snapshot"):
            cls.frozen_scope[key] = copy.deepcopy(cls.frozen[key])
        cls.frozen_scope["reviewed_source_slices"].update(
            copy.deepcopy(cls.frozen["french_authority"]["source_scopes"]))
        cls.frozen_tables = {}
        for ledger in cls.frozen["ledgers"]:
            raw = (ROOT / ledger["path"]).read_bytes()
            historical = b"".join(raw.splitlines(keepends=True)[:ledger["final_rows"] + 1])
            cls.frozen_tables[ledger["path"]] = list(csv.DictReader(
                io.StringIO(historical.decode("utf-8"), newline="")))
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

    def test_historical_v1_contract(self):
        self.assertEqual(self.errors(), [])

    def test_exact_base_prefixes_append_blocks_and_historical_postimages(self):
        for entry in self.receipt["ledgers"]:
            with self.subTest(path=entry["path"]):
                raw = (ROOT / entry["path"]).read_bytes()
                base = subprocess.check_output(["git", "show",
                    self.receipt["starting_content_commit"] + ":" + entry["path"]], cwd=ROOT)
                self.assertTrue(raw.startswith(base))
                historical = b"".join(raw.splitlines(keepends=True)[:entry["final_rows"] + 1])
                for data, count, digest in (
                        (base, entry["prefix_bytes"], entry["prefix_sha256"]),
                        (historical[len(base):], entry["append_bytes"], entry["append_sha256"]),
                        (historical, entry["bytes"], entry["sha256"])):
                    self.assertEqual((len(data), hashlib.sha256(data).hexdigest().upper()),
                                     (count, digest))

    def test_every_appended_row_is_bound(self):
        for entry in self.frozen["ledgers"]:
            for row in entry["rows"]:
                with self.subTest(identifier=row[entry["id_field"]]):
                    self.setUp()
                    actual = next(r for r in self.tables[entry["path"]]
                                  if r[entry["id_field"]] == row[entry["id_field"]])
                    field = next(k for k in actual if k != entry["id_field"])
                    actual[field] += " changed"
                    self.assertTrue(self.errors())

    def test_source_edge_omission_duplication_and_reordering_rejected(self):
        for mutate in (lambda rows: rows.pop(),
                       lambda rows: rows.append(copy.deepcopy(rows[-1])),
                       lambda rows: rows.reverse()):
            self.setUp()
            mutate(self.tables["ega/smap.csv"])
            self.assertTrue(self.errors())

    def test_residual_omission_duplication_and_reordering_rejected(self):
        for mutate in (lambda rows: rows.pop(),
                       lambda rows: rows.append(copy.deepcopy(rows[-1])),
                       lambda rows: rows.reverse()):
            self.setUp()
            mutate(self.tables["ega/resid.csv"])
            self.assertTrue(self.errors())

    def test_schematic_density_substitution_rejected(self):
        self.receipt["semantic_contract"]["domain_density"] = "schematic"
        self.assertTrue(self.errors())

    def test_pseudo_morphism_cannot_be_a_positive_target(self):
        self.receipt["pinned_targets"][0] = self.receipt["negative_comparison_targets"][0]
        self.assertTrue(self.errors())

    def test_witness_cannot_be_replaced_by_full_overlap(self):
        self.receipt["semantic_contract"]["equality_witness"] = "all of U intersect V intersect W"
        self.assertTrue(self.errors())

    def test_reducedness_separatedness_and_finite_components_are_not_added(self):
        for key, value in (("additional_source_hypotheses", ["reduced"]),
                           ("additional_target_hypotheses", ["separated"]),
                           ("finite_component_assumption", True)):
            self.setUp()
            self.receipt["semantic_contract"][key] = value
            self.assertTrue(self.errors())

    def test_canonical_quotient_cannot_be_strengthened_to_injection(self):
        self.receipt["semantic_contract"]["canonical_quotient_injective"] = True
        self.assertTrue(self.errors())

    def test_verified_printing_and_proposed_correction_boundaries(self):
        for key, value in (("status", "ACCEPTED"),
                           ("classification", "TRANSCRIPTION_ONLY"),
                           ("printed_authority_comparison", "NOT_PERFORMED"),
                           ("established_printed_error", False),
                           ("authority_mutation", True)):
            self.setUp()
            self.receipt["proposed_source_edition_evidence"][key] = value
            self.assertTrue(self.errors())

    def test_discovery_units_remain_frozen(self):
        for unit in self.receipt["source_units"]:
            self.setUp()
            self.units[unit]["authority_state"] = "french_admitted"
            self.assertTrue(self.errors())

    def test_each_french_slice_is_bound(self):
        for unit in self.receipt["source_units"]:
            self.setUp()
            self.scope["reviewed_source_slices"][unit]["slice_sha256"] = "0" * 64
            self.assertTrue(self.errors())

    def test_unverified_french_manifest_binding_is_rejected(self):
        self.receipt["french_authority"]["manifest_file_binding"]["status"] = "NOT_YET_VERIFIED"
        self.assertTrue(self.errors())

    def test_original_manifest_row_and_printed_page_cannot_be_substituted(self):
        self.receipt["french_authority"]["manifest_file_binding"]["manifest_file_row"]["sha256"] = "0" * 64
        self.assertTrue(self.errors())
        self.setUp()
        self.receipt["proposed_source_edition_evidence"]["original_source"]["overstatement_printed_page"] = 156
        self.assertTrue(self.errors())

    def test_wrong_cursor_and_stale_live_counts_rejected(self):
        self.receipt["next_semantic_cursor"] = "ega:I.7.1.3"
        self.assertTrue(self.errors())
        self.setUp()
        self.scope["statement_review_snapshot"]["file_rows"] = 1290
        self.assertTrue(self.errors())

    def test_pinned_block_and_tag_join_mutations_rejected(self):
        self.assertTrue(self.errors(lambda commit, path: b"wrong source\n"))
        self.tags["morphisms-definition-rational-map"] = "01RX"
        self.assertTrue(self.errors())

    def test_historical_receipt_and_preserved_inputs_are_immutable(self):
        for item in self.receipt["preserved_inputs"] + [self.receipt["historical_checkpoint"]]:
            raw = (ROOT / item["path"]).read_bytes()
            self.assertEqual((len(raw), hashlib.sha256(raw).hexdigest().upper()),
                             (item["bytes"], item["sha256"]))


if __name__ == "__main__":
    unittest.main()
