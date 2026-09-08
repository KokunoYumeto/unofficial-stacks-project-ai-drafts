# Independent review of EGA I 7.3.5–7.3.7

Recorded 2026-09-08. Candidate base verified by `git rev-parse HEAD`:
`20307123eefacd21760bdf6f306774c09d4bab18`.

Disposition: **mathematical PASS; bounded source-boundary tests PASS**.
No substantive mathematical defect was found. One minor hypothesis-strength
wording correction was sent to the implementing agent, applied, and verified;
its disposition is recorded below. This is an independent review, not a semantic-admission,
release, original-PDF-read, or proof-assistant claim. Human response is not a
gate. The implementing agent owns the choice ledger, contract, freeze,
admission, and release checks.

## Exact objects actually consulted

The following two preparation artifacts were read completely, including all
17 source passages, all 36 target blocks, and the provenance qualifications.
They are identified by filename and content hash without exposing private
storage locations.

| Artifact | SHA-256 |
| --- | --- |
| `EGA_I_7_3_5_7_PREFLIGHT_20260908.md` | `B3793AA78722831FFA94089F20A3BE506F25FA44FB4AC4E16AF075D9F5F11ACD` |
| `EGA_I_7_3_5_7_SOURCE_TARGET_EVIDENCE_20260908.json` | `774FB4EFB98D4FB482E8FA24E0E08660EF8AE0AAB986A6ADD76CDBA6A66CCB9F` |

The candidate files below were read in full. These identities describe the
reviewed initial bytes, not an inferred future freeze.

| File | SHA-256 |
| --- | --- |
| `ega/i737.md` | `D54EB2309C97FF805FDE281D7D8CE2981606E2C7219F38004B495DAD590BA0D9` |
| `tools/check_ega_i737_source_boundaries.py` | `8F8621DB1CF2768F574244D8713CA039C8620B4361AE9518F5B241D0F9D15FE3` |
| `tests/test_ega_i_737_source_boundaries.py` | `8DC740098DCAC51AE9A57B294531E76D8C1146E1662A7318DD84617B4AB81A07` |
| Imported `tools/ega_raw_source_boundaries.py` | `ACB26A19E1E9DF3A7E4B14F1B93581C513C7AA7223C98EDF5FD6A356C3357C5D` |

### French authority and comparison witnesses

The evidence retains the exact Chapter I French authority at repository
`KokunoYumeto/ega-fr`, commit
`6b38875842e3723b619d4aeeda9ed260a4f94f7c`, file
`source/ega1/ega1-7-fr.tex`, whole SHA-256
`73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522`.
Its complete reviewed source units are LF 606–622, 623–633, and 634–647.
Their unwrapped proofs are respectively LF 612–621, 632, and 644–646;
the page marker at LF 637 remains inside 7.3.7. The source dependencies
were also read completely: 7.2.2–7.2.3 at LF 304–362, and 7.3.1–7.3.4
at LF 531–605. Reading those dependency passages does not re-own them.

The English comparison is repository `KokunoYumeto/ega-en`, commit
`94d5c73ac9263b26043ad0551646b824b1030c9b`, file
`source/ega1/ega1-7.tex`, whole SHA-256
`B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC`.
The complete corresponding units are LF 350–358, 359–367, and 368–379;
their proof wrappers/body intervals are 355–357/356,
364–366/365, and 376–378/377. Its dependency passages at LF 181–216
and 313–349 were read as comparison, not silently promoted to authority.
French LF 648–649 and English LF 380–381 were read only as the excluded
7.3.8 begin/label boundary. No 7.3.8 mathematics was admitted or reviewed.

At the French repository pin, `source/ega0/ega0-3.tex` is English:
whole SHA-256
`39A938B994A65AB06CC026419E140CB37163109BB94659BE7B37299BC07DB343`.
I read its 0.3.6.1 at LF 717–727 and complete 0.3.6.2 argument at
LF 728–760. Likewise `source/ega0/ega0-5.tex` is English, whole SHA-256
`C86A79ADF70D29D0257CBA61EA3E73E0A4B5AC133B91C7EBF34FBAFB4D98FDA3`;
the reviewed passages are 0.5.1.1 at LF 7–27, 0.5.1.3 at LF 38–44,
and 0.5.1.4 at LF 45–53. The distinction between a repository's name
and the actual language of its contents is maintained.

