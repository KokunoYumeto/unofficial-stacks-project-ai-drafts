# Illusie I: correction of the mathematics and build history

This note corrects earlier claims about our AI-written integration. It does
not report an error in the official Stacks Project or in Illusie's statement
of the Eilenberg-Zilber comparison.

## What was wrong, and what has changed

The draft claimed that Alexander-Whitney followed by shuffle gives a strict
inverse on **unnormalized** bisimplicial chains. This is false. For the
constant bisimplicial abelian group Z, the total complex in degree one is
Z squared, whereas the diagonal complex is Z. An identity on Z squared
cannot factor through Z. Both composites are naturally homotopic to the
identity; strictness requires the appropriate normalized statement.

The [corrected source](../illusie_volume_I/relative-homotopy.tex) supplies
typed ordinal-map formulas, consistent chain/cochain grading, and explicit
recursive homotopies on free models. It also explains the Moore-normalization
comparison through the quotient by degeneracies. Independently checked
[localization consequences](../illusie_volume_I/localization.tex) establish
the general derived-functor construction and localized Dold-Kan with its
fixed nonpositive degree bound.

These changes were already available at candidate commit
`4c3647f926f32a0edade647ebb52adce05d24a8e`, but had not reached the cumulative
main source. They were recovered exactly in source commit
`ea606e202707d215f38e050be2621d0c83cadef0`. The current source-map and
composition checks and five regression tests pass. Tests in finite degrees
support, but do not replace, the independently reviewed all-degree proofs.

This does not complete Illusie Volume I. The inventory currently reaches
printed pages 1-16; the normal/degenerate comparison on page 11 remains
explicitly pending as `I-1.3-006`.

## Why the older PDF did not prove the later source

The [historical combined-build receipt](stacks-errata-a04446e-r47-illusie-build-2026-09-07.json)
retains a 75-page Simplicial PDF, 849,608 bytes, SHA-256
`C88D3FA53E1F7530A84EB4B98CAAD43A5C8103B712BFA79A34BE070764DACCFE`.
The original receipt at commit `c09c0fdb88c82574d034973e011fb8953b24d1bd`
bound that artifact to source `4d62d13fad147acc5f8ed70d80a63994d7c4bd7f`.
The source field was later changed at `ab1c24ea69a45a0204c81af530d9fdca63d5de45`
to `afdbdc289cc4536179af90988eccb70fdfe67998`, and its tree field was amended
at `5817f4c1af8724b147401c785f57ca315b52e31c`. The PDF identity and original
timestamp did not change. Those metadata amendments did not demonstrate a
new build of the later source, so that receipt must not be used as such.

The two actual R48 builds at
`1c7fa79a3d8fdb24a9ec45ba65e65ce1fd8867c2` independently produced matching
36-chapter artifacts, including a 78-page Simplicial PDF. This exposed the
uncorrected AI-written theorem. Reproducibility is evidence about the build,
not a certificate of mathematical truth. Those receipts remain intact and
are not relabelled as builds of the repaired source.

## Current validation boundary

Fresh cumulative builds, corrected-page inspection and public readback of
the recovered source are still required. A separate correction-successor
receipt will bind them to the actual source revision. The sealed R48 errata
admission is unchanged, and no official Stacks tags are assigned to these
AI-written additions.
