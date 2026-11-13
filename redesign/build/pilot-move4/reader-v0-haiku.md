# 독자 시험 v0 (수 4, 질문 1–9) — 독자: Haiku 5.5, 통계물리 대학원생 역할

읽은 파일: /tmp/reader-in-v0/L0.md, L1.md, L2.md, rules.md, glossary.md, 그리고 질문지 /home/user/math2phys-site/redesign/build/pilot-move4/questions.md.
L2는 §1–§10과 부록 A를 모두 읽었다. glossary는 질문에 필요한 항목(tree-coefficient, tree-law, protected-leaf, extension-history, reference-path, anchor, mark, palm-identity, tree-identity, depth-delay, score, selected-sequence, insertion, multioverlap, conditional-decorrelation, depth-average 등)을 찾아 읽었다. rules.md는 P6, P6′, P7 행을 읽었다.

줄 번호는 각 파일의 행 번호다. 출처 표기: 글에 적혀 있음 / 글에서 추론함 / 추측함 / 찾지 못함.

---

## 1. 주 식 (P6′)

**(a) 답.** P6′이 주장하는 것은 다음 항등식이다. 좌변은 old tree T 에서 anchor a* 의 삽입 인자 A^{a*} 를 상쇄한 tree 기대값을, 섭동 크기 t_1,…,t_k 로 한 번씩 미분해 t=0 에서 본 혼합 도함수다. 우변은 extension history E 마다 계수 c_E 가 붙은 tree 기대값의 합이다.

- 좌변: ∂_{t_1}⋯∂_{t_k} E^{A_t}_T[ H / A^{a*}_t ] |_{t=0}. 여기서 A_t = 1 + Σ_j t_j D_j (L2 §1.5의 2번 항목에서 정의), H 는 old tree 변수의 유계 함수다. "anchor 인자를 상쇄한다"는 것은 1/A^{a*}_t 를 곱한다는 뜻이다.
- 우변: Σ_E c_E · E_{T_E}[ H ∏_j D_j^{a_j(E)} ]. E 는 color 1..k 를 anchor에서 차례로 붙이는 방법, T_E 는 그 확장 tree, a_j(E) 는 color j 가 D_j 를 받는 leaf 표시다. a_j(E) 의 정확한 정의는 찾지 못했다.
- 각 항 = 계수 c_E × 확장 tree 위 기대값. 합은 가능한 모든 history에 대한 것이다.

**(b) 근거 위치.**
- L2 §6.2, 줄 232: 말로 된 기술("anchor의 삽입 인자를 상쇄한 tree 기대값을 … 한 번씩 미분", "결과는 … 계수 c_E 가 붙은 tree 기대값의 합").
- L2 §6.2, 줄 230: "혼합 미분은 이 순서 있는 확장 규칙 그대로" 라는 문장이 있다.
- L2 본문에는 H, D_j, a_j(E) 가 든 식이 없다. 식은 rules.md 22행(P6′ 행)의 "차이" 칸에 있다.

**(c) 출처.** 말로 된 주 식: 글에 적혀 있음. 식의 H, D_j, a_j(E) 세부: L2에서는 찾지 못함, rules.md 22행에만 있음. a_j(E) 의 정의: 찾지 못함.

---

## 2. c_E 의 정의

**(a) 답.**
- extension history E: anchor a* 를 고정하고 color 1, …, k 를 차례로 붙이는 기록이다. 한 걸음에서 새 replica 가 할 수 있는 선택은 두 가지다.
  - (i) 아직 쓰지 않은 old replica (anchor 제외) 하나를 다시 쓴다. 이 선택의 계수는 +1 이다.
  - (ii) 현재 tree 의 내부 vertex β 에서 새 path 를 갈라낸다. 이 선택의 계수는 γ_β = m_{d_β} − n_β m_{d_β+1} 이다. d_β 는 β 의 깊이다.