The original French Chapter 0 visual review is **attributed evidence**.
The preflight reviewer reports visually reading printed pages 33 and 45,
PDF pages 32 and 44 one-based, of the 1960 EGA I volume,
DOI `10.1007/BF02684778`, PDF SHA-256
`9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.
This reviewer did not render, open, or visually read that PDF and does
not turn the preflight's short quotations into a claimed new reading.
The actual Chapter I French words, the English Chapter 0 comparison,
and the modern definitions below independently make the normalization
mathematically coherent. The historical PDF provenance remains attributed.

### Modern mathematical canon actually read

Every full block below was read at both exact pins, including all printed
proofs, remarks, examples, reference/history blocks, and explicit proof
omissions. Official pin:
`a04446e57ec1fbc252a871afcec7752fb2807b14`.
Integrated comparison pin:
`1bed4dc0cb48717c476c7292b91b018743e9a530`.
The companion evidence supplies each exact text, byte interval, whole-file
hash, and span hash; those records were independently verified against
14 exact local Git blobs, without repository-wide scans. All 36 tag-to-label
mappings were independently checked against the two exact `tags/tags`
blobs. The seven current mathematical source files also match the integrated
whole-file hashes. A matching hash is an identity check; the complete block
readings and derivations, not the hashes, support the mathematical review.

| Tag | Exact file | Official LF | Integrated LF | Use and limits checked |
| --- | --- | --- | --- | --- |
| 006W | `sheaves.tex` | 587–595 | 591–599 | Constant sheaf as locally constant maps. |
| 0081 | `sheaves.tex` | 1629–1638 | 1696–1705 | Sheafification of the constant presheaf. |
| 01BE | `modules.tex` | 1020–1039 | 1046–1065 | Local cokernel of arbitrary sheaf direct sums. |
| 01BG | `modules.tex` | 1085–1125 | 1111–1151 | Pullback presentation over a named sheaf of rings. |
| 01BJ | `modules.tex` | 1216–1245 | 1253–1282 | Restriction/pullback of an associated module, used when refining the neighborhood. |
| 01BK | `modules.tex` | 1246–1314 | 1283–1351 | Quasi-compact-neighborhood argument giving a column-finite presentation matrix. |
| 01CB | `modules.tex` | 2332–2349 | 2464–2484 | Tensor stalk formula; the printed proof says “Omitted.” |
| 01CC | `modules.tex` | 2364–2391 | 2499–2529 | Right exactness checked stalkwise, not flatness. |
| 05NB | `modules.tex` | 2406–2438 | 2544–2576 | Tensor product commutes with arbitrary direct sums. |
| 02CF | `modules.tex` | 1077–1084 | 1103–1110 | Excludes unrestricted arbitrary-sum closure on general ringed spaces. |
| 01J1 | `schemes.tex` | 2153–2170 | 2286–2303 | Reducedness and rings of sections. |
| 01J2 | `schemes.tex` | 2171–2184 | 2304–2317 | Reduced affine rings and their localizations. |
| 01OZ | `properties.tex` | 495–508 | 495–508 | Scheme-local Noetherianity implies topological local Noetherianity, not conversely. |
| 01RV | `morphisms.tex` | 12704–12740 | 12807–12846 | Finite-component dense-open rational ring as a product of generic local rings. |
| 01HV | `schemes.tex` | 691–729 | 697–764 | Principal-open localization, stalks, global sections, exact associated-module functor. |
| 01I7 | `schemes.tex` | 1077–1111 | 1148–1182 | Associated-sheaf comparison and mapping property. |
| 00EU | `algebra.tex` | 4542–4558 | 4601–4617 | Elementwise nilpotence at a minimal prime; field after reducedness. |
| 0052 | `topology.tex` | 1252–1302 | 1302–1356 | Finitely many components in a Noetherian topological neighborhood. |

Differences of references and wording between the pins were not erased.
For example 01HV has a larger integrated reference/history block, 01CB's
proof remains omitted at both pins, and 0052's integrated proof uses
“minimal element” where the official proof says “smallest element.” The
descending-chain argument requires a minimal element, not a least element.
This target-version distinction does not create a new defect in the dossier.

## Independent mathematical rederivation

### Inherited construction and terminology

For finitely many components, each dense open contains every generic point.
One can refine to the pairwise disjoint opens obtained by removing the other
components. Choosing finitely many representatives of generic germs and
gluing on that disjoint dense union proves the product description of the
dense-open rational ring. Equality of germs gives equality on a common
dense refinement, proving injectivity as well. Restrictions discard the
coordinates of components not met. Compatible local tuples glue coordinate
by coordinate, so this presheaf is already a sheaf in that finite-component
case. On an affine open it is the associated module of the finite sum
of localizations at minimal primes. At a principal open, a factor survives
unchanged when the element is outside that minimal prime, and vanishes
when its image is nilpotent inside the corresponding generic local ring.
This needs elementwise nilpotence only; it does not require the entire
maximal ideal to have a common nilpotence exponent. The reduced-component
pushforward formulation of 7.3.4 then has the same field factors and
restriction maps. These checks justify precisely the inherited portion
used here, without turning a generic local ring into a field prematurely.

The English 0.3.6.1 definition and modern 006W/0081 identify the historical
“simple” with constant sheaf. On an irreducible nonempty space every
nonempty open and every finite intersection of such opens is nonempty;
this makes constant presheaves sheaves and makes the overlap identifications
of locally constant sheaves compatible. It is not the definition of a
simple object in a module category. In 0.5.1.1 a map from a rank-one free
sheaf is determined by its value at 1; a map from an arbitrary sheaf direct
sum is determined by one such section for each summand. This does not
replace sheaf sections of arbitrary sums by products or give a uniformly
finite matrix. The overly broad direct-sum closure sentence in 0.5.1.3
is explicitly excluded, in accordance with 02CF.

### 7.3.5: arbitrary sums, cokernel, and canonical global gluing

For nonempty irreducible X, every nonempty open contains the generic point
eta, so the inherited result makes R_X the constant sheaf with value
B = O_(X,eta). For arbitrary I, the natural coproduct map from the direct
sum of constant B-sheaves to the constant sheaf B^(I) is an isomorphism
on every stalk. On an irreducible open its sections are exactly B^(I):
a locally constant map has only one nonempty fiber. In particular each
section has finite support, while the index set itself can be infinite.

A local R_X-free presentation therefore gives one B-linear map
u : B^(I) -> B^(J). The image of each basis vector has finite support;
there is no bound on the number of nonzero columns. The constant sheaf
of coker(u) is the sheaf cokernel, since the module sequence is exact
on every stalk. This argument does not take an arbitrary sheaf cokernel
through a right-exact global-sections functor.

All nonempty presentation neighborhoods contain eta. Identifying each
local constant fiber with F_eta by its germ identifies overlap maps with
the same identity. A morphism between constant sheaves on a nonempty
irreducible open is determined by that fiber map. The local identifications
therefore glue to the canonical R_X-linear isomorphism
F = constant(F_eta). Equivalently the generic germ map on every nonempty
open is injective by the local identifications and surjective by their
compatible constant sections. No reducedness, separation, finite rank,
finite presentation, or Noetherian hypothesis has entered.

### Scalar-ring comparison

For an irreducible affine V = Spec(A), the unique minimal prime p is the
nilradical, and B = A_p. For any B-module M, localization at f is M
if f is outside p and zero if f lies in p; in the latter case f is
nilpotent in A and D(f) is empty. Thus the associated A-sheaf of M is
the constant M-sheaf on V, with the same restriction maps. The conclusion
of 7.3.5 consequently is quasi-coherent as an underlying O_X-module.

Conversely, 01BK gives an associated-module presentation near a point
because a scheme has a basis of quasi-compact affine neighborhoods.
If that initial neighborhood is not affine, refine to an affine one and
use 01BJ and 01I7; this is why the manuscript's refinement clause matters.
The existing R_X-action gives a B-action on M = Gamma(V,F). A free
B-presentation sheafifies exactly as A-modules by 01HV. It is compatible
with the prescribed rational action: a fixed b in B induces the same
endomorphism on global sections, hence on the associated sheaf by 01I7,
and every local rational section is locally such a b. This proves the
two named quasi-coherence conventions agree here. It neither declares
an arbitrary R_X-module quasi-coherent nor proves such equivalence for
an arbitrary ringed space.

### 7.3.6: tensorization and basis choice

Tensoring a local O_X-free presentation with R_X is right exact stalkwise,
and tensoring commutes with arbitrary direct sums. Thus the resulting
module G has an R_X-free local presentation. The tensor-stalk identity
can itself be checked by representing the finitely many tensor generators
and relations on a common neighborhood; filtered stalk colimits give
(F tensor R_X)_eta = F_eta tensor_B B = F_eta. The printed omission at
01CB is not mistaken for a supplied proof. Applying the preceding constant
sheaf argument gives a canonical isomorphism G = constant(F_eta).
The change of ring is the identity-on-spaces morphism of ringed spaces;
it need not be a morphism of locally ringed spaces.

If X is reduced, B is a field by minimal-prime localization. Choosing
any vector-space basis of F_eta identifies it with B^(I), with arbitrary
I and finite support in each vector. This gives G = R_X^(I), but that
free-module isomorphism is not canonical. The generic-fiber isomorphism
remains canonical. The empty basis covers the zero module. The additional
presentation proof is correctly labeled an independent expansion of the
first assertion, not invented text in the printed one-sentence proof.

### 7.3.7: local hypotheses and reduced injection

Integral open neighborhoods have one component. Noetherian affine
neighborhoods have finitely many components by 01OZ and 0052. The
restriction identity R_X|U = R_U and the finite-component associated-module
calculation therefore give quasi-coherence locally and hence globally.
No global finite-component hypothesis is needed. More generally, the
irreducible components meeting an open U correspond exactly to the
components of U: intersect a component with U, or take closure in X
of a component of U, and use maximal irreducibility. Consequently a
Noetherian topological neighborhood meets only finitely many global
components. This justifies the weaker, purely topological local
Noetherianity premise of 7.3.3 without asserting its coordinate rings
are Noetherian. The wording finding below concerns the direction of
generality, not this valid argument.

For any reduced scheme, a germ in the kernel of O_X -> R_X becomes
zero in the rational presheaf after shrinking, because sheafification
preserves stalks. It therefore vanishes on a dense open D. On any affine
refinement Spec(A), the representing element a cannot be invertible at
a point of D, so its principal open D(a) is disjoint from the dense
open D intersect Spec(A). Thus D(a) is empty, a belongs to every prime,
and a is nilpotent. Reducedness makes a zero, so the original germ is
zero. This proves injection with no component-finiteness or separation
assumption. Locally integral schemes are reduced by their integral
neighborhoods, so the injection is automatic in that branch.

The complete source 7.2.2–7.2.3 argument is consistent with this use:
for two maps from a reduced scheme to a separated target, their closed
equalizer contains the dense open of agreement. Its defining ideal
vanishes on that dense open; on a reduced affine open the same nilpotence
argument makes the ideal zero. The maps agree and glue over their full
domain. For functions the affine-line target is separated; the source
scheme is not required to be separated. This supplies the consequence
actually used without reinterpreting the target's hypothesis as one on X.

### Adverse examples independently checked

1. At Spec(k), k^2 is constant but contains the proper nonzero submodule
   k direct-sum 0. Historical “simple” cannot mean simple module.
2. On Spec(k[t]), the topological skyscraper with value K = k(t) at a
   closed point x has a constant-K scalar action. Its stalk at x is K;
   at the generic point one may choose an open excluding x, so the
   generic stalk is zero. It is not constant and hence not R_X-quasi-coherent.
   The notation refers to a sheaf on a topological point and does not
   require a residue-field-module interpretation of K.
3. On two disjoint k-points, the quasi-coherent module with fibers k and
   0 is not a constant sheaf. A fixed nonempty index set for R_X^(I)
   would give a nonzero fiber at both points, while the empty set gives
   zero at both. Both global conclusions need irreducibility.
4. For B = k[e]/(e^2), the one-point scheme has O_X = R_X = B. The
   module k = B/(e) is constant and quasi-coherent, but nonzero and
   annihilated by e. A nonzero free B-module is not annihilated by e,
   even with infinite rank. This refutes freeness without reducedness.
5. In A = k[t,e]/(e^2,te), e is nonzero because setting t = 0 leaves
   the dual numbers. The space is the irreducible affine line and D(t)
   is dense. There e becomes zero, and the generic localization is
   k(t), so the rational structure map kills e. Localization at all
   non-zero-divisors remains injective; t is a zero divisor. This
   distinguishes dense-open R_X from regular-denominator K_X.
6. The same one-point dual-number scheme has the identity structure
   map O_X = R_X despite being nonreduced. Reducedness is sufficient
   for injection, not necessary.
7. Empty X has the zero sheaf and empty direct sum but no generic point.
   The manuscript explicitly restricts its generic-point arguments to
   nonempty irreducible X and treats the empty case separately.

Editorial confidence is high because of the complete source comparison,
independent stalk/module calculations, and checked counterexamples. This
is an uncalibrated editorial assessment, not a probability.

## Mechanical review and completed checks

The checker fixes independent URL, whole-byte/hash, raw-LF, span, wrapper,
label, page-marker, literal-content, and next-excluded-boundary contracts.
Receipt fields cannot self-authorize changed content: strict recursive
comparison rejects changed inventory and bool/float substitutions for
integers. Its exact raw-byte certification is separate from its ASCII
whitespace/comment-normalized content check. The latter never replaces
the former. French proof prose remains unwrapped; all three English
proof wrappers and bodies are separately bounded; blank separators
cannot absorb an extra independent argument; no old heading is re-owned.

Each source transport uses one read capped at the fixed length plus one,
with a 30-second network timeout and no retry. Both language contracts
are validated before either source read. The cached route performs no
network request. Raw LF splitting, UTF-8 validity, BOM/CR rejection,
maximum size, duplicated JSON keys, and malformed contracts are handled
fail-closed. The imported comment parser correctly distinguishes escaped
percent signs using preceding-backslash parity. Whole-file identity
still rejects changes outside the reviewed semantic interval.

Executed offline, with bytecode writes disabled:

```text
python -B -m unittest discover -s tests -p 'test_ega_i_737_source_boundaries.py' -v
Ran 25 tests in 0.625s
OK
```

The independent literal fixtures agree with the source passages in the
evidence. Their surrounding bytes are explicitly synthetic, and the test
suite verifies they fail whole-source certification. The tests cover all
contract leaves, every substantive declaration/proof line, hypothesis,
quantifier, scalar ring, tensor formula, source cross-reference, source
notation drift, wrapper displacement/duplication, page markers, excluded
boundaries, malformed byte inputs, transport failures, exact inventory,
and CLI no-write behavior. This is mechanical evidence only, not an
automated proof of the mathematics.

A separate read-only PowerShell calculation verified all 17 embedded
source spans' UTF-8 length, SHA-256, LF counts and byte-interval lengths.
For all 36 modern blocks it re-read the 14 exact Git blobs and checked
whole length/hash, exact text, span length/hash, byte endpoints, and
physical LF boundaries. The 36 tag mappings and seven current full source
files matched their declared pins. No discrepancy was found. This review
did not freshly fetch the complete French/English remote source files;
the independent full-source replay remains a production check owned by
the implementing agent.

## Concrete finding and scope limits

`737-R1` — **resolved** minor wording correction in `ega/i737.md`, 7.3.7's paragraph
beginning “This is a local argument.” The reviewed initial sentence started
“The stronger premise of 7.3.3, a locally finite family of irreducible
components, also suffices.” Locally finite components is a more general,
weaker hypothesis than the local-integral/local-Noetherian alternatives;
it is the conclusion's generality, not the premise's strength, that
increases. The implementing agent replaced “The stronger premise” by
“The more general hypothesis.” I read the revised manuscript completely
and verified its SHA-256:
`9A32D1C92B5CEF907AC8455C4DECAFA0927C508F933618CF12156D53D0AFDFE8`
(16,005 bytes). Reversing exactly this phrase in memory and restoring
one removed terminal blank line reproduces the initial manuscript hash;
there is no additional textual change. The checker and test hashes are
unchanged. The finding does not invalidate the proof or any source
comparison. No manuscript, checker, or test was edited by this reviewer.

The initial review did not certify historical ledger prefixes, the twelve
earlier residual-gap bytes, or the final semantic cursor; the bounded
production-contract extension below now covers those assigned objects.
No build, TeX engine, PDF rendering, Lean/Lake process, publication,
source-edition change, cleanup, sidebar mutation, or broad workspace/Git
scan was performed. The only public file written by this reviewer is
this review; its verbatim task inputs are retained in a private control log.

## Completed production-contract extension

Disposition: **PASS, with two evidence-link/provenance corrections resolved**.
No substantive mathematical or contract-wiring defect remains in the
reviewed objects. This extends, rather than restarts, the preceding review.

The complete new `tools/ega_i737_semantic_contract.py` and
`tests/test_ega_i_737_semantic.py`, complete migrated
`tools/ega_i734_semantic_contract.py` and
`tests/test_ega_i_734_semantic.py`, changed `ega/check.py` sections and
its live-table/tag-loader connections were read. The semantic receipt
`validation/ega-i-7.3.5-7.3.7-semantic-checkpoint-2026-09-08.json` was
reviewed by its actual fields: source authority/discovery, complete
passages, paired targets, choices, normalization, semantic propositions,
ledger rows, preserved inputs/gaps, snapshots, dossier and review binding,
and nonclaims. Its repeated source and target texts were compared exactly
with the already-read preparation evidence, rather than treated as new
unread source attestations. The live appended ledger rows and scope
changes were checked independently.

### Findings resolved in the implementation

`737-R2` — the three original `target_text_ref` values used fragments
`#7.3.5`, `#7.3.6`, and `#7.3.7`, but the dossier had neither matching
explicit anchors nor those generated heading slugs. Thus the audit links
did not resolve to the declared target segments. The implementation now
uses unique explicit anchors `ega-i-735`, `ega-i-736`, and `ega-i-737`.
Each choice carries the exact matching `target_segment_id`,
`target_text_ref`, and independent `target_text` from that anchored section.
I read those three exact target texts, verified their manuscript intervals,
and ran the new regression test. The last segment deliberately includes
the final adverse-example section; its bytes are not silently truncated.

