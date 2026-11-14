### 6.1 replica tree와 log 전개 (P6)

**목적.** spin weight에 인자 $A$ 를 곱했을 때 root logarithm이 얼마나 바뀌는지를, 삽입 전의 법칙으로 뽑은 replica tree 위의 평균으로 쓴다. 수 2의 증분과 수 6의 비교가 이 꼴의 양이고, 6.2의 전개가 같은 미분 규칙에서 나온다.

**설정(6절 전체가 쓴다).**

- **수와 path.** $0=m_0<m_1<\cdots<m_{L-1}<m_L=1$ 을 고정한다. 하한에서는 $m_d=d/L$, $\delta=1/L$ 이지만([[g:grid]]) 6.1과 6.2의 ①, ②는 일반 격자에서 성립한다. path는 깊이 $0,\ldots,L$ 마다 변수를 하나씩 갖는다. 깊이 0이 [[g:root|root]], 깊이 $L$ 이 spin 배치다. 깊이 $d$ 의 변수는 그 앞 prefix가 주어지면 확률 kernel $K_d$ 로 뽑는다([[g:hierarchy]]).
- **tree.** [[g:prescribed-tree|prescribed tree]] $\mathcal T$ 는 root를 공유하고 깊이 $L$ 에서 끝나는 유한 개의 labeled path다. 각 path는 깊이 $0,\ldots,L$ 마다 vertex를 하나씩 갖고, 두 path는 어느 깊이까지 vertex를 공유하다가 갈라진다. 마지막 공통 vertex의 깊이가 그 둘의 **split 깊이**다. 깊이 $L$ 의 vertex가 leaf이고 leaf에 놓인 spin 배치가 [[g:replica|replica]]다. **내부 vertex**는 깊이 $0,\ldots,L-1$ 의 모든 vertex이며, 자식이 하나뿐인(unary) vertex도 포함한다. 자식이 둘 이상이면 branching vertex라 부른다. ([[g:topology]]가 unary vertex를 지우는 것은 모양을 적을 때뿐이다.)
- **tree 표본 규칙.** 각 vertex에서 서로 다른 자식은 그 prefix가 주어지면 같은 kernel로 독립으로 뽑힌다. leaf 일부를 지워도 남은 tree의 법칙은 바뀌지 않는다. $E_{\mathcal T}$ 는 root가 주어졌을 때 이 규칙으로 $\mathcal T$ 를 뽑는 기대값이고, $\mathbb E$ 는 root 평균까지 포함한다. path 함수 $D$ 를 leaf $a$ 의 path에서 본 값을 $D^a$ 로 쓴다.
- **multioverlap.** replica 집합 $U$ 에 대해 $R_U=\frac1N\sum_i\prod_{a\in U}\sigma_i^a$, $R_\varnothing=1$ 이다([[g:multioverlap]]). $\lvert U\rvert=2$ 가 보통의 overlap, $\lvert U\rvert=1$ 이 자화다. 희석 모형에서는 pair overlap만으로 부족해서 모든 $R_U$ 를 쓴다. (원문과 rules 머리말은 $R_S$ 로 쓴다. 이 절에서 $S$ 는 6.2 ②의 모양에 남겨 둔다.)
- **삽입.** 양의 path 함수 $A$ 를 spin weight에 곱하는 것이 [[g:insertion|삽입]]이다. 아래에서 위로
$$Y_L=A,\qquad Y_{d-1}=\bigl(K_dY_d^{m_d}\bigr)^{1/m_d}\quad(d=L,\ldots,1)$$
로 정하면, 삽입은 root logarithm을 정확히 $\log Y_0$ 만큼 바꾸고 kernel을 $K_d^A=(Y_d/Y_{d-1})^{m_d}K_d$ 로 바꾼다. **$E^A_{\mathcal T}$ 는 바뀐 kernel $K^A_d$ 로 뽑는 tree 기대값**이고, 위첨자가 없는 $E_{\mathcal T}$ 는 원래 kernel $K_d$ 로 뽑는 기대값이다. 둘의 관계는 $E^A_{\mathcal T}[\,\cdot\,]=E_{\mathcal T}[\,\cdot\;W_{\mathcal T}(A)]$ 이고 밀도는
$$W_{\mathcal T}(A)=\prod_{a\in\text{leaf}}A^a\prod_{\beta\in\text{내부 vertex}}Y_\beta^{\gamma_\beta},\qquad\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$$
이다. $d_\beta$ 는 $\beta$ 의 깊이, $n_\beta$ 는 $\mathcal T$ 에서 $\beta$ 의 자식 수, $Y_\beta$ 는 $\beta$ 의 prefix에서 본 $Y_{d_\beta}$ 다. $n_\beta\ge1$ 이고 $m_d<m_{d+1}$ 이므로 [[g:tree-coefficient|tree 계수]] $\gamma_\beta$ 는 항상 음수다.

