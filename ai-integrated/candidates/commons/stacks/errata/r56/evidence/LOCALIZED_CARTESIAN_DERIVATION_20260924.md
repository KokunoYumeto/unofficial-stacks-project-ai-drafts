# Cartesian morphisms after localization in the construction of inverse image

Independent mathematical derivation, 2026-09-24. This note concerns the construction in `stacks.tex` at authority commit `a04446e57ec1fbc252a871afcec7752fb2807b14`. It does not edit the repository or certify the surrounding received reports.

## Source identity and reading coverage

The original Stacks Project source files at the stated commit were read locally and compared, byte for byte, with the corresponding anonymous `raw.githubusercontent.com/stacks/stacks-project/` downloads. All three comparisons agreed:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `stacks.tex` | 137049 | `ca374cb00b1c71acf10e30faef293108d079258211d935fe0d4add1477634ba9` |
| `categories.tex` | 350957 | `62f7611af4c3feebd041db4728b42c7112004cfbb9fa5ecb643c6f5d90db3f25` |
| `sites.tex` | 424197 | `07ae4690c2d8eb6873837d3d14a37f07408bb14f9e0be6077ed570c220b1845d` |

Actual mathematical reading: `stacks.tex` 2661–2818 and 2824–3330, including the definitions of both base-change constructions, the right calculus of fractions, the claimed characterization, and its use in adjointness; `sites.tex` 2811–2900, including `proposition-get-morphism`; and the following original-source definitions and lemmas in `categories.tex`:

- [Definition of a multiplicative system, line 3906](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L3906).
- [Right fractions and their equivalence, preceding line 4582](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L4531).
- [Common denominators, line 4619](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L4619), and [equality after a right refinement, line 4642](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L4642).
- [Universal property of right localization, line 4693](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L4693).
- [Composition and invertibility of strongly cartesian morphisms, line 6242](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L6242).

The source authorship is that of the Stacks Project Authors. The counterexample and replacement proofs below are the present independent derivation. The source's omitted converse is false under its stated hypotheses. The fibred-category and adjointness conclusions can both be proved without that converse.

## 1. Construction with all bases retained

Let \(p:\mathcal S\to\mathcal C\) be fibred. Assume that \(\mathcal C\) has nonempty finite limits and that \(u:\mathcal C\to\mathcal D\) preserves these limits. Write \(E=u_{pp}\mathcal S\). Its objects are

\[
X=(U,\phi:V\to u(U),x),\qquad p(x)=U.
\]

A morphism \(A:X_1\to X_2\) is a triple

\[
A=(a,b,\alpha),\quad a:U_1\to U_2,\quad b:V_1\to V_2,
\quad \alpha:x_1\to x_2,
\]

with \(p(\alpha)=a\) and \(u(a)\phi_1=\phi_2b\). Composition is componentwise. The functor \(E\to\mathcal D\) sends \(X\) to \(V\) and \(A\) to \(b\). Let

\[
R=\{(a,\mathrm{id}_V,\alpha):\alpha\text{ is strongly }p\text{-cartesian}\}.
\]

Write \(L=R^{-1}E\), with localization functor \(Q:E\to L\), and \(\ell:L\to\mathcal D\) for the induced base functor. An arrow is a right fraction

\[
Q(A)Q(r)^{-1}:X\longrightarrow Y,
\qquad A:Z\to Y,\quad r:Z\to X\text{ in }R.
\]

All uses of preservation of a limit below mean its canonical comparison isomorphism. No literal equality between an arbitrarily chosen limit object and its image under \(u\) is required.

We use three elementary facts about strongly cartesian arrows. Composites of such arrows are strongly cartesian; isomorphisms are strongly cartesian; and a strongly cartesian arrow over an identity is an isomorphism. For the last assertion, apply its universal property to the identity of its target to obtain a right inverse, and apply uniqueness to obtain the left-inverse identity. We also need cancellation: if \(g\) and \(gf\) are strongly cartesian, then \(f\) is strongly cartesian. Indeed, for \(h:z\to\operatorname{cod}(f)\) over \(p(f)d\), the universal property of \(gf\) gives a unique \(k\) over \(d\) with \(gfk=gh\); the universal property of \(g\) then gives \(fk=h\). Uniqueness follows from that of \(gf\).

