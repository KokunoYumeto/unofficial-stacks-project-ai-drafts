# Algebra: ascending properties, with the original local rings retained

This is an editorial verification of the Stacks Project authors' argument, not a replacement translation or a novelty claim. The authority is commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, `algebra.tex` lines 46293–46632, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`. The [original source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L46293) attributes the module depth formula to Grothendieck and Dieudonné, EGA IV, Proposition 6.3.1. The preceding normality criterion retains its EGA IV, Theorem 5.8.6 attribution. Those original attributions are preserved; no new reading of EGA is claimed here.

The source statement, hypotheses, notation, finite-depth induction, localization maps, and finite-type models remain identifiable. The long arguments below belong in linked editorial material. Four existing correction units, MC-STK-ERR-0725–0728, are retained. Only two additional copyedits are proposed. One is an explicit refinement of the postimage of MC-STK-ERR-0725-OP1, whose original receipt is immutable.

## The module depth formula, including zero modules

Let \((R,\mathfrak m_R)\to(S,\mathfrak m_S)\) be the original local homomorphism of Noetherian local rings. Let \(M\) be a finite \(R\)-module and \(N\) a finite \(S\)-module, flat over \(R\). Put \(C=S/\mathfrak m_RS\). All three depths in the original assertion are taken over their stated rings:
\[
 \operatorname{depth}_S(M\otimes_RN)
 =\operatorname{depth}_R(M)+\operatorname{depth}_C(N/\mathfrak m_RN).
\]
Depth of the zero module is \(+\infty\), by the source definition at 17765–17776, and addition takes place in the nonnegative extended integers. If \(M=0\), the left side and the first summand are infinite. If \(N=0\), the left side and the second summand are infinite. These cases prove the formula directly. They must precede induction on a finite integer; no subtraction from infinity is used. This is the substantive content of retained unit 0725.

Assume henceforth that both modules are nonzero. Nakayama over \(S\), with \(\mathfrak m_RS\subseteq\mathfrak m_S\), gives \(N/\mathfrak m_RN\ne0\). Nakayama over \(R\) gives a nonzero finite-dimensional vector space \(M/\mathfrak m_RM\cong (R/\mathfrak m_R)^r\), with \(r\ge1\). Tensoring its quotient map with \(N\) gives a surjection
\[
 M\otimes_RN\longrightarrow
 (M/\mathfrak m_RM)\otimes_RN
 \cong (N/\mathfrak m_RN)^r\ne0.
\]
Thus the left module is nonzero as well. All these modules are finite over their respective Noetherian local rings. Their depths are finite: a regular sequence on a nonzero finite module has length at most its support dimension, and a Noetherian local ring has finite dimension, bounded by a finite generating set for its maximal ideal. Denote by \(n\) the right-hand sum. The additional copyedit inserts the missing word “by” in this designation, without altering the preceding zero-module correction.

For \(n=0\), the depth-zero associated-prime criterion supplies the original \(z\in M\), with annihilator \(\mathfrak m_R\), and \(\bar y\in N/\mathfrak m_RN\), with annihilator \(\mathfrak m_S/\mathfrak m_RS\) in \(C\). The map
\[
 R/\mathfrak m_R\longrightarrow M,\qquad \bar r\longmapsto rz
\]
is injective. Flatness of \(N\) over \(R\) therefore makes
\[
 N/\mathfrak m_RN\longrightarrow M\otimes_RN,
 \qquad \bar v\longmapsto z\otimes v
\]
injective; this formula is independent of the chosen lift of \(\bar v\). It is \(S\)-linear. If \(y\) is a lift of \(\bar y\), the annihilator of \(z\otimes y\) is consequently exactly \(\mathfrak m_S\). The target has depth zero.

