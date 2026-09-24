"""Exact Fields chapter proposal replay; no source or registry writes."""
import argparse
from collections import Counter
import difflib
import itertools
import json
import re
import sys

import fields_chapter_intake_20260924 as source
import reconcile_correction_occurrences_20260922 as intake
from verify_categories_intake_review_20260922 import replace_bound, require
from verify_sets_intake_review_20260922 import git, patch_for, replay_index

HERE, ROOT, BASE, CURRENT = source.HERE, source.ROOT, source.BASE, source.CURRENT


def line_map(original, current):
    result = {}
    for block in difflib.SequenceMatcher(None, original, current, autojunk=False).get_matching_blocks():
        for d in range(block.size):
            result[block.a + d] = block.b + d
    return result


def structure(raw):
    # Preserve citation keys, not their optional human-readable locator spelling.
    pattern = rb'\\(ref|eqref|pageref|nameref|label|cite)(?:\[[^\]]*\])?\{([^}]*)\}'
    return re.findall(pattern, raw)



REQUIRED_PROOFS = {
    'FIELDS_NORMAL_DECOMPOSITION_PROOF_20260925.tex',
    'FIELDS_NORMAL_DECOMPOSITION_PROOF_CHECK_20260925.md',
    'FIELDS_NORMAL_DECOMPOSITION_PRIMARY_REVIEW_20260925.json',
}

PROOF_FILE = 'FIELDS_NORMAL_DECOMPOSITION_PROOF_20260925.tex'
PROOF_OLD = 'We found the subfield $E_{sep}$ in Lemma \\ref{lemma-separable-first}.\nWe set $E_{insep} = E^{\\text{Aut}(E/F)}$. Details omitted.'
PROOF_REFS = [(b'ref', name.encode()) for name in [
    'lemma-separable-first', 'lemma-separable-first-normal', 'lemma-lift-maps',
    'lemma-irreducible-polynomials', 'lemma-normal-goes-up', 'lemma-separable-goes-up',
    'lemma-subalgebra-algebraic-extension-field', 'lemma-primitive-element',
]]


def verify_proof_evidence(review, directory=HERE):
    require(review.get('mathematical_review_complete') is True,
            'Primary mathematical repairs are not yet finalized')
    rows = review.get('required_proof_evidence', [])
    names = [row['path'] for row in rows]
    require(len(names) == len(set(names)) and set(names) == REQUIRED_PROOFS,
            'Required complete proof evidence is missing or duplicated')
    for row in rows:
        require('/' not in row['path'] and '\\' not in row['path'], 'Evidence path is not a basename')
        raw = (directory / row['path']).read_bytes()
        require(len(raw) == row['bytes'] and intake.digest(raw) == row['sha256'],
                'Required complete proof evidence changed')
    groups = {g['id']:g for g in review['groups']}
    group = groups['FIELDS-RECON-059']
    link = group.get('proof_evidence', {})
    require(link.get('file') == 'FIELDS_NORMAL_DECOMPOSITION_PROOF_CHECK_20260925.md'
            and link.get('required_in_candidate') is True,
            'Mathematical correction lost its complete proof link')
    fragment = (directory / PROOF_FILE).read_text(encoding='utf-8').rstrip('\n')
    targets = [op for op in group['operations'] if op['line'] == 3679]
    require(len(targets) == 1 and targets[0]['replacement_text'] == fragment,
            'Proposed source no longer contains the checked complete proof')
    require(structure(fragment.encode()) == PROOF_REFS,
            'Checked source proof reference targets changed')
    receipt = json.loads((directory / 'FIELDS_NORMAL_DECOMPOSITION_PRIMARY_REVIEW_20260925.json').read_bytes())
    require(receipt['proof'] in rows and receipt['proof_check'] in rows,
            'Primary review does not bind the retained proof and check')
    dependencies = review.get('dependency_groups', [])
    expected = {'normal-decomposition-prerequisites': {
        'FIELDS-RECON-033', 'FIELDS-RECON-034', 'FIELDS-RECON-038', 'FIELDS-RECON-059'}}
    require(len(dependencies) == 1 and {d['id']:set(d['review_ids']) for d in dependencies} == expected,
            'Mathematical dependency membership changed')
    require(all(d['required_together'] is True and set(d['review_ids']) <= set(groups)
                for d in dependencies), 'Unbound mathematical dependency')


