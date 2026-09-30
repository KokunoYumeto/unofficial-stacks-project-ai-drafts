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

### MC-STK-ERR-2506

`derived.tex` — derived.tex:737; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L737) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is the isomorphic
+is isomorphic
````

### MC-STK-ERR-2507

`derived.tex` — derived.tex:893; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L893-L898) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Let $F : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
+Let $(F, \xi) : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
 pre-triangulated categories. Since
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(F(0), F(0), F(0), 1_{F(0)}, 1_{F(0)}, F(0))
+(F(0), F(0), F(0), 1_{F(0)}, 1_{F(0)}, \xi_0 \circ F(0))
````

### MC-STK-ERR-2508

`derived.tex` — derived.tex:917; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L917-L920) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $F : \mathcal{D} \to \mathcal{D}'$ be a fully faithful exact functor
+Let $(F, \xi) : \mathcal{D} \to \mathcal{D}'$ be a fully faithful exact functor
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(F(X), F(Y), F(Z), F(f), F(g), F(h))$ is distinguished in $\mathcal{D}'$.
+$(F(X), F(Y), F(Z), F(f), F(g), \xi_X \circ F(h))$ is distinguished in $\mathcal{D}'$.
````

### MC-STK-ERR-2509

`derived.tex` — derived.tex:1011; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1011) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(G(A), G(B), G(C), a, b, \delta)$ is
+$(G(A), G(B), G(C), G(a), G(b), \delta)$ is
````

### MC-STK-ERR-2510

`derived.tex` — derived.tex:1049; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1049-L1050) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-Moreover, each of the rows and columns are
-distinguished triangles. Finally,
+Moreover, each of the first three rows and columns is a
+distinguished triangle. The bottom row and right column become distinguished
+triangles after negating their last arrows. Finally,
````

### MC-STK-ERR-2511

`derived.tex` — derived.tex:1068; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1068-L1069) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-The conclusion of our application TR4
-are that
+The conclusion of our application of TR4
+is that
````

### MC-STK-ERR-2512

`derived.tex` — derived.tex:1080; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1080-L1081) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-$(X, X', X'') \to (X, Y', A)$ and $(X, Y', A) \to (Y, Y', Y'')$.
+$(X, X', X'') \to (X, Y', A)$ and $(X, Y', A) \to (Y, Y', Y'')$
 are morphisms
````

### MC-STK-ERR-2513

`derived.tex` — derived.tex:1365; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1365) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-the localization functor $Q : \mathcal{D} \to S^{-1}\mathcal{D}$ is exact.
+the localization functor $Q : \mathcal{D} \to S^{-1}\mathcal{D}$ is exact
+with the identity translation comparison.
````

### MC-STK-ERR-2514

`derived.tex` — derived.tex:1787; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1787-L1803) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Let $F : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
+Let $(F, \xi) : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
 pre-triangulated categories. Let $\mathcal{D}''$ be the full subcategory
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(F(X), F(Y), F(Z), F(f), F(g), F(h))$ is distinguished.
+$(F(X), F(Y), F(Z), F(f), F(g), \xi_X \circ F(h))$ is distinguished.
````

### MC-STK-ERR-2515

`derived.tex` — derived.tex:1976; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L1976) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-are stable under translations
+are stable under translations.
````

### MC-STK-ERR-2516

`derived.tex` — derived.tex:2535; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2535) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-p_2 \circ c = a \circ p_1
+p_2 \circ c = a[1] \circ p_1
````

### MC-STK-ERR-2517

`derived.tex` — derived.tex:2934; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L2934-L2937) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,4 +1,7 @@
-In other words, we have
-$\Im(b^n) \subset \Im(A_2^n \to B_2^n)$ and
-$\Ker((b')^n) \supset \Im(A_2^n \to B_2^n)$.
-Then $b' \circ b = 0$ as a map of complexes.
+Writing $\alpha_2 : A_2^\bullet \to B_2^\bullet$ and
+$\beta_2 : B_2^\bullet \to C_2^\bullet$ for the maps in the middle
+split sequence, we have $\beta_2 \circ b = 0$ and
+$b' \circ \alpha_2 = 0$. Choose its degreewise retractions
+$\pi_2^n : B_2^n \to A_2^n$. The splitting identities give
+$b^n = \alpha_2^n \circ \pi_2^n \circ b^n$, so
+$(b')^n \circ b^n = 0$ in every degree.
````

### MC-STK-ERR-2518

`derived.tex` — derived.tex:3292; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3292-L3293) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-are compatible with the chosen splittings and hence
-define morphisms of triangles
+define morphisms of triangles in $K(\mathcal{A})$
+(the boundary squares commute up to homotopy)
````

### MC-STK-ERR-2519

`derived.tex` — derived.tex:3306; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3306) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of the bottom split sequence in the diagram provides a splitting
+of the bottom split sequence in the diagram provide a splitting
````

### MC-STK-ERR-2520

`derived.tex` — derived.tex:3350; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3350) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Precomposing the previous isomorphism of triangles with $-1$ on $Y$
+Precomposing the previous isomorphism of triangles with $-1$ on $X$
````

