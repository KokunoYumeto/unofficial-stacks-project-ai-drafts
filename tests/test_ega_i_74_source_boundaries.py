"""Offline exact owned-excerpt fixtures, never copies of complete sources.

The Chapter I literals were independently read from the source preparation.
Err_III 12 and its disjoint List 2 heading were independently read from the
pinned Chapter III French container. Synthetic surrounding bytes preserve
physical positions only and MUST fail whole-source certification. No fixture
pin or expectation is computed from the checker under test.
"""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from tools import check_ega_i74_source_boundaries as check


VERSIONS = ("fr", "en", "errata_fr")
FRENCH_OWNED = r"""\subsection{Faisceaux de torsion et faisceaux sans torsion.}
\label{subsection:I.7.4-fr}

\begin{env}[7.4.1]
\label{I.7.4.1-fr}
Soit $X$ un préschéma \emph{intègre}. Pour tout $\mathscr{O}_X$-Module
$\mathscr{F}$, l'homomorphisme canonique
$\mathscr{O}_X\to\mathscr{R}(X)$ définit par tensorisation un homomorphisme
(dit encore \emph{canonique})
\[
  \mathscr{F}\to
  \mathscr{F}\otimes_{\mathscr{O}_X}\mathscr{R}(X)
\]
qui, sur chaque fibre, n'est autre que l'homomorphisme $z\to z\otimes 1$ de
$\mathscr{F}_x$ dans
$\mathscr{F}_x\otimes_{\mathscr{O}_x}R(X)$. Le \emph{noyau $\mathscr{T}$}
de cet homomorphisme est un sous-$\mathscr{O}_X$-Module de $\mathscr{F}$,
appelé \emph{faisceau de torsion de $\mathscr{F}$}~; il est quasi-cohérent si
$\mathscr{F}$ est quasi-cohérent
(\hyperref[I.4.1.1-fr]{4.1.1} et \hyperref[I.7.3.6-fr]{7.3.6}). On dit que
$\mathscr{F}$ est \emph{sans torsion} si $\mathscr{T}=0$ et que
$\mathscr{F}$ est un \emph{faisceau de torsion} si
$\mathscr{T}=\mathscr{F}$. Pour tout $\mathscr{O}_X$-Module $\mathscr{F}$,
$\mathscr{F}/\mathscr{T}$ est sans torsion. On déduit de
(\hyperref[I.7.3.5-fr]{7.3.5}) que~:
\end{env}

\begin{proposition}[7.4.2]
\label{I.7.4.2-fr}
Si $X$ est un préschéma intègre, tout $\mathscr{O}_X$-Module quasi-cohérent
sans torsion $\mathscr{F}$ est isomorphe à un sous-faisceau $\mathscr{G}$
d'un faisceau simple de la forme $(\mathscr{R}(X))^{(I)}$, engendré (en tant
que $\mathscr{R}(X)$-Module) par $\mathscr{G}$.
\end{proposition}

Le cardinal de $I$ est appelé le \emph{rang de $\mathscr{F}$}~; pour tout
ouvert affine non vide $U$ de $X$, le rang de $\mathscr{F}$ est égal au rang
de $\Gamma(U,\mathscr{F})$ en tant que $\Gamma(U,\mathscr{O}_X)$-module,
comme on le voit aussitôt en considérant le point générique de $X$, contenu
dans $U$. En particulier~:

\begin{corollary}[7.4.3]
\label{I.7.4.3-fr}
Sur un préschéma intègre $X$, tout $\mathscr{O}_X$-Module quasi-cohérent sans
torsion et de rang $1$ (en particulier tout $\mathscr{O}_X$-Module
inversible) est isomorphe à un sous-$\mathscr{O}_X$-Module de
$\mathscr{R}(X)$, et réciproquement.
\end{corollary}

\begin{corollary}[7.4.4]
\label{I.7.4.4-fr}
Soient $X$ un préschéma intègre, $\mathscr{L}$, $\mathscr{L}'$ deux
$\mathscr{O}_X$-Modules sans torsion, $f$ (resp. $f'$) une section de
$\mathscr{L}$ (resp. $\mathscr{L}'$) au-dessus de $X$. Pour que
$f\otimes f'=0$, il faut et il suffit que l'une des sections $f$, $f'$ soit
nulle.
\end{corollary}

Soit $x$ le point générique de $X$~; on a par hypothèse
$(f\otimes f')_x=f_x\otimes f'_x=0$. Comme $\mathscr{L}_x$ et
$\mathscr{L}'_x$ s'identifient à des sous-$\mathscr{O}_x$-Modules du corps
$\mathscr{O}_x$, la relation précédente entraîne $f_x=0$ ou $f'_x=0$, et par
suite $f=0$ ou $f'=0$ puisque $\mathscr{L}$ et $\mathscr{L}'$ sont sans
torsion (\hyperref[I.7.3.5-fr]{7.3.5}).

\begin{proposition}[7.4.5]
\label{I.7.4.5-fr}
Soient $X$, $Y$ deux préschémas intègres, $f:X\to Y$ un morphisme dominant.
Pour tout $\mathscr{O}_X$-Module quasi-cohérent sans torsion $\mathscr{F}$,
$f_*(\mathscr{F})$ est un $\mathscr{O}_Y$-Module sans torsion.
\end{proposition}

\oldpage[I]{164}
\begin{proof}
Comme $f_*$ est exact à gauche
(\hyperref[0.4.2.1-fr]{0, 4.2.1}), il suffit, en vertu de
(\hyperref[I.7.4.2-fr]{7.4.2}), de prouver la proposition lorsque
$\mathscr{F}=(\mathscr{R}(X))^{(I)}$. Or, tout ouvert non vide $U$ de $Y$
contient le point générique de $Y$, donc $f^{-1}(U)$ contient le point
générique de $X$ (\hyperref[0.2.1.5-fr]{0, 2.1.5}), donc on a alors
\[
  \Gamma(U,f_*(\mathscr{F}))
  =\Gamma(f^{-1}(U),\mathscr{F})=(R(X))^{(I)}~;
\]
autrement dit, $f_*(\mathscr{F})$ est le faisceau simple de fibre
$(R(X))^{(I)}$, considéré comme $\mathscr{R}(Y)$-Module, et il est évidemment
sans torsion.
\end{proof}

\begin{proposition}[7.4.6]
\label{I.7.4.6-fr}
Soient $X$ un préschéma intègre, $x$ son point générique. Pour tout
$\mathscr{O}_X$-Module quasi-cohérent de type fini $\mathscr{F}$, les
conditions suivantes sont équivalentes~: a) $\mathscr{F}$ est un faisceau de
torsion~; b) $\mathscr{F}_x=0$~; c)
$\operatorname{Supp}(\mathscr{F})\neq X$.
\end{proposition}

En vertu de (\hyperref[I.7.3.5-fr]{7.3.5}) et de
(\hyperref[I.7.4.1-fr]{7.4.1}), les relations $\mathscr{F}_x=0$ et
$\mathscr{F}\otimes_{\mathscr{O}_X}\mathscr{R}(X)=0$ sont équivalentes, donc
a) et b) sont équivalentes~; d'autre part,
$\operatorname{Supp}(\mathscr{F})$ est fermé dans $X$
(\hyperref[0.5.2.2-fr]{0, 5.2.2}), et comme tout ouvert non vide de $X$
contient $x$, b) et c) sont équivalentes.

\begin{env}[7.4.7]
\label{I.7.4.7-fr}
On étend (par abus de langage) les définitions de
(\hyperref[I.7.4.1-fr]{7.4.1}) au cas où $X$ est un préschéma
\emph{réduit} n'ayant qu'un nombre \emph{fini} de composantes irréductibles~;
il résulte alors de (\hyperref[I.7.3.4-fr]{7.3.4}) que l'équivalence de a) et
c) dans (\hyperref[I.7.4.6-fr]{7.4.6}) est encore valable pour un tel
préschéma.
\end{env}
"""
ENGLISH_OWNED = r"""\subsection{Torsion sheaves and torsion-free sheaves}
\label{subsection:I.7.4}
\label{I.7.4}

\begin{env}[7.4.1]
\label{I.7.4.1}
Let $X$ be an \emph{integral} prescheme.
For every $\sh{O}_X$-module $\sh{F}$, the canonical homomorphism $\sh{O}_X\to\sh{R}(X)$ defines, by tensoring, a homomorphism (again said to be \emph{canonical}) $\sh{F}\to\sh{F}\otimes_{\sh{O}_X}\sh{R}(X)$, which, on each fibre, is exactly the homomorphism $z\to z\otimes1$ from $\sh{F}_x$ to $\sh{F}_x\otimes_{\sh{O}_x}R(X)$.
The \emph{kernel $\sh{T}$} of this homomorphism is an $\sh{O}_X$-submodule of $\sh{F}$, called the \emph{torsion sheaf} of $\sh{F}$; it is quasi-coherent if $\sh{F}$ is quasi-coherent (\sref{I.4.1.1} and \sref{I.7.3.6}).
We say that $\sh{F}$ is \emph{torsion free} if $\sh{T}=0$, and that $\sh{F}$ is a \emph{torsion sheaf} if $\sh{T}=\sh{F}$.
For every $\sh{O}_X$-module $\sh{F}$, $\sh{F}/\sh{T}$ is torsion free.
We deduce from \sref{I.7.3.5} that:
\end{env}

\begin{proposition}[7.4.2]
\label{I.7.4.2}
If $X$ is an integral prescheme, then every torsion-free quasi-coherent $\sh{O}_X$-module $\sh{F}$ is isomorphic to a subsheaf $\sh{G}$ of a simple sheaf of the form $(\sh{R}(X))^{(I)}$, generated (as a $\sh{R}(X)$-module) by $\sh{G}$.
\end{proposition}

The cardinality of $I$ is called the \emph{rank} of $\sh{F}$; for every nonempty affine open subset $U$ of $X$, the rank of $\sh{F}$ is equal to the rank of $\Gamma(U,\sh{F})$ as a $\Gamma(U,\sh{O}_X)$-module, as we see by considering the generic point of $X$, contained in $U$.
In particular:
\begin{corollary}[7.4.3]
\label{I.7.4.3}
On an integral prescheme $X$, every torsion-free quasi-coherent $\sh{O}_X$-module of rank $1$ (in particular, every invertible $\sh{O}_X$-module) is isomorphic to an $\sh{O}_X$-submodule of $\sh{R}(X)$, and vice versa.
\end{corollary}

\begin{corollary}[7.4.4]
\label{I.7.4.4}
Let $X$ be an integral prescheme, $\sh{L}$ and $\sh{L}'$ torsion-free $\sh{O}_X$-modules, and $f$ (resp. $f'$) a section of $\sh{L}$ (resp. $\sh{L}'$) over $X$.
In order to have $f\otimes f'=0$, it is necessary and sufficient for one of the sections $f$ and $f'$ to be zero.
\end{corollary}

\begin{proof}
Let $x$ be the generic point of $X$; we have, by hypothesis, that $(f\otimes f')_x=f_x\otimes f'_x=0$.
Since $\sh{L}_x$ and $\sh{L}'_x$ can be identified with $\sh{O}_x$-submodules of the field $\sh{O}_x$, the above equation leads to $f_x=0$ or $f'_x=0$, and thus $f=0$ or $f'=0$, since $\sh{L}$ and $\sh{L}'$ are torsion free \sref{I.7.3.5}.
\end{proof}

\begin{proposition}[7.4.5]
\label{I.7.4.5}
Let $X$ and $Y$ be integral preschemes, and $f:X\to Y$ a dominant morphism.
For every torsion-free quasi-coherent $\sh{O}_X$-module $\sh{F}$, $f_*(\sh{F})$ is a torsion-free $\sh{O}_Y$-module.
\end{proposition}

\oldpage[I]{164}
\begin{proof}
Since
$f_*$ is left exact \sref[0]{0.4.2.1}, it suffices, by \sref{I.7.4.2}, to prove the proposition in the case where $\sh{F}=(\sh{R}(X))^{(I)}$.
But every nonempty open subset $U$ of $Y$ contains the generic point of $Y$, so $f^{-1}(U)$ contains the generic point of $X$ \sref[0]{0.2.1.5}, so we have that $\Gamma(U,f_*(\sh{F}))=\Gamma(f^{-1}(U),\sh{F})=(R(X))^{(I)}$; in other words, $f_*(\sh{F})$ is the simple sheaf with fibre $(R(X))^{(I)}$, considered as a $\sh{R}(Y)$-module, and it is clearly torsion free.
\end{proof}

\begin{proposition}[7.4.6]
\label{I.7.4.6}
Let $X$ be an integral prescheme, and $x$ its generic point.
For every quasi-coherent $\sh{O}_X$-module $\sh{F}$ of finite type, the following conditions are equivalent: \emph{(a)} $\sh{F}$ is a torsion sheaf; \emph{(b)} $\sh{F}_x=0$; \emph{(c)} $\Supp(\sh{F})\neq X$.
\end{proposition}

\begin{proof}
By \sref{I.7.3.5} and \sref{I.7.4.1}, the equations $\sh{F}_x=0$ and $\sh{F}\otimes_{\sh{O}_X}\sh{R}(X)=0$ are equivalent, so (a) and (b) are equivalent; then $\Supp(\sh{F})$ is closed in $X$ \sref[0]{0.5.2.2}, and since every nonempty open subset of $X$ contains $x$, (b) and (c) are equivalent.
\end{proof}

\begin{env}[7.4.7]
\label{I.7.4.7}
We generalise (by an abuse of language) the definitions of \sref{I.7.4.1} to the case where $X$ is a \emph{reduced} prescheme having only a \emph{finite} number of irreducible components; it then follows from \sref{I.7.3.4} that the equivalence between \emph{a)} and \emph{c)} in \sref{I.7.4.6} still holds true for such a prescheme.
\end{env}
"""
ERRATA_OWNED = r"""\noindent\textbf{$(\mathbf{Err}_{\mathrm{III}},\,12)$} Remplacer (I, 7.4.7)
par : On étend (par abus de langage) les définitions de (7.4.1) au cas où
$X$ est un préschéma \emph{réduit} dont tout point admet un voisinage ouvert
n'ayant qu'un nombre \emph{fini} de composantes irréductibles ; il résulte
alors de (7.3.4) et (7.4.6) que, pour un $\mathscr O_X$-Module quasi-cohérent de
type fini $\mathscr F$, dire que $\mathscr F$ est un \emph{faisceau de torsion}
équivaut à dire que $\operatorname{Supp}(\mathscr F)$ \emph{ne contient aucune
composante irréductible de $X$}.

"""
ERRATA_LIST_HEADING = r"""\oldpage[III]{217}
\section*{ERRATA ET ADDENDA}
\begin{center}
(Liste 2)

\medskip
A) \emph{Erreurs typographiques}
\end{center}
"""
ERRATA_EXCLUDED_NEXT = r"""\noindent\textbf{$(\mathbf{Err}_{\mathrm{III}},\,13)$} Dans (I, 10.11.7),
"""

URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
    "errata_fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-7-fr.tex",
}
LENGTH = {"fr": 38226, "en": 35788, "errata_fr": 172424}
LINE_COUNT = {"fr": 786, "en": 466, "errata_fr": 4479}
PINNED_SHA = {
    "fr": "73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522",
    "en": "B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC",
    "errata_fr": "20A61BA348909E4309A3CDA89FD6DDAF8C0FC5BA346FD44232458CDFEA2A2972",
}
RANGES = {
    "fr": {
        "owned": (672, 786),
        "heading": (672, 674),
        "ega:I.7.4.1": (675, 698),
        "ega:I.7.4.2": (699, 712),
        "ega:I.7.4.3": (713, 720),
        "ega:I.7.4.4": (721, 736),
        "ega:I.7.4.5": (737, 760),
        "ega:I.7.4.6": (761, 777),
        "ega:I.7.4.7": (778, 786),
        "rank-tail": (707, 711),
        "744-proof": (730, 735),
        "745-page-marker": (744, 744),
        "745-proof": (745, 759),
        "746-proof": (770, 776),
    },
    "en": {
        "owned": (403, 466),
        "heading": (403, 406),
        "ega:I.7.4.1": (407, 416),
        "ega:I.7.4.2": (417, 423),
        "ega:I.7.4.3": (424, 428),
        "ega:I.7.4.4": (429, 439),
        "ega:I.7.4.5": (440, 452),
        "ega:I.7.4.6": (453, 462),
        "ega:I.7.4.7": (463, 466),
        "rank-tail": (422, 423),
        "744-proof": (435, 438),
        "745-page-marker": (446, 446),
        "745-proof": (447, 451),
        "746-proof": (459, 461),
    },
    "errata_fr": {
        "list_heading": (3981, 3988),
        "owned": (4268, 4276),
        "heading": (4268, 4268),
        "replacement_body": (4269, 4275),
        "inference": (4271, 4275),
        "excluded_next": (4277, 4277),
    },
}

