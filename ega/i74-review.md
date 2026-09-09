# Independent mathematical review of EGA I 7.4.1–7.4.7

Date: 2026-09-08. Reviewer: Codex AI reviewer, independent task identity
`/root/ega74_implementation/final_review`. This reviewer did not author the
candidate manuscript or its prepared predecessor. The review was not blind:
the earlier mathematical preflight was read as evidence, after the complete
candidate, and each argument was independently checked rather than accepted
on the earlier reviewer's conclusion. This is an AI mathematical review, not
human expert approval or formal proof verification.

## Disposition and exact object

**Mathematical review passed, with no unresolved mathematical finding in the
seven-unit comparison as read.** The literal source claims rejected in 7.4.4
and the superseded version of 7.4.7 are not thereby certified as true. Their
counterexamples, sufficient repairs, and source-version distinctions are
part of the object that passed. The independent strengthenings in 7.4.5,
7.4.6, and 7.4.7 were checked separately from the printed claims.

The object read in full is `ega/i74.md`, 19,207 bytes, SHA-256
`828336F9F505DAFCBD9C5DF17739D4917F9FBB078E3CA937D964986D82F9368E`.
That digest was recomputed from the working file during this review. This
receipt applies to those exact bytes; substantive subsequent changes require
a bounded review of what changed, not repetition of unchanged work.

The task did not edit that object, any source edition, any Stacks theorem,
the tags registry, or the admission ledgers. Its only authored file is this
review receipt. No TeX, Lean, publication, commit, or cleanup operation was
performed by this reviewer.

## Evidence actually read

The complete French and English subsection passages embedded in
`EGA_I_7_4_1_7_SOURCE_PREPARATION_20260908.json` were read, including the
heading, all seven units, the rank paragraph, all three full source proofs,
and the page marker in the proof of 7.4.5. Their source spans are French
LF672–786 and English LF403–466. These are the source identities recorded in
that preparation:

- French: `KokunoYumeto/ega-fr` commit
  `6b38875842e3723b619d4aeeda9ed260a4f94f7c`,
  `source/ega1/ega1-7-fr.tex`, whole-file SHA-256
  `73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522`;
  subsection SHA-256
  `D03397BDE8F9E84049541D6655294BC8522D29EE09CCA0288A3F022A5A187800`.
- English discovery witness: `KokunoYumeto/ega-en` commit
  `94d5c73ac9263b26043ad0551646b824b1030c9b`,
  `source/ega1/ega1-7.tex`, whole-file SHA-256
  `B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC`;
  subsection SHA-256
  `78FB59B32F1A355403892294271E94B73DC8FC36E3B4AF684CA8F529B68B1FB5`.

The historical source-preparation limits and preflight provenance limits
were not silently rewritten. The following three local input digests were
independently recomputed; unlike the preceding transcribed source digests,
these are direct byte checks by this reviewer:

| Input filename | Bytes | SHA-256 |
| --- | ---: | --- |
| `EGA_I_7_4_1_7_SOURCE_PREPARATION_20260908.json` | 19084 | `D0E64F5CC01F6A411B2B3EF8B3378FBE8E9BE67527E09C871D69C69700CD943C` |
| `EGA_I_7_4_1_7_INDEPENDENT_PREFLIGHT_20260908.md` | 21834 | `FDCA81F98658034AD0B70A26E0DEB2170722B8B7AF8EB4D94730A1A4CC71C4C1` |
| `EGA_I_7_4_1_7_PRINT_AND_ERRATA_BINDING_20260908.json` | 16421 | `BC58FFC0193A85DB94DD17F5D532FF6934598E89AC66E538475B978D84AF1E65` |

The complete preflight and the complete additive print/errata receipt were
read. The latter attributes the original EGA I printed pages 163–164,
DOI `10.1007/BF02684778`, and the relevant later printed errata to the
historical source reviewer. This reviewer did **not** inspect those images
anew, fetch or hash the source PDFs, perform a new original-print collation,
or repeat a comprehensive errata search. In particular, the existing
Err_III12 replacement in EGA III, second part, Liste 2, printed p.88
(additional footer 220), DOI `10.1007/BF02684890`, is attributed printed
evidence, not a newly discovered correction. No universal absence or novelty
claim is made about 7.4.4.