### MC-STK-ERR-2521

`derived.tex` — derived.tex:3396; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3396) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-bounded (above, below) is bounded (above, below).
+bounded (above, below) complexes is bounded (above, below).
````

### MC-STK-ERR-2522

`derived.tex` — derived.tex:3572; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L3572-L3575) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-$\text{Comp}(\mathcal{A}) \to \text{DoubleComp}(\mathcal{C})$,
+$\text{Comp}(\mathcal{B}) \to \text{DoubleComp}(\mathcal{C})$,
 $Y^\bullet \mapsto X^\bullet \otimes Y^\bullet$ and
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-$\text{Comp}(\mathcal{B}) \to \text{DoubleComp}(\mathcal{C})$,
+$\text{Comp}(\mathcal{A}) \to \text{DoubleComp}(\mathcal{C})$,
 $X^\bullet \mapsto X^\bullet \otimes Y^\bullet$
````

### MC-STK-ERR-2523

`derived.tex` — derived.tex:4379; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4379) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such that $\text{gr}(X) \in D^b(\mathcal{A})$.
+such that $\text{gr}(X) \in D^b(\text{Gr}(\mathcal{A}))$.
````

### MC-STK-ERR-2524

`derived.tex` — derived.tex:4792; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4792-L4794) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
+\Mor_{\mathcal{D}'}(W, C)
+\longrightarrow
 \colim_\mathcal{I} \Mor_{\mathcal{D}'}(W, F(Z''))
-\longrightarrow
-\Mor_{\mathcal{D}'}(W, C)
````

### MC-STK-ERR-2525

`derived.tex` — derived.tex:4891; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4891) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The proof of the corresponding statements for $LF$ are dual.
+The proof of the corresponding statements for $LF$ is dual.
````

### MC-STK-ERR-2526

`derived.tex` — derived.tex:4933; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4933-L4967) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The fully faithfulness in (6) follows from (3) and
+The full faithfulness in (6) follows from (3) and
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We say $F$ is {\it right derivable}, or that $RF$ {\it everywhere defined}
+We say $F$ is {\it right derivable}, or that $RF$ is {\it everywhere defined}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We say $F$ is {\it left derivable}, or that $LF$ {\it everywhere defined}
+We say $F$ is {\it left derivable}, or that $LF$ is {\it everywhere defined}
````

### MC-STK-ERR-2527

`derived.tex` — derived.tex:4982; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L4982-L4983) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-In fact, it might happen that the canonical map
-$F(X) \to RF(X)$ is never an isomorphism.
+The canonical map
+$F(X) \to RF(X)$ need not be an isomorphism for a given $X$.
````

### MC-STK-ERR-2528

