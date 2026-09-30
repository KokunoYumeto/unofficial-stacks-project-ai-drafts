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

### MC-STK-ERR-1594

`algebra.tex` — 17587-17589, 17601-17602; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17587-L17602) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The chosen alpha:F→G induces precomposition Hom(G,N)→Hom(F,N), hence the same direction on cohomology. The displayed induced arrow has its source and target reversed. Both chosen lifts F→G induce homotopic maps in the contravariant direction Hom(G,N)→Hom(F,N). Match the proof to the corrected display.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
+H^i(\Hom_R(G_{\bullet}, N))
+\longrightarrow
 H^i(\Hom_R(F_{\bullet}, N))
-\longrightarrow
-H^i(\Hom_R(G_{\bullet}, N))
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-maps $\Hom_R(F_\bullet, N) \to
-\Hom_R(G_\bullet, N)$
+maps $\Hom_R(G_\bullet, N) \to
+\Hom_R(F_\bullet, N)$
````

### MC-STK-ERR-1595

`algebra.tex` — 17594; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17594) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The induced identity is on the cohomology of the Hom cochain complex, named H^i(alpha) in the displayed construction; H_i(alpha) instead denotes homology of the original chain map.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$H_i(\alpha)$
+$H^i(\alpha)$
````

### MC-STK-ERR-1596

`algebra.tex` — 17615, 17616, 17617; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17615-L17617) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

Precomposition reverses order: alpha*:H(G,N)→H(F,N), beta*:H(F,N)→H(G,N); alpha* after beta* equals (beta after alpha)* on H(F,N). The composite beta after alpha is an endomorphism of F and lifts id_M1, so it is homotopic to id_F. The swapped composition is handled by the next sentence.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H^i(\alpha \circ \beta)
+H^i(\beta \circ \alpha)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H^i(\alpha \circ \beta)
+H^i(\beta \circ \alpha)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{id}_{G_{\bullet}}
+\text{id}_{F_{\bullet}}
````

### MC-STK-ERR-1597

`algebra.tex` — 13073, 13152; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13073-L13152) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

Each immediately preceding short exact sequence has endpoints M-prime and M-double-prime. Since the quotient is finite free, the splitting is M≅M-prime⊕M-double-prime. The identical typo occurs in both the PID example and local-ring K0 proof; both loci are explicitly included.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M' \oplus M'
+M' \oplus M''
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M' \oplus M'
+M' \oplus M''
````

### MC-STK-ERR-1599

`algebra.tex` — 26495; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26495) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The subject a commutative diagram is singular.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist a commutative diagram
+there exists a commutative diagram
````

### MC-STK-ERR-1600

`algebra.tex` — 27084; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27084) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The resolution maps have the specified property; to is a typographical substitution for the article.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-have to property that
+have the property that
````

### MC-STK-ERR-1601

`algebra.tex` — 27704; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27704) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

The proof assumes injectivity at i and shows the quotient with i+1 variables and equations is a field. Its surjective unital map is psi_(i+1), so that map is now injective.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\psi_i$
+$\psi_{i + 1}$
````

### MC-STK-ERR-1602

`algebra.tex` — 17466; mathematical source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17466) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

alpha_i has target G_i. The outgoing differential there is d_(G,i):G_i→G_(i-1); d_(G,i-1) is not composable with alpha_i.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-d_{G, i-1} \circ \alpha_i
+d_{G, i} \circ \alpha_i
````

### MC-STK-ERR-1603

`algebra.tex` — 17562; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17562) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

Single-word spelling in the Ext-definition footnote; the line break before of remains.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in stead
+instead
````

### MC-STK-ERR-1604

`algebra.tex` — 17610; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17610) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r51/candidate.manifest.json)

Supply the infinitival to in Choose beta to be a map.

Adverse evidence / qualification: The exact type/domain argument is recorded in the bound review.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be a map inducing
+to be a map inducing
````

### MC-STK-ERR-1906

`algebra.tex` — 139; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L139) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The two ideals I and J require the plural noun ideals. The prime-product assertion, its ring and every hypothesis remain unchanged.

Adverse evidence / qualification: This is a spelling/grammar correction; the prime-product statement is already correct. No new result is inferred from this edit.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-are ideal,
+are ideals,
````

### MC-STK-ERR-1907

`algebra.tex` — 1021, 1022; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1021-L1022) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing given-construction and the conventional module compound, with a comma before the main clause. Both reports identify the same grammatical omission.

Adverse evidence / qualification: Keep the arbitrary index set J, including the empty case, and all three direct sums. The two proposed connecting words express the same data; given is selected once.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-In other words, exact sequences
+In other words, given exact sequences
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $R$ modules we have to show that
+of $R$-modules, we have to show that
````

### MC-STK-ERR-1908

`algebra.tex` — 1341; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1341) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The paragraph fixes A and localization at S in A; bind the exactness proposition to that same ring.

Adverse evidence / qualification: This restores the existing base ring rather than imposing a new ring hypothesis. All maps and the exactness proof retain their original coordinates.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $R$-modules. Then
+of $A$-modules. Then
````

### MC-STK-ERR-1909

`algebra.tex` — 1431; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1431) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The submodule N prime lies in the localization of an A-module and is closed under S inverse A scalars, which justify multiplication by 1/s.

Adverse evidence / qualification: The existing proof has not introduced R in this scope. Preserve A, S, M, N and N prime rather than renaming the whole paragraph.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an $S^{-1}R$-submodule
+an $S^{-1}A$-submodule
````

### MC-STK-ERR-1910

`algebra.tex` — 1371; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1371) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The result being proved is in a lemma environment with its existing stable label.

Adverse evidence / qualification: No statement, label or proof is changed, and the distinct following reference already fixed by MC-STK-ERR-0424 remains intact.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The corollary then follows.
+The lemma then follows.
````

### MC-STK-ERR-1911

`algebra.tex` — 1308-1310; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1308-L1310) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The earlier universal-property lemma already proves the property declared unavailable here. Correct that stale assertion while retaining the explicit maps f and g. Their construction, denominator independence and both inverse identities now follow from the stated universal property with exact source and target modules.

Adverse evidence / qualification: Do not remove the coordinate formulas or substitute a ring-localization statement. The independently changed substring does not overlap the prior article/math-mode repair or the prior independent-of repair.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-we have not proved any
-universal property for $S^{-1}M$. Hence we cannot reason
-as in the preceding proof; we have to construct the isomorphism explicitly.
+the universal property of
+Lemma \ref{lemma-universal-property-localization-module} is available.
+We give an explicit construction of the isomorphism.
````

### MC-STK-ERR-1912

`algebra.tex` — 1602; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1602) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the article an before the spoken symbol i prime.

Adverse evidence / qualification: The common upper index, finite generating set and filtered-colimit argument are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-find a $i'
+find an $i'
````

### MC-STK-ERR-1913

`algebra.tex` — 1759, 1761; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1759-L1761) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the naming construction and split the two independent clauses.

Adverse evidence / qualification: The natural map pi, elementary tensors and their generating property remain unchanged; the adjacent arbitrary-codomain clarification is a separate group.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote the image
+Denote the image by
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-y$, then these elements generate
+y$. Then these elements generate
````

### MC-STK-ERR-1914

`algebra.tex` — 2114; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2114) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Introduce the definition of m with a complete sentence after the display.

Adverse evidence / qualification: Every summand, numerator, denominator and the following injectivity argument is preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Where $m =
+Here $m =
````

### MC-STK-ERR-1915

`algebra.tex` — 2388, 2389; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2388-L2389) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the tensor-algebra symbol actually defined in this section on both sides of the localization identity, and use the adverb in the adjacent sentence.

Adverse evidence / qualification: The localized algebra and the base-changed tensor algebra are unchanged. This is notation/wording consistency, not evidence of a false localization theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S^{-1}T_R(M) = T_{S^{-1}R}(S^{-1}M)
+S^{-1}\text{T}_R(M) = \text{T}_{S^{-1}R}(S^{-1}M)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Similar for symmetric and exterior algebras.
+Similarly for symmetric and exterior algebras.
````

### MC-STK-ERR-1916

`algebra.tex` — 2768; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2768) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The indicated invertible row and column operations change bases of the two free modules over the current ring. This follows, and is distinct from, the preceding localization R→R_a.

Adverse evidence / qualification: Keep the actual scalar extension R→R_a, the unit pivot, both ranks and the ensuing induction. Only the name of the basis operation changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-do a base change on both
+make a change of basis in both
````

### MC-STK-ERR-1917

`algebra.tex` — 4179; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4179) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Part (2) gives a finite generating set of M of some cardinality m, independent of the fixed number n of covering opens. Use m for the free-module rank and retain every covering index 1 through n.

Adverse evidence / qualification: For a field R, the one-element cover f_1=1 and module M=R^2 satisfy the hypotheses with n=1, but no R-linear map R to R^2 is surjective: its image has dimension at most one. The finite-presentation conclusion is valid; the asserted intermediate rank was unjustified.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-0 \rightarrow K \rightarrow R^n \rightarrow M \rightarrow 0
+0 \rightarrow K \rightarrow R^m \rightarrow M \rightarrow 0
````

### MC-STK-ERR-1918

`algebra.tex` — 5391; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5391) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The ambient space is Spec(R) in every other condition and throughout the proof.

Adverse evidence / qualification: No X is introduced in the lemma; the identity for a finitely generated ideal is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$X \setminus V(I) = U$
+$\Spec(R) \setminus V(I) = U$
````

### MC-STK-ERR-1919

`algebra.tex` — 5426; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5426) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The preceding finite and the next inverse-image assertion require a union.

Adverse evidence / qualification: This is a noun substitution; the mathematical finite-union argument is already correct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-open of standard opens.
+union of standard opens.
````

### MC-STK-ERR-1920

`algebra.tex` — 5574; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5574) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The image f tensor 1 belongs to the fibre algebra, which is the domain and codomain of its multiplication map.

Adverse evidence / qualification: For A=R[x]/(x^2) the image of x in a nonzero fibre is not a scalar; the later formula f tensor 1 confirms the intended target.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\kappa(\mathfrak p)$, is just the image of $P(T)$ in
+$A\otimes_R\kappa(\mathfrak p)$, is just the image of $P(T)$ in
````

### MC-STK-ERR-1921

`algebra.tex` — 5601; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5601) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Elements is plural.

Adverse evidence / qualification: No mathematical quantifier or index changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-There exists elements
+There exist elements
````

### MC-STK-ERR-1922

`algebra.tex` — 5659; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5659) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The constructible-set decomposition is precisely lemma-constructible; the missing subject is also restored.

Adverse evidence / qualification: The quasi-compact-open lemma supports that decomposition indirectly, but does not state the invoked result. Three physical reports concern two edits to one sentence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the case $S = R[x]$. By Lemma \ref{lemma-qc-open} suffices
+the case $S = R[x]$. By Lemma \ref{lemma-constructible} it suffices
````

### MC-STK-ERR-1923

`algebra.tex` — 5773; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5773) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The verb construction requires for to name the displayed map.

Adverse evidence / qualification: Both alternatives in the reports express the same induced map; for makes the smallest change.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Write $f : Y \to X$ the induced
+Write $f : Y \to X$ for the induced
````

### MC-STK-ERR-1924

`algebra.tex` — 5898; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5898) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The vanishing locus and density argument take place in the prime spectrum.

Adverse evidence / qualification: R denotes the ring here; replacing the ambient space does not change the element f or the map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a proper closed subset of $R$.
+is a proper closed subset of $\Spec(R)$.
````

### MC-STK-ERR-1925

`algebra.tex` — 6038; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6038) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Formal power-series exponents here range over nonnegative integers.

Adverse evidence / qualification: Negative integer d is outside the displayed power-series definition; subsequent indices already begin at zero.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For each integer
+For each nonnegative integer
````

### MC-STK-ERR-1926

`algebra.tex` — 6083; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6083) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restores the article in the singular noun phrase.

Adverse evidence / qualification: The principal-ideal argument is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathbf{Z}$ is Noetherian ring
+$\mathbf{Z}$ is a Noetherian ring
````

### MC-STK-ERR-1927

`algebra.tex` — 6408; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6408) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restores the article before the vowel sound in nth.

Adverse evidence / qualification: No mathematical content changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a $n$th power
+is an $n$th power
````

### MC-STK-ERR-1928

`algebra.tex` — 7035-7036; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7035-L7036) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Uses grammatical assumptions for the already introduced ring and field.

Adverse evidence / qualification: The inclusion and finite-type hypothesis are preserved exactly.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Let $R$ be a Jacobson ring. Let $K$ be a field. Let $R \subset K$ and
-$K$ is of finite type over $R$. Then $R$ is a field and $K/R$
+Let $R$ be a Jacobson ring and let $K$ be a field. Assume
+$R\subset K$ and that $K$ is of finite type over $R$. Then $R$ is a field and $K/R$
````

### MC-STK-ERR-1929

`algebra.tex` — 7103; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7103) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restores the preposition introducing the spectrum map.

Adverse evidence / qualification: The source and target of f are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Write $f : Y \to X$ the induced
+Write $f : Y \to X$ for the induced
````

### MC-STK-ERR-1930

`algebra.tex` — 7179; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7179) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restores the noun and consistent singular agreement.

Adverse evidence / qualification: No hypothesis on image constructibility changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-images of a constructible is constructible.
+the image of a constructible set is constructible.
````

### MC-STK-ERR-1931

`algebra.tex` — 7181; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7181) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restores the notation-introduction preposition.

Adverse evidence / qualification: The set and notation are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\text{Constr}(X)$
+Denote by $\text{Constr}(X)$
````

### MC-STK-ERR-1932

`algebra.tex` — 7184; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7184) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restores the preposition in the second notation paragraph.

Adverse evidence / qualification: This is a distinct physical occurrence of the same grammar issue.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Write $f : Y \to X$ the induced
+Write $f : Y \to X$ for the induced
````

### MC-STK-ERR-1933

`algebra.tex` — 7191; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7191) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Corrects the reversed source and target, fixes the introductory fragment, and proves the diagram for Jacobson R with a finitely presented map using the exact hypotheses of the topology lemma.

Adverse evidence / qualification: Noetherianity originally supplies finite presentation from finite type. It is not simply dropped while keeping only finite type; the required finite-presentation hypothesis is stated explicitly in the generalization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-With notation as above. Assume that
+With notation as above, assume that
````

### MC-STK-ERR-1934

`algebra.tex` — 7250; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7250) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Primality is the exact hypothesis needed for the product inference.

Adverse evidence / qualification: The original arbitrary-ideal assertion is false: (xy) contains xy but neither x nor y. All three reports concern this one defect.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-any ideal containing
+any prime ideal containing
````

### MC-STK-ERR-1935

`algebra.tex` — 7259; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7259) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Removes the unmatched parenthesis from the polynomial ring.

Adverse evidence / qualification: Every variable and bracket defining the original ring is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}])$
+$k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}]$
````

### MC-STK-ERR-1936

`algebra.tex` — 7294; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7294) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restores the article to its grammatical position.

Adverse evidence / qualification: The separate field and orbit qualifications below address mathematical scope.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the image of irreducible an algebraic set
+the image of an irreducible algebraic set
````

### MC-STK-ERR-1937

`algebra.tex` — 7371; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7371) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Removes the duplicated determiner without changing the rank invariant.

Adverse evidence / qualification: Both reports concern the same grammatical defect.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-classified by the its rank
+classified by its rank
````

### MC-STK-ERR-1938

`algebra.tex` — 7382; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7382) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specifies the original base field whose characteristic is used.

Adverse evidence / qualification: The printed three-by-three trace example remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-For instance, $char = 3$
+For instance, if $k$ has characteristic $3$,
````

### MC-STK-ERR-1939

`algebra.tex` — 7799; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7799) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Adds the missing verb and repairs the sentence boundary.

Adverse evidence / qualification: These are grammatical defects; the nonzero-element requirement is adjudicated separately.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $S$ integral over $k$ and assume $S$ is a domain,
+Let $S$ be integral over $k$ and assume $S$ is a domain.
````

### MC-STK-ERR-1940

`algebra.tex` — 7800; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7800) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Requires the nonzero element at both choices and proves the injection needed for the finite-dimensional argument, as well as the domain-quotient implication.

Adverse evidence / qualification: Multiplication by zero is not surjective in a domain. The finite subalgebra is a domain because its inclusion in S is injective.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Take $s \in S$.
+Take a nonzero $s\in S$.
````

### MC-STK-ERR-1941

`algebra.tex` — 8032; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8032) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Corrects the indefinite article before the variable name.

Adverse evidence / qualification: The original spanning list through g to the power d is retained; it need not be a minimal list.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists an $d > 0$
+there exists a $d > 0$
````

### MC-STK-ERR-1942

`algebra.tex` — 8103; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8103) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Makes the verb agree with the singular subject the set.

Adverse evidence / qualification: Both received reports refer to this same agreement error.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-elements form a subring
+elements forms a subring
````

### MC-STK-ERR-1943

`algebra.tex` — 8297; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8297) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repairs the verb construction while keeping the original coordinate idempotent.

Adverse evidence / qualification: No coordinate, index or factor of the product is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $e_i = (0, \ldots, 0, 1, 0, \ldots, 0)$ the $i$th idempotent
+Let $e_i = (0, \ldots, 0, 1, 0, \ldots, 0)$ be the $i$th idempotent
````

### MC-STK-ERR-1944

`algebra.tex` — 8403; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8403) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The singular subject is set, and the spoken letter R begins with a vowel sound.

Adverse evidence / qualification: Both physical reports concern the same sentence; one mentions only agreement and the other also supplies the article correction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-over $I$ form a $R$-submodule of $S$.
+over $I$ forms an $R$-submodule of $S$.
````

### MC-STK-ERR-1945

`algebra.tex` — 9038-9039; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9038-L9039) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supplies parallel verbs in the statement as a grammatical copyedit.

Adverse evidence / qualification: The compressed original wording already determines the intended mathematical hypotheses; this edit is not a change to those hypotheses.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Suppose that $R$ is a ring, $0 \to M'' \to M' \to M \to 0$
-a short exact sequence, and $N$ an $R$-module. If $M$ is flat
+Suppose that $R$ is a ring, that $0\to M''\to M'\to M\to0$
+is a short exact sequence, and that $N$ is an $R$-module. If $M$ is flat
````

### MC-STK-ERR-1946

`algebra.tex` — 9100; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9100) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Adds the list-introducing colon consistently with the adjacent equivalence lemmas.

Adverse evidence / qualification: This is an editorial punctuation change only; the original mathematical list is unambiguous.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The following are equivalent
+The following are equivalent:
````

### MC-STK-ERR-1947

`algebra.tex` — 9132; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9132) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Replaces the adverb then by the definite article required by the tensor-product noun phrase.

Adverse evidence / qualification: The two physical reports refer to the same word; this is a single copyedit.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then tensor product
+the tensor product
````

### MC-STK-ERR-1948

`algebra.tex` — 9520-9522; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9520-L9522) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Uses the grammatical let construction for the same two original points.

Adverse evidence / qualification: Both reports concern the same sentence; their prime and point assignments are retained.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-topology. Denote $x \in X$ the point corresponding
-to $\mathfrak p$ and $x' \in X$ the point corresponding
+topology. Let $x\in X$ be the point corresponding
+to $\mathfrak p$ and $x'\in X$ the point corresponding
 to $\mathfrak p'$. Then we have:
````

### MC-STK-ERR-1949

`algebra.tex` — 9535, 9541; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9535-L9541) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Removes the extraneous article before the same named map in both definition items.

Adverse evidence / qualification: This is one physical report covering two parallel copyedits, not two independent mathematical corrections.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We say a $\varphi : R \to S$ satisfies
+We say $\varphi : R \to S$ satisfies
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We say a $\varphi : R \to S$ satisfies
+We say $\varphi : R \to S$ satisfies
````

### MC-STK-ERR-1950

`algebra.tex` — 9551; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9551) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Uses the past participle required after have.

Adverse evidence / qualification: The two reports have exactly the same source word and correction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we have see
+we have seen
````

### MC-STK-ERR-1951

`algebra.tex` — 9558; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9558) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Adds terminal punctuation to the list item.

Adverse evidence / qualification: This is punctuation only; the referenced going-down theorem is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemma \ref{lemma-flat-going-down}
+Lemma \ref{lemma-flat-going-down}.
````

### MC-STK-ERR-1952

`algebra.tex` — 10431; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10431) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Makes the root-field test defined for the arbitrary base field in the statement, supplies characteristic zero explicitly, and proves all original field injections, finite coefficient capture, two-sided scalar comparisons and localization maps.

Adverse evidence / qualification: The source defines k^(1/p) only in positive characteristic. Restricting the entire theorem to positive characteristic would unnecessarily weaken its valid scope. Testing all finite height-one purely inseparable extensions suffices, but no claim that only extensions of degree p suffice is made.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-\item $k^{1/p} \otimes_k S$ is reduced,
+\item if $\operatorname{char}(k)=p>0$, then
+$k^{1/p}\otimes_k S$ is reduced; if
+$\operatorname{char}(k)=0$, then $S$ is reduced,
````

### MC-STK-ERR-1953

`algebra.tex` — 11489, 11577; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11489-L11577) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Resolves both reported occurrences with the same established separably closed terminology used by the irreducibility and field tests.

Adverse evidence / qualification: The original conclusions do not require the stronger algebraically closed hypothesis. Both physical loci of this one report are included exactly once.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-separably algebraically closed
+separably closed
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-separably algebraically closed
+separably closed
````

### MC-STK-ERR-1954

`algebra.tex` — 11666; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11666) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Removes the extraneous preposition in the geometric integrality definition, reported twice.

Adverse evidence / qualification: The tensor itself is the ring. Its nonzero-domain requirement is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $S \otimes_k k'$
+$S \otimes_k k'$
````

### MC-STK-ERR-1955

`algebra.tex` — 11671; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11671) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Corrects the directional preposition in the reformulation sentence, reported twice.

Adverse evidence / qualification: This is a wording correction; the separate equivalence proof supplies its mathematical content.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in a question
+into a question
````

### MC-STK-ERR-1956

`algebra.tex` — 11804; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11804) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Corrects the second summation to indices 1 through d and makes nonzero inversion explicit. Supplies the missing prime-localization contradiction, unit leading coefficient and complete original-to-monic polynomial comparison.

Adverse evidence / qualification: The i=0 coefficient is already retained in 1-t_0 and must not be counted again. The original scalar factor is retained; zero is not assigned an inverse.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $x \in K$.
+Let $x \in K^*$.
````

### MC-STK-ERR-1957

`algebra.tex` — 11894; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11894) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Corrects the genuine zero-localization boundary and proves the quotient, residue-field and localization assertions with the original maps. The source multiplicative-subset definition allows zero.

Adverse evidence / qualification: Localization at a set containing zero gives the zero ring, which is not a domain and therefore not a valuation ring. This was checked directly against source definitions 1042-1047 and lemma-localization-zero, unlike a conjectural convention objection.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-any localization of $A$.
+any nonzero localization of $A$.
````

### MC-STK-ERR-1958

`algebra.tex` — 11963; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11963) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Corrects the article before the consonant sound in totally.

Adverse evidence / qualification: Only the article is changed; the original ordered-group definition and order direction are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-An {
+A {
````

### MC-STK-ERR-1959

`algebra.tex` — 12188; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12188) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Gives the ideal hypothesis its own complete sentence.

Adverse evidence / qualification: The same ring and ideal hypotheses are retained; this is a grammatical correction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Suppose that $R$ is Noetherian, $I \subset R$ an ideal.
+Suppose that $R$ is Noetherian. Let $I \subset R$ be an ideal.
````

### MC-STK-ERR-1960

`algebra.tex` — 12539; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12539) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Names the newly chosen maximal ideal m instead of rebinding the existing annihilator I.

Adverse evidence / qualification: The existing element, annihilator, quotient isomorphism and simplicity argument are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $I \subset \mathfrak m$ be a maximal ideal containing $I$.
+Let $\mathfrak m$ be a maximal ideal containing $I$.
````

### MC-STK-ERR-1961

`algebra.tex` — 12798, 12799, 12817; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12798-L12817) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repairs the two wording defects and completes the original Artinian-to-finite-length argument with actual quotient maps and strict inverse-image chains.

Adverse evidence / qualification: The reduction to local factors is justified by the explicit original product map and surjective component maps; no finite-dimensional layer is assumed without proving it.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-equal to product
+equal to the product
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-at maximal ideals
+at its maximal ideals
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sub vector spaces
+vector subspaces
````

### MC-STK-ERR-1962

`algebra.tex` — 12951; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12951) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The evaluation of the entire polynomial ring in A requires all variable images to lie in A. The complementary case selects a least value among the nonzero images; zero images cause no valuation-domain exception.

Adverse evidence / qualification: One variable image in A is insufficient. The editorial note proves the original chart comparison and both cases, including n=0, without changing the lemma or replacing its proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-If the image $\lambda_i \in \kappa(\mathfrak q)$
+If every image $\lambda_i \in \kappa(\mathfrak q)$
````

### MC-STK-ERR-1963

`algebra.tex` — 13017; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13017) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Ordinary finite free powers have nonnegative integer ranks. Every finite module has such a quotient presentation, including the zero module at rank zero.

Adverse evidence / qualification: This is not a restriction to positive ranks and does not exclude the zero module. Negative module ranks are not defined in the displayed construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-all integers
+all nonnegative integers
````

### MC-STK-ERR-1964

`algebra.tex` — 13080, 13087; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13080-L13087) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The defining exact-sequence relation subtracts the ideal class from the ring class. State the nonzero choice of torsion invariant factors needed for the source identification of each ideal with R.

Adverse evidence / qualification: A zero factor has quotient R and contributes [R], so the ideal-isomorphism justification would fail without the stated choice. Nonzero units and the empty list are allowed. The editorial note retains all zero-factor contributions before explaining the permitted choice.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$M = R^{\oplus r} \oplus R/(d_1) \oplus \ldots \oplus R/(d_k)$.
+$M = R^{\oplus r} \oplus R/(d_1) \oplus \ldots \oplus R/(d_k)$ with $d_i \ne 0$ for every $i$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$[R/(d_i)] = [(d_i)]-[R] = 0$
+$[R/(d_i)] = [R]-[(d_i)] = 0$
````

### MC-STK-ERR-1965

`algebra.tex` — 13227; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13227) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Removes the comma separating two coordinated objects.

Adverse evidence / qualification: No mathematical convention or graded-module definition changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-definitions, and lemmas
+definitions and lemmas
````

### MC-STK-ERR-1966

`algebra.tex` — 13247; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13247) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Names the scalar action that gives the asserted graded S-module. The degree n+e formula is proved in the separate editorial note using the original twist convention.

Adverse evidence / qualification: Multiplication can mean scalar multiplication, so this is a terminology clarification rather than a demonstrated false assertion of an internal algebra structure.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the multiplication
+the $S$-action
````

### MC-STK-ERR-1967

`algebra.tex` — 13338; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13338) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Names the base being integrally closed and its original ambient Laurent ring in the conventional order.

Adverse evidence / qualification: The surrounding argument identifies the intended set correctly. This is a terminology clarification, not a change to the ring C or a claim that the mathematical proof is false.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of $S[t, t^{-1}]$ over $R[t, t^{-1}]$
+of $R[t, t^{-1}]$ in $S[t, t^{-1}]$
````

### MC-STK-ERR-1968

`algebra.tex` — 13377; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13377) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The homogeneous-product criterion for primality requires a proper ideal. A highest-component argument proves the corrected criterion for the original grading and for the receiving integer grading.

