# Source notes for I.1.1

## I.1.1.6, printed p.5: postcomposition carrier

The primary authority has an `f`-homotopy between arrows over
`f:S -> T` and a postcomposing arrow over `h:T -> T'`, then calls the composite
an `hg`-homotopy. The earlier `g` has domain `S'` and codomain `S`, so `hg`
is not the base map of this composite. Functoriality gives `hf:S -> T'`.

This reading was checked directly on physical PDF p.23, against the authority
SHA-256 recorded in `README.md`. The corrected French and English witnesses
also retain `hg`; they do not provide independent support for that carrier.
The draft uses `hf` and explains the composition in its proof. No source
witness was changed at that historical checkpoint and no external
source-correction report was submitted. On 2026-09-08, the maintained
corrected-French and English LaTeX were corrected to `hf`; the diplomatic
witness remains unchanged. See `erratum-p005.json` for exact old/new hashes.

## I.1.1.6: a common pullback object

The two arrows being compared have the same base map `f`. Their lifted
homotopy is therefore written into one chosen object `f^*Y`. Using two
unidentified choices as the two codomains would not define a homotopy between
parallel arrows. Different choices are related by their unique compatible
isomorphism, and this comparison is included in the proof.

## I.1.1.6: strong cartesianness and coherence

Naturality of the lifted homotopy compares arrows over the structure maps of
the simplicial base, not only arrows in one fibre. The draft explicitly uses
strongly cartesian morphisms in the terminology of Stacks Tag 02XK.
Base change is a pseudofunctor with canonical comparison isomorphisms; strict
equality of successive pullbacks is not assumed.

## I.1.2 source and coverage notes

The primary scan at printed pp.6-8 was checked against the diplomatic,
corrected-French and English witnesses. The source uses commuting differentials
in an $n$-complex, the prefix-sign total differential, and finite-degree sums
for the multisimplicial chain construction. The signed total definition in the
new dossier therefore qualifies existence of the required coproducts; it does
not silently assume infinite coproducts in an arbitrary additive category.

The maintained repository's Tags 012Y, 012Z, 08BI, 0194, 0195, 018Z, 019H,
019I, 08QC and 08QD were checked. Tag 08QC gives a derived-category
Eilenberg-Zilber comparison under cosimplicial-resolution hypotheses, not the
chain-level shuffle and Alexander--Whitney maps, their natural homotopy, or
the strict trisimplicial coherence asserted by Illusie. Those items are the
new local theorem and definition in `relative-homotopy.tex`. The revised proof
specifies ordinal maps explicitly to avoid indexing ambiguity and preserves
front/back face order. Both unnormalized composites are homotopic to identity,
not strictly equal; see `corrections-20260908.md`.

## I.1.3 source and coverage notes

The primary scan and corrected French/English witnesses for printed pp.8-11
(physical pp.26-29) were checked before integration. The normal-complex and
homotopy statements are already represented by Tags 0194, 0195, 019C, 019S,
and 01A4, while Tag 019G supplies the one-variable Dold-Kan equivalence.
The source's genuinely n-variable assertion is not supplied by those tags:
the new local theorem records iterated normalization in each simplicial
variable, canonical comparison of successive orders, and signed-total
compatibility. This is a constructive Stacks-style gap fill, not a silent
repair of the source. No transcription witness was altered.

### I.1.3.5, printed p.11: raw versus normalized Alexander--Whitney

The printed diagram says that both unnormalized Eilenberg--Zilber arrows
restrict to the Moore normal subcomplexes. The raw Alexander--Whitney arrow
does not do so in general. For the free bisimplicial abelian group
`Z[Hom([a],[0]) x Hom([b],[1])]`, the degree-one element
`[(0,0);(0,0)] - [(0,0);(0,1)]` is killed by the positive diagonal face, but
the positive horizontal face of the `(1,0)` Alexander--Whitney component is
`[(0);(0)] - [(0);(1)]`, which is nonzero.

The correct normalized assertion is obtained on the quotient by degenerate
subcomplexes. Under the Moore splitting, shuffle restricts without change,
whereas Alexander--Whitney is followed by the horizontal and vertical Moore
projections. The resulting maps are natural chain-homotopy inverses. This is
proved in `lemma-illusie-I-normalized-eilenberg-zilber`; the diplomatic source
continues to preserve the printed claim.

## I.2.1.1--I.2.1.2, printed pp.20--24

