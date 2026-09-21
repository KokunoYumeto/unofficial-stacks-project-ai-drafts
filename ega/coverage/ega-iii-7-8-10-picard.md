# EGA III.7.8.10(ii): the Picard cotangent module and a jumping family

This note supplies the two arguments previously missing from the
[III §§7.7–7.9 comparison](ega-iii-7-7-9.md): the representing module is the
cotangent module of the relative Picard space at its identity, and it need
not be locally free even for a smooth projective family. The example below
has $h^1(\mathcal O)=1$ on its characteristic-zero fibre and $h^1(\mathcal
O)=2$ on its characteristic-two fibre.

**Status: primary-session proof draft, not yet a root-source addition.**
The cotangent calculation derives from existing Stacks results. The explicit
family is a candidate addition, not a theorem already located in the pinned
Stacks source. It still needs conversion into the cumulative LaTeX source,
dependency checking there, and the chapter build and release checks. The
32-item comparison therefore remains 30 supported, one qualified and one
partial at the root-integration level; the last item now has a concrete proof
and implementation target instead of an unspecified example request.

The [evidence ledger](ega-iii-7-8-10-picard.json) binds the French transcription
and the exact Stacks passages consulted. This is not an independent expert
review or proof-assistant certificate. No new official Stacks tag is assigned.

## The entire coefficient functor, not just a tangent-space dimension

