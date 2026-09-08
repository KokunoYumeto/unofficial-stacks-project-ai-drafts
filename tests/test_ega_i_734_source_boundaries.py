"""Independent offline extraction/rehash attacks for EGA I 7.3.1--7.3.4.

The reviewed source blocks and coordinates below were transcribed independently
from the pinned raw sources and preparation. They do not use the checker's
tables or hashes to synthesize passing content. Surrounding bytes are synthetic:
these fixtures must NEVER pass whole-source identity or imply semantic admission.
"""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i734_source_boundaries as check


BLOCKS = {
    "fr": r"""\subsection{Faisceau des fonctions rationnelles.}
\label{subsection:I.7.3-fr}

\begin{env}[7.3.1]
\label{I.7.3.1-fr}
Soit $X$ un préschéma. Pour tout ouvert $U\subset X$, désignons par $R(U)$
l'anneau des fonctions rationnelles sur $U$
(\hyperref[I.7.1.3-fr]{7.1.3})~; c'est une
$\Gamma(U,\mathscr{O}_X)$-algèbre. En outre, si $V\subset U$ est un second
ouvert de $X$, toute section de $\mathscr{O}_X$ au-dessus d'une partie
ouverte partout dense de $U$ donne par restriction à $V$ une section
au-dessus d'une partie ouverte partout dense de $V$, et si deux sections
coïncident au-dessus d'une partie ouverte partout dense de $U$, leurs
restrictions à $V$ coïncident au-dessus d'une partie ouverte partout dense de
$V$. On définit donc ainsi un di-homomorphisme d'algèbres
$\rho_{V,U}:R(U)\to R(V)$, et il est clair que si $U\supset V\supset W$ sont
trois ouverts de $X$, on a
$\rho_{W,U}=\rho_{W,V}\circ\rho_{V,U}$~; les $R(U)$ définissent donc un
\emph{préfaisceau} d'algèbres sur $X$.
\end{env}

\oldpage[I]{162}
\begin{definition}[7.3.2]
\label{I.7.3.2-fr}
On appelle \emph{faisceau des fonctions rationnelles} sur un préschéma $X$
et on désigne par $\mathscr{R}(X)$ la $\mathscr{O}_X$-Algèbre associée au
préfaisceau formé des $R(U)$.
\end{definition}

Pour tout préschéma $X$ et tout ouvert $U\subset X$, il est clair que le
faisceau induit $\mathscr{R}(X)|U$ n'est autre que $\mathscr{R}(U)$.

\begin{proposition}[7.3.3]
\label{I.7.3.3-fr}
Soit $X$ un préschéma tel que la famille $(X_\lambda)$ de ses composantes
irréductibles soit localement finie (ce qui est en particulier le cas lorsque
l'espace sous-jacent à $X$ est localement noethérien). Alors le
$\mathscr{O}_X$-Module $\mathscr{R}(X)$ est quasi-cohérent, et pour tout
ouvert $U$ de $X$ ne rencontrant qu'un nombre fini de composantes $X_\lambda$,
$R(U)$ est égal à $\Gamma(U,\mathscr{R}(X))$ et s'identifie canoniquement au
composé direct des anneaux locaux des points génériques des $X_\lambda$ telles
que $U\cap X_\lambda\neq\varnothing$.
\end{proposition}

On peut évidemment se limiter au cas où $X$ n'a qu'un nombre fini de
composantes irréductibles $X_i$, de points génériques $x_i$
($1\leq i\leq n$). Le fait que $R(U)$ est canoniquement identifié au composé
direct des $\mathscr{O}_{x_i}=R(X_i)$ tels que
$U\cap X_i\neq\varnothing$ résulte alors de
(\hyperref[I.7.1.7-fr]{7.1.7}). Montrons en outre que le préfaisceau
$U\to R(U)$ vérifie les axiomes des faisceaux, ce qui prouvera que
$R(U)=\Gamma(U,\mathscr{R}(X))$. En effet, il vérifie (F 1) d'après ce qui
précède. Pour voir qu'il satisfait à (F 2), considérons un recouvrement d'un
ouvert $U$ de $X$ par des ouverts $V_\alpha\subset U$~; si les
$s_\alpha\in R(V_\alpha)$ sont telles que les restrictions de $s_\alpha$ et
$s_\beta$ à $V_\alpha\cap V_\beta$ coïncident pour tout couple d'indices, on
en conclut que pour tout indice $i$ tel que $U\cap X_i\neq\varnothing$, les
composantes dans $R(X_i)$ de toutes les $s_\alpha$ telles que
$V_\alpha\cap X_i\neq\varnothing$ sont les mêmes~; désignant par $t_i$ cette
composante, il est clair que l'élément de $R(U)$ ayant les $t_i$ pour
composantes a pour restriction $s_\alpha$ à chaque $V_\alpha$. Enfin, pour
voir que $\mathscr{R}(X)$ est quasi-cohérent, on peut se limiter au cas où
$X=\operatorname{Spec}(A)$ est affine~; en prenant pour $U$ les ouverts
affines de la forme $D(f)$, où $f\in A$, il résulte de ce qui précède et de la
définition (\hyperref[I.1.3.4-fr]{1.3.4}) que l'on a
$\mathscr{R}(X)=\widetilde M$, où $M$ est somme directe des $A$-modules
$A_{x_i}$.

\begin{corollary}[7.3.4]
\label{I.7.3.4-fr}
Soit $X$ un préschéma réduit n'ayant qu'un nombre fini de composantes
irréductibles, et soient $X_i$ ($1\leq i\leq n$) les sous-préschémas fermés
réduits de $X$ ayant pour espaces sous-jacents les composantes irréductibles de
$X$ (\hyperref[I.5.2.1-fr]{5.2.1}). Si $h_i$ est l'injection canonique
$X_i\to X$, $\mathscr{R}(X)$ est alors composée directe des
$\mathscr{O}_X$-Algèbres $(h_i)_*(\mathscr{R}(X_i))$.
\end{corollary}

\begin{corollary}[7.3.5]
\label{I.7.3.5-fr}
""",
    "en": r"""\subsection{Sheaf of rational functions}
\label{subsection:I.7.3}

\begin{env}[7.3.1]
\label{I.7.3.1}
Let $X$ be a prescheme.
For every open subset $U\subset X$, we denote by $R(U)$ the ring of rational functions on $U$ \sref{I.7.1.3}; this is a $\Gamma(U,\sh{O}_X)$-algebra.
Further, if $V\subset U$ is a second open subset of $X$, then every section of $\sh{O}_X$ over a dense open subset of $U$ gives, by restriction to $V$, a section over a dense open subset of $V$, and if two sections agree on a dense open subset of $U$, then their restrictions to $V$ agree on a dense open subset of $V$.
We can thus define a di-homomorphism of algebras $\rho_{V,U}:R(U)\to R(V)$, and it is clear that, if $U\supset V\supset W$ are open subsets of $X$, then we have $\rho_{W,U}=\rho_{W,V}\circ\rho_{V,U}$; the $R(U)$ thus define a \emph{presheaf} of algebras on $X$.
\end{env}

\oldpage[I]{162}
\begin{definition}[7.3.2]
\label{I.7.3.2}
We define the sheaf of rational functions on a prescheme $X$, denoted by $\sh{R}(X)$, to be the $\sh{O}_X$-algebra associated to the presheaf defined by the $R(U)$.
\end{definition}

For every prescheme $X$ and open subset $U\subset X$, it is clear that the induced sheaf $\sh{R}(X)|U$ is exactly $\sh{R}(U)$.

\begin{proposition}[7.3.3]
\label{I.7.3.3}
Let $X$ be a prescheme such that the family $(X_\lambda)$ of its irreducible components is locally finite (which is the case whenever the underlying space of $X$ is locally Noetherian).
Then the $\sh{O}_X$-module $\sh{R}(X)$ is quasi-coherent, and for every open subset $U$ of $X$ that has a nonempty intersection with only finitely many of the components $X_\lambda$, $R(U)$ is equal to $\Gamma(U,\sh{R}(X))$, and can be canonically identified with the direct product of the local rings of the generic points of the $X_\lambda$ such that $U\cap X_\lambda\neq\emp$.
\end{proposition}

\begin{proof}
We can evidently restrict to the case where $X$ has only a finite number of irreducible components $X_i$, with generic points $x_i$ ($1\leq i\leq n$).
The fact that $R(U)$ can be canonically identified with the direct product of the $\sh{O}_{x_i}=R(X_i)$ such that $U\cap X_i\neq\emp$ then follows from \sref{I.7.1.7}.
We will show that the presheaf $U\to R(U)$ satisfies the sheaf axioms, which will prove that $R(U)=\Gamma(U,\sh{R}(X))$.
Indeed, it satisfies (F1) by what has already been discussed.
To see that it satisfies (F2), consider a cover of an open subset $U$ of $X$ by open subsets $V_\alpha\subset U$; if the $s_\alpha\in R(V_\alpha)$ are such that the restrictions of $s_\alpha$ and $s_\beta$ to $V_\alpha\cap V_\beta$ agree for every pair of indices, then we can conclude that, for every index $i$ such that $U\cap X_i\neq\emp$, the components in $R(X_i)$ of all the $s_\alpha$ such that $V_\alpha\cap X_i\neq\emp$ are all the same; denoting this component by $t_i$, it is clear that the element of $R(U)$ that has the $t_i$ as its components has $s_\alpha$ as its restriction to each $V_\alpha$.
Finally, to see that $\sh{R}(X)$ is quasi-coherent, we can restrict to the case where $X=\Spec(A)$ is affine; by taking $U$ to be an affine open subset of the form $D(f)$, where $f\in A$, it follows from the above and from Definition~\sref{I.1.3.4} that we have $\sh{R}(X)=\widetilde{M}$, where $M$ is the direct sum of the $A$-modules $A_{x_i}$.
\end{proof}

\begin{corollary}[7.3.4]
\label{I.7.3.4}
Let $X$ be a reduced prescheme that has only a finite number of irreducible components, and let $X_i$ ($1\leq i\leq n$) be the closed reduced preschemes of $X$ that have the irreducible components of $X$ as their underlying spaces \sref{I.5.2.1}.
If $h_i$ is the canonical injection $X_i\to X$, then $\sh{R}(X)$ is the direct product of the $\sh{O}_X$-algebras $(h_i)_*(\sh{R}(X_i))$.
\end{corollary}

\begin{corollary}[7.3.5]
\label{I.7.3.5}
""",
}
FIRST = {"fr": 528, "en": 310}
OFFSET = {"fr": 26520, "en": 24481}
LENGTH = {"fr": 38226, "en": 35788}
PINNED_SHA = {
    "fr": "73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522",
    "en": "B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC",
}
URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
SLICES = {"fr": ((531, 548), (549, 559), (560, 595), (596, 605)),
          "en": ((313, 320), (321, 328), (329, 343), (344, 349))}
