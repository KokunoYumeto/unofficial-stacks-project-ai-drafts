# Derived Categories corrections and their propagation

This candidate accounts for 176 Derived reports, plus six separately identified receiver reports. It preserves 92 earlier correction units and proposes 64 new units with 89 operations across six chapters. The 33 proved editorial consequences and the refinement of UNDER-007 remain separate.

## MC-STK-ERR-2506: DERIVED-RECON-001

Delete the spurious article before isomorphic.

Complete proof: [evidence/review/PROOFS_0001_1140.md](evidence/review/PROOFS_0001_1140.md); section(s) complete note.

Original derived.tex line 737:

```tex
is the isomorphic
```

Proposed corrected reading:

```tex
is isomorphic
```

## MC-STK-ERR-2507: DERIVED-NEW-001

Name (F,xi) and retain xi_0 after F of the zero boundary.

Complete proof: [evidence/review/PROOFS_0001_1140.md](evidence/review/PROOFS_0001_1140.md); section(s) complete note.

Original derived.tex line 893:

```tex
Let $F : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
pre-triangulated categories. Since
```

Proposed corrected reading:

```tex
Let $(F, \xi) : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
pre-triangulated categories. Since
```

Original derived.tex line 898:

```tex
(F(0), F(0), F(0), 1_{F(0)}, 1_{F(0)}, F(0))
```

Proposed corrected reading:

```tex
(F(0), F(0), F(0), 1_{F(0)}, 1_{F(0)}, \xi_0 \circ F(0))
```

## MC-STK-ERR-2508: DERIVED-NEW-002

Use xi_X composed with F(h); the reflection theorem is unchanged.

Complete proof: [evidence/review/PROOFS_0001_1140.md](evidence/review/PROOFS_0001_1140.md); section(s) complete note.

Original derived.tex line 917:

```tex
Let $F : \mathcal{D} \to \mathcal{D}'$ be a fully faithful exact functor
```

Proposed corrected reading:

```tex
Let $(F, \xi) : \mathcal{D} \to \mathcal{D}'$ be a fully faithful exact functor
```

Original derived.tex line 920:

```tex
$(F(X), F(Y), F(Z), F(f), F(g), F(h))$ is distinguished in $\mathcal{D}'$.
```

Proposed corrected reading:

```tex
$(F(X), F(Y), F(Z), F(f), F(g), \xi_X \circ F(h))$ is distinguished in $\mathcal{D}'$.
```

## MC-STK-ERR-2509: DERIVED-NEW-003

Use the actual arrows G(a) and G(b) between the displayed image objects.

Complete proof: [evidence/review/PROOFS_0001_1140.md](evidence/review/PROOFS_0001_1140.md); section(s) complete note.

Original derived.tex line 1011:

```tex
$(G(A), G(B), G(C), a, b, \delta)$ is
```

Proposed corrected reading:

```tex
$(G(A), G(B), G(C), G(a), G(b), \delta)$ is
```

## MC-STK-ERR-2510: DERIVED-NEW-004

The first three are distinguished as drawn; negate the last arrow to obtain a distinguished fourth row or column.

Complete proof: [evidence/review/PROOFS_0001_1140.md](evidence/review/PROOFS_0001_1140.md); section(s) complete note.

Original derived.tex line 1049:

```tex
Moreover, each of the rows and columns are
distinguished triangles. Finally,
```

Proposed corrected reading:

```tex
Moreover, each of the first three rows and columns is a
distinguished triangle. The bottom row and right column become distinguished
triangles after negating their last arrows. Finally,
```

## MC-STK-ERR-2511: DERIVED-RECON-002

Restore application of TR4 and agreement of conclusion with is; the octahedral argument is unchanged.

Complete proof: [evidence/review/PROOFS_0001_1140.md](evidence/review/PROOFS_0001_1140.md); section(s) complete note.

Original derived.tex line 1068:

```tex
The conclusion of our application TR4
are that
```

Proposed corrected reading:

```tex
The conclusion of our application of TR4
is that
```

## MC-STK-ERR-2512: DERIVED-RECON-003

Remove the period interrupting the compound subject of are morphisms of triangles.

Complete proof: [evidence/review/PROOFS_0001_1140.md](evidence/review/PROOFS_0001_1140.md); section(s) complete note.

Original derived.tex line 1080:

```tex
$(X, X', X'') \to (X, Y', A)$ and $(X, Y', A) \to (Y, Y', Y'')$.
are morphisms
```

Proposed corrected reading:

```tex
$(X, X', X'') \to (X, Y', A)$ and $(X, Y', A) \to (Y, Y', Y'')$
are morphisms
```

## MC-STK-ERR-2513: DERIVED-NEW-005

Require the localization functor to have the identity translation comparison, as in its construction.

Complete proof: [evidence/review/PROOFS_1149_1843.md](evidence/review/PROOFS_1149_1843.md); section(s) 3.

Original derived.tex line 1365:

```tex
the localization functor $Q : \mathcal{D} \to S^{-1}\mathcal{D}$ is exact.
```

Proposed corrected reading:

```tex
the localization functor $Q : \mathcal{D} \to S^{-1}\mathcal{D}$ is exact
with the identity translation comparison.
```

## MC-STK-ERR-2514: DERIVED-NEW-006

Name (F,xi) and use xi_X composed with F(h). The kernel statement is unchanged.

Complete proof: [evidence/review/PROOFS_1149_1843.md](evidence/review/PROOFS_1149_1843.md); section(s) 5.

Original derived.tex line 1787:

```tex
Let $F : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
pre-triangulated categories. Let $\mathcal{D}''$ be the full subcategory
```

Proposed corrected reading:

```tex
Let $(F, \xi) : \mathcal{D} \to \mathcal{D}'$ be an exact functor of
pre-triangulated categories. Let $\mathcal{D}''$ be the full subcategory
```

Original derived.tex line 1803:

```tex
$(F(X), F(Y), F(Z), F(f), F(g), F(h))$ is distinguished.
```

Proposed corrected reading:

```tex
$(F(X), F(Y), F(Z), F(f), F(g), \xi_X \circ F(h))$ is distinguished.
```

## MC-STK-ERR-2515: DERIVED-RECON-007

End the completed sentence with its missing period.

Complete proof: [evidence/review/PROOFS_1844_2401.md](evidence/review/PROOFS_1844_2401.md); section(s) 1.

Original derived.tex line 1976:

```tex
are stable under translations

```

Proposed corrected reading:

```tex
are stable under translations.

```

## MC-STK-ERR-2516: DERIVED-NEW-007

Insert a[1] and retain the original cone matrix and homotopy.

Complete proof: [evidence/review/PROOFS_2419_2994.md](evidence/review/PROOFS_2419_2994.md); section(s) 1.

Original derived.tex line 2535:

```tex
p_2 \circ c = a \circ p_1
```

Proposed corrected reading:

```tex
p_2 \circ c = a[1] \circ p_1
```

## MC-STK-ERR-2517: DERIVED-NEW-008

State the original split-sequence factorization b=alpha*pi*b and its zero composite explicitly.

Complete proof: [evidence/review/PROOFS_2419_2994.md](evidence/review/PROOFS_2419_2994.md); section(s) 4.

Original derived.tex line 2934:

```tex
In other words, we have
$\Im(b^n) \subset \Im(A_2^n \to B_2^n)$ and
$\Ker((b')^n) \supset \Im(A_2^n \to B_2^n)$.
Then $b' \circ b = 0$ as a map of complexes.
```

Proposed corrected reading:

```tex
Writing $\alpha_2 : A_2^\bullet \to B_2^\bullet$ and
$\beta_2 : B_2^\bullet \to C_2^\bullet$ for the maps in the middle
split sequence, we have $\beta_2 \circ b = 0$ and
$b' \circ \alpha_2 = 0$. Choose its degreewise retractions
$\pi_2^n : B_2^n \to A_2^n$. The splitting identities give
$b^n = \alpha_2^n \circ \pi_2^n \circ b^n$, so
$(b')^n \circ b^n = 0$ in every degree.
```

