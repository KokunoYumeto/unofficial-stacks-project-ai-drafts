# Cohen–Macaulay loci: original charts, base changes and component maps

Source: Stacks Project authors, algebra.tex:33515–33787, authority a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3. All twelve reports OCC-00665–OCC-00676 were read. There are no earlier canonical operations in this interval. Lookahead 33788–33890 is read but unadjudicated.

Original TeX dependencies reread: 27475–27533, 28048–28105, 24180–24254, 28300–28365, 4376–4438, and 31160–31226. The preceding source-bound notes for fibre dimension, local flatness and openness of flatness supply the already proved receiving arguments. All complete proofs and stronger consequences below are separate editorial material. No translation is silently recast; no novelty is claimed.

## Report dispositions and the empty-fibre boundary

The omitted complementizer in “prove the set ... is open” and the abbreviated “Trivial from ...” proof are optional prose, not false mathematics. Retain those passages. Supply the two short predicate verbs in the displayed sets, use “Set” for the contraction at 33540, specify \(\operatorname{Spec}(S)\) at 33575, repair the \(k\)-algebra spelling, retain the fixed relative dimension in the proof's local goal, add its intervening comma, supply “by” in the two final declarations, and make the three map predicates grammatically parallel.

At 33762 explicitly say “all nonempty fibres”. A factor in the product can have empty fibres, even when the original algebra has a point over each base prime. For example let \(R=k\times k\) and \(S=k[x]\times k\), with the componentwise structural map. It is flat and finitely presented over \(R\), with Cohen–Macaulay fibres. Its dimension-one factor \(k[x]\) has empty fibre over the second component of the base; its dimension-zero factor \(k\) has empty fibre over the first. The intended component-dimension assertion applies to each nonempty fibre and keeps the zero factors and empty spectra harmless. This clarification does not replace any nonempty fibre by another object.

## The original quasi-finite flat chart criterion

Let \(k\) be a field, \(S\) a finite-type \(k\)-algebra and \(P=k[y_1,\ldots,y_d]\to S\) the original quasi-finite map. For \(\mathfrak q\subset S\), retain the actual contraction \(\mathfrak p\subset P\), and write \(A=P_{\mathfrak p}\), \(B=S_{\mathfrak q}\). These are nonzero Noetherian local rings and their map is local. Quasi-finiteness gives \(\dim(B/\mathfrak pB)=0\), the dimension inequality \(\dim B\leq\dim A\), and a finite residue-field extension \(\kappa(\mathfrak q)/\kappa(\mathfrak p)\).

If \(B\) is \(P\)-flat, it is \(A\)-flat. The source lemma at 27489–27503 has a second alternative: flatness together with \(\dim B\leq\dim A\) suffices. This alternative applies since \(A\) is regular, hence Cohen–Macaulay. One must not pretend that the localized quasi-finite map \(A\to B\) is necessarily finite. It follows that \(B\) is Cohen–Macaulay and \(\dim B=\dim A\). Retaining the source point-dimension formula and the exact residue fields gives
\[
\dim_{\mathfrak q}(S/k)
=\dim B+\operatorname{trdeg}_k\kappa(\mathfrak q)
=\dim A+\operatorname{trdeg}_k\kappa(\mathfrak p)=d.
\]

Conversely, if \(B\) is Cohen–Macaulay and the left side is \(d\), equality of the two transcendence degrees implies \(\dim B=\dim A\). Together with \(\dim(B/\mathfrak pB)=0\), this is the dimension identity required by miracle flatness. The original \(A\) is regular. The source local criterion therefore proves \(B\) flat over \(A\), and then over \(P\), since \(A\) is a localization of \(P\). This proves both directions of the displayed source locus identity with the original objects and maps.

