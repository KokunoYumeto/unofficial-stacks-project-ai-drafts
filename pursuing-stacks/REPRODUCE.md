# Reproducing Categories of Elements, Relative Nerves, and a Counit Criterion

The complete editable text is `pursuing-stacks/02-category-models.tex`.
It has no body inputs, custom style files, figures, private fonts, or
bibliography dependencies. Install Python 3 and a standard TeX distribution
with `pdflatex`, `amsart`, `lmodern`, `amsmath`, `amssymb`, `amsthm`, `xy`,
and `hyperref`. From this archive's root run:

```sh
python pursuing-stacks/check.py
python pursuing-stacks/build.py --output fresh-module-build
```

The output is `fresh-module-build/a/02-category-models.pdf`. The builder
requires two fresh fixed-point builds to agree, rejects unresolved references
and overfull lines, and records the PDF hash. The recorded build used MiKTeX
pdfTeX 1.40.29; other TeX distributions can reproduce the text but may produce
different bytes. No bundled commercial software or private credentials are
needed. On Windows, the builder holds `Global\InterlanguageTeXSlotV1` and uses
the included `tools/tex_process_guard.py` to capture the whole process tree.
An occupied slot produces a bounded timeout, never termination of another task.

`pursuing-stacks/build-receipt.json` records the original two-build result;
`visual-qa.json` records inspection of all six pages. These are typesetting
checks, not independent mathematical certification. `REVIEW.md` and
`source-map.json` give the mathematical scope and historical source locators.
`source-package.json` inventories the archive's other files by hash.

This independently worded AI draft is distributed under the GNU Free
Documentation License 1.2, supplied in `COPYING`, consistently with the
repository's source license. It uses the Stacks Project's existing
category-of-elements and presheaf foundations as cited dependencies and
Grothendieck's *Pursuing Stacks* (arXiv:2111.01000v2) as the historical source.
Neither the Stacks Project nor the historical source's authors have endorsed
this draft. It is not a re-publication of the whole historical source and does
not change its or the Stacks Project's licensing.
