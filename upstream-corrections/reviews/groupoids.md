# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## groupoids

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/groupoids.patch)

### MC-STK-ERR-1480

`groupoids.tex` — groupoids.tex:71; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L71-L72) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

A relation is the subset R itself; 'a subset of R subset A times A' is malformed. Removing only 'of' restores the definition.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 is just a subset
-of $R \subset A \times A$
+$R \subset A \times A$
````

### MC-STK-ERR-1481

`groupoids.tex` — groupoids.tex:172; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L172-L173) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The construction 'denote by X the morphisms' requires 'by'.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Denote $x_K, y_K, z_K : \Spec(K) \to U$
+Denote by $x_K, y_K, z_K : \Spec(K) \to U$
 the morphisms
````

### MC-STK-ERR-1482

`groupoids.tex` — groupoids.tex:229; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L229) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

'Unramified' is predicative here and does not take an indefinite article.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j$ is a unramified
+$j$ is unramified
````

### MC-STK-ERR-1483

`groupoids.tex` — groupoids.tex:264; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L264) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The indefinite article before i(g) must be 'an'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists a $i(g) \in G$
+there exists an $i(g) \in G$
````

### MC-STK-ERR-1484

`groupoids.tex` — groupoids.tex:375; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L375) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

'Add more as needed.' is an authoring instruction embedded in a finished mathematical definition and should not be reader text.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
-Add more as needed.
````

### MC-STK-ERR-1485

`groupoids.tex` — groupoids.tex:510; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L510) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The comultiplication entry for matrix multiplication sums over the repeated index k; the printed sum has no index and is incomplete.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\sum x_{ik} \otimes x_{kj}
+\sum_k x_{ik} \otimes x_{kj}
````

### MC-STK-ERR-1486

`groupoids.tex` — groupoids.tex:749; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L749) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The lemma introduces its data rather than stating a conditional. Replacing the initial 'If' by 'Let' repairs the fragment without changing meaning.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-If $(G, m)$ is a group scheme over a field $k$.
+Let $(G, m)$ be a group scheme over a field $k$.
````

### MC-STK-ERR-1487

`groupoids.tex` — groupoids.tex:991; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L991) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

'Quasi-compect' is a typographical error for 'quasi-compact'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-quasi-compect
+quasi-compact
````

### MC-STK-ERR-1488

`groupoids.tex` — groupoids.tex:1028; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1028) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

'Subsgroup' is a typographical error for 'subgroup'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-closed subsgroup scheme
+closed subgroup scheme
````

### MC-STK-ERR-1489

`groupoids.tex` — groupoids.tex:1150; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1150) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The next sentence uses left G^0-invariance of W to infer g^{-1}U is contained in W. This requires the affine neighbourhood U to be chosen inside W; W is open and contains G^0 after the reduction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Choose an affine open neighbourhood $U \subset G$
+Choose an affine open neighbourhood $U \subset W$
````

### MC-STK-ERR-1490

`groupoids.tex` — groupoids.tex:1164; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1164) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The domain is U times T and the formula uses u in U and t in T, so the displayed input pair must be (u,t).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(t, u) \longrightarrow (uf(t)^{-1}, t)
+(u, t) \longrightarrow (uf(t)^{-1}, t)
````

### MC-STK-ERR-1491

`groupoids.tex` — groupoids.tex:1534,1557; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1534-L1557) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

An inner automorphism has trivial ordinary kernel, whereas the proof requires the equalizer with the identity: the closed centralizer locus containing every subscheme on which conjugation is the identity.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-the closed subschemes $G_{n, S}$. Consider the kernel
-$K = \Ker(\text{inn}_h : G_S \to G_S)$.
+the closed subschemes $G_{n, S}$. Consider the equalizer
+$K \subset G_S$ of $\text{inn}_h$ and $\text{id}_{G_S}$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-C = H \cap \bigcap\nolimits_i \Ker(\text{inn}_{g_i} : G \to G)
+C = H \cap \bigcap\nolimits_i \operatorname{Eq}(\text{inn}_{g_i}, \text{id}_G)
````

### MC-STK-ERR-1492