For the field case of openness, at a Cohen–Macaulay prime use the original Noether normalization at that point: some \(S_g\) has a finite injective map from \(k[y_1,\ldots,y_d]\), where \(d=\dim_{\mathfrak q}(S/k)\). Apply the just-proved criterion at that prime, then the proved openness-of-flatness theorem to obtain a further principal neighborhood flat over the same polynomial algebra. The map remains quasi-finite after this localization. The criterion at each remaining prime makes every local ring Cohen–Macaulay.

Every minimal prime of a finite-type algebra over a field belongs to this open: its local ring is zero-dimensional Noetherian, hence Artinian and Cohen–Macaulay. The spectrum of such an algebra is Noetherian, and every nonempty open meets a minimal prime of a component it meets. Thus the open is dense, including the vacuous assertion when the spectrum is empty.

## The original relative proof with fixed dimension retained

Let \(R\to S\) be flat of finite presentation and let \(\mathfrak q\) have Cohen–Macaulay fibre local ring and relative dimension \(d\). Write \(\mathfrak p=R\cap\mathfrak q\). The source quasi-finite chart lemma at 31170–31208 gives a principal neighborhood of \(\mathfrak q\) and an actual quasi-finite map
\[
P=R[t_1,\ldots,t_d]\longrightarrow S.
\]
Retain these original parameter images and set \(\mathfrak q'=P\cap\mathfrak q\). On the residue-field fibre the preceding field criterion gives flatness of
\[
P_{\mathfrak q'}/\mathfrak pP_{\mathfrak q'}
\longrightarrow S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}.
\]
Apply the local fibre criterion to \(R_{\mathfrak p}\to P_{\mathfrak q'}\to S_{\mathfrak q}\) and \(M=S_{\mathfrak q}\). The last module is nonzero and free of rank one over its own local ring, is flat over \(R_{\mathfrak p}\), and has the closed-fibre flatness just proved. Both displayed algebras are essentially finitely presented over \(R_{\mathfrak p}\). Thus \(S_{\mathfrak q}\) is \(P_{\mathfrak q'}\)-flat.

The map \(P\to S\) is finitely presented, a hypothesis worth verifying before applying openness of flatness. Write the actual finite presentation \(S=R[x_1,\ldots,x_m]/(h_1,\ldots,h_l)\), including any variables and inverse equations introduced by the principal localization. Choose polynomial representatives \(F_j(x)\) for the actual images of \(t_j\). Then
\[
S\cong
P[x_1,\ldots,x_m]/
(h_1,\ldots,h_l,\ t_1-F_1(x),\ldots,t_d-F_d(x)).
\]
The mutually inverse maps send each original \(x_a\) and \(t_j\) to its specified element; every original relation is retained. This proves finite presentation over \(P\).

