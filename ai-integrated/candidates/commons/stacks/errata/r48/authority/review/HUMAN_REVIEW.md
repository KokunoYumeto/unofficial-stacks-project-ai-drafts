# Chapter 75: nine source corrections reviewed

## Result and limits

All nine submitted observations are valid. The coordinator and a separate reviewer read the relevant statements, proofs and definitions. Exact line-bound replacement replay passes. No duplicate was found in the source maps of all 47 errata rounds in the 48-entry registry, whose bytes were anonymously checked at public commit `7f676209d9c2136265996bc7451d3c6a9bff3d00`.

These are **reviewed candidates, not an admitted or published overlay**. The frozen English source and every translation remain untouched. Any later admission must use the current registry cutoff and the affected-source build requirements. Human review is welcome but is not a prerequisite for that work.

## Decisions for expert review

All line numbers below refer to the pinned `spaces-perfect.tex`, SHA-256 `5791551E4C8BAE909A05C066AD60FE7FF95ED07B6D4A6537CB29527D8280DF34`, in Stacks commit `a04446e57ec1fbc252a871afcec7752fb2807b14`.

| Producer ID | Source line | Selected correction | Why this is the best supported reading |
|---|---:|---|---|
| CH075-SD-001 | 492 | Close the outer parenthesis in `H^i(RF(\tau_{\leq a}E))`. | The expression is the source cohomology group of the displayed map. Its argument is otherwise unclosed. |
| CH075-SD-002 | 552 | `i >= b+n` → `i >= b+N`. | The lemma fixes the bound `N`. Its stated interval and the vanishing truncation both give `b+N`. |
| CH075-SD-003 | 1418 | `V_{p,1}` → `V_{p,i}`. | The induction uses each member of the indexed affine cover, not only its first member. The original first-member assertion is insufficient; it is not necessarily false by itself. |
| CH075-SD-004 | 1498 | Delete `where`; retain `such that` on the next line. | One connector introduces the unchanged list of conditions. |
| CH075-SD-005 | 1524 | `W cap U_{n+1}` → `W cup U_{n+1}`. | The proof defined `W_p` by union, and `U_{n+1}` is empty. Union gives the required base case `W`. |
| CH075-SD-006 | 1563 | “elementary distinguished triangle” → “elementary distinguished square”. | The defined input is a square. The subsequent construction produces triangles from it. |
| CH075-SD-007 | 1724 | “right exact” → “left exact”. | Contravariant Hom yields the displayed left-exact sequence. The following Ext¹ obstruction explicitly allows failure of surjectivity at the right end. |
| CH075-SD-008 | 1785 | `U cap V` → `U times_X V`. | `V→X` is only assumed étale, not an inclusion. The statement and later formula explicitly use the fibre product. |
| CH075-SD-009 | 1904 | `V→Y` → `V→X`. | The lemma forms `V times_X U` and restricts sheaves from `X`; it never introduces `Y`. |

## Choices warranting particular attention

**007: exactness convention.** This was checked against the same frozen corpus, not decided by terminology preference. `categories.tex:459–463` defines contravariance via the opposite category; `categories.tex:3278–3287` defines left and right exactness. `homology.tex:750–760` explicitly gives the sequence starting with `0→Hom(M3,N)→Hom(M2,N)→Hom(M1,N)`. Removing the adjective entirely, as the French producer does, would avoid the erroneous assertion but would be less precise than the minimally corrected English text. The selected correction is “left exact”.

**008: intersection is not harmless shorthand here.** The definition at lines 1296–1313 does not embed `V` in `X`. For example, the permitted étale map `V=X disjoint-union U→X` gives `U times_X V=U disjoint-union U`, not merely the intersection of `U` with the image of `V`. The selected fibre product is already used at lines 1766, 1772 and 1798.

**003: qualification of the producer's reason.** Saying the property holds for the first affine member can be true. The defect is that this does not establish the uniform assertion needed by the induction. The corrected index repairs that omission without claiming the first-member assertion was false.

The editorial confidence is high because local definitions, types and proof steps directly determine each replacement. This is a reasoned judgment, not a calibrated probability or external expert certification.

## Reproducible evidence

- [Exact operations and rationales](ADJUDICATION_SPEC.json).
- [Replay and public-registry duplicate check](REPLAY_v2.json), including exact old/new lines and their hashes.
- The original 4,545-byte packet survives byte-for-byte at the start of the producer's growing ledger and is frozen as `producer-prefix-4545.bin`.
- The effective source was calculated in memory only: 283,794 bytes, SHA-256 `388F63697C59EA6228CBD604B0969D8341014AAE0375E8CDAC914FC4D0D8D988`.
- Ordered preservation passes for 187 labels, 752 references, 5 citation commands, 730 environment markers and 206 items.
- The later producer rows 010 and 011 are outside this nine-row packet. They are not silently included or marked reviewed here.

The first replay receipt is preserved. Its duplicate-check gaps were caused by the checker's assumption that every historical map identity contained a byte count. R1–R32 bind those maps by SHA-256 alone. The second replay checks those actual historical contracts and records observed sizes; no mismatching hash was excused.
