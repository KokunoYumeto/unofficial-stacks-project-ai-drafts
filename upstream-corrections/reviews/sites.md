# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## sites

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/sites.patch)

### MC-STK-ERR-0148

`sites.tex` — 253-270; undefined category identifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L267) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof defines G'(U) for U in Ob(C), using plain C. The ambient category is mathcal C throughout the lemma and plain C is undefined; line 302 uses Ob(mathcal C) in the same chapter. Independent disposition: canon/control/private/R4_SITES_010_012_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Ob(C)
+\Ob(\mathcal{C})
````

### MC-STK-ERR-0149

`sites.tex` — 1248-1278; index binding type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L1273) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The induced morphism f_{jj'} has target U_{alpha(i)} x_U U_{alpha(i')}, although i and i' are not bound in this sentence. The map alpha has domain J; f_{jj'} is induced by f_j and f_{j'}, and the next two formulas use U_{alpha(j)} x_U U_{alpha(j')}. Independent disposition: canon/control/private/R4_SITES_010_012_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The preceding dummy i,i' do not rescue the target because alpha has domain J and f_j,f_j' force alpha(j),alpha(j').

````diff
--- original
+++ replacement
@@ -1 +1 @@
-U_{\alpha(i)} \times_U U_{\alpha(i')}
+U_{\alpha(j)} \times_U U_{\alpha(j')}
````

### MC-STK-ERR-0150

`sites.tex` — 1692-1703; transposed index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L1702) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof defines sections s_{j,i} and s_{j,i'} but then invokes s_{i,j} and s_{i',j}. The latter index order was never defined and reverses the established covering-index/system-index convention. Independent disposition: canon/control/private/R4_SITES_029_033_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$s_{i, j}$ and $s_{i', j}$
+$s_{j, i}$ and $s_{j, i'}$
````

### MC-STK-ERR-0151

`sites.tex` — 1966-1971; quantifier preposition error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L1970) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The definition says 'for all coverings of {U_i -> U}'. The displayed family itself is the covering; the extra preposition makes the quantification ungrammatical. Independent disposition: canon/control/private/R4_SITES_029_033_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $\{U_i \rightarrow U\}$
+$\{U_i \rightarrow U\}$
````

### MC-STK-ERR-0152

`sites.tex` — 2005-2010; colimit map direction error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2009) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof says s and s' map to the same element of H^0 of the refined covering. Here s,s' are elements of F^+(U), and the construction shows instead that they are images of the same H^0 element; no map F^+(U)->H^0 is defined. Independent disposition: canon/control/private/R4_SITES_029_033_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: No canonical map from the colimit back to a chosen H^0 representative exists; the construction sends one common representative forward.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$s, s'$ map to the same element of
+$s, s'$ are the images of the same element of
````

### MC-STK-ERR-0153

`sites.tex` — 2034-2038; domain type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2037) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sheaf property is stated as bijectivity of a map F -> H^0(U,F). For a covering of U the domain is the set of sections F(U), not the presheaf F. Independent disposition: canon/control/private/R4_SITES_029_033_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{F} \to H^0
+$\mathcal{F}(U) \to H^0
````

### MC-STK-ERR-0154

`sites.tex` — 2146-2151; functor notation error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2149) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The text calls F -> F^+ a functor commuting with finite limits. An arrow denotes one component/natural morphism, whereas the functor is the assignment F maps to F^+. Independent disposition: canon/control/private/R4_SITES_029_033_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The arrow may denote a natural transformation, but a transformation is not the endofunctor asserted to preserve finite limits.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{F} \to \mathcal{F}^+$
+$\mathcal{F} \mapsto \mathcal{F}^+$
````

### MC-STK-ERR-0155

`sites.tex` — 2166-2201; ambient category identifier error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2200) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The covering {U_{ijk} -> U_i x_U U_j} at line 2200 is said to be of site D. The lemma defines only site C; the cited lemma states the identical covering is of C at line 2168. Independent disposition: canon/control/private/R4_SITES_010_012_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Other lemmas may use D, but D is unbound in this lemma and the cited covering clause explicitly lies in C.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $\mathcal{D}$
+of $\mathcal{C}$
````

### MC-STK-ERR-0156

`sites.tex` — 2212-2223; proof circularity error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2221) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof says the pullbacks of t_i and t_j agree because 'we have the agreement for t_i and t_j'. This is circular: agreement of the t-sections is the conclusion; the known agreement is for their images s_i and s_j, and bijectivity over U_{ijk} then lifts it uniquely. Independent disposition: canon/control/private/R4_SITES_013_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: No earlier agreement of the t-sections exists; that agreement is exactly the conclusion, while agreement of their images s_i,s_j is known.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for $t_i$ and $t_j$
+for $s_i$ and $s_j$
````

### MC-STK-ERR-0157

`sites.tex` — 2580-2582; sentence fragment.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2580-L2581) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The lemma begins with the sentence fragment 'In the situation of Lemma ... .'. The prepositional phrase is punctuated as a complete sentence and is disconnected from 'The functor ...'. Independent disposition: canon/control/private/R4_SITES_001_004_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: A source-wide habit of such fragments does not turn this running-prose prepositional phrase into a clause; it has no heading markup or predicate.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-\ref{lemma-pushforward-sheaf}.
-The functor
+\ref{lemma-pushforward-sheaf}, the functor
````

### MC-STK-ERR-0158

`sites.tex` — 2595-2597; sentence fragment.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2595-L2596) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The lemma repeats the sentence fragment 'In the situation of Lemma ... .'. As at lines 2580-2582 the prepositional phrase is not a complete sentence. Independent disposition: canon/control/private/R4_SITES_001_004_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The repeated house-style fragment remains grammatically incomplete; no heading markup or predicate supplies an adverse reading.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-\ref{lemma-pushforward-sheaf}.
-For any presheaf
+\ref{lemma-pushforward-sheaf}, for any presheaf
````

### MC-STK-ERR-0159

`sites.tex` — 2832-2834; typography spacing error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2833) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

There is a space before the comma in '\\mathcal{D}$ , and'. The punctuation spacing is inconsistent with the rest of the source. Independent disposition: canon/control/private/R4_SITES_001_004_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The whitespace can be visually subtle under TeX, but there is no grammatical reason for interword space before the comma.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathcal{D}$ , and
+$\mathcal{D}$, and
````

### MC-STK-ERR-0160

`sites.tex` — 3354-3360; section typing grammar error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3357) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence says that id_U 'lifts to a section of s_c of h_{U_{iota(c)}}^#'. The next sentence defines s_c as the section; 'of s_c' makes s_c an object possessing a section and is grammatically and mathematically inconsistent. Independent disposition: canon/control/private/R4_SITES_005_009_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Reading s_c as an object that has a section fails because s_c is introduced only in the next sentence as the lifted section itself.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $s_c$ of
+$s_c$ of
````

### MC-STK-ERR-0161

`sites.tex` — 3405; spelling error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3405) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence begins 'Finite copoducts of sheaves'. The standard categorical noun is 'coproducts'. Independent disposition: canon/control/private/R4_SITES_005_009_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-copoducts
+coproducts
````

### MC-STK-ERR-0162

`sites.tex` — 3460-3474; typed transition argument error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3472-L3474) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

