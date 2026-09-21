# EGA III.7.7.9: representing modules without a global presentation

The three clauses of this remark have different outcomes. **Base change of
the representing modules is supported. Removing the two-term presentation
hypothesis is also supported. The relative-ampleness clause needs a
local-versus-global qualification.** These are comparisons with existing
Stacks mathematics, not three new theorems.

This supplements the [comparison of III §§7.7–7.9](ega-iii-7-7-9.md).
The [clause ledger](ega-iii-7-7-9-representability.json) records exact source
spans, proof steps, target labels and hashes. Its authority is the
[pinned French transcription, lines 2841–2904](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-7-fr.tex#L2841-L2904),
not a newly collated printed witness. The checking was performed in the
primary AI session, without sub-agents or proof-assistant verification.

## (i) Why the representing modules commute with base change

Retain the notation and hypotheses of III.7.7.6–7.7.8: $f:X\to Y$ is
proper, $Y$ is locally Noetherian, and the sheaves serving as targets of
the coefficient functors are coherent and flat over $Y$.

Over an affine base $\operatorname{Spec}A$, the direct image of a single
such sheaf has a finite-projective model
$E^0\to E^1\to\cdots$ in nonnegative degrees. Its degree-zero
coefficient functor is represented by

$$
Q=\operatorname{coker}\bigl((E^1)^\vee\to(E^0)^\vee\bigr),
\qquad
H^0(E^\bullet\otimes_A M)=\operatorname{Hom}_A(Q,M).
$$

After any ring map $A\to B$, the
[base-change theorem](https://stacks.math.columbia.edu/tag/0A1D)
identifies the new direct image with $E^\bullet\otimes_A B$.
Duals of finite-projective modules commute with this base change, and
tensor preserves cokernels. The new representing module is therefore
$Q\otimes_A B$.

For the kernel functor in III.7.7.7, the representing module is
$R=\operatorname{coker}(Q'\to Q)$, so the same argument gives
$R\otimes_A B$. In III.7.7.8 the assumed presentation
$E_1\to E_0\to G\to0$ stays right exact under arbitrary pullback;
the pulled-back vector bundles and their duals reduce the assertion
to that kernel case. Unique isomorphisms respecting the representations
glue these affine calculations.

This argument does **not** assume that arbitrary pullback commutes with
sheaf Hom for arbitrary coherent modules. It transports the finite-projective
model and its representing cokernel instead.

## (ii) Relative ampleness supplies local presentations, not automatically global ones

For every affine open $V\subset Y$, an $f$-ample line bundle becomes
ample on $X_V$. Stacks [01VT](https://stacks.math.columbia.edu/tag/01VT)
and [01Q3](https://stacks.math.columbia.edu/tag/01Q3) then provide a
finite direct sum of negative powers surjecting onto $G|_{X_V}$.
Its kernel is coherent; repeat the construction to obtain

$$
E_1\longrightarrow E_0\longrightarrow G|_{X_V}\longrightarrow0.
$$

This is a presentation on all of $X_V$. In particular it is a global
presentation on $X$ when $Y$ is affine. A global presentation also follows
if $X$ has the resolution property—for example, if it has an ample line
bundle in the absolute sense. Relative ampleness alone does not imply that
these locally chosen bundles glue to a presentation on all of $X$.

Here is a counterexample to that unrestricted global reading, using two
existing Stacks results. Let $Y$ be the affine plane with its origin
doubled, from [01JD](https://stacks.math.columbia.edu/tag/01JD).
It is Noetherian, but its two affine charts meet in the nonaffine punctured
plane. Consequently its diagonal is not affine.
[0F8C](https://stacks.math.columbia.edu/tag/0F8C) says that a
quasi-compact quasi-separated scheme with the resolution property has
affine diagonal. Thus $Y$ lacks that property: some coherent sheaf has
no finite-vector-bundle quotient.

Now take $X=Y$ and $f=\operatorname{id}_Y$. The identity is proper,
and $\mathcal O_Y$ is $f$-ample: on every affine base open it is ample.
The global reading of the transcription would give a vector-bundle
quotient for every coherent sheaf on $Y$, contradicting the preceding
example. The local statement remains valid and sufficient for local
representability arguments.

This is a proved qualification of the pinned transcription's wording.
It is **not** an admitted Stacks erratum, and no claim is made here that
the original printed French has been collated or corrected.

## (iii) The presentation hypothesis can nevertheless be removed

The conclusion of III.7.7.8 remains valid for **arbitrary coherent $G$**,
without assuming that $G$ admits the displayed global presentation.
One must prove this directly, not infer a nonexistent presentation from
relative ampleness.

Work over $\operatorname{Spec}A\subset Y$. Apply Stacks
[08IF(A)](https://stacks.math.columbia.edu/tag/08IF) with source
$G[0]$, target $F[0]$, and cutoff $m=0$. It gives a perfect complex $K$
and natural identifications, for every $A$-module $M$ and every $j\leq0$,

$$
H^j(K\otimes_A^{\mathbf L}M)
\cong \operatorname{Ext}^j_X(G,F\otimes_A M).
$$

The negative Ext groups vanish. Hence $K$ has nonnegative Tor amplitude;
perfectness bounds it above. By [0658](https://stacks.math.columbia.edu/tag/0658)
choose a finite-projective model $E^0\to E^1\to\cdots$. Set

$$
N=\operatorname{coker}\bigl((E^1)^\vee\to(E^0)^\vee\bigr).
$$

Then, naturally in every coefficient module,

$$
\operatorname{Hom}_A(N,M)
=\ker(E^0\otimes_A M\to E^1\otimes_A M)
\cong\operatorname{Hom}_X(G,F\otimes_A M).
$$

The construction in 08IF uses a **perfect approximation** to $G$, not a
global resolution of $G$ by vector bundles. This distinction also appears
in the [Hom-functor proof, 08JY](https://stacks.math.columbia.edu/tag/08JY).

To recover the sheaf statement, localize the coefficient module on a
principal base open. Finite presentation of $G$ makes sheaf Hom commute
with this scalar localization; quasi-compactness and quasi-separatedness
of $X$ let global sections commute with the filtered localization.
The natural formula therefore restricts to the corresponding sheaf
formula. On overlaps the local coherent modules represent the same
functor, so the unique compatible isomorphisms glue them to a coherent
$N$ on $Y$. This gives

$$
f_*\mathcal{H}om_X(G,F\otimes f^*M)
\cong \mathcal{H}om_Y(N,M),
$$

and taking global sections gives the global Hom formulation. The argument
does not require $Y$ to be separated or $X$ to have the resolution property.

## Result and remaining boundaries

The one numbered remark is now compared clause by clause: two clauses
are supported by existing Stacks arguments, and one has a valid local
form with its unrestricted global reading refuted. No root theorem,
translation source or errata registry was changed.

The separate questions in III.7.7.12(ii) about historical global hypertor,
and III.7.8.10(ii) about a smooth-projective example and Picard cotangent
interpretation, remain open in this comparison program. Resolving this
remark does not resolve those questions or complete EGA III.
