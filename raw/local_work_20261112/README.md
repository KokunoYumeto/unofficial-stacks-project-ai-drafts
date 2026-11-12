# Local working copies of the Stacks-format work, as they stood on 12 November 2026

The Stacks-format drafts in this repository (FAC, GAGA, FGA, EGA and the Tôhoku paper written up as statements and
proofs in Stacks-style LaTeX) were made in local clones of the Stacks project. Their branches were pushed to a fork,
KokunoYumeto/stacks-project, that no longer exists; those commits are kept here, in the `history/source/*` branches
and in the history of `main`. This folder holds what the clones contained beyond those commits: work files that were
never committed, uncommitted edits, and three one-line fixes committed only locally. It is a raw record of the
method, not part of the edition: nothing in it is integrated into the source at the top of this repository, and
later rounds in `main` supersede most of it.

## The clones

All are clones or `git worktree`s of one local Stacks clone, based on upstream commit
[`a04446e`](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14), the commit this
repository is pinned at.

| Folder | What the clone was | Branch and commit | Where that commit is here | What this folder holds |
|---|---|---|---|---|
| `stacks-ftg/` | The main working copy: FAC, GAGA, FGA and the Tôhoku paper in Stacks format | `codex/fac-tohoku-gaga` at `8688a72` | ancestor of `history/source/fac-tohoku-gaga` (`ad58625`) | the uncommitted edits (full copies of 17 modified files: nine chapters, the FGA tables, three `srcmap` scripts, the Makefiles; its `.gitattributes` is renamed `dot-gitattributes` so that it does not act on this repository); the source-map rounds of the Tôhoku comparison `tohoku_r9` to `tohoku_r20` and `tohoku_r35` to `tohoku_r70` (the final round, `tohoku_r71`, is at the top of this repository) and the GAGA rounds `gaga_r1`, `gaga_r2`; the English GAGA (our AI translation, as in [serre-gaga](https://github.com/KokunoYumeto/serre-gaga)) split by sections, with its reference ledgers and receipt (`gaga_source_r1/`; the scan of the 1956 article is left out); the round builders and checkers (`srcmap/`); the scan, repair and formalization rounds D1002–D1031 with their checks (`D10xx_CHECK.json`, `tmp/d10xx_*`); the GAGA candidate blocks and designs (`tmp/gaga_*`); review tables of the Tôhoku bibliography and pages (`.review-*`) |
| `stacks-ftg-fga-normalized/` | FGA in Stacks format, notation normalized | `codex/fga-notation-sync` at `ad58625` | tip of `history/source/fac-tohoku-gaga` | the FGA source-validation tables (`tmp/fga-source-validation/`) |
| `stacks-ftg-fga-pr/` | FGA in Stacks format, prepared as a pull request | `codex/fga-pr-normalized` at `1b422a9` | tip of `history/source/fga-integration` | nothing beyond the commit (only build outputs and images were local) |
| `stacks-ega/` | EGA in Stacks format: the scaffold of the EGA comparison | `codex/ega-scaffold` at `dc37296` | tip of `history/source/ega-scaffold` | the uncommitted edits to five EGA mapping tables (`ega/dec.csv`, `resid.csv`, `smap.csv`, `tmap.csv`, `topics.csv`), full copies |
| `stacks-project/` | The clone itself; its own checkout was the FGA integration | `codex/fga-integration` at `d3e5349` | ancestor of `history/source/fga-integration` | nothing beyond the commit: its local files are page images and PDFs of the sources, build outputs, and papers by other authors |
| `stacks-fga-micro/` | Micro test of a single fix (FGA) | `codex/fix-picard-base-change-direction` at `77db1c9` | not on GitHub | `unpublished_commits/77db1c93.diff`: base-change direction in the rigidified Picard stack (`quot.tex`, one line) |
| `stacks-tohoku-micro/` | Micro test of a single fix (Tôhoku) | `codex/fix-generator-proof-parenthesis` at `491f999` | not on GitHub | `unpublished_commits/491f9997.diff`: a parenthesis in a generator proof (`injectives.tex`, one line) |
| `stacks-01kr-micro/` | Micro test of a single fix (a separate clone) | `codex/fix-01kr-duplicate-arrow` at `63830cfe` | not on GitHub | `unpublished_commits/63830cfe.diff`: a duplicated arrow in a fibre-product diagram (`schemes.tex`, one line) |

Each `unpublished_commits/*.diff` begins with the commit's hash, parent, date and message, followed by `git diff`
against its parent (`a04446e`). All three corrections are already in the source at the top of this repository
(`quot.tex`, `injectives.tex` and `schemes.tex` read as these fixes do), so the diffs are kept only as a record.

## What was left out

Only our own work files are here. Left out: page images and PDFs of the sources; PDFs, DVI, auxiliary files, TeX and
BibTeX logs and console transcripts, the auto-generated index and text extracted from rendered PDFs (build outputs);
Python caches; archives; papers and TeX sources by other authors (`tmp/refs/`, the SMF TeX of SGA 2, text extracted
from the source PDFs); files identical to the upstream Stacks files at `a04446e`; and files identical to a file
already in this repository (on `main` or another branch). `LEFT_OUT.tsv` counts them by clone and reason.
Also left out: the 94 copies of `stx.csv` in `stacks-ftg` (496 MB; 44 distinct versions, about 5.3 MB each), the
index of every Stacks label and tag with the hash of its text that each source-map round writes again with
`srcmap/scan.py`; `HELD_STX_CSV.tsv` lists each copy with its path, size and git blob hash. `MANIFEST.tsv` lists every file here with its kind (untracked, ignored by `.gitignore`, modified tracked file, commit
diff), size and SHA-256.

## Notes

- Everything here was written by AI (OpenAI Codex models, as for the rest of this repository) or generated by its
  scripts. The checks and reports are the models' own and have not been reviewed by a person.
- In these copies the first name of the user who ran the project is replaced by "user", local paths included. Nothing
  else is changed, so scripts name the local folders they ran in, and a hash recorded in a check file can differ from
  that of the copy here when the copy had such a path rewritten.
- The Stacks text is the work of the Stacks project authors (see [CONTRIBUTORS](../../CONTRIBUTORS)). Like the rest of
  this repository, this modified material is distributed under the GNU Free Documentation License 1.2; see
  [COPYING](../../COPYING).
