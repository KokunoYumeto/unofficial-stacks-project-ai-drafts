# Fields: corrections and complete decomposition proof

47 proposed corrections and clarifications: 21 copyedits, 21 source corrections and five clarifications. All 75 received reports retain their decisions and adverse evidence, including optional proposals and previously composed repairs. All eight earlier Fields corrections remain intact. The normal algebraic decomposition now has its complete multiplication-map proof. The transcendence-basis statement exposes the extension property already proved in its source. Further consequences are proved separately in the retained proof evidence; no new theorem is mislabelled as a received defect.

Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.

## MC-STK-ERR-1859 — FIELDS-RECON-003 (copyedit)

Insert the missing conjunction between the two predicates finite and equal to the prime field.

Official fields.tex line 221:

```tex
or finite equal to
```

Replace with:

```tex
or finite and equal to
```

## MC-STK-ERR-1860 — FIELDS-RECON-004 (copyedit)

Remove the extra preposition before the displayed arrow describing the morphisms.

Official fields.tex line 295:

```tex
morphisms from $E \to E'$
```

Replace with:

```tex
morphisms $E \to E'$
```

## MC-STK-ERR-1861 — FIELDS-RECON-005 (copyedit)

Give the singular subject class a singular verb while retaining exactly the extensions described by the relative clause.

Official fields.tex line 605:

```tex
An important class of extensions are those where every element generates
```

Replace with:

```tex
An important class consists of extensions where every element generates
```

## MC-STK-ERR-1862 — FIELDS-RECON-006 (copyedit)

Restore the missing verb in the let-construction introducing the nonconstant meromorphic function.

Official fields.tex line 636:

```tex
$f \in \mathbf{C}(X) - \mathbf{C}$ any
```

Replace with:

```tex
$f \in \mathbf{C}(X) - \mathbf{C}$ be any
```

## MC-STK-ERR-1863 — FIELDS-RECON-007 (copyedit)

Make the grammatical subject the numbers that receive the name algebraic numbers, matching the existing plural verb.

Official fields.tex line 712:

```tex
The set of complex numbers that are algebraic
```

Replace with:

```tex
The complex numbers that are algebraic
```

## MC-STK-ERR-1864 — FIELDS-RECON-008 (source_correction)

The quotient belongs to the finite field k(alpha,beta) only when its denominator is nonzero. State that domain condition explicitly; each resulting generated subfield is finite over k and its generator is algebraic by the cited lemmas.

Official fields.tex line 732:

```tex
product and quotient of $\alpha$ and $\beta$.
```

Replace with:

```tex
product and, when $\beta \not = 0$, the quotient of $\alpha$ by $\beta$.
```

## MC-STK-ERR-1865 — FIELDS-RECON-009 (source_correction)

The finite set S of polynomial coefficients lies in E and generates k(S) between k and E. The subextension is therefore of E/k.

Official fields.tex line 748:

```tex
finitely generated subextension of $k$.
```

Replace with:

```tex
finitely generated subextension of $E/k$.
```

## MC-STK-ERR-1866 — FIELDS-RECON-010 (copyedit)

Insert the missing verb introducing the algebraic field extension.

Official fields.tex line 808:

```tex
Let $E/F$ an algebraic extension
```

Replace with:

```tex
Let $E/F$ be an algebraic extension
```

## MC-STK-ERR-1867 — FIELDS-RECON-011 (copyedit)

Separate the two independent clauses with a semicolon.

Official fields.tex line 897:

```tex
complex analysis, we shall
```

Replace with:

```tex
complex analysis; we shall
```

## MC-STK-ERR-1868 — FIELDS-RECON-012 (source_correction)

The statement permits arbitrary towers, but the original proof chooses finite bases without a finiteness hypothesis. The added direct-sum map is proved surjective and injective with every coefficient support explicit, establishing the stated cardinal degree formula for arbitrary extensions.

Official fields.tex line 550:

```tex
Let $\alpha_1, \ldots, \alpha_n \in F$ be an $E$-basis for $F$. Let
```

