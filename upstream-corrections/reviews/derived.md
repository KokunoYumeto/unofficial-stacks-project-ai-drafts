# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## derived

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/derived.patch)

### MC-STK-ERR-0812

`derived.tex` — derived.tex:1340; undefined morphism symbol.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1340) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_wrong_factorization_arrow. Use the triangle arrow u; g is undefined in the proof.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \circ g = a
+i \circ u = a
````

### MC-STK-ERR-0813

`derived.tex` — derived.tex:1423; wrong shifted vertical morphism.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1423) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_wrong_shifted_arrow. Use k[1], induced by the displayed vertical map k : X to X''.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ar[d]^{g[1]}
+\ar[d]^{k[1]}
````

### MC-STK-ERR-0814

`derived.tex` — derived.tex:1445; wrong result type reference.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1445) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_wrong_result_noun. Refer to the enclosing proposition, not a lemma.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-first statement of the lemma
+first statement of the proposition
````

### MC-STK-ERR-0815

`derived.tex` — derived.tex:1521; duplicated copula.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1521) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_duplicated_word. Delete the second occurrence of 'is'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence $S'$ is is a
+Hence $S'$ is a
````

### MC-STK-ERR-0816

`derived.tex` — derived.tex:2061; extraneous auxiliary.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2061) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Delete the auxiliary 'is' before the finite verb 'follows'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-It is also
+It also
````

### MC-STK-ERR-0817

`derived.tex` — derived.tex:2204; missing indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2204) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Insert the article before the singular count noun 'multiplicative system'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-that $S$ is multiplicative system
+that $S$ is a multiplicative system
````

### MC-STK-ERR-0818

`derived.tex` — derived.tex:2361; wrong hom category subscript.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2361) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_category_typing_error. The representable functor is on D, which contains the triangle and G(C).

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Hom_{\mathcal{D}'}(W, -)
+\Hom_{\mathcal{D}}(W, -)
````

### MC-STK-ERR-0819

`derived.tex` — derived.tex:2362; wrong yoneda test category.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2362) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_category_typing_error. The Yoneda test object W lies in D, not D'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$W$ of $\mathcal{D}'$
+$W$ of $\mathcal{D}$
````

### MC-STK-ERR-0820

`derived.tex` — derived.tex:2364; wrong hom category subscripts.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2364) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_category_typing_error. Both Hom sets are computed in D because X and G(C) lie there.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Hom_{\mathcal{D}'}(W, X) \to \Hom_{\mathcal{D}'}(W, G(C))
+\Hom_{\mathcal{D}}(W, X) \to \Hom_{\mathcal{D}}(W, G(C))
````

### MC-STK-ERR-0821

`derived.tex` — derived.tex:2424; malformed definition clause.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2424) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use 'We let ... be' for the definition clause.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We set
+We let
````

### MC-STK-ERR-0822

`derived.tex` — derived.tex:2533; subject verb disagreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2533) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use the singular verb 'shows'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A matrix computation show
+A matrix computation shows
````

### MC-STK-ERR-0823

`derived.tex` — derived.tex:2855; number and article error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2855) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. The displayed object is one termwise split exact sequence.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be termwise split exact sequences as in
+be a termwise split exact sequence as in
````

### MC-STK-ERR-0824

`derived.tex` — derived.tex:3129; missing triangle arrow.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3129) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_incomplete_triangle_tuple. Restore f so the cone triangle is the required sextuple.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(K^\bullet, L^\bullet, C(f), i, p)
+(K^\bullet, L^\bullet, C(f), f, i, p)
````

### MC-STK-ERR-0825

`derived.tex` — derived.tex:3130; missing triangle arrow.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3130) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_incomplete_triangle_tuple. Restore tilde f in the corresponding cone-triangle sextuple.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(K^\bullet, \tilde L^\bullet, C(\tilde f), \tilde i, \tilde p)
+(K^\bullet, \tilde L^\bullet, C(\tilde f), \tilde f, \tilde i, \tilde p)
````

### MC-STK-ERR-0826

`derived.tex` — derived.tex:3422; wrong indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3422) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use 'a' before the consonant-initial phrase 'termwise split injection'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-isomorphic to an termwise split injection
+isomorphic to a termwise split injection
````

