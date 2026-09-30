# Editorial evidence for Algebra 12926–13248

Source: the original `algebra.tex` at authority commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`. The source interval and all eight received reports were read. The exact old and proposed readings are retained in `ALGEBRA_INTAKE_REVIEW_20260925.json`, groups 368–373.

These are editorial arguments supporting small, source-linked corrections. This file is not replacement text for the translated chapter. Both current and diplomatic translations must retain the original exposition and identify mathematical source corrections visibly. The source's omitted proofs and its stated degree of generality do not create mandatory rewriting assignments. No novelty is claimed.

## Valuation quantifier

Source: `lemma-localization-at-closed-point-special-fibre`, lines 12930–12972. Report `OCC-00370` concerns lines 12951–12954: the homomorphism from the entire polynomial ring to the valuation ring requires **every** variable image to belong to that valuation ring.

Write \(P=R[x_1,\ldots,x_n]\), let \(\mathfrak q\subset P\) be the original prime, and let \(\lambda_j\) be the image of \(x_j\) in \(\kappa(\mathfrak q)\). The image \(D\) of \(R\) in this field is a quotient of the local ring \(R\), hence is a local domain. The valuation ring \(A\subset\kappa(\mathfrak q)\) chosen in the source dominates \(D\), so the inverse image of \(\mathfrak m_A\) in \(R\) is \(\mathfrak m_R\).

If all \(\lambda_j\) belong to \(A\), the original evaluation map factors as \(P\to A\subset\kappa(\mathfrak q)\). Its inverse image \(\mathfrak p\) of \(\mathfrak m_A\) is proper and contains both \(\mathfrak q\) and \(\mathfrak m_RP\). A maximal ideal \(\mathfrak m\) of \(P\) containing \(\mathfrak p\) contracts to \(\mathfrak m_R\), since its contraction is proper and contains that maximal ideal. Localizing \(P_{\mathfrak m}\) at the images of \(P\setminus\mathfrak q\) gives \(P_{\mathfrak q}\), with both comparison maps given by the original fractions.

Otherwise at least one nonzero \(\lambda_j\) lies outside \(A\). Use the additive order convention \(a\in A\setminus\{0\}\) if and only if \(v(a)\geq0\). Among the finitely many **nonzero** \(\lambda_j\), choose an index \(i\) of least value. Its value is negative. Thus \(v(\lambda_i^{-1})>0\) and \(v(\lambda_j/\lambda_i)\geq0\) whenever \(\lambda_j\ne0\). For a zero \(\lambda_j\), the ratio is zero and belongs to \(A\) directly; no value of zero is used.

For the original chart \(Q=R[y_0,y_1,\ldots,\widehat{y_i},\ldots,y_n]\), the maps

\[
\alpha:Q_{y_0}\longrightarrow P_{x_i},\qquad
y_0\longmapsto x_i^{-1},\quad y_j\longmapsto x_jx_i^{-1},
\]
\[
\beta:P_{x_i}\longrightarrow Q_{y_0},\qquad
x_i\longmapsto y_0^{-1},\quad x_j\longmapsto y_jy_0^{-1}
\]

fix \(R\) and are inverse. Indeed, \(\beta\alpha(y_0)=y_0\), \(\beta\alpha(y_j)=(y_jy_0^{-1})y_0=y_j\), \(\alpha\beta(x_i)=x_i\), and \(\alpha\beta(x_j)=(x_jx_i^{-1})x_i=x_j\); these identities also give the inverses on denominators. Since \(\lambda_i\ne0\), \(x_i\notin\mathfrak q\). The evaluation maps to \(\kappa(\mathfrak q)\) agree under these two isomorphisms. Their kernel primes therefore correspond, giving the claimed isomorphism \(Q_{\mathfrak q'}\cong P_{\mathfrak q}\), where \(\mathfrak q'\) is the inverse image of \(\mathfrak qP_{\mathfrak q}\). Every chart variable, including \(y_0\), now has image in \(A\). The preceding proper-ideal argument applies to \(Q\). When \(n=0\), the all-images condition is vacuous and the first case applies; no index is chosen.

The initial quotient reduction also preserves the original ring. If the given local ring is \(S=W^{-1}(P/I)\), let \(\mathfrak q\) be the inverse image of its maximal ideal in \(P\), and let \(U\subset P\) be the inverse image of \(W\). Every element outside \(\mathfrak q\) maps to a unit in \(S\), and \(U\cap\mathfrak q=\varnothing\). Consequently \(P_{\mathfrak q}\to S\) is defined and surjective. If \(p/t\) maps to zero, some \(u\in U\) has \(up\in I\), so \(p/t\in IP_{\mathfrak q}\). The reverse inclusion is immediate, proving \(S=P_{\mathfrak q}/IP_{\mathfrak q}\). A quotient of a localization of \(P_{\mathfrak m}\) is a localization of its quotient by the contracted ideal: both rings have fractions with the same denominators and the same zero criterion. Thus the source reduction is valid. Only the all-images quantifier needs a textual clarification.

## Nonnegative presentation rank

Source: lines 13013–13022; report `OCC-00371`. The ordinary finite free module \(R^n\) in this construction has \(n\geq0\). A finite generating list of a module \(M\), of length \(n\), defines a surjection \(R^n\to M\); its kernel \(K\) yields \(R^n/K\cong M\). The union over nonnegative integers of the sets of submodules of \(R^n\) is a set. Zero is included: \(R^0=0\) represents the zero module. Negative ranks have no meaning in the displayed construction. The correction changes only “all integers” to “all nonnegative integers”.

## Both split exact sequences

Source: lines 13068–13074 and 13147–13153. Reports `OCC-00372`, `OCC-00373`, and the overlapping report `OCC-12299` refer to the same two wrong summands. The second actual correction is at line **13152**; the overlapping report's proposed line 13157 and range 13154–13158 are stale.

In a split exact sequence \(0\to M'\xrightarrow{u}M\xrightarrow{q}M''\to0\), choose its section \(s:M''\to M\), with \(qs=1\). The maps

\[
\Phi:M'\oplus M''\to M,\quad (a,b)\mapsto u(a)+s(b),
\qquad
\Psi:M\to M'\oplus M'',\quad
m\mapsto\bigl(u^{-1}(m-sq(m)),q(m)\bigr)
\]

are defined: \(q(m-sq(m))=0\), and \(u\) is an isomorphism onto \(\ker q\). They are linear. Their composites satisfy \(\Phi\Psi(m)=m-sq(m)+sq(m)=m\) and \(\Psi\Phi(a,b)=(a,b)\). Hence the second summand is the actual quotient \(M''\). For finite free terms, adjoining their bases gives rank additivity. Over a PID or a local ring, uniqueness of finite free rank gives the source's stated relation. The wrong formula is false even for \(M'=0\), \(M=M''=R\ne0\), with the quotient map the identity. The three reports are accounted for once each.

Both minimal corrections already exist in the cumulative source as `MC-STK-ERR-1597-OP1` and `MC-STK-ERR-1597-OP2`, with the exact original authority lines 13073 and 13152. The manifest-bound unit and both current readings were inspected. This batch retains `MC-STK-ERR-1597` and records semantic agreement; it proposes no duplicate operation or new correction identity for either occurrence. An initial draft check wrongly required the whole interval to remain identical to the authority. It stopped before append. Inspection identified these two prior corrections and a separate retained FAC insertion after line 13247. The check now binds each actual edit and the retained canonical unit separately. The FAC insertion is preserved and is not newly certified by this batch.

This change does not alter the local finite-projective argument or its use at lines 13174–13180: a free module of rank \(n\) still has length \(n\operatorname{length}_R(R)\) over an Artinian local ring, by the original length additivity.

## PID subtraction and zero factors

Source: `example-K0-PID`, lines 13078–13090; report `OCC-01373`. The exact sequence \(0\to(d_i)\to R\to R/(d_i)\to0\) gives

\[
[R/(d_i)]=[R]-[(d_i)].
\]

The source prints the subtraction in the opposite order. For \(d_i\ne0\), the map \(R\to(d_i)\), \(a\mapsto ad_i\), is surjective by definition of the ideal and injective because the PID is a domain. Its inverse sends \(ad_i\) to the uniquely determined coefficient \(a\). Thus \([(d_i)]=[R]\) and the correctly signed difference is zero. Nonzero unit factors are allowed and have zero quotient.

If a displayed factor has \(d_i=0\), then \((d_i)=0\), \(R/(d_i)=R\), and its class is \([R]\), not zero. For the original displayed decomposition with arbitrary values of the \(d_i\), the exact formula is

\[
[M]=r[R]+\sum_{\{i:d_i=0\}}[R]
       +\sum_{\{i:d_i\ne0\}}\bigl([R]-[R]\bigr)
     =\bigl(r+\#\{i:d_i=0\}\bigr)[R].
\]

Every contribution is retained in the first expression; the second equality follows from the group law. The structure theorem permits choosing the torsion cyclic summands with all \(d_i\ne0\); any zero factors contribute free summands. The small proposed clarification states that choice explicitly next to the decomposition. This makes the source's subsequent isomorphism \((d_i)\cong R\) legitimate without changing the theorem or its exposition.

For completeness of the receiving identification, put \(K=\operatorname{Frac}(R)\). Localizing an exact sequence at \(R\setminus\{0\}\) remains exact: an element mapping to zero is killed by a nonzero denominator, which multiplies its numerator into the original kernel; injectivity is checked by the same zero criterion, and lifts of numerators give surjectivity. Taking finite \(K\)-dimensions therefore defines an additive rank map on \(K'_0(R)\). A nonzero \(d_i\) gives zero after localization, whereas a zero \(d_i\) gives one copy of \(K\). The map sends \([R]\) to 1, so the displayed generator formula proves its inverse is \(n\mapsto n[R]\). The original PID conclusion and its \(k[x]\) consequence at lines 13093–13098 remain valid. The separate node example at lines 13100–13106 is not proved or certified by this correction.

## Graded wording

Source: lines 13224–13228; report `OCC-01374`. Removing the comma between “definitions” and “and lemmas” changes punctuation only. The mathematical definitions, including the allowance of negative module degrees and exclusion of negative ring degrees, remain unchanged.

## Graded scalar action

Source: lines 13231–13247; report `OCC-00374`. With the source's exact convention \(N(n)_d=N_{n+d}\), an element \(f\in\operatorname{GrHom}_n(M,N)\) is an \(S\)-linear map with \(f(M_d)\subset N_{d+n}\). For homogeneous \(s\in S_e\), define \((sf)(m)=s f(m)\). The original ring is commutative, so \((sf)(am)=sa f(m)=a(sf)(m)\), proving \(S\)-linearity. The image of \(M_d\) lies in \(N_{d+n+e}\), so \(sf\) has degree \(n+e\).

For finite homogeneous decompositions \(s=\sum_e s_e\) and \(f=\sum_n f_n\), define the component of degree \(k\) of their action to be \(\sum_{e+n=k}s_ef_n\). Only finitely many components occur. Additivity, \((st)f=s(tf)\), and \(1f=f\) follow by evaluating each map on every element of \(M\) and using the module axioms of \(N\). Thus this is exactly the asserted graded \(S\)-module structure. Composable maps \(M\to N\to P\) have a graded composition, but for unrelated \(M,N\), the given data do not supply composition as an internal operation on \(\operatorname{GrHom}(M,N)\).

“Multiplication” can also mean scalar multiplication, so the original sentence is not evidence that the source falsely asserts an internal algebra structure. Classify the proposed “\(S\)-action” wording as clarification. Keep the construction here as editorial evidence; do not replace the source's deliberate omission with this expanded argument.
