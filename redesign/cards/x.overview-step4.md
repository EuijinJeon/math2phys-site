---
id: x:overview-step4
kind: remark
title: '전략 4단계: 독립 cavity message 되찾기'
uses: [model:chain, model:functional]
provides: 'x:overview-strategy. L1 수 6'
math: |
  균일하게 고른 reservoir site 하나의 유한 계층 전체를 연속한 조건부 법칙으로 부호화한다. multioverlap 집중 덕에 cavity insertion에서 서로 다른 site label을 이 과정의 독립 사본으로 바꿀 수 있다. 이것이 선택된 증분에 가까운 admissible 시행값을 준다.
physics: |
  무작위 site 하나의 계층별 cavity field([[g:message|message]]) 분포를 깊이 방향으로 쌓아 시행 [[g:order-parameter|order parameter]]를 만든다([[g:encoded-law]]). 모든 [[g:multioverlap|multioverlap]]이 집중하므로 cavity 삽입에서 이웃 site들의 [[g:spin-pattern|spin pattern]]을 그 독립 사본으로 바꿔도 된다([[g:independent-copies]]). 독립 사본으로 계산한 삽입은 시행 [[g:functional|functional]] 값이고, 그것이 선택된 [[g:increment|증분]]에 가깝다.
gap: |
  (1) "가깝다"의 정확한 뜻은 $\lim_L\limsup_N\lvert\Delta_N-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\rvert=0$ 이고 $N$ 은 각 $L$ 의 [[g:selected-sequence|선택된 수열]]이다(comp:insertion-comparison). (2) 독립 사본의 근거는 국소 tree 구조나 그래프 거리에 따른 상관 감쇠가 아니라 균일 site 표본과 multioverlap 집중이다(comp:patterns). multioverlap 집중의 증명은 보조 계층 prefix 안의 조건부 공분산 소멸을 재료로 쓰므로(x:overview-step3), 그 뜻의 상관 소멸은 간접적으로 쓰인다(rules.md P11의 주의). (3) 부호화의 깊이는 보조 계층의 것이고, $\zeta_{L,N}$ 을 [[g:physical-pure-state|물리적 pure state]] 계층의 order parameter로 읽는 것은 증명되지 않는다. (4) 여기서 쓰는 집중은 깊이 평균이고 그것으로 충분한 이유는 x:overview-closing이 말한다.
abstraction: approximation
children: []
source:
  - {file: overview.tex, lines: [35, 41]}
status: proposed
---

41행은 `\end{enumerate}` 이다.

**가리키는 곳.**

| 문장 | 본문 노드 | overview.tex |
|---|---|---|
| 한 site의 유한 계층을 조건부 법칙으로 부호화 | [[comp:encoding]] | 36–37 |
| site label을 독립 사본으로 | [[comp:patterns]], [[comp:insertion-comparison]] | 37–39 |
| 선택된 증분에 가까운 admissible 시행값 | [[comp:insertion-comparison]], [[comp:bounded-lower]], [[comp:section]] | 39–40 (`\cref{comp:section}`) |
