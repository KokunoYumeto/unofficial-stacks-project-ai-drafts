# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## spaces-perfect

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-perfect.patch)

### MC-STK-ERR-1545

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L492) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Close the outer argument of H^i(RF(tau_{<=a}E)); the displayed source cohomology group otherwise has an unmatched parenthesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item $H^i(RF(\tau_{\leq a}E) \to H^i(RF(E))$ is an isomorphism
+\item $H^i(RF(\tau_{\leq a}E)) \to H^i(RF(E))$ is an isomorphism
````

### MC-STK-ERR-1546

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L552) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The bound fixed by the lemma is N, and the stated truncation interval gives b+N; the lower-case n is not the asserted uniform bound.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we get the vanishing of $H^i(RF(E))$ for $i \geq b + n$ from
+we get the vanishing of $H^i(RF(E))$ for $i \geq b + N$ from
````

### MC-STK-ERR-1547

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1418) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Use the indexed affine member V_{p,i} throughout the induction. A statement only about the first member may be true but does not establish the required uniform assertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Note that $P$ holds for each $V_{p, 1}$ (as affine schemes) and for
+Note that $P$ holds for each $V_{p, i}$ (as affine schemes) and for
````

### MC-STK-ERR-1548

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1498) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Delete the redundant connector 'where' while retaining 'such that' and the full unchanged condition list.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(W_1 \subset W_2, f : V \to W_2)$ where 
+$(W_1 \subset W_2, f : V \to W_2)$
````

### MC-STK-ERR-1549

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1524) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The proof defines W_p by union and U_{n+1} is empty; W union U_{n+1} equals W, whereas the printed intersection does not give the base case.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Note that $P$ holds for $W_{n + 1} = W \cap U_{n + 1} = W$
+Note that $P$ holds for $W_{n + 1} = W \cup U_{n + 1} = W$
````

### MC-STK-ERR-1550

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1563) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The defined input is an elementary distinguished square; its derived constructions are triangles, not the input itself.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-In this section we prove that an elementary distinguished triangle
+In this section we prove that an elementary distinguished square
````

### MC-STK-ERR-1551

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1724) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Contravariant Hom gives the displayed left-exact sequence. The subsequent Ext^1 obstruction explicitly allows failure of surjectivity; 'left exact' is the precise minimal correction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the right exact functor $\Hom_{\mathcal{O}_X}(- , \mathcal{F})$
+the left exact functor $\Hom_{\mathcal{O}_X}(- , \mathcal{F})$
````

### MC-STK-ERR-1552

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1785) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

V to X is etale, not necessarily an inclusion. The overlap is U times_X V as already specified in the statement and subsequent formulas; intersection with its image is insufficient.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Similarly for $U$, $V$, and $U \cap V$ by
+Similarly for $U$, $V$, and $U \times_X V$ by
````

### MC-STK-ERR-1553

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1904) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Replace the unbound Y by X in V to X: the lemma restricts sheaves from X and forms V times_X U.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-spaces over $S$. Given an \'etale morphism $V \to Y$, set $W = V \times_X U$
+spaces over $S$. Given an \'etale morphism $V \to X$, set $W = V \times_X U$
````

### MC-STK-ERR-1554

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2279) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The stipulated morphism is j:V to W. Both its underived functor and the diagram use O_V; its derived functor must also have domain D(QCoh(O_V)).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Phi : D(\QCoh(\mathcal{O}_U)) \to D(\QCoh(\mathcal{O}_W))
+\Phi : D(\QCoh(\mathcal{O}_V)) \to D(\QCoh(\mathcal{O}_W))
````

### MC-STK-ERR-1555

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2586-L2588) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Correct both intermediate categories to QCoh(O_W), since j:U to W and g:W to Z; exact-left-adjoint preservation of K-injectives is applied on U and W.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Since $j_* : \QCoh(\mathcal{O}_U) \to \QCoh(\mathcal{O}_X)$
+Since $j_* : \QCoh(\mathcal{O}_U) \to \QCoh(\mathcal{O}_W)$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j^* : \QCoh(\mathcal{O}_X) \to \QCoh(\mathcal{O}_U)$
+$j^* : \QCoh(\mathcal{O}_W) \to \QCoh(\mathcal{O}_U)$
````

### MC-STK-ERR-1556

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2633) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Repair 'reside field' to 'residue field', matching the following kappa(p) and the cited injective-hull theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and therefore isomorphic to the injective hull of a reside field
+and therefore isomorphic to the injective hull of a residue field
````

### MC-STK-ERR-1557

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2639-L2645) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Restore the missing p in both numerator localizations A_mathfrak p; the intervening definition of Z_n and R=A_p substitution determine both exact occurrences.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A_\mathfrak/\mathfrak p^nA_\mathfrak p$, see
+$A_\mathfrak p/\mathfrak p^nA_\mathfrak p$, see
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finite $A_\mathfrak/\mathfrak p^nA_\mathfrak p$-module $J[\mathfrak p^n]$.
+finite $A_\mathfrak p/\mathfrak p^nA_\mathfrak p$-module $J[\mathfrak p^n]$.
````

### MC-STK-ERR-1558

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2642) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The sheaves (Z_n to S)_*G_n live on S=Spec(A), as specified by the lemma. X is unbound in this lemma; the pushforward must target S.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(Z_n \to X)_*\mathcal{G}_n$ where
+$(Z_n \to S)_*\mathcal{G}_n$ where
````

### MC-STK-ERR-1559

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2644) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Restore mathcal G_n in its defining phrase, matching the preceding pushforward and the statement. No second fraktur-named sheaf is introduced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak G_n$ the coherent sheaf associated to the
+$\mathcal G_n$ the coherent sheaf associated to the
````

### MC-STK-ERR-1560

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2891) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The refined etale neighbourhood X'' must still contain a point above x; repeating that condition only for X' does not make its image a neighbourhood. Replace X' by X'' in this locus.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in the image of $X' \to X$ and such that
+in the image of $X'' \to X$ and such that
````

### MC-STK-ERR-1561

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3040) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The stalk is at the chosen geometric point overline{x}, not the whole space X; the cited strict-henselization description and following formula both fix that index.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Since the stalk of $\mathcal{O}_{X_\etale}$ at $X$ is
+Since the stalk of $\mathcal{O}_{X_\etale}$ at $\overline{x}$ is
````

### MC-STK-ERR-1562

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3633) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

Supply the base X in W times_X V, the overlap used by every adjacent restriction and the fixed elementary distinguished square. Preserve both maps and the other terms.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Q|_{W \times_X V} \to (P \oplus P[1])|_{W \times V}
+Q|_{W \times_X V} \to (P \oplus P[1])|_{W \times_X V}
````

### MC-STK-ERR-1563

`spaces-perfect.tex` — ; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3812) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r48/candidate.manifest.json)

The chosen functions and Koszul complex both end at s; the same sequence's zero locus must end at g_s, not the unbound g_r.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f^{-1}(Z \cap T) = V(g_1, \ldots, g_r)$.
+$f^{-1}(Z \cap T) = V(g_1, \ldots, g_s)$.
````
