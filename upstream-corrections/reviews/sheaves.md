# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## sheaves

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sheaves.patch)

### MC-STK-ERR-0077

`sheaves.tex` — 192-195; typing/prose.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L193) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The display types zero as an element and negation as a map; the plural head misclassifies zero.

Adverse evidence / qualification: A singleton-domain encoding is possible abstractly but is not used at this locus.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then the zero and the negation maps are
+then the zero element and the negation map are
````

### MC-STK-ERR-0078

`sheaves.tex` — 320-327; agreement/number.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L325) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

A fixed inclusion supplies one restriction mapping and one image.

Adverse evidence / qualification: A collective plural rewrite would require a larger change.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the restriction mappings $\rho^U_V$ is the image
+the restriction mapping $\rho^U_V$ is the image
````

### MC-STK-ERR-0079

`sheaves.tex` — 339-350; substantive definition gap.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L349) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Composition alone permits nonidentity idempotent self-restrictions, so the direct data definition must impose the identity axiom.

Adverse evidence / qualification: Calling a presheaf a contravariant functor would build identities in, but this passage purports to list the data and axioms directly.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $\mathcal{C}$ such that whenever $W \subset V \subset U$
+in $\mathcal{C}$ such that $\rho_U^U = \text{id}_{\mathcal{F}(U)}$ for every open $U \subset X$, and whenever $W \subset V \subset U$
````

### MC-STK-ERR-0080

`sheaves.tex` — 351-354; substantive morphism-data/wording.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L351-L354) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

A natural transformation requires a component for every open and compatibility; one free unindexed U is insufficient.

Adverse evidence / qualification: Suppressing component subscripts is conventional only after the family has been quantified.

````diff
--- original
+++ replacement
@@ -1,4 +1,5 @@
 \item A {\it morphism $\varphi : \mathcal{F} \to \mathcal{G}$
-of presheaves with value in $\mathcal{C}$} is given by a
-morphism $\varphi : \mathcal{F}(U) \to \mathcal{G}(U)$
-in $\mathcal{C}$ compatible with restriction morphisms.
+of presheaves with values in $\mathcal{C}$} is given by
+morphisms $\varphi_U : \mathcal{F}(U) \to \mathcal{G}(U)$
+in $\mathcal{C}$, one for every open $U \subset X$, compatible with
+restriction morphisms.
````

### MC-STK-ERR-0081

`sheaves.tex` — 402-410; duplicated word.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L409-L410) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The phrase repeats 'structure' in the same syntactic role.

Adverse evidence / qualification: The sentence is recoverable but lexically defective.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 defines the structure of an $\mathcal{O}(U)$-module
-structure on the abelian group $\mathcal{F}(U)$.
+on the abelian group $\mathcal{F}(U)$.
````

### MC-STK-ERR-0082

`sheaves.tex` — 596-604; missing grammatical relation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L601) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The bare singular 'open set' lacks a determiner or copula.

Adverse evidence / qualification: Compressed 'U open' is conventional; 'U open set' is not.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For $U \subset X$ open set
+For every open $U \subset X$
````

### MC-STK-ERR-0083

`sheaves.tex` — 871-876; number.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L874) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

A set contains morphisms, requiring the plural count noun.

Adverse evidence / qualification: The noun is not an adjunct here.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the set of morphism of sheaves
+the set of morphisms of sheaves
````

### MC-STK-ERR-0084

`sheaves.tex` — 1106-1127; substantive object misclassification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1127) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The hypotheses provide only a presheaf; allowed examples need not satisfy the sheaf axiom.

Adverse evidence / qualification: The intended object and stalk maps remain recoverable.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the corresponding maps for the underlying sheaf of sets.
+the corresponding maps for the underlying presheaf of sets.
````

### MC-STK-ERR-0085

`sheaves.tex` — 1542-1546; grammar.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1544-L1545) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The presheaf contains all continuous functions; the singular count noun after 'of' is ungrammatical.

Adverse evidence / qualification: 'Function' can be an adjunct elsewhere, but not in this prepositional phrase.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 presheaf of continuous
-function
+functions
````

### MC-STK-ERR-0086

`sheaves.tex` — 1747-1753; subject-verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1750) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The singular subject 'Lemma ...' requires 'shows'.

Adverse evidence / qualification: None.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemma \ref{lemma-diagram-fibre-product} show that
+Lemma \ref{lemma-diagram-fibre-product} shows that
````

### MC-STK-ERR-0087

`sheaves.tex` — 1765-1769; missing article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1767) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

A singular predicative count noun requires an article.