PROOF_FORMS = {
    "fr": {"744": "unwrapped", "745": "wrapped", "746": "unwrapped"},
    "en": {"744": "wrapped", "745": "wrapped", "746": "wrapped"},
    "errata_fr": {"replacement": "inference_in_prose_no_separate_proof"},
}
ANCHORS = {
    "fr": ((672, 33215, FRENCH_OWNED),),
    "en": ((403, 31406, ENGLISH_OWNED),),
    "errata_fr": ((3981, 147450, ERRATA_LIST_HEADING),
                  (4268, 160179, ERRATA_OWNED + ERRATA_EXCLUDED_NEXT)),
}


def split_raw(raw):
    return [piece + b"\n" for piece in raw.split(b"\n")[:-1]]


def padding(byte_count, line_count):
    if not byte_count and not line_count:
        return b""
    tag = b"% SYNTHETIC NON-AUTHORITY SURROUNDING BYTES "
    assert byte_count >= len(tag) + line_count and line_count > 0
    return tag + b"x" * (byte_count - len(tag) - line_count) + b"\n" * line_count


def fixture(version):
    raw = b""
    for first, offset, text in ANCHORS[version]:
        raw += padding(offset - len(raw), first - 1 - len(split_raw(raw)))
        raw += text.encode("utf-8")
    raw += padding(LENGTH[version] - len(raw), LINE_COUNT[version] - len(split_raw(raw)))
    assert len(raw) == LENGTH[version]
    assert len(split_raw(raw)) == LINE_COUNT[version]
    return raw