Replace with:

```tex
First suppose both degrees on the right are finite.
Let $\alpha_1, \ldots, \alpha_n \in F$ be an $E$-basis for $F$. Let
```

Official fields.tex line 580:

```tex
Then $k$-linear independence of the $\{\beta_j\}$ shows that the
$c_{ij}$ all vanish.
```

Replace with:

```tex
Then $k$-linear independence of the $\{\beta_j\}$ shows that the
$c_{ij}$ all vanish.

\medskip\noindent
For arbitrary extensions, choose an $E$-basis
$\{\alpha_i\}_{i \in I}$ of $F$ and a $k$-basis
$\{\beta_j\}_{j \in J}$ of $E$. Define the $k$-linear map
$$
\Phi : \bigoplus_{(i,j) \in I \times J} k \longrightarrow F,
\qquad
(c_{ij}) \longmapsto \sum_{(i,j) \in I \times J} c_{ij}\alpha_i\beta_j.
$$
The direct sum means that the family $(c_{ij})$ has finite support,
so the displayed sum is defined. For $f \in F$, write
$f = \sum_{i \in I_0} a_i\alpha_i$ with $I_0 \subset I$ finite and
$a_i \in E$. For every $i \in I_0$, write
$a_i = \sum_{j \in J_i} b_{ij}\beta_j$ with $J_i \subset J$ finite
and $b_{ij} \in k$. Then
$$
f = \sum_{i \in I_0}\sum_{j \in J_i} b_{ij}\alpha_i\beta_j,
$$
so $\Phi$ is surjective. If a finitely supported family $(c_{ij})$
has image zero, regrouping its finite sum gives
$$
0 = \sum_{i \in I}\alpha_i
\left(\sum_{j \in J} c_{ij}\beta_j\right).
$$
The $E$-linear independence of the $\alpha_i$ makes each inner sum
zero. The $k$-linear independence of the $\beta_j$ then gives
$c_{ij} = 0$ for every $(i,j)$, so $\Phi$ is injective.
Thus the products form a $k$-basis indexed by $I \times J$,
and $[F:k] = |I \times J| = |I||J| = [F:E][E:k]$,
including when a degree is infinite. The original finite-degree
calculation is the case $I = \{1,\ldots,n\}$ and $J = \{1,\ldots,m\}$.
```

## MC-STK-ERR-1869 — FIELDS-RECON-013 (clarification)

Choose the annihilating polynomial nonzero, as guaranteed by algebraicity, so that its distinct roots form a finite set and the generated intermediate field is finite.

Official fields.tex line 818:

```tex
polynomial such that $P(\alpha) = 0$.
```

Replace with:

```tex
nonzero polynomial such that $P(\alpha) = 0$.
```

## MC-STK-ERR-1870 — FIELDS-RECON-014 (copyedit)

Restore the prepositions naming the indexed extension of the fixed field F.

Official fields.tex line 991:

```tex
we will denote $E_i
```

Replace with:

```tex
we will denote by $E_i
```

Official fields.tex line 992:

```tex
field extension to $F$
```

Replace with:

```tex
field extension of $F$
```

## MC-STK-ERR-1871 — FIELDS-RECON-015 (copyedit)

Correct the participial adjective and indefinite article in the Zorn argument.

Official fields.tex line 1003:

```tex
every totally order subset of $I$ has a upper bound
```

Replace with:

```tex
every totally ordered subset of $I$ has an upper bound
```

## MC-STK-ERR-1872 — FIELDS-RECON-016 (copyedit)

Restore the consequence marker after choosing alpha outside the maximal intermediate field.

Official fields.tex line 1040:

```tex
The $\alpha$ is algebraic
```

Replace with:

```tex
Then $\alpha$ is algebraic
```

## MC-STK-ERR-1873 — FIELDS-RECON-018 (source_correction)

The roots belong to the algebraically closed field K fixed in this paragraph; lowercase k is not introduced there.

Official fields.tex line 1081:

```tex
\alpha_n \in k
```

