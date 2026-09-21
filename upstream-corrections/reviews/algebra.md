# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## algebra

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/algebra.patch)

### MC-STK-ERR-0621

`algebra.tex` — algebra.tex:28903-28906; subject verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28905) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. which exist -> which exists

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-exist by Lemma \ref{lemma-dominate}).
+exists by Lemma \ref{lemma-dominate}).
````

### MC-STK-ERR-0622

`algebra.tex` — algebra.tex:28934-28937; ambiguous relative clause chain.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28934-L28937) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_qualified. Recast condition (4) into coordinated predicates; comma insertion alone does not resolve attachment.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 \item there exists a finite ring map $R \to R'$ which is not
-an isomorphism whose kernel and cokernel are annihilated by a power
-of $\mathfrak m$ such that $\mathfrak m$ is not an associated
-prime of $R'$ and $R' \not = 0$.
+an isomorphism, has kernel and cokernel annihilated by a power of
+$\mathfrak m$, satisfies $\mathfrak m \notin \operatorname{Ass}(R')$,
+and has $R' \not = 0$.
````

### MC-STK-ERR-0623

`algebra.tex` — algebra.tex:28991-28994; wrong preposition for localization.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28992) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. in the generic point -> at the generic point

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in the generic point
+at the generic point
````

### MC-STK-ERR-0624

`algebra.tex` — algebra.tex:29098-29100; unfinished editorial placeholder.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29098-L29100) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Delete the literal future-reference placeholder and state the each-maximal-ideal completion condition directly.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,3 +1,2 @@
-On the other hand, if the completion of $R$ in all of its maximal
-ideals is reduced, then the procedure stops (insert future reference
-here).
+On the other hand, if the completion of $R$ at each of its maximal
+ideals is reduced, then the procedure stops.
````

### MC-STK-ERR-0625

`algebra.tex` — algebra.tex:29114-29116; missing exponent domain.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29116) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Add n in Z_{>=0}.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$u\pi^n$, where $u \in A$ is a unit.
+$u\pi^n$, where $u \in A$ is a unit and $n \in \mathbf{Z}_{\geq 0}$.
````

### MC-STK-ERR-0626

`algebra.tex` — algebra.tex:29192-29195; attributive noun error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29194) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. vectors space -> vector space

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as a vectors space
+as a vector space
````

### MC-STK-ERR-0627

`algebra.tex` — algebra.tex:29221-29225; missing relation in chain.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29224) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Insert the missing subset relation before N_k.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-0 \subset N_0 \subset N_1 \subset N_2 \subset \ldots N_k \subset M/xM
+0 \subset N_0 \subset N_1 \subset N_2 \subset \ldots \subset N_k \subset M/xM
````

### MC-STK-ERR-0628

`algebra.tex` — algebra.tex:29259-29263; subject verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29261) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. results ... implies -> results ... imply

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-structural results on Artinian rings implies parts (1) and (2)
+structural results on Artinian rings imply parts (1) and (2)
````

### MC-STK-ERR-0629

`algebra.tex` — algebra.tex:29311-29318; missing article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29316) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. there exists discrete valuation ring -> there exists a discrete valuation ring

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then there exists discrete valuation ring $A$ with fraction field
+Then there exists a discrete valuation ring $A$ with fraction field
````

### MC-STK-ERR-0630

`algebra.tex` — algebra.tex:29363-29364; prime element zero case.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29363-L29364) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_by_counterexample. Require a prime element to be nonzero.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-\item An element $x \in R$ is called {\it prime} if the ideal
+\item A nonzero element $x \in R$ is called {\it prime} if the ideal
 generated by $x$ is a prime ideal.
````

### MC-STK-ERR-0631

`algebra.tex` — algebra.tex:29377; undefined ring symbol.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29377) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. f,g in A -> f,g in R

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some $f, g \in A$.
+for some $f, g \in R$.
````

### MC-STK-ERR-0632

`algebra.tex` — algebra.tex:29374-29379; invalid zero cancellation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29378) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Handle x=0 before cancellation.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Then $x = fg x$ and since $R$ is a domain $fg = 1$. Thus
+If $x = 0$, then also $y = 0$, and the conclusion is immediate.
+Otherwise, $x = fg x$ and since $R$ is a domain $fg = 1$. Thus
````

### MC-STK-ERR-0633

`algebra.tex` — algebra.tex:29434-29442; missing zero factorization cases.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29435) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_qualified. Dispose of zero cases, then use empty factorizations for units.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-Say $ab \in (x)$, i.e., $ab = cx$. Choose factorizations
+Say $ab \in (x)$, i.e., $ab = cx$. If $a = 0$ or $b = 0$, the
+conclusion is immediate. Thus $a$, $b$, and $c$ are nonzero. Choose
+factorizations (allowing the empty product for a unit)
````

### MC-STK-ERR-0634

`algebra.tex` — algebra.tex:29448-29455; swapped factorization endpoints.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29453-L29455) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. a_2...a_n=u b_2...b_m -> a_2...a_m=u b_2...b_n

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,3 +1,4 @@
-and $a_2 \ldots a_n = ub_2\ldots b_m$. By induction on $n + m$
-we see that $n = m$ and $a_i$ associate to $b_{\sigma(i)}$ for
-$i = 2, \ldots, n$ as desired.
+and $a_2 \ldots a_m = ub_2\ldots b_n$. If $m = 1$ or $n = 1$,
+this equality forces $m = n = 1$. Otherwise, absorb $u$ into $b_2$
+and apply induction on $n + m$ to see that $n = m$ and $a_i$ is
+associate to $b_{\sigma(i)}$ for $i = 2, \ldots, n$, as desired.
````

### MC-STK-ERR-0635

`algebra.tex` — algebra.tex:29549-29553; missing initial zero ideal case.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29550) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Handle or truncate an initial zero-ideal segment before factoring a_1.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1,4 @@
-of principal ideals in $R$. Write $a_1 = p_1^{e_1} \ldots p_r^{e_r}$
+of principal ideals in $R$. If $a_n = 0$ for every $n$, there is
+nothing to prove. Otherwise, after dropping an initial segment and
+renumbering, we may assume $a_1 \not = 0$. Write
+$a_1 = p_1^{e_1} \ldots p_r^{e_r}$
````

### MC-STK-ERR-0636

`algebra.tex` — algebra.tex:29564-29574; missing initial zero polynomial case.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29565) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Handle or truncate an initial zero-polynomial segment before degrees are used.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-of principal ideals in $R[x]$. Since
+of principal ideals in $R[x]$. If $f_n = 0$ for every $n$, there is
+nothing to prove. Otherwise, after dropping an initial segment and
+renumbering, we may assume $f_1 \not = 0$. Since
````

### MC-STK-ERR-0637

`algebra.tex` — algebra.tex:29589-29593; overbroad factorization quantifiers.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29589-L29592) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Qualify both factorization assertions by nonzero nonunit.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-element of $R[x]$
+nonzero nonunit element of $R[x]$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-every nonunit of $R$
+every nonzero nonunit of $R$
````

### MC-STK-ERR-0638

`algebra.tex` — algebra.tex:29606-29610; missing zero integral element case.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29608) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Handle x=0 before the irreducible-power representation.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We can write
+If $x = 0$, there is nothing to prove. Thus we may assume $x \not = 0$ and write
````

### MC-STK-ERR-0639

`algebra.tex` — algebra.tex:29699-29704; false zero prime square claim.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29699) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_by_counterexample. Dispose of the zero prime, then take a nonzero prime.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak p \subset R$ be a prime ideal. Observe that
+$\mathfrak p \subset R$ be a nonzero prime ideal (the zero ideal is already finitely generated). Observe that
````

### MC-STK-ERR-0640

`algebra.tex` — algebra.tex:29727-29729; mismatched localization variable and scope.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29728) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Use R_m for every nonzero maximal ideal m.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-prime ideal $\mathfrak p$
+nonzero maximal ideal $\mathfrak m$
````

### MC-STK-ERR-0641

`algebra.tex` — algebra.tex:29735-29738; missing unit and zero ideal cases.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29735) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Treat I=R by the empty product, then take I nonzero and proper.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $I \subset R$ be an ideal.
+The unit ideal is the empty product. Let $I \subset R$ be a nonzero proper ideal.
````

### MC-STK-ERR-0642

`algebra.tex` — algebra.tex:29441-29442; omitted factor list endpoint.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29442) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. a_1,...,b_m -> a_1,...,a_n,b_1,...,b_m

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$a_1, \ldots, b_m$
+$a_1, \ldots, a_n, b_1, \ldots, b_m$
````

### MC-STK-ERR-0643

`algebra.tex` — algebra.tex:29868-29875;29937-29942; ungrouped ill typed quotients.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29869-L29940) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_typed. Group six quotient numerators and intersections explicitly.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M/M \cap M'
+M/(M \cap M')
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M'/M \cap M'
+M'/(M \cap M')
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M + M' / M'
+(M + M')/M'
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M + M'/M
+(M + M')/M
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M/M \cap M'
+M/(M \cap M')
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M'/M \cap M'
+M'/(M \cap M')
````

### MC-STK-ERR-0644

`algebra.tex` — algebra.tex:29996-30000; unmatched parenthesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29997) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_qualified. Insert one closing parenthesis before the first alignment ampersand.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-d(M, \varphi(\psi((M))) & = &
+d(M, \varphi(\psi((M)))) & = &
````

### MC-STK-ERR-0645

`algebra.tex` — algebra.tex:30020-30034; undefined dimension symbol.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30032) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_typed. R^{oplus b} -> R^{oplus n}

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R^{\oplus b}
+R^{\oplus n}
````

### MC-STK-ERR-0646

`algebra.tex` — algebra.tex:30334-30336; missing article.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30334) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. is Artinian ring -> is an Artinian ring

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-it is Artinian ring
+it is an Artinian ring
````

