---
id: x:model-hypothesis-remarks
kind: remark
title: '가정에 대한 주석: 퇴화 경우와 승수 $a$'
uses: [model:factorization]
provides: 'upper:bound 증명 첫 단락(upper.tex 18–23: 퇴화 경우의 spin 무관 상호작용, (ii)와 같은 관찰)과 upper:regularization(upper.tex 71–72: $\log a$ 의 적분 가능성 없이 $a$ 를 먼저 없앰, (iii)). 두 곳 모두 같은 사실을 스스로 다시 적으므로 받아 써도 되고 안 써도 된다. 이 카드는 upper:bound에 기대지 않으므로 받아 써도 순환이 없다. main:theorem.s1은 (iii)과 같은 사실을 reduction.tex 46–47에 직접 적으므로 uses에 넣지 않고 본문에서 가리킨다'
math: |
  (ii) 곱 항 $b\prod_\ell f_\ell(s_\ell)$ 이 항등적으로 0이면 상호작용은 spin 무관이고 $b=0$ 으로 잡아도 된다.
  (iii) (2.3)의 승수 $a$ 는 표현의 다른 모든 변수에 의존해도 된다. $\log a$ 의 별도 적분 가능성은 가정하지 않는다.
physics: |
  (2.3)의 [[g:factorization|전개]]에서 정규화 상수 $a$ 는 자유롭고(spin에 의존하지 않는 무작위 에너지 원점), 실제 제약은 $b$ 와 $f$ 에 있다. 곱 항이 없으면 factor는 spin과 무관한 상수다.
gap: |
  "에너지 원점"은 $a$ 가 spin에 의존하지 않기 때문에 맞는 읽기다. 다만 $a$ 가 $f_\ell$ 들에 비대칭으로 의존할 수 있어서 원래 $\theta$ 의 법칙은 입력 순열에 불변이 아닐 수 있다. 이것을 [[g:constant-shift|상수 이동]] $\widehat\theta=\theta-\theta(1,\ldots,1)$ 로 없애는 것이 main:theorem.s1이다. 물리 문장은 이 비대칭을 말하지 않는다.
abstraction: weakening
children: []
source:
  - {file: model.tex, lines: [41, 44]}
status: proposed
---

번호 (ii), (iii)은 원래의 번호를 유지한다. 원래 (i)("비퇴화 경우 (2.4)의 기대값이 자동으로 유한", model.tex 38–41)은 upper:bound의 증명에 기대므로 [[x:model-moment-finiteness]]로 떼었다. 이 카드는 이제 upper:bound에 기대지 않는다.

model.tex 41행은 (i)의 끝("as shown in upper:bound")과 (ii)의 시작("If the product term")을 함께 담고 있어 두 카드의 범위가 그 줄에서 겹친다. 41행의 `\cref{upper:bound}`는 (i)에 속한다.