ENVS = {"fr": ((531, 547), (550, 555), (560, 570), (596, 604)),
        "en": ((313, 319), (322, 325), (329, 333), (344, 348))}
PARTS = {"fr": ((557, 558), (572, 594)), "en": ((327, 327), (335, 342))}
OWNERS = ("ega:I.7.3.2:restriction-tail", "ega:I.7.3.3:proof")
PAGE = {"fr": 549, "en": 321}
LAST = {"fr": 605, "en": 349}
NEXT = {"fr": (606, 607), "en": (350, 351)}
UNITS = ("ega:I.7.3.1", "ega:I.7.3.2", "ega:I.7.3.3", "ega:I.7.3.4")
ENV_NAMES = ("env", "definition", "proposition", "corollary")


def split_raw(raw):
    return [part + b"\n" for part in raw.split(b"\n")[:-1]]


def fixture(language):
    """Exact review blocks/offsets, conspicuously synthetic surrounding bytes."""
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
    """No helper tables, extractor, normalization or hash constants are used."""
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
        "page_markers": {"ega:I.7.3.2:page-marker": span(raw, PAGE[language], PAGE[language])},
        "section_heading": {"source_unit": "ega:I.7.3", **span(raw, FIRST[language], FIRST[language] + 2)},
        "combined": span(raw, FIRST[language], LAST[language]),
        "next_excluded_boundary": {"source_unit": "ega:I.7.3.5", **span(raw, *NEXT[language])},
    }


