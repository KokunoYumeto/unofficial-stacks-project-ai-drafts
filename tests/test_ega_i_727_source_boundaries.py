"""Offline synthetic/rehashed-adversary tests for EGA I 7.2.5--7.2.7."""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i727_source_boundaries as check


def metadata(raw, language):
    return check.source_metadata(raw, language)


def synthetic_source(language):
    """Synthetic clauses at physical LF positions; never a stored source copy."""
    lines = [b"\n"] * (check.NEXT_RANGES[language][1] + 2)
    lines[0] = b"% synthetic fixture, not authority bytes\n"
    suffix = "-fr" if language == "fr" else ""
    for number, env, (start, end), (tokens, final) in zip(
            check.NUMBERS, check.ENVIRONMENTS, check.ENVIRONMENT_RANGES[language],
            check.UNIT_WITNESSES[language]):
        lines[start - 1] = f"\\begin{{{env}}}[{number}]\n".encode()
        lines[start] = f"\\label{{I.{number}{suffix}}}\n".encode()
        lines[end - 2] = (" ".join(tokens) + " " + final).encode() + b"\n"
        lines[end - 1] = f"\\end{{{env}}}\n".encode()
    for index, ((start, end), (initial, tokens, final)) in enumerate(zip(
            check.OWNED_RANGES[language], check.OWNED_WITNESSES[language])):
        first, last = start - 1, end - 1
        if index == 0:
            lines[first] = check.PAGE_MARKER.encode() + b"\n"
            first += 1
        if language == "en":
            lines[first] = b"\\begin{proof}\n"
            lines[last] = b"\\end{proof}\n"
            first += 1
            last -= 1
        if first == last:
            lines[first] = (initial + " " + " ".join(tokens) + " " + final).encode() + b"\n"
        else:
            lines[first] = initial.encode() + b"\n"
            lines[last] = (" ".join(tokens) + " " + final).encode() + b"\n"
    for n, marker in check.NEXT_MARKERS[language]:
        lines[n - 1] = marker.encode() + b"\n"
    end = check.NEXT_RANGES[language][1]
    lines[end] = b"next mathematics is deliberately not adjudicated\n"
    lines[end + 1] = b"\\end{env}\n"
    raw = b"".join(lines)
    return raw, metadata(raw, language)


def replace_in_interval(raw, interval, old, new):
    lines = check.raw_lines(raw)
    start, end = interval
    block = b"".join(lines[start - 1:end])
    assert old in block, (interval, old)
    return b"".join(lines[:start - 1]) + block.replace(old, new) + b"".join(lines[end:])


