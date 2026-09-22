# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## categories

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/categories.patch)

### MC-STK-ERR-0056

`categories.tex` — 7005-7008; composition order error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7005-L7008) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: lift g after f → lift f after g

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Let $x \in \Ob(\mathcal{S}_U)$. By the first condition we can lift
 $f$ to $ \phi : y \to x$ and then we can lift $g$ to $\psi : z \to y$.
-Instead of doing this two step process we can directly lift $g \circ f$ to
+Instead of doing this two step process we can directly lift $f \circ g$ to
 $\gamma : z' \to x$. This gives the solid arrows in the diagram
````

### MC-STK-ERR-0057

`categories.tex` — 7046-7050; pseudofunctor index order error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7046-L7050) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: alpha_{f,g} → alpha_{g,f}

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
 strongly cartesian. In addition, given $f^\ast x \to x$
 lying over $f$ for all $f: V \to U = p(x)$ the data
-$(U \mapsto \mathcal{S}_U, f \mapsto f^*, \alpha_{f, g}, \alpha_U)$
+$(U \mapsto \mathcal{S}_U, f \mapsto f^*, \alpha_{g, f}, \alpha_U)$
 constructed in Lemma \ref{lemma-fibred}
 defines a pseudo functor from $\mathcal{C}^{opp}$ in to
````

### MC-STK-ERR-0058

`categories.tex` — 7425-7429; missing calligraphic symbol.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7425-L7429) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: plain I_S → calligraphic I_S

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
 Lemma \ref{lemma-inertia-fibred-category}
 or by using (from the same lemma) that
-$I_\mathcal{S} \to \mathcal{S}
+$\mathcal{I}_\mathcal{S} \to \mathcal{S}
 \times_{\Delta, \mathcal{S} \times_\mathcal{C} \mathcal{S}, \Delta}\mathcal{S}$
 is an equivalence and appealing to
````

### MC-STK-ERR-0059

`categories.tex` — 7603-7623; composition order error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7603-L7623) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: d to b after c → d to c after b

````diff
--- original
+++ replacement
@@ -18,4 +18,4 @@
 (p(x), b^{-1}(b(x)), g(b(x)), \alpha_x \circ F(\beta_x))
 $$
 is a functorial isomorphism which gives our $2$-morphism
-$d \to b \circ c$. Finally, if the diagram commutes then
+$d \to c \circ b$. Finally, if the diagram commutes then
````

### MC-STK-ERR-0060

`categories.tex` — 9142-9149; duplicated operator error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9142-L9149) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: duplicated composition operator → single composition operator

````diff
--- original
+++ replacement
@@ -4,5 +4,5 @@
 \circ
 1 \circ (\text{id}_\mathbf{1} \otimes b) \circ 1^{-1}
 =
-1 \circ (a \otimes b) \circ \circ 1^{-1}
+1 \circ (a \otimes b) \circ 1^{-1}
 $$
````

### MC-STK-ERR-0061

`categories.tex` — 9480-9483; bifunctor domain error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9480-L9483) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: tensor bifunctor domain C tensor C → categorical product domain C times C

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 A quadruple $(\mathcal{C}, \otimes, \phi, \psi)$ where
 $\mathcal{C}$ is a category,
-$\otimes : \mathcal{C} \otimes \mathcal{C} \to \mathcal{C}$ is a functor,
+$\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ is a functor,
 $\phi$ is an associativity constraint, and
````

### MC-STK-ERR-0062

`categories.tex` — 8840-8852; representable slice error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L8840-L8852) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: three malformed C/U times V representables → three C/(U times V) representables

````diff
--- original
+++ replacement
@@ -1,13 +1,13 @@
 Suppose the diagonal is representable, and let $U, G$ be given.
 Consider any $V \in \Ob(\mathcal{C})$ and any
 $G' : \mathcal{C}/V \to \mathcal{S}$.
