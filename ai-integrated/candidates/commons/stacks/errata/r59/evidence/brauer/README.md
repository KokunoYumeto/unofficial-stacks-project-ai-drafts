# Brauer Groups: corrections and complete editorial proofs

This preparation contains the Stacks Project authors' original Brauer Groups
chapter and a source-bound review of twelve received reports in ten groups.
The ten earlier corrections are retained. Two further propagation findings
give nine bounded source edits: the exact nonzero hypothesis in the
simple-module lemma, and the multiplication order in specified endomorphism
and centralizer identifications. The correct opposite algebra in the
centralizer conclusion remains intact.

Read PROOFS.md for the complete maps, calculations and arguments.
CLAIM_PROPAGATION.json identifies affected statements and the two proved
editorial underclaims: Schur's argument without the finite-algebra restriction,
and the bicommutant conclusion for every nonzero module over the original
finite simple algebra. These supplements do not replace the source exposition.

The patches directory retains isolated, cumulative and combined-correction
patches, with exact previews. BATCH.json binds every file. ORIGINAL_BATCH.json
and PUBLIC_TRANSPORT.json preserve the prior identities and the single
relative-path adjustment to the optional checker. All twenty original
preparation files, including the entire proof, remain byte-identical.

With Python and SymPy installed, run `python replay_operator_order.py` from
this directory to check all sixteen ordered quaternion basis products,
the reversed right-operator products and the commuting left/right actions.
The forty-eight integer matrix identities illustrate the specified order;
the universal proof is in PROOFS.md and is not inferred from an example.

Original source: the Stacks Project authors, authority commit
`a04446e57ec1fbc252a871afcec7752fb2807b14`. COPYING preserves the source license.
Editorial review and supplementary arguments: OpenAI Codex, GPT-6 Astra,
Ultra effort. No independent human review, novelty or official endorsement
is claimed. This is prepared evidence; stable-ID allocation, admission,
source composition, rendered acceptance and publication remain unfinished.
The separately received open-problem research packet remains deferred.
