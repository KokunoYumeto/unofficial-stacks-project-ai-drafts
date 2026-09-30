"""Repair the exact editorial-note conversion while retaining original authoring bytes."""
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

C = Path(__file__).resolve().parent
S = C / 'ALGEBRA_CONTEXTUAL_COMPANION_20260929'
H = 'revision-history/before-indetale-literal-repair'
NOTE = 'ALGEBRA_INDETALE_NOTES_20260929'
sha = lambda b: hashlib.sha256(b).hexdigest().upper()
dump = lambda x: (json.dumps(x, ensure_ascii=False, indent=2) + '\n').encode()

def walk(n, kind):
    if isinstance(n, dict):
        if n.get('t') == kind:
            yield n
        for v in n.values():
            yield from walk(v, kind)
    elif isinstance(n, list):
        for v in n:
            yield from walk(v, kind)

def main():
    assert not (S / H).exists()
    old_manifest = (S / 'MANIFEST.json').read_bytes()
    assert sha(old_manifest) == '0ED5DE14F6D7D27462549348BE3EBE5F64D367295FA87AB2B469FB089BF87937'
    manifest = json.loads(old_manifest)
    for r in manifest['files']:
        assert sha((S / r['file']).read_bytes()) == r['sha256'], r['file']
    raw = (S / ('notes-source/' + NOTE + '.md')).read_bytes()
    assert raw == (C / (NOTE + '.md')).read_bytes()
    assert sha(raw) == 'D870DDC69060B200A884A20FCFC69F6ED295A1DFBE27B2E2E34C74DBE7B59A7E'
    old_tex = (S / ('notes/' + NOTE + '.tex')).read_bytes()
    broken = b'{' + bytes([13]) + b'm finite}'
    repaired = br'{\rm finite}'
    assert raw.count(broken) == 2 and raw.count(repaired) == 0
    corrected = raw.replace(broken, repaired)
    assert corrected.replace(repaired, broken) == raw
    parts = re.split(r'(\\\[.*?\\\])', corrected.decode(), flags=re.S)
    assert len(parts) == 31
    assert all(r'\_' not in p for i, p in enumerate(parts) if i % 2 == 0)
    prepared_parts = [p if i % 2 else p.replace('_', r'\_') for i, p in enumerate(parts)]
    restored_parts = [p if i % 2 else p.replace(r'\_', '_') for i, p in enumerate(prepared_parts)]
    assert restored_parts == parts
    input_bytes = ''.join(prepared_parts).encode()
    reader = 'markdown+tex_math_single_backslash+tex_math_double_backslash+raw_tex-smart-superscript-subscript'
    common = [shutil.which('pandoc'), '--from=' + reader]
    tree = json.loads(subprocess.check_output(common + ['--to=json'], input=input_bytes))
    for kind in ['Emph', 'Strong', 'Superscript', 'Subscript']:
        assert not list(walk(tree, kind)), kind
    payloads = [n['c'][1] for n in walk(tree, 'Math')]
    assert len(payloads) == 15
    assert [p[2:-2] for p in parts[1::2]] == payloads
    tex = subprocess.check_output(common + ['--to=latex', '--wrap=none', '--eol=lf',
                                  '--syntax-highlighting=none', '--shift-heading-level-by=1'], input=input_bytes).decode()
    labels = re.findall(r'\\label\{([^}]+)\}', tex)
    tex = re.sub(r'\\label\{([^}]+)\}', lambda m: r'\label{algebra-proof-059-' + m[1] + '}', tex)
    assert re.findall(rb'\\label\{([^}]+)\}', old_tex) == re.findall(rb'\\label\{([^}]+)\}', tex.encode())
    for payload in payloads:
        assert payload in tex
    assert r'\emph{' not in tex and r'\textsuperscript{' not in tex
    assert tex.count(r'\textquotesingle\textquotesingle') == 2
    assert r'T/Q\^{}(a+1)→T/Q\^{}a' in tex
    assert r'd\_F=∏\_(h∈F)d\_h, with d\_∅=1' in tex
    assert r'D=E⊗\_R E' in tex and r'Ω\_(E/R)=0' in tex
    assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\r]', tex)
    # The only changed mathematical display is the explicitly identified roman finite label.
    old_displays = re.findall(r'\\\[(.*?)\\\]', old_tex.decode(), re.S)
    new_displays = re.findall(r'\\\[(.*?)\\\]', tex, re.S)
    assert len(old_displays) == len(new_displays) == 15
    changed_displays = [(a, b) for a, b in zip(old_displays, new_displays) if a != b]
    assert len(changed_displays) == 1
    a, b = changed_displays[0]
    assert a.count('{m finite}') == 2 and a.replace('{m finite}', r'{\rm finite}') == b
    audit_raw = (C / 'ALGEBRA_MARKDOWN_PARSE_AUDIT_20260930.json').read_bytes()
    audit = json.loads(audit_raw)
    assert audit['notes_audited'] == 73
    receipt = dict(id='RENDER-TEX-007', recorded_at_utc=datetime.now(timezone.utc).isoformat(),
        original_source_sha256=sha(raw), previous_tex_sha256=sha(old_tex), repaired_tex_sha256=sha(tex.encode()),
        original_source_preserved=True, source_chapter_changed=False, source_routing_changed=False,
        reader=reader, derived_input='conversion-input/' + NOTE + '.md',
        literal_underscore_inserted_escapes=sum(p.count('_') for p in parts[::2]),
        inserted_escape_inverse_exact=True, source_typo_inverse_exact=True,
        literal_prime_sequences_retained=True, literal_caret_exponents_retained=True,
        raw_source_math_displays=15, unchanged_typeset_math_displays=14,
        declared_display_repair=dict(original_control_byte=13, occurrences=2,
          original_bytes_hex=broken.hex(), replacement_bytes_hex=repaired.hex(),
          reason='The finite-subset colimit index has a damaged roman-font command; the preceding paragraph explicitly defines F to be finite. No indexing set, factor, map, or hypothesis changes.'),
        exact_labels_preserved=len(labels), all_73_note_parser_spans_audited=True,
        audit_file='MARKDOWN_PARSE_AUDIT.json',
        remaining_emphasis='Only intentional source emphasis and titles in the other notes; their TeX is unchanged.',
        double_prime_audit='All 73 notes parsed with smart punctuation disabled: the only double-ASCII-prime prose tokens are the two repaired in this note.',
        build_verified=False, visual_acceptance=False)
    ledger_path = S / 'TYPESETTING_CORRECTIONS.json'
    old_ledger = ledger_path.read_bytes()
    ledger = json.loads(old_ledger)
    ledger['literal_markdown_repair'] = receipt
    files = {H + '/MANIFEST.json': old_manifest,
             H + '/TYPESETTING_CORRECTIONS.json': old_ledger,
             H + '/' + NOTE + '.tex': old_tex,
             'notes/' + NOTE + '.tex': tex.encode(),
             'conversion-input/' + NOTE + '.md': input_bytes,
             'MARKDOWN_PARSE_AUDIT.json': audit_raw,
             'INDETALE_CONVERSION_REPAIR.json': dump(receipt),
             'TYPESETTING_CORRECTIONS.json': dump(ledger),
             'reproducers/' + Path(__file__).name: Path(__file__).read_bytes()}
    for row in manifest['proof_notes']:
        if row['source'] == NOTE + '.md':
            row['before_literal_repair_tex_sha256'] = row['tex_sha256']
            row['tex_sha256'] = sha(tex.encode())
            row['literal_conversion_repair'] = 'INDETALE_CONVERSION_REPAIR.json'
            row['namespace_inverse_recovers_exact_initial_tex'] = False
            row['namespace_inverse_note'] = 'The historical initial conversion is preserved; the current TeX also includes the recorded literal and roman-label repairs.'
            row['exact_math_payloads_preserved'] = False
            row['math_payload_status'] = '14 unchanged displays and one explicitly recorded display transcription repair; all 15 current derived-input payloads preserved exactly.'
    manifest['typesetting_corrections'].update(sha256=sha(files['TYPESETTING_CORRECTIONS.json']),
        literal_note_conversion_repaired=True, literal_note_repair='INDETALE_CONVERSION_REPAIR.json')
    manifest['revised_at_utc'] = receipt['recorded_at_utc']
    index = {r['file']: r for r in manifest['files']}
    for name, content in files.items():
        index[name] = dict(file=name, bytes=len(content), sha256=sha(content))
    manifest['files'] = sorted(index.values(), key=lambda r: r['file'])
    # All invariants precede the mutation; preserved history is part of the new manifest.
    for name, content in files.items():
        p = S / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(content)
    (S / 'MANIFEST.json').write_bytes(dump(manifest))
    print(json.dumps(dict(result='PASS_EXACT_LITERAL_CONVERSION_REPAIR', manifest_sha256=sha(dump(manifest)),
        unchanged_displays=14, declared_display_repairs=1, original_markdown_unchanged=True, build_verified=False)))

if __name__ == '__main__':
    main()