def span(raw, first, last):
    lines = split_raw(raw)
    block = b"".join(lines[first - 1:last])
    offset = len(b"".join(lines[:first - 1]))
    return {"lf_line_start": first, "lf_line_end": last, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(), "byte_offset_start": offset,
            "byte_offset_end_exclusive": offset + len(block)}


def independent_metadata(raw, version):
    """No checker tables, extraction, metadata or expected-contract calls."""
    return {"url": URLS[version], "full_bytes": len(raw),
            "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
            "full_lf_lines": len(split_raw(raw)), "proof_forms": dict(PROOF_FORMS[version]),
            "end_boundary": "excluded_next" if version == "errata_fr" else "EOF",
            "spans": {key: span(raw, *bounds) for key, bounds in RANGES[version].items()}}


def pinned_metadata(version):
    result = independent_metadata(fixture(version), version)
    result["full_sha256"] = PINNED_SHA[version]
    return result


def replace_line(raw, number, content):
    lines = split_raw(raw)
    lines[number - 1] = content
    return b"".join(lines)


def leaf_paths(value, prefix=()):
    for key, child in value.items():
        if isinstance(child, dict):
            yield from leaf_paths(child, (*prefix, key))
        else:
            yield (*prefix, key)


def at_path(value, path):
    for key in path:
        value = value[key]
    return value


