# Independent check of the replacement localization proof

Date: 2026-09-24. Scope: mathematical verification only; no source edits, packaging, or publication.

**Verdict: the complete replacement fragment is mathematically valid. No change to the fragment is required.** Its first invocation of the preceding forward implication is not circular.

## Exact artifact and reading bounds

- Fragment: `STACKS_LOCALIZED_CARTESIAN_PROOF_20260924.tex` in this control directory.
- SHA-256: `70fce1119beed9a374306e537f7e35bb6dce319030e3995bf31d66b3e5c70d87`.
- Size: 6,814 bytes; 166 lines.
- Every line 1–166 was read in the present check; the tool output was complete.
- Original context reread: `stacks.tex` 2982–3148 at authority `a04446e57ec1fbc252a871afcec7752fb2807b14`, including the original statement, the complete forward existence and uniqueness argument, the omitted-converse paragraph, and the final chosen-lift argument.
- The mathematical comparison is with Sections 4–6 of `LOCALIZED_CARTESIAN_DERIVATION_20260924.md`, SHA-256 `1ac4abe855a5b259957bdef9f2c1332c6622d4e4d5f0647504210fe388aec562`. That note supplies the earlier full source reading and exact source-file identities.

## Dependency and type checks

**Lines 1–16: canonical lifts.** The preceding forward argument assumes only that the original \(\alpha\) is strongly cartesian in \(\mathcal S\). It uses the already established right multiplicative system, cartesian lifts in \(\mathcal S\), preservation of a fibre product and an equalizer, and the right-fraction equality criterion. It does not use reflection of cartesianness by localization, the new converse, or the conclusion that the localized category is fibred. Applying this implication to \((\mathrm{id}_U,b,\mathrm{id}_y)\) is legitimate because \(\mathrm{id}_y\) is strongly cartesian in every category over a base. Strong cartesianness is defined for any category over a base, before proving the existence of all lifts. The universal-property argument then proves both inverse identities for \(i_h\) in the fragment. Thus its opening dependency is acyclic.

**Lines 19–40: detection statement and its easy direction.** Both lifts have base \(c:W\to U\), and \(\delta_W\) is vertical over \(W\). The equation \(\gamma_y\delta_W=\delta\gamma_x\) defines the actual pullback morphism. The triples containing \(\gamma_x,\gamma_y\) belong to \(R\), using the stated relation \(u(c)\psi=\phi\). Invertibility therefore descends to the localization by the displayed equation. The unique vertical isomorphisms comparing choices intertwine the morphisms on the two sides, so the assertion is independent of choices.

**Lines 43–78: putting the inverse over one base map.** Since the inverse lies over \(\mathrm{id}_V\) and the denominator also lies over that identity, both triples have the specified \(\mathcal D\)-components. Their two \(\mathcal C\)-components \(a,c:T\to U\) are parallel. The preserved equalizer gives \(\theta_1\) because \(u(a)\theta=u(c)\theta\). After refinement, \(d=ah=ch\), so both \(\eta\) and \(\delta_1\) are vertical over \(T_1\). All four triples \(t_x,t_y,E_\eta,D_1\) are typed, and \(t_x,t_y\in R\). The two formulas for the morphism and its inverse imply separately

\[
Q(E_\eta D_1)=\mathrm{id}_{(T_1,\theta_1,x_1)},\qquad
Q(D_1E_\eta)=\mathrm{id}_{(T_1,\theta_1,y_1)}.
\]

Neither identity is inferred merely from a one-sided inverse.

**Lines 79–130: making both inverse identities hold before localization.** The equality criterion with identity denominators supplies arrows actually in \(R\); no two-sided calculus of fractions or saturation assumption is used. The maps \(\theta_x,\theta_y\) have the required common composite \(\theta_1\), so their preserved fibre product supplies \(\theta_2\). In particular the final refinement is admissible since \(u(dk)\theta_2=\phi\).

To verify the cancellation step explicitly, cartesianness of \(\rho_x\) gives a unique \(\lambda_x:x_2\to z_x\) over \(e_x\) with \(\rho_x\lambda_x=\kappa_x\), since \(k=c_xe_x\). Consequently \(\eta\delta_1\kappa_x=(\eta\delta_1)\rho_x\lambda_x=\rho_x\lambda_x=\kappa_x\). The same argument gives \(\delta_1\eta\kappa_y=\kappa_y\). The two chains in the fragment therefore prove

\[
\kappa_x\eta_2\delta_2=\kappa_x,
\qquad \kappa_y\delta_2\eta_2=\kappa_y.
\]

All arrows compared behind each cartesian arrow have the same identity base map over \(T_2\), so cartesian uniqueness proves both inverse identities. The final equation with \(\tau_x\kappa_x,\tau_y\kappa_y\) identifies \(\delta_2\) as a pullback of the original \(\delta\), not a different morphism. This establishes the detection result without the disputed converse.

**Lines 133–166: the corrected characterization and arbitrary roofs.** The factorization through \(X_a\) and \((X_2)_b\) retains the original domains, structural maps, and \(b:V_1\to V_2\). Its middle factor is in \(R\). Thus cartesianness of \(Q(A)\) makes the vertical factor relative to \(Q(k_b)\) invertible, and then makes \(Q(D_\delta)\) invertible. The detection argument supplies cartesian \(\gamma,\rho\) over the same admissible \(c\), with invertible \(\delta_W\). The equality \(\alpha\gamma=\tau\rho\delta_W\) is typed and proves cartesianness of the refined numerator. The reverse implication uses the valid earlier forward direction and precomposition with the isomorphism \(Q(r)^{-1}\). For an existing roof with denominator \(r_0\), the added refinement \(r_1\) has target the common source of \(A,r_0\), so \(r_0r_1\in R\), and the asserted refined roof represents exactly the same morphism.

## Integration boundary

The claim preceding this fragment must state the refinement criterion, not retain the original false assertion that every original numerator is cartesian. The supplied parent-task context states that this claim change and the separate surrounding type repairs are being applied. This receipt checks the replacement proof, not the application of those other edits.

In particular, the original forward proof contains already identified transcription problems involving the \(\mathcal D\)-map \(b_1\), the order \(r\circ r'\), the missing denominator \(r\) on the right-hand side of its numerator comparison, and the base lifted by \(\gamma'\). Their corrected types are needed when retaining that forward proof. They do not create a circular dependency, and no additional defect in the new 166-line fragment was found.
