# Sites and Sheaves: proposed corrections and clarifications

29 proposed changes: 22 copyedits, five source corrections and two clarifications. The complete intake review retains all 246 reports, duplicates, rejected claims and adverse evidence. All 107 earlier corrections remain intact. No new theorem is claimed.

Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.

## MC-STK-ERR-1754 — SITES-RECON-002 (copyedit)

Insert the missing possessive apostrophe and state that the two constructed maps are inverses. The map constructions and the adjunction statement remain unchanged.

Official sites.tex line 583:

```tex
verify they are each others inverse.
```

Replace with:

```tex
verify that they are each other's inverses.
```

## MC-STK-ERR-1755 — SITES-RECON-003 (copyedit)

Remove the singular article before the coordinated plural nouns presheaves and sheaves. Preserve the existing comparison and its reference.

Official sites.tex line 781:

```tex
a presheaves and sheaves
```

Replace with:

```tex
presheaves and sheaves
```

## MC-STK-ERR-1756 — SITES-RECON-004 (copyedit)

Delete the first by in replace by G-Sets by a full subcategory, leaving the intended category replacement and both set-theoretic references intact.

Official sites.tex line 801:

```tex
We first replace by
```

Replace with:

```tex
We first replace
```

## MC-STK-ERR-1757 — SITES-RECON-007 (copyedit)

Use the plural categories as the subject of are equal, referring to the two sheaf categories in the preceding inclusions.

Official sites.tex line 1310:

```tex
the category of sheaves are equal.
```

Replace with:

```tex
the categories of sheaves are equal.
```

## MC-STK-ERR-1758 — SITES-RECON-008 (copyedit)

Attach the refinement data to the chosen family with with the refinement given by, preserving alpha and every component f_j.

Official sites.tex line 1333:

```tex
 and refinement given
```

Replace with:

```tex
, with the refinement given
```

## MC-STK-ERR-1759 — SITES-RECON-010 (source_correction)

The definition makes H^0 an equalizer of sets for a set-valued presheaf and supplies no group operations. This cannot uniformly be a group: on the category with one object and its identity, use only the identity covering and let F take the empty set. Its restriction is the identity of the empty set; the sheaf condition for the identity covering holds, and H^0 of that covering is empty. A group must contain an identity element, so this H^0 is not a group. The identity functor of the same site gives the same counterexample at the quasi-continuous loci. Replace group/groups by set/sets in all three reported phrases.

Official sites.tex line 1635:

```tex
cohomology group
```

Replace with:

```tex
cohomology set
```

Official sites.tex line 2658:

```tex
cohomology group
```

Replace with:

```tex
cohomology set
```

Official sites.tex line 2670:

```tex
groups.
```

Replace with:

```tex
sets.
```

## MC-STK-ERR-1760 — SITES-RECON-023 (source_correction)

Write v:V_c to U_alpha(c) for the refinement map. Applying sheafification to the induced map of representable presheaves gives h_Vc-sharp to h_Ualpha(c)-sharp. Since F_iota(alpha(c)) is a sheaf, the section s_alpha(c) corresponds by Yoneda and the sheafification adjunction to a unique map from h_Ualpha(c)-sharp to that sheaf. Composing these two maps and the given map to h_U-sharp corresponds to the restriction of the image of s_alpha(c), which is id_U restricted to V_c. By the same adjunction/Yoneda bijection this is exactly the map h_Vc-sharp to h_U-sharp induced by V_c to U. The added marker makes the displayed chain this actual chain of sheaf morphisms.

Official sites.tex line 3342:

```tex
h_{U_{\alpha(c)}}
```

Replace with:

```tex
h_{U_{\alpha(c)}}^\#
```

## MC-STK-ERR-1761 — SITES-RECON-035 (copyedit)

The plural subject compatibilities takes imply, preserving the exact adjunction assertion and all of its indices.

Official sites.tex line 3939:

```tex
implies that
```

Replace with:

```tex
imply that
```

## MC-STK-ERR-1762 — SITES-RECON-050 (source_correction)

At X the presheaf extension of G is the disjoint union of G(X,a) over a:X to U. Applying that functor to G to the terminal presheaf sends (a,s) to (a,*), and its target is the disjoint union of singleton sets indexed by a, canonically h_U(X). This map is natural because restriction sends (a,s) to (a composed with b, G(b)(s)); on the target it sends a to a composed with b. Thus the named gamma factors through j_{U!}^{PSh}*, exactly as the following identification requires. Adding the PSh superscript supplies the actual intermediate object.