### MC-STK-ERR-0647

`algebra.tex` — algebra.tex:30381-30386; missing determiner.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30386) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_qualified. Insert the determiner in the finite type property.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the stability of finite type property under base change
+the stability of the finite type property under base change
````

### MC-STK-ERR-0648

`algebra.tex` — algebra.tex:30432-30444; undefined unindexed polynomial.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30440-L30444) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_typed. P(x_i)^{e_i} -> P_i(x_i)^{e_i} at both occurrences.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$P(x_i)^{e_i} = 0$
+$P_i(x_i)^{e_i} = 0$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$P(x_i)^{e_i} = 0$
+$P_i(x_i)^{e_i} = 0$
````

### MC-STK-ERR-0649

`algebra.tex` — algebra.tex:30483-30495; invalid n zero proof step.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30489) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_by_boundary_case. Handle n=0, then assume n>=1.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Namely, multiply the equation
+If $n = 0$, then $\varphi(a_0)t = 0$ and the assertion is immediate.
+Otherwise, multiply the equation
````

### MC-STK-ERR-0650

`algebra.tex` — algebra.tex:30488-30491; wrong verb preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30491) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. multiply ... with -> multiply ... by

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-with $\varphi(a_n)^{n-1}$
+by $\varphi(a_n)^{n-1}$
````

### MC-STK-ERR-0651

`algebra.tex` — algebra.tex:30570-30580; missing copula and misattached predicate.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30579) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Assume that phi(R) is integrally closed in S.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $\varphi(R) \subset S$ integrally closed in $S$.
+Assume that $\varphi(R)$ is integrally closed in $S$.
````

### MC-STK-ERR-0652

`algebra.tex` — algebra.tex:30713-30718; invalid assume be construction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30716) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Assume ... be -> Assume ... is

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $x \in S$ be strongly transcendental over $R$
+Assume $x \in S$ is strongly transcendental over $R$
````

### MC-STK-ERR-0653

`algebra.tex` — algebra.tex:30754-30756; duplicated copula.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30754-L30755) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Delete the first duplicated is.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-The base case is
+The base case
 $m = 0$ is vacuous
````

### MC-STK-ERR-0654

`algebra.tex` — algebra.tex:30759-30767; omitted integrality transitivity step.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30760-L30767) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_typed. State integrality over S', transitivity over R, and membership in the integral closure in both cases.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-$b_mx \in S'$ by
-Lemma \ref{lemma-make-integral-trivial}.
+$b_mx \in S'$: Lemma \ref{lemma-make-integral-trivial} makes it
+integral over $S'$, hence over $R$ by Lemma
+\ref{lemma-integral-transitive}, so the definition of $S'$ applies.
````

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-$b_mx \in S'$ by
-Lemma \ref{lemma-make-integral-trivial}.
+$b_mx \in S'$: Lemma \ref{lemma-make-integral-trivial} makes it
+integral over $S'$, hence over $R$ by Lemma
+\ref{lemma-integral-transitive}, so the definition of $S'$ applies.
````

### MC-STK-ERR-0655

`algebra.tex` — algebra.tex:30778-30785; ill typed algebra subject.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30780) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_typed. Let S be a finite type R-algebra.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $R \to S$ be a finite type $R$-algebra.
+Let $S$ be a finite type $R$-algebra.
````

### MC-STK-ERR-0656

`algebra.tex` — algebra.tex:30789-30793; wrong result kind.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30792) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. proposition -> theorem

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We prove the proposition
+We prove the theorem
````

### MC-STK-ERR-0657

`algebra.tex` — algebra.tex:30789-30793; missing parenthetical comma.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30791-L30792) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_qualified. For example generators -> For example, generators

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 (For
-example generators of $S$ over $R$.)
+example, generators of $S$ over $R$.)
````

### MC-STK-ERR-0658

`algebra.tex` — algebra.tex:30859-30861; sentence fragments.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30859-L30861) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed. Supply finite predicates to the surjectivity and injectivity clauses.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,3 +1,2 @@
-Surjectivity
-because of how we chose $y_i$, injectivity because
-$R'' \subset R'$, and localization is exact.
+Surjectivity follows from the choice of the $y_i$; injectivity follows
+from $R'' \subset R'$ and the exactness of localization.
````

### MC-STK-ERR-0659

`algebra.tex` — algebra.tex:30965-30984;30991-31007; missing nonfield hypothesis.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30970-L30971) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r6/candidate.manifest.json)

Independent replay result: confirmed_by_counterexample. After the enumerated hypotheses, assume moreover that B is not a field.

Adverse evidence / qualification: Exact frozen-source and mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
 \end{enumerate}
+Assume moreover that $B$ is not a field.
 Then $B$ is semi-local.
````

### MC-STK-ERR-0660

`algebra.tex` — algebra.tex:31171-31183; missing contraction definition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31171-L31172) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Define p as the inverse image of q in R before the proof forms kappa(p).

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
 Let $R \to S$ be a finite type ring map.
 Let $\mathfrak q \subset S$ be a prime.
+Let $\mathfrak p \subset R$ be the inverse image of $\mathfrak q$.
````

### MC-STK-ERR-0661

`algebra.tex` — algebra.tex:31187; malformed fraktur identifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31187) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed. Replace the undefined overline q by the defined overline fraktur q.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{q}
+\overline{\mathfrak q}
````

### MC-STK-ERR-0662

`algebra.tex` — algebra.tex:31203; missing polynomial variable separator.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31203) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed. Insert the missing comma after t_1 in the polynomial-variable list.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\kappa(\mathfrak p)[t_1\ldots, t_n]
+\kappa(\mathfrak p)[t_1, \ldots, t_n]
````

### MC-STK-ERR-0663

`algebra.tex` — algebra.tex:31280-31284; ill typed lies over relation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31283-L31284) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Define q' as S' intersect qS_p rather than saying that a prime of S' lies over a prime of S.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-we have $S_{\mathfrak q} = S'_{\mathfrak q'}$ for some
-$\mathfrak q' \subset S'$ lying over $\mathfrak q$.
+we have $S_{\mathfrak q} = S'_{\mathfrak q'}$, where
+$\mathfrak q' = S' \cap \mathfrak qS_{\mathfrak p}$.
````

### MC-STK-ERR-0664

`algebra.tex` — algebra.tex:31295-31297; wrongly asserted injectivity.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31297) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_by_counterexample. Replace the asserted inclusion by an arbitrary quasi-finite k-algebra map.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\subset
+\to
````

### MC-STK-ERR-0665

`algebra.tex` — algebra.tex:31358-31376; presentation variable collision.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31368-L31371) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Use a fresh N for the unrelated number of presentation generators.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_N
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_N
````

### MC-STK-ERR-0666

`algebra.tex` — algebra.tex:31381-31397; ill typed relative dimension.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31392-L31397) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Replace all three ill-typed dim_q(S/k) expressions by the relative fibre dimension dim_q(S/R).

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim_{\mathfrak q}(S/k)
+\dim_{\mathfrak q}(S/R)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim_{\mathfrak q}(S/k)
+\dim_{\mathfrak q}(S/R)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim_{\mathfrak q}(S/k)
+\dim_{\mathfrak q}(S/R)
````

### MC-STK-ERR-0667

`algebra.tex` — algebra.tex:31454-31457; transposed generator indices.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31457) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Generate A by the already bound elements x_{ji}.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$x_{ij}$
+$x_{ji}$
````

### MC-STK-ERR-0668

`algebra.tex` — algebra.tex:31478-31481; transposed relation indices.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31481) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Generate J by the already bound elements f_{ji}.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f_{ij}$
+$f_{ji}$
````

### MC-STK-ERR-0669

`algebra.tex` — algebra.tex:31658-31659; wrong product idempotent.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31659) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Localize at the idempotent corresponding to the factor S, not C.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$C$
+$S$
````

### MC-STK-ERR-0670

`algebra.tex` — algebra.tex:31684-31693; undefined variable count.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31685-L31692) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Replace the three undefined variable counts n by the declared count m.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_m
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_m
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_m
````

### MC-STK-ERR-0671

`algebra.tex` — algebra.tex:31707-31709;31735-31737; missing copula parallelism.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31708-L31736) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_editorial_copyedit. Insert is in both parallel finite-presentation hypotheses; this is a grammar and parallelism repair, not a mathematical change.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S'$ of finite presentation over $R$
+$S'$ is of finite presentation over $R$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S'$ of finite presentation over $R$
+$S'$ is of finite presentation over $R$
````

### MC-STK-ERR-0672

`algebra.tex` — algebra.tex:31642-31645;31651-31653; malformed parallel replacement clause.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31644-L31652) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed. State both parallel replacements by replacing the old polynomial ring by the ring with the inverse variable adjoined.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R[y_1, \ldots, y_m, y_{m + 1}]$
+$R[y_1, \ldots, y_m]$ by $R[y_1, \ldots, y_m, y_{m + 1}]$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R[y_1, \ldots, y_m, y_{m + 1}]$
+$R[y_1, \ldots, y_m]$ by $R[y_1, \ldots, y_m, y_{m + 1}]$
````

### MC-STK-ERR-0673

`algebra.tex` — algebra.tex:43650-43656;43683-43698; unnamed prime and unstated contraction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43650-L43684) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed_typed. Name the kernel prime q' and explicitly take its inverse image under the canonical map at line 43683.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-at the prime ideal which is the kernel of the map
+at the prime ideal $\mathfrak q'$ which is the kernel of the map
````

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-at the prime ideal $\mathfrak q'$
-given in the statement of the lemma
+at the inverse image of $\mathfrak q'$ under the canonical map
+$R_{\mathfrak p}^{sh} \otimes_R S \to
+R_{\mathfrak p}^{sh} \otimes_{R_{\mathfrak p}} S_{\mathfrak q}$
````

