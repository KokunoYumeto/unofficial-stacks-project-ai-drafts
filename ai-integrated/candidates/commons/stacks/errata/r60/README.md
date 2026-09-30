# Homology corrections and their dependent passages

This candidate records 35 source units and 43 bounded edits in Homology, More on Algebra, Weil Cohomology Theories and Cohomology on Sites. The review covers all 136 received Homology reports, reconciles earlier corrections, and adds the source-bound findings proved during that review. Seven optional changes are not integrated. [Read the passages and decisions](REVIEW.md).

The [55-page editorial proof supplement](proofs/correction-proofs.pdf) retains all ten complete proof notes. Its [complete editable LaTeX](proof-source/correction-proofs-assembled.tex), [original notes and review evidence](evidence/review), and [complete reproducible source ZIP](proofs/complete-proof-source.zip) retain the exact calculations and provenance. Eleven editorial underclaims are recorded separately in the [claim and propagation ledger](evidence/review/FINAL_CLAIM_PROPAGATION.json). The longer Kunneth proof completion is explicitly labelled editorial; stronger results do not silently replace the source's claims.

## Corrected chapters and prior readings

- **Homology**: [corrected PDF](proofs/homology-successor.pdf), [complete chapter LaTeX](proof-source/successor/homology.tex); [prior PDF](proofs/homology-prior.pdf), [prior chapter LaTeX](proof-source/prior/homology.tex).
- **More on Algebra**: [corrected PDF](proofs/more-algebra-successor.pdf), [complete chapter LaTeX](proof-source/successor/more-algebra.tex); [prior PDF](proofs/more-algebra-prior.pdf), [prior chapter LaTeX](proof-source/prior/more-algebra.tex).
- **Weil Cohomology Theories**: [corrected PDF](proofs/weil-successor.pdf), [complete chapter LaTeX](proof-source/successor/weil.tex); [prior PDF](proofs/weil-prior.pdf), [prior chapter LaTeX](proof-source/prior/weil.tex).
- **Cohomology on Sites**: [corrected PDF](proofs/sites-cohomology-successor.pdf), [complete chapter LaTeX](proof-source/successor/sites-cohomology.tex); [prior PDF](proofs/sites-cohomology-prior.pdf), [prior chapter LaTeX](proof-source/prior/sites-cohomology.tex).

The four corrected chapters and the supplement reproduce in two fresh builds. All 686 chapter pages were raster-compared, and all 88 changed pages plus one unchanged edit location were visually inspected. All 55 supplement pages were inspected, including direct review of the three final revised pages. Inherited chapter warnings and fifteen readable underfull supplement paragraphs remain recorded. These counts describe rendering checks, not additional mathematical results. [Actual review](replay/independent-review.json) and [source-package verification](replay/source-package.json) state the exact scope.

## Reproduction

Extract the complete source ZIP, then run `python build.py --validate-only`. With pdfLaTeX, XeLaTeX, BibTeX and Python pypdf available, run `python build.py --output /absolute/path/to/new-build-directory`. The destination must be new. The included Windows process guard and shared TeX mutex prevent overlapping engines. The builder retains original prior chapters and two fresh corrected sets, compares PDF and auxiliary bytes at a fixed point, and reports unresolved diagnostics. The reference adapter gives exact source tags and pinned links; cited source authorities are included. [Source roles](proof-source/README.md) distinguish the cumulative chapters from the editorial supplement.

AI source review, corrections, editorial arguments, typesetting and checks: OpenAI Codex - GPT-6 Astra, Ultra effort. No human review, novelty or official Stacks endorsement is claimed. Modified Stacks material retains GNU FDL 1.2; the original licence is included. Preparation-stage status statements in the retained notes are historical. Sealing does not itself admit or compose the edits; those transitions have separate repository receipts.
