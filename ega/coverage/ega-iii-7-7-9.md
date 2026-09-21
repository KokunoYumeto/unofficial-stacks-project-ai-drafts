# EGA III §§7.7–7.9: exactness, base change and Euler characteristics

These comparisons explain how existing Stacks arguments supply EGA's
cohomology-and-base-change criteria, coherent representing modules, and
constancy of Euler characteristics and Hilbert polynomials. **Thirty selected
numbered items are supported without an additional convention qualification;
one is qualified and one remains partial. No new theorem is claimed.**
This is not a claim that all of EGA III §7 has been integrated.

The [original row-by-row comparison](ega-iii-7-7-9.json) preserves the earlier
30-supported/two-partial snapshot. The [global-hypertor supplement](ega-iii-7-7-12-hypertor.md)
subsequently identifies III.7.7.12(ii)'s construction and exchange map, with
the necessary coefficient-extension convention stated explicitly.
The [Picard cotangent and jumping-family supplement](ega-iii-7-8-10-picard.md)
now supplies a proof draft for III.7.8.10(ii), including an explicit smooth
projective family. Its cumulative LaTeX integration remains pending, so the
root-integration count above has not been increased.
The original comparison contains the hypotheses,
derivations, exact source spans, target labels and hashes. A fresh
primary-session AI review checked the mathematical arguments against the
[pinned French transcription](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-7-fr.tex)
and the [committed Stacks draft](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/75aec3348656b93fc75fae9759472ff0fa8615d3).
It is neither a separate independent review nor a proof-assistant check.
The French witness is an editable transcription; original printed pages
were not freshly collated in this checkpoint.

## The common model, with the full complex retained