### MC-STK-ERR-0827

`derived.tex` — derived.tex:3651; unresolved editorial placeholder.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3651) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_reader_placeholder. Delete the placeholder together with its leading space; the following sentence supplies exact references.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
- (insert future reference here)
````

### MC-STK-ERR-0828

`derived.tex` — derived.tex:3702; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3702) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Insert 'by' in the construction 'denote by X the object'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We denote $H^0 : D(\mathcal{A}) \to \mathcal{A}$ the unique functor
+We denote by $H^0 : D(\mathcal{A}) \to \mathcal{A}$ the unique functor
````

### MC-STK-ERR-0829

`derived.tex` — derived.tex:3968; incomplete participial modifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3968) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Add 'above' to identify the previously defined functor.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-defined has the natural structure
+defined above has the natural structure
````

### MC-STK-ERR-0830

`derived.tex` — derived.tex:4056; article number disagreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4056) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use singular 'sequence' for the one displayed short exact sequence.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be a short exact sequences of complexes
+be a short exact sequence of complexes
````

### MC-STK-ERR-0831

`derived.tex` — derived.tex:4062; wrong noun number.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4062) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r18/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use singular 'sequence' for the one sequence mapped to a triangle.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-maps the short exact sequences
+maps the short exact sequence
````

### MC-STK-ERR-0832

`derived.tex` — derived.tex:4361; stray noun phrase.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4361) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_stray_noun_phrase. The words 'the statement' have no grammatical role in the sentence.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For the last one the statement we have to do a little
+For the last one we have to do a little
````

### MC-STK-ERR-0833

`derived.tex` — derived.tex:5260; missing indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5260) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_missing_indefinite_article. The singular count noun 'quasi-isomorphism' requires an article.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists quasi-isomorphism
+there exists a quasi-isomorphism
````

### MC-STK-ERR-0834

`derived.tex` — derived.tex:5454; singular plural disagreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5454) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_singular_plural_disagreement. The displayed Im(d^0)=Ker(d^1) is a single element of the set under discussion.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is an elements of
+is an element of
````

### MC-STK-ERR-0835

`derived.tex` — derived.tex:5459; wrong morphism property.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5459) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_morphism_property. The stated goal at line 5437 is a quasi-isomorphism and the proof establishes cohomology isomorphisms; a resolution may retain nonzero contractible terms, so a chainwise isomorphism does not follow.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is an isomorphism as desired.
+is a quasi-isomorphism as desired.
````

### MC-STK-ERR-0836

`derived.tex` — derived.tex:5580; missing outer parenthesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5580) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_missing_outer_parenthesis. The cohomology expression opens H^i( but closes only RF(; the outer parenthesis is missing.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^i(RF(A[0]) = 0$
+$H^i(RF(A[0])) = 0$
````

### MC-STK-ERR-0837

`derived.tex` — derived.tex:5922; missing copula.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5922) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_missing_copula. The let-construction requires the infinitive 'be'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We let $D_\mathcal{B}(\mathcal{A})$ the full subcategory
+We let $D_\mathcal{B}(\mathcal{A})$ be the full subcategory
````

### MC-STK-ERR-0838

`derived.tex` — derived.tex:5948; duplicated noun phrase.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5948) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_duplicated_noun_phrase. Each direct summand is the kernel of an idempotent endomorphism of the object H^n(X \oplus Y) in the weak Serre subcategory; 'maps between maps of objects' is malformed.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-kernels of maps between maps of objects
+kernels of maps between objects
````

### MC-STK-ERR-0839

`derived.tex` — derived.tex:6128; extra closing parenthesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6128) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_extra_closing_parenthesis. The displayed inline expression has one unmatched closing parenthesis.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$X, Y \in \Ob(\mathcal{A}))$
+$X, Y \in \Ob(\mathcal{A})$
````

### MC-STK-ERR-0840

`derived.tex` — derived.tex:6197; wrong property name.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6197) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_property_name. The preceding argument has just established faithfulness; fullness is the remaining property to prove.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Fully faithfulness
+Fullness
````