After introducing sections s and s' and assuming phi_{ii_a}(s)=phi_{i'i_a}(s'), the conclusion twice uses phi_{i'i''}(s). The second transition morphism has source F_{i'} and must act on s'; using s is ill-typed unless i=i', which is not assumed. Independent disposition: canon/control/private/R4_SITES_005_009_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: No equality i=i', transition, or coercion places s in the domain of the second transition map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\varphi_{i'i''}(s)
+\varphi_{i'i''}(s')
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\varphi_{i'i''}(s)
+\varphi_{i'i''}(s')
````

### MC-STK-ERR-0163

`sites.tex` — 3622-3628; duplicated auxiliary grammar error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3626) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof says 'This is done shown in the next paragraph'. The doubled auxiliary is ungrammatical. Independent disposition: canon/control/private/R4_SITES_005_009_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-This is done shown
+This is shown
````

### MC-STK-ERR-0164

`sites.tex` — 3738-3744; preposition typo.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3741) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof says 'Since the cardinality if I x I'. The preposition is a typographical error. Independent disposition: canon/control/private/R4_SITES_005_009_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cardinality if
+cardinality of
````

### MC-STK-ERR-0165

`sites.tex` — 3883-3886; duplicated article error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3884) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof says 'we can pick a a : j -> i'. The indefinite article is duplicated. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-pick a $a : j \to i$
+pick $a : j \to i$
````

### MC-STK-ERR-0166

`sites.tex` — 3883-3889; object domain type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3885) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The representative V_j is declared to lie in Ob(mathcal C). The notation V_j and the equation V=u_j(V_j), with u_j:mathcal C_j->mathcal C, require V_j to be an object of mathcal C_j. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Ob(\mathcal{C})
+\Ob(\mathcal{C}_j)
````

### MC-STK-ERR-0167

`sites.tex` — 3888-3896; bound index variance error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3891-L3896) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The independence sentence refers to the choice of b:j->i although the representative was chosen with a:j->i; the next sentence again chooses b:j->i and then applies u_b to a morphism in C_j. In the displayed colimit b has type k->j, so u_b acts on C_j; an arrow b:j->i instead gives u_b:C_i->C_j and cannot act on alpha_j in C_j. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Renaming a dummy variable cannot repair the printed form without separately binding b:k->j for the restriction family.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $b : j \to i$
+of $a : j \to i$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-choose $b : j \to i$
+choose $a : j \to i$
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-along the morphisms $u_b(\alpha_j) : u_b(V_j) \to u_b(V'_j)$. A check
+along the morphisms $u_b(\alpha_j) : u_b(V_j) \to u_b(V'_j)$ for
+$b : k \to j$. A check
````

### MC-STK-ERR-0168

`sites.tex` — 3898-3907; ill typed composition error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3905-L3906) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Both colimit terms use f_{b o a}^{-1} for a:j->i and b:k->j. The composition b o a is ill-typed; the Situation fixes c=a o b, and the defining formula at line 3888 correctly uses f_{a o b}^{-1}. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-f_{b \circ a}^{-1}
+f_{a \circ b}^{-1}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-f_{b \circ a}^{-1}
+f_{a \circ b}^{-1}
````

### MC-STK-ERR-0169

`sites.tex` — 3933-3947; identity notation error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3940-L3947) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The identity-indexed map is written varphi_id twice after being defined as varphi_{text{id},text{id},V_i}. Plain id is typeset as a product of variables and does not match the established identity index text{id} in the same paragraph. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended identity component is inferable, but bare id is not the established text-form identity symbol and renders as math letters.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\varphi_{id}
+\varphi_{\text{id}}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\varphi_{id}
+\varphi_{\text{id}}
````

### MC-STK-ERR-0170

`sites.tex` — 3954-3961; subject verb agreement error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3957) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence has plural subject 'the functors f_a^{-1}' with singular verb 'commutes'. Standard subject-verb agreement requires 'commute'. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-functors $f_a^{-1}$ commutes
+functors $f_a^{-1}$ commute
````

### MC-STK-ERR-0171

`sites.tex` — 3967-3994; sheaf domain error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3987) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The formal colimit at line 3987 evaluates F_i on u_a(X_i). For a:j->i, u_a(X_i) lies in C_j, so F_i on C_i cannot be evaluated there; the lemma statement at line 3980 correctly uses F_j(u_a(X_i)). Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{F}_i(u_a(X_i))
+\mathcal{F}_j(u_a(X_i))
````

### MC-STK-ERR-0172

`sites.tex` — 4011-4025; composition domain error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4022) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The cocycle check takes a:j->i and b:k->i while declaring c=a o b. The composition a o b is defined only when b:k->j, as in the preceding colimit lemma and the governing Situation. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$b : k \to i$
+$b : k \to j$
````

### MC-STK-ERR-0173

`sites.tex` — 3967-4045; undefined index category error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4028-L4040) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Three colimits at lines 4028, 4035 and 4040 are indexed by i in I, but the only index category defined in the Situation is mathcal I and no I is introduced here. Earlier quantified indices use i in Ob(mathcal I); plain I is undefined in this construction. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim_{i \in I}
+\colim_{i \in \Ob(\mathcal{I})}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim_{i \in I}
+\colim_{i \in \Ob(\mathcal{I})}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim_{i \in I}
+\colim_{i \in \Ob(\mathcal{I})}
````

### MC-STK-ERR-0174

`sites.tex` — 3997-4045; omitted functor and undefined sheaf error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4035-L4040) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof twice writes colim f_i^{-1}F_i although no sheaves F_i are defined in this lemma. The lemma statement is F=colim f_i^{-1}f_{i,*}F and the next line evaluates f_{j,*}F; the dropped direct-image factor changes the object and leaves F_i undefined. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-f_i^{-1}\mathcal{F}_i
+f_i^{-1}f_{i, *}\mathcal{F}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-f_i^{-1}\mathcal{F}_i
+f_i^{-1}f_{i, *}\mathcal{F}
````

### MC-STK-ERR-0175

`sites.tex` — 4383-4391; sentence fragment.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4388-L4389) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The lemma opens with the standalone fragment 'In the situation of Lemma ... .'. The prepositional phrase is not a complete sentence and is disconnected from the following quantifier. Independent disposition: canon/control/private/R4_SITES_014_024_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Parallel source fragments establish repetition, not grammatical completeness; the quantifier is the missing main clause.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-\ref{lemma-exact-cocontinuous}.
-For any presheaf
+\ref{lemma-exact-cocontinuous}, for any presheaf
````

### MC-STK-ERR-0176

`sites.tex` — 4477-4483; ambient object target error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4479) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The family {E_i -> v(u(U))} is called a covering of U in E. U is an object of C, while the displayed family has target v(u(U)), which is the object of E covered by the family. Independent disposition: canon/control/private/R4_SITES_025_028_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Even if categories shared an underlying object, no identity U=v(u(U)) is declared and the displayed family has target v(u(U)).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a covering of $U$ in $\mathcal{E}$
+a covering of $v(u(U))$ in $\mathcal{E}$
````

### MC-STK-ERR-0177

`sites.tex` — 4797-4804; duplicate subject error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4801) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The question reads 'shouldn't any covering of U cap Z it come'. The pronoun 'it' is an extraneous duplicate subject. Independent disposition: canon/control/private/R4_SITES_025_028_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-it come
+come
````

### MC-STK-ERR-0178

`sites.tex` — 4933-4937; unbound index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4935) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The image covering {v(V_j) -> v(u(U))} is indexed by i in I. The source covering on the preceding line is indexed by j in J; i and I are unbound in this proof. Independent disposition: canon/control/private/R4_SITES_025_028_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-_{i \in I}
+_{j \in J}
````

