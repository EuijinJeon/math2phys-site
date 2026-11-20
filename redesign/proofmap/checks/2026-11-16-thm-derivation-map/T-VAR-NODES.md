# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| TV_SET | 부모 지도에서 받는 것 | [0,0] | ext | T_SET (증명 2) | $M$의 정의 | $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$ | decorrelation.tex 537–552 |
| TV_L2 | 부모 지도에서 받는 것 | [0,0] | ext | T_L2 (증명 4) | $M$ 아래 잔여의 경계 | $\mathbb E(R_S-M)^2\le2p_N(S,e)^2+2\,\mathbb E(G-G_-)^2$ | decorrelation.tex 590–595 |
| TV_ADJ | 부모 지도에서 받는 것 | [0,0] | ext | T_ADJ · eq decor:adjacent-prefix-error | 이웃 prefix 오차 | $\mathcal A_{L,\eta}\,\mathbb E(G-G_-)^2\le C_k/L$ | decorrelation.tex 582–589 |
| TV_FIB | 부모 지도에서 받는 것 | [0,0] | ext | T_FIB (증명 5) | $p_N^2$ 평균의 경계 | $\limsup_N\mathcal A_{L,\eta}\,p_N(S,e)^2\le C\,V_{k-1,L}(\eta/2)^{1/2}$ | decorrelation.tex 605–609 |
| TV_VM | 부모 지도에서 받는 것 | [1,0] | ext | T_VM · eq decor:prefix-projection-concentration | Prefix 사영의 집중 | $\mathrm{Var}(M)\to0\quad(N\to\infty;\ L,S,e\ \text{고정})$ | decorrelation.tex 556–569 |
| TV_ERR | 부모 지도에서 받는 것 | [1,0] | ext | A_ERR · eq decor:identity-error | 항등식 오차의 유한 최대 | $\varepsilon_{N,L,k}\to0\quad(N\to\infty;\ L,k\ \text{고정})$ | decorrelation.tex 48–58 |
| TV_ADEF | 부모 지도에서 받는 것 | [1,0] | ext | A_DEF · eq decor:average-definition | 깊이 평균 $\mathcal A_{L,\eta}$ | $\mathcal A_{L,\eta}z=L^{-a}\sum_{\mathbf q\ \eta\text{-regular}}z(\mathbf q)$ | decorrelation.tex 15–37 |
| TV_DEC | T_VAR · 조립 순서 | [0,1] | 보통 | 증명 6 · 분산 분해 | 1. 분산을 prefix 사영과 잔여로 나눔 | $\mathrm{Var}(R_S)=\mathrm{Var}(M)+\mathbb E(R_S-M)^2$ | decorrelation.tex 596 |
| TV_BND | T_VAR · 조립 순서 | [0,2] | 보통 | 증명 6 | 2. 잔여에 사영 경계를 넣음 | $\mathrm{Var}(R_S)\le\mathrm{Var}(M)+2p_N(S,e)^2+2\,\mathbb E(G-G_-)^2$ | decorrelation.tex 590–597 |
| TV_AVG | T_VAR · 조립 순서 | [0,3] | 보통 | 증명 6 | 3. 깊이 평균과 $\limsup_N$을 항별로 | $\limsup_N\mathcal A\,\mathrm{Var}(R_S)\le\limsup_N\mathcal A\,\mathrm{Var}(M)+2\limsup_N\mathcal A\,p_N^2+2\sup_N\mathcal A\,\mathbb E(G-G_-)^2$ | decorrelation.tex 596–603 |
| TV_T1 | T_VAR · 조립 순서 | [1,3] | 보통 | 증명 6 | 첫 항: 고정 $L$에서 0 | $\limsup_N\mathcal A_{L,\eta}\mathrm{Var}(M)=0$ | decorrelation.tex 562–569, 596–597 |
| TV_SUM | T_VAR · 조립 순서 | [2,4] | 보통 | eq decor:variance-estimate | 4. 세 경계를 모음 | $\limsup_N\mathcal A_{L,\eta}\mathrm{Var}(R_S)\le C_k\big(L^{-1}+V_{k-1,L}(\eta/2)^{1/2}\big)$ | decorrelation.tex 597–611 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | TV_SET | TV_DEC | $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$ | 입력 |
| 1 | TV_DEC | TV_BND | 둘째 항 $\mathbb E(R_S-M)^2$ | key |
| 2 | TV_L2 | TV_BND | $\le2p_N^2+2\mathbb E(G-G_-)^2$ | key |
| 3 | TV_BND | TV_AVG | 점별 부등식 | key |
| 4 | TV_ADEF | TV_AVG | 양의 선형 | 입력 |
| 5 | TV_VM | TV_T1 | 배정마다 $\to0$ | key |
| 6 | TV_ERR | TV_T1 | 유한 모음 | 입력 |
| 7 | TV_ADEF | TV_T1 | 고정 $L$: 유한 합 | 입력 |
| 8 | TV_AVG | TV_SUM | 세 항 | key |
| 9 | TV_T1 | TV_SUM | 첫 항 $=0$ | key |
| 10 | TV_FIB | TV_SUM | 둘째 항 $\le CV^{1/2}$ | key |
| 11 | TV_ADJ | TV_SUM | 셋째 항 $\le C_k/L$ | key |