class SourceBoundary74Tests(unittest.TestCase):
    def test_independent_literals_all_units_proofs_rank_and_erratum_metadata(self):
        for version in VERSIONS:
            raw = fixture(version)
            self.assertEqual(check.expected_contract(version), pinned_metadata(version), version)
            self.assertEqual(check.validate_artifact(pinned_metadata(version), version), [])
            self.assertEqual(check.artifact(raw, version), independent_metadata(raw, version))
            self.assertEqual(check.verify_structure(raw, version), [])
        self.assertEqual([pinned_metadata(v)["spans"]["owned"]["bytes"] for v in VERSIONS],
                         [5011, 4382, 588])
        self.assertEqual(check.LANGUAGES, VERSIONS)

    def test_synthetic_full_sources_and_coordinated_self_rehash_always_fail(self):
        for version in VERSIONS:
            raw = fixture(version)
            self.assertEqual(check.verify_source(raw, version),
                             [version + ".source.full_sha256: pinned identity/boundary mismatch"])
            self.assertTrue(check.validate_artifact(independent_metadata(raw, version), version))
            self.assertTrue(check.verify_source(raw, version, independent_metadata(raw, version)))

    def test_all_six_source_version_swaps_are_rejected(self):
        for version in VERSIONS:
            for other in set(VERSIONS) - {version}:
                self.assertTrue(check.validate_artifact(pinned_metadata(other), version))
                self.assertTrue(check.verify_source(fixture(other), version, pinned_metadata(version)))

    def test_all_seven_units_partition_owned_and_retain_complete_tails(self):
        for version in ("fr", "en"):
            parts = pinned_metadata(version)["spans"]
            keys = ["heading"] + ["ega:I.7.4." + str(n) for n in range(1, 8)]
            self.assertEqual(parts[keys[0]]["byte_offset_start"], parts["owned"]["byte_offset_start"])
            for previous, following in zip(keys, keys[1:]):
                self.assertEqual(parts[previous]["byte_offset_end_exclusive"],
                                 parts[following]["byte_offset_start"])
            self.assertEqual(parts[keys[-1]]["byte_offset_end_exclusive"], LENGTH[version])
            self.assertEqual(parts[keys[-1]]["lf_line_end"], LINE_COUNT[version])
            self.assertEqual(sum(parts[key]["bytes"] for key in keys), parts["owned"]["bytes"])
            for tail, unit in (("rank-tail", "2"), ("744-proof", "4"), ("745-page-marker", "5"),
                               ("745-proof", "5"), ("746-proof", "6")):
                unit_span = parts["ega:I.7.4." + unit]
                self.assertLessEqual(unit_span["byte_offset_start"], parts[tail]["byte_offset_start"])
                self.assertLessEqual(parts[tail]["byte_offset_end_exclusive"],
                                     unit_span["byte_offset_end_exclusive"])
                altered = pinned_metadata(version)
                del altered["spans"][tail]
                self.assertTrue(check.validate_artifact(altered, version))
            self.assertEqual(parts["745-page-marker"]["byte_offset_end_exclusive"],
                             parts["745-proof"]["byte_offset_start"])

    def test_erratum_is_distinct_full_replacement_with_disjoint_next_boundary(self):
        version = "errata_fr"
        parts = pinned_metadata(version)["spans"]
        self.assertEqual(parts["heading"]["byte_offset_start"], parts["owned"]["byte_offset_start"])
        self.assertEqual(parts["heading"]["byte_offset_end_exclusive"],
                         parts["replacement_body"]["byte_offset_start"])
        self.assertEqual(parts["replacement_body"]["byte_offset_end_exclusive"] + 1,
                         parts["owned"]["byte_offset_end_exclusive"])
        self.assertEqual(parts["owned"]["byte_offset_end_exclusive"],
                         parts["excluded_next"]["byte_offset_start"])
        self.assertLess(parts["list_heading"]["byte_offset_end_exclusive"],
                        parts["owned"]["byte_offset_start"])
        self.assertEqual(parts["inference"]["byte_offset_end_exclusive"],
                         parts["replacement_body"]["byte_offset_end_exclusive"])
        self.assertNotIn("proof", parts)  # No invented standalone proof in this source.
        self.assertIn("Remplacer (I, 7.4.7)", ERRATA_OWNED)
        self.assertIn("dont tout point admet un voisinage ouvert", ERRATA_OWNED)
        self.assertIn("ne contient aucune\ncomposante", ERRATA_OWNED)
        self.assertNotIn("13)", ERRATA_OWNED)
        self.assertIn("13)", ERRATA_EXCLUDED_NEXT)
        altered = pinned_metadata(version)
        altered["spans"]["owned"] = span(fixture(version), 4268, 4277)
        self.assertTrue(check.validate_artifact(altered, version))

    def test_every_metadata_leaf_type_and_inventory_fails_closed(self):
        for version in VERSIONS:
            expected = pinned_metadata(version)
            for path in leaf_paths(expected):
                old = at_path(expected, path)
                values = (old + 1, float(old), True, None) if type(old) is int else (old + "changed", "", None, [])
                for new in values:
                    altered = copy.deepcopy(expected)
                    at_path(altered, path[:-1])[path[-1]] = new
                    self.assertTrue(check.validate_artifact(altered, version), (version, path, new))
            for key in expected:
                altered = copy.deepcopy(expected)
                del altered[key]
                self.assertTrue(check.validate_artifact(altered, version))
            for key in expected["spans"]:
                altered = copy.deepcopy(expected)
                altered["spans"]["unreviewed"] = altered["spans"].pop(key)
                self.assertTrue(check.validate_artifact(altered, version))
                altered = copy.deepcopy(expected)
                altered["spans"][key]["extra"] = 1
                self.assertTrue(check.validate_artifact(altered, version))
            for bad in (None, [], {}, True, "not metadata"):
                self.assertTrue(check.validate_artifact(bad, version))
            changed = check.expected_contract(version)
            changed["spans"]["owned"]["bytes"] = 0
            changed["proof_forms"].clear()
            self.assertEqual(check.expected_contract(version), expected)

    def test_every_owned_and_excluded_line_is_required_without_normalization(self):
        for version in VERSIONS:
            raw = fixture(version)
            scoped = sorted({n for first, last in RANGES[version].values()
                             for n in range(first, last + 1)})
            for n in scoped:
                line = split_raw(raw)[n - 1]
                replacements = (b"omitted clause\n",) if line == b"\n" else (b"\n", b"% " + line, b" \t" + line)
                for replacement in replacements:
                    damaged = replace_line(raw, n, replacement)
                    self.assertTrue(check.verify_structure(damaged, version), (version, n))
                    self.assertTrue(check.verify_source(damaged, version, independent_metadata(damaged, version)))

    def test_removed_rank_tail_each_proof_page_and_erratum_component_are_named(self):
        for version in VERSIONS:
            keys = ("rank-tail", "744-proof", "745-page-marker", "745-proof", "746-proof") \
                if version != "errata_fr" else ("heading", "replacement_body", "inference", "excluded_next", "list_heading")
            for key in keys:
                raw = fixture(version)
                lines = split_raw(raw)
                first, last = RANGES[version][key]
                for n in range(first, last + 1):
                    lines[n - 1] = b"\n"
                damaged = b"".join(lines)
                self.assertIn(key + ": exact literal source span mismatch",
                              check.verify_structure(damaged, version))
                self.assertTrue(check.verify_source(damaged, version, independent_metadata(damaged, version)))

    def test_wrapped_unwrapped_and_foreign_nesting_cannot_be_swapped(self):
        for version in ("fr", "en"):
            raw = fixture(version)
            for key in ("744-proof", "745-proof", "746-proof"):
                first, last = RANGES[version][key]
                for n in (first, last):
                    line = split_raw(raw)[n - 1]
                    for token in (b"\\begin{proof} ", b"\\end{proof} ", b"\\begin{foreign} "):
                        errors = check.verify_structure(replace_line(raw, n, token + line), version)
                        self.assertTrue(any("wrapper" in error for error in errors), (version, key, n))
            for key in ("744-proof", "745-proof", "746-proof"):
                if PROOF_FORMS[version][key[:3]] == "wrapped":
                    for n in RANGES[version][key]:
                        errors = check.verify_structure(replace_line(raw, n, b"\n"), version)
                        self.assertTrue(any("wrapper" in error for error in errors))
        raw = fixture("errata_fr")
        for n in (4269, 4275):
            damaged = replace_line(raw, n, b"\\begin{proof}\n")
            self.assertTrue(any("wrapper" in error for error in check.verify_structure(damaged, "errata_fr")))

    def test_non_ascii_environment_tokens_return_structured_failures(self):
        for version, position in (("fr", 675), ("en", 407), ("errata_fr", 3983)):
            raw = fixture(version)
            damaged = replace_line(raw, position, "\\begin{é}[7.4.1]\n".encode("utf-8"))
            for errors in (check.verify_structure(damaged, version),
                           check.verify_source(damaged, version)):
                self.assertTrue(any("wrapper inventory" in error for error in errors), version)

    def test_global_marker_uniqueness_not_only_owned_position(self):
        marker_lines = {"fr": (673, 675, 676, 699, 700, 713, 714, 721, 722, 737, 738, 744, 761, 762, 778, 779),
                        "en": (404, 405, 407, 408, 417, 418, 424, 425, 429, 430, 440, 441, 446, 453, 454, 463, 464),
                        "errata_fr": (3981, 3982, 4268, 4277)}
        for version in VERSIONS:
            raw = fixture(version)
            for n in marker_lines[version]:
                marker = split_raw(raw)[n - 1]
                errors = check.verify_structure(replace_line(raw, 2, marker), version)
                self.assertTrue(any("globally unique" in error for error in errors), (version, n))
                self.assertEqual(check.verify_structure(replace_line(raw, 2, b"% " + marker), version), [])

    def test_exact_eof_and_excluded_next_omissions(self):
        for version in ("fr", "en"):
            raw = fixture(version)
            for damage in (b"\n", b"unreviewed next section\n", b"% comment still changes EOF\n"):
                self.assertTrue(any("EOF boundary" in error for error in check.verify_structure(raw + damage, version)))
                self.assertTrue(check.verify_source(raw + damage, version, independent_metadata(raw + damage, version)))
            last = LINE_COUNT[version]
            self.assertTrue(check.verify_structure(b"".join(split_raw(raw)[:last - 1]), version))
        raw = fixture("errata_fr")
        self.assertTrue(check.verify_structure(b"".join(split_raw(raw)[:4276]), "errata_fr"))
        self.assertTrue(check.verify_structure(replace_line(raw, 4277, b"\n"), "errata_fr"))
        # Later unowned prose is not re-owned, but still affects whole identity.
        later = replace_line(raw, 4400, b"unreviewed later mathematics\n")
        self.assertEqual(check.verify_structure(later, "errata_fr"), [])
        self.assertTrue(check.verify_source(later, "errata_fr", independent_metadata(later, "errata_fr")))

    def test_raw_lf_utf8_size_version_and_span_fail_closed(self):
        for version in VERSIONS:
            raw = fixture(version)
            for damaged in (None, "not bytes", bytearray(raw), b"", raw[:-1],
                            raw.replace(b"\n", b"\r\n"), b"\xff\n", b"\xef\xbb\xbf" + raw,
                            b"x" * 1048577 + b"\n"):
                self.assertTrue(check.verify_source(damaged, version))
            unusual = raw.replace(b"SYNTHETIC", b"SYNTHETIC\x0c\xe2\x80\xa8", 1)
            self.assertEqual(len(check.raw_lines(unusual)), LINE_COUNT[version])
            self.assertEqual(check.verify_structure(unusual, version), [])
        for version in ("old_fr", "wrong", None, [], True):
            self.assertTrue(check.validate_artifact({}, version))
            self.assertTrue(check.verify_source(b"x\n", version))
            with self.assertRaises(ValueError):
                check.artifact(b"x\n", version)
        for first, last in ((0, 1), (1, 3), (2, 1), (True, 1), (1, 2.0), ("1", 2)):
            with self.assertRaises(ValueError):
                check.raw_span([b"a\n", b"bc\n"], first, last)
        self.assertEqual(check.raw_span([b"a\n", b"bc\n"], 2, 2), span(b"a\nbc\n", 2, 2))


