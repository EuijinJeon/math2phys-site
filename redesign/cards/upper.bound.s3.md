---
id: upper:bound.s3
kind: step
title: 'Poisson 미분: $\varphi^\prime(t)/\alpha$ 를 삽입 증분으로'
uses: [upper:bound.s2, tree:insertion, x:model-cavity-bounds, model:integrability]
provides: 'upper:derivative ($\varphi^\prime$ 의 표현), upper:bound.s4 (끝점 연속성)'
math: |
  Poisson 미분은 $\varphi'(t)/\alpha$ 를 실제 상호작용 하나의 기대 삽입 증분에서, 균일 site에 놓은 cavity 상호작용 하나의 증분의 $p$ 배를 뺀 것으로 준다. recursion이 곱셈적 한계를 보존하므로 각 증분의 절댓값은 $B(\theta)$ 이하다. 개수에 조건을 걸면 $(0,1)$ 에서 도함수가 정당화되고, 같은 한계가 끝점에서의 연속성을 준다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: upper.tex, lines: [51, 56]}
status: proposed
---

**풀이 (작성자).** Poisson 평균 $\lambda$ 에 대해 $\frac{d}{d\lambda}\mathbb EG(\mathrm{Pois}(\lambda))=\mathbb E[G(n+1)-G(n)]$ 이다. 실제 상호작용은 평균 $t\alpha N$ 이므로 $\varphi=\frac1N\mathbb E(\cdot)$ 에 $\alpha N\cdot\frac1N$ 을, site $N$ 개 각각의 cavity 개수는 평균 $(1-t)\alpha p$ 이므로 $-\alpha p$ 를 균일 site 평균과 함께 준다. 여기서 "삽입 증분"은 상호작용 하나를 더했을 때 root logarithm의 변화이고, [[tree:insertion]]에 따라 그 값은 $\log Y_0$ 이다(새 message label을 쓰는 cavity 상호작용은 [[x:tree-extra-variables]]의 약속으로 들어온다; 이 단계에서는 크기만 쓰므로 `uses`에 넣지 않았다).

$\lvert\text{증분}\rvert\le B(\theta)$: 실제 상호작용은 $e^{\pm B(\theta)}$ 사이, cavity 상호작용은 $\lvert U_\theta\rvert\le B(\theta)$([[x:model-cavity-bounds]])이고, 이 root-가측 한계를 recursion이 보존한다([[tree:insertion]]의 단조성). $\mathbb EB(\theta)<\infty$(model:integrability)가 개수에 대한 합과 미분의 교환, 끝점 연속성의 지배 함수가 된다.
