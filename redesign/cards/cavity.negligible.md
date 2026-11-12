---
id: cavity:negligible
kind: remark
title: '섭동의 비용 $\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N$ (5.3)'
uses: [x:cavity-root-logarithm, cavity:factor-bounds, x:cavity-root-convention, tree:original-tilt, model:hamiltonian]
provides: 'pert:selection (perturbations.tex 271: $\liminf_N\frac1N\int P_N^{L,\mathbf u}\pi(d\mathbf u)=\underline F$), perturbations.tex 65–67 (항별 비교의 본보기), cavity:increment.s4 (작은 $N$ 의 상수, 작성자 읽기). 규칙 P3, L1 수 2'
math: |
  섭동되지 않은 spin weight와 점별로 비교한 뒤 recursion을 적용하면
  $$\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N\tag{5.3}$$
  이고, 이것은 계층, 그 매개변수, $N$ 에 대해 균일하다.
physics: |
  sublinear한 수 $N^{3/4}$ 의 [[g:perturbation|섭동]]은 계층 free entropy([[g:root-logarithm|root logarithm]])의 밀도를 [[g:pressure|pressure]] $F_N$ 에서 $o(1)$ 만큼만 옮긴다: $P_N^{L,\mathbf u}/N-F_N\to0$.
gap: |
  정확한 진술은 $(\log2)N^{3/4}$ 의 균일한 부등식이고, 물리 문장은 밀도 수준의 결론만 남겼다. "그 매개변수(its parameters)"가 계층의 매개변수($m_d$)인지 섭동 매개변수 $\mathbf u$ 인지 원문 문장만으로는 갈리지 않는다 ❓. 증명이 한계 (5.2)만 쓰므로 두 경우 모두에 균일하다(작성자 확인).
abstraction: weakening
children: []
source:
  - {file: cavity.tex, lines: [35, 41]}
status: proposed
---

**확인 (작성자).** 섭동되지 않은 spin weight의 분배함수 $Z_N$ 은 보조 변수에 의존하지 않으므로 recursion 뒤에도 root logarithm이 $\log Z_N$ 이다. 섭동 factor가 $n$ 개면 $2^{-n}Z_N\le Z\le(3/2)^nZ_N\le2^nZ_N$ 이고, $n$ 이 root 변수([[x:cavity-root-convention]])라서 이 곱셈적 한계가 backward recursion을 그대로 통과한다(recursion은 단조이고 root-가측 상수를 그대로 옮긴다). 따라서 $\lvert X_0-\log Z_N\rvert\le n\log2$, 기대값에서 $\mathbb En=s_N$.
