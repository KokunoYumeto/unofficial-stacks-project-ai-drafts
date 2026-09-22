# Categories: proposed corrections and clarifications

83 proposed changes: 51 copyedits, 11 clarifications and 21 source corrections. These are not 83 new mathematical errors or theorems. The complete intake review retains all 165 reports, duplicates, rejected claims and adverse evidence.

Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.

## MC-STK-ERR-1605 — CATEGORIES-RECON-001 (notation_clarification)

Line 379 defines j(phi) to be the unique morphism whose F-image is phi'. The right vertical map is therefore F(j(phi)); explicitly grouping the evaluation removes the misleading composition sign between a functor and an already evaluated morphism.

Official source line 385:

```tex
F\circ j(\phi)
```

Replace with:

```tex
F(j(\phi))
```

## MC-STK-ERR-1606 — CATEGORIES-RECON-003 (copyedit)

The same morphism is denoted by the Greek mathematical symbol in the next sentence and in both defining equations. Restore its consistent typesetting.

Official source line 852:

```tex
uniqueness of delta.
```

Replace with:

```tex
uniqueness of $\delta$.
```

## MC-STK-ERR-1607 — CATEGORIES-RECON-004 (clarification)

Specify the structural maps of the universal object. The displayed square uses identity projections, and its universal property forces alpha=beta. An arbitrary abstract isomorphism X times_Y X congruent X would not suffice: an infinite countable set maps noninjectively to a singleton while its square is abstractly isomorphic to itself. The dual assertion follows in the opposite category. This wording does not assume fibre products or pushouts exist beforehand.

Official source line 1225:

```tex
\item $f$ is a monomorphism if and only if $X$ is the fibre
```

Replace with:

```tex
\item $f$ is a monomorphism if and only if $X$, with both projections
```

Official source line 1226:

```tex
product $X \times_Y X$, and
```

Replace with:

```tex
equal to $\text{id}_X$, is a fibre product of $X$ with itself over $Y$, and
```

Official source line 1227:

```tex
\item $f$ is an epimorphism if and only if $Y$ is the pushout
```

Replace with:

```tex
\item $f$ is an epimorphism if and only if $Y$, with both coprojections
```

Official source line 1228:

```tex
$Y \amalg_X Y$.
```

Replace with:

```tex
equal to $\text{id}_Y$, is a pushout of $Y$ with itself over $X$.
```

Official source line 1247:

```tex
Suppose that $X \times_Y X \cong X $. The diagram
```

Replace with:

```tex
Suppose that $X$, with both projections equal to $\text{id}_X$, is
a fibre product of $X$ with itself over $Y$. The diagram
```

Official source line 1262:

```tex
The proof is exactly the same for the second point, but with the
```

Replace with:

```tex
The second assertion follows by applying the first assertion to the
```

Official source line 1263:

```tex
pushout $Y\amalg_X Y = Y$.
```

Replace with:

```tex
opposite category.
```

## MC-STK-ERR-1608 — CATEGORIES-RECON-005 (copyedit)

The common morphism W to X equips W with an object structure in the slice category. It does not define an object of W.

Official source line 1692:

```tex
object of $W$ in $\mathcal{C}/X$
```

Replace with:

```tex
object of $\mathcal{C}/X$ on $W$
```

## MC-STK-ERR-1609 — CATEGORIES-RECON-006 (copyedit)

The subject is the single sequence of morphisms. By contrast, the neighboring clause at 1731 quantifies an object AND a morphism, a coordinated subject for which plural exist is defensible; leave that clause unchanged.

Official source line 1734:

```tex
there exist a sequence
```

Replace with:

```tex
there exists a sequence
```

## MC-STK-ERR-1610 — CATEGORIES-RECON-007 (source_correction)

A path in the comma category must connect the two specified objects (x,H(x)->y) and (x',H(x')->y), not arbitrary morphisms with those underlying x-values. The dual cofinal definition explicitly fixes endpoints at 1741, and 1806 says this definition is its dual. Without the requirement, the functor from a terminal category to a one-object category of a nontrivial group would satisfy the printed weakened condition (choose n=0 and ignore the given arrows), while its relevant comma category is a disconnected discrete set of group elements.

Official source line 1791:

```tex
in $\mathcal{I}$ and morphisms $H(x_i) \to y$ in $\mathcal{J}$
```

