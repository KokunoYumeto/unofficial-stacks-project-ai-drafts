"""Compare all Stacks pages, including pagination added by the complete proof."""
import argparse
import json
from pathlib import Path
import re
import subprocess

from PIL import Image, ImageChops, ImageDraw
from r51_render_compare_20260922 import sha, ident, write


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--batch', type=Path, required=True)
    parser.add_argument('--poppler', required=True)
    parser.add_argument('--synctex', required=True)
    args = parser.parse_args()
    root = args.build.resolve()
    out = root / 'visual'
    out.mkdir()
    build = json.loads((root / 'BUILD_RECEIPT.json').read_bytes())
    prior_count, count = build['builds'][0]['pages'], build['builds'][1]['pages']
    assert count >= prior_count, 'Unexpected page reduction after the complete inserted proof'
    for role, expected in [('prior', prior_count), ('a', count)]:
        dest = out / role
        dest.mkdir()
        subprocess.run([args.poppler, '-r', '72', '-png', str(root/role/'stacks.pdf'), str(dest/'page')],
                       check=True, capture_output=True)
        assert len(list(dest.glob('page-*.png'))) == expected
    pages, changed = [], []
    for page in range(1, count+1):
        after_path = out/'a'/f'page-{page:0{len(str(count))}d}.png'
        with Image.open(after_path) as image:
            after = image.convert('RGB')
        if page <= prior_count:
            before_path = out/'prior'/f'page-{page:0{len(str(prior_count))}d}.png'
            with Image.open(before_path) as image:
                before = image.convert('RGB')
            assert before.size == after.size
            box = ImageChops.difference(before, after).getbbox()
            previous = sha(before.tobytes())
        else:
            box, previous = (0, 0, after.width, after.height), None
        pages.append({'page': page, 'prior': previous, 'successor': sha(after.tobytes()),
                      'changed_bbox': box, 'prior_same_number_exists': page <= prior_count})
        if box:
            changed.append(page)
    batch = json.loads(args.batch.read_bytes())
    source = next(row for row in batch['sources'] if row['source'] == 'stacks.tex')
    ops = source['rebound_operations']
    post = (root/'a'/'stacks.tex').read_bytes()
    assert sha(post) == source['prospective_cumulative_postimage']['sha256']
    loci = []
    for op in ops:
        preceding = [other for other in ops if other['end_byte_exclusive'] <= op['start_byte']]
        byte_delta = sum(len(other['replacement_text'].encode())-len(other['old_text'].encode()) for other in preceding)
        line_delta = sum(other['replacement_text'].count('\n')-other['old_text'].count('\n') for other in preceding)
        start = op['start_byte']+byte_delta
        replacement = op['replacement_text'].encode()
        assert post[start:start+len(replacement)] == replacement
        line = post[:start].count(b'\n')+1
        assert line == op['cumulative_line']+line_delta
        targets = []
        last = line+replacement.count(b'\n')
        # A full proof spans several pages. Query every source line of long
        # replacements so internal displays cannot be missed by endpoint maps.
        source_lines = range(line, last+1) if last-line > 15 else sorted({line, last})
        for source_line in source_lines:
            call = subprocess.run([args.synctex, 'view', '-i', f"{source_line}:1:{root/'a'/'stacks.tex'}",
                                   '-o', 'stacks.pdf'], cwd=root/'a', capture_output=True, text=True, check=True)
            for block in call.stdout.split('Page:')[1:]:
                page = int(block.splitlines()[0])
                assert 1 <= page <= count
                fields = dict(re.findall(r'^(x|y|h|v|W|H):([-\d.]+)', block, re.M))
                targets.append({'page': page, 'line': source_line, **{key: float(value) for key, value in fields.items()}})
        assert targets, op['operation_id']
        covered_pages = sorted({target['page'] for target in targets})
        loci.append({'operation_id': op['operation_id'], 'cumulative_line': op['cumulative_line'],
                     'postimage_line': line, 'postimage_byte': start, 'pages': covered_pages,
                     'queried_source_lines': list(source_lines), 'targets': targets})
    selected = sorted(set(changed) | {page for row in loci for page in row['pages']})
    high = out/'high'
    high.mkdir()
    pairs = []
    for page in selected:
        for role in (('prior', 'a') if page <= prior_count else ('a',)):
            subprocess.run([args.poppler, '-r', '150', '-f', str(page), '-l', str(page), '-singlefile',
                            '-png', str(root/role/'stacks.pdf'), str(high/f'{role}-{page}')], check=True, capture_output=True)
        with Image.open(high/f'a-{page}.png') as image:
            after = image.convert('RGB')
        if page <= prior_count:
            with Image.open(high/f'prior-{page}.png') as image:
                before = image.convert('RGB')
        else:
            before = Image.new('RGB', after.size, 'white')
            ImageDraw.Draw(before).text((40, 80), 'The prior edition has no page with this number.', fill='black')
        pair = Image.new('RGB', (before.width+after.width, max(before.height,after.height)+36), 'white')
        pair.paste(before, (0,36))
        pair.paste(after, (before.width,36))
        draw = ImageDraw.Draw(pair)
        draw.text((15,8), f'Stacks page {page}: prior page with the same number', fill='black')
        draw.text((before.width+15,8), 'R56 candidate; pagination may differ', fill='black')
        path = high/f'compare-{page}.png'
        pair.save(path)
        pairs.append({'page': page, 'image': path.relative_to(root).as_posix(), **ident(path.read_bytes())})
    result = {'schema': 'stacks-r56-page-comparison/v1', 'chapter': 'stacks.tex',
              'page_count': count, 'prior_page_count': prior_count, 'page_count_change': count-prior_count,
              'changed_pages': changed, 'unchanged_page_count': count-len(changed), 'pages': pages,
              'mapped_operations': loci, 'inspection_images': pairs,
              'prior_pdf': build['builds'][0]['pdf'], 'successor_pdf': build['builds'][1]['pdf'],
              'status': 'EXACT_PAGE_COMPARISON_COMPLETE_VISUAL_REVIEW_PENDING',
              'changed_pages_visual_review': 'not_performed',
              'line_mapping': 'Postimage byte and line independently recomputed after every preceding edit. Every line of the complete inserted proof was queried. Changed pagination is retained; all changed and added successor pages require visual inspection.'}
    write(out/'comparison.json', result)
    print(json.dumps({'prior_pages': prior_count, 'pages': count, 'changed': changed,
                      'inspect': selected, 'operations': len(loci)}), flush=True)


if __name__ == '__main__':
    main()
