# Stacks: corrections and complete replacement proofs

76 proposed corrections and clarifications: 34 copyedits, 35 source corrections and seven clarifications. All 114 received reports are retained with their decisions, including one rejected grammar claim. Independent discoveries are separately attributed. The substack hypothesis and localized-cartesian criterion are repaired with complete counterexamples and proofs; all six proof and review files are retained under evidence/.

Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.

## MC-STK-ERR-1783 — STACKS-RECON-001 (copyedit)

The naming clause introduces the same object symbols for their corresponding 1-morphisms. Add the missing preposition and move also to the beginning of the naming clause.

Official stacks.tex line 231:

```tex
Denote $x, y : \mathcal{C}/U \to \mathcal{S}$ also the corresponding
```

Replace with:

```tex
Also denote by $x, y : \mathcal{C}/U \to \mathcal{S}$ the corresponding
```

## MC-STK-ERR-1784 — STACKS-RECON-002 (copyedit)

Restore of in the instruction selecting pullback functors. The same wording occurs in the definition at source line 432.

Official stacks.tex line 370:

```tex
Make a choice pullbacks
```

Replace with:

```tex
Make a choice of pullbacks
```

## MC-STK-ERR-1785 — STACKS-RECON-003 (copyedit)

Two displayed families are introduced by the plural noun families; remove its conflicting singular article.

Official stacks.tex line 374:

```tex
be a families
```

Replace with:

```tex
be families
```

## MC-STK-ERR-1786 — STACKS-RECON-004 (copyedit)

Put morphism of families before the displayed data specifying that morphism, so the hypothesis has a grammatical noun phrase. Retain the equality of base maps and the original conclusion.

Official stacks.tex line 394:

```tex
\item Given a second $\alpha' : I \to J$, $h' : U \to V$ and
$g'_i : U_i \to V_{\alpha'(i)}$ morphism of families
of maps with fixed target, then if $h = h'$ the two resulting functors
between descent data are canonically isomorphic.
```

Replace with:

```tex
\item Given a second morphism of families of maps with fixed target,
$\alpha' : I \to J$, $h' : U \to V$ and
$g'_i : U_i \to V_{\alpha'(i)}$, if $h = h'$ then the two resulting functors
between descent data are canonically isomorphic.
```

## MC-STK-ERR-1787 — STACKS-RECON-005 (copyedit)

Use the single-word noun for the corresponding morphism presheaves.

Official stacks.tex line 640:

```tex
counter parts
```

Replace with:

```tex
counterparts
```

## MC-STK-ERR-1788 — STACKS-RECON-006 (source_correction)

Definition-stack requires Mor(x,y) to be a sheaf. Fullness gives equality of the Hom sets in the fibre categories with those in the ambient stack, using the same chosen cartesian lifts; the restriction maps are then the same uniquely factored arrows. Thus the required Mor presheaf, not only its Isom subpresheaf, inherits the sheaf condition.

Official stacks.tex line 639:

```tex
\mathit{Isom}
```

Replace with:

```tex
\mathit{Mor}
```

## MC-STK-ERR-1789 — STACKS-RECON-007 (source_correction)

F maps S1 to S2, so its image objects belong to S2. At f:V->U the exact map sends phi to beta_V^{-1} F(phi) alpha_V, where alpha_V:f^*F(x)->F(f^*x) and beta_V:f^*F(y)->F(f^*y) are the unique comparison isomorphisms commuting with the cartesian projections. Its inverse sends psi to the unique phi with F(phi)=beta_V psi alpha_V^{-1}, by full faithfulness of F on the fibre. Both maps commute with restrictions by uniqueness of cartesian factorization. Thus this is an isomorphism of the displayed presheaves, with precisely the corrected target subscript.

Official stacks.tex line 675:

```tex
\mathit{Mor}_{\mathcal{S}_1}(F(x), F(y))
```

Replace with:

```tex
\mathit{Mor}_{\mathcal{S}_2}(F(x), F(y))
```

## MC-STK-ERR-1790 — STACKS-RECON-008 (copyedit)

Restore the preposition in both parallel descent-datum sentences.

Official stacks.tex line 684:

```tex
relative the covering
```

Replace with:

```tex
relative to the covering
```

Official stacks.tex line 686:

```tex
relative the covering
```

Replace with:

```tex
relative to the covering
```

## MC-STK-ERR-1791 — STACKS-RECON-009 (copyedit)

Restore the article introducing the second fibre-product object.

Official stacks.tex line 747:

```tex
be second
```

Replace with:

```tex
be a second
```

## MC-STK-ERR-1792 — STACKS-RECON-010 (copyedit)

Agree the demonstrative with the plural noun.

Official stacks.tex line 752:

```tex
With this identifications
```

Replace with:

```tex
With these identifications
```

## MC-STK-ERR-1793 — STACKS-RECON-011 (copyedit)

Restore the article for the singular functor.

Official stacks.tex line 884:

```tex
is functor
```

Replace with:

```tex
is a functor
```

## MC-STK-ERR-1794 — STACKS-RECON-012 (copyedit)

Use the appropriate article before equivalent.

Official stacks.tex line 890:

```tex
a equivalent category
```

Replace with:

```tex
an equivalent category
```

## MC-STK-ERR-1795 — STACKS-RECON-013 (copyedit)

Agree the noun with the singular fibre and article.

Official stacks.tex line 891:

```tex
a fibre categories
```

Replace with:

```tex
a fibre category
```

## MC-STK-ERR-1796 — STACKS-RECON-014 (source_correction)

Restore the site hypothesis required by the defined 2-category of stacks in groupoids and both stack lemmas invoked in the proof. A topology is needed to give meaning to descent and to the stack condition.

Official stacks.tex line 1037:

```tex
Let $\mathcal{C}$ be a category.
```

Replace with:

```tex
Let $\mathcal{C}$ be a site.
```

## MC-STK-ERR-1797 — STACKS-RECON-015 (clarification)

