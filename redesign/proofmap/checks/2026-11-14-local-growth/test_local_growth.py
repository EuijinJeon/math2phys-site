"""fresh path의 유한 kernel 검산과 국소 확장 범위 검사."""
import itertools
import json
import math
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def example(t=0.19):
    m = 0.43
    K1 = [0.37, 0.63]
    K2 = [[0.28, 0.72], [0.61, 0.39]]
    D = [[-0.8, 1.1], [0.3, -0.5]]
    A = [[1 + t * v for v in row] for row in D]
    Y1 = [sum(k * a for k, a in zip(ks, aa)) for ks, aa in zip(K2, A)]
    Y0 = sum(k * y**m for k, y in zip(K1, Y1))**(1 / m)
    q1 = [k * (y / Y0)**m for k, y in zip(K1, Y1)]
    q2 = [[k * a / y for k, a in zip(ks, aa)] for ks, aa, y in zip(K2, A, Y1)]
    lhs, rhs, new_coeff_rhs, worst_density_error = 0.0, 0.0, 0.0, 0.0
    signs = [-1, 1]
    for z, w, a, b, c in itertools.product(range(2), repeat=5):
        old_prob = q1[z] * q2[z][a] * q2[z][b] * q1[w] * q2[w][c]
        G = 1 + 0.7 * signs[a] * signs[b] * signs[c] + 0.2 * z * signs[b]
        H = G / A[z][a]  # C={a}; G uses siblings and a different root branch.
        derivative = sum(k * v for k, v in zip(K2[z], D[z])) / Y1[z]
        gamma_old, gamma_new = m - 2, m - 3
        lhs += gamma_old * old_prob * H * derivative
        for x in range(2):
            h = D[z][x] / A[z][x]
            fresh_prob = old_prob * q2[z][x]
            rhs += gamma_old * fresh_prob * H * h
            new_coeff_rhs += gamma_new * fresh_prob * H * h
            base_prob = K1[z] * K2[z][a] * K2[z][b] * K1[w] * K2[w][c] * K2[z][x]
            Wplus = (A[z][a] * A[z][b] * A[w][c] * A[z][x]
                     * Y0**(-2 * m) * Y1[z]**(m - 3) * Y1[w]**(m - 1))
            worst_density_error = max(worst_density_error, abs(fresh_prob - base_prob * Wplus))
    return {'lhs': lhs, 'rhs': rhs, 'wrong_new_coefficient_rhs': new_coeff_rhs,
            'density_error': worst_density_error, 'Y1': Y1, 'q1': q1, 'q2': q2}


class LocalGrowthTests(unittest.TestCase):
    def test_old_tree_internal_contribution_equals_fresh_protected_term(self):
        for t in [-0.2, 0, 0.19, 0.4]:
            r = example(t)
            self.assertAlmostEqual(r['lhs'], r['rhs'], places=12)

    def test_updated_sampling_matches_density_formula(self):
        self.assertLess(example()['density_error'], 1e-14)

    def test_old_coefficient_must_not_be_replaced(self):
        r = example()
        self.assertGreater(abs(r['lhs'] - r['wrong_new_coefficient_rhs']), 1e-3)

    def test_first_variation_by_finite_difference(self):
        h, t = 1e-6, 0.19
        lo, hi, middle = example(t-h), example(t+h), example(t)
        D, K2 = [[-0.8, 1.1], [0.3, -0.5]], [[0.28, 0.72], [0.61, 0.39]]
        for z in range(2):
            actual = (math.log(hi['Y1'][z]) - math.log(lo['Y1'][z])) / (2*h)
            expected = sum(k*v for k,v in zip(K2[z], D[z])) / middle['Y1'][z]
            self.assertAlmostEqual(actual, expected, places=8)

    def test_boundary_and_local_growth_counts(self):
        doc = json.loads((ROOT/'graphs/move4.json').read_text())
        before = json.loads((HERE/'baseline-inventory.json').read_text())
        after = json.loads((HERE/'after-inventory.json').read_text())
        self.assertEqual(set(after)-set(before), {'fresh'})
        added = [(gid,e) for gid,g in after.items() for e in g['edges']
                 if e not in before.get(gid,{}).get('edges',{})]
        self.assertEqual(len(added), 11)
        changed = {gid for gid in before if before[gid] != after[gid]}
        self.assertEqual(changed, {'top','diff'})
        fresh = next(g for g in doc['graphs'] if g['id']=='fresh')
        self.assertEqual({n['external_ref'] for n in fresh['nodes'] if n['kind']=='external'},
                         {'XO','D1','D2','S1'})
        self.assertTrue(all(n.get('status')=='complete' for n in fresh['nodes'] if n['kind']=='step'))


if __name__ == '__main__':
    unittest.main()