**주 식 (P6).** 유계 실수 path 함수 $D$ 와 실수 $t$ 로 $A=1+tD$ 를 삽입하면
$$\log Y_0=\sum_{k\ge1}\frac{(-1)^{k-1}t^k}{k}\;\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a,\qquad\lvert t\rvert\,\lVert D\rVert_\infty<1 .$$
좌변은 삽입이 root logarithm에 준 변화다. 우변의 $k$ 차 항은 leaf가 $k$ 개인 tree $\mathcal T$ 를 법칙 $Q_k$ 로 고르고, 그 tree를 **삽입 전의** kernel로 뽑아, $k$ 개 replica에서 본 $D$ 의 곱을 평균한 것이다.

**tree 법칙 $Q_k$.** path 하나에서 시작한다. 현재 tree $\mathcal T$ 의 leaf 수를 $\lvert\mathcal T\rvert$ 라 할 때 내부 vertex $\beta$ 를 확률
$$\frac{n_\beta m_{d_\beta+1}-m_{d_\beta}}{\lvert\mathcal T\rvert}=\frac{-\gamma_\beta}{\lvert\mathcal T\rvert}$$
로 골라 거기에 새 자식을 만들고 깊이 $L$ 까지 새 path를 잇는다. leaf가 $k$ 개가 되면 멈춘다. 확률인 것은 $-\gamma_\beta/\lvert\mathcal T\rvert$ 이고 $\gamma_\beta$ 자체는 음수다. 합이 1인 것은 모든 tree에서 $\sum_\beta(-\gamma_\beta)=\lvert\mathcal T\rvert$ 이기 때문이다([[tree:telescoping]]; 원문은 leaf 수를 $n$ 으로 쓴다). 각 vertex는 자기 깊이의 $m$ 을 한 번 빼고 자식마다 다음 깊이의 $m$ 을 더하므로 합이 root의 $-m_0=0$ 과 leaf마다의 $m_L=1$ 만 남긴다. (산수) 예를 들어 $Q_2$ 에서 두 path가 깊이 $d$ 에서 갈라질 확률은 $m_{d+1}-m_d$ 이고, 균등 격자에서는 깊이 $0,\ldots,L-1$ 에 균일하다([[g:tree-law]]).

**최소 예.** $L=1$ 이면 kernel은 Gibbs 평균 $\langle\cdot\rangle$ 하나이고 $Y_0=\langle1+tD\rangle$ 이다. $\log(1+t\langle D\rangle)=t\langle D\rangle-\tfrac{t^2}2\langle D\rangle^2+\cdots$ 의 $k$ 차 항은 독립 replica $k$ 개의 $\langle D\rangle^k$ 이고, 실제로 $L=1$ 에서 $Q_k$ 는 root에서 모두 갈라지는 tree 하나에 확률 1을 준다. $L=2$, $m_1=m$ 에서는 깊이 1의 변수가 주어진 Gibbs 평균을 $\langle\cdot\rangle_1$, 깊이 1 변수의 평균을 $K_1$ 이라 할 때 $Y_1=1+t\langle D\rangle_1$, $Y_0=(K_1Y_1^m)^{1/m}$ 이고, 전개하면
$$\log Y_0=t\,K_1\langle D\rangle_1-\frac{t^2}{2}\Bigl[m\,(K_1\langle D\rangle_1)^2+(1-m)\,K_1\langle D\rangle_1^2\Bigr]+O(t^3)$$
이다. 대괄호 안이 $\mathbb E_{Q_2}E_{\mathcal T}[D^1D^2]$ 다: 확률 $m_1-m_0=m$ 으로 깊이 0에서 갈라져 깊이 1 변수까지 독립이고, 확률 $m_2-m_1=1-m$ 으로 깊이 1에서 갈라져 깊이 1 변수를 공유한다. (산수)

