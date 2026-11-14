# 새 적용 시험

packet 본문만 근거로 다음을 한국어로 답하라. 식의 계산 과정을 짧게 쓰고, 본문에 있는 사실과 자신이 유도한 사실을 구별하라. 풀 수 없으면 빈칸의 이유를 적어라. 총 답변은 대략 2,500 단어 이하. 다른 자료는 열지 않는다.

1. **observable이 있는 세 replica (6점).** L=1이고 root는 고정이다. 각 leaf의 X는 독립으로 ±1을 취하며 P(X=1)=3/4이다. old tree의 leaf는 a,b,c이고 anchor는 a다. A=1+t₁X+t₂, G=XᵇXᶜ이다. F(t₁,t₂)=Eᴀ_T[G/Aᵃ]라 둔다. (i) 원래 법칙의 평균으로 F를 닫힌 유리식으로 쓰라. (ii) ∂₁F(0,0)을 history 세 종류(사용 가능한 old leaf 각각, fresh)로 계산하라. (iii) ∂₂∂₁F(0,0)을 구하고, 첫 걸음이 old 재사용/fresh인 경우 각각 두 번째 걸음의 현재 leaf 수와 사용 가능한 old leaf 수를 이용해 검산하라. 혼합 미분에 factorial을 곱하는가?

2. **보호집합 바꾸기 (4점).** Q1의 확률법칙·old tree에서 a와 b 둘의 삽입 인자를 상쇄한다. A=1+tX, G=Xᶜ로 두고 U(t)=Eᴀ_T[G/(AᵃAᵇ)]라 한다. U′(0)을 구하라. 어떤 old leaf가 직접 선택되는지, fresh 계수는 무엇인지 보이고 원래 법칙의 유리식으로 검산하라. 단일 anchor 식을 기계적으로 복사해서는 안 된다.

3. **비균등 격자에서 현재 tree (5점).** L=3, (m₀,m₁,m₂,m₃)=(0,0.2,0.7,1). old leaf는 a,b,c다. a,b는 깊이 1까지 vertex를 공유하고 거기서 갈라지며 c는 깊이 0에서 이들과 갈라진다. 모든 unary vertex를 유지한다. anchor는 a. (i) 깊이·위치별 내부 vertex γ를 전부 쓰고 합을 구하라. (ii) 여기서 Q 법칙으로 fresh path 한 개만 붙일 때 root 선택 확률은? (iii) canceled-anchor 미분에 그 Q fresh 선택만 쓰면 충분한가? G=D=1일 때 실제 미분값과 fresh 항만의 합을 수치로 비교하라.

4. **두 전개의 세 번째 항 (3점).** 임의의 유한 kernel 열, 상수 D=1에서 (i) log Y₀의 3차 도함수와 t³ 계수, (ii) anchor 하나를 상쇄한 Eᴀ_T[1/Aᵃ]의 3차 도함수와 t³ 계수를 쓰라. (iii) 두 경우의 history 가중치에 왜 (k−1)!과 k!가 각각 나타나는지 하나의 미분 규칙으로 설명하라.

5. **다음 주장의 참/거짓과 이유 (각 1점, 6점).**
   - (a) unary vertex의 기여를 버리고 나머지 vertex의 기존 γ만 합산해도 일반적으로 같은 미분 계산이다.
   - (b) 서로 다른 leaf에서 우연히 같은 spin 배치가 뽑히면 같은 leaf로 합쳐야 한다.
   - (c) 모든 c_E를 양의 확률로 읽을 수 있다.
   - (d) kernel에 균일한 해석적 경계가 있으므로 depth L에도 균일하다.
   - (e) 이 문서에 제시된 δ^{b_sep} 절댓값 계수 한계와 J 비교 논증만으로, 추가 조건 없이 절댓값 계수 합/|J_sep|의 L-uniform bound가 보장된다.
   - (f) 이 유한 tree 계산으로 물리 Gibbs 측도의 pure-state/RPC 구조가 증명된다.

6. **매개변수에 의존하는 observable (4점).** 단일 anchor, A=1+t₁D₁+t₂D₂, H(t₁,t₂)=H₀+t₁H₁이며 H₀,H₁은 유계 old-tree 함수다. V(t)=Eᴀ_T[H(t)/Aᵃ]라 둔다. mixed derivative ∂₁∂₂V(0)를 parameter-independent observable용 history 연산을 사용해 정확히 표현하라. H₀만 넣은 원래 공식이 놓치는 항과 factorial 여부를 말하라. Q1의 L=1 확률법칙에서 old tree가 anchor 하나, D₁=X,D₂=1,H₀=0,H₁=1이면 값을 구하라.

마지막에 시험 과정에서 다시 읽은 부분 두 곳과 이해에 실패한 곳을 적어라(비채점). 이 자기보고를 성과 점수로 바꾸지 않는다.