Adverse evidence / qualification: The unit ideal satisfies the printed product implication and is not prime. This is an actual missing qualification, not a stronger replacement for the source theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a homogeneous ideal
+a proper homogeneous ideal
````

### MC-STK-ERR-1969

`algebra.tex` — 13407; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13407) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Corrects the compound noun without changing the explicitly stated scalar ring S_(f).

Adverse evidence / qualification: The degree-zero part need not be an S_f-submodule; this copyedit does not assert otherwise.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sub module
+submodule
````

### MC-STK-ERR-1970

`algebra.tex` — 13662, 13663; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13662-L13663) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The homogeneous core is generated by elements already in p, so it is contained in p. This direction proves the needed product inclusion and also proves properness. Adds the missing verb.

Adverse evidence / qualification: The following minimal-prime proof already uses q contained in p. The reversed printed containment is not used to alter that receiving proof; the exact argument is recorded in the editorial note.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-either $f$ or $g$ in
+either $f$ or $g$ is in
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak p \subset \mathfrak q$
+$\mathfrak q \subset \mathfrak p$
````

### MC-STK-ERR-1971

`algebra.tex` — 13682; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13682) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supplies the missing main verb in the second assertion proof.

Adverse evidence / qualification: Passing to S/I preserves the graded quotient and prime correspondence. The mathematical argument remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The second because
+The second follows because
````

### MC-STK-ERR-1972

`algebra.tex` — 13726; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13726) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The module generators may have negative degrees, so reducing their exponents modulo deg(f) can leave a negative denominator exponent. State its meaning using a nonnegative power in the numerator of the actual localization.

Adverse evidence / qualification: For M=k[t](1), f=t and its generator x of degree minus one, the listed residue exponents force e=-1 although the degree-zero localization is nonzero and generated by tx. The theorem is correct; a reading that silently forbids this list entry would not prove it.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$e_i < \deg(f)$.
+$e_i < \deg(f)$; a fraction with $e < 0$ denotes its numerator multiplied by $f^{-e}$.
````

### MC-STK-ERR-1973

`algebra.tex` — 13745-13747, 13748, 13750, 13756, 13760-13761; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13745-L13761) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Positive-degree homogeneous relations preserve the original R as S_0 while their localization still gives exactly R prime. Polynomial lifts make the module relation matrix defined. Specified degrees cover zero entries, and r>=1 makes each column maximum defined, including M=0. Two grammar fixes are included.

Adverse evidence / qualification: The original minimal-degree construction fails for R=Z and R prime=Z/(2): it gives S_0=Z/(2). A quotient class k_ij is not itself a polynomial to which the printed homogenization applies. The full corrected ring and module comparisons are proved separately with every t-power retained; the lemma statement is not weakened.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-For an element $g \in R[x_1, \ldots, x_n]$ denote
-$\tilde g \in R[X_0, \ldots, X_n]$ the element homogeneous of minimal
+For an element $g \in R[x_1, \ldots, x_n]$ choose a homogeneous
+polynomial $\tilde g \in R[X_0, \ldots, X_n]$ of a specified positive
 degree such that $g = \tilde g(1, x_1, \ldots, x_n)$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ldots, X_n]$ generated
+\ldots, X_n]$ be generated
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote $f$ the image
+denote by $f$ the image
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we choose a presentation
+we choose a presentation with $r \geq 1$
````

````diff
--- original
+++ replacement
@@ -1,2 +1,4 @@
-with $k_j = (k_{1j}, \ldots, k_{rj})$. Let $d_{ij} = \deg(\tilde k_{ij})$.
-Set $d_j = \max\{d_{ij}\}$. Set $K_{ij} = X_0^{d_j - d_{ij}}\tilde k_{ij}$
+with $k_j = (k_{1j}, \ldots, k_{rj})$. Choose polynomial lifts $h_{ij}$
+of the $k_{ij}$ and assign positive degrees $d_{ij}$ to their
+homogenizations $\tilde h_{ij}$, including zero entries.
+Set $d_j = \max\{d_{ij}\}$. Set $K_{ij} = X_0^{d_j - d_{ij}}\tilde h_{ij}$
````

### MC-STK-ERR-1974

`algebra.tex` — 13815, 13824; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13815-L13824) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repairs the polynomial-variable separator and the nearby adverb in the numerical-polynomial definition.

Adverse evidence / qualification: The list of indeterminates, arbitrary abelian coefficient group and binomial basis are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-X_1, \ldots X_n
+X_1, \ldots, X_n
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-sufficient large
+sufficiently large
````

### MC-STK-ERR-1975

`algebra.tex` — 13918-13919; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13918-L13919) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specifies the submodule, quotient and least positive exponents used in the existing inner induction. Their finite generation, inherited grading and exact degree sequences are proved in the editorial note.

Adverse evidence / qualification: The original existence statement has a valid witness; it is not a false theorem. The later largest torsion submodule is justified by stabilization of the kernel chain under the original Noetherian hypothesis, not by assuming uniform nilpotence without it.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-$0 \to M' \to M \to M'' \to 0$ such that the integers
-$r', r''$ are strictly smaller than $r$. Thus we know
+$0 \to M' \to M \to M'' \to 0$ with $M' = xM$ and $M'' = M/xM$.
+Their least positive nilpotence exponents satisfy
+$r' \leq r - 1 < r$ and $r'' = 1 < r$. Thus we know
````

### MC-STK-ERR-1976

`algebra.tex` — 13977; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13977) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Uses the existing TeX command for sufficiently large degrees in the Hilbert-function estimate.

Adverse evidence / qualification: The exact dimension difference and asymptotic condition are retained. Zero quotients and the zero-variable boundary are handled in the separate editorial explanation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$n >> e$
+$n \gg e$
````

### MC-STK-ERR-1977

`algebra.tex` — 14031; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14031) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Uses the established phrase for the finite-length assertion.

Adverse evidence / qualification: This is a copyedit; the original mathematical assertion is valid. The ideal-power and residue-layer argument retains the original exponents.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-has a finite length
+has finite length
````

### MC-STK-ERR-1978

`algebra.tex` — 14047; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14047) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports identify the same singular/plural mismatch before the two constants. One operation resolves both.

Adverse evidence / qualification: The two inequalities and n>=c_2 bound are correct. The separate editorial argument also shows the explicit choice c_1=c_2=length_R(M/M prime); that strengthening is not substituted into the source theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists a
+there exist
````

### MC-STK-ERR-1979

`algebra.tex` — 14127; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14127) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The intermediate formula uses chi_{I,N}(-1) at its stated endpoint. Define that boundary value by the original quotient Q/I^0Q=0; a direct exact graded sequence proves the original phi formula even at n=c.

Adverse evidence / qualification: The statement is correct at n=c and must not be weakened to n>c. No previously defined nonnegative argument or original ideal power is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for $n \geq c$. We have
+for $n \geq c$, with the convention $\chi_{I,Q}(-1)=0$ for any finite $R$-module $Q$. We have
````

### MC-STK-ERR-1980

`algebra.tex` — 14218; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14218) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supplies the missing article in the comparison of the two already specified eventual polynomials.

Adverse evidence / qualification: Their equal positive degree and leading coefficient follow from the finite-colength inequalities. The preceding sentence already identifies the two polynomials; no additional mathematical defect is asserted.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-degree $<$ degree
+degree $<$ the degree
````

### MC-STK-ERR-1981

`algebra.tex` — 14341; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14341) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Allows the phrase following the display to finish its sentence.

Adverse evidence / qualification: Strict prime inclusions and their chain length are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathfrak p_{i + 1}.
+\mathfrak p_{i + 1}
````

### MC-STK-ERR-1982

`algebra.tex` — 14376; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14376) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Irreducible components correspond to minimal primes, with minimality taken among prime ideals.

Adverse evidence / qualification: Minimality among all ideals would be a different assertion. The original prime-to-closed-subset order reversal proves the intended statement.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a minimal ideal
+a minimal prime ideal
````

### MC-STK-ERR-1983

`algebra.tex` — 14366, 14419; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14366-L14419) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The original and current Topology definitions assign dimension minus infinity to the empty spectrum. The zero ring is Artinian and Noetherian, so both the converse and item (2) need the at-most-zero formulation to cover their stated arbitrary-ring scope.

Adverse evidence / qualification: Do not change the source dimension convention or silently exclude the zero ring. On nonzero rings the new inequality is exactly dimension zero. All ten equivalent conditions hold for the zero ring, including empty finite products. The local and prime-localized receiving rings are nonzero and retain their equality-with-zero statements.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-dimension zero
+dimension at most zero
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\dim(R) = 0$
+$\dim(R) \leq 0$
````

### MC-STK-ERR-1984

`algebra.tex` — 14487; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14487) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports identify the same misplaced adverb; one operation repairs the order.

Adverse evidence / qualification: The ideal-of-definition equivalence is unchanged and no duplicate operation is allocated.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-from directly
+directly from
````

### MC-STK-ERR-1985

`algebra.tex` — 14509, 14582; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14509-L14582) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Labels multiplication by the original x in the reported sequence and propagates the same clarification to its repeated use in the general dimension proof. Its exact kernel, image and cokernel are proved in the editorial note.

Adverse evidence / qualification: The original sequence has the required map and is mathematically valid. It is not the identity map. The quotient action preserves the original module lengths, so the subsequent signed Hilbert-polynomial difference is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R/\mathfrak p \to R/\mathfrak p
+R/\mathfrak p \xrightarrow{x} R/\mathfrak p
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R/\mathfrak p \to R/\mathfrak p
+R/\mathfrak p \xrightarrow{x} R/\mathfrak p
````

### MC-STK-ERR-1986

`algebra.tex` — 14602; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14602) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The generators of the original maximal ideal are ring elements, not necessarily polynomial variables.

Adverse evidence / qualification: The residue-vector-space dimension and Nakayama comparison remain exactly as stated.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-variables
+elements
````

### MC-STK-ERR-1987

`algebra.tex` — 14769; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14769) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The one-dimensional example is Z_p, the p-adic integers. Q_p is a field of dimension zero. The original surrounding dimension assertion is retained.

Adverse evidence / qualification: The complete valuation and ideal argument for Z_p is in the separate editorial note; the source reading is kept in the review so this mathematical object correction is visible.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-numbers
+integers
````

### MC-STK-ERR-1988

`algebra.tex` — 14803; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14803) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The two reports identify one source reminder. Preserve its words as a labelled unnumbered note rather than an eighth mathematical condition. The proof still establishes exactly the seven original conditions.

Adverse evidence / qualification: The user requires translations to retain the original work. Inventing an eighth theorem or silently removing the source reminder is unnecessary; this visible treatment resolves its status without changing the mathematical list.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item add more here.
+\item[] \textit{Source editorial reminder: add more here.}
````

### MC-STK-ERR-1989

`algebra.tex` — 14866; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14866) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The locally closed point is a prime of Spec(R); its quotient must be the original domain R/p.

Adverse evidence / qualification: The cited topological result supplies a point of the spectrum, so primality is intended. This is a missing noun qualification, not a new assumption on the theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a non-maximal ideal
+a non-maximal prime ideal
````

### MC-STK-ERR-1990

`algebra.tex` — 14871, 14879; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14871-L14879) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The claimed localized dimension one requires q strictly above p. Both quantified occurrences are corrected. The exact local domain has a nonzero maximal ideal and an open generic singleton, proving dimension exactly one.

Adverse evidence / qualification: At q=p the original localization is Frac(R/p), of dimension zero. Every maximal ideal above the nonmaximal p is still covered by the strict condition, so the global dimension and Jacobson conclusions are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak p \subset \mathfrak q$
+$\mathfrak p \subsetneq \mathfrak q$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak q \supset \mathfrak p$
+$\mathfrak q \supsetneq \mathfrak p$
````

### MC-STK-ERR-1991

`algebra.tex` — 14955; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14955) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports identify the same compound-noun copyedit.

Adverse evidence / qualification: The maximal counterexample argument and its Oka-family input are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-counter example
+counterexample
````

### MC-STK-ERR-1992

`algebra.tex` — 14962, 15018; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14962-L15018) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports cover the same two missing verbs. The two operations repair each source opening once.

Adverse evidence / qualification: The original filtration primes, support and local multiplicity formula are retained; no extra residue-degree factor is inserted.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak p_i$ as in
+$\mathfrak p_i$ be as in
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak p_i$ as in
+$\mathfrak p_i$ be as in
````

### MC-STK-ERR-1993

`algebra.tex` — 15146; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15146) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Two reports identify the same misspelled mathematical term.

Adverse evidence / qualification: The original annihilator dichotomy for the submodule and quotient is valid over the stated arbitrary ring.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-annilator
+annihilator
````

### MC-STK-ERR-1994

`algebra.tex` — 15446; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15446) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The object being quantified is a prime ideal, as required for disjointness from S and the localization comparison. One operation resolves the two reports.

Adverse evidence / qualification: The original two-stage localization isomorphism is proved with the fraction (m/s)/(r/t) mapping to tm/(sr). The Noetherian condition still supplies the finitely generated prime needed by the associated-prime converse.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for $\mathfrak p \in R$,
+for $\mathfrak p \in \Spec(R)$ with
````

### MC-STK-ERR-1995

`algebra.tex` — 15519; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15519) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports concern the same original placement reminder. Preserve it at its original position and label its source-editorial status visibly.

Adverse evidence / qualification: The reports supply no determined destination and do not justify relocating either adjoining lemma. The user requires a translation to preserve the original work; neither silent deletion nor source reorganization is needed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-This lemma should probably be put somewhere else.
+\textit{Source editorial note: This lemma should probably be put somewhere else.}
````

### MC-STK-ERR-1996

`algebra.tex` — 15579; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15579) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

One missing article resolves the two reports.

Adverse evidence / qualification: The flat ring map, original prime-extension hypothesis and symbolic-power formula are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be flat ring map
+be a flat ring map
````

### MC-STK-ERR-1997

`algebra.tex` — 15611; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15611) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The domain filtration quotients give injective multiplication, which proves injectivity of the further localization and equality of the two original kernels.

Adverse evidence / qualification: For R=k, S=k[t], p=q=0, n=1 and f=t, multiplication on k[t] is injective but misses 1. The full arbitrary-dimensional vector-space filtration proof needs no additional Noetherian hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-acts invertibly
+acts injectively
````

### MC-STK-ERR-1998

`algebra.tex` — 15628; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15628) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the specified base ring R in the fibre-ring subscript once for both reports.

Adverse evidence / qualification: The adjacent spectrum map and all receiving expressions already use the same tensor product over R.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S \otimes \kappa
+S \otimes_R \kappa
````

### MC-STK-ERR-1999

`algebra.tex` — 15645; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15645) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

List all six already-defined sets in the lemma opening.

Adverse evidence / qualification: The missing set occurs in the existing conclusions and proof; no additional set or assertion is introduced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A_{fin}$, $B$
+$A_{fin}$, $A'_{fin}$, $B$
````

### MC-STK-ERR-2000

`algebra.tex` — 15675; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15675) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports identify one subject-verb correction.

Adverse evidence / qualification: The quotient and localized-spectrum identifications remain those of the original proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-This prove that
+This proves that
````

### MC-STK-ERR-2001

`algebra.tex` — 15713; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15713) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore N in the denominator submodule of the original quotient.

Adverse evidence / qualification: The preceding flatness assertion and following associated-prime comparison already concern N/p-prime N, so no mathematical hypothesis changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$N/\mathfrak p'$
+$N/\mathfrak p'N$
````

### MC-STK-ERR-2002

`algebra.tex` — 15777, 15883; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15777-L15883) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Resolve the two reports with one article insertion at each of their two shared loci.

Adverse evidence / qualification: Both original flatness assumptions remain intact.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-flat as $R$-module
+flat as an $R$-module
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-flat as $R$-module
+flat as an $R$-module
````

### MC-STK-ERR-2003

`algebra.tex` — 15827; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15827) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The prime qS_q belongs to the associated set over S_q, as the earlier correctly typed statement already says.

Adverse evidence / qualification: Exact local tensor maps and the nonzero associated witness give the same contradiction over the original local coefficient ring. Do not conflate an extended ideal with an ideal of S.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{Ass}_S
+\text{Ass}_{S_{\mathfrak q}}
````

### MC-STK-ERR-2004

`algebra.tex` — 15815; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15815) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

End the displayed tensor/localization identity with a period.

Adverse evidence / qualification: Only terminal punctuation is added; both original comparison maps are verified in the editorial note.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-N_{\mathfrak q}
+N_{\mathfrak q}.
````

### MC-STK-ERR-2005

`algebra.tex` — 15914, 15916; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15914-L15916) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Give the explanatory sentence a finite verb and matching coordinated wording.

Adverse evidence / qualification: The original quotient-ring and localization references remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The first equality by
+The first equality follows from
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and the second by
+and the second from
````

### MC-STK-ERR-2006

`algebra.tex` — 15930; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15930) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The introduction names the class of rings in the plural.

Adverse evidence / qualification: This changes no definition or finiteness condition.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-non-Noetherian ring and
+non-Noetherian rings and
````

### MC-STK-ERR-2007

`algebra.tex` — 15996; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15996) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair the sentence fragment while preserving the reduced-ring contradiction.

Adverse evidence / qualification: The witness has proper annihilator and is therefore nonzero; the source nilpotence argument is valid.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence $x = 0$. Which contradicts
+Hence $x = 0$. This contradicts
````

### MC-STK-ERR-2008

`algebra.tex` — 16042; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16042) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the annihilator definition from its appositive description.

Adverse evidence / qualification: The exact annihilator and its embedding into M are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-0\}$ the annihilator
+0\}$, the annihilator
````

### MC-STK-ERR-2009

`algebra.tex` — 16045; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16045) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the doubled finite-predicate construction.

Adverse evidence / qualification: The proper ideal still gives a nonzero quotient with a minimal prime, exactly as needed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$I \not = R$ we have
+$I \not = R$,
````

### MC-STK-ERR-2010

`algebra.tex` — 16128; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16128) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the infinitive marker.

Adverse evidence / qualification: The descending sum of positive annihilating exponents proves the finite-generator argument. Preserve the source hypothesis on this particular prime, without adding ring Noetherianity.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-enough the prove
+enough to prove
````

### MC-STK-ERR-2011

`algebra.tex` — 16191, 16214; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16191-L16214) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

One report identifies the same naming construction at two loci; fix each exactly once.

Adverse evidence / qualification: The contraction map on spectra and all associated-prime inclusions remain the source maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $f
+Denote by $f
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $f
+Denote by $f
````

### MC-STK-ERR-2012

`algebra.tex` — 16240; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16240) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The nonvanishing witness ym is a module element and belongs to M_q.

Adverse evidence / qualification: The exact source witness remains nonzero because its annihilator stays proper at q and y is a unit there. It vanishes at the other maximal localizations for the reason given in the source.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S_{\mathfrak q}$
+$M_{\mathfrak q}$
````

### MC-STK-ERR-2013

`algebra.tex` — 16291; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16291) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the prime-as-ring-element quantifier at the later weak-association occurrence.

Adverse evidence / qualification: This is the repeated wording recorded as pending in ALGEBRA-RECON-407. The source weak-localization lemma is now fully read, and the same two-stage fraction maps justify the correction without Noetherian assumptions.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for $\mathfrak p \in R$,
+for $\mathfrak p \in \Spec(R)$ with
````

### MC-STK-ERR-2014

`algebra.tex` — 16421; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16421) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The purely transcendental stage has r variables; n was the earlier finite-extension degree.

Adverse evidence / qualification: Retain the exact polynomial ring, its nonzero coefficient-field denominators, and the resulting domain used in the proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n]
+x_r]
````

### MC-STK-ERR-2015

`algebra.tex` — 16410, 16417; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16410-L16417) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the requested comma and state explicitly that the input used to prove injection is nonzero.

Adverse evidence / qualification: The displayed nonzero residue and Nakayama contradiction fail for z=0. Choosing a nonzero input is sufficient for injection and leaves the field-extension theorem unchanged; the original coefficients and minimal finite submodule are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be an element.
+be a nonzero element.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemma \ref{lemma-NAK}
+Lemma \ref{lemma-NAK},
````

### MC-STK-ERR-2016

`algebra.tex` — 16419; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16419) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Add terminal punctuation before the next sentence.

Adverse evidence / qualification: The residue-module tensor product and its base field are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes_k K$
+\otimes_k K$.
````

### MC-STK-ERR-2017

`algebra.tex` — 16430; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16430) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Membership in the annihilator ideal applies to the ring element gf^n; its action on z is zero.

Adverse evidence / qualification: The exact equivalence gf^n in J iff gf^nz=0 preserves every multiplier and exponent. The previously proved injection justifies removing g from the vanishing equation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g f^n z \in J$
+$g f^n \in J$
````

### MC-STK-ERR-2018

`algebra.tex` — 16508; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16508) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The vanishing statement concerns the newly quantified K', as required by the following element argument.

Adverse evidence / qualification: The source separately proves and uses vanishing for K. Both submodules retain their original definitions.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-K_{\mathfrak q_j}
+K'_{\mathfrak q_j}
````

### MC-STK-ERR-2019

`algebra.tex` — 16643; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16643) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The source definition reserves unqualified regularity for the ring module R; the permutation conclusion must retain M.

Adverse evidence / qualification: The local ring k[t,epsilon]/(t epsilon,epsilon^2) localized at (t,epsilon), with M=R/(epsilon), gives an M-regular element t that is a ring zerodivisor. The existing proof works on M.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a regular
+is an $M$-regular
````

### MC-STK-ERR-2020

`algebra.tex` — 16671; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16671) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The adjacent-transposition argument takes the quotient by the generated submodule, restoring its omitted final M.

Adverse evidence / qualification: Keep the same order, ideal generators, local Noetherian hypotheses, and nonzero final quotient.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$M/(x_1, \ldots, x_{i-2})$
+$M/(x_1, \ldots, x_{i-2})M$
````

### MC-STK-ERR-2021

`algebra.tex` — 16836; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16836) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The next multiplier must use the next variable x_(i+1). Its shift leaves each coefficient ideal I_E unchanged.

Adverse evidence / qualification: All supports of E, including zero exponents, give precisely all ordered subsequence conditions. This justification stays in the note; only the wrong index is replaced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-f_{i + 1}x_i
+f_{i + 1}x_{i + 1}
````

### MC-STK-ERR-2022

`algebra.tex` — 16942; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16942) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the inner induction base l=0 before the displayed rewrite uses l-1 and l-2.

Adverse evidence / qualification: The induction on c already proves the base without any inverse power. All terms in the original step remain; the l=1 empty sum and no-primed-variable boundary are accounted for.

````diff
--- original
+++ replacement
@@ -1 +1,4 @@
-Namely, set $J' = (f_1, \ldots, f_{c-1})$.
+Set $J' = (f_1, \ldots, f_{c-1})$.
+For $l = 0$, the induction hypothesis on $c$ gives
+$a_{I',0} \in J' \subset J$, which proves the assertion.
+Assume now $l \geq 1$; the sum from $0$ to $l-2$ below is empty when $l=1$.
````

### MC-STK-ERR-2023

`algebra.tex` — 16975; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16975) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Module coefficients belong to the generated submodule JM, not to the ring ideal J.

Adverse evidence / qualification: The same original induction works with M/JM. No ring-module identification is assumed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-coefficients $m_I$ are in $J$
+coefficients $m_I$ are in $JM$
````

### MC-STK-ERR-2024

`algebra.tex` — 17046, 17053; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17046-L17053) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Handle degree zero by its actual quotient and restrict both formulas containing J^(n-1) to positive n.

Adverse evidence / qualification: The exact intersection identity for n>=1 follows from injectivity of the monomial shift on the original polynomial module. It does not require separatedness; it makes no assertion involving J^-1.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Thus, in order to prove the lemma it suffices to show that
+For $n=0$, the displayed quotient is $M/JM$, as required.
+For $n \geq 1$, it suffices to show that
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Actually, we have
+Actually, for $n \geq 1$, we have
````

### MC-STK-ERR-2025

`algebra.tex` — 17055-17056; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17055-L17056) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the module quotient and name the original tensor product as a polynomial module.

Adverse evidence / qualification: For a general R-module M this is not an algebra. The notation M/JM[X] in the preceding line is consistent polynomial-module shorthand and is retained.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-polynomial algebra
-$M/J[X_1, \ldots, X_c]$
+polynomial module
+$(M/JM) \otimes_{R/J} (R/J)[X_1, \ldots, X_c]$
````

### MC-STK-ERR-2026

`algebra.tex` — 17127; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17127) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Define the image ideal used by the displayed graded comparison.

Adverse evidence / qualification: The original quotients by the intersections of all ideal powers are retained. Exact representative maps prove the comparison in every degree, including the unit ideal and zero module.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
+Set $\overline{J}=J\overline{R}
+= (\overline{f}_1, \ldots, \overline{f}_r)$.
 This is true because
````

### MC-STK-ERR-2027

`algebra.tex` — 17199, 17206; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17199-L17206) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the declared image b consistently on the S-side of the base-change proof.

Adverse evidence / qualification: The assertion about the tensor kernel itself is valid: b^n sum(s_i tensor x_i)=sum(s_i x_i) tensor a^n=0. This is notation clarification, not a new false-torsion claim.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-annihilates $a$-power torsion
+annihilates $b$-power torsion
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-annihilated by $a^n$
+annihilated by $b^n$
````

### MC-STK-ERR-2028

`algebra.tex` — 17221; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17221) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The last factor uses the declared polynomial variable t_n.

Adverse evidence / qualification: The original degree, all monomial components and the Rees presentation are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n^{e_n}
+t_n^{e_n}
````

### MC-STK-ERR-2029

`algebra.tex` — 17267; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17267) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The base-change target is the ring R introduced in the statement and proof.

Adverse evidence / qualification: The tensor map and power-torsion quotient retain their original rings and denominators.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$P \to A$
+$P \to R$
````

### MC-STK-ERR-2030

`algebra.tex` — 17359, 17362, 17370, 17372; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17359-L17372) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The original indexing conditions exclude every object when R is a field. Admit the identity chart so the full original class of local domains remains covered, and explicitly index charts inside the specified A.

Adverse evidence / qualification: The zero-denominator chart is zero and fails the fibre condition. The identity chart has nonzero closed fibre and is itself an affine blowup. The source valuation-ring hypothesis is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-affine blowups $R \to R[\frac{I}{a}]$ with
+affine blowups $R \to R[\frac{I}{a}]$ contained in $A$, with
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item $a \in I \subset \mathfrak m$,
+\item $a \in I \subset \mathfrak m$, or $(I,a)=(R,1)$,
````

````diff
--- original
+++ replacement
@@ -1 +1,4 @@
-Any blowup algebra $R[\frac{I}{a}]$ is a domain contained in $K$ see
+If $R$ is a field, then $A=R$ and the identity chart $(I,a)=(R,1)$
+gives the result. Assume henceforth that $\mathfrak m\ne0$.
+Condition (3) forces $a\ne0$. Each chart $R[\frac{I}{a}]$
+in the diagram is a domain contained in $K$, see
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-directed union of the ones where $a \in I$ have properties (1), (2), (3).
+directed union of those contained in $A$ and having properties (1), (2), (3).
````

### MC-STK-ERR-2031

`algebra.tex` — 17386-17387, 17390; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17386-L17390) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

A scaled common denominator puts every generator in the original maximal ideal; contraction from the dominating A proves the nonzero fibre.