Replace with:

```tex
\alpha_n \in K
```

## MC-STK-ERR-1874 — FIELDS-RECON-019 (source_correction)

For nonzero P the product of the displayed monic factors has leading coefficient 1, so the multiplier c is the leading coefficient. The constant coefficient is c times the product of all negative roots.

Official fields.tex line 1081:

```tex
constant term
```

Replace with:

```tex
leading coefficient
```

## MC-STK-ERR-1875 — FIELDS-RECON-020 (copyedit)

Capitalize the opening word of the second complete sentence in the enumeration.

Official fields.tex line 1192:

```tex
\item if $K$
```

Replace with:

```tex
\item If $K$
```

## MC-STK-ERR-1876 — FIELDS-RECON-021 (copyedit)

Use the plural sets for the two root sets compared by the Frobenius bijection, preserving the plural verb have.

Official fields.tex line 1228:

```tex
the set of roots of $P$ and $P(x^p)$
```

Replace with:

```tex
the sets of roots of $P$ and $P(x^p)$
```

## MC-STK-ERR-1877 — FIELDS-RECON-022 (copyedit)

Correct the finite verb in the declarative introduction of the situation.

Official fields.tex line 1270:

```tex
Here $F$ be a field
```

Replace with:

```tex
Here $F$ is a field
```

## MC-STK-ERR-1878 — FIELDS-RECON-023 (copyedit)

Add the missing preposition in the naming construction.

Official fields.tex line 1277:

```tex
Denote $P_i$
```

Replace with:

```tex
Denote by $P_i$
```

## MC-STK-ERR-1879 — FIELDS-RECON-025 (copyedit)

Correct both misspellings of homomorphism.

Official fields.tex line 1313:

```tex
homorphism
```

Replace with:

```tex
homomorphism
```

Official fields.tex line 1320:

```tex
homorphism
```

Replace with:

```tex
homomorphism
```

## MC-STK-ERR-1880 — FIELDS-RECON-028 (copyedit)

Restore the past participle in the reference to the part already established.

Official fields.tex line 1379:

```tex
already prove above
```

Replace with:

```tex
already proved above
```

## MC-STK-ERR-1881 — FIELDS-RECON-029 (copyedit)

Bind the omitted index of the vanishing coefficient.

Official fields.tex line 1473:

```tex
for some, then
```

Replace with:

```tex
for some $i$, then
```

## MC-STK-ERR-1882 — FIELDS-RECON-030 (source_correction)

The union of an empty chain is not a field containing F. Give that chain the existing element F as an upper bound, and apply the union construction to nonempty chains.

Official fields.tex line 1000:

```tex
Let $T \subset I$ be a totally ordered subset. Then it is clear that
```

Replace with:

```tex
The empty totally ordered subset has an upper bound given by the
field $F$ with its given operations. Let $T \subset I$ be a nonempty
totally ordered subset. Then it is clear that
```

## MC-STK-ERR-1883 — FIELDS-RECON-031 (source_correction)

Treat the empty chain separately using the prescribed embedding of F in its algebraic closure.

Official fields.tex line 1034:

```tex
$\varphi'|_E = \varphi$. If $T = \{(E_t,  \varphi_t)\} \subset I$
```

Replace with:

```tex
$\varphi'|_E = \varphi$. The empty chain has the upper bound
$(F, F \hookrightarrow \overline{F})$. If
$T = \{(E_t, \varphi_t)\} \subset I$ is nonempty and
```

Official fields.tex line 1035:

```tex
is a totally ordered subset, then
```

Replace with:

```tex
totally ordered, then
```

## MC-STK-ERR-1884 — FIELDS-RECON-032 (source_correction)

The finite complete root factorization with a leading coefficient requires a nonzero polynomial. Constants are included with no roots and the empty product equal to 1.

Official fields.tex line 1077:

```tex
every polynomial $P \in K[x]$
```

Replace with:

```tex
every nonzero polynomial $P \in K[x]$
```