### MC-STK-ERR-0841

`derived.tex` — derived.tex:4727; reversed index arrow.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4727) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_reversed_index_arrow. The definition of Y/S uses arrows out of Y, the diagram labels s' from Y to Y', and the factorization s''=h composed with s' is typed only in that direction.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\{F(Y')\}_{s' : Y' \to Y}$
+$\{F(Y')\}_{s' : Y \to Y'}$
````

### MC-STK-ERR-0842

`derived.tex` — derived.tex:4842; undefined functor.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4842) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_undefined_functor. Only F is defined in the standing situation, and the remainder of the proof uses F restricted to Y/S.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$G|_{Y/S} : Y/S \to \mathcal{D}'$
+$F|_{Y/S} : Y/S \to \mathcal{D}'$
````

### MC-STK-ERR-0843

`derived.tex` — derived.tex:4845; undefined functor.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4845) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_undefined_functor. Only F is defined in the standing situation; lines 4850-4859 confirm the second factor is F restricted to Y/S.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$G|_{Y/S} \circ \text{pr}_2 : X/S \times Y/S \to \mathcal{D}'$
+$F|_{Y/S} \circ \text{pr}_2 : X/S \times Y/S \to \mathcal{D}'$
````

### MC-STK-ERR-0844

`derived.tex` — derived.tex:6297; undefined subscripted object.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6297) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_undefined_subscripted_object. A is embedded in I^0 and d^0 has source I^0; the quotient is I^0/A and I_0 is undefined.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$I_0/A \to I^1$
+$I^0/A \to I^1$
````

### MC-STK-ERR-0845

`derived.tex` — derived.tex:6326,6328,6330,6333,6338; ill typed homotopy indices.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6326-L6338) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_ill_typed_homotopy_indices. The degree-n homotopy identity is alpha^n=d_I^{n-1}h^n+h^{n+1}d_K^n. Five printed h^{n-1} indices are ill-typed, and independent replay additionally found that the first expansion term at line 6328 must be alpha^n rather than alpha^{n-1}.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h^{n - 1}
+h^n
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\alpha^{n - 1}
+\alpha^n
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h^{n - 1}
+h^n
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h^{n - 1}
+h^n
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h^{n - 1}
+h^n
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h^{n - 1}
+h^n
````

### MC-STK-ERR-0846

`derived.tex` — derived.tex:6412,6502; missing complex bullet.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6412-L6502) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_missing_complex_bullet. Both invocations of the make-injective lemma have source the complex K^bullet; plain K is undefined.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\tilde \alpha : K \to \tilde L^\bullet$
+$\tilde \alpha : K^\bullet \to \tilde L^\bullet$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\tilde \alpha : K \to \tilde L^\bullet$
+$\tilde \alpha : K^\bullet \to \tilde L^\bullet$
````

### MC-STK-ERR-0847

`derived.tex` — derived.tex:6532; ill typed homotopy coboundary.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6532) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_ill_typed_homotopy_coboundary. The degree-n coboundary is d_I h^n+h^{n+1}d_L; the printed parentheses produce incompatible summand types.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(d \circ h^n + h^{n + 1}) \circ d
+(d \circ h^n + h^{n + 1} \circ d)
````

### MC-STK-ERR-0848

`derived.tex` — derived.tex:6599-6600; editorial placeholder and dangling conjunction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6599-L6600) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_editorial_placeholder_and_dangling_conjunction. The fourth item is an unresolved authoring placeholder. Deleting it alone would leave the third and final substantive item ending with a dangling ', and', so the exact canon operation also closes that item with a period.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-, and
-\item add more here.
+.
````

### MC-STK-ERR-0849

`derived.tex` — derived.tex:6844,6845; wrong bounded complex category.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6844-L6845) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_bounded_complex_category. The lemma is dual to the bounded-below injective-resolution result. Projective resolutions and all three complexes are bounded above, so both category annotations must be Comp-minus.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $\text{Comp}^{+}(\mathcal{A})$
+of $\text{Comp}^{-}(\mathcal{A})$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-commutative diagram in $\text{Comp}^{+}(\mathcal{A})$
+commutative diagram in $\text{Comp}^{-}(\mathcal{A})$
````