class SourceBoundary727Tests(unittest.TestCase):
    def test_fixed_ownership_and_default_receipt(self):
        self.assertEqual(check.NUMBERS, ("7.2.5", "7.2.6", "7.2.7"))
        self.assertEqual(check.RANGES, {"fr": ((378, 391), (392, 403), (404, 430)),
                                       "en": ((227, 237), (238, 247), (248, 259))})
        self.assertEqual(check.ENVIRONMENT_RANGES, {
            "fr": ((378, 385), (392, 397), (404, 414)),
            "en": ((227, 231), (238, 242), (248, 252))})
        self.assertEqual(check.OWNED_KEYS, ("ega:I.7.2.5:proof", "ega:I.7.2.6:proof", "ega:I.7.2.7:proof"))
        self.assertEqual(check.OWNED_RANGES, {"fr": ((387, 390), (399, 402), (416, 429)),
                                             "en": ((233, 236), (244, 246), (254, 258))})
        self.assertEqual(check.PAGE_RANGES, {"fr": (387, 387), "en": (233, 233)})
        self.assertEqual(check.NEXT_RANGES, {"fr": (431, 432), "en": (260, 261)})
        self.assertEqual(check.RECEIPT.name, "ega-i-7.2.5-7.2.7-semantic-checkpoint-2026-09-08.json")

    def test_complete_bilingual_synthetic_sources_pass(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            with self.subTest(language=language):
                self.assertEqual(check.verify_source(raw, language, expected), [])
                self.assertEqual(expected["combined"]["bytes"],
                                 sum(span["bytes"] for span in expected["slices"].values()))

    def test_statements_only_cannot_replace_complete_storage_slices(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for number, interval in zip(check.NUMBERS, check.ENVIRONMENT_RANGES[language]):
                altered = copy.deepcopy(expected)
                altered["slices"]["ega:I." + number] = check.raw_span(check.raw_lines(raw), *interval)
                self.assertTrue(any("complete source-order" in e for e in check.verify_source(raw, language, altered)))

    def test_each_proof_interval_cannot_drop_either_endpoint_after_rehash(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for owner, (start, end) in zip(check.OWNED_KEYS, check.OWNED_RANGES[language]):
                for interval in ((start + 1, end), (start, end - 1)):
                    with self.subTest(language=language, owner=owner, interval=interval):
                        altered = copy.deepcopy(expected)
                        altered["owned_parts"][owner] = check.raw_span(check.raw_lines(raw), *interval)
                        self.assertTrue(any(owner + ": complete independently owned" in e
                                            for e in check.verify_source(raw, language, altered)))

    def test_every_statement_hypothesis_and_clause_required_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for number, interval, (tokens, final) in zip(
                    check.NUMBERS, check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]):
                for token in (*tokens, final):
                    with self.subTest(language=language, number=number, token=token):
                        damaged = replace_in_interval(raw, interval, token.encode(), b"statement clause omitted")
                        self.assertTrue(any("ega:I." + number + ": final statement semantic witness" in e
                                            for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_every_proof_clause_and_both_direction_conclusions_required_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for owner, interval, (initial, tokens, final) in zip(
                    check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                for token in (initial, *tokens, final):
                    with self.subTest(language=language, owner=owner, token=token):
                        damaged = replace_in_interval(raw, interval, token.encode(), b"proof clause omitted")
                        self.assertTrue(any(owner + ": " in e and ("witness" in e or "conclusion" in e)
                                            for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_historical_parenthetical_cannot_be_silently_removed_or_corrected(self):
        for language, token in (("fr", "l'application rationnelle de $Y$ dans $X$ prolongeant $g$ soit partout définie"),
                                ("en", "the rational map from $Y$ to $X$ extending $g$ to be defined everywhere")):
            raw, _ = synthetic_source(language)
            damaged = replace_in_interval(raw, check.ENVIRONMENT_RANGES[language][2], token.encode(),
                                          b"a corrected relative section-domain assertion")
            self.assertTrue(any("7.2.7: final statement semantic witness" in e
                                for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_swapped_missing_extra_and_nonobject_inventories_rejected(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            altered = copy.deepcopy(expected)
            a, b = check.OWNED_KEYS[:2]
            altered["owned_parts"][a], altered["owned_parts"][b] = altered["owned_parts"][b], altered["owned_parts"][a]
            self.assertTrue(any("independently owned" in e for e in check.verify_source(raw, language, altered)))
            for key in ("slices", "numbered_environments", "owned_parts", "page_markers"):
                for value in (None, [], {}, dict(expected[key], foreign_owner={})):
                    altered = dict(expected, **{key: value})
                    self.assertTrue(any("semantic owners" in e for e in check.verify_source(raw, language, altered)))
                altered = copy.deepcopy(expected)
                altered[key][next(iter(altered[key]))] = None
                self.assertTrue(check.verify_source(raw, language, altered))

    def test_every_unowned_separator_rejects_substantive_or_wrapped_prose(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            covered = set()
            for start, end in (*check.ENVIRONMENT_RANGES[language], *check.OWNED_RANGES[language]):
                covered.update(range(start, end + 1))
            for n in range(check.RANGES[language][0][0], check.RANGES[language][-1][1] + 1):
                if n in covered:
                    continue
                for body in (b"unowned proof continuation\n", b"\\begin{proof}\n"):
                    with self.subTest(language=language, line=n, body=body):
                        lines = check.raw_lines(raw)
                        lines[n - 1] = body
                        damaged = b"".join(lines)
                        self.assertTrue(any("unowned substantive source line: " + str(n) in e
                                            for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_all_english_proof_wrappers_required_unique_and_not_nested(self):
        raw, _ = synthetic_source("en")
        for interval in check.OWNED_RANGES["en"]:
            for old, new in ((b"\\begin{proof}", b"missing begin"),
                             (b"\\end{proof}", b"missing end"),
                             (b"\\begin{proof}", b"\\begin{proof} \\begin{proof}"),
                             (b"\\end{proof}", b"\\end{proof} \\end{proof}"),
                             (b"\\begin{proof}", b"% \\begin{proof}"),
                             (b"\\end{proof}", b"% \\end{proof}")):
                damaged = replace_in_interval(raw, interval, old, new)
                self.assertTrue(any("English proof wrapper" in e
                                    for e in check.verify_source(damaged, "en", metadata(damaged, "en"))))
            token = check.OWNED_WITNESSES["en"][check.OWNED_RANGES["en"].index(interval)][0].encode()
            damaged = replace_in_interval(raw, interval, token, b"\\begin{proof} " + token)
            self.assertTrue(any("English proof wrapper" in e
                                for e in check.verify_source(damaged, "en", metadata(damaged, "en"))))

    def test_french_proofs_must_remain_unwrapped(self):
        raw, _ = synthetic_source("fr")
        for interval, (initial, _, _) in zip(check.OWNED_RANGES["fr"], check.OWNED_WITNESSES["fr"]):
            damaged = replace_in_interval(raw, interval, initial.encode(), b"\\begin{proof} " + initial.encode())
            self.assertTrue(any("French unwrapped proof" in e
                                for e in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))

    def test_english_proof_wrappers_cannot_shift_within_rehashed_owned_span(self):
        raw, _ = synthetic_source("en")
        start, end = check.OWNED_RANGES["en"][2]
        # Preserve every substantive clause, moving only a delimiter and blank
        # space inside the complete five-line owned interval.
        lines = check.raw_lines(raw)
        body = b" ".join(line.strip() for line in lines[start:end - 1] if line.strip()) + b"\n"
        for replacement in ((b"\n", b"\\begin{proof}\n", body, b"\n", b"\\end{proof}\n"),
                            (b"\\begin{proof}\n", body, b"\n", b"\\end{proof}\n", b"\n")):
            damaged = b"".join(lines[:start - 1]) + b"".join(replacement) + b"".join(lines[end:])
            errors = check.verify_source(damaged, "en", metadata(damaged, "en"))
            self.assertTrue(any("English proof wrapper" in e for e in errors))
            self.assertFalse(any("semantic witness" in e or "semantic conclusion" in e for e in errors))

    def test_page_marker_separate_identity_and_complete_proof_membership(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            page = expected["page_markers"][check.PAGE_KEY]
            proof = expected["owned_parts"][check.OWNED_KEYS[0]]
            self.assertEqual(page["byte_offset_start"], proof["byte_offset_start"])
            altered = copy.deepcopy(expected)
            altered["page_markers"][check.PAGE_KEY] = proof
            self.assertTrue(any("old-page marker identity" in e for e in check.verify_source(raw, language, altered)))
            for new in (b"omitted page", b"% " + check.PAGE_MARKER.encode(), b"\\oldpage[I]{161}"):
                damaged = raw.replace(check.PAGE_MARKER.encode(), new)
                self.assertTrue(any("old-page marker must occur exactly once" in e
                                    for e in check.verify_source(damaged, language, metadata(damaged, language))))
            for duplicate in (check.PAGE_MARKER.encode(), b"inline " + check.PAGE_MARKER.encode()):
                damaged = raw + duplicate + b"\n"
                self.assertTrue(any("old-page marker must occur exactly once" in e
                                    for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_page_marker_cannot_trade_places_with_proof_wrapper_or_prose(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            lines = check.raw_lines(raw)
            page = check.PAGE_RANGES[language][0] - 1
            lines[page], lines[page + 1] = lines[page + 1], lines[page]
            damaged = b"".join(lines)
            self.assertTrue(any("old-page marker must occur exactly once" in e
                                for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_comment_hidden_statement_and_proof_witnesses_do_not_count(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for intervals, witnesses in ((check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]),
                                          (check.OWNED_RANGES[language], check.OWNED_WITNESSES[language])):
                for index, interval in enumerate(intervals):
                    token = (witnesses[index][0][0] if len(witnesses[index]) == 2 else witnesses[index][0]).encode()
                    damaged = replace_in_interval(raw, interval, token, b"% " + token)
                    self.assertTrue(any("semantic witness" in e
                                        for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_comment_escape_parity(self):
        self.assertEqual(check._uncomment(b"x % hidden"), b"x ")
        self.assertEqual(check._uncomment(rb"x \% visible"), rb"x \% visible")
        self.assertEqual(check._uncomment(rb"x \\% hidden"), rb"x \\")
        self.assertEqual(check._uncomment(rb"x \\\% visible"), rb"x \\\% visible")

    def test_missing_duplicate_misnumbered_and_unclosed_statements_fail_without_metadata_regeneration(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            suffix = "-fr" if language == "fr" else ""
            for number in check.NUMBERS:
                begin = f"\\begin{{corollary}}[{number}]".encode()
                label = f"\\label{{I.{number}{suffix}}}".encode()
                for damaged in (raw.replace(label, b"missing label"), raw.replace(begin, b"missing begin"),
                                raw.replace(begin, begin.replace(number.encode(), b"7.2.99")),
                                raw + label + b"\n", raw + b"inline " + label + b"\n",
                                raw + begin + b"\n", raw.replace(b"\\end{corollary}", b"missing close")):
                    self.assertTrue(check.verify_source(damaged, language, expected))

    def test_early_closing_and_nested_numbered_statement_rejected_after_rehash(self):
        raw, _ = synthetic_source("fr")
        lines = check.raw_lines(raw)
        lines[380] = b"\\end{corollary}\n"
        damaged = b"".join(lines)
        self.assertTrue(any("complete numbered environment boundary" in e
                            for e in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))
        token = check.UNIT_WITNESSES["fr"][0][0][0].encode()
        damaged = replace_in_interval(raw, check.ENVIRONMENT_RANGES["fr"][0], token,
                                      b"\\begin{env}[7.2.5.1] " + token)
        self.assertTrue(any("next numbered begin" in e
                            for e in check.verify_source(damaged, "fr", metadata(damaged, "fr"))))

    def test_duplicated_or_prose_suffixed_numbered_closing_markers_rejected_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for interval in check.ENVIRONMENT_RANGES[language]:
                for suffix in (b" \\end{corollary}", b" trailing unowned closing-line prose"):
                    damaged = replace_in_interval(raw, interval, b"\\end{corollary}", b"\\end{corollary}" + suffix)
                    self.assertTrue(any("complete numbered environment boundary" in e
                                        for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_foreign_numbered_begin_with_inline_text_inside_each_proof_is_detected(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for interval, (initial, _, _) in zip(check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                damaged = replace_in_interval(raw, interval, initial.encode(),
                                              initial.encode() + b" \\begin{env}[7.2.5.1] foreign text")
                self.assertTrue(any("next numbered begin" in e
                                    for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_next_begin_and_label_required_unique_including_inline_duplicates(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for n, marker in check.NEXT_MARKERS[language]:
                for damaged in (replace_in_interval(raw, (n, n), marker.encode(), b"missing next marker"),
                                replace_in_interval(raw, (n, n), marker.encode(), b"% " + marker.encode()),
                                raw + marker.encode() + b"\n", raw + b"inline " + marker.encode() + b"\n"):
                    self.assertTrue(any("next excluded 7.2.8 marker" in e
                                        for e in check.verify_source(damaged, language, metadata(damaged, language))))

    def test_excluded_boundary_cannot_drop_label_or_absorb_following_math(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            start, end = check.NEXT_RANGES[language]
            for interval in ((start, start), (start, end + 1)):
                altered = dict(expected, next_excluded_boundary={"source_unit": "ega:I.7.2.8",
                               **check.raw_span(check.raw_lines(raw), *interval)})
                self.assertTrue(any("next excluded 7.2.8 boundary" in e
                                    for e in check.verify_source(raw, language, altered)))
            altered = copy.deepcopy(expected)
            altered["combined"] = check.raw_span(check.raw_lines(raw), check.RANGES[language][0][0], end)
            altered["slices"]["ega:I.7.2.7"] = check.raw_span(check.raw_lines(raw), check.RANGES[language][-1][0], end)
            errors = check.verify_source(raw, language, altered)
            self.assertTrue(any("combined source-order" in e for e in errors))
            self.assertTrue(any("7.2.7: complete source-order" in e for e in errors))

    def test_next_mathematical_content_is_not_adjudicated_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            damaged = raw.replace(b"next mathematics is deliberately not adjudicated", b"different later mathematics")
            self.assertEqual(check.verify_source(damaged, language, metadata(damaged, language)), [])

    def test_lf_only_and_sufficient_next_context_required(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for damaged in (raw.replace(b"\n", b"\r\n"), raw.replace(b"synthetic", b"\rsynthetic"),
                            raw[:-1], b"", "not bytes", None):
                self.assertTrue(check.verify_source(damaged, language, expected))
            damaged = b"".join(check.raw_lines(raw)[:check.NEXT_RANGES[language][1] - 1])
            self.assertTrue(any("following 7.2.8" in e for e in check.verify_source(damaged, language, expected)))
            damaged = raw.replace(b"synthetic", b"synthetic\x0c\xe2\x80\xa8", 1)
            self.assertEqual(check.verify_source(damaged, language, metadata(damaged, language)), [])

    def test_malformed_source_identity_and_language_fail_closed(self):
        raw, expected = synthetic_source("fr")
        for key, value in (("full_bytes", True), ("full_sha256", "0" * 64), ("combined", []),
                           ("next_excluded_boundary", None), ("url", "https://example.invalid/mutable")):
            self.assertTrue(check.verify_source(raw, "fr", dict(expected, **{key: value})))
        for language in ("other", [], None):
            self.assertTrue(check.verify_source(raw, language, expected))
        self.assertTrue(check.verify_source(raw, "fr", []))
        for language in ("other", [], None):
            with self.assertRaises(ValueError):
                metadata(raw, language)

    def test_raw_span_validates_physical_intervals_and_offsets(self):
        lines = [b"a\n", b"b\n"]
        for interval in ((0, 1), (1, 3), (2, 1), (True, 1), (1, False), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span(lines, *interval)
        self.assertEqual(check.raw_span(lines, 2, 2), {
            "lf_line_start": 2, "lf_line_end": 2, "bytes": 2,
            "sha256": hashlib.sha256(b"b\n").hexdigest().upper(),
            "byte_offset_start": 2, "byte_offset_end_exclusive": 4})


class BoundedReplay727Tests(unittest.TestCase):
    def test_cached_route_reads_once_and_never_uses_network(self):
        raw, expected = synthetic_source("fr")
        cached = MagicMock(spec=Path)
        handle = cached.open.return_value.__enter__.return_value
        handle.read.return_value = raw
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            self.assertEqual(check.read_source(expected, "fr", cached), raw)
        cached.open.assert_called_once_with("rb")
        handle.read.assert_called_once_with(len(raw) + 1)

    def test_network_route_uses_one_fixed_url_bounded_read_and_timeout(self):
        raw, expected = synthetic_source("en")
        response = MagicMock()
        response.__enter__.return_value.read.return_value = raw
        with patch.object(check, "urlopen", return_value=response) as fetch:
            self.assertEqual(check.read_source(expected, "en"), raw)
        fetch.assert_called_once_with(check.SOURCE_URLS["en"], timeout=30)
        response.__enter__.return_value.read.assert_called_once_with(len(raw) + 1)

    def test_bad_bounds_languages_and_urls_fail_before_cache_or_network(self):
        _, expected = synthetic_source("fr")
        cached = MagicMock(spec=Path)
        bad = [("fr", dict(expected, full_bytes=size)) for size in (0, -1, True, "38226", check.MAX_SOURCE_BYTES + 1)]
        bad += [("other", expected), ([], expected), (None, expected), ("fr", []),
                ("fr", dict(expected, url="https://example.invalid/"))]
        with patch.object(check, "urlopen") as fetch:
            for language, value in bad:
                for cache in (None, cached):
                    with self.assertRaises(ValueError):
                        check.read_source(value, language, cache)
            fetch.assert_not_called()
            cached.open.assert_not_called()

    def test_network_failures_have_no_retries(self):
        _, expected = synthetic_source("en")
        with patch.object(check, "urlopen", side_effect=OSError("one bounded failure")) as fetch:
            with self.assertRaises(OSError):
                check.read_source(expected, "en")
        fetch.assert_called_once()

    def test_short_and_oversized_responses_fail_verification_without_retry(self):
        raw, expected = synthetic_source("en")
        for returned in (raw[:100], raw + b"\n"):
            response = MagicMock()
            response.__enter__.return_value.read.return_value = returned
            with patch.object(check, "urlopen", return_value=response) as fetch:
                replayed = check.read_source(expected, "en")
                self.assertTrue(check.verify_source(replayed, "en", expected))
            fetch.assert_called_once()

    def test_cli_bilingual_cached_success_and_schema(self):
        fixtures = {language: synthetic_source(language) for language in ("fr", "en")}
        receipt = {"languages": {language: pair[1] for language, pair in fixtures.items()}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=lambda expected, language, cached: fixtures[language][0]) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "cached-fr.tex", "--english", "cached-en.tex"]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(read.call_args_list[0].args[2], Path("cached-fr.tex"))
        self.assertEqual(read.call_args_list[1].args[2], Path("cached-en.tex"))
        result = json.loads(output.getvalue())
        self.assertEqual(result["schema"], "ega-i727-raw-source-boundary-replay/v1")
        self.assertEqual(result["status"], "PASS")

    def test_cli_missing_receipt_and_malformed_language_inventories_never_fetch(self):
        fixtures = {language: synthetic_source(language)[1] for language in ("fr", "en")}
        invalid = ["{}", "[]", "{", '{"languages":[]}', '{"languages":{"fr":{}}}']
        for language in ("fr", "en"):
            for value in (None, [], {}):
                invalid.append(json.dumps({"languages": dict(fixtures, **{language: value})}))
            for field, value in (("owned_parts", []), ("slices", {}), ("page_markers", {}),
                                  ("numbered_environments", {}), ("full_bytes", True),
                                  ("full_sha256", "invalid"), ("combined", None),
                                  ("next_excluded_boundary", []), ("url", "https://example.invalid")):
                invalid.append(json.dumps({"languages": dict(fixtures, **{language: dict(fixtures[language], **{field: value})})}))
        invalid.append(json.dumps({"languages": dict(fixtures, other={})}))
        for value in invalid:
            with patch.object(Path, "read_text", return_value=value), patch.object(check, "read_source") as read, \
                    patch("sys.stdout", new_callable=io.StringIO):
                self.assertTrue(check.main([]))
                read.assert_not_called()
        with patch.object(Path, "read_text", side_effect=FileNotFoundError("not found")), \
                patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            read.assert_not_called()
        self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")

    def test_cli_each_language_read_failure_is_reported_once_without_retry(self):
        receipt = {"languages": {language: synthetic_source(language)[1] for language in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(len(json.loads(output.getvalue())["errors"]), 2)

    def test_cli_malformed_nested_span_entries_never_fetch_either_language(self):
        receipt = {"languages": {language: synthetic_source(language)[1] for language in ("fr", "en")}}
        for language in ("fr", "en"):
            for inventory in ("slices", "owned_parts", "numbered_environments", "page_markers"):
                for bad in (None, [], {}, {"bytes": True}):
                    altered = copy.deepcopy(receipt)
                    owner = next(iter(altered["languages"][language][inventory]))
                    altered["languages"][language][inventory][owner] = bad
                    with patch.object(Path, "read_text", return_value=json.dumps(altered)), \
                            patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO):
                        self.assertTrue(check.main([]))
                        read.assert_not_called()
            for field in ("bytes", "lf_line_start", "byte_offset_start", "sha256"):
                altered = copy.deepcopy(receipt)
                altered["languages"][language]["combined"][field] = True
                with patch.object(Path, "read_text", return_value=json.dumps(altered)), \
                        patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO):
                    self.assertTrue(check.main([]))
                    read.assert_not_called()


if __name__ == "__main__":
    unittest.main()