`groupoids.tex` — groupoids.tex:1554; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1554-L1555) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The sentence has two competing predicates joined without a conjunction. The components are both irreducible components and translates of G^0.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 the connected components of $G$ are the irreducible components
-of $G$ are the translates of $G^0$
+of $G$ and are the translates of $G^0$
````

### MC-STK-ERR-1493

`groupoids.tex` — groupoids.tex:1567; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1567) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The let-construction requires 'be'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A \subset G_{\overline{k}}$ the closed subgroup scheme
+$A \subset G_{\overline{k}}$ be the closed subgroup scheme
````

### MC-STK-ERR-1494

`groupoids.tex` — groupoids.tex:1771; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1771) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

For d=0 and positive-dimensional A, multiplication by d is not finite and the displayed degree argument degenerates. The proof and statement require a nonzero integer.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Let $[d] : A \to A$ be the multiplication by $d$.
+Let $d \in \mathbf{Z}$ be nonzero, and let
+$[d] : A \to A$ be multiplication by $d$.
````

### MC-STK-ERR-1495

`groupoids.tex` — groupoids.tex:2132; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2132) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The pronounced initial consonant in G requires 'a', not 'an'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an $G$-equivariant isomorphism
+a $G$-equivariant isomorphism
````

### MC-STK-ERR-1496

`groupoids.tex` — groupoids.tex:2220; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2220) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The plural subject 'answers' requires 'are'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the answers to these questions is no
+the answers to these questions are no
````

### MC-STK-ERR-1497

`groupoids.tex` — groupoids.tex:2314; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2314) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The clause 'verify that' is followed only by a diagram and where-clause. Naming commutativity supplies the missing predicate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Namely, to check this we have to verify that
+Namely, to check this we have to verify commutativity of the diagram
````

### MC-STK-ERR-1498

`groupoids.tex` — groupoids.tex:2360; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2360) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

Coassociativity sends f_n tensor x^n to f_n tensor x^n tensor x^n. The printed right-hand side multiplies f_n by x^n across distinct tensor factors.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\sum f_n x^n \otimes x^n
+\sum f_n \otimes x^n \otimes x^n
````

### MC-STK-ERR-1499

`groupoids.tex` — groupoids.tex:2643; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2643) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The displayed object is a commutative diagram, not 'a commutative'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a commutative in the category of
+is a commutative diagram in the category of
````

### MC-STK-ERR-1500

`groupoids.tex` — groupoids.tex:2849,2850; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2849-L2851) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

Both explanatory clauses lack 'holds'; the first and last are two equalities and therefore require the plural.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The middle equality because
+The middle equality holds because
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-and the first and the last
-equality because
+and the first and last
+equalities hold because
````

### MC-STK-ERR-1501

`groupoids.tex` — groupoids.tex:2860; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2860) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

Because j=(t,s), the equivalence-relation groupoid on R has source pr_1 and target pr_0. The morphism displayed immediately afterward uses that correct order.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(R, R \times_{t, U, t} R, \text{pr}_0, \text{pr}_1, \text{pr}_{02})
+(R, R \times_{t, U, t} R, \text{pr}_1, \text{pr}_0, \text{pr}_{02})
````

### MC-STK-ERR-1502

`groupoids.tex` — groupoids.tex:2991; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2991) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The infinitive is 'to show'; 'the show' is a typographical substitution.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-it suffices the show that
+it suffices to show that
````

### MC-STK-ERR-1503

`groupoids.tex` — groupoids.tex:3145; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3145) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The article and predicate select one quasi-coherent module.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a quasi-coherent modules on
+is a quasi-coherent module on
````

### MC-STK-ERR-1504

`groupoids.tex` — groupoids.tex:3183; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3183) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The symbolic relation greater-than-or-equal already supplies the comparison; 'than' is extraneous.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cardinal $\geq$ than the cardinality
+cardinal $\geq$ the cardinality
````

### MC-STK-ERR-1505

`groupoids.tex` — groupoids.tex:3215; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3215-L3216) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The identity-overlap convention has j=i, hence k lies in I_ii and m lies in M_i. Writing those domains explicitly removes the malformed variable list.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 Moreover, let's agree that $S(i, i, k, m) = \{m\}$ for all
-$i, j = i, k, m$ when $k \in I_{ij}$.
+$i \in I$, $k \in I_{ii}$, and $m \in M_i$.
````

