# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| XS_KER | §3 정의에서 받는 것 | [0,0] | ext | §3 path kernel | Path kernel과 prefix | $K_d(dz\mid\mathscr F_{d-1}),\quad \int K_d(dz\mid\cdot)=1$ | trees.tex 16–23 |
| XS_TREE | §3 정의에서 받는 것 | [1,0] | ext | §3 tree 표본 규칙 | Finite tree의 표본 규칙 | 각 vertex에서 서로 다른 child는 그 vertex의 prefix가 주어지면 kernel로 독립하게 뽑는다 | trees.tex 29–37 |
| XS_JOINT | X_SAMP · 유도와 §7의 쓰임 | [2,1] | 보통 | 표본 규칙의 식 | Tree law = edge마다 kernel 하나의 곱 | $P_{\mathcal T}(dx)=\prod_{v\neq\text{root}}K_{d_v}\big(dx_v\mid x_{\mathrm{anc}(v)}\big)$ | trees.tex 29–34, 126–131 |
| XS_PROJ | X_SAMP · 유도와 §7의 쓰임 | [0,2] | 보통 | §3 잎 제거 (projectivity) | 잎을 지워도 남은 tree의 법칙은 그대로 | $\int P_{\mathcal T}(dx)\,\big\|_{\mathcal T'}=P_{\mathcal T'}\qquad(\mathcal T'\subset\mathcal T)$ | trees.tex 38–39; 201 |
| XS_CI | X_SAMP · 유도와 §7의 쓰임 | [1,3] | 보통 | §3 child 조건부 독립 | 갈라짐 아래 subtree들의 조건부 독립 | $\mathcal T$가 깊이 $e$에서 $T_1,\dots,T_s$로 처음 갈라지면, $\mathscr F_e$ 아래 $T_j$의 continuation들은 독립 | trees.tex 32–33, 201–202; decorrelation.tex 209 |
| XS_U_DC | X_SAMP · 유도와 §7의 쓰임 | [0,4] | 보통 | → B_DC (decorrelation.tex 204–205) | 쓰임: 큰 tree 안에서도 한 prefix 주변법칙 불변 | 다른 branch를 지워도 one-prefix 주변법칙 그대로 $\Rightarrow$ 추정이 더 큰 tree에서도 성립 | decorrelation.tex 204–205 |
| XS_U_PB | X_SAMP · 유도와 §7의 쓰임 | [1,4] | 보통 | → B_PB (decorrelation.tex 208–210) | 쓰임: 조건부 평균의 인수분해 | $\mu_{e,S}=\prod_{j=1}^s\mu_{e,T_j}$ | decorrelation.tex 208–210 |
| XS_U_SIDES | X_SAMP · 유도와 §7의 쓰임 | [0,4] | 보통 | → T_SIDES (decorrelation.tex 553–555) | 쓰임: marker continuation 삭제 | anchor만 있는 쪽: marker의 $e-1$ 아래 continuation 삭제 $\Rightarrow$ 보통 법칙 $S$, 평균 $\mathbb ER_S$ | decorrelation.tex 550–555 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | XS_KER | XS_JOINT | kernel $K_d$ | 입력 |
| 1 | XS_TREE | XS_JOINT | child 독립 규칙 | 입력 |
| 2 | XS_JOINT | XS_PROJ | 자손 없는 vertex부터 적분 | key |
| 3 | XS_KER | XS_PROJ | $\int K_d=1$ | 입력 |
| 4 | XS_JOINT | XS_CI | factor가 subtree별로 나뉨 | key |
| 5 | XS_PROJ | XS_CI | factor = 작은 tree의 법칙 | 입력 |
| 6 | XS_PROJ | XS_U_DC | 다른 branch 삭제 | key |
| 7 | XS_CI | XS_U_PB | 조건부 독립 → 곱 | key |
| 8 | XS_PROJ | XS_U_PB | $\mu_{e,T_j}$로 식별 | 입력 |
| 9 | XS_PROJ | XS_U_SIDES | continuation 삭제 | key |
