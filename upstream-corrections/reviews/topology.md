# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## topology

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/topology.patch)

### MC-STK-ERR-0033

`topology.tex` — 1235; undefined vertex set error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1235) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: diameter endpoints in E → diameter endpoints in V

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j, j' \in E$ with maximal distance and then $j$ works (choose a leaf!).
+$j, j' \in V$ with maximal distance and then $j$ works (choose a leaf!).
````

### MC-STK-ERR-0034

`topology.tex` — 1276-1277; ill typed order definition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1276-L1277) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: order on undefined alpha-indexed sets → order directly on Z,Z-prime in A

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-The set $A$ is partially ordered by inclusion: $\alpha \leq \alpha'
-\Leftrightarrow Z_{\alpha} \subset Z_{\alpha'}$.
+The set $A$ is partially ordered by inclusion: $Z \leq Z'
+\Leftrightarrow Z \subset Z'$ for $Z, Z' \in A$.
````

### MC-STK-ERR-0035

`topology.tex` — 2380; indexing category object error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2380) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: J subset undefined I → J subset Ob(mathcal I)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some subset $J \subset I$ and opens $U_j \subset X_j$.
+for some subset $J \subset \Ob(\mathcal{I})$ and opens $U_j \subset X_j$.
````

### MC-STK-ERR-0036

`topology.tex` — 1882-1884; set parenthesization error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1882-L1884) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: two ungrouped X minus U union V spans → two complements X minus (U union V)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$C \subset V$. Then $X \setminus U \cup V$ is closed in $X$
+$C \subset V$. Then $X \setminus (U \cup V)$ is closed in $X$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-It follows that $(X \setminus U \cup V) \cap Z_\alpha = \emptyset$
+It follows that $(X \setminus (U \cup V)) \cap Z_\alpha = \emptyset$
````

### MC-STK-ERR-0037

`topology.tex` — 1946-1947; set parenthesization error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1947) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: X minus U_i1 union U_i2 → X minus (U_i1 union U_i2)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(X \setminus U_{i_1} \cup U_{i_2}) \supset \ldots$ is a strictly
+(X \setminus (U_{i_1} \cup U_{i_2})) \supset \ldots$ is a strictly
````

### MC-STK-ERR-0038

`topology.tex` — 3124; unmatched delimiter error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3124) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: set-builder ending with extra parenthesis → balanced set-builder

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$U_K := \{J\subset I \mid J \in Z, \ K\subset J \})$.
+$U_K := \{J\subset I \mid J \in Z, \ K\subset J \}$.
````

### MC-STK-ERR-0039

`topology.tex` — 2649; omitted union index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2649) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: unindexed big union of E intersect V_j → union j=1 to m of (E intersect V_j)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then $E = \bigcup E \cap V_j$ is a finite union of
+Then $E = \bigcup_{j = 1}^m (E \cap V_j)$ is a finite union of
````

### MC-STK-ERR-0040

`topology.tex` — 3775-3776; domain codomain type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3776) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: chain called closed subsets of X → chain called closed subsets of Y

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of irreducible closed subsets of $X$. Let $\xi_e \in X$ be a point
+of irreducible closed subsets of $Y$. Let $\xi_e \in X$ be a point
````

### MC-STK-ERR-0041

`topology.tex` — 3877-3888; specialization direction and sign error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3880-L3888) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: two reversed delta differences and xi_i specializes to xi_i+1 → two corrected delta differences and xi_i+1 specializes to xi_i

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\text{codim}(Y, Y') \leq \delta(\xi) - \delta(\xi') < \infty$.
+$\text{codim}(Y, Y') \leq \delta(\xi') - \delta(\xi) < \infty$.
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-$\xi_i \leadsto \xi_{i + 1}$ is an immediate specialization.
-Hence we see that $e = \delta(\xi) - \delta(\xi')$ as desired.
+$\xi_{i + 1} \leadsto \xi_i$ is an immediate specialization.
+Hence we see that $e = \delta(\xi') - \delta(\xi)$ as desired.
````

### MC-STK-ERR-0042

`topology.tex` — 3910-3911; topological property word error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3911) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: not necessarily closed → not necessarily open

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(not necessarily closed). We claim that $\delta - \delta'$ is
+(not necessarily open). We claim that $\delta - \delta'$ is
````

### MC-STK-ERR-0043

`topology.tex` — 4103-4109; proof circularity error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4106) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: T is nowhere dense before proof → T has empty interior

````diff
--- original
+++ replacement
@@ -1 +1 @@
-say $T = T_1 \cup \ldots \cup T_n$, and $T$ is nowhere dense in $X$.
+say $T = T_1 \cup \ldots \cup T_n$, and $T$ has empty interior in $X$.
````