The dossier immediately after that anchor repair was 16,077 bytes, SHA-256
`17D43D8C0BE58435358E90C063ECD9545A7B856786ED5D3D947F091798CEEF2F`.
Removing only the three explicit anchor lines and their following blank
lines in memory reproduces the prior reviewed dossier hash
`9A32D1C92B5CEF907AC8455C4DECAFA0927C508F933618CF12156D53D0AFDFE8`.
The mathematical text was not otherwise changed by this repair.

`737-R3` — the copied first two normalization confidence fields originally
described direct visual confirmation without locally identifying whose
reading it was, although other receipt fields correctly attributed the
historical PDF reading. Those confidence fields now explicitly attribute
the original French Chapter 0 visual confirmation to the preflight source
reviewer. Every normalization decision also has an explicit
`consultation_provenance` distinguishing that attributed reading from the
implementation owner's reading of the exact short quotation, full English
comparison, and modern/source passages. This does not invent a new visual
reading by either the implementation owner or this reviewer.

The verbatim task-input block was removed from this public record and
preserved in the authorized private control log. Public mathematical
evidence and the review's consulted-object identities remain intact.

### Final skyscraper clarification independently verified

The final dossier additionally spells out the topological skyscraper in
adverse example 2: S_x(U) is K when x belongs to U and zero otherwise;
restrictions are identities between opens containing x and zero when
the target open omits x. The constant rational sheaf acts by multiplication.
The underlying O_X-action at x is induced by O_(X,x) -> K, not by the
residue-field quotient. This action does not factor through kappa(x):
the nonzero generator of the closed point's maximal ideal acts invertibly
in K, whereas it would act by zero on a module pushed forward from the
closed subscheme Spec(kappa(x)). The revised paragraph is mathematically
correct and removes the possible ringed-closed-point interpretation of
the earlier topological notation. Its generic stalk is still zero.