### Exact Stacks target comparison

Using the read-only `--targets` operation of
`ega74_candidate_build_20260908.py`, this reviewer read every complete target
statement and its complete displayed proof block at both exact commits:

- Official: `a04446e57ec1fbc252a871afcec7752fb2807b14`.
- Integrated predecessor: `c9c1b046e2d8f353edaaf51a4311cb8827f03cfb`.

The ranges below are one-based LF ranges of the exact Git source blobs,
including displayed proof blocks where present. They are not a claim that
every proof is supplied in Stacks: several explicitly say that the proof is
omitted, and 0537 points to the preceding discussion.

| Tag | File | Official LF | Integrated LF | Relevance actually checked |
| --- | --- | --- | --- | --- |
| 0536 | `more-algebra.tex` | 4781–4792 | 4785–4796 | Torsion over a domain; no finite-generation hypothesis. |
| 0537 | `more-algebra.tex` | 4801–4811 | 4805–4815 | Fraction-field kernel and torsion-free quotient. |
| 0AUR | `more-algebra.tex` | 4813–4822 | 4817–4826 | Localization preserves torsion-freeness. |
| 0AUT | `more-algebra.tex` | 4850–4861 | 4854–4865 | Maximal-localization test for module torsion-freeness. |
| 0AXR | `divisors.tex` | 1649–1665 | 1649–1665 | Generic-germ detection is stated for quasi-coherent sheaves. |
| 0AVR | `divisors.tex` | 1667–1677 | 1667–1677 | The Divisors definition is in the quasi-coherent category. |
| 0AXS | `divisors.tex` | 1682–1695 | 1682–1695 | Affine sections test within that category. |
| 0AXT | `divisors.tex` | 1697–1709 | 1697–1709 | Quasi-coherent torsion subsheaf and quotient. |
| 0AXW | `divisors.tex` | 1749–1759 | 1749–1759 | Stalk test within that category. |
| 01B8 | `modules.tex` | 875–894 | 889–911 | Finite generators spread stalk surjectivity to a neighborhood. |
| 01B9 | `modules.tex` | 896–910 | 913–927 | Finite-type zero stalk gives local vanishing. |
| 01BA | `modules.tex` | 912–924 | 929–950 | Finite-type support is closed on a ringed space. |
| 0CC1 | `morphisms.tex` | 1407–1449 | 1407–1449 | Dominance for integral schemes and all local-ring injections. |
| 01RV | `morphisms.tex` | 12704–12739 | 12807–12845 | Finite generic-local-ring product for rational functions. |
| 01CB | `modules.tex` | 2332–2348 | 2464–2483 | Tensor product is computed on stalks. |
| 0H7H | `sheaves.tex` | 1398–1414 | 1462–1478 | Sheaf monomorphisms/epimorphisms detected on stalks. |
| 00DK | `algebra.tex` | 2087–2121 | 2096–2130 | Tensoring with a localized ring is module localization. |

