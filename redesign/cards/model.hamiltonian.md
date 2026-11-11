---
id: model:hamiltonian
kind: definition
title: 'Hamiltonian $H_N$, 분배함수 $Z_N$, pressure $F_N$'
uses: [model:integrability]
provides: '주정리가 극한을 구하는 양 $F_N$. upper:bound, reduction:stability, cavity.tex의 reservoir, consequences.tex 8(Poisson 개수와 복원추출 유지)'
math: |
  서로 독립인 $M_N\sim\mathrm{Pois}(\alpha N)$, $\theta$ 의 독립 사본 $\theta_k$, $h$ 의 독립 사본 $h_i$, 독립 균일 index $i_{\ell,k}\in[N]=\{1,\ldots,N\}$ 에 대해
  $$-H_N(\sigma)=\sum_{k=1}^{M_N}\theta_k(\sigma_{i_{1,k}},\ldots,\sigma_{i_{p,k}})+\sum_{i=1}^Nh_i\sigma_i,\qquad Z_N=\sum_{\sigma\in\{-1,1\}^N}e^{-H_N(\sigma)},\qquad F_N=\frac1N\mathbb E\log Z_N.\tag{2.2}$$
  이 정의의 모든 족은 서로 독립이다. 특히 index는 복원추출이다(한 factor 안에서 같은 site가 반복될 수 있다). 모형 매개변수와 disorder 법칙은 $N$ 이 변해도 고정이다.
physics: |
  spin당 평균 $\alpha$ 개의 $p$체 factor가 놓인 Poisson random [[g:hypergraph|hypergraph]](Erdős–Rényi형 factor graph) 위의 Ising spin glass이고, $F_N$ 은 quenched [[g:pressure|pressure]]($=-\beta f$)이다. [[g:disorder|disorder]]는 factor 개수, factor의 site, factor별 [[g:interaction|상호작용]], site별 [[g:field|장]]이다.
gap: |
  factor 개수는 고정 $\alpha N$ 이 아니라 Poisson이고 site는 복원추출이다. 이 선택은 cavity 비교의 정확한 Poisson 분해(cavity.tex)와 명명 모형(consequences.tex 6–8)에서 그대로 유지된다. 고정 개수나 비복원추출 모형과의 동치는 이 섹션이 다루지 않는다.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [9, 23]}
status: proposed
---

"$F_N$ 이 유한하다"는 원문에 따로 적혀 있지 않다. $\lvert\log Z_N-N\log2\rvert\le\sum_{k\le M_N}B(\theta_k)+\sum_i\lvert h_i\rvert$ 이고 (2.1)에서 기대값이 $\alpha N\,\mathbb EB(\theta)+N\,\mathbb E\lvert h\rvert<\infty$ 이므로 유한하다(작성자가 보탠 확인).
