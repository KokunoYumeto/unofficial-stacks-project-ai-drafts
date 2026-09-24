# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## stacks

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/stacks.patch)

### MC-STK-ERR-1783

`stacks.tex` — 231; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L231) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The naming clause introduces the same object symbols for their corresponding 1-morphisms. Add the missing preposition and move also to the beginning of the naming clause.

Adverse evidence / qualification: Both functors, their domains and codomains, the 2-fibre-product statement and the comparison by beta composed with alpha inverse remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $x, y : \mathcal{C}/U \to \mathcal{S}$ also the corresponding
+Also denote by $x, y : \mathcal{C}/U \to \mathcal{S}$ the corresponding
````

### MC-STK-ERR-1784

`stacks.tex` — 370; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L370) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore of in the instruction selecting pullback functors. The same wording occurs in the definition at source line 432.

Adverse evidence / qualification: No chosen pullback, coherence data, fibre-product existence hypothesis or reference target changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Make a choice pullbacks
+Make a choice of pullbacks
````

### MC-STK-ERR-1785

`stacks.tex` — 374; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L374) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Two displayed families are introduced by the plural noun families; remove its conflicting singular article.

Adverse evidence / qualification: Both families, index sets, fixed targets and all four required fibre-product forms remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be a families
+be families
````

### MC-STK-ERR-1786

`stacks.tex` — 394-397; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L394-L397) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Put morphism of families before the displayed data specifying that morphism, so the hypothesis has a grammatical noun phrase. Retain the equality of base maps and the original conclusion.

Adverse evidence / qualification: This is a wording repair. No map, index, domain, codomain, hypothesis or conclusion is added, removed or identified.

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
-\item Given a second $\alpha' : I \to J$, $h' : U \to V$ and
-$g'_i : U_i \to V_{\alpha'(i)}$ morphism of families
-of maps with fixed target, then if $h = h'$ the two resulting functors
+\item Given a second morphism of families of maps with fixed target,
+$\alpha' : I \to J$, $h' : U \to V$ and
+$g'_i : U_i \to V_{\alpha'(i)}$, if $h = h'$ then the two resulting functors
 between descent data are canonically isomorphic.
````

### MC-STK-ERR-1787

`stacks.tex` — 640; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L640) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Use the single-word noun for the corresponding morphism presheaves.

Adverse evidence / qualification: The comparison and its hypotheses are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-counter parts
+counterparts
````

### MC-STK-ERR-1788

`stacks.tex` — 639; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L639) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Definition-stack requires Mor(x,y) to be a sheaf. Fullness gives equality of the Hom sets in the fibre categories with those in the ambient stack, using the same chosen cartesian lifts; the restriction maps are then the same uniquely factored arrows. Thus the required Mor presheaf, not only its Isom subpresheaf, inherits the sheaf condition.

Adverse evidence / qualification: The categories here need not be groupoids, so Mor cannot be replaced by Isom. This correction does not change the intended statement. Independently checking the original unqualified isomorphism wording in the first and third assumptions remains part of this source review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathit{Isom}
+\mathit{Mor}
````

### MC-STK-ERR-1789

`stacks.tex` — 675; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L675) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

F maps S1 to S2, so its image objects belong to S2. At f:V->U the exact map sends phi to beta_V^{-1} F(phi) alpha_V, where alpha_V:f^*F(x)->F(f^*x) and beta_V:f^*F(y)->F(f^*y) are the unique comparison isomorphisms commuting with the cartesian projections. Its inverse sends psi to the unique phi with F(phi)=beta_V psi alpha_V^{-1}, by full faithfulness of F on the fibre. Both maps commute with restrictions by uniqueness of cartesian factorization. Thus this is an isomorphism of the displayed presheaves, with precisely the corrected target subscript.

Adverse evidence / qualification: The base site, source presheaf, image objects, functors and descent argument remain unchanged. The comparison is already typed this way in lemma-presheaf-mor-map-fibred-categories, source 171-203.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathit{Mor}_{\mathcal{S}_1}(F(x), F(y))
+\mathit{Mor}_{\mathcal{S}_2}(F(x), F(y))
````

### MC-STK-ERR-1790

`stacks.tex` — 684, 686; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L684-L686) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the preposition in both parallel descent-datum sentences.

Adverse evidence / qualification: Both categories, the same covering and the full descent data remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-relative the covering
+relative to the covering
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-relative the covering
+relative to the covering
````

### MC-STK-ERR-1791

`stacks.tex` — 747; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L747) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the article introducing the second fibre-product object.

Adverse evidence / qualification: The complete quadruple and its common base object U remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be second
+be a second
````

### MC-STK-ERR-1792

`stacks.tex` — 752; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L752) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Agree the demonstrative with the plural noun.

Adverse evidence / qualification: Both displayed isomorphisms and the morphism-presheaf fibre-product formula remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-With this identifications
+With these identifications
````

### MC-STK-ERR-1793

`stacks.tex` — 884; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L884) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the article for the singular functor.

Adverse evidence / qualification: The original functor, domain, codomain and size hypotheses remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is functor
+is a functor
````

### MC-STK-ERR-1794

`stacks.tex` — 890; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L890) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Use the appropriate article before equivalent.

Adverse evidence / qualification: No change to equivalence or the stated size obstruction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a equivalent category
+an equivalent category
````

### MC-STK-ERR-1795

`stacks.tex` — 891; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L891) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Agree the noun with the singular fibre and article.

Adverse evidence / qualification: The possible proper class of isomorphism classes is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a fibre categories
+a fibre category
````

### MC-STK-ERR-1796

`stacks.tex` — 1037; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1037) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the site hypothesis required by the defined 2-category of stacks in groupoids and both stack lemmas invoked in the proof. A topology is needed to give meaning to descent and to the stack condition.

Adverse evidence / qualification: The same site is already fixed in definition-stacks-in-groupoids-over-C at 1010. The fibre-product construction and its universal property are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $\mathcal{C}$ be a category.
+Let $\mathcal{C}$ be a site.
````

### MC-STK-ERR-1797

`stacks.tex` — 1276-1278; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1276-L1278) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The local essential-image hypothesis supplies one object x over U and one fibre isomorphism f:F(x)->G(y). State this directly so the quadruple (U,x,y,f) is a well-defined object of the 2-fibre product. Since G(gamma)=id, its endomorphism (id_x,gamma) obeys G(gamma) f = f F(id_x).

