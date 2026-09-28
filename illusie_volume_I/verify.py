"""Bounded checks for the Illusie I source map and chapter additions."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

BASE_SHA256 = "23E8DB6115B5B3465D2C1292D7E6CB244308204C6D1B7EE5F3AC071092D643F9"
AUTHORITY_SHA256 = "1855B49FE461B13B1CBAEE1341C8FC3E3E0CDDC034C54ABEC1165AF061B90A56"
START = b"% BEGIN ILLUSIE VOLUME I 1.1.6\n"
END = b"% END ILLUSIE VOLUME I 1.1.6\n\n"
HOMOTOPY_SHEAVES_START = b"% BEGIN ILLUSIE VOLUME I 2.1.2.1\n"
HOMOTOPY_SHEAVES_END = b"% END ILLUSIE VOLUME I 2.1.2.1\n\n"

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()

def identity(path: Path) -> dict:
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha(data)}

def source_section(text: str, page: int) -> str:
    # The current source span ends at the end of printed page 16.
    # Do not retain obsolete mid-page cuts from earlier section checkpoints.
    return text

def write_source_lock(root: Path, edition: Path, authority: Path) -> None:
    authority_id = identity(authority)
    assert authority_id["sha256"] == AUTHORITY_SHA256, "authority lock mismatch"
    files, anchors_by_lane = [], {}
    for lane in ("fr_diplomatic", "fr_corrected", "en"):
        anchors = []
        for page in range(1, 17):
            relative = f"tex/volume_I/{lane}/ch1/{page:03d}_p{page:03d}.tex"
            path = edition / relative
            text = source_section(path.read_text(encoding="utf-8"), page)
            page_anchors = re.findall(r"\\hypertarget\{([^}]+)\}", text)
            anchors.extend(page_anchors)
            files.append({"path": relative, "printed_page": page,
                          "physical_page": page + 18, **identity(path),
                          "section_anchors": page_anchors})
        anchors_by_lane[lane] = anchors
    assert anchors_by_lane["fr_diplomatic"] == anchors_by_lane["fr_corrected"]
    assert anchors_by_lane["fr_corrected"] == anchors_by_lane["en"]
    assert len(set(anchors_by_lane["en"])) == len(anchors_by_lane["en"])
    result = {"schema": "illusie-volume-I-source-lock/v1",
              "authority": {"doi": "10.1007/BFb0059052", **authority_id},
              "files": files, "section_anchors": anchors_by_lane["en"]}
    (root / "illusie_volume_I/source-lock.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

def composition(root: Path) -> tuple[bytes, bytes, bytes]:
    source = (root / "simplicial.tex").read_bytes()
    first_snippet = b"\n\n".join(
        (root / "illusie_volume_I" / name).read_bytes().rstrip()
        for name in ("relative-homotopy.tex", "localization.tex")) + b"\n"
    homotopy_sheaves_snippet = (
        root / "illusie_volume_I/homotopy-sheaves.tex").read_bytes()
    assert source.count(START) == source.count(END) == 1, "composition markers not unique"
    assert source.count(HOMOTOPY_SHEAVES_START) == 1
    assert source.count(HOMOTOPY_SHEAVES_END) == 1
    before, rest = source.split(START)
    inserted, after = rest.split(END)
    assert inserted == first_snippet, "first root insertion differs from reviewed snippets"
    without_first = before + after
    before, rest = without_first.split(HOMOTOPY_SHEAVES_START)
    inserted, after = rest.split(HOMOTOPY_SHEAVES_END)
    assert inserted == homotopy_sheaves_snippet, (
        "homotopy-sheaf root insertion differs from reviewed snippet")
    preimage = before + after
    assert sha(preimage) == BASE_SHA256, "changes outside the bounded insertion"
    snippet = first_snippet + b"\n" + homotopy_sheaves_snippet
    return source, snippet, preimage

def validate(root: Path) -> dict:
    dossier = root / "illusie_volume_I"
    source, snippet, preimage = composition(root)
    mapping = json.loads((dossier / "map.json").read_text(encoding="utf-8"))
    lock = json.loads((dossier / "source-lock.json").read_text(encoding="utf-8"))
    mapped = list(mapping["structural_anchors"])
    for row in mapping["decisions"]:
        prefix = row.get("anchor_prefix", mapping["anchor_prefix"])
        mapped.extend(prefix + suffix for suffix in row["anchors"])
    assert len(mapped) == len(set(mapped)), "duplicate source disposition"
    assert set(mapped) == set(lock["section_anchors"]), "source coverage gap or surplus"
    assert lock["authority"]["sha256"] == AUTHORITY_SHA256
    tags = dict(line.split(",", 1) for line in
                (root / "tags/tags").read_text(encoding="utf-8").splitlines()
                if line and not line.startswith("#") and "," in line)
    local_labels = re.findall(rb"\\label\{([^}]+)\}", snippet)
    assert len(local_labels) == len(set(local_labels)) == 17
    assert b"section-illusie-I-homotopy-sheaves" in local_labels
    assert b"lemma-illusie-I-homotopy-sheaves-colimits-pullback" in local_labels
    for row in mapping["decisions"]:
        assert len(row["tags"]) == len(row["labels"]), row["id"]
        for tag, label in zip(row["tags"], row["labels"]):
            assert tags.get(tag) == label, f"unverified tag mapping {tag}: {label}"
            parts = label.split("-")
            target = None
            raw_label = ""
            for cut in range(len(parts), 0, -1):
                candidate = root / ("-".join(parts[:cut]) + ".tex")
                if candidate.exists():
                    target = candidate.read_bytes()
                    raw_label = "-".join(parts[cut:])
                    break
            assert target is not None and raw_label, label
            assert target.count((r"\label{" + raw_label + "}").encode()) == 1, label
        for label in row.get("local_labels", []):
            assert label.encode() in local_labels, label
    effective = ["simplicial-" + label.decode() for label in local_labels]
    assert not set(effective) & set(tags.values()), "local label has permanent tag"
    for label in local_labels:
        assert source.count(b"\\label{" + label + b"}") == 1
    # References within the inserted text must resolve either in the live
    # chapter or to a permanent cross-chapter label in the tag table.
    tagged_labels = set(tags.values())
    for label in re.findall(rb"\\ref\{([^}]+)\}", snippet):
        if source.count(b"\\label{" + label + b"}") == 1:
            continue
        assert label.decode() in tagged_labels, label
    check = json.loads((dossier / "check.json").read_text(encoding="utf-8"))
    for key, data in (("source_postimage", source), ("snippet", snippet),
                      ("source_preimage", preimage)):
        assert check[key] == {"bytes": len(data), "sha256": sha(data)}, key
    pending = mapping["completion"]["pending_decisions"]
    assert all(item in {row["id"] for row in mapping["decisions"]} for item in pending)
    return {"status": "PASS", "scope": "inventory, labels, and composition only",
            "mathematical_dispositions_complete": not pending,
            "pending_decisions": pending, "source_anchors": len(mapped),
            "decisions": len(mapping["decisions"]), "local_labels": effective,
            "source_preimage": preimage,
            "current_source_sha256": sha(source)}

def write_check(root: Path) -> None:
    source, snippet, preimage = composition(root)
    check = {"schema": "illusie-volume-I-composition/v1",
             "base_commit": "f73b18165c7162b8386de06cc3c50bd4ced745b6",
             "source": "simplicial.tex", "official_tags_assigned": [],
             "fragments": ["relative-homotopy.tex", "localization.tex",
                           "homotopy-sheaves.tex"],
             "source_postimage": {"bytes": len(source), "sha256": sha(source)},
             "snippet": {"bytes": len(snippet), "sha256": sha(snippet)},
             "source_preimage": {"bytes": len(preimage), "sha256": sha(preimage)}}
    (root / "illusie_volume_I/check.json").write_text(
        json.dumps(check, indent=2) + "\n", encoding="utf-8", newline="\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition-root", type=Path)
    parser.add_argument("--authority", type=Path)
    parser.add_argument("--write-check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.edition_root:
        if not args.authority:
            parser.error("--authority is required with --edition-root")
        write_source_lock(root, args.edition_root, args.authority)
    if args.write_check:
        write_check(root)
    result = validate(root)
    result.pop("source_preimage")
    print(json.dumps(result, indent=2))
