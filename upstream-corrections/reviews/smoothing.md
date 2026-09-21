# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## smoothing

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/smoothing.patch)

### MC-STK-ERR-0001

`smoothing.tex` — 262-265; mathematical reference error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L262-L265) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: let A = ... , c, and a' in A → let A = ... and c

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1,4 +1,4 @@
 Assume $a$ is strictly standard in $A$ over $R$. We claim that
 $A_a$ is smooth over $R$, which proves that $a \in H_{A/R}$. Namely,
-let $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$, $c$, and $a' \in A$
+let $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ and $c$
 be as in Definition \ref{definition-strictly-standard}.
````

### MC-STK-ERR-0002

`smoothing.tex` — 475; mathematical index error.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L475) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: R[y_1, ..., y_c] lifting → R[y_1, ..., y_m] lifting

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$f_1, \ldots, f_c \in R[y_1, \ldots, y_c]$ lifting
+$f_1, \ldots, f_c \in R[y_1, \ldots, y_m]$ lifting
````

### MC-STK-ERR-0003

`smoothing.tex` — 344; copyediting.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L344) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: There exists finite type → There exists a finite type

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-There exists finite type $R$-algebra map $A \to C$ which has a
+There exists a finite type $R$-algebra map $A \to C$ which has a
````

### MC-STK-ERR-0005

`smoothing.tex` — 708; copyediting.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L708) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: Choose an enumerations → Choose an enumeration

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-is invertible in $A$. Choose an enumerations $E = \{a_1, \ldots, a_n\}$
+is invertible in $A$. Choose an enumeration $E = \{a_1, \ldots, a_n\}$
````

### MC-STK-ERR-0006

`smoothing.tex` — 830; copyediting.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L830) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/candidate.manifest.json)

Reviewed legacy summary: correspond a_i/1 → correspond to a_i/1

[Detailed argument](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/proofs.md)

````diff
--- original
+++ replacement
@@ -1 +1 @@
-correspond $a_i/1$ where $a_1, \ldots, a_m \in A$ are generators of $A$
+correspond to $a_i/1$ where $a_1, \ldots, a_m \in A$ are generators of $A$
````

### MC-STK-ERR-1177

`smoothing.tex` — smoothing.tex:378; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L378) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-there is a short exact sequence
+there is an exact sequence
````

### MC-STK-ERR-1178

`smoothing.tex` — smoothing.tex:991-994; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L991-L994) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(I/I^2)_\mathfrak p
+(I/I^2)_{\mathfrak p'}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-at $\mathfrak p$
+at $\mathfrak p'$
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\NL_{A'/R})_\mathfrak p
+\NL_{A'/R})_{\mathfrak p'}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Omega_{A'/R, \mathfrak p}
+\Omega_{A'/R, \mathfrak p'}
````

### MC-STK-ERR-1179

`smoothing.tex` — smoothing.tex:1163-1170; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L1163-L1170) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\mathfrak p B_\mathfrak p/\mathfrak p^2 B_\mathfrak p
+\mathfrak p_B B_{\mathfrak p_B}/\mathfrak p_B^2 B_{\mathfrak p_B}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$g_j \in \mathfrak p^2$
+$g_j \in \mathfrak p_B^2$
````

### MC-STK-ERR-1180

`smoothing.tex` — smoothing.tex:1167; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L1167) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-over $k$
+over $R/\pi R$
````

### MC-STK-ERR-1181

`smoothing.tex` — smoothing.tex:1206; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L1206) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$A$ is separable
+$K$ is separable
````

### MC-STK-ERR-1182

`smoothing.tex` — smoothing.tex:1333; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L1333) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-kills of $h_n$
+kills $h_n$
````

### MC-STK-ERR-1184

`smoothing.tex` — smoothing.tex:1491; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L1491) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-h_{i, \ell}^j, g_{i, \ell}
+h_{k, \ell}^j, g_{k, \ell}
````

### MC-STK-ERR-1185

`smoothing.tex` — smoothing.tex:1976; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L1976) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-(f_1, \ldots, x_c)
+(f_1, \ldots, f_c)
````

### MC-STK-ERR-1186

