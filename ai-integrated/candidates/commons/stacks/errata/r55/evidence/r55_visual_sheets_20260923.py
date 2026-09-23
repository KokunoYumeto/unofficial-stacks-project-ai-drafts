"""Make bounded, readable page-layout sheets and precise corrected-region strips."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('--build', type=Path, required=True)
args = parser.parse_args()
ROOT = args.build.resolve()/'visual'
comparison = json.loads((ROOT/'comparison.json').read_bytes())
pages = [r['page'] for r in comparison['inspection_images']]
dest = ROOT/'inspection'; dest.mkdir(exist_ok=True)
for start in range(0, len(pages), 4):
    selected = pages[start:start+4]
    sheet = Image.new('RGB', (1530, 2040), 'white')
    for i, page in enumerate(selected):
        with Image.open(ROOT/'high'/f'a-{page}.png') as im:
            im.thumbnail((765,990), Image.Resampling.LANCZOS)
            x, y = (i%2)*765, (i//2)*1020
            sheet.paste(im,(x,y+30))
            ImageDraw.Draw(sheet).text((x+10,y+10),f"R55 {comparison['chapter']} page {page}",fill='black')
    sheet.save(dest/f'layout-{start//4+1:02d}.png')

# The original source and mathematical review remain the authority; these strips
# inspect rendering of the exact mapped replacement loci and their context.
regions = []
for item in comparison['mapped_operations']:
    for target in item['targets']:
        regions.append((target['page'], target.get('y',target.get('v',0)),item['operation_id']))
by_page = {}
for page,y,oid in regions:
    by_page.setdefault(page,[]).append((y,oid))
strips=[]
for page, rows in sorted(by_page.items()):
    bands=[]
    for y,oid in sorted(rows):
        lo,hi=max(0,int(y*150/72)-85),int(y*150/72)+105
        if bands and lo <= bands[-1][1]:
            bands[-1][1]=max(hi,bands[-1][1]);bands[-1][2].add(oid)
        else:bands.append([lo,hi,{oid}])
    with Image.open(ROOT/'high'/f'a-{page}.png') as im:
        for lo,hi,ids in bands:
            crop=im.crop((0,lo,im.width,min(hi,im.height)))
            strip=Image.new('RGB',(im.width,crop.height+28),'white')
            strip.paste(crop,(0,28))
            ImageDraw.Draw(strip).text((10,6),f'Page {page}: '+', '.join(sorted(ids)),fill='black')
            strips.append(strip)
sheet_number=1; pending=[];height=0
for strip in strips:
    if height+strip.height>2400 and pending:
        sheet=Image.new('RGB',(max(s.width for s in pending),height),'white');y=0
        for s in pending:sheet.paste(s,(0,y));y+=s.height
        sheet.save(dest/f'loci-{sheet_number:02d}.png');sheet_number+=1;pending=[];height=0
    pending.append(strip);height+=strip.height
if pending:
    sheet=Image.new('RGB',(max(s.width for s in pending),height),'white');y=0
    for s in pending:sheet.paste(s,(0,y));y+=s.height
    sheet.save(dest/f'loci-{sheet_number:02d}.png')
print(json.dumps({'layout_sheets':(len(pages)+3)//4,'locus_sheets':sheet_number,'pages':len(pages),'operations':len(comparison['mapped_operations'])}))
