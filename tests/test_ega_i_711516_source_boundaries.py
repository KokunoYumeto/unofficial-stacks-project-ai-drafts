"""Offline, rehashed-adversary tests for complete EGA I 7.1.15--7.1.16."""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i711516_source_boundaries as check


def metadata(raw, language):
    """Recompute every hash even for damaged synthetic source bytes."""
    return check.source_metadata(raw, language)


def synthetic_source(language):
    """Small synthetic clauses at fixed physical LF lines, never authority text."""
    lines = [b"\n"] * (check.NEXT_CONTEXT_RANGES[language]["boundary"][1] + 2)
    lines[0] = b"% synthetic fixture, not a source-authority copy\n"
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
        begin, finish = start - 1, end - 1
        if language == "en" and key.endswith(":proof"):
            lines[begin] = b"\\begin{proof}\n"
            lines[finish] = b"\\end{proof}\n"
            begin += 1
            finish -= 1
        text = (initial + " " + " ".join(tokens) + " " + final).encode() + b"\n"
        if not tokens and initial == final:
            text = initial.encode() + b"\n"
        if begin == finish:
            lines[begin] = text
        else:
            lines[begin] = initial.encode() + b"\n"
            lines[finish] = (" ".join(tokens) + " " + final).encode() + b"\n"
    for n, marker in check.NEXT_MARKERS[language]:
        lines[n - 1] = marker.encode() + b"\n"
    end = check.NEXT_CONTEXT_RANGES[language]["boundary"][1]
    lines[end] = b"next mathematics not adjudicated in this tranche\n"
    lines[end + 1] = b"\\end{env}\n"
    raw = b"".join(lines)
    return raw, metadata(raw, language)


def replace_in_interval(raw, interval, old, new):
    lines = check.raw_lines(raw)
    start, end = interval
    part = b"".join(lines[start - 1:end])
    assert old in part, (interval, old)
    return b"".join(lines[:start - 1]) + part.replace(old, new) + b"".join(lines[end:])


