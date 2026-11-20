# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| TS_TI | 부모 지도에서 받는 것 | [0,0] | ext | X_TI · Thm pert:tree-identity | Prescribed tree 위의 항등식 (marker anchor) | $\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\,\mathbb E[fR_E]$ $\quad-\,\mathbb Ef\sum_{E\in\mathfrak E(\{a_*\},a_*,\mathcal C)}c_E\,\mathbb E[R_E]\to0$ | perturbations.tex 427–465 |
| TS_SET | 부모 지도에서 받는 것 | [0,0] | ext | T_SET (증명 2) | $e-1$에서의 marker anchor | old tree $=S$, target $=$ anchor에서 $e-1$에 갈라진 $S$의 사본, $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$ | decorrelation.tex 537–545 |
| TS_C | 부모 지도에서 받는 것 | [1,0] | ext | T_C · eq decor:marker-coefficient | 양쪽의 extension 계수 | $\sum_{E}c_E=C(S,e)=-\delta\,\kappa(S)\neq0$ (두 쪽 모두) | decorrelation.tex 544–549; trees.tex 336–386 |
| TS_SAMP | 부모 지도에서 받는 것 | [1,0] | ext | X_SAMP · §3 표본 규칙 | Projectivity와 조건부 독립 | 잎을 지워도 남은 법칙 그대로 · 갈라짐 아래 subtree는 prefix가 주어지면 독립 | trees.tex 29–39 |
| TS_APPLY | T_SIDES · 두 쪽의 계산 | [2,1] | 보통 | 항등식 적용 | $\mathcal T=S$, $f=R_S$로 놓기 | $\sum_{E}c_E\,\mathbb E[R_S\,R_E]\;-\;\mathbb ER_S\sum_{E\,(\text{anchor만})}c_E\,\mathbb E[R_E]=o_N(1)$ | decorrelation.tex 550–552 |
| TS_LSHAPE | T_SIDES · 두 쪽의 계산 | [0,2] | 보통 | old-tree 쪽 · 모양 | 모든 허용 history가 같은 결합 tree를 준다 | $\sum_E c_E\,\mathbb E[R_SR_E]=C(S,e)\,\mathbb E\big[R_S^{\mathrm{old}}R_S^{\mathrm{tgt}}\big]$ | decorrelation.tex 537–553 |
| TS_RSHAPE | T_SIDES · 두 쪽의 계산 | [1,2] | 보통 | anchor만 있는 쪽 · 모양 | Old tree를 anchor 하나로 줄인 쪽 | $\mathbb ER_S\sum_{E\,(\text{anchor만})}c_E\,\mathbb E[R_E]=\mathbb ER_S\cdot C(S,e)\cdot\mathbb E[R_E]$ | decorrelation.tex 544–546, 553–555 |
| TS_CI | T_SIDES · 두 쪽의 계산 | [0,3] | 보통 | old-tree 쪽 · 조건부 iid | 조건부 기대값이 $M^2$ | $\mathbb E\big[R_S^{\mathrm{old}}R_S^{\mathrm{tgt}}\mid\mathscr F_{e-1}\big]=M\cdot M=M^2$ | decorrelation.tex 550–553 |
| TS_DEL | T_SIDES · 두 쪽의 계산 | [1,3] | 보통 | anchor만 있는 쪽 · continuation 삭제 | Target의 평균은 보통의 $\mathbb ER_S$ | $\mathbb E[R_E]=\mathbb ER_S\ \Rightarrow\ $ 이쪽 $=C(S,e)\,(\mathbb ER_S)^2$ | decorrelation.tex 553–555 |
| TS_SUB | T_SIDES · 두 쪽의 계산 | [2,4] | 보통 | 두 쪽을 넣기 | 항등식이 주는 식 | $C(S,e)\,\mathbb EM^2-C(S,e)\,(\mathbb ER_S)^2=o_N(1)$ | decorrelation.tex 556–561 |
| TS_VAR | T_SIDES · 두 쪽의 계산 | [2,5] | key | eq decor:marker-variance-identity | $C(S,e)\,\mathrm{Var}(M)=o_N(1)$ | $C(S,e)\big(\mathbb EM^2-(\mathbb ER_S)^2\big)=C(S,e)\,\mathrm{Var}(M)=o_N(1)$ | decorrelation.tex 557–561 |
| TS_U_VM | T_SIDES · 두 쪽의 계산 | [2,6] | 보통 | → T_VM (decorrelation.tex 562–569) | 쓰임: $C(S,e)$로 나눔 | $C(S,e)\neq0$이므로 $\mathrm{Var}(M)\to0$ ($L,S,e$ 고정) | decorrelation.tex 562–569 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | TS_TI | TS_APPLY | marker anchor 항등식 | key |
| 1 | TS_SET | TS_APPLY | old tree $S$, constraint | 입력 |
| 2 | TS_APPLY | TS_LSHAPE | old-tree 쪽 | key |
| 3 | TS_APPLY | TS_RSHAPE | anchor만 있는 쪽 | key |
| 4 | TS_SET | TS_LSHAPE | target은 $e-1$의 fresh subtree | 입력 |
| 5 | TS_C | TS_LSHAPE | $\sum c_E=C(S,e)$ | 입력 |
| 6 | TS_C | TS_RSHAPE | 같은 reference tree → 같은 $C$ | 입력 |
| 7 | TS_LSHAPE | TS_CI | $\mathbb E[R^{\mathrm{old}}R^{\mathrm{tgt}}]$ | key |
| 8 | TS_SAMP | TS_CI | $\mathscr F_{e-1}$ 아래 조건부 iid | 입력 |
| 9 | TS_RSHAPE | TS_DEL | $\mathbb E[R_E]$ | key |
| 10 | TS_SAMP | TS_DEL | projectivity | 입력 |
| 11 | TS_CI | TS_SUB | $C\,\mathbb EM^2$ | key |
| 12 | TS_DEL | TS_SUB | $C(\mathbb ER_S)^2$ | key |
| 13 | TS_SUB | TS_VAR | $\mathbb EM=\mathbb ER_S$ | key |
| 14 | TS_VAR | TS_U_VM | $C\neq0$, 고정 $L$ | key |