Adverse evidence / qualification: Telegraphic headings do not govern this running prose.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is morphism of presheaves
+is a morphism of presheaves
````

### MC-STK-ERR-0088

`sheaves.tex` — 1847-1854; grammar/mathematical prose.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1851) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The target module is G viewed as an O-module by restriction of scalars; the original article and construction are defective.

Adverse evidence / qualification: The surrounding types make the intended scalar restriction recoverable.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(into the restriction of $\mathcal{G}$ to a $\mathcal{O}$-module)
+(where $\mathcal{G}$ is viewed as an $\mathcal{O}$-module by restriction of scalars)
````

### MC-STK-ERR-0089

`sheaves.tex` — 1949-1953; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1952) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The established object is a sheaf of O-modules.

Adverse evidence / qualification: 'Module sheaf' would be grammatical only in a different word order.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a sheaf $\mathcal{O}$-modules
+a sheaf of $\mathcal{O}$-modules
````

### MC-STK-ERR-0090

`sheaves.tex` — 2100-2105; missing quantifier/type binder.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2100-L2101) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

G(U) requires U open in Y, but the paragraph does not bind the newly switched U.

Adverse evidence / qualification: The type can be inferred from G(U), but inference does not quantify the free symbol.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-A small useful remark is that there exists
+A small useful remark is that for every open $U \subset Y$ there exists
 a canonical map $\mathcal{G}(U) \to f_p\mathcal{G}(f^{-1}(U))$,
````

### MC-STK-ERR-0091

`sheaves.tex` — 2116-2120; missing copula.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2118) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

After 'let', the predicate adjective requires 'be'.

Adverse evidence / qualification: Postpositive shorthand in a range does not license this finite construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Namely, let $U \subset X$ open.
+Namely, let $U \subset X$ be open.
````

### MC-STK-ERR-0092

`sheaves.tex` — 2264-2273; article/agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2272-L2273) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The singular head 'family' requires the definite article and singular verb.

Adverse evidence / qualification: The plural members a_V do not control agreement.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-if and only if corresponding family of maps $a_V$
-satisfy the condition
+if and only if the corresponding family of maps $a_V$
+satisfies the condition
````

### MC-STK-ERR-0093

`sheaves.tex` — 2298-2305; typographical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2303) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The map is a restriction map; 'restruction' is a typo.

Adverse evidence / qualification: None.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-restruction map
+restriction map
````

### MC-STK-ERR-0094

`sheaves.tex` — 2320,2380; article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2320-L2380) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The spoken symbol g begins with a consonant sound, so both occurrences require 'a'.

Adverse evidence / qualification: Article choice follows pronunciation rather than glyph shape.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an $g$-map
+a $g$-map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an $g$-map
+a $g$-map
````

### MC-STK-ERR-0095

`sheaves.tex` — 2435-2437; assignment notation/type.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2436) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The parallel object assignments require mapsto; a right arrow would assert a nonexistent morphism.

Adverse evidence / qualification: The word 'assignments' makes the intent recoverable but does not type the arrow.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{G} \to f_p\mathcal{G}$
+$\mathcal{G} \mapsto f_p\mathcal{G}$
````

### MC-STK-ERR-0096

`sheaves.tex` — 2455-2464; grammar/successive predicates.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2460-L2464) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The source gives one subject two uncoordinated finite predicates; the displayed composite already supplies its type.

Adverse evidence / qualification: The mathematical composite itself is correct.

````diff
--- original
+++ replacement
@@ -1,5 +1,4 @@
 then the corresponding map
-$\mathcal{G} \to f_*\mathcal{F}$ is the map
 $f_*\psi \circ i_\mathcal{G} :
 \mathcal{G} \to f_* f_p \mathcal{G} \to f_* \mathcal{F}$
 is also a map of abelian presheaves.
````

### MC-STK-ERR-0097

`sheaves.tex` — 2455-2476; substantive typing.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2474) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

f_*psi has source f_*f_pG; precomposition with the unit is required to land in Mor(G,f_*F).

Adverse evidence / qualification: The full construction earlier in the paragraph is correct, confining the defect to the summary.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\psi \mapsto f_*\psi$
+$\psi \mapsto f_*\psi \circ i_\mathcal{G}$
````

### MC-STK-ERR-0098

`sheaves.tex` — 2479-2483; substantive variance reversal.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2479-L2480) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

For f:X→Y, F is on X and f_*F is on Y; the source reverses both.

