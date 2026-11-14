# 부호를 보존하는 random tree 연산으로 두 전개 계산하기

목표는 삽입 A의 효과 두 가지를 하나의 random tree 연산으로 표현하는 것이다. log Y₀는 root logarithm의 변화이며 압력 비교에 쓰인다. Eᴬ_T[H/A^{a_*}]는 old tree의 anchor에서 삽입 인자 하나가 상쇄된 평균이며 score 집중으로 tree 항등식을 얻는 데 쓰인다. 아래 random 연산은 signed coefficient를 양의 확률로 잘못 읽지 않으면서 기대값으로 계산하는 **유한 importance sampling representation**이다. RPC와의 동일시를 사용하지 않는다.

## object와 원래 확률법칙

깊이0 root를 고정하고 depth d의 변수는 앞 prefix가 주어질 때 확률 kernel K_d로 뽑는다. 0=m₀<m₁<⋯<m_L=1. tree T는 root를 공유하는 labeled path 여러 개로 이루어진다. 각 path는 depth0,…,L에 vertex 하나씩 가진다. leaf는 depth L의 위치이며 같은 값이 뽑혀도 서로 다른 위치는 별개다. 서로 다른 자식들은 prefix 조건부로 독립이다. leaf 일부를 지워도 나머지 tree 법칙이 그대로다. unary vertex도 계산에 모두 포함한다. 두 path의 마지막 공통 vertex depth가 split 깊이다.

E_T는 root 고정 평균, 𝔼는 root까지 평균한다. Dᵃ는 D를 leaf a의 path에서 본 값이다. spin 적용에서 multioverlap R_U=N⁻¹∑ᵢ∏_{a∈U}σᵢᵃ, R_∅=1이다. 이 계산은 spin이나 상호작용 형태를 쓰지 않는다.

bounded real path 함수 Dⱼ를 고정하고 A=1+∑ⱼtⱼDⱼ를 삽입한다. 바뀐 kernel과 backward 함수는

$$Y_L=A,\quad Y_{d-1}=(K_dY_d^{m_d})^{1/m_d},\quad K_d^A=(Y_d/Y_{d-1})^{m_d}K_d.$$

재귀식으로 K_dᴬ도 확률 kernel이다. 분배함수에서 얻은 tilted K라면 root logarithm 변화는 log Y₀다. L≥2에서 보통의 단일 분배함수 비 로그라고 단순화하지 않는다. edge 밀도를 곱하면

$$E_T^A[F]=E_T[FW_T(A)],\quad W_T(A)=\prod_{a\text{ leaf}}A^a\prod_{\beta\text{ internal}}Y_\beta^{\gamma_\beta},\quad \gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}<0.$$

n_β는 **그 단계의 현재 tree에서** β의 자식 수다. incoming edge의 m_d와 outgoing edge들의 −m_{d+1}을 합친 지수다. root는 m₀=0, leaf는 m_L=1이다. 모든 internal vertex에서 망원 합하면 ∑_β(−γ_β)=n, n은 현재 leaf 수다. unary vertex도 m_{d+1}−m_d>0을 내므로 없애면 이 항등식이 깨진다.

## 미분을 선택지 목록으로 바꾸기

G는 t에 무관한 유계 current-tree 함수다. W의 leaf Aᵃ를 integrand의 1/Aᵃ로 상쇄한 leaf를 protected라고 하고 그 집합을 C라 쓴다. 다루는 양은 F_{T,C}[G]=Eᴬ_T[G∏_{a∈C}(Aᵃ)⁻¹]다. 첫 변분

$$\partial_j\log Y_\beta=E^A[D_j/A\mid\beta\text{ prefix}]$$

은 β 아래 fresh path 하나를 뽑는 연산이다. power mean 미분 ∂log Y_{d−1}=K_dᴬ∂log Y_d와 말단 ∂log A=Dⱼ/A로부터 나온다. W와 보호 분모를 함께 미분하면 protected leaf의 직접 leaf 항은 정확히 상쇄된다. 나머지는

1. unprotected leaf a 하나를 택하고 G에 Dⱼᵃ를 곱한다. a를 protected로 바꾸며 계수+1.
2. current internal vertex β를 택해 새 child와 depth L까지 전부 fresh인 path를 붙인다. G에 그 끝 x에서 본 Dⱼˣ를 곱한다. x는 protected이며 계수γ_β<0.

각 resulting 기대값에는 모든 protected leaf의 1/A가 들어간다. 추가 path는 Kᴬ로 뽑는다. G가 β의 다른 자식들에 의존해도 prefix 조건부 독립과 tree projectivity 때문에 정확하다. 처음 anchor만 protected라면 unprotected는 미사용 old leaf들뿐이다. anchor의 path 위 internal vertex는 여전히 선택 가능하다. old path는 미사용 것도 지우지 않는다.

## representation: 양의 proposal과 signed weight를 분리하기

위 선택지들의 coefficient를 w(z)라 하자. unprotected leaf 수를 u라 하면 절댓값 총합은

$$M(T,C)=\sum_z|w(z)|=u+\sum_\beta(-\gamma_\beta)=u+n.$$

tree에 leaf가 하나 이상이므로 M>0. **한 미분 step을 random 연산**으로 만들 수 있다.

| event z | 선택 확률 p(z) | signed multiplier w(z)/p(z) |
|---|---|---|
| 특정 unprotected leaf a 선택 | 1/(n+u) | +(n+u) |
| 특정 internal β에서 fresh path 생성 | (−γ_β)/(n+u) | −(n+u) |

