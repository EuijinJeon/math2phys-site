# 검토 1 대응 — §7 노드 카드

대상: `build/review-1-cards.md`의 발견 F1–F14, 작성자 표시 불확실점 1–6, 인터페이스 시험의 누수, §8 인터페이스, physics 칸 점검의 부수 지적.
모든 항목을 `source/sections/decorrelation.tex`(보조로 `trees.tex`, `perturbations.tex`, `comparison.tex`, `cavity.tex`)의 인용 행과 다시 대조했다. 고친 파일은 `cards/` 안의 카드뿐이다. 수정 후 `python3 tools/check.py --sections decorrelation`는 8개 검사 모두 통과(오류 0, 경고 0, 종료 코드 0).

## 대응 표

| 항목 | 검증 결과 | 조치 | 바뀐 카드 |
|---|---|---|---|
| F1 cavity field 독립을 명제 7.4에 돌림 | 맞음. tex 99–100, 236–244의 양은 site 쌍 평균 조건부 공분산 제곱뿐이다. 독립성은 comparison.tex 87–120 (`comp:patterns`, 균일 site 표본추출)과 153 (`decor:overlap-concentration` 적용)에서 나온다 | physics에서 그 문장을 지우고 "상태 안 절반"으로 바꿈. gap (5)에 독립성의 실제 출처와 비동치를 적음 | `decor:conditional-concentration` |
| F2 두 측 사영에 aligned 조건 누락 | 맞음. tex 226–228의 "two such sides"는 aligned 사본이다(26–28, 295–296). aligned가 아니면 같은 논법으로 $p_N^{\rm I}+p_N^{\rm II}$만 나온다 | `math`에 "깊이 배정이 aligned"를 넣고 `uses`에 `x:decor-eta-regular`를 더함. 본문에 근거와 일반 경우(작성자 유도)를 적음 | `decor:projection-bound` |
| F3 "셋 모두 $L$에 균등" | 맞음. tex 618–621에서 "uniform"은 상대 절댓값 비용 상계에만 붙는다 | `math`를 원문대로 고침: "균등한(uniform) 상대 절댓값 비용 상계, 더 작은 모양의 공분산 평균, martingale 추정 $C/L$". 검토자가 제안한 대체 문장("곱하는 상수는 $L$에 무관")은 `math`에 넣지 않음(아래 참조) | `decor:order-of-limits` |
| F4 누수: anchor 혼자인 쪽의 확장이 모두 같은 법칙 | 맞음. tex 362–363 "In every extension …", 418–419, 444–445 | s5.s3와 s5의 `math`에 그 사실과 합 $-\delta J\,\mathbb ER_{\rm target}$을 올림(`uses`에 s3.s1, `x:decor-tree-sampling` 추가). s6 `math`가 이를 s5에서 인용. 부모 뼈대도 s5의 `math`로 인용 | `decor:conditional-concentration.s5`, `.s5.s3`, `.s6`, `decor:conditional-concentration` |
| F5 누수: $\limsup_N$과 유한 깊이 평균의 교환 | 맞음. tex 49–52, 616–618 | `decor:identity-error`의 `math`에 "고정 $L$에서 $\mathcal A_{L,\eta}$는 유한 합이므로 $\limsup_N\mathcal A\le\mathcal A\limsup_N$, 배정마다의 $o_N(1)$은 평균 뒤에도 사라짐"을 넣음(`uses`에 `decor:average-definition`). s7.s4와 overlap-concentration.s4의 `math`가 이를 인용(후자의 `uses`에 `decor:identity-error`). 두 부모 뼈대와 s7 뼈대도 인용 | `decor:identity-error`, `decor:conditional-concentration.s7.s4`, `.s7`, `decor:conditional-concentration`, `decor:overlap-concentration.s4`, `decor:overlap-concentration` |
| F6 `decor:depth-continuity`의 `intuition` 유형 | 맞음. 앞 세 문장은 `math`의 정확한 약화이고 lemma는 논증에 쓰인다 | `abstraction: weakening`. $q(x)$ 문장은 gap으로 옮겨 "그림(intuition, 논증에 안 쓰임, math가 함의하지 않음)"으로 표시. s1에 정직한 대응(깊이별 자기 overlap $\mathbb E\|\mu_t\|_N^2$의 증가분 합 $\le1$)을 physics로 넣고, 그 등식을 s1 `math`에 올림 | `decor:depth-continuity`, `decor:depth-continuity.s1` |
| F7 gap (1) "평균으로만" | 맞음. tex 288–289 "at each fixed $L,d$" | gap (1)을 "$|S|\ge2$에서는 평균으로만, singleton은 각 $\eta$-regular $d$에서 점별로 $\limsup_Nv_N\le1/(\eta L)$"로 고침 | `decor:conditional-concentration` |
| F8 누수: 깊은 branching vertex에서 $\mathscr F_q$, $\mu_{q,T_j}$ 미정의 | 맞음. tex 179–184가 암묵적으로 쓴다 | `x:decor-topology`의 `math`에 "임의의 branching vertex $v$ 아래 부분 모양은 root→$v$ 경로를 initial stem으로 갖는 topology"를 넣음. s2의 `math`가 이 약속과 `decor:covariance-definition`으로 $\mathscr F_q$, $\mu_{q,T_j}$, $\mu_{q+1,T_j}$를 정의(`uses`에 두 카드 추가). 부모 뼈대도 인용 | `x:decor-topology`, `decor:depth-continuity.s2`, `decor:depth-continuity` |
| F9 누수: s3의 "$L\ge L_0$" | 맞음(불확실점 1과 같은 항목) | 불확실점 1 행 참조 | `decor:depth-continuity.s3`, `.s4`, `decor:depth-continuity` |
| F10 `x:decor-mesh`의 `uses: []`와 $L\ge2$ | 맞음. decorrelation.tex 4에 $L\ge2$ 없음. perturbations.tex 257 "For every fixed $L\geq2$", cavity.tex 16 "Fix $L\ge2$" | `uses: [pert:selection, cavity:grid]`, `math`에 출처를 적음 | `x:decor-mesh` |
| F11 s2의 physics null | 맞음 | 기저 단계에 physics(고정 $L$, 각 $\eta$-regular 깊이 $d$에서 단일 spin connected correlation 제곱 평균 $\le1/(\eta L)$), gap(상태=보조 prefix, 고정 $L$의 $\limsup_N$, $L^2$ 평균, 경계 깊이 제외), `abstraction: approximation` | `decor:conditional-concentration.s2` |
| F12 "$L$단계 계층" | 맞음. cavity.tex 16 "$r=L-1$ auxiliary levels", trees.tex 23 "$L=r+1$", comparison.tex 162–166 $\mathcal B_{L-1}$ | physics를 "깊이 $L$의 계층, 즉 $(L-1)$단 RSB"로 고침 | `x:decor-mesh` |
| F13 행 번호 | 맞음. regular shape 정의는 trees.tex 460–467 (0<η<1/2는 462, singleton regular는 465). comp:shape-error 논증은 comparison.tex 122–156, 명제는 160부터 | 두 카드의 행 번호와 내용 보강 | `x:decor-eta-regular`, `decor:section` |
| F14 "국소 자화의 곱" | 맞음. $\mu_{e,T_j}$가 국소 자화인 것은 $T_j$가 singleton일 때뿐 | physics를 "가지 $T_j$의 replica spin 곱의 상태 평균, singleton이면 국소 자화"로 고치고 gap에 명시 | `decor:projection-bound` |
| 불확실점 1 s3의 $L_0$ 출처 | 맞음(정정). tex가 "large $L$"을 부르는 곳은 201–203(s4 범위). s3에 필요한 조건은 $\eta L\ge1$이고 원문에 없다. 직접 재계산: $q'-q_v>\eta L\ge1\Rightarrow q_v+1<q'$, $q_v<(1-\eta)L\Rightarrow q_v+1\le L-1$ | s3 `math`를 "$\eta'$-regular 배정에서 $\eta'L\ge1$이면"으로 바꾸고 작성자 유도임을 명시. s4 `math`에 tex 201–203 인용과 $\eta'=\eta/2$ 적용을 적음. 부모 `math`의 $L_0$는 tex 148 "for all sufficiently large $L$"로 근거를 붙임. ❓ 제거 | `decor:depth-continuity.s3`, `.s4`, `decor:depth-continuity` |
| 불확실점 2 s4.s1, $e$가 평균 좌표 | 맞음. tex 155–162, 492–493, 588–589 | s4.s1 `math`에 "$e$는 평균 좌표, $[e,e+1]$은 regularity로 $T_j$의 initial stem 위"를 넣고(`uses`에 `x:decor-eta-regular`), 본문의 ❓를 근거와 함께 해소 문장으로 바꿈 | `decor:conditional-concentration.s4.s1` |
| 불확실점 3 부분 tree의 조건부 독립 | 맞음. trees.tex 20–22, 31–32, 200–201; decorrelation.tex 209, 216–217, 550–551 | `math`에 "prefix(root 포함)"를 넣고 본문의 "원문에 그 형태로 없다"를 근거 목록으로 바꿈 | `x:decor-tree-sampling` |
| 불확실점 4 average-comparisons (iii) | 맞음. tex 509, 520–522, 601·607 | 본문에 사용처를 적음 | `x:decor-average-comparisons` |
| 불확실점 5 product-difference의 축약 부등식 | 맞음. tex 91–92의 $N^{-1}$ 정규화로 $\|\cdot\|_N\le1$; 368, 582–583이 암묵적으로 씀 | 본문에 확인 기록 | `x:decor-product-difference` |
| 불확실점 6 identity-error의 사례 집합 | 맞음. tex 49–53. 카드의 집합은 원문보다 넓은 유한 집합이라 안전 | 본문에 확인 기록 | `decor:identity-error` |
| §8 인터페이스 export 목록 | 맞음(행 번호 일부 어긋남: singleton은 comparison.tex 140, regularity 동치는 141–143, 정규화와 Cauchy–Schwarz는 144–150, 선택된 수열은 130) | `decor:section`의 `provides`에 여섯 카드를 모두 적고, 본문에 항목별 근거(고친 행 번호)를 적음 | `decor:section` |
| 부수: "상태 = 보조 prefix" 단서 누락 | 맞음 | gap에 추가 | `decor:overlap-concentration.s2`, `decor:projection-bound` (그리고 새로 쓴 `decor:conditional-concentration.s2`, `decor:depth-continuity`, `.s1`) |
| 부수: "Ghirlanda–Guerra 형" 이름 | 맞음(tex에 그 이름의 대응 주장 없음). 논문은 perturbations.tex 17–21에서 GG의 self-averaging 논법과 Aizenman–Contucci의 stochastic stability를 "antecedents"로만 든다. introduction.tex에는 GG 언급이 없다 | 두 카드의 physics에서 "GG 형 항등식"을 지우고 "논문이 선행 연구로 드는 계열"로 바꿈. gap에 "논문은 GG 항등식과 같다고 하거나 그것에서 유도하지 않는다"를 적음. s2.s1의 "stochastic stability에서 나오는"도 "섭동 도함수의 집중에서 얻는"으로 바꿈(perturbations.tex 12–16) | `decor:conditional-concentration.s2.s1`, `decor:overlap-concentration.s2` |