**성립 범위와 단서.**
- root가 주어진 조건부 항등식이다. $A$ 는 root가 주어졌을 때 위로 유계이고 0에서 떨어져 있다고 둔다($A=1+tD$, $\lvert t\rvert\lVert D\rVert_\infty<1$ 이면 그렇다). 임의의 유한 확률 kernel 열에서 성립하며, kernel이 분배함수의 tilted kernel일 때 $\log Y_0$ 가 root logarithm의 변화가 된다.
- 수렴 영역은 $\lvert t\rvert\lVert D\rVert_\infty<1$ 이다. $\lvert t\rvert\lVert D\rVert_\infty\le c<1$ 이면 $K$ 차까지 자른 나머지는 $\sum_{k>K}c^k/k$ 이하다([[tree:log-expansion]]).
- 삽입은 원래 모형에 없던 변수를 써도 된다. 그 변수의 독립 prior kernel로 path를 넓힌 뒤 적용한다([[x:tree-extra-variables]]). 6.3의 새 site와 mark가 이 경우다.
- replica 수를 0으로 보내는 해석적 연속을 쓰지 않는다. 계층은 무한 계층이 아니라 깊이 $L$ 의 유한 kernel 열이다.
- $L\ge2$ 에서 $\log Y_0$ 는 보통의 분배함수 비의 로그가 아니다(4.3절).

### 6.2 anchor를 상쇄한 전개와 계수 한계 (P6′)

**목적.** 6.3에서 score 집중을 tree 언어로 옮기면 "old tree의 leaf 하나(anchor)에서만 삽입 인자가 상쇄된, 바뀐 법칙의 tree 기대값"이 나온다. P6′ 은 이 양을 삽입 크기로 미분한 값을 **원래 법칙**의 tree 기대값들의 유한 합으로 쓴다(①). 그 합의 계수는 부호가 섞이므로, 부호 있는 합(②)과 절댓값 합(③)을 따로 계산해 둔다. ①은 6.3이, ②와 ③은 수 5가 쓴다.

**받는 것 / 넘기는 것.** 받는 것은 6.1의 설정과 밀도 $W_{\mathcal T}$ 의 미분 규칙뿐이고 모형은 들어오지 않는다. 넘기는 것은 ① 전개 식과 그 좌변의 균일 해석적 경계, ② 모양별 총합 $\kappa(S)$, ③ 계수 한계다.

#### ① 전개

기호(주 식보다 먼저):
- **old tree** $\mathcal T$ 는 삽입 전에 주어진 tree이고, 그 path와 leaf를 old path, old leaf라 부른다. [[g:anchor|anchor]] $a_*$ 는 그 가운데 구별해 둔 leaf 하나다.
- $G$ 는 old tree 위 변수의 유계 함수이고 $\boldsymbol t$ 에 의존하지 않는다. lemma `tree:extension-expansion` 과 카드에서는 이것을 $H$ 로 쓴다. 원문의 그 증명(trees.tex 180–202, 299–301)에 나오는 $G$ 는 미분할 때마다 $D_j/A$ 를 흡수해 가는 함수로, 처음 값이 이 $H$ 다. 6.3에서는 $G$ 가 시험함수 $f$ 에 anchor의 mark와 spin 인자를 곱한 것이다.
- **color.** 새로 붙는 replica에 붙인 번호 $1,\ldots,k$ 다. color $j$ 는 방향 $D_j$ 와 짝이다.
- $E$ 는 아래에서 정의하는 extension history, $c_E$ 는 그 계수, $\mathcal T_E$ 는 그 history가 만든 마지막 tree, $a_j(E)$ 는 그 tree에서 color $j$ 를 받은 leaf다. 글자 $E$ 가 history와 기대값에 함께 쓰이지만(원문 표기), 기대값에는 늘 tree 첨자가 붙는다($E_{\mathcal T}$, $E^A_{\mathcal T}$). $\mathbb E$ 는 root 평균까지 포함한 기대값, $\mathfrak E$ 는 6.3의 history 모임이다.

**주 식 (P6′).** old tree $\mathcal T$, anchor $a_*$, $G$, 유계 실수 path 함수 $D_1,\ldots,D_k$ 에 대해 $A_{\boldsymbol t}=1+\sum_{j=1}^kt_jD_j$ 를 삽입하면
$$\partial_{t_1}\cdots\partial_{t_k}\,E^{A_{\boldsymbol t}}_{\mathcal T}\!\left[\frac{G}{A_{\boldsymbol t}^{a_*}}\right]\Bigg\rvert_{\boldsymbol t=0}=\sum_{E}c_E\;E_{\mathcal T_E}\!\Bigl[G\prod_{j=1}^kD_j^{a_j(E)}\Bigr].$$

