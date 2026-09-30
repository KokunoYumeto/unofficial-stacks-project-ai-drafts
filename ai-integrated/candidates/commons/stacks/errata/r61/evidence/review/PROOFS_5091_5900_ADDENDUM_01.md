# A further degree in the left-exact finite-prefix comparison

This strengthens the left-exact clause of DERIVED-UNDER-007 in section 5
of `PROOFS_5091_5900.md`. The earlier statement and its exact defect
sequence remain valid. No source-body replacement or new claim ID is
introduced, and no novelty is asserted.

Let F:A -> B be additive and left exact, let A^bullet be bounded below,
and suppose RF(A^bullet) is defined. If A^n is right F-acyclic for
n<=m, then its canonical comparison satisfies

\[
 H^j(F(A^\bullet))\xrightarrow{\sim}H^j(RF(A^\bullet))
       \quad(j\le m+1),
 \qquad
 H^{m+2}(F(A^\bullet))\lhook\joinrel\longrightarrow
                                  H^{m+2}(RF(A^\bullet)).       \tag{1}
\]

Thus for an isomorphism through degree q, acyclicity through degree
q-1 suffices. This retains every term and differential of A, including
the term A^{q+1} used to calculate H^q of F(A). No existence of RF
on all complexes or on any additional cohomology object is assumed.

First consider a complex T zero below an integer a, with RF(T)
defined. For a quasi-isomorphism s:T -> L with L also zero below a,
the original cone C(s) has components T^{n+1} direct-sum L^n and
differential (-d_T,0;s,d_L). It is zero below a-1 and acyclic, so

\[
 0\longrightarrow C(s)^{a-1}\longrightarrow C(s)^a
                         \longrightarrow C(s)^{a+1}
\]

is exact. Left exactness preserves this exact sequence, including its
kernel in the middle. Hence H^{a-1}(F(C(s)))=H^a(F(C(s)))=0.
Additivity identifies F(C(s)) with C(F(s)), preserving that entire
matrix and its minus sign. The cone long exact sequence consequently
makes H^a(F(s)) an isomorphism and H^{a+1}(F(s)) a monomorphism.

Targets L zero below a form a cofinal subcategory of T/Qis(A), as
proved in section 4 of the main note. It includes the identity of T.
Applying H^a to the essential-constancy diagram, every transition is
an isomorphism by the preceding calculation. Its canonical map from
H^a(F(T)) to the value H^a(RF(T)) is therefore an isomorphism.

For the next degree, apply H^{a+1} to the original essential-constancy
witness. Write c:H^{a+1}(F(T)) -> H^{a+1}(RF(T)) for the canonical
map. The eventual factorization property at the identity index gives
some denominator s:T -> L and a map v from H^{a+1}(RF(T)) to
H^{a+1}(F(L)) such that

\[
 H^{a+1}(F(s))=v c.
\]

The left side is monic by the cone calculation; hence c is monic.
This proof uses the witness itself and does not assume that an
arbitrary colimit of monomorphisms exists or stays monic in B.
We have proved the exact lowest-degree comparison

\[
 H^a(F(T))\simeq H^a(RF(T)),\qquad
 H^{a+1}(F(T))\lhook\joinrel\longrightarrow H^{a+1}(RF(T)). \tag{2}
\]

Now put P=sigma_{<=m}A and T=sigma_{>=m+1}A, keeping the termwise
split sequence 0 -> T -> A -> P -> 0. P is bounded and consists
of acyclic objects, so it computes RF. Two-out-of-three therefore
defines RF(T). All cohomology of F(P) and RF(P) above m is zero.
At degree m+1 the comparison of the two triangle sequences is a map
between the cokernels of

\[
 H^m(F(P))\longrightarrow H^{m+1}(F(T)),
 \qquad
 H^m(RF(P))\longrightarrow H^{m+1}(RF(T)).
\]

Both vertical maps are isomorphisms: the first by computation on P,
the second by (2) with a=m+1. Their cokernels, respectively
H^{m+1}(F(A)) and H^{m+1}(RF(A)), are therefore canonically isomorphic.
The lower degrees are isomorphic by the main note's argument.
At degree m+2 the same triangle sequences identify H^{m+2}(F(A))
with H^{m+2}(F(T)) and H^{m+2}(RF(A)) with H^{m+2}(RF(T)), because
both adjacent cohomology objects of P vanish. Under those identifications
the comparison is the monomorphism in (2). This proves (1) with
the actual canonical maps.

For the receiving global-sections calculation in the main note,
degree q therefore only requires Gamma(Y,-)-acyclicity of K^n for
n<=q-1. Its displayed formula (7.1), including K^{q+1} and both
differentials, is unchanged. For the repaired H^0 step in Perfect
Complexes, the bounded-below original-term truncation only needs
acyclicity in its negative degrees to obtain that H^0 comparison;
the original theorem supplies acyclicity of all terms, so its statement
and the recorded source repair remain unchanged.
