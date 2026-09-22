# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## derham

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/derham.patch)

### MC-STK-ERR-1569

`derham.tex` — 459; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derham.tex#L459) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/candidate.manifest.json)

The singular noun phrase 'a Cartan-Eilenberg resolution' requires the finite verb 'exists'. The cited lemma itself asserts existence of such a resolution for a bounded below complex in an abelian category with enough injectives; the de Rham complex starts in degree zero. Adding s preserves that assertion and its citation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist a Cartan-Eilenberg resolution for $\Omega^\bullet_{X/S}$.
+there exists a Cartan-Eilenberg resolution for $\Omega^\bullet_{X/S}$.
````

### MC-STK-ERR-1570

`derham.tex` — 540; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derham.tex#L540) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/candidate.manifest.json)

The article a cannot govern the plural noun sheaves across the line break. Removing a preserves the printed plural and the preceding indexed family of cohomology sheaves.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then the sheaves $\mathcal{H}^q$ are computable (in terms of a certain
+then the sheaves $\mathcal{H}^q$ are computable (in terms of certain
````

### MC-STK-ERR-1571

`derham.tex` — 592, 594, 596; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derham.tex#L592-L596) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/candidate.manifest.json)

Each upper-row term has exactly one literal opening parenthesis and two closing parentheses; the sigma subscript is delimited by braces. Deleting the second closing parenthesis is sufficient and leaves all mathematical tokens and diagram arrows intact.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H^n(X, \sigma_{\geq i}\Omega^\bullet_{X/S}))
+H^n(X, \sigma_{\geq i}\Omega^\bullet_{X/S})
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H^m(X, \sigma_{\geq j}\Omega^\bullet_{X/S}))
+H^m(X, \sigma_{\geq j}\Omega^\bullet_{X/S})
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H^{n + m}(X, \sigma_{\geq i + j}\Omega^\bullet_{X/S})) \ar[d] \\
+H^{n + m}(X, \sigma_{\geq i + j}\Omega^\bullet_{X/S}) \ar[d] \\
````

### MC-STK-ERR-1572

`derham.tex` — 729; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derham.tex#L729) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/candidate.manifest.json)

Locally bounded is a predicative adjective phrase for the already specified complex. Deleting the article completes the sentence without adding mathematical content.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Also, observe that $\Omega^\bullet_{X/S}$ is a locally bounded. Thus
+Also, observe that $\Omega^\bullet_{X/S}$ is locally bounded. Thus
````

### MC-STK-ERR-1573

`derham.tex` — 730; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derham.tex#L730) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r49/candidate.manifest.json)

The sentence 'Thus the result by Lemma ... and ...' lacks a finite verb. Inserting follows before the existing by states the already intended inference and preserves both references.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the result by Lemma \ref{lemma-de-rham-complex-product} and
+the result follows by Lemma \ref{lemma-de-rham-complex-product} and
````