Suppose that \(n>0\) and the fibre depth is positive. Choose the original \(f\in\mathfrak m_S\) whose image is a nonzerodivisor on \(N/\mathfrak m_RN\). Apply the source's fibre-injectivity lemma, 23423–23477, to multiplication by \(f:N\to N\). It is injective, and \(N/fN\) is flat over \(R\). To recall why the latter conclusion is available, the lemma first lifts injectivity modulo \(\mathfrak m_R\) through all \(\mathfrak m_R^j\) using
\[
 (N/\mathfrak m_RN)\otimes_{R/\mathfrak m_R}
 (\mathfrak m_R^j/\mathfrak m_R^{j+1})
\]
and flatness of the target. The tensor maps are injective over the residue field. Krull intersection for the finite \(S\)-module kills the intersection of the kernels. The same argument after quotienting by any ideal \(I\subset R\) proves injectivity modulo \(I\). The exact sequence
\[
 0\to\operatorname{Tor}_1^R(N/fN,R/I)
 \to N/IN\xrightarrow{f}N/IN
\]
then gives flatness of the cokernel by the ideal criterion. This preserves the actual multiplication map and the original ideals.

Nakayama shows that \(N/fN\ne0\). The quotient of the original fibre is
\[
 (N/fN)/\mathfrak m_R(N/fN)
 =N/(f,\mathfrak m_R)N.
\]
The depth-drop lemma gives
\[
 \operatorname{depth}_C(N/\mathfrak m_RN)
 =\operatorname{depth}_C(N/(f,\mathfrak m_R)N)+1.
\]
Depth here can equally be computed over the further quotient by \(\bar f\): all maximal-ideal actions on the module are the same, and regular sequences lift and descend through that quotient. The new right-hand sum is exactly \(n-1\), so induction applies to \(M,N/fN\). Flatness of \(N/fN\) makes the tensor sequence
\[
 0\to M\otimes_RN\xrightarrow{1_M\otimes f}M\otimes_RN
 \to M\otimes_R(N/fN)\to0
\]
exact. Its first map is the original scalar multiplication by \(f\), its cokernel is the displayed quotient, and the depth-drop lemma gives
\[
 \operatorname{depth}_S(M\otimes_RN)
 =\operatorname{depth}_S(M\otimes_R(N/fN))+1
 =\operatorname{depth}_R(M)
   +\operatorname{depth}_C(N/(f,\mathfrak m_R)N)+1.
\]
This is the required formula with every summand retained.

If the fibre depth is zero and \(n>0\), choose the original \(f\in\mathfrak m_R\) regular on \(M\). Flatness of \(N\) preserves the exact sequence
\[
 0\to M\otimes_RN\xrightarrow{f}M\otimes_RN
 \to (M/fM)\otimes_RN\to0.
\]
Both \(M/fM\) and the tensor cokernel are nonzero by the preceding Nakayama and tensor-quotient arguments. Now
\(\operatorname{depth}_R(M)=\operatorname{depth}_R(M/fM)+1\).
Induction for \(M/fM,N\), followed by depth drop over \(S\), proves
\[
 \operatorname{depth}_S(M\otimes_RN)
 =\operatorname{depth}_R(M/fM)
  +\operatorname{depth}_C(N/\mathfrak m_RN)+1
 =\operatorname{depth}_R(M)+\operatorname{depth}_C(N/\mathfrak m_RN).
\]
The two positive-depth branches exhaust the finite integer \(n>0\). Taking \(M=R,N=S\) proves the ring depth formula at 46373–46384.

## Cohen–Macaulay ascent and the original local fibre maps

For a flat local homomorphism of Noetherian local rings, the source dimension formula gives
\[
 \dim S=\dim R+\dim(S/\mathfrak m_RS).
\]
Its proof at 27420–27456 retains a chain of length \(d\) in the closed fibre and a chain of length \(e\) below \(\mathfrak m_R\). Going down lifts the latter below the first prime of the former. Strictness follows from distinct contractions. This gives a chain of length \(e+d\) in \(S\), and the previously proved dimension upper bound gives equality. Combined with depth addition, it gives the exact identity
\[
 \dim S-\operatorname{depth}S
 =\bigl(\dim R-\operatorname{depth}R\bigr)
 +\bigl(\dim(S/\mathfrak m_RS)
       -\operatorname{depth}(S/\mathfrak m_RS)\bigr).
\]
Both right-hand summands are nonnegative finite integers. Thus the left side vanishes exactly when both right-hand summands vanish. This proves the original Cohen–Macaulay equivalence. The proposed colon after “equivalent” is punctuation only.

