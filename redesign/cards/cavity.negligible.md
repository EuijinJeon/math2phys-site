---
id: cavity:negligible
kind: remark
title: '섭동의 비용 $\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N$ (5.3)'
uses: [x:cavity-root-logarithm, cavity:factor-bounds, x:cavity-root-convention, tree:original-tilt, tree:insertion, x:tree-extra-variables, model:hamiltonian]
provides: 'pert:selection (perturbations.tex 271: $\liminf_N\frac1N\int P_N^{L,\mathbf u}\pi(d\mathbf u)=\underline F$), pert:factor (perturbations.tex 65–67: 항별 비교의 본보기), cavity:increment.s4 (작은 $N$ 의 상수, 작성자 읽기). 규칙 P3, L1 수 2'
math: |
  섭동되지 않은 spin weight와 점별로 비교한 뒤 recursion을 적용하면
  $$\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)s_N\tag{5.3}$$
  이고, 이것은 계층, 그 매개변수, $N$ 에 대해 균일하다.
physics: |
  sublinear한 수 $N^{3/4}$ 의 [[g:perturbation|섭동]]은 계층 free entropy([[g:root-logarithm|root logarithm]])의 밀도를 [[g:pressure|pressure]] $F_N$ 에서 $o(1)$ 만큼만 옮긴다: $P_N^{L,\mathbf u}/N-F_N\to0$.
gap: |
  정확한 진술은 $(\log2)N^{3/4}$ 의 균일한 부등식이고, 물리 문장은 밀도 수준의 결론만 남겼다. "그 매개변수(its parameters)"는 섭동 매개변수 $\mathbf u$ 로 읽는다(작성자 읽기, 검토자 동의. 근거: $P_N^{L,\mathbf u}$ 의 세 첨자 $L$, $\mathbf u$, $N$ 이 "the hierarchy, its parameters, and $N$"에 하나씩 대응한다; 바로 앞 29–30행이 "The parameters of the factors are denoted by $\mathbf u$"로 이 말을 들여온다; 16–19행이 $m_d=d/L$ 을 고정해 계층의 지수는 $L$ 로 정해진다; lemma가 "uniform in $L,\mathbf u$"라 쓰고(45, 55, 114) perturbations.tex 271–273이 $\pi(d\mathbf u)$ 로 적분하며 이 균일성을 쓴다). 증명이 한계 (5.2)와 개수만 쓰므로 지수 $m_d$ 의 선택에도 균일하다(작성자 확인).
abstraction: weakening
children: []
source:
  - {file: cavity.tex, lines: [35, 41]}
status: proposed
---

**확인 (작성자).** 섭동되지 않은 spin weight의 분배함수 $Z_N$ 은 보조 변수에 의존하지 않으므로 recursion 뒤에도 root logarithm이 $\log Z_N$ 이다. 섭동 factor가 $n$ 개면 $2^{-n}Z_N\le Z\le(3/2)^nZ_N\le2^nZ_N$ 이고, $n$ 이 root 변수([[x:cavity-root-convention]])라서 이 곱셈적 한계가 backward recursion을 그대로 통과한다. 근거는 [[tree:insertion]]의 단조성이다(작성자 읽기, `\ref` 없음): 섭동 factor의 곱 $A=\prod\psi$ 를 섭동되지 않은 spin weight에 대한 insertion으로 보면(섭동 factor의 보조 변수는 섭동되지 않은 계에 없으므로 [[x:tree-extra-variables]]대로 path kernel을 그 prior로 넓힌다) root logarithm의 변화가 $\log Y_0$ 이고, $2^{-n}\le A\le(3/2)^n$ 의 한계가 root-가측이므로 $2^{-n}\le Y_0\le(3/2)^n$ 이다. 따라서 $\lvert X_0-\log Z_N\rvert\le n\log2$, 기대값에서 $\mathbb En=s_N$.

원문 36–37 "Comparing pointwise with the unperturbed spin weight and then applying the recursion"은 어느 결과도 가리키지 않는다. 논문에서 recursion의 단조성이 진술된 곳은 trees.tex 107–110([[tree:insertion]]) 하나뿐이고, [[tree:original-tilt]]는 recursion과 tilted kernel을 정의할 뿐 단조성을 진술하지 않는다. 그래서 단조성은 [[tree:insertion]]에서 받는다(검토 2 F2). power mean $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$ 가 점별 단조라는 직접 논법도 같은 backward induction이다.
