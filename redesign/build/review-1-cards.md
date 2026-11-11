# 검토 1 — §7 노드 카드 (독립 검토)

대상: `cards/`의 54개 카드 전부. 기준: `source/sections/decorrelation.tex` (보조로 `trees.tex`, `perturbations.tex`, `comparison.tex`, `cavity.tex`).
아래에서 "확인"은 tex와 직접 대조해 손으로 다시 계산했다는 뜻이고, "의심"은 그렇게 못 한 것이다.

## 요약

- 읽은 카드: 54 / 54 (머리말과 본문 모두). 정리급 7, setup 13, 단계 34.
  (의뢰문은 "setup 14개"라 했지만 나열된 ID는 13개이고 `cards/`에도 13개뿐이다.)
- 수학 진술(`math`)에서 tex와 어긋나는 식, 부호, 지수, 합 범위, 상수는 **찾지 못했다**. 계수 계산($c_d$, $\sum c_\ell$, $-\delta J$, $m_eJ$, $C(S,e)$, 한 층 항등식, 사영된 항등식 재배열, $4p_N$ 비용, fiber bound)은 전부 다시 계산해 맞았다.
- 발견 14건:

| 등급 | 건수 | 번호 |
|---|---|---|
| 틀림 (조건 누락으로 문자 그대로는 성립 안 함) | 1 | F2 |
| 과장 | 3 | F1, F3, F7 |
| 구멍 | 0 | — |
| 누수 | 5 | F4, F5, F8, F9, F10 |
| 유형 오류 | 2 | F6, F11 |
| 표기 | 3 | F12, F13, F14 |

세 부모의 분해(자식 진술 ⇒ 부모 진술)는 모두 성립한다. 숨은 단계는 없고, 자식 본문에만 있는 사실에 기대는 곳이 몇 군데 있다(누수).

## 발견 (심각도 순)

### F1. 과장 — `decor:conditional-concentration` (physics)
- 카드: "cavity method가 '한 상태 안에서 cavity field들은 서로 독립'이라고 가정하는 근거다."
- `math`가 주는 것: $\mathcal A_{L,\eta}v_N(S,d)\to0$, 즉 site 쌍 평균 조건부 공분산 **제곱**의 깊이 평균 (decorrelation.tex:99–100, 236–244). 여러 site의 cavity field가 결합해서 독립이라는 진술은 여기서 나오지 않는다. 논문에서 그 독립성은 정리 7.1(모든 multioverlap 집중)과 균일 site 표본추출에서 나온다 (comparison.tex:98–118 `comp:patterns`, 153 "Apply \cref{decor:overlap-concentration}"). 프로젝트의 `layers/rules.md` P11도 "독립성의 근거는 … P9와 균일한 무작위 site 선택"이라고 적어 이 카드와 어긋난다.
- `gap` (2)는 "$L^2$ 평균의 의미"만 적고 이 초과분을 적지 않았다.
- 수정: 그 문장을 지우거나 "독립성 자체는 이 명제가 아니라 decor:overlap-concentration + comp:patterns에서 나온다. 이 명제는 그 증명의 '상태 안' 절반이다"로 바꾸고 gap에 같은 내용을 넣는다.

### F2. 틀림 (조건 누락, 경미) — `decor:projection-bound` (math, 두 측 형태)
- 카드: "두 측 I, II가 각각 같은 모양 $S$의 사본이고 $e$ 이전에서 갈라졌으면 $\|A^{\rm I}_S\cdot A^{\rm II}_S-a^{\rm I}\cdot a^{\rm II}\|_{L^2}\le2p_N(S,e)$."
- tex: decorrelation.tex:226–228 "For two such sides, both can be projected with total $L^2$ error at most $2p_N(S,e)$". 문맥의 두 측은 aligned depth를 쓰는 사본이다 (26–28, 295–296). 깊이 배정이 다르면 두 측의 $p_N$이 다른 값이어서 상계는 $p_N^{\rm I}+p_N^{\rm II}$이고, 한쪽의 $p_N(S,e)$ 두 배는 일반적으로 성립하지 않는다. 카드도 본문에서는 "aligned depth 때문에 같은 값"이라고 쓰지만 `math`에는 없다.
- 수정: `math`에 "두 측이 같은 깊이 배정(aligned)을 쓰면"을 넣고 `uses`에 `x:decor-eta-regular`를 더한다.

