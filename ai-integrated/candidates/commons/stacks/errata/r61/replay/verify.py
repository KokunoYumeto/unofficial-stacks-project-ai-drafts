"""Replay R61 in both source contexts and verify its complete retained evidence."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ('derived.tex', 'more-algebra.tex', 'perfect.tex', 'cohomology.tex', 'equiv.tex', 'spaces-perfect.tex')


def identity(raw):
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest().upper())


def load(name):
    return json.loads((ROOT / name).read_bytes())


def transform(raw, operations):
    result, inverses, cursor = bytearray(), [], 0
    for op in sorted(operations, key=lambda x: x['start_byte']):
        start, end = op['start_byte'], op['end_byte_exclusive']
        old, new = op['old_text'].encode(), op['replacement_text'].encode()
        assert cursor <= start < end <= len(raw) and raw[start:end] == old, op['operation_id']
        assert identity(old)['sha256'] == op['old_sha256']
        assert identity(new)['sha256'] == op['replacement_sha256']
        result.extend(raw[cursor:start])
        inverses.append((len(result), len(result) + len(new), old, new))
        result.extend(new)
        cursor = end
    result.extend(raw[cursor:])
    restored = bytes(result)
    for start, end, old, new in reversed(inverses):
        assert restored[start:end] == new
        restored = restored[:start] + old + restored[end:]
    assert restored == raw
    return bytes(result)


def checked_proof(proof):
    name = proof['file']
    if not name.startswith('evidence/'):
        name = 'evidence/review/' + name
    path = (ROOT / name).resolve()
    assert path.is_relative_to(ROOT)
    raw = path.read_bytes()
    assert identity(raw)['sha256'] == proof['sha256'], name
    if 'bytes' in proof:
        assert len(raw) == proof['bytes']
    for number in proof.get('sections', [proof['section']] if 'section' in proof else []):
        assert len(re.findall(r'^##\s+' + re.escape(str(number)) + r'\.\s', raw.decode(), re.M)) == 1
    return name


def all_proofs(value):
    result = set()
    if isinstance(value, dict):
        if 'file' in value and 'sha256' in value and Path(value['file']).name.startswith('PROOFS_'):
            result.add(checked_proof(value))
        for child in value.values():
            result.update(all_proofs(child))
    elif isinstance(value, list):
        for child in value:
            result.update(all_proofs(child))
    return result


def literal_transport(text):
    def escape(fragment):
        result = re.sub(r'\\|_|\*+', lambda m: m[0] if m[0] == '**' else ''.join('\\' + c for c in m[0]), fragment)
        assert re.sub(r'\\([\\_*])', r'\1', result) == fragment
        return result
    cursor, result = 0, []
    for match in re.finditer(r'(?ms)^(`{3,})[^\n]*\n.*?^\1[ \t]*(?:\n|$)|`[^`\n]+`', text):
        result += [escape(text[cursor:match.start()]), match[0]]
        cursor = match.end()
    result.append(escape(text[cursor:]))
    return ''.join(result)


def forbidden_notation_nodes(value):
    if isinstance(value, dict):
        assert value.get('t') not in ('Emph', 'RawInline', 'RawBlock'), value.get('t')
        for child in value.values():
            forbidden_notation_nodes(child)
    elif isinstance(value, list):
        for child in value:
            forbidden_notation_nodes(child)


def verify():
    isolated = load('operation-spec.json')['operations']
    cumulative = load('cumulative-operation-spec.json')['operations']
    units = load('stable-units.json')['units']
    source_map = [json.loads(x) for x in (ROOT / 'source-map.jsonl').read_bytes().splitlines()]
    assert len(units) == 64 and len(isolated) == len(cumulative) == 89
    assert [x['id'] for x in units] == [f'MC-STK-ERR-{n}' for n in range(2506, 2570)]
    assert [x['unit_id'] for x in source_map] == [x['id'] for x in units]
    assert len({x['operation_id'] for x in isolated}) == 89
    assert sorted(x['operation_id'] for x in isolated) == sorted(o for u in units for o in u['operation_ids'])
    canonical = load('evidence/review/prior-canonical-units.json')
    earlier = {op['operation_id']: op for unit in canonical for op in unit['operations']}
    assert len(canonical) == 92 and len(earlier) == 109
    prior_reconciled = load('evidence/review/FINAL_PRIOR_RECONCILIATION.json')
    assert len(prior_reconciled) == 109 and {x['operation_id'] for x in prior_reconciled} == set(earlier)
    rebased = {x['operation_id']: x for x in cumulative}
    assert len(rebased) == 89
    supersessions = []
    for op in isolated:
        other = rebased[op['operation_id']]
        allowed = {'start_byte', 'end_byte_exclusive'}
        if 'supersedes_operation_id' in op:
            assert op['producer_operation_id'] == 'DERIVED-NEW-023-OP2'
            assert op['supersedes_operation_id'] == 'MC-STK-ERR-0839-OP1'
            previous = earlier[op['supersedes_operation_id']]
            assert op['old_text'] == previous['old_text']
            assert other['old_text'] == previous['replacement_text']
            allowed |= {'old_text', 'old_sha256', 'old_bytes'}
            supersessions.append(dict(operation_id=op['operation_id'], predecessor=op['supersedes_operation_id'],
                original_text=op['old_text'], retained_prior_correction=other['old_text'], replacement=op['replacement_text']))
        assert {k: v for k, v in op.items() if k not in allowed} == {k: v for k, v in other.items() if k not in allowed}
    assert len(supersessions) == 1
    for unit, mapping in zip(units, source_map):
        assert mapping['operations'] == [x for x in isolated if x['stable_id'] == unit['id']]
        assert mapping['operation_ids'] == unit['operation_ids']
    proofs = all_proofs(units)
    inventory = load('formula-diagram-inventory.json')
    sources = []
    reference_pattern = r'\\(?:ref|eqref|cite)\{[^}]*\}'
    for source in SOURCES:
        contexts = []
        for context, operations, before, after in (
            ('official-authority', isolated, ROOT / 'authority' / source, ROOT / 'payload' / source),
            ('cumulative', cumulative, ROOT / 'proof-source/prior' / source, ROOT / 'cumulative-preview' / source)):
            old, new = before.read_bytes(), after.read_bytes()
            selected = [x for x in operations if x['source'] == source]
            assert transform(old, selected) == new, (source, context)
            for pattern in (rb'\\label\{[^}]*\}', rb'\\cite(?:\[[^]]*\])?\{[^}]+\}', rb'\\(?:begin|end)\{[^}]+\}'):
                assert re.findall(pattern, old) == re.findall(pattern, new), (source, context, pattern)
            refs = Counter(re.findall(reference_pattern, old.decode()))
            for op in selected:
                refs.subtract(re.findall(reference_pattern, op['old_text']))
                refs.update(re.findall(reference_pattern, op['replacement_text']))
            assert +refs == Counter(re.findall(reference_pattern, new.decode()))
            contexts.append(dict(context=context, preimage=identity(old), postimage=identity(new),
                operations=len(selected), inverse_exact=True, outside_operation_bytes_exact=True))
        expected = [dict(operation_id=x['operation_id'], old=re.findall(reference_pattern, x['old_text']),
            new=re.findall(reference_pattern, x['replacement_text'])) for x in isolated if x['source'] == source and
            re.findall(reference_pattern, x['old_text']) != re.findall(reference_pattern, x['replacement_text'])]
        recorded, = [x for x in inventory['sources'] if x['source'] == source]
        assert expected == recorded['reference_changes']
        assert (ROOT / 'proof-source' / source).read_bytes() == (ROOT / 'cumulative-preview' / source).read_bytes()
        assert (ROOT / 'proof-source/successor' / source).read_bytes() == (ROOT / 'cumulative-preview' / source).read_bytes()
        sources.append(dict(source=source, contexts=contexts, reference_changes=expected))
    evidence = load('evidence-export.json')['files']
    for row in evidence:
        path = (ROOT / row['file']).resolve()
        assert path.is_relative_to(ROOT) and identity(path.read_bytes()) == row['public_evidence'], row['file']
        if row['exact_bytes_retained']:
            assert row['private_intake'] == row['public_evidence']
    reports = load('evidence/review/FINAL_REPORT_DISPOSITIONS.json')
    receivers = load('evidence/review/FINAL_RECEIVER_REPORT_DISPOSITIONS.json')
    assert len(reports) == len({x['occurrence_id'] for x in reports}) == 176
    assert len(receivers) == len({x['occurrence_id'] for x in receivers}) == 6
    assert not {x['occurrence_id'] for x in receivers} & {x['occurrence_id'] for x in reports}
    classes = Counter(x['disposition'] for x in reports)
    assert classes['already_corrected_semantically_reconciled'] == 160 and classes['resolution_metadata_only'] == 1
    assert sum(v for k, v in classes.items() if 'copyedit' in k) == 13
    assert sum(v for k, v in classes.items() if 'mathematical' in k) == 2
    original = [json.loads(x) for x in (ROOT / 'evidence/review/original-reports.jsonl').read_bytes().splitlines()]
    assert len(original) == 176
    for report in reports:
        source = original[report['original_report_line'] - 1]
        assert (source['producer'], source['candidate_id'], source['line']) == (report['producer'], report['producer_id'], report['producer_ledger_line'])
    claims = load('evidence/review/FINAL_CLAIM_PROPAGATION.json')
    assert len(claims['findings']) == 44 and len({x['finding_id'] for x in claims['findings']}) == 44
    assert len(claims['claims']) == 33 and len({x['claim_id'] for x in claims['claims']}) == 33
    refinement, = claims['claim_refinements']
    assert refinement['claim_id'] == 'DERIVED-UNDER-007' and refinement['new_claim_id'] is False
    proofs |= all_proofs([claims, reports, receivers, prior_reconciled])
    assert len(proofs) == 25
    conversion = load('proof-source/PROOF_CONVERSION.json')
    assert len(conversion['documents']) == 25
    order = lambda d: (int(Path(d['source']).stem.split('_')[1]), int(Path(d['source']).stem.split('_')[2]), 'ADDENDUM' in d['source'])
    assert conversion['documents'] == sorted(conversion['documents'], key=order)
    notation = {r['source']: r for r in conversion['literal_notation_fidelity']}
    assert len(notation) == 25
    assembled = (ROOT / 'proof-source/correction-proofs-assembled.tex').read_bytes()
    assert identity(assembled) == conversion['assembled_identity']
    math_count = 0
    layout_adjustments = Counter()
    for doc in conversion['documents']:
        assert identity((ROOT / 'proof-source' / doc['source']).read_bytes()) == doc['source_identity']
        tex = (ROOT / 'proof-source' / doc['tex']).read_bytes()
        assert identity(tex) == doc['tex_identity']
        assert (ROOT / 'evidence/review' / Path(doc['source']).name).read_bytes() == (ROOT / 'proof-source' / doc['source']).read_bytes()
        adjustments = {a['original_text']: a for a in doc.get('math_rendering_adjustments', [])}
        for payload in doc['parsed_payloads']:
            if payload['kind'] == 'Math':
                original = payload['text']
                if original in adjustments:
                    change = adjustments[original]
                    revised = change['rendered_text']
                    if change['kind'] == 'move_equation_tag_outside_aligned':
                        tag = change['retained_tag']
                        assert original.count(tag) == revised.count(tag) == 1
                        assert original.replace(tag, '') == revised.replace(tag, '')
                        assert original.index(tag) < original.index('\\end{aligned}')
                        assert revised.index(tag) > revised.index('\\end{aligned}')
                    else:
                        assert change['kind'] == 'align_comparison_diagram_cells'
                        assert doc['source'] == 'notes-source/PROOFS_4166_5089.md'
                        def tokens(text):
                            text = re.sub(r'\\begin\{array\}\{c+\}', '', text).replace('\\end{array}', '').replace('\\qquad', '').replace('&', '')
                            return re.sub(r'\s+', '', text)
                        assert tokens(original) == tokens(revised)
                        assert original.count('\\downarrow') == revised.count('\\downarrow') == 5
                        assert '\\begin{array}{ccccccccc}' in revised
                    assert revised.encode() in tex and revised.encode() in assembled
                    layout_adjustments[change['kind']] += 1
                else:
                    assert original.encode() in tex and original.encode() in assembled
                    math_count += 1
        assert len(doc['exact_math_marker_replacements']) == doc['tex_math_payloads']
        assert b'R61MATHEMATICALPAYLOAD' not in tex
        proof_source = (ROOT / 'proof-source' / doc['source']).read_text(encoding='utf-8')
        details = notation[doc['source']]
        chunks, cursor = [], 0
        for span in details['math_source_spans']:
            assert cursor <= span['start'] < span['end'] <= len(proof_source)
            assert proof_source[span['start']:span['end']] == span['original']
            chunks += [proof_source[cursor:span['start']], span['marker']]
            cursor = span['end']
        chunks.append(proof_source[cursor:])
        masked = ''.join(chunks)
        restored = masked
        for span in details['math_source_spans']:
            assert restored.count(span['marker']) == 1
            restored = restored.replace(span['marker'], span['original'])
        assert restored == proof_source
        alias = Path(doc['source']).stem
        assert literal_transport(masked).encode() == (ROOT / 'proof-source/notes-source' / (alias + '.render.md')).read_bytes()
        protected_ast = load('proof-source/notes-source/' + alias + '.protected.pandoc.json')
        forbidden_notation_nodes(protected_ast)
    diagram = conversion['literal_diagram_layout']
    diagram_source = (ROOT / 'proof-source' / diagram['source']).read_text(encoding='utf-8')
    assert diagram_source.count(diagram['original_text']) == 1
    assert diagram_source.splitlines()[98:102] == diagram['original_text'].splitlines()
    data = diagram['structure']
    assert data == dict(top_objects=['T', 'T', 'C_T', 'T[1]'], top_arrows=['u_T', 'v_T', 'w_T'],
        bottom_objects=['S', 'S', 'C', 'S[1]'], bottom_arrows=['u', 'v', 'w'],
        vertical_labels=['b', 'a', 'φ', 'b[1]'], vertical_direction='down', final_punctuation='.')
    def horizontal(objects, arrows):
        parts = [objects[0]]
        for arrow, obj in zip(arrows, objects[1:]):
            parts.extend(['\\xrightarrow{' + arrow + '}', obj])
        return '&'.join(parts)
    rendered_diagram = ('\\[\n\\begin{array}{ccccccc}\n' + horizontal(data['top_objects'], data['top_arrows']) + '\\\\\n'
        + '&&'.join('\\scriptstyle ' + label + '\\downarrow' for label in data['vertical_labels']) + '\\\\\n'
        + horizontal(data['bottom_objects'], data['bottom_arrows']) + '.\n\\end{array}\n\\]\n')
    assert rendered_diagram == diagram['rendered_tex']
    assert rendered_diagram.encode() in assembled
    assert rendered_diagram.encode() in (ROOT / 'proof-source/notes/PROOFS_10139_10427.tex').read_bytes()
    return dict(status='PASS_EXACT_SOURCE_AND_INVERSE_REPLAY', units=64, operations=89,
        sources=sources, supersessions=supersessions, retained_evidence_files=len(evidence), proof_files=len(proofs),
        derived_reports=176, separate_receiver_reports=6, report_dispositions=dict(classes),
        prior_units=92, prior_operations=109, editorial_underclaims=33, claim_refinements=1,
        original_labels_citations_environments_exact=True, reference_changes_explicitly_enumerated=True,
        original_tex_math_payloads_exact=math_count, mathematical_layout_adjustments=dict(layout_adjustments),
        literal_notation_source_transports_verified=25,
        restored_literal_diagrams=1,
        proof_order_numeric=True, source_builds_verified=False,
        independence_scope='Executable forward and inverse replay against retained original and cumulative preimages. No second mathematical reviewer is claimed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    receipt = verify()
    if args.output:
        args.output.write_bytes((json.dumps(receipt, indent=2, ensure_ascii=False) + '\n').encode())
    print(json.dumps({k: receipt[k] for k in ('status', 'units', 'operations', 'retained_evidence_files', 'original_tex_math_payloads_exact')}))
