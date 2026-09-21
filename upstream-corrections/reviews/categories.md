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