The **final reviewed manuscript** is 16,406 bytes, SHA-256
`4AF5241FB491CAFDCD7484D359E2C06286BE5DC3AE4DAEE139B8643AD8FDCBB2`.
The explicit new semantic-test expectation was read and checked:

```text
adverse_skyscraper_scalar_action:
S_x(U)=K if x in U and zero otherwise; identity or zero restrictions; O_Xx to K action, not a module pushforward from Spec kappa(x)
```

At this review's completion, updating the receipt's exact D000371 target
text, this additional semantic field, and its dossier/review bindings is
the implementation owner's already-specified final sealing operation.
The exact-link regression and final semantic suite must run on that sealed
postimage. The earlier focused regression result below precedes this last
clarification and is not misrepresented as a test of the future reseal.
There is no unresolved mathematical finding in the clarification.

### Historical migration and runtime wiring

The 7.3.1–7.3.4 receipt remains immutable, with SHA-256
`B9C0C421F58F12064B8F6B37FE5E45F111631510F396C24E0CEA26E88DE591A4`.
Its new `historical_inputs` first authenticates that sealed receipt, then
extracts each old complete ledger postimage from the live physical-LF
prefix and checks its exact byte length and hash before parsing it.
The old active rows are reconstructed from that frozen prefix, not from
the mutable successor ledger. Only the historical snapshots and cursor
are projected back; existing source-scope entries remain taken from the
live scope and are checked by the old verifier. The old receipt's
semantic/source/target/ledger verification is not weakened or resealed.

