# 하나의 미분 규칙에서 두 전개 만들기

이 글의 목표는 삽입의 두 효과를 같은 계산으로 다루는 것이다. 하나는 root logarithm의 변화 log Y₀, 다른 하나는 old replica 중 anchor 하나의 삽입 인자를 상쇄한 기대값이다. 첫 것은 압력 비교에, 두 번째는 score 집중으로부터 tree 항등식을 꺼내는 데 쓰인다. 이 절에서는 물리적 상태 구조를 가정하지 않고 유한 확률 kernel만 다룬다.

## object: 무엇이 움직이는가

깊이 0부터 L까지 path를 둔다. 깊이 0인 root의 값은 고정한다. prefix가 주어지면 다음 변수를 확률 kernel K_d로 뽑는다. 0=m₀<m₁<⋯<m_L=1이다. 유한 tree T는 root를 공유하는 labeled path들의 집합이다. 서로 다른 자식은 그 prefix가 주어지면 독립이며 같은 kernel을 쓴다. leaf는 깊이 L의 위치다. 서로 다른 leaf에서 같은 값이 뽑혀도 위치는 다르다. 자식이 하나인 unary vertex도 실제 계산에서 모두 남긴다. 마지막 공통 vertex의 깊이가 split 깊이다. leaf를 일부 지워도 남은 tree의 법칙은 바뀌지 않는다.

E_T는 root가 주어진 tree 평균이다. Dᵃ는 path 함수 D를 leaf a의 path에서 본 값이다. root 평균을 더하면 𝔼로 쓴다. spin 적용에서 leaf a에 σᵃ∈{−1,1}ᴺ을 놓을 수 있고 multioverlap R_U=N⁻¹∑ᵢ∏_{a∈U}σᵢᵃ, R_∅=1이다. 아래 계산에는 spin이라는 특수성은 필요 없다.

움직이는 것은 양의 path 함수 A=1+∑ⱼtⱼDⱼ에 의해 재가중된 법칙이다. Dⱼ는 유계 실수 함수이며 t에 무관하다. 아래에서 위로

$$Y_L=A,\quad Y_{d-1}=(K_dY_d^{m_d})^{1/m_d},\qquad K_d^A=(Y_d/Y_{d-1})^{m_d}K_d.$$

K_dY_d^{m_d}=Y_{d-1}^{m_d}이므로 K_dᴬ도 확률 kernel이다. 위첨자 A의 평균은 이 바뀐 kernel을 사용한다. 원래 tilted kernel이 분배함수에서 왔다면 삽입 A는 그 iterated root logarithm을 log Y₀만큼 바꾼다. L≥2에서 일반적인 단일 분배함수 비의 로그로 바꾸어 읽지는 않는다.

## representation: 바뀐 기대값을 고정 법칙의 밀도로 쓰기

edge마다의 밀도 비를 곱하면

$$E_T^A[F]=E_T[F W_T(A)],\quad W_T(A)=\prod_{a\text{ leaf}}A^a\prod_{\beta\text{ internal}}Y_\beta^{\gamma_\beta},\quad \gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}<0.$$

깊이 d의 internal vertex β는 incoming edge에서 m_d를 받고 outgoing edge마다 −m_{d+1}을 받는다. root에는 incoming edge가 없어 m₀=0과 맞는다. leaf에는 m_L=1이 남는다. n_β는 **현재 tree**에서 β의 자식 수다. fresh path가 붙으면 이 값도 바뀐다. Y_β는 그 vertex의 prefix에서 본 Y_d다.

이 표현이 필요한 이유는 미분할 함수와 확률법칙이 동시에 바뀌는 문제를 고정 E_T 아래의 보통 곱 미분으로 바꾸기 위해서다. 밀도의 leaf 인자 Aᵃ가 integrand의 분모 Aᵃ로 지워진 leaf를 protected라고 하자. C가 그 집합이면

$$F_{T,C}[G](\boldsymbol t)=E_T^{A_{\boldsymbol t}}[G\prod_{a\in C}(A^a_{\boldsymbol t})^{-1}].$$

G는 현재 tree 변수의 유계 함수이며 t에 무관하다. 시작 문제의 G와, 미분 중 Dⱼ를 흡수한 새 G를 혼동하지 않는다. C는 여러 leaf여도 된다. anchor 문제는 C={a_*}인 경우다.

## rule: 한 번 미분하면 leaf 선택 또는 path 생성

power mean 한 단계를 미분하면

$$\partial_j\log Y_{d-1}=K_d^A\partial_j\log Y_d,\qquad \partial_j\log Y_L=D_j/A.$$

따라서 **first variation**은 ∂ⱼlog Y_β=Eᴬ[Dⱼ/A|β의 prefix]다. 이 조건부 평균은 β 아래 새 path 하나를 뽑는 연산이다.