### MC-STK-ERR-0674

`algebra.tex` — algebra.tex:43832; subject verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43832) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r7/candidate.manifest.json)

Independent replay result: confirmed. filtered colimit commute -> filtered colimits commute

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-filtered colimit commute with tensor products
+filtered colimits commute with tensor products
````

### MC-STK-ERR-0675

`algebra.tex` — algebra.tex:44031-44041; omitted case and associated prime check.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44038-L44040) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_proof_gap. Separate the trivial x in R case, then verify nonisomorphism, zero kernel, nonzero target, and that m is not associated to R' by a nonzerodivisor in m which stays injective on R' inside Q(R).

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,3 +1,9 @@
 It follows that $R'/R$ is annihilated by a power of $\mathfrak m$
 (Lemma \ref{lemma-Noetherian-power-ideal-kills-module}).
-By Lemma \ref{lemma-hart-serre-loc-thm} this
+If $x \in R$, there is nothing to prove, so assume $x \notin R$.
+Then $R \to R'$ is not an isomorphism and has zero kernel.
+Since $\text{depth}(R) \geq 2$, there is a nonzerodivisor
+$t \in \mathfrak m$ on $R$. As $t$ is invertible in $Q(R)$, it
+is a nonzerodivisor on $R' \subset Q(R)$. Thus $\mathfrak m$ is
+not an associated prime of $R'$, and $R' \not = 0$.
+By~Lemma~\ref{lemma-hart-serre-loc-thm} this
````

### MC-STK-ERR-0676

`algebra.tex` — algebra.tex:44071;44108; malformed associated prime terminology.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44071-L44108) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_terminology. Replace associates primes and associate primes by associated primes.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-all its associates primes
+all its associated primes
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the set of associate primes
+the set of associated primes
````

### MC-STK-ERR-0677

`algebra.tex` — algebra.tex:44078; missing sentence terminator.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44078) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_punctuation. Add the missing period after the parenthetical sentence before Hence.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(use Lemma \ref{lemma-depth-in-ses} for example)
+(use Lemma \ref{lemma-depth-in-ses} for example).
````

### MC-STK-ERR-0678

`algebra.tex` — algebra.tex:44287-44288; circular field of fractions presentation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44287-L44288) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_circular_presentation. Join the broken sentence and replace the coefficient field K by k in the domain whose fraction field is K.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Moreover $K$ is the field of fractions of the domain.
-$S = K[X_1, \ldots, X_{r + 1}]/(G)$.
+Moreover $K$ is the field of fractions of the domain
+$S = k[X_1, \ldots, X_{r + 1}]/(G)$.
````

### MC-STK-ERR-0679

`algebra.tex` — algebra.tex:44298;44314; undefined differential shorthand.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44298-L44314) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_undefined_shorthand. Replace both undefined Omega_k tokens by Omega_{k/F_p}.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S \otimes_k \Omega_k \oplus
+S \otimes_k \Omega_{k/\mathbf{F}_p} \oplus
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-K \otimes_k \Omega_k \oplus
+K \otimes_k \Omega_{k/\mathbf{F}_p} \oplus
````

### MC-STK-ERR-0680

`algebra.tex` — algebra.tex:44324; wrong differential codomain.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44324) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_wrong_codomain. Replace the codomain Omega_{S/F_p} by the localized codomain Omega_{K/F_p}.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$K \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{S/\mathbf{F}_p}$
+$K \otimes_k \Omega_{k/\mathbf{F}_p} \to \Omega_{K/\mathbf{F}_p}$
````

### MC-STK-ERR-0681

`algebra.tex` — algebra.tex:44389-44393; characteristic scope and differential base gap.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44389-L44393) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_proof_scope_gap. Dispose of characteristic zero first, then in characteristic p apply the formal-smoothness exact-sequence lemma directly over F_p to obtain precisely the differential injection required by the cited separability criterion.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,5 +1,8 @@
 Assume $K$ is formally smooth over $k$.
+If $k$ has characteristic zero, then $K/k$ is separable.
+Thus we may assume that $k$ has characteristic $p > 0$.
 By Lemma \ref{lemma-ses-formally-smooth} we see that
-$K \otimes_k \Omega_{k/\mathbf{Z}} \to \Omega_{K/\mathbf{Z}}$
+$K \otimes_k \Omega_{k/\mathbf{F}_p} \to
+\Omega_{K/\mathbf{F}_p}$
 is injective. Hence $K$ is separable over $k$ by
 Lemma \ref{lemma-separable-differentials}.
````

### MC-STK-ERR-0682

`algebra.tex` — algebra.tex:44405; subject number error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44405) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_grammar. Replace a vector spaces is free by a vector space is free.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the fact that a vector spaces is free
+the fact that a vector space is free
````

### MC-STK-ERR-0683

`algebra.tex` — algebra.tex:44500-44504; omitted characterization reference.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44500-L44504) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_missing_reference. Add the characterization of formal smoothness by H_1 vanishing and repair the missing list comma.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1,5 +1,6 @@
 This is a combination of
 Lemmas \ref{lemma-characterize-separable-field-extensions},
-\ref{lemma-fields-are-formally-smooth}
+\ref{lemma-fields-are-formally-smooth},
+\ref{lemma-characterize-formally-smooth-field-extension},
 \ref{lemma-formally-smooth-implies-separable}, and
 \ref{lemma-separable-differentials}.
````

### MC-STK-ERR-0684

`algebra.tex` — algebra.tex:44547; wrong technical term.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44547) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_technical_term. Replace minimum polynomial by minimal polynomial.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-minimum polynomial
+minimal polynomial
````

### MC-STK-ERR-0685

`algebra.tex` — algebra.tex:44549-44551; index and agreement errors.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44549-L44551) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r8/candidate.manifest.json)

Independent replay result: confirmed_index_and_agreement_errors. Use plural agreement for P_1 through P_r and replace both x_r endpoints by x_d, the previously declared transcendence-basis endpoint.

Adverse evidence / qualification: Exact frozen-source and independent mathematical review evidence is bound under authority/canon; no translation or authority byte was used as the corrected payload.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$P_1, \ldots, P_r$ is a regular sequence
+$P_1, \ldots, P_r$ are a regular sequence
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$k(x_1, \ldots, x_r)[Y_1, \ldots, Y_r]$
+$k(x_1, \ldots, x_d)[Y_1, \ldots, Y_r]$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$L = k(x_1, \ldots, x_r)[Y_1, \ldots, Y_r]/(P_1, \ldots, P_r)$
+$L = k(x_1, \ldots, x_d)[Y_1, \ldots, Y_r]/(P_1, \ldots, P_r)$
````

### MC-STK-ERR-0686

`algebra.tex` — algebra.tex:44590;44607;44617; inconsistent component order.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44607-L44617) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_notation_error. Normalize the two reversed category-object triples to the declared field-first order.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$((R_i, k_i, \phi_i), \psi_{ii'})$ is a system over $I$, see
+$((k_i, R_i, \phi_i), \psi_{ii'})$ is a system over $I$, see
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(R', k', \phi')$ is an
+$(k', R', \phi')$ is an
````

### MC-STK-ERR-0687

`algebra.tex` — algebra.tex:44595-44603; missing r algebra compatibility.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44596) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_type_and_proof_gap. Require transition morphisms to be R-algebra maps so the colimit R-structure and flatness claim are defined.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-given by ring maps $\psi : R_1 \to R_2$ such that
+given by $R$-algebra maps $\psi : R_1 \to R_2$ such that
````

### MC-STK-ERR-0688

`algebra.tex` — algebra.tex:44625-44629; missing base field in generated subfield.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44625-L44626) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_definition_gap. Define K(x) as the subfield generated over k by the initial segment.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 For $x \in K$ we let $K(x)$ be the subfield of $K$ generated
-by all elements of $K$ which are $\leq x$.
+over $k$ by all elements of $K$ which are $\leq x$.
````

### MC-STK-ERR-0689

`algebra.tex` — algebra.tex:44631;44637; polynomial ring notation for field adjunction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44631-L44637) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_notation_error. Use field-adjunction parentheses at both loci.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Namely, if $x$ has a predecessor $x'$, then $K(x) = K(x')[x]$
+Namely, if $x$ has a predecessor $x'$, then $K(x) = K(x')(x)$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Since $K(x) = K'(x)[x]$ we see that we can use the construction of the
+Since $K(x) = K'(x)(x)$ we see that we can use the construction of the
````

### MC-STK-ERR-0690

`algebra.tex` — algebra.tex:44634-44638; missing least element base case.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44633-L44636) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_base_case_gap. Initialize the least-element branch with R'(x)=R and K'(x)=k before using the nonleast limit construction.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,4 +1,6 @@
 If $x$ does not
-have a predecessor, then we first set
+have a predecessor, then we set $R'(x) = R$ and $K'(x) = k$
+if $x$ is the least element. Otherwise, we set
 $R'(x) = \colim_{x' < x} R(x')$ as in the third paragraph
-of the proof. The residue field of $R'(x)$ is $K'(x) = \bigcup_{x' < x} K(x')$.
+of the proof. In this case the residue field of $R'(x)$ is
+$K'(x) = \bigcup_{x' < x} K(x')$.
````

### MC-STK-ERR-0691

`algebra.tex` — algebra.tex:44624-44639;44652-44656; missing terminal colimit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44624-L44639) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_terminal_construction_gap. Choose the well-order with a greatest element and identify its constructed ring as the required extension with residue field K.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-To get around this problem we choose a well ordering on $K$.
+To get around this problem we choose a well ordering on $K$ with a greatest
+element.
````

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
 first paragraph of the proof to produce $R'(x) \subset R(x)$.
