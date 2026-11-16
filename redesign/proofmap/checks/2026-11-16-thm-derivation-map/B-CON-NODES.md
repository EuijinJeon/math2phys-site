# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| BC_C | B_CON · 세부 유도 | [0,0] | 보통 | Lemma decor:contractions | 조건부 공분산 | $C_{ij}=\operatorname{Cov}(A_{S,i},A_{S,j}\mid\mathscr F_d)$ | decorrelation.tex 86–106 |
| BC_Q | B_CON · 세부 유도 | [0,1] | 보통 | Lemma decor:contractions | 조건부 제곱 | $\mathbb E[((A_S-\mu)\cdot B)^2\mid\mathscr F_d,B]=N^{-2}B^{\mathsf T}CB$ | decorrelation.tex 108–115, 127–130 |
| BC_CS | B_CON · 세부 유도 | [0,2] | 보통 | Lemma decor:contractions | Cauchy–Schwarz 두 번 | $\\|(A_S-\mu)\cdot B\\|_{L^2}^2\le\sqrt{v_N}$ | decorrelation.tex 127–131 |
| BC_DIFF | B_CON · 세부 유도 | [0,1] | 보통 | Lemma decor:contractions | 세 사본의 차 | $\mathbb E[(Y-Z)(Y-Z)^{\mathsf T}\mid\mathscr G]=2C$ | decorrelation.tex 117–123, 132–136 |
| BC_TRACE | B_CON · 세부 유도 | [0,2] | 보통 | Lemma decor:contractions | trace의 양의 항 | $\mathbb E[(X\cdot(Y-Z))^2]\ge 2N^{-2}\mathbb E\operatorname{tr}(C^2)$ | decorrelation.tex 132–139 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | BC_C | BC_Q | 공분산을 곱에 적용 | 입력 |
| 1 | BC_Q | BC_CS | 좌표·prefix에서 Cauchy–Schwarz | 입력 |
| 2 | BC_C | BC_DIFF | 조건부 iid 세 사본 | 입력 |
| 3 | BC_DIFF | BC_TRACE | 제곱 전개와 양의 항 | 입력 |
