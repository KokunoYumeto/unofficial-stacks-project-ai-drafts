"""Replay R59 in both retained source contexts, including exact inverse maps."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


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
        inverse.append((len(result), len(result)+len(new), old, new))
        result.extend(new)
        cursor = end
    result.extend(raw[cursor:])
    restored = bytes(result)
    for start, end, old, new in reversed(inverse):
        assert restored[start:end] == new
        restored = restored[:start]+old+restored[end:]
    assert restored == raw
    return bytes(result)


def verify():
    isolated = json.loads((ROOT/'operation-spec.json').read_bytes())['operations']
    cumulative = json.loads((ROOT/'cumulative-operation-spec.json').read_bytes())['operations']
    units = json.loads((ROOT/'stable-units.json').read_bytes())['units']
    source_map = [json.loads(x) for x in (ROOT/'source-map.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len(units) == 5 and len(isolated) == len(cumulative) == 13
    assert {x['id'] for x in units} == {x['unit_id'] for x in source_map}
    assert {x['operation_id'] for x in isolated} == {x['operation_id'] for x in cumulative}
    assert sorted(x['operation_id'] for x in isolated) == sorted(op for row in units for op in row['operation_ids'])
    for row in units:
        evidence = row['proof_evidence']
        raw = (ROOT/evidence['file']).read_bytes()
        assert identity(raw)['sha256'] == evidence['sha256']
        lines = raw.splitlines()
        assert evidence['locators']
        for locus in evidence['locators']:
            assert 1 <= locus['start_line'] <= locus['end_line'] <= len(lines)
    sources = []
    for source in ('examples.tex','more-algebra.tex','brauer.tex'):
        contexts = []
        for context, operations, before, after in (
            ('official-authority',isolated,ROOT/'authority'/source,ROOT/'payload'/source),
            ('cumulative',cumulative,ROOT/'proof-source/prior'/source,ROOT/'cumulative-preview'/source)):
            old, new = before.read_bytes(), after.read_bytes()
            selected = [x for x in operations if x['source'] == source]
            assert transform(old, selected) == new, (source,context)
            for pattern in (rb'\\label\{[^}]+\}', rb'\\(?:[a-zA-Z]*ref|cite)\*?(?:\[[^]]*\])?\{[^}]+\}',rb'\\(?:begin|end)\{[^}]+\}'):
                assert re.findall(pattern,old) == re.findall(pattern,new), (source,context,pattern)
            contexts.append(dict(context=context,preimage=identity(old),postimage=identity(new),operations=len(selected),inverse_exact=True))
        assert (ROOT/'proof-source'/source).read_bytes() == (ROOT/'cumulative-preview'/source).read_bytes()
        assert (ROOT/'proof-source/successor'/source).read_bytes() == (ROOT/'cumulative-preview'/source).read_bytes()
        sources.append(dict(source=source,contexts=contexts))
    evidence_count = 0
    for group in ('cross-chapter','brauer'):
        batch = json.loads((ROOT/'evidence'/group/'BATCH.json').read_bytes())
        for row in batch['files']:
            path = (ROOT/'evidence'/group/row['file']).resolve()
            assert path.is_relative_to((ROOT/'evidence'/group).resolve())
            assert identity(path.read_bytes()) == {k:row[k] for k in ('bytes','sha256')}, row['file']
            evidence_count += 1
    return dict(status='PASS_EXACT_SOURCE_AND_INVERSE_REPLAY',units=5,operations=13,
        sources=sources,retained_batch_files=evidence_count,
        labels_references_citations_environments_unchanged=True,
        complete_proof_locators_verified=True,
        independence_scope='Executable byte replay from retained original and cumulative preimages; no second mathematical reviewer is claimed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    receipt = verify()
    if args.output:
        args.output.write_bytes((json.dumps(receipt,indent=2)+'\n').encode())
    print(json.dumps({k:receipt[k] for k in ('status','units','operations','retained_batch_files')}))
