# Topology and Introduction: proposed corrections and clarifications

54 proposed changes: 44 copyedits, five clarifications, four notation clarifications and one source correction. These are not 54 new mathematical errors or theorems. The complete intake review retains all 152 reports, duplicates, rejected claims and adverse evidence. One adjacent delimiter typo was independently found during review.

Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.

## MC-STK-ERR-1688 — INTRODUCTION-RECON-001 (copyedit)

Use singular agreement with a key feature while preserving the following hyperlink description.

Official introduction.tex line 41:

```tex
We expect this material to be read online as a key feature are the hyperlinks
```

Replace with:

```tex
We expect this material to be read online, as a key feature is the set of hyperlinks
```

## MC-STK-ERR-1689 — TOPOLOGY-RECON-001 (copyedit)

Restore the finite clause introducing the equivalent neighbourhood conditions.

Official topology.tex line 143:

```tex
In other words, with
```

Replace with:

```tex
In other words, we have
```

## MC-STK-ERR-1690 — TOPOLOGY-RECON-002 (copyedit)

Supply the article before the singular count noun.

Official topology.tex line 204:

```tex
be continuous map
```

Replace with:

```tex
be a continuous map
```

## MC-STK-ERR-1691 — TOPOLOGY-RECON-003 (copyedit)

Repair the independently repeated missing article.

Official topology.tex line 249:

```tex
be continuous map
```

Replace with:

```tex
be a continuous map
```

## MC-STK-ERR-1692 — TOPOLOGY-RECON-006 (copyedit)

Supply the article before the modified singular noun.

Official topology.tex line 555:

```tex
be surjective, open, continuous map
```

Replace with:

```tex
be a surjective, open, continuous map
```

## MC-STK-ERR-1693 — TOPOLOGY-RECON-007 (copyedit)

Supply the article at the parallel closed-map statement.

Official topology.tex line 585:

```tex
be surjective, closed, continuous map
```

Replace with:

```tex
be a surjective, closed, continuous map
```

## MC-STK-ERR-1694 — TOPOLOGY-RECON-008 (copyedit)

The construction Let A requires be.

Official topology.tex line 646:

```tex
$A \subset f(E)$ an open
```

Replace with:

```tex
$A \subset f(E)$ be an open
```

## MC-STK-ERR-1695 — TOPOLOGY-RECON-009 (source_correction)

An unrestricted f-preimage of A can include points outside E. Explicit reduction to E to f(E) makes all later preimages clopen in the connected domain and all existing image equalities correctly typed.

Official topology.tex line 645:

```tex
\begin{proof}
```

Replace with:

```tex
\begin{proof}
Replacing $f$ by its continuous restriction $E \to f(E)$,
we may assume $X = E$ and $Y = f(E)$.
```

## MC-STK-ERR-1696 — TOPOLOGY-RECON-010 (copyedit)

Separate the connectedness premise from the resulting alternative.

Official topology.tex line 741:

```tex
is connected we conclude
```

Replace with:

```tex
is connected, and we conclude
```

## MC-STK-ERR-1697 — TOPOLOGY-RECON-011 (copyedit)

Give the introduced system a grammatical defining clause without asserting uniqueness.

Official topology.tex line 832:

```tex
For all $x\in X$ let write $\mathcal{N}(x)$ the fundamental system of connected
```

Replace with:

```tex
For each $x \in X$, let $\mathcal{N}(x)$ be a fundamental system of connected
```

## MC-STK-ERR-1698 — TOPOLOGY-RECON-012 (copyedit)

Use the nonpersonal antecedent and plural noun.

Official topology.tex line 845:

```tex
each of his point
```

Replace with:

```tex
each of its points
```

## MC-STK-ERR-1699 — TOPOLOGY-RECON-013 (clarification)

The nonempty open intersection meets the dense set in (c). Saying y lies in it makes both intersections with the fibre nonempty.

Official topology.tex line 1131:

```tex
there is a point $y$ which
```

Replace with:

```tex
there is a point $y$ in this intersection
```

Official topology.tex line 1132:

```tex
corresponds to a point of this intersection such that the fibre
```

Replace with:

```tex
such that the fibre
```

## MC-STK-ERR-1700 — TOPOLOGY-RECON-015 (copyedit)

The subject is the singular collection of U-prime.

Official topology.tex line 1199:

```tex
$U'$ form a topology
```