The local essential-image hypothesis supplies one object x over U and one fibre isomorphism f:F(x)->G(y). State this directly so the quadruple (U,x,y,f) is a well-defined object of the 2-fibre product. Since G(gamma)=id, its endomorphism (id_x,gamma) obeys G(gamma) f = f F(id_x).

Official stacks.tex line 1276:

```tex
we may therefore assume that we have
$f : F(x) \to G(y)$ for some object $x$ of $\mathcal{S}_2$ over $U$
and morphisms $f$ of $(\mathcal{S}_1)_U$. In this case we get
```

Replace with:

```tex
we may therefore assume that there are an object $x$ of $\mathcal{S}_2$
over $U$ and an isomorphism $f : F(x) \to G(y)$ in
$(\mathcal{S}_1)_U$. In this case we get
```

## MC-STK-ERR-1798 — STACKS-RECON-016 (source_correction)

G prime is the projection from S2 times over S1 T1 to S2. It sends (id_x,gamma) to id_x, an arrow in (S2)_U. Restore that target category.

Official stacks.tex line 1284:

```tex
under $G'$ in $\mathcal{S}_1$
```

Replace with:

```tex
under $G'$ in $\mathcal{S}_2$
```

## MC-STK-ERR-1799 — STACKS-RECON-017 (copyedit)

Restore the verb in the purpose clause.

Official stacks.tex line 1319:

```tex
To to this
```

Replace with:

```tex
To do this
```

## MC-STK-ERR-1800 — STACKS-RECON-018 (source_correction)

The presheaf is evaluated at h:V->U. Its pair consists of x in S_V and an arrow f:F(x)->h^*y in T_V; f is a fibre arrow and cannot serve as a base-change arrow to U. Under a map k:W->V over U, restrict x and f and use the cartesian comparison k^*h^*y -> (h k)^*y. This gives the same isomorphism class independently of cartesian choices. The corrected formula has the exact object type used throughout both descent arguments.

Official stacks.tex line 1346:

```tex
f^*y
```

Replace with:

```tex
h^*y
```

## MC-STK-ERR-1801 — STACKS-RECON-019 (copyedit)

Remove the preposition with no complement.

Official stacks.tex line 1537:

```tex
any object $y$ of lying over $V$
```

Replace with:

```tex
any object $y$ lying over $V$
```

## MC-STK-ERR-1802 — STACKS-RECON-020 (source_correction)

Cartesianness is a property of arrows. For a strongly cartesian a:y->x over u and a locally represented b:z->x over u v, each local representative b_i factors uniquely as a c_i, with c_i over the prescribed v on that cover. On pairwise overlaps the c_i agree by uniqueness of cartesian factorization. They define a locally defined morphism c:z->y, and the same uniqueness on a common refinement proves that c is unique. Thus G^2 preserves the original strongly cartesian morphisms.

Official stacks.tex line 1581:

```tex
strongly cartesian objects
```

Replace with:

```tex
strongly cartesian morphisms
```

## MC-STK-ERR-1803 — STACKS-RECON-021 (copyedit)

Restore the preposition relating the descent datum to its covering.

Official stacks.tex line 1596:

```tex
descent datum relative $\mathcal{U}$
```

Replace with:

```tex
descent datum relative to $\mathcal{U}$
```

## MC-STK-ERR-1804 — STACKS-RECON-022 (source_correction)

The preceding definition includes all natural transformations over C, not only invertible ones. To see the distinction exactly, take the one-object one-arrow site with its identity covering. For any small category A, A->C is a stack: it is fibred using identity pullbacks, every Hom presheaf is a sheaf, and descent for the sole identity covering is effective. Take A to be the terminal category and B to be the category with objects 0,1 and a single nonidentity arrow a:0->1. The two functors A->B selecting 0 and 1 preserve cartesian arrows, and a gives a noninvertible 2-morphism. Therefore the defined category of stacks is a 2-category and is not in general a (2,1)-category. Its 2-fibre-product construction and the given proof still apply in this 2-category.

Official stacks.tex line 724:

```tex
The $(2, 1)$-category of stacks
```

Replace with:

```tex
The $2$-category of stacks
```

## MC-STK-ERR-1805 — STACKS-RECON-023 (source_correction)

Definition-descent-data has phi_ij:pr_0^*x_i->pr_1^*x_j. Here beta_i:F(x_i)->y|Ui and beta_j:F(x_j)->y|Uj. On Ui times_U Uj, the descent compatibility is beta_j F(phi_ij)=beta_i, so F(phi_ij)=beta_j^{-1} beta_i. Likewise alpha_i:x_i->x|Ui and alpha_j:x_j->x|Uj give alpha_j phi_ij=alpha_i. With beta_i=beta|Ui F(alpha_i), the corrected first equation yields F(phi_ij)=F(alpha_j)^{-1} F(alpha_i)=F(alpha_j^{-1} alpha_i), and fibre faithfulness gives phi_ij=alpha_j^{-1} alpha_i. Every restriction in the edited formulas is retained. These equations show precisely that the obtained object x realizes the original descent datum.

Official stacks.tex line 1381:

```tex
F(\varphi_{ij}) = \beta_j|_{U_i \times_U U_j} \circ
(\beta_i|_{U_i \times_U U_j})^{-1}
```

Replace with:

```tex
F(\varphi_{ij}) = (\beta_j|_{U_i \times_U U_j})^{-1} \circ
\beta_i|_{U_i \times_U U_j}
```

Official stacks.tex line 1393:

```tex
\varphi_{ij} = \alpha_j|_{U_i \times_U U_j} \circ
(\alpha_i|_{U_i \times_U U_j})^{-1}
```

Replace with:

```tex
\varphi_{ij} = (\alpha_j|_{U_i \times_U U_j})^{-1} \circ
\alpha_i|_{U_i \times_U U_j}
```

## MC-STK-ERR-1806 — STACKS-RECON-024 (source_correction)

The preceding item defines Hom sets between descent-data objects in F prime(U), by common refinements; the following item defines F prime(h). The composition just constructed is composition in F prime(U), not in the original category F(U).