For the subsequent global assertions, keep the original map \(\varphi:R\to S\), prime \(\mathfrak q\subset S\), and its inverse image \(\mathfrak p\subset R\). Set
\[
 A=R_{\mathfrak p},\qquad B=S_{\mathfrak q},\qquad
 F=S\otimes_R\kappa(\mathfrak p),\qquad C=B/\mathfrak pB.
\]
Write \(U=R\setminus\mathfrak p\). The map \(R\to B\) inverts \(U\), so it factors uniquely as \(A\to B\), sending \(r/u\) to \(\varphi(r)/\varphi(u)\); it is flat and local. There is an explicit isomorphism
\[
 F\xrightarrow{\sim}U^{-1}S/\mathfrak pU^{-1}S,
 \qquad s\otimes(\bar r/\bar u)\longmapsto
 \overline{s\varphi(r)/\varphi(u)}.
\]
Its inverse takes the class of \(s/\varphi(u)\) to \(s\otimes1/\bar u\). Balanced tensor relations and the quotient by \(\mathfrak p\) make both maps well-defined; on each displayed generator their composites are the identity. Let \(\bar{\mathfrak q}\) be the prime of this ring induced by \(U^{-1}\mathfrak q\). Then
\[
 F_{\bar{\mathfrak q}}\xrightarrow{\sim}C,
 \qquad
 \frac{\overline{s/\varphi(u)}}{\overline{t/\varphi(v)}}
 \longmapsto\overline{\frac{s\varphi(v)}{t\varphi(u)}}.
\]
Here \(t\notin\mathfrak q\), and \(u,v\notin\mathfrak p\), so every displayed denominator is invertible in the specified target. The inverse sends the class of \(s/t\in B\) to
\((s\otimes1)/(t\otimes1)\). Clearing these same invertible denominators verifies well-definedness, multiplicativity, additivity, and both inverse identities. This identifies the actual fibre localization, not a different field or local ring.

## Serre conditions, reducedness and normality in the Noetherian case

Assume the original Noetherian hypotheses and flatness. Write
\(a=\dim A\), \(c=\dim C\), \(b=\dim B\). The local fibre comparison just proved lets us apply the assumed fibre condition to \(C\). If the base and fibres satisfy \((S_k)\), for the original nonnegative integer \(k\), depth addition gives the source's full calculation
\[
 \begin{aligned}
 \operatorname{depth}B
 &=\operatorname{depth}C+\operatorname{depth}A\\
 &\ge\min(k,c)+\min(k,a)\\
 &=\min(2k,c+k,k+a,c+a)\\
 &\ge\min(k,b).
 \end{aligned}
\]
The middle equality distributes the two minima over all four sums; none is discarded. For the last inequality, the first three entries are at least \(k\) because \(k,a,c\ge0\), and the fourth is at least \(b\) by the dimension inequality (in fact equality). Thus every entry is at least \(\min(k,b)\), including \(k=0\). This proves \((S_k)\) for \(S\).

If the base and fibres satisfy \((R_k)\), take \(\mathfrak q\) with \(b\le k\). The exact dimension equality \(b=a+c\) forces \(a\le k,c\le k\), so \(A,C\) are regular. For completeness, the source regular-ascent argument at 27458–27480 chooses generators \(x_1,\ldots,x_a\) of the maximal ideal of \(A\), and lifts \(y_1,\ldots,y_c\in\mathfrak m_B\) of generators of the maximal ideal of \(C\). Any element of \(\mathfrak m_B\) is congruent modulo \(\mathfrak m_AB\) to a linear combination of the \(y_j\). Its difference is a combination of the images of the \(x_i\). Thus these \(a+c=b\) elements generate \(\mathfrak m_B\). The general inequality \(\dim B\le\dim_{\kappa(\mathfrak m_B)}\mathfrak m_B/\mathfrak m_B^2\), together with this generating set of size \(b\), gives equality and hence regularity of \(B\). Zero-sized parameter lists are permitted. This proves \((R_k)\) for \(S\).

