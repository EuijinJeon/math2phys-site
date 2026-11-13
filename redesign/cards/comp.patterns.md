---
id: comp:patterns
kind: lemma
title: 'Empirical-pattern comparison (경험 pattern 비교)'
uses: [comp:encoding, comp:encoding.s4, tree:multioverlap, x:tree-sampling, cavity:increment]
provides: 'comp:insertion-comparison.s3 (차수 $k$ 항의 평가 오차 $\le pM\sum_{S\ne\varnothing}\mathbb E\lvert R_S-\mathbb ER_S\rvert$, comparison.tex 207–209). 규칙 P11, L1 수 6'
math: |
  leaf가 $k$ 개인 prescribed tree를 고정한다. 절댓값이 1 이하인 관측량이 $a$ 개의 독립 균일 site label에서의 replica-spin pattern을 쓴다고 하자. 이 pattern들을 comp:encoding의 독립 trial label pattern $a$ 개로 바꾸면 그 기대값은 많아야
  $$a\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\lvert R_S-\mathbb ER_S\rvert\tag{comp:pattern-error}$$
  만큼 바뀐다. 관측량은 reservoir와 독립인 새 insertion disorder에도 의존해도 된다.
physics: |
  leaf $k$ 개의 [[g:prescribed-tree|prescribed tree]]를 고정한다. [[g:reservoir|reservoir]]에서 독립 균일하게 고른 site label $a$ 개의 [[g:replica|replica]] [[g:spin-pattern|spin pattern]]을 [[g:encoded-law|encoded law]]의 서로 독립인 label 사본으로 바꿔도([[g:independent-copies]]), 절댓값이 1 이하인 관측량의 기대값은 그 tree의 [[g:multioverlap|multioverlap]] 평균 절대 요동의 합에 $a$ 를 곱한 것, 곧 $a\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\lvert R_S-\mathbb ER_S\rvert$ 이하만 바뀐다. 관측량은 reservoir와 독립인 새 삽입 disorder에 의존해도 된다.
gap: |
  (1) 정확한 부등식이다. tree 하나를 고정한 진술이고 tree 법칙 평균은 comp:shape-error가 한다. (2) site는 고정된 이웃이 아니라 복원추출한 독립 균일 label이다. 고정한 두 site의 결합 법칙이 곱이라는 말이 아니고, 그래프의 국소 구조나 거리를 쓰지 않는다. (3) 우변이 작다는 것은 이 lemma가 아니라 [[g:overlap-concentration]](comp:shape-error)에서 온다.
abstraction: exact
children: [comp:patterns.s1, comp:patterns.s2]
source:
  - {file: comparison.tex, lines: [85, 97]}
  - {file: comparison.tex, lines: [99, 121]}
status: proposed
---

**증명의 뼈대.** [[comp:patterns.s1]]: reservoir 배치가 주어지면 균일 site의 pattern 분포는 $\pi(\mathbf e)=2^{-k}\sum_SR_S\prod_{b\in S}e_b$ 이고 trial label의 분포는 $\bar\pi=\mathbb E\pi$ 다. [[comp:patterns.s2]]: 곱측도의 telescoping $\lVert\pi^{\otimes a}-\bar\pi^{\otimes a}\rVert_{\rm TV}\le a\lVert\pi-\bar\pi\rVert_{\rm TV}\le\frac a2\sum_{S\ne\varnothing}\lvert R_S-\mathbb ER_S\rvert$ 를 기대값으로 옮긴다.

**두 쪽의 차이가 어디서 나는가.** reservoir 쪽에서는 $a$ 개 site가 같은 reservoir 배치를 보므로 조건부로 $\pi^{\otimes a}$ 이고 $\pi$ 자체가 무작위다. trial 쪽은 label마다 전체 구성의 독립 사본이라 $\bar\pi^{\otimes a}$ 다([[comp:encoding.s4]]). 두 쪽의 차이는 $\pi$ 의 요동, 곧 $R_S$ 의 요동뿐이다.
