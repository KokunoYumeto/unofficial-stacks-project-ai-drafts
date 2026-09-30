# Openness of the flat locus: corrections and separate consequences

Source: Stacks Project authors, algebra.tex:33227–33514, authority a04446e57ec1fbc252a871afcec7752fb2807b14, file SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3. All six reports OCC-00659–OCC-00664 are reviewed. Source lookahead 33515–33550 has been read but is not adjudicated here. No earlier canonical correction overlaps this section.

Dependencies reread in the original TeX: 23495–23645, 24825–24970, and 28208–28296. The rank-zero correction and complete criterion proof in ALGEBRA_COMPLEX_EXACTNESS_NOTES_20260928.md, section “The exactness criterion with all rank-zero cases retained”, were reread. Use that proved criterion, including groups 572, 576 and 577, rather than repeating its earlier overclaim that every determinantal ideal is proper. The cited Buchsbaum–Eisenbud bibliography entry is human-source attribution, not a new claim to have read that paper. The preceding Noetherian approximation and flatness proofs remain the receiving dependencies.

All full arguments here are editorial supplements, not replacement translations. Source statements, formulas, matrix ranks, ideals, prime contractions, residue fields and localization denominators remain identifiable. No novelty is claimed.

## The nonempty zero locus and its exact equivalence

In lemma-CM-dim-finite-type the assertion of equality needs \(V(f_1,\ldots,f_i)\ne\varnothing\). For \(S=k[x]\), \(d=i=1\), \(f_1=1\), the zero locus is empty and has dimension strictly less than zero under the source convention. It satisfies the displayed upper bound but not the asserted equality. The regular-sequence conclusion over primes of that empty set is vacuous. A nonempty-zero-locus hypothesis repairs the dimension statement; it must be visible as a source correction.

Here is the complete proof and its converse. Let \(S\) be a finite-type, Cohen–Macaulay, equidimensional \(k\)-algebra of dimension \(d\), and let \(J=(f_1,\ldots,f_i)\) be proper. Then the following are equivalent:

1. \(\dim(S/J)\leq d-i\).
2. The original ordered sequence is regular in \(S_{\mathfrak q}\) for every \(\mathfrak q\in V(J)\).
3. \(S/J\) is Cohen–Macaulay and equidimensional of dimension \(d-i\).

For (1), every maximal ideal \(\mathfrak m\) containing \(J\) has \(\dim S_{\mathfrak m}=d\), by the source disjoint-decomposition result for Cohen–Macaulay finite-type algebras. The height theorem gives
\[
d-i\leq\dim(S_{\mathfrak m}/JS_{\mathfrak m})\leq\dim(S/J)\leq d-i.
\]
Thus equality holds throughout. The source characterization of parameter subsequences in a nonzero Cohen–Macaulay local module gives regularity of the specified \(f_1,\ldots,f_i\) and the Cohen–Macaulay quotient of dimension \(d-i\) at each such maximal ideal. If \(\mathfrak q\in V(J)\), choose a maximal ideal \(\mathfrak m\supset\mathfrak q\). Localizing the multiplication injections from \(S_{\mathfrak m}\) to \(S_{\mathfrak q}\) preserves them; the final quotient is nonzero because \(J\subset\mathfrak q\). This proves (2).

Conversely, (2) at those maximal ideals gives Cohen–Macaulay local quotients of dimension \(d-i\) by successive regular-element quotients. All local rings of \(S/J\) are localizations of these quotients, so the quotient is Cohen–Macaulay. Its equidimensional decomposition over the field, by the same source decomposition result, has components of the dimensions of its closed local rings, all equal to \(d-i\). It is nonzero since \(J\) is proper. This proves (3), which gives (1).

The source's “forms” is changed to “form”. The phrase “prime of \(V(J)\)” is understandable as a prime of the quotient defining that closed subset, so the suggested replacement of “of” is optional prose. It does not identify a mathematical defect.

For any field extension \(K/k\), the original sequence localized at a prime over \(V(J)\) stays regular: the relevant map from \(S_{\mathfrak q}\) to the localized base change is flat and local, and the final quotient remains nonzero by faithful flatness. This preserves the exact ordered sequence. No assertion is made about regularity at primes where its ideal is the unit ideal.

## Openness of the fibre regular-sequence condition

