"""Exact R49 transport and cumulative replay; never merge a candidate branch."""
import argparse
import difflib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]
PREVIOUS = 'ad922ad1fdf496debd487a49b95bc77633363970'
ADMISSION = '7b888f82e3988a174a0a97bbdb8bc7cce5a368dd'
AUTHORITY = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
PREFIX = 'ai-integrated/candidates/commons/stacks/errata/r49/'
MANIFEST = '8B00DC8D9F6E400F4CD05F9473EFDA71A167E4F272BB509FA7108B9203E673E0'
OVERLAYS = 'ai-integrated/registry/overlays.json'
LEASES = 'ai-integrated/registry/leases.json'
IMPORT_RECEIPT = 'validation/r49-registry-import-2026-09-22.json'
SOURCE_RECEIPT = 'validation/r49-source-composition-2026-09-22.json'


def require(value, message):
    if not value:
        raise ValueError(message)


def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, check=True).stdout


def sha(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def identity(raw):
    return {'bytes': len(raw), 'sha256': sha(raw)}


def blob(ref, name):
    return git('show', ref + ':' + name)


def read_json(raw):
    return json.loads(raw)


def append_check(before, after, key, count):
    require(after[key][:len(before[key])] == before[key] and len(after[key]) == len(before[key]) + count,
            'Non-append registry change')
    require({k: v for k, v in before.items() if k != key} == {k: v for k, v in after.items() if k != key},
            'Registry header changed')


def candidate_archive():
    archive = git('archive', '--format=tar', ADMISSION, '--', PREFIX)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
        for item in stream:
            if item.isdir():
                continue
            require(item.isfile() and item.name.startswith(PREFIX) and '..' not in Path(item.name).parts,
                    'Unsafe candidate member')
            require(item.name not in files, 'Duplicate candidate member')
            files[item.name] = stream.extractfile(item).read()
    manifest = read_json(files[PREFIX + 'candidate.manifest.json'])
    require(sha(files[PREFIX + 'candidate.manifest.json']) == MANIFEST, 'Wrong admitted manifest')
    closure = set()
    def walk(value):
        if isinstance(value, dict):
            if {'path', 'bytes', 'sha256'} <= value.keys():
                name = PREFIX + value['path']
                require(name in files and identity(files[name]) == {'bytes': value['bytes'], 'sha256': value['sha256']},
                        'Manifest reference drift: ' + name)
                closure.add(name)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(manifest)
    require(closure == set(files) - {PREFIX + 'candidate.manifest.json'},
            'Candidate includes unbound files or missing manifest references')
    review = read_json(files[PREFIX + 'replay/FINAL_INDEPENDENT_REVIEW.json'])
    require(review['passed'] and review['source_replay_passed'] and review['source_operations'] == 7
            and review['source_units'] == 5 and all(c['passed'] for c in review['checks']), 'Candidate review failed')
    require(manifest['review_state'] == 'performed' and manifest['independent_replay'] == 'passed', 'Candidate not reviewed')
    require(manifest['candidate_id'] == review['candidate_id'] == 'stacks-errata-a04446e-r49', 'Wrong candidate')
    return files, len(closure)


def evidence():
    files, closure = candidate_archive()
    before = read_json(blob(PREVIOUS, OVERLAYS))
    after = read_json(blob(ADMISSION, OVERLAYS))
    append_check(before, after, 'registered_entries', 1)
    entry = after['registered_entries'][-1]
    require(entry['id'] == 'stacks-errata-a04446e-r49' and entry['manifest_sha256'] == MANIFEST,
            'Wrong registry successor')
    old_leases, new_leases = read_json(blob(PREVIOUS, LEASES)), read_json(blob(ADMISSION, LEASES))
    append_check(old_leases, new_leases, 'events', 2)
    issue, release = new_leases['events'][-2:]
    require(issue['state'] == 'active' and release['state'] == 'released'
            and release['supersedes_event_id'] == issue['event_id']
            and issue['namespace'] == release['namespace'] == entry['namespace'], 'Lease succession mismatch')
    require(issue['event_id'] == 'lease-event-000102' and release['event_id'] == 'lease-event-000103',
            'Wrong historical R49 lease events')
    ops = read_json(files[PREFIX + 'operation-spec.json'])['operations']
    require(len(ops) == 7 and {o['stable_id'] for o in ops} == set(entry['stable_ids']), 'Operation/ID closure mismatch')
    authority = blob(AUTHORITY, 'derham.tex')
    require(authority == files[PREFIX + 'authority/source/derham.tex'], 'Wrong source authority')
    payload = apply_exact(authority, ops)
    require(payload == files[PREFIX + 'payload/derham.tex'], 'Isolated payload replay failed')
    return files, closure, ops, authority


def apply_exact(source, ops):
    previous = len(source) + 1
    for op in sorted(ops, key=lambda x: x['start_byte'], reverse=True):
        a, b = op['start_byte'], op['end_byte_exclusive']
        old, new = op['old_text'].encode(), op['replacement_text'].encode()
        require(0 <= a <= b <= previous and source[a:b] == old, 'Operation preimage or overlap failure')
        source = source[:a] + new + source[b:]
        previous = a
    return source


def compose(previous, authority, ops):
    original_lines, current_lines = authority.splitlines(True), previous.splitlines(True)
    mapping = {}
    for block in difflib.SequenceMatcher(None, original_lines, current_lines, autojunk=False).get_matching_blocks():
        for i in range(block.size):
            mapping[block.a + i] = block.b + i
    offsets = [0]
    for line in current_lines:
        offsets.append(offsets[-1] + len(line))
    rebound = []
    for op in ops:
        require(op['source'] == 'derham.tex' and op['source_start_line'] == op['source_end_line'], 'Unexpected R49 scope')
        line = op['source_start_line'] - 1
        require(line in mapping, 'Changed cumulative authority line')
        current_line = mapping[line]
        old = op['old_text'].encode()
        require(current_lines[current_line].count(old) == 1, 'Ambiguous cumulative preimage')
        start = offsets[current_line] + current_lines[current_line].index(old)
        rebound.append({**op, 'start_byte': start, 'end_byte_exclusive': start + len(old),
                        'cumulative_line': current_line + 1, 'authority_start_byte': op['start_byte']})
    return apply_exact(previous, rebound), rebound


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('check-evidence', 'import', 'compose'))
    args = parser.parse_args()
    files, closure, ops, authority = evidence()
    previous = blob(PREVIOUS, 'derham.tex')
    post, rebound = compose(previous, authority, ops)
    print(json.dumps({'candidate_files': len(files), 'manifest_bound_references': closure, 'operations': len(ops),
                      'authority': identity(authority), 'previous': identity(previous), 'postimage': identity(post)}))
    if args.action == 'check-evidence':
        return
    if args.action == 'import':
        require(git('rev-parse', 'HEAD').decode().strip() == PREVIOUS, 'Import base changed')
        require(not (ROOT / PREFIX).exists(), 'Candidate already materialized; inspect before retry')
        for path in (OVERLAYS, LEASES):
            require((ROOT / path).read_bytes() == blob(PREVIOUS, path), 'Dirty registry file')
        for name, raw in files.items():
            path = ROOT / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
        for path in (OVERLAYS, LEASES):
            (ROOT / path).write_bytes(blob(ADMISSION, path))
        write_json(ROOT / IMPORT_RECEIPT, {'schema': 'stacks-r49-exact-registry-import/v1',
            'previous_public': PREVIOUS, 'admission_commit': ADMISSION, 'manifest_sha256': MANIFEST,
            'candidate_files': [{'path': n, **identity(b)} for n, b in sorted(files.items())],
            'manifest_bound_references': closure, 'historical_registry_prefix_unchanged': True,
            'source_composed': False, 'new_admission_claimed': False})
    else:
        require((ROOT / IMPORT_RECEIPT).is_file(), 'Missing import receipt')
        require((ROOT / 'derham.tex').read_bytes() == previous, 'Dirty or already-composed chapter')
        require((ROOT / OVERLAYS).read_bytes() == blob(ADMISSION, OVERLAYS), 'Registry not imported')
        (ROOT / 'derham.tex').write_bytes(post)
        write_json(ROOT / SOURCE_RECEIPT, {'schema': 'stacks-r49-exact-source-composition/v1',
            'previous_public': PREVIOUS, 'admission_commit': ADMISSION, 'import_commit': git('rev-parse', 'HEAD').decode().strip(),
            'official_authority': AUTHORITY, 'manifest_sha256': MANIFEST,
            'source': 'derham.tex', 'preimage': identity(previous), 'postimage': identity(post),
            'operations': rebound, 'prior_source_additions_preserved': True,
            'whole_isolated_payload_copied': False, 'status': 'PASS_SOURCE_REPLAY_BUILD_PENDING',
            'model': 'OpenAI Codex — GPT-6 Astra, Ultra effort'})


if __name__ == '__main__':
    main()