class BoundedReplay74Tests(unittest.TestCase):
    def test_cached_and_network_one_bounded_read_per_source(self):
        for version in VERSIONS:
            cached = MagicMock(spec=Path)
            cached.open.return_value.__enter__.return_value.read.return_value = fixture(version)
            with patch.object(check, "urlopen", side_effect=AssertionError("network forbidden")):
                self.assertEqual(check.read_source(pinned_metadata(version), version, cached), fixture(version))
            cached.open.assert_called_once_with("rb")
            cached.open.return_value.__enter__.return_value.read.assert_called_once_with(LENGTH[version] + 1)
            response = MagicMock()
            response.__enter__.return_value.read.return_value = fixture(version)
            with patch.object(check, "urlopen", return_value=response) as fetch:
                self.assertEqual(check.fetch_source(version), fixture(version))
            fetch.assert_called_once_with(URLS[version], timeout=30)
            response.__enter__.return_value.read.assert_called_once_with(LENGTH[version] + 1)

    def test_short_oversized_nonbytes_transport_failure_no_retry(self):
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

    def test_bad_contract_or_size_causes_no_source_io(self):
        cached = MagicMock(spec=Path)
        with patch.object(check, "urlopen") as fetch:
            for version in VERSIONS:
                expected = pinned_metadata(version)
                bad = [None, [], {}, {**expected, "full_bytes": True},
                       {**expected, "full_bytes": 1048577}, {**expected, "spans": {}},
                       {**expected, "url": "https://example.invalid/"}]
                bad += [pinned_metadata(other) for other in set(VERSIONS) - {version}]
                for receipt in bad:
                    for cache in (None, cached):
                        with self.assertRaises(ValueError):
                            check.read_source(receipt, version, cache)
            for version in ("wrong", None, []):
                with self.assertRaises(ValueError):
                    check.fetch_source(version, cached)
            for size in (True, 0, 1048576, 1048577):
                with patch.dict(check.SOURCE_IDENTITIES, {"en": (size, PINNED_SHA["en"], LINE_COUNT["en"])}):
                    with self.assertRaises(ValueError):
                        check.fetch_source("en", cached)
            fetch.assert_not_called()
            cached.open.assert_not_called()

    def test_cli_prevalidates_all_contracts_and_duplicate_keys_before_reads(self):
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        invalid = ["{", "[]", "{}", '{"languages":[]}', '{"languages":{"fr":{}}}']
        for version in VERSIONS:
            for key in receipt["languages"][version]:
                altered = copy.deepcopy(receipt)
                altered["languages"][version][key] = "invalid"
                invalid.append(json.dumps(altered))
            for other in set(VERSIONS) - {version}:
                altered = copy.deepcopy(receipt)
                altered["languages"][version] = pinned_metadata(other)
                invalid.append(json.dumps(altered))
        invalid.append(json.dumps({"languages": {**receipt["languages"], "unreviewed": {}}}))
        valid = json.dumps(receipt)
        invalid += [valid.replace('"full_bytes": 38226', '"full_bytes": 0, "full_bytes": 38226'),
                    valid.replace('"languages":', '"languages": {}, "languages":', 1)]
        for text in invalid:
            with patch.object(Path, "read_text", return_value=text), patch.object(check, "read_source") as read, \
                    patch("sys.stdout", new_callable=io.StringIO) as output:
                self.assertTrue(check.main([]))
                read.assert_not_called()
                self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")

    def test_cli_missing_receipt_and_three_transport_failures_are_structured(self):
        with patch.object(Path, "read_text", side_effect=FileNotFoundError("absent")), \
                patch.object(check, "read_source") as read, patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            read.assert_not_called()
            self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=OSError("bounded failure")) as read, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            self.assertEqual(read.call_count, 3)
            self.assertEqual(len(json.loads(output.getvalue())["errors"]), 3)

    def test_cli_transport_success_is_not_whole_source_certification(self):
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)), \
                patch.object(check, "read_source", side_effect=lambda expected, version, cached: fixture(version)), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertTrue(check.main([]))
            result = json.loads(output.getvalue())
            self.assertEqual(set(result["sources"]), set(VERSIONS))
            self.assertTrue(all(source["status"] == "FAIL" for source in result["sources"].values()))
            self.assertEqual(len(result["errors"]), 3)

    def test_cli_passing_plumbing_uses_each_cache_without_writes(self):
        receipt = {"languages": {version: pinned_metadata(version) for version in VERSIONS}}
        with patch.object(Path, "read_text", return_value=json.dumps(receipt)) as load, \
                patch.object(check, "read_source", side_effect=lambda expected, version, cached: fixture(version)) as read, \
                patch.object(check, "verify_source", return_value=[]) as verify, \
                patch.object(Path, "write_text") as write_text, patch.object(Path, "write_bytes") as write_bytes, \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertFalse(check.main(["--french", "fr.tex", "--english", "en.tex",
                                         "--errata-french", "errata-fr.tex"]))
            load.assert_called_once_with(encoding="utf-8")
            self.assertEqual(read.call_count, 3)
            self.assertEqual(verify.call_count, 3)
            self.assertEqual([call.args[2] for call in read.call_args_list],
                             [Path("fr.tex"), Path("en.tex"), Path("errata-fr.tex")])
            write_text.assert_not_called()
            write_bytes.assert_not_called()
            result = json.loads(output.getvalue())
            self.assertEqual(result["schema"], "ega-i74-raw-source-boundary-replay/v1")
            self.assertEqual(result["status"], "PASS")
        self.assertEqual(check.RECEIPT.name, "ega-i-7.4.1-7.4.7-semantic-checkpoint-2026-09-08.json")


if __name__ == "__main__":
    unittest.main()
