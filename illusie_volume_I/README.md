# Illusie Volume I: Stacks-style integration

This dossier develops independently written mathematical statements and proofs
from Luc Illusie, *Complexe cotangent et deformations I*, Lecture Notes in
Mathematics 239, in the existing unofficial Stacks-derived repository.
It is not an official Stacks contribution or proof-assistant formalization.

The scope is the complete substantive mathematical corpus of Volume I.
Production proceeds by source section. I.1.1 is now mapped in 13 decisions
covering all 47 section anchors; the whole volume is not yet mapped or integrated.

## Current mathematical work

[`relative-homotopy.tex`](relative-homotopy.tex) gives a complete draft proof of
the relative homotopy construction in I.1.1.6, printed pp.4-6. It constructs
pointwise strongly cartesian lifts of simplicial objects, transports relative
homotopies through a fixed lift, and proves that base change descends to the
homotopy quotient categories. It also separates functoriality over the base
from the stronger property of preserving cartesian morphisms.

Absolute simplicial homotopies and their functoriality are already covered by
Stacks Tags [019M](https://stacks.math.columbia.edu/tag/019M),
[08RJ](https://stacks.math.columbia.edu/tag/08RJ), and
[019Y](https://stacks.math.columbia.edu/tag/019Y). Those results are dependencies,
not new contributions. The relative construction uses the strongly cartesian
universal property of [02XK](https://stacks.math.columbia.edu/tag/02XK) and
fibred categories as in [02XM](https://stacks.math.columbia.edu/tag/02XM).

The addition is composed into [`simplicial.tex`](../simplicial.tex), Section 28
in the targeted build: Lemmas 28.1-28.2 and Remark 28.3, rendered on pp.48-50.
The proof received an independent mathematical check, and the affected pages
were directly inspected after the chapter build reached a fixed point.
`map.json` records existing coverage separately from the new construction;
`source-lock.json` binds the 24 source witness files used for I.1.1-I.1.2.

The original and changed chapter were built with identical inputs under one
machine-wide TeX mutex. Both reached a fixed point in four passes, with no
fatal errors, missing glyphs, unresolved citations, or final rerun requests.
The 75-page changed chapter has SHA-256
`550D8C5A18F9BDB0AFA3224D265AB6F56B84F3E9C2D4E1B6E6BC8332424A6CF9`.
This sparse targeted build has 67 unchanged unresolved external labels because
other-chapter AUX files are absent; none occurs in the new section. It is not
a full-book build. `build-receipt.json` records this limitation explicitly.

`verify.py` checks complete source-anchor disposition, exact existing tag/label
identities, local-label uniqueness, and exact additive root composition. Removing
the marked addition recovers the original chapter byte-for-byte, so the older
Volume II receipt remains immutable and replayable. Two negative regression
checks reject unrelated root edits and a changed proof not reflected in the root.
Automated checks and AI review do not certify mathematical correctness.

The I.1.2 targeted candidate build is 77 pages and 889,443 bytes, SHA-256
`409F12D9076D36E05CB8610B137E7E0EE3FE47E5571DA1AF81CDDC289435065C`.
Its dedicated receipt is `build-receipt-i1-2.json` and its bounded QA is
`qa-i1-2.json`; the six rendered review pages passed visual inspection.

I.1.2, printed pp.6-8, is now mapped and integrated as the signed
multisimplicial totalization and explicit Eilenberg-Zilber--Cartier theorem.
The repository's derived Tag 08QC is recorded as related coverage only; it
does not supply these chain-level maps or homotopies. The source map records
the exact gap and the new local labels.

The bounded canon-keeper rule for this edition is additive and scan-based:
when a transcription or translation defect is found, compare the witness with
the primary scan, make the smallest evidenced correction or erratum, and
record old/new text, locus, evidence and hashes. Mathematical uncertainty is
kept reversible rather than silently normalized.

Next source unit: I.1.3, beginning on printed p.8.

## Source and repository identities

- Primary authority: Volume I, DOI `10.1007/BFb0059052`, 14,349,904 bytes,
  SHA-256 `1855B49FE461B13B1CBAEE1341C8FC3E3E0CDDC034C54ABEC1165AF061B90A56`.
- For the current section, physical PDF pp.19-24 correspond to printed pp.1-6.
  The authority hash was recomputed and those six pages were directly inspected.
- Repository baseline: `f73b18165c7162b8386de06cc3c50bd4ced745b6`.
- Branch: `codex/illusie-volume-i-20260906`.
- Existing `illusie_r1` and `illusie_r2` dossiers concern Volume II and do not
  count toward Volume I completion.
- Independent edition sources are retained in the existing
  [Illusie edition lineage](https://github.com/KokunoYumeto/illusie-cotangent-complex-editions).

The primary scan and editable witnesses remain unchanged. A printed carrier
error on p.5 is documented in `source-notes.md`; the new proof uses the typed
composition. Local source images are evidence only and are not included here.

GitHub records coherent incremental work. Zenodo is used for substantial
cumulative milestones in the established lineage. Public access is preserved.