### MC-STK-ERR-0179

`sites.tex` — 4953-4957; terminology spelling error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L4956) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The adjective is spelled 'cocontinous'. The defined term throughout the chapter is 'cocontinuous'. Independent disposition: canon/control/private/R4_SITES_025_028_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cocontinous
+cocontinuous
````

### MC-STK-ERR-0180

`sites.tex` — 5358-5363; missing copula error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L5360) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence reads 'where j_{U!}^{PSh} G the presheaf defined by the formula'. The copula is missing, leaving an ungrammatical and incomplete definition. Independent disposition: canon/control/private/R4_SITES_034_039_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j_{U!}^{PSh}\mathcal{G}$ the presheaf
+$j_{U!}^{PSh}\mathcal{G}$ is the presheaf
````

### MC-STK-ERR-0181

`sites.tex` — 5383-5387; duplicated copula error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L5385) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence reads 'The value of the presheaf ... is on X is'. The first 'is' is misplaced/duplicated. Independent disposition: canon/control/private/R4_SITES_034_039_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j_{U!}^{PSh}\mathcal{F}_\varphi$ is
+$j_{U!}^{PSh}\mathcal{F}_\varphi$
````

### MC-STK-ERR-0182

`sites.tex` — 5468-5472;5553-5557; reversed localization indices error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L5555) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The relocalization functor is defined as j_{V/U}: C/V -> C/U, but the later inverse-image description writes j^{-1}=j_{U/V}^{-1}. The latter reverses the established source/target indices and names a different, undefined relocalization in this context. Independent disposition: canon/control/private/R4_SITES_034_039_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Bare j lets a reader guess the intended functor, but the asserted indexed equality names the opposite, wrong-direction localization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j_{U/V}^{-1}
+j_{V/U}^{-1}
````

### MC-STK-ERR-0183

`sites.tex` — 5597-5602; paired adjunction grammar error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L5600) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence says two functors 'which are right, left adjoint' to j_U^{-1}. The paired order needs an explicit distributive marker; as written it is ungrammatical. Independent disposition: canon/control/private/R4_SITES_034_039_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Experts can infer the pairwise assignment from order, but inference does not repair the under-coordinated English clause.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-which are right, left adjoint
+which are respectively right and left adjoint
````

### MC-STK-ERR-0184

`sites.tex` — 5979-5984; missing copula error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L5983) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The construction says 'where restriction along f ... given by'. The copula is missing from the definition. Independent disposition: canon/control/private/R4_SITES_043_047_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-along $f : V \to U$ given by
+along $f : V \to U$ is given by
````

### MC-STK-ERR-0185

`sites.tex` — 6069-6074; comma splice error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6072) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The declaration 'Let (s_i,varphi_i)...' ends with a comma before a new sentence beginning 'This means'. The comma creates a sentence-boundary punctuation error. Independent disposition: canon/control/private/R4_SITES_043_047_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The close relation between the two clauses permits a semicolon, but not the printed comma before a capitalized independent sentence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\prod_i \mathcal{H}(V_i)$,
+\prod_i \mathcal{H}(V_i)$.
````

### MC-STK-ERR-0186

`sites.tex` — 6072-6083; composition order type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6077-L6083) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The restrictions to V_i times_V V_j use pr_1 composed with varphi_i and pr_2 composed with varphi_j, and the compatibility equality repeats those orders. Here pr_1 has codomain V_i and varphi_i has domain V_i, so only varphi_i composed with pr_1 is typed; similarly for j. The displayed source compositions are undefined under the stated convention. Independent disposition: canon/control/private/R4_SITES_040_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: A reversed composition convention is ruled out by the same file's typed p circ psi = varphi example.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{pr}_1 \circ \varphi_i
+\varphi_i \circ \text{pr}_1
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{pr}_2 \circ \varphi_j
+\varphi_j \circ \text{pr}_2
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{pr}_1 \circ \varphi_i
+\varphi_i \circ \text{pr}_1
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{pr}_2 \circ \varphi_j
+\varphi_j \circ \text{pr}_2
````

### MC-STK-ERR-0187

`sites.tex` — 6168-6174; malformed nominalization error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6172) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof uses the phrase 'equivalent to the fully faithfulness'. The standard noun phrase is 'full faithfulness'. Independent disposition: canon/control/private/R4_SITES_043_047_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the fully faithfulness
+the full faithfulness
````

### MC-STK-ERR-0188

`sites.tex` — 6536-6545; undefined object name error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6543) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The functor u':C/U -> D/V sends U'/U to V'/V, but V' is not defined. The commutative square requires the underlying object to be u(U'), and the proof at lines 6562-6575 constructs exactly u(U')/V. Independent disposition: canon/control/private/R4_SITES_043_047_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$U'/U \mapsto V'/V$
+$U'/U \mapsto u(U')/V$
````

### MC-STK-ERR-0189

`sites.tex` — 6562-6571; wrong base object error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6569) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The morphisms phi_i:u(U_i')->V_{alpha(i)} are called morphisms over U'. Both objects lie in D and their displayed structure maps target u(U'); U' lies in C and cannot be their base in D. Independent disposition: canon/control/private/R4_SITES_043_047_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-over $U'$
+over $u(U')$
````

### MC-STK-ERR-0190

`sites.tex` — 6768-6772; citation expose error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6771) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The citation attributes SGA 4 Proposition 4.9.4 to Expose III. The native French SGA 4 Expose IV facsimile places Proposition 4.9.4 in Expose IV (Topos), page 356. Independent disposition: canon/control/private/R4_SITES_057_064_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: A loose citation reading is defeated by the primary SGA 4 text and a later same-file citation, both locating Proposition 4.9.4 in Expose IV.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Expos\'e III
+Expos\'e IV
````

### MC-STK-ERR-0191

`sites.tex` — 6818-6867; distinguished component index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6866) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The constructed limit element is said to satisfy s_{(U,psi)}=s. The category's final object and the prescribed distinguished component are explicitly (U,id) at lines 6821-6825; psi is not the distinguished arrow here. Independent disposition: canon/control/private/R4_SITES_057_064_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Generic psi does not index the distinguished final object; even U with a nonidentity endomorphism is a different component.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$s_{(U, \psi)} = s$
+$s_{(U, \text{id})} = s$
````

### MC-STK-ERR-0192

`sites.tex` — 6953-6968; ill typed composition error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6966) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The final equality says u(c_{ik})=c composed with u(f_{ik}). Here f_{ik}:U''_{ik}->U''_i while c has domain u(U''); these maps are not composable. Since c_{ik}=c_i composed with f_{ik} and u(c_i)=c composed with u(f_i), the covering composite f_i composed with f_{ik} is required. Independent disposition: canon/control/private/R4_SITES_057_064_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-u(f_{ik})
+u(f_i \circ f_{ik})
````

### MC-STK-ERR-0193

`sites.tex` — 7011-7016; extraneous verb grammar error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7013) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The warning says statements 'may look be a bit confusing'. The verb 'be' is extraneous after 'look'. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-may look be a bit confusing
+may look a bit confusing
````

### MC-STK-ERR-0194

`sites.tex` — 7115-7126; inductive sequence index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7119) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The displayed increasing sequence repeats C_2: C_1 subset C_2 subset C_2 subset ... The inductive definition immediately below defines C_{n+1}; the third term of the illustrative sequence is C_3. Independent disposition: canon/control/private/R4_SITES_057_064_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The repeated C_2 can denote a redundant inclusion only by defeating the displayed enumeration and the immediately stated recurrence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{C}_2 \subset \mathcal{C}_2
+\mathcal{C}_2 \subset \mathcal{C}_3
````

