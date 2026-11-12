---
id: pert:concentration.s3.s3
kind: step
title: '유계 차분, Lipschitz 조건부 평균, Poisson 분산'
uses: [pert:concentration.s3.s2, pert:concentration.s3.s1, pert:concentration.s1, x:pert-standing, tree:insertion, x:tree-extra-variables]
provides: 'pert:concentration.s4.s1 ((6.11) 완성)'
math: |
  상호작용, 장, 섭동 항 하나를 다시 뽑으면 $X_0$ 는 유계만큼 바뀐다: spin weight에서는 바로 보이고 각 power mean이 이를 보존한다. 항을 없앨 때는 쓰지 않는 그 독립 mark 변수를 적분해 없앨 수 있으므로 항의 추가나 삭제에도 같은 주장이 성립한다. 따라서 조건부 분산은 root 변수 개수의 상수배 이하다. 조건부 평균은 개수의 Lipschitz 함수이고 Lipschitz 상수가 유계다. $Q,Q'$ 이 Poisson 변수의 독립 사본이고 $b$ 가 $C$-Lipschitz이면
  $$\operatorname{Var}(b(Q))=\tfrac12\mathbb E(b(Q)-b(Q'))^2\le C^2\operatorname{Var}(Q).$$
  이것을 독립 개수들에 적용하면 $O(N)$ 추정이 끝난다. 보정 $2nu^2$ 도 같은 추정을 따른다. (6.11)의 도함수 경계는 (6.6)에서 바로 나온다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [192, 209]}
status: proposed
---

풀이(작성자). "each power mean preserves"는 [[tree:insertion]]의 단조성·동차성을 `\ref` 없이 쓴 것이다: 바뀌는 인자의 비가 root-가측 상수 $e^{\pm c}$ 사이에 있으면 root logarithm도 $\pm c$ 안에서 바뀐다. 상호작용은 $B$, 장은 $H$, 섭동은 $\log 3$ 정도의 상수다($1/2<\psi<3/2$). "unused independent mark variables can be integrated out"은 [[x:tree-extra-variables]]의 약속(쓰지 않는 보조 변수는 prior로 적분해 없앤다, cavity.tex 96–98과 같음)이다.

root 변수 개수: reservoir나 원래 계에서 물리 상호작용 개수의 평균 $O(N)$, 장 $N$ 개, 섭동 개수의 평균 $s_N$([[x:pert-standing]]). 그래서 $\mathbb E[\text{조건부 분산}]=O(N)$. 개수 쪽은 분산 분해 $\operatorname{Var}=\mathbb E\operatorname{Var}(\cdot\mid\text{개수})+\operatorname{Var}(\mathbb E[\cdot\mid\text{개수}])$ 의 둘째 항으로, 독립 개수 하나씩 위 Poisson 부등식을 쓰면 $\operatorname{Var}(Q)=\mathbb EQ=O(N)$ 이다. 보정 $2nu^2$ 는 $n$ 의 Lipschitz 함수이고 $u$ 가 유계이므로 같다. 도함수: $|G'|\le|X_0'|+4n|u|\le(2+4|u|)n$ 이고 $\mathbb En=\lambda_\nu$.