Retain the source finite-type map \(R\to S\), equidimensional Cohen–Macaulay fibres of dimension \(d\), and the elements \(f_1,\ldots,f_i\). At a prime \(\mathfrak q\in V(J)\) with contraction \(\mathfrak p\), let
\[
A=S_{\mathfrak q}/\mathfrak pS_{\mathfrak q},\qquad
r=\operatorname{trdeg}_{\kappa(\mathfrak p)}\kappa(\mathfrak q).
\]
If the sequence is regular in \(A\), successive regular quotients give \(\dim(A/JA)=\dim A-i\). The original point-dimension formula at 28222–28262 therefore gives
\[
\dim_{\mathfrak q}(S/R)=\dim A+r=d,\qquad
\dim_{\mathfrak q}((S/J)/R)=\dim(A/JA)+r=d-i.
\]
Upper semicontinuity of the source relative-dimension function on \(\operatorname{Spec}(S/J)\) provides a principal neighborhood \(D(g)\) of \(\mathfrak q\) on which its values are at most \(d-i\).

Fix any prime \(\mathfrak q'\in V(J)\cap D(g)\), with contraction \(\mathfrak p'\). The fibre \((S_g)\otimes_R\kappa(\mathfrak p')\) is nonempty because it contains that point. It remains Cohen–Macaulay and equidimensional of dimension \(d\): each surviving component is a nonempty open subset of an original \(d\)-dimensional finite-type component over the field. The closed subscheme defined by the original \(f_j\) is nonempty and has dimension at most \(d-i\), since every point in this quotient fibre satisfies the preceding bound. The corrected nonempty-locus lemma applies. It gives regularity at \(\mathfrak q'\), proving the required openness in \(V(J)\). Empty fibres elsewhere in this localization require no dimension or regularity assertion.

## Exact fibre complexes under the equidimensional hypothesis

The printed lemma-exact-on-fibres-open assumes Cohen–Macaulay fibres of a fixed dimension, without saying equidimensional, but its proof invokes the preceding lemma which does require equidimensionality. These hypotheses differ: over a field, \(k[x]\times k\) is Cohen–Macaulay of dimension one and has a zero-dimensional component. Merely inserting “equidimensional” would narrow the original claim. Instead this note first proves the restricted case needed for the following theorem, then proves the full original claim with weaker hypotheses after that theorem. This supplies a noncircular editorial repair and preserves the original statement.

For now assume \(R\) Noetherian, \(S\) finite type and flat over \(R\), and all nonempty fibres Cohen–Macaulay and equidimensional of dimension \(d\). Retain the actual finite free complex
\[
0\longrightarrow S^{n_e}\xrightarrow{\varphi_e}\cdots
\xrightarrow{\varphi_2}S^{n_1}\xrightarrow{\varphi_1}S^{n_0}.
\]
Exactness here and below means exactness in the positive homological degrees, as in the cited source criterion; no surjectivity at degree zero is required.

If the exact-fibre locus is empty, openness is immediate. At a point \(\mathfrak q\) in that locus, with contraction \(\mathfrak p\), the source local complex criterion at 23528–23551 applies to \(R_{\mathfrak p}\to S_{\mathfrak q}\): all terms are \(R_{\mathfrak p}\)-flat and the closed-fibre complex is exact. Thus the original complex is exact at \(\mathfrak q\). Its positive homology modules are finite over Noetherian \(S\), so finitely many annihilators of their generating sets give \(g\notin\mathfrak q\) killing them all. Localize at their product, retaining the original maps.

For \(1\leq j\leq e\) set, with all terms and signs retained,
\[
r_j=n_j-n_{j+1}+\cdots+(-1)^{e-j}n_e,\qquad
I_j=I_{r_j}(\varphi_j).
\]
Positive exactness at every local ring and the corrected source rank criterion show that these \(r_j\) are nonnegative and all minors of size \(r_j+1\) vanish. They vanish in the ring itself because an element zero in all prime localizations is zero. Use the convention \(I_0(\varphi_j)=S\); rank-zero maps do not have proper determinantal ideals.

At \(\mathfrak q\), for each \(j\), either \((I_j)_{\mathfrak q}=S_{\mathfrak q}\), an open condition, or its image in \(A=S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}\) contains a regular sequence of length \(j\). In the second case choose actual lifts \(a_l/s_l\in(I_j)_{\mathfrak q}\), \(s_l\notin\mathfrak q\), of that ordered sequence. Localize at \(\prod_l s_l\). Each original lift is now an element of \(I_j\) in this ring, with its exact fraction retained. This is the missing localization before treating these elements as global equations.

