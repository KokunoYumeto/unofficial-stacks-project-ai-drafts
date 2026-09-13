"""Small in-memory immutable Git fixtures: no production mutation or builds."""
from copy import deepcopy
import hashlib
import unittest
from unittest.mock import patch
from pathlib import Path

import ai_source_correction_composition as c
import direct_successor_composition as d
from test_direct_successor_composition import FixtureGit, raw
import test_direct_successor_composition as baseline
import subprocess


class CorrectionGit(FixtureGit):
    def text(self, *args):
        if args[:4] == ("ls-tree", "-r", "--name-only", c.CORRECTED):
            return "\n".join(sorted(p for p in self.commits[c.CORRECTED] if p.startswith("illusie_volume_I/")))
        return super().text(*args)


class CorrectionFixture:
    def __init__(self):
        self.git = CorrectionGit()
        self.parent = "a" * 40
        self.old = {"simplicial.tex": b"old root\n"}
        self.old.update({"illusie_volume_I/file%02d.txt" % i: b"old\n" for i in range(20)})
        self.old.update({d.OVERLAYS: b"registry\n", d.LEASES: b"leases\n",
                         c.SEALED_RECEIPT: b"sealed receipt\n", c.RECEIPT: b"sealed receipt\n"})
        self.git.add(self.parent, None, self.old)
        changes = {p: b"new " + value for p, value in self.old.items()
                   if p == "simplicial.tex" or p.startswith("illusie_volume_I/")}
        self.git.add(c.CANDIDATE, self.parent, changes)
        self.git.add(c.SEALED, self.parent, {})
        self.git.add(c.CORRECTED, c.SEALED, changes)
        self.proof_path = "validation/direct-successor-actual-proof.json"
        self.review_path = "validation/direct-successor-reviewed-correction.json"
        proof = raw({"status": "PASS", "actual_review": True})
        proof_ref = {"path": self.proof_path, **d.identity(proof)}
        self.review = {"schema": c.REVIEW_SCHEMA, "status": "PASS", "candidate_commit": c.CANDIDATE,
                       "candidate_tree": self.git.tree(c.CANDIDATE), "source_commit": c.CORRECTED,
                       "source_tree": self.git.tree(c.CORRECTED), "reviewed_claims": c.CLAIMS,
                       "unresolved_defects": [], "evidence": [proof_ref]}
        self.loci = [{"unit_id": claim, "source": "simplicial.tex", "start_byte": 0,
                      "end_byte_exclusive": len(changes["simplicial.tex"]),
                      "sha256": d.identity(changes["simplicial.tex"])["sha256"]} for claim in c.CLAIMS]
        self.review["visual_loci"] = self.loci
        review_raw = raw(self.review)
        self.review_ref = {"path": self.review_path, **d.identity(review_raw)}
        self.manifest = {"schema": c.MANIFEST_SCHEMA, "status": "PASS", "correction_id": c.CORRECTION_ID,
                         "candidate": {"commit": c.CANDIDATE, "tree": self.git.tree(c.CANDIDATE), "parent": self.parent},
                         "source": {"commit": c.CORRECTED, "tree": self.git.tree(c.CORRECTED), "parent": c.SEALED},
                         "files": c.changed_rows(self.git, c.SEALED, c.CORRECTED),
                         "dossier": [{"path": p, **self.git.ident(c.CORRECTED, p)} for p in sorted(changes)]
                                      + [proof_ref, self.review_ref], "independent_review": self.review_ref,
                         "visual_loci": self.loci}
        self.head = "f" * 40
        self.git.add(self.head, c.CORRECTED, {self.proof_path: proof, self.review_path: review_raw,
                                           c.MANIFEST: raw(self.manifest)})

    def validate(self):
        with patch.object(c, "SEALED_RECEIPT_SHA256", d.identity(b"sealed receipt\n")["sha256"]):
            return c.validate_manifest(self.git, self.manifest, self.head)


