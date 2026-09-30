# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## examples

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/examples.patch)

### MC-STK-ERR-2466

`examples.tex` — 1481; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L1481) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r59/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r59/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and since $z_{j + 1} = x^{-1}z_j - a_j = \ldots = f_j(x, x^{-1}, z)$).
+and since $z_{j + 1} = x^{-1}(z_j - a_j) = \ldots = f_j(x, x^{-1}, z)$).
````
