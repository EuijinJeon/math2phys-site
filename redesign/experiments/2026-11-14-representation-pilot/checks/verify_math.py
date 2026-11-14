"""Finite exact-arithmetic spot checks; does not grade reader prose."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

mu = F(1, 2)

def moment(xs):
    return mu ** sum(xs.count(a) % 2 for a in set(xs))

def step(states, direction):
    out = []
    for leaves, protected, factors, coefficient in states:
        for a in leaves:
            if a not in protected:
                out.append((leaves[:], protected | {a}, factors + ([a] if direction == 'X' else []), coefficient))
        new = max(leaves) + 1
        out.append((leaves + [new], protected | {new}, factors + ([new] if direction == 'X' else []), coefficient * -len(leaves)))
    return out

def value(states):
    return sum(c * moment(f) for _, _, f, c in states)

s0 = [([0, 1, 2], {0}, [1, 2], F(1))]
s1 = step(s0, 'X')
s2 = step(s1, '1')
q2 = step([([0, 1, 2], {0, 1}, [2], F(1))], 'X')
gammas = [F(-2,5), F(-6,5), F(-1,2), F(-3,10), F(-3,10), F(-3,10)]
result = {
    'Q1_first_history_terms': [str(c * moment(f)) for _, _, f, c in s1],
    'Q1_first': str(value(s1)),
    'Q1_mixed_history_count': len(s2),
    'Q1_mixed': str(value(s2)),
    'Q2_history_terms': [str(c * moment(f)) for _, _, f, c in q2],
    'Q2_first': str(value(q2)),
    'Q3_gammas': list(map(str, gammas)),
    'Q3_sum': str(sum(gammas)),
    'Q3_root_Q_probability': str(-gammas[0]/3),
    'Q6_extra_term': str(value(step([([0], {0}, [], F(1))], '1'))),
}
assert value(s1) == F(5,8)
assert value(s2) == F(-5,4)
assert value(q2) == F(1,4)
assert sum(gammas) == -3
assert -gammas[0]/3 == F(2,15)

# Signed-proposal expectation: enumerate every one/two-step branch, including
# conditional probability changes. For each branch p * multiplier == coefficient.
def proposal(states, direction):
    out = []
    for leaves, protected, factors, prob, weight in states:
        n = len(leaves)
        u = n - len(protected)
        M = n+u
        for a in leaves:
            if a not in protected:
                out.append((leaves[:], protected | {a}, factors + ([a] if direction=='X' else []), prob/F(M), weight*M))
        new = max(leaves)+1
        out.append((leaves+[new], protected|{new}, factors+([new] if direction=='X' else []), prob*F(n,M), -weight*M))
    return out

p0 = [([0,1,2],{0},[1,2],F(1),F(1))]
p2 = proposal(proposal(p0,'X'),'1')
pv = sum(p*w*moment(f) for _,_,f,p,w in p2)
assert sum(p for _,_,_,p,_ in p2) == 1
assert pv == value(s2)
result['C_two_step_proposal_expectation'] = str(pv)
result['C_two_step_proposal_second_moment_after_exact_path_average'] = str(sum(p*(w*moment(f))**2 for _,_,f,p,w in p2))
result['status'] = 'all exact-arithmetic assertions passed'
Path(__file__).with_name('math-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