Official stacks.tex line 1699:

```tex
morphisms in $F(U)$
```

Replace with:

```tex
morphisms in $F'(U)$
```

## MC-STK-ERR-1807 — STACKS-RECON-025 (copyedit)

Supply be in the sentence introducing the already constructed stack and morphism.

Official stacks.tex line 1735:

```tex
the stack and $1$-morphism constructed
```

Replace with:

```tex
be the stack and $1$-morphism constructed
```

## MC-STK-ERR-1808 — STACKS-RECON-026 (source_correction)

F:S->X sends x_i to y_i=F(x_i), and y is obtained by effective descent of the y_i in X. Therefore its restrictions are isomorphic to F(x_i). G(x_i) lies instead in S prime and cannot be the displayed local object in X.

Official stacks.tex line 1766:

```tex
agreeing with $G(x_i)$
```

Replace with:

```tex
agreeing with $F(x_i)$
```

## MC-STK-ERR-1809 — STACKS-RECON-027 (clarification)

Close the second argument and then the Mor expression: the base sheaf is Mor(j(f(x)),j(f(x prime))). This matches the original base presheaf immediately above and the declared functor j:Y->Y prime.

Official stacks.tex line 1839:

```tex
\times_{\mathit{Mor}(j(f(x)), j(f(x'))}
```

Replace with:

```tex
\times_{\mathit{Mor}(j(f(x)), j(f(x')))}
```

## MC-STK-ERR-1810 — STACKS-RECON-028 (copyedit)

Supply the article for the specified inertia fibred category.

Official stacks.tex line 1871:

```tex
is inertia of the stackification
```

Replace with:

```tex
is the inertia of the stackification
```

## MC-STK-ERR-1811 — STACKS-RECON-029 (copyedit)

Supply be in the sentence introducing the constructed stack in groupoids and its morphism.

Official stacks.tex line 1934:

```tex
the stack in groupoids and $1$-morphism constructed
```

Replace with:

```tex
be the stack in groupoids and $1$-morphism constructed
```

## MC-STK-ERR-1812 — STACKS-RECON-030 (copyedit)

Introduce the following content clause with that.

Official stacks.tex line 2040:

```tex
fibred category. We say $
```

Replace with:

```tex
fibred category. We say that $
```

## MC-STK-ERR-1813 — STACKS-RECON-031 (copyedit)

Remove the singular article before the plural predicate morphisms.

Official stacks.tex line 2090:

```tex
are both a strongly cartesian
```

Replace with:

```tex
are both strongly cartesian
```

## MC-STK-ERR-1814 — STACKS-RECON-032 (source_correction)

The base functors are p:X->C and q:Y->C, with q F=p. Since F(x_i)=y_i, p(x_i)=q(y_i). The local arrow F(psi_i) therefore defines the section of Isom_Y(F(x),y) over q(y_i), with the cartesian comparison between F(x)|q(y_i) and F(x|q(y_i)) and the covering identification of y_i with y|q(y_i). The expression q(x_i) is undefined because x_i belongs to X.

Official stacks.tex line 2151:

```tex
\mathit{I}(q(x_i))
```

Replace with:

```tex
\mathit{I}(q(y_i))
```

## MC-STK-ERR-1815 — STACKS-RECON-033 (source_correction)

The available hypothesis is q:Y->X a stack for the inherited topology on X. The preceding descent datum is over the covering {x|Ui->x} of X; applying this hypothesis supplies its descent object. Invoking Y/C would invoke the conclusion being proved.

Official stacks.tex line 2218:

```tex
By our assumption that $\mathcal{Y}$ is a stack over $\mathcal{C}$
```

Replace with:

```tex
By our assumption that $\mathcal{Y}$ is a stack over $\mathcal{X}$
```

## MC-STK-ERR-1816 — STACKS-RECON-034 (copyedit)

Restore the subject of may assume.

Official stacks.tex line 2426:

```tex
fibre product may assume
```

Replace with:

```tex
fibre product we may assume
```

## MC-STK-ERR-1817 — STACKS-RECON-035 (source_correction)

The tuple x prime_i=(U,y prime_i,x_i,alpha_i) is in Y prime times_Y X. By the displayed square, F prime is its Y prime projection and G prime is its X projection. The two corrected equations therefore follow directly from the specified objects and functors.

Official stacks.tex line 2448:

```tex
$F'(x'_i) = x_i$
```

Replace with:

```tex
$F'(x'_i) = y'_i$
```

Official stacks.tex line 2449:

```tex
$G'(x'_i) = y'_i$
```

Replace with:

```tex
$G'(x'_i) = x_i$
```

## MC-STK-ERR-1818 — STACKS-RECON-036 (copyedit)

Restore the subject of may assume in this second proof.

Official stacks.tex line 2516:

```tex
fibre product may assume
```

Replace with:

```tex
fibre product we may assume
```

## MC-STK-ERR-1819 — STACKS-RECON-038 (copyedit)

Restore the word both referring to the two displayed lifts.

Official stacks.tex line 2739:

```tex
Then bot
```

Replace with:

```tex
Then both
```

## MC-STK-ERR-1820 — STACKS-RECON-039 (source_correction)

Both arrows lift the fixed a:U->U prime and both underlying arrows beta:y->y prime and beta prime:y double-prime->y prime have common target y prime. Their target objects must therefore both be (U prime,y prime). The cartesian properties then give a unique vertical isomorphism (id_U,iota) from (U,y) to (U,y double-prime) satisfying beta=beta prime iota, proving the stated comparison.

Official stacks.tex line 2739:

```tex
(a, \beta) : (U, y) \to (U, y')
```

Replace with:

```tex
(a, \beta) : (U, y) \to (U', y')
```

Official stacks.tex line 2740:

```tex
(a, \beta') : (U, y'') \to (U, y)
```

Replace with:

```tex
(a, \beta') : (U, y'') \to (U', y')
```

