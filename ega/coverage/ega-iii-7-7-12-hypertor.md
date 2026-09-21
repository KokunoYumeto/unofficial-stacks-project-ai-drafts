# EGA III.7.7.12(ii): global hypertor without flatness

The historical global-hypertor functor in this remark **is accounted for by
existing Stacks mathematics**. Its finite-free model and exchange criterion
work without flatness of the original sheaves. One qualification matters:
**extend the coefficient functor; do not ordinarily pull back the original
sheaf and recompute over the new base.** Those operations can differ.

This resolves the construction question left open in the
[III §§7.7–7.9 comparison](ega-iii-7-7-9.md), while recording that qualification
explicitly. Of that checkpoint's 32 selected items, 30 are supported without
this extra qualification, III.7.7.12 is now qualified rather than unresolved,
and III.7.8.10 remains partial. These are coverage results, not new theorems.

The [source-and-proof ledger](ega-iii-7-7-12-hypertor.json) binds the exact
French passages, Stacks labels, proof steps and byte hashes. The source is
the pinned editable transcription, not a newly collated printed witness.
The review was performed in the primary AI session, without subagents,
independent expert review or proof-assistant verification.

## Identify the historical construction, not just its name

Let $f:X\to Y$ be proper, let $Y$ be locally Noetherian, and let $P_\bullet$
be a homologically bounded-below complex of coherent sheaves. No flatness
over $Y$ is assumed. Write $P^j=P_{-j}$.

On an affine base $\operatorname{Spec}A\subset Y$, choose a finite affine
cover of $X$. Properness makes $X$ separated over this affine base, so its
finite intersections are affine. The alternating Čech total $C$ has finite
Čech width and is bounded above. Its terms, cokernels and cohomology sheaves
are quasi-coherent, so [08C2](https://stacks.math.columbia.edu/tag/08C2) gives

$$
C\simeq R\Gamma(X,P^\bullet).
$$

[III.6.6.1–6.6.2](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-6-fr.tex#L1573-L1679)
defines global hypertor by tensor hyperhomology of these Čech bicomplexes.
The identity-map factor with coefficient module $M$ contributes $M[0]$.
III.6.6.6 allows a projective Cartan–Eilenberg resolution of the first
factor alone. Its total $E$ is a bounded-above complex of projectives:
after reversing indices, all three homological indices are bounded below,
so a fixed total degree contains only finitely many summands.

Thus $E$ is K-flat by [064K](https://stacks.math.columbia.edu/tag/064K).
Projective resolutions [0646](https://stacks.math.columbia.edu/tag/0646)
and their homotopy comparison [064B](https://stacks.math.columbia.edu/tag/064B)
identify this historical total with a modern projective model of $C$.
Tensoring that comparison with $M$ preserves the identification. Therefore

$$
\operatorname{Tor}^{Y}_p(f,1_Y;P_\bullet,M)
\cong \mathcal H^{-p}(Rf_*P^\bullet\otimes_Y^{\mathbf L}M).
$$

This is natural in coefficients and their connecting homomorphisms.
Flat localization of the finite Čech totals is exactly the localization
used to glue the historical construction in III.6.7.1–6.7.2, so the affine
identifications give the displayed sheaf formula. The scheme projection
formula [08EU](https://stacks.math.columbia.edu/tag/08EU) also identifies it
with

$$
\mathcal H^{-p}Rf_*
\bigl(P^\bullet\otimes_X^{\mathbf L}Lf^*M\bigr).
$$

Both tensor and pullback remain derived in this formula.

## Why one finite-free model computes all coefficients

The direct image $C$ is bounded above by
[08D5](https://stacks.math.columbia.edu/tag/08D5). Its cohomology is finite:
for any fixed degree $q$, truncate $P^\bullet$ sufficiently far below.
The same uniform cohomological bound makes the discarded tail contribute
nothing in degrees $q$ and $q+1$. The retained truncation is bounded coherent,
so proper coherent direct image [08E2](https://stacks.math.columbia.edu/tag/08E2)
applies.

Over the Noetherian ring $A$, [066E](https://stacks.math.columbia.edu/tag/066E)
then makes $C$ pseudo-coherent. By [064U](https://stacks.math.columbia.edu/tag/064U)
choose a single bounded-above complex $L$ of finite free $A$-modules representing
$C$. It computes every coefficient functor:

$$
T_p(M)=H^{-p}(L\otimes_A M).
$$

There is no claim that $L$ has finite length. Removing flatness does not turn
every coherent sheaf into a perfect complex.

## The precise exchange map

For $A\to B$ and a $B$-module $M'$, the scalar-extension convention of
[III.7.1.3](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-7-fr.tex#L79-L113)
is to apply the original functor to the underlying $A$-module. Hence

$$
T_p^{(B)}(M')=H^{-p}(L\otimes_A M')
=H^{-p}\bigl((L\otimes_A B)\otimes_B M'\bigr).
$$

This is also III.6.10.1 with one geometric factor and the additional identity
factor over $\operatorname{Spec}B$, keeping the original base $A$ fixed.
The historical coefficient map of III.6.7.10 then gives precisely

$$
H^{-p}(L)\otimes_A B\longrightarrow H^{-p}(L\otimes_A B).
$$

The [previously checked finite-free argument for III.7.7.5](ega-iii-7-7-9.md)
now applies: upper semicontinuity, the equivalent exactness conditions,
tensor and coherent Hom representations, and affine locality all follow.
For the converse from exchange under every ring extension, use the
square-zero algebra $A\oplus M$ and its $M$ summand; residue-field tests
alone are not substituted for this step. Localization and the natural maps
give the corresponding statements on a nonaffine base.

## Why ordinary geometric pullback is a different assertion

Take $A=k[t]$, $X=Y=\operatorname{Spec}A$, $f=1_Y$, and
$P=A/(t)$ concentrated in degree zero. Its finite-free model is
$A\xrightarrow{t}A$ in cohomological degrees $-1,0$. Consequently

$$
T_1(A)=0,\qquad T_1(k)=k.
$$

The surjection $A\to k$ shows that $T_1$ is not right exact. Correct
coefficient extension to $B=k$ tests the exchange map $0\to k$, which is
not an isomorphism—as required.

If one instead pulls $P$ back ordinarily and starts again over $B$, the
identity morphism gives

$$
\operatorname{Tor}_1^B(P\otimes_A B,B)=0
$$

for every $A$-algebra $B$. All those incorrect replacement tests would be
$0\to0$, even though right exactness has failed. This is why dropping the
flatness hypothesis requires keeping the coefficient-extension convention
explicit. The example tests a reading; it is not an erratum admission.

## What this does not settle

The old totalization and the fixed-base nonflat exchange map are now
identified in the stated one-sided-bounded domain. No unresolved construction
gap remains for that coefficient version. The ordinary-geometric replacement
is excluded, with a counterexample, rather than left as a conjectural gap.

This does not compare all six historical hypertor spectral sequences or close
the broader unbounded questions in [III §§6.2 and 6.10](ega-iii-6-2-10.md).
The smooth-projective example and Picard-cotangent identification in
III.7.8.10(ii) remain the next separate question. Official Stacks, translation
sources, and the errata registry were not modified.