Adverse evidence / qualification: The separate field case is handled by the identity chart. Because f_i=t(de_i), membership in the maximal ideal already follows inside R; no extra valuation assumption is hidden in that calculation.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-Choose a nonzero $a \in R$ such that we can write $e_i = f_i/a$ for
-all $i = 1, \ldots, n$.
+Choose $0\ne d\in R$ such that $de_i\in R$ for all $i$.
+Choose $0\ne t\in\mathfrak m$ and put $a=td$ and $f_i=ae_i$.
+Then $a\ne0$, $a,f_i\in\mathfrak m$, and $e_i=f_i/a$.
````

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-$e_i$. The lemma follows immediately from this observation.
+$e_i$. The maximal ideal of $A$ contracts to a prime of this chart
+over $\mathfrak m$, so its fibre at $\mathfrak m$ is nonzero.
+Thus the constructed chart has all three required properties, proving the lemma.
````

### MC-STK-ERR-2032

`algebra.tex` — 17430; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17430) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the first syzygy before the printed recursion refers to its preceding free module.

Adverse evidence / qualification: The first kernel is finite by Noetherianity. All original modules and subsequent differentials stay intact; no negative free-module index is assigned to M.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-As a first step choose a surjection $R^{n_0} \to M$.
+As a first step choose a surjection $R^{n_0} \to M$,
+and then a surjection $R^{n_1}\to\Ker(R^{n_0}\to M)$.
+For the subsequent steps take $e\geq1$.
````

### MC-STK-ERR-2033

`algebra.tex` — 17646; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17646) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The distributive subject each takes a singular verb.

Adverse evidence / qualification: The short exact sequence of Hom complexes, differential and connecting maps are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-each of the $F_i$ are free
+each of the $F_i$ is free
````

### MC-STK-ERR-2034

`algebra.tex` — 17698; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17698) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the article before the singular sequence.

Adverse evidence / qualification: The split free-module sequence and the resulting sequence of kernels are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is short exact sequence
+is a short exact sequence
````

### MC-STK-ERR-2035

`algebra.tex` — 17976; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17976) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The module N/xN is the quotient by the entire sum ideal p+(x).

Adverse evidence / qualification: The explicit generator map proves this quotient and its inverse; all support and associated-prime calculations retain the original objects.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R/\mathfrak p + (x)
+R/(\mathfrak p + (x))
````

### MC-STK-ERR-2036

`algebra.tex` — 18008; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18008) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The dimension calculation uses the same whole quotient ideal as the preceding inheritance lemma.

Adverse evidence / qualification: The original x is a nonzerodivisor and is not in p. The minimal-prime choice, power x^n and exact depth drop are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim(R/\mathfrak p + (x))
+\dim(R/(\mathfrak p + (x)))
````

### MC-STK-ERR-2037

`algebra.tex` — 18060, 18080-18081; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18060-L18081) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Handle the zero module and empty maximal spectrum before finite induction, and restrict the asserted depth drop to the nonzero localizations.

Adverse evidence / qualification: The theorem remains valid. A nonzero finite module has a nonzero maximal localization with finite depth; zero localizations can still occur and retain infinite depth. All original rings, f and localizations are preserved.

````diff
--- original
+++ replacement
@@ -1 +1,4 @@
-By Lemmas
+Use the convention $\min\varnothing=\infty$. If $N=0$, the equality
+is immediate, including when $S=0$. Assume $N\ne0$; some maximal
+localization of $N$ is nonzero and has finite depth, so the minimum
+used below is finite. By Lemmas
````

````diff
--- original
+++ replacement
@@ -1,2 +1,5 @@
-all the depths drop exactly by $1$ when passing from $N$ to
-$N/fN$ and the induction hypothesis does the rest.
+the depth over $R$ and the depths of the nonzero maximal localizations
+drop exactly by $1$ when passing from $N$ to $N/fN$.
+The nonzero localizations remain nonzero by Nakayama's lemma;
+zero localizations stay zero with infinite depth. Thus the finite
+minimum drops by $1$, and the induction hypothesis finishes the proof.
````

### MC-STK-ERR-2038

`algebra.tex` — 18103, 18111; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18103-L18111) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the declared Ext operator consistently in the two displayed maps.

Adverse evidence / qualification: The functors are already mathematically correct; this changes operator typography only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{Ext}
+\Ext
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{Ext}
+\Ext
````

### MC-STK-ERR-2039

`algebra.tex` — 18125; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18125) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The Hom complexes increase cohomological degree, so their isomorphism acts on cohomology.

Adverse evidence / qualification: The explicit adjunction and inverse commute with the original differentials; no variance or resolution change is needed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-homology groups
+cohomology groups
````

### MC-STK-ERR-2040

`algebra.tex` — 18156; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18156) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the article before injection.

Adverse evidence / qualification: The kernel is zero by the original Jacobson-radical intersection theorem; the proof and its hypothesis are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is injection
+is an injection
````

### MC-STK-ERR-2041

`algebra.tex` — 18447-18449; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18447-L18449) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The reported reversed index must be corrected together with the inconsistent minus sign and omitted endpoint generators, so the generators describe the original displayed denominator.

Adverse evidence / qualification: The printed positive cycle equations require matching signs. An identity square over the integers shows the opposite-sign pair is not a cycle. A one-row example shows that omitting endpoint boundaries already gives the wrong degree-zero quotient. Preserve the original commuting square and positive boundary formula.

````diff
--- original
+++ replacement
@@ -1,3 +1,7 @@
-Naturally, we divide out by ``trivial'' zig-zags, namely the submodule
-generated by elements of the form $(0, \ldots, 0, -\delta(a_{t + 1, t-i}),
-d(a_{t + 1, t-i}), 0, \ldots, 0)$. Note that there are canonical
+Naturally, we divide out by the ``trivial'' zig-zags in the displayed
+denominator. They are generated by tuples supported at the left endpoint
+with value $d(a_{i+1,0})$, tuples supported at the right endpoint
+with value $\delta(a_{0,i+1})$, and the adjacent pairs
+$(0,\ldots,0,\delta(a_{t+1,i-t}),d(a_{t+1,i-t}),0,\ldots,0)$
+for $0\leq t<i$. For $i=0$ only the endpoint generators occur.
+Note that there are canonical
````

### MC-STK-ERR-2042

`algebra.tex` — 18466; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18466) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The representative belongs to the kernel of a degree-lowering differential.

Adverse evidence / qualification: Both endpoint maps land in the original homology groups; all cycles and degrees stay unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a cocycle
+a cycle
````

### MC-STK-ERR-2043

`algebra.tex` — 18476; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18476) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the parenthetical calculation before its period.

Adverse evidence / qualification: The commutation and square-zero calculation itself is correct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-= 0$. By exactness
+= 0$). By exactness
````

### MC-STK-ERR-2044

`algebra.tex` — 18488, 18490, 18491; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18488-L18491) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the right-edge cokernels in the two actual consecutive degrees, rather than the transposed top-edge terms.

Adverse evidence / qualification: The original a_(0,i) lands in the corrected target, and delta is induced from A_(0,i+1). The full boundary-clearing proof includes the endpoints and degree zero.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Coker(A_{i, 1} \to A_{i, 0})
+\Coker(A_{1, i} \to A_{0, i})
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Coker(A_{i + 1, 1} \to A_{i + 1, 0})
+\Coker(A_{1, i + 1} \to A_{0, i + 1})
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Coker(A_{i, 1} \to A_{i, 0})
+\Coker(A_{1, i} \to A_{0, i})
````

### MC-STK-ERR-2045

`algebra.tex` — 18549, 18551; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18549-L18551) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the specified tensor base R explicit in both codomains.

Adverse evidence / qualification: The base ring is already determined by the surrounding definition; no change of mathematical tensor product is claimed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-F_{i-1} \otimes G_j
+F_{i-1} \otimes_R G_j
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-F_i \otimes G_{j-1}
+F_i \otimes_R G_{j-1}
````

### MC-STK-ERR-2046

`algebra.tex` — 18626-18628, 18628-18629, 18631; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18626-L18631) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Include dimensions zero and one, qualify the initial nonidentity assertion, and state the characteristic condition for the two distinct eigenspace multiplicities.

Adverse evidence / qualification: The full basis decomposition proves the swap is the identity in dimensions zero and one. In characteristic two every off-diagonal pair is a size-two Jordan block; distinct plus/minus eigenvalue multiplicities require characteristic different from two.

````diff
--- original
+++ replacement
@@ -1,3 +1,2 @@
-this map is not the
-identity, because even when $i = 0$ this map is not the
-identity!
+this map need not be the
+identity, even when $i = 0$.
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-For example, if $V$ is a vector space of dimension
-$n$ over a field, then the switch map
+For example, let $V$ be a vector space of dimension
+$n$ over a field. If its characteristic is not $2$, the switch map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-In characteristic $2$ it is not even diagonalizable.
+In characteristic $2$ it is not diagonalizable when $n\geq2$.
````

### MC-STK-ERR-2047

`algebra.tex` — 18764; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18764) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing verb in the conclusion.

Adverse evidence / qualification: Tensor products and exact filtered colimits give precisely the stated homology identity.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus the result by Lemma
+Thus the result follows by Lemma
````

### MC-STK-ERR-2048

`algebra.tex` — 18824; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18824) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the missing leading arrow in the alternating free resolution.

Adverse evidence / qualification: The exact kernel/image equalities for the original two projectors verify every degree; no map is replaced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ldots F
+\ldots \to F
````

### MC-STK-ERR-2049

`algebra.tex` — 18826-18827; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18826-L18827) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the two distinct projectors in the same order as a and b.

Adverse evidence / qualification: The augmentation is projection to P; its kernel is the image of b, with a and b alternating as printed.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-the projector onto
-$P$ and $Q$.
+the projectors onto
+$P$ and $Q$, respectively.
````

### MC-STK-ERR-2050

`algebra.tex` — 18976; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18976) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the verb before surjective.

Adverse evidence / qualification: The actual fibre-product map q is onto: lift the difference of its two representatives through IF and retain their classes modulo J. The complete construction is separate editorial evidence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and $q$ surjective
+and $q$ is surjective
````

### MC-STK-ERR-2051

`algebra.tex` — 18985; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18985) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The difference of two module elements lies in JP, rather than in the ring ideal J.

Adverse evidence / qualification: Write that difference as a finite sum of J coefficients times P elements; IJ=0 then proves the required annihilation. With t=a-id, t(P) lies in IP and t(IP)=0, so t^2=0. The exact inverse 2id-a and section h(2id-a) prove the source conclusion without replacing its omitted details.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$j_\alpha \in J$
+$j_\alpha \in JP$
````

### MC-STK-ERR-2052

`algebra.tex` — 19024; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19024) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the literal horizontal-tab byte from the source expression.

Adverse evidence / qualification: TeX treats the tab as whitespace. This is source hygiene only; the rank claim and its nonzero-ring hypothesis are already correct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$	R_{f_i}$
+$R_{f_i}$
````

### MC-STK-ERR-2053

`algebra.tex` — 19083-19084; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19083-L19084) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Represent the actual localized element by its numerator and denominator, state its avoidance of the selected prime, and identify the resulting original-ring open.

Adverse evidence / qualification: The mutual universal localization maps prove (R_g)_(h/g^a) is R_(gh) with every original fraction retained. The source conclusion is valid once its original-ring denominator and neighbourhood are specified.

````diff
--- original
+++ replacement
@@ -1,2 +1,4 @@
-Hence by Nakayama's lemma again there exists a $g' \in R_g$ such that
-$\Ker(\varphi)_{g'} = 0$. In other words, $M_{gg'}$ is free.
+Hence by Nakayama's lemma again there exists
+$g'=h/g^a\in R_g\setminus\mathfrak pR_g$, with $a\geq0$ and
+$h\in R\setminus\mathfrak p$, such that $\Ker(\varphi)_{g'}=0$.
+Thus $(M_g)_{g'}\cong M_{gh}$ is free on the neighbourhood $D(gh)$.
````

### MC-STK-ERR-2054

`algebra.tex` — 19114, 19117; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19114-L19117) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural for the modules in the exact sequence and the singular verb for its one covering.

Adverse evidence / qualification: The adjacent agreement issue was detected in the same paragraph. Neither edit changes the finite-presentation hypothesis, Hom maps or localization cover.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R$-module.
+$R$-modules.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist a covering
+there exists a covering
````

### MC-STK-ERR-2055

`algebra.tex` — 19164; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19164) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the subject of the concluding clause.

Adverse evidence / qualification: The map is a surjection between free modules of the same finite rank. Its determinant is a unit, giving the original inverse; rank zero is included.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-whence is an isomorphism
+whence it is an isomorphism
````

### MC-STK-ERR-2056

`algebra.tex` — 19213-19214; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19213-L19214) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Join the compound noun across the original line break.

Adverse evidence / qualification: The mathematical counterexample is correct. Smooth cutoffs identify the original localization with the cyclic quotient, and connectedness rules out a nontrivial idempotent kernel. The full verification stays in editorial evidence.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-counter
-example
+counterexample
````

### MC-STK-ERR-2057

`algebra.tex` — 19281; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19281) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the maximal ideal of R already specified in the source module quotient.

Adverse evidence / qualification: The residue-field tensor map and original lifted basis verify the local descent. No different maximal ideal or residue field is substituted.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\kappa(\mathfrak m)
+\kappa(\mathfrak m_R)
````

### MC-STK-ERR-2058

`algebra.tex` — 19300; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19300) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural for the enumerated maximal ideals.

Adverse evidence / qualification: Chinese remainder lifts one basis at every maximal ideal. The local determinant argument then proves the original constant-rank result; the source hint remains a hint.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-all maximal ideal
+all maximal ideals
````

### MC-STK-ERR-2059

`algebra.tex` — 19351; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19351) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing article.

Adverse evidence / qualification: An explicit finite dual basis gives the inverse of the original tensor-Hom map; that supplementary calculation is not substituted for the author proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $R$ be ring.
+Let $R$ be a ring.
````

### MC-STK-ERR-2060

`algebra.tex` — 19424-19427; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19424-L19427) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Clear the original preimage denominators and the localized equalities before defining the map into M_f.

Adverse evidence / qualification: A chosen element of M_p need not belong to the later M_f. The two explicit multipliers put m_i in M and prove the actual equality in N while keeping every chosen denominator outside p.

````diff
--- original
+++ replacement
@@ -1,4 +1,6 @@
-For each $i \in \{1, \ldots, n\}$ choose an element
-$m_i \in M_{\mathfrak p}$ such that $\varphi(m_i) = f_i e_i$
-for some $f_i \in R$, $f_i \not \in \mathfrak p$. This is possible
-as $\varphi_{\mathfrak p}$ is an isomorphism. Set $f = f_1 \ldots f_n$
+For each $i \in \{1,\ldots,n\}$ choose a preimage
+$n_i/s_i\in M_{\mathfrak p}$ of $e_i/1$, with $n_i\in M$ and
+$s_i\notin\mathfrak p$. Choose $t_i\notin\mathfrak p$ such that
+$t_i(\varphi(n_i)-s_ie_i)=0$ in $N$.
+Put $m_i=t_in_i\in M$ and $f_i=t_is_i\notin\mathfrak p$;
+then $\varphi(m_i)=f_ie_i$ in $N$. Set $f=f_1\cdots f_n$
````

### MC-STK-ERR-2061

`algebra.tex` — 19433; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19433) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the actual codomain M_f of psi for the relation images.

Adverse evidence / qualification: Vanishing after further localization to M_p supplies g_j outside p which kills this same element in M_f. The product then gives the original factorization through N_(fg).

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an element of $M$
+an element of $M_f$
````

### MC-STK-ERR-2062

`algebra.tex` — 20029; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L20029) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Exclude the zero torsion module from the example that promises all three modules are nonflat.

Adverse evidence / qualification: Zero is torsion and flat. Every nonzero torsion abelian group has a nonzero element annihilated by a nonzero integer, witnessing failure of flatness. The nonsplit and combined examples are otherwise correct, with their original sequence and maps preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-any torsion module
+any nonzero torsion module
````

### MC-STK-ERR-2063

`algebra.tex` — 20316-20317; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L20316-L20317) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the authoring instruction from the enumerated mathematical statement and finish its actual last item with a period.

Adverse evidence / qualification: The deleted fourth item contains no mathematical claim or proved additional descent property. Retain its original occurrence in editorial documentation for any translation; do not replace it silently by the separately proved extension.

````diff
--- original
+++ replacement
@@ -1,2 +1 @@
-$M$ is flat, and
-\item add more here as needed.
+$M$ is flat.
````

### MC-STK-ERR-2064

`algebra.tex` — 20323-20324; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L20323-L20324) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the coefficients depend on the generator j while using the one common finite list of original M entries.

Adverse evidence / qualification: Collecting the finitely many tensor presentations and inserting zero coefficients proves the required common list. The source argument then uses precisely these x_i and its map R^n to M.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Write $y_j = \sum x_i \otimes f_i$ for some
-$x_1, \ldots, x_n \in M$.
+Write $y_j=\sum_{i=1}^n x_i\otimes f_{ij}$ using one
+common finite list $x_1,\ldots,x_n\in M$ and coefficients $f_{ij}\in S$.
````

### MC-STK-ERR-2065

`algebra.tex` — 20418; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L20418) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Choose a section only when the successor quotient belongs to the original indexed family.

Adverse evidence / qualification: If S has a last member alpha, M_(alpha+1) is undefined. The definition and direct-sum statement already quantify over alpha+1 in S. The explicit sections and transfinite inverse prove the original lemma with this index repair.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for each $\alpha \in S$
+for each $\alpha+1\in S$
````

### MC-STK-ERR-2066

`algebra.tex` — 20464-20466; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L20464-L20466) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Include the terminal stage M_I=M in the original partial-sum construction.

Adverse evidence / qualification: For a successor ordinal I the printed union omits the last coordinate summand. S=I+1 also gives the required zero stage when I is empty. Limit continuity, the coordinate retraction and the countably generated successor quotient verify every defining property.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-Well-order $I$ so that we can think of it as an ordinal.  Then setting $M_i =
-\bigoplus_{j < i} N_j$ gives a Kaplansky d\'evissage $(M_i)_{i \in I}$ of
-$M$.
+Well-order $I$ so that we can think of it as an ordinal. Set $S=I+1$ and
+$M_\alpha=\bigoplus_{j<\alpha}N_j$ for $\alpha\in S$.
+Then $(M_\alpha)_{\alpha\in S}$ is a Kaplansky d\'evissage of $M$.
````

### MC-STK-ERR-2067

`algebra.tex` — 21031; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21031) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Enlarge the lifted factorization stage until the two actual maps from M_i agree, before asserting commutativity.

Adverse evidence / qualification: Equality after M_j to the colimit does not imply equality in M_j. Each difference on a finite generating set dies at a later stage; one common upper bound kills all of them. The original diagram, domination argument and statement then hold.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-for some $h': Q \to M_j$.  In total we have a commutative diagram
+for some $h': Q \to M_j$. Since $M_i$ is finitely generated,
+after increasing $j$ and composing $h'$ with the transition map we have
+$f_{ij}=h'\circ g$. Thus we have a commutative diagram
````

### MC-STK-ERR-2068

`algebra.tex` — 21101-21102; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21101-L21102) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Cover arbitrary k>=i by a common upper bound with j; a directed set need not linearly order these indices.

Adverse evidence / qualification: The source proves the factor for indices above j, then only treats indices below j. For an incomparable k, ell>=j,k and the actual composite a f_(k,ell) prove the same factorization without changing the theorem or its quantifier.

````diff
--- original
+++ replacement
@@ -1,2 +1,4 @@
-such that $f_{ij} = h \circ f_{ik}$.  If $j \geq k$ then we can take
-$h = f_{kj}$. Hence (3) holds.
+such that $f_{ij} = h \circ f_{ik}$. For any $k\geq i$, choose
+$\ell\geq j,k$ and $a:M_\ell\to M_j$ with $f_{ij}=a\circ f_{i\ell}$.
+Then $h=a\circ f_{k\ell}$ satisfies $f_{ij}=h\circ f_{ik}$.
+Hence (3) holds.
````

### MC-STK-ERR-2069

`algebra.tex` — 21173; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21173) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the adverb in the comparative phrase.

Adverse evidence / qualification: The kernel argument is valid: the surjection after tensoring detects equality of its two receiving kernels. This report warrants the one-word copyedit only.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is clear weaker
+is clearly weaker
````

### MC-STK-ERR-2070

`algebra.tex` — 21353; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21353) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the R-valued coordinate of a_i in R^M while preserving the declared projection p_x:M^M to M.

Adverse evidence / qualification: The displayed application p_x(a_i) is outside the declared domain. The actual canonical tensor map gives coefficient (a_i)_x, so the finite list x_i generates the original module. The subsequent finite-presentation diagram chase uses right exactness and remains valid.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-p_x(a_i)
+(a_i)_x
````

### MC-STK-ERR-2071

`algebra.tex` — 21866; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21866) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the biconditional wording.

Adverse evidence / qualification: For a finite module the tensor/product map is onto, and ML makes it injective. The finite-presentation criterion gives precisely the claimed equivalence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-only it is
+only if it is
````

### MC-STK-ERR-2072

`algebra.tex` — 21878; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21878) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the missing preposition.

Adverse evidence / qualification: The following criterion, product lemma and coefficient isomorphism justify the stated power-series consequence with the original Noetherian hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a consequence the following lemma
+a consequence of the following lemma
````

### MC-STK-ERR-2073

`algebra.tex` — 21979; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L21979) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the apposition naming the coordinate span F-prime inside F.

Adverse evidence / qualification: Over the source Noetherian ring this coordinate span is finite presented, so its tensor inclusion is exactly the product inclusion and it is the smallest submodule.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the submodule of $F'$ of $F$
+the submodule $F'$ of $F$
````

### MC-STK-ERR-2074

`algebra.tex` — 22014; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22014) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the missing preposition in the annihilator statement.

Adverse evidence / qualification: The full coordinate formula is b(l)=max_m max(min(2^m,l)-2^(m-1),0), with m>=1 as in the displayed sequence. At l=2^r it is exactly 2^(r-1); the source mathematical claim is correct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is generated $x
+is generated by $x
````

### MC-STK-ERR-2075

`algebra.tex` — 22024; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22024) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the intended much-greater-than relation in the source asymptotic range.

Adverse evidence / qualification: Artin-Rees on the actual cyclic submodule gives the eventual annihilator exponent a or l-a. The powers-of-two exponent cannot equal either for all sufficiently large powers; the proof does not depend on any stronger asymptotic assertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$l = 2^m >> 0$
+$l = 2^m \gg 0$
````

### MC-STK-ERR-2076

`algebra.tex` — 22107-22108; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22107-L22108) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the increasing cofinal sequence with the correct order and allow repetitions, as required also for finite directed sets.

Adverse evidence / qualification: Changing only the order symbol leaves the false assertion that a finite directed set has a subset isomorphic to the natural numbers. The original upper-bound construction yields a sequence, possibly repeated. Explicit colimit maps verify its use with the original direct system.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-to see that a countable directed set has a cofinal
-subset isomorphic to $(\mathbf{N}, \geq)$. Suppose
+to obtain an increasing cofinal sequence indexed by
+$(\mathbf{N},\leq)$, allowing repetitions. Suppose
````

### MC-STK-ERR-2077

`algebra.tex` — 22274; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22274) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the article in the singular map phrase.

Adverse evidence / qualification: The mathematical implication retains the original countable-direct-sum hypothesis, flatness and ML descent along the actual pure injection.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be universally injective map
+be a universally injective map
````

### MC-STK-ERR-2078

`algebra.tex` — 22358; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22358) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Complete the infinitival phrase defining the original pushout.

Adverse evidence / qualification: The original cokernel presentation and each tensor-test map verify the source proof. The human attribution is retained. Pure reflection gives a second proof of the earlier group 511 result, kept separately from the source hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Take $N$ the pushout
+Take $N$ to be the pushout
````

### MC-STK-ERR-2079

`algebra.tex` — 22375; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22375) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the sentence after the display with lowercase is.

Adverse evidence / qualification: Tensoring the original cokernel gives exactly the displayed pushout. No mathematical statement or map is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Is a pushout diagram.
+is a pushout diagram.
````

### MC-STK-ERR-2080

`algebra.tex` — 22433; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22433) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert to in the construction of the original countable submodule.

Adverse evidence / qualification: The finite tensor entries of the countable generating family give P and only require containment in its tensor image. The subsequent adapted-submodule proof likewise uses actual images, without assuming tensor injections.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then take $P$ be
+Then take $P$ to be
````

### MC-STK-ERR-2081

`algebra.tex` — 22758; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22758) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Declare the module used by the quotients and maps.

Adverse evidence / qualification: For positive r, the original cofinal ideals and telescoping representatives justify the finite sum of principal-adic lifts. For r=0 the printed cofinality bound I^(rn) fails, but I=0 and the assertion is the canonical identity. That boundary is proved separately rather than replacing the translation proof.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-generated ideal. If $M
+generated ideal. Let $M$ be an $A$-module.
+If $M
````

### MC-STK-ERR-2082

`algebra.tex` — 22777; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22777) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Declare the module whose two adic filtrations are used.

Adverse evidence / qualification: The original J-adic limit x is retained. Writing u_n=x_n-x and summing the exact differences gives u_n=f^n v_n, with every sign, index and initial limit preserved.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
 be ideals.
+Let $M$ be an $A$-module.
````

### MC-STK-ERR-2083

`algebra.tex` — 22873; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22873) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the article required by the spoken initial letter R.

Adverse evidence / qualification: The finite span of the lifted residue generators is separated and complete; its completion surjects onto that of M, and separatedness identifies the actual elements. The zero-generator case is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as a $R/I$-module
+as an $R/I$-module
````

### MC-STK-ERR-2084

`algebra.tex` — 22873; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22873) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the missing preposition in the naming construction.

Adverse evidence / qualification: The original submodule M-prime and its inclusion in M remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $M'
+Denote by $M'
````

### MC-STK-ERR-2085

`algebra.tex` — 22903; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22903) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert by when introducing the completion notation.

Adverse evidence / qualification: Artin-Rees gives the exact shifted filtrations. The tensor comparison follows from the completed presentation, surjectivity for its finite kernel and the finite-free isomorphism, without assuming completion is flat before proving it.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote ${}^\wedge$
+Denote by ${}^\wedge$
````

### MC-STK-ERR-2086

`algebra.tex` — 22958; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22958) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair the repeated naming construction.

Adverse evidence / qualification: The injection for every ideal follows from the preceding finite-module result because every ideal is finite in the original Noetherian ring. The ideal criterion then supplies flatness.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote ${}^\wedge$
+Denote by ${}^\wedge$
````

### MC-STK-ERR-2087

`algebra.tex` — 22978; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L22978) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Propagate the same missing-preposition copyedit to the immediately following completion lemma.

Adverse evidence / qualification: This is an independently found repetition of the naming omission. Its mathematical statement remains the original sufficient Jacobson-radical condition.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $R^\wedge$
+Denote by $R^\wedge$
````

### MC-STK-ERR-2088

`algebra.tex` — 23050; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23050) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restrict the homogeneous sum to generators of degree at most n.

Adverse evidence / qualification: Only those generators contribute in degree n; negative ideal powers were not defined. Higher-degree generators receive zero coefficients in the following approximation argument. The exact coefficient bounds and convergent series prove the same source theorem, including the empty homogeneous-generator case.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\sum \overline{g}_j
+\sum_{j:\,d_j \leq n} \overline{g}_j
````

### MC-STK-ERR-2089

`algebra.tex` — 23118; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23118) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the subject of the sentence about the original Artinian quotient.

