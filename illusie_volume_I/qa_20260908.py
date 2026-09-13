"""Seal the bounded correction check after direct review of final pages 51-56."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from illusie_volume_I.verify import identity, sha, validate
from illusie_volume_I.record_carrier_correction import OLD

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT / "illusie_volume_I"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("edition_root", type=Path)
    args = parser.parse_args()
    result = validate(ROOT)
    result.pop("source_preimage")
    subprocess.run([sys.executable, "-X", "utf8", "-m", "unittest",
                    "illusie_volume_I.test_composition", "illusie_volume_I.test_ez"], cwd=ROOT, check=True)
    receipt_path = DOSSIER / "build-receipt-i1-4-20260908-final.json"
    build = json.loads(receipt_path.read_text(encoding="utf-8"))
    pdf = DOSSIER / "build_i1_4_20260908_final/candidate/simplicial.pdf"
    assert identity(pdf) == build["lanes"]["candidate"]["pdf"]
    assert not build["new_unresolved_references"]
    changes = json.loads((DOSSIER / "erratum-p005.json").read_text(encoding="utf-8"))["changes"]
    for row in changes:
        path = args.edition_root / row["path"]
        assert identity(path) == row["after"]
        raw = path.read_bytes()
        comment = b"% ILLUSIE-I-ERR-001: printed hg is corrected to hf (postcomposition over h after f)."
        before = raw.replace(comment + b"\n", b"").replace(comment + b"\r\n", b"")
        before = before.replace(b"$hf$-homotop", b"$hg$-homotop")
        assert sha(before) == row["before"]["sha256"], "unexpected witness edit"
    historical = {}
    for name in ("relative-homotopy.tex",):
        data = subprocess.check_output(["git", "show", f"e083b71a:illusie_volume_I/{name}"], cwd=ROOT)
        historical[name] = {"bytes": len(data), "sha256": sha(data)}
    data = subprocess.check_output(["git", "show", "e083b71a:simplicial.tex"], cwd=ROOT)
    historical["simplicial.tex"] = {"bytes": len(data), "sha256": sha(data)}
    result.update({"schema": "illusie-volume-I-correction-qa/v1", "date": "2026-09-08",
        "regression_tests": {"count": 5, "status": "PASS", "maximum_free_model_degree": 4},
        "build_receipt": {"path": receipt_path.name, **identity(receipt_path)},
        "pdf": {"path": str(pdf.relative_to(DOSSIER)).replace("\\", "/"), "pages": 81, **identity(pdf)},
        "visual_review": {"status": "PASS", "pages": list(range(51, 57)),
            "note": "Direct inspection of final Poppler PNGs: readable equations, margins, labels and page transitions; new overflow corrected.",
            "renders": [{"path": f"evidence/normalization-20260908/final-{p}.png", **identity(DOSSIER / f"evidence/normalization-20260908/final-{p}.png")} for p in range(51,57)]},
        "historical_identities": historical,
        "limitation": "67 unchanged external AUX references outside the addition; targeted chapter, not full book. Inventory PASS is not whole-volume completion.",
        "new_source_erratum": {"path": "erratum-p005.json", **identity(DOSSIER / "erratum-p005.json")}})
    (DOSSIER / "qa-20260908.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": result["status"], "historical_identities": historical, "pending": result["pending_decisions"]}))

if __name__ == "__main__":
    main()