- **좌변.** $A_{\boldsymbol t}$ 의 삽입으로 **바뀐 법칙** $E^{A_{\boldsymbol t}}_{\mathcal T}$ 아래에서 $G/A^{a_*}_{\boldsymbol t}$ 를 평균하고, 삽입 크기 $t_1,\ldots,t_k$ 로 한 번씩 미분해 $\boldsymbol t=0$ 에서 본 값이다. 6.1의 밀도로 쓰면 $E_{\mathcal T}\bigl[G\prod_{a\ne a_*}A^a\prod_\beta Y_\beta^{\gamma_\beta}\bigr]$ 이다. 분모 $A^{a_*}$ 가 밀도의 leaf 인자 가운데 anchor의 것 하나를 지웠다.
- **우변.** [[g:extension-history|extension history]] $E$ 에 대한 유한 합이다. 각 항은 계수 $c_E$ 에, $\mathcal T_E$ 를 **삽입이 없는 원래 kernel**로 뽑아 $G$ 와 "leaf $a_j(E)$ 에서 본 $D_j$"들의 곱을 평균한 값을 곱한 것이다. $\boldsymbol t=0$ 에서는 $A$ 와 $Y$ 가 모두 1이라 삽입의 흔적이 법칙에 남지 않는다.

**extension history와 $c_E$.** old tree에서 시작해 color $1,\ldots,k$ 를 차례로 leaf에 준다. color마다 다음 둘 가운데 하나를 고른다.

| 선택 | 하는 일 | 계수 |
|---|---|---|
| (i) 재사용 | anchor가 아니고 아직 color를 받지 않은 old leaf 하나에 이 color를 준다 | $+1$ |
| (ii) fresh path | 현재 tree의 내부 vertex $\beta$ 하나를 골라 거기에 새 자식을 만들고 깊이 $L$ 까지 새 vertex로 path를 잇는다. 그 끝의 새 leaf가 이 color를 받는다 | $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}<0$ |

- **현재 tree**는 old path 전부(color를 받지 않은 것과 anchor 포함)와 그때까지 붙인 fresh path 전부다. (ii)의 $\beta$ 는 그 어느 path 위의 내부 vertex든 될 수 있다. anchor의 path 위 vertex도 된다.
- **$n_\beta$ 는 그 걸음을 하기 직전 현재 tree에서 $\beta$ 가 가진 자식 수**다. 6.1의 $\gamma_\beta$ 를 그 걸음의 현재 tree에 대해 쓴 것이므로, 6.1의 정의("$\mathcal T$ 에서의 자식 수")를 그 tree에 적용한 값이다. 앞 걸음의 fresh path가 $\beta$ 에 자식을 더했으면 그것도 센다(아래 예 3).
- color를 받은 leaf는 다시 고를 수 없고, anchor leaf는 처음부터 고를 수 없다.
- $c_E$ 는 걸음마다의 계수의 곱이다. $k=0$ 이면 빈 history 하나뿐이고 계수는 1이다. (i)은 $+1$, (ii)는 음수라서 $c_E$ 는 **부호가 섞인다**. 확률 가중치가 아니다.

**규칙이 나오는 곳 (P6의 미분 규칙).** **[[g:protected-leaf|protected leaf]]** 는 밀도의 leaf 인자 $A^a$ 가 분모 $A^a$ 로 상쇄된 leaf다. 6.1의 밀도의 로그를 미분하면 $\partial_{t_j}\log W_{\mathcal T}=\sum_{\text{leaf }a}D_j^a/A^a+\sum_\beta\gamma_\beta\,\partial_{t_j}\log Y_\beta$ 이다. leaf 항이 선택 (i)이고, 내부 vertex 항이 선택 (ii)다: $\partial_{t_j}\log Y_\beta$ 는 $\beta$ 아래로 새 path 하나를 뽑아 그 끝에서 $D_j/A$ 를 본 기대값이기 때문이다([[tree:first-variation]]). protected leaf에서는 이 leaf 항이 분모의 미분과 정확히 상쇄되어 남지 않는다. anchor는 처음부터 protected이고, 한 번 고른 leaf와 새로 붙은 leaf도 $D_j/A$ 를 받으면서 protected가 된다. 그래서 anchor와 이미 쓴 leaf는 선택지에서 빠진다. old leaf 없이 path 하나에서 시작하면 선택 (ii)만 남고, 그 계수의 절댓값을 정규화한 것이 6.1의 $Q_k$ 의 확률이다([[x:tree-differentiation-rule]]).