밀도와 보호 분모를 함께 미분한다. ∂ⱼlog W=∑_a Dⱼᵃ/Aᵃ+∑_βγ_β∂ⱼlog Y_β. C에 속한 leaf 항은 (1/Aᵃ)의 미분과 상쇄된다. 남은 연산은 다음 두 개뿐이다.

| 선택 | 새 함수와 보호집합 | 계수 |
|---|---|---|
| a∉C인 현재 leaf a를 선택 | G에 Dⱼᵃ를 곱하고 C에 a 추가 | +1 |
| 현재 internal vertex β에서 fresh path 생성, 끝을 x라 함 | G에 Dⱼˣ를 곱하고 C에 x 추가 | γ_β |

두 경우 모두 전체 평균에는 새 보호집합의 1/A 분모들이 들어간다. 두 번째의 β 아래 path는 updated kernel Kᴬ로 독립 생성한다. G가 β의 다른 자식들에 의존해도, prefix 조건부 독립성과 leaf 제거의 일관성 때문에 정확하다. 선택된 leaf는 보호되므로 다시 직접 선택할 수 없다. 새 path는 β에서 새 자식으로 시작하고 이후 모든 깊이에서 새 vertex를 갖는다. anchor의 **path 위** internal vertex는 여전히 선택 가능하다.

이를 색 j=1,…,k마다 반복하고 t=0을 대입하면 모든 A,Y가 1이 된다. 그러므로 각 history의 끝에서 쓰는 것은 **원래 kernel**이다. 이때 G∏Dⱼ의 평균에 history 계수 곱 c_E를 곱해 더하면 mixed derivative다. color 순서를 바꾸어도 같은 mixed derivative가 나온다.

## derivation 1: anchor 전개

처음 C={a_*}, G=H로 시작한다. H는 유계 old-tree 함수이며 t에 무관하다. 사용되지 않은 old leaf는 첫째 선택을 하고, fresh leaf는 생기자마자 protected다. 그래서 재사용은 anchor 이외의 미사용 old leaf에만 허용된다. current tree는 미사용 old path도 포함한 모든 old path와 이미 생성한 path다. 결과는

$$\left.\partial_1\cdots\partial_kE_T^{A_{\boldsymbol t}}[H/A^{a_*}_{\boldsymbol t}]\right|_0=\sum_E c_E E_{T_E}[H\prod_jD_j^{a_j(E)}].$$

aⱼ(E)는 color j가 선택한 leaf, T_E는 끝 tree, c_E는 +1 또는 그 단계 γ의 곱이다. c_E는 확률이 아니다. 빈 history는 계수1이다. 동일 방향으로 t 하나를 쓰는 Taylor 계수는 이 k차 도함수를 k!로 나눈다. 서로 다른 tⱼ를 한 번씩 미분한 식에는 factorial이 없다.

**실행 예.** L=1이고 old leaf가 anchor a뿐이면 root의 γ는 −1이다. 첫 미분은 fresh leaf x의 −E[HD₁ˣ]. 둘째 미분에는 root 자식이 2개이므로 γ=−2, 모두 protected여서 fresh만 가능하다. 따라서 두-step 계수는 (−1)(−2)=2. H=D₁=D₂=1이면 Eᴬ[1/Aᵃ]=(1+t₁+t₂)⁻¹이므로 mixed derivative2와 맞는다. 둘째 단계에 old tree의 γ=−1을 쓰면 틀린다.

## derivation 2: log 전개

first variation에서 ∂ₜlog Y₀=Eᴬ[D/A]는 path 하나의 끝을 protected로 둔 기대값이다. 이제 **모든 leaf가 protected**라서 매번 fresh 생성만 남는다. tree의 leaf 수를 n이라 하면 edge 지수의 망원 합으로 ∑_β(−γ_β)=n. 따라서 fresh 선택 확률을 (−γ_β)/n으로 정할 수 있다. path 하나에서 이 선택을 반복해 k leaf를 만든 법칙이 Q_k다. tree 모양은 path 변수와 별도로 먼저 뽑는다.

각 fresh 단계의 계수는 −n·확률이므로 k−1번의 곱은 (−1)^{k−1}(k−1)!·history 확률이다. 그러므로

$$\left.\partial_t^k\log Y_0\right|_0=(-1)^{k-1}(k-1)!\,\mathbb E_{Q_k}E_T\prod_{a=1}^kD^a,$$
$$\log Y_0=\sum_{k\ge1}\frac{(-1)^{k-1}t^k}{k}\,\mathbb E_{Q_k}E_T\prod_{a=1}^kD^a.$$

