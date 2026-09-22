# Twenty-nine proposed corrections

This batch repairs inherited text only. It adds no theorems. It combines missing Sets/Schemes findings with the eleven remaining proposals from the readable selection.

AI review and correction preparation: OpenAI Codex — GPT-6 Astra, Ultra effort. No human review or upstream endorsement is claimed. Earlier rejected and optional findings remain in the bound evidence; they are not admitted by this batch.

## SETS-RECON-005 — sets.tex (mathematical_source_correction)

beta_0 is already determined at 989–993 by representative covers of each support; it was not chosen to bound the ranks of all prescribed members of Cov_0. Choosing beta_1 at 1047 cannot change the already-fixed beta_0 in the printed condition. Since Cov_0 is a set, one can choose beta_1 large enough to bound both it and the arrow set, and also beta_1 >= beta_0. This is exactly what 1051–1053 use to propagate the conditions to f(beta_1) and later stages, yielding the first property of the lemma.

Official source line 1049:

```tex
$\text{Cov}_0 \subset V_{\beta_0}$,
```

Replace with:

```tex
$\text{Cov}_0 \subset V_{\beta_1}$,
```

## SETS-RECON-006 — sets.tex (copyedit)

The indefinite article precedes alpha, which begins with a vowel sound. Changing a to an leaves every quantifier, symbol and inference unchanged.

Official source line 203:

```tex
pick a $\alpha_s < \beta$
```

Replace with:

```tex
pick an $\alpha_s < \beta$
```

## SCHEMES-RECON-001 — schemes.tex (mathematical_source_correction)

The refined cover is D(f_i) at 1301 and phi_i at 1303 identifies the sheaf on that open with the sheaf from M_i. Thus phi_i inverse sends m_i to a section on D(f_i), which is then restricted to D(f_if_j).

Official source line 1373:

```tex
\mathcal{F}(U_i)
```

Replace with:

```tex
\mathcal{F}(D(f_i))
```

## SCHEMES-RECON-002 — schemes.tex (copyedit)

The property named immediately above is universally closed; the adverb modifies closed.

Official source line 3754:

```tex
universal closed morphisms
```

Replace with:

```tex
universally closed morphisms
```

## SCHEMES-RECON-003 — schemes.tex (copyedit)

The equivalence phrase has a missing final d in and.

Official source line 4078:

```tex
if an only if
```

Replace with:

```tex
if and only if
```

## SCHEMES-RECON-004 — schemes.tex (diagram_source_correction)

The cartesian square has one bottom edge, the diagonal T to T times_S T. The second identical-direction arrow instruction contributes no second morphism or label and duplicates that edge.

Official source line 4252:

```tex
T \ar[r]^{\Delta_{T/S}} \ar[r] & T \times_S T
```

Replace with:

```tex
T \ar[r]^{\Delta_{T/S}} & T \times_S T
```

## SCHEMES-RECON-005 — schemes.tex (mathematical_source_correction)

GL_2 is represented by matrices whose determinant ad-bc is a unit. Its coordinate ring inverts the entire determinant. The printed slash expression does not group that denominator and instead reads as 1/(ad) minus bc (or 1/a times d minus bc); neither is the displayed localization of GL_2.

Official source line 4434:

```tex
1/ad - bc
```

Replace with:

```tex
1/(ad - bc)
```

## SCHEMES-RECON-006 — schemes.tex (copyedit)

The morphism has two scheme objects; the standard category description is morphism of schemes.

Official source line 4452:

```tex
of scheme where
```

Replace with:

```tex
of schemes where
```

## SCHEMES-RECON-007 — schemes.tex (copyedit)

The title omits of between criterion and separatedness; the section heading already supplies the complete phrase.

Official source line 4498:

```tex
Valuative criterion separatedness
```

Replace with:

```tex
Valuative criterion of separatedness
```

## SCHEMES-RECON-010 — schemes.tex (copyedit)

The subject names the kernel and cokernel, two objects, and takes a plural verb.

Official source line 4742:

```tex
is quasi-coherent.
```

Replace with:

```tex
are quasi-coherent.
```

## SCHEMES-RECON-012 — schemes.tex (copyedit)

The paired restriction-sheaf symbols form a plural subject.

Official source line 4811:

```tex
$\mathcal{F}_i, \mathcal{F}_{ijk}$ denotes the
```

Replace with:

```tex
$\mathcal{F}_i, \mathcal{F}_{ijk}$ denote the
```

## SCHEMES-RECON-013 — schemes.tex (copyedit)

The preceding line says second and, so the pair of numbered terms needs the plural noun terms.

Official source line 4817:

```tex
third term of the exact sequence are
```

Replace with:

```tex
third terms of the exact sequence are
```

## SCHEMES-RECON-014 — schemes.tex (copyedit)

The sentence introduces f and g, two morphisms.

Official source line 145:

```tex
be morphism of locally
```

Replace with:

```tex
be morphisms of locally
```

## SCHEMES-RECON-015 — schemes.tex (mathematical_source_correction)

The sheaf O_V lives on V, and the declared map with codomain V is f': X to V. Lines 257–260 explicitly factor the inverse image through f', and lines 264 and 268 use f' inverse already. The missing prime at 267 is the unique inconsistent sheaf-domain annotation.

Official source line 267:

```tex
$f^{-1}(\mathcal{O}_V)
```

Replace with:

```tex
$f'^{-1}(\mathcal{O}_V)
```

## SCHEMES-RECON-017 — schemes.tex (copyedit)

The printed subject restriction mapping is singular, so is restores agreement without altering the localization construction.

Official source line 922:

```tex
restriction mapping on the affine schemes are defined
```

Replace with:

```tex
restriction mapping on the affine schemes is defined
```

## SCHEMES-RECON-018 — schemes.tex (copyedit)

The paragraph varies x, and both the predicate maps and the following relative clause are plural. Pluralizing the subject gives consistent agreement.

Official source line 1103:

```tex
The induced map on stalks are the maps
```

Replace with:

```tex
The induced maps on stalks are the maps
```

## SCHEMES-RECON-019 — schemes.tex (copyedit)

The existential asserts one R-module M, requiring exists.

Official source line 1356:

```tex
there exist an $R$-module
```

Replace with:

```tex
there exists an $R$-module
```

## SCHEMES-RECON-022 — schemes.tex (copyedit)

The comma immediately after Because separates the conjunction from its subject rather than an intervening parenthesis.

Official source line 2964:

```tex
Because, $(U_i,
```

Replace with:

```tex
Because $(U_i,
```

## H100B-SOURCE-006 — algebra.tex (mathematical_source_correction)

The chosen alpha:F→G induces precomposition Hom(G,N)→Hom(F,N), hence the same direction on cohomology. The displayed induced arrow has its source and target reversed. Both chosen lifts F→G induce homotopic maps in the contravariant direction Hom(G,N)→Hom(F,N). Match the proof to the corrected display.

Official source line 17587:

```tex
H^i(\Hom_R(F_{\bullet}, N))
\longrightarrow
H^i(\Hom_R(G_{\bullet}, N))
```

Replace with:

```tex
H^i(\Hom_R(G_{\bullet}, N))
\longrightarrow
H^i(\Hom_R(F_{\bullet}, N))
```

Official source line 17601:

```tex
maps $\Hom_R(F_\bullet, N) \to
\Hom_R(G_\bullet, N)$
```

Replace with:

```tex
maps $\Hom_R(G_\bullet, N) \to
\Hom_R(F_\bullet, N)$
```

## H100B-SOURCE-007 — algebra.tex (mathematical_source_correction)

The induced identity is on the cohomology of the Hom cochain complex, named H^i(alpha) in the displayed construction; H_i(alpha) instead denotes homology of the original chain map.

Official source line 17594:

```tex
$H_i(\alpha)$
```

Replace with:

```tex
$H^i(\alpha)$
```

## H100B-SOURCE-009 — algebra.tex (mathematical_source_correction)

Precomposition reverses order: alpha*:H(G,N)→H(F,N), beta*:H(F,N)→H(G,N); alpha* after beta* equals (beta after alpha)* on H(F,N). The composite beta after alpha is an endomorphism of F and lifts id_M1, so it is homotopic to id_F. The swapped composition is handled by the next sentence.

Official source line 17615:

```tex
H^i(\alpha \circ \beta)
```

Replace with:

```tex
H^i(\beta \circ \alpha)
```

Official source line 17616:

```tex
H^i(\alpha \circ \beta)
```

Replace with:

```tex
H^i(\beta \circ \alpha)
```

Official source line 17617:

```tex
\text{id}_{G_{\bullet}}
```

Replace with:

```tex
\text{id}_{F_{\bullet}}
```

## H100B-SOURCE-011 — algebra.tex (mathematical_source_correction)

Each immediately preceding short exact sequence has endpoints M-prime and M-double-prime. Since the quotient is finite free, the splitting is M≅M-prime⊕M-double-prime. The identical typo occurs in both the PID example and local-ring K0 proof; both loci are explicitly included.

Official source line 13073:

```tex
M' \oplus M'
```

Replace with:

```tex
M' \oplus M''
```

Official source line 13152:

```tex
M' \oplus M'
```

Replace with:

```tex
M' \oplus M''
```

## H100B-SOURCE-013 — homology.tex (copyedit)

The preposition is the ordinary single word instead; no mathematical notation changes.

Official source line 3962:

```tex
in stead of
```

Replace with:

```tex
instead of
```

## H100B-SOURCE-014 — algebra.tex (copyedit)

The subject a commutative diagram is singular.

Official source line 26495:

```tex
there exist a commutative diagram
```

Replace with:

```tex
there exists a commutative diagram
```

## H100B-SOURCE-015 — algebra.tex (copyedit)

The resolution maps have the specified property; to is a typographical substitution for the article.

Official source line 27084:

```tex
have to property that
```

Replace with:

```tex
have the property that
```

## H100B-SOURCE-016 — algebra.tex (mathematical_source_correction)

The proof assumes injectivity at i and shows the quotient with i+1 variables and equations is a field. Its surjective unital map is psi_(i+1), so that map is now injective.

Official source line 27704:

```tex
$\psi_i$
```

Replace with:

```tex
$\psi_{i + 1}$
```

## H100B-SOURCE-017 — algebra.tex (mathematical_source_correction)

alpha_i has target G_i. The outgoing differential there is d_(G,i):G_i→G_(i-1); d_(G,i-1) is not composable with alpha_i.

Official source line 17466:

```tex
d_{G, i-1} \circ \alpha_i
```

Replace with:

```tex
d_{G, i} \circ \alpha_i
```

## H100B-SOURCE-018 — algebra.tex (copyedit)

Single-word spelling in the Ext-definition footnote; the line break before of remains.

Official source line 17562:

```tex
in stead
```

Replace with:

```tex
instead
```

## H100B-SOURCE-019 — algebra.tex (copyedit)

Supply the infinitival to in Choose beta to be a map.

Official source line 17610:

```tex
be a map inducing
```

Replace with:

```tex
to be a map inducing
```
