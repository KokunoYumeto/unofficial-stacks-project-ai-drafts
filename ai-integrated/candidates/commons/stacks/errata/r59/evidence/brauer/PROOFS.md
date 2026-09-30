# Brauer Groups: source review and propagation of the received corrections

Source: The Stacks Project authors, `brauer.tex`, authority commit
`a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256
`B2504820D769EBE4E9E33B8ADD78753FB30ACA6E8A7F75C8D54DDA885EDCD682`.
The retained original TeX has 817 lines; all were read for this review.
The twelve received reports and ten existing source operations are retained
separately. This note supplies editorial arguments and propagation findings.
It does not silently replace the source or claim a new research theorem.

## 1. The module and multiplication conventions

The source defines modules to be unital **right** modules at lines 33–37.
In its Rieffel proof, lines 100–106, the endomorphisms of a right module act
on the left, whereas endomorphisms of the resulting left module are made
to act on the right. Its footnote explicitly reverses multiplication in
the latter ring. We retain both conventions and distinguish their maps.

Write `End^comp` for endomorphisms multiplied by composition,
`f g = f ∘ g`. Write `End^right` for the same functions with multiplication
`f ⋆ g = g ∘ f`. The identity on functions is an isomorphism
`End^right ≅ (End^comp)^op`, not an isomorphism to `End^comp` in general.
Thus the source's first commutant is `End_A^comp(M)`, acting on the left,
and its bicommutant is `End_L^right(M)`, acting on the right.

For the right action of any ring A, define `R_a(m)=ma`. Then

    (R_a ∘ R_b)(m) = (mb)a = m(ba) = R_{ba}(m),
    (R_a ⋆ R_b)(m) = (ma)b = m(ab) = R_{ab}(m).

Consequently the original action is a homomorphism into `End^right`
and an antihomomorphism into `End^comp`. No opposite algebra can be removed
or introduced without checking this multiplication.

## 2. Matrix corners and the two inverse module maps

This checks `MC-STK-ERR-0745` against source lines 259–278. Let R be the
original possibly noncommutative ring, let `n≥1`, and put
`R_n=Mat(n×n,R)`. Denote the matrix units by `e_ij`; for `r∈R`,
`r e_ij` denotes the matrix with r in position `(i,j)` and zero elsewhere.
The multiplication formula, with the factors in their original order, is

    (r e_ij)(s e_uv) = δ_ju (rs)e_iv.

Let J be a two-sided ideal of R_n. The additive sum
`J=⊕_{1≤i,j≤n} e_ii J e_jj` is direct because its summands have disjoint
matrix positions. Put `I={r∈R : r e_11∈J}`. Addition, additive inverses,
and multiplication on either side by `s e_11` prove that I is a two-sided
ideal of R. For every pair i,j, the two identities

    e_i1 (r e_11)e_1j = r e_ij,
    e_1i (r e_ij)e_j1 = r e_11

prove `e_ii J e_jj={r e_ij:r∈I}`. The inverse maps between this corner
and I take r to `r e_ij` and extract its `(i,j)` coefficient. They do not
identify different corners as subsets of the matrix ring. Summing the
corners proves `J=I R_n`. The retained source correction expresses precisely
this common coefficient ideal; its unexpanded direct-sum notation has the
unique available pair of indices and is not another defect.

For completeness, the source's equivalence of right-module categories is
given by actual inverse maps. Regard `X^⊕n` as rows over a right R-module X,
with `(xU)_j=Σ_i x_i u_ij`. Conversely take `Y e_11` for a right R_n-module Y,
with its R-action through `r↦r e_11`. Define

    α_Y : (Y e_11)^⊕n → Y,       (y_i)_i ↦ Σ_i y_i e_1i,
    β_Y : Y → (Y e_11)^⊕n,       y ↦ (y e_i1)_i.

The entries of β lie in `Y e_11` since `e_i1 e_11=e_i1`. The relations
`e_1j e_i1=δ_ji e_11` and `Σ_i e_i1 e_1i=Σ_i e_ii=1` give
`β_Y α_Y=id` and `α_Y β_Y=id`. Matrix multiplication verifies that these
are right R_n-module maps. The analogous identification
`(X^⊕n)e_11→X` extracts the first entry and its inverse inserts zeros.
All these maps commute with module homomorphisms, so they give the stated
equivalence, including for modules which are not finitely generated.

Commutation with every `e_ii` forces a central matrix to be diagonal;
commutation with every `e_ij` makes its diagonal entries equal. Commutation
with `r e_11` for every r then forces that common entry into `Z(R)`.
Conversely each such scalar matrix is central. This proves the exact
center map `Z(R)→Z(R_n), r↦r·1_n`, with inverse taking entry `(1,1)`.

## 3. The zero-algebra correction does not yet reach every dependent statement

The ten existing corrections include `MC-STK-ERR-0746`, requiring a simple
algebra to be nonzero at source lines 63–64. This is necessary: the zero
algebra satisfies the printed two-sided-ideal condition, but cannot be
a positive-size matrix algebra over a skew field, whose identity is nonzero.

However, the separate lemma at lines 119–138 assumes only that A is finite,
not that A is simple. Its assertion (1), that A has a simple module, is
still false for A=0 after the definition of “simple algebra” is repaired.
For a unital module over the zero algebra, every m satisfies
`m=m·1=m·0=0`. Therefore all such modules are zero and none is simple.

The precise correction restricts **assertion (1)** to `A≠0`; assertions
(2)–(4) remain valid for every finite algebra, including zero. Their full
argument is as follows. In any nonzero right A-module N, choose `m≠0`.
Then `m=m1` belongs to the cyclic submodule mA, which is a nonzero quotient
of the finite-dimensional k-vector space A. Among nonzero submodules of mA
choose one of least positive k-dimension, called M. Any nonzero proper
submodule of M would have smaller positive dimension, so M is simple.
This proves (2). Applying (2) to the module A proves (1) when A is nonzero.
Conversely existence of a simple unital A-module implies A is nonzero by
the preceding zero-algebra calculation.

If M is simple, any `m≠0` generates it, since `0≠mA⊂M`. Hence M is a
quotient of A and has finite k-dimension, proving (3). Finally a nonzero
A-endomorphism f of M has kernel zero and image M, since its kernel and
image are submodules. It is bijective, and its inverse is A-linear:
if `f(x)=m`, then `f(xa)=ma`, so `f^{-1}(ma)=f^{-1}(m)a`.
The identity of M is nonzero. Thus `End_A^comp(M)` is a skew field,
proving (4). This last argument requires no finiteness assumption at all;
the general Schur assertion is a proved underclaim recorded editorially.

The word “nonzero” is also needed before “submodule of minimal (finite)
dimension” in the proof at line 133: among all submodules, zero has the
smallest dimension. This is a bounded repair of the stated minimization.

Downstream: the construction of a simple submodule of a finite simple A
in Wedderburn's proof is now valid because the corrected definition already
gives `A≠0`. No new hypothesis is needed in that theorem or in its later
uses. The unrelated zero-module exception in assertion (6) at lines
295–296 is correctly excluded by existing `MC-STK-ERR-0747`.

## 4. The exact endomorphism rings of the original right matrix module

Retain the source's `A=Mat(n×n,K)` and its right module `M=K^⊕n`, with
row action. For each a∈K let `L_a(v_1,…,v_n)=(av_1,…,av_n)`.
Associativity shows `L_a(vU)=L_a(v)U`, so L_a is A-linear. Moreover

    L_a ∘ L_b = L_{ab}.

Every A-linear f is of this form. If ε_i is the i-th unit row, then
`ε_i e_ii=ε_i` implies f(ε_i) has only its i-th entry, say a_i.
The equation `ε_i e_ij=ε_j` gives `a_i=a_j` for every pair. Write their
common value a. Using the matrix with r in diagonal position `(i,i)` gives
`f(r ε_i)=ar ε_i`. Additivity now gives f=L_a on every row. Evaluation
on ε_1 supplies the inverse to `a↦L_a`. Thus the exact ring isomorphism is

    K → End_A^comp(M),             a ↦ L_a,

and its target is K, not K^op, under the source's left action convention.
The formula is compatible with the central k-actions on both sides.

Now let M be a left K-vector space with ordered basis ε_1,…,ε_n, retaining
coefficients on the left. A left K-linear map is determined by
`t(ε_i)=Σ_j u_ij ε_j` and sends the coefficient row v to vU.
Let t_U denote this map. Direct multiplication gives

    t_U ∘ t_V = t_{VU},            t_U ⋆ t_V = t_{UV}.

Consequently `End_K^right(M)≅Mat(n×n,K)` by `t_U↦U`, whereas
`End_K^comp(M)≅Mat(n×n,K^op)` by `t_U↦(u_ji^op)_{i,j}`.
The latter transpose retains every entry and reverses multiplication
inside K; it is not a change in the original action.

This proves that the final line 158 of the source's Wedderburn proof,
which uses its explicitly defined right-acting bicommutant, should have
`Mat(n×n,K)`, with the original `K=End_A^comp(M)`. Likewise the expressions
`End_A(M)=K^op` at lines 290 and 411 and `L=K^op` at line 311 are
inconsistent with that same convention. The correct identifications there
use K. The uniqueness proof at line 413 then directly gives `K≅K'`.
The theorem that a finite simple algebra is some matrix algebra over a
skew field remains true; the error is in the explicitly named division
algebra and its action, not in the existential classification.

