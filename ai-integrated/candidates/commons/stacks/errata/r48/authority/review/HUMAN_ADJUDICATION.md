# Independent adjudication of the five recovered groupoid findings

All **five findings are valid**, with **six exact operations**, **no registered duplicates**, and **no disagreements with the supplied packet**. The RHS-only inverse-order alternative is rejected as a complete repair of the written derivation. No source, registry, ID allocation, build, admission, or publication was changed.

This reviewer read the actual complete relevant proofs in both source versions. The supplied verdicts and replay claims were treated as assertions to check. The review did not re-audit the whole chapter or repeat historical task mining.

## Source and intake identities

The intake file is:

`<USER_ROOT>/Documents/interlanguage/03_projects/language_management/stacks_on_stacks_hub/00_control/session_fixes_20260910/GROUPOIDS_RECOVERED_FIX_REVIEW.json`

Its actual size is 25,610 bytes and SHA-256 is `03BC386D88EDF536A0A90664676DA2FD34007FC12D49A436BC3C9A23F984C47D`, matching the delegated identity.

The current chapter is:

`<USER_ROOT>/Documents/interlanguage/worktrees/unofficial-ai-stacks-r47-illusie-linear-successor-20260907/groupoids.tex`

It is 205,795 bytes, 5,513 LF-terminated lines, SHA-256 `C6CF7E55C1C4F87EC475F514AED7219AF824EC3AC7734319367E54D5F6DFE7A5`.

The pinned original is:

`<USER_ROOT>/Documents/interlanguage/03_projects/language_management/cjk/03_working_translations/stacks_cjk_20260821/upstream/src/stacks-project-a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids.tex`

It is 189,166 bytes, 5,124 LF-terminated lines, SHA-256 `157CC1C792F41465B8249582FEE0F6DFF266AC4224F06B05E936C66C65DB043A`. Both actual identities equal the packet's claims.

## Independent mathematical judgments

### Zero multiplication in the étaleness proof — valid

The current degree lemma, 1935–1991, explicitly assumes a nonzero integer d. The étaleness statement and its complete proof at 1993–2016 still allow d=0 and invoke finite local freeness without separating it. The pinned comparison is 1768–1848.

For a nonzero abelian variety, dimension is positive. Indeed, a zero-dimensional integral variety is a single reduced point with a finite residue extension L/k; the unit provides a k-algebra map L to k, forcing L=k. Such an abelian variety is the zero group variety. The definition at current 1762–1767 and smoothness at 1799–1815 are consistent with this argument.

For d=0, the fibre over the unit is all of A. Its positive dimension rules out local quasi-finiteness and therefore étaleness. The latter implication was read in pinned `morphisms.tex`, 8161–8172. This argument does not invoke the multiplication-degree lemma. Once d=0 is handled, its finite-local-freeness hypothesis applies to the remaining proof. Tangent injectivity at the rational unit has the stated relation to unramifiedness; the cited criterion was read in pinned `varieties.tex`, 3148–3171.

The packet's three-line case split is therefore sufficient and noncircular. The lemma statement should continue to include d=0. Registered unit **MC-STK-ERR-1494** repairs the nonzero hypothesis of the separate degree lemma at pinned 1771; it does not repair this later proof invocation at pinned 1836. Preserve that existing repair.

### Cover orientation in the colimit proof — valid

The full current proof at 3443–3557 was read together with the module definition and inverse proof at 2912–2967. The corresponding pinned passages are 3152–3266 and 2622–2676. The underlying referenced sheaf-generation proof in pinned `properties.tex`, 3554–3631, was also read.

The fixed convention is `alpha : t*F -> s*F`. The source of its restriction to W_ijk is `M_i tensor_(A_i,t) B_ijk`; the target is `M_j tensor_(A_j,s) B_ijk`. These expressions require t(W_ijk) to lie in U_i and s(W_ijk) to lie in U_j. The existing cover supplies the opposite two structure maps. Swapping s and t in the cover at current 3470 is exactly the needed repair.

