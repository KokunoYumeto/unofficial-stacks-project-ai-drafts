"""Bind the single scan-proven p.5 carrier erratum to old and new witnesses."""
import argparse
import json
from pathlib import Path
from illusie_volume_I.verify import identity, sha, AUTHORITY_SHA256

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT / "illusie_volume_I"
OLD = {
    "fr_corrected": "878900C380B54FA30043E633AC26C4FE6F16C8A487F6BDFD1E234C975CD2DB94",
    "en": "2DB9AD582AAB2D796EF6442F085F3F7C03487FC04CB7B980CA4A0BD2A3DA168B",
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("edition_root", type=Path)
    args = parser.parse_args()
    destination = DOSSIER / "erratum-p005.json"
    if destination.exists():
        raise RuntimeError("Receipt exists; do not overwrite historical evidence")
    lock = json.loads((DOSSIER / "source-lock.json").read_text(encoding="utf-8"))
    rows = []
    for lane, expected in OLD.items():
        rel = f"tex/volume_I/{lane}/ch1/005_p005.tex"
        old = next(row for row in lock["files"] if row["path"] == rel)
        assert old["sha256"] == expected
        path = args.edition_root / rel
        text = path.read_text(encoding="utf-8")
        assert text.count("$hf$-homotop") == 1 and "$hg$-homotop" not in text
        raw = path.read_bytes()
        comment = b"% ILLUSIE-I-ERR-001: printed hg is corrected to hf (postcomposition over h after f)."
        assert raw.count(comment) == 1
        before = raw.replace(comment + b"\n", b"").replace(comment + b"\r\n", b"")
        before = before.replace(b"$hf$-homotop", b"$hg$-homotop")
        assert sha(before) == expected, "change exceeds the exact erratum and comment"
        rows.append({"path": rel, "before": {key: old[key] for key in ("bytes", "sha256")},
                     "after": identity(path), "old": "$hg$-homotop", "new": "$hf$-homotop"})
    diplomatic = "tex/volume_I/fr_diplomatic/ch1/005_p005.tex"
    old = next(row for row in lock["files"] if row["path"] == diplomatic)
    assert identity(args.edition_root / diplomatic) == {key: old[key] for key in ("bytes", "sha256")}
    result = {
        "schema": "illusie-volume-I-erratum/v1", "id": "ILLUSIE-I-ERR-001",
        "date": "2026-09-08", "classification": "printed mathematical carrier error, not transcription error",
        "authority_sha256": AUTHORITY_SHA256, "printed_page": 5, "physical_page": 23,
        "source_anchor": "illusie:I:ch1:s1:1:p14c1",
        "pixel_receipt": {"path": "evidence/normalization-20260908/source-023.png",
                          **identity(DOSSIER / "evidence/normalization-20260908/source-023.png")},
        "proof": "The homotopy u lies over f:S->T and w lies over h:T->T'. Thus p(wu)=hf:S->T'. The printed hg is not composable in the stated types because g:S'->S.",
        "adverse_evidence": "Primary pixels and both prior corrected-French/English witnesses read hg. These establish a printed error, not evidence for the typed composition.",
        "changes": rows, "diplomatic_retained": {"path": diplomatic, **identity(args.edition_root / diplomatic)},
        "review": {"confidence": "high: follows directly from functoriality and displayed domains", "human_review_required": False},
        "publication": "LaTeX corrected; previously released PDF bytes retained. Include this erratum in the next cumulative edition version."
    }
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"receipt": str(destination), **identity(destination)}))

if __name__ == "__main__":
    main()
