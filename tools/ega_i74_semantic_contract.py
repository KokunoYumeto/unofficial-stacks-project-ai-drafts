"""Exact EGA I7.4 evidence contracts; not a mathematical proof checker.

The seal is independent of receipt metadata. Actual target blocks, source
boundaries, discovery, ledger prefixes, dossier and final review are separately
checked. Live source retrieval is performed only by the bounded replay tool.
"""
import csv
import hashlib
import io
import json

RECEIPT_PATH = 'validation/ega-i-7.4.1-7.4.7-semantic-checkpoint-2026-09-08.json'
RECEIPT_BYTES = 231315
RECEIPT_SHA256 = '82D960315E0E6E806E1B1AB34A37257846F32F152660B6A4D256CA19A9163F43'
CONTRACT_SHA256 = '173EE5295BCF7CE35C221EBD52D2453567A9C9751A37C81251C957AA20D2AFC9'
SEMANTICS = {'source_versions': ['fr', 'en', 'errata_fr'], 'source_744': 'literal arbitrary torsion-free claim false; no bounded checked erratum found; no novelty claim', 'source_747': 'old proper-support extension superseded by printed Err_III12', 'R_definition': 'sheafification of dense-open regular functions; not general regular-denominator meromorphic sheaf', 'simple_normalization': 'constant sheaf; parenthesized powers are arbitrary sheaf direct sums', 'I741_category': 'arbitrary O_X-module sheaves on integral X', 'I741_kernel': 'stalkwise elements killed by nonzero local scalar', 'I741_quotient': 'torsion-free without quasi-coherence or finite generation', 'I741_torsion_subsheaf_qc': 'conditional on F quasi-coherent', 'I742_category': 'quasi-coherent torsion-free on integral X', 'I742_embedding': 'canonical into constant generic fibre; chosen basis for R_X^(I)', 'I742_generation': 'local or stalkwise rational linear span, not global tensor sections', 'I742_rank': 'arbitrary cardinal including zero; independent of nonempty affine open', 'I743_converse': 'nonzero quasi-coherent submodule only; zero has rank zero', 'I743_nonqc_subsheaf': 'kernel O_X to S_p(O_Xp), zero at p but nonzero generic stalk', 'I744_skyscraper': 'S_p(N)(U)=N if p in U else0; O_Xp scalar action, not residue-field action', 'I744_counterexample': 'distinct closed-point K skyscrapers are torsion-free with nonzero1sections and zero tensor sheaf', 'I744_finite_type_counterexample': 'local-ring skyscrapers are sheaf quotients of O_X; stalkwise surjection not all-open section surjection', 'I744_repair': 'both sheaves quasi-coherent and torsion-free; sufficient, not asserted minimal', 'I744_rank_error': 'arbitrary generic fibres need not embed in K; K^2 already refutes rank-one inference', 'I744_pure_tensor': 'linear functional proves nonvanishing for arbitrary-dimensional vector spaces', 'I745_printed': 'dominant integral X to integral Y; qc torsion-free F has torsion-free f_*F', 'I745_derived': 'qc unnecessary; nonzero local scalar stays nonzero at every source stalk', 'I745_pushforward_qc_claimed': False, 'I745_morphism_finiteness_required': False, 'I745_false_738_iso_used': False, 'I746_printed': 'qc finite-type F; torsion iff zero generic stalk iff proper support', 'I746_derived': 'same literal equivalence for arbitrary qc F by further localization', 'I746_dense_example': 'direct sum Q[t]/(r) over monic irreducibles has all closed points and no generic point in support', 'I746_proper_equals_nowhere_dense_without_ft': False, 'I747_counterexample': 'Spec(k times k), e1O has proper support and identity rationalization, hence nonzero torsion-free', 'I747_corrected_hypothesis': 'reduced; every point has an open neighborhood with finitely many irreducible components', 'I747_global_finite_components_required': False, 'I747_printed_sheaf': 'quasi-coherent of finite type', 'I747_condition': 'support contains no irreducible component; equivalently all component generic stalks zero', 'I747_proof': 'affine finite minimal-prime localization product; tensor finite product; cover by such neighborhoods', 'I747_without_ft': 'generic/component exclusion retained for qc F; not nowhere-dense reformulation', 'printed_original_visual_read': 'attributed to source reviewer; not newly performed by implementation owner', 'proofs_complete': True, 'official_tags_assigned': 0, 'new_root_theorem': False, 'source_edition_mutated': False, 'formal_proof_checking': False, 'complete_EGA_claimed': False}
AUTHORITY = {'path': 'validation/ega-i-7.4.1-7.4.7-printed-authority-2026-09-08.json', 'bytes': 17535, 'sha256': '0A88EE3EE0093F0EEA0D79EFD599E54E7FD906E06BBCA182BD016125DA31D74A'}
DOSSIER = {'path': 'ega/i74.md', 'bytes': 19207, 'sha256': '828336F9F505DAFCBD9C5DF17739D4917F9FBB078E3CA937D964986D82F9368E'}
UNITS = ['ega:I.7.4.' + str(n) for n in range(1, 8)]
PROOFS = ['ega:I.7.4.' + str(n) + ':proof' for n in (4, 5, 6)]
UPSTREAM = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
BASE = 'c9c1b046e2d8f353edaaf51a4311cb8827f03cfb'
TARGET_COMMIT = BASE


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def identity_errors(raw, expected, label):
    if (type(raw) is not bytes or len(raw) != expected.get('bytes')
            or digest(raw) != expected.get('sha256')):
        return ['I7.4 ' + label + ' exact bytes changed']
    return []