Adverse evidence / qualification: The finite-dimensional quotient is local Artinian, its maximal ideal is nilpotent, and the two original filtrations are canonically cofinal. No mathematical hypothesis is changed by this copyedit.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence has dimension
+Hence it has dimension
````

### MC-STK-ERR-2090

`algebra.tex` — 23228; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23228) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the missing complementizer in the Nakayama parenthesis.

Adverse evidence / qualification: The original complete ring has I in its Jacobson radical. The finite cokernel of A to B vanishes modulo I and hence vanishes; faithful flatness then identifies the actual completion map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-using $I$ is
+using that $I$ is
````

### MC-STK-ERR-2091

`algebra.tex` — 23224; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23224) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Cite the finite-module tensor-completion comparison that directly identifies B/IB with the completion of A/I.

Adverse evidence / qualification: The canonical comparison for the finite module A/I gives (A/I) tensor B = lim A/(I+J^n). Flatness alone does not state this identification. The later use of the flatness lemma for A to B is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{lemma-completion-flat}
+\ref{lemma-completion-tensor}
````

### MC-STK-ERR-2092

`algebra.tex` — 23308, 23317, 23319-23322, 23328-23329; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23308-L23329) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the strictly positive stabilized index b(d), repair the premature equality, and use the same index in the generation check.

Adverse evidence / qualification: A transition is an isomorphism in degree d only for n>d-min(d_i). The positive maximum handles all degrees and never invokes N_0. When N_1=0, nilpotent iteration forces every N_n=0, avoiding the undefined minimum of an empty generator family. Exact degreewise maps prove both generation and the quotient kernel; the zero case is an independently checked boundary.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Pick $r$ and homogeneous elements
+If $N_1=0$, all $N_n$ vanish and we take $N=0$.
+Otherwise pick $r>0$ and homogeneous elements
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-in those degrees). Thus the inverse system of degree $d$ parts
+in those degrees). Put $b(d)=\max\{1,1+d-\min(d_i)\}$.
+The inverse system of degree $d$ parts
````

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 \ldots
-= N_{2 + d - \min(d_i), d}
-= N_{1 + d - \min(d_i), d}
-= N_{d - \min(d_i), d} \to N_{-1 + d - \min(d_i), d} \to \ldots
+= N_{b(d)+2, d}
+= N_{b(d)+1, d}
+= N_{b(d), d}
````

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-because we can check this in $N_{d - \min(d_i), d}$ where it holds
-as $x_{d - \min(d_i), i}$ generate $N_{d - \min(d_i)}$.
+because we can check this in $N_{b(d), d}$ where it holds
+as $x_{b(d), i}$ generate $N_{b(d)}$.
````

### MC-STK-ERR-2093

`algebra.tex` — 23373; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23373) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the generator shifts in the module-degree injectivity bound.

Adverse evidence / qualification: The quotient kernel I^n M-prime has no components below min(d_i)+n. With n=d-min(d_i)+1 this includes the actual degree d. The source coefficient bound alone omitted the shifts. The finite homogeneous witness and tensor comparison prove this without treating A-prime as a graded ring.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-degrees $\leq n - 1$
+degrees $<\min(d_i)+n$ (in particular, in degree $d$)
````

### MC-STK-ERR-2094

`algebra.tex` — 23427, 23482, 23494; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23427-L23494) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert by at all three reported maximal-ideal declarations.

Adverse evidence / qualification: The actual quotient maps prove injection, a flat cokernel and universal tensor injection. The auxiliary ring S is Noetherian; the source does not require R Noetherian for this first lemma. The two receiving corollaries use exactly that argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\mathfrak m$
+Denote by $\mathfrak m$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\mathfrak m$
+Denote by $\mathfrak m$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\mathfrak m$
+Denote by $\mathfrak m$
````

### MC-STK-ERR-2095

`algebra.tex` — 23569; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23569) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Describe the finite-length proof by its actual induction direction.

Adverse evidence / qualification: Length zero is the zero module, length one is the residue field, and the exact Tor segment proves a longer module from two shorter ones. This is ordinary induction on length.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-By descending induction
+By induction
````

### MC-STK-ERR-2096

`algebra.tex` — 23597-23598; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23597-L23598) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Quantify the arbitrary ideal J in the finite-colength assertion.

Adverse evidence / qualification: The source applies the preparation lemma to R/J. Its later two ideals both have finite colength, and the explicit signed diagram chase supplies the actual lift needed by Artin-Rees.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-is injective for all ideals
+is injective for every ideal $J$
 of finite colength.
````

### MC-STK-ERR-2097

`algebra.tex` — 23601, 23633; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23601-L23633) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the intended much-greater-than TeX relation in both sufficiently-large-index statements.

Adverse evidence / qualification: The original proof has one uniform Artin-Rees constant c and takes all sufficiently large n. The notation correction does not change that quantifier, the shift n-c or the original module.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$n >> 0$
+$n \gg 0$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$n >> 0$
+$n \gg 0$
````

### MC-STK-ERR-2098

`algebra.tex` — 23666, 23668, 23674, 23676, 23680, 23681, 23687; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23666-L23687) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Choose a sufficiently large free index set and propagate it to all six sums in the argument.

Adverse evidence / qualification: The unrelated ideal I cannot determine a surjective presentation of an arbitrary R/I-module; I=0 over a field already fails for a rank-two module. The report says two occurrences, but there are six, and all must use the same chosen Lambda. The ideal I and the already corrected tensor base remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Choose a short exact sequence
+Choose a set $\Lambda$ and a short exact sequence
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \in I
+\lambda \in \Lambda
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \in I
+\lambda \in \Lambda
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \in I
+\lambda \in \Lambda
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \in I
+\lambda \in \Lambda
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \in I
+\lambda \in \Lambda
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \in I
+\lambda \in \Lambda
````

### MC-STK-ERR-2099

`algebra.tex` — 23932; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L23932) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert the missing preposition in the ideal and module declaration.

Adverse evidence / qualification: The original localization, quotient and tensor maps are retained. The two actual Tor comparison surjections compose to the source map before localization, so its zero-image hypothesis forces the localized obstruction to vanish.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $I'
+Denote by $I'
````

### MC-STK-ERR-2100

`algebra.tex` — 24082, 24155; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24082-L24155) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the finite verb in both explanations of the localized Tor vanishing.

Adverse evidence / qualification: The original scalar maps factor through K/K[f_j] and multiply by f_j. Injectivity on Tor and exact localization force vanishing. The full descending range 1 through j+1 is retained, and the omitted faithful-flatness argument is proved separately by its actual residue fibres.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The vanishing by the flatness
+The last vanishing follows from the flatness
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The vanishing by the flatness
+The last vanishing follows from the flatness
````

### MC-STK-ERR-2101

`algebra.tex` — 24471; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24471) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural noun in the general statement about injective ring maps.

Adverse evidence / qualification: The following theorem concerns arbitrary injective maps with Artinian source. This grammatical correction changes no mathematical hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-along injective homomorphism
+along injective homomorphisms
````

### MC-STK-ERR-2102

`algebra.tex` — 24649; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24649) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair the ring-module terminology and make the changed basis explicit.

Adverse evidence / qualification: The incoming image is in the span of the primed vectors. The original-coordinate pivot calculation gives exact inverse basis maps and a chain retraction. The map (1,1) over Z with incoming e_2-e_1 disproves the literal unprimed span; interpreting a silent basis relabelling recovers the intended source proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-subspace spanned by $e_j$
+submodule spanned by $e'_j$
````

### MC-STK-ERR-2103

`algebra.tex` — 24693, 24777; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24693-L24777) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Add the missing preposition in both notation declarations.

Adverse evidence / qualification: The actual socle proof and the quotient-complex homology maps retain their original objects and work without these grammatical omissions.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote $f_1$
+denote by $f_1$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $F_\bullet$
+Denote by $F_\bullet$
````

### MC-STK-ERR-2104

`algebra.tex` — 24704; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24704) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports describe the same incorrect article.

Adverse evidence / qualification: The Artinian reduction is proved using the last nonzero power of the maximal ideal, with the field and empty-complex cases retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a Artinian
+an Artinian
````

### MC-STK-ERR-2105

`algebra.tex` — 24723, 24740; source hypothesis correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24723-L24740) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Record the independently found nonzero-ring boundary of the exterior rank definition and numerical trivial-complex lemma.

Adverse evidence / qualification: The chapter permits the zero ring. There the maximum of exterior degrees with nonzero map is undefined, and a rank-zero convention still contradicts the displayed rank-one identity disk. The zero complex is exact but its arbitrarily chosen free presentation cannot support the numerical rank formula. All later local uses already have nonzero rings.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $R$ be a ring.
+Let $R$ be a nonzero ring.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-In Situation \ref{situation-complex}, suppose the complex is
+In Situation \ref{situation-complex}, suppose $R \ne 0$ and the complex is
````

### MC-STK-ERR-2106

`algebra.tex` — 24760; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24760) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the hyphen joining a cardinality to the following noun.

Adverse evidence / qualification: The actual disk counts t_i satisfy n_i=t_i+t_(i+1), giving the original alternating formula and all zero-rank unit ideals.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$r_{i + 1}$-basis
+$r_{i + 1}$ basis
````

### MC-STK-ERR-2107

`algebra.tex` — 24809; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24809) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports correct the same lowering-degree terminology.

Adverse evidence / qualification: The quotient is H_i for differentials M_i to M_(i-1), consistent with the immediately preceding long exact homology sequence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-cohomology group
+homology group
````

### MC-STK-ERR-2108

`algebra.tex` — 24810; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24810) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

The displayed list includes a left-exact sequence without a surjective final map, so remove the erroneous description short.

Adverse evidence / qualification: The separate note supplies its actual image factor B_(i-1) and proves the required depth bound, including i=e and i=e-1. No surjectivity onto M_(i-1) is assumed and no full translated proof is replaced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-short exact sequences
+exact sequences
````

### MC-STK-ERR-2109

`algebra.tex` — 24861, 24918-24920; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24861-L24920) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the highest nonzero degree to infer the depth bound; retain rank-zero maps and their unit ideals.

Adverse evidence / qualification: A zero matrix has I=R by the source convention, so maximal-ideal entries alone do not make every maximal-minor ideal proper. After discarding only zero top terms, the top rank is n_e>0. Its positive-size minors lie in the maximal ideal and suffice for the exactness argument.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-We may also assume that $e \geq 1$.
+Discard zero terms at the left. If no positive-degree term remains,
+the assertion holds. Otherwise we may assume that
+$e \geq 1$ and $n_e > 0$.
````

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-As $I(\varphi_i) \subset \mathfrak m$ for all $i$ because
-of what was said in the first paragraph of the proof, we
-see that (2)(b) implies $\text{depth}(R) \geq e$.
+Since $r_e = n_e > 0$ and the matrix entries lie in
+$\mathfrak m$, we have $I(\varphi_e) \subset \mathfrak m$.
+Thus (2)(b) implies $\text{depth}(R) \geq e$.
````

### MC-STK-ERR-2110

`algebra.tex` — 24964, 25054, 25143, 25248; conceptual correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24964-L25248) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the missing zero-module convention explicit and propagate its finite-parameter boundaries.

Adverse evidence / qualification: The source defines depth zero as positive infinity and the empty support dimension as negative infinity. Its literal CM equality excludes zero, contradicting localization at every prime: R=k[t]_(t), M=R/(t), p=0 is explicit. The zero exception repairs the intended later convention. The regular-sequence proposition must still exclude zero, the maximal-CM depth comparison is among nonzero modules, and a zero polynomial localization must be handled before choosing parameters.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-if $\dim(\text{Supp}(M)) = \text{depth}(M)$.
+if $M=0$ or if $\dim(\text{Supp}(M)) = \text{depth}(M)$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $M$ be a Cohen-Macaulay module
+Let $M$ be a nonzero Cohen-Macaulay module
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-ring is a finite module with
+ring is a nonzero finite module with
````

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
 be a maximal ideal, and let $\mathfrak p = R \cap \mathfrak m$.
+If $M_{\mathfrak p}=0$, then $M[x]_{\mathfrak m}=0$ and we are done.
+Hence assume $M_{\mathfrak p}\ne0$.
````

### MC-STK-ERR-2111

`algebra.tex` — 24986, 24993-24995, 24997; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L24986-L24997) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Exclude the vacuous zero-dimensional goodness case and retain the possible zero kernel.

Adverse evidence / qualification: For M=k and g=0 the d=0 goodness conditions are empty while multiplication is not injective. The given regular sequence already excludes M=0, so the missing hypothesis is d>0. In the d=1 proof the kernel may be zero and then has empty support; containment is the actual proved statement.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Notation and assumptions as above. If $g$ is good with respect to
+Notation and assumptions as above. Assume $d>0$. If $g$ is good with respect to
````

````diff
--- original
+++ replacement
@@ -1,3 +1 @@
-We prove the lemma by induction on $d$.
-If $d = 0$, then $M$ is finite and there is no case
-to which the lemma applies.
+We prove the lemma by induction on $d \geq 1$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The kernel $K$ has support $\{\mathfrak m\}$
+The kernel $K$ has support contained in $\{\mathfrak m\}$
````

### MC-STK-ERR-2112

`algebra.tex` — 25027, 25249; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25027-L25249) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct both articles in the single received report.

Adverse evidence / qualification: Both complete source units are read; the polynomial parameter sequence is chosen only after its nonzero localized-module case has been established.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Choose a $M$-regular
+Choose an $M$-regular
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be a $M_\mathfrak p$-regular
+be an $M_\mathfrak p$-regular
````

### MC-STK-ERR-2113

`algebra.tex` — 25068; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25068) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports require the actual module factor in the successive quotient.

Adverse evidence / qualification: The dimension-drop induction acts on M_i=M/(g_1,...,g_i)M and the exact quotient maps, whose nonzero targets follow from Nakayama.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$M/(g_1, \ldots, g_i)$
+$M/(g_1, \ldots, g_i)M$
````

### MC-STK-ERR-2114

`algebra.tex` — 25209; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25209) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair the missing verb while naming the actual nonzero localization needed in the depth comparison.

Adverse evidence / qualification: A nonzero M can have zero localization. With the explicit CM zero exception that case is immediate; otherwise p is in the support and the original finite depth and dimension inequalities apply. This also implies M is nonzero.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and $M$ not zero.
+and $M_{\mathfrak p}$ is nonzero.
````

### MC-STK-ERR-2115

`algebra.tex` — 25313; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25313) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the article before the spoken initial R.

Adverse evidence / qualification: The regular sequence, zero-dimensional quotient and their equivalence to the local-ring CM definition are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of a $R$-regular
+of an $R$-regular
````

### MC-STK-ERR-2116

`algebra.tex` — 25346; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25346) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports supply the omitted article and head noun.

Adverse evidence / qualification: The original predecessor theorem already has precisely this Noetherian local ring hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $R$ be Noetherian local.
+Let $R$ be a Noetherian local ring.
````

### MC-STK-ERR-2117

`algebra.tex` — 25348; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25348) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports correct the missing primality requirement.

Adverse evidence / qualification: The zero-dimensional CM ring k[epsilon]/epsilon^2 has the maximal arbitrary-ideal chain 0 < (epsilon) < R of length two. The source predecessor and Krull dimension concern prime chains.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Any maximal chain of ideals
+Any maximal chain of prime ideals
````

### MC-STK-ERR-2118

`algebra.tex` — 25391; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25391) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the finite-variable boundary of the cited polynomial-module theorem.

Adverse evidence / qualification: The chapter permits infinitely many variables but defines CM rings to be Noetherian. Over a field, the polynomial ring in infinitely many variables has the strictly increasing chain (x_1)<(x_1,x_2)<... and is not Noetherian. The source proof applies only to the finite-variable result.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Any polynomial algebra over $R$
+Any polynomial algebra in finitely many variables over $R$
````

### MC-STK-ERR-2119

`algebra.tex` — 25413, 25414; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25413-L25414) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Handle the empty free segment when e=d and exclude infinite depth before using the integer indices.

Adverse evidence / qualification: A nonzero finite M has finite e<=d. The e=d case is the identity complex, not an undefined F_(-1). For e<d the actual free covers may include a redundant R summand, ensuring every kernel is nonzero and the final K satisfies the source strict maximal-CM equality. Complete proof gives exact depth min(d,e+j) at each nonzero syzygy.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $M$ be a finite $R$-module of depth $e$.
+Let $M$ be a nonzero finite $R$-module of depth $e$.
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-There exists an exact complex
+If $e=d$, take $K=M$ and the identity map $K\to M$, with no free terms.
+If $e<d$, there exists an exact complex
````

### MC-STK-ERR-2120

`algebra.tex` — 25559; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25559) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports correct the same attributive noun.

Adverse evidence / qualification: The original localization bijection identifies every intermediate prime and preserves saturation and exact lengths.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-primes ideals
+prime ideals
````

### MC-STK-ERR-2121

`algebra.tex` — 25722; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25722) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Choose finite maximal-ideal orders only for nonzero factors.

Adverse evidence / qualification: The zero element lies in every power and has no finite maximal order. For both nonzero factors Krull intersection supplies the exact finite orders, whose initial forms have nonzero product.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $f, g \in R$ such that $fg = 0$.
+Suppose, for a contradiction, that $f, g \in R$ are nonzero and $fg = 0$.
````

### MC-STK-ERR-2122

`algebra.tex` — 25760; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25760) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the omitted preposition in the notation declaration.

Adverse evidence / qualification: The quotient maximal ideal and residue field remain exactly the original ones.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\overline{\mathfrak m}
+Denote by $\overline{\mathfrak m}
````

### MC-STK-ERR-2123

`algebra.tex` — 25765; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25765) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports restore the residue-field binding in the third vector-space dimension.

Adverse evidence / qualification: The actual tangent-space short exact sequence has all three terms over the same kappa. Its basis lifts and regular quotient kernel argument are proved with c=0 and c=d included.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-- \dim(\overline{\mathfrak m}
+- \dim_\kappa(\overline{\mathfrak m}
````

### MC-STK-ERR-2124

`algebra.tex` — 25791; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25791) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the article before the spoken initial R.

Adverse evidence / qualification: The original coefficient relation gives K=xK using regularity on M, including the rank-zero case.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a $R/xR$-basis
+an $R/xR$-basis
````

### MC-STK-ERR-2125

`algebra.tex` — 25842; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25842) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural for the directed family of maximal ideals.

Adverse evidence / qualification: The exact unit/nonunit argument proves the original maximal ideal is their colimit, with no injectivity hypothesis on transition maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of the maximal ideal
+of the maximal ideals
````

### MC-STK-ERR-2126

`algebra.tex` — 25843; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25843) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Bind the induction parameter to the grouped tangent space and its actual residue field.

Adverse evidence / qualification: The limit is Noetherian, so this dimension is finite. The quotient by x outside m squared has tangent dimension exactly d-1 via the original quotient map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$d = \dim \mathfrak m/\mathfrak m^2$
+$d = \dim_{R/\mathfrak m}(\mathfrak m/\mathfrak m^2)$
````

### MC-STK-ERR-2127

`algebra.tex` — 25853; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25853) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Both reports point to the direct domain theorem used in the argument.

Adverse evidence / qualification: The graded theorem is its ingredient, but the immediately following domain lemma states the result. A directed colimit of these domains is a domain by actual finite-stage zero detection, even for noninjective transition maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{lemma-regular-graded}
+\ref{lemma-regular-domain}
````

### MC-STK-ERR-2128

`algebra.tex` — 25914; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25914) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the comma separating the phrase from its that-clause.

Adverse evidence / qualification: Composition, base change and passage through the actual image are proved by the original maps; no source hypothesis changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in particular, that
+in particular that
````

### MC-STK-ERR-2129

`algebra.tex` — 25936; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25936) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the equality of composites required by epicity explicitly.

Adverse evidence / qualification: The common R-algebra structure on A defines both localizations. The actual annihilator argument proves the comparison into the product of localizations injective.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-from $S$ to a ring $A$ equalizing the map $R \to S$.
+from $S$ to a ring $A$ whose composites with $R \to S$ are equal.
````

### MC-STK-ERR-2130

`algebra.tex` — 25996, 25997; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L25996-L25997) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct all four undefined R occurrences in the alternate field argument to the original S.

Adverse evidence / qualification: OCC-12192 undercounts the occurrences as three. The direct proof concerns a tensor-factor inclusion, not multiplication, which is always surjective. A linear functional separating 1 and s proves the intended assertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R \to R \otimes_k R$
+$S \to S \otimes_k S$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\dim_k(R) \leq 1$
+$\dim_k(S) \leq 1$
````

### MC-STK-ERR-2131

`algebra.tex` — 26057; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26057) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the superfluous conjunction after the participial clause.

Adverse evidence / qualification: Right exactness and finite expansions in the original generators produce finite total matrix support; all row and column equations are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$ and we obtain
+$, we obtain
````

### MC-STK-ERR-2132

`algebra.tex` — 26092; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26092) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the image of the possibly noninjective ring map as required by the source statement.

Adverse evidence / qualification: The omitted rows and the exceptional j=1 column are checked exactly. An explicit signed block matrix represents g, including coincident generators and n=0.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-s_i \in R
+s_i \in \varphi(R)
````

### MC-STK-ERR-2133

`algebra.tex` — 26096; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26096) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the singular verb for the set of elements.

Adverse evidence / qualification: Block sums, negation, scalar representations and indexed tensor products prove the stated subalgebra property.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-expression as in (2) form an
+expression as in (2) forms an
````

### MC-STK-ERR-2134

`algebra.tex` — 26112, 26113; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26112-L26113) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Bind the declared uppercase matrices Y and Z in their defining sentence.

Adverse evidence / qualification: The following products use exactly those matrices. A separate conceptual erratum records the additional image-versus-source type issue and its effect on the triple argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-let $y$ be
+let $Y$ be
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-let $z$ be
+let $Z$ be
````

### MC-STK-ERR-2135

`algebra.tex` — 26232; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26232) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the parentheses for the actual quotient cokernel.

Adverse evidence / qualification: The original map J/JI to R/I has kernel (J intersection I)/JI and cokernel R/(I+J); all eleven equivalences are checked with the original localization maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R/I + J
+R/(I + J)
````

### MC-STK-ERR-2136

`algebra.tex` — 26259; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26259) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Replace the repeated implication verb by its grammatical consequence.

Adverse evidence / qualification: When I lies in the prime, 1-y is outside it; x(1-y)=0 therefore kills the original x in the localization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some $y \in I$, implies
+for some $y \in I$, and hence
````

### MC-STK-ERR-2137

`algebra.tex` — 26419; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26419) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Cite the existence-and-uniqueness correspondence actually needed for an arbitrary closed generalization-stable set.

Adverse evidence / qualification: The earlier uniqueness lemma cannot supply the pure ideal. The next lemma supplies it by the explicit x=xy construction. The full converse rank-stratum proof is checked separately.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{lemma-pure-ideal-determined-by-zero-set}
+\ref{lemma-pure-open-closed-specializations}
````

### MC-STK-ERR-2138

`algebra.tex` — 26429; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26429) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Terminate the localization equality before the next sentence.

Adverse evidence / qualification: The actual base-changed free module remains nonzero under a generalization, giving the stated support implication.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R_{\mathfrak p}$
+R_{\mathfrak p}$.
````

### MC-STK-ERR-2139

`algebra.tex` — 26738, 26740; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26738-L26740) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specify the missing augmentation and degree-minus-one syzygy binding without changing the source split-tail argument.

Adverse evidence / qualification: For n=0 the first projective object is M itself. Only nonnegative e defines P_e as a differential kernel; the separate P_-1=M convention avoids an undefined d_-1.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
-$d_e : F_e \to F_{e - 1}$. By
+the augmentation by $d_0 : F_0 \to M$ and the differentials by
+$d_e : F_e \to F_{e - 1}$ for $e \geq 1$. Put $P_{-1}=M$
+and $P_e = \Ker(d_e)$ for $e \geq 0$. By
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we see that $P_e = \Ker(d_e)$ is projective for $e \geq n - 1$.
+we see that $P_e$ is projective for $e \geq n - 1$.
````

### MC-STK-ERR-2140

`algebra.tex` — 26924; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26924) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Require finite depth before forming the integer-indexed resolution.

Adverse evidence / qualification: The original convention gives depth(0)=positive infinity, so F_(d-e) is undefined for M=0. Nonzero finite modules have integer depth; the zero module separately has its zero resolution and does not affect the global bound.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Every finite $R$-module
+Every nonzero finite $R$-module
````

### MC-STK-ERR-2141

`algebra.tex` — 26947; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26947) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the required preposition in the citation sentence.

Adverse evidence / qualification: The cited localization lemma proves the stated bound using the actual localized projective resolution.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We saw, Lemma
+We saw in Lemma
````

### MC-STK-ERR-2142

`algebra.tex` — 27165; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27165) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Exclude the zero ring from equality of global and Krull dimensions with an attained prime.

Adverse evidence / qualification: The zero ring has global dimension zero but empty spectrum of dimension negative infinity, and it has no prime or maximal ideal attaining a bound. The fixed-n equivalence for nonzero rings follows from exact local dimensions and the attained finite supremum.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $R$ be a Noetherian ring.
+Let $R$ be a nonzero Noetherian ring.
````

### MC-STK-ERR-2143

`algebra.tex` — 27206; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27206) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Cite the preceding theorem proving the stated exact global dimension.

Adverse evidence / qualification: The equality is true. The new reference proves equality, whereas the old reference states an upper bound. There is no need to weaken the assertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{proposition-regular-finite-gl-dim}
+\ref{proposition-finite-gl-dim-regular}
````

### MC-STK-ERR-2144

`algebra.tex` — 27338, 27339; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27338-L27339) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Join the original if-clause to its conclusion.

Adverse evidence / qualification: Going up lifts any larger contracted prime above the original maximal ideal; maximality forces equality. The two reports concern the same punctuation defect.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a maximal ideal.
+is a maximal ideal,
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then the inverse image
+then the inverse image
````

### MC-STK-ERR-2145

`algebra.tex` — 27491; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27491) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing copula.

Adverse evidence / qualification: The finite-flat map is faithfully flat and injective, so integral dimension equality applies. The other case follows from depth and the assumed dimension bound.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $R$ Cohen-Macaulay.
+Assume $R$ is Cohen-Macaulay.
````

### MC-STK-ERR-2146

`algebra.tex` — 27572; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27572) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the prime declaration.

Adverse evidence / qualification: The prime is the original preimage of q under R[x] to S; the exact localized quotient comparison is proved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\mathfrak q
+Denote by $\mathfrak q
````

### MC-STK-ERR-2147

`algebra.tex` — 27635; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27635) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the generic-point hypothesis in the auxiliary topological assertion.

Adverse evidence / qualification: An infinite cofinite space is Noetherian and every point is closed, but it is infinite and has no generic point for its irreducible whole space. The original fibre is a spectrum and therefore sober; finite irreducible components then give the claimed finite set.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A Noetherian topological space
+A sober Noetherian topological space
````

### MC-STK-ERR-2148

`algebra.tex` — 27672; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27672) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing preposition in the declaration of the original residue classes.

Adverse evidence / qualification: The residue field and images are those of the original quotient map; only wording changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\alpha_i
+Denote by $\alpha_i
````

### MC-STK-ERR-2149

`algebra.tex` — 27673; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27673) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the defining verb for the equality specifying the intermediate fields.

Adverse evidence / qualification: The original finite field tower and kappa_0=k remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\kappa_i
+Set $\kappa_i
````