-Note that $\mathcal{C}/U \times \mathcal{C}/V = \mathcal{C}/U \times V$
+Note that $\mathcal{C}/U \times \mathcal{C}/V = \mathcal{C}/(U \times V)$
 is representable. Hence the fibre product
 $$
 \xymatrix{
-(\mathcal{C}/U \times V)
+(\mathcal{C}/(U \times V))
 \times_{(\mathcal{S} \times \mathcal{S})}
 \mathcal{S}
 \ar[r] \ar[d] &
 \mathcal{S} \ar[d] \\
-\mathcal{C}/U \times V \ar[r]^{(G, G')} &
+\mathcal{C}/(U \times V) \ar[r]^{(G, G')} &
````

### MC-STK-ERR-0396

`categories.tex` — categories.tex:655-706;1071-1115; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L661) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-amalgamated sum
+sum
````

### MC-STK-ERR-1605

`categories.tex` — 385; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L385) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Line 379 defines j(phi) to be the unique morphism whose F-image is phi'. The right vertical map is therefore F(j(phi)); explicitly grouping the evaluation removes the misleading composition sign between a functor and an already evaluated morphism.

Adverse evidence / qualification: A reader may parse F circ j(phi) as shorthand for (F circ j)(phi); the commutative square already fixes the intended map. This is a notation clarification, not a defective equivalence theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-F\circ j(\phi)
+F(j(\phi))
````

### MC-STK-ERR-1606

`categories.tex` — 852; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L852) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The same morphism is denoted by the Greek mathematical symbol in the next sentence and in both defining equations. Restore its consistent typesetting.

Adverse evidence / qualification: The spelling delta is intelligible and changes no map; classify as a copyedit, not a proof repair.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-uniqueness of delta.
+uniqueness of $\delta$.
````

### MC-STK-ERR-1607

`categories.tex` — 1225, 1226, 1227, 1228, 1247, 1262, 1263; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1225-L1263) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Specify the structural maps of the universal object. The displayed square uses identity projections, and its universal property forces alpha=beta. An arbitrary abstract isomorphism X times_Y X congruent X would not suffice: an infinite countable set maps noninjectively to a singleton while its square is abstractly isomorphic to itself. The dual assertion follows in the opposite category. This wording does not assume fibre products or pushouts exist beforehand.

Adverse evidence / qualification: The ordinary phrase X is the fibre product is often understood to include its evident structure maps, and the displayed proof already gives them. Do not claim the intended theorem was false; the repair removes an ambiguity made explicit by the bare congruence in the reverse implication.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item $f$ is a monomorphism if and only if $X$ is the fibre
+\item $f$ is a monomorphism if and only if $X$, with both projections
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-product $X \times_Y X$, and
+equal to $\text{id}_X$, is a fibre product of $X$ with itself over $Y$, and
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item $f$ is an epimorphism if and only if $Y$ is the pushout
+\item $f$ is an epimorphism if and only if $Y$, with both coprojections
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$Y \amalg_X Y$.
+equal to $\text{id}_Y$, is a pushout of $Y$ with itself over $X$.
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Suppose that $X \times_Y X \cong X $. The diagram
+Suppose that $X$, with both projections equal to $\text{id}_X$, is
+a fibre product of $X$ with itself over $Y$. The diagram
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The proof is exactly the same for the second point, but with the
+The second assertion follows by applying the first assertion to the
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-pushout $Y\amalg_X Y = Y$.
+opposite category.
````

### MC-STK-ERR-1608

`categories.tex` — 1692; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1692) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The common morphism W to X equips W with an object structure in the slice category. It does not define an object of W.

Adverse evidence / qualification: The immediately surrounding argument determines the intended slice structure; no new existence statement is added.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-object of $W$ in $\mathcal{C}/X$
+object of $\mathcal{C}/X$ on $W$
````

### MC-STK-ERR-1609

`categories.tex` — 1734; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1734) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The subject is the single sequence of morphisms. By contrast, the neighboring clause at 1731 quantifies an object AND a morphism, a coordinated subject for which plural exist is defensible; leave that clause unchanged.

Adverse evidence / qualification: Grammar only; the following endpoint condition is already present and unchanged. Do not generalize the replacement to coordinated existential clauses.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist a sequence
+there exists a sequence
````

### MC-STK-ERR-1610

`categories.tex` — 1791; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1791) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

A path in the comma category must connect the two specified objects (x,H(x)->y) and (x',H(x')->y), not arbitrary morphisms with those underlying x-values. The dual cofinal definition explicitly fixes endpoints at 1741, and 1806 says this definition is its dual. Without the requirement, the functor from a terminal category to a one-object category of a nontrivial group would satisfy the printed weakened condition (choose n=0 and ignore the given arrows), while its relevant comma category is a disconnected discrete set of group elements.

Adverse evidence / qualification: The author plainly intends the given endpoints, and a reader may supply that convention from context. The correction makes that necessary requirement explicit rather than changing the intended notion.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
 in $\mathcal{I}$ and morphisms $H(x_i) \to y$ in $\mathcal{J}$
+with $H(x_0) \to y$ and $H(x_{2n}) \to y$ the given morphisms
````

### MC-STK-ERR-1611

`categories.tex` — 1786; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1786) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The sequence subject is singular, as in the cofinal definition. This verb repair is independent of the missing endpoint condition. The neighboring object-and-morphism coordinated subject at 1782 remains unchanged.

Adverse evidence / qualification: No change to quantifier scope, sequence length or existence hypotheses.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist a sequence
+there exists a sequence
````

### MC-STK-ERR-1612

`categories.tex` — 1868; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1868) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Two categories are introduced; the singular article before the plural noun is malformed.

Adverse evidence / qualification: Deleting the article changes no connectedness hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be a categories
+be categories
````

### MC-STK-ERR-1613

`categories.tex` — 1946, 1953, 1955; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1946-L1955) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The family in the limit cone is indexed by objects of J, here y_i and z_i. The two components have domains W and agree because F(h_i) maps to the identity. Their common value then defines q_i. Restore subscripts rather than the meaningless product-like qy_i notation. Both producer reports describe the same six occurrences and are one correction group.

Adverse evidence / qualification: The printed types W to M(F(y_i)) and W to M(F(z_i)) make the intent recoverable. This fixes cone-component notation, not the limit comparison construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-qy_i
+q_{y_i}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-qz_i
+q_{z_i}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-qy_i
+q_{y_i}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-qz_i
+q_{z_i}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-qy_{s(j)}
+q_{y_{s(j)}}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-qz_{t(j)}
+q_{z_{t(j)}}
````

