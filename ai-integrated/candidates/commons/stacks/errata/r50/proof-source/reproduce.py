"""Reproduce the two isolated chapter proofs, with bounded captured TeX jobs."""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from tex_slot import TexSlot

ROOT = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--pdflatex', default=shutil.which('pdflatex'))
    p.add_argument('--bibtex', default=shutil.which('bibtex'))
    args = p.parse_args()
    out = args.output.resolve()
    if out.exists() or not args.pdflatex or not args.bibtex:
        raise ValueError('Choose a new output directory and available TeX engines')
    expected = json.loads((ROOT / 'inputs.json').read_bytes())
    for row in expected['files']:
        raw = (ROOT / row['path']).read_bytes()
        assert len(raw) == row['bytes'] and sha(raw) == row['sha256'], row['path']
    out.mkdir(parents=True)
    env = dict(os.environ, SOURCE_DATE_EPOCH='1789776000', FORCE_SOURCE_DATE='1', TZ='UTC')
    results, captures = [], []
    if os.name == 'nt':
        from tex_process_guard import run_captured
    with TexSlot(15000) as slot:
        (out / 'mutex-acquisition.json').write_text(json.dumps(slot.receipt, indent=2) + '\n')
        for role in ('authority', 'candidate'):
            folder = out / role
            folder.mkdir()
            for row in expected['files']:
                if row['path'].startswith(role + '/'):
                    (folder / Path(row['path']).name).write_bytes((ROOT / row['path']).read_bytes())
            commands = []
            for run in range(1, 4):
                commands.append((f'tex-{run}', [args.pdflatex, '-no-shell-escape', '-recorder', '-synctex=1',
                    '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'spaces-limits.tex']))
                if run == 1:
                    commands.append(('bibtex', [args.bibtex, 'spaces-limits']))
            for label, command in commands:
                capture = out / f'{role}-{label}-capture.json'
                if os.name == 'nt':
                    result = run_captured(command, cwd=folder, env=env, timeout=180,
                        caller_holds_tex_mutex=slot.owned, receipt_path=capture)
                    captures.append({'path': capture.name, 'sha256': sha(capture.read_bytes())})
                else:
                    result = subprocess.run(command, cwd=folder, env=env, timeout=180,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                (out / f'{role}-{label}.log').write_text(result.stdout, encoding='utf-8')
                if result.returncode:
                    raise RuntimeError(f'Failed {role}/{label}; inspect preserved output')
            pdf = (folder / 'spaces-limits.pdf').read_bytes()
            log = (folder / 'spaces-limits.log').read_text(encoding='utf-8', errors='replace')
            diagnostics = {
                'undefined_references': dict(sorted(Counter(re.findall(r"LaTeX Warning: Reference `([^']+)'", log)).items())),
                'undefined_citations': dict(sorted(Counter(re.findall(r"LaTeX Warning: Citation `([^']+)'", log)).items())),
                'overfull_boxes': len(re.findall(r'Overfull \\[hv]box', log)),
                'fatal_duplicate_glyph': re.findall(r'^!.*|.*(?:multiply defined|Missing character).*', log, re.M)}
            assert not diagnostics['fatal_duplicate_glyph']
            actual = {'bytes': len(pdf), 'sha256': sha(pdf)}
            assert actual == expected['pdfs'][role], (role, actual, expected['pdfs'][role])
            results.append({'role': role, 'pdf': actual, 'exact_historical_pdf_reproduced': True,
                            'diagnostics': diagnostics})
            print(json.dumps(results[-1]), flush=True)
        assert results[0]['diagnostics'] == results[1]['diagnostics']
    receipt = {'schema': 'stacks-r50-proof-source-reproduction/v1', 'passed': True,
        'scope': 'Exact isolated authority/candidate proofs, not a complete cross-chapter reader.',
        'source_date_epoch': '1789776000', 'inputs': expected['files'], 'builds': results,
        'captures': captures, 'mutex': slot.receipt,
        'model': 'OpenAI Codex - GPT-6 Astra, Ultra effort'}
    (out / 'SOURCE_REPRODUCTION.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