확률은 모두 양이고 합1이다. 그러나 최종 weight는 부호가 있다. 조건부 평균에서 p(z)·[w(z)/p(z)]=w(z)이므로 모든 event를 더한 정확한 미분 연산을 되찾는다. 이를 k회 반복해 event history h를 뽑고, 각 단계 multiplier의 곱 B_h를 기록한다. 매번 n,u,n_β를 갱신한다. old 선택이면 n은 같고 u가1 줄며, fresh면 n이1 늘고 u는 같다. t=0에서는 A=Y=1이므로 마지막 tree의 변수는 **원래 kernel**로 뽑는다. 그 결과

$$\left.\partial_1\cdots\partial_k F_{T,C}[G]\right|_0=\mathbb E_{\text{proposal }h}\left[B_h\ E_{T_h}\{G\prod_jD_j^{a_j(h)}\}\right].$$

event proposal의 난수와 tree 위 path 변수의 난수를 구별한다. 이는 정확한 algebraic expectation representation이며 실제 Monte Carlo를 실행해야 항등식이 성립하는 것이 아니다. 모든 history를 열거해도 같다. 처음 C={a_*}, G=H이고 H가 t-independent old-tree 함수이면 이 식이 canceled-anchor 전개다. history의 원래 signed coefficient c_h는 각 +1/γ의 곱이다. proposal 확률 P(h)와의 관계는 P(h)B_h=c_h이며 c_h 자체는 확률이 아니다. 혼합 미분에는 factorial이 없다. 동일 방향 t의 Taylor 계수에는 k!로 나눈다.

**실행 예.** L=1 old tree가 anchor 하나라면 n=1,u=0. 첫 event는 root fresh밖에 없어 확률1,multiplier−1. 다음 단계 n=2,u=0이므로 역시 root fresh, multiplier−2. 두-step B=2이고 D₁=D₂=H=1이면 (1+t₁+t₂)⁻¹의 mixed derivative2와 맞는다. 다음 step에서 n을 처음 값으로 두면 이 검산에 실패한다.

이 sampler를 '효율적인 수치 방법'이라고 주장하지 않는다. 고정 q=초기 leaf 수, k=미분 횟수에서 n≤q+k, u≤q라서 |B_h|≤(2q+k)^k이고 Dⱼ,G도 유계이므로 고정 크기의 estimator는 유한한 second moment를 가진다. 이 bound는 k나 q에 빠르게 커지고 signed cancellation에 따른 상대분산은 클 수 있다. 또한 제약 history만을 더할 때 proposal을 몰래 그 부분에 재정규화해서 같은 값이라 하면 안 된다. 원래 proposal 아래 event indicator를 넣거나 바꾼 proposal의 확률 비를 weight에 보정해야 한다. 상쇄가 크면 signed 총합만으로 절댓값 오차를 제어하지 못한다.

## log 전개는 이 random 연산의 all-protected 경우

first variation은 ∂ₜlog Y₀=Eᴬ[D/A]. path 하나에서 이미 말단이 protected다. 이후에는 u=0인 상태만 거치므로 확률은 (−γ_β)/n, multiplier는 항상 −n이다. path 하나에서 이 확률로 k leaf까지 tree를 키운 법칙이 Q_k다. k차 log 도함수에는 k−1번 연산이 들어가므로

$$B_h=(-1)^{k-1}(k-1)!,\qquad \left.\partial_t^k\log Y_0\right|_0=(-1)^{k-1}(k-1)!\mathbb E_{Q_k}E_T\prod_aD^a,$$
$$\log Y_0=\sum_{k\ge1}\frac{(-1)^{k-1}t^k}{k}\mathbb E_{Q_k}E_T\prod_aD^a.$$

Q₂에서 split depth d의 확률은 m_{d+1}−m_d이며 균등 격자일 때만 depth에 균일하다. L=1이면 Q_k의 topology는 root에서 전부 갈라지는 하나뿐이므로 log(1+tED) 급수다. L=2,m₁=m, ν=K₂D라 하면 t² 계수는 −[m(K₁ν)²+(1−m)K₁ν²]/2다. 두 항은 root split과 depth1 split이다. 일반 canceled-anchor 문제에는 u>0인 old 선택이 있어 Q_k의 fresh 확률만으로는 계산을 재현하지 못한다.

## 조건과 근거

실수 근방에서 A는 위로 유계이고 0에서 떨어져 있다고 한다. bounded Dⱼ에 대해 ∑|tⱼ|∥Dⱼ∥∞<1에서 해석성이 있다. 작은 닫힌 영역의 미분 경계는 **고정 L·exponent·tree 크기·D bounds에서 kernel에 균일**하다. depth에도 균일하다는 뜻은 아니다. log 급수는 |t|∥D∥∞<1에서 수렴하며 |t|∥D∥∞≤c<1이면 K차 나머지는 ∑_{k>K}c^k/k 이하.

독립 prior kernel로 path를 넓혀 원래 모형에 없던 insertion 변수를 쓸 수 있으며 새 root 변수는 quenched로 둔다. 임의의 유한 kernel 열에 대해 조건부 항등식이다. n→0 해석적 연속, 무한 cascade, 물리적 Gibbs pure-state 구조를 가정하거나 도출하지 않는다. 기존 RPC와의 동일시는 미검증이다. 여기의 '확률적 representation'은 위에 완전히 정의한 유한 proposal와 signed multiplier에 한정한다.

원문의 density/first variation/protected-leaf 회계(tree:Y-recursion, tree:density, tree:first-variation, trees.tex180–210)와 두 전개(tree:log-expansion, tree:extension-expansion)는 근거가 있는 exact 진술이다. 새 proposal는 그 유한 signed 합에 importance sampling 항등식 p·(w/p)=w를 적용해 얻은 exact 재표현이며 외부 확률 객체와의 대응 주장이 아니다. second moment bound는 위 직접 부등식에서 나온다. 복소 해석 경계의 상세 증명은 blackbox다.