### MC-STK-ERR-2150

`algebra.tex` — 27872; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27872) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the k-algebra noun used elsewhere in this section.

Adverse evidence / qualification: The supplied proposal changes k algebra to k-algebra; it does not require hyphenating finite type. The mathematical hypothesis is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finite type $k$ algebra
+finite type $k$-algebra
````

### MC-STK-ERR-2151

`algebra.tex` — 27888; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27888) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the irreducible components the plural subject of all have dimension.

Adverse evidence / qualification: The local CM chain theorem makes every component through the closed point have the local dimension; the original sentence mistakenly makes a dimension have dimension.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence, the dimension of the irreducible
+Hence, the irreducible
````

### MC-STK-ERR-2152

`algebra.tex` — 27944; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27944) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restrict the weight inequalities to the actual defined indices.

Adverse evidence / qualification: The first required inequality is for e_1 against the tail beginning at A_2e_2. There is no e_0; the n=1 case is direct.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-If for each $i$ we have
+If for $i = 2, \ldots, n$ we have
````

### MC-STK-ERR-2153

`algebra.tex` — 28017; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28017) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Match the verb to the plural integers.

Adverse evidence / qualification: The same original integer weights and inverse substitutions are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists integers
+there exist integers
````

### MC-STK-ERR-2154

`algebra.tex` — 28052; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28052) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the dimension assertion actually proved by the cited lemma.

Adverse evidence / qualification: Integer-coefficient generators come from the original substitutions and induction. Integral dimension equality proves r=dim(S), not that last generator assertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The last assertion follows from Lemma
+The assertion that $r = \dim(S)$ follows from Lemma
````

### MC-STK-ERR-2155

`algebra.tex` — 28059, 28180, 28224, 28272; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28059-L28272) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the k-algebra noun in all four reported declarations.

Adverse evidence / qualification: The same ring hypotheses, original points and exact quotient residue fields remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finite type $k$ algebra
+finite type $k$-algebra
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finite type $k$ algebra
+finite type $k$-algebra
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finite type $k$ algebra
+finite type $k$-algebra
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finite type $k$ algebras
+finite type $k$-algebras
````

### MC-STK-ERR-2156

`algebra.tex` — 28094; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28094) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Give the actual coefficient ring for the polynomial in x_n.

Adverse evidence / qualification: The source monic convention additionally uses the nonzero original leading coefficient a. The editorial proof tracks h, h/a, the source scaling by a, and sigma inverse explicitly; it does not silently discard the unit or rename the target prime.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$k[x_1, \ldots, x_n]$
+$k[x_1, \ldots, x_{n-1}]$
````

### MC-STK-ERR-2157

`algebra.tex` — 28343; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28343) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing preposition in the two-point declaration.

Adverse evidence / qualification: Both reports concern the same line; the corresponding prime labels and common fibre comparison remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $x'
+Denote by $x'
````

### MC-STK-ERR-2158

`algebra.tex` — 28377; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28377) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the finite verb in the dimension-equality sentence.

Adverse evidence / qualification: The exact common fibre is proved before using the equality. Minimal primes over q S_K contract to q by going down, so the zero-height-jump choice is justified.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-equality by Lemma
+equality follows from Lemma
````

### MC-STK-ERR-2159

`algebra.tex` — 28522; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28522) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the subordinate since clause from its conclusion.

Adverse evidence / qualification: The minimal comma repairs the clause boundary while preserving the original extension-of-free-modules argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-also we conclude
+also, we conclude
````

### MC-STK-ERR-2160

`algebra.tex` — 28545; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28545) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the missing preposition in the image declaration.

Adverse evidence / qualification: The original quotient and coefficient-model construction remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote $\overline{g}$
+denote by $\overline{g}$
````

### MC-STK-ERR-2161

`algebra.tex` — 28593; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28593) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair both declarations on the same line.

Adverse evidence / qualification: K and all three tensor objects keep their original definitions; no kernel or torsion is discarded.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $K$ the fraction field of $R$. Denote
+Denote by $K$ the fraction field of $R$. Set
````

### MC-STK-ERR-2162

`algebra.tex` — 28771; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28771) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the quotient by an ideal of the actual algebra S.

Adverse evidence / qualification: J_i is defined as an ideal of S in the preceding sentence; R/J_i is generally undefined. All three reports identify this one operation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R/J_i$
+$S/J_i$
````

### MC-STK-ERR-2163

`algebra.tex` — 28868-28869; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28868-L28869) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair the clause order of the final dense-open inference.

Adverse evidence / qualification: The original equality of good loci and finite intersection argument remain unchanged.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Hence as we've just finished proving the right two opens are dense also
-the open on the left is dense.
+Hence, as we have just proved that the two opens on the right are dense,
+the open on the left is dense as well.
````

### MC-STK-ERR-2164

`algebra.tex` — 28494; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28494) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the source project convention for the empty generic spectrum.

Adverse evidence / qualification: This unreported source inconsistency follows from the explicit definition at topology.tex:1391-1419, particularly 1410, and its restatement at algebra.tex:43890-43895. The empty-fibre induction base is still valid; only its dimension label changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$d = -1$
+$d = -\infty$
````

### MC-STK-ERR-2165

`algebra.tex` — 28906; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L28906) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the original valuation declaration.

Adverse evidence / qualification: The valuation and its ordered group are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $v$
+Denote by $v$
````

### MC-STK-ERR-2166

`algebra.tex` — 29075; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29075) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Apply the local lemma to its actual local ring while preserving the original semilocal theorem.

Adverse evidence / qualification: The separate proof clears the original monic-equation denominators and uses CRT to extend the finite local overring without changing other maximal localizations. The optional blowup is checked by its actual charts and the proper finite-fibre theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$(R, \mathfrak m)$
+$(R_{\mathfrak m}, \mathfrak mR_{\mathfrak m})$
````

### MC-STK-ERR-2167

`algebra.tex` — 29135; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29135) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Parenthesize the original coefficient residue field.

Adverse evidence / qualification: The preceding phrase for all n>=0 already provides the direct-sum degree range; no second operation is needed. The exact graded map is proved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A/\mathfrak m[T]$
+$(A/\mathfrak m)[T]$
````

### MC-STK-ERR-2168

`algebra.tex` — 29436, 29439; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29436-L29439) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Complete the residual unit case by retaining the three original unit factors in both equalities.

Adverse evidence / qualification: These operations are disjoint from MC-STK-ERR-0633 and preserve its valid zero-case contribution. The note proves precisely how the source uniqueness axiom applies to the original equations with their displayed units.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-$a = a_1 \ldots a_n$, $b = b_1 \ldots b_m$, and $c = c_1 \ldots c_r$.
+$a = u_a a_1 \ldots a_n$, $b = u_b b_1 \ldots b_m$, and
+$c = u_c c_1 \ldots c_r$, with units $u_a, u_b, u_c \in R^*$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a_1 \ldots a_n b_1 \ldots b_m = c_1 \ldots c_r x
+u_a u_b a_1 \ldots a_n b_1 \ldots b_m = u_c c_1 \ldots c_r x
````

### MC-STK-ERR-2169

`algebra.tex` — 29687; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29687) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the colon introducing the original equivalences.

Adverse evidence / qualification: The three conditions and all hypotheses are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The following are equivalent
+The following are equivalent:
````

### MC-STK-ERR-2170

`algebra.tex` — 29798; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29798) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing complementizer in the original parenthetical instruction.

Adverse evidence / qualification: The actual multiplication-by-b injection and quotient maps prove additivity. The separate citation-hypothesis issue is recorded in ALGEBRA-RECON-734.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Use length is additive
+Use that length is additive
````

### MC-STK-ERR-2171

`algebra.tex` — 29891; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29891) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the sentence-ending period before Hence.

Adverse evidence / qualification: The original common denominator kills the finite quotient. This is punctuation only, not a change of the local finiteness argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some $n$
+for some $n$.
````

### MC-STK-ERR-2172

`algebra.tex` — 29928; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L29928) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the period after the original exact sequence.

Adverse evidence / qualification: The actual inclusion and quotient maps give the asserted short exact sequence, and all terms have finite length.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-0 \to M'/M \to M''/M \to M''/M' \to 0
+0 \to M'/M \to M''/M \to M''/M' \to 0.
````

### MC-STK-ERR-2173

`algebra.tex` — 30205; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30205) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the original point designation.

Adverse evidence / qualification: The fibre point and the canonical localized quotient map are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2174

`algebra.tex` — 30206; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30206) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the colon introducing the equivalent fibre conditions.

Adverse evidence / qualification: All six conditions are proved on the original fibre, including the actual lift of an isolating fibre element to its numerator in S.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-The following are equivalent
+The following are equivalent:
````

### MC-STK-ERR-2175

`algebra.tex` — 30304; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30304) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the finite verb in the original assumption.

Adverse evidence / qualification: The source surjective comparison map remains unchanged. Its stronger finite-map version is proved separately in ALGEBRA-RECON-747.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $R \to S$ of finite type
+Assume $R \to S$ is of finite type
````

### MC-STK-ERR-2176

`algebra.tex` — 30353; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30353) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the redundant then following the causal clause.

Adverse evidence / qualification: The original witnesses b and c and the image c prime are retained; their product excludes every other point of the composite fibre.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then there exist
+there exist
````

### MC-STK-ERR-2177

`algebra.tex` — 30770; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30770) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the period terminating the original displayed assertion.

Adverse evidence / qualification: Every coefficient and exponent in the original relation is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-b'_{m - 1}x^{m - 1} + b_{m - 2}x^{m - 2} + \ldots + b_0 = 0
+b'_{m - 1}x^{m - 1} + b_{m - 2}x^{m - 2} + \ldots + b_0 = 0.
````

### MC-STK-ERR-2178

`algebra.tex` — 30791, 30857; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L30791-L30857) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the reported compound noun and propagate the same correction to the second occurrence in the same induction.

Adverse evidence / qualification: The two exact occurrences have the same construction. The differently arranged sub R-algebra phrase at 30894 is not changed. Both proposed intervals are disjoint from the canonical example and localization corrections.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R$-sub algebra
+$R$-subalgebra
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R$-sub algebra
+$R$-subalgebra
````

### MC-STK-ERR-2179

`algebra.tex` — 31080; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31080) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Terminate the displayed product-decomposition sentence.

Adverse evidence / qualification: Both factor maps and their inverse addition map remain unchanged. The selected factor is proved to equal the completion through the original idempotent.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R_\mathfrak p^\wedge \otimes_R S = A \times B
+R_\mathfrak p^\wedge \otimes_R S = A \times B.
````

### MC-STK-ERR-2180

`algebra.tex` — 31097; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31097) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the preposition under for the image through the displayed map.

Adverse evidence / qualification: The original natural projection is checked on all pure tensors using an actual equality g^(m+n)y=g^m c in S, retaining the localization-kernel exponent.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is the image of $y'$ by the composition
+is the image of $y'$ under the composition
````

### MC-STK-ERR-2181

`algebra.tex` — 31226; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31226) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the terminal period in the original refined-chart statement.

Adverse evidence / qualification: OCC-01428 quotes an unrelated phrase, but its stated locus does have this omission. Its quote is not adopted as source text. The exact contraction is proved through the coefficient injection and all original denominators.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(\mathfrak p, x_{r + 1}, \ldots, x_n)R_f[x_1, \ldots, x_n]$
+(\mathfrak p, x_{r + 1}, \ldots, x_n)R_f[x_1, \ldots, x_n]$.
````

### MC-STK-ERR-2182

`algebra.tex` — 31337; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31337) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the actual spectrum-map declaration.

Adverse evidence / qualification: The report quote refers to a composition, which is not the source wording at this locus. The actual sentence still lacks by; the original base-change map on spectra is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and denote $f :
+and denote by $f :
````

### MC-STK-ERR-2183

`algebra.tex` — 31386; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31386) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the period after the original dimension equality.

Adverse evidence / qualification: The next sentence begins In fact. Neither the nonempty-fibre assumption nor either original fibre ring changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim(S \otimes_R k) = \dim(S \otimes_R K)
+\dim(S \otimes_R k) = \dim(S \otimes_R K).
````

### MC-STK-ERR-2184

`algebra.tex` — 31577; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31577) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the terminal period after the original cross-reference.

Adverse evidence / qualification: The module-lifting argument remains unchanged, including the full relation A_Rprime=s A_prime and the distinction between surjectivity before and after localization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemma \ref{lemma-construct-fp-module-from-localization}
+Lemma \ref{lemma-construct-fp-module-from-localization}.
````

### MC-STK-ERR-2185

`algebra.tex` — 31764; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31764) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the plural count noun in the introductory sentence.

Adverse evidence / qualification: The change leaves the stated role of the preliminary lemmas unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-prove result using
+prove results using
````

### MC-STK-ERR-2186

`algebra.tex` — 31782; source correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31782) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Give the initial object its actual target A.

Adverse evidence / qualification: The objects are finitely presented R-algebras equipped with a map to A. The structural map R to A supplies the required object for arbitrary A.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R \to R$ is an object
+$R \to A$ is an object
````

### MC-STK-ERR-2187

`algebra.tex` — 31816; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31816) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing verb in the preorder declaration.

Adverse evidence / qualification: The indexing order and transition directions remain the original ones.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a preordered set.
+be a preordered set.
````

### MC-STK-ERR-2188

`algebra.tex` — 31865; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31865) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing preposition.

Adverse evidence / qualification: The actual finite generator and relation pairs remain unchanged. The fixed-generator subsystem has its own proved colimit and is not claimed cofinal among all finite generator subsets.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-equal the set
+equal to the set
````

### MC-STK-ERR-2189

`algebra.tex` — 31948; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31948) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing article.

Adverse evidence / qualification: The class of finitely presented algebras is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of given type
+of a given type
````

### MC-STK-ERR-2190

`algebra.tex` — 31958; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31958) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the source standard spelling of R-algebra.

Adverse evidence / qualification: This changes no map or factorization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R$ algebra map
+$R$-algebra map
````

### MC-STK-ERR-2191

`algebra.tex` — 31985; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L31985) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the variance and plural in the categorical introduction.

Adverse evidence / qualification: The following source lemmas descend objects and arrows with eventual equality. The explicit stage-object category and its equivalence are proved separately; an inverse limit is not the stated construction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the limit of the category
+the colimit of the categories
````

### MC-STK-ERR-2192

`algebra.tex` — 32124; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32124) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the map used in the fourth item explicit in that item.

Adverse evidence / qualification: The earlier items introduce their own maps. This local declaration supplies the domain, codomain and algebra structure already required by the following tensor formula; it adds no stronger hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A$-algebra, and
+$A$-algebra, and $u : B \to C$ is an $A$-algebra map such that
````

### MC-STK-ERR-2193

`algebra.tex` — 32235, 32294; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32235-L32294) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in both original ring-map declarations.

Adverse evidence / qualification: The original restrictions of phi, subrings and prime localizations are retained. Complete local and nonlocal proofs remain editorial.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

### MC-STK-ERR-2194

`algebra.tex` — 32350; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32350) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural for the system of local homomorphisms.

Adverse evidence / qualification: Each indexed map retains the original source and target local rings.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-local homomorphism $
+local homomorphisms $
````

### MC-STK-ERR-2195

`algebra.tex` — 32377; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32377) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the compatible local transition maps explicit in the base-system choice.

Adverse evidence / qualification: The two-stage system Z_(2) to Q has local rings but yields a nonlocal stage map in the construction for the identity Q to Q. The source existence theorem is valid using the preceding local subring system; the proof of locality of its structural maps is supplied editorially.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-local and essentially of finite type over $\mathbf{Z}$.
+local and essentially of finite type over $\mathbf{Z}$,
+and with local transition maps.
````

### MC-STK-ERR-2196

`algebra.tex` — 32380; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32380) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the declaration of the transported original polynomials.

Adverse evidence / qualification: All original coefficients and their actual representatives and transition maps are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote
+denote by
````

### MC-STK-ERR-2197

`algebra.tex` — 32388; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32388) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Complete the inverse-image prime declaration.

Adverse evidence / qualification: This is the actual contraction of the original prime; no injectivity of the polynomial quotient map is assumed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Set $\mathfrak q_\lambda$ the inverse
+Set $\mathfrak q_\lambda$ to be the inverse
````

### MC-STK-ERR-2198

`algebra.tex` — 32416, 32418; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32416-L32418) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the intended universal negative with matching singular grammar.

Adverse evidence / qualification: The original element y_(n+1)^2 is proved nonzero before quotienting. The full calculation proves failure for every later transition, not only the adjacent ones; no author counterexample is replaced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-All the maps
+None of the maps
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-are not localizations (i.e., isomorphisms in this case)
+is a localization (i.e., an isomorphism in this case)
````

### MC-STK-ERR-2199

`algebra.tex` — 32662; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32662) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing verb in the Cohen-Macaulay hypothesis.

Adverse evidence / qualification: The original dimension identity and regularity hypotheses remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S$ Cohen-Macaulay
+$S$ is Cohen-Macaulay
````

### MC-STK-ERR-2200

`algebra.tex` — 32674; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32674) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply punctuation before the coordinated reasons for the display.

Adverse evidence / qualification: The strict dimension inequality and every original quotient are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\dim(S/\mathfrak m_R S)
+\dim(S/\mathfrak m_R S),
````

### MC-STK-ERR-2201

`algebra.tex` — 32772, 32794, 32871, 32888; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32772-L32888) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the three reported maximal-ideal declarations and the identical unreported stage declaration.

Adverse evidence / qualification: The additional occurrence at 32794 is independently present in the source. No ideals or residue fields are changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

### MC-STK-ERR-2202

`algebra.tex` — 32813; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32813) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use a weak upper bound in the directed preorder.

Adverse evidence / qualification: A one-element index set satisfies the hypotheses and has no strictly larger index. The proof only needs a common upper bound.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\lambda' > \lambda
+\lambda' \geq \lambda
````

### MC-STK-ERR-2203

`algebra.tex` — 32841, 32842, 32843, 32845; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32841-L32845) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Choose an actual numerator in the earlier scalar-extended module and retain its tensor base.

Adverse evidence / qualification: The earlier module need not inject into its localization. The denominator maps to a unit in the target, which puts the chosen numerator in the earlier kernel. The complete generator argument is editorial.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then for some $w \in W$ we have
+Write $x = y/w$ for some $w \in W$ and
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$wx \in M_\lambda/\mathfrak m_\lambda M_\lambda \otimes \kappa$.
+$y \in M_\lambda/\mathfrak m_\lambda M_\lambda \otimes_{\kappa_\lambda} \kappa$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence $wx \in \Ker(\Psi_\lambda)$. Hence $wx$ is a linear
+Hence $y \in \Ker(\Psi_\lambda)$. Hence $y$ is a linear
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence $wx = 0$
+Hence the image of $y$ is zero
````

### MC-STK-ERR-2204

`algebra.tex` — 32925, 33011; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32925-L33011) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the original ideal declarations.

Adverse evidence / qualification: The ideals remain the original inverse-image and maximal ideals with their original base rings.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

### MC-STK-ERR-2205

`algebra.tex` — 32927; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32927) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the actual quotient base in the quotient approximation system.

Adverse evidence / qualification: The limit is the map R/I to S/IS. Keeping the unquotiented stage base would apply the approximation lemma to different data.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R_\lambda \to S_\lambda/I_\lambda S_\lambda$
+$R_\lambda/I_\lambda \to S_\lambda/I_\lambda S_\lambda$
````

### MC-STK-ERR-2206

`algebra.tex` — 32933; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32933) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the quotient base over which eventual flatness is proved.

Adverse evidence / qualification: Flatness over R_lambda itself is not asserted and does not follow for this quotient module.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is flat for all
+is flat over $R_\lambda/I_\lambda$ for all
````

### MC-STK-ERR-2207

`algebra.tex` — 32975; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32975) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Keep the actual localization in the quotient-module flatness comparison.

Adverse evidence / qualification: The original systems only give localizations of the raw base changes. Localization preserves flatness and commutes with the required Tor complex; the full proof retains the original multiplicative set.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as it is a base
+as it is a localization of a base
````

### MC-STK-ERR-2208

`algebra.tex` — 33040; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33040) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore both original relation families in the presentation over R_lambda.

Adverse evidence / qualification: The g-relations were imposed over S_lambda, which already had the f-relations. They cannot be dropped on returning to a polynomial algebra over R_lambda.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-(g_{1, \lambda}, \ldots, g_{v, \lambda})
+(f_{1, \lambda}, \ldots, f_{u, \lambda},
+g_{1, \lambda}, \ldots, g_{v, \lambda})
````

### MC-STK-ERR-2209

`algebra.tex` — 33049; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33049) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Place the descended original matrix over the primed ring.

Adverse evidence / qualification: The original matrix is over S_prime and the following cokernel uses free S_prime_lambda modules. Its entries need not come from S_lambda.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S_{\lambda_3}
+S'_{\lambda_3}
````

### MC-STK-ERR-2210

`algebra.tex` — 33108-33110; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33108-L33110) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore localization in both endpoint comparisons.

Adverse evidence / qualification: The reported first equality and the adjacent module equality both fail in the explicit Q to Q(t) example. The original matrices and tensor bases remain unchanged.

````diff
--- original
+++ replacement
@@ -1,3 +1,4 @@
-Pick such a $\lambda$. Then $S = S_\lambda \otimes_{R_\lambda} R$
-is flat over $R$, and $M = M_\lambda \otimes_{S_\lambda} S$
-is flat over $S$ (since the base change of a flat module is flat).
+Pick such a $\lambda$. Then $S$ is a localization of
+$S_\lambda \otimes_{R_\lambda} R$, hence is flat over $R$.
+Also $M$ is a localization of $M_\lambda \otimes_{S_\lambda} S$,
+hence is flat over $S$ (base change and localization preserve flatness).
````

### MC-STK-ERR-2211

`algebra.tex` — 33136; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33136) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Begin with the finite-type hypothesis actually given.

Adverse evidence / qualification: Finite presentation is the conclusion being established by finite generation of the original kernel J.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-essentially of finite presentation
+essentially of finite type
````

### MC-STK-ERR-2212

`algebra.tex` — 33138; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33138) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use Let with the existing be declaration.

Adverse evidence / qualification: The inverse-image prime and original quotient presentation remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Let
````

### MC-STK-ERR-2213

`algebra.tex` — 33158; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33158) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the two distinct ideals appearing in the quotient map.

Adverse evidence / qualification: The exact common-algebra argument uses B/J_prime and B/J_doubleprime as finitely presented B-modules, not an assumed finite presentation of S.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$J' \subset J' \subset J$
+$J' \subset J'' \subset J$
````

### MC-STK-ERR-2214

`algebra.tex` — 33198-33200, 33209-33210; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33198-L33210) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Choose a support prime and justify flatness at every stalk, including zero stalks.

Adverse evidence / qualification: A nonzero fibre module need not be supported at every prime of its fibre ring, as k times k with module k times zero shows. The original nil ideal lies in every contracted prime. The weaker support hypothesis is proved only in the separate extension.

````diff
--- original
+++ replacement
@@ -1,3 +1,4 @@
-$S' \otimes_S \kappa(\mathfrak q)$ is nonzero and hence
-there exists a prime $\mathfrak q' \subset S'$ lying over
-$\mathfrak q$ (Lemma \ref{lemma-in-image}). Let
+choose a prime in the support of this finite fibre module.
+Its inverse image $\mathfrak q' \subset S'$ lies over
+$\mathfrak q$ and $M_{\mathfrak q'} \ne 0$
+(see also Lemma \ref{lemma-in-image}). Let
````

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-Since $\mathfrak q'$ was an arbitrary prime of $S'$ we also
-see that $M$ is flat over $S$ (Lemma \ref{lemma-flat-localization}).
+For every $\mathfrak q' \in \Supp_{S'}(M)$ the same local argument applies;
+at primes outside this support, $M_{\mathfrak q'} = 0$ is flat.
+Thus $M$ is flat over $S$ (Lemma \ref{lemma-flat-localization}).
````

### MC-STK-ERR-2215

`algebra.tex` — 33242; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33242) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural verb for the listed elements.

Adverse evidence / qualification: The original ordered sequence and its local regularity claim are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-forms a regular
+form a regular
````

### MC-STK-ERR-2216

`algebra.tex` — 33241; source hypothesis correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33241) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Add the missing nonempty-zero-locus hypothesis to the dimension equality.

Adverse evidence / qualification: For S=k[x], d=i=1 and f_1=1 the displayed upper bound holds but equality fails. Local regularity on the empty locus is merely vacuous. The later use is at a fibre containing an actual zero-locus point.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
+$V(f_1, \ldots, f_i) \ne \varnothing$ and
 $\dim V(f_1, \ldots, f_i) \leq d - i$.
````

### MC-STK-ERR-2217

`algebra.tex` — 33333; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33333) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Complete the original coordinated ring-map hypotheses.

Adverse evidence / qualification: No equidimensionality hypothesis is silently added; the original lemma is proved in its full scope separately.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is finite type, flat
+is of finite type and flat
````

### MC-STK-ERR-2218

`algebra.tex` — 33398; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33398) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Perform the promised localization before using the chosen fractions as global equations.

Adverse evidence / qualification: Choose their actual denominators outside q and invert the finite product. The elements remain in the original minor ideal and their fibre images remain the specified ordered regular sequence.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
 form a regular sequence in $S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}$.
+After further localizing away from $\mathfrak q$, take these same
+fraction representatives as elements of $I_i \subset S$.
````

### MC-STK-ERR-2219

`algebra.tex` — 33465; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33465) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the singular attributive noun.

Adverse evidence / qualification: The original polynomial-fibre global dimension statement remains valid before localization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-fibres rings
+fibre rings
````

### MC-STK-ERR-2220

`algebra.tex` — 33487; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33487) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the bound on the localized polynomial-fibre global dimension.

Adverse evidence / qualification: At a generic point of a polynomial line the local fibre is a field, of global dimension zero. The nth syzygy argument needs only the upper bound.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is $n$
+is at most $n$
````

### MC-STK-ERR-2221

`algebra.tex` — 33469, 33471; mathematical correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33469-L33471) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Handle the zero-variable presentation and define the first syzygy at n=1.

Adverse evidence / qualification: The printed formula has undefined negative-index resolution terms in these cases. The repair keeps the original nth-syzygy formula for every n>=2. Zero syzygies are free of rank zero and do not require the nonzero-module citation.

````diff
--- original
+++ replacement
@@ -1 +1,4 @@
+If $n = 0$, then $S = R$ and the finite flat module $M_{\mathfrak q}$
+is free, including rank zero. Its basis spreads after a localization,
+proving the claim. Hence assume $n \geq 1$.
 Choose a resolution $F_\bullet$ of $M$ over $S$ with each
````

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-Let $K_n = \Ker(F_{n-1} \to F_{n-2})$. Note that
+Let $K_1 = \Ker(F_0 \to M)$ and, for $n \geq 2$,
+let $K_n = \Ker(F_{n-1} \to F_{n-2})$. Note that
````

### MC-STK-ERR-2222

`algebra.tex` — 33531, 33534; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33531-L33534) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply both predicate verbs in the paired locus descriptions.

Adverse evidence / qualification: All original local rings, polynomial variables and relative dimensions are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{ flat over }
+\text{ is flat over }
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{ CM and }
+\text{ is CM and }
````

### MC-STK-ERR-2223

`algebra.tex` — 33540; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33540) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use Set for the displayed equality defining the contraction.

Adverse evidence / qualification: This is the original inverse-image prime, not a changed ring or coordinate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Set
````

