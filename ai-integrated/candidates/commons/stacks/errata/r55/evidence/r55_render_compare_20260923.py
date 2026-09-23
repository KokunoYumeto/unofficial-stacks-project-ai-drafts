"""R55 page comparison with exact post-edit source-line mapping for every operation."""
import argparse
import json
from pathlib import Path
import re
import subprocess
from PIL import Image, ImageChops, ImageDraw
from r51_render_compare_20260922 import sha, ident, write

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--chapter', choices=['sites.tex'], required=True)
    p.add_argument('--build', type=Path, required=True)
    p.add_argument('--batch', type=Path, required=True)
    p.add_argument('--poppler', required=True)
    p.add_argument('--synctex', required=True)
    a = p.parse_args(); root = a.build.resolve(); out = root/'visual'; stem = a.chapter[:-4]
    out.mkdir()
    build = json.loads((root/'BUILD_RECEIPT.json').read_bytes())
    n = build['builds'][0]['pages']; pages = []; changed = []
    assert n == build['builds'][1]['pages']
    for role in ('prior', 'a'):
        dest = out/role; dest.mkdir()
        subprocess.run([a.poppler, '-r', '72', '-png', str(root/role/(stem+'.pdf')), str(dest/'page')], check=True, capture_output=True)
        assert len(list(dest.glob('page-*.png'))) == n
    for i in range(1, n+1):
        name = f'page-{i:0{len(str(n))}d}.png'
        with Image.open(out/'prior'/name) as before, Image.open(out/'a'/name) as after:
            assert before.size == after.size
            box = ImageChops.difference(before.convert('RGB'), after.convert('RGB')).getbbox()
            pages.append({'page': i, 'prior': sha(before.tobytes()), 'successor': sha(after.tobytes()), 'changed_bbox': box})
            if box: changed.append(i)
    source = next(row for row in json.loads(a.batch.read_bytes())['sources'] if row['source'] == a.chapter)
    ops = source['rebound_operations']; loci = []
    post = (root/'a'/a.chapter).read_bytes()
    for op in ops:
        preceding = [x for x in ops if x['end_byte_exclusive'] <= op['start_byte']]
        byte_delta = sum(len(x['replacement_text'].encode())-len(x['old_text'].encode()) for x in preceding)
        line_delta = sum(x['replacement_text'].count('\n')-x['old_text'].count('\n') for x in preceding)
        start = op['start_byte'] + byte_delta; replacement = op['replacement_text'].encode()
        assert post[start:start+len(replacement)] == replacement
        line = post[:start].count(b'\n') + 1
        assert line == op['cumulative_line'] + line_delta
        targets = []
        for at in sorted({line, line + replacement.count(b'\n')}):
            call = subprocess.run([a.synctex, 'view', '-i', f"{at}:1:{root/'a'/a.chapter}", '-o', (stem+'.pdf')], cwd=root/'a', capture_output=True, text=True, check=True)
            for block in call.stdout.split('Page:')[1:]:
                page = int(block.splitlines()[0]); assert 1 <= page <= n
                fields = dict(re.findall(r'^(x|y|h|v|W|H):([-\d.]+)', block, re.M))
                targets.append({'page': page, 'line': at, **{k:float(v) for k,v in fields.items()}})
        assert targets, op['operation_id']
        loci.append({'operation_id': op['operation_id'], 'cumulative_line': op['cumulative_line'],
            'postimage_line': line, 'postimage_byte': start, 'pages': sorted({t['page'] for t in targets}), 'targets': targets})
    selected = sorted(set(changed) | {page for row in loci for page in row['pages']})
    high = out/'high'; high.mkdir(); pairs = []
    for page in selected:
        for role in ('prior', 'a'):
            subprocess.run([a.poppler, '-r', '150', '-f', str(page), '-l', str(page), '-singlefile', '-png', str(root/role/(stem+'.pdf')), str(high/f'{role}-{page}')], check=True, capture_output=True)
        with Image.open(high/f'prior-{page}.png') as before, Image.open(high/f'a-{page}.png') as after:
            pair = Image.new('RGB', (before.width+after.width, after.height+36), 'white')
            pair.paste(before, (0,36)); pair.paste(after, (before.width,36))
            draw = ImageDraw.Draw(pair); draw.text((15,8), f'{stem.title()} page {page}: prior', fill='black')
            draw.text((before.width+15,8), 'R55 candidate', fill='black')
            path = high/f'compare-{page}.png'; pair.save(path)
            pairs.append({'page': page, 'image': path.relative_to(root).as_posix(), **ident(path.read_bytes())})
    result = {'schema': 'stacks-r55-page-comparison/v1', 'chapter': a.chapter, 'page_count': n,
        'changed_pages': changed, 'unchanged_page_count': n-len(changed), 'pages': pages,
        'mapped_operations': loci, 'inspection_images': pairs, 'prior_pdf': build['builds'][0]['pdf'],
        'successor_pdf': build['builds'][1]['pdf'], 'status': 'EXACT_PAGE_COMPARISON_COMPLETE_VISUAL_REVIEW_PENDING',
        'changed_pages_visual_review': 'not_performed',
        'line_mapping': 'Postimage byte and source line independently recomputed after every preceding edit; both ends of multiline replacements queried.'}
    write(out/'comparison.json', result)
    print(json.dumps({'pages':n, 'changed':changed, 'inspect':selected, 'operations':len(loci)}), flush=True)

if __name__ == '__main__': main()