## MC-STK-ERR-2518: DERIVED-NEW-010

define morphisms of triangles in $K(\mathcal{A})$
(the boundary squares commute up to homotopy)

Complete proof: [evidence/review/PROOFS_2995_3485.md](evidence/review/PROOFS_2995_3485.md); section(s) 3.

Original derived.tex line 3292:

```tex
are compatible with the chosen splittings and hence
define morphisms of triangles
```

Proposed corrected reading:

```tex
define morphisms of triangles in $K(\mathcal{A})$
(the boundary squares commute up to homotopy)
```

## MC-STK-ERR-2519: DERIVED-NEW-011

of the bottom split sequence in the diagram provide a splitting

Complete proof: [evidence/review/PROOFS_2995_3485.md](evidence/review/PROOFS_2995_3485.md); section(s) 3.

Original derived.tex line 3306:

```tex
of the bottom split sequence in the diagram provides a splitting
```

Proposed corrected reading:

```tex
of the bottom split sequence in the diagram provide a splitting
```

## MC-STK-ERR-2520: DERIVED-NEW-009

Precomposing the previous isomorphism of triangles with $-1$ on $X$

Complete proof: [evidence/review/PROOFS_2995_3485.md](evidence/review/PROOFS_2995_3485.md); section(s) 2.

Original derived.tex line 3350:

```tex
Precomposing the previous isomorphism of triangles with $-1$ on $Y$
```

Proposed corrected reading:

```tex
Precomposing the previous isomorphism of triangles with $-1$ on $X$
```

## MC-STK-ERR-2521: DERIVED-NEW-012

bounded (above, below) complexes is bounded (above, below).

Complete proof: [evidence/review/PROOFS_2995_3485.md](evidence/review/PROOFS_2995_3485.md); section(s) 3.

Original derived.tex line 3396:

```tex
bounded (above, below) is bounded (above, below).
```

Proposed corrected reading:

```tex
bounded (above, below) complexes is bounded (above, below).
```

## MC-STK-ERR-2522: DERIVED-NEW-013

Use Comp(B) when varying Y and Comp(A) when varying X. The theorem statements already have correct domains.

Complete proof: [evidence/review/PROOFS_3487_4161.md](evidence/review/PROOFS_3487_4161.md); section(s) 2.

Original derived.tex line 3572:

```tex
$\text{Comp}(\mathcal{A}) \to \text{DoubleComp}(\mathcal{C})$,
$Y^\bullet \mapsto X^\bullet \otimes Y^\bullet$ and
```

Proposed corrected reading:

```tex
$\text{Comp}(\mathcal{B}) \to \text{DoubleComp}(\mathcal{C})$,
$Y^\bullet \mapsto X^\bullet \otimes Y^\bullet$ and
```

Original derived.tex line 3574:

```tex
$\text{Comp}(\mathcal{B}) \to \text{DoubleComp}(\mathcal{C})$,
$X^\bullet \mapsto X^\bullet \otimes Y^\bullet$
```

Proposed corrected reading:

```tex
$\text{Comp}(\mathcal{A}) \to \text{DoubleComp}(\mathcal{C})$,
$X^\bullet \mapsto X^\bullet \otimes Y^\bullet$
```

## MC-STK-ERR-2523: DERIVED-NEW-015

Use D^b(Gr(A)), with a common cochain bound across graded components.

Complete proof: [evidence/review/PROOFS_4166_5089.md](evidence/review/PROOFS_4166_5089.md); section(s) 1.

Original derived.tex line 4379:

```tex
such that $\text{gr}(X) \in D^b(\mathcal{A})$.
```

Proposed corrected reading:

```tex
such that $\text{gr}(X) \in D^b(\text{Gr}(\mathcal{A}))$.
```

## MC-STK-ERR-2524: DERIVED-NEW-016

Display Hom(W,C) to the colimit, the direction actually constructed; its inverse exists afterward.

Complete proof: [evidence/review/PROOFS_4166_5089.md](evidence/review/PROOFS_4166_5089.md); section(s) 4.

Original derived.tex line 4792:

```tex
\colim_\mathcal{I} \Mor_{\mathcal{D}'}(W, F(Z''))
\longrightarrow
\Mor_{\mathcal{D}'}(W, C)
```

Proposed corrected reading:

```tex
\Mor_{\mathcal{D}'}(W, C)
\longrightarrow
\colim_\mathcal{I} \Mor_{\mathcal{D}'}(W, F(Z''))
```

## MC-STK-ERR-2525: DERIVED-RECON-025

Repair the grammatical agreement in the derived-functor argument.

Complete proof: [evidence/review/PROOFS_4166_5089.md](evidence/review/PROOFS_4166_5089.md); section(s) 5.

Original derived.tex line 4891:

```tex
The proof of the corresponding statements for $LF$ are dual.
```

Proposed corrected reading:

```tex
The proof of the corresponding statements for $LF$ is dual.
```

## MC-STK-ERR-2526: DERIVED-NEW-019

Three grammar repairs, with mathematical statements unchanged.

Complete proof: [evidence/review/PROOFS_4166_5089.md](evidence/review/PROOFS_4166_5089.md); section(s) 6.

Original derived.tex line 4933:

```tex
The fully faithfulness in (6) follows from (3) and
```

Proposed corrected reading:

```tex
The full faithfulness in (6) follows from (3) and
```

Original derived.tex line 4965:

```tex
We say $F$ is {\it right derivable}, or that $RF$ {\it everywhere defined}
```

Proposed corrected reading:

```tex
We say $F$ is {\it right derivable}, or that $RF$ is {\it everywhere defined}
```

Original derived.tex line 4967:

```tex
We say $F$ is {\it left derivable}, or that $LF$ {\it everywhere defined}
```

Proposed corrected reading:

```tex
We say $F$ is {\it left derivable}, or that $LF$ is {\it everywhere defined}
```

## MC-STK-ERR-2527: DERIVED-NEW-018

Say it need not be an isomorphism for a given X; the note proves the zero-object case and an everywhere-defined counterexample to universal invertibility.

Complete proof: [evidence/review/PROOFS_4166_5089.md](evidence/review/PROOFS_4166_5089.md); section(s) 6.

Original derived.tex line 4982:

```tex
In fact, it might happen that the canonical map
$F(X) \to RF(X)$ is never an isomorphism.
```

Proposed corrected reading:

```tex
The canonical map
$F(X) \to RF(X)$ need not be an isomorphism for a given $X$.
```

## MC-STK-ERR-2528: DERIVED-NEW-017

Swap the Hom arguments in both displayed comparisons, preserving all objects and forward denominator categories.

Complete proof: [evidence/review/PROOFS_4166_5089.md](evidence/review/PROOFS_4166_5089.md); section(s) 7.

Original derived.tex line 5056:

```tex
\Hom_{\mathcal{D}'}(F(X \oplus Y), W)
\longrightarrow
\colim_{s : X \to X', s' : Y \to Y'} \Hom_{\mathcal{D}'}(F(X' \oplus Y'), W)
```

Proposed corrected reading:

```tex
\Hom_{\mathcal{D}'}(W, F(X \oplus Y))
\longrightarrow
\colim_{s : X \to X', s' : Y \to Y'} \Hom_{\mathcal{D}'}(W, F(X' \oplus Y'))
```

Original derived.tex line 5063:

```tex
\Hom_{\mathcal{D}'}(F(X), W)
\longrightarrow
\colim_{s : X \to X'} \Hom_{\mathcal{D}'}(F(X'), W)
```

Proposed corrected reading:

```tex
\Hom_{\mathcal{D}'}(W, F(X))
\longrightarrow
\colim_{s : X \to X'} \Hom_{\mathcal{D}'}(W, F(X'))
```

