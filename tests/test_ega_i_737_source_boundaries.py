"""Independent offline extraction and rehash attacks for EGA I 7.3.5--7.3.7.

Literal source blocks below are transcribed from the source-target evidence,
not synthesized from checker constants. Their surrounding bytes are explicitly
synthetic and NEVER qualify as whole-source identity or semantic admission.
"""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i737_source_boundaries as check


BLOCKS = {
    "fr": r"""\begin{corollary}[7.3.5]
\label{I.7.3.5-fr}
Si $X$ est irréductible, tout $\mathscr{R}(X)$-Module quasi-cohérent
$\mathscr{F}$ est un faisceau simple.
\end{corollary}

Il suffit de montrer que tout $x\in X$ admet un voisinage $U$ tel que
$\mathscr{F}|U$ soit un faisceau simple
(\hyperref[0.3.6.2-fr]{0, 3.6.2}), autrement dit on est ramené au cas où $X$
est affine~; on peut en outre supposer que $\mathscr{F}$ est le conoyau d'un
homomorphisme
$(\mathscr{R}(X))^{(I)}\to(\mathscr{R}(X))^{(J)}$
(\hyperref[0.5.1.3-fr]{0, 5.1.3}), et tout revient à voir que
$\mathscr{R}(X)$ est un faisceau simple~; mais cela est évident puisque
$\Gamma(U,\mathscr{R}(X))=R(X)$ pour tout ouvert non vide $U$, $U$ contenant
le point générique de $X$.

\begin{corollary}[7.3.6]
\label{I.7.3.6-fr}
Si $X$ est irréductible, pour tout $\mathscr{O}_X$-Module quasi-cohérent
$\mathscr{F}$, $\mathscr{F}\otimes_{\mathscr{O}_X}\mathscr{R}(X)$ est un
faisceau simple~; si en outre $X$ est réduit (donc intègre),
$\mathscr{F}\otimes_{\mathscr{O}_X}\mathscr{R}(X)$ est isomorphe à un
faisceau de la forme $(\mathscr{R}(X))^{(I)}$.
\end{corollary}

La seconde assertion résulte de ce que $R(X)$ est alors un corps.

\begin{proposition}[7.3.7]
\label{I.7.3.7-fr}
Supposons que le préschéma $X$ soit localement intègre ou localement
\oldpage[I]{163}
noethérien. Alors $\mathscr{R}(X)$ est une $\mathscr{O}_X$-Algèbre
quasi-cohérente~; si en outre $X$ est réduit (ce qui est le cas lorsque $X$
est localement intègre), l'homomorphisme canonique
$\mathscr{O}_X\to\mathscr{R}(X)$ est injectif.
\end{proposition}

La question étant locale, la première assertion résulte de
(\hyperref[I.7.3.3-fr]{7.3.3})~; la seconde résulte aussitôt de
(\hyperref[I.7.2.3-fr]{7.2.3}).

\begin{env}[7.3.8]
\label{I.7.3.8-fr}
""",
    "en": r"""\begin{corollary}[7.3.5]
\label{I.7.3.5}
If $X$ is irreducible, then every quasi-coherent $\sh{R}(X)$-module $\sh{F}$ is a simple sheaf.
\end{corollary}

\begin{proof}
It suffices to show that every $x\in X$ admits a neighbourhood $U$ such that $\sh{F}|U$ is a simple sheaf \sref[0]{0.3.6.2}; in other words, we are led to considering the case where $X$ is affine; we can further suppose that $\sh{F}$ is the cokernel of a homomorphism $(\sh{R}(X))^{I}\to(\sh{R}(X))^{J}$ \sref[0]{0.5.1.3}, and everything then follows from showing that $\sh{R}(X)$ is a simple sheaf; but this is evident, because $\Gamma(U,\sh{R}(X))=R(X)$ for every nonempty open subset $U$, where $U$ contains the generic point of $X$.
\end{proof}

\begin{corollary}[7.3.6]
\label{I.7.3.6}
If $X$ is irreducible, then, for every quasi-coherent $\sh{O}_X$-module $\sh{F}$, $\sh{F}\otimes_{\sh{O}_X}\sh{R}(X)$ is a simple sheaf; if, further, $X$ is reduced (and thus integral), then $\sh{F}\otimes_{\sh{O}_X}\sh{R}(X)$ is isomorphic to a sheaf of the form $(\sh{R}(X))^{(I)}$.
\end{corollary}

\begin{proof}
The second claim follows from the fact that $R(X)$ is a field.
\end{proof}

\begin{proposition}[7.3.7]
\label{I.7.3.7}
Suppose that the prescheme $X$ is locally integral or locally
\oldpage[I]{163}
Noetherian.
Then $\sh{R}(X)$ is a quasi-coherent $\sh{O}_X$-algebra; if, further, $X$ is reduced (which will be the case whenever $X$ is locally integral), then the canonical homomorphism $\sh{O}_X\to\sh{R}(X)$ is injective.
\end{proposition}

\begin{proof}
Since the question is local, the first claim follows from \sref{I.7.3.3}; the second follows from \sref{I.7.2.3}.
\end{proof}

\begin{env}[7.3.8]
\label{I.7.3.8}
""",
}
FIRST = {"fr": 606, "en": 350}
OFFSET = {"fr": 30619, "en": 28278}
LENGTH = {"fr": 38226, "en": 35788}
PINNED_SHA = {
    "fr": "73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522",
    "en": "B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC",
}
URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
SLICES = {"fr": ((606, 622), (623, 633), (634, 647)),
          "en": ((350, 358), (359, 367), (368, 379))}