-This finishes the proof of the lemma.
+For the greatest element $x$ of the chosen ordering we have $K(x) = K$.
+Thus $R(x)$ is the extension required by the lemma.
````

### MC-STK-ERR-0692

`algebra.tex` — algebra.tex:44661-44671; omitted locality descent.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44664-L44667) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_proof_gap. Prove locality of the descended finite-etale algebra and every later base change by faithfully flat descent.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,4 +1,11 @@
 there exists an $i$ and a finite \'etale extension $R_i \to R_{i, 1}$
 such that $R_{\alpha + 1} = R_\alpha \otimes_{R_i} R_{i, 1}$.
-Thus $R_{\alpha + 1} = \colim_{i' \geq i} R_{i'} \otimes_{R_i} R_{i, 1}$
-and the result holds for $\alpha + 1$. Suppose $\alpha$ is not a successor
+The map $R_i \to R_\alpha$ is flat local, hence faithfully flat. Since
+$R_{\alpha + 1}$ is the base change of $R_{i, 1}$, faithfully flat
+descent of locality shows that $R_{i, 1}$ is local. More generally,
+for every $i' \geq i$, the map $R_{i'} \to R_\alpha$ is flat local,
+hence faithfully flat, and the base change of
+$R_{i'} \otimes_{R_i} R_{i, 1}$ to $R_\alpha$ is $R_{\alpha + 1}$.
+Hence all these rings are local, and
+$R_{\alpha + 1} = \colim_{i' \geq i} R_{i'} \otimes_{R_i} R_{i, 1}$.
+Thus the result holds for $\alpha + 1$. Suppose $\alpha$ is not a successor
````

### MC-STK-ERR-0693

`algebra.tex` — algebra.tex:44669-44671; malformed logical coordination.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44670) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Remove the malformed and after the Since-clause and insert the needed comma.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some $\beta < \alpha$ and we see that $E$ is contained in a finite \'etale
+for some $\beta < \alpha$, we see that $E$ is contained in a finite \'etale
````

### MC-STK-ERR-0694

`algebra.tex` — algebra.tex:44685; wrong induction preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44685) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Change induction of the degree to induction on the degree.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-By induction of the degree of $\kappa(\mathfrak p) \subset L$.
+By induction on the degree of $\kappa(\mathfrak p) \subset L$.
````

### MC-STK-ERR-0695

`algebra.tex` — algebra.tex:44687-44691; nondecreasing induction and grammar.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44687-L44691) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_induction_gap_and_grammar_error. Require a proper nontrivial intermediate field and replace then construction by then constructing.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,5 +1,6 @@
 In general, if there exists a sub extension
-$\kappa(\mathfrak p) \subset L' \subset L$ then we win by induction
+$\kappa(\mathfrak p) \subset L' \subset L$ with both inclusions strict,
+then we win by induction
 on the degree (by first constructing $R \subset S'$ corresponding
-to $L'/\kappa(\mathfrak p)$ and then construction $S' \subset S$
+to $L'/\kappa(\mathfrak p)$ and then constructing $S' \subset S$
 corresponding to $L/L'$). Thus we may assume that
````

### MC-STK-ERR-0696

`algebra.tex` — algebra.tex:44748; typographical error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44748) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_typographical_error. Correct choicse to choices.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Given these choicse, we let $E_{k + 1} \subset B$ be the $A$-subalgebra
+Given these choices, we let $E_{k + 1} \subset B$ be the $A$-subalgebra
````

### MC-STK-ERR-0697

`algebra.tex` — algebra.tex:44755-44756; malformed cardinality phrase.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44755-L44756) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Change has at most cardinality to has cardinality at most.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Some set theory (omitted) shows that $E_{k + 1}$ has at most
-cardinality $\kappa$ (this uses that we inductively know
+Some set theory (omitted) shows that $E_{k + 1}$ has cardinality
+at most $\kappa$ (this uses that we inductively know
````

### MC-STK-ERR-0698

`algebra.tex` — algebra.tex:44813; zero ring counterexample to quotient claim.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44813) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_scope_error. Restrict the assertion to quotients by proper ideals.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Any quotient of $R$ is also a Noetherian complete local ring.
+Any quotient of $R$ by a proper ideal is also a Noetherian complete local ring.
````

### MC-STK-ERR-0699

`algebra.tex` — algebra.tex:44814; malformed given then construction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44814) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Delete then from the malformed Given construction.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Given a finite ring map $R \to S$, then $S$ is a product of
+Given a finite ring map $R \to S$, $S$ is a product of
````

### MC-STK-ERR-0700

`algebra.tex` — algebra.tex:44873-44874; missing copula.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44873-L44874) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. State explicitly that the uniformizer p is a prime number.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-A {\it Cohen ring} is a complete discrete valuation ring with
-uniformizer $p$ a prime number.
+A {\it Cohen ring} is a complete discrete valuation ring whose
+uniformizer $p$ is a prime number.
````

### MC-STK-ERR-0701

`algebra.tex` — algebra.tex:44994; ill typed arrow label.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44985-L44986) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_type_error. Declare the overloaded notation for reduction modulo p^(n-1) followed by phi_(n-1).

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,5 @@
-for $n = 1$. If $n > 1$, let $\varphi_{n - 1}$ be given.
+for $n = 1$. If $n > 1$, let $\varphi_{n - 1}$ be given, and also
+write $\varphi_{n - 1}$ for the composite
+$\Lambda/p^n\Lambda \to \Lambda/p^{n - 1}\Lambda
+\xrightarrow{\varphi_{n - 1}} R/\mathfrak m^{n - 1}$.
 The ring map $\mathbf{Z}/p^n\mathbf{Z} \to \Lambda/p^n\Lambda$
````

### MC-STK-ERR-0702

`algebra.tex` — algebra.tex:45016-45019; mismatched adic ideals.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45016-L45019) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_notation_and_proof_gap. Name the respective source (x_i)-adic and target (y_i)-adic ideals.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,4 +1,5 @@
-Since both sides are $(x_1, \ldots, x_n)$-adically complete
-this map is surjective by Lemma \ref{lemma-completion-generalities}
-as it is surjective modulo $(x_1, \ldots, x_n)$ by
-construction.
+Since the source and target are complete with respect to the ideals
+$(x_1, \ldots, x_n)$ and $(y_1, \ldots, y_n) = \mathfrak m$,
+respectively, this map is surjective by
+Lemma \ref{lemma-completion-generalities} as the induced map modulo
+these respective ideals is surjective by construction.
````

### MC-STK-ERR-0703

`algebra.tex` — algebra.tex:45067; missing head noun.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45067) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Insert subring before R_0.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then there exists a $R_0 \subset R$ with the following properties
+Then there exists a subring $R_0 \subset R$ with the following properties
````

### MC-STK-ERR-0704

`algebra.tex` — algebra.tex:45099-45102; premature proof closure.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45098-L45102) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_proof_structure_error. Replace the premature whole-lemma closure by This proves Case I.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
-$R_0 \to R$ is injective (see Lemma \ref{lemma-integral-dim-up}),
-and the lemma is proved.
+$R_0 \to R$ is injective (see Lemma \ref{lemma-integral-dim-up}).
+This proves Case I.
 
 \medskip\noindent
 Case II: $\Lambda$ is a Cohen ring. Let $d + 1 = \dim(R)$.
````

### MC-STK-ERR-0705

`algebra.tex` — algebra.tex:44799-44802; ambiguous footnote attachment.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44799-L44802) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_editorial_ambiguity. Split the finite-generation and Noetherian-completion assertions.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
-This does not happen when $\mathfrak m$ is finitely generated, see
-Lemma \ref{lemma-hathat-finitely-generated} in which
-case the completion is Noetherian, see
+This does not happen when $\mathfrak m$ is finitely generated; see
+Lemma \ref{lemma-hathat-finitely-generated}. In this
+case the completion is Noetherian; see
 Lemma \ref{lemma-completion-Noetherian}.}.
````

### MC-STK-ERR-0706

`algebra.tex` — algebra.tex:45311-45312; malformed invariant subfield apposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45311-L45312) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Identify L^G as the invariant subfield of L with a grammatical apposition.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-with fraction field $K = L^G$ the $G$-invariants in the fraction field
-$L$ of $A$.
+with fraction field $K = L^G$, the subfield of $G$-invariants in the
+fraction field $L$ of $A$.
````

### MC-STK-ERR-0707

`algebra.tex` — algebra.tex:45325-45326; unstated fraction field extension of derivation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45325-L45326) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_type_gap. State that the unique extension of D to the fraction field satisfies D(a) nonzero.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
 Let $a \in K$ be an element such that there exists a derivation
-$D : R \to R$ with $D(a) \not = 0$. Then the integral closure
+$D : R \to R$ whose unique extension to the fraction field satisfies
+$D(a) \not = 0$. Then the integral closure
````

### MC-STK-ERR-0708

`algebra.tex` — algebra.tex:45364-45366; omitted normality argument.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45364-L45366) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_proof_gap. State that the integral difference lies in the fraction field and hence in R by normality.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,5 @@
-Hence $D(a)^{i + 1}a_0$ is also in $R$ because it is the
-difference of $D(a)^{i + 1}y$ and $\sum_{j > 0} D(a)^{i + 1}a_jx^j$ which
-are integral over $R$ (since $x$ is integral over $R$ as $a \in R$).
+Hence $D(a)^{i + 1}a_0$ is also in $R$: it is the
+difference of $D(a)^{i + 1}y$ and $\sum_{j > 0} D(a)^{i + 1}a_jx^j$, both
+of which are integral over $R$ (since $x$ is integral over $R$ as
+$a \in R$). Their difference also lies in the fraction field, so
+normality shows that it belongs to the ring.
````

