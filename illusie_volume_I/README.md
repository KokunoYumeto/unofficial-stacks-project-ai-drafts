# Illusie Volume I: Stacks-style integration

Independently written statements and proofs from Luc Illusie,
*Complexe cotangent et deformations I*, Lecture Notes in Mathematics 239,
integrated into this maintained, unofficial Stacks-derived repository.
This is written mathematics, not proof-assistant formalization or an official
Stacks Project contribution.

The intended scope is all substantive mathematics of Volume I. The current
inventory covers printed pp.1-16, I.1.1-I.1.4: 197 source anchors, 30 decisions,
and 48 French/English witness files. Inventory coverage is not mathematical
completion. The normal/degenerate comparison diagram on p.11 remains explicitly
pending as `I-1.3-006`; the rest of Volume I remains to be processed.

## Mathematics

[`relative-homotopy.tex`](relative-homotopy.tex) develops relative simplicial
homotopies and strongly cartesian base change, signed multicomplex totals,
explicit shuffle and Alexander--Whitney maps with natural homotopies, and
iterated Dold--Kan normalization. The two unnormalized composites are homotopic
to identity, not generally equal to identity. The homotopies have recursive
finite simplex-operator formulas and an acyclic-model proof.

[`localization.tex`](localization.tex) proves general categorical localization
and the essentially constant pro-object derived-functor construction without
triangulated assumptions. It also proves localized Dold--Kan with the fixed
nonpositive degree bound, including both calculi of fractions on the bounded
homotopy category. Neither result assumes enough injectives or projectives.

Both fragments are composed into [`simplicial.tex`](../simplicial.tex).
[`map.json`](map.json) distinguishes exact existing coverage, new proofs, and
unresolved comparisons. No permanent Stacks tags are assigned to new labels.

## Corrections and evidence

[`corrections-20260908.md`](corrections-20260908.md) documents corrections to
earlier versions of this integration and an omitted source-inventory span.
Historical receipts remain unchanged; successful compilation did not establish
those earlier mathematical claims.

The printed p.5 postcomposition carrier `hg` is corrected to `hf` in the
maintained corrected-French and English LaTeX. The diplomatic transcription and
primary PDF remain unchanged. [`erratum-p005.json`](erratum-p005.json) records
the exact locus, proof, and before/after witness identities.

Primary authority: DOI `10.1007/BFb0059052`, 14,349,904 bytes, SHA-256
`1855B49FE461B13B1CBAEE1341C8FC3E3E0CDDC034C54ABEC1165AF061B90A56`.
Printed page N corresponds to physical PDF page N+18 in this authority.
The maintained edition has its own
[GitHub lineage](https://github.com/KokunoYumeto/illusie-cotangent-complex-editions).
The existing `illusie_r1` and `illusie_r2` additions concern Volume II and do
not count toward Volume I completion.

## Validation and continuation

The source verifier checks identities, complete anchor inventory, exact tag
labels, and composition isolation. It reports pending mathematical decisions
separately. The regression tests check composition isolation and the free-model
shuffle/AW identities and homotopies through degree four; the written proofs,
not finite tests, establish the general assertions.

The targeted chapter build uses a single machine-wide TeX mutex and fixed-point
passes. This sparse build has 67 unchanged external AUX references outside the
addition, and is not a full-book build. New strict diagnostics must be zero.
The current build and visual-inspection receipt records its precise scope.

Next: resolve the p.11 normal/degenerate comparison diagram, then continue at
I.1.5, printed p.17. GitHub preserves coherent increments; the established
Zenodo lineage receives substantial cumulative milestones. Public access is
preserved throughout.