ENVS = {"fr": ((606, 610), (623, 630), (634, 642)),
        "en": ((350, 353), (359, 362), (368, 374))}
PARTS = {"fr": ((612, 621), (632, 632), (644, 646)),
         "en": ((355, 357), (364, 366), (376, 378))}
BODIES = {"fr": ((612, 621), (632, 632), (644, 646)),
          "en": ((356, 356), (365, 365), (377, 377))}
OWNERS = ("ega:I.7.3.5:proof", "ega:I.7.3.6:proof", "ega:I.7.3.7:proof")
PAGE = {"fr": 637, "en": 371}
LAST = {"fr": 647, "en": 379}
NEXT = {"fr": (648, 649), "en": (380, 381)}
UNITS = ("ega:I.7.3.5", "ega:I.7.3.6", "ega:I.7.3.7")
ENV_NAMES = ("corollary", "corollary", "proposition")


def split_raw(raw):
    return [part + b"\n" for part in raw.split(b"\n")[:-1]]


def fixture(language):
    """Exact review blocks and offsets, synthetic whole-source surroundings."""
    lines = [b"\n"] * (FIRST[language] - 1)
    comment = b"% SYNTHETIC NON-AUTHORITY SURROUNDING BYTES "
    padding = OFFSET[language] - len(lines) - len(comment)
    lines[0] = comment + b"x" * padding + b"\n"
    before = b"".join(lines)
    assert len(before) == OFFSET[language]
    raw = before + BLOCKS[language].encode("utf-8")
    tail = b"later mathematics is deliberately outside this review "
    raw += tail + b"x" * (LENGTH[language] - len(raw) - len(tail) - 1) + b"\n"
    assert len(raw) == LENGTH[language]
    return raw


def span(raw, start, end):
    lines = split_raw(raw)
    block = b"".join(lines[start - 1:end])
    offset = len(b"".join(lines[:start - 1]))
    return {"lf_line_start": start, "lf_line_end": end, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(),
            "byte_offset_start": offset, "byte_offset_end_exclusive": offset + len(block)}