The order discrepancy is substantive even without finding a division
algebra abstractly nonisomorphic to its opposite. As an explicit witness,
inside `Mat(2×2,C)` put

    I = diag(i,-i),     J = [[0,1],[-1,0]],     Q = IJ.

Their real span with the identity is an associative real algebra because
it is closed under multiplication, with `I²=J²=-1` and `JI=-IJ`.
The four matrices are linearly independent over R. For
`h=a+bI+cJ+dQ`, multiplication by `h̄=a-bI-cJ-dQ` in either order gives
`(a²+b²+c²+d²)·1`. Every nonzero h is therefore invertible. In this
skew field, `L_I∘L_J=L_Q`, while multiplication of I and J in the opposite
ring gives `JI=-Q`, which would map to `-L_Q`. These are unequal because
`2Q≠0`. Thus the source's unmodified left action cannot identify its
composition ring with K^op by the claimed coefficient assignment.

## 5. Bicommutants, including the missed generality for the module

For the finite case in source lines 280–317 write
`A=Mat(n×n,K)`, `M=K^⊕n`, and `N=M^⊕r`, where r is the actual number
of simple summands. For `r≥1`, an A-linear endomorphism of N is a matrix
`(b_ij)∈Mat(r×r,K)` acting by
`(v_j)_j↦(Σ_j b_ij v_j)_i`. The calculation in Section 4 proves both
that every endomorphism has these entries and that composition is ordinary
matrix multiplication. Hence

    B=End_A^comp(N) ≅ Mat(r×r,K)=Mat(r×r,L),   L=End_A^comp(M)≅K.

