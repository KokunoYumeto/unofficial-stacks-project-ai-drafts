# Formal smoothness of fields: original-source validation

Source: Stacks Project authors, `algebra.tex:44127–44565`, original commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, file SHA256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`. This note preserves the actual extensions, polynomials, coefficients, differential modules and maps in that source. It validates the original assertions and received corrections; optional generalizations and wider paper mining remain deferred until completion of the Algebra review.

## Finite generation and the original differential kernel

For the six equivalent conditions in 44136–44171 keep the stated finite generation of the field extension \(K/k\). The established characterizations of formal unramifiedness, étale field algebras and formal étaleness give all implications except \(\Omega_{K/k}=0\Rightarrow K/k\) finite separable. Choose the original finite-type domain \(A\subset K\) with fraction field \(K\), and retain the multiplicative set \(S=A\setminus\{0\}\). The exact localization map is
\[
 S^{-1}\Omega_{A/k}\longrightarrow\Omega_{K/k},\qquad
 \omega/s\longmapsto s^{-1}\omega,
\]
with the inverse determined on every original fraction by
\(d(a/s)\mapsto (s\,da-a\,ds)/s^2\). The quotient and Leibniz rules give both inverse identities. If the target is zero, choose a finite generating list \(\omega_1,\ldots,\omega_m\) of \(\Omega_{A/k}\). For each generator its zero localization gives an actual \(s_i\in S\) with \(s_i\omega_i=0\). The full product \(f=\prod_i s_i\) is nonzero in the original domain and kills all generators. For an empty list take \(f=1\). Thus \(\Omega_{A_f/k}=0\) under the same comparison maps. This finite-type algebra is unramified by the previously proved differential criterion. Its selected prime is zero and its residue field is the unchanged \(K\), so the unramified-at-a-prime theorem makes \(K/k\) finite separable. No assertion is made here for an arbitrary extension without finite generation.

For 44173–44226 retain the perfect base \(k\) of characteristic \(p>0\), the extension \(K/k\), and the given \(a\in K\). The easy direction keeps the full derivative identity \(d(b^p)=p b^{p-1}db=0\). Conversely if \(da=0\), the directed colimit of the differential modules of finite generated intermediate fields realizes this particular zero relation at one such field containing \(a\). Indeed a class zero in a filtered module colimit is zero at a later stage, and the finite set of field elements needed for that stage generates a finite generated field extension. This reduces the proof to the original finite generated situation without assuming injective transition maps on differential modules.

Choose the source separating transcendence basis \(x_1,\ldots,x_r\) and put \(F=k(x_1,\ldots,x_r)\), retaining \(K/F\) finite separable. Its existence follows from the original definition of a perfect field, `algebra.tex:10488–10500`, and separability of finite generated extensions. The canonical derivations \(\partial_j\) on \(F\) give
\(\Omega_{F/k}=\bigoplus_j F\,dx_j\); the inverse universal map sends \(df\) to \(\sum_j\partial_j(f)dx_j\), with the complete quotient derivative \(\partial_j(P/Q)=(Q\partial_jP-P\partial_jQ)/Q^2\).

Here is the source's rational-function claim with every coefficient retained. Perfection gives
\(F^p=k(x_1^p,\ldots,x_r^p)\). The monomials \(x^I\), with all \(0\leq i_j<p\), form an \(F^p\)-basis of \(F\). Polynomial spanning follows by writing each exponent as a multiple of \(p\) plus its remainder and taking the actual coefficient's \(p\)th root in \(k\). For an original nonzero denominator \(Q\), keep the identity \(Q^{-1}=Q^{p-1}/Q^p\); this proves rational spanning without cancelling its factors. For independence, multiply a relation over \(k(x_1^p,\ldots,x_r^p)\) by the full product of its coefficient denominators. Distinct residue vectors \(I\) give disjoint monomial supports in the polynomial ring, so every coefficient vanishes. Accordingly write an arbitrary original \(f\in F\) uniquely as
\[
 f=\sum_{0\leq i_j<p} b_I^p x^I.
\]
In its derivative with respect to \(x_j\), the terms with \(i_j=0\) have coefficient zero and the remaining terms are \(i_jb_I^p x^{I-e_j}\). Their exponents still lie in the displayed basis range and are distinct. If all partial derivatives vanish, each coefficient with \(i_j>0\) is zero, since that integer is nonzero in the prime field. Every \(I\ne0\) has such a coordinate, so only \(b_0^p\) remains. For \(r=0\) the same formula consists of its single constant term.

The comparison to the original \(K\) is also explicit. A primitive generator \(\theta\) for the finite separable auxiliary extension \(K/F\) has original monic minimal polynomial \(M(T)=T^n+\sum_{i=1}^n c_iT^{n-i}\), with \(M'(\theta)\ne0\). Its differential relation is
\[
 M'(\theta)d\theta+\sum_{i=1}^n\theta^{n-i}dc_i=0.
\]
Thus the canonical map \(K\otimes_F\Omega_{F/k}\to\Omega_{K/k}\) is an isomorphism. Its inverse sends each \(dx_j\) to itself and sends
\[
 d\theta\longmapsto-\bigl(M'(\theta)\bigr)^{-1}
                         \sum_{i=1}^n\theta^{n-i}dc_i.
\]
The full relation above makes that map well-defined on the polynomial presentation and then on all fractions by the quotient rule. The two composites fix the differentials of the original generators, so are identities. No derivative coefficient or inverse factor is omitted.

Now retain the source monic minimal polynomial of the original \(a\),
\(P(T)=T^d+\sum_{i=1}^d a_iT^{d-i}\in F[T]\). Differentiation gives the complete identity
\[
 0=P'(a)da+\sum_{i=1}^d a^{d-i}da_i.
\]
Only after retaining this formula use \(da=0\). The just-proved basis \(dx_j\) of \(\Omega_{K/k}\) gives
\(\sum_{i=1}^d a^{d-i}\partial_j(a_i)=0\) for every \(j\). The powers \(1,a,\ldots,a^{d-1}\) are independent over \(F\) by minimality of the original \(P\). Hence all those partial derivatives vanish, and \(a_i=b_i^p\) in the original \(F\).

Choose the unique \(p\)th root \(\beta\) of \(a\) in an algebraic closure of \(K\), and retain the coefficient-root polynomial
\(Q(T)=T^d+\sum_{i=1}^d b_iT^{d-i}\). The exact equality \(Q(\beta)^p=P(a)=0\) gives \(Q(\beta)=0\), so \([F(\beta):F]\leq d\). But \(a=\beta^p\) yields the original inclusion \(F(a)\subseteq F(\beta)\), and \([F(a):F]=d\). The tower degree therefore forces \(F(a)=F(\beta)\), placing \(\beta\) inside the original \(K\). This supplies the required root, consistently with the complete original source lemma `fields.tex:3746–3774`. It does not replace \(a\) or its minimal polynomial by a rescaled object.

For 44228–44253 let the source differentials \(da_1,\ldots\,da_n\) be independent in \(\Omega_{k/\mathbf F_p}\). The base \(\mathbf F_p\) is perfect, so the preceding result makes \(a_1\) a non-\(p\)th-power. The polynomial \(T^p-a_1\) is irreducible and gives degree \(p\). Inductively the preceding root adjunctions have their full monomial basis \(\prod_{j<n}a_j^{i_j/p}\), \(0\leq i_j<p\). If \(a_n\) became a \(p\)th power in that field, the actual putative root would have a unique expression with coefficients \(\lambda_I\in k\), giving exactly
\[
 a_n=\sum_I\lambda_I^p\prod_{j<n}a_j^{i_j}.
\]
Differentiation retains every term: \(d(\lambda_I^p)=0\), and the coefficient of \(da_j\) is the full sum
\(\sum_{I:i_j>0}\lambda_I^p i_j a_j^{i_j-1}\prod_{\ell\ne j}a_\ell^{i_\ell}\).
The omitted indices with \(i_j=0\) contribute exactly zero. This expresses \(da_n\) in the span of the preceding differentials, a contradiction. The next irreducible \(p\)th-root polynomial has degree \(p\), giving the original \(p^n\) by the tower law. The empty tower, when used, has degree \(1=p^0\).

## The corrected coefficient field and both differential maps

In 44255–44379 the lemma needs to introduce the actual extension \(K/k\) in its statement. The correction adds that datum after the original characteristic hypothesis. All subsequent maps then have their stated domains.

For the reduction to finite generated subfields keep the original system \(K=\mathop{\rm colim}K_i\). If the final map \(K\otimes_k\Omega_{k/\mathbf F_p}\to\Omega_{K/\mathbf F_p}\) is injective, the corresponding map at \(K_i\) is injective: its kernel maps to zero in the final module, while \(K_i\otimes_k\Omega_{k/\mathbf F_p}\to K\otimes_k\Omega_{k/\mathbf F_p}\) is injective because it is scalar extension along fields. Conversely if each stage map is injective, its filtered colimit is injective, since filtered colimits of modules preserve exactness. The source and target colimits are respectively the actual scalar extension and the actual differential module by their generator/Leibniz presentations. This proves both directions, without assuming that the target differential transition maps are injective.

For a finite generated separable \(K/k\), retain the source separating generators \(x_1,\ldots,x_r,x_{r+1}\) and its irreducible polynomial \(G\in k[X_1,\ldots,X_{r+1}]\). The evaluation map has kernel \((G)\): over the rational function field in the first \(r\) variables this is the minimal-polynomial ideal, and its primitive irreducible polynomial descends the same principal ideal to \(k[X_1,\ldots,X_r][X_{r+1}]\) by Gauss's lemma. Its image is the original \(k[x_1,\ldots,x_{r+1}]\) and its fraction field is \(K\). Thus the source domain is
\(S=k[X_1,\ldots,X_{r+1}]/(G)\), with the original lower-case coefficient field. `MC-STK-ERR-0678` restores exactly this field and joins its defining sentence.

Retain the full polynomial \(G=\sum_I a_I X^I\). The universal differential presentation of that actual ring is
\[
 \Omega_{S/\mathbf F_p}=
 \frac{(S\otimes_k\Omega_{k/\mathbf F_p})\oplus\bigoplus_j S\,dX_j}
 {S\bigl(\sum_I X^I\otimes da_I,\ \sum_j(\partial_jG)dX_j\bigr)}.
\]
The map sends \(s\otimes da\) to \(s\,da\) and \(s\,dX_j\) to \(s\,d\overline X_j\). Its inverse is induced by the derivation on the polynomial ring obtained by differentiating every coefficient and every monomial; its value on the full original relation \(G\) is precisely the displayed vector. These constructions factor through the quotient and are inverse on every generator. Localizing at every nonzero element of the original \(S\), with the full quotient derivative already given above, yields
\[
 \Omega_{K/\mathbf F_p}=
 \frac{(K\otimes_k\Omega_{k/\mathbf F_p})\oplus\bigoplus_j K\,dx_j}
 {K\bigl(\sum_I x^I\otimes da_I,\ \sum_j(\partial_jG)(x)dx_j\bigr)}.
\]
Both occurrences of the source shorthand \(\Omega_k\) refer to \(\Omega_{k/\mathbf F_p}\); `MC-STK-ERR-0679` makes the base explicit without changing the module.

The derivative \(\partial_{r+1}G\) has nonzero image in \(K\). It is a nonzero polynomial of smaller degree in \(X_{r+1}\), hence is not divisible by the irreducible \(G\), which is the evaluation kernel. If \((\omega,0)\) in the localized numerator is a multiple \(t\) of the relation vector, its final coordinate is \(0=t(\partial_{r+1}G)(x)\). The nonzero field element forces \(t=0\), then \(\omega=0\). This proves injectivity of the original canonical map to \(\Omega_{K/\mathbf F_p}\), the codomain restored by `MC-STK-ERR-0680`. A map from \(K\otimes_k\Omega_{k/\mathbf F_p}\) into the unlocalized \(\Omega_{S/\mathbf F_p}\) does not in general have the needed scalar action. For example, with \(k=\mathbf F_p(t)\), \(S=k[X,Y]/(Y)=k[X]\) and \(K=k(X)\), the localized element \(X^{-1}\otimes dt\) has image \(X^{-1}dt\), which is not in the original free \(S\)-module \(S\,dt\oplus S\,dX\). The localization map between the two differential modules retains their exact relation.

## The original inseparable polynomial and its coefficient factor

For the converse injectivity criterion choose the source transcendence basis \(x_1,\ldots,x_r\) with minimal finite inseparable degree of \(K/F\), \(F=k(x_1,\ldots,x_r)\). Suppose this degree is greater than one and choose the original inseparable \(\alpha\in K\). Its minimal polynomial is a polynomial in \(T^p\). Clearing its original denominators and taking a primitive irreducible polynomial yields exactly a \(G=\sum_{I,i} a_{I,i}X^IT^i\in k[X_1,\ldots,X_r,T]\) whose evaluation kernel is \((G)\), with \(\partial_TG=0\). Keep that actual \(G\), including an arbitrary chosen nonzero coefficient \(c=a_{I_0,i_0}\); do not replace it by a polynomial with that coefficient suppressed.

Assume also that all \(\partial_{X_j}G\) vanish. Every supported exponent in \(X\) and \(T\) is then divisible by \(p\). Write \(m_{I,i}=x^I\alpha^i\). Differentiation of the original relation, with all coordinate derivatives zero, gives
\(\sum_{I,i}m_{I,i}\,da_{I,i}=0\) in \(\Omega_{K/\mathbf F_p}\). Injectivity puts this relation in \(K\otimes_k\Omega_{k/\mathbf F_p}\) itself.

The supported monomials other than \(m_{I_0,i_0}\) are linearly independent over \(k\). A relation among them is a polynomial in the evaluation kernel \((G)\), of total degree at most that of \(G\); it must therefore be a scalar multiple of \(G\). Its coefficient at the omitted supported monomial is zero, while that of \(G\) is \(c\ne0\), so this scalar and the entire relation vanish. Substituting the actual original relation
\(c\,m_{I_0,i_0}=-\sum_{(I,i)\ne(I_0,i_0)}a_{I,i}m_{I,i}\)
into the differential relation therefore gives, for every other coefficient,
\[
 da_{I,i}-\frac{a_{I,i}}c\,dc=0,
 \qquad
 d(a_{I,i}/c)=\frac{c\,da_{I,i}-a_{I,i}\,dc}{c^2}=0.
\]
The full terms involving \(dc\) and \(c^2\) remain present. The preceding differential-kernel theorem over the perfect prime field gives actual \(b_{I,i}\in k\) with \(a_{I,i}/c=b_{I,i}^p\). For the chosen coefficient take \(b_{I_0,i_0}=1\), and for a zero coefficient take zero. Since every supported exponent is divisible by \(p\), the original polynomial satisfies the complete factorization
\[
 G=c\left(\sum_{I,i} b_{I,i}X^{I/p}T^{i/p}\right)^p.
\]
The polynomial in parentheses is nonconstant because \(G\) is nonconstant; writing the right-hand side as \((cH)H^{p-1}\) gives two nonunits and contradicts irreducibility. The source's special choice \(c=1\) is recovered by that substitution, while this validation retains the actual coefficient throughout rather than silently changing the working polynomial.

Thus some \(\partial_{X_j}G\) is nonzero; keep that coordinate and use the source's indexing name \(X_1\) for it. The evaluation of this derivative is nonzero because its degree in \(X_1\) is smaller than that of the irreducible \(G\). The elements \(x_2,\ldots,x_r,\alpha\) are algebraically independent: a polynomial relation among them would belong to \((G)\) but have degree zero in \(X_1\), impossible since \(\deg_{X_1}G>0\). Put \(F'=k(x_2,\ldots,x_r,\alpha)\) and retain the common field \(E=F(\alpha)=F'(x_1)\). The original polynomial proves that \(x_1\) is separable algebraic over \(F'\), so \(E/F'\) is finite separable, whereas \([E:F]_i>1\) by the chosen inseparability of \(\alpha\). The two actual towers give
\[
 [K:F]_i=[K:E]_i[E:F]_i>[K:E]_i
        =[K:E]_i[E:F']_i=[K:F']_i.
\]
The finite inseparable-degree multiplication used here is the complete finite case of `fields.tex:1778–1803`: embeddings of the intermediate field into an algebraic closure each have exactly the same number of extensions to the top field, giving multiplication of separable degrees; divide the ordinary degree multiplication by that identity. All degrees here are finite, so the source's omitted infinite-degree case is not used. This strict inequality contradicts the original minimality. If \(r=0\), the coefficient argument already supplies the contradiction without selecting a coordinate. The differential injectivity criterion is proved on the original fields.

## Formal lifting and the characteristic-zero assertions

For the implication in 44381–44394, first retain its two characteristic cases. In characteristic zero every finite generated intermediate extension has a transcendence basis with finite algebraic remainder, and that remainder is separable because irreducible polynomials over a field of characteristic zero have nonzero derivative. Thus the extension is separable by the source definition. In characteristic \(p>0\), every derivation of \(k\) or \(K\) over \(\mathbf Z\) kills \(\mathbf F_p\), since it kills \(1\) and every integer multiple of \(1\). The identity on universal differentials therefore gives inverse comparison maps
\(\Omega_{k/\mathbf Z}\leftrightarrows\Omega_{k/\mathbf F_p}\) and
\(\Omega_{K/\mathbf Z}\leftrightarrows\Omega_{K/\mathbf F_p}\), each sending \(da\) to \(da\). Under these actual maps the short exact differential sequence for a formally smooth extension gives the injection just proved equivalent to separability. This validates the characteristic split and explicit base in the retained MC-STK-ERR-0681, rather than applying a positive-characteristic lemma to characteristic zero.

For 44396–44406 the earlier characterization, algebra.tex:37985–38037, says that formal smoothness is equivalent to \(H_1(L_{K/k})=0\) together with projectivity of \(\Omega_{K/k}\). The latter is a vector space over the actual field \(K\): choose a basis to obtain the isomorphism from the direct sum of copies of \(K\) sending each unit basis vector to the corresponding differential-module basis element. It is free and hence projective. Therefore the vanishing condition is exactly sufficient as well as necessary. The retained correction MC-STK-ERR-0682 changes only “a vector spaces” to “a vector space”.

Here is the full lifting argument for 44408–44449. For a purely transcendental extension keep the original \(K=k(x_j;j\in J)\), the original \(k\)-algebra \(A\), the ideal \(I\) with \(I^2=0\), and the map \(\varphi:K\to A/I\). Choose the actual lifts \(a_j\in A\) of \(\varphi(x_j)\). Evaluation gives \(k[x_j;j\in J]\to A\). Every nonzero original polynomial \(Q(x)\) is a unit in \(K\), so \(Q(a)\) is a unit modulo \(I\). If \(b\in A\) lifts its inverse and \(Q(a)b=1-e\) with \(e\in I\), the exact inverse is \(b(1+e)\), because
\[
 Q(a)b(1+e)=(1-e)(1+e)=1-e^2=1.
\]
Thus evaluation extends uniquely to the original rational function field, with every fraction mapped by
\[
 P(x)/Q(x)\longmapsto P(a)\,Q(a)^{-1}.
\]
Cross multiplication proves that this map is independent of the chosen fraction representation. It reduces to \(\varphi\) and is unique after the lifts \(a_j\) have been chosen, since the images of every denominator inverse are then forced. Every polynomial uses only finitely many variables; no finiteness assumption on \(J\) is needed. If \(A/I=0\), then \(I=A\) and \(I^2=0\) force \(A=0\); the unique zero-ring map handles that case as well.

If \(K/k\) is separable algebraic, its finite intermediate extensions are finite étale \(k\)-algebras. Each has a unique lift against the given square-zero quotient. For nested finite intermediate fields, uniqueness makes the restriction of the larger lift equal to the smaller one. Their filtered union therefore gives a unique lift on \(K\). This is formal étaleness, which includes the existence required for formal smoothness.

For an arbitrary separable \(K/k\), take the actual directed system of finite generated \(k\)-subextensions \(K_i\subset K\). Each has a separating transcendence basis and a finite separable algebraic remainder. Composition of the two lifts just established gives formal smoothness of each \(K_i/k\), so \(H_1(L_{K_i/k})=0\). The filtered-colimit assertion used next is the specific cotangent assertion of algebra.tex:35556–35572. Its canonical presentation uses the polynomial ring \(P_i=k[K_i]\) on symbols for all elements of \(K_i\), its evaluation kernel \(J_i\), and
\[
 J_i/J_i^2 \longrightarrow \bigoplus_{s\in K_i}K_i\,d[s].
\]
Under an inclusion \(K_i\to K_j\), the symbol \([s]\) maps to the symbol of the same element in \(K_j\), and each polynomial relation maps to that same relation. Their colimits are \(P=k[K]\), its actual evaluation kernel \(J\), and the displayed presentation with \(K\) in place of \(K_i\). A polynomial relation and a finite sum of products of relations occur at a finite stage, so the relation modules also have colimit \(J/J^2\). Filtered exactness of modules identifies the first homology with the colimit of the first homologies, hence with zero. Since \(\Omega_{K/k}\) is projective over the field \(K\), the preceding criterion gives formal smoothness of \(K/k\). This is the source's argument; it does not assert that every filtered colimit of formally smooth algebras is formally smooth.

The positive-characteristic proposition now combines the original separability/reducedness criterion at 10360–10407 with the differential injection and formal-smoothness criteria proved here. Its maps retain the original fields. In particular the earlier reducedness criterion uses
\[
 m:K\otimes_k k^{1/p}\longrightarrow K,\qquad
 \lambda\otimes\mu\longmapsto\lambda^p\mu^p,
 \qquad x^p=m(x)\otimes1.
\]
If the tensor ring is reduced, \(m(x)=0\) forces \(x=0\). A relation \(\sum_i c_i a_i^p=0\) then lifts to the exact element \(\sum_i a_i\otimes c_i^{1/p}\) in its kernel. Independence of the \(a_i\) over \(k\) remains independence after the field extension \(k^{1/p}/k\), and forces all the actual \(c_i\) to vanish. The reverse separability implication, with its minimal-inseparable-degree argument, is the earlier reviewed criterion, not a new claim of this batch. The existing correction MC-STK-ERR-0683 supplies the missing comma and the exact homology criterion reference in the proposition's proof.

In characteristic zero **all five assertions of the proposition are true**. Separability, formal smoothness and homology vanishing follow above. The original differential injection over \(\mathbf Z\) follows from the formally smooth short exact sequence with that base. Geometric reducedness can also be checked directly: for a finite generated intermediate \(K_i/k\), let \(F=k(x_1,\ldots,x_d)\) be a separating rational subfield, so \(K_i/F\) is finite separable and hence finite étale. For every field extension \(k'/k\), the exact tensor ring \(F\otimes_k k'\) is the localization of \(k'[x_1,\ldots,x_d]\) at the original nonzero polynomials over \(k\), so is a domain. The ring \(K_i\otimes_k k'\) is finite étale over that domain and is flat; it injects into its scalar extension to the fraction field, which is a product of finite separable field extensions and is reduced. Thus it is reduced itself. Finally \(K\otimes_k k'\) is the filtered union of these tensor rings, with injective transitions since tensoring vector spaces by the field \(k'\) preserves injections. Every nilpotent lies in a stage and is zero there. This proves geometric reducedness with the actual tensor rings and localization maps.

Consequently the two reports alleging a missing predicate after “If the characteristic of \(k\) is zero then” are rejected. The five enumerated clauses are precisely the asserted conjunction, with “and” before the last clause. Replacing that assertion by mere equivalence would remove information: an equivalence by itself does not assert that any clause holds. The stronger, correct original statement is retained.

## The original triangular complete-intersection algebras

For 44511–44524 retain the finite generation of \(K/k\) and the finite type domain \(R\subset K\) with fraction field \(K\). The previously proved generic-point criterion says that the original map \(k\to R\) is smooth at its zero prime exactly when \(K/k\) is separable. Smoothness at that point gives a nonzero \(f\in R\) with \(R_f\) smooth, and \(K\) remains its fraction field. Conversely, if \(K\) is a localization of a smooth \(k\)-algebra, the smooth algebra is formally smooth and localization is formally étale. For the latter assertion, lift the map on the algebra and note that every specified denominator has unit image modulo a square-zero ideal, hence unit image in the target by the explicit inverse formula above; the lift to its localization is unique. Composition gives formal smoothness of \(K/k\), and the field criterion gives separability. This proves both directions with the original localization maps.

For 44526–44559 fix the source finite subset \(E\subset K\), its generated subfield \(L=k(E)\), the transcendence basis \(x_1,\ldots,x_d\), and
\[
 F=k(x_1,\ldots,x_d),\qquad
 L=F[y_1,\ldots,y_r].
\]
Keep \(d\), the number of transcendence generators, distinct from \(r\), the number of algebraic generators. Every intermediate \(F[y_1,\ldots,y_i]\) is a field: each generator is algebraic, and the inverse of a nonzero element of a finite-dimensional domain over a field exists by injectivity and then surjectivity of multiplication by that element.

Write the original monic minimal polynomial of \(y_i\) over the preceding field as
\[
 T^{n_i}+\sum_{j=0}^{n_i-1}c_{ij}T^j.
\]
Represent each actual coefficient \(c_{ij}\) by a polynomial \(C_{ij}\) over \(F\) in the preceding \(y\)'s, and keep its chosen full representative. Then
\[
 P_i(Y_1,\ldots,Y_i)
   =Y_i^{n_i}+\sum_{j=0}^{n_i-1}C_{ij}(Y_1,\ldots,Y_{i-1})Y_i^j
\]
is the exact triangular polynomial in the source. Induction gives the isomorphism
\[
 F[Y_1,\ldots,Y_i]/(P_1,\ldots,P_i)
       \longrightarrow F[y_1,\ldots,y_i],
 \qquad Y_j\longmapsto y_j.
\]
At the next step the preceding quotient is already the preceding field and the image of \(P_i\) is exactly the minimal polynomial. Polynomial division by that monic polynomial gives the inverse by the unique remainder of degree less than \(n_i\). Equivalently, each prefix quotient has basis \(\prod_{j\leq i}Y_j^{e_j}\) with \(0\leq e_j<n_j\). The remaining \(Y\) variables are polynomial variables, so multiplication by \(P_i\), monic in its new variable, is injective on the preceding prefix quotient: the leading coefficient of a nonzero polynomial remains the same nonzero coefficient after multiplication by a monic polynomial. The final quotient is the nonzero field \(L\). This proves regularity of the full sequence and the claimed quotient with the actual coefficient field \(F\).

Choose a nonzero \(h\in k[x_1,\ldots,x_d]\) as the full product of all denominators of all coefficients in the selected \(P_i\). Include also all denominators of the coefficients in polynomial expressions over \(F\) for each element of the original finite set \(E\) in the \(y_i\). There are finitely many such denominators and each is nonzero; for an empty list choose \(h=1\). Retain every factor of this actual product. Set
\[
 D=k[x_1,\ldots,x_d,1/h],\qquad
 A=D[Y_1,\ldots,Y_r]/(P_1,\ldots,P_r).
\]
The same monic division argument, now over \(D\), gives an exact free \(D\)-basis of \(A\) consisting of all \(\prod_iY_i^{e_i}\), \(0\leq e_i<n_i\). Each \(P_i\) remains a non-zero-divisor at its step by the monic leading-coefficient argument. In particular \(A\) is nonzero and torsion-free over the domain \(D\), and the exact localization map
\[
 A\longrightarrow A\otimes_D F
       =F[Y_1,\ldots,Y_r]/(P_1,\ldots,P_r)=L
\]
is injective: a nonzero coefficient in the free basis remains nonzero in \(F\). Its evaluation sends \(Y_i\) to \(y_i\), \(x_j\) to \(x_j\), and \(1/h\) to the original inverse in \(L\). The chosen coefficient denominators place every element of \(E\) in its image.

For a global polynomial presentation, retain the extra relation instead of absorbing the inverse into the notation. In
\(k[X_1,\ldots,X_d,Z,Y_1,\ldots,Y_r]\) first impose \(h(X)Z-1\). Its quotient maps isomorphically to \(D[Y_1,\ldots,Y_r]\) by \(X_j\mapsto x_j\), \(Z\mapsto h(x)^{-1}\) and \(Y_i\mapsto Y_i\). The inverse exists because the original \(x_j\) are algebraically independent and the equation makes the image of \(h\) invertible. For every coefficient fraction \(a(X)/q(X)\) in a \(P_i\), the chosen product \(h\) is divisible by that actual \(q\); represent the fraction by \(a(X)(h(X)/q(X))Z\). This gives a polynomial lift \(\widetilde P_i\) with precisely the prescribed image \(P_i\), retaining the full coefficient and denominator factors. Therefore
\[
 A\cong
 \frac{k[X_1,\ldots,X_d,Z,Y_1,\ldots,Y_r]}
 {(h(X)Z-1,\widetilde P_1,\ldots,\widetilde P_r)}.
\]
The first relation is a nonzero element of a polynomial-ring domain, and every subsequent relation is a non-zero-divisor in the previous quotient because its image is the corresponding monic \(P_i\). The quotient is nonzero. This is the required global complete-intersection presentation. If \(d=0\), the actual nonzero constant \(h\) still has its inverse represented by \(Z\). If \(r=0\), the remaining sequence is empty and the same presentation gives \(D\). Neither boundary case changes the maps.

The set of actual global complete-intersection \(k\)-subalgebras of \(K\) just constructed is filtered under inclusion. Given two, take the union of their finite lists of algebra generators as \(E\); the construction supplies a third containing both as subalgebras of the original \(K\). Every element of \(K\) occurs by applying the construction to its singleton. Thus their filtered colimit with the actual inclusion maps is \(K\). No closure of complete intersections under an arbitrary tensor product is assumed.

In the separable case, \(L=k(E)\) is a finite generated separable subextension. Choose the smooth localization \(R_f\subset L\) above. Express every element of \(E\) as its original fraction in \(\operatorname{Frac}(R_f)=L\), and let \(g\) be the full product of their nonzero denominators. Then \((R_f)_g\subset L\subset K\) is a smooth \(k\)-algebra containing the actual \(E\). The same union-of-finite-generators argument proves filteredness and the exact colimit \(K\) in this case as well.

The retained MC-STK-ERR-0684 corrects “minimum polynomial” to “minimal polynomial”. In MC-STK-ERR-0685, both occurrences of \(k(x_1,\ldots,x_r)\) must be \(k(x_1,\ldots,x_d)\), as the exact maps above show: \(d\) and \(r\) are independent quantities. The unit's existing change from “\(P_1,\ldots,P_r\) is a regular sequence” to “are a regular sequence” is a stylistic choice only; the singular wording can refer to the tuple and is not itself a mathematical defect. Retaining that already composed unit does not turn the stylistic wording into an additional defect.

## Report accounting and propagation

Twenty physical reports have eleven dispositions. Eight previously composed units, MC-STK-ERR-0678 through MC-STK-ERR-0685, contribute eleven retained operations. Two new operations introduce the field extension in the differential criterion and change “finitely generated sub \(k\)-extensions” to “finitely generated \(k\)-subextensions”. The two characteristic-zero predicate reports are one rejected group for the reason proved above. No optional extension group is added.

The corrected coefficient field, explicit prime-field differential base and localized target are used together in the exact presentation of \(\Omega_{K/\mathbf F_p}\). Its injectivity feeds the formal smoothness criterion, which feeds both the characteristic split and the smooth-colimit argument. The triangular presentation retains every original coefficient, every inverse factor and both independent generator counts. These are checked receiving arguments within the source interval. Full proof elaborations remain this separate source-linked editorial note; they do not replace the translated source. Additional paper mining and broader consequence synthesis remain after the core review.