`derived.tex` — derived.tex:5056; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5056-L5065) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-\Hom_{\mathcal{D}'}(F(X \oplus Y), W)
+\Hom_{\mathcal{D}'}(W, F(X \oplus Y))
 \longrightarrow
-\colim_{s : X \to X', s' : Y \to Y'} \Hom_{\mathcal{D}'}(F(X' \oplus Y'), W)
+\colim_{s : X \to X', s' : Y \to Y'} \Hom_{\mathcal{D}'}(W, F(X' \oplus Y'))
````

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-\Hom_{\mathcal{D}'}(F(X), W)
+\Hom_{\mathcal{D}'}(W, F(X))
 \longrightarrow
-\colim_{s : X \to X'} \Hom_{\mathcal{D}'}(F(X'), W)
+\colim_{s : X \to X'} \Hom_{\mathcal{D}'}(W, F(X'))
````

### MC-STK-ERR-2529

`derived.tex` — derived.tex:5515; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5515) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence in the category $K^\bullet/\text{Qis}^{+}(\mathcal{A})$ the
+Hence in the category $K^\bullet/\text{Qis}(\mathcal{A})$ the
````

### MC-STK-ERR-2530

`derived.tex` — derived.tex:5826; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5826) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item If every object of $\mathcal{A}$ is quotient of
+\item If every object of $\mathcal{A}$ is a quotient of
````

### MC-STK-ERR-2531

`derived.tex` — derived.tex:5856; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5856-L5877) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,22 +1,8 @@
-Say $I^n = 0$ for $n < n_0$. Setting $J^n = \Im(d^n)$ we break
-$I^\bullet$ into short exact sequences
-$0 \to J^n \to I^{n + 1} \to J^{n + 1} \to 0$
-for $n \geq n_0$. These sequences induce distinguished triangles
-$(J^n, I^{n + 1}, J^{n + 1})$ in $D^+(\mathcal{A})$ by
-Lemma \ref{lemma-derived-canonical-delta-functor}.
-For each $k \in \mathbf{Z}$ denote $H_k$ the assertion:
-For all $n \leq k$ the object $J^n$ is in $\mathcal{I}$.
-Then $H_k$ holds trivially for $k < n_0$. If $H_n$ holds,
-then Lemma \ref{lemma-2-out-of-3-computes} shows that
-$J^{n + 1}$ is in $\mathcal{I}$ and we have $H_{n + 1}$.
-By Proposition \ref{proposition-derived-functor} we have a
-distinguished triangle $(RF(J^n), RF(I^{n + 1}), RF(J^{n + 1}))$.
-Since $J^n, I^{n + 1}, J^{n + 1}$ are in $\mathcal{I}$
-the long exact cohomology sequence
-(\ref{equation-long-exact-cohomology-sequence-D})
-associated to this distinguished triangle collapses
-to an exact sequence
-$$
-0 \to F(J^n) \to F(I^{n + 1}) \to F(J^{n + 1}) \to 0
-$$
-This in turn proves that $F(I^\bullet)$ is exact.
+Since $I^\bullet$ is acyclic, it is isomorphic to zero in
+$D^+(\mathcal{A})$. The right derived functor is defined at zero,
+with value zero, and hence at $I^\bullet$, with value zero, by
+Lemma \ref{lemma-derived-inverts}.
+The complex $I^\bullet$ is bounded below and all its terms are
+right $F$-acyclic. Thus Lemma \ref{lemma-leray-acyclicity} shows that
+$F(I^\bullet) \to RF(I^\bullet)$ is an isomorphism.
+Consequently $F(I^\bullet)$ is acyclic.
````

### MC-STK-ERR-2532

`derived.tex` — derived.tex:6063; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6063-L6064) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-t_{-2}
+t^{-2}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-g_{-2}
+g^{-2}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-t_{-1}
+t^{-1}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-g_{-1}
+g^{-1}
````

### MC-STK-ERR-2533

`derived.tex` — derived.tex:6118; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6118-L6128) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,8 @@
 Lemma \ref{lemma-derived-of-quotient}.
+Apply $u$ termwise to complexes. If $s$ is a quasi-isomorphism,
+then the cohomology of the cone of $u(s)$ lies in $\mathcal{B}$,
+because $vu$ is naturally isomorphic to the identity.
+Thus this construction sends quasi-isomorphisms to isomorphisms
+after passing to $D(\mathcal{A})/D_\mathcal{B}(\mathcal{A})$,
+and induces a functor from $D(\mathcal{A}/\mathcal{B})$ to this quotient.
 For an object
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$X, Y \in \Ob(\mathcal{A}))$
+$X, Y \in \Ob(D(\mathcal{A}))$
````

### MC-STK-ERR-2534

`derived.tex` — derived.tex:6524; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6524-L6527) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-d \circ (h_1^n - h_2^n) + (h_1^{n + 1} - h_2^{n + 1}) \circ d
+d \circ (h_2^n - h_1^n) + (h_2^{n + 1} - h_1^{n + 1}) \circ d
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-equals $h_1^n - h_2^n$ on the first summand
+equals $h_2^n - h_1^n$ on the first summand
````

### MC-STK-ERR-2535

`derived.tex` — derived.tex:6543; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6543-L6824) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $I^\bullet$ be bounded below complex consisting of injective
+Let $I^\bullet$ be a bounded below complex consisting of injective
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $P^\bullet$ be bounded above complex consisting of projective
+Let $P^\bullet$ be a bounded above complex consisting of projective
````

