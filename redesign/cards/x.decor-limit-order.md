---
id: x:decor-limit-order
kind: convention
title: '선택된 수열과 극한 순서'
uses: [pert:selection, pert:tree-identity]
provides: '§7의 모든 limsup_N과 o_N(1)의 의미. decor:identity-error와 decor:order-of-limits의 전제'
math: |
  각 고정 $L$에 대해 (그리고 pert:selection의 고정된 $\varepsilon>0$에 대해) $N\to\infty$의 모든 극한과 $\limsup_N$, $o_N(1)$은 pert:selection이 주는 크기 $N_j\uparrow\infty$와 결정적 매개변수 $\mathbf u_j$의 수열을 따라 취한다. 이 수열에서 pert:tree-identity의 항등식
  $$\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\,\mathbb E[fR_E]-\mathbb Ef\sum_{E\in\mathfrak E(\{a_*\},a_*,\mathcal C)}c_E\,\mathbb E[R_E]\longrightarrow0$$
  이 모든 고정 old tree $\mathcal T$, spin/marker anchor $a_*$, 유계 multioverlap 다항식 $f$, 유한 개 added color, 제약 $\mathcal C$에 대해 성립한다. 수열은 $L$마다 다를 수 있다. $\lim_L\limsup_N$ 꼴의 진술은 항상 고정 $L$에서 $N$ 극한을 먼저 취한다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [4, 9]}
status: proposed
---

§7은 §6의 항등식과 [[g:prescribed-tree|tree 표본 규칙]]([[x:decor-tree-sampling]])만 쓴다. 모형의 interaction factorization은 쓰지 않는다(tex 8–9). 그래서 §7의 결과는 "이 항등식들을 만족하는 임의의 깊이-$L$ tree 계"에 대한 정리로 읽을 수 있다.
