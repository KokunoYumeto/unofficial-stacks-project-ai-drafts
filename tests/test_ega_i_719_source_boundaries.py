"""Offline adversarial tests for complete numbered and independently owned spans."""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i719_source_boundaries as check
from tools.ega_raw_source_boundaries import verify_numbered_span


CLOSING_LINES = {
    "fr": (83, 93, 130, 140, 148, 156, 165),
    "en": (43, 49, 66, 73, 79, 85, 91),
}


def metadata(raw, language):
    """Recompute every hash, even for semantically damaged synthetic sources."""
    lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
    suffix = "-fr" if language == "fr" else ""
    return {
        "url": check.SOURCE_URLS[language], "full_bytes": len(raw),
        "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
        "slices": {"ega:I." + number: verify_numbered_span(
            raw, start, end, "I." + number + suffix)
            for number, (start, end) in zip(check.NUMBERS, check.RANGES[language])},
        "owned_parts": {key: check.raw_span(lines, start, end)
                        for key, (start, end) in zip(check.OWNED_KEYS, check.OWNED_RANGES[language])},
        "combined": check.raw_span(lines, check.RANGES[language][0][0], check.RANGES[language][-1][1]),
    }


def synthetic_source(language):
    """Small semantic fixtures at the pinned physical LF boundaries; no network."""
    lines = [b"\n"] * (check.RANGES[language][-1][1] + 4)
    lines[0] = b"% synthetic fixture, not an authority-source copy\n"
    suffix = "-fr" if language == "fr" else ""
    for number, env, (start, _), close, witnesses in zip(
            check.NUMBERS, check.ENVIRONMENTS, check.RANGES[language],
            CLOSING_LINES[language], check.UNIT_WITNESSES[language]):
        lines[start - 1] = f"\\begin{{{env}}}[{number}]\n".encode()
        lines[start] = f"\\label{{I.{number}{suffix}}}\n".encode()
        lines[start + 1] = witnesses[0].encode() + b"\n"
        lines[close - 2] = (witnesses[0] + " " + witnesses[1]).encode() + b"\n"
        lines[close - 1] = f"\\end{{{env}}}\n".encode()
    for key, (start, end), (initial, tokens, final) in zip(
            check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
        for line in range(start - 1, end):
            lines[line] = b"intermediate proof text\n"
        if start == end:
            lines[start - 1] = (initial + " " + " ".join(tokens) + " " + final).encode() + b"\n"
        else:
            lines[start - 1] = initial.encode() + b"\n"
            lines[start] = " ".join(tokens).encode() + b"\n"
            last = end - 1
            if language == "en" and key.endswith(":proof"):
                lines[last] = b"\\end{proof}\n"
                last -= 1
            lines[last] = (" ".join(tokens) + " " + final).encode() + b"\n"
    sentinel = check.RANGES[language][-1][1]
    lines[sentinel] = b"\\begin{env}[7.1.10]\n"
    lines[sentinel + 1] = f"\\label{{I.7.1.10{suffix}}}\n".encode()
    lines[sentinel + 2] = b"following unit, outside the reviewed slice\n"
    lines[sentinel + 3] = b"\\end{env}\n"
    raw = b"".join(lines)
    return raw, metadata(raw, language)


class RawSourceBoundary719Tests(unittest.TestCase):
    def test_fixed_source_range_contract_and_semantic_owners(self):
        self.assertEqual(check.RANGES["fr"], ((72, 84), (85, 114), (115, 131),
                         (132, 141), (142, 149), (150, 159), (160, 191)))
        self.assertEqual(check.RANGES["en"], ((37, 44), (45, 58), (59, 68),
                         (69, 74), (75, 80), (81, 87), (88, 99)))
        self.assertEqual(dict(zip(check.OWNED_KEYS, check.OWNED_RANGES["fr"])), {
            "ega:I.7.1.5:proof": (95, 103), "ega:I.7.1.5:tail": (105, 113),
            "ega:I.7.1.9:deduction": (167, 175), "ega:I.7.1.9.1:proof": (177, 190)})
        self.assertEqual(check.OWNED_RANGES["en"], ((51, 55), (57, 57), (93, 93), (95, 98)))

    def test_complete_french_and_english_sources(self):
        for language in ("fr", "en"):
            with self.subTest(language=language):
                raw, expected = synthetic_source(language)
                self.assertEqual(check.verify_source(raw, language, expected), [])

    def test_valid_hash_environment_only_slices_are_not_complete_source_order(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for number, (start, _), close in zip(check.NUMBERS, check.RANGES[language], CLOSING_LINES[language]):
                with self.subTest(language=language, number=number):
                    changed = copy.deepcopy(expected)
                    suffix = "-fr" if language == "fr" else ""
                    changed["slices"]["ega:I." + number] = verify_numbered_span(
                        raw, start, close, "I." + number + suffix)
                    self.assertTrue(any("complete source-order span identity" in error
                                        for error in check.verify_source(raw, language, changed)))

    def test_valid_hash_truncated_owned_proofs_are_rejected(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
            for key, (start, end) in zip(check.OWNED_KEYS, check.OWNED_RANGES[language]):
                with self.subTest(language=language, owner=key):
                    changed = copy.deepcopy(expected)
                    changed["owned_parts"][key] = check.raw_span(lines, start, max(start, end - 1))
                    if start == end:
                        changed["owned_parts"][key] = check.raw_span(lines, start - 1, end - 1)
                    self.assertTrue(any("independently owned" in error
                                        for error in check.verify_source(raw, language, changed)))

    def test_valid_hash_deduction_cannot_be_owned_exclusively_by_lemma(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            parts = expected["owned_parts"]
            parts["ega:I.7.1.9.1:deduction"] = parts.pop("ega:I.7.1.9:deduction")
            self.assertTrue(any("semantic owners" in error for error in check.verify_source(raw, language, expected)))

    def test_valid_hash_swapped_deduction_and_lemma_proof_owners_rejected(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            parts = expected["owned_parts"]
            a, b = "ega:I.7.1.9:deduction", "ega:I.7.1.9.1:proof"
            parts[a], parts[b] = parts[b], parts[a]
            self.assertTrue(any("independently owned" in error for error in check.verify_source(raw, language, expected)))

    def test_each_owned_semantic_token_required_even_with_recomputed_hashes(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for key, (_, tokens, _) in zip(check.OWNED_KEYS, check.OWNED_WITNESSES[language]):
                for token in tokens:
                    with self.subTest(language=language, owner=key, token=token):
                        changed = raw.replace(token.encode(), b"removed semantic token")
                        expected = metadata(changed, language)
                        self.assertTrue(any(key + ": independent ownership/semantic witness" in error
                                            for error in check.verify_source(changed, language, expected)))

    def test_each_owned_final_conclusion_required_even_with_recomputed_hashes(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for key, (_, _, final) in zip(check.OWNED_KEYS, check.OWNED_WITNESSES[language]):
                with self.subTest(language=language, owner=key):
                    changed = raw.replace(final.encode(), b"conclusion omitted")
                    expected = metadata(changed, language)
                    self.assertTrue(any(key + ": final proof/tail semantic conclusion" in error
                                        for error in check.verify_source(changed, language, expected)))

    def test_each_statement_final_clause_required_even_with_recomputed_hashes(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for number, (_, final) in zip(check.NUMBERS, check.UNIT_WITNESSES[language]):
                with self.subTest(language=language, number=number):
                    changed = raw.replace(final.encode(), b"statement conclusion omitted")
                    expected = metadata(changed, language)
                    self.assertTrue(any("ega:I." + number + ": final statement semantic witness" in error
                                        for error in check.verify_source(changed, language, expected)))

    def test_semantic_tokens_hidden_in_comments_do_not_count(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            token = "est nilpotent" if language == "fr" else "is nilpotent"
            changed = raw.replace(token.encode(), b"% " + token.encode())
            self.assertTrue(any("ownership/semantic witness" in error
                                for error in check.verify_source(changed, language, metadata(changed, language))))

    def test_english_proof_closing_wrapper_cannot_be_omitted(self):
        raw, _ = synthetic_source("en")
        changed = raw.replace(b"\\end{proof}\n", b"omitted proof end\n")
        self.assertTrue(any("English proof wrapper" in error
                            for error in check.verify_source(changed, "en", metadata(changed, "en"))))

    def test_missing_duplicate_or_misnumbered_source_markers_rejected(self):
        raw, expected = synthetic_source("fr")
        for changed in (
                raw.replace(b"\\label{I.7.1.7-fr}", b"\\label{I.7.1.70-fr}"),
                raw + b"\\begin{proposition}[7.1.7]\n",
                raw.replace(b"\\begin{env}[7.1.10]", b"\\begin{env}[7.1.11]"),
                raw.replace(b"\\label{I.7.1.10-fr}", b"\\label{I.7.1.11-fr}"),
                raw.replace(b"\\end{lemma}", b"missing lemma close")):
            self.assertTrue(check.verify_source(changed, "fr", expected))

    def test_extra_numbered_unit_in_proof_is_not_a_valid_source_order(self):
        raw, _ = synthetic_source("fr")
        changed = raw.replace(b"intermediate proof text\n", b"\\begin{env}[7.1.50]\n", 1)
        self.assertTrue(any("next numbered begin" in error
                            for error in check.verify_source(changed, "fr", metadata(changed, "fr"))))

    def test_complete_combined_span_required_with_valid_hash(self):
        raw, expected = synthetic_source("fr")
        lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
        expected["combined"] = check.raw_span(lines, 72, 190)
        self.assertTrue(any("combined" in error for error in check.verify_source(raw, "fr", expected)))

    def test_lf_serialization_and_terminal_boundary_required(self):
        raw, expected = synthetic_source("fr")
        for changed in (raw.replace(b"\n", b"\r\n"), raw[:-1], b""):
            self.assertTrue(check.verify_source(changed, "fr", expected))
        changed = b"\n".join(raw.split(b"\n")[:191]) + b"\n"
        self.assertTrue(any("7.1.10" in error for error in check.verify_source(changed, "fr", expected)))

    def test_form_feed_never_changes_physical_lf_boundaries(self):
        raw, _ = synthetic_source("fr")
        changed = raw.replace(b"synthetic", b"synthetic\x0c", 1)
        self.assertEqual(check.verify_source(changed, "fr", metadata(changed, "fr")), [])

    def test_malformed_receipt_inventories_and_identities_fail_closed(self):
        raw, expected = synthetic_source("fr")
        for field, value in (("slices", []), ("owned_parts", None), ("combined", {}),
                             ("full_bytes", True), ("full_sha256", "0" * 64),
                             ("url", "https://example.invalid/mutable.tex")):
            changed = copy.deepcopy(expected)
            changed[field] = value
            self.assertTrue(check.verify_source(raw, "fr", changed))
        self.assertTrue(check.verify_source(raw, "invalid", expected))
        self.assertTrue(check.verify_source(raw, "fr", []))


class BoundedReplay719Tests(unittest.TestCase):
    def test_cached_reads_are_bounded_and_never_fetch(self):
        raw, expected = synthetic_source("fr")
        cached = MagicMock(spec=Path)
        handle = cached.open.return_value.__enter__.return_value
        handle.read.return_value = raw
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            self.assertEqual(check.read_source(expected, "fr", cached), raw)
        cached.open.assert_called_once_with("rb")
        handle.read.assert_called_once_with(len(raw) + 1)

    def test_live_route_reads_once_with_timeout_and_fixed_url(self):
        raw, expected = synthetic_source("en")
        response = MagicMock()
        response.__enter__.return_value.read.return_value = raw
        with patch.object(check, "urlopen", return_value=response) as fetch:
            self.assertEqual(check.read_source(expected, "en"), raw)
        fetch.assert_called_once_with(check.SOURCE_URLS["en"], timeout=30)
        response.__enter__.return_value.read.assert_called_once_with(len(raw) + 1)

    def test_invalid_bounds_and_unpinned_url_fail_before_open(self):
        _, expected = synthetic_source("fr")
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            for count in (0, -1, True, "38226", check.MAX_SOURCE_BYTES + 1):
                changed = dict(expected, full_bytes=count)
                with self.assertRaises(ValueError):
                    check.read_source(changed, "fr")
            with self.assertRaises(ValueError):
                check.read_source(dict(expected, url="https://example.invalid/"), "fr")

    def test_offline_cli_uses_given_language_contract(self):
        fixtures = {language: synthetic_source(language) for language in ("fr", "en")}
        receipt = {"languages": {language: pair[1] for language, pair in fixtures.items()}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=lambda expected, language, cached: fixtures[language][0]) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "cached-fr.tex", "--english", "cached-en.tex"]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "PASS")
        self.assertEqual(read.call_args_list[0].args[2], Path("cached-fr.tex"))

    def test_bad_receipt_or_failed_fetch_returns_failure_without_retry(self):
        with patch.object(Path, "read_text", return_value="{}"), \
                patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO):
            self.assertTrue(check.main([]))
            read.assert_not_called()
        receipt = {"languages": {language: synthetic_source(language)[1] for language in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(len(json.loads(output.getvalue())["errors"]), 2)


if __name__ == "__main__":
    unittest.main()