### MC-STK-ERR-0195

`sites.tex` — 7209-7221; sheaf category operator notation error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7213-L7219) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Four Hom subscripts use Sh(...) without the established control sequence. The sheaf-category notation throughout is the macro Sh, and the unescaped letters render as a product of variables rather than the category symbol. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Readers can infer Sh, but bare math letters are not TeX-equivalent to the defined sheaf-category operator and differ from 531 local macro uses.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_{Sh
+\Mor_{\Sh
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_{Sh
+\Mor_{\Sh
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_{Sh
+\Mor_{\Sh
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_{Sh
+\Mor_{\Sh
````

### MC-STK-ERR-0196

`sites.tex` — 7240-7247; number agreement error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7244) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The prose says 'Lemmas' but cites a single lemma-topos-good-site reference. Only one lemma is invoked at this step. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemmas
+Lemma
````

### MC-STK-ERR-0197

`sites.tex` — 7376-7381; missing relative marker error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7379) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence says the functor 'is the one associates to' an arrow a sheaf. The relative clause lacks 'that'. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is the one associates to
+is the one that associates to
````

### MC-STK-ERR-0198

`sites.tex` — 7652-7673; unbound localization object error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7658-L7659) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

After defining F=h_{u(V)}, the localization diagram suddenly uses C/U and j_U although U is not defined in the lemma. The intended localization object is u(V); the subsequent comparison also identifies j_F with the representable localization at that object. Independent disposition: canon/control/private/R4_SITES_057_064_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: A variable local to the cited lemma is not bound in this proof; the uniquely intended object is u(V).

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
 Lemma \ref{lemma-pullback-representable-sheaf}.
+Set $U = u(V)$.
 By
````

### MC-STK-ERR-0199

`sites.tex` — 7693-7702; number agreement error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7699) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof contrasts a singular choice of morphism of sites with 'the morphisms of sites given to us in the lemma'. The lemma supplies one morphism, and the next sentence compares two choices using 'both cases'. Independent disposition: canon/control/private/R4_SITES_073_075_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-morphisms of sites given to us
+morphism of sites given to us
````

### MC-STK-ERR-0200

`sites.tex` — 7706-7727; slice codomain type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7725) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The localized morphism f' is typed with codomain Sh(D)/F. F is a sheaf on C, not D; the preceding square and lemma-localize-morphism-topoi give codomain Sh(D)/G. Independent disposition: canon/control/private/R4_SITES_057_064_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Sh(\mathcal{D})/\mathcal{F}
+\Sh(\mathcal{D})/\mathcal{G}
````

### MC-STK-ERR-0201

`sites.tex` — 7788-7795; false representable equality error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7793) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

For an arbitrary morphism c:U->u(V), the source states h_U^#=f^{-1}h_V^#. In general f^{-1}h_V^#=h_{u(V)}^#, while h_U^# maps to it via c and need not equal it; the next line correctly defines that induced map. Independent disposition: canon/control/private/R4_SITES_057_064_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: An arbitrary map c induces a map of representables, not an equality; the arrow-category counterexample in the independent review defeats identification.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
- = f^{-1}h_V^\#
````

### MC-STK-ERR-0202

`sites.tex` — 7926-7936; colimit element noun error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7930) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

Two representatives of an element of (h_U)_p are said to determine the same object. The proof is comparing elements of the colimit, as stated at lines 7927 and 7935. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Object can be generic prose, but here it conflicts with the technical indexing-category sense while the colimit definition explicitly says element.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-determine the same object
+determine the same element
````

### MC-STK-ERR-0203

`sites.tex` — 7926-7936; equivalence relation terminology error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7933) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The equivalence relation is said to require 'chains of identities like this'. The preceding relation is induced by morphisms and identifications, not by identity maps. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Identity can loosely mean equality, but the generating relation uses arbitrary morphisms; identifications is the exact equivalence-closure term.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-chains of identities like this
+chains of identifications like this
````

### MC-STK-ERR-0204

`sites.tex` — 7957-7962; sentence fragment.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7959-L7960) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The lemma statement ends 'For any functor ... Sets.' and starts a new fragment 'The functor...'. The introductory phrase must be joined to its predicate. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The phrase is not marked as a heading; the following sentence supplies precisely its missing predicate.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-\textit{Sets}$.
-The functor
+\textit{Sets}$, the functor
````

### MC-STK-ERR-0205

`sites.tex` — 8022-8028; missing predicative link error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8025) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The definition reads 'we define p_*E=u^sE the sheaf described'. The predicative construction lacks 'to be'. Independent disposition: canon/control/private/R4_SITES_065_072_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: A comma could suggest an appositive, but its attachment to an equality is ambiguous; to be is the smallest unambiguous defining link.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$p_*E = u^sE$ the sheaf
+$p_*E = u^sE$ to be the sheaf
````

### MC-STK-ERR-0206

`sites.tex` — 8042-8048; subject verb agreement error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8047) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The singular subject 'the pair of functors' takes the plural verb 'define'. The grammatical subject is 'pair'. Independent disposition: canon/control/private/R4_SITES_073_075_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-above define a morphism
+above defines a morphism
````

### MC-STK-ERR-0207

`sites.tex` — 8198-8223; false coequalizer preservation claim.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8204-L8222) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The lemma claims p_* commutes with arbitrary coequalizers and says this follows from p_*E(U)=Map(u(U),E). For a fixed set S, Map(S,-) is a right adjoint and need not preserve coequalizers. With a coarsest-topology category having Hom(0,1) of size two, evaluation at 0 is a valid point and p_* at 1 is (-)^2; the coequalizer of the two maps {*}=>{0,1} becomes a singleton before squaring but has three classes after applying (-)^2. Independent disposition: canon/control/private/R4_SITES_073_075_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Right-adjoint status proves limit preservation, not arbitrary coequalizer preservation; the independently replayed two-arrow chaotic-site example yields three coequalizer classes after p_* versus one before it.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
-it commutes with coequalizers, 
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 transforms
-surjections into surjections and coequalizers into coequalizers.
+surjections into surjections.
````

### MC-STK-ERR-0208

`sites.tex` — 8276-8281; duplicated article error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8278) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The conclusion begins 'Then the the category'. The article is accidentally duplicated. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then the the category
+Then the category
````

### MC-STK-ERR-0209

`sites.tex` — 8382-8403; number agreement error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8397) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The functor is said to commute with 'product and fibred products'. The criterion is preservation of finite limits; in this setting the intended pair is the final object/product and fibre products, and the singular bare 'product' is incomplete English. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Bare singular product can name an operation informally, but the exact parallel point example says products and fibred products.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-commutes with product and fibred products
+commutes with products and fibred products
````

### MC-STK-ERR-0210

`sites.tex` — 8490-8500; wrong condition number error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8497) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

After conditions (1) and (2) are checked, the exactness condition is again called Condition (2). Exactness of the stalk functor is condition (3) of Definition definition-point at lines 7901-7902. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Condition (2) holds
+Condition (3) holds
````

### MC-STK-ERR-0211

`sites.tex` — 8490-8500; topology name error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8498) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The example assumes the chaotic topology but the final sentence calls it discrete. Example example-indiscrete at lines 820-825 defines the same isomorphism-only coverings as the chaotic or indiscrete topology; discrete is the opposite extreme terminology used separately later. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Terminology varies externally, but this file explicitly defines the topology as chaotic or indiscrete and opens this example with chaotic.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the topology is discrete
+the topology is chaotic
````

