"""Read-only R49 provenance audit. Emits JSON; launches no child or TeX process."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timedelta
import copy
import hashlib
import json
import os
import re

BATCH = Path(__file__).resolve().parent.parent
ROOT = Path('USERROOT/Documents/interlanguage/worktrees/stacks-errata-r48-20260910/ai-integrated/candidates/commons/stacks/errata/r49')
checks = []
bindings = {}
cache = {}

def digest(data):
    return hashlib.sha256(data).hexdigest().upper()

def read(path):
    return path.read_bytes()

def load(path):
    return json.loads(read(path))

def identity(path):
    data = read(path)
    return dict(bytes=len(data), sha256=digest(data))

def cached_identity(path):
    key = str(path.resolve()).lower()
    if key not in cache:
        cache[key] = identity(path)
    return cache[key]

def bind(path):
    label = ('candidate/' + path.relative_to(ROOT).as_posix()) if path.is_relative_to(ROOT) else ('batch/' + path.relative_to(BATCH).as_posix())
    bindings[label] = identity(path)
    return bindings[label]

def test(name, condition, details=None):
    checks.append(dict(name=name, passed=bool(condition), **({} if details is None else dict(details=details))))

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')

def published_json(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')

def sanitize(raw):
    text = raw.decode('utf-8', errors='replace')
    profile = os.environ['USERPROFILE']
    atoms = [r'(?:\\|/)' if c in '\\/' else re.escape(c) for c in profile]
    pattern = r'(?:\r?\n)?'.join(atoms)
    text = re.sub(pattern, '<USER_ROOT>', text, flags=re.I)
    text = re.sub(r'C:(?:\\|/)Users(?:\\|/)[^\\/\r\n]+', '<USER_ROOT>', text, flags=re.I)
    text = re.sub(r'C:(?:\\|/)Users(?:\\|/)', '<USERS_ROOT>/', text)
    return text.encode('utf-8')

config = load(ROOT / 'candidate.config.json')
execution = load(ROOT / 'builds/build-execution.json')
receipt = load(ROOT / 'builds/build-receipt.json')
mutex = load(ROOT / 'builds/TEX_MUTEX_RECEIPT.json')
replay = load(ROOT / 'builds/deterministic-replay.json')
privates = {key: load(BATCH / f'private_build_{key}/private-build-execution.json') for key in ('a', 'b')}
for filename in ('candidate.config.json', 'candidate.config.input.json', 'operation-spec.json', 'source-map.jsonl', 'stable-units.json', 'unresolved-findings.json', 'BUILD.md', 'replay-build.py', 'build-receipt.py', 'deterministic-replay.py', 'CapturedR49Tree20260913.cs', 'run-builds-with-mutex.ps1', 'payload/derham.tex', 'authority/source/derham.tex', 'builds/build-execution.json', 'builds/build-receipt.json', 'builds/deterministic-replay.json', 'builds/TEX_MUTEX_RECEIPT.json'):
    bind(ROOT / filename)
test('candidate identity and declared scope', config['candidate_id'] == 'stacks-errata-a04446e-r49' and config['accepted'] == 5 and config['operation_count'] == 7 and 'P07-ERR-0003' not in config['expected_producer_ids'])
test('config input byte equality', read(ROOT / 'candidate.config.json') == read(ROOT / 'candidate.config.input.json'))
test('build execution binds pinned authority identity', execution['authority_commit'] == config['authority_commit'] and execution['authority_tree'] == config['authority_tree'] and execution['passed'])
test('B private receipt binds current public execution', identity(ROOT / 'builds/build-execution.json') == {k: privates['b']['public_execution'][k] for k in ('bytes', 'sha256')})

sources = {}
spec = load(ROOT / 'operation-spec.json')
for phase, subdir, hashkey in [('candidate', 'payload', 'payload_sha256'), ('authority', 'authority/source', 'authority_sha256')]:
    path = ROOT / subdir / 'derham.tex'
    sources[phase] = identity(path)
    test(f'{phase} live source config binding', sources[phase]['sha256'] == config['stems']['derham'][hashkey])
    test(f'{phase} source execution binding', {k: execution[phase + '_phase']['stems']['derham']['source'][k] for k in ('bytes', 'sha256')} == sources[phase])
authority = read(ROOT / 'authority/source/derham.tex')
composed = authority
ops = sorted(spec['operations'], key=lambda row: row['start_byte'])
test('seven disjoint source operations', len(ops) == 7 and all(a['end_byte_exclusive'] <= b['start_byte'] for a, b in zip(ops, ops[1:])))
for op in reversed(ops):
    old, new = op['old_text'].encode(), op['replacement_text'].encode()
    test('operation preimage and replacement binding ' + op['operation_id'], authority[op['start_byte']:op['end_byte_exclusive']] == old and digest(old) == op['old_sha256'] and digest(new) == op['replacement_sha256'])
    composed = composed[:op['start_byte']] + new + composed[op['end_byte_exclusive']:]
test('seven operations exactly reconstruct payload', composed == read(ROOT / 'payload/derham.tex'))

guard = BATCH / 'build_guard_01'
test('exact mutex and guard binding', mutex['mutex_name'] == 'Global\\InterlanguageTeXSlotV1' and mutex['captured_tree_guard']['sha256'] == identity(ROOT / 'CapturedR49Tree20260913.cs')['sha256'] and mutex['captured_tree_guard']['breakaway_allowed'] is False)
test('mutex acquired and released without failure', mutex['acquired'] and mutex['released'] and mutex['passed'] and mutex['failure'] is None and mutex['wait_timeout_seconds'] == 60)
expected_roles = ['fresh_candidate_authority_build_1', 'fresh_candidate_authority_build_2', 'deterministic_pdf_comparison', 'immediate_log_and_build_preflight']
test('all expected captured jobs', [r['role'] for r in mutex['guarded_commands']] == expected_roles)
previous_end = mutex['acquired_at_utc']
for row in mutex['guarded_commands']:
    test('captured successful job ' + row['role'], row['exit_code'] == 0 and row['assigned_before_resume'] and row['cleanup_completed'] and row['captured_total_processes'] >= 1 and not row['termination_requested'] and row['failure'] is None)
    test('serial mutex-contained interval ' + row['role'], previous_end <= row['started_at_utc'] <= row['completed_at_utc'] <= mutex['released_at_utc'])
    previous_end = row['completed_at_utc']
    for stream in ('stdout', 'stderr'):
        data = bind(guard / row[stream]['private_filename'])
        test('guard stream binding ' + row['role'] + '/' + stream, data == {k: row[stream][k] for k in ('bytes', 'sha256')})
post = load(guard / 'POST_RELEASE_BINDING.json')
bind(guard / 'POST_RELEASE_BINDING.json')
test('post-release no-TeX receipt binding captured successfully', post['started_at_utc'] >= mutex['released_at_utc'] and post['exit_code'] == 0 and post['cleanup_completed'] and post['assigned_before_resume'] and not post['termination_requested'])
for stream in ('stdout', 'stderr'):
    data = bind(guard / post[stream]['private_filename'])
    test('post-release stream binding ' + stream, data == {k: post[stream][k] for k in ('bytes', 'sha256')})
test('post-release stdout binds final build receipt', load(guard / post['stdout']['private_filename'])['sha256'] == identity(ROOT / 'builds/build-receipt.json')['sha256'])
test('build receipt binds final mutex bytes', {k: receipt['tex_mutex'][k] for k in ('bytes', 'sha256')} == identity(ROOT / 'builds/TEX_MUTEX_RECEIPT.json'))

pdfs = {}
fls_results = []
inventories = {}
raw_output_hashes = {}
reconstructed_a = copy.deepcopy(execution)
for run in ('a', 'b'):
    private = BATCH / f'private_build_{run}'
    bind(private / 'private-build-execution.json')
    record = privates[run]
    work = Path(record['work_root'])
    upstream = Path(record['upstream_root'])
    test('removed isolated workroot ' + run, not work.exists() and work.name == f'stacks-r49-derham-20260913-build-{run}' and work.parent == Path(os.environ['TEMP']).resolve())
    test('retained candidate source ' + run, identity(private / 'derham.tex') == sources['candidate'])
    for phase, suffix in [('candidate', ''), ('authority', '.authority')]:
        prefix = f'derham.{phase}'
        private_rows = record[phase + '_phase']['stems']['derham']
        public_rows = execution[phase + '_phase']['stems']['derham']
        for kind, row in private_rows.items():
            actual = bind(private / row['path'])
            test('private raw binding ' + run + '/' + phase + '/' + kind, actual == {k: row[k] for k in ('bytes', 'sha256')})
        pdfs[run + '/' + phase] = identity(private / (prefix + '.pdf'))
        public_pdf = ROOT / f'builds/derham{suffix}.pdf'
        test('PDF raw/public equality ' + run + '/' + phase, read(public_pdf) == read(private / (prefix + '.pdf')))
        bind(public_pdf)
        for role in ('pdflatex_pass_1', 'bibtex', 'pdflatex_pass_2', 'pdflatex_pass_3'):
            path = private / f'{prefix}.{role}.stdout.txt'
            actual = bind(path)
            raw_output_hashes[run + '/' + phase + '/' + role] = actual
            command = next(c for c in public_rows['commands'] if c['role'] == role)
            if run == 'b':
                test('B explicit command exit and stdout binding ' + phase + '/' + role, command['exit_code'] == 0 and actual == dict(bytes=command['stdout_bytes'], sha256=command['stdout_sha256_raw']))
            else:
                rc = next(c for c in reconstructed_a[phase + '_phase']['stems']['derham']['commands'] if c['role'] == role)
                rc['stdout_bytes'], rc['stdout_sha256_raw'] = actual['bytes'], actual['sha256']
        for kind, public_extension, private_extension in [('log', '.log', '.log'), ('fls', '.fls', '.fls'), ('pass3_stdout', '.pass3.txt', '.pass3_stdout.txt'), ('bibtex_stdout', '.bibtex.txt', '.bibtex_stdout.txt')]:
            sanitized = sanitize(read(private / (prefix + private_extension)))
            public_path = ROOT / f'builds/derham{suffix}{public_extension}'
            if run == 'b':
                test('B raw-to-public exact sanitization ' + phase + '/' + kind, sanitized == read(public_path))
                bind(public_path)
            else:
                reconstructed_a[phase + '_phase']['stems']['derham']['outputs'][kind].update(bytes=len(sanitized), sha256=digest(sanitized))
        if run == 'a':
            reconstructed_a[phase + '_phase']['stems']['derham']['outputs']['fls_dependencies'].update(identity(private / (prefix + '.fls-dependencies.json')))
        invpath = private / (prefix + '.fls-dependencies.json')
        inv = load(invpath)
        inventories[run + '/' + phase] = inv
        fls_path = private / (prefix + '.fls')
        test('raw FLS hash binding ' + run + '/' + phase, identity(fls_path) == dict(bytes=inv['raw_fls_bytes'], sha256=inv['raw_fls_sha256']))
        paths = {'INPUT': [], 'OUTPUT': []}
        actual_paths = {}
        pwd = None
        for line in read(fls_path).decode().splitlines():
            kind, sep, value = line.partition(' ')
            if kind == 'PWD':
                pwd = Path(value)
            if not sep or kind not in paths:
                continue
            path = Path(value)
            resolved = (path if path.is_absolute() else work / path).resolve()
            logical = ('worktree/' + resolved.relative_to(work).as_posix()) if resolved.is_relative_to(work) else sanitize(str(resolved).encode()).decode()
            if logical not in paths[kind]:
                paths[kind].append(logical)
                actual_paths[logical] = resolved
        test('raw FLS PWD and full ordered inventory ' + run + '/' + phase, pwd == work and paths['INPUT'] == [r['logical_path'] for r in inv['inputs']] and paths['OUTPUT'] == [r['logical_path'] for r in inv['outputs']])
        test('all FLS outputs confined ' + run + '/' + phase, all(p.startswith('worktree/') for p in paths['OUTPUT']))
        closure = digest(canonical([{k: r[k] for k in ('logical_path', 'bytes', 'sha256')} for r in inv['inputs']]))
        test('independently recomputed input closure ' + run + '/' + phase, closure == inv['input_closure_sha256'] and len(paths['INPUT']) == inv['input_count'] and len(paths['OUTPUT']) == inv['output_count'])
        available, unavailable, changed = [], [], []
        for row in inv['inputs']:
            logical = row['logical_path']
            if logical == 'worktree/derham.tex':
                resolved = ROOT / ('payload' if phase == 'candidate' else 'authority/source') / 'derham.tex'
            elif logical.startswith('worktree/'):
                resolved = upstream / logical.removeprefix('worktree/')
            else:
                resolved = actual_paths[logical]
            if resolved.is_file():
                available.append(logical)
                if cached_identity(resolved) != {k: row[k] for k in ('bytes', 'sha256')}:
                    changed.append(logical)
            else:
                unavailable.append(logical)
        test('available retained input bytes match final inventory ' + run + '/' + phase, not changed, dict(available=len(available), changed=changed))
        if run == 'b':
            public_inv = ROOT / f'builds/derham{suffix}.fls-dependencies.json'
            bind(public_inv)
            test('B public/private inventory byte equality ' + phase, read(public_inv) == read(invpath))
        fls_results.append(dict(run=run, phase=phase, input_count=inv['input_count'], output_count=inv['output_count'], recomputed_closure_sha256=closure, input_bytes_independently_rehashed=len(available), unavailable_input_bytes=unavailable, input_hash_mismatches=changed))

reconstructed_a['completed_at_utc'] = privates['a']['completed_at_utc']
start = datetime.fromisoformat(mutex['guarded_commands'][0]['started_at_utc'].replace('Z', '+00:00')).replace(microsecond=0)
stop = datetime.fromisoformat(privates['a']['completed_at_utc'].replace('Z', '+00:00'))
recovered = []
while start <= stop:
    reconstructed_a['started_at_utc'] = start.isoformat().replace('+00:00', 'Z')
    data = published_json(reconstructed_a)
    if dict(bytes=len(data), sha256=digest(data)) == {k: privates['a']['public_execution'][k] for k in ('bytes', 'sha256')}:
        recovered.append(copy.deepcopy(reconstructed_a))
    start += timedelta(seconds=1)
test('A exact original public execution recoverable from hash-bound raw evidence', len(recovered) == 1)
if recovered:
    test('A recovered receipt records all eight command exits zero', all(c['exit_code'] == 0 for phase in ('candidate', 'authority') for c in recovered[0][phase + '_phase']['stems']['derham']['commands']))
for phase in ('candidate', 'authority'):
    first, second = inventories['a/' + phase], inventories['b/' + phase]
    test('A/B actual PDF equality ' + phase, pdfs['a/' + phase] == pdfs['b/' + phase])
    test('A/B complete input row equality ' + phase, first['inputs'] == second['inputs'])
    test('A/B complete output row equality ' + phase, first['outputs'] == second['outputs'])
    r = next(row for row in replay['pdfs'] if row['phase'] == phase)
    test('deterministic receipt agrees with actual PDF and recomputed closure ' + phase, r['first_sha256'] == pdfs['a/' + phase]['sha256'] == r['second_sha256'] and r['first_bytes'] == pdfs['a/' + phase]['bytes'] == r['second_bytes'] and r['fls_input_closure_sha256'] == second['input_closure_sha256'])

def warnings(path):
    text = read(path).decode('utf-8')
    reference, citation = Counter(), Counter()
    for block in text.split('LaTeX Warning:')[1:]:
        compact = re.sub(r'\s+', '', block.split('\n\n', 1)[0])
        for category, collection in [('(?:Hyperreference|Reference)', reference), ('Citation', citation)]:
            match = re.search(category + r"`([^']+)'onpage\d+undefinedoninputline\d+\.", compact)
            if match:
                collection[match[1]] += 1
    flat = re.sub(r'\s+', ' ', text)
    output = re.search(r'Output written on .*?\((\d+) pages?, (\d+) bytes\)\.', flat)
    result = dict(pages=int(output[1]), reported_pdf_bytes=int(output[2]), undefined_reference_targets=dict(sorted(reference.items())), undefined_citation_targets=dict(sorted(citation.items())))
    for box in ('hbox', 'vbox'):
        for fullness in ('Overfull', 'Underfull'):
            result[fullness.lower() + '_' + box + 'es'] = text.count(fullness + ' \\' + box)
    result['fatal_markers'] = len(re.findall(r'(?m)^! (?:Emergency stop\.|Undefined control sequence\.|LaTeX Error:|Package [^\r\n]+ Error:)|^!  ==> Fatal error occurred|^Emergency stop\.|Fatal error occurred', text))
    result['missing_glyph_markers'] = text.count('Missing character:')
    return result

warning_results = {}
for run in ('a', 'b'):
    for phase in ('candidate', 'authority'):
        summary = warnings(BATCH / f'private_build_{run}/derham.{phase}.log')
        warning_results[run + '/' + phase] = summary
        test('raw log agrees with public warning receipt ' + run + '/' + phase, summary == receipt['chapters'][0][phase + '_log_summary'])
        test('raw log successful PDF byte record ' + run + '/' + phase, summary['reported_pdf_bytes'] == pdfs[run + '/' + phase]['bytes'] and summary['fatal_markers'] == summary['missing_glyph_markers'] == 0)
candidate_warning, authority_warning = warning_results['b/candidate'], warning_results['b/authority']
warning_delta = {key: candidate_warning[key] - authority_warning[key] for key in candidate_warning if isinstance(candidate_warning[key], int) and key != 'reported_pdf_bytes'}
test('candidate/authority reference and citation multisets equal', candidate_warning['undefined_reference_targets'] == authority_warning['undefined_reference_targets'] and candidate_warning['undefined_citation_targets'] == authority_warning['undefined_citation_targets'])
test('all page and warning-count deltas zero', all(value == 0 for value in warning_delta.values()))
for phase in ('candidate', 'authority'):
    for key, row in execution[phase + '_phase']['stems']['derham']['outputs'].items():
        test('public output receipt binding ' + phase + '/' + key, identity(ROOT / row['path']) == {k: row[k] for k in ('bytes', 'sha256')})

report = dict(schema='r49-independent-build-provenance-review/v1', candidate_id=config['candidate_id'], passed=all(row['passed'] for row in checks), writes_to_candidate=False, tex_processes_launched=0, visual_review_performed=False, admission_performed=False, review_scope='five prior deRham units, seven operations; final-pass recorder and two fresh executions', checks=checks, sources=sources, actual_pdfs=pdfs, fls_checks=fls_results, mutex_summary={key: mutex[key] for key in ('mutex_name', 'acquired_at_utc', 'released_at_utc', 'abandoned_mutex_recovered', 'command_timeout_seconds')}, captured_jobs=[{key: r[key] for key in ('role', 'exit_code', 'captured_total_processes', 'cleanup_completed')} for r in mutex['guarded_commands']], warnings=dict(candidate_pages=candidate_warning['pages'], reference_occurrences=sum(candidate_warning['undefined_reference_targets'].values()), reference_distinct_targets=len(candidate_warning['undefined_reference_targets']), citation_occurrences=sum(candidate_warning['undefined_citation_targets'].values()), candidate_authority_count_deltas=warning_delta, reference_multiset_sha256=digest(canonical(candidate_warning['undefined_reference_targets'])), citation_multiset_sha256=digest(canonical(candidate_warning['undefined_citation_targets']))), first_execution_recovery=dict(recovered=len(recovered) == 1, expected=privates['a']['public_execution'], method='Reconstructed first execution using first raw hashes, sanitizer, retained first completion time and bounded whole-second start timestamps; unique exact SHA-256 preimage match.'), bindings=bindings, limitations=['FLS records only the final TeX pass of each phase in each execution. No complete earlier-pass or BibTeX dependency closure is claimed.', 'Deleted temporary workroots prevent independent rehashing of generated inputs listed as unavailable_input_bytes. Their retained inventory hashes and A/B equality remain available.', 'The first public execution file was overwritten by the second run. A deterministic reconstruction is accepted only when it exactly matches the originally retained first receipt SHA-256 and byte count.', 'Mutex coverage is supported by inspected wrapper and captured-tree implementation plus hash-bound execution receipts; this is not an independent kernel event trace or a new fault-injection test.', 'MiKTeX binary executables and every earlier read are not cryptographically pinned by the reviewed recorder closure; this audit checks retained final-pass inputs and reported tool versions.', 'Warning equivalence is relative to standalone pinned authority; unresolved cross-chapter references remain. It is not a zero-warning or cumulative-book-build claim.', 'No visual, mathematical admission, registry, publication, or new P07-ERR-0003 operation decision is made by this review.'])
print(json.dumps(dict(report=report, reconstructed_first_execution=recovered[0] if recovered else None), ensure_ascii=False, indent=2, sort_keys=True))