## MC-STK-ERR-1821 — STACKS-RECON-040 (source_correction)

The functor p:S->D takes values in D. The fibre of the pullback over U consists of pairs (U,y) with p(y)=u(U), and fibre arrows (id_U,beta) with p(beta)=id_u(U). The projection to y and beta has inverse y->(U,y), beta->(id_U,beta), giving the declared identification with S_u(U). The same applies over U prime. Under these identifications, a^*(U prime,y prime)=(U,u(a)^*y prime), exactly as the next displayed formula states.

Official stacks.tex line 2774:

```tex
(u^p\mathcal{S})_U = \mathcal{S}_U
```

Replace with:

```tex
(u^p\mathcal{S})_U = \mathcal{S}_{u(U)}
```

Official stacks.tex line 2775:

```tex
(u^p\mathcal{S})_{U'} = \mathcal{S}_{U'}
```

Replace with:

```tex
(u^p\mathcal{S})_{U'} = \mathcal{S}_{u(U')}
```

## MC-STK-ERR-1822 — STACKS-RECON-041 (copyedit)

Restore the defined term descent data in both occurrences.

Official stacks.tex line 2786:

```tex
descend data
```

Replace with:

```tex
descent data
```

Official stacks.tex line 2787:

```tex
descend data
```

Replace with:

```tex
descent data
```

## MC-STK-ERR-1823 — STACKS-RECON-042 (source_correction)

The original tuple comparison maps are alpha_k:G(y prime_k)->F(x_k). Given b prime:y prime_1->y prime_2, the required arrow between F(x_1) and F(x_2) is alpha_2 G(b prime) alpha_1^{-1}. Gerbe condition (2)(b) gives local lifts a_i of this exact arrow. Multiplying the corrected equation on the right by alpha_1|Ui gives F(a_i) alpha_1|Ui=alpha_2|Ui G(b prime)|Ui, which is precisely the square defining the fibre-product morphism (b prime|Ui,a_i).

Official stacks.tex line 2452:

```tex
$F(a_i) = G(b')|_{U_i}$. Then $(b'|_{U_i}, a_i)$ is a morphism
```

Replace with:

```tex
$F(a_i) = \alpha_2|_{U_i} \circ G(b')|_{U_i} \circ
(\alpha_1|_{U_i})^{-1}$. Then $(b'|_{U_i}, a_i)$ is a morphism
```

## MC-STK-ERR-1824 — STACKS-RECON-043 (copyedit)

Restore if in the stated if and only if equivalence.

Official stacks.tex line 2771:

```tex
only $\beta$ is strongly cartesian
```

Replace with:

```tex
only if $\beta$ is strongly cartesian
```

## MC-STK-ERR-1825 — STACKS-RECON-044 (copyedit)

Restore the article introducing the fibre arrow alpha.

Official stacks.tex line 2841:

```tex
is morphism of
```

Replace with:

```tex
is a morphism of
```

## MC-STK-ERR-1826 — STACKS-RECON-045 (copyedit)

Supply the noun triple before its three displayed entries.

Official stacks.tex line 2838:

```tex
is given by a
```

Replace with:

```tex
is given by a triple
```

## MC-STK-ERR-1827 — STACKS-RECON-046 (source_correction)

The two components into u(U1) and u(U prime) must both start at V1. The first is phi1; the second is phi prime b. They have the same composite to u(U), since u(a) phi1=phi b and u(c) phi prime=phi. Therefore the pullback universal property supplies the indicated map phi prime_1:V1->u(U prime_1).

Official stacks.tex line 2906:

```tex
\phi'_1 = (\phi_1, \phi')
```

Replace with:

```tex
\phi'_1 = (\phi_1, \phi' \circ b)
```

## MC-STK-ERR-1828 — STACKS-RECON-047 (source_correction)

The functor p:S->C sends gamma1:x prime_1->x1 to the projection c prime:U prime_1->U1. The map phi prime_1 instead lies in D and determines the structure map of the new triple.

Official stacks.tex line 2909:

```tex
p(\gamma_1) = \phi'_1
```

Replace with:

```tex
p(\gamma_1) = c'
```

## MC-STK-ERR-1829 — STACKS-RECON-048 (source_correction)

The object x prime_1 lies over U prime_1 and its structure map is phi prime_1:V1->u(U prime_1); x prime lies over U prime and its map is phi prime:V->u(U prime). These are exactly the source and target of (a prime,b,alpha prime), where p(alpha prime)=a prime and u(a prime) phi prime_1=phi prime b.

Official stacks.tex line 2916:

```tex
(U_1, \phi_1 : V_1 \to u(U'_1), x'_1)
```

Replace with:

```tex
(U'_1, \phi'_1 : V_1 \to u(U'_1), x'_1)
```

Official stacks.tex line 2918:

```tex
(U, \phi : V \to u(U'), x')
```

Replace with:

```tex
(U', \phi' : V \to u(U'), x')
```

## MC-STK-ERR-1830 — STACKS-RECON-049 (source_correction)

The target is the original object X1 with structure map phi1, as defined at 2891. The arrow (c prime,id_V1,gamma1) satisfies u(c prime) phi prime_1=phi1 and belongs to R because gamma1 is cartesian.

Official stacks.tex line 2925:

```tex
(U_1, \phi : V_1 \to u(U_1), x_1)
```

Replace with:

```tex
(U_1, \phi_1 : V_1 \to u(U_1), x_1)
```

## MC-STK-ERR-1831 — STACKS-RECON-050 (clarification)

State that the two constructed arrows form the required commutative square; this also repairs the singular/plural disagreement.

Official stacks.tex line 2927:

```tex
is an element of $R$ which form a solution of the existence problem
posed by RMS2.
```

Replace with:

```tex
is an element of $R$. Together these two morphisms solve the existence
problem posed by RMS2.
```

## MC-STK-ERR-1832 — STACKS-RECON-051 (source_correction)

