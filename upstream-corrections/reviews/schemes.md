# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## schemes

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/schemes.patch)

### MC-STK-ERR-1578

`schemes.tex` — 1373; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L1373) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The refined cover is D(f_i) at 1301 and phi_i at 1303 identifies the sheaf on that open with the sheaf from M_i. Thus phi_i inverse sends m_i to a section on D(f_i), which is then restricted to D(f_if_j).

Adverse evidence / qualification: Earlier arbitrary opens U occur before refinement, but no indexed U_i is defined for this later cover. The correction names the actual domain without altering the glueing argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{F}(U_i)
+\mathcal{F}(D(f_i))
````

### MC-STK-ERR-1579

`schemes.tex` — 3754; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L3754) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The property named immediately above is universally closed; the adverb modifies closed.

Adverse evidence / qualification: The intended property is already inferable; this is terminology/prose repair, not a new criterion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-universal closed morphisms
+universally closed morphisms
````

### MC-STK-ERR-1580

`schemes.tex` — 4078; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4078) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The equivalence phrase has a missing final d in and.

Adverse evidence / qualification: No logical direction or hypothesis changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-if an only if
+if and only if
````

### MC-STK-ERR-1581

`schemes.tex` — 4252; diagram source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4252) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The cartesian square has one bottom edge, the diagonal T to T times_S T. The second identical-direction arrow instruction contributes no second morphism or label and duplicates that edge.

Adverse evidence / qualification: Depending on rendering, two identical arrows may visually overprint and look like one. The source duplication is certain; a claim of visible double arrows is not needed. Verify the affected diagram at the build gate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-T \ar[r]^{\Delta_{T/S}} \ar[r] & T \times_S T
+T \ar[r]^{\Delta_{T/S}} & T \times_S T
````

### MC-STK-ERR-1582

`schemes.tex` — 4434; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4434) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

GL_2 is represented by matrices whose determinant ad-bc is a unit. Its coordinate ring inverts the entire determinant. The printed slash expression does not group that denominator and instead reads as 1/(ad) minus bc (or 1/a times d minus bc); neither is the displayed localization of GL_2.

Adverse evidence / qualification: A reader may infer the intended denominator from the name GL_2. Adding parentheses makes that existing intended coordinate ring explicit; it does not extend the theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-1/ad - bc
+1/(ad - bc)
````

### MC-STK-ERR-1583

`schemes.tex` — 4452; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4452) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The morphism has two scheme objects; the standard category description is morphism of schemes.

Adverse evidence / qualification: No change to the four properties under discussion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of scheme where
+of schemes where
````

### MC-STK-ERR-1584

`schemes.tex` — 4498; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4498) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The title omits of between criterion and separatedness; the section heading already supplies the complete phrase.

Adverse evidence / qualification: Title-only correction; no theorem hypothesis changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Valuative criterion separatedness
+Valuative criterion of separatedness
````

### MC-STK-ERR-1585

`schemes.tex` — 4742; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4742) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The subject names the kernel and cokernel, two objects, and takes a plural verb.

Adverse evidence / qualification: The mathematical assertion already includes both objects; this does not claim a new closure property.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is quasi-coherent.
+are quasi-coherent.
````

### MC-STK-ERR-1586

`schemes.tex` — 4811; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4811) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The paired restriction-sheaf symbols form a plural subject.

Adverse evidence / qualification: Restriction to the corresponding open remains distributive; no sheaf or map is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{F}_i, \mathcal{F}_{ijk}$ denotes the
+$\mathcal{F}_i, \mathcal{F}_{ijk}$ denote the
````

### MC-STK-ERR-1587

`schemes.tex` — 4817; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L4817) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The preceding line says second and, so the pair of numbered terms needs the plural noun terms.

Adverse evidence / qualification: The exact sequence and quasi-coherence conclusion are unaffected.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-third term of the exact sequence are
+third terms of the exact sequence are
````

### MC-STK-ERR-1588

`schemes.tex` — 145; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L145) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The sentence introduces f and g, two morphisms.

Adverse evidence / qualification: Only number agreement changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be morphism of locally
+be morphisms of locally
````

### MC-STK-ERR-1589

`schemes.tex` — 267; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L267) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The sheaf O_V lives on V, and the declared map with codomain V is f': X to V. Lines 257–260 explicitly factor the inverse image through f', and lines 264 and 268 use f' inverse already. The missing prime at 267 is the unique inconsistent sheaf-domain annotation.

Adverse evidence / qualification: Readers can regard f as implicitly corestricted to V, but the proof has deliberately named that corestriction f'. Keeping the explicit name avoids an undeclared identification.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f^{-1}(\mathcal{O}_V)
+$f'^{-1}(\mathcal{O}_V)
````

### MC-STK-ERR-1590

`schemes.tex` — 922; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L922) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The printed subject restriction mapping is singular, so is restores agreement without altering the localization construction.

Adverse evidence / qualification: Pluralizing mapping instead would also be grammatical; the smaller verb substitution preserves the printed subject.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-restriction mapping on the affine schemes are defined
+restriction mapping on the affine schemes is defined
````

### MC-STK-ERR-1591

`schemes.tex` — 1103; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L1103) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The paragraph varies x, and both the predicate maps and the following relative clause are plural. Pluralizing the subject gives consistent agreement.

Adverse evidence / qualification: Each individual stalk has one map; the statement ranges over all such stalks.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The induced map on stalks are the maps
+The induced maps on stalks are the maps
````

### MC-STK-ERR-1592

`schemes.tex` — 1356; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L1356) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The existential asserts one R-module M, requiring exists.

Adverse evidence / qualification: No existence or uniqueness claim is strengthened.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist an $R$-module
+there exists an $R$-module
````

### MC-STK-ERR-1593

`schemes.tex` — 2964; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L2964) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The comma immediately after Because separates the conjunction from its subject rather than an intervening parenthesis.

Adverse evidence / qualification: The functor representation and uniqueness argument remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Because, $(U_i,
+Because $(U_i,
````