Adverse evidence / qualification: Surrounding formulas reveal the intended variance.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-If $\mathcal{F}$ is an abelian sheaf on $Y$, then $f_*\mathcal{F}$
-is an abelian sheaf on $X$.
+If $\mathcal{F}$ is an abelian sheaf on $X$, then $f_*\mathcal{F}$
+is an abelian sheaf on $Y$.
````

### MC-STK-ERR-0099

`sheaves.tex` — 2686-2690; punctuation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2688) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

A comma cannot separate the complete subject from its predicate.

Adverse evidence / qualification: A rhetorical pause does not license the comma.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the pullback and pushforward functors, is the setting
+the pullback and pushforward functors is the setting
````

### MC-STK-ERR-0100

`sheaves.tex` — 2708-2710; grammar.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2709) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Imperative 'Let' selects 'be', not finite 'is'.

Adverse evidence / qualification: The intended open subset is recoverable.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $V \subset Y$ is open.
+Let $V \subset Y$ be open.
````

### MC-STK-ERR-0101

`sheaves.tex` — 2741-2743; grammar.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2742) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Imperative 'Let' selects 'be', not finite 'is'.

Adverse evidence / qualification: The intended open subset is recoverable.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $U \subset X$ is open.
+Let $U \subset X$ be open.
````

### MC-STK-ERR-0102

`sheaves.tex` — 2802-2809; sentence-boundary punctuation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2806) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The display-final period makes the following lowercase citation phrase a fragment.

Adverse evidence / qualification: A lowercase continuation would be valid only without the earlier terminator.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_{\textit{PAb}(Y)}(\mathcal{G}, f_*\mathcal{F}).
+\Mor_{\textit{PAb}(Y)}(\mathcal{G}, f_*\mathcal{F})
````

### MC-STK-ERR-0103

`sheaves.tex` — 2835-2838,2871-2873; substantive object misclassification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2873) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The lemma assumes presheaves and all Hom sets are in PMod; allowed inputs need not be sheaves.

Adverse evidence / qualification: The equality is correct; only the object class is wrong.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of abelian sheaves which is $f_*\mathcal{O}$-linear.
+of abelian presheaves which is $f_*\mathcal{O}$-linear.
````

### MC-STK-ERR-0104

`sheaves.tex` — 2952-2962; sentence fragment/reference number.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2960-L2961) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Lowercase 'where' follows a completed display, and plural 'Lemmas' introduces one reference.

Adverse evidence / qualification: Attaching the clause by removing the display period is possible but less local to the defective phrase.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-where the second is
-Lemmas \ref{lemma-adjoint-push-pull-presheaves-modules}
+The second equality is
+Lemma \ref{lemma-adjoint-push-pull-presheaves-modules}
````

### MC-STK-ERR-0105

`sheaves.tex` — 2986-2998; sentence fragment.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L2996) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Lowercase 'which' starts a fragment after a completed display.

Adverse evidence / qualification: Deleting the display period would be an alternate repair.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-which are a combination of
+These equalities are a combination of
````

### MC-STK-ERR-0106

`sheaves.tex` — 3122-3128; grammar/typed module construction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3123-L3128) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The second conjunct lacks a governing verb; parallel clauses must identify the underlying sheaf and restricted scalar structure.

Adverse evidence / qualification: The intended construction is recoverable from the cited lemma and ring map.

````diff
--- original
+++ replacement
@@ -1,6 +1,6 @@
-sheaf of $\mathcal{O}_Y$-modules which as a sheaf
-of abelian groups equals $f_*\mathcal{F}$ and with
-module structure given by the restriction
+sheaf of $\mathcal{O}_Y$-modules whose underlying sheaf
+of abelian groups is $f_*\mathcal{F}$ and whose
+module structure is obtained by restriction of scalars
 via $f^\sharp : \mathcal{O}_Y \to f_*\mathcal{O}_X$
-of the module structure given
+from the module structure given
 in Lemma \ref{lemma-pushforward-module}.
````

### MC-STK-ERR-0107

`sheaves.tex` — 3206-3211; grammar/coordination.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3206-L3209) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Three governed hypotheses require parallel coordination; the third is otherwise unattached.

Adverse evidence / qualification: The mathematical types remain clear.

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Given a morphism of ringed spaces
 $(f, f^\sharp) : (X, \mathcal{O}_X) \to (Y, \mathcal{O}_Y)$,
-and a sheaf of $\mathcal{O}_X$-modules $\mathcal{F}$,
+a sheaf of $\mathcal{O}_X$-modules $\mathcal{F}$, and
 a sheaf of $\mathcal{O}_Y$-modules $\mathcal{G}$ on $Y$,
````

### MC-STK-ERR-0108

