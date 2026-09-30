# Editorial evidence for Algebra 13249–13990

Authority: original `algebra.tex`, commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`. This interval and all twelve reports whose first loci lie in it were read. The proposed source operations are small corrections or clarifications. The arguments and strengthening below are separately identified editorial material, not replacement proof bodies for a translation. No novelty is claimed.

## Bounded-below graded Nakayama

Source: `lemma-graded-NAK`, lines 13249–13272. Its four statements are valid as written. A finite graded module over the original nonnegatively graded ring is bounded below: take homogeneous parts of a finite generating list; multiplication by a ring element never lowers degree below the least generator degree. The original induction therefore works, including a module with no generators.

There is a strengthening, recorded here without changing the source. In statements (1), (3), and (4), replace finite generation of \(M\) by the assumption that \(M_d=0\) for all \(d<b\), for some integer \(b\). In (2), the corresponding weaker assumption is that \(N'\) is bounded below. The original nonnegative ring grading, possible negative module degrees, and all original maps remain unchanged.

For (1), suppose \(M=S_+M\). Induct on integers \(d\geq b\). For a homogeneous \(m\in M_d\), an expression in \(S_+M\), followed by taking its degree-\(d\) component, writes \(m\) as a finite sum of products \(s_e m_{d-e}\) with \(e>0\). Every module component has strictly smaller degree and is zero by induction. Thus \(M_d=0\) for every \(d\), so \(M=0\). This uses no finite generating set or Noetherian assumption.

For (2), let \(Q=M/N\), and let \(L\) be the image of \(N'\) in \(Q\). The original equation gives \(Q=S_+L\). Since \(L\) is a submodule, \(S_+L\subset L\subset Q\), hence \(Q=L=S_+Q\). The surjection \(N'\to Q\) is graded, so boundedness below of \(N'\) passes to \(Q\). Part (1) gives \(Q=0\), or \(M=N\).

For (3), if \(\varphi:N\to M\) has surjective reduction modulo \(S_+\), then \(Q=M/\operatorname{Im}\varphi\) satisfies \(Q=S_+Q\). It is a graded quotient of bounded-below \(M\), so (1) gives \(Q=0\). For (4), assign \(d_i=\deg(x_i)\) to every nonzero generator and any specified degree to a zero generator. The original degree-zero map \(\bigoplus_i S(-d_i)\to M\), \((s_i)\mapsto\sum_i s_i x_i\), has surjective reduction, so (3) applies. If the generating list is empty, its reduction condition is \(M/S_+M=0\), already covered by (1).

Boundedness cannot simply be discarded. For \(S=k[t]\), \(\deg(t)=1\), and the original graded module \(M=k[t,t^{-1}]\), one has \(S_+M=tM=M\ne0\), with nonzero components in arbitrarily negative degrees. The map \(0\to M\) becomes surjective modulo \(S_+\) but is not surjective. Thus the stated weaker hypothesis has a necessary role in the proof. No broader classification is asserted.

## Integral-closure wording

Source: `lemma-integral-closure-graded`, lines 13307–13355; report `OCC-01375`. The ring \(C\) consists of elements of \(S[t,t^{-1}]\) integral over the image of \(R[t,t^{-1}]\). The conventional expression is therefore “the integral closure of \(R[t,t^{-1}]\) in \(S[t,t^{-1}]\)”. This corrects the description of the base and ambient ring; it does not assert that the original author's intended construction was different.

With the source's degree-zero variable \(t\), the displayed ring automorphism sends \(\sum_j s_j\) to \(\sum_j t^j s_j\) on homogeneous components and fixes \(t\). Its inverse sends each \(s_j\) to \(t^{-j}s_j\) and again fixes \(t\). Applying the two maps to each generator gives the identity. The analogous maps on \(R[t,t^{-1}]\) commute with the given structural homomorphism, so applying the automorphism to any monic integral equation gives another monic equation over the same base. Thus it preserves exactly the described \(C\).

The later descent in the source is also valid: for \(m>i>0\), the quotient by \(t^m-t^i-1\) is free with basis \(1,t,\ldots,t^{m-1}\) over its coefficient ring, by division by this monic polynomial. In that quotient \(t(t^{m-1}-t^{i-1})=1\), so adjoining \(t^{-1}\) does not change the quotient. The inclusion of the original coefficient ring is injective, since a nonzero multiple of the monic degree-\(m\) polynomial cannot be a nonzero constant. The finite base extension and integral transitivity used at lines 13348–13352 therefore return an actual monic equation for the original \(s_i\) in \(S\). No factor or coefficient-ring map is discarded.

## Proper homogeneous prime test

Source: lines 13369–13380. The printed test needs the ideal to be **proper**. The whole ring satisfies the implication about products of homogeneous elements but is not a prime ideal.

Here is the exact test, also valid for a commutative \(\mathbf Z\)-graded ring. If a proper homogeneous ideal \(J\) has the property that a product of homogeneous elements belongs to \(J\) only when one factor belongs to \(J\), then \(S/J\) has no zero divisors. Indeed, two nonzero elements of \(S/J\) have finite homogeneous supports. Let their highest nonzero components have degrees \(a\) and \(b\). The degree-\(a+b\) component of the product is precisely the product of those two components: any term of lower degree in one factor cannot be paired with a degree exceeding the other factor's maximum. That component is nonzero by the homogeneous-product property. Thus the quotient is a nonzero domain and \(J\) is prime. The converse follows directly from primality. The minimal proposed wording inserts “proper”.

This also supplies the precise input to the source's \(\mathbf Z\)-graded localization argument at lines 13410–13437. For a prime \(\mathfrak p_0\subset S_0\), \(I=\mathfrak p_0S\) is homogeneous, and taking degree zero gives \(I\cap S_0=\mathfrak p_0\). Its radical is homogeneous: in the quotient by any homogeneous ideal, if \(z=\sum z_j\) is nilpotent, its highest component is nilpotent by taking the highest degree of a power. Subtract that component and continue through its finite support. The subtraction remains nilpotent because a sum of two commuting nilpotents is nilpotent, as the binomial expansion shows. Hence every component belongs to the radical.

Write \(f\in S_d\), \(d>0\), for the actual homogeneous unit. For homogeneous \(a,b\) with \(ab\in\sqrt I\), choose \(N\geq1\) such that \((ab)^N\in I\). Then

\[
\left(a^{Nd}/f^{N\deg(a)}\right)
\left(b^{Nd}/f^{N\deg(b)}\right)\in I\cap S_0=\mathfrak p_0.
\]

One factor belongs to \(\mathfrak p_0\), so \(a\in\sqrt I\) or \(b\in\sqrt I\). Also \(\sqrt I\cap S_0=\mathfrak p_0\), making \(\sqrt I\) proper. The corrected prime test proves it is prime. Conversely, for a homogeneous prime \(\mathfrak p\) contracting to \(\mathfrak p_0\), any homogeneous \(a\in\mathfrak p\) has \(a^d/f^{\deg(a)}\in\mathfrak p_0\), so \(a\in\sqrt{\mathfrak p_0S}\). The reverse inclusion follows from \(\mathfrak p_0S\subset\mathfrak p\); thus the two prime correspondences are inverse. Negative degrees cause no problem because the original \(f\) is a unit. The source's open-image formula follows from \(a\notin\mathfrak p\) if and only if \(a^d/f^{\deg(a)}\notin\mathfrak p_0\), and homogeneity handles the finite sum of components. This explains why the properness correction is compatible with the receiving homeomorphism, without replacing that proof in a translation.

## Degree-zero localization wording

Source: lines 13402–13408; report `OCC-01376`. “Submodule” is a single word. Its scalar ring remains the explicitly specified \(S_{(f)}\). This copyedit does not assert that the degree-zero part is an \(S_f\)-submodule, which need not be true.

## Homogeneous core of a prime

Source: `lemma-smear-out`, lines 13650–13667; reports `OCC-00375` and `OCC-01377`. Let \(\mathfrak q\) be the ideal generated by the homogeneous elements of the original prime \(\mathfrak p\). Every generator is in \(\mathfrak p\), so \(\mathfrak q\subset\mathfrak p\), making \(\mathfrak q\) proper. If homogeneous \(f,g\) satisfy \(fg\in\mathfrak q\), then \(fg\in\mathfrak p\), so one factor is in \(\mathfrak p\). That homogeneous factor is a generator of \(\mathfrak q\). The proper homogeneous prime test just proved shows that \(\mathfrak q\) is prime. The two small corrections reverse the printed containment and supply the missing verb “is”.

In the receiving minimal-prime lemma, a minimal prime \(\mathfrak p\) contains the prime \(\mathfrak q\), so minimality gives equality and hence homogeneity. For a homogeneous ideal \(I\), the same argument in the graded quotient \(S/I\) applies to the prime \(\mathfrak p/I\) minimal over zero. Its inverse image \(\mathfrak p\) is homogeneous. Report `OCC-01378` corrects only the sentence fragment “The second because” to “The second follows because”; the source already uses the correct containment in this receiving argument.

## Negative degrees in the finite generator list

Source: `lemma-dehomogenize-finite-type`, lines 13685–13727. Keep the original ring generators \(f_1,\ldots,f_n\), their degrees \(a_i\geq0\), the original homogeneous denominator \(f\) of degree \(d>0\), and module generators \(x_j\) of arbitrary integer degrees \(b_j\). The final finite generator list needs a convention when its resulting exponent \(e\) is negative. For \(S=k[t]\), \(f=t\), and \(M=S(1)\) with generator \(x\) of degree \(-1\), that list forces \(e=-1\), although \(M_{(f)}\ne0\) and is generated by \(tx\). Reading the list as requiring only nonnegative \(e\) would incorrectly give an empty list.

For an original monomial fraction
\(f_1^{E_1}\cdots f_n^{E_n}x_j/f^e\) of degree zero, initially with \(e\geq0\), write \(E_i=q_i d+r_i\), \(0\leq r_i<d\), and retain
\(e_0=e-\sum_i q_i a_i\). The exact identity in the original localization is

\[
\frac{f_1^{E_1}\cdots f_n^{E_n}x_j}{f^e}
=\left(\prod_i\left(\frac{f_i^d}{f^{a_i}}\right)^{q_i}\right)
\frac{f_1^{r_1}\cdots f_n^{r_n}x_j}{f^{e_0}},
\qquad de_0=\sum_i r_i a_i+b_j.
\]

Each factor in parentheses belongs to the original \(S_{(f)}\). If \(e_0<0\), the last term means the actual element \(f^{-e_0}f_1^{r_1}\cdots f_n^{r_n}x_j\) with denominator 1; its degree is zero by the displayed equality. All factors are retained. There are at most \(m d^n\) choices of \((j,r_1,\ldots,r_n)\), and for each choice the equation determines at most one integral \(e_0\). Expanding a homogeneous numerator in the original finite generators gives a finite \(R\)-linear combination of these fractions, so the list generates \(M_{(f)}\). This proves the asserted finiteness and the explicit bound, including an empty module generating list. A zero localization gives the zero module and satisfies the same bound. The minimal proposed clarification states the negative-exponent convention beside the list; it does not change the module or its grading.

## Positive-degree homogenization and the original base ring

Source: `lemma-homogenize`, lines 13729–13769; reports `OCC-01309`, `OCC-00376`, `OCC-01379`, and `OCC-01380`. Keep the original presentation \(R'=P/I\), \(P=R[x_1,\ldots,x_n]\), and \(H=R[X_0,\ldots,X_n]\) with every \(X_i\) of degree 1. The printed minimal-degree homogenization fails to preserve \(S_0=R\): for \(R=\mathbf Z\), \(n=0\), and \(I=(2)\), it gives \(S=\mathbf Z[X_0]/(2)\), whose degree-zero ring is \(\mathbf Z/(2)\).

For every polynomial \(g=\sum_\alpha c_\alpha x^\alpha\), choose an integer \(D(g)\geq1\) at least as large as every total degree \(|\alpha|\) in its finite support. For the zero polynomial the empty support allows any specified positive integer. Define

\[
\widetilde g=\sum_\alpha c_\alpha
 X_0^{D(g)-|\alpha|}X_1^{\alpha_1}\cdots X_n^{\alpha_n}.
\]

This retains every coefficient and exponent, is homogeneous of its assigned degree \(D(g)\), and satisfies \(\widetilde g(1,x_1,\ldots,x_n)=g\). The zero polynomial is homogeneous of the assigned degree without assigning an intrinsic polynomial degree to zero. Set \(\widetilde I=(\widetilde g:g\in I)\), \(S=H/\widetilde I\), and let \(f\) be the image of \(X_0\). All generators of \(\widetilde I\) have positive degree, so every homogeneous part of any product used to generate this ideal has positive degree. Thus \(\widetilde I\cap H_0=0\), and the original structural map gives \(S_0=R\), even when \(R\to R'\) is not injective.

There are exact inverse graded ring maps

\[
H_{X_0}\longrightarrow P[t,t^{-1}],\quad X_0\mapsto t,\quad X_i\mapsto t x_i,
\]
\[
P[t,t^{-1}]\longrightarrow H_{X_0},\quad t\mapsto X_0,\quad x_i\mapsto X_i/X_0,
\]

where \(P\) has degree zero and \(t\) has degree 1. Each composite fixes the original coefficients, variables, and the inverse variable. Under these maps \(\widetilde g\) becomes \(t^{D(g)}g\). Since that displayed power is a unit after localization, the localized ideal generated by all \(\widetilde g\) is exactly \(I P[t,t^{-1}]\). Passing to quotients gives \(S_f\cong R'[t,t^{-1}]\), and taking degree zero gives the original dehomogenization map \(S_{(f)}\cong R'\), \(X_i/X_0\mapsto x_i\). This includes \(R'=0\) and a zero image of \(f\). The ring \(S\) remains generated by the original finite list of degree-one variable images over \(R\).

For the module, choose a presentation with \(r\geq1\),

\[
M=(R')^{\oplus r}/\sum_{j\in J}R'k_j,\qquad
k_j=(k_{1j},\ldots,k_{rj}).
\]

Every finite module admits this choice; for the zero module one may use \(r=1\). Choose actual polynomial lifts \(h_{ij}\in P\) mapping to the original \(k_{ij}\in R'\). Assign positive homogenization degrees \(d_{ij}\) as above, including zero entries. Let \(d_j=\max_{1\leq i\leq r}d_{ij}\), and define the original presentation column with its corrected, now defined coefficients

\[
K_{ij}=X_0^{d_j-d_{ij}}\widetilde h_{ij},\qquad
N=\operatorname{Coker}\left(\bigoplus_{j\in J}S(-d_j)
 \xrightarrow{(K_{ij})} S^{\oplus r}\right).
\]

Every exponent is nonnegative and every column has its specified degree \(d_j\), so the map has degree zero with the original twist convention. The module \(N\) is finite because it is a quotient of \(S^{\oplus r}\); the set \(J\) need not be finite. Under \(S_f\cong R'[t,t^{-1}]\), the coefficient \(K_{ij}\) becomes \(t^{d_j}k_{ij}\). The degree-zero generator of \((S(-d_j))_f\) is \(t^{-d_j}\) times its original basis element, which has degree \(d_j\). The induced degree-zero matrix therefore has entries exactly \(k_{ij}\), with both displayed powers retained and multiplied to 1.

Localization preserves cokernels by the numerator-and-denominator definition. Taking degree zero preserves cokernels of degree-zero maps: a homogeneous degree-zero element in the image is the image of the degree-zero component of any preimage. Taking degree zero also commutes with the direct sum, since every element has finite support. Consequently the localized degree-zero cokernel is exactly
\((R')^{\oplus r}/\sum_j R'k_j=M\). This proves the specified \(R'\)-linear isomorphism \(N_{(f)}\cong M\), together with every asserted property of the corrected construction. The other two reports insert the missing “be” and correct “denote by”. These changes and the polynomial-lift choice are linked to the original passage, not attributed silently to the source author.

## Noetherian and numerical wording

Source: lines 13812–13830. Report `OCC-00377` inserts the missing comma in \(S_0[X_1,\ldots,X_n]\). A nearby copyedit changes “sufficient large” to “sufficiently large”. Neither changes a hypothesis, coefficient group, or the integer-valued binomial basis.

## Nilpotence induction in the Hilbert proof

Source: `proposition-graded-hilbert-polynomial`, lines 13889–13944; report `OCC-00378`. In the inner induction with least positive \(r>1\) satisfying \(x^rM=0\), take the actual graded submodule \(M'=xM\) and quotient \(M''=M/xM\). The maps are its inclusion and quotient map, giving the short exact sequence used by the source. The module \(M'\) is finite, generated by the products of \(x\) with any finite generating list of \(M\); \(M''\) is a finite quotient. The degrees are inherited, so taking each degree is exact. One has \(x^{r-1}M'=x^rM=0\) and \(xM''=0\). Their least positive annihilating exponents therefore satisfy \(r'\leq r-1<r\) and \(r''=1<r\), including zero modules under the least-positive convention. This supplies the previously unnamed objects and exponents without changing the proof's induction.

The outer reduction retains its original Noetherian hypothesis. The ascending chain \(\ker(x:M\to M)\subset\ker(x^2)\subset\cdots\) stabilizes because \(M\) is Noetherian. Its union is the graded submodule \(T\) of all \(x\)-power torsion and equals \(\ker(x^N)\) for some \(N\). Thus \(x^NT=0\). If \(xm\in T\), then \(x^{N+1}m=0\), so stability gives \(m\in T\). Hence multiplication by \(x\) on \(M/T\) is injective, as required by the receiving exact degree sequence. No new assumption or replacement theorem is needed. In degree \(d\), its maps give exactly \([M_{d+1}]-[M_d]=[(M/xM)_{d+1}]\) after that reduction; the original binomial antidifference step applies with its original sign and shift.

## Hilbert bound notation

Source: `lemma-quotient-smaller-d`, lines 13964–13982; report `OCC-00379`. The proposed change replaces the literal `>>` with `\gg`, preserving “sufficiently large”. Multiplication by the original nonzero homogeneous \(f\) in the polynomial domain is injective, so its degree-\(n\) image has the original dimension \(\binom{n-e-1+d}{d-1}\). Subtracting this lower bound for \(\dim I_n\) from \(\binom{n-1+d}{d-1}\) gives the displayed upper bound. For \(d\geq2\), the two degree-\(d-1\) polynomials have the same leading coefficient \(1/(d-1)!\), so their difference has smaller degree; a nonnegative eventual dimension polynomial bounded by it also has smaller degree. For \(d=1\) the difference is zero. If the allowed nonzero ideal contains a degree-zero unit, the quotient is zero directly. For zero variables, a nonzero ideal of the field is the whole field and the quotient is again zero, without using a binomial coefficient with lower entry \(-1\). These boundary explanations remain editorial material.

## Reading and propagation limits

The other complete source units in this interval were read for their surrounding argument. In particular the Proj chart/localization formulas, the finite-type ring generator argument, and the receiving minimal-prime and Hilbert calculations were compared with the findings above. This is not a new certification of every omitted detail or of previously inserted FAC proofs. The original Veronese argument uses a positive number of positive-degree algebra generators; when that number is zero, \(S=S_0\) and its conclusion holds directly for every positive \(d\). That boundary explanation does not require expanding its translated proof. The periodic-polynomial remark is read in the preceding finite-module context. Broader combined-results synthesis and the short mathematical paper remain after the core correction work. Source from 13991 onward is not adjudicated by this batch.
