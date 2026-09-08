# Review of the EGA I 7.3.8 comparison

Review date: 2026-09-08. Verdict: **PASS for the mathematical argument and the
reviewed code/evidence design, after the qualification correction recorded
below.** Final artifact sealing and the post-seal regression run are separate
mechanical operations; this review does not claim they have already finished.

The scope is the single, source-ordered EGA I 7.3.8 comparison, including its
numbered formula and complete proof. It does not admit the following section,
close any of the twelve inherited gaps, modify an EGA edition, assign an
official Stacks tag, establish formal proof checking, or claim publication or
completion of EGA I–IV.

## Review identity and limits

The reviewer is the separate task `/root/ega738_continue/ega738_final_review`.
The implementation owner is `/root/ega738_continue`. The reviewer read the
actual manuscript, source helper, semantic contract and tests, the scoped
checker and predecessor-migration changes, the appended ledger records, the
three source preparations and the separate printed-authority binding.

The reviewer authored `tests/test_ega_i_738_source_boundaries.py` and this
report. The existing source helper was reviewed and retained unchanged.
Consequently this is an independent review of the owner's manuscript and
semantic implementation, but not an independent second authorship review of
the reviewer's own new source tests. The implementation owner will read those
tests and this report and run the final combined gates.

Printed EGA II pages 221–222 were visually compared with the transcription by
the root preflight reader. This reviewer read the attributed record, not the
PDF or its rendered pages, and did not perform a new visual inspection. The
public binding preserves that distinction: its implementation-owner visual
reading flag is false. No historical F37ZW receipt is represented as admitting
those later pages.

The following actual bytes were hashed during this review:

| Object | Bytes | SHA-256 |
| --- | ---: | --- |
| `ega/i738.md` | 15134 | `105555649407DA07C90400359A95A48935F906F7816EE5B8B8BFE8A29D574E39` |
| `tools/check_ega_i738_source_boundaries.py` | 14830 | `F54B129D5F529C716606CD943BD16CD922DBE0F3A70D9E3FE356CEC88CDE8419` |
| `tests/test_ega_i_738_source_boundaries.py` | 25869 | `DF0D0C434BAE0E6F4B370E426CD963B2C8D3941E240140A8139204986592D62C` |
| Printed-replacement authority binding | 6890 | `59EE5247301B33877F46FAFF8CCD92382FF4CCDC74C8F825EA1361CF6DBB3487` |

The authority object is
`validation/ega-i-7.3.8-printed-replacement-authority-2026-09-08.json`.
The semantic receipt and its seal constants are intentionally not described
as final here: recording this review changes those mechanical seals. Their
final identities belong to the subsequent tested-byte freeze.

The prepared manuscript was independently compared with the actual candidate:
the prepared 14729-byte object has SHA-256
`5C90C1B359BCDF307FA4CDAE876E4CA813457F70314B5B15EC6C66D201EAEEE5`.
The complete diff contains only candidate framing, six stable anchors and the
final disposition paragraph. No mathematical argument was replaced or
silently restarted. The arguments were nevertheless checked afresh below.

## Three distinct source versions

The complete literal declarations, proofs and excluded boundaries were read.
The source helper's independent constants were compared with the separately
prepared source records. The bounded live replay then fetched each whole
source once and returned PASS with no errors:

| Version | Whole bytes | Whole-source SHA-256 | Owned physical LF lines | Complete proof LF lines |
| --- | ---: | --- | --- | --- |
| Original French Chapter I | 38226 | `73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522` | 648–671 | 661–670, unwrapped |
| Corrected French EGA II errata | 19746 | `EC20D329248B99CF0533CB868DBDF8135D5BDAFA233133814DB67F8CD4F09643` | 470–507 | 486–506, unwrapped |
| Corrected English Chapter I | 35788 | `B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC` | 380–402 | 392–401, wrapped |

Both French files are pinned to revision
`6b38875842e3723b619d4aeeda9ed260a4f94f7c` of `KokunoYumeto/ega-fr`;
the English file is pinned to revision
`94d5c73ac9263b26043ad0551646b824b1030c9b` of `KokunoYumeto/ega-en`.
The exact source URLs, nested spans and offset/hash inventories are retained
in the semantic checkpoint and source helper.

The original assertion is a false global-isomorphism claim under a
finite-component generic-point-surjectivity hypothesis. The later French
instruction expressly replaces it. The replacement assumes integral source
and target and a dominant morphism, constructs a canonical module map, and
proves that its generic stalk is an isomorphism. The English note and proof
follow this replacement; the version difference is not misclassified as a
new translation error.