### MC-STK-ERR-1614

`categories.tex` — 1997; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L1997) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The comma separates the final displayed item in the finite object enumeration.

Adverse evidence / qualification: The omitted-index notation and the actual set of objects are already clear; classify as presentation only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ldots x_n
+\ldots, x_n
````

### MC-STK-ERR-1615

`categories.tex` — 2012; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2012) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The newly defined functor M' has domain I'. Its morphism from x to y_j is f', corresponding to f in the old category I. Thus M'(f') equals M(f) after the first projection. The old argument of M on the right remains unchanged.

Adverse evidence / qualification: A reader might identify corresponding arrows informally, but the preceding sentence expressly gives them different names and source objects.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M'(f)
+M'(f')
````

### MC-STK-ERR-1616

`categories.tex` — 2018; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2018) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The equalizers are constructed in C, where the hypothesis provides them. The index arrows x_1 to y_j induce the parallel arrows between M-images; these are the arrows being equalized.

Adverse evidence / qualification: Applying the diagram functor may be intended implicitly. The repair makes the category of the equalizer explicit without changing the finite-limit argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the successive equalizer of pairs of maps $x_1 \to y_j$ hence
+the successive equalizer of pairs of induced maps $M(x_1) \to M(y_j)$ hence
````

### MC-STK-ERR-1617

`categories.tex` — 2246; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2246) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Restore the conventional spelling of the compound adjective.

Adverse evidence / qualification: No mathematical content or hypothesis changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finegrained
+fine-grained
````

### MC-STK-ERR-1618

`categories.tex` — 2291; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2291) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The named additional condition is in the cited lemma; its connecting preposition is missing.

Adverse evidence / qualification: The reference target and example remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-condition Lemma
+condition in Lemma
````

### MC-STK-ERR-1619

`categories.tex` — 2388; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2388) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The diagram has n two-arrow spans and vertices i_0 through i_{2n}. The endpoint element at 2405 is n_{i_{2n}}=m', and n is the induction parameter. Both producer reports identify the same inconsistent endpoint index.

Adverse evidence / qualification: Renaming n throughout would be larger and would disrupt the induction. Correct only the introductory endpoint.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i_n = i'
+i_{2n} = i'
````

### MC-STK-ERR-1620

`categories.tex` — 2433; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2433) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The induction uses a shorter chain, not shorter elements. Name the subject explicitly and separate the sentence while preserving the displayed chain, all its elements and the conclusion.

Adverse evidence / qualification: The intended antecedent is already recoverable from the display, so classify this as prose repair rather than a new inductive argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and the elements $n_{i_j}$ for $j \geq 3$ which has a smaller length
+together with the elements $n_{i_j}$ for $j \geq 3$. This chain has smaller length
````

### MC-STK-ERR-1621

`categories.tex` — 2850; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2850) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The fixed convention at 2579 uses (I,leq), and 2594 defines geq to be its reverse. A greatest element for leq is terminal for the associated category at 2599–2601 and computes colimits. Match that convention in the remark.

Adverse evidence / qualification: One can name an arbitrary ordering by a geq symbol and interpret greatest relative to it, but here geq has already been defined as the opposite of leq. This is notation consistency, not a new finite-colimit theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(I, \geq)$
+$(I, \leq)$
````

### MC-STK-ERR-1622

`categories.tex` — 2623, 2624; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2623-L2624) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The sentence supplies notation for the direct and inverse cases just defined. The revised sentence fixes the broken article/parenthesis construction and places the infinitive after the notation it introduces. Both reports concern the same sentence.