The right action of A identifies A with `End_B^right(N)`. Here is a proof
which also establishes the exact stronger statement for **every nonzero
right A-module N**, without requiring N finite.

The inverse equivalences in Section 2, with R=K, identify N with
`(N e_11)^⊕n`. Choose a basis of the right K-vector space `N e_11`.
Writing its index set as T gives an A-module isomorphism
`N≅⊕_{t∈T} M_t`, where each `M_t=M`, and every element has finite support.
The set T is nonempty because N is nonzero. This is an explicit direct
sum of the original simple right matrix modules, with no finiteness
restriction on T.

Put `B=End_A^comp(N)`. Suppose F is an additive map commuting with all
of B. For each t, the projection onto M_t belongs to B, so F preserves
each M_t. The A-linear map which transfers the row in M_t to M_u and
annihilates the other summands also belongs to B. Commutation with these
maps shows that the restrictions of F are one and the same additive
map `f:M→M`, under the displayed identifications. For every a∈K, the map
which applies L_a to a single summand and is zero on all others belongs
to B. Therefore `f(av)=a f(v)`: f is left K-linear.
Section 4 now gives a unique matrix `U∈Mat(n×n,K)` with `f(v)=vU`.
On an arbitrary finite-support element `(v_t)`, additivity and the
projections give `F((v_t))=(v_t U)`. Thus F is exactly the original right
action R_U on N. Conversely every R_U commutes with every A-linear map
by the definition of A-linearity. The action is faithful: if R_U is zero,
apply it to each unit row in any one nonempty summand to read off all
entries of U. The multiplication calculation in Section 1 proves

    A ≅ End_B^right(N),     A^op ≅ End_B^comp(N).