## MC-STK-ERR-2529: DERIVED-NEW-020

Use the full K/Qis(A); its indicated bounded-target subcategory is cofinal.

Complete proof: [evidence/review/PROOFS_5091_5900.md](evidence/review/PROOFS_5091_5900.md); section(s) 4.

Original derived.tex line 5515:

```tex
Hence in the category $K^\bullet/\text{Qis}^{+}(\mathcal{A})$ the
```

Proposed corrected reading:

```tex
Hence in the category $K^\bullet/\text{Qis}(\mathcal{A})$ the
```

## MC-STK-ERR-2530: DERIVED-RECON-030

Insert the article in is a quotient of while retaining the stated conclusion.

Complete proof: [evidence/review/PROOFS_5091_5900.md](evidence/review/PROOFS_5091_5900.md); section(s) 6.

Original derived.tex line 5826:

```tex
\item If every object of $\mathcal{A}$ is quotient of
```

Proposed corrected reading:

```tex
\item If every object of $\mathcal{A}$ is a quotient of
```

## MC-STK-ERR-2531: DERIVED-NEW-021

Use the acyclic complex zero-object value and the already proved Leray lemma. The full counterexample has F(M)=M[p]/D(M)[p] and the exact four-term complex Z to Z to Q/Z to Q/Z.

Complete proof: [evidence/review/PROOFS_5091_5900.md](evidence/review/PROOFS_5091_5900.md); section(s) 6.

Original derived.tex line 5856:

```tex
Say $I^n = 0$ for $n < n_0$. Setting $J^n = \Im(d^n)$ we break
$I^\bullet$ into short exact sequences
$0 \to J^n \to I^{n + 1} \to J^{n + 1} \to 0$
for $n \geq n_0$. These sequences induce distinguished triangles
$(J^n, I^{n + 1}, J^{n + 1})$ in $D^+(\mathcal{A})$ by
Lemma \ref{lemma-derived-canonical-delta-functor}.
For each $k \in \mathbf{Z}$ denote $H_k$ the assertion:
For all $n \leq k$ the object $J^n$ is in $\mathcal{I}$.
Then $H_k$ holds trivially for $k < n_0$. If $H_n$ holds,
then Lemma \ref{lemma-2-out-of-3-computes} shows that
$J^{n + 1}$ is in $\mathcal{I}$ and we have $H_{n + 1}$.
By Proposition \ref{proposition-derived-functor} we have a
distinguished triangle $(RF(J^n), RF(I^{n + 1}), RF(J^{n + 1}))$.
Since $J^n, I^{n + 1}, J^{n + 1}$ are in $\mathcal{I}$
the long exact cohomology sequence
(\ref{equation-long-exact-cohomology-sequence-D})
associated to this distinguished triangle collapses
to an exact sequence
$$
0 \to F(J^n) \to F(I^{n + 1}) \to F(J^{n + 1}) \to 0
$$
This in turn proves that $F(I^\bullet)$ is exact.
```

Proposed corrected reading:

```tex
Since $I^\bullet$ is acyclic, it is isomorphic to zero in
$D^+(\mathcal{A})$. The right derived functor is defined at zero,
with value zero, and hence at $I^\bullet$, with value zero, by
Lemma \ref{lemma-derived-inverts}.
The complex $I^\bullet$ is bounded below and all its terms are
right $F$-acyclic. Thus Lemma \ref{lemma-leray-acyclicity} shows that
$F(I^\bullet) \to RF(I^\bullet)$ is an isomorphism.
Consequently $F(I^\bullet)$ is acyclic.
```

## MC-STK-ERR-2532: DERIVED-RECON-033

Use superscripts for all four components of the specified cochain maps.

Complete proof: [evidence/review/PROOFS_5910_6199.md](evidence/review/PROOFS_5910_6199.md); section(s) 2.

Original derived.tex line 6063:

```tex
t_{-2}
```

Proposed corrected reading:

```tex
t^{-2}
```

Original derived.tex line 6063:

```tex
g_{-2}
```

Proposed corrected reading:

```tex
g^{-2}
```

Original derived.tex line 6064:

```tex
t_{-1}
```

Proposed corrected reading:

```tex
t^{-1}
```

Original derived.tex line 6064:

```tex
g_{-1}
```

Proposed corrected reading:

```tex
g^{-1}
```

## MC-STK-ERR-2533: DERIVED-NEW-023

Quantify over D(A) and specify that the termwise functor inverts quasi-isomorphisms after the Verdier quotient. Its exact inverse and counit maps are proved in the editorial note.

Complete proof: [evidence/review/PROOFS_5910_6199.md](evidence/review/PROOFS_5910_6199.md); section(s) 3.

Original derived.tex line 6118:

```tex
Lemma \ref{lemma-derived-of-quotient}.
For an object
```

Proposed corrected reading:

```tex
Lemma \ref{lemma-derived-of-quotient}.
Apply $u$ termwise to complexes. If $s$ is a quasi-isomorphism,
then the cohomology of the cone of $u(s)$ lies in $\mathcal{B}$,
because $vu$ is naturally isomorphic to the identity.
Thus this construction sends quasi-isomorphisms to isomorphisms
after passing to $D(\mathcal{A})/D_\mathcal{B}(\mathcal{A})$,
and induces a functor from $D(\mathcal{A}/\mathcal{B})$ to this quotient.
For an object
```

Original derived.tex line 6128:

```tex
$X, Y \in \Ob(\mathcal{A}))$
```

Proposed corrected reading:

```tex
$X, Y \in \Ob(D(\mathcal{A}))$
```

Preserves and extends MC-STK-ERR-0839-OP1; its historical evidence remains retained.

## MC-STK-ERR-2534: DERIVED-NEW-024

Use h_2-h_1 in both the displayed difference and its extension to the direct sum. The original parenthesis correction remains in place.

Complete proof: [evidence/review/PROOFS_6209_7089.md](evidence/review/PROOFS_6209_7089.md); section(s) 3.

Original derived.tex line 6524:

```tex
d \circ (h_1^n - h_2^n) + (h_1^{n + 1} - h_2^{n + 1}) \circ d
```

Proposed corrected reading:

```tex
d \circ (h_2^n - h_1^n) + (h_2^{n + 1} - h_1^{n + 1}) \circ d
```

Original derived.tex line 6527:

```tex
equals $h_1^n - h_2^n$ on the first summand
```

Proposed corrected reading:

```tex
equals $h_2^n - h_1^n$ on the first summand
```

## MC-STK-ERR-2535: DERIVED-NEW-025

Insert a before bounded in both sentences, preserving their opposite bounds.

Complete proof: [evidence/review/PROOFS_6209_7089.md](evidence/review/PROOFS_6209_7089.md); section(s) 3.

Original derived.tex line 6543:

```tex
Let $I^\bullet$ be bounded below complex consisting of injective
```

Proposed corrected reading:

```tex
Let $I^\bullet$ be a bounded below complex consisting of injective
```

Original derived.tex line 6824:

```tex
Let $P^\bullet$ be bounded above complex consisting of projective
```

Proposed corrected reading:

```tex
Let $P^\bullet$ be a bounded above complex consisting of projective
```

## MC-STK-ERR-2536: DERIVED-RECON-044

Use q for the horizontal cohomology and its resolution, retaining vertical degree p and the sign (-1)^q.

Complete proof: [evidence/review/PROOFS_7096_7578.md](evidence/review/PROOFS_7096_7578.md); section(s) 2.

Original derived.tex line 7248:

```tex
the differential of the complex $H^p_I(I^{\bullet, \bullet})$
```

Proposed corrected reading:

```tex
the differential of the complex $H^q_I(I^{\bullet, \bullet})$
```

Original derived.tex line 7249:

```tex
which is an injective resolution of $H^p(K^\bullet)$. Hence the
```

Proposed corrected reading:

```tex
which is an injective resolution of $H^q(K^\bullet)$. Hence the
```

## MC-STK-ERR-2537: DERIVED-NEW-026

Evaluate at I[0] and identify RF(I[0]) with F(I)[0]; this gives the actual acyclicity comparison.

Complete proof: [evidence/review/PROOFS_7096_7578.md](evidence/review/PROOFS_7096_7578.md); section(s) 4.

Original derived.tex line 7311:

```tex
$t$ on $RF(I) = F(I)$. Conversely, assume (1) holds.
```

Proposed corrected reading:

```tex
$t$ at $I[0]$, using $RF(I[0]) = F(I)[0]$. Conversely, assume (1) holds.
```

## MC-STK-ERR-2538: DERIVED-NEW-027

Describe the displayed strict monomorphism as the pushout of u by f; retain the original quotient and extension argument.

Complete proof: [evidence/review/PROOFS_7589_8350.md](evidence/review/PROOFS_7589_8350.md); section(s) 3.

Original derived.tex line 7906:

```tex
The pushout $f' : I \to I \amalg_A B$ of $f$ by $u$ is a strict
```

Proposed corrected reading:

```tex
The pushout $f' : I \to I \amalg_A B$ of $u$ by $f$ is a strict
```

## MC-STK-ERR-2539: DERIVED-NEW-029

With f^(-i)=id_A, composition is (-1)^(ij) times the splice class; retain this factor in the higher-vanishing proof.

Complete proof: [evidence/review/PROOFS_8774_9196.md](evidence/review/PROOFS_8774_9196.md); section(s) 3.

Original derived.tex line 8826:

```tex
We call $\delta(E) = fs^{-1}$ the {\it class} of the Yoneda extension.

```

Proposed corrected reading:

```tex
Here $f^{-i} = \text{id}_A$ and all other components of $f$ are zero.
We call $\delta(E) = fs^{-1}$ the {\it class} of the Yoneda extension.

```

Original derived.tex line 8917:

```tex
can be described in terms of Yoneda extensions as follows: the
composition of
$$
0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to B \to 0
$$
and
$$
0 \to B \to Z'_{j - 1} \to Z'_{j - 2} \to \ldots \to Z'_0 \to C \to 0
$$
is the Yoneda extension
$$
0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to 
Z'_{j - 1} \to Z'_{j - 2} \to \ldots \to Z'_0 \to C \to 0
$$

```

Proposed corrected reading:

```tex
can be described in terms of Yoneda extensions as follows. Let
$$
E : 0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to B \to 0
$$
and
$$
E' : 0 \to B \to Z'_{j - 1} \to Z'_{j - 2} \to \ldots \to Z'_0 \to C \to 0
$$
be given. With the projection convention for $\delta$ above, their
composition $\delta(E)[j] \circ \delta(E')$ equals
$(-1)^{ij}\delta(S)$, where
$$
S : 0 \to A \to Z_{i - 1} \to Z_{i - 2} \to \ldots \to Z_0 \to
Z'_{j - 1} \to Z'_{j - 2} \to \ldots \to Z'_0 \to C \to 0
$$
is the spliced extension; its joining arrow is the composition
$Z_0 \to B \to Z'_{j - 1}$.

```

Original derived.tex line 8997:

```tex
Then $\delta(E)$ is the composition of $\delta(E')$ and $\delta(E'')$

```

Proposed corrected reading:

```tex
Then $\delta(E) = (-1)^{p(i - p)}\delta(E'')[p] \circ \delta(E')$,

```

## MC-STK-ERR-2540: DERIVED-NEW-028

Ext^i(B,A) times Ext^j(C,B) maps to Ext^(i+j)(C,A).

Complete proof: [evidence/review/PROOFS_8774_9196.md](evidence/review/PROOFS_8774_9196.md); section(s) 3.

Original derived.tex line 8913:

```tex
\Ext^j_\mathcal{A}(B, C) \times \Ext^i_\mathcal{A}(A, B)
\longrightarrow
\Ext^{i + j}_\mathcal{A}(A, C)

```

Proposed corrected reading:

```tex
\Ext^i_\mathcal{A}(B, A) \times \Ext^j_\mathcal{A}(C, B)
\longrightarrow
\Ext^{i + j}_\mathcal{A}(C, A)

```

## MC-STK-ERR-2541: DERIVED-NEW-030

Prove p=0 from id_A=0; for p>=1 use C=im(Z_p to Z_(p-1)).

Complete proof: [evidence/review/PROOFS_8774_9196.md](evidence/review/PROOFS_8774_9196.md); section(s) 6.

Original derived.tex line 8990:

```tex
For $i > p$ write any class $\xi$ as $\delta(E)$

```

Proposed corrected reading:

```tex
If $p = 0$, then $\Hom_\mathcal{A}(A, A) = 0$ for every object $A$.
Thus $\text{id}_A = 0$, every object is zero, and the conclusion follows.
Assume $p \geq 1$. For $i > p$ write any class $\xi$ as $\delta(E)$

```

Original derived.tex line 8996:

```tex
Set $C = \Ker(Z_{p - 1} \to Z_{p - 2}) = \Im(Z_p \to Z_{p - 1})$.

```

Proposed corrected reading:

```tex
Set $C = \Im(Z_p \to Z_{p - 1})$.

```

## MC-STK-ERR-2542: DERIVED-RECON-069

Use objects of the category in the second occurrence.

Complete proof: [evidence/review/PROOFS_8774_9196.md](evidence/review/PROOFS_8774_9196.md); section(s) 8.

Original derived.tex line 9067:

```tex
as follows. Take the free abelian group on the objects on $\mathcal{D}$

```

Proposed corrected reading:

```tex
as follows. Take the free abelian group on the objects of $\mathcal{D}$

```

## MC-STK-ERR-2543: DERIVED-NEW-032

Use K^b in all six factors, supply the full Hom differential, and state the vanishing for every shifted target.

Complete proof: [evidence/review/PROOFS_9206_9744.md](evidence/review/PROOFS_9206_9744.md); section(s) 7.

Original derived.tex line 9712:

```tex
\prod\nolimits_b \Hom(K^{-b}, I^{b - 1}) \to
\prod\nolimits_b \Hom(K^{-b}, I^b) \to
\prod\nolimits_b \Hom(K^{-b}, I^{b + 1})

```

Proposed corrected reading:

```tex
\prod\nolimits_b \Hom(K^b, I^{b - 1}) \to
\prod\nolimits_b \Hom(K^b, I^b) \to
\prod\nolimits_b \Hom(K^b, I^{b + 1})

```

Original derived.tex line 9717:

```tex
in the middle. Similarly, the complex

```

Proposed corrected reading:

```tex
in the middle. Here these are the degrees $-1,0,1$ of the full Hom complex,
with $C^r = \prod_b \Hom(K^b, I^{b + r})$ and
$(d_C^r f)^b = d_I^{b + r}f^b - (-1)^r f^{b + 1}d_K^b$.
Its degree $r$ cohomology is
$\Hom_{K(\mathcal{A})}(K^\bullet, I^\bullet[r])$.
Similarly, the complex

```

Original derived.tex line 9720:

```tex
\prod\nolimits_b \Hom(K^{-b}, I_t^{b - 1}) \to
\prod\nolimits_b \Hom(K^{-b}, I_t^b) \to
\prod\nolimits_b \Hom(K^{-b}, I_t^{b + 1})

```

Proposed corrected reading:

```tex
\prod\nolimits_b \Hom(K^b, I_t^{b - 1}) \to
\prod\nolimits_b \Hom(K^b, I_t^b) \to
\prod\nolimits_b \Hom(K^b, I_t^{b + 1})

```

Original derived.tex line 9732:

