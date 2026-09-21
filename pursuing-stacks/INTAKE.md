# Pursuing Stacks: received draft, not an integrated chapter

A separate English Stacks-style draft covers source sections 1–48 and 16bis
of Grothendieck's *Pursuing Stacks*. The rest of the 140-section work is not
claimed complete. Pausing its producer does not discard the completed work
or require that producer to resume before reusable mathematics can be adopted.

## What is actually available

- A 68-page interim reader and nine editable chapter files.
- 151 local definitions, lemmas, propositions, and examples, mapped to 286
  source-passage dispositions. These are not 151 established additions to Stacks.
- Material on globular data, nerves, localization, categories of elements,
  test categories, relative nerves, asphericity, and homotopy intervals.
- Source issues, conjectures, and unresolved hypotheses recorded separately.

Fresh receiving-side replay found no source-span hash mismatch, duplicate
local tag, missing tag mapping, or malformed ledger record. There are 437 tag
rows and 698 dependency rows. This verifies the bookkeeping, not all proofs.
The reader hash agrees with the producer's checkpoint-0010 receipt:
701,575 bytes, SHA-256
`127164A5BFA65CC6B2E5AB9967C756B44D87D3F252CDF142F1042750F007EECA`.
The producer reported 32 overfull boxes and inspected three representative
pages; no whole-reader visual approval is claimed here.

## First comparison findings

1. **Do not duplicate the nerve theorem.** Local `PSM-DEF-0009` and
   `PSM-PROP-0003` restate the nerve construction and its full faithfulness.
   These are already in this draft's [Simplicial Methods](../simplicial.tex),
   at `definition-nerve-category` and `lemma-characterize-nerves-categories`,
   from the earlier FGA work. Reuse those results and preserve the source map.
2. **Review the category-of-elements/test-category module next.** Its explicit
   equivalence between presheaves over a presheaf and presheaves on its category
   of elements is a useful candidate component. Novelty relative to the full
   official and extended trees has not yet been established.
3. **Correct the draft before import.** In `test_categories.tex`, the displayed
   target in `definition-relative-test-functor` spells `operatorname{PSh}`
   without the leading backslash. This is a defect in the received AI draft,
   not an erratum in official Stacks. Its README also still reports the older
   section-28 checkpoint and must not supply the current coverage count.
4. **Qualify the free-cocompletion uniqueness statement.** For
   `PSM-PROP-0004`, uniqueness of the extension's natural isomorphism must be
   relative to a specified identification on the Yoneda image. Merely saying
   that the restriction is isomorphic to the chosen functor does not remove
   its natural automorphisms. This is a receiving-side proof-edit finding,
   not an upstream Stacks correction or a claim that the universal property fails.

## Integration boundary

Keep the producer's frozen files intact. Work from a hash-bound candidate copy;
deduplicate against both official Stacks and this draft, normalize notation,
retain only justified statements and dependencies, then run source/reference,
build, and visual checks before cumulative-source admission. Do not turn local
`PSM-` identifiers into official Stacks tags. No source admission, full mathematical
review, or GitHub publication of the 68-page reader is claimed by this intake note.

This material belongs to [Possible new additions](../POSSIBLE_ADDITIONS.md).
Neither it nor repairs to it belongs in the list of possible upstream fixes.
