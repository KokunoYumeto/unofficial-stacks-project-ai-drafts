# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## perfect

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/perfect.patch)

### MC-STK-ERR-1437

`perfect.tex` — perfect.tex:9226; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9226) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The second occurrence of module has no grammatical or mathematical role; deleting it preserves the finite-presentation condition and the module type.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-every $\mathcal{O}_X$-module module of finite presentation
+every $\mathcal{O}_X$-module of finite presentation
````

### MC-STK-ERR-1438

`perfect.tex` — perfect.tex:9277; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9277) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Lines 9262 and 9269-9273 define s_{j,i} with exponent n_{j,i} and place it in H_{-n_{j,i}}; adjunction followed by tensoring back therefore requires L^{otimes n_{j,i}}.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{L}^{\otimes n_{i, j}}
+\mathcal{L}^{\otimes n_{j, i}}
````

### MC-STK-ERR-1439

`perfect.tex` — perfect.tex:9284; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9284) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The only section family introduced is s_{j,i}, over V_j, and H'_{i,j} is explicitly a submodule of H_{-n_{j,i}}.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$s_{i, j}$
+$s_{j, i}$
````

### MC-STK-ERR-1440

`perfect.tex` — perfect.tex:9286; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9286) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The preceding sentence constructs H'_{i,j}; the resolution-property surjection from E_{i,j} must target that same finite-type submodule.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{E}_{i, j} \to \mathcal{H}'_{j, i}$
+$\mathcal{E}_{i, j} \to \mathcal{H}'_{i, j}$
````

### MC-STK-ERR-1441

`perfect.tex` — perfect.tex:9371; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9371) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The prose calls this the ideal on U_j, so U_j must be the restriction subscript; without the underscore the TeX does not express a restriction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{I}_{j'}|{U_j}$
+$\mathcal{I}_{j'}|_{U_j}$
````

### MC-STK-ERR-1442

`perfect.tex` — perfect.tex:9403; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9403) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The section s_{jk} lives on U_j and the immediately following composition uses I_j^{n_{jk}}; I_i is not the covering ideal for this step.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$s'_{jk} : \mathcal{I}_i^{n_{jk}} \to \mathcal{F}$
+$s'_{jk} : \mathcal{I}_j^{n_{jk}} \to \mathcal{F}$
````

### MC-STK-ERR-1443

`perfect.tex` — perfect.tex:9448; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9448) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Resolution property is the singular defined property used throughout the statement and proof.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the resolution properties for some $i$.
+the resolution property for some $i$.
````

### MC-STK-ERR-1444

`perfect.tex` — perfect.tex:9790; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9790) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The proposition twice uses the established phrase triangulated categories; trianglated is an unambiguous spelling error.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-trianglated
+triangulated
````

### MC-STK-ERR-1445

`perfect.tex` — perfect.tex:9869; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9869) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The nested K_0(D^b(Coh(O_X))) expression opens three ordinary parentheses but the line closes only two before the equality; the adjacent first and third terms are balanced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-K_0(D^b(\textit{Coh}(\mathcal{O}_X)) =
+K_0(D^b(\textit{Coh}(\mathcal{O}_X))) =
````

### MC-STK-ERR-1446

`perfect.tex` — perfect.tex:9903; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L9903) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Line 9902 already ends with 'It is the'; deleting the repeated 'is the' at the start of line 9903 yields the intended single copular phrase.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is the zeroth $K$-group
+zeroth $K$-group
````

### MC-STK-ERR-1447

`perfect.tex` — perfect.tex:10062; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10062) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The displayed acyclic-complex decomposition advances from F^{a+1} to E^{a+2} and therefore has cokernel F^{a+2}; a+3 breaks the consecutive exact-sequence pattern used in the alternating-sum proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{F}^{a + 3} \to 0
+\mathcal{F}^{a + 2} \to 0
````

### MC-STK-ERR-1448

`perfect.tex` — perfect.tex:10073; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10073) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

This is the Euler characteristic, and the immediately following expansion uses (-1)^n; without the exponent the first sum is a constant negative sum and the stated cancellation does not follow.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\sum (-1)[\mathcal{E}^n]
+\sum (-1)^n[\mathcal{E}^n]
````

### MC-STK-ERR-1449

`perfect.tex` — perfect.tex:10098; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10098) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The proof introduces the quasi-isomorphism a and its cone C(a) at lines 10090 and 10093; no f is introduced in this argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-c(C(f)^\bullet)
+c(C(a)^\bullet)
````

### MC-STK-ERR-1450

`perfect.tex` — perfect.tex:10120; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10120) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The repeated definite article is a source-prose typo with no mathematical effect.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then the the existence
+Then the existence
````

### MC-STK-ERR-1451

