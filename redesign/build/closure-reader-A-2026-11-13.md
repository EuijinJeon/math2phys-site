# 닫힘 시험 — 재구성자 A

읽은 파일: rules.md, glossary.md(525행 전부), L0.md, L1.md. 그 밖의 파일은 열지 않았다.
관례: "블랙박스"는 규칙 문장이 결론을 그대로 진술하고, 나는 그것을 받아들여 다음 단계로 간다는 뜻이다.

## 0. 먼저 확인한 것

규칙·용어집만으로 직접 검산이 되어서 신뢰도가 오른 곳:

- **tree 확률의 정규화.** `g:tree-law`의 선택 확률은 $(n_\beta m_{d_\beta+1}-m_{d_\beta})/n=-\gamma_\beta/n$ 이다. 현재 tree에서 비루트 vertex마다 $m_{d_v}$ 가 자식 항으로 한 번 나오고 내부 vertex마다 $-m_{d_\beta}$ 가 한 번 나오므로, 남는 것은 잎의 $m_L=1$ 뿐이다. 합은 $n$ 이고 확률이 정규화된다. $\gamma_\beta<0$ 은 $m_{d}<m_{d+1}$ 에서 나온다. 단일 path($n=1$)에서는 $Q_2$ 의 split 깊이가 확률 $m_{d+1}-m_d=1/L$ 로 균등하다. $L=1$ 에서는 log 전개가 $\log(1+t\langle D\rangle)$ 의 Taylor 급수로 환원된다.
- **P4의 개수.** reservoir 평균 $\rho_N=\alpha(N+1)(N/(N+1))^p$ 에서 $(N+1)$계는 새 spin에 닿는 factor $\approx$ Poisson$(\alpha p)$, $N$계는 $\alpha N-\rho_N\to\alpha(p-1)$ 개의 bond를 더 가진다. 그래서 site 삽입 $\alpha p$, bond 삽입 $\alpha(p-1)$ 이 맞다.
- **$\mathcal B_r$ 의 지수 정렬.** $T_d$ 의 지수 $m_{d+1}$ 은 tilt 재귀 $Y_{d}=(K_{d+1}Y_{d+1}^{m_{d+1}})^{1/m_{d+1}}$ 와 같은 꼴이다($T_r V=V$ 는 $Y_{L-1}$, 곧 $m_L=1$ 의 leaf Gibbs 평균). $r=L-1$, $\mathbf m=\mathbf m^{(L)}$ 이면 $(m_1,\ldots,m_r)$ 와 일치한다.
- **P2의 부호 구조.** $P^p-pPB^{p-1}+(p-1)B^p\ge0$ 는 $x^p$ 의 볼록성(짝수 $p$ 이면 $P,B$ 의 부호와 무관)이다. 여기에 $\mathbb E[(-b)^n]\ge0$ 과 앞의 $-\lambda^n/n$ 을 곱하면 나머지항이 $\le0$ 이다. 그러면 $\varphi'(t)+\alpha(p-1)\mathbb E\log T_0V_{\rm e}\le0$ 에서 $\varphi(1)\le\varphi(0)-\alpha(p-1)\mathbb E\log T_0V_{\rm e}=\mathcal B_r$ 이다. 이 부호 논리는 규칙 문장만으로 검산된다. interpolation 경로 자체와 $\varphi'$ 의 전개는 검산되지 않는다.
- **P3의 부등식.** 섭동 factor는 $\psi\in[1/2,3/2]$ 이므로 $\lvert\log\psi\rvert\le\log2$ 이고 평균 개수는 $N^{3/4}$ 이다. 섭동이 없으면 power-mean 재귀는 항등이라 root logarithm이 $\log Z_N$ 이다. 재귀가 단조이고 상수 이동에 대해 등변이면 $\lvert P_N-NF_N\rvert\le(\log2)N^{3/4}$ 이 나온다. 이 "단조 + 상수 이동 등변"은 규칙·용어집에 명시되어 있지 않다(아래 P12 항목과 같은 구멍).
- **P12의 상수.** $\alpha D+d$ 는 개수 평균 $\alpha N$ 으로 바로 나온다. $\alpha(2p-1)D+d=\alpha pD+\alpha(p-1)D+d$ 는 site 항 $\alpha p$ 와 edge 항 $\alpha(p-1)$ 의 합으로 맞다. 조립의 $2\alpha pD_K+2d_K$ 는 $(\alpha D+d)+(\alpha(2p-1)D+d)$ 이다. 이 산수는 맞다.

## 1. 수별 표

### 수 1 — 상한 (P1, P2)

