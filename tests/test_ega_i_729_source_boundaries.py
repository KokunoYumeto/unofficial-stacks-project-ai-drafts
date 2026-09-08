"""Offline ownership/adversarial-rehash tests for EGA I 7.2.8--7.2.9.

Fixtures are synthetic, not stored historical source. Passing these tests proves
source-checker behavior, not a mathematical theorem or semantic admission.
"""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i729_source_boundaries as check


def metadata(raw, language):
    return check.source_metadata(raw, language)


def synthetic_source(language):
    """Keep independent physical positions; obtain only clauses from the API."""
    env_ranges = {
        "fr": ((431, 451), (453, 464), (487, 496)),
        "en": ((260, 269), (271, 276), (289, 295)),
    }
    owned_ranges = {
        "fr": ((466, 478), (480, 485), (498, 526)),
        "en": ((278, 284), (286, 287), (297, 308)),
    }
    enum_range = {"fr": (442, 450), "en": (265, 268)}[language]
    page = {"fr": 474, "en": 282}[language]
    next_end = {"fr": 529, "en": 311}[language]
    lines = [b"\n"] * (next_end + 2)
    lines[0] = b"% synthetic fixture, never authority bytes\n"
    suffix = "-fr" if language == "fr" else ""
    numbers = ("7.2.8", "7.2.8.1", "7.2.9")
    envs = ("env", "lemma", "proposition")
    for index, (number, env, (start, end), (tokens, final)) in enumerate(zip(
            numbers, envs, env_ranges[language], check.UNIT_WITNESSES[language])):
        lines[start - 1] = f"\\begin{{{env}}}[{number}]\n".encode()
        lines[start] = f"\\label{{I.{number}{suffix}}}\n".encode()
        if index == 0:
            enum_start, enum_end = enum_range
            lines[enum_start - 1] = b"\\begin{enumerate}\n"
            first_item = r"\item[1\textsuperscript{o}]" if language == "fr" else r"\item[1st.]"
            second_item = r"\item[2\textsuperscript{o}]" if language == "fr" else r"\item[2nd.]"
            item_lines = (443, 448) if language == "fr" else (266, 267)
            lines[item_lines[0] - 1] = (first_item + " " + " ".join(tokens)).encode() + b"\n"
            lines[item_lines[1] - 1] = (second_item + " " + final).encode() + b"\n"
            lines[enum_end - 1] = b"\\end{enumerate}\n"
        else:
            lines[end - 2] = (" ".join(tokens) + " " + final).encode() + b"\n"
        lines[end - 1] = f"\\end{{{env}}}\n".encode()
    for index, ((start, end), (initial, tokens, final)) in enumerate(zip(
            owned_ranges[language], check.OWNED_WITNESSES[language])):
        first, last = start - 1, end - 1
        if language == "en" and index in (0, 2):
            lines[first] = b"\\begin{proof}\n"
            lines[last] = b"\\end{proof}\n"
            first += 1
            last -= 1
        if first == last:
            lines[first] = (initial + " " + " ".join(tokens) + " " + final).encode() + b"\n"
        else:
            lines[first] = initial.encode() + b"\n"
            lines[last] = (" ".join(tokens) + " " + final).encode() + b"\n"
    lines[page - 1] = rb"\oldpage[I]{161}" + b"\n"
    for n, marker in check.NEXT_MARKERS[language]:
        lines[n - 1] = marker.encode() + b"\n"
    lines[next_end] = b"later mathematics is deliberately outside this review\n"
    lines[next_end + 1] = b"\\end{env}\n"
    raw = b"".join(lines)
    return raw, metadata(raw, language)


def replace_in_interval(raw, interval, old, new):
    lines = check.raw_lines(raw)
    start, end = interval
    block = b"".join(lines[start - 1:end])
    assert old in block, (interval, old)
    return b"".join(lines[:start - 1]) + block.replace(old, new) + b"".join(lines[end:])


def rehashed_errors(raw, language):
    return check.verify_source(raw, language, metadata(raw, language))