### MC-STK-ERR-0212

`sites.tex` — 8580-8588; missing predicate error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8585) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The explanation begins 'The first equality since f^{-1}=u_s'. The predicate is missing. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended reading remains recoverable and TeX may still compile, but recoverability does not supply the missing, duplicated, or malformed token; the bound independent review found the correction forced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The first equality since
+The first equality holds since
````

### MC-STK-ERR-0213

`sites.tex` — 8616-8621; unmatched delimiter error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8618) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The display has i_*E(v(u(U)) with one missing closing parenthesis before the equality to Mor. The identical construction at line 8157 reads i_*E(u(U)) = Mor(u(U),E); here the argument is v(u(U)). Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The later Hom-expression parenthesis closes a different expression after an equality sign and cannot balance i_*E evaluation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i_*E(v(u(U)) =
+i_*E(v(u(U))) =
````

### MC-STK-ERR-0214

`sites.tex` — 8620-8625; malformed formula reference prose error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8623) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The sentence reads 'this is the same as the formula for which is equal to (v composed u)^pE'. The object after 'formula for' is missing and 'which is equal to' has no antecedent; the displayed Hom formula is precisely the formula for (v composed u)^pE. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Inserting a new antecedent could repair the sentence, but is larger and less directly supported than binding formula for to the named functor.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
-which is equal to 
````

### MC-STK-ERR-0215

`sites.tex` — 8625-8634; wrong point subscript error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8629) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The functor right-adjoint to g_*i_* is called the stalk functor F maps to F_q. Here g and i construct the new point p of C; q is the original point of D, so F on C has stalk F_p, not F_q. The following sentence also names p^{-1}. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: The intended expression may be recoverable from context, but no local declaration, coercion, or convention makes the printed source exact; the bound independent review found no defeating adverse construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{F}_q
+\mathcal{F}_p
````

### MC-STK-ERR-0216

`sites.tex` — 8795-8809; undefined localization morphism error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8805) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r4/candidate.manifest.json)

The proof uses q^{-1} composed with j^{-1}=p^{-1}. The localization morphism throughout the lemma is j_U; no unindexed j is defined here. Independent disposition: canon/control/private/R4_SITES_048_056_INDEPENDENT_REVIEW.md.

Adverse evidence / qualification: Bare j can be guessed as j_U, but the abbreviation is never declared and every surrounding formula retains U.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-j^{-1}
+j_U^{-1}
````

### MC-STK-ERR-0217

`sites.tex` — sites.tex:6513; malformed fibre-product base subscript.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6513) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Line 6515 identifies h_{u(V')}^# as the fibre-product base and c' as its structure map.

Adverse evidence / qualification: The printed subscript places c' inside the representable and is not the typed base-map pair used by the adjacent analogue.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\times_{h_{u(V'), c'}^\#}
+\times_{h_{u(V')}^\#, c'}
````

### MC-STK-ERR-0218

`sites.tex` — sites.tex:6821-6822; false final-object assertion.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6821) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The indexing objects allow arbitrary psi:u(U')->u(U), which need not be u(alpha); the proof uses only the indexed object (U,id).

Adverse evidence / qualification: Without a lift of every psi, (U,id) need not receive the unique morphisms required of a final object.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-has a final
+has an
````

### MC-STK-ERR-0219

`sites.tex` — sites.tex:7054; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7054) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

English names a morphism with the construction 'denote by'.

Adverse evidence / qualification: The printed 'Denote g ... the equivalence' is grammatically incomplete.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $g
+Denote by $g
````

### MC-STK-ERR-0220

`sites.tex` — sites.tex:9140; sentence-initial capitalization.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9140) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The lemma sentence begins at this token.

Adverse evidence / qualification: Lowercase 'let' remains a sentence-initial copy defect.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-let $\{(p_i, u_i)\}
+Let $\{(p_i, u_i)\}
````

### MC-STK-ERR-0221

`sites.tex` — sites.tex:9224; missing predicate.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9224) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The explanatory clause requires 'holds' before 'since'.

Adverse evidence / qualification: The printed fragment has a subject and causal clause but no predicate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The first equality since
+The first equality holds since
````

### MC-STK-ERR-0222

`sites.tex` — sites.tex:9316,9324,9418; plural agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9316-L9418) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Each locus compares two distinct sections/elements and therefore has plural images.

Adverse evidence / qualification: Correcting only one of the three identical constructions would leave the same number-agreement defect twice.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-distinct image
+distinct images
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-distinct image
+distinct images
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-distinct image
+distinct images
````

### MC-STK-ERR-0223

`sites.tex` — sites.tex:9349; wrong transition-map symbol.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9349) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The refinement is introduced and used with transition maps f_{ii'}.

Adverse evidence / qualification: The printed g_{ii'} belongs to the old system and contradicts the new tuple displayed on the same line.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-g_{ii'}
+f_{ii'}
````

### MC-STK-ERR-0224

`sites.tex` — sites.tex:9443; missing sheafification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9443) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The coproduct is asserted in Sh(C); the exact sheafified analogue occurs at line 9170.

Adverse evidence / qualification: A representable h_{U_i} need not itself be a sheaf on a general site.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\coprod h_{U_i}
+\coprod h_{U_i}^\#
````

### MC-STK-ERR-0225

`sites.tex` — sites.tex:9533; dropped mathematical qualifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9533) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Only weakly contractible objects are defined and used in this section.

Adverse evidence / qualification: The unqualified phrase asserts the stronger, undefined property 'contractible objects'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-enough contractible objects
+enough weakly contractible objects
````

### MC-STK-ERR-0226

`sites.tex` — sites.tex:9841; singular predicate complement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9841) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The subject alpha is one morphism.

Adverse evidence / qualification: The printed plural 'maps' disagrees with the singular typed subject.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be maps of sheaves
+be a map of sheaves
````

### MC-STK-ERR-0227

`sites.tex` — sites.tex:9864-9866; malformed site description.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9865) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The sentence defines the sites and then their covering families; 'with coverings the...' supplies the missing relation.

Adverse evidence / qualification: The printed coordination does not grammatically state which families are coverings.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and coverings countable families
+, with coverings the countable families
````

### MC-STK-ERR-0228

`sites.tex` — sites.tex:9949; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9949) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The lemma is applied to an argument.

Adverse evidence / qualification: The printed 'applied the empty covering' is not grammatical English.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-applied the empty covering
+applied to the empty covering
````

### MC-STK-ERR-0229

`sites.tex` — sites.tex:10015; missing covered object.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10015) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Every displayed arrow in the reduced family targets u(U).

Adverse evidence / qualification: The printed sentence ends 'covering of' without naming any object.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is still a covering of
+is still a covering of $u(U)$
````

### MC-STK-ERR-0230

`sites.tex` — sites.tex:10042; malformed Let declaration.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10042) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

After 'Let', the indexed assignment must be declared to be a diagram.

Adverse evidence / qualification: The printed 'by a diagram' leaves the declaration without a predicate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-by a diagram
+be a diagram
````

### MC-STK-ERR-0231

`sites.tex` — sites.tex:10057; case-inconsistent operator notation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10057) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Line 10046 defines the presheaf colimit notation as Psh and adjacent uses retain that spelling.