Adverse evidence / qualification: The shorter producer proposal saying that f is a morphism is also mathematically sufficient because the fibre is a groupoid; the adopted wording states exactly the supplied essential-image witness and repairs the original plural grammar. No stronger hypothesis is added.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-we may therefore assume that we have
-$f : F(x) \to G(y)$ for some object $x$ of $\mathcal{S}_2$ over $U$
-and morphisms $f$ of $(\mathcal{S}_1)_U$. In this case we get
+we may therefore assume that there are an object $x$ of $\mathcal{S}_2$
+over $U$ and an isomorphism $f : F(x) \to G(y)$ in
+$(\mathcal{S}_1)_U$. In this case we get
````

### MC-STK-ERR-1798

`stacks.tex` — 1284; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1284) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

G prime is the projection from S2 times over S1 T1 to S2. It sends (id_x,gamma) to id_x, an arrow in (S2)_U. Restore that target category.

Adverse evidence / qualification: The original object x, base U, arrow and faithfulness inference are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-under $G'$ in $\mathcal{S}_1$
+under $G'$ in $\mathcal{S}_2$
````

### MC-STK-ERR-1799

`stacks.tex` — 1319; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1319) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the verb in the purpose clause.

Adverse evidence / qualification: The local reduction and automorphism-sheaf argument remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-To to this
+To do this
````

### MC-STK-ERR-1800

`stacks.tex` — 1346; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1346) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The presheaf is evaluated at h:V->U. Its pair consists of x in S_V and an arrow f:F(x)->h^*y in T_V; f is a fibre arrow and cannot serve as a base-change arrow to U. Under a map k:W->V over U, restrict x and f and use the cartesian comparison k^*h^*y -> (h k)^*y. This gives the same isomorphism class independently of cartesian choices. The corrected formula has the exact object type used throughout both descent arguments.

Adverse evidence / qualification: Only the base-change label changes. The quotient by pair isomorphism, all objects, the original h, and the arrow f remain explicit. A separate adjacent discovery records incorrectly ordered descent-comparison inverses in this proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-f^*y
+h^*y
````

### MC-STK-ERR-1801

`stacks.tex` — 1537; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1537) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Remove the preposition with no complement.

Adverse evidence / qualification: Both original objects, their bases and the locally defined morphism data are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-any object $y$ of lying over $V$
+any object $y$ lying over $V$
````

### MC-STK-ERR-1802

`stacks.tex` — 1581; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1581) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Cartesianness is a property of arrows. For a strongly cartesian a:y->x over u and a locally represented b:z->x over u v, each local representative b_i factors uniquely as a c_i, with c_i over the prescribed v on that cover. On pairwise overlaps the c_i agree by uniqueness of cartesian factorization. They define a locally defined morphism c:z->y, and the same uniqueness on a common refinement proves that c is unique. Thus G^2 preserves the original strongly cartesian morphisms.

Adverse evidence / qualification: The functor G^2, original categories, object set, base arrows and locally defined morphisms are unchanged; line 1530 uses the correct term for the preceding stage.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-strongly cartesian objects
+strongly cartesian morphisms
````

### MC-STK-ERR-1803

`stacks.tex` — 1596; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1596) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the preposition relating the descent datum to its covering.

Adverse evidence / qualification: The full covering and descent data are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-descent datum relative $\mathcal{U}$
+descent datum relative to $\mathcal{U}$
````

### MC-STK-ERR-1804

`stacks.tex` — 724; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L724) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The preceding definition includes all natural transformations over C, not only invertible ones. To see the distinction exactly, take the one-object one-arrow site with its identity covering. For any small category A, A->C is a stack: it is fibred using identity pullbacks, every Hom presheaf is a sheaf, and descent for the sole identity covering is effective. Take A to be the terminal category and B to be the category with objects 0,1 and a single nonidentity arrow a:0->1. The two functors A->B selecting 0 and 1 preserve cartesian arrows, and a gives a noninvertible 2-morphism. Therefore the defined category of stacks is a 2-category and is not in general a (2,1)-category. Its 2-fibre-product construction and the given proof still apply in this 2-category.

Adverse evidence / qualification: The correction retains all stacks and all specified 2-morphisms. Restricting to groupoids or to invertible transformations would alter the definition and scope. The groupoid-only subcategory is separately identified as (2,1) at 1031-1033.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The $(2, 1)$-category of stacks
+The $2$-category of stacks
````

### MC-STK-ERR-1805

`stacks.tex` — 1381-1382, 1393-1394; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1381-L1394) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Definition-descent-data has phi_ij:pr_0^*x_i->pr_1^*x_j. Here beta_i:F(x_i)->y|Ui and beta_j:F(x_j)->y|Uj. On Ui times_U Uj, the descent compatibility is beta_j F(phi_ij)=beta_i, so F(phi_ij)=beta_j^{-1} beta_i. Likewise alpha_i:x_i->x|Ui and alpha_j:x_j->x|Uj give alpha_j phi_ij=alpha_i. With beta_i=beta|Ui F(alpha_i), the corrected first equation yields F(phi_ij)=F(alpha_j)^{-1} F(alpha_i)=F(alpha_j^{-1} alpha_i), and fibre faithfulness gives phi_ij=alpha_j^{-1} alpha_i. Every restriction in the edited formulas is retained. These equations show precisely that the obtained object x realizes the original descent datum.

Adverse evidence / qualification: The original products beta_j beta_i^{-1} and alpha_j alpha_i^{-1} generally fail to compose: their middle objects differ. Neither the definition of phi_ij nor the displayed directions of beta_i and alpha_i are changed. No commutativity of the morphisms is assumed.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-F(\varphi_{ij}) = \beta_j|_{U_i \times_U U_j} \circ
-(\beta_i|_{U_i \times_U U_j})^{-1}
+F(\varphi_{ij}) = (\beta_j|_{U_i \times_U U_j})^{-1} \circ
+\beta_i|_{U_i \times_U U_j}
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-\varphi_{ij} = \alpha_j|_{U_i \times_U U_j} \circ
-(\alpha_i|_{U_i \times_U U_j})^{-1}
+\varphi_{ij} = (\alpha_j|_{U_i \times_U U_j})^{-1} \circ
+\alpha_i|_{U_i \times_U U_j}
````

### MC-STK-ERR-1806

