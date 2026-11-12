# 용어집 — The Mézard–Parisi formula for diluted spin glasses

L0, L1, 규칙 표, 카드에 나오는 용어와 기호가 원문에서 정확히 무엇이고 증명에서 무슨 일을 하는지 적는다. 예전 사이트의 역할 표를 대신하며, 원문(`source/sections/*.tex`)에 맞춰 다시 썼다.

**읽는 법.**
- 항목마다 기호, 뜻(이 사이트에서의 정확한 정의), 역할(증명에서 하는 일과 그것을 받아 쓰는 규칙 P번호·노드), 정의 위치(노드 ID 또는 `파일.tex` 행), 물리 대응(유형: exact / weakening / blackbox / approximation / intuition), 쓰지 않는 뜻(잘못 읽기 쉬운 것)을 둔다. intuition은 증명에 쓰이지 않는 그림이다.
- 다른 문서는 `g:slug` 를 이중 대괄호로 감싸 항목을 가리킨다(예: [[g:state]]). 표시어를 바꿀 때는 slug 뒤에 `|표시어`를 붙인다(예: [[g:state|상태]]). 규칙 표의 칸 안에서는 표의 `|` 와 겹치므로 표시어 없이 쓴다.
- "상태"는 [[g:state]] 하나만 뜻한다: 보조 계층의 깊이 $d$ prefix. 물리적 pure state는 [[g:physical-pure-state]]이고, 논문은 그것을 다루지 않는다.

## 모형

### g:interaction — 상호작용 $\theta$
- **기호**: 무작위 함수 $\theta:\{-1,1\}^p\to\mathbb R$, 독립 사본 $\theta_k$, $B(\theta)=\max_s\lvert\theta(s)\rvert$
- **뜻**: $p$체 factor 하나의 log-weight다. $-H_N(\sigma)=\sum_{k\le M_N}\theta_k(\sigma_{i_{1,k}},\ldots,\sigma_{i_{p,k}})+\sum_ih_i\sigma_i$ 이므로 $\theta$ 가 큰 배치가 선호되고, 역온도는 $\theta$ 안에 흡수되어 있다.
- **역할**: 모형의 입력이다. 상한(P2)은 [[g:factorization]] 꼴을 쓰고, 하한(L1 수 2–6)은 bounded이고 [[g:permutation-invariance|순열 불변]]인 $\theta$ 만 쓴다(`cavity.tex` 11–14). $B(\theta)$ 는 $\lvert\log C_\theta\rvert$, $\lvert U_\theta\rvert$ 의 상계(`model.tex` 65–66)와 P12의 거리 $D$ 에 쓰인다.
- **정의 위치**: `model:hamiltonian`, `model.tex` 3–23
- **물리 대응**: exact — factor(clause)의 Boltzmann weight $e^{\theta(s)}$. 명명 모형에서는 $\theta_\beta=\beta J\prod_\ell s_\ell$ 등이다([[g:named-models]]).

### g:field — 장 $h$
- **기호**: $h$, 독립 사본 $h_i$
- **뜻**: site마다 독립인 무작위 외부장이다. 역온도가 흡수되어 $e^{h_i\sigma_i}$ 로 들어간다.
- **역할**: P1의 moment 조건 $\mathbb E\lvert h\rvert<\infty$, 하한의 유계 가정 $\lvert h\rvert\le H$(`cavity.tex` 11–12), site 항 $V_{\rm s}$ 의 $h\varepsilon$, P12의 거리 $d=\mathbb E\lvert h-h'\rvert$ 에 쓰인다.
- **정의 위치**: `model:integrability`, `model:hamiltonian`, `model.tex` 3–23
- **물리 대응**: exact — 무작위 외부장 $\beta H$.

### g:hypergraph — 밀도 $\alpha$ 와 Poisson hypergraph
- **기호**: $\alpha>0$, $M_N\sim\mathrm{Poisson}(\alpha N)$, 독립 균일 site $i_{\ell,k}\in[N]$
- **뜻**: factor 수 $M_N$ 은 평균 $\alpha N$ 의 Poisson이고 각 factor의 $p$ 개 site는 $[N]$ 에서 독립 균일로 복원추출한다. spin당 평균 factor 수는 $\alpha$, spin 하나의 평균 차수는 $\alpha p$ 다.
- **역할**: site 항의 $k\sim\mathrm{Poisson}(\alpha p)$ 와 edge 항 계수 $\alpha(p-1)$(`model:functional`), reservoir의 평균 개수 $\rho_N$(`cavity:reservoir-mean`), 삽입 개수 $K_{\rm s}$, $K_{\rm b}$(P4)를 정한다.
- **정의 위치**: `model:hamiltonian`, `model.tex` 9–23
- **물리 대응**: exact — Erdős–Rényi형 random factor graph. $K$-SAT에서는 clause density.
- **쓰지 않는 뜻**: 증명은 이 그래프의 국소 tree 구조를 쓰지 않는다(P11 차이). 논문의 문장이 아니라, §5–§8의 어느 단계도 국소 구조를 쓰지 않는다는 데서 읽은 것이다.

### g:pressure — pressure $F_N$
- **기호**: $F_N=\frac1N\mathbb E\log Z_N$, $Z_N=\sum_\sigma e^{-H_N(\sigma)}$
- **뜻**: quenched pressure다. free energy density $f$ 와는 $F_N=-\beta f$ 관계다.
- **역할**: 주정리가 극한을 구하는 양이다. 상한 $F_N\le\mathcal B_r$(P2), 섭동에 대한 안정성(P3), $\underline F$ 의 정의([[g:lower-pressure]]), $L^1$ 안정성(P12)에 쓰인다.
- **정의 위치**: `model:hamiltonian`, `main:theorem`
- **물리 대응**: exact.

### g:hypotheses — 가정
- **기호**: `model:integrability`–`model:positivity`
- **뜻**: 짝수 $p\ge2$, $\mathbb EB(\theta)+\mathbb E\lvert h\rvert<\infty$, [[g:factorization]], [[g:positivity]]. 정확한 목록과 각 가정이 쓰이는 곳은 규칙 P1 행에 있다.
- **역할**: 주정리 전체의 가정이다. 상한은 모두 쓰고, 하한은 bounded·순열 불변 경우(`comp:bounded-lower`)로 줄인 뒤 factorization을 상수 이동의 대칭화에 한 번만 쓴다(`reduction.tex` 45–63).
- **정의 위치**: `model:integrability`, `model:factorization`, `model:positivity`, `main:theorem`
- **물리 대응**: 없음. 물리 유도는 이 조건들을 의식하지 않는다.

### g:factorization — factor weight 전개 ($a$, $b$, $f_\ell$)
- **기호**: $e^{\theta(s)}=a\bigl(1+b\prod_{\ell=1}^pf_\ell(s_\ell)\bigr)$, 모든 spin 조에서 a.s. $\lvert b\prod_\ell f_\ell(s_\ell)\rvert<1$
- **뜻**: $a>0$ 과 $b$ 는 실수 확률변수, $f_\ell:\{-1,1\}\to\mathbb R$ 은 한 무작위 함수의 독립 사본이고, $b$ 는 $f_\ell$ 들과 독립이다. $a$ 는 다른 모든 변수에 의존해도 되고 $\log a$ 의 적분 가능성은 가정하지 않는다.
- **역할**: 상한(P2)에서 나머지항을 $P^p-pPB^{p-1}+(p-1)B^p$ 꼴로 나누고 $b$, $f$ 를 본질적으로 유계로 만든다(`upper.tex` 17–34). 여기서 $n$ 개 replica leaf의 tree $\mathcal T$ 위에서 $P=P_{\mathcal T}=\frac1N\sum_i\mathbb E_f\prod_{a=1}^nf(\sigma_i^a)$ 는 실제 spin 위 $f$ 곱의 site 평균(새 $f$ 하나를 모든 leaf가 공유), $B=B_{\mathcal T}=\mathbb E_{f,x}\prod_{a=1}^n\bar f(x^a)$, $\bar f(x)=\sum_sf(s)q_x(s)$ 는 새 시행 message tree 위의 같은 양이다(`upper.tex` 62–66, 98–112). 하한 쪽에서는 `main:theorem` 증명에서 $c=\theta(1,\ldots,1)$ 을 빼 $a$ 를 없애고 $\widehat\theta$ 의 법칙을 순열 불변으로 만드는 데 한 번만 쓰인다(P1, P12).
- **정의 위치**: `model:factorization`, `model.tex` 25–44
- **물리 대응**: exact(예에서) — Viana–Bray에서 $a=\cosh\beta J$, $b=\tanh\beta J$, $f(s)=s$ 인 tanh 전개다(`models:spin` 증명). 일반 꼴을 high-temperature(loop) 전개로 읽는 것은 intuition이다.
- **쓰지 않는 뜻**: §5–§8의 bounded 하한은 이 전개를 쓰지 않는다(`cavity.tex` 13–14, `decorrelation.tex` 8–9).

### g:positivity — 부호 조건 $\mathbb E[(-b)^n]\ge0$
- **기호**: $\mathbb E[(-b)^n]\ge0$ $(n\ge1)$
- **뜻**: [[g:factorization]]의 $b$ 의 모든 차수 moment에 대한 부호 조건이다(유한 실수 기대값으로 해석).
- **역할**: 상한의 나머지항 전체를 0 이하로 만든다(P2, `upper:remainder`). 하한에는 쓰이지 않는다.
- **정의 위치**: `model:positivity`, `model.tex` 35–44
- **물리 대응**: weakening(예에서) — 대칭 coupling(홀수 moment 0)과 soft SAT($b=e^{-\beta W}-1$, $W\ge0$ 이라 $-1<b\le0$)에서 성립한다(`models:spin`, `models:sat` 증명, `consequences.tex` 30–31, 40, 59–62). intuition — "frustration이 대칭이거나 반강자성 쪽"이라는 읽기는 일반적인 동치 조건이 아니다.

### g:permutation-invariance — 순열 불변성
- **기호**: 없음
- **뜻**: $\theta$ 의 법칙이 $p$ 개 입력 좌표의 순열에 대해 불변이라는 조건이다.
- **역할**: bounded 하한(`cavity.tex` 11–14, `comp:bounded-lower`)의 가정이다. 원래 $\theta$ 는 $a$ 때문에 불변이 아닐 수 있어서 `main:theorem` 증명이 $\widehat\theta=\theta-c$ 로 불변성을 만들고, truncation은 그것을 보존한다(`reduction.tex` 46–63, P12).
- **정의 위치**: `cavity.tex` 11–14, `reduction.tex` 45–63
- **물리 대응**: 없음.

### g:named-models — 명명 모형
- **기호**: Viana–Bray, diluted 짝수 $p$-spin, soft random 짝수 $K$-SAT
- **뜻**: 두 따름정리 모두 모든 $\beta>0$ 에 대한 것이다. `models:spin`은 서로 독립인 실수 확률변수 $J$, $H$ 로 $J$ 의 분포가 대칭이고 $\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert<\infty$, $\theta_\beta=\beta J\prod_\ell s_\ell$, $h_\beta=\beta H$ 이고 $p=2$ 가 Viana–Bray다. `models:sat`은 독립 공정 부호 $\varepsilon_\ell$, 그것과 독립인 $W\ge0$($\mathbb EW<\infty$), $\theta_\beta=-\beta W\prod_\ell(1+\varepsilon_\ell s_\ell)/2$, $h=0$ 이고 $W=1$ 이 soft random 짝수 $K$-SAT다.
- **역할**: 주정리의 가정을 확인하는 예다(각 증명이 $a,b,f_\ell$ 를 준다). [[g:ground-state]] 따름정리의 대상이다.
- **정의 위치**: `models:spin`, `models:sat`(`consequences.tex` 10–49)
- **물리 대응**: exact.

