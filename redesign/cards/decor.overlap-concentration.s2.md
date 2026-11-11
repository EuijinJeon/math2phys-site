---
id: decor:overlap-concentration.s2
kind: step
title: 'marker anchor로 prefix 사영 $M$을 집중시키기'
uses: [pert:tree-identity, tree:reference-total, x:decor-tree-sampling, x:decor-mesh]
provides: 'decor:overlap-concentration.s4 (Var(M)→0)'
math: |
  $|S|\ge2$, 첫 갈라짐 $e$, $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$이라 하면 각 고정 $L$, $S$, 깊이 배정에서 $\operatorname{Var}(M)\to0$ ($N\to\infty$).
physics: |
  깊이 $e-1$ [[g:state|상태]]에서의 평균 [[g:multioverlap|overlap]] $M$은 상태와 disorder에 따라 요동하지 않는다(상태 사이 요동의 소멸). marker [[g:anchor|anchor]]를 쓴 [[g:tree-identity|prescribed-tree 항등식]]에서 나온다.
gap: |
  고정 $L$과 고정 깊이에서, [[g:selected-sequence|선택된 perturbed 수열]]을 따라 $N\to\infty$로만 성립한다. 계수 $C(S,e)=-\delta\kappa(S)$로 나누므로 $L$에 균등한 진술이 아니다. 논문은 이 항등식이 Ghirlanda–Guerra 항등식과 같다고 주장하지 않고(선행 연구와의 관계는 intuition으로만 [[g:tree-identity]]의 물리 대응 칸에 있다), overlap 분포의 형태를 정하지도 않는다. "상태"는 perturbed [[g:reservoir|reservoir]]의 [[g:hierarchy|보조 계층]] prefix $\mathscr F_{e-1}$(root 포함)이며 [[g:physical-pure-state|물리적 pure state]]가 아니다.
abstraction: approximation
children: [decor:overlap-concentration.s2.s1, decor:overlap-concentration.s2.s2]
source:
  - {file: decorrelation.tex, lines: [537, 570]}
status: proposed
---

**증명의 뼈대.** [[decor:overlap-concentration.s2.s1]]: old tree $S$에 marker anchor를 두고 anchor와 $e-1$에서 갈라지는 $S$의 사본 하나를 target으로 요구하면, 모든 확장이 fresh 부분 tree를 만들고 양쪽 총 계수가 같은 0 아닌 수 $C(S,e)=-\delta\kappa(S)$이다. [[decor:overlap-concentration.s2.s2]]: target과 old 사본은 $\mathscr F_{e-1}$가 주어지면 조건부 i.i.d.이므로 $f=R_S$일 때 항등식이 $C(S,e)\operatorname{Var}(M)=o_N(1)$이 된다. 고정 $L$에서 $C(S,e)$로 나눈다.
