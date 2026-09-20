# EGA III §§6.2 and 6.10: hypercohomology and base-change representatives

This bounded comparison supports **seven mathematical units from existing
Stacks results**. Five further units remain partial because their full
historical domain or construction has not been matched. One reindexing
convention is checked separately and is not counted as a theorem.

The key positive result is concrete: for a proper morphism over a Noetherian
affine base, the cohomology of a coherent, base-flat complex can be represented
by a fixed bounded-above complex of finite free base modules, compatibly with
arbitrary base change. For a single base-flat coherent sheaf, that representative
can instead be a bounded complex of finite projectives in a precise degree
range. These are existing derivations, not seven new root-chapter theorems.

## Sources, conventions and review boundary

The [pinned French transcription](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-6-fr.tex)
and a separate English discovery witness are bound in the
[full comparison](ega-iii-6-2-10.json). It includes exact statement and proof
spans, hypotheses, target tags, finite arguments and retained limitations.
An existing independent AI review is reused after current raw-byte and
tag checks. This is not a fresh independent review, human approval, a
machine-checked formalization, or a new full collation of the printed source.

We use cohomological grading: $K^i=K_{-i}$. Thus EGA's *homologically bounded
below* complexes become **cohomologically bounded above**, not bounded below
and not necessarily bounded in both directions.

| EGA object | Content | Result |
|---|---|---|
| III.6.2.1 | Two hypercohomology spectral sequences | Bounded-below case covered; unrestricted historical regularity remains partial |
| III.6.2.2 | Čech computation | Arbitrary covers with bounded-below input, or finite affine covers with the stated acyclicity, are covered; simultaneous unrestricted features are not |
| III.6.2.3 | Quasi-coherence of direct-image cohomology | Stronger modern qcqs result, with the source-functor comparison |
| III.6.2.4 | Affine sections of the direct image | Derived, including the canonical comparison map |
| III.6.2.5 | Coherence of direct-image cohomology | Modern derived assertion covered; arbitrary unbounded old-functor comparison remains partial |
| III.6.2.6 | Exact sequences and homotopy compatibility | Restricted regimes covered; larger old-unbounded regimes remain partial |
| III.6.2.7 | Homological/cohomological reindexing | Convention checked; not counted |
| III.6.10.1 | One base-flat representing complex for the coefficient functors | Derived |
| III.6.10.2 | Bounds on that representative | Derived; the two-sided case uses finite ring global dimension |
| III.6.10.3 | Spectral sequence and quasi-isomorphism comparisons | Partial; boundedness, K-flatness and convergence cannot be omitted |
| III.6.10.4 | Long exact coefficient sequences | Derived under flatness |
| III.6.10.5 | Finite-free representative and arbitrary base change | Derived |
| III.6.10.6 | Finite-projective representative for a single sheaf | Derived; the subsequent converse question is not answered |

## A fixed finite-free representative: III.6.10.5

Let $A$ be Noetherian, let $f:X\to\operatorname{Spec}(A)$ be proper, and let
$P^\bullet$ be a bounded-above complex of coherent sheaves whose terms are
flat over $A$. Set $C=R\Gamma(X,P^\bullet)$.

