# Homomorphisms, fibre dimensions and the dimension formula

Primary authority: `algebra.tex` 27305–27647 at commit
`a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256
`FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`.
The entire current interval is byte-identical to this authority. No earlier
canonical operation or added environment occurs in it.

These are source-linked editorial arguments. Both translation branches retain
the source's statements and exposition; none of the expanded proofs below is
a replacement translation. Proposed minimal corrections retain their old
readings in the review ledger. Further consequences are not novelty claims.

## Chains, integral maps and the original fibre rings

Source 27312–27388. Write the ring map as \(\varphi:R\to S\).
For a finite strict chain \(\mathfrak p_0\subsetneq\cdots\subsetneq
\mathfrak p_e\), surjectivity on spectra supplies a prime over the first
endpoint for going up, or the last endpoint for going down. Apply the
respective lifting property successively. Every lifted inclusion is strict,
since its contractions are distinct. Taking the supremum of these finite
lengths proves the dimension inequality, also when the supremum is infinite.
If \(R=0\), a unital map forces \(S=0\); both spectra are empty. If \(R\ne0\),
surjectivity rules out an empty target spectrum.

If \(\mathfrak q\) is maximal and contracts to \(\mathfrak p\), every prime
\(\mathfrak p'\supset\mathfrak p\) lifts by going up to
\(\mathfrak q'\supset\mathfrak q\). Maximality gives
\(\mathfrak q'=\mathfrak q\), hence \(\mathfrak p'=\mathfrak p\).
This proves the assertion labelled "Trivial" in the source. OCC-12242 and
OCC-00536 concern only its broken if/then punctuation.

For an integral map, incomparability makes contractions of any strict chain
in \(S\) strict in \(R\), giving \(\dim S\leq\dim R\); going up gives the
closed-point conclusion. More exactly, let \(K=\ker\varphi\). The original
map factors through the injection \(R/K\to S\). Integrality and lying over
give surjectivity \(\operatorname{Spec}S\to\operatorname{Spec}(R/K)\), and
the two chain arguments prove \(\dim S=\dim(R/K)\). The prime correspondence
is inverse image under \(R\to R/K\); it preserves every inclusion. The source
inclusion \(R\subset S\) is the case \(K=0\). If \(S=0\), then \(K=R\) and
both spectra in the equality are empty. No nonzero-ring convention has
silently replaced this case.

Fix \(\mathfrak q\in\operatorname{Spec}S\) and
\(\mathfrak p=\varphi^{-1}\mathfrak q\). Put
\(A=R_{\mathfrak p}\), \(B=S_{\mathfrak q}\),
\(\mathfrak m=\mathfrak pA\), and \(\mathfrak n=\mathfrak qB\).
The map is explicitly \(r/u\mapsto\varphi(r)/\varphi(u)\); its denominator
is a unit because \(u\notin\mathfrak p\). Put
\(C=S\otimes_R\kappa(\mathfrak p)\).
First \(C=(R\setminus\mathfrak p)^{-1}(S/\mathfrak pS)\) by
\(s\otimes(\bar r/\bar u)\mapsto\overline{s\varphi(r)}/\bar u\).
Its inverse takes \(\bar s/\bar u\) to \(s\otimes1/\bar u\).
The prime induced by \(\mathfrak q\) is
\(\tilde{\mathfrak q}=(R\setminus\mathfrak p)^{-1}
(\mathfrak q/\mathfrak pS)\). There are inverse maps
\[
 B/\mathfrak pB\longleftrightarrow C_{\tilde{\mathfrak q}},
 \qquad
 [s/t]\longmapsto(s\otimes1)/(t\otimes1),\quad t\notin\mathfrak q.
\]
To describe the reverse map, \(s\otimes(\bar r/\bar u)\) maps to
\([s\varphi(r)/\varphi(u)]\). An element \(\bar s/\bar u\) outside
\(\tilde{\mathfrak q}\) has \(s\notin\mathfrak q\), so its image is invertible.
The localization universal property therefore supplies the reverse map;
both composites fix the original numerators and every inverted denominator.
The comparison with \((S/\mathfrak pS)_{\mathfrak q/\mathfrak pS}\)
uses the same \([s/t]\). This proves all displayed fibre identifications
without discarding their prime labels.

## The parameter bound and the zero-length going-down case

Source 27390–27456. For the original Noetherian local \(A,B\), put
\(d=\dim A\), \(e=\dim(B/\mathfrak mB)\). Choose parameters \(x_1,\ldots,x_d\)
in \(A\) and lifted fibre parameters \(y_1,\ldots,y_e\) in \(B\).
The source chooses representatives in \(R,S\); this is possible by clearing
each localization denominator, which is a unit in the respective local ring.
Multiplying a parameter by that unit does not change its generated ideal.

Here is the claimed nilpotence explicitly. There are positive integers \(a,b\)
such that
\[
 \mathfrak m^a\subset(x_1,\ldots,x_d)A,\qquad
 \mathfrak n^b\subset\mathfrak mB+(y_1,\ldots,y_e)B.
\]
The first follows from the ideal of definition, the second from the fibre
ideal of definition. With \(J=(\varphi(x_1),\ldots,\varphi(x_d),
y_1,\ldots,y_e)B\), the image of \(\mathfrak mB\) in \(B/J\) has \(a\)-th
power zero. The second inclusion therefore gives
\(\mathfrak n^{ab}\subset J\). Thus \(J\) is an ideal of definition generated
by \(d+e\) elements, proving \(\dim B\leq d+e\). Empty parameter sequences,
including \(d=0\) or \(e=0\), obey exactly the same ideal calculation.

For the reverse inequality assume going down. In the source's indexing choose
\[
 \mathfrak pS\subset\mathfrak q_0\subsetneq\cdots
 \subsetneq\mathfrak q_d=\mathfrak q,\qquad
 \mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_e=\mathfrak p,
\]
where now \(d=\dim(B/\mathfrak pB)\) and \(e=\dim A\), exactly as at
27442–27447. Every \(\mathfrak q_i\) contracts to \(\mathfrak p\):
it contains \(\mathfrak pS\) and is contained in \(\mathfrak q\).
If \(e=0\), the existing fibre chain already has length \(d+e\).
If \(e\geq1\), use going down \(e\) times to obtain
\(\mathfrak q_{-j}\) over \(\mathfrak p_{e-j}\), \(1\leq j\leq e\).
Each new inclusion is strict by contraction. The concatenation has length
\(d+e\). This proves equality and resolves OCC-12243 in a separate proof
clarification, without rewriting the source's exposition.

There are two precise extensions of these calculations. For arbitrary rings
and a fixed prime \(\mathfrak q\), going down alone gives the lower bound
\[
 \dim S_{\mathfrak q}\ \geq\
 \dim R_{\mathfrak p}+\dim(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q})
\]
in the extended nonnegative integers: concatenate arbitrary finite chains as
above; if either dimension is infinite, their finite lengths are unbounded.
All these local spectra are nonempty, so no undefined sum with
\(-\infty\) occurs. No Noetherian hypothesis enters this bound.

For the upper bound, \(A\) need not be Noetherian. It suffices that \(B\) is
Noetherian local and that there are \(c\) actual elements
\(x_1,\ldots,x_c\in\mathfrak m\) with
\(\sqrt{(x_1,\ldots,x_c)A}=\mathfrak m\).
Then \(\mathfrak mB\subset\sqrt{(x_1,\ldots,x_c)B}\): for every \(z\in
\mathfrak m\), an actual positive power of \(z\) lies in the ideal in \(A\).
Choose \(e=\dim B/\mathfrak mB\) fibre parameters. Every prime of \(B\)
containing their lifts and the \(x_i\) contains \(\mathfrak mB\), and hence is
\(\mathfrak n\). Thus the lifted \(c+e\) elements generate an ideal of
definition and \(\dim B\leq c+e\). This argument does not assume a uniform
power of \(\mathfrak m\) in non-Noetherian \(A\). If \(c=\dim A<\infty\)
and going down holds, the upper and lower bounds give equality.

## Regular ascent under going down and the resulting flatness

Source 27458–27480. Suppose \(R\to S\) is a local map of Noetherian local
rings, \(R\) is regular, and \(S/\mathfrak m_RS\) is regular.
Put \(d=\dim R\), \(e=\dim(S/\mathfrak m_RS)\).
Choose the original \(d\) generators \(x_i\) of \(\mathfrak m_R\) and lift
the original \(e\) generators \(y_j\) of the fibre maximal ideal. Then
\[
 \mathfrak m_S=(\varphi(x_1),\ldots,\varphi(x_d),y_1,\ldots,y_e)S.
\]
Indeed, reducing an element of \(\mathfrak m_S\) modulo \(\mathfrak m_RS\)
expresses it in the \(\bar y_j\); subtracting the lifts leaves an element of
\(\mathfrak m_RS\), which is generated by the displayed \(\varphi(x_i)\).

The following three conditions are equivalent under these hypotheses:
the map is flat; it has going down; and
\(\dim S=d+e\). Flatness gives going down and the preceding chain argument
gives the dimension equality. Conversely, if the equality holds, the
displayed generating set shows that the embedding dimension of \(S\) is
at most \(\dim S\). The reverse inequality follows from the ideal-of-definition
bound. Thus \(S\) is regular and this generating set is a regular system of
parameters. Regular local rings are Cohen–Macaulay, so the ordered sequence
\(\varphi(x_1),\ldots,\varphi(x_d),y_1,\ldots,y_e\) is regular. In particular
the initial \(d\) elements are regular on \(S\).

For completeness the flatness implication uses the original rings and their
successive quotients. Put \(R_i=R/(x_1,\ldots,x_i)\) and
\(S_i=S/(\varphi(x_1),\ldots,\varphi(x_i))S\).
Then \(R_d=\kappa(R)\), so \(S_d\) is \(R_d\)-flat. Working backwards from
\(i=d\) to \(i=1\), multiplication by \(x_i\) is injective on \(R_{i-1}\),
and multiplication by \(\varphi(x_i)\) is injective on \(S_{i-1}\).
The exact two-term free resolution of \(R_i\) over \(R_{i-1}\) therefore
gives
\(\operatorname{Tor}_1^{R_{i-1}}(S_{i-1},R_i)=0\).
The local criterion at authority 23750–23805, with \(M=S_{i-1}\) finite
over itself, lifts flatness of \(S_i\) to \(S_{i-1}\).
This reaches \(R\to S\). Every ideal used is proper because the maps are
local. If \(d=0\), \(R\) is already a field and the backwards induction is
empty. This also proves the result for \(e=0\).

Thus the source's flatness hypothesis can be weakened to going down,
and flatness is recovered as a conclusion. This agrees with the later
regular-parameter flatness proof at 32693–32715, read in full as a bounded
receiving comparison. Reading that later passage does not adjudicate its
received reports or advance the source-order cursor past it.

## Cohen–Macaulay ascent with an arbitrary Cohen–Macaulay fibre

Source 27482–27503. The received copula correction OCC-12244 is accepted.
The original finite-flat case is justified as follows. A flat local map is
faithfully flat, hence injective. Finiteness implies integrality, so the
integral dimension equality gives \(\dim S=\dim R=d\). A length-\(d\)
regular sequence in \(R\) stays regular on \(S\): flatness preserves each
multiplication injection after quotienting, and the final quotient is
nonzero by faithful flatness (or by locality and Nakayama).
In the other source case going down gives \(\dim S\geq d\), while the stated
hypothesis gives the reverse inequality. In both cases
\(d\leq\operatorname{depth}S\leq\dim S=d\), proving the assertion.

More generally, let \(R\to S\) be flat local between Noetherian local rings.
If \(R\) and \(F=S/\mathfrak m_RS\) are Cohen–Macaulay, then \(S\) is
Cohen–Macaulay and
\(\dim S=\dim R+\dim F\), without assuming \(\dim F=0\).
Here is the complete regular-sequence argument. Put \(d=\dim R\),
\(e=\dim F\). Choose a system of parameters \(x_1,\ldots,x_d\) of \(R\),
which is regular since \(R\) is Cohen–Macaulay.
Flatness makes its image an \(S\)-regular sequence. Put
\(A=R/(x_1,\ldots,x_d)\) and \(Q=S/(x_1,\ldots,x_d)S\).
Base change gives \(Q\) flat over \(A\), and its residue fibre is the
original \(F\). Choose fibre parameters \(\bar y_1,\ldots,\bar y_e\),
which form an \(F\)-regular sequence, and take lifts \(y_j\) in \(Q\).

For \(Q_j=Q/(y_1,\ldots,y_j)Q\), begin with the \(A\)-flat \(Q_0=Q\).
Multiplication by \(y_j\) on \(Q_{j-1}\) is injective after tensoring with
\(\kappa(A)\), by the original regular sequence on \(F\).
The proved injection-modulo-the-maximal-ideal lemma applies with the
Noetherian local auxiliary ring \(Q\) and finite modules \(Q_{j-1}\).
It proves that multiplication is injective and \(Q_j\) is \(A\)-flat.
Induction proves the entire lifted sequence regular. Its final quotient
surjects onto the nonzero \(F/(\bar y_1,\ldots,\bar y_e)\), so the nonzero
condition is retained at every step. Thus
\(x_1,\ldots,x_d,y_1,\ldots,y_e\) is \(S\)-regular.
The dimension equality already proved gives \(\dim S=d+e\); the depth
inequality gives the opposite bound to the constructed sequence, proving
that \(S\) is Cohen–Macaulay.

This receives group 559's exact module and quotient maps, in
ALGEBRA_FLATNESS_CRITERIA_NOTES_20260928.md, section "Removing the unused
base Noetherian hypothesis". The auxiliary ring remains Noetherian and the
module finite as required. The construction works with either empty sequence.
The source lemma is the case of zero-dimensional fibre, which is automatically
Cohen–Macaulay as a nonzero zero-dimensional Noetherian local ring.
No converse about arbitrary fibres has been assumed.

## The dimension formula with the original tower and height-one prime

Source 27519–27596. Let \(R\subset S\) be the stated finite-type extension
of domains with \(R\) Noetherian, and retain \(\mathfrak p,\mathfrak q\).
All heights here are finite, since the corresponding local rings are
Noetherian. For \(R\subset S'\subset S\), where \(S'\) is generated by an
initial part of the fixed generator list, put
\(\mathfrak q'=\mathfrak q\cap S'\). Write
\[
 g_1=\operatorname{trdeg}_{\operatorname{Frac}R}\operatorname{Frac}S',
 \quad g_2=\operatorname{trdeg}_{\operatorname{Frac}S'}\operatorname{Frac}S,
 \quad t_1=\operatorname{trdeg}_{\kappa(\mathfrak p)}\kappa(\mathfrak q'),
 \quad t_2=\operatorname{trdeg}_{\kappa(\mathfrak q')}\kappa(\mathfrak q).
\]
Adding the two inequalities gives
\[
 \operatorname{ht}\mathfrak q\leq
 \operatorname{ht}\mathfrak q'+g_2-t_2\leq
 \operatorname{ht}\mathfrak p+g_1+g_2-t_1-t_2.
\]
Field-tower additivity identifies both sums with those in the source formula.
If \(R\) is universally catenary, each finite-type \(S'\) is universally
catenary: every finite-type \(S'\)-algebra is finite type over \(R\).
Consequently both inductive equalities are justified.

For the one-generator polynomial case, put \(T=R[x]\) and
\(\mathfrak r=\mathfrak pT\). The original fibre is
\(\kappa(\mathfrak p)[x]\).
A prime over \(\mathfrak p\) corresponds either to its zero prime, exactly
when it equals \(\mathfrak r\), or to an ideal generated by a nonconstant
irreducible polynomial. In the first case its residue field is
\(\kappa(\mathfrak p)(x)\), of transcendence degree one, and the local fibre
has dimension zero. In the second case its residue field is a finite
algebraic extension and the local fibre is a one-dimensional discrete
valuation ring: ideals in the PID \(\kappa(\mathfrak p)[x]\) are principal,
and the primes below that nonzero prime are just zero and itself.
Flatness and the preceding dimension equality prove the source formula
with equality in both cases.

For the algebraic case \(S=R[x]/\mathfrak n\), \(\mathfrak n\) is a
nonzero prime with \(\mathfrak n\cap R=0\). Let
\(F=\operatorname{Frac}R\). Localization at \(R\setminus\{0\}\) gives a
nonzero prime \(\mathfrak nF[x]\): a nonzero polynomial of \(\mathfrak n\)
stays nonzero because \(R[x]\) is a domain. The polynomial relation also
shows that the image of \(x\) is algebraic over \(F\), so the generic
transcendence degree is zero. Every prime below \(\mathfrak n\) is disjoint
from \(R\setminus\{0\}\). The localization bijection therefore preserves
the entire interval \([0,\mathfrak n]\), whose length is one since \(F[x]\)
is a PID. In particular \(\operatorname{ht}\mathfrak n=1\), without
assuming catenarity.

Let \(\mathfrak q'\) be the preimage of \(\mathfrak q\) and put
\(C=R[x]_{\mathfrak q'}\). Quotient and localization give the exact
isomorphism
\[
 C/\mathfrak nC\longrightarrow S_{\mathfrak q},\qquad
 [(f/g)]\longmapsto \bar f/\bar g
\]
with inverse given by any polynomial representatives; two choices differ
by the localized kernel. The residue fields at \(\mathfrak q'\) and
\(\mathfrak q\) are thereby the same. Every chain in \(C/\mathfrak nC\)
extends by \(0\subsetneq\mathfrak nC\), so
\(\dim(C/\mathfrak nC)\leq\dim C-1\).
The already proved polynomial formula supplies
\(\dim C=\operatorname{ht}\mathfrak p+1-
\operatorname{trdeg}_{\kappa(\mathfrak p)}\kappa(\mathfrak q)\).
This proves the inequality. If \(C\) is catenary, every saturated chain
from \(\mathfrak nC\) to its maximal ideal, extended by this same
height-one interval, has length \(\dim C\). Hence the quotient dimension
is exactly \(\dim C-1\). Universal catenarity of \(R\) implies the required
catenarity of \(C\), proving the source equality.

OCC-00537 is the missing "by" in the prime declaration and is accepted.
OCC-00538 overstates a stylistic preference: "in case R is ..." is a valid
conditional construction. OCC-00539 likewise proposes a smoother order of
modifiers but the existing comparison is intelligible and mathematically
correct: append \(0\subsetneq\mathfrak n\) to the quotient chain.
Both optional rewrites remain unapplied; they are not counted as defects.

## Essential finite type, local catenarity and the full codimension-one fibre

The dimension formula above extends as follows. Suppose \(R\) is a
Noetherian domain and \(S=T^{-1}B\), where \(R\subset B\) is a finite-type
domain and \(S\ne0\). For \(\mathfrak q\in\operatorname{Spec}S\), let
\(\mathfrak q_0\) be its contraction to \(B\). Every prime below
\(\mathfrak q_0\) is disjoint from \(T\). Thus localization identifies
the entire interval below \(\mathfrak q_0\) with the interval below
\(\mathfrak q\), preserving height. It also gives the explicit isomorphism
\(B_{\mathfrak q_0}\simeq S_{\mathfrak q}\) by the unchanged fractions.
Fraction fields and residue fields are unchanged. Applying the preceding
formula to \(R\subset B\) proves it for \(R\subset S\).

For equality it suffices that \(R_{\mathfrak p}\) is universally catenary.
Indeed apply the finite-type formula after localization at
\(R\setminus\mathfrak p\). Every prime below \(\mathfrak p\) and below
\(\mathfrak q_0\) survives this localization, so both heights, both fraction
fields and both residue fields in the formula retain their original
values. The localized finite-type algebra is over the stipulated
universally catenary ring \(R_{\mathfrak p}\). This proves equality without
requiring universal catenarity away from \(\mathfrak p\).
This is a sufficient local hypothesis; no necessity claim is made.

Now retain the source's generically finite extension \(A\subset B\), and
allow \(B\) essentially of finite type. Let
\(\operatorname{ht}\mathfrak p=1\). For each prime \(\mathfrak q\) above it,
the dimension formula and generic transcendence degree zero give
\[
 1\leq\operatorname{ht}\mathfrak q
 \leq1-\operatorname{trdeg}_{\kappa(\mathfrak p)}\kappa(\mathfrak q).
\]
The first inequality uses a nonzero \(a\in\mathfrak p\), whose image is
nonzero in the domain \(B\) and belongs to \(\mathfrak q\); thus
\(0\subsetneq\mathfrak q\). Hence \(\operatorname{ht}\mathfrak q=1\)
and the residue transcendence degree is zero.
Put \(D=B\otimes_A\kappa(\mathfrak p)\). It is an essentially finite-type
Noetherian algebra over the field \(\kappa(\mathfrak p)\).
Every residue field at a prime of \(D\) is a finite extension of that field:
represent \(B\) by a finite-type algebra before localization, retain the
same residue field, and use that an algebraic finitely generated field
extension is finite. Each corresponding prime of that finite-type field
algebra is maximal by the field-algebra lemma, so each prime of \(D\)
is maximal. There are finitely many of them by the corrected spectrum
argument in the next section.

In fact the entire fibre algebra \(D\), including its nilpotents, is finite
dimensional over \(\kappa(\mathfrak p)\).
If \(D=0\), this is immediate and there is no fibre point.
Otherwise its nilradical \(J\) is finitely generated, say by nilpotent
elements \(z_1,\ldots,z_t\), with \(z_i^{a_i}=0\).
Every monomial of total degree
\(N=1+\sum_i(a_i-1)\) contains such a zero factor, so \(J^N=0\).
For \(J=0\) use \(N=1\).
The finitely many distinct maximal ideals are pairwise comaximal, with
intersection \(J\); the Chinese remainder maps give
\(D/J\simeq\prod_{\mathfrak q}\kappa(\mathfrak q)\), a finite-dimensional
algebra over \(\kappa(\mathfrak p)\).
Each \(J^i/J^{i+1}\) is a finite \(D/J\)-module (its generators are the
degree-\(i\) monomials in the original \(z_j\)), so it too is finite
dimensional. The exact sequences of the finite filtration by the
\(J^i\) prove the assertion for \(D\). No reduced-fibre assumption is used.
This strengthens the source's finite-point conclusion while retaining
its original finite-type case and its possibly empty fibre.

## The missing topological hypothesis and its exact repair

Source 27624–27637. The statement "A Noetherian topological space
consisting of closed points is finite" is false for general spaces.
Let \(X\) be an infinite set with the cofinite topology. Closed subsets
are \(X\) and finite subsets. Every descending chain of closed subsets
stabilizes: once it leaves \(X\), it is a chain inside one finite set.
Thus \(X\) is Noetherian, and all its points are closed, but \(X\) is
infinite. Moreover any two nonempty opens meet, so \(X\) is irreducible.
It has no generic point, since each point has singleton closure.
This identifies the exact missing structure.

The corrected assertion is true for a sober Noetherian space with all
points closed. A Noetherian space has finitely many irreducible components:
otherwise choose a minimal closed counterexample by the descending-chain
condition; it is reducible, and its two proper closed pieces each have
finite decompositions, a contradiction. In a sober space each component
is the closure of its generic point. If that point is closed, the component
is a singleton. Hence the space is finite, including the empty case.

For \(X=\operatorname{Spec}D\), sobriety follows directly. An irreducible
closed subset \(V(I)\) has prime radical \(P=\sqrt I\): if \(ab\in P\), then
\(V(I)\subset V(a)\cup V(b)\), and irreducibility puts it in one of these
sets, so \(a\in P\) or \(b\in P\).
Its generic point is precisely \(P\), since \(\overline{\{P\}}=V(P)=V(I)\);
uniqueness follows because distinct primes have distinct closures.
This proves the hypothesis for the original fibre, so the source theorem
remains valid. The minimal proposal adds "sober" to its topological
assertion and keeps the cited Topology lemma, which states finiteness
of irreducible components at authority 1252–1301, not finiteness of
arbitrary Noetherian \(T_1\) spaces.

## The original literature counterexample and propagation boundaries

The indexed original author source is Katharina Heinrich,
"Some remarks on biequidimensionality of topological spaces and Noetherian
schemes", arXiv:1403.5814, canonical ID
`PUBUNIT-EB76FB876CD8CEEBBA2086CE`.
Exact file:
`F:/user/Documents/arxiv_latex/_expanded_by_topic/krull_dimension_theory/6637bf65ee5385b5/1403.5814/1403.5814.tex`,
SHA-256 `CB4305F104ABA334E06B0556137AA89484EE797E31D3558B5D6AEB244841A911`.
Actual reading: lines 1–343, 502–667 and 701–741.
The construction section 344–501 and the later example 668–700 remain
unread. No claim is made to have independently checked every result in
the read ranges or any EGA passage quoted by this paper.

Here is an independent verification of the exact example
`ex:glue2`, lines 531–550, used to test propagation.
Keep the author's ring and both prime ideals:
\[
 B=k[u,v,w,x,y,z]/(uy,uz,vy,vz,wy,wz),\qquad
 M_1=(u,v,w,y,z),\quad M_2=(u,v,w,x,y-1,z-1),
\]
and put \(T=B\setminus(M_1\cup M_2)\), \(A=T^{-1}B\).
The complement is multiplicatively closed because \(M_1,M_2\) are prime.
A prime disjoint from \(T\) is contained in \(M_1\cup M_2\), hence in one
of them: if an ideal contained in their union were contained in neither,
choose one element outside each and use their sum for a contradiction.
The two primes are incomparable. Thus these are exactly the two maximal
ideals after localization.

In the original polynomial ring,
\((u,v,w)\cap(y,z)=(u,v,w)(y,z)\): a monomial belongs to the intersection
exactly when it has a factor from each of the two disjoint variable sets.
Their product is exactly the six displayed generators.
Consequently \(B\) is reduced with precisely two minimal primes
\(P=(u,v,w)\), \(Q=(y,z)\).
Every prime contains one of them: in a prime containing their product,
failure to contain either would give a product of two elements outside
the prime. The component rings before localization are
\(B/P=k[x,y,z]\) and \(B/Q=k[u,v,w,x]\).

The \(P\)-component has maximal primes \((y,z)\) and
\((x,y-1,z-1)\), of heights two and three.
The \(Q\)-component has only the maximal prime \((u,v,w)\), of height
three: \(M_2\) does not contain \(Q\).
These height counts can be checked with the exact coordinate ideals.
At \((y,z)\) the coefficient \(x\) passes to \(k(x)\), leaving the
two-variable coordinate maximal ideal; at \((u,v,w)\) the coefficient
\(x\) likewise passes to \(k(x)\), leaving three variables.
At \((x,y-1,z-1)\) the three displayed generators give the upper bound
three, and their successive prime ideals give the lower bound three.
Thus both irreducible components of \(\operatorname{Spec}A\) have
dimension three, and both maximal ideals have height three; at \(M_1\)
the two component heights are two and three, while at \(M_2\) only the
height-three \(P\)-component remains. The equality of dimension with the
maximum of component dimensions follows by putting each prime chain
inside a component containing its first prime.

These component polynomial rings are catenary. One can check this without
using a general global dimension formula: their local rings are
Cohen–Macaulay, as successive polynomial extension and localization of a
field preserve the already proved Cohen–Macaulay property. The earlier
CM chain theorem proves each such local ring catenary. Every fixed interval
of primes lies in the localization at its upper prime and retains exactly
its intermediate primes, so the whole component is catenary.
The same holds after localization. The closed-cover criterion proved
in group 594 therefore makes \(A\) catenary.

Now keep the source prime \(\mathfrak p=(u,v,w,y)A\).
Before localization it is prime with quotient \(k[x,z]\), it is disjoint
from \(T\), and it lies under \(M_1\) alone.
It contains \(P\) and does not contain \(Q\), since \(z\notin\mathfrak p\).
Thus every prime below it contains \(P\); on that component it corresponds
to the height-one prime \((y)\) of \(k[x,y,z]\).
The entire lower interval survives localization, so
\(\operatorname{ht}_A\mathfrak p=1\).
The primes of \(A/\mathfrak p\) correspond to the primes of \(k[x,z]\)
contained in \((z)\), giving dimension one, with its strict chain
\(0\subsetneq(z)\). Therefore, retaining all original objects,
\[
 \operatorname{ht}_A\mathfrak p+\dim(A/\mathfrak p)=1+1=2<3=\dim A.
\]
This verifies the cited counterexample, rather than treating the abstract
as proof.

It checks the limitations of earlier groups 590 and 595: they retained a
local ring, and group 590 also retained a nonzero Cohen–Macaulay module
and its actual support. Equidimensionality, equal heights of maximal
ideals and catenarity of a nonlocal ring do not replace those hypotheses.
No contradiction with the source's relative dimension formula for an
extension of domains follows from this example. Both original statements
remain valid in their checked scopes; no earlier formula is silently
broadened. This is use of an existing human result, not a new result or
a claim that the EGA counterexample construction has been exhaustively read.

The other new routing hit, Epstein–Shapiro arXiv:1501.03411, remains unread.
The topic route preserves its source identity without using its theorems.