### MC-STK-ERR-0044

`topology.tex` — 4576-4590; projection argument error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4580-L4581) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: closures of p(X) and q(Y) → closures of p(Z) and q(Z)

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-point of the closure of $p(X)$ and let $y \in Y$ be the generic
-point of the closure of $q(Y)$. If $(x, y) \not \in Z$, then
+point of the closure of $p(Z)$ and let $y \in Y$ be the generic
+point of the closure of $q(Z)$. If $(x, y) \not \in Z$, then
````

### MC-STK-ERR-0045

`topology.tex` — 4684-4693; premature undefined codomain.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4686) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: f:X to undefined Y → f:X to product_U W

````diff
--- original
+++ replacement
@@ -1 +1 @@
-By construction the map $f : X \to Y$ is spectral. By
+By construction the map $f : X \to \prod\nolimits_U W$ is spectral. By
````

### MC-STK-ERR-0046

`topology.tex` — 4791-4803; primed inverse limit error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4801) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: Z-prime = limit Z_i → Z-prime = limit Z-prime_i

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus $Z' = \lim Z_i$ is quasi-compact by
+Thus $Z' = \lim Z'_i$ is quasi-compact by
````

### MC-STK-ERR-0047

`topology.tex` — 5058-5065; topology name error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5061) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: spectral topology in compact-Hausdorff argument → constructible topology

````diff
--- original
+++ replacement
@@ -1 +1 @@
-with empty intersection. Using that the spectral topology on $Z$
+with empty intersection. Using that the constructible topology on $Z$
````

### MC-STK-ERR-0048

`topology.tex` — 5070-5088; inverse limit parenthesization error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5086) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: limit U_i minus E → limit (U_i minus E)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$W \setminus E = \lim U_i \setminus E$ by the universal property of limits.
+$W \setminus E = \lim (U_i \setminus E)$ by the universal property of limits.
````

### MC-STK-ERR-0049

`topology.tex` — 5163-5167; codomain object error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5167) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: open subspace of X → open subspace of X-star

````diff
--- original
+++ replacement
@@ -1 +1 @@
-that $X \to X^*$ identifies $X$ with an open subspace of $X$.
+that $X \to X^*$ identifies $X$ with an open subspace of $X^*$.
````

### MC-STK-ERR-0050

`topology.tex` — 5362-5369; set parenthesization error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5364) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: X minus U intersect inverse-image V → X minus (U intersect inverse-image V)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$p \in U$, $f(p) \in V$ and set $E = X \setminus U \cap f^{-1}(V)$.
+$p \in U$, $f(p) \in V$ and set $E = X \setminus (U \cap f^{-1}(V))$.
````

### MC-STK-ERR-0051

`topology.tex` — 5410-5442; minimal cover object error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5436-L5442) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: uniqueness run on ambient X-prime and shadowed E → uniqueness run on minimal cover E with proper subset T

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we can find a continuous map $g : X' \to X''$ over $X$.
+we can find a continuous map $g : E \to X''$ over $X$.
````

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
-Hence $g(X') \subset X''$ is a closed subset surjecting onto $X$
-and we conclude $g(X') = X''$ by minimality of $X''$.
-On the other hand, if $E \subset X'$ is a proper closed subset,
-then $g(E) \not = X''$ as $E$ does not map onto $X$ by minimality
-of $X'$. By Lemma \ref{lemma-isomorphism} we see that $g$ is an isomorphism.
+Hence $g(E) \subset X''$ is a closed subset surjecting onto $X$
+and we conclude $g(E) = X''$ by minimality of $X''$.
+On the other hand, if $T \subset E$ is a proper closed subset,
+then $g(T) \not = X''$ as $T$ does not map onto $X$ by minimality
+of $E$. By Lemma \ref{lemma-isomorphism} we see that $g$ is an isomorphism.
````

### MC-STK-ERR-0052

`topology.tex` — 5480-5490; unfinished scaffold error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5484) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: literal item add more here → placeholder item removed

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
-\item add more here.
````

### MC-STK-ERR-0053

`topology.tex` — 5507-5522; reversed definition error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5512-L5513) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: unnamed reversed refinement definition → named standard refinement definition

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-Given two partitions of $X$ we say one {\it refines} the other if
-the parts of one are unions of parts of the other.
+Given two partitions $\mathcal{P}$ and $\mathcal{Q}$ of $X$, we say
+$\mathcal{P}$ {\it refines} $\mathcal{Q}$ if every part of $\mathcal{Q}$
+is a union of parts of $\mathcal{P}$.
````

### MC-STK-ERR-0054