Adverse evidence / qualification: The transition-map directions remain exactly as defined in the preceding two items.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We will say $(M_i, f_{ii'})$ is a (inverse) system over $I$ to
+We will use $(M_i, f_{ii'})$ to denote a system or an inverse system
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote this. The maps $f_{ii'}$ are sometimes
+over $I$. The maps $f_{ii'}$ are sometimes
````

### MC-STK-ERR-1623

`categories.tex` — 2669, 2670; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2669-L2670) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Pullback along pi sends a system N on the quotient preorder to M_i=N_pi(i) on I. The same construction works contravariantly for inverse systems. The following choice of section gives a quasi-inverse in either case, and the final paragraph explicitly uses systems/colimits before mentioning inverse systems/limits.

Adverse evidence / qualification: The original surrounding paragraph already makes both cases inferable, so classify as clarification of scope and direction rather than a missing proof or a new equivalence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-This construction defines a functor between the category
+This construction defines a functor from the category of (inverse)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of inverse systems over $I$ and $\overline{I}$.
+systems over $\overline{I}$ to the corresponding category over $I$.
````

### MC-STK-ERR-1624

`categories.tex` — 2801; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2801) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

F is a subcategory of I times omega, its cocone is constructed there, and the added terminal object has an omega-coordinate strictly larger than all F-coordinates. Consequently F+ remains in the product category. Only afterward does cofinality of the projection justify the reduction.

Adverse evidence / qualification: The later proof may rename the reduced index category as I, but no such renaming has occurred inside this construction. Both producers describe the same ambient-category omission.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-subcategory of $\mathcal{I}$
+subcategory of $\mathcal{I} \times \omega$
````

### MC-STK-ERR-1625

`categories.tex` — 2856; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2856) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Restore the established category-name typesetting used in the immediately following lemma.

Adverse evidence / qualification: The word Sets is intelligible as a category name already; do not claim a semantic multiplication error or a changed example.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\to Sets
+\to \textit{Sets}
````

### MC-STK-ERR-1626

`categories.tex` — 2993; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2993) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The sentence coordinates two imperative definitions, Let M ... and let S ...; the extra infinitive marker is stray.

Adverse evidence / qualification: The shift operator, colimit and nonessential-constancy example are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and to let
+and let
````

### MC-STK-ERR-1627

`categories.tex` — 3072; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3072) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The preceding sentence defines m(n',n) only for n' at least n, dominating m(n') and m(n). That is precisely the index of the diagram's common source. Both reports refer to this same reversed pair.

Adverse evidence / qualification: For n'=n both notations coincide, but the compatibility condition ranges over all n' at least n.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-X_{m(n, n')}
+X_{m(n', n)}
````

### MC-STK-ERR-1628

`categories.tex` — 3076; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3076) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

m(k,l) is selected only for k at least l. The triangular index set removes undefined terms. Its maximum contains every m(k,l) with l at most k at most n, hence dominates m(n) via m(n,n), is nondecreasing in n, and enforces each required compatibility square. The two reports are duplicates of one repair.

Adverse evidence / qualification: One could extend the pair-index function by an extra convention, but no such convention is stated; restricting the finite range is the smaller fix.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\max_{k, l \leq n}
+\max_{l \leq k \leq n}
````

### MC-STK-ERR-1629

`categories.tex` — 3094; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3094) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The comparison quantifies a common refinement m' dominating the two representative index maps m_1 and m_2. The second pair must introduce m_2 instead of repeating m_1. Both reports identify the same token.

Adverse evidence / qualification: Representatives can happen to have equal index maps, but the asserted criterion is for arbitrary representatives, not only that special case.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(m_1, a_2)$
+$(m_2, a_2)$
````

### MC-STK-ERR-1630

`categories.tex` — 3432; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3432) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The clause refers to the specific natural first arrow just displayed and is missing its determiner. The two producer reports are the same copyedit.

Adverse evidence / qualification: The natural map and counit map remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is natural one
+is the natural one
````

### MC-STK-ERR-1631

`categories.tex` — 3490; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3490) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The first sentence and displayed Hom calculation concern maps from colim M_i. Its compatible source maps are from the diagram objects of that colimit, not from a limit object. Both reports locate this same noun mismatch.

Adverse evidence / qualification: The following displayed calculation is already correct, so the repair fixes prose terminology, not the adjoint-preserves-colimits theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-constituents of the limit
+constituents of the colimit
````

### MC-STK-ERR-1632

`categories.tex` — 3528; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3528) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Applying u to the unit X to v(u(X)) gives codomain u(v(u(X))), which is the counit's source in the next arrow. Close the missing outer application parenthesis. Both producers report the same delimiter.

Adverse evidence / qualification: The unit/counit triangle already makes the intended object clear; no adjunction identity changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-u(v(u(X))
+u(v(u(X)))
````

### MC-STK-ERR-1633

`categories.tex` — 3559; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3559) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

At fixed C,D the displayed Hom expression is one map, followed by the singular is the map. Make the subject singular.

Adverse evidence / qualification: The construction is natural in C,D, but that does not make the displayed single Hom-map a plural subject in this sentence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the induced maps
+the induced map
````

### MC-STK-ERR-1634

`categories.tex` — 3590; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3590) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The where clause continues the preceding displayed equation inside the same list item; it is not a standalone sentence.

Adverse evidence / qualification: Capitalization only; the counit formula and label remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Where $\epsilon$
+where $\epsilon$
````

### MC-STK-ERR-1635

`categories.tex` — 3613; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3613) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The comma separates because from its clause subject without an intervening parenthesis. Deleting it suffices; no need to rewrite the demonstrative.

Adverse evidence / qualification: The composition of the two bijections is already specified correctly.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-because, this
+because this
````

### MC-STK-ERR-1636

`categories.tex` — 3631; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3631) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

A semicolon separates the assertion from the independent imperative without altering either clause.

Adverse evidence / qualification: Punctuation only; the representability statement and reference are untouched.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-big categories, please
+big categories; please
````

### MC-STK-ERR-1637

`categories.tex` — 3817; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3817) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The bound index is j in J and all subsequent target diagram objects are Y_j. The unrelated i indexes the source presentation X. Both reports identify the same subscript.

Adverse evidence / qualification: The two diagrams are distinct; there is no prior identification I=J that would make the printed expression correct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Y = \colim_{j \in J} Y_i
+Y = \colim_{j \in J} Y_j
````

### MC-STK-ERR-1638

`categories.tex` — 3818; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3818) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The sentence describes two separate presentations, for X and Y. The plural noun agrees with those two presentations.

Adverse evidence / qualification: No indexing category or preservation assertion changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as filtered colimit of objects
+as filtered colimits of objects
````

### MC-STK-ERR-1639