By the preceding regular-sequence openness lemma, the sequence is fibrewise regular on a neighborhood of \(\mathfrak q\) within its zero locus. The complement of that neighborhood is closed in the zero locus, hence closed in the ambient spectrum; shrink once more to avoid it. Outside the zero locus at least one chosen element is invertible, so \(I_j\) is the unit ideal. Inside it, \(I_j\) contains the required fibre regular sequence. For each fibre local ring these alternatives, together with the already-vanishing larger minors, give exactly the original ranks and grade conditions: a regular element in a positive-size minor ideal is nonzero, so rank cannot drop; a unit minor also cannot vanish. Apply the corrected exactness criterion. Taking the finite product of all these localization elements proves openness near \(\mathfrak q\). The complex with no positive-degree terms has the whole spectrum as its locus.

## Openness of flatness with the zero and one variable cases

Retain the original finitely presented \(R\)-algebra \(S\), finitely presented \(S\)-module \(M\), and a point \(\mathfrak q\) where \(M_{\mathfrak q}\) is \(R\)-flat. Let \(\mathfrak p\) be its contraction. The preceding global Noetherian approximation of the entire presentation gives \(R_\lambda,S_\lambda,M_\lambda\), with exact global tensor isomorphisms for \(S\) and \(M\). Localize those stage rings at the contractions of \(\mathfrak p,\mathfrak q\). Eventual flatness from the previous section supplies a stage at which \((M_\lambda)_{\mathfrak q_\lambda}\) is \((R_\lambda)_{\mathfrak p_\lambda}\)-flat, equivalently \(R_\lambda\)-flat. A principal flat neighborhood at that stage pulls back, by the actual module tensor isomorphism and base change, to the requested neighborhood. Thus it is enough to prove the assertion when \(R,S\) are finite type over \(\mathbf Z\), hence Noetherian.

Choose the original surjection \(P=R[x_1,\ldots,x_n]\to S\), and let \(\widetilde{\mathfrak q}\) be the inverse image of \(\mathfrak q\). Regard the same module \(M\) through that surjection. It is finite, hence finitely presented, over Noetherian \(P\). Its localization at \(\widetilde{\mathfrak q}\) is the original \(M_{\mathfrak q}\). A principal element of \(P\) producing flatness maps to an element of \(S\) outside \(\mathfrak q\) and gives exactly the same module localization. This proves the legitimacy of the source polynomial presentation reduction without replacing the original quotient object in the result. In the following polynomial calculation write \(S=P\), as in the source.

If \(n=0\), \(S=R\) and \(M_{\mathfrak q}\) is a finite flat module over the Noetherian local ring \(R_{\mathfrak q}\), hence free, including rank zero. A finite basis and its inverse matrix lift after a localization, and the finitely many resulting errors are killed by another element outside \(\mathfrak q\). More explicitly, lift basis vectors to \(M_g\), let \(R_g^r\to M_g\) be the induced map, and kill the finite kernel and cokernel, which vanish at \(\mathfrak q\), by a product of annihilators outside \(\mathfrak q\). This gives a finite free principal neighborhood, proving this case.

Assume \(n\geq1\) and choose the original finite-free resolution of \(M\). Define
\[
K_1=\ker(F_0\to M),\qquad
K_n=\ker(F_{n-1}\to F_{n-2})\quad(n\geq2).
\]
The source's displayed formula alone has an undefined \(F_{-1}\) when \(n=1\); the preceding \(n=0\) case also cannot be put into that formula. The two boundary repairs preserve the original formula for every \(n\geq2\).

At \(\mathfrak q\), all these syzygies are \(R\)-flat by induction from \(M_{\mathfrak q}\) and the short exact sequences with the \(R\)-flat finite free terms. Thus tensoring the original truncated resolution with \(\kappa(\mathfrak p)\) remains exact there. The fibre local ring
\[
A=S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}
\]
is a localization of a polynomial ring in \(n\) variables over \(\kappa(\mathfrak p)\); its global dimension is at most \(n\), not necessarily equal to \(n\). For instance the generic point of a polynomial line over a field gives a field of global dimension zero. Dimension shifting along the exact fibre resolution gives
\(\operatorname{Ext}_A^1((K_n)_{\mathfrak q}/\mathfrak p(K_n)_{\mathfrak q},T)
\cong\operatorname{Ext}_A^{n+1}(M_{\mathfrak q}/\mathfrak pM_{\mathfrak q},T)=0\)
for every \(A\)-module \(T\). Hence that finite fibre syzygy is projective, and therefore free over local \(A\).

