# Pursuing Stacks: categories of elements and homotopy intervals

AI mathematical drafting, source/proof review and packaging for these modules:
OpenAI Codex — GPT-6 Astra, Ultra effort. No human review or proof-assistant
verification is claimed.

This first normalized module supplies explicit proofs of the
category-of-elements adjunction, its counit's comma-category formula, and a
criterion for an equivalence after localization. It also explains the
presheaf-slice equivalence and the realization--nerve universal property used
in those proofs. The source is Grothendieck's *Pursuing Stacks*, sections 19,
26, 28--30, and 38; [exact source locators](source-map.json) accompany the text.

## Read or reuse the module

### Categories of elements, relative nerves, and a counit criterion

1. [Reader PDF](01-category-models.pdf).
2. [Complete editable LaTeX](02-category-models.tex).
3. [Complete reproducible source ZIP](03-category-models-source.zip).

The direct LaTeX contains the whole text, not just an input-only master. The
archive includes the same LaTeX, builder, Windows process guard, source map,
review, and licensing material. [Artifact identities](release.json) identify
the exact PDF and source archive. No new Zenodo version is created for this
small module.

### Homotopy intervals and an asphericity criterion

1. [Reader PDF](04-homotopy-intervals.pdf).
2. [Complete editable LaTeX](05-homotopy-intervals.tex).
3. [Complete reproducible source ZIP](06-homotopy-intervals-source.zip).

The second six-page module proves the sieve-cutoff contraction, the
product-asphericity calculation making cylinder projections weak, and the
sufficient counit-test criterion. It then proves universal contraction,
comparison of intervals, and the subobject-classifier criterion. Two
elementary weak-equivalence lemmas make the additional closure assumption
explicit. There are eight statements with proofs, mapped to fourteen source
IDs from sections 31 and 37. [The review](INTERVALS_REVIEW.md) records a
historical repeated-endpoint typo separately from official Stacks fixes;
[artifact identities](intervals-release.json) bind this module's files.

## What the seven statements establish

- Presheaves over a presheaf are equivalent to presheaves on its category of
  elements, with both inverse functors given explicitly. This is an explicit
  formulation of existing Stacks mathematics, not a new general theorem.
- Any functor from a small category into a cocomplete category extends by
  colimits to presheaves; the relative nerve is its right adjoint. Uniqueness
  is relative to a fixed identification on representables.
- The category-of-elements functor has right adjoint
  `C |-> (a |-> Fun(A/a, C))`, where the values are sets of functors.
- A comma category of its evaluation counit is explicitly isomorphic to
  the category of elements formed from `C/c`.
- With the stated Theorem-A-type assumption, testing the counit on categories
  with a final object is equivalent to every counit being a weak equivalence.
- An adjunction with weak-equivalence counits descends to an equivalence of
  localizations under the precise inverse-image definition of weak
  equivalences in its domain.
- Combining the last two results gives the conditional test-category
  localization equivalence. It does **not** prove that an arbitrary category
  meets the criterion or that the localizations exist.

[The mathematical review](REVIEW.md) separates existing coverage, additional
explicit proofs, and repairs to the received AI draft. Those repairs are not
official Stacks errata. No theorem here is claimed to be mathematically new,
human-reviewed, or proof-assistant-verified.

## How much is integrated?

This is a **standalone extension module in the unified repository**, not yet
an insertion into `categories.tex` or the existing cumulative Stacks PDFs.
Together the two modules contain fifteen proof-bearing statements linked to
twenty-five received source IDs. The received draft has 151 local definitions,
results, and examples; these modules are not completion of that draft, nor of
the whole historical work.
[The intake record](INTAKE.md) and [frozen-input inventory](received-inventory.json)
retain those boundaries. The next comparison concerns the remaining
asphericity and interval arguments, not EGA.

## Reproduce

Install Python 3 and a TeX distribution supplying `pdflatex`, `amsart`,
`lmodern`, `amsmath`, `amssymb`, `amsthm`, `xy`, and `hyperref`. These are
standard packages; no custom style, external image, private font, bibliography,
or missing body file is required. From the extracted archive root run:

```sh
python pursuing-stacks/check.py
python pursuing-stacks/build.py --output fresh-module-build
```

For the interval module, use `check.py --record intervals-integration.json`
and `build.py --source 05-homotopy-intervals.tex --output fresh-interval-build`.

The builder creates two fresh builds, requires a fixed point and matching
PDF/auxiliary bytes, and rejects unresolved references and overfull boxes.
On Windows it acquires `Global\InterlanguageTeXSlotV1`, captures every TeX
process tree, and fails closed if the shared slot is occupied. It does not
terminate other tasks' processes. Identical TeX distributions and package
versions are required to reproduce the recorded PDF hash; other versions may
render equivalent content with different bytes. The published build and
visual receipts describe the actual checks, not a proof certificate.

The repository's [GNU Free Documentation License](../COPYING) is retained;
inherited Stacks material is not relicensed. The historical source edition's
separate CC0 notice is identified in the source map. This independently
written module does not reproduce that edition wholesale.