For N=0 the target is the zero ring, so neither can recover nonzero A.
This proves both the necessity of the existing nonzero correction and the
editorial underclaim: finiteness of N is unnecessary for the bicommutant
conclusion. It is still needed for the accompanying description of B as
a finite-size matrix algebra. No change to that finite-matrix assertion
is inferred from the stronger bicommutant conclusion.

The dimensions in assertion (5) remain exactly
`[A:k]=n²[K:k]`, `[L:k]=[K:k]`, `dim_k(M)=n[K:k]`, and hence
`[A:k][L:k]=dim_k(M)²`. The centers of A and L identify with Z(K) by
the explicit scalar-matrix map of Section 2.

## 6. Propagation through Skolem–Noether and the centralizer argument

This checks the mathematical qualification in `MC-STK-ERR-0748` and the
explicit multiplication map in `MC-STK-ERR-0749`.

In the source Skolem–Noether proof retain the right A-module M and
`L=End_A^comp(M)`, acting on its left. For embeddings f,g:B→A, the two
right actions of `H=B⊗_k L^op` are

    m·_1(b⊗l^op)=l m f(b),         m·_2(b⊗l^op)=l m g(b).

For example, applying `(b_1⊗l_1^op)` and then `(b_2⊗l_2^op)` gives
`l_2 l_1 m f(b_1)f(b_2)`, exactly the action of their product in H.
Their k-dimensions are equal. The source's finite simple classification
therefore supplies an H-module isomorphism φ from the first action to
the second. Its L-linearity identifies it with `R_x` for x∈A by the
bicommutant result. Its inverse is `R_y` for y∈A, so faithfulness gives
`xy=yx=1`. Intertwining the B-actions gives `f(b)x=xg(b)`, hence
`f(b)=xg(b)x^{-1}`. The opposite on L is essential and stays in this proof.

Taking B=A, f a k-algebra automorphism, and g the identity proves the
corrected inner-automorphism assertion. Without “k-algebra”, take k=C,
A=C, and complex conjugation. It is a unital ring automorphism which is
not the identity. Every inner automorphism of the commutative field C
is the identity, so the unqualified ring assertion would be false.

For the centralizer theorem retain the source's
`H=B⊗_k L^op` acting on the right of M and `C=Cent_A(B)`.
The assignment `c↦R_c` takes C into `End_H^comp(M)`. It is bijective:
an H-linear map commutes with L, so the A-bicommutant identifies it with
some R_a; commutation with the B-action says `ba=ab` for every b,
by faithfulness of M. Thus a∈C. But composition is reversed:
`R_c∘R_d=R_{dc}`. The exact identification in source line 546 is therefore

    C^op ≅ End_H^comp(M).

If `H=Mat(m×m,K)` and M is a direct sum of n copies of its right simple
module `K^⊕m`, Section 5 gives `End_H^comp(M)≅Mat(n×n,K)`.
Taking opposites and the entrywise transpose gives
`C≅Mat(n×n,K^op)`. **The opposite in source line 553 is correct and must
be retained.** It differs from the incorrect occurrences in the right
simple module's left-acting endomorphism ring. All original dimension
formulas at lines 556–558 remain unchanged:

    dim_k(M)=nm[K:k],      [B:k][L:k]=m²[K:k],
    [C:k]=n²[K:k],         [A:k][L:k]=dim_k(M)².