### MC-STK-ERR-2536

`derived.tex` — derived.tex:7248; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7248-L7249) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the differential of the complex $H^p_I(I^{\bullet, \bullet})$
+the differential of the complex $H^q_I(I^{\bullet, \bullet})$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-which is an injective resolution of $H^p(K^\bullet)$. Hence the
+which is an injective resolution of $H^q(K^\bullet)$. Hence the
````

### MC-STK-ERR-2537

`derived.tex` — derived.tex:7311; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7311) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$t$ on $RF(I) = F(I)$. Conversely, assume (1) holds.
+$t$ at $I[0]$, using $RF(I[0]) = F(I)[0]$. Conversely, assume (1) holds.
````

### MC-STK-ERR-2538

`derived.tex` — derived.tex:7906; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L7906) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The pushout $f' : I \to I \amalg_A B$ of $f$ by $u$ is a strict
+The pushout $f' : I \to I \amalg_A B$ of $u$ by $f$ is a strict
````

### MC-STK-ERR-2539

`derived.tex` — derived.tex:8826; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8826-L8997) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
+Here $f^{-i} = \text{id}_A$ and all other components of $f$ are zero.
 We call $\delta(E) = fs^{-1}$ the {\it class} of the Yoneda extension.
````

````diff
--- original
+++ replacement
@@ -1,14 +1,17 @@
-can be described in terms of Yoneda extensions as follows: the
-composition of
+can be described in terms of Yoneda extensions as follows. Let
 $$
-0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to B \to 0
+E : 0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to B \to 0
 $$
 and
 $$
-0 \to B \to Z'_{j - 1} \to Z'_{j - 2} \to \ldots \to Z'_0 \to C \to 0
+E' : 0 \to B \to Z'_{j - 1} \to Z'_{j - 2} \to \ldots \to Z'_0 \to C \to 0
 $$
-is the Yoneda extension
+be given. With the projection convention for $\delta$ above, their
+composition $\delta(E)[j] \circ \delta(E')$ equals
+$(-1)^{ij}\delta(S)$, where
 $$
-0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to 
+S : 0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to
 Z'_{j - 1} \to Z'_{j - 2} \to \ldots \to Z'_0 \to C \to 0
 $$
+is the spliced extension; its joining arrow is the composition
+$Z_0 \to B \to Z'_{j - 1}$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then $\delta(E)$ is the composition of $\delta(E')$ and $\delta(E'')$
+Then $\delta(E) = (-1)^{p(i - p)}\delta(E'')[p] \circ \delta(E')$,
````

### MC-STK-ERR-2540

`derived.tex` — derived.tex:8913; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8913-L8915) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-\Ext^j_\mathcal{A}(B, C) \times \Ext^i_\mathcal{A}(A, B)
+\Ext^i_\mathcal{A}(B, A) \times \Ext^j_\mathcal{A}(C, B)
 \longrightarrow
-\Ext^{i + j}_\mathcal{A}(A, C)
+\Ext^{i + j}_\mathcal{A}(C, A)
````

### MC-STK-ERR-2541

`derived.tex` — derived.tex:8990; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8990-L8996) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-For $i > p$ write any class $\xi$ as $\delta(E)$
+If $p = 0$, then $\Hom_\mathcal{A}(A, A) = 0$ for every object $A$.
+Thus $\text{id}_A = 0$, every object is zero, and the conclusion follows.
+Assume $p \geq 1$. For $i > p$ write any class $\xi$ as $\delta(E)$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Set $C = \Ker(Z_{p - 1} \to Z_{p - 2}) = \Im(Z_p \to Z_{p - 1})$.
+Set $C = \Im(Z_p \to Z_{p - 1})$.
````

### MC-STK-ERR-2542

`derived.tex` — derived.tex:9067; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9067) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as follows. Take the free abelian group on the objects on $\mathcal{D}$
+as follows. Take the free abelian group on the objects of $\mathcal{D}$
````

### MC-STK-ERR-2543

