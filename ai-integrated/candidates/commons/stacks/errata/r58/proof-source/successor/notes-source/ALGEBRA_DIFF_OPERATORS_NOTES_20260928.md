# Finite-order differential operators: source review and editorial arguments

Authority: Stacks Project authors, `algebra.tex` at `a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`, lines 34651–35115. All twenty-four reports, including the duplicate diagonal-statement report OCC-12206, are adjudicated. The whole current interval equals the authority, with no earlier canonical operation. The naive cotangent complex at 35116–35330 is read lookahead, not adjudicated here.

Bounded dependencies were read at `categories.tex:536–621` (including the complete Yoneda lemma and representability discussion), authority SHA256 `62F7611AF4C3FEEBD041DB4728B42C7112004CFBB9FA5ECB643C6F5D90DB3F25`, and `algebra.tex:291–376` (including the snake lemma). The cited original Yoneda, Grothendieck and Cartan–Eilenberg works were not newly read. Arguments needed here are supplied below. The preceding differential and de Rham notes are retained with SHA256 `0EC7E677030EF57E9AAA46CCBC90104CB59F57E386BF08F1ADE48A13937A62F9` and `E7527FC4B77594FB1F50FB94471756AC92EF5B8D3BACD94B1A23C4D3707E5992` respectively.

The query `principal parts differential operators` returned two research PDF records and two local TeX records; none was read or adopted as evidence. There was no PDF fallback. Earlier external reading records retain their exact coverage. All proofs and stronger consequences here are separate editorial material, with no novelty claim or authorization to rewrite the source exposition.

## Dispositions and the order convention

OCC-00709 adds a period at 34680. OCC-00710 corrects the reversed universal factorization at 34716 to \(D=\alpha\circ D_{univ}\), with the original domains and codomains retained. OCC-00711 identifies an unfinished citation placeholder. The proposed local correction removes that parenthetical; it does not invent a reference. The source's explicit generators-and-relations construction already proves existence and remains in place. OCC-00712 and OCC-00713 add periods at 34744 and 34770. OCC-00714 adds a period at 34814; OCC-00715 supplies “to” at 34819. OCC-00716 and OCC-00717 punctuate the two functoriality diagrams; OCC-00718 adds the comma before “but”.

OCC-00719 and OCC-12206 describe the same missing-verb defect at 34938–34939 and receive one shared correction: the single universal operator corresponds to the specified class map. OCC-00720 and OCC-00721 are handled together at 34943, supplying the tensor base \(R\) and the sentence-final period. OCC-00722 adds a period at 34984. OCC-00723 makes \(k\ge1\) explicit in the generator criterion, since the source has not defined negative order. OCC-00724 punctuates the product commutator. OCC-00727 punctuates the inference at 35039; OCC-00728, OCC-00729, OCC-00730 and OCC-00731 punctuate the localization formulas. OCC-00725 replaces both undefined \(R\)-linear occurrences at 35057–35058 by \(A\)-linear. OCC-00726 supplies the actual order-zero tensor argument before the induction step. These are twenty-three local operations in twenty-two report groups; all twenty-four reports receive exactly one disposition.

The source's “order \(k\)” is the filtered convention expressed by its inclusions \(\operatorname{Diff}^0\subset\operatorname{Diff}^1\subset\cdots\); it does not assert minimal order exactly \(k\). All statements below use those original nonnegative indices. Whenever a commutator would have negative order in an induction, the corresponding order-zero commutator is zero and is treated directly.

## Commutators, composition and the original universal presentation

