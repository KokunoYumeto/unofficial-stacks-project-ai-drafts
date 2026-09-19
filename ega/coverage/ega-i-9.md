# EGA I §9: quasi-coherent sheaves and scheme-theoretic images

The coverage-first comparison supports **42 of 44 numbered objects using
existing Stacks results**. Two passages need a qualification about *closed*
subschemes; they are not two missing Stacks theorems. We therefore add a
comparison, not another copy of these results to the root chapters.

The 42 comprise 38 theorem/proposition/lemma/corollary objects, two definitions
and two substantive remarks. Three other numbered contextual passages are read
but excluded from that count. This is one section of EGA I, **not a percentage
of all EGA** and not a claim that the overall integration is complete.

## Sources and what was checked

The French witness is the [pinned repository transcription of §9](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-9-fr.tex).
The [separately pinned English discovery witness](https://github.com/KokunoYumeto/ega-en/blob/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-9.tex)
was used for comparison, not as a replacement for the French. This pass does not
claim a new collation against printed page images.

A preserved independent AI review compared all 44 statement bodies, their
hypotheses, and the required Stacks proof passages. On 19 September 2026 the
integration task read that review and revalidated its source identities and
target bindings against draft commit `6402f0425425fb5d3bd1c2f206e3b4bab1e28e47`.
All ten bound target files were unchanged, so the mathematical review was reused,
not repeated or represented as a new independent review. The replay checks 44
source IDs in each language, 54 target labels/tags and 148 source/target spans.
These mechanical checks preserve the evidence; they are not a proof of the
mathematics or expert approval.

The [complete 44-row crosswalk](ega-i-9.json) gives each source locator,
statement scope, target links, finite dependency chain, reasoning and residual.
An *exact* match has the corresponding content; a *stronger* result implies it
under weaker assumptions; a *derived* match includes a stated finite argument
from existing results. A matching citation or keyword alone is not a match.

## The useful correspondences

| EGA range | Content | Outcome |
|---|---|---|
| I.9.1.1–I.9.1.13, excluding contextual I.9.1.8 | Tensor products, internal Hom, external products and pullback | 12 correspondences |
| I.9.2.1–I.9.2.2 | Direct images of quasi-coherent sheaves | 2 correspondences |
| I.9.3.1–I.9.3.5 | Extending sections after multiplication; annihilation by powers of an ideal | 5 correspondences |
| I.9.4.2–I.9.4.10 | Extending finite-type submodules and exhausting quasi-coherent sheaves | 9 correspondences |
| I.9.5.1–I.9.5.11 | Scheme-theoretic images, closure and epimorphisms | 9 correspondences; 2 literal-scope qualifications |
| I.9.6.1 and I.9.6.3–I.9.6.6 | Modules over quasi-coherent algebras and finite-type subalgebras | 5 correspondences |

### Tensor products and pullback: arbitrary modules remain arbitrary

[01CE](https://stacks.math.columbia.edu/tag/01CE) treats tensor products of
quasi-coherent modules. The finite-type and coherence conclusions have their
own finiteness assumptions; those assumptions are not imposed on the general
tensor statement. Internal Hom in [01CQ](https://stacks.math.columbia.edu/tag/01CQ)
does require finite presentation of its first argument, as in the source.

The external product is the tensor product of the two projection pullbacks.
On an affine fibre product with coordinate ring $D=B\otimes_A C$, its module is

$$
(D\otimes_B M)\otimes_D(D\otimes_C N)\cong M\otimes_A N.
$$

Balanced pure-tensor maps give this isomorphism without a flatness hypothesis.
The affine sheaf correspondences are
[01I8](https://stacks.math.columbia.edu/tag/01I8) and
[01I9](https://stacks.math.columbia.edu/tag/01I9).
Associativity, base-change transitivity and compatibility with pullback then
follow from the tensor and pullback constructions
([01CD](https://stacks.math.columbia.edu/tag/01CD),
[0097](https://stacks.math.columbia.edu/tag/0097)).

The support equality in I.9.1.13 is different: it retains the finite-type
hypothesis. At a product point, Nakayama's lemma turns nonzero finite stalk
modules into nonzero residue vector spaces, whose tensor product over the
residue field is nonzero. Dropping finite type would discard the argument.

### Direct images and extension of sections

The finite affine-cover and overlap hypotheses of I.9.2.1 establish exactly
the quasi-compact and quasi-separated conditions used in
[01LC](https://stacks.math.columbia.edu/tag/01LC). The argument applies to
arbitrary quasi-coherent sheaves, not only finitely presented ones.

For I.9.3.1–I.9.3.3, the section-localization results
[01PW](https://stacks.math.columbia.edu/tag/01PW) and
[01P7](https://stacks.math.columbia.edu/tag/01P7) give both conclusions:
a section vanishing on the nonvanishing locus is killed by a power, and a
section on that locus extends after multiplication by a power. Negative
integer twists are handled by using the corresponding invertible tensor
power; degree zero is ordinary function localization.

For a coherent sheaf supported on the vanishing set of an ideal, the
annihilation result [01Y9](https://stacks.math.columbia.edu/tag/01Y9) supplies
one positive power annihilating it. The closed-immersion module equivalence
[01QY](https://stacks.math.columbia.edu/tag/01QY) then identifies the canonical
map to the pushforward of its restriction—not merely some unspecified
isomorphic sheaf on the closed subscheme.

### Extending finite-type submodules without adding global quasi-compactness

On a quasi-compact, quasi-separated scheme, the relevant extension and
directed-union results are already
[01PE](https://stacks.math.columbia.edu/tag/01PE),
[01PF](https://stacks.math.columbia.edu/tag/01PF) and
[01PG](https://stacks.math.columbia.edu/tag/01PG).
Some of EGA's other alternatives are not globally quasi-compact, however.

I.9.4.6 supplies a well-ordered affine cover $(V_\alpha)$ whose successive
overlaps are quasi-compact, together with a quasi-compact open immersion
$U\to X$. Starting with the prescribed finite-type submodule on $U$, extend
over one $V_\alpha$ at a time. Its overlap with the constructed domain is the
union of $V_\alpha\cap U$ and the stipulated earlier-chart overlap; both are
quasi-compact. The affine extension lemma applies there. Glue the two compatible
submodules using [00AM](https://stacks.math.columbia.edu/tag/00AM).

At a limit ordinal, glue on the increasing union. Quasi-coherence and finite
type are local, so they persist; there is no requirement of a uniform global
number of generators. If the affine cover has order type $\kappa$, perform
the construction through stage $\kappa$, including the last chart when one
exists. This closes the source argument without silently assuming $X$ is
quasi-compact.

For a topologically locally Noetherian scheme, every open subset of an affine
chart is quasi-compact, so these overlap conditions hold. This is a statement
about the topology; it does **not** assert that the coordinate rings are
Noetherian. Extending cyclic submodules from affine charts and taking finite
sums gives the directed-union conclusion of I.9.4.9 in that generality.

### Closed images and epimorphisms: keep the category explicit

The scheme-theoretic image is supplied by
[01R6](https://stacks.math.columbia.edu/tag/01R6) and
[01R7](https://stacks.math.columbia.edu/tag/01R7).
Where EGA assumes only that $f_*\mathcal O_X$ is quasi-coherent, the kernel
construction suffices. The comparison does not replace that hypothesis by
quasi-compactness of $f$.

In I.9.5.6, two maps to a **separated** test target have a closed equalizer
([01KM](https://stacks.math.columbia.edu/tag/01KM)). If they agree after $f$
and the whole target of $f$ is its scheme-theoretic image, this equalizer must
be the whole target. This does not prove cancellation for arbitrary
nonseparated test schemes.

The converse in I.9.5.7 can also be derived from existing material. If
$\mathcal I$ is the ideal of the closed image, zero and inclusion
$\mathcal I\to\mathcal O_Y$ induce two algebra maps
$\operatorname{Sym}(\mathcal I)\to\mathcal O_Y$. By relative Spec
([01LU](https://stacks.math.columbia.edu/tag/01LU)), they give two sections
of $T=\operatorname{Spec}_Y\operatorname{Sym}(\mathcal I)\to Y$.
They agree after $f$, since $f$ kills $\mathcal I$. The affine morphism
$T\to Y$ is separated, so $T$ remains a permitted test object when $Y$ is
separated over the source's base. Epimorphic cancellation makes the sections
equal; comparing their degree-one maps forces $\mathcal I=0$.
No finite-generation hypothesis on $\mathcal I$ is needed.

### Quasi-coherent algebras are not necessarily finite as modules

For a quasi-coherent algebra $\mathcal B$, I.9.6.1 compares a
$\mathcal B$-module on the ringed space $(X,\mathcal B)$ with its underlying
$\mathcal O_X$-module. Arbitrary free presentations and the affine equivalence
[01IB](https://stacks.math.columbia.edu/tag/01IB) give both directions.
The ringed space $(X,\mathcal B)$ is not being identified with relative Spec.

On a Noetherian affine chart, a finite-type algebra $B$ is Noetherian even
when it is not finite as a module over the base ring. This proves the
ring-sheaf coherence assertion in I.9.6.3; it does not prove coherence of
$\mathcal B$ as an $\mathcal O_X$-module. Finally, finite-type submodules
generate finite-type subalgebras through the image of their symmetric algebras.
The established module exhaustion, or the direct algebra result
[05JT](https://stacks.math.columbia.edu/tag/05JT), gives I.9.6.6.

## Two qualifications, not two missing Stacks results

### I.9.5.1: a least locally closed image need not exist

The two pinned transcriptions omit “closed” from the minimum requested in
this statement, though the subsequent definition expressly concerns closed
images. Read literally over all locally closed subschemes, existence fails.

For $\operatorname{Spec}\mathbb Q\to\operatorname{Spec}\mathbb Z$, the
pushforward of the structure sheaf is quasi-coherent, but the map factors
through every nonempty open subset. A locally closed subset containing the
generic point is open. Every nonempty open contains some closed prime that
can be removed while keeping a nonempty open. Therefore there is no least
locally closed factorization target.

### I.9.5.2: the kernel-defined image is minimal among closed subschemes

For $D(2)\to\operatorname{Spec}\mathbb Z$, the kernel of the structure-sheaf
map is zero, so its closed image is all of $\operatorname{Spec}\mathbb Z$.
It nevertheless factors through the smaller open $D(2)$. Thus the
kernel-defined closed image cannot be minimal among *all* locally closed
subschemes.

Both passages have fully covered **closed-subscheme readings**. Their
unqualified transcription readings remain recorded as partial matches,
not newly admitted source errata. Resolving what the printed original and
its historical conventions intended is separate source-collation work.
Neither issue justifies writing a duplicate image theorem into Stacks.

## Next work

This comparison removes these 42 objects from the unassessed coverage queue
and preserves the two exact qualifications. It adds no root-source theorem,
assigns no new official tag, changes no French or English source witness,
and makes no claim to have completed EGA I–IV or the other integration strands.
The remaining preserved coverage batches and genuine candidate gaps are the
next work; the completed source inventory need not be restarted.