Let $f:X\to Y$ be proper, with $Y$ locally Noetherian, and let
$P_\bullet$ be a bounded-below complex of coherent modules flat over $Y$.
Use cohomological indices $P^i=P_{-i}$ and put $K=Rf_*P^\bullet$.
Stacks [0CSC](https://stacks.math.columbia.edu/tag/0CSC) makes $K$
pseudo-coherent; [064U](https://stacks.math.columbia.edu/tag/064U) gives
a bounded-above finite-free model on each affine base. The
[projection formula](https://stacks.math.columbia.edu/tag/08EU) identifies
EGA's coefficient functor with

$$
T_p(M)=H^{-p}(K\otimes^{\mathbf L}M).
$$

Thus the comparison covers the whole bounded-below homological complex,
not merely a coherent sheaf placed in degree zero. For a finite input
complex, [0A1H](https://stacks.math.columbia.edu/tag/0A1H) gives perfectness,
and [0658](https://stacks.math.columbia.edu/tag/0658) supplies a global
finite-projective model over an affine base in the required Tor interval.
The precise [base-change map](https://stacks.math.columbia.edu/tag/0A1D)
uses ordinary termwise pullback of the base-flat input complex. This does
not justify replacing nonflat ordinary pullback by derived pullback.

## Exactness and representability: III.7.7.5–III.7.7.10

Write $i=-p$. On an affine base the finite-free model commutes with direct
sums. If $H^i(K\otimes^{\mathbf L}-)$ is right exact, applying it to a
free presentation of $M$ yields the **canonical** formula

$$
H^i(K)\otimes M\ \cong\ H^i(K\otimes^{\mathbf L}M).
$$

The connecting homomorphism in the coefficient long exact sequence shows
that this right exactness is equivalent to left exactness in degree $i+1$.
Under the residue-surjectivity criterion,
[0A1U](https://stacks.math.columbia.edu/tag/0A1U) splits $K$ locally into
a lower complex through degree $i$ and a finite-projective upper complex
$E^{i+1}\to E^{i+2}\to\cdots$. The latter supplies

$$
H^{i+1}(K\otimes^{\mathbf L}M)
=\operatorname{Hom}(Q,M),\qquad
Q=\operatorname{coker}\bigl((E^{i+2})^\vee\to(E^{i+1})^\vee\bigr).
$$

The coherent representing modules glue by the unique isomorphisms
preserving their natural representations. No separatedness of $Y$ is
needed: an affine-open inclusion into a locally Noetherian scheme is
quasi-compact, and [01PE](https://stacks.math.columbia.edu/tag/01PE)
extends the middle object and subobject of a quasi-coherent short exact
sequence. Taking their quotient supplies the locality argument.

Arbitrary base change follows from the canonical coefficient formula.
Conversely, test exchange on the square-zero algebra $A\oplus M$ and
take its $M$ summand. This recovers the formula for every $A$-module;
testing fields alone would not establish that implication.

For the infinitesimal criterion of III.7.7.10, take the
[minimal local model](https://stacks.math.columbia.edu/tag/0BCC) over
$(A,\mathfrak m,k)$. Its differentials vanish modulo $\mathfrak m$.
Surjectivity from $A/\mathfrak m^{n+1}$ to the residue cohomology supplies
cycle vectors generating the middle free module modulo that power,
by Nakayama. The outgoing matrix is therefore zero modulo every power.
[Krull intersection](https://stacks.math.columbia.edu/tag/00IQ) makes it
zero over $A$, leaving a right-exact cokernel functor. The local splitting
lemma spreads this property and proves that its locus is the largest
open set of right exactness.

## The length and reduced-point criteria: III.7.8.4

In that minimal model let $r=\operatorname{rank}F^i$ and
$B=A/\mathfrak m^{n+1}$. The cycles-and-boundaries sequences give

$$
\ell H^i(F\otimes B)
=r\ell(B)-\ell\operatorname{im}(d^{i-1}_B)
          -\ell\operatorname{im}(d^i_B).
$$

EGA's eventual length equality forces both image lengths to vanish for
every sufficiently large $n$. Krull intersection then kills both adjacent
matrices. Conversely a finite-free tensor functor gives those equalities.
The [isolated-cohomology lemma](https://stacks.math.columbia.edu/tag/0A1V)
spreads the free summand and its coefficient formula to a neighborhood.

For the converse from constant fibre dimension at a **reduced point**,
first take the **stupid, termwise truncation** below degree $i-1$.
It keeps the two maps calculating $H^i$ after every coefficient tensor;
a good truncation would not justify this step. Apply
[0BCD](https://stacks.math.columbia.edu/tag/0BCD) to this finite perfect
complex. Its middle term has rank $r=d_i(y)$. If the fibre cohomology
dimension stays $r$, both adjacent matrices have rank zero at every
nearby prime. Their entries are nilpotent, vanish in the reduced local
ring at $y$, and vanish on a smaller neighborhood. This proves exactness
without assuming the whole initial neighborhood is reduced.

## A separable algebra of global sections suffices: III.7.8.6

EGA assumes that $H^0(X_y,\mathcal O_{X_y})$ is a finite product of
finite separable field extensions. Stacks
[0G7Y](https://stacks.math.columbia.edu/tag/0G7Y) is stated with the
stronger hypothesis that the fibre is geometrically reduced. Merely
citing its statement would leave a gap; its proof supplies the needed
argument under EGA's actual hypothesis.

Use [03C3](https://stacks.math.columbia.edu/tag/03C3) to extend the local
base flatly to a local ring whose residue field $k'$ splits the algebra.
[Flat base change](https://stacks.math.columbia.edu/tag/02KH) identifies
the new fibre algebra with $(k')^r$. Each coordinate idempotent is in the
image of the direct-image stalk by
[0G7X](https://stacks.math.columbia.edu/tag/0G7X). Lifting its scalar
coefficients from the new local base gives surjectivity onto the entire
fibre algebra, and faithful field extension descends the original residue
surjection.

Here an idempotent is **in the image**; the chosen preimage is not claimed
to be idempotent. No Zariski splitting of a finite étale cover is inferred.
The splitting lemma now separates $H^0(K)$ from a perfect upper summand
of Tor amplitude at least one. Since $K$ has nonnegative Tor amplitude,
$H^0(K)$ is flat and perfect, hence finite locally free. The coefficient
formula proves cohomological flatness in degree zero.

## Uniform twists and flatness: III.7.9.14

The French statement assumes **Noetherian** $Y$, whereas the checked
English discovery file says only *locally Noetherian*. This comparison
certifies the French statement, not that strengthening.

For flat $\mathcal F$, [02O1](https://stacks.math.columbia.edu/tag/02O1)
gives one global cutoff beyond which all positive direct images of twists
vanish. Its finite-affine-cover proof uses the Noetherian hypothesis.
[0D4E](https://stacks.math.columbia.edu/tag/0D4E) then makes all those
degree-zero direct images locally free.

Conversely, work over $\operatorname{Spec}A$. Ampleness supplies affine
opens $X_s$ for sections $s$ of positive powers $\mathcal L^d$.
[01PW](https://stacks.math.columbia.edu/tag/01PW) gives

$$
\Gamma(X_s,\mathcal F)
=\varinjlim_n\Gamma(X,\mathcal F\otimes\mathcal L^{dn}),
$$

where the transition maps multiply by $s$. Discarding finitely many
initial terms is cofinal. The remaining modules are finite projective
by the hypothesis on high direct images. Their filtered colimit is flat;
the affine opens $X_s$ cover $X$, proving relative flatness. No unproved
global vector-bundle resolution is inserted into this argument.

## What each selected item contributes

“Supported” means an explicit derivation from the linked Stacks mathematics,
not an additional root theorem. The JSON records each derivation separately.

| EGA III item | Content compared | Result |
| --- | --- | --- |
| 7.7.4 | One finite-free coefficient model for the full bounded-below complex | Supported |
| 7.7.5 | Semicontinuity; exactness, exchange and coherent Hom representability | Supported |
| 7.7.6 | Coherent representation of the flat-sheaf section functor | Supported |
| 7.7.7 | Representation of a kernel of two section functors | Supported |
| 7.7.8 | Representation of Hom from a sheaf with the stated two-term vector-bundle presentation | Supported |
| 7.7.10 | Residue and infinitesimal surjectivity; open right-exactness locus | Supported |
| 7.7.11 | Exactness under base change and faithful-flat detection | Supported |
| 7.7.12 | Finite-projective models; nonflat historical global hypertor | Partial: first part supported |
| 7.8.3 | Equivalent pairs of adjacent one-sided exactness conditions | Supported |
| 7.8.4 | Exactness, Artinian lengths, local freeness and the reduced-point converse | Supported |
| 7.8.5 | Exactness in a range versus locally free direct-image cohomology | Supported |
| 7.8.6 | Degree-zero cohomological flatness from separable fibrewise global sections | Supported |
| 7.8.6.1 | Connected locally ringed spaces and nontrivial product rings | Supported |
| 7.8.7 | A common neighborhood with free direct image and residue exchange | Supported |
| 7.8.8 | The unit isomorphism when fibrewise global sections equal the residue field | Supported |
| 7.8.9 | Coherent Hom representation of the degree-one coefficient functor | Supported |
| 7.8.10 | Étaleness of the Stein factor; nonfree representing examples and Picard interpretation | First part supported; explicit second-part proof draft available, root integration pending |
| 7.9.1 | Finite-projective modules, locally free sheaves and residue rank | Supported |
| 7.9.2 | Equality of alternating homology dimensions and term ranks | Supported |
| 7.9.3 | Local constancy for a finite-projective complex | Supported |
| 7.9.4 | Local constancy of the family Euler characteristic | Supported |
| 7.9.5 | Its value on a connected nonempty base | Supported |
| 7.9.6 | Additivity, even shifts and the alternating-term formula | Supported |
| 7.9.7 | Base-change invariance of the Euler function | Supported |
| 7.9.8 | One-degree fibre cohomology gives a locally free sheaf of signed Euler rank | Supported |
| 7.9.9 | The corresponding single-sheaf assertion | Supported |
| 7.9.10 | Vanishing higher direct images gives a locally free degree-zero image | Supported |
| 7.9.10.1 | Positive fibre cohomology vanishes under those hypotheses | Supported |
| 7.9.11 | Hilbert polynomial for all integer twists, constant on connected components | Supported |
| 7.9.12 | Polynomial additivity and base change with the polarization | Supported |
| 7.9.13 | A uniform high-twist cutoff and polynomial rank | Supported |
| 7.9.14 | Flatness characterized by locally free high-twist direct images | Supported under the French Noetherian hypothesis |

Euler comparisons use [0BDJ](https://stacks.math.columbia.edu/tag/0BDJ),
the single-degree argument in [0BDK](https://stacks.math.columbia.edu/tag/0BDK),
and [08AC](https://stacks.math.columbia.edu/tag/08AC) for Hilbert polynomials.
Index reversal leaves parity unchanged. The factor $(-1)^{i_0}$ in
III.7.9.8's French statement is retained; its proof display omits it.
This is a source-comparison note, not a new errata admission.

## Resolved qualification and remaining questions

- **III.7.7.12(ii), subsequently resolved with a qualification:** the
  [global-hypertor supplement](ega-iii-7-7-12-hypertor.md) identifies the
  historical coefficient functor and its canonical exchange maps. The
  extension changes coefficients while keeping the original base for hypertor;
  ordinary geometric pullback followed by recomputation is a different,
  refuted reading. The broader [III.6 partials](ega-iii-6-2-10.md) remain open.
- **III.7.8.10(ii):** the [new supplement](ega-iii-7-8-10-picard.md) proves
  the all-coefficient cotangent identification and gives a smooth projective
  family over $\mathbb Z_{(2)}$ whose representing module has fibre dimensions
  1 and 2. Promote that explicit candidate into the cumulative LaTeX source
  with the full dependency and build checks; do not count this proof note as
  an already integrated root theorem.
- **Other context:** III.7.7.1–7.7.3 are used only under the bounded
  hypotheses above, not certified in unrestricted unbounded generality.
  III.7.7.9 is now treated in a [separate representability comparison](ega-iii-7-7-9-representability.md),
  including the local/global qualification on presentations; it is not
  included in this checkpoint's 32-row count. III.7.8.1 is a definition; III.7.8.2's unrestricted
  locality claim is not separately counted. III.7.1–7.6 are outside this
  selected batch.

The source bytes, 103 spans and 31 target labels are mechanically checked.
Those checks establish identity and traceability, not mathematical truth.
No LaTeX source, PDF or release artifact changed in this documentation
checkpoint, and it does not create a small additional Zenodo version.
