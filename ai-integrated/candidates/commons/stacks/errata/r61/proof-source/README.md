# Complete editable R61 proof sources

The six chapter files contain the exact cumulative previews. correction-proofs.tex inputs all twenty-five complete editorial proof notes; correction-proofs-assembled.tex contains the same mathematical text in one directly editable file. Original Markdown, the Pandoc syntax trees and parsed mathematical payloads are retained.

Build the chapter PDFs with pdfLaTeX and BibTeX, and the proof supplement with XeLaTeX. The provided guarded build.py checks all input hashes, holds the shared Windows TeX mutex, and reproduces prior chapters and two fresh successor sets. The reference adapter supplies exact source tags where external auxiliary files are absent. GNU FDL 1.2 is included. AI editorial work: OpenAI Codex - GPT-6 Astra, Ultra effort; no human or official review is claimed.

For the editorial supplement, install the Cambria, Cambria Math and Segoe UI Symbol fonts. Segoe UI Symbol supplies U+266D, which is absent from Cambria and Cambria Math. Python pypdf is used by the guarded builder. The original proof notes remain unchanged; PROOF_CONVERSION.json records two layout adjustments inside parsed math and the restored four-map ASCII diagram. Unmarked mathematical notation is otherwise retained literally.
