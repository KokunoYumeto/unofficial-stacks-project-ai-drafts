# Independent source review: P07-ERR-0001 through P07-ERR-0006

Reviewed 2026-09-13. Five findings support the proposed seven small edits. P07-ERR-0003 is a real unresolved reference placeholder with no supported replacement in this batch. This review supplies evidence, not admission, implementation, a build result, or publication certification.

I read the complete pinned source sections covering the spectral sequences and Hodge filtration (derham.tex 453–606) and the relevant Künneth setup, lemma, and proof (621–732). Their current counterparts, 465–618 and 633–744, are line-for-line identical. I also consulted the exact local definitions and cited lemma statements recorded in `source_evidence.json`; the producer's judgments were claims to check, not authorities.

| Finding | Pinned / current line | Independent conclusion |
| --- | --- | --- |
| P07-ERR-0001 | 459 / 471 | Change `exist` to `exists`. The singular noun phrase is “a Cartan-Eilenberg resolution.” The cited existence lemma uses the same singular assertion; its bounded-below hypothesis is consistent with the de Rham complex starting in degree zero. |
| P07-ERR-0002 | 540–541 / 552–553 | Delete the article `a ` in “in terms of a certain sheaves.” Preserve “certain sheaves”: the source explicitly uses a plural noun and has just defined the indexed cohomology sheaves. This grammar finding does not verify a particular Cartier description or supply the missing citation. |
| P07-ERR-0003 | 542 / 554 | The literal `(insert future reference here)` is present. No replacement is justified by the evidence consulted. Leave this occurrence unchanged and outside the seven-operation batch. |
| P07-ERR-0004 | 592, 594, 596 / 604, 606, 608 | Delete exactly the second closing parenthesis in each upper-row cohomology term. Each term has one literal `(` and two literal `)`; the sigma subscript uses braces. The original producer explanation about an “inner sigma argument” opening a parenthesis is inaccurate. |
| P07-ERR-0005 | 729 / 741 | Delete `a ` in “is a locally bounded.” The displayed object is already a complex, so “locally bounded” is a complete predicative adjective phrase. No added noun or altered boundedness assertion is needed. |
| P07-ERR-0006 | 730 / 742 | Insert `follows ` before the existing `by`, yielding “the result follows by Lemma … and ….” The sentence lacks a finite verb. Preserve `by` and both references; changing it to `from` would be unnecessary. |

For P07-ERR-0004, set $K_r=\sigma_{\geq r}\Omega^\bullet_{X/S}$. Homology 3724–3752 defines this cochain truncation as a subcomplex; derham.tex 569–588 explicitly applies it here. The three terms are the hypercohomology groups $H^n(X,K_i)$, $H^m(X,K_j)$, and $H^{n+m}(X,K_{i+j})$, naturally modules over $H^0(S,\mathcal O_S)$. The upper arrow is the bilinear product from the displayed wedge map; the downward maps come from the inclusions $K_r\to\Omega^\bullet_{X/S}$. The deletions preserve every degree, truncation bound, variable, coefficient ring, direct-product symbol, arrow, and the resulting filtration inclusion at pinned line 605. These are punctuation repairs; no mathematical object is replaced.

For P07-ERR-0005 and 0006, the smooth-differentials lemma makes $\Omega^1$ finite locally free; the de Rham definition takes its exterior powers. They vanish above the local rank, which supports local boundedness. Quasi-compactness supplies a finite bound, matching the boundedness hypothesis in the cited Künneth lemma; the second complex starts in degree zero. These are source-grounded checks of the nearby application, not a new full proof audit of its dependencies.

The independently recomputed SHA-256 values are:

- Pinned derham.tex, 230539 bytes: `2DC4E936FCE0E3B2729F9D9B68D4FF5E6F188F1C25F6723D61B92FA682E90FC8`.
- Current derham.tex, 237942 bytes: `0AA0F22D9765CCBB167D3C63D47143ACD35B241972B6B71FC772D8F0B327CDF3`.

`INDEPENDENT_SOURCE_REVIEW.json` records the six decisions and seven proposed textual operations. `source_evidence.json` preserves exact consulted excerpts, line locations, full-file identities, and explicitly normalized excerpt hashes. Confidence is high because the defects and proposed repairs are directly visible and contextually unambiguous; this is an editorial assessment, not a calibrated probability. Byte replay and registry deduplication remain the parent's separate responsibility. No source, registry, canonical identifier, TeX, or public artifact was changed.
