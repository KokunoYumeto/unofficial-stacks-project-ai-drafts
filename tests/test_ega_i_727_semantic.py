"""Exact EGA I 7.2.5--7 evidence contracts; not formal proof checking."""
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
BASE = "5d00ecc6c78e55f0a9118ffe7198a53242ac41b5"
RECEIPT = ROOT / "validation/ega-i-7.2.5-7.2.7-semantic-checkpoint-2026-09-08.json"


class Semantic727Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parsed = ast.parse((ROOT / "ega/check.py").read_text(encoding="utf-8"))
        nodes = [n for n in parsed.body if isinstance(n, ast.FunctionDef)
                 and n.name.startswith("i727_")]
        env = {"hashlib": hashlib, "json": json, "PINNED_STACKS_COMMIT": UPSTREAM}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), "ega/check.py", "exec"), env)
        cls.verify = staticmethod(env["i727_semantic_contract_errors"])
        cls.verify_dossier = staticmethod(env["i727_dossier_contract_errors"])
        cls.verify_targets = staticmethod(env["i727_source_target_contract_errors"])
        cls.verify_ledgers = staticmethod(env["i727_ledger_contract_errors"])
        cls.frozen = json.loads(RECEIPT.read_text(encoding="utf-8"))
        cls.frozen_scope = json.loads((ROOT / "ega/scope.json").read_text(encoding="utf-8"))
        for key in ("statement_review_snapshot", "residual_snapshot"):
            cls.frozen_scope[key] = copy.deepcopy(cls.frozen[key])
        cls.frozen_tables = {}
        for ledger in cls.frozen["ledgers"]:
            raw = (ROOT / ledger["path"]).read_bytes()
            lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
            rows = list(csv.DictReader(io.StringIO(
                b"".join(lines[:ledger["final_rows"] + 1]).decode(), newline="")))
            superseded = {r.get("supersedes") for r in rows if r.get("supersedes")}
            cls.frozen_tables[ledger["path"]] = [
                r for r in rows if r[ledger["id_field"]] not in superseded]
        with (ROOT / "ega/units.csv").open(encoding="utf-8", newline="") as handle:
            source_ids = set(cls.frozen["source_units"] + cls.frozen["source_proof_units"])
            cls.frozen_units = {r["unit_id"]: r for r in csv.DictReader(handle)
                                if r["unit_id"] in source_ids}
        paths = {t["path"] for t in cls.frozen["integrated_targets"]} | {"tags/tags"}
        cls.frozen_blobs = {(commit, path): subprocess.check_output(
            ["git", "show", commit + ":" + path], cwd=ROOT)
            for commit in (UPSTREAM, BASE) for path in paths}
        cls.frozen_tags = {line.split(",", 1)[1]: line.split(",", 1)[0]
                           for line in cls.frozen_blobs[UPSTREAM, "tags/tags"].decode().splitlines()
                           if line and not line.startswith("#")}

    def setUp(self):
        self.receipt = copy.deepcopy(self.frozen)
        self.scope = copy.deepcopy(self.frozen_scope)
        self.tables = copy.deepcopy(self.frozen_tables)
        self.units = copy.deepcopy(self.frozen_units)
        self.tags = dict(self.frozen_tags)
        self.blobs = dict(self.frozen_blobs)

    def errors(self):
        return self.verify(self.receipt, self.scope, self.tables, self.units,
                           lambda commit, path: self.blobs[commit, path], self.tags)

    def mutate_both(self, path, key, identity, **changes):
        ledger = next(l for l in self.receipt["ledgers"] if l["path"] == path)
        for rows in (ledger["rows"], self.tables[path]):
            for row in rows:
                if row[key] == identity:
                    row.update(changes)

    def test_frozen_candidate_passes(self):
        self.assertEqual(self.errors(), [])

    def test_malformed_top_level_inputs_return_controlled_errors(self):
        loader = lambda commit, path: self.blobs[commit, path]
        original = [self.receipt, self.scope, self.tables, self.units, loader, self.tags]
        for index in range(6):
            for value in (None, [], "not an object"):
                arguments = list(original)
                arguments[index] = value
                with self.subTest(argument=index, value=value):
                    self.assertTrue(self.verify(*arguments))

    def test_malformed_nested_containers_return_controlled_errors(self):
        paths = [
            ("french_authority",), ("french_authority", "manifest_file_binding"),
            ("french_authority", "manifest_file_binding", "manifest_file_row"),
            ("french_authority", "source_scopes"), ("languages",), ("languages", "fr"),
            ("languages", "fr", "owned_parts"), ("languages", "en", "page_markers"),
            ("pinned_targets",), ("negative_comparison_targets",), ("supporting_targets",),
            ("integrated_targets",), ("ledgers",), ("english_discovery",),
            ("english_discovery", "stable_units"), ("preserved_inputs",),
            ("preserved_open_gap_rows",), ("statement_review_snapshot",), ("derivation_dossier",),
        ]
        for path in paths:
            for value in (None, "not a container", [None]):
                self.setUp()
                target = self.receipt
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value
                with self.subTest(path=path, value=value):
                    self.assertTrue(self.errors())

    def test_malformed_rows_and_scalar_IDs_return_controlled_errors(self):
        for path in ("pinned_targets", "negative_comparison_targets", "supporting_targets",
                     "integrated_targets", "ledgers", "preserved_inputs"):
            for value in (None, [], "not a row"):
                self.setUp()
                self.receipt[path][0] = value
                self.assertTrue(self.errors(), (path, value))
        for field in ("rows", "path", "id_field"):
            self.setUp()
            self.receipt["ledgers"][0][field] = [None]
            self.assertTrue(self.errors())
        self.setUp()
        self.receipt["pinned_targets"][0]["tag"] = []
        self.assertTrue(self.errors())
        self.setUp()
        self.tables["ega/smap.csv"][0]["source_unit"] = []
        self.assertTrue(self.errors())

    def test_direct_helpers_also_reject_malformed_inputs(self):
        loader = lambda commit, path: self.blobs[commit, path]
        for value in (None, [], "wrong"):
            self.assertTrue(self.verify_targets(value, self.scope, loader, self.tags))
            self.assertTrue(self.verify_ledgers(value, self.scope, self.tables, self.units))
        self.assertTrue(self.verify_targets(self.receipt, self.scope, loader, None))
        self.assertTrue(self.verify_ledgers(self.receipt, self.scope, None, self.units))
        for value in (None, [], "not raw bytes"):
            self.assertTrue(self.verify_targets(self.receipt, self.scope,
                                               lambda commit, path: value, self.tags))

    def test_malformed_scope_and_actual_tables_return_controlled_errors(self):
        for key in ("reviewed_source_slices", "statement_review_snapshot", "residual_snapshot"):
            self.setUp()
            self.scope[key] = None
            self.assertTrue(self.errors())
        for path in self.frozen_tables:
            for value in (None, [None], "wrong"):
                self.setUp()
                self.tables[path] = value
                self.assertTrue(self.errors())

    def test_exact_base_and_upstream_are_reachable(self):
        self.assertEqual(self.frozen["starting_content_commit"], BASE)
        for commit in (BASE, UPSTREAM):
            self.assertEqual(subprocess.run(
                ["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT).returncode, 0)

    def test_source_units_proofs_and_next_boundary_cannot_advance(self):
        for key, value in (
                ("source_units", ["ega:I.7.2.5", "ega:I.7.2.6"]),
                ("source_proof_units", ["ega:I.7.2.5:proof", "ega:I.7.2.6:proof"]),
                ("next_semantic_cursor", "ega:I.7.2.9"),
                ("starting_content_commit", UPSTREAM),
                ("stacks_upstream", BASE),
                ("next_cursor_starts_with_numbered_environment", False)):
            self.setUp()
            self.receipt[key] = value
            self.assertTrue(self.errors(), key)

    def test_all_semantic_hypothesis_and_nonclaim_mutations_fail(self):
        for key, value in self.frozen["semantic_contract"].items():
            with self.subTest(key=key):
                self.setUp()
                self.receipt["semantic_contract"][key] = not value if isinstance(value, bool) else "ADVERSE"
                self.assertTrue(self.errors())

    def test_boolean_claims_cannot_be_replaced_by_numeric_truth_values(self):
        for key, value in self.frozen["semantic_contract"].items():
            if isinstance(value, bool):
                self.setUp()
                self.receipt["semantic_contract"][key] = int(value)
                self.assertTrue(self.errors(), key)

    def test_unknown_semantic_claims_cannot_be_added(self):
        self.receipt["semantic_contract"]["complete_EGA_II"] = True
        self.assertTrue(self.errors())

    def test_dossier_is_independently_sealed_even_after_rehash(self):
        raw = (ROOT / "ega/i727.md").read_bytes()
        expected = self.receipt["derivation_dossier"]
        self.assertEqual(self.verify_dossier(raw, expected), [])
        damaged = raw.replace(b"This equality of domains holds even when $X$ is not reduced.",
                              b"This equality of domains requires $X$ to be reduced.")
        self.assertNotEqual(raw, damaged)
        rehashed = dict(expected, bytes=len(damaged),
                        sha256=hashlib.sha256(damaged).hexdigest().upper())
        self.assertTrue(self.verify_dossier(damaged, expected))
        self.assertTrue(self.verify_dossier(damaged, rehashed))
        self.receipt["derivation_dossier"] = rehashed
        self.assertTrue(self.errors())

    def test_each_complete_bilingual_unit_and_proof_is_required(self):
        for lang in ("fr", "en"):
            for key in ("slices", "owned_parts", "numbered_environments"):
                for owner in self.frozen["languages"][lang][key]:
                    for mode in ("omit", "truncate", "rehash", "reassign"):
                        with self.subTest(language=lang, key=key, owner=owner, mode=mode):
                            self.setUp()
                            entries = self.receipt["languages"][lang][key]
                            if mode == "omit":
                                del entries[owner]
                            elif mode == "truncate":
                                entries[owner]["lf_line_end"] -= 1
                            elif mode == "rehash":
                                entries[owner]["sha256"] = "0" * 64
                            else:
                                entries["ega:I.7.2.8"] = entries.pop(owner)
                            self.assertTrue(self.errors())

    def test_numbered_environments_cannot_replace_complete_proof_storage(self):
        for lang in ("fr", "en"):
            self.setUp()
            self.receipt["languages"][lang]["slices"] = copy.deepcopy(
                self.receipt["languages"][lang]["numbered_environments"])
            self.assertTrue(self.errors())

    def test_page_marker_is_retained_with_proof_and_separately_bound(self):
        for lang, start in (("fr", 387), ("en", 233)):
            self.setUp()
            self.assertEqual(self.receipt["languages"][lang]["owned_parts"]["ega:I.7.2.5:proof"]["lf_line_start"], start)
            del self.receipt["languages"][lang]["page_markers"]
            self.assertTrue(self.errors())
            self.setUp()
            self.receipt["languages"][lang]["owned_parts"]["ega:I.7.2.5:proof"]["lf_line_start"] += 1
            self.assertTrue(self.errors())

    def test_next_boundary_is_excluded_not_absorbed(self):
        for lang, end in (("fr", 432), ("en", 261)):
            self.setUp()
            self.receipt["languages"][lang]["combined"]["lf_line_end"] = end
            self.assertTrue(self.errors())
            self.setUp()
            self.receipt["languages"][lang]["next_excluded_boundary"]["source_unit"] = "ega:I.7.2.9"
            self.assertTrue(self.errors())

    def test_complete_file_urls_and_hashes_are_fixed(self):
        for lang in ("fr", "en"):
            for key, value in (("url", "https://example.invalid/source.tex"),
                               ("full_sha256", "0" * 64), ("full_bytes", 1)):
                self.setUp()
                self.receipt["languages"][lang][key] = value
                self.assertTrue(self.errors())

    def test_french_scope_cannot_be_rehashed_in_both_receipt_and_scope(self):
        for field, value in (("slice_sha256", "0" * 64), ("lf_line_end", 385),
                             ("receipt", "EN.json"), ("path", "ega1/ega1-7.tex"),
                             ("full_bytes", 1)):
            self.setUp()
            for target in (self.receipt["french_authority"]["source_scopes"],
                           self.scope["reviewed_source_slices"]):
                target["ega:I.7.2.5"][field] = value
            self.assertTrue(self.errors())

    def test_french_manifest_row_is_independently_bound(self):
        for key, value in (("manifest", "OTHER.json"), ("manifest_bytes", 1),
                           ("manifest_sha256", "0" * 64)):
            self.setUp()
            self.receipt["french_authority"]["manifest_file_binding"][key] = value
            self.assertTrue(self.errors())
        self.setUp()
        self.receipt["french_authority"]["manifest_file_binding"]["manifest_file_row"]["bytes"] += 1
        self.assertTrue(self.errors())

    def test_all_reviewed_append_rows_are_required(self):
        for path, key, identity in (("ega/dec.csv", "decision_id", "D000359"),
                ("ega/smap.csv", "edge_id", "S001414"), ("ega/resid.csv", "residual_id", "R000913"),
                ("ega/agent.csv", "run_id", "A000278")):
            self.setUp()
            self.tables[path] = [r for r in self.tables[path] if r[key] != identity]
            self.assertTrue(self.errors())

    def test_coordinated_row_and_receipt_prose_mutations_fail(self):
        for path, key, identity, field in (("ega/dec.csv", "decision_id", "D000360", "rationale"),
                ("ega/smap.csv", "edge_id", "S001414", "evidence"),
                ("ega/resid.csv", "residual_id", "R000915", "evidence"),
                ("ega/agent.csv", "run_id", "A000278", "returned")):
            self.setUp()
            self.mutate_both(path, key, identity, **{field: "altered claim"})
            self.assertTrue(self.errors())

    def test_coordinated_append_ID_mutation_fails(self):
        self.mutate_both("ega/smap.csv", "edge_id", "S001414", edge_id="S001423")
        self.assertTrue(self.errors())

    def test_complete_ledger_and_metadata_inventory_is_fixed(self):
        self.receipt["ledgers"].pop()
        self.assertTrue(self.errors())
        self.setUp()
        self.receipt["ledgers"][0]["append_sha256"] = "0" * 64
        self.assertTrue(self.errors())
        self.setUp()
        self.receipt["ledgers"][0]["final_rows"] += 1
        self.assertTrue(self.errors())

    def test_no_unreviewed_source_row_can_hide_outside_the_append(self):
        row = copy.deepcopy(self.tables["ega/smap.csv"][-1])
        row["edge_id"] = "S001423"
        self.tables["ega/smap.csv"].append(row)
        self.assertTrue(self.errors())

    def test_discovery_is_not_promoted_or_rewritten(self):
        for unit in ("ega:I.7.2.5", "ega:I.7.2.6:proof", "ega:I.7.2.7"):
            self.setUp()
            self.units[unit]["authority_state"] = "french_admitted"
            self.assertTrue(self.errors())
            self.setUp()
            self.units[unit]["review_state"] = "reviewed_existing"
            self.assertTrue(self.errors())
        self.setUp()
        self.receipt["english_discovery"]["stable_units"][0]["anchor_sha256"] = "0" * 64
        self.units["ega:I.7.2.5"]["anchor_sha256"] = "0" * 64
        self.assertTrue(self.errors())

    def test_domain_differences_cannot_be_relabelled_as_gaps_or_full_coverage(self):
        for identity in ("R000907", "R000913"):
            for status in ("open_gap", "covered_derived", "integrated_local_mirror"):
                self.setUp()
                self.mutate_both("ega/resid.csv", "residual_id", identity, status=status)
                self.assertTrue(self.errors())

    def test_existing_graph_domain_result_is_not_a_semantic_difference(self):
        self.mutate_both("ega/resid.csv", "residual_id", "R000910", status="known_semantic_difference")
        self.assertTrue(self.errors())

    def test_no_component_can_be_promoted_to_full_statement_equivalence(self):
        for n in range(1402, 1423):
            self.setUp()
            self.mutate_both("ega/smap.csv", "edge_id", f"S{n:06d}",
                             relation="equivalent", coverage_claim="full_statement")
            self.assertTrue(self.errors())

    def test_prior_twelve_open_gap_contents_and_statuses_are_unchanged(self):
        for mode in ("close", "rewrite", "omit"):
            self.setUp()
            row = next(r for r in self.tables["ega/resid.csv"] if r["residual_id"] == "R000443")
            if mode == "close":
                row["status"] = "covered_derived"
            elif mode == "rewrite":
                row["evidence"] = "nothing remains"
            else:
                self.tables["ega/resid.csv"].remove(row)
            self.assertTrue(self.errors())

    def test_prior_gap_receipt_cannot_be_rewritten_in_parallel(self):
        self.receipt["preserved_open_gap_rows"][0]["evidence"] = "changed"
        self.tables["ega/resid.csv"][0]["evidence"] = "changed"
        self.assertTrue(self.errors())

    def test_current_counts_cannot_be_inflated_even_in_both_places(self):
        for key, field in (("statement_review_snapshot", "source_units"),
                           ("statement_review_snapshot", "full_statement_equivalences"),
                           ("statement_review_snapshot", "distinct_existing_official_tags"),
                           ("residual_snapshot", "open_gaps")):
            self.setUp()
            self.receipt[key][field] += 1
            self.scope[key][field] += 1
            self.assertTrue(self.errors())

    def test_target_roles_cannot_be_swapped(self):
        for key in ("negative_comparison_targets", "supporting_targets"):
            self.setUp()
            self.receipt["pinned_targets"].extend(self.receipt[key])
            self.receipt[key] = []
            self.assertTrue(self.errors())

    def test_retrocompact_target_is_not_whole_corollary_coverage(self):
        self.mutate_both("ega/smap.csv", "edge_id", "S001417", official_tag="0CNG",
                         stacks_label="morphisms-lemma-scheme-theoretic-image-of-partial-section",
                         stacks_file="morphisms.tex")
        self.assertTrue(self.errors())

    def test_official_and_integrated_targets_are_separately_pinned(self):
        self.assertNotEqual(
            next(t for t in self.receipt["pinned_targets"] if t["tag"] == "01JB")["sha256"],
            next(t for t in self.receipt["integrated_targets"] if t["tag"] == "01JB")["sha256"])
        self.receipt["integrated_targets"] = (copy.deepcopy(self.receipt["pinned_targets"])
            + copy.deepcopy(self.receipt["negative_comparison_targets"])
            + copy.deepcopy(self.receipt["supporting_targets"]))
        self.assertTrue(self.errors())

    def test_target_loader_cannot_substitute_official_for_integrated(self):
        self.blobs[BASE, "schemes.tex"] = self.blobs[UPSTREAM, "schemes.tex"]
        self.assertTrue(self.errors())

    def test_target_loader_detects_integrated_source_damage(self):
        raw = self.blobs[BASE, "schemes.tex"]
        target = next(t for t in self.receipt["integrated_targets"] if t["tag"] == "01J3")
        lines = raw.splitlines(keepends=True)
        block = b"".join(lines[target["lf_line_start"] - 1:target["lf_line_end"]])
        corrupted = block.replace(b"the underlying topological", b"the unverified topological", 1)
        self.assertNotEqual(block, corrupted)
        damaged = (b"".join(lines[:target["lf_line_start"] - 1]) + corrupted
                   + b"".join(lines[target["lf_line_end"]:]))
        self.assertNotEqual(raw, damaged)
        self.blobs[BASE, "schemes.tex"] = damaged
        self.assertTrue(self.errors())

    def test_all_target_inventories_hashes_and_labels_are_fixed(self):
        for role in ("pinned_targets", "negative_comparison_targets", "supporting_targets", "integrated_targets"):
            for mode in ("omit", "rehash", "wrong_label"):
                self.setUp()
                if mode == "omit":
                    self.receipt[role].pop()
                elif mode == "rehash":
                    self.receipt[role][0]["sha256"] = "0" * 64
                else:
                    self.receipt[role][0]["label"] = "schemes-lemma-glue"
                self.assertTrue(self.errors(), (role, mode))

    def test_valid_but_wrong_target_block_cannot_be_rehashed_into_receipt(self):
        target = self.receipt["pinned_targets"][0]
        raw = self.blobs[UPSTREAM, target["path"]].split(b"\n")[0] + b"\n"
        target.update(lf_line_start=1, lf_line_end=1, bytes=len(raw),
                      sha256=hashlib.sha256(raw).hexdigest().upper())
        self.assertTrue(self.errors())

    def test_exact_tag_label_join_is_required(self):
        self.tags[self.receipt["pinned_targets"][0]["label"]] = "0000"
        self.assertTrue(self.errors())

    def test_integrated_target_commit_cannot_drift(self):
        self.receipt["integrated_target_commit"] = UPSTREAM
        self.assertTrue(self.errors())

    def test_no_preserved_input_may_be_omitted_or_rehashed(self):
        self.receipt["preserved_inputs"].pop()
        self.assertTrue(self.errors())
        self.setUp()
        self.receipt["preserved_inputs"][0]["sha256"] = "0" * 64
        self.assertTrue(self.errors())

    def test_exact_append_prefixes_and_historical_postimages(self):
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

    def test_earlier_724_receipt_and_dossier_remain_exact(self):
        for path, size, digest in (
                ("validation/ega-i-7.2.1-7.2.4-semantic-checkpoint-2026-09-07.json",
                 67065, "F78D3E44617A76DDEACFB4D3D2152C1CCB2A08850E12F3D97F7DCCCE10B7F3DA"),
                ("ega/i724.md", 9809, "BC17A0E2E12740C650DF1044EB0AE4AD865E10395091D14E5919E9FCA8EFE91E")):
            raw = (ROOT / path).read_bytes()
            self.assertEqual(len(raw), size)
            self.assertEqual(hashlib.sha256(raw).hexdigest().upper(), digest)

    def test_preserved_sources_and_discovery_match_exact_base(self):
        for item in self.receipt["preserved_inputs"]:
            raw = (ROOT / item["path"]).read_bytes()
            self.assertEqual(raw, subprocess.check_output(
                ["git", "show", BASE + ":" + item["path"]], cwd=ROOT))
            self.assertEqual(len(raw), item["bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest().upper(), item["sha256"])


if __name__ == "__main__":
    unittest.main()