Replace with:

```tex
in $\mathcal{I}$ and morphisms $H(x_i) \to y$ in $\mathcal{J}$
with $H(x_0) \to y$ and $H(x_{2n}) \to y$ the given morphisms
```

## MC-STK-ERR-1611 — CATEGORIES-RECON-008 (copyedit)

The sequence subject is singular, as in the cofinal definition. This verb repair is independent of the missing endpoint condition. The neighboring object-and-morphism coordinated subject at 1782 remains unchanged.

Official source line 1786:

```tex
there exist a sequence
```

Replace with:

```tex
there exists a sequence
```

## MC-STK-ERR-1612 — CATEGORIES-RECON-009 (copyedit)

Two categories are introduced; the singular article before the plural noun is malformed.

Official source line 1868:

```tex
be a categories
```

Replace with:

```tex
be categories
```

## MC-STK-ERR-1613 — CATEGORIES-RECON-010 (source_correction)

The family in the limit cone is indexed by objects of J, here y_i and z_i. The two components have domains W and agree because F(h_i) maps to the identity. Their common value then defines q_i. Restore subscripts rather than the meaningless product-like qy_i notation. Both producer reports describe the same six occurrences and are one correction group.

Official source line 1946:

```tex
qy_i
```

Replace with:

```tex
q_{y_i}
```

Official source line 1946:

```tex
qz_i
```

Replace with:

```tex
q_{z_i}
```

Official source line 1953:

```tex
qy_i
```

Replace with:

```tex
q_{y_i}
```

Official source line 1953:

```tex
qz_i
```

Replace with:

```tex
q_{z_i}
```

Official source line 1955:

```tex
qy_{s(j)}
```

Replace with:

```tex
q_{y_{s(j)}}
```

Official source line 1955:

```tex
qz_{t(j)}
```

Replace with:

```tex
q_{z_{t(j)}}
```

## MC-STK-ERR-1614 — CATEGORIES-RECON-011 (copyedit)

The comma separates the final displayed item in the finite object enumeration.

Official source line 1997:

```tex
\ldots x_n
```

Replace with:

```tex
\ldots, x_n
```

## MC-STK-ERR-1615 — CATEGORIES-RECON-012 (source_correction)