### MC-STK-ERR-2224

`algebra.tex` — 33575; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33575) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the spectrum as the topological ambient space.

Adverse evidence / qualification: The point set is the set of prime ideals and the proof already uses principal opens of its spectrum.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-open in $S$
+open in $\Spec(S)$
````

### MC-STK-ERR-2225

`algebra.tex` — 33610; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33610) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the algebra compound spelling used in the chapter.

Adverse evidence / qualification: An additional finite-type hyphen is not needed; mathematical hypotheses are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$k$ algebra
+$k$-algebra
````

### MC-STK-ERR-2226

`algebra.tex` — 33645; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33645) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the fixed relative dimension in the stated local goal.

Adverse evidence / qualification: The existing final argument proves both conditions through the original d-variable quasi-finite chart. This is a clarification of what the proof establishes, not an added theorem hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
-all fibre rings of $R \to S_g$ are Cohen-Macaulay.
+all fibre rings of $R \to S_g$ are Cohen-Macaulay and
+$\dim_{\mathfrak r}(S_g/R) = d$ for every prime $\mathfrak r \subset S_g$.
````

### MC-STK-ERR-2227

`algebra.tex` — 33663; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33663) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the intervening condition with a comma.

Adverse evidence / qualification: The same original localization element and map are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g \not \in \mathfrak q$ the ring map
+$g \not \in \mathfrak q$, the ring map
````

### MC-STK-ERR-2228

`algebra.tex` — 33742, 33766; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33742-L33766) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the spectrum-map and stratum declarations.

Adverse evidence / qualification: The actual base-change map and dimension indexing remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote $
+denote by $
````

### MC-STK-ERR-2229

`algebra.tex` — 33758-33759; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33758-L33759) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the three original ring-map predicates parallel.

Adverse evidence / qualification: No condition or order is changed.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-which is (a) flat,
-(b) of finite presentation, (c) has
+which (a) is flat,
+(b) is of finite presentation, and (c) has
````

### MC-STK-ERR-2230

`algebra.tex` — 33762; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33762) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the empty-fibre convention explicit for the component factors.

Adverse evidence / qualification: For R=k times k and S=k[x] times k, the two dimension factors each have an empty fibre over the other base component. The intended finite dimension applies to nonempty fibres; zero factors are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-has all fibres equidimensional
+has all nonempty fibres equidimensional
````

### MC-STK-ERR-2231

`algebra.tex` — 33967; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L33967) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the sentence into its defining where clause.

Adverse evidence / qualification: The original directed colimit and all varying-ring actions are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\colim_i \Omega_{S_i/R_i}.
+\colim_i \Omega_{S_i/R_i},
````

### MC-STK-ERR-2232

`algebra.tex` — 34001; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34001) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the source of the lifted relation generators.

Adverse evidence / qualification: The upper-left relation module receives its vertical arrow from the lower-left relation module.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-lower right corner
+lower left corner
````

### MC-STK-ERR-2233

`algebra.tex` — 34014; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34014) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the ill-typed application of the map to a coefficient already in its target ring.

Adverse evidence / qualification: The coefficient s_l_prime lies in S_prime. The equality retains phi(s) on the left and the original indexed base generators.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\varphi(s_l')
+s_l'
````

### MC-STK-ERR-2234

`algebra.tex` — 34025; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34025) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing definite article.

Adverse evidence / qualification: The original fibre product and all diagram maps are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-have following
+have the following
````

### MC-STK-ERR-2235

`algebra.tex` — 34037; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34037) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the actual generators of the differential submodule.

Adverse evidence / qualification: The derivation vanishing condition kills differentials of the ring images, not the ring elements themselves.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-by the image of $R''$
+by the differentials of elements in the image of $R''$
````

### MC-STK-ERR-2236

`algebra.tex` — 34096; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34096) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the indefinite article.

Adverse evidence / qualification: The next source formula already extends the universal derivation. Its complete inverse proof retains the denominator squares and works with zero divisors.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a $A$-derivation
+an $A$-derivation
````

### MC-STK-ERR-2237

`algebra.tex` — 34093; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34093) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the introductory clause.

Adverse evidence / qualification: No change to the localization or canonical map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-To show (2) note
+To show (2), note
````

### MC-STK-ERR-2238

`algebra.tex` — 34115; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34115) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the exact-sequence sentence.

Adverse evidence / qualification: No left injectivity is introduced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-0
+0.
````

### MC-STK-ERR-2239

`algebra.tex` — 34123; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34123) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the notation declaration.

Adverse evidence / qualification: The original class in I/I squared is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-denote $
+denote by $
````

### MC-STK-ERR-2240

`algebra.tex` — 34130; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34130) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct agreement with the singular subject.

Adverse evidence / qualification: Linearity follows from the retained product rule modulo I.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-computation show
+computation shows
````

### MC-STK-ERR-2241

`algebra.tex` — 34184; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34184) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the displayed definition.

Adverse evidence / qualification: The full section-dependent derivation and inverse identities are proved in the editorial note.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x \longmapsto x - \beta(\alpha(x))
+x \longmapsto x - \beta(\alpha(x)).
````

### MC-STK-ERR-2242

`algebra.tex` — 34270; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34270) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the displayed comparison sentence.

Adverse evidence / qualification: Both tensor factor actions are retained and proved explicitly in the note.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega_{S/R}
+\Omega_{S/R}.
````

### MC-STK-ERR-2243

`algebra.tex` — 34278; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34278) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the established notation for the universal differential.

Adverse evidence / qualification: All three presentation relations, including additivity, are checked editorially.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-- d(ab)
+- \text{d}(ab)
````

### MC-STK-ERR-2244

`algebra.tex` — 34360; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34360) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the exact-sequence sentence.

Adverse evidence / qualification: The conormal term need only be finitely generated; no additional finite presentation or injectivity is assumed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-0
+0.
````

### MC-STK-ERR-2245

`algebra.tex` — 34371; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34371) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing article.

Adverse evidence / qualification: The finite-type conclusion is proved without assuming a finitely generated relation ideal.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is finitely generated
+is a finitely generated
````

### MC-STK-ERR-2246

`algebra.tex` — 34046; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34046) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the independently noticed singular existential agreement.

Adverse evidence / qualification: The original element in the fibre product remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exist an
+there exists an
````

### MC-STK-ERR-2247

`algebra.tex` — 34391-34392; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34391-L34392) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Declare the map and its target with their correct mathematical types.

Adverse evidence / qualification: The universal derivation and module remain exactly those constructed in the preceding source section.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Denote $\text{d} : B \to \Omega_{B/A}$
-the module of differentials with its universal $A$-derivation
+Denote by $\text{d} : B \to \Omega_{B/A}$
+the universal $A$-derivation into the module of differentials
````

### MC-STK-ERR-2248

`algebra.tex` — 34414; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34414) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the defining-equation sentence.

Adverse evidence / qualification: All factors and their order are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{d}b_0 \wedge \text{d}b_1 \wedge \ldots \wedge \text{d}b_p
+\text{d}b_0 \wedge \text{d}b_1 \wedge \ldots \wedge \text{d}b_p.
````

### MC-STK-ERR-2249

`algebra.tex` — 34498; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34498) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the displayed equality into its reformulation clause.

Adverse evidence / qualification: The original product-rule terms and their signs are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-- b \text{d}b' \wedge \text{d}(fc) \wedge \text{d}c'
+- b \text{d}b' \wedge \text{d}(fc) \wedge \text{d}c',
````

### MC-STK-ERR-2250

`algebra.tex` — 34535; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34535) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the absolute-complex declaration into its where clause.

Adverse evidence / qualification: The relative base remains the integers.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ldots
+\ldots,
````

### MC-STK-ERR-2251

`algebra.tex` — 34545; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34545) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the diagram sentence.

Adverse evidence / qualification: All four original ring maps are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+}.
````

### MC-STK-ERR-2252

`algebra.tex` — 34549; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34549) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the displayed functorial-map sentence.

Adverse evidence / qualification: The map remains induced by the original commutative square.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega^\bullet_{B/A} \longrightarrow \Omega^\bullet_{B'/A'}
+\Omega^\bullet_{B/A} \longrightarrow \Omega^\bullet_{B'/A'}.
````

### MC-STK-ERR-2253

`algebra.tex` — 34577; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34577) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the declaration of the projected derivative.

Adverse evidence / qualification: The original surjective module map is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $
+Denote by $
````

### MC-STK-ERR-2254

`algebra.tex` — 34591; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34591) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the lemma statement.

Adverse evidence / qualification: The quotient generator formula is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\text{d}f_0 \wedge \text{d}f_1 \wedge \ldots \wedge \text{d}f_p
+\text{d}f_0 \wedge \text{d}f_1 \wedge \ldots \wedge \text{d}f_p.
````

### MC-STK-ERR-2255

`algebra.tex` — 34607, 34609; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34607-L34609) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the completed diagram sentence from its explanation.

Adverse evidence / qualification: No diagram object or differential is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+}.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the description
+The description
````

### MC-STK-ERR-2256

`algebra.tex` — 34613; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34613) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the compound spelling.

Adverse evidence / qualification: The degree-zero vertical map remains the identity of B.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-left most
+leftmost
````

### MC-STK-ERR-2257

`algebra.tex` — 34633; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34633) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the display into the following which clause.

Adverse evidence / qualification: The minus sign and both wedge factors are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\omega_1 \wedge \text{d}_{B/A}(\omega_2)
+\omega_1 \wedge \text{d}_{B/A}(\omega_2),
````

### MC-STK-ERR-2258

`algebra.tex` — 34680; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34680) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the filtered inclusion-chain sentence.

Adverse evidence / qualification: The source filtered order convention is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\subset \ldots
+\subset \ldots.
````

### MC-STK-ERR-2259

`algebra.tex` — 34716; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34716) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the order of the universal factorization.

Adverse evidence / qualification: The universal map has domain M and target P, while alpha has domain P and target N; only alpha after the universal map has the declared type.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-D_{univ} \circ \alpha
+\alpha \circ D_{univ}
````

### MC-STK-ERR-2260

`algebra.tex` — 34721; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34721) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the unfinished citation placeholder without fabricating a reference.

Adverse evidence / qualification: The complete explicit construction immediately following proves representability. Its source argument is preserved; no unspecified category-theory theorem is presented as a newly read citation.

````diff
--- original
+++ replacement
@@ -1 +0,0 @@
- (insert future reference here)
````

### MC-STK-ERR-2261

`algebra.tex` — 34744; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34744) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the full alternating-relation sentence.

Adverse evidence / qualification: Every source term and sign is retained, and the full subset expansion is proved editorially.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-+(-1)^{k + 1}[g_0\ldots g_km]
++(-1)^{k + 1}[g_0\ldots g_km].
````

### MC-STK-ERR-2262

`algebra.tex` — 34770; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34770) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the principal-parts tower sentence.

Adverse evidence / qualification: The original quotient maps remain surjective.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-= M
+= M.
````

### MC-STK-ERR-2263

`algebra.tex` — 34814; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34814) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the displayed symbol-map definition.

Adverse evidence / qualification: The actual bilinear derivation construction is verified in the note.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\sigma_D : \Omega_{S/R} \otimes_S M \to N
+\sigma_D : \Omega_{S/R} \otimes_S M \to N.
````

### MC-STK-ERR-2264

`algebra.tex` — 34819; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34819) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition completing corresponds.

Adverse evidence / qualification: The source phrase begins on the preceding line; the representing-object arrow has the original correct direction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a map
+to a map
````

### MC-STK-ERR-2265

`algebra.tex` — 34879; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34879) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the given-data list after the ring diagram.

Adverse evidence / qualification: No ring or module map is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+},
````

### MC-STK-ERR-2266

`algebra.tex` — 34893; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34893) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the tower-diagram sentence.

Adverse evidence / qualification: The original functorial maps are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+}.
````

### MC-STK-ERR-2267

`algebra.tex` — 34898; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34898) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the independent clauses joined by but.

Adverse evidence / qualification: Both the source presentation and universal-property explanations remain.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-} but
+}, but
````

### MC-STK-ERR-2268

`algebra.tex` — 34938-34939; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34938-L34939) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the missing verb and singular operator in the diagonal identification.

Adverse evidence / qualification: Both reports describe the same sentence and exact defect; one shared operation resolves them. The actual universal map remains m to the class of 1 tensor m.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-and such that the universal differential operators of order $k$
-to the map
+and such that the universal differential operator of order $k$
+corresponds to the map
````

### MC-STK-ERR-2269

`algebra.tex` — 34943; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34943) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the specified tensor base and close the map declaration.

Adverse evidence / qualification: The two distinct local reports are resolved by one exact replacement of their shared line.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Consider the map $T : M \to S \otimes M$, $m \mapsto 1 \otimes m$
+Consider the map $T : M \to S \otimes_R M$, $m \mapsto 1 \otimes m$.
````

### MC-STK-ERR-2270

`algebra.tex` — 34984; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L34984) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the displayed double-commutator identity.

Adverse evidence / qualification: All four operator compositions and their signs remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-b' \circ \text{d} \circ b + b' \circ b \circ \text{d} = 0
+b' \circ \text{d} \circ b + b' \circ b \circ \text{d} = 0.
````

### MC-STK-ERR-2271

`algebra.tex` — 35002; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35002) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the nonnegative lower-order boundary needed by the generator criterion.

Adverse evidence / qualification: The source has no order-minus-one definition. The separate order-zero generator test is proved editorially, preserving the original filtered convention.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $D :
+Let $k \geq 1$. Let $D :
````

### MC-STK-ERR-2272

`algebra.tex` — 35019; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35019) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the product-commutator sentence.

Adverse evidence / qualification: The full two-term identity is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(D \circ g - g \circ D) \circ g' + g \circ (D \circ g' - g' \circ D)
+(D \circ g - g \circ D) \circ g' + g \circ (D \circ g' - g' \circ D).
````

### MC-STK-ERR-2273

`algebra.tex` — 35039; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35039) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the inference after the inline identity.

Adverse evidence / qualification: The original operator order and multiplication sides are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-L_{b'} \circ b + b' \circ L_b$
+L_{b'} \circ b + b' \circ L_b$,
````

### MC-STK-ERR-2274

`algebra.tex` — 35045; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35045) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the defining localization formula.

Adverse evidence / qualification: Both occurrences of the actual fraction m/g remain.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-E(m/g) = (1/g)(D(m) - E_g(m/g))
+E(m/g) = (1/g)(D(m) - E_g(m/g)).
````

### MC-STK-ERR-2275

`algebra.tex` — 35055; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35055) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the display into its which clause.

Adverse evidence / qualification: The proof below verifies full fraction equality, including torsion factors.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(1/g'g)(g'D(m) - g' E_g(m/g))
+(1/g'g)(g'D(m) - g' E_g(m/g)),
````

### MC-STK-ERR-2276

`algebra.tex` — 35057, 35058; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35057-L35058) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the actual base ring in both linearity assertions.

Adverse evidence / qualification: The lemma starts with A to B, so R is undefined here; the construction is A-linear.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R$-linear
+$A$-linear
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R$-linear
+$A$-linear
````

### MC-STK-ERR-2277

`algebra.tex` — 35072; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35072) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the first commutator display into its which clause.

Adverse evidence / qualification: The exact lower-order operator is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-E_b(m/g)
+E_b(m/g),
````

### MC-STK-ERR-2278

`algebra.tex` — 35081; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35081) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the inverse-scalar commutator display into its which clause.

Adverse evidence / qualification: The minus sign and both denominator factors remain explicit.

````diff
--- original
+++ replacement
@@ -1 +1 @@
--(1/g')E_{g'}(m/g'g)
+-(1/g')E_{g'}(m/g'g),
````

### MC-STK-ERR-2279

`algebra.tex` — 35100; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35100) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the actual order-zero case before invoking the lower-order generator criterion.

Adverse evidence / qualification: The complete tensor calculation works for every B-module N and uses no flatness.

````diff
--- original
+++ replacement
@@ -1 +1,3 @@
 It is clear that $D' = D \otimes \text{id}_N$ is $B$-linear.
+If $k = 0$, then $D'$ is $A \otimes_R B$-linear because $D$ is $A$-linear.
+For $k \geq 1$, we argue as follows.
````

### MC-STK-ERR-2280

`algebra.tex` — 35120; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35120) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the designation preposition.

Adverse evidence / qualification: The canonical polynomial algebra is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $R[S]$
+Denote by $R[S]$
````

### MC-STK-ERR-2281

`algebra.tex` — 35124; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35124) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural verb with the listed variables.

Adverse evidence / qualification: The original unordered finite sequences include the empty sequence.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-ranges
+range
````

### MC-STK-ERR-2282

`algebra.tex` — 35151; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35151) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the designation preposition.

Adverse evidence / qualification: The original degree-one homology notation is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-We will denote
+We will denote by
````

### MC-STK-ERR-2283

`algebra.tex` — 35163; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35163) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the augmentation sentence.

Adverse evidence / qualification: The separate category qualification is recorded independently.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-P_\bullet \longrightarrow S
+P_\bullet \longrightarrow S.
````

### MC-STK-ERR-2284

`algebra.tex` — 35168; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35168) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the simplicial-module definition sentence.

Adverse evidence / qualification: The original unnormalized associated chain complex is retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega_{P_\bullet/R} \otimes_{P_\bullet} S
+\Omega_{P_\bullet/R} \otimes_{P_\bullet} S.
````

### MC-STK-ERR-2285

`algebra.tex` — 35196, 35197; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35196-L35197) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make both already specified tensor bases explicit.

Adverse evidence / qualification: The preceding defining display already fixes P; this is a notation clarification, not a change of module.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes S
+\otimes_P S
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes S
+\otimes_P S
````

### MC-STK-ERR-2286

`algebra.tex` — 35203; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35203) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the omitted subject.

Adverse evidence / qualification: The finite-variable presentation is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then will
+then we will
````

### MC-STK-ERR-2287

`algebra.tex` — 35231; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35231) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specify the bases of the functorial differential modules.

Adverse evidence / qualification: Each target scalar action is through the original square.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\Omega_{P/R} \otimes S \to \Omega_{P'/R'} \otimes S'$
+$\Omega_{P/R} \otimes_P S \to \Omega_{P'/R'} \otimes_{P'} S'$
````

### MC-STK-ERR-2288

`algebra.tex` — 35257; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35257) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the introductory clause after its diagram.

Adverse evidence / qualification: The composition square is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+},
````

### MC-STK-ERR-2289

`algebra.tex` — 35305; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35305) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the missing introductory verb.

Adverse evidence / qualification: Both original presentation lifts are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi'$ morphisms
+$\varphi'$ be morphisms
````

### MC-STK-ERR-2290

`algebra.tex` — 35322; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35322) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Attach the homotopy identities to the map h.

Adverse evidence / qualification: The identities and both of their signs remain exactly those in the source.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-where the vertical maps are induced by $\varphi$, $\varphi'$ such that
+where the vertical maps are induced by $\varphi$ and $\varphi'$, and $h$ must satisfy
````

### MC-STK-ERR-2291

`algebra.tex` — 35339; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35339) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the article matching the pronounced ring letter.

Adverse evidence / qualification: The derivation is proved for the common action modulo the square ideal.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a $R$-derivation
+an $R$-derivation
````

### MC-STK-ERR-2292

`algebra.tex` — 35384; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35384) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Include the part that actually supplies the homotopies.

Adverse evidence / qualification: Part (3) alone only identifies the composite maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-maps by (3)
+maps by (2) and (3)
````

### MC-STK-ERR-2293

`algebra.tex` — 35430; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35430) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Continue the diagram sentence before its exact-row clause.

Adverse evidence / qualification: The bottom row deliberately has no leading zero.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+},
````

### MC-STK-ERR-2294

`algebra.tex` — 35498; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35498) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the square sentence.

Adverse evidence / qualification: The following explicit nullhomotopy is verified with its actual B-action.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+}.
````

### MC-STK-ERR-2295

`algebra.tex` — 35591; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35591) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the introductory verb be.

Adverse evidence / qualification: The multiplicative subset and original base ring are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S \subset A$ is
+$S \subset A$ be
````

### MC-STK-ERR-2296

`algebra.tex` — 35625; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35625) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the last item before the new sentence.

Adverse evidence / qualification: The actual disk differential is multiplication by g, not a silently substituted identity.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\NL(\alpha) \otimes_B B_g \oplus (B_g \xrightarrow{g} B_g)
+\NL(\alpha) \otimes_B B_g \oplus (B_g \xrightarrow{g} B_g).
````

### MC-STK-ERR-2297

`algebra.tex` — 35637, 35638, 35639, 35649, 35651, 35653; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35637-L35653) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specify all six reported tensor bases.

Adverse evidence / qualification: The original polynomial differential modules determine these bases; the maps are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes B_g
+\otimes_P B_g
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes B_g
+\otimes_{P[x]} B_g
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes B_g
+\otimes_{B[x]} B_g
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes B_g
+\otimes_{B[x]} B_g
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes B_g
+\otimes_{P[x]} B_g
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\otimes B_g
+\otimes_{B[x]} B_g
````

### MC-STK-ERR-2298

`algebra.tex` — 35661; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35661) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the predicate verb.

Adverse evidence / qualification: The square-zero retraction proves the asserted injectivity for every fraction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-J/J^2$ injective
+J/J^2$ is injective
````

### MC-STK-ERR-2299

`algebra.tex` — 35683; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35683) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the explicit splitting display.

Adverse evidence / qualification: Both the differential term and its complete denominator are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-B_g (g^{-2}\text{d}f + \text{d}x)
+B_g (g^{-2}\text{d}f + \text{d}x).
````

### MC-STK-ERR-2300

`algebra.tex` — 35704; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35704) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Match both verb and complement to each.

Adverse evidence / qualification: Changing only are to is would leave a singular subject with an inappropriate plural complement.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-are quasi-isomorphisms.
+is a quasi-isomorphism.
````

### MC-STK-ERR-2301

`algebra.tex` — 35711; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35711) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the comma splitting the coordinated complexes.

Adverse evidence / qualification: The additional hyphenation preference is not integrated; the complexes and assumptions are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A_1 \to A_0$, and
+$A_1 \to A_0$ and
````

### MC-STK-ERR-2302

`algebra.tex` — 35754; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35754) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the matrix-product sentence.

Adverse evidence / qualification: The independent ill-typed entry and missing reverse product receive separate records.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\right)
+\right).
````

### MC-STK-ERR-2303

`algebra.tex` — 35756-35757; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35756-L35757) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the reverse-product justification for invertibility of both factors.

Adverse evidence / qualification: An invertible product alone is insufficient for arbitrary modules, as the explicit shift example shows. Both products and exact inverses are proved separately with all source signs.

````diff
--- original
+++ replacement
@@ -1,2 +1,3 @@
-This shows that both matrices on the right hand side
-are invertible and proves the lemma.
+The product in the reverse order is also upper triangular with identity
+diagonal entries. Thus both products are invertible, so both factors
+are invertible and the lemma follows.
````

### MC-STK-ERR-2304

`algebra.tex` — 35763; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35763) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the comma splitting the two presentations.

Adverse evidence / qualification: Both presentations have the same source base and target algebra.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\to S$, and
+\to S$ and
````

### MC-STK-ERR-2305

`algebra.tex` — 35768; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35768) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the supplementary ideal definitions.

Adverse evidence / qualification: The conormal stable isomorphism follows from the corrected two-term argument.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as $S$-modules where
+as $S$-modules, where
````

### MC-STK-ERR-2306

`algebra.tex` — 35779; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35779) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the comma splitting the presentation pair.

Adverse evidence / qualification: The second target remains the localized algebra, as in the source.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\to S$, and
+\to S$ and
````

### MC-STK-ERR-2307

`algebra.tex` — 35784; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35784) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the supplementary ideal definitions.

Adverse evidence / qualification: The original localized conormal modules and both ranks remain.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-as $S_g$-modules where
+as $S_g$-modules, where
````

### MC-STK-ERR-2308

`algebra.tex` — 35161; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35161) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specify the category in which the standard resolution is a homotopy equivalence.

Adverse evidence / qualification: Simplicial 6944 explicitly states underlying simplicial sets. For Z to F_p no reverse Z-algebra map into Z[F_p] exists.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-which comes equipped with a canonical homotopy equivalence
+which comes equipped with a canonical homotopy equivalence on underlying simplicial sets
````

### MC-STK-ERR-2309

`algebra.tex` — 35586; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35586) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the actual conclusion of the cited surjection lemma.

Adverse evidence / qualification: For a nonzero identity algebra the canonical degree-zero term is nonzero. It is the zero-variable comparison that is literally zero.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-zero (by
+homotopy equivalent to zero (by
````

### MC-STK-ERR-2310

`algebra.tex` — 35738; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35738) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the ill-typed order of the upper-right matrix composition.

Adverse evidence / qualification: The original product has upper-right entry minus psi_1 after h_prime plus h after psi_0. This correction is independent of the reported missing reverse product.

````diff
--- original
+++ replacement
@@ -1 +1 @@
--h' \circ \psi_1
+-\psi_1 \circ h'
````

### MC-STK-ERR-2311

`algebra.tex` — 35796; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L35796) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Apply the two-term stable-isomorphism lemma to the established homotopy equivalence.

Adverse evidence / qualification: The localized presentation complex need not be a polynomial presentation over R; the earlier conormal statement alone would require unjustified free-summand cancellation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\ref{lemma-conormal-module}
+\ref{lemma-sum-two-terms}
````

### MC-STK-ERR-2312

`algebra.tex` — 36051; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36051) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the finite verb in the transition.

Adverse evidence / qualification: The four equivalent original assertions and their supporting Cohen-Macaulay criterion are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence the equivalences
+Hence we have the equivalences
````

### MC-STK-ERR-2313

`algebra.tex` — 36068; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36068) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the displayed-map sentence.

Adverse evidence / qualification: The original composite is injective on J modulo mJ by the regular-quotient parameter lemma.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-J/ \mathfrak m J \to  I / \mathfrak m I \to \mathfrak m /\mathfrak m^2
+J/ \mathfrak m J \to  I / \mathfrak m I \to \mathfrak m /\mathfrak m^2.
````

### MC-STK-ERR-2314

`algebra.tex` — 36173; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36173) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the singular one-condition quantification explicit.

Adverse evidence / qualification: All five conditions remain equivalent, so this does not alter the mathematical criterion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-any of the equivalent conditions (1) -- (5) of Lemma \ref{lemma-lci} hold.
+any one of the equivalent conditions (1) -- (5) of Lemma \ref{lemma-lci} holds.
````

### MC-STK-ERR-2315

`algebra.tex` — 36282; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36282) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the designation preposition.

Adverse evidence / qualification: The three primes and their original ambient rings remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2316

`algebra.tex` — 36291; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36291) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the first local-ring diagram sentence.

Adverse evidence / qualification: Both vertical flat maps and the quotient arrows are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+}.
````

### MC-STK-ERR-2317

`algebra.tex` — 36309; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36309) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the residue-field designation preposition.

Adverse evidence / qualification: The original kappa and its finite extension of k remain explicit.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2318

`algebra.tex` — 36337; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36337) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the second local-ring diagram sentence.

Adverse evidence / qualification: The zero-dimensional closed fibre and exact local dimensions are checked separately.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+}.
````

### MC-STK-ERR-2319

`algebra.tex` — 36466, 36467; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36466-L36467) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Mark the prime quantification within the original sentence.

