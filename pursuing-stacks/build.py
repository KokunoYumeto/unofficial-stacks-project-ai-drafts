"""Build the standalone category-models module, with bounded Windows TeX capture.

Requires Python 3 and a TeX distribution providing pdflatex and the standard
amsart, lmodern, xy, and hyperref packages. No network access is needed.
"""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

MODULE = Path(__file__).resolve().parent
EPOCH = "1790010000"


def sha(data):
    return hashlib.sha256(data).hexdigest().upper()


class TexSlot:
    def __init__(self, timeout_ms):
        if not 1 <= timeout_ms <= 600000:
            raise ValueError("slot wait must be between 1 and 600000 ms")
        self.timeout_ms = timeout_ms

    def __enter__(self):
        self.receipt = {"name": r"Global\InterlanguageTeXSlotV1", "platform": sys.platform}
        self.owned = False
        if os.name == "nt":
            from ctypes import wintypes
            self.kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            self.kernel.CreateMutexW.argtypes = (ctypes.c_void_p, wintypes.BOOL, wintypes.LPCWSTR)
            self.kernel.CreateMutexW.restype = wintypes.HANDLE
            self.kernel.WaitForSingleObject.argtypes = (wintypes.HANDLE, wintypes.DWORD)
            self.kernel.WaitForSingleObject.restype = wintypes.DWORD
            self.kernel.ReleaseMutex.argtypes = (wintypes.HANDLE,)
            self.kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
            self.handle = self.kernel.CreateMutexW(None, False, self.receipt["name"])
            if not self.handle:
                raise OSError(ctypes.get_last_error(), "CreateMutexW")
            result = self.kernel.WaitForSingleObject(self.handle, self.timeout_ms)
            if result not in (0, 0x80):
                self.kernel.CloseHandle(self.handle)
                raise RuntimeError(f"TeX slot not acquired: {result:#x}; no engine launched")
            self.owned = True
            self.receipt.update(acquisition_timeout_ms=self.timeout_ms, abandoned_mutex_recovered=result == 0x80,
                                acquired_utc=datetime.now(timezone.utc).isoformat())
        else:
            self.receipt["note"] = "Windows named mutex is not applicable on this platform."
        return self

    def __exit__(self, *_):
        if self.owned:
            try:
                if not self.kernel.ReleaseMutex(self.handle):
                    raise OSError(ctypes.get_last_error(), "ReleaseMutex")
            finally:
                self.kernel.CloseHandle(self.handle)
                self.owned = False
                self.receipt["released_utc"] = datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default="02-category-models.tex",
                        choices=("02-category-models.tex", "05-homotopy-intervals.tex"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--resume-empty", action="store_true",
                        help="Reuse only an empty directory left by an unavailable TeX slot")
    parser.add_argument("--slot-wait-ms", type=int, default=15000)
    args = parser.parse_args()
    name = Path(args.source).stem
    out = args.output.resolve()
    if out.exists() and not (args.resume_empty and out.is_dir() and not any(out.iterdir())):
        raise RuntimeError("Choose a fresh output directory; existing builds are preserved.")
    latex = shutil.which("pdflatex")
    if not latex:
        raise RuntimeError("pdflatex is not available")
    source = (MODULE / args.source).read_bytes()
    assert source.count(b"\\begin{document}") == source.count(b"\\end{document}") == 1
    out.mkdir(parents=True, exist_ok=args.resume_empty)
    env = dict(os.environ, SOURCE_DATE_EPOCH=EPOCH, FORCE_SOURCE_DATE="1", TZ="UTC")
    captures, builds = [], []
    if os.name == "nt":
        sys.path.insert(0, str(MODULE.parent / "tools"))
        from tex_process_guard import run_captured
    with TexSlot(args.slot_wait_ms) as slot:
        (out / "mutex-acquisition.json").write_text(json.dumps(slot.receipt, indent=2) + "\n")
        for run in ("a", "b"):
            folder = out / run
            folder.mkdir()
            (folder / (name + ".tex")).write_bytes(source)
            previous = None
            for sweep in range(1, 6):
                command = [latex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
                           "-recorder", name + ".tex"]
                capture = out / f"capture-{run}-{sweep}.json"
                if os.name == "nt":
                    done = run_captured(command, cwd=folder, env=env, timeout=180,
                                        caller_holds_tex_mutex=slot.owned, receipt_path=capture)
                    output = done.stdout
                    captures.append({"file": capture.name, "sha256": sha(capture.read_bytes())})
                else:
                    done = subprocess.run(command, cwd=folder, env=env, timeout=180,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    output = done.stdout
                (out / f"output-{run}-{sweep}.log").write_text(output, encoding="utf-8")
                if done.returncode:
                    raise RuntimeError(f"Build {run}/{sweep} failed; inspect the preserved log")
                names = ("pdf", "aux", "out", "toc")
                vector = {ext: sha((folder / (name + "." + ext)).read_bytes()) for ext in names}
                if vector == previous:
                    break
                previous = vector
            else:
                raise RuntimeError("No fixed point within five sweeps")
            log = (folder / (name + ".log")).read_text(encoding="utf-8", errors="replace")
            errors = re.findall(r"^!.*|.*(?:undefined|multiply defined|Missing character|Overfull \\hbox|Rerun to get).*", log, re.M)
            if errors:
                raise RuntimeError("Unresolved build diagnostics: " + repr(errors))
            builds.append({"run": run, "sweeps": sweep, "identities": vector,
                           "fatal_undefined_duplicate_glyph_overfull_rerun": 0})
            print(f"Build {run}: fixed point in {sweep} sweeps", flush=True)
        assert builds[0]["identities"] == builds[1]["identities"], "Fresh builds differ"
    pdf = (out / "a" / (name + ".pdf")).read_bytes()
    receipt = {"schema": "pursuing-stacks-module-build/v1", "status": "PASS_BUILD_VISUAL_PENDING",
               "source": {"file": name + ".tex", "bytes": len(source), "sha256": sha(source)},
               "pdf": {"bytes": len(pdf), "sha256": sha(pdf)}, "source_date_epoch": EPOCH,
               "fresh_builds": builds, "mutex": slot.receipt, "captures": captures,
               "scope": f"Standalone normalized module {name}; not a cumulative Stacks rebuild.",
               "independent_mathematical_review_claimed": False}
    (out / "BUILD_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt["pdf"]))


if __name__ == "__main__":
    main()