`stacks.tex` — 1699; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1699) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The preceding item defines Hom sets between descent-data objects in F prime(U), by common refinements; the following item defines F prime(h). The composition just constructed is composition in F prime(U), not in the original category F(U).

Adverse evidence / qualification: The original category F(U) and its canonical map to F prime(U) are still used explicitly at 1722-1724. No original category or formula is replaced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-morphisms in $F(U)$
+morphisms in $F'(U)$
````

### MC-STK-ERR-1807

`stacks.tex` — 1735; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1735) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Supply be in the sentence introducing the already constructed stack and morphism.

Adverse evidence / qualification: The entire universal-property diagram and all functor types are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the stack and $1$-morphism constructed
+be the stack and $1$-morphism constructed
````

### MC-STK-ERR-1808

`stacks.tex` — 1766; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1766) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

F:S->X sends x_i to y_i=F(x_i), and y is obtained by effective descent of the y_i in X. Therefore its restrictions are isomorphic to F(x_i). G(x_i) lies instead in S prime and cannot be the displayed local object in X.

Adverse evidence / qualification: The local isomorphisms alpha_ijk, the induced beta_ij and H(x prime)=y are unchanged. The original G is retained in its proper role comparing x_i with x prime.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-agreeing with $G(x_i)$
+agreeing with $F(x_i)$
````

### MC-STK-ERR-1809

`stacks.tex` — 1839; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1839) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Close the second argument and then the Mor expression: the base sheaf is Mor(j(f(x)),j(f(x prime))). This matches the original base presheaf immediately above and the declared functor j:Y->Y prime.

Adverse evidence / qualification: Every original functor, object and fibre-product factor remains present; this is delimiter repair, not a changed comparison.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\times_{\mathit{Mor}(j(f(x)), j(f(x'))}
+\times_{\mathit{Mor}(j(f(x)), j(f(x')))}
````

### MC-STK-ERR-1810

`stacks.tex` — 1871; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1871) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Supply the article for the specified inertia fibred category.

Adverse evidence / qualification: The inertia construction and stackification claim are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is inertia of the stackification
+is the inertia of the stackification
````

### MC-STK-ERR-1811

`stacks.tex` — 1934; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L1934) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Supply be in the sentence introducing the constructed stack in groupoids and its morphism.

Adverse evidence / qualification: All groupoid conditions, objects and functors are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the stack in groupoids and $1$-morphism constructed
+be the stack in groupoids and $1$-morphism constructed
````

### MC-STK-ERR-1812

`stacks.tex` — 2040; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2040) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Introduce the following content clause with that.

Adverse evidence / qualification: The structure of the inherited site and its original reference are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-fibred category. We say $
+fibred category. We say that $
````

### MC-STK-ERR-1813

`stacks.tex` — 2090; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2090) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Remove the singular article before the plural predicate morphisms.

Adverse evidence / qualification: Both morphisms, their common target, common base arrow and unique fibre isomorphism are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-are both a strongly cartesian
+are both strongly cartesian
````

### MC-STK-ERR-1814

`stacks.tex` — 2151; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2151) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The base functors are p:X->C and q:Y->C, with q F=p. Since F(x_i)=y_i, p(x_i)=q(y_i). The local arrow F(psi_i) therefore defines the section of Isom_Y(F(x),y) over q(y_i), with the cartesian comparison between F(x)|q(y_i) and F(x|q(y_i)) and the covering identification of y_i with y|q(y_i). The expression q(x_i) is undefined because x_i belongs to X.

Adverse evidence / qualification: The two producer alternatives p(x_i) and q(y_i) are exactly equal by q F=p and F(x_i)=y_i. The adopted q(y_i) retains the labels already used in the surrounding restriction equations.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathit{I}(q(x_i))
+\mathit{I}(q(y_i))
````

### MC-STK-ERR-1815

`stacks.tex` — 2218; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2218) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The available hypothesis is q:Y->X a stack for the inherited topology on X. The preceding descent datum is over the covering {x|Ui->x} of X; applying this hypothesis supplies its descent object. Invoking Y/C would invoke the conclusion being proved.

Adverse evidence / qualification: Both original stack assumptions and the resulting descent object over the same U are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-By our assumption that $\mathcal{Y}$ is a stack over $\mathcal{C}$
+By our assumption that $\mathcal{Y}$ is a stack over $\mathcal{X}$
````

### MC-STK-ERR-1816

`stacks.tex` — 2426; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2426) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the subject of may assume.

Adverse evidence / qualification: The original 2-fibre-product replacement and all projection labels remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-fibre product may assume
+fibre product we may assume
````

### MC-STK-ERR-1817

`stacks.tex` — 2448, 2449; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2448-L2449) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The tuple x prime_i=(U,y prime_i,x_i,alpha_i) is in Y prime times_Y X. By the displayed square, F prime is its Y prime projection and G prime is its X projection. The two corrected equations therefore follow directly from the specified objects and functors.

Adverse evidence / qualification: The original functor labels and tuple order remain unchanged; the right sides are restored to their actual codomains.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$F'(x'_i) = x_i$
+$F'(x'_i) = y'_i$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$G'(x'_i) = y'_i$
+$G'(x'_i) = x_i$
````

### MC-STK-ERR-1818

`stacks.tex` — 2516; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2516) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the subject of may assume in this second proof.

Adverse evidence / qualification: Its separate occurrence and separate producer reports are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-fibre product may assume
+fibre product we may assume
````

### MC-STK-ERR-1819

`stacks.tex` — 2739; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2739) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the word both referring to the two displayed lifts.

Adverse evidence / qualification: The associated corrections of their codomains are recorded in a separate mathematical group.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then bot
+Then both
````

### MC-STK-ERR-1820

`stacks.tex` — 2739, 2740; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2739-L2740) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Both arrows lift the fixed a:U->U prime and both underlying arrows beta:y->y prime and beta prime:y double-prime->y prime have common target y prime. Their target objects must therefore both be (U prime,y prime). The cartesian properties then give a unique vertical isomorphism (id_U,iota) from (U,y) to (U,y double-prime) satisfying beta=beta prime iota, proving the stated comparison.