`categories.tex` — 3836; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3836) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The exact definition of F(X) at 3810 and the compatible family at 3827–3832 use F'(X_i). Match that construction in the displayed induced morphism.

Adverse evidence / qualification: The extension will agree with F' on C', as stated later at 3855, so the original can be interpreted through that identification. Use the defining notation directly rather than claiming the intended map was nonexistent.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim F(X_i)
+\colim F'(X_i)
````

### MC-STK-ERR-1640

`categories.tex` — 3862; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3862) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

C is the category in which the displayed diagram's colimit is taken, not the diagram being colimited.

Adverse evidence / qualification: The objects and structure maps already identify the ambient category; this is preposition repair only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a filtered colimit of $\mathcal{C}$
+a filtered colimit in $\mathcal{C}$
````

### MC-STK-ERR-1641

`categories.tex` — 4148; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L4148) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The pair p represents X to Y and q represents Y to Z; the constructed pair r has numerator with source X and denominator with source Z, so represents q composed with p. The later equations at 4154 and 4180–4183 use this correct order.

Adverse evidence / qualification: The sentence at 4153 also considers composition on the other side when meaningful, but that does not change the domains in the construction concluded at 4148.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$p \circ q$
+$q \circ p$
````

### MC-STK-ERR-1642

`categories.tex` — 4756; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L4756) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Hyphenate the compound adjective modifying calculus, consistently with the earlier fine-grained copyedit.

Adverse evidence / qualification: Pure typography; no multiplicative-system axiom or localization theorem changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-two sided
+two-sided
````

### MC-STK-ERR-1643

`categories.tex` — 4891; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L4891) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The displayed vertical composition has two natural transformations; the count noun should be plural.

Adverse evidence / qualification: Only the noun changes. In particular, the displayed composite t composed with t-prime must remain unchanged, as the next review entry explains.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Composition of transformation of functors
+Composition of transformations of functors
````

### MC-STK-ERR-1644

`categories.tex` — 5107; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5107) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Use the plural count noun transformations and plural agreement for the two coordinated composition operations which supply the bifunctor's object and morphism maps.

Adverse evidence / qualification: The two operations together constitute one construction, so singular notional agreement is conceivable; the minimally rephrased plural makes the displayed coordinated subject explicit without changing the bifunctor.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of transformation of functors gives rise
+of transformations of functors give rise
````

### MC-STK-ERR-1645

`categories.tex` — 5183; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5183) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Delete the comma separating a nonparenthetical subject from its predicate.

Adverse evidence / qualification: No change to the subset or subcategory requirements.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $\mathcal{C}$, is
+of $\mathcal{C}$ is
````

### MC-STK-ERR-1646

`categories.tex` — 5185; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5185) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Use the standard closed compound for subcategories of the hom-categories.

Adverse evidence / qualification: Spelling only, not an assertion that the subcategories must be full.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sub categories
+subcategories
````

### MC-STK-ERR-1647

`categories.tex` — 5188, 5189; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5188-L5189) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Both parenthetical descriptions omit the preposition relating composition to the morphisms composed.

Adverse evidence / qualification: Keep the two uses of circ and the horizontal star exactly as printed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-composition $1$-morphisms
+composition of $1$-morphisms
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-composition $2$-morphisms
+composition of $2$-morphisms
````

### MC-STK-ERR-1648

`categories.tex` — 5220; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5220) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The object class belongs to the specified 2-category mathcal C, as do the hom-categories on the next line. The two reports concern the same dropped font command.

Adverse evidence / qualification: The intended referent is evident; this is a notation repair, not a change to the smallness convention.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Ob(C)
+\Ob(\mathcal{C})
````

### MC-STK-ERR-1649

`categories.tex` — 5249; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5249) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The singular count noun denotes the already fixed target and needs its article.

Adverse evidence / qualification: The construction still forgets all 2-morphisms; no weak-functor coherence data are introduced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-out of 2-category
+out of the 2-category
````

### MC-STK-ERR-1650

`categories.tex` — 5258; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5258) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The identity coherence morphism is indexed by objects of the domain category mathcal A, matching both preceding data. These French/CJK reports identify one font-command omission.

Adverse evidence / qualification: No invertibility or coherence condition changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Ob(A)
+\Ob(\mathcal{A})
````

### MC-STK-ERR-1651

`categories.tex` — 5529; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5529) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The referenced construction is a 2-category and the immediately preceding final-object definition is bicategorical, requiring a unique invertible 2-morphism between each pair of 1-morphisms. Restore that qualifier instead of suggesting the ordinary category's stronger strict uniqueness property.

Adverse evidence / qualification: The words 'described above' identify the intended structure, so this clarifies its stated type rather than replacing the intended universal property.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-category of 2-commutative diagrams
+$2$-category of $2$-commutative diagrams
````

### MC-STK-ERR-1652

`categories.tex` — 5437; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5437) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The target quadruple's second and third entries are the structure 1-morphisms a',b', not the comparison 2-morphisms alpha',beta' carried by the incoming 1-morphism. All three physical reports identify exactly this same tuple.

Adverse evidence / qualification: The correct objects occur immediately before and in later diagrams; the compositional formula itself is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(w', \alpha', \beta', \phi')
+(w', a', b', \phi')
````