def verify_structure(before, after, operations):
    changed = [op for op in operations
               if structure(op['old_text'].encode()) != structure(op['replacement_text'].encode())]
    require(all(op['review_id'] == 'FIELDS-RECON-059' and op['line'] == 3679
                and op['old_text'] == PROOF_OLD
                and structure(op['replacement_text'].encode()) == PROOF_REFS
                for op in changed) and len(changed) <= 1,
            'Unexpected reference-key exception')
    expected = replace_bound(before, changed)
    require(structure(expected) == structure(after),
            'Reference/label/citation-key inventory changed outside bound exceptions')
    return [{'review_id':op['review_id'], 'authority_line':op['line'],
             'start_byte':op['start_byte'], 'old_text':op['old_text'],
             'replacement_text':op['replacement_text']} for op in changed]


def verify_one(name, count, existing_count, model):
    stem = name.removesuffix('.tex').upper()
    review, review_id = intake.loaded(HERE / f'{stem}_INTAKE_REVIEW_20260924.json')
    received, authority = source.inputs(name)
    expected = {oid for oid, _, _ in received}
    actual = [o for g in review['groups'] for o in g['occurrences']]
    require(len(expected) == count, 'Received count changed')
    require(len(actual) == len(set(actual)) and set(actual) == expected,
            f'{name} coverage mismatch: missing={sorted(expected-set(actual))}, extra={sorted(set(actual)-expected)}')
    require(review['next_source_start_line'] is None, 'Review incomplete')
    verify_proof_evidence(review)
    require(review['authority_commit'] == BASE and review['compared_public_commit'] == CURRENT,
            'Review revision mismatch')
    require(review['inventory_sha256'] == intake.EXPECTED_RECORDS, 'Inventory identity mismatch')
    require(review['authority_sha256'] == intake.digest(authority), 'Authority identity mismatch')
    current = git('show', f'{CURRENT}:{name}')
    require((ROOT/name).read_bytes().replace(b'\r\n', b'\n') == current, 'Working source differs')
    units = {u.stable_id:u for u in model.units if u.source == name}
    from dataclasses import asdict
    retained_units = json.loads((HERE / 'FIELDS_PRIOR_ADMITTED_UNITS_20260924.json').read_bytes())
    require({u['stable_id']:u for u in retained_units} == json.loads(json.dumps({i:asdict(u) for i,u in units.items()})),
            'Retained prior-unit evidence no longer matches the bound model')
    require([g['id'] for g in review['groups']] ==
            [f'FIELDS-RECON-{n:03d}' for n in range(1,len(review['groups'])+1)], 'Group IDs differ')
    claimed = {i for g in review['groups'] for i in g['canonical_ids']}
    require(claimed == set(units) and len(units) == existing_count, 'Existing-unit closure differs')
    module = sys.modules['bound_changes_model']
    old_corrected = module.apply_operations(authority, [o for u in units.values() for o in u.operations], name)
    old_lines = old_corrected.splitlines(keepends=True)
    current_lines = current.splitlines(keepends=True)
    preserved = line_map(old_lines, current_lines)
    require(len(preserved) == len(old_lines), 'Prior corrections are not fully retained')
    lines = authority.splitlines(keepends=True)
    mapping = line_map(lines,current_lines)
    offsets = list(itertools.accumulate([0]+list(map(len,lines))))
    current_offsets = list(itertools.accumulate([0]+list(map(len,current_lines))))
    proposed, cumulative = [], []
    for group in review['groups']:
        ops = group.get('operations',[])
        require(bool(ops) == group['disposition'].startswith('accepted_missing_'), 'Disposition/operation mismatch')
        require(group.get('rationale') and group.get('adverse_evidence'), 'Missing evidence')
        require(group['occurrences'] or group.get('discovery'), 'Unattributed discovered unit')
        for op in ops:
            old,new = op['old_text'].encode(),op['replacement_text'].encode()
            first = op['line'] - 1
            span = old.count(b'\n') + 1
            window = b''.join(lines[first:first+span])
            require(old and old != new and window.count(old) == 1,
                    f'Nonunique/wrong preimage {group["id"]} line {op["line"]}: {op["old_text"]!r}')
            within = window.index(old)
            require(within < len(lines[first]), 'Preimage starts outside its declared line')
            start = offsets[first]+within
            end = start+len(old)
            mapped = mapping.get(first)
            require(mapped is not None and all(mapping.get(first+k) == mapped+k for k in range(span))
                    and b''.join(current_lines[mapped:mapped+span]) == window,
                    f'Target lines changed in cumulative source: {group["id"]}')
            current_start = current_offsets[mapped]+within
            overlaps = sorted({u.stable_id for u in units.values() for o in u.operations
                if o.start_byte < end and start < o.end_byte_exclusive})
            proposed.append({'review_id':group['id'],'occurrences':group['occurrences'],**op,
                'start_byte':start,'end_byte_exclusive':end,
                'old_sha256':intake.digest(old),'replacement_sha256':intake.digest(new),
                'admitted_context_envelope_overlaps':overlaps,
                'current_line':mapped+1,'current_start_byte':current_start})
            cumulative.append({'review_id':group['id'],**op,'start_byte':current_start,'end_byte_exclusive':current_start+len(old)})
    isolated = replace_bound(authority,proposed)
    composed = replace_bound(current,cumulative)
    inverse,delta = [],0
    for op in sorted(cumulative,key=lambda o:o['start_byte']):
        start=op['start_byte']+delta
        old,new=op['old_text'],op['replacement_text']
        inverse.append({'start_byte':start,'end_byte_exclusive':start+len(new.encode()),
                        'old_text':new,'replacement_text':old})
        delta+=len(new.encode())-len(old.encode())
    require(replace_bound(composed,inverse)==current,'Inverse replay did not recover all cumulative bytes')
    reference_changes = verify_structure(authority, isolated, proposed)
    verify_structure(current, composed, cumulative)
    envs=lambda b:re.findall(rb'\\(?:begin|end)\{[^}]*\}',b)
    require(envs(authority)==envs(isolated) and envs(current)==envs(composed),'Environment inventory changed')
    patch=patch_for(authority,isolated,name)
    cumulative_patch=patch_for(current,composed,name)
    replays=[replay_index(BASE,patch,isolated,name),replay_index(CURRENT,cumulative_patch,composed,name)]
    paths={f'{stem}_PENDING_SOURCE_REPAIRS_20260924.patch':patch,
           f'{stem}_PENDING_CUMULATIVE_REPAIRS_20260924.patch':cumulative_patch}
    receipt={'schema':'stacks-source-intake-review-replay/v1','source':name,'review':review_id,
        'authority':{'commit':BASE,'bytes':len(authority),'sha256':intake.digest(authority)},
        'current':{'commit':CURRENT,'bytes':len(current),'sha256':intake.digest(current)},
        'occurrence_coverage':{'reviewed':count,'received':count,'exactly_once':True},
        'review_groups':len(review['groups']),
        'disposition_counts':dict(Counter(g['disposition'] for g in review['groups'])),
        'new_proposed_units':sum(g['disposition'].startswith('accepted_missing_') for g in review['groups']),
        'new_operations':len(proposed),'already_composed_units':sorted(units),
        'existing_corrected_lines_retained':len(preserved),
        'cumulative_extra_lines_preserved':len(current_lines)-len(old_lines),
        'exact_inverse_replay_preserves_other_cumulative_bytes':True,
        'labels_citation_keys_environments':'All labels, citation keys and environments retained; seven proof references added',
        'reference_key_changes':reference_changes,
        'reference_key_change_policy':'Original targets retained; only the eight named references in the complete normal-decomposition proof are allowed in its replacement',
        'operations':proposed,'git_replays':replays,
        'patches':[{'path':p,'bytes':len(b),'sha256':intake.digest(b)} for p,b in paths.items()],
        'not_claimed':['new registry admission','source mutation','rendered chapter build',
                       'independent second review of the entire batch','human review','overall inventory completion']}
    paths[f'{stem}_INTAKE_REVIEW_REPLAY_20260924.json']=(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n').encode()
    return receipt,paths


def main():
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true')
    p.add_argument('--candidate-head',help='Explicit candidate-only descendant; reviewed source and overlay registry must be unchanged')
    a=p.parse_args()
    head=git('rev-parse','HEAD').decode().strip()
    if a.candidate_head:
        require(head==a.candidate_head,'Candidate HEAD drift')
        git('merge-base','--is-ancestor',CURRENT,head)
        for path in git('diff-tree','-r','--no-commit-id','--name-only',CURRENT,head).decode().splitlines():
            require(path=='ai-integrated/registry/leases.json' or path.startswith('ai-integrated/candidates/commons/stacks/errata/r57/'),'Not a candidate-only descendant: '+path)
    else:
        require(head==CURRENT,'HEAD advanced; rebind explicitly')
    model=intake.import_model()
    summaries=[]
    for name,count,existing in [('fields.tex',75,8)]:
        receipt,outputs=verify_one(name,count,existing,model)
        for filename,raw in outputs.items():
            target=HERE/filename
            if a.check:require(target.read_bytes()==raw,f'Non-deterministic output: {filename}')
            else:target.write_bytes(raw)
        summaries.append({k:v for k,v in receipt.items() if k not in ('operations','reference_key_changes')})
    print(json.dumps(summaries,indent=2))


if __name__=='__main__':main()