### MC-STK-ERR-0709

`algebra.tex` — algebra.tex:45429-45431; mis scoped purely inseparable extension.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45429-L45431) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_scope_error. Quantify the finite purely inseparable field extension and its integral closure unambiguously.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 In characteristic $p > 0$ we have to show that the integral
-closure of $R[x]$ is finite in any finite purely inseparable extension
-of $L/K(x)$ where $K$ is the fraction field of $R$. There
+closure of $R[x]$ in every finite purely inseparable field extension
+$L/K(x)$ is finite, where $K$ is the fraction field of $R$. There
````

### MC-STK-ERR-0710

`algebra.tex` — algebra.tex:45435-45437; missing relative clause.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45436-L45437) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Introduce the integral closure R' with an explicit relative clause.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-is equal to $R'[x^{1/q}]$ with $R \subset R' \subset L'$ the integral
-closure of $R$ in $L'$.
+is equal to $R'[x^{1/q}]$ with $R \subset R' \subset L'$, where the middle
+ring is the integral closure of $R$ in $L'$.
````

### MC-STK-ERR-0711

`algebra.tex` — algebra.tex:45458-45464; wrong alternative connective.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45460-L45462) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_logical_connective_error. Join the two Serre-criterion alternatives with or.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 \item Case I: $\text{depth}(R_{\mathfrak q}) < 2$
-and $\dim(R_{\mathfrak q}) \geq 2$, and
+and $\dim(R_{\mathfrak q}) \geq 2$, or
 \item Case II: $R_{\mathfrak q}$ is not regular
````

### MC-STK-ERR-0712

`algebra.tex` — algebra.tex:45509; malformed denote construction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45509) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Repair the denote construction.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For such a ring $R'$ denote $Z_{R'} \subset \Spec(R)$ this image.
+For such a ring $R'$, denote this image by $Z_{R'} \subset \Spec(R)$.
````

### MC-STK-ERR-0713

`algebra.tex` — algebra.tex:45523-45529; omitted contraction and normality localization argument.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45527-L45529) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_proof_gap. Define the contractions and use an intermediate localization to justify the normality equality safely.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,11 @@
-Namely, every prime $\mathfrak p'$ lies over a prime $\mathfrak p'_i$
-such that $(R'_i)_{\mathfrak p'_i}$ is normal. This implies
-that $R'_{\mathfrak p'} = (R'_i)_{\mathfrak p'_i}$ is normal too.
+Namely, let $\mathfrak p' \in \Spec(R')$ and set
+$\mathfrak p = \mathfrak p' \cap R$. Choose $i$ such that
+$\mathfrak p \not \in Z_{R'_i}$ and set
+$\mathfrak p'_i = \mathfrak p' \cap R'_i$. Then
+$(R'_i)_{\mathfrak p'_i}$ is normal. Set
+$T = R'_i \setminus \mathfrak p'_i$. The extension
+$R'_i \subset R'$ is integral, and hence $T^{-1}R'$ is integral over
+$(R'_i)_{\mathfrak p'_i}$. Both rings are contained in $K$, the fraction
+field of $(R'_i)_{\mathfrak p'_i}$, so normality gives
+$T^{-1}R' = (R'_i)_{\mathfrak p'_i}$. Localizing at $\mathfrak p'$ gives
+$R'_{\mathfrak p'} = (R'_i)_{\mathfrak p'_i}$, which is normal.
````

### MC-STK-ERR-0714

`algebra.tex` — algebra.tex:45561-45563; omitted reduction after field enlargement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45562-L45563) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r9/candidate.manifest.json)

Independent canon replay: confirmed_proof_gap. Justify reduction from the enlarged purely inseparable field back to the original normalization.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,8 @@
-By enlarging $L$ if necessary we may assume there exists
-an element $y \in L$ such that $y^q = x$.
+Choose a $q$th root $y$ of $x$ in an algebraic closure of $K$, set
+$\widetilde L = L(y)$, and let $\widetilde S$ be the integral closure
+of $R$ in $\widetilde L$. Then $\widetilde L/K$ is a finite purely
+inseparable extension and $\widetilde L^q \subset K$. Moreover,
+$S = \widetilde S \cap L$, so $S$ is an $R$-submodule of $\widetilde S$.
+Thus, if $\widetilde S$ is finite over $R$, then $S$ is finite over $R$
+because $R$ is Noetherian. Replacing $L$ by $\widetilde L$ and $S$ by
+$\widetilde S$, we may therefore assume that $y \in L$ and $y^q = x$.
````

### MC-STK-ERR-0715

`algebra.tex` — algebra.tex:45748-45751; zero localization outside n2 domain.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45748-L45751) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_definition_domain_error. Restrict the localization claim to f_i outside the prime and state that the surviving images generate the unit ideal.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,4 +1,6 @@
-$\mathfrak p \subset R$ is a prime, then we see each
-$R_{f_i}/\mathfrak pR_{f_i} = (R/\mathfrak p)_{f_i}$ is N-2
-and hence we conclude $R/\mathfrak p$ is N-2 by
+$\mathfrak p \subset R$ is a prime, then for every $i$ such that
+$f_i \not \in \mathfrak p$ we see
+$R_{f_i}/\mathfrak pR_{f_i} = (R/\mathfrak p)_{f_i}$ is N-2.
+The images of these $f_i$ in $R/\mathfrak p$ generate the unit ideal, and
+hence we conclude $R/\mathfrak p$ is N-2 by
 Lemma \ref{lemma-Japanese-local}. This proves (2).
````

### MC-STK-ERR-0716

`algebra.tex` — algebra.tex:45877; article agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45877) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Correct the indefinite article before R-completion-submodule.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a $R^\wedge$-submodule
+is an $R^\wedge$-submodule
````

### MC-STK-ERR-0717

`algebra.tex` — algebra.tex:46042-46051; rescaling fails at closed prime.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46042-L46051) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_proof_gap. Split off the field case and rescale every generator by one fixed element of m outside p.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,2 +1,5 @@
 To prove (1) we have to show that the integral closure of $R/\mathfrak p$
-is finite over $R/\mathfrak p$. Choose $x_1, \ldots, x_n \in L$
+is finite over $R/\mathfrak p$. If $\mathfrak p = \mathfrak m$, then
+$R/\mathfrak p$ is a field and the assertion is immediate. Thus we may
+assume $\mathfrak p \not = \mathfrak m$ and choose
+$g \in \mathfrak m \setminus \mathfrak p$. Choose $x_1, \ldots, x_n \in L$
````

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-$a_{i, j} \in R/\mathfrak p$. In fact, after further multiplying
-by elements of $\mathfrak m$, we may assume
+$a_{i, j} \in R/\mathfrak p$. After further replacing each $x_i$
+by $g x_i$, we may assume
 $a_{i, j} \in \mathfrak m/\mathfrak p \subset R/\mathfrak p$ for all $i, j$.
````

### MC-STK-ERR-0718

`algebra.tex` — algebra.tex:46110; unjustified normality restriction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46110) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_logical_restriction_error. Remove normal from the arbitrary Nagata-domain reduction.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Step 4. Let $R$ be a normal Nagata domain and
+Step 4. Let $R$ be a Nagata domain and
````

### MC-STK-ERR-0719

`algebra.tex` — algebra.tex:46143; missing subject.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46143) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Insert the missing subject in the localization reduction.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and $S$ by $S_a$, may assume
+and $S$ by $S_a$, we may assume
````

### MC-STK-ERR-0720

`algebra.tex` — algebra.tex:46144; wrong polynomial indeterminate.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46144) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_notation_error. Use R[X] for the polynomial indeterminate.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $R[x]$ with
+in $R[X]$ with
````

### MC-STK-ERR-0721

`algebra.tex` — algebra.tex:46152-46154; overbroad maximal ideal quantifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46152-L46154) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_quantifier_error. Restrict to maximal ideals of S' lying over the fixed maximal ideal.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 Moreover, $S'$ is finite over $S$. If for every maximal ideal
-$\mathfrak m'$ of $S'$ the local ring $S'_{\mathfrak m'}$ is
-N-1, then $S'_{\mathfrak m}$ is N-1 by
+$\mathfrak m'$ of $S'$ lying over $\mathfrak m$ the local ring
+$S'_{\mathfrak m'}$ is N-1, then $S'_{\mathfrak m}$ is N-1 by
````

### MC-STK-ERR-0722

`algebra.tex` — algebra.tex:46170; missing zero branch.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46170) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_missing_case. Dispose of x=0 before invoking the nonzero-element criterion.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-We have to show $S_{\mathfrak m}$ is N-1.
+We have to show $S_{\mathfrak m}$ is N-1. If $x = 0$, then $S = R$
+and there is nothing to prove. Thus we may and do assume $x \not = 0$.
````

### MC-STK-ERR-0723

`algebra.tex` — algebra.tex:46185; missing plus sign.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46185) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_formula_typo. Insert the missing plus sign after the polynomial ellipsis.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-+ \ldots a_1 X +
++ \ldots + a_1 X +
````

### MC-STK-ERR-0724

`algebra.tex` — algebra.tex:46280; unstated locality and topology agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46280) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r10/candidate.manifest.json)

Independent canon replay: confirmed_proof_gap. Prove B is local and that its maximal-adic and mB-adic topologies agree before applying the completion lemma.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1,5 @@
 $B = A[x]/(x^p - a)$ is a domain because $K[x]/(x^p - a)$ is a field.
