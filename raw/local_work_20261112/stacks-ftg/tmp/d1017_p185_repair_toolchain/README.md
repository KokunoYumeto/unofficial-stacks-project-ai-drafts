# D1017-R001 p185 source-repair toolchain

Prepared, hash-frozen, no-overwrite transaction for the p.185 scalar-ring
repair. No mutating step runs without the explicit execution token recorded in
`contract.json`.

The contracted steps are source admission, reader build, and QA
preparation/commit. Semantic r21 is intentionally absent from this revision of
the contract: it must be adapted only after the exact r20 build and v68r42 QA
identities exist, rather than guessing future artifact hashes. Run `run.py
--help` for the frozen surface.