def authority_errors(raw):
    return identity_errors(raw, AUTHORITY, 'separately attributed printed authority')


def dossier_errors(raw, expected):
    if expected != DOSSIER:
        return ['I7.4 dossier cannot authenticate its own changed metadata']
    return identity_errors(raw, DOSSIER, 'full seven-unit proof dossier')


def receipt_errors(raw):
    return identity_errors(raw, {'bytes': RECEIPT_BYTES, 'sha256': RECEIPT_SHA256}, 'immutable receipt')


def verify(checkpoint, scope, tables, discovery, target_loader, tag_map, raw_loader):
    """Fail closed before using metadata, then replay the actual byte objects."""
    if (not all(type(x) is dict for x in (checkpoint, scope, tables, discovery, tag_map))
            or not callable(target_loader) or not callable(raw_loader)):
        return ['I7.4 inputs must be exact objects and callable byte loaders']
    try:
        if digest(canonical(checkpoint)) != CONTRACT_SHA256:
            return ['I7.4 reviewed source/target/choice/ledger contract changed']
    except (TypeError, ValueError, OverflowError):
        return ['I7.4 checkpoint must contain serializable JSON metadata']
    errors = []
    if (canonical(checkpoint['semantic_contract']) != canonical(SEMANTICS)
            or checkpoint['source_units'] != UNITS
            or checkpoint['source_proof_units'] != PROOFS
            or checkpoint['starting_content_commit'] != BASE
            or checkpoint['stacks_upstream'] != UPSTREAM
            or checkpoint['next_semantic_cursor'] != 'ega:I.8.1.1'):
        errors.append('I7.4 reviewed hypotheses or source order changed')
    for key in ('statement_review_snapshot', 'residual_snapshot', 'next_semantic_cursor'):
        if scope.get(key) != checkpoint[key]:
            errors.append('I7.4 live scope changed: ' + key)
    for field, items in [('reviewed_source_slices', checkpoint['french_authority']['source_scopes']),
                         ('reviewed_errata_slices', checkpoint['french_authority']['reviewed_errata_scopes'])]:
        if type(scope.get(field)) is not dict:
            errors.append('I7.4 scope source dictionary missing: ' + field)
        else:
            for key, item in items.items():
                if scope[field].get(key) != item:
                    errors.append('I7.4 exact source scope changed: ' + key)

    def read(loader, *args):
        try:
            raw = loader(*args)
            if type(raw) is not bytes:
                raise ValueError('expected bytes')
            return raw
        except (OSError, ValueError, TypeError, KeyError):
            errors.append('I7.4 byte object unavailable: ' + str(args))
            return b''

    cache = {}
    target_joins = set()
    for target in checkpoint['targets']:
        target_joins.add((target['tag'], target['label'], target['path']))
        if tag_map.get(target['label']) != target['tag']:
            errors.append('I7.4 official tag-label join changed: ' + target['tag'])
        for edition, commit in [('official', UPSTREAM), ('integrated', TARGET_COMMIT)]:
            item = target[edition]; key = (commit, target['path'])
            if key not in cache:
                cache[key] = read(target_loader, *key)
            raw = cache[key]; lines = raw.splitlines(keepends=True)
            block = b''.join(lines[item['lf_line_start'] - 1:item['lf_line_end']])
            prefix = target['path'][:-4] + '-'; short = target['label'][len(prefix):]
            if (not target['label'].startswith(prefix) or item['commit'] != commit
                    or len(raw) != item['source_bytes'] or digest(raw) != item['source_sha256']
                    or len(block) != item['bytes'] or digest(block) != item['sha256']
                    or block != item['text'].encode()
                    or raw[item['byte_offset_start']:item['byte_offset_end_exclusive']] != block
                    or ('\\label{' + short + '}').encode() not in block):
                errors.append('I7.4 actual ' + edition + ' complete target changed: ' + target['tag'])
    for context in checkpoint['target_contexts']:
        for edition, commit in [('official', UPSTREAM), ('integrated', TARGET_COMMIT)]:
            item = context[edition]; key = (commit, context['path'])
            raw = cache.get(key)
            if raw is None:
                raw = read(target_loader, *key); cache[key] = raw
            block = b''.join(raw.splitlines(keepends=True)[item['lf_line_start'] - 1:item['lf_line_end']])
            if (len(raw) != item['source_bytes'] or digest(raw) != item['source_sha256']
                    or len(block) != item['bytes'] or digest(block) != item['sha256']
                    or block != item['text'].encode()
                    or raw[item['byte_offset_start']:item['byte_offset_end_exclusive']] != block):
                errors.append('I7.4 actual target dependency context changed: ' + context['name'])
    from tools.check_ega_i74_source_boundaries import LANGUAGES, validate_artifact
    for version in LANGUAGES:
        errors.extend(validate_artifact(checkpoint['languages'][version], version))
    errors.extend(authority_errors(read(raw_loader, AUTHORITY['path'])))
    if checkpoint['french_authority']['primary_binding'] != AUTHORITY:
        errors.append('I7.4 printed authority metadata changed')
    errors.extend(dossier_errors(read(raw_loader, DOSSIER['path']), checkpoint['derivation_dossier']))

    unit_set = set(UNITS + PROOFS)
    for ledger in checkpoint['ledgers']:
        path, key = ledger['path'], ledger['id_field']; table = tables.get(path)
        if (type(table) is not list or any(type(row) is not dict or
                any(type(k) is not str or (type(v) is not str and not
                    (k == 'supersedes' and v is None)) for k, v in row.items()) for row in table)):
            errors.append('I7.4 supplied CSV table malformed: ' + path); continue
        ids = {row[key] for row in ledger['rows']}
        if [row for row in table if row.get(key) in ids] != ledger['rows']:
            errors.append('I7.4 exact appended ledger rows changed: ' + path)
        if path != 'ega/agent.csv':
            source_key = 'subject_id' if path == 'ega/dec.csv' else 'source_unit'
            if [row for row in table if row.get(source_key) in unit_set] != ledger['rows']:
                errors.append('I7.4 source-unit closure changed: ' + path)
        raw = read(raw_loader, path)
        if b'\r' in raw or not raw.endswith(b'\n'):
            errors.append('I7.4 ledger must retain exact LF serialization: ' + path)
        lines = raw.splitlines(keepends=True)
        prefix = b''.join(lines[:ledger['prefix_rows'] + 1])
        append = b''.join(lines[ledger['prefix_rows'] + 1:ledger['final_rows'] + 1])
        for data, size, seal, kind in [(prefix, ledger['prefix_bytes'], ledger['prefix_sha256'], 'historical prefix'),
                (append, ledger['append_bytes'], ledger['append_sha256'], 'reviewed append'),
                (raw, ledger['bytes'], ledger['sha256'], 'current postimage')]:
            if len(data) != size or digest(data) != seal:
                errors.append('I7.4 ' + kind + ' changed: ' + path)
        parsed = list(csv.DictReader(io.StringIO(raw.decode('utf-8', errors='replace'), newline='')))
        superseded = {row.get('supersedes') for row in parsed if row.get('supersedes')}
        if table != [row for row in parsed if row.get(key) not in superseded]:
            errors.append('I7.4 supplied active table differs from actual CSV bytes: ' + path)
    actual_edges = tables.get('ega/smap.csv', [])
    if type(actual_edges) is list and all(type(r) is dict and
            type(r.get('source_unit')) is str and all(type(k) is str and
                (type(v) is str or (k == 'supersedes' and v is None))
                for k, v in r.items()) for r in actual_edges):
        joins = {(r.get('official_tag'), r.get('stacks_label'), r.get('stacks_file'))
                 for r in actual_edges if r.get('source_unit') in unit_set}
        if joins != target_joins:
            errors.append('I7.4 exact target and ledger joins are not closed')
    actual_residuals = tables.get('ega/resid.csv', [])
    if type(actual_residuals) is list and all(type(r) is dict for r in actual_residuals):
        gaps = [r for r in actual_residuals if r.get('status') == 'open_gap']
        if gaps != checkpoint['preserved_open_gap_rows'] or len(gaps) != 12:
            errors.append('I7.4 twelve earlier gaps changed or falsely closed')
    raw = read(raw_loader, 'ega/units.csv')
    inventory = list(csv.DictReader(io.StringIO(raw.decode('utf-8', errors='replace'), newline='')))
    if discovery != {r.get('unit_id'): r for r in inventory} or len(discovery) != len(inventory):
        errors.append('I7.4 supplied discovery differs from live unchanged inventory')
    for row in checkpoint['english_discovery']['stable_units']:
        if discovery.get(row['unit_id']) != row:
            errors.append('I7.4 discovery unit changed or promoted: ' + row['unit_id'])
    for item in checkpoint['preserved_inputs'] + checkpoint['reviewed_artifacts']:
        errors.extend(identity_errors(read(raw_loader, item['path']), item, item['path']))
    if not checkpoint['review_record'] or not any(x['path'] == 'ega/i74-review.md' for x in checkpoint['reviewed_artifacts']):
        errors.append('I7.4 actual independent final review record missing')
    return errors
