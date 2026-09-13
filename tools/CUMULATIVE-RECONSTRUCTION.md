# Cumulative reader and complete editable source

The cumulative reader is assembled from 36 separately compiled native LaTeX
chapters. This is the released chapter collection, not the complete Stacks
Project. Printed chapter pagination is retained. Chapter bookmarks and
namespaced destinations make links between included chapters work inside the
reader. References to unbuilt chapters remain external and inherited `??`
markers are not represented as repaired.

`tools/cumulative-master.json` is the executable cumulative assembly master.
It lists every chapter in reader order. Each listed `<stem>.tex` is itself a
complete native LaTeX document. `tools/cumulative_reader.py` combines their
compiled output without rewriting the mathematical page content. No isolated
patch or master with missing chapter bodies substitutes for those sources.

## What is preserved

- `current/`: exact native source at the final build-source Git commit, including
  all chapter bodies, shared classes/macros, bibliography, figures, build and
  reconstruction scripts. Additional preserved native chapters are not claimed
  as built in this 36-chapter reader.
- `baseline/`: unmodified native source at the pinned official upstream commit.
  It is separate from the corrected/current draft; neither overwrites the other.
- `SOURCE-INVENTORY.json`: exact archived member paths, original Git commit and
  blob IDs, byte counts and SHA-256 values. This manifest is also independently
  committed in the public repository. Its own bytes are the archive's sole
  non-member-table entry, avoiding a circular self-hash.

Applicable licenses and original contributor attribution remain in the source
trees. This package does not assert a new license over someone else's work.

## Reconstruct without Git

Install the same TeX toolchain and fonts recorded in the release build receipt:
pdfLaTeX, BibTeX, the AMS packages, Xy-pic with 2cell support, Latin Modern,
hyperref/xr-hyper, and the other standard TeX packages named in `preamble.tex`.
Install Python 3 and `pypdf==6.10.0`. `pdfinfo` is needed for the original full
release validator. Python dependencies and tools are external runtimes, not
editable mathematical source.

Extract the source ZIP into a new directory. From a Windows shell, run:

```text
python <extracted>/current/tools/reconstruct_cumulative.py --extracted-root <extracted> --output <new-empty-build-directory> --source-date-epoch <value-in-release-build-receipt>
```

The script validates the inventory schema, both source namespaces, the bound
assembly master, every chapter stem, and every listed source identity. It then
copies only listed `current/` files into an exclusively new, disjoint sibling
build directory, rechecking each file at copy time. Unlisted files are never
copied. Symlinks, Windows reparse points, unsafe Windows path aliases, and an
output nested inside either preserved source tree are rejected. Reference-label
collection reads only those verified archive members and never consults Git or
an unrelated parent checkout. It primes each chapter, runs BibTeX,
and repeats global sequential TeX passes to a bounded fixed point. It holds the
same machine-wide Windows TeX mutex throughout and preserves the source archive
and baseline unchanged. It then produces `01-cumulative-reader.pdf` and a
mechanical reconstruction receipt. It does not publish anything. A non-Windows
runner would need a separately reviewed process/mutex adaptation before use.

Reproduction on a different TeX distribution can change PDF bytes even where
mathematics and page layout agree. Exact binary reproducibility requires the
original tool versions, environment, source-date epoch and independent A/B
checks. This reconstruction helper does not replace the release's source,
formula, external-reference, visual, deterministic-build or public-readback
checks and does not claim those checks were performed by a recipient.

The native-source selector recursively follows literal `input` and `include`
dependencies regardless of the included file's extension. It also follows local
classes and packages, and preserves the bibliography and referenced figures.
Unsupported executable dependency syntax, such as a macro-valued input filename,
fails explicitly; the selector is not an arbitrary TeX macro interpreter.
Standard system packages remain part of the recorded external TeX toolchain.
Only links naming an included sibling chapter PDF are internalized by the
reader assembler. A target such as `other-edition/algebra.pdf` remains external
and is not redirected merely because its basename matches a current chapter.

## Release maintainer sequence

1. Commit this master and its helpers before choosing the final build source.
2. Produce the final fresh 36-chapter build and bind its exact source commit.
3. Call `cumulative_source.make_inventory(root, source_commit, authority_commit,
   chapter_stems)`, commit its canonical JSON at an explicit validation path,
   and preserve that same inventory blob through the public content head.
4. Run `tools/package_cumulative_successor.py` with the final build, source
   inventory commit/path, and public content commit. It consumes the existing
   direct-successor build gate; it neither builds TeX nor publishes.
5. Independently reopen both new assets. Recompute the ZIP inventory from Git,
   check every member, verify reader links and all page drawing streams, compare
   two independent reader assemblies, and render/inspect the new cumulative PDF.
6. Publish `01-cumulative-reader.pdf` first and
   `02-full-cumulative-editable-source.zip` immediately second. The chapter PDFs
   and evidence follow. Verify public order and anonymously download/hash/reopen
   the source ZIP; filenames alone are not proof of completeness.