### g:ground-state — 최댓값 밀도 $g$ (영온도)
- **기호**: $\mathcal E_N$, $g=\lim_N\frac1N\mathbb E\max_\sigma\mathcal E_N(\sigma)$
- **뜻**: $\beta$ 를 뗀 에너지 점수 $\mathcal E_N$($Z_N(\beta)=\sum_\sigma e^{\beta\mathcal E_N(\sigma)}$)의 최댓값 밀도로, ground-state 에너지 밀도의 부호를 바꾼 것이다. 단위 가중치 SAT에서 $-g$ 는 변수당 위반 clause 최소 개수 기대값의 극한이다.
- **역할**: `models:ground`가 극한의 존재와 $\frac1\beta\inf_r\inf_{\zeta,\mathbf m}\mathcal B_{r,\beta}\in[g,g+\log2/\beta]$ 를 준다.
- **정의 위치**: `models:ground`, `consequences.tex` 66–101
- **물리 대응**: exact.
- **쓰지 않는 뜻**: 영온도 order parameter나 inf의 달성을 말하지 않는다. inf는 각 $\beta$ 에서 따로 취한다.

### g:lower-pressure — $\underline F$ 와 여유 $\varepsilon$
- **기호**: $\underline F=\liminf_NF_N$, $\varepsilon>0$
- **뜻**: bounded 모형에서 모든 크기 $N$ 에 대해 취한 pressure의 liminf다(선택 전의 것). $\varepsilon$ 은 [[g:selected-sequence]]를 고를 때의 여유다.
- **역할**: P5(i) $\Delta_{N_j}\le\underline F+2\varepsilon$ 의 기준이다. 하한은 $\inf_r\Phi_r\le\underline F+2\varepsilon+\limsup_N\lvert\Delta_N-\mathcal B_{L-1}\rvert$ 로 닫힌다(`comp:bounded-lower`).
- **정의 위치**: `perturbations.tex` 249–253, `comp:low-increments`
- **물리 대응**: 없음. 물리 유도는 $\lim F_N=\lim\Delta_N$ 을 쓰지만 논문은 liminf만 쓴다.

### g:disorder — 물리적 disorder
- **기호**: $M_N$, $\theta_k$, $h_i$, $i_{\ell,k}$; 시행 functional에서는 $k$, $\theta,\theta_1,\ldots$, $h$
- **뜻**: 모형과 시행 functional에서 보조 message가 아닌 무작위 변수 전부다: factor 개수, factor의 site index, factor별 상호작용, site별 장. 시행 사슬($\eta^\omega_d$, $x^\omega$)은 이것과 독립이다(`model.tex` 79–80). power mean $T_d$ 의 조건부 기대값은 이것을 고정한 채 보조 message만 적분하고(`model.tex` 97, 109–110), 바깥의 $\mathbb E$ 는 disorder와 $\eta_0$ 을 평균한다($T_0V$ 는 $\mathscr F_0$-가측이고 $\mathscr F_0$ 은 disorder와 $\eta_0^\omega$ 가 생성한다, `model.tex` 90–91).
- **역할**: $F_N=\frac1N\mathbb E\log Z_N$ 의 quenched 평균(`model:hamiltonian`), $\mathscr F_d$ 의 생성원(`model:power-means`), `model:trial-bounds`의 한계가 disorder만의 함수라 모든 $\mathscr F_d$ 에 가측이라는 점에 쓰인다. reservoir에서는 [[g:root]]가 물리 disorder에 섭동 factor의 개수·type·site를 더한 것이고, 섭동 매개변수는 root의 무작위 변수가 아니라 선택된 고정값이다(`cavity.tex` 29–31).
- **정의 위치**: `model:hamiltonian`, `model:vs`, `model.tex` 9–23, 79–82, 90–91, 109–110
- **물리 대응**: exact — quenched disorder. 평균 $\mathbb E\log Z$ 가 quenched 평균이다.
- **쓰지 않는 뜻**: 시행 message $x$ 와 사슬 $\eta_d$ 는 disorder가 아니다(물리의 annealed 평균과 혼동하지 않는다).

## 변분 공식

### g:message — cavity field (message) $x$
- **기호**: $x\in\mathbb R$, $q_x(s)=e^{xs}/(2\cosh x)$, message label $\omega$
- **뜻**: spin 하나 위의 확률분포 $q_x$ 를 정하는 실수다. 시행 법칙에서는 [[g:order-parameter]] 사슬의 마지막 변수이고, 서로 다른 label의 message는 독립이다.
- **역할**: site 항과 edge 항의 입력이다(`model:site-message`, `model:edge`). encoding(P10)에서는 reservoir의 무작위 site $i$ 에 대해 깊이 $r$ prefix가 주어졌을 때 $x=\operatorname{arctanh}\langle\sigma_i\rangle$ 로 만든다(`comparison.tex` 32–42).
- **정의 위치**: `model.tex` 48–54, `model:chain`, `comp:encoding`
- **물리 대응**: exact — cavity field(역온도 단위): 이웃 하나를 떼어낸 spin의 유효 국소장, $\langle s\rangle_{q_x}=\tanh x$.
- **쓰지 않는 뜻**: 시행 functional의 $x$ 는 실제 계에서 계산한 것이 아니라 임의의 시행 법칙에서 뽑은 것이고 moment 조건도 없다(`model:trial-bounds`).

### g:site-term — site 항 $V_{\rm s}$ 와 $U_\theta$
- **기호**: $U_\theta(x_1,\ldots,x_{p-1};\varepsilon)$, $V_{\rm s}=\frac12\sum_{\varepsilon=\pm1}\exp\bigl(h\varepsilon+\sum_{j\le k}U_{\theta_j}(x^j_1,\ldots,x^j_{p-1};\varepsilon)\bigr)$, $k\sim\mathrm{Poisson}(\alpha p)$
- **뜻**: $U_\theta$ 는 나머지 $p-1$ 개 spin이 $q_{x_\ell}$ 를 따를 때 factor 하나가 새 spin $\varepsilon$ 에 주는 log-weight다. 새 spin은 $\theta$ 의 $p$ 번째(마지막) 좌표에 놓인다($e^{\theta(s_1,\ldots,s_{p-1},\varepsilon)}$, `model.tex` 59–63). 원래 $\theta$ 의 법칙은 순열 불변이 아닐 수 있으므로(`reduction.tex` 46–47) 상한에 쓰는 $\mathcal B_r$ 의 정의는 이 좌표 선택에 달려 있다(`upper.tex` 37–39, 62–66). $V_{\rm s}$ 는 새 spin 하나를 장과 Poisson$(\alpha p)$ 개 factor와 함께 넣는 site 분배함수다.
- **역할**: $\mathcal B_r$ 의 $\mathbb E\log T_0V_{\rm s}$ 항이다. 상한 interpolation의 끝점 $\varphi(0)$(`upper.tex` 47–48)이고, 비교에서 독립 사본으로 계산한 site 삽입이 정확히 $T_0V_{\rm s}$ 다(P11, `comparison.tex` 178–180).
- **정의 위치**: `model:site-message`, `model:vs`
- **물리 대응**: exact — $U_\theta$ 는 factor→spin cavity bias($u$-message), $V_{\rm s}$ 는 Bethe free entropy의 site 항.

### g:edge-term — edge 항 $V_{\rm e}$ 와 $C_\theta$
- **기호**: $C_\theta(x_1,\ldots,x_p)=\sum_se^{\theta(s)}\prod_\ell q_{x_\ell}(s_\ell)$, $V_{\rm e}=C_\theta(x_1,\ldots,x_p)$
- **뜻**: $p$ 개 spin이 서로 다른 label의 message 분포를 따를 때 factor 하나를 붙이는 분배함수다.
- **역할**: $\mathcal B_r$ 의 $-\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ 항으로, site 삽입에서 중복해 센 factor를 보정한다(`model.tex` 50–52). 비교에서 bond 삽입이 $\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ 가 된다(P11, `comparison.tex` 181–192).
- **정의 위치**: `model:edge`, `model:ve`
- **물리 대응**: exact — Bethe free entropy의 factor(edge) 항.

### g:order-parameter — order parameter $\zeta$ 와 $\mathcal M_{r+1}$
- **기호**: $\mathcal M_1=\mathcal P(\mathbb R)$, $\mathcal M_{j+1}=\mathcal P(\mathcal M_j)$, $\zeta\in\mathcal M_{r+1}$; 사슬 $\eta_0^\omega\sim\zeta$, $\eta_{d+1}^\omega\mid\eta_d^\omega\sim\eta_d^\omega$, $x^\omega\mid\eta_{r-1}^\omega\sim\eta_{r-1}^\omega$
- **뜻**: message label $\omega$ 마다 독립으로 무작위 측도의 사슬을 뽑아 마지막에 [[g:message]] $x$ 를 얻는 $r$단 시행 법칙이다. $r=0$ 이면 $\zeta$ 는 $x$ 의 분포 하나다. 사슬은 물리적 disorder와 독립이다.
- **역할**: $\mathcal B_r(\zeta,\mathbf m)$ 의 인자이고 inf의 범위다(P2). 하한에서는 reservoir에서 만든 [[g:encoded-law]] $\zeta_{L,N}\in\mathcal M_L$ 이 이 자리에 들어간다(P10).
- **정의 위치**: `model:chain`, `model.tex` 68–81
- **물리 대응**: exact — $r$단 RSB order parameter. $r=0$ 은 RS의 cavity field 분포, $r=1$ 은 1RSB의 "분포의 분포"(population of populations).
- **쓰지 않는 뜻**: 사슬의 깊이 $d$ 를 물리적 pure state 계층의 단계와 동일시하지 않는다([[g:physical-pure-state]]).

### g:parisi-parameters — Parisi parameter $\mathbf m$
- **기호**: $\mathbf m=(m_1,\ldots,m_r)$, $0<m_1<\cdots<m_r<1$; tree 계산에서는 $m_0=0$, $m_L=1$
- **뜻**: [[g:power-mean]]의 지수열이다.
- **역할**: 상한에서는 임의다(inf의 범위, P2). 하한에서는 최적화하지 않고 [[g:grid]] $m_d=d/L$ 로 고정한다(P10, P11). tree 계수 $\gamma_\beta$ 와 $Q_k$ 의 확률을 정한다(P6).
- **정의 위치**: `model.tex` 70–71, `trees.tex` 16–19
- **물리 대응**: intuition — Parisi의 $m$(overlap 분포 누적함수 $x(q)$ 의 계단 위치). $Q_2$ 에서 두 path가 깊이 $d$ 에서 갈라질 확률이 $m_{d+1}-m_d$ 라는 사실(`trees.tex` 220–222)이 이 읽기와 맞지만, 동일시 자체는 증명되거나 쓰이지 않는다.

### g:power-mean — power mean $T_d$
- **기호**: $T_rV=V$, $T_dV=\bigl(\mathbb E[(T_{d+1}V)^{m_{d+1}}\mid\mathscr F_d]\bigr)^{1/m_{d+1}}$ $(d=r-1,\ldots,0)$
- **뜻**: 시행 사슬의 깊이 $d+1$ 변수만 적분하는 조건부 거듭제곱 평균을 깊이 $r-1$ 부터 0까지 반복한 것이다. 물리적 disorder는 내내 고정된다. tree 계산의 recursion $Y_{d-1}=(K_dY_d^{m_d})^{1/m_d}$ 도 같은 꼴이다.
- **역할**: $\mathcal B_r$ 의 $T_0V_{\rm s}$, $T_0V_{\rm e}$ 를 만든다. 곱셈적 상·하한을 보존해서 $\mathcal B_r$ 이 시행 message에 대한 moment 조건 없이 유한하다(`model:trial-bounds`, `model.tex` 122–128; 상계 $\lvert h\rvert+\sum_jB(\theta_j)$ 의 유한성에는 물리 disorder의 1차 moment `model:integrability`가 여전히 쓰인다). reservoir에서는 같은 recursion이 [[g:root-logarithm]]을 정의한다(P3, P4).
- **정의 위치**: `model:power-means`, `model.tex` 90–110, `tree:Y-recursion`
- **물리 대응**: intuition — 물리에서는 물리적 pure state 계층 위의 Ruelle cascade 평균을 적분해 낸 꼴로 읽는다. 논문은 Panchenko–Talagrand가 cascade 가중치를 쓴다고만 적고, 필요한 항등식을 임의의 유한 kernel 열에 대해 직접 세운다(`trees.tex` 7–12). 이 동일시는 증명에 쓰이지 않는다.

