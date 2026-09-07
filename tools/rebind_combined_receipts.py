from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "validation"
COMP = V / "composition-current.json"
HEAD = "4d62d13fad147acc5f8ed70d80a63994d7c4bd7f"
TREE = "a62b9e8d340ff9a1844e65ec0080fdf11295cd9b"
BASE = "284c5acef853029f603f5326ecaa0d6d52bbf5fe"
SOURCE = "bb34cd90ea3da510cb21a01b14c7362f0a520872"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def blob_sha(data: bytes) -> str:
    h = hashlib.sha1()
    h.update(f"blob {len(data)}\0".encode())
    h.update(data)
    return h.hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> bytes:
    data = (json.dumps(value, indent=2) + "\n").encode("utf-8")
    path.write_bytes(data)
    return data


comp = load(COMP)
cmd = (
    "python tools/compose_overlay_projection.py --existing-rounds "
    + " ".join(str(i) for i in range(18, 40))
    + " --target-rounds "
    + " ".join(str(i) for i in range(18, 48))
    + f" --base-revision {BASE} --check-revision {SOURCE}"
)
comp["projection_verifier"]["command"] = cmd
comp_bytes = dump(COMP, comp)
comp_sha = sha256(comp_bytes)
comp_blob = blob_sha(comp_bytes)

for name in (
    "stacks-errata-a04446e-r47-illusie-build-2026-09-07.json",
    "stacks-errata-a04446e-r47-illusie-repro-build-2026-09-07.json",
    "stacks-errata-a04446e-r47-illusie-reproducibility-2026-09-07.json",
):
    path = V / name
    value = load(path)
    value["source"] = {"commit": HEAD, "tree": TREE}
    value["composition"] = dict(comp)
    value["composition"]["receipt_sha256"] = comp_sha
    value["composition"]["receipt_git_blob"] = comp_blob
    dump(path, value)

print(json.dumps({"composition_sha256": comp_sha, "composition_git_blob": comp_blob}))