### MC-STK-ERR-1506

`groupoids.tex` — groupoids.tex:3432; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3432) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The conditional clause requires the displayed action as its main subject; deleting 'which' supplies the missing predicate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-which turns $R_p$ into a
+turns $R_p$ into a
````

### MC-STK-ERR-1507

`groupoids.tex` — groupoids.tex:3518; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3518) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The adverb is 'sometimes'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We sometime use the notation
+We sometimes use the notation
````

### MC-STK-ERR-1508

`groupoids.tex` — groupoids.tex:3614; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3614) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The inverse image s^{-1}(W) is open by continuity; its image is open because t is open. Naming t makes the stated inference direct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Since $s$ is open the set $W' = t(s^{-1}(W))$
+Since $t$ is open the set $W' = t(s^{-1}(W))$
````

### MC-STK-ERR-1509

`groupoids.tex` — groupoids.tex:3865; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3865) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The let-construction requires 'be'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $g : U' \to U$ a morphism
+Let $g : U' \to U$ be a morphism
````

### MC-STK-ERR-1510

`groupoids.tex` — groupoids.tex:4050; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4050) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The nonrestrictive parenthetical 'which we omit' requires a closing comma.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A computation, which we omit shows
+A computation, which we omit, shows
````

### MC-STK-ERR-1511

`groupoids.tex` — groupoids.tex:4172; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4172) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The preceding paragraph proves that condition (b) gives the identity-section property (c). The implication (b) to (a) was not established there and is handled through (c) in the next paragraph.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus (b) $\Rightarrow$ (a) in both (1) and (2).
+Thus (b) $\Rightarrow$ (c) in both (1) and (2).
````

### MC-STK-ERR-1512

`groupoids.tex` — groupoids.tex:4224; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4224) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The unresolved authoring placeholder is not a citation and contributes no mathematical content; delete the parenthetical residue.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
- (insert future reference here)
````

### MC-STK-ERR-1513

`groupoids.tex` — groupoids.tex:4276; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4276) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The fibre product is formed using the source morphism s and target morphism t, as in the defining diagram at line 4266. Capital S is the base scheme and is ill-typed in this subscript.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R \times_{S, U, t} R
+R \times_{s, U, t} R
````

### MC-STK-ERR-1514

`groupoids.tex` — groupoids.tex:4309; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4309) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The symbolic biconditional and the words 'if and only if' duplicate the same connective.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$u \in U_r \Leftrightarrow$ if and only if
+$u \in U_r \Leftrightarrow$
````

### MC-STK-ERR-1515

`groupoids.tex` — groupoids.tex:4421; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4421) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

U' was defined as Spec(A tensor_C C') and A' abbreviates that ring. Spec(C') maps to Spec(C), not directly to U.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$U' = \Spec(C') \to U$
+$U' = \Spec(A') \to U$
````

### MC-STK-ERR-1516

`groupoids.tex` — groupoids.tex:4537,4541; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4537-L4542) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

Both parentheticals are unresolved authoring placeholders, not valid references. Removing them preserves the mathematical assertions and removes reader-facing residue.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
- (insert future reference on property determinant here)
````

````diff
--- original
+++ replacement
@@ -1,2 +0,0 @@
- (insert future reference
-on property determinant here)
````

### MC-STK-ERR-1517

`groupoids.tex` — groupoids.tex:4570; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4570) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

A groupoid-scheme tuple includes composition c. The source groupoid therefore requires c', which the same proof uses explicitly at line 4615.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(U', R', s', t') \to (U, R, s, t, c)
+(U', R', s', t', c') \to (U, R, s, t, c)
````

### MC-STK-ERR-1518

`groupoids.tex` — groupoids.tex:4641; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4641) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The sentence requires the sequencing adverb 'Then', not the article 'The'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The $M_1 = \lim M_i$
+Then $M_1 = \lim M_i$
````

### MC-STK-ERR-1519

`groupoids.tex` — groupoids.tex:4777; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4777) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

'Tow' is a typographical error for 'two'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the tow left squares
+the two left squares
````

