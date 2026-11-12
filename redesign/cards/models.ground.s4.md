---
id: models:ground.s4
kind: step
title: 'SAT에서 최대화 = 위반 수 최소화'
uses: [x:cons-energy-score]
provides: 'models:ground의 마지막 문장 (단위 가중치 SAT에서 $-g$ 의 뜻)'
math: |
  satisfiability 모형에서 음의 위반 개수를 최대화하는 것은 그 개수를 최소화하는 것과 같다.
physics: |
  $W=1$ 이면 $-\mathcal E_N(\sigma)$ 는 배치 $\sigma$ 가 위반하는 clause 수다. 그래서 $-\max_\sigma\mathcal E_N$ 은 최소 위반 수이고, $-g$ 는 그 기대값의 변수당 극한이다.
gap: |
  정확하다. 원문은 이 한 문장으로 진술의 마지막 줄(99–100행)을 정당화한다. 일반 $W$ 에서 $-g$ 는 위반 가중치 합의 최소값 밀도다(작성자 읽기). Poisson 개수와 복원추출 모형에서의 값이고, 고정 개수 앙상블과의 비교는 하지 않는다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [123, 125]}
status: proposed
---
