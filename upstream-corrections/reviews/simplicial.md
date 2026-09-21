# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## simplicial

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/simplicial.patch)

### MC-STK-ERR-0904

`simplicial.tex` — simplicial.tex:277; wrong simplicial map source target.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L277) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_wrong_simplicial_map_source_target. The displayed d_j^2 maps are face maps U_2 to U_1 by the definition at lines 324-325 and the adjacent diagram; U_3 to U_2 is ill-typed.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U_3 \to U_2
+U_2 \to U_1
````

### MC-STK-ERR-0905

`simplicial.tex` — simplicial.tex:510; undefined category symbol.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L510) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_undefined_category_symbol. The standing category is mathcal C throughout the example; plain C is undefined.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$C$
+$\mathcal{C}$
````

### MC-STK-ERR-0906

`simplicial.tex` — simplicial.tex:527; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L527) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_missing_preposition. The English construction is denote by C[n] the cosimplicial set.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we denote $C[n]$ the cosimplicial set
+we denote by $C[n]$ the cosimplicial set
````

### MC-STK-ERR-0907

`simplicial.tex` — simplicial.tex:545; ill typed identity object.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L545) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_ill_typed_identity_object. The composite sigma_i^{n-1} after delta_i^n is an endomorphism of U_{n-1}; its identity cannot be the identity of U_n.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{id}_{U_n}
+\text{id}_{U_{n - 1}}
````

### MC-STK-ERR-0908

`simplicial.tex` — simplicial.tex:546; wrong index and missing terminal case.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L546) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_wrong_index_and_missing_terminal_case. The displayed morphism is indexed by i, not j. For i<n the printed retraction applies; the terminal case i=n uses sigma_{n-1}^{n-1} after delta_n^n.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for $j < n$.
+for $i < n$; for $i = n$ use $\sigma_{n - 1}^{n - 1} \circ \delta^n_n = \text{id}_{U_{n - 1}}$.
````

### MC-STK-ERR-0909

`simplicial.tex` — simplicial.tex:1338; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L1338) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_missing_preposition. The noun phrase requires of before the category.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-simplicial objects $\mathcal{C}$
+simplicial objects of $\mathcal{C}$
````

### MC-STK-ERR-0910

`simplicial.tex` — simplicial.tex:477; wrong cosimplicial map source target.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L477) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_wrong_cosimplicial_map_source_target. The displayed delta_j^2 maps are coface maps U_1 to U_2 by line 428 and the adjacent diagram; U_2 to U_3 is ill-typed.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U_2 \to U_3
+U_1 \to U_2
````

### MC-STK-ERR-0911

`simplicial.tex` — simplicial.tex:1726; unmatched closing parenthesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L1726) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_unmatched_closing_parenthesis. The final Mor term in the aligned equality has one unmatched extra closing parenthesis.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor(X \times \Delta[n] \times (V \amalg_U W), T))
+\Mor(X \times \Delta[n] \times (V \amalg_U W), T)
````

### MC-STK-ERR-0912

`simplicial.tex` — simplicial.tex:1731; wrong pullback operator for pushout.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L1731) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_wrong_pullback_operator_for_pushout. Both maps leave the common U term for the V and W terms, and the next line identifies the construction with V amalg_U W; the operator must be a pushout amalgamation, not a fibre product.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\times_{X \times \Delta[n] \times U}
+\amalg_{X \times \Delta[n] \times U}
````

### MC-STK-ERR-0913

`simplicial.tex` — simplicial.tex:2301; wrong indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L2301) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_wrong_indefinite_article. Final begins with a consonant sound, so the required article is a.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-has an final object
+has a final object
````

### MC-STK-ERR-0914

`simplicial.tex` — simplicial.tex:2762; undefined simplicial set symbol.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/simplicial.tex#L2762) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r21/candidate.manifest.json)

Independent canon replay: confirmed_undefined_simplicial_set_symbol. The proof fixes the simplicial set U and quantifies u in U_i; X is undefined in the lemma, so the degree-one edge lies in U_1.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$i = 1$ and $u \in X_1$
+$i = 1$ and $u \in U_1$
````
