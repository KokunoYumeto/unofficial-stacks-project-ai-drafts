"""Offline adversarial tests for EGA I 7.1.10--7.1.14 source ownership.

Synthetic fixtures deliberately permit recomputation of every receipt hash.
They test the independent boundary/semantic contract rather than relying on
the whole-file hash to catch damaged statements, proofs, or next-unit context.
"""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i711014_source_boundaries as check


def metadata(raw, language):
    """Rehash even damaged synthetic fixtures; verification remains separate."""
    return check.source_metadata(raw, language)


def synthetic_source(language):
    """Small offline semantic fixture at the immutable physical-LF boundaries."""
    lines = [b"\n"] * (check.NEXT_CONTEXT_RANGES[language]["boundary"][1] + 2)
    lines[0] = b"% synthetic fixture, not an authority copy\n"
    suffix = "-fr" if language == "fr" else ""
    for number, env, (start, end), (required, final) in zip(
            check.NUMBERS, check.ENVIRONMENTS, check.ENVIRONMENT_RANGES[language],
            check.UNIT_WITNESSES[language]):
        lines[start - 1] = f"\\begin{{{env}}}[{number}]\n".encode()
        lines[start] = f"\\label{{I.{number}{suffix}}}\n".encode()
        lines[end - 2] = (" ".join(required) + " " + final).encode() + b"\n"
        lines[end - 1] = f"\\end{{{env}}}\n".encode()
    for key, (start, end), (initial, tokens, final) in zip(
            check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
        for n in range(start - 1, end):
            lines[n] = b"\n"
        begin, finish = start - 1, end - 1
        if language == "en" and key.endswith(":proof"):
            lines[begin] = b"\\begin{proof}\n"
            lines[finish] = b"\\end{proof}\n"
            begin += 1
            finish -= 1
        text = (initial + " " + " ".join(tokens) + " " + final).encode() + b"\n"
        # Page markers and introductions have no hidden duplicate text.
        if not tokens and initial == final:
            text = initial.encode() + b"\n"
        if begin == finish:
            lines[begin] = text
        else:
            lines[begin] = initial.encode() + b"\n"
            lines[finish] = (" ".join(tokens) + " " + final).encode() + b"\n"
    intro_start, intro_end = check.NEXT_CONTEXT_RANGES[language]["introduction"]
    initial, tokens, final = check.NEXT_WITNESSES[language]
    if intro_start == intro_end:
        lines[intro_start - 1] = (initial + " " + " ".join(tokens) + " " + final).encode() + b"\n"
    else:
        lines[intro_start - 1] = initial.encode() + b"\n"
        lines[intro_end - 1] = (" ".join(tokens) + " " + final).encode() + b"\n"
    begin, label = check.NEXT_CONTEXT_RANGES[language]["boundary"]
    lines[begin - 1] = b"\\begin{corollary}[7.1.15]\n"
    lines[label - 1] = f"\\label{{I.7.1.15{suffix}}}\n".encode()
    lines[label] = b"next numbered statement, not adjudicated here\n"
    lines[label + 1] = b"\\end{corollary}\n"
    raw = b"".join(lines)
    return raw, metadata(raw, language)


def replace_in_interval(raw, interval, old, new):
    """Damage only one independently owned part; preserve physical LF count."""
    lines = check.raw_lines(raw)
    start, end = interval
    part = b"".join(lines[start - 1:end])
    assert old in part, (interval, old)
    return b"".join(lines[:start - 1]) + part.replace(old, new) + b"".join(lines[end:])


class SourceBoundary711014Tests(unittest.TestCase):
    def test_fixed_physical_boundary_contract(self):
        self.assertEqual(check.NUMBERS, ("7.1.10", "7.1.11", "7.1.12", "7.1.13", "7.1.14"))
        self.assertEqual(check.RANGES["fr"], ((192, 205), (206, 220), (221, 231), (232, 243), (244, 258)))
        self.assertEqual(check.RANGES["en"], ((100, 106), (107, 118), (119, 128), (129, 139), (140, 149)))
        self.assertEqual(check.ENVIRONMENT_RANGES["fr"], ((192, 204), (207, 216), (221, 227), (232, 239), (246, 253)))
        self.assertEqual(check.ENVIRONMENT_RANGES["en"], ((100, 105), (108, 113), (119, 123), (129, 134), (141, 144)))
        self.assertEqual(check.OWNED_RANGES["fr"], ((194, 203), (206, 206), (218, 219), (229, 230), (241, 242), (244, 244), (255, 257)))
        self.assertEqual(check.OWNED_RANGES["en"], ((102, 104), (107, 107), (115, 117), (125, 127), (136, 138), (140, 140), (146, 148)))
        self.assertEqual(check.NEXT_CONTEXT_RANGES, {
            "fr": {"introduction": (259, 261), "boundary": (263, 264), "combined": (259, 264)},
            "en": {"introduction": (150, 150), "boundary": (151, 152), "combined": (150, 152)}})

    def test_complete_bilingual_fixtures_pass(self):
        for language in ("fr", "en"):
            with self.subTest(language=language):
                raw, expected = synthetic_source(language)
                self.assertEqual(check.verify_source(raw, language, expected), [])

    def test_environment_only_rehashed_slices_cannot_drop_proofs_or_intros(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            lines = check.raw_lines(raw)
            for number, interval in zip(check.NUMBERS, check.ENVIRONMENT_RANGES[language]):
                with self.subTest(language=language, number=number):
                    changed = copy.deepcopy(expected)
                    changed["slices"]["ega:I." + number] = check.raw_span(lines, *interval)
                    self.assertTrue(any("complete source-order span" in error
                                        for error in check.verify_source(raw, language, changed)))

    def test_rehashed_owned_spans_cannot_drop_final_lines(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            lines = check.raw_lines(raw)
            for key, (start, end) in zip(check.OWNED_KEYS, check.OWNED_RANGES[language]):
                with self.subTest(language=language, key=key):
                    changed = copy.deepcopy(expected)
                    interval = (start, end - 1) if start < end else (start + 1, end + 1)
                    changed["owned_parts"][key] = check.raw_span(lines, *interval)
                    self.assertTrue(any(key + ": complete independently owned" in error
                                        for error in check.verify_source(raw, language, changed)))

    def test_each_statement_token_required_even_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for number, interval, (tokens, _) in zip(
                    check.NUMBERS, check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]):
                for token in tokens:
                    with self.subTest(language=language, number=number, token=token):
                        damaged = replace_in_interval(raw, interval, token.encode(), b"clause omitted")
                        self.assertTrue(any("ega:I." + number + ": final statement semantic witness" in error
                                            for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_each_statement_final_conclusion_required_even_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for number, interval, (_, final) in zip(
                    check.NUMBERS, check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]):
                with self.subTest(language=language, number=number):
                    damaged = replace_in_interval(raw, interval, final.encode(), b"final conclusion omitted")
                    self.assertTrue(any("ega:I." + number + ": final statement semantic witness" in error
                                        for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_each_owned_token_required_even_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for key, interval, (_, tokens, _) in zip(
                    check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                for token in tokens:
                    with self.subTest(language=language, owner=key, token=token):
                        damaged = replace_in_interval(raw, interval, token.encode(), b"semantic token omitted")
                        self.assertTrue(any(key + ": independent ownership/semantic witness" in error
                                            for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_each_owned_final_conclusion_required_even_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for key, interval, (_, _, final) in zip(
                    check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                with self.subTest(language=language, owner=key):
                    damaged = replace_in_interval(raw, interval, final.encode(), b"final conclusion omitted")
                    self.assertTrue(any(key + ": final proof/construction/intro semantic conclusion" in error
                                        for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_rehashed_proof_ownership_swaps_and_unowned_new_parts_rejected(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            parts = expected["owned_parts"]
            a, b = "ega:I.7.1.11:proof", "ega:I.7.1.12:proof"
            parts[a], parts[b] = parts[b], parts[a]
            self.assertTrue(any("independently owned" in error for error in check.verify_source(raw, language, expected)))
            parts["ega:I.7.1.15:introduction"] = parts.pop("ega:I.7.1.14:introduction")
            self.assertTrue(any("independent semantic owners" in error for error in check.verify_source(raw, language, expected)))

    def test_missing_or_duplicated_english_proof_wrappers_rejected_after_rehash(self):
        raw, _ = synthetic_source("en")
        for old, replacement in ((b"\\begin{proof}", b"proof start omitted"),
                                 (b"\\end{proof}", b"proof end omitted"),
                                 (b"\\begin{proof}", b"\\begin{proof} \\begin{proof}"),
                                 (b"\\end{proof}", b"\\end{proof} \\end{proof}")):
            with self.subTest(replacement=replacement):
                damaged = raw.replace(old, replacement, 1)
                self.assertTrue(any("English proof wrapper" in error
                                    for error in check.verify_source(damaged, "en", metadata(damaged, "en"))))

    def test_semantic_witnesses_hidden_in_comments_do_not_count(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            token = "localement noethérien" if language == "fr" else "locally Noetherian"
            damaged = raw.replace(token.encode(), b"% " + token.encode())
            self.assertTrue(any("semantic witness" in error
                                for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_page_marker_and_intro_are_content_not_ignorable_prefixes(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for key in ("ega:I.7.1.11:page-marker", "ega:I.7.1.14:introduction"):
                index = check.OWNED_KEYS.index(key)
                initial = check.OWNED_WITNESSES[language][index][0]
                damaged = replace_in_interval(raw, check.OWNED_RANGES[language][index], initial.encode(), b"")
                self.assertTrue(any(key + ":" in error
                                    for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_numbered_metadata_must_be_separate_from_complete_source_slice(self):
        raw, expected = synthetic_source("fr")
        expected["numbered_environments"]["ega:I.7.1.11"] = expected["slices"]["ega:I.7.1.11"]
        self.assertTrue(any("numbered environment identity" in error
                            for error in check.verify_source(raw, "fr", expected)))

    def test_numbered_close_cannot_move_early_even_with_rehashed_metadata(self):
        raw, _ = synthetic_source("fr")
        lines = check.raw_lines(raw)
        # Move 7.1.11's closing marker into a blank earlier line. Mechanical
        # metadata can still be made, but fixed boundary and tail checks fail.
        lines[212] = b"\\end{proposition}\n"
        damaged = b"".join(lines)
        self.assertTrue(any("complete numbered environment boundary" in error
                            for error in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))

    def test_missing_duplicate_and_wrong_number_markers_fail_closed(self):
        raw, expected = synthetic_source("fr")
        for damaged in (
                raw.replace(b"\\label{I.7.1.11-fr}", b"\\label{I.7.1.110-fr}"),
                raw + b"\\begin{proposition}[7.1.11]\n",
                raw.replace(b"\\begin{corollary}[7.1.12]", b"\\begin{corollary}[7.1.120]"),
                raw.replace(b"\\end{proposition}", b"missing proposition close")):
            self.assertTrue(check.verify_source(damaged, "fr", expected))

    def test_extra_numbered_unit_inside_proof_breaks_source_order(self):
        raw, _ = synthetic_source("fr")
        lines = check.raw_lines(raw)
        lines[216] = b"\\begin{env}[7.1.111]\n"
        damaged = b"".join(lines)
        self.assertTrue(any("next numbered begin" in error
                            for error in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))

    def test_unowned_substantive_text_cannot_replace_blank_separator(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            lines = check.raw_lines(raw)
            lines[check.RANGES[language][0][1] - 1] = b"previously unassigned mathematical claim\n"
            damaged = b"".join(lines)
            self.assertTrue(any("unowned substantive source line" in error
                                for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_excluded_next_intro_and_boundary_inventory_required(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for changed in ({}, {"source_unit": "ega:I.7.1.14"},
                            {"boundary": expected["next_excluded_context"]["boundary"]}):
                altered = dict(expected, next_excluded_context=changed)
                self.assertTrue(any("next excluded" in error for error in check.verify_source(raw, language, altered)))

    def test_rehashed_truncated_next_intro_rejected(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            lines = check.raw_lines(raw)
            start, end = check.NEXT_CONTEXT_RANGES[language]["introduction"]
            altered = copy.deepcopy(expected)
            altered["next_excluded_context"]["introduction"] = check.raw_span(lines, end + 1, end + 1)
            self.assertTrue(any("next excluded" in error for error in check.verify_source(raw, language, altered)))
            initial, tokens, final = check.NEXT_WITNESSES[language]
            for token in (initial, *tokens, final):
                with self.subTest(language=language, token=token):
                    damaged = replace_in_interval(raw, (start, end), token.encode(), b"next context omitted")
                    self.assertTrue(any("next excluded 7.1.15 introduction semantic witness" in error
                                        for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_next_context_cannot_be_silently_absorbed_into_current_scope(self):
        raw, expected = synthetic_source("fr")
        lines = check.raw_lines(raw)
        expected["combined"] = check.raw_span(lines, 192, 264)
        expected["slices"]["ega:I.7.1.14"] = check.raw_span(lines, 244, 264)
        problems = check.verify_source(raw, "fr", expected)
        self.assertTrue(any("combined source-order" in error for error in problems))
        self.assertTrue(any("7.1.14: complete source-order" in error for error in problems))

    def test_missing_or_duplicated_next_boundary_rejected(self):
        raw, expected = synthetic_source("fr")
        for damaged in (raw.replace(b"\\begin{corollary}[7.1.15]", b"\\begin{corollary}[7.1.16]"),
                        raw.replace(b"\\label{I.7.1.15-fr}", b"\\label{I.7.1.16-fr}"),
                        raw + b"\\begin{corollary}[7.1.15]\n"):
            self.assertTrue(any("7.1.15" in error for error in check.verify_source(damaged, "fr", expected)))
        lines = check.raw_lines(raw)
        lines[261] = b"unowned next-intro continuation\n"
        damaged = b"".join(lines)
        self.assertTrue(any("7.1.15 source-order" in error
                            for error in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))

    def test_raw_lf_serialization_and_next_context_presence_required(self):
        raw, expected = synthetic_source("fr")
        for damaged in (raw.replace(b"\n", b"\r\n"), raw[:-1], b"", "not bytes"):
            self.assertTrue(check.verify_source(damaged, "fr", expected))
        damaged = b"".join(check.raw_lines(raw)[:258])
        self.assertTrue(any("following 7.1.15" in error for error in check.verify_source(damaged, "fr", expected)))

    def test_formfeed_unicode_separator_and_comment_percent_are_not_lf(self):
        raw, _ = synthetic_source("fr")
        damaged = raw.replace(b"synthetic", b"synthetic\x0c\xe2\x80\xa8", 1)
        self.assertEqual(check.verify_source(damaged, "fr", metadata(damaged, "fr")), [])

    def test_malformed_receipt_identities_and_inventories_fail_closed(self):
        raw, expected = synthetic_source("fr")
        for field, value in (("slices", []), ("numbered_environments", None), ("owned_parts", "bad"),
                             ("combined", {}), ("full_bytes", True), ("full_sha256", "0" * 64),
                             ("url", "https://example.invalid/mutable")):
            with self.subTest(field=field):
                self.assertTrue(check.verify_source(raw, "fr", dict(expected, **{field: value})))
        self.assertTrue(check.verify_source(raw, "other", expected))
        self.assertTrue(check.verify_source(raw, "fr", []))

    def test_raw_span_rejects_invalid_bounds(self):
        lines = [b"a\n", b"b\n"]
        for interval in ((0, 1), (1, 3), (2, 1), (True, 1), (1, False), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span(lines, *interval)
        self.assertEqual(check.raw_span(lines, 2, 2), {
            "lf_line_start": 2, "lf_line_end": 2, "bytes": 2,
            "sha256": hashlib.sha256(b"b\n").hexdigest().upper(),
            "byte_offset_start": 2, "byte_offset_end_exclusive": 4})


class BoundedReplay711014Tests(unittest.TestCase):
    def test_cached_reads_once_without_network(self):
        raw, expected = synthetic_source("fr")
        cache = MagicMock(spec=Path)
        handle = cache.open.return_value.__enter__.return_value
        handle.read.return_value = raw
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            self.assertEqual(check.read_source(expected, "fr", cache), raw)
        cache.open.assert_called_once_with("rb")
        handle.read.assert_called_once_with(len(raw) + 1)

    def test_live_reads_once_with_fixed_url_and_timeout(self):
        raw, expected = synthetic_source("en")
        response = MagicMock()
        response.__enter__.return_value.read.return_value = raw
        with patch.object(check, "urlopen", return_value=response) as fetch:
            self.assertEqual(check.read_source(expected, "en"), raw)
        fetch.assert_called_once_with(check.SOURCE_URLS["en"], timeout=30)
        response.__enter__.return_value.read.assert_called_once_with(len(raw) + 1)

    def test_invalid_counts_or_unpinned_url_fail_before_read(self):
        _, expected = synthetic_source("fr")
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            for count in (0, -1, True, "38226", check.MAX_SOURCE_BYTES + 1):
                with self.assertRaises(ValueError):
                    check.read_source(dict(expected, full_bytes=count), "fr")
            for language, receipt in (("fr", dict(expected, url="https://example.invalid/")),
                                      ("other", expected), ("fr", [])):
                with self.assertRaises(ValueError):
                    check.read_source(receipt, language)

    def test_cli_bilingual_cached_success_and_exact_schema(self):
        fixtures = {lang: synthetic_source(lang) for lang in ("fr", "en")}
        receipt = {"languages": {lang: value[1] for lang, value in fixtures.items()}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=lambda expected, lang, cache: fixtures[lang][0]) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "cached-fr.tex", "--english", "cached-en.tex"]))
        result = json.loads(output.getvalue())
        self.assertEqual(result["schema"], "ega-i711014-raw-source-boundary-replay/v1")
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(read.call_count, 2)
        self.assertEqual(read.call_args_list[0].args[2], Path("cached-fr.tex"))
        self.assertEqual(read.call_args_list[1].args[2], Path("cached-en.tex"))

    def test_cli_malformed_inventory_does_not_fetch(self):
        for serialized in ("{}", "[]", "{", '{"languages": {"fr": {}}}', '{"languages": []}'):
            with self.subTest(serialized=serialized), \
                    patch.object(Path, "read_text", return_value=serialized), \
                    patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO):
                self.assertTrue(check.main([]))
                read.assert_not_called()

    def test_cli_failed_reads_are_bounded_no_retries(self):
        receipt = {"languages": {lang: synthetic_source(lang)[1] for lang in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(len(json.loads(output.getvalue())["errors"]), 2)


if __name__ == "__main__":
    unittest.main()