The preceding source criteria are already proved with their zero-quotient and local-height boundaries in `ALGEBRA_SERRE_NOTES_20260929.md`, sections “The depth conditions and reducedness” and “The original Serre argument and its zero quotient”. For Noetherian rings, reducedness is exactly \((R_0)+(S_1)\), and normality is exactly \((R_1)+(S_2)\). Applying the two ascent assertions to these pairs gives both original Noetherian ascent theorems. The fibre rings are Noetherian, being quotients of localizations of the original Noetherian \(S\). The zero ring, when present globally, has no primes, so these local conditions are vacuous and it is reduced and normal under the source conventions. No exclusion is added. Unit 0726 merely supplies the two missing list commas.

## Smooth reduced ascent with the finite-stage witnesses retained

Let \(R\to S\) be smooth and \(R\) reduced; no Noetherian assumption is imposed on \(R\). Smoothness gives flatness and regular, hence reduced, fibres. If \(R\) is Noetherian then \(S\), being finitely presented over \(R\), is Noetherian, and the preceding theorem applies.

In general the finite-presentation descent of smooth maps, as cited in source smooth overview item (10), gives a finitely generated \(\mathbf Z\)-subalgebra \(R_0\subset R\), a smooth \(R_0\)-algebra \(S_0\), and the original isomorphism \(S\cong R\otimes_{R_0}S_0\). Let \(R_\lambda\) run over finite-type \(\mathbf Z\)-subalgebras of \(R\) containing \(R_0\). This is a directed system under inclusion: adjoining the finite generating sets of any two gives a third. Its union is \(R\), and
\[
 \underset{\lambda}{\operatorname{colim}}
 (R_\lambda\otimes_{R_0}S_0)
 \xrightarrow{\sim}R\otimes_{R_0}S_0
\]
sends each \(r_\lambda\otimes s_0\) to that same tensor. Surjectivity holds because a tensor is a finite sum; injectivity holds because any finite tensor relation uses finitely many coefficients, all contained in one later stage. These are ring maps, since products of elementary tensors use the same finite products of coefficients.

If the original \(x\in S\) satisfies \(x^2=0\), first choose a stage containing a representative \(x_\lambda\). The equality \(x_\lambda^2=0\) in the colimit has a witness in one later stage: equality in a filtered colimit of rings is eventual equality. Thus the original two enlargements of \(R_0\) are justified separately. Call the resulting ring and element again \(R_0,S_0,x_0\), preserving the source's rebasing convention. Smoothness persists by base change, \(R_0\) is reduced as a subring of the reduced \(R\), and it is Noetherian as a finite-type \(\mathbf Z\)-algebra. The Noetherian theorem gives reduced \(S_0\), whence \(x_0=0\) and \(x=0\). Finally, if a nonzero element were nilpotent with minimal exponent \(e\ge2\), its nonzero power of exponent \(\lceil e/2\rceil<e\) would be square-zero. Hence absence of nonzero square-zero elements proves reducedness. Retained unit 0727 specifies the subring as the subject of “is reduced”; it changes no ring or hypothesis.

## Smooth normal ascent and the exact filtered-colimit proof

Let the original \(R\to S\) be smooth with \(R\) normal. Normality means that each prime localization is an integrally closed domain. In particular \(R\) is reduced: a nilpotent vanishes at each prime, and an element vanishing at all prime localizations is zero (otherwise its annihilator is contained in a maximal ideal at which it does not vanish). Thus the preceding theorem gives reduced \(S\).