`sheaves.tex` — 3230-3236; punctuation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3233) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The comma must close the introductory data before the main subject, not split its two-item coordination.

Adverse evidence / qualification: The display and following verb reveal the boundary.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as above, and $x \in X$ the induced map on stalks
+as above and $x \in X$, the induced map on stalks
````

### MC-STK-ERR-0109

`sheaves.tex` — 3273-3278; missing complement marker.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3276) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The notation-setting clause requires 'Let ... be ...' or 'denote ... by'.

Adverse evidence / qualification: The compressed house usage is recoverable but not standard grammar.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $i_x : \{x\} \to X$ the inclusion map.
+Let $i_x : \{x\} \to X$ be the inclusion map.
````

### MC-STK-ERR-0110

`sheaves.tex` — 3331-3335; missing copula.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3333) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The predicate nominative after 'let' requires 'be'.

Adverse evidence / qualification: Compact apposition elsewhere does not cure this finite directive.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-let $x \in X$ a point.
+let $x \in X$ be a point.
````

### MC-STK-ERR-0111

`sheaves.tex` — 3341-3343; missing conjunction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3342) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

A two-item list requires a coordinator.

Adverse evidence / qualification: Punctuation makes the intent recoverable.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-abelian groups, algebraic structures.
+abelian groups and algebraic structures.
````

### MC-STK-ERR-0112

`sheaves.tex` — 3511-3521; substantive free index.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3513) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof reindexes the chosen finite cover by 1,…,m, but later quantifies j,j' over undefined J.

Adverse evidence / qualification: The generic J in the lemma statement suggests the intended identification but does not define it after reindexing.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-quasi-compact for all $j, j' \in J$ and
+quasi-compact for all $1 \leq j, j' \leq m$ and
````

### MC-STK-ERR-0113

`sheaves.tex` — 3582-3584,3587-3591; number/agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3582-L3589) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Two sections have two images; plural 'are different' requires plural 'images'.

Adverse evidence / qualification: Ellipsis cannot make the overt singular head agree with the plural verb.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-the image of
+the images of
 $s$ and $s'$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the image of $s$ and $s'$
+the images of $s$ and $s'$
````

### MC-STK-ERR-0114

`sheaves.tex` — 3587-3592; substantive composition typing.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3591) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

For a:j→i and b:k→j, only a∘b is composable; b∘a is undefined.

Adverse evidence / qualification: The preceding correct formula reveals the intended order.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(f_{b \circ a}^{-1}\mathcal{G})_{p_k(x)}
+(f_{a \circ b}^{-1}\mathcal{G})_{p_k(x)}
````

### MC-STK-ERR-0115

`sheaves.tex` — 3606-3608; missing copula/number.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3607) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The coordinated plural subject needs 'are' and plural 'opens'.

Adverse evidence / qualification: 'Quasi-compact open' is a valid singular noun phrase, not for two named subsets.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we may assume $L$ is finite and $W_l$ and $V_{l, i}$ quasi-compact open
+we may assume $L$ is finite and $W_l$ and $V_{l, i}$ are quasi-compact opens
````

### MC-STK-ERR-0116

`sheaves.tex` — 3615-3618; missing complement marker.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3615) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Notation-setting 'write symbol for expression' requires 'for'.

Adverse evidence / qualification: The intended definition is unambiguous but grammatically incomplete.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Write $s_{l, j}$ the restriction
+Write $s_{l, j}$ for the restriction
````

### MC-STK-ERR-0117

`sheaves.tex` — 3705-3707; missing conjunction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3705-L3706) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Two complete axiomatic predicates run together without punctuation or conjunction.

Adverse evidence / qualification: A line break is not grammatical coordination.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-$\rho^U_U = \text{id}_{\mathcal{F}(U)}$ for all $U \in \mathcal{B}$
+$\rho^U_U = \text{id}_{\mathcal{F}(U)}$ for all $U \in \mathcal{B}$ and
 whenever $W \subset V \subset U$ in $\mathcal{B}$ we have
````

### MC-STK-ERR-0118

`sheaves.tex` — 3718-3725; colimit/directed-system terminology.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3723-L3725) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The display is a colimit and directedness belongs to the neighbourhood index system.

Adverse evidence / qualification: 'Direct limit' is older terminology, but the source says neither that nor predicates directedness correctly.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-As in the case of the stalk of a presheaf on $X$ this limit is
-directed. The reason is that the collection of $U\in \mathcal{B}$,
-$x \in U$ is a fundamental system of open neighbourhoods of $x$.
+As in the case of the stalk of a presheaf on $X$, this is a
+directed colimit. The reason is that the collection of $U\in \mathcal{B}$,
+$x \in U$ is a directed fundamental system of open neighbourhoods of $x$.
````

