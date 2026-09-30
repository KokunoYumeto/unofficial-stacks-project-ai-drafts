"""Replay all R60 operations and inverses in both retained source contexts."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ('homology.tex', 'more-algebra.tex', 'weil.tex', 'sites-cohomology.tex')


def identity(raw):
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest().upper())


def transform(raw, operations):
    result = bytearray()
    cursor = 0
    inverse = []
    for op in sorted(operations, key=lambda x: x['start_byte']):
        start, end = op['start_byte'], op['end_byte_exclusive']
        old, new = op['old_text'].encode(), op['replacement_text'].encode()
        assert cursor <= start < end <= len(raw) and raw[start:end] == old, op['operation_id']
        assert identity(old)['sha256'] == op['old_sha256']
        assert identity(new)['sha256'] == op['replacement_sha256']
        result.extend(raw[cursor:start])
        inverse.append((len(result), len(result) + len(new), old, new))
        result.extend(new)
        cursor = end
    result.extend(raw[cursor:])
    restored = bytes(result)
    for start, end, old, new in reversed(inverse):
        assert restored[start:end] == new
        restored = restored[:start] + old + restored[end:]
    assert restored == raw
    return bytes(result)


def checked_proof(proof):
    path = (ROOT / proof['file']).resolve()
    assert path.is_relative_to(ROOT)
    raw = path.read_bytes()
    assert identity(raw)['sha256'] == proof['sha256']
    if 'bytes' in proof:
        assert len(raw) == proof['bytes']
    if 'section' in proof:
        assert re.search(r'^## ' + str(proof['section']) + r'\. ', raw.decode(), re.M), proof
    return proof['file']


def verify():
    isolated = json.loads((ROOT / 'operation-spec.json').read_bytes())['operations']
    cumulative = json.loads((ROOT / 'cumulative-operation-spec.json').read_bytes())['operations']
    units = json.loads((ROOT / 'stable-units.json').read_bytes())['units']
    source_map = [json.loads(x) for x in (ROOT / 'source-map.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len(units) == 35 and len(isolated) == len(cumulative) == 43
    assert {x['id'] for x in units} == {f'MC-STK-ERR-{i}' for i in range(2471, 2506)}
    assert {x['id'] for x in units} == {x['unit_id'] for x in source_map}
    assert len({x['operation_id'] for x in isolated}) == 43
    assert {x['operation_id'] for x in isolated} == {x['operation_id'] for x in cumulative}
    assert sorted(x['operation_id'] for x in isolated) == sorted(op for row in units for op in row['operation_ids'])
    for op in isolated:
        other, = [x for x in cumulative if x['operation_id'] == op['operation_id']]
        assert {k: v for k, v in op.items() if k not in ('start_byte', 'end_byte_exclusive')} == {
            k: v for k, v in other.items() if k not in ('start_byte', 'end_byte_exclusive')}
    proofs = set()
    for row in units:
        for proof in [row['proof_evidence'], *row['additional_proof_evidence']]:
            proofs.add(checked_proof(proof))
        mapping, = [x for x in source_map if x['unit_id'] == row['id']]
        assert mapping['operations'] == [x for x in isolated if x['stable_id'] == row['id']]
        assert mapping['operation_ids'] == row['operation_ids']
    sources = []
    inventory = json.loads((ROOT / 'formula-diagram-inventory.json').read_bytes())
    reference_pattern = r'\\(?:ref|eqref|cite)\{[^}]*\}'
    for source in SOURCES:
        contexts = []
        for context, operations, before, after in (
            ('official-authority', isolated, ROOT / 'authority' / source, ROOT / 'payload' / source),
            ('cumulative', cumulative, ROOT / 'proof-source/prior' / source, ROOT / 'cumulative-preview' / source)):
            old, new = before.read_bytes(), after.read_bytes()
            selected = [x for x in operations if x['source'] == source]
            assert transform(old, selected) == new, (source, context)
            assert re.findall(rb'\\label\{[^}]*\}', old) == re.findall(rb'\\label\{[^}]*\}', new)
            contexts.append(dict(context=context, preimage=identity(old), postimage=identity(new),
                                 operations=len(selected), inverse_exact=True, outside_operation_bytes_exact=True))
        expected = [dict(operation_id=x['operation_id'], old=re.findall(reference_pattern, x['old_text']),
                         new=re.findall(reference_pattern, x['replacement_text']))
                    for x in isolated if x['source'] == source and
                    re.findall(reference_pattern, x['old_text']) != re.findall(reference_pattern, x['replacement_text'])]
        recorded, = [x for x in inventory['sources'] if x['source'] == source]
        assert expected == recorded['reference_changes']
        assert (ROOT / 'proof-source' / source).read_bytes() == (ROOT / 'cumulative-preview' / source).read_bytes()
        assert (ROOT / 'proof-source/successor' / source).read_bytes() == (ROOT / 'cumulative-preview' / source).read_bytes()
        sources.append(dict(source=source, contexts=contexts, reference_changes=expected))
    evidence = json.loads((ROOT / 'evidence-export.json').read_bytes())['files']
    for row in evidence:
        path = (ROOT / row['file']).resolve()
        assert path.is_relative_to(ROOT)
        assert identity(path.read_bytes()) == row['public_evidence'], row['file']
        if row['exact_bytes_retained']:
            assert row['private_intake'] == row['public_evidence']
    reports = json.loads((ROOT / 'evidence/review/FINAL_REPORT_DISPOSITIONS.json').read_bytes())
    assert len(reports) == len({x['occurrence_id'] for x in reports}) == 136
    classes = Counter(x['disposition'] for x in reports)
    assert classes['optional_not_integrated'] == 7
    amendment, = json.loads((ROOT / 'presentation-amendment.json').read_bytes())['amendments']
    assert amendment['candidate_replacement'].replace('\\textbf{Editorial proof completion.}\n', '', 1) == amendment['intake_replacement']
    editorial, = [x for x in units if x['class'] == 'editorial_proof_completion']
    op, = [x for x in isolated if x['stable_id'] == editorial['id']]
    assert op['replacement_text'] == amendment['candidate_replacement']
    conversion = json.loads((ROOT / 'proof-source/PROOF_CONVERSION.json').read_bytes())
    assembled = (ROOT / 'proof-source/correction-proofs-assembled.tex').read_bytes()
    math_count = 0
    for document in conversion['documents']:
        assert identity((ROOT / 'proof-source' / document['source']).read_bytes()) == document['source_identity']
        for payload in document['parsed_payloads']:
            if payload['kind'] == 'Math':
                assert payload['text'].encode() in assembled
                math_count += 1
    assert math_count == 1769
    return dict(status='PASS_EXACT_SOURCE_AND_INVERSE_REPLAY', units=35, operations=43,
                sources=sources, retained_evidence_files=len(evidence), proof_files=len(proofs),
                report_dispositions=dict(classes), original_labels_exact=True,
                reference_changes_explicitly_enumerated=True, editorial_completion_visible=True,
                original_tex_math_payloads_exact=math_count,
                independence_scope='Executable forward and inverse replay against retained original and cumulative preimages. No second mathematical reviewer is claimed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    receipt = verify()
    if args.output:
        args.output.write_bytes((json.dumps(receipt, indent=2, ensure_ascii=False) + '\n').encode())
    print(json.dumps({k: receipt[k] for k in ('status', 'units', 'operations', 'retained_evidence_files', 'original_tex_math_payloads_exact')}))
