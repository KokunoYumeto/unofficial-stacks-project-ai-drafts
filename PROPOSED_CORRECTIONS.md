# Possible fixes to the inherited Stacks text

These are AI-reviewed suggestions, not expert-approved corrections or officially
adopted Stacks errata. Each argument below is intended to be checked directly.
Automated replay establishes which bytes would change; it does not establish
that the mathematics is correct. Expert corrections are welcome, without being
a prerequisite for making these drafts available.

This page is **separate from additions and expository expansions**. Translation
choices are a third category and are not, by themselves, defects in the English
source. [Possible new additions](POSSIBLE_ADDITIONS.md) are listed separately, or
[browse all recorded integrated differences](CHANGES_FROM_UPSTREAM.md).

**Use a correction without adopting this project:**
[download one small patch](possible-fixes/README.md), read its explanation below,
and run `git apply --check` against your checkout. Each patch touches only
inherited official source. The three related Ext proposals also have a combined
patch so they can be considered together. The patch index states its exact
coverage and pinned baseline; clean application is not a mathematical endorsement.

## Coverage and status

This initial readable selection contains **13 proposed correction units**, plus
**three historical findings that need no new edit**. It is not an exhaustive
review of Stacks or of the translation findings. Eleven proposals were recovered
while reviewing this project's history; two came from French translation work.
The fuller recorded comparison linked above covers earlier integrated batches.

For the much larger already-integrated collection, use the separate
[corrections-only combined and chapter patches](upstream-corrections/README.md).
That export accounts for all 1,304 historical IDs: 1,302 effective textual units,
one superseded correction and one excluded fork-specific tag allocation. These
13 additional proposals are not silently mixed into that export.