| 항목 | 내용 |
|---|---|
| (a) 쓴 규칙 | P2 첫 문장 "모든 $N$ 에서 $F_N\le\mathcal B_r(\zeta,\mathbf m)$"과, 나머지항 $n$차 계수 $-\frac{\lambda^n}{n}\mathbb E[(-b)^n]\mathbb E_{Q_n}\mathbb E[P^p-pPB^{p-1}+(p-1)B^p]$. P1의 짝수 $p$, $\mathbb E[(-b)^n]\ge0$. 용어집 `g:interpolation`의 $\varphi(1)=F_N$, $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$, $\varphi'+\alpha(p-1)\mathbb E\log T_0V_{\rm e}\le0$. |
| (b) 밖의 가정 | $\varphi'(t)$ 가 위 $Q_n$ 급수가 된다는 계산(interpolation의 정의와 Gaussian이 아닌 Poisson 적분 부분, $\lambda\uparrow1$ 정규화)은 규칙에 진술만 있고 유도는 없다. $b$, $f$ 의 본질적 유계성은 "엄격한 곱 한계와 독립성에서 나온다"고만 적혀 있다. 유혹: Guerra interpolation을 "표준이니 당연"으로 받아들이고 싶다. 그 부분은 블랙박스다. |
| (c) 막힌 곳 | $r=0$ 규약: $T_r V=V$ 에서 $r=0$ 이면 $T_0=\mathrm{id}$ 이고 $\zeta$ 는 $x$ 의 분포 하나이므로 $\mathcal B_0=\log2+\mathbb E\log V_{\rm s}-\alpha(p-1)\mathbb E\log V_{\rm e}$ 가 평가된다. 단 $U_\theta$ 의 식이 용어집에 말로만 있다("$p-1$ 개 spin이 $q_{x_\ell}$ 를 따를 때 새 spin $\varepsilon$ 에 주는 log-weight"). 자연스러운 읽기 $U_\theta=\log\sum_{s}e^{\theta(s,\varepsilon)}\prod_\ell q_{x_\ell}(s_\ell)$ 는 내가 채웠다. 새 spin을 $\theta$ 의 마지막 좌표에 놓는다는 약속은 용어집에 있다. 양화사: 모든 $N$, 모든 $r$, 모든 $(\zeta,\mathbf m)$. |
| (d) 판정 | **블랙박스로 받으면 닫힘.** 결론이 P2에 그대로 진술되어 있다. 극한 가정은 필요 없고 $\limsup F_N\le\inf_r\Phi_r$ 가 바로 나온다. 규칙 문장이 내놓는 것은 부호 구조까지다. |

### 수 2 — cavity reservoir와 증분 (P3, P4)

| 항목 | 내용 |
|---|---|
| (a) 쓴 규칙 | P3: $\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)N^{3/4}$ ($L,\mathbf u,N$ 균일). P4: $\Delta_N=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o(1)$, $o(1)$ 은 $L,\mathbf u$ 균일, 증분은 $N,L,\mathbf u$ 균일 유계. 용어집 `g:reservoir`($\rho_N$), `g:site-bond-insertion`, `g:root-logarithm`. |
| (b) 밖의 가정 | (1) $A_{\rm s}$, $A_{\rm b}$ 의 명시적 식(`cavity.tex` (5.6), (5.7))이 없다. 새 spin의 factor가 이웃 $p-1$ 개 site를 어떻게 잡는지가 말로만 있다. (2) $\log Y_0$ 가 reservoir의 tilted kernel로 계산된다는 것: 용어집이 $Y_{d-1}=(K_dY_d^{m_d})^{1/m_d}$ 를 주지만 reservoir의 $K_d$ 구성은 "섭동 mark를 tilt한 것"이라는 말뿐이다. (3) $(N+1)$계의 섭동 개수가 $s_{N+1}\ne s_N$ 이라는 불일치는 $o(1)$ 에 묻힌다. 개수 차이 $\sim N^{-1/4}$ 에 섭동 하나당 $\log2$ 를 곱하는 논증은 내가 채웠다. 유혹: "$\lim F_N=\lim\Delta_N$"은 쓰지 않았다(규칙 표가 금지). |
| (c) 막힌 곳 | P3, P4의 $o(1)$ 이 $L,\mathbf u$ 에 균일하다는 말은 있지만 $\varepsilon$ 과의 관계는 없다. 이후 사용에 지장은 없다. |
| (d) 판정 | **블랙박스로 받으면 닫힘.** P3은 power mean의 단조성 + 상수 등변성이 명시되면 독립 검산이 되고, P4는 개수만 검산된다. |

### 수 3 — 선택된 수열 (P5)

