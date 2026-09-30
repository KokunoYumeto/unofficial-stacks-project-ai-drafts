# Corrections only: review or reuse without adopting this fork

**2,301 effective textual correction units across 38 chapters.**
Download one chapter patch or the combined patch. You do not need to clone this
repository, import its history, or take any of its added theorems.

- [Download all textual corrections as one patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/ALL-TEXTUAL-CORRECTIONS.patch).
- [Download the patch bundle and offline review index](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/corrections-only.zip).
- [Review exact old/new text, reasons and evidence](REVIEW.md).
- [Machine-readable identities and replay results](manifest.json).

## Apply to your own Stacks checkout

The patches target the official Stacks revision
`a04446e57ec1fbc252a871afcec7752fb2807b14`. Later upstream changes have **not** been checked.
Inspect the diff and use the non-mutating check first:

```sh
git apply --stat /path/to/ALL-TEXTUAL-CORRECTIONS.patch
git apply --check /path/to/ALL-TEXTUAL-CORRECTIONS.patch
git apply /path/to/ALL-TEXTUAL-CORRECTIONS.patch
```

Use a chapter filename instead for a smaller batch. Choose the combined patch
**or** chapter patches, not both. Chapter patches touch disjoint files, so they
can be used independently or together. No commit is created automatically.
If a check fails, inspect conflicts or already-fixed passages; do not force it.
To choose smaller pieces, use the unit-by-unit review below and normal diff
editing or interactive staging in your own checkout.

## Choose a chapter

| Chapter | Correction units | Download | Review |
|---|---:|---|---|
| `algebra.tex` | 788 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/algebra.patch) | [entries](reviews/algebra.md) |
| `artin.tex` | 131 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/artin.patch) | [entries](reviews/artin.md) |
| `brauer.tex` | 12 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/brauer.patch) | [entries](reviews/brauer.md) |
| `categories.tex` | 91 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/categories.patch) | [entries](reviews/categories.md) |
| `cohomology.tex` | 5 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/cohomology.patch) | [entries](reviews/cohomology.md) |
| `crystalline.tex` | 1 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/crystalline.patch) | [entries](reviews/crystalline.md) |
| `derham.tex` | 5 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/derham.patch) | [entries](reviews/derham.md) |
| `derived.tex` | 146 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/derived.patch) | [entries](reviews/derived.md) |
| `descent.tex` | 35 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/descent.patch) | [entries](reviews/descent.md) |
| `equiv.tex` | 1 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/equiv.patch) | [entries](reviews/equiv.md) |
| `examples.tex` | 1 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/examples.patch) | [entries](reviews/examples.md) |
| `fields.tex` | 55 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/fields.patch) | [entries](reviews/fields.md) |
| `groupoids.tex` | 48 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/groupoids.patch) | [entries](reviews/groupoids.md) |
| `homology.tex` | 91 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/homology.patch) | [entries](reviews/homology.md) |
| `injectives.tex` | 40 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/injectives.patch) | [entries](reviews/injectives.md) |
| `introduction.tex` | 1 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/introduction.patch) | [entries](reviews/introduction.md) |
| `modules.tex` | 14 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/modules.patch) | [entries](reviews/modules.md) |
| `more-algebra.tex` | 120 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/more-algebra.patch) | [entries](reviews/more-algebra.md) |
| `more-groupoids.tex` | 22 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/more-groupoids.patch) | [entries](reviews/more-groupoids.md) |
| `perfect.tex` | 29 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/perfect.patch) | [entries](reviews/perfect.md) |
| `schemes.tex` | 16 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/schemes.patch) | [entries](reviews/schemes.md) |
| `sets.tex` | 6 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sets.patch) | [entries](reviews/sets.md) |
| `sheaves.tex` | 83 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sheaves.patch) | [entries](reviews/sheaves.md) |
| `simplicial.tex` | 11 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/simplicial.patch) | [entries](reviews/simplicial.md) |
| `sites-cohomology.tex` | 81 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sites-cohomology.patch) | [entries](reviews/sites-cohomology.md) |
| `sites-modules.tex` | 31 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sites-modules.patch) | [entries](reviews/sites-modules.md) |
| `sites.tex` | 136 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sites.patch) | [entries](reviews/sites.md) |
| `smoothing.tex` | 30 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/smoothing.patch) | [entries](reviews/smoothing.md) |
| `spaces-cohomology.tex` | 7 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-cohomology.patch) | [entries](reviews/spaces-cohomology.md) |
| `spaces-duality.tex` | 38 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-duality.patch) | [entries](reviews/spaces-duality.md) |
| `spaces-limits.tex` | 2 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-limits.patch) | [entries](reviews/spaces-limits.md) |
| `spaces-morphisms.tex` | 7 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-morphisms.patch) | [entries](reviews/spaces-morphisms.md) |
| `spaces-perfect.tex` | 20 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-perfect.patch) | [entries](reviews/spaces-perfect.md) |
| `stacks-limits.tex` | 11 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/stacks-limits.patch) | [entries](reviews/stacks-limits.md) |
| `stacks.tex` | 76 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/stacks.patch) | [entries](reviews/stacks.md) |
| `topologies.tex` | 19 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/topologies.patch) | [entries](reviews/topologies.md) |
| `topology.tex` | 90 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/topology.patch) | [entries](reviews/topology.md) |
| `weil.tex` | 1 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/weil.patch) | [entries](reviews/weil.md) |

## What is and is not included

The 2,305 historical IDs in R1–R61 remain accounted for:
2,301 effective textual units are exported; 2 earlier corrections are
superseded by their explicitly recorded replacements, and one fork-specific tag
allocation is excluded. Explicitly classified editorial proof completions remain
available in the full comparison and their candidate packages, but are excluded
from this corrections-only download. No unofficial permanent tags are proposed for upstream.
The original [13-item readable selection](../possible-fixes/README.md) remains available.
13 of those fixes are now included here; 0 remain pending.
Do not apply an individual selection patch again if the combined patch already includes it. Translation
choices, Verdier/FGA/FAC/Pursuing Stacks additions and other new exposition are
excluded. Historical correction evidence remains unchanged.

These are AI-reviewed suggestions already present in our draft, not officially
accepted Stacks errata. Exact replay proves which bytes change, not mathematical
correctness. There is no claim of human review or upstream endorsement.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.
Historical candidate review records retain their original provenance.

Modified Stacks text retains its existing GNU Free Documentation License; see
[COPYING](COPYING). Reproduce or check the export with
`python tools/export_upstream_corrections.py` (or append `--check`) in this repository.