All original passages below refer to the fixed official Stacks revision
[`a04446e57ec1fbc252a871afcec7752fb2807b14`](https://github.com/stacks/stacks-project/commit/a04446e57ec1fbc252a871afcec7752fb2807b14),
not necessarily today's upstream text. The cumulative draft checked here was
[`0e40e317e02e7b05437fcc7c7f13659e140e128f`](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/commit/0e40e317e02e7b05437fcc7c7f13659e140e128f).

“Proposed” means the correction has **not been composed into that checked draft**.
The two limit-preservation items have reserved draft registry IDs, but their
admission and integration are not claimed. The history-recovery identifiers are
stable identifiers within this review, not official Stacks tags or allocated
registry IDs. [Exact operations and source identities](ai-integrated/review-notes/2026-09-19-proposed-corrections.json)
are supporting evidence after, not instead of, the arguments.

## Mathematical and proof corrections

### 1. The map on Ext goes in the opposite direction

**Proposed.** Review ID `H100B-SOURCE-006`.
[Original display and proof](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17575-L17604),
`lemma-ext-welldefined`, lines 17587–17589 and 17601–17602.

The lemma chooses a chain map $\alpha:F_\bullet\to G_\bullet$. It prints

```tex
H^i(\Hom_R(F_{\bullet}, N))
\longrightarrow
H^i(\Hom_R(G_{\bullet}, N))
```

The proposed replacement is

```tex
H^i(\Hom_R(G_{\bullet}, N))
\longrightarrow
H^i(\Hom_R(F_{\bullet}, N))
```

**Why:** a homomorphism $u:G_j\to N$ gives $u\circ\alpha_j:F_j\to N$.
Thus applying $\operatorname{Hom}_R(-,N)$ reverses the arrow, and taking
cohomology keeps that reversed direction. The proof's displayed Hom-complex
arrow needs the same reversal. This does not alter the resolution-independence
theorem; it corrects the types of its induced maps.

### 2. The identity acts on cohomology, not homology

**Proposed.** Review ID `H100B-SOURCE-007`.
[Original](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17584-L17594),
same lemma, line 17594.

Original: `$H_i(\alpha)$`. Replacement: `$H^i(\alpha)$`.

**Why:** this sentence refers to the maps just defined on the cohomology of
the Hom cochain complex, denoted $H^i(\alpha)$. A homological subscript denotes
a different construction on the original chain complexes.

### 3. The inverse-map argument must reverse composition too

**Proposed.** Review ID `H100B-SOURCE-009`.
[Original](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17607-L17619),
same lemma, lines 17615–17617. Read with correction 1.

Original:

```tex
H^i(\alpha \circ \beta)$. By the above the
map $H^i(\alpha \circ \beta)$ is the {\it same}
as the map $H^i(\text{id}_{G_{\bullet}}) = \text{id}$.
```

Replacement:

```tex
H^i(\beta \circ \alpha)$. By the above the
map $H^i(\beta \circ \alpha)$ is the {\it same}
as the map $H^i(\text{id}_{F_{\bullet}}) = \text{id}$.
```

**Why:** write $\alpha^*$ for precomposition. Then
$\alpha^*\circ\beta^*=(\beta\circ\alpha)^*$ acts on
$H^i(\operatorname{Hom}_R(F_\bullet,N))$. The chain map
$\beta\circ\alpha:F_\bullet\to F_\bullet$ lifts the identity on $M_1$,
so the comparison-of-resolutions lemma makes it homotopic to $\mathrm{id}_F$.
The existing next sentence handles the other composite in the same way.

### 4. A split exact sequence has the two different endpoint modules

**Proposed.** Review ID `H100B-SOURCE-011`; two occurrences of the same typo.
[PID example](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13063-L13075),
line 13073, and
[local-ring proof](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13146-L13154),
line 13152.

Original: `$M \cong M' \oplus M'$`.
Replacement: `$M \cong M' \oplus M''$`.

**Why:** each passage has just written $0\to M'\to M\to M''\to0$ with
finite free endpoints. A splitting identifies $M$ with the kernel $M'$ plus
the quotient $M''$, not with two copies of the kernel. This also gives the
rank equality used on the preceding line. The second locus was the mined
finding; source comparison exposed the same typo in the first locus.

### 5. The induction proves injectivity at the next index

**Proposed.** Review ID `H100B-SOURCE-016`.
[Original argument](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27688-L27704),
line 27704.

Original: `hence $\psi_i$ is injective`.
Replacement: `hence $\psi_{i + 1}$ is injective`.

**Why:** injectivity at $i$ is the induction hypothesis. The displayed quotient
with $i+1$ variables and equations is then shown to be a field. Its surjective
unital map is $\psi_{i+1}$; a unital map from a field into a field is injective.
The written conclusion should state the newly proved induction step.

### 6. A chain map uses the differential leaving its target degree

**Proposed.** Review ID `H100B-SOURCE-017`.
[Original definition](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17454-L17468),
line 17466.

Original:

```tex
\alpha_{i-1} \circ d_{F, i} = d_{G, i-1} \circ \alpha_i
```

Replacement:

```tex
\alpha_{i-1} \circ d_{F, i} = d_{G, i} \circ \alpha_i
```

**Why:** $\alpha_i$ lands in $G_i$, whose outgoing differential is
$d_{G,i}:G_i\to G_{i-1}$. The printed $d_{G,i-1}$ has domain $G_{i-1}$,
so it cannot be composed with $\alpha_i$ as written. Both corrected sides
are maps $F_i\to G_{i-1}$.

### 7. The fibre functor must use the point fixed in this direction of the proof

**Proposed; R50 candidate in progress, not yet admitted or integrated.**
Reserved draft ID `MC-STK-ERR-1574`; producer alias
`SPACES-SRC-00178-UNBOUND-Y`.
[Original proof](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-limits.tex#L168-L178),
`lemma-characterize-relative-limit-preserving`, line 178.

Original: `\colim_i F_y(T'_i)`.
Replacement: `\colim_i F_{y_T}(T'_i)`.

**Why:** this direction begins by fixing $y_T\in G(T)$ and aims to prove
that $F_{y_T}$ is limit preserving. The subscript $y$ belonged to the separate
forward implication. The conclusion here must use the fibre functor based
on the chosen $y_T$. This is a correction to this particular occurrence,
not certification of every nearby sentence.

### 8. The fibre-product comparison uses finite limits, not only products

**Proposed; R50 candidate in progress, not yet admitted or integrated.**
Reserved draft ID `MC-STK-ERR-1575`; producer alias
`SPACES-SRC-00269-PRODUCTS-VS-LIMITS`.
[Original proof](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-limits.tex#L252-L269),
`lemma-fibre-product-locally-finite-presentation`, line 269.

Original: `filtered colimits commute with finite products`.
Replacement: `filtered colimits commute with finite limits`.

**Why:** the preceding display compares a filtered colimit of
$F(T_i)\times_{G(T_i)}H(T_i)$ with a fibre product of colimits. A fibre product
over a varying base is a finite limit, not merely a product. In sets, a pair
whose images agree in the colimit has representatives whose images agree
at a common later stage. Likewise, equality of two such pairs occurs at
a common later stage. This proves the displayed map is bijective and explains
the stronger fact actually being used. The producer also supplied an SGA 4
parallel; this entry's argument does not rely on an unverified quotation.

## Grammar and typography only

These five proposals do not change mathematical claims. Their review IDs are
listed so they cannot be confused with five new mathematical results.

| Review ID | Pinned source | Original | Smallest replacement | Reason |
|---|---|---|---|---|
| `H100B-SOURCE-013` | [homology.tex:3962](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/homology.tex#L3958-L3964) | `in stead of` | `instead of` | Single-word spelling in the bigraded-shift paragraph. |
| `H100B-SOURCE-014` | [algebra.tex:26495](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26484-L26498) | `there exist a commutative diagram` | `there exists a commutative diagram` | The noun phrase is singular. |
| `H100B-SOURCE-015` | [algebra.tex:27084](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27079-L27086) | `have to property that` | `have the property that` | The maps have a property; the article is mistyped. |
| `H100B-SOURCE-018` | [algebra.tex:17562](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17560-L17563) | `in stead` | `instead` | Single-word spelling; preserve the following line break and “of”. |
| `H100B-SOURCE-019` | [algebra.tex:17610](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17607-L17612) | `be a map inducing` | `to be a map inducing` | Complete the construction “Choose beta to be a map”. |

## Historical findings that require no new edit

These are deliberately outside the proposed-change count.

### The resolution cokernel is already correct in the pinned source

Review ID `H100B-SOURCE-008`.
[Pinned passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17609-L17612).
An older excerpt had assigned the wrong resolution cokernel to $M_1$.
Both the pinned authority and the checked draft already say
`M_1 = \Coker(d_{F, 1})`, as required because $F$ resolves $M_1$.
**No edit; not a correction made by this review.**

### The negative-Ext truncation inequality was already corrected

Review ID `H100B-SOURCE-010`; existing draft ID `MC-STK-ERR-0875`, R20.
[Original](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L8733-L8742)
said `$L^i = 0$ for $i < a$`; the
[checked draft](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/0e40e317e02e7b05437fcc7c7f13659e140e128f/derived.tex#L8789-L8798)
already says `$L^i = 0$ for $i > a$`.
**Why:** the immediately preceding truncation is $\tau_{\leq a}L$,
which vanishes above $a$. Preserve that correction; do not apply it twice.

### The unfinished unit sentence was already completed

Review ID `H100B-SOURCE-012`; existing draft ID `MC-STK-ERR-0771`, R16.
[Original](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/homology.tex#L4073-L4083):
`As unit we take`.
The [checked draft](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/0e40e317e02e7b05437fcc7c7f13659e140e128f/homology.tex#L4156-L4166)
already completes it as
`As unit we take the object $\mathbf{1}$ described above.`
The proof then identifies this object with $F$ in degree zero.
**No new edit:** the historical suggestion to delete the fragment is superseded
by this already-integrated completion.

## Qualifications and continuation

These proposals were compared with the admitted correction metadata available
at the checked commit. Pending intake elsewhere may still identify a duplicate;
such a finding will be linked rather than counted twice. Neither publication
of this page nor a reserved ID means a proposed source edit has been integrated.
No upstream report or issue has been sent as part of this review.

Future additions to this log will preserve withdrawn, rejected, duplicated and
superseded suggestions outside the active proposal list, with the reason for
their disposition. The goal is a useful, inspectable record—not a claim that
every AI suggestion is right.
