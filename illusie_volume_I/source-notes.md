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
witness was changed and no external source-correction report was submitted.

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
new local theorem and definition in `relative-homotopy.tex`. The proof keeps
the source's one-based shuffle convention and front/back face order.