Adverse evidence / qualification: The exact fibre comparison and field-extension criterion remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Thus it suffices to show
+Thus it suffices to show,
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-given primes $\mathfrak p' \subset R'$ lying over $\mathfrak p \subset R$
+for primes $\mathfrak p' \subset R'$ lying over $\mathfrak p \subset R$,
````

### MC-STK-ERR-2320

`algebra.tex` — 36492; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36492) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the separator in the original finite list.

Adverse evidence / qualification: The finite principal cover and unit-ideal hypothesis are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-g_1, \ldots g_m
+g_1, \ldots, g_m
````

### MC-STK-ERR-2321

`algebra.tex` — 36580; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36580) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the stray preposition before the displayed map.

Adverse evidence / qualification: The specified domain, field extension and monic factorization equations are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A $k$-algebra map of
+A $k$-algebra map
````

### MC-STK-ERR-2322

`algebra.tex` — 36651, 36652; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36651-L36652) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Join the if-clause to its consequence.

Adverse evidence / qualification: The original base localization and every polynomial coefficient remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some $f \in R$.
+for some $f \in R$,
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then the ring
+then the ring
````

### MC-STK-ERR-2323

`algebra.tex` — 36731; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36731) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the singular verb for the chosen subalgebra.

Adverse evidence / qualification: The approximation keeps all original equations and descends a finite unit-ideal certificate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-There exist a finite type
+There exists a finite type
````

### MC-STK-ERR-2324

`algebra.tex` — 36744; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36744) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the designation preposition.

Adverse evidence / qualification: The original prime lies above all three indicated contractions. No rewrite of the contraction diagram is needed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and denote
+and denote by
````

### MC-STK-ERR-2325

`algebra.tex` — 36805, 36806; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36805-L36806) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the designation and the plural count of the three primes.

Adverse evidence / qualification: Each prime remains in its original ring, with the original contraction map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the prime of
+the primes of
````

### MC-STK-ERR-2326

`algebra.tex` — 36834; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36834) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the conormal-module designation preposition.

Adverse evidence / qualification: The original generators and the localization argument proving their basis property remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $N$
+Denote by $N$
````

### MC-STK-ERR-2327

`algebra.tex` — 36905; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36905) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the localization condition from the main clause.

Adverse evidence / qualification: The selected element still avoids the same original prime.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g\not\in \mathfrak q$ we may
+$g\not\in \mathfrak q$, we may
````

### MC-STK-ERR-2328

`algebra.tex` — 36927; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36927) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the sentence containing the exact sequence.

Adverse evidence / qualification: The finite kernel and flat quotient justify the displayed fibre injection.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-0 \to J \to S' \to S \to 0
+0 \to J \to S' \to S \to 0.
````

### MC-STK-ERR-2329

`algebra.tex` — 37025; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37025) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural verb for the chosen localization elements.

Adverse evidence / qualification: Their bars and original ambient quotient algebra are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists elements
+there exist elements
````

### MC-STK-ERR-2330

`algebra.tex` — 37069; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37069) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the formula from its reference clause.

Adverse evidence / qualification: The original partial derivatives and differential module are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\frac{\partial f}{\partial y} \text{d}y$ see
+\frac{\partial f}{\partial y} \text{d}y$, see
````

### MC-STK-ERR-2331

`algebra.tex` — 37124; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37124) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the comparison of the complex with its degree-zero homology accurately.

Adverse evidence / qualification: The source definition gives a quasi-isomorphism, not equality of its chain modules. A chosen splitting gives the stronger homotopy comparison in the separate note.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-complex of $S/R$ is $\Omega_{S/R}$
+complex of $S/R$ is quasi-isomorphic to $\Omega_{S/R}$
````

### MC-STK-ERR-2332

`algebra.tex` — 37229; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37229) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the cited criterion from its consequence.

Adverse evidence / qualification: The original coordinate classes, regular sequence and neighbourhood remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemma \ref{lemma-lci}
+Lemma \ref{lemma-lci},
````

### MC-STK-ERR-2333

`algebra.tex` — 37238; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37238) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Separate the given polynomial data from the main clause.

Adverse evidence / qualification: All inequalities, equations and determinant entries are preserved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R[x_1, \ldots, x_n]$ we say
+R[x_1, \ldots, x_n]$, we say
````

### MC-STK-ERR-2334

`algebra.tex` — 37297; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37297) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the sentence containing the displayed complex.

Adverse evidence / qualification: The original differential and free target remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\bigoplus\nolimits_{i = 1}^n S \text{d}x_i
+\bigoplus\nolimits_{i = 1}^n S \text{d}x_i.
````

### MC-STK-ERR-2335

`algebra.tex` — 37317; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37317) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use a direct designation for the displayed base-changed algebra.

Adverse evidence / qualification: Every coefficient is still transformed by the original ring map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Set
````

### MC-STK-ERR-2336

`algebra.tex` — 37562; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37562) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specify the actual target of the split surjection.

Adverse evidence / qualification: Projectivity of the image splits E onto its image, making the kernel a finite direct summand. A polynomial algebra gives E=0 and F nonzero, disproving a right inverse onto all of F.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a direct summand and this map has a right inverse too.
+is a direct summand, so the surjection onto this image has a right inverse.
````

### MC-STK-ERR-2337

`algebra.tex` — 37637; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37637) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Keep the predicate attached to the displayed polynomial.

Adverse evidence / qualification: The full chosen determinant and the original prime condition are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-i \in I}.
+i \in I}
````

### MC-STK-ERR-2338

`algebra.tex` — 37691; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37691) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the given prime when applying the local syntomic criterion.

Adverse evidence / qualification: The cited criterion supplies exactly an element outside that prime; the replacement must preserve the point under study.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a $g \in S$ such that
+a $g \in S$, $g \not \in \mathfrak q$, such that
````

### MC-STK-ERR-2339

`algebra.tex` — 37716; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37716) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Complete the designation of the original base change.

Adverse evidence / qualification: Its flatness hypothesis and exact tensor factors are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $S' = R' \otimes_R S$ the base change.
+Let $S' = R' \otimes_R S$ be the base change.
````

### MC-STK-ERR-2340

`algebra.tex` — 37719; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37719) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing verb.

Adverse evidence / qualification: The smooth locus and the original target spectrum are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Spec(S')$ the set
+\Spec(S')$ be the set
````

### MC-STK-ERR-2341

`algebra.tex` — 37764; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37764) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural verb for the localization elements.

Adverse evidence / qualification: The original barred elements and lifting charts are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists elements
+there exist elements
````

### MC-STK-ERR-2342

`algebra.tex` — 37327, 37331; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37327-L37331) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restrict the dimension argument to the nonempty fibres required by the source definition.

Adverse evidence / qualification: Z[z]/(2z-1) is standard smooth with n=c=1 but its fibre over (2) is zero. The theorem is valid; the two unqualified dimension claims in its proof omit the empty-fibre exception.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S \otimes_R \kappa(\mathfrak p)$ has dimension
+every nonzero fibre $S \otimes_R \kappa(\mathfrak p)$ has dimension
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-over a field $k$ has dimension
+over a field $k$, if nonzero, has dimension
````

### MC-STK-ERR-2343

`algebra.tex` — 37396, 37398, 37408, 37410; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37396-L37410) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Differentiate the actual chosen polynomial lifts with respect to the x variables.

Adverse evidence / qualification: The g_j have coefficients in the quotient S, where x-derivatives need not be defined. Their g prime lifts lie in the displayed polynomial ring. The y-derivatives of g_j are already well-defined and are retained. The corrected block determinant equals the original product of units.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\partial g_1
+\partial g'_1
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\partial g_d
+\partial g'_d
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\partial g_1
+\partial g'_1
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\partial g_d
+\partial g'_d
````

### MC-STK-ERR-2344

`algebra.tex` — 37858; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37858) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the redundant final preposition.

Adverse evidence / qualification: The relative clause already contains to which; every chosen variable lift and the original diagram are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-map to under
+map under
````

### MC-STK-ERR-2345

`algebra.tex` — 37865; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37865) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the kernel designation preposition.

Adverse evidence / qualification: The original polynomial presentation and the right inverse to its quotient remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2346

`algebra.tex` — 37914; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37914) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the repeated kernel designation preposition.

Adverse evidence / qualification: The original split conormal criterion and all tensor factors remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2347

`algebra.tex` — 38082; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38082) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use Let for the two displayed kernel definitions.

Adverse evidence / qualification: Both kernels, their ambient rings and the original split exact sequence are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Let
````

### MC-STK-ERR-2348

`algebra.tex` — 38316; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38316) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the finite-subring designation preposition.

Adverse evidence / qualification: The original Noetherian approximation and every selected image and coordinate remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2349

`algebra.tex` — 37973; conceptual source correction recorded.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L37973) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the actual chosen polynomial lifts as coefficients in the ideal-membership assertion.

Adverse evidence / qualification: The classes lambda and mu act on J/J^2, but are not themselves specified elements of P. The assertion that a polynomial expression lies in J^2 must use x_mu and x_lambda. The full derivation preserves the additional f_lambda f_mu term and the original R-structure; the theorem itself remains valid.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mu f_\lambda
+x_\mu f_\lambda
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\lambda f_\mu
+x_\lambda f_\mu
````

### MC-STK-ERR-2350

`algebra.tex` — 38094, 38096, 38142, 38163; conceptual source correction recorded.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38094-L38163) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Specify the commuting lift and the exact left-inverse directions.

Adverse evidence / qualification: Compatibility with A alone does not specify the reduction B to C needed to map J into I/I^2. Formal smoothness supplies both conditions. The split conormal map is a retraction, not a two-sided inverse: A=C=k and B=k[x] gives 0 to k. In the later square-zero proof the exact correction delta=Delta r_0 gives (r_0+delta)d=1.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\sigma : B \to A/I^2$ whose composition
+$\sigma : B \to A/I^2$, lifting $B \to C$, whose composition
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is inverse to the map
+is a left inverse to the map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a section to
+is a left inverse to
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is a section of
+is a left inverse to
````

### MC-STK-ERR-2351

`algebra.tex` — 38348; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38348) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the redundant then from the Given construction.

Adverse evidence / qualification: The original exact sequence is valid and even split; that strengthening stays in separate editorial material.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-smooth, then the sequence
+smooth, the sequence
````

### MC-STK-ERR-2352

`algebra.tex` — 38389; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38389) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use Let for the two kernel definitions.

Adverse evidence / qualification: The original split conormal maps are the ones verified in group 1083.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Let
````

### MC-STK-ERR-2353

`algebra.tex` — 38410; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38410) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the algebra as a power series ring.

Adverse evidence / qualification: The source statement identifies an algebra, not a single series. The retraction and conormal freeness hypotheses remain in the formal statement.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a power series over
+a power series ring over
````

### MC-STK-ERR-2354

`algebra.tex` — 38436; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38436) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use Let for the specified power-series algebra and augmentation ideal.

Adverse evidence / qualification: All chosen f_i and the actual map x_i to f_i remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Let
````

### MC-STK-ERR-2355

`algebra.tex` — 38439; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38439) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the designation preposition for the inverse.

Adverse evidence / qualification: The source inverse at order two and the later inverse induction are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2356

`algebra.tex` — 38554, 38555, 38556; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38554-L38556) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair the three consecutive designation constructions.

Adverse evidence / qualification: The original intermediate quotient and both maximal ideals retain their exact roles.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $J
+Let $J
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $S'
+Let $S'
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $\mathfrak m' = \mathfrak m''S'$ the corresponding
+Let $\mathfrak m' = \mathfrak m''S'$ be the corresponding
````

### MC-STK-ERR-2357

`algebra.tex` — 38753, 38754; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38753-L38754) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing ideal noun and both designation constructions.

Adverse evidence / qualification: The original local ring, maximal ideal and residue field remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $R
+Let $R
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-its maximal
+its maximal ideal
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-its residue field $\kappa$
+its residue field by $\kappa$
````

### MC-STK-ERR-2358

`algebra.tex` — 38755; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38755) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the plural for the two coordinated lemma references.

Adverse evidence / qualification: Both cited exact differential comparisons are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-By Lemma
+By Lemmas
````

### MC-STK-ERR-2359

`algebra.tex` — 38785, 38786, 38801; conceptual source correction recorded.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38785-L38801) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Make the intended free summand and nonzero-ring hypotheses explicit and include the n=1 nilpotence case.

Adverse evidence / qualification: A cyclic direct summand need not be free on df: S=R=Q,f=0,C=0 satisfies the literal decomposition but not the conclusion. The zero ring also contradicts the nonnilpotence conclusion. The proof needs the coefficient derivation theta(f)=1, exactly supplied by the clarified hypothesis; the later regularity proof already supplies it by a unit basis coordinate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-a $\mathbf{Q}$-algebra map.
+a $\mathbf{Q}$-algebra map with $S \not= 0$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Let $f \in S$ be such that
+Let $f \in S$ be such that $S \to S\text{d}f$, $a \mapsto a\text{d}f$, is an isomorphism and
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-with $n > 1$ minimal
+with $n \geq 1$ minimal
````

### MC-STK-ERR-2360

`algebra.tex` — 38953; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L38953) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing verb in the finite type hypothesis.

Adverse evidence / qualification: The source assumes a Noetherian base. The separate extension weakens that assumption while retaining finite presentation; it does not replace the original statement.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R \to S$ of finite type.
+$R \to S$ is of finite type.
````

### MC-STK-ERR-2361

`algebra.tex` — 39007; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39007) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use Let for the defined first-order thickening.

Adverse evidence / qualification: The original quotient by I squared and its localization remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Let
````

### MC-STK-ERR-2362

`algebra.tex` — 39116, 39118; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39116-L39118) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the displayed equality sentence and capitalize the next sentence.

Adverse evidence / qualification: The subsequent tensor operation uses the same original B_N and both original exponents. No mathematical object is changed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega_{S'_{\mathfrak q'}/R}
+\Omega_{S'_{\mathfrak q'}/R}.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we can further tensor
+We can further tensor
````

### MC-STK-ERR-2363

`algebra.tex` — 39187; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39187) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing maximal-ideal predicate verb.

Adverse evidence / qualification: The proposed enumeration colon is an optional preference and is not integrated. Algebraic closedness and the maximal-ideal hypothesis remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak m \subset S$ a maximal ideal
+$\mathfrak m \subset S$ is a maximal ideal
````

### MC-STK-ERR-2364

`algebra.tex` — 39197, 39208, 39214; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39197-L39214) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing predicate in all three prime-ideal clauses.

Adverse evidence / qualification: The proposed enumeration colon is optional. Each original field, residue separability and characteristic-zero condition remains in its own overview item.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak q \subset S$ a prime ideal
+$\mathfrak q \subset S$ is a prime ideal
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak q \subset S$ a prime ideal
+$\mathfrak q \subset S$ is a prime ideal
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak q \subset S$ a prime ideal
+$\mathfrak q \subset S$ is a prime ideal
````

### MC-STK-ERR-2365

`algebra.tex` — 39183; conceptual source correction recorded.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39183) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore finite presentation to the flat-base-change statement, as in its cited theorem.

Adverse evidence / qualification: The overview invites consultation of precise statements, explaining the likely abbreviation, but the unqualified assertion is false. For R=product_i k, I=direct_sum_i k and S=R/I, the map is flat, finite type and formally smooth, with field local target rings, yet its smooth locus is empty. Flat base change to R_p for a prime containing I gives the smooth identity of a field. Every proposed principal neighbourhood has an explicitly non-finitely-generated quotient kernel.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-points where a
+points where a finitely presented
````

### MC-STK-ERR-2366

`algebra.tex` — 39735; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39735) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing preposition in the kernel notation.

Adverse evidence / qualification: The coefficient map need not be surjective as a ring map. Its kernel nevertheless has exactly the original residue field because its image contains R/p inside its fraction field. No surjectivity claim or change of point is introduced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2367

`algebra.tex` — 39864; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39864) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the descended target algebra in the base-change equality.

Adverse evidence / qualification: The first tensor factor remains the original base R; the resulting algebra is S. The source approximation argument is preserved even though a separate direct proof is available.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R = R \otimes_{R_0} S_0$
+$S = R \otimes_{R_0} S_0$
````

### MC-STK-ERR-2368

`algebra.tex` — 39864; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39864) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the contracted-prime definition.

Adverse evidence / qualification: The prime is the contraction along the base-change map, not a new prime chosen independently.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2369

`algebra.tex` — 39876; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39876) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Join the two required localization conditions without repeating such that.

Adverse evidence / qualification: Testing membership through a stated ring map is conventional notation for its image; that part of the reports is not an additional mathematical defect. The original map and both localizations remain explicit in the note.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-such that $S'
+and $S'
````

### MC-STK-ERR-2370

`algebra.tex` — 39891; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39891) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Punctuate the displayed decomposition before its citation.

Adverse evidence / qualification: The display still has exactly the original n local Artinian factors; the chosen field factor is not replaced by all factors.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\prod\nolimits_{i = 1}^n A_i
+\prod\nolimits_{i = 1}^n A_i,
````

### MC-STK-ERR-2371

`algebra.tex` — 39931; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39931) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the contracted-prime definition.

Adverse evidence / qualification: The unique-prime and finite-cokernel arguments use the same contraction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2372

`algebra.tex` — 39968; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39968) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the predicate verb in the enumerated condition.

Adverse evidence / qualification: The original proof uses Noetherianity here. A separate direct finite-cokernel argument proves the step without it; that proof is not substituted into the translation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S$ finite over $R$
+$S$ is finite over $R$
````

### MC-STK-ERR-2373

`algebra.tex` — 39991; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39991) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Define the first exponent used by the following uniform indexed formula.

Adverse evidence / qualification: The first factor is a field and its original irreducible polynomial occurs with exponent one. This explicit index convention changes no factor or multiplicity.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$e_2, \ldots, e_n \geq 1$. Here
+$e_2, \ldots, e_n \geq 1$, with $e_1 = 1$. Here
````

### MC-STK-ERR-2374

`algebra.tex` — 40000; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40000) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the reduction notation.

Adverse evidence / qualification: The original monic polynomial m and its reduction remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2375

`algebra.tex` — 40117; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40117) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the root-reduction notation.

Adverse evidence / qualification: All actual roots and their reduction into the chosen residue field are retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2376

`algebra.tex` — 40167; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40167) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the base-prime notation.

Adverse evidence / qualification: This is the contraction of the specified prime in the tensor-product cover.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2377

`algebra.tex` — 40171; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40171) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply to be in the definition of the contracted prime.

Adverse evidence / qualification: The source already specifies the ring map into the tensor product. Its contraction proves the nonmembership used in the next step.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the image
+to be the image
````

### MC-STK-ERR-2378

`algebra.tex` — 39978, 39987, 40013, 40018; conceptual source correction recorded.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L39978-L40018) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the actual nonzero scalar introduced when lifting the monic fibre-ideal generator.

Adverse evidence / qualification: After rescaling the generator its leading coefficient is lambda, not automatically one. The missing factor occurs in three later polynomial equalities. R=Z,p=(3),I=(x-1),h=2(x-1),m=x-1,l=2 gives actual f=x^2-1 but the printed formula gives x^2-x. Keeping lambda preserves the simple-root argument and the theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\lambda \in \kappa(\mathfrak p)
+\lambda \in \kappa(\mathfrak p)^*
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{h} = \overline{h}_1
+\overline{h} = \lambda \overline{h}_1
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{h}_1 \overline{h}_2^{e_2}
+\lambda \overline{h}_1 \overline{h}_2^{e_2}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{h}_1(\overline{h}_2^{e_2}
+\overline{h}_1(\lambda \overline{h}_2^{e_2}
````

### MC-STK-ERR-2379

`algebra.tex` — 40210; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40210) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the predicate verb in the unit hypothesis.

Adverse evidence / qualification: The unit is in the original fibre algebra, including the allowed zero fibre, and is not asserted to be a unit globally before base localization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g$ invertible
+$g$ is invertible
````

### MC-STK-ERR-2380

`algebra.tex` — 40212; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40212) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the incorrect indefinite article before f.

Adverse evidence / qualification: The nonmembership in the original base prime remains explicit.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists a $f
+there exists $f
````

### MC-STK-ERR-2381

`algebra.tex` — 40219-40220; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40219-L40220) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Repair punctuation around the specific closed-image citation.

Adverse evidence / qualification: The complementizer that is optional and is not inserted as a supposed requirement. Closedness follows from the actual integral map.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-By Section \ref{section-going-up}
-especially, Lemma \ref{lemma-going-up-closed} we see $T$ is closed.
+By Section \ref{section-going-up},
+especially Lemma \ref{lemma-going-up-closed}, we see $T$ is closed.
````

### MC-STK-ERR-2382

`algebra.tex` — 40232, 40365, 40424; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40232-L40424) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the finite-type predicate in the two reported hypotheses and the identical unreported middle hypothesis.

Adverse evidence / qualification: All three lemmas retain finite type rather than finite presentation. The mathematical proofs use finite type, integral localization and the Noetherian field fibre, not a Noetherian base.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $R \to S$ finite type
+Assume $R \to S$ is finite type
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $R \to S$ finite type
+Assume $R \to S$ is finite type
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $R \to S$ finite type
+Assume $R \to S$ is finite type
````

### MC-STK-ERR-2383

`algebra.tex` — 40272; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40272) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the bar identifying the closed point of the fibre spectrum.

Adverse evidence / qualification: The integral-over-field argument proves closedness of the fibre point. The corresponding prime of the integral algebra need not be closed; Z at its generic point gives the exact distinction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\mathfrak q'$
+$\overline{\mathfrak q}'$
````

### MC-STK-ERR-2384

`algebra.tex` — 40259; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40259) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the fibre-prime notation.

Adverse evidence / qualification: The prime remains the one corresponding to the original contraction.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2385

`algebra.tex` — 40295; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40295) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the reduced-polynomial notation.

Adverse evidence / qualification: The original monic annihilating polynomial is retained, including its optional multiplication by x before factorization.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2386

`algebra.tex` — 40381, 40442; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40381-L40442) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing predicate at both remainder conclusions, accounting once for the shared report.

Adverse evidence / qualification: The conclusion is restricted to primes above the specified base prime. It does not assert that the remainder is zero or that it has no quasi-finite points elsewhere.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R' \to B$ not quasi-finite
+$R' \to B$ is not quasi-finite
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R' \to B$ not quasi-finite
+$R' \to B$ is not quasi-finite
````

### MC-STK-ERR-2387

`algebra.tex` — 40386; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40386) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the fibre-ring notation.

Adverse evidence / qualification: The fibre field is the original residue field, preserved by the subsequent pointed etale steps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2388

`algebra.tex` — 40409; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40409) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Punctuate the completed displayed decomposition.

Adverse evidence / qualification: The already extracted finite factor is base changed separately and retained in the next display.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A_2 \times \ldots \times A_n \times B
+A_2 \times \ldots \times A_n \times B.
````

### MC-STK-ERR-2389

`algebra.tex` — 40455; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40455) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the finite-count typographical error once for both reports.

Adverse evidence / qualification: The count is of isolated closed points in the fixed finite type field fibre, not all primes of the source.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finitely may primes
+finitely many primes
````

### MC-STK-ERR-2390

`algebra.tex` — 40457; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40457) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the actual base prime below the selected source primes.

Adverse evidence / qualification: The fibre was fixed at mathfrak p. Replacing it by the entire base ring is not the asserted prime-contraction relation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$R$ at which
+$\mathfrak p$ at which
````

### MC-STK-ERR-2391

`algebra.tex` — 40452; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40452) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the preposition in the fibre-ring notation.

Adverse evidence / qualification: The subsequent separable and purely inseparable degrees are computed over this same residue field.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2392

`algebra.tex` — 40514; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40514) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the indefinite article before t once for both reports.

Adverse evidence / qualification: Retain t in the original maximal ideal and all powers n greater than or equal to one.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there exists an $t
+there exists a $t
````

### MC-STK-ERR-2393

`algebra.tex` — 40515; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40515) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the spelling once for both reports.

Adverse evidence / qualification: The canonical quotient maps, rather than unspecified isomorphisms, are asserted and proved.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-isomorphsm
+isomorphism
````

### MC-STK-ERR-2394

`algebra.tex` — 40536; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40536) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the conjunction joining the derivative predicate and its consequence.

Adverse evidence / qualification: The derivative being a unit implies nonmembership in the exact prime. The source degree-one boundary is explained editorially without replacing its proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-in $T$ in particular is not contained
+in $T$ and in particular is not contained
````

### MC-STK-ERR-2395

`algebra.tex` — 40564; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40564) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the period which cuts the sentence before its of-the-ring-map complement.

Adverse evidence / qualification: The map still ends in the actual local ring; no claim that all denominators invert on one principal neighbourhood is introduced.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R \to S \to S'_{\mathfrak m'}.
+R \to S \to S'_{\mathfrak m'}
````

### MC-STK-ERR-2396

`algebra.tex` — 40684, 40686; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40684-L40686) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore both actual endpoints in the differentiated product over all p roots, counting the two reports once.

Adverse evidence / qualification: Keep the omitted i-factor, p times alpha_i to power p-1, and every root index. The resulting product is a unit, including p=2. The stronger d less than or equal to p boundary is separate editorial material.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(\alpha_i - \alpha_1)
+(\alpha_i - \alpha_0)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(\alpha_i - \alpha_1)
+(\alpha_i - \alpha_{p - 1})
````

### MC-STK-ERR-2397

`algebra.tex` — 40760; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40760) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use plural agreement for the two coordinated operations.

Adverse evidence / qualification: The finite-coefficient and eventual-zero proof establishes the claimed comparison even with noninjective filtered transition maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-commutes with filtered colimits
+commute with filtered colimits
````

### MC-STK-ERR-2398

`algebra.tex` — 40898; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40898) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the lemma sentence.

Adverse evidence / qualification: The source directed-colimit claim is valid; stronger small-diagram closure is separate.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is formally unramified over $R$
+is formally unramified over $R$.
````

### MC-STK-ERR-2399

`algebra.tex` — 40950; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40950) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the decomposition sentence.

Adverse evidence / qualification: The chosen splitting is retained; the conormal kernel is independent up to the unique universal comparison.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-J/J^2 = K \oplus \Omega_{P/R} \otimes_P S
+J/J^2 = K \oplus \Omega_{P/R} \otimes_P S.
````

### MC-STK-ERR-2400

`algebra.tex` — 40990; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40990) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the sum defining the universal differential once for both reports.

Adverse evidence / qualification: Every polynomial uses finitely many variables; keep all terms and the source tensor with one. The Taylor correction uses the same complete sum.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-g \mapsto \frac{\partial g}{\partial x_i}
+g \mapsto \sum_i \frac{\partial g}{\partial x_i}
````

### MC-STK-ERR-2401

`algebra.tex` — 40987; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L40987) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the Taylor identity sentence.

Adverse evidence / qualification: The omitted higher terms vanish by the actual square-zero target ideal, not a finiteness assumption.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\beta(g) + \sum\nolimits_i \delta_i \beta(\frac{\partial g}{\partial x_i})
+\beta(g) + \sum\nolimits_i \delta_i \beta(\frac{\partial g}{\partial x_i}).
````

### MC-STK-ERR-2402

`algebra.tex` — 41120; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41120) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the actual square-zero kernel of B prime to B at both occurrences in this line.

Adverse evidence / qualification: J prime/J squared is not an ideal of B prime. The correct kernel is J/J prime and its square is zero. The nilpotent quotient argument works for arbitrarily many generators.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$J'/J^2$ by construction. Since $J'/J^2$ is a nilpotent ideal, we see
+$J/J'$ by construction. Since $J/J'$ is a nilpotent ideal, we see
````

