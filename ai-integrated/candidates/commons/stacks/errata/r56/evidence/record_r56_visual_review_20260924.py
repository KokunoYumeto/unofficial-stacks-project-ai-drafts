"""Record the primary session's completed page and correction-locus inspection."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = HERE/'r56-build-stacks-20260924'
comparison = json.loads((BUILD/'visual/comparison.json').read_bytes())
expected = [1,3,4,5,7,8,9,11,12,13,14,15,17,18,19,20,21,22,24,26,27,28,29,30,31,32,33,34,35,36,37,38]
assert [item['page'] for item in comparison['inspection_images']] == expected
assert comparison['page_count'] == 38 and comparison['prior_page_count'] == 36
assert comparison['unchanged_page_count'] == 6 and len(comparison['mapped_operations']) == 86
files = [BUILD/'visual/inspection'/f'layout-{n:02d}.png' for n in range(1,9)]
files += [BUILD/'visual/inspection'/f'loci-{n:02d}.png' for n in range(1,10)]
files += [BUILD/'visual/high/a-26.png']
identities = [{'path':file.relative_to(BUILD).as_posix(), 'bytes':file.stat().st_size,
               'sha256':hashlib.sha256(file.read_bytes()).hexdigest().upper()} for file in files]
notes = ('Inspected all 32 changed or added successor pages in eight complete-page layout sheets, '
         'and all 86 mapped operations in nine correction-locus sheets. The complete 166-line localization proof '
         'was rendered on pages 30-32 and inspected including both inverse identities, all maps, and its beginning and ending across page boundaries. '
         'Page 26 was additionally inspected at full size for the inherited 6.43765-point overfull formula: the formula is legible and unclipped. '
         'No new overlap, clipped formula, missing glyph, damaged diagram or pagination defect was found. '
         'Six unchanged pages have exact pixel equality and are not claimed to have a new mathematical review. '
         'The prior chapter has 36 pages and the successor 38; the additional pagination preserves the complete proof. '
         'The one inherited overfull box and missing external-chapter references remain recorded, unchanged; these PDFs are isolated chapter checks.')
result = {'stacks': {'passed':True, 'pages':expected, 'notes':notes,
                     'inspected_artifacts':identities, 'actual_inspection':'Primary session displayed and inspected every listed image.',
                     'human_review':False, 'new_mathematical_certification_of_unedited_text':False}}
(HERE/'R56_ACTUAL_VISUAL_REVIEW_20260924.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'visual':'PASS', 'pages':len(expected), 'operations':86, 'inspected_images':len(files)}))
