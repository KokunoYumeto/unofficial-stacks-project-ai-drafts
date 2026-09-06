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
