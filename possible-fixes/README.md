# Possible fixes: ready-to-inspect patches

These patches change only inherited official Stacks text. They contain no new
theorems from this project, no translation changes, and no repairs to AI additions.
They are proposals, not officially accepted errata. Applying cleanly is a byte check,
not a mathematical correctness certificate.

[Read the arguments and original/replacement passages](../PROPOSED_CORRECTIONS.md) ·
[Possible new additions (separate)](../POSSIBLE_ADDITIONS.md)

## Review or use one correction

All patches are based on official commit `a04446e57ec1fbc252a871afcec7752fb2807b14`.
Each individual patch and both bundles have been applied in a separate index
containing only the affected official files, with exact postimage verification.
There is no dependency on this fork. Check against your own checkout before applying:

```sh
git apply --check /path/to/chosen.patch
git apply /path/to/chosen.patch
```

The first command changes nothing; the second applies only the chosen diff.
Current upstream may have changed since the pinned commit: inspect conflicts or
already-fixed passages instead of forcing a patch. No current-upstream check is claimed.

The Ext arrow and composition corrections belong together mathematically. Use
[the three-proposal Ext bundle](EXT-CONTRAVARIANCE.patch) for that argument;
individual diffs remain available for inspection. Nearby individual patches may
share context, so do not assume arbitrary sequential application will work.

| Possible fix | Original location | Patch |
|---|---|---|
| Reverse the induced Ext arrows (`H100B-SOURCE-006`) | [algebra.tex:17587](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17587) | [diff](H100B-SOURCE-006.patch) |
| Use the cohomological index (`H100B-SOURCE-007`) | [algebra.tex:17594](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17594) | [diff](H100B-SOURCE-007.patch) |
| Reverse composition in the inverse-map argument (`H100B-SOURCE-009`) | [algebra.tex:17615](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17615) | [diff](H100B-SOURCE-009.patch) |
| Use both endpoint modules in the split sequence (`H100B-SOURCE-011`) | [algebra.tex:13073](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13073) | [diff](H100B-SOURCE-011.patch) |
| Write 'instead of' as two words (`H100B-SOURCE-013`) | [homology.tex:3962](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/homology.tex#L3962) | [diff](H100B-SOURCE-013.patch) |
| Use singular agreement for a diagram (`H100B-SOURCE-014`) | [algebra.tex:26495](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L26495) | [diff](H100B-SOURCE-014.patch) |
| Write 'have the property' (`H100B-SOURCE-015`) | [algebra.tex:27084](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27084) | [diff](H100B-SOURCE-015.patch) |
| Advance the injectivity index (`H100B-SOURCE-016`) | [algebra.tex:27704](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L27704) | [diff](H100B-SOURCE-016.patch) |
| Use the differential leaving the target degree (`H100B-SOURCE-017`) | [algebra.tex:17466](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17466) | [diff](H100B-SOURCE-017.patch) |
| Write 'instead' as one word (`H100B-SOURCE-018`) | [algebra.tex:17562](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17562) | [diff](H100B-SOURCE-018.patch) |
| Supply 'to' in 'Choose beta to be' (`H100B-SOURCE-019`) | [algebra.tex:17610](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17610) | [diff](H100B-SOURCE-019.patch) |
| Use the fibre point fixed in this implication (`SPACES-SRC-00178-UNBOUND-Y`) | [spaces-limits.tex:178](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-limits.tex#L178) | [diff](SPACES-SRC-00178-UNBOUND-Y.patch) |
| Use finite limits in the fibre-product comparison (`SPACES-SRC-00269-PRODUCTS-VS-LIMITS`) | [spaces-limits.tex:269](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-limits.tex#L269) | [diff](SPACES-SRC-00269-PRODUCTS-VS-LIMITS.patch) |

[All 13 proposals as one patch](ALL-13-PROPOSALS.patch) · [Hashes and replay evidence](manifest.json)

## Coverage

This exporter covers the 13-unit, 17-operation readable selection, not every
historical correction. The larger [integrated correction comparison](../CHANGES_FROM_UPSTREAM.md)
and [filterable chapter browser](../ai-integrated/changes/index.html) remain separate.
Their other corrections are not silently included in these downloads. Historical
duplicates and withdrawn suggestions receive no patch. Regenerate or verify with
`python tools/generate_possible_fix_patches.py` or the same command with `--check`.