```tex
$\Hom_{K(\mathcal{A})}(K^\bullet, I_t^\bullet) = 0$, hence

```

Proposed corrected reading:

```tex
$\Hom_{K(\mathcal{A})}(K^\bullet, I_t^\bullet[r]) = 0$
for every integer $r$, hence

```

## MC-STK-ERR-2544: DERIVED-NEW-033

Choose a cutoff a below every remaining infinite dimension, resolve the tail from a, and retain every original degree in the resulting splice.

Complete proof: [evidence/review/PROOFS_9746_10132.md](evidence/review/PROOFS_9746_10132.md); section(s) 4.

Original derived.tex line 9909:

```tex
By Lemma \ref{lemma-subcategory-right-resolution} we can find a
quasi-isomorphism $\sigma_{\geq 0}K^\bullet \to M^\bullet$ with
$M^n = 0$ for $n < 0$ and $d(M^n) = 0$ for $n \geq 0$. Then $K^\bullet$
is quasi-isomorphic to the complex
$$
\ldots \to K^{-2} \to K^{-1} \to M^0 \to M^1 \to \ldots
$$
Hence we may assume that $d(K^n) = 0$ for $n \gg 0$. Note that
the condition $n + d(K^n) \to -\infty$ as $n \to -\infty$ is not
violated by this replacement.

```

Proposed corrected reading:

```tex
Choose an integer $a$ such that $d(K^n) < \infty$ for all $n < a$.
By Lemma \ref{lemma-subcategory-right-resolution} we can find a
quasi-isomorphism $\sigma_{\geq a}K^\bullet \to M^\bullet$ with
$M^n = 0$ for $n < a$ and $d(M^n) = 0$ for $n \geq a$. Then $K^\bullet$
is quasi-isomorphic to the complex
$$
\ldots \to K^{a - 2} \to K^{a - 1} \to M^a \to M^{a + 1} \to \ldots
$$
Hence we may assume that every $d(K^n)$ is finite and that
$d(K^n) = 0$ for $n \gg 0$. Note that the condition
$n + d(K^n) \to -\infty$ as $n \to -\infty$ is not violated by this replacement.

```

## MC-STK-ERR-2545: DERIVED-RECON-074

Insert the missing article before finite sequence.

Complete proof: [evidence/review/PROOFS_9746_10132.md](evidence/review/PROOFS_9746_10132.md); section(s) 5.

Original derived.tex line 9968:

```tex
find finite sequence of elementary transformations which

```

Proposed corrected reading:

```tex
find a finite sequence of elementary transformations which

```

## MC-STK-ERR-2546: DERIVED-NEW-034

The exact spectral-sequence support ends at i-2, making both adjacent cone cohomology objects zero.

Complete proof: [evidence/review/PROOFS_9746_10132.md](evidence/review/PROOFS_9746_10132.md); section(s) 6.

Original derived.tex line 10048:

```tex
$j \in \{i - n - 2, \ldots, i - 1\}$. Hence we see that

```

Proposed corrected reading:

```tex
$j \in \{i - n - 2, \ldots, i - 2\}$. Hence we see that

```

## MC-STK-ERR-2547: DERIVED-RECON-077

State for every integer c; retain the general cutoff and its later specialization.

Complete proof: [evidence/review/PROOFS_9746_10132.md](evidence/review/PROOFS_9746_10132.md); section(s) 7.

Original derived.tex line 10064:

```tex
by the complex $F(L^\bullet)$ and $RF(\sigma_{\geq c}L^\bullet)$
is represented by $\sigma_{\geq c}F(L^\bullet)$. Consider the

```

Proposed corrected reading:

```tex
by the complex $F(L^\bullet)$ and, for every integer $c$,
$RF(\sigma_{\geq c}L^\bullet)$ is represented by
$\sigma_{\geq c}F(L^\bullet)$. Consider the

```

## MC-STK-ERR-2548: DERIVED-NEW-036

End the sum at K_(n_i-1), set h to zero at selected indices, and use the least selected upper endpoint to include the initial segment in h and c.

Complete proof: [evidence/review/PROOFS_10139_10427.md](evidence/review/PROOFS_10139_10427.md); section(s) 3.

Original derived.tex line 10263:

```tex
If $n_{i - 1} < j \leq n_i$, then we let $c_j = c|_{K_j}$
be the map

```

Proposed corrected reading:

```tex
For each $j$, let $i$ be the least index such that $j \leq n_i$.
We let $c_j = c|_{K_j}$ be the map (the identity when $j = n_i$)

```

Original derived.tex line 10283:

```tex
the rule: for $n_{i - 1} < j < n_i$ we set
$$
h_j : K_j
\xrightarrow{1,\ f_j,\ f_{j + 1} \circ f_j,
\ \ldots,\ f_{n_i - 1} \circ \ldots \circ f_j}
K_j \oplus \ldots \oplus K_{n_i}
$$

```

Proposed corrected reading:

```tex
the rule: let $i$ be the least index such that $j \leq n_i$.
Set $h_j = 0$ if $j = n_i$. For $j < n_i$ we set
$$
h_j : K_j
\xrightarrow{1,\ f_j,\ f_{j + 1} \circ f_j,
\ \ldots,\ f_{n_i - 2} \circ \ldots \circ f_j}
K_j \oplus \ldots \oplus K_{n_i - 1}
$$
where for $j = n_i - 1$ this map has just the identity component.

```

## MC-STK-ERR-2549: DERIVED-NEW-035

Use psi phi for the subsequence triangle and phi psi for the full triangle in all three expressions.

Complete proof: [evidence/review/PROOFS_10139_10427.md](evidence/review/PROOFS_10139_10427.md); section(s) 3.

Original derived.tex line 10278:

```tex
$\varphi \circ \psi$ is an isomorphism by

```

Proposed corrected reading:

```tex
$\psi \circ \varphi$ is an isomorphism by

```

Original derived.tex line 10292:

```tex
$\text{id} - \psi \circ \varphi$ has square zero by
Lemma \ref{lemma-third-map-square-zero} (small argument omitted).
In other words, $\psi \circ \varphi$ differs from the identity

```

Proposed corrected reading:

```tex
$\text{id} - \varphi \circ \psi$ has square zero by
Lemma \ref{lemma-third-map-square-zero} (small argument omitted).
In other words, $\varphi \circ \psi$ differs from the identity

```

## MC-STK-ERR-2550: DERIVED-NEW-037

Equality of their isomorphism closures, using the given shift comparison of the exact functor.

Complete proof: [evidence/review/PROOFS_10691_11108.md](evidence/review/PROOFS_10691_11108.md); section(s) 2.

Original derived.tex line 10800:

```tex
F(\mathcal{A}[a, b]) = F(\mathcal{A})[a, b]
$$

```

Proposed corrected reading:

```tex
\operatorname{Iso}(F(\mathcal{A}[a, b])) =
\operatorname{Iso}(F(\mathcal{A})[a, b]),
$$
where $\operatorname{Iso}$ denotes isomorphism closure. Moreover,

```

## MC-STK-ERR-2551: DERIVED-NEW-039

The actual lift is E_i[m] to X_1[-1] to (hocolim X_n)[-1].

Complete proof: [evidence/review/PROOFS_11121_11450.md](evidence/review/PROOFS_11121_11450.md); section(s) 2.

Original derived.tex line 11209:

```tex
$\text{hocolim} X_n$ and we conclude that our morphism $E_i[m] \to C$

```

Proposed corrected reading:

```tex
$(\text{hocolim} X_n)[-1]$ and we conclude that our morphism $E_i[m] \to C$

```

## MC-STK-ERR-2552: DERIVED-RECON-091

Join the introductory With-assumptions phrase to its complete if/then sentence.

Complete proof: [evidence/review/PROOFS_11121_11450.md](evidence/review/PROOFS_11121_11450.md); section(s) 8.

Original derived.tex line 11216:

```tex
With assumptions and notation as in Lemma \ref{lemma-write-as-colimit}.
If $C$ is a compact object and $C \to X_n$ is a morphism, then

```

Proposed corrected reading:

```tex
With assumptions and notation as in Lemma \ref{lemma-write-as-colimit},
if $C$ is a compact object and $C \to X_n$ is a morphism, then

```

## MC-STK-ERR-2553: DERIVED-NEW-040

Their composites into Y_(n-1)[1] agree. The exact Hom sequence then lifts their difference to X_(n-1).

Complete proof: [evidence/review/PROOFS_11121_11450.md](evidence/review/PROOFS_11121_11450.md); section(s) 3.

Original derived.tex line 11255:

```tex
the compositions into $Y_{n - 1}$ are equal. Let $C \to X_{n - 1}$

```

Proposed corrected reading:

```tex
the compositions into $Y_{n - 1}[1]$ are equal. Let $C \to X_{n - 1}$

```

## MC-STK-ERR-2554: DERIVED-RECON-095

Insert there is to complete the sentence asserting the natural transformation.

Complete proof: [evidence/review/PROOFS_11121_11450.md](evidence/review/PROOFS_11121_11450.md); section(s) 5.

Original derived.tex line 11386:

```tex
in $\prod H(X_n)$. Hence a natural transformation

```

Proposed corrected reading:

```tex
in $\prod H(X_n)$. Hence there is a natural transformation

```

## MC-STK-ERR-2555: DERIVED-RECON-096

Insert there is to complete the sentence asserting the natural transformation.

Complete proof: [evidence/review/PROOFS_11460_11655.md](evidence/review/PROOFS_11460_11655.md); section(s) 6.

Original derived.tex line 11536:

```tex
in $\prod H(X_n)$. Hence a natural transformation

```

Proposed corrected reading:

```tex
in $\prod H(X_n)$. Hence there is a natural transformation

```

## MC-STK-ERR-2556: DERIVED-NEW-041

Prove the restricted Yoneda countable-coproduct comparison by evaluation presentations. Split the restricted tower from its second stage into its common quotient and killed kernels, construct the finite-prefix left inverse, and retain the initial stage by an explicit target automorphism.

Complete proof: [evidence/review/PROOFS_11460_11655.md](evidence/review/PROOFS_11460_11655.md); section(s) 3.

Original derived.tex line 11547:

```tex
Let $E \in \mathcal{E}$. Let us show that
$$
\Hom_\mathcal{D}(E, \bigoplus X_n) \to  \Hom_\mathcal{D}(E, \bigoplus X_n)
$$
is injective. Namely, let $\alpha : E \to \bigoplus X_n$. Then
by assumption (2) we obtain a factorization
$\alpha = (\bigoplus \beta_n) \circ \gamma$.
Since $E_n \to X_n \to X_{n + 1}$ is zero by construction, we see that
the composition $\bigoplus E_n \to \bigoplus X_n \to \bigoplus X_n$
is equal to $\bigoplus \beta_n$. Hence also the composition
$E \to \bigoplus X_n \to \bigoplus X_n$ is equal to $\alpha$.
This proves the stated injectivity and hence also
$$
\Hom_\mathcal{D}(E, \bigoplus X_n[1]) \to \Hom_\mathcal{D}(E, \bigoplus X_n[1])
$$
is injective. It follows that we have an exact sequence
$$
\Hom_\mathcal{D}(E, \bigoplus X_n) \to
\Hom_\mathcal{D}(E, \bigoplus X_n) \to
\Hom_\mathcal{D}(E, X) \to 0
$$
for all $E \in \mathcal{E}$.

```

Proposed corrected reading:

```tex
Let us prove that the telescope map is injective on maps from
each $E \in \mathcal{E}$. Let $\mathcal{P}$ be the full subcategory
of direct sums of objects of $\mathcal{E}$ and write
$hY = \Hom_\mathcal{D}(-, Y)|_\mathcal{P}$.
Let $\mathcal{A}$ be the category of additive functors
$\mathcal{P}^{opp} \to \textit{Ab}$ taking direct sums to products.
Kernels and cokernels in this category are computed pointwise:
both commute with products of abelian groups.
Thus $\mathcal{A}$ is abelian. Natural transformations form sets,
since they are determined by their components at the set $\mathcal{E}$.

\medskip\noindent
We first show that $h$ preserves countable direct sums with values
in $\mathcal{A}$. For every object $Y$ choose the evaluation map
$P_Y = \bigoplus_{(E, f : E \to Y)} E \to Y$, complete it to a
distinguished triangle $C_Y \to P_Y \to Y \to C_Y[1]$, and choose
an evaluation map $Q_Y \to C_Y$ with $Q_Y \in \mathcal{P}$.
We obtain an exact presentation
$$
hQ_Y \to hP_Y \to hY \to 0.
$$
For any countable family $Y_n$, assumption (2) shows that
$\bigoplus P_{Y_n} \to \bigoplus Y_n$ is surjective on maps from
every $E \in \mathcal{E}$: factor such a map through $\bigoplus E_n$
and lift each $E_n \to Y_n$ to $P_{Y_n}$.
The same holds for $\bigoplus Q_{Y_n} \to \bigoplus C_{Y_n}$.
It holds for maps from every object of $\mathcal{P}$ by taking products.
The direct sum of the distinguished triangles therefore gives
an exact presentation
$$
h(\bigoplus Q_{Y_n}) \to h(\bigoplus P_{Y_n}) \to
h(\bigoplus Y_n) \to 0.
$$
For $F \in \mathcal{A}$, Yoneda's lemma and the product property give
$$
\Hom_\mathcal{A}(h(\bigoplus Y_n), F)
= \Ker\left(\prod F(P_{Y_n}) \to \prod F(Q_{Y_n})\right)
= \prod \Hom_\mathcal{A}(hY_n, F).
$$
These identifications are induced by the inclusions of the summands.
Thus $h(\bigoplus Y_n)$ is their direct sum in $\mathcal{A}$.
This does not assert that these direct sums are computed pointwise.

\medskip\noindent
Put $T = H|_\mathcal{P}$ and $M_n = hX_n$, and denote the
transformations induced by $a_n$ by $\theta_n : M_n \to T$.
Each $\theta_n$ is surjective, first on $\mathcal{E}$ by construction
of $X_1$, and then on $\mathcal{P}$ by taking products.
Write $u_n : X_n \to X_{n + 1}$ and $v_n = h(u_n)$.
The construction gives
$v_n(\Ker(\theta_n)) = 0$ and $\theta_{n + 1}v_n = \theta_n$.
Hence $v_1$ factors as $\sigma_2\theta_1$ for a morphism
$\sigma_2 : T \to M_2$ with $\theta_2\sigma_2 = 1$.
Inductively put $\sigma_{n + 1} = v_n\sigma_n$ for $n \geq 2$.
Then $\theta_n\sigma_n = 1$, and with $L_n = \Ker(\theta_n)$
the isomorphisms
$$
T \oplus L_n \longrightarrow M_n,\qquad (x, z) \longmapsto \sigma_nx + z
$$
identify $v_n$, for $n \geq 2$, with $(x, z) \mapsto (x, 0)$.

\medskip\noindent
Let $V = \bigoplus_{n \geq 2} M_n$ in $\mathcal{A}$.
Its idempotent induced by the $\sigma_n\theta_n$ splits it as
$$
V = C \oplus L,\qquad
C = \bigoplus_{n \geq 2} T,\quad L = \bigoplus_{n \geq 2} L_n.
$$
These last two direct sums exist as the images of that idempotent
and its complement; their universal properties follow from the
component splittings. The tail telescope map $t_V$ is
$(1 - s_C) \oplus 1_L$, where $s_C j_n = j_{n + 1}$ for the
inclusions $j_n : T \to C$. The morphism $\ell_C : C \to C$ defined by
$$
\ell_C j_n = -\sum_{j = 2}^{n - 1} j_j
$$
(the empty sum is zero) satisfies $\ell_C(1 - s_C) = 1_C$.
Thus $\ell_V = \ell_C \oplus 1_L$ is a left inverse of $t_V$.
For the entire sequence, use the canonical isomorphism
$h(\bigoplus X_n) \cong M_1 \oplus V$ and write $b : M_1 \to V$
for $v_1$ followed by the inclusion of $M_2$.
The entire telescope map is
$$
(x, y) \longmapsto (x, t_V y - bx),
$$
and it has the left inverse
$$
(x, y) \longmapsto (x, \ell_V(y + bx)).
$$
Evaluating at $E \in \mathcal{E}$ proves the required injectivity.
Evaluating at $E[-1]$ proves injectivity on
$\Hom_\mathcal{D}(E, \bigoplus X_n[1])$ as well.
The distinguished triangle defining $X$ now gives the exact sequence
$$
\Hom_\mathcal{D}(E, \bigoplus X_n) \to
\Hom_\mathcal{D}(E, \bigoplus X_n) \to
\Hom_\mathcal{D}(E, X) \to 0
$$
for every $E \in \mathcal{E}$.

```