The newly defined functor M' has domain I'. Its morphism from x to y_j is f', corresponding to f in the old category I. Thus M'(f') equals M(f) after the first projection. The old argument of M on the right remains unchanged.

Official source line 2012:

```tex
M'(f)
```

Replace with:

```tex
M'(f')
```

## MC-STK-ERR-1616 — CATEGORIES-RECON-013 (notation_clarification)

The equalizers are constructed in C, where the hypothesis provides them. The index arrows x_1 to y_j induce the parallel arrows between M-images; these are the arrows being equalized.

Official source line 2018:

```tex
the successive equalizer of pairs of maps $x_1 \to y_j$ hence
```

Replace with:

```tex
the successive equalizer of pairs of induced maps $M(x_1) \to M(y_j)$ hence
```

## MC-STK-ERR-1617 — CATEGORIES-RECON-015 (copyedit)

Restore the conventional spelling of the compound adjective.

Official source line 2246:

```tex
finegrained
```

Replace with:

```tex
fine-grained
```

## MC-STK-ERR-1618 — CATEGORIES-RECON-016 (copyedit)

The named additional condition is in the cited lemma; its connecting preposition is missing.

Official source line 2291:

```tex
condition Lemma
```

Replace with:

```tex
condition in Lemma
```

## MC-STK-ERR-1619 — CATEGORIES-RECON-018 (source_correction)

The diagram has n two-arrow spans and vertices i_0 through i_{2n}. The endpoint element at 2405 is n_{i_{2n}}=m', and n is the induction parameter. Both producer reports identify the same inconsistent endpoint index.

Official source line 2388:

```tex
i_n = i'
```

Replace with:

```tex
i_{2n} = i'
```

## MC-STK-ERR-1620 — CATEGORIES-RECON-019 (copyedit)

The induction uses a shorter chain, not shorter elements. Name the subject explicitly and separate the sentence while preserving the displayed chain, all its elements and the conclusion.

Official source line 2433:

```tex
and the elements $n_{i_j}$ for $j \geq 3$ which has a smaller length
```

Replace with:

```tex
together with the elements $n_{i_j}$ for $j \geq 3$. This chain has smaller length
```

## MC-STK-ERR-1621 — CATEGORIES-RECON-020 (notation_clarification)

The fixed convention at 2579 uses (I,leq), and 2594 defines geq to be its reverse. A greatest element for leq is terminal for the associated category at 2599–2601 and computes colimits. Match that convention in the remark.

Official source line 2850:

```tex
$(I, \geq)$
```

Replace with:

```tex
$(I, \leq)$
```

## MC-STK-ERR-1622 — CATEGORIES-RECON-021 (copyedit)

The sentence supplies notation for the direct and inverse cases just defined. The revised sentence fixes the broken article/parenthesis construction and places the infinitive after the notation it introduces. Both reports concern the same sentence.

Official source line 2623:

```tex
We will say $(M_i, f_{ii'})$ is a (inverse) system over $I$ to
```

Replace with:

```tex
We will use $(M_i, f_{ii'})$ to denote a system or an inverse system
```

Official source line 2624:

```tex
denote this. The maps $f_{ii'}$ are sometimes
```

Replace with:

```tex
over $I$. The maps $f_{ii'}$ are sometimes
```

## MC-STK-ERR-1623 — CATEGORIES-RECON-022 (clarification)

Pullback along pi sends a system N on the quotient preorder to M_i=N_pi(i) on I. The same construction works contravariantly for inverse systems. The following choice of section gives a quasi-inverse in either case, and the final paragraph explicitly uses systems/colimits before mentioning inverse systems/limits.

Official source line 2669:

```tex
This construction defines a functor between the category
```

Replace with:

```tex
This construction defines a functor from the category of (inverse)
```

Official source line 2670:

```tex
of inverse systems over $I$ and $\overline{I}$.
```

Replace with:

```tex
systems over $\overline{I}$ to the corresponding category over $I$.
```

## MC-STK-ERR-1624 — CATEGORIES-RECON-024 (source_correction)

F is a subcategory of I times omega, its cocone is constructed there, and the added terminal object has an omega-coordinate strictly larger than all F-coordinates. Consequently F+ remains in the product category. Only afterward does cofinality of the projection justify the reduction.

Official source line 2801:

```tex
subcategory of $\mathcal{I}$
```

Replace with:

```tex
subcategory of $\mathcal{I} \times \omega$
```

## MC-STK-ERR-1625 — CATEGORIES-RECON-025 (copyedit)

Restore the established category-name typesetting used in the immediately following lemma.

Official source line 2856:

```tex
\to Sets
```

Replace with:

```tex
\to \textit{Sets}
```

## MC-STK-ERR-1626 — CATEGORIES-RECON-028 (copyedit)

The sentence coordinates two imperative definitions, Let M ... and let S ...; the extra infinitive marker is stray.

Official source line 2993:

```tex
and to let
```

Replace with:

```tex
and let
```

## MC-STK-ERR-1627 — CATEGORIES-RECON-029 (source_correction)

The preceding sentence defines m(n',n) only for n' at least n, dominating m(n') and m(n). That is precisely the index of the diagram's common source. Both reports refer to this same reversed pair.

Official source line 3072:

```tex
X_{m(n, n')}
```

Replace with:

```tex
X_{m(n', n)}
```

## MC-STK-ERR-1628 — CATEGORIES-RECON-030 (source_correction)

m(k,l) is selected only for k at least l. The triangular index set removes undefined terms. Its maximum contains every m(k,l) with l at most k at most n, hence dominates m(n) via m(n,n), is nondecreasing in n, and enforces each required compatibility square. The two reports are duplicates of one repair.

Official source line 3076:

```tex
\max_{k, l \leq n}
```

Replace with:

```tex
\max_{l \leq k \leq n}
```

## MC-STK-ERR-1629 — CATEGORIES-RECON-031 (source_correction)

The comparison quantifies a common refinement m' dominating the two representative index maps m_1 and m_2. The second pair must introduce m_2 instead of repeating m_1. Both reports identify the same token.

Official source line 3094:

```tex
$(m_1, a_2)$
```

Replace with:

```tex
$(m_2, a_2)$
```

## MC-STK-ERR-1630 — CATEGORIES-RECON-034 (copyedit)

The clause refers to the specific natural first arrow just displayed and is missing its determiner. The two producer reports are the same copyedit.

Official source line 3432:

```tex
is natural one
```

Replace with:

```tex
is the natural one
```

## MC-STK-ERR-1631 — CATEGORIES-RECON-035 (source_correction)

The first sentence and displayed Hom calculation concern maps from colim M_i. Its compatible source maps are from the diagram objects of that colimit, not from a limit object. Both reports locate this same noun mismatch.

Official source line 3490:

```tex
constituents of the limit
```

Replace with:

```tex
constituents of the colimit
```

## MC-STK-ERR-1632 — CATEGORIES-RECON-036 (source_correction)

Applying u to the unit X to v(u(X)) gives codomain u(v(u(X))), which is the counit's source in the next arrow. Close the missing outer application parenthesis. Both producers report the same delimiter.

Official source line 3528:

```tex
u(v(u(X))
```

Replace with:

```tex
u(v(u(X)))
```

## MC-STK-ERR-1633 — CATEGORIES-RECON-037 (copyedit)

At fixed C,D the displayed Hom expression is one map, followed by the singular is the map. Make the subject singular.

Official source line 3559:

```tex
the induced maps
```

Replace with:

```tex
the induced map
```

## MC-STK-ERR-1634 — CATEGORIES-RECON-038 (copyedit)

The where clause continues the preceding displayed equation inside the same list item; it is not a standalone sentence.

Official source line 3590:

```tex
Where $\epsilon$
```

Replace with:

```tex
where $\epsilon$
```

## MC-STK-ERR-1635 — CATEGORIES-RECON-039 (copyedit)

The comma separates because from its clause subject without an intervening parenthesis. Deleting it suffices; no need to rewrite the demonstrative.

Official source line 3613:

```tex
because, this
```

Replace with:

```tex
because this
```

## MC-STK-ERR-1636 — CATEGORIES-RECON-040 (copyedit)

A semicolon separates the assertion from the independent imperative without altering either clause.

Official source line 3631:

```tex
big categories, please
```

Replace with:

```tex
big categories; please
```

## MC-STK-ERR-1637 — CATEGORIES-RECON-042 (source_correction)

The bound index is j in J and all subsequent target diagram objects are Y_j. The unrelated i indexes the source presentation X. Both reports identify the same subscript.

Official source line 3817:

```tex
Y = \colim_{j \in J} Y_i
```

Replace with:

```tex
Y = \colim_{j \in J} Y_j
```

## MC-STK-ERR-1638 — CATEGORIES-RECON-043 (copyedit)

The sentence describes two separate presentations, for X and Y. The plural noun agrees with those two presentations.

Official source line 3818:

```tex
as filtered colimit of objects
```

Replace with:

```tex
as filtered colimits of objects
```

## MC-STK-ERR-1639 — CATEGORIES-RECON-044 (notation_clarification)

The exact definition of F(X) at 3810 and the compatible family at 3827–3832 use F'(X_i). Match that construction in the displayed induced morphism.

Official source line 3836:

```tex
\colim F(X_i)
```

Replace with:

```tex
\colim F'(X_i)
```

## MC-STK-ERR-1640 — CATEGORIES-RECON-045 (copyedit)

C is the category in which the displayed diagram's colimit is taken, not the diagram being colimited.

Official source line 3862:

```tex
a filtered colimit of $\mathcal{C}$
```

Replace with:

```tex
a filtered colimit in $\mathcal{C}$
```

## MC-STK-ERR-1641 — CATEGORIES-RECON-047 (source_correction)

The pair p represents X to Y and q represents Y to Z; the constructed pair r has numerator with source X and denominator with source Z, so represents q composed with p. The later equations at 4154 and 4180–4183 use this correct order.

Official source line 4148:

```tex
$p \circ q$
```

Replace with:

```tex
$q \circ p$
```

## MC-STK-ERR-1642 — CATEGORIES-RECON-050 (copyedit)

Hyphenate the compound adjective modifying calculus, consistently with the earlier fine-grained copyedit.

Official source line 4756:

```tex
two sided
```

Replace with:

```tex
two-sided
```

## MC-STK-ERR-1643 — CATEGORIES-RECON-051 (copyedit)

The displayed vertical composition has two natural transformations; the count noun should be plural.

Official source line 4891:

```tex
Composition of transformation of functors
```

Replace with:

```tex
Composition of transformations of functors
```

## MC-STK-ERR-1644 — CATEGORIES-RECON-054 (copyedit)

Use the plural count noun transformations and plural agreement for the two coordinated composition operations which supply the bifunctor's object and morphism maps.

Official source line 5107:

```tex
of transformation of functors gives rise
```

Replace with:

```tex
of transformations of functors give rise
```

## MC-STK-ERR-1645 — CATEGORIES-RECON-055 (copyedit)

Delete the comma separating a nonparenthetical subject from its predicate.

Official source line 5183:

```tex
of $\mathcal{C}$, is
```

Replace with:

```tex
of $\mathcal{C}$ is
```

## MC-STK-ERR-1646 — CATEGORIES-RECON-056 (copyedit)

Use the standard closed compound for subcategories of the hom-categories.

Official source line 5185:

```tex
sub categories
```

Replace with:

```tex
subcategories
```

## MC-STK-ERR-1647 — CATEGORIES-RECON-057 (copyedit)

Both parenthetical descriptions omit the preposition relating composition to the morphisms composed.

Official source line 5188:

```tex
composition $1$-morphisms
```

Replace with:

```tex
composition of $1$-morphisms
```

Official source line 5189:

```tex
composition $2$-morphisms
```

Replace with:

```tex
composition of $2$-morphisms
```

## MC-STK-ERR-1648 — CATEGORIES-RECON-058 (source_correction)

The object class belongs to the specified 2-category mathcal C, as do the hom-categories on the next line. The two reports concern the same dropped font command.

Official source line 5220:

```tex
\Ob(C)
```

Replace with:

```tex
\Ob(\mathcal{C})
```

## MC-STK-ERR-1649 — CATEGORIES-RECON-059 (copyedit)

The singular count noun denotes the already fixed target and needs its article.

Official source line 5249:

```tex
out of 2-category
```

Replace with:

```tex
out of the 2-category
```

## MC-STK-ERR-1650 — CATEGORIES-RECON-060 (source_correction)

The identity coherence morphism is indexed by objects of the domain category mathcal A, matching both preceding data. These French/CJK reports identify one font-command omission.

Official source line 5258:

```tex
\Ob(A)
```

Replace with:

```tex
\Ob(\mathcal{A})
```

## MC-STK-ERR-1651 — CATEGORIES-RECON-062 (notation_clarification)

The referenced construction is a 2-category and the immediately preceding final-object definition is bicategorical, requiring a unique invertible 2-morphism between each pair of 1-morphisms. Restore that qualifier instead of suggesting the ordinary category's stronger strict uniqueness property.

Official source line 5529:

```tex
category of 2-commutative diagrams
```

Replace with:

```tex
$2$-category of $2$-commutative diagrams
```

## MC-STK-ERR-1652 — CATEGORIES-RECON-063 (source_correction)

The target quadruple's second and third entries are the structure 1-morphisms a',b', not the comparison 2-morphisms alpha',beta' carried by the incoming 1-morphism. All three physical reports identify exactly this same tuple.

Official source line 5437:

```tex
(w', \alpha', \beta', \phi')
```

Replace with:

```tex
(w', a', b', \phi')
```

## MC-STK-ERR-1653 — CATEGORIES-RECON-064 (copyedit)

Supply the nominal clause and finite verb in the omission notice.

Official source line 5630:

```tex
(Check this is a functor omitted.)
```

Replace with:

```tex
(The check that this is a functor is omitted.)
```

## MC-STK-ERR-1654 — CATEGORIES-RECON-065 (source_correction)

Each quadruple is an object of the diagram 2-category, so its first component is the category mathcal W. Plain W elsewhere is an object of that category. Both producer reports cover the same two occurrences.

Official source line 5635:

```tex
(W, a, b, t)
```

Replace with:

```tex
(\mathcal{W}, a, b, t)
```

Official source line 5641:

```tex
(W, a, b, t)
```

Replace with:

```tex
(\mathcal{W}, a, b, t)
```

## MC-STK-ERR-1655 — CATEGORIES-RECON-067 (source_correction)

Beta has domain category X and identifies MH(X) with FL(X); alpha has domain Y and identifies GK(Y) with MI(Y). Swap the names while keeping the corresponding X,Y subscripts. The object map at 5706 independently confirms their roles. The two reports are duplicates.

Official source line 5741:

```tex
\alpha_X
```

Replace with:

```tex
\beta_X
```

Official source line 5742:

```tex
\beta_Y
```

Replace with:

```tex
\alpha_Y
```

## MC-STK-ERR-1656 — CATEGORIES-RECON-068 (copyedit)

The noun phrase is full faithfulness; fully modifies faithful, not faithfulness.

Official source line 5760:

```tex
fully faithfulness
```

Replace with:

```tex
full faithfulness
```

## MC-STK-ERR-1657 — CATEGORIES-RECON-069 (clarification)

The producer's given-to-give correction is valid. Source review also shows that the displayed constructions are inverse up to natural isomorphism, not literally: the round trip replaces S by G_2(X_2), with comparison isomorphism phi_2. In the direction from the original triple to the round-trip triple its third component is phi_2^{-1}, while its first two components are identities; the required square follows from phi_2^{-1} phi_1=psi. In the other direction the composite returns psi exactly. Thus quasi-inverse is the precise term in both sentences.

Official source line 5889:

```tex
constructions given mutually inverse functors
```

Replace with:

```tex
constructions give mutually quasi-inverse functors
```

Official source line 5891:

```tex
they are mutually inverse
```

Replace with:

```tex
they are mutually quasi-inverse
```

## MC-STK-ERR-1658 — CATEGORIES-RECON-070 (copyedit)

The unlabelled command draws the same edge as the labelled diagonal functor. Remove only that redundant command; both reports concern the same diagram edge.

Official source line 5934:

```tex
\mathcal{C} \ar[r]^-{\Delta_{\mathcal{C}/\mathcal{D}}} \ar[r] &
```

Replace with:

```tex
\mathcal{C} \ar[r]^-{\Delta_{\mathcal{C}/\mathcal{D}}} &
```

## MC-STK-ERR-1659 — CATEGORIES-RECON-071 (copyedit)

Hyphenate the compound attributive modifier, consistently with the other accepted compound copyedits.

Official source line 5967:

```tex
$2$-category theoretic
```

Replace with:

```tex
$2$-category-theoretic
```

## MC-STK-ERR-1660 — CATEGORIES-RECON-073 (copyedit)

The pronoun referring to the axioms is they; the printed article leaves the clause without its subject.

Official source line 6033:

```tex
that the hold
```

Replace with:

```tex
that they hold
```

## MC-STK-ERR-1661 — CATEGORIES-RECON-074 (copyedit)

The intended frequency adverb agrees with the parallel 'We sometimes say' in the next item.

Official source line 6061:

```tex
also sometime say
```

Replace with:

```tex
also sometimes say
```

## MC-STK-ERR-1662 — CATEGORIES-RECON-076 (copyedit)

Restore the chapter's fibre spelling within a paragraph comparing two constructions of the same named notion.

Official source line 6144:

```tex
$2$-fiber product
```

Replace with:

```tex
$2$-fibre product
```

## MC-STK-ERR-1663 — CATEGORIES-RECON-077 (copyedit)

Terminate the lemma's sentence with a period at the end of its displayed identity.

Official source line 6163:

```tex
\mathcal{X}_U \times_{\mathcal{S}_U} \mathcal{Y}_U
```

Replace with:

```tex
\mathcal{X}_U \times_{\mathcal{S}_U} \mathcal{Y}_U.
```

## MC-STK-ERR-1664 — CATEGORIES-RECON-078 (copyedit)

Add the missing period ending the definition's final prose sentence.

Official source line 6548:

```tex
$(\mathcal{S}, p)$ and $(\mathcal{S}', p')$
```

Replace with:

```tex
$(\mathcal{S}, p)$ and $(\mathcal{S}', p')$.
```

## MC-STK-ERR-1665 — CATEGORIES-RECON-079 (source_correction)

The fibre-product equality is in C/U and uses p', whereas strong cartesianness for p lifts underlying C-maps. Psi-prime lands in x', whose slice image is V'/U, so its underlying codomain is V'. The forgetful functor C/U to C is faithful: with fixed slice source/target, equal underlying maps give equal slice morphisms. In the final lift the slice structure on x' is forced by its arrow to x, so it agrees with the source of g. Four reports partially overlap and are grouped into one coherent typing repair.

Official source line 6615:

```tex
$g \circ h = p(\psi)$
```

Replace with:

```tex
$g \circ h = p'(\psi)$
```

Official source line 6618:

```tex
and $p(\psi') = h$. OK, and now $p'(\psi') : W/U \to V/U$
```

Replace with:

```tex
and $p(\psi')$ equal to the underlying map of $h$. Then
$p'(\psi') : W/U \to V'/U$
```

Official source line 6619:

```tex
is a morphism whose corresponding map $W \to V$ is $h$, hence
```

Replace with:

```tex
is a morphism whose underlying map $W \to V'$ is that of $h$, hence
```

Official source line 6628:

```tex
with $p(\varphi) = g$. By the same argument as above it follows
```

Replace with:

```tex
with $p(\varphi)$ equal to the underlying map of $g$.
By the same argument as above it follows
```

## MC-STK-ERR-1666 — CATEGORIES-RECON-080 (source_correction)

All three functor source/target references denote the same relative inertia category defined at 6786, whose symbol is calligraphic I. Both reports list the same three missing mathcal commands.

Official source line 6837:

```tex
I_{\mathcal{S}/\mathcal{S}'}
```

Replace with:

```tex
\mathcal{I}_{\mathcal{S}/\mathcal{S}'}
```

Official source line 6854:

```tex
I_{\mathcal{S}/\mathcal{S}'}
```

Replace with:

```tex
\mathcal{I}_{\mathcal{S}/\mathcal{S}'}
```

Official source line 6861:

```tex
I_{\mathcal{S}/\mathcal{S}'}
```

Replace with:

```tex
\mathcal{I}_{\mathcal{S}/\mathcal{S}'}
```

## MC-STK-ERR-1667 — CATEGORIES-RECON-085 (copyedit)

Use the single destination preposition for the pseudofunctor. Both producers report the same split word.

Official source line 7050:

```tex
in to
```

Replace with:

```tex
into
```

## MC-STK-ERR-1668 — CATEGORIES-RECON-086 (copyedit)

The label describes the lifted diagram/category as lying above the base diagram. It is deliberate reader-facing prose positioned by an invisible arrow; typeset it as text. The French proposal preserves this meaning while fixing the bare math letters.

Official source line 7188:

```tex
^{above}
```

Replace with:

```tex
^{\text{above}}
```

## MC-STK-ERR-1669 — CATEGORIES-RECON-087 (copyedit)

The following line already supplies 'to morphisms', so 'from morphisms' corrects both the singular noun and the mixed between/to construction in one local edit.

Official source line 7336:

```tex
between morphism
```

Replace with:

```tex
from morphisms
```

## MC-STK-ERR-1670 — CATEGORIES-RECON-089 (copyedit)

The first for all has no bound variable and duplicates the complete for-all-U clause later in the sentence. Both producers identify the same stray words.

Official source line 7352:

```tex
Finally suppose for all $G_U$
```

Replace with:

```tex
Finally suppose $G_U$
```

## MC-STK-ERR-1671 — CATEGORIES-RECON-091 (copyedit)

Supply the article before the singular count noun.

Official source line 7516:

```tex
As functor
```

Replace with:

```tex
As a functor
```

## MC-STK-ERR-1672 — CATEGORIES-RECON-093 (source_correction)

Beta was defined at 7609 with type b^{-1}b to id. The displayed arrow starts at d(x), whose first component is x, and ends at c(b(x)), whose first component is b^{-1}(b(x)). Its first component must therefore be beta_x^{-1}. The target comparison is alpha_x composed with F(beta_x), so the compatibility square reads alpha_x F(beta_x) F(beta_x^{-1})=alpha_x, exactly as required by the fibre-product morphism definition at 7508.

Official source line 7617:

```tex
(\beta_x, \alpha_x)
```

Replace with:

```tex
(\beta_x^{-1}, \alpha_x)
```

## MC-STK-ERR-1673 — CATEGORIES-RECON-094 (copyedit)

The displayed pair is itself a morphism of the fibre category, with objects as endpoints. Deleting the duplicated 'between morphisms' phrase in both parallel constructions gives the intended sentence. Both producers report the same two loci.

Official source line 7789:

```tex
between morphisms in
```

Replace with:

```tex
in
```

Official source line 7936:

```tex
between morphisms in
```

Replace with:

```tex
in
```

## MC-STK-ERR-1674 — CATEGORIES-RECON-095 (copyedit)

Use the frequency adverb for a recurring identification convention.

Official source line 7968:

```tex
we sometime confuse
```

Replace with:

```tex
we sometimes confuse
```

## MC-STK-ERR-1675 — CATEGORIES-RECON-096 (copyedit)

The perfect construction requires the participle seen.

Official source line 8053:

```tex
have already see
```

Replace with:

```tex
have already seen
```

## MC-STK-ERR-1676 — CATEGORIES-RECON-098 (notation_clarification)

Here F is set-valued, so direct membership in F(U) is the explicit notation for its elements and agrees with the fibre's underlying set at 8053.

Official source line 8039:

```tex
x \in \Ob(F(U))
```

Replace with:

```tex
x \in F(U)
```

## MC-STK-ERR-1677 — CATEGORIES-RECON-100 (notation_clarification)

These definitions retain 2-morphisms and declare sub-2-categories, unlike the strict ordinary functor construction in the preceding review. Name the ambient 2-category consistently in both parallel definitions.

Official source line 7988:

```tex
of the category of categories
```

Replace with:

```tex
of the $2$-category of categories
```

Official source line 8189:

```tex
of the category of categories
```

Replace with:

```tex
of the $2$-category of categories
```

## MC-STK-ERR-1678 — CATEGORIES-RECON-101 (copyedit)

Delete the stray auxiliary is before would. Both reports identify the same malformed clause.

Official source line 8132:

```tex
this is would not
```

Replace with:

```tex
this would not
```

## MC-STK-ERR-1679 — CATEGORIES-RECON-102 (notation_clarification)

The lemma asserts uniqueness of the pair (X,j). Name both components in the second such pair while preserving the explicit type of j'.

Official source line 8449:

```tex
For the second, suppose that $j' : \mathcal{S} \to \mathcal{C}/X'$ is
```

Replace with:

```tex
For the second, suppose that $(X', j')$, with
$j' : \mathcal{S} \to \mathcal{C}/X'$, is
```

## MC-STK-ERR-1680 — CATEGORIES-RECON-104 (copyedit)

Delete the syntactically stray article. The two producer reports are duplicates.

Official source line 8949:

```tex
as a above
```

Replace with:

```tex
as above
```

## MC-STK-ERR-1681 — CATEGORIES-RECON-105 (copyedit)

The referenced associativity coherence diagram connects the five bracketings of four objects around a pentagon, not the star called a pentagram.

Official source line 8963:

```tex
pentagram diagram
```

Replace with:

```tex
pentagon diagram
```

## MC-STK-ERR-1682 — CATEGORIES-RECON-106 (copyedit)

Restore the missing h in isomorphism. Both reports concern the same spelling error.

Official source line 9024:

```tex
isomorpism
```

Replace with:

```tex
isomorphism
```

## MC-STK-ERR-1683 — CATEGORIES-RECON-107 (source_correction)

After X=Z tensor 1 and Y=1 tensor W, the right side must be r_{Z tensor 1} tensor id_1 tensor id_W, the expansion of r_X tensor id_Y. The printed last id_Y adds an extra unit factor. Both subsequent expressions at 9046–9047 end in id_W and independently confirm the repair.

Official source line 9043:

```tex
\text{id}_Y
```

Replace with:

```tex
\text{id}_W
```

## MC-STK-ERR-1684 — CATEGORIES-RECON-109 (copyedit)

Supply the article before the singular predicate noun, as both reports propose.

Official source line 9264:

```tex
is functor of monoidal
```

Replace with:

```tex
is a functor of monoidal
```

## MC-STK-ERR-1685 — CATEGORIES-RECON-110 (copyedit)

The preceding data specify an adjunction and its unit; use the matching name for the structure supplying the counit.

Official source line 9401:

```tex
counit of the adjoint
```

Replace with:

```tex
counit of the adjunction
```

## MC-STK-ERR-1686 — CATEGORIES-RECON-112 (copyedit)

The coordinated subject eta-prime and epsilon-prime takes plural agreement.

Official source line 9585:

```tex
makes $X$
```

Replace with:

```tex
make $X$
```

## MC-STK-ERR-1687 — CATEGORIES-RECON-114 (copyedit)

The commutativity constraint swaps X and hom(X,Y), the final two factors of the three-factor tensor product. Calling them two products names the wrong objects.

Official source line 9661:

```tex
last two tensor products
```

Replace with:

```tex
last two tensor factors
```
