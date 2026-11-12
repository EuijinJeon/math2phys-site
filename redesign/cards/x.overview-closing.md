---
id: x:overview-closing
kind: remark
title: '전략 마무리: 깊이 평균으로 충분함, 그리고 일반 법칙으로'
uses: [main:theorem, model:integrability, model:factorization, model:positivity]
provides: 'x:overview-strategy. L1 수 6(깊이 평균으로 충분함), 수 7'
math: |
  3단계의 추정은 서로 떨어진 내부 branching 깊이에 대한 평균이다. insertion 전개가 예외적 tree에 사라지는 확률을 주므로 이 평균으로 4단계에 충분하다. 깊이에 대해 균일한 집중은 필요 없다. 이렇게 얻은 하한은 입력의 순열에 불변인 모든 유계 상호작용 법칙에서, factorization이나 positivity 없이 성립한다. 마지막으로 정규화와 모든 시행 법칙에 균일한 추정이 유계성을 없애고, 명시된 1차 moment 가정 아래 main:theorem을 준다.
physics: |
  모든 [[g:multioverlap|multioverlap]]의 [[g:concentration|집중]]은 [[g:eta-regular|떨어진]] 내부 깊이에 대한 [[g:depth-average|깊이 평균]]으로만 얻지만, cavity 삽입의 [[g:tree-law|tree 법칙]] 전개가 예외적 깊이 배치에 작은 확률만 주므로 그것으로 충분하다. 그래서 하한은 [[g:bounded-law|유계]]이고 [[g:permutation-invariance|순열 불변]]인 상호작용(그리고 유계 장)에서 [[g:factorization|전개]]와 [[g:positivity|부호 조건]] 없이 성립한다. [[g:constant-shift|상수 이동]]과 시행 법칙 전체에 균일한 [[g:stability|$L^1$ 안정성]]으로 [[g:truncation|truncation]]을 걷어 내면, 1차 moment만 있는 일반 법칙에서 주정리가 나온다.
gap: |
  (1) 예외적 tree의 확률은 $\le C_k(\eta+L^{-1})$ 이고, 깊이 평균에서 $Q_k$ 평균으로 넘어가는 오차는 고정 $\eta$ 에서 $N$, $L$ 순으로 보낸 뒤 $\eta\downarrow0$ 으로 없앤다(tree:regular-shapes, comp:shape-error). (2) "factorization 없이"는 bounded 하한(comp:bounded-lower)에 대한 말이다. 일반 법칙으로 넓힐 때는 상수 이동이 $a$ 를 없애 순열 불변성을 만드는 데 factorization을 한 번 쓴다(main:theorem.s1). 원문 문단은 이것을 말하지 않는다. (3) 주정리의 결론은 이 하한과 상한(x:overview-upper, upper:bound)을 맞붙여서 나온다(main:theorem.s4). 문단은 이 맞붙임을 따로 적지 않는다. (4) "the stated first moment assumption"은 (2.1)이지만, 주정리의 가정은 (2.1)–(2.4) 전부다(상한이 나머지를 쓴다).
abstraction: approximation
children: []
source:
  - {file: overview.tex, lines: [43, 51]}
status: proposed
---

**가리키는 곳.**

| 문장 | 본문 노드 | overview.tex |
|---|---|---|
| 3단계 추정은 떨어진 내부 깊이의 평균 | [[decor:average-definition]], [[x:decor-eta-regular]], [[decor:overlap-concentration]] | 43–44 |
| 예외적 tree의 확률이 사라져 평균으로 충분 | [[tree:regular-shapes]] (`tree:irregular-probability`), [[comp:shape-error]], [[comp:shape-error-bound]] | 44–45 |
| 깊이에 균일한 집중은 필요 없음 | [[decor:order-of-limits]] | 45–46 |
| bounded·순열 불변 하한, factorization·positivity 없이 | [[comp:bounded-lower]], [[x:cavity-bounded]] | 46–48 |
| 정규화와 균일 추정으로 유계성 제거, 주정리 | [[reduction:stability]], [[main:theorem.s1]]–[[main:theorem.s3]], [[main:theorem.s4]], [[reduction:section]] | 48–51 (`\cref{main:theorem}`, `\cref{reduction:section}`) |

`uses` 의 [[main:theorem]]은 이 문단이 결론으로 이름을 부르는 진술(50행 `\cref`)이고, 주정리의 증명에 기대는 것이 아니다. 주정리 카드와 그 자손은 overview 카드를 `uses` 에 넣지 않으므로 순환이 없다. [[model:factorization]], [[model:positivity]], [[model:integrability]]는 "without factorization or positivity", "the stated first moment assumption"이 가리키는 가정이다.
