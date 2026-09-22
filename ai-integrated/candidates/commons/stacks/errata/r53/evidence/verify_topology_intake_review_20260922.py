"""Exact proposal replay for Topology/Introduction; no source/registry writes."""
import argparse
from collections import Counter
import difflib
import itertools
import json
import re
import sys

import topology_intake_20260922 as source
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


def verify_one(name, count, existing_count, model):
    stem = name.removesuffix('.tex').upper()
    review, review_id = intake.loaded(HERE / f'{stem}_INTAKE_REVIEW_20260922.json')
    received, authority = source.inputs(name)
    expected = {oid for oid, _, _ in received}
    actual = [o for g in review['groups'] for o in g['occurrences']]
    require(len(expected) == count, 'Received count changed')
    require(len(actual) == len(set(actual)) and set(actual) == expected,
            f'{name} coverage mismatch: missing={sorted(expected-set(actual))}, extra={sorted(set(actual)-expected)}')
    require(review['next_source_start_line'] is None, 'Review incomplete')
    require(review['authority_commit'] == BASE and review['compared_public_commit'] == CURRENT,
            'Review revision mismatch')
    require(review['inventory_sha256'] == intake.EXPECTED_RECORDS, 'Inventory identity mismatch')
    require(review['authority_sha256'] == intake.digest(authority), 'Authority identity mismatch')
    current = git('show', f'{CURRENT}:{name}')
    require((ROOT/name).read_bytes().replace(b'\r\n', b'\n') == current, 'Working source differs')
    units = {u.stable_id:u for u in model.units if u.source == name}
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
            line = lines[op['line']-1]
            old,new = op['old_text'].encode(),op['replacement_text'].encode()
            require(old and old != new and line.count(old) == 1,
                    f'Nonunique/wrong preimage {group["id"]} line {op["line"]}: {op["old_text"]!r}')
            start = offsets[op['line']-1]+line.index(old)
            end = start+len(old)
            mapped = mapping.get(op['line']-1)
            require(mapped is not None and current_lines[mapped] == line,
                    f'Target line changed in cumulative source: {group["id"]}')
            current_start = current_offsets[mapped]+line.index(old)
            overlaps = sorted({u.stable_id for u in units.values() for o in u.operations
                if o.start_byte < end and start < o.end_byte_exclusive})
            proposed.append({'review_id':group['id'],'occurrences':group['occurrences'],**op,
                'start_byte':start,'end_byte_exclusive':end,
                'old_sha256':intake.digest(old),'replacement_sha256':intake.digest(new),
                'admitted_context_envelope_overlaps':overlaps,
                'current_line':mapped+1,'current_start_byte':current_start})
            cumulative.append({**op,'start_byte':current_start,'end_byte_exclusive':current_start+len(old)})
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
    require(structure(authority)==structure(isolated) and structure(current)==structure(composed),
            'Reference/label/citation-key inventory changed')
    envs=lambda b:re.findall(rb'\\(?:begin|end)\{[^}]*\}',b)
    require(envs(authority)==envs(isolated) and envs(current)==envs(composed),'Environment inventory changed')
    patch=patch_for(authority,isolated,name)
    cumulative_patch=patch_for(current,composed,name)
    replays=[replay_index(BASE,patch,isolated,name),replay_index(CURRENT,cumulative_patch,composed,name)]
    paths={f'{stem}_PENDING_SOURCE_REPAIRS_20260922.patch':patch,
           f'{stem}_PENDING_CUMULATIVE_REPAIRS_20260922.patch':cumulative_patch}
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
        'labels_references_citation_keys_environments':'UNCHANGED',
        'operations':proposed,'git_replays':replays,
        'patches':[{'path':p,'bytes':len(b),'sha256':intake.digest(b)} for p,b in paths.items()],
        'not_claimed':['new registry admission','source mutation','rendered chapter build',
                       'second-agent/human review','overall inventory completion']}
    paths[f'{stem}_INTAKE_REVIEW_REPLAY_20260922.json']=(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n').encode()
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
            require(path=='ai-integrated/registry/leases.json' or path.startswith('ai-integrated/candidates/commons/stacks/errata/r53/'),'Not a candidate-only descendant: '+path)
    else:
        require(head==CURRENT,'HEAD advanced; rebind explicitly')
    model=intake.import_model()
    summaries=[]
    for name,count,existing in [('introduction.tex',1,0),('topology.tex',151,37)]:
        receipt,outputs=verify_one(name,count,existing,model)
        for filename,raw in outputs.items():
            target=HERE/filename
            if a.check:require(target.read_bytes()==raw,f'Non-deterministic output: {filename}')
            else:target.write_bytes(raw)
        summaries.append({k:v for k,v in receipt.items() if k!='operations'})
    print(json.dumps(summaries,indent=2))


if __name__=='__main__':main()
