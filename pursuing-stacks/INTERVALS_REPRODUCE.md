# Reproduce the homotopy-interval module

The whole editable text is `pursuing-stacks/05-homotopy-intervals.tex`.
It needs only standard TeX packages: `amsart`, `lmodern`, `amsmath`,
`amssymb`, `amsthm`, `xy`, and `hyperref`. With Python 3 and `pdflatex`
installed, run from the extracted archive root:

```sh
python pursuing-stacks/check.py --record intervals-integration.json
python pursuing-stacks/build.py --source 05-homotopy-intervals.tex --output fresh-interval-build
```

The PDF is `fresh-interval-build/a/05-homotopy-intervals.pdf`. The builder
uses two independent fixed-point builds and the Windows named TeX mutex where
applicable. `tools/tex_process_guard.py` is included. No custom class, style,
private font, image, bibliography, or separate text input is missing. The
recorded original build used MiKTeX pdfTeX 1.40.29; exact byte reproduction
requires the same TeX/package versions. The included companion LaTeX is a
mathematical reference, not a hidden typesetting input.

`source-package.json` inventories the complete archive. The interval build,
visual, source-map, integration, and review records accompany the source.
The module is an independently written AI draft distributed under the
repository's GNU Free Documentation License 1.2 (`COPYING`). Neither the
Stacks Project nor the historical source's authors have endorsed it. No
independent mathematical or proof-assistant certification is claimed.