### MC-STK-ERR-1653

`categories.tex` — 5630; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5630) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Supply the nominal clause and finite verb in the omission notice.

Adverse evidence / qualification: This does not purport to add a missing mathematical proof; naturality of t already defines the required functor on morphisms.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(Check this is a functor omitted.)
+(The check that this is a functor is omitted.)
````

### MC-STK-ERR-1654

`categories.tex` — 5635, 5641; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5635-L5641) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Each quadruple is an object of the diagram 2-category, so its first component is the category mathcal W. Plain W elsewhere is an object of that category. Both producer reports cover the same two occurrences.

Adverse evidence / qualification: Restore a single mathcal command, not the doubled backslash accidentally serialized in one French prose proposal. The exact authority-bound replacement is recorded here.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(W, a, b, t)
+(\mathcal{W}, a, b, t)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(W, a, b, t)
+(\mathcal{W}, a, b, t)
````

### MC-STK-ERR-1655

`categories.tex` — 5741, 5742; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5741-L5742) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Beta has domain category X and identifies MH(X) with FL(X); alpha has domain Y and identifies GK(Y) with MI(Y). Swap the names while keeping the corresponding X,Y subscripts. The object map at 5706 independently confirms their roles. The two reports are duplicates.

Adverse evidence / qualification: The sentence uses identifications by isomorphisms, so no inverse-direction token is required; only the wrongly typed names change.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\alpha_X
+\beta_X
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\beta_Y
+\alpha_Y
````

### MC-STK-ERR-1656

`categories.tex` — 5760; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5760) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The noun phrase is full faithfulness; fully modifies faithful, not faithfulness.

Adverse evidence / qualification: The full-and-faithful hypothesis, which lifts the isomorphism, remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-fully faithfulness
+full faithfulness
````

### MC-STK-ERR-1657

`categories.tex` — 5889, 5891; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5889-L5891) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The producer's given-to-give correction is valid. Source review also shows that the displayed constructions are inverse up to natural isomorphism, not literally: the round trip replaces S by G_2(X_2), with comparison isomorphism phi_2. In the direction from the original triple to the round-trip triple its third component is phi_2^{-1}, while its first two components are identities; the required square follows from phi_2^{-1} phi_1=psi. In the other direction the composite returns psi exactly. Thus quasi-inverse is the precise term in both sentences.

Adverse evidence / qualification: 'Mutually inverse' is sometimes used informally up to natural isomorphism in equivalence proofs; this is a clarification of the intended equivalence, not a false-theorem claim. The second lexical correction was found during this review, not attributed to the producer.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-constructions given mutually inverse functors
+constructions give mutually quasi-inverse functors
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-they are mutually inverse
+they are mutually quasi-inverse
````

### MC-STK-ERR-1658

`categories.tex` — 5934; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5934) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The unlabelled command draws the same edge as the labelled diagonal functor. Remove only that redundant command; both reports concern the same diagram edge.

Adverse evidence / qualification: The duplicate may merely overprint rather than visibly separate, so this is redundant typesetting, not a second mathematical map or a changed square.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{C} \ar[r]^-{\Delta_{\mathcal{C}/\mathcal{D}}} \ar[r] &
+\mathcal{C} \ar[r]^-{\Delta_{\mathcal{C}/\mathcal{D}}} &
````

### MC-STK-ERR-1659

`categories.tex` — 5967; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L5967) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Hyphenate the compound attributive modifier, consistently with the other accepted compound copyedits.

Adverse evidence / qualification: No mathematical claim or generality changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$2$-category theoretic
+$2$-category-theoretic
````

### MC-STK-ERR-1660

`categories.tex` — 6033; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6033) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The pronoun referring to the axioms is they; the printed article leaves the clause without its subject.

Adverse evidence / qualification: The following sentence repeats the correct assertion and confirms the referent.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-that the hold
+that they hold
````

### MC-STK-ERR-1661

`categories.tex` — 6061; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6061) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The intended frequency adverb agrees with the parallel 'We sometimes say' in the next item.

Adverse evidence / qualification: The object-lift terminology is unaffected.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-also sometime say
+also sometimes say
````

### MC-STK-ERR-1662

`categories.tex` — 6144; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6144) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Restore the chapter's fibre spelling within a paragraph comparing two constructions of the same named notion.

Adverse evidence / qualification: Fiber itself is correct American spelling; this is house-style consistency, not a terminological or mathematical error.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$2$-fiber product
+$2$-fibre product
````

### MC-STK-ERR-1663

`categories.tex` — 6163; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6163) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Terminate the lemma's sentence with a period at the end of its displayed identity.

Adverse evidence / qualification: The mathematical identity is unchanged; the period is sentence punctuation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{X}_U \times_{\mathcal{S}_U} \mathcal{Y}_U
+\mathcal{X}_U \times_{\mathcal{S}_U} \mathcal{Y}_U.
````

### MC-STK-ERR-1664

`categories.tex` — 6548; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6548) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Add the missing period ending the definition's final prose sentence.