Adverse evidence / qualification: The source pairs, underlying arrows, base arrow a and comparison iota are preserved. No change of arrow direction is made.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(a, \beta) : (U, y) \to (U, y')
+(a, \beta) : (U, y) \to (U', y')
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(a, \beta') : (U, y'') \to (U, y)
+(a, \beta') : (U, y'') \to (U', y')
````

### MC-STK-ERR-1821

`stacks.tex` — 2774, 2775; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2774-L2775) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The functor p:S->D takes values in D. The fibre of the pullback over U consists of pairs (U,y) with p(y)=u(U), and fibre arrows (id_U,beta) with p(beta)=id_u(U). The projection to y and beta has inverse y->(U,y), beta->(id_U,beta), giving the declared identification with S_u(U). The same applies over U prime. Under these identifications, a^*(U prime,y prime)=(U,u(a)^*y prime), exactly as the next displayed formula states.

Adverse evidence / qualification: The source uses equality to denote its explicit identification already declared at 2693-2695. The repair changes only the erroneous indices, retaining the pairs and their comparison maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(u^p\mathcal{S})_U = \mathcal{S}_U
+(u^p\mathcal{S})_U = \mathcal{S}_{u(U)}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(u^p\mathcal{S})_{U'} = \mathcal{S}_{U'}
+(u^p\mathcal{S})_{U'} = \mathcal{S}_{u(U')}
````

### MC-STK-ERR-1822

`stacks.tex` — 2786, 2787; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2786-L2787) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the defined term descent data in both occurrences.

Adverse evidence / qualification: The original covering families, fibre products, all pullback identifications and effectivity assertion are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-descend data
+descent data
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-descend data
+descent data
````

### MC-STK-ERR-1823

`stacks.tex` — 2452; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2452) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The original tuple comparison maps are alpha_k:G(y prime_k)->F(x_k). Given b prime:y prime_1->y prime_2, the required arrow between F(x_1) and F(x_2) is alpha_2 G(b prime) alpha_1^{-1}. Gerbe condition (2)(b) gives local lifts a_i of this exact arrow. Multiplying the corrected equation on the right by alpha_1|Ui gives F(a_i) alpha_1|Ui=alpha_2|Ui G(b prime)|Ui, which is precisely the square defining the fibre-product morphism (b prime|Ui,a_i).

Adverse evidence / qualification: The previous formula omitted both original tuple isomorphisms and equated arrows with different sources and targets. Every original alpha, its direction, and its necessary inverse are now retained.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-$F(a_i) = G(b')|_{U_i}$. Then $(b'|_{U_i}, a_i)$ is a morphism
+$F(a_i) = \alpha_2|_{U_i} \circ G(b')|_{U_i} \circ
+(\alpha_1|_{U_i})^{-1}$. Then $(b'|_{U_i}, a_i)$ is a morphism
````

### MC-STK-ERR-1824

`stacks.tex` — 2771; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2771) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore if in the stated if and only if equivalence.

Adverse evidence / qualification: Both directions are proved in the preceding lemma; no mathematical condition is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-only $\beta$ is strongly cartesian
+only if $\beta$ is strongly cartesian
````

### MC-STK-ERR-1825

`stacks.tex` — 2841; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2841) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the article introducing the fibre arrow alpha.

Adverse evidence / qualification: The full tuple, its base arrows and commutative square remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is morphism of
+is a morphism of
````

### MC-STK-ERR-1826

`stacks.tex` — 2838; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2838) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Supply the noun triple before its three displayed entries.

Adverse evidence / qualification: The entry order a,b,alpha and all their domains and codomains remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is given by a
+is given by a triple
````

### MC-STK-ERR-1827

`stacks.tex` — 2906; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2906) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The two components into u(U1) and u(U prime) must both start at V1. The first is phi1; the second is phi prime b. They have the same composite to u(U), since u(a) phi1=phi b and u(c) phi prime=phi. Therefore the pullback universal property supplies the indicated map phi prime_1:V1->u(U prime_1).

Adverse evidence / qualification: Retain the original b and both original structure maps; the second component previously had the wrong domain.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\phi'_1 = (\phi_1, \phi')
+\phi'_1 = (\phi_1, \phi' \circ b)
````

### MC-STK-ERR-1828

`stacks.tex` — 2909; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2909) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The functor p:S->C sends gamma1:x prime_1->x1 to the projection c prime:U prime_1->U1. The map phi prime_1 instead lies in D and determines the structure map of the new triple.

Adverse evidence / qualification: The original cartesian lift and the pullback projection are retained, with their correct category types.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-p(\gamma_1) = \phi'_1
+p(\gamma_1) = c'
````

### MC-STK-ERR-1829

`stacks.tex` — 2916, 2918; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2916-L2918) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The object x prime_1 lies over U prime_1 and its structure map is phi prime_1:V1->u(U prime_1); x prime lies over U prime and its map is phi prime:V->u(U prime). These are exactly the source and target of (a prime,b,alpha prime), where p(alpha prime)=a prime and u(a prime) phi prime_1=phi prime b.

Adverse evidence / qualification: Restore tuple labels to the already constructed data without changing any map or object.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(U_1, \phi_1 : V_1 \to u(U'_1), x'_1)
+(U'_1, \phi'_1 : V_1 \to u(U'_1), x'_1)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(U, \phi : V \to u(U'), x')
+(U', \phi' : V \to u(U'), x')
````

### MC-STK-ERR-1830

`stacks.tex` — 2925; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2925) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The target is the original object X1 with structure map phi1, as defined at 2891. The arrow (c prime,id_V1,gamma1) satisfies u(c prime) phi prime_1=phi1 and belongs to R because gamma1 is cartesian.

Adverse evidence / qualification: The denominator arrow, target base, target object and original structure map are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(U_1, \phi : V_1 \to u(U_1), x_1)
+(U_1, \phi_1 : V_1 \to u(U_1), x_1)
````

### MC-STK-ERR-1831

`stacks.tex` — 2927-2928; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2927-L2928) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

State that the two constructed arrows form the required commutative square; this also repairs the singular/plural disagreement.

Adverse evidence / qualification: The RMS2 equation is gamma alpha prime=alpha gamma1, with ca prime=ac prime on bases and identity_V b=b identity_V1; both arrows are required, so an isolated singular forms wording would obscure their joint role.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-is an element of $R$ which form a solution of the existence problem
-posed by RMS2.
+is an element of $R$. Together these two morphisms solve the existence
+problem posed by RMS2.
````

### MC-STK-ERR-1832

`stacks.tex` — 2943; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2943) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The target structure map has codomain u(U prime) and is phi prime=u(c) phi. The source phi:V->u(U) is retained, so the same symbol no longer denotes two differently typed arrows.

Adverse evidence / qualification: The relation follows from the defining square for (c,id_V,gamma). Only its target label is repaired.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(U', \phi : V \to u(U'), x')
+(U', \phi' : V \to u(U'), x')
````

### MC-STK-ERR-1833

`stacks.tex` — 2952; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2952) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Because b=b prime, u(a) phi1=phi b=phi b prime=u(a prime) phi1. The equalizer u(d):u(U2)->u(U1) therefore gives the unique phi2:V1->u(U2) with u(d) phi2=phi1, as required for the new source object.

Adverse evidence / qualification: The equalizer, both original parallel arrows and the unique factor phi2 are retained explicitly.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\phi_1 = u(d) \circ \phi_1
+\phi_1 = u(d) \circ \phi_2
````

### MC-STK-ERR-1834

`stacks.tex` — 2953; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2953) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The arrow delta:x2->x1 is a cartesian lift under p:S->C of d:U2->U1. Its p-image is d, while u(d) is the image of that base arrow in D. The lift gives p(x2)=U2 and p(alpha delta)=ad=a prime d=p(alpha prime delta).