## MC-STK-ERR-1885 — FIELDS-RECON-033 (source_correction)

The original contradiction used a strict degree bound for a generator of (P,P prime) without excluding the zero derivative. Split off that actual second case and prove the contradiction when the derivative is nonzero.

Official fields.tex line 1146:

```tex
Note that $P'$ has degree $< \deg(P)$. Hence if $P$ and $P'$ are not relatively
prime, then $(P, P') = (R)$ where $R$ is a polynomial of degree $< \deg(P)$
contradicting the irreducibility of $P$. This proves we have the dichotomy
between (1) and (2).
```

Replace with:

```tex
If $P' = 0$, we are in case (2). Otherwise
$\deg(P') < \deg(P)$. If $P$ and $P'$ were not relatively prime,
write $(P, P') = (R)$. Then $R$ is a nonunit divisor of $P$,
so irreducibility gives $(R) = (P)$. But $R$ also divides the
nonzero polynomial $P'$, which would force
$\deg(P) = \deg(R) \leq \deg(P') < \deg(P)$, a contradiction.
Thus $P$ and $P'$ are relatively prime, and we are in case (1).
```

## MC-STK-ERR-1886 — FIELDS-RECON-034 (source_correction)

A nonconstant common factor over E contradicts the Bezout identity for the separable polynomial P over F. Explicitly transport that unchanged identity by F[x] -> E[x], then apply the dichotomy to Q over its actual coefficient field E.

Official fields.tex line 1202:

```tex
hence $P' = 0$ by the lemma. This proves (1). Part (2)
```

Replace with:

```tex
in $E[x]$. Since $P$ is separable over $F$, there are
$A, B \in F[x]$ such that $AP + BP' = 1$. The same identity
holds in $E[x]$, so the nonconstant polynomial $Q$ would divide $1$,
a contradiction. Hence $Q' \not = 0$; as $Q$ is irreducible over $E$,
the lemma shows that $Q$ is separable. This proves (1). Part (2)
```

## MC-STK-ERR-1887 — FIELDS-RECON-037 (source_correction)

The definition allows only the identity purely inseparable extension in characteristic zero. Treat its elements first, then use the given p-power identities only in positive characteristic.

Official fields.tex line 1658:

```tex
Let $p$ be the characteristic of $k$.
```

Replace with:

```tex
In characteristic zero the elements in question are exactly those of $k$,
so the assertion follows. Assume henceforth that the characteristic of $k$
is a prime $p > 0$.
```

## MC-STK-ERR-1888 — FIELDS-RECON-038 (source_correction)

The cited irreducible-polynomial lemma gives a separable irreducible polynomial P; algebraic is a property of the field element, not the missing polynomial description.

Official fields.tex line 1721:

```tex
with $P$ separable algebraic
```

Replace with:

```tex
with $P$ a separable irreducible polynomial
```

## MC-STK-ERR-1889 — FIELDS-RECON-041 (source_correction)

A nonempty family supplies a member in which the minimal polynomial splits. The displayed complete proof puts each root, with its original multiplicity, into every member and hence into the intersection.

Official fields.tex line 1853:

```tex
$M/E_i/F$, $i \in I$ be subextensions with
```

Replace with:

```tex
$M/E_i/F$, $i \in I$, be a nonempty family of subextensions with
```

Official fields.tex line 1858:

```tex
Direct from the definitions.
```

Replace with:

```tex
Put $E = \bigcap_{i \in I} E_i$. Intersections of subfields of $M$
are subfields, and $E$ contains $F$ and is algebraic over $F$.
For $\alpha \in E$, let $P \in F[x]$ be its minimal polynomial.
Choose $i_0 \in I$. Normality of $E_{i_0}/F$ gives a factorization
$P = c\prod_{j=1}^d(x-\alpha_j)$ with $c \in F^*$ and
$\alpha_j \in E_{i_0} \subset M$, retaining multiplicities.
For every $i \in I$, the same polynomial splits over $E_i$ because
$\alpha \in E_i$. Each $\alpha_j$ is then a root of that factorization
in the field $M$, so $\alpha_j$ is one of its roots in $E_i$.
Thus every $\alpha_j$ lies in every $E_i$, and the displayed
factorization lies in $E[x]$. This proves that $E/F$ is normal.
```