- c_E = 그 history 의 걸음마다 계수의 곱이다.
- n_β: β 의 자식 수다. 정확히는 그 걸음의 현재 tree 에서 β 의 자식 수이며, 안 쓴 old path 와 이미 붙인 path 를 모두 포함한다. (주: 이 정의는 확률 정규화로 확인된다. 2-leaf tree 에서 β 를 모두 더하면 Σ_β (n_β m_{d_β+1} − m_{d_β}) = 2 = 잎 수가 된다. 이 확인은 내가 한 계산이다.)
- γ_β < 0 이다. n_β ≥ 1 이고 m_d < m_{d+1} 이므로 γ_β ≤ m_d − m_{d+1} < 0 이다. 이것은 L2가 적은 대로다.

**(b) 근거 위치.**
- L2 §6.2, 줄 232: 걸음 선택 (i)(+1)과 (ii)(γ_β), 그리고 "c_E 는 그 곱이라 부호가 섞인다".
- L2 §6.1, 줄 224: γ_β 의 정의, "n_β 는 자식 수", "n_β ≥ 1 이므로 γ_β < 0".
- n_β 가 "현재 tree 의 자식 수 (안 쓴 old path 포함)"라는 것: rules.md 22행 "차이" 칸. glossary.md 의 g:extension-history (줄 347–352), g:tree-coefficient (줄 326–331).

**(c) 출처.**
- 계수의 곱 구조와 (i), (ii) 선택: 글에 적혀 있음 (L2 줄 232).
- n_β 의 정확한 지시 대상 (현재 tree, 안 쓴 old path 포함): L2 본문에는 없다. L2는 "자식 수"라고만 쓴다. 규칙 표(rules.md 22행)와 용어집에서 찾았다. 그러므로 L2만 읽은 독자에게는 "글에 적혀 있지 않음"이다.
- γ_β < 0: 글에 적혀 있음 (L2 줄 224).

---

## 3. 계산 (k=1, H=1, D=1, m_0=0, m_L=1)

설정: old tree 에 anchor a* 와 다른 replica b 가 있고, 둘은 깊이 s (0 ≤ s ≤ L−1) 에서 갈라진다. 그 tree 의 내부 vertex 는 다음과 같다.
- 공통 prefix: v_0, …, v_{s−1}. 각각 자식 1개 (n=1).
- 갈라짐 vertex: v_s. 자식 2개 (n=2).
- anchor 쪽: α_{s+1}, …, α_{L−1}. 각각 n=1.
- b 쪽: β_{s+1}, …, β_{L−1}. 각각 n=1.
(잎은 깊이 L 이다. 내부 vertex 는 깊이 0..L−1 에만 있다.)

**가능한 history 전부 (k=1, 총 2L − s 개):**

| history | 설명 | c_E |
|---|---|---|
| E_reuse | color 1 이 old replica b 를 다시 씀 | +1 |
| E_{v_d}, 0 ≤ d ≤ s−1 | 공통 prefix 의 n=1 vertex v_d 에서 갈라짐 | m_d − m_{d+1} |
| E_{v_s} | 갈라짐 vertex v_s (n=2) 에서 갈라짐 | m_s − 2m_{s+1} |
| E_{α_d}, s+1 ≤ d ≤ L−1 | anchor 쪽 vertex α_d (n=1) 에서 갈라짐 | m_d − m_{d+1} |
| E_{β_d}, s+1 ≤ d ≤ L−1 | b 쪽 vertex β_d (n=1) 에서 갈라짐 | m_d − m_{d+1} |

history 개수 확인: 1 + s + 1 + 2(L−1−s) = 2L − s.

**합:**
1 + Σ_{d=0}^{s−1}(m_d − m_{d+1}) + (m_s − 2m_{s+1}) + 2 Σ_{d=s+1}^{L−1}(m_d − m_{d+1})
= 1 + (m_0 − m_s) + (m_s − 2m_{s+1}) + 2(m_{s+1} − m_L)
= 1 + m_0 − 2m_L
= 1 + 0 − 2 = **−1**.

s 가 소거되어 합은 s 에 무관하다.

**좌변 값.** H=1, D=1 이면 A_t = 1 + t 는 모든 잎에서 같은 상수다. 이때 tilted tree 법칙은 변하지 않는다. A 가 상수이면 Y_d/Y_{d−1} 이 t 에 무관하기 때문이다. 따라서 E^{A_t}_T[1/A^{a*}_t] = 1/(1+t) 이고, ∂_t |_{t=0} = **−1**.

