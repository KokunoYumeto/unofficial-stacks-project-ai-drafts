# Textual corrections: exact changes and review evidence

These entries are separate from new theorem additions. The chapter patches
and combined patch contain exactly this effective textual set.

Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections.

## spaces-limits

[Chapter patch](https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/chapters/spaces-limits.patch)

### MC-STK-ERR-1574

`spaces-limits.tex` — 178; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-limits.tex#L178) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r50/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r50/candidate.manifest.json)

The reverse implication fixes y_T in G(T), and the fibre functor is F_{y_T}. The y in the separate forward implication is not bound in this direction. Only the subscript at line 178 changes.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-F_y(T'_i)
+F_{y_T}(T'_i)
````

### MC-STK-ERR-1575

`spaces-limits.tex` — 269; source defect.

[Original passage](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-limits.tex#L269) · [Review evidence](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r50/replay/FINAL_INDEPENDENT_REVIEW.json) · [Manifest](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/main/ai-integrated/candidates/commons/stacks/errata/r50/candidate.manifest.json)

The displayed comparison is a fibre product over a varying set. In the frozen Categories lemma-directed-commutes, filtered colimits commute with finite limits, explicitly including fibre products and equalizers. At a common later index the equality of images of representatives is witnessed, giving surjectivity; eventual equality of pairs gives injectivity. Finite products alone is not the stated justification needed.

````diff
--- original
+++ replacement
@@ -1 +1 @@
-finite products
+finite limits
````