class SourceBoundary729Tests(unittest.TestCase):
    def test_fixed_source_ownership_and_default_receipt(self):
        self.assertEqual(check.NUMBERS, ("7.2.8", "7.2.8.1", "7.2.9"))
        self.assertEqual(check.ENVIRONMENTS, ("env", "lemma", "proposition"))
        self.assertEqual(check.RANGES, {
            "fr": ((431, 486), (453, 479), (487, 527)),
            "en": ((260, 288), (271, 285), (289, 309))})
        self.assertEqual(check.ENVIRONMENT_RANGES, {
            "fr": ((431, 451), (453, 464), (487, 496)),
            "en": ((260, 269), (271, 276), (289, 295))})
        self.assertEqual(check.OWNED_KEYS, (
            "ega:I.7.2.8.1:proof", "ega:I.7.2.8:induced-map", "ega:I.7.2.9:proof"))
        self.assertEqual(check.OWNED_RANGES, {
            "fr": ((466, 478), (480, 485), (498, 526)),
            "en": ((278, 284), (286, 287), (297, 308))})
        self.assertEqual(check.PROOF_INDICES, (0, 2))
        self.assertEqual(check.PAGE_KEY, "ega:I.7.2.8.1:page-marker")
        self.assertEqual(check.PAGE_RANGES, {"fr": (474, 474), "en": (282, 282)})
        self.assertEqual(check.PAGE_MARKER, r"\oldpage[I]{161}")
        self.assertEqual(check.ENUM_RANGES, {"fr": (442, 450), "en": (265, 268)})
        self.assertEqual(check.NEXT_RANGES, {"fr": (528, 529), "en": (310, 311)})
        self.assertEqual(check.NEXT_NUMBER, "7.3")
        self.assertEqual(check.RECEIPT.name, "ega-i-7.2.8-7.2.9-semantic-checkpoint-2026-09-08.json")

    def test_bilingual_complete_fixtures_and_deliberate_parent_child_overlap(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            with self.subTest(language=language):
                self.assertEqual(check.verify_source(raw, language, expected), [])
                spans = expected["slices"]
                self.assertEqual(expected["combined"]["bytes"],
                                 spans["ega:I.7.2.8"]["bytes"] + spans["ega:I.7.2.9"]["bytes"])
                self.assertGreater(spans["ega:I.7.2.8"]["bytes"], spans["ega:I.7.2.8.1"]["bytes"])
                self.assertGreater(spans["ega:I.7.2.8.1"]["byte_offset_start"],
                                   spans["ega:I.7.2.8"]["byte_offset_start"])
                self.assertLess(spans["ega:I.7.2.8.1"]["byte_offset_end_exclusive"],
                                spans["ega:I.7.2.8"]["byte_offset_end_exclusive"])

    def test_statement_environment_is_not_a_complete_storage_unit(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for number, interval in zip(check.NUMBERS, check.ENVIRONMENT_RANGES[language]):
                altered = copy.deepcopy(expected)
                altered["slices"]["ega:I." + number] = check.raw_span(check.raw_lines(raw), *interval)
                self.assertTrue(any("complete source-order" in e
                                    for e in check.verify_source(raw, language, altered)))

    def test_parent_slice_must_include_nested_proof_and_induced_map(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            start, _ = check.RANGES[language][0]
            for end in (check.ENVIRONMENT_RANGES[language][0][1],
                        check.RANGES[language][1][1], check.OWNED_RANGES[language][1][1] - 1):
                altered = copy.deepcopy(expected)
                altered["slices"]["ega:I.7.2.8"] = check.raw_span(check.raw_lines(raw), start, end)
                self.assertTrue(any("ega:I.7.2.8: complete source-order" in e
                                    for e in check.verify_source(raw, language, altered)))

    def test_each_owned_proof_or_parent_part_cannot_drop_either_endpoint(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for owner, (start, end) in zip(check.OWNED_KEYS, check.OWNED_RANGES[language]):
                for interval in ((start + 1, end), (start, end - 1)):
                    altered = copy.deepcopy(expected)
                    altered["owned_parts"][owner] = check.raw_span(check.raw_lines(raw), *interval)
                    with self.subTest(language=language, owner=owner, interval=interval):
                        self.assertTrue(any(owner in e and "owned" in e
                                            for e in check.verify_source(raw, language, altered)))

    def test_parent_induced_map_cannot_be_absorbed_into_nested_proof(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            altered = copy.deepcopy(expected)
            start = check.OWNED_RANGES[language][0][0]
            end = check.OWNED_RANGES[language][1][1]
            altered["owned_parts"][check.OWNED_KEYS[0]] = check.raw_span(check.raw_lines(raw), start, end)
            del altered["owned_parts"][check.OWNED_KEYS[1]]
            self.assertTrue(check.verify_source(raw, language, altered))

    def test_every_hypothesis_and_statement_clause_survives_adversarial_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for number, interval, (tokens, final) in zip(
                    check.NUMBERS, check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]):
                for token in (*tokens, final):
                    damaged = replace_in_interval(raw, interval, token.encode(), b"omitted clause")
                    with self.subTest(language=language, number=number, token=token):
                        self.assertTrue(any("ega:I." + number in e and "witness" in e
                                            for e in rehashed_errors(damaged, language)))

    def test_every_proof_and_parent_construction_clause_required_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for owner, interval, (initial, tokens, final) in zip(
                    check.OWNED_KEYS, check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                for token in (initial, *tokens, final):
                    damaged = replace_in_interval(raw, interval, token.encode(), b"omitted proof clause")
                    with self.subTest(language=language, owner=owner, token=token):
                        self.assertTrue(any(owner in e and ("witness" in e or "conclusion" in e)
                                            for e in rehashed_errors(damaged, language)))

    def assert_independent_clause_required(self, language, interval, owner, clause, negation):
        """Use independently spelled contracts, not the checker's witness list."""
        raw, _ = synthetic_source(language)
        for replacement in ("omitted independent clause", negation):
            damaged = replace_in_interval(raw, interval, clause.encode(), replacement.encode())
            errors = rehashed_errors(damaged, language)
            with self.subTest(language=language, owner=owner, replacement=replacement):
                self.assertTrue(any(owner in error and "witness" in error for error in errors))
                self.assertFalse(any("identity mismatch" in error for error in errors))

    def test_nested_lemma_density_criterion_is_independently_required_after_rehash(self):
        clauses = {
            "fr": (r"$U\cap\operatorname{Spec}(\mathscr{O}_x)$ soit dense dans $\operatorname{Spec}(\mathscr{O}_x)$",
                   r"$U\cap\operatorname{Spec}(\mathscr{O}_x)$ ne soit pas dense dans $\operatorname{Spec}(\mathscr{O}_x)$"),
            "en": (r"$U\cap\Spec(\sh{O}_x)$ is dense in $\Spec(\sh{O}_x)$",
                   r"$U\cap\Spec(\sh{O}_x)$ is not dense in $\Spec(\sh{O}_x)$"),
        }
        for language, (clause, negation) in clauses.items():
            self.assert_independent_clause_required(language, check.ENVIRONMENT_RANGES[language][1],
                                                    "ega:I.7.2.8.1", clause, negation)

    def test_nested_proof_minimal_prime_correspondence_is_independently_required_after_rehash(self):
        clauses = {
            "fr": (r"les idéaux premiers minimaux de $A_x$ correspondent aux idéaux premiers minimaux de $A$ contenus dans $\mathfrak{j}_x$",
                   r"les idéaux premiers minimaux de $A_x$ ne correspondent pas aux idéaux premiers minimaux de $A$ contenus dans $\mathfrak{j}_x$"),
            "en": (r"the minimal prime ideals of $A_x$ correspond to the minimal prime ideals of $A$ that are contained in $\mathfrak{j}_x$",
                   r"the minimal prime ideals of $A_x$ do not correspond to the minimal prime ideals of $A$ that are contained in $\mathfrak{j}_x$"),
        }
        for language, (clause, negation) in clauses.items():
            self.assert_independent_clause_required(language, check.OWNED_RANGES[language][0],
                                                    "ega:I.7.2.8.1:proof", clause, negation)

    def test_irreducible_branch_rational_map_identity_is_independently_required_after_rehash(self):
        clauses = {
            "fr": ("$f$ et $g$ sont des $S$-applications rationnelles, elles sont identiques",
                   "$f$ et $g$ sont des $S$-applications rationnelles, elles ne sont pas identiques"),
            "en": ("$f$ and $g$ are rational $S$-maps, they are identical",
                   "$f$ and $g$ are rational $S$-maps, they are not identical"),
        }
        for language, (clause, negation) in clauses.items():
            self.assert_independent_clause_required(language, check.OWNED_RANGES[language][2],
                                                    "ega:I.7.2.9:proof", clause, negation)

    def test_irreducible_branch_defined_at_x_is_independently_required_after_rehash(self):
        clauses = {
            "fr": ("donc $f$ est définie en $x$.", "donc $f$ n'est pas définie en $x$."),
            "en": ("and so $f$ is defined at $x$.", "and so $f$ is not defined at $x$."),
        }
        for language, (clause, negation) in clauses.items():
            self.assert_independent_clause_required(language, check.OWNED_RANGES[language][2],
                                                    "ega:I.7.2.9:proof", clause, negation)

    def test_final_extension_of_glued_map_is_independently_required_after_rehash(self):
        clauses = {
            "fr": ("$f$ est une extension de $f_1$", "$f$ n'est pas une extension de $f_1$"),
            "en": ("$f$ is an extension of $f_1$", "$f$ is not an extension of $f_1$"),
        }
        for language, (clause, negation) in clauses.items():
            self.assert_independent_clause_required(language, check.OWNED_RANGES[language][2],
                                                    "ega:I.7.2.9:proof", clause, negation)

    def test_comment_hidden_hypotheses_and_owned_clauses_do_not_count(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            groups = ((check.ENVIRONMENT_RANGES[language], check.UNIT_WITNESSES[language]),
                      (check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]))
            for intervals, witnesses in groups:
                for interval, witness in zip(intervals, witnesses):
                    token = witness[0][0] if len(witness) == 2 else witness[0]
                    damaged = replace_in_interval(raw, interval, token.encode(), b"% " + token.encode())
                    self.assertTrue(any("witness" in e for e in rehashed_errors(damaged, language)))

    def test_error_messages_do_not_claim_semantic_adjudication(self):
        raw, _ = synthetic_source("en")
        token = check.UNIT_WITNESSES["en"][2][0][0].encode()
        damaged = replace_in_interval(raw, check.ENVIRONMENT_RANGES["en"][2], token, b"omitted")
        errors = rehashed_errors(damaged, "en")
        self.assertTrue(errors)
        self.assertFalse(any("semantic witness" in e or "semantic conclusion" in e for e in errors))

    def test_historical_cross_reference_discrepancy_cannot_be_silently_corrected(self):
        for language, old, new in (
                ("fr", rb"\hyperref[0.1.2.6-fr]{0, 1.2.6}", rb"\hyperref[0.2.1.6-fr]{0, 2.1.6}"),
                ("en", rb"\sref{0.2.1.6}", rb"\sref{0.1.2.6}")):
            raw, _ = synthetic_source(language)
            damaged = replace_in_interval(raw, check.OWNED_RANGES[language][0], old, new)
            self.assertTrue(any(check.OWNED_KEYS[0] in e and "witness" in e
                                for e in rehashed_errors(damaged, language)))

    def test_source_finite_type_cannot_be_replaced_by_proved_stronger_hypothesis(self):
        for language, old, new in (
                ("fr", "$Y$ un $S$-schéma de type fini", "$Y$ un $S$-schéma localement de type fini"),
                ("en", "$Y$ an $S$-scheme of finite type", "$Y$ an $S$-scheme locally of finite type")):
            raw, _ = synthetic_source(language)
            damaged = replace_in_interval(raw, check.ENVIRONMENT_RANGES[language][2], old.encode(), new.encode())
            self.assertTrue(any("ega:I.7.2.9" in e and "witness" in e
                                for e in rehashed_errors(damaged, language)))

    def test_literal_local_morphism_wording_is_preserved_without_endorsing_it(self):
        for language, old, new in (("fr", b"soit un morphisme.", b"soit un $S$-morphisme."),
                                   ("en", b"to be a morphism.", b"to be an $S$-morphism.")):
            raw, _ = synthetic_source(language)
            damaged = replace_in_interval(raw, check.ENVIRONMENT_RANGES[language][2], old, new)
            self.assertTrue(any("ega:I.7.2.9" in e and "witness" in e
                                for e in rehashed_errors(damaged, language)))

    def test_topological_noetherian_hypothesis_cannot_be_strengthened_in_source(self):
        for language, old, new in (
                ("fr", "un préschéma dont l'espace sous-jacent est localement noethérien", "un préschéma localement noethérien"),
                ("en", "whose underlying space is locally Noetherian", "that is locally Noetherian")):
            raw, _ = synthetic_source(language)
            damaged = replace_in_interval(raw, check.ENVIRONMENT_RANGES[language][1], old.encode(), new.encode())
            self.assertTrue(any("ega:I.7.2.8.1" in e and "witness" in e
                                for e in rehashed_errors(damaged, language)))

    def test_every_unowned_separator_rejects_new_substantive_text(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            covered = set()
            for start, end in (*check.ENVIRONMENT_RANGES[language], *check.OWNED_RANGES[language]):
                covered.update(range(start, end + 1))
            for n in range(check.RANGES[language][0][0], check.RANGES[language][-1][1] + 1):
                if n in covered:
                    continue
                for body in (b"unowned continuation\n", b"\\begin{proof}\n"):
                    lines = check.raw_lines(raw)
                    lines[n - 1] = body
                    with self.subTest(language=language, line=n):
                        self.assertTrue(any("unowned substantive source line: " + str(n) in e
                                            for e in rehashed_errors(b"".join(lines), language)))

    def test_swapped_missing_extra_and_nonobject_owner_inventories_fail(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            altered = copy.deepcopy(expected)
            a, b = check.OWNED_KEYS[:2]
            altered["owned_parts"][a], altered["owned_parts"][b] = altered["owned_parts"][b], altered["owned_parts"][a]
            self.assertTrue(check.verify_source(raw, language, altered))
            for key in ("slices", "numbered_environments", "owned_parts", "page_markers"):
                for value in (None, [], {}, dict(expected[key], foreign_owner={})):
                    self.assertTrue(check.verify_source(raw, language, dict(expected, **{key: value})))
                altered = copy.deepcopy(expected)
                altered[key][next(iter(altered[key]))] = None
                self.assertTrue(check.verify_source(raw, language, altered))

    def test_english_proof_wrappers_required_exact_unique_and_uncommented(self):
        raw, _ = synthetic_source("en")
        for index in (0, 2):
            interval = check.OWNED_RANGES["en"][index]
            for marker in (b"\\begin{proof}", b"\\end{proof}"):
                for replacement in (b"missing wrapper", b"% " + marker, marker + b" " + marker):
                    damaged = replace_in_interval(raw, interval, marker, replacement)
                    self.assertTrue(any("English proof wrapper" in e for e in rehashed_errors(damaged, "en")))

    def test_english_proof_wrappers_cannot_slide_inside_owned_interval(self):
        raw, _ = synthetic_source("en")
        for index in (0, 2):
            start, end = check.OWNED_RANGES["en"][index]
            fixture_lines = check.raw_lines(raw)
            blank_lines = [n for n in range(start, end - 1) if fixture_lines[n] == b"\n"]
            self.assertTrue(blank_lines)
            for marker_line, empty_line in ((start - 1, blank_lines[0]), (end - 1, blank_lines[-1])):
                lines = check.raw_lines(raw)
                # Move only the delimiter to a blank line; preserve all clauses.
                self.assertEqual(lines[empty_line], b"\n")
                lines[marker_line], lines[empty_line] = lines[empty_line], lines[marker_line]
                errors = rehashed_errors(b"".join(lines), "en")
                self.assertTrue(any("English proof wrapper" in e for e in errors))

    def test_parent_construction_is_not_an_english_proof_environment(self):
        raw, _ = synthetic_source("en")
        interval = check.OWNED_RANGES["en"][1]
        initial = check.OWNED_WITNESSES["en"][1][0].encode()
        for marker in (b"\\begin{proof} ", b"\\end{proof} "):
            damaged = replace_in_interval(raw, interval, initial, marker + initial)
            self.assertTrue(any(check.OWNED_KEYS[1] in e for e in rehashed_errors(damaged, "en")))

    def test_all_french_owned_parts_remain_unwrapped(self):
        raw, _ = synthetic_source("fr")
        for interval, (initial, _, _) in zip(check.OWNED_RANGES["fr"], check.OWNED_WITNESSES["fr"]):
            for marker in (b"\\begin{proof} ", b"\\end{proof} "):
                damaged = replace_in_interval(raw, interval, initial.encode(), marker + initial.encode())
                self.assertTrue(rehashed_errors(damaged, "fr"))

    def test_page_marker_is_inside_nested_proof_but_not_at_its_start(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            page = expected["page_markers"][check.PAGE_KEY]
            proof = expected["owned_parts"][check.OWNED_KEYS[0]]
            self.assertGreater(page["byte_offset_start"], proof["byte_offset_start"])
            self.assertLess(page["byte_offset_end_exclusive"], proof["byte_offset_end_exclusive"])
            altered = copy.deepcopy(expected)
            altered["page_markers"][check.PAGE_KEY] = proof
            self.assertTrue(check.verify_source(raw, language, altered))
            for replacement in (b"omitted page", b"% " + check.PAGE_MARKER.encode(), rb"\oldpage[I]{160}"):
                damaged = raw.replace(check.PAGE_MARKER.encode(), replacement)
                self.assertTrue(any("old-page marker" in e for e in rehashed_errors(damaged, language)))
            for extra in (check.PAGE_MARKER.encode(), b"inline " + check.PAGE_MARKER.encode()):
                self.assertTrue(any("old-page marker" in e
                                    for e in rehashed_errors(raw + extra + b"\n", language)))

    def test_page_marker_cannot_move_within_rehashed_proof(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            lines = check.raw_lines(raw)
            page = check.PAGE_RANGES[language][0] - 1
            lines[page], lines[page - 1] = lines[page - 1], lines[page]
            self.assertTrue(any("old-page marker" in e for e in rehashed_errors(b"".join(lines), language)))

    def test_introduction_enumeration_is_unique_exact_and_not_comment_hidden(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            interval = check.ENUM_RANGES[language]
            for marker in (b"\\begin{enumerate}", b"\\end{enumerate}"):
                for replacement in (b"missing enumeration", b"% " + marker, marker + b" " + marker):
                    damaged = replace_in_interval(raw, interval, marker, replacement)
                    self.assertTrue(rehashed_errors(damaged, language))
            for marker in (b"\\begin{enumerate}", b"\\end{enumerate}"):
                token = check.OWNED_WITNESSES[language][1][0].encode()
                damaged = replace_in_interval(raw, check.OWNED_RANGES[language][1], token, marker + b" " + token)
                self.assertTrue(rehashed_errors(damaged, language))

    def test_enumeration_cannot_shift_within_numbered_introduction(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            start, end = check.ENUM_RANGES[language]
            for marker_line, destination in ((start - 1, start - 2), (end - 1, start - 2)):
                lines = check.raw_lines(raw)
                self.assertEqual(lines[destination], b"\n")
                lines[marker_line], lines[destination] = lines[destination], lines[marker_line]
                self.assertTrue(rehashed_errors(b"".join(lines), language))

    def test_missing_duplicate_misnumbered_and_unclosed_environments_fail(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            suffix = "-fr" if language == "fr" else ""
            for number, env in zip(check.NUMBERS, check.ENVIRONMENTS):
                begin = f"\\begin{{{env}}}[{number}]".encode()
                label = f"\\label{{I.{number}{suffix}}}".encode()
                close = f"\\end{{{env}}}".encode()
                for damaged in (raw.replace(label, b"missing label"), raw.replace(begin, b"missing begin"),
                                raw.replace(begin, begin.replace(number.encode(), b"7.2.99")),
                                raw + label + b"\n", raw + b"inline " + label + b"\n",
                                raw + begin + b"\n", raw.replace(close, b"missing close")):
                    self.assertTrue(check.verify_source(damaged, language, expected))

    def test_environment_early_close_extra_close_and_trailing_prose_after_rehash(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for env, interval in zip(check.ENVIRONMENTS, check.ENVIRONMENT_RANGES[language]):
                close = f"\\end{{{env}}}".encode()
                for replacement in (close + b" " + close, close + b" unowned trailing prose"):
                    damaged = replace_in_interval(raw, interval, close, replacement)
                    self.assertTrue(rehashed_errors(damaged, language))
                lines = check.raw_lines(raw)
                lines[interval[0] + 1] = close + b"\n"
                self.assertTrue(rehashed_errors(b"".join(lines), language))

    def test_foreign_inline_numbered_begin_cannot_hide_in_any_owned_part(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for interval, (initial, _, _) in zip(check.OWNED_RANGES[language], check.OWNED_WITNESSES[language]):
                damaged = replace_in_interval(raw, interval, initial.encode(),
                                              initial.encode() + b" \\begin{env}[7.2.8.99] foreign text")
                self.assertTrue(any("numbered source order" in e for e in rehashed_errors(damaged, language)))

    def test_next_subsection_heading_and_label_are_exact_unique_boundary_only(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            for n, marker in check.NEXT_MARKERS[language]:
                for damaged in (replace_in_interval(raw, (n, n), marker.encode(), b"missing marker"),
                                replace_in_interval(raw, (n, n), marker.encode(), b"% " + marker.encode()),
                                raw + marker.encode() + b"\n", raw + b"inline " + marker.encode() + b"\n"):
                    self.assertTrue(any("next excluded 7.3 marker" in e for e in rehashed_errors(damaged, language)))

    def test_next_boundary_cannot_lose_label_or_absorb_future_mathematics(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            start, end = check.NEXT_RANGES[language]
            for interval in ((start, start), (start, end + 1)):
                altered = dict(expected, next_excluded_boundary={"source_unit": "ega:I.7.3",
                               **check.raw_span(check.raw_lines(raw), *interval)})
                self.assertTrue(any("next excluded 7.3 boundary" in e
                                    for e in check.verify_source(raw, language, altered)))
            altered = copy.deepcopy(expected)
            altered["combined"] = check.raw_span(check.raw_lines(raw), check.RANGES[language][0][0], end)
            altered["slices"]["ega:I.7.2.9"] = check.raw_span(check.raw_lines(raw), check.RANGES[language][-1][0], end)
            self.assertTrue(check.verify_source(raw, language, altered))

    def test_later_mathematics_is_not_adjudicated_by_rehash_checker(self):
        for language in ("fr", "en"):
            raw, _ = synthetic_source(language)
            damaged = raw.replace(b"later mathematics is deliberately outside this review", b"changed later mathematics")
            self.assertEqual(rehashed_errors(damaged, language), [])

    def test_physical_lf_and_minimum_context_fail_closed(self):
        for language in ("fr", "en"):
            raw, expected = synthetic_source(language)
            for damaged in (raw.replace(b"\n", b"\r\n"), raw.replace(b"synthetic", b"\rsynthetic"),
                            raw[:-1], b"", "not bytes", None):
                self.assertTrue(check.verify_source(damaged, language, expected))
            truncated = b"".join(check.raw_lines(raw)[:check.NEXT_RANGES[language][1] - 1])
            self.assertTrue(check.verify_source(truncated, language, expected))
            # Only LF separates physical lines; form feed and Unicode separators do not.
            damaged = raw.replace(b"synthetic", b"synthetic\x0c\xe2\x80\xa8", 1)
            self.assertEqual(rehashed_errors(damaged, language), [])

    def test_malformed_source_identity_and_language_fail_closed(self):
        raw, expected = synthetic_source("fr")
        for key, value in (("full_bytes", True), ("full_sha256", "0" * 64), ("combined", []),
                           ("next_excluded_boundary", None), ("url", "https://example.invalid/mutable")):
            self.assertTrue(check.verify_source(raw, "fr", dict(expected, **{key: value})))
        for language in ("other", [], None):
            self.assertTrue(check.verify_source(raw, language, expected))
            with self.assertRaises(ValueError):
                metadata(raw, language)
        self.assertTrue(check.verify_source(raw, "fr", []))

    def test_raw_span_strict_types_intervals_and_offsets(self):
        lines = [b"a\n", b"b\n"]
        for interval in ((0, 1), (1, 3), (2, 1), (True, 1), (1, False), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span(lines, *interval)
        self.assertEqual(check.raw_span(lines, 2, 2), {
            "lf_line_start": 2, "lf_line_end": 2, "bytes": 2,
            "sha256": hashlib.sha256(b"b\n").hexdigest().upper(),
            "byte_offset_start": 2, "byte_offset_end_exclusive": 4})

    def test_comment_escape_parity(self):
        self.assertEqual(check._uncomment(b"x % hidden"), b"x ")
        self.assertEqual(check._uncomment(rb"x \% visible"), rb"x \% visible")
        self.assertEqual(check._uncomment(rb"x \\% hidden"), rb"x \\")
        self.assertEqual(check._uncomment(rb"x \\\% visible"), rb"x \\\% visible")


class BoundedReplay729Tests(unittest.TestCase):
    def test_cached_route_reads_once_and_never_uses_network(self):
        raw, expected = synthetic_source("fr")
        cached = MagicMock(spec=Path)
        handle = cached.open.return_value.__enter__.return_value
        handle.read.return_value = raw
        with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
            self.assertEqual(check.read_source(expected, "fr", cached), raw)
        cached.open.assert_called_once_with("rb")
        handle.read.assert_called_once_with(len(raw) + 1)

    def test_network_route_is_pinned_bounded_timed_and_single_attempt(self):
        raw, expected = synthetic_source("en")
        response = MagicMock()
        response.__enter__.return_value.read.return_value = raw
        with patch.object(check, "urlopen", return_value=response) as fetch:
            self.assertEqual(check.read_source(expected, "en"), raw)
        fetch.assert_called_once_with(check.SOURCE_URLS["en"], timeout=30)
        response.__enter__.return_value.read.assert_called_once_with(len(raw) + 1)

    def test_invalid_language_url_or_size_fails_before_any_source_io(self):
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

    def test_network_failure_does_not_retry(self):
        _, expected = synthetic_source("en")
        with patch.object(check, "urlopen", side_effect=OSError("bounded failure")) as fetch:
            with self.assertRaises(OSError):
                check.read_source(expected, "en")
        fetch.assert_called_once()

    def test_short_or_oversized_response_fails_without_retry(self):
        raw, expected = synthetic_source("en")
        for returned in (raw[:100], raw + b"\n"):
            response = MagicMock()
            response.__enter__.return_value.read.return_value = returned
            with patch.object(check, "urlopen", return_value=response) as fetch:
                self.assertTrue(check.verify_source(check.read_source(expected, "en"), "en", expected))
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
        self.assertEqual(result["schema"], "ega-i729-raw-source-boundary-replay/v1")
        self.assertEqual(result["status"], "PASS")

    def test_cli_malformed_language_or_span_inventory_fails_before_either_read(self):
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

    def test_cli_missing_future_default_receipt_is_structured_failure_before_io(self):
        with patch.object(Path, "read_text", side_effect=FileNotFoundError("not found")), \
                patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            read.assert_not_called()
        self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")

    def test_cli_reports_each_read_failure_once(self):
        receipt = {"languages": {language: synthetic_source(language)[1] for language in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
        self.assertEqual(read.call_count, 2)
        self.assertEqual(len(json.loads(output.getvalue())["errors"]), 2)

    def test_cli_malformed_nested_spans_fail_before_either_language_io(self):
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
