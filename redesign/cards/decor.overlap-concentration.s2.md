---
id: decor:overlap-concentration.s2
kind: step
title: 'marker anchor로 prefix 사영 $M$을 집중시키기'
uses: [pert:tree-identity, tree:reference-total, x:decor-tree-sampling, x:decor-mesh]
provides: 'decor:overlap-concentration.s4 (Var(M)→0)'
math: |
  $|S|\ge2$, 첫 갈라짐 $e$, $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$이라 하면 각 고정 $L$, $S$, 깊이 배정에서 $\operatorname{Var}(M)\to0$ ($N\to\infty$).
physics: |
  깊이 $e-1$ 상태에서의 평균 overlap $M$은 상태와 disorder에 따라 요동하지 않는다(상태 사이 요동의 소멸). marker anchor를 쓴 Ghirlanda–Guerra 형 항등식에서 나온다.
gap: |
  고정 $L$과 고정 깊이에서, 선택된 perturbed 수열을 따라 $N\to\infty$로만 성립한다. 계수 $C(S,e)=-\delta\kappa(S)$로 나누므로 $L$에 균등한 진술이 아니다. 고전적 GG 항등식처럼 overlap 분포의 형태를 정하지는 않는다.
abstraction: approximation
children: [decor:overlap-concentration.s2.s1, decor:overlap-concentration.s2.s2]
source:
  - {file: decorrelation.tex, lines: [537, 570]}
status: proposed
---

**증명의 뼈대.** [[decor:overlap-concentration.s2.s1]]: old tree $S$에 marker anchor를 두고 anchor와 $e-1$에서 갈라지는 $S$의 사본 하나를 target으로 요구하면, 모든 확장이 fresh 부분 tree를 만들고 양쪽 총 계수가 같은 0 아닌 수 $C(S,e)=-\delta\kappa(S)$이다. [[decor:overlap-concentration.s2.s2]]: target과 old 사본은 $\mathscr F_{e-1}$가 주어지면 조건부 i.i.d.이므로 $f=R_S$일 때 항등식이 $C(S,e)\operatorname{Var}(M)=o_N(1)$이 된다. 고정 $L$에서 $C(S,e)$로 나눈다.
