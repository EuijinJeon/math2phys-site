# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| DC_ME | B_DC · 세부 유도 | [0,0] | 보통 | eq decor:martingale-energy | 한 path의 martingale energy | $\sum_t\mathbb E\\|\mu_{t+1,T}-\mu_{t,T}\\|_N^2\le1$ | decorrelation.tex 168–175 |
| DC_EVAL | B_DC · 세부 유도 | [0,1] | 보통 | eq decor:evaluation-depth-continuity | 평가 깊이의 이동 | $\mathcal A_{L,\eta}\mathbb E\\|\mu_{d+1,S}-\mu_{d,S}\\|_N^2\le1/L$ | decorrelation.tex 154–163, 168–177 |
| DC_PROD | B_DC · 세부 유도 | [0,1] | 보통 | Lemma decor:depth-continuity | 갈라짐 한 칸 지연 | $\prod_j\mu_{q,T_j}\quad\longleftrightarrow\quad\mathbb E[\prod_j\mu_{q+1,T_j}\mid\mathscr F_q]$ | decorrelation.tex 179–185 |
| DC_ONE | B_DC · 세부 유도 | [0,2] | 보통 | eq decor:one-vertex-shift | 곱 차이의 제곱 경계 | $\mathbb E\\|\prod_j\mu_{q,T_j}-\mathbb E[\prod_j\mu_{q+1,T_j}\mid\mathscr F_q]\\|_N^2\le s\sum_j\mathbb E\\|\mu_{q+1,T_j}-\mu_{q,T_j}\\|_N^2$ | decorrelation.tex 185–193 |
| DC_SUM | B_DC · 세부 유도 | [0,3] | 보통 | Lemma decor:depth-continuity | 갈라짐 깊이 평균 | $L^{-1}\sum_q s\sum_j\mathbb E\\|\mu_{q+1,T_j}-\mu_{q,T_j}\\|_N^2\le s^2/L$ | decorrelation.tex 194–195 |
| DC_ALL | B_DC · 세부 유도 | [0,4] | 보통 | Lemma decor:depth-continuity | 상위 prefix와 여러 이동 | $\mathcal A_{L,\eta}\mathbb E\\|\mu_{d,S^U}-\mu_{d,S}\\|_N^2\le C/L$ | decorrelation.tex 195–205 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | DC_ME | DC_EVAL | 깊이 평균 | 입력 |
| 1 | DC_PROD | DC_ONE | 곱 차이와 Jensen | 입력 |
| 2 | DC_ONE | DC_SUM | 갈라짐 깊이마다 더함 | 입력 |
| 3 | DC_ME | DC_SUM | 자식마다 energy | 입력 |
| 4 | DC_SUM | DC_ALL | 위쪽 전파와 여러 이동 | 입력 |