The changed root wiring calls that historical verifier with its projected
loader and calls the new 7.3.5–7.3.7 verifier with the real current
`i665_tables` values: active decisions, statement edges, residual rows,
and agent rows. These values are not historical projections despite the
older variable name. The new verifier checks the entire current ledger
postimages and compares the supplied active tables against fresh parsing
of those bytes. Consequently accepting an arbitrary successor suffix in
the historical-prefix unit test does not exempt it from the successor
validator or the root checks. Source/tag loaders retain their exact pins.

The known routine changes to the root checker are bounded: final scope
and four ledger pins advance; the closed reviewed-source inventory adds
only 7.3.5–7.3.7; the old historical call is projected; and the new current
contract is invoked before the existing privacy check and final result.
No earlier source slice is removed. No 7.3.8 source content is admitted.
The sorted public agent-write inventory also matches the actual row.

### Receipt, source, target and ledger agreement

An independent read-only comparison found all 17 source passages exactly
retained from the preflight: full source identities, each exact text,
span hash/length, and original byte/LF locations. All 36 target blocks
retain their separately verified official/integrated texts and identities.
The original Chapter 0 PDF review remains attributed. The inherited
F37ZW manifest binding is explicitly sourced from the unchanged prior
receipt; this continuation does not claim a fresh archive retrieval.
The fresh complete-source network replay was reported PASS by the
implementation owner, not independently performed by this reviewer.