### g:functional — 시행 functional $\mathcal B_r$
- **기호**: $\mathcal B_r(\zeta,\mathbf m)=\log2+\mathbb E\log T_0V_{\rm s}-\alpha(p-1)\mathbb E\log T_0V_{\rm e}$
- **뜻**: $r$단 시행 법칙 $(\zeta,\mathbf m)$ 에서 계산한 계층 cavity functional(Panchenko–Talagrand functional의 power-mean 꼴)이다.
- **역할**: 상한 $F_N\le\mathcal B_r$(P2), 하한의 $\Delta_N\approx\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$(P11), $L^1$ 안정성(P12)의 대상이다.
- **정의 위치**: `model:functional`
- **물리 대응**: exact — $r$단 RSB Mézard–Parisi(Bethe) free entropy를 시행 order parameter에서 계산한 값. 물리는 정류점에서 평가하지만 여기서는 모든 시행값이 상한이다([[g:phi]]).

### g:phi — 변분값 $\Phi_r$ 와 $\inf_r\Phi_r$
- **기호**: $\Phi_r=\inf_{\zeta,\mathbf m}\mathcal B_r(\zeta,\mathbf m)$, $\inf_{r\ge0}\Phi_r$
- **뜻**: 고정한 단계 수 $r$ 에서의 inf와, 모든 유한 $r$ 에 대한 inf다.
- **역할**: 주정리의 우변 $\lim F_N=\inf_{r\ge0}\Phi_r$ 이다. 상한(P2)과 하한(`comp:bounded-lower`)이 이 값에서 만난다.
- **정의 위치**: `model:functional`, `main:formula`
- **물리 대응**: approximation — 물리의 "saddle point 선택"에 해당한다. 수학은 inf이고, inf의 달성이나 무한 깊이 극한은 주장하지 않는다(`model.tex` 138–140).

### g:rsb-steps — RSB 단계 수 $r$ 와 계층 깊이 $L=r+1$
- **기호**: $r$, $L=r+1$
- **뜻**: $r$ 은 시행 법칙의 보조 단계 수(RSB 단계 수)다. tree 계산의 깊이는 $L=r+1$ 이고, 깊이 $1,\ldots,r$ 에 보조 변수, 깊이 $L$ 에 spin 배치가 놓인다.
- **역할**: 하한은 깊이 $L$ 의 reservoir에서 $\mathcal B_{L-1}$ 을 얻는다. $L\to\infty$ 가 하한의 마지막 극한이다(P9, P11, [[g:order-of-limits]]).
- **정의 위치**: $r$ 은 `model:chain`(`model.tex` 70–81, "Fix $r\ge1$"), $r=0$ 은 `model.tex` 118–120; $L=r+1$ 은 `trees.tex` 24–27, `cavity.tex` 16–19
- **물리 대응**: exact(시행 법칙에서) — $r$단 사슬이 $r$단 RSB 시행 order parameter이고 tree 계산에서 $L=r+1$ 이다(`model.tex` 70–81, `trees.tex` 24–27). intuition(reservoir에서) — 하한의 깊이 $L$ 계층은 섭동 mark로 만든 보조 계층이므로(`cavity.tex` 20–24), 그것을 계의 물리적 $(L-1)$단 RSB 구조로 읽는 것은 증명되지 않는다([[g:depth]], `introduction.tex` 75–77).

### g:interpolation — interpolation (상한)
- **기호**: $\varphi(t)$, $t\in[0,1]$
- **뜻**: 평균 $t\alpha N$ 개의 실제 factor와, site마다 평균 $(1-t)\alpha p$ 개의 cavity factor $U_\theta(x_1,\ldots,x_{p-1};\sigma_i)$ 사이를 잇는 경로다. $\varphi(t)$ 는 power-mean recursion 뒤의 root logarithm의 기대값을 $N$ 으로 나눈 것이다(`upper.tex` 41–43).
- **역할**: P2. $\varphi(1)=F_N$, $\varphi(0)=\log2+\mathbb E\log T_0V_{\rm s}$, $\varphi'(t)+\alpha(p-1)\mathbb E\log T_0V_{\rm e}\le0$ 에서 모든 $N$ 의 $F_N\le\mathcal B_r$ 이 나온다. [[g:hypotheses]]를 모두 쓴다.
- **정의 위치**: `upper:bound`, `upper:derivative`, `upper.tex` 36–60
- **물리 대응**: exact — Guerra의 interpolation을 Franz–Leone, Panchenko–Talagrand가 희석계와 유한 단계로 옮긴 것(`upper.tex` 3–7).

## 보조 계층

### g:hierarchy — 보조 계층 (path kernel, tilted kernel)
- **기호**: $K_d(dz\mid\mathscr F_{d-1})$ $(1\le d\le L)$; 분배함수에서 만들 때 $1\le d<L$ 에서는 prior kernel $P_d$ 의 tilt $K_d=e^{m_d(X_d-X_{d-1})}P_d$, $K_L$ 은 prefix가 주어진 Gibbs kernel(`trees.tex` 51–65)
- **뜻**: 깊이 $0,\ldots,L$ 의 path를 뽑는 확률 kernel 열이다. 깊이 0은 [[g:root]], 깊이 $1,\ldots,L-1$ 은 보조 변수, 깊이 $L$ 은 spin 배치다. 분배함수에서 만들 때는 prior $P_d$ 를 $e^{m_dX_d}$ 로 기울인 tilted kernel을 쓰고, 마지막 $K_L$ 은 prefix가 주어진 Gibbs 분포다.
- **역할**: reservoir에서는 섭동 factor의 [[g:mark]] 변수가 보조 변수이고(`cavity.tex` 23–24, `perturbations.tex` 61–62), 그 tilted kernel이 [[g:state]], [[g:replica]], [[g:prescribed-tree]]를 정한다. 시행 사슬 $\eta_d$ 도 이 틀의 한 예다(`trees.tex` 26–27). P6–P10이 모두 이 위에서 진술된다.
- **정의 위치**: `trees.tex` 14–27, `tree:original-tilt`(`trees.tex` 51–65)
- **물리 대응**: intuition — tilt $\propto e^{m_dX_d}$ 는 Monasson식 $Z^m$ 재가중과 같은 꼴이다. 그러나 가중되는 것은 보조 변수의 값이지 물리적 pure state가 아니다.
- **쓰지 않는 뜻**: 계층의 branching은 구성의 일부이고 유도된 것이 아니며, 원문은 "no ultrametric organization of the physical Gibbs states is assumed"라고 쓴다(`introduction.tex` 75–77). 그래서 이 계층을 물리적 Gibbs 측도의 [[g:physical-pure-state|물리적 pure state]] 분해로 읽지 않는다(이 마지막 문장은 원문의 문장이 아니라 위 인용에서 읽은 것이다).

### g:depth — 깊이 $d$
- **기호**: $d\in\{0,\ldots,L\}$, 정규화 깊이 $d/L$
- **뜻**: 보조 계층 path의 정수 좌표다. 0은 [[g:root]], $L$ 은 spin leaf다. 두 path의 split 깊이는 마지막 공통 vertex의 깊이다([[g:replica]]).
- **역할**: split 깊이, branching 깊이, prefix 깊이가 모두 이 좌표다. 하한에서 $m_d=d/L$ 이므로 정규화 깊이가 [[g:eta-regular]]와 [[g:depth-average]]에 쓰인다.
- **정의 위치**: `trees.tex` 20–23
- **물리 대응**: intuition — Parisi 변수 $x=m_d=d/L$ 의 격자점으로 읽을 수 있다. overlap 값 $q$ 가 아니다.
- **쓰지 않는 뜻**: 물리적 pure state 계층의 단계가 아니다.

### g:root — root 와 기대값 표기 ($\mathbb E$, $E_{\mathcal T}$, $\langle\cdot\rangle$, $\mathbb E_{\mathbf u}$)
- **기호**: 깊이 0 변수; $\mathbb E$, $E_{\mathcal T}$, $\langle\cdot\rangle$, $\mathbb E_{\mathbf u}$
- **뜻**: root는 보조 계층 path의 깊이 0 변수이고("Its depth-zero variable is the root", `trees.tex` 20), tree의 모든 path가 공유한다. 그 분포는 insertion을 해도 바뀌지 않는다(`trees.tex` 23). reservoir에서는 [[g:disorder|물리 disorder]]("the reservoir root disorder", `comparison.tex` 20–21, 28–29)와 섭동의 개수·type·site가 root 변수다(`cavity.tex` 29, `perturbations.tex` 60–61). 섭동 매개변수 $\mathbf u$ 는 root 변수가 아니라 고정된 결정적 값이고(`cavity.tex` 29–31), mark 변수는 root가 아니라 지정된 보조 깊이에서 뽑힌다(`perturbations.tex` 61–62). 기대값 표기는 다음과 같다. $E_{\mathcal T}$ 는 root가 주어졌을 때 tree $\mathcal T$ 의 표본추출에 대한 기대값(`trees.tex` 33–34), 첨자 없는 $\mathbb E$ 는 root와 지정된 tree의 표본추출을 모두 포함한 기대값이다(`trees.tex` 48–49). §6의 $\langle\cdot\rangle$ 은 root가 주어졌을 때 tilted path 하나를 따른 기대값, $\mathbb E_{\mathbf u}$ 는 고정된 $\mathbf u$ 에서 root에 대한 평균이다(`perturbations.tex` 83–85). 매개변수를 지정한 진술의 기대값은 그 값을 고정한 채 취한다(`perturbations.tex` 9–10). §8의 encoding은 독립 균일 site $i$ 도 root에 넣고(`comparison.tex` 28–29), 거기서 $x=\operatorname{arctanh}\langle\sigma_i\rangle$ 의 괄호는 보조 prefix가 주어진 leaf Gibbs 기대값이다(`comparison.tex` 34–36).
- **역할**: 집중 진술의 뜻이 이 약속에 달려 있다. $\operatorname{Var}(R_S)$ 와 $v_N(S,d)$ 의 바깥 기대값은 root를 포함하고(`decorrelation.tex` 103, [[g:overlap-concentration]], [[g:conditional-covariance]]), score 오차 $e_{\nu,N}$ 은 $\mathbb E_{\mathbf u}\langle\cdot\rangle$ 로 정의된다([[g:score]]). [[g:state]]의 $\mathscr F_d$ 는 root를 포함하고, 깊이 0의 상태는 root 자신이다. P5, P7–P11의 기대값이 모두 이 표기를 따른다.
- **정의 위치**: `trees.tex` 20–23, 33–34, 48–49; `cavity.tex` 28–31; `perturbations.tex` 9–10, 60–62, 83–85
- **물리 대응**: approximation — root의 물리 disorder 부분은 quenched disorder이고 첨자 없는 $\mathbb E$ 는 물리의 disorder 평균과 thermal(tree 표본) 평균을 함께 취한 것에 해당한다. 다만 root에는 섭동의 개수·type·site도 들어 있고, $\langle\cdot\rangle$ 은 $L\ge2$ 에서 보조 변수를 tilt해서 적분한 path 기대값이라 보통의 Gibbs 평균이 아니다(보조 계층이 없는 $L=1$ 이면 Gibbs 평균이다, `trees.tex` 63–65).
- **쓰지 않는 뜻**: 물리 disorder만을 뜻하지 않는다. 섭동 매개변수 $\mathbf u$ 를 포함하지 않으며, 분산·기대값은 $\mathbf u$ 에 대해 평균하지 않는다(매개변수 평균은 $\pi$ 로 명시할 때만, [[g:perturbation]]).