I.2.1.1 is explicitly a review of standard simplicial-set homotopy theory.
The frozen target already contains simplicial homotopies, Kan fibrations, the
Kan property for simplicial groups, and normalized complexes, but not a
standalone theory of general homotopy groups, geometric realization,
barycentric subdivision, or `Ex^infinity`. Reproducing that whole review was
therefore recorded as non-worthwhile background rather than a new
Illusie-specific chapter.

The exact sheaf-level consequence in Proposition 2.1.2.1 is worthwhile and is
proved in `homotopy-sheaves.tex`. The proof uses only the standard operational
description: each degree of `Ex` is a finite limit because the subdivided
simplex is finite; `Ex^infinity` adds a filtered colimit; and the Kan
cycle/homotopy quotient adds finite limits and a coequalizer. Filtered colimits
of sets commute with finite limits, while an inverse-image functor of topoi
preserves all colimits and finite limits.

The diplomatic p.21 carrier has `0 <= i <= n` in the witness condition for
the relation defining homotopy classes; the corrected French and English use
the mathematically required `0 <= i < n`. The p.23 and p.24 corrections are
typographical only (`distingué de Ker` and removal of an extra parenthesis).
The coverage ledger binds all three lane identities and records these source
truth distinctions.

## I.2.2.1--I.2.2.10, printed pp.25--38

The target had the normalized-complex/Dold--Kan and free-abelian-sheaf
ingredients, but no theorem asserting that the free abelian object preserves
an $n$-equivalence. The new `whitehead-free-abelian.tex` supplies the missing
statement in both cases used by Illusie: detection at enough points and a
local finite-type reduction for a morphism of simplicial abelian sheaves.

The point case is the relative Hurewicz theorem applied to the mapping-cylinder
pair. In the additive case, normalization turns the assertion into a bounded
cohomological approximation problem. The proof records both finite-free
extension operations from 2.2.7 and 2.2.8 explicitly: one kills the kernel in
the next cohomological degree without changing its image, and the other makes
the current cohomology map surjective while preserving injectivity in the next
degree. Alternating them proves the cofinal $n$-quasi-isomorphic subsystem of
2.2.9. The varying-ring finite-support argument of 2.2.10 is retained as its
own lemma rather than weakened to the constant-$\mathbf{Z}$ case needed by the
main theorem.

The unmatched-parenthesis repairs on printed p.25, `ci-dessous` to
`ci-dessus` on p.27, and the grammatical repairs on pp.33 and 36 do not change
the mathematical assertions. Remark 2.2.4 is explicitly a historical
conjecture that the theorem's two sufficient hypotheses are unnecessary; it
is recorded as context, not promoted to a theorem or asserted as resolved.

## I.2.3.1, printed pp.38--42

The target already contains the definition and expected degree formula for an
internal Hom of simplicial objects (Tag 017G), the construction of Hom from a
finite simplicial set (Tag 017L), and cartesian closedness for sheaves on a
site (Tag 0BWQ). It did not identify simplicial sheaves with sheaves on a
product site, so those ingredients did not by themselves prove that arbitrary
internal Homs of simplicial sheaves exist. Nor did it record the geometric
morphism induced degreewise or the finite-presentation criterion for inverse
image to preserve internal Hom.

The new `simplicial-topos.tex` fills exactly those residuals. It presents
`Simp(Sh(C))` as sheaves on `C x Delta` for the degreewise topology and uses
Tag 017F for the evaluation formula. The base-change proof constructs the
canonical comparison from evaluation, reduces a constant finite first
argument to the finite-limit construction of Tag 017L, and descends the result
from slice topoi when the first argument is only locally constant. The arrow
category and relative/slice Hom formulas (2.3.1.9--2.3.1.13) remain routine
fiber-product and exponential-law consequences of cartesian closedness; the
right-adjoint limit and algebraic-structure observation is already the general
adjoint fact of Tag 0038. They are classified in the source ledger rather than
repeated as new stand-alone Stacks lemmas.

The p.39 `Quant` carrier is corrected to `Quand`. The diplomatic p.41 witness
has three further printed defects corrected in the maintained French and
English lanes: `Par exemples`, a morphism written `T' -> T'` rather than
`T' -> T`, and a duplicated equation number `(2.3.1.13)` repaired to
`(2.3.1.14)`. These repairs affect grammar, well-typedness, and numbering but
not the intended theorem. The p.42 `d_1 s_1` defect belongs to the following
subsection I.2.3.2 and is not part of this batch.