Official sites.tex line 5362:

```tex
\to j_{U!}*
```

Replace with:

```tex
\to j_{U!}^{PSh}*
```

## MC-STK-ERR-1763 — SITES-RECON-055 (copyedit)

Each singular article introduces one structured collection. Use datum for that single structure, retaining data for collections or the category of such structures. The nearby defining occurrence at 5942 has the same singular article an across the line break and is repaired in the same unit.

Official sites.tex line 5844:

```tex
glueing data
```

Replace with:

```tex
glueing datum
```

Official sites.tex line 5942:

```tex
glueing data
```

Replace with:

```tex
glueing datum
```

Official sites.tex line 5980:

```tex
glueing data
```

Replace with:

```tex
glueing datum
```

## MC-STK-ERR-1764 — SITES-RECON-057 (copyedit)

The coordinated objects of the hypotheses are the site and the object of localization. Moving the misplaced on yields on the site or on the object.

Official sites.tex line 6047:

```tex
on the site on or the object
```

Replace with:

```tex
on the site or on the object
```

## MC-STK-ERR-1765 — SITES-RECON-060 (copyedit)

The subject contains two coordinated restrictions, so its verb is produce. The statement still discusses both the pushforward and extension by the empty set before giving the precise hypothesis below.

Official sites.tex line 6155:

```tex
produces back
```

Replace with:

```tex
produce back
```

## MC-STK-ERR-1766 — SITES-RECON-062 (copyedit)

The introduction refers to the specific relation treated by the following lemma, so the singular count noun relation takes the article the.

Official sites.tex line 6261:

```tex
understand relation
```

Replace with:

```tex
understand the relation
```

## MC-STK-ERR-1767 — SITES-RECON-081 (copyedit)

The imperative names the inverse equivalence a; Denote by a the inverse functor requires the preposition by, as at the earlier naming occurrence for g.

Official sites.tex line 7366:

```tex
Denote
```

Replace with:

```tex
Denote by
```

## MC-STK-ERR-1768 — SITES-RECON-094 (copyedit)

The first condition names u(X)={*} and then describes it as a singleton. Inserting is completes that predicate while retaining the exact equality and all later conditions.

Official sites.tex line 8351:

```tex
$u(X) = \{*\}$ a singleton
```

Replace with:

```tex
$u(X) = \{*\}$ is a singleton
```

## MC-STK-ERR-1769 — SITES-RECON-106 (copyedit)

The naming construction denotes the composite point by q_j. Inserting by after denote supplies the required preposition.

Official sites.tex line 9178:

```tex
denote
```

Replace with:

```tex
denote by
```

## MC-STK-ERR-1770 — SITES-RECON-109 (copyedit)

The grammatical subject each of the functors is singular, so its verb is does. The representable functors and filtered-colimit finite-limit argument are unchanged.

Official sites.tex line 9265:

```tex
do, see
```

Replace with:

```tex
does, see
```

## MC-STK-ERR-1771 — SITES-RECON-110 (copyedit)

The definition gives three simultaneous conditions, including the assertion that the ordering on J is induced from I. Inserting is completes that clause.

Official sites.tex line 9270:

```tex
the ordering on $J$ induced
```

Replace with:

```tex
the ordering on $J$ is induced
```

## MC-STK-ERR-1772 — SITES-RECON-111 (source_correction)

The supplied J-system has transition maps g_{j j_0}:V_j to V_{j_0}. With f prime:V_{j_0} to W, its pullback of W_k to V_j therefore uses f prime composed with g_{j j_0}. For j prime at least j, the transition g_{j prime j} induces the map between these pullbacks because g_{j j_0} composed with g_{j prime j}=g_{j prime j_0}; identities and compositions follow uniquely from the pullback property. This is the exact system used to take the subsequent colimits and construct the refinement.

Official sites.tex line 9303:

```tex
f_{j j_0}
```

Replace with:

```tex
g_{j j_0}
```

## MC-STK-ERR-1773 — SITES-RECON-113 (copyedit)

The naming imperative uses Denote by S the class of all pairs. Adding by repairs that construction without altering the ordered class or its elements.

Official sites.tex line 9355:

```tex
Denote $\mathcal{S}$
```

Replace with:

```tex
Denote by $\mathcal{S}$
```

## MC-STK-ERR-1774 — SITES-RECON-118 (copyedit)

The clause introduces one surjective map of sheaves and needs the article a. The specified arrow and subsequent pullback square are unchanged.

Official sites.tex line 9699:

```tex
be surjective map
```

Replace with:

```tex
be a surjective map
```

## MC-STK-ERR-1775 — SITES-RECON-122 (copyedit)

The concessive phrase while not exact on sheaves of sets interrupts the subject i_* and the main predicate is exact. Its existing closing comma needs the opening comma after i_*.

Official sites.tex line 9974:

```tex
$i_*$ while
```

Replace with:

```tex
$i_*$, while
```

## MC-STK-ERR-1776 — SITES-RECON-126 (copyedit)

Two additional naming clauses read while adjudicating the cited proof contexts use Denote [symbol] the [object] without by: the stalk notation at 9216 and presheaf-colimit notation at 10046. Insert the same preposition used in the other verified naming repairs. These two occurrences were found directly in primary-source reading and are not counted as received reports.

Official sites.tex line 9216:

```tex
Denote $p_i$
```

Replace with:

```tex
Denote by $p_i$
```

Official sites.tex line 10046:

```tex
Denote $\colim
```

Replace with:

```tex
Denote by $\colim
```

## MC-STK-ERR-1777 — SITES-RECON-136 (clarification)

Write Delta=(id,id):F to F times F. The two endomorphisms lambda_r and lambda_r prime induce their product lambda_r times lambda_r prime:F times F to F times F, and addition maps that product object to F. Hence the intended identity is lambda_{r+r prime}=addition composed with (lambda_r times lambda_r prime) composed with Delta; at each object it sends x to lambda_r(x)+lambda_r prime(x). Parenthesizing the product states this exact composition unambiguously.

Official sites.tex line 10558:

```tex
+ \circ \lambda_r \times \lambda_{r'} \circ
```

Replace with:

```tex
+ \circ (\lambda_r \times \lambda_{r'}) \circ
```

## MC-STK-ERR-1778 — SITES-RECON-140 (copyedit)

The naming clause denotes the set of sieves by J(U). The insertion completes denote by J(U) the set while leaving its universal base-change condition unchanged.

Official sites.tex line 11117:

```tex
denote
```

Replace with:

```tex
denote by
```

## MC-STK-ERR-1779 — SITES-RECON-148 (source_correction)

Lemma sieves-set proves that an intersection is a sieve, without asserting that it is covering. Lemma topology-basic (1) proves finite intersections of covering sieves are covering: if alpha:V to U is in S(V), pulling back S intersect S prime along alpha gives the pullback of S prime, which covers V; transitivity then makes S intersect S prime cover U. This is exactly the fact needed both for the directed colimit at 11484 and the common representative sieve at 11574. Replace the two wrong references by this proved lemma; the latter matching occurrence was found directly during the source review.

Official sites.tex line 11484:

```tex
\ref{lemma-sieves-set}
```

Replace with:

```tex
\ref{lemma-topology-basic}
```

Official sites.tex line 11574:

```tex
\ref{lemma-sieves-set}
```

Replace with:

```tex
\ref{lemma-topology-basic}
```

## MC-STK-ERR-1780 — SITES-RECON-154 (copyedit)

The naming clause denotes the common restriction by psi. Inserting by relates the named map to its symbol in the same way as the other naming repairs.

Official sites.tex line 11636:

```tex
Denote the common restriction $\psi$.
```

Replace with:

```tex
Denote the common restriction by $\psi$.
```

## MC-STK-ERR-1781 — SITES-RECON-155 (copyedit)

The lemma adopts the category and both topologies from the preceding theorem. Assumptions and notation are as in states that inherited setup as a complete clause and uses the plural for the collected hypotheses.

Official sites.tex line 11763:

```tex
Assumption and notation as in
```

Replace with:

```tex
Assumptions and notation are as in
```

## MC-STK-ERR-1782 — SITES-RECON-157 (clarification)

The second arrow describes the image of an object F under the stalk functor, so mapsto makes that assignment explicit. It matches the object-assignment arrow in the presheaf stalk display immediately above.

Official sites.tex line 11840:

```tex
\mathcal{F} \to \mathcal{F}_p
```

Replace with:

```tex
\mathcal{F} \mapsto \mathcal{F}_p
```