The corrected French replacement instruction, internal page-222 marker,
running header and equation are owned nested evidence, not new mathematical
units. The English translator note and both proof wrappers are retained,
while its proof body is identified separately. The French Chapter I
LF672–676 and English LF403–408 heading/opening blocks are excluded; the
corrected French next paragraph at LF508 is also excluded. No ownership is
extended to I 7.4.1 or I 9.5.2.

The printed-source binding identifies EGA II, DOI `10.1007/BF02699291`,
the 27414108-byte original PDF with SHA-256
`111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB`,
and the two attributed page-image identities. This is a new direct binding,
not a retrospective alteration of the older source interface.

## Mathematical checks

The following checks concern the manuscript's actual six anchored sections,
not merely true flags in a metadata object.

1. **Integral affine construction and gluing.** Dominance identifies the
   generic-point image and gives the injection `B -> A` on every compatible
   pair of nonempty affine opens. Its fraction-field embedding is the map of
   generic local rings and is therefore fixed independently of that pair.
   The affine pullback is associated to `A tensor_B L`, canonically `S^-1 A`
   for `S = B \ {0}`, with its inclusion in `K`. The given formula has the
   right scalars and direction. The common-refinement argument refines both
   source and target neighborhoods and covers each source overlap; it does
   not assume affine intersections are affine or impose separatedness.

2. **Generic stalk versus global injectivity.** The generic map is
   `K tensor_L L -> K`, multiplication, exactly the replacement's stalk
   conclusion. Global injectivity is explicitly an additional derivation:
   every stalk is the inclusion `S^-1 A_p -> K` of a localization of a domain.
   The all-stalk criterion applies. Neither injectivity nor a global
   isomorphism is inferred from the generic stalk alone, and arbitrary
   pullback exactness is not used.

3. **Exact isomorphism criterion.** Localization primes are precisely the
   primes of `A` contracting to zero in `B`, namely the entire point-set
   generic fiber inside the affine open. If only the zero prime remains,
   the domain `S^-1 A` is a field and must equal `K`. Conversely an affine
   section isomorphism with `K` forces this singleton prime spectrum.
   Compatible affine pairs cover `X`, so both implications are global.
   The identification of the scheme-theoretic generic fiber's underlying
   space and its compatible `Spec K` pieces is valid without finiteness or
   a dimension formula. A bijection of component-generic-point sets alone
   is correctly rejected.

4. **Old false assertion and birationality.** For the affine line over a
   field, the pullback from `Spec k` is the structure sheaf, whose stalk at
   `(t)` lacks `1/t`; the rational sheaf has it. The old proof's constancy
   invocation requires a compatible rational-sheaf module structure that
   this example cannot possess, since that structure would invert `t`.
   Birationality forces `L = K` in the affine calculation and is sufficient.
   Any field extension `Spec K -> Spec L` provides an isomorphism without
   requiring birationality, algebraicity or finite generation.

5. **Finitely many components, without reducedness.** A dense open contains
   each component generic point: remove the other finitely many components
   and use density in the resulting nonempty open. Under the stated
   generic-point mapping hypothesis, dense representatives and dense
   agreement subsets pull back densely. Rational pullback is therefore
   well-defined, compatible with restrictions and ring operations, and
   sheafifies before scalar multiplication. Surjectivity onto target
   generic points is unused and unnecessary. At a source component generic
   point the rational and ordinary local rings agree; tensor multiplication
   gives the claimed generic-stalk isomorphism. These local rings need not
   be fields, and no global injection is claimed in this generality.

6. **Embedded torsion and the meromorphic distinction.** In
   `A = k[t,e]/(e^2,te)`, the element `e` is nonzero, dies at the sole minimal
   prime `(e)`, and survives at `(t,e)` because every element outside that
   maximal ideal acts on it by a nonzero constant. Its annihilator exposes
   the embedded associated prime. The map to `Spec k` has a rational kernel
   but has defined meromorphic pullback by flatness. For the map to the
   affine line, `A tensor_{k[t]} k(t) = k(t)` gives a rational isomorphism,
   while regular target `t` becomes a zero divisor, so meromorphic pullback
   is not defined in the cited sense. The bridge via Tag 0EMF retains both
   weak-associated-point and quasi-compact-open finite-component hypotheses.
   The reduced-source alternative in Tag 02OU(4) is not extended to an
   arbitrary nonreduced source.

No actionable mathematical defect remains from this review. Confidence is
high as an ordinal editorial judgment based on these complete arguments and
adverse cases; it is not a calibrated probability or a kernel-checked proof.

## Actual modern targets and auditable choices

All twelve complete target declaration/proof blocks were read at the
official baseline `a04446e57ec1fbc252a871afcec7752fb2807b14` and candidate
base `027e32195209a05d1b28a854e030d71600c9c76b`. Actual `git show` bytes were
checked for all 24 spans, all twelve tag/label joins and the twelve distinct
commit/file whole-source objects. Receipt text, physical-LF intervals,
exclusive byte offsets, byte counts and SHA-256 identities agreed.

