#!/usr/bin/env python3
"""Build the no-overwrite Tohoku sem/r10 Stacks mapping successor."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r9"
TARGET = ROOT / "tohoku_r10"
STAGE = ROOT / ".tohoku-r10-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r10"
QA = PROJECT / "qa" / "v68r24"
AUTHORITY = PROJECT / "authority_snapshot"

EXPECTED_GIT = {
    "branch": "codex/fac-tohoku-gaga",
    "head": "952bb0e39acfa050db054d7ae7ea91c51487b7a9",
    "tree": "5a07bc1e20e706f88e2d7a4856bba6a7d7bf29b9",
    "upstream": "952bb0e39acfa050db054d7ae7ea91c51487b7a9",
}

EXPECTED_SOURCE = {
    "cfg.json": (5024, "FC9AB6B47AF213020CA2D6B8CD4579A59167CAF5A1C6F3153A6FEE39CB286022"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "dec.csv": (309417, "E923CB42E2C8F9F764F4E3A913376BCE7DA668FC289DD6A44FB637764B4439D2"),
    "issues.csv": (15030, "33B8440A0B11DB9B9563C1C7B767AAE20C32DA88FD55169E56BA932CDB87A4E8"),
    "units.csv": (390661, "FF05EC39664B1973215335C6D0C485149879935ED32CE916F13E331ECA164ADE"),
    "map.csv": (449523, "3A8B46214FBBA36BD3AF22FEC783CEB11B5A654E71A44DE403F6F6608CD6EFA1"),
    "mcheck.json": (58987, "B8D0EFDC3F0536B58999E032B2FDE2F0858B22D0588BE7EDBD3F1AA919C14E30"),
}

EXPECTED_TOOLS = {
    "srcmap/intake.py": (9923, "CFD53B71649BEF84A166397AA18E39AC5E4EDF00DD860142B2936F886AB080B1"),
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
    "fga/mkidx.py": (14844, "4425B5D021B3E35371DEBB567881697F88DF6F533ACFC9783A749CE1A5176A6B"),
    "fga/mkmap.py": (22213, "7281F57EC7439E00431F2962DF9A6944779294955A9C4369615FFF04318B0053"),
    "tags/tags": (991506, "C5C7017FB5C50B60295B30801CA1B5BAB8F5B379F61B084D8219441938125FCF"),
}

EXPECTED_SEM = {
    "nodes.csv": (582572, "0F656565E4F4732E7DF1CE1ABA910A6A68BE4CC6896B325ED562E8CD573CF7A8"),
    "edges.csv": (260771, "5DCC1F11489A88AC02351103A6B5987877F55424CFFB066EAB9404EA5FA38BB1"),
    "terms.csv": (325273, "5E416E9CDC6983745E6D907110F4E91B5DD9EE273FF613FD70A0CC34CE8C4B12"),
    "stacks.csv": (11777, "E13EFA405B525D69BFF38256601E4AF64D22FA3075F3A95AB3DFB78C15CFD060"),
    "manifest.json": (6402, "F314863C1F6586FBEBC91ADBF7256C3C3B3B32307F72C5726DD5DB916C758D52"),
    "validation.json": (3744, "CBD612B566B2517A854A841154391E62C01EE0AE02834AB5BE7C48926673C9D2"),
}

EXPECTED_QA = {
    "sem-input.json": (299780, "42437BDDF7BE9AAB14869FD4B1F741191C8BCC9EDE1FFCDA3EB04964F8F1FB26"),
    "sem-check.json": (6395, "A425DDAA035F9E00D01579039F0E3786BCB0B52B079D614A7421D8828D837ADB"),
}

EXPECTED_AUTHORITY = {
    "part_i": (7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "part_ii": (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
}

DECISION_ROW = {
    "decision_id": "D000920",
    "unit_id": "tohoku:comparison:cech-h2-injection",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-equivariant-cech-comparison-low-degree",
    "rationale": (
        "The authority-correct bidegree E_2^{0,n} has now been carried through "
        "the source, reader, semantic, and mapping successors. Stacks proves the "
        "same unrestricted degree-two injection from the vanishing of E_2^{0,1}."
    ),
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000919",
}

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical JSON text: {path}")
    value = json.loads(data.decode("utf-8"), object_pairs_hook=_no_duplicate_pairs)
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def _no_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"Duplicate JSON key: {key}")
        output[key] = value
    return output


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    data = path.read_bytes()
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical CSV text: {path}")
    text = data.decode("utf-8-sig")
    reader = csv.DictReader(text.splitlines())
    rows = list(reader)
    if reader.fieldnames is None or any(None in row or None in row.values() for row in rows):
        raise RuntimeError(f"Malformed CSV: {path}")
    return list(reader.fieldnames), rows


def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    import io

    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    if path.read_bytes() != data:
        raise RuntimeError(f"Write readback mismatch: {path}")


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    if identity(path) != expected:
        raise RuntimeError(f"Input identity drift: {path}")


def git_value(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def verify_inputs() -> dict[str, object]:
    for name, expected in EXPECTED_SOURCE.items():
        require_identity(SOURCE / name, expected)
    for name, expected in EXPECTED_TOOLS.items():
        require_identity(ROOT / name, expected)
    for name, expected in EXPECTED_SEM.items():
        require_identity(SEM / name, expected)
    for name, expected in EXPECTED_QA.items():
        require_identity(QA / name, expected)
    authority_paths = {
        "part_i": AUTHORITY / "jstage_part_I_9_2_119.pdf",
        "part_ii": AUTHORITY / "jstage_part_II_9_3_185.pdf",
    }
    for key, expected in EXPECTED_AUTHORITY.items():
        require_identity(authority_paths[key], expected)
    sem_check = strict_json(QA / "sem-check.json")
    sem_validation = strict_json(SEM / "validation.json")
    if sem_check.get("status") != "PASS" or sem_check.get("errors") != []:
        raise RuntimeError("sem/r10 check is not PASS")
    if sem_validation.get("status") != "PASS" or sem_validation.get("errors") != []:
        raise RuntimeError("sem/r10 validation is not PASS")
    surface = sem_check.get("semantic_surface")
    if not isinstance(surface, dict) or (
        surface.get("file_count"), surface.get("bytes"), surface.get("aggregate_sha256")
    ) != (18, 2020949, "80A41130E5797219568E87AC0E15F7AF5F996EFE2895A159FC807C0356DCC33D"):
        raise RuntimeError("sem/r10 surface receipt drift")
    git = {
        "branch": git_value("branch", "--show-current"),
        "head": git_value("rev-parse", "HEAD"),
        "tree": git_value("rev-parse", "HEAD^{tree}"),
        "upstream": git_value("rev-parse", "@{upstream}"),
    }
    if git != EXPECTED_GIT:
        raise RuntimeError(f"Git baseline drift: {git}")
    status = subprocess.check_output(["git", "status", "--porcelain=v1", "-z"], cwd=ROOT)
    git["status_porcelain_v1_z_bytes"] = len(status)
    git["status_porcelain_v1_z_sha256"] = digest(status)
    git["worktree_clean"] = not bool(status)
    git["scanned_live_worktree"] = True
    git["scanned_tex_and_tags_match_head"] = False
    git["remote_server_freshness_verified"] = False
    return git


def make_config() -> dict:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r10"
    cfg["inputs"]["part_i"] = {
        **record(AUTHORITY / "jstage_part_I_9_2_119.pdf", "J-STAGE Part I"),
        "filename": "jstage_part_I_9_2_119.pdf",
    }
    cfg["inputs"]["part_ii"] = {
        **record(AUTHORITY / "jstage_part_II_9_3_185.pdf", "J-STAGE Part II"),
        "filename": "jstage_part_II_9_3_185.pdf",
    }
    cfg["inputs"]["primary"] = {
        **record(SEM / "nodes.csv", "nodes.csv"),
        "filename": "nodes.csv",
        "source_file": "sem/r10/nodes.csv",
    }
    for key, filename in (("edges", "edges.csv"), ("terms", "terms.csv"), ("stacks", "stacks.csv")):
        cfg["inputs"][key] = {**record(SEM / filename, filename), "filename": filename}
    cfg["inputs"]["sem_manifest"] = {
        **record(SEM / "manifest.json", "sem/r10 manifest"), "filename": "manifest.json"
    }
    cfg["inputs"]["sem_validation"] = {
        **record(SEM / "validation.json", "sem/r10 validation"), "filename": "validation.json"
    }
    cfg["inputs"]["sem_input"] = {
        **record(QA / "sem-input.json", "v68r24 sem input"), "filename": "sem-input.json"
    }
    cfg["inputs"]["sem_check"] = {
        **record(QA / "sem-check.json", "v68r24 sem check"), "filename": "sem-check.json"
    }
    cfg["semantic_successor"] = {
        "generation": "sem/r10",
        "surface_files": 18,
        "surface_bytes": 2020949,
        "surface_sha256": "80A41130E5797219568E87AC0E15F7AF5F996EFE2895A159FC807C0356DCC33D",
        "receipt": record(QA / "sem-check.json", "qa/v68r24/sem-check.json"),
    }
    cfg["stacks_baseline"] = {
        **EXPECTED_GIT,
        "remote_server_freshness_verified": False,
        "scan_basis": "exact_live_worktree_receipted_by_check_json_tex_sha256",
    }
    return cfg


def make_decisions() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    if [row["decision_id"] for row in rows] != [f"D{n:06d}" for n in range(1, 920)]:
        raise RuntimeError("r9 decision prefix drift")
    if rows[-1]["decision_id"] != "D000919" or rows[-1]["unit_id"] != DECISION_ROW["unit_id"]:
        raise RuntimeError("Unexpected r9 decision tail")
    # Preserve the sealed r9 ledger byte-for-byte as the exact append-only prefix.
    row_bytes = csv_bytes(fields, [DECISION_ROW])
    header_end = row_bytes.index(b"\n") + 1
    return (SOURCE / "dec.csv").read_bytes() + row_bytes[header_end:]


def make_issues() -> bytes:
    fields, rows = load_csv(SOURCE / "issues.csv")
    matches = [row for row in rows if row["issue_id"] == "I000019"]
    if len(matches) != 1:
        raise RuntimeError("I000019 is not unique")
    row = matches[0]
    if row["status"] != "confirmed" or row["resolution_decision"]:
        raise RuntimeError("Unexpected I000019 predecessor state")
    before = (SOURCE / "issues.csv").read_bytes()
    lines = before.splitlines(keepends=True)
    indexes = [index for index, line in enumerate(lines) if line.startswith(b"I000019,")]
    if len(indexes) != 1:
        raise RuntimeError("I000019 byte row is not unique")
    index = indexes[0]
    line = lines[index]
    marker = b",confirmed,authority_transcription_bidegree_error,"
    if line.count(marker) != 1 or not line.endswith(b",\n"):
        raise RuntimeError("Unexpected I000019 byte form")
    lines[index] = line.replace(
        marker, b",resolved,authority_transcription_bidegree_error,", 1
    )[:-2] + b",D000920\n"
    after = b"".join(lines)
    _, check_rows = load_csv_bytes(after)
    check = next(item for item in check_rows if item["issue_id"] == "I000019")
    if check["status"] != "resolved" or check["resolution_decision"] != "D000920":
        raise RuntimeError("I000019 byte patch failed")
    return after


def load_csv_bytes(data: bytes) -> tuple[list[str], list[dict[str, str]]]:
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError("Noncanonical in-memory CSV")
    text = data.decode("utf-8-sig")
    reader = csv.DictReader(text.splitlines())
    rows = list(reader)
    if reader.fieldnames is None or any(None in row or None in row.values() for row in rows):
        raise RuntimeError("Malformed in-memory CSV")
    return list(reader.fieldnames), rows


def run_tool(name: str, *args: str) -> None:
    relative = f"srcmap/{name}"
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])
    subprocess.run([sys.executable, "-I", "-B", str(ROOT / relative), *args], cwd=ROOT, check=True)
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])


def intake_args() -> list[str]:
    specs = [
        ("part_i", AUTHORITY / "jstage_part_I_9_2_119.pdf"),
        ("part_ii", AUTHORITY / "jstage_part_II_9_3_185.pdf"),
        ("edges", SEM / "edges.csv"), ("terms", SEM / "terms.csv"),
        ("stacks", SEM / "stacks.csv"), ("sem_manifest", SEM / "manifest.json"),
        ("sem_validation", SEM / "validation.json"),
        ("sem_input", QA / "sem-input.json"), ("sem_check", QA / "sem-check.json"),
    ]
    result: list[str] = []
    for key, path in specs:
        result += ["--extra", f"{key}={path}"]
    return result


def verify_deltas(root: Path) -> dict[str, object]:
    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, receipt in (("intake", intake), ("scan", check), ("map", mcheck)):
        if receipt.get("status") != "PASS" or receipt.get("errors") != []:
            raise RuntimeError(f"{name} receipt is not PASS")
    if mcheck.get("outputs_promoted") is not True:
        raise RuntimeError("Mapping outputs were not promoted")
    for filename in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv", "ucand.csv"):
        if (root / filename).read_bytes() != (SOURCE / filename).read_bytes():
            raise RuntimeError(f"Unchanged scan/candidate surface drift: {filename}")
    if check["sha256"].get("tags/tags") != digest((ROOT / "tags" / "tags").read_bytes()):
        raise RuntimeError("Tags changed after the Stacks scan")
    for filename, expected_hash in check.get("tex_sha256", {}).items():
        tex_path = ROOT / filename
        if not tex_path.is_file() or digest(tex_path.read_bytes()) != expected_hash:
            raise RuntimeError(f"TeX input changed after the Stacks scan: {filename}")

    _, old_units = load_csv(SOURCE / "units.csv")
    _, new_units = load_csv(root / "units.csv")
    if [row["id"] for row in new_units] != [row["id"] for row in old_units]:
        raise RuntimeError("Unit ID/order drift")
    title_changes: list[dict[str, str]] = []
    for old, new in zip(old_units, new_units, strict=True):
        changed = {field for field in old if old[field] != new[field]}
        allowed = {"title_en", "source_file"}
        if not changed <= allowed:
            raise RuntimeError(f"Unexpected unit delta {new['id']}: {sorted(changed)}")
        if old["source_file"] != "sem/r9/nodes.csv" or new["source_file"] != "sem/r10/nodes.csv":
            raise RuntimeError(f"Unexpected source transition: {new['id']}")
        if old["title_en"] != new["title_en"]:
            title_changes.append({"id": new["id"], "old": old["title_en"], "new": new["title_en"]})
    if [item["id"] for item in title_changes] != ["tohoku:comparison:cech-h2-injection"]:
        raise RuntimeError(f"Unexpected title changes: {title_changes}")

    _, decisions = load_csv(root / "dec.csv")
    if not (root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()):
        raise RuntimeError("r9 decision ledger is not an exact byte prefix")
    if [row["decision_id"] for row in decisions] != [f"D{n:06d}" for n in range(1, 921)]:
        raise RuntimeError("Decision ledger is not D000001..D000920")
    if decisions[-1] != DECISION_ROW:
        raise RuntimeError("D000920 differs from the frozen successor")

    _, issues = load_csv(root / "issues.csv")
    issue = next(row for row in issues if row["issue_id"] == "I000019")
    if issue["status"] != "resolved" or issue["resolution_decision"] != "D000920":
        raise RuntimeError("I000019 is not resolved by D000920")
    if sum(row["status"] != "resolved" for row in issues) != 0:
        raise RuntimeError("Unexpected active source issue remains")
    _, old_issues = load_csv(SOURCE / "issues.csv")
    for old, new in zip(old_issues, issues, strict=True):
        changed = {field for field in old if old[field] != new[field]}
        allowed = {"status", "resolution_decision"} if old["issue_id"] == "I000019" else set()
        if changed != allowed:
            raise RuntimeError(f"Unexpected issue delta {old['issue_id']}: {sorted(changed)}")

    _, old_map = load_csv(SOURCE / "map.csv")
    _, new_map = load_csv(root / "map.csv")
    if [row["unit_id"] for row in new_map] != [row["unit_id"] for row in old_map]:
        raise RuntimeError("Map unit ID/order drift")
    map_changes: list[str] = []
    for old, new in zip(old_map, new_map, strict=True):
        changed = {field for field in old if old[field] != new[field]}
        allowed = {"source_loc"}
        if new["unit_id"] == DECISION_ROW["unit_id"]:
            allowed |= {"decision_id", "rationale"}
        if not changed <= allowed:
            raise RuntimeError(f"Unexpected map delta {new['unit_id']}: {sorted(changed)}")
        if old["source_loc"].startswith("sem/r9/nodes.csv:") and new["source_loc"] == old["source_loc"].replace("sem/r9/", "sem/r10/", 1):
            pass
        else:
            raise RuntimeError(f"Unexpected map source transition: {new['unit_id']}")
        if changed - {"source_loc"}:
            map_changes.append(new["unit_id"])
    if map_changes != [DECISION_ROW["unit_id"]]:
        raise RuntimeError(f"Unexpected substantive map changes: {map_changes}")

    counts = mcheck.get("counts", {})
    expected_counts = {
        "units": 990, "decisions": 920, "decided_units": 678,
        "source_issues": 19, "active_source_issues": 0,
        "review_units": 0, "candidate_units": 0, "unit_candidates": 0,
    }
    if any(counts.get(key) != value for key, value in expected_counts.items()):
        raise RuntimeError(f"Mapping counts drift: {counts}")
    old_counts = strict_json(SOURCE / "mcheck.json")["counts"]
    if counts.get("dispositions") != old_counts.get("dispositions"):
        raise RuntimeError("Disposition histogram drift")
    return {
        "title_changes": title_changes,
        "substantive_map_changes": map_changes,
        "counts": counts,
        "scan": {
            "tex_files": check["counts"]["tex_files"],
            "labels": check["counts"]["labels"],
            "tex_sha256": check["tex_sha256"],
            "tags_sha256": check["sha256"]["tags/tags"],
        },
    }


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def receipt_payload(root: Path, git: dict[str, object], deltas: dict[str, object]) -> dict[str, object]:
    attestation = globals().get("EXECUTION_ATTESTATION", {})
    return {
        "schema": "tohoku-stacks-sem-r10-dossier-v1",
        "status": "PASS",
        "errors": [],
        "semantic_source": {
            "generation": "sem/r10",
            "surface_files": 18,
            "surface_bytes": 2020949,
            "surface_sha256": "80A41130E5797219568E87AC0E15F7AF5F996EFE2895A159FC807C0356DCC33D",
            "sem_input": record(QA / "sem-input.json", "qa/v68r24/sem-input.json"),
            "sem_check": record(QA / "sem-check.json", "qa/v68r24/sem-check.json"),
        },
        "predecessor_dossier": {
            "name": "tohoku_r9",
            "locked_files": [record(SOURCE / name) for name in sorted(EXPECTED_SOURCE)],
        },
        "execution": {
            "attestation": attestation,
            "dependencies": {name: record(ROOT / name) for name in sorted(EXPECTED_TOOLS)},
            "contract": "bootstrap_reads_hashes_and_executes_the_same_builder_bytes; dependencies_hash_checked_before_and_after",
        },
        "git": git,
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git commit or push is made by this receipt.",
            "No remote-server freshness check is performed.",
            "The Stacks scan binds the exact live dirty worktree through check.json, not the frozen HEAD tree.",
            "No release, publication, upload, DOI, Zenodo, rights, or whole-paper gate is closed.",
            "132 previously recorded Tohoku gap-class dispositions remain after this provenance-only successor.",
        ],
    }


def verify_existing(git: dict[str, object]) -> dict[str, object]:
    names = {path.name for path in TARGET.iterdir() if path.is_file()}
    if names != PAYLOAD | {"r10-check.json"} or any(path.is_dir() for path in TARGET.iterdir()):
        raise RuntimeError("Existing r10 dossier surface drift")
    deltas = verify_deltas(TARGET)
    receipt = strict_json(TARGET / "r10-check.json")
    expected = receipt_payload(TARGET, receipt["git"], deltas)
    # Git status can grow after generation; the receipt intentionally binds its creation snapshot.
    if receipt != expected:
        raise RuntimeError("Existing r10 receipt replay mismatch")
    return receipt


def main() -> int:
    git = verify_inputs()
    if TARGET.exists():
        receipt = verify_existing(git)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        return 0
    if STAGE.exists():
        raise FileExistsError(f"Unresolved transaction exists: {STAGE}")
    STAGE.mkdir()
    exclusive_write(STAGE / "cfg.json", json_bytes(make_config()))
    exclusive_write(STAGE / "topics.csv", (SOURCE / "topics.csv").read_bytes())
    exclusive_write(STAGE / "dec.csv", make_decisions())
    exclusive_write(STAGE / "issues.csv", make_issues())
    run_tool("intake.py", str(STAGE), str(SEM / "nodes.csv"), *intake_args())
    run_tool("scan.py", str(STAGE))
    run_tool("map.py", str(STAGE))
    deltas = verify_deltas(STAGE)
    status = (
        "# Tohoku sem/r10 mapping status\n\n"
        "- Semantic source: validated local-unpublished `sem/r10`.\n"
        "- Stable source inventory: 990 units, with the sole title correction on the p.213 H2 comparison unit.\n"
        "- Append-only mapping: `D000920` supersedes `D000919`; all earlier decisions remain unchanged.\n"
        "- Source issue `I000019` is resolved by the source/reader/semantic/mapping successor chain.\n"
        "- The Stacks scan binds the exact live integrated worktree; it does not claim that this dirty tree equals HEAD.\n"
        "- This local checkpoint makes no release, publication, remote-freshness, DOI, rights, or completion claim.\n"
    ).encode("utf-8")
    exclusive_write(STAGE / "STATUS.md", status)
    receipt = receipt_payload(STAGE, git, deltas)
    exclusive_write(STAGE / "r10-check.json", json_bytes(receipt))
    if {path.name for path in STAGE.iterdir() if path.is_file()} != PAYLOAD | {"r10-check.json"}:
        raise RuntimeError("Staged dossier surface mismatch")
    os.rename(STAGE, TARGET)
    final = verify_existing(git)
    print(json.dumps(final, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
