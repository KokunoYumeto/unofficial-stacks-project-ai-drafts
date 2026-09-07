"""Correction contracts and adversarial raw-source environment tests."""
import copy
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import unittest

from tools.check_ega_i713_source_boundaries import verify_source
import tests.test_ega_i_713_semantic as historical713


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "validation/ega-i-7.1.1-7.1.3-source-boundary-correction-2026-09-07.json"
# Public cherry-pick of the immutable pre-correction ledger state. The original
# local candidate hash remains in its receipt, but is not public-clone history.
PUBLIC_PREDECESSOR = "886acaf2fa71dd14b2b4e3850610819260f16959"


class Corrected713Tests(historical713.Semantic713Tests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.frozen = json.loads(RECEIPT.read_text(encoding="utf-8"))
        cls.frozen_scope = json.loads((ROOT / "ega/scope.json").read_text(encoding="utf-8"))
        for entry in cls.frozen["ledgers"]:
            with (ROOT / entry["path"]).open(encoding="utf-8", newline="") as f:
                values = list(csv.DictReader(f))
            superseded = {r["supersedes"] for r in values if r.get("supersedes")}
            key = entry["id_field"]
            cls.frozen_tables[entry["path"]] = [r for r in values if r[key] not in superseded]

    def test_exact_base_prefixes_append_blocks_and_historical_postimages(self):
        # Override the inherited method by its exact name. Bind public history
        # and all immutable receipt hashes without requiring a local-only ref.
        for entry in self.receipt["ledgers"]:
            raw = (ROOT / entry["path"]).read_bytes()
            prefix = subprocess.check_output(
                ["git", "show", PUBLIC_PREDECESSOR + ":" + entry["path"]], cwd=ROOT)
            self.assertTrue(raw.startswith(prefix))
            historical = b"".join(raw.splitlines(keepends=True)[:entry["final_rows"] + 1])
            for data, count, digest in (
                    (prefix, entry["prefix_bytes"], entry["prefix_sha256"]),
                    (historical[len(prefix):], entry["append_bytes"], entry["append_sha256"]),
                    (historical, entry["bytes"], entry["sha256"])):
                self.assertEqual((len(data), hashlib.sha256(data).hexdigest().upper()),
                                 (count, digest))

    def test_preserved_predecessor_is_in_public_lineage(self):
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", PUBLIC_PREDECESSOR, "HEAD"], cwd=ROOT)
        self.assertEqual(result.returncode, 0)

    def test_v1_ranges_rejected_even_with_matching_scope_overlay(self):
        for unit, pair in zip(self.receipt["source_units"], [(6, 15), (16, 52), (53, 64)]):
            self.setUp()
            value = self.receipt["french_authority"]["source_scopes"][unit]
            value["lf_line_start"], value["lf_line_end"] = pair
            self.scope["reviewed_source_slices"][unit] = copy.deepcopy(value)
            self.assertTrue(self.errors())

    def test_actual_raw_restriction_line_is_required(self):
        self.receipt["proposed_source_edition_evidence"]["french_line"] = 36
        self.assertTrue(self.errors())


def synthetic_source(language):
    suffix = "-fr" if language == "fr" else ""
    lines = [b"% harmless preamble\n", b"\n"]
    scopes = {}
    restriction_line = None
    for number in (1, 2, 3):
        env = "definition" if number == 2 else "env"
        start = len(lines) + 1
        lines += [f"\\begin{{{env}}}[7.1.{number}]\n".encode(),
                  f"\\label{{I.7.1.{number}{suffix}}}\n".encode()]
        if number == 2:
            restriction_line = len(lines) + 1
            lines.append(b"U\\cap V\\cap W\n")
            lines.append(b"\\Gamma_{\\mathrm{rat}}((X\\times_S Y)/X)\n" if language == "fr"
                         else b"\\Gamma_\\mathrm{rat}((X\\times_S Y)/X)\n")
        elif number == 3:
            lines.append(b"\\emph{anneau} $R(X)$.\n" if language == "fr"
                         else b"\\emph{ring} $R(X)$.\n")
        else:
            lines.append(b"equivalence witnesses\n")
        lines.append(f"\\end{{{env}}}\n".encode())
        end = len(lines)
        block = b"".join(lines[start-1:end])
        offset = sum(map(len, lines[:start-1]))
        scopes[f"ega:I.7.1.{number}"] = {
            "lf_line_start": start, "lf_line_end": end,
            "byte_offset_start": offset, "byte_offset_end_exclusive": offset + len(block),
            "slice_bytes": len(block), "slice_sha256": hashlib.sha256(block).hexdigest().upper()}
        lines.append(b"\n")
    raw = b"".join(lines)
    expected = {"full_bytes": len(raw), "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
        "slices": scopes, "restriction_line": restriction_line,
        "restriction_line_sha256": hashlib.sha256(lines[restriction_line-1]).hexdigest().upper()}
    return raw, expected


class RawSourceBoundaryTests(unittest.TestCase):
    def test_complete_raw_french_and_english_environments(self):
        for lang in ("fr", "en"):
            raw, expected = synthetic_source(lang)
            self.assertEqual(verify_source(raw, lang, expected), [])

    def test_arbitrary_interval_hashes_do_not_prove_coverage(self):
        raw, expected = synthetic_source("fr")
        lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
        for unit in expected["slices"]:
            changed = copy.deepcopy(expected)
            s = changed["slices"][unit]
            s["lf_line_end"] -= 1
            block = b"".join(lines[s["lf_line_start"]-1:s["lf_line_end"]])
            s["slice_bytes"] = len(block)
            s["slice_sha256"] = hashlib.sha256(block).hexdigest().upper()
            s["byte_offset_end_exclusive"] = s["byte_offset_start"] + len(block)
            self.assertTrue(any("complete raw environment" in e for e in verify_source(raw, "fr", changed)))

    def test_missing_ring_conclusion_is_rejected(self):
        raw, expected = synthetic_source("fr")
        changed = raw.replace(b"\\emph{anneau} $R(X)$.", b"omitted")
        self.assertTrue(any("ring conclusion" in e for e in verify_source(changed, "fr", expected)))

    def test_missing_final_graph_correspondence_is_rejected(self):
        raw, expected = synthetic_source("en")
        changed = raw.replace(b"\\Gamma_\\mathrm{rat}((X\\times_S Y)/X)", b"omitted")
        self.assertTrue(any("correspondence" in e for e in verify_source(changed, "en", expected)))

    def test_wrong_label_duplicate_begin_and_missing_close_rejected(self):
        raw, expected = synthetic_source("fr")
        for changed in (
                raw.replace(b"\\label{I.7.1.3-fr}", b"\\label{I.7.1.4-fr}"),
                raw + b"\\begin{env}[7.1.3]\n",
                raw.replace(b"\\end{definition}\n", b"")):
            self.assertTrue(verify_source(changed, "fr", expected))

    def test_crlf_and_blank_restriction_locator_rejected(self):
        raw, expected = synthetic_source("fr")
        self.assertTrue(verify_source(raw.replace(b"\n", b"\r\n"), "fr", expected))
        expected["restriction_line"] = 2
        expected["restriction_line_sha256"] = hashlib.sha256(b"\n").hexdigest().upper()
        self.assertTrue(any("actual overstatement" in e for e in verify_source(raw, "fr", expected)))

    def test_form_feed_is_not_a_physical_lf_boundary(self):
        raw, expected = synthetic_source("fr")
        raw = raw.replace(b"harmless", b"harmless\x0c")
        expected["full_bytes"] = len(raw)
        expected["full_sha256"] = hashlib.sha256(raw).hexdigest().upper()
        for span in expected["slices"].values():
            span["byte_offset_start"] += 1
            span["byte_offset_end_exclusive"] += 1
        self.assertEqual(verify_source(raw, "fr", expected), [])


if __name__ == "__main__":
    unittest.main()
