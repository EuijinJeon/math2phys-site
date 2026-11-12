---
id: upper:section
kind: section
title: '§4 interpolation 상한'
uses: [x:model-hypotheses, model:hamiltonian, model:integrability, model:factorization, model:positivity, model:chain, x:model-message, model:site-message, model:edge, x:model-cavity-bounds, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero, tree:original-tilt, tree:Y-recursion, tree:insertion, x:tree-extra-variables, x:tree-sampling, tree:Q-rule, tree:log-expansion]
provides: 'main:theorem.s4 (reduction.tex 85의 upper:bound: $\limsup_NF_N\le\inf_r\Phi_r$, 원래의 truncate하지 않은 법칙에 적용). x:model-moment-finiteness (model.tex 39–41의 예고가 upper:bound.s1을 가리킴). overview.tex 4 (전략 소개). 규칙 P1·P2, L1 수 1'
math: |
  받는 것 (§2, §3). 가정 묶음 x:model-hypotheses((2.1)–(2.4), 짝수 $p$), 모형 model:hamiltonian, 시행 법칙과 functional(model:chain, x:model-message, model:site-message, model:edge, x:model-cavity-bounds, model:vs, model:ve, model:power-means, model:functional, x:model-depth-zero), 그리고 §3의 insertion 미적분(tree:original-tilt, tree:Y-recursion, tree:insertion, x:tree-extra-variables, x:tree-sampling, tree:Q-rule, tree:log-expansion).

  내놓는 것 (upper:bound). main:theorem의 가정 아래 모든 $N$ 과 모든 admissible 유한 단계 시행 법칙에 대해 $F_N\le\mathcal B_r(\zeta,\mathbf m)$, 따라서 $F_N\le\inf_{r\ge0}\Phi_r$.
physics: |
  Guerra의 [[g:interpolation|interpolation]](Franz–Leone이 희석계로, Panchenko–Talagrand가 임의의 유한 단계로 옮긴 것, upper.tex 3–6): 실제 $p$체 factor 각각을 독립 [[g:message|cavity field]]를 보는 $p$ 개의 cavity factor로 바꾸는 경로에서 차이를 $x\mapsto x^p$ 의 볼록성으로 제어해, 모든 [[g:rsb-steps|RSB 단계 수]]의 시행 Bethe free entropy([[g:functional]])가 모든 $N$ 에서 [[g:pressure|pressure]]의 상한임을 보인다.
gap: |
  (1) 물리의 정류점 선택이 아니라 모든 시행값이 상한이다([[g:phi]]). (2) [[g:hypotheses|가정]] 전부를 쓴다: [[g:factorization|factor 전개]]와 그 독립 구조(삽입의 $a(1+D)$ 꼴, 나머지항의 $P^p$, $PB^{p-1}$, $B^p$ 분해, $b$ 와 $f$ 의 유계성), 짝수 $p$ (볼록성), [[g:positivity|부호 조건]](나머지항의 부호), (2.1)(지배 함수). (3) 시행 message에 moment 조건이 없고 물리 disorder는 적분 가능하기만 하면 된다(upper.tex 7–9). $\log a$ 의 적분 가능성도 요구하지 않는다(upper:regularization). (4) 증분은 [[g:power-mean|power mean]] recursion을 거친 [[g:root-logarithm|root logarithm]]의 변화이고, 그 전개의 tree 법칙 $Q_n$ 을 물리 그림으로 읽는 것은 [[g:tree-law]]의 물리 대응 칸에 intuition으로만 있다.
abstraction: approximation
children: [upper:bound]
source:
  - {file: upper.tex, lines: [1, 128]}
status: proposed
---

**뼈대.** 이 절은 명제 하나 [[upper:bound]]이다. 증명 단계: [[upper:bound.s1]] (퇴화 경우, 유계성) → [[upper:bound.s2]] (보간과 끝점) → [[upper:bound.s3]] (Poisson 미분, 증분 한계) → [[upper:derivative]] (핵심 부등식; [[upper:derivative.s1]] 세 삽입의 꼴, [[upper:regularization]] 정규화, [[upper:remainder]] 볼록성) → [[upper:bound.s4]] (적분).