| 항목 | 내용 |
|---|---|
| (a) 쓴 규칙 | P5 (i) $\Delta_{N_j}(\mathbf u_j)\le\underline F+2\varepsilon$, (ii) 모든 고정 type $\nu$ 에서 $e_{\nu,N_j}(\mathbf u_j)\to0$, (iii) 깊이 $L$ 유한 prescribed tree 위 multioverlap 유한곱 기대값의 수렴. 용어집 `g:selected-sequence`, `g:score`, `g:lower-pressure`. |
| (b) 밖의 가정 | 세 조건을 동시에 만족하는 점의 선택(매개변수 평균의 집중 → Markov → 대각 부분수열)은 "못 옮긴 것"이다. (i) 자체가 어떻게 나오는지는 P3과 P4의 균일 유계로 설명된다. 내가 채운 논증: 모든 큰 $N$ 에서 $\Delta_N>\underline F+2\varepsilon$ 이면 $P_N/N$ 의 liminf가 $\underline F+2\varepsilon$ 이상이 되어 모순이다. 하지만 (i)–(iii)를 동시에 만족하려면 좋은 $N$ 들의 양의 밀도가 필요하고, 이 부분은 규칙에 없다. 유혹: "generic한 계를 고른다"는 물리 그림은 쓰지 않았다. |
| (c) 막힌 곳 | 수열이 $(L,\varepsilon)$ 마다 다르다. P8, P9, P11의 문장은 $\varepsilon$ 을 언급하지 않는다("L마다 고른 수열"). 올바른 읽기는 "고정한 $\varepsilon$ 과 각 $L$ 에서 (ii), (iii)을 만족하는 임의의 수열"이다. 표기 충돌: $j$ 가 type 지수이자 수열 지수다. |
| (d) 판정 | **블랙박스로 받으면 닫힘.** (i)이 상한뿐이라는 것, 극한 존재를 요구하지 않는 것은 규칙 문장대로다. |

### 수 4 — branching pattern별 항등식 (P6, P7)

| 항목 | 내용 |
|---|---|
| (a) 쓴 규칙 | P6: 삽입 효과 $\log Y_0$ 의 tilted kernel 전개, 계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$, 법칙 $Q_k$. P7: $\sum_Ec_E\mathbb E[fR_E]-\mathbb Ef\sum_Ec_E\mathbb E[R_E]\to0$. 용어집 `g:extension-history`(c_E의 정의: old leaf 1, fresh path $\gamma_\beta$), `g:protected-leaf`(미분 규칙), `g:insertion`($W_{\mathcal T}(A)=\prod_aA^a\prod_\beta Y_\beta^{\gamma_\beta}$), `g:mark`(selector), `g:palm-identity`, `g:score`. |
| (b) 밖의 가정 | (1) **canceled-anchor 전개의 진술**: P6 문장에는 $\log$ 전개와 $Q_k$ 만 있고 extension history 전개 자체는 없다. 노드 `tree:extension-expansion` 이 P6의 노드 칸에만 이름으로 있다. $c_E$ 의 정의는 용어집에 있지만, "삽입 $A=1+tD$ 의 anchor 인자를 상쇄한 tree 기대값의 $t^k$ 계수가 $\sum_Ec_E\mathbb E_{\mathcal T_E}[G\prod D^{a_i}]$ 이다"라는 문장(및 $1/k!$ 등의 조합 인자)은 어느 규칙에도 없다. 미분 규칙은 `g:protected-leaf` 에 말로 있으나 $Y_\beta^{\gamma_\beta}$ 를 미분하면 fresh path가 붙는다는 것(`tree:first-variation`, `tree:telescoping`)은 "못 옮긴 것"이다. (2) Palm 항등식: Poisson add-one $\mathbb E[nG(n)]=\lambda\mathbb EG(n+1)$ 은 표준이지만 reservoir 법칙의 tilt와 결합하는 부분이 규칙에 없다. (3) Taylor 계수 소거: $u_\nu\in[j^{-j},2j^{-j}]$ 가 $t=1/j$ 의 모든 거듭제곱보다 작다는 것에서 극한 계수가 0이 된다는 논법. 계수의 $u$ 에 대한 Lipschitz 균일성, $t$ 의 수렴 반경, 계수 극한의 존재(P5(iii))가 모두 필요하지만 규칙에는 결론만 있다. (4) polarization과 selector로 한 제약 $\mathcal C$ 를 고르는 부분(용어집 `g:mark` 에 selector 정의는 있다. polarization은 없다). 유혹: 이 항등식을 Ghirlanda–Guerra 항등식의 변형으로 읽고 싶다. 규칙 표가 같은 꼴이 아니라고 하므로 쓰지 않았다. 확인 용도로만 말하면 $k=1$, 스핀 anchor, 깊이 $d$ 제약에서 식은 $\sum_{a\text{ old},\,\mathrm{split}(a_*,a)=d}\mathbb E[fR_{a_*a}]-\delta\,\mathbb E[fR_{a_*,\mathrm{new},d}]\approx-\delta\,\mathbb Ef\,\mathbb ER_{a_*,\mathrm{new},d}$ 가 되어 구조는 자연스럽다. |
| (c) 막힌 곳 | 양화사: $j$ 를 고정하고 $N\to\infty$ 한 뒤 $j\to\infty$. 오차는 $L$, tree, 제약에 균일하지 않다(P7이 말한다). $c_E$ 의 정확한 합 범위 $\mathfrak E(\mathcal T,a_*,\mathcal C)$ 에서 old leaf를 몇 개까지 구별하는지는 `g:reference-path` 의 한 문장("같은 조상 관계의 unused old path는 구별하지 않는다")뿐이다. $c_E$ 의 old leaf 합이 old tree와 무관한 닫힌 꼴이 된다는 `tree:reference-total` 의 주장은 내가 확인하지 못했다(old leaf 개수가 tree에 의존해 보인다). |
| (d) 판정 | (i) 수준(P7 블랙박스): **블랙박스로 받으면 닫힘**(P7이 항등식을 그대로 진술). (ii) 수준(P5, P6 → P7): **구멍**. 구멍의 위치는 위 (b)의 (1)–(4)다. |

