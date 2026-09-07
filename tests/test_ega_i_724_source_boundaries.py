"""Offline rehashed-adversary tests for exact EGA I7.2.1--4 ownership."""
import copy
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i724_source_boundaries as check


def synthetic_source(language):
    """Synthetic witness text at exact LF positions; never authority evidence."""
    lines = [b"\n"] * (check.NEXT_RANGE[language][1] + 2)
    lines[0] = b"% synthetic boundary fixture, not a source copy\n"
    suffix = "-fr" if language == "fr" else ""
    for number, env, (start, end), (tokens, final) in zip(
            check.NUMBERS, check.ENVIRONMENTS, check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]):
        lines[start - 1] = f"\\begin{{{env}}}[{number}]\n".encode()
        lines[start] = f"\\label{{I.{number}{suffix}}}\n".encode()
        lines[end - 2] = (" ".join(tokens) + " " + final).encode() + b"\n"
        lines[end - 1] = f"\\end{{{env}}}\n".encode()
    for key, (start, end), (initial, tokens, final) in zip(
            check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
        begin, finish = start - 1, end - 1
        if language == "en" and key.endswith(":proof"):
            lines[begin], lines[finish] = b"\\begin{proof}\n", b"\\end{proof}\n"
            begin += 1
            finish -= 1
        text = (initial + " " + " ".join(tokens) + " " + final).encode() + b"\n"
        if not tokens and initial == final:
            text = initial.encode() + b"\n"
        if begin == finish:
            lines[begin] = text
        else:
            lines[begin] = initial.encode() + b"\n"
            lines[finish] = (" ".join(tokens) + " " + final).strip().encode() + b"\n"
    start, end = check.NEXT_RANGE[language]
    lines[start - 1] = b"\\begin{corollary}[7.2.5]\n"
    lines[end - 1] = ("\\label{I.7.2.5" + suffix + "}\n").encode()
    lines[end] = b"following mathematics outside the tranche\n"
    lines[end + 1] = b"\\end{corollary}\n"
    raw = b"".join(lines)
    return raw, check.source_metadata(raw, language)


def damage_span(raw, interval, old, new):
    lines = check.raw_lines(raw)
    start, end = interval
    part = b"".join(lines[start - 1:end])
    assert old in part, (interval, old)
    return b"".join(lines[:start - 1]) + part.replace(old, new) + b"".join(lines[end:])


class SourceBoundary724Tests(unittest.TestCase):
    def test_fixed_complete_source_order_and_semantic_ownership(self):
        self.assertEqual(check.NUMBERS, ("7.2.1", "7.2.2", "7.2.2.1", "7.2.3", "7.2.4"))
        self.assertEqual(check.RANGES["fr"], ((290, 302), (303, 315), (316, 349), (350, 362), (363, 377)))
        self.assertEqual(check.RANGES["en"], ((169, 179), (180, 189), (190, 206), (207, 216), (217, 226)))
        self.assertEqual(check.OWNED_KEYS[5], "ega:I.7.2.2:consequence_and_transition")
        self.assertEqual(check.OWNED_RANGES["fr"][4:6], ((325, 338), (340, 348)))
        self.assertEqual(check.OWNED_RANGES["en"][4:6], ((196, 202), (204, 206)))
        self.assertEqual(check.NEXT_RANGE, {"fr": (378, 379), "en": (227, 228)})

    def test_complete_bilingual_fixtures_pass(self):
        for lang in ("fr", "en"):
            raw, receipt = synthetic_source(lang)
            self.assertEqual(check.verify_source(raw, lang, receipt), [])

    def test_every_statement_clause_required_after_all_hashes_recomputed(self):
        for lang in ("fr", "en"):
            raw, _ = synthetic_source(lang)
            for n, interval, (tokens, final) in zip(check.NUMBERS, check.ENVIRONMENT_RANGES[lang], check.UNIT_WITNESSES[lang]):
                for token in (*tokens, final):
                    with self.subTest(lang=lang, unit=n, token=token):
                        damaged = damage_span(raw, interval, token.encode(), b"omitted statement clause")
                        self.assertTrue(any(n + ": statement semantic witness" in e
                            for e in check.verify_source(damaged, lang, check.source_metadata(damaged, lang))))

    def test_every_owned_intro_proof_and_consequence_clause_required_after_rehash(self):
        for lang in ("fr", "en"):
            raw, _ = synthetic_source(lang)
            for key, interval, (initial, tokens, final) in zip(check.OWNED_KEYS, check.OWNED_RANGES[lang], check.OWNED_WITNESSES[lang]):
                for token in (initial, *tokens, final):
                    with self.subTest(lang=lang, owner=key, token=token):
                        damaged = damage_span(raw, interval, token.encode(), b"omitted owned clause")
                        self.assertTrue(any(key + ":" in e
                            for e in check.verify_source(damaged, lang, check.source_metadata(damaged, lang))))

    def test_numbered_only_slices_cannot_omit_proofs_or_context(self):
        for lang in ("fr", "en"):
            raw, expected = synthetic_source(lang)
            for n, interval in zip(check.NUMBERS, check.ENVIRONMENT_RANGES[lang]):
                altered = copy.deepcopy(expected)
                altered["slices"]["ega:I." + n] = check.raw_span(check.raw_lines(raw), *interval)
                self.assertTrue(any("complete source-order span" in e for e in check.verify_source(raw, lang, altered)))

    def test_owned_span_cannot_be_omitted_truncated_or_rehashed(self):
        for lang in ("fr", "en"):
            raw, expected = synthetic_source(lang)
            for key, (start, end) in zip(check.OWNED_KEYS, check.OWNED_RANGES[lang]):
                altered = copy.deepcopy(expected)
                altered["owned_parts"][key] = check.raw_span(check.raw_lines(raw), start, max(start, end - 1)) if start < end else {}
                self.assertTrue(any(key + ": complete independently owned" in e for e in check.verify_source(raw, lang, altered)))
                del altered["owned_parts"][key]
                self.assertTrue(any("semantic owners" in e for e in check.verify_source(raw, lang, altered)))

    def test_parent_consequence_is_not_nested_lemma_proof(self):
        for lang in ("fr", "en"):
            raw, expected = synthetic_source(lang)
            parts = expected["owned_parts"]
            a, b = "ega:I.7.2.2.1:proof", "ega:I.7.2.2:consequence_and_transition"
            parts[a] = check.raw_span(check.raw_lines(raw), parts[a]["lf_line_start"], parts[b]["lf_line_end"])
            del parts[b]
            problems = check.verify_source(raw, lang, expected)
            self.assertTrue(any("semantic owners" in e for e in problems))
            self.assertTrue(any(a + ": complete independently owned" in e for e in problems))

    def test_parent_package_cannot_drop_nested_proof_or_consequence(self):
        for lang in ("fr", "en"):
            raw, expected = synthetic_source(lang)
            expected["parent_proposition_package"] = expected["slices"]["ega:I.7.2.2"]
            self.assertTrue(any("parent_proposition_package" in e for e in check.verify_source(raw, lang, expected)))

    def test_english_all_proofs_require_both_exact_wrappers(self):
        raw, _ = synthetic_source("en")
        for interval in [r for k, r in zip(check.OWNED_KEYS, check.OWNED_RANGES["en"]) if k.endswith(":proof")]:
            for old, new in ((b"\\begin{proof}", b"missing begin"), (b"\\end{proof}", b"missing end"),
                             (b"\\begin{proof}", b"\\begin{proof} \\begin{proof}")):
                damaged = damage_span(raw, interval, old, new)
                self.assertTrue(any("English proof wrapper" in e
                    for e in check.verify_source(damaged, "en", check.source_metadata(damaged, "en"))))

    def test_comment_hidden_hypotheses_and_proof_tokens_do_not_count(self):
        for lang in ("fr", "en"):
            raw, _ = synthetic_source(lang)
            interval = check.OWNED_RANGES[lang][4]
            token = check.OWNED_WITNESSES[lang][4][1][1]
            damaged = damage_span(raw, interval, token.encode(), b"% " + token.encode())
            self.assertTrue(any("ownership/semantic witness" in e
                for e in check.verify_source(damaged, lang, check.source_metadata(damaged, lang))))

    def test_unowned_separator_prose_cannot_hide_after_rehash(self):
        for lang in ("fr", "en"):
            raw, _ = synthetic_source(lang)
            for n in (check.RANGES[lang][0][1], check.RANGES[lang][-1][1]):
                lines = check.raw_lines(raw)
                lines[n - 1] = b"unassigned proof continuation\n"
                damaged = b"".join(lines)
                self.assertTrue(any("unowned substantive source line" in e
                    for e in check.verify_source(damaged, lang, check.source_metadata(damaged, lang))))

    def test_next_boundary_markers_required_and_unique(self):
        for lang in ("fr", "en"):
            raw, expected = synthetic_source(lang)
            for n in check.NEXT_RANGE[lang]:
                lines = check.raw_lines(raw)
                marker = lines[n - 1]
                lines[n - 1] = b"missing next marker\n"
                damaged = b"".join(lines)
                self.assertTrue(any("next excluded marker" in e
                    for e in check.verify_source(damaged, lang, check.source_metadata(damaged, lang))))
                duplicate = raw + marker
                self.assertTrue(any("next excluded marker" in e
                    for e in check.verify_source(duplicate, lang, check.source_metadata(duplicate, lang))))

    def test_next_mathematics_is_excluded_not_adjudicated(self):
        for lang in ("fr", "en"):
            raw, _ = synthetic_source(lang)
            damaged = raw.replace(b"following mathematics outside the tranche", b"different later theorem")
            self.assertEqual(check.verify_source(damaged, lang, check.source_metadata(damaged, lang)), [])

    def test_combined_cannot_absorb_next_unit(self):
        raw, expected = synthetic_source("fr")
        expected["combined"] = check.raw_span(check.raw_lines(raw), 290, 379)
        self.assertTrue(any("combined: complete source-order" in e for e in check.verify_source(raw, "fr", expected)))

    def test_missing_duplicate_misnumbered_or_early_closing_environment_rejected(self):
        raw, expected = synthetic_source("fr")
        for damaged in (raw.replace(b"\\label{I.7.2.2.1-fr}", b"\\label{I.7.2.2.10-fr}"),
                        raw.replace(b"\\begin{lemma}[7.2.2.1]", b"\\begin{lemma}[7.2.2.10]"),
                        raw + b"\\begin{lemma}[7.2.2.1]\n",
                        raw.replace(b"\\end{lemma}", b"omitted closing lemma")):
            self.assertTrue(check.verify_source(damaged, "fr", expected))
        lines = check.raw_lines(raw)
        lines[318] = b"\\end{lemma}\n"
        damaged = b"".join(lines)
        self.assertTrue(any("complete numbered environment boundary" in e
            for e in check.verify_source(damaged, "fr", check.source_metadata(damaged, "fr"))))

    def test_extra_numbered_environment_breaks_exact_source_order(self):
        raw, _ = synthetic_source("fr")
        lines = check.raw_lines(raw)
        lines[325] = b"\\begin{env}[7.2.2.2]\n"
        damaged = b"".join(lines)
        self.assertTrue(any("next numbered begin" in e
            for e in check.verify_source(damaged, "fr", check.source_metadata(damaged, "fr"))))

    def test_physical_lf_and_full_next_boundary_required(self):
        raw, expected = synthetic_source("fr")
        for damaged in (raw.replace(b"\n", b"\r\n"), raw[:-1], b"", "not bytes"):
            self.assertTrue(check.verify_source(damaged, "fr", expected))
        self.assertTrue(any("following 7.2.5" in e
            for e in check.verify_source(b"".join(check.raw_lines(raw)[:377]), "fr", expected)))
        damaged = raw.replace(b"synthetic", b"synthetic\x0c\xe2\x80\xa8", 1)
        self.assertEqual(check.verify_source(damaged, "fr", check.source_metadata(damaged, "fr")), [])

    def test_bad_identity_inventory_language_or_receipt_fails_closed(self):
        raw, expected = synthetic_source("fr")
        for key, value in (("slices", []), ("numbered_environments", None), ("owned_parts", {}),
                ("full_bytes", True), ("full_sha256", "0" * 64), ("url", "https://example.invalid/")):
            self.assertTrue(check.verify_source(raw, "fr", dict(expected, **{key: value})))
        self.assertTrue(check.verify_source(raw, "other", expected))
        self.assertTrue(check.verify_source(raw, "fr", []))

    def test_invalid_span_intervals_fail_closed(self):
        for interval in ((0, 1), (1, 3), (2, 1), (True, 1), (1, False), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span([b"a\n", b"b\n"], *interval)


class BoundedReplay724Tests(unittest.TestCase):
    def test_cached_route_reads_once_without_network(self):
        raw, expected = synthetic_source("fr")
        cached = MagicMock(spec=Path)
        handle = cached.open.return_value.__enter__.return_value
        handle.read.return_value = raw
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            self.assertEqual(check.read_source(expected, "fr", cached), raw)
        handle.read.assert_called_once_with(len(raw) + 1)

    def test_live_route_reads_once_with_fixed_url_timeout_and_size(self):
        raw, expected = synthetic_source("en")
        response = MagicMock()
        response.__enter__.return_value.read.return_value = raw
        with patch.object(check, "urlopen", return_value=response) as fetch:
            self.assertEqual(check.read_source(expected, "en"), raw)
        fetch.assert_called_once_with(check.SOURCE_URLS["en"], timeout=30)
        response.__enter__.return_value.read.assert_called_once_with(len(raw) + 1)

    def test_bad_bounds_or_url_fail_before_network(self):
        _, expected = synthetic_source("fr")
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            for size in (0, -1, True, "38226", check.MAX_SOURCE_BYTES + 1):
                with self.assertRaises(ValueError):
                    check.read_source(dict(expected, full_bytes=size), "fr")
            with self.assertRaises(ValueError):
                check.read_source(dict(expected, url="https://example.invalid/"), "fr")

    def test_cli_bilingual_replay(self):
        fixtures = {lang: synthetic_source(lang) for lang in ("fr", "en")}
        receipt = {"languages": {lang: pair[1] for lang, pair in fixtures.items()}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=lambda expected, lang, cache: fixtures[lang][0]) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "fr.tex", "--english", "en.tex"]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "PASS")

    def test_cli_malformed_receipt_never_fetches(self):
        for value in ("{}", "[]", "{", '{"languages":[]}', '{"languages":{"fr":{}}}'):
            with patch.object(Path, "read_text", return_value=value), patch.object(check, "read_source") as read, \
                    patch("sys.stdout", new_callable=io.StringIO):
                self.assertTrue(check.main([]))
                read.assert_not_called()

    def test_cli_read_failures_have_no_retries(self):
        receipt = {"languages": {lang: synthetic_source(lang)[1] for lang in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO):
            self.assertTrue(check.main([]))
        self.assertEqual(read.call_count, 2)


if __name__ == "__main__":
    unittest.main()
