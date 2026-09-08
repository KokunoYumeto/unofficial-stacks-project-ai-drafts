"""Independent adverse cases for the source-bound I7.3.1--4 dossier.

These test evidence contracts, not mathematical truth.
"""
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import unittest
from tools import ega_i734_semantic_contract as contract

ROOT = Path(__file__).resolve().parents[1]

class Semantic734Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt_raw = (ROOT / contract.RECEIPT_PATH).read_bytes()
        cls.frozen = json.loads(cls.receipt_raw)
        cls.live_scope = json.loads((ROOT / "ega/scope.json").read_bytes())
        paths = {x["path"] for x in cls.frozen["preserved_inputs"]}
        paths |= {x["path"] for x in cls.frozen["ledgers"]} | {"ega/i734.md"}
        cls.live_raw = {p: (ROOT / p).read_bytes() for p in paths}
        cls.frozen_scope, cls.frozen_tables, historical_loader = contract.historical_inputs(
            cls.frozen, cls.live_scope, lambda p: cls.live_raw[p])
        cls.frozen_raw = {p: historical_loader(p) for p in paths}
        cls.frozen_units = {r["unit_id"]: r for r in csv.DictReader(io.StringIO(cls.frozen_raw["ega/units.csv"].decode("utf-8"), newline=""))}
        target_paths = {t["path"] for t in cls.frozen["targets"]} | {"tags/tags"}
        cls.frozen_blobs = {(c, p): subprocess.check_output(["git", "show", c + ":" + p], cwd=ROOT)
                            for c in (contract.UPSTREAM, contract.TARGET_COMMIT) for p in target_paths}
        cls.frozen_tags = {line.split(",", 1)[1]: line.split(",", 1)[0]
                           for line in cls.frozen_blobs[contract.UPSTREAM, "tags/tags"].decode("utf-8").splitlines()
                           if line and not line.startswith("#")}

    def setUp(self):
        self.receipt = copy.deepcopy(self.frozen)
        self.scope = copy.deepcopy(self.frozen_scope)
        self.tables = copy.deepcopy(self.frozen_tables)
        self.units = dict(self.frozen_units)
        self.raw = dict(self.frozen_raw)
        self.blobs = dict(self.frozen_blobs)
        self.tags = dict(self.frozen_tags)

    def errors(self):
        return contract.verify(self.receipt, self.scope, self.tables, self.units,
                               lambda c, p: self.blobs[c, p], self.tags, lambda p: self.raw[p])

    def test_reviewed_candidate_and_immutable_receipt_pass(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(contract.receipt_errors(self.receipt_raw), [])

    def test_historical_projection_accepts_successor_append_without_changing734(self):
        live = dict(self.live_raw)
        for ledger in self.frozen["ledgers"]:
            live[ledger["path"]] += b"successor append belongs to its own validator\n"
        scope, tables, loader = contract.historical_inputs(self.frozen,
            dict(self.live_scope, next_semantic_cursor="ega:I.7.3.8"), lambda p: live[p])
        self.assertEqual(scope["next_semantic_cursor"], "ega:I.7.3.5")
        self.assertEqual(scope["statement_review_snapshot"], self.frozen["statement_review_snapshot"])
        self.assertEqual(tables, self.frozen_tables)
        for ledger in self.frozen["ledgers"]:
            self.assertEqual(loader(ledger["path"]), self.frozen_raw[ledger["path"]])

    def test_historical_projection_rejects_prefix_damage_and_rewritten_receipt(self):
        for ledger in self.frozen["ledgers"]:
            for mode in ("prefix", "truncate", "crlf", "nonbytes"):
                live = dict(self.live_raw)
                raw = live[ledger["path"]]
                live[ledger["path"]] = {"prefix": b"X" + raw[1:],
                    "truncate": raw[:ledger["bytes"]-1],
                    "crlf": raw.replace(b"\n", b"\r\n"), "nonbytes": None}[mode]
                with self.assertRaises(ValueError):
                    contract.historical_inputs(self.frozen, self.live_scope, lambda p: live[p])
        changed = copy.deepcopy(self.frozen)
        changed["ledgers"][0]["final_rows"] += 1
        with self.assertRaises(ValueError):
            contract.historical_inputs(changed, self.live_scope, lambda p: self.live_raw[p])

    def test_exact_five_units_and_owned_tail_heading_page_marker(self):
        self.assertEqual([r["unit_id"] for r in self.receipt["english_discovery"]["stable_units"]],
                         ["ega:I.7.3.1", "ega:I.7.3.2", "ega:I.7.3.3", "ega:I.7.3.3:proof", "ega:I.7.3.4"])
        self.assertEqual(self.receipt["owned_unnumbered_parts"], {"ega:I.7.3.2:restriction-tail": "ega:I.7.3.2"})
        self.assertEqual(self.receipt["source_proof_units"], ["ega:I.7.3.3:proof"])
        self.assertEqual(self.receipt["owned_section_heading"], "ega:I.7.3")
        self.receipt["source_proof_units"].append("ega:I.7.3.4:proof")
        self.assertTrue(self.errors())

    def test_all_semantic_claims_and_boolean_number_substitution_rejected(self):
        for key, value in self.frozen["semantic_contract"].items():
            for replacement in ([not value, int(value)] if isinstance(value, bool) else ["ADVERSE"]):
                with self.subTest(key=key, value=replacement):
                    self.receipt = copy.deepcopy(self.frozen)
                    self.receipt["semantic_contract"][key] = replacement
                    self.assertTrue(self.errors())

    def test_R_and_K_qualifications_cannot_be_weakened(self):
        for key, value in [("R_equals_K_general_nonreduced", True),
                           ("I733_generic_factors", "residue fields"),
                           ("I733_coordinate_rings_required_Noetherian", True),
                           ("I733_maximal_ideal_nilpotent_required", True),
                           ("I734_X_reduced", False)]:
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt["semantic_contract"][key] = value
            self.assertTrue(self.errors(), key)

    def test_unknown_claim_and_cursor_mutations_rejected(self):
        self.receipt["semantic_contract"]["complete_EGA"] = True
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt["next_semantic_cursor"] = "ega:I.7.3.6"
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.scope["next_semantic_cursor"] = "ega:I.7.3.6"
        self.assertTrue(self.errors())

    def test_complete_bilingual_ownership_cannot_be_truncated_reassigned_or_rehashed(self):
        for lang in ("fr", "en"):
            for section in ("slices", "numbered_environments", "owned_parts", "page_markers"):
                for owner in self.frozen["languages"][lang][section]:
                    for mode in ("omit", "truncate", "reassign", "rehash"):
                        self.receipt = copy.deepcopy(self.frozen)
                        spans = self.receipt["languages"][lang][section]
                        if mode == "omit":
                            del spans[owner]
                        elif mode == "truncate":
                            spans[owner]["lf_line_end"] -= 1
                        elif mode == "reassign":
                            spans["ega:I.7.3.4:proof"] = spans.pop(owner)
                        else:
                            spans[owner]["sha256"] = "0" * 64
                        self.assertTrue(self.errors(), (lang, section, owner, mode))

    def test_exact_source_passage_and_consulted_choice_text_bound(self):
        self.receipt["source_passages"]["fr"]["spans"]["unit733"]["text"] += "ADVERSE"
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt["choices"][2]["rejected_alternatives"] = []
        self.assertTrue(self.errors())

    def test_each_official_and_integrated_target_actual_bytes_replayed(self):
        for target in self.frozen["targets"]:
            for edition, c in (("official", contract.UPSTREAM), ("integrated", contract.TARGET_COMMIT)):
                self.blobs = dict(self.frozen_blobs)
                key = c, target["path"]
                raw = self.blobs[key]
                pos = target[edition]["byte_offset_start"]
                self.blobs[key] = raw[:pos] + b"X" + raw[pos + 1:]
                self.assertTrue(self.errors(), (target["tag"], edition))

    def test_whole_target_identity_not_only_label_span(self):
        for key, raw in self.frozen_blobs.items():
            if key[1] != "tags/tags":
                self.blobs = dict(self.frozen_blobs)
                self.blobs[key] = b"X" + raw[1:]
                self.assertTrue(self.errors(), key)

    def test_each_adjacent_context_actual_bytes_replayed(self):
        self.assertEqual(len(self.frozen["target_contexts"]), 3)
        for target in self.frozen["target_contexts"]:
            for edition, c in (("official", contract.UPSTREAM), ("integrated", contract.TARGET_COMMIT)):
                self.blobs = dict(self.frozen_blobs)
                key = c, target["path"]
                raw = self.blobs[key]
                pos = target[edition]["byte_offset_start"]
                self.blobs[key] = raw[:pos] + b"X" + raw[pos + 1:]
                self.assertTrue(self.errors(), (target["name"], edition))

    def test_unequal_target_versions_and_comparison_only_roles_bound(self):
        unequal = {t["tag"] for t in self.frozen["targets"] if t["official"]["sha256"] != t["integrated"]["sha256"]}
        self.assertEqual(unequal, {"01RV", "0089", "01HV", "00E3", "00EU", "0052"})
        for t in self.frozen["targets"]:
            if t["tag"] in unequal:
                self.receipt = copy.deepcopy(self.frozen)
                next(x for x in self.receipt["targets"] if x["tag"] == t["tag"])["official"] = t["integrated"]
                self.assertTrue(self.errors())
        for tag in ("0EMF", "01X5", "0BA8"):
            self.receipt = copy.deepcopy(self.frozen)
            next(x for x in self.receipt["targets"] if x["tag"] == tag)["role"] = "full_equivalent_theorem"
            self.assertTrue(self.errors())

    def test_ledger_prefix_append_extra_rows_crlf_and_active_views_bound(self):
        for ledger in self.frozen["ledgers"]:
            path = ledger["path"]
            for mode in ("prefix", "append", "extra", "crlf"):
                self.raw = dict(self.frozen_raw)
                raw = self.raw[path]
                if mode == "prefix":
                    raw = b"X" + raw[1:]
                elif mode == "append":
                    n = ledger["prefix_bytes"]
                    raw = raw[:n] + b"X" + raw[n + 1:]
                elif mode == "extra":
                    raw += b"ADVERSE\n"
                else:
                    raw = raw.replace(b"\n", b"\r\n")
                self.raw[path] = raw
                self.assertTrue(self.errors(), (path, mode))
        self.raw = dict(self.frozen_raw)
        self.tables["ega/smap.csv"].append(dict(self.tables["ega/smap.csv"][-1], edge_id="S009999"))
        self.assertTrue(self.errors())

    def test_scope_snapshots_and_source_scope_bound(self):
        for key in ("statement_review_snapshot", "residual_snapshot", "reviewed_source_slices"):
            self.scope = copy.deepcopy(self.frozen_scope)
            self.scope[key] = {}
            self.assertTrue(self.errors(), key)

    def test_twelve_prior_active_gaps_not_closed(self):
        rows = self.tables["ega/resid.csv"]
        self.assertEqual(sum(x["status"] == "open_gap" for x in rows), 12)
        next(x for x in rows if x["status"] == "open_gap")["status"] = "covered_derived"
        self.assertTrue(self.errors())

    def test_discovery_not_promoted_or_fictionally_extended(self):
        for unit in ("ega:I.7.3.4:proof", "ega:I.7.3.2:restriction-tail"):
            self.units = dict(self.frozen_units)
            self.units[unit] = {"unit_id": unit, "kind": "proof"}
            self.assertTrue(self.errors(), unit)
        self.units = copy.deepcopy(self.frozen_units)
        self.units["ega:I.7.3.3"]["review_state"] = "reviewed_existing"
        self.assertTrue(self.errors())

    def test_every_preserved_input_actual_bytes_bound(self):
        for item in self.frozen["preserved_inputs"]:
            self.raw = dict(self.frozen_raw)
            self.raw[item["path"]] += b"ADVERSE"
            self.assertTrue(self.errors(), item["path"])

    def test_tag_label_join_and_receipt_seal_cannot_self_rehash(self):
        for t in self.frozen["targets"]:
            self.tags = dict(self.frozen_tags)
            self.tags[t["label"]] = "ZZZZ"
            self.assertTrue(self.errors())
        self.assertTrue(contract.receipt_errors(self.receipt_raw + b" "))

    def test_dossier_damage_rejected_even_with_coordinated_hash(self):
        raw = self.frozen_raw["ega/i734.md"]
        cases = [(b"not necessarily fields", b"always fields"),
                 (b"arbitrary infinite open covers", b"finite open covers only"),
                 (b"the maximal ideal is not asserted to be nilpotent", b"the maximal ideal is nilpotent"),
                 (b"In contrast, $\\mathcal O_X\\to\\mathcal K_X$ is injective.", b"The two sheaves are always equal."),
                 (b"Suppose now that $X$ is reduced", b"Suppose now that $X$ is arbitrary")]
        for before, after in cases:
            damaged = raw.replace(before, after)
            self.assertNotEqual(damaged, raw, before)
            rehashed = dict(contract.DOSSIER, bytes=len(damaged), sha256=hashlib.sha256(damaged).hexdigest().upper())
            self.assertTrue(contract.dossier_errors(damaged, rehashed))
            self.raw["ega/i734.md"] = damaged
            self.assertTrue(self.errors())

    def test_malformed_metadata_tables_and_nonbyte_loaders_fail_closed(self):
        original = [self.receipt, self.scope, self.tables, self.units,
                    lambda c, p: self.blobs[c, p], self.tags, lambda p: self.raw[p]]
        for index in range(len(original)):
            for value in (None, [], "wrong"):
                args = list(original); args[index] = value
                self.assertTrue(contract.verify(*args), (index, value))
        for key in self.frozen:
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt[key] = [None]
            self.assertTrue(self.errors(), key)
        self.receipt = copy.deepcopy(self.frozen)
        for path in self.frozen_tables:
            for value in (None, [None], [{"source_unit": []}], "wrong"):
                self.tables = copy.deepcopy(self.frozen_tables)
                self.tables[path] = value
                self.assertTrue(self.errors(), (path, value))
        for value in (None, [], "wrong"):
            self.assertTrue(contract.verify(self.frozen, self.frozen_scope, self.frozen_tables, self.frozen_units,
                lambda c, p: value, self.frozen_tags, lambda p: self.frozen_raw[p]))
            self.assertTrue(contract.verify(self.frozen, self.frozen_scope, self.frozen_tables, self.frozen_units,
                lambda c, p: self.frozen_blobs[c, p], self.frozen_tags, lambda p: value))

if __name__ == "__main__":
    unittest.main()