Adverse evidence / qualification: The isolated PSh spelling changes the established case-sensitive notation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim^{PSh}
+\colim^{Psh}
````

### MC-STK-ERR-0232

`sites.tex` — sites.tex:10285; number agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10285) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The source explicitly introduces two parallel morphisms a and b.

Adverse evidence / qualification: The singular noun after 'two' is a copy defect.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-two morphism of
+two morphisms of
````

### MC-STK-ERR-0233

`sites.tex` — sites.tex:10326; subject-verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10326) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The antecedent is the plural pair of pushforward and pullback functors.

Adverse evidence / qualification: The printed singular verb disagrees with the compound plural subject.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-which agrees
+which agree
````

### MC-STK-ERR-0234

`sites.tex` — sites.tex:10329; comma separating subject and predicate.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10329) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The full gerund phrase is the subject of 'works'.

Adverse evidence / qualification: The printed comma incorrectly separates that subject from its predicate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of a space, works
+of a space works
````

### MC-STK-ERR-0235

`sites.tex` — sites.tex:10384; lexical typo.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10384) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The infinitive construction is 'trying to define'.

Adverse evidence / qualification: The printed 'trying the define' is ungrammatical.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-trying the define
+trying to define
````

### MC-STK-ERR-0236

`sites.tex` — sites.tex:10462; corrupted French quotation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10462) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The quoted construction is 'espece de structure algebrique'.

Adverse evidence / qualification: The English article 'the' interrupts and corrupts the French phrase.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the structure
+de structure
````

### MC-STK-ERR-0237

`sites.tex` — sites.tex:10463; French adjective agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10463) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The adjective agrees with plural 'limites'.

Adverse evidence / qualification: Singular 'finie' disagrees with the plural noun.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-projectives finie
+projectives finies
````

### MC-STK-ERR-0238

`sites.tex` — sites.tex:10478-10479; duplicated direction syntax.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10479) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The displayed arrow already expresses the morphism's source and target.

Adverse evidence / qualification: Combining 'from' with an arrow yields the malformed 'from A -> B'.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-from $\Sh(\mathcal{D}) \to \Sh(\mathcal{C})$
+$\Sh(\mathcal{D}) \to \Sh(\mathcal{C})$
````

### MC-STK-ERR-0239

`sites.tex` — sites.tex:10545-10546; incomplete monoid-object datum and axioms.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10545-L10546) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

A monoid object requires multiplication, a unit, associativity, and unit axioms; the adjacent group and unital-ring data confirm this convention.

Adverse evidence / qualification: The printed pair with one unspecified axiom supplies at most a semigroup object and omits the unit datum.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a pair $(\mathcal{F}, \cdot)$
+a triple $(\mathcal{F}, \cdot, 1)$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-with suitable axiom.
+with suitable axioms.
````

### MC-STK-ERR-0240

`sites.tex` — sites.tex:10549; article agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10549) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The following noun begins with a consonant sound.

Adverse evidence / qualification: The printed article 'An' is ungrammatical.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-An sheaf
+A sheaf
````

### MC-STK-ERR-0241

`sites.tex` — sites.tex:10605-10606; subject-verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10606) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The grammatical subject is plural 'global sections'.

Adverse evidence / qualification: The singular verb disagrees with the printed subject.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is the set
+are the set
````

### MC-STK-ERR-0242

`sites.tex` — sites.tex:10622; object-morphism type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10622) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The declarations a,b:V->U and the coequalizer diagram require parallel morphisms.

Adverse evidence / qualification: Calling the typed arrows objects contradicts both their types and the following pullback maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be objects of
+be morphisms of
````

### MC-STK-ERR-0243

`sites.tex` — sites.tex:10761; wrong ringed-topos qualifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10761) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The diagram uses only ordinary topoi and f_*,g^{-1}; the parallel composition remark at line 10735 says topoi.

Adverse evidence / qualification: No structure sheaves or ringed morphisms occur in this base-change statement.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of ringed topoi
+of topoi
````

### MC-STK-ERR-0244

`sites.tex` — sites.tex:11272-11274; malformed and shadowed sieve definition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11273) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The preceding definition identifies the sieve generated by a covering family, which is exactly what must be contained in S.

Adverse evidence / qualification: The printed clause both shadows S and treats an unquantified image expression as the sieve.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such that $S$ the image of $h_{U_i} \to h_U$
+such that the sieve generated by the $f_i$
````

### MC-STK-ERR-0245

`sites.tex` — sites.tex:11276,11278; morphism-subobject type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11276-L11278) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

A morphism of representables contributes its image subpresheaf to a sieve.

Adverse evidence / qualification: The printed arrows are not literally subpresheaves and therefore cannot themselves be contained in a sieve.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$h_{U_{ij}} \to h_{U_i}$
+the image of $h_{U_{ij}} \to h_{U_i}$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$h_{U_{ij}} \to h_U$
+the image of $h_{U_{ij}} \to h_U$
````

### MC-STK-ERR-0246

`sites.tex` — sites.tex:11293; spelling error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11293) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The adverb is one word.

Adverse evidence / qualification: The printed split spelling is incorrect.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-In stead
+Instead
````

### MC-STK-ERR-0247

`sites.tex` — sites.tex:11299; undefined ambient category.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11299) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

T is an object of the ambient site C on which the sieve S is evaluated.

Adverse evidence / qualification: The printed mathcal U is undefined as a category in this proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$T \in \mathcal{U}$
+$T \in \mathcal{C}$
````

### MC-STK-ERR-0248

`sites.tex` — sites.tex:11303-11304; wrong factorization index.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11304) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The second chosen factorization is indexed by i' and must use f_{i'}.

Adverse evidence / qualification: Using f_i for both choices defeats and generally mistypes the comparison.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-= f_i \circ \alpha_{i'}'
+= f_{i'} \circ \alpha_{i'}'
````

### MC-STK-ERR-0249

`sites.tex` — sites.tex:11343-11351; coverage-versus-covering type error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11345) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Each Cov_k(C) is a set or system of covering families, as the surrounding definition and discussion state.

Adverse evidence / qualification: Calling each whole Cov_k(C) one covering confuses a coverage with an element of it.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be two coverings defining
+be two sets of coverings defining
````

### MC-STK-ERR-0250

`sites.tex` — sites.tex:11363; wrong object of enlargement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11363) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Adding covering families enlarges Cov(C), not the objects and morphisms of C.

Adverse evidence / qualification: The printed operation changes the category rather than its coverage.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-add to $\mathcal{C}$ any set of families
+add to $\text{Cov}(\mathcal{C})$ any set of families
````

### MC-STK-ERR-0251

`sites.tex` — sites.tex:11503; missing cross-reference command.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11503) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The exact label exists in categories.tex and line 524 uses the correct ref command for it.

Adverse evidence / qualification: Without ref, TeX prints the raw label key and creates no numbered cross-reference.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-{categories-lemma-functorial-colimit}
+\ref{categories-lemma-functorial-colimit}
````

### MC-STK-ERR-0252

`sites.tex` — sites.tex:11598; wrong representative codomain.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11598) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The representatives are maps into F, and equality after refinement must be established before applying L.

Adverse evidence / qualification: Equality in LF is already the assumption and cannot prove separatedness of the represented maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_{\textit{PSh}(\mathcal{C})}(S'', L\mathcal{F})
+\Mor_{\textit{PSh}(\mathcal{C})}(S'', \mathcal{F})
````

### MC-STK-ERR-0253

`sites.tex` — sites.tex:11606; wrong Hom category.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11606) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