## MC-STK-ERR-1890 — FIELDS-RECON-043 (copyedit)

Insert the missing preposition naming the field whose normal closure is taken.

Official fields.tex line 2127:

```tex
normal closure $E$ over $F$
```

Replace with:

```tex
normal closure of $E$ over $F$
```

## MC-STK-ERR-1891 — FIELDS-RECON-044 (source_correction)

Treat the trivial group before choosing a first nontrivial invariant factor. For nontrivial A, exponent dividing n implies e_1 divides n; the hypothesis at d=e_1 gives e_1^r <= e_1, hence r=1 since e_1>1. Its order e_1 then divides n.

Official fields.tex line 2241:

```tex
The structure of finite abelian groups shows that
```

Replace with:

```tex
If $A = 0$, then $A$ is cyclic of order $1$, which divides $n$.
Suppose $A \not = 0$. The structure of finite abelian groups shows that
```

## MC-STK-ERR-1892 — FIELDS-RECON-047 (source_correction)

Restrict the quotient to a nonzero denominator. For q double prime at least both p-powers, alpha^q double prime and beta^q double prime lie in k; the latter is nonzero, so their quotient also lies in k.

Official fields.tex line 1665:

```tex
product and quotient of $\alpha$ and $\beta$.
```

Replace with:

```tex
product and, when $\beta \not = 0$, the quotient of $\alpha$ by $\beta$.
```

## MC-STK-ERR-1893 — FIELDS-RECON-048 (clarification)

Separate the characteristic-zero identity case before invoking the finite purely inseparable tower lemma, whose hypothesis explicitly requires p>0.

Official fields.tex line 1757:

```tex
We first prove this when $K/F$ is purely inseparable. Namely, we claim that
```

Replace with:

```tex
We first prove this when $K/F$ is purely inseparable. In characteristic
zero, $K = F$ and both sides of the asserted equality are $1$.
Assume for this paragraph that the characteristic is a prime $p > 0$.
Namely, we claim that
```

## MC-STK-ERR-1894 — FIELDS-RECON-049 (source_correction)

The extension, minimal polynomial and algebraic closure in the proof all have base K. Restore that same base in the separability assertion.

Official fields.tex line 2576:

```tex
Since $L/k$ is separable
```

Replace with:

```tex
Since $L/K$ is separable
```

## MC-STK-ERR-1895 — FIELDS-RECON-051 (source_correction)

The orbit polynomial has coefficients in K^G, and K=K^G(alpha). Its degree bounds the degree of alpha over K^G, which is [K:K^G].

Official fields.tex line 2777:

```tex
over $K$. However, the
```

Replace with:

```tex
over $K^G$. However, the
```

## MC-STK-ERR-1896 — FIELDS-RECON-052 (source_correction)

The primitive element in this paragraph generates K over K^G; L was the auxiliary finite subfield in the preceding reduction.

Official fields.tex line 2779:

```tex
$K^G(\alpha) = L$
```

Replace with:

```tex
$K^G(\alpha) = K$
```

## MC-STK-ERR-1897 — FIELDS-RECON-054 (source_correction)

Bind s to every element of the finite set S. Equality of restrictions c(h)=c(g) on E then proves h belongs to the displayed neighbourhood since S is contained in E.

Official fields.tex line 3098:

```tex
$U_S(g) = \{g' \in G \mid g'(s) = g(s)\}$
```

Replace with:

```tex
$U_S(g) = \{g' \in G \mid g'(s) = g(s)\text{ for all }s\in S\}$
```

## MC-STK-ERR-1898 — FIELDS-RECON-056 (copyedit)

Use the same compound noun as the definition and the proof below.

Official fields.tex line 3284:

```tex
any sub extension
```

Replace with:

```tex
any subextension
```

