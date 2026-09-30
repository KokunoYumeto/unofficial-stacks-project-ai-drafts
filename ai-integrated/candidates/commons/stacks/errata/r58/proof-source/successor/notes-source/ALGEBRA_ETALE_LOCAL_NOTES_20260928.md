# Local étale presentations, retained scalar factors and finite covers

Private source-linked editorial evidence, 2026-09-28. Source: The Stacks Project authors, algebra.tex at a04446e57ec1fbc252a871afcec7752fb2807b14, lines 39754–40187, and the second locus 40463–40470 of report OCC-12163. Full authority SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3. Original assertions, objects and proof order remain identifiable. The additional proofs below are editorial material; no novelty is claimed.

## Original local-structure proof and the missing scalar

For a standard étale presentation \(S=R[x]_g/(f)\), keep the given monic \(f\) and the specified invertible image of \(f'\). Writing
\[
S=R[x,z]/(f,zg-1)
\]
gives the derivative matrix with equation order \((f,zg-1)\), variable order \((x,z)\):
\[
\begin{pmatrix} f'&0\\zg'&g\end{pmatrix},
\qquad \det=f'g.
\]
Both factors are units in \(S\), proving étaleness. Under base change the same equations, their monicity and the inverse identities persist. If \(s=h/g^a\in S\), its principal localization is \(R[x]_{gh}/(f)\): inverting \(g\) makes \(s\) invertible exactly when \(h\) is invertible. This proves the first three properties at 39781–39792 without changing the definition.

For prescribed residue fields at 39809–39841, put \(K=\kappa(\mathfrak p)\), choose the original primitive element \(\alpha\) of the given finite separable \(L/K\), and let
\[
F(X)=X^d+a_1X^{d-1}+\cdots+a_d.
\]
Choose representations \(a_i=u_i/v_i\) in \(K\), with \(u_i,v_i\in R\), \(v_i\notin\mathfrak p\), and put \(c=\prod_i v_i\notin\mathfrak p\). If the degree is zero there is no field extension, so here \(d\ge1\). The auxiliary element \(\beta=\bar c\alpha\) has minimal polynomial
\[
F_c(X)=\bar c^{\,d}F(X/\bar c)
=X^d+\bar c\,a_1X^{d-1}+\cdots+\bar c^{\,d}a_d.
\]
Each coefficient is in the image of \(R\), because \(c^i a_i=u_i(c/v_i)c^{i-1}\). Retain these powers, and recover \(\alpha=\beta/\bar c\) in \(L\). The derivative is \(F_c'(X)=\bar c^{d-1}F'(X/\bar c)\), so \(F_c'(\beta)\ne0\). Lift \(F_c\) to a monic \(f\in R[X]\). The evaluation map \(R[X,1/f']/(f)\to L\) sends \(X\) to \(\beta\) and the inverse of \(f'\) to \(F_c'(\beta)^{-1}\). Its image contains the image of \(R/\mathfrak p\) and \(\beta\); its fraction field is therefore \(K(\beta)=L\). Thus the residue field at its kernel is the required original extension \(L/K\), without asserting that the evaluation map is surjective as a ring map.

In the original eleven-step proof at 39843–40062, Step 2 has a genuine target typo: the descended target is \(S=R\otimes_{R_0}S_0\), not \(R=R\otimes_{R_0}S_0\). This is recorded as a minimal correction, with the original approximation argument retained.

Step 3 uses 30906–30949 to choose a finite \(R\)-subalgebra and a principal open on which it agrees with the original algebra. Membership of its element in a prime of the target means membership of its image under the displayed map. This conventional notation is not an ill-typed assertion. Removing the repeated “such that” repairs the sentence while leaving that map explicit in the argument.