### MC-STK-ERR-0850

`derived.tex` — derived.tex:6962; singular plural disagreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6962) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_singular_plural_disagreement. The singular article and copula require the singular noun 'consequence'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Part (2) is a direct consequences of part (1)
+Part (2) is a direct consequence of part (1)
````

### MC-STK-ERR-0851

`derived.tex` — derived.tex:7113; indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7113) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_indefinite_article. Independent replay confirms the exact bounded correction at 7113.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-There exists a $i \ll 0$
+There exists an $i \ll 0$
````

### MC-STK-ERR-0852

`derived.tex` — derived.tex:7278; malformed hypothesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7278) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_malformed_hypothesis. Independent replay confirms the exact bounded correction at 7278.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Suppose that $\mathcal{A}, \mathcal{B}, \mathcal{C}$ be abelian categories.
+Suppose that $\mathcal{A}, \mathcal{B}, \mathcal{C}$ are abelian categories.
````

### MC-STK-ERR-0853

`derived.tex` — derived.tex:7303,7305; broken display sentence.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7303-L7305) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_broken_display_sentence. Independent replay confirms the exact bounded correction at 7303, 7305.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-t : R(G \circ F) \longrightarrow RG \circ RF.
+t : R(G \circ F) \longrightarrow RG \circ RF
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is isomorphism of functors
+is an isomorphism of functors
````

### MC-STK-ERR-0854

`derived.tex` — derived.tex:7320; unmatched parenthesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7320) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_unmatched_parenthesis. Independent replay confirms the exact bounded correction at 7320.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-G(F(I^\bullet))) \to
+G(F(I^\bullet)) \to
````

### MC-STK-ERR-0855

`derived.tex` — derived.tex:7330,7331; malformed assumption clause.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7330-L7331) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_malformed_assumption_clause. Independent replay confirms the exact bounded correction at 7330, 7331.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-With assumptions as in Lemma \ref{lemma-compose-derived-functors}
+Assume the hypotheses of Lemma \ref{lemma-compose-derived-functors}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and assuming the equivalent conditions (1) and (2) hold.
+and that the equivalent conditions (1) and (2) hold.
````

### MC-STK-ERR-0856

`derived.tex` — derived.tex:7575,7576; ill typed composition and category.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7575-L7576) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_ill_typed_composition_and_category. With i:K->I, a:I->J, and i':K->J, the forced identity is i'=a composed with i in K+(A).

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$i' = i \circ a$
+$i' = a \circ i$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$K^{+}(\mathcal{I})$. Hence
+$K^{+}(\mathcal{A})$. Hence
````

### MC-STK-ERR-0857

`derived.tex` — derived.tex:7396; wrong noun form.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7396) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_noun_form. Independent replay confirms the exact bounded correction at 7396.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Fully faithfulness is a consequence of
+Full faithfulness is a consequence of
````

### MC-STK-ERR-0858

`derived.tex` — derived.tex:7570; wrong functor name.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7570) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_functor_name. Independent replay confirms the exact bounded correction at 7570.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-any two localization functors
+any two resolution functors
````

### MC-STK-ERR-0859

`derived.tex` — derived.tex:7676; wrong verb.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7676) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_verb. Independent replay confirms the exact bounded correction at 7676.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-rests to show that the construction above
+remains to show that the construction above
````

### MC-STK-ERR-0860

`derived.tex` — derived.tex:7759; editorial placeholder.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7759) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_editorial_placeholder. Independent replay confirms the exact bounded correction at 7759.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
-\item Add more here as needed.
````

### MC-STK-ERR-0861

`derived.tex` — derived.tex:7707,7710; misplaced complex decoration.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7707-L7710) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_misplaced_complex_decoration. Independent replay confirms the exact bounded correction at 7707, 7710.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j(K)^\bullet
+j(K^\bullet)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j(L)^\bullet
+j(L^\bullet)
````

### MC-STK-ERR-0862

`derived.tex` — derived.tex:7780; missing terminal punctuation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7780) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_missing_terminal_punctuation. Independent replay confirms the exact bounded correction at 7780.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $\mathcal{A}$ be an abelian category with enough injectives
+Let $\mathcal{A}$ be an abelian category with enough injectives.
````