`derived.tex` — derived.tex:9712; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9712-L9732) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-\prod\nolimits_b \Hom(K^{-b}, I^{b - 1}) \to
-\prod\nolimits_b \Hom(K^{-b}, I^b) \to
-\prod\nolimits_b \Hom(K^{-b}, I^{b + 1})
+\prod\nolimits_b \Hom(K^b, I^{b - 1}) \to
+\prod\nolimits_b \Hom(K^b, I^b) \to
+\prod\nolimits_b \Hom(K^b, I^{b + 1})
````

````diff
--- original
+++ replacement
@@ -1 +1,6 @@
-in the middle. Similarly, the complex
+in the middle. Here these are the degrees $-1,0,1$ of the full Hom complex,
+with $C^r = \prod_b \Hom(K^b, I^{b + r})$ and
+$(d_C^r f)^b = d_I^{b + r}f^b - (-1)^r f^{b + 1}d_K^b$.
+Its degree $r$ cohomology is
+$\Hom_{K(\mathcal{A})}(K^\bullet, I^\bullet[r])$.
+Similarly, the complex
````

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-\prod\nolimits_b \Hom(K^{-b}, I_t^{b - 1}) \to
-\prod\nolimits_b \Hom(K^{-b}, I_t^b) \to
-\prod\nolimits_b \Hom(K^{-b}, I_t^{b + 1})
+\prod\nolimits_b \Hom(K^b, I_t^{b - 1}) \to
+\prod\nolimits_b \Hom(K^b, I_t^b) \to
+\prod\nolimits_b \Hom(K^b, I_t^{b + 1})
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-$\Hom_{K(\mathcal{A})}(K^\bullet, I_t^\bullet) = 0$, hence
+$\Hom_{K(\mathcal{A})}(K^\bullet, I_t^\bullet[r]) = 0$
+for every integer $r$, hence
````

### MC-STK-ERR-2544

`derived.tex` — derived.tex:9909; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9909-L9918) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,10 +1,11 @@
+Choose an integer $a$ such that $d(K^n) < \infty$ for all $n < a$.
 By Lemma \ref{lemma-subcategory-right-resolution} we can find a
-quasi-isomorphism $\sigma_{\geq 0}K^\bullet \to M^\bullet$ with
-$M^n = 0$ for $n < 0$ and $d(M^n) = 0$ for $n \geq 0$. Then $K^\bullet$
+quasi-isomorphism $\sigma_{\geq a}K^\bullet \to M^\bullet$ with
+$M^n = 0$ for $n < a$ and $d(M^n) = 0$ for $n \geq a$. Then $K^\bullet$
 is quasi-isomorphic to the complex
 $$
-\ldots \to K^{-2} \to K^{-1} \to M^0 \to M^1 \to \ldots
+\ldots \to K^{a - 2} \to K^{a - 1} \to M^a \to M^{a + 1} \to \ldots
 $$
-Hence we may assume that $d(K^n) = 0$ for $n \gg 0$. Note that
-the condition $n + d(K^n) \to -\infty$ as $n \to -\infty$ is not
-violated by this replacement.
+Hence we may assume that every $d(K^n)$ is finite and that
+$d(K^n) = 0$ for $n \gg 0$. Note that the condition
+$n + d(K^n) \to -\infty$ as $n \to -\infty$ is not violated by this replacement.
````

### MC-STK-ERR-2545

`derived.tex` — derived.tex:9968; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L9968) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-find finite sequence of elementary transformations which
+find a finite sequence of elementary transformations which
````

### MC-STK-ERR-2546

`derived.tex` — derived.tex:10048; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10048) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j \in \{i - n - 2, \ldots, i - 1\}$. Hence we see that
+$j \in \{i - n - 2, \ldots, i - 2\}$. Hence we see that
````

### MC-STK-ERR-2547

`derived.tex` — derived.tex:10064; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10064-L10065) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-by the complex $F(L^\bullet)$ and $RF(\sigma_{\geq c}L^\bullet)$
-is represented by $\sigma_{\geq c}F(L^\bullet)$. Consider the
+by the complex $F(L^\bullet)$ and, for every integer $c$,
+$RF(\sigma_{\geq c}L^\bullet)$ is represented by
+$\sigma_{\geq c}F(L^\bullet)$. Consider the
````

### MC-STK-ERR-2548

`derived.tex` — derived.tex:10263; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10263-L10289) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-If $n_{i - 1} < j \leq n_i$, then we let $c_j = c|_{K_j}$
-be the map
+For each $j$, let $i$ be the least index such that $j \leq n_i$.
+We let $c_j = c|_{K_j}$ be the map (the identity when $j = n_i$)
````