class SourceBoundary711516Tests(unittest.TestCase):
    def test_fixed_source_and_ownership_boundaries(self):
        self.assertEqual(check.NUMBERS, ("7.1.15", "7.1.16"))
        self.assertEqual(check.RANGES, {"fr": ((259, 278), (279, 289)), "en": ((150, 161), (162, 168))})
        self.assertEqual(check.ENVIRONMENT_RANGES, {"fr": ((263, 272), (281, 288)), "en": ((151, 156), (163, 167))})
        self.assertEqual(check.OWNED_KEYS, ("ega:I.7.1.15:introduction", "ega:I.7.1.15:proof", "ega:I.7.1.16:introduction"))
        self.assertEqual(check.OWNED_RANGES, {"fr": ((259, 261), (274, 277), (279, 279)),
                                            "en": ((150, 150), (158, 160), (162, 162))})
        self.assertEqual(check.NEXT_CONTEXT_RANGES, {
            "fr": {"heading": (290, 290), "labels": (291, 291), "boundary": (293, 294), "combined": (290, 294)},
            "en": {"heading": (169, 169), "labels": (170, 171), "boundary": (173, 174), "combined": (169, 174)}})

    def test_complete_bilingual_synthetic_sources_pass(self):
        for language in ("fr", "en"):
            with self.subTest(language=language):
                raw, expected = synthetic_source(language)
                self.assertEqual(check.verify_source(raw, language, expected), [])

    def test_numbered_only_slices_cannot_omit_introductions_or_proof(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for number, interval in zip(check.NUMBERS, check.ENVIRONMENT_RANGES[language]):
                with self.subTest(language=language, number=number):
                    altered = copy.deepcopy(expected)
                    altered["slices"]["ega:I." + number] = check.raw_span(check.raw_lines(raw), *interval)
                    self.assertTrue(any("complete source-order span" in error
                                        for error in check.verify_source(raw, language, altered)))

    def test_rehashed_proof_and_intro_slices_cannot_truncate_final_line(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            lines = check.raw_lines(raw)
            for key, (start, end) in zip(check.OWNED_KEYS, check.OWNED_RANGES[language]):
                with self.subTest(language=language, owner=key):
                    altered = copy.deepcopy(expected)
                    interval = (start, end - 1) if start < end else (start + 1, end + 1)
                    altered["owned_parts"][key] = check.raw_span(lines, *interval)
                    self.assertTrue(any(key + ": complete independently owned" in error
                                        for error in check.verify_source(raw, language, altered)))

    def test_every_statement_clause_required_even_after_all_hashes_recomputed(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for number, interval, (tokens, _) in zip(
                    check.NUMBERS, check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]):
                for token in tokens:
                    with self.subTest(language=language, number=number, token=token):
                        damaged = replace_in_interval(raw, interval, token.encode(), b"clause omitted")
                        self.assertTrue(any("ega:I." + number + ": final statement semantic witness" in error
                                            for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_every_final_statement_conclusion_required_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for number, interval, (_, final) in zip(
                    check.NUMBERS, check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]):
                damaged = replace_in_interval(raw, interval, final.encode(), b"conclusion omitted")
                self.assertTrue(any("ega:I." + number + ": final statement semantic witness" in error
                                    for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_each_proof_or_intro_clause_required_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for key, interval, (_, tokens, _) in zip(
                    check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                for token in tokens:
                    with self.subTest(language=language, owner=key, token=token):
                        damaged = replace_in_interval(raw, interval, token.encode(), b"proof clause omitted")
                        self.assertTrue(any(key + ": independent ownership/semantic witness" in error
                                            for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_each_proof_or_intro_final_conclusion_required_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for key, interval, (_, _, final) in zip(
                    check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                damaged = replace_in_interval(raw, interval, final.encode(), b"final proof conclusion omitted")
                self.assertTrue(any(key + ": final proof/intro semantic conclusion" in error
                                    for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_geometric_point_term_cannot_be_silently_rewritten_in_source_evidence(self):
        for language, historical in (("fr", "points géométriques"), ("en", "geometric points")):
            raw, _ = synthetic_source(language)
            damaged = raw.replace(historical.encode(), b"modern corrected terminology")
            self.assertTrue(any("final statement semantic witness" in error
                                for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_embedding_tail_is_not_replaceable_by_underlying_point_only(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            token = "$k(s)$-monomorphisme de $k(y)$ dans" if language == "fr" else r"$\kres(s)$-monomorphism from $\kres(y)$ to"
            damaged = replace_in_interval(raw, check.ENVIRONMENT_RANGES[language][0], token.encode(), b"underlying point only")
            self.assertTrue(any("7.1.15: final statement semantic witness" in error
                                for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_wrong_fibre_and_omitted_base_compatibility_rejected(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            old = r"$Y\otimes_S k(s)$" if language == "fr" else r"$Y\otimes_S\kres(s)$"
            damaged = raw.replace(old.encode(), b"$Y$")
            self.assertTrue(any("semantic witness" in error
                                for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_english_proof_requires_both_exact_delimiters(self):
        raw, _ = synthetic_source("en")
        for old, replacement in ((b"\\begin{proof}", b"omitted proof begin"),
                                 (b"\\end{proof}", b"omitted proof close"),
                                 (b"\\begin{proof}", b"\\begin{proof} \\begin{proof}"),
                                 (b"\\end{proof}", b"\\end{proof} \\end{proof}")):
            damaged = raw.replace(old, replacement)
            self.assertTrue(any("English proof wrapper" in error
                                for error in check.verify_source(damaged, "en", metadata(damaged, "en"))))

    def test_comment_hidden_tokens_do_not_count(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            token = "homomorphismes locaux" if language == "fr" else "local"
            damaged = replace_in_interval(raw, check.OWNED_RANGES[language][1], token.encode(), b"% " + token.encode())
            self.assertTrue(any("ownership/semantic witness" in error
                                for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_owner_swaps_or_extra_proof16_inventory_rejected(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            parts = expected["owned_parts"]
            a, b = "ega:I.7.1.15:introduction", "ega:I.7.1.16:introduction"
            parts[a], parts[b] = parts[b], parts[a]
            self.assertTrue(any("independently owned" in error for error in check.verify_source(raw, language, expected)))
            parts["ega:I.7.1.16:proof"] = parts["ega:I.7.1.15:proof"]
            self.assertTrue(any("semantic owners" in error for error in check.verify_source(raw, language, expected)))

    def test_trailing_proof16_or_prose_before_heading_rejected_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for text in (b"additional unwrapped proof\n", b"\\begin{proof}\n"):
                lines = check.raw_lines(raw)
                lines[check.RANGES[language][-1][1] - 1] = text
                damaged = b"".join(lines)
                problems = check.verify_source(damaged, language, metadata(damaged, language))
                self.assertTrue(any("trailing proof/content" in error for error in problems))
                self.assertTrue(any("unowned substantive" in error for error in problems))

    def test_each_section_heading_and_label_marker_required_and_unique(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for n, marker in check.NEXT_MARKERS[language]:
                with self.subTest(language=language, line=n):
                    damaged = replace_in_interval(raw, (n, n), marker.encode(), b"missing next marker")
                    self.assertTrue(any("7.2 marker" in error
                                        for error in check.verify_source(damaged, language, metadata(damaged, language))))
                    duplicate = raw + marker.encode() + b"\n"
                    self.assertTrue(any("7.2 marker" in error
                                        for error in check.verify_source(duplicate, language, metadata(duplicate, language))))

    def test_rehashed_next_context_cannot_drop_english_second_label(self):
        raw, expected = synthetic_source("en")
        expected["next_excluded_context"]["labels"] = check.raw_span(check.raw_lines(raw), 170, 170)
        self.assertTrue(any("next excluded 7.2.1 context" in error
                            for error in check.verify_source(raw, "en", expected)))

    def test_unowned_prose_between_section_labels_and_next_unit_rejected(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            lines = check.raw_lines(raw)
            lines[check.NEXT_CONTEXT_RANGES[language]["boundary"][0] - 2] = b"unassigned next introductory prose\n"
            damaged = b"".join(lines)
            self.assertTrue(any("unowned prose before 7.2.1" in error
                                for error in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_next_mathematics_is_excluded_not_semantically_adjudicated(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            damaged = raw.replace(b"next mathematics not adjudicated in this tranche", b"different later theorem prose")
            self.assertEqual(check.verify_source(damaged, language, metadata(damaged, language)), [])

    def test_current_combined_and_unit_spans_cannot_absorb_next_section(self):
        raw, expected = synthetic_source("fr")
        lines = check.raw_lines(raw)
        expected["combined"] = check.raw_span(lines, 259, 294)
        expected["slices"]["ega:I.7.1.16"] = check.raw_span(lines, 279, 294)
        problems = check.verify_source(raw, "fr", expected)
        self.assertTrue(any("combined source-order" in error for error in problems))
        self.assertTrue(any("7.1.16: complete source-order" in error for error in problems))

    def test_missing_duplicate_or_misnumbered_environments_rejected(self):
        raw, expected = synthetic_source("fr")
        for damaged in (raw.replace(b"\\label{I.7.1.15-fr}", b"\\label{I.7.1.150-fr}"),
                        raw.replace(b"\\begin{corollary}[7.1.16]", b"\\begin{corollary}[7.1.160]"),
                        raw + b"\\begin{corollary}[7.1.15]\n",
                        raw.replace(b"\\end{corollary}", b"omitted closing marker", 1)):
            self.assertTrue(check.verify_source(damaged, "fr", expected))

    def test_extra_numbered_unit_in_proof_breaks_source_order(self):
        raw, _ = synthetic_source("fr")
        lines = check.raw_lines(raw)
        lines[274] = b"\\begin{env}[7.1.15.1]\n"
        damaged = b"".join(lines)
        self.assertTrue(any("next numbered begin" in error
                            for error in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))

    def test_early_closing_environment_even_with_rehashed_metadata_rejected(self):
        raw, _ = synthetic_source("fr")
        lines = check.raw_lines(raw)
        lines[266] = b"\\end{corollary}\n"
        damaged = b"".join(lines)
        self.assertTrue(any("complete numbered environment boundary" in error
                            for error in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))

    def test_physical_lf_only_and_sufficient_next_context_required(self):
        raw, expected = synthetic_source("fr")
        for damaged in (raw.replace(b"\n", b"\r\n"), raw[:-1], b"", "not bytes"):
            self.assertTrue(check.verify_source(damaged, "fr", expected))
        damaged = b"".join(check.raw_lines(raw)[:289])
        self.assertTrue(any("following 7.2 heading" in error for error in check.verify_source(damaged, "fr", expected)))
        damaged = raw.replace(b"synthetic", b"synthetic\x0c\xe2\x80\xa8", 1)
        self.assertEqual(check.verify_source(damaged, "fr", metadata(damaged, "fr")), [])

    def test_bad_identity_inventory_or_nonobject_receipt_fails_closed(self):
        raw, expected = synthetic_source("fr")
        for field, value in (("slices", []), ("numbered_environments", None), ("owned_parts", {}),
                             ("next_excluded_context", {}), ("combined", {}), ("full_bytes", True),
                             ("full_sha256", "0" * 64), ("url", "https://example.invalid/mutable")):
            self.assertTrue(check.verify_source(raw, "fr", dict(expected, **{field: value})))
        self.assertTrue(check.verify_source(raw, "unknown", expected))
        self.assertTrue(check.verify_source(raw, "fr", []))

    def test_raw_span_validates_intervals_and_offsets(self):
        lines = [b"a\n", b"b\n"]
        for interval in ((0, 1), (1, 3), (2, 1), (True, 1), (1, False), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span(lines, *interval)
        self.assertEqual(check.raw_span(lines, 2, 2), {
            "lf_line_start": 2, "lf_line_end": 2, "bytes": 2,
            "sha256": hashlib.sha256(b"b\n").hexdigest().upper(),
            "byte_offset_start": 2, "byte_offset_end_exclusive": 4})


class BoundedReplay711516Tests(unittest.TestCase):
    def test_cached_route_reads_once_without_network(self):
        raw, expected = synthetic_source("fr")
        cached = MagicMock(spec=Path)
        handle = cached.open.return_value.__enter__.return_value
        handle.read.return_value = raw
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            self.assertEqual(check.read_source(expected, "fr", cached), raw)
        cached.open.assert_called_once_with("rb")
        handle.read.assert_called_once_with(len(raw) + 1)

    def test_live_route_reads_once_from_pinned_url_with_timeout(self):
        raw, expected = synthetic_source("en")
        response = MagicMock()
        response.__enter__.return_value.read.return_value = raw
        with patch.object(check, "urlopen", return_value=response) as fetch:
            self.assertEqual(check.read_source(expected, "en"), raw)
        fetch.assert_called_once_with(check.SOURCE_URLS["en"], timeout=30)
        response.__enter__.return_value.read.assert_called_once_with(len(raw) + 1)

    def test_bad_bounds_language_or_unpinned_url_fail_before_read(self):
        _, expected = synthetic_source("fr")
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            for count in (0, -1, True, "38226", check.MAX_SOURCE_BYTES + 1):
                with self.assertRaises(ValueError):
                    check.read_source(dict(expected, full_bytes=count), "fr")
            for language, receipt in (("other", expected), ("fr", []),
                                      ("fr", dict(expected, url="https://example.invalid/"))):
                with self.assertRaises(ValueError):
                    check.read_source(receipt, language)

    def test_cli_cached_bilingual_success_and_schema(self):
        fixtures = {language: synthetic_source(language) for language in ("fr", "en")}
        receipt = {"languages": {language: pair[1] for language, pair in fixtures.items()}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=lambda expected, lang, cache: fixtures[lang][0]) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "cached-fr.tex", "--english", "cached-en.tex"]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(read.call_args_list[0].args[2], Path("cached-fr.tex"))
        self.assertEqual(read.call_args_list[1].args[2], Path("cached-en.tex"))
        result = json.loads(output.getvalue())
        self.assertEqual(result["schema"], "ega-i711516-raw-source-boundary-replay/v1")
        self.assertEqual(result["status"], "PASS")

    def test_cli_malformed_language_inventory_or_missing_receipt_never_fetches(self):
        for value in ("{}", "[]", "{", '{"languages":[]}', '{"languages":{"fr":{}}}'):
            with patch.object(Path, "read_text", return_value=value), \
                    patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO):
                self.assertTrue(check.main([]))
                read.assert_not_called()
        with patch.object(Path, "read_text", side_effect=OSError("not found")), \
                patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO):
            self.assertTrue(check.main([]))
            read.assert_not_called()

    def test_cli_read_failures_have_no_retries(self):
        receipt = {"languages": {lang: synthetic_source(lang)[1] for lang in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(len(json.loads(output.getvalue())["errors"]), 2)


if __name__ == "__main__":
    unittest.main()