1. Properness supplies qcqs geometry. A finite affine Čech cover has bounded
   Čech width, so $C$ is bounded above. The uniform bound in
   [08D5](https://stacks.math.columbia.edu/tag/08D5), coherent direct images
   [08E2](https://stacks.math.columbia.edu/tag/08E2), and truncation show that
   its cohomology modules are finite. Here the terms are quasi-coherent, so
   the finite-Čech comparison with the source functor applies; the unresolved
   arbitrary-term version of III.6.2.5 is not being used.
2. Over a Noetherian ring, this makes $C$ pseudo-coherent by
   [066E](https://stacks.math.columbia.edu/tag/066E). The explicit construction
   in [064U](https://stacks.math.columbia.edu/tag/064U) gives one bounded-above
   finite-free complex $L^\bullet$ representing $C$.
3. Relative flatness gives $A$-flat sections on each affine chart, by
   [01U4](https://stacks.math.columbia.edu/tag/01U4). Bounded-above flat
   complexes are K-flat by [064K](https://stacks.math.columbia.edu/tag/064K).
   Consequently ordinary base change of $P^\bullet$ computes the derived
   base change. The local criterion
   [0DJ8](https://stacks.math.columbia.edu/tag/0DJ8) and the comparison
   [0DJ9](https://stacks.math.columbia.edu/tag/0DJ9) apply to arbitrary
   $Y'\to\operatorname{Spec}(A)$.
4. The projection formula [08EU](https://stacks.math.columbia.edu/tag/08EU)
   identifies coefficient functors with tensoring the fixed representative.
   On an affine base change $\operatorname{Spec}(A')$, for a coefficient
   complex $Q'^\bullet$ this yields

   $$
   R\Gamma\bigl(X',P'^\bullet\otimes_{A'}Q'^\bullet\bigr)
   \simeq (L^\bullet\otimes_A A')\otimes_{A'}Q'^\bullet.
   $$

   Relative K-flatness justifies ordinary tensor on the geometric side;
   K-flatness of $L^\bullet$ justifies it on the module side. The comparison
   maps are canonical. Both routes in a coefficient-change square are
   induced by the same tensor map, so they commute; the local statements
   glue for nonaffine $Y'$. Exact flat tensor also preserves the connecting
   homomorphisms.

Neither flatness of $f$ nor perfection of $P^\bullet$ over $\mathcal O_X$
is assumed. “Finite free” refers to each term: $L^\bullet$ can still have
infinitely many nonzero terms to the left.

## Finite length and the exact degree range: III.6.10.6

Now suppose $P^\bullet=\mathcal F[0]$ for a coherent sheaf $\mathcal F$ flat
over $A$. The previous argument makes $C=R\Gamma(X,\mathcal F)$
pseudo-coherent. Choose $N\geq1$ from the uniform bound in
[08D5](https://stacks.math.columbia.edu/tag/08D5). For every $A$-module $M$,
the projection formula and relative flatness give

$$
C\otimes_A^{\mathbf L}M\simeq
R\Gamma\bigl(X,\mathcal F\otimes_A M\bigr).
$$

The right side has no negative cohomology because its input is a sheaf,
and no cohomology in degrees $\geq N$ by the uniform bound. Thus $C$ has
Tor amplitude $[0,N-1]$. The statement and proof of
[0658](https://stacks.math.columbia.edu/tag/0658) give a complex of finite
projective $A$-modules in exactly that interval: truncate a finite-free
resolution, then use Tor amplitude to show that the remaining finitely
presented end term is flat and hence projective.

Sheafification gives finite locally free terms. Reindexing gives the
homological interval $[-(N-1),0]$. Projective lifting
[064B](https://stacks.math.columbia.edu/tag/064B) and K-flatness preserve the
coefficient comparison and the base-change square. This completes the
forward assertion that was partial in the initial comparison.

The final paragraph of III.6.10.6 asks a **converse realization question**:
whether an appropriate projective complex can always arise from a projective
flat scheme and a locally free sheaf. No answer to that question is claimed
or included in the count.

## Why five comparisons remain partial

EGA's old Cartan–Eilenberg-totalized construction cannot simply be renamed
modern unbounded $Rf_*$. An identity in notation is not an identification of
the functors. In particular:

- [015J](https://stacks.math.columbia.edu/tag/015J) supplies the familiar
  spectral sequences in its bounded-below domain; it does not by itself
  settle the unrestricted regularity clause of III.6.2.1.
- Arbitrary-cover comparison [0FLH](https://stacks.math.columbia.edu/tag/0FLH)
  and the finite-cover unbounded comparison
  [08C2](https://stacks.math.columbia.edu/tag/08C2) have different hypotheses.
  Combining their names does not prove the case with both an infinite cover
  and unrestricted complex.
- Coherent cohomology of modern $Rf_*P$ does not alone identify EGA's old
  construction for unbounded, non-quasi-coherent terms. The same issue affects
  the larger exact-sequence regimes in III.6.2.6.
- A Künneth statement for bounded derived objects does not automatically
  establish the one-sided-unbounded spectral sequence and convergence in
  III.6.10.3. Nor does arbitrary termwise flatness imply K-flatness.

For the last warning, take $B=k[\epsilon]/(\epsilon^2)$ and the bi-infinite
complex with term $B$ in every degree and differential multiplication by
$\epsilon$. Its kernel and image are both $(\epsilon)$ in every degree,
so it is acyclic and termwise free. Tensoring it with $k=B/(\epsilon)$ gives
zero differentials and nonzero cohomology in every degree. The unrestricted
tensor-invariance inference therefore fails. This tests an interpretation;
it is not an admitted source erratum.

The remaining comparisons require precise totalization and convergence
arguments. They are **not established absences from Stacks**. Sections
III.6.3–6.9 have not all been compared by this checkpoint, and no global EGA
completion percentage follows from its counts.
