# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## descent

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/descent.patch)

### MC-STK-ERR-1402

`descent.tex` — descent.tex:6663; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L6663) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

The statement lists six topologies in order but only five corresponding precomposition classes; smooth is the missing fourth class between syntomic and etale.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-resp.\ \'etale, resp.\ an open immersion, the composition
+resp.\ smooth, resp.\ \'etale, resp.\ an open immersion, the composition
````

### MC-STK-ERR-1403

`descent.tex` — descent.tex:6790; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L6790) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

The sentence introducing the displayed predicate requires the definite article; no mathematical token changes.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then property
+The property
````

### MC-STK-ERR-1404

`descent.tex` — descent.tex:6876; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L6876) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

For f:X->Y and Xi->X, the named compositions are Xi->X->Y. The proof compares their universal openness as maps to Y; the preferred full-line repair also supplies the missing English 'by'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $f_i : X_i \to X$ the compositions.
+Denote by $f_i : X_i \to Y$ the compositions.
````

### MC-STK-ERR-1405

`descent.tex` — descent.tex:7081; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7081) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

Here xi lies in Xi and fi:Xi->Yi is the base change; f has domain X. The next line uses gi(fi(xi))=f(hi(xi)).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $\mathcal{P}(f)$. Let $f(x_i) \leadsto y_i$
+Assume $\mathcal{P}(f)$. Let $f_i(x_i) \leadsto y_i$
````

### MC-STK-ERR-1406

`descent.tex` — descent.tex:7105; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7105) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

Since fi=f composed with hi has domain Xi, the specialization of xi must start at fi(xi), as confirmed by the following f(hi(xi)).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f(x_i) \leadsto y$ be a specialization. Then $f(h_i(x_i)) \leadsto y$ so
+$f_i(x_i) \leadsto y$ be a specialization. Then $f(h_i(x_i)) \leadsto y$ so
````

### MC-STK-ERR-1407

`descent.tex` — descent.tex:7132; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7132) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

The construction introduces two evident morphisms a and b, so the copula and plural agreement are both required.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$V = X \amalg Y$, let $a, b$ the obvious map, and let $h : U \to V$
+$V = X \amalg Y$, let $a, b$ be the obvious maps, and let $h : U \to V$
````

### MC-STK-ERR-1408

`descent.tex` — descent.tex:7292; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7292) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

The copula is missing. Condition (g) combines the target-cover and source-cover reductions already proved equivalent to (a).

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(a) equivalent to (g).
+(a) is equivalent to (g).
````

### MC-STK-ERR-1409

`descent.tex` — descent.tex:7481; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7481) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

The diagram identifies X and X'=f_Y^{-1}(Y') as the two pieces covering X times_Z Y. X times_Y Z is not defined because no map Z->Y is given.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\{X \to X \times_Z Y, X' \to X \times_Y Z\}$ is an \'etale covering,
+$\{X \to X \times_Z Y, X' \to X \times_Z Y\}$ is an \'etale covering,
````

### MC-STK-ERR-1410

`descent.tex` — descent.tex:7511; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7511) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

The standard property, and the cited lemma name immediately below it, are 'locally of finite type'. The existing public comment on this tag concerns adding surjective and is unrelated.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item locally finite type, see
+\item locally of finite type, see
````

### MC-STK-ERR-1411

`descent.tex` — descent.tex:7609; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7609) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

Line 7606 already names the restriction f'|_{U'}:U'->V'; after composition with V'->Y', the same restricted morphism to Y' is meant. The subscripted f'_{U'} is undefined here.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we conclude that $f'_{U'} : U' \to Y'$ has $\mathcal{P}$.
+we conclude that $f'|_{U'} : U' \to Y'$ has $\mathcal{P}$.
````

### MC-STK-ERR-1412

`descent.tex` — descent.tex:7622; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7622) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r40/candidate.manifest.json)

The restriction is to the open U' in X'. Braces are required so the prime belongs to the subscript; the same restriction is written correctly at lines 7602, 7603, and 7615.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-morphism $g'|_U' : U' \to X$. Then $\{U' \to U\}$
+morphism $g'|_{U'} : U' \to X$. Then $\{U' \to U\}$
````

### MC-STK-ERR-1413

`descent.tex` — descent.tex:7632; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7632) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/candidate.manifest.json)

English requires 'denote by T the automorphism'; the full-line guard distinguishes this locus from the parallel omission at line 7779 and changes no mathematical object.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$i \not = j$ and $d \geq 0$ denote $T_{i, j, d}$ the automorphism
+$i \not = j$ and $d \geq 0$ denote by $T_{i, j, d}$ the automorphism
````

### MC-STK-ERR-1414

