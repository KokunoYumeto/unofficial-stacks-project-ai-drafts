# Review: homotopy intervals and the sufficient asphericity criterion

This is primary-session source and proof review, not an independent review or
proof-assistant certificate. The source was read in `ps2.tex`, sections 31 and
37, including the source's distinction between two-out-of-three and the
stronger split-projector condition. Fourteen exact source-map IDs support eight
proof-bearing statements.

## Mathematical content

| Result | Source IDs | Receiving decision |
|---|---|---|
| Weak-equivalence transport along a homotopy | PSM-LEM-0019 | Elementary two-out-of-three consequence, retained as an explicit dependency. |
| Inverse images of isomorphisms have split-projector closure | PSM-LEM-0020 | Shortened proof: an invertible idempotent is the identity. Not claimed as new mathematics. |
| Sieve-cutoff contraction of the slice-based relative nerve | PSM-PROP-0014 | Explicit object/arrow construction, composition, naturality, and both endpoint checks. |
| Product-asphericity implies weak cylinder projections | PSM-PROP-0015 | Both comma-category isomorphisms checked on objects and morphisms; products are presheaf products, not assumed to exist in the indexing category. |
| Sufficient counit-test criterion | PSM-PROP-0016 | Split-projector closure stated as the precise used hypothesis; saturation in the received statement implies it. The proof reuses the prior counit model and supplies the sufficient conditions. |
| Universal asphericity from a contraction | PSM-LEM-0022 | Multiply the entire contraction by an arbitrary object; do not assume weak equivalences are automatically product-stable. |
| Comparison with an interval carrying a multiplication | PSM-LEM-0023 | Only left-unit and left-zero identities are needed; no associativity or commutativity is smuggled in. |
| Subobject-classifier criterion | PSM-PROP-0028 | Empty pullbacks require the stated strict initial object. The endpoints are different; the characteristic map and intersection multiplication give the proof. |

The definitions mapped as PSM-DEF-0035..0038 and PSM-DEF-0044..0045 are
retained with their scope and variance explicit. The notions of homotopy
interval and asphericity do not assert a Quillen model structure. The
Theorem-A-type condition is assumed and plainly identified, not purportedly
proved by this module. No simplex/cube example is inferred without its own
argument.

## Adverse checks

- **Sieve direction:** arrows may leave the sieve but cannot enter it from its
  complement. Reversing this convention would invalidate the cutoff. The table
  depicts the three permitted arrow types and their actual images.
- **Comma categories:** the slice object includes an arrow *to* the selected
  target. Its element coordinate is forced by contravariance, leaving the two
  representable arrows. This proves the displayed isomorphisms rather than
  only suggesting them.
- **Closure:** two-out-of-three does not, by itself, justify cancelling a weak
  split projector into two weak factors. The extra condition remains explicit.
- **Products:** universal asphericity quantifies over every factor. The
  contraction proof derives each projection separately and does not assume
  arbitrary base-change stability of the weak class.
- **Classifier endpoints:** a point is a split monomorphism, so its
  characteristic map exists. Pullback along itself is full and along the other
  disjoint endpoint is empty. Both pullback squares are shown.

## Historical-source correction, not an official Stacks fix

`PSI-HIST-001`: in the classifier corollary of source section 37, manuscript
page 60, `ps2.tex` byte span `[182319,183952)`, the empty-intersection formula
prints `e_0^L \sand e_0^L=\varnothing`. The second endpoint must be `e_1^L`.
The same paragraph defines the points as full and empty subobjects and the
next paragraph uses their mixed intersection, which supplies the direct
evidence. The received AI draft already uses the corrected pair. No official
Stacks source was changed or assigned an erratum ID for this historical typo.

## Comparison and integration boundary

Categories of elements, presheaf products, subobject classifiers, and
categorical localization are existing foundations. The added value is the
explicit cutoff construction and the chain of conditional arguments. Targeted
comparison is recorded; neither a keyword search nor these eight statements
establishes eight mathematically novel results or exhaustive absence from
Stacks. The module follows the previous module's notation and is a separate
readable mathematical addition in the unified repository. The old cumulative
Stacks PDFs and original chapter sources are unchanged.