For each of the four ledgers, the new receipt's prefix row count, byte
length, and SHA-256 equal the old 7.3.1–7.3.4 receipt's entire postimage.
The actual live byte prefixes match those identities. The new complete
postimage hashes and all parsed appended rows match the new receipt:

| Ledger | Preserved rows | New rows | Final rows | Reviewed new IDs |
| --- | --- | --- | --- | --- |
| `ega/dec.csv` | 368 | 3 | 371 | D000369–D000371 |
| `ega/smap.csv` | 1466 | 22 | 1488 | S001467–S001488 |
| `ega/resid.csv` | 945 | 10 | 955 | R000946–R000955 |
| `ega/agent.csv` | 282 | 2 | 284 | A000283–A000284 |

Each of the three choice decision IDs joins to exactly its declared
ordered edge IDs and modern target tags. Each choice's French source
text is exactly the declared unit passage. The 22 edges explicitly
describe components or qualifications of the independent derivation,
not 22 equivalent whole theorems. In particular 01J1/01J2 supply the
reduced-ring component of the independently proved dense-open injection;
they are not standalone citations for preservation of sheafification
stalks or for the complete injection argument. Likewise the basis choice
is supplied by the independent vector-space argument, while 01RV supplies
the field identification. The 02CF warning remains a qualification.