## MC-STK-ERR-1899 — FIELDS-RECON-057 (source_correction)

Each of the d factors contributes -zeta_i alpha to the constant term. Retain (-1)^d in that equality and in the solved expression for alpha^d. Treat e=1 first so the later division by alpha^d is defined in the remaining case. Since zeta is a product of eth roots it is itself an eth root in L and hence in K.

Official fields.tex line 3288:

```tex
Observe that for $d | e$ the subfield
```

Replace with:

```tex
If $e=1$, then $L=L'=K=K(\alpha)$ and the assertion holds with
$d=1$. Assume $e>1$. Since $L=K(\alpha)$ has degree $e$, we have
$\alpha\not =0$. Observe that for $d | e$ the subfield
```

Official fields.tex line 3305:

```tex
c = (\prod\nolimits_{i = 1, \ldots, d} \zeta_i) \alpha^d
```

Replace with:

```tex
c = (-1)^d (\prod\nolimits_{i = 1, \ldots, d} \zeta_i) \alpha^d
```

Official fields.tex line 3309:

```tex
$\alpha^d = \zeta^{-1}c \in L'$
```

Replace with:

```tex
$\alpha^d = (-1)^d\zeta^{-1}c \in L'$
```

## MC-STK-ERR-1900 — FIELDS-RECON-059 (clarification)

Specify and prove the canonical multiplication map. The complete proof identifies the fixed field as the purely inseparable elements, proves the Galois upper extension and compositum equality, and proves linear disjointness through finite separable subextensions without assuming the original extension finite.

Official fields.tex line 3674:

```tex
\item $E = E_{sep} \otimes_F E_{insep}$.
```

Replace with:

```tex
\item multiplication induces an isomorphism of $F$-algebras
$E_{sep}\otimes_F E_{insep}\longrightarrow E$,
$\sum_i a_i\otimes b_i\longmapsto\sum_i a_i b_i$.
```

Official fields.tex line 3679:

```tex
We found the subfield $E_{sep}$ in Lemma \ref{lemma-separable-first}.
We set $E_{insep} = E^{\text{Aut}(E/F)}$. Details omitted.
```

Replace with:

```tex
Put $S = E_{sep}$, as constructed in Lemma \ref{lemma-separable-first},
and put $G = \text{Aut}(E/F)$ and $N = E^G$.
The extension $S/F$ is separable and $E/S$ is purely inseparable.
Moreover, $S/F$ is normal by Lemma \ref{lemma-separable-first-normal},
so $S/F$ is Galois. We will take $E_{insep} = N$.

\medskip\noindent
We first show that $N/F$ is purely inseparable. Let $a \in N$ and let
$f \in F[T]$ be its monic minimal polynomial. Since $E/F$ is normal,
every root $b$ of $f$ in an algebraic closure of $E$ belongs to $E$.
The map $F(a) \to E$ sending $a$ to $b$ is an $F$-embedding:
it is the map induced by evaluation at $b$ on $F[T]/(f)$.
By Lemma \ref{lemma-lift-maps} it extends to an element $g \in G$.
Thus $b = g(a) = a$. Consequently $f$ has just one distinct root.
In characteristic zero, $f$ is separable, so $\deg(f) = 1$ and $a \in F$.
In characteristic $p > 0$, Lemma \ref{lemma-irreducible-polynomials}
gives $f(T) = h(T^q)$ for $q = p^r$, $r \geq 0$, and a monic
separable irreducible polynomial $h \in F[T]$.
The map $x \mapsto x^q$ is bijective on an algebraically closed field:
existence follows by taking a root of $T^q-c$, and uniqueness follows
from $x^q-y^q=(x-y)^q$. Therefore $h$ has just one distinct root.
Since $h$ is separable and monic, $h(T)=T-c$ for some $c \in F$.
Hence $a^q=c \in F$. This proves the assertion in every characteristic.
Conversely, if $a \in E$ is purely inseparable over $F$, then every
$g \in G$ fixes $a$: in characteristic $p>0$, choose $q=p^r$ with
$a^q\in F$ and use $(g(a)-a)^q=g(a^q)-a^q=0$; in characteristic
zero the relevant elements already lie in $F$.
Thus $N$ consists exactly of the elements of $E$ purely inseparable
over $F$.

\medskip\noindent
The extension $E/N$ is normal by Lemma \ref{lemma-normal-goes-up}.
To prove separability, let $a \in E$. The orbit $G\cdot a$ is finite,
since its elements are roots of the minimal polynomial of $a$ over $F$.
The polynomial
$$
P_a(T)=\prod_{b\in G\cdot a}(T-b)
$$
has coefficients in $N$, since every element of $G$ permutes its factors.
Its roots are distinct, and the minimal polynomial of $a$ over $N$
divides $P_a$. Thus $a$ is separable over $N$. As $E/N$ is algebraic,
normal and separable, it is Galois.

\medskip\noindent
Let $C=SN$ be the compositum inside $E$. Since $E/N$ is separable,
so is $E/C$ by Lemma \ref{lemma-separable-goes-up}. Since $E/S$
is purely inseparable, $E/C$ is purely inseparable as well.
In characteristic zero, $E=S\subset C$. In characteristic $p>0$,
for each $a\in E$ choose $q=p^r$ with $a^q\in S\subset C$.
The minimal polynomial of $a$ over $C$ is separable and divides
$T^q-a^q=(T-a)^q$ in $E[T]$. It therefore has degree one, so $a\in C$.
It follows that $E=C=SN$.

\medskip\noindent
Multiplication in $E$ is $F$-balanced and defines the $F$-algebra map
$$
\mu:S\otimes_F N\longrightarrow E,\qquad
\sum_i s_i\otimes n_i\longmapsto\sum_i s_i n_i.
$$
Its image is a subring of the algebraic extension $E/F$ containing $F$,
and is therefore a field by Lemma \ref{lemma-subalgebra-algebraic-extension-field}.
The image contains both $S$ and $N$, so it contains $SN=E$.
Thus $\mu$ is surjective.

\medskip\noindent
It remains to prove injectivity. In characteristic zero, $N=F$ and
the inverse of $\mu$ is $a\mapsto a\otimes 1$.
Assume the characteristic is $p>0$. Let $L/F$ be any finite
subextension of $S/F$. By Lemma \ref{lemma-primitive-element},
write $L=F(\theta)$. Let $f\in F[T]$ be the monic minimal polynomial
of $\theta$ over $F$, and let $g\in N[T]$ be its monic minimal
polynomial over $N$. Then $g$ divides $f$ in $N[T]$.
Write $g(T)=\sum_{i=0}^d b_iT^i$, with $b_d=1$.
Since $N/F$ is purely inseparable and this list of coefficients is finite,
there is one $q=p^r$ such that every $b_i^q$ belongs to $F$. Hence
$$
g(T)^q=\sum_{i=0}^d b_i^q T^{iq}\in F[T].
$$
This polynomial vanishes at $\theta$, so $f$ divides $g^q$ in $F[T]$.
Separability of $f$ gives $A,B\in F[T]$ with $Af+Bf'=1$.
This identity also holds in $N[T]$, so $f$ is squarefree in $N[T]$.
Every irreducible factor of $f$ in $N[T]$ divides $g^q$, hence divides $g$.
Since those factors occur in $f$ with multiplicity one, $f$ divides $g$.
The two monic polynomials $f$ and $g$ therefore coincide.

\medskip\noindent
For completeness the corresponding tensor-product map is explicit.
Write $m=\deg(f)$, so $1,\theta,\ldots,\theta^{m-1}$ is an $F$-basis of $L$.
The map $L\otimes_F N\longrightarrow N[T]/(f)$ given by
$$
\left(\sum_{j=0}^{m-1}a_j\theta^j\right)\otimes n
\longmapsto\left[\sum_{j=0}^{m-1}a_j n T^j\right]
$$
and $[\sum_j c_jT^j]\mapsto\sum_j\theta^j\otimes c_j$
are mutually inverse algebra maps. The first respects products by reduction
modulo $f$; the second is well defined because $f(\theta)=0$.
Evaluation $N[T]/(f)\to N(\theta)=LN$ is an isomorphism, since $f=g$
is the minimal polynomial over $N$. Their composite is multiplication
$L\otimes_F N\to LN\subset E$, which is consequently injective.
Every element $z\in S\otimes_F N$ is a finite sum $\sum_i s_i\otimes n_i$.
The field $L=F(s_1,\ldots,s_t)\subset S$ is a finite separable extension
of $F$. Let $z_L=\sum_i s_i\otimes n_i\in L\otimes_F N$.
If $\mu(z)=0$, then multiplication sends $z_L$ to zero in $E$;
the injectivity just proved gives $z_L=0$, and its image $z$ is zero.
Thus $\mu$ is injective and hence an isomorphism, as claimed.
```