````diff
--- original
+++ replacement
@@ -1,7 +1,9 @@
-the rule: for $n_{i - 1} < j < n_i$ we set
+the rule: let $i$ be the least index such that $j \leq n_i$.
+Set $h_j = 0$ if $j = n_i$. For $j < n_i$ we set
 $$
 h_j : K_j
 \xrightarrow{1,\ f_j,\ f_{j + 1} \circ f_j,
-\ \ldots,\ f_{n_i - 1} \circ \ldots \circ f_j}
-K_j \oplus \ldots \oplus K_{n_i}
+\ \ldots,\ f_{n_i - 2} \circ \ldots \circ f_j}
+K_j \oplus \ldots \oplus K_{n_i - 1}
 $$
+where for $j = n_i - 1$ this map has just the identity component.
````

### MC-STK-ERR-2549

`derived.tex` — derived.tex:10278; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10278-L10294) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi \circ \psi$ is an isomorphism by
+$\psi \circ \varphi$ is an isomorphism by
````

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-$\text{id} - \psi \circ \varphi$ has square zero by
+$\text{id} - \varphi \circ \psi$ has square zero by
 Lemma \ref{lemma-third-map-square-zero} (small argument omitted).
-In other words, $\psi \circ \varphi$ differs from the identity
+In other words, $\varphi \circ \psi$ differs from the identity
````

### MC-STK-ERR-2550

`derived.tex` — derived.tex:10800; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L10800-L10801) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,4 @@
-F(\mathcal{A}[a, b]) = F(\mathcal{A})[a, b]
+\operatorname{Iso}(F(\mathcal{A}[a, b])) =
+\operatorname{Iso}(F(\mathcal{A})[a, b]),
 $$
+where $\operatorname{Iso}$ denotes isomorphism closure. Moreover,
````

### MC-STK-ERR-2551

`derived.tex` — derived.tex:11209; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11209) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\text{hocolim} X_n$ and we conclude that our morphism $E_i[m] \to C$
+$(\text{hocolim} X_n)[-1]$ and we conclude that our morphism $E_i[m] \to C$
````

### MC-STK-ERR-2552

`derived.tex` — derived.tex:11216; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11216-L11217) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-With assumptions and notation as in Lemma \ref{lemma-write-as-colimit}.
-If $C$ is a compact object and $C \to X_n$ is a morphism, then
+With assumptions and notation as in Lemma \ref{lemma-write-as-colimit},
+if $C$ is a compact object and $C \to X_n$ is a morphism, then
````

### MC-STK-ERR-2553

`derived.tex` — derived.tex:11255; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11255) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the compositions into $Y_{n - 1}$ are equal. Let $C \to X_{n - 1}$
+the compositions into $Y_{n - 1}[1]$ are equal. Let $C \to X_{n - 1}$
````

### MC-STK-ERR-2554

`derived.tex` — derived.tex:11386; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11386) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $\prod H(X_n)$. Hence a natural transformation
+in $\prod H(X_n)$. Hence there is a natural transformation
````

### MC-STK-ERR-2555

`derived.tex` — derived.tex:11536; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11536) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $\prod H(X_n)$. Hence a natural transformation
+in $\prod H(X_n)$. Hence there is a natural transformation
````

### MC-STK-ERR-2556

`derived.tex` — derived.tex:11547; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11547-L11568) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,22 +1,99 @@
-Let $E \in \mathcal{E}$. Let us show that
+Let us prove that the telescope map is injective on maps from
+each $E \in \mathcal{E}$. Let $\mathcal{P}$ be the full subcategory
+of direct sums of objects of $\mathcal{E}$ and write
+$hY = \Hom_\mathcal{D}(-, Y)|_\mathcal{P}$.
+Let $\mathcal{A}$ be the category of additive functors
+$\mathcal{P}^{opp} \to \textit{Ab}$ taking direct sums to products.
+Kernels and cokernels in this category are computed pointwise:
+both commute with products of abelian groups.
+Thus $\mathcal{A}$ is abelian. Natural transformations form sets,
+since they are determined by their components at the set $\mathcal{E}$.
+
+\medskip\noindent
+We first show that $h$ preserves countable direct sums with values
+in $\mathcal{A}$. For every object $Y$ choose the evaluation map
+$P_Y = \bigoplus_{(E, f : E \to Y)} E \to Y$, complete it to a
+distinguished triangle $C_Y \to P_Y \to Y \to C_Y[1]$, and choose
+an evaluation map $Q_Y \to C_Y$ with $Q_Y \in \mathcal{P}$.
+We obtain an exact presentation
 $$