The six English discovery rows remain exact and `unreviewed` in the
discovery inventory; semantic source admission does not rewrite that
inventory's provenance. The three added French source scopes match the
receipt's whole-unit boundaries. No heading or neighboring proof is
re-owned. The live cursor is exactly `ega:I.7.3.8`.

Independently recomputed live counts agree: 1,488 statement-map rows,
1,469 active rows, 19 superseded rows, 479 source units, 1,456 existing
official-tag rows, 384 distinct existing tags, 13 local untagged rows,
and 62 rows satisfying both `relation=equivalent` and
`coverage_claim=full_statement`. The latter is not the count of every
row whose relation alone is `equivalent`. Residual counts are 955 raw
rows, 922 active rows, and 33 superseded rows. All 12 active prior gaps
retain their exact IDs and every field; none is superseded or closed
by the new append. The new ten residual entries state the bounded
derived coverage and its limitations, not completion of all EGA.

### Additional executable checks and artifact identities

The three additional focused regression tests passed in 1.657 seconds:

```text
test_choice_segment_links_resolve_and_bind_exact_target_text
test_historical_projection_accepts_successor_append_without_changing734
test_historical_projection_rejects_prefix_damage_and_rewritten_receipt
Ran 3 tests
OK
```

They were run with Python bytecode writing disabled. The earlier 25
source-boundary tests remain completed evidence; unchanged tests were
not repeatedly rerun. The complete new and migrated semantic test code
was read, including actual raw target/ledger corruption tests and the
new exact target-segment regression. These tests distinguish immutable
receipt metadata from the actual byte objects being checked. The final
complete suite and scaffold run belong to the implementation owner
after this record's artifact binding is sealed; this review does not
misreport that future run as already executed.

