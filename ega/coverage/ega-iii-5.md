# EGA III §5: existence and algebraization are already in Stacks

This comparison supports **23 of 24 mathematical claim/proof units using
existing Stacks results**. The remaining literal-scope comparison concerns
separatedness in III.5.1.7. Its unrestricted reading fails, as the explicit
example below shows. No new root-chapter theorem is claimed.

The content includes Grothendieck's existence theorem for coherent sheaves,
algebraization of formal morphisms and finite covers, and the ample-line-bundle
criterion for algebraizing a proper formal scheme. These are substantive
existing results, not gaps inferred from missing EGA labels.

## What was compared

The [pinned French transcription](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-1-fr.tex#L13168-L14137)
and a separate English discovery witness underlie the
[statement-by-statement comparison](ega-iii-5.json). It records exact source
and target locations, hashes, hypotheses and finite derivations.
The earlier independent AI review is reused after checking its bound bytes
against the current committed tree. This is not a new independent review,
a machine-checked proof, expert approval, or a fresh collation of the printed
French original.

Of 28 numbered objects, two are setup/definitions and two are historical
remarks; none of those four is counted as a proved mathematical claim.
“Derived” below means that the comparison supplies a finite argument from
existing results, rather than finding an identical statement under one tag.

| EGA object | Mathematical content | Comparison |
|---|---|---|
| III.5.1.2 | Cohomology agrees with completion for proper support | Derived |
| III.5.1.3 | Hom comparison; detection of injectivity and surjectivity | Derived, retaining the closed-map hypothesis for detection |
| III.5.1.3.1 | A neighbourhood of the special fibre exhausts a closed-over-base scheme | Derived |
| III.5.1.4–5 | Proper-support existence and its essential image | Exact via [088E](https://stacks.math.columbia.edu/tag/088E) |
| III.5.1.6 | Existence for a proper scheme | Exact via [088C](https://stacks.math.columbia.edu/tag/088C) |
| III.5.1.7 | Recasting existence as compatible coherent modules on thickenings | Covered with separatedness; literal wider reading fails |
| III.5.1.8 | Algebraizing proper closed formal subschemes | Derived |
| III.5.2.2 | Kernels, images and cokernels stay algebraizable | Derived |
| III.5.2.3 | One ample-twist bound controls all infinitesimal levels | Derived |
| III.5.2.4 | Eventual generation by global sections | Derived |
| III.5.2.5 | Projective existence using presentations by ample powers | Exact via [0885](https://stacks.math.columbia.edu/tag/0885) |
| III.5.2.6 | The quasi-projective proper-support case | Derived |
| III.5.3.1–2 | Extension and kernel/cokernel reductions | Derived, including the stated non-separated ambient scope |
| III.5.3.3 | Proper pushforward preserves algebraizability | Derived |
| III.5.3.4 | Control of the adjunction error by an ideal power | Derived after discharging a local algebraization hypothesis |
| III.5.3.5 | Chow reduction and ideal induction prove general existence | The existing proof supplies the reduction |
| III.5.4.1–2 | Algebraizing morphisms and compatible morphism systems | Exact via [0A42](https://stacks.math.columbia.edu/tag/0A42) |
| III.5.4.4 | Algebraizing a finite formal cover of an algebraizable proper target | Stronger target [09ZT](https://stacks.math.columbia.edu/tag/09ZT) |
| III.5.4.5 | An ample special-fibre line bundle yields projective algebraization | Derived |
| III.5.5.1 | Splitting off a proper part from the special fibre | Stronger henselian-pair result [0CT9](https://stacks.math.columbia.edu/tag/0CT9) |
| III.5.5.2 | The resulting proper part contains every proper closed subset | Derived |

## Why the less immediate comparisons work

**Uniform vanishing on a formal scheme (III.5.2.3).** No algebraization is
assumed in advance. On the proper special fibre, the associated graded base
algebra is of finite type and the graded coherent module is generated in
degree zero locally. Graded finiteness
[0897](https://stacks.math.columbia.edu/tag/0897) gives a single twist bound
for positive cohomological degrees of the whole graded module. The same bound
therefore works for each graded summand. Exact sequences between adjacent
quotients give vanishing at every infinitesimal level and surjective maps on
sections. Formal-affine acyclicity, the inverse-limit criterion
[0BKS](https://stacks.math.columbia.edu/tag/0BKS), and
[0D60](https://stacks.math.columbia.edu/tag/0D60) finish the passage to formal
cohomology. This is stronger than merely checking vanishing on one thickening.

**Non-separated ambient reductions (III.5.3.1–2).** Proper algebraic support
is a Serre condition under the finite-type hypotheses of
[0CYV](https://stacks.math.columbia.edu/tag/0CYV), including its non-separated
case. Subobjects, quotients and extensions can consequently be placed on one
proper closed supporting subscheme. Apply proper existence there and push
forward. This argument does not silently add separatedness to these two
reductions or use the general existence theorem circularly.

**The adjunction error (III.5.3.4).** The target
[088B](https://stacks.math.columbia.edu/tag/088B) assumes an algebraization of
a pulled-back system. Locally on an affine chart, a coherent formal module
is a finite module over the completed ring. Pulling that module back to the
proper base-changed scheme supplies the required local algebraization.
The quotient rings and completed adjunction maps agree. The coherent
adjunction errors vanish away from the specified closed locus, so
[01Y9](https://stacks.math.columbia.edu/tag/01Y9) annihilates them by an ideal
power. Exact completion preserves this, and a finite affine cover supplies
one exponent. The extra hypothesis is discharged, not ignored.

**Projective algebraization (III.5.4.5).**
[089A](https://stacks.math.columbia.edu/tag/089A) algebraizes the proper formal
scheme with its ample line bundle. Uniqueness of algebraized morphisms
transports that bundle to any other proper algebraization. Over the affine
base, [01VT](https://stacks.math.columbia.edu/tag/01VT) supplies a single
projective embedding; merely local projectivity would not suffice.

## Why separatedness cannot be dropped

The pinned transcription of III.5.1.7 refers to the finite-type setup of
III.5.1.1, whereas III.5.1.4 and Stacks
[088F](https://stacks.math.columbia.edu/tag/088F) explicitly require
separatedness. The following elementary example distinguishes these scopes.
It is a supplementary primary-session argument, not a claim made by the
preserved independent review.

Let $A=k[[t]]$, $K=k((t))$, and form

$$
X=\operatorname{Spec}(A)\ \mathop{\cup}_{\operatorname{Spec}(K)}\
\operatorname{Spec}(A).
$$

The two affine charts share their generic point but have distinct closed
points. The map $X\to\operatorname{Spec}(A)$ is of finite type and is not
separated. Set $A_n=A/(t^{n+1})$. Because $t$ is invertible on the overlap,

$$
X_n=X\times_A A_n=\operatorname{Spec}(A_n)\amalg\operatorname{Spec}(A_n).
$$

On these two components take the coherent module
$\mathcal F_n=(\widetilde{A_n},0)$, with its natural quotient transition maps.
This is a compatible system, and the support of $\mathcal F_0$ is one
$k$-point, hence proper over $k$.

Suppose a coherent sheaf on $X$ induced this system. Its restrictions to the
two affine charts would give finite $A$-modules $M_1,M_2$. Completion of a
finite module over a Noetherian ring is tensor with the completed ring
([00MA](https://stacks.math.columbia.edu/tag/00MA)). Since $A$ is complete,
this gives

$$
M_1\simeq\varprojlim_n M_1/t^{n+1}M_1\simeq A.
$$

On the other chart, $M_2/tM_2=0$ forces $M_2=0$ by
[Nakayama's lemma](https://stacks.math.columbia.edu/tag/00DV). But a
sheaf on the glued scheme requires an isomorphism on the shared generic
point, which would identify

$$
M_1\otimes_A K=K\quad\text{with}\quad M_2\otimes_A K=0.
$$

That is impossible. Thus this system has **no coherent algebraization at
all**, even before imposing proper support on an algebraization. The wider
non-separated statement is not a missing theorem to add to Stacks.

The separated version is already covered. The historical comparison's
23-supported/1-partial count is retained so that the literal source claim is
not silently replaced by a qualified one. This is not an admitted erratum
for the printed original, a novelty claim, or a claim to have searched all
historical corrections.

## What remains outside this comparison

The historical remarks III.5.4.3 and III.5.4.6 are not counted: this checkpoint
does not construct a proper nonalgebraizable formal scheme or settle the
question about algebraization after removing nilpotents. The subsequent
[hypercohomology comparison](ega-iii-6-2-10.md) retains its own unbounded-domain
limitations. None of these section-level results establishes whole-EGA
completion.
