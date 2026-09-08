# Review of the local extension criterion

This record concerns only EGA I 7.2.8–7.2.9, including the nested Lemma
7.2.8.1 and the parent construction following its proof. It accompanies the
[complete derivation](i729.md) and its
[immutable source/target checkpoint](../validation/ega-i-7.2.8-7.2.9-semantic-checkpoint-2026-09-08.json).
It is not a formal proof certificate or a completion claim for EGA.

## Mathematical review and decisions

The complete prepared manuscript received independent review against freshly
read French and English passages and eighteen official Stacks blocks. The
relative proof and the independently derived counterexample were also checked
separately during preflight. A later implementation reviewer reread the entire
manuscript and all eighteen official target blocks and found no remaining
mathematical defect.

The review required one attribution correction: Tag 01TT gives **local** finite
presentation. The target open immersion is separated; quasi-compactness and
quasi-separatedness then imply finite presentation. The manuscript records
those steps separately. The initial manuscript was 15,442 bytes with SHA-256
`B144676526E7FA4A9F7D28458DCF7C3FD95A8194F8D4DDA9FE9B63CEE57B9120`.
The final source-bound manuscript is 15,631 bytes with SHA-256
`CF028E092E8AE86FD52B43125771819F8F8FD4011E97109D44FBDF9C0FB9AAC7`.

| Decision | Evidence and rationale | Rejected alternative / uncertainty |
|---|---|---|
| D000362: local scheme and induced rational class | Canonical generalizations, dense pullbacks, and independence on a dense agreement open; parent prose is separately owned. | Do not treat the local scheme as an open neighbourhood or invent a sixth discovery unit. |
| D000363: component and density lemma | Minimal-prime correspondence, global component traces, iterated local rings, and finite-component density are all proved. | Coordinate rings need not be Noetherian: only the underlying space has the source's local Noetherian hypothesis. |
| D000364: relative extension criterion | A local map over S spreads using 01TX and 0BX6; both source alternatives and the final disjoint-open globalization are retained. | An ordinary local morphism is insufficient. The explicit DVR counterexample verifies this, including the two distinct closed base points. |

Editorial confidence is high for the relative theorem and the adverse
construction because every hypothesis-bearing step is explicit and has been
independently reconstructed. This is an editorial assessment, not a calibrated
probability. The stronger 0BX6(2b,c) route remains separate from the historical
hypotheses; 0BX8 is comparison evidence only, and 00PB supplies only the DVR seed,
not the whole counterexample.

The French/English Chapter 0 cross-reference mismatch remains a literal
discrepancy, not an admitted correction to a printed edition. No source text,
official tag, root theorem, or earlier open gap is changed. All twelve earlier
open gaps remain exact. Later expert observations may support reversible
improvements, but human review is not a prerequisite for this candidate.

## Deterministic review

The source audit found five missing independent literal relationships in the
prepared boundary helper: the nested density condition, the full minimal-prime
correspondence, the integral branch's rational-map identity and definedness,
and the final extension step. Added bilingual deletion/negation tests reject
each omission even after fixture metadata is rehashed. All original 44 tests
remain, and the resulting 49-test source suite and pinned-byte replay pass.

The implementation audit additionally found that a supplied discovery
dictionary could contain an invented parent proof beside the five correct
rows. The checker now compares the whole supplied discovery dictionary with
the exact CSV byte view; a regression rejects both invented parent-proof and
induced-prose discovery IDs. This does not alter the discovery CSV.

The offline semantic checker seals the reviewed metadata and independently
reads actual ledger, dossier, preserved-input and official/current target
bytes. It does not mistake copied metadata for byte evidence. Historical
7.2.5–7.2.7 postimages are checked as immutable prefixes, using their original
snapshots and prefix-local supersession view. Current coverage counts include
the new append-only rows without weakening earlier receipts.

The source replay establishes physical-LF boundaries and literal preservation.
The semantic tests establish evidence contracts and reject adverse mutations.
Neither replaces the mathematical review above.