### MC-STK-ERR-0863

`derived.tex` — derived.tex:7782; reversed functor tuple.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7782) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_reversed_functor_tuple. Independent replay confirms the exact bounded correction at 7782.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $(i, j)$ be a resolution functor
+Let $(j, i)$ be a resolution functor
````

### MC-STK-ERR-0864

`derived.tex` — derived.tex:7978; undefined resolution argument.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7978) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_undefined_resolution_argument. Independent replay confirms the exact bounded correction at 7978.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A[0] \to I^\bullet$ and $C[0] \to J^\bullet$
+$A[0] \to I^\bullet$ and $B[0] \to J^\bullet$
````

### MC-STK-ERR-0865

`derived.tex` — derived.tex:7946,7948; wrong filtered object category.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7946-L7948) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_filtered_object_category. Independent replay confirms the exact bounded correction at 7946, 7948.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{A}$. Denote $d^0$
+$\text{Fil}^f(\mathcal{A})$. Denote $d^0$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a filtered injective object of $\mathcal{A}$
+a filtered injective object of $\text{Fil}^f(\mathcal{A})$
````

### MC-STK-ERR-0866

`derived.tex` — derived.tex:8092; wrong map source.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8092) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_map_source. Independent replay confirms the exact bounded correction at 8092.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$b \oplus c \circ \beta : M \to I^0 \oplus J^0$
+$b \oplus c \circ \beta : B \to I^0 \oplus J^0$
````

### MC-STK-ERR-0867

`derived.tex` — derived.tex:8176; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8176) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_missing_preposition. Independent replay confirms the exact bounded correction at 8176.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\text{Tot}(I^{\bullet, \bullet})$
+Denote by $\text{Tot}(I^{\bullet, \bullet})$
````

### MC-STK-ERR-0868

`derived.tex` — derived.tex:8288,8289; wrong homotopy category.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8288-L8289) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_homotopy_category. Independent replay confirms the exact bounded correction at 8288, 8289.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Hom_{K(\mathcal{A})}(L^\bullet, I^\bullet)
+\Hom_{K(\text{Fil}^f(\mathcal{A}))}(L^\bullet, I^\bullet)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Hom_{K(\mathcal{A})}(K^\bullet, I^\bullet)
+\Hom_{K(\text{Fil}^f(\mathcal{A}))}(K^\bullet, I^\bullet)
````

### MC-STK-ERR-0869

`derived.tex` — derived.tex:8364; possessive typography.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8364) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_possessive_typography. Independent replay confirms the exact bounded correction at 8364.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-if we use a set worth of diagrams
+if we use a set's worth of diagrams
````

### MC-STK-ERR-0870

`derived.tex` — derived.tex:8573; missing copula.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8573) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_missing_copula. Independent replay confirms the exact bounded correction at 8573.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Note that this stupid in the sense that
+Note that this is stupid in the sense that
````

### MC-STK-ERR-0871

`derived.tex` — derived.tex:8603; malformed idiom.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8603) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_malformed_idiom. Independent replay confirms the exact bounded correction at 8603.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-could just have well developed the whole theory
+could just as well have developed the whole theory
````

### MC-STK-ERR-0872

`derived.tex` — derived.tex:8447; wrong singular plural reference noun.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8447) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_singular_plural_reference_noun. Independent replay confirms the exact bounded correction at 8447.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemmas \ref{lemma-injective-acyclic}
+Lemma \ref{lemma-injective-acyclic}
````

### MC-STK-ERR-0873

`derived.tex` — derived.tex:8530,8531; wrong spectral sequence abutment and missing degreewise clause.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8530-L8531) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_spectral_sequence_abutment_and_missing_degreewise_clause. The spectral sequence converges to the graded object R-star; each degree H^n=R^n receives the induced finite filtration.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^n(T(I^\bullet)) = R^nT(K^\bullet)$
+$H^*(T(I^\bullet)) = R^*T(K^\bullet)$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-moreover inducing finite filtrations on each of the terms
+and induces a finite filtration on each $H^n(T(I^\bullet)) = R^nT(K^\bullet)$
````

