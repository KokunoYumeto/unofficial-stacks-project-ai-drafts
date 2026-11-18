# Local work saved on 18 November 2026: `Documents_mathematics-commons-stacks`

Work that existed only in a local clone (`Documents\mathematics-commons-stacks`), found by the scan of 18 Nov 2026 and saved here as raw material. Not reviewed; nothing is merged.

- `uncommitted.patch` (19,468 bytes): uncommitted changes of the working tree and index (git diff HEAD).
- `untracked.tar.gz` (11,768 bytes): untracked files, respecting .gitignore (tar.gz).

## How to apply

- A patch: on the clone's branch, `git apply uncommitted.patch` (or `stash0.patch`).
- The bundle: `git bundle verify local.bundle`, then `git fetch local.bundle 'refs/heads/*:refs/remotes/rescued/*'`.
- Untracked files: `tar -xzf untracked.tar.gz` at the root of the working tree.