The target structure map has codomain u(U prime) and is phi prime=u(c) phi. The source phi:V->u(U) is retained, so the same symbol no longer denotes two differently typed arrows.

Official stacks.tex line 2943:

```tex
(U', \phi : V \to u(U'), x')
```

Replace with:

```tex
(U', \phi' : V \to u(U'), x')
```

## MC-STK-ERR-1833 — STACKS-RECON-052 (source_correction)

Because b=b prime, u(a) phi1=phi b=phi b prime=u(a prime) phi1. The equalizer u(d):u(U2)->u(U1) therefore gives the unique phi2:V1->u(U2) with u(d) phi2=phi1, as required for the new source object.

Official stacks.tex line 2952:

```tex
\phi_1 = u(d) \circ \phi_1
```

Replace with:

```tex
\phi_1 = u(d) \circ \phi_2
```

## MC-STK-ERR-1834 — STACKS-RECON-053 (source_correction)

The arrow delta:x2->x1 is a cartesian lift under p:S->C of d:U2->U1. Its p-image is d, while u(d) is the image of that base arrow in D. The lift gives p(x2)=U2 and p(alpha delta)=ad=a prime d=p(alpha prime delta).

Official stacks.tex line 2953:

```tex
p(\delta) = u(d)
```

Replace with:

```tex
p(\delta) = d
```

## MC-STK-ERR-1835 — STACKS-RECON-054 (source_correction)

p_p has codomain D; X lies over V, X1 over V1, and b:V1->V2. Thus p_p(f2)=b b1 has b1:V->V1. This is the base map required for the cartesian factorization X->X1.

Official stacks.tex line 3017:

```tex
b_1 : U \to U_1
```

Replace with:

```tex
b_1 : V \to V_1
```

## MC-STK-ERR-1836 — STACKS-RECON-055 (source_correction)

The arrow f prime_1 lies in the localized category u_p S, whose structural functor is p_p:u_p S->D, extending p_pp. Since r lies over id_V, passing between f1 and f prime_1 leaves its base arrow b1 unchanged.

Official stacks.tex line 3026:

```tex
p(f'_1) = b_1
```

Replace with:

```tex
p_p(f'_1) = b_1
```

## MC-STK-ERR-1837 — STACKS-RECON-056 (source_correction)

The arrows are r:X prime->X and r prime:X double-prime->X prime. Their composite with domain X double-prime is r r prime, the denominator in the refined roof at 3091.

Official stacks.tex line 3084:

```tex
r' \circ r \in R
```

Replace with:

```tex
r \circ r' \in R
```

## MC-STK-ERR-1838 — STACKS-RECON-057 (source_correction)

The numerator f2=(a2,b2,alpha2) has domain X, while f1,f prime_1 have domain X prime. Comparing their roofs over a common X double-prime requires f f1 r prime=f f prime_1 r prime=f2 r r prime. After refining and renaming X double-prime to X prime, the denominator remains r:X prime->X, so the equation is f f1=f f prime_1=f2 r. Its C-base and fibre-arrow components are precisely a a1=a a prime_1=a2 c and alpha alpha1=alpha alpha prime_1=alpha2 gamma at 3102-3103.

Official stacks.tex line 3088:

```tex
(a_2, b_2, \alpha_2) \circ r'
```

Replace with:

```tex
(a_2, b_2, \alpha_2) \circ r \circ r'
```

Official stacks.tex line 3096:

```tex
(a_2, b_2, \alpha_2).
```

Replace with:

```tex
(a_2, b_2, \alpha_2) \circ r.
```

## MC-STK-ERR-1839 — STACKS-RECON-058 (clarification)

Complete the declared arrow signature with its already fixed target X=(U,phi:V->u(U),x). This makes the ensuing equations a2 c and alpha2 gamma explicitly typed.

Official stacks.tex line 3098:

```tex
Write $r = (c, \text{id}_V, \gamma) : (U', \phi' : V \to u(U'), x')$,
```

Replace with:

```tex
Write $r = (c, \text{id}_V, \gamma) : (U', \phi' : V \to u(U'), x')
\to (U, \phi : V \to u(U), x)$,
```

## MC-STK-ERR-1840 — STACKS-RECON-059 (source_correction)

The new arrow gamma prime:x double-prime->x prime is the cartesian lift of the equalizer inclusion c prime:U double-prime->U prime under p:S->C. The old gamma:x prime->x is already a morphism of S, so is not a base arrow that p can lift. With the corrected lift, the precomposed fibre arrows have equal p-images; cartesianness of alpha then gives their equality.

Official stacks.tex line 3113:

```tex
lifting $\gamma$
```

Replace with:

```tex
lifting $c'$
```

## MC-STK-ERR-1841 — STACKS-RECON-060 (source_correction)

The cartesian property of gamma lifts the particular arrow alpha gamma1 over ac prime=ca prime. It supplies the unique alpha prime over a prime whose composite with gamma is alpha gamma1; its base alone does not specify it uniquely. This exact equation also proves the square required by RMS2.

Official stacks.tex line 2912:

```tex
$\alpha' : x'_1 \to x'$ with $p(\alpha') = a'$.
```

Replace with:

```tex
$\alpha' : x'_1 \to x'$ with $p(\alpha') = a'$ and
$\gamma \circ \alpha' = \alpha \circ \gamma_1$.
```

## MC-STK-ERR-1842 — STACKS-RECON-061 (copyedit)

Separate the concluding hence clause from its cited justification.

Official stacks.tex line 3161:

```tex
Categories, Lemma \ref{categories-lemma-fibred-groupoids}
```

Replace with:

```tex
Categories, Lemma \ref{categories-lemma-fibred-groupoids};
```

## MC-STK-ERR-1843 — STACKS-RECON-062 (source_correction)

The defined source-arrow notation is alpha/a. A target arrow in u^p T consists of its C-base a and its T-arrow beta. Here beta=G prime(a,u(a),alpha) has q-image u(a), because G is over D. Hence the complete ordered pair is exactly (a,G prime(a,u(a),alpha)); it maps the object H(x/U) to H(x prime/U prime) with the types declared at 3201. Composition is componentwise: the C-components compose to a prime a and the T-components compose by functoriality of G prime; identities likewise have both required components.

