# Reproduce the two R50 chapter proofs

This package contains the complete project-specific editable inputs for the
isolated authority and corrected **Limits of Algebraic Spaces** chapter proofs.
It is not a full Stacks reader. Cross-chapter auxiliaries are intentionally
absent, so inherited external-reference question marks remain in both proofs.
The package needs Python 3 and a TeX distribution providing pdfLaTeX, BibTeX,
AMS packages, Xy-pic, hyperref, and the other standard packages named by the
included class and preamble. No project-specific input is downloaded at build time.

Run `python reproduce.py --output /path/to/new-proof-build` from this directory.
On Windows the script holds `Global\InterlanguageTeXSlotV1` continuously and
captures each complete engine process tree. It fails without launching TeX if
the slot is unavailable. `--pdflatex` and `--bibtex` accept explicit executable
paths. Builds use the original fixed epoch and three PDF passes with BibTeX.
The expected byte identities are in `inputs.json`; a different TeX distribution
may change PDF bytes without changing the mathematics.

The authority is Stacks commit `a04446e57ec1fbc252a871afcec7752fb2807b14`.
The corrected source differs only at the two operations in the enclosing R50
candidate. All modified Stacks content retains GNU FDL 1.2; see `COPYING`.
The original Stacks text is the work of its authors. This is an unofficial
AI-produced correction draft with no upstream endorsement or human review.
Source packaging and final review: OpenAI Codex - GPT-6 Astra, Ultra effort.
