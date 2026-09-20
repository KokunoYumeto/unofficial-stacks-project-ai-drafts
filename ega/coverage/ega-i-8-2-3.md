# EGA I §§8.2–8.3: a scheme described by its local rings

This comparison accounts for ten numbered objects: **eight are derived from
existing Stacks results**, and two have the same substantive coverage once
empty-set conventions are stated correctly. No new root-chapter theorem is
claimed. In particular, “Chevalley schemes” here concerns reconstructing a
scheme from local subrings of a field—not Chevalley's constructible-image
theorem.

The sources are the [pinned French transcription](https://github.com/KokunoYumeto/ega-fr/blob/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-8-fr.tex#L138-L410)
and [separate English discovery edition](https://github.com/KokunoYumeto/ega-en/blob/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-8.tex#L98-L256).
The [full crosswalk](ega-i-8-2-3.json) includes exact source and target spans,
hashes, hypotheses, derivations, and the preserved independent AI review.
The integration task reuses that review after checking that its bound
source and target bytes still match. This is not a fresh independent review,
human approval, machine-checked proof, or a claim of complete EGA coverage.

## What is covered?

| EGA object | Mathematical content | Disposition |
|---|---|---|
| I.8.2.1 | Regular functions are intersections of embedded stalks | Covered for nonempty opens; assign zero to the empty open |
| I.8.2.2 | Separatedness is uniqueness of centres of allied local rings | Derived without an extra quasi-separatedness hypothesis |
| I.8.2.3 | Specialization corresponds to containment of local rings | Derived, with the direction of containment explicit |
| I.8.2.4 | Distinct points have distinct embedded stalks | Derived |
| I.8.2.5 | Regularity domains generate the topology | Derived as a subbasis, assuming topological Noetherianity |
| I.8.2.6 | The embedded stalk family recovers topology and structure sheaf | Derived, including restriction maps |
| I.8.2.7 | A dominant morphism determines centres compatibly | Derived with the specified function-field embedding |
| I.8.2.8 | A separated local immersion from an irreducible scheme is an immersion | Derived without discarding nilpotents |
| I.8.3.1 | Noetherian integral separated schemes satisfy Chevalley's axioms | Derived |
| I.8.3.2 | Reconstruct a scheme from those local-ring axioms | Derived with a nonempty family and the empty-open convention explicit |

Throughout, EGA's “integral prescheme” is a modern integral scheme. Its
“integral scheme” also imposes separatedness. All local rings are **specified
subrings of a fixed field** $K$, not abstract isomorphism classes.
Two such local rings are *allied* if a local subring of $K$ dominates both.

## Sections, specializations, and the topology

The function field and embedded stalks are supplied by
[01RV](https://stacks.math.columbia.edu/tag/01RV). For a nonempty open $U$,
[0HD5](https://stacks.math.columbia.edu/tag/0HD5) gives

$$
\Gamma(U,\mathcal O_X)=\bigcap_{x\in U}\mathcal O_{X,x}\subset K.
$$

On the empty open the section ring is the zero ring; it is not the empty
intersection inside $K$, which would be $K$. This is the first literal
source-convention qualification.

For an integral separated scheme, [02NF](https://stacks.math.columbia.edu/tag/02NF)
gives the reverse implication in

$$
x\in\overline{\{y\}}\quad\Longleftrightarrow\quad
\mathcal O_{X,x}\subset\mathcal O_{X,y}.
$$

The forward implication is ordinary localization on an affine neighbourhood
of $x$. In particular the generic point has the largest stalk, $K$.
Equal embedded stalks give equal point closures and hence equal points by
the $T_0$ property of schemes
([01IS](https://stacks.math.columbia.edu/tag/01IS)).

If the underlying space is Noetherian, every closed subset is a finite union
of irreducible closed subsets, each with a generic point. For
$x\notin\overline{\{y\}}$, choose $f\in\mathcal O_{X,x}\setminus\mathcal O_{X,y}$.
Its open regularity domain contains $x$ and misses every specialization of
$y$. Thus regularity domains form a subbasis. This uses Noetherian
**topology**, not Noetherian coordinate rings.

The same argument recovers closed sets as finite unions of sets
$\{y:\mathcal O_{X,y}\subset\mathcal O_{X,x}\}$.
Intersections of stalks recover sections on nonempty opens; inclusions give
their restriction maps. Adding the zero section ring on the empty open
recovers the whole ringed space, not just its specialization order.

## Separatedness from uniqueness of centres

If $X$ is separated, a common dominating local ring $Q\subset K$ gives two
maps $\operatorname{Spec}Q\to X$ agreeing at the generic point. Their equalizer
is closed by [01KM](https://stacks.math.columbia.edu/tag/01KM).
Its ideal vanishes in the fraction field of the domain $Q$, hence is zero.
The two centres are therefore the same.

Conversely, suppose allied stalks always have the same centre. For nonempty
affine opens $U=\operatorname{Spec}A$ and $V=\operatorname{Spec}B$, let
$C\subset K$ be the ring generated by $A$ and $B$. Each $C_{\mathfrak r}$
dominates the two localizations at the contracted primes. The hypothesis
identifies their centres and hence their stalks; that common stalk is
$C_{\mathfrak r}$. This last equality follows because the common stalk
contains $C$, is local inside $C_{\mathfrak r}$, and inverts every element of
$C\setminus\mathfrak r$.

Consequently $W=U\cap V$ has exactly the points and stalks of
$\operatorname{Spec}C$. The intersection formula gives
$\Gamma(W,\mathcal O_X)=C$; the elementary domain identity
$C=\bigcap_{\mathfrak m}C_{\mathfrak m}$ occurs in the proof of
[030B](https://stacks.math.columbia.edu/tag/030B), without requiring normality
for that identity. The affine mapping property constructs
$W\to\operatorname{Spec}C$. For a closed subset
$F=W\cap V_U(\mathfrak a)$, its image is $V_C(\mathfrak a C)$.
The map is therefore a homeomorphism with isomorphic stalks, hence an
isomorphism of schemes.

Finally $A\otimes_{\mathbf Z}B\to C$ is surjective. The affine-overlap
criterion [01KP](https://stacks.math.columbia.edu/tag/01KP) proves
separatedness. No quasi-separatedness assumption was inserted to invoke
a valuative criterion. The displayed closed-trace expression also makes
explicit the correction already noted in the English source's footnote.

For a dominant map between integral schemes with separated target, the
same equalizer argument proves uniqueness of the target centre dominated
by a given source stalk. The embedding $K(Y)\hookrightarrow K(X)$ is the
one induced by the morphism, as in
[0CC1](https://stacks.math.columbia.edu/tag/0CC1).

## Local immersions: put the nilpotents back

For I.8.2.8, let $f:X\to Y$ be separated, $X$ irreducible, and $f$ locally
an immersion. Reduce and factor through the reduced closed subscheme
$Z\subset Y$ supported on $\overline{f(X)}$
([01J3](https://stacks.math.columbia.edu/tag/01J3)).
This is a topological closure with its reduced structure, not an invocation
of a scheme-theoretic-image theorem.

Each nonempty reduced local closed-immersion piece contains the generic
point and has both dense and closed image in its target open of $Z$.
It is an isomorphism there. Over affine target opens, separatedness makes
the reduced source integral and separated. Points in the same fibre would
then have equal embedded stalks; the preceding uniqueness makes them equal.
Thus the reduced map is an open immersion into $Z$, so the original map is
a homeomorphism onto a locally closed subset.

Now return to the original, possibly nonreduced $X$. Restrict the target so
the image is closed. The original local-immersion assumption gives
surjective stalk maps, including all nilpotent information. The
closed-pushforward stalk formula gives a surjection of structure sheaves.
The closed-immersion criterion
[01LD](https://stacks.math.columbia.edu/tag/01LD) proves the original map
is an immersion. If $f$ was locally an isomorphism, its image is open and
the result is an open immersion. Merely proving a statement about
$X_{\mathrm{red}}$ would not suffice.

## Reconstructing the Chevalley scheme

Write $L(A)=\{A_{\mathfrak p}:\mathfrak p\in\operatorname{Spec}A\}$ as
embedded local subrings of $K$. The data are a **nonempty** family
$\mathcal X$ of local subrings with fraction field $K$, together with a
finite cover $\mathcal X=\bigcup_i L(A_i)$ by Noetherian subrings.
The generated overlap ring $A_{ij}\subset K$ is finite type over $A_i$;
allied members of $\mathcal X$ must coincide.

These conditions hold for an integral separated Noetherian scheme:
take a finite affine cover, use separated affine overlaps for $A_{ij}$,
and apply uniqueness of centres. Conversely they suffice to glue that
scheme without assuming its existence:

1. For $C=A_{ij}$ and $\mathfrak r\in\operatorname{Spec}C$, contraction and
   the allied-ring condition give
   $C_{\mathfrak r}=(A_i)_{\mathfrak p}=(A_j)_{\mathfrak q}$.
2. Choose finitely many generators of $C$ over $A_i$. At $\mathfrak r$
   they all lie in $(A_i)_{\mathfrak p}$, so one $s\in A_i\setminus\mathfrak p$
   clears their denominators. Hence $C_s=(A_i)_s$. These standard opens
   cover $\operatorname{Spec}C$. Two primes contracting to the same
   $\mathfrak p$ have the same local ring and maximal-ideal contraction,
   hence coincide. Thus the overlap maps are open immersions.
3. Their overlaps are exactly $L(A_i)\cap L(A_j)$. The maps are identities
   on the embedded local rings; on triple intersections the identities
   agree. Apply [01JB](https://stacks.math.columbia.edu/tag/01JB) and
   [01JC](https://stacks.math.columbia.edu/tag/01JC) to glue.
4. The finite Noetherian affine cover proves Noetherianity. All generic
   points are the same ring $K$, so the glued scheme is integral.
   The surjections $A_i\otimes_{\mathbf Z}A_j\to A_{ij}$ prove separatedness.
   The reconstruction above then supplies exactly the prescribed topology,
   sections, and restrictions.

This fills in the construction that EGA leaves to the reader. Finite
denominator clearing is essential: pointwise equality of local rings
alone would not establish the overlap open immersions.

The second literal convention qualification is nonemptiness. An empty
family with an empty finite chart cover satisfies the three displayed
axioms vacuously, but cannot produce an integral scheme. We state
nonemptiness explicitly, and again set sections on the empty open to zero.
These edge cases remain visible in the crosswalk rather than being
counted as unqualified exact matches.

## What this changes

Two previously partial proof comparisons—I.8.2.2 and I.8.2.8—are closed by
the full-generality arguments above. The reconstruction in I.8.3.2 is also
supplied with its conventions explicit. All ten items now have a concrete
disposition; none requires a duplicate root theorem on this evidence.
No source transcription, admitted errata registry, official Stacks tag,
or historical review was changed.