### MC-STK-ERR-1520

`groupoids.tex` — groupoids.tex:4788; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4788) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The phrase requires the definite article 'the'; 'then' has no syntactic role.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and hence also then isomorphic arrow $t$
+and hence also the isomorphic arrow $t$
````

### MC-STK-ERR-1521

`groupoids.tex` — groupoids.tex:4941; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4941) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The subsequent closedness, containment W' subset W, and invariant-orbit description require the complement of s^{-1}(W) intersect t^{-1}(W), not the left-associative intersection of a complement with t^{-1}(W).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$Z = R \setminus s^{-1}(W) \cap t^{-1}(W)$
+$Z = R \setminus (s^{-1}(W) \cap t^{-1}(W))$
````

### MC-STK-ERR-1522

`groupoids.tex` — groupoids.tex:5049; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L5049-L5050) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r46/candidate.manifest.json)

The tuple length d is unbound in the statement. Quantifying over every positive integer d states the required hypothesis; the proof then applies it at the uniform fibre bound chosen afterward.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Let $V$ be a scheme over $X$ such that for all 
+Let $V$ be a scheme over $X$ such that for every positive integer $d$ and all
 $(y, v_1, \ldots, v_d)$
````

### MC-STK-ERR-1564

`groupoids.tex` — 1836; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L1836) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

If d=0 the fibre over the unit is the positive-dimensional abelian variety A, so multiplication is not etale. Split off that case before applying the degree lemma requiring d nonzero, and retain the theorem's full statement.

````diff
--- original
+++ replacement
@@ -1 +1,4 @@
+If $d = 0$, then the fibre of $[d]$ over the unit is the
+positive-dimensional variety $A$, so $[d]$ is not \'etale.
+Thus we may assume $d \not= 0$.
 Observe that $[d](x + y) = [d](x) + [d](y)$. Since translation by a
````

### MC-STK-ERR-1565

`groupoids.tex` — 3179; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3179) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The convention alpha:t*F to s*F and the displayed tensors require t(W_ijk) subset U_i and s(W_ijk) subset U_j. Reverse the cover's two labels; all other indices and the existing admitted support repairs remain.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-s^{-1}(U_i) \cap t^{-1}(U_j) = \bigcup\nolimits_{k \in J_{ij}} W_{ijk}.
+t^{-1}(U_i) \cap s^{-1}(U_j) = \bigcup\nolimits_{k \in J_{ij}} W_{ijk}.
````

### MC-STK-ERR-1566

`groupoids.tex` — 4425; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L4425) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

After base change the rank component produces its polynomial over C'_r, not C_r. The identity-groupoid base change k to k[z] with f=z gives x-z as a direct counterexample to the unprimed ring.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then given $f \in C^1$ let $P_r \in C_r[x]$ be the polynomial
+Then given $f \in C^1$ let $P_r \in C'_r[x]$ be the polynomial
````

### MC-STK-ERR-1567

`groupoids.tex` — 3214; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L3214) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The two displayed support equalities lie respectively in M_ijk and M_j tensor_{A_j,s} B_ijk. Name both ambient modules in that order, as the later passage already does.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-in $M_{ijk}$ for some $a_{m'} \in A_{ijk}$ or $b_{m'} \in B_{ijk}$.
+in $M_{ijk}$ or $M_j \otimes_{A_j, s} B_{ijk}$, respectively,
+for some $a_{m'} \in A_{ijk}$ or $b_{m'} \in B_{ijk}$.
````

### MC-STK-ERR-1568

`groupoids.tex` — 2671, 2673; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex#L2671-L2673) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Pulling the cocycle back by (i,1) gives alpha composed with i*alpha = s*e*alpha; (1,i) gives i*alpha composed with alpha = t*e*alpha. Correct both left-hand orders. Swapping only right-hand labels would misidentify the named pullbacks.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then we see that $i^*\alpha \circ \alpha = s^*e^*\alpha$.
+Then we see that $\alpha \circ i^*\alpha = s^*e^*\alpha$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\alpha \circ i^*\alpha = t^*e^*\alpha$. By the second assumption 
+$i^*\alpha \circ \alpha = t^*e^*\alpha$. By the second assumption 
````