+The ring $B$ is local because its special fibre
+$B/\mathfrak mB = \kappa(\mathfrak m)[x]/(x^p - \overline{a})$ has a unique
+prime ideal. Moreover, the maximal-adic and $\mathfrak mB$-adic topologies
+on $B$ agree.
````

### MC-STK-ERR-0725

`algebra.tex` — algebra.tex:46321; zero module dimension case.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46321) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/candidate.manifest.json)

Independent canon replay: confirmed_missing_case. Add the omitted zero-module case before introducing the finite right-hand-side dimension.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
+If $M = 0$ or $N = 0$, then both sides of the formula are infinite,
+and there is nothing to prove. Thus we may assume that $M$ and $N$ are nonzero.
 Denote $n$ the right hand side. First assume that $n$ is zero.
````

### MC-STK-ERR-0726

`algebra.tex` — algebra.tex:46464,46493; missing item punctuation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46464-L46493) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Add the missing terminal comma to both repeated list items.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item $S$ is Noetherian
+\item $S$ is Noetherian,
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item $S$ is Noetherian
+\item $S$ is Noetherian,
````

### MC-STK-ERR-0727

`algebra.tex` — algebra.tex:46536; missing subring subject and comma.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46536) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Identify R_0 as a subring and punctuate the introductory clause.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-However, since $R_0 \subset R$ is reduced we see that
+However, since the subring $R_0 \subset R$ is reduced, we see that
````

### MC-STK-ERR-0728

`algebra.tex` — algebra.tex:46623; incorrect lemma application quantifier.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46623) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r11/candidate.manifest.json)

Independent canon replay: confirmed_proof_exposition_error. State the lemma application with the correct per-index quantifier.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-This follows from Lemma \ref{lemma-Rk-goes-up} applied for all $(R_k)$
+This follows by applying Lemma \ref{lemma-Rk-goes-up} for every $k \geq 0$
````

### MC-STK-ERR-0729

`algebra.tex` — algebra.tex:46640; subject verb agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46640) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use singular agreement for the assumption on one ring map.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-words, the assumption on the ring map $R \to S$ are often weaker than
+words, the assumption on the ring map $R \to S$ is often weaker than
````

### MC-STK-ERR-0730

`algebra.tex` — algebra.tex:46698; missing flatness adjective.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46698) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/candidate.manifest.json)

Independent canon replay: confirmed_missing_word. Restore flat in the faithfully flat localization claim.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is faithfully over $R_{\mathfrak p}$ too we may assume that
+is faithfully flat over $R_{\mathfrak p}$ too we may assume that
````

### MC-STK-ERR-0731

`algebra.tex` — algebra.tex:46814; missing terminal punctuation.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46814) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/candidate.manifest.json)

Independent canon replay: confirmed_punctuation_error. Add the missing full stop after the parenthetical sentence.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(by going down, see Lemma \ref{lemma-flat-going-down})
+(by going down, see Lemma \ref{lemma-flat-going-down}).
````

### MC-STK-ERR-0732

`algebra.tex` — algebra.tex:46834; missing integral closure definition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46834) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/candidate.manifest.json)

Independent canon replay: confirmed_missing_definition. Define A' as the integral closure of A in Q(A) before using it.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
+Let $A'$ be the integral closure of $A$ in $Q(A)$.
 Via this map $A'$ maps into $B'$. This induces a map
````

### MC-STK-ERR-0733

`algebra.tex` — algebra.tex:46844; verb tense agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46844) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use present tense for the simultaneous module-generation conclusion.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the $x_i$ also generated $A'$ as an $A$-module, and we win.
+the $x_i$ also generate $A'$ as an $A$-module, and we win.
````

### MC-STK-ERR-0734

`algebra.tex` — algebra.tex:46856; residue field agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46856) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r12/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. State separately that each local factor has the same residue field as A.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-respectively, and the same residue fields as that of $A$.
+respectively, and each has the same residue field as $A$.
````

### MC-STK-ERR-0735

`algebra.tex` — algebra.tex:47042; incorrect tensor base field.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47042) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r13/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r13/candidate.manifest.json)

Independent canon replay: confirmed_mathematical_type_error. Tensor A and L over the shared base field k, not over the fraction field K.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A \otimes_K L$
+$A \otimes_k L$
````

### MC-STK-ERR-0736

`algebra.tex` — algebra.tex:47011,47023; compound number agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47011-L47023) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r13/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r13/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use the singular compound fraction fields at both repeated loci.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-fractions fields
+fraction fields
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-fractions fields
+fraction fields
````

### MC-STK-ERR-0737

`algebra.tex` — algebra.tex:47013,47015,47016; closed compound spelling.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47013-L47016) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r13/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r13/candidate.manifest.json)

Independent canon replay: confirmed_spelling_error. Use the closed compound subalgebra in all three adjacent occurrences.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sub algebras
+subalgebras
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sub algebra
+subalgebra
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sub algebra
+subalgebra
````

### MC-STK-ERR-0738

`algebra.tex` — algebra.tex:47214; incorrect colimit field identity.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47214) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/candidate.manifest.json)

Independent canon replay: confirmed_mathematical_identity_error. The finite extension is chosen so that k-prime is the scalar extension of k, not so that k_i equals that scalar extension.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$k_i = k \otimes_{k_i} k_i'$
+$k' = k \otimes_{k_i} k_i'$
````

### MC-STK-ERR-0739

`algebra.tex` — algebra.tex:47344; determiner number agreement.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47344) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Remove the singular article before the plural noun phrase ring maps.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-together with a ring maps
+together with ring maps
````

### MC-STK-ERR-0740

`algebra.tex` — algebra.tex:47394-47396; malformed flat locus sentence.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47394-L47396) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/candidate.manifest.json)

Independent canon replay: confirmed_omitted_words_error. State the openness theorem as the set of primes at which M_lambda is flat being open.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-By Theorem \ref{theorem-openness-flatness} we get an open subset
-$U_\lambda \subset \Spec(S_\lambda)$ such that $M_\lambda$
-flat over $R_\lambda$ at all the primes of $U_\lambda$.
+By Theorem \ref{theorem-openness-flatness}, the set
+$U_\lambda \subset \Spec(S_\lambda)$ of primes at which $M_\lambda$
+is flat over $R_\lambda$ is open.
````

### MC-STK-ERR-0741

`algebra.tex` — algebra.tex:47410; inconsistent index bound.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47410) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/candidate.manifest.json)

Independent canon replay: confirmed_mathematical_index_error. Index the chosen s_i by the same bound r as the f_i appearing in the sum.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$s_1, \ldots, s_n \in S$
+$s_1, \ldots, s_r \in S$
````

### MC-STK-ERR-0742

`algebra.tex` — algebra.tex:47488; missing preposition.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47488) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/candidate.manifest.json)

Independent canon replay: confirmed_grammar_error. Use the idiom replaced by Z.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-with $R$ replaced $\mathbf{Z}$
+with $R$ replaced by $\mathbf{Z}$
````

### MC-STK-ERR-0743

`algebra.tex` — algebra.tex:47852; incorrect prime label.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47852) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/candidate.manifest.json)

Independent canon replay: confirmed_mathematical_notation_error. Quasi-finiteness is asserted at the prime q-prime of S-prime, not at q of S.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-quasi-finite at $\mathfrak q$ as the local ring
+quasi-finite at $\mathfrak q'$ as the local ring
````

### MC-STK-ERR-0744

`algebra.tex` — algebra.tex:47855; incorrect quotient parenthesization.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47855) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r14/candidate.manifest.json)

Independent canon replay: confirmed_mathematical_parenthesization_error. Place the full sum of ideals in the denominator of the localized quotient.

Adverse evidence / qualification: The frozen source and producer evidence are retained; no translation byte or mutable upstream file was used as the correction authority.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S_{\mathfrak q}/(f_1, \ldots, f_d) + \mathfrak pS_{\mathfrak q} =
+S_{\mathfrak q}/\big((f_1, \ldots, f_d) + \mathfrak pS_{\mathfrak q}\big) =
````

### MC-STK-ERR-0399

`algebra.tex` — algebra.tex:31816-31827; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31824) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(I, \leq)$
+$(\Lambda, \leq)$
````

### MC-STK-ERR-0400

`algebra.tex` — algebra.tex:31801; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31801) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cofiltered
+filtered
````

### MC-STK-ERR-0401

`algebra.tex` — algebra.tex:32020; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32020) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $M \otimes_A R_i$
+in $N \otimes_A R_i$
````

### MC-STK-ERR-0402

`algebra.tex` — algebra.tex:32034-32036; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32036) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\sum a_j x_j
+\sum a_j y_j
````

### MC-STK-ERR-0403

`algebra.tex` — algebra.tex:32056-32057; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32056-L32057) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M \otimes_R R_i
+M \otimes_A R_i
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-N \otimes_R R_i
+N \otimes_A R_i
````

### MC-STK-ERR-0404

`algebra.tex` — algebra.tex:32134-32136; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32134-L32136) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$B \otimes_A R = \colim_i B \otimes_A R_i$
+$C \otimes_A R = \colim_i C \otimes_A R_i$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $B \otimes_A R_i$
+in $C \otimes_A R_i$
````

### MC-STK-ERR-0405

`algebra.tex` — algebra.tex:32151; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32151) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$K = \Ker(A[x_1, \ldots, x_m] \to N)$
+$K = \Ker(A[x_1, \ldots, x_m] \to C)$
````

### MC-STK-ERR-0406

`algebra.tex` — algebra.tex:32152; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32152) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_j \mapsto \sum c_j
+x_j \mapsto c_j
````

### MC-STK-ERR-0407

`algebra.tex` — algebra.tex:32162; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32162) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\xi_s = f_j(z_1, \ldots, z_m)$
+$\xi_s = f_s(z_1, \ldots, z_m)$
````

