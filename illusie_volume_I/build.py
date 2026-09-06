"""Build the original and changed simplicial chapter under one TeX mutex."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.build_fixed_point import WindowsNamedMutex, run
from illusie_volume_I.verify import composition, sha

def file_id(path: Path) -> dict:
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha(data)}

def diagnostics(log: str) -> dict:
    return {
        "fatal": len(re.findall(r"^!|Fatal error|Emergency stop", log, re.M)),
        "missing_glyphs": log.count("Missing character:"),
        "undefined_citations": len(re.findall(r"Citation .+ undefined", log)),
        "rerun_requests": len(re.findall(r"Rerun to get|Rerun LaTeX|Please rerun", log)),
        "duplicate_destinations": len(re.findall(r"destination with the same identifier", log)),
        "overfull_boxes": len(re.findall(r"Overfull \\[hv]box", log)),
        "undefined_labels": sorted(set(re.findall(r"(?:Hyper )?[Rr]eference [`']([^']+)'[^\n]*undefined", log))),
    }

def main() -> None:
    source, _, preimage = composition(ROOT)
    output = ROOT / "illusie_volume_I/build_i1_2"
    output.mkdir(exist_ok=True)
    dependencies = ("preamble.tex", "stacks-project.cls", "my.bib", "chapters.tex")
    dep_ids = {name: file_id(ROOT / name) for name in dependencies}
    for lane, data in (("baseline", preimage), ("candidate", source)):
        folder = output / lane
        folder.mkdir(exist_ok=True)
        if (folder / "simplicial.pdf").exists():
            raise RuntimeError(f"{lane} output exists; do not restart a completed build")
        for name in dependencies:
            shutil.copyfile(ROOT / name, folder / name)
        (folder / "simplicial.tex").write_bytes(data)
    env = os.environ.copy()
    env.update(SOURCE_DATE_EPOCH="1788730435", FORCE_SOURCE_DATE="1", TZ="UTC")
    engine = shutil.which("pdflatex")
    bibtex = shutil.which("bibtex")
    if not engine or not bibtex:
        raise RuntimeError("pdflatex/bibtex executable missing")
    receipt = {"schema": "illusie-volume-I-targeted-build/v1", "status": "RUNNING",
               "dependencies": dep_ids, "lanes": {},
               "source_date_epoch": env["SOURCE_DATE_EPOCH"]}
    mutex = WindowsNamedMutex("Global\\InterlanguageTeXSlotV1", 45000)
    with mutex:
        for lane in ("baseline", "candidate"):
            folder = output / lane
            passes = []
            stable = False
            for number in range(1, 5):
                started = time.monotonic()
                transcript = run([engine, "--disable-installer", "-no-shell-escape",
                                  "-interaction=nonstopmode", "-halt-on-error",
                                  "-file-line-error", "simplicial.tex"], folder, env, mutex)
                (folder / f"pass-{number}.txt").write_text(transcript, encoding="utf-8")
                if number == 1:
                    bibliography = run([bibtex, "simplicial"], folder, env, mutex)
                    (folder / "bibliography.txt").write_text(bibliography, encoding="utf-8")
                row = {"pass": number, "seconds": round(time.monotonic()-started, 3),
                       "pdf": file_id(folder / "simplicial.pdf"),
                       "aux": file_id(folder / "simplicial.aux"),
                       "toc": file_id(folder / "simplicial.toc")}
                passes.append(row)
                print(f"{lane} pass {number} completed", flush=True)
                if len(passes) >= 2 and all(passes[-1][key] == passes[-2][key]
                                             for key in ("pdf", "aux", "toc")):
                    stable = True
                    break
            log = (folder / "simplicial.log").read_text(encoding="utf-8", errors="replace")
            diag = diagnostics(log)
            if not stable:
                raise RuntimeError(f"{lane} did not reach a fixed point within four passes")
            if any(diag[key] for key in ("fatal", "missing_glyphs", "undefined_citations",
                                        "rerun_requests", "duplicate_destinations")):
                raise RuntimeError(f"{lane} has strict diagnostics: {diag}")
            receipt["lanes"][lane] = {"passes": passes, "stable": stable,
                                       "diagnostics": diag,
                                       "pdf": file_id(folder / "simplicial.pdf"),
                                       "log": file_id(folder / "simplicial.log")}
        old = set(receipt["lanes"]["baseline"]["diagnostics"]["undefined_labels"])
        new = set(receipt["lanes"]["candidate"]["diagnostics"]["undefined_labels"])
        if new - old:
            raise RuntimeError(f"new unresolved references: {sorted(new-old)}")
    receipt["mutex"] = mutex.receipt_details()
    receipt["status"] = "PASS_TARGETED_WITH_UNCHANGED_EXTERNAL_AUX_LIMITATION"
    receipt["new_unresolved_references"] = sorted(new-old)
    receipt["note"] = "The sparse targeted build lacks other-chapter AUX files; baseline and candidate use the same inputs. The new section has no unresolved reference. This is not a full-book build."
    (ROOT / "illusie_volume_I/build-receipt-i1-2.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"],
                      "candidate_pdf": receipt["lanes"]["candidate"]["pdf"],
                      "unchanged_external_labels": len(new)}), flush=True)

if __name__ == "__main__":
    main()