`topology.tex` — 5820-5824; coset conjugation orientation error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5823) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: right cosets with g_i H g_i^-1 → right cosets with g_i^-1 H g_i

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$N = \bigcap_{i = 1, \ldots, n} g_iHg_i^{-1}$ is
+$N = \bigcap_{i = 1, \ldots, n} g_i^{-1}Hg_i$ is
````

### MC-STK-ERR-0055

`topology.tex` — 5865-5873; category codomain error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5868) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r3/candidate.manifest.json)

Reviewed legacy summary: diagram into Top → diagram into TopGroup

````diff
--- original
+++ replacement
@@ -1 +1 @@
-that $\mathcal{I} \to \textit{Top}$, $i \mapsto G_i$ is a functor
+that $\mathcal{I} \to \textit{TopGroup}$, $i \mapsto G_i$ is a functor
````

### MC-STK-ERR-0063

`topology.tex` — topology.tex:345-349; proof-construction indexing defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L345-L349) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The basis member is chosen after and for each point x, so it depends on x rather than only on the possibly repeated cover index i_x. Indexing the refinement by U binds every chosen B_x and proves the stated refinement.

Adverse evidence / qualification: With the one-member cover U_0=R and a basis of bounded rational intervals, every i_x is 0 but no single basis interval B_0 covers R; the printed J={i_x} construction therefore fails.

````diff
--- original
+++ replacement
@@ -1,5 +1,4 @@
-If $ x \in U = \bigcup_{i\in I} U_i $, there is an $ i_x \in I $ such that
-$ x \in U_{i_x} $. Thus we have a $ B_{i_x} \in \mathcal{B}$
-verifying $ x \in B_{i_x} \subset U_{i_x}$. Set
-$J = \{i_x | x \in U\}$ and for $j = i_x \in J$ set $V_j = B_{i_x}$.
+For every $x \in U = \bigcup_{i \in I} U_i$, choose $i_x \in I$ and
+$B_x \in \mathcal{B}$ such that $x \in B_x \subset U_{i_x}$.
+Set $J = U$ and, for $j = x \in J$, set $V_j = B_x$.
 This gives the desired open covering of $U$ by $\{V_j\}_{j \in J}$.
````

### MC-STK-ERR-0064

`topology.tex` — topology.tex:514-515; source/codomain type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L514-L515) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

For f:X to Y, inverse image accepts subsets of Y and returns subsets of X. The complement law is f^{-1}(Y\E)=X\f^{-1}(E) for E subset Y.

Adverse evidence / qualification: The printed identity puts X inside f^{-1}, puts Y on the result side, and quantifies E as a subset of X, reversing all three required types.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Finally, (2) and (3) equivalence follows from $f^{-1}(X\setminus E) = Y
-\setminus f^{-1}(E)$ for all subsets $E \subset X$.
+Finally, (2) and (3) equivalence follows from $f^{-1}(Y \setminus E) = X
+\setminus f^{-1}(E)$ for all subsets $E \subset Y$.
````

### MC-STK-ERR-0065

`topology.tex` — topology.tex:1278-1279; order-theoretic proof terminology defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1279) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

DCC supplies a minimal member under inclusion, and the contradiction proof uses only the absence of a strictly smaller member of A.

Adverse evidence / qualification: A finite DCC poset can have incomparable minimal elements and no least element, so 'smallest' is not implied.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-smallest element of $A$
+minimal element of $A$
````

### MC-STK-ERR-0066

`topology.tex` — topology.tex:1297; missing mathematical union operator.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1297) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The named irreducible components are Z,Z_1,...,Z_n and the next line takes the complement of the union of Z_1,...,Z_n; the displayed finite union therefore requires a final union operator.

Adverse evidence / qualification: The printed ellipsis followed by Z_n is juxtaposition, not the finite set union used by the proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Z \cup Z_1 \cup \ldots Z_n
+Z \cup Z_1 \cup \ldots \cup Z_n
````

### MC-STK-ERR-0067

`topology.tex` — topology.tex:1345-1348; missing mathematical union operator.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1347) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Distributivity expands G_m intersected with the finite union X_1 union ... union X_n as the finite union of every G_m intersect X_i.

Adverse evidence / qualification: Without the final union operator the right side concatenates the ellipsis and last term and does not state the equality used for stabilization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(G_m \cap X_1) \cup \ldots (G_m \cap X_n)
+(G_m \cap X_1) \cup \ldots \cup (G_m \cap X_n)
````

### MC-STK-ERR-0068

`topology.tex` — topology.tex:1847-1853; unbound proof index.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1851-L1852) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The earlier observation that finite intersections of the Z_alpha are again family members proves existence of an index alpha representing Z_alpha' intersect Z_alpha'', but that index must be explicitly chosen before use.