Both S and LF are presheaves on C.

Adverse evidence / qualification: Mor_C is ill-typed because neither argument is an object of C.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Mor_\mathcal{C}(S, L\mathcal{F})
+\Mor_{\textit{PSh}(\mathcal{C})}(S, L\mathcal{F})
````

### MC-STK-ERR-0254

`sites.tex` — sites.tex:11626; missing text-math boundary space.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11626) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r5/candidate.manifest.json)

The prose word and following inline-math variable require a separating space.

Adverse evidence / qualification: The printed tokens concatenate in source and can render without the intended word boundary.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-choice$ V'
+choice $V'
````

### MC-STK-ERR-1754

`sites.tex` — 583; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L583) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Insert the missing possessive apostrophe and state that the two constructed maps are inverses. The map constructions and the adjunction statement remain unchanged.

Adverse evidence / qualification: The defect is grammatical; the existing proof already specifies maps in both directions. No new assertion or independent proof of the adjunction is claimed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-verify they are each others inverse.
+verify that they are each other's inverses.
````

### MC-STK-ERR-1755

`sites.tex` — 781; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L781) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Remove the singular article before the coordinated plural nouns presheaves and sheaves. Preserve the existing comparison and its reference.

Adverse evidence / qualification: The singular word notion can refer collectively to both kinds of object; changing it to notions is unnecessary.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a presheaves and sheaves
+presheaves and sheaves
````

### MC-STK-ERR-1756

`sites.tex` — 801; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L801) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Delete the first by in replace by G-Sets by a full subcategory, leaving the intended category replacement and both set-theoretic references intact.

Adverse evidence / qualification: No size convention, category, action or covering changes; the two by tokens are a grammatical duplication.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We first replace by
+We first replace
````

### MC-STK-ERR-1757

`sites.tex` — 1310; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L1310) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Use the plural categories as the subject of are equal, referring to the two sheaf categories in the preceding inclusions.

Adverse evidence / qualification: This agreement repair changes none of the covering conditions or inclusions.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the category of sheaves are equal.
+the categories of sheaves are equal.
````

### MC-STK-ERR-1758

`sites.tex` — 1333; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L1333) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Attach the refinement data to the chosen family with with the refinement given by, preserving alpha and every component f_j.

Adverse evidence / qualification: The argument is mathematically recoverable; this repairs the grammatical attachment of the already specified data.

````diff
--- original
+++ replacement
@@ -1 +1 @@
- and refinement given
+, with the refinement given
````

### MC-STK-ERR-1759

`sites.tex` — 1635, 2658, 2670; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L1635-L2670) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The definition makes H^0 an equalizer of sets for a set-valued presheaf and supplies no group operations. This cannot uniformly be a group: on the category with one object and its identity, use only the identity covering and let F take the empty set. Its restriction is the identity of the empty set; the sheaf condition for the identity covering holds, and H^0 of that covering is empty. A group must contain an identity element, so this H^0 is not a group. The identity functor of the same site gives the same counterexample at the quasi-continuous loci. Replace group/groups by set/sets in all three reported phrases.

Adverse evidence / qualification: Group-valued presheaves can give groups, but the stated hypotheses allow every set-valued presheaf, including this example. No equalizer, map, hypothesis or sheafification construction changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cohomology group
+cohomology set
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cohomology group
+cohomology set
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-groups.
+sets.
````

### MC-STK-ERR-1760

`sites.tex` — 3342; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3342) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Write v:V_c to U_alpha(c) for the refinement map. Applying sheafification to the induced map of representable presheaves gives h_Vc-sharp to h_Ualpha(c)-sharp. Since F_iota(alpha(c)) is a sheaf, the section s_alpha(c) corresponds by Yoneda and the sheafification adjunction to a unique map from h_Ualpha(c)-sharp to that sheaf. Composing these two maps and the given map to h_U-sharp corresponds to the restriction of the image of s_alpha(c), which is id_U restricted to V_c. By the same adjunction/Yoneda bijection this is exactly the map h_Vc-sharp to h_U-sharp induced by V_c to U. The added marker makes the displayed chain this actual chain of sheaf morphisms.

Adverse evidence / qualification: The site is arbitrary and is not assumed subcanonical, so the intermediate representable need not already be a sheaf. Its sheafification cannot be suppressed using a hypothesis absent from the lemma. The required representable-to-sheaf map extends uniquely to its sheafification; the asserted factorization remains the same.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h_{U_{\alpha(c)}}
+h_{U_{\alpha(c)}}^\#
````

### MC-STK-ERR-1761

`sites.tex` — 3939; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L3939) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The plural subject compatibilities takes imply, preserving the exact adjunction assertion and all of its indices.

Adverse evidence / qualification: This corrects agreement only; the family of maps and the argument determining it by the identity component are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-implies that
+imply that
````

### MC-STK-ERR-1762

`sites.tex` — 5362; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L5362) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

At X the presheaf extension of G is the disjoint union of G(X,a) over a:X to U. Applying that functor to G to the terminal presheaf sends (a,s) to (a,*), and its target is the disjoint union of singleton sets indexed by a, canonically h_U(X). This map is natural because restriction sends (a,s) to (a composed with b, G(b)(s)); on the target it sends a to a composed with b. Thus the named gamma factors through j_{U!}^{PSh}*, exactly as the following identification requires. Adding the PSh superscript supplies the actual intermediate object.

Adverse evidence / qualification: The sheaf extension j_{U!}* is h_U sheafified; on an arbitrary site this need not equal h_U. The proof is constructing a presheaf over h_U before sheafification, and no subcanonical assumption identifies those targets.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\to j_{U!}*
+\to j_{U!}^{PSh}*
````

### MC-STK-ERR-1763

`sites.tex` — 5844, 5942, 5980; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L5844-L5980) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Each singular article introduces one structured collection. Use datum for that single structure, retaining data for collections or the category of such structures. The nearby defining occurrence at 5942 has the same singular article an across the line break and is repaired in the same unit.

Adverse evidence / qualification: The operations change only the noun at the three singular-article occurrences read in context. The constituent sheaves, isomorphisms, cocycle conditions and category of absolute glueing data retain their names and definitions.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-glueing data
+glueing datum
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-glueing data
+glueing datum
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-glueing data
+glueing datum
````

### MC-STK-ERR-1764

`sites.tex` — 6047; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6047) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The coordinated objects of the hypotheses are the site and the object of localization. Moving the misplaced on yields on the site or on the object.

Adverse evidence / qualification: Neither hypothesis nor the logical or changes; the correction restores the order of the two prepositions.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-on the site on or the object
+on the site or on the object
````

### MC-STK-ERR-1765

`sites.tex` — 6155; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6155) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The subject contains two coordinated restrictions, so its verb is produce. The statement still discusses both the pushforward and extension by the empty set before giving the precise hypothesis below.

Adverse evidence / qualification: No claim that these two functors agree in general is introduced; the next sentence and lemma retain the required condition on U.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-produces back
+produce back
````

### MC-STK-ERR-1766

`sites.tex` — 6261; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L6261) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The introduction refers to the specific relation treated by the following lemma, so the singular count noun relation takes the article the.

Adverse evidence / qualification: The scope remains localization and morphisms of sites and topoi; the operation changes no definition.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-understand relation
+understand the relation
````

### MC-STK-ERR-1767

`sites.tex` — 7366; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L7366) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The imperative names the inverse equivalence a; Denote by a the inverse functor requires the preposition by, as at the earlier naming occurrence for g.

