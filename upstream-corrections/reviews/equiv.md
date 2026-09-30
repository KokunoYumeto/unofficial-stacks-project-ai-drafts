# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## equiv

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/equiv.patch)

### MC-STK-ERR-2568

`equiv.tex` — equiv.tex:1836; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/equiv.tex#L1836-L1863) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,3 +1,5 @@
-Since $K$ is perfect, there exist $a \leq b$ such that
-$H^i(X, K)$ is nonzero only for $i \in [a, b]$. Since $X$ is proper,
-each $H^i(X, K)$ is finite dimensional. We conclude that
+Since $K \otimes_{\mathcal{O}_X}^\mathbf{L} \mathcal{E}$ is perfect,
+there exist $a \leq b$ such that its cohomology
+$H^i(X, K \otimes_{\mathcal{O}_X}^\mathbf{L} \mathcal{E})$ is nonzero
+only for $i \in [a, b]$. Since $X$ is proper, each of these groups
+is finite dimensional. We conclude that
````

````diff
--- original
+++ replacement
@@ -1,2 +1,5 @@
-for any $a \leq b$ such that $H^i(X, \mathcal{F})$ is nonzero only
-for $i \in [a, b]$. Thus we can take $a = 0$ and $b = \dim(X)$.
+for any $a \leq b$ such that
+$H^i(X, \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{E})$
+is nonzero only for $i \in [a, b]$, where $\mathcal{E}$ is the
+finite locally free module chosen in the preceding proof.
+Thus we can take $a = 0$ and $b = \dim(X)$.
````