**확인.** 합 −1 = 좌변 −1. 맞는다.

**(a) 답 요약.** 가능한 history 는 2L − s 개다. 합은 −1 이고, 좌변 −1 과 일치한다.

**(b) 근거.** history 구조: L2 줄 232, glossary g:tree-coefficient 줄 331과 g:extension-history 줄 349. 잎 깊이와 내부 vertex 범위: L2 §6.1 줄 218. m_0 = 0, m_L = 1 은 L2 본문에 없고 glossary g:parisi-parameters 줄 142의 "tree 계산에서는 m_0=0, m_L=1"에 있다. 좌변 계산: L2 줄 230의 정의와 rules.md 22행, 그리고 내가 한 계산.

**(c) 출처.**
- history 목록과 계수: 글에서 추론함 (글의 규칙을 이 tree 에 적용한 것이다).
- 합 −1: 글에서 추론함 (내 계산).
- 좌변 −1: 글에서 추론함. 정규화된 tilted 기대값을 쓰는 방식은 L2 본문에 없고 내가 가정했다. "tree 기대값은 확률 기대값"이라고 읽었다.

---

## 4. anchor

**(a) 답.**
- anchor 를 따로 보는 이유: Palm 항등식(Poisson add-one)이 score 곱을 "anchor 에 새 섭동 하나를 넣은 tree 기대값"으로 바꾼다. 그래서 anchor 의 삽입 인자를 상쇄한 기대값이 나온다.
- 상쇄가 anchor 에만 적용되는 이유: 글에는 명시적 이유가 없다. 용어집 g:protected-leaf (줄 342–343)는 "상쇄된 leaf 는 미분해도 새 항이 생기지 않는다"고 쓴다. anchor 를 처음부터 protected 로 두면 확장 전개의 history 에서 anchor 가 빠진다. 그래서 anchor 는 다시 고를 수 없다. 이 설명은 회계상의 편의로 읽힌다.
- P7 으로 이어지는 연결 (L2 §6.3, 줄 254): (1) score 집중(P5(ii))으로 Palm 항등식의 차이 H_N(t_ν,u_ν) 가 작아진다. (2) u_ν 를 t_ν 의 모든 고정 거듭제곱보다 작게 잡으면 Taylor 계수가 모두 0 으로 간다. (3) 계수의 극한 존재는 P5(iii)이 준다. (4) 각 Taylor 계수를 P6′ 으로 history 합으로 풀고, polarization 과 mark selector 로 제약을 고르면 P7 이 된다.

**(b) 근거 위치.** L2 §6.2 줄 232 ("anchor는 처음부터 상쇄되어 다시 고를 수 없다"), L2 §6.3 줄 254 (연쇄 전체). glossary g:palm-identity (줄 375–380), g:protected-leaf (줄 340–345), g:anchor (줄 361–366).

**(c) 출처.**
- anchor 가 상쇄되고 다시 고를 수 없다는 것: 글에 적혀 있음.
- Palm 항등식이 anchor 에 섭동을 넣는 tree 로 바꾼다는 것: 글에 적혀 있음 (말로).
- anchor 만 상쇄하는 이유의 근본: 찾지 못함. perturbations.tex 원문 카드는 이 파일 집합에 없다.
- "회계상의 편의"라는 읽기: 추측함.

---

## 5. 모양별 총합 κ(S)

