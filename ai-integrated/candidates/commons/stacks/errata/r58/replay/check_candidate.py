"""Verify the sealed R58 artifact closure and exact forward/inverse source maps."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sha = lambda raw: hashlib.sha256(raw).hexdigest().upper()
load = lambda name: json.loads((ROOT / name).read_bytes())

def replay(raw, operations, cumulative=False):
    ak, bk = ('cumulative_start_byte', 'cumulative_end_byte_exclusive') if cumulative else ('start_byte', 'end_byte_exclusive')
    ordered = sorted(operations, key=lambda x:x[ak])
    boundary, delta, inverse = 0, 0, []
    for op in ordered:
        a, b = op[ak], op[bk]
        old, new = op['old_text'].encode(), op['replacement_text'].encode()
        assert 0 <= boundary <= a < b <= len(raw), op['operation_id']
        assert raw[a:b] == old and sha(old) == op['old_sha256'] and sha(new) == op['replacement_sha256']
        inverse.append((a+delta, a+delta+len(new), new, old))
        delta += len(new)-len(old); boundary = b
    post = raw
    for op in reversed(ordered):
        post = post[:op[ak]] + op['replacement_text'].encode() + post[op[bk]:]
    recovered = post
    for a,b,new,old in reversed(inverse):
        assert recovered[a:b] == new
        recovered = recovered[:a] + old + recovered[b:]
    assert recovered == raw
    return post

def main(manifest=None):
    if manifest is None:
        manifest = load('candidate.manifest.json')
    refs = manifest['source_authorities'] + manifest['builds'] + [manifest[k] for k in
        ['stable_unit_manifest','source_map','decision_ledger','rejection_ledger','formula_diagram_inventory']]
    names = set()
    for row in refs:
        name = row['path']; p = Path(name)
        assert not p.is_absolute() and '..' not in p.parts and name not in names
        raw = (ROOT/p).read_bytes()
        assert sha(raw) == row['sha256'] and len(raw) == row['bytes'], name
        names.add(name)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    expected = names | ({'candidate.manifest.json'} if (ROOT/'candidate.manifest.json').exists() else set())
    assert actual == expected
    assert manifest['review_state'] == 'performed' and manifest['independent_replay'] == 'passed'
    assert not manifest['unresolved_defects']
    materialization = load('materialization.json')
    for row in materialization['files']:
        raw = (ROOT/row['file']).read_bytes()
        assert sha(raw) == row['sha256'] and len(raw) == row['bytes'], row['file']
    units = load('stable-units.json')['units']
    ids = [x['id'] for x in units]
    assert ids == [f'MC-STK-ERR-{n}' for n in range(1906,2466)]
    spec = load('operation-spec.json')['operations']
    assert len(spec) == 690 and len({op['operation_id'] for op in spec}) == 690
    assert {op['operation_id'] for op in spec} == {k for x in units for k in x['operation_ids']}
    maps = [json.loads(line) for line in (ROOT/'source-map.jsonl').read_text(encoding='utf-8').splitlines()]
    assert [x['unit_id'] for x in maps] == ids
    fields = ['operation_id','source','start_byte','end_byte_exclusive','old_text','replacement_text','old_sha256','replacement_sha256']
    canon = lambda o: tuple(o[k] for k in fields)
    assert sorted(map(canon,spec)) == sorted(canon(o) for r in maps for o in r['operations'])
    isolated = replay((ROOT/'authority/algebra.tex').read_bytes(),spec)
    assert isolated == (ROOT/'payload/algebra.tex').read_bytes()
    cumulative = replay((ROOT/'proof-source/prior/algebra.tex').read_bytes(),spec,True)
    assert cumulative == (ROOT/'cumulative-preview/algebra.tex').read_bytes()
    visible = (ROOT/'visible-edition-preview/algebra.tex').read_bytes()
    assert visible == (ROOT/'proof-source/successor/algebra.tex').read_bytes()
    routes = load('editorial-apparatus-operations.json')
    stripped = visible
    for text in [routes['front_notice']] + [r['text'] for r in routes['body_notice_operations']]:
        assert stripped.count(text.encode()) == 1
        stripped = stripped.replace(text.encode(),b'')
    assert stripped == cumulative
    review = load('replay/independent-review.json')
    assert review['passed'] and all(x['passed'] for x in review['checks'])
    transport = load('evidence/completed/TRANSPORT.json')
    for row in transport['files']:
        assert sha((ROOT/row['public_file']).read_bytes()) == row['public_sha256']
        assert row['inverse_recovers_original_json']
    build = load('builds/attempt-16/BUILD_RECEIPT.json')
    for doc in ['algebra','algebra-editorial']:
        pair = [r for r in build['builds'] if r['document'] == doc and r['group'] in ['a','b']]
        assert len(pair) == 2 and pair[0]['identities'] == pair[1]['identities']
        assert sha((ROOT/'proofs'/(doc+'.pdf')).read_bytes()) == pair[0]['identities']['pdf']
        assert not any(pair[0]['diagnostics'][k] for k in ['fatal','missing_glyph','undefined_reference','undefined_citation','duplicate','rerun'])
    chapter = load('visual/chapter/CHAPTER_VISUAL_ACCEPTANCE.json')
    companion = load('visual/companion/COMPANION_VISUAL_ACCEPTANCE.json')
    assert chapter['whole_chapter_visual_acceptance'] and companion['whole_companion_visual_acceptance']
    assert chapter['full_page_layouts'] == 484 and companion['full_page_layouts'] == 667
    assert chapter['source_pdf_sha256'] == sha((ROOT/'proofs/algebra.pdf').read_bytes())
    assert companion['source_pdf_sha256'] == sha((ROOT/'proofs/algebra-editorial.pdf').read_bytes())
    image_count = 0
    for package in load('visual/IMAGE_PACKAGES.json')['packages']:
        raw = (ROOT/package['archive']).read_bytes()
        assert sha(raw) == package['sha256'] and len(raw) == package['bytes']
        with zipfile.ZipFile(ROOT/package['archive']) as z:
            assert z.testzip() is None and set(z.namelist()) == {r['file'] for r in package['members']}
            for row in package['members']:
                raw = z.read(row['file'])
                assert sha(raw) == row['sha256'] and len(raw) == row['bytes']
                image_count += 1
    with zipfile.ZipFile(ROOT/'reproduction/source-08/algebra-r58-complete-source.zip') as z:
        assert z.testzip() is None and len(z.namelist()) == len(set(z.namelist())) == 1121
        package = json.loads(z.read('algebra-r58-source/PACKAGE_MANIFEST.json'))
        for row in package['files']:
            raw = z.read('algebra-r58-source/'+row['file'])
            assert sha(raw) == row['sha256'] and len(raw) == row['bytes']
        assert z.read('algebra-r58-source/algebra-editorial-assembled.tex') == (ROOT/'reproduction/source-08/algebra-editorial-assembled.tex').read_bytes()
    print(json.dumps(dict(status='PASS',candidate_files=len(actual),units=len(ids),operations=len(spec),
        full_inverse_exact=True,chapter_pages=484,companion_pages=667,visual_images=image_count,source_zip_members=1121)))

if __name__ == '__main__': main()
