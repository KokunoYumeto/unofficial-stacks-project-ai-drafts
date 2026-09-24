# Normal algebraic decomposition: primary proof review

Authority: Stacks Project `fields.tex`, commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256 `87E07F0373DC60CFC284E2F19078BC9BC7AB0B89C40EEF83941F6C38C765C549`, lemma-normal-case at lines 3665–3681. Received report OCC-11983 concerns the tensor-product map. This is a primary-session derivation and review, not a human or independent-worker check. It completes the source's omitted proof; no novelty is claimed.

## Exact proof checks

The complete source fragment is `FIELDS_NORMAL_DECOMPOSITION_PROOF_20260925.tex`.

- The separable part is the source's actual subfield of separable elements, rather than a substituted abstract copy. Lemma-separable-first (1703–1724) supplies it and the purely inseparable upper extension. Lemma-separable-first-normal (1861–1876) makes its lower extension normal. No finiteness is assumed.
- For the fixed field N, every conjugate of an element a is in E by normality. Evaluation on F[T]/(f) gives the embedding sending a to a chosen conjugate. Lemma-lift-maps (1945–1979), with L=E, M=F(a), K=F, supplies the automorphism. Thus all distinct roots coincide. The irreducible-polynomial dichotomy (1130–1162) and injectivity and surjectivity of Frobenius on the algebraic closure prove pure inseparability, including the characteristic-zero identity case of definition-purely-inseparable (1580–1593). The previously proposed repair of the dichotomy proof is retained in the same review.
- The finite orbit polynomial proves separability over N without assuming E/F finite or its automorphism group finite. Normality goes up by lemma-normal-goes-up (1837–1848). Thus E/N is Galois under exactly the source hypotheses.
- The compositum C=SN lies inside the original E. Its upper extension is both separable and purely inseparable. The minimal polynomial calculation with T^q-a^q=(T-a)^q proves E=C, including multiplicities and characteristic zero.
- The multiplication map is explicitly balanced over F. Its image is a field by lemma-subalgebra-algebraic-extension-field (785–804), so the compositum calculation proves surjectivity.
- Injectivity uses only finite separable subextensions L/F of S/F, the primitive-element theorem (2300–2351), and pure inseparability of N/F. A common power q for the finitely many coefficients yields g(T)^q, with every exponent iq and coefficient b_i^q retained. The Bezout identity for f and f' proves squarefreeness after scalar extension; no irreducibility over N is assumed in advance. Unique factorization in N[T] then proves f=g. The displayed mutually inverse quotient/tensor maps prove injectivity at each finite stage. An arbitrary tensor has finite support and lifts to one such stage, so the proof covers infinite extensions.

The authority's equality is customary identification notation; that notation alone does not falsify the theorem. The correction specifies the actual map and supplies its proof. The original conclusion remains true.

## Further consequences and generality

These are established consequences of the proof, recorded separately from the received erratum. They are not additional claims of original research and are not silently inserted into the correction as new theorems.

1. **Normality is unnecessary for the linear-disjointness step.** Let S/F be any separable algebraic extension and N/F any purely inseparable extension embedded in one field Omega. Every tensor uses a finite separable subextension L/F. The preceding argument with f, g and q proves that multiplication L tensor_F N to LN is injective. Finite support then proves injectivity for S tensor_F N. Its image is an algebraic F-subalgebra of Omega, hence a field by the cited subalgebra lemma, containing S and N. It equals the compositum SN. This proves the canonical multiplication isomorphism S tensor_F N to SN without normality of either separable extension or ambient field.

2. **The factors meet exactly in F.** If a belongs to S intersect N, its minimal polynomial over F is separable. In positive characteristic it also divides T^q-a^q for some q=p^r and a^q in F, so it has just one distinct root and hence degree one. In characteristic zero N=F. Thus S intersect N=F in all cases.

3. **Both degrees are preserved, including infinite cardinals.** Let (s_i) indexed by I be an F-basis of S. Every element of S tensor_F N is a finite N-linear combination of s_i tensor 1. Apply each F-coordinate functional lambda_i:S to F, tensored with the identity of N, to a finite relation to see that every coefficient is zero. Multiplication therefore transports this basis to an N-basis of SN and [SN:N]=[S:F]. Repeating the same argument with an F-basis of N proves [SN:S]=[N:F]. No cancellation of infinite cardinal products is used.

4. **The normal decomposition canonically identifies the Galois groups.** Now take the original normal E/F and its S and N. Every F-automorphism of E fixes N pointwise and preserves S, since separability of an element over F is invariant under F-automorphisms. Restriction defines r:Aut_F(E)=Gal(E/N) to Gal(S/F). For sigma in Gal(S/F), define its extension by mu composed with (sigma tensor id_N) composed with mu inverse. This is an automorphism of E fixing N and restricting to sigma on S. Conversely, multiplication generates E from S and N, so the extension is unique. The displayed formulas give inverse group homomorphisms, not just a comparison of orders.

   With both Galois groups given their source pointwise-convergence profinite topologies, r is continuous: agreement on any finite subset of S is the same finite evaluation condition in E. For its inverse, express each element of a finite subset X of E as a finite sum of products s_ij n_ij. The extension's value on every element of X depends only on the finitely many values sigma(s_ij), since n_ij is fixed. Evaluation and the finite field operations into the discrete E are continuous. This proves continuity of the inverse, hence the exact isomorphism of profinite groups. The relevant topology is lemma-galois-profinite at 2858–2948, not a topology on an unspecified abstract automorphism group.

## Receiving uses

A bounded root-TeX reference search found three external uses of fields-lemma-normal-case. Their full receiving paragraphs were read.

- `algebra.tex:46182` uses the purely inseparable lower extension and separable upper extension to prove finiteness of integral closure. Both conclusions and their actual subfields are preserved.
- `more-algebra.tex:33381` writes the residue field as a tensor product with the factors in the reverse order. The exact comparison is multiplication after the symmetry n tensor s maps to s tensor n. Its inverse is that symmetry after mu inverse. It preserves each embedded residue subfield, so its use of conjugates of alpha in the separable factor is unchanged.
- `more-algebra.tex:36044` uses the compositum of a Galois and a purely inseparable extension to construct a filtration. The equality E=SN is proved inside the original field, preserving that use.

No receiving-source edit is required by this map clarification.

The separately reviewed transcendence-basis proof (3397–3420) already proves the stronger extension property A contained in B contained in G. The final intake group promotes that existing proved generality to the lemma statement and fixes the empty-chain case. This implements the user's underclaims directive without inventing a new theorem from an unproved suggestion.