### MC-STK-ERR-0119

`sheaves.tex` — 3916-3920; substantive undefined restrictions.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3919) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Equality of germs supplies a basis neighbourhood contained in U_i∩U_j; without this containment the displayed restrictions are untyped.

Adverse evidence / qualification: The missing containment is inferable from the stalk equivalence relation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$y \in V_{ijy}$ such that
+$y \in V_{ijy} \subset U_i \cap U_j$ such that
````

### MC-STK-ERR-0120

`sheaves.tex` — 3982-3985,4121-4125,4241-4244; typographical/grammar.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3983-L4242) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Singular 'The inverse functor' requires passive 'is given'; 'in given' has no verb.

Adverse evidence / qualification: None.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The inverse functor in given
+The inverse functor is given
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The inverse functor in given
+The inverse functor is given
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The inverse functor in given
+The inverse functor is given
````

### MC-STK-ERR-0121

`sheaves.tex` — 4043-4046; subject-verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4044-L4045) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Singular subject 'The analogue' requires 'needs'.

Adverse evidence / qualification: The cited lemma lies in an of-phrase and does not pluralize the subject.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 The analogue of
-Lemma \ref{lemma-extend-off-basis} need some care.
+Lemma \ref{lemma-extend-off-basis} needs some care.
````

### MC-STK-ERR-0122

`sheaves.tex` — 4087-4090; wrong local condition label.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4090) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The underlying-set construction above is defined by condition (*), while (**) labels the sheaf gluing axiom.

Adverse evidence / qualification: The extension eventually satisfies (**), but that is not the definition being referenced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sets is the same as the definition using $(**)$ above.
+sets is the same as the definition using $(*)$ above.
````

### MC-STK-ERR-0123

`sheaves.tex` — 4255-4256,4322-4323; defined technical phrase.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4256-L4323) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The defined pair is 'a type of algebraic structure' in the singular.

Adverse evidence / qualification: Generic prose could pluralize structures, but these loci invoke the defined term.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a type of algebraic structures
+a type of algebraic structure
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a type of algebraic structures
+a type of algebraic structure
````

### MC-STK-ERR-0124

`sheaves.tex` — 4349-4353; grammar.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4351) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

'Let us' selects the bare infinitive 'prove'.

Adverse evidence / qualification: None.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let us first proves this
+Let us first prove this
````

### MC-STK-ERR-0125

`sheaves.tex` — 4352-4358; substantive component-domain error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4352) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

phi_V^U exists only for V in the basis; the proof evaluates it before extending components to arbitrary opens.

Adverse evidence / qualification: The later return to V in the basis confirms the intended range.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Fix $V \subset Y$ open.
+Fix $V \in \mathcal{B}_Y$.
````

### MC-STK-ERR-0126

`sheaves.tex` — 4375-4380; substantive map-kind/variance error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4379) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The constructed cross-space object is an f-map, not an ordinary same-space sheaf morphism.

Adverse evidence / qualification: 'Map' can be used generically, but the omitted f changes the Hom type.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the map of sheaves of sets so constructed
+the $f$-map of sheaves of sets so constructed
````

### MC-STK-ERR-0127

`sheaves.tex` — 4387-4390; number/agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4389-L4390) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Plural maps on stalks require plural verb and complement.

Adverse evidence / qualification: Singularizing the schematic construction would be a larger alternative.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-the maps on stalks is a morphism of algebraic
+the maps on stalks are morphisms of algebraic
 structures.
````

### MC-STK-ERR-0128

`sheaves.tex` — 4434-4437; sentence fragment.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4436) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof note lacks both subject and finite copula.

Adverse evidence / qualification: Terse proof-note shorthand is intelligible but the written sentence is incomplete.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Similar to the above and omitted.
+The proof is similar to the one above and is omitted.
````

### MC-STK-ERR-0129

`sheaves.tex` — 4464-4468; substantive parenthesization/type.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4467) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The intended object is the stalk of the restricted sheaf; the unparenthesized parse applies j^{-1} to a stalk.

Adverse evidence / qualification: The sentence makes intent recoverable, but the competing standard parse is ill-typed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j^{-1}\mathcal{G}_u
+(j^{-1}\mathcal{G})_u
````

### MC-STK-ERR-0130

`sheaves.tex` — 4469-4470,4577-4578,4715-4718; base-space preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4469-L4717) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Presheaves and sheaves are on a space; 'of' denotes the value type.

