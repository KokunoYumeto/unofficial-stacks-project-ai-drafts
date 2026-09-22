# R50: two corrections in Spaces and Limits

This is a bounded review of two reported locations, not a certification of the
entire chapter. The frozen authority is Stacks commit
`a04446e57ec1fbc252a871afcec7752fb2807b14`. Both decisions were re-examined
directly in the primary session rather than accepted on the producer's say-so.
No human expert or independent second-model review is claimed.

## MC-STK-ERR-1574 — the fixed fibre

Producer identity: `SPACES-SRC-00178-UNBOUND-Y`.

At source line 178, change `F_y(T'_i)` to `F_{y_T}(T'_i)`.

The definition at lines 84-87 defines the fibre functor from an element of
`G(T)`. The reverse implication of
`lemma-characterize-relative-limit-preserving` fixes `y_T` at line 168 and
explicitly names `F_{y_T}` as the functor to be tested at line 169. The output
element at line 178 must lie in that fibre. The variable `y` belongs to the
separate forward implication and is not the fixed element here.

Keeping `F_y` would require an unstated renaming across proof directions.
Renaming all occurrences of `y_T` instead would be a larger, unnecessary edit.
The bounded subscript correction is the best-supported choice. Editorial
confidence is high because the definition and local binding determine it;
this is not a calibrated probability. No hypothesis, arrow, or conclusion is
changed. The one formula alteration is explicit, not counted as invariant.

## MC-STK-ERR-1575 — the fact used in the fibre-product comparison

Producer identity: `SPACES-SRC-00269-PRODUCTS-VS-LIMITS`.

At source line 269, change `finite products` to `finite limits`.

The preceding display identifies a filtered colimit of fibre products with a
fibre product of filtered colimits, over the varying sets `G(T_i)`. A fibre
product involves the equality of two images, not merely an unrestricted pair.
The fact actually needed is finite-limit preservation. The frozen
`categories.tex`, lines 2181-2195, `lemma-directed-commutes`, states this and
explicitly includes fibre products and equalizers.

Direct check: represent a pair in the target by two elements at a common index.
Equality of their images in the colimit holds at a common later index, where
they define an element of the fibre product. This proves surjectivity. If two
such pairs have the same images in the colimits, a common later index witnesses
both component equalities, proving injectivity. This uses the filteredness
already assumed; no additional mathematical hypothesis is introduced.

The alternative wording 'finite products and equalizers' would also state a
sufficient fact but is longer than the standard source-attested 'finite limits'.
Keeping 'finite products' leaves the displayed fibre-product comparison
unjustified by the fact cited. Editorial confidence is high for this localized
proof-justification repair, not for the chapter as a whole.

The producer mentioned SGA 4. That passage has not been independently consulted
in this review and is not claimed as evidence. The actually consulted source is
preserved at `authority/source/categories.tex`, with exact lines and hash in
`PREFLIGHT.json`.

## Deduplication, limitations, and follow-up

All 50 admitted overlay manifests through R49 (including the separate Verdier
overlay) were hash-checked against their registry records. Their 200 bound
stable-unit, source-map, decision, and rejection files were read and checked.
No previous `spaces-limits.tex` operation was found. Both local pinned bytes and
the observed public generated-source commit retain the reported preimages.

Nearby lines 170-173 contain additional apparent inconsistencies, recorded in
`unresolved-findings.json`; this batch does not silently fix them or call that
whole proof error-free. They remain executable follow-up work, not a human gate.
Translations retain their source-fidelity policy. Generated English composition
belongs to its designated composer, using the exact operations in registry order.

## Build implementation note

R49's inspected build/replay scripts were adapted mechanically for R50. The
source-copy step is narrowed to the 154 individually Git-blob-verified pinned
files, excluding incidental caches. Initial preparation rejected an executable
Git file because it expected mode 100644 only; allowing regular executable mode
100755 corrected that local preflight without changing source bytes. No build
or mathematical result was manufactured by this repair.