Adverse evidence / qualification: The optional denote-by proposal in the same sentence is separately recorded and not required by this punctuation correction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(\mathcal{S}, p)$ and $(\mathcal{S}', p')$
+$(\mathcal{S}, p)$ and $(\mathcal{S}', p')$.
````

### MC-STK-ERR-1665

`categories.tex` — 6615, 6618, 6619, 6628; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6615-L6628) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The fibre-product equality is in C/U and uses p', whereas strong cartesianness for p lifts underlying C-maps. Psi-prime lands in x', whose slice image is V'/U, so its underlying codomain is V'. The forgetful functor C/U to C is faithful: with fixed slice source/target, equal underlying maps give equal slice morphisms. In the final lift the slice structure on x' is forced by its arrow to x, so it agrees with the source of g. Four reports partially overlap and are grouped into one coherent typing repair.

Adverse evidence / qualification: Identification of a slice morphism with its underlying arrow is common shorthand, but the V/V-prime errors are genuine and the mix of p and p' obscures the precise lifting proof. The revised text retains all hypotheses and constructs no new morphism beyond the original argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g \circ h = p(\psi)$
+$g \circ h = p'(\psi)$
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-and $p(\psi') = h$. OK, and now $p'(\psi') : W/U \to V/U$
+and $p(\psi')$ equal to the underlying map of $h$. Then
+$p'(\psi') : W/U \to V'/U$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a morphism whose corresponding map $W \to V$ is $h$, hence
+is a morphism whose underlying map $W \to V'$ is that of $h$, hence
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-with $p(\varphi) = g$. By the same argument as above it follows
+with $p(\varphi)$ equal to the underlying map of $g$.
+By the same argument as above it follows
````

### MC-STK-ERR-1666

`categories.tex` — 6837, 6854, 6861; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6837-L6861) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

All three functor source/target references denote the same relative inertia category defined at 6786, whose symbol is calligraphic I. Both reports list the same three missing mathcal commands.

Adverse evidence / qualification: Plain I is not a distinct construction here. Keep the separate already-admitted absolute-inertia correction at 7427 distinct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-I_{\mathcal{S}/\mathcal{S}'}
+\mathcal{I}_{\mathcal{S}/\mathcal{S}'}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-I_{\mathcal{S}/\mathcal{S}'}
+\mathcal{I}_{\mathcal{S}/\mathcal{S}'}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-I_{\mathcal{S}/\mathcal{S}'}
+\mathcal{I}_{\mathcal{S}/\mathcal{S}'}
````

### MC-STK-ERR-1667

`categories.tex` — 7050; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7050) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Use the single destination preposition for the pseudofunctor. Both producers report the same split word.

Adverse evidence / qualification: No source/codomain or coherence datum changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in to
+into
````

### MC-STK-ERR-1668

`categories.tex` — 7188; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7188) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The label describes the lifted diagram/category as lying above the base diagram. It is deliberate reader-facing prose positioned by an invisible arrow; typeset it as text. The French proposal preserves this meaning while fixing the bare math letters.

Adverse evidence / qualification: The Japanese proposal to delete above assumes without evidence that it is a leftover layout placeholder. Retain the word and the invisible positioning arrow rather than removing meaningful annotation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-^{above}
+^{\text{above}}
````

### MC-STK-ERR-1669

`categories.tex` — 7336; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7336) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The following line already supplies 'to morphisms', so 'from morphisms' corrects both the singular noun and the mixed between/to construction in one local edit.

Adverse evidence / qualification: Changing the later to into and would also work, but requires a second locus and gives no mathematical benefit.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-between morphism
+from morphisms
````

### MC-STK-ERR-1670

`categories.tex` — 7352; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7352) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The first for all has no bound variable and duplicates the complete for-all-U clause later in the sentence. Both producers identify the same stray words.

Adverse evidence / qualification: The actual universal quantifier at the end of the clause remains untouched.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Finally suppose for all $G_U$
+Finally suppose $G_U$
````

### MC-STK-ERR-1671

`categories.tex` — 7516; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7516) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Supply the article before the singular count noun.

Adverse evidence / qualification: The explicit object/morphism construction and equivalence assertion are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-As functor
+As a functor
````

### MC-STK-ERR-1672

`categories.tex` — 7617; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7617) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Beta was defined at 7609 with type b^{-1}b to id. The displayed arrow starts at d(x), whose first component is x, and ends at c(b(x)), whose first component is b^{-1}(b(x)). Its first component must therefore be beta_x^{-1}. The target comparison is alpha_x composed with F(beta_x), so the compatibility square reads alpha_x F(beta_x) F(beta_x^{-1})=alpha_x, exactly as required by the fibre-product morphism definition at 7508.

Adverse evidence / qualification: Reversing the definition of beta would require changing the already correctly typed comparison map alpha_x F(beta_x). Inverting only the component at 7617 is the smaller consistent repair. This is not claimed as a producer-supplied correction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(\beta_x, \alpha_x)
+(\beta_x^{-1}, \alpha_x)
````

### MC-STK-ERR-1673

`categories.tex` — 7789, 7936; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7789-L7936) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The displayed pair is itself a morphism of the fibre category, with objects as endpoints. Deleting the duplicated 'between morphisms' phrase in both parallel constructions gives the intended sentence. Both producers report the same two loci.