### MC-STK-ERR-2403

`algebra.tex` — 41142; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41142) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the tensored exact-sequence sentence.

Adverse evidence / qualification: Right exactness is sufficient here; no left exactness of tensoring is asserted.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega_{B'/R} \otimes_{B'} B \to 0
+\Omega_{B'/R} \otimes_{B'} B \to 0.
````

### MC-STK-ERR-2404

`algebra.tex` — 41148; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41148) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Complete the reference to the preceding direct-sum decomposition.

Adverse evidence / qualification: The adjacent mathematical graph correction is recorded independently in1202, rather than attributed to this wording report.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$ given
+$ given above,
````

### MC-STK-ERR-2405

`algebra.tex` — 41229; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41229) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the formal-etale colimit sentence.

Adverse evidence / qualification: Compatibility of the unique lifts is proved for each transition map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is formally \'etale over $R$
+is formally \'etale over $R$.
````

### MC-STK-ERR-2406

`algebra.tex` — 41282; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41282) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the sentence after the three lifting diagrams.

Adverse evidence / qualification: The two inverse quotient maps are proved using nilpotent uniqueness, with each original ideal power retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-}
+}.
````

### MC-STK-ERR-2407

`algebra.tex` — 41294; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41294) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the undefined base in the diagonal ideal.

Adverse evidence / qualification: All original maps are relative to R; both tensor actions and the diagonal multiplication remain unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S' \otimes_{R'} S'
+S' \otimes_R S'
````

### MC-STK-ERR-2408

`algebra.tex` — 41323; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41323) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use extension of the original S-module along S to S prime.

Adverse evidence / qualification: Tensoring over R would change the module and already contradict the k=0 case. The proof keeps the right S action on diagonal principal parts.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-M' = S' \otimes_R M
+M' = S' \otimes_S M
````

### MC-STK-ERR-2409

`algebra.tex` — 41325; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41325) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the principal-parts comparison sentence.

Adverse evidence / qualification: The canonical isomorphism has both tensor actions specified in the editorial proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S' \otimes_S P^k_{S/R}(M) = P^k_{S'/R}(M')
+S' \otimes_S P^k_{S/R}(M) = P^k_{S'/R}(M').
````

### MC-STK-ERR-2410

`algebra.tex` — 41349; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41349) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the actual common base in the last principal-parts term.

Adverse evidence / qualification: R prime has not been introduced; this correction agrees with the statement and diagonal algebra.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-P^k_{S'/R'}(M')
+P^k_{S'/R}(M')
````

### MC-STK-ERR-2411

`algebra.tex` — 41356, 41357; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41356-L41357) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct all three scalar-extension bases in the operator construction once for both reports.

Adverse evidence / qualification: The original gamma is S-linear, and its extended map has the same S-base tensor in domain and codomain. Retain the corrected factorization D=gamma composed with D_univ from924.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S' \otimes_R N
+S' \otimes_S N
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S' \otimes_R P^k_{S/R}(M)
+S' \otimes_S P^k_{S/R}(M)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S' \otimes_R N
+S' \otimes_S N
````

### MC-STK-ERR-2412

`algebra.tex` — 41149-41150; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41149-L41150) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the source identification of a graph with the second direct summand.

Adverse evidence / qualification: For f_i=sum a_i,nu x^nu, df_i=(sum d(a_i,nu) tensor z^nu,dx_i). The image is the graph of these full base-differential terms; projection is an isomorphism. The exact inverse quotient map (e,v) maps to e-eta(v) proves the stated theorem. The example A=k[t],f=x-t has df=dx-dt and refutes the printed intermediate claim.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-we see that the submodule $(f_i)/(J')^2 \otimes_{B'} B$ maps
+we see that the image of the first arrow projects
 isomorphically onto the summand $\bigoplus B\text{d}x_i$.
````

### MC-STK-ERR-2413

`algebra.tex` — 41369; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41369) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the central scalar base of the differential-operator algebra.

Adverse evidence / qualification: For S=Q[x],M=S, the derivative and multiplication by x have commutator the identity, so natural S scalars are not central. Every differential operator is R-linear; the resulting possibly noncommutative R-algebra acts by the proven extension functor.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-over the $S$-algebra
+over the (possibly noncommutative) $R$-algebra
````

### MC-STK-ERR-2414

`algebra.tex` — 41382; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41382) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the indefinite article once for both reports.

Adverse evidence / qualification: The source comparison with EGA terminology remains unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-an G-unramified
+a G-unramified
````

### MC-STK-ERR-2415

`algebra.tex` — 41448; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41448) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the full finite-presentation alternative.

Adverse evidence / qualification: The G-unramified branch requires the same finite-presentation hypothesis as the preceding parallel tests; no global finiteness assumption is weakened.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of finite type (resp.\ presentation)
+of finite type (resp.\ finite presentation)
````

### MC-STK-ERR-2416

`algebra.tex` — 41477; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41477) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Cite the actual permanence lemma for composition.

Adverse evidence / qualification: The replaced reference concerns scalar base change; the exact composition lemma proves both finite-type and finite-presentation transitivity.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-lemma-base-change-finiteness
+lemma-compose-finite-type
````

### MC-STK-ERR-2417

`algebra.tex` — 41519-41520; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41519-L41520) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the principal-neighbourhood definition and the proved finite-cover gluing assertion.

Adverse evidence / qualification: Items (6) and (7) already assume global finite type or presentation, absent here. The definition gives local neighbourhoods, quasi-compactness gives a finite cover, and (10) supplies global finiteness and differential vanishing.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-Ad (11). Follows from (6) and (7) and the fact that the spectrum of $S$
-is quasi-compact.
+Ad (11). Follows from (10), the definition of being unramified
+(resp.\ G-unramified) at a prime, and quasi-compactness of $\Spec(S)$.
````

### MC-STK-ERR-2418

`algebra.tex` — 41574; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41574) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Join the original equality to its maximal-ideal predicate.

Adverse evidence / qualification: Retain both original ideals and the actual local ring. The fibre is the original finite separable residue field.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\item we have $\mathfrak p S_{\mathfrak q} = \mathfrak qS_{\mathfrak q}$
+\item we have $\mathfrak p S_{\mathfrak q} = \mathfrak qS_{\mathfrak q}$, which
````

### MC-STK-ERR-2419

`algebra.tex` — 41663; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41663) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use plural agreement for the two cited results.

Adverse evidence / qualification: The equivalence retains finite presentation; flat unramified alone is not substituted.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-shows that (3) implies (1)
+show that (3) implies (1)
````

### MC-STK-ERR-2420

`algebra.tex` — 41703; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41703) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the modal spelling once for both reports.

Adverse evidence / qualification: The dimension formula is checked at the actual contracted maximal ideal, with base dimension n and zero-dimensional fibre.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-we my apply
+we may apply
````

### MC-STK-ERR-2421

`algebra.tex` — 41759-41760; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41759-L41760) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the repeated clause and make the stated map explicit once for both reports.

Adverse evidence / qualification: Testing prime membership via the given map is conventional and is not independently a mathematical defect. The source needs the image outside the prime, which the replacement states explicitly.

````diff
--- original
+++ replacement
@@ -1,2 +1,2 @@
-an element $g' \in S'$ such that
-$g' \not \in \mathfrak q$ such that
+an element $g' \in S'$ whose image in $S$
+does not belong to $\mathfrak q$, such that
````

### MC-STK-ERR-2422

`algebra.tex` — 41853; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41853) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the copula in the list of reduced assumptions.

Adverse evidence / qualification: The Noetherian finite-module argument and the original finiteness claim are unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$S$ finite over $R$
+$S$ is finite over $R$
````

### MC-STK-ERR-2423

`algebra.tex` — 41862; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41862) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Place the monic generator in the actual polynomial PID.

Adverse evidence / qualification: The fibre ideal is proper and nonzero at the specified point; its monic generator is not a nonzero constant in the coefficient field.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{h} \in \kappa(\mathfrak p)
+\overline{h} \in \kappa(\mathfrak p)[x]
````

### MC-STK-ERR-2424

`algebra.tex` — 41863; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41863) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State explicitly the unit condition required for rescaling a generator.

Adverse evidence / qualification: A zero scalar does not preserve the generator. The denominator construction produces an actual nonzero scalar; the source conclusion needs no stronger hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\lambda \in \kappa(\mathfrak p)
+\lambda \in \kappa(\mathfrak p)^*
````

### MC-STK-ERR-2425

`algebra.tex` — 41872, 41898, 41903; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41872-L41903) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the same nonzero scalar in all three polynomial identities.

Adverse evidence / qualification: After rescaling the original monic fibre generator, the leading scalar is lambda. For h=2(x-1),m=x-1,l=2 over Z with residue F_3, the actual f=x^2-1 differs from the printed scalar-free x^2-x. Preserve all chosen polynomials and both derivative summands.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{h} = \overline{h}_1
+\overline{h} = \lambda \overline{h}_1
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{h}_1 \overline{h}_2^{e_2}
+\lambda \overline{h}_1 \overline{h}_2^{e_2}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\overline{h}_1(\overline{h}_2^{e_2}
+\overline{h}_1(\lambda \overline{h}_2^{e_2}
````

### MC-STK-ERR-2426

`algebra.tex` — 41864; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41864) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Require the lift to lie in the actual kernel ideal I.

Adverse evidence / qualification: The later assertion f=m^l+h in I uses this membership. Express the monic fibre generator as a finite combination of images of members of I and clear every coefficient denominator by their finite product; the resulting h belongs to I and retains its nonzero scalar.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h \in R[x]
+h \in I
````

### MC-STK-ERR-2427

`algebra.tex` — 41876; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L41876) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Define the distinguished exponent in the uniform factor-algebra formula.

Adverse evidence / qualification: The separable field factor has multiplicity one. Naming e_1=1 preserves all other exponents and does not change the fibre decomposition.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$e_2, \ldots, e_n \geq 1$. Here the numbering is chosen so that
+$e_2, \ldots, e_n \geq 1$; set $e_1 = 1$. Here the numbering is chosen so that
````

### MC-STK-ERR-2428

`algebra.tex` — 42232; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42232) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Correct the direction of ideal contraction along the retraction.

Adverse evidence / qualification: The map tau has domain Rprime and codomain R, so the inverse image of m is mprime. The exact tensor/retraction inverse maps retain the given residue point.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathfrak m = \tau^{-1}(\mathfrak m')
+\mathfrak m' = \tau^{-1}(\mathfrak m)
````

### MC-STK-ERR-2429

`algebra.tex` — 42255; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42255) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restore the final distinct factor of the base-changed finite product.

Adverse evidence / qualification: The preceding product and following A_1 through A_n require the nth factor. No factor or complementary algebra is omitted.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(A'_1 \otimes_{R', \tau} R)
+(A'_n \otimes_{R', \tau} R)
````

### MC-STK-ERR-2430

`algebra.tex` — 42311; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42311) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the residue polynomial whose simple root defines the point.

Adverse evidence / qualification: The referent is recoverable from the construction, so this is a clarification rather than a false theorem.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-be a simple root.
+be a simple root of $\overline{f}$.
````

### MC-STK-ERR-2431

`algebra.tex` — 42144, 42350; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42144-L42350) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Handle both allowed zero residue factors and qualify the impossible zero-polynomial degree requirement.

Adverse evidence / qualification: In k[epsilon]/epsilon^2, f=epsilon has factorization of its residue 0 times1; requiring degree(g)=degree(0) cannot give f. Coprimality makes the other zero-case factor a nonzero constant, and the displayed unit lifts solve both cases exactly. Nonzero factors retain the full leading-scalar comparison.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-moreover $\deg_T(g) = \deg_T(g_0)$,
+moreover $\deg_T(g) = \deg_T(g_0)$ if $g_0 \ne 0$,
````

````diff
--- original
+++ replacement
@@ -1 +1,5 @@
-$\gcd(g_0, h_0) = 1$. We may and do assume that $g_0$ is monic.
+$\gcd(g_0, h_0) = 1$. If $g_0 = 0$, then $h_0$ is a nonzero
+constant; lift it to a unit $h \in R$ and set $g = h^{-1}f$.
+If $h_0 = 0$, lift the nonzero constant $g_0$ to a unit $g \in R$
+and set $h = g^{-1}f$. Thus we may assume that both residue factors
+are nonzero. We may and do assume that $g_0$ is monic.
````

### MC-STK-ERR-2432

`algebra.tex` — 42498; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42498) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Replace the undefined part reference with the finite-algebra decomposition lemma.

Adverse evidence / qualification: There is no numbered part(1) in this equivalence lemma; lemma-mop-up supplies the exact finite factors and the empty-closed-fibre remainder.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-By part (1)
+By Lemma \ref{lemma-mop-up}
````

### MC-STK-ERR-2433

`algebra.tex` — 42741; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42741) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Quantify the positive multiplicity in the lifted factorization.

Adverse evidence / qualification: For the corrected polynomial P(T^2), e is the exact multiplicity of T-1 in its residue polynomial, including characteristic two. Its positivity follows from P(1)x=0 for nonzero x.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-for some $Q_1, Q_2 \in R[T]$ with
+for some $Q_1, Q_2 \in R[T]$ and integer $e \geq 1$ with
````

### MC-STK-ERR-2434

`algebra.tex` — 42730, 42731, 42733, 42739; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42730-L42739) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Keep the original endomorphisms and restore the missing square in all four uses.

Adverse evidence / qualification: Here a=pi alpha i=(pi i)^2 and i a^j pi=alpha^(2j+1), so P(a)=0 gives alpha P(alpha^2)=0. With pi=id and i=diag(1,-1), a=id and P=(T-1)^2 give alpha^2P(alpha)=diag(0,4), although x=(1,0) is fixed. The corrected factorization, Bezout idempotent, both images and explicit surjection E i prove the theorem without changing its maps.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-P(\alpha)
+P(\alpha^2)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R[T]/(T^2P)
+R[T]/(T^2P(T^2))
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-P(\alpha)
+P(\alpha^2)
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-T^2P = (T^2 Q_1) Q_2
+T^2P(T^2) = (T^2 Q_1) Q_2
````

### MC-STK-ERR-2435

`algebra.tex` — 42773; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42773) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the duplicated predicate once for both reports.

Adverse evidence / qualification: The base-change conclusion is valid; the exact tensor and filtered-colimit maps are inverse.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-then so is
+then
````

### MC-STK-ERR-2436

`algebra.tex` — 42807; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42807) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Complete the causal sentence without changing the descended algebra.

Adverse evidence / qualification: The original finite-presentation descent, tensor product and composite etale map prove the conclusion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-As $A \to C' = B_{i'} \otimes_{B_i} C'_j$ is \'etale as
+The map $A \to C' = B_{i'} \otimes_{B_i} C'_j$ is \'etale since
````

### MC-STK-ERR-2437

`algebra.tex` — 42892; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L42892) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

State the induced residue-field map with its exact domain.

Adverse evidence / qualification: Reduction first has domain A/q; its uniquely induced fraction-field map has domain kappa(q). The explicit fraction formula proves the intended meaning, so this is a clarification rather than a false lifting assertion.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f \bmod \mathfrak q = \tau$
+$f$ induces $\tau$ on residue fields
````

### MC-STK-ERR-2438

`algebra.tex` — 43139; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43139) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Close the final definition item with a period.

Adverse evidence / qualification: The original item is a complete sentence with no terminal punctuation; no mathematical condition changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Lemma \ref{lemma-strict-henselization}
+Lemma \ref{lemma-strict-henselization}.
````

### MC-STK-ERR-2439

`algebra.tex` — 43284; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43284) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the defined prime of S prime in the fibre residue map.

Adverse evidence / qualification: The selected factor of F prime corresponds to q prime. The source defines no p prime. The original tensor coequalizer extends precisely this selected residue map.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathfrak p'
+\mathfrak q'
````

### MC-STK-ERR-2440

`algebra.tex` — 43360; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43360) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Take the inverse image of the maximal ideal in the actual strict-henselization target.

Adverse evidence / qualification: The displayed map has codomain S strict h. The ordinary-henselization maximal ideal is in a different ring. Unique henselian lifting with the specified residue embedding proves the corrected condition.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathfrak m_{S^h}
+\mathfrak m_{S^{sh}}
````

### MC-STK-ERR-2441

`algebra.tex` — 43381-43383; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43381-L43383) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Join the given-diagram clause to its main existence clause.

Adverse evidence / qualification: The original source has a capitalized main clause after the unclosed given clause; the map and all residue conditions stay identical.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-}
+},
 $$
-There exists
+there exists
````

### MC-STK-ERR-2442

`algebra.tex` — 43422; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43422) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Name the category using all three pieces of its original object data.

Adverse evidence / qualification: The residue embedding is part of each object and every morphism preserves it. The exact filteredness proof retains those embeddings.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-category of pairs
+category of triples
````

### MC-STK-ERR-2443

`algebra.tex` — 43441; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43441) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the stray article and close the introductory phrase.

Adverse evidence / qualification: The combined map remains x tensor y to phi(x) phi-prime(y), with the exact compositum residue field.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Combining the maps the above we
+Combining the maps above, we
````

### MC-STK-ERR-2444

`algebra.tex` — 43461; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43461) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the stated name for arrows preserving the residue embeddings.

Adverse evidence / qualification: Such arrows also are arrows of underlying pairs; this is a terminology correction, not a false-arrow claim. Triple compatibility is retained in the original tensor coequalizer proof.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-morphisms of pairs
+morphisms of triples
````

### MC-STK-ERR-2445

`algebra.tex` — 43522-43524; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L43522-L43524) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Join the given-diagram clause to the strict-henselization identification.

Adverse evidence / qualification: There is no post-display period in the actual source, contrary to the report. The accepted operation fixes the actual clause joining and capitalization; the chosen residue map still specifies the base-change prime.

````diff
--- original
+++ replacement
@@ -1,3 +1,3 @@
-}
+},
 $$
-The local ring map
+the local ring map
````

### MC-STK-ERR-2446

`algebra.tex` — 44037; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44037) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the existing full case-(4) hypothesis check and qualify the preceding support equality to include the zero quotient.

Adverse evidence / qualification: The permitted choice x=0 gives the original Rprime=R[0]=R, whose quotient has empty support. The existing x-in-R branch appears after the unqualified support equality. Inclusion in the singleton is exactly what is proved and suffices for annihilation by a power; all nontrivial-case hypotheses and the original total quotient ring remain intact.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence the support of $R'/R$ is
+Hence the support of $R'/R$ is contained in
````

### MC-STK-ERR-2447

`algebra.tex` — 44065; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44065) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Add the missing period to the first complete enumerated assertion.

Adverse evidence / qualification: The item ends before the next item without punctuation. Its zero-module and unit cases remain valid and vacuous.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-height $1$
+height $1$.
````

### MC-STK-ERR-2448

`algebra.tex` — 44257; clarification.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44257) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Introduce the field extension used by every subsequent assertion of the lemma.

Adverse evidence / qualification: The original first sentence quantifies only k; neither the statement nor its proof introduces K elsewhere. The inserted datum preserves both properties and every original map.

````diff
--- original
+++ replacement
@@ -1 +1,2 @@
 Let $k$ be a field of characteristic $p > 0$.
+Let $K/k$ be a field extension.
````

### MC-STK-ERR-2449

`algebra.tex` — 44439; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L44439) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Use the standard compound for intermediate field extensions over k.

Adverse evidence / qualification: The same directed system of finite generated fields is retained. Its H_1 vanishing follows from the exact cotangent colimit, not a general assertion that filtered formally smooth colimits remain formally smooth.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finitely generated sub $k$-extensions
+finitely generated $k$-subextensions
````

### MC-STK-ERR-2450

`algebra.tex` — 45175; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45175) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Qualify any localization by nonzero, respecting the domain-only definitions of N-1 and N-2.

Adverse evidence / qualification: The source multiplicative-subset definition allows zero and its fraction equivalence then gives the zero ring. A field localized at {0,1} is zero, which is not a domain and has no fraction field. The ordinary intended domain-localization reading is valid; the minimal qualification makes it explicit. All later uses in this interval invert nonzero elements or prime complements.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-any localization of $R$
+any nonzero localization of $R$
````

### MC-STK-ERR-2451

`algebra.tex` — 45742; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45742) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the corrected domain quotient charts in part (2), and propagate nonzero to the domain charts in part (1).

Adverse evidence / qualification: N-1 and N-2 are defined only for domains. Images phi(f_i)=0 produce zero charts, and the original unit-ideal identity remains valid after exactly those indices are removed. The zero ring itself remains Nagata and universally Japanese, so no exclusion is added to those definitions.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Hence if each $S_{f_i} = S_{\varphi(f_i)}$ is N-1 then so is
+Hence if each nonzero $S_{f_i} = S_{\varphi(f_i)}$ is N-1 then so is
````

### MC-STK-ERR-2452

`algebra.tex` — 45872; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L45872) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the construction naming the original integral closure.

Adverse evidence / qualification: The exact total-quotient inclusions and faithful-flat finite-generation descent identify this Rprime throughout; the edit only repairs its designation.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $R'$ the integral closure
+Denote by $R'$ the integral closure
````

### MC-STK-ERR-2453

`algebra.tex` — 46020; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46020) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Add the colon introducing the three equivalent conditions.

Adverse evidence / qualification: The equivalence is proved with finite local domains and the original finite field extension, including the maximal-prime case.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-are equivalent
+are equivalent:
````

### MC-STK-ERR-2454

`algebra.tex` — 46026; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46026) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Remove the redundant then from the for construction.

Adverse evidence / qualification: The source already introduces the quantified finite local homomorphism; its conclusion is unchanged.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-with $S$ a domain, then $S$
+with $S$ a domain, $S$
````

### MC-STK-ERR-2455

`algebra.tex` — 46052; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46052) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Parenthesize the coefficient quotient before adjoining the chosen generators.

Adverse evidence / qualification: The actual domain is the subalgebra of L generated over R/p; no quotient of the polynomial ideal p[x_i] is intended.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-S = R/\mathfrak p[x_1, \ldots, x_n]
+S = (R/\mathfrak p)[x_1, \ldots, x_n]
````

### MC-STK-ERR-2456

`algebra.tex` — 46054; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46054) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Parenthesize the residue-field coefficient ring in the truncated polynomial algebra.

Adverse evidence / qualification: The displayed quotient maps onto the actual special fibre, with every exponent d_i and the zero-variable case retained.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-R/\mathfrak m[T_1, \ldots, T_n]
+(R/\mathfrak m)[T_1, \ldots, T_n]
````

### MC-STK-ERR-2457

`algebra.tex` — 46101; mathematical.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46101) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Restrict the transcendental branch to positive transcendence degree, leaving the identity field extension in the finite branch.

Adverse evidence / qualification: The source Fields definition permits no variables, so K/K is purely transcendental. The monogenic injection Z into Z[1/2] has that fraction extension but evaluation of Z[X] has kernel containing 2X-1. The polynomial N-2 theorem applies exactly when the chosen generator is transcendental, while the subsequent finite case covers the degree-zero extension.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is purely transcendental. In this case
+is purely transcendental of positive transcendence degree. In this case
````

### MC-STK-ERR-2458

`algebra.tex` — 46160; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46160) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Retain the precise maximal ideals over the fixed m, and repair the singular verb splits.

Adverse evidence / qualification: The finite localization D of S-prime is semilocal, with exactly those maximal local rings. Its nonzero generic normal open is supplied by the original denominator a_0, so local N-1 implies N-1 for D and descends to the original S_m. The stronger original antecedent would suffice, but the following proof establishes the required restricted family.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-the polynomial $f$ above split completely
+the polynomial $f$ above splits completely
````

### MC-STK-ERR-2459

`algebra.tex` — 46321; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46321) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert by in the original designation of n, explicitly refining the unchanged sentence inside the prior zero-module operation.

Adverse evidence / qualification: The prior operation adds the necessary infinite-depth cases but retains Denote n without by. Its complete immutable preimage and postimage are hash-bound; the new operation changes only that unique retained phrase and must inverse-replay to the full prior paragraph.

This edit refines the unchanged fragment inside earlier operation MC-STK-ERR-0725-OP1. The chapter patch composes both changes, retaining the earlier correction in full. Both immutable historical records remain available.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote $n$ the right hand side.
+Denote by $n$ the right hand side.
````

### MC-STK-ERR-2460

`algebra.tex` — 46389; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46389) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the colon introducing the equivalent Cohen–Macaulay conditions.

Adverse evidence / qualification: Depth and dimension addition give an exact sum of two nonnegative deficiencies, so the two original conditions are equivalent without a changed hypothesis.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then the following are equivalent
+Then the following are equivalent:
````

### MC-STK-ERR-2461

`algebra.tex` — 47000; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47000) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Insert by in the original designation of the two contracted primes.

Adverse evidence / qualification: The original respective pair and singular prime are meaningful. Preserve them and prove the actual two factor-localization maps and the further localization at the original tensor prime.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2462

`algebra.tex` — 47397; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47397) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply by in the adjacent original inverse-image declaration.

Adverse evidence / qualification: The inverse-image map, its source and target are unchanged. The directed-cover argument uses the actual V_lambda and does not assume an arbitrary directed set has a largest element.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Denote
+Denote by
````

### MC-STK-ERR-2463

`algebra.tex` — 47472; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47472) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply the missing copula in the faithful-flatness hypothesis.

Adverse evidence / qualification: Retain faithful flatness and finite presentation exactly. The complete proof uses the stage algebra as the rank-one module model, not an unrelated finite module whose flatness would not prove ring flatness.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Assume $A \to B$ faithfully
+Assume $A \to B$ is faithfully
````

### MC-STK-ERR-2464

`algebra.tex` — 47524, 47549, 47573, 47601, 47628, 47668, 47708; copyedit.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L47524-L47708) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Supply be in all seven original declarations of the algebra map.

Adverse evidence / qualification: Retain every directed-system and finiteness hypothesis. Prove finite and surjective descent with original coefficients and later equality witnesses, differential descent, finitely generated kernel removal, both conormal inverse identities, the smooth splitting, and the exact complete-intersection model and finite syntomic cover.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi_0 : B_0 \to C_0$ a map
+$\varphi_0 : B_0 \to C_0$ be a map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi_0 : B_0 \to C_0$ a map
+$\varphi_0 : B_0 \to C_0$ be a map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi_0 : B_0 \to C_0$ a map
+$\varphi_0 : B_0 \to C_0$ be a map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi_0 : B_0 \to C_0$ a map
+$\varphi_0 : B_0 \to C_0$ be a map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi_0 : B_0 \to C_0$ a map
+$\varphi_0 : B_0 \to C_0$ be a map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi_0 : B_0 \to C_0$ a map
+$\varphi_0 : B_0 \to C_0$ be a map
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\varphi_0 : B_0 \to C_0$ a map
+$\varphi_0 : B_0 \to C_0$ be a map
````

### MC-STK-ERR-2465

`algebra.tex` — 1; rendering support.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r58/candidate.manifest.json)

Load the exact AMS relation symbols and define the support operator used by the reviewed strict-inclusion and flatness corrections. The reusable chapter patch carries both dependencies.

Adverse evidence / qualification: This is a dependency introduced by the corrected edition, not another mathematical defect in the upstream chapter. The failed successor build stops at subsetneq, while the prior chapter builds. No formula, hypothesis, proof, or symbol slot is replaced.

````diff
--- original
+++ replacement
@@ -1 +1,4 @@
 \input{preamble}
+% AMS symbols required by the reviewed strict-inclusion correction.
+\usepackage{amssymb}
+\providecommand{\Supp}{\operatorname{Supp}}
````