`smoothing.tex` — smoothing.tex:2268-2271; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2268-L2271) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-C[y_1, \ldots, y_r, z, z^{-1}]
+C[z, z^{-1}, t_{ij}]
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and hence is smooth. On the other hand,
+as a C-algebra. Choose $c \in H_{C/R}$ whose image in $\Lambda$ is not in $\mathfrak q$. Then $B_{zc}$ is smooth over $R$. On the other hand,
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$z$ and $a_\ell y_\ell$
+$zc$ and $a_\ell y_\ell$
````

### MC-STK-ERR-1187

`smoothing.tex` — smoothing.tex:2308-2311; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2308-L2311) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-positive integers
+positive integers.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Then there exists an $n > 0$ and
+Then there exist
````

### MC-STK-ERR-1188

`smoothing.tex` — smoothing.tex:2370-2693; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2370-L2693) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H_{A/R}
+H_{A/k}
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-H_{A/R}
+H_{A/k}
````

### MC-STK-ERR-1189

`smoothing.tex` — smoothing.tex:2374; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2374) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-smooth over $R$ it is
+smooth over $R$ because it is
````

### MC-STK-ERR-1190

`smoothing.tex` — smoothing.tex:2379; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2379) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-diagram above
+diagram below
````

### MC-STK-ERR-1191

`smoothing.tex` — smoothing.tex:2387; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2387) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$\pi_{ij} \in \Lambda$
+$\lambda_{ij} \in \Lambda$
````

### MC-STK-ERR-1192

`smoothing.tex` — smoothing.tex:2492; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2492) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-F[x_1, \ldots, x_d]
+F'[x_1, \ldots, x_d]
````

### MC-STK-ERR-1193

`smoothing.tex` — smoothing.tex:2737; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2737) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-t_1, \ldots, t_m
+t_1, \ldots, t_d
````

### MC-STK-ERR-1194

`smoothing.tex` — smoothing.tex:2873; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2873) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A_{a_i}
+A_{a_j}
````

### MC-STK-ERR-1195

`smoothing.tex` — smoothing.tex:2880-3002; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2880-L3002) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_d
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_d
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_d
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-x_n
+x_d
````

### MC-STK-ERR-1196

`smoothing.tex` — smoothing.tex:2893-2894; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2893-L2894) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\in \Lambda
+\in \mathfrak p
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-\Lambda_\mathfrak q
+k[y_1, \ldots, y_m]_\mathfrak p
````

### MC-STK-ERR-1197

`smoothing.tex` — smoothing.tex:2990; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L2990) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-and we conclude
+we conclude
````

### MC-STK-ERR-1198

`smoothing.tex` — smoothing.tex:3054; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L3054) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-of (\ref{item-fifth-resolve}
+of (\ref{item-fifth-resolve})
````

### MC-STK-ERR-1199

`smoothing.tex` — smoothing.tex:3187-3266; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L3187-L3266) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-d_{n, l}
+d_l
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-d_{n, l}
+d_l
````

### MC-STK-ERR-1200

`smoothing.tex` — smoothing.tex:3191-3270; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L3191-L3270) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Suppose that we can show that $g_j$ as a solution $(b_{i, l})$ in $R$.
+Suppose that we can show that the system of equations $g_j = 0$ has a solution $(b_{i, l})$ in $R$.
````

````diff
--- original
+++ replacement
@@ -1 +1 @@
-Suppose that we can show that $g_j$ as a solution $(b_{i, l})$ in $R'$
+Suppose that we can show that the system of equations $g_j = 0$ has a solution $(b_{i, l})$ in $R'$
````

### MC-STK-ERR-1201

`smoothing.tex` — smoothing.tex:3425; source defect correction.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L3425) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r26/candidate.manifest.json)

accepted_after_independent_frozen_authority_replay

Adverse evidence / qualification: Producer rows are allegation evidence only; frozen authority, bounded preimages, and independent adjudication control.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-A \to P
+A \to B
````

### MC-STK-ERR-1216

`smoothing.tex` — smoothing.tex:1481; source defect correction supersession.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/smoothing.tex#L1481) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r28/replay/independent-review.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r28/candidate.manifest.json)

accepted_after_independent_counterexample_and_localization_reproof

Adverse evidence / qualification: R26 remains immutable. This new unit corrects its insufficient replacement and must be composed last-wins only at the explicitly bound overlapping locus.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-$a_kb_k$
+$a_k((a_k)^N + b_k)$
````
