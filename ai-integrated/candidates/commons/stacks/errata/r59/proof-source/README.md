# Complete editable sources for the R59 corrections

The three chapter files contain the complete cumulative chapter text, with thirteen bounded edits representing five findings. `correction-proofs.tex` inputs both complete editorial proof notes; `correction-proofs-assembled.tex` contains the same text in one directly editable file. Original Markdown, syntax trees and the explicit Brauer notation conversion map remain included. The stronger conclusions are editorial material, with no novelty claim.

## Reproduce the PDFs

Use Python 3 with `pypdf`, a TeX installation providing pdfLaTeX, XeLaTeX and BibTeX, the packages named by the retained preamble and masters, and Cambria/Cambria Math fonts for the supplement. The recorded builds use MiKTeX on Windows; other software or font versions may change PDF bytes.

From this directory, run:

```text
python -B build.py --validate-only
python -B build.py --output PATH_TO_A_NEW_BUILD_DIRECTORY
```

The first command verifies every source-package hash. The second compiles the three prior chapters, two fresh copies of all three corrected chapters, and two fresh copies of the editorial supplement. It requires a fresh destination. Every document must reach a fixed point, and the two corrected copies must have identical output hashes and diagnostics. `BUILD_RECEIPT.json` records the actual result; it does not certify visual review.

For a supplement-only presentation revision, use:

```text
python -B build.py --supplement-only --output PATH_TO_A_NEW_BUILD_DIRECTORY
```

This performs both fresh supplement builds and records the restricted scope. On Windows the builder holds `Global\InterlanguageTeXSlotV1` through the complete captured process trees and log checks. If its one bounded acquisition attempt fails, it starts no engine.

## Exact source roles

The root chapter bodies are the corrected cumulative versions. For the prior builds, the runner substitutes all three bodies from `prior/` while retaining the same root rendering dependencies. `successor/` also preserves the corrected bodies. Original dependencies in those subdirectories are retained for provenance; the reproducible chapter rendering uses the root preamble, reference adapter, chapter navigation, class and bibliography.

The reference adapter resolves external references to exact source tags and pinned primary-source links, with the cited source files retained under `reference-authority/`. It does not invent external theorem or page numbers. `EXTERNAL_REFERENCE_CLOSURE.json` and `NAVIGATION_DERIVATION.json` record the complete transformations. The full-project-only index is labelled as such. This package supplies isolated chapters and their editorial arguments, rather than the entire Stacks reader.

The direct assembled supplement contains all proof text. Its fonts and package dependencies, together with both original proof notes and the conversion evidence, are supplied or identified here. The complete-source ZIP preserves this directory byte for byte, including `PACKAGE_MANIFEST.json`.

Modified Stacks material retains GNU FDL 1.2; the licence is included. AI source review, corrections, editorial arguments, packaging and checks: OpenAI Codex - GPT-6 Astra, Ultra effort. No human review or official Stacks endorsement is claimed.
