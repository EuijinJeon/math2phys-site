# 용어집 추가 제안 — §3 trees

`layers/glossary.md`의 "## Tree 계산과 항등식" 묶음에 넣을 항목. 형식은 용어집 항목 그대로다. §3 카드가 이 slug로 링크를 건다.

### g:protected-leaf — protected leaf
- **기호**: protected leaf 집합 $C$, $E_{\mathcal T}^A[G\prod_{a\in C}(A^a)^{-1}]$
- **뜻**: tree 밀도 $W_{\mathcal T}(A)$의 leaf 인자 $A^a$가 분모 $A^a$로 상쇄된 leaf다. 이 leaf에서는 삽입 매개변수로 미분해도 새 항이 생기지 않는다. 미분으로 $D_j^a/A^a$를 받은 leaf와 새로 붙은 fresh leaf는 곧바로 protected가 된다.
- **역할**: 미분 규칙(`x:tree-differentiation-rule`)의 회계다. 모든 leaf가 protected이면 미분은 fresh path만 붙이고 이것이 log 전개의 $Q_k$를 낳는다(`tree:log-expansion`). anchor를 처음부터 protected로 두는 것이 canceled-anchor 전개(`tree:extension-expansion`)이고, 그래서 [[g:extension-history]]의 선택지에서 anchor가 빠진다. §6의 Palm 단계에서 anchor 인자 $A^{a_*}$가 상쇄되는 것(perturbations.tex 370–371)이 이 상황이다.
- **정의 위치**: `trees.tex` 180–183, `x:tree-differentiation-rule`
- **물리 대응**: 없음.

### g:reference-path — reference path
- **기호**: anchor $a_*$와 이미 color를 받은 path; 처방된 reference 모양 $S$, 한 걸음 합 $m_d-jm_{d+1}$, $\kappa(S)$
- **뜻**: extension history에서 anchor와 이미 color를 받은 path를 말한다. 새 color에 대한 제약은 이 path들과의 갈라짐 깊이만 지정하고, 쓰지 않은 old path는 구별하지 않는다.
- **역할**: 한 걸음 계수 합이 현재 reference tree에만 의존해서 old tree와 무관한 닫힌 꼴 $\kappa(S)$가 된다(`tree:reference-total`). [[g:depth-delay]]에서 처방하는 것이 reference 모양이다(`tree:charging`). §7의 $J=\kappa(S^+)^2$, $C(S,e)=-\delta\kappa(S)$, §6 제약 $\mathcal C$("anchor와 added color 사이의 split 깊이만", perturbations.tex 433–436)가 이것을 쓴다.
- **정의 위치**: `trees.tex` 311–315, `x:tree-reference-paths`
- **물리 대응**: 없음.

## 기존 항목에 대한 메모 (고치지 않았음)

- `g:insertion`의 뜻 칸은 "$A$가 root가 주어진 조건부로 위로 유계이고 0에서 떨어져 있다"는 가정(trees.tex 73–74)과 "kernel이 그 분배함수의 tilted kernel"이라는 가정(trees.tex 85–87)을 적지 않는다.
- `g:hierarchy`의 기호 칸 $K_d=e^{m_d(X_d-X_{d-1})}P_d$는 $1\le d<L$에서만이고 $K_L$은 Gibbs kernel이다(trees.tex 58–64). 기호 칸이 $(1\le d\le L)$와 tilt 식을 한 줄에 두어 $d=L$까지 tilt 꼴로 읽힐 수 있다.