Fix \(\mathfrak q\subset S\) and \(\mathfrak p=\varphi^{-1}(\mathfrak q)\). With \(U=R\setminus\mathfrak p\), the comparison
\[
 R_{\mathfrak p}\otimes_RS\xrightarrow{\sim}U^{-1}S,
 \quad (r/u)\otimes s\longmapsto\varphi(r)s/\varphi(u)
\]
has inverse \(s/\varphi(u)\mapsto (1/u)\otimes s\). Further localization at \(U^{-1}\mathfrak q\) is \(S_{\mathfrak q}\); the maps send each represented quotient to the same quotient and are inverse on all generators. Smoothness is retained by this base change. The original source reduction to \(R_{\mathfrak p}\), a normal domain, therefore suffices to prove the desired assertion about the unchanged \(S_{\mathfrak q}\).

Now assume \(R\) is a normal domain and retain a finite model \(R_0\subset R,S_0\) as above. In the original fraction field \(K_0=\operatorname{Frac}(R_0)\), let \(R_0'\) be the integral closure of \(R_0\). The immediately preceding Nagata ubiquity theorem makes every finite-type \(\mathbf Z\)-domain Nagata, so \(R_0'\) is finite over \(R_0\). Since \(K_0\subset\operatorname{Frac}(R)\), every element of \(R_0'\) is integral over \(R\); normality of the domain \(R\) puts it in \(R\). Here local normality implies integral closedness in the fraction field: an integral fraction lies in every \(R_{\mathfrak p}\); if it did not lie in \(R\), the proper denominator ideal \(I=\{r\in R:rx\in R\}\) would lie in a maximal ideal \(\mathfrak m\), contradicting membership in \(R_{\mathfrak m}\). Thus the original inclusion \(R_0'\subset R\) is proved with its field specified.