### g:state — 상태
- **기호**: 깊이 $d$ prefix; $\sigma$-field $\mathscr F_d$ 로 조건을 건 것
- **뜻**: 보조 계층 path의 [[g:root]](disorder, 섭동 개수·type·site; 섭동 매개변수는 선택된 값으로 고정)부터 깊이 $d$ $(0\le d<L)$ 까지의 prefix다. "상태 안"은 $\mathscr F_d$ 가 주어진 조건부 법칙, "상태 평균"은 $\mathbb E[\,\cdot\mid\mathscr F_d]$ 를 뜻한다. 같은 상태를 공유하는 replica들은 깊이 $d$ 까지 같은 vertex를 지난다(더 깊은 vertex도 공유할 수 있다). 조건부 독립은 갈라짐에 대한 것이다: 깊이 $d$ vertex의 서로 다른 자식 아래에 든 replica 묶음들(곧 정확히 깊이 $d$ 에서 갈라지는 묶음들)이 $\mathscr F_d$ 가 주어지면 조건부 독립이다(`trees.tex` 32–35).
- **역할**: [[g:conditional-covariance]] $v_N(S,d)$ 와 [[g:clustering]]의 조건(P8), [[g:projection]]의 상태 평균 $\mu_{e,T_j}$, 집중 증명의 "상태 안 / 상태 사이" 분해 $\operatorname{Var}(R_S)=\mathbb E(R_S-M)^2+\operatorname{Var}(M)$, $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$(P9, `decor:overlap-concentration`)에 쓰인다.
- **정의 위치**: `trees.tex` 20–23($\mathscr F_d$ 는 prefix $\sigma$-field), `decorrelation.tex` 94–96; 시행 사슬의 $\mathscr F_d$ 는 `model.tex` 90–91
- **물리 대응**: intuition — 물리에서 깊이 $d$ 의 물리적 pure state 묶음이 하는 일을 이 prefix가 한다. 그 동일시는 증명되지 않으며 증명에 쓰이지 않는다.
- **쓰지 않는 뜻**: 물리적 pure state가 아니다([[g:physical-pure-state]]). 섭동된 계 전체의 Gibbs 측도, [[g:selected-sequence]], 극한 Gibbs 측도를 "상태"라고 부르지 않는다. 일반 $\sigma$-field $\mathscr G$ 로 조건을 건 것도 상태라고 부르지 않는다.

### g:physical-pure-state — 물리적 pure state
- **기호**: 원문에 없음(물리 문헌의 $\langle\cdot\rangle_\alpha$, 가중치 $w_\alpha$)
- **뜻**: 물리에서 열역학 극한의 Gibbs 측도를 분해한 극단적 성분이다(물리에서는 그 안에서 connected correlation이 사라진다고 본다). Parisi 그림에서는 성분마다 가중치가 있고 성분 사이 overlap이 계층 구조를 이룬다고 본다.
- **역할**: 논문은 이것을 가정하지도 증명하지도 않는다. 서론은 보조 계층의 branching이 구성의 일부이고 물리적 Gibbs 측도를 물리적 pure state 계층으로 조직하는 것은 가정하지 않는다고 쓰고(`introduction.tex` 75–77), 극한 무한 깊이 Gibbs 측도가 만들어져 있다고 가정하지 않는다고 쓴다(`model.tex` 138–140). 어떤 노드도 이것을 받아 쓰지 않으며, 물리 유도에서 이것이 하던 일은 [[g:state]](보조 계층 prefix)가 한다.
- **정의 위치**: 원문에 정의 없음. 다루지 않는다는 진술은 `introduction.tex` 75–77, `model.tex` 138–140
- **물리 대응**: intuition — Parisi 그림의 물리적 pure state와 그 ultrametric 조직이다(원문 표현은 "no ultrametric organization of the physical Gibbs states is assumed", `introduction.tex` 77). 물리 유도의 수 4–6("물리적 pure state 안에서 이웃 cavity field는 독립")이 기대는 대상이며, 이 사이트는 L1 끝 문단과 규칙 차이 칸에서 대조용으로만 쓴다.
- **쓰지 않는 뜻**: [[g:state]]가 아니다.

### g:replica — replica
- **기호**: leaf $a$, spin 배치 $\sigma^a\in\{-1,1\}^N$
- **뜻**: [[g:prescribed-tree]]의 깊이 $L$ leaf에 놓인 spin 배치다. 두 replica의 split 깊이는 두 path의 마지막 공통 vertex의 깊이다("A split at depth $d$ means that the last common vertex is at depth $d$", `trees.tex` 34–35). 두 replica는 split 깊이까지 공통 prefix를 갖고 그 아래로는 조건부 독립이다. leaf 위치가 달라도 값은 같을 수 있다(`trees.tex` 35–37).
- **역할**: [[g:multioverlap]] $R_S$ 의 변수(P7–P9)이고 [[g:spin-pattern]]의 좌표다(P11).
- **정의 위치**: `trees.tex` 29–47
- **물리 대응**: approximation — "같은 Gibbs 계의 표본"(`introduction.tex` 65–66). $L=1$ 이면 정확히 독립 Gibbs 표본이고, $L\ge2$ 에서는 보조 계층을 따라 뽑아 prefix를 공유한다.
- **쓰지 않는 뜻**: replica trick의 $n\to0$ 해석적 연속이 아니다(P6 차이).

### g:prescribed-tree — prescribed tree 와 tree 표본 규칙
- **기호**: $\mathcal T$, $E_{\mathcal T}$
- **뜻**: 공통 [[g:root]]와 깊이 $L$ 에서 끝나는 유한 개의 labeled path로 된 tree다. 각 vertex에서 서로 다른 자식은 그 prefix가 주어지면 kernel로 독립으로 뽑히고, 일부 leaf를 지워도 나머지 tree의 표본 법칙은 바뀌지 않는다(사영 일관성). 이 두 성질이 tree 표본 규칙이다. $E_{\mathcal T}$ 는 root가 주어졌을 때 이 표본추출에 대한 기대값이다(`trees.tex` 33–34).
- **역할**: P5(iii)의 모멘트, P6의 전개, P7 항등식이 이 위에서 진술된다. §7은 [[g:tree-identity]]와 이 표본 규칙만 쓴다(`decorrelation.tex` 8–9).
- **정의 위치**: `trees.tex` 29–39, 200–202; `x:decor-tree-sampling`
- **물리 대응**: intuition — replica 사이 overlap 행렬의 계층(Parisi 행렬) 그림.

### g:topology — topology, branching pattern, 깊이 배정
- **기호**: $S$, $\operatorname{Br}(S)$, $b(S)$, $\mathbf q=(q_v)$, initial stem, 자식 모양 $T_j$
- **뜻**: topology는 labeled leaf를 갖는 유한 rooted tree에서 unary vertex(자식이 하나인 vertex)를 지운 것이다. initial stem은 root에서 첫 branching vertex까지의 경로이고(`decorrelation.tex` 94), 자식 모양 $T_j$ 는 첫 branching vertex 아래의 부분 topology다(`decorrelation.tex` 208). 깊이 배정은 각 branching vertex에 $\{0,\ldots,L-1\}$ 의 정수를 주며 가지를 따라 엄격히 증가한다. branching pattern은 (topology, 깊이 배정)의 짝, 곧 replica들이 어느 깊이에서 갈라지는지다.
- **역할**: P7의 제약 $\mathcal C$, P8–P9의 대상 $S$, $\mathcal A_{L,\eta}$ 의 좌표다.
- **정의 위치**: `decorrelation.tex` 18–21, `x:decor-topology`; 원문이 (topology, branching 깊이 좌표)의 짝에 붙이는 말은 "shape"다(`trees.tex` 460–462)
- **물리 대응**: intuition — replica들의 overlap tree. 갈라짐 깊이는 보조 계층의 정수 깊이이지 overlap 값이 아니다.

### g:eta-regular — $\eta$-regular
- **기호**: $\eta>0$
- **뜻**: 깊이 배정의 모든 깊이를 $L$ 로 나눈 값이 $(\eta,1-\eta)$ 안에 있고 서로 다른 branching vertex의 정규화 깊이가 $\eta$ 보다 더 떨어진 것이다. 추가 prefix 깊이 $d$ 가 있으면 모든 branching 깊이에 대해 같은 조건을 지키고, aligned 두 사본은 공통 좌표에 조건을 건다.
- **역할**: [[g:depth-average]]의 합 범위다(P8, P9). 두 조건은 하는 일이 다르다. (a) 아래 경계 $m_d=d/L>\eta$ 가 $\lvert m_d-jm_{d+1}\rvert=(j-1)m_d+j\delta\ge\eta$ $(j\ge2)$ 를 주어 정규화 계수의 하한을 지킨다(`trees.tex` 410, 449–455; 이 하한은 $m_{d_v}\ge\eta$ 하나에서 나온다). 같은 아래 경계가 기저의 $c_d=(d+2)\delta\ge\eta$ 를 준다(`decorrelation.tex` 288). (b) 깊이 사이의 간격 조건은, 한 칸 미룬 깊이가 old tree의 어떤 branching 깊이와도 겹치지 않게 해서 fresh unary split을 강제하고(`decorrelation.tex` 345–347), 깊이를 옮긴 중간 모양들이 같은 조상 관계를 지키며 $\eta/2$-regular 범위에 머물게 한다(`decorrelation.tex` 44–47, 201–203). 예외 tree의 확률 $\le C_k(\eta+L^{-1})$(`tree:irregular-probability`)이 이 평균을 P11로 넘긴다.
- **정의 위치**: `decorrelation.tex` 21–28, `x:decor-eta-regular`; tree 하나의 regular는 `trees.tex` 460–467
- **물리 대응**: 없음.

### g:grid — 균등 격자 $m_d=d/L$, $\delta$, $\mathbf m^{(L)}$
- **기호**: $m_d=d/L$ $(0\le d\le L)$, $\delta=1/L$, $\mathbf m^{(L)}=(1/L,\ldots,(L-1)/L)$
- **뜻**: 하한 내내 쓰는 Parisi parameter의 고정 선택이다.
- **역할**: §5–§8의 계수 계산($\gamma_\beta$, $\kappa$, $c_\ell$, $J$)과 $Q_2$ split 깊이의 균등성(`trees.tex` 220–222)을 준다. 깊이를 한 칸 미룰 때 새 split마다 계수 $\delta$ 가 나온다([[g:depth-delay]]). 비교의 결과가 $\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$ 이다(P10, P11).
- **정의 위치**: `cavity:grid`, `x:decor-mesh`
- **물리 대응**: intuition — Parisi 변수 $x$ 축의 간격 $1/L$ 격자. 최적화된 Parisi parameter가 아니다.

## Reservoir와 증분

### g:reservoir — reservoir
- **기호**: 물리 상호작용 개수의 평균 $\rho_N=\alpha(N+1)(N/(N+1))^p$
- **뜻**: 크기 $N$ 과 $N+1$ 의 계를 비교하는 공통 $N$-spin 계다. 평균 $\rho_N$ 개의 상호작용, 보통의 장, 그리고 type $\nu$ 마다 평균 $c_\nu s_N$ 개(합계 Poisson$(s_N)$)의 [[g:perturbation|섭동]] factor를 가진다(`cavity.tex` 20–28, 45–50).
- **역할**: $\Delta_N$ 을 reservoir에 site·bond를 넣는 차로 쓰는 자리다(P4). score 집중(P5), 항등식(P7), 집중(P8, P9), encoding(P10)이 모두 이 계에 대해 진술된다.
- **정의 위치**: `cavity:increment`, `cavity:reservoir-mean`, `cavity.tex` 3–9
- **물리 대응**: exact — Aizenman–Sims–Starr cavity 비교의 공통계(`cavity.tex` 4–6).
- **쓰지 않는 뜻**: 원래의 $N$-spin 계가 아니다(평균 상호작용 수가 $\alpha N$ 이 아니다).

### g:perturbation — 섭동 (Poisson 섭동 factor)
- **기호**: type $\nu$, $\psi_\nu=1+t_\nu g\sigma_i+u_\nu g_0S_0$, $t_\nu=1/j$, $u_\nu\in I_\nu=[j^{-j},2j^{-j}]$, $n_\nu\sim\mathrm{Poisson}(c_\nu s_N)$, $s_N=N^{3/4}$, $\mathbf u=(u_\nu)$, $\pi$
- **뜻**: type마다 독립인 Poisson 개수의 단일 site factor $\psi_\nu\in(1/2,3/2)$ 를 spin weight에 곱한다. 각 항은 독립 균일 site 하나와 자기 [[g:mark]] 과정의 독립 사본을 쓴다. $\mathbf u$ 는 고정된 결정적 매개변수이고, $\pi$ 는 그것을 고를 때만 쓰는 균일 측도다.
- **역할**: 밀도에 $o(1)$ 만 기여한다(P3). $u$ 미분이 [[g:score]]가 되어 집중하고(P5), 같은 factor의 $t$ 전개가 Taylor 계수 항등식을 낸다(P7, [[g:palm-identity]]).
- **정의 위치**: `cavity.tex` 20–32, `pert:parameters`, `pert:factor`, `perturbations.tex` 26–71
- **물리 대응**: intuition — 물리의 무한소 섭동장(generic한 Gibbs 측도를 고르는 것). 여기서는 개수 $N^{3/4}$, 값 $(1/2,3/2)$ 의 구체적인 factor다.