def pinned_metadata(language):
    result = independent_metadata(fixture(language), language)
    # Only the full-file hash is non-fixture evidence, transcribed explicitly.
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


class SourceBoundary734Tests(unittest.TestCase):
    def test_independent_blocks_match_all_pinned_span_metadata(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            self.assertEqual(check.validate_artifact(expected, language), [])
            self.assertEqual(check.expected_contract(language), expected)
            self.assertEqual(check.artifact(fixture(language), language),
                             independent_metadata(fixture(language), language))
            self.assertEqual(check.verify_structure(fixture(language), language), [])
        self.assertEqual(pinned_metadata("fr")["combined"]["sha256"],
                         "1EDC404D41146486D7095EEBE70DC298A2B63C1351292A4B625848AB80A4D20B")
        self.assertEqual(pinned_metadata("en")["combined"]["sha256"],
                         "14966D617B087628BEB1D8682988D363D3C192259EA4644796FB2F70EC967F21")

    def test_synthetic_surroundings_never_certify_whole_source(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            errors = check.verify_source(raw, language, pinned_metadata(language))
            self.assertEqual(errors, [language + ".source.full_sha256: pinned identity/boundary mismatch"])
            rehashed = independent_metadata(raw, language)
            self.assertTrue(check.validate_artifact(rehashed, language))
            self.assertTrue(check.verify_source(raw, language, rehashed))

    def test_source_ownership_is_complete_contiguous_and_disjoint(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            previous = expected["section_heading"]["byte_offset_end_exclusive"]
            for unit in UNITS:
                owner = expected["slices"][unit]
                self.assertEqual(owner["byte_offset_start"], previous)
                previous = owner["byte_offset_end_exclusive"]
            self.assertEqual(previous, expected["combined"]["byte_offset_end_exclusive"])
            self.assertEqual(previous, expected["next_excluded_boundary"]["byte_offset_start"])
            self.assertEqual(expected["combined"]["bytes"],
                             expected["section_heading"]["bytes"] +
                             sum(s["bytes"] for s in expected["slices"].values()))
            self.assertEqual(set(expected["owned_parts"]), set(OWNERS))
            self.assertNotIn("ega:I.7.3.4:proof", expected["owned_parts"])

    def test_page_marker_belongs_to_732_not_731_or_numbered_wrapper(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            page = expected["page_markers"]["ega:I.7.3.2:page-marker"]
            self.assertEqual(page["byte_offset_start"], expected["slices"]["ega:I.7.3.2"]["byte_offset_start"])
            self.assertEqual(page["byte_offset_start"], expected["slices"]["ega:I.7.3.1"]["byte_offset_end_exclusive"])
            self.assertEqual(page["byte_offset_end_exclusive"],
                             expected["numbered_environments"]["ega:I.7.3.2"]["byte_offset_start"])
            altered = copy.deepcopy(expected)
            altered["page_markers"]["ega:I.7.3.1:page-marker"] = altered["page_markers"].pop("ega:I.7.3.2:page-marker")
            self.assertTrue(check.validate_artifact(altered, language))

    def test_all_contract_leaves_are_fixed_and_strictly_typed(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            for path in leaf_paths(expected):
                old = at_path(expected, path)
                alternatives = (old + 1, float(old), True, None) if type(old) is int else (old + "changed", "", None, [])
                for new in alternatives:
                    altered = copy.deepcopy(expected)
                    at_path(altered, path[:-1])[path[-1]] = new
                    with self.subTest(language=language, path=path, replacement=new):
                        self.assertTrue(check.validate_artifact(altered, language))

    def test_missing_extra_swapped_and_malformed_inventories_fail(self):
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            for key in expected:
                altered = copy.deepcopy(expected)
                del altered[key]
                self.assertTrue(check.validate_artifact(altered, language))
            for key in ("slices", "numbered_environments", "owned_parts", "page_markers"):
                for value in (None, [], {}, {**expected[key], "foreign-owner": {}}):
                    self.assertTrue(check.validate_artifact({**expected, key: value}, language))
                for owner in expected[key]:
                    for value in (None, [], {}, {**expected[key][owner], "foreign-field": 0}):
                        altered = copy.deepcopy(expected)
                        altered[key][owner] = value
                        self.assertTrue(check.validate_artifact(altered, language))
            altered = copy.deepcopy(expected)
            a, b = OWNERS
            altered["owned_parts"][a], altered["owned_parts"][b] = altered["owned_parts"][b], altered["owned_parts"][a]
            self.assertTrue(check.validate_artifact(altered, language))

    def test_artifact_and_contract_do_not_share_mutable_objects(self):
        first = check.expected_contract("fr")
        first["owned_parts"]["ega:I.7.3.3:proof"]["lf_line_end"] = 570
        self.assertEqual(check.expected_contract("fr"), pinned_metadata("fr"))
        result = check.artifact(fixture("fr"), "fr")
        result["slices"].clear()
        self.assertEqual(check.artifact(fixture("fr"), "fr"), independent_metadata(fixture("fr"), "fr"))

    def test_wrapper_only_slices_tail_truncation_and_proof_endpoints_fail(self):
        for language in ("fr", "en"):
            raw, expected = fixture(language), pinned_metadata(language)
            for unit, interval in zip(UNITS, ENVS[language]):
                altered = copy.deepcopy(expected)
                altered["slices"][unit] = span(raw, *interval)
                self.assertTrue(check.validate_artifact(altered, language))
            for owner, (start, end) in zip(OWNERS, PARTS[language]):
                candidates = ((start, end + 1), (start - 1, end))
                if start < end:
                    candidates += ((start + 1, end), (start, end - 1))
                for interval in candidates:
                    altered = copy.deepcopy(expected)
                    altered["owned_parts"][owner] = span(raw, *interval)
                    self.assertTrue(check.validate_artifact(altered, language))
            for unit in ("ega:I.7.3.2", "ega:I.7.3.3"):
                altered = copy.deepcopy(expected)
                original = altered["slices"][unit]
                altered["slices"][unit] = span(raw, original["lf_line_start"], original["lf_line_end"] - 2)
                self.assertTrue(check.validate_artifact(altered, language))

    def test_no_printed_734_proof_owner_or_735_coverage_can_be_added(self):
        for language in ("fr", "en"):
            raw, expected = fixture(language), pinned_metadata(language)
            for key, owner in (("owned_parts", "ega:I.7.3.4:proof"), ("slices", "ega:I.7.3.5")):
                altered = copy.deepcopy(expected)
                altered[key][owner] = span(raw, *NEXT[language])
                self.assertTrue(check.validate_artifact(altered, language))
            for interval in ((NEXT[language][0], NEXT[language][0]), (NEXT[language][0], NEXT[language][1] + 1)):
                altered = copy.deepcopy(expected)
                altered["next_excluded_boundary"] = {"source_unit": "ega:I.7.3.5", **span(raw, *interval)}
                self.assertTrue(check.validate_artifact(altered, language))
            for key in ("combined", "slices"):
                altered = copy.deepcopy(expected)
                if key == "combined":
                    altered[key] = span(raw, FIRST[language], NEXT[language][1])
                else:
                    altered[key]["ega:I.7.3.4"] = span(raw, ENVS[language][-1][0], NEXT[language][1])
                self.assertTrue(check.validate_artifact(altered, language))

    def assert_literal_damage(self, language, old, new, owner):
        raw = fixture(language)
        self.assertIn(old.encode(), raw)
        damaged = raw.replace(old.encode(), new.encode())
        errors = check.verify_structure(damaged, language)
        self.assertIn(owner + ": literal content fingerprint mismatch", errors)
        # Fresh hashes of damaged bytes cannot become a new source authority.
        self.assertTrue(check.verify_source(damaged, language, independent_metadata(damaged, language)))

    def test_substantive_hypotheses_restrictions_formulas_and_crossrefs_after_rehash(self):
        cases = {
            "fr": (
                (r"$\rho_{W,U}=\rho_{W,V}\circ\rho_{V,U}$", r"$\rho_{W,U}=\rho_{V,U}\circ\rho_{W,V}$", UNITS[0]),
                ("préfaisceau formé des $R(U)$.", "préfaisceau formé des $R(X)$.", UNITS[1]),
                (r"$\mathscr{R}(X)|U$ n'est autre que $\mathscr{R}(U)$", r"$\mathscr{R}(X)|U$ n'est pas $\mathscr{R}(U)$", OWNERS[0]),
                ("irréductibles soit localement finie", "irréductibles soit arbitraire", UNITS[2]),
                ("ne rencontrant qu'un nombre fini", "rencontrant un nombre infini", UNITS[2]),
                (r"$U\cap X_\lambda\neq\varnothing$", r"$U\cap X_\lambda=\varnothing$", UNITS[2]),
                ("composé direct des anneaux locaux", "produit tensoriel des anneaux locaux", UNITS[2]),
                ("pour tout couple d'indices", "pour un couple d'indices", OWNERS[1]),
                (r"$\mathscr{O}_{x_i}=R(X_i)$", r"$\mathscr{O}_{x_i}=K(X_i)$", OWNERS[1]),
                (r"\hyperref[I.7.1.7-fr]{7.1.7}", r"\hyperref[I.7.1.3-fr]{7.1.3}", OWNERS[1]),
                ("est somme directe des $A$-modules", "est produit tensoriel des $A$-modules", OWNERS[1]),
                (r"$A_{x_i}$.", r"$A$.", OWNERS[1]),
                ("un préschéma réduit n'ayant qu'un nombre fini", "un préschéma n'ayant qu'un nombre fini", UNITS[3]),
                (r"$(h_i)_*(\mathscr{R}(X_i))$", r"$(h_i)^*(\mathscr{R}(X_i))$", UNITS[3])),
            "en": (
                (r"$\rho_{W,U}=\rho_{W,V}\circ\rho_{V,U}$", r"$\rho_{W,U}=\rho_{V,U}\circ\rho_{W,V}$", UNITS[0]),
                ("presheaf defined by the $R(U)$.", "presheaf defined by the $R(X)$.", UNITS[1]),
                (r"$\sh{R}(X)|U$ is exactly $\sh{R}(U)$", r"$\sh{R}(X)|U$ is not $\sh{R}(U)$", OWNERS[0]),
                ("irreducible components is locally finite", "irreducible components is arbitrary", UNITS[2]),
                ("only finitely many of the components", "infinitely many of the components", UNITS[2]),
                (r"$U\cap X_\lambda\neq\emp$", r"$U\cap X_\lambda=\emp$", UNITS[2]),
                ("direct product of the local rings", "tensor product of the local rings", UNITS[2]),
                ("agree for every pair of indices", "agree for some pair of indices", OWNERS[1]),
                (r"$\sh{O}_{x_i}=R(X_i)$", r"$\sh{O}_{x_i}=K(X_i)$", OWNERS[1]),
                (r"\sref{I.7.1.7}", r"\sref{I.7.1.3}", OWNERS[1]),
                ("direct sum of the $A$-modules", "tensor product of the $A$-modules", OWNERS[1]),
                (r"$A_{x_i}$.", r"$A$.", OWNERS[1]),
                ("a reduced prescheme that has only a finite number", "a prescheme that has only a finite number", UNITS[3]),
                (r"$(h_i)_*(\sh{R}(X_i))$", r"$(h_i)^*(\sh{R}(X_i))$", UNITS[3])),
        }
        for language, entries in cases.items():
            for old, new, owner in entries:
                with self.subTest(language=language, clause=old):
                    self.assert_literal_damage(language, old, new, owner)

    def test_every_substantive_body_line_is_required_not_comment_hidden(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            ranges = [(u, (a + 2, b - 1)) for u, (a, b) in zip(UNITS, ENVS[language])]
            ranges += [(OWNERS[0], PARTS[language][0]), (OWNERS[1],
                       (572, 594) if language == "fr" else (336, 341))]
            for owner, (start, end) in ranges:
                for n in range(start, end + 1):
                    original = split_raw(raw)[n - 1]
                    self.assertTrue(original.strip())
                    for replacement in (b"\n", b"% " + original, b"omitted clause\n"):
                        errors = check.verify_structure(replace_line(raw, n, replacement), language)
                        self.assertIn(owner + ": literal content fingerprint mismatch", errors)

    def test_comment_normalization_never_substitutes_for_exact_bytes(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            n = ENVS[language][0][0] + 2
            line = split_raw(raw)[n - 1]
            damaged = replace_line(raw, n, b" \t" + line[:-1] + b"  % harmless comment\n")
            self.assertEqual(check.verify_structure(damaged, language), [])
            self.assertTrue(check.verify_source(damaged, language, independent_metadata(damaged, language)))

    def test_all_numbered_begin_label_and_close_markers_fail_on_mutation(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            for start, end in ENVS[language]:
                for n in (start, start + 1, end):
                    token = split_raw(raw)[n - 1].rstrip(b"\n")
                    for damaged_line in (b"\n", b"% " + token + b"\n", token + b" " + token + b"\n",
                                         token + b" unowned continuation\n"):
                        errors = check.verify_structure(replace_line(raw, n, damaged_line), language)
                        self.assertTrue(errors)
                        self.assertTrue(any("marker" in e or "wrapper" in e or "label" in e for e in errors))

    def test_missing_misnumbered_nested_foreign_and_unclosed_wrappers_fail(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            for index, (start, end) in enumerate(ENVS[language]):
                env = ENV_NAMES[index].encode()
                body_line = split_raw(raw)[start + 1]
                for token in (b"\\begin{" + env + b"}", b"\\end{" + env + b"}",
                              b"\\begin{foreign}", b"\\end{foreign}", b"\\begin{env}[7.3.99]",
                              b"\\begin{proof}\\end{proof}"):
                    damaged = replace_line(raw, start + 2, token + b" " + body_line)
                    self.assertTrue(any("wrapper" in e for e in check.verify_structure(damaged, language)))
                begin = split_raw(raw)[start - 1]
                damaged = replace_line(raw, start, begin.replace(b"7.3.", b"7.4."))
                self.assertTrue(any("numbered" in e for e in check.verify_structure(damaged, language)))
                damaged = replace_line(raw, end, b"\n")
                self.assertTrue(any("wrapper" in e for e in check.verify_structure(damaged, language)))
                self.assertTrue(check.verify_source(damaged, language))

    def test_global_duplicate_labels_numbered_begins_heading_and_page_fail(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            positions = [FIRST[language], FIRST[language] + 1, PAGE[language], *NEXT[language]]
            positions += [n for start, _ in ENVS[language] for n in (start, start + 1)]
            for n in positions:
                marker = split_raw(raw)[n - 1]
                for added in (marker, b"inline " + marker):
                    self.assertTrue(check.verify_structure(raw + added, language))

    def test_english_proof_wrappers_exact_endpoints_and_unique(self):
        raw = fixture("en")
        for n in (335, 342):
            token = split_raw(raw)[n - 1].rstrip(b"\n")
            for line in (b"\n", b"% " + token + b"\n", token + b" " + token + b"\n"):
                errors = check.verify_structure(replace_line(raw, n, line), "en")
                self.assertTrue(any("wrapper" in e for e in errors))
            for destination in (334, 336, 341, 343):
                lines = split_raw(raw)
                lines[n - 1], lines[destination - 1] = lines[destination - 1], lines[n - 1]
                self.assertTrue(any("wrapper" in e for e in check.verify_structure(b"".join(lines), "en")))

    def test_french_proof_and_both_restriction_tails_remain_unwrapped(self):
        for language, positions in (("fr", (557, 558, 572, 594)), ("en", (327,))):
            raw = fixture(language)
            for n in positions:
                original = split_raw(raw)[n - 1]
                for token in (b"\\begin{proof} ", b"\\end{proof} ", b"\\begin{env}[7.3.99] "):
                    errors = check.verify_structure(replace_line(raw, n, token + original), language)
                    self.assertTrue(any("wrapper" in e for e in errors))

    def test_no_unowned_separator_accepts_new_prose_or_a_734_proof(self):
        blank_lines = {"fr": (530, 548, 556, 559, 571, 595, 605),
                       "en": (312, 320, 326, 328, 334, 343, 349)}
        for language in ("fr", "en"):
            raw = fixture(language)
            for n in blank_lines[language]:
                self.assertEqual(split_raw(raw)[n - 1], b"\n")
                for content in (b"unowned mathematical continuation\n",
                                b"\\begin{proof} fabricated proof \\end{proof}\n"):
                    self.assertTrue(check.verify_structure(replace_line(raw, n, content), language))

    def test_page_and_heading_cannot_move_be_hidden_or_change(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            for n in (FIRST[language], FIRST[language] + 1, PAGE[language], *NEXT[language]):
                line = split_raw(raw)[n - 1]
                for changed in (b"\n", b"% " + line, b"changed " + line):
                    self.assertTrue(check.verify_structure(replace_line(raw, n, changed), language))
                lines = split_raw(raw)
                lines[n - 1], lines[n] = lines[n], lines[n - 1]
                self.assertTrue(check.verify_structure(b"".join(lines), language))
            self.assertTrue(check.verify_structure(raw.replace(b"\\oldpage[I]{162}", b"\\oldpage[I]{161}"), language))

    def test_later_mathematics_excluded_from_structure_but_whole_identity_stays_fixed(self):
        for language in ("fr", "en"):
            raw = fixture(language).replace(b"later mathematics is deliberately outside this review", b"changed later material")
            self.assertEqual(check.verify_structure(raw, language), [])
            self.assertTrue(check.verify_source(raw, language, independent_metadata(raw, language)))

    def test_raw_lf_utf8_context_types_and_size_fail_closed(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            cases = (None, "not bytes", bytearray(raw), b"", raw[:-1], raw.replace(b"\n", b"\r\n"),
                     b"\xff\n", b"x" * (1048576 + 1) + b"\n",
                     b"".join(split_raw(raw)[:NEXT[language][1] - 1]))
            for damaged in cases:
                self.assertTrue(check.verify_source(damaged, language))
            # Physical LF, not str/bytes.splitlines(), defines the line count.
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


class BoundedReplay734Tests(unittest.TestCase):
    def test_cached_route_exact_bound_once_and_no_network(self):
        for language in ("fr", "en"):
            raw = fixture(language)
            cached = MagicMock(spec=Path)
            handle = cached.open.return_value.__enter__.return_value
            handle.read.return_value = raw
            with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
                self.assertEqual(check.read_source(pinned_metadata(language), language, cached), raw)
            cached.open.assert_called_once_with("rb")
            handle.read.assert_called_once_with(LENGTH[language] + 1)

    def test_network_route_pinned_timed_bounded_and_single_attempt(self):
        for language in ("fr", "en"):
            response = MagicMock()
            response.__enter__.return_value.read.return_value = fixture(language)
            with patch.object(check, "urlopen", return_value=response) as fetch:
                self.assertEqual(check.fetch_source(language), fixture(language))
            fetch.assert_called_once_with(URLS[language], timeout=30)
            response.__enter__.return_value.read.assert_called_once_with(LENGTH[language] + 1)

    def test_short_oversized_nonbytes_and_network_failures_never_retry(self):
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

    def test_malformed_contract_or_language_fails_before_any_source_io(self):
        cached = MagicMock(spec=Path)
        for language in ("fr", "en"):
            expected = pinned_metadata(language)
            bad = [None, [], {}, {**expected, "full_bytes": True},
                   {**expected, "full_bytes": 1048577}, {**expected, "url": "https://example.invalid/"},
                   {**expected, "full_sha256": "0" * 64}, {**expected, "combined": {}}]
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
            fetch.assert_not_called()
            cached.open.assert_not_called()

    def test_cli_validates_both_languages_before_reading_either(self):
        receipt = {"languages": {lang: pinned_metadata(lang) for lang in ("fr", "en")}}
        invalid = ["{", "[]", "{}", '{"languages":[]}', '{"languages":{"fr":{}}}']
        for language in ("fr", "en"):
            for key in receipt["languages"][language]:
                altered = copy.deepcopy(receipt)
                altered["languages"][language][key] = None
                invalid.append(json.dumps(altered))
            altered = copy.deepcopy(receipt)
            altered["languages"][language]["owned_parts"]["ega:I.7.3.4:proof"] = {}
            invalid.append(json.dumps(altered))
        invalid += [json.dumps({"languages": {**receipt["languages"], "other": {}}})]
        # Duplicate keys must fail before json.loads can silently discard them.
        valid = json.dumps(receipt)
        invalid += [valid.replace('"full_bytes": 38226', '"full_bytes": 0, "full_bytes": 38226'),
                    valid.replace('"languages":', '"languages": {}, "languages":', 1)]
        for text in invalid:
            with patch.object(Path, "read_text", return_value=text), patch.object(check, "read_source") as read, \
                    patch("sys.stdout", new_callable=io.StringIO) as output:
                self.assertTrue(check.main([]))
                read.assert_not_called()
                self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")

    def test_cli_receipt_missing_and_each_transport_failure_structured(self):
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

    def test_cli_plumbing_and_default_receipt(self):
        # Only CLI plumbing is mocked here; extraction/literal/identity behavior
        # has independent tests above and a separate pinned-source replay.
        receipt = {"languages": {lang: pinned_metadata(lang) for lang in ("fr", "en")}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)) as load, \
                patch.object(check, "read_source", side_effect=lambda expected, language, cached: fixture(language)) as read, \
                patch.object(check, "verify_source", return_value=[]) as verify, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "cached-fr.tex", "--english", "cached-en.tex"]))
            load.assert_called_once_with(encoding="utf-8")
            self.assertEqual(read.call_count, 2)
            self.assertEqual(verify.call_count, 2)
            self.assertEqual(read.call_args_list[0].args[2], Path("cached-fr.tex"))
            self.assertEqual(read.call_args_list[1].args[2], Path("cached-en.tex"))
            result = json.loads(output.getvalue())
            self.assertEqual(result["schema"], "ega-i734-raw-source-boundary-replay/v1")
            self.assertEqual(result["status"], "PASS")
        self.assertEqual(check.RECEIPT.name, "ega-i-7.3.1-7.3.4-semantic-checkpoint-2026-09-08.json")


if __name__ == "__main__":
    unittest.main()