## MC-STK-ERR-1901 — FIELDS-RECON-060 (copyedit)

Insert the missing preposition in the introduction of the minimal polynomial.

Official fields.tex line 3702:

```tex
is algebraic over $k$. Denote
```

Replace with:

```tex
is algebraic over $k$. Denote by
```

## MC-STK-ERR-1902 — FIELDS-RECON-061 (copyedit)

Give the greater-than relation its explicit left operand p.

Official fields.tex line 3716:

```tex
characteristic $p$ of $k$ is $ > 0$
```

Replace with:

```tex
characteristic $p$ of $k$ satisfies $p > 0$
```

## MC-STK-ERR-1903 — FIELDS-RECON-062 (clarification)

The definition of Galois requires normality in addition to algebraicity and separability. The same orbit polynomial supplies it: each minimal polynomial divides a product of linear factors already in K[x].

Official fields.tex line 2753:

```tex
we conclude that $K/K^G$ is separable. Thus $K/K^G$ is Galois.
```

Replace with:

```tex
we conclude that $K/K^G$ is separable. Also, $Q$ divides the displayed
polynomial $P$, which splits completely over $K$, so $Q$ splits over $K$.
Thus $K/K^G$ is normal as well, and hence Galois.
```

## MC-STK-ERR-1904 — FIELDS-RECON-063 (source_correction)

Restore the identity-extension case explicitly included in definition-purely-inseparable at lines 1589-1592, which allows k prime=k in every characteristic.

Official fields.tex line 3731:

```tex
extension $k'/k$ is called {\it purely inseparable} if
the characteristic of $k$ is $p > 0$ and for every element
```

Replace with:

```tex
extension $k'/k$ is called {\it purely inseparable} if $k'=k$, or if
the characteristic of $k$ is $p > 0$ and for every element
```

## MC-STK-ERR-1905 — FIELDS-RECON-064 (clarification)

The first paragraph of the original proof establishes the stronger extension property with prescribed independent A and generating G. Make that already-proved generality visible in the statement. For Zorn, the empty chain has upper bound A; a nonempty chain has union containing A and every finite polynomial relation occurs in one member. Maximality forces each generator algebraic over F(B), hence E algebraic over F(B).

Official fields.tex line 3399:

```tex
Let $E/F$ be a field extension. A transcendence basis of $E$ over $F$ exists.
Any two transcendence bases have the same cardinality.
```

Replace with:

```tex
Let $E/F$ be a field extension. A transcendence basis of $E$ over $F$ exists.
More precisely, if $A\subset G\subset E$, $A$ is algebraically independent
over $F$, and $G$ generates $E/F$, then there is a transcendence basis $B$
with $A\subset B\subset G$.
Any two transcendence bases have the same cardinality.
```

Official fields.tex line 3411:

```tex
The union of the elements of a totally ordered subset $T$ of $\mathcal{B}$
```

Replace with:

```tex
The empty chain has upper bound $A\in\mathcal{B}$.
The union of the elements of a nonempty totally ordered subset $T$ of $\mathcal{B}$
```