Replace with:

```tex
$U'$ forms a topology
```

## MC-STK-ERR-1701 — TOPOLOGY-RECON-016 (copyedit)

Explicitly bind j and avoid an article directly before the inequality.

Official topology.tex line 1225:

```tex
there is an
```

Replace with:

```tex
there is an index $j$ with
```

## MC-STK-ERR-1702 — TOPOLOGY-RECON-018 (clarification)

Bind X before referring to its closed subsets.

Official topology.tex line 1245:

```tex
A topological space is called
```

Replace with:

```tex
A topological space $X$ is called
```

## MC-STK-ERR-1703 — TOPOLOGY-RECON-023 (copyedit)

Supply be after Let in the first construction and is for the second sequence subject.

Official topology.tex line 1336:

```tex
\mathbf{N}}$ a decreasing sequence
```

Replace with:

```tex
\mathbf{N}}$ be a decreasing chain
```

Official topology.tex line 1341:

```tex
\mathbf{N}}$ a decreasing
```

Replace with:

```tex
\mathbf{N}}$ is a decreasing
```

## MC-STK-ERR-1704 — TOPOLOGY-RECON-026 (copyedit)

Remove the malformed imperative auxiliary.

Official topology.tex line 1580:

```tex
Let suppose
```

Replace with:

```tex
Suppose
```

## MC-STK-ERR-1705 — TOPOLOGY-RECON-027 (copyedit)

Use a transitive verb in the first clause and an adjectival phrase modifying length in the second.

Official topology.tex line 1600:

```tex
equals to
```

Replace with:

```tex
equals
```

Official topology.tex line 1601:

```tex
the same length equals to the
```

Replace with:

```tex
the same length, equal to the
```

## MC-STK-ERR-1706 — TOPOLOGY-RECON-028 (copyedit)

Use the logical-direction term and remove the misplaced colon.

Official topology.tex line 1607:

```tex
For the reciprocal, we show by induction that : if
```

Replace with:

```tex
For the converse, we show by induction that if
```

## MC-STK-ERR-1707 — TOPOLOGY-RECON-029 (copyedit)

Repair plural agreement and identify U_i directly as the open neighbourhoods.

Official topology.tex line 1682:

```tex
then there exists opens $E_i \subset U_i$ with
```

Replace with:

```tex
then there exist open subsets $U_i$ with $E_i \subset U_i$ and
```

## MC-STK-ERR-1708 — TOPOLOGY-RECON-031 (copyedit)

Use the noun complement for the complement of the displayed covering.

Official topology.tex line 1739:

```tex
The complementary is
```

Replace with:

```tex
The complement is
```

## MC-STK-ERR-1709 — TOPOLOGY-RECON-035 (clarification)

Name X before the proof uses it.

Official topology.tex line 1956:

```tex
A quasi-compact locally Noetherian space is Noetherian.
```

Replace with:

```tex
A quasi-compact locally Noetherian space $X$ is Noetherian.
```

## MC-STK-ERR-1710 — TOPOLOGY-RECON-037 (copyedit)

Separate the contradiction apposition from the preceding assertion.

Official topology.tex line 1992:

```tex
U_{i_{j, l}}$ a contradiction.
```

Replace with:

```tex
U_{i_{j, l}}$, a contradiction.
```

## MC-STK-ERR-1711 — TOPOLOGY-RECON-040 (notation_clarification)

Name j explicitly as the varying index in the finite family grouped by i.

Official topology.tex line 2102:

```tex
\bigcup_{i = i(x_j)}
```

Replace with:

```tex
\bigcup_{j : i(x_j) = i}
```

## MC-STK-ERR-1712 — TOPOLOGY-RECON-041 (clarification)

Explicitly name the displayed summands that become V-prime_k in the refinement.

Official topology.tex line 2166:

```tex
in the empty set and the other opens $V_{j_0, k}$ of the RHS
```

Replace with:

```tex
in the empty set. Write $V_{j_0, k} = V_{j_0} \cap W_{i_0 \ldots i_p, k}$
for $k \in K$. These other opens on the RHS
```

## MC-STK-ERR-1713 — TOPOLOGY-RECON-045 (copyedit)

Correct the past-tense verb.

Official topology.tex line 2300:

```tex
where arbitrary
```

Replace with:

```tex
were arbitrary
```

