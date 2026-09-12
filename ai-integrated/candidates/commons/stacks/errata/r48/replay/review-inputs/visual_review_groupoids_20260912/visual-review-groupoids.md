# R48 groupoids actual visual review

Result: **PASS with preserved warnings**. No new blocking visual finding was observed.

The reviewed PDF is `groupoids.pdf`, 55 pages, 731,715 bytes, SHA-256 `8364B86EBD7B74CDF8400838C9C1111AD8CD57C217E29191FB76539AC1E7A1C4`. Its current bytes match the task, render manifest and source-page map. All 64 listed PNG files were independently rehashed: 55 page PNGs, four contact sheets and five sensitive-page PNGs. Verification time: 2026-09-12T16:52:41.2371783Z.

## Actual inspection and limits

All pages 1-55 were actually inspected in the four labelled contact sheets. This establishes a coarse layout review, not exhaustive small-glyph or mathematical review of every page. Pages 20, 28, 33, 34 and 46 were additionally inspected as full-page 180-dpi source PNGs. Their 1530 x 1980 images were displayed by the image tool at 1376 x 1780; this is not a claim of 1:1 original-pixel inspection. Pages 3 and 42 were additionally viewed at their full 816 x 1056, 96-dpi size to assess inherited overfull warnings.

Covered pages: 1-55. Sensitive high-resolution pages: 5. Additional full-page 96-dpi inspections: 2. Unreviewed pages: none. Blocking findings: none.

The PDF skill directed the use of actual rendered-page inspection. No new render, TeX process, PDF mutation, source edit, registry edit or publication was performed. Existing render-manifest provenance was checked against hashes; this review did not independently rerender the PDF or reconstruct the contact sheets.

## Six rendered corrections

- **MC-STK-ERR-1564-OP1**, page 20: Page 20, Lemma 9.9: the new zero case is visible at the start of the proof. It states that the fibre over the unit is the positive-dimensional A, so [d] is not etale, and then assumes d != 0. No clipping or colliding glyphs.
- **MC-STK-ERR-1568-OP1**, page 28: Page 28, Lemma 14.2: the first relation visibly has alpha composed with i*alpha on the left and s*e*alpha on the right. Composition order and star positions match the replacement.
- **MC-STK-ERR-1568-OP2**, page 28: Page 28, Lemma 14.2: the second relation visibly has i*alpha composed with alpha on the left and t*e*alpha on the right. It is distinct from the first relation and matches the replacement.
- **MC-STK-ERR-1565-OP1**, page 33: Page 33, Lemma 15.7: the affine-cover display visibly places t^{-1}(U_i) before s^{-1}(U_j). The union and W_{ijk} indices are present; the display fits.
- **MC-STK-ERR-1567-OP1**, page 34: Page 34, Lemma 15.7 continuation: below the sums, M_{ijk} or M_j tensor_{A_j,s} B_{ijk}, respectively, is visible, followed by both coefficient conditions. The added second module has legible subscript s.
- **MC-STK-ERR-1566-OP1**, page 46: Page 46, Lemma 23.5 proof (2)(a): the coefficient ring is visibly C'_r[x]. The prime is clear and distinct from the nearby C^1_r; the paragraph is not clipped.

Each operation's exact replacement text, source/payload coordinates and PNG hash are recorded in the companion JSON.

## Preserved warnings and limitations

- Page 3: the existing **25.04082 pt overfull box**, source line 220, log line 1291. The lower three-diagram row extends beyond the body-text right margin. All diagram labels and arrows remain within the page, with no clipping or collision observed at the expanded 96-dpi view. This is recorded as inherited, non-blocking overwidth, not as an absent warning.
- Page 42: the existing **1.05727 pt overfull paragraph**, source lines 3989-3993, log line 1833. Definition 21.1 and the adjacent diagram remain readable and contained within the page; no visible clipping or collision was found at the expanded view.
- External chapter references still visibly show `??`, including Varieties/Morphisms on page 20, Properties on page 33, and Algebra/Morphisms on page 46. The task's incoming external-only classification is preserved; this visual pass does not independently recertify every reference namespace.
- The log still states that there were undefined references and that labels may have changed. This is **not a zero-warning or clean-build claim**.
- Read-only Poppler inspection confirms **Tagged: no**. Untagged status is preserved; no accessibility or PDF/UA certification is made.