### g:root-logarithm — root logarithm $X_0$ 와 그 기대값 $P_N^{L,\mathbf u}$
- **기호**: $X_0$, $P_N^{L,\mathbf u}=\mathbb EX_0$
- **뜻**: root logarithm $X_0$ 는 섭동된 leaf 분배함수 $Z$ 에서 $X_{L-1}=\log Z$, $X_{d-1}=m_d^{-1}\log P_de^{m_dX_d}$ 로 power-mean recursion을 거슬러 올라가 얻은 깊이 0의 값이다(`trees.tex` 51–56). 그것은 [[g:root]]에 대해 무작위다("the random root log partition function", `perturbations.tex` 121). $P_N^{L,\mathbf u}$ 는 그 기대값이다("its expected root logarithm", `cavity.tex` 34–35; "root-averaged perturbed log partition function", `perturbations.tex` 251).
- **역할**: $\lvert P_N^{L,\mathbf u}-NF_N\rvert\le(\log2)N^{3/4}$(P3)와 증분 $\Delta_N$ 의 정의(P4)에 쓰인다.
- **정의 위치**: `cavity.tex` 34–41, `cavity:negligible`, `trees.tex` 51–56
- **물리 대응**: approximation — 섭동된 계의 계층 free entropy. 하한은 $L\ge2$ 만 쓰고(`cavity.tex` 16), 이때 보통 뜻의 pressure가 아니다. 보조 계층이 없으면($L=1$, `trees.tex` 65) recursion이 없고 섭동된 계의 $\mathbb E\log Z$ 가 된다.

### g:increment — cavity 증분 $\Delta_N$
- **기호**: $\Delta_N^{L,\mathbf u}=P_{N+1}^{L,\mathbf u}-P_N^{L,\mathbf u}$
- **뜻**: 섭동된 계의 $N\to N+1$ root logarithm 증분이다. $N,L,\mathbf u$ 에 대해 균일하게 유계다.
- **역할**: P4의 $\Delta_N=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o(1)$, P5(i)의 $\Delta_{N_j}\le\underline F+2\varepsilon$, P11의 $\Delta_N\approx\mathcal B_{L-1}$ 에 쓰인다.
- **정의 위치**: `cavity:increment`, `cavity:identity`
- **물리 대응**: approximation — Aizenman–Sims–Starr 증분. 물리는 $\lim F_N=\lim\Delta_N$ 을 쓰지만 논문은 극한의 존재를 가정하지 않고 [[g:selected-sequence]] 위의 상한만 쓴다.

### g:site-bond-insertion — site 삽입과 bond 삽입 ($Y_{0,\rm s}$, $Y_{0,\rm b}$)
- **기호**: $A_{\rm s}$, $A_{\rm b}$, $K_{\rm s}\sim\mathrm{Poisson}(\alpha p)$, $K_{\rm b}\sim\mathrm{Poisson}(\alpha(p-1))$, $\log Y_{0,\rm s}$, $\log Y_{0,\rm b}$
- **뜻**: reservoir에 새 spin 하나를 장과 $K_{\rm s}$ 개 factor와 함께 넣는 terminal [[g:insertion]] $A_{\rm s}$, factor $K_{\rm b}$ 개를 넣는 $A_{\rm b}$, 그리고 tilted reservoir kernel로 계산한 그 $\log Y_0$ 값이다.
- **역할**: P4의 증분 식을 이룬다. P11에서 site label을 독립 사본으로 바꾸면 $\widetilde Y_{0,\rm s}=T_0V_{\rm s}$, $\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ 가 된다.
- **정의 위치**: `cavity:site-insertion`, `cavity:bond-insertion`, `cavity:identity`
- **물리 대응**: exact — cavity method의 site 추가와 bond 추가에 따른 (계층) free entropy 변화.

### g:score — perturbation score 와 score 오차
- **기호**: $D_\nu=\sum_{q\le n_\nu}g_{0,q}S_{0,q}/(1+t_\nu g_q\sigma_{i_q}+u_\nu g_{0,q}S_{0,q})$, $e_{\nu,N}(\mathbf u)$
- **뜻**: $D_\nu$ 는 type $\nu$ 섭동의 $u_\nu$ 미분이 path 위에서 갖는 값이다. $\langle\cdot\rangle$ 은 root가 주어졌을 때 tilted path 하나를 따른 기대값, $\mathbb E_{\mathbf u}$ 는 고정된 $\mathbf u$ 에서 root에 대한 평균이다([[g:root]], `perturbations.tex` 83–85). $e_{\nu,N}=\frac1{c_\nu s_N}\mathbb E_{\mathbf u}\langle\lvert D_\nu-\mathbb E_{\mathbf u}\langle D_\nu\rangle\rvert\rangle$ 은 그 정규화된 평균 절대 편차이고, "score가 [[g:self-average]]한다"는 $e_{\nu,N}\to0$ 을 뜻한다.
- **역할**: 매개변수 평균 집중(`pert:concentration`) → 선택(P5(ii)) → [[g:palm-identity|Palm 항등식]](`pert:palm`)의 부등식 $\lvert H_N(t_\nu,u_\nu)\rvert\le\lVert f\rVert_\infty e_{\nu,N}$ → Taylor 계수 소거(`pert:analytic`) → 항등식(P7)으로 이어진다.
- **정의 위치**: `pert:score`, `pert:error`, `pert:concentration`
- **물리 대응**: approximation — 섭동 에너지의 self-averaging. type별 진술이고 $L$ 이나 type에 균일하지 않다.

### g:selected-sequence — 선택된 수열 (선택된 섭동계)
- **기호**: $(N_j,\mathbf u_j)_{j\ge1}$; 이후 $N\to\infty$ 는 이 수열을 따른다
- **뜻**: 고정한 $L\ge2$ 와 $\varepsilon>0$ 마다 `pert:selection`이 주는 크기 $N_j\uparrow\infty$ 와 결정적 섭동 매개변수 $\mathbf u_j$ 의 수열로, (i) $\Delta_{N_j}(\mathbf u_j)\le\underline F+2\varepsilon$, (ii) reservoir에서 모든 고정 type의 $e_{\nu,N_j}(\mathbf u_j)\to0$, (iii) reservoir에서 깊이 $L$ 의 모든 유한 prescribed tree 위 multioverlap 유한곱의 기대값이 수렴한다. "선택된 섭동계"는 이 수열의 각 항에서 그 매개변수로 섭동한 reservoir(와 $N$-spin 계)를 말한다.
- **역할**: §6–§8의 모든 $N$ 극한이 이 수열을 따른다(`perturbations.tex` 308–312, `decorrelation.tex` 4–8, `comparison.tex` 8–15). (i)은 하한의 마지막 부등식(`comp:bounded-lower`), (ii)는 [[g:palm-identity|Palm 항등식]](`pert:palm`)의 부등식을 거쳐 [[g:tree-identity]], (iii)은 Taylor 계수의 수렴(`perturbations.tex` 399–409)에 쓰인다. P5가 이것을 진술하고 P7–P11이 받아 쓴다.
- **정의 위치**: `pert:selection`, `perturbations.tex` 308–312, 538–547
- **물리 대응**: intuition — 물리의 "무한소 섭동으로 generic한 계를 고른다". 실제 대상은 크기마다 다른 섭동계의 수열이며 극한 측도가 아니다.
- **쓰지 않는 뜻**: [[g:state]]가 아니다. "모든 $N$ 에서 generic"하다는 말이 아니고, $L$ 과 $\varepsilon$ 마다 다른 수열이며, 집중은 type별이라 $L$ 이나 type에 균일하지 않다. 예전 판의 "generic 상태"가 이것이다.

## Tree 계산과 항등식

### g:insertion — insertion $A$ 와 $\log Y_0$
- **기호**: $Y_L=A$, $Y_{d-1}=(K_dY_d^{m_d})^{1/m_d}$, $K_d^A=(Y_d/Y_{d-1})^{m_d}K_d$, $W_{\mathcal T}(A)$
- **뜻**: 반복할 분배함수의 tilted kernel $K_1,\ldots,K_{L-1}$ 과 terminal Gibbs kernel $K_L$ 을 쓰고(`trees.tex` 85–87), $A$ 가 root가 주어진 조건부로 위로 유계이고 0에서 떨어져 있다고 하자(원문이 처음에 두는 가정, `trees.tex` 73–74). 그러면 spin weight에 양의 path 함수 $A$ 를 곱하면 반복된 root logarithm이 정확히 $\log Y_0$ 만큼 바뀌고 kernel은 $K_d^A$ 로 바뀐다. tree 법칙의 밀도는 $W_{\mathcal T}(A)=\prod_aA^a\prod_\beta Y_\beta^{\gamma_\beta}$ 이다.
- **역할**: 증분(P4), 섭동 효과(P6, P7), 비교(P11)가 모두 이 꼴로 계산된다.
- **정의 위치**: `tree:insertion`, `tree:Y-recursion`, `tree:updated-kernel`, `tree:density`
- **물리 대응**: exact — Boltzmann weight 섭동 $-\delta H=\log A$ 에 따른 계층 free entropy 변화. $L=1$ 이면 $\log Y_0=\log(Z_A/Z)$.