If \((K_n)_{\mathfrak q}=0\), it is free of rank zero. Otherwise the source free-fibre-flat-free lemma at 23507–23524 applies and makes it free over \(S_{\mathfrak q}\). Since \(K_n\) is finite over Noetherian \(S\), the same finite-presentation spreading argument gives \(g\notin\mathfrak q\) for which \((K_n)_g\) is finite free. Retain its basis, the original differential into \(F_{n-1}\), and all other original matrices.

The fibres of this localized polynomial algebra are Cohen–Macaulay and equidimensional of dimension \(n\) whenever nonempty. Apply the restricted exact-fibre openness lemma just proved to
\[
0\longrightarrow (K_n)_g\longrightarrow (F_{n-1})_g
\longrightarrow\cdots\longrightarrow(F_0)_g.
\]
It has an exact fibre at \(\mathfrak q\), so a further principal localization makes its fibres exact everywhere. At every remaining prime the local complex criterion then gives \(R\)-flatness of its degree-zero cokernel, which is the original \(M\). For \(n=1\) this cokernel is that of \(K_1\to F_0\), equal to that of the original \(F_1\to F_0\) because both have the same image. Since flatness can be checked at all prime localizations of the module's acting algebra, \(M_g\) is \(R\)-flat. This proves the theorem without using the unproved, non-equidimensional instance of the preceding lemma.

## Exact-fibre openness without Cohen–Macaulay assumptions

Keep \(R\) Noetherian and \(S\) a finite-type \(R\)-algebra. More generally than the printed lemma, let
\[
0\longrightarrow F_e\longrightarrow\cdots\longrightarrow F_0
\]
be a finite complex of finite \(S\)-modules, each flat over \(R\); neither freeness over \(S\), flatness of \(S/R\), nor any Cohen–Macaulay or fibre-dimension condition is needed. Put \(C=\operatorname{coker}(F_1\to F_0)\), taking \(C=F_0\) when \(e=0\), and let \(H_j\) be its positive homology modules.

The exact-fibre locus is precisely
\[
E=
\left(\operatorname{Spec}S\setminus\bigcup_{j=1}^e\operatorname{Supp}_S H_j\right)
\cap
\{\mathfrak q:C_{\mathfrak q}\text{ is flat over }R\}.
\]
If the fibre is exact at \(\mathfrak q\), the source local complex criterion gives both positive exactness of the original localized complex and \(R_{\mathfrak p}\)-flatness of \(C_{\mathfrak q}\); this is equivalent to \(R\)-flatness. Conversely assume those two properties. Beginning with \(0\to K_1\to(F_0)_{\mathfrak q}\to C_{\mathfrak q}\to0\), flatness of the two right modules proves flatness of \(K_1\) and exactness after every \(R\)-module tensor. Continue upward using positive exactness. Every syzygy is \(R\)-flat and every short exact sequence stays exact under tensor. Tensoring with \(\kappa(\mathfrak p)\) proves exactness of the fibre complex. This also proves the assertion for all zero terms and for \(e=0\).

All \(H_j\) are finite over Noetherian \(S\), so their supports are closed. The module \(C\) is finitely presented, and the map \(R\to S\) is finitely presented because it is finite type over Noetherian \(R\). The now-proved flat-locus theorem makes its flat locus open. This proves openness of \(E\), establishes the original printed exact-fibre lemma with its original hypotheses, and removes all its Cohen–Macaulay and dimension restrictions. The proof order is: equidimensional restricted lemma, flat-locus theorem, then this general lemma; there is no circular dependence.

On any open part of \(E\), the augmented complex ending in \(C\) is exact and universally exact over \(R\), by the same syzygy argument. In particular it stays exact after every \(R\)-module tensor, not only on residue-field fibres.