Adverse evidence / qualification: The printed alpha is new and free; only alpha' and alpha'' have been bound at that point.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-Then $Z_\alpha = Z_{\alpha'} \cap Z_{\alpha''}$ is contained
+Choose $\alpha \in A$ such that
+$Z_\alpha = Z_{\alpha'} \cap Z_{\alpha''}$. Then $Z_\alpha$ is contained
 in $U \cup V$ and disjoint from $U \cap V$.
````

### MC-STK-ERR-0069

`topology.tex` — topology.tex:2165-2168; missing mathematical intersection operator.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2167) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The containment concerns the full (p+1)-fold intersection, as required by both the preceding construction and the lemma statement.

Adverse evidence / qualification: The printed V_{j_1} followed by an ellipsis lacks the intersection operator and therefore does not denote the required iterated intersection.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-V_{j_1} \ldots \cap V_{j_p}
+V_{j_1} \cap \ldots \cap V_{j_p}
````

### MC-STK-ERR-0070

`topology.tex` — topology.tex:2174-2176; proof termination overclaim.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2174-L2176) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The replacement eliminates the selected bad tuple without creating a new one, so N strictly decreases; it can eliminate additional tuples simultaneously, hence termination is after at most the original N repetitions.

Adverse evidence / qualification: A finite discrete example with two bad tuples sharing the refined first entry makes N fall from 2 to 0 in one replacement, disproving 'decreased by one'.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-A simple check shows that $N$ has decreased by one under this replacement.
-Repeating this procedure $N$ times we arrive at the situation where
-$N = 0$.
+A simple check shows that $N$ has decreased by at least one under this
+replacement. Repeating this procedure at most the original $N$ times,
+we arrive at the situation where $N = 0$.
````

### MC-STK-ERR-0071

`topology.tex` — topology.tex:2487-2523; ill-typed inverse-limit compatibility locus.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2491-L2523) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

For every arrow j to k, including endomorphisms, the compatibility locus is the inverse image of the graph under p_{j,k}(x_i)=(x_j,x_k). This is a closed subset and uniformly gives the correct fixed-point condition when j=k.

Adverse evidence / qualification: When j=k, Gamma_phi has two X_j factors while the ambient product has only one X_j coordinate, so Gamma_phi times the remaining factors is not a subset of the ambient product. Both copied occurrences require repair.

````diff
--- original
+++ replacement
@@ -1,6 +1,6 @@
-It is clear that $\lim X_i$ is the intersection of the
-closed subsets
+Let $p_{j,k} : \prod X_i \to X_j \times X_k$ be the continuous map
+$(x_i) \mapsto (x_j, x_k)$. It is clear that $\lim X_i$ is the
+intersection of the closed subsets
 $$
-\Gamma_\varphi \times \prod\nolimits_{l \not = j, k} X_l
-\subset \prod X_i
+p_{j,k}^{-1}(\Gamma_\varphi) \subset \prod X_i.
 $$
````

````diff
--- original
+++ replacement
@@ -1,6 +1,8 @@
 $$
-Z_\varphi = \Gamma_\varphi \times \prod\nolimits_{l \not = j, k} X_l
+Z_\varphi = p_{j,k}^{-1}(\Gamma_\varphi)
 $$
-inside the quasi-compact space $\prod X_i$ where $\varphi : j \to k$
-is a morphism of $\mathcal{I}$ and $\Gamma_\varphi \subset X_j \times X_k$
-is the graph of the corresponding morphism $X_j \to X_k$.
+inside the quasi-compact space $\prod X_i$, where
+$p_{j,k} : \prod X_i \to X_j \times X_k$ is the map
+$(x_i) \mapsto (x_j, x_k)$, $\varphi : j \to k$ is a morphism of
+$\mathcal{I}$, and $\Gamma_\varphi \subset X_j \times X_k$ is the graph
+of the corresponding morphism $X_j \to X_k$.
````

### MC-STK-ERR-0072

`topology.tex` — topology.tex:2916-2919; order-theoretic proof terminology defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2918) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Noetherian DCC supplies a minimal closed member of the counterexample family, and the proof uses only that every proper closed subset is outside that family.

Adverse evidence / qualification: DCC does not imply that a nonempty family has a least member, so 'smallest' overstates the available order-theoretic conclusion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then it has a smallest element $Y$
+then it has a minimal element $Y$
````

### MC-STK-ERR-0073

`topology.tex` — topology.tex:3594-3611; directedness proof gap.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3605-L3607) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Finite unions of point closures are closed, contained in T, directed by inclusion through union of finite index sets, and have union T. This proves the stated directed-union characterization.

Adverse evidence / qualification: In a two-point discrete space the family of the two point closures has no member containing their union, so the family exhibited by the printed proof need not be directed.