### g:tree-coefficient — tree 계수 $\gamma_\beta$, $\kappa(S)$
- **기호**: $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$, $\kappa(S)=\prod_{v\in\operatorname{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$
- **뜻**: $\gamma_\beta$ 는 내부 vertex $\beta$(깊이 $d_\beta$, 자식 $n_\beta$ 개)에서 새 path를 붙일 때의 계수다. $\kappa(S)$ 는 anchor와 color가 모양 $S$ 를 갖는 모든 확장의 계수 합이다.
- **역할**: P6의 전개 계수이고 [[g:extension-history]]의 $c_E$ 를 이룬다. marker anchor 단계의 $C(S,e)=-\delta\kappa(S)$, 귀납의 정규화 $J=\kappa(S^+)^2$ 에 쓰인다(P8, P9).
- **정의 위치**: `tree:insertion`(`trees.tex` 92–96), `tree:reference-total`, `tree:K`
- **물리 대응**: intuition — replica trick의 Parisi block counting($n\to0$). 논문은 유한 tree에서 직접 세우고 $n\to0$ 을 쓰지 않는다.
- **쓰지 않는 뜻**: 부호가 섞인 계수가 아니다. $n_\beta\ge1$ 이고 $m_{d_\beta}<m_{d_\beta+1}$ 이므로 $\gamma_\beta<0$ 이 항상 성립한다(`trees.tex` 204–209 "All summands are positive", 245–246 "all $k-1$ fresh coefficients are negative"). $\kappa(S)$ 의 인자 $m_{d_v}-jm_{d_v+1}$ $(j\ge1)$ 도 모두 음수라서 $\kappa(S)$ 의 부호는 $(-1)^{\sum_v(a_v-1)}$ 로 topology만으로 정해진다(`tree:K`의 식에서 읽은 것). 부호가 섞이는 것은 [[g:extension-history]]의 $c_E$ 다: old leaf 선택은 계수 $+1$, fresh path는 음수 계수 $\gamma_\beta$ 다(`trees.tex` 264–268). 그 합의 상쇄(부호 있는 합 $-\delta$, 절댓값 합 $2+\delta$, `trees.tex` 317–329)가 [[g:depth-delay]]의 대상이다.

### g:tree-law — tree 법칙 $Q_k$ 와 log 전개
- **기호**: $Q_k$; $\log Y_0=\sum_{k\ge1}\frac{(-1)^{k-1}t^k}{k}\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a$
- **뜻**: path 하나에서 시작해, leaf가 $n$ 개일 때 내부 vertex $\beta$ 를 확률 $(n_\beta m_{d_\beta+1}-m_{d_\beta})/n$ 로 골라 새 path를 붙여 가는 무작위 tree 법칙이다. $A=1+tD$ 의 $\log Y_0$ 가 이 법칙의 tree 평균 급수로 정확히 쓰인다($\lvert t\rvert\lVert D\rVert_\infty<1$).
- **역할**: P6. P11에서 삽입 log를 $Q_k$ 평균으로 쓰기 때문에 [[g:overlap-concentration]]의 깊이 평균으로 충분하다(`tree:regular-shapes`, `tree:averaging-remark`, `comp:shape-error-bound`).
- **정의 위치**: `tree:Q-rule`, `tree:log-expansion`
- **물리 대응**: intuition — cascade에서 뽑은 $k$ 개 replica의 overlap tree 법칙(nested Chinese restaurant). 논문은 이 동일시를 증명하거나 쓰지 않는다.

### g:protected-leaf — protected leaf
- **기호**: protected leaf 집합 $C$, $E_{\mathcal T}^A[G\prod_{a\in C}(A^a)^{-1}]$
- **뜻**: tree 밀도 $W_{\mathcal T}(A)$의 leaf 인자 $A^a$가 분모 $A^a$로 상쇄된 leaf다. 이 leaf에서는 삽입 매개변수로 미분해도 새 항이 생기지 않는다. 미분으로 $D_j^a/A^a$를 받은 leaf와 새로 붙은 fresh leaf는 곧바로 protected가 된다(`trees.tex` 180–183, 190–196).
- **역할**: 미분 규칙(`x:tree-differentiation-rule`)의 회계다. 모든 leaf가 protected이면 미분은 fresh path만 붙이고 이것이 log 전개의 $Q_k$를 낳는다(`tree:log-expansion`). anchor를 처음부터 protected로 두는 것이 canceled-anchor 전개(`tree:extension-expansion`)이고, 그래서 [[g:extension-history]]의 선택지에서 anchor가 빠진다. §6의 Palm 단계에서 anchor 인자 $A^{a_*}$가 상쇄되는 것(`perturbations.tex` 370–371)이 이 상황이다.
- **정의 위치**: `trees.tex` 180–183, `x:tree-differentiation-rule`
- **물리 대응**: 없음.

### g:extension-history — extension history 와 계수 $c_E$
- **기호**: $E$, $a_j(E)$, $\mathcal T_E$, $c_E$, color $1,\ldots,k$
- **뜻**: anchor leaf $a_*$ 가 있는 old tree에서 color $1,\ldots,k$ 를 차례로 (i) 아직 안 쓴 anchor 아닌 old leaf(계수 1) 또는 (ii) 현재 tree의 내부 vertex $\beta$ 에서 새 path(계수 $\gamma_\beta$)에 주는 선택의 기록이다. $c_E$ 는 그 계수들의 곱이다. 어휘: old tree는 섭동을 넣기 전에 주어진 tree이고 그 path와 leaf가 old path, old leaf다(`trees.tex` 259–261). fresh path는 (ii)로 새로 만든 path로, 갈라지는 vertex에서 새 자식을 쓰고 그보다 깊은 모든 깊이에서 새 vertex를 쓴다(`trees.tex` 270–271). 제약이 쓰는 기준 path는 [[g:reference-path]]다. $c_E$ 는 부호가 섞인다: old leaf는 $+1$, fresh path는 음수 $\gamma_\beta$ 다([[g:tree-coefficient]]).
- **역할**: canceled-anchor 전개(`tree:extension-expansion`)의 합 범위이고, P7 항등식은 이 합에 대한 것이다.
- **정의 위치**: `trees.tex` 259–276, `tree:extension-expansion`
- **물리 대응**: 없음.

### g:reference-path — reference path
- **기호**: anchor $a_*$와 이미 color를 받은 path; 처방된 reference 모양 $S$, 한 걸음 합 $m_d-jm_{d+1}$, $\kappa(S)$
- **뜻**: extension history에서 anchor와 이미 color를 받은 path를 말한다. 새 color에 대한 제약은 이 path들과의 갈라짐 깊이만 지정하고, 지정된 조상 관계가 같은 쓰지 않은 old path들은 구별하지 않는다("does not distinguish unused old paths with the same specified ancestry", `trees.tex` 311–315).
- **역할**: 한 걸음 계수 합이 현재 reference tree에만 의존해서 old tree와 무관한 닫힌 꼴 $\kappa(S)$가 된다(`tree:reference-total`). [[g:depth-delay]]에서 처방하는 것이 reference 모양이다(`tree:charging`). §7의 $J=\kappa(S^+)^2$, $C(S,e)=-\delta\kappa(S)$(`decorrelation.tex` 332–335), §6 제약 $\mathcal C$("anchor와 added color 사이의 split 깊이만", `perturbations.tex` 433–436)가 이것을 쓴다.
- **정의 위치**: `trees.tex` 311–315, `x:tree-reference-paths`
- **물리 대응**: 없음.

### g:anchor — anchor (spin anchor, marker anchor)
- **기호**: $a_*$, $S_0=\sigma_i$(spin anchor), $S_0=1$(marker anchor)
- **뜻**: 섭동을 넣는 old tree의 구별된 leaf다. 그 leaf에서 삽입 인자 $A^{a_*}$ 가 상쇄된다. spin anchor는 $R_E$ 에 anchor spin을 넣고, marker anchor는 spin을 내지 않는다.
- **역할**: spin anchor는 singleton 집중(P9, `decor:overlap-concentration.s1`, `decorrelation.tex` 533–535)과 상태 안 귀납(P8, `decor:conditional-concentration`, `decorrelation.tex` 265, 296–297)에, marker anchor는 상태 사이 요동 $\operatorname{Var}(M)\to0$(P9, `decor:overlap-concentration.s2`)에 쓰인다.
- **정의 위치**: `trees.tex` 259–260, `perturbations.tex` 316–321, 429–449
- **물리 대응**: 없음.

### g:mark — mark 와 selector
- **기호**: Rademacher 좌표(깊이 $1,\ldots,L-1$), 좌표의 함수 $g,g_0:\{-1,1\}^n\to\mathbb Q\cap[-1,1]$, $S_0\in\{1,\sigma_i\}$, 공유 지시함수 $H_d$, 제약 $\mathcal C$, `pert:mark-selector`
- **뜻**: mark specification은 유한 개의 Rademacher 좌표, 각 좌표의 깊이, 좌표의 유리수값 함수 $g$, $g_0$, 그리고 $S_0$ 의 선택을 묶은 것이다(`perturbations.tex` 28–35). 좌표는 지정된 깊이에서 path를 따라 뽑히고 공유 vertex에서는 값을 공유한다. 두 color $a,b$ 의 $g_a$, $g_b$ 에 같은 새 좌표의 인자를 넣으면 mark 기대값이 "$a,b$ 가 깊이 $d$ vertex를 공유", 곧 "split 깊이 $\ge d$"의 지시함수 $H_d(a,b)$ 가 된다(selector, `perturbations.tex` 494–511). 정확히 깊이 $d$ 의 split은 $H_d-H_{d+1}$ 로 쓰고, 그 곱과 유한 일차결합으로 원하는 split 깊이 제약 $\mathcal C$ 를 고른다(`perturbations.tex` 514–520).
- **역할**: P7에서 anchor와 새 color 사이의 split 깊이를 지정한다(다른 old replica와의 관계는 지정하지 않는다). reservoir에서는 mark 변수가 [[g:hierarchy]]의 보조 변수다.
- **정의 위치**: `perturbations.tex` 28–38, 494–524, `pert:mark-selector`
- **물리 대응**: intuition — 계층 깊이마다 무작위 부호를 갖는 탐침장. 물리적 국소장이 아니라 selector를 만드는 장치다.

### g:palm-identity — Palm 항등식과 Taylor 계수 소거
- **기호**: $J_{N,\mathcal T}(t,u)$, $H_N(t,u)=J_{N,\mathcal T}(t,u)-\mathbb Ef\,J_{N,\{a_*\}}(t,u)$; $\lvert H_N(t_\nu,u_\nu)\rvert\le\lVert f\rVert_\infty e_{\nu,N}$
- **뜻**: Palm 항등식(`pert:palm`, 원문 이름 "Palm identity")은 Poisson add-one 항등식으로 score 곱 $\mathbb E[fD_\nu^{a_*}]/(c_\nu s_N)$ 을, reservoir 법칙은 그대로 둔 채 anchor $a_*$ 에 새 섭동 하나($A=1+t_\nu g\sigma_i+u_\nu g_0S_0$)를 넣은 tree 기대값 $J_{N,\mathcal T}(t_\nu,u_\nu)$ 로 바꾼다. 그래서 score 오차가 차이 $H_N$ 을 위 부등식으로 누른다(쓰이는 결론은 이 부등식이다). $H_N(t,u)$ 는 같은 mark specification의 모든 type $j$ 에 대해 같은 함수다. Taylor 계수 소거(`pert:analytic`)는 $u_\nu\in[j^{-j},2j^{-j}]$ 가 $t_\nu=1/j$ 의 모든 고정 거듭제곱보다 작다는 것으로, $H_N(t,0)$ 의 $t=0$ Taylor 계수가 모두 선택된 수열을 따라 0으로 감을 보인다("Taking $u$ smaller than every fixed power of $t$ will force each limiting Taylor coefficient to vanish", `perturbations.tex` 40–43).
- **역할**: score 집중(P5(ii), [[g:score]])에서 항등식(P7, [[g:tree-identity]])으로 넘어가는 다리다. 계수의 극한 존재는 P5(iii)이 준다(`perturbations.tex` 399–409). 그 계수를 [[g:extension-history]]로 풀고 polarization과 [[g:mark]] selector로 제약을 고르면 `pert:tree-identity`가 된다(`perturbations.tex` 472–535). 극한은 $j$ 를 고정하고 $N\to\infty$ 한 뒤 $j\to\infty$ 다([[g:order-of-limits]]).
- **정의 위치**: `pert:palm`, `pert:analytic`, `perturbations.tex` 314–425
- **물리 대응**: 없음. 규칙 표에서는 "규칙으로 못 옮긴 것"의 Taylor 계수 추출 항목이다.

### g:tree-identity — prescribed-tree 항등식
- **기호**: $\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\,\mathbb E[fR_E]-\mathbb Ef\sum_{E\in\mathfrak E(\{a_*\},a_*,\mathcal C)}c_E\,\mathbb E[R_E]\to0$
- **뜻**: [[g:selected-sequence]] 위에서, 고정한 old tree $\mathcal T$, anchor 종류, old multioverlap의 유계 다항식 $f$, 추가 color 수, split 깊이 제약 $\mathcal C$ 마다 위 식이 성립한다. 곧 제약을 지키는 [[g:extension-history]]에 대한 부호 있는 계수 합이 시험함수 $f$ 와 분리된다. 오차는 고정 $L$, tree, 제약에서 $N\to\infty$ 로만 사라진다.
- **역할**: §7이 모형에서 받는 유일한 입력이다: §7은 "these identities and the tree sampling rules"만 쓰고 상호작용 factorization을 쓰지 않으며(`decorrelation.tex` 4–9), 여기에 §3의 유한 tree 조합(`tree:reference-total`, `tree:charging`)과 모형 무관한 확률 부등식(`decor:contractions`, `decor:depth-continuity`)만 더해 모든 multioverlap의 깊이 평균 집중 `decor:overlap-concentration`을 얻는다. §8은 이 항등식에서만 나오지 않는다: §7의 집중에 증분 항등식 `cavity:identity`(P4, `comparison.tex` 195–196, 221–222), 선택된 수열의 낮은 증분 `comp:low-increments`(P5(i), `comparison.tex` 13–15, 235–236), encoding(P10), 균일 site 표본(`comp:patterns`), log 전개(P6), 유계성 $C=H+BM$ 과 Poisson 개수 절단(`comparison.tex` 198–217)을 더해 $\Delta_N\approx\mathcal B_{L-1}$ 과 하한을 얻는다(`comp:shape-error`, `comp:insertion-comparison`, `comp:bounded-lower`). 이 입력들 가운데 어느 것도 factorization이나 positivity를 쓰지 않으므로(`cavity.tex` 13–14, `overview.tex` 46–48), L1 수 5–6은 bounded·순열 불변 상호작용에 대해 상호작용의 구체적 꼴과 무관하다. 받아 쓰는 곳은 P7, P8, P9와 `decor:conditional-concentration`, `decor:overlap-concentration`이다.
- **정의 위치**: `pert:tree-identity`(`perturbations.tex` 451–470), 제약과 $R_E$ 는 `perturbations.tex` 427–449
- **물리 대응**: intuition — 논문은 집중으로 overlap 항등식을 얻는 방법의 antecedent로 Ghirlanda–Guerra의 self-averaging 논법, Aizenman–Contucci의 stochastic stability 관계, 그 diluted multioverlap 확장(Barra–De Sanctis)을 들 뿐이고(`perturbations.tex` 17–21), 이 항등식이 그것들과 같다거나 그것들에서 나온다고 하지 않는다. 꼴도 고전적 Ghirlanda–Guerra 항등식("새 replica의 overlap은 확률 $1/n$ 으로 기존 replica를 복사"; 원문에 없는 대조용 요약이고 항등식의 한쪽 항만 말한다)이 아니라 extension history 위의 부호 있는 합이며, 두 꼴의 상호 유도는 여기서 확인하지 않았다. 이 이름이 물리학자에게 주던 "이것만으로 아래가 다 나온다"는 정보는 위 역할 칸이 근거와 함께 대신한다.
- **쓰지 않는 뜻**: 계층(tree) 구조는 이 항등식에서 유도되는 것이 아니라 보조 계층의 구성에 들어 있다(`introduction.tex` 75–77). 이것에서 물리적 Gibbs 측도의 계층 구조는 나오지 않고, overlap 극한값이나 분포도 식별되지 않는다. $\lvert S\rvert\ge2$ 의 multioverlap에 대해 논문은 고정 깊이 배정마다의 집중을 얻지 않는다(깊이 평균만, `decorrelation.tex` 63–75; "No uniform concentration in the depth is needed", `overview.tex` 46). 이것은 얻지 않는다는 말이지 거짓이라는 말이 아니다. 반면 항등식에서 고정 깊이로 바로 나오는 것도 있다: singleton의 $\operatorname{Var}(R_S)\to0$(각 고정 $L$, `decorrelation.tex` 72–74, 533–535)과 prefix 사영의 $\operatorname{Var}(M)\to0$(각 고정 $L,S,e$, `decorrelation.tex` 563–566).

### g:depth-delay — 깊이 미루기 (부호 있는 계수의 상쇄 제어)
- **기호**: $S\to S^+$, $J=\kappa(S^+)^2$, 상대 비용 $\frac1{\lvert J\rvert}\sum_E\lvert c_E\rvert\le C_{k,\eta}$
- **뜻**: target(항등식의 제약 $\mathcal C$ 가 anchor와 새 color에 요구하는 모양) tree의 내부 branching 깊이를 한 칸 늦춰 각 새 split이 계수 $\delta$ 하나를 내게 하는 장치다. 부호 있는 합과 절댓값 합의 크기 차이를 상대 비용 상계로 제어한다.
- **역할**: 항등식을 $J$ 로 나눈 뒤에도 오차가 유계로 남게 해서 P8의 귀납을 닫는다.
- **정의 위치**: `tree:charging`, `decor:J-definition`, `decor:J-lower-bound`, `decor:relative-absolute-cost`, `decorrelation.tex` 77–83
- **물리 대응**: 없음.

## 집중

### g:multioverlap — multioverlap $R_S$ (overlap)
- **기호**: $R_S=\frac1N\sum_{i=1}^N\prod_{a\in S}\sigma_i^a$, $R_\varnothing=1$
- **뜻**: replica leaf 집합 $S$ 위 spin 곱의 공간 평균이다. $\lvert S\rvert=2$ 가 보통의 overlap, $\lvert S\rvert=1$ 이 자화다.
- **역할**: P5(iii)의 모멘트, P7의 시험함수 $f$ 와 $R_E$, P9 집중의 대상이고, P11에서 spin pattern의 경험분포를 정한다($\pi(\mathbf e)=2^{-k}\sum_SR_S\prod_{b\in S}e_b$).
- **정의 위치**: `tree:multioverlap`
- **물리 대응**: exact — overlap과 multi-replica overlap. 희석 모형에서는 pair overlap만으로 replica-spin pattern이 정해지지 않아 모든 $R_S$ 가 필요하다(`introduction.tex` 65–73).

### g:spin-product — spin-product vector $A_S$
- **기호**: $A_S=(\prod_{a\in S}\sigma_i^a)_{i\le N}$, $x\cdot y=N^{-1}\sum_ix_iy_i$, $\lVert x\rVert_N^2=x\cdot x$, $R_S=\mathbf1\cdot A_S$
- **뜻**: sampled copy의 leaf spin 곱을 site별로 모은 벡터와 그 정규화 내적이다.
- **역할**: §7의 모든 축약과 노름이 이 위에서 계산된다([[g:conditional-covariance]], [[g:three-copy]]).
- **정의 위치**: `decorrelation.tex` 87–93, `x:decor-spin-product`
- **물리 대응**: 없음.

### g:conditional-covariance — 조건부 평균 $\mu_{d,S}$ 와 조건부 공분산 제곱 $v_N(S,d)$
- **기호**: $\mu_{d,S}=\mathbb E[A_S\mid\mathscr F_d]$, $v_N(S,d)=\frac1{N^2}\mathbb E\sum_{i,j=1}^N\operatorname{Cov}(A_{S,i},A_{S,j}\mid\mathscr F_d)^2$
- **뜻**: $S$ 의 initial stem 위 깊이 $d$(첫 branching 깊이 포함)에서, [[g:state]]가 주어졌을 때 spin-product vector의 site별 조건부 공분산 제곱을 site 쌍에 대해 평균하고 [[g:root]]까지 기대값을 취한 양이다. $0\le v_N\le1$ 이다.
- **역할**: P8 귀납의 대상이다. 세 사본 부등식으로 overlap 차이에 눌리고(`decor:three-copy-bound`), 사영 오차 $p_N$ 을 통제한다([[g:projection]]).
- **정의 위치**: `decor:covariance-definition`
- **물리 대응**: approximation — singleton이면 상태 안 connected correlation $\langle\sigma_i\sigma_j\rangle_d-\langle\sigma_i\rangle_d\langle\sigma_j\rangle_d$ 제곱의 site 쌍 평균이다. $\lvert S\rvert\ge2$ 이면 여러 replica spin 곱의 공분산이라 단일 replica의 두 점 상관함수가 아니다.

### g:clustering — clustering
- **기호**: $\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}v_N(S,d)=0$
- **뜻**: 이 사이트의 "clustering"은 `decor:conditional-concentration`의 결론 하나만 가리킨다. 모든 고정 labeled topology $S$ 와 $\eta>0$ 에서, [[g:selected-sequence]]를 따라 $N\to\infty$ 한 뒤 $L\to\infty$ 하면 [[g:conditional-covariance]] $v_N(S,d)$ 의 [[g:depth-average]]가 0으로 간다. $\lvert S\rvert\ge2$ 이면 평균은 $S$ 의 모든 branching 깊이와 첫 split보다 엄격히 앞선 추가 깊이 $d$ 의 $\eta$-regular 배정에 대해 취하고, singleton이면 $d$ 하나에 대해 취하며 이때는 더 강하게 각 고정 $L$ 과 $d/L\in(\eta,1-\eta)$ 에서 $\limsup_Nv_N(S,d)\le1/(\eta L)$ 이다(`decorrelation.tex` 287–290).
- **역할**: `decor:overlap-concentration` 증명에서 prefix 아래 조건부 분산을 누르는 재료다($V_{k-1,L}(\eta/2)\to0$, `decor:overlap-concentration.s4`, `.s5`). 여기서 $V_{k,L}(\eta)=\max_{1\le\lvert S\rvert\le k}\limsup_N\mathcal A_{L,\eta}v_N(S,d)$ 는 잎이 $k$ 개 이하인 모든 topology에 대한 최댓값이다(`decor:V-definition`, `decorrelation.tex` 253–257). 귀납 안에서는 자식을 상태 평균으로 바꾸는 [[g:projection]] 오차를 작게 한다. P8이 진술하고 P9가 쓰며, P11에는 P9를 거쳐 간접적으로만 쓰인다.
- **정의 위치**: `decor:conditional-concentration`, `decor:covariance-definition`, singleton은 `decorrelation.tex` 287–290
- **물리 대응**: approximation — 물리의 "물리적 pure state 안에서 connected correlation이 사라진다". 여기서 조건은 보조 계층 prefix이고, 양은 site 쌍에 대한 $L^2$ 평균이며, $\lvert S\rvert\ge2$ 에서는 깊이 평균으로만 성립한다.
- **쓰지 않는 뜻**: 그래프 거리에 따른 상관 감쇠가 아니다(거리 개념을 쓰지 않는다). 모든 site 쌍에 대한 진술이 아니다. 물리적 pure state 안의 clustering이 아니다. 이웃 cavity field의 독립([[g:independent-copies]])을 혼자서 주지 않는다. $\lvert S\rvert\ge2$ 에서 고정 깊이 진술이 아니다.

### g:depth-average — 깊이 평균 $\mathcal A_{L,\eta}$
- **기호**: $\mathcal A_{L,\eta}z=L^{-a}\sum_{\mathbf q\ \eta\text{-regular}}z(\mathbf q)$
- **뜻**: $a$ 개 깊이 좌표의 [[g:eta-regular]] 배정에 대한, 정규화하지 않은(질량 $\le1$) 평균이다. 추가 순서 제약은 합 범위에 넣는다.
- **역할**: P8, P9 결론의 형식이다. $\mathcal A(z^\gamma)\le(\mathcal Az)^\gamma$(`decor:average-holder`)로 분수 거듭제곱을 다루고, P11에서 $Q_k$ 평균으로 넘어간다(`comp:shape-error-bound`).
- **정의 위치**: `decor:average-definition`
- **물리 대응**: intuition — 갈라짐 위치를 Parisi 변수 $x\in(\eta,1-\eta)$ 에 대해 균등하게 평균하는 것.
- **쓰지 않는 뜻**: 고정 깊이에서의 진술이 아니다.

### g:self-average — self-average
- **기호**: 없음
- **뜻**: 어떤 무작위 양이 [[g:root]](disorder, 섭동 개수·type·site)와 tree 표본추출 전부에 대한 평균 주위로 집중한다는 말이다. 정량은 양마다 정해 둔다: score는 $e_{\nu,N}\to0$([[g:score]]), multioverlap은 [[g:overlap-concentration]]의 식이다.
- **역할**: P5, P9 문장의 물리 말을 이 두 정량 진술에 묶는다.
- **정의 위치**: `pert:error`, `decor:overlap-concentration`
- **물리 대응**: approximation — 물리의 self-averaging. 수열과 극한 순서는 해당 항목을 따른다.
- **쓰지 않는 뜻**: disorder 표본 하나에 대한 거의 확실한 수렴을 말하지 않는다.

### g:overlap-concentration — multioverlap 집중
- **기호**: $\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}\operatorname{Var}(R_S)=0$ $(\eta>0)$
- **뜻**: 모든 고정 labeled topology $S$ 에서 위 식이 성립한다. 평균은 $S$ 의 $b(S)$ 개 branching 깊이에 대해서이고, singleton은 각 고정 $L$ 에서 $\operatorname{Var}(R_S)\to0$ 이다. 분산은 [[g:root]]와 tree 표본추출 전부에 대한 것이고(섭동 매개변수는 선택된 값으로 고정) $N$ 극한은 [[g:selected-sequence]]를 따른다.
- **역할**: P9. §8로 가는 출력이다: `comp:shape-error`를 거쳐 P11의 독립 사본 대체 오차를 0으로 보낸다(`comparison.tex` 122–156).
- **정의 위치**: `decor:overlap-concentration`
- **물리 대응**: approximation — "branching pattern을 정하면 overlap은 요동하지 않는다"는 Parisi 그림을 모든 multioverlap으로 넓힌 것.
- **쓰지 않는 뜻**: 극한값을 식별하지 않는다(overlap이 깊이만의 함수 $q_d$ 로 수렴한다는 말이 아니다). 물리적 Gibbs 측도의 계층 구조에 대한 진술이 아니다. $\lvert S\rvert\ge2$ 에서 고정 깊이 배정마다의 진술이 아니다.

