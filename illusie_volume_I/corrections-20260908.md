# Mathematical correction and review record, 2026-09-08

This record supersedes the affected mathematical and coverage claims at commit
`e083b71ac21e0ecb7508aa6a1067a1b0016d89a7`. It does not rewrite the historical
build receipts. No defect below is attributed to Illusie unless explicitly
identified as a printed error.

## Unnormalized Eilenberg--Zilber

The previous integration asserted `AW Sh = 1` on the unnormalized total.
That is false. For the constant bisimplicial group Z in degree one, shuffle
is the row `(1 1)` and AW its transpose; their composite on Z squared is the
all-ones matrix, not identity. The other composite is multiplication by two.
Illusie printed p.7 (physical p.25) correctly asserts inverseness up to
functorial homotopy. The primary pixels were consulted directly.

The replacement specifies shuffle by signed lattice paths and AW by front/back
ordinal inclusions. It proves the chain-map identities by boundary cancellation
and supplies both natural homotopies recursively on free bisimplicial models,
using explicit contractions. Universality of finite integral simplex operators
extends the proof to any additive category. The earlier unspecified exceptional
simplex argument is removed. Associativity/coassociativity are proved by
three-type words and consecutive cuts in a fixed variable order.

Independent mathematical review confirmed the counterexample and recursive
proof construction. Exact-integer free-model regression tests verify both
chain maps and both homotopy equations through degree four. These finite tests
are regression evidence, not a substitute for the universal proof.

## Totalization and normalization

The signed-total definition now explicitly distinguishes chain and cochain
grading and requires any intermediate coproducts used in regrouping to exist.
The Dold--Kan statement now requires nonnegative degree in each chain direction.
The proof uses the explicit Moore projection and comparison through the
degenerate quotient. It does not infer equivalence by an unexplained ordinal
reversal or identify a simplicial diagonal with a chain total.

The source p.11 normal/degenerate shuffle/AW diagram is not proved merely by
iterated normalization. Its two anchors have their own pending decision
`I-1.3-006`. No complete disposition of that diagram is claimed in this increment.

## Source inventory

An obsolete cut at the I.1.1/I.1.2 boundary on printed p.6 survived earlier
section expansions. It excluded the I.1.2 section marker and ten substantive
anchors. The current pp.1-16 span consists of whole pages; the cut is removed.
All 197 anchors occur exactly once in the inventory. This repairs an inventory
defect; anchor counting does not prove semantic completeness.

## I.1.4 additions and review

Existing derived-functor results with exact triangulated/saturated assumptions
do not alone establish Illusie's arbitrary-category right-fraction construction.
The new localization lemma gives a path construction for arbitrary localization,
proves the denominator category cofiltered, and proves the initial roof functor
into the right-Kan comma category. Essentially constant pro-objects then give
the stated universal derived functor. Opposites give the ind-object dual.

The localized Dold--Kan lemma separately proves the fixed nonpositive bound,
not merely boundedness above. Its contractible cylinder forces homotopic maps
to agree under localization. Canonical truncation preserves homotopies and
quasi-isomorphisms, so transports Ore/cancellation diagrams and roof refinements
to the fixed bound. An independent one-pass review checked the variance,
cofilteredness, cylinder signs, and truncation argument; the explicit
cofilteredness argument was added in response. No substantive residual was
identified in those two proofs.

## Printed source correction

`ILLUSIE-I-ERR-001`, p.5, corrects the postcomposition carrier `hg` to `hf`.
The primary print and old witnesses all read `hg`; this is a printed
mathematical error, not a transcription discrepancy. Functoriality gives
`p(wu)=p(w)p(u)=hf`. The corrected-French and English witnesses were edited;
the diplomatic witness and authority bytes remain intact. The separate
`erratum-p005.json` binds the source locus and old/new identities. This is a
high-confidence type correction with no human-dependent review gate.

## Historical identities

At the superseded commit, the relative-homotopy fragment SHA-256 was
`DEEA7F8EDB999E66514598E70039AFC255FC298B5639D72B649B1CBD7F551AE9` and
the composed chapter SHA-256 was
`0674FEC5991A7861F66FECC48EB4C3D222071FC608F2014A25114105EAD04CBB`.
The strict unnormalized identity first appeared in commit
`4eb2eaec67479813553a6c98b32a232d4f7936dd`.
Current identities are recorded in `check.json` and the new QA/build receipts.