`perfect.tex` — perfect.tex:10205; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10205) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Only and most often assert incompatible uniqueness and frequency claims. Removing only is the smallest repair and preserves the explicit practical-frequency statement without adding exclusivity.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-If $Y$ is quasi-compact (the only
+If $Y$ is quasi-compact (the
````

### MC-STK-ERR-1452

`perfect.tex` — perfect.tex:10342; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10342) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The sentence's subject is already Lf^*K. The second K appears between the predicate noun and its of-complement, has no syntactic role, and falsely renames the pullback object; deleting it restores the intended assertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-perfect object $K$ of $D(\mathcal{O}_X)$
+perfect object of $D(\mathcal{O}_X)$
````

### MC-STK-ERR-1453

`perfect.tex` — perfect.tex:10387,10432; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10387-L10432) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Both equalities are adjunction calculations in D(O_U). Their first argument is K|_U[-n], and the second must likewise be an object on U. The surrounding term Rj_*(E|_U) already identifies the intended restriction. Plain E is an object on X and is ill-typed as written.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Hom_{D(\mathcal{O}_U)}(K|_U[-n], E)
+\Hom_{D(\mathcal{O}_U)}(K|_U[-n], E|_U)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Hom_{D(\mathcal{O}_U)}(K|_U[-n], E)
+\Hom_{D(\mathcal{O}_U)}(K|_U[-n], E|_U)
````

### MC-STK-ERR-1454

`perfect.tex` — perfect.tex:10423,10435,10444,10446,10449,10450; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10423-L10450) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Write B = Rj_*(E|_U). Rotating the triangle E -> B -> N -> E[1] gives N[-1] -> E -> B. Because Hom(K[-n], B[q]) vanishes for every shift q, the long exact Hom sequence gives Hom(K[-n], N[-1]) isomorphic to Hom(K[-n], E). Hom(K[-n], N[-1]) equals Hom(K[-n+1], N). Therefore condition (2) for n <= a is equivalent, after m = n - 1, to Hom(K[-m], N) = 0 for m <= a - 1, not m <= a. Condition (1) at a implies tau_{<=a-1}N = 0 and is implied by tau_{<=a}N = 0. Hence (1)_a implies (2)_a, while (2)_a implies (1)_{a-1}. The printed implication order is reversed because it relies on the lost shift. Rejected partial repair: Changing only the Hom index on line 10435 would leave the repeated bounds and final truncation conclusion inconsistent. Rejected partial repair: Preserving line 10423 would require changing the hypothesis in item (2) to n <= a + 1; that is mathematically valid but less faithful than preserving the stated condition and repairing the proof and implication order.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then (2) implies (1) and (1) implies (2) with $a$ replaced by $a - 1$.
+Then (1) implies (2) and (2) implies (1) with $a$ replaced by $a - 1$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\Hom_{D(\mathcal{O}_X)}(K[-n], N) = 0$ for all $n \leq a$.
+$\Hom_{D(\mathcal{O}_X)}(K[-n], N) = 0$ for all $n \leq a - 1$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\Hom_{D(\mathcal{O}_X)}(K[-n], N) = 0$ for all $n \leq a$
+$\Hom_{D(\mathcal{O}_X)}(K[-n], N) = 0$ for all $n \leq a - 1$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\Hom_{D(\mathcal{O}_X)}(K_e[-n], N) = 0$ for all $n \leq a$ and all $e \geq 1$
+$\Hom_{D(\mathcal{O}_X)}(K_e[-n], N) = 0$ for all $n \leq a - 1$ and all $e \geq 1$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^n(X, N) = 0$ for $n \leq a$. We conclude that (2) is equivalent to
+$H^n(X, N) = 0$ for $n \leq a - 1$. We conclude that (2) is equivalent to
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\tau_{\leq a}N = 0$ since $N$ is determined by the complex of
+$\tau_{\leq a - 1}N = 0$ since $N$ is determined by the complex of
````

### MC-STK-ERR-1455

`perfect.tex` — perfect.tex:10534,10652; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10534-L10652) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Each sentence coordinates two separately numbered parts, so the singular noun Part is grammatically wrong at both parallel loci.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Part (5) and (6)
+Parts (5) and (6)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Part (5) and (6)
+Parts (5) and (6)
````

### MC-STK-ERR-1456

`perfect.tex` — perfect.tex:10552,10670; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10552-L10671) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Both parallel phrases name the distinct properties (7)(b) and (7)(c), so the shared singular noun property must be plural.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-except that for property
+except that for properties
 (7)(b) and (7)(c)
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-except that for property
+except that for properties
 (7)(b) and (7)(c)
````

### MC-STK-ERR-1457

`perfect.tex` — perfect.tex:10772; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10772) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The indefinite article a requires the singular count noun morphism.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a morphisms of ringed sites
+a morphism of ringed sites
````

### MC-STK-ERR-1458

`perfect.tex` — perfect.tex:10792; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10792) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

Lines 10768-10777 explicitly define the chaotic site X_affine with structure sheaf O, item (5) uses (X_affine,O), and the proof at lines 10827-10842 applies a result to the ringed site (X_affine,O). The cited Cohomology on Sites lemma likewise takes a sheaf O on the category. O_X belongs to the ringed space X and is not the named sheaf in item (4).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$D_\QCoh(X_{affine}, \mathcal{O}_X)$
+$D_\QCoh(X_{affine}, \mathcal{O})$
````

### MC-STK-ERR-1459

`perfect.tex` — perfect.tex:10822; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10822) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The doubled interword space is an isolated source typography defect.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus  we get
+Thus we get
````