Let $S$ be locally Noetherian and $f:X\to S$ be proper, flat and finitely
presented. First assume that $\mathcal O_T\to f_{T*}\mathcal O_{X_T}$ is an
isomorphism for every base change $T\to S$. The relative fppf Picard functor
is then an algebraic space $P$ by [0D2C](https://stacks.math.columbia.edu/tag/0D2C).
Write $e:S\to P$ for its identity. Suppose $Q$ represents the degree-one
coefficient functor, as in EGA III.7.8.9:

$$
R^1f_*f^*M\simeq\mathcal Hom_S(Q,M)
$$

for every quasi-coherent $M$. Then, canonically,

$$
Q\simeq e^*\Omega_{P/S}.
$$

Here is the identification with its sheafification issue included. Work
locally on an affine base $T$. After a faithfully flat, finitely presented
cover we can give $X_T\to T$ a section: use $X_T\to T$ itself, with its
diagonal section after base change, and refine by affine opens. Surjectivity
follows from the universal degree-zero hypothesis. Flat base change
[02KH](https://stacks.math.columbia.edu/tag/02KH) allows this reduction.
Here $Q$ is coherent on the locally Noetherian base, so its Hom functor
also commutes with flat base change.

For an arbitrary quasi-coherent $M$ on $T$, put
$T[M]=\operatorname{Spec}_T(\mathcal O_T\oplus M)$ with $M^2=0$. This is a
split square-zero thickening, not just the special case $M=\mathcal O_T$.
The pullback thickening of $X_T$ has ideal $f_T^*M$. Its global units reduce
surjectively because the thickening is split. The units exact sequence
[0C6R](https://stacks.math.columbia.edu/tag/0C6R) consequently gives

$$
\ker\bigl(\operatorname{Pic}(X_{T[M]})\to\operatorname{Pic}(X_T)\bigr)
\simeq H^1(X_T,f_T^*M).
$$

The chosen section and the universal degree-zero hypothesis identify the
relative Picard functor with the split quotient by the Picard group of the
base, by [0D28](https://stacks.math.columbia.edu/tag/0D28). On the affine base
$T$, the same units sequence and quasi-coherent cohomology vanishing show
$\operatorname{Pic}(T[M])\simeq\operatorname{Pic}(T)$. Thus

$$
\ker\bigl(P(T[M])\to P(T)\bigr)
\simeq H^1(X_T,f_T^*M).
$$

On the other hand, the difference-of-lifts calculation for differentials,
[02H5](https://stacks.math.columbia.edu/tag/02H5) for schemes and
[04D0](https://stacks.math.columbia.edu/tag/04D0) for algebraic spaces,
identifies the left side at the identity with
$\operatorname{Hom}_T(e_T^*\Omega_{P_T/T},M)$. The zero lift is supplied by
the identity section. These identifications are additive, natural in **all**
$M$, and compatible with flat base change. Yoneda now identifies the two
representing modules. The canonical identification descends from the cover.
No smoothness of $P$ was used.

EGA assumes the more general separable-algebra condition on degree-zero
cohomology. After shrinking as in III.7.8.6–7.8.10(i), the Stein factor is
finite étale. Étale locally it splits, and $X$ becomes a finite disjoint
union of proper flat families with universal degree-zero cohomology equal
to the base. Apply the argument to each component. The relative fppf Picard
sheaf of the disjoint union is the product of their Picard sheaves; this
follows after sheafification, since line bundles on the base are fppf
locally trivial. Both the coefficient functor and the cotangent module at
the identity are finite direct sums. The identifications descend again.
When the Picard space is a scheme, this is precisely EGA's scheme wording.

The existing draft's smooth-Picard tangent lemma is not a substitute: it
assumes smoothness near the identity and concludes local freeness. Nor may
one simply replace $Q$ by $(R^1f_*\mathcal O_X)^\vee$ without a local-freeness
hypothesis. Evaluating a represented functor only at $M=\mathcal O_S$ does
not recover the representing module in general.

## A smooth projective family with a nonfree representing module

Set $R=\mathbb Z_{(2)}$ and let $E\subset\mathbb P^2_R$ be

$$
Y^2Z+XYZ=X^3+XZ^2.
$$

Its affine equation is $y^2+xy=x^3+x$. The Weierstrass discriminant is
$-63$, a unit of $R$. Directly, the special-fibre derivatives on $Z=1$
cannot vanish simultaneously on the curve: in characteristic two the
$y$-derivative is $x$, forcing $x=y=0$, where the $x$-derivative is nonzero.
At the point at infinity $O=[0:1:0]$, the $Z$-derivative is nonzero.
The characteristic-zero fibre is nonsingular as well (equivalently,
its discriminant is nonzero). Thus $E/R$ is smooth and projective, with
geometrically connected genus-one fibres; the genus calculation is
[0BYD](https://stacks.math.columbia.edu/tag/0BYD).

Two involutions will be used. One is

$$
\iota(x,y)=(x,-y-x).
$$

The other is initially written on $x\ne0$ as

$$
\tau(x,y)=\left(\frac1x,-\frac{y+x}{x^2}\right).
$$

It preserves the equation and squares to the identity. For completeness,
it extends over the missing points as follows. At $P=(0,0)$ set
$D=1-y+x^2$, so $xD=y^2$. In the target chart $Y'=1$, its coordinates are

$$
\frac{X'}{Y'}=-\frac{y}{D+y},\qquad
\frac{Z'}{Y'}=-\frac{y^3}{D(D+y)}.
$$

Both denominators are units at $P$, and the image is $O$. At $O$, write
$u=X/Y$, $v=Z/Y$, and $C=1+u-uv$. The equation says $vC=u^3$, and the
target affine coordinates are

$$
x'=\frac{u^2}{C},\qquad y'=-\frac{u(1+u)}{C}.
$$

These are regular at $O$ and give $P$. Together with the $x\ne0$ chart
they cover $E$. Consequently $\tau$ is a global involution interchanging
$P$ and $O$. This construction does not require a separate elliptic-curve
group-law assertion.

The involution $\tau$ has no fixed subscheme. Away from $P,O$, the fixed
equations imply $x^2=1$ and $2y=-x$. Multiplying the cubic equation by four
then gives $1+8x=0$. Combining this with $x^2=1$ gives $63=0$, impossible
over $R$. At $P$ and $O$ the two disjoint sections are interchanged.

Let $\Gamma$ be the **constant** group scheme $\mathbb Z/2\mathbb Z$ over
$R$, and define

$$
B=E/\langle\tau\rangle,\qquad
X=(E\times_R E)/\langle\tau\times\iota\rangle.
$$

Both actions are free. The quotient theorem
[07S7](https://stacks.math.columbia.edu/tag/07S7) gives schemes, and both
quotient maps are finite étale torsors of degree two. In particular, the
characteristic-two quotient is still étale: the constant group scheme is
not $\mu_2$. Smoothness descends along these étale covers. The quotients
are separated by [0BBM](https://stacks.math.columbia.edu/tag/0BBM), and
proper by [03GN](https://stacks.math.columbia.edu/tag/03GN), using their
smoothness for finite type and the surjective proper covering for universal
closedness. The norm of an ample line bundle on either covering is ample
on its quotient, by [0BD2](https://stacks.math.columbia.edu/tag/0BD2) and
[0BD0](https://stacks.math.columbia.edu/tag/0BD0). Since the base is affine,
properness plus ampleness gives projectivity by
[0B45](https://stacks.math.columbia.edu/tag/0B45). Thus $X/R$ is indeed a
smooth **projective** family, not merely a proper algebraic space.

The first projection induces $g:X\to B$. Pulling it back along the
torsor $q:E\to B$ recovers the product projection $E\times_R E\to E$:

$$
\begin{array}{ccc}
E\times_R E&\longrightarrow&X\\
\downarrow\scriptstyle{\mathrm{pr}_1}&&\downarrow\scriptstyle g\\
E&\xrightarrow{q}&B.
\end{array}
$$

This square is cartesian. On each geometric fibre over $R$, $B$ is a
smooth connected genus-one curve: apply the unramified Riemann–Hurwitz
formula [0C1B](https://stacks.math.columbia.edu/tag/0C1B) to its degree-two
étale cover by $E$.

## The cohomology calculation and its characteristic-two trap

Fix a geometric fibre field $k$ of $R$. Flat base change along $q_k$ shows
that $g_{k*}\mathcal O_{X_k}=\mathcal O_{B_k}$ and that
$L_k=R^1g_{k*}\mathcal O_{X_k}$ is the line bundle obtained from the
$\Gamma$-torsor $E_k\to B_k$ using the action of $\iota$ on
$H^1(E_k,\mathcal O_{E_k})$.

That one-dimensional action is multiplication by $-1$. For example, the
regular differential $dx/(2y+x)$ changes sign under $\iota$; the duality
pairing [0BS2](https://stacks.math.columbia.edu/tag/0BS2) for a smooth proper
curve gives the same action on $H^1(\mathcal O)$. On the affine curve the
implicit-differentiation identity supplies the alternate expression where
$2y+x=0$; smoothness ensures that one of the two partial derivatives is a
unit. At infinity the same differential is
$-du/(1+u-2uv)$, which is regular and nonzero at $O$. In
characteristic two one can also see the scalar without any formula: an
involution on a one-dimensional vector space has scalar $1=-1$.

Sections of $L_k$ correspond to functions $a$ on $E_k$ satisfying
$\tau^*a=-a$. Since $E_k$ is geometrically connected and proper, these
functions are constants. It follows that

$$
h^0(B_k,L_k)=
\begin{cases}0,&\operatorname{char}k=0,\\1,&\operatorname{char}k=2.
\end{cases}
$$

In the second case the character itself is trivial, so $L_k\simeq
\mathcal O_{B_k}$. The low-degree Leray sequence, with
$H^2(B_k,\mathcal O_{B_k})=0$ because $B_k$ is a curve, now gives

$$
0\longrightarrow H^1(B_k,\mathcal O_{B_k})
\longrightarrow H^1(X_k,\mathcal O_{X_k})
\longrightarrow H^0(B_k,L_k)\longrightarrow0.
$$

| Geometric fibre | $h^1(B_k,\mathcal O)$ | $h^0(B_k,L_k)$ | $h^1(X_k,\mathcal O)$ |
| --- | ---: | ---: | ---: |
| Characteristic zero | 1 | 0 | 1 |
| Characteristic two | 1 | 1 | 2 |

We have **not** computed the cohomology of the quotient by taking invariants
of $H^1(E_k\times E_k,\mathcal O)$. Such an invariants argument is not exact
in characteristic two and would miss the extra class. The valid argument
descends the relative direct-image line bundle and then uses Leray.

Finally, the fibres of $X/R$ are geometrically connected and smooth, hence
have only scalar global functions. EGA's degree-zero hypothesis holds.
For its representing module $Q$, use the coefficient module $k$ itself:

$$
\operatorname{Hom}_R(Q,k)\simeq H^1(X_k,\mathcal O_{X_k}).
$$

Thus the fibre dimensions of $Q$ are respectively 1 and 2, so $Q$ cannot
be locally free at the closed point of $\operatorname{Spec}R$. Combined
with the first calculation this gives a non-locally-free
$e^*\Omega_{\operatorname{Pic}_{X/R}/R}$. No specific elementary-divisor
decomposition of $Q$, and no nonflatness assertion about the whole Picard
scheme, is inferred from this calculation.

The quotient pattern is classical Igusa-type geometry; for a primary modern
reference to the translation/inversion construction see
[Yang, §2.3, the example after Corollary 2.3.4](https://arxiv.org/html/2410.09969v3#S2.SS3).
That reference uses a different second elliptic curve in characteristic two.
The explicit mixed-characteristic equations and the calculation above are
given here separately; they are not quoted from that paper or asserted to
be its example verbatim.

## Remaining integration work

Promote the all-coefficient cotangent statement and the explicit family into
the cumulative LaTeX chapter, retaining the affine-cover/sheafification
argument, quotient projectivity, and characteristic-two warning. Verify
every chapter dependency, build, cross-reference and affected page before
claiming source integration. This note changes no root theorem, PDF or
Zenodo release. The wider EGA I–IV coverage program remains unfinished.
