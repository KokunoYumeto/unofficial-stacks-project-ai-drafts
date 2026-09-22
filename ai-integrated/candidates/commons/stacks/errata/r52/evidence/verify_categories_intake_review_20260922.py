"""Replay Categories proposals in isolated indexes; never edit source/registry."""
import argparse
from collections import Counter
import difflib
import itertools
import json
import re
import sys

import categories_intake_20260922 as source
import reconcile_correction_occurrences_20260922 as intake
from verify_sets_intake_review_20260922 import git, patch_for, replay_index

HERE, ROOT, BASE, CURRENT = source.HERE, source.ROOT, source.BASE, source.CURRENT
NAME = 'categories.tex'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def replace_bound(raw, operations):
    result = raw
    prior_start = len(raw) + 1
    for op in sorted(operations, key=lambda x: x['start_byte'], reverse=True):
        start, end = op['start_byte'], op['end_byte_exclusive']
        require(end <= prior_start, 'Overlapping proposed operations')
        require(result[start:end] == op['old_text'].encode(), 'Preimage drift')
        result = result[:start] + op['replacement_text'].encode() + result[end:]
        prior_start = start
    return result


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    review, identity = intake.loaded(HERE / 'CATEGORIES_INTAKE_REVIEW_20260922.json')
    records, triage, authority = source.inputs()
    require(source.sha((HERE / 'CORRECTION_OCCURRENCE_TRIAGE_20260922.jsonl').read_bytes()) ==
            'CED820133BA55EE051A60532925F90A312D7FC1B3F3C9C522F1EE7B653C12EB6', 'Triage drift')
    expected = {f'OCC-{i:05d}' for i, row in enumerate(records, 1) if intake.source_name(row) == NAME}
    actual = [o for g in review['groups'] for o in g['occurrences']]
    require(len(expected) == 165 and len(actual) == len(set(actual)) and set(actual) == expected,
            'Review must cover all 165 received Categories reports exactly once')
    require(review['next_source_start_line'] is None, 'Review is incomplete')
    require(review['authority_commit'] == BASE and review['compared_public_commit'] == CURRENT,
            'Review revision mismatch')
    require(source.sha(authority) == review['authority_sha256'], 'Authority hash mismatch')
    require(git('rev-parse', 'HEAD').decode().strip() == CURRENT, 'Current HEAD advanced; rebind explicitly')
    current = git('show', f'{CURRENT}:{NAME}')
    require((ROOT / NAME).read_bytes().replace(b'\r\n', b'\n') == current,
            'Working Categories source differs from the reviewed Git object')
    model = intake.import_model()
    module = sys.modules['bound_changes_model']
    units = {u.stable_id: u for u in model.units if u.source == NAME}
    claimed = {i for g in review['groups'] for i in g['canonical_ids']}
    require(claimed == set(units) and len(units) == 8, 'Existing Categories unit closure mismatch')
    admitted = [op for u in units.values() for op in u.operations]
    corrected_existing = module.apply_operations(authority, admitted, 'categories-existing-operations')
    # Ensure current source retains every exact corrected line from admitted
    # operations. Additional theorem text is expected and must not be replaced.
    existing_lines = corrected_existing.splitlines(keepends=True)
    current_lines = current.splitlines(keepends=True)
    matched_existing = set()
    for block in difflib.SequenceMatcher(None, existing_lines, current_lines, autojunk=False).get_matching_blocks():
        matched_existing.update(range(block.a, block.a + block.size))
    require(len(matched_existing) == len(existing_lines),
            'Existing corrected source is not retained line-for-line among cumulative additions')

    lines = authority.splitlines(keepends=True)
    offsets = list(itertools.accumulate([0] + [len(line) for line in lines]))
    current_offsets = list(itertools.accumulate([0] + [len(line) for line in current_lines]))
    mapping = {}
    for block in difflib.SequenceMatcher(None, lines, current_lines, autojunk=False).get_matching_blocks():
        for d in range(block.size):
            mapping[block.a + d] = block.b + d
    proposals, cumulative = [], []
    for group in review['groups']:
        ops = group.get('operations', [])
        require(bool(ops) == group['disposition'].startswith('accepted_missing_'),
                f'Operation/disposition mismatch: {group["id"]}')
        require(group.get('rationale') and group.get('adverse_evidence'), 'Missing review evidence')
        if not group['occurrences']:
            require(group.get('discovery'), 'Unattributed extra review unit')
        for op in ops:
            line = lines[op['line'] - 1]
            old, new = op['old_text'].encode(), op['replacement_text'].encode()
            require(old and old != new and line.count(old) == 1,
                    f'Exact unique authority preimage failed: {group["id"]} line {op["line"]}')
            start = offsets[op['line'] - 1] + line.index(old)
            end = start + len(old)
            cumulative_index = mapping.get(op['line'] - 1)
            require(cumulative_index is not None and current_lines[cumulative_index] == line,
                    f'Authority line was changed or lost in current source: {group["id"]}')
            cumulative_start = current_offsets[cumulative_index] + line.index(old)
            envelope_overlaps = sorted({u.stable_id for u in units.values() for prior in u.operations
                if prior.start_byte < end and start < prior.end_byte_exclusive})
            # Legacy operations include unchanged context. Such envelope overlap
            # is permitted only because the complete actual target line above is
            # proved unchanged in current source; no admitted edit is overwritten.
            proposals.append({'review_id': group['id'], 'occurrences': group['occurrences'], **op,
                'start_byte': start, 'end_byte_exclusive': end,
                'old_sha256': source.sha(old), 'replacement_sha256': source.sha(new),
                'admitted_context_envelope_overlaps': envelope_overlaps,
                'current_line': cumulative_index + 1, 'current_start_byte': cumulative_start})
            cumulative.append({**op, 'start_byte': cumulative_start,
                               'end_byte_exclusive': cumulative_start + len(old)})
    corrected_authority = replace_bound(authority, proposals)
    corrected_current = replace_bound(current, cumulative)
    inverse = []
    delta = 0
    for op in sorted(cumulative, key=lambda x: x['start_byte']):
        start = op['start_byte'] + delta
        inverse.append({'start_byte': start, 'end_byte_exclusive': start + len(op['replacement_text'].encode()),
                        'old_text': op['replacement_text'], 'replacement_text': op['old_text']})
        delta += len(op['replacement_text'].encode()) - len(op['old_text'].encode())
    require(replace_bound(corrected_current, inverse) == current, 'Untouched cumulative bytes not preserved')
    refs = re.compile(rb'\\(?:ref|eqref|pageref|nameref|label|cite)\{[^}]*\}')
    require(refs.findall(authority) == refs.findall(corrected_authority), 'Authority references changed')
    require(refs.findall(current) == refs.findall(corrected_current), 'Current references changed')
    patch = patch_for(authority, corrected_authority, NAME)
    cumulative_patch = patch_for(current, corrected_current, NAME)
    replays = [replay_index(BASE, patch, corrected_authority, NAME),
               replay_index(CURRENT, cumulative_patch, corrected_current, NAME)]
    paths = {'CATEGORIES_PENDING_SOURCE_REPAIRS_20260922.patch': patch,
             'CATEGORIES_PENDING_CUMULATIVE_REPAIRS_20260922.patch': cumulative_patch}
    disposition_counts = Counter(g['disposition'] for g in review['groups'])
    receipt = {'schema': 'stacks-categories-intake-review-replay-v1', 'review': identity,
        'authority': {'commit': BASE, 'bytes': len(authority), 'sha256': source.sha(authority)},
        'current': {'commit': CURRENT, 'bytes': len(current), 'sha256': source.sha(current)},
        'occurrence_coverage': {'reviewed': len(actual), 'received': len(expected), 'exactly_once': True,
                              'missing': [], 'duplicates': []},
        'review_groups': len(review['groups']), 'disposition_counts': dict(disposition_counts),
        'new_proposed_units': sum(g['disposition'].startswith('accepted_missing_') for g in review['groups']),
        'new_operations': len(proposals), 'already_composed_units': sorted(units),
        'existing_corrected_lines_retained': len(matched_existing),
        'cumulative_extra_lines_preserved': len(current_lines) - len(existing_lines),
        'exact_inverse_replay_preserves_other_cumulative_bytes': True,
        'labels_references_citations': 'UNCHANGED', 'operations': proposals, 'git_replays': replays,
        'patches': [{'path': name, 'bytes': len(raw), 'sha256': source.sha(raw)} for name, raw in paths.items()],
        'not_claimed': ['new registry admission', 'cumulative source mutation', 'new rendered chapter build',
                        'independent second-agent or human review', 'overall multilingual inventory completion'],
        'next_action': 'Seal a separate Categories candidate, validate affected cumulative and authority builds and visual QA, then admit/compose/publish under the existing contract.'}
    paths['CATEGORIES_INTAKE_REVIEW_REPLAY_20260922.json'] = (json.dumps(receipt, ensure_ascii=False, indent=2) + '\n').encode()
    for name, raw in paths.items():
        path = HERE / name
        if args.check:
            require(path.read_bytes() == raw, f'Non-deterministic generated output: {name}')
        else:
            path.write_bytes(raw)
    print(json.dumps({k: v for k, v in receipt.items() if k != 'operations'}, indent=2))


if __name__ == '__main__':
    main()
