# EGA IV §18.12: finiteness, Zariski's Main Theorem and ampleness

**Sixteen of the eighteen numbered items have supported correspondences
with existing Stacks results.** They include étale-local finite neighbourhoods,
the proper/quasi-finite finiteness criterion, Zariski's Main Theorem,
normalization under étale base change, and two ampleness criteria.
No duplicate root-chapter theorem is added.

The remaining two items have different roles: IV.18.12.9 is explicitly
conjectural in the source; IV.18.12.14 has a supported normalization
construction but an unchecked assertion about its historical proof route.
Neither is being reported as a missing established Stacks theorem.

## Sources and what the comparison proves

The [pinned French transcription](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega4/ega4-18-fr.tex#L2207-L2419)
and [separate English discovery witness](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/source_aligned/ega4-18.tex#L3235-L3556)
are linked individually in the [full comparison](ega-iv-18-12.json).
That file records hypotheses, proof arguments, target tags, exact source and
target spans, and the unresolved clauses.

The existing independent AI review is reused after checking its bytes and
bindings against the current committed tree: 124 recorded spans, 39 tag
bindings, and 18 distinct source identities. This is not a new independent
review, a machine-checked formalization, expert approval, or a fresh collation
of the printed original. Matching bytes validates the evidence identity;
the mathematical arguments are recorded separately.

All item numbers in the table are prefixed by **IV.18.12**.

| Item | Mathematical content | Result |
|---|---|---|
| .1 | A finite étale-local neighbourhood of an isolated fibre point | Derived; separatedness makes the neighbourhood closed as well as open |
| .2 | The neighbourhood can preserve the base residue field | Stronger target [02LK](https://stacks.math.columbia.edu/tag/02LK) |
| .3 | A finite discrete fibre can be split off after étale base change | Stronger target [02LP](https://stacks.math.columbia.edu/tag/02LP) |
| .4 | Finiteness criterion; proper and quasi-finite implies finite | Exact [02LS](https://stacks.math.columbia.edu/tag/02LS) |
| .5 | In that criterion, closedness after étale base change suffices | Derived from the actual proof |
| .6 | Closed immersion iff proper monomorphism; equivalent fibre criterion | Derived |
| .7 | A closed-immersion criterion near one fibre | Derived, including an essential further shrinking |
| .7.1 | An affine neighbourhood of an entire fibre gives local affineness | Derived, retaining the French affine-base conclusion |
| .8 | Integral iff affine and universally closed | Exact [01WM](https://stacks.math.columbia.edu/tag/01WM) |
| .9 | Proposed removal of the affine hypothesis under integral fibres | Conjectural remark; not proved or declared currently open here |
| .10 | Injective and universally closed implies integral | Derived; universal injectivity is not required |
| .11 | Universal homeomorphism iff integral, radicial and surjective | Derived |
| .12 | A separated quasi-finite morphism is quasi-affine | Stronger normalization factorization [02LR](https://stacks.math.columbia.edu/tag/02LR) |
| .13 | Finite Zariski Main factorization over a qcqs base | Exact [05K0](https://stacks.math.columbia.edu/tag/05K0) |
| .14 | Normalization gives an alternative route to that factorization | Construction covered; historical dependency claim remains partial |
| .15 | Integral closure commutes with étale base change | Exact [03GE](https://stacks.math.columbia.edu/tag/03GE) |
| .16 | Pullback of relative ampleness along a separated quasi-finite map | Derived |
| .17 | Ampleness detected by the canonical map to the full section-ring Proj | Both explicit criteria derived |

## The two Zariski Main statements

For a quasi-finite separated morphism $f:X\to Y$, normalize $Y$ in $X$.
[02LR](https://stacks.math.columbia.edu/tag/02LR) gives

$$
X\xrightarrow{j}\overline Y\xrightarrow{\nu}Y,
\qquad j\text{ a quasi-compact open immersion},\quad\nu\text{ integral}.
$$

This implies the quasi-affineness assertion of .12 without imposing that
the base itself be quasi-compact or quasi-separated.

If $Y$ is additionally quasi-compact and quasi-separated,
[05K0](https://stacks.math.columbia.edu/tag/05K0) supplies .13: $f$ factors
as a quasi-compact open immersion into a scheme finite over $Y$.
The proof approximates the integral algebra by finite quasi-coherent
subalgebras and descends the relevant open along that limit. The qcqs-base
hypotheses must remain visible; the integral and finite factorizations are
not interchangeable without them.

The normalization argument also explains the substantive construction in
.14. Étale-local splitting gives a product algebra with a finite factor.
Integral closure respects the étale base change and the product splitting,
and is already the whole finite factor. On that component the comparison
map is an isomorphism; descent gives the required open immersion.
What has **not** been checked is the historical claim that this proof avoids
EGA IV.8.12.8 while depending on IV.18.5.11 and IV.8.12.9. This limitation
concerns the provenance of the proof, not an absent construction.

## Why the local closed-immersion argument needs another shrink

In .7, $f$ is locally of finite type. Near a chosen $y\in Y$, suppose that
$f$ is universally closed and its fibre is empty or
$\operatorname{Spec}(\kappa(y))$.
An empty fibre is handled by removing the closed image. Otherwise .7.1
first gives an affine neighbourhood of the base over which the morphism
is affine. Universal closedness makes it integral by
[01WM](https://stacks.math.columbia.edu/tag/01WM), and local finite type
makes it finite by [01WJ](https://stacks.math.columbia.edu/tag/01WJ).

Write that finite map as $A\to B$, with $y$ corresponding to
$\mathfrak p$. The fibre condition says

$$
B\otimes_A\kappa(\mathfrak p)=\kappa(\mathfrak p).
$$

It does not justify declaring the same condition on every nearby fibre.
Instead apply localized Nakayama
[0GLX](https://stacks.math.columbia.edu/tag/0GLX) to the finite module $B$
and its element $1$. There exists $t\notin\mathfrak p$ such that $1$
generates $B_t$ as an $A_t$-module. Therefore $A_t\to B_t$ is surjective:
the restriction over $D(t)$ is a closed immersion. This explicit shrinking
completes the compressed argument in the witnesses.

For .7.1, choose an affine base neighbourhood $U_0$ and an affine
neighbourhood $V\subset f^{-1}(U_0)$ of the whole fibre. Closedness of $f$
allows removal of $f(X\setminus V)$. A smaller principal affine open
$U\subset U_0$ then has
$f^{-1}(U)=V\times_{U_0}U$, an affine scheme. This retains the stronger
French conclusion that $U$ is affine, rather than only open.

## Ampleness: the full section ring matters

For .16, let $g:Y\to S$ be quasi-compact, $f:X\to Y$ separated and
quasi-finite, and $\mathcal L$ relatively ample for $g$.
The quasi-affineness of $f$ above and the pullback theorem
[0892](https://stacks.math.columbia.edu/tag/0892), checked over affine opens
of $S$, show that $f^*\mathcal L$ is relatively ample for $g\circ f$.
No finite-type assumption on $g$ is inserted.

For .17, assume $h:X\to Z$ is of finite type and $Z=\operatorname{Spec}(A)$.
For an invertible sheaf $\mathcal L$ set

$$
S=\bigoplus_{n\geq0}\Gamma(X,\mathcal L^{\otimes n}).
$$

This is the **full section ring**, not a chosen linear subsystem.
Assume every point lies in the nonvanishing locus of some positive-degree
section, so the canonical evaluation map $u:X\to\operatorname{Proj}(S)$
is everywhere defined. The two criteria assert that $\mathcal L$ is ample
exactly when either:

- $h$ is separated and $u$ has finite discrete fibres; or
- $u$ is radicial.

For the first condition, $u$ is locally of finite type and separated.
Its quasi-compactness comes from the **canonical-map** theorem
[01Q0](https://stacks.math.columbia.edu/tag/01Q0), not from assuming that
an arbitrary map out of a quasi-compact scheme is quasi-compact.
It is consequently quasi-finite and hence quasi-affine.

Choose finitely many homogeneous sections covering $X$ by their
nonvanishing loci and raise them to a common positive degree. Their
standard opens form a quasi-compact open $Y'\subset\operatorname{Proj}(S)$
containing $u(X)$. The construction in
[01MW](https://stacks.math.columbia.edu/tag/01MW) supplies a suitable
positive multiple $d$ for which $\mathcal O(d)|_{Y'}$ is invertible and
ample. Evaluation identifies its pullback with $\mathcal L^{\otimes d}$.
Quasi-affine pullback preserves ampleness, and
[01PT](https://stacks.math.columbia.edu/tag/01PT) then gives ampleness of
$\mathcal L$ itself. Neither standard grading nor global quasi-compactness
of the entire Proj is assumed.

Conversely, ampleness makes $u$ an open immersion by
[01Q1](https://stacks.math.columbia.edu/tag/01Q1), hence radicial. A radicial
$u$ is separated and universally injective; since Proj is separated over
$Z$, this implies the first criterion. This proves both explicit statements.
The final invitation to formulate analogous relative criteria is an
unformulated exercise and contributes no additional counted result.

## Boundaries still visible

For .9, “integral fibres” means that each fibre morphism to
$\operatorname{Spec}(\kappa(y))$ is integral. It does **not** mean merely
that the fibre is an integral scheme. The proposed conclusion from
separatedness, universal closedness and these integral fibre morphisms
would require an affineness argument not supplied by this comparison.
No present-day open-problem status is asserted.

The English proof language concerning strict henselization differs from
the French henselization wording near .1–2. The target theorem proves the
stated neighbourhood and residue-field claims without equating those
phrases. Their historical translation/proof provenance is not certified.

These are finite section-level comparisons, not a global EGA coverage
percentage or a declaration that the full integration program is complete.