### F3. 과장 — `decor:order-of-limits` (math)
- 카드: "$N$ 극한 후에 남는 오차는 상대 절댓값 비용 상계, 더 작은 모양의 공분산 평균, martingale 추정 $C/L$로 제어되며, **이 셋은 모두 $L$에 균등하다**."
- tex: decorrelation.tex:618–621 "controlled by the uniform relative absolute-cost bound, the lower-order covariance averages, and the martingale estimate $C/L$". "uniform"은 비용 상계에만 붙는다. 공분산 평균 $V_{k-1,L}(\eta/2)$와 $C/L$은 $L$의 함수이고 $L\to\infty$에서 0으로 가는 양이다. "균등"은 원문에 없는 주장이다.
- 수정: "이 항들에 곱해지는 상수는 $L$에 무관하다"로 바꾼다.

### F4. 누수 — `decor:conditional-concentration.s6`
- `math`의 식에 $\delta\,\mathbb Ef\,\mathbb ER_{\rm target}$이 나오려면 "anchor 혼자인 쪽의 모든 확장이 같은 법칙의 target($d$에서 분리된 $S^+$ 두 사본)을 주므로 합이 $-\delta J\,\mathbb ER_{\rm target}$로 묶인다"가 필요하다 (tex 418–419, 444–445). s5의 `math`는 총 계수 $-\delta J$만 주고, 법칙이 같다는 사실은 s6 **본문**에만 있다. 부모 뼈대에도 없다.
- 수정: s5 또는 s6의 `math`에 한 문장으로 올린다.

### F5. 누수 — `decor:overlap-concentration.s4`, `decor:conditional-concentration.s7.s4`
- 고정 배정마다의 $o_N(1)$ ($\operatorname{Var}(M)\to0$, $\varepsilon_{N,L,k}\to0$)을 깊이 평균 뒤로 넘기는 단계("고정 $L$에서 $\mathcal A_{L,\eta}$는 유한 합이므로 $\limsup_N\mathcal A\le\mathcal A\limsup_N$")가 두 카드 모두 본문에만 있다. tex는 이를 decor:identity-error 주변(49–52)과 remark(616–618)에서 말한다. 극한 순서가 이 절의 핵심 gap이므로 `math`에 있어야 한다.

### F6. 유형 오류 — `decor:depth-continuity` (`abstraction: intuition`)
- physics의 앞 세 문장("상태 평균은 깊이에 대해 평균적으로 연속…")은 `math`의 정확한 약화이고 이 lemma는 논증에 쓰인다. SCHEMA의 `intuition`은 "논증에 쓰이지 않는 그림"이다. 그림에 해당하는 것은 마지막 문장($q(x)$ 단조 유계)뿐이다.
- 수정: `weakening`으로 두고 $q(x)$ 문장은 본문으로 옮기거나 gap에서 "그림"이라 밝힌다. 덧붙여 `depth-continuity.s1`에는 정직한 대응이 있다: $\sum_t\mathbb E\|\mu_{t+1}-\mu_t\|_N^2=\mathbb E\|\mu_{\rm last}\|_N^2-\mathbb E\|\mu_{\rm first}\|_N^2$, 즉 깊이별 자기 overlap $\mathbb E\|\mu_t\|_N^2$의 증가분 합이 1 이하라는 것. 현재는 null이다.

### F7. 과장 (gap이 부정확) — `decor:conditional-concentration` (gap (1))
- 카드: "고정 깊이 $d$와 고정 깊이 배정마다가 아니라 … 평균 $\mathcal A_{L,\eta}$로만 성립한다."
- tex: singleton에서는 점별로 증명된다. decorrelation.tex:288–289 "$v_N(S,d)\le\delta/\eta+o_N(1)$ at each fixed $L,d$". 카드 s2도 그렇게 쓴다. "평균으로만"은 $|S|\ge2$에만 맞다.
- 수정: "$|S|\ge2$에서는 평균으로만. singleton은 각 $\eta$-regular $d$에서 $\limsup_Nv_N\le1/(\eta L)$."

### F8. 누수 — `decor:depth-continuity.s2`
- `math`가 첫 갈라짐이 아닌 임의 branching vertex에서 $\mathscr F_q$, $\mu_{q,T_j}$를 쓴다. `decor:covariance-definition`은 $S$의 initial stem 위에서만 이들을 정의하고, `x:decor-topology`는 첫 vertex의 자식 모양만 "root부터 stem을 공유하는 모양"으로 읽는다고 적는다. 깊은 vertex의 자식 모양에 대한 같은 약속이 어느 `math`에도 없다. s2의 `uses`에 `decor:covariance-definition`도 없다(s1을 거쳐 간접).
- 수정: `x:decor-topology`의 `math`에 "임의의 branching vertex $v$ 아래 부분 모양은 root에서 $v$까지의 경로를 stem으로 갖는 topology로 본다"를 넣는다.