Set \(S_0'=R_0'\otimes_{R_0}S_0\). The exact base-change comparison is
\[
 R\otimes_{R_0'}S_0'\xrightarrow{\sim}R\otimes_{R_0}S_0,
 \quad r\otimes(a'\otimes s_0)\longmapsto ra'\otimes s_0,
\]
with inverse \(r\otimes s_0\mapsto r\otimes(1\otimes s_0)\). Tensor balancing verifies both inverse identities and the preserved structure maps. The new finite model is smooth; \(R_0'\) is a normal Noetherian domain, and its algebra \(S_0'\) is normal by Noetherian ascent. It need not be a domain, exactly as the source notes.

For every finite subset \(E\subset R\), take the finite-type domain \(D_E=R_0'[E]\) and its integral closure \(A_E\) in \(\operatorname{Frac}(D_E)\). Nagata finiteness makes \(A_E\) finite over \(D_E\), hence Noetherian and finite type over \(\mathbf Z\). The preceding denominator argument gives \(A_E\subset R\). If \(E\subset E'\), then \(\operatorname{Frac}(D_E)\subset\operatorname{Frac}(D_{E'})\), and every element of \(A_E\) is integral over \(D_{E'}\); consequently \(A_E\subset A_{E'}\). This is a directed family of normal Noetherian domains whose union is exactly \(R\): each \(r\in R\) lies in \(D_{\{r\}}\subset A_{\{r\}}\). Put \(B_E=A_E\otimes_{R_0'}S_0'\). Each \(B_E\) is normal by Noetherian smooth ascent, and the same finite-tensor comparison identifies
\[
 \operatorname{colim}_E B_E\xrightarrow{\sim}S.
\]

Here is the full normal-colimit argument needed for the source's final sentence. Let \(T=\operatorname{colim}_i T_i\) be a filtered colimit of normal rings with unital transition maps, and let \(\mathfrak q\subset T\). Put \(\mathfrak q_i\) equal to its inverse image and \(D_i=(T_i)_{\mathfrak q_i}\). These are normal domains. The transition maps \(D_i\to D_j\) are local, because denominators outside \(\mathfrak q_i\) remain outside \(\mathfrak q_j\). They need not be injective. There is a canonical map
\[
 \operatorname{colim}_iD_i\longrightarrow T_{\mathfrak q},
 \quad [a_i/s_i]\longmapsto a/s.
\]
Every target fraction has its numerator and denominator represented at a common stage, with the denominator outside the corresponding inverse-image prime, proving surjectivity. If \(a_i/s_i\) maps to zero, there is \(t\in T\setminus\mathfrak q\) such that \(ta_i=0\) in \(T\). Represent \(t\) at a common later stage and move once more to a stage where that equality holds. Its representative remains outside the inverse-image prime, so \(a_i/s_i\) becomes zero in the localized ring at that stage. This proves injectivity. Subtracting two fractions gives the corresponding equality test. The displayed map is therefore an isomorphism of the original local rings.

The target is a domain: a product equal to zero is represented by a product equal to zero at some later \(D_j\), and since that ring is a domain, one factor is already zero there and hence in the colimit. The target is nonzero because it is localization at a prime. To prove integral closedness, take an actual fraction \(a/b\in\operatorname{Frac}(T_{\mathfrak q})\), \(b\ne0\), satisfying a monic equation with coefficients \(c_1,\ldots,c_n\in T_{\mathfrak q}\):
\[
 (a/b)^n+c_1(a/b)^{n-1}+c_2(a/b)^{n-2}
 +\cdots+c_{n-1}(a/b)+c_n=0.
\]
All finitely many numerators, denominators and coefficients occur in one \(D_i\). Multiplication by the original \(b^n\), followed by one eventual-equality witness, gives in a later \(D_j\) the complete relation
\[
 a_j^n+c_{1,j}a_j^{n-1}b_j+c_{2,j}a_j^{n-2}b_j^2
 +\cdots+c_{n-1,j}a_jb_j^{n-1}+c_{n,j}b_j^n=0.
\]
The element \(b_j\) is nonzero, since its image is the fixed nonzero \(b\). Thus \(a_j/b_j\) is integral over the normal domain \(D_j\), so it equals some \(d_j\in D_j\). The equation \(a_j=b_jd_j\) maps to \(a=bd\) in the target, giving \(a/b=d\in T_{\mathfrak q}\). This argument does not assert a map between entire fraction fields when a transition map has a kernel; it uses the specific denominator whose image is nonzero. Hence every prime localization of \(T\) is a normal domain, proving normality of \(T\). Applied to the original \(B_E\), this proves the smooth normal-ascent theorem and fills the stated omitted details in editorial material.

## Regular smooth ascent and report accounting

For the source's Noetherian regular-ring convention, smoothness makes \(S\) Noetherian with regular fibres. A regular ring and all these fibres satisfy \((R_k)\) for every integer \(k\ge0\). By the established ascent theorem, \(S\) satisfies every such condition. At each fixed prime \(\mathfrak q\), the Noetherian local ring \(S_{\mathfrak q}\) has a finite dimension \(d\); applying \((R_d)\) proves it regular. No bound on the global dimension of \(S\) is assumed or needed. Retained unit 0728 makes the quantified integer explicit.

Ten physical reports are accounted for in six groups. OCC-01015 is the missing “by”, explicitly refining the unchanged designation inside prior operation MC-STK-ERR-0725-OP1. OCC-12436 retains that prior operation's zero-module branch. OCC-01016 supplies the colon at 46389. OCC-01017, OCC-01018 and OCC-12437 retain both commas in unit 0726. OCC-01019 and OCC-12438 retain unit 0727. OCC-01020 and OCC-12439 retain unit 0728. These are two additional operations and five retained operations in four canonical units. The additional copyedit must never erase the zero-module paragraph, and inverse replay must recover the entire current chapter including that paragraph and unrelated admitted material.

The consequences checked here feed the existing ascent chain: the zero-module depth convention is verified before the finite induction; the preceding Serre criteria give the reduced and normal Noetherian cases; the preceding Nagata finite-type theorem supplies the finite normal domains in smooth ascent. The filtered-colimit argument is a complete standard proof of the source's asserted step, not a new theorem claim or a requested translation rewrite. Remaining source review begins at 46633. The later Brauer and other research packets remain deferred until the core Algebra review is complete.