## Per-page actual decisions

C = contact-sheet layout inspection. H = additional 180-dpi source full-page PNG inspection, displayed downsampled as disclosed above. E = additional full-page 96-dpi inspection. Every page below also has its individual PNG SHA-256 and contact-sheet SHA-256 in the JSON.

| Page | Method | Decision | Actual observation |
| --- | --- | --- | --- |
| 1 | C | Pass at contact scale | Title, contents block and introduction are separated; red link outlines remain visible. |
| 2 | C | Pass at contact scale | Text and displayed relation are contained; Equivalence relations heading is separated from the preceding paragraph. |
| 3 | C + E | Pass; inherited overwidth | Three adjacent lower diagrams extend somewhat beyond the body-text right margin; all labels and arrows remain inside the page with no clipping or collision. Expanded at 96 dpi for the inherited 25.04082 pt overfull warning. |
| 4 | C | Pass at contact scale | Group schemes heading, condition lists and centred square have clear separation. |
| 5 | C | Pass at contact scale | Lemma continuation and examples with displayed equations are orderly at contact-sheet scale. |
| 6 | C | Pass at contact scale | Examples contain several short displayed maps with distinct rows and no gross overlap. |
| 7 | C | Pass at contact scale | Properties heading, lemmas and squares fit the visible body area. |
| 8 | C | Pass at contact scale | Proofs, section 7 heading and lower diagram are separated; no gross clipping seen. |
| 9 | C | Pass at contact scale | Dense proof and enumerated conditions remain in the body area at contact-sheet scale. |
| 10 | C | Pass at contact scale | Lemma/proof blocks and displayed maps are separated; reference outlines remain visible. |
| 11 | C | Pass at contact scale | Dense proof blocks and proposition conditions show no gross overlap or missing content at contact-sheet scale. |
| 12 | C | Pass at contact scale | Multi-line alignment and lemmas below it remain separated and inside the page. |
| 13 | C | Pass at contact scale | Long proof continuation and lower displayed formula have clear page boundaries. |
| 14 | C | Pass at contact scale | Section 8 heading, lemma/proof blocks and coloured reference annotations remain contained. |
| 15 | C | Pass at contact scale | Long proof paragraphs and proof-end marks remain separated at contact-sheet scale. |
| 16 | C | Pass at contact scale | Top square and dense proof below it have clear separation. |
| 17 | C | Pass at contact scale | Long proof with several displayed equations remains within the visible body area. |
| 18 | C | Pass at contact scale | Abelian varieties heading and successive short lemma/proof blocks have consistent spacing. |
| 19 | C | Pass at contact scale | Successive lemma/proof blocks and lower formula are clearly separated. |
| 20 | C + H | Pass; correction visible | Lemma 9.9 proof visibly includes d = 0, the positive-dimensional fibre A, [d] not etale, and the reduction to d != 0; the insertion wraps cleanly. External chapter references still display ??. |
| 21 | C | Pass at contact scale | Proposition conditions and proof occupy the body area; section 10 begins clearly near the foot. |
| 22 | C | Pass at contact scale | Middle diagrams and section 11 heading are separated, with no gross collisions. |
| 23 | C | Pass at contact scale | Lemma/proof text and numbered condition blocks are contained and distinguishable. |
| 24 | C | Pass at contact scale | Section 12, its commutative diagram and following text are clearly separated. |
| 25 | C | Pass at contact scale | Example diagram and lemma displays below it fit the body width. |
| 26 | C | Pass at contact scale | Section 13 and two numbered groupoid-definition lists remain clearly structured. |
| 27 | C | Pass at contact scale | Two commutative diagrams are separated from one another and surrounding text; intervening white space is intentional. |
| 28 | C + H | Pass; correction visible | Lemma 14.2 visibly reads alpha composed with i*alpha = s*e*alpha and then i*alpha composed with alpha = t*e*alpha. Stars, order and right-hand sides are legible; the large definition diagram has no label/arrow collision. |
| 29 | C | Pass at contact scale | Upper square and paired diagrams below it remain within the visible page area. |
| 30 | C | Pass at contact scale | Long proof, conditions and central square remain separated at contact-sheet scale. |
| 31 | C | Pass at contact scale | Proof/remark text, functor conditions and square have no gross overlap. |
| 32 | C | Pass at contact scale | Lemma/proof blocks and two squares are visibly separated. |
| 33 | C + H | Pass; correction visible | Lemma 15.7 lower affine-cover display visibly reads t^{-1}(U_i) intersect s^{-1}(U_j) = union W_{ijk}; indices and order are legible and contained. Proof continuation is normal. |
| 34 | C + H | Pass; correction visible | Under the two sums, the two ambient modules M_{ijk} and M_j tensor_{A_j,s} B_{ijk}, respectively, are visible with their coefficient conditions. The added text fits; section 16 starts cleanly below. |
| 35 | C | Pass at contact scale | Lemma/proof blocks, section 17 heading and square are separated. |
| 36 | C | Pass at contact scale | Section 18 and the wide lower curved-arrow diagram remain inside the page; no gross clipping. |
| 37 | C | Pass at contact scale | Proof blocks and section 19 heading remain separated at contact-sheet scale. |
| 38 | C | Pass at contact scale | Dense lemmas/proofs and the section 20 heading remain inside the visible body area. |
| 39 | C | Pass at contact scale | Quotient-sheaf discussion and displayed maps are separated; no gross overlap. |
| 40 | C | Pass at contact scale | Lemma/proof blocks and the small lower diagram remain contained. |
| 41 | C | Pass at contact scale | Long proof and two stacked squares have distinct rows and margins. |
| 42 | C + E | Pass; inherited overwidth | Definition 21.1 paragraph, square and Lemma 21.2 displays are fully visible at 96 dpi. The inherited 1.05727 pt overfull paragraph does not visibly clip or collide with other content. |
| 43 | C | Pass at contact scale | Section 22 heading, equation row and enumerated conditions remain distinguishable. |
| 44 | C | Pass at contact scale | Section 23 heading, central square and subsequent lemmas are separated. |
| 45 | C | Pass at contact scale | Wide upper commutative diagram fits inside the page; proofs below it remain separated. |
| 46 | C + H | Pass; correction visible | Lemma 23.5 proof part (2)(a) visibly reads P_r in C'_r[x]; the prime is distinguishable from C^1_r nearby. Dense proof and lower displayed norm remain contained. |
| 47 | C | Pass at contact scale | Dense proof and lower-middle multi-arrow diagram remain separated and inside the page. |
| 48 | C | Pass at contact scale | Three adjacent squares and surrounding proof text remain contained at contact-sheet scale. |
| 49 | C | Pass at contact scale | Dense algebraic proof and displayed expressions show no gross overlap or truncation. |
| 50 | C | Pass at contact scale | Several morphism diagrams are separated; lower proposition starts clearly. |
| 51 | C | Pass at contact scale | Long proposition proof remains contained; reference annotations remain visible. |
| 52 | C | Pass at contact scale | Sections 24 and 25 are clearly separated and displayed equations have adequate spacing. |
| 53 | C | Pass at contact scale | Proof/enumeration blocks continue within the visible page area without gross cutoff. |
| 54 | C | Pass at contact scale | Short proof precedes a structured two-column Other chapters list; columns remain distinct. |
| 55 | C | Pass at contact scale | Other chapters continues into References; the lower white area is intentional end matter, not an unreviewed or missing PDF page. |

## Evidence identities

| Input | Bytes | SHA-256 |
| --- | ---: | --- |
| Render manifest | 12450 | `9BE35A3024943D3EBA380268C826D432BDD6FDE3F2403E18D05FBB459C979B60` |
| Source-page map | 2514 | `F65511EF52307C06EC04D0B05092BEB264A8881AF9373B709942E8B1D151FFEF` |
| Operation spec | 30858 | `14C03664126894B674CDB01ABA0CC71179657EB593F11CE786034C1CFB2D4BDB` |
| Build log | 68315 | `7529265D0927338652F5265E0F20D9AAB56D708AE4C5A70DF204DFC2408940AF` |

The companion JSON includes absolute input paths, the verbatim bounded assignment, all page-level bindings, all six operation bindings, preserved findings and the coverage lists. Candidate assembly remains with the parent task. No further visual blocker is recorded for this PDF identity.

