"""Build one prior/successor chapter, twice fresh for the successor, under one mutex."""
import sys
sys.path.insert(0, r'C:\Users\Floris\Documents\interlanguage\worktrees\unofficial-ai-stacks-r47-illusie-linear-successor-20260907\tools')
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import r50_successor as r
from build_r49_chapter import diagnostics
from pypdf import PdfReader


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prior', required=True)
    p.add_argument('--successor', required=True)
    p.add_argument('--chapter', required=True)
    p.add_argument('--successor-source', help='Candidate-owned preview path at the successor commit; never mutates cumulative source')
    p.add_argument('--resume', action='store_true', help='Resume this exact source-bound unfinished directory, preserving prior captures')
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--pdflatex', default=shutil.which('pdflatex'))
    p.add_argument('--bibtex', default=shutil.which('bibtex'))
    args = p.parse_args()
    out = args.output.resolve()
    r.require(not out.exists() or (args.resume and not (out / 'BUILD_RECEIPT.json').exists()), 'Choose a fresh or explicitly resumed unfinished output directory')
    r.require(args.pdflatex and args.bibtex, 'TeX executables unavailable')
    r.require(args.chapter.endswith('.tex') and Path(args.chapter).name == args.chapter, 'Expected root chapter filename')
    r.require(args.chapter == 'stacks.tex', 'This build workflow is restricted to the Stacks proof-repair batch')
    r.require(args.prior == '4fddc4a808dc08f74755ac2327e9e9547bb4501f', 'Wrong prior edition')
    r.require(r.sha(r.blob(args.successor, args.successor_source or args.chapter)) == 'C86970D63A200A4782290A6CB1F242563503CA35D90664FBB6A2946DB90DE781', 'Complete reviewed proof postimage changed')
    stem = args.chapter[:-4]
    inputs = (args.chapter, 'preamble.tex', 'stacks-project.cls', 'chapters.tex', 'my.bib')
    for name in inputs[1:]:
        r.require(r.blob(args.prior, name) == r.blob(args.successor, name), 'Dependency changed: ' + name)
    spec = importlib.util.spec_from_file_location('supplement_build', r.ROOT / 'pursuing-stacks/build.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    from tex_process_guard import run_captured
    out.mkdir(parents=True, exist_ok=args.resume)
    env = dict(os.environ, SOURCE_DATE_EPOCH='1790010000', FORCE_SOURCE_DATE='1', TZ='UTC')
    builds, captures = [], []
    with module.TexSlot(15000) as slot:
        r.write(out / ('mutex-acquisition-resume.json' if args.resume else 'mutex-acquisition.json'), slot.receipt)
        for name, ref in [('prior', args.prior), ('a', args.successor), ('b', args.successor)]:
            folder = out / name
            resumed = folder.exists()
            r.require(not resumed or args.resume, 'Build directory already exists')
            folder.mkdir(exist_ok=args.resume)
            for source in inputs:
                lookup = args.successor_source if name != 'prior' and source == args.chapter and args.successor_source else source
                expected = r.blob(ref, lookup)
                if resumed:
                    r.require((folder / source).read_bytes() == expected, 'Resume source drift: ' + source)
                else:
                    (folder / source).write_bytes(expected)
            def launch(command, suffix):
                if resumed: suffix = 'resume-' + suffix
                capture = out / (name + '-' + suffix + '-capture.json')
                r.require(not capture.exists(), 'Refuse to overwrite a prior capture')
                if os.name == 'nt':
                    done = run_captured(command, cwd=folder, env=env, timeout=180,
                        caller_holds_tex_mutex=slot.owned, receipt_path=capture)
                    captures.append({'file': capture.name, **r.identity(capture.read_bytes())})
                else:
                    done = subprocess.run(command, cwd=folder, env=env, timeout=180,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                (out / (name + '-' + suffix + '.log')).write_text(done.stdout, encoding='utf-8')
                r.require(done.returncode == 0, 'Engine failed: ' + name + '/' + suffix)
            previous = {ext: r.sha((folder / (stem + '.' + ext)).read_bytes()) for ext in ('pdf', 'aux', 'out', 'toc', 'bbl')} if resumed else None
            for sweep in range(1, 7):
                launch([args.pdflatex, '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
                    '-file-line-error', '-recorder', '-synctex=1', args.chapter], 'tex-' + str(sweep))
                if sweep == 1 and not resumed: launch([args.bibtex, stem], 'bibtex')
                vector = {ext: r.sha((folder / (stem + '.' + ext)).read_bytes()) for ext in ('pdf', 'aux', 'out', 'toc', 'bbl')}
                if vector == previous: break
                previous = vector
            else: raise ValueError('No fixed point within six sweeps')
            log = (folder / (stem + '.log')).read_text(encoding='utf-8', errors='replace')
            diag = diagnostics(log)
            r.require(not diag['fatal_duplicate_glyph_rerun'], 'Fatal/duplicate/glyph/rerun diagnostics')
            build = {'name': name, 'source_commit': ref, 'sweeps': sweep, 'resumed_exact_inputs': resumed, 'identities': vector,
                'source': r.identity((folder / args.chapter).read_bytes()),
                'pdf': r.identity((folder / (stem + '.pdf')).read_bytes()),
                'pages': len(PdfReader(folder / (stem + '.pdf')).pages), 'diagnostics': diag,
                'log': r.identity((folder / (stem + '.log')).read_bytes()),
                'fls': r.identity((folder / (stem + '.fls')).read_bytes())}
            builds.append(build)
            print(json.dumps({'build': name, 'sweeps': sweep, 'pages': build['pages'], 'pdf': build['pdf']}), flush=True)
        r.require(builds[1]['identities'] == builds[2]['identities'], 'Fresh successor builds differ')
        r.require(builds[1]['diagnostics'] == builds[2]['diagnostics'], 'Successor diagnostics differ')
        before, after = builds[0]['diagnostics'], builds[1]['diagnostics']
        for key in before:
            if key == 'underfull_boxes':
                r.require(after[key] <= before[key], 'New underfull warnings')
            else:
                r.require(before[key] == after[key], 'Diagnostic regression: ' + key)
        r.require(builds[1]['pages'] == builds[2]['pages'], 'Successor page counts differ')
    r.write(out / 'BUILD_RECEIPT.json', {'schema': 'stacks-cumulative-errata-chapter-build/v1',
        'status': 'PASS_BUILD_VISUAL_PENDING', 'prior_public': args.prior, 'source_commit': args.successor,
        'chapter': args.chapter, 'source_date_epoch': '1790010000',
        'input_files': [{'path': (args.successor_source if name == args.chapter and args.successor_source else name),
            'build_filename': name, **r.identity(r.blob(args.successor, args.successor_source if name == args.chapter and args.successor_source else name))} for name in inputs],
        'builds': builds, 'captures': captures, 'mutex': slot.receipt,
        'scope': 'Isolated cumulative-chapter proof, not a complete cross-chapter reader or release.',
        'pagination_change': {'prior': builds[0]['pages'], 'successor': builds[1]['pages'], 'reason': 'The source repair inserts the complete 166-line proof of the corrected refinement criterion. Preserve it in full and inspect every changed and added successor page.'},
        'external_auxiliaries': 'Absent identically; diagnostic multisets must match.',
        'model': 'OpenAI Codex - GPT-6 Astra, Ultra effort'})

if __name__ == '__main__': main()