Adverse evidence / qualification: No original functor is suppressed; the distinct roles of p and u are restored.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-p(\delta) = u(d)
+p(\delta) = d
````

### MC-STK-ERR-1835

`stacks.tex` — 3017; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3017) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

p_p has codomain D; X lies over V, X1 over V1, and b:V1->V2. Thus p_p(f2)=b b1 has b1:V->V1. This is the base map required for the cartesian factorization X->X1.

Adverse evidence / qualification: The original C-objects U,U1 remain in the triples but do not type a D-base arrow.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-b_1 : U \to U_1
+b_1 : V \to V_1
````

### MC-STK-ERR-1836

`stacks.tex` — 3026; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3026) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The arrow f prime_1 lies in the localized category u_p S, whose structural functor is p_p:u_p S->D, extending p_pp. Since r lies over id_V, passing between f1 and f prime_1 leaves its base arrow b1 unchanged.

Adverse evidence / qualification: The original p:S->C cannot be applied to this localized morphism.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-p(f'_1) = b_1
+p_p(f'_1) = b_1
````

### MC-STK-ERR-1837

`stacks.tex` — 3084; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3084) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The arrows are r:X prime->X and r prime:X double-prime->X prime. Their composite with domain X double-prime is r r prime, the denominator in the refined roof at 3091.

Adverse evidence / qualification: The same two arrows and their given directions are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-r' \circ r \in R
+r \circ r' \in R
````

### MC-STK-ERR-1838

`stacks.tex` — 3088, 3096; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3088-L3096) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The numerator f2=(a2,b2,alpha2) has domain X, while f1,f prime_1 have domain X prime. Comparing their roofs over a common X double-prime requires f f1 r prime=f f prime_1 r prime=f2 r r prime. After refining and renaming X double-prime to X prime, the denominator remains r:X prime->X, so the equation is f f1=f f prime_1=f2 r. Its C-base and fibre-arrow components are precisely a a1=a a prime_1=a2 c and alpha alpha1=alpha alpha prime_1=alpha2 gamma at 3102-3103.

Adverse evidence / qualification: OCC-11940 reports the first omitted denominator only. The second omission at 3096 is an independent adjacent discovery, retained explicitly here; neither can be removed by merely renaming the common source.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(a_2, b_2, \alpha_2) \circ r'
+(a_2, b_2, \alpha_2) \circ r \circ r'
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(a_2, b_2, \alpha_2).
+(a_2, b_2, \alpha_2) \circ r.
````

### MC-STK-ERR-1839

`stacks.tex` — 3098; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3098) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Complete the declared arrow signature with its already fixed target X=(U,phi:V->u(U),x). This makes the ensuing equations a2 c and alpha2 gamma explicitly typed.

Adverse evidence / qualification: This is the same r:X prime->X already specified at 3079-3080; no target is newly selected.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Write $r = (c, \text{id}_V, \gamma) : (U', \phi' : V \to u(U'), x')$,
+Write $r = (c, \text{id}_V, \gamma) : (U', \phi' : V \to u(U'), x')
+\to (U, \phi : V \to u(U), x)$,
````

### MC-STK-ERR-1840

`stacks.tex` — 3113; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3113) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The new arrow gamma prime:x double-prime->x prime is the cartesian lift of the equalizer inclusion c prime:U double-prime->U prime under p:S->C. The old gamma:x prime->x is already a morphism of S, so is not a base arrow that p can lift. With the corrected lift, the precomposed fibre arrows have equal p-images; cartesianness of alpha then gives their equality.

Adverse evidence / qualification: The equalizer object, both original parallel arrows, the denominator and every fibre object are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-lifting $\gamma$
+lifting $c'$
````

### MC-STK-ERR-1841

`stacks.tex` — 2912; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2912) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The cartesian property of gamma lifts the particular arrow alpha gamma1 over ac prime=ca prime. It supplies the unique alpha prime over a prime whose composite with gamma is alpha gamma1; its base alone does not specify it uniquely. This exact equation also proves the square required by RMS2.

Adverse evidence / qualification: The equation uses only the existing arrows and is required by the cited universal property. It is an independent omission adjacent to the reported base-lift label error.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-$\alpha' : x'_1 \to x'$ with $p(\alpha') = a'$.
+$\alpha' : x'_1 \to x'$ with $p(\alpha') = a'$ and
+$\gamma \circ \alpha' = \alpha \circ \gamma_1$.
````

### MC-STK-ERR-1842

`stacks.tex` — 3161; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3161) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Separate the concluding hence clause from its cited justification.

Adverse evidence / qualification: The cited result and the invertibility argument are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Categories, Lemma \ref{categories-lemma-fibred-groupoids}
+Categories, Lemma \ref{categories-lemma-fibred-groupoids};
````

### MC-STK-ERR-1843

`stacks.tex` — 3205; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3205) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The defined source-arrow notation is alpha/a. A target arrow in u^p T consists of its C-base a and its T-arrow beta. Here beta=G prime(a,u(a),alpha) has q-image u(a), because G is over D. Hence the complete ordered pair is exactly (a,G prime(a,u(a),alpha)); it maps the object H(x/U) to H(x prime/U prime) with the types declared at 3201. Composition is componentwise: the C-components compose to a prime a and the T-components compose by functoriality of G prime; identities likewise have both required components.

