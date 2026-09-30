# Local flatness criteria and their exact Tor maps

Separate editorial evidence for the Stacks Project authors' algebra.tex, authority commit a04446e57ec1fbc252a871afcec7752fb2807b14, lines 23415–24176. Authority SHA-256: FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3. All complete source units and all ten received reports in this interval were read. The next section heading at 24177–24180 is lookahead only.

The two retained canonical units MC-STK-ERR-0485 and MC-STK-ERR-0486 resolve four reports. Seventeen minimal operations are proposed for the other six reports and the two independently found much-greater-than symbols. Full proofs and three further consequences are separate editorial material. The source statements retain their original hypotheses and remain identifiable; no chapter or translation mutation, formal certification or novelty claim is asserted. The bounded library query records all four hits as unread, including the local-work hits.

## Injection modulo the maximal ideal and its original quotients

Source 23423–23477. The naming correction at 23427 is part of OCC-00485. Keep the local map \(R\to S\), maximal ideal \(\mathfrak m\subset R\), finite \(S\)-module \(N\), flat \(R\)-module \(M\), and original \(R\)-linear map \(u:N\to M\). No \(S\)-module structure on \(M\), or \(S\)-linearity of \(u\), is assumed.

Assume \(u_1:N/\mathfrak mN\to M/\mathfrak mM\) is injective. For each \(n\), the map on the left tensor terms in the source diagram is \(u_1\otimes_{R/\mathfrak m}\mathrm{id}_{\mathfrak m^n/\mathfrak m^{n+1}}\). It is injective because tensoring over a field is exact. The lower left term injects into \(M/\mathfrak m^{n+1}M\) by flatness of \(M\). To prove the inductive step, take an element in the kernel of \(u_{n+1}\). Its image modulo \(\mathfrak m^n\) is zero by injectivity of \(u_n\), so it lifts from the upper left tensor term. The image of that lift in the lower middle term is zero, and lower left injectivity then kills its image in the lower left term. Injectivity of the left vertical map kills the lift itself. Thus \(u_{n+1}\) is injective.

For \(x\in\ker u\), all these injections give \(x\in\bigcap_n\mathfrak m^nN\). The ideal \(\mathfrak mS\) lies in the maximal ideal of the Noetherian local ring \(S\); \(N\) is finite over \(S\). The source's Krull-intersection result gives this intersection zero, hence \(u\) is injective.

For a proper ideal \(J\subset R\), \(J\subset\mathfrak m\), and \(JS\) lies in the maximal ideal of \(S\). Consequently \(R/J\to S/JS\) is a local map of nonzero local rings, \(S/JS\) is Noetherian, \(N/JN\) is finite over it, and \(M/JM\) is flat over \(R/J\). Reduction of the quotient map modulo \(\mathfrak m/J\) is precisely \(u_1\). Applying the just-proved injection assertion shows \(N/JN\to M/JM\) injective. For \(J=R\) both quotient modules are zero and the injection is immediate; the zero ring is not incorrectly called a local ring. This supplies the boundary implicit in the source's ideal argument without changing its theorem.

The long exact sequence from \(0\to N\to M\to Q\to0\), with \(Q=M/u(N)\), now identifies
\[
\operatorname{Tor}_1^R(Q,R/J)
 =\ker(N/JN\to M/JM)=0
\]
for every ideal \(J\). Thus \(Q\) is flat. More generally tensoring that exact sequence with any module \(X\) remains exact on the left because \(\operatorname{Tor}_1^R(Q,X)=0\). The injection \(u\) is therefore universally injective as a map of \(R\)-modules. Also \(N\) is flat: for an injection \(X\to Y\), its tensor with \(N\) sits as a map of submodules of \(X\otimes_RM\to Y\otimes_RM\), with both horizontal inclusions just proved; flatness of \(M\) makes the latter injective. These consequences use no Noetherianity of \(R\).

## The early corollaries and the exact-complex induction

