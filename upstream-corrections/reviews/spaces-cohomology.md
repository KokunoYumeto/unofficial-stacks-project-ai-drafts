# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## spaces-cohomology

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-cohomology.patch)

### MC-STK-ERR-0009

`spaces-cohomology.tex` — 320; mathematical object error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-cohomology.tex#L320) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: Z -> X → X -> Y

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then $Z \to X$ is a finite morphism of schemes and the result is
+Then $X \to Y$ is a finite morphism of schemes and the result is
````

### MC-STK-ERR-0010

`spaces-cohomology.tex` — 376; mathematical subscript error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-cohomology.tex#L376) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: B_xbar → B_ybar

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes_{\mathcal{B}_{\overline{x}}}
+\otimes_{\mathcal{B}_{\overline{y}}}
````

### MC-STK-ERR-0011

`spaces-cohomology.tex` — 384; mathematical morphism type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-cohomology.tex#L384) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: closed immersion → finite morphism

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the behaviour of stalks under pushforward along a closed immersion
+the behaviour of stalks under pushforward along a finite morphism
````

### MC-STK-ERR-0012

`spaces-cohomology.tex` — 564; mathematical case error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-cohomology.tex#L564) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: h_{u'} → h_{U'}

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such that the map $h_{U''}^\# \to h_U^\# \times h_{u'}^\#$ is
+such that the map $h_{U''}^\# \to h_U^\# \times h_{U'}^\#$ is
````

### MC-STK-ERR-0013

`spaces-cohomology.tex` — 615; mathematical argument omission.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-cohomology.tex#L615) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: the sheaf f_! is → the sheaf f_!G is

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the sheaf $f_!$ is the sheafification of the presheaf
+the sheaf $f_!\mathcal{G}$ is the sheafification of the presheaf
````

### MC-STK-ERR-0014

`spaces-cohomology.tex` — 1032; tex typography.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-cohomology.tex#L1032) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: Z(chi_p)) → Z(chi_p)

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{G} \otimes_\mathbf{Z} \underline{\mathbf{Z}}(\chi_p))$
+\mathcal{G} \otimes_\mathbf{Z} \underline{\mathbf{Z}}(\chi_p)$
````

### MC-STK-ERR-0015

`spaces-cohomology.tex` — 1033; mathematical category error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-cohomology.tex#L1033) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: Ab(U_p) → Ab(U_{p,etale})

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is an auto-equivalence of $\textit{Ab}(U_p)$, whence transforms injective
+is an auto-equivalence of $\textit{Ab}(U_{p, \etale})$, whence transforms injective
````