class CandidateReplayTests(unittest.TestCase):
    def setUp(self):
        self.f = CorrectionFixture()

    def test_exact_candidate_21_paths_and_review_closure(self):
        protected = self.f.validate()
        self.assertEqual(len(self.f.manifest["files"]), 21)
        self.assertEqual(len(protected), 23)

    def test_wrong_parent(self):
        self.f.manifest["source"]["parent"] = self.f.parent
        with self.assertRaisesRegex(ValueError, "parent"):
            self.f.validate()

    def test_wrong_candidate(self):
        self.f.manifest["candidate"]["commit"] = c.SEALED
        self.f.manifest["candidate"]["tree"] = self.f.git.tree(c.SEALED)
        with self.assertRaisesRegex(ValueError, "identity"):
            self.f.validate()

    def test_changed_source_preimage(self):
        self.f.git.commits[c.SEALED]["simplicial.tex"] = b"drift\n"
        with self.assertRaisesRegex(ValueError, "preimage"):
            self.f.validate()

    def test_changed_source_postimage(self):
        self.f.git.commits[c.CORRECTED]["simplicial.tex"] = b"different\n"
        self.f.manifest["source"]["tree"] = self.f.git.tree(c.CORRECTED)
        with self.assertRaisesRegex(ValueError, "postimage"):
            self.f.validate()

    def test_manifest_inventory_incomplete(self):
        self.f.manifest["files"].pop()
        with self.assertRaisesRegex(ValueError, "inventory"):
            self.f.validate()

    def test_unrelated_source_path(self):
        self.f.git.commits[c.CORRECTED]["other.tex"] = b"not permitted\n"
        self.f.manifest["source"]["tree"] = self.f.git.tree(c.CORRECTED)
        with self.assertRaisesRegex(ValueError, "unrelated"):
            self.f.validate()

    def test_missing_unchanged_dossier_file(self):
        self.f.manifest["dossier"].pop(0)
        with self.assertRaisesRegex(ValueError, "closure"):
            self.f.validate()

    def test_dossier_hash_drift(self):
        self.f.manifest["dossier"][0]["sha256"] = "B" * 64
        with self.assertRaisesRegex(ValueError, "identity"):
            self.f.validate()

    def test_late_source_drift(self):
        self.f.git.commits[self.f.head]["simplicial.tex"] = b"unreviewed\n"
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            self.f.validate()

    def test_registry_drift(self):
        self.f.git.commits[self.f.head][d.OVERLAYS] = b"changed\n"
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            self.f.validate()

    def test_old_receipt_cannot_be_rewritten_as_metadata(self):
        self.f.git.commits[self.f.head][c.SEALED_RECEIPT] = b"relabelled\n"
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            self.f.validate()

    def test_no_missing_I14_acceptance(self):
        self.f.review["reviewed_claims"] = [c.CLAIMS[0]]
        self.f.git.commits[self.f.head][self.f.review_path] = raw(self.f.review)
        self.f.review_ref.update(d.identity(raw(self.f.review)))
        with self.assertRaisesRegex(ValueError, "both claims"):
            self.f.validate()

    def test_review_evidence_cannot_be_omitted_from_dossier(self):
        self.f.manifest["dossier"] = [r for r in self.f.manifest["dossier"] if r["path"] != self.f.proof_path]
        with self.assertRaisesRegex(ValueError, "not closed"):
            self.f.validate()

    def test_missing_correction_visual_unit(self):
        self.f.manifest["visual_loci"] = self.f.loci[:1]
        with self.assertRaisesRegex(ValueError, "visual units incomplete"):
            self.f.validate()

    def test_drifted_correction_visual_interval(self):
        self.f.manifest["visual_loci"] = deepcopy(self.f.loci)
        self.f.manifest["visual_loci"][0]["sha256"] = "A" * 64
        with self.assertRaisesRegex(ValueError, "interval hash"):
            self.f.validate()