For an \(R\)-linear map \(D:M\to N\), write \(\delta_gD=D\circ g-g\circ D\), where multiplication on each side acts on its specified module. The operators \(\delta_g\) commute: both \(\delta_g\delta_hD\) and \(\delta_h\delta_gD\) equal
\[
D\circ gh-g\circ D\circ h-h\circ D\circ g+gh\circ D.
\]
Induction on \(k\) gives the precise criterion: \(D\) has order \(k\) if and only if every \((k+1)\)-fold iterated commutator vanishes. For \(k=0\) this is exactly \(S\)-linearity; the induction step applies the criterion to each \(\delta_gD\). The full expansion, for any \(r\ge1\), is
\[
(\delta_{g_1}\cdots\delta_{g_r}D)(m)
=\sum_{U\subset\{1,\ldots,r\}}(-1)^{r-|U|}
\left(\prod_{j\notin U}g_j\right)
D\left(\left(\prod_{j\in U}g_j\right)m\right).
\]
Induction proves the expansion by splitting subsets according to membership of the last index. Empty products equal \(1\), and every summand is retained. The source's displayed relation with initial positive coefficient is \((-1)^r\) times this expression for \(r=k+1\), so its vanishing is exactly equivalent, including characteristic two.

The identity
\[
\delta_g(D'\circ D)=D'\circ\delta_gD+(\delta_gD')\circ D
\]
proves the composition lemma by induction on \(k+k'\). If both orders are zero, the composite is \(S\)-linear. If just one is zero, its displayed commutator term is zero; the other term has total order at most \(k+k'-1\). If both are positive, both terms have that bound by induction. Sums and multiplication by scalars preserve each filtered piece by the same commutator criterion.

At 34700–34751, quotient the original free module \(F=\bigoplus_{m\in M}S[m]\) by its additive relations, its \(R\)-linearity relations, and the full alternating \((k+1)\)-fold relations. A linear map \(F\to N\) annihilates the first two sets exactly when \(m\mapsto L([m])\) is \(R\)-linear, and the last set exactly when that map has order \(k\), by the expansion just proved. Therefore this quotient represents the stated operator functor. The universal map is \(j_k(m)=[m]\), and its unique factorization is \(D=L_D\circ j_k\). In particular \(L_D\) follows \(j_k\), not the reverse. Two representing pairs have inverse linear maps because both composites fix all \(j_k(m)\), which generate. This proves the universal assertion directly; no unspecified category-theory existence theorem is needed.

The identity on generators gives the quotient maps \(P^k(M)\twoheadrightarrow P^{k-1}(M)\), since vanishing of every \(k\)-fold commutator implies vanishing of every \((k+1)\)-fold one. Their composites are the original tower maps. All constructions are functorial in \(M\): a linear map sends the generator \([m]\) to the corresponding generator for its image and respects every displayed relation.

## The diagonal comparison with both actions retained

Put \(C=S\otimes_R S\), \(J=\ker(\mu:C\to S)\), and \(W=S\otimes_R M\). The first factor supplies the left \(S\)-action, while the second acts on \(M\). Set \(\Delta(g)=1\otimes g-g\otimes1\). The ideal \(J\) is generated by all \(\Delta(g)\): if \(\sum a_i\otimes b_i\) has product sum zero, then it equals \(\sum(a_i\otimes1)\Delta(b_i)\). This proof keeps the original multiplication map and tensor coordinates.

For any \(R\)-linear \(D:M\to N\), define \(L_D:W\to N\) by \(L_D(a\otimes m)=aD(m)\). It exists by \(R\)-balancing. Expanding the product of \(\Delta(g_i)\) gives
\[
L_D\bigl(\Delta(g_1)\cdots\Delta(g_r)(1\otimes m)\bigr)
=(\delta_{g_1}\cdots\delta_{g_r}D)(m).
\]
Thus the commutator criterion is equivalent to \(L_D\) killing \(J^{k+1}W\). The source uses the negative generators \(g\otimes1-1\otimes g=-\Delta(g)\); its full product has the factor \((-1)^{k+1}\), exactly matching its alternating relation. Every element of \(J^{k+1}W\) is a sum of scalar multiples of these products applied to \(1\otimes m\), so the criterion checks the entire submodule, not merely its named generators.

Consequently the maps
\[
P^k_{S/R}(M)\longrightarrow W/J^{k+1}W,\quad j_k(m)\longmapsto[1\otimes m],
\]
and
\[
W/J^{k+1}W\longrightarrow P^k_{S/R}(M),\quad[a\otimes m]\longmapsto a\,j_k(m)
\]
are well defined and inverse on their generating classes. This supplies the omitted inverse verification. Writing \(C_k=C/J^{k+1}\), there is also the exact comparison
\[
P^k_{S/R}(M)\cong C_k\otimes_{S,\mathrm{right}}M.
\]
Indeed \(C\otimes_{S,\mathrm{right}}M\to W\), \((a\otimes b)\otimes m\mapsto a\otimes bm\), has inverse \(a\otimes m\mapsto(a\otimes1)\otimes m\); passing to the quotient uses right exactness, not flatness.

## The first principal-parts sequence for every module

For order one, an operator \(D:S\to N\) satisfies \(\delta_gD(h)=h\delta_gD(1)\). Thus \(\sigma_D(g)=D(g)-gD(1)\) obeys \(\sigma_D(gh)=g\sigma_D(h)+h\sigma_D(g)\), and is \(R\)-linear with value zero on \(R\). Conversely a derivation plus \(g\mapsto gn\) is an order-one operator. The two constructions give inverse maps \(\operatorname{Diff}^1(S,N)\cong\operatorname{Der}_R(S,N)\oplus N\), proving the source example.

For arbitrary \(M\), the injection in the claimed sequence is
\[
i:\Omega_{S/R}\otimes_SM\longrightarrow P^1(M),\qquad
dg\otimes m\longmapsto j_1(gm)-g\,j_1(m).
\]
The right-hand side defines a derivation in \(g\) by the order-one commutator law and is \(S\)-linear in \(m\), since \(\delta_gj_1\) is linear. It therefore gives the displayed tensor map. The augmentation \(\epsilon:P^1(M)\to M\) sends \(j_1(m)\) to \(m\). These formulas are precisely the maps constructed via Yoneda in the source.

To prove injectivity without assumptions on \(M\), use the previously proved identification \(J/J^2\cong\Omega_{S/R}\), \(dg\mapsto\Delta(g)\). The short exact sequence of right \(S\)-modules
\[
0\longrightarrow J/J^2\longrightarrow C_1\xrightarrow\mu S\longrightarrow0
\]
splits by the actual second-factor map \(s\mapsto[1\otimes s]\). Tensoring this split sequence over that right action with \(M\) is exact on the left as well as the right, because a split direct-sum decomposition remains a direct sum after tensoring. The two \(S\)-actions on \(J/J^2\) agree, and the left action on \(C_1\) supplies the indicated actions on the resulting sequence. Hence it becomes exactly
\[
0\longrightarrow\Omega_{S/R}\otimes_SM\xrightarrow{i}P^1(M)\xrightarrow{\epsilon}M\longrightarrow0.
\]
This proves the source assertion for arbitrary modules. The right-action splitting before tensoring is not a claim that the resulting sequence splits for the left \(S\)-action.

The source free-module argument is also valid without assuming the desired conclusion for \(M'\). A presentation \(0\to M'\to F\to M\to0\) gives right exact columns for \(\Omega\otimes-\) and \(P^1(-)\), the latter from the displayed right-tensor description. Suppose \(x\in\Omega\otimes M\) maps to zero. Lift it to \(y\in\Omega\otimes F\). Its image in \(P^1(F)\) comes from some \(z\in P^1(M')\). The image of \(z\) in \(M'\) maps to zero in \(F\), hence is zero because \(M'\to F\) is injective. Right exactness of the top row gives \(z=i(y')\) for some \(y'\in\Omega\otimes M'\). Injectivity for the free module \(F\), which follows by direct sums from the source example, implies that \(y\) is the image of \(y'\). Therefore \(x=0\). The leading zero drawn in the top row is not needed for this chase; no circular hypothesis is used.

## Functoriality, base change and order-one de Rham maps

For a commutative ring square and a compatible map of modules, the maps \(a\otimes m\mapsto f(a)\otimes h(m)\) carry each \(\Delta(g)\) to \(\Delta(f(g))\). They carry every indicated ideal power into its target ideal power and so induce the source tower maps. Composition is exact on tensors, and the formulas for \(i,\epsilon\) show compatibility with the first principal-parts sequence.

For \(B'=B\otimes_A A'\) and \(M'=M\otimes_A A'\), the base-changed universal map is \(j_k\otimes1\). Its \((k+1)\)-fold commutators vanish: it is enough to test the \(A'\)-algebra generators \(b\otimes1\), for which the commutator is the base change of the original one; the generator criterion is proved below. For \(k=0\) linearity is direct. Every target operator restricted to \(M\) factors uniquely through \(j_k\), and extending the factor by \(u\otimes a'\mapsto a'\gamma(u)\) gives its unique \(B'\)-linear factor. Equality and uniqueness can be checked on \(j_k(m)\otimes a'\), which generate. This proves the source arbitrary-base-change isomorphism without a flatness condition.

The earlier graded Leibniz proof gives the exact de Rham commutator \([d,b](\omega)=db\wedge\omega\). This is \(B\)-linear in \(\omega\), so \(d\) has order one in every degree, including degree zero. Expanding \(d(bb'b_0)-b\,d(b'b_0)-b'\,d(bb_0)+bb'\,d(b_0)\) gives zero: the coefficients of \(db\), \(db'\) and \(db_0\) each cancel. Wedge with the retained \(db_1,\ldots,db_i\) to obtain the source's entire displayed calculation.

For the algebra-generator criterion at 34998–35023 assume \(k\ge1\). The set of \(g\) with \(\delta_gD\) of order \(k-1\) contains the image of \(A\), since those commutators vanish. It is closed under sums and additive inverses. The identity \(\delta_{gg'}D=(\delta_gD)\circ g'+g\circ\delta_{g'}D\), together with composition with order-zero multiplication, proves closure under products. It is therefore an \(A\)-subalgebra containing the named generators, hence all of \(B\). At order zero one instead checks that all generator commutators vanish; the same identities prove linearity directly.

For the tensor lemma at 35088–35109, if \(k=0\), then \(D\) is \(A\)-linear, and for every elementary scalar \(a\otimes b\),
\[
(D\otimes1)((a\otimes b)(m\otimes n))=D(am)\otimes bn
=aD(m)\otimes bn=(a\otimes b)(D\otimes1)(m\otimes n).
\]
Sums of elementary tensors give full \(A\otimes_RB\)-linearity. For \(k\ge1\), \(D\otimes1_N\) is \(B\)-linear and its commutator with \(a\otimes1\) equals \((\delta_aD)\otimes1_N\); induction and the generator criterion give the stated order. No flatness of \(N\) enters.

## Localization and the complete fraction comparison

Use the original notation \(A\to B\), multiplicative set \(T\subset B\), and modules \(M,N\), so that the source's unnamed \(R\) at 35057–35058 is correctly read as \(A\). Set \(B_T=T^{-1}B\). In the induction, \(L_b=\delta_bD\) has order \(k-1\), with unique extension \(E_b\). The original identities give \(E_{b'b}=E_{b'}\circ b+b'\circ E_b\) and \([E_{b'},b]=[E_b,b']\), by the induction's uniqueness. Define
\[
E(m/g)=g^{-1}\bigl(D(m)-E_g(m/g)\bigr).
\]
For a common rescaling \(m/g=g'm/(g'g)\), substitute \(D(g'm)=g'D(m)+L_{g'}(m)\) and
\[
E_{g'g}(g'm/(gg'))=E_{g'}(m)+g'E_g(m/g).
\]
The second identity follows by applying \(E_{g'g}=E_{g'}\circ g+g'\circ E_g\) to the actual element \(g'm/(gg')=m/g\). Since \(E_{g'}\) extends \(L_{g'}\), the two extra terms cancel and the original fraction formula is unchanged. If \(m/g=m'/g'\) only after a torsion factor, choose \(u\in T\) with \(u(g'm-gm')=0\). Rescaling both fractions to denominator \(ugg'\) gives equal numerators \(ug'm=ugm'\). The just-proved rescaling invariance therefore establishes full representative independence even with torsion and zero divisors.

The formula is additive by choosing a common denominator and using additivity of \(D,E_g\); multiplication by an element of \(A\) commutes by their \(A\)-linearity. Taking \(g=1\), with \(E_1=0\), shows that \(E\) extends \(D\). For \(b\in B\), use \([E_g,b]=[E_b,g]\) to obtain exactly
\[
E(bm/g)-bE(m/g)
=g^{-1}\bigl(L_b(m)-E_b(m)+gE_b(m/g)\bigr)=E_b(m/g).
\]
For \(g'\in T\), the product identity for \(E_{g'g}\) gives
\[
E(m/(g'g))-(g')^{-1}E(m/g)=-(g')^{-1}E_{g'}(m/(g'g)).
\]
These are compositions of an order-\((k-1)\) operator with order-zero maps. Since \(B_T\) is generated over \(A\) by the images of \(B\) and the inverses of \(T\), the generator criterion proves that \(E\) has order \(k\). If \(E^*\) were another extension of that order, its commutator with \(g\) would extend \(L_g\), hence equal \(E_g\) by induction. The equation \(E^*(m)=gE^*(m/g)+E_g(m/g)\) forces the same displayed formula, proving uniqueness. The order-zero case is ordinary localization of a linear map. If \(0\in T\), both localized modules are zero, so the unique zero extension satisfies the same conclusion.

## Symbols and the exact connection criterion

Editorial consequence retaining the source principal parts and the specified left action. For \(k\ge1\), the tower has the exact sequence
\[
0\longrightarrow J^kW/J^{k+1}W\longrightarrow P^k(M)\longrightarrow P^{k-1}(M)\longrightarrow0.
\]
Products of the original \(\Delta(g)\) give a surjection
\[
\operatorname{Sym}^k_S(\Omega_{S/R})\otimes_SM\twoheadrightarrow J^kW/J^{k+1}W,
\quad dg_1\cdots dg_k\otimes m\longmapsto[\Delta(g_1)\cdots\Delta(g_k)(1\otimes m)].
\]
To prove that it is defined on differentials, additivity and vanishing on \(R\) follow for each \(\Delta\), and the exact product identity
\[
\Delta(ab)=(a\otimes1)\Delta(b)+(b\otimes1)\Delta(a)+\Delta(a)\Delta(b)
\]
shows Leibniz after multiplication by \(k-1\) other \(\Delta\)'s and reduction modulo \(J^{k+1}\). The factors commute, giving symmetry. Moving a scalar from \(M\) to the first-factor coefficient changes the expression by one more \(\Delta\), hence by zero in this quotient. Generation of \(J\) proves surjectivity. Injectivity is not asserted.

An operator \(D\) induces its symbol
\[
dg_1\cdots dg_k\otimes m\longmapsto(\delta_{g_1}\cdots\delta_{g_k}D)(m).
\]
It is the composite of the last surjection with \(L_D\) on the kernel of the tower map. It vanishes exactly when \(L_D\) factors through \(P^{k-1}(M)\), equivalently when \(D\) has order \(k-1\). Thus there is an injection
\[
\operatorname{Diff}^k(M,N)/\operatorname{Diff}^{k-1}(M,N)
\hookrightarrow\operatorname{Hom}_S(\operatorname{Sym}^k\Omega_{S/R}\otimes_SM,N).
\]
This construction retains every commutator and its positive \(\Delta\) sign.

At order one, an \(S\)-linear splitting \(s:M\to P^1(M)\) of \(\epsilon\) is equivalent to an \(R\)-linear connection \(\nabla:M\to\Omega_{S/R}\otimes_SM\) with
\[
\nabla(am)=a\nabla(m)+da\otimes m.
\]
Given the splitting, define \(\nabla=i^{-1}(j_1-s)\), using the proved injectivity and exactness. The identity \(j_1(am)-a j_1(m)=i(da\otimes m)\) proves the product rule. Conversely \(s=j_1-i\nabla\) is \(S\)-linear and \(\epsilon s=1\); these constructions are inverse. If one connection exists, all are obtained by adding an arbitrary \(S\)-linear map \(M\to\Omega\otimes M\), since subtraction cancels the displayed product-rule defect. This is a torsor statement only for the nonempty set of connections; no flatness or integrability of a connection is claimed.

For a concrete failure take a nonzero field \(k\), \(S=k[x]\), \(R=k\), and \(M=N=S/(x)\). Every \(k\)-linear map \(k\to k\) is \(S\)-linear because the \(S\)-action is evaluation at zero. Thus \(\operatorname{Diff}^r(M,M)=k\) for every integer \(r\ge0\), with every positive symbol zero, whereas \(\operatorname{Hom}_S(\operatorname{Sym}^r\Omega\otimes M,M)=k\) for every integer \(r\ge1\). The symbol injection is therefore not generally onto. Nor can a connection exist: applying its product rule to \(x\cdot1=0\) gives \(0=dx\otimes1\), a nonzero generator of \(\Omega\otimes M\). Explicitly \(P^1(M)=k[x]/(x^2)\): in the diagonal presentation the second coordinate is zero and \(\Delta(x)=-x\). The injection sends \(dx\otimes1\) to \(-x\), the universal class of \(1\) is \(1\), and the augmentation is reduction modulo \(x\). A section would lift \(1\) to \(1+ax\), whose product with \(x\) is the nonzero class \(x\). This proves the nonsplitting with the exact maps and signs.

## Localized principal parts and finite denominator formulas

Editorial consequence receiving the diagonal comparison and source localization theorem. Return to \(R\to S\), \(T\subset S\), and \(C_k=(S\otimes_RS)/J^{k+1}\). After inverting the first-factor elements \(g_L=g\otimes1\) for \(g\in T\), the second-factor element is \(g_R=g_L+\Delta(g)\). Since \(\Delta(g)^{k+1}=0\) in \(C_k\), it has the exact inverse
\[
g_R^{-1}=\sum_{i=0}^k(-1)^i g_L^{-i-1}\Delta(g)^i.
\]
Multiplication by \(g_L+\Delta(g)\) cancels every intermediate term and leaves \(1+(-1)^kg_L^{-k-1}\Delta(g)^{k+1}=1\). The zero-ring localization causes no exception. Thus localizing the first factor already inverts the required second-factor elements.

Localizing both factors of \(S\otimes_RS\) gives \(S_T\otimes_RS_T\). Localization is exact, so the kernel of its multiplication map is the extended ideal \(J\): applying the two localizations to the exact multiplication sequence gives that kernel and target \(S_T\). The image of \(J^{k+1}\) is the corresponding power, by expansion of products of localized generators. Therefore the preceding finite inverse gives the canonical isomorphism
\[
S_T\otimes_{S,\mathrm{left}}P^k_{S/R}(M)
\cong P^k_{S_T/R}(M_T),
\]
with \([a\otimes m]\) carried to the same localized class. A reverse map sends \(1\otimes(m/g)\) to \(g_R^{-1}(1\otimes m)\); the displayed inverse makes it defined on localization relations and the diagonal ideal power. Composites fix these generators, proving the isomorphism for arbitrary \(M\).

Apply the localized \(L_D\) to that formula. The unique extension of an order-\(k\) operator is
\[
E(m/g)=\sum_{i=0}^k(-1)^i g^{-i-1}(\delta_g^iD)(m).
\]
Every term has the original denominator power and iterated commutator. This agrees with the source's recursive formula because the extension of \(\delta_gD\) has the same formula with order \(k-1\); substituting it yields exactly the terms indexed \(1\) through \(k\).

For an integer \(n\ge1\), multiplication of \(n\) copies of the finite inverse gives
\[
E(m/g^n)=\sum_{i=0}^k(-1)^i\binom{n+i-1}{i}g^{-n-i}(\delta_g^iD)(m).
\]
Indeed for a fixed \(i\le k\), the coefficient counts ordered \(n\)-tuples of nonnegative exponents with sum \(i\); inserting \(n-1\) separators among \(i\) entries gives \(\binom{n+i-1}{i}\). Terms of total exponent above \(k\) vanish by the ideal power. These are integer coefficients, not divisions by factorials in the ring. The formula thus holds in all characteristics with zero divisors and torsion retained. It supplies a finite explicit denominator expansion of the original extension, not a modified operator.

## Polynomial principal parts with all characteristic coefficients

Editorial consequence for \(S=R[x_1,\ldots,x_n]\). Let \(\xi_i=1\otimes x_i-x_i\otimes1\). The two inverse \(S\)-algebra maps identify the original diagonal tensor algebra with \(S[\xi_1,\ldots,\xi_n]\): send the second coordinate \(1\otimes x_i\) to \(x_i+\xi_i\), and send \(\xi_i\) back to the displayed tensor difference. Multiplication sets every \(\xi_i\) to zero, so \(J=(\xi_1,\ldots,\xi_n)\). Consequently
\[
P^k_{S/R}(S)\cong S[\xi_1,\ldots,\xi_n]/(\xi_1,\ldots,\xi_n)^{k+1}
\]
is free for the left \(S\)-action on the explicitly retained monomials \(\xi^\alpha\), \(|\alpha|\le k\). The quotient has precisely those coefficients because its ideal is spanned by monomials of higher total degree. Their number is \(\binom{n+k}{k}\), counted by introducing the extra nonnegative coordinate \(k-|\alpha|\). For \(n=0\) only the empty monomial remains.

For \(f=\sum_\nu a_\nu x^\nu\) with finite support, define
\[
\partial^{[\alpha]}f
=\sum_{\nu\ge\alpha}a_\nu\left(\prod_{j=1}^n\binom{\nu_j}{\alpha_j}\right)x^{\nu-\alpha}.
\]
Binomial expansion, with every integer coefficient mapped into \(R\), gives the exact universal operator
\[
j_k(f)=[f(x+\xi)]=\sum_{|\alpha|\le k}(\partial^{[\alpha]}f)\xi^\alpha.
\]
All omitted terms are zero in the specified quotient because their total \(\xi\)-degree exceeds \(k\); no coefficient of a retained term is suppressed. For every \(S\)-module \(N\), the universal property therefore gives the explicit bijection
\[
\bigoplus_{|\alpha|\le k}N\longrightarrow\operatorname{Diff}^k_{S/R}(S,N),
\qquad(n_\alpha)_\alpha\longmapsto\left[f\mapsto\sum_{|\alpha|\le k}(\partial^{[\alpha]}f)n_\alpha\right].
\]
The inverse takes the associated linear map \(P^k(S)\to N\) on each basis monomial \(\xi^\alpha\). Equivalently its coefficient is \((\delta_{x_1}^{\alpha_1}\cdots\delta_{x_n}^{\alpha_n}D)(1)\), by the original diagonal calculation. The order drops to \(k-1\), for \(k\ge1\), exactly when all coefficients of total degree \(k\) vanish, because those basis monomials span the kernel of the tower projection.

The comparison with the ordinary iterated partial derivative is
\[
\partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}
=\left(\prod_j\alpha_j!\right)\partial^{[\alpha]}.
\]
On each monomial it follows from the exact identity \(\nu_j(\nu_j-1)\cdots(\nu_j-\alpha_j+1)=\alpha_j!\binom{\nu_j}{\alpha_j}\), and then by additivity. The multiplier is retained; it is not inverted. In particular over \(\mathbf F_p[x]\), \(\partial^{[p]}(x^p)=1\), while \(\partial^p=p!\partial^{[p]}=0\). Thus ordinary derivatives alone do not recover these original finite-order operators in positive characteristic.

## Propagation and continuation

The corrected universal factorization determines the diagonal inverse and every functorial map. The diagonal description proves the first principal-parts sequence without flatness, supplies its exact symbol and connection maps, and gives the localized comparison with finite denominator expansions. The full commutator expansion proves the source free presentation and every sign in the denominator formula. The polynomial comparison retains all binomial and factorial coefficients, including their vanishing in positive characteristic. The previous de Rham graded product rule now receives an exact principal symbol: \(db\otimes\omega\mapsto db\wedge\omega\).

The three consequence groups have no translation operations. Full proofs and extensions remain editorial. The failed symbol-surjectivity and connection examples are exact boundaries, not a claim that the structures are unrelated. Next is the naive cotangent complex at 35116; its read lookahead remains to be adjudicated. Broader synthesis follows core completion. No source or translation mutation, TeX build, publication, new task or delegation occurred.