There is also an exact base-change identity for the fibre locus itself, without restrictions on the new base. For any map \(R\to R'\), put \(S'=S\otimes_R R'\) and use the original base-changed complex. At a prime \(\mathfrak q'\subset S'\), let \(\mathfrak p'\subset R'\), \(\mathfrak q\subset S\), \(\mathfrak p\subset R\) be its contractions. The map
\[
A=S_{\mathfrak q}\otimes_R\kappa(\mathfrak p)
\longrightarrow
B=S'_{\mathfrak q'}\otimes_{R'}\kappa(\mathfrak p')
\]
is a local flat map: it is the localization induced by the field extension \(\kappa(\mathfrak p)\to\kappa(\mathfrak p')\) on the original fibre. The contraction of its maximal ideal is the maximal ideal of \(A\), so it is faithfully flat. The new fibre complex is the old localized fibre complex tensor \(B\) over \(A\). Exactness therefore ascends and descends, giving \(E'=(\operatorname{Spec}S'\to\operatorname{Spec}S)^{-1}(E)\). This equality does not require Noetherianity of \(R'\) or flatness of \(R'/R\).

## The flat open and its radical ideal under base change

For the original arbitrary \(R\), finitely presented \(R\)-algebra \(S\) and finitely presented \(S\)-module \(M\), let \(U\) be the flat locus of the theorem. Define the actual ideal
\[
J_M=\{s\in S:M_s\text{ is flat over }R\}
    =\{s\in S:D(s)\subset U\}.
\]
The equality holds by the flat-localization criterion. This is a radical ideal: \(0\) belongs to it; \(D(as)\subset D(s)\); \(D(s+t)\subset D(s)\cup D(t)\); and \(D(s^m)=D(s)\) for every positive integer \(m\). Consequently
\[
U=D(J_M),\qquad
J_M=\bigcap_{\mathfrak q\notin U}\mathfrak q,
\]
with empty intersection equal to \(S\). No finite-generation or quasi-compactness assertion is needed.

For a flat base change \(R\to R'\), put \(S'=S\otimes_R R'\), \(M'=M\otimes_R R'\), and let \(U'\) be its \(R'\)-flat locus. Then \(U'\) is exactly the inverse image of \(U\), and
\[
J_{M'}=\sqrt{J_M S'}.
\]
Forward inclusion of the loci holds by flat base change and localization, even when \(R'\) is not flat over \(R\). For the converse under flatness, take a prime \(\mathfrak q'\subset S'\) over \(\mathfrak q\) and write \(A=S_{\mathfrak q}\), \(B=S'_{\mathfrak q'}\). The map \(A\to B\) is local, flat and faithfully flat. If \(M'_{\mathfrak q'}\) is \(R'\)-flat, it is \(R\)-flat because \(R'\) is \(R\)-flat. For any injection \(T_1\to T_2\) of \(R\)-modules, the kernel of
\(M_{\mathfrak q}\otimes_R T_1\to M_{\mathfrak q}\otimes_R T_2\)
is an \(A\)-module. Tensoring it with flat \(B\) identifies it with the zero kernel for the \(R\)-flat module \(M_{\mathfrak q}\otimes_A B=M'_{\mathfrak q'}\). Faithfulness makes the original kernel zero. Thus \(M_{\mathfrak q}\) is \(R\)-flat. The radical-ideal identity follows from equality of the corresponding basic-open unions.

For arbitrary, possibly nonflat base change only the inclusion
\(\sqrt{J_M S'}\subset J_{M'}\) follows in general. It can be strict: take \(R=S=k[t]\), \(M=R/(t)\), and \(R'=k=R/(t)\). The original flat locus is \(D(t)\), since the module is zero there and is not flat at a prime containing \(t\): multiplication by the nonzerodivisor \(t\) becomes zero on a nonzero module. After base change \(M'=k\) is free everywhere. Thus \(J_M=(t)\), \(J_MS'=0\), and \(J_{M'}=k\). This also distinguishes ordinary flat-locus base change from the unrestricted exact-fibre-locus identity above.

## Propagation and reading boundary

The nonempty-locus repair is received by the relative regular-sequence proof only at fibres with an actual point of the zero locus. The earlier rank-zero correction is received by the determinantal argument with \(I_0=S\) intact. The equidimensionality gap is repaired editorially through the noncircular proof order above, preserving the original full statement. The syzygy boundary repairs retain the original formula for \(n\geq2\), and the rank-zero syzygy needs no nonzero-module citation.

The three consequence groups give the full dimension/regularity/quotient equivalence, exact-fibre openness with much weaker hypotheses and unrestricted fibre-locus base change, and the actual flat-open radical ideal with exact flat-base-change law and a counterexample outside that hypothesis. These receive the preceding flatness results rather than replacing their source formulations.

The query “openness flat locus” has two research routing hits and no local-work hits. Neither was read as mathematical evidence; the first is indexed only by PDF content and no PDF fallback was used. Seven earlier external source records retain their prior bounded coverage. Broader synthesis and novelty review remain after the core task.