## MC-STK-ERR-1714 — TOPOLOGY-RECON-047 (copyedit)

Use singular agreement with basis and the idiom is given by.

Official topology.tex line 2388:

```tex
A basis for the topology of $\prod X_i$ are
```

Replace with:

```tex
A basis for the topology of $\prod X_i$ is given by
```

## MC-STK-ERR-1715 — TOPOLOGY-RECON-048 (copyedit)

Use the article matching the pronunciation of i.

Official topology.tex line 2417:

```tex
pick a $i
```

Replace with:

```tex
pick an $i
```

## MC-STK-ERR-1716 — TOPOLOGY-RECON-049 (copyedit)

Use the correct article before point.

Official topology.tex line 2463:

```tex
choose an point
```

Replace with:

```tex
choose a point
```

## MC-STK-ERR-1717 — TOPOLOGY-RECON-051 (copyedit)

Delete the duplicated article.

Official topology.tex line 2559:

```tex
and a the terminology
```

Replace with:

```tex
and the terminology
```

## MC-STK-ERR-1718 — TOPOLOGY-RECON-054 (clarification)

Retain explicitly the nonemptiness supplied by assumption (2), so Y minus V is a proper closed subset when minimality is invoked.

Official topology.tex line 2930:

```tex
contains an open $V$
```

Replace with:

```tex
contains a nonempty open $V$
```

## MC-STK-ERR-1719 — TOPOLOGY-RECON-055 (copyedit)

Repair the two existential clauses with plural opens.

Official topology.tex line 3047:

```tex
there exists opens
```

Replace with:

```tex
there exist opens
```

Official topology.tex line 3063:

```tex
there exists opens
```

Replace with:

```tex
there exist opens
```

## MC-STK-ERR-1720 — TOPOLOGY-RECON-056 (copyedit)

Correct the spelling of the French reference label.

Official topology.tex line 3105:

```tex
Corrolaire
```

Replace with:

```tex
Corollaire
```

## MC-STK-ERR-1721 — TOPOLOGY-RECON-058 (copyedit)

The M set-builder has a stray closing parenthesis after U_i^c. The coordinate pair (J,x) already closes before the separator, and no other opening parenthesis occurs.

Official topology.tex line 3129:

```tex
U_i^c)\}
```

Replace with:

```tex
U_i^c\}
```

## MC-STK-ERR-1722 — TOPOLOGY-RECON-060 (copyedit)

Supply the article for the fixed map.

Official topology.tex line 3177:

```tex
Assume map
```

Replace with:

```tex
Assume the map
```

## MC-STK-ERR-1723 — TOPOLOGY-RECON-061 (copyedit)

Repair the missing and mistyped articles.

Official topology.tex line 3344:

```tex
be closed subset
```

Replace with:

```tex
be a closed subset
```

Official topology.tex line 3345:

```tex
be and open subset
```

Replace with:

```tex
be an open subset
```

## MC-STK-ERR-1724 — TOPOLOGY-RECON-062 (copyedit)

Delete the duplicated copula.

Official topology.tex line 3468:

```tex
is is finite
```

Replace with:

```tex
is finite
```

## MC-STK-ERR-1725 — TOPOLOGY-RECON-063 (copyedit)

Name the three preserved subclasses of the displayed collection directly.

Official topology.tex line 3490:

```tex
the subsets of locally closed, of open and of closed subsets.
```

Replace with:

```tex
the classes of locally closed, open, and closed subsets.
```

## MC-STK-ERR-1726 — TOPOLOGY-RECON-065 (copyedit)

Separate the two clauses and give the singular specialization variable a matching quantifier phrase.

Official topology.tex line 3580:

```tex
subset of $X$, if
```

Replace with:

```tex
subset of $X$. If
```

Official topology.tex line 3581:

```tex
Thus for all
```

Replace with:

```tex
Thus for every
```

## MC-STK-ERR-1727 — TOPOLOGY-RECON-067 (copyedit)

Use a condition-introducing conjunction and plural agreement.

Official topology.tex line 3638:

```tex
such as
```

Replace with:

```tex
such that
```

Official topology.tex line 3644:

```tex
specialization lift
```

Replace with:

```tex
specializations lift
```

## MC-STK-ERR-1728 — TOPOLOGY-RECON-068 (copyedit)

Match the lemma's plural lifting-property wording.

Official topology.tex line 3662:

```tex
specialization lift
```