### MC-STK-ERR-0408

`algebra.tex` — algebra.tex:32170-32171; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32170) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$v : B \otimes_A R \to C \otimes_A R$
+$v : C \otimes_A R \to B \otimes_A R$
````

### MC-STK-ERR-0409

`algebra.tex` — algebra.tex:32173-32174; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32173-L32174) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-B \otimes_R R_i
+B \otimes_A R_i
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-C \otimes_R R_i
+C \otimes_A R_i
````

### MC-STK-ERR-0410

`algebra.tex` — algebra.tex:32197-32198; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32197-L32198) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi \otimes 1_R = \psi \otimes 1_R$
+$\varphi_\lambda \otimes 1_R = \psi_\lambda \otimes 1_R$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi \otimes 1_{R_\mu} = \psi \otimes 1_{R_\mu}$
+$\varphi_\lambda \otimes 1_{R_\mu} = \psi_\lambda \otimes 1_{R_\mu}$
````

### MC-STK-ERR-0411

`algebra.tex` — algebra.tex:32531-32532; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32531-L32532) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 integral
-over $S$
+over $R$
````

### MC-STK-ERR-0412

`algebra.tex` — algebra.tex:16530-16532; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16531) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$D(f) \cap \text{supp}(K) = 0$
+$D(f) \cap \text{supp}(K) = \emptyset$
````

### MC-STK-ERR-0413

`algebra.tex` — algebra.tex:18416-18417; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18416) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H_i(R(A)_\bullet))$
+$H_i(R(A)_\bullet)$
````

### MC-STK-ERR-0414

`algebra.tex` — algebra.tex:18643-18646; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18644) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cohomology groups
+homology groups
````

### MC-STK-ERR-0415

`algebra.tex` — algebra.tex:522; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L522) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an surjection
+a surjection
````

### MC-STK-ERR-0416

`algebra.tex` — algebra.tex:972; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L972) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-zero on $H$
+zero in $H$
````

### MC-STK-ERR-0417

`algebra.tex` — algebra.tex:1148-1150; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1148-L1150) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 Denote by $m/s$ (or
-$\frac{m}{s}$) be the equivalence class of $(m, s)$ and $S^{-1}M$ be
+$\frac{m}{s}$) the equivalence class of $(m, s)$ and by $S^{-1}M$
 the set of all equivalence classes.
````

### MC-STK-ERR-0418

`algebra.tex` — algebra.tex:1140-1156; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1150-L1154) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,5 +1,5 @@
-Define the addition and scalar
-multiplication as follows
+For $a \in A$, $m, n \in M$, and $s, t \in S$, define addition and scalar
+multiplication by
 $$
 m/s + n/t = (mt + ns)/st,\quad
-m/s\cdot n/t = mn/st
+(a/s)\cdot(m/t) = am/st
````

### MC-STK-ERR-0419

`algebra.tex` — algebra.tex:1172; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1172) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $S \subset R$ a multiplicative subset.
+Let $S \subset R$ be a multiplicative subset.
````

### MC-STK-ERR-0420

`algebra.tex` — algebra.tex:1187; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1187) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a given R-linear map
+a given $R$-linear map
````

### MC-STK-ERR-0421

`algebra.tex` — algebra.tex:1308; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1308) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-given a $A$-module M
+given an $A$-module $M$
````

### MC-STK-ERR-0422

`algebra.tex` — algebra.tex:1322; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1322) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-independent the choice
+independent of the choice
````

### MC-STK-ERR-0423

`algebra.tex` — algebra.tex:1327-1329; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1327) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an $A$ homomorphism
+an $A$-module homomorphism
````

### MC-STK-ERR-0424

`algebra.tex` — algebra.tex:1375-1377; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1375) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the preceding Corollary
+the preceding Lemma
````

### MC-STK-ERR-0425

`algebra.tex` — algebra.tex:1769-1774; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1771-L1774) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(j\circ j') \circ g$
+$(j'\circ j) \circ g$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(j'\circ j) \circ g'
+$(j\circ j') \circ g'
````

### MC-STK-ERR-0426

`algebra.tex` — algebra.tex:1771-1772; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1772) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-satisfies the universal properties
+satisfy the universal properties
````

### MC-STK-ERR-0427

`algebra.tex` — algebra.tex:1807-1809; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1808) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an $R$-module T
+an $R$-module $T$
````

### MC-STK-ERR-0428

`algebra.tex` — algebra.tex:1899-1902; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1901) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-isomorphic as both as $A$-module and $B$-module
+isomorphic both as $A$-modules and as $B$-modules
````

### MC-STK-ERR-0429

`algebra.tex` — algebra.tex:2057-2060; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2059) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-to be {\it flat} $R$-module
+to be a {\it flat} $R$-module
````

### MC-STK-ERR-0430

`algebra.tex` — algebra.tex:19523-19527; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19526) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a direct summand of $P_{2, f}$
+a direct summand of $P_{1, f}$
````

### MC-STK-ERR-0431

`algebra.tex` — algebra.tex:2606-2612; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2611) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then $x + fy$ is not contained in $\mathfrak p_1, \ldots, \mathfrak p_s$.
+Then $x + fy$ does not belong to any of $\mathfrak p_1, \ldots, \mathfrak p_s$.
````

### MC-STK-ERR-0432

`algebra.tex` — algebra.tex:2728-2737; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2736) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A_1B = B A_1 = f$
+$A_1B = B A_1 = fI_m$
````

### MC-STK-ERR-0433

`algebra.tex` — algebra.tex:2738-2743; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2741) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A_1^{ij}$
+$A_1^{jk}$
````

### MC-STK-ERR-0434

`algebra.tex` — algebra.tex:2860-2868; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2867) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$P = t^n + a_1 t^{n - 1} + \ldots + a_n \in R[T]$
+$P = T^n + a_1 T^{n - 1} + \ldots + a_n \in R[T]$
````

### MC-STK-ERR-0435

`algebra.tex` — algebra.tex:2906-2911; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2910) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\sum_{j = 1, \ldots, n}
+\sum_{j = 1}^{n}
````

### MC-STK-ERR-0436

`algebra.tex` — algebra.tex:3029-3035; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3033-L3034) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Since 1 $\notin I$ for all $I \in A$, the union does not contain
-1 and thus is proper.
+Since $1 \notin I$ for all $I \in A$, the union does not contain
+$1$ and thus is proper.
````

### MC-STK-ERR-0437

`algebra.tex` — algebra.tex:3072-3075; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3075) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-either $I$ of $J$ is in $\mathfrak{p}$
+either $I \subset \mathfrak{p}$ or $J \subset \mathfrak{p}$
````

### MC-STK-ERR-0438

`algebra.tex` — algebra.tex:3177-3183; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3179-L3180) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-let $\mathfrak p$
+let $\mathfrak p$ be
 the inverse image
````

### MC-STK-ERR-0439

`algebra.tex` — algebra.tex:3293-3297; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3297) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$U \cap V = \bigcup D(f_ig_j)$
+$U \cap V = \bigcup_{1 \leq i \leq n,\ 1 \leq j \leq m} D(f_i g_j)$
````

### MC-STK-ERR-0440

`algebra.tex` — algebra.tex:21138-21156; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21145-L21151) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M_i \otimes_R M_j$
+M_i \otimes_R N_j$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$b : M_{j''} \to M_{j'}$
+$b : N_{j''} \to N_{j'}$
````

### MC-STK-ERR-0441

`algebra.tex` — algebra.tex:3380-3396; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3388) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The equivalence (1) and (2)
+The equivalence of (1) and (2)
````

### MC-STK-ERR-0442

`algebra.tex` — algebra.tex:3527-3537; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3533-L3535) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
 Namely, there is an obvious ring map
 $F \to S_\mathfrak q \otimes_{R_\mathfrak p} \kappa(\mathfrak p)$
-which is easily seen to be isomorphic to $F \to F_{\overline{\mathfrak q}}$.
+which, under the displayed isomorphism, identifies with $F \to F_{\overline{\mathfrak q}}$.
````

### MC-STK-ERR-0443

`algebra.tex` — algebra.tex:36369-36375; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36374) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\overline{J} = J/\mathfrak m_R \cap J \subset \overline{S}$
+$\overline{J} = J/(\mathfrak m_R S \cap J) \subset \overline{S}$
````

### MC-STK-ERR-0444

`algebra.tex` — algebra.tex:36389-36396; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36391-L36392) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S/(f_1, \ldots, f_{\overline{c}}) + IS$
+$S/((f_1, \ldots, f_{\overline{c}}) + IS)$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S/(f_1, \ldots, f_{\overline{c}}) + IS
+$S/((f_1, \ldots, f_{\overline{c}}) + IS)
````

### MC-STK-ERR-0445

`algebra.tex` — algebra.tex:37000-37010; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37001-L37009) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak q' \subset S$
+$\mathfrak q' \subset S'$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S_g \to S_{gg'}$
+$S_g \to S'_{gg'}$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R \to S_{gg'}$
+$R \to S'_{gg'}$
````

### MC-STK-ERR-0446

`algebra.tex` — algebra.tex:37021-37037 and 37760-37775; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37027-L37774) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{S}_{g_i}
+\overline{S}_{\overline{g}_i}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{S}_{g_i}
+\overline{S}_{\overline{g}_i}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{S}_{g_i}
+\overline{S}_{\overline{g}_i}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{S}_{g_i}
+\overline{S}_{\overline{g}_i}
````

### MC-STK-ERR-0447

`algebra.tex` — algebra.tex:3679-3683; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3680-L3681) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-is
+is an
 invertible element
````

### MC-STK-ERR-0448

`algebra.tex` — algebra.tex:3718-3725; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3725) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-generates $M_{st}$
+generate $M_{st}$
````

