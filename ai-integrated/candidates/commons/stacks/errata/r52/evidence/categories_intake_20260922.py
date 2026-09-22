"""Bounded primary-source display for the received Categories reports."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path('C:/Users/Floris/Documents/interlanguage/worktrees/unofficial-ai-stacks-r47-illusie-linear-successor-20260907')
INVENTORY = Path('C:/Users/Floris/Documents/interlanguage/03_projects/language_management/cjk/00_lane_control/multilingual_reader_20260922/CORRECTION_OCCURRENCES.jsonl')
BASE = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
CURRENT = '0755a4cee48442859b7ec315c581108a12445663'

def sha(raw):
    return hashlib.sha256(raw).hexdigest().upper()

def inputs():
    raw = INVENTORY.read_bytes()
    assert sha(raw) == '53667E865189AF21A0E0132B6CB670E9E6D83B9B5996F8EF1D3D903E8E56F56B'
    records = [json.loads(line) for line in raw.splitlines()]
    triage = [json.loads(line) for line in (HERE / 'CORRECTION_OCCURRENCE_TRIAGE_20260922.jsonl').read_bytes().splitlines()]
    triage = [row for row in triage if row['source'] == 'categories.tex']
    authority = subprocess.check_output(['git', '-C', str(ROOT), 'show', f'{BASE}:categories.tex'])
    assert sha(authority) == '62F7611AF4C3FEEBD041DB4728B42C7112004CFBB9FA5ECB643C6F5D90DB3F25'
    return records, triage, authority

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    p = argparse.ArgumentParser(); p.add_argument('--first', type=int, required=True); p.add_argument('--last', type=int, required=True)
    a = p.parse_args(); records, triage, authority = inputs()
    selected = [r for r in triage if a.first <= min(lo for lo, hi in r['ranges']) <= a.last]
    for row in sorted(selected, key=lambda r: (r['ranges'][0][0], r['inventory_line'])):
        record = records[row['inventory_line'] - 1]['source_record']
        print(json.dumps({'occurrence': row['occurrence_id'], 'producer_id': row['producer_id'], 'ranges': row['ranges'], 'record': record}, ensure_ascii=False))
    lines = authority.decode().splitlines(); intervals = []
    for row in selected:
        for lo, hi in row['ranges']:
            intervals.append((max(1, lo-8), min(len(lines), hi+8)))
    merged = []
    for lo, hi in sorted(intervals):
        if merged and lo <= merged[-1][1]+1:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    for lo, hi in merged:
        print(f'PRIMARY SOURCE categories.tex:{lo}-{hi}')
        print('\n'.join(f'{i}: {lines[i-1]}' for i in range(lo, hi+1)))
    print('PHYSICAL REPORTS DISPLAYED', len(selected))

if __name__ == '__main__':
    main()
