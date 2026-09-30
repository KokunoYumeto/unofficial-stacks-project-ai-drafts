# Constructing flat ring maps: source review with the original maps

Source: Stacks Project authors, algebra.tex:44566–44778, authority a04446e57ec1fbc252a871afcec7752fb2807b14, file SHA256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3. The twelve existing correction units MC-STK-ERR-0686 through MC-STK-ERR-0697 are checked against the original constructions here. Full proof elaborations remain separate editorial material. This batch adds no optional extension and does not replace source translations.

## The original monogenic local extensions

Retain the original local ring \((R,\mathfrak m,k)\) and a monogenic extension \(k(\alpha)/k\). If \(\alpha\) is transcendental, take the source ring
\[
 R'=R[x]_{\mathfrak mR[x]}.
\]
The ideal \(\mathfrak mR[x]\) is prime because its quotient is the domain \(k[x]\). Thus \(R'\) is local, with maximal ideal \(\mathfrak mR'\), and reduction gives the exact isomorphism
\[
 R'/\mathfrak mR'\longrightarrow k(\alpha),\qquad
 \overline{f(x)/s(x)}\longmapsto \overline f(\alpha)/\overline s(\alpha).
\]
Here \(s\notin\mathfrak mR[x]\), so \(\overline s\) is a nonzero polynomial, and transcendence makes its value nonzero. Conversely every rational expression in \(\alpha\) comes from lifts of its numerator and nonzero denominator. Cross multiplication, with the nonzero reduced denominators retained, proves injectivity and independence of the lifts. The ring map \(R\to R'\) is flat because it is a polynomial extension followed by localization. It is injective directly: if a constant \(r\in R\) becomes zero, then \(sr=0\) for some polynomial \(s\notin\mathfrak mR[x]\); a coefficient of \(s\) lies outside \(\mathfrak m\) and is a unit, so its product with \(r\) being zero forces \(r=0\).

If \(\alpha\) is algebraic, retain its original monic minimal polynomial
\[
 \overline F(T)=T^d+\sum_{i=1}^{d}\overline\lambda_iT^{d-i},
 \qquad
 F(T)=T^d+\sum_{i=1}^{d}\lambda_iT^{d-i},
 \qquad R'=R[T]/(F).
\]
Each \(\lambda_i\) is the chosen lift in \(R\) of that actual coefficient. Monic division gives the free \(R\)-basis \(1,t,\ldots,t^{d-1}\), where \(t\) is the class of \(T\), so the original map is finite free and injective. Every maximal ideal of the integral \(R\)-algebra \(R'\) contracts to the maximal ideal \(\mathfrak m\). But
\[
 R'/\mathfrak mR'\cong k[T]/(\overline F)
       \xrightarrow[\ T\mapsto\alpha\ ]{\ \sim\ } k(\alpha)
\]
is a field. Thus \(\mathfrak mR'\) is the unique maximal ideal and \(R'\) is local. The inverse to the displayed field map represents each element by its unique polynomial remainder of degree less than \(d\). All original coefficients and the selected root are retained.

If the algebraic extension is separable, \(\overline F'(\alpha)\ne0\); hence \(F'(t)\) lies outside the unique maximal ideal of \(R'\) and is a unit. This makes the original monic quotient finite étale. The lifting assertion can be seen directly: for a square-zero ideal \(J\subset D\), a root modulo \(J\), and a chosen lift \(u\), the derivative \(F'(u)\) is a unit and the exact corrected root is
\[
 u-F'(u)^{-1}F(u).
\]
Taylor expansion retains the original coefficients; all terms with at least two copies of \(F(u)\in J\) vanish because \(J^2=0\). The resulting value of \(F\) is exactly zero. If two roots have the same reduction and differ by \(v\in J\), their polynomial values differ by \(F'(u)v\); invertibility forces \(v=0\). Thus the lift is unique. Finite presentation together with this formal étaleness gives étaleness, consistently with the preceding chapter criterion.

## The fixed base and the directed local colimit

The source category has objects \((k_i,R\to R_i,\phi_i)\), with \(\phi_i:R_i\to k_i\) inducing the prescribed residue-field isomorphism and \(k_i\subset K\). Its morphisms must be the \(R\)-algebra maps restored by MC-STK-ERR-0687. The residue-field diagram alone does not enforce this. For example, let \(R=k[\epsilon]/(\epsilon^2)\), let both objects have \(R_i=R\) with the identity structure map, and let \(\psi:R\to R\) send \(\epsilon\) to zero and fix \(k\). Its residue-field diagram commutes, but it is not an \(R\)-algebra map. A tower of these ring maps has colimit \(k\). The induced quotient \(R\to k\) is not flat: the inclusion \((\epsilon)\hookrightarrow R\) becomes the zero map from the nonzero module
\((\epsilon)\otimes_R k\cong k\) into \(R\otimes_R k\cong k\).
Thus the omitted base compatibility has a concrete effect on the asserted flatness.

MC-STK-ERR-0686 puts the displayed tuples in the same field-first order. Its shorter notation \((k_i,R_i,\phi_i)\) is read in the category of the fixed \(R\)-algebras: \(R_i\) carries the specified structure map. Restoring that already specified map gives \((k_i,R\to R_i,\phi_i)\); forgetting only its repeated display gives the inverse notation. No additional change of the mathematical object is needed.

Now let \(I\) be the original nonempty directed set of such objects. The residue diagram makes each transition local: an element is in the inverse image of the target maximal ideal exactly when its residue in \(k_i\) becomes zero in \(k_j\), and the field inclusion \(k_i\subset k_j\) is injective. Put
\[
 R'=\operatorname*{colim}_{i\in I}R_i,\qquad k'=\bigcup_{i\in I}k_i.
\]
The compatible \(\phi_i\) induce \(\phi':R'\to k'\). This map is surjective because an element of the union belongs to some \(k_i\) and lifts to \(R_i\). Its kernel is exactly \(\mathfrak mR'\): if an element represented by \(a_i\in R_i\) has zero residue in the union, injectivity of the field inclusion says \(\phi_i(a_i)=0\), hence \(a_i\in\mathfrak mR_i\). Conversely every element of \(\mathfrak mR'\) maps to zero. An element outside this kernel has a representative outside the corresponding maximal ideal of \(R_i\), so is already a unit at that stage and remains a unit. This proves that \(R'\) is local with maximal ideal \(\mathfrak mR'\) and with the exact stated residue field.

For every injection of \(R\)-modules \(M\hookrightarrow N\), flatness at each stage gives
\(M\otimes_R R_i\hookrightarrow N\otimes_R R_i\).
The identifications
\[
 \operatorname*{colim}_i(M\otimes_R R_i)\longrightarrow
 M\otimes_R R',\qquad [m\otimes a_i]\longmapsto m\otimes[a_i],
\]
and the analogous map for \(N\), are isomorphisms by the universal property of the tensor product. Their inverses send a tensor with a represented second factor to that stage and extend by additivity; finite tensor relations hold at a common stage. Filtered exactness preserves the injections. Thus the actual map \(R\to R'\) is flat. This argument needs flatness of each stage over the fixed \(R\); it does not infer flatness of arbitrary category transitions merely from the objects being flat over \(R\).

## The original transfinite construction and its endpoints

The coefficient base in MC-STK-ERR-0688 is necessary: the field \(K(x)\) must be generated **over \(k\)** by elements at most \(x\). Otherwise, for example, a well-order beginning with \(0\) in an extension of \(k=\mathbf Q(t)\) would initially generate only the prime field \(\mathbf Q\), which does not contain the given \(k\).

Keep the existing MC-STK-ERR-0691 choice of a well-order on the actual set \(K\) with a greatest element. It exists: select one element, well-order its complement, and put the selected element last. At a successor \(x\) of \(x'\), the correct equality is
\[
 K(x)=K(x')(x),
\]
as restored by MC-STK-ERR-0689. Square brackets would give only the generated algebra, which need not be a field: if \(x\) is transcendental over the preceding field, \(x^{-1}\) does not belong to that polynomial algebra. The monogenic construction above provides the required flat local extension \(R(x')\to R(x)\), with the specified extension of residue fields and the original new element \(x\).

At the least element, retain MC-STK-ERR-0690's actual initial pair \(R'(x)=R\), \(K'(x)=k\). An empty union of fields would not supply \(k\). At every nonzero limit position take the directed colimit \(R'(x)=\operatorname*{colim}_{y<x}R(y)\); the preceding proof gives its maximal ideal \(\mathfrak mR'(x)\) and residue field \(K'(x)=\bigcup_{y<x}K(y)\). Then use the same original monogenic construction for
\[
 K(x)=K'(x)(x).
\]
All transition maps produced in this construction are flat local and faithfully flat. For completeness, a flat local map \(A\to B\) is faithfully flat as follows. If \(M\ne0\), choose a nonzero cyclic submodule \(A/I\hookrightarrow M\). The ideal \(I\) is proper, so \(IB\) lies in the maximal ideal of \(B\). Hence \((A/I)\otimes_A B=B/IB\ne0\), and flatness embeds this nonzero module into \(M\otimes_A B\). Faithfulness together with flatness implies injectivity of \(A\to B\): if its kernel is \(J\), then the injection \(J\hookrightarrow A\) tensored with \(B\) has image zero, forcing \(J\otimes_A B=0\), then \(J=0\). Thus the constructed rings have the claimed compatible embeddings.

At the greatest element \(x_{\max}\), the original generated field is exactly \(K(x_{\max})=K\), and \(R(x_{\max})\) is the required ring. This verifies the actual retained endpoint correction. No assertion is made that an arbitrary well-order must have a largest stage. For example, a well-order of type \(\omega\) on the countable field \(\mathbf Q(t_1,t_2,\ldots)\) has only finite initial subsets, each generating a field of finite transcendence degree, whereas the full field has infinite transcendence degree.

The next lemma uses a continuous ordinal indexing of the same construction. To make the comparison exact, index the chosen ordered elements by \(x_\gamma\), \(\gamma<\lambda\), and define \(T_0=R\), \(T_{\gamma+1}=R(x_\gamma)\), and
\(T_\delta=\operatorname*{colim}_{\gamma<\delta}T_\gamma\) for nonzero limits. At a limit \(\delta\), this is precisely the intermediate \(R'(x_\delta)\), before adjoining the next element; at a successor it is the original after-adjunction ring. These identifications commute with every transition by construction. The final \(T_\lambda\) equals the selected final \(R(x_{\max})\) when \(\lambda\) is a successor, and in the continuous formulation has residue field \(K\). This supplies the exact relation between the source's element-indexed and ordinal-indexed presentations; it does not silently assume that an after-adjunction ring at a limit position was already the preceding colimit.

## Finite étale local stages and descent of locality

Assume now that the original \(K/k\) is separable algebraic. Every successor residue extension in the preceding construction is finite separable, so every \(T_\gamma\to T_{\gamma+1}\) is the finite étale monic quotient already checked.

We use the following property of the finite étale rings that occur here. An \(R\)-algebra map \(A\to B\) between finite étale \(R\)-algebras is finite étale. It is finite because finitely many generators of \(B\) as an \(R\)-module also generate it as an \(A\)-module. It is finitely presented: if \(A=R[X_1,\ldots,X_s]/(f_1,\ldots,f_u)\), \(B=R[Y_1,\ldots,Y_t]/(g_1,\ldots,g_v)\), and the image of \(X_j\) is represented by \(h_j(Y)\), then the exact \(A\)-presentation of \(B\) is
\[
 A[Y_1,\ldots,Y_t]/(g_1,\ldots,g_v,X_1-h_1(Y),\ldots,X_s-h_s(Y)).
\]
Both inverse maps follow by substitution on these original generators. To verify formal étaleness over \(A\), start with an \(A\)-algebra square-zero lifting problem for \(B\). Formal étaleness of \(B/R\) gives a unique \(R\)-algebra lift. Its restriction to \(A\) and the prescribed \(A\)-structure have the same reduction; formal unramifiedness of \(A/R\) makes them equal. The lift is therefore \(A\)-linear and unique, proving the assertion by the finite-presentation criterion. If \(A\) and \(B\) are local, integrality implies that the maximal ideal of \(B\) contracts to the maximal ideal of \(A\). The map is flat local, hence faithfully flat and injective by the preceding argument.

Maintain inductively that each \(T_\gamma\) is a directed union of actual finite étale local \(R\)-subalgebras. At a successor write \(T_\gamma=\operatorname*{colim}_i R_i\), with those injections. The source uses a finite étale algebra \(R_{i,1}\) with
\[
 T_{\gamma+1}=T_\gamma\otimes_{R_i}R_{i,1}.
\]
The descent in this particular construction can be given explicitly. The successor is the original monic quotient \(T_\gamma[U]/(F)\). Its finitely many coefficients all belong to one \(R_i\); let \(F_i\in R_i[U]\) be that same polynomial and let \(R_{i,1}=R_i[U]/(F_i)\). Base change sends the class of \(U\) to the original class of \(U\), and coefficientwise evaluation gives the exact displayed isomorphism.

The residue field \(k_i\) of \(R_i\) embeds in the residue field \(k_\gamma\) of \(T_\gamma\). The image of \(\overline F_i\) over \(k_\gamma\) is the original irreducible separable minimal polynomial. A factorization over \(k_i\) would remain a nontrivial factorization over \(k_\gamma\), so \(\overline F_i\) is irreducible. A repeated irreducible factor, equivalently a nonconstant common divisor with its derivative, would likewise remain one after the field extension, so it is separable. The monogenic proof above now makes \(R_{i,1}\) a finite étale local ring. The same argument applies to the polynomial over every later \(R_{i'}\).

The locality assertion in the existing MC-STK-ERR-0692 also holds for an arbitrary finite étale descended algebra giving that exact base change. Indeed \(R_i\to T_\gamma\) is a filtered colimit of the finite étale local transition maps checked above. It is flat, and the residue-field injection makes it local, hence faithfully flat. Consequently
\[
 R_{i,1}\longrightarrow T_\gamma\otimes_{R_i}R_{i,1}=T_{\gamma+1}
\]
is faithfully flat. If a ring \(C\) has a faithfully flat map to a local ring \(D\), then \(C\) is local. To prove this, for each maximal ideal \(\mathfrak n\subset C\), the ring \(D/\mathfrak nD\) is nonzero by faithfulness. Choose a prime in it; its inverse image \(\mathfrak q\subset D\) contracts to \(\mathfrak n\), because its quotient contains the field \(C/\mathfrak n\) injectively. The unique maximal ideal \(\mathfrak m_D\) contains \(\mathfrak q\), so \(\mathfrak n\subseteq \mathfrak m_D\cap C\). The latter is proper, forcing equality. Every maximal ideal of \(C\) is therefore the same ideal. This proves the descent claim used by the correction.

For each \(i'\geq i\), retain the actual ring
\[
 D_{i'}=R_{i'}\otimes_{R_i}R_{i,1}.
\]
Its base change along the faithfully flat local \(R_{i'}\to T_\gamma\) is again \(T_{\gamma+1}\), so the same proof makes \(D_{i'}\) local. It is finite étale over \(R\) by base change and composition. Its map into \(T_{\gamma+1}\) is faithfully flat, hence injective, so it is an actual subalgebra. The tensor-colimit isomorphism
\[
 \operatorname*{colim}_{i'\geq i}D_{i'}
      \longrightarrow T_\gamma\otimes_{R_i}R_{i,1}
\]
sends \([a_{i'}\otimes b]\) to \([a_{i'}]\otimes b\). Its inverse is determined on simple tensors by a stage representing \(a\); all finite sums and tensor relations occur at a common later stage. This proves the successor assertion without suppressing a tensor factor or locality requirement.

At a nonzero limit \(\delta\), every finite subset of \(T_\delta\) belongs to some \(T_\gamma\), because there are finitely many representing stages and one larger ordinal below \(\delta\) contains all of them. At that stage the induction hypothesis places it in a finite étale local \(R\)-subalgebra. To verify directedness under inclusion, take the union of finite \(R\)-algebra generator sets of any two such subalgebras, and apply this finite-subset assertion; the resulting subalgebra contains both. The inclusions between these finite étale local \(R\)-algebras are faithfully flat by the argument above. Every element lies in one of them, so their directed union is exactly \(T_\delta\), with its actual ring operations. The initial stage \(R\) uses the identity finite étale extension. This proves the full lemma with the stated local rings, and verifies the receiving role of the existing locality correction. MC-STK-ERR-0693 repairs only the “Since ... and we see” coordination in the limit-stage sentence.

## Finite free realization with the original minimal polynomial

For 44674–44701 retain the original ring \(R\), prime \(\mathfrak p\), residue field \(F=\kappa(\mathfrak p)=\operatorname{Frac}(R/\mathfrak p)\), and finite field extension \(L/F\). The induction is on \([L:F]\), as MC-STK-ERR-0694 states. If the degree is one, the identity ring map suffices. A proper nontrivial intermediate field \(F\subsetneq L'\subsetneq L\) has both degrees strictly smaller. If \(R\to S'\) realizes \(L'/F\) and \(S'\to S\) realizes \(L/L'\), then the composite is finite free, its prime is
\[
 (\mathfrak pS')S=\mathfrak pS,
\]
and its residue-field isomorphism is the actual composite with \(L'\subset L\). A product of the two chosen free bases is a free \(R\)-basis, of rank \([L':F][L:L']=[L:F]\). These strict inequalities are the mathematical content of MC-STK-ERR-0695; the gerund correction is separate. If no such intermediate field exists and the degree exceeds one, choose \(\alpha\in L\setminus F\). Then \(F(\alpha)\) cannot be a proper intermediate field, so \(L=F(\alpha)\).

Keep this actual \(\alpha\) and its monic minimal polynomial
\[
 P(T)=T^d+\sum_{i=0}^{d-1}a_iT^i.
\]
Choose a single actual nonzero denominator \(\overline g\in R/\mathfrak p\) for the coefficients, lifted by \(g\in R\setminus\mathfrak p\), with \(a_i=\overline f_i/\overline g\). Such a common denominator is the full product of the finitely many original denominators; the numerators are multiplied by the corresponding products of the other factors. Keep those factors and retain the auxiliary element \(\beta=\overline g\alpha\) alongside \(\alpha\). Define
\[
 Q(X)=X^d+\sum_{i=0}^{d-1}g^{d-i-1}f_iX^i\in R[X].
\]
No negative exponent occurs because \(i<d\). Its image over \(F\) satisfies the complete comparison
\[
 \overline Q(X)=\overline g^{\,d}P(X/\overline g),
 \qquad
 \overline Q(\beta)=\overline g^{\,d}P(\alpha)=0.
\]
The nonzero factor \(\overline g^{\,d}\) and the inverse scale \(X/\overline g\) remain explicit. The inverse substitution gives \(P(T)=\overline g^{-d}\overline Q(\overline gT)\), so any factorization of \(\overline Q\) would factor \(P\). Thus \(\overline Q\) is irreducible and
\[
 F[X]/(\overline Q)\xrightarrow{\sim}L,\quad [X]\longmapsto\overline g\alpha,
 \qquad \alpha\longleftrightarrow\overline g^{-1}[X].
\]
This proves the exact relationship behind the source's generator replacement while keeping its original field, original root and polynomial available.

Take \(S=R[X]/(Q)\), with free basis \(1,x,\ldots,x^{d-1}\). Modulo \(\mathfrak p\) this is free over the domain \(R/\mathfrak p\), so it injects into its localization
\[
 S/\mathfrak pS\longrightarrow
 (S/\mathfrak pS)\otimes_{R/\mathfrak p}F
       \cong F[X]/(\overline Q)\cong L.
\]
The injection follows by the free-basis coefficients, each of which embeds into \(F\). Thus \(S/\mathfrak pS\) is a domain and \(\mathfrak q=\mathfrak pS\) is prime. Its fraction field is exactly \(L\): the displayed localization is already the field \(L\), and it contains both the embedded domain and inverses of its nonzero coefficient elements; its element \(\overline g^{-1}x\) is the original \(\alpha\). The induced map on residue fields sends each actual quotient \(u/v\) to the quotient of its two displayed images, with nonzero denominator preserved, and has the inverse determined by the coefficients in \(F\) and \(\alpha=\overline g^{-1}x\). This proves the stated extension isomorphism, not just equality of degrees.

## The cardinal bound and the actual relation witnesses

For 44703–44769 retain \(A\), the flat \(A\)-algebra \(B\), and the exact infinite cardinal \(\kappa=\max(|A|,\aleph_0)\). Given a subalgebra \(E=E_0\subset B\) of size at most \(\kappa\), the set \(S_k\) of tuples
\[
 (n,a_1,\ldots,a_n,e_1,\ldots,e_n),\qquad
 n\geq1,\quad \sum_i a_ie_i=0
\]
has cardinality at most \(\kappa\). For each fixed \(n\), it is a subset of \(A^n\times E_k^n\), with cardinality at most \(\kappa\); the countable union over \(n\) still has cardinality at most \(\kappa\).

Flatness and the equational criterion at algebra.tex:8994–9034 give exactly the source witnesses
\[
 m_s\geq0,\quad b_{s,j}\in B,\quad a_{s,ij}\in A,\qquad
 e_i=\sum_{j=1}^{m_s}a_{s,ij}b_{s,j},\qquad
 \sum_i a_i a_{s,ij}=0\quad(1\leq j\leq m_s).
\]
All coefficients, indices and zero cases remain. If \(m_s=0\), the first formula states that every \(e_i=0\), and no witness elements need be adjoined. For all other \(s\), adjoining the finitely many \(b_{s,j}\) for each of at most \(\kappa\) relations adds at most \(\kappa\) elements. The \(A\)-algebra generated by these elements and \(E_k\) consists of evaluations of finite polynomials in at most \(\kappa\) generators with coefficients in \(A\). The set of finite monomials has cardinality at most \(\kappa\), and so does the set of finite sums of such terms. Hence the actual \(E_{k+1}\) has cardinality at most \(\kappa\). The countable union \(B'=\bigcup_{k\geq0}E_k\) has the same bound.

Every finite relation \(\sum_i a_i b_i'=0\) in \(B'\) has all its entries in one \(E_k\), where it is that identical relation, since the rings are actual subalgebras of \(B\). Its chosen witnesses belong to \(E_{k+1}\subset B'\), and their displayed equalities hold unchanged. Thus every relation in \(B'\) is trivial in the precise equational sense, and \(B'\) is flat over \(A\). To retain the direction actually used from the criterion: if \(I=(a_1,\ldots,a_n)\subset A\) and an element \(\sum_i a_i\otimes b_i'\) of \(I\otimes_A B'\) maps to zero in \(B'\), the witness equalities give
\[
 \sum_i a_i\otimes b_i'
 =\sum_{i,j}a_i\otimes a_{s,ij}b_{s,j}
 =\sum_j\left(\sum_i a_i a_{s,ij}\right)\otimes b_{s,j}
 =0.
\]
The finitely generated ideal criterion then proves flatness.

If \(B\) is faithfully flat over \(A\), each such \(B'\) is faithfully flat too. For a maximal ideal \(\mathfrak n\subset A\), faithfulness gives \(\mathfrak nB\ne B\). The inclusion of the actual subalgebra implies
\(\mathfrak nB'\subseteq\mathfrak nB\); hence \(1\notin\mathfrak nB'\) and \(B'/\mathfrak nB'\ne0\). Together with flatness, this gives faithfulness: a nonzero cyclic submodule \(A/I\) of any nonzero module has \(I\subseteq\mathfrak n\), so \(B'/IB'\ne0\), and flatness preserves its injection into the tensor of the full module. This includes the parenthetical assertion of the original lemma.

Finally, every finite subset of \(B\) generates an \(A\)-subalgebra of cardinality at most \(\kappa\). The algebra generated by two subalgebras of that size has that size bound by the same finite-polynomial count. Applying the witness construction to it gives a flat subalgebra containing both. Thus the actual collection of small flat subalgebras is directed under inclusion, contains every element of \(B\) at some stage, and has colimit \(B\) with the original maps. If \(B\) itself already satisfies the bound, it is the terminal member and the assertion remains valid. MC-STK-ERR-0696 corrects only “choicse”; MC-STK-ERR-0697 corrects the word order of the same cardinal bound. The fuller cardinal and relation arguments here remain editorial.

## Report accounting and propagation

There are twenty-one physical reports in this interval and thirteen review groups. Twelve existing units, MC-STK-ERR-0686 through MC-STK-ERR-0697, supply fifteen retained operations. The two reports requiring “were” in place of “was” are grouped as an optional stylistic proposal and rejected as a mandatory defect; they do not change the construction or its set-size issue.

The base-compatible category maps, generated-over-\(k\) residue fields, field adjunctions, initial pair and final selected stage are checked together at the construction's receiving maps. That constructed ring feeds the next lemma through the explicit continuous ordinal reindexing. Its finite étale local stages and exact tensor base changes validate the existing locality correction. The finite-free field realization retains the original minimal polynomial and all scaling factors in the comparison; the small-flat-subalgebra lemma retains every original relation witness and the exact cardinal bound. These checks produce no new optional consequence group. Broader paper mining and synthesis remain after the core correction review.