### g:projection — 첫 갈라짐에서의 사영 $a_{S,e}$, $p_N(S,e)$
- **기호**: $a_{S,e}=\prod_{j=1}^s\mu_{e,T_j}$, $p_N(S,e)=\sum_{j=1}^sv_N(T_j,e)^{1/4}$
- **뜻**: $S$ 가 깊이 $e$ 에서 처음 자식 $T_1,\ldots,T_s$ 로 갈라질 때, 각 자식의 spin 곱을 상태 평균 $\mu_{e,T_j}$ 로 바꾼 벡터와 그 바꿈의 오차량이다. $e$ 아래 continuation과 조건부 독립인 $B\in[-1,1]^N$ 에 대해 $\lVert(A_S-a_{S,e})\cdot B\rVert_{L^2}\le p_N(S,e)$ 다.
- **역할**: P8 귀납과 P9 증명(`decor:overlap-concentration.s3`)에서 자식을 평균으로 바꾸는 단계다.
- **정의 위치**: `decor:projection-definition`, `decor:projection-bound`
- **물리 대응**: approximation — cavity 계산에서 "한 물리적 pure state 안에서는 spin을 국소 자화(평균장)로 대체"하는 단계에 해당하고, 여기서는 보조 계층 prefix가 물리적 pure state 자리에 있다. 오차는 $v_N^{1/4}$ 로만 통제되고 조건부 독립인 벡터와의 축약에만 적용된다.