`descent.tex` — descent.tex:7652; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7652) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/candidate.manifest.json)

Line 7650 defines the chosen point as xi=(xi_1,...,xi_n), and line 7666 immediately renumbers so xi_n is transcendental; x_i denotes an ambient coordinate function, not the chosen coordinate value.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such that at least one of $x_1, \ldots, x_n$ is transcendental over the
+such that at least one of $\xi_1, \ldots, \xi_n$ is transcendental over the
````

### MC-STK-ERR-1415

`descent.tex` — descent.tex:7712; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7712) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/candidate.manifest.json)

The morphism g:Y'->Y is assumed smooth at the domain point y'; the proof then works in open neighbourhoods of y' and uses smooth locality on the target.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such that $g$ is smooth $y'$ and $X' \to X \times_Y Y'$ is \'etale
+such that $g$ is smooth at $y'$ and $X' \to X \times_Y Y'$ is \'etale
````

### MC-STK-ERR-1416

`descent.tex` — descent.tex:7718; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7718-L7720) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/candidate.manifest.json)

For the etale morphism X'->X times_Y Y' at x', source locality compares x' in W(f') with its image in the base-change open. The point x alone has no chosen lift to the fibre product, and x in W(f) is the conclusion still being proved.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 Since $\mathcal{P}$ is \'etale local on the source we see
-that $x \in W(f)$ if and only if the image of $x$ in
+that $x' \in W(f')$ if and only if the image of $x'$ in
 $X \times_Y Y'$ is in $W(X \times_Y Y' \to Y')$. Hence we
````

### MC-STK-ERR-1417

`descent.tex` — descent.tex:7779; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7779) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/candidate.manifest.json)

English requires 'denote by T the automorphism'; this full-line guard is unique despite the parallel omission at line 7632 and changes no mathematical object.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote $T_{i, j, d}$ the automorphism of $\mathbf{A}^n$ defined
+denote by $T_{i, j, d}$ the automorphism of $\mathbf{A}^n$ defined
````

### MC-STK-ERR-1418

`descent.tex` — descent.tex:7814; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7814) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r41/candidate.manifest.json)

No standalone W is introduced in this proof; lines 7748--7753 establish W(f_n), and applying the cited etale-locality lemma to the T_p square gives invariance of that open on the fibre over x.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-T_p^{-1}(W) \cap \mathbf{A}^n_x = W \cap \mathbf{A}^n_x
+T_p^{-1}(W(f_n)) \cap \mathbf{A}^n_x = W(f_n) \cap \mathbf{A}^n_x
````

### MC-STK-ERR-1419

`descent.tex` — descent.tex:7896; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7896) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

The associated property is defined as mathcal Q at lines 7856--7865 and item (2) of this lemma again names it mathcal Q at line 7904; bare Q is an inconsistent notation.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $Q$ be the associated property
+Let $\mathcal{Q}$ be the associated property
````

### MC-STK-ERR-1420

`descent.tex` — descent.tex:8051; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8051) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

The vertical etale maps give finite separable residue-field extensions kappa(u')/kappa(u) and kappa(v')/kappa(v), so invariance of transcendence degree compares kappa(u') over kappa(v') with kappa(u) over kappa(v); the unprimed final u is ill-typed for the right-hand base field.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\text{trdeg}_{\kappa(v)} \kappa(u) = \text{trdeg}_{\kappa(v')} \kappa(u)$
+$\text{trdeg}_{\kappa(v)} \kappa(u) = \text{trdeg}_{\kappa(v')} \kappa(u')$
````

### MC-STK-ERR-1421

`descent.tex` — descent.tex:8141; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8141) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

The sentence lacks its finite copula; inserting 'is' yields the grammatical explanation 'This is because' and changes neither fibre-product identity.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-This because $X \times_{\Delta, X \times_S X} (V \times_S X) = V$
+This is because $X \times_{\Delta, X \times_S X} (V \times_S X) = V$
````

### MC-STK-ERR-1422

`descent.tex` — descent.tex:8362; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8362) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

Line 8355 defines mathcal V as the family {V_j -> S}; S' is instead the target of the U_i family, so the stated V-family base must be S.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-family $\{V_j \to S'\}$. The system
+family $\{V_j \to S\}$. The system
````

### MC-STK-ERR-1423

`descent.tex` — descent.tex:8370; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8370) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

The displayed system is indexed by i and obtained by pulling the V-data to U_i via g_i, hence it is descent data relative to mathcal U; keeping mathcal V contradicts the construction and the change-of-base direction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a descent datum relative to $\mathcal{V}$.
+is a descent datum relative to $\mathcal{U}$.
````

### MC-STK-ERR-1424

`descent.tex` — descent.tex:8423; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8423) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