Openness of flatness now supplies a further \(g\notin\mathfrak q\) for which \(S_g\) is flat over \(P\). At every \(\mathfrak r\subset S_g\), contract to \(\mathfrak r'\subset P\) and \(\mathfrak p'\subset R\). Base change of the local flat map to the fibre over \(\mathfrak p'\), followed by the field criterion, proves both that its fibre local ring is Cohen–Macaulay and that
\(\dim_{\mathfrak r}(S_g/R)=d\).
The proof's intermediate goal must retain this fixed-dimension conclusion; Cohen–Macaulayness alone would not identify the displayed locus.

The union over \(d\) of these open strata is the fibre Cohen–Macaulay locus \(W\). On each fibre it is exactly the open Cohen–Macaulay locus of the corresponding finite-type algebra over its residue field, hence dense there. It is also dense in the total spectrum: any nonempty open contains a point, and its intersection with that point's fibre is nonempty open in the fibre, so it meets \(W\).

## Field extension and the actual local tensor comparison

Retain \(S_K=K\otimes_k S\) and a prime \(\mathfrak q_K\) over \(\mathfrak q\). The original pointwise Noether normalization provides a principal localization with finite injective \(P=k[x_1,\ldots,x_d]\to S\), where \(\dim_{\mathfrak q}(S/k)=d\). Flat extension of the field preserves this finite injection. The source point-dimension result at 28307–28355 proves
\(\dim_{\mathfrak q_K}(S_K/K)=d\).

Write \(\mathfrak p=P\cap\mathfrak q\), \(P_K=K[x_1,\ldots,x_d]\), and \(\mathfrak p_K=P_K\cap\mathfrak q_K\). In the original square of local rings, the bottom map \(P_{\mathfrak p}\to(P_K)_{\mathfrak p_K}\) is flat. The top-right ring \((S_K)_{\mathfrak q_K}\) is the localization of
\[
S_{\mathfrak q}\otimes_{P_{\mathfrak p}}(P_K)_{\mathfrak p_K}
\]
at the prime induced by \(\mathfrak q_K\), not an unqualified tensor equality. Every denominator from \(S\setminus\mathfrak q\) and \(P_K\setminus\mathfrak p_K\) is a unit there, so the universal property gives the original ring with precisely that remaining prime localization.

The source flat-up-and-down result at 24185–24236 therefore proves that the two vertical maps are flat simultaneously. Its downward implication is faithful descent through the top local flat map and retains the actual localization. Apply the field chart criterion on each side to conclude
\[
S_{\mathfrak q}\text{ is Cohen–Macaulay}
\quad\Longleftrightarrow\quad
(S_K)_{\mathfrak q_K}\text{ is Cohen–Macaulay}.
\]
This proof does not assume that \(K/k\) is algebraic, finite or separable.

For any finite-type map \(R\to S\), any \(R\to R'\), and \(S'=R'\otimes_R S\), a prime \(\mathfrak q'\subset S'\) gives contractions \(\mathfrak q\subset S\), \(\mathfrak p'\subset R'\), \(\mathfrak p\subset R\). The new fibre local ring is a prime localization of the old fibre algebra
\(S\otimes_R\kappa(\mathfrak p)\)
after the exact field extension
\(\kappa(\mathfrak p)\to\kappa(\mathfrak p')\).
The preceding equivalence proves the source equality \(W'=f^{-1}(W)\). In addition, the point-dimension theorem proves equality of the relative dimensions at \(\mathfrak q'\) and \(\mathfrak q\). Neither equality needs flatness of the base change.

## A maximal open without assuming global flatness

Group 878. Suppose only that \(R\to S\) is finitely presented. Define
\[
C_d=\{\mathfrak q:S_{\mathfrak q}\text{ is }R\text{-flat},
\ S_{\mathfrak q}\otimes_R\kappa(\mathfrak p)\text{ is Cohen–Macaulay},
\ \dim_{\mathfrak q}(S/R)=d\},
\qquad \mathfrak p=R\cap\mathfrak q.
\]
Then each \(C_d\) is open. At a point of \(C_d\), choose the original quasi-finite \(d\)-parameter chart \(P=R[t_1,\ldots,t_d]\to S_g\). Within that chart the exact equality is
\[
C_d\cap D(g)
=\{\mathfrak r\in D(g):(S_g)_{\mathfrak r}
       \text{ is flat over }P\}.
\]
Indeed \(P\)-flatness implies \(R\)-flatness because \(P\) is \(R\)-flat, and the field chart criterion on every fibre proves Cohen–Macaulayness and relative dimension \(d\). In the other direction, apply the local fibre criterion exactly as in the preceding relative proof, using the assumed flatness of the one local ring \((S_g)_{\mathfrak r}\) over \(R\), not global flatness of \(S_g/R\). The same finite presentation over \(P\) proved there allows openness of its flat locus. This proves the equality and openness near every point of \(C_d\).

Let \(C=\bigcup_d C_d\). It is the largest open part on which the original morphism is flat with Cohen–Macaulay fibres. Any such open has every local ring flat over \(R\) and every fibre local ring Cohen–Macaulay, so is contained in \(C\). Conversely those two properties hold at every point of \(C\), which is precisely their local meaning for the restricted morphism. The \(C_d\) are disjoint and open; each is closed in \(C\), since its complement there is the union of the others. Finite type bounds the fibre dimension by the number of generators in any fixed algebra presentation, so only finitely many \(d\) occur.

For a flat base change \(R\to R'\), the \(C_d\) pull back exactly. The ordinary flat-locus equality from group 865 and the just-proved arbitrary-base-change invariance of fibre Cohen–Macaulayness and relative dimension prove all three conditions. For arbitrary base change the inverse image is contained in \(C'_d\), but equality can fail: take \(R=k[t]\), \(S=k=R/(t)\). The source algebra is finitely presented and every nonempty fibre is Cohen–Macaulay of relative dimension zero, but its sole local ring is not \(R\)-flat because multiplication by \(t\) kills a nonzero module. Thus \(C=\varnothing\). After base change to \(R'=k\), the map is the identity of \(k\), and \(C'_0=\operatorname{Spec}k\).

## Universal dimension strata and their radical ideals

Group 879. For any finite-type \(R\to S\), let \(W_d\) consist of the primes whose fibre local ring is Cohen–Macaulay and whose relative dimension is \(d\). The field-extension proof gives, for every ring map \(R\to R'\),
\[
W'_d=f^{-1}(W_d)
\]
with no flatness or finite-presentation hypothesis for this set identity. Flatness and finite presentation of \(S/R\) make these sets open by the source theorem; the base-changed map remains flat and finitely presented, so the new sets are open too.

Under these latter hypotheses define the actual radical ideal
\[
J_d=\{s\in S:D(s)\subset W_d\}
    =\bigcap_{\mathfrak q\notin W_d}\mathfrak q .
\]
The principal-open union and prime-intersection identities prove \(W_d=D(J_d)\); closure under addition and multiplication and radicality follow from
\(D(a+b)\subset D(a)\cup D(b)\), \(D(ab)\subset D(a)\), and \(D(a^n)=D(a)\).
The exact set identity under arbitrary base change therefore gives
\[
J'_d=\sqrt{J_d S'}
\]
for every \(R\to R'\), including nonflat maps. The same proof applies to the union \(W\). This differs from the ordinary flat-open ideal law, which needs a flat base change for equality. No finite generation of these ideals is asserted.

On \(W=\coprod_d W_d\) relative dimension is a locally constant function with finite range, bounded by a fixed number of algebra generators. Each \(W_d\) is closed in \(W\), not necessarily closed in \(\operatorname{Spec}S\). For a flat finitely presented map, \(W\) is dense in every fibre and in the total spectrum as proved above. These assertions retain the original relative point-dimension function, not the varying Krull dimensions of the fibre local rings.

## Canonical dimension idempotents with all nilpotents retained

Group 880. Assume \(R\to S\) is flat, finitely presented, and has Cohen–Macaulay fibres. Choose any finite algebra generating list of size \(n\). Every fibre is a quotient of an \(n\)-variable polynomial ring over a field, so at every point \(0\leq\dim_{\mathfrak q}(S/R)\leq n\). Thus
\[
\operatorname{Spec}S=\coprod_{d=0}^n W_d .
\]
Each \(W_d\) is open and its complement is the finite union of the other opens, hence it is closed. The original disjoint-decomposition lemma gives an idempotent \(e_d\in S\) with \(D(e_d)=W_d\).

These idempotents are unique, including empty strata. If \(e,f\) are idempotents defining the same open, then \(e(1-f)\) and \(f(1-e)\) are idempotents with empty basic opens. Such an idempotent lies in every prime and is nilpotent, hence is zero. Therefore \(e=ef=f\). The same argument proves \(e_de_c=0\) for \(d\ne c\), and \(1-\sum_d e_d=0\). This reasoning does not replace \(S\) by its reduced ring.

Define the original component algebra
\[
S_d=e_dS=S/(1-e_d)S\cong S_{e_d},
\]
with unit \(e_d\) and structural map \(r\mapsto e_d\varphi(r)\). The exact mutually inverse product maps are
\[
S\longrightarrow\prod_{d=0}^nS_d,\quad s\longmapsto(e_ds)_d,
\qquad
(s_d)_d\longmapsto\sum_{d=0}^n s_d.
\]
All original nilpotents survive in their corresponding factors. Since \(S_d\) is an \(R\)-module direct summand of the flat module \(S\), it is \(R\)-flat. Its displayed quotient adds the one relation \(1-e_d\) to a finite algebra presentation, so it is finitely presented over \(R\). Every nonempty fibre is Cohen–Macaulay and equidimensional of dimension \(d\): all of its points have the original point-dimension value \(d\), in particular its generic points; their component closures therefore have dimension \(d\). Empty fibres and zero factors require no finite numerical dimension assertion.

For every \(R\to R'\), the image \(e'_d=e_d\otimes1\) has basic open \(f^{-1}(W_d)=W'_d\), by the preceding arbitrary-base-change result. Uniqueness makes it the dimension-\(d\) idempotent of \(S'=S\otimes_R R'\). The component comparison
\[
S_d\otimes_R R'\longrightarrow e'_dS',
\qquad (e_ds)\otimes r'\longmapsto e'_d(s\otimes r')
\]
is an isomorphism: tensor the direct decomposition \(S=e_dS\oplus(1-e_d)S\) and retain its two projections. Thus the full finite product decomposition commutes with every base change. A component may become zero; it is not reassigned a different dimension.

The radical ideal \(J_d\) of the preceding section is generally not \(e_dS\). Its exact formula is
\[
J_d=\sqrt{e_dS}=e_dS+\sqrt{(0)_S}.
\]
If \(x^m\in e_dS\), then \(((1-e_d)x)^m=0\), and \(x=e_dx+(1-e_d)x\) lies in the last ideal. Conversely its image modulo \(e_dS\) is nilpotent, giving the reverse inclusion. For \(S=k[\epsilon]/(\epsilon^2)\), the empty dimension-one stratum has \(e_1=0\) but \(J_1=(\epsilon)\ne0\). This illustrates why replacing the radical ideal by the idempotent ideal would erase relevant nilpotent data.

Every \(S\)-module has the exact component decomposition
\[
M\longrightarrow\prod_{d=0}^n e_dM,\quad m\longmapsto(e_dm)_d,
\qquad (m_d)_d\longmapsto\sum_d m_d.
\]
The composites are identities by orthogonality and the sum-to-one equation. Every \(S\)-linear map preserves these components, and these decompositions commute with tensor base change by the same split projections. Finally, if \(\operatorname{Spec}S\) is nonempty and connected, exactly one \(e_d\) is nonzero, and all its nonempty fibres are equidimensional of that one dimension. Connectedness of the base is insufficient: over the field \(k\), the flat finitely presented algebra \(k[x]\times k\) has dimensions one and zero on its two components.

## Propagation and reading boundary

The chart criterion uses the actual second alternative of the earlier Cohen–Macaulay flatness lemma, rather than a false finite-local-map assertion. The local fibre criterion and the corrected openness-of-flatness proof are used with their full hypotheses. Group 878 propagates these to the maximal flat Cohen–Macaulay open without a global flatness assumption. Group 879 adds the dimension-preserving universal set and radical-ideal identities. Group 880 gives the canonical component maps, their universal comparisons and the exact nilpotent correction to the radical ideals.

All three consequence groups have zero translation replacement operations. The source product proof was checked directly: its finite range follows either from the generator bound just proved or compactness of the affine spectrum. No new hypothesis is needed to make the product finite.

The query “Cohen Macaulay locus base change” returns two research routing hits and one local-work hit. None is read as mathematical evidence; the local hit is a PDF and was not used. Earlier external-source coverage is unchanged. No claim of novelty, literature exhaustiveness or source mutation accompanies this batch. Broader synthesis remains follow-on work after core completion.
