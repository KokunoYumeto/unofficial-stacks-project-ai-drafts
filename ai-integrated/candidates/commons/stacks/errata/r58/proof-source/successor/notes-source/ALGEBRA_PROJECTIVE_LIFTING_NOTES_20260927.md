# Editorial evidence for Algebra 18863–19374

Primary source: Stacks Project authors, algebra.tex, commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3. The complete interval and ten due reports were read. The proofs and consequences below are editorial evidence, distinct from the proposed minimal source corrections. They are not replacements for the translated exposition.

## Original projectors and nilpotent lifting

Sources: 18863–18958; earlier idempotent lemmas 6318–6328 and 6385–6399 were consulted at their actual source loci.

If each original projective module \(P_\alpha\) is a summand of \(F_\alpha\), the direct sum of the inclusions and projections has composite identity on \(\bigoplus P_\alpha\). Its ambient \(\bigoplus F_\alpha\) is free on the disjoint union of the original bases. This proves the direct-sum assertion, including the empty sum.

For the arbitrary free module \(F=\bigoplus_{\alpha\in A}R\), lift each column of the original projector \(\overline p\) with its finite support. The resulting endomorphism \(p\) is well-defined on the direct sum. Put \(x=p^2-p\). If \(I^n=0\), then \(x(F)\subset IF\), and induction gives \(x^j(F)\subset I^jF\); hence \(x^n=0\). This argument uses the original uniform nilpotence and does not replace an infinite matrix by a finite one.

The cited noncommutative lemma applies to this actual \(x\). Its proof uses the homomorphism \(\mathbf Z[e]/((e^2-e)^n)\to\operatorname{End}_R(F)\) sending \(e\) to \(p\); it is a ring homomorphism because all polynomials in one endomorphism commute. In that commutative source ring, the ideal \((e^2-e)\) is nilpotent. The earlier idempotent-lifting lemma supplies an idempotent congruent to \(e\), giving exactly an idempotent \(p'\) congruent to \(p\) modulo endomorphisms with image in \(IF\). Thus
\[
F=\operatorname{im}p'\oplus\operatorname{im}(1-p'),
\qquad
(\operatorname{im}p')/I(\operatorname{im}p')\cong\operatorname{im}\overline p.
\]
For the last equality, reduce the displayed direct-sum decomposition modulo \(I\); the induced idempotent is precisely \(\overline p\). This also proves that the quotient map is the original reduction, rather than an unspecified isomorphism between modules of the same rank.

For a finite projective quotient, the image of finitely many generators in a free direct sum uses a finite subset of its basis. The original retraction restricts to that finite free submodule because its image is the same projective module contained there; consequently it remains a direct summand. Retain the source matrix \(p\in\operatorname{Mat}(n\times n,R)\). There are finitely many entries \(c_{ij}\) of \(p^2-p\), so a common positive \(t\) satisfies \(c_{ij}^t=0\). Every entry of \((p^2-p)^{tn^2}\) is a finite sum of products of \(tn^2\) such entries. In each product one of the \(n^2\) entries occurs at least \(t\) times. Since \(R\) is commutative, that product is zero. The printed bound therefore works without assuming the entire ideal is nilpotent. When \(n=0\), both the module and its lift are zero. Applying the same polynomial correction preserves the original reduction and gives a summand of the same finite free module.

In the flat lifting lemma, for each original exponent \(a\), flatness of a module \(T\) identifies
\[
(I^a/I^{a+1})\otimes_RT\longrightarrow I^aT/I^{a+1}T,
\quad [u]\otimes t\longmapsto[ut]
\]
as an isomorphism: tensor the two inclusions of ideals into \(R\), and then the exact sequence \(0\to I^{a+1}\to I^a\to I^a/I^{a+1}\to0\). Because \(I\) kills the first factor, this tensor product is also canonically \((I^a/I^{a+1})\otimes_{R/I}(T/IT)\), with the displayed formula unchanged. Apply this to the actual lift \(P\to M\). Its degree-zero reduction is an isomorphism, so every map on successive quotients is an isomorphism. Starting at \(I^nP=I^nM=0\), injectivity and surjectivity in each short exact sequence of successive filtration steps prove, by downward induction, that \(P\to M\) is an isomorphism. No unbounded filtration argument is being used.