Adverse evidence / qualification: Surrounding categories reveal U as the base but do not license the preposition.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-On the category of presheaves of $U$
+On the category of presheaves on $U$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-On the category of sheaves of $U$
+On the category of sheaves on $U$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-On the category of presheaves of $U$
+On the category of presheaves on $U$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-On the category of sheaves of $U$
+On the category of sheaves on $U$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-On the category of abelian presheaves of $U$
+On the category of abelian presheaves on $U$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-On the category of abelian sheaves of $U$
+On the category of abelian sheaves on $U$
````

### MC-STK-ERR-0131

`sheaves.tex` — 4477-4479; missing definite article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4478) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The particular singular collection requires 'the'.

Adverse evidence / qualification: Bare plurals are possible; the source uses a singular count noun.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is over collection of all $W \subset X$ open
+is over the collection of all $W \subset X$ open
````

### MC-STK-ERR-0132

`sheaves.tex` — 4486-4487; substantive presheaf/sheaf functor mismatch.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4486-L4487) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Part (4) concerns presheaf inverse image j_p, while part (5) concerns sheaf inverse image j^{-1}; one sheaf calculation cannot type both.

Adverse evidence / qualification: Parallel section values make the proof idea recoverable.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-Parts (4) and (5) follow by computing
-$j^{-1}j_*\mathcal{F}(V) = j_*\mathcal{F}(V) = \mathcal{F}(V)$.
+Part (4) follows by computing
+$j_pj_*\mathcal{F}(V) = j_*\mathcal{F}(V) = \mathcal{F}(V)$,
+and part (5) follows from the same computation with $j^{-1}$.
````

### MC-STK-ERR-0133

`sheaves.tex` — 4501-4505; coordination/object-kind list.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4503-L4504) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Moving 'on X' after all value kinds restores parallel typing.

Adverse evidence / qualification: Ellipsis makes intent recoverable but the existing modifier attachment is ambiguous.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Let $\mathcal{G}$ be a sheaf of sets on $X$, abelian groups or
+Let $\mathcal{G}$ be a sheaf of sets, abelian groups, or
 algebraic structures on $X$.
````

### MC-STK-ERR-0134

`sheaves.tex` — 4566-4570,4705-4708,4749-4752,4796-4799,4905-4908; substantive parenthesization/type.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4569-L4907) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Each expression is the stalk of j_!F; the bare parse applies j_! to a stalk and can be undefined outside U.

Adverse evidence / qualification: Expert precedence can recover intent, but the alternate visible parse is untypeable.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j_{!}\mathcal{F}_x
+(j_{!}\mathcal{F})_x
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j_{!}\mathcal{F}_x
+(j_{!}\mathcal{F})_x
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j_{!}\mathcal{F}_x
+(j_{!}\mathcal{F})_x
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j_{!}\mathcal{F}_x
+(j_{!}\mathcal{F})_x
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j_!\mathcal{F}_x
+(j_!\mathcal{F})_x
````

### MC-STK-ERR-0135

`sheaves.tex` — 4594-4595; presheaf/sheaf object-kind conflation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4595) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The paired calculations concern one presheaf and one sheaf, so 'the sheaf' is false in the presheaf case.

Adverse evidence / qualification: The section formula is shared, making the proof idea correct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-value of the sheaf on any open of $U$.
+value of the relevant (pre)sheaf on any open of $U$.
````

### MC-STK-ERR-0136

`sheaves.tex` — 4599-4601,4605-4606; punctuation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4600-L4606) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

A comma cannot separate either full subject from its verb.

Adverse evidence / qualification: Long subjects may invite a spoken pause but not this grammatical comma.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 $j_!\mathcal{F}$ as
-defined above, is not a sheaf
+defined above is not a sheaf
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-extension by the empty set, is that it is the initial object
+extension by the empty set is that it is the initial object
````

### MC-STK-ERR-0137

`sheaves.tex` — 4648-4651; typographical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4650) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The attributive modifier must be the participle 'given'.

Adverse evidence / qualification: None.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(of the give type)
+(of the given type)
````

### MC-STK-ERR-0138

`sheaves.tex` — 4673-4676; semantic-label typesetting.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4675) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Bare word subscripts are products of italic variables rather than semantic labels.

Adverse evidence / qualification: Readers can infer the labels visually, but the math subscripts remain malformed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j_{!, rings}\mathcal{O} \not = j_{!, abelian}\mathcal{O}$
+$j_{!, \mathrm{rings}}\mathcal{O} \not = j_{!, \mathrm{abelian}}\mathcal{O}$
````

### MC-STK-ERR-0139