**계산 예 1: old leaf 둘, $k=1$.** old tree가 anchor $a_*$ 와 다른 replica $a'$ 둘이고 깊이 $s$($0\le s\le L-1$)에서 갈라진다. $G=1$, $D=1$ 로 둔다. 내부 vertex는 공통 줄기의 깊이 $0,\ldots,s$ 와 두 가지 각각의 깊이 $s+1,\ldots,L-1$ 에 있다. history는 걸음이 하나다.

| history | 개수 | 계수 |
|---|---|---|
| $a'$ 을 재사용 | 1 | $+1$ |
| 공통 줄기의 깊이 $d<s$ vertex(자식 1개)에서 fresh | $s$ | $m_d-m_{d+1}$ |
| 갈라지는 깊이 $s$ vertex(자식 2개)에서 fresh | 1 | $m_s-2m_{s+1}$ |
| anchor 가지의 깊이 $\ell>s$ vertex(자식 1개)에서 fresh | $L-1-s$ | $m_\ell-m_{\ell+1}$ |
| $a'$ 가지의 깊이 $\ell>s$ vertex(자식 1개)에서 fresh | $L-1-s$ | $m_\ell-m_{\ell+1}$ |

모두 $2L-s$ 개다. $G=D=1$ 이라 각 항의 기대값은 1이고, 우변은 계수의 합이다:
$$1+(m_0-m_s)+(m_s-2m_{s+1})+2(m_{s+1}-m_L)=1+m_0-2m_L=-1 .$$
좌변을 따로 계산한다. $A=1+t$ 는 상수이므로 모든 깊이에서 $Y_d=1+t$ 이고 $K^A_d=K_d$, 곧 법칙이 바뀌지 않는다. 그래서 $E^A_{\mathcal T}[1/A^{a_*}]=(1+t)^{-1}$ 이고 $t=0$ 에서의 미분은 $-1$ 이다. 두 값이 맞는다. (산수)

**계산 예 2: $L=1$, anchor 하나.** old tree가 anchor뿐이고 $k=1$, $G=1$, $D$ 는 일반이다. 좌변은 $\langle A\cdot A^{-1}\rangle/\langle A\rangle=1/(1+t\langle D\rangle)$ 의 미분 $-\langle D\rangle$ 이다. 우변은 재사용할 old leaf가 없으므로 root(자식 1개)에서의 fresh 하나뿐이고, 계수 $m_0-m_1=-1$ 에 새 replica의 $\langle D\rangle$ 를 곱한 $-\langle D\rangle$ 다. anchor 자신은 항을 내지 않는다. (산수)

**계산 예 3: $L=1$, $k=2$ — 앞 걸음이 $n_\beta$ 를 바꾼다.** $G=1$, $D_1=D_2=1$ 이다. $L=1$ 이면 내부 vertex는 root 하나이고 $m_0=0$, $m_1=1$ 이라 root에서의 fresh 계수는 $-n_{\rm root}$ 다. 좌변은 예 1과 같은 이유로 법칙이 바뀌지 않아 $\partial_{t_1}\partial_{t_2}(1+t_1+t_2)^{-1}\rvert_0=2(1+t_1+t_2)^{-3}\rvert_0=2$ 다.
- old tree가 anchor 하나: 재사용할 leaf가 없다. 첫 걸음은 root(자식 1개: anchor)에서 fresh, 계수 $m_0-m_1=-1$. 이 fresh path가 root에 자식을 더해, 둘째 걸음에서는 root의 자식이 2개이고 계수는 $m_0-2m_1=-2$ 다. history는 하나, $c_E=(-1)(-2)=2$.
- old tree가 anchor와 $a'$(root에서 갈라짐): 첫 걸음은 $a'$ 재사용($+1$) 또는 root(자식 2개)에서 fresh($-2$). 재사용 뒤 둘째 걸음은 root(자식 2개) fresh뿐이라 $(+1)(-2)$. fresh 뒤 둘째 걸음은 $a'$ 재사용 $(-2)(+1)$ 또는 root(자식 3개) fresh $(-2)(-3)$. 합 $-2-2+6=2$.

두 경우 모두 좌변 2와 맞는다. 둘째 걸음의 $n_{\rm root}$ 를 old tree에서 세면(각각 1, 2) 합이 $1$, $-2-2+4=0$ 이 되어 틀린다. (산수)

**factorial.** 위 식은 color의 순서를 어떻게 정해도 성립하고, 좌변의 혼합 미분에는 factorial이 붙지 않는다. 모든 방향이 같을 때($D_j=D$, $A=1+tD$) $t^k$ 의 Taylor 계수는 $k$ 차 미분을 $k!$ 로 나눈 것이므로 우변$/k!$ 이다. 두 말은 같은 사실이다.