## Patching over the two original ideals

Source: 18960–18989; OCC-01397 and OCC-01398.

Keep the source surjection \(p:F\to P\), ideals \(I,J\) with \(I\cap J=0\), and original maps \(f,q,f',g\). To prove the omitted surjectivity of \(q\), let \((\overline v,\overline w)\) be in its target fibre product. Choose representatives \(v\in F\), \(w\in P\). Compatibility says \(w-p(v)\in(I+J)P\). Write it as \(x+y\) with \(x\in IP\), \(y\in JP\). The equality \(p(IF)=IP\) supplies \(u\in IF\) with \(p(u)=x\). The class of \(v+u\) in \(F/JF\) maps to the specified pair: its first component is \(\overline v\), and its image under \(p\) is \(w-y\), which has class \(\overline w\) modulo \(JP\). This proves surjectivity using exactly the original modules.

The map induced by \(f\) on \(P/(I+J)P\) is well-defined because the \(R\)-linear \(f\) sends the image of \(JP\) in \(P/IP\) into the image of \(JF\) in \(F/IF\). This defines \(f'\). Projectivity over \(R/J\) then gives the stated \(g\), and \(qg=f'\) is the exact compatibility of their reductions.

The natural map
\[
F\longrightarrow(F/IF)\times_{F/(I+J)F}(F/JF)
\]
is injective since, coordinate by coordinate on the original free basis, \(IF\cap JF=(I\cap J)F=0\). It is surjective: if representatives \(u,v\in F\) satisfy \(u-v=i+j\) with \(i\in IF\), \(j\in JF\), then \(u-i=v+j\) represents both required classes. The construction gives the original \(h:P\to F\), whose reductions are \(f,g\).

Set \(a=ph\) and \(t=a-\operatorname{id}_P\). The reductions of \(a\) are identities, so \(t(P)\subset IP\cap JP\). For each \(x_\alpha\in P\), the difference
\[
j_\alpha=a(x_\alpha)-x_\alpha
\]
is an element of \(JP\), not an element of the ideal \(J\). Write \(j_\alpha=\sum_\beta j_{\alpha\beta}p_{\alpha\beta}\) with \(j_{\alpha\beta}\in J\). For \(i_\alpha\in I\), every \(i_\alpha j_{\alpha\beta}\) is zero because \(IJ\subset I\cap J=0\). Therefore \(i_\alpha j_\alpha=0\), and \(t(IP)=0\). Since \(t(P)\subset IP\), it follows that \(t^2=0\).

In particular the omitted inverse has the exact formula
\[
a^{-1}=\operatorname{id}_P-t=2\operatorname{id}_P-a,
\qquad
\sigma=h(2\operatorname{id}_P-a),\qquad p\sigma=\operatorname{id}_P.
\]
Both products \((1+t)(1-t)\) and \((1-t)(1+t)\) are \(1-t^2=1\); this uses no division by two and works in every characteristic. The explicit section proves projectivity. The proposed source edits insert the missing “is” and correct membership to \(JP\); they do not replace the author's omitted details with this full proof.

## Finite-projective criteria and the localization element

Sources: 19000–19208; OCC-01310, OCC-00443, OCC-01399 and OCC-01400.

The tab on line 19024 is a whitespace byte in source, not an extra mathematical symbol or a rendered mathematical error. Removing it is source hygiene only. Uniqueness of rank still requires a nonzero ring, as the author states.

For OCC-00443 retain the original prime \(\mathfrak p\), element \(g\notin\mathfrak p\), and surjection \(\varphi:R_g^r\to M_g\). Its finite kernel has zero fibre at \(\mathfrak pR_g\), so localized Nakayama supplies \(g'\in R_g\setminus\mathfrak pR_g\) with \((\ker\varphi)_{g'}=0\). Write the actual \(g'\) as \(h/g^a\), where \(a\geq0\), \(h\in R\). The avoidance condition gives \(h\notin\mathfrak p\). Inverting \(gh\) inverts \(g\) and \(h\), hence \(g'=h/g^a\). Conversely in \((R_g)_{g'}\), the equality \(h=g^ag'\) makes \(gh\) invertible. The universal localization maps are inverse and preserve the original fractions. Tensoring them with the original module gives
\[
(M_g)_{g'}\cong M_{gh}.
\]
Thus \(D(gh)\) is an original-ring neighbourhood of \(\mathfrak p\), and \(M_{gh}\) is free of the same rank \(r\). Writing \(gg'\) as if \(g'\in R\) did not specify this original-ring localization. The proposed correction retains the actual fraction and its numerator, rather than silently changing the chosen ring.

The rest of the equivalence proof retains its hypotheses. A finite free summand is finite and projective; its complement is finite, giving a finite presentation of the original quotient. The original finite-presentation hypothesis permits the Hom-localization comparison. For a short exact sequence, the three localized Hom terms agree with Hom out of the locally free module; their exactness detects the original exactness on the open cover. The two grammar repairs in this paragraph affect neither that map nor its cover.

For (8), the source map \(\Psi:R_{fg}^r\to M_{fg}\) is surjective and, at every prime in \(D(fg)\), both source and target are free of rank \(r\). After choosing bases locally its matrix has a right inverse. Taking determinants makes its determinant a unit; the adjugate formula supplies the inverse. The zero-rank case is the unique map between zero modules. This validates the map referred to by the missing subject in OCC-01400.

In the reduced-ring criterion keep the same \(\Psi\). At each minimal prime the localized ring is the original residue field and the two finite dimensions coincide, so the kernel localizes to zero. A vector in the kernel has each coordinate zero in every such localization. The canonical injection of a reduced ring into the product of these fields kills no nonzero coordinate; hence the vector is zero. Surjectivity was already established. This proves the source's conclusion without deleting the reducedness assumption.

## The smooth-function counterexample

Source: 19210–19220; OCC-01401.

Keep \(R=\mathcal C^\infty(\mathbf R)\), \(\mathfrak m=\{f:f(0)=0\}\), and the printed ideal \(I\) of functions vanishing on some neighbourhood of zero. The kernel of \(R\to R_{\mathfrak m}\) is exactly \(I\). If \(gf=0\) with \(g(0)\ne0\), continuity makes \(g\) nonzero near zero, so \(f\) vanishes there. Conversely, for \(f\in I\), choose a smooth cutoff \(\chi\), equal to one near zero and supported inside a neighbourhood where \(f=0\). Then \(\chi f=0\) and \(\chi\notin\mathfrak m\).

This localization map is surjective. Given \(f/g\) with \(g(0)\ne0\), choose such a cutoff supported in the open set where \(g\ne0\), and define \(h=\chi f/g\) on that open set and zero outside. Its support is contained there, so the extension is smooth. Near zero, \(gh=f\), and therefore \(f-gh\in I\); its localization vanishes. Thus \(f/g=h/1\). These constructions prove the author's exact isomorphism \(R/I\cong R_{\mathfrak m}\), with the actual quotient map.

Consequently \(M\) is cyclic and flat. If it were projective, the quotient \(R\to R/I\) would split and its kernel \(I\) would be an idempotent-generated summand of \(R\). Every smooth idempotent takes only values zero and one, and continuity on connected \(\mathbf R\) forces it to be constant. But \(I\) is nonzero (take a nonzero bump function supported away from zero) and proper (it does not contain one). This contradiction proves the source counterexample. The accepted edit only joins the noun “counterexample”; it is not a mathematical correction to this example.

## Local flatness, descent and semilocal bases

Sources: 19222–19347; OCC-00444 and OCC-01402.

For the local flatness proof, the equational criterion converts each finite relation \(\sum_i f_i x_i=0\) into the source equations \(x_i=\sum_j a_{ij}y_j\) and \(\sum_i f_i a_{ij}=0\). If the residues of \(x_1,\ldots,x_n\) are independent, then some \(a_{nj}\) is a unit. Substitution gives exactly
\[
f_n=\sum_{i<n}(-a_{ij}/a_{nj})f_i,
\qquad
\sum_{i<n}f_i\bigl(x_i+(-a_{ij}/a_{nj})x_n\bigr)=0.
\]
If a residue-field linear combination of the displayed \(n-1\) modified vectors vanishes, independence of the original \(n\) residues makes every coefficient zero. Induction therefore gives every \(f_i=0\), and the displayed first equality then gives \(f_n=0\). In degree one, the same criterion gives a unit coefficient annihilated by \(f\), hence \(f=0\). In degree zero the zero set is independent. Nakayama gives the original finite generating family from a residue basis; its independence proves that a finite flat module over a local ring is free.

For the local descent lemma, the residue field is \(\kappa(\mathfrak m_R)\), correcting the otherwise undeclared ideal. For the original local map \((R,\mathfrak m_R)\to(S,\mathfrak m_S)\), its residue-field map is injective. The residue of the free \(S\)-module \(M\otimes_RS\) is
\[
(M/\mathfrak m_RM)\otimes_{\kappa(\mathfrak m_R)}\kappa(\mathfrak m_S).
\]
The selected basis tensors to a residue basis. Nakayama makes it a generating set, and its size equals the rank of the free \(S\)-module. The determinant argument just given makes the corresponding square matrix invertible. Faithful flatness of the original local map then kills both kernel and cokernel of \(R^r\to M\), proving the asserted descent. The forward implication follows by tensoring a direct-summand decomposition.

For constant rank \(d\) over a nonzero semilocal ring, the finitely many maximal ideals \(\mathfrak m_i\) are pairwise comaximal. The Chinese remainder map
\(M\to\prod_iM/\mathfrak m_iM\)
is surjective: choose ring elements that are one at one maximal ideal and zero at all others, and form their finite linear combination of representatives. Lift the \(j\)-th vector of a basis at every maximal ideal simultaneously to \(x_j\in M\), for \(1\leq j\leq d\). The map \(R^d\to M\) is an isomorphism at every maximal ideal by Nakayama and the square-matrix determinant argument. Its kernel and cokernel are therefore zero, since any nonzero module has a nonzero localization at some maximal ideal. This proves the hinted argument. Over the zero ring the only module is zero, so the assertion is immediate. Connected nonempty spectrum makes the locally constant rank constant, as stated by the author. Only the singular “ideal” in the hint is corrected in the source proposal.

For the basis-in-submodule lemma retain the source quotients by \(I=\operatorname{Jac}(S)\). Because \(\mathfrak mN\subset IM\), the image of \(N\) is indeed a vector space over the original infinite field \(k=R/\mathfrak m\). For \(S\ne0\), write the source quotient as \(\prod_{i=1}^r k_i\). When \(n>0\), choose finitely many \(x_j\in N\) with a nonzero image in every factor among them; such a family exists because \(N\) generates \(M\). For each \(i\), the \(k\)-linear map \((c_j)\mapsto\sum_j c_j(x_j)_i\) has a proper kernel. A finite union of proper subspaces cannot fill the finite-dimensional vector space over infinite \(k\): choose a nonzero linear functional vanishing on each subspace, take the product of those linear forms, and use induction on the number of variables to see that a nonzero polynomial cannot vanish on all of \(k^m\). Thus some original coefficient vector gives \(y\in N\) nonzero in every factor. In each factor its vector spans a direct summand; together these give \(Sy\cong S\) with free quotient of rank \(n-1\). Apply induction to the image of \(N\) and lift the resulting basis. The base \(n=0\), and the case \(S=0\), are immediate. These details verify the source use of infinitude; they introduce no replacement hypothesis.

## Constant fibre rank and the exact nilradical kernel

This is a separate consequence of the original finite-projective lifting lemma, reduced-ring criterion, and local flatness result. No source statement is replaced.

Let \(R\) be any commutative ring, \(\mathcal N=\sqrt{(0)}\) its actual nilradical, and \(M\) a finite \(R\)-module. The following are equivalent:

1. The original function \(\rho_M(\mathfrak p)=\dim_{\kappa(\mathfrak p)}(M\otimes_R\kappa(\mathfrak p))\) is locally constant.
2. There exists a finite projective \(R\)-module \(P\) and a surjection \(\pi:P\to M\) whose actual kernel \(K\) is contained in \(\mathcal NP\).

For (1), set \(\overline R=R/\mathcal N\) and \(\overline M=M/\mathcal NM\). Each prime of \(R\) contains \(\mathcal N\), so the quotient gives a homeomorphism of spectra with the corresponding residue fields unchanged. The explicit fibre map
\[
(M/\mathcal NM)\otimes_{R/\mathcal N}\kappa(\mathfrak p/\mathcal N)
\longrightarrow M\otimes_R\kappa(\mathfrak p),
\quad (m+\mathcal NM)\otimes c\longmapsto m\otimes c
\]
is well-defined and has the inverse induced by \(m\mapsto m+\mathcal NM\). Hence the same rank function is locally constant for \(\overline M\). The proved reduced-ring criterion makes \(\overline M\) finite projective over \(\overline R\). Every finite subset of \(\mathcal N\) generates a nilpotent ideal: if its generators have powers \(a_i^{t_i}=0\), every product of more than \(\sum_i(t_i-1)\) generators vanishes. Thus the finite-projective lifting lemma applies to the actual nilradical, even if that ideal is not nilpotent. It gives finite projective \(P\) and an isomorphism \(\alpha:P/\mathcal NP\to\overline M\).

Projectivity lifts the composite \(P\to P/\mathcal NP\xrightarrow\alpha\overline M\) through the actual quotient \(M\to\overline M\), producing \(\pi:P\to M\). Its cokernel \(C\) is finite and satisfies \(C/\mathcal NC=0\). Since \(\mathcal N\) lies in every maximal ideal, Nakayama gives \(C=0\). If \(p\in\ker\pi\), then \(\alpha(p+\mathcal NP)=0\); injectivity of \(\alpha\) gives \(p\in\mathcal NP\). This proves the asserted surjection and exact kernel containment.

Conversely, such a surjection gives
\[
M/\mathcal NM=P/(K+\mathcal NP)=P/\mathcal NP.
\]
The residue-field maps are the same maps induced by \(\pi\). Therefore \(\rho_M=\rho_P\), a locally constant function because \(P\) is finite projective. This proves (2) implies (1).

For every such \(\pi\), the module \(M\) is flat if and only if \(K=0\). One implication is immediate from \(M\cong P\). For the other, if \(M\) is flat, then at every prime both \(P_{\mathfrak p}\) and \(M_{\mathfrak p}\) are finite free by the original local theorem. Their ranks agree by the proved fibre comparison. The surjection \(\pi_{\mathfrak p}\) is consequently a square invertible matrix (including rank zero), so \(K_{\mathfrak p}=0\) for every prime. A nonzero element of \(K\) would have a proper annihilator contained in a maximal ideal and would survive there, a contradiction. Hence \(K=0\). This proves an exact obstruction statement about the original kernel, without discarding it or asserting that some common nilpotence exponent exists.

The obstruction can be nonzero. For \(R=k[\epsilon]/(\epsilon^2)\), \(M=R/(\epsilon)\), the unique prime gives constant fibre rank one. The original quotient \(R\to M\) has kernel \((\epsilon)\subset\mathcal NR\), which is nonzero. Thus \(M\) is not flat or projective. Directly, tensoring the inclusion \((\epsilon)\hookrightarrow R\) with \(M\) gives the zero map from a nonzero copy of \(k\). This verifies that the reducedness hypothesis of the original projectivity criterion cannot simply be erased.

A receiving consequence is the finite version of the earlier lifting theorem for any nil ideal \(I\): if \(M\) is finite flat and \(M/IM\) is projective over \(R/I\), then \(M\) is projective over \(R\). Indeed \(M/IM\) is finite projective, its rank is locally constant, and the quotient by the nil ideal identifies spectra and residue fields exactly as above. Thus \(\rho_M\) is locally constant, and the just-proved kernel criterion forces \(M\) to be finite projective. Conversely base change of a finite-projective summand is finite projective. This does not claim the same relaxation for arbitrary nonfinite modules, and the source's unrestricted nilpotent theorem remains intact.

## Evaluation and the converse dual-basis criterion

Source: 19349–19369; OCC-01403. Inserting the missing article is the only proposed source edit here.

Retain the canonical map
\[
\Phi:\operatorname{Hom}_R(M,N)\otimes_RL\longrightarrow
\operatorname{Hom}_R(M,N\otimes_RL),
\quad f\otimes\ell\longmapsto(m\mapsto f(m)\otimes\ell).
\]
For finite projective \(M\), choose a splitting of a finite free module and let \(m_i\in M\), \(\lambda_i\in M^*=\operatorname{Hom}_R(M,R)\) be the images of its basis vectors and restrictions of its coordinate functionals. The composite of projection and inclusion is the identity, so
\[
m=\sum_{i=1}^n\lambda_i(m)m_i\quad\text{for every }m\in M.
\]
For \(T:M\to N\otimes_RL\), write \(T(m_i)=\sum_j n_{ij}\otimes\ell_{ij}\). Define
\[
\Theta(T)=\sum_{i,j}(m\mapsto\lambda_i(m)n_{ij})\otimes\ell_{ij}.
\]
This is independent of each tensor presentation: for fixed \(i\), the map \(N\times L\to\operatorname{Hom}(M,N)\otimes L\), \((n,\ell)\mapsto(m\mapsto\lambda_i(m)n)\otimes\ell\), is balanced and therefore factors through \(N\otimes_RL\). Evaluating on \(m\) gives \(\Phi\Theta(T)(m)=\sum_i\lambda_i(m)T(m_i)=T(m)\). Conversely \(\Theta\Phi(f\otimes\ell)=\sum_i(m\mapsto\lambda_i(m)f(m_i))\otimes\ell=f\otimes\ell\). Thus these are actual inverse maps for the source assertion.

There is also an exact converse for an arbitrary module \(M\). It suffices that the identity belongs to the image of the single canonical map
\[
\eta:M^*\otimes_RM\longrightarrow\operatorname{End}_R(M),
\quad \lambda\otimes m\longmapsto(x\mapsto\lambda(x)m).
\]
If \(\operatorname{id}_M=\eta(\sum_{i=1}^n\lambda_i\otimes m_i)\), set
\[
s:M\to R^n,\quad x\mapsto(\lambda_1(x),\ldots,\lambda_n(x)),
\qquad
t:R^n\to M,\quad(a_i)\mapsto\sum_i a_i m_i.
\]
Then \(ts=\operatorname{id}_M\), proving that the original \(M\) is a finite-projective summand. Its complement is \(\ker t\): the explicit mutually inverse decomposition maps are \((x,z)\mapsto s(x)+z\) and \(v\mapsto(t(v),v-st(v))\). Conversely a finite-projective splitting gives the identity tensor just constructed. This includes \(M=0\) using the empty sum.

Taking \(N=R\), \(L=M\) in \(\Phi\), and using the canonical map \(R\otimes_RM\to M\), identifies that instance with \(\eta\). Hence the source isomorphism for all \(N,L\) is equivalent to finite projectivity, and the weaker requirement that this one map hit the identity already suffices. The original forward lemma is retained; this proved converse is recorded separately as an underclaim consequence.

## Reading and preservation limits

The complete current interval agrees with the authority after removing exactly one retained FAC reference/history pair at the finite-projective criterion. There are no earlier canonical correction operations in this interval. The FAC passage is retained without a new audit of its external historical assertions.

The next source section at 19375–19414 was read only as lookahead: it contains the complete first surjectivity-locus lemma and the beginning of the next statement. It has not been adjudicated in this batch.

Three bounded canonical-corpus queries were executed: literal terms “finite projective”, that exact phrase, and the exact phrase “projective module” together with “nilpotent”. The first two routed to unrelated geometry or local work; the last supplied only PDF-primary records. Those hits were not read or adopted, and no PDF fallback was used. The exact supplied Stacks TeX and the explicitly located prior source lemmas provide the proof dependencies here. These standard consequences are not asserted to be novel, and the bounded queries are not an exhaustive literature survey. The broader synthesis remains after the core work.