## 바꾼 카드 (27개)

`decor:conditional-concentration`, `.s2`, `.s2.s1`, `.s4.s1`, `.s5`, `.s5.s3`, `.s6`, `.s7`, `.s7.s4`;
`decor:overlap-concentration`, `.s2`, `.s4`;
`decor:depth-continuity`, `.s1`, `.s2`, `.s3`, `.s4`;
`decor:projection-bound`, `decor:order-of-limits`, `decor:identity-error`, `decor:section`;
`x:decor-mesh`, `x:decor-topology`, `x:decor-eta-regular`, `x:decor-tree-sampling`, `x:decor-average-comparisons`, `x:decor-product-difference`.

`source` 범위는 하나도 바꾸지 않았다. 모든 카드의 `status`는 `proposed`.

## 받아들이지 않았거나 고쳐서 받아들인 것

- **F3의 대체 문장.** 검토자는 "이 항들에 곱해지는 상수는 $L$에 무관하다"로 바꾸자고 했다. 이 내용은 맞지만(tex 516–517의 $C_{k,\eta}$, 601의 $C_k$, 164–165의 lemma 상수 진술) remark 613–623 자체가 말하는 것은 아니다. 지시대로 `math`는 remark가 말하는 것만 담게 했다: "uniform"은 비용 상계에만 붙이고, 나머지 두 항에는 균등성을 말하지 않는다. 상수의 $L$ 무관성은 본문 메모에 출처와 함께 적었다.
- **F7의 제안 문구.** 검토자 문구 "singleton은 각 $\eta$-regular $d$에서 …"를 그대로 쓰되, 원래 gap의 "$d$는 첫 갈라짐보다 $\eta L$ 넘게 앞" 조건은 $|S|\ge2$에만 붙이고 singleton에는 $d/L\in(\eta,1-\eta)$를 적었다(singleton에는 갈라짐이 없다).
- **불확실점 1의 s3 조건.** 검토자 제안은 "$\eta L\ge1$"이다. s4가 s3을 $\eta/2$-regular 중간 배정에 적용하므로 s3을 일반 $\eta'$로 적고 조건을 "$\eta'L\ge1$"로 두었다(s4에서는 $\eta L/2\ge1$, 큰 $L$에서 성립).
- **§8 인터페이스 행 번호.** 검토자가 적은 comparison.tex 138, 140–143, 146–150, 129는 실제로 140, 141–143, 144–150, 130이다. 고친 번호로 적었다.
- **F4 사실의 근거.** "anchor 혼자인 쪽의 모든 확장이 같은 법칙"은 tex가 한 문장으로 쓰지 않는다. tex 362–363 "In every extension, the marginal target tree consists of two ordinary copies of $S^+$"와 444–445의 단수 표현 "the anchor-alone extension", 그리고 tree 표본 법칙이 모양에만 의존한다는 것(`x:decor-tree-sampling`)에서 읽었다. 카드에 이 근거를 적었다.

## 남은 문제

- `layers/rules.md`는 이 작업에서 고치지 않았다(다른 작업자가 편집 중). P8의 대응 노드와 "Ghirlanda–Guerra 항등식"을 바닥으로 드는 서술은 이번 카드 수정(F1, GG 이름)과 맞춰 볼 필요가 있다. P11은 이미 독립성의 근거를 P9 + 균일 site 선택으로 적고 있어 카드와 일치한다.
- `x:decor-mesh`의 `uses`에 넣은 `cavity:grid`는 cavity.tex의 라벨이다. 검사기는 통과하지만 그 절의 카드가 아직 없다면 그 카드가 생길 때 연결을 다시 봐야 한다.
- 남은 ❓ 표시는 없다.
