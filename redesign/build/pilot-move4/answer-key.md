# 채점 기준 (독자에게 주지 않는다)

근거: 카드 `x:tree-differentiation-rule`, `x:tree-extension-history`, `tree:extension-expansion`, `tree:reference-total`, `tree:charging`, `tree:insertion`, `pert:palm`, 규칙 P6′·P7 (2026-11-13 판).

점수: 2 = 맞고 출처가 "글에 적혀 있음" / 1 = 맞지만 추론·부분적, 또는 출처 표시가 추측 / 0 = 틀림 또는 찾지 못함. 9번은 점수 없이 목록으로 모은다.

1. $\partial_{t_1}\cdots\partial_{t_k}E^{A_{\boldsymbol t}}_{\mathcal T}[H/A^{a_*}_{\boldsymbol t}]\big|_{\boldsymbol t=0}=\sum_Ec_E\,E_{\mathcal T_E}[H\prod_jD_j^{a_j(E)}]$. 좌변: insertion $A_{\boldsymbol t}=1+\sum t_jD_j$ 로 바뀐 tree 법칙 아래, anchor 인자를 나눈 old tree 함수 $H$ 의 기대값의 $\boldsymbol t=0$ 혼합 미분. 우변: extension history에 대한 합, 각 항은 원래(섭동 없는) 법칙에서 최종 tree $\mathcal T_E$ 의 기대값에 color $j$ leaf의 $D_j$ 를 곱한 것. 우변이 원래 법칙의 기대값이라는 점이 핵심.
2. color $1..k$ 를 순서대로: (i) anchor 아닌, 아직 color 안 받은 old leaf 재사용, 계수 $+1$; (ii) 현재 tree의 내부 vertex $\beta$ 에서 fresh path, 계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$. $n_\beta$ 는 **그 걸음 시점의 현재 tree**(안 쓴 old path와 이미 붙인 path 포함)에서 $\beta$ 의 자식 수. $c_E$ 는 계수의 곱. ($n_\beta$ 의 시점을 말하지 못하면 1점.)
3. history $2L-s$ 개: 재사용 $b$ ($+1$); 줄기 깊이 $d=0..s-1$ ($n=1$): $m_d-m_{d+1}$, 합 $-m_s$; 갈라지는 vertex $d=s$ ($n=2$): $m_s-2m_{s+1}$; 두 가지 아래 $d=s+1..L-1$ 각각 ($n=1$): 합 $2(m_{s+1}-1)$. 총합 $-1$. 좌변 $\frac{d}{dt}\frac1{1+t}|_0=-1$ 과 같다. (fresh 위치를 빠뜨리거나 $n$ 을 틀리면 감점.)
4. P7은 score 집중에서 온다. Palm(Poisson add-one) 항등식이 score와 시험함수의 곱 기대값을 "anchor에 새 섭동 하나를 넣은 tree 기대값"($H=f$ 인 old tree 판과 anchor 하나 판)으로 바꾸고, 그 차이의 $t$-Taylor 계수가 0으로 가며, 각 계수를 P6′ 으로 history 합으로 푼 것이 P7의 두 합이다. 상쇄의 정확한 이유는 Palm 단계 세부라 "anchor에 넣은 섭동의 효과를 재는 꼴"까지 말하면 2점.
5. 처방한 모양 $S$ 와 호환되는 모든 history의 $c_E$ 합. reference 없는 old 부분 tree의 계수 합이 telescoping으로 $m_{d+1}$ 이 되어 old tree가 지워진다. 예: $j=1$ 이므로 $m_d-m_{d+1}$, 격자에서 $-\delta=-1/L$.
6. $f$: old replica multioverlap의 유계 다항식. $R_E$: 새 replica들(spin anchor면 anchor 포함)의 multioverlap. $c_E$: P6′ 계수. 첫 합: old tree에서 제약 $\mathcal C$ 를 지키는 history, 둘째 합: anchor 하나만의 tree에서 같은 제약. 뜻: anchor에 새 섭동을 더한 효과가 $f$ 와 분리된다(무상관). P5의 선택된 수열을 따라, 고정 $L$·tree·제약에서 $N\to\infty$, 율·$L$-균일성 없음.
7. 받는 것: P5의 선택된 수열(score 집중 (ii), 모멘트 수렴 (iii)), P6·P6′ 의 tree 전개. 넘기는 것: 모든 고정 tree·제약에서의 P7 항등식; 수 5는 이것과 tree 표본 규칙, $\kappa$·계수 한계(P6′), 확률 부등식만 쓴다.
8. $\sum_E\lvert c_E\rvert\le C_{q,k}\delta^b$(처방 깊이 $b$ 개가 old branching 깊이와 겹치지 않을 때), $\lvert J\rvert$ 도 $\delta^b$ 크기로 작고 $L$ 에 균일한 양의 하한이 없다. $L$ 에 균일한 것은 비율 $\sum\lvert c_E\rvert/\lvert J\rvert\le C_{q,k,\eta}$($m_{d_v}\ge\eta$).