Adverse evidence / qualification: The pullback construction and coherence identifications are not altered.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-between morphisms in
+in
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-between morphisms in
+in
````

### MC-STK-ERR-1674

`categories.tex` — 7968; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7968) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Use the frequency adverb for a recurring identification convention.

Adverse evidence / qualification: The identification of a set with its discrete category remains explicitly permitted.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we sometime confuse
+we sometimes confuse
````

### MC-STK-ERR-1675

`categories.tex` — 8053; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L8053) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The perfect construction requires the participle seen.

Adverse evidence / qualification: No assertion about the fibre categories changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-have already see
+have already seen
````

### MC-STK-ERR-1676

`categories.tex` — 8039; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L8039) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Here F is set-valued, so direct membership in F(U) is the explicit notation for its elements and agrees with the fibre's underlying set at 8053.

Adverse evidence / qualification: The source explicitly allows identifying sets with discrete categories at 7966–7969, so Ob(F(U)) can be interpreted through that convention. Classify this as removing unnecessary notation, not as an undefined construction or a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x \in \Ob(F(U))
+x \in F(U)
````

### MC-STK-ERR-1677

`categories.tex` — 7988, 8189; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L7988-L8189) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

These definitions retain 2-morphisms and declare sub-2-categories, unlike the strict ordinary functor construction in the preceding review. Name the ambient 2-category consistently in both parallel definitions.

Adverse evidence / qualification: The referenced definition already supplies the intended 2-category, so this repairs the qualifier rather than changing either construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of the category of categories
+of the $2$-category of categories
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of the category of categories
+of the $2$-category of categories
````

### MC-STK-ERR-1678

`categories.tex` — 8132; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L8132) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Delete the stray auxiliary is before would. Both reports identify the same malformed clause.

Adverse evidence / qualification: The intended invariance-under-equivalence requirement remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-this is would not
+this would not
````

### MC-STK-ERR-1679

`categories.tex` — 8449; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L8449) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The lemma asserts uniqueness of the pair (X,j). Name both components in the second such pair while preserving the explicit type of j'.

Adverse evidence / qualification: The original typed functor implicitly identifies X', so this is clarification of the pair notation rather than a missing uniqueness argument.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-For the second, suppose that $j' : \mathcal{S} \to \mathcal{C}/X'$ is
+For the second, suppose that $(X', j')$, with
+$j' : \mathcal{S} \to \mathcal{C}/X'$, is
````

### MC-STK-ERR-1680

`categories.tex` — 8949; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L8949) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Delete the syntactically stray article. The two producer reports are duplicates.

Adverse evidence / qualification: The citation and coherence assertion remain intact.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as a above
+as above
````

### MC-STK-ERR-1681

`categories.tex` — 8963; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L8963) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The referenced associativity coherence diagram connects the five bracketings of four objects around a pentagon, not the star called a pentagram.

Adverse evidence / qualification: The diagram and its actual commutativity condition are already correct; only the descriptive name changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-pentagram diagram
+pentagon diagram
````

### MC-STK-ERR-1682

`categories.tex` — 9024; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9024) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Restore the missing h in isomorphism. Both reports concern the same spelling error.

Adverse evidence / qualification: The map's invertibility is already part of the unit data.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-isomorpism
+isomorphism
````

### MC-STK-ERR-1683

`categories.tex` — 9043; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9043) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

After X=Z tensor 1 and Y=1 tensor W, the right side must be r_{Z tensor 1} tensor id_1 tensor id_W, the expansion of r_X tensor id_Y. The printed last id_Y adds an extra unit factor. Both subsequent expressions at 9046–9047 end in id_W and independently confirm the repair.

Adverse evidence / qualification: Units are not assumed strictly equal to omitted tensor factors here; this proof is establishing their compatibility, so silently removing the extra unit would be circular. Two reports describe one operation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{id}_Y
+\text{id}_W
````

### MC-STK-ERR-1684

`categories.tex` — 9264; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9264) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

Supply the article before the singular predicate noun, as both reports propose.

Adverse evidence / qualification: No tensor product, ring map or monoidal structure changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is functor of monoidal
+is a functor of monoidal
````

### MC-STK-ERR-1685

`categories.tex` — 9401; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9401) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The preceding data specify an adjunction and its unit; use the matching name for the structure supplying the counit.

Adverse evidence / qualification: The informal phrase counit of an adjoint is recoverable when the other functor is understood. This is terminology consistency, not a changed counit formula.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-counit of the adjoint
+counit of the adjunction
````

### MC-STK-ERR-1686

`categories.tex` — 9585; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9585) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The coordinated subject eta-prime and epsilon-prime takes plural agreement.

Adverse evidence / qualification: The maps jointly constitute duality data, but the explicit sentence subject consists of two maps. The duality assertion is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-makes $X$
+make $X$
````

### MC-STK-ERR-1687

`categories.tex` — 9661; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L9661) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r52/candidate.manifest.json)

The commutativity constraint swaps X and hom(X,Y), the final two factors of the three-factor tensor product. Calling them two products names the wrong objects.

Adverse evidence / qualification: The following evaluation maps already give the correct construction; the repair is the noun describing the swap.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-last two tensor products
+last two tensor factors
````
