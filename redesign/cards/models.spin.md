---
id: models:spin
kind: corollary
title: 'Viana–Bray와 희석 짝수 $p$-spin 모형 (Corollary 10.1)'
uses: [x:cons-standard-examples, model:hamiltonian, model:integrability, model:factorization, model:positivity, x:model-hypotheses, model:functional, main:theorem]
provides: 'models:ground (consequences.tex 88: 대상 모형, 1차 moment $\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert<\infty$), x:cons-energy-score (법칙 $J$, $H$). introduction.tex 29–31("the Viana–Bray model, diluted even-spin models with symmetric couplings"), L0, g:named-models, g:factorization·g:positivity의 물리 대응 칸, model:factorization·model:positivity의 예'
math: |
  짝수 정수 $p\ge2$, $\alpha>0$ 과 서로 독립인 실수 확률변수 $J,H$ 를 고정한다. $J$ 의 분포는 대칭이고 $\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert<\infty$ 이다. 모든 $\beta>0$ 에 대해
  $$\theta_\beta(s_1,\ldots,s_p)=\beta J\prod_{\ell=1}^ps_\ell,\qquad h_\beta=\beta H$$
  인 모형은 변분 공식 (2.13)을 만족하고, 시행 functional은 이 상호작용 법칙과 장 법칙에서 계산한다. 특히 $p=2$ 인 Viana–Bray 모형에서 성립한다.
physics: |
  spin당 평균 $\alpha$ 개의 $p$체 coupling $J\prod_\ell s_\ell$ 과 무작위 장 $H$ 를 갖는 희석 짝수 $p$-spin glass([[x:cons-standard-examples]]의 Poisson [[g:hypergraph|hypergraph]] 위; $p=2$ 가 Viana–Bray)에서, $J$ 의 분포가 대칭이고 $J$, $H$ 가 서로 독립이며 1차 moment가 유한하면, 모든 온도 $\beta>0$ 에서 quenched [[g:pressure|pressure]]의 열역학 극한이 존재하고 모든 유한 [[g:rsb-steps|RSB 단계 수]]의 Mézard–Parisi 시행값([[g:functional]])의 [[g:phi|inf]]와 같다.
gap: |
  (1) "모든 $\beta>0$"은 원문 그대로다. 어느 $\beta$ 에서 몇 단 RSB가 필요한지, 예컨대 어떤 온도에서 $r=0$ 으로 충분한지는 말하지 않는다. inf의 달성도 주장하지 않는다(x:model-theorem-scope). (2) $J$ 의 분포가 대칭이 아닌 경우는 이 따름정리가 다루지 않는다. 대칭성은 (2.4)의 홀수 moment를 0으로 만드는 데 쓰인다(models:spin.s2). (3) factor 개수가 Poisson이고 site가 복원추출이다. 고정 연결도(random regular) 그래프나 고정 개수 모형은 대상이 아니다. (4) 증명은 주정리의 [[g:hypotheses|가정]]을 확인할 뿐이고, 새로운 논증은 없다.
abstraction: exact
children: [models:spin.s1, models:spin.s2, models:spin.s3]
source:
  - {file: consequences.tex, lines: [10, 22]}
  - {file: consequences.tex, lines: [24, 34]}
status: proposed
---

**증명의 뼈대.** 주정리의 가정 (2.1)–(2.4)([[x:model-hypotheses]])를 하나씩 확인한다.

- [[models:spin.s1]]: $a=\cosh(\beta J)$, $b=\tanh(\beta J)$, $f_\ell(s)=s$ 로 (2.3)의 표현과 엄격한 곱 한계.
- [[models:spin.s2]]: $J$ 의 대칭성으로 (2.4).
- [[models:spin.s3]]: $B(\theta_\beta)=\beta\lvert J\rvert$, $\lvert h_\beta\rvert=\beta\lvert H\rvert$ 로 (2.1). 그러므로 [[main:theorem]]이 적용된다.

짝수 $p$ 는 진술에서 고정한다(12행). 이것이 (2.1)–(2.4)와 함께 [[model:integrability]]의 전제다.

**$J$ 와 $H$ 의 독립 (작성자 읽기).** 증명은 $J$, $H$ 의 독립을 따로 쓰지 않는다. (2.2)는 $\theta$ 의 사본 $\theta_k$ 와 $h$ 의 사본 $h_i$ 를 서로 독립인 족으로 뽑으므로([[model:hamiltonian]]) 모형에는 $J$ 와 $H$ 의 결합 법칙이 들어가지 않는다. 진술의 "independent"는 원문 그대로 옮겼다.