### MC-STK-ERR-1460

`perfect.tex` — perfect.tex:10859; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L10859-L10860) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r44/candidate.manifest.json)

The sentence has no predicate as printed. Follows from supplies the evident relation to the cited discussion while preserving its target.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Thus the result by the discussion in
+Thus the result follows from the discussion in
 Schemes, Section
````

### MC-STK-ERR-2562

`perfect.tex` — perfect.tex:529; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L529-L536) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1,8 +1,21 @@
-may assume $S$ affine. By
-Lemma \ref{lemma-quasi-coherence-direct-image}
-we have $R^0f_*\mathcal{F}^\bullet = R^0f_*\tau_{\geq -n}\mathcal{F}^\bullet$
-for all sufficiently large $n$. Thus we may assume $\mathcal{F}^\bullet$
-bounded below. As each $\mathcal{F}^n$ is right $f_*$-acyclic by
-assumption we see that $f_*\mathcal{F}^\bullet \to Rf_*\mathcal{F}^\bullet$
-is a quasi-isomorphism by Leray's acyclicity lemma (Derived Categories, Lemma
-\ref{derived-lemma-leray-acyclicity}).
+may assume $S$ affine. Choose $N$ as in
+Lemma \ref{lemma-quasi-coherence-direct-image} and an integer
+$n \geq \max\{1, N\}$. The termwise split short exact sequence
+$$
+0 \to \sigma_{\geq -n}\mathcal{F}^\bullet \to
+\mathcal{F}^\bullet \to \sigma_{\leq -n-1}\mathcal{F}^\bullet \to 0
+$$
+gives a distinguished triangle. The last complex has quasi-coherent
+cohomology, vanishing in degrees greater than $-n-1$. The bound $N$
+therefore gives vanishing of
+$H^j(Rf_*\sigma_{\leq -n-1}\mathcal{F}^\bullet)$ for $j \geq N-n-1$,
+in particular for $j=-1,0$. It follows that
+$H^0(Rf_*\sigma_{\geq -n}\mathcal{F}^\bullet) \to
+H^0(Rf_*\mathcal{F}^\bullet)$ is an isomorphism.
+Also $H^0(f_*\sigma_{\geq -n}\mathcal{F}^\bullet) =
+H^0(f_*\mathcal{F}^\bullet)$ since $n \geq 1$.
+The complex $\sigma_{\geq -n}\mathcal{F}^\bullet$ is bounded below
+and consists of the original right $f_*$-acyclic terms, so it computes
+$Rf_*$ by Leray's acyclicity lemma (Derived Categories, Lemma
+\ref{derived-lemma-leray-acyclicity}). Naturality of the canonical map
+now proves the desired isomorphism in degree zero.
````

### MC-STK-ERR-2563

`perfect.tex` — perfect.tex:4324; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L4324-L4404) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the perfect objects define compact objects of $D(\mathcal{O}_X)$
+the perfect objects define compact objects of $D_\QCoh(\mathcal{O}_X)$
````

````diff
--- original
+++ replacement
@@ -1,9 +1,10 @@
-using the generator $E$. Since the functor $\mathcal{D} \to D(\mathcal{O}_X)$
+using the generator $E$. Since the functor $\mathcal{D} \to D_\QCoh(\mathcal{O}_X)$
 commutes with direct sums, we see that $K = \text{hocolim} K_n$
-holds in $D(\mathcal{O}_X)$. Since $\mathcal{O}_X$ is a compact
-object of $D(\mathcal{O}_X)$ we find an $n$ and a morphism
+holds in $D_\QCoh(\mathcal{O}_X)$. Since $\mathcal{O}_X$ is a compact
+object of $D_\QCoh(\mathcal{O}_X)$ we find an $n$ and a morphism
 $\alpha_n : \mathcal{O}_X \to K_n$ which gives rise to $\alpha$, see
 Derived Categories, Lemma \ref{derived-lemma-commutes-with-countable-sums}.
-By Derived Categories, Lemma \ref{derived-lemma-factor-through}
+By the finite-stage argument in the proof of Derived Categories, Lemma \ref{derived-lemma-factor-through}
 applied to the morphism $\mathcal{O}_X[0] \to K_n$ in the ambient
-category $D(\mathcal{O}_X)$ we see that $\alpha_n$ factors as
+category $D_\QCoh(\mathcal{O}_X)$, which does not require $E$ to generate
+the ambient category, we see that $\alpha_n$ factors as
````

### MC-STK-ERR-2564

`perfect.tex` — perfect.tex:4326; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L4326) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sums. For the converse we will use there exists a generator
+sums. For the converse we will use that there exists a generator
````

### MC-STK-ERR-2565

`perfect.tex` — perfect.tex:4385; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L4385) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H^0(K) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[0], K)$.
+$H^0(X, K) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[0], K)$.
````

### MC-STK-ERR-2566

`perfect.tex` — perfect.tex:4848; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/perfect.tex#L4848) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r61/candidate.manifest.json)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The adjoint exists if and only if for every object $K$ of
+The adjoint exists if and only if for every object $E$ of
````