class ScopeTests(unittest.TestCase):
    def setUp(self):
        self.scope = {"correction_id": c.CORRECTION_ID, "candidate_commit": c.CANDIDATE, "candidate_tree": "a" * 40,
            "manifest": {"path": c.MANIFEST, "bytes": 20, "sha256": "A" * 64, "git_blob": "a" * 40},
            "corrected_source_commit": c.CORRECTED, "corrected_source_tree": "b" * 40,
            "sealed_predecessor_commit": c.SEALED, "sealed_predecessor_receipt_sha256": c.SEALED_RECEIPT_SHA256}

    def test_scope_exact(self):
        c.validate_ai_source_correction_scope(self.scope, source_commit=c.CORRECTED, source_tree="b" * 40)

    def test_wrong_source(self):
        with self.assertRaisesRegex(ValueError, "source commit"):
            c.validate_ai_source_correction_scope(self.scope, source_commit=c.SEALED)

    def test_extra_field_rejected(self):
        self.scope["bypass"] = True
        with self.assertRaisesRegex(ValueError, "shape"):
            c.validate_ai_source_correction_scope(self.scope)

    def test_boolean_size_rejected(self):
        self.scope["manifest"]["bytes"] = True
        with self.assertRaisesRegex(ValueError, "byte count"):
            c.validate_ai_source_correction_scope(self.scope)


class HistoricalEndpointTests(unittest.TestCase):
    def test_full_historical_derivation_keeps_endpoint_when_live_source_is_newer(self):
        f, endpoint, inventory, projection = baseline.FullDeriveFixtureTests().prepare()
        later = "6" * 40
        f.git.add(later, endpoint, {"groupoids.tex": b"later AI correction\n"})
        old_clean = f.git.clean_file
        def endpoint_clean(commit, path, exact=False):
            if d._helper.ROOT_TEX.fullmatch(path):
                d.require(f.git.ident(commit, path) == f.git.ident(endpoint, path), "historical source drift")
            else:
                old_clean(commit, path, exact=exact)
        f.git.clean_file = endpoint_clean
        result = subprocess.CompletedProcess([], 0, stdout=raw(projection), stderr=b"")
        with patch.object(d, "HistoricalEndpointGit", return_value=f.git), \
             patch.object(d._helper, "target_inventory", return_value=inventory), \
             patch.object(d.subprocess, "run", return_value=result):
            receipt, evidence = d.derive(f.git.root, f.base, f.admission, endpoint, validation_endpoint=endpoint)
        self.assertEqual(receipt["composition"]["source_commit"], endpoint)
        self.assertEqual(projection["check_revision"], endpoint)
        self.assertFalse(evidence["claims"]["build_started"])

    def test_default_derivation_rejects_same_unregistered_later_source(self):
        f, endpoint, _, _ = baseline.FullDeriveFixtureTests().prepare()
        f.git.add("6" * 40, endpoint, {"groupoids.tex": b"later AI correction\n"})
        with patch.object(d, "Git", return_value=f.git), self.assertRaisesRegex(ValueError, "unsupported path"):
            d.derive(f.git.root, f.base, f.admission, endpoint)

    def test_historical_root_compares_exact_objects_without_live_read(self):
        git = object.__new__(d.HistoricalEndpointGit)
        git.endpoint = "endpoint"
        git.ident = lambda revision, path: {"hash": "same"}
        git.clean_file("source", "simplicial.tex")

    def test_historical_root_drift_rejected(self):
        git = object.__new__(d.HistoricalEndpointGit)
        git.endpoint = "endpoint"
        git.ident = lambda revision, path: {"hash": revision}
        with self.assertRaisesRegex(ValueError, "endpoint root differs"):
            git.clean_file("source", "simplicial.tex")

    def test_historical_nonroot_still_checks_live_input(self):
        git = object.__new__(d.HistoricalEndpointGit)
        git.endpoint = "endpoint"
        with patch.object(d.Git, "clean_file") as live:
            git.clean_file("source", "ai-integrated/registry/overlays.json", exact=True)
        live.assert_called_once_with("source", "ai-integrated/registry/overlays.json", exact=True)

    def test_v1_metadata_never_allows_source_even_with_ai_tools(self):
        f = CorrectionFixture()
        with self.assertRaisesRegex(ValueError, "unsupported path"):
            d.validate_metadata_suffix(f.git, c.SEALED, c.CORRECTED, additional_tools=d.AI_PREPARATION_TOOLS)


if __name__ == "__main__":
    unittest.main()
