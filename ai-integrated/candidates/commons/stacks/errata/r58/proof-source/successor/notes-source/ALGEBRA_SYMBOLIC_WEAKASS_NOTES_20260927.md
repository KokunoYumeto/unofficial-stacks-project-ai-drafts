# Editorial evidence for Algebra 15542–16444

Primary source: Stacks Project authors, original `algebra.tex` at commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`. The complete interval and its thirty received reports were read. Source 16445–16480 is lookahead only, ending within the opening of the next lemma. The operations in the review contain minimal corrections; these arguments and strengthenings are separate editorial material. No novelty is claimed.

## Symbolic powers and the associated-prime strengthening

Source: definition-symbolic-power and lemma-symbolic-power-associated, 15548–15575. Retain the exact ideal

\[
J=\mathfrak p^{(n)}=\ker\bigl(R\longrightarrow R_{\mathfrak p}/\mathfrak p^nR_{\mathfrak p}\bigr).
\]

For every commutative ring, every prime \(\mathfrak p\), and every positive integer \(n\), one has

\[
\operatorname{Ass}_R(R/J)=\operatorname{WeakAss}_R(R/J)=\{\mathfrak p\}.
\]

The original Noetherian hypothesis is unnecessary for this particular statement. Here is the complete argument. The ideal \(\mathfrak p^nR_{\mathfrak p}\) lies in the proper maximal ideal, so its quotient is nonzero and \(J\) is proper. Directly from the defining map, \(\mathfrak p^n\subset J\subset\mathfrak p\): an element outside \(\mathfrak p\) becomes a unit and cannot lie in that proper localized ideal. These inclusions give \(\sqrt J=\mathfrak p\). If \(a\notin\mathfrak p\) and \(ab\in J\), the image of \(a\) is invertible in \(R_{\mathfrak p}\), so \(b/1\in\mathfrak p^nR_{\mathfrak p}\) and \(b\in J\). Thus every such \(a\) acts injectively on \(R/J\).

Choose the least integer \(r\in\{1,\ldots,n\}\) with \(\mathfrak p^r\subset J\). Because \(\mathfrak p^{r-1}\not\subset J\), there is a \(c\in\mathfrak p^{r-1}\setminus J\). Every element of \(\mathfrak p\) kills \(c+J\), while the preceding injection property says no element outside \(\mathfrak p\) kills it. Hence \(\operatorname{Ann}_R(c+J)=\mathfrak p\), proving existence of the associated prime without a Noetherian existence theorem. This includes \(r=1\), where one may choose \(c=1\).

For any nonzero \(b+J\), its annihilator contains \(J\) and is contained in \(\mathfrak p\), so its radical is exactly \(\mathfrak p\). Thus its unique minimal annihilator prime is \(\mathfrak p\); if its annihilator itself is prime, that prime is also \(\mathfrak p\). This proves both asserted equalities. At \(n=0\), the original definition gives \(J=R\), the quotient is zero, and both associated sets are empty; that boundary must not be included in the positive-power assertion. The original source statement remains unchanged, with this strengthening identified as editorial material.

## Flat extension requires injection, not invertibility

Source: lemma-symbolic-power-flat-extension, 15577–15612; reports OCC-00397, OCC-12311 and OCC-00398. Insert the article in “a flat ring map” and replace “acts invertibly” by “acts injectively”. The theorem and its flatness hypothesis remain unchanged.

First verify the original base-ring maps used in its proof. Write \(\mathfrak q=\mathfrak pS\), assumed prime. The nonzero domain \(S/\mathfrak q\) is flat over \(R/\mathfrak p\). Multiplication by a nonzero element of \(R/\mathfrak p\) is injective there and remains injective after tensoring with \(S/\mathfrak q\). Such an element therefore cannot kill its nonzero identity element. Hence \(R/\mathfrak p\to S/\mathfrak q\) is injective and \(\mathfrak q\cap R=\mathfrak p\). In particular every original denominator in \(R\setminus\mathfrak p\) also avoids \(\mathfrak q\).

Set \(A=R_{\mathfrak p}\) and \(B=S_{\mathfrak p}\), retaining the source's localization at the image of \(R\setminus\mathfrak p\). Flatness gives

\[
\ker\bigl(S\to B/\mathfrak p^nB\bigr)=\mathfrak p^{(n)}S.
\]

The comparison \(B/\mathfrak p^nB\to S_{\mathfrak q}/\mathfrak p^nS_{\mathfrak q}\) localizes further at the elements of \(S\setminus\mathfrak q\). For \(n>0\), filter its source by \(\mathfrak p^iB/\mathfrak p^nB\), for \(0\leq i\leq n\). Exact tensoring with the flat \(A\)-algebra \(B\) identifies the successive quotients with

\[
\bigl(\mathfrak p^iA/\mathfrak p^{i+1}A\bigr)\otimes_A B
=\bigl(\mathfrak p^iA/\mathfrak p^{i+1}A\bigr)
 \otimes_{\kappa(\mathfrak p)}(S/\mathfrak q)_{\mathfrak p}.
\]

The first factor is the original residue-field vector space, possibly of infinite dimension. Choosing a basis expresses this tensor product as a direct sum of copies of the domain \((S/\mathfrak q)_{\mathfrak p}\). For \(f\in S\setminus\mathfrak q\), its image is nonzero in that domain, so multiplication by \(f\) is injective on every copy and hence on the direct sum. If \(fz=0\) in the filtered module, injection on its first quotient puts \(z\) in the next filtration term; repeating through the finite filtration gives \(z=0\). Thus every additional denominator is a nonzerodivisor, and the comparison map is injective. Its composite with the original map from \(S\) has kernel \(\mathfrak q^{(n)}\), so the two kernels coincide. At \(n=0\), both symbolic powers are unit ideals and the equality is immediate.

Surjectivity of multiplication is false even for \(R=k\), \(\mathfrak p=(0)\), \(S=k[t]\), \(\mathfrak q=(0)\), \(n=1\), \(f=t\). The filtration quotient is \(k[t]\); multiplication by \(t\) is injective but misses 1. The original further localization \(k[t]\to k(t)\) is nevertheless injective, exactly as required. No Noetherian hypothesis or finite-dimensionality of the vector-space quotients is added.

## Relative-assassin wording and exact local tensor maps

Source: 15616–15918. The definition of \(A'\) requires the base \(R\) in its fibre ring, and the comparison lemma's opening list should include the already-defined sixth set \(A'_{fin}\). The remaining corrections restore “proves”, the module \(N/\mathfrak p'N\), two occurrences of “an \(R\)-module”, and finite verbs in the explanatory remark. These changes preserve every original set and hypothesis.

The identifications of associated sets in this interval are through the canonical maps on spectra, not identifications of arbitrary ideals in different rings. For an \(S/\mathfrak pS\)-module, annihilators over \(S\) are inverse images of annihilators over the quotient, with the inverse correspondence given by quotienting by \(\mathfrak pS\). For a localized module the same statement uses extension and contraction of its annihilator. This is precisely the quotient/localization comparison already proved in the preceding source lemmas and used in the definition of the fibre sets.

In lemma-bourbaki, the membership at line 15827 must use \(\operatorname{Ass}_{S_{\mathfrak q}}\), since the prime written there is \(\mathfrak qS_{\mathfrak q}\). The map at the preceding display is exact as printed, with an added terminal period. Its first isomorphism sends \((m\otimes n)/s\) to \(m\otimes(n/s)\), with inverse \(m\otimes(n/s)\mapsto(m\otimes n)/s\). Writing \(\varphi:R\to S\) and \(\mathfrak p=\varphi^{-1}(\mathfrak q)\), the next isomorphism and inverse are

\[
M\otimes_RN_{\mathfrak q}\longrightarrow
 M_{\mathfrak p}\otimes_{R_{\mathfrak p}}N_{\mathfrak q},
\quad m\otimes(n/s)\longmapsto(m/1)\otimes(n/s),
\]
\[
(m/a)\otimes(n/s)\longmapsto m\otimes n/(\varphi(a)s),
\qquad a\notin\mathfrak p,\ s\notin\mathfrak q.
\]

Every displayed denominator is invertible in the indicated target; tensor balancing and the localization universal property make these maps well-defined. Their two composites fix each displayed pure tensor, which generates its module. Consequently the nonzerodivisor chosen in \(\mathfrak pR_{\mathfrak p}\), together with flatness of \(N_{\mathfrak q}\), acts injectively on the original localized tensor product. An associated element whose annihilator is \(\mathfrak qS_{\mathfrak q}\) would be a nonzero element killed by that same multiplier, giving the claimed contradiction over the correctly named local ring. The field and residue-field statements receiving this argument keep their original hypotheses.

## Weakly associated primes and the original counterexample

Source: 15925–16209. The received plural, sentence-fragment, apposition and infinitive corrections do not change the characterization of weak association. In the reduced local argument, an annihilator with radical the maximal ideal is proper, so its witness is nonzero; reducedness then contradicts the resulting nilpotence unless the maximal ideal is zero. In the arbitrary-module existence argument, a nonzero element has proper annihilator and the nonzero quotient has a minimal prime. The correction “But as ...” removes a doubled finite predicate while preserving that argument.

For the finite-generation lemma at 16114–16144, the positive exponents \(e_i\) apply to the original generators of \(\mathfrak p\). Replacing the nonzero localized witness by \(g_i^{e_i-1}m\) keeps it nonzero, sets that exponent to 1, and cannot increase the least annihilating exponents of the other generators. The finite sum decreases until every generator kills the witness. Its proper annihilator is then the maximal ideal, and the earlier finite-generator localization argument descends it. The source already states the weaker hypothesis that this particular prime is finitely generated; no global Noetherian condition is inserted.

The example at 16146–16166 retains exactly

\[
R=k[x_1,x_2,\ldots],\qquad
S=k[x_1,x_2,\ldots,y_1,y_2,\ldots]/(x_iy_i:i\geq1),\qquad M=S.
\]

Its prime \(\mathfrak q=\sum_i x_iS\) is minimal: the quotient is the domain \(k[y_1,y_2,\ldots]\); if a prime is contained in \(\mathfrak q\), none of the \(y_i\) belongs to it, so \(x_iy_i=0\) forces all \(x_i\) into it. Thus that prime equals \(\mathfrak q\).

The monomial relations express \(S\), as an \(R\)-module, as the direct sum over the finite-support exponent vectors \(\beta\) of \((R/I_\beta)y^\beta\), where \(I_\beta=(x_i:\beta_i>0)\). A nonzero element has finitely many nonzero components. Each component has annihilator \(I_\beta\), since \(R/I_\beta\) is a domain. Its total annihilator is therefore the intersection of these finitely many coordinate ideals. If a component has \(\beta=0\), the intersection is zero. Otherwise let \(F\) be the finite union of their supports. The intersection is generated by the monomials \(\prod_{i\in E}x_i\) as \(E\) ranges over the subsets of \(F\) meeting every component support: a monomial belongs to every coordinate ideal exactly when its support meets each of these finite sets, and the monomial basis gives the same criterion for polynomials. This proves finite generation. The annihilator is contained in the prime \((x_i:i\in F)\), strictly below \((x_1,x_2,\ldots)\). Hence the latter is not minimal over that annihilator. This proves the exact failure of weak-association functoriality asserted in the source; unequal radicals alone would not suffice. The source's omitted details remain editorial here, not a replacement passage.

## Finite maps and the repeated localization type correction

Source: 16211–16314; reports OCC-00407, OCC-00408 and OCC-00409. Insert “by” at both occurrences of “Denote”, and correct the target of \(ym\) from \(S_{\mathfrak q}\) to \(M_{\mathfrak q}\). The actual witness is nonzero there: its annihilator localizes to a proper ideal, and \(y\notin\mathfrak q\) is invertible. The witness is zero at the other maximal ideals because \(x\) is inverted there and \(yx^tm=0\). For each \(f\in\mathfrak pR_{\mathfrak p}\), a power kills its localization at \(\mathfrak q\), and it already vanishes at the other maximal ideals. Detection of zero by those localizations shows that power kills \(ym\) in \(M_{\mathfrak p}\). The witness remains nonzero, so its proper annihilator there has radical the maximal ideal. The earlier local characterization proves precisely the asserted contraction of weak association.

The source at 16291 repeats the earlier malformed quantifier from 15446. Correct it to \(\mathfrak p\in\operatorname{Spec}(R)\) with the given disjointness condition. This resolves the pending propagation entry in ALGEBRA-RECON-407. The exact two-stage module maps are the same maps already recorded in the preceding editorial note: \(m/r\mapsto(m/1)/(r/1)\) and \((m/s)/(r/t)\mapsto tm/(sr)\), with every original denominator retained. The proof uses the weakly-associated local characterization, so it needs no Noetherian hypothesis. Its original statement remains unchanged.

## Field-extension proof and the nonzero witness

Source: lemma-weakly-ass-change-fields, 16360–16439. The polynomial ring in the purely transcendental stage uses \(x_1,\ldots,x_r\); the earlier finite-extension degree \(n\) does not name its variables. The annihilator membership is \(gf^n\in J\), equivalent to \(gf^nz=0\); the latter module element is not itself an element of the ideal \(J\). These are the two received mathematical type/index repairs.

The nonzerodivisor argument at 16410 should explicitly choose a nonzero \(z\). Injection is proved by showing a nonzero input has nonzero image; the source's subsequent contradiction would be false for \(z=0\). Write this original \(z\) as a finite sum \(\sum_\alpha m_\alpha\otimes t_\alpha\) in a fixed \(k\)-basis of \(K\), and let \(M'\) be generated by its actual coefficients. Coordinate extraction shows that every submodule containing \(z\) after tensoring contains all these coefficients. If \(z\) belonged to \(\mathfrak pM'\otimes_kK\), each coefficient would lie in \(\mathfrak pM'\), giving \(M'=\mathfrak pM'\). Nakayama would give \(M'=0\), contrary to \(z\ne0\). Thus its residue is nonzero.

In this stage \(K=k(x_1,\ldots,x_r)\). The ring \(\kappa(\mathfrak p)\otimes_kK\) is the localization of \(\kappa(\mathfrak p)[x_1,\ldots,x_r]\) at the nonzero polynomials from \(k[x_1,\ldots,x_r]\). Those denominators remain nonzero, so the localization is a domain. The original residue module is a direct sum of copies of this domain, and the chosen \(f\) has nonzero residue. Multiplication cannot kill the nonzero residue of \(z\). The comma after the Nakayama reference and the period after the residue-module sentence complete the received wording repairs.

For the final annihilator argument, \(\mathfrak p(R\otimes_kK)\subset\mathfrak q\), so \(g\notin\mathfrak q\) implies \(g\notin\mathfrak p(R\otimes_kK)\). The proved injection permits cancellation of this actual multiplier from \(gf^nz=0\). Every \(f\in\mathfrak p\) thus has a power annihilating \(z\), while any annihilator in \(R\) lies in \(\mathfrak q\cap R=\mathfrak p\). Its radical is exactly \(\mathfrak p\). The finitely many nonzero coefficients of \(z\) place it in a finite direct sum of copies of \(M\). Applying the source's weak-association short-exact-sequence inclusions successively yields weak association to one copy of \(M\), with the same original prime. This completes the receiving argument without altering its field-extension statement.

## Torsion-free generic-fibre comparison

Sources: lemma-post-bourbaki, 15853–15877, and lemma-weak-post-bourbaki, 16338–16358. A separate strengthening replaces their flatness hypothesis by the exact property used in both proofs: every nonzero element of the domain \(R\) acts injectively on the \(S\)-module \(N\). Retain its fraction field \(K\) and the original coefficient map \(R\to S\).

Under this hypothesis, localization gives an injection \(N\to N\otimes_RK\). For any numerator \(u\in N\), denominator \(s\in R\setminus\{0\}\) and \(a\in S\), the relation \(a(u/s)=0\) means there is an original nonzero \(t\in R\) with \(tau=0\); injectivity of multiplication by \(t\) makes this equivalent to \(au=0\). Thus the annihilator in \(S\) of every fraction equals the annihilator of its numerator. Conversely every numerator occurs with denominator 1. Their associated and weakly associated sets over \(S\) are consequently identical. Passing to the localized coefficient ring by the source localization correspondences gives

\[
\operatorname{Ass}_S(N)=\operatorname{Ass}_{S\otimes_RK}(N\otimes_RK),\qquad
\operatorname{WeakAss}_S(N)=\operatorname{WeakAss}_{S\otimes_RK}(N\otimes_RK),
\]

where both equalities use the canonical injection of localized spectra. The maps retain the original numerators and denominators. The zero module is included, with empty associated sets. Flatness implies the stated injectivity by tensoring \(0\to R\xrightarrow{t}R\), but is stronger than necessary.

For a strict example let \(R=S=k[x,y]\), \(N=(x,y)\), and \(\mathfrak m=(x,y)\). This module is torsion-free because it is a submodule of the domain. It is not flat: tensor the injection \(N\hookrightarrow R\) with \(N\). The element \(x\otimes y-y\otimes x\) maps to zero in \(R\otimes_RN\), but maps to the nonzero vector \(\bar x\otimes\bar y-\bar y\otimes\bar x\) in \((N/\mathfrak mN)\otimes_k(N/\mathfrak mN)\). The degree-one monomials \(\bar x,\bar y\) form a basis, and the two displayed ordered tensor basis elements are distinct in every characteristic. Thus tensoring fails to preserve that injection. Both generic-fibre conclusions still apply to this original torsion-free module. The source's flat statements stay unchanged.

## Bounded literature comparison and limits

The machine-readable topic route and corpus-reading record preserve the four actual bounded queries and source identities. M. Richard Sayanagi, *Power Series Rings over Zero-Dimensional Rings*, source `20251008_Power_Series_Rings_Sayanagi.tex`, lines 589–630, defines weak-Bourbaki primes of an ideal by minimal primes over \((I:a)\). The exact comparison with the source module convention is \(\operatorname{Ann}_R(a+I)=(I:a)\), since \(r(a+I)=0\) exactly when \(ra\in I\); minimal primes therefore agree for the same witness. This dictionary applies directly to the symbolic quotient above. The later power-series lemma's proof was only opened, not reviewed in full.

Roman Bezrukavnikov, Michael Finkelberg and Ivan Mirkovic, *Equivariant (K-)homology of affine Grassmannian and Toda lattice*, `equiv_K.tex`, lines 1695–1742, uses symbolic powers in the construction of an affine blow-up and discusses intersections over components of a reduced subscheme. This contextual passage does not replace the original prime-ideal definition under review. Its Proposition `blow` was only partially read, and no assertion of that proposition is adopted here. The exact TeX hashes and section checks are retained in the route. These bounded readings are neither a novelty survey nor a claim to have read all corpus hits. Broader combined-results synthesis remains after completion of the core integration work.