For completeness, two cartesian lifts \(c:x\to y\) and \(c':x'\to y\) of the same base arrow have a unique vertical isomorphism \(j:x\to x'\) with \(c'j=c\). The two universal properties supply \(j\) and its inverse; uniqueness supplies both inverse identities. This controls every change of a chosen cartesian lift below.

## 2. The localization prerequisites with typed arrows

The right multiplicative-system assertion used here has a direct proof.

RMS1 follows from identities and composition of strongly cartesian arrows. For RMS2 take

\[
(a,b,\alpha):X=(U,\phi:V\to u(U),x)\longrightarrow
Y=(T,\theta:W\to u(T),y)
\]

and

\[
(c,\mathrm{id}_W,\gamma):Y'=(T',\theta':W\to u(T'),y')\longrightarrow Y
\]

in \(R\). Form \(P=U\times_TT'\), with projections \(d:P\to U\) and \(a':P\to T'\). The relation \(u(a)\phi=u(c)\theta'b\) gives a unique \(\psi:V\to u(P)\) satisfying

\[
u(d)\psi=\phi,\qquad u(a')\psi=\theta'b.
\]

Choose cartesian \(\delta:z\to x\) over \(d\). Since \(ca'=ad\), cartesianness of \(\gamma\) gives a unique \(\epsilon:z\to y'\) over \(a'\) such that \(\gamma\epsilon=\alpha\delta\). Then

\[
t=(d,\mathrm{id}_V,\delta):(P,\psi,z)\to X\quad\text{belongs to }R,
\]

\[
h=(a',b,\epsilon):(P,\psi,z)\to Y',\qquad (a,b,\alpha)t=(c,\mathrm{id}_W,\gamma)h.
\]

For RMS3 suppose \((a,b,\alpha),(a',b',\alpha'):X\to Y\) are equalized by \((c,\mathrm{id}_W,\gamma):Y\to Y'\) in \(R\). Thus \(b=b'\), \(ca=ca'\), and \(\gamma\alpha=\gamma\alpha'\). Let \(e:P\to U\) equalize \(a,a'\). Since

\[
u(a)\phi=\theta b=u(a')\phi,
\]

preservation of the equalizer gives \(\psi:V\to u(P)\) with \(u(e)\psi=\phi\). Choose cartesian \(\delta:z\to x\) over \(e\). The arrows \(\alpha\delta\) and \(\alpha'\delta\) have the same base \(ae=a'e\) and become equal after \(\gamma\), so they are equal by the cartesian universal property of \(\gamma\). Therefore \((e,\mathrm{id}_V,\delta)\in R\) equalizes the original arrows. This proves RMS3.

Consequently the stated right-fraction construction exists. Its equality criterion gives, in particular:

\[
Q(f)=Q(g),\quad f,g:X\to Y
\quad\Longleftrightarrow\quad
\exists r:Z\to X\text{ in }R\text{ with }fr=gr.
\tag{2.1}
\]

Its finite-common-denominator property will also be used. Both facts are the original right-localization lemmas linked above, and require only a right multiplicative system, not a two-sided one.

## 3. Counterexample under all the relevant hypotheses

Let \(\mathcal C\) be the ordered category \(0<1\), with its unique nonidentity arrow \(c:0\to1\). Let \(\mathcal D\) be the terminal category with object \(*\), and let \(u\) be its unique incoming functor.

The category \(\mathcal C\) has every finite limit. Its terminal object is \(1\), and the limit of a nonempty finite diagram is \(0\) if the diagram contains \(0\), and \(1\) otherwise. The unique functor to \(\mathcal D\) preserves every such limit, including the terminal object.

Define a strict contravariant diagram of categories by

\[
F(1)=[s\xrightarrow{v}t],\qquad F(0)=\{z\},
\qquad c^*:F(1)\to F(0),\quad s,t\mapsto z,\quad v\mapsto\mathrm{id}_z.
\]

Its fibred category \(p:\mathcal S\to\mathcal C\) has objects \(z,s,t\), with \(p(z)=0\), \(p(s)=p(t)=1\), and exactly these nonidentity arrows:

\[
r_s:z\longrightarrow s,\qquad v:s\longrightarrow t,
\qquad r_t:z\longrightarrow t,
\quad r_t=v r_s.
\]

Here \(p(r_s)=p(r_t)=c\), and \(p(v)=\mathrm{id}_1\). The arrows \(r_s,r_t\) are cartesian: to test either of their universal properties, an arrow into its target with base factoring through \(c\) must have source over \(0\), and that source can only be \(z\); its required factorization is unique. Identities provide all remaining cartesian lifts, so \(p\) is fibred.

The arrow \(v\) is not cartesian. A cartesian arrow over \(\mathrm{id}_1\) would be invertible, and no arrow \(t\to s\) exists. Equivalently, the identity of \(t\), with base factorization \(\mathrm{id}_1\), has no factorization through \(v\).

For this \(u\), the category \(E\) is isomorphic to \(\mathcal S\): the \(\mathcal D\)-object and its structural map carry unique choices. Both \(r_s,r_t\) lie in \(R\), so

\[
Q(v)=Q(r_t)Q(r_s)^{-1}
\]

is an isomorphism in \(L\). Since \(L\to\mathcal D\) has terminal base, its strongly cartesian arrows are exactly its isomorphisms. Thus \(Q(v)\) is strongly cartesian and \(v\) is not. This directly contradicts the asserted converse for the triple \((\mathrm{id}_1,\mathrm{id}_*,v)\).

The example also meets the later site hypotheses. Give each base category the topology in which only maximal sieves cover, equivalently the topology generated by singleton identity coverings. All presheaves are sheaves, so \(u\) is continuous. It preserves the terminal object and fibre products, as required by [Sites, `proposition-get-morphism`](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/sites.tex#L2825). The fibred category \(\mathcal S\) is a stack for the identity-covering site: a descent datum for the singleton identity covering is an object with its identity gluing map, since an invertible idempotent is the identity, and all its morphisms are exactly the fibre morphisms. More explicitly, in either of these ordered base categories, any family generating a maximal sieve contains an identity arrow: its generated sieve contains the identity, and an arrow through which an identity factors in an ordered category is itself an identity. For a descent datum on such a family, choose one identity component \(x\) over the covered object. The gluing isomorphism between that component and each other component identifies the latter with the corresponding pullback of \(x\). The cocycle equation identifies each remaining gluing map with the map induced by these identifications. A compatible morphism of descent data is likewise determined uniquely by its identity component, and every morphism of that component supplies the compatible pullback morphisms. Thus descent is effective and fully faithful for every covering family. Neither continuity nor the stack condition repairs the converse.

The exact lost information is the noninvertibility of \(v\), which the permitted pullback \(c^*\) sends to an identity. Its cartesian refinement is already visible:

\[
v r_s=r_t,
\]

where both \(r_s\) and \(r_t\) are cartesian.

## 4. Canonical cartesian lifts in the localization

For \(Y=(U,\phi:V\to u(U),y)\) and \(b:V'\to V\), set

\[
Y_b=(U,\phi b:V'\to u(U),y),\qquad
k_b=(\mathrm{id}_U,b,\mathrm{id}_y):Y_b\to Y.
\tag{4.1}
\]

**Claim.** \(Q(k_b)\) is strongly \(\ell\)-cartesian.

Let \(Z=(T,\psi:W\to u(T),z)\), let \(d:W\to V'\), and let \(h:Z\to Y\) in \(L\) satisfy \(\ell(h)=bd\). Choose a right-fraction representative

\[
h=Q(h_0)Q(r)^{-1},\quad r:Z'\to Z\text{ in }R,
\quad h_0=(a,bd,\alpha):Z'\to Y.
\]

Since \(r\) has identity \(\mathcal D\)-component, \(Z'\) also lies over \(W\). The same \(a,\alpha\), with base arrow \(d\), define

\[
h_1=(a,d,\alpha):Z'\to Y_b,
\]

because the required relation is exactly the relation for \(h_0\). Then \(k_bh_1=h_0\), and \(Q(h_1)Q(r)^{-1}\) is a lift of \(h\) over \(d\).

To prove uniqueness, write two proposed lifts with a common denominator, as \(Q(g_1)Q(s)^{-1}\) and \(Q(g_2)Q(s)^{-1}\). Both \(g_i\) have \(\mathcal D\)-component \(d\). Equality after composition with \(Q(k_b)\) implies, by the right-localization equality criterion, that for some \(t\in R\),

\[
k_bg_1t=k_bg_2t
\]

in \(E\). Composition with \(k_b\) leaves the \(\mathcal C\)-component and the \(\mathcal S\)-component unchanged. The \(\mathcal D\)-components of \(g_1t,g_2t\) are already both \(d\). Therefore the last equality implies \(g_1t=g_2t\), hence equality of the two proposed lifts in \(L\). This proves the claim and proves directly that \(L\to\mathcal D\) is fibred.

Every \(f:X\to Y\) over \(b\) therefore has a unique factorization

\[
f=Q(k_b)i_f,
\qquad i_f:X\to Y_b\text{ over }\mathrm{id}_{V'}.
\tag{4.2}
\]

Moreover,

\[
f\text{ is strongly cartesian}\quad\Longleftrightarrow\quad i_f\text{ is an isomorphism}.
\tag{4.3}
\]

For the nontrivial direction, if \(f\) is cartesian, its universal property supplies \(j:Y_b\to X\) over the identity with \(fj=Q(k_b)\). Then \(i_fj=\mathrm{id}_{Y_b}\) follows by cancellation through \(Q(k_b)\), and \(ji_f=\mathrm{id}_X\) follows by cancellation through \(f\). The converse follows by composition with an isomorphism.

This also gives the valid implication in the original claim without its longer lifting argument. If \(A=(a,b,\alpha):X\to Y\) has cartesian \(\alpha\), then

\[
A=k_b(a,\mathrm{id}_{V'},\alpha),
\]

and the second factor lies in \(R\). Hence \(Q(A)\) is cartesian.

## 5. Eventual detection of vertical isomorphisms

Fix \(U\in\mathcal C\), \(\phi:V\to u(U)\), and a vertical morphism \(\delta:x\to y\) in \(\mathcal S_U\). Let

\[
X=(U,\phi,x),\quad Y=(U,\phi,y),\quad D_\delta=(\mathrm{id}_U,\mathrm{id}_V,\delta):X\to Y.
\]

Call a pair \((c:W\to U,\psi:V\to u(W))\) admissible for \((U,\phi)\) when \(u(c)\psi=\phi\). Choose cartesian lifts

\[
\gamma_x:x_W\to x,\quad\gamma_y:y_W\to y
\]

over \(c\), and define the vertical morphism \(\delta_W:x_W\to y_W\) by

\[
\gamma_y\delta_W=\delta\gamma_x.
\tag{5.1}
\]

Then

\[
Q(D_\delta)\text{ is invertible}
\quad\Longleftrightarrow\quad
\delta_W\text{ is invertible for some admissible }(c,\psi).
\tag{5.2}
\]

The choice of the two lifts does not change invertibility: the unique comparison isomorphisms for the two cartesian lifts on each side intertwine the corresponding versions of \(\delta_W\), by (5.1) and cartesian uniqueness.

**Proof of the reverse implication.** The triples formed from \(\gamma_x,\gamma_y\) belong to \(R\). Equation (5.1) therefore expresses \(Q(D_\delta)\) as the product of their images and the image of the invertible vertical morphism \(\delta_W\), with the source comparison inverted. All three factors are invertible.

**Proof of the forward implication.** Write an inverse as

\[
Q(e)Q(r)^{-1}:Y\to X,
\]

where

\[
r=(c,\mathrm{id}_V,\gamma):(T,\theta,z)\to Y\text{ lies in }R,
\quad
e=(a,\mathrm{id}_V,\epsilon):(T,\theta,z)\to X.
\]

Here \(a,c:T\to U\), and \(u(a)\theta=\phi=u(c)\theta\). Form the equalizer \(h:T_1\to T\) of \(a,c\). Preservation of the equalizer supplies \(\theta_1:V\to u(T_1)\) with \(u(h)\theta_1=\theta\). Choose cartesian \(\zeta:z_1\to z\) over \(h\). Right-refining both numerator and denominator by \((h,\mathrm{id}_V,\zeta)\in R\) leaves the represented inverse unchanged. Put

\[
d=ah=ch:T_1\to U,\qquad
\tau_y=\gamma\zeta:z_1\to y.
\]

The arrow \(\tau_y\) is cartesian over \(d\). Put \(y_1=z_1\), and choose cartesian \(\tau_x:x_1\to x\) over the same \(d\). There are unique vertical morphisms

\[
\eta:y_1\to x_1,\qquad \delta_1:x_1\to y_1
\]

satisfying

\[
\tau_x\eta=\epsilon\zeta,\qquad
\tau_y\delta_1=\delta\tau_x.
\tag{5.3}
\]

Regard all objects and arrows at this stage as triples with structural map \(\theta_1\). In \(L\), the represented inverse equals

\[
Q(\tau_x)Q(\eta)Q(\tau_y)^{-1}.
\]

Conjugating the two inverse identities by \(Q(\tau_x),Q(\tau_y)\), which are invertible, gives

\[
Q(\eta\delta_1)=\mathrm{id}_{(T_1,\theta_1,x_1)},\qquad
Q(\delta_1\eta)=\mathrm{id}_{(T_1,\theta_1,y_1)}.
\tag{5.4}
\]

By (2.1), there exist two elements of \(R\), with respective \(\mathcal C\)-maps \(c_x:T_x\to T_1\), \(c_y:T_y\to T_1\), structural maps \(\theta_x,\theta_y\), and cartesian \(\mathcal S\)-maps \(\rho_x:z_x\to x_1\), \(\rho_y:z_y\to y_1\), such that

\[
(\eta\delta_1)\rho_x=\rho_x,\qquad
(\delta_1\eta)\rho_y=\rho_y.
\tag{5.5}
\]

The base relations are \(u(c_x)\theta_x=\theta_1=u(c_y)\theta_y\). Form

\[
T_2=T_x\times_{T_1}T_y,
\quad e_x:T_2\to T_x,\quad e_y:T_2\to T_y,
\quad k=c_xe_x=c_ye_y:T_2\to T_1.
\]

Preservation of this fibre product supplies \(\theta_2:V\to u(T_2)\) satisfying \(u(e_x)\theta_2=\theta_x\), \(u(e_y)\theta_2=\theta_y\). In particular \(u(k)\theta_2=\theta_1\), so \((dk,\theta_2)\) is admissible for the original \((U,\phi)\).

Choose cartesian \(\kappa_x:x_2\to x_1\), \(\kappa_y:y_2\to y_1\) over \(k\), and define unique vertical arrows \(\delta_2:x_2\to y_2\), \(\eta_2:y_2\to x_2\) by

\[
\kappa_y\delta_2=\delta_1\kappa_x,
\qquad \kappa_x\eta_2=\eta\kappa_y.
\tag{5.6}
\]

Because \(k=c_xe_x\), cartesianness of \(\rho_x\) factors \(\kappa_x\) through \(\rho_x\). Thus (5.5) gives \(\eta\delta_1\kappa_x=\kappa_x\). Similarly \(\delta_1\eta\kappa_y=\kappa_y\). Hence

\[
\kappa_x\eta_2\delta_2
=\eta\kappa_y\delta_2
=\eta\delta_1\kappa_x
=\kappa_x,
\]

\[
\kappa_y\delta_2\eta_2
=\delta_1\kappa_x\eta_2
=\delta_1\eta\kappa_y
=\kappa_y.
\]

Cartesian uniqueness for \(\kappa_x,\kappa_y\), with fixed identity base maps, proves

\[
\eta_2\delta_2=\mathrm{id}_{x_2},\qquad
\delta_2\eta_2=\mathrm{id}_{y_2}.
\]

Finally, the composites \(\tau_x\kappa_x,\tau_y\kappa_y\) are cartesian over \(dk\), and (5.3), (5.6) give

\[
(\tau_y\kappa_y)\delta_2=\delta(\tau_x\kappa_x).
\]

Thus \(\delta_2\) is exactly a pullback of the original \(\delta\) along the admissible \(dk\), and is invertible. This completes the proof of (5.2).

## 6. Correct characterization, including refinement of any chosen roof

Let \(A=(a,b,\alpha):X_1\to X_2\) be as in Section 1. Then the following three conditions are equivalent:

1. \(Q(A)\) is strongly \(\ell\)-cartesian.
2. There is an element \(r=(c,\mathrm{id}_{V_1},\gamma):Z\to X_1\) of \(R\) such that \(\alpha\gamma\) is strongly \(p\)-cartesian.
3. Choose a cartesian lift \(\tau:a^*x_2\to x_2\) over \(a\), and factor \(\alpha=\tau\delta\) with \(\delta:x_1\to a^*x_2\) vertical. Then \(\delta\) becomes invertible after some admissible pullback for \((U_1,\phi_1)\).

**Proof.** With \((X_2)_b=(U_2,\phi_2b,x_2)\), factor

\[
A=k_b A_0,
\qquad A_0=(a,\mathrm{id}_{V_1},\alpha):X_1\to(X_2)_b.
\]

Equation (4.3) says that (1) is equivalent to invertibility of \(Q(A_0)\). Choose \(\tau\) and \(\delta\) as in (3). Put \(X_a=(U_1,\phi_1,a^*x_2)\). Then

\[
A_0=(a,\mathrm{id}_{V_1},\tau)
(\mathrm{id}_{U_1},\mathrm{id}_{V_1},\delta),
\]

and the first factor is in \(R\). By (5.2), invertibility of \(Q(A_0)\) is equivalent to (3).

If (3) holds, take cartesian \(\gamma:z\to x_1\), \(\rho:w\to a^*x_2\) over an admissible \(c:W\to U_1\), with \(\delta_W:z\to w\) the invertible pullback of \(\delta\). Then

\[
\alpha\gamma=\tau\delta\gamma=\tau\rho\delta_W
\]

is strongly cartesian, proving (2). If (2) holds, \(Q(Ar)\) is strongly cartesian by the valid implication proved in Section 4. Since \(Q(r)\) is an isomorphism,

\[
Q(A)=Q(Ar)Q(r)^{-1}
\]

is strongly cartesian. This proves (1) and the equivalence.

Now let \(f=Q(A)Q(r_0)^{-1}\) be any chosen roof, with \(r_0:Z\to X\) in \(R\) and \(A=(a,b,\alpha):Z\to Y\). Because \(Q(r_0)\) is an isomorphism, \(f\) is cartesian if and only if \(Q(A)\) is cartesian. The equivalence just proved supplies, precisely when \(f\) is cartesian, a further \(r_1=(c,\mathrm{id},\gamma):Z'\to Z\) in \(R\) with \(\alpha\gamma\) cartesian. Therefore

\[
f=Q(Ar_1)Q(r_0r_1)^{-1}
\tag{6.1}
\]

is a roof with cartesian numerator and denominator. This proves the useful existential roof statement from the adjointness proof, even though the stronger statement about an arbitrary numerator is false.

For an arrow \(A\) over \(\mathrm{id}_V\), the criterion has the particularly concrete form

\[
Q(A)\text{ invertible}
\quad\Longleftrightarrow\quad
\exists r\in R\text{ with }Ar\in R.
\tag{6.2}
\]

This is a property of the present fibred-category construction proved above; it was not assumed as a general assertion about right multiplicative systems.

## 7. The exact obstruction to reflection

For a fixed \((U,\phi:V\to u(U))\), define a class of vertical morphisms of \(\mathcal S_U\) by

\[
W_\phi=
\{\delta:x\to y:\text{some admissible }(c:W\to U,\psi:V\to u(W))
\text{ makes }c^*\delta\text{ invertible}\}.
\]

Section 5 proves that \(W_\phi\) is the inverse image of the isomorphisms under the actual functor

\[
J_\phi:\mathcal S_U\longrightarrow L_V,
\qquad x\longmapsto(U,\phi,x),\quad
\delta\longmapsto Q(\mathrm{id}_U,\mathrm{id}_V,\delta).
\]

In particular it contains all isomorphisms, is closed under composition, and has the two-out-of-three property. These assertions follow by applying the functor \(J_\phi\) and the corresponding identities for isomorphisms; they do not require any faithfulness assertion for \(J_\phi\).

For \(\alpha=\tau\delta\) as in Section 6, \(\alpha\) itself is cartesian exactly when \(\delta\) is an isomorphism, whereas \(Q(a,b,\alpha)\) is cartesian exactly when \(\delta\in W_{\phi_1}\). Thus the obstruction is the precisely defined class

\[
W_{\phi_1}\setminus\operatorname{Iso}(\mathcal S_{U_1}).
\]

Reflection for all triples is equivalent to \(W_\phi=\operatorname{Iso}(\mathcal S_U)\) for every \((U,\phi)\). Equivalently, each \(J_\phi\) is conservative. The source hypotheses do not imply this: in Section 3 the class contains \(v\). A sufficient additional assumption is that every admissible pullback functor \(c^*\) is conservative, but that extra assumption is unnecessary for the construction, the roof characterization, or the adjointness statement.

## 8. Full repair of the cartesian-functor step in adjointness

Let \(q:\mathcal T\to\mathcal D\) be fibred, and let

\[
H:\mathcal S\longrightarrow u^p\mathcal T
\]

be a cartesian functor over \(\mathcal C\). For \(x\in\mathcal S_U\), write \(h_x=\operatorname{pr}(H(x))\in\mathcal T_{u(U)}\). For \(\alpha:x\to y\) over \(a:U\to U'\), write

\[
h_\alpha=\operatorname{pr}(H(\alpha)):h_x\to h_y,
\qquad q(h_\alpha)=u(a).
\]

If \(\alpha\) is cartesian, then \(h_\alpha\) is cartesian. Here is the needed justification for the projection. A cartesian lift \(z\to h_y\) in \(\mathcal T\) over \(u(a)\) gives a cartesian arrow \((U,z)\to(U',h_y)\) in \(u^p\mathcal T\), by its universal property with a specified \(\mathcal C\)-base arrow. The latter arrow and \(H(\alpha)\) are cartesian lifts of \(a\), so their domains are related by a vertical isomorphism intertwining the arrows. Projecting that isomorphism shows that \(h_\alpha\) is the composite of the chosen cartesian lift with a vertical isomorphism. Thus it is cartesian.

For every \(X=(U,\phi:V\to u(U),x)\), choose a cartesian arrow

\[
\lambda_X:t_X\longrightarrow h_x\quad\text{over }\phi.
\]

Define \(G'(X)=t_X\). For \(A=(a,b,\alpha):X\to Y\), define \(G'(A)=\beta_A:t_X\to t_Y\) by the exact conditions

\[
q(\beta_A)=b,\qquad
\lambda_Y\beta_A=h_\alpha\lambda_X.
\tag{8.1}
\]

Existence and uniqueness follow from cartesianness of \(\lambda_Y\), because

\[
q(h_\alpha\lambda_X)=u(a)\phi_X=\phi_Yb.
\]

The identity arrow of \(t_X\) satisfies (8.1) for \(A=\mathrm{id}_X\), so \(G'\) preserves identities. For composable \(A:X\to Y\), \(B:Y\to Z\),

\[
\lambda_Z\beta_B\beta_A
=h_{\alpha_B}\lambda_Y\beta_A
=h_{\alpha_B}h_{\alpha_A}\lambda_X
=h_{\alpha_B\alpha_A}\lambda_X.
\]

The base is \(b_Bb_A\), so uniqueness in (8.1) yields \(\beta_{BA}=\beta_B\beta_A\). Hence \(G'\) is a functor over \(\mathcal D\).

If \(r=(a,\mathrm{id}_V,\alpha)\in R\), then \(h_\alpha\) and \(\lambda_X\) are cartesian. Equation (8.1) and cancellation through cartesian \(\lambda_Y\) show that \(\beta_r\) is cartesian. Its base is an identity, so it is an isomorphism. The localization universal property therefore gives a unique functor

\[
G:L\longrightarrow\mathcal T,\qquad GQ=G',
\]

over \(\mathcal D\), with

\[
G\bigl(Q(A)Q(r)^{-1}\bigr)=G'(A)G'(r)^{-1}.
\]

It remains to prove that \(G\) is cartesian. This can be done directly from canonical lifts, with no detection-of-isomorphisms lemma. For \(k_b:Y_b\to Y\) of (4.1), its \(\mathcal S\)-component is an identity, so (8.1) becomes

\[
\lambda_Y G'(k_b)=\lambda_{Y_b}.
\tag{8.2}
\]

Both \(\lambda_Y\) and \(\lambda_{Y_b}\) are cartesian, over \(\phi\) and \(\phi b\), respectively. Cartesian cancellation proves that \(G'(k_b)\) is cartesian over \(b\).

Now take any strongly cartesian \(f:X\to Y\) of \(L\) over \(b\). By (4.2)–(4.3),

\[
f=Q(k_b)i_f
\]

for a vertical isomorphism \(i_f:X\to Y_b\). Every functor preserves isomorphisms, so

\[
G(f)=G'(k_b)G(i_f)
\]

is a composite of a cartesian arrow and an isomorphism. It is therefore cartesian. This proves the required implication for every localized cartesian arrow, including the arrows for which the source's converse fails.

Alternatively, (6.1) gives the roof-based proof the source intended: choose a right refinement with cartesian numerator \(\alpha\gamma\), apply the already proved implication from cartesianness of that numerator to cartesianness of its \(G'\)-image by (8.1) and cancellation, and compose with the inverse image of the refined denominator. That proof is valid only after proving the refined-roof criterion; it does not justify the statement for an arbitrary representative.

## 9. Precise correction recommendations

The affected source is [the cartesian characterization in `lemma-fibred-category-pullback`](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L2991), [its omitted converse](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3124), and [the dependent adjointness step](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks.tex#L3274).

1. The original “if and only if” claim must not remain. Its forward direction from cartesian \(\alpha\) to cartesian \(Q(A)\) is correct. The reverse direction is contradicted by Section 3.
2. A concise repair can retain only the valid implication, remove the omitted-converse assertion, and prove the cartesian-functor step by (4.2)–(4.3) and (8.2). This retains the entire stated fibred-category and adjointness conclusions and supplies the missing mathematics.
3. If a complete characterization is wanted at the original location, state Section 6, with an allowed right refinement, and supply the proof from Sections 4–6. Its quantifier is essential: the numerator becomes cartesian after a suitable refinement, and need not be cartesian before refinement.
4. In the roof in the adjointness proof, the denominator has target \(X\), not \(Y\): it is \(r:X'\to X\). Its base is the identity of the source base object. The notation for the numerator's functor image has three components, \(G'(a,b,\alpha)\).

This note establishes the counterexample, the complete refined-roof characterization, the exact obstruction to reflection, and the corrected cartesian-functor argument. It makes no claim to have verified the omitted mutually-quasi-inverse checks at the end of the source's adjointness proof or the later stackification arguments.
