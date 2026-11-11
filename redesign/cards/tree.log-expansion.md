---
id: tree:log-expansion
kind: lemma
title: 'Logarithmic expansion (log 전개)'
uses: [tree:Q-rule, tree:telescoping, tree:first-variation, x:tree-differentiation-rule, x:tree-analytic-bounds, tree:Y-recursion]
provides: '§4 upper:bound (upper.tex 81, 97–121: 정규화된 증분의 전개와 차수 n 계수, Q_n이 세 삽입에 공통). §8 comp:insertion-comparison (comparison.tex 123의 Q_k, 205–211: 차수별 비교와 꼬리 Σ_{k>q} c^k/k). tree:averaging-remark'
math: |
  유계 실수 path 함수 $D$와 $A=1+tD$에 대해
  $$\log Y_0=\sum_{k\geq1}\frac{(-1)^{k-1}t^k}{k}\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a,\qquad |t|\|D\|_\infty<1.$$
  이 항등식은 root가 주어진 조건부다. $|t|\|D\|_\infty\leq c<1$이면 차수 $K$ 뒤의 나머지의 절댓값은
  $$\sum_{k>K}\frac{c^k}{k}$$
  이하다. (작성자 보탬, 원문 문맥에서 읽은 것: $Y_0$은 insertion 전 kernel로 계산한 (tree:Y-recursion), $\mathcal T$는 $Q_k$로 뽑은 tree, $E_{\mathcal T}$는 그 위의 원래 kernel 표본 기대값이다.)
physics: |
  [[g:insertion|insertion]] $A=1+tD$의 효과 $\log Y_0$는 [[g:tree-law|tree 법칙]] $Q_k$로 뽑은 $k$개 [[g:replica|replica]] tree 위에서 $D$의 곱의 평균을 계수 $(-1)^{k-1}t^k/k$로 더한 급수다. $L=1$이면 모든 replica가 독립 Gibbs 표본이라 $\mathbb E_{Q_k}E_{\mathcal T}\prod_aD^a=\langle D\rangle^k$이고, 식은 $\log(1+t\langle D\rangle)$의 Taylor 급수다. $L\ge2$에서는 $\langle D\rangle^k$ 자리에 계층 [[g:state|상태]]를 공유하는 replica들의 결합 평균이 들어간다.
gap: |
  root가 주어진 조건부 항등식이고, 수렴 영역은 $|t|\|D\|_\infty<1$이다. 유한 깊이 $L$의 임의의 kernel 열에 대해 정확히 성립하며 $n\to0$ 연속을 쓰지 않는다. $Q_k$를 물리 그림의 replica overlap tree 법칙으로 읽는 것은 [[g:tree-law]]의 물리 대응 칸에 intuition으로만 있다.
abstraction: exact
children: [tree:log-expansion.s1, tree:log-expansion.s2]
source:
  - {file: trees.tex, lines: [224, 239]}
  - {file: trees.tex, lines: [241, 257]}
status: proposed
---

**증명의 뼈대.** [[tree:log-expansion.s1]]: 1차 도함수는 updated path 하나 위의 $D/A$이고 그 leaf를 [[g:protected-leaf|protected]]로 둔다. 그 뒤로는 모든 leaf가 protected이므로 [[x:tree-differentiation-rule]]의 미분은 fresh path만 붙인다. 계수는 모두 음이고, [[tree:telescoping]]으로 정규화하면 절댓값의 곱이 $(k-1)!\,Q_k$ 확률이다. 그래서 $k$차 도함수가 $(-1)^{k-1}(k-1)!\,\mathbb E_{Q_k}E_{\mathcal T}\prod D^a$다. [[tree:log-expansion.s2]]: 해석성([[x:tree-analytic-bounds]])이 급수를 확정하고, 계수 크기 $\le\|D\|_\infty^k/k$가 수렴 영역과 꼬리 경계를 준다.

$L=1$ 점검(작성자): $Q_k$는 모든 path를 root에서 가르고([[tree:Q-rule]] 끝 메모), $\log(1+t\langle D\rangle)=\sum_k(-1)^{k-1}t^k\langle D\rangle^k/k$. 섭동론의 cumulant 전개($\log\langle e^{tD}\rangle$)가 아니라 $\log\langle1+tD\rangle$의 전개다.