Adverse evidence / qualification: Retain the previously suppressed base component a. No convention about recovering that component is needed and no object is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H((\alpha, a) : x/U \to x'/U') = G'(a, u(a), \alpha)
+H(\alpha/a : x/U \to x'/U') = (a, G'(a, u(a), \alpha))
````

### MC-STK-ERR-1844

`stacks.tex` — 3196; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3196) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the preposition introducing the notation for the composite functor.

Adverse evidence / qualification: Both functors and their exact domains and codomains are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $G'
+Denote by $G'
````

### MC-STK-ERR-1845

`stacks.tex` — 3225; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3225) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore by in the naming clause for the projection functor.

Adverse evidence / qualification: The original projection and its value on (U,y) are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We denote
+We denote by
````

### MC-STK-ERR-1846

`stacks.tex` — 3246; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3246) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Use the source-arrow notation alpha/a established at 3191 and used in the corrected functor definition.

Adverse evidence / qualification: The full bottom arrow is pr(H(alpha/a)); its C-base has been forgotten by pr, leaving the required arrow in T. The square and all four objects are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H(a, \alpha)
+H(\alpha/a)
````

### MC-STK-ERR-1847

`stacks.tex` — 625-626; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L625-L626) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The literal unqualified condition permits changing the base object. Take the two-object groupoid with objects A,B and one arrow between each pair, all singleton-isomorphism covers, S=C with p=id, and S prime the full subcategory on A. S is a stack with terminal fibres. Every object of S is isomorphic to A, so all three original conditions hold, but S prime has no object over B and cannot lift B->A. With the corrected condition, an ambient cartesian lift c:y->x over f:V->U can be composed with a vertical isomorphism e:y prime->y from an S prime object; c e is an S prime cartesian lift by fullness. The inclusion preserves cartesian arrows by comparison with these lifts. Moreover any total isomorphism z->t with t in S prime, over h:U->W, becomes vertical by composing with the inverse of a cartesian S prime lift t_U->t of h. Thus the original condition (3) gives the fibre isomorphism needed for descent. The complete proof, including the exact natural Mor comparison and all descent comparison maps, is in SUBSTACK_VERTICAL_DERIVATION_20260923.md, Sections 3-7.

Adverse evidence / qualification: Qualifying (1) is sufficient: once S prime is fibred, the explicit cartesian lift of the base isomorphism proves that the unqualified condition (3) is equivalent to its fibre-qualified version. No unnecessary independent strengthening of (3) is asserted. The note was independently derived and then fully read and checked in the primary session.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-$x$ is an object of $\mathcal{S}'$, then $y$ is isomorphic to an
-object of $\mathcal{S}'$,
+$x$ is an object of $\mathcal{S}'$, then $y$ is isomorphic in
+$\mathcal{S}_{p(y)}$ to an object of $\mathcal{S}'$,
````

### MC-STK-ERR-1848

`stacks.tex` — 3277; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3277) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Remove the article before the predicate adjective.

Adverse evidence / qualification: The full mathematical claim and its dependent argument are being checked separately; this wording repair alone does not certify the asserted characterization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a strongly cartesian.
+is strongly cartesian.
````

### MC-STK-ERR-1849

`stacks.tex` — 3279; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3279) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

A roof representing f:X->Y has numerator X prime->Y and denominator r:X prime->X; in the localization it is Q(numerator) Q(r)^{-1}. Restore the denominator target X.

Adverse evidence / qualification: The arrow f, numerator, denominator membership in R and all fibre/base components are retained. The separate mathematical correction to the cartesian characterization must be proved before candidate acceptance.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-r : X' \to Y
+r : X' \to X
````

### MC-STK-ERR-1850

`stacks.tex` — 3281; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3281) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore the separator between the second and third entries of the existing triple.

Adverse evidence / qualification: The original three entries and their defined meanings remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-G'(a, b \alpha)
+G'(a, b, \alpha)
````

### MC-STK-ERR-1851

`stacks.tex` — 3283; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3283) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Use the defined source-morphism notation alpha/a in this second occurrence.

Adverse evidence / qualification: The projected morphism pr(H(alpha/a)) and all its domain and codomain data are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H(a, \alpha)
+H(\alpha/a)
````

### MC-STK-ERR-1852

`stacks.tex` — 3285; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3285) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Agree the verb with the plural subject all arrows except possibly beta.

Adverse evidence / qualification: The sentence still distinguishes beta from the three arrows already known to be cartesian; no property of beta is assumed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\beta$ is strongly cartesian
+$\beta$ are strongly cartesian
````

### MC-STK-ERR-1853

`stacks.tex` — 3436, 3459; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3436-L3459) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Use the noun phrase full faithfulness in both the subsection lead-in and its later restatement.

Adverse evidence / qualification: The received locus identifies the first occurrence; the second matching misuse at 3459 was found in the same paragraph and is recorded explicitly.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Fully faithfulness.
+Full faithfulness.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-proof of fully faithfulness
+proof of full faithfulness
````

### MC-STK-ERR-1854

`stacks.tex` — 3446; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3446) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Supply a grammatical subject for the pullback assertion.

Adverse evidence / qualification: Both producer alternatives convey the same assertion; the adopted text directly refers to the preceding equality without altering it.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Similar holds
+The same holds
````

### MC-STK-ERR-1855

`stacks.tex` — 3464; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3464) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The category u_p S is over D. The canonical functor c prime sends x over U to (U,id_u(U),x), whose D-base is u(U). Therefore its Hom set between c prime(x) and c prime(y) is taken in the fibre over u(U).

Adverse evidence / qualification: All objects and functors are unchanged; the corrected target agrees with the presheaf formula already given at 3457 and the sentence immediately after the display.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_{(u_p\mathcal{S})_U}
+\Mor_{(u_p\mathcal{S})_{u(U)}}
````

### MC-STK-ERR-1856

`stacks.tex` — 3482; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3482) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Here c:U prime->U and c prime:U->U prime. The denominator square gives u(c) phi=id_u(U). Writing phi=u(c prime), faithfulness of u yields c c prime=id_U, whose domain and codomain are U. The cartesian property of gamma then lifts c prime against id_x to the specified gamma prime with gamma gamma prime=id_x.

Adverse evidence / qualification: The base object U prime is retained as the domain of c; only the falsely typed identity is repaired.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$c \circ c' = \text{id}_{U'}$
+$c \circ c' = \text{id}_U$
````

### MC-STK-ERR-1857

`stacks.tex` — 3536; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3536) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