**(a) 답.**
- κ(S) 는 anchor 와 새 replica 들이 모양 S 로 갈라지도록 처방된 모든 history 의 계수 합이다. 공식: κ(S) = ∏_{v∈Br(S)} ∏_{j=1}^{a_v−1} (m_{d_v} − j m_{d_v+1}).
- old tree 와 무관한 이유: 처방은 reference path (anchor 와 이미 붙인 path) 와의 split 깊이만 지정한다. reference 가 없는 old 부분 tree 의 계수 합이 m_{d+1} 로 telescoping 되어 old tree 의 모양이 지워진다. glossary g:reference-path (줄 354–359)는 "지정된 조상 관계가 같은 쓰지 않은 old path 들은 구별하지 않는다"고 쓴다. 이것이 telescoping 의 조건이다.
- 2-leaf 경우 (anchor 와 새 replica 하나가 깊이 d 에서 갈라짐): Br(S) = {v}, d_v = d, a_v = 2 라고 보면 κ(S) = m_d − m_{d+1}. 격자 m_d = d/L 에서 κ(S) = (d − (d+1))/L = **−1/L = −δ**.
- 내가 한 확인: old tree 의 갈라짐 깊이 s 를 두고 세 경우를 모두 세었다.
  - d < s: 공통 prefix v_d 하나만 가능. 합 = m_d − m_{d+1}.
  - d = s: reuse b (+1), 갈라짐 vertex v_s (m_s − 2m_{s+1}), b 쪽 vertex β_{d'} (d' ≥ s+1, 합 m_{s+1} − 1). 합 = m_s − m_{s+1}.
  - d > s: anchor 쪽 α_d 하나만 가능. 합 = m_d − m_{d+1}.
  - 셋 모두 격자에서 −δ 다. s 에 무관하다.

**(b) 근거 위치.** L2 §6.2 줄 234 (κ 공식과 telescoping), 줄 232 (reference path). L2 줄 238 ("미루기 전" 예: 부호 있는 합 −δ). glossary g:tree-coefficient (줄 326–331), g:reference-path (줄 354–359), g:depth-delay (줄 390–395). rules.md 22행 P6′ 차이 칸 (telescoping 정당화 `trees.tex` 359–375 인용).

**(c) 출처.**
- κ 공식과 "old tree 와 무관": 글에 적혀 있음 (L2 줄 234).
- telescoping 이 reference 없는 부분 tree 에서 일어난다는 것: 글에 적혀 있음 (L2 줄 234).
- Br(S) 와 a_v 의 정의: 찾지 못함. 이 파일 집합 어디에도 정의가 없다 (grep으로 확인). 2-leaf 에서 a_v = 2 로 읽은 것은 추측함이다.
- κ = −δ 의 값과 s 무관성: 글에서 추론함 (내 계산).

---

## 6. P7

