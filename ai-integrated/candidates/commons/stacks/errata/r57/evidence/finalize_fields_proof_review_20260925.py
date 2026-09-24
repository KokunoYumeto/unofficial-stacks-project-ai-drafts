"""Bind the primary-reviewed complete proof before replay and candidate preparation."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def identity(name):
    raw = (HERE / name).read_bytes()
    return {'path': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest().upper()}

proof = identity('FIELDS_NORMAL_DECOMPOSITION_PROOF_20260925.tex')
check = identity('FIELDS_NORMAL_DECOMPOSITION_PROOF_CHECK_20260925.md')
receipt = {
    'schema': 'fields-normal-decomposition-primary-review/v1',
    'reviewer': 'OpenAI Codex - GPT-6 Astra, Ultra effort',
    'kind': 'Primary-session proof and source review; no independent worker or human review claimed',
    'proof': proof, 'proof_check': check,
    'authority_commit': 'a04446e57ec1fbc252a871afcec7752fb2807b14',
    'authority_sha256': '87E07F0373DC60CFC284E2F19078BC9BC7AB0B89C40EEF83941F6C38C765C549',
    'source_locator': 'fields.tex:3665-3681, lemma-normal-case',
    'status': 'COMPLETE_PRIMARY_PROOF_REVIEW',
    'checks': [
        'Fixed field equals the purely inseparable elements, including characteristic zero',
        'Finite orbit polynomial proves E/N separable for arbitrary algebraic E/F',
        'Normality and separability hypotheses checked against their actual source lemmas',
        'Compositum equality proved inside E using both separability and pure inseparability',
        'Canonical multiplication surjective and injective, with explicit inverse quotient maps',
        'Finite-support argument covers infinite algebraic extensions without cardinal cancellation',
        'All three external receiving uses read and their actual maps preserved',
        'Further generality and corollaries proved separately; no novelty claim',
    ],
    'rendered_build': 'Not yet run; mathematical reading does not certify layout',
}
name = 'FIELDS_NORMAL_DECOMPOSITION_PRIMARY_REVIEW_20260925.json'
(HERE / name).write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
path = HERE / 'FIELDS_INTAKE_REVIEW_20260924.json'
review = json.loads(path.read_bytes())
groups = {g['id']: g for g in review['groups']}
assert [o for o in groups['FIELDS-RECON-059']['operations'] if o['line'] == 3679][0]['replacement_text'] == (HERE / proof['path']).read_text(encoding='utf-8').rstrip('\n')
assert len([o for g in groups.values() for o in g['occurrences']]) == 75
assert review['next_source_start_line'] is None
review['mathematical_review_complete'] = True
review['mathematical_review_scope'] = 'Primary source review of this proposed correction batch; not an exhaustive certification of every unedited proof in Fields'
review['admission_state'] = 'Received review complete; no new allocation, source mutation, admission, build or publication'
review['required_proof_evidence'] = [proof, check, identity(name)]
review['dependency_groups'] = [{
    'id': 'normal-decomposition-prerequisites',
    'review_ids': ['FIELDS-RECON-033', 'FIELDS-RECON-034', 'FIELDS-RECON-038', 'FIELDS-RECON-059'],
    'required_together': True,
    'reason': 'Retain the corrected derivative dichotomy and separability transport proof, the precise separable-polynomial description, and the complete normal-decomposition proof together.',
}]
review['underclaims_review'] = {
    'source_statement': 'FIELDS-RECON-064 exposes the A-contained-in-B-contained-in-G property already proved in the source',
    'separate_consequences': check['path'],
    'proved': ['separable/purely-inseparable linear disjointness without normality', 'intersection of the two factors', 'both base-changed degrees, including infinite cardinals', 'canonical isomorphism of the Galois groups with their profinite topologies'],
    'source_additions_policy': 'Further consequences remain in the complete proof evidence; no new theorem is silently classified as a received defect',
}
path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'proof': proof, 'proof_check': check, 'review': identity(path.name)}))