### g:three-copy — 축약 부등식과 세 사본 부등식
- **기호**: $\lVert(A_S-\mu_{d,S})\cdot B\rVert_{L^2}\le v_N(S,d)^{1/4}$; $\mathbb E(X\cdot Y-X\cdot Z)^2\ge\frac2{N^2}\mathbb E\sum_{i,j}C_{ij}^2$
- **뜻**: 첫째는 상태 안에서 조건부 독립인 벡터와의 축약 오차를 $v_N$ 로 누르는 부등식, 둘째는 $\sigma$-field $\mathscr G$ 가 주어지면 조건부 독립인 세 사본의 overlap 차이가 조건부 공분산 제곱을 위에서 누르는 부등식이다.
- **역할**: 둘째가 P8의 기저와 귀납 단계에서 항등식을 $v_N$ 상계로 바꾸고, 첫째가 [[g:projection]]을 준다.
- **정의 위치**: `decor:contractions`, `decor:contraction-bound`, `decor:three-copy-bound`
- **물리 대응**: weakening — 물리의 "조건이 주어졌을 때 overlap이 요동하지 않으면 connected correlation이 작다"의 정량적 한 방향 판. 둘째 부등식의 조건은 일반 $\sigma$-field $\mathscr G$ 이고, 상태 $\mathscr F_d$ 는 그 특수한 경우다.

### g:depth-continuity — 깊이 연속성 (martingale energy)
- **기호**: $\sum_t\mathbb E\lVert\mu_{t+1,T}-\mu_{t,T}\rVert_N^2\le1$; $\mathcal A_{L,\eta}\mathbb E\lVert\mu_{d,S^U}-\mu_{d,S}\rVert_N^2\le C/L$
- **뜻**: 한 path를 따라 상태 평균 $\mu_{t,T}$ 는 유계 vector martingale이라 증분 에너지의 합이 1 이하다. 그래서 충분히 큰 $L$ 에서 갈라짐 깊이를 한 칸 옮기는 비용은 깊이 평균으로 $C/L$ 이다. 평가 깊이 $d$ 를 한 칸 옮기는 비용의 같은 $C/L$ 상계는 $d$ 가 $S$ 의 initial unary 구간 위를 움직일 때의 진술이다. $C$ 는 vertex 수와 이동 수에만 의존하고 $N$, 평가 깊이, kernel에 균일하다(`decorrelation.tex` 148, 155–165).
- **역할**: 깊이를 미룬 사본과 원래 사본을 비교하는 비용 $h_N$(P8)과 인접 prefix 오차(P9)를 준다. 모형과 kernel에 무관한 사실이다.
- **정의 위치**: `decor:depth-continuity`, `decor:martingale-energy`
- **물리 대응**: intuition — Parisi 함수 $q(x)$ 가 단조 유계라 큰 점프가 드물다는 그림과 닮았다. 실제로 쓰는 단조량은 깊이별 자기 overlap $\mathbb E\lVert\mu_{t,T}\rVert_N^2$ 이다.

### g:order-of-limits — 극한 순서
- **기호**: $\lim_{\varepsilon\downarrow0}\lim_{\eta\downarrow0}\lim_{L\to\infty}\limsup_{N\to\infty}$(바깥에서 안쪽 순)
- **뜻**: 하한의 극한은 $L$, $\varepsilon$, $\eta$ 를 고정하고 [[g:selected-sequence]]를 따라 $N\to\infty$, 그다음 $L\to\infty$, 그다음 $\eta\downarrow0$(§8의 shape error), 마지막으로 $\varepsilon\downarrow0$ 의 순서로만 취한다. §6 안에서는 type 지수 $j$ 를 고정하고 $N\to\infty$ 한 뒤 $j\to\infty$ 이고, 비교 안에서는 Poisson 절단 $M$ 과 전개 차수 $q$ 를 먼저 고정한다.
- **역할**: P5, P7–P11의 차이 칸이 이 순서를 가리킨다. `decor:order-of-limits`는 $L$ 에 의존하는 작은 분모가 고정 $L$ 에서 먼저 사라지는 항등식 오차에만 붙는다는 것을 정리한다.
- **정의 위치**: `decor:order-of-limits`, `x:decor-limit-order`, `perturbations.tex` 538–547, `comparison.tex` 130, 153–156, 218–222
- **물리 대응**: 없음. 물리 유도는 순서를 따지지 않는다.
- **쓰지 않는 뜻**: $L$ 에 균일한 $N$ 수렴 속도를 주지 않는다(`decorrelation.tex` 621–622).

## 비교

### g:encoded-law — encoded trial law $\zeta_{L,N}$
- **기호**: $\zeta_{L,N}=\operatorname{Law}(\eta_0)\in\mathcal M_L$
- **뜻**: 고정한 $N$, $L$, 선택된 매개변수에서, reservoir root와 독립 균일 site $i$ 를 root에 넣고 tilted kernel로 뽑은 path 위에 $x=\operatorname{arctanh}\langle\sigma_i\rangle$(깊이 $r=L-1$), $\eta_{r-1}=\operatorname{Law}(x\mid\mathscr G_{r-1})$, $\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)$ 를 거꾸로 쌓아 얻은 시행 법칙이다. 한 label의 spin 과정은 모든 prescribed tree에서 균일 site와 같은 기대 spin 곱 $\mathbb ER_S$ 를 갖는다.
- **역할**: P10. P11에서 독립 사본의 원천이다.
- **정의 위치**: `comp:encoding`, `comp:single-label-moments`
- **물리 대응**: exact(부호화) — 한 label이 모든 prescribed tree에서 $\mathbb ER_S$ 를 보존한다(`comp:single-label-moments`). intuition(해석) — 이것을 계의 RSB order parameter(물리적 pure state 계층에 따른 cavity field 분포)로 읽는 것. 여기서 깊이는 섭동 mark로 만든 보조 계층의 것이고(`cavity.tex` 23–24), 물리적 Gibbs 측도의 계층은 가정하지 않는다(`introduction.tex` 75–77, [[g:depth]]).
- **쓰지 않는 뜻**: 극한 order parameter나 최적 $\zeta$ 가 아니다. $N$, $L$, $\mathbf u$ 에 따라 달라진다.

### g:spin-pattern — spin pattern
- **기호**: $\boldsymbol\sigma_i=(\sigma_i^1,\ldots,\sigma_i^k)$, 경험분포 $\pi(\mathbf e)$, $\bar\pi=\mathbb E\pi$
- **뜻**: site $i$ 에서 $k$ 개 replica leaf의 spin 값 묶음이다. 균일 site에서 그 경험분포는 $\pi(\mathbf e)=2^{-k}\sum_{S\subseteq[k]}R_S\prod_{b\in S}e_b$ 이고, encoded law의 한 label 분포는 $\bar\pi=\mathbb E\pi$ 다.
- **역할**: P11에서 바꾸는 대상이다. $\lVert\pi^{\otimes a}-\bar\pi^{\otimes a}\rVert_{\rm TV}\le\frac a2\sum_{S\ne\varnothing}\lvert R_S-\mathbb ER_S\rvert$ 로 오차가 multioverlap 요동에 묶인다.
- **정의 위치**: `comp:patterns`, `comparison.tex` 99–120
- **물리 대응**: 없음.

### g:independent-copies — 독립 사본 대체 ("이웃 cavity field의 독립")
- **기호**: `comp:pattern-error` $a\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\lvert R_S-\mathbb ER_S\rvert$
- **뜻**: 이 사이트에서 "이웃 cavity field의 독립"은 다음 진술 하나만 가리킨다: cavity 삽입($A_{\rm s}$, $A_{\rm b}$)이 쓰는 reservoir site label들의 replica-spin pattern을 [[g:encoded-law]]의 서로 독립인 label 사본으로 바꿔도 기대 삽입 log가 $\lim_L\limsup_N$ 의 뜻으로 변하지 않는다(`comp:insertion-comparison`). 독립 균일 site label $a$ 개를 바꾸는 오차는 위 식 이하다(`comp:patterns`).
- **역할**: P11. 독립 사본으로 계산한 삽입이 정확히 $\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$ 이므로 하한이 닫힌다(`comp:bounded-lower`).
- **정의 위치**: `comp:patterns`, `comp:shape-error`, `comp:insertion-comparison`; 서로 다른 label의 독립 구성은 `comparison.tex` 80–82
- **물리 대응**: approximation — cavity method의 "한 물리적 pure state 안에서 이웃 site들의 cavity field는 독립". 논문의 근거는 국소 tree 구조나 거리에 따른 상관 감쇠가 아니라 균일 무작위 site 표본과 모든 multioverlap의 집중(P9)이다.
- **쓰지 않는 뜻**: 고정한 두 site의 결합 법칙이 곱이라는 말이 아니다. [[g:clustering]]만으로는 나오지 않는다. 물리적 pure state 안의 독립이 아니다.

## 축소

### g:constant-shift — 상수 이동
- **기호**: $c=\theta(1,\ldots,1)$, $\widehat\theta=\theta-c$; $\widehat F_N=F_N-\alpha\mathbb Ec$, $\widehat{\mathcal B}_r=\mathcal B_r-\alpha\mathbb Ec$
- **뜻**: spin 무관인 적분 가능한 상수를 상호작용에서 빼는 것이다. pressure와 시행 functional이 같은 양 $-\alpha\mathbb Ec$ 만큼 움직인다.
- **역할**: `main:theorem` 증명에서 [[g:factorization]]의 $a$ 를 없애고 $\widehat\theta$ 의 법칙을 순열 불변으로 만든다(P1, P12). 하한을 얻은 뒤 되돌린다.
- **정의 위치**: `reduction:shift`, `reduction.tex` 45–59
- **물리 대응**: exact — 에너지 원점 이동.

### g:truncation — truncation
- **기호**: $\widehat\theta^{(K)}$, $h^{(K)}$, $D_K$, $d_K$
- **뜻**: $\widehat\theta$ 의 각 값과 $h$ 를 $[-K,K]$ 로 자르는 것이다. 순열 불변성을 보존하고, $D_K=\mathbb E\max_s\lvert\widehat\theta-\widehat\theta^{(K)}\rvert\to0$, $d_K=\mathbb E\lvert h-h^{(K)}\rvert\to0$ 이다.
- **역할**: bounded 하한(`comp:bounded-lower`)을 1차 moment 가정만 있는 경우로 넘긴다(P12): $\liminf_N\widehat F_N\ge\inf_r\widehat\Phi_r-2\alpha pD_K-2d_K$.
- **정의 위치**: `reduction.tex` 61–84
- **물리 대응**: 없음. 물리 유도는 이 단계를 생략한다.

### g:stability — $L^1$ 안정성
- **기호**: $\lvert F_N-F_N'\rvert\le\alpha D+d$, $\lvert\mathcal B_r-\mathcal B_r'\rvert\le\alpha(2p-1)D+d$
- **뜻**: 두 상호작용·장 법칙을 결합했을 때 pressure와 시행 functional이 $D=\mathbb E\max_s\lvert\theta-\theta'\rvert$, $d=\mathbb E\lvert h-h'\rvert$ 에 Lipschitz라는 것이다. 시행 쪽 상수는 모든 $N$, $r$, 시행 법칙에 균일하다.
- **역할**: 균일성 덕에 inf와 truncation 극한이 교환된다(P12, [[g:truncation]]).
- **정의 위치**: `reduction:stability`, `reduction:free-stability`, `reduction:trial-stability`
- **물리 대응**: 없음.
