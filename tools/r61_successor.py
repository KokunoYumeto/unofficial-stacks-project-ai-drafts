"""Admit and compose eighty-nine source-bound R61 edits in separate transitions."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PRIOR = '95a51593aceb247ac7a183111678c3a0f8b8f4b5'
CANDIDATE = '4185e4882af6f1b432244bf4462dc47b1bb0278b'
MANIFEST = '24BF27947E2917EEC1006533F5E5AF4C83F1E5169E677506276077800D736C6A'
PREFIX = 'ai-integrated/candidates/commons/stacks/errata/r61/'
ID = 'stacks-errata-a04446e-r61'
OVERLAYS = 'ai-integrated/registry/overlays.json'
LEASES = 'ai-integrated/registry/leases.json'
ADMISSION = 'validation/r61-admission-2026-09-30.json'
COMPOSITION = 'validation/r61-source-composition-2026-09-30.json'
HISTORY = 'validation/r61-reviewed-publication-history.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def identity(raw):
    return dict(bytes=len(raw), sha256=sha(raw))


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def evidence_commit(ref):
    path = ROOT/HISTORY
    if not path.exists():
        return ref
    history = json.loads(path.read_bytes())
    require(history['schema'] == 'stacks-r61-reviewed-history-transport/v1'
        and history['public_predecessor'] == PRIOR
        and history['candidate_manifest_sha256'] == MANIFEST, 'Wrong reviewed-history binding')
    steps = {x['kind']:x for x in history['steps']}
    require(set(steps) == {'lease','candidate','admission','composition'} and len(history['steps']) == 4,
        'Transition scope changed')
    require(steps['lease']['local_commit'] == 'fcdbc34c39cd4762fa9288752d7ef071129f2b12'
        and steps['candidate']['local_commit'] == CANDIDATE, 'Transition provenance changed')
    parent = PRIOR
    for item in history['steps']:
        require(item['parent'] == parent and git('rev-parse', item['public_commit']+'^').decode().strip() == parent,
            'Public transition ancestry changed')
        parent = item['public_commit']
    matches = [x['public_commit'] for x in history['steps'] if x['local_commit'] == ref]
    return matches[0] if matches else ref


def blob(ref, name):
    return git('show', evidence_commit(ref)+':'+name)


def write(name, value):
    path = ROOT/name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode())


def now():
    return datetime.now(timezone.utc).isoformat()


def frozen_files(ref, expected):
    ref = evidence_commit(ref)
    tree = {}
    for line in git('ls-tree', '-r', '-z', ref, '--', PREFIX).split(b'\0'):
        if not line:
            continue
        head, name = line.split(b'\t', 1)
        mode, kind, oid = head.split()
        require(mode == b'100644' and kind == b'blob', 'Unexpected candidate mode')
        tree[name.decode()] = oid.decode()
    require(set(tree) == set(expected), 'Frozen candidate closure differs')
    process = subprocess.Popen(['git', '-C', str(ROOT), 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        for name, oid in tree.items():
            process.stdin.write((oid+'\n').encode()); process.stdin.flush()
            header = process.stdout.readline().decode().split()
            require(len(header) == 3 and header[1] == 'blob', 'Missing frozen blob')
            size = int(header[2]); require(size == expected[name]['bytes'], 'Frozen size drift: '+name)
            digest = hashlib.sha256(); remaining = size
            while remaining:
                block = process.stdout.read(min(1048576, remaining)); require(bool(block), 'Truncated frozen blob')
                digest.update(block); remaining -= len(block)
            require(process.stdout.read(1) == b'\n', 'Frozen stream separator')
            require(digest.hexdigest().upper() == expected[name]['sha256'], 'Frozen hash drift: '+name)
        process.stdin.close(); require(process.wait() == 0, 'Frozen stream failed')
    finally:
        if process.poll() is None:
            process.terminate(); process.wait()


def evidence():
    root = ROOT/PREFIX
    raw = blob(CANDIDATE, PREFIX+'candidate.manifest.json')
    require(sha(raw) == MANIFEST, 'Candidate manifest identity drift')
    manifest = json.loads(raw)
    refs = manifest['source_authorities']+manifest['builds']+[manifest[k] for k in
        ('stable_unit_manifest','source_map','decision_ledger','rejection_ledger','formula_diagram_inventory')]
    expected = {PREFIX+r['path']:{k:r[k] for k in ('bytes','sha256')} for r in refs}
    require(len(expected) == len(refs), 'Duplicate manifest reference')
    expected[PREFIX+'candidate.manifest.json'] = identity(raw)
    require(len(expected) == 529, 'Candidate file count changed')
    frozen_files(CANDIDATE, expected)
    for name, item in expected.items():
        require(identity((ROOT/name).read_bytes()) == item, 'Working candidate drift: '+name)
    require(manifest['review_state'] == 'performed' and manifest['independent_replay'] == 'passed'
        and not manifest['unresolved_defects'], 'Candidate review incomplete')
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('r61_retained_verifier', root/'replay/verify.py')
    check = importlib.util.module_from_spec(spec); spec.loader.exec_module(check)
    require(check.verify() == json.loads((root/'replay/source-replay.json').read_bytes()), 'Source replay differs')
    units = json.loads((root/'stable-units.json').read_bytes())['units']
    ids = [u['id'] for u in units]
    require(ids == [f'MC-STK-ERR-{n}' for n in range(2506,2570)], 'Unit scope changed')
    operations = json.loads((root/'cumulative-operation-spec.json').read_bytes())['operations']
    require(len(operations) == 89, 'Operation scope changed')
    maps = [json.loads(x) for x in (root/'source-map.jsonl').read_text(encoding='utf-8').splitlines()]
    original_ops = json.loads((root/'operation-spec.json').read_bytes())['operations']
    require([x['unit_id'] for x in maps] == ids, 'Source-map unit order changed')
    canon = lambda x:json.dumps(x, sort_keys=True)
    require(sorted(map(canon,original_ops)) == sorted(canon(o) for x in maps for o in x['operations']), 'Source-map operations differ')
    builds = json.loads((root/'builds/chapters.json').read_bytes())
    visuals = json.loads((root/'visual/chapters/COMPARISON.json').read_bytes())
    reviewed = json.loads((root/'visual/chapters/ACTUAL_REVIEW.json').read_bytes())
    require(reviewed['prior_pages_raster_compared'] == 913 and reviewed['successor_pages_raster_compared'] == 915
        and reviewed['total_pages_actually_viewed'] == 101 and reviewed['changed_pages_actually_viewed'] == 99
        and reviewed['total_operations_mapped_and_viewed'] == 89,
        'Chapter visual coverage changed')
    require(reviewed['comparison'] == identity((root/'visual/chapters/COMPARISON.json').read_bytes()), 'Chapter review binding changed')
    sources = []
    for stem in ('derived','more-algebra','perfect','cohomology','equiv','spaces-perfect'):
        name = stem+'.tex'; prior = blob(PRIOR,name); authority = blob(manifest['upstream']['commit'],name)
        require(prior == (root/'proof-source/prior'/name).read_bytes(), 'Prior source differs')
        require(authority == (root/'authority'/name).read_bytes(), 'Official authority differs')
        selected = [x for x in operations if x['source'] == name]
        post = check.transform(prior,selected)
        require(post == (root/'cumulative-preview'/name).read_bytes(), 'Composed preview differs')
        rows = {x['group']:x for x in builds['builds'] if x['document'] == stem}
        require(rows['a']['identities'] == rows['b']['identities'], 'Chapter reproduction differs')
        import re
        prior_diag, final_diag = rows['prior']['diagnostics'], rows['a']['diagnostics']
        require(final_diag == rows['b']['diagnostics'] and prior_diag.keys() == final_diag.keys(), 'Chapter diagnostics differ')
        from collections import Counter
        delta = {}
        for key in prior_diag:
            without_line = lambda values:Counter(re.sub(r' at lines? \d+(?:--\d+)?', ' at SOURCE_LINE', value) for value in values)
            before,after = without_line(prior_diag[key]),without_line(final_diag[key])
            delta[key] = dict(added=dict(after-before),removed=dict(before-after))
        retained = json.loads((root/'builds/chapter-diagnostic-comparison.json').read_bytes())
        recorded = next(x for x in retained['chapters'] if x['chapter'] == stem)
        require(delta == recorded['diagnostic_delta'], 'Recorded chapter diagnostic delta changed')
        if stem == 'derived':
            require(delta['overfull']['added'] == {
                'Overfull \\hbox (4.35858pt too wide) in paragraph at SOURCE_LINE':1,
                'Overfull \\hbox (5.62982pt too wide) in paragraph at SOURCE_LINE':1,
                'Overfull \\hbox (18.56595pt too wide) in paragraph at SOURCE_LINE':1,
                'Overfull \\hbox (35.16754pt too wide) in paragraph at SOURCE_LINE':1}
                and delta['overfull']['removed'] == {'Overfull \\hbox (8.17108pt too wide) in paragraph at SOURCE_LINE':1},
                'Reviewed Derived overflow scope changed')
            require(delta['underfull']['added'] == {'Underfull \\vbox (badness 1648) has occurred while \\output is active []':1}
                and not delta['underfull']['removed'], 'Reviewed Derived underfull scope changed')
            require(reviewed['additional_closeup_pages']['derived'] == [11,12,102], 'Overflow closeup review changed')
            require(all(not value['added'] and not value['removed'] for key,value in delta.items()
                if key not in ('overfull','underfull')), 'Other Derived diagnostics changed')
        else:
            require(all(not value['added'] and not value['removed'] for value in delta.values()),
                'Unexpected receiving-chapter diagnostic change')
        require(rows['prior']['source_sha256'] == sha(prior) and rows['a']['source_sha256'] == sha(post), 'Built source differs')
        visual = next(x for x in visuals['chapters'] if x['chapter'] == stem)
        viewed = sorted(p for x in reviewed['viewed_sheets'] if x['chapter'] == stem for p in x['pages'])
        require(visual['selected_pages'] == viewed, 'Uninspected selected page')
        require(set(visual['changed_pages']).issubset(viewed), 'Uninspected changed page')
        require({x['operation_id'] for x in selected} == {x['operation_id'] for x in visual['mapped_operations']}, 'Unmapped operation')
        for role, group in (('prior','prior'),('successor','a')):
            require(sha((root/'proofs'/(stem+'-'+role+'.pdf')).read_bytes()) == rows[group]['identities']['pdf'], 'Chapter PDF differs')
        sources.append(dict(source=name,preimage=identity(prior),postimage=identity(post),operations=selected))
    supplement = json.loads((root/'builds/supplement.json').read_bytes())
    a,b = supplement['builds']
    require(a['identities'] == b['identities'] and a['diagnostics'] == b['diagnostics'], 'Supplement reproduction differs')
    require(all(not v for k,v in a['diagnostics'].items() if k != 'underfull'), 'Unresolved supplement diagnostic')
    actual = json.loads((root/'visual/supplement/ACTUAL_REVIEW.json').read_bytes())
    require(actual['status'] == 'PASS_COMPLETE_SUPPLEMENT_VISUAL_REVIEW'
        and actual['pdf'] == identity((root/'proofs/correction-proofs.pdf').read_bytes()), 'Supplement visual binding changed')
    require(actual['prior_pages_actually_viewed'] == list(range(1,160))
        and actual['final_pages_actually_viewed'] == [109,110,111,112]
        and sorted(actual['final_pages_actually_viewed']+actual['final_pages_pixel_identical_to_viewed_prior']) == list(range(1,160)), 'Incomplete supplement page coverage')
    require(actual['pdf']['sha256'] == a['identities']['pdf'], 'Supplement PDF differs')
    with zipfile.ZipFile(root/'proofs/complete-proof-source.zip') as archive:
        names = {x.removeprefix(PREFIX+'proof-source/') for x in expected if x.startswith(PREFIX+'proof-source/')}
        require(set(archive.namelist()) == names and archive.testzip() is None, 'Incomplete source archive')
        for name in archive.namelist():
            require(archive.read(name) == (root/'proof-source'/name).read_bytes(), 'Source ZIP member differs')
    return manifest, ids, sources, expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('check','admit','compose'))
    args = parser.parse_args()
    manifest, ids, sources, expected = evidence()
    head = git('rev-parse','HEAD').decode().strip()
    if args.action == 'check':
        print(json.dumps(dict(status='PASS',files=len(expected),units=64,operations=89))); return
    require(git('diff','--cached','--name-only') == b'', 'Unrelated staged changes')
    for row in sources:
        require(identity((ROOT/row['source']).read_bytes()) == row['preimage'], 'Dirty or already composed chapter')
    moduli = (ROOT/'moduli.tex').read_bytes()
    if args.action == 'admit':
        require(head == CANDIDATE and not (ROOT/ADMISSION).exists(), 'Admission state changed')
        raw = blob(PRIOR,OVERLAYS); require((ROOT/OVERLAYS).read_bytes() == raw, 'Registry changed')
        registry = json.loads(raw)
        require(len(registry['registered_entries']) == 63, 'Predecessor overlay scope changed')
        require(not set(ids).intersection(i for x in registry['registered_entries'] for i in x['stable_ids']), 'Reused stable ID')
        entry = dict(id=ID,namespace=manifest['namespace'],writer=manifest['writer_task'],source_commit=manifest['upstream']['commit'],
            source_tree=manifest['upstream']['tree'],manifest_sha256=MANIFEST,stable_ids=ids,rights_state=manifest['rights_state'],
            review_receipt=PREFIX.removeprefix('ai-integrated/')+'replay/independent-review.json',admitted_at_utc=now())
        registry['registered_entries'].append(entry)
        lease_raw = (ROOT/LEASES).read_bytes(); require(lease_raw == blob(CANDIDATE,LEASES), 'Lease registry changed')
        leases = json.loads(lease_raw); issued = leases['events'][-1]
        require(issued['event_id'] == 'lease-event-000134' and issued['state'] == 'active'
            and issued['lease_id'] == manifest['lease_id'], 'Lease identity changed')
        released = {**issued,'event_id':'lease-event-000135','event':'released','state':'released',
            'issued_at_utc':now(),'supersedes_event_id':issued['event_id']}
        leases['events'].append(released)
        from jsonschema import Draft202012Validator
        for value,name in ((registry,'overlay-entry'),(leases,'lease-registry')):
            Draft202012Validator(json.loads((ROOT/f'ai-integrated/schemas/{name}.schema.json').read_bytes())).validate(value)
        write(OVERLAYS,registry); write(LEASES,leases)
        write(ADMISSION,dict(schema='stacks-r61-separate-admission/v1',passed=True,previous_public=PRIOR,candidate_commit=CANDIDATE,
            candidate_manifest_sha256=MANIFEST,admission=entry,release_event=released,source_composed=False,candidate_files_checked=len(expected)))
    else:
        require(not (ROOT/COMPOSITION).exists(), 'Composition already exists')
        for name in (ADMISSION,OVERLAYS,LEASES):
            require((ROOT/name).read_bytes() == blob(head,name), 'Admission must be committed')
        admission = json.loads((ROOT/ADMISSION).read_bytes())
        registry = json.loads((ROOT/OVERLAYS).read_bytes())
        require(admission['candidate_commit'] == CANDIDATE and admission['admission'] == registry['registered_entries'][-1]
            and admission['admission']['id'] == ID, 'Admission binding changed')
        for row in sources:
            post = (ROOT/PREFIX/'cumulative-preview'/row['source']).read_bytes()
            require(identity(post) == row['postimage'], 'Postimage changed')
            (ROOT/row['source']).write_bytes(post)
        write(COMPOSITION,dict(schema='stacks-r61-exact-source-composition/v1',passed=True,previous_public=PRIOR,
            candidate_commit=CANDIDATE,manifest_sha256=MANIFEST,admission_commit=head,sources=sources,units=64,operations=89,
            whole_isolated_payload_copied=False,only_admitted_operations_applied=True,prior_additions_preserved=True,
            prevalidated_preview_bytes_match_composition=True,model='OpenAI Codex - GPT-6 Astra, Ultra effort'))
    require((ROOT/'moduli.tex').read_bytes() == moduli, 'Unrelated source changed')
    print(json.dumps(dict(action=args.action,status='PASS',units=64,operations=89)))


if __name__ == '__main__':
    main()