def independent_metadata(raw, language):
    """No checker tables, extraction, normalization or hash constants used."""
    suffix = "-fr" if language == "fr" else ""
    return {
        "url": URLS[language], "full_bytes": len(raw),
        "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
        "slices": {u: span(raw, *r) for u, r in zip(UNITS, SLICES[language])},
        "numbered_environments": {u: {
            "label": u[4:] + suffix, "environment": env, "begin_line": r[0],
            "label_line": r[0] + 1, "closing_line": r[1], **span(raw, *r)}
            for u, env, r in zip(UNITS, ENV_NAMES, ENVS[language])},
        "owned_parts": {u: span(raw, *r) for u, r in zip(OWNERS, PARTS[language])},
        "proof_bodies": {u: span(raw, *r) for u, r in zip(OWNERS, BODIES[language])},
        "page_markers": {"ega:I.7.3.7:page-marker": span(raw, PAGE[language], PAGE[language])},
        "section_heading": None,
        "combined": span(raw, FIRST[language], LAST[language]),
        "next_excluded_boundary": {"source_unit": "ega:I.7.3.8", **span(raw, *NEXT[language])},
    }


def pinned_metadata(language):
    result = independent_metadata(fixture(language), language)
    # Full-file identity is non-fixture evidence, explicitly transcribed above.
    result["full_sha256"] = PINNED_SHA[language]
    return result


def replace_line(raw, number, content):
    lines = split_raw(raw)
    lines[number - 1] = content
    return b"".join(lines)


def at_path(value, path):
    for key in path:
        value = value[key]
    return value


def leaf_paths(value, prefix=()):
    for key, child in value.items():
        if isinstance(child, dict):
            yield from leaf_paths(child, (*prefix, key))
        else:
            yield (*prefix, key)