### 수 5 — 모든 multioverlap의 집중 (P6, P8, P9)

| 항목 | 내용 |
|---|---|
| (a) 쓴 규칙 | P8(진술: 잎 하나면 점별 $\limsup_Nv_N(S,d)\le1/(\eta L)$, $\lvert S\rvert\ge2$ 이면 $\lim_L\limsup_N\mathcal A_{L,\eta}v_N=0$), P9(진술: $\lim_L\limsup_N\mathcal A_{L,\eta}\mathrm{Var}(R_S)=0$, singleton은 고정 $L$ 에서 $\mathrm{Var}\to0$). 용어집 `g:three-copy`, `g:projection`, `g:depth-continuity` 의 부등식 진술들, `g:depth-delay` 의 기호. |
| (b) 밖의 가정 | P7에서 P8로 가는 길이 규칙에 없다. 어떤 $f$ 와 어떤 제약 $\mathcal C$ 를 P7에 넣는지, 항등식의 좌변에서 $J\,\mathbb E[\cdot]$ 를 어떻게 분리하는지, 잎 수 귀납의 단계, 세 사본 부등식과 사영 오차를 어떻게 이어 붙이는지가 전부 "못 옮긴 것" 목록이다. 용어집은 도구의 진술(세 사본, 사영, martingale energy)을 주지만 조립은 주지 않는다. 깊이 미루기의 $-\delta$ 대 $2+\delta$ 와 $J=\kappa(S^+)^2$, $(1/\lvert J\rvert)\sum_E\lvert c_E\rvert\le C_{k,\eta}$ 는 용어집(`g:tree-coefficient`, `g:depth-delay`)에 기호로만 있고 합 범위와 상수의 의존성이 없다. 유혹: P8을 "물리적 pure state 안의 clustering"으로, P9를 "ultrametricity와 Ghirlanda–Guerra"로 설명하고 싶다. 쓰지 않았다. |
| (c) 막힌 곳 | L1 수 5의 "남은 조건부 평균을 각 고정 깊이에서 집중"은 용어집으로 보면 $\mathrm{Var}(M)\to0$ 하나(각 고정 $L,S,e$)에만 해당하고 최종 P9는 깊이 평균이다. 문장이 오독되기 쉽다. $\eta$-regular의 "서로 다른 branching vertex의 정규화 깊이가 $\eta$ 보다 더 떨어짐"이 모든 쌍인지 조상 관계의 쌍만인지 정의가 모호하다. 추가 prefix 깊이 $d$ 와 aligned 사본의 조건은 "같은 조건을 지킨다" 수준이다. singleton에서 P8(깊이 평균 불필요)과 `g:conditional-decorrelation`("$d$ 하나에 대해 평균")이 표현이 다르다. |
| (d) 판정 | (i) 수준: P8, P9 블랙박스이므로 수 5 자체는 시험 대상이 아니다. (ii) 수준(P6, P7 → P8, P9): **구멍.** 아래 2절 참조. |

### 수 6 — 독립 cavity message로 바꾸기 (P4, P5, P6, P9, P10, P11)

