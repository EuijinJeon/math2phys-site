---
id: tree:multioverlap
kind: definition
title: 'multioverlap $R_S$ 와 기대값 $\mathbb E$ 의 약속'
uses: [x:tree-sampling]
provides: '§6 (x:pert-test-setup의 시험함수 f, x:pert-colored-extensions의 R_E), §7 (x:decor-spin-product, 모든 집중 진술), §8 (spin pattern의 경험분포)'
math: |
  말단 변수가 spin 배치 $\sigma^a\in\{-1,1\}^N$일 때 replica leaf의 부분집합 $S$ 위 multioverlap은
  $$R_S=\frac1N\sum_{i=1}^N\prod_{a\in S}\sigma_i^a,\qquad R_\varnothing=1.$$
  이하 첨자 없는 기대값 $\mathbb E$는 root와 지시된 tree의 표본추출을 함께 포함한다.
physics: |
  [[g:multioverlap|multioverlap]]: $|S|=2$이면 보통의 [[g:replica|replica]] overlap $q_{ab}$, $|S|=1$이면 자화, 일반 $S$는 여러 replica의 spin 곱의 공간 평균이다. 빈 집합에서는 $R_\varnothing=1$ 로 둔다. 첨자 없는 $\mathbb E$ 는 root와 지정된 tree 표본을 함께 평균한다.
gap: |
  replica들은 [[x:tree-sampling]]의 tree 규칙으로 뽑힌다. 따라서 $R_S$의 분포는 replica들이 공유하는 prefix 깊이(tree 모양)에 의존한다. $\mathbb E$는 [[g:root|root]]까지 평균한 것이다. 쓰이는 곳에서 root는 물리 disorder와 섭동의 개수·type·site를 담는다. 섭동 매개변수 $\mathbf u$는 root가 아니라 고정값이고 $\mathbb E$는 그것을 평균하지 않는다(cavity.tex 29–31 "fixed, not quenched random variables", perturbations.tex 68–69).
abstraction: exact
children: []
source:
  - {file: trees.tex, lines: [41, 49]}
status: proposed
---

이 절 안에서 $R_S$는 정의만 되고 쓰이지 않는다. 받아 쓰는 곳은 §6(perturbations.tex 316–318의 시험함수 $f$, 437–449의 $R_E$), §7([[x:decor-spin-product]]), §8의 spin pattern이다.