Official stacks.tex line 3205:

```tex
H((\alpha, a) : x/U \to x'/U') = G'(a, u(a), \alpha)
```

Replace with:

```tex
H(\alpha/a : x/U \to x'/U') = (a, G'(a, u(a), \alpha))
```

## MC-STK-ERR-1844 — STACKS-RECON-063 (copyedit)

Restore the preposition introducing the notation for the composite functor.

Official stacks.tex line 3196:

```tex
Denote $G'
```

Replace with:

```tex
Denote by $G'
```

## MC-STK-ERR-1845 — STACKS-RECON-064 (copyedit)

Restore by in the naming clause for the projection functor.

Official stacks.tex line 3225:

```tex
We denote
```

Replace with:

```tex
We denote by
```

## MC-STK-ERR-1846 — STACKS-RECON-065 (clarification)

Use the source-arrow notation alpha/a established at 3191 and used in the corrected functor definition.

Official stacks.tex line 3246:

```tex
H(a, \alpha)
```

Replace with:

```tex
H(\alpha/a)
```

## MC-STK-ERR-1847 — STACKS-RECON-066 (source_correction)

The literal unqualified condition permits changing the base object. Take the two-object groupoid with objects A,B and one arrow between each pair, all singleton-isomorphism covers, S=C with p=id, and S prime the full subcategory on A. S is a stack with terminal fibres. Every object of S is isomorphic to A, so all three original conditions hold, but S prime has no object over B and cannot lift B->A. With the corrected condition, an ambient cartesian lift c:y->x over f:V->U can be composed with a vertical isomorphism e:y prime->y from an S prime object; c e is an S prime cartesian lift by fullness. The inclusion preserves cartesian arrows by comparison with these lifts. Moreover any total isomorphism z->t with t in S prime, over h:U->W, becomes vertical by composing with the inverse of a cartesian S prime lift t_U->t of h. Thus the original condition (3) gives the fibre isomorphism needed for descent. The complete proof, including the exact natural Mor comparison and all descent comparison maps, is in SUBSTACK_VERTICAL_DERIVATION_20260923.md, Sections 3-7.

Official stacks.tex line 625:

```tex
$x$ is an object of $\mathcal{S}'$, then $y$ is isomorphic to an
object of $\mathcal{S}'$,
```

Replace with:

```tex
$x$ is an object of $\mathcal{S}'$, then $y$ is isomorphic in
$\mathcal{S}_{p(y)}$ to an object of $\mathcal{S}'$,
```

## MC-STK-ERR-1848 — STACKS-RECON-067 (copyedit)

Remove the article before the predicate adjective.

Official stacks.tex line 3277:

```tex
is a strongly cartesian.
```

Replace with:

```tex
is strongly cartesian.
```

## MC-STK-ERR-1849 — STACKS-RECON-068 (source_correction)

A roof representing f:X->Y has numerator X prime->Y and denominator r:X prime->X; in the localization it is Q(numerator) Q(r)^{-1}. Restore the denominator target X.

Official stacks.tex line 3279:

```tex
r : X' \to Y
```

Replace with:

```tex
r : X' \to X
```

## MC-STK-ERR-1850 — STACKS-RECON-069 (clarification)

Restore the separator between the second and third entries of the existing triple.

Official stacks.tex line 3281:

```tex
G'(a, b \alpha)
```

Replace with:

```tex
G'(a, b, \alpha)
```

## MC-STK-ERR-1851 — STACKS-RECON-070 (clarification)

Use the defined source-morphism notation alpha/a in this second occurrence.

Official stacks.tex line 3283:

```tex
H(a, \alpha)
```

Replace with:

```tex
H(\alpha/a)
```

## MC-STK-ERR-1852 — STACKS-RECON-071 (copyedit)

Agree the verb with the plural subject all arrows except possibly beta.

Official stacks.tex line 3285:

```tex
$\beta$ is strongly cartesian
```

Replace with:

```tex
$\beta$ are strongly cartesian
```

## MC-STK-ERR-1853 — STACKS-RECON-072 (copyedit)

Use the noun phrase full faithfulness in both the subsection lead-in and its later restatement.

Official stacks.tex line 3436:

```tex
Fully faithfulness.
```

Replace with:

```tex
Full faithfulness.
```

Official stacks.tex line 3459:

```tex
proof of fully faithfulness
```

Replace with:

```tex
proof of full faithfulness
```

## MC-STK-ERR-1854 — STACKS-RECON-073 (copyedit)

Supply a grammatical subject for the pullback assertion.

Official stacks.tex line 3446:

```tex
Similar holds
```

Replace with:

```tex
The same holds
```

## MC-STK-ERR-1855 — STACKS-RECON-074 (source_correction)

The category u_p S is over D. The canonical functor c prime sends x over U to (U,id_u(U),x), whose D-base is u(U). Therefore its Hom set between c prime(x) and c prime(y) is taken in the fibre over u(U).

Official stacks.tex line 3464:

```tex
\Mor_{(u_p\mathcal{S})_U}
```

Replace with:

```tex
\Mor_{(u_p\mathcal{S})_{u(U)}}
```

## MC-STK-ERR-1856 — STACKS-RECON-075 (source_correction)

Here c:U prime->U and c prime:U->U prime. The denominator square gives u(c) phi=id_u(U). Writing phi=u(c prime), faithfulness of u yields c c prime=id_U, whose domain and codomain are U. The cartesian property of gamma then lifts c prime against id_x to the specified gamma prime with gamma gamma prime=id_x.

Official stacks.tex line 3482:

```tex
$c \circ c' = \text{id}_{U'}$
```

Replace with:

```tex
$c \circ c' = \text{id}_U$
```

## MC-STK-ERR-1857 — STACKS-RECON-076 (copyedit)