| 항목 | 내용 |
|---|---|
| (a) 쓴 규칙 | P10(부호화: $\zeta_{L,N}\in\mathcal M_L$, 한 label이 모든 tree에서 $\mathbb ER_S$ 를 가짐), P11($\lim_L\limsup_N\lvert\Delta_N-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\rvert=0$ 과 "독립 사본으로 계산한 삽입 $=\mathcal B_{L-1}$"), P5(i). 용어집 `g:spin-pattern`($\lVert\pi^{\otimes a}-\bar\pi^{\otimes a}\rVert_{\rm TV}\le\frac a2\sum_{S\ne\varnothing}\lvert R_S-\mathbb ER_S\rvert$), `g:independent-copies`, `g:tree-law`. |
| (b) 밖의 가정 | **연쇄 부등식은 규칙만으로 검산된다**: $\inf_r\Phi_r\le\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$ 은 $\zeta_{L,N}\in\mathcal M_L=\mathcal M_{r+1}$ 이고 $\mathbf m^{(L)}$ 이 $0<m_1<\cdots<m_r<1$ 이므로 inf의 정의다. $\le\Delta_N+\lvert\Delta_N-\mathcal B_{L-1}\rvert$ 는 삼각부등식. $\Delta_{N_j}\le\underline F+2\varepsilon$ 은 P5(i). 그다음 $\limsup_j$, $L\to\infty$, $\varepsilon\downarrow0$ 순서. 극한 존재는 쓰지 않는다. **P11을 규칙으로 받으면 닫힌다.** P11을 P9, P10, P6에서 유도하려면 다음이 규칙·용어집 밖이다. (1) 삽입 $A_{\rm s}$, $A_{\rm b}$ 의 식과 $A=z(1+D)$, $z=\cosh(H+BM)$, $\lVert D\rVert<1$ 정규화. P6의 log 전개는 $\lvert t\rvert\lVert D\rVert_\infty<1$ 에서만 수렴하므로 이것이 없으면 전개를 못 쓴다. (2) Poisson 절단 $K\le M$ 과 전개 차수 절단: $M$ 에 의존하는 $\lVert D\rVert$ 가 $M\to\infty$ 에서 1로 가므로 먼저 $q$ 를 보낸 뒤 $M$ 을 보내야 한다. 이 순서는 `g:order-of-limits` 에 말로 있다. (3) $Q_k$ 평균을 $\mathcal A_{L,\eta}$ 평균으로 누르는 지배 부등식($Q_k$ 의 shape 확률 $\lesssim C_k L^{-b}$)과 예외 shape 확률 $\le C_k(\eta+L^{-1})$ 은 P11 차이 칸에 결론만 있다. (4) 독립 사본 삽입 $=\mathcal B_{L-1}$ 의 exact 부분: 서로 다른 label의 leaf spin이 prefix를 주면 독립이고 $e^{\theta}$ 가 각 spin에 대해 multi-affine이라 $\mathbb E[e^{\theta}]=C_\theta(x_1,\ldots,x_p)$ 가 된다. 이 논증은 내가 채웠다. 또 $Y$ 재귀와 $T_d$ 의 정렬은 위 0절에서 확인했다. bond 삽입이 $K_{\rm b}\sim$ Poisson$(\alpha(p-1))$ 개의 독립 label 곱이라 $T_0$ 가 곱을 인수분해해서 $\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ 가 된다는 것도 내가 채웠다. (5) $\pi$ 를 $\bar\pi$ 로 바꾸는 오차가 $\mathbb E\lvert R_S-\mathbb ER_S\rvert$ 이고 $\mathrm{Var}$ 로 누르는 것은 Cauchy–Schwarz다. 단 $\bar\pi=\mathbb E\pi$ 가 shape별 평균이어야 한다(P10이 "모든 prescribed tree에서"라고 말한다). 유혹: "이웃 cavity field는 국소 tree라서 독립"은 쓰지 않았다. |
| (c) 막힌 곳 | 양화사: 고정 $\varepsilon$ 에서 각 $L$ 의 수열 위 $\limsup_N$, 그다음 $L$, 마지막 $\varepsilon$. P11 안에서는 $\eta$ 고정 → $N$ → $L$ → $\eta\downarrow0$. $\lvert\Delta_N-\mathcal B\rvert$ 는 $\eta$ 에 의존하지 않으므로 이 순서가 정합한다. P11의 문장이 $\varepsilon$ 을 말하지 않는 것은 위 수 3에서 지적했다. |
| (d) 판정 | (i) 수준: **P11을 블랙박스로 받으면 닫힘.** P9에서 P11까지를 규칙으로 내려가면 (b)의 (1)–(3) 때문에 **구멍**(블랙박스를 P11에 두는 설계가 맞다). |

### 수 7 — 일반 상호작용으로 넓히고 맞붙이기 (P1, P2, P12)

