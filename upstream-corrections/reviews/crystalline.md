# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## crystalline

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/crystalline.patch)

### MC-STK-ERR-0007

`crystalline.tex` — 237; mathematical index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L237) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: t', t in I → t', t in T

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item $x_{t'}^{[m]}(x_t - f_t)$ where $m > 0$ and $t', t \in I$.
+\item $x_{t'}^{[m]}(x_t - f_t)$ where $m > 0$ and $t', t \in T$.
````
