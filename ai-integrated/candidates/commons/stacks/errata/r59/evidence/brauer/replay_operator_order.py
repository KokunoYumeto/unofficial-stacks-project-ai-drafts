"""Recheck the retained exact left/right multiplication certificate without writing."""
import hashlib
import json
from pathlib import Path
import sympy as s

C = Path(__file__).resolve().parent
receipt = json.loads((C / 'BRAUER_OPERATOR_ORDER_CHECK_20260930.json').read_bytes())
assert hashlib.sha256((C / 'PROOFS.md').read_bytes()).hexdigest().upper() == receipt['proof_sha256']
I = s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
J = s.Matrix([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
RI = s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,1],[0,0,-1,0]])
RJ = s.Matrix([[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]])
L = [s.eye(4), I, J, I*J]
R = [s.eye(4), RI, RJ, RJ*RI]
table = [[(1,0),(1,1),(1,2),(1,3)],
         [(1,1),(-1,0),(1,3),(-1,2)],
         [(1,2),(-1,3),(-1,0),(1,1)],
         [(1,3),(1,2),(-1,1),(-1,0)]]
assert [m.tolist() for m in L] == receipt['left_operators']
assert [m.tolist() for m in R] == receipt['right_operators']
for a in range(4):
    for b in range(4):
        sign, index = table[a][b]
        assert L[a]*L[b] == sign*L[index]
        assert R[b]*R[a] == sign*R[index]
        assert L[a]*R[b] == R[b]*L[a]
        expected = dict(left=a, right=b, product_sign=sign, product_basis=index,
                        left_composition_exact=True, right_reversed_composition_exact=True,
                        actions_commute=True)
        assert receipt['all_sixteen_ordered_basis_products'][4*a+b] == expected
assert RI*RJ == -R[3] and RJ*RI == R[3] and R[3] != -R[3]
print(json.dumps(dict(result='PASS_RETAINED_OPERATOR_CERTIFICATE', ordered_products=16,
                      exact_identities=48, source_or_receipt_changed=False)))