| 항목 | 내용 |
|---|---|
| (a) 쓴 규칙 | P1(factorization으로 $a$ 가 $c=\theta(1,\ldots,1)$ 을 빼면 사라지고 $\widehat\theta$ 의 법칙이 순열 불변), P12($\lvert F_N-F_N'\rvert\le\alpha D+d$, $\lvert\mathcal B_r-\mathcal B_r'\rvert\le\alpha(2p-1)D+d$, 상수 이동이 양쪽을 $-\alpha\mathbb Ec$ 만큼 옮김, 조립식 $\liminf\widehat F_N\ge\widehat I-2\alpha pD_K-2d_K$). 수 1의 상한. |
| (b) 밖의 가정 | (1) **power mean의 성질**: P12의 "시행 쪽 상수는 모든 $r$ 과 모든 시행 법칙에 균일"은 $\lvert\log V-\log V'\rvert\le b$ ($b$ 는 disorder 가측이라 모든 $\mathscr F_d$ 에 가측)이면 $\lvert\log T_0V-\log T_0V'\rvert\le b$ 라는 것에 기댄다. 이것은 $T_d$ 의 단조성과 $\mathscr F_d$-가측 양수 인수의 상수 등변성($T_d(cV)=cT_dV$)에서 나온다. 규칙에는 없다. 용어집 `g:power-mean` 에 "곱셈적 상·하한을 보존한다"가 있고 `g:disorder` 에 "한계가 disorder만의 함수라 모든 $\mathscr F_d$ 에 가측"이 있어서 거의 있지만, 단조성과 등변성이 명시되지 않았다. (2) 상수 이동이 $\mathcal B_r$ 을 정확히 $-\alpha\mathbb Ec$ 만큼 옮긴다는 것은 $U_\theta$ 가 $\log$ 합 꼴이라는 (수 1의) 내 읽기가 필요하다. 그러면 site 항은 $-\alpha p\mathbb Ec$, edge 항은 $+\alpha(p-1)\mathbb Ec$ 이라 합이 $-\alpha\mathbb Ec$ 로 맞는다. (3) truncation의 결합: $\theta$ 와 $\theta^{(K)}$ 를 같은 확률공간에 두는 것과 값별 절단이 순열 불변성을 보존하는 것(용어집이 말하지만 이유는 한 줄이다: 값에 대한 점별 사상이라 입력 순열과 가환). (4) $\mathbb Ec$ 의 유한성은 $\lvert c\rvert\le B(\theta)$ 와 P1의 1차 moment에서. $\widehat F_N=F_N-\alpha\mathbb Ec$ 는 $M_N$ 과 $c_k$ 가 독립이라는 것을 쓴다. 규칙에 한 줄로 있다. 유혹: 홀수 $p$ 나 부호 조건으로 하한이 성립하는지는 말하지 않았다. |
| (c) 막힌 곳 | 조립: $\widehat F_N\ge\widehat F_N^{K}-(\alpha D_K+d_K)$, $\liminf\widehat F_N^K\ge\inf_r\widehat\Phi_r^K$ (bounded 하한, 수 2–6), $\widehat\Phi_r^K\ge\widehat\Phi_r-(\alpha(2p-1)D_K+d_K)$ (모든 $r$ 에 균일하므로 inf 통과). 합이 $2\alpha pD_K+2d_K$ 로 P12와 일치한다. 그다음 $K\to\infty$, 상수 이동 되돌림, 수 1의 $\limsup F_N\le\inf_r\Phi_r$ 와 맞붙여 극한의 존재가 나온다. 순서에 모호함은 없다. 규칙 표가 "짝수 $p$ 는 상한에만 쓰인다"고 쓰지 않은 것(확신이 낮은 대응)과 호출자의 주의 문구가 어긋난다. 규칙 문장만 보면 하한 쪽은 bounded·순열 불변만 요구하므로 짝수 $p$ 를 쓰지 않는 것처럼 보이지만, 표는 홀수 $p$ 하한이 성립한다고 주장하지 않는다. 나는 어느 쪽도 추론에 쓰지 않았다. |
| (d) 판정 | **블랙박스로 받으면 닫힘.** (1)이 한 줄 보충되면 P12의 Lipschitz 부분이 독립 검산된다. |

## 2. 두 수준의 판정

### (i) P8, P9 블랙박스 → 상한·하한 조립 (수 1–3, 6–7)

- 수 1, 2, 3, 7은 P2, P3·P4, P5, P12를 규칙 문장 그대로 받으면 닫힌다. 극한 존재를 가정하는 곳은 없다. 하한은 $\underline F$ 의 liminf 꼴이고, 극한의 존재는 상한과 하한이 맞아서 마지막에 나온다.
- 수 6은 P11을 규칙으로 받으면 닫힌다. P9, P10, P6에서 P11을 규칙만으로 유도하는 것은 구멍이다(수 6 (b)의 (1)–(3)). 따라서 "P9만 블랙박스"로는 부족하고 "P9와 P11"이 블랙박스여야 닫힌다는 것이 시험 결과다.
- 그 밖에 이 수준에서 규칙에 한 줄씩 있으면 좋은 것: power mean의 단조·등변(수 2의 P3 검산과 수 7의 P12에서 둘 다 쓰임), $U_\theta$, $A_{\rm s}$, $A_{\rm b}$ 의 명시적 식, 양화사에 $\varepsilon$ 를 넣는 것.
- 확인한 항목:
  - **깊이 평균 정의**: $\mathcal A_{L,\eta}z=L^{-a}\sum_{\mathbf q\ \eta\text{-regular}}z(\mathbf q)$ 이고 합 범위는 $\{0,\ldots,L-1\}$ 의 정수 배정이라 질량이 $\le1$ 이다. 이 정의에서 `decor:average-holder` $\mathcal A(z^\gamma)\le(\mathcal Az)^\gamma$ 는 Hölder로 독립 검산된다. 단 $\eta$-regular의 두 조건(모든 쌍인지 조상 쌍만인지, 추가 prefix 깊이의 취급)은 한 줄 더 필요해서 "거의 닫힘"이다.
  - **P12의 power mean 성질**: 위 수 7 (b)의 (1). 부분적으로만 있다.
  - **$r=0$ 규약**: 닫힌다. $T_0=T_r=\mathrm{id}$, $\zeta$ 는 $x$ 의 분포, $\mathcal B_0=\log2+\mathbb E\log V_{\rm s}-\alpha(p-1)\mathbb E\log V_{\rm e}$ 가 평가된다. 단 $U_\theta$ 식 보충이 필요하다.

### (ii) P6, P7 → P8, P9 (수 4–5)

**판정: 구멍.** 규칙만으로는 P7의 항등식에서 P8, P9의 결론까지 이어지지 않는다. 이 간격은 규칙 표가 "규칙으로 못 옮긴 것"에 이미 명시한 것과 같다. 구체적인 위치는 다음과 같다.