### MC-STK-ERR-0874

`derived.tex` — derived.tex:8044; wrong cross chapter reference.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8044) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r19/candidate.manifest.json)

Independent canon replay: confirmed_wrong_cross_chapter_reference. The unprefixed label resolves to an unrelated local Derived lemma; the required strictness result is the Homology lemma.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{lemma-filtered-acyclic}
+\ref{homology-lemma-filtered-acyclic}
````

### MC-STK-ERR-0875

`derived.tex` — derived.tex:8739; reversed truncation inequality.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8739) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_reversed_truncation_inequality. After replacing L by its canonical truncation tau_{<=a}L, it vanishes in degrees above a. This upper bound is exactly what makes Y^{i+n} vanish for n < b-a; the printed lower-bound inequality reverses the argument.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$L^i = 0$ for $i < a$
+$L^i = 0$ for $i > a$
````

### MC-STK-ERR-0876

`derived.tex` — derived.tex:9386,9388,9440; reversed colimit map and malformed cohomology map.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9386-L9440) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_reversed_colimit_map_and_malformed_cohomology_map. The displayed quasi-isomorphism must run from P to Q: the following diagram, the finite-stage comparison maps, and the concluding H^i(F(alpha)) map all run from P to Q. The printed display alone reverses the two colimits. This is the second half of the P-to-Q direction correction required by the proof's diagram and conclusion. The printed formula has unbalanced parentheses and applies H^i directly to alpha although the proof concerns F(alpha). Restoring both missing parentheses and F gives the induced cohomology map used to prove F(alpha) is a quasi-isomorphism.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim Q_n^\bullet = Q^\bullet
+P^\bullet = \colim P_n^\bullet
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-P^\bullet = \colim P_n^\bullet
+Q^\bullet = \colim Q_n^\bullet
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^i(\alpha) : H^i(F(P^\bullet) \to H^i(F(Q^\bullet)$
+$H^i(F(\alpha)) : H^i(F(P^\bullet)) \to H^i(F(Q^\bullet))$
````

### MC-STK-ERR-0877

`derived.tex` — derived.tex:9556,9562; wrong localization categories.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9556-L9562) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_localization_categories. The general lemma has no abelian category B. Its Hom set is in the localization (S')^{-1}D', as displayed in the equality being justified. The general lemma has no abelian category A. Its Hom set is in S^{-1}D, as displayed in the equality being justified.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$D(\mathcal{B})$, see Categories, Remark
+$(S')^{-1}\mathcal{D}'$, see Categories, Remark
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $D(\mathcal{A})$, see Categories, Remark
+in $S^{-1}\mathcal{D}$, see Categories, Remark
````

### MC-STK-ERR-0878

`derived.tex` — derived.tex:9993; missing closing parenthesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9993) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_missing_closing_parenthesis. The source omits the closing parenthesis of H^i(RF(tau_{<=a}E)), leaving the displayed morphism malformed.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^i(RF(\tau_{\leq a}E) \to H^i(RF(E))$
+$H^i(RF(\tau_{\leq a}E)) \to H^i(RF(E))$
````

### MC-STK-ERR-0879

`derived.tex` — derived.tex:10017; ill typed maximum scope.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10017) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_ill_typed_maximum_scope. The maximum must be taken over the union of the singleton {0} with the nonvanishing degrees. The printed parentheses instead form max({0}) union a set, which is ill-typed.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$d(A) = \max \{0\} \cup \{i \mid R^iF(A) \not = 0\}$
+$d(A) = \max\bigl(\{0\} \cup \{i \mid R^iF(A) \not = 0\}\bigr)$
````

### MC-STK-ERR-0880

`derived.tex` — derived.tex:10119; missing closing parenthesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10119) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_missing_closing_parenthesis. The dual statement repeats the same missing closing parenthesis, leaving the cohomology morphism malformed.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^i(LF(\tau_{\leq a + n - 1}E) \to H^i(LF(E))$
+$H^i(LF(\tau_{\leq a + n - 1}E)) \to H^i(LF(E))$
````

### MC-STK-ERR-0881

`derived.tex` — derived.tex:10208; ill typed naturality equation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10208) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_ill_typed_naturality_equation. For a morphism of systems a_n: K_n to L_n, the structural square requires a after i_n to equal j_n after a_n. The printed right side j_n alone has domain L_n rather than K_n and is ill-typed.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$a \circ i_n = j_n$
+$a \circ i_n = j_n \circ a_n$
````

### MC-STK-ERR-0882

`derived.tex` — derived.tex:10681; wrong product index.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10681) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_product_index. Here p is the fixed cohomological degree and the product ranges over the tower index n for which the truncation has p-th cohomology. The printed subscript incorrectly makes the fixed p look like the product index.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\prod\nolimits_{p \geq -n} H^p(K)
+\prod\nolimits_{n : p \geq -n} H^p(K)
````

