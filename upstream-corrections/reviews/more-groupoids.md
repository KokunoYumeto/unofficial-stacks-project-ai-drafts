# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## more-groupoids

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/more-groupoids.patch)

### MC-STK-ERR-1523

`more-groupoids.tex` — more-groupoids.tex:228; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L228) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The definite statement established by the lemma requires the article: 'to prove the statement'.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus to prove statement
+Thus to prove the statement
````

### MC-STK-ERR-1524

`more-groupoids.tex` — more-groupoids.tex:250; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L250) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The parenthesis introduced by '(see' is distinct from the inner parenthesis around the reference and needs its own closing delimiter.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Diagram (\ref{equation-quotient-stack}).
+Diagram (\ref{equation-quotient-stack})).
````

### MC-STK-ERR-1525

`more-groupoids.tex` — more-groupoids.tex:269,499,549; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L269-L550) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

In all three constructions, English 'denote by X the object' requires the preposition 'by'.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $h$ the composition
+Denote by $h$ the composition
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-we will denote $F_u = s^{-1}(u)$ the scheme
+we will denote by $F_u = s^{-1}(u)$ the scheme
 theoretic fibre
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Denote $F_u = s^{-1}(u)$ and $F_{u'} = s^{-1}(u')$ the scheme
+Denote by $F_u = s^{-1}(u)$ and $F_{u'} = s^{-1}(u')$ the scheme
 theoretic fibres.
````

### MC-STK-ERR-1526

`more-groupoids.tex` — more-groupoids.tex:345; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L345) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The equalizer descent is along the split projection to U-prime, and sigma has source U-prime; the descended subset is therefore a subset of U-prime, not U.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is the inverse image of a subset of $U$,
+is the inverse image of a subset of $U'$,
````

### MC-STK-ERR-1527

`more-groupoids.tex` — more-groupoids.tex:524; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L524) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The two morphisms form a plural subject and must be described as open immersions.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g$ and $g'$ are an open immersion
+$g$ and $g'$ are open immersions
````

### MC-STK-ERR-1528

`more-groupoids.tex` — more-groupoids.tex:599; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L599) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The clause introduced by 'show that' otherwise ends with a noun phrase; adding 'hold' supplies the required predicate.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\tau$-topology''.
+$\tau$-topology'' hold.
````

### MC-STK-ERR-1529

`more-groupoids.tex` — more-groupoids.tex:655; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L655) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The sentence begins on the previous line with 'such that'; deleting the stray 'Let' restores the grammatical assertion.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $t^{-1}(U') \subset R$ is
+$t^{-1}(U') \subset R$ is
````

### MC-STK-ERR-1530

`more-groupoids.tex` — more-groupoids.tex:769,867; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L769-L867) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

Both definitions compose with s-prime, whose source is R-prime; the displayed comparison diagram likewise uses R-prime. The two producer rows are linked occurrences of one defect.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U'' \times_{g', U', t} R \to U'
+U'' \times_{g', U', t} R' \to U'
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U'' \times_{g', U', t} R \to U'
+U'' \times_{g', U', t} R' \to U'
````

### MC-STK-ERR-1531

`more-groupoids.tex` — more-groupoids.tex:854; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L854) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The outer ordered pair on the right-hand side lacks its final closing parenthesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-((u', r_0), (u'', r_1)) = ((v', p), (v'', c(r, p))
+((u', r_0), (u'', r_1)) = ((v', p), (v'', c(r, p)))
````

### MC-STK-ERR-1532

`more-groupoids.tex` — more-groupoids.tex:896; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L896) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The projection is the base change of t along g; tau is a topology, not a morphism.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as a base change of $\tau$ and condition (a).
+as a base change of $t$ using condition (a).
````

### MC-STK-ERR-1533

`more-groupoids.tex` — more-groupoids.tex:1082; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L1082) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The preceding construction defines sigma on the rational function field inside kappa(r), then extends sigma to kappa(r); kappa(alpha) is undefined and tau is reserved for the later automorphism of k-prime.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then extend to $\tau : \kappa(\alpha) \to k'$ using that $k'$ is
+Then extend to $\sigma : \kappa(r) \to k'$ using that $k'$ is
````

### MC-STK-ERR-1534