1. **extension history 전개.** P6 문장에는 없다. 노드 이름 `tree:extension-expansion` 이 P6의 노드 칸에 있을 뿐이다. 용어집에는 $c_E$ 의 정의만 있다.
2. **$c_E$.** 정의는 `g:extension-history` 에 있다(old leaf 계수 1, fresh path 계수 $\gamma_\beta$, 곱). $\gamma_\beta$ 는 P6 문장에 있다. $c_E$ 를 포함하는 항등식은 P7에 있다. 그러나 "삽입의 $t^k$ 계수 $=\sum_Ec_E\ldots$"라는 연결 문장이 규칙 표 어디에도 없다.
3. **계수 한계(charging).** 규칙 표 안에 없다. 위치는 "규칙으로 못 옮긴 것"의 `tree:charging`, `tree:relative-charging`, `decor:J-*` 항목(P8의 증명에 숨는다)과 용어집 `g:depth-delay`, `g:tree-coefficient` 의 기호 수준 서술이다. L1 수 5는 근거 노드로 `tree:charging` 을 들면서 규칙 칸에는 P6을 적는데 P6의 노드 칸에는 `tree:charging` 이 없다. 출처가 어긋난다.
4. **한 걸음 총합 $\kappa(S)$.** `tree:reference-total` 이 P6의 노드 칸에 있고 용어집 `g:tree-coefficient`, `g:reference-path` 에 식이 있다. 그러나 old leaf 합이 old tree와 무관하게 닫힌다는 이유는 확인하지 못했다.
5. **P7에서 P8로의 조립.** $f$ 와 $\mathcal C$ 의 선택, $J$ 로 나누기, 잎 수 귀납, 사영·세 사본·martingale energy의 연결. 이것은 P6′ 만으로 채워지지 않는다. P6′ 이 있어도 P8의 증명 윤곽 규칙(또는 P8을 블랙박스로 유지하는 선택)이 필요하다.

따라서 수 4, 5는 P8, P9를 블랙박스로 유지하는 한에서만 규칙 표 위에서 서고, P6′ 을 더하면 구멍 1–4가 메워지고 5만 남는다.

## 3. P6′ 필요 내용 — 문장 초안

**P6′ (extension history 전개와 계수 한계).** P6의 설정(깊이 $L$ 의 유한 prescribed tree $\mathcal T$, $m_d=d/L$, tilted kernel)에서 anchor $a_*$ 가 있는 old tree에 삽입 $A=1+\sum_{i\le k}t_iD_i$ 를 넣는다($D_i$ 는 유계 path 함수).

(a) **미분 규칙.** tree 밀도 $W_{\mathcal T}(A)=\prod_aA^a\prod_\beta Y_\beta^{\gamma_\beta}$ 를 $t_i$ 로 미분하면 두 가지뿐이다. (i) protected가 아닌 leaf $a$ 에서 $A^a\to D_i^a$ 가 되고(계수 $+1$) 그 leaf는 protected가 된다. (ii) 현재 tree의 내부 vertex $\beta$ 에서 fresh path가 붙고(계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$, $n_\beta$ 는 현재 tree의 자식 수) 새 leaf는 protected다. 처음에 anchor는 protected다(그 인자 $A^{a_*}$ 를 상쇄한다).

(b) **전개.** 임의의 유계 $G$ 에 대해 $t_1\cdots t_k$ 의 계수(곧 $t=0$ 의 혼합 미분)는 $\sum_{E\in\mathfrak E_k(\mathcal T,a_*)}c_E\,\mathbb E_{\mathcal T_E}[G\prod_{i\le k}D_i^{a_i(E)}]$ 이다. 합은 color $1,\ldots,k$ 를 차례로 (i) 아직 안 쓴 anchor 아닌 old leaf 또는 (ii) 내부 vertex의 fresh path에 배정하는 모든 history이고, $c_E$ 는 각 단계 계수의 곱이다. 단일 $D$ 에서 $t^k$ 계수의 조합 인자($1/k!$ 등)와 수렴 영역 $\lvert t\rvert\lVert D\rVert_\infty<1$ 의 정확한 꼴은 [확정 필요: 파일로는 알 수 없음]. 모든 leaf를 처음부터 protected로 두면 같은 규칙이 P6의 $\log$ 전개와 $Q_k$ 를 낳는다.

(c) **부호.** old leaf 선택은 $+1$, fresh path는 $\gamma_\beta<0$($n_\beta\ge1$, $m_d<m_{d+1}$)이므로 $c_E$ 는 부호가 섞인다. 또 $\sum_\beta(-\gamma_\beta)=n$ (현재 leaf 수)이다. 이것이 $Q_k$ 의 확률 $-\gamma_\beta/n$ 의 정규화다.