Replace with:

```tex
specializations lift
```

## MC-STK-ERR-1729 — TOPOLOGY-RECON-070 (copyedit)

Restore the inclusion sign between the ellipsis and the final member of the chain.

Official topology.tex line 3775:

```tex
\subset \ldots Z_e
```

Replace with:

```tex
\subset \ldots \subset Z_e
```

## MC-STK-ERR-1730 — TOPOLOGY-RECON-075 (notation_clarification)

Make explicit the open complements used to conclude that U lies in both closed nowhere dense sets and hence is empty.

Official topology.tex line 4015:

```tex
U \setminus U \cap \overline{B}
```

Replace with:

```tex
U \setminus (U \cap \overline{B})
```

Official topology.tex line 4017:

```tex
U \setminus U \cap \overline{A}
```

Replace with:

```tex
U \setminus (U \cap \overline{A})
```

## MC-STK-ERR-1731 — TOPOLOGY-RECON-082 (notation_clarification)

Explicitly group the rectangular neighbourhood before intersecting it with Z in the product.

Official topology.tex line 4583:

```tex
Z \cap U \times V
```

Replace with:

```tex
Z \cap (U \times V)
```

## MC-STK-ERR-1732 — TOPOLOGY-RECON-083 (copyedit)

Use singular agreement and the same basis idiom as the earlier product-topology repair.

Official topology.tex line 4594:

```tex
A basis of the topology of $X \times Y$ are
```

Replace with:

```tex
A basis of the topology of $X \times Y$ is given by
```

## MC-STK-ERR-1733 — TOPOLOGY-RECON-085 (copyedit)

Supply the missing ambient-space preposition.

Official topology.tex line 4754:

```tex
quasi-compact opens $X'$
```

Replace with:

```tex
quasi-compact opens of $X'$
```

## MC-STK-ERR-1734 — TOPOLOGY-RECON-087 (notation_clarification)

Show explicitly that each object of the inverse system is the set difference, closed in the constructible topology.

Official topology.tex line 4851:

```tex
\lim_{a : j \to i} f_a^{-1}(E) \setminus f_a^{-1}(F)
```

Replace with:

```tex
\lim_{a : j \to i} (f_a^{-1}(E) \setminus f_a^{-1}(F))
```

## MC-STK-ERR-1735 — TOPOLOGY-RECON-088 (copyedit)

Two indexed families of arrows are introduced, requiring the plural noun.

Official topology.tex line 4894:

```tex
and morphism
```

Replace with:

```tex
and morphisms
```

## MC-STK-ERR-1736 — TOPOLOGY-RECON-089 (copyedit)

A basis here consists of the indicated open subsets, not one singular open.

Official topology.tex line 4922:

```tex
by the quasi-compact open,
```

Replace with:

```tex
by the quasi-compact opens,
```

## MC-STK-ERR-1737 — TOPOLOGY-RECON-092 (copyedit)

Supply the conventional designation preposition.

Official topology.tex line 5139:

```tex
and denote $\beta(X)$ the closure
```

Replace with:

```tex
and denote by $\beta(X)$ the closure
```

## MC-STK-ERR-1738 — TOPOLOGY-RECON-096 (copyedit)

Use the imperative to select a preimage in the standalone sentence.

Official topology.tex line 5367:

```tex
Writing $x = f(y)$
```

Replace with:

```tex
Write $x = f(y)$
```

## MC-STK-ERR-1739 — TOPOLOGY-RECON-098 (copyedit)

Remove the stray article before the named identity map.

Official topology.tex line 5427:

```tex
Thus the $\text{id}_E$
```

Replace with:

```tex
Thus $\text{id}_E$
```

## MC-STK-ERR-1740 — TOPOLOGY-RECON-099 (copyedit)

Repair the comparative idiom.

Official topology.tex line 5448:

```tex
bigger or equal than
```

Replace with:

```tex
greater than or equal to
```

## MC-STK-ERR-1741 — TOPOLOGY-RECON-103 (copyedit)

Repair plural agreement in all three parallel product-limit proofs.

Official topology.tex line 5771:

```tex
products commutes
```

Replace with:

```tex
products commute
```

Official topology.tex line 5928:

```tex
products commutes
```

Replace with:

```tex
products commute
```

Official topology.tex line 5985:

```tex
products commutes
```

Replace with:

```tex
products commute
```
