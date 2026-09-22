"""Bind the completed Categories review for the next separate candidate role."""
import argparse
from collections import Counter
import json

import categories_intake_20260922 as source
import reconcile_correction_occurrences_20260922 as intake
from verify_categories_intake_review_20260922 import git, require, replace_bound


def identity(raw):
    return {'bytes': len(raw), 'sha256': source.sha(raw)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--check', action='store_true')
    args = p.parse_args()
    here = source.HERE
    review_raw = (here / 'CATEGORIES_INTAKE_REVIEW_20260922.json').read_bytes()
    review = json.loads(review_raw)
    replay_raw = (here / 'CATEGORIES_INTAKE_REVIEW_REPLAY_20260922.json').read_bytes()
    replay = json.loads(replay_raw)
    require(replay['review']['sha256'] == source.sha(review_raw), 'Stale replay receipt')
    require(replay['occurrence_coverage']['reviewed'] == 165 and replay['new_operations'] == 107,
            'Unexpected reviewed scope')
    registry = (source.ROOT / 'ai-integrated/registry/overlays.json').read_bytes()
    require(registry == git('show', source.CURRENT + ':ai-integrated/registry/overlays.json'),
            'Registry changed since review')
    groups = [g for g in review['groups'] if g['disposition'].startswith('accepted_missing_')]
    all_ops, rebound, units = [], [], []
    for g in groups:
        ops = []
        for j, op in enumerate([o for o in replay['operations'] if o['review_id'] == g['id']], 1):
            bound = {key: op[key] for key in ('line', 'old_text', 'replacement_text', 'start_byte',
                'end_byte_exclusive', 'old_sha256', 'replacement_sha256')}
            bound['operation_id'] = f'{g["id"]}-OP{j}'
            ops.append(bound)
            rebound.append({**bound, 'start_byte': op['current_start_byte'],
                'end_byte_exclusive': op['current_start_byte'] + len(op['old_text'].encode()),
                'cumulative_line': op['current_line']})
        all_ops.extend(ops)
        units.append({'id': g['id'], 'source': 'categories.tex', 'operations': ops,
            'producer_occurrences': g['occurrences'], 'class': g['disposition'],
            'rationale': g['rationale'], 'adverse_evidence': g['adverse_evidence'],
            'review_file': 'CATEGORIES_INTAKE_REVIEW_20260922.json',
            'discovery': g.get('discovery'), 'occurrence_dispositions': g.get('occurrence_dispositions', {})})
    authority = git('show', source.BASE + ':categories.tex')
    current = git('show', source.CURRENT + ':categories.tex')
    isolated = replace_bound(authority, all_ops)
    cumulative = replace_bound(current, rebound)
    require(identity(isolated)['sha256'] == replay['git_replays'][0]['postimage_sha256'], 'Isolated replay mismatch')
    require(identity(cumulative)['sha256'] == replay['git_replays'][1]['postimage_sha256'], 'Cumulative replay mismatch')
    evidence_names = ['CATEGORIES_INTAKE_REVIEW_20260922.json', 'CATEGORIES_INTAKE_REVIEW_REPLAY_20260922.json',
        'CATEGORIES_PENDING_SOURCE_REPAIRS_20260922.patch', 'CATEGORIES_PENDING_CUMULATIVE_REPAIRS_20260922.patch',
        'categories_intake_20260922.py', 'verify_categories_intake_review_20260922.py',
        'test_categories_intake_replay_20260922.py', 'prepare_categories_batch_20260922.py']
    result = {'schema': 'stacks-next-correction-batch-input/v1', 'prepared_on': '2026-09-22',
        'authority_commit': source.BASE, 'checked_public_main': source.CURRENT,
        'registry_sha256': source.sha(registry), 'units': units, 'unit_count': len(units),
        'operation_count': len(all_ops), 'sources': [{'source': 'categories.tex',
            'authority': identity(authority), 'cumulative_preimage': identity(current),
            'prospective_isolated_postimage': identity(isolated), 'prospective_cumulative_postimage': identity(cumulative),
            'operations': len(all_ops), 'rebound_operations': rebound, 'exact_preimages': True,
            'prior_corrections_preserved': True, 'legacy_context_envelope_overlaps':
                [o for o in replay['operations'] if o['admitted_context_envelope_overlaps']]}],
        'evidence': [{'path': name, **identity((here / name).read_bytes())} for name in evidence_names],
        'dependency_groups': [], 'scope': '83 new reviewed correction/clarification/copyedit groups, 107 exact operations, Categories only. Includes one adjacent inverse-map repair found during review. All 165 producer reports are disposed; duplicates, already composed fixes, optional suggestions and rejected allegations remain in bound evidence.',
        'registry_admission': False, 'canonical_ids_allocated': False, 'source_mutations': 0,
        'build_claimed': False, 'reviewer': 'OpenAI Codex — GPT-6 Astra, Ultra effort', 'workers_used': False,
        'next_action': 'Issue the next available Categories candidate lease after checking live registry; materialize this exact batch; complete source closure, build, visual and independent executable replay gates; separately admit, compose and publish with fixes-only exports.'}
    raw = (json.dumps(result, indent=2, ensure_ascii=False) + '\n').encode()
    path = here / 'CATEGORIES_CORRECTION_BATCH_INPUT_20260922.json'
    if args.check:
        require(path.read_bytes() == raw, 'Prepared batch is not reproducible')
    else:
        path.write_bytes(raw)
    physical = Counter()
    for group in review['groups']:
        physical[group['disposition']] += len(group['occurrences'])
    print(json.dumps({'path': str(path), **identity(raw), 'unit_count': len(units),
        'operation_count': len(all_ops), 'physical_report_dispositions': dict(physical),
        'review_replay': identity(replay_raw)}, indent=2))


if __name__ == '__main__':
    main()