(d) **한 걸음 총합.** 제약 $\mathcal C$ 가 새 color와 reference path(anchor와 이미 color를 받은 path) 사이의 split 깊이만 지정하고 같은 조상 관계의 unused old path를 구별하지 않으면, 한 color의 계수 총합은 reference tree에만 의존한다: 깊이 $d$ 의 vertex가 reference 자식을 $j$ 개 가지면 $m_d-jm_{d+1}$. 모양 $S$ 에 대한 총합은 $\kappa(S)=\prod_{v\in\mathrm{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ 이고 부호는 $(-1)^{\sum_v(a_v-1)}$ 이다. [확정 필요: old leaf의 $+1$ 합이 old tree의 leaf 개수와 무관해지는 이유]

(e) **계수 한계(charging).** target 모양 $S$ 의 내부 branching 깊이를 한 칸씩 미룬 $S^+$ 와 $J=\kappa(S^+)^2$ 에 대해, 각 새 split이 인자 $\delta=1/L$ 하나를 내고 부호 있는 합은 $-\delta$, 절댓값 합은 $2+\delta$ 이다. 모든 $k$ 와 $\eta>0$ 에 대해 $L$, $N$, kernel에 무관한 $C_{k,\eta}$ 가 있어 $\eta$-regular한 모든 target에서 $\lvert J\rvert\ge c_{k,\eta}>0$ 이고 $\frac1{\lvert J\rvert}\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}\lvert c_E\rvert\le C_{k,\eta}$ 이다. [확정 필요: $\lvert J\rvert$ 하한의 꼴, 합 범위에서 old leaf 선택을 어떻게 세는지, $C_{k,\eta}$ 가 old tree의 잎 수에 의존하는지]

참고: P8, P9의 조립(잎 수 귀납, 사영, 세 사본, martingale energy)은 P6′ 에 들어가지 않는다. 그것까지 규칙으로 두려면 별도의 P8 증명 윤곽 규칙이 필요하고, 아니면 현재대로 P8, P9를 블랙박스로 둔다.

## 4. 열린 항목 목록

1. P6 문장에 extension history 전개가 없다(노드 이름만). → P6′ (a), (b).
2. 계수 한계(charging)가 규칙 표 어디에도 없고 L1 수 5는 근거 노드로만 부른다. → P6′ (e). L1 수 5의 "쓰는 규칙: P6" 칸과 P6의 노드 칸이 어긋난다.
3. `tree:reference-total` 의 old tree 무관성의 이유가 확인되지 않는다. → P6′ (d).
4. power mean의 단조성과 $\mathscr F_d$-가측 인수의 상수 등변성이 명시되지 않았다. P3의 독립 검산과 P12의 균일성에 필요하다. 한 줄 추가 권고.
5. $U_\theta$, $A_{\rm s}$, $A_{\rm b}$ 의 명시적 식이 규칙·용어집에 없다($r=0$ 평가, 상수 이동의 $-\alpha\mathbb Ec$, P11의 exact 부분에 필요).
6. P11의 log 전개 사용에는 정규화 $A=z(1+D)$, $\lVert D\rVert<1$ 과 Poisson·차수 절단 순서, $Q_k$ 에 대한 shape 지배 부등식이 필요한데 규칙에는 결론(예외 확률 $\le C_k(\eta+L^{-1})$)만 있다.
7. 양화사: P8, P9, P11의 문장이 $\varepsilon$ 와 수열의 $(L,\varepsilon)$ 의존성을 말하지 않는다. "고정 $\varepsilon$, 각 $L$ 의 선택된 수열"로 명시하는 것을 권한다. 표기 충돌: type 지수 $j$ 와 수열 지수 $j$.
8. L1 수 5의 "각 고정 깊이에서 집중"은 $\mathrm{Var}(M)\to0$ 에만 해당하고 최종 P9는 깊이 평균이다. 문장이 오독되기 쉽다.
9. $\eta$-regular 정의의 모호함: "서로 다른 branching vertex가 $\eta$ 보다 더 떨어짐"이 모든 쌍인지 조상 쌍인지, 추가 prefix 깊이 $d$ 와 aligned 사본의 조건.
10. singleton 서술의 불일치: P8은 "깊이 평균 불필요", `g:conditional-decorrelation` 은 "$d$ 하나에 대해 평균".
11. P7의 Taylor 계수 소거(`pert:analytic`)는 $u$ 에 대한 계수의 균일성, $t$ 의 수렴 반경, 계수 극한의 존재(P5(iii))를 쓴다. 규칙에는 결론뿐이다.
12. 호출자의 주의 문구("짝수 $p$ 와 부호 조건은 상한에서만 쓰인다")와 규칙 표의 "확신이 낮은 대응"("짝수 $p$ 는 상한에만 쓰인다고 쓰지 않았다")이 어긋난다. 규칙 표를 따르면 부호 조건은 하한에 쓰이지 않고, 짝수 $p$ 는 상한의 볼록성에서 직접 쓰이되 홀수 $p$ 하한은 주장되지 않는다.
13. P5의 (i)–(iii) 동시 선택에 필요한 "좋은 $N$ 들의 양의 밀도"는 규칙에 없다(블랙박스).