No mathematical alteration of these target statements or displayed proofs
was found between the two versions. The integrated blocks for 01B8, 01BA,
01RV, and 01CB have FAC reference additions, with a history addition in
01BA; these additions were not misrepresented as official wording.
The live official pages for [0CC1](https://stacks.math.columbia.edu/tag/0CC1),
[01RV](https://stacks.math.columbia.edu/tag/01RV), and
[0AXR](https://stacks.math.columbia.edu/tag/0AXR) were also consulted as a
bounded primary-source cross-check. The pinned Git blocks, not the mutable
web pages, govern this version-specific review.

## Independent proof checks and challenges

### 7.4.1 — arbitrary module sheaves

At every point the rationalization map is the localization map of an
arbitrary module over a domain into its tensor product with the fraction
field. A localized element is zero exactly when some nonzero denominator
annihilates it. Thus the candidate's torsion kernel agrees with algebraic
torsion on every stalk without assuming quasi-coherence. The stalk of the
quotient embeds in a vector space over that field, and multiplication by a
nonzero ring element is invertible there; the quotient is torsion-free.
For a quasi-coherent sheaf the affine kernel is the module kernel sheafified,
so it is quasi-coherent. The candidate restricts precisely this last claim,
not the definition or quotient assertion, to quasi-coherent sheaves. The
extension from the cited quasi-coherent Stacks statements is justified by
the explicit stalk proof, not by deleting their hypotheses. Pass.

### 7.4.2 — arbitrary rank and generation

On an affine chart, tensoring the representing module with the function
field produces the generic fibre. The sheaf associated with this vector
space is constant on the integral scheme: every nonempty open is
irreducible, and the field localizations have identity restrictions.
The canonical map is injective exactly under torsion-freeness. Choosing a
basis gives a possibly infinite direct sum of copies of the field; it is
not a product and is not a canonical basis choice. Every tensor is locally
a finite sum of pure tensors, so the image generates the rationalization
as a sheaf of rational modules. This does not assert that global tensor
sections are all global pure-tensor sums. Further localization on any
nonempty affine chart gives the same vector space and therefore the same
cardinal rank, including zero. No hidden finite-rank hypothesis is needed.
Pass.

### 7.4.3 — the exact converse

A nonzero quasi-coherent submodule of the rational-function sheaf is
torsion-free and has a generic fibre that is a subspace of the function
field. If that fibre were zero, the injective generic-fibre map from 7.4.2
would make the whole sheaf zero. Its generic dimension is therefore one.
The zero submodule is correctly excluded. To challenge quasi-coherence of
arbitrary submodules, the displayed kernel of the germ map to the local-ring
skyscraper has zero stalk at the closed point but nonzero generic stalk.
For a quasi-coherent sheaf generic localization is a further localization
at that closed point, which rules out that combination of stalks. This
really is a non-quasi-coherent submodule of the rational-function sheaf.
The manuscript gives a scope qualification without a novelty claim. Pass.

### 7.4.4 — two different defects, not one

The sheaf property of the proposed skyscraper is valid: all members of a
cover containing the closed point have intersections containing that
point, so compatible nonzero values agree, and the remaining members carry
zero. Closedness of the point supplies an open complement and makes every
other stalk zero. The only nonzero stalk of the field-valued version is the
function field over the local domain, a torsion-free module. Distinct
closed points give disjoint stalk supports, so the tensor sheaf is zero by
01CB although both global sections named 1 are nonzero.

The action factors through the **local ring**, not the residue field. In
the field-valued example the parameter at the closed point acts invertibly;
it would act as zero under the residue-field closed-immersion action. The
candidate explicitly prevents that incorrect replacement. Replacing the
field by the local ring still gives torsion-free stalks and disjoint support.
The germ map from the structure sheaf is the identity at the distinguished
stalk and surjective onto zero elsewhere. Hence it is a sheaf epimorphism
and the skyscraper is finite type. This proves that finite type alone does
not repair the assertion; global sectionwise surjectivity was not used.

With both sheaves quasi-coherent and torsion-free, the generic section maps
are injective. A nonzero vector in an arbitrary vector space admits a
linear functional taking it to 1, so tensoring that functional proves a
pure tensor of two nonzero vectors is nonzero. This proves the sufficient
repair in arbitrary rank. It also isolates the second printed proof defect:
general generic fibres are not subspaces of the one-dimensional field.
The example of a free rank-two sheaf refutes that inference independently
of the missing quasi-coherence hypothesis. Both challenges are correctly
resolved. Pass.

### 7.4.5 — printed proof and arbitrary-sheaf strengthening

The printed quasi-coherent argument is sound. Dominance sends the source
generic point to the target generic point and injects their function fields.
The inverse image of a nonempty target open is a nonempty irreducible open.
The constant sheaf with any vector-space fibre therefore has exactly that
fibre as its sections there; direct image is the same constant sheaf on the
target, with the restricted field action. Left exactness preserves the
embedding of the original sheaf. No quasi-coherence of the direct image is
asserted or needed.

I separately challenged the removal of source quasi-coherence. A germ of
a direct-image section and a nonzero target scalar admit representatives
on a common neighborhood. Equality of their product to zero as a germ
permits shrinking that neighborhood. On an integral target the scalar has
a nonzero rational value; dominance keeps that value nonzero in the source
function field. Consequently its pullback is nonzero in every source local
ring over the neighborhood. Torsion-freeness of the arbitrary source sheaf
then kills the section at every stalk, hence as a section. This proves the
claimed strengthening for **any** torsion-free module sheaf. The argument
does not require surjectivity, quasi-compactness, separation, finite type,
or finite rank. It does not use the superseded global rational-pullback
isomorphism from 7.3.8. Pass.

### 7.4.6 — proper support is not closed or nowhere dense

Quasi-coherence identifies rationalization with the generic fibre sheaf,
so torsion is equivalent to zero generic stalk. Finite type makes support
closed by finitely many local generators, and on an irreducible space a
closed subset containing the generic point is the whole space. This checks
the original finite-type argument.

Independently, if any stalk of a quasi-coherent sheaf on an integral scheme
vanishes, its generic stalk vanishes by further localization. Conversely,
a zero generic stalk itself gives a missing support point. These two
implications prove the literal proper-support equivalence without finite
type. They do not prove closed support. In the direct sum of all
closed-point residue modules over the polynomial ring in one variable over
the rationals, localization at a closed point leaves its corresponding
nonzero summand, while generic localization kills every element, since
each has finite support and a common nonzero annihilator. Every nonempty
principal open contains a rational closed point avoiding the finitely many
roots of its defining polynomial. The support is therefore dense and
proper, and the sheaf vanishes on no nonempty open. This explicitly refutes
the stronger nowhere-dense formulation without finite type. The earlier
local-ring skyscraper separately excludes removal of quasi-coherence.
Pass.

### 7.4.7 — the known replacement is genuinely local

For the two-field product ring, the rational-function sheaf equals the
structure sheaf. The idempotent summand has one-point support but its
rationalization is the identity on a nonzero sheaf. It is not torsion.
This valid finite-type quasi-coherent counterexample refutes the old merely
proper-support extension, not the later Err_III12 replacement.

The candidate states the erratum's **local** hypothesis: every point has
an open neighborhood with finitely many irreducible components. Such a
neighborhood can be refined to an affine chart still having finitely many
components. On a reduced such chart the rational ring is the finite product
of the fields at its minimal primes. Tensoring a module with this finite
product is the direct sum of its localizations at those primes. Thus
rationalization vanishes exactly when all chart component generic stalks
vanish. A global component that meets an open contains its generic point
in that open; the chart components correspond to the global components
meeting the chart. The test therefore glues without requiring a globally
finite list or commuting a tensor product with an infinite product.

For a quasi-coherent sheaf, a nonzero component-generic stalk forces a
nonzero stalk at every specialization in that component, again by further
localization. Thus excluding component generic points from support is
equivalent to excluding entire components even for arbitrary quasi-coherent
sheaves. With finite type, closed support excluding every component is
nowhere dense: on every finite-component chart the complementary open is
dense in each component. Conversely, on such a chart each component has a
nonempty open part away from the other finitely many components; a closed
set containing that component cannot be nowhere dense. This justifies the
dense-open vanishing reformulation exactly where the manuscript uses it.
Without finite type the generic/component-exclusion criterion remains, but
the preceding dense-support example rules out the stronger reformulation.
Pass.

## Limits and completed-review meaning

The conclusion is based on the explicit sheaf, stalk, field, localization,
and support arguments above, not on matching expected hashes or a semantics
dictionary. Hashes identify the reviewed evidence; they do not establish
the truth of its mathematical assertions. The supplied arguments use the
usual basis/linear-functional existence for vector spaces. No choice-free
reformulation is claimed.

Editorial mathematical confidence is high because the critical hypotheses
were challenged with concrete counterexamples and both directions of the
derived equivalences were proved. This is not a calibrated probability.
The review is bounded to this seven-unit candidate and its named target
blocks; it does not certify the rest of EGA, close the twelve inherited
open gaps, assign official Stacks tags, or certify release/public bytes.

No human action is a prerequisite for using this completed mathematical
review. Deterministic implementation checks are a distinct operation; any
subsequent code-audit supplement must name the exact files actually read
and report what its tests demonstrate without presenting them as a
mathematical proof checker.

## Independent code-audit supplement — 2026-09-09

Reviewer: Codex AI reviewer, independent task identity
`/root/ega74_finish_candidate/code_review`. The continuation owner recorded
the reviewer's actual findings and resolution below. This is a separate
bounded code review, not a second mathematical review and not attribution
of the new code audit to the earlier mathematical reviewer. The complete
preceding mathematical receipt is preserved as its original byte prefix,
whose SHA-256 is
`FD199082B272DBB1F01A780967C7D5BD8EF43908D8F672DBE9761685D7B5DD1E`.

The code reviewer read the seven code/test files named below and the
preceding review, including the narrow predecessor diff for the two 7.3.8
files and the relevant `ega/check.py` wiring. The audit covered receipt-seal
ordering, live-byte binding, malformed runtime views, source ownership,
historical ledger-prefix preservation, and the 7.3.8 historical projection.

One concrete minor finding was made: after validating source bytes as
UTF-8, the source-boundary helper decoded environment tokens as ASCII.
Replacing the French fixture's `\begin{env}[7.4.1]` by
`\begin{é}[7.4.1]` made `verify_source` raise `UnicodeDecodeError` instead
of returning diagnostic failures. The command-line entry point already
caught that exception as `ValueError`, so this was not an acceptance
bypass. The continuation owner changed that token decoding to UTF-8 and
added `test_non_ascii_environment_tokens_return_structured_failures`,
covering both validation functions and all three source versions.

The reviewer then inspected those exact changed lines and independently
reran the original in-memory reproduction using `python -B`. It returned
a failure list containing the wrapper-inventory diagnostic without raising.
The reviewer's final disposition was: **no unresolved concrete findings
remain from this bounded review**. No other concrete finding was found in
the inspected trust boundaries or historical compatibility. The historical
projection remains narrow; the live successor is checked separately by the
7.4 contract. The reviewer did not write files, run the complete suite,
retrieve live sources, re-review the mathematics, or perform a build.

The following are the exact SHA-256 identities returned by that reviewer
after the correction. The semantic helper identity is deliberately
**pre-reseal**: the existing candidate generator updates only its literal
receipt seals after this supplement is included in the checkpoint. Final
frozen byte identities and executed gates are recorded in the implementation
freeze manifest. This table does not claim to hash itself or later seals.

| Reviewed file | SHA-256 |
| --- | --- |
| `tools/ega_i74_semantic_contract.py` | `71F297FEA8318C9CBD1966B5449787BA0417A71B322DB45017FC73BE59FA631F` |
| `tools/check_ega_i74_source_boundaries.py` | `E43B206A35465C7686293078E6C54522EE61A2283F8A6A271285B00F0F5FA189` |
| `tests/test_ega_i_74_semantic.py` | `BCC719D87CF2D13641B28452AA15BF9F5A58AD9EB6AF63A3E49C5D7BAE0395F7` |
| `tests/test_ega_i_74_source_boundaries.py` | `EC70FAB556C27DB38A4FF9A68C2DE9FFA8307633742E611EC77866C7EC136E41` |
| `tools/ega_i738_semantic_contract.py` | `EDC66DD7AAB17CA011D0F1BC494510765AA20D35485C457D2F397D2B77EB5DC8` |
| `tests/test_ega_i_738_semantic.py` | `DE8ACF98EC83A734CEFE82DCA20BC013E08160FBC6939414E0AA8B3047CFCE0C` |
| `ega/check.py` | `CAB90EF596DD820C5E35D13985985064AC6C0A191C717C860348E7A12FE767A4` |

Separately, the continuation owner executed the pre-reseal combined
7.4/7.3.8/7.3.7 semantic and source-boundary suite: 116 tests passed in
52.376 seconds. The full EGA checker passed with no errors. Live French,
English and Err_III12 source-boundary replays passed against all three
pinned whole-source identities. After the concrete fix the source-boundary
module passed all 20 tests, including the new regression, in 3.083 seconds.
These are implementation checks, not evidence of formal mathematical proof.
The final freeze additionally requires replay of the complete affected
gates against the resealed candidate; it does not repeat the unchanged
mathematical review or require human action.
