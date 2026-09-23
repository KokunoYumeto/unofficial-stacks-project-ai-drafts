# Sheaves on Spaces: proposed corrections and clarification

12 proposed changes: 11 copyedits and one clarification of an existing isomorphism and factorization. The complete intake review retains all 146 reports, duplicates, rejected claims and adverse evidence. No new theorem is claimed.

Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.

## MC-STK-ERR-1742 — SHEAVES-RECON-008 (copyedit)

The singular noun collection takes forms. Replace the final relative construction by the category in which the sheaf takes values, preserving the empty-cover explanation.

Official sheaves.tex line 535:

```tex
actually form
```

Replace with:

```tex
actually forms
```

Official sheaves.tex line 537:

```tex
of the category the sheaf has values in.
```

Replace with:

```tex
of the category in which the sheaf takes values.
```

## MC-STK-ERR-1743 — SHEAVES-RECON-012 (copyedit)

Close the parenthetical indexing phrase with a comma, preserving the family of discrete spaces and the counterexample.

Official sheaves.tex line 841:

```tex
for $i \in \mathbf{N}$ be
```

Replace with:

```tex
for $i \in \mathbf{N}$, be
```

## MC-STK-ERR-1744 — SHEAVES-RECON-014 (copyedit)

Insert by before the notation s_x so the sentence correctly relates the germ symbol to its represented equivalence class.

Official sheaves.tex line 926:

```tex
we sometimes denote
```

Replace with:

```tex
we sometimes denote by
```

## MC-STK-ERR-1745 — SHEAVES-RECON-016 (copyedit)

Use the singular verb determines with the head noun pair. The two functions represent the same germ exactly when they agree near x, as already defined.

Official sheaves.tex line 1025:

```tex
functions $f$, $g$ determine
```

Replace with:

```tex
functions $f$, $g$ determines
```

## MC-STK-ERR-1746 — SHEAVES-RECON-019 (clarification)

Let P=A times_B C with projections p_A and p_C. Since F preserves fibre products, F(p_A) identifies with the projection from pairs (a,c) satisfying F(f)(a)=F(g)(c). The image inclusion gives a c for every a, and injectivity of F(g) makes it unique. Thus F(p_A) is bijective, so reflection of isomorphisms makes p_A invertible. Setting t=p_C composed with p_A inverse gives g composed with t=f by the fibre-product identity. Name this exact isomorphism and factorization explicitly.

Official sheaves.tex line 1277:

```tex
Hence $A = A \times_B C$ because $F$ reflects isomorphisms.
```

Replace with:

```tex
Hence the projection $A \times_B C \to A$ is invertible, since $F$ reflects isomorphisms.
```

Official sheaves.tex line 1278:

```tex
The result follows.
```

Replace with:

```tex
Follow its inverse by the projection to $C$ to obtain $t$ with $g \circ t = f$.
```

## MC-STK-ERR-1747 — SHEAVES-RECON-021 (copyedit)

Capitalize the first word of the lemma statement.

Official sheaves.tex line 1419:

```tex
let $X$ be a topological space.
```

Replace with:

```tex
Let $X$ be a topological space.
```

## MC-STK-ERR-1748 — SHEAVES-RECON-022 (copyedit)

End the final proof sentence with a period after the Example reference.

Official sheaves.tex line 1447:

```tex
see also Example \ref{example-application-lemma-image-contained-in}
```

Replace with:

```tex
see also Example \ref{example-application-lemma-image-contained-in}.
```

## MC-STK-ERR-1749 — SHEAVES-RECON-023 (copyedit)

For the fixed inclusion V subset U the display is one projection map. Use the singular noun map with the existing singular verb maps.

Official sheaves.tex line 1492:

```tex
the projection maps
```

Replace with:

```tex
the projection map
```

## MC-STK-ERR-1750 — SHEAVES-RECON-024 (copyedit)

Remove the redundant as why construction and write for the same reason that.

Official sheaves.tex line 1544:

```tex
for the same reason as why
```

Replace with:

```tex
for the same reason that
```

## MC-STK-ERR-1751 — SHEAVES-RECON-029 (copyedit)

The parenthetical adverb however needs its opening comma as well as its existing closing comma.

Official sheaves.tex line 1807:

```tex
The main idea however, is
```

Replace with:

```tex
The main idea, however, is
```

## MC-STK-ERR-1752 — SHEAVES-RECON-072 (copyedit)

All three category-naming clauses lack by after Denote. Inserting it preserves the categories, value types and restriction functors.

Official sheaves.tex line 3972:

```tex
Denote $\Sh(\mathcal{B})$
```

Replace with:

```tex
Denote by $\Sh(\mathcal{B})$
```

Official sheaves.tex line 4109:

```tex
Denote $\Sh(\mathcal{B}, \mathcal{C})$
```

Replace with:

```tex
Denote by $\Sh(\mathcal{B}, \mathcal{C})$
```

Official sheaves.tex line 4229:

```tex
Denote $\textit{Mod}(\mathcal{O}|_\mathcal{B})$
```

Replace with:

```tex
Denote by $\textit{Mod}(\mathcal{O}|_\mathcal{B})$
```

## MC-STK-ERR-1753 — SHEAVES-RECON-086 (copyedit)

Item (4) already specifies the restricted module presheaf, its restricted scalar action and its name. Remove the immediately following claim that this definition is left to the reader.

Official sheaves.tex line 4518:

```tex
We leave a definition of the restriction of presheaves
of modules to the reader. 
```

Replace with:

```tex

```
