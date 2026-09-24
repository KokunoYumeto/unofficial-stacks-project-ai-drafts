"""Record completed mathematical reading and retain all supporting proof bytes."""
from collections import Counter
import json
from pathlib import Path

import reconcile_correction_occurrences_20260922 as intake
from verify_stacks_intake_review_20260924 import REQUIRED_PROOFS, verify_proof_evidence, require

HERE = Path(__file__).resolve().parent


def identity(name):
    raw = (HERE / name).read_bytes()
    return {'path': name, 'bytes': len(raw), 'sha256': intake.digest(raw)}


def write(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def main():
    review_path = HERE / 'STACKS_INTAKE_REVIEW_20260923.json'
    before = review_path.read_bytes()
    review = json.loads(before)
    require(len(review['groups']) == 77, 'Review group scope changed')
    require(sum(len(g['operations']) for g in review['groups']) == 86, 'Operation scope changed')
    proof = identity('LOCALIZED_CARTESIAN_DERIVATION_20260924.md')
    fragment = identity('STACKS_LOCALIZED_CARTESIAN_PROOF_20260924.tex')
    check = identity('STACKS_LOCALIZED_CARTESIAN_PROOF_CHECK_20260924.md')
    require(proof['sha256'] == '1AC4ABE855A5B259957BDEF9F2C1332C6622D4E4D5F0647504210FE388AEC562', 'Derivation drift')
    require(fragment['sha256'] == '70FCE1119BEED9A374306E537F7E35BB6DCE319030E3995BF31D66B3E5C70D87', 'Fragment drift')
    require(check['sha256'] == '48FF7117C41203EF16D23BF467BE6C0A9DF38609D9E925932276E4817422D652', 'Proof-check drift')
    receipt = {
        'schema': 'stacks-localized-cartesian-proof-review/v1',
        'reviewed_on': '2026-09-24',
        'reviewer': 'Primary session, after independent mathematical derivation',
        'authority_commit': review['authority_commit'],
        'current_commit': review['compared_public_commit'],
        'proof': proof, 'source_fragment': fragment, 'independent_fragment_check': check,
        'actual_reading': 'Complete derivation note read in three bounded intervals and checked; all 166 source-fragment lines read; original context 2990-3139 and dependent source 3273-3290 reread; complete independent fragment-check receipt read. Earlier source-context coverage is retained in the intake review.',
        'checks': {
            'counterexample_meets_category_and_site_hypotheses': True,
            'right_multiplicative_system_with_all_component_maps': True,
            'forward_cartesianness_used_without_converse_or_fibredness_circularity': True,
            'equalizer_refines_inverse_to_one_base_map': True,
            'both_inverse_identities_hold_after_common_admissible_refinement': True,
            'vertical_isomorphism_detection_with_actual_triples': True,
            'corrected_cartesian_criterion_both_directions': True,
            'arbitrary_chosen_roof_refinement': True,
            'dependent_cartesian_functor_argument_preserved': True,
            'no_additional_conservativity_or_saturation_assumption': True,
        },
        'dependent_source_review': {
            'source': 'stacks.tex', 'authority_lines': [3274, 3286],
            'result': 'The proof uses existence of a roof with cartesian numerator. The new complete criterion proves exactly that existence after refinement, and the original functor argument then applies. The separately recorded roof target, tuple, projection and grammatical repairs remain in the same required dependency group.',
        },
        'reading_limits': 'No independent audit of omitted mutual quasi-inverse checks or later stackification is claimed.',
        'source_mutations': 0, 'admission': False,
    }
    write('LOCALIZED_CARTESIAN_PRIMARY_REVIEW_20260924.json', receipt)
    review['mathematical_review_complete'] = True
    review['admission_state'] = 'All 114 received reports adjudicated and both independent mathematical repairs proved and checked. Proposals only; no canonical allocation, source mutation, admission, build or publication.'
    review['scope'] = 'All 114 received Stacks chapter reports adjudicated exactly once in 77 groups: 76 accepted proposed units with 86 exact operations, and one rejected grammar proposal. Independent discoveries remain separately attributed; no overall project completion claim.'
    review['independent_mathematical_derivations'][1].update({
        'state': 'Complete derivation and full fragment checked; primary session read both in full',
        'primary_review': 'LOCALIZED_CARTESIAN_PRIMARY_REVIEW_20260924.json',
        'independent_fragment_check': check['path'],
    })
    review['required_proof_evidence'] = [identity(name) for name in sorted(REQUIRED_PROOFS)]
    review['dependency_groups'] = [
        {'id': 'substack-fibre-condition', 'review_ids': ['STACKS-RECON-006', 'STACKS-RECON-066'],
         'required_together': True, 'reason': 'The Mor sheaf proof uses cartesian lifts in the full subcategory, supplied by the corrected fibre-isomorphism hypothesis and its complete proof.'},
        {'id': 'localized-cartesian-criterion',
         'review_ids': [f'STACKS-RECON-{n:03d}' for n in list(range(44, 66)) + list(range(67, 72)) + [77]],
         'required_together': True, 'reason': 'The complete refinement criterion uses the corrected multiplicative-system and forward-cartesianness arguments, and supplies the roof existence used by the corrected adjointness proof.'},
    ]
    verify_proof_evidence(review)
    archive = HERE / 'STACKS_INTAKE_REVIEW_BEFORE_PROOF_FINALIZATION_20260924.json'
    if not archive.exists():
        archive.write_bytes(before)
    write(review_path.name, review)
    print(json.dumps({'review': identity(review_path.name), 'groups': 77, 'operations': 86,
                      'classes': dict(Counter(g['disposition'] for g in review['groups'])),
                      'required_proof_files': len(review['required_proof_evidence']),
                      'source_mutations': 0}))


if __name__ == '__main__':
    main()