Since `[L:k]>0`, substitution and cancellation of that nonzero integer
give `[A:k]=[B:k][C:k]`. The source double-centralizer conclusion follows
from `B⊂Cent_A(C)` and applying this formula to C; equality of the finite
k-dimensions makes the inclusion surjective.

When B is central, `Z(C)=C∩Cent_A(C)=C∩B=Z(B)=k`.
The map in the existing corrected tensor statement is

    μ:B⊗_k C→A,                  μ(b⊗c)=bc.

It is well defined by k-balance. It is multiplicative since C commutes
with B: `(bc)(b'c')=bb'cc'`. It takes the identity to the nonzero identity
of A. Its domain is simple by the source tensor-simplicity lemma, so its
kernel is zero. Its domain and codomain have the same finite dimension
by the formula just proved, so μ is an isomorphism. This supplies the
exact map rather than treating distinct presentations as unrelated.
The source's equality was usable as a customary canonical identification;
the existing edit is recorded as a clarification making that map explicit,
not as a new counterexample to the theorem.

## 7. The corrected separability negation and its receiving argument

Both producer reports at source line 733 refer to existing
`MC-STK-ERR-0017`. The sought element at lines 724–726 belongs to `K\k`
and is separable over k. Its negation is that no element of `K\k` is
separable, not that K has no separable element at all. Every a∈k has
minimal polynomial `T-a`, whose derivative is 1, so the latter statement
is always false. Existing `MC-STK-ERR-0016` independently repairs the
spelling of “splitting field” at line 711. These are two shared mathematical
loci, each reported twice; they are not four distinct corrections.

The corrected negation really does give the next assertion in the proof.
In characteristic p>0, let f be the monic irreducible polynomial of x∈K.
Repeatedly remove powers of p from every exponent until
`f(T)=g(T^{p^r})` with `g'≠0`. The polynomial g is irreducible, since a
factorization of g would give one of f. Therefore it is separable, and
`y=x^{p^r}` is separable over k. The corrected assumption forces y∈k.
Since g is the monic irreducible polynomial of y, `g(U)=U-y`; thus
`f(T)=T^{p^r}-y`. Its degree `p^r` is at most `[K:k]`. Choose a p-power
q at least `[K:k]`. Each such `p^r` divides q, hence `x^q∈k` for every x.

With the original basis `a_1=1,a_2,…,a_n`, write every ordered product
`a_{i_1}…a_{i_q}=Σ_j c^j_{i_1,…,i_q}a_j`, keeping all q factors.
Then the coordinate polynomials in the source are exactly

    f_j(X_1,…,X_n)=Σ_{1≤i_1,…,i_q≤n}
                      c^j_{i_1,…,i_q} X_{i_1}…X_{i_q}.

For j≥2 they vanish on all k^n. Over the infinite field k this implies
they are the zero polynomials: induct on the number of variables, using
that a nonzero one-variable polynomial has at most its degree many roots
and applying that assertion to each coefficient. Their vanishing therefore
persists over the algebraic closure. The resulting matrix algebra has
size at least 2, since `K≠k` and `[K:k]=d²`. Its element e_11 has
`e_11^q=e_11`, and is not central because
`e_11 e_12=e_12` whereas `e_12 e_11=0`. This is the required contradiction.

The existing punctuation edits at lines 561 and 728 and article insertion
at line 771 preserve all mathematical assertions. No change to those
already-admitted operations is required by this review.

## 8. Scope and remaining integration

The ten existing corrections replay exactly to the current complete
`brauer.tex`; all twelve received reports have been compared with their
actual source operations. The separate zero-algebra lemma and the
endomorphism-order propagation above are new findings from this review.
Their bounded edits and this complete editorial argument require their
own prepared source record and later admission. Neither reading the
chapter nor proving these comparisons is a publication receipt.

The stronger Schur and nonzero-module bicommutant conclusions are proved
editorial underclaims. They do not authorize replacing the source's
finite-module exposition. The later joint synthesis and novelty review
remain after the core correction work. No claim about the separately
received open Brauer problem or its proposed solution is made here.
