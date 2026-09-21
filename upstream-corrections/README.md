# Corrections only: review or reuse without adopting this fork

**1,302 effective textual correction units across 30 chapters.**
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
| `algebra.tex` | 218 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/algebra.patch) | [entries](REVIEW.md#algebra) |
| `artin.tex` | 131 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/artin.patch) | [entries](REVIEW.md#artin) |
| `brauer.tex` | 10 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/brauer.patch) | [entries](REVIEW.md#brauer) |
| `categories.tex` | 8 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/categories.patch) | [entries](REVIEW.md#categories) |
| `cohomology.tex` | 4 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/cohomology.patch) | [entries](REVIEW.md#cohomology) |
| `crystalline.tex` | 1 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/crystalline.patch) | [entries](REVIEW.md#crystalline) |
| `derived.tex` | 92 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/derived.patch) | [entries](REVIEW.md#derived) |
| `descent.tex` | 35 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/descent.patch) | [entries](REVIEW.md#descent) |
| `fields.tex` | 8 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/fields.patch) | [entries](REVIEW.md#fields) |
| `groupoids.tex` | 48 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/groupoids.patch) | [entries](REVIEW.md#groupoids) |
| `homology.tex` | 59 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/homology.patch) | [entries](REVIEW.md#homology) |
| `injectives.tex` | 40 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/injectives.patch) | [entries](REVIEW.md#injectives) |
| `modules.tex` | 14 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/modules.patch) | [entries](REVIEW.md#modules) |
| `more-algebra.tex` | 116 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/more-algebra.patch) | [entries](REVIEW.md#more-algebra) |
| `more-groupoids.tex` | 22 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/more-groupoids.patch) | [entries](REVIEW.md#more-groupoids) |
| `perfect.tex` | 24 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/perfect.patch) | [entries](REVIEW.md#perfect) |
| `sets.tex` | 4 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sets.patch) | [entries](REVIEW.md#sets) |
| `sheaves.tex` | 71 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sheaves.patch) | [entries](REVIEW.md#sheaves) |
| `simplicial.tex` | 11 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/simplicial.patch) | [entries](REVIEW.md#simplicial) |
| `sites-cohomology.tex` | 80 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sites-cohomology.patch) | [entries](REVIEW.md#sites-cohomology) |
| `sites-modules.tex` | 31 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sites-modules.patch) | [entries](REVIEW.md#sites-modules) |
| `sites.tex` | 107 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sites.patch) | [entries](REVIEW.md#sites) |
| `smoothing.tex` | 30 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/smoothing.patch) | [entries](REVIEW.md#smoothing) |
| `spaces-cohomology.tex` | 7 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-cohomology.patch) | [entries](REVIEW.md#spaces-cohomology) |
| `spaces-duality.tex` | 38 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-duality.patch) | [entries](REVIEW.md#spaces-duality) |
| `spaces-morphisms.tex` | 7 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-morphisms.patch) | [entries](REVIEW.md#spaces-morphisms) |
| `spaces-perfect.tex` | 19 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-perfect.patch) | [entries](REVIEW.md#spaces-perfect) |
| `stacks-limits.tex` | 11 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/stacks-limits.patch) | [entries](REVIEW.md#stacks-limits) |
| `topologies.tex` | 19 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/topologies.patch) | [entries](REVIEW.md#topologies) |
| `topology.tex` | 37 | [patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/topology.patch) | [entries](REVIEW.md#topology) |

## What is and is not included

The 1,304 historical IDs in R1–R48 remain accounted for:
1,302 effective textual units are exported; one earlier correction was
superseded by its explicitly recorded replacement, and one fork-specific tag
allocation is excluded. No unofficial permanent tags are proposed for upstream.
The 13 [additional possible-fix proposals](../possible-fixes/README.md) are a
separate, not-yet-composed set and are not silently included here. Translation
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
