---
id: x:model-hypothesis-remarks
kind: remark
title: '가정에 대한 주석: 유한성, 퇴화 경우, 승수 $a$'
uses: [model:factorization, model:positivity, upper:bound]
provides: 'upper:bound 증명 첫 단락(upper.tex 17–34: 퇴화 경우 처리와 $b$, $M$ 의 본질적 유계성), main:theorem.s1($a$ 가 입력에 비대칭으로 의존할 수 있음), upper:regularization($\log a$ 를 피하는 정규화)'
math: |
  (i) 비퇴화 경우, 독립성과 엄격한 곱 한계 (2.3)이 $b$ 와 $\max_s\lvert f_1(s)\rvert$ 를 본질적으로 유계로 만들므로 (2.4)의 기대값은 자동으로 유한하다. 원문은 이것을 upper:bound(의 증명)에서 보인다고 미리 말한다.
  (ii) 곱 항이 항등적으로 0이면 상호작용은 spin 무관이고 $b=0$ 으로 잡아도 된다.
  (iii) 승수 $a$ 는 표현의 다른 모든 변수에 의존해도 된다. $\log a$ 의 별도 적분 가능성은 가정하지 않는다.
physics: |
  (2.3)의 [[g:factorization|전개]]에서 정규화 상수 $a$ 는 자유롭고(에너지 원점의 무작위 이동), 실제 제약은 $b$ 와 $f$ 에 있다. 엄격한 곱 한계가 사실상 $\lvert\tanh\rvert<1$ 의 균일한 형태라서 모든 moment가 유한하다.
gap: |
  "에너지 원점"은 $a$ 가 spin에 의존하지 않기 때문에 맞는 읽기다. 다만 $a$ 가 $f_\ell$ 들에 비대칭으로 의존할 수 있어서 원래 $\theta$ 의 법칙은 입력 순열에 불변이 아닐 수 있다. 이것을 [[g:constant-shift|상수 이동]] $\widehat\theta=\theta-\theta(1,\ldots,1)$ 로 없애는 것이 main:theorem.s1이다. (i)의 유계성 상수는 upper.tex 25–29에 있다: $\mathbb P(M\ge u)>0$, $\mathbb P(\lvert b\rvert\ge v)>0$ 이면 $\lVert b\rVert_\infty\le u^{-p}$, $\lVert M\rVert_\infty\le(vu^{p-1})^{-1}$.
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [38, 44]}
status: proposed
---

(i)의 "nondegenerate"는 upper.tex 18–20의 대우로 읽었다: $b=0$ a.s. 도 아니고 $M=\max_{s=\pm1}\lvert f(s)\rvert=0$ a.s. 도 아닌 경우. 퇴화 경우에 상한은 $F_N=\mathcal B_r=\log2+\mathbb E\log\cosh h+\alpha\mathbb Ec$ 로 직접 맞는다(upper.tex 20–23).
