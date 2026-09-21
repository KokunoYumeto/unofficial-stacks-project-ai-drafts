# Mathematical comparison and review: category-models module

This is a primary-session mathematical review, not an independent reviewer or
proof-assistant certificate. The executable checks establish source identities,
local references, and reproducible rendering; they do not certify the proofs.

## What was adopted, derived, or reused

| Module label | Source-map origin | Decision |
|---|---|---|
| `psm-slice-equivalence` | `PSM-PROP-0008`, section 26 | Explicit inverse-functor formulation of existing topos-localization mathematics; retained as a useful model, not a new general theorem. |
| `psm-realization-adjunction` | `PSM-PROP-0004`, section 19; `PSM-PROP-0031`, section 38 | Combined adjunction and universal property with the uniqueness qualification repaired. Derived from the existing density/Yoneda foundations. |
| `psm-elements-adjunction` | `PSM-DEF-0030`, `PSM-PROP-0011`, section 28 | Full explicit ordinary-category adjunction, including the action on arrows and inverse constructions. |
| `psm-counit-comma` | `PSM-LEM-0018`, section 30 | Explicit isomorphism on both objects and morphisms, with the direction of the comma category fixed. |
| `psm-counit-test` | `PSM-DEF-0032..0034`, `PSM-PROP-0013`, section 30 | Conditional theorem with all weak-equivalence assumptions visible. No claim that an arbitrary class satisfies Theorem A. |
| `psm-localization-counit` | `PSM-LEM-0016`, section 29 | Descent of the adjunction proved using two-out-of-three, naturality, and the triangle identities. Existence of localizations is an explicit hypothesis. |
| `psm-test-localization` | Consequence of the preceding counit criterion and localization lemma | An explicit derived conclusion, not a separately claimed historical theorem or novel result. |

These seven proof-bearing statements do not equal seven new theorems absent
from Stacks. The distinction between a useful explicit formulation, a derived
consequence, and additional material is intentional.

## Existing mathematics not duplicated as a new contribution

- The category of elements already occurs as the category fibred in sets
  constructed in `categories.tex`, `example-presheaf`.
- The colimit-of-representables calculation is in `sites.tex`,
  `lemma-colimit-representable`; the indiscrete topology gives the presheaf case.
- Localization over an arbitrary sheaf is in `sites.tex`,
  `lemma-localize-topos`, with the representable presheaf case explained in
  `remark-localize-presheaves`. The module makes the category-of-elements
  equivalence explicit, rather than claiming that localization was missing.
- The received nerve definition and full-faithfulness proposition
  (`PSM-DEF-0009`, `PSM-PROP-0003`) are already covered by the earlier FGA
  insertion in `simplicial.tex`, `lemma-characterize-nerves-categories`.
  They are not copied into this module or counted again.

## Adverse checks and corrections

1. **Uniqueness of cocompletion.** The phrase “unique up to unique natural
   isomorphism” needs compatibility with a specified identification on
   representables. The replacement is the equivalence of functor categories;
   the pointed uniqueness assertion is then a consequence. Otherwise natural
   automorphisms of the prescribed functor need not disappear.
2. **Set versus category of functors.** The right adjoint is set-valued:
   its value is the set of functors from the slice, not the category of functors.
   The notation convention now states this explicitly. The proofs use ordinary
   categorical adjunctions, not a silently asserted 2-adjunction.
3. **Comma orientation.** An object over `c` has a map `T(id_a) -> c`, not
   `c -> T(id_a)`. The structural maps on every object of `A/a` and their
   morphism compatibility are written out. Reversing that orientation would
   give a different result.
4. **Weak-equivalence hypotheses.** The criterion assumes isomorphism
   invariance, two-out-of-three, asphericity of categories with final objects,
   and a right-asphericity implication. It does not prove that implication or
   identify all historical definitions of test category. Under the producer's
   final-object and right-asphericity assumptions, categorical isomorphisms
   already lie in the weak class; spelling this out loses no intended case.
5. **Localization descent.** Naturality for formal inverses follows from
   naturality for the original arrows. Thus unit and counit actually descend;
   an objectwise isomorphism alone was not substituted for a natural one.
6. **Malformed received TeX.** The received display in `PSM-PROP-0031` uses
   `ightleftarrows` without a leading backslash. The new module uses a correctly
   stated adjunction and hom-set formula. The earlier missing backslash in the
   provisional test-functor definition is outside this selected module and
   remains a receiving-side correction for that later import.

## Source reading and boundary

The receiving session read the exact `ps2.tex` spans identified in
`source-map.json`, including the historical qualifications and the distinction
between the slice-based right adjoint and the usual nerve. It also read the
relevant received proofs and the existing Stacks source blocks above.
All new prose is independently written. The source edition carries a CC0
dedication, whose exact file hash is recorded; this does not relicense inherited
Stacks material. The accompanying repository `COPYING` is preserved.

The new file is an independently readable extension module in this repository.
It does not replace `categories.tex`, change the inherited 48-round errata
registry, or claim that the existing cumulative Stacks PDFs contain it.
Its separate PDF, complete direct LaTeX, and reproducible source ZIP are the
module's deliverables. Stitching modules into a later cumulative reader is a
separate release step, not evidence that these already available proofs are
unfinished. The rest of the received 151-unit draft remains under comparison.