````diff
--- original
+++ replacement
@@ -1,3 +1,9 @@
-Suppose that $T$ is stable under specialization, then for all $y\in T$ we have
-$\overline{\{y\}} \subset T$. Thus $T = \bigcup_{y\in T} \overline{\{y\}}$
-which is an union of closed subsets of $X$. Reciprocally, suppose that $T =
+Suppose that $T$ is stable under specialization. For every finite subset
+$S \subset T$ set
+$$
+F_S = \bigcup_{y \in S} \overline{\{y\}}.
+$$
+Then $F_S$ is closed and contained in $T$, the family $(F_S)$ is directed
+by inclusion since $F_S \cup F_{S'} = F_{S \cup S'}$, and
+$T = \bigcup_{S \subset T\text{ finite}} F_S$.
+Reciprocally, suppose that $T =
````

### MC-STK-ERR-0074

`topology.tex` — topology.tex:4499-4501; unsupported distinctness implication.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4500) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof produces a common generalization but never proves that it differs from x or y; deleting 'third' makes the statement exactly match the proof.

Adverse evidence / qualification: For x=y in a one-point spectral space, and for comparable points in the Sierpinski space, a common generalization can equal one of the named points while disjoint neighbourhoods do not exist.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a third point specializing to both $x$ and $y$
+a point specializing to both $x$ and $y$
````

### MC-STK-ERR-0075

`topology.tex` — topology.tex:4530-4538; unfinished editorial placeholder.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4536-L4537) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof establishes equivalence only through item (8); deleting the non-proposition placeholder leaves the complete proved list and closes item (8) grammatically.

Adverse evidence / qualification: The literal text 'add more here.' is neither a mathematical condition nor addressed by the proof.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-\item the constructible topology equals the given topology on $X$, and
-\item add more here.
+\item the constructible topology equals the given topology on $X$.
````

### MC-STK-ERR-0076

`topology.tex` — topology.tex:5813-5816; missing universal quantifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5814) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

For every g in U_t and w in W, the chosen finite subcover gives gw in W and hence f(gw)=t. This two-variable statement is exactly what proves the later intersection is contained in H.

Adverse evidence / qualification: The printed sentence quantifies w only, leaving g free and failing to state the fact used in the next inclusion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such that $f(gw) = t$ for all $w \in W$.
+such that $f(gw) = t$ for all $g \in U_t$ and $w \in W$.
````

### MC-STK-ERR-1689

`topology.tex` — 143; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L143) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Restore the finite clause introducing the equivalent neighbourhood conditions.

Adverse evidence / qualification: The preceding product condition is correct; this is sentence repair.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-In other words, with
+In other words, we have
````

### MC-STK-ERR-1690

`topology.tex` — 204; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L204) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Supply the article before the singular count noun.

Adverse evidence / qualification: All hypotheses and equivalences remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be continuous map
+be a continuous map
````

### MC-STK-ERR-1691

`topology.tex` — 249; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L249) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Repair the independently repeated missing article.

Adverse evidence / qualification: This is a separate source occurrence, not a second mathematical result.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be continuous map
+be a continuous map
````

### MC-STK-ERR-1692

`topology.tex` — 555; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L555) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Supply the article before the modified singular noun.

Adverse evidence / qualification: No map property is added or removed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be surjective, open, continuous map
+be a surjective, open, continuous map
````

### MC-STK-ERR-1693

`topology.tex` — 585; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L585) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Supply the article at the parallel closed-map statement.

Adverse evidence / qualification: The hypotheses and conclusion are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be surjective, closed, continuous map
+be a surjective, closed, continuous map
````

### MC-STK-ERR-1694

`topology.tex` — 646; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L646) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

The construction Let A requires be.

Adverse evidence / qualification: The proof's separate inverse-image problem is recorded next.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A \subset f(E)$ an open
+$A \subset f(E)$ be an open
````

### MC-STK-ERR-1695

`topology.tex` — 645; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L645) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

An unrestricted f-preimage of A can include points outside E. Explicit reduction to E to f(E) makes all later preimages clopen in the connected domain and all existing image equalities correctly typed.

Adverse evidence / qualification: The intended theorem is true; a reader might tacitly restrict f. One reduction is smaller than editing all inverse-image expressions separately.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
 \begin{proof}
+Replacing $f$ by its continuous restriction $E \to f(E)$,
+we may assume $X = E$ and $Y = f(E)$.
````

### MC-STK-ERR-1696

`topology.tex` — 741; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L741) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Separate the connectedness premise from the resulting alternative.

Adverse evidence / qualification: Both mathematical facts were already correctly stated.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is connected we conclude
+is connected, and we conclude
````