### MC-STK-ERR-0449

`algebra.tex` — algebra.tex:37934-37945; 38017-38025; 38131-38140; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37945-L38138) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega_{P/R} \otimes_R S
+\Omega_{P/R} \otimes_P S
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\NL_{P/R} \otimes_R S
+\NL_{P/R} \otimes_P S
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega_{P/R} \otimes_R S
+\Omega_{P/R} \otimes_P S
````

### MC-STK-ERR-0450

`algebra.tex` — algebra.tex:37946-37962; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37957) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{d}\lambda \mu
+\text{d}(\lambda\mu)
````

### MC-STK-ERR-0451

`algebra.tex` — algebra.tex:21748-21760; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21757) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-since $\Ker(\varphi)$
+since $\Im(\varphi)$
````

### MC-STK-ERR-0452

`algebra.tex` — algebra.tex:21930-21946; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21937-L21944) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim_{j \in J}
+\colim_{j \in I}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim_{j \in J} (Q \otimes_R M_j) \subset \colim_{j \in J}
+\colim_{j \in I} (Q \otimes_R M_j) \subset \colim_{j \in I}
````

### MC-STK-ERR-0453

`algebra.tex` — algebra.tex:22062-22071; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22068) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a countable,
+is a countable set,
````

### MC-STK-ERR-0454

`algebra.tex` — algebra.tex:22062-22075; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22073-L22074) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 if $\ell$
-is odd
+is even
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-if $\ell$ is even
+if $\ell$ is odd
````

### MC-STK-ERR-0455

`algebra.tex` — algebra.tex:22482-22497; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22491-L22492) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 \Im(P
-\otimes_R S \to M \otimes_R S)
+\otimes_R S \to (M/M_{\alpha}) \otimes_R S)
````

### MC-STK-ERR-0456

`algebra.tex` — algebra.tex:22503-22512; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22508-L22512) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-ordinal $S$
+ordinal $\gamma$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\alpha \in S$
+$\alpha \in \gamma$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(M_{\alpha})_{\alpha \in S}$
+$(M_{\alpha})_{\alpha \in \gamma}$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$M = \bigoplus_{\alpha + 1 \in S}
+$M = \bigoplus_{\alpha + 1 \in \gamma}
````

### MC-STK-ERR-0457

`algebra.tex` — algebra.tex:3895-3905; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3902-L3903) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-An idempotent
+A nonzero idempotent
 is not nilpotent
````

### MC-STK-ERR-0458

`algebra.tex` — algebra.tex:4017-4022; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4020) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we have see
+we see
````

### MC-STK-ERR-0459

`algebra.tex` — algebra.tex:38564-38575; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38572) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\dim(S_{\mathfrak m'})
+$\dim(S'_{\mathfrak m'})
````

### MC-STK-ERR-0460

`algebra.tex` — algebra.tex:38580-38586; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38585) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g \not \in \mathfrak m'$
+$g' \not \in \mathfrak m'$
````

### MC-STK-ERR-0461

`algebra.tex` — algebra.tex:38898-38907; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38905) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a geometrically reduced
+is geometrically reduced
````

### MC-STK-ERR-0462

`algebra.tex` — algebra.tex:4353-4356; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4355) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f_1, f_2, \ldots f_n\in R$
+$f_1, f_2, \ldots, f_n \in R$
````

### MC-STK-ERR-0463

`algebra.tex` — algebra.tex:38869-38883; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38880-L38882) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x^p + y^2 + \alpha
+x^p + y^2 + t
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(y, x^p + \alpha)$
+(y, x^p + t)$
````

### MC-STK-ERR-0464

`algebra.tex` — algebra.tex:4550-4556; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4556) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-hence it is a field
+hence $R_{\mathfrak p}$ is a field
````

### MC-STK-ERR-0465

`algebra.tex` — algebra.tex:4622-4626; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4624) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is contained in $R \setminus \mathfrak q_i$
+lies in $R \setminus \mathfrak q_i$
````

### MC-STK-ERR-0466

`algebra.tex` — algebra.tex:38998-39013; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39012) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\bigoplus\nolimits_{j = 1}^m
+\bigoplus\nolimits_{j = 1}^n
````

### MC-STK-ERR-0467

`algebra.tex` — algebra.tex:39102-39110; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39109) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-these tensor product are
+these tensor products are
````

### MC-STK-ERR-0468

`algebra.tex` — algebra.tex:4758-4773; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4770-L4771) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-\item every standard open $D(f) \subset X$ is closed, and
-\item add more here.
+\item every standard open $D(f) \subset X$ is closed.
````

### MC-STK-ERR-0469

`algebra.tex` — algebra.tex:39186-39195; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39193) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim_{\kappa(m)}
+\dim_{\kappa(\mathfrak m)}
````

### MC-STK-ERR-0470

`algebra.tex` — algebra.tex:39434-39444; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39440) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item we have $\mathfrak p S_{\mathfrak q}
+\item $\mathfrak p S_{\mathfrak q}
````

### MC-STK-ERR-0471

`algebra.tex` — algebra.tex:39460-39466; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39464) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a finite products of fields
+a finite product of fields
````

### MC-STK-ERR-0472

`algebra.tex` — algebra.tex:39488-39501; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39496-L39497) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Replace $S$ by $S_g$ again we may
+Replacing $S$ by $S_g$ again, we may
 assume
````

### MC-STK-ERR-0473

`algebra.tex` — algebra.tex:39533-39538; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39536) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist an idempotent
+there exists an idempotent
````

### MC-STK-ERR-0474

`algebra.tex` — algebra.tex:39684-39747; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39744) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\text{Res}_x(f, g)$
+$\text{Res}_x(g, h)$
````

### MC-STK-ERR-0475

`algebra.tex` — algebra.tex:4868-4886; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4877) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-In this case, $\mathfrak p$ must be generated by nonconstant polynomials
+In this case, if $\mathfrak p = (0)$ there is nothing more to prove. Otherwise, $\mathfrak p$ contains nonconstant polynomials
````

### MC-STK-ERR-0476

`algebra.tex` — algebra.tex:4899-4904; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4904) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-obtain $p = af + bg$ for $p, a, b \in k[x]$.
+obtain $p = af + bg$ for $0 \ne p \in k[x]$ and $a, b \in k[x, y]$.
````

### MC-STK-ERR-0477

`algebra.tex` — algebra.tex:4905-4910; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4907) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for $ah, bh \in k[x]$
+for $ah, bh \in k[x, y]$
````

### MC-STK-ERR-0478

`algebra.tex` — algebra.tex:4952-4959; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4958) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$h(z) = c_1z + c_0$
+$g(z) = c_1z + c_0$
````

### MC-STK-ERR-0479

`algebra.tex` — algebra.tex:4956-4963; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4961) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f(z) = A(z)^2h(z)+b_1B(z)+b_0A(z)$
+$f(z) = A(z)^2h(z)+b_1B(z)+b_0A(z)+a$
````

### MC-STK-ERR-0480

`algebra.tex` — algebra.tex:4981-4987; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4981) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for a ring T and a
+for a ring $T$ and a
````

### MC-STK-ERR-0481

`algebra.tex` — algebra.tex:4989-4993; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4990) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$D(f)\subset T$
+$D(f)\subset \Spec(T)$
````

### MC-STK-ERR-0482

`algebra.tex` — algebra.tex:5042-5050; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5049) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-2a-a
+2a-2
````

### MC-STK-ERR-0483

`algebra.tex` — algebra.tex:5057-5067; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5060-L5062) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
 is the localization of $\mathbf{Q}[z]$
-at the maximal ideal $(z-a)$
+at the element $z-a$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Any localization $S^{-1}R$
+Any proper localization $S^{-1}R$
````

### MC-STK-ERR-0484

`algebra.tex` — algebra.tex:5063-5082; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5079-L5080) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-that $(z-a)^{k + \ell}$ can only be in $R$ for $k = \ell = 0$; indeed, if
-$a = 1/2$, then this is in $R$ as long as $k + \ell$ is even.
+that $(z-a)^n$ can belong to $R_a$ only for $n = 0$; indeed, if
+$a = 1/2$, then it belongs to $R_a$ whenever $n$ is even.
````

### MC-STK-ERR-0485

`algebra.tex` — algebra.tex:23670-23691; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23688) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-N \otimes_{R/} M/IM
+N \otimes_{R/I} M/IM
````

### MC-STK-ERR-0486

`algebra.tex` — algebra.tex:23900-23918; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23917) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-surjection on cohomology
+surjection on homology
````

### MC-STK-ERR-0487

`algebra.tex` — algebra.tex:24218-24235; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24226) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-has a kernel
+has a nonzero kernel
````

### MC-STK-ERR-0488

`algebra.tex` — algebra.tex:24494-24500; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24498) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-both $R$ and $S$
+both $M$ and $S$
````

### MC-STK-ERR-0489

`algebra.tex` — algebra.tex:24501-24510; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24504) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$x_\alpha \in A$
+$x_\alpha \in M$
````

### MC-STK-ERR-0490

`algebra.tex` — algebra.tex:24548-24562; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24559) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\text{Tor}_1^S(IS, M)
+$\text{Tor}_1^S(S/IS, M)
````

### MC-STK-ERR-0491

`algebra.tex` — algebra.tex:5275-5285; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5281) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-ideals that not principal
+ideals that are not principal
````

### MC-STK-ERR-0492

`algebra.tex` — algebra.tex:5329-5338; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5335) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r32/candidate.manifest.json)

prior_acceptance_replayed_against_frozen_authority

Adverse evidence / qualification: The original provisional-acceptance status is preserved; R32 performs the previously missing exact materialization only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-radical ideas
+radical ideals
````
