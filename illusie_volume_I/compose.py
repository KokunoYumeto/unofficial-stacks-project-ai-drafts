"""Mechanical bounded composition of the reviewed Volume I source fragments."""
from pathlib import Path
from illusie_volume_I.verify import START, END, BASE_SHA256, sha

root = Path(__file__).resolve().parents[1]
path = root / 'simplicial.tex'
source = path.read_bytes()
assert source.count(START) == source.count(END) == 1
before, rest = source.split(START)
_, after = rest.split(END)
assert sha(before + after) == BASE_SHA256, 'unrelated root edits must be preserved'
snippet = b'\n\n'.join((root / 'illusie_volume_I' / name).read_bytes().rstrip()
                       for name in ('relative-homotopy.tex', 'localization.tex')) + b'\n'
path.write_bytes(before + START + snippet + END + after)
print('Composed two fragments; outside-insertion bytes unchanged.')
