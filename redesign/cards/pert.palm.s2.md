---
id: pert:palm.s2
kind: step
title: '(6.16)과 $H_N$ 의 type 무관성'
uses: [pert:palm.s1, pert:score-identity, pert:analytic-difference]
provides: 'pert:palm의 결론'
math: |
  이제 (6.16)은 (6.13)에서 나온다. 특히 base reservoir의 법칙에서 어떤 type도 지워지지 않았다. 이것이 마지막 주장을 증명한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [378, 381]}
status: proposed
---

풀이(작성자). s1의 두 식을 (6.13)의 분자에 넣으면 그 분자가 $c_\nu s_N H_N(t_\nu,u_\nu)$ 다. 마지막 주장: s1에서 남은 계가 원래 reservoir 법칙(type $\nu$ 를 포함한 모든 Poisson 족)을 그대로 가지므로 $J$ 와 $H_N$ 은 base reservoir와 insertion의 mark specification, $(t,u)$ 로만 정해지고 type 첨자 $j$ 에 의존하지 않는다. 다만 base reservoir는 선택된 벡터 $\mathbf u$ 전체에 의존하므로 $H_N$ 도 $N$ 과 그 벡터에 의존한다.