Restore by in the naming clause for the localization functor.

Adverse evidence / qualification: This is a distinct Stacks chapter occurrence, unrelated to the differently located Categories report mentioned by the producer.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We denote $j
+We denote by $j
````

### MC-STK-ERR-1858

`stacks.tex` — 3009-3011, 3124-3128; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3009-L3128) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r56/candidate.manifest.json)

The original converse is false. Let C=[0->1], D be terminal, and S have objects z over 0 and s,t over 1, with nonidentity arrows r_s:z->s, v:s->t, r_t:z->t=v r_s. Both r_s and r_t are cartesian, whereas v is not invertible and hence not cartesian over id_1. Both cartesian arrows become invertible in the localization, so Q(v)=Q(r_t)Q(r_s)^{-1} is invertible and cartesian. The corrected criterion retains the entire original construction and states exactly that Q(a,b,alpha) is cartesian iff an allowed R-refinement makes alpha gamma cartesian. The inserted proof derives invertibility of a vertical arrow after an admissible pullback from an inverse roof: equalize its two base maps, obtain a vertical inverse candidate, refine each inverse equation using the right-fraction equality criterion, pass to a common fibre-product refinement, and use cartesian uniqueness to prove both actual inverse identities. Factoring alpha through a cartesian lift then proves the full criterion, including refinement of any chosen roof. The complete independent derivation and counterexample are retained in LOCALIZED_CARTESIAN_DERIVATION_20260924.md, Sections 1-8.

Adverse evidence / qualification: No extra conservativity assumption is imposed and the original fibred-category and adjointness conclusions are retained. The false claim about an arbitrary numerator is replaced by a proved statement about a suitable refinement, not by an unproved existence assertion. The source construction preserves every original base arrow, comparison map and needed inverse. The later roof-based argument at 3274-3286 remains valid by the now-proved final paragraph; its independently recorded label corrections are retained.

````diff
--- original
+++ replacement
@@ -1,3 +1,5 @@
 of $u_{pp}\mathcal{S}$ has image $f = ((a, b, \alpha), 1)$
-strongly cartesian in $u_p\mathcal{S}$ if and only if $\alpha$
-is a strongly cartesian morphism of $\mathcal{S}$.
+strongly cartesian in $u_p\mathcal{S}$ if and only if there is an arrow
+$r = (c,\text{id}_{V_1},\gamma) : Z \to X_1$ in $R$ such that
+$\alpha \circ \gamma$ is strongly cartesian in $\mathcal{S}$.
+In particular, this holds whenever $\alpha$ is strongly cartesian.
````

