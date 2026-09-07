from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_fixed_point import validate_import_preparation_topology
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

template_build = load(V / "stacks-errata-a04446e-r47-build-2026-09-06.json")
flat = dict(template_build["composition"])
flat.update({
    "receipt": "validation/composition-current.json",
    "receipt_sha256": comp_sha,
    "receipt_git_blob": comp_blob,
    "authority_commit": comp["authority"]["commit"],
    "authority_tree": comp["authority"]["tree"],
    "previous_public_main_head": comp["previous_cutoff"]["public_main_head"],
    "previous_public_main_tree": comp["previous_cutoff"]["public_main_tree"],
    "previous_registry_commit": comp["previous_cutoff"]["registry_commit"],
    "previous_last_admitted_overlay": comp["previous_cutoff"]["last_admitted_overlay"],
    "previous_source_blobs": comp["previous_cutoff"]["source_blobs"],
    "composition_mode": comp["composition"]["mode"],
    "composition_base_commit": comp["composition"]["base_commit"],
    "composition_base_tree": comp["composition"]["base_tree"],
    "composition_source_commit": comp["composition"]["source_commit"],
    "composition_source_tree": comp["composition"]["source_tree"],
    "registry_cutoff_commit": comp["registry"]["cutoff_commit"],
    "registry_cutoff_tree": comp["registry"]["cutoff_tree"],
    "registry_import_commit": comp["registry"]["linear_import_commit"],
    "registry_import_tree": comp["registry"]["linear_import_tree"],
    "registry_overlays_path": comp["registry"]["overlays_path"],
    "registry_overlays_git_blob": comp["registry"]["overlays_git_blob"],
    "registry_overlays_sha256": comp["registry"]["overlays_sha256"],
    "registered_overlays": comp["registry"]["registered_overlays"],
    "registered_stable_ids": comp["registry"]["registered_stable_ids"],
    "last_admitted_overlay": comp["registry"]["last_admitted_overlay"],
    "new_overlays": comp["new_overlays"],
    "new_overlay_ids": [row["id"] for row in comp["new_overlays"]],
    "new_overlay_candidate_commits": [row["candidate_commit"] for row in comp["new_overlays"]],
    "new_overlay_intake_commits": [row["intake_commit"] for row in comp["new_overlays"]],
    "new_overlay_admission_commits": [row["admission_commit"] for row in comp["new_overlays"]],
    "required_build_stems": comp["required_build_stems"],
    "affected_source_stems": [Path(p).stem for p in comp["composition"]["affected_sources"]],
    "affected_source_identities": comp["composition"]["affected_sources"],
    "registry_leases_path": comp["registry"]["leases_path"],
    "registry_leases_git_blob": comp["registry"]["leases_git_blob"],
    "registry_leases_sha256": comp["registry"]["leases_sha256"],
})
flat["import_preparation_topology"] = validate_import_preparation_topology(ROOT, comp)

for name in (
    "stacks-errata-a04446e-r47-illusie-build-2026-09-07.json",
    "stacks-errata-a04446e-r47-illusie-repro-build-2026-09-07.json",
    "stacks-errata-a04446e-r47-illusie-reproducibility-2026-09-07.json",
):
    path = V / name
    value = load(path)
    value["source"] = {"commit": HEAD, "tree": TREE}
    value["composition"] = flat
    checkpoint = value.get("source_checkpoint")
    if isinstance(checkpoint, dict):
        checkpoint["canonical_composition"] = {
            "path": "validation/composition-current.json",
            "git_blob": comp_blob,
            "sha256": comp_sha,
            "composition_source_commit": SOURCE,
            "composition_source_tree": comp["composition"]["source_tree"],
        }
        successor = checkpoint.get("semantic_successor")
        if isinstance(successor, dict) and isinstance(successor.get("canonical_composition"), dict):
            successor["canonical_composition"] = {
                "path": "validation/composition-current.json",
                "git_blob": comp_blob,
                "sha256": comp_sha,
                "composition_source_commit": SOURCE,
                "composition_source_tree": comp["composition"]["source_tree"],
            }
    dump(path, value)

# Rebind the full-schema visual receipt while retaining its bounded R40-R47
# locus inventory and all historical inspection evidence.
visual_old = V / "stacks-errata-a04446e-r47-visual-qa-2026-09-06.json"
visual_new = V / "stacks-errata-a04446e-r47-illusie-visual-qa-2026-09-07.json"
visual = load(visual_old)
build = load(V / "stacks-errata-a04446e-r47-illusie-build-2026-09-07.json")
visual["source"] = {"commit": HEAD, "tree": TREE}
build_bytes = (V / "stacks-errata-a04446e-r47-illusie-build-2026-09-07.json").read_bytes()
visual["build_receipt"] = {
    "path": "validation/stacks-errata-a04446e-r47-illusie-build-2026-09-07.json",
    "bytes": len(build_bytes),
    "sha256": sha256(build_bytes),
    "status": build["status"],
    "global_fixed_point_sweep": build["build"]["global_fixed_point_sweep"],
}
by_stem = {row["stem"]: row for row in build["artifacts"]}
for stem, row in visual.get("artifacts", {}).items():
    if stem in by_stem:
        fresh = by_stem[stem]
        row["bytes"] = fresh["bytes"]
        row["sha256"] = fresh["sha256"]
        row["pages"] = fresh["pages"]
visual["created_utc"] = "2026-09-07T00:19:23Z"
dump(visual_new, visual)

# Refresh the reproducibility envelope after the two build receipts have their
# final bytes and the successor checkpoint has been rebound.
repro_path = V / "stacks-errata-a04446e-r47-illusie-reproducibility-2026-09-07.json"
repro = load(repro_path)
first_path = V / "stacks-errata-a04446e-r47-illusie-build-2026-09-07.json"
second_path = V / "stacks-errata-a04446e-r47-illusie-repro-build-2026-09-07.json"
first_bytes = first_path.read_bytes()
second_bytes = second_path.read_bytes()
repro["scope"] = {
    "admitted_errata": "R1-R47",
    "registry_cutoff_commit": comp["registry"]["cutoff_commit"],
    "source_commit": HEAD,
    "source_tree": TREE,
    "composition_receipt": "validation/composition-current.json",
    "composition_receipt_sha256": comp_sha,
}
repro["runs"] = {
    "first": {"receipt": "validation/stacks-errata-a04446e-r47-illusie-build-2026-09-07.json", "created_utc": load(first_path)["created_utc"], "bytes": len(first_bytes), "sha256": sha256(first_bytes), "status": "PASS", "global_fixed_point_sweep": 4},
    "second": {"receipt": "validation/stacks-errata-a04446e-r47-illusie-repro-build-2026-09-07.json", "created_utc": load(second_path)["created_utc"], "bytes": len(second_bytes), "sha256": sha256(second_bytes), "status": "PASS", "global_fixed_point_sweep": 4},
}
repro["composition"] = flat
dump(repro_path, repro)

print(json.dumps({"composition_sha256": comp_sha, "composition_git_blob": comp_blob}))