**(a) 답.**
- f: old replica multioverlap 의 유계 다항식. 고정된 시험함수다.
- R_E: 새 replica 들 (spin anchor 이면 anchor 포함) 의 multioverlap.
- c_E: 제약 C 를 지키는 extension history 의 계수.
- 첫 합 Σ_{E∈𝔈(T,a*,C)} c_E E[f R_E]: old tree T 에서 제약을 지키는 history 에 대한 합.
- 둘째 합 E f · Σ_{E'∈𝔈({a*},a*,C)} c_{E'} E[R_{E'}]: anchor 하나만 있는 tree 에서 같은 제약을 지키는 history 에 대한 합.
- 두 합의 차가 0 으로 간다.
- 말로 하면: anchor 에 새 섭동 하나를 더한 효과가 old tree 의 시험함수 f 와 분리된다.
- 성립 범위: 고정한 L, tree, f, 제약 C 마다, P5 의 선택된 수열을 따라 N → ∞ 로만 성립한다. 수렴 속도는 주어지지 않고, L 에 대한 균일성은 주장되지 않는다.

**(b) 근거 위치.** L2 §6.3 줄 246–248 (식과 말), 줄 250 (제약 C 의 뜻과 mark), 줄 252 (성립 범위). rules.md 23행 (P7 행).

**(c) 출처.** 식, f, R_E, 두 합의 범위, 말의 뜻, 성립 범위: 글에 적혀 있음. E[·] 의 정확한 측도(어떤 기대값인지)는 L2 본문에 명시되어 있지 않다. 글에서 추론함: root 와 tree 표본 전체에 대한 기대값으로 읽었다 (glossary g:root 줄 202–208 참고).

---

## 7. 흐름

**(a) 답.**
- 수 4 가 받는 것 (수 3 에서):
  - 선택된 수열 (N_j, u_j) 위에서 score 오차 e_{ν,N_j} → 0 (P5(ii)). 이것이 Palm 항등식의 차이를 누른다.
  - 유한 tree 모멘트의 수렴 (P5(iii)). 이것이 Taylor 계수의 극한 존재를 준다.
  - 섭동의 정의 (P3 의 섭동 틀, L2 §4.2) 는 수 4 가 쓰는 장치다. 다만 §6 본문에서 P3 과 P4 를 직접 인용하는 곳은 찾지 못했다.
- 수 4 가 수 5 에 넘기는 것: P7 항등식 (L2 §6.4, 줄 260: "수 5가 모형에서 받는 입력은 이 항등식과 tree 표본 규칙뿐"). 또한 P6′ 의 계수 구조 (κ, 계수 한계) 가 수 5 의 귀납에서 쓰인다 (L2 §7.2 줄 294).
- 수 4 가 수 6 에 넘기는 것: P6 의 log 전개 (L2 §6.1, 줄 222–223). L2 §8 의 "수 6이 더하는 입력" 목록 (줄 336 이후)에 log 전개가 있다. 또한 L2 줄 260은 수 6 의 입력이 (2.3), (2.4) 를 쓰지 않는다고 한다.

**(b) 근거.** L2 §1.3 줄 53–54 (수 4 의 역할: "P6, P6′, P7"), L2 §5 줄 191–196 (P5), L2 §6.4 줄 260, L2 §7.2 줄 294, L2 §8 줄 336. L1 항목 4 와 5 (L1.md 줄 22–25, 28–30).

**(c) 출처.** 수 3 → 수 4 와 수 4 → 수 5 의 연결: 글에 적혀 있음. 수 4 → 수 6 에서 P6 이 넘어간다는 것: 글에서 추론함 (L2 §8 의 입력 목록을 P6 의 위치와 맞춘 것). P3, P4 가 수 4 안에서 어떻게 쓰이는지: 찾지 못함.

---

## 8. 계수 한계

**(a) 답.**
- δ^b 크기로 작은 것: 정규화 계수 |J| 와 절댓값 계수 합 Σ_E |c_E|. 여기서 J = ∏_v ∏_{j=1}^{a_v−1} (m_{d_v} − j m_{d_v+1}) 이다. 격자에서 각 vertex 의 j=1 인자가 −δ 이므로 |J| ~ δ^b 다.
- L 에 균일하게 유계인 것: 상대 한계 (1/|J|) Σ_E |c_E| ≤ C_{q,k,η} (η 고정). 상수 C_{q,k} 는 old leaf 수 q 와 새 replica 수 k 에만 의존하고 L 과 지정 깊이에 무관하다. 절댓값 합 자체는 Σ|c_E| ≤ C_{q,k} δ^b 이므로 L 에 균일하게 δ^b 로 작다.
- 주의: |J| 에는 L 에 균일한 양의 하한이 없다. 균일한 것은 비율뿐이다.

**(b) 근거 위치.** L2 §6.2 줄 236 (계수 한계 전체). glossary g:depth-delay (줄 391): |J| ≥ c δ^{2b}, 상대 비용 ≤ C_{k,η} (L 에 균일). rules.md 22행: |J| 의 하한 δ^b η^{Σ(a_v−2)}.

**(c) 출처.** 계수 한계의 진술: 글에 적혀 있음 (L2 줄 236). |J| ~ δ^b 의 이유 (j=1 인자가 −δ): 규칙 표(rules.md 22행)에 있다. 내가 격자에서 확인했다 (글에서 추론함).

---

## 9. 막힌 곳

읽다가 막히거나 다시 읽은 곳을 모두 적는다.

1. **L2 줄 224, "붙이는 확률은 tree 계수 γ_β 로 정해진다".** γ_β < 0 이므로 확률이 될 수 없다. 용어집 g:tree-law (줄 335)는 확률이 (n_β m_{d+1} − m_d)/n = −γ_β/n 라고 쓴다. L2 문장은 부정확하다. 용어집을 보고서야 풀렸다.
2. **L2 줄 224, "n_β 는 자식 수".** 어느 tree 의 자식 수인지 적혀 있지 않다. 규칙 표 P6′ 차이 칸 (rules.md 22행)에서 "현재 tree (안 쓴 old path 와 이미 붙인 path 포함)"라고 풀렸다.
3. **L2 줄 230–232, P6′ 좌변.** 좌변과 우변의 식이 L2 본문에 없다. 말로만 되어 있다. 식은 rules.md 22행에서 찾았다. H, D_j, a_j(E) 의 정의도 L2에는 없다.
4. **L2 줄 232 vs rules.md 22행, "추가 factorial".** L2 는 "혼합 미분은 … 추가 factorial 이 붙지 않는다"고 쓴다. rules.md 는 "D_j = D 이면 t^k 계수는 우변/k!"라고 쓴다. 혼합 도함수와 Taylor 계수의 차이 (k!) 다. 두 문장을 맞춰 읽느라 다시 읽었다.
5. **L2 줄 234, a_v 와 Br(S).** 정의가 없다. glossary g:tree-coefficient (줄 326)에도 없다. 내가 2-leaf 에서 a_v = 2 로 읽었다.
6. **L2 줄 224 와 232, "현재 tree" 와 "old tree" 와 "확장 tree".** 세 용어가 섞여 나온다. L2 줄 232는 "현재 tree 의 내부 vertex β" 라고 한다. 용어집 g:extension-history (줄 349)의 "어휘" 설명으로 구분했다.
7. **L2 줄 254, H_N(t_ν, u_ν).** L2 본문에서 정의되지 않았다. 용어집 g:palm-identity (줄 376)에서 H_N = J_{N,T}(t,u) − E f J_{N,{a*}}(t,u) 로 찾았다. J_{N,T} 도 L2 에서 정의되지 않았다.
8. **L2 줄 254 및 256, "polarization" 과 "mark selector".** polarization 은 L2 와 용어집 어디에도 정의가 없다. rules.md 39행에 "pert:tree-identity 증명 안의 polarization"이라는 이름만 있다. 찾지 못함. mark selector 는 용어집 g:mark (줄 368–373)에서 찾았다.
9. **L2 줄 250, "추가 color".** color 라는 말은 본문에서 괄호 설명 없이 나온다. 용어집 g:extension-history 에서 color 1..k 로 풀렸다.
10. **L2 줄 294, S^+.** §7.2 의 J = κ(S^+)^2 에서 S^+ 가 정의되지 않았다. 용어집 g:depth-delay (줄 391)는 "S → S^+"라고만 쓴다. 정의는 찾지 못했다.
11. **L2 줄 294, "깊이 연속성 (유계 martingale 의 증분 에너지 합 ≤ 1)".** 설명이 한 줄뿐이라 용어집이나 다른 곳을 찾아야 했다. 용어집에 더 자세한 정의는 없었다. 찾지 못함.
12. **L2 줄 216 과 215 (§6.1 vs §4.1), m_0 = 0, m_L = 1.** L2 §6 본문에서 이 경계 조건을 명시하지 않는다. 격자 m_d = d/L (줄 155) 에서 따라 나오지만, 일반 m 에 대해서는 용어집 g:parisi-parameters (줄 142)에서 찾았다.
13. **L2 줄 232, "anchor 는 처음부터 상쇄되어 다시 고를 수 없다", 그리고 "protected".** protected 는 링크가 걸려 있다. 용어집 g:protected-leaf (줄 340–345)에서 "미분해도 새 항이 생기지 않는다"는 뜻을 찾았다.

---

## 요약

- 질문 1–9 에 모두 답했다. 3번 계산은 과정을 전부 적었다. 합은 −1 이고 좌변과 일치한다. 합은 갈라짐 깊이 s 에 무관하다.
- 5번: κ = m_d − m_{d+1}, 격자에서 −δ. old tree 와 무관함을 세 경우로 확인했다.
- 주된 막힘: (1) L2 줄 224 의 "확률 = γ_β" 가 부정확하다 (용어집으로 바로잡았다). (2) P6′ 의 식이 L2 본문에 없고 규칙 표에만 있다. (3) a_v, Br(S), polarization 의 정의가 어디에도 없다. (4) 혼합 도함수와 Taylor 계수의 k! 차이가 L2 와 규칙 표 사이에서 어긋나 보인다.
- 이 파일 밖에서 찾은 정보는 모두 용어집과 규칙 표에서 왔다. 다른 파일은 열지 않았다.