class SourceBoundary737Tests(unittest.TestCase):
    def test_independent_blocks_match_all_pinned_span_metadata(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            self.assertEqual(check.validate_artifact(expected, language), [])
            self.assertEqual(check.expected_contract(language), expected)
            self.assertEqual(check.artifact(fixture(language), language),
                             independent_metadata(fixture(language), language))
            self.assertEqual(check.verify_structure(fixture(language), language), [])
        self.assertEqual(pinned_metadata("fr")["combined"]["sha256"],
                         "44892720D0751CDD5EEC00B030AB61E153260DB6AE29629A6207643B103D55AD")
        self.assertEqual(pinned_metadata("en")["combined"]["sha256"],
                         "BBB8126EE7F4EB4EEC4235E9154111E17EB2B47AA0E87A4B490AA0F70B4EC29F")

    def test_synthetic_surroundings_never_certify_whole_source(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            self.assertEqual(check.verify_source(raw, language, pinned_metadata(language)),
                             [language + ".source.full_sha256: pinned identity/boundary mismatch"])
            rehashed = independent_metadata(raw, language)
            self.assertTrue(check.validate_artifact(rehashed, language))
            self.assertTrue(check.verify_source(raw, language, rehashed))

    def test_no_heading_reownership_and_complete_contiguous_unit_proofs(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            self.assertIsNone(expected["section_heading"])
            previous = expected["combined"]["byte_offset_start"]
            for unit, proof in zip(UNITS, OWNERS):
                owner = expected["slices"][unit]
                declaration = expected["numbered_environments"][unit]
                complete = expected["owned_parts"][proof]
                body = expected["proof_bodies"][proof]
                self.assertEqual(owner["byte_offset_start"], previous)
                self.assertEqual(owner["byte_offset_start"], declaration["byte_offset_start"])
                self.assertEqual(complete["byte_offset_start"], declaration["byte_offset_end_exclusive"] + 1)
                self.assertEqual(owner["byte_offset_end_exclusive"], complete["byte_offset_end_exclusive"] + 1)
                if language == "fr":
                    self.assertEqual(complete, body)
                else:
                    self.assertEqual(body["lf_line_start"], complete["lf_line_start"] + 1)
                    self.assertEqual(body["lf_line_end"], complete["lf_line_end"] - 1)
                    self.assertEqual(complete["bytes"] - body["bytes"], 26)
                previous = owner["byte_offset_end_exclusive"]
            self.assertEqual(previous, expected["combined"]["byte_offset_end_exclusive"])
            self.assertEqual(previous, expected["next_excluded_boundary"]["byte_offset_start"])
            self.assertEqual(expected["combined"]["bytes"], sum(s["bytes"] for s in expected["slices"].values()))
            self.assertEqual(set(expected["owned_parts"]), set(OWNERS))
            self.assertEqual(set(expected["proof_bodies"]), set(OWNERS))
            self.assertNotIn("ega:I.7.3.8", expected["slices"])

    def test_page_marker_is_nested_inside_737_declaration_not_extra_owner(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            page = expected["page_markers"]["ega:I.7.3.7:page-marker"]
            declaration = expected["numbered_environments"][UNITS[2]]
            self.assertGreater(page["byte_offset_start"], declaration["byte_offset_start"])
            self.assertLess(page["byte_offset_end_exclusive"], declaration["byte_offset_end_exclusive"])
            for group in ("slices", "owned_parts", "proof_bodies"):
                altered = copy.deepcopy(expected)
                altered[group]["ega:I.7.3.7:page-marker"] = page
                self.assertTrue(check.validate_artifact(altered, language))
            altered = copy.deepcopy(expected)
            altered["page_markers"]["ega:I.7.3.6:page-marker"] = altered["page_markers"].pop("ega:I.7.3.7:page-marker")
            self.assertTrue(check.validate_artifact(altered, language))

    def test_every_contract_leaf_is_fixed_and_strictly_typed(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            for path in leaf_paths(expected):
                old = at_path(expected, path)
                if type(old) is int:
                    alternatives = (old + 1, float(old), True, None)
                elif old is None:
                    alternatives = ({}, "", False, {"source_unit": "ega:I.7.3"})
                else:
                    alternatives = (old + "changed", "", None, [])
                for new in alternatives:
                    altered = copy.deepcopy(expected)
                    at_path(altered, path[:-1])[path[-1]] = new
                    with self.subTest(language=language, path=path, replacement=new):
                        self.assertTrue(check.validate_artifact(altered, language))
            for key in expected:
                altered = copy.deepcopy(expected)
                del altered[key]
                self.assertTrue(check.validate_artifact(altered, language))
            for group in ("slices", "numbered_environments", "owned_parts", "proof_bodies", "page_markers"):
                altered = copy.deepcopy(expected)
                altered[group]["fabricated owner"] = {}
                self.assertTrue(check.validate_artifact(altered, language))
            altered = check.expected_contract(language)
            altered["slices"][UNITS[0]]["bytes"] = 0
            self.assertEqual(check.expected_contract(language), expected)

    def assert_literal_damage(self, language, old, new, owner):
        raw = fixture(language)
        self.assertIn(old.encode("utf-8"), raw)
        damaged = raw.replace(old.encode("utf-8"), new.encode("utf-8"), 1)
        self.assertIn(owner + ": literal content fingerprint mismatch", check.verify_structure(damaged, language))
        self.assertTrue(check.verify_source(damaged, language, independent_metadata(damaged, language)))

    def test_substantive_hypotheses_scalar_rings_formulas_and_crossrefs_after_rehash(self):
        cases = {
            "fr": (
                ("irréductible, tout", "réduit, tout", UNITS[0]),
                (r"$\mathscr{R}(X)$-Module", r"$\mathscr{O}_X$-Module", UNITS[0]),
                ("quasi-cohérent\n", "cohérent\n", UNITS[0]),
                ("tout $x\\in X$", "un $x\\in X$", OWNERS[0]),
                (r"\hyperref[0.3.6.2-fr]{0, 3.6.2}", r"\hyperref[0.3.6.1-fr]{0, 3.6.1}", OWNERS[0]),
                ("le conoyau d'un", "le noyau d'un", OWNERS[0]),
                (r"\hyperref[0.5.1.3-fr]{0, 5.1.3}", r"\hyperref[0.5.1.2-fr]{0, 5.1.2}", OWNERS[0]),
                (r"$\Gamma(U,\mathscr{R}(X))=R(X)$", r"$\Gamma(U,\mathscr{R}(X))=K(X)$", OWNERS[0]),
                ("non vide $U$", "vide $U$", OWNERS[0]),
                ("le point générique", "un point fermé", OWNERS[0]),
                (r"\otimes_{\mathscr{O}_X}", r"\otimes_{\mathscr{R}(X)}", UNITS[1]),
                ("réduit (donc intègre)", "intègre (donc réduit)", UNITS[1]),
                ("La seconde assertion", "La première assertion", OWNERS[1]),
                ("est alors un corps", "est toujours un corps", OWNERS[1]),
                ("intègre ou localement", "intègre et localement", UNITS[2]),
                ("est injectif", "est surjectif", UNITS[2]),
                ("La question étant locale", "La question étant globale", OWNERS[2]),
                (r"\hyperref[I.7.3.3-fr]{7.3.3}", r"\hyperref[I.7.3.4-fr]{7.3.4}", OWNERS[2]),
                (r"\hyperref[I.7.2.3-fr]{7.2.3}", r"\hyperref[I.7.2.4-fr]{7.2.4}", OWNERS[2])),
            "en": (
                ("irreducible, then every", "reduced, then every", UNITS[0]),
                (r"$\sh{R}(X)$-module", r"$\sh{O}_X$-module", UNITS[0]),
                ("every quasi-coherent", "every coherent", UNITS[0]),
                ("every $x\\in X$", "some $x\\in X$", OWNERS[0]),
                (r"\sref[0]{0.3.6.2}", r"\sref[0]{0.3.6.1}", OWNERS[0]),
                ("the cokernel of", "the kernel of", OWNERS[0]),
                (r"\sref[0]{0.5.1.3}", r"\sref[0]{0.5.1.2}", OWNERS[0]),
                (r"$\Gamma(U,\sh{R}(X))=R(X)$", r"$\Gamma(U,\sh{R}(X))=K(X)$", OWNERS[0]),
                ("every nonempty open", "some nonempty open", OWNERS[0]),
                ("the generic point", "a closed point", OWNERS[0]),
                (r"\otimes_{\sh{O}_X}", r"\otimes_{\sh{R}(X)}", UNITS[1]),
                ("reduced (and thus integral)", "integral (and thus reduced)", UNITS[1]),
                ("The second claim", "The first claim", OWNERS[1]),
                ("is a field", "is a domain", OWNERS[1]),
                ("integral or locally", "integral and locally", UNITS[2]),
                ("is injective", "is surjective", UNITS[2]),
                ("question is local", "question is global", OWNERS[2]),
                (r"\sref{I.7.3.3}", r"\sref{I.7.3.4}", OWNERS[2]),
                (r"\sref{I.7.2.3}", r"\sref{I.7.2.4}", OWNERS[2])),
        }
        for language, entries in cases.items():
            for old, new, owner in entries:
                with self.subTest(language=language, clause=old):
                    self.assert_literal_damage(language, old, new, owner)

    def test_735_literal_direct_sum_notation_drift_is_preserved_not_normalized(self):
        self.assert_literal_damage("fr", r"^{(I)}\to(\mathscr{R}(X))^{(J)}",
                                   r"^{I}\to(\mathscr{R}(X))^{J}", OWNERS[0])
        self.assert_literal_damage("en", r"^{I}\to(\sh{R}(X))^{J}",
                                   r"^{(I)}\to(\sh{R}(X))^{(J)}", OWNERS[0])

    def test_every_substantive_declaration_and_proof_line_is_required(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            ranges = [(u, (a + 2, b - 1)) for u, (a, b) in zip(UNITS, ENVS[language])]
            ranges += list(zip(OWNERS, BODIES[language]))
            for owner, (start, end) in ranges:
                for n in range(start, end + 1):
                    original = split_raw(raw)[n - 1]
                    self.assertTrue(original.strip())
                    for replacement in (b"\n", b"% " + original, b"omitted clause\n"):
                        errors = check.verify_structure(replace_line(raw, n, replacement), language)
                        self.assertIn(owner + ": literal content fingerprint mismatch", errors)

    def test_comment_normalization_never_substitutes_for_exact_source_bytes(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            n = ENVS[language][0][0] + 2
            line = split_raw(raw)[n - 1]
            damaged = replace_line(raw, n, b" \t" + line[:-1] + b"  % harmless comment\n")
            self.assertEqual(check.verify_structure(damaged, language), [])
            self.assertTrue(check.verify_source(damaged, language, independent_metadata(damaged, language)))

    def test_numbered_markers_missing_nested_foreign_duplicated_or_misnumbered_fail(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            for index, (start, end) in enumerate(ENVS[language]):
                for n in (start, start + 1, end):
                    token = split_raw(raw)[n - 1].rstrip(b"\n")
                    for replacement in (b"\n", b"% " + token + b"\n", token + b" " + token + b"\n",
                                        token + b" unowned continuation\n"):
                        self.assertTrue(check.verify_structure(replace_line(raw, n, replacement), language))
                body_line = split_raw(raw)[start + 1]
                env = ENV_NAMES[index].encode()
                for token in (b"\\begin{" + env + b"}", b"\\end{" + env + b"}",
                              b"\\begin{foreign}", b"\\end{foreign}", b"\\begin{env}[7.3.99]",
                              b"\\begin{proof}\\end{proof}"):
                    damaged = replace_line(raw, start + 2, token + b" " + body_line)
                    self.assertTrue(any("wrapper" in e for e in check.verify_structure(damaged, language)))
                begin = split_raw(raw)[start - 1]
                damaged = replace_line(raw, start, begin.replace(b"7.3.", b"7.4."))
                self.assertTrue(any("numbered" in e for e in check.verify_structure(damaged, language)))

    def test_all_english_proof_wrappers_have_exact_unique_endpoints(self):
        raw = fixture("en")
        for start, end in PARTS["en"]:
            for n in (start, end):
                token = split_raw(raw)[n - 1].rstrip(b"\n")
                for line in (b"\n", b"% " + token + b"\n", token + b" " + token + b"\n"):
                    self.assertTrue(any("wrapper" in e for e in check.verify_structure(replace_line(raw, n, line), "en")))
                for destination in (start - 1, start + 1, end + 1):
                    lines = split_raw(raw)
                    lines[n - 1], lines[destination - 1] = lines[destination - 1], lines[n - 1]
                    self.assertTrue(any("wrapper" in e for e in check.verify_structure(b"".join(lines), "en")))

    def test_all_french_proofs_remain_unwrapped(self):
        raw = fixture("fr")
        for start, end in PARTS["fr"]:
            for n in (start, end):
                original = split_raw(raw)[n - 1]
                for token in (b"\\begin{proof} ", b"\\end{proof} ", b"\\begin{env}[7.3.99] "):
                    self.assertTrue(any("wrapper" in e for e in check.verify_structure(replace_line(raw, n, token + original), "fr")))

    def test_separators_cannot_acquire_source_prose_independent_argument_or_heading(self):
        for language, blanks in (("fr", (611, 622, 631, 633, 643, 647)),
                                 ("en", (354, 358, 363, 367, 375, 379))):
            raw = fixture(language)
            for n in blanks:
                self.assertEqual(split_raw(raw)[n - 1], b"\n")
                for content in (b"independent tensor-presentation argument\n",
                                b"\\begin{proof} extra first-assertion proof \\end{proof}\n",
                                b"\\subsection{Sheaf of rational functions}\n"):
                    self.assertTrue(check.verify_structure(replace_line(raw, n, content), language))

    def test_page_excluded_env_and_label_cannot_move_be_hidden_or_change(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            for n in (PAGE[language], *NEXT[language]):
                line = split_raw(raw)[n - 1]
                for changed in (b"\n", b"% " + line, b"changed " + line, line[:-1] + b" " + line):
                    self.assertTrue(check.verify_structure(replace_line(raw, n, changed), language))
                lines = split_raw(raw)
                lines[n - 1], lines[n] = lines[n], lines[n - 1]
                self.assertTrue(check.verify_structure(b"".join(lines), language))
            self.assertTrue(check.verify_structure(raw.replace(b"\\oldpage[I]{163}", b"\\oldpage[I]{162}"), language))
            self.assertTrue(check.verify_structure(raw.replace(b"\\begin{env}[7.3.8]", b"\\begin{proposition}[7.3.8]"), language))

    def test_global_duplicate_labels_numbered_begins_and_page_fail(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            positions = [PAGE[language], *NEXT[language]]
            positions += [n for start, _ in ENVS[language] for n in (start, start + 1)]
            for n in positions:
                marker = split_raw(raw)[n - 1]
                for added in (marker, b"inline " + marker):
                    self.assertTrue(check.verify_structure(raw + added, language))

    def test_preceding_and_later_math_is_excluded_but_whole_identity_stays_pinned(self):
        for language in ("fr", "en"):
            raw = fixture(language).replace(b"later mathematics is deliberately outside this review", b"changed later material")
            raw = replace_line(raw, FIRST[language] - 1, b"preceding 7.3.4 is not re-owned\n")
            self.assertEqual(check.verify_structure(raw, language), [])
            self.assertTrue(check.verify_source(raw, language, independent_metadata(raw, language)))

    def test_raw_lf_utf8_context_types_and_size_fail_closed(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            cases = (None, "not bytes", bytearray(raw), b"", raw[:-1], raw.replace(b"\n", b"\r\n"),
                     b"\xff\n", b"\xef\xbb\xbf" + raw, b"x" * (1048576 + 1) + b"\n",
                     b"".join(split_raw(raw)[:NEXT[language][1] - 1]))
            for damaged in cases:
                self.assertTrue(check.verify_source(damaged, language))
            unusual = raw.replace(b"SYNTHETIC", b"SYNTHETIC\x0c\xe2\x80\xa8", 1)
            self.assertEqual(len(check.raw_lines(unusual)), len(split_raw(raw)))
            self.assertEqual(check.verify_structure(unusual, language), [])
        for language in ("xx", [], None, 1):
            self.assertTrue(check.validate_artifact({}, language))
            self.assertTrue(check.verify_source(b"x\n", language))
            with self.assertRaises(ValueError):
                check.artifact(b"x\n", language)
        for value in (None, [], {}, True):
            self.assertTrue(check.validate_artifact(value, "fr"))

    def test_raw_span_inclusive_offsets_strict_types_and_comment_escape_parity(self):
        lines = [b"a\n", b"bc\n"]
        for start, end in ((0, 1), (1, 3), (2, 1), (True, 1), (1, 2.0), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span(lines, start, end)
        self.assertEqual(check.raw_span(lines, 2, 2), span(b"a\nbc\n", 2, 2))
        for raw, expected in ((b"x % hidden", b"x "), (rb"x \% visible", rb"x \% visible"),
                              (rb"x \\% hidden", rb"x \\"), (rb"x \\\% visible", rb"x \\\% visible")):
            self.assertEqual(check._uncomment(raw), expected)
        self.assertEqual(check._text([b"a % omitted\n", b" b\tc\n"]), b"a b c")


class BoundedReplay737Tests(unittest.TestCase):
    def test_cached_route_exact_bound_once_and_no_network(self):
        for language in ("fr", "en"):
            cached = MagicMock(spec=Path)
            handle = cached.open.return_value.__enter__.return_value
            handle.read.return_value = fixture(language)
            with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
                self.assertEqual(check.read_source(pinned_metadata(language), language, cached), fixture(language))
            cached.open.assert_called_once_with("rb")
            handle.read.assert_called_once_with(LENGTH[language] + 1)

    def test_network_route_pinned_timed_bounded_single_attempt(self):
        for language in ("fr", "en"):
            response = MagicMock()
            response.__enter__.return_value.read.return_value = fixture(language)
            with patch.object(check, "urlopen", return_value=response) as fetch:
                self.assertEqual(check.fetch_source(language), fixture(language))
            fetch.assert_called_once_with(URLS[language], timeout=30)
            response.__enter__.return_value.read.assert_called_once_with(LENGTH[language] + 1)

    def test_short_oversized_nonbytes_and_transport_failure_never_retry(self):
        for returned in (b"", fixture("en")[:-1], fixture("en") + b"x", "not bytes", None):
            response = MagicMock()
            response.__enter__.return_value.read.return_value = returned
            with patch.object(check, "urlopen", return_value=response) as fetch:
                with self.assertRaises(ValueError):
                    check.fetch_source("en")
                fetch.assert_called_once()
        with patch.object(check, "urlopen", side_effect=OSError("bounded failure")) as fetch:
            with self.assertRaises(OSError):
                check.fetch_source("en")
            fetch.assert_called_once()

    def test_malformed_contract_language_or_cap_fail_before_io(self):
        cached = MagicMock(spec=Path)
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            bad = [None, [], {}, {**expected, "full_bytes": True},
                   {**expected, "full_bytes": 1048577}, {**expected, "url": "https://example.invalid/"},
                   {**expected, "full_sha256": "0" * 64}, {**expected, "proof_bodies": {}}]
            with patch.object(check, "urlopen") as fetch:
                for receipt in bad:
                    for cache in (None, cached):
                        with self.assertRaises(ValueError):
                            check.read_source(receipt, language, cache)
                fetch.assert_not_called()
                cached.open.assert_not_called()
        with patch.object(check, "urlopen") as fetch:
            for language in ("invalid", None, []):
                with self.assertRaises(ValueError):
                    check.fetch_source(language, cached)
            for size in (True, 0, 1048576, 1048577):
                with patch.dict(check.SOURCE_IDENTITIES, {"en": (size, PINNED_SHA["en"])}):
                    with self.assertRaises(ValueError):
                        check.fetch_source("en", cached)
            fetch.assert_not_called()
            cached.open.assert_not_called()

    def test_cli_validates_both_language_contracts_before_either_source_read(self):
        receipt = {"languages": {lang: pinned_metadata(lang) for lang in ("fr", "en")}}
        invalid = ["{", "[]", "{}", '{"languages":[]}', '{"languages":{"fr":{}}}']
        for language in ("fr", "en"):
            for key in receipt["languages"][language]:
                altered = copy.deepcopy(receipt)
                altered["languages"][language][key] = "invalid"
                invalid.append(json.dumps(altered))
            altered = copy.deepcopy(receipt)
            altered["languages"][language]["owned_parts"]["ega:I.7.3.8:proof"] = {}
            invalid.append(json.dumps(altered))
        invalid += [json.dumps({"languages": {**receipt["languages"], "other": {}}})]
        valid = json.dumps(receipt)
        invalid += [valid.replace('"full_bytes": 38226', '"full_bytes": 0, "full_bytes": 38226'),
                    valid.replace('"languages":', '"languages": {}, "languages":', 1)]
        for text in invalid:
            with patch.object(Path, "read_text", return_value=text), patch.object(check, "read_source") as read, \
                    patch("sys.stdout", new_callable=io.StringIO) as output:
                self.assertTrue(check.main([]))
                read.assert_not_called()
                self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")

    def test_cli_missing_receipt_and_each_transport_failure_structured(self):
        with patch.object(Path, "read_text", side_effect=FileNotFoundError("absent")), \
                patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            read.assert_not_called()
            self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")
        receipt = {"languages": {lang: pinned_metadata(lang) for lang in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            self.assertEqual(read.call_count, 2)
            self.assertEqual(len(json.loads(output.getvalue())["errors"]), 2)

    def test_cli_plumbing_default_receipt_and_no_file_writes(self):
        receipt = {"languages": {lang: pinned_metadata(lang) for lang in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)) as load, \
                patch.object(check, "read_source", side_effect=lambda expected, language, cached: fixture(language)) as read, \
                patch.object(check, "verify_source", return_value=[]) as verify, \
                patch.object(Path, "write_text") as write_text, patch.object(Path, "write_bytes") as write_bytes, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "cached-fr.tex", "--english", "cached-en.tex"]))
            load.assert_called_once_with(encoding="utf-8")
            self.assertEqual(read.call_count, 2)
            self.assertEqual(verify.call_count, 2)
            self.assertEqual(read.call_args_list[0].args[2], Path("cached-fr.tex"))
            self.assertEqual(read.call_args_list[1].args[2], Path("cached-en.tex"))
            write_text.assert_not_called()
            write_bytes.assert_not_called()
            result = json.loads(output.getvalue())
            self.assertEqual(result["schema"], "ega-i737-raw-source-boundary-replay/v1")
            self.assertEqual(result["status"], "PASS")
        self.assertEqual(check.RECEIPT.name, "ega-i-7.3.5-7.3.7-semantic-checkpoint-2026-09-08.json")


if __name__ == "__main__":
    unittest.main()
