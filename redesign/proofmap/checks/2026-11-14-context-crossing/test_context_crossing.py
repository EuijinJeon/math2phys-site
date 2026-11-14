"""고정 L 전달 원칙의 유한 예제와 잘못된 극한 추론의 반례.

합성 수열은 논문의 실제 항등식 오차가 아니다. 극한의 일반 논리만 시험한다.
"""
from fractions import Fraction
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent


def bad_order_error(L, N):
    """각 고정 L에서 결국 0, 각 고정 N에서 결국 1."""
    return int(N <= L)


def finite_errors(L, N):
    return [min(Fraction(1), Fraction(q + 1, N)) for q in range(L)]


class ContextCrossingTests(unittest.TestCase):
    def test_fixed_L_finite_maximum_eventually_small(self):
        # epsilon=max min(1,(q+1)/N) <= L/N; 원하는 오차 tau마다 N>L/tau.
        tau = Fraction(1, 100)
        for L in [2, 7, 29]:
            N = 100 * L + 1
            self.assertLess(max(finite_errors(L, N)), tau)

    def test_finite_normalized_average_is_bounded_by_maximum(self):
        for L in [3, 8, 17]:
            errors = finite_errors(L, 101)
            # 일부 regular 깊이만 쓰는 상황의 모형. 총 질량 <=1.
            domain = [q for q in range(L) if Fraction(1, 4) < Fraction(q, L) < Fraction(3, 4)]
            avg = sum((errors[q] for q in domain), Fraction(0)) / L
            self.assertLessEqual(Fraction(len(domain), L), 1)
            self.assertLessEqual(avg, max(errors))

    def test_fixed_L_amplification_disappears_with_N_first(self):
        for L in [2, 7, 29]:
            B = L**4  # J^{-1} 등의 L-의존 비용을 흉내 낸 합성 상수.
            tau = Fraction(1, 100)
            N = 100 * B * L + 1
            self.assertLess(B * max(finite_errors(L, N)), tau)

    def test_reversing_limits_is_not_licensed(self):
        # 정확한 threshold 성질: 고정 L에서는 N>L이면 0.
        # 고정 N에서는 L>=N이면 1. 두 반복 극한은 각각 0과 1이다.
        for L in [2, 10, 100]:
            self.assertEqual(bad_order_error(L, L + 1), 0)
        for N in [2, 10, 100]:
            self.assertEqual(bad_order_error(N, N), 1)
            self.assertEqual(bad_order_error(100 * N, N), 1)

    def test_joint_sequence_is_not_licensed(self):
        for L in [2, 10, 100, 1000]:
            self.assertEqual(bad_order_error(L, L), 1)

    def test_even_vanishing_raw_error_can_fail_after_amplification(self):
        for L in [2, 10, 100]:
            N, B = L**4, L**4
            raw_error = Fraction(1, N)
            self.assertEqual(B * raw_error, 1)
        # raw_error=1/N은 N→∞인 공동 수열에서 0으로 간다. 증폭 뒤에는 별개다.

    def test_context_packet_matches_actual_graph_interface(self):
        packet = json.loads((HERE / 'edge-packet.json').read_text())
        doc = json.loads((HERE.parents[1] / 'graphs/move4.json').read_text())
        top = doc['graphs'][0]
        edge = next(e for e in top['edges'] if e['id'] == 'top-e9')
        receiver = next(n for n in top['nodes'] if n['id'] == 'XM5')
        self.assertEqual(edge, packet['edge'])
        self.assertEqual(receiver, packet['receiver'])
        self.assertTrue(edge['complete'])
        self.assertEqual((edge['from'], edge['to']), ('R4', 'XM5'))
        self.assertIn('R4', receiver['inputs'])
        self.assertIn(packet['receiver_context'], top['contexts'])


if __name__ == '__main__':
    unittest.main()