### MC-STK-ERR-0883

`derived.tex` — derived.tex:9709; wrong indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9709) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_indefinite_article. The indefinite article before the consonant sound in complex must be a, not an.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $K^\bullet$ be an complex.
+Let $K^\bullet$ be a complex.
````

### MC-STK-ERR-0884

`derived.tex` — derived.tex:9870; wrong indefinite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9870) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_indefinite_article. The indefinite article before acyclic must be an.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $M^\bullet$ be a acyclic complex of $\mathcal{B}$.
+Let $M^\bullet$ be an acyclic complex of $\mathcal{B}$.
````

### MC-STK-ERR-0885

`derived.tex` — derived.tex:10328; subject verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10328) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_subject_verb_agreement. The plural subject countable direct sums requires the plural verb exist.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then countable direct sums exists and are exact.
+Then countable direct sums exist and are exact.
````

### MC-STK-ERR-0886

`derived.tex` — derived.tex:10541; spelling.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10541) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_spelling. Occurrence is misspelled with two r's in the source.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-where each occurence of $f$ denotes a suitable transition map of
+where each occurrence of $f$ denotes a suitable transition map of
````

### MC-STK-ERR-0887

`derived.tex` — derived.tex:10561; double connector.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10561) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_double_connector. The source combines and with a relative clause introduced by which, leaving an ungrammatical double connector.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-inverse system of complexes and which in particular determines
+inverse system of complexes which in particular determines
````

### MC-STK-ERR-0888

`derived.tex` — derived.tex:10798; subject verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10798) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_subject_verb_agreement. The plural subject objects requires the plural verb consist.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-consists of all objects $F(A)$
+consist of all objects $F(A)$
````

### MC-STK-ERR-0889

`derived.tex` — derived.tex:10872; unbound cohomological index.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10872) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_unbound_cohomological_index. In the base case b-a=0, K has cohomology only in the single degree a. The index i is unbound, while the canonical identification is K isomorphic to H^a(K)[-a].

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^i(K)[-a]$
+$H^a(K)[-a]$
````

### MC-STK-ERR-0890

`derived.tex` — derived.tex:10876; wrong canonical truncation triangle.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10876) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_canonical_truncation_triangle. The proof is in the derived category and requires the canonical truncation triangle. K^b is a term of a chosen complex and is neither intrinsic nor the required one-degree cohomology object.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\tau_{\leq b - 1}K^\bullet \to K^\bullet \to K^b[-b]
+\tau_{\leq b - 1}K \to K \to H^b(K)[-b]
````

### MC-STK-ERR-0891

`derived.tex` — derived.tex:10890; false cohomological bound.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10890) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_false_cohomological_bound. Every shifted generator in E[-m,m] has cohomology in [a-m,b+m], and finite sums, direct summands, and extensions preserve this same interval. Multiplying a and b by the extension length n gives a false bound.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$i \not \in [-m + na, m + nb]$
+$i \not \in [a - m, b + m]$
````

### MC-STK-ERR-0892

`derived.tex` — derived.tex:10913; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10913) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_missing_preposition. The English construction denote an object the name is missing the required preposition by.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\langle E \rangle_1$ the strictly full subcategory
+Denote by $\langle E \rangle_1$ the strictly full subcategory
````

### MC-STK-ERR-0893