English requires 'denote by O this datum'; inserting 'by' is the minimal grammatical repair and changes no mathematical object.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote $(X \times_S U, can)$ this descent datum.
+denote by $(X \times_S U, can)$ this descent datum.
````

### MC-STK-ERR-1425

`descent.tex` — descent.tex:8453; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8453) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

English requires 'denote this datum by O'; inserting 'by' is the minimal grammatical repair and changes no indexed object.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We denote this descent datum $(X_i \times_S U, can)$.
+We denote this descent datum by $(X_i \times_S U, can)$.
````

### MC-STK-ERR-1426

`descent.tex` — descent.tex:8472; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8472) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

The standard noun corresponding to 'fully faithful' is 'full faithfulness'; 'fully faithfulness' is ungrammatical and the section body immediately states that the functor is fully faithful.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\section{Fully faithfulness of the pullback functors}
+\section{Full faithfulness of the pullback functors}
````

### MC-STK-ERR-1427

`descent.tex` — descent.tex:8708,8727; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8708-L8727) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

In each factorization X -> X times_S X' -> X', the first arrow is the graph of f and the first projection is its retraction; the graph is a section, but is not thereby a morphism having a section. Both repeated proofs require 'has a retraction' to invoke the equivalence lemma in the correct categorical direction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The first morphism has a section
+The first morphism has a retraction
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The first morphism has a section
+The first morphism has a retraction
````

### MC-STK-ERR-1428

`descent.tex` — descent.tex:8718; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8718-L8719) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

The hypothesis is that X -> S is an fpqc covering. Surjectivity, flatness, and quasi-compactness of the different morphism f:X->X' do not imply that hypothesis, so the parenthetical sufficient condition must refer to X -> S. The full two-line guard avoids changing the valid f-based parenthetical at lines 8565--8566.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Assume $\{X \to S\}$ is an fpqc covering (for example if $f$ is
+Assume $\{X \to S\}$ is an fpqc covering (for example if $X \to S$ is
 surjective, flat and quasi-compact).
````

### MC-STK-ERR-1429

`descent.tex` — descent.tex:8766; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8766) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r42/candidate.manifest.json)

The family morphisms are g_i:U_i->V_{alpha(i)} indexed by i in I, while alpha(i) lies in J and does not index a g-map; the ith coproduct component is therefore mapped by g_i.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-via the morphism $g_{\alpha(i)}$
+via the morphism $g_i$
````

### MC-STK-ERR-1430

`descent.tex` — descent.tex:8830; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8830) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/candidate.manifest.json)

Full faithfulness already implies faithfulness, so the phrase 'faithful and fully faithful' is redundant; the minimal repair retains the mathematically stronger property used by the cited result.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The functor is faithful and fully faithful by
+The functor is fully faithful by
````

### MC-STK-ERR-1431

`descent.tex` — descent.tex:8955; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8955-L8956) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/candidate.manifest.json)

The sentence refers to one collection of gluing isomorphisms satisfying the cocycle condition, so the singular count noun is 'datum', not 'data'.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 is a glueing
-data as in Schemes
+datum as in Schemes
````

### MC-STK-ERR-1432

`descent.tex` — descent.tex:8976; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8976) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/candidate.manifest.json)

The initialism 'fpqc' begins with a vowel sound, so the indefinite article is 'an'.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-relative to a fpqc-covering
+relative to an fpqc-covering
````

### MC-STK-ERR-1433

`descent.tex` — descent.tex:8986; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8986) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/candidate.manifest.json)

The adverb modifying the recurring condition is 'sometimes'; 'sometime' denotes an unspecified time and is not grammatical here.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then it is sometime the
+then it is sometimes the
````

### MC-STK-ERR-1434

`descent.tex` — descent.tex:9060; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L9060) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/candidate.manifest.json)

The phrasal verb is 'pull back'; the closed compound 'pullback' is a noun or adjective, not the finite verb required after 'we'.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-if we pullback
+if we pull back
````

### MC-STK-ERR-1435

`descent.tex` — descent.tex:9125; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L9125) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/candidate.manifest.json)

The proof shrinks the affine base opens S_i covering S so that their pullbacks X_i retain the desired property; the smaller affine opens are therefore opens of S, not opens of X.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-restricting to smaller affine opens in $X$.
+restricting to smaller affine opens in $S$.
````

### MC-STK-ERR-1436

`descent.tex` — descent.tex:9395; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L9395) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r43/candidate.manifest.json)

English requires 'denote by F_i the sheaf'; inserting 'by' is the minimal grammatical repair and changes no mathematical object.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For each $i$ denote $F_i$ the sheaf
+For each $i$ denote by $F_i$ the sheaf
````