Steps 4–6 retain the fibre decomposition into local Artinian \(K\)-algebras, with distinguished factor \(A_1=\kappa(\mathfrak q)\). Choose a nonzero primitive element \(\alpha\) in that field. In the fibre choose \((\alpha,0,\ldots,0)\). Since the fibre is a localization of \(S/\mathfrak pS\), multiplying by the image of one element of \(R\setminus\mathfrak p\) makes this element lift to \(t\in S\); the resulting nonzero scalar multiple of \(\alpha\) remains primitive. Set \(T=R[t]\subset S\), using the source's \(S'\) for this ring when reading the passage. The other fibre primes contract to \(x=0\), whereas the distinguished one does not because \(\alpha\ne0\). Thus the distinguished prime is the only one over its contraction \(\mathfrak q'\subset T\).

Finiteness makes \(T\to S\) integral. The unique-prime localization result at 9797–9830 identifies \(S_{\mathfrak q'}=S_{\mathfrak q}\). The injective map \(T_{\mathfrak q'}\to S_{\mathfrak q}\) is finite, and
\[
\mathfrak pS_{\mathfrak q}
=\mathfrak qS_{\mathfrak q}
=\mathfrak q'S_{\mathfrak q}.
\]
The last equality follows because the middle ideal contains \(\mathfrak q'S_{\mathfrak q}\), which contains the first ideal. The image of \(\alpha\) shows \(\kappa(\mathfrak q')=\kappa(\mathfrak q)\). Nakayama applied to the finite cokernel now proves \(T_{\mathfrak q'}=S_{\mathfrak q}\). The source's Step 7 extends this to principal neighbourhoods. Its dependency 31623–31660 is read with the already retained corrections MC-STK-ERR-0669 (invert the idempotent selecting the \(S\) factor) and MC-STK-ERR-0672 (both missing polynomial-presentation replacement verbs). No duplicate correction is submitted here.

**The scalar error.** In Step 8, let \(H\in K[x]\) be the initial monic generator of the fibre ideal. The argument multiplies it by a nonzero scalar \(\lambda\in K^\times\) so that its replacement is the image of a particular \(h\in I\subset R[x]\). This scalar cannot subsequently disappear. With the original monic irreducible factors and their original exponents, the actual formula is
\[
\overline h
=\lambda\overline h_1\overline h_2^{e_2}\cdots\overline h_n^{e_n}.
\]
Set \(e_1=1\), making the following uniform formula for the rings \(A_i\) well-defined. The unit \(\lambda\) changes neither the ideal generated by \(\overline h\) nor its primary factors, but it does change its polynomial coefficients.

Keep the original monic \(m\in I\), its factorization
\[
\overline m=\overline k\prod_{i=1}^n\overline h_i^{d_i},
\qquad d_1\ge1,\quad d_i\ge e_i\ (i\ge2),
\]
and the original integer \(l\ge2\) with \(l\deg m>\deg h\). The actual \(f=m^l+h\) is monic, and its full reduction is
\[
\begin{aligned}
\overline f
&=\lambda\overline h_1\prod_{i=2}^n\overline h_i^{e_i}
 +\overline k^{\,l}\prod_{i=1}^n\overline h_i^{ld_i}\\
&=\overline h_1
\left(
\lambda\prod_{i=2}^n\overline h_i^{e_i}
+\overline k^{\,l}\overline h_1^{ld_1-1}
 \prod_{i=2}^n\overline h_i^{ld_i}
\right)
=\overline h_1\overline w.
\end{aligned}
\]
Modulo \(\overline h_1\), the second summand inside parentheses is zero because \(ld_1-1\ge1\), whereas the first is nonzero because \(\lambda\ne0\) and the original irreducibles are pairwise coprime. Therefore \(\overline w\) is coprime to \(\overline h_1\). The derivative retains both summands:
\[
\overline{f'}=\overline h_1'\overline w+\overline h_1\overline w'.
\]
At the specified residue point its value is \(\overline h_1'\overline w\ne0\), by separability. Hence the conclusion of Steps 9–10 remains valid with the scalar restored.

The missing factor is a literal polynomial error, not only a preferred notation. Take \(R=\mathbf Z\), \(\mathfrak p=(3)\), \(S=R[x]/(x-1)\), distinguished residue element \(1\), \(h=2(x-1)\), \(m=x-1\), \(l=2\). Then \(\lambda=2\) in \(\mathbf F_3\) and the actual \(f=m^2+h=x^2-1\). The uncorrected displayed expression instead gives \((x-1)+(x-1)^2=x^2-x\). Both satisfy a simple-root argument at the chosen point, but they are different polynomials. The repair therefore keeps the actual \(h,m,f\), inserts the missing \(\lambda\) at 39987, 40013 and 40018, and states \(\lambda\ne0\) at 39978.

In Step 11, retain \(g=f'\) and the separate element \(g'\) selecting an étale neighbourhood of \(S\). The resulting surjection
\[
R[x]_{gg'}/(f)\longrightarrow S_{\varphi(gg')}
\]
is between étale \(R\)-algebras, so is étale, flat and finitely presented. Its kernel is generated by an idempotent; the quotient is a principal localization at the complementary idempotent. Any element of the left side is represented by a polynomial divided by a power of \(gg'\), so further principal localization still has the original standard étale form. The local-structure theorem follows. The repaired formulas and the complete explanation remain visible editorial material; they are not grounds for replacing the original eleven-step translation by a new proof.

## Monogenic étale algebras over fields

For a field \(k\), a finite étale \(k\)-algebra \(A\) is standard étale if and only if it is generated by one element as a \(k\)-algebra. To prove the nontrivial forward assertion, write \(A=k[x]_g/(f)\), and let \(a\) be the image of \(x\). The subalgebra \(B=k[a]\subset A\) is finite-dimensional because \(f\) is monic. Multiplication by \(g(a)\) on \(B\) is injective, since \(g(a)\) is invertible in \(A\). It is consequently surjective on the finite-dimensional vector space \(B\), so \(g(a)b=1\) for some \(b\in B\). Thus \(g(a)^{-1}\in B\) and \(A=B\). Conversely, if \(A=k[a]\), write \(A=k[x]/(F)\) with \(F\) monic. The finite étale field classification implies that \(F\) is a product of distinct separable irreducible polynomials, so \(\gcd(F,F')=1\). Hence \(F'\) is invertible in \(A\), giving a standard étale presentation with \(g=1\). For \(A=0\), use \(F=1\), whose derivative is the unit \(0=1\) of the zero ring.

Let now \(k=\mathbf F_q\) and
\[
A=\prod_{d\ge1}\bigl(\mathbf F_{q^d}\bigr)^{r_d},
\]
with only finitely many nonzero \(r_d\). Let \(N_q(d)\) be the number of monic irreducible polynomials of degree \(d\) in \(\mathbf F_q[x]\). Then the exact criterion is
\[
A\text{ is standard étale over }\mathbf F_q
\quad\Longleftrightarrow\quad
r_d\le N_q(d)\text{ for every }d.
\]
Indeed an element generating \(A\) must generate each factor field, and its minimal polynomials in distinct factors must be pairwise different: the evaluation map onto the product is surjective exactly when its kernel ideals are pairwise comaximal. Distinct monic irreducible polynomials are comaximal, while equal ones are not. For each degree \(d\), therefore, one needs \(r_d\) distinct irreducibles of degree \(d\). Conversely choose precisely that many distinct irreducibles for every degree and use the Chinese remainder theorem on their product. Each quotient is the corresponding finite field, proving sufficiency.

The numerical bound is
\[
N_q(d)=\frac1d\sum_{e\mid d}\mu(e)\,q^{d/e}.
\]
Here \(\mu(e)\) is zero when a prime square divides \(e\), and otherwise equals \((-1)^s\) when \(e\) has \(s\) distinct prime factors. For completeness, the roots of \(x^{q^a}-x\) in an algebraic closure form a field with \(q^a\) elements: addition, multiplication and inverses are preserved by the \(q^a\)-power map, and the derivative \(-1\) gives exactly \(q^a\) distinct roots. Frobenius permutes the roots of a monic irreducible of degree \(d\) in one orbit of length \(d\). To justify the orbit length, its distinct Frobenius orbit product has coefficients fixed by \(z\mapsto z^q\), hence in \(\mathbf F_q\); minimality forces that product to be the given irreducible. Thus this irreducible divides \(x^{q^a}-x\) exactly when \(d\mid a\). Factoring that square-free polynomial gives \(q^a=\sum_{d\mid a}dN_q(d)\). Multiplying these equalities by \(\mu(e)\) over divisors \(e\mid d\) and using \(\sum_{e\mid m}\mu(e)=0\) for \(m>1\), \(=1\) for \(m=1\), yields the displayed formula. The divisor identity follows by expanding \(\prod_{\ell\mid m}(1-1)\) over the distinct prime divisors \(\ell\).

In the original example \(q=2,d=2\), \(N_2(2)=(4-2)/2=1\). Therefore \(\mathbf F_4^4\) is not standard étale over \(\mathbf F_2\), although \(\mathbf F_2\to\mathbf F_4\) has polynomial \(x^2+x+1\) and the diagonal \(\mathbf F_4\to\mathbf F_4^4\) has polynomial \(x^4-x\), with invertible derivative \(1\). The example is correct.

Two copies already suffice: the composition \(\mathbf F_2\to\mathbf F_4\to\mathbf F_4^2\) uses \(x^2+x+1\) for the first map and \(x(x-1)\) for the second. The derivative \(2x-1=1\) of the latter is invertible in characteristic two. But \(r_2=2>N_2(2)\), so the composite is not standard étale. This is a smaller valid counterexample, kept as a separate editorial consequence.

The obstruction disappears over infinite fields. Write a finite étale algebra as \(\prod_{i=1}^r L_i\) with each \(L_i/k\) finite separable, and choose a primitive element \(a_i\in L_i\). Choose constants \(c_i\in k\) successively so that the sets of conjugates of \(a_i+c_i\) are pairwise disjoint. At stage \(i\), the forbidden equalities are
\[
\sigma(a_i)+c_i=\tau(a_j)+c_j,\qquad j<i,
\]
over the finitely many embeddings into an algebraic closure. Each excludes at most one value of \(c_i\) in \(k\), so an infinite field supplies a permitted value. Within one factor the conjugates remain distinct. Therefore the shifted elements have pairwise different separable minimal polynomials, and the tuple \((a_i+c_i)_i\) generates the product by the Chinese remainder theorem. The original elements are recovered as \(a_i=(a_i+c_i)-c_i\). Hence every étale algebra over an infinite field is standard étale, using the earlier theorem that such algebras are finite. Compositions of standard étale maps over an infinite base field are accordingly standard étale. This statement concerns the base field and does not assert a general ring version.

## Explicit finite free covers and every chosen fibre point

The end-of-section finite projective cover can be taken finite free, syntomic, and of a specified rank. For a given standard presentation \(S=R[x]_g/(f)\) of monic degree \(n\), construct the ordered-root algebra of the original polynomial, retaining all coefficients.

Put \(R_0=R\), \(Q_0(X)=f(X)\), and for \(j=1,\ldots,n\) define
\[
R_j=R_{j-1}[\alpha_j]/(Q_{j-1}(\alpha_j)),
\qquad
Q_{j-1}(X)=(X-\alpha_j)Q_j(X)\text{ in }R_j[X].
\]
The polynomial \(Q_j\) exists by monic division. If \(Q_{j-1}=X^d+u_1X^{d-1}+\cdots+u_d\), its quotient coefficients are \(v_0=1\),
\[
v_k=u_k+\alpha_jv_{k-1}\ (1\le k<d),
\qquad u_d=-\alpha_jv_{d-1}.
\]
Thus no coefficient or constant relation has been suppressed. Monic division gives the free \(R\)-basis
\[
\alpha_1^{a_1}\cdots\alpha_n^{a_n},
\qquad 0\le a_j<n-j+1,
\]
of \(R_n\), of rank \(n!\). The case \(n=0\) uses the empty tower \(R_n=R\), empty basis product \(1\), and rank \(0!=1\). Each step has a monic relation, hence a non-zero-divisor in its polynomial ring when that ring is nonzero, and after every residue-field base change has a zero-dimensional hypersurface fibre. Therefore each step is a relative global complete intersection, flat and syntomic. Composition is syntomic. The positive free rank makes \(R\to R_n\) faithfully flat. These assertions also follow from the exact ordered-root calculation in group 1042 and lemma-adjoin-roots at 36857–36875; the recursive proof here specifies the rank and basis used in the present cover.

Take \(D=R_n\). For every specified \(\mathfrak q\in\operatorname{Spec}S\) over \(\mathfrak p\in\operatorname{Spec}R\), and every \(\mathfrak q'\in\operatorname{Spec}D\) over the same \(\mathfrak p\), one can choose a principal neighbourhood of \(\mathfrak q'\) and a map from \(S\) whose contraction is exactly the specified \(\mathfrak q\). In fact put \(K=\kappa(\mathfrak p)\) and \(K'=\kappa(\mathfrak q')\). The prime \(\mathfrak q\) corresponds to an irreducible factor \(f_1\) of \(\bar f\in K[x]\) with \(f_1\nmid\bar g\). The polynomial \(\bar f\) splits in \(K'\) with roots the images of the actual \(\alpha_j\). Since \(f_1\) divides it, some root \(\bar\alpha_j\) satisfies \(f_1(\bar\alpha_j)=0\). Its minimal polynomial over \(K\) is \(f_1\). A Bézout identity for \(f_1,\bar g\), evaluated at this root, proves \(\bar g(\bar\alpha_j)\ne0\).

The map \(R[x]/(f)\to D\) sending \(x\) to \(\alpha_j\) therefore extends to
\[
S\longrightarrow D_{\,g(\alpha_j)}.
\]
Its contraction of \(\mathfrak q'D_{g(\alpha_j)}\) is \(\mathfrak q\), because its residue evaluation has exactly the irreducible kernel \((f_1)\) over \(K\). This proves both conditions the source leaves implicit at 40125–40127.

For an arbitrary étale \(R\)-algebra \(S\), choose a finite principal cover \(S_{s_i}\) by standard presentations of degrees \(n_i\), and perform the preceding construction for each, giving \(D_i\). Put
\[
D=\bigotimes_{i=1}^r D_i.
\]
The tensor products of the displayed ordered-root monomial bases give an actual free \(R\)-basis of cardinality
\[
\prod_{i=1}^r n_i!.
\]
This finite free map is faithfully flat and syntomic, and every construction commutes with arbitrary base change because it uses the same polynomial relations and monic divisions.

More precisely, no surjectivity assumption on \(\operatorname{Spec}S\to\operatorname{Spec}R\) is needed for the following statement. For each pair of primes \(\mathfrak q\in\operatorname{Spec}S\), \(\mathfrak q'\in\operatorname{Spec}D\) lying over the same \(\mathfrak p\), there is \(h\in D\setminus\mathfrak q'\) and an \(R\)-map \(S\to D_h\) whose contraction of \(\mathfrak q'D_h\) is exactly \(\mathfrak q\). Choose \(i\) with \(s_i\notin\mathfrak q\), and contract \(\mathfrak q'\) to \(D_i\). The previous paragraph supplies \(h_i\) outside that contracted prime and \(S_{s_i}\to(D_i)_{h_i}\) with the prescribed contraction. Its base change to \(D_{h_i}\), preceded by \(S\to S_{s_i}\), gives the required map. The element \(h_i\) remains outside \(\mathfrak q'\) by the definition of contraction.

Consequently the set of points of \(\operatorname{Spec}D\) admitting such a local factorization is exactly the inverse image of the image of \(\operatorname{Spec}S\). One inclusion is the construction just proved. Conversely any such factorization supplies a prime of \(S\) by contraction, lying over the same base prime. The image of an étale map is open, since it is flat and finitely presented, so this is an open subset of \(\operatorname{Spec}D\). When the original map is surjective on spectra it is the whole space, giving the source's last lemma with the stronger finite free, syntomic conclusion and the explicit rank above. If \(S=0\), use the empty cover and \(D=R\); the relevant open subset is empty and all assertions about specified pairs of primes are vacuous. No claim is made that \(D/R\) is étale, nor that a general nonfinite étale \(S\) becomes a finite product of copies of the base on these neighbourhoods.

## Direct finite-cokernel comparison over an arbitrary base

There is also a direct variant of the local-structure proof which avoids Noetherian approximation. This does not strengthen the already arbitrary-base conclusion of the source theorem; it weakens hypotheses in an intermediate argument and gives a separate proof of that same conclusion.

First suppose \(A\hookrightarrow B\) is a finite injective ring map, \(\mathfrak p\in\operatorname{Spec}A\) has just one prime \(\mathfrak q\) of \(B\) above it, and \(A_{\mathfrak p}\to B_{\mathfrak q}\) is an isomorphism. Finiteness makes \(B_{\mathfrak p}\) integral over the local ring \(A_{\mathfrak p}\). Its maximal ideals all lie over the maximal ideal of \(A_{\mathfrak p}\), so the specified uniqueness makes \(B_{\mathfrak p}\) local with maximal ideal induced by \(\mathfrak q\). Hence \(B_{\mathfrak p}=B_{\mathfrak q}\).

The cokernel \(C=B/A\) is a finitely generated \(A\)-module: any finite set of \(A\)-generators of \(B\) maps to generators of \(C\). Its localization at \(\mathfrak p\) is zero by the assumed isomorphism. For actual generators \(c_1,\ldots,c_a\), choose \(u_i\in A\setminus\mathfrak p\) with \(u_ic_i=0\), and set \(u=\prod_i u_i\). Then \(u\notin\mathfrak p\) and \(C_u=0\). Localization preserves the original injection, so
\[
A_u\xrightarrow{\;\sim\;}B_u.
\]
No Noetherian assumption and no finite-presentation hypothesis on \(A\) or \(B\) was used. The uniqueness of the prime is essential to this stated argument; a local isomorphism at just one of several points above \(\mathfrak p\) does not imply \(C_{\mathfrak p}=0\).

Apply this to the source after Step 1. The finite-algebra neighbourhood in Step 3 exists over an arbitrary base by 30906–30949. Choose the fibre element and \(t\) exactly as in Steps 4–5, and put \(T=R[t]\subset S\) for the resulting finite \(R\)-algebra \(S\). The element \(t\) is integral over \(R\), since \(S/R\) is finite; the powers of \(t\) up to one less than the degree of an actual monic relation span \(T\). Thus \(T/R\) is finite without invoking the generally false assertion that every submodule of a finite module is finite over a non-Noetherian ring.

The argument in Step 6 uses only finiteness, injectivity, uniqueness of the prime over \(\mathfrak q'\), the original étale residue-field conclusions and Nakayama for a finite cokernel. All remain valid over the arbitrary base. The finite-cokernel comparison just proved then replaces Step 7, with an explicit \(u\in T\setminus\mathfrak q'\) giving \(T_u=S_u\). Consequently \(T\) is étale at \(\mathfrak q'\), is finite over \(R\), and is a quotient \(R[x]/I\).

Steps 8–10 require only a principal ideal after passing to the field \(\kappa(\mathfrak p)\), a monic integral relation and a lift of a scalar multiple of that field-ideal generator. These hold without Noetherianity. To justify the lift explicitly, write the field generator as a finite combination of images of elements of \(I\), with polynomial coefficients in \(\kappa(\mathfrak p)[x]\); multiply by a product of their finitely many nonzero denominators from \(R/\mathfrak p\). This gives precisely the nonzero scalar \(\lambda\) and \(h\in I\) used above, with all three scalar factors retained. Step 11 uses a standard étale algebra and a principal neighbourhood of \(T\) already known to be étale; these are finitely presented by definition. Its surjection therefore has finitely generated idempotent kernel, completing the same standard étale neighbourhood construction.

One final localization detail keeps the statement's original source ring. When replacing a ring by an isomorphic principal neighbourhood, any further principal localization is still a principal localization of that original ring: if the first denominator is \(a\) and the new element is \(b/a^N\), their combined localization is the localization at \(ab\). The relevant point excludes both factors. This proves that the successive finite-algebra and monogenic comparisons return an actual \(S_g\) in the original theorem, rather than only an unrelated locally isomorphic algebra.

## Report accounting and propagation

Nineteen received reports have sixteen report groups. No existing canonical operation lies in 39754–40187 or in 40463–40470; both current intervals agree with authority.

- OCC-00880: optional mathematical source whitespace, no edit.
- OCC-12163: reject the alleged mismatch between extension notations \(L/K\) and \(K\subset L\). Both name the same field-extension data, not a quotient ring; the two source loci have been read. The second locus does not adjudicate the rest of the future section.
- OCC-12164 and OCC-00881: one target-algebra correction at 39864, \(R\) to \(S\).
- OCC-00882: “Denote by” at 39864.
- OCC-12165, OCC-12166 and OCC-00883: one correction to the repeated connective at 39876. Membership is interpreted through the already specified ring map; that conventional shorthand is not a second mathematical defect.
- OCC-00884: punctuation at the end of the fibre-product display, 39891.
- OCC-00885: “Denote by” at 39931.
- OCC-00886: reject the assertion that “we have going up” is grammatically malformed. It names a property, as does “we have flatness”; the actual finite integral map has that property.
- OCC-00887: supply “is” in the finite-algebra condition at 39968.
- OCC-00888: explicitly set \(e_1=1\) at 39991 for the following formula indexed by all \(i\).
- OCC-00889: “Denote by” at 40000.
- OCC-00890: optional enumeration colon, no edit.
- OCC-00891 and OCC-00892: separate “Denote by” corrections at 40117 and 40167.
- OCC-00893: supply “to be” in the contracted-prime definition at 40171.
- OCC-00894: optional restatement of the inherited nonmembership of \(g_i'\) in \(\mathfrak q_i'\), no source edit. The preceding lemma supplies that condition, and contraction proves the required nonmembership in \(\mathfrak q'\). An omitted repeated condition is not a missing proof here.

Group 1145 adds the four-operation scalar repair and propagates it through every displayed factorization of the same original polynomial. It does not change the theorem. Groups 1146–1148 have zero operations: the field-generator criterion and exact finite-field bound; the finite free syntomic cover with its rank and prescribed fibre points; and the finite-cokernel comparison with the direct arbitrary-base proof. The last is an alternative argument for the source's existing general theorem, not a newly generalized statement of that theorem.

Receiving dependencies are the source's étale field classification, finite flat quotient and local lifting arguments, group 1042's full ordered-root basis, and group 1128's factor and multiplicity analysis. Earlier idempotent and presentation corrections remain retained. Complete mathematical arguments stay in this note and are not substituted for the translation. Broader synthesis and its paper follow the core review.

Dependencies read: 9785–9834, 30896–30966, 31615–31670, 36848–36918; the exact cited portions are 9797–9830, 30906–30949, 31623–31660 and 36857–36875. The new indexed query returned two research routing records, both unread and unused. Seven earlier external-source reading records retain their exact coverage. No new external reading, PDF fallback or novelty claim is asserted.

Next authority line 40188, Étale local structure of quasi-finite ring maps; only opening 40188–40200 and the explicitly scoped second report locus 40463–40470 have been read ahead. No translation mutation, TeX run or publication is performed by this intake.
