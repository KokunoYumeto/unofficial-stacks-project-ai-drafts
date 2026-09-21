# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## topologies

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/topologies.patch)

### MC-STK-ERR-1461

`topologies.tex` — topologies.tex:664,684; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L664-L684) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The site is (\Sch/S)_{Zar}; \Sh((\Sch/S)_{Zar}) is its topos. The proof evaluates F on site objects and constructs a presheaf on those objects, so removing only \Sh is the uniform minimal repair.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Given a sheaf $\mathcal{F}$ on $\Sh((\Sch/S)_{Zar})$
+Given a sheaf $\mathcal{F}$ on $(\Sch/S)_{Zar}$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we may define a presheaf $\mathcal{F}$ on $\Sh((\Sch/S)_{Zar})$
+we may define a presheaf $\mathcal{F}$ on $(\Sch/S)_{Zar}$
````

### MC-STK-ERR-1462

`topologies.tex` — topologies.tex:860,1522,1779,2055,2610; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L860-L2613) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

sets-lemma-what-is-in-it supplies object-existence facts but not combinatorial equivalence of coverings. Item (3) of sets-lemma-coverings-site is exactly the required result. Only the third citation in each proof changes.

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Moreover, $\{V_i \to T\}_{i \in I}$ is combinatorially equivalent to a
 covering $\{U_j \to T\}_{j \in J}$ of $T$ in the site
 $\Sch_\etale$ by
-Sets, Lemma \ref{sets-lemma-what-is-in-it}.
+Sets, Lemma \ref{sets-lemma-coverings-site}.
````

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Moreover, $\{V_i \to T\}_{i \in I}$ is combinatorially equivalent to a
 covering $\{U_j \to T\}_{j \in J}$ of $T$ in the site
 $\Sch_{smooth}$ by
-Sets, Lemma \ref{sets-lemma-what-is-in-it}.
+Sets, Lemma \ref{sets-lemma-coverings-site}.
````

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Moreover, $\{V_i \to T\}_{i \in I}$ is combinatorially equivalent to a
 covering $\{U_j \to T\}_{j \in J}$ of $T$ in the site
 $\Sch_{syntomic}$ by
-Sets, Lemma \ref{sets-lemma-what-is-in-it}.
+Sets, Lemma \ref{sets-lemma-coverings-site}.
````

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Moreover, $\{V_i \to T\}_{i \in I}$ is combinatorially equivalent to a
 covering $\{U_j \to T\}_{j \in J}$ of $T$ in the site
 $\Sch_{fppf}$ by
-Sets, Lemma \ref{sets-lemma-what-is-in-it}.
+Sets, Lemma \ref{sets-lemma-coverings-site}.
````

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Moreover, $\{V_i \to T\}_{i \in I}$ is combinatorially equivalent to a
 covering $\{U_j \to T\}_{j \in J}$ of $T$ in the site
 $\Sch_{ph}$ by
-Sets, Lemma \ref{sets-lemma-what-is-in-it}.
+Sets, Lemma \ref{sets-lemma-coverings-site}.
````

### MC-STK-ERR-1463

`topologies.tex` — topologies.tex:942; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L942) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The site is consistently denoted S_{affine, \etale}; this is the sole use of the text accent command inside that math identifier.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We omit the proof that $S_{affine, \'etale}$ is a site.
+We omit the proof that $S_{affine, \etale}$ is a site.
````

### MC-STK-ERR-1464

`topologies.tex` — topologies.tex:1251,2839; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L1251-L2839) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

Each following line declares f : X -> Y and g : Y -> Z. The second Y in the scheme list is unambiguously Z.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Given schemes $X$, $Y$, $Y$ in $\Sch_\etale$
+Given schemes $X$, $Y$, $Z$ in $\Sch_\etale$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Given schemes $X$, $Y$, $Y$ in $(\Sch/S)_{ph}$
+Given schemes $X$, $Y$, $Z$ in $(\Sch/S)_{ph}$
````

### MC-STK-ERR-1465

`topologies.tex` — topologies.tex:1324,1348; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L1324-L1349) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

As in candidate 1, \Sh denotes the topos, not the site on which the presheaf is defined.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Given a sheaf $\mathcal{F}$ on $\Sh((\Sch/S)_\etale)$
+Given a sheaf $\mathcal{F}$ on $(\Sch/S)_\etale$
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 we may define a presheaf $\mathcal{F}$ on
-$\Sh((\Sch/S)_\etale)$
+$(\Sch/S)_\etale$
````

### MC-STK-ERR-1466

`topologies.tex` — topologies.tex:1585,1842,1627,1884; editorial or notational clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L1585-L1887) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

Each marker is followed immediately by a further lemma. The same-source convention places this marker after the final proof and before the next section or file end. Preserve it verbatim and relocate it after each actual final proof.