### MC-STK-ERR-1697

`topology.tex` — 832; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L832) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Give the introduced system a grammatical defining clause without asserting uniqueness.

Adverse evidence / qualification: Merely adding us would leave 'write N the fundamental system' awkward.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For all $x\in X$ let write $\mathcal{N}(x)$ the fundamental system of connected
+For each $x \in X$, let $\mathcal{N}(x)$ be a fundamental system of connected
````

### MC-STK-ERR-1698

`topology.tex` — 845; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L845) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use the nonpersonal antecedent and plural noun.

Adverse evidence / qualification: The argument for openness is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-each of his point
+each of its points
````

### MC-STK-ERR-1699

`topology.tex` — 1131, 1132; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1131-L1132) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

The nonempty open intersection meets the dense set in (c). Saying y lies in it makes both intersections with the fibre nonempty.

Adverse evidence / qualification: The original intention is recoverable; no separately defined correspondence or new irreducibility result is needed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there is a point $y$ which
+there is a point $y$ in this intersection
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-corresponds to a point of this intersection such that the fibre
+such that the fibre
````

### MC-STK-ERR-1700

`topology.tex` — 1199; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1199) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

The subject is the singular collection of U-prime.

Adverse evidence / qualification: The topology construction is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$U'$ form a topology
+$U'$ forms a topology
````

### MC-STK-ERR-1701

`topology.tex` — 1225; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1225) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Explicitly bind j and avoid an article directly before the inequality.

Adverse evidence / qualification: The bounds already identify the intended variable.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there is an
+there is an index $j$ with
````

### MC-STK-ERR-1702

`topology.tex` — 1245; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1245) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Bind X before referring to its closed subsets.

Adverse evidence / qualification: The standard intended descending-chain definition is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A topological space is called
+A topological space $X$ is called
````

### MC-STK-ERR-1703

`topology.tex` — 1336, 1341; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1336-L1341) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Supply be after Let in the first construction and is for the second sequence subject.

Adverse evidence / qualification: The decreasing families and stabilization argument are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathbf{N}}$ a decreasing sequence
+\mathbf{N}}$ be a decreasing chain
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathbf{N}}$ a decreasing
+\mathbf{N}}$ is a decreasing
````

### MC-STK-ERR-1704

`topology.tex` — 1580; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1580) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Remove the malformed imperative auxiliary.

Adverse evidence / qualification: The catenarity assumption remains identical.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let suppose
+Suppose
````

### MC-STK-ERR-1705

`topology.tex` — 1600, 1601; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1600-L1601) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use a transitive verb in the first clause and an adjectival phrase modifying length in the second.

Adverse evidence / qualification: Blindly deleting to twice would leave the second sentence ungrammatical; the two occurrences need different repairs.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-equals to
+equals
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the same length equals to the
+the same length, equal to the
````

### MC-STK-ERR-1706

`topology.tex` — 1607; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1607) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use the logical-direction term and remove the misplaced colon.

Adverse evidence / qualification: Reciprocal can be deciphered as a French-influenced term here; the proof is not claiming a numerical reciprocal.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For the reciprocal, we show by induction that : if
+For the converse, we show by induction that if
````

### MC-STK-ERR-1707

`topology.tex` — 1682; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1682) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Repair plural agreement and identify U_i directly as the open neighbourhoods.

Adverse evidence / qualification: Opens is itself valid mathematical English; this report is accepted for agreement and clarity, not a ban on that noun.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then there exists opens $E_i \subset U_i$ with
+then there exist open subsets $U_i$ with $E_i \subset U_i$ and
````

### MC-STK-ERR-1708

`topology.tex` — 1739; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1739) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use the noun complement for the complement of the displayed covering.

Adverse evidence / qualification: The following contraposition argument is correct; do not adopt the producer's larger redundant rewrite.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The complementary is
+The complement is
````

### MC-STK-ERR-1709

`topology.tex` — 1956; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1956) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Name X before the proof uses it.

Adverse evidence / qualification: The theorem's conventional intended quantification is unambiguous; this is a notation clarification.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A quasi-compact locally Noetherian space is Noetherian.
+A quasi-compact locally Noetherian space $X$ is Noetherian.
````

### MC-STK-ERR-1710

`topology.tex` — 1992; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1992) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Separate the contradiction apposition from the preceding assertion.

Adverse evidence / qualification: The finite subcover argument is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U_{i_{j, l}}$ a contradiction.
+U_{i_{j, l}}$, a contradiction.
````

### MC-STK-ERR-1711

`topology.tex` — 2102; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2102) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Name j explicitly as the varying index in the finite family grouped by i.

