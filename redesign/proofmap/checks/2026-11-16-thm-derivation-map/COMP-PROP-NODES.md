# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| PR_INC | §8 지도에서 받는 것 | [0,0] | ext | X_INC · Lemma cavity:increment | Cavity increment와 두 insertion | $\Delta_N^{L,\mathbf u}=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o_N(1)$ | cavity.tex 43–69; comparison.tex 8–15 |
| PR_Y | §8 지도에서 받는 것 | [0,0] | ext | X_Y · eq tree:Y-recursion | Power-mean recursion | $Y_L=A,\quad Y_{d-1}=\big(K_dY_d^{m_d}\big)^{1/m_d}$ | trees.tex 55–72 |
| PR_ENC | §8 지도에서 받는 것 | [0,0] | ext | ENC · Lemma comp:encoding | Trial law $\zeta_{L,N}$과 독립 trial label | $\zeta_{L,N}\in\mathcal M_L$: 한 label의 spin process가 reservoir uniform site와 같은 spin 곱 기대값 | comparison.tex 19–25, 58–83 |
| PR_B | §8 지도에서 받는 것 | [0,0] | ext | X_B · §2 model:vs · model:ve · model:functional | $V_{\rm s}$, $V_{\rm e}$, $T_0$와 $\mathcal B_{L-1}$ | $\mathcal B_{L-1}(\zeta,\mathbf m)=\log2+\mathbb E\log T_0V_{\rm s}-\alpha(p-1)\,\mathbb E\log T_0V_{\rm e}$ | model.tex 54–118 |
| PR_BD | §8 지도에서 받는 것 | [1,0] | ext | §5 유계 모형 가정 | $B(\theta)\le B$, $\|h\|\le H$ | $B(\theta)=\max_s\|\theta(s)\|\le B,\quad \|h\|\le H$ (a.s.) | cavity.tex 11–14; model.tex 5 |
| PR_LOG | §8 지도에서 받는 것 | [1,0] | ext | X_LOG · Lemma tree:log-expansion | 로그 전개와 tree law $Q_k$ | $\log Y_0=\sum_{k\ge1}\frac{(-1)^{k-1}}{k}\,\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a$ ($A=1+D$) | trees.tex 205–252 |
| PR_PAT | §8 지도에서 받는 것 | [1,0] | ext | PAT · Lemma comp:patterns | Empirical-pattern comparison | 오차 $\le a\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\|R_S-\mathbb ER_S\|$ | comparison.tex 87–97 |
| PR_SH | §8 지도에서 받는 것 | [1,0] | ext | SH · eq comp:shape-error | 모양 오차의 소멸 (§7 집중의 귀결) | $\lim_{L\to\infty}\limsup_{N\to\infty}\mathbb E_{Q_k}\sum_{S\ne\varnothing}\mathbb E\|R_S-\mathbb ER_S\|=0$ ($k$ 고정) | comparison.tex 123–130, 153–156 |
| PR_TR | PROP · trial 항등식(위)과 로그 비교(아래) | [2,1] | 보통 | 증명 1 · trial insertion | Reservoir spin을 trial spin process로 바꿈 | $A_{\rm s},A_{\rm b}\mapsto\widetilde A_{\rm s},\widetilde A_{\rm b}$, $\quad Y_{0,\cdot}\mapsto\widetilde Y_{0,\cdot}$ | comparison.tex 171–176 |
| PR_SITE | PROP · trial 항등식(위)과 로그 비교(아래) | [0,2] | 보통 | 증명 2a · site 쪽 | $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$ | 마지막 spin transition에서 $\widetilde A_{\rm s}$를 trial spin으로 평균 $=V_{\rm s}$ | comparison.tex 178–180 |
| PR_BOND | PROP · trial 항등식(위)과 로그 비교(아래) | [0,2] | 보통 | 증명 2b · bond 쪽 | $\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\,\mathbb E\log T_0V_{\rm e}$ | $\widetilde Y_{0,\rm b}=\prod_{j\le K_{\rm b}}T_0V_{\rm e}^{(j)}$ | comparison.tex 180–189 |
| PR_TID | PROP · trial 항등식(위)과 로그 비교(아래) | [0,3] | key | 증명 2 · trial 항등식 | Trial 쪽은 정확히 $\mathcal B_{L-1}$ | $\log2+\mathbb E\log\widetilde Y_{0,\rm s}-\mathbb E\log\widetilde Y_{0,\rm b}=\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$ | comparison.tex 189–196 |
| PR_CUT | PROP · trial 항등식(위)과 로그 비교(아래) | [1,2] | 보통 | 증명 3 · count cutoff | $K\le M$에서 $A=z(1+D)$, $\|D\|\le c$ | $C=H+BM,\quad z=\cosh C,\quad c=\tanh C\lt1$ | comparison.tex 198–203 |
| PR_POIS | PROP · trial 항등식(위)과 로그 비교(아래) | [1,3] | 보통 | 증명 5 · Poisson 꼬리 | Cutoff 밖의 기여 | $\le2\,\mathbb E\big[(H+BK)\mathbf 1_{\{K\gt M\}}\big]\xrightarrow{M\to\infty}0$ | comparison.tex 215–217 |
| PR_TERM | PROP · trial 항등식(위)과 로그 비교(아래) | [1,3] | 보통 | 증명 4a · 차수 $k$ 항 | 차수 $k$ 항은 유계 pattern 함수 | $\prod_{a=1}^kD^a$: 많아야 $pM$개 label의 replica-spin pattern과 독립 insertion disorder의 함수, $\|\cdot\|\le1$ | comparison.tex 205–207 |
| PR_PERR | PROP · trial 항등식(위)과 로그 비교(아래) | [1,4] | 보통 | 증명 4b · 고정 tree 오차 | comp:patterns를 $a=pM$으로 | 고정 $\mathcal T$: $\big\|\text{reservoir}-\text{trial}\big\|\le pM\sum_{S\ne\varnothing}\mathbb E\|R_S-\mathbb ER_S\|$ | comparison.tex 207–209 |
| PR_GEO | PROP · trial 항등식(위)과 로그 비교(아래) | [1,4] | 보통 | 증명 4d · 기하 꼬리 | 전개를 $q$항에서 자름 | 양쪽 각각 오차 $\le\sum_{k\gt q}c^k/k$ ($N,L$에 균일) | comparison.tex 211–213 |
| PR_AVG | PROP · trial 항등식(위)과 로그 비교(아래) | [1,5] | 보통 | 증명 4c · tree 평균 | 차수 $k$ 항의 차이가 0으로 | $\lim_{L}\limsup_{N}\ pM\,\mathbb E_{Q_k}\sum_{S\ne\varnothing}\mathbb E\|R_S-\mathbb ER_S\|=0$ ($k,M$ 고정) | comparison.tex 209–211 |
| PR_CONV | PROP · trial 항등식(위)과 로그 비교(아래) | [1,6] | key | 증명 6 · 극한 순서 | 기대 insertion 로그의 수렴 | $\lim_{L}\limsup_{N}\big\|\mathbb E\log Y_{0,\cdot}-\mathbb E\log\widetilde Y_{0,\cdot}\big\|=0$ (site, bond 각각) | comparison.tex 217–221 |
| PR_EQ | PROP · trial 항등식(위)과 로그 비교(아래) | [2,7] | key | Proposition comp:insertion-comparison | Cavity increment = $\mathcal B_{L-1}$ (극한에서) | $\lim_{L\to\infty}\limsup_{N\to\infty}\big\|\Delta_N^{L,\mathbf u_{L,N}}-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\big\|=0$ | comparison.tex 160–167, 196–197, 221–222 |
| PR_U | PROP · trial 항등식(위)과 로그 비교(아래) | [2,8] | 보통 | → COR (comparison.tex 225–246) | 쓰임: 유계 모형의 하한 | $\inf_r\Phi_r\le\underline F+2\varepsilon+\limsup_N\|\Delta_N-\mathcal B_{L-1}\|\ \xrightarrow{L\to\infty}\ \underline F+2\varepsilon$ | comparison.tex 225–246 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | PR_INC | PR_TR | insertion $A_{\rm s},A_{\rm b}$ | 입력 |
| 1 | PR_ENC | PR_TR | 독립 trial spin process | 입력 |
| 2 | PR_Y | PR_TR | trial kernel로 recursion | 입력 |
| 3 | PR_TR | PR_SITE | $\widetilde A_{\rm s}$ | key |
| 4 | PR_B | PR_SITE | $V_{\rm s}$, $U_\theta$ | 입력 |
| 5 | PR_TR | PR_BOND | $\widetilde A_{\rm b}$ | key |
| 6 | PR_ENC | PR_BOND | label 묶음의 독립 | 입력 |
| 7 | PR_B | PR_BOND | $V_{\rm e}=C_\theta$, $T_0$ | 입력 |
| 8 | PR_SITE | PR_TID | $\mathbb E\log T_0V_{\rm s}$ | key |
| 9 | PR_BOND | PR_TID | $\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ | key |
| 10 | PR_B | PR_TID | $\mathcal B_{L-1}$의 정의 | 입력 |
| 11 | PR_TR | PR_CUT | reservoir 쪽과 trial 쪽 | key |
| 12 | PR_BD | PR_CUT | $\|\log A\|\le H+BK$ | 입력 |
| 13 | PR_Y | PR_CUT | homogeneity: $\log z$ 상쇄 | 입력 |
| 14 | PR_BD | PR_POIS | $H+BK$ | 입력 |
| 15 | PR_CUT | PR_POIS | $K\gt M$ 쪽 | 입력 |
| 16 | PR_CUT | PR_TERM | $A=z(1+D)$ | key |
| 17 | PR_LOG | PR_TERM | 차수 $k$ 항 | 입력 |
| 18 | PR_TERM | PR_PERR | $\le pM$ label, $\|\cdot\|\le1$ | key |
| 19 | PR_PAT | PR_PERR | $a=pM$ | 입력 |
| 20 | PR_CUT | PR_GEO | $\|D\|\le c\lt1$ | 입력 |
| 21 | PR_LOG | PR_GEO | 나머지 bound | 입력 |
| 22 | PR_PERR | PR_AVG | $Q_k$ 평균 | key |
| 23 | PR_SH | PR_AVG | comp:shape-error | 입력 |
| 24 | PR_AVG | PR_CONV | 유한 개 항 → 0 | key |
| 25 | PR_GEO | PR_CONV | $q$ 선택 | 입력 |
| 26 | PR_POIS | PR_CONV | $M$ 선택 | 입력 |
| 27 | PR_TID | PR_EQ | trial 쪽 $=\mathcal B_{L-1}$ | key |
| 28 | PR_CONV | PR_EQ | reservoir $\approx$ trial | key |
| 29 | PR_INC | PR_EQ | cavity:identity | 입력 |
| 30 | PR_EQ | PR_U | $L\to\infty$ | key |
