---
id: pert:selection.s2
kind: step
title: 'score 오차가 작은 매개변수를 Markov 부등식으로 고르기'
uses: [pert:selection.s1, pert:concentration, pert:error, x:pert-parameter-measure]
provides: 'pert:selection (i), (ii)'
math: |
  유한 개 type 모임에 대해 pert:concentration과 Markov 부등식은 그 오차가 모두 작은 집합의 매개변수 측도가 1로 감을 보인다. 구체적으로, 앞의 무한 집합에서 $N_j$ 를 차례로 충분히 크게 골라
  $$\sum_{\nu\le j}\int e_{\nu,N_j}(\mathbf u)\,\pi(d\mathbf u)\le j^{-3}$$
  이 되게 한다. 그러면 모든 $\nu\le j$ 에서 $e_{\nu,N_j}\le j^{-1}$ 인 집합 $G_j$ 의 여집합 측도는 $q_j\le j^{-2}$ 이다. $G_j$ 위 조건부 평균 증분은 충분히 큰 모든 $j$ 에서
  $$\frac{\underline F+\varepsilon+Cq_j}{1-q_j}\le\underline F+2\varepsilon$$
  이하다. 따라서 $G_j$ 안에서 증분이 $\underline F+2\varepsilon$ 이하인 벡터를 고를 수 있다. 꼬리를 다시 번호 매기면 (i)과 (ii)가 증명된다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [281, 299]}
status: proposed
---

풀이(작성자). Markov: $\pi(e_{\nu,N_j}>j^{-1})\le j\int e_{\nu,N_j}\,d\pi$ 이고 $\nu\le j$ 에 대해 합하면 $q_j\le j\cdot j^{-3}$. 조건부 평균: $\int_{G_j}\Delta\,d\pi\le\int\Delta\,d\pi+\int_{G_j^c}|\Delta|\,d\pi\le\underline F+\varepsilon+Cq_j$ 를 $\pi(G_j)=1-q_j$ 로 나눈다. 평균이 $\underline F+2\varepsilon$ 이하이면 그 이하의 점이 양의 측도로 있다. 고정된 $\nu$ 에 대해 $j\ge\nu$ 부터 $e_{\nu,N_j}(\mathbf u_j)\le j^{-1}$ 이므로 (ii)다. $N_j$ 를 고를 수 있는 것은 각 $\nu$ 에서 $\int e_{\nu,N}\,d\pi\to0$ 이라 유한 합도 0으로 가기 때문이다. 원문은 여기서 $e_{\nu,N}$ 이 reservoir의 것이라고 다시 적지 않는다. 진술 (ii)와 pert:concentration의 "holds for the reservoir"로 보아 reservoir의 score 오차로 읽었다(작성자 읽기).