`sheaves.tex` — 4731-4734; number/established phrase.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4733) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The established object-kind phrase is '(pre)sheaves of algebraic structures'.

Adverse evidence / qualification: The singular is correct only in 'a type of algebraic structure', a different head.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(pre)sheaves of algebraic structure
+(pre)sheaves of algebraic structures
````

### MC-STK-ERR-0140

`sheaves.tex` — 4773-4806; substantive module-ring mismatch.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4794) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

On U the acting ring is O restricted to U, as the surrounding categories repeatedly state.

Adverse evidence / qualification: Restriction bars are sometimes suppressed, but not in this local statement family.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $\mathcal{F}$ be a sheaf of $\mathcal{O}$-modules on $U$.
+Let $\mathcal{F}$ be a sheaf of $\mathcal{O}|_U$-modules on $U$.
````

### MC-STK-ERR-0141

`sheaves.tex` — 4835-4838; wrong part of speech.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4837) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The nominal property is 'full faithfulness'.

Adverse evidence / qualification: 'Fully faithful' remains correct in the adjacent adjectival predicate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Fully faithfulness
+Full faithfulness
````

### MC-STK-ERR-0142

`sheaves.tex` — 4940-4947,5041-5046; substantive parenthesization/type.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4942-L5045) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The intended object is the stalk of i_*F; the unparenthesized parse applies i_* to a stalk and is ill-typed.

Adverse evidence / qualification: Expert precedence can recover intent, but the standard alternate parse is impossible.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i_*\mathcal{F}_x
+(i_*\mathcal{F})_x
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i_*\mathcal{F}_x
+(i_*\mathcal{F})_x
````

### MC-STK-ERR-0143

`sheaves.tex` — 4990-4993; wrong part of speech.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4991) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The nominal property is 'full faithfulness'; 'fully' is adverbial.

Adverse evidence / qualification: 'Fully faithful' is correct only in an adjectival predicate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Fully faithfulness
+Full faithfulness
````

### MC-STK-ERR-0144

`sheaves.tex` — 5123-5135; substantive undefined/ill-typed section.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L5134) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

s_V is undefined and phi_V requires an element of F(V), namely s restricted to V.

Adverse evidence / qualification: The file consistently uses s|_V and no local definition licenses s_V.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\varphi_V(s_{V})|_{V \cap U_i}
+\varphi_V(s|_V)|_{V \cap U_i}
````

### MC-STK-ERR-0145

`sheaves.tex` — 5136-5140; missing article/linking syntax.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L5138) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The singular count phrase 'open subset' lacks a determiner or copula.

Adverse evidence / qualification: Postpositive 'U open' shorthand does not license adding bare 'subset'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-since given $U \subset X$ open subset
+since given an open subset $U \subset X$
````

### MC-STK-ERR-0146

`sheaves.tex` — 5186-5189,5191-5197,5233-5238,5252-5259; terminology/number.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L5188-L5256) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

One gluing object is a datum; the source repeatedly combines singular articles/quantifiers with plural 'data'.

Adverse evidence / qualification: Modern mass-noun use cannot license explicit 'a data'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a {\it glueing data for sheaves of sets
+a {\it glueing datum for sheaves of sets
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Given any glueing data $(\mathcal{F}_i, \varphi_{ij})$
+Given any glueing datum $(\mathcal{F}_i, \varphi_{ij})$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of a glueing data
+of a glueing datum
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be a glueing data
+be a glueing datum
````

### MC-STK-ERR-0147

`sheaves.tex` — 5224-5228; spurious article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L5225-L5226) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

After 'by', the gerund directly introduces the means; 'the' has no head.

Adverse evidence / qualification: None.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-are defined by the restricting
+are defined by restricting
 each of the $s_i$
````

### MC-STK-ERR-1742

`sheaves.tex` — 535, 537; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L535-L537) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

The singular noun collection takes forms. Replace the final relative construction by the category in which the sheaf takes values, preserving the empty-cover explanation.

Adverse evidence / qualification: The sentence remains understandable in its original form. This is a grammatical correction, not a new assertion about final objects or elements of an arbitrary category.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-actually form
+actually forms
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of the category the sheaf has values in.
+of the category in which the sheaf takes values.
````

### MC-STK-ERR-1743

`sheaves.tex` — 841; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L841) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

Close the parenthetical indexing phrase with a comma, preserving the family of discrete spaces and the counterexample.

Adverse evidence / qualification: The original sentence is understandable. This punctuation repair makes no claim about changing the discrete/product-topology argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for $i \in \mathbf{N}$ be
+for $i \in \mathbf{N}$, be
````

### MC-STK-ERR-1744