Restore by in the naming clause for the localization functor.

Official stacks.tex line 3536:

```tex
We denote $j
```

Replace with:

```tex
We denote by $j
```

## MC-STK-ERR-1858 — STACKS-RECON-077 (source_correction)

The original converse is false. Let C=[0->1], D be terminal, and S have objects z over 0 and s,t over 1, with nonidentity arrows r_s:z->s, v:s->t, r_t:z->t=v r_s. Both r_s and r_t are cartesian, whereas v is not invertible and hence not cartesian over id_1. Both cartesian arrows become invertible in the localization, so Q(v)=Q(r_t)Q(r_s)^{-1} is invertible and cartesian. The corrected criterion retains the entire original construction and states exactly that Q(a,b,alpha) is cartesian iff an allowed R-refinement makes alpha gamma cartesian. The inserted proof derives invertibility of a vertical arrow after an admissible pullback from an inverse roof: equalize its two base maps, obtain a vertical inverse candidate, refine each inverse equation using the right-fraction equality criterion, pass to a common fibre-product refinement, and use cartesian uniqueness to prove both actual inverse identities. Factoring alpha through a cartesian lift then proves the full criterion, including refinement of any chosen roof. The complete independent derivation and counterexample are retained in LOCALIZED_CARTESIAN_DERIVATION_20260924.md, Sections 1-8.

Official stacks.tex line 3009:

```tex
of $u_{pp}\mathcal{S}$ has image $f = ((a, b, \alpha), 1)$
strongly cartesian in $u_p\mathcal{S}$ if and only if $\alpha$
is a strongly cartesian morphism of $\mathcal{S}$.
```

Replace with:

```tex
of $u_{pp}\mathcal{S}$ has image $f = ((a, b, \alpha), 1)$
strongly cartesian in $u_p\mathcal{S}$ if and only if there is an arrow
$r = (c,\text{id}_{V_1},\gamma) : Z \to X_1$ in $R$ such that
$\alpha \circ \gamma$ is strongly cartesian in $\mathcal{S}$.
In particular, this holds whenever $\alpha$ is strongly cartesian.
```

Official stacks.tex line 3124:

```tex
We omit the proof of the fact that for any strongly cartesian morphism
of $u_p\mathcal{S}$ of the form $((a, b, \alpha), 1)$ the morphism
$\alpha$ is strongly cartesian in $\mathcal{S}$.
(We do not need the characterization of strongly cartesian morphisms
in the rest of the proof, although we do use it later in this section.)
```

Replace with:

```tex
We prove the converse with the stated refinement. Write
$Q : u_{pp}\mathcal{S} \to u_p\mathcal{S}$ for the localization functor.
For $Y = (U, \phi : V \to u(U), y)$ and $b : V' \to V$, put
$$
Y_b = (U, \phi \circ b : V' \to u(U), y),\qquad
k_b = (\text{id}_U, b, \text{id}_y) : Y_b \to Y.
$$
The implication already proved shows that $Q(k_b)$ is strongly cartesian.
Consequently every morphism $h : X \to Y$ over $b$ factors uniquely as
$h = Q(k_b) \circ i_h$, with $i_h : X \to Y_b$ over $\text{id}_{V'}$.
Moreover, $h$ is strongly cartesian if and only if $i_h$ is an isomorphism.
Indeed, if $h$ is strongly cartesian, its universal property gives
$j : Y_b \to X$ over $\text{id}_{V'}$ with $h \circ j = Q(k_b)$.
Uniqueness for $Q(k_b)$ gives $i_h \circ j = \text{id}_{Y_b}$, and
uniqueness for $h$ gives $j \circ i_h = \text{id}_X$.
The reverse implication follows by composition with an isomorphism.

\medskip\noindent
We first establish the required detection of vertical isomorphisms.
Fix $\phi : V \to u(U)$ and a morphism $\delta : x \to y$ in
$\mathcal{S}_U$. Write
$$
D_\delta = (\text{id}_U, \text{id}_V, \delta) :
(U,\phi,x) \longrightarrow (U,\phi,y).
$$
We claim that $Q(D_\delta)$ is invertible if and only if there exist
$c : W \to U$ and $\psi : V \to u(W)$ with $u(c) \circ \psi = \phi$
such that the pullback of $\delta$ along $c$ is invertible.
More explicitly, choose strongly cartesian morphisms
$\gamma_x : x_W \to x$ and $\gamma_y : y_W \to y$ over $c$.
The pullback is the unique vertical morphism $\delta_W : x_W \to y_W$
such that
$$
\gamma_y \circ \delta_W = \delta \circ \gamma_x.
$$
Changing these two cartesian lifts conjugates $\delta_W$ by the unique
vertical comparison isomorphisms, so invertibility is independent of
these choices. If $\delta_W$ is invertible, the displayed equation and
the two morphisms of $R$ defined by $\gamma_x,\gamma_y$ show that
$Q(D_\delta)$ is invertible.

\medskip\noindent
Conversely, represent an inverse to $Q(D_\delta)$ by $Q(e)Q(r)^{-1}$, where
$$
r = (c,\text{id}_V,\gamma) : (T,\theta,z) \to (U,\phi,y),\qquad
e = (a,\text{id}_V,\epsilon) : (T,\theta,z) \to (U,\phi,x),
$$
and $r \in R$. Thus $a,c : T \to U$ and
$u(a)\theta = \phi = u(c)\theta$.
Let $h : T_1 \to T$ be the equalizer of $a,c$.
As $u$ preserves this equalizer, there exists
$\theta_1 : V \to u(T_1)$ with $u(h)\theta_1 = \theta$.
Choose a strongly cartesian $\zeta : z_1 \to z$ over $h$ and refine
the inverse roof by $(h,\text{id}_V,\zeta) \in R$.
Put $d = ah = ch$ and $y_1 = z_1$.
Then $\tau_y = \gamma\zeta : y_1 \to y$ is strongly cartesian over $d$.
Choose a strongly cartesian $\tau_x : x_1 \to x$ over $d$.
There are unique vertical morphisms
$\eta : y_1 \to x_1$ and $\delta_1 : x_1 \to y_1$ satisfying
$$
\tau_x\eta = \epsilon\zeta,\qquad
\tau_y\delta_1 = \delta\tau_x.
$$
For this paragraph, regard $x_1,y_1$ as the triples with base $T_1$
and structure map $\theta_1$, and write
$$
t_x = (d,\text{id}_V,\tau_x),\quad
t_y = (d,\text{id}_V,\tau_y),\quad
E_\eta = (\text{id}_{T_1},\text{id}_V,\eta),\quad
D_1 = (\text{id}_{T_1},\text{id}_V,\delta_1).
$$
The inverse is $Q(t_x)Q(E_\eta)Q(t_y)^{-1}$, whereas
$Q(D_\delta) = Q(t_y)Q(D_1)Q(t_x)^{-1}$.
The two inverse identities therefore give
$$
Q(E_\eta D_1) = \text{id}_{(T_1,\theta_1,x_1)},\qquad
Q(D_1 E_\eta) = \text{id}_{(T_1,\theta_1,y_1)}.
$$
The equality criterion for right fractions, applied to denominators
equal to identities, supplies two arrows of $R$. Write their
$\mathcal{C}$-components as $c_x : T_x \to T_1$ and
$c_y : T_y \to T_1$, their structure maps as $\theta_x,\theta_y$, and
their strongly cartesian $\mathcal{S}$-components as
$\rho_x : z_x \to x_1$ and $\rho_y : z_y \to y_1$.
Then
$$
(\eta\delta_1)\rho_x = \rho_x,\qquad
(\delta_1\eta)\rho_y = \rho_y,\qquad
u(c_x)\theta_x = \theta_1 = u(c_y)\theta_y.
$$
Form $T_2 = T_x \times_{T_1} T_y$, with projections $e_x,e_y$, and put
$k = c_xe_x = c_ye_y$. Preservation of this fibre product gives
$\theta_2 : V \to u(T_2)$ such that
$u(e_x)\theta_2 = \theta_x$ and $u(e_y)\theta_2 = \theta_y$.
In particular $u(k)\theta_2 = \theta_1$ and $u(dk)\theta_2 = \phi$.
Choose strongly cartesian arrows $\kappa_x : x_2 \to x_1$ and
$\kappa_y : y_2 \to y_1$ over $k$, and the unique vertical arrows
$\delta_2 : x_2 \to y_2$ and $\eta_2 : y_2 \to x_2$ with
$$
\kappa_y\delta_2 = \delta_1\kappa_x,\qquad
\kappa_x\eta_2 = \eta\kappa_y.
$$
Since $k = c_xe_x$, cartesianness of $\rho_x$ factors $\kappa_x$
through $\rho_x$, and hence $\eta\delta_1\kappa_x = \kappa_x$.
Similarly $\delta_1\eta\kappa_y = \kappa_y$.
It follows that
$$
\kappa_x\eta_2\delta_2
= \eta\kappa_y\delta_2
= \eta\delta_1\kappa_x
= \kappa_x,
$$
and
$$
\kappa_y\delta_2\eta_2
= \delta_1\kappa_x\eta_2
= \delta_1\eta\kappa_y
= \kappa_y.
$$
Cartesian uniqueness, with fixed identity base maps, yields
$\eta_2\delta_2 = \text{id}_{x_2}$ and
$\delta_2\eta_2 = \text{id}_{y_2}$.
The composites $\tau_x\kappa_x,\tau_y\kappa_y$ are strongly cartesian
over $dk$, and
$$
(\tau_y\kappa_y)\delta_2 = \delta(\tau_x\kappa_x).
$$
Thus $\delta_2$ is the required invertible pullback of $\delta$.
This proves the detection claim without assuming that localization
reflects isomorphisms before a refinement.

\medskip\noindent
Return to $A = (a,b,\alpha) : X_1 \to X_2$.
Choose a strongly cartesian $\tau : a^*x_2 \to x_2$ over $a$, and
write $\alpha = \tau\delta$, where $\delta : x_1 \to a^*x_2$ is vertical.
Put $X_a = (U_1,\phi_1 : V_1 \to u(U_1),a^*x_2)$.
The exact factorization is
$$
A = k_b \circ (a,\text{id}_{V_1},\tau)
\circ (\text{id}_{U_1},\text{id}_{V_1},\delta),
$$
where $k_b : (X_2)_b \to X_2$, and the middle factor belongs to $R$.
Consequently, if $Q(A)$ is strongly cartesian, its vertical factor
relative to $Q(k_b)$ is invertible, and so is $Q(D_\delta)$.
The detection claim supplies $c : W \to U_1$, $\psi : V_1 \to u(W)$
with $u(c)\psi = \phi_1$, strongly cartesian
$\gamma : z \to x_1$ and $\rho : w \to a^*x_2$ over $c$, and an
invertible $\delta_W : z \to w$ such that
$\rho\delta_W = \delta\gamma$.
Therefore
$$
\alpha\gamma = \tau\delta\gamma = \tau\rho\delta_W
$$
is strongly cartesian. The arrow
$r = (c,\text{id}_{V_1},\gamma) : (W,\psi,z) \to X_1$
belongs to $R$, as required.
Conversely, if such an $r$ exists, the implication proved earlier
shows that $Q(Ar)$ is strongly cartesian. Since $Q(r)$ is an
isomorphism, $Q(A) = Q(Ar)Q(r)^{-1}$ is strongly cartesian as well.
This proves the stated characterization.
For any chosen roof $Q(A)Q(r_0)^{-1}$ representing a strongly
cartesian morphism, the same argument gives an additional $r_1 \in R$
with cartesian numerator in the refined roof
$Q(Ar_1)Q(r_0r_1)^{-1}$. Thus the characterization applies to the
roof representation used below, without asserting that an arbitrary
original numerator is already strongly cartesian.
```