### F9. 누수 — `decor:depth-continuity.s3`의 "$L\ge L_0$"
- `math`에 "$L\ge L_0$"가 근거 없이 들어 있고 이유는 본문의 ❓뿐이다. 해소는 아래 "작성자 표시 불확실점" 1번.

### F10. 누수 — `x:decor-mesh` (`uses: []`인데 "$L\ge2$")
- decorrelation.tex:4에는 $L\ge2$가 없다. 출처는 perturbations.tex:257 "For every fixed $L\geq2$"와 cavity.tex:16이다. `uses`가 비어 있어 근거를 따라갈 수 없다. 거짓은 아니다.
- 수정: "$L\ge2$"를 `x:decor-limit-order`로 옮기거나 `uses`에 `pert:selection`을 넣는다.

### F11. 유형 오류 — `decor:conditional-concentration.s2` (physics null)
- 기저 단계에는 분명한 물리 대응이 있다: "고정 $L$, 각 깊이 $d$ ($d/L>\eta$)의 상태 안에서 단일 spin의 connected correlation 제곱 평균은 $N\to\infty$에서 $1/(\eta L)$ 이하"다. 깊이 평균 없이 성립한다는 점에서 부모보다 강한 정보이고 F7과 직결된다. 자식 s2.s1에는 physics가 있는데 결론을 담은 s2에는 없다.

### F12. 표기 — `x:decor-mesh` (physics)
- "$L$단계 계층"이라 썼다. cavity.tex:16 "use $r=L-1$ auxiliary levels", `layers/rules.md` "$r=L-1$단 RSB"와 맞추면 "깊이 $L$, $(L-1)$단 RSB"다.

### F13. 표기 — 행 번호
- `x:decor-eta-regular` 본문 "trees.tex 452–458" → regular shape 정의는 460–467 (452는 tree:charging 증명 안). trees.tex:462는 $0<\eta<1/2$로 제한하고 465는 "A singleton is regular"를 명시한다. 둘 다 카드에 없다(§8은 $0<\eta<1/2$만 쓰므로 문제는 없다).
- `decor:section` provides "comparison.tex 123–158" → comp:shape-error 논증은 122–156, 명제는 160부터.

### F14. 표기 — `decor:projection-bound` (physics)
- "각 가지의 spin 곱을 그 상태의 평균(**국소 자화의 곱**)으로" — $\mu_{e,T_j}$가 국소 자화인 것은 $T_j$가 singleton일 때뿐이다. 일반적으로는 $T_j$의 replica들 spin 곱의 상태 평균이다.

## 작성자 표시 불확실점

