# Source corrections and exact proof locators

Five findings with thirteen bounded source edits. Complete arguments remain in the separate supplement. AI review and proof work: OpenAI Codex - GPT-6 Astra, Ultra effort. No human review, novelty or official Stacks endorsement is claimed.

## MC-STK-ERR-2466: CC-SERIES-FACTOR

Retain the factor x inverse on the original coefficient a_j.

Complete proof: [evidence/cross-chapter/PROOFS.md](evidence/cross-chapter/PROOFS.md).

Original examples.tex line 1481:

```tex
and since $z_{j + 1} = x^{-1}z_j - a_j = \ldots = f_j(x, x^{-1}, z)$).

```

Corrected reading:

```tex
and since $z_{j + 1} = x^{-1}(z_j - a_j) = \ldots = f_j(x, x^{-1}, z)$).

```

## MC-STK-ERR-2467: CC-FITTING-INDEX

Append the coordinate vectors after the original n-k kernel vectors.

Complete proof: [evidence/cross-chapter/PROOFS.md](evidence/cross-chapter/PROOFS.md).

Original more-algebra.tex line 1385:

```tex
$z'_{n + j'} = (0, \ldots, 0, 1, 0, \ldots, 0) \in K'$. Then we see that

```

Corrected reading:

```tex
$z'_{n - k + j'} = (0, \ldots, 0, 1, 0, \ldots, 0) \in K'$. Then we see that

```

## MC-STK-ERR-2468: CC-CONORMAL-BASE

The conormal quotient is balanced over B=P/I; the original A-balanced tensor can have an extra kernel. The injective conormal map has domain (I/I^2) tensor_B C.

Complete proof: [evidence/cross-chapter/PROOFS.md](evidence/cross-chapter/PROOFS.md).

Original more-algebra.tex line 8502:

```tex
$I/I^2 \otimes_A C = IA[x_s, y_j]/IK$ by right exactness

```

Corrected reading:

```tex
$I/I^2 \otimes_B C = IA[x_s, y_j]/IK$ by right exactness

```

Original more-algebra.tex line 8504:

```tex
$I/I^2 \otimes_A C \to K/K^2$.

```

Corrected reading:

```tex
$I/I^2 \otimes_B C \to K/K^2$.

```

## MC-STK-ERR-2469: BRAUER-PROP-001

Restrict assertion (1) to nonzero A and select a nonzero minimal-dimensional submodule in the proof. Preserve the full generality of (2)-(4).

Complete proof: [evidence/brauer/PROOFS.md](evidence/brauer/PROOFS.md).

Original brauer.tex line 123:

```tex
\item $A$ has a simple module,
```

Corrected reading:

```tex
\item if $A \not = 0$, then $A$ has a simple module,
```

Original brauer.tex line 132:

```tex
Of course (1) follows from (2) since $A$ is a nonzero $A$-module.
```

Corrected reading:

```tex
When $A \not = 0$, assertion (1) follows from (2) applied to the $A$-module $A$.
```

Original brauer.tex line 133:

```tex
For (2), any submodule of minimal (finite) dimension
```

Corrected reading:

```tex
For (2), any nonzero submodule of minimal (finite) dimension
```

## MC-STK-ERR-2470: BRAUER-PROP-002

Use K in the right-simple-module composition rings, retain Mat(n,K) for the explicitly right-acting bicommutant, and identify C opposite with the left-acting H-endomorphism ring. Preserve the correct K opposite in the centralizer matrix presentation at 553.

Complete proof: [evidence/brauer/PROOFS.md](evidence/brauer/PROOFS.md).

Original brauer.tex line 158:

```tex
$A \cong \text{Mat}(n \times n, K^{op})$.
```

Corrected reading:

```tex
$A \cong \text{Mat}(n \times n, K)$.
```

Original brauer.tex line 290:

```tex
$\text{End}_A(M) = K^{op}$.
```

Corrected reading:

```tex
$\text{End}_A(M) = K$.
```

Original brauer.tex line 311:

```tex
we see that $L = K^{op}$. The statement about the center of $L = K^{op}$
```

Corrected reading:

```tex
we see that $L = K$. The statement about the center of $L = K$
```

Original brauer.tex line 411:

```tex
we have $\text{End}_A(M) = K^{op}$, see
```

Corrected reading:

```tex
we have $\text{End}_A(M) = K$, see
```

Original brauer.tex line 413:

```tex
Hence $A \cong B$ implies $K^{op} \cong (K')^{op}$ and we win.
```

Corrected reading:

```tex
Hence $A \cong B$ implies $K \cong K'$ and we win.
```

Original brauer.tex line 546:

```tex
$C = \text{End}_{B \otimes_k L^{op}}(M)$.
```

Corrected reading:

```tex
right multiplication identifies $C^{op}$ with
$\text{End}_{B \otimes_k L^{op}}(M)$.
```
