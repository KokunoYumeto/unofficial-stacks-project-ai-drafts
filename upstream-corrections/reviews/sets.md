# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## sets

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sets.patch)

### MC-STK-ERR-0029

`sets.tex` — 993; undefined identifier error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sets.tex#L993) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: bare S_tau → calligraphic S_tau

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\beta_0 = \sup_{T \in S_\tau} \beta(T)$.
+$\beta_0 = \sup_{T \in \mathcal{S}_\tau} \beta(T)$.
````

### MC-STK-ERR-0030

`sets.tex` — 1027-1031;1083-1089; linked recursion clause and free index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sets.tex#L1028-L1088) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: recursive clause (3) takes Cov_{kappa,alpha}; application uses free f(beta + 1) → recursive clause (3) takes Cov_{kappa,f(alpha)}; application uses f(beta(U) + 1)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\in \text{Cov}(\mathcal{C})_{\kappa, \alpha}$
+\in \text{Cov}(\mathcal{C})_{\kappa, f(\alpha)}$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f$ contained in $\text{Cov}(\mathcal{C})_{\kappa, f(\beta + 1)}$
+$f$ contained in $\text{Cov}(\mathcal{C})_{\kappa, f(\beta(\mathcal{U}) + 1)}$
````

### MC-STK-ERR-0031

`sets.tex` — 1092-1104; linked site axiom index and common stage error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sets.tex#L1093-L1102) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: two Cov_{kappa,f(alpha)} inputs, beta < beta_1, and no common-stage bound for outer U → two Cov_{kappa,alpha} inputs, beta < beta_2, and beta increased to bound outer U at Cov_{kappa,f(beta)}

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\in \text{Cov}(\mathcal{C})_{\kappa, f(\alpha)}$
+\in \text{Cov}(\mathcal{C})_{\kappa, \alpha}$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\in \text{Cov}(\mathcal{C})_{\kappa, f(\alpha)}$.
+\in \text{Cov}(\mathcal{C})_{\kappa, \alpha}$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cofinal subset. Hence there exists a $\beta < \beta_1$ such
+cofinal subset. Hence there exists a $\beta < \beta_2$ such
````

````diff
--- original
+++ replacement
@@ -0,0 +1,3 @@
+After increasing $\beta$ to at least $\beta(\mathcal{U})$ if necessary,
+which still leaves $\beta < \beta_2$, we may also assume that
+$\mathcal{U} \in \text{Cov}_{\kappa, f(\beta)}$.
````

### MC-STK-ERR-0032

`sets.tex` — 848; transposed indices error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sets.tex#L848) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: W_{i,a} → W_{a,i}

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\text{size}(\coprod_a \coprod_{i \in I_a} W_{i, a}) \leq \text{size}(X)$
+$\text{size}(\coprod_a \coprod_{i \in I_a} W_{a, i}) \leq \text{size}(X)$
````
