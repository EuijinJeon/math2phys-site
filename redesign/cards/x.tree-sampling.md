---
id: x:tree-sampling
kind: definition
title: '유한 tree, 표본 기대값 $E_{\mathcal T}$, split, 사영 일관성'
uses: [x:tree-path-kernels]
provides: '§3 전체 (tree 밀도, 미분 규칙, 확장, Q_k). §7은 이것을 x:decor-tree-sampling으로 다시 적어 쓴다. §5 cavity.tex 117–118 ("all spin trees are sampled from this reservoir"), §4 upper:bound (tree:log-expansion을 거친 replica tree, upper.tex 81, 97–112, 120–121), §6 pert:score-identity·pert:palm·제약 ("The anchor marginal is always one tilted path", sampled tree 안의 위치, perturbations.tex 321, 516–517), §8의 induced subtree. §4·§6·§8 사용은 \ref 없음'
math: |
  유한 tree $\mathcal T$는 공통 root와 유한 개의 labeled path로 이루어지며 각 path는 깊이 $L$에서 끝난다. 모든 내부 vertex는 자식이 적어도 하나다. 특히 path의 unary 부분은 모두 남긴다. 각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑힌다. 이 표본 기대값을 root가 주어진 조건부로 $E_{\mathcal T}$라 쓴다. 깊이 $d$의 split이란 마지막 공통 vertex가 깊이 $d$에 있다는 뜻이다. 깊이 $L$의 replica 위치는 서로 다른 vertex이지만 그곳에서 뽑힌 값이 다를 필요는 없다. 따라서 독립 spin replica가 같은 spin 배치일 수 있다. 일부 leaf와, 남은 leaf가 쓰지 않는 그 path 부분을 지워도 남은 tree의 표본 법칙은 보존된다.
physics: |
  [[g:prescribed-tree|prescribed tree]]는 [[g:replica|replica]]들의 계층 그림이다: leaf마다 replica 하나가 있고, 두 replica는 split 깊이까지 같은 [[g:state|상태]](같은 prefix vertex)를 지나며 그 아래로는 그 상태가 주어지면 조건부 독립으로 뽑힌다. 일부 replica를 잊어도 나머지의 결합 법칙은 바뀌지 않는다.
gap: |
  물리 문장은 다음 내용을 생략한 약화다: unary 구간 보존, 말단의 서로 다른 vertex와 같은 표본값의 구별, root 조건부 기대값의 약속을 생략한다.
  조건부 독립은 보조 계층 kernel의 구성에서 오는 것이고([[g:hierarchy]]), Gibbs 측도의 [[g:physical-pure-state|물리적 pure state]] 분해에서 유도된 것이 아니다. 서로 다른 leaf의 spin 배치가 같을 수 있다(특히 $L=1$이면 replica들은 같은 Gibbs 측도의 독립 표본이고, $L\ge2$에서도 값의 일치는 배제되지 않는다).
abstraction: weakening
children: []
source:
  - {file: trees.tex, lines: [29, 39]}
status: proposed
---

"Every internal vertex has at least one child; in particular, all unary portions of paths are retained"(30–31)는 tree가 깊이마다 vertex를 다 가진다는 뜻이다. 그래서 내부 vertex 집합 $\operatorname{Int}(\mathcal T)$에는 root와 모든 unary vertex가 들어가고, $\gamma_\beta$와 $Q_k$의 선택지가 unary vertex에서도 생긴다([[tree:insertion]], [[tree:Q-rule]]).

사영 일관성(38–39)과 자식의 조건부 독립은 뒤의 미분 규칙에서 다시 정당화 근거로 불린다(trees.tex 200–202, [[x:tree-differentiation-rule]]). §7의 [[x:decor-tree-sampling]]은 이 카드의 내용에 "부분 tree는 prefix가 주어지면 나머지와 조건부 독립"이라는 유도된 꼴을 더해 적은 것이다.
