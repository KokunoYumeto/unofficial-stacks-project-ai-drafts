# Independent R48 actual-build audit — 2026-09-12

The existing build passes this independent artifact, log-regression, and mutex-evidence audit, with the evidence limits below. No TeX was rerun, and no candidate, receipt, mathematical source, registry, or Git state was changed. Root retains the separate visual and mathematical review work.

All four PDFs are byte-identical across the first private run, second private run, and public candidate builds directory. Sources match the configured authority/payload hashes. The audit verified 109 recorded artifact bindings and hashed 402 distinct files.

| PDF | Bytes | SHA-256 |
| --- | ---: | --- |
| groupoids candidate | 731715 | 8364B86EBD7B74CDF8400838C9C1111AD8CD57C217E29191FB76539AC1E7A1C4 |
| groupoids authority | 731479 | 5EE63331EE97854DCA8123B494C0150A6E06B0B25172BDDB6EBA9AF791EA8246 |
| spaces-perfect candidate | 883674 | 84477331BE747CF2BAD63C77CE247D2E66421075BE452F0798EB8ADF2452B4C7 |
| spaces-perfect authority | 884477 | 018CC10F1E299920F7782661D70984CC5986B8C945617247AB5E0F6D6A8D260B |

The exact paths, source hashes, recorder identities, raw-command-output hashes, and check results are in [ACTUAL_BUILD_AUDIT.json](<WORKSPACE>/03_projects/language_management/cjk/00_lane_control/canon_audit_20260906/manager_verification/stacks_intake/r48_preparation_20260910/actual_build_review_20260912/ACTUAL_BUILD_AUDIT.json). The final build-receipt SHA-256 is `93E3A559DB3A66A087E055814575E4B9580A250497D1F0A3211ADB5FB8ACF92E`.

The global mutex was acquired at 16:32:34.0270950 UTC after approximately 0.869 seconds, before the first captured worker started. The two build trees, deterministic comparison, and immediate log preflight ran sequentially and completed cleanup before release at 16:33:27.7803785 UTC: 53.753 seconds of continuous ownership. All four roles returned zero and recorded capture before resume, completed cleanup, no termination request, and empty stderr. Captured process counts were 20, 20, 2, and 2. The post-release binder then returned zero and its output hash matches the current final receipt. Actual installed wrapper, runner, validator, and C# hashes match the previously reviewed code.

All 32 private build-command outputs exist. The second execution records all 16 pdflatex/BibTeX exits as zero, with matching output byte counts and hashes; all 12 recorded pdflatex invocations include `-no-shell-escape`. Both runs' 24 pdflatex outputs contain successful PDF-completion records and no fatal/error/glyph markers. The first run's successful guarded root plus the inspected fail-fast runner supports success of its 16 commands; individual first-run exit records are not retained separately.

For every one of the eight FLS inventories, this audit independently reconstructed input/output ordering from raw FLS, recomputed the canonical input-closure hash, checked output confinement, and bound the retained PDF/log output hashes. Repeated input lists and closure hashes match. All 2,172 available input occurrences rehashed successfully against current retained source, package, and format files.

The final logs show no new fatal errors, missing glyphs, undefined citations, local undefined references, page-count changes, or box regressions versus authority. Groupoids remains 55 pages; spaces-perfect remains 75 pages. Box dimensions and their order match after normalizing only source line numbers: groupoids retains two overfull horizontal boxes and one underfull vertical box; spaces-perfect retains twelve overfull horizontal boxes and one overfull vertical box. The unchanged maxima are 25.04082 pt and 22.57962 pt horizontally, with a 1.70636 pt vertical overflow in spaces-perfect.

Standalone limitations remain visible. Groupoids has 264 distinct unresolved external targets occurring 290 times; spaces-perfect has 375 occurring 496 times. Missing external-AUX warning multisets also match authority (116 and 115). Neither chapter has an undefined citation. Spaces-perfect retains the authority's BibTeX warning about missing pages in `rydh_etale_devissage`. Groupoids retains the authority's label-rerun warning; this fixed three-pass recipe does not establish AUX convergence. The generated index reference is an external navigation target explicitly identified in pinned `chapters.tex:153`.

Evidence limits matter for interpreting this pass. The second run overwrote the first public execution JSON; the first private receipt retains its hash but not those original JSON bytes. Each groupoids FLS inventory has four generated inputs whose bytes were not retained after successful work-root deletion (`.aux/.out/.toc/.bbl`); each spaces-perfect inventory has those four plus `groupoids.aux`. Their recorded hashes agree across builds, but the 36 missing generated-input occurrences cannot be independently rehashed now. Final-pdflatex FLS is also not a separate, complete BibTeX dependency manifest. This is not a claim of a self-contained archived toolchain.

The existing validators alone do not cover everything checked here: they record box counts without failing on regressions, do not classify local versus external references or test the generic label-rerun warning, and compare advertised FLS closure hashes without independently recomputing them. This audit supplied those additional comparisons. Mutex chronology is supported by the actual receipt, reviewed capture-before-resume code and Job Object accounting; no per-engine OS trace or new fault-injection test exists.

The audit's initial short-prefix heuristic misclassified `groupoids-quotients-section-phantom` as local to groupoids. The recorded source chapter identity resolves it as external. That audit correction and its original false findings are preserved in the JSON.

The completed artifact checks support proceeding with root's existing visual/source/final workflow while retaining these precise limitations.