Source 23479–23552. The remaining two naming corrections of OCC-00485 occur at 23482 and 23494. Multiplication by the original \(f\) on \(S\) is an \(R\)-linear map from a finite \(S\)-module to an \(R\)-flat module. Its reduction is injective by the given fibre nonzerodivisor hypothesis. The preceding lemma gives both injectivity of multiplication by \(f\) and flatness of its exact cokernel \(S/fS\).

For a regular sequence, put \(S_i=S/(f_1,\ldots,f_i)\). At stage \(i\), multiplication by \(f_i\) on \(S_{i-1}\) has exactly the specified injective fibre map. Apply the same lemma with the original Noetherian \(S\) as the auxiliary ring and the finite \(S\)-module \(S_{i-1}\) as both domain and target. It gives the next injection and \(R\)-flatness of \(S_i\). The source definition of regularity also requires \(S_c\ne0\); this follows because its reduction modulo \(\mathfrak m\) is the given nonzero final fibre quotient. Thus no unit or zero-quotient case has been lost.

For the free-fibre lemma, \(M\ne0\) finite over local \(S\) implies \(M/\mathfrak mM\ne0\) by Nakayama, since \(\mathfrak mS\) is inside the maximal ideal. The fibre basis has finite positive size \(n\). The source map \(S^{\oplus n}\to M\) is injective by the injection lemma, and its finite cokernel vanishes modulo \(\mathfrak m\), hence vanishes by Nakayama. This gives the actual chosen-basis isomorphism. Since \(n>0\), \(S\) is a direct summand of \(M\) as an \(R\)-module, so it is \(R\)-flat.

For the finite complex with \(e\geq1\), apply the injection lemma to \(F_e\to F_{e-1}\). Its cokernel \(C\) is finite over \(S\) and \(R\)-flat. Right exactness identifies \(C/\mathfrak mC\) with the fibre cokernel. The assumed fibre exactness therefore makes \(0\to C/\mathfrak mC\to F_{e-2}/\mathfrak mF_{e-2}\to\cdots\) exact. This is the required induction hypothesis on the shorter original quotient complex. It proves exactness at every term at which the displayed complex asserts exactness and flatness of \(\operatorname{coker}(F_1\to F_0)\). If a complex of length zero is included by the convention \(F_1=0\), its final flatness assertion is just the given flatness of \(F_0\). No missing end map is treated as a surjectivity assertion.

## Finite length, Artin--Rees and the local criterion

Source 23559–23641; OCC-00486 changes the incorrectly described descending induction to ordinary induction, and OCC-00487 introduces the quantified ideal \(J\). Both printed occurrences of \(n>>0\) receive the intended TeX relation \(\gg\).