`derived.tex` — derived.tex:10966; unmatched bracket.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10966) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_unmatched_bracket. The expression has one unmatched closing square bracket after add(E[-infinity,infinity]).

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-smd(add(E[-\infty, \infty])])
+smd(add(E[-\infty, \infty]))
````

### MC-STK-ERR-0894

`derived.tex` — derived.tex:11003; wrong additive closure subject.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11003) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_additive_closure_subject. The proof checks that the strictly full saturated triangulated subcategory D' is stable under the operations used to generate <E>. The printed inclusion for add(D) is generally false and does not express closure of D'.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$add(\mathcal{D}) \subset \mathcal{D}'$
+$add(\mathcal{D}') \subset \mathcal{D}'$
````

### MC-STK-ERR-0895

`derived.tex` — derived.tex:11258; wrong factorization object prime count.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11258) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_factorization_object_prime_count. The preceding sentence introduces the new factorization object E'''. E'' already denotes the earlier induction object attached to I'', so this occurrence must be E'''.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$E''$ an object of $\langle \bigoplus_{i \in I'''} E_i \rangle$
+$E'''$ an object of $\langle \bigoplus_{i \in I'''} E_i \rangle$
````

### MC-STK-ERR-0896

`derived.tex` — derived.tex:11259; wrong support index prime count.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11259) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_support_index_prime_count. The new object E''' is supported on the newly introduced finite index set I'''. The following union I' union I'' union I''' confirms the required index.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some finite subset $I' \subset I$
+for some finite subset $I''' \subset I$
````

### MC-STK-ERR-0897

`derived.tex` — derived.tex:11309; wrong result type noun.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11309) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_result_type_noun. The enclosing numbered unit is Proposition lemma-compactly-generated-classical-generator, not a lemma.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the lemma is proven
+the proposition is proven
````

### MC-STK-ERR-0898

`derived.tex` — derived.tex:11625; ordinary colimit in place of homotopy colimit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11625) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_ordinary_colimit_in_place_of_homotopy_colimit. The first part of the proof constructs X as the homotopy colimit of the sequence X_n. An ordinary colimit is neither assumed to exist in the triangulated category nor the object constructed there.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\colim X_n = X \to Y$
+$\text{hocolim} X_n = X \to Y$
````

### MC-STK-ERR-0899

`derived.tex` — derived.tex:11744; spelling.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11744) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_spelling. Subcategories is misspelled.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-triangulated subcagories
+triangulated subcategories
````

### MC-STK-ERR-0900

`derived.tex` — derived.tex:11890; spelling.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11890) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_spelling. Inclusion is misspelled.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Since the incusion $\mathcal{A} \subset {}^\perp(\mathcal{A}^\perp)$
+Since the inclusion $\mathcal{A} \subset {}^\perp(\mathcal{A}^\perp)$
````

### MC-STK-ERR-0901

`derived.tex` — derived.tex:12278; wrong primed Postnikov target.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L12278) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_wrong_primed_Postnikov_target. The second arrow is the structure map of the target Postnikov system and therefore lands in X'_n[n]. The next line and the displayed distinguished triangle both use X'_n[n].

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$Y_n[n] \to Y'_n[n] \to X_n[n]$
+$Y_n[n] \to Y'_n[n] \to X'_n[n]$
````

### MC-STK-ERR-0902

`derived.tex` — derived.tex:12551; missing let clause.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L12551) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_missing_let_clause. The displayed subject A_n to B_n is followed by be but lacks the corresponding Let. Joining its introduction to the preceding sentence supplies the missing construction.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $\mathcal{A}$ be an abelian category.
+Let $\mathcal{A}$ be an abelian category and let
````

### MC-STK-ERR-0903

`derived.tex` — derived.tex:12560; subject verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L12560) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r20/candidate.manifest.json)

Independent canon replay: confirmed_subject_verb_agreement. The singular head noun system requires the singular verb defines.

Adverse evidence / qualification: The frozen source and admitted overlay evidence are retained; no translation byte, prior payload, or mutable upstream file was used as correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-define an isomorphism of pro-objects of $\mathcal{A}$
+defines an isomorphism of pro-objects of $\mathcal{A}$
````
