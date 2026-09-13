"""Finite free-simplex checks of the formulas in relative-homotopy.tex.

These are regression tests, not substitutes for the proof for all degrees.
Tuples encode actual ordinal maps, including degenerate simplices.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
import unittest


def add(*terms):
    result = Counter()
    for coefficient, vector in terms:
        for basis, value in vector.items():
            result[basis] += coefficient * value
    return {basis: value for basis, value in result.items() if value}


def unit(a, b):
    return {(tuple(a), tuple(b)): 1}


def linear(vector, fn):
    return add(*((value, fn(*basis)) for basis, value in vector.items()))


def boundary(kind, a, b):
    terms = []
    if kind == 'C':
        if len(a) > 1:
            terms = [((-1)**i, unit(a[:i]+a[i+1:], b[:i]+b[i+1:]))
                     for i in range(len(a))]
    else:
        if len(a) > 1:
            terms += [((-1)**i, unit(a[:i]+a[i+1:], b)) for i in range(len(a))]
        if len(b) > 1:
            terms += [((-1)**(len(a)-1+i), unit(a, b[:i]+b[i+1:]))
                      for i in range(len(b))]
    return add(*terms)


def aw(a, b):
    return add(*((1, unit(a[:p+1], b[p:])) for p in range(len(a))))


def sh(a, b):
    p, q = len(a)-1, len(b)-1
    terms = []
    for horizontal in combinations(range(p+q), p):
        x, y, inv = 0, 0, 0
        aa, bb = [a[0]], [b[0]]
        for i in range(p+q):
            if i in horizontal:
                inv += y
                x += 1
            else:
                y += 1
            aa.append(a[x])
            bb.append(b[y])
        terms.append(((-1)**inv, unit(aa, bb)))
    return add(*terms)


def difference(kind, a, b):
    composite = linear(aw(a, b), sh) if kind == 'C' else linear(sh(a, b), aw)
    return add((1, composite), (-1, unit(a, b)))


def contract(kind, a, b):
    if kind == 'C':
        return unit((0,)+a, (0,)+b)
    terms = [(1, unit((0,)+a, b))]
    if len(a) == 1:
        terms.append((1, unit((0,), (0,)+b)))
    return add(*terms)


@lru_cache(None)
def universal_h(kind, p, q):
    degree = p if kind == 'C' else p+q
    if degree == 0:
        return {}
    a, b = tuple(range(p+1)), tuple(range(q+1))
    r = add((1, difference(kind, a, b)),
            (-1, linear(boundary(kind, a, b), lambda x, y: homotopy(kind, x, y))))
    assert not linear(r, lambda x, y: boundary(kind, x, y)), 'residual is not a cycle'
    return linear(r, lambda x, y: contract(kind, x, y))


def homotopy(kind, a, b):
    universal = universal_h(kind, len(a)-1, len(b)-1)
    return linear(universal, lambda u, v: unit([a[i] for i in u], [b[j] for j in v]))


class ShuffleRegression(unittest.TestCase):
    def test_constant_degree_one_rejects_strict_identity(self):
        self.assertEqual(linear(sh((0, 0), (0,)), aw),
                         {((0, 0), (0,)): 1, ((0,), (0, 0)): 1})
        self.assertNotEqual(linear(sh((0, 0), (0,)), aw), unit((0, 0), (0,)))

    def test_chain_maps_on_universal_simplices_through_degree_four(self):
        for n in range(5):
            a = tuple(range(n+1))
            self.assertEqual(linear(aw(a, a), lambda x, y: boundary('T', x, y)),
                             linear(boundary('C', a, a), aw))
            for p in range(n+1):
                a, b = tuple(range(p+1)), tuple(range(n-p+1))
                self.assertEqual(linear(sh(a, b), lambda x, y: boundary('C', x, y)),
                                 linear(boundary('T', a, b), sh))

    def test_recursive_homotopies_through_degree_four(self):
        for kind in ('C', 'T'):
            for n in range(5):
                degrees = [(n, n)] if kind == 'C' else [(p, n-p) for p in range(n+1)]
                for p, q in degrees:
                    a, b = tuple(range(p+1)), tuple(range(q+1))
                    lhs = add((1, linear(homotopy(kind, a, b),
                                         lambda x, y: boundary(kind, x, y))),
                              (1, linear(boundary(kind, a, b),
                                         lambda x, y: homotopy(kind, x, y))))
                    self.assertEqual(lhs, difference(kind, a, b), (kind, p, q))


if __name__ == '__main__':
    unittest.main()
