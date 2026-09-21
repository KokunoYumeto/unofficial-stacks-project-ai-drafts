# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## stacks-limits

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/stacks-limits.patch)

### MC-STK-ERR-0018

`stacks-limits.tex` — 83; mathematical base error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L83) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: affine schemes over U → affine schemes over S

````diff
--- original
+++ replacement
@@ -1 +1 @@
-If for every directed limit $U = \lim U_i$ of affine schemes over $U$,
+If for every directed limit $U = \lim U_i$ of affine schemes over $S$,
````

### MC-STK-ERR-0019

`stacks-limits.tex` — 208; undefined morphism error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L208) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: phi : f(x) -> y_i|V → phi : p(x) -> y_i|V

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\{(x, \phi) \mid x \in \Ob(\mathcal{X}_V), \phi : f(x) \to y_i|V\}/\cong
+\{(x, \phi) \mid x \in \Ob(\mathcal{X}_V), \phi : p(x) \to y_i|V\}/\cong
````

### MC-STK-ERR-0020

`stacks-limits.tex` — 440; quotient relation error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L440) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: fibre categories of [U/T] → fibre categories of [U/R]

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in the fibre categories of $[U/T]$ given in
+in the fibre categories of $[U/R]$ given in
````

### MC-STK-ERR-0021

`stacks-limits.tex` — 527; undefined system object error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L527) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: X_i is quasi-compact and quasi-separated → Y_i is quasi-compact and quasi-separated

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We assume that $X_i$ is quasi-compact and quasi-separated for all $i \in I$.
+We assume that $Y_i$ is quasi-compact and quasi-separated for all $i \in I$.
````

### MC-STK-ERR-0022

`stacks-limits.tex` — 702; mechanical spelling error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L702) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: two morpisms → two morphisms

````diff
--- original
+++ replacement
@@ -1 +1 @@
-algebraic spaces of finite type over $Y$. We have two morpisms
+algebraic spaces of finite type over $Y$. We have two morphisms
````

### MC-STK-ERR-0023

`stacks-limits.tex` — 876; number agreement error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L876) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: a proper morphisms → a proper morphism

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Composing these morphisms we obtain a proper morphisms
+Composing these morphisms we obtain a proper morphism
````

### MC-STK-ERR-0024

`stacks-limits.tex` — 881; duplicated copula error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L881) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: this is the morphism is the same as → this morphism is the same as

````diff
--- original
+++ replacement
@@ -1 +1 @@
-shows that this is the morphism is the same as $(s_i, t_i)$
+shows that this morphism is the same as $(s_i, t_i)$
````

### MC-STK-ERR-0025

`stacks-limits.tex` — 912; stack symbol error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L912) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: T' subset |X times_Y Z'| → T' subset |mathcal X times_Y Z'|

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and a closed subset $T' \subset |X \times_Y Z'|$ such that
+and a closed subset $T' \subset |\mathcal{X} \times_Y Z'|$ such that
````

### MC-STK-ERR-0026

`stacks-limits.tex` — 982; fibre product base error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L982) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: |mathcal X times_Y Z| → |mathcal X times_mathcal Y Z|

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the map $|\mathcal{X} \times_Y Z| \to |Z|$ is closed, and
+the map $|\mathcal{X} \times_{\mathcal{Y}} Z| \to |Z|$ is closed, and
````

### MC-STK-ERR-0027

`stacks-limits.tex` — 1054; fibre product base error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L1054) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: mathcal X times_Y V → mathcal X times_mathcal Y V

````diff
--- original
+++ replacement
@@ -1 +1 @@
-If we can show that $\mathcal{X} \times_Y V \to V$ is universally closed,
+If we can show that $\mathcal{X} \times_{\mathcal{Y}} V \to V$ is universally closed,
````

### MC-STK-ERR-0028

`stacks-limits.tex` — 1096-1098; linked diagram ambient space error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-limits.tex#L1096-L1098) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: three mismatched ambient spaces for T, T', and its image → top-left mathcal X; top-right A^n times mathcal X; bottom-right A^n times Y

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-of $|X \times_Y Z|$ is the pullback of a closed subset $T'$ of
-$|\mathbf{A}^n \times Y|$. Since the assumption is that the image
-of $T'$ in $|\mathbf{A}^n \times X|$ is closed we conclude that
+of $|\mathcal{X} \times_Y Z|$ is the pullback of a closed subset $T'$ of
+$|\mathbf{A}^n \times \mathcal{X}|$. Since the assumption is that the image
+of $T'$ in $|\mathbf{A}^n \times Y|$ is closed we conclude that
````