Q₂에서 split 깊이 d의 확률은 m_{d+1}−m_d이며 균등 격자일 때만 깊이에 균일하다. L=1에서는 root에서 모두 갈라지는 모양만 존재하고 E_T∏Dᵃ=(ED)^k이어서 보통 log(1+tED) 급수다. L=2,m₁=m에서 ν(prefix)=K₂D라 쓰면 2차 계수는 −[m(K₁ν)²+(1−m)K₁ν²]/2다. 이는 Q₂의 root split과 depth1 split을 더한 것이다.

## 어디까지 정당한가

root 고정의 조건부 항등식이며 임의의 유한 확률 kernel 열에 대해 성립한다. A는 실수 근방에서 위로 유계이고 0에서 떨어져 있어야 한다. bounded Dⱼ에 대해 ∑|tⱼ|∥Dⱼ∥∞<1에서 해석적이다. 작은 닫힌 영역의 미분 경계는 **고정 depth·exponent·tree 크기·D bounds에서 kernel에 균일**하다. 이 사실만으로 L에 균일하지 않다. log 급수는 |t|∥D∥∞<1에서 성립하고 |t|∥D∥∞≤c<1이면 K차 나머지≤∑_{k>K}c^k/k다.

원래 모형에 없던 변수는 독립 prior kernel로 path를 넓혀 쓸 수 있고 추가 root 변수는 quenched로 둔다. replica 수 n→0이나 무한 cascade는 쓰지 않는다. 물리 Gibbs 측도의 pure-state 구조와 위 보조 tree의 동일시는 여기서 증명되지 않는다.

근거: trees.tex의 tree:Y-recursion, tree:density, tree:first-variation, protected-leaf 회계, tree:log-expansion, tree:extension-expansion. 같은 유한 tree 진술의 재배열이며 본문에 적은 두 전개는 exact, 해석 경계의 상세 증명은 blackbox다.

## 공통 부록: 모양별 합, 계수 한계, 사용 경계

다음은 세 후보가 공통으로 받는 진술이며 여기서는 증명을 블랙박스로 둔다. anchor와 color가 만드는 split 모양 S를 처방하되 미사용 old path를 추가로 구별하지 않는다. Br(S)는 branching vertex 집합, a_v는 S에서의 자식 수, d_v는 깊이다. 모양 S를 갖는 history의 signed 계수 총합은 old tree와 무관하게

$$\kappa(S)=\prod_{v\in\mathrm{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1}).$$

uniform mesh m_d=d/L, δ=1/L에서 처방한 branching vertex 중 깊이가 old tree의 어느 branching 깊이와도 같지 않은 것을 b_sep개 고른다. (전부 또는 일부.) old leaf 수 q,color 수 k에 대해

$$\sum_{E\text{ 허용}}|c_E|\le C_{q,k}\delta^{b_{\rm sep}}.$$

고른 vertex의 κ 인자 곱을 J_sep라 하면 그 모든 vertex에서 m_{d_v}≥η>0이라는 조건 아래

$$\frac{\sum_{E\text{ 허용}}|c_E|}{|J_{\rm sep}|}\le C_{q,k,\eta}$$

라는 L-uniform bound를 쓴다. |J_sep| 자체는 δ^{b_sep} 크기로 작아지며 L-uniform 양의 하한이 없다. η 조건 없이는 고차 branching의 j≥2 인자가 추가로 작아질 수 있다. 이 계수 한계는 uniform mesh 전용이며, 미분·log 전개와 κ 항등식은 일반 증가 mesh에서 성립한다. signed 합과 절댓값 합은 다르다. 예컨대 old 두 path가 depth s에서 갈라질 때 color도 anchor와 s에서 갈라지게 하면 signed 합 −δ이지만 절댓값 합 2+δ이다. 목표 split을 s+1<L로 미루면 허용 fresh 하나의 계수 −δ만 남아 절댓값 합 δ다.

P7은 별도 입력인 선택된 수열의 score 집중과 tree 모멘트 수렴, Palm 변환·해석성·polarization·mark selector를 이 미분 전개와 결합해 얻는 prescribed-tree 항등식이다. 이 문서는 그 전체 증명을 재구성하지 않는다. P7의 극한은 고정 L·tree·제약에서 선택된 수열을 따라 N→∞이며 L-uniform 수렴률이 없다. 여기의 유한 보조 tree 계산으로 물리적 Gibbs 측도의 pure-state/RPC 구조나 overlap 극한값이 증명되는 것은 아니다.

근거(열람 불필요): trees.tex tree:reference-total, tree:charging, perturbations.tex pert:tree-identity. 문서 바깥 링크를 열지 않아도 이 시험의 모든 질문을 풀 수 있게 제공한 범위다.
