---
id: pert:selection.s1
kind: step
title: '매개변수 평균한 증분이 낮은 크기가 무한히 많다'
uses: [x:pert-increment, cavity:negligible, cavity:increment, x:pert-parameter-measure]
provides: 'pert:selection.s2 (N_j를 고를 무한 집합과 상수 C)'
math: |
  균일 섭동 경계 (cavity:negligible)가
  $$\liminf_N\frac1N\int P_N^{L,\mathbf u}\,\pi(d\mathbf u)=\underline F$$
  를 준다. 따라서 무한히 많은 $N$ 이 $\int\Delta_N\,d\pi\le\underline F+\varepsilon$ 을 만족한다: 그렇지 않으면 평균 증분의 telescoping이 이 liminf와 모순이다. cavity:increment가 $|\Delta_N(\mathbf u)|\le C$ 가 균등하게 성립하는 상수 $C$ 를 준다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [269, 279]}
status: proposed
---

풀이(작성자). $|P_N^{L,\mathbf u}-NF_N|\le(\log2)N^{3/4}$ 가 $\mathbf u$ 에 균등하므로 $\frac1N\int P_N\,d\pi-F_N\to0$ 이고 liminf가 $\underline F$ 다. 어떤 $N_0$ 이후 모든 $N$ 에서 $\int\Delta_N\,d\pi>\underline F+\varepsilon$ 이면 $\int P_N\,d\pi\ge\int P_{N_0}\,d\pi+(N-N_0)(\underline F+\varepsilon)$ 이라 liminf가 $\underline F+\varepsilon$ 이상이 되어 모순이다. $\int\Delta_N\,d\pi=\int P_{N+1}\,d\pi-\int P_N\,d\pi$ 는 $\Delta_N$ 의 균등 유계성으로 적분이 정의된다. $\underline F$ 가 유한한 것은 bounded 모형이기 때문이다.