## MC-STK-ERR-2557: DERIVED-NEW-042

Require strictly full subcategories invariant under all shifts, then prove that (3) gives B=A-perp and A=left-perp-B. Their saturated triangulated structures follow, so the adjoint criteria apply.

Complete proof: [evidence/review/PROOFS_11665_12003.md](evidence/review/PROOFS_11665_12003.md); section(s) 4.

Original derived.tex line 11956:

```tex
be subcategories. The following are equivalent

```

Proposed corrected reading:

```tex
be strictly full subcategories invariant under all shifts.
The following are equivalent

```

Original derived.tex line 11976:

```tex
The equivalence between (1), (2), and (3) follows in a straightforward manner
from Lemmas \ref{lemma-right-adjoint} and \ref{lemma-left-adjoint} (small
detail omitted). Denote $v : \mathcal{D} \to \mathcal{A}$ the right

```

Proposed corrected reading:

```tex
Assume (3). Then $\mathcal{B} \subset \mathcal{A}^\perp$ and
$\mathcal{A} \subset {}^\perp\mathcal{B}$.
If $X \in \mathcal{A}^\perp$, its triangle in (3) has zero first map,
so $B \cong X \oplus A[1]$.
Since $\Hom(A[1], B) = 0$, we obtain $A = 0$ and
$X \cong B \in \mathcal{B}$. Strict fullness gives
$\mathcal{A}^\perp = \mathcal{B}$.
Similarly, if $X \in {}^\perp\mathcal{B}$, the second map of its
triangle is zero, so $A \cong X \oplus B[-1]$.
Since $\Hom(A, B[-1]) = 0$, we obtain $B = 0$ and
$X \cong A \in \mathcal{A}$.
Thus $\mathcal{A} = {}^\perp\mathcal{B}$.
The orthogonal subcategories are saturated and triangulated as shown above.
Lemmas \ref{lemma-right-adjoint} and \ref{lemma-left-adjoint}
now give (1) and (2).
Conversely, each of (1) and (2) gives (3) by its adjoint criterion.
Denote $v : \mathcal{D} \to \mathcal{A}$ the right

```

## MC-STK-ERR-2558: DERIVED-RECON-100

Use Y_(n-2) as the preceding stage receiving the Postnikov lift.

Complete proof: [evidence/review/PROOFS_12008_12370.md](evidence/review/PROOFS_12008_12370.md); section(s) 2.

Original derived.tex line 12160:

```tex
know whether the composition $X_n \to X_{n - 1} \to Y_{n - 1}$

```

Proposed corrected reading:

```tex
know whether the composition $X_n \to X_{n - 1} \to Y_{n - 2}$

```

## MC-STK-ERR-2559: DERIVED-NEW-043

All three conditions imply terminal-map uniqueness; condition (3) additionally implies uniqueness of the whole map of systems.

Complete proof: [evidence/review/PROOFS_12008_12370.md](evidence/review/PROOFS_12008_12370.md); section(s) 4.

Original derived.tex line 12253:

```tex
then there exists at most one morphism between these Postnikov systems.

```

Proposed corrected reading:

```tex
then any two morphisms between these Postnikov systems induce the same
morphism $Y_n \to Y'_n$. In case (3), the morphism of Postnikov
systems itself is unique.

```

## MC-STK-ERR-2560: DERIVED-NEW-044

Compute both off-diagonal blocks. Constant-to-pro-zero vanishes at every index; pro-zero-to-constant vanishes only on a further tail. Take that tail before applying TR3.

Complete proof: [evidence/review/PROOFS_12380_12604.md](evidence/review/PROOFS_12380_12604.md); section(s) 2.

Original derived.tex line 12451:

```tex
$\delta : C \to A[1]$ which is independent of $n$. Choose a distinguished

```

Proposed corrected reading:

```tex
$\delta : C \to A[1]$ which is independent of $n$.
The components $C'_n \to A[1]$ vanish for all sufficiently large $n$:
fix an index and use a later zero transition in $(C'_n)$.
After increasing the starting index once more, the projections onto
$C$ and $A[1]$ commute with the connecting maps. Choose a distinguished

```

## MC-STK-ERR-2561: DERIVED-NEW-014

Name K_3 as the actual receiving truncation. Both truncations vanish, so the theorem is not refuted.

Complete proof: [evidence/review/PROOFS_3487_4161.md](evidence/review/PROOFS_3487_4161.md); section(s) 6.

Original more-algebra.tex line 22722:

```tex
$\tau_{\leq -2}K_2 = 0$
```

Proposed corrected reading:

```tex
$\tau_{\leq -2}K_3 = 0$
```

## MC-STK-ERR-2562: DERIVED-NEW-022

Use the original-term truncation with n>=max(1,N), prove the exact tail bound, and retain the comparison to canonical truncation through the image sheaf J[n].

Complete proof: [evidence/review/PROOFS_5091_5900.md](evidence/review/PROOFS_5091_5900.md); section(s) 7.

Original perfect.tex line 529:

```tex
may assume $S$ affine. By
Lemma \ref{lemma-quasi-coherence-direct-image}
we have $R^0f_*\mathcal{F}^\bullet = R^0f_*\tau_{\geq -n}\mathcal{F}^\bullet$
for all sufficiently large $n$. Thus we may assume $\mathcal{F}^\bullet$
bounded below. As each $\mathcal{F}^n$ is right $f_*$-acyclic by
assumption we see that $f_*\mathcal{F}^\bullet \to Rf_*\mathcal{F}^\bullet$
is a quasi-isomorphism by Leray's acyclicity lemma (Derived Categories, Lemma
\ref{derived-lemma-leray-acyclicity}).
```

Proposed corrected reading:

```tex
may assume $S$ affine. Choose $N$ as in
Lemma \ref{lemma-quasi-coherence-direct-image} and an integer
$n \geq \max\{1, N\}$. The termwise split short exact sequence
$$
0 \to \sigma_{\geq -n}\mathcal{F}^\bullet \to
\mathcal{F}^\bullet \to \sigma_{\leq -n-1}\mathcal{F}^\bullet \to 0
$$
gives a distinguished triangle. The last complex has quasi-coherent
cohomology, vanishing in degrees greater than $-n-1$. The bound $N$
therefore gives vanishing of
$H^j(Rf_*\sigma_{\leq -n-1}\mathcal{F}^\bullet)$ for $j \geq N-n-1$,
in particular for $j=-1,0$. It follows that
$H^0(Rf_*\sigma_{\geq -n}\mathcal{F}^\bullet) \to
H^0(Rf_*\mathcal{F}^\bullet)$ is an isomorphism.
Also $H^0(f_*\sigma_{\geq -n}\mathcal{F}^\bullet) =
H^0(f_*\mathcal{F}^\bullet)$ since $n \geq 1$.
The complex $\sigma_{\geq -n}\mathcal{F}^\bullet$ is bounded below
and consists of the original right $f_*$-acyclic terms, so it computes
$Rf_*$ by Leray's acyclicity lemma (Derived Categories, Lemma
\ref{derived-lemma-leray-acyclicity}). Naturality of the canonical map
now proves the desired isomorphism in degree zero.
```