Adverse evidence / qualification: Accepted as an editorial or notational source correction, not classified as a false theorem.

````diff
--- original
+++ replacement
@@ -1,4 +1 @@
-\noindent
-To be continued...
-
 \begin{lemma}
````

````diff
--- original
+++ replacement
@@ -1,4 +1 @@
-\noindent
-To be continued...
-
 \begin{lemma}
````

````diff
--- original
+++ replacement
@@ -2,3 +2,6 @@
 \ref{sites-lemma-have-functor-other-way-morphism} to get the
 formula for $f_{big, *}$.
 \end{proof}
+
+\noindent
+To be continued...
````

````diff
--- original
+++ replacement
@@ -2,3 +2,6 @@
 \ref{sites-lemma-have-functor-other-way-morphism} to get the
 formula for $f_{big, *}$.
 \end{proof}
+
+\noindent
+To be continued...
````

### MC-STK-ERR-1467

`topologies.tex` — topologies.tex:1955,1960; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L1955-L1964) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

An fppf cover assumes flat morphisms locally of finite presentation, not globally of finite presentation. The cited composition and base-change lemmas explicitly include the required local results, so their keys remain unchanged.

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
 The second follows as the composition of flat morphisms is flat
 (see Morphisms, Lemma \ref{morphisms-lemma-composition-flat})
-and the composition of morphisms of finite presentation is
-of finite presentation
+and the composition of morphisms which are locally of finite presentation is
+locally of finite presentation
 (see Morphisms, Lemma \ref{morphisms-lemma-composition-finite-presentation}).
````

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
 The third follows as the base change of a flat morphism is flat
 (see Morphisms, Lemma \ref{morphisms-lemma-base-change-flat})
-and the base change of a morphism of finite presentation is
-of finite presentation
+and the base change of a morphism which is locally of finite presentation is
+locally of finite presentation
 (see Morphisms, Lemma \ref{morphisms-lemma-base-change-finite-presentation}).
````

### MC-STK-ERR-1468

`topologies.tex` — topologies.tex:2353; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L2353) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The lemma has only items (1) and (2); this paragraph proves the iterated-cover refinement in item (2).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Proof of (3). Choose $U \to T$ proper surjective and
+Proof of (2). Choose $U \to T$ proper surjective and
````

### MC-STK-ERR-1469

`topologies.tex` — topologies.tex:2517; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L2517) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The affine cover has j-indexed outer members and the next line has l=1,...,n_j inner covers. The conventional outer bound is m. The identical text in candidate 12 is a distinct, line-scoped sibling.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-covering $U' = U'_1 \cup \ldots \cup U'$ such that
+covering $U' = U'_1 \cup \ldots \cup U'_m$ such that
````

### MC-STK-ERR-1470

`topologies.tex` — topologies.tex:2964; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L2964) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The ambient polynomial ring, the f_i, and the cited construction use t_i throughout. x_i is an isolated accidental rename.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$x_1, \ldots, x_m$. Then $p = (0, \ldots, 0, 1, 0, \ldots)$ with $1$
+$t_1, \ldots, t_m$. Then $p = (0, \ldots, 0, 1, 0, \ldots)$ with $1$
````

### MC-STK-ERR-1471

`topologies.tex` — topologies.tex:3470; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L3470) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The proof defines U -> T and g : Spec(V) -> T. X is undefined here, and properness supplies the lift over T.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Spec(K) \ar[r] & \Spec(V) \ar[r]^g & X
+\Spec(K) \ar[r] & \Spec(V) \ar[r]^g & T
````

### MC-STK-ERR-1472

`topologies.tex` — topologies.tex:3595; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L3595) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

As in candidate 9, the j-indexed finite outer cover requires terminal member U'_m; this replacement is restricted to the declared offset.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-covering $U' = U'_1 \cup \ldots \cup U'$ such that
+covering $U' = U'_1 \cup \ldots \cup U'_m$ such that
````

### MC-STK-ERR-1473

`topologies.tex` — topologies.tex:3798; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L3798-L3800) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The available arrows are X -> Y and Spec(V) -> U -> Y. Both products over X are ill-defined. The corrected object is Spec(V) x_Y X = Spec(V) x_U (U x_Y X), agreeing with the U_j cover used below.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 $$
-T = \Spec(V) \times_X Y = \Spec(V) \times_U (U \times_X Y)
+T = \Spec(V) \times_Y X = \Spec(V) \times_U (U \times_Y X)
 $$
````

### MC-STK-ERR-1474

`topologies.tex` — topologies.tex:4000; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L4000-L4001) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

Containment was defined by Cov(Sch_tau) being a subset of Cov(Sch'_tau'), so tau' has at least the covering families of tau and is the stronger/finer topology. The fppf-versus-etale example remains correct after the swap.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-In this case $\tau$ is stronger than $\tau'$, for example, no fppf
+In this case $\tau'$ is stronger than $\tau$, for example, no fppf
 site can be contained in an \'etale site.
