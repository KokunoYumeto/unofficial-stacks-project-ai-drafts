# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## brauer

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/brauer.patch)

### MC-STK-ERR-0016

`brauer.tex` — 711; mechanical spelling error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L711) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: spitting field → splitting field

````diff
--- original
+++ replacement
@@ -1 +1 @@
-spitting field.
+splitting field.
````

### MC-STK-ERR-0017

`brauer.tex` — 733; logical negation error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L733) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r2/candidate.manifest.json)

Reviewed legacy summary: assume no element of K is separable over k → assume no element of K outside k is separable over k

````diff
--- original
+++ replacement
@@ -1 +1 @@
-To get a contradiction assume no element of $K$ is separable over $k$.
+To get a contradiction assume no element of $K$ outside $k$ is separable over $k$.
````

### MC-STK-ERR-0745

`brauer.tex` — brauer.tex:274-276; lemma-matrix-algebras; matrix corner coefficient sets misidentified.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L274-L276) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_typed_matrix_corner_error. Identify the common two-sided ideal through the (i,j)-entry coefficient sets; distinct matrix corners are not equal subsets of the matrix ring and are not themselves ideals of R.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,4 @@
 Part (1) proves itself. If $J \subset R_n$ is a two-sided ideal, then
-$J = \bigoplus e_{ii}Je_{jj}$ and all of the summands $e_{ii}Je_{jj}$ are
-equal to each other and are a two-sided ideal $I$ of $R$. This proves (2).
+$J = \bigoplus e_{ii}Je_{jj}$, and the sets of $(i,j)$-entries occurring
+in $e_{ii}Je_{jj}$ are all equal to a two-sided ideal $I$ of $R$.
+This proves (2).
````

### MC-STK-ERR-0746

`brauer.tex` — brauer.tex:63-64; definition-simple; zero algebra inadvertently simple.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L63-L64) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_definition_domain_error. Require a simple algebra to be nonzero, as the following existence lemma and Wedderburn theorem do; otherwise the zero algebra satisfies the stated ideal condition.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-We say $A$ is {\it simple} if the only two-sided ideals of $A$ are
-$0$ and $A$.
+We say $A$ is {\it simple} if it is nonzero and the only two-sided
+ideals of $A$ are $0$ and $A$.
````

### MC-STK-ERR-0747

`brauer.tex` — brauer.tex:295-296; lemma-simple-module-unique; zero module counterexample to double centralizer.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L295) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_missing_nonzero_hypothesis. Restrict item (6) to nonzero finite modules; for N=0 its endomorphism algebra is zero and End_B(N) cannot recover nonzero A.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For a finite $A$-module $N$
+For a nonzero finite $A$-module $N$
````

### MC-STK-ERR-0748

`brauer.tex` — brauer.tex:512-514; lemma-automorphism-inner; automorphism scope overbroad.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L512-L514) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_automorphism_scope_error. State the Skolem-Noether consequence for k-algebra automorphisms; an ordinary field automorphism of A=k need not be inner.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-Let $A$ be a finite central simple $k$-algebra. Any automorphism of $A$ is
-inner. In particular, any automorphism of $\text{Mat}(n \times n, k)$
-is inner.
+Let $A$ be a finite central simple $k$-algebra. Any $k$-algebra
+automorphism of $A$ is inner. In particular, any $k$-algebra automorphism
+of $\text{Mat}(n \times n, k)$ is inner.
````

### MC-STK-ERR-0749

`brauer.tex` — brauer.tex:570-579; lemma-when-tensor-is-equal; literal equality in place of multiplication isomorphism.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L570) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_equality_type_error. State the natural multiplication map and its isomorphism, matching the proof; the tensor product is not literally the same set as A.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-then $A = B \otimes_k C$ where $C$ is the (central simple)
+then the multiplication map $B \otimes_k C \to A$ is an isomorphism,
+where $C$ is the (central simple)
````

### MC-STK-ERR-0750

`brauer.tex` — brauer.tex:561; theorem-centralizer proof; ungrammatical causal construction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L561) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Remove the extraneous preposition so that the clause has the subject '(2) applied to C subset A'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Part (3) follows because of (2) applied to $C \subset A$ shows
+Part (3) follows because (2) applied to $C \subset A$ shows
````

### MC-STK-ERR-0751

`brauer.tex` — brauer.tex:728; proposition-separable-splitting-field proof; spurious comma after then.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L727-L728) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_punctuation_error. Remove the comma between 'then' and the main clause.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 If the
-ground field $k$ is finite then, the result is clear as well
+ground field $k$ is finite, then the result is clear as well
````

### MC-STK-ERR-0752

`brauer.tex` — brauer.tex:771; lemma-finite-central-simple-algebra; missing indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L771) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r15/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Add the article before the singular predicate noun phrase.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A$ is finite central simple $k$-algebra,
+$A$ is a finite central simple $k$-algebra,
````
