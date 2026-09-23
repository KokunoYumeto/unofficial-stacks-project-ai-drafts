"""Read-only, hash-bound display of the next received source reports."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import reconcile_correction_occurrences_20260922 as helpers

HERE = Path(__file__).resolve().parent
ROOT = helpers.PROD
BASE = helpers.BASE
CURRENT = 'b74477a0946b25f33e4485c6948389155e136675'
HASHES = {'sheaves.tex': 'AC4F9EDC7DB85E66329806EC9EA42816187A469772844BAEA663E1C9A9F00B38'}


def inputs(source):
    raw = (helpers.INTAKE / 'CORRECTION_OCCURRENCES.jsonl').read_bytes()
    assert helpers.digest(raw) == helpers.EXPECTED_RECORDS
    reports = []
    for n, line in enumerate(raw.splitlines(), 1):
        row = json.loads(line)
        if helpers.source_name(row) == source:
            reports.append((f'OCC-{n:05d}', row, helpers.locus_ranges(row)))
    authority = subprocess.check_output(['git', '-C', str(ROOT), 'show', f'{BASE}:{source}'])
    assert helpers.digest(authority) == HASHES[source]
    return reports, authority


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    p = argparse.ArgumentParser()
    p.add_argument('--source', choices=HASHES, default='sheaves.tex')
    p.add_argument('--first', type=int, default=1)
    p.add_argument('--last', type=int, required=True)
    p.add_argument('--context', type=int, default=7)
    p.add_argument('--source-only', action='store_true')
    a = p.parse_args()
    reports, authority = inputs(a.source)
    selected = [r for r in reports if r[2] and a.first <= min(lo for lo, hi in r[2]) <= a.last]
    omitted_metadata = {'timestamp_utc','source_path','source_file','source','source_sha256','authority_sha256','status','translation_impact'}
    if not a.source_only:
        for oid, row, spans in sorted(selected, key=lambda r:(r[2][0][0],r[0])):
            record = {k:v for k,v in helpers.source_record(row).items() if k not in omitted_metadata}
            print(json.dumps({'occurrence':oid,'ranges':spans,'record':record,'historical_ids':helpers.historical_ids(row)},ensure_ascii=False))
    lines = authority.decode().splitlines()
    intervals = [(max(1,lo-a.context),min(len(lines),hi+a.context)) for _,_,spans in selected for lo,hi in spans]
    if a.source_only:
        intervals = [(a.first,min(a.last,len(lines)))]
    merged = []
    for lo,hi in sorted(intervals):
        if merged and lo <= merged[-1][1]+1:
            merged[-1][1] = max(merged[-1][1],hi)
        else:
            merged.append([lo,hi])
    for lo,hi in merged:
        print(f'PRIMARY {a.source}:{lo}-{hi}')
        print('\n'.join(f'{n}: {lines[n-1]}' for n in range(lo,hi+1)))
    print('REPORTS',len(selected),'TOTAL',len(reports),'AUTHORITY_SHA256',helpers.digest(authority))


if __name__ == '__main__':
    main()