`more-groupoids.tex` — more-groupoids.tex:1736; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L1736) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The fibre product is not canonically a subscheme of Z; the proof needs only that it is reduced before constructing the composition morphism to Z.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$Z \times_{\text{pr}_1, U, \text{pr}_0} Z \subset Z$
+$Z \times_{\text{pr}_1, U, \text{pr}_0} Z$
````

### MC-STK-ERR-1535

`more-groupoids.tex` — more-groupoids.tex:1944,1949,1972; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L1944-L1972) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The tensor-product computation and the subsequent local quotient require quotienting by the sum of the two ideals, not adding the second ideal after taking a quotient.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-B/s(\mathfrak m)B + t(\mathfrak m)B
+B/(s(\mathfrak m)B + t(\mathfrak m)B)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-B_{\mathfrak q}/s(\mathfrak m)B_{\mathfrak q} + t(\mathfrak m)B_{\mathfrak q}
+B_{\mathfrak q}/(s(\mathfrak m)B_{\mathfrak q} + t(\mathfrak m)B_{\mathfrak q})
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-B_{\mathfrak q}/s(\mathfrak m)B_{\mathfrak q} + t(\mathfrak m)B_{\mathfrak q}
+B_{\mathfrak q}/(s(\mathfrak m)B_{\mathfrak q} + t(\mathfrak m)B_{\mathfrak q})
````

### MC-STK-ERR-1536

`more-groupoids.tex` — more-groupoids.tex:1957; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L1957) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The dimension expression needs its outer closing parenthesis, and the relevant B-element is t(f), as used throughout the following flatness and fibre computation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim(B_{\mathfrak q}/(s(\mathfrak m)B_{\mathfrak q} + fB_{\mathfrak q}) < d_2
+\dim(B_{\mathfrak q}/(s(\mathfrak m)B_{\mathfrak q} + t(f)B_{\mathfrak q})) < d_2
````

### MC-STK-ERR-1537

`more-groupoids.tex` — more-groupoids.tex:1974; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L1974) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The minimal primes are indexed by j before and after this line; i is unbound here.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-t^{-1}(\mathfrak n_i)
+t^{-1}(\mathfrak n_j)
````

### MC-STK-ERR-1538

`more-groupoids.tex` — more-groupoids.tex:1998; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L1998) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The element of B whose nonzerodivisor property is established is t(f), not the element f of A itself.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and $f$ is not contained
+and $t(f)$ is not contained
````

### MC-STK-ERR-1539

`more-groupoids.tex` — more-groupoids.tex:2047; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L2047) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The fibre and stabilizer belong to the restricted groupoid, whose identity point is e-prime(u), as used in the slicing lemma and induction proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim_{e(u)}(F'_u)
+\dim_{e'(u)}(F'_u)
````

### MC-STK-ERR-1540

`more-groupoids.tex` — more-groupoids.tex:2437; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L2437) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

A section e:U to R splits the O_U-algebra map O_U to s_*O_R; O_S is not the direct summand supplied by this section.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$s_*\mathcal{O}_R$ contains $\mathcal{O}_S$
+$s_*\mathcal{O}_R$ contains $\mathcal{O}_U$
````

### MC-STK-ERR-1541

`more-groupoids.tex` — more-groupoids.tex:2479; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L2479) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The construction has just defined W_1 and W-prime_1; W_0 and W-prime_0 do not exist in this proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$W_0$ is a thickening of $W'_0$
+$W_1$ is a thickening of $W'_1$
````

### MC-STK-ERR-1542

`more-groupoids.tex` — more-groupoids.tex:2661; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L2661) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The orbit of u_j was named {u_{j1},...,u_{jn_j}} and is consistently indexed first by j, then by i.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\{u_{ij}\}$
+$\{u_{ji}\}$
````

### MC-STK-ERR-1543

`more-groupoids.tex` — more-groupoids.tex:2750; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L2750) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

Orbits of the groupoid are subsets of U, and the proof immediately chooses r in R with source u and target u-prime.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$u, u' \in R$
+$u, u' \in U$
````

### MC-STK-ERR-1544

`more-groupoids.tex` — more-groupoids.tex:2944; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/more-groupoids.tex#L2944) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r47/candidate.manifest.json)

The principal open in Spec(A_h) is defined by f-prime, the image of f in A_h, exactly as in the preceding sentence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence $(j')^{-1}D(f)$ is affine.
+Hence $(j')^{-1}D(f')$ is affine.
````