1. **`decor:depth-continuity.s3`, "$L\ge L_0$"의 출처 — 정정.** tex가 "large $L$"을 실제로 부르는 곳은 s3의 범위(194–199)가 아니라 s4의 범위다: 201–203 "Regularity ensures that the intermediate shapes have the same ancestry relations and, for large $L$, lie in the enlarged $\eta/2$-regular domain". 즉 여러 이동의 중간 모양이 $\eta/2$-regular이어야 한다는 조건이다. 작성자의 추측(늦춘 $q+1$이 자식의 다음 갈라짐보다 앞)은 이동 하나에서도 실제로 필요한 조건이지만 약하다: $\eta$-regular이면 $q'-q>\eta L$이므로 $\eta L\ge1$이면 $q+1<q'$이고 $q+1\le L-1$이다. 이것은 내가 계산한 것이고 tex에는 적혀 있지 않다. 제안: s3은 "$\eta L\ge1$" (작성자 유도로 표시), s4는 tex 그대로 "$L$이 크면 중간 배정이 $\eta/2$-regular".
2. **`decor:conditional-concentration.s4.s1`, $e$가 평균 좌표여야 함 — 확인.** lemma는 "If $d$ ranges along an initial unary stretch … this average includes $d$" (155–162)를 요구한다. $e$가 평균 좌표라는 것은 492–493 "$D=b(S)+1$ distinct depth coordinates, including $d$ and $e$"에 있고, 같은 논법을 정리 증명이 명시한다: 588–589 "Here $e$ is itself a ranged coordinate, so the one-step increments are summed before division by $L$". $[e,e+1]$이 $T_j$의 initial stem 위라는 것은 regularity에서 나온다. ❓를 지워도 된다.
3. **`x:decor-tree-sampling`, 부분 tree의 조건부 독립 — 확인 (유도로서 옳음).** 근거: trees.tex:21–22 (kernel은 prefix 전체에 의존), 32–33 "different children are drawn independently", 200–201 "Conditional independence of children and the projectivity of tree sampling". decorrelation.tex도 이 형태로 쓴다: 209, 216–217 "independent of the continuation of $S$ given its prefix at $e$", 550–551. prefix에 root가 포함된다는 점만 `math`에 한 번 더 적으면 좋다.
4. **`x:decor-average-comparisons` (iii) — 확인.** 참이고 실제로 쓰인다: 509 "The unshifted term has the same bound without translating the coordinates" ($\eta$-regular ⊂ $\eta/2$-regular), 520–522의 흡수($V_{k-1,L}(\eta)\le V_{k-1,L}(\eta/2)$), 601·607의 $\gamma=1/2$ 적용.
5. **`x:decor-product-difference`, $|x\cdot y-x'\cdot y'|\le\|x-x'\|_N+\|y-y'\|_N$ — 확인.** $x\cdot y$가 $N^{-1}$로 정규화되어 있어 (tex 91–92) $[-1,1]^N$ 벡터의 $\|\cdot\|_N\le1$이고, $(x-x')\cdot y+x'\cdot(y-y')$에 Cauchy–Schwarz를 쓰면 된다. 좌표별 곱 형태 $\|\prod x_j-\prod y_j\|_N^2\le s\sum\|x_j-y_j\|_N^2$도 맞다. tex 368, 582–583이 암묵적으로 쓴다.
6. **`decor:identity-error`, "finite collection" → "$k$로 유계인 크기" — 확인.** tex 49–53: "finitely many labeled topologies of any bounded size and, at fixed $L$, only finitely many assignments of their depths … any of the finite collections used below … $\varepsilon_{N,L,k}$". 실제로 쓰이는 사례(leaf $\le2k$, color $\le2k-1$, $f$는 특정 overlap 단항식)는 모두 카드의 집합 안에 있다. 카드의 집합은 원문보다 넓게 잡은 유한 집합이므로 안전한 쪽이다.

## 인터페이스 시험 (부모 카드 + 직계 자식의 `math`만 읽음)

- **`decor:overlap-concentration` — 통과.** s1 → singleton. s2 ($\operatorname{Var}(M)\to0$) + s3 ($G$, $G_-$) + s4 (추정) + s5로 증명 개요가 닫힌다. 본문을 열어야 했던 곳: F5 하나($\limsup_N$과 깊이 평균의 교환). $V_{k-1,L}$과 fiber bound는 다른 부모의 카드지만 s4의 `uses`에 있어 규약상 문제없다.
- **`decor:conditional-concentration` — 통과.** s1–s7의 `math`만으로 귀납 구조(기저, 구성과 상대 비용, 사영, class별 계수, 사영된 항등식, 점화식)를 재구성했다. 본문을 열어야 했던 곳: F4(anchor 혼자인 쪽의 묶음). s7의 `math`는 결론뿐이라 s6에서 s7로 가는 길은 부모 뼈대의 문장과 s7의 자식들에 의존하는데, s7이 자체 부모이므로 규약 위반은 아니다.
- **`decor:depth-continuity` — 통과.** 둘째 부등식은 s1, 첫째는 s2 → s3 → s4, "더 큰 tree"는 s4. 본문이나 tex를 열어야 했던 곳: F8($\mathscr F_q$의 의미), F9($L_0$의 출처).

세 부모 모두 자식 진술 + 부모 `uses`가 부모 진술을 함의한다. `구멍`은 없다.

## §8 인터페이스

comparison.tex에서 §7을 쓰는 곳은 122–156 한 군데다 (153 `\cref{decor:overlap-concentration}`; 208–211은 comp:shape-error를 거쳐 간접). 거기서 필요한 것:

1. 모든 $U\in\mathfrak S_k$ ($[k]$의 공집합 아닌 부분집합 위의 labeled topology)에 대한 정리, 각 고정 $0<\eta<1/2$ — `decor:overlap-concentration`의 `math`에 있음.
2. singleton은 좌표 없는 평균 (comparison.tex:138) — 있음.
3. $\mathcal A_{L,\eta}$가 정규화 $L^{-a'}$의 비정규 평균이고 질량 $\le1$ (146–150, Cauchy–Schwarz) — `decor:average-definition`에 있음.
4. §7의 $\eta$-regular가 trees.tex:462–465의 regular와 같은 조건 (140–143) — `x:decor-eta-regular`.
5. $\operatorname{Var}(R_U)$가 고정 깊이 배정에서 root를 포함한 분산 — `x:decor-spin-product`.
6. 안쪽 극한이 고정 $L$의 선택된 수열을 따름 (129, 153–155) — `x:decor-limit-order`.

판정: §8은 선언된 두 export의 `math`와 그 `uses`에 없는 것을 §7에서 가져가지 않는다. 다만 4–6은 두 export 카드 자체가 아니라 그 `uses`에 있으므로, export 목록을 `decor:overlap-concentration`, `decor:average-definition`, `x:decor-eta-regular`, `x:decor-topology`, `x:decor-spin-product`, `x:decor-limit-order`로 적는 것이 정확하다. 유도된 subtree의 법칙이 단독 사본과 같다는 것(projectivity)은 §7이 아니라 trees.tex:38–39, 482–483에서 온다.

## physics 칸 점검 (non-null 13개)

- gap이 다섯 항목(깊이 평균/점별, 극한 순서, 보조 계층, 모든 multioverlap, 극한값 미식별)을 모두 갖춘 카드: `decor:section`, `decor:overlap-concentration`.
- 고칠 곳: F1, F6, F7, F11, F12, F14.
- 경미한 gap 누락: `decor:overlap-concentration.s2`와 `decor:projection-bound`의 gap에 "상태 = 보조 계층의 prefix"라는 단서가 없다(부모와 정의 카드에는 있다).
- 유형이 맞다고 본 것: `decor:contractions` (weakening), `decor:average-definition` (intuition), `decor:covariance-definition`, `x:decor-topology` (exact, "상태 = prefix" 사전을 전제로).
- `conditional-concentration.s2.s1`과 `overlap-concentration.s2`의 "Ghirlanda–Guerra 형"은 `rules.md`가 스스로 "확신이 낮은 대응"으로 적은 것이다. 나도 tex에서 뒷받침을 찾지 못했다 (미해결).
- 억지 physics: 없다고 본다. `x:decor-eta-regular`, `decor:order-of-limits`, 계수 단계들의 null은 적절하다.

## 완전히 맞다고 본 카드

tex와 줄 단위로 대조해 `math`에서 고칠 것을 찾지 못한 카드:

- 정리급: `decor:overlap-concentration`, `decor:contractions`, `decor:depth-continuity` (math), `decor:section` (math).
- setup: `x:decor-limit-order`, `x:decor-tree-sampling`, `x:decor-topology`, `x:decor-eta-regular` (math), `decor:average-definition`, `decor:identity-error`, `x:decor-spin-product`, `decor:covariance-definition`, `decor:projection-definition`, `decor:average-holder`, `x:decor-average-comparisons`, `x:decor-product-difference`.
- 정리 7.1 단계: s1, s2, s2.s1, s2.s2, s3, s5.
- lemma 단계: `decor:contractions.s1`, `.s2`, `decor:depth-continuity.s1`, `.s4`.
- 명제 7.4 단계: s1, s2.s1, s2.s2, s3, s3.s1, s3.s2, s3.s3, s4, s4.s1, s4.s2, s5, s5.s1, s5.s2, s5.s3, s7, s7.s1, s7.s2, s7.s3.

## 검토하지 않은 것

- 카드 중 읽지 않은 것은 없다.
- 하지 않은 것: `layers/L0.md`, `L1.md`는 읽지 않았다. `rules.md`는 P8, P9, P11만 대조했다. `uses`에 든 §3, §6 노드의 카드가 있는지는 보지 않았고 tex 원문만 봤다. `provides` 문구는 행 번호만 확인했다. 원 논문 자체의 증명이 옳은지는 카드와 대조하는 범위에서만 따라갔다.

## 확정 전에 사용자가 직접 봐야 할 것

1. F1: "cavity field 독립의 근거"를 명제 7.4에 둘지 정리 7.1 + comp:patterns에 둘지. `rules.md` P8/P11과 맞춰야 한다.
2. F2: 두 측 사영 형태에 aligned 조건 추가.
3. F3: remark의 "셋 모두 $L$에 균등" 문장.
4. 불확실점 1: `depth-continuity.s3`의 $L_0$를 "$\eta L\ge1$ (작성자 유도)"로 적을지, s4로 옮길지.
5. F7 + F11: singleton은 깊이 평균 없이 성립한다는 사실을 gap과 physics에 드러낼지.
6. "Ghirlanda–Guerra 형"이라는 이름을 카드 두 곳에 남길지 (tex 근거 없음).
