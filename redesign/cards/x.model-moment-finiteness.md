---
id: x:model-moment-finiteness
kind: remark
title: '(2.4)의 기대값이 자동으로 유한한 경우 (비퇴화 경우)'
uses: [model:factorization, model:positivity, upper:bound.s1]
provides: '받아 쓰는 카드 없음(예고 주석). 증명은 §4 상한 명제의 증명 첫 단락(upper.tex 17–34)에 있고 그쪽은 이 카드를 쓰지 않고 스스로 증명한다. 이 카드를 uses에 넣는 카드는 그 상한 명제에 기대게 되므로, §4 카드와 하한 쪽 카드는 이 카드를 uses에 넣지 않는다'
math: |
  (2.4)의 기대값은 유한한 실수 기대값으로 해석한다(model:positivity). 비퇴화 경우에는 이것이 자동이다: $b$ 와 $f_\ell$ 들의 독립성과 엄격한 곱 한계 (2.3)이 $b$ 와 $\max_s\lvert f_1(s)\rvert$ 를 본질적으로 유계로 만든다. 원문은 이것을 upper:bound(의 증명)에서 보인다고 미리 말한다.
physics: |
  [[g:factorization|전개]]의 계수 $b$ 와 단일 spin 인자 $f$ 가 서로 독립이고 곱이 a.s. 1보다 작으면, 비퇴화 경우에는 둘 다 본질적으로 유계이고 [[g:positivity|부호 조건]] (2.4)의 moment가 모두 유한하다.
gap: |
  정확하다. 조건이 둘이다: 비퇴화(곱 항이 항등적으로 0이 아님)와 독립성(upper.tex 26 "independence gives"). 퇴화 경우에는 곱 한계가 $b$ 를 제약하지 않으며, 그때는 $b=0$ 으로 잡는다(x:model-hypothesis-remarks (ii)). 얻는 한계는 $\mathbb P(M\ge u)>0$, $\mathbb P(\lvert b\rvert\ge v)>0$ 인 $u,v>0$ 에 대해 $\lVert b\rVert_\infty\le u^{-p}$, $\lVert M\rVert_\infty\le(vu^{p-1})^{-1}$ 이고($M=\max_{s=\pm1}\lvert f(s)\rvert$, upper.tex 24–30), 1보다 클 수 있다. 두 명명 예에서는 $M=1$ 이라 $\lvert b\rvert<1$ 이지만(Viana–Bray $b=\tanh\beta J$, consequences.tex 26–30; soft SAT $0\le-b<1$, consequences.tex 59–61), 일반적으로 표현은 $f\mapsto\lambda f$, $b\mapsto\lambda^{-p}b$ 로 척도를 옮길 수 있어 "$b$ 가 tanh처럼 1 미만"은 성립하지 않는다(작성자 관찰).
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [38, 41]}
status: proposed
---

이 카드는 원래 [[x:model-hypothesis-remarks]]의 (i)이었다. (i)만 upper:bound의 증명에 기대므로 따로 떼었다. 그래서 (ii), (iii)을 받아 쓰는 카드(§4의 upper 카드, [[main:theorem.s1]]의 본문)는 upper:bound에 전이적으로 기대지 않고, upper:bound 카드가 (ii)·(iii)을 가리켜도 순환이 생기지 않는다.

"nondegenerate"는 upper.tex 18–20의 대우로 읽었다: $b=0$ a.s. 도 아니고 $M=0$ a.s. 도 아닌 경우. 이것은 "곱 항 $b\prod_\ell f_\ell(s_\ell)$ 이 a.s. 항등적으로 0"의 부정과 같다(작성자 확인: 퇴화면 곱 항이 a.s. 0이고, 비퇴화면 $\mathbb P(b\ne0)>0$, $\mathbb P(M_\ell>0)>0$ 과 독립성으로 곱 항이 양의 확률로 0이 아니다). 퇴화 경우에 상한은 $F_N=\mathcal B_r=\log2+\mathbb E\log\cosh h+\alpha\mathbb Ec$ 로 직접 맞는다(upper.tex 20–23).