For a finite-length \(N\), length zero means \(N=0\), whose Tor groups vanish. Length one identifies \(N\) with the residue field \(\kappa\). For length greater than one, use the source exact sequence with both nonzero end modules of smaller length. The exact segment
\[
\operatorname{Tor}_1^R(N',M)\longrightarrow
\operatorname{Tor}_1^R(N,M)\longrightarrow
\operatorname{Tor}_1^R(N'',M)
\]
and the two induction hypotheses force the middle term to zero. This proves the preparation lemma over every local \(R\).

In the local flatness criterion retain both Noetherian hypotheses. For every ideal \(J\) of finite colength, the preparation lemma and the exact sequence \(0\to J\to R\to R/J\to0\) show \(J\otimes_RM\to M\) injective. Fix the source ideal \(I\subset R\) and \(n\geq1\). Its displayed short exact sequence can be equipped consistently with the actual maps
\[
x\longmapsto(x,-x),\qquad (a,b)\longmapsto a+b.
\]
Use the same maps in the ambient split sequence. Both \(I+\mathfrak m^n\) and \(\mathfrak m^n\) have finite colength, since \(R\) is Noetherian local. If \(z\in\ker(I\otimes_RM\to M)\), then \((z,0)\) maps to zero in \((I+\mathfrak m^n)\otimes_RM\), because the latter maps injectively into \(M\). Tensor right exactness supplies a lift \(w\in(I\cap\mathfrak m^n)\otimes_RM\). Its component in \(\mathfrak m^n\otimes_RM\) is zero, so its multiplication image in \(M\) is zero. Thus this lift belongs to the precise kernel asserted in the source and maps to \(z\).

Artin--Rees for \(I\subset R\) gives \(c\) with \(I\cap\mathfrak m^n\subset\mathfrak m^{n-c}I\) for \(n\geq c\). The image of its tensor with \(M\) is contained in \(\mathfrak m^{n-c}(I\otimes_RM)\), without assuming that tensoring the inclusion is injective. Hence the original kernel lies in every sufficiently high power of \(\mathfrak m\) on \(I\otimes_RM\). This module is finite over \(S\): choose the finite \(R\)-generators of \(I\) and the finite \(S\)-generators of \(M\), and use their simple tensors. Krull intersection over \(S\) therefore makes the kernel zero. Equivalently, as the source argues, the finite-module comparison identifies its completion with tensoring by the faithfully flat \(\mathfrak mS\)-adic completion of \(S\), whose unit is injective. Both routes retain the original ideal and uniform Artin--Rees shift. Flatness follows from the ideal criterion.

## The correct free index and the ideal-adic Tor criterion

Source 23650–23748. OCC-00488 concerns a substantive rank problem, not merely a glyph collision. The original ideal \(I\) cannot be the prescribed index set for a free presentation of an arbitrary \(R/I\)-module. For instance, for a nonzero field \(R\), \(I=0\) has one underlying element and its indexed free module cannot surject onto \(R^2\). Choose an actual sufficiently large set \(\Lambda\), for example the underlying set of \(N\), and the evaluation surjection
\[
(R/I)^{(\Lambda)}\longrightarrow N,\qquad e_\lambda\longmapsto \lambda .
\]
With its actual kernel \(K\), this supplies the source exact sequence. All six free-sum occurrences must use the same new index, not just the two mentioned by the report. The separate malformed base \(R/\) is already corrected to \(R/I\) by MC-STK-ERR-0485; both OCC-12142 and OCC-00489 retain it.

Direct sums commute with the Tor construction, by a free resolution and componentwise homology. Thus \(\operatorname{Tor}_1^R((R/I)^{(\Lambda)},M)=0\). For every module \(X\) annihilated by \(I\), the canonical map
\[
X\otimes_R M\longrightarrow X\otimes_{R/I}(M/IM)
\]
sends \(x\otimes m\) to \(x\otimes\overline m\). Its inverse sends \(x\otimes\overline m\) to \(x\otimes m\); changing \(m\) by a finite sum of terms \(am'\), \(a\in I\), changes this by terms \(ax\otimes m'=0\). These inverse balanced maps preserve the exact presentation and its kernel tensor. Flatness of \(M/IM\) therefore shows \(K\otimes_RM\to(R/I)^{(\Lambda)}\otimes_RM\) injective, and the Tor exact sequence gives \(\operatorname{Tor}_1^R(N,M)=0\).

If \(I^mN=0\), the case \(m=0\) gives \(N=0\). The case \(m=1\) is proved. For \(m>1\), retain \(N'=IN\) and \(N''=N/IN\); both are annihilated by \(I^{m-1}\). The same Tor exact segment proves the assertion inductively. Applied to every exact sequence of \(R/I^n\)-modules, this vanishing shows exactness of tensoring with \(M/I^nM\), through the canonical comparison just given with \(I^n\) in place of \(I\). Thus \(M/I^nM\) is \(R/I^n\)-flat.

For the following graded-piece criterion, work at stage \(R/I^{n+1}\) with its ideal \(I^n/I^{n+1}\). Its square is zero for \(n\geq1\), and the ideal tensor exact sequence identifies
\[
\operatorname{Tor}_1^{R/I^{n+1}}(M/I^{n+1}M,R/I^n)
 =\ker\bigl(M\otimes_R I^n/I^{n+1}\to I^nM/I^{n+1}M\bigr).
\]
The target on the right is the actual multiplication image; replacing it by its containing module does not change the kernel. Assuming the previous stage flat, the nilpotent case of the just-proved criterion makes the next stage flat. This proves both statements with the original stage indices.

## The two local variants and the support boundary

Source 23750–23843. In the first proof of the ideal variant, the proper ideal \(I\) is inside \(\mathfrak m\), so \(\kappa\) is annihilated by \(I\). The preceding criterion gives its Tor vanishing, and the proved local criterion applies.

For the second proof retain every original \(f_i,x_i,a_{ij},y_j\). Put \(v_i=x_i-\sum_j a_{ij}y_j\in IM\) and \(b_j=\sum_i f_i a_{ij}\in I\). For each \(i\) choose a finite expression \(v_i=\sum_\ell c_{i\ell}z_{i\ell}\), with \(c_{i\ell}\in I\). Then
\[
w=\sum_{i,\ell}f_ic_{i\ell}\otimes z_{i\ell}
       +\sum_j b_j\otimes y_j\in I\otimes_RM
\]
maps to the source's tensor \(\sum_i f_i\otimes x_i\) in \(\mathfrak m\otimes_RM\). The equality uses the two balancing identities, with the original plus signs and the subtracted \(a_{ij}y_j\) restored in \(v_i\). Its product in \(M\) is zero. The assumed Tor vanishing makes \(I\otimes_RM\to M\) injective, so \(w=0\) and the original tensor is zero. For \(I=(x)\) with \(x\) a nonzerodivisor of \(R\), the original length-one free resolution with differential multiplication by \(x\) identifies the stated Tor group with the actual annihilator \(M[x]\).

In the powers lemma, retain \(K=\ker(I\otimes_RM\to M)\). The level-\(n\) flatness assumption kills its image in
\[
(I/I^n)\otimes_{R/I^n}(M/I^nM)
 \cong (I\otimes_RM)/I^{n-1}(I\otimes_RM).
\]
The final quotient follows from tensor right exactness and \(I^n=I^{n-1}I\); the image of \(I^n\otimes_RM\) is precisely the displayed power submodule. At \(n=1\) both descriptions are zero, as required. Hence \(K\) lies in their intersection for all \(n\). The module \(I\otimes_RM\) is finite over Noetherian \(S\), and the earlier uniform Krull-intersection annihilator from group 344 gives one \(s\in1+IS\) annihilating that intersection. For every \(\mathfrak q\supset IS\), \(s\notin\mathfrak q\), so \(K_{\mathfrak q}=0\). This proves the localization assertion without an unsupported interchange of intersection and localization.

For completeness, put \(\mathfrak p=\mathfrak q\cap R\). The localized hypotheses give the original local map \(R_{\mathfrak p}\to S_{\mathfrak q}\), proper ideal \(IR_{\mathfrak p}\), and finite module \(M_{\mathfrak q}\). Localization and the tensor comparisons identify its Tor kernel with \(K_{\mathfrak q}\), and its quotient is flat over \(R_{\mathfrak p}/IR_{\mathfrak p}\). The local variant proves flatness over \(R_{\mathfrak p}\), hence over \(R\).

The locus restriction is necessary. For \(R=S=k[t]\), \(I=(t)\) and \(M=R/(t-1)\), every \(M/I^nM\) is zero and therefore flat, while \(M\) is not \(R\)-flat: multiplication by the nonzero \(t-1\) on \(R\) becomes the zero map on the nonzero \(M\). At the only prime containing \(t\), the localization of \(M\) is zero, in agreement with the proved result. No global flatness is inferred solely from these formal quotients.

## Tor comparisons and the exact change-of-rings sequence

Source 23845–23918. MC-STK-ERR-0486 already changes “cohomology” to “homology”; both OCC-00490 and OCC-12143 retain it. The original complexes compute first homology.

The two lemmas have the following common extension for every ring map \(R\to R'\), \(R\)-module \(M\), and \(R'\)-module \(X\). Put \(M'=M\otimes_RR'\). There is a natural right-exact sequence
\[
\operatorname{Tor}_1^R(M,R')\otimes_{R'}X
 \xrightarrow{a}\operatorname{Tor}_1^R(M,X)
 \xrightarrow{b}\operatorname{Tor}_1^{R'}(M',X)
 \longrightarrow0.
\]
No injectivity of \(a\) is asserted.

Here is a construction and proof with all original maps retained. Take a free resolution \(F_\bullet\to M\) over \(R\), and put \(C_\bullet=F_\bullet\otimes_RR'\). Let
\(Z=\ker(C_1\to C_0)\) and \(B=\operatorname{im}(C_2\to C_1)\).
Then \(Z/B=\operatorname{Tor}_1^R(M,R')\), and \(C_1\to C_0\to M'\to0\) is exact. Choose a free \(R'\)-module \(G\) surjecting onto \(Z\). Replace \(C_2\) by \(C_2\oplus G\), sending \((c,g)\) to \(d_2(c)+g\) through this chosen surjection. Keep degrees one and zero exactly \(C_1,C_0\). This is exact in degrees one and zero; choose further free modules onto its successive kernels to obtain a resolution \(P_\bullet\to M'\). The identity in degrees zero and one and the inclusion \(C_2\to C_2\oplus G\) extend to a chain map \(C_\bullet\to P_\bullet\): at every higher step, the previous compatibility puts the required image in the next kernel, and freeness lifts it along the chosen surjection.

After tensoring with \(X\), both complexes have the same degree-one cycles
\[
T=\ker(C_1\otimes_{R'}X\to C_0\otimes_{R'}X).
\]
The first homology of \(C_\bullet\otimes X=F_\bullet\otimes_RX\) is \(T/\operatorname{im}(C_2\otimes X)\). That of \(P_\bullet\otimes X\) is \(T/\operatorname{im}(Z\otimes X)\), because \(G\to Z\) is onto and tensoring is right exact. The quotient map gives the surjective \(b\), and its kernel is the image of \(Z\otimes X\) modulo the old boundaries. The map from \(Z\otimes X\) to the first homology kills \(\operatorname{im}(B\otimes X)\); tensor right exactness therefore factors it through \((Z/B)\otimes X\), giving \(a\) with exactly that image. Explicitly \(a([z]\otimes x)\) is the class of the cycle \(z\otimes x\). This proves exactness at every asserted term.

Changing the free resolutions uses their comparison maps lifting the identity. Such maps exist by degreewise free lifting, and two choices are chain homotopic by the same kernel-lifting induction. Tensoring preserves the equation \(f-g=dh+hd\), so the induced homology maps agree. The same construction for module maps commutes on homology. Thus this is the natural sequence, not a choice-dependent replacement. The earlier complete comparison-homotopy argument in group 460 applies to these exact maps.

If \(M'\) is flat, the last Tor group is zero and \(a\) is onto for every \(R'\)-module \(X\). Taking \(X=R''\) recovers the source's first lemma; it actually proves the stronger arbitrary-module version. The source proof's tensor exactness is also justified directly: the image of \(C_1\to C_0\) is flat, as the kernel of a surjection from a free module onto flat \(M'\), and tensoring the two short exact sequences preserves the stated exactness. Taking arbitrary \(M'\) and \(X=R'/IR'\) recovers the second lemma; its surjection \(b\) in fact holds for every \(X\).

## The localized comparison criterion and the fibre criterion

Source 23920–24023. OCC-00491 only inserts “by” in the notation declaration. Let \(T=S\otimes_RR'\) and write \(S'=W^{-1}T\), retaining the source localization and all original maps. Then
\[
M'=(M\otimes_RR')\otimes_T S',
\]
by the map on simple tensors \(m\otimes(s\otimes r')\mapsto sm\otimes r'\) and its balanced inverse. Its reduction modulo \(I'=IR'\) is the corresponding localization of \((M/IM)\otimes_{R/I}(R'/I')\), which is flat over \(R'/I'\). Localization of a flat module with an auxiliary algebra action remains flat over the base: each localization is a filtered colimit of copies of the base-flat module with its multiplication transitions, and filtered colimits preserve tensor exactness.

Apply \(a\) in the preceding sequence first to \(R\to R/I\) and \(X=R'/I'\). Since \(M/IM\) is flat, it is surjective. Then apply \(b\) to \(R\to R'\) and this same \(X\). Their composite is exactly
\[
\operatorname{Tor}_1^R(M,R/I)\otimes_R R'
 \longrightarrow \operatorname{Tor}_1^{R'}(M\otimes_RR',R'/I'),
\]
using the canonical equality of tensoring an \(I\)-annihilated module by \(R'\) and by \(R'/I'\). It is onto. Localizing the target in \(T\) identifies it with the Tor group for \(M'\); this follows either from a free resolution of \(R'/I'\) tensored with \(M\otimes_RR'\), or from exactness of localization on its resulting homology. The source assumption that the original Tor map is zero makes every image generator, and hence its localization, zero. The local criterion over the original Noetherian \(R',S'\) then gives the asserted flatness.

For the fibre criterion retain \(I=\mathfrak mS\). Multiplication gives a surjection \(\mathfrak m\otimes_RS\to I\), and tensoring with \(M\) gives
\[
\mathfrak m\otimes_RM\longrightarrow I\otimes_SM\longrightarrow M.
\]
The first map is onto and the composite is injective by \(R\)-flatness of \(M\). Thus the first map is also injective, and the second is injective: any element in its kernel lifts along the first map and the composite kills that lift. It follows that \(\operatorname{Tor}_1^S(S/I,M)=0\). The ideal variant for the original Noetherian local map \(S\to S'\) gives \(S\)-flatness of \(M\). Since \(M\ne0\) is finite over local \(S'\), its residue quotient at the maximal ideal of \(S'\) is nonzero by Nakayama. Its quotient at the smaller maximal ideal from \(S\) maps onto that quotient and is nonzero. Flatness over the local ring \(S\) therefore makes \(M\) faithfully flat.

The original source then tensors the exact Tor-kernel sequence with this flat \(M\) and uses faithfulness to kill \(\operatorname{Tor}_1^R(\kappa,S)\). This is valid under its Noetherian \(R\) hypothesis. The next section gives the stronger conclusion by testing arbitrary ideals, thereby avoiding that particular extra hypothesis.

## Removing the unused base Noetherian hypothesis

This is editorial propagation, not a change of the source theorem statements. The injection lemma assumes only \(S\) Noetherian, and its proof above uses no Noetherianity of \(R\). It follows that the three early corollaries and the finite-complex assertion remain valid for arbitrary local \(R\), retaining local Noetherian \(S\). The individual arguments in the second section explicitly check every application and cokernel. This does not remove Noetherianity from the separate local Tor criterion, whose Artin--Rees argument uses it.

There is a module version of the regular-sequence consequence. Let \(R\to S\) be local with \(S\) Noetherian, let \(Q\) be finite over \(S\) and flat over \(R\), and suppose the original elements \(f_1,\ldots,f_c\in S\) are regular on \(Q/\mathfrak mQ\), including the nonzero final quotient required by the source definition. Set \(Q_i=Q/(f_1,\ldots,f_i)Q\). Multiplication by \(f_i\) on \(Q_{i-1}\), with the unchanged auxiliary ring \(S\), satisfies the injection lemma whenever the preceding quotient is \(R\)-flat. Induction gives each injection and flatness of every \(Q_i\). The final fibre quotient is nonzero; each preceding quotient maps onto it, so every \(Q_i\) is nonzero. Each is finite over local \(S\). Nakayama makes \(Q_i/\mathfrak mQ_i\ne0\); the flat local criterion for faithful modules then makes every \(Q_i\) faithfully flat over \(R\). Thus this strengthens the ring case while retaining the original elements, quotients and nonzero condition.

The fibre criterion at 23977 also works for arbitrary local \(R\), with \(S,S'\) still Noetherian local. The preceding section already proves \(M\) faithfully flat over \(S\) without Noetherianity of \(R\): its local criterion is over \(S\). For any ideal \(J\subset R\), put
\[
L_J=\ker(J\otimes_RS\to S).
\]
Flatness of \(M\) over \(S\) identifies \(L_J\otimes_SM\) with the kernel of \(J\otimes_RM\to M\), which is zero by \(R\)-flatness of \(M\). Faithfulness over \(S\) gives \(L_J=0\). The ideal criterion therefore makes \(S\) flat over arbitrary \(R\). This is the exact map replacing the Noetherian-only last step, and proves the extended fibre criterion. Moreover the local map \(R\to S\) is faithfully flat because its residue fibre is nonzero. No finiteness of the ideal \(J\) was assumed in this argument.

## Elementwise ideal-power torsion and the associated graded map

Under exactly the source hypotheses \(M/IM\) flat over \(R/I\) and \(\operatorname{Tor}_1^R(R/I,M)=0\), the preceding bounded-power vanishing extends to every module \(N\) whose every element is annihilated by some power of \(I\), with no single power required for all elements. Define
\[
N[n]=\{x\in N:I^nx=0\}.
\]
These are increasing submodules and their union is exactly \(N\). Each has the proved Tor vanishing. A fixed free resolution of \(M\), tensored with this filtered system, computes the Tor groups. Tensor products commute with filtered colimits, and filtered colimits of modules are exact, so kernels modulo images, and hence homology, commute with this system. It follows that
\[
\operatorname{Tor}_1^R(N,M)=
 \varinjlim_n\operatorname{Tor}_1^R(N[n],M)=0.
\]
Thus tensoring with \(M\) preserves any short exact sequence of such modules. No finite generation of \(I\) is assumed, and no closure of this class under arbitrary extensions is asserted when \(I\) is infinitely generated.

The same hypotheses give canonical isomorphisms in every associated-graded degree:
\[
(I^n/I^{n+1})\otimes_{R/I}(M/IM)
 \xrightarrow{\;\mu_n\;} I^nM/I^{n+1}M,\qquad
(a\bmod I^{n+1})\otimes(m\bmod IM)\longmapsto am\bmod I^{n+1}M.
\]
For \(n=0\) this is the usual identity comparison. For \(n\geq1\), the bounded-power vanishing applied to \(R/I^n\) identifies \(I^n\otimes_RM\) injectively with its actual multiplication image \(I^nM\). The same holds for \(n+1\). Tensor right exactness on \(I^{n+1}\to I^n\to I^n/I^{n+1}\to0\) then identifies the quotient with \(I^nM/I^{n+1}M\). The source-balanced comparison for the \(I\)-annihilated module \(I^n/I^{n+1}\) gives the displayed map. Its inverse is induced by these quotient isomorphisms, so it is independent of every representative. Multiplication by an original class \(b\in I^a/I^{a+1}\) commutes with the maps, since both composites send \(b\otimes(a\otimes m)\) to \(bam\). Hence they assemble into an isomorphism of graded modules over the original associated graded ring.

Conversely, flatness of \(M/IM\) and injectivity of all these original graded-piece multiplication maps imply flatness of every \(M/I^nM\), by the source's proved square-zero induction. This converse is only a statement about all finite quotients. It does not by itself prove \(\operatorname{Tor}_1^R(R/I,M)=0\) or flatness of \(M\); the preceding support example shows why global flatness cannot be inferred from the formal quotients alone.

## The localization gluing lemmas and faithful flatness

Source 24025–24168; OCC-00492 repairs only the two sentence fragments explaining Tor vanishing. For the single element \(f\), the original exact free resolution \(0\to A\xrightarrow{f}A\to A/fA\to0\) and injectivity of \(f\) on \(M\) give \(\operatorname{Tor}_1^A(M,A/fA)=0\), while length one gives the vanishing in degree two. The flat quotient \(M/fM\) and the ideal-adic criterion give Tor degree one zero for every \(f\)-annihilated module. Presenting such a module by a sum of copies of \(A/fA\) and using the exact Tor segment in the source gives degree two zero as well.

For any original \(K\), use the actual maps \(K\to K'=K/K[f]\) and \(K'\to K\), the latter sending the class of \(k\) to \(fk\). This is well defined, injective, and has image \(fK\); their composite is multiplication by \(f\). The source's two exact Tor segments show that both induced maps on degree one are injective, because their preceding terms vanish. Thus multiplication by \(f\) on \(\operatorname{Tor}_1^A(M,K)\) is injective. The localization map from this Tor module is injective: any element in its kernel is killed by a finite power of \(f\), and repeated injectivity forces it to zero. Exact localization of the free resolution identifies that localized Tor module with \(\operatorname{Tor}_1^{A_f}(M_f,K_f)=0\). Therefore every original Tor group vanishes and \(M\) is flat.

For the multi-generator lemma retain \(I=(f_1,\ldots,f_r)\), \(r\geq1\), and the full assumed range \(1,\ldots,r+1\). First, presenting any \(I\)-annihilated \(K\) by a free \(A/I\)-module, whose kernel is again \(I\)-annihilated, gives the stated vanishing successively in each degree through \(r+1\). Define the induction assertion for \(0\leq j\leq r\) to be vanishing in degrees \(1,\ldots,j+1\) on modules annihilated by \(f_1,\ldots,f_j\). The assertion at \(r\) is just proved. For \(j\geq1\), take \(K\) annihilated by the first \(j-1\) elements. Its submodule \(K[f_j]\) and quotient \(K/f_jK\) are both annihilated by all first \(j\) elements. For each \(1\leq i\leq j\), the two source sequences and the inductive vanishings in degrees \(i\) and \(i+1\) make multiplication by \(f_j\) injective on \(\operatorname{Tor}_i^A(M,K)\). Its localization is zero by the given \(A_{f_j}\)-flatness of \(M_{f_j}\). Thus it is zero. This proves the assertion at \(j-1\), retaining both endpoints of the degree range. At \(j=0\) it is precisely Tor degree one vanishing for every \(K\), which proves flatness.

Here is the faithful-flatness argument omitted by both source proofs. Once flatness is established, take any maximal ideal \(\mathfrak q\) of \(A\). If some \(f_i\notin\mathfrak q\), the assumed faithful flatness of \(M_{f_i}\) gives
\(M\otimes_A\kappa(\mathfrak q)
 \cong M_{f_i}\otimes_{A_{f_i}}\kappa(\mathfrak q)\ne0\).
If all \(f_i\in\mathfrak q\), use instead the faithfully flat \(M/IM\) over \(A/I\) to obtain the same nonzero fibre. The single-element case is this argument with \(I=(f)\). The nonzero-fibre criterion for a flat module now gives faithful flatness over \(A\). Conversely faithful flatness over \(A\) passes to each displayed localization and quotient by its base-change definition. Unit ideals, empty spectra and zero rings are covered by these same base-change maps; the source explicitly keeps \(r\geq1\). This completed argument stays in editorial evidence and does not replace the source's omitted-proof sentence.

All receiving consequences above are linked in the claim ledger. The current scope is source-ordered correction accounting and the exact implications it reveals. Broader synthesis, claims of novelty and a combined-results paper remain after the core work.

