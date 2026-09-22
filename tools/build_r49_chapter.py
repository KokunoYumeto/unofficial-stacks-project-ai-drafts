"""Bounded cumulative-chapter regression build; no source composition or publication.

Build the prior cumulative chapter once and the R49 successor twice in fresh
directories. External chapter auxiliaries are deliberately absent in all three
builds; this is a comparative regression proof, not a complete Stacks reader.
"""
import argparse
from collections import Counter
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

import r49_successor as r

ROOT = r.ROOT
EPOCH = '1790010000'
INPUTS = ('derham.tex', 'preamble.tex', 'stacks-project.cls', 'chapters.tex', 'my.bib')


def diagnostics(log):
    return {
        'undefined_references': dict(sorted(Counter(re.findall(r"LaTeX Warning: Reference `([^']+)'", log)).items())),
        'undefined_citations': dict(sorted(Counter(re.findall(r"LaTeX Warning: Citation `([^']+)'", log)).items())),
        'overfull_boxes': len(re.findall(r'Overfull \\[hv]box', log)),
        'underfull_boxes': len(re.findall(r'Underfull \\[hv]box', log)),
        # TeX's overfull-box font dump may wrap with a printed exclamation glyph.
        # That exact font-dump prefix is not an error; actual ! diagnostics remain fatal.
        'fatal_duplicate_glyph_rerun': re.findall(r'^!(?! \[\]\[\]\\[A-Za-z0-9]+/).*|.*(?:multiply defined|Missing character|Rerun to get).*', log, re.M),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--pdflatex', default=shutil.which('pdflatex'))
    parser.add_argument('--bibtex', default=shutil.which('bibtex'))
    parser.add_argument('--slot-wait-ms', type=int, default=15000)
    args = parser.parse_args()
    out = args.output.resolve()
    r.require(not out.exists(), 'Choose a fresh output directory; existing evidence is preserved')
    r.require(args.pdflatex and args.bibtex, 'TeX engines unavailable')
    files, _, ops, authority = r.evidence()
    expected, _ = r.compose(r.blob(r.PREVIOUS, 'derham.tex'), authority, ops)
    current = r.git('rev-parse', 'HEAD').decode().strip()
    r.require(r.blob(current, 'derham.tex') == expected, 'Current committed chapter is not exact R49 composition')
    for name in INPUTS[1:]:
        r.require(r.blob(current, name) == r.blob(r.PREVIOUS, name), 'Build dependency changed: ' + name)
    spec = importlib.util.spec_from_file_location('supplement_build', ROOT / 'pursuing-stacks/build.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    from tex_process_guard import run_captured
    from pypdf import PdfReader
    out.mkdir(parents=True)
    env = dict(os.environ, SOURCE_DATE_EPOCH=EPOCH, FORCE_SOURCE_DATE='1', TZ='UTC')
    builds, captures = [], []
    with module.TexSlot(args.slot_wait_ms) as slot:
        r.write_json(out / 'mutex-acquisition.json', slot.receipt)
        for name, ref in [('prior', r.PREVIOUS), ('a', current), ('b', current)]:
            folder = out / name
            folder.mkdir()
            for source in INPUTS:
                (folder / source).write_bytes(r.blob(ref, source))
            def launch(command, suffix):
                capture = out / (name + '-' + suffix + '-capture.json')
                if os.name == 'nt':
                    done = run_captured(command, cwd=folder, env=env, timeout=180,
                                        caller_holds_tex_mutex=slot.owned, receipt_path=capture)
                    captures.append({'file': capture.name, **r.identity(capture.read_bytes())})
                else:
                    done = subprocess.run(command, cwd=folder, env=env, timeout=180,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                (out / (name + '-' + suffix + '.log')).write_text(done.stdout, encoding='utf-8')
                r.require(done.returncode == 0, 'Engine failed: ' + name + '/' + suffix)
            previous = None
            for sweep in range(1, 7):
                launch([args.pdflatex, '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
                        '-recorder', '-synctex=1', 'derham.tex'], 'tex-' + str(sweep))
                if sweep == 1:
                    launch([args.bibtex, 'derham'], 'bibtex')
                vector = {ext: r.sha((folder / ('derham.' + ext)).read_bytes())
                          for ext in ('pdf', 'aux', 'out', 'toc', 'bbl')}
                if vector == previous:
                    break
                previous = vector
            else:
                raise ValueError('No deterministic fixed point in six passes')
            log = (folder / 'derham.log').read_text(encoding='utf-8', errors='replace')
            diag = diagnostics(log)
            r.require(not diag['fatal_duplicate_glyph_rerun'], 'New build has fatal/duplicate/glyph/rerun diagnostics')
            build = {'name': name, 'source_commit': ref, 'sweeps': sweep, 'identities': vector,
                     'source': r.identity((folder / 'derham.tex').read_bytes()),
                     'pdf': r.identity((folder / 'derham.pdf').read_bytes()),
                     'pages': len(PdfReader(folder / 'derham.pdf').pages), 'diagnostics': diag,
                     'log': r.identity((folder / 'derham.log').read_bytes()),
                     'fls': r.identity((folder / 'derham.fls').read_bytes())}
            builds.append(build)
            print(json.dumps({'build': name, 'sweeps': sweep, 'pages': build['pages'], 'pdf': build['pdf']}), flush=True)
        r.require(builds[1]['identities'] == builds[2]['identities'], 'Fresh successor builds differ')
        r.require(builds[0]['diagnostics'] == builds[1]['diagnostics'] == builds[2]['diagnostics'],
                  'Build diagnostic multiset changed')
        r.require(builds[0]['pages'] == builds[1]['pages'], 'Page count changed; investigate before publishing')
    r.write_json(out / 'BUILD_RECEIPT.json', {
        'schema': 'stacks-r49-cumulative-chapter-build/v1', 'status': 'PASS_BUILD_VISUAL_PENDING',
        'prior_public': r.PREVIOUS, 'source_commit': current, 'source_date_epoch': EPOCH,
        'input_files': [{'path': name, **r.identity(r.blob(current, name))} for name in INPUTS],
        'builds': builds, 'captures': captures, 'mutex': slot.receipt,
        'scope': 'Isolated cumulative de Rham regression proof, not a complete cross-chapter reader or release.',
        'external_auxiliaries': 'Absent identically in baseline and successors; unresolved-reference multisets must match.',
        'model': 'OpenAI Codex — GPT-6 Astra, Ultra effort'})


if __name__ == '__main__':
    main()