## MC-STK-ERR-2563: DERIVED-PERFECT-RECEIVER-001

Use D_QCoh(O_X), the actual ambient category, and the proved finite-stage hypotheses in the propagated argument.

Complete proof: [evidence/review/PROOFS_11121_11450.md](evidence/review/PROOFS_11121_11450.md); section(s) 7.

Original perfect.tex line 4324:

```tex
the perfect objects define compact objects of $D(\mathcal{O}_X)$

```

Proposed corrected reading:

```tex
the perfect objects define compact objects of $D_\QCoh(\mathcal{O}_X)$

```

Original perfect.tex line 4396:

```tex
using the generator $E$. Since the functor $\mathcal{D} \to D(\mathcal{O}_X)$
commutes with direct sums, we see that $K = \text{hocolim} K_n$
holds in $D(\mathcal{O}_X)$. Since $\mathcal{O}_X$ is a compact
object of $D(\mathcal{O}_X)$ we find an $n$ and a morphism
$\alpha_n : \mathcal{O}_X \to K_n$ which gives rise to $\alpha$, see
Derived Categories, Lemma \ref{derived-lemma-commutes-with-countable-sums}.
By Derived Categories, Lemma \ref{derived-lemma-factor-through}
applied to the morphism $\mathcal{O}_X[0] \to K_n$ in the ambient
category $D(\mathcal{O}_X)$ we see that $\alpha_n$ factors as

```

Proposed corrected reading:

```tex
using the generator $E$. Since the functor $\mathcal{D} \to D_\QCoh(\mathcal{O}_X)$
commutes with direct sums, we see that $K = \text{hocolim} K_n$
holds in $D_\QCoh(\mathcal{O}_X)$. Since $\mathcal{O}_X$ is a compact
object of $D_\QCoh(\mathcal{O}_X)$ we find an $n$ and a morphism
$\alpha_n : \mathcal{O}_X \to K_n$ which gives rise to $\alpha$, see
Derived Categories, Lemma \ref{derived-lemma-commutes-with-countable-sums}.
By the finite-stage argument in the proof of Derived Categories, Lemma \ref{derived-lemma-factor-through}
applied to the morphism $\mathcal{O}_X[0] \to K_n$ in the ambient
category $D_\QCoh(\mathcal{O}_X)$, which does not require $E$ to generate
the ambient category, we see that $\alpha_n$ factors as

```

## MC-STK-ERR-2564: DERIVED-PERFECT-RECEIVER-002

Insert that in we will use that there exists a generator.

Complete proof: [evidence/review/PROOFS_11121_11450.md](evidence/review/PROOFS_11121_11450.md); section(s) 7.

Original perfect.tex line 4326:

```tex
sums. For the converse we will use there exists a generator

```

Proposed corrected reading:

```tex
sums. For the converse we will use that there exists a generator

```

## MC-STK-ERR-2565: DERIVED-PERFECT-RECEIVER-003

Use the stated global cohomology group rather than a cohomology sheaf in the compactness comparison.

Complete proof: [evidence/review/PROOFS_11121_11450.md](evidence/review/PROOFS_11121_11450.md); section(s) 7.

Original perfect.tex line 4385:

```tex
$H^0(K) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[0], K)$.

```

Proposed corrected reading:

```tex
$H^0(X, K) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[0], K)$.

```

## MC-STK-ERR-2566: DERIVED-PERFECT-RECEIVER-004

Quantify over the actual input object in the adjoint criterion.

Complete proof: [evidence/review/PROOFS_11665_12003.md](evidence/review/PROOFS_11665_12003.md); section(s) 7.

Original perfect.tex line 4848:

```tex
The adjoint exists if and only if for every object $K$ of

```

Proposed corrected reading:

```tex
The adjoint exists if and only if for every object $E$ of

```

## MC-STK-ERR-2567: DERIVED-NEW-031

Display the actual middle row with kernel I^(i+2)/I^(i+3), middle I^i/I^(i+3), quotient I^i/I^(i+2), and its pullback.

Complete proof: [evidence/review/PROOFS_8774_9196.md](evidence/review/PROOFS_8774_9196.md); section(s) 5.

Original cohomology.tex line 14424:

```tex
using that the module $\mathcal{I}^i/\mathcal{I}^{i + 3}$
is an extension of $\mathcal{I}^{i + 1}/\mathcal{I}^{i + 3}$
by $\mathcal{I}^i/\mathcal{I}^{i + 1}$.

```

Proposed corrected reading:

```tex
using the exact sequence
$$
0 \to \mathcal{I}^{i + 2}/\mathcal{I}^{i + 3}
\to \mathcal{I}^i/\mathcal{I}^{i + 3}
\to \mathcal{I}^i/\mathcal{I}^{i + 2} \to 0.
$$
Its pullback along
$\mathcal{I}^{i + 1}/\mathcal{I}^{i + 2}
\to \mathcal{I}^i/\mathcal{I}^{i + 2}$
is the extension
$0 \to \mathcal{I}^{i + 2}/\mathcal{I}^{i + 3}
\to \mathcal{I}^{i + 1}/\mathcal{I}^{i + 3}
\to \mathcal{I}^{i + 1}/\mathcal{I}^{i + 2} \to 0$.

```

## MC-STK-ERR-2568: DERIVED-NEW-038

Use H^i(X,K tensor^L E) and H^i(X,F tensor E), keeping the fixed finite locally free E and the original final dimension bound.

Complete proof: [evidence/review/PROOFS_10691_11108.md](evidence/review/PROOFS_10691_11108.md); section(s) 8.

Original equiv.tex line 1836:

```tex
Since $K$ is perfect, there exist $a \leq b$ such that
$H^i(X, K)$ is nonzero only for $i \in [a, b]$. Since $X$ is proper,
each $H^i(X, K)$ is finite dimensional. We conclude that

```

Proposed corrected reading:

```tex
Since $K \otimes_{\mathcal{O}_X}^\mathbf{L} \mathcal{E}$ is perfect,
there exist $a \leq b$ such that its cohomology
$H^i(X, K \otimes_{\mathcal{O}_X}^\mathbf{L} \mathcal{E})$ is nonzero
only for $i \in [a, b]$. Since $X$ is proper, each of these groups
is finite dimensional. We conclude that

```

Original equiv.tex line 1862:

```tex
for any $a \leq b$ such that $H^i(X, \mathcal{F})$ is nonzero only
for $i \in [a, b]$. Thus we can take $a = 0$ and $b = \dim(X)$.

```

Proposed corrected reading:

```tex
for any $a \leq b$ such that
$H^i(X, \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{E})$
is nonzero only for $i \in [a, b]$, where $\mathcal{E}$ is the
finite locally free module chosen in the preceding proof.
Thus we can take $a = 0$ and $b = \dim(X)$.

```

## MC-STK-ERR-2569: DERIVED-SPACES-PERFECT-RECEIVER-001

Quantify over the actual input object in the algebraic-space adjoint criterion.

Complete proof: [evidence/review/PROOFS_11665_12003.md](evidence/review/PROOFS_11665_12003.md); section(s) 7.

Original spaces-perfect.tex line 4459:

```tex
The adjoint exists if and only if for every object $K$ of

```

Proposed corrected reading:

```tex
The adjoint exists if and only if for every object $E$ of

```