| Targets | Checked use |
| --- | --- |
| 0CC1, 01RV, 01X5 | Dominance, rational generic rings and integral meromorphic agreement |
| 01I9, 00DK, 01CB | Affine pullback, tensor/localization identification and tensor stalks |
| 0H7H, 00E3, 01K1 | All-stalk injection, localization primes and actual generic fiber |
| 02OT, 02OU, 0EMF | Regular-denominator pullback, valid sufficient cases and both bridge hypotheses |

The versions of 01RV and 01CB differ by inherited reference material;
00E3 has an inherited proof change, including the final topological argument.
Those three pairs retain unequal identities. The remaining nine pairs have
identical block text. The two 00E3 proofs establish the same localization
prime correspondence used here. Omitted target proofs, including those of
01X5, 0H7H and 01CB, are recorded as omitted, not invented as printed proofs.

The choices D000372–D000374 connect all three distinct source versions to
the six exact anchored target-text segments and the actual S001489–S001504
edges. Their rationales distinguish printed conclusions from independently
derived results and retain meaningful rejected alternatives and uncalibrated
confidence reasons. R000956–R000965 document the resulting dispositions.
The old source statement remains historically false; its coverage entry
does not promote it to a true theorem. The twelve earlier open-gap rows
remain outside the newly covered material.

### Finding corrected during this review

The first version of the 01X5 evidence note said the two sheaf definitions
agree “for integral schemes only.” That phrasing could imply that integrality
is necessary, which neither 01X5 establishes nor the conditional 0EMF bridge
permits. The owner changed actual S001491 and both corresponding semantic
receipt occurrences to state that 01X5 establishes agreement in the integral
case, without inferring unconditional nonreduced agreement. The corrected
actual rows and choice relevance were read back. The mathematical manuscript
already made the correct qualified statement and was not changed.

## Code and deterministic evidence review

The source helper independently pins each source URL, full identity, physical
LF count and all nested owned/excluded intervals. It compares complete
inventories with strict scalar types, requires exact raw UTF-8/LF bytes,
checks literal span identities and wrapper inventories, and detects global
duplication of the scoped source markers. It rejects source-version swaps
before transport. Each source read has a 30-second transport timeout and
reads at most its expected length plus one byte, with no retry or file write.
Structural acceptance alone is explicitly not whole-source certification.

The new 18-test offline suite passed. Its literals independently reproduce
the three complete reviewed intervals in explicitly synthetic surroundings.
It exercises every owned and excluded line, all six version swaps, complete
proof ownership and wrapper distinctions, the translator note, replacement
instruction, internal page marker and header, changed metadata leaves and
types, extra/missing owners, duplicated markers, extended boundaries,
self-rehash attempts, malformed raw bytes, bounded cached/network plumbing,
failed reads, duplicate JSON keys and absence of writes. Synthetic fixtures
are required to fail whole-source certification; a mocked transport success
does not count as source authenticity.

The semantic contract seals the complete reviewed metadata separately from
loading actual source authority, manuscript, target, discovery and ledger
objects. It verifies paired target blocks against actual pinned Git blobs,
checks the independently fixed source contracts, and binds the separate
printed replacement. Ledger checks preserve the previous prefixes and exact
new appends, enforce the actual active CSV view, retain the three unpromoted
English discovery units, and protect the twelve earlier gaps. The manuscript
seal rejects altered text even when a caller supplies a coordinated new hash.
These are deterministic evidence checks, not mathematical proof procedures.

The scoped changes to `ega/check.py` admit only the exact newly bound printed
replacement, advance the source frontier to I 7.4.1, and invoke both the new
contract and the predecessor's historical-prefix projection. The latter
verifies the immutable 7.3.5–7.3.7 receipt before selecting its exact former
ledger postimages; it does not rewrite that receipt or discard successor
rows from the new validator. The predecessor regression's twenty tests
passed in this review, including appended-successor acceptance and old-prefix
damage rejection.

The combined 37-test semantic run completed with 35 passes and two expected
pre-seal failures: the deliberately empty `reviewed_artifacts` inventory and
the canonical receipt seal after the 01X5 correction. Those failures were
not waived or represented as a passing acceptance run. The owner must now
bind this report and the reviewed helper/tests, mechanically reseal the
corrected objects, and execute the complete post-seal tests, checker and live
source replays. The final frozen identities and results are recorded by that
transaction; no new human review or approval is required to perform it.

No TeX, PDF renderer or Lean worker was launched by this review, and no
publication action was performed. The code, source and mathematical review
is complete; the remaining work is the explicitly identified sealing and
verification transaction.