**밖에서 받는 것** (원문의 실제 참조와 `\ref` 없는 사용).

| 받는 것 | 카드 | 원문 위치 |
|---|---|---|
| 주정리의 가정 | [[x:model-hypotheses]] (`\cref{main:theorem}` 대신) | upper.tex 12 |
| (2.3) factorization | [[model:factorization]] | upper.tex 63 (`\eqref`), 18–34, 71–75 (`\ref` 없음) |
| (2.4) positivity | [[model:positivity]] | upper.tex 125 (`\eqref`) |
| log 전개, $Y_0$, $Q_n$ | [[tree:log-expansion]], [[tree:Q-rule]], [[tree:Y-recursion]] | upper.tex 81, 97, 121 (`\cref`) |
| recursion의 단조·동차성, 삽입 증분 $=\log Y_0$ | [[tree:insertion]] | upper.tex 51–54, 71, 82–93 (`\ref` 없음) |
| 새 message 과정을 tilted tree에 덧붙임 | [[x:tree-extra-variables]] | upper.tex 66–68 (`\ref` 없음) |
| tree 표본과 replica | [[x:tree-sampling]] | upper.tex 97–109 (`\ref` 없음) |
| backward power-mean recursion | [[tree:original-tilt]], [[model:power-means]] | upper.tex 41–43 |
| $\mathcal B_r$, $V_{\rm s}$, $V_{\rm e}$, $T_0$, $U_\theta$, $C_\theta$, $q_x$, $r=0$ | [[model:functional]], [[model:vs]], [[model:ve]], [[model:power-means]], [[model:site-message]], [[model:edge]], [[x:model-message]], [[x:model-depth-zero]], [[model:chain]] | upper.tex 13–14, 39, 43–48, 60, 65–68, 108 (기호로만) |
| $\lvert U_\theta\rvert\le B(\theta)$ | [[x:model-cavity-bounds]] | upper.tex 53–54 (`\ref` 없음) |
| $F_N$, Poisson 구조 | [[model:hamiltonian]], [[model:integrability]] | upper.tex 13, 22, 37, 48 |

**밖에 내주는 것.**

| 받는 곳 | 쓰는 것 | 원문 위치 |
|---|---|---|
| [[main:theorem.s4]] | [[upper:bound]] ($\limsup_NF_N\le\inf_r\Phi_r$) | reduction.tex 85 |
| [[x:model-moment-finiteness]] | [[upper:bound]] (실제 내용은 [[upper:bound.s1]]) | model.tex 39–41 (예고) |
| overview.tex 전략 | 이 절 전체 | overview.tex 3–6 |

**순환.** [[main:theorem]] → [[upper:bound]] 방향만 있다. [[upper:bound]]와 자손은 [[main:theorem]], [[x:model-moment-finiteness]], [[x:model-hypothesis-remarks]]를 `uses`에 넣지 않는다. 앞의 둘은 `upper:bound`에 기대므로 넣으면 순환이고, 마지막은 증명이 같은 사실을 스스로 적어서 필요가 없다.

**인터페이스 점검.** [[tree:section]]의 export 표는 §4에 [[tree:log-expansion]](`\cref`)과 `\ref` 없는 [[tree:insertion]](증분 $=\log Y_0$, 단조·동차성), [[x:tree-extra-variables]], [[tree:original-tilt]](41–43, 68)를 적는다([[tree:original-tilt]]는 검토 2 F10 대응으로 더했다). [[tree:Y-recursion]], [[tree:Q-rule]], [[x:tree-sampling]]은 원문이 81, 120–121에서 [[tree:log-expansion]]을 통해 가리키므로 그 표의 §4 행에도 함께 적었다. [[model:section]]의 표(upper.tex 12/63/125)는 `\ref` 기준으로 맞고, 기호로만 쓰는 것($V_{\rm s}$, $V_{\rm e}$, $T_0$)도 그 카드가 따로 적었다.