-\Hom_\mathcal{D}(E, \bigoplus X_n) \to  \Hom_\mathcal{D}(E, \bigoplus X_n)
+hQ_Y \to hP_Y \to hY \to 0.
 $$
-is injective. Namely, let $\alpha : E \to \bigoplus X_n$. Then
-by assumption (2) we obtain a factorization
-$\alpha = (\bigoplus \beta_n) \circ \gamma$.
-Since $E_n \to X_n \to X_{n + 1}$ is zero by construction, we see that
-the composition $\bigoplus E_n \to \bigoplus X_n \to \bigoplus X_n$
-is equal to $\bigoplus \beta_n$. Hence also the composition
-$E \to \bigoplus X_n \to \bigoplus X_n$ is equal to $\alpha$.
-This proves the stated injectivity and hence also
+For any countable family $Y_n$, assumption (2) shows that
+$\bigoplus P_{Y_n} \to \bigoplus Y_n$ is surjective on maps from
+every $E \in \mathcal{E}$: factor such a map through $\bigoplus E_n$
+and lift each $E_n \to Y_n$ to $P_{Y_n}$.
+The same holds for $\bigoplus Q_{Y_n} \to \bigoplus C_{Y_n}$.
+It holds for maps from every object of $\mathcal{P}$ by taking products.
+The direct sum of the distinguished triangles therefore gives
+an exact presentation
 $$
-\Hom_\mathcal{D}(E, \bigoplus X_n[1]) \to \Hom_\mathcal{D}(E, \bigoplus X_n[1])
+h(\bigoplus Q_{Y_n}) \to h(\bigoplus P_{Y_n}) \to
+h(\bigoplus Y_n) \to 0.
 $$
-is injective. It follows that we have an exact sequence
+For $F \in \mathcal{A}$, Yoneda's lemma and the product property give
+$$
+\Hom_\mathcal{A}(h(\bigoplus Y_n), F)
+= \Ker\left(\prod F(P_{Y_n}) \to \prod F(Q_{Y_n})\right)
+= \prod \Hom_\mathcal{A}(hY_n, F).
+$$
+These identifications are induced by the inclusions of the summands.
+Thus $h(\bigoplus Y_n)$ is their direct sum in $\mathcal{A}$.
+This does not assert that these direct sums are computed pointwise.
+
+\medskip\noindent
+Put $T = H|_\mathcal{P}$ and $M_n = hX_n$, and denote the
+transformations induced by $a_n$ by $\theta_n : M_n \to T$.
+Each $\theta_n$ is surjective, first on $\mathcal{E}$ by construction
+of $X_1$, and then on $\mathcal{P}$ by taking products.
+Write $u_n : X_n \to X_{n + 1}$ and $v_n = h(u_n)$.
+The construction gives
+$v_n(\Ker(\theta_n)) = 0$ and $\theta_{n + 1}v_n = \theta_n$.
+Hence $v_1$ factors as $\sigma_2\theta_1$ for a morphism
+$\sigma_2 : T \to M_2$ with $\theta_2\sigma_2 = 1$.
+Inductively put $\sigma_{n + 1} = v_n\sigma_n$ for $n \geq 2$.
+Then $\theta_n\sigma_n = 1$, and with $L_n = \Ker(\theta_n)$
+the isomorphisms
+$$
+T \oplus L_n \longrightarrow M_n,\qquad (x, z) \longmapsto \sigma_nx + z
+$$
+identify $v_n$, for $n \geq 2$, with $(x, z) \mapsto (x, 0)$.
+
+\medskip\noindent
+Let $V = \bigoplus_{n \geq 2} M_n$ in $\mathcal{A}$.
+Its idempotent induced by the $\sigma_n\theta_n$ splits it as
+$$
+V = C \oplus L,\qquad
+C = \bigoplus_{n \geq 2} T,\quad L = \bigoplus_{n \geq 2} L_n.
+$$
+These last two direct sums exist as the images of that idempotent
+and its complement; their universal properties follow from the
+component splittings. The tail telescope map $t_V$ is
+$(1 - s_C) \oplus 1_L$, where $s_C j_n = j_{n + 1}$ for the
+inclusions $j_n : T \to C$. The morphism $\ell_C : C \to C$ defined by
+$$
+\ell_C j_n = -\sum_{j = 2}^{n - 1} j_j
+$$
+(the empty sum is zero) satisfies $\ell_C(1 - s_C) = 1_C$.
+Thus $\ell_V = \ell_C \oplus 1_L$ is a left inverse of $t_V$.
+For the entire sequence, use the canonical isomorphism
+$h(\bigoplus X_n) \cong M_1 \oplus V$ and write $b : M_1 \to V$
+for $v_1$ followed by the inclusion of $M_2$.
+The entire telescope map is
+$$
+(x, y) \longmapsto (x, t_V y - bx),
+$$
+and it has the left inverse
+$$
+(x, y) \longmapsto (x, \ell_V(y + bx)).
+$$
+Evaluating at $E \in \mathcal{E}$ proves the required injectivity.
+Evaluating at $E[-1]$ proves injectivity on
+$\Hom_\mathcal{D}(E, \bigoplus X_n[1])$ as well.
+The distinguished triangle defining $X$ now gives the exact sequence
 $$
 \Hom_\mathcal{D}(E, \bigoplus X_n) \to
 \Hom_\mathcal{D}(E, \bigoplus X_n) \to
 \Hom_\mathcal{D}(E, X) \to 0
 $$