````diff
--- original
+++ replacement
@@ -1,5 +1,166 @@
-We omit the proof of the fact that for any strongly cartesian morphism
-of $u_p\mathcal{S}$ of the form $((a, b, \alpha), 1)$ the morphism
-$\alpha$ is strongly cartesian in $\mathcal{S}$.
-(We do not need the characterization of strongly cartesian morphisms
-in the rest of the proof, although we do use it later in this section.)
+We prove the converse with the stated refinement. Write
+$Q : u_{pp}\mathcal{S} \to u_p\mathcal{S}$ for the localization functor.
+For $Y = (U, \phi : V \to u(U), y)$ and $b : V' \to V$, put
+$$
+Y_b = (U, \phi \circ b : V' \to u(U), y),\qquad
+k_b = (\text{id}_U, b, \text{id}_y) : Y_b \to Y.
+$$
+The implication already proved shows that $Q(k_b)$ is strongly cartesian.
+Consequently every morphism $h : X \to Y$ over $b$ factors uniquely as
+$h = Q(k_b) \circ i_h$, with $i_h : X \to Y_b$ over $\text{id}_{V'}$.
+Moreover, $h$ is strongly cartesian if and only if $i_h$ is an isomorphism.
+Indeed, if $h$ is strongly cartesian, its universal property gives
+$j : Y_b \to X$ over $\text{id}_{V'}$ with $h \circ j = Q(k_b)$.
+Uniqueness for $Q(k_b)$ gives $i_h \circ j = \text{id}_{Y_b}$, and
+uniqueness for $h$ gives $j \circ i_h = \text{id}_X$.
+The reverse implication follows by composition with an isomorphism.
+
+\medskip\noindent
+We first establish the required detection of vertical isomorphisms.
+Fix $\phi : V \to u(U)$ and a morphism $\delta : x \to y$ in
+$\mathcal{S}_U$. Write
+$$
+D_\delta = (\text{id}_U, \text{id}_V, \delta) :
+(U,\phi,x) \longrightarrow (U,\phi,y).
+$$
+We claim that $Q(D_\delta)$ is invertible if and only if there exist
+$c : W \to U$ and $\psi : V \to u(W)$ with $u(c) \circ \psi = \phi$
+such that the pullback of $\delta$ along $c$ is invertible.
+More explicitly, choose strongly cartesian morphisms
+$\gamma_x : x_W \to x$ and $\gamma_y : y_W \to y$ over $c$.
+The pullback is the unique vertical morphism $\delta_W : x_W \to y_W$
+such that
+$$
+\gamma_y \circ \delta_W = \delta \circ \gamma_x.
+$$
+Changing these two cartesian lifts conjugates $\delta_W$ by the unique
+vertical comparison isomorphisms, so invertibility is independent of
+these choices. If $\delta_W$ is invertible, the displayed equation and
+the two morphisms of $R$ defined by $\gamma_x,\gamma_y$ show that
+$Q(D_\delta)$ is invertible.
+
+\medskip\noindent
+Conversely, represent an inverse to $Q(D_\delta)$ by $Q(e)Q(r)^{-1}$, where
+$$
+r = (c,\text{id}_V,\gamma) : (T,\theta,z) \to (U,\phi,y),\qquad
+e = (a,\text{id}_V,\epsilon) : (T,\theta,z) \to (U,\phi,x),
+$$
+and $r \in R$. Thus $a,c : T \to U$ and
+$u(a)\theta = \phi = u(c)\theta$.
+Let $h : T_1 \to T$ be the equalizer of $a,c$.
+As $u$ preserves this equalizer, there exists
+$\theta_1 : V \to u(T_1)$ with $u(h)\theta_1 = \theta$.
+Choose a strongly cartesian $\zeta : z_1 \to z$ over $h$ and refine
+the inverse roof by $(h,\text{id}_V,\zeta) \in R$.
+Put $d = ah = ch$ and $y_1 = z_1$.
+Then $\tau_y = \gamma\zeta : y_1 \to y$ is strongly cartesian over $d$.
+Choose a strongly cartesian $\tau_x : x_1 \to x$ over $d$.
+There are unique vertical morphisms
+$\eta : y_1 \to x_1$ and $\delta_1 : x_1 \to y_1$ satisfying
+$$
+\tau_x\eta = \epsilon\zeta,\qquad
+\tau_y\delta_1 = \delta\tau_x.
+$$
+For this paragraph, regard $x_1,y_1$ as the triples with base $T_1$
+and structure map $\theta_1$, and write
+$$
+t_x = (d,\text{id}_V,\tau_x),\quad
+t_y = (d,\text{id}_V,\tau_y),\quad
+E_\eta = (\text{id}_{T_1},\text{id}_V,\eta),\quad
+D_1 = (\text{id}_{T_1},\text{id}_V,\delta_1).
+$$
+The inverse is $Q(t_x)Q(E_\eta)Q(t_y)^{-1}$, whereas
+$Q(D_\delta) = Q(t_y)Q(D_1)Q(t_x)^{-1}$.
+The two inverse identities therefore give
+$$
+Q(E_\eta D_1) = \text{id}_{(T_1,\theta_1,x_1)},\qquad
+Q(D_1 E_\eta) = \text{id}_{(T_1,\theta_1,y_1)}.
+$$
+The equality criterion for right fractions, applied to denominators
+equal to identities, supplies two arrows of $R$. Write their
+$\mathcal{C}$-components as $c_x : T_x \to T_1$ and
+$c_y : T_y \to T_1$, their structure maps as $\theta_x,\theta_y$, and
+their strongly cartesian $\mathcal{S}$-components as
+$\rho_x : z_x \to x_1$ and $\rho_y : z_y \to y_1$.
+Then
+$$
+(\eta\delta_1)\rho_x = \rho_x,\qquad
+(\delta_1\eta)\rho_y = \rho_y,\qquad
+u(c_x)\theta_x = \theta_1 = u(c_y)\theta_y.
+$$
+Form $T_2 = T_x \times_{T_1} T_y$, with projections $e_x,e_y$, and put
+$k = c_xe_x = c_ye_y$. Preservation of this fibre product gives
+$\theta_2 : V \to u(T_2)$ such that
+$u(e_x)\theta_2 = \theta_x$ and $u(e_y)\theta_2 = \theta_y$.
+In particular $u(k)\theta_2 = \theta_1$ and $u(dk)\theta_2 = \phi$.
+Choose strongly cartesian arrows $\kappa_x : x_2 \to x_1$ and
+$\kappa_y : y_2 \to y_1$ over $k$, and the unique vertical arrows
+$\delta_2 : x_2 \to y_2$ and $\eta_2 : y_2 \to x_2$ with
+$$
+\kappa_y\delta_2 = \delta_1\kappa_x,\qquad
+\kappa_x\eta_2 = \eta\kappa_y.
+$$
+Since $k = c_xe_x$, cartesianness of $\rho_x$ factors $\kappa_x$
+through $\rho_x$, and hence $\eta\delta_1\kappa_x = \kappa_x$.
+Similarly $\delta_1\eta\kappa_y = \kappa_y$.
+It follows that
+$$
+\kappa_x\eta_2\delta_2
+= \eta\kappa_y\delta_2
+= \eta\delta_1\kappa_x
+= \kappa_x,
+$$
+and
+$$
+\kappa_y\delta_2\eta_2
+= \delta_1\kappa_x\eta_2
+= \delta_1\eta\kappa_y
+= \kappa_y.
+$$
+Cartesian uniqueness, with fixed identity base maps, yields
+$\eta_2\delta_2 = \text{id}_{x_2}$ and
+$\delta_2\eta_2 = \text{id}_{y_2}$.
+The composites $\tau_x\kappa_x,\tau_y\kappa_y$ are strongly cartesian
+over $dk$, and
+$$
+(\tau_y\kappa_y)\delta_2 = \delta(\tau_x\kappa_x).
+$$
+Thus $\delta_2$ is the required invertible pullback of $\delta$.
+This proves the detection claim without assuming that localization
+reflects isomorphisms before a refinement.
+
+\medskip\noindent
+Return to $A = (a,b,\alpha) : X_1 \to X_2$.
+Choose a strongly cartesian $\tau : a^*x_2 \to x_2$ over $a$, and
+write $\alpha = \tau\delta$, where $\delta : x_1 \to a^*x_2$ is vertical.
+Put $X_a = (U_1,\phi_1 : V_1 \to u(U_1),a^*x_2)$.
+The exact factorization is
+$$
+A = k_b \circ (a,\text{id}_{V_1},\tau)
+\circ (\text{id}_{U_1},\text{id}_{V_1},\delta),
+$$
+where $k_b : (X_2)_b \to X_2$, and the middle factor belongs to $R$.
+Consequently, if $Q(A)$ is strongly cartesian, its vertical factor
+relative to $Q(k_b)$ is invertible, and so is $Q(D_\delta)$.
+The detection claim supplies $c : W \to U_1$, $\psi : V_1 \to u(W)$
+with $u(c)\psi = \phi_1$, strongly cartesian
+$\gamma : z \to x_1$ and $\rho : w \to a^*x_2$ over $c$, and an
+invertible $\delta_W : z \to w$ such that
+$\rho\delta_W = \delta\gamma$.
+Therefore
+$$
+\alpha\gamma = \tau\delta\gamma = \tau\rho\delta_W
+$$
+is strongly cartesian. The arrow
+$r = (c,\text{id}_{V_1},\gamma) : (W,\psi,z) \to X_1$
+belongs to $R$, as required.
+Conversely, if such an $r$ exists, the implication proved earlier
+shows that $Q(Ar)$ is strongly cartesian. Since $Q(r)$ is an
+isomorphism, $Q(A) = Q(Ar)Q(r)^{-1}$ is strongly cartesian as well.
+This proves the stated characterization.
+For any chosen roof $Q(A)Q(r_0)^{-1}$ representing a strongly
+cartesian morphism, the same argument gives an additional $r_1 \in R$
+with cartesian numerator in the refined roof
+$Q(Ar_1)Q(r_0r_1)^{-1}$. Thus the characterization applies to the
+roof representation used below, without asserting that an arbitrary
+original numerator is already strongly cartesian.
````
