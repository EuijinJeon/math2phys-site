# 사전 정답과 채점 기준 — 독자 비공개

채점은 소항목 단위. 올바른 대체 유도 허용, 핵심 계산 없는 결론에는 해당 reasoning 점수 미지급. 후보명을 모르는 독립 채점자가 응답의 근거를 인용해 채점한다.

## Q1 (6)

μ=EX=1/2, Z=1+μt₁+t₂. L=1에서 Kᴬ=A K/Z, 원래 tree 세 leaf의 밀도 AᵃAᵇAᶜ/Z³. anchor 상쇄 후 F=[μ(1+t₂)+t₁]²/Z³. (유리식 2점: 분자1/분모1.)

첫 미분: b 재사용은 E[X_b²X_c]=μ=1/2, c 재사용도 1/2. root fresh는 γ=−3, E[X_bX_cX_new]=μ³=1/8, 따라서 1−3/8=5/8. (1점 계산, 1점 history와 γ.)

두 번째 방향은 D₂=1. 첫 걸음 old 선택이면 n=3,u=1, 둘째 계수 총합 u−n=−2. 첫 걸음 fresh이면 n=4,u=2, 역시 −2. 따라서 mixed derivative=−2·5/8=−5/4. 유리식 미분으로도 같다. 혼합 미분에 factorial 없음. (값1점, 두 경우 n/u와 무factorial1점.)

## Q2 (4)

U=(μ+t)/(1+μt)³. U′(0)=1−3μ²=1/4. old c만 고를 수 있고 +1·E[X_c²]=1, fresh는 root γ=−3·E[X_cX_new]=−3/4. a,b 모두 분모가 있어 leaf 항이 상쇄. (선택·보호 이유1, fresh1, 값1, 유리식 검산1.)

## Q3 (5)

root n=2: −0.4. 깊이1의 ab 공통 vertex n=2: 0.2−1.4=−1.2. 깊이1의 c unary: −0.5. 깊이2는 a,b,c 각각 −0.3. 총 γ=−3. (목록2점: branch1/unary1.) Q root 확률=0.4/3=2/15 (1점). canceled-anchor에는 old b,c +1항이 필요: 실제 상수 삽입은 kernel 불변이고 F=(1+t)⁻¹이므로 미분−1. fresh만은−3. (실제값/비교1, old 누락 이유1.)

## Q4 (3)

log Y₀=log(1+t): 3차 도함수2, t³계수1/3. canceled F=(1+t)⁻¹: 도함수−6, 계수−1. (각 쌍1점.) log는 첫 미분 뒤 protected leaf 하나에서 시작하여 k−1번 fresh만, 절댓값 곱1·2···(k−1). canceled-anchor는 처음 anchor 하나에서 k번 fresh, 곱1·2···k. 모든 leaf가 protected인 anchor-only tree의 사례이며 일반 old tree의 경우는 상쇄를 거쳐 같은 상수 결과. 각각 도함수를 k!로 나누면 Taylor 계수. (1점.)

## Q5 (6)

모두 거짓. 각 1점은 이유까지 있어야 한다. (a) unary γ=m_d−m_{d+1}≠0, 실제 미분 합산에서 생략 불가. 형상 topology의 축약과 혼동 금지. (b) replica 위치가 별개이므로 값의 우연한 일치는 vertex 동일시가 아니다. (c) fresh는 음수이고 곱 부호 혼합. 별도 양의 proposal과 signed weight는 가능하나 c_E가 확률인 것은 아님. (d) 고정 L·exponent·tree size·방향 bound에서 kernel uniform이다. (e) 제시된 비교 논증은 m_d≥η>0을 사용한다. d=0의 고차 branching 인자에서 추가 δ가 생겨 |J|가 δ^{b_sep}보다 작아질 수 있으므로 그 논증을 추가 조건 없이 적용할 수 없다. 이것은 실제 비율이 발산한다는 증명도 η 조건의 필요성 주장도 아니다. (f) 보조 유한 kernel tree의 항등식이며 물리 Gibbs/RPC 동일시를 증명하지 않는다.

## Q6 (4)

L_{12}[H₀]=D₁,D₂를 차례로 붙이는 두-step history 합, L₂[H₁]=D₂를 한 번 붙이는 한-step history 합이라 쓰면 ∂₁∂₂V(0)=L_{12}[H₀]+L₂[H₁]. product rule에서 H의 t₁미분이 H₁이라 한 번 생김. 2!이나 2배 없음. (정확한 두 합2점, 추가 항과 무factorial1점.) 수치 예 V=t₁/(1+t₂+μt₁), mixed=−1. (1점.)

근거: trees.tex 67–154(밀도·first variation), 180–210(임의 protected set), 241–301(두 전개), 393–455(계수 한계). Q1/2/3/6은 신규 유도이며 기존 pilot 문항의 상수 G=1, old leaf 두 개 계산과 다르다.