Adverse evidence / qualification: The original restricted union is conventionally understood to vary j; this removes ambiguity rather than changing the constructed V_i.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\bigcup_{i = i(x_j)}
+\bigcup_{j : i(x_j) = i}
````

### MC-STK-ERR-1712

`topology.tex` — 2166; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2166) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Explicitly name the displayed summands that become V-prime_k in the refinement.

Adverse evidence / qualification: The original phrase 'other opens ... of the RHS' implicitly identifies the same terms. Classify as an explicit definition, not an absent mathematical construction.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-in the empty set and the other opens $V_{j_0, k}$ of the RHS
+in the empty set. Write $V_{j_0, k} = V_{j_0} \cap W_{i_0 \ldots i_p, k}$
+for $k \in K$. These other opens on the RHS
````

### MC-STK-ERR-1713

`topology.tex` — 2300; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2300) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Correct the past-tense verb.

Adverse evidence / qualification: No quantifier changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-where arbitrary
+were arbitrary
````

### MC-STK-ERR-1714

`topology.tex` — 2388; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2388) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use singular agreement with basis and the idiom is given by.

Adverse evidence / qualification: The noun opens in the next line is valid and is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A basis for the topology of $\prod X_i$ are
+A basis for the topology of $\prod X_i$ is given by
````

### MC-STK-ERR-1715

`topology.tex` — 2417; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2417) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use the article matching the pronunciation of i.

Adverse evidence / qualification: The cofilteredness selection is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-pick a $i
+pick an $i
````

### MC-STK-ERR-1716

`topology.tex` — 2463; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2463) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use the correct article before point.

Adverse evidence / qualification: The product-cover argument is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-choose an point
+choose a point
````

### MC-STK-ERR-1717

`topology.tex` — 2559; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2559) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Delete the duplicated article.

Adverse evidence / qualification: The historical terminology comparison and citation remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and a the terminology
+and the terminology
````

### MC-STK-ERR-1718

`topology.tex` — 2930; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L2930) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Retain explicitly the nonemptiness supplied by assumption (2), so Y minus V is a proper closed subset when minimality is invoked.

Adverse evidence / qualification: The assumption already supplies a nonempty choice, so the theorem and intended proof are not new; this makes an essential choice visible.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-contains an open $V$
+contains a nonempty open $V$
````

### MC-STK-ERR-1719

`topology.tex` — 3047, 3063; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3047-L3063) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Repair the two existential clauses with plural opens.

Adverse evidence / qualification: Opens is valid mathematical English. A finite number of points permits plural notional agreement; the producer's requested changes there are not required. Accept only the two exists-to-exist corrections.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists opens
+there exist opens
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists opens
+there exist opens
````

### MC-STK-ERR-1720

`topology.tex` — 3105; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3105) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Correct the spelling of the French reference label.

Adverse evidence / qualification: No bibliographic key, item number or page changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Corrolaire
+Corollaire
````

### MC-STK-ERR-1721

`topology.tex` — 3129; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3129) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

The M set-builder has a stray closing parenthesis after U_i^c. The coordinate pair (J,x) already closes before the separator, and no other opening parenthesis occurs.

Adverse evidence / qualification: This was independently noticed while reading the three reports about U_K; it is not an additional received report. The set and proof are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U_i^c)\}
+U_i^c\}
````

### MC-STK-ERR-1722

`topology.tex` — 3177; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3177) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Supply the article for the fixed map.

Adverse evidence / qualification: The universally closed implication is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume map
+Assume the map
````

### MC-STK-ERR-1723

`topology.tex` — 3344, 3345; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3344-L3345) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Repair the missing and mistyped articles.

Adverse evidence / qualification: The closed set and open set retain the same roles.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be closed subset
+be a closed subset
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be and open subset
+be an open subset
````

### MC-STK-ERR-1724

`topology.tex` — 3468; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3468) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Delete the duplicated copula.

Adverse evidence / qualification: No finiteness hypothesis changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is is finite
+is finite
````

### MC-STK-ERR-1725

`topology.tex` — 3490; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3490) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Name the three preserved subclasses of the displayed collection directly.

Adverse evidence / qualification: The original phrase can be decoded as subsets of the set of finite unions; the replacement clarifies that collection-level meaning.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the subsets of locally closed, of open and of closed subsets.
+the classes of locally closed, open, and closed subsets.
````

### MC-STK-ERR-1726

`topology.tex` — 3580, 3581; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3580-L3581) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Separate the two clauses and give the singular specialization variable a matching quantifier phrase.

Adverse evidence / qualification: No quantifier scope or specialization relation changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-subset of $X$, if
+subset of $X$. If
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus for all
+Thus for every
````

### MC-STK-ERR-1727