Adverse evidence / qualification: The directions of a and its inverse, and all three associated functors, remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-1768

`sites.tex` — 8351; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L8351) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The first condition names u(X)={*} and then describes it as a singleton. Inserting is completes that predicate while retaining the exact equality and all later conditions.

Adverse evidence / qualification: The remark is a counterexample under weakened fibre-product assumptions; no condition is strengthened by this verb insertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$u(X) = \{*\}$ a singleton
+$u(X) = \{*\}$ is a singleton
````

### MC-STK-ERR-1769

`sites.tex` — 9178; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9178) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The naming construction denotes the composite point by q_j. Inserting by after denote supplies the required preposition.

Adverse evidence / qualification: The composite remains the point on C obtained from p_j on C/U_i followed by localization; no index or arrow is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote
+denote by
````

### MC-STK-ERR-1770

`sites.tex` — 9265; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9265) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The grammatical subject each of the functors is singular, so its verb is does. The representable functors and filtered-colimit finite-limit argument are unchanged.

Adverse evidence / qualification: The correction does not change all finite limits representable in C to a different class of limits.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-do, see
+does, see
````

### MC-STK-ERR-1771

`sites.tex` — 9270; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9270) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The definition gives three simultaneous conditions, including the assertion that the ordering on J is induced from I. Inserting is completes that clause.

Adverse evidence / qualification: The inclusion of directed index sets and equality of restricted objects and transition maps remain exact.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the ordering on $J$ induced
+the ordering on $J$ is induced
````

### MC-STK-ERR-1772

`sites.tex` — 9303; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9303) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The supplied J-system has transition maps g_{j j_0}:V_j to V_{j_0}. With f prime:V_{j_0} to W, its pullback of W_k to V_j therefore uses f prime composed with g_{j j_0}. For j prime at least j, the transition g_{j prime j} induces the map between these pullbacks because g_{j j_0} composed with g_{j prime j}=g_{j prime j_0}; identities and compositions follow uniquely from the pullback property. This is the exact system used to take the subsequent colimits and construct the refinement.

Adverse evidence / qualification: The maps f_{ii prime} belong to the refinement still being constructed. They have not been supplied on J at this stage, whereas g is the actual transition system in the hypotheses.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-f_{j j_0}
+g_{j j_0}
````

### MC-STK-ERR-1773

`sites.tex` — 9355; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9355) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The naming imperative uses Denote by S the class of all pairs. Adding by repairs that construction without altering the ordered class or its elements.

Adverse evidence / qualification: This editorial operation makes no new claim concerning the size of that class or the Zorn argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\mathcal{S}$
+Denote by $\mathcal{S}$
````

### MC-STK-ERR-1774

`sites.tex` — 9699; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9699) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The clause introduces one surjective map of sheaves and needs the article a. The specified arrow and subsequent pullback square are unchanged.

Adverse evidence / qualification: No surjectivity assertion is added; the map was already assumed surjective.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be surjective map
+be a surjective map
````

### MC-STK-ERR-1775

`sites.tex` — 9974; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9974) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The concessive phrase while not exact on sheaves of sets interrupts the subject i_* and the main predicate is exact. Its existing closing comma needs the opening comma after i_*.

Adverse evidence / qualification: The statement continues to distinguish sheaves of sets from sheaves of abelian groups and retains the same cited example.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$i_*$ while
+$i_*$, while
````

### MC-STK-ERR-1776

`sites.tex` — 9216, 10046; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L9216-L10046) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Two additional naming clauses read while adjudicating the cited proof contexts use Denote [symbol] the [object] without by: the stalk notation at 9216 and presheaf-colimit notation at 10046. Insert the same preposition used in the other verified naming repairs. These two occurrences were found directly in primary-source reading and are not counted as received reports.

Adverse evidence / qualification: The operations leave all symbols, adjunctions, category labels and colimit formulas unchanged. The independent-discovery status must remain visible in the final intake accounting.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $p_i$
+Denote by $p_i$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\colim
+Denote by $\colim
````

### MC-STK-ERR-1777

`sites.tex` — 10558; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L10558) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Write Delta=(id,id):F to F times F. The two endomorphisms lambda_r and lambda_r prime induce their product lambda_r times lambda_r prime:F times F to F times F, and addition maps that product object to F. Hence the intended identity is lambda_{r+r prime}=addition composed with (lambda_r times lambda_r prime) composed with Delta; at each object it sends x to lambda_r(x)+lambda_r prime(x). Parenthesizing the product states this exact composition unambiguously.

Adverse evidence / qualification: The types already identify the intended interpretation. This is classified as clarification of grouping, not a new module law or a proof that the original intended formula was false.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-+ \circ \lambda_r \times \lambda_{r'} \circ
++ \circ (\lambda_r \times \lambda_{r'}) \circ
````

### MC-STK-ERR-1778

`sites.tex` — 11117; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11117) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The naming clause denotes the set of sieves by J(U). The insertion completes denote by J(U) the set while leaving its universal base-change condition unchanged.

Adverse evidence / qualification: The set J(U), every morphism V to U and every presheaf F_i keep their original quantifiers.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote
+denote by
````

### MC-STK-ERR-1779

`sites.tex` — 11484, 11574; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11484-L11574) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

Lemma sieves-set proves that an intersection is a sieve, without asserting that it is covering. Lemma topology-basic (1) proves finite intersections of covering sieves are covering: if alpha:V to U is in S(V), pulling back S intersect S prime along alpha gives the pullback of S prime, which covers V; transitivity then makes S intersect S prime cover U. This is exactly the fact needed both for the directed colimit at 11484 and the common representative sieve at 11574. Replace the two wrong references by this proved lemma; the latter matching occurrence was found directly during the source review.

Adverse evidence / qualification: The earlier reference to sieves-set at 11459 concerns partial ordering and is correct, so it is retained. The operation changes exactly two reference targets and must be an explicit exception to reference-key invariance in the replay checks.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{lemma-sieves-set}
+\ref{lemma-topology-basic}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{lemma-sieves-set}
+\ref{lemma-topology-basic}
````

### MC-STK-ERR-1780

`sites.tex` — 11636; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11636) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The naming clause denotes the common restriction by psi. Inserting by relates the named map to its symbol in the same way as the other naming repairs.

Adverse evidence / qualification: The common restriction and evaluation at id_T remain the same; the operation changes no covering sieve or representative.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote the common restriction $\psi$.
+Denote the common restriction by $\psi$.
````

### MC-STK-ERR-1781

`sites.tex` — 11763; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11763) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The lemma adopts the category and both topologies from the preceding theorem. Assumptions and notation are as in states that inherited setup as a complete clause and uses the plural for the collected hypotheses.

Adverse evidence / qualification: The reference and the inclusion criterion for J,J prime are untouched; no new topological condition is introduced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assumption and notation as in
+Assumptions and notation are as in
````

### MC-STK-ERR-1782

`sites.tex` — 11840; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L11840) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r55/candidate.manifest.json)

The second arrow describes the image of an object F under the stalk functor, so mapsto makes that assignment explicit. It matches the object-assignment arrow in the presheaf stalk display immediately above.

Adverse evidence / qualification: The functor and its exactness condition remain unchanged. The old to arrow is understandable as informal assignment notation; this is classified as notation clarification rather than a new map between F and its stalk.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathcal{F} \to \mathcal{F}_p
+\mathcal{F} \mapsto \mathcal{F}_p
````
