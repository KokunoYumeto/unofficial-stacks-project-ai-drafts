# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## weil

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/weil.patch)

### MC-STK-ERR-2504

`weil.tex` — weil.tex:1712; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/weil.tex#L1712-L1721) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r60/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r60/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H^*(X) \otimes F[-2d] = G(h(X)(d)) \longrightarrow G(\mathbf{1}) = F
+H^*(X) \otimes F[2d] = G(h(X)(d)) \longrightarrow G(\mathbf{1}) = F
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$G(h(X)(d)) = H^*(X) \otimes F[-2d]$ is a left dual to
+$G(h(X)(d)) = H^*(X) \otimes F[2d]$ is a left dual to
````
