# Fibre isomorphisms in the substack lemma

Private independent mathematical derivation, 2026-09-23. This note does not edit the source or declare an admitted correction.

## 1. Source identity and conclusion

Primary source: The Stacks Project Authors, Stacks and Categories chapters, authority `a04446e57ec1fbc252a871afcec7752fb2807b14`. The authority `stacks.tex` and the current local `stacks.tex` both have SHA-256 `ca374cb00b1c71acf10e30faef293108d079258211d935fe0d4add1477634ba9`. The relevant lemma is `lemma-substack`, lines 617–645. Its statement contains unqualified isomorphisms in conditions (1) and (3). Read with isomorphisms in the total category, the statement is false; Section 3 gives a complete counterexample.

A sufficient local wording repair is to replace condition (1)'s conclusion by:

> then there is an object \(y'\) of \(\mathcal S'\) over \(p(y)\) and an isomorphism \(y'\to y\) in the fibre category \(\mathcal S_{p(y)}\).

One need not independently strengthen every occurrence in (3). Once repaired condition (1) and fullness hold, an arbitrary total-category isomorphism to an object of \(\mathcal S'\) can be converted to an isomorphism in the appropriate fibre; Section 5 proves the exact conversion. Thus condition (3) can equivalently be written with all isomorphisms in their indicated fibre categories. Writing those fibres explicitly throughout is accurate; saying that each of those extra qualifiers is separately necessary would overstate the result.

The proof's `Isom` at line 639 must address `Mor`: the stack definition at lines 575–578 requires the morphism presheaves to be sheaves. Section 6 proves the full natural comparison for arbitrary choices of pullbacks, including its restriction maps. The two presheaves are canonically isomorphic; they become equal for compatible choices.

## 2. Exact definitions and the convention issue

The following authority blocks were read directly from Git, separately from the modified local Categories chapter:

- `categories.tex`, `definition-fibre-category`, authority lines 6043–6067; current lines 6196–6220. Objects of \(\mathcal S_U\) satisfy the literal equality \(p(x)=U\), and its morphisms satisfy \(p(\phi)=\operatorname{id}_U\).
- `categories.tex`, `definition-cartesian-over-C`, authority lines 6204–6221; current lines 6357–6374. A morphism \(\phi:y\to x\) is strongly cartesian if, for every \(z\in\mathcal S\), the map
  \[
  \operatorname{Mor}_{\mathcal S}(z,y)\longrightarrow
  \operatorname{Mor}_{\mathcal S}(z,x)
  \times_{\operatorname{Mor}_{\mathcal C}(p(z),p(x))}
  \operatorname{Mor}_{\mathcal C}(p(z),p(y)),
  \qquad t\longmapsto(\phi t,p(t))
  \]
  is bijective. The two maps into the fibre-product base are \(p\) and composition with \(p(\phi)\), respectively.
- `categories.tex`, `definition-fibred-category`, authority lines 6360–6369; current lines 6513–6522. For every \(x\) over \(U\) and every \(f:V\to U\), a strongly cartesian arrow to \(x\) lying over exactly \(f\) must exist.
- `stacks.tex`, lines 29–70 and 147–201, defines the morphism presheaf and its restriction maps; lines 280–324 and 428–452 define descent and effectivity; lines 567–583 define a stack.
- `sites.tex`, current lines 679–696, requires singleton isomorphisms to be coverings, composition of coverings, and pullbacks of coverings.

The authority Categories file has SHA-256 `62f7611af4c3feebd041db4728b42c7112004cfbb9fa5ecb643c6f5d90db3f25`; the current local Categories file read for contextual explanations has SHA-256 `05ad27c125bc31801dc1c4644d44684db74ed6d43f2bdc6e01fb9d4b46260688`. The essential definitions above agree in the two versions.

There is no licence in these definitions to replace equality of base objects by isomorphism. Current `categories.tex` lines 7455–7468 explicitly begin with an unrestricted isomorphism \(x'\cong G(x)\), take its possibly nonidentity base isomorphism \(f:U'\to U\), and then construct a new isomorphism over \(\operatorname{id}_{U'}\). This is positive source evidence that the two notions are distinguished, rather than a claim based only on failing to find a convention. The object-level wording in `lemma-substack` supplies no fibre qualifier.

In this note, a **vertical isomorphism over \(U\)** means an isomorphism whose image under \(p\) is \(\operatorname{id}_U\), equivalently an isomorphism of \(\mathcal S_U\).

## 3. Complete counterexample to the literal statement

Let \(\mathcal C\) have two distinct objects \(A\) and \(B\). Its four morphisms are
\[
\operatorname{id}_A:A\to A,\qquad
\operatorname{id}_B:B\to B,\qquad
u:B\to A,\qquad v:A\to B,
\]
with \(uv=\operatorname{id}_A\) and \(vu=\operatorname{id}_B\). There is exactly one morphism between each ordered pair of objects.

Give \(\mathcal C\) the site whose coverings are all singleton families \(\{f:X\to U\}\). Every morphism is an isomorphism. This satisfies the site axioms: the required singleton isomorphisms are present; a composite of singleton coverings is another such covering; and for \(f:X\to U\), \(g:Y\to U\), take
\[
X\times_UY=X,\qquad \pi_0=\operatorname{id}_X,
\qquad \pi_1=g^{-1}f:X\to Y.
\]
The square commutes. For any \(T\), there is exactly one arrow to each object, so the map from \(\operatorname{Mor}(T,X)\) to the set of pairs of arrows \(T\to X,T\to Y\) having equal composites to \(U\) is a bijection of singleton sets. This proves the pullback universal property. The projection \(g^{-1}f\) is an isomorphism, so its singleton is again a covering. Iterated pullbacks give the triple fibre products needed for descent.

Set \(\mathcal S=\mathcal C\) and \(p=\operatorname{id}_{\mathcal C}\). This is a stack:

1. Every morphism is strongly cartesian: every set in the defining comparison is a singleton. For any \(f:V\to U\), the arrow \(f\) itself is the required lift with target the sole object \(U\) of \(\mathcal S_U\).
2. The fibre \(\mathcal S_U\) has the single object \(U\) and the single morphism \(\operatorname{id}_U\). Consequently every morphism presheaf required by the stack definition is the singleton presheaf on \(\mathcal C/U\), which satisfies the sheaf axiom because every matching family and its amalgamation are unique.
3. A covering has one member \(f:X\to U\). A descent datum has the sole object \(X\) in its local fibre and the unique vertical isomorphism on its overlap. Its cocycle condition holds because every relevant Hom set is a singleton. It is precisely the canonical descent datum of \(U\in\mathcal S_U\), for any choice of pullbacks, since every local fibre has only its specified single object and morphism. Thus every descent datum is effective.

Let \(\mathcal S'\) be the full subcategory with sole object \(A\). Its only morphism is \(\operatorname{id}_A\). All three unqualified hypotheses of the printed lemma hold:

- In (1), the source of every strongly cartesian arrow with target \(A\) is either \(A\) or \(B\), and both are isomorphic in \(\mathcal S\) to \(A\in\mathcal S'\).
- Condition (2) holds by construction.
- In (3), every object \(x\) of \(\mathcal S\) is isomorphic in the total category to \(A\), so the conclusion holds for every cover and every \(x\), regardless of the premise. In fact the premise holds as well.

Nevertheless \(\mathcal S'\to\mathcal C\) is not fibred. The arrow \(u:B\to A\) and the object \(A\in\mathcal S'_A\) would require an object of \(\mathcal S'_B\), but that fibre is empty. The only morphism of \(\mathcal S'\) maps to \(\operatorname{id}_A\), never to \(u\). Thus it cannot be a stack.

The failure has an exact categorical description. The inclusion \(I:\mathcal S'\hookrightarrow\mathcal S\) is fully faithful and essentially surjective as a functor of ordinary categories. A quasi-inverse \(Q\) sends both \(A\) and \(B\) to \(A\) and every arrow to \(\operatorname{id}_A\). The natural isomorphism \(IQ\to\operatorname{id}_{\mathcal S}\) has components \(\operatorname{id}_A\) at \(A\) and \(v:A\to B\) at \(B\). The latter lies over \(v\), not over \(\operatorname{id}_B\). Furthermore \(p'Q(B)=A\ne B=p(B)\), so \(Q\) is not a functor over \(\mathcal C\). The ordinary categorical equivalence therefore does not supply the required equivalence over the fixed base.

Define the vertical essential image fibre by fibre: \(E_U\) consists of those \(z\in\mathcal S_U\) vertically isomorphic to an object of \(\mathcal S'_U\). In this example \(E_A=\{A\}\) and \(E_B=\varnothing\), whereas the unrestricted essential image is all of \(\mathcal S\). The missing pullback is exactly the failure of this vertical essential image to be preserved by \(u^*\), since \(u^*A=B\). This identifies the defect without dismissing the ordinary equivalence.

## 4. Pullback lifts after the repair

Assume now that \(p:\mathcal S\to\mathcal C\) is the original stack, that \(\mathcal S'\) is full, and that condition (1) is repaired as in Section 1. Write \(p'=p|_{\mathcal S'}\).

Fix \(x\in\mathcal S'\) over \(U\) and \(f:V\to U\). Since \(\mathcal S\) is fibred, choose an ambient strongly cartesian arrow
\[
c:y\to x,\qquad p(c)=f,\qquad p(y)=V.
\]
The repaired hypothesis supplies \(y'\in\mathcal S'_V\) and an isomorphism \(e:y'\to y\) with \(p(e)=\operatorname{id}_V\). Then
\[
c'=ce:y'\to x,\qquad p(c')=f
\]
is an arrow of \(\mathcal S'\) by fullness. It is ambient strongly cartesian: for any \(z\in\mathcal S\), \(a:z\to x\), and \(h:p(z)\to V\) with \(p(a)=fh\), cartesianness of \(c\) gives the unique \(t:z\to y\) with \(ct=a\), \(p(t)=h\). The unique lift through \(c'\) is \(e^{-1}t\). For \(z\in\mathcal S'\), fullness puts that lift in \(\mathcal S'\). Hence \(c'\) is strongly cartesian for \(p'\), and \(p'\) is fibred.

Moreover the inclusion preserves every strongly cartesian arrow, not only the chosen lifts. Let \(d:z'\to x\) be strongly cartesian in \(\mathcal S'\), lying over \(f:V\to U\). Choose \(c':y'\to x\) as above over the same \(f\). Applying the two cartesian universal properties inside \(\mathcal S'\), there are unique vertical maps
\[
a:y'\to z',\qquad b:z'\to y',\qquad da=c',\qquad c'b=d.
\]
Then \(d(ab)=d\) and \(c'(ba)=c'\). Uniqueness in the respective cartesian properties gives \(ab=\operatorname{id}_{z'}\) and \(ba=\operatorname{id}_{y'}\). Thus \(b\) is a vertical isomorphism and \(d=c'b\). Applying the explicit factorization argument of the preceding paragraph proves that \(d\) is ambient strongly cartesian. Conversely, every ambient strongly cartesian arrow between objects of \(\mathcal S'\) remains strongly cartesian there by fullness. This proves the exact relation between the two kinds of lift and shows that the inclusion is a 1-morphism of fibred categories.

## 5. Converting a total-category isomorphism to a fibre isomorphism

Continue under the repaired (1) and fullness. Let \(z\in\mathcal S_U\), let \(t\in\mathcal S'_W\), and let \(a:z\to t\) be an arbitrary isomorphism of \(\mathcal S\). Its base map \(h=p(a):U\to W\) is an isomorphism. Section 4 gives a lift
\[
c:t_U\to t,\qquad t_U\in\mathcal S'_U,\qquad p(c)=h,
\]
that is strongly cartesian in both categories. This arrow is invertible. Indeed, apply its ambient cartesian property to \(\operatorname{id}_t\) and \(h^{-1}\) to obtain \(d:t\to t_U\) with \(cd=\operatorname{id}_t\) and \(p(d)=h^{-1}\); uniqueness applied to \(c\) and \(\operatorname{id}_U\) gives \(dc=\operatorname{id}_{t_U}\).

Consequently
\[
e=c^{-1}a:z\longrightarrow t_U,
\qquad p(e)=h^{-1}h=\operatorname{id}_U
\]
is the required vertical isomorphism. Conversely any vertical isomorphism is a total-category isomorphism. This proves equality between the total essential image and the union of the vertical essential images after the pullback repair, with the actual comparison map displayed.

It follows that original condition (3) is equivalent, under these hypotheses, to the following fibre-qualified condition:

> For every covering \(\{f_i:U_i\to U\}_{i\in I}\) and \(x\in\mathcal S_U\), if every \(f_i^*x\) is isomorphic in \(\mathcal S_{U_i}\) to an object of \(\mathcal S'_{U_i}\), then \(x\) is isomorphic in \(\mathcal S_U\) to an object of \(\mathcal S'_U\).

For one implication, vertical local isomorphisms satisfy the original premise; apply original (3) and then the conversion just proved. For the reverse implication, convert each unrestricted local isomorphism to a vertical one, apply the displayed condition, and forget the vertical qualifier in its conclusion. These implications also cover an empty covering: the local premise is then vacuous and the same conclusion argument applies.

## 6. The exact natural comparison of morphism presheaves

Let \(x,y\in\mathcal S'_U\). Choose arbitrary pullbacks in \(\mathcal S\) and in \(\mathcal S'\), denoted respectively by
\[
f^*x\xrightarrow{c_{f,x}}x,
\qquad f^{*'}x\xrightarrow{c'_{f,x}}x
\]
for \(f:V\to U\), and likewise for \(y\). All four arrows are ambient strongly cartesian by Section 4. Their unique vertical comparison isomorphisms are
\[
\kappa_{f,x}:f^*x\longrightarrow f^{*'}x,
\qquad c'_{f,x}\kappa_{f,x}=c_{f,x},
\qquad p(\kappa_{f,x})=\operatorname{id}_V,
\]
and the corresponding \(\kappa_{f,y}\). Existence is the cartesian property of \(c'\); reversing its role with \(c\) and using uniqueness gives the inverse.

Define
\[
\Theta_f:\operatorname{Mor}_{\mathcal S'_V}(f^{*'}x,f^{*'}y)
\longrightarrow\operatorname{Mor}_{\mathcal S_V}(f^*x,f^*y),
\qquad a\longmapsto\kappa_{f,y}^{-1}a\kappa_{f,x}.
\tag{M1}
\]
Its inverse takes \(b\) to \(\kappa_{f,y}b\kappa_{f,x}^{-1}\). This is a vertical ambient arrow between objects of \(\mathcal S'\), so fullness makes it an arrow of \(\mathcal S'_V\). Thus \(\Theta_f\) is bijective for every \(f\).

To prove naturality, take a morphism \(g:(V',fg)\to(V,f)\) in \(\mathcal C/U\). Write
\[
\rho_{g,f,x}:(fg)^*x\to f^*x,
\quad c_{f,x}\rho_{g,f,x}=c_{fg,x},
\quad p(\rho_{g,f,x})=g,
\]
and define \(\rho'_{g,f,x}\) for the other choices. Existence and uniqueness follow from cartesianness of \(c_{f,x}\). The arrow \(\rho_{g,f,x}\) is strongly cartesian: if \(t:z\to f^*x\) lies over \(gh\), cartesianness of \(c_{fg,x}\) gives a unique \(s:z\to(fg)^*x\) with \(c_{fg,x}s=c_{f,x}t\) and \(p(s)=h\); cartesianness of \(c_{f,x}\) then gives \(\rho_{g,f,x}s=t\). The same uniqueness proves uniqueness of \(s\). This argument also applies to \(\rho'\).

The comparison identity is
\[
\kappa_{f,x}\rho_{g,f,x}
=\rho'_{g,f,x}\kappa_{fg,x}.
\tag{M2}
\]
Both sides lie over \(g\) and have the same composite \(c_{fg,x}\) with \(c'_{f,x}\), so its cartesian property proves the identity. The corresponding identity holds for \(y\).

The restriction of \(a\) is the unique vertical arrow \(a|_g\) satisfying
\[
\rho'_{g,f,y}(a|_g)=a\rho'_{g,f,x}.
\tag{M3}
\]
This description retains the source's composition comparisons: if \(\alpha'_{g,f,x}:(fg)^{*'}x\to g^{*'}f^{*'}x\) is the canonical comparison, then
\[
\rho'_{g,f,x}=c'_{g,f^{*'}x}\alpha'_{g,f,x},
\qquad
a|_g=(\alpha'_{g,f,y})^{-1}g^{*'}(a)\alpha'_{g,f,x}.
\tag{M4}
\]
The square for \(g^{*'}(a)\) verifies (M3), and uniqueness proves equality with the restriction in `stacks.tex` lines 65–70.

Using (M2) and (M3), with every comparison map retained, gives
\[
\begin{aligned}
\rho_{g,f,y}\Theta_{fg}(a|_g)
&=\rho_{g,f,y}\kappa_{fg,y}^{-1}(a|_g)\kappa_{fg,x}\\
&=\kappa_{f,y}^{-1}\rho'_{g,f,y}(a|_g)\kappa_{fg,x}\\
&=\kappa_{f,y}^{-1}a\rho'_{g,f,x}\kappa_{fg,x}\\
&=\kappa_{f,y}^{-1}a\kappa_{f,x}\rho_{g,f,x}\\
&=\Theta_f(a)\rho_{g,f,x}.
\end{aligned}
\]
By the uniqueness in the cartesian property of \(\rho_{g,f,y}\), this is precisely
\[
\Theta_{fg}(a|_g)=\Theta_f(a)|_g.
\tag{M5}
\]
Thus (M1) is a natural isomorphism
\[
\mathit{Mor}_{\mathcal S'}(x,y)
\xrightarrow{\ \sim\ }
\mathit{Mor}_{\mathcal S}(x,y)
\quad\text{on }\mathcal C/U.
\tag{M6}
\]
The target is a sheaf because \(\mathcal S\) is a stack. To spell out transfer of the sheaf property, a matching family in the source maps by (M6) to a matching family in the target, has a unique target amalgamation, and its inverse image under \(\Theta_f\) is a source amalgamation by (M5); uniqueness follows from injectivity of \(\Theta_f\). Hence the source is a sheaf.

Conjugation in (M1) also restricts to isomorphisms, so it proves the corresponding `Isom` comparison. That weaker statement alone does not address all morphisms required for a stack in categories. `stacks.tex` lines 166–168 equates `Isom` and `Mor` only under the additional hypothesis of being fibred in groupoids, which `lemma-substack` does not impose.

## 7. Complete descent proof

Fix any choice of pullbacks in \(\mathcal S'\). Section 4 proves that these very arrows are ambient strongly cartesian. For this proof choose ambient pullbacks agreeing with them on objects of \(\mathcal S'\), and retain arbitrary pullbacks for other objects. This selects lifts without identifying unequal objects or dropping any comparison transformation. The morphism pullbacks and all canonical composition comparisons for objects of \(\mathcal S'\) agree in the two categories, because their characterizing diagrams and uniqueness properties agree by fullness and Section 4.

Choice independence here is explicit: between any two ambient choices the maps \(\kappa\) above identify the pullbacks. For a pair of base arrows with a common composite, (M2), applied to each route, identifies their canonical comparison maps. A descent isomorphism \(d_{ij}\) is transported to \(\kappa_{\pi_1,X_j}^{-1}d_{ij}\kappa_{\pi_0,X_i}\). These formulas are invertible. Substitution into the cocycle equation cancels the middle \(\kappa\) with its inverse and leaves the original cocycle equation, with (M2) accounting for iterated pullbacks. The same formula for morphisms preserves the descent compatibility square. It carries canonical descent data to isomorphic canonical descent data by \(\kappa_{f_i,X}\). Thus effectivity for the original ambient choice is equivalent to effectivity for the choice made in this paragraph.

Let \(\{f_i:U_i\to U\}_{i\in I}\) be any covering and let
\[
(X_i,d_{ij}),\qquad
X_i\in\mathcal S'_{U_i},\qquad
d_{ij}:\pi_0^*X_i\xrightarrow{\sim}\pi_1^*X_j
\]
be a descent datum in \(\mathcal S'\). Here the projections from \(U_i\times_UU_j\) are \(\pi_0\) and \(\pi_1\), preserving the source's indexing. Its maps are vertical. The same objects and maps form a descent datum in \(\mathcal S\), with exactly the same cocycle equation and comparison transformations.

Effectivity in \(\mathcal S\) gives \(X\in\mathcal S_U\) and vertical isomorphisms
\[
\eta_i:f_i^*X\xrightarrow{\sim}X_i
\]
forming an isomorphism of descent data. Write \(q_{ij}=f_i\pi_0=f_j\pi_1\). For any \(Z\in\mathcal S_U\), put
\[
A_{0,Z}=\alpha_{\pi_0,f_i,Z}:q_{ij}^*Z\xrightarrow{\sim}\pi_0^*f_i^*Z,
\qquad
A_{1,Z}=\alpha_{\pi_1,f_j,Z}:q_{ij}^*Z\xrightarrow{\sim}\pi_1^*f_j^*Z.
\]
Its canonical descent transition is
\[
\operatorname{can}_{ij,Z}=A_{1,Z}A_{0,Z}^{-1}:
\pi_0^*f_i^*Z\xrightarrow{\sim}\pi_1^*f_j^*Z.
\tag{D1}
\]
The compatibility of \(\eta\) reads
\[
d_{ij}\,\pi_0^*(\eta_i)
=\pi_1^*(\eta_j)\operatorname{can}_{ij,X}.
\tag{D2}
\]

Each \(f_i^*X\) is vertically isomorphic to an object of \(\mathcal S'_{U_i}\), namely \(X_i\). By condition (3) and Section 5 there exist \(X'\in\mathcal S'_U\) and a vertical isomorphism \(e:X'\to X\). Define
\[
\eta'_i=\eta_i f_i^*(e):f_i^*X'\xrightarrow{\sim}X_i.
\tag{D3}
\]
Both objects are in \(\mathcal S'\); fullness puts \(\eta'_i\) and its inverse in \(\mathcal S'_{U_i}\). Naturality of the two canonical composition comparisons gives the exact identity
\[
\operatorname{can}_{ij,X}\,\pi_0^*f_i^*(e)
=\pi_1^*f_j^*(e)\operatorname{can}_{ij,X'}.
\tag{D4}
\]
Indeed, \(\pi_0^*f_i^*(e)A_{0,X'}=A_{0,X}q_{ij}^*(e)\) and \(\pi_1^*f_j^*(e)A_{1,X'}=A_{1,X}q_{ij}^*(e)\); substituting these two equations into (D1) proves (D4). No associativity comparison is omitted from (D1) or (D4).

Now (D2)–(D4) yield
\[
\begin{aligned}
d_{ij}\,\pi_0^*(\eta'_i)
&=d_{ij}\,\pi_0^*(\eta_i)\,\pi_0^*f_i^*(e)\\
&=\pi_1^*(\eta_j)\operatorname{can}_{ij,X}\,\pi_0^*f_i^*(e)\\
&=\pi_1^*(\eta_j)\,\pi_1^*f_j^*(e)\operatorname{can}_{ij,X'}\\
&=\pi_1^*(\eta'_j)\operatorname{can}_{ij,X'}.
\end{aligned}
\]
Thus \((\eta'_i)\) is an isomorphism from the canonical descent datum of \(X'\) to the original datum, within \(\mathcal S'\). The datum is effective. For an empty covering the same argument begins with the ambient descent object \(X\), applies condition (3) with its vacuous local premise, and obtains \(X'\); the compatibility equations are vacuous. No covering case is excluded.

Section 4 proves the fibred axiom, Section 6 the morphism-sheaf axiom, and this section the effectivity axiom. These are exactly the three clauses of `definition-stack`, so the repaired lemma is proved.

## 8. Scope of the proposed correction

This establishes an independently detected defect in the literal statement, adjacent to the received `Isom`/`Mor` report. It does not establish that the received report itself requested the fibre qualifier, nor that the source authors intended unrestricted isomorphisms. The counterexample shows why the wording needs a fibre-level interpretation or repair; the construction in Sections 4–7 proves that interpretation.

A concise repair can qualify condition (1), replace `Isom` by `Mor`, and refer in the proof to canonical isomorphisms of the presheaves. A more explicit wording can also qualify both local and global isomorphisms in (3), using their equivalent formulation from Section 5. Either mathematical version is justified by the complete proofs above. Only this private derivation note was written; no source mutation, candidate allocation, or publication was performed.