-for all $E \in \mathcal{E}$.
+for every $E \in \mathcal{E}$.
````

### MC-STK-ERR-2557

`derived.tex` — derived.tex:11956; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L11956-L11978) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-be subcategories. The following are equivalent
+be strictly full subcategories invariant under all shifts.
+The following are equivalent
````

````diff
--- original
+++ replacement
@@ -1,3 +1,17 @@
-The equivalence between (1), (2), and (3) follows in a straightforward manner
-from Lemmas \ref{lemma-right-adjoint} and \ref{lemma-left-adjoint} (small
-detail omitted). Denote $v : \mathcal{D} \to \mathcal{A}$ the right
+Assume (3). Then $\mathcal{B} \subset \mathcal{A}^\perp$ and
+$\mathcal{A} \subset {}^\perp\mathcal{B}$.
+If $X \in \mathcal{A}^\perp$, its triangle in (3) has zero first map,
+so $B \cong X \oplus A[1]$.
+Since $\Hom(A[1], B) = 0$, we obtain $A = 0$ and
+$X \cong B \in \mathcal{B}$. Strict fullness gives
+$\mathcal{A}^\perp = \mathcal{B}$.
+Similarly, if $X \in {}^\perp\mathcal{B}$, the second map of its
+triangle is zero, so $A \cong X \oplus B[-1]$.
+Since $\Hom(A, B[-1]) = 0$, we obtain $B = 0$ and
+$X \cong A \in \mathcal{A}$.
+Thus $\mathcal{A} = {}^\perp\mathcal{B}$.
+The orthogonal subcategories are saturated and triangulated as shown above.
+Lemmas \ref{lemma-right-adjoint} and \ref{lemma-left-adjoint}
+now give (1) and (2).
+Conversely, each of (1) and (2) gives (3) by its adjoint criterion.
+Denote $v : \mathcal{D} \to \mathcal{A}$ the right
````

### MC-STK-ERR-2558

`derived.tex` — derived.tex:12160; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L12160) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-know whether the composition $X_n \to X_{n - 1} \to Y_{n - 1}$
+know whether the composition $X_n \to X_{n - 1} \to Y_{n - 2}$
````

### MC-STK-ERR-2559

`derived.tex` — derived.tex:12253; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L12253) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-then there exists at most one morphism between these Postnikov systems.
+then any two morphisms between these Postnikov systems induce the same
+morphism $Y_n \to Y'_n$. In case (3), the morphism of Postnikov
+systems itself is unique.
````

### MC-STK-ERR-2560

`derived.tex` — derived.tex:12451; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L12451) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1,5 @@
-$\delta : C \to A[1]$ which is independent of $n$. Choose a distinguished
+$\delta : C \to A[1]$ which is independent of $n$.
+The components $C'_n \to A[1]$ vanish for all sufficiently large $n$:
+fix an index and use a later zero transition in $(C'_n)$.
+After increasing the starting index once more, the projections onto
+$C$ and $A[1]$ commute with the connecting maps. Choose a distinguished
````