`topology.tex` — 3638, 3644; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3638-L3644) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use a condition-introducing conjunction and plural agreement.

Adverse evidence / qualification: The two composed lifts and their directions remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such as
+such that
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-specialization lift
+specializations lift
````

### MC-STK-ERR-1728

`topology.tex` — 3662; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3662) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Match the lemma's plural lifting-property wording.

Adverse evidence / qualification: The chosen point and its lifted specialization are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-specialization lift
+specializations lift
````

### MC-STK-ERR-1729

`topology.tex` — 3775; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3775) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Restore the inclusion sign between the ellipsis and the final member of the chain.

Adverse evidence / qualification: The mixed French report also repeats the already-composed ambient-space repair MC-STK-ERR-0040. Only the missing relation sign remains to be applied.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\subset \ldots Z_e
+\subset \ldots \subset Z_e
````

### MC-STK-ERR-1730

`topology.tex` — 4015, 4017; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4015-L4017) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Make explicit the open complements used to conclude that U lies in both closed nowhere dense sets and hence is empty.

Adverse evidence / qualification: Precedence conventions can differ; the surrounding proof reveals the intended grouping. These are two operations for one clarification, reported three times.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U \setminus U \cap \overline{B}
+U \setminus (U \cap \overline{B})
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U \setminus U \cap \overline{A}
+U \setminus (U \cap \overline{A})
````

### MC-STK-ERR-1731

`topology.tex` — 4583; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4583) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Explicitly group the rectangular neighbourhood before intersecting it with Z in the product.

Adverse evidence / qualification: The product is naturally read as a unit in context, so the report overstates that the original necessarily has a false parse. This is disambiguation, not a new product theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Z \cap U \times V
+Z \cap (U \times V)
````

### MC-STK-ERR-1732

`topology.tex` — 4594; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4594) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use singular agreement and the same basis idiom as the earlier product-topology repair.

Adverse evidence / qualification: Opens is a valid noun and remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A basis of the topology of $X \times Y$ are
+A basis of the topology of $X \times Y$ is given by
````

### MC-STK-ERR-1733

`topology.tex` — 4754; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4754) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Supply the missing ambient-space preposition.

Adverse evidence / qualification: The sobriety and quasi-compactness argument is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-quasi-compact opens $X'$
+quasi-compact opens of $X'$
````

### MC-STK-ERR-1734

`topology.tex` — 4851; notation clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4851) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Show explicitly that each object of the inverse system is the set difference, closed in the constructible topology.

Adverse evidence / qualification: The subsequent sentence already identifies the spaces correctly; this removes the ambiguity in the displayed scope of lim.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\lim_{a : j \to i} f_a^{-1}(E) \setminus f_a^{-1}(F)
+\lim_{a : j \to i} (f_a^{-1}(E) \setminus f_a^{-1}(F))
````

### MC-STK-ERR-1735

`topology.tex` — 4894; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4894) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Two indexed families of arrows are introduced, requiring the plural noun.

Adverse evidence / qualification: Neither family nor its directions change.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and morphism
+and morphisms
````

### MC-STK-ERR-1736

`topology.tex` — 4922; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L4922) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

A basis here consists of the indicated open subsets, not one singular open.

Adverse evidence / qualification: The mathematical basis assertion is otherwise correct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-by the quasi-compact open,
+by the quasi-compact opens,
````

### MC-STK-ERR-1737

`topology.tex` — 5139; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5139) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Supply the conventional designation preposition.

Adverse evidence / qualification: The compactification definition and subsequent universal property are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and denote $\beta(X)$ the closure
+and denote by $\beta(X)$ the closure
````

### MC-STK-ERR-1738

`topology.tex` — 5367; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5367) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Use the imperative to select a preimage in the standalone sentence.

Adverse evidence / qualification: The surjectivity justification and contradiction remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Writing $x = f(y)$
+Write $x = f(y)$
````

### MC-STK-ERR-1739

`topology.tex` — 5427; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5427) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Remove the stray article before the named identity map.

Adverse evidence / qualification: The retract and extremal-disconnectedness argument is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus the $\text{id}_E$
+Thus $\text{id}_E$
````

### MC-STK-ERR-1740

`topology.tex` — 5448; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5448) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Repair the comparative idiom.

Adverse evidence / qualification: The same cardinal lower bound is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-bigger or equal than
+greater than or equal to
````

### MC-STK-ERR-1741

`topology.tex` — 5771, 5928, 5985; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L5771-L5985) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r53/candidate.manifest.json)

Repair plural agreement in all three parallel product-limit proofs.

Adverse evidence / qualification: One received report covers three independent textual occurrences, not three received reports.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-products commutes
+products commute
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-products commutes
+products commute
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-products commutes
+products commute
````