| Reviewed implementation object | SHA-256 |
| --- | --- |
| Final `tests/test_ega_i_737_semantic.py` | `E2A5CB59A6B5BAF9E3792F1CFFA7489F5DAF98583358B8EA836A08FE0969A216` |
| `tools/ega_i734_semantic_contract.py` | `7D655C034A59AB9DC0E494F55B4AB850D0B26886707E3CD0929CF952929A4CCB` |
| `tests/test_ega_i_734_semantic.py` | `41D388A92973F3BB3D05A3C400163FD098ADEE8D51934C43F1D5D8738B9019A2` |
| `ega/check.py` | `2FFA67EBCD5851F128A4AEB0996BC9609879DBDEEE4BE97A787F5BFE336E533B` |
| `ega/scope.json` | `D723D088DC738B19810B72898EBA4118E4E32F67C3528D083B62D8DD24A86728` |

To avoid a circular review/receipt hash dependency, this record does not
pin the new contract's whole-file hash before its final sealing operation.
Its complete verification-function suffix, beginning at the literal
`def digest(raw):` and continuing through EOF, has UTF-8 SHA-256
`5F944E9978805B152D150358886BE64935109454EA1E811467C999C5AD2E81EF`.
This identifies the reviewed verification logic, not its preceding global
constants. Those global source/target/semantic expectations were also read
and checked as described above; the final skyscraper semantic addition is
quoted exactly. The dossier's final identity is separately stated above.
Final sealing can proceed from this finished review to the updated receipt
and its runtime seals without rewriting the review to chase its own hash.
This completes the assigned independent review; there is no human-dependent
gate or unresolved review finding.
