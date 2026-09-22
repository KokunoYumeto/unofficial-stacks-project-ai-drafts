# R50: final, bounded source review

Reviewed against the exact local primary sources at official Stacks commit
`a04446e57ec1fbc252a871afcec7752fb2807b14`, not against a summary or an
unverified parallel source. Reviewer: OpenAI Codex - GPT-6 Astra, Ultra effort.
No human review, second-model review, or upstream endorsement is claimed.

## Fixed point of the fibre functor (MC-STK-ERR-1574)

`spaces-limits.tex`, line 178, ends the reverse implication of
`lemma-characterize-relative-limit-preserving`. Lines 168-169 fix
`y_T` in `G(T)` and explicitly set the aim of proving `F_{y_T}` limit
preserving. The final functor must therefore be `F_{y_T}`, not `F_y`.
The `y` in the preceding forward implication does not supply the point fixed
in this direction. Definition `definition-locally-finite-presentation` fixes
the fibre by its chosen element, so this is a typing/scope correction.
The exact operation changes only `F_y(T'_i)` to `F_{y_T}(T'_i)`.

This change does not claim to repair every sentence of the proof. In
particular, the further inconsistencies listed below remain visible.

## Fibre products require finite limits (MC-STK-ERR-1575)

`spaces-limits.tex`, lines 263-269, compares a filtered colimit of fibre
products with the fibre product of the colimits, over the varying base
`G(T_i)`. Commutation with products alone does not express the compatibility
of the two images in that base. Replace `finite products` by `finite limits`.

This is supported directly by `categories.tex`,
`lemma-directed-commutes`, lines 2181-2195: filtered colimits of sets commute
with finite limits, including fibre products and equalizers. Explicitly, a
pair with equal images in the colimit is represented at a common stage;
its images become equal at a later common stage, so it comes from a fibre
product. Equality of two such pairs is also witnessed at a common later
stage, proving injectivity. This explains the exact displayed identification.
No SGA quotation is needed or claimed as consulted evidence here.

## Deliberately separate follow-up findings

The following source locators are preserved for later deduplication and
adjudication, not silently added to the two accepted operations:

- Line 159: `that x_T the image` lacks a finite verb.
- Lines 170-171: the displayed inverse limit is called a directed limit,
  and the indexed family is called singular `affine scheme`.
- Line 171: `x_{T'} in F_{y_T}` omits evaluation of the fibre functor at `T'`.
- Lines 172-173: the image of the fixed `y_T` should belong to `G(T'_i)`;
  the printed `F(T'_i)` and undefined `y_{T'}` require their own check.

These observations do not change the isolated payload or establish completed
intake for the chapter. The operation spec, payload and formula/diagram
inventory continue to cover exactly two source edits and two stable units.
