"""Reproduce the three corrected chapters and complete R59 editorial proofs."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
EPOCH = '1790010000'
CHAPTERS = ('examples', 'more-algebra', 'brauer')


def sha(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def write(path, value):
    path.write_bytes((json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode())


def diagnostics(text):
    patterns = {
        'fatal': r'^!\s+(?!\[\])\S.*|^.*(?:LaTeX Error|Package .* Error|Undefined control sequence|Emergency stop|Fatal error|Missing .* inserted|invalid character).*',
        'missing_glyph': r'^.*Missing character:.*',
        'duplicate': r'^.*(?:multiply defined|duplicate ignored|destination with the same identifier).*',
        'rerun': r'^.*(?:Rerun to get|Label\(s\) may have changed|rerunfilecheck.*Warning).*',
        'overfull': r'^Overfull \\[hv]box.*',
        'underfull': r'^Underfull \\[hv]box.*',
    }
    result = {key: re.findall(pattern, text, re.M) for key, pattern in patterns.items()}
    blocks = re.findall(r'LaTeX Warning:[\s\S]*?(?=\n\s*\n|\Z)', text)
    for key, word in [('undefined_reference', 'reference'), ('undefined_citation', 'citation')]:
        result[key] = [block for block in blocks if 'undefined' in block.replace('\n', '').lower()
                       and word in block.replace('\n', '').lower()]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    manifest_raw = (HERE / 'PACKAGE_MANIFEST.json').read_bytes()
    manifest = json.loads(manifest_raw)
    for row in manifest['files']:
        path = (HERE / row['file']).resolve()
        assert path.is_relative_to(HERE) and path.is_file(), row['file']
        raw = path.read_bytes()
        assert len(raw) == row['bytes'] and sha(raw) == row['sha256'], row['file']
    if args.validate_only:
        print(json.dumps(dict(status='PASS_PACKAGE_INPUTS', files=len(manifest['files']), manifest_sha256=sha(manifest_raw))))
        return
    if args.output is None:
        parser.error('--output is required')
    out = args.output.resolve()
    assert not out.exists() and not HERE.is_relative_to(out)
    engines = {x: shutil.which(x) for x in ('pdflatex', 'xelatex', 'bibtex')}
    assert all(engines.values()), 'pdfLaTeX, XeLaTeX and BibTeX are required'
    from tex_mutex import TexSlot
    if os.name == 'nt':
        from tex_process_guard import run_captured
    from pypdf import PdfReader
    env = dict(os.environ, SOURCE_DATE_EPOCH=EPOCH, FORCE_SOURCE_DATE='1', TZ='UTC')
    out.mkdir(parents=True)
    (out / 'PACKAGE_MANIFEST.json').write_bytes(manifest_raw)
    receipt = dict(schema='stacks-r59-portable-build/v1', created_at_utc=datetime.now(timezone.utc).isoformat(),
        package_manifest_sha256=sha(manifest_raw), source_date_epoch=EPOCH,
        builds=[], captures=[], rendered_acceptance=False, admission=False, publication=False)
    slot = TexSlot(1000)

    def launch(command, folder, label):
        capture = out / (label + '-capture.json')
        if os.name == 'nt':
            done = run_captured(command, cwd=folder, env=env, timeout=900,
                caller_holds_tex_mutex=slot.owned, receipt_path=capture)
            receipt['captures'].append(dict(file=capture.name, sha256=sha(capture.read_bytes())))
        else:
            done = subprocess.run(command, cwd=folder, env=env, timeout=900,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        (out / (label + '-output.log')).write_text(done.stdout, encoding='utf-8')
        assert done.returncode == 0, 'Engine failed: ' + label
        return done.stdout

    def build(group, stem, engine):
        folder = out / group
        previous = None
        for sweep in range(1, 9):
            command = [engines[engine], '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-recorder', '-synctex=1']
            if 'miktex' in engines[engine].lower():
                command.append('--disable-installer')
            command.append(stem + '.tex')
            launch(command, folder, f'{group}-{stem}-tex-{sweep}')
            aux = (folder / (stem + '.aux')).read_bytes()
            if sweep == 1 and b'\\bibdata' in aux:
                result = launch([engines['bibtex'], stem], folder, group + '-' + stem + '-bibtex')
                assert not re.search(r"Warning--I didn't find|I couldn't open|error message", result, re.I), 'Missing bibliography'
            vector = {ext: sha((folder / (stem + '.' + ext)).read_bytes()) for ext in ('pdf', 'aux', 'out', 'toc', 'bbl')
                      if (folder / (stem + '.' + ext)).exists()}
            if vector == previous:
                break
            previous = vector
        else:
            raise ValueError('No fixed point: ' + group + '/' + stem)
        log = (folder / (stem + '.log')).read_text(encoding='utf-8', errors='replace')
        diag = diagnostics(log)
        failures = {k: v for k, v in diag.items() if k not in ('overfull', 'underfull') and v}
        result = dict(group=group, document=stem, engine=engine, sweeps=sweep, identities=vector,
            source_sha256=sha((folder / (stem + '.tex')).read_bytes()), diagnostics=diag,
            pages=len(PdfReader(folder / (stem + '.pdf')).pages), log_sha256=sha(log.encode()))
        receipt['builds'].append(result)
        write(out / 'BUILD_PROGRESS.json', receipt)
        assert not failures, 'Unresolved diagnostics: ' + group + '/' + stem + ': ' + ', '.join(failures)
        print(json.dumps(dict(group=group, document=stem, pages=result['pages'], sweeps=sweep,
            pdf_sha256=vector['pdf'], overfull=len(diag['overfull']), underfull=len(diag['underfull']))), flush=True)
        return result

    try:
        with slot:
            for group in ('prior', 'a', 'b'):
                folder = out / group
                folder.mkdir()
                for row in manifest['files']:
                    # Reference authorities and syntax trees document the package;
                    # they are not execution inputs and need not be copied three times.
                    name = row['file']
                    if name.startswith(('reference-authority/', 'notes-source/', 'prior/', 'successor/')):
                        continue
                    target = folder / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes((HERE / name).read_bytes())
                if group == 'prior':
                    for stem in CHAPTERS:
                        (folder / (stem + '.tex')).write_bytes((HERE / 'prior' / (stem + '.tex')).read_bytes())
            # Check the converted supplement before the longer chapter runs.
            build('a', 'correction-proofs', 'xelatex')
            build('b', 'correction-proofs', 'xelatex')
            for group in ('prior', 'a', 'b'):
                for stem in CHAPTERS:
                    build(group, stem, 'pdflatex')
            for stem in (*CHAPTERS, 'correction-proofs'):
                a, = [x for x in receipt['builds'] if x['group'] == 'a' and x['document'] == stem]
                b, = [x for x in receipt['builds'] if x['group'] == 'b' and x['document'] == stem]
                assert a['identities'] == b['identities'] and a['diagnostics'] == b['diagnostics'], 'Fresh successor builds differ: ' + stem
            receipt['status'] = 'PASS_FIXED_POINT_REPRODUCTION_VISUAL_PENDING'
    except Exception as error:
        receipt['status'] = 'NO_ENGINE_SLOT_UNAVAILABLE' if 'not acquired' in str(error) and not receipt['captures'] else 'BUILD_ERROR'
        receipt['error'] = str(error)
    finally:
        receipt['mutex'] = getattr(slot, 'receipt', {})
        write(out / 'BUILD_RECEIPT.json', receipt)
    print(json.dumps(dict(status=receipt['status'], builds=len(receipt['builds']), output=str(out), error=receipt.get('error'))))
    if receipt['status'] == 'BUILD_ERROR':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
