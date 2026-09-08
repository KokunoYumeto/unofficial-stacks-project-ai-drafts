# Review of the dense-open rational-function sheaf

This record concerns complete EGA I 7.3.1–7.3.4, the section heading,
7.3.2 restriction tail, and the entire 7.3.3 proof. The
[independent derivation](i734.md) is bound to the
[immutable source/target checkpoint](../validation/ega-i-7.3.1-7.3.4-semantic-checkpoint-2026-09-08.json).
It does not claim formal proof checking or completion of EGA.

## Mathematical review

An independent root review read the entire 16,660-byte manuscript and found
the presheaf, algebra-compatible restriction, sheafification, local finite
component reduction, natural generic-local product, arbitrary-cover sheaf
argument, finite localization, and full quasi-coherence proof sound.
The reduced-component decomposition and both nonreduced adverse examples
were also reviewed. The continuation owner read the entire manuscript and
all exact paired French/English source and sixteen official/current target
blocks. No concrete mathematical defect required changing the manuscript:
SHA-256 `D4F939E921750A907E0B335DB9D9DA9242EC407B90AD7561EA63C9682C5C3163`.

Three additional paired context passages bind the ring operations preceding
01RU, the localization presheaf preceding 01X2, and the definition of a
regular section as injective multiplication. Exact locations, source texts,
byte counts, hashes, and their roles appear in the checkpoint. These
contexts support the construction and the distinction between the sheaves;
they are not extra full-theorem equivalence claims.

| Decision | Source ownership | Reviewed choice |
|---|---|---|
| D000365 | 7.3.1 | Dense-open restrictions preserve rational equivalence and act through the scalar restriction map. |
| D000366 | 7.3.2 and its tail | Ring/module sheafification and cofinal germs give restriction to an open; no injectivity is inferred. |
| D000367 | 7.3.3 and complete proof | Generic factors remain local rings; arbitrary-cover gluing and finite elementwise-nilpotence localization give quasi-coherence. |
| D000368 | 7.3.4 | Reducedness identifies generic factors with component fields; sections, restrictions, and scalar actions give the algebra decomposition. |

The material rejected alternatives are recorded with source and target
joins in the machine-readable choice ledger inside the checkpoint:
automatic R=K identification, Noetherian coordinate rings in the topological
special case, globally finite in place of locally finite components,
residue fields in the nonreduced theorem, and omission of reducedness in
7.3.4. The notation R(X_i) in the source proof remains an explicit caveat,
not an adjudicated printed erratum. Editorial confidence is high because
of the direct source comparisons and complete derivations; it is not a
calibrated probability. Later expert evidence may improve this reversible
decision and is not a release gate.

## Evidence and implementation scope

There are five unchanged discovery units. The page marker belongs to
7.3.2; the restriction tail is separately owned without a fictional unit.
French 7.3.3 has an unwrapped proof, while English wraps it explicitly.
No proof is printed for 7.3.4: its proof in the dossier is independently
supplied. The next excluded numbered environment is 7.3.5.

All twelve earlier active open gaps and all historical ledger prefixes
remain unchanged. The 7.2.8–9 contract now receives its exact historical
prefixes and coverage snapshots; its immutable receipt is unchanged.
The new contract checks current ledger bytes and active views, exact paired
target objects, preserved inputs, source ownership metadata, and reviewed
dossier and receipt seals. Adverse tests deliberately damage those objects
and distinguish Boolean values from numerical substitutions.

Raw-source replay is separate from offline evidence checks. Neither
checksums nor semantic flags prove mathematics. No root TeX, source
edition, translation, official tags, publication, or visual-QA claim is
changed by this candidate.

## Independent final implementation review

A separate reviewer read the entire manuscript and review record, all sixteen
paired target blocks and three paired context passages, all new decisions,
mappings and residuals, the complete new semantic contract and tests, and the
7.2.8–9 historical-prefix migration. Final result: PASS, with no actionable
mathematical or code defect. The reviewer independently replayed all 32 target
blocks and six context blocks against Git objects; all seven target files
agreed across the candidate base, integrated comparison commit, and live files.
All four historical ledger prefixes and their appends matched the receipt.
The reviewed pre-final-metadata receipt was 159,889 bytes, SHA-256
`CB665C49E3A24A3974CCB2A00A03789812C781C0520A748E1897F8D205420AE5`.
The final metadata append records this review; it does not alter the manuscript
or its mathematical decisions.

The reviewer ran 29 independent boundary tests and a combined 71-test
boundary/current-semantic/predecessor-semantic suite, all passing. A separate
bounded raw replay verified the pinned French and English whole identities
and every owned interval. The continuation owner also ran 372 predecessor
7.x regression tests and the full EGA checker successfully. Final post-review
metadata checks are recorded in the candidate freeze receipt.

The root independently read the complete new semantic contract and tests,
the predecessor historical-prefix projection and checker wiring, the
complete source-boundary helper, and all 29 boundary-test bodies; no defect
was found. This is a read-only review, not a claim that the root ran the final
post-reseal suite on this candidate.