All downstream indices agree with the corrected cover. The support construction first gives the inclusion `alpha(t*G) subset s*G`. Pulling it back by inversion gives `i*alpha(s*G) subset t*G`. Since `i*alpha = alpha^{-1}`, applying alpha gives the reverse inclusion. Thus the equality used at current 3534 and 3539 follows. No requirement that particular affine cover members be inverse to one another is needed.

Registered units **MC-STK-ERR-1504** and **MC-STK-ERR-1505** respectively repair the cardinal-comparison wording and the identity support-choice indices. Neither changes the cover. This finding is also distinct from the ambient-module correction below.

### Coefficient ring after base change — valid

The invariant-ring definition at current 4487–4510, determinant and rank-decomposition arguments at 4542–4659, and entire base-change lemma at 4661–4744 were read. The pinned base-change lemma is 4367–4450.

At current 4718, the component system is explicitly `A_r, B_r, C_r, C'_r, C^1_r`. Its part (2)(a) produces a polynomial over **C'_r**, as the final norm argument independently confirms by mapping `D[x] -> C'[x]` at 4743. The finitely many invariant rank strata give compatible finite product decompositions. Choosing a positive common multiple n of their ranks and taking `P_r^(n/r)` glues to the claimed polynomial over C'.

There is also a direct counterexample to the unprimed ring. Take the identity groupoid over a field k and base-change to k[z]. Then the rank is one, the invariant ring after base change is k[z], and f=z requires P=x-z. This polynomial cannot come from k[x]. It does lie in k[z][x].

Changing C_r[x] to C'_r[x] at current 4719 is therefore forced. Registered unit **MC-STK-ERR-1515** already changes `U'=Spec(C')` to `U'=Spec(A')` at current 4715/pinned 4421. The two changes affect different objects and different lines; preserve the admitted one.

### Two ambient modules in the support choices — valid

The first displayed support equality at current 3501 lies in M_ijk. The second at 3503 lies in the codomain `M_j tensor_(A_j,s) B_ijk` of alpha restricted to W_ijk. The existing sentence at 3505 names only M_ijk for both alternatives. The proposed replacement lists the two modules in the displayed order and adds “respectively.”

Current line 3536 independently supplies exactly the same pair of ambient modules. This was also checked in the pinned full proof, particularly 3210–3216 and 3241–3245.

The cover correction is needed to supply the structure maps, but cannot itself correct the wrong ambient-module sentence. These are complementary defects. The neighbouring registered unit **MC-STK-ERR-1505** starts at pinned 3215; the present operation is at 3214. Their byte and line spans are disjoint.

### Inverse composition order — valid; RHS-only alternative rejected

The full module definition and inverse proof show that alpha maps t*F to s*F, while i*alpha maps s*F to t*F. The actual cocycle order is:

`pr_1*alpha composed with pr_0*alpha = c*alpha`.

The groupoid inverse axioms were read directly at current 2719–2725. They state `c(i,1)=e s` and `c(1,i)=e t`. Pulling back the cocycle therefore gives:

| Named pullback | Correct left side | Correct right side | Endomorphism of |
| --- | --- | --- | --- |
| (i,1) | alpha composed with i*alpha | s*e*alpha | s*F |
| (1,i) | i*alpha composed with alpha | t*e*alpha | t*F |

The packet's two LHS-order replacements repair both the types and the stated derivation. The historical trailing space at current 2964 is preserved.

Swapping only the two right-hand letters would give true, type-correct standalone identities, but would attach each identity to the wrong explicitly named pullback map. That alternative is rejected **as a complete two-line repair**, not because those standalone identities are false. It would also require swapping the two preceding named maps. The accepted two LHS changes need no such extra edits.

Registered **MC-STK-ERR-1499** inserts the missing word “diagram” in the module definition at pinned 2643. **MC-STK-ERR-1501** changes projection ordering in another construction at pinned 2860. Neither repairs these inverse identities at pinned 2671 and 2673.

Each of these five judgments has high qualitative editorial confidence for the reasons above. These are not calibrated probability estimates. No mathematical disagreement with the supplied packet remains.

## Registered-unit reconciliation

At the local observation **2026-09-09T23:36:21.2448020Z**, HEAD was `7c763a2c168ffec7b6fbe3917ecd953f1e584787`. The registry SHA-256 remained `180D91A7C2FFD034B469EFF40339AB3C312E77CE6745968CB172289CA934223A`. This is a local-registry observation; this pass makes no new remote-freshness claim.

The 48 registered candidate source maps contain 1,292 rows. Exactly 43 target groupoids.tex, all in r46 and covering stable IDs **MC-STK-ERR-1480–1522**. Their 46 operations were examined. All 43 IDs are present in both the r46 stable-unit file and the current registry entry.

The relevant files are:

| File under the worktree | SHA-256 |
| --- | --- |
| `ai-integrated/candidates/commons/stacks/errata/r46/source-map.jsonl` | `9B2DD65725C4221A641555A09D5A765918E9C1000F21D16D5062B073B47CAE91` |
| `ai-integrated/candidates/commons/stacks/errata/r46/stable-units.json` | `F3F0C645BACB2B173113CEA81D6F8C3D340C8FBA3C375FFCDDFB8BFCD9FC5505` |

No new operation overlaps an existing registered operation interval in pinned-source coordinates. No old/new operation pair duplicates one of the existing pairs. Semantic comparison of the existing unit descriptions and corrections also finds no duplicate or conflict; the nearby repairs are distinguished above.

This does not claim to search unregistered candidates, rejected reports, or other task history. No new IDs were assigned.

## Exact replay and preservation

`EXACT_REPLAY.json` beside this report contains the complete LF-inclusive old and replacement text, independently checked byte lengths and hashes, one-based line positions, and zero-based end-exclusive byte coordinates for both source versions.

| Finding / operation | Current line and byte span | Pinned line and byte span |
| --- | --- | --- |
| Zero multiplication | 2004; [74899, 74967) | 1836; [67383, 67451) |
| Inverse order, first identity | 2962; [110525, 110583) | 2671; [97731, 97789) |
| Inverse order, second identity | 2964; [110644, 110711) | 2673; [97850, 97917) |
| Cover orientation | 3470; [129575, 129647) | 3179; [116774, 116846) |
| Two ambient modules | 3505; [130679, 130747) | 3214; [117883, 117951) |
| Coefficient ring | 4719; [174233, 174295) | 4425; [161388, 161450) |

Every old preimage is unique in each entire file. All six operations are non-overlapping. Exact byte splicing was performed only in memory, and each of the seven untouched spans was compared byte-for-byte.

| Input | Candidate bytes in memory | Candidate SHA-256 | Lines |
| --- | ---: | --- | ---: |
| Current integrated source | 205,993 | `91E6BC02125516C95ED04DE98FAA097C884D3E9F94DD228FAD77CB31231DE444` | 5,517 |
| Pinned original | 189,364 | `8BDE7E962B3C3D3A3094BA9F73536F17452A3204861372496D4EEC23ACF13F2C` | 5,128 |

The current-source result exactly matches the packet's expected candidate hash. The pinned replay is only a coordinate and preimage check; it omits other already admitted corrections and must never replace the cumulative current chapter.

The single writer can use the six current-source operations after rechecking the source and registry identities at its transaction boundary. The current degree-lemma restriction, base-change object correction, and every nonoperation byte are preserved. This independent review requires no human-dependent hold.

## Durable instruction record

The verbatim delegated task is retained in the `verbatim_task_input` field of `EXACT_REPLAY.json`. It governs the finite scope of this review. The completed work consists solely of this report and that JSON; no build or source artifact was written.