````

### MC-STK-ERR-1475

`topologies.tex` — topologies.tex:4072; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L4072) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

F is on the smaller site and F' is on the larger site. The preceding sentence defines restriction from larger to smaller, so F' restricted to Sch_tau equals F; F cannot be restricted to the larger domain.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{F}|_{\Sch'_\tau} = \mathcal{F}'$. In fact the sheaf
+$\mathcal{F}'|_{\Sch_\tau} = \mathcal{F}$. In fact the sheaf
````

### MC-STK-ERR-1476

`topologies.tex` — topologies.tex:4201; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L4201) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

Condition (a) is the sheaf condition and condition (b) is continuity under directed affine limits. This paragraph invokes only the sheaf condition.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence the sheaf condition (b) for $F$ and the Zariski coverings
+Hence the sheaf condition (a) for $F$ and the Zariski coverings
````

### MC-STK-ERR-1477

`topologies.tex` — topologies.tex:4271,4276,4280; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L4271-L4283) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The argument has X = lim X_i and has just chosen i. V, V_i, and their opens are undefined here. Uniformly restoring X_i, X_{i,k}, X_k, and X_{i',k} refers to the declared inverse system.

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
-a finite affine open covering $V_i = V_{i, 1} \cup \ldots \cup V_{i, n}$
-such that $V_{i, k} \to S$ factors through an affine open of $S$.
-Let $V_k \subset V$ and $V_{i', k}$ for $i' \geq i$
-be the inverse images of $V_{i, k}$.
+a finite affine open covering $X_i = X_{i, 1} \cup \ldots \cup X_{i, n}$
+such that $X_{i, k} \to S$ factors through an affine open of $S$.
+Let $X_k \subset X$ and $X_{i', k}$ for $i' \geq i$
+be the inverse images of $X_{i, k}$.
````

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 $$
-F'_{V_k}(V_k) = \colim_{i' \geq i} F'_{V_{i', k}}(V_{i', k})
+F'_{X_k}(X_k) = \colim_{i' \geq i} F'_{X_{i', k}}(X_{i', k})
 $$
````

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 $$
-F'_{V_k \cap V_l}(V_k \cap V_l) =
+F'_{X_k \cap X_l}(X_k \cap X_l) =
 \colim_{i' \geq i}
-F'_{V_{i', k} \cap V_{i', l}}(V_{i', k} \cap V_{i', l})
+F'_{X_{i', k} \cap X_{i', l}}(X_{i', k} \cap X_{i', l})
````

### MC-STK-ERR-1478

`topologies.tex` — topologies.tex:4312,4316; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L4312-L4320) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

Both assertions start with coverings V_i and V'_i of T_i. The unindexed V is undefined; its required domain is V_i before and after base change.

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 $i' \geq i$ and a morphism
-$f_{i'} : T_{i'} \times_{T_i} \mathcal{V} \to
+$f_{i'} : T_{i'} \times_{T_i} \mathcal{V}_i \to
 T_{i'} \times_{T_i} \mathcal{V}'_i$
 whose base change to $T$ is $f$.
````

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
 \item If
-$f, g : \mathcal{V} \to \mathcal{V}'_i$
+$f, g : \mathcal{V}_i \to \mathcal{V}'_i$
 are morphisms of standard $\tau$-coverings of $T_i$ whose
 base changes $f_T, g_T$ to $T$ are equal then there exists an
 index $i' \geq i$ such that $f_{T_{i'}} = g_{T_{i'}}$.
````

### MC-STK-ERR-1479

`topologies.tex` — topologies.tex:4408,4411,4419,4429; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topologies.tex#L4408-L4434) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r45/candidate.manifest.json)

The colimit varies k', so its summand is F(V_{k'}), not constant F(V_k). Each Equalizer( must close after its xymatrix; these repairs preserve the stated equalizer/filtered-colimit argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim_{k' \geq k} F(V_k) \\
+\colim_{k' \geq k} F(V_{k'}) \\
````

````diff
--- original
+++ replacement
@@ -3,4 +3,4 @@
 \prod F(V_{k', i})
 \ar@<1ex>[r] \ar@<-1ex>[r] &
 \prod F(V_{k', i} \times_{V_{k'}} V_{k', j})
-}
+})
````

````diff
--- original
+++ replacement
@@ -5,4 +5,4 @@
 \ar@<1ex>[r] \ar@<-1ex>[r] &
 \colim_{k' \geq k}
 \prod F(V_{k', i} \times_{V_{k'}} V_{k', j})
-}
+})
````

````diff
--- original
+++ replacement
@@ -3,4 +3,4 @@
 \prod F'(X_i)
 \ar@<1ex>[r] \ar@<-1ex>[r] &
 \prod F'(X_i \times_X X_j)
-}
+})
````
