---
id: x:comp-standing
kind: convention
title: '§8의 고정된 선택: $\varepsilon$, 깊이마다의 선택된 수열, 선택 전의 $\underline F$'
uses: [pert:selection, x:pert-selected-limits, x:pert-increment, x:cavity-bounded, cavity:grid]
provides: 'comp:low-increments, comp:encoding("selected parameter vector"), comp:shape-error(130 "the inner limit is along the selected fixed-$L$ sequence"), comp:insertion-comparison, comp:bounded-lower(243 "that depth''s selected sequence")의 모든 $N$ 과 기대값의 뜻'
math: |
  $\varepsilon>0$ 을 고정한다. 각 깊이 $L\ge2$ 에서 pert:selection이 주는 크기 수열과 결정적 매개변수 선택을 쓴다. 이 수열 위의 크기를 $N$ 으로 쓰고, 그 크기의 선택된 벡터를 $\mathbf u_{L,N}$ 으로 쓴다. 선택은 $L$ 에 의존할 수 있고, 아래의 모든 진술은 이 선택에 관한 것이다. $\underline F$ 는 선택 전과 같이 bounded 모형의 **모든** 크기에 대한 liminf로 남겨 둔다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [8, 12]}
status: proposed
---

$\mathbf u_{L,N}$ 이라는 표기는 원문 14행(comp:low-increments)에서 처음 나온다. pert:selection의 수열은 $L$ 과 $\varepsilon$ 마다 하나씩이므로(pert:selection "for every fixed $L\ge2$ and $\varepsilon>0$"), §8 전체에서 $\varepsilon$ 이 고정된 채 $L$ 만 움직인다는 것이 이 약속의 요점이다(작성자 읽기). $\varepsilon\downarrow0$ 은 [[comp:bounded-lower.s2]]의 맨 마지막에만 나온다.

$\underline F$ 가 "모든 크기"의 liminf라는 것은 [[x:pert-increment]]의 정의 그대로다. 이것이 중요한 이유: $\underline F$ 는 수열, $L$, $\varepsilon$ 에 의존하지 않으므로 [[comp:bounded-lower.s2]]에서 $L\to\infty$, $\varepsilon\downarrow0$ 을 보낸 뒤에도 같은 양이고, 결론 $\liminf_NF_N\ge\inf_r\Phi_r$ 이 부분수열이 아닌 모든 $N$ 에 대한 진술이 된다. 기대값은 선택된 벡터를 고정한 [[g:root]]·tree 기대값이다([[x:pert-selected-limits]]). 이 절 전체가 [[x:cavity-bounded]]의 유계·순열 불변 가정 아래에 있고 $m_d=d/L$ 이다([[cavity:grid]]).
