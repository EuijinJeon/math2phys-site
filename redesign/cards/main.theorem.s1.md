---
id: main:theorem.s1
kind: step
title: '상수 이동으로 승수 $a$ 제거와 순열 불변성'
uses: [model:factorization, model:integrability]
provides: 'main:theorem.s2(순열 불변인 $\widehat\theta$, $\mathbb EB(\widehat\theta)<\infty$), main:theorem.s3($\widehat\theta$ 가 (2.1)을 만족해 reduction:stability가 적용됨, 적분 가능한 되돌릴 상수 $c$)'
math: |
  승수 $a$ 는 label 붙은 입력 함수들에 비대칭으로 의존할 수 있으므로 원래 상호작용 법칙은 순열 불변이 아닐 수 있다. $c=\theta(1,\ldots,1)$, $\widehat\theta=\theta-c$ 로 둔다. $\lvert c\rvert\le B(\theta)$ 이므로 $c$ 는 적분 가능하다. (2.3)에서
  $$\widehat\theta(s)=\log\frac{1+b\prod_{\ell=1}^pf_\ell(s_\ell)}{1+b\prod_{\ell=1}^pf_\ell(1)}.$$
  $a$ 가 사라졌다. $f_\ell$ 들이 i.i.d.이고 $b$ 와 독립이므로 $\widehat\theta$ 의 법칙은 입력의 순열에 대해 불변이다. 또 $\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)<\infty$.
physics: |
  spin 무관인 무작위 상수(에너지 원점) $c=\theta(1,\ldots,1)$ 를 빼는 [[g:constant-shift|상수 이동]]이다($\lvert c\rvert\le B(\theta)$ 라 적분 가능). 그러면 factor weight는 [[g:factorization|전개]]의 $b$, $f_\ell$ 만으로 정해지고, 그 대칭 때문에 [[g:interaction|상호작용]]의 법칙이 $p$ 개 입력에 대해 대칭([[g:permutation-invariance|순열 불변]])이 된다. 이동한 상호작용도 1차 moment 가정을 지킨다: $\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)$.
gap: |
  정확하다. 상수 이동이 pressure와 functional을 같은 양 $-\alpha\mathbb Ec$ 만큼 옮긴다는 것은 이 단계가 아니라 main:theorem.s3에서 reduction:shift로 쓴다.
abstraction: exact
children: []
source:
  - {file: reduction.tex, lines: [45, 59]}
status: proposed
---

$\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)$ 는 $\lvert\widehat\theta(s)\rvert\le\lvert\theta(s)\rvert+\lvert c\rvert\le2B(\theta)$ 에서 온다(원문은 결과만 적는다). 순열 불변성은 분자의 $\prod_\ell f_\ell(s_\ell)$ 와 분모의 $\prod_\ell f_\ell(1)$ 의 결합 법칙이 $(f_1,\ldots,f_p)$ 의 순열에 대해 불변이고 $b$ 가 그것과 독립이라는 데서 나온다.

첫 문장(승수 $a$ 의 비대칭 의존)은 reduction.tex 46–47에 직접 적혀 있고, 같은 사실을 가정 쪽에서 적은 주석이 [[x:model-hypothesis-remarks]] (iii)이다. 이 단계는 그 주석을 `uses`에 넣지 않는다.