`sheaves.tex` — 926; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L926) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

Insert by before the notation s_x so the sentence correctly relates the germ symbol to its represented equivalence class.

Adverse evidence / qualification: The mathematical definition and equivalence relation are already explicit. This is an English repair only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we sometimes denote
+we sometimes denote by
````

### MC-STK-ERR-1745

`sheaves.tex` — 1025; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1025) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

Use the singular verb determines with the head noun pair. The two functions represent the same germ exactly when they agree near x, as already defined.

Adverse evidence / qualification: Plural agreement may be understood by focusing on the two functions; the replacement is editorial and leaves the mathematical criterion intact.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-functions $f$, $g$ determine
+functions $f$, $g$ determines
````

### MC-STK-ERR-1746

`sheaves.tex` — 1277, 1278; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1277-L1278) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

Let P=A times_B C with projections p_A and p_C. Since F preserves fibre products, F(p_A) identifies with the projection from pairs (a,c) satisfying F(f)(a)=F(g)(c). The image inclusion gives a c for every a, and injectivity of F(g) makes it unique. Thus F(p_A) is bijective, so reflection of isomorphisms makes p_A invertible. Setting t=p_C composed with p_A inverse gives g composed with t=f by the fibre-product identity. Name this exact isomorphism and factorization explicitly.

Adverse evidence / qualification: The equality signs can already denote these canonical identifications; the report does not refute the factorization theorem. This is a clarification of the morphisms used in the proof, not a new theorem or counterexample.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence $A = A \times_B C$ because $F$ reflects isomorphisms.
+Hence the projection $A \times_B C \to A$ is invertible, since $F$ reflects isomorphisms.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The result follows.
+Follow its inverse by the projection to $C$ to obtain $t$ with $g \circ t = f$.
````

### MC-STK-ERR-1747

`sheaves.tex` — 1419; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1419) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

Capitalize the first word of the lemma statement.

Adverse evidence / qualification: No hypothesis or assertion changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-let $X$ be a topological space.
+Let $X$ be a topological space.
````

### MC-STK-ERR-1748

`sheaves.tex` — 1447; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1447) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

End the final proof sentence with a period after the Example reference.

Adverse evidence / qualification: The proof and reference are already complete; this is punctuation only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-see also Example \ref{example-application-lemma-image-contained-in}
+see also Example \ref{example-application-lemma-image-contained-in}.
````

### MC-STK-ERR-1749

`sheaves.tex` — 1492; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1492) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

For the fixed inclusion V subset U the display is one projection map. Use the singular noun map with the existing singular verb maps.

Adverse evidence / qualification: Alternatively a plural rewrite could use the verb map. The singular repair is smaller and preserves the displayed restriction morphism.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the projection maps
+the projection map
````

### MC-STK-ERR-1750

`sheaves.tex` — 1544; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1544) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

Remove the redundant as why construction and write for the same reason that.

Adverse evidence / qualification: The analogy and reference remain unchanged; this does not provide a new proof of sheafification.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for the same reason as why
+for the same reason that
````

### MC-STK-ERR-1751

`sheaves.tex` — 1807; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L1807) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

The parenthetical adverb however needs its opening comma as well as its existing closing comma.

Adverse evidence / qualification: The sheafification construction remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The main idea however, is
+The main idea, however, is
````

### MC-STK-ERR-1752

`sheaves.tex` — 3972, 4109, 4229; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L3972-L4229) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

All three category-naming clauses lack by after Denote. Inserting it preserves the categories, value types and restriction functors.

Adverse evidence / qualification: These are wording repairs, not changes to the equivalences of categories.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\Sh(\mathcal{B})$
+Denote by $\Sh(\mathcal{B})$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\Sh(\mathcal{B}, \mathcal{C})$
+Denote by $\Sh(\mathcal{B}, \mathcal{C})$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\textit{Mod}(\mathcal{O}|_\mathcal{B})$
+Denote by $\textit{Mod}(\mathcal{O}|_\mathcal{B})$
````

### MC-STK-ERR-1753

`sheaves.tex` — 4518-4519; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sheaves.tex#L4518-L4519) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r54/candidate.manifest.json)

Item (4) already specifies the restricted module presheaf, its restricted scalar action and its name. Remove the immediately following claim that this definition is left to the reader.

Adverse evidence / qualification: Do not invent an additional module case to justify the stale sentence. The next sentence begins the left-adjoint discussion and remains in place.

````diff
--- original
+++ replacement
@@ -1,2 +0,0 @@
-We leave a definition of the restriction of presheaves
-of modules to the reader. 
````
