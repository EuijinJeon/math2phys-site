# 검토 2 대응 — §10 consequences와 overview

대상 보고서: `build/review-2-cons-overview.md` (지적 10건: 중간 1, 낮음 9)와 항목별 의견(L1 대응표, `model:section` 에 overview 걸기, 137행과 `\ref` 없는 사용, L0, 짝수 체수).
기준: `source/sections/consequences.tex` 전체, `overview.tex` 전체, `decorrelation.tex` 1–95·270–300·326–360·520–623, `trees.tex` 300–340·495–525, `perturbations.tex` 425–440, `upper.tex` 66–92·115–128, `model.tex` 1–6. 원문 전체에서 "even"을 grep으로 찾았다. 지적마다 원문 줄을 직접 열어 다시 대조했다.

결과: 반영 8, 좁혀서 반영 2(F1, F6), 기각 0. 짝수 체수 지적은 맞았고 §10 카드 다섯 곳에 반영했다. L1 수 1과 수 5에 한 구절씩 넣었다. `model:section` 에는 overview를 걸었다(다른 일을 모두 끝낸 뒤, 고치기 직전에 다시 읽고 다섯 곳만 바꿈).

중단 확인: 다시 시작할 때 `cards/`·`layers/`에서 검토 보고서(18:41)보다 새로운 파일이 없었다. 중단 전에 고친 것은 없었고, 일부만 고쳐진 파일도 없었다.

## 건별 표

| 번호 | 판정 | 한 줄 근거 | 고친 파일 |
|---|---|---|---|
| F1 (중간) | 좁혀서 반영 | overview 45–46 "No uniform concentration in the depth is needed"의 "the depth"는 원문이 특정하지 않는다. branching 깊이로 읽으면 decorrelation.tex 11–13·81–83과 trees.tex 516–524, 계층 깊이 $L$ 로 읽으면 decorrelation.tex 568–569·621–622와 맞는다. 둘 다 본문에서 참이므로 두 읽기를 작성자 읽기로 밝히고 둘 다 가리켰다 | `x.overview-closing.md` (표 2·3행, gap (5)), `x.overview-strategy.md` (표 C3) |
| F2 | 반영 | perturbations.tex 434–436 "prescribes any consistent collection of their pairwise split depths, involving only the added colors and the anchor. It imposes no extra restrictions involving the other old replicas". overview 22 "select any prescribed branching pattern". 표 2c의 따옴표 문구는 지금 L1 23행에 없다 | `x.overview-step2.md` (math "임의의", gap (1), 표 2행), `x.overview-strategy.md` (표 2c) |
| F3 | 반영 | decorrelation.tex 81–83 "concentrate the remaining conditional mean at each fixed depth. Averaging over depths is essential when combining the two estimates", 564–569 "$\operatorname{Var}(M)\to0$ at each fixed $L,S,e$". 잎 하나인 경우는 72–74, 287–290 | `x.overview-step3.md` (gap (1), 표 1행) |
| F4 | 반영 | rules.md P11 주의 "'상관 감쇠와 무관하다'고 읽으면 안 된다 … 쓰이지 않는 것은 그래프 거리에 따른 상관 감쇠다" | `x.overview-step4.md` (gap (2)) |
| F5 | 반영 | introduction.tex 75–77 "no ultrametric organization of the physical Gibbs states is assumed". 논문은 그 가정의 내용을 증명하지 않고, 가정 없이 같은 공식에 이른다 | `x.overview-strategy.md` (physics 마지막 문장) |
| F6 | 좁혀서 반영 | 88–91은 $g$ 를 $\beta$ 없이 최댓값의 $N$ 극한으로 정의하고, 108–110의 끼움에서 각 $N$ 마다 $g_N=\lim_\beta P_N(\beta)/\beta$. "두 순서가 같은 값을 준다"는 원문이 쓰지 않는 문장이라 작성자 읽기로 적었다 | `models.ground.md` (gap (1)), `models.section.md` (표의 한정어 칸) |
| F7 | 반영 | 81 $Z_N(\beta)=\sum_\sigma e^{\beta\mathcal E_N}$ 이라 inf$/\beta$ 의 극한은 $g$ 이고 ground-state 에너지 밀도는 $-g$ 다. 기대값의 밀도다(90행 $\mathbb E\max$) | `models.section.md` (physics) |
| F8 | 반영 | 39 "independent fair signs" | `models.sat.md` (physics) |
| F9 | 반영 | (a) `models:spin` 본문이 짝수 $p$ 를 (2.1)의 전제로 읽히게 했다. (b) $\max_s\lvert f\rvert=1$ 은 원문에 없다. (c) 3-SAT remark의 이유 설명과 "같은"은 원문 132–137에 없다 | `models.spin.md` (본문), `models.section.md` (본문), `x.cons-3sat-remark.md` (본문, physics) |
| F10 | 반영 (ID 그대로, 조율에 넘김) | SCHEMA 20행의 `x:<섹션 접두어>-…` 대로면 `x:models-*` 이지만, §2의 `x:model-*` 와 한 글자 차이라는 이유가 타당하고 검사도 통과한다. ID를 바꾸지 않는다 | 없음 (아래 "조율 세션에 넘기는 것") |
| 짝수 체수 | 반영 | §10의 증명은 짝수를 쓰지 않는다($x=\pm1$ 이면 $e^{\beta Jx}=\cosh\beta J(1+x\tanh\beta J)$ 는 홀짝과 무관). 원문 전체에서 "$p$ is even"을 쓰는 곳은 upper.tex 123–124뿐이다 | `models.section.md` (gap (1), 표 아래 한 문단), `models.spin.md` (본문), `models.spin.s3.md`, `models.sat.s3.md` (gap), `x.cons-3sat-remark.md` (본문에 줄 번호) |
| L1 수 1·수 5 | 반영 | overview 4–6, 27–29, 32–33과 upper.tex 70–91, decorrelation.tex 337–359, 81–83, 562–569 | `layers/L1.md` (아래 "L1에 넣은 문구") |
| `model:section` 에 overview 걸기 | 반영 | graph.json의 `model:section` 범위에 overview.tex 1–51이 든다. SCHEMA "모든 카드는 원문 범위에 닿아야" | `model.section.md` (다섯 곳), `x.overview-strategy.md` (본문 "위치"), `models.section.md` (본문) |
| 137행과 `\ref` 없는 사용 | 반영 | 137 "its trial functional differs from \eqref{model:functional}"은 비교다. $\mathcal B_{r,\beta}$ 는 82–84에서 정의된다 | `model.section.md` (표 한 행, 문장 하나) |

## 상세 근거

### F1 — "the depth"의 두 읽기

원문 43–46: "The estimates in Step~3 are averages over separated interior branching depths. The insertion expansion assigns vanishing probability to the exceptional trees, so these averages are sufficient for Step~4. No uniform concentration in the depth is needed."

- **읽기 (a) branching 깊이.** 앞 두 문장이 branching 깊이 평균과 그것으로 충분하다는 것을 말하므로, "깊이 배정마다 균일하게(점별로) 집중할 필요는 없고 깊이 평균이면 된다"로 읽힌다. 본문의 짝: decorrelation.tex 11–13("concentration of every finite multioverlap, averaged over separated interior branching depths. These are the averages needed for the comparison"), 82–83("Averaging over depths is essential when combining the two estimates"), trees.tex 516–524(`tree:averaging-remark`, "this allows averaged estimates on regular depth assignments to be used in the logarithmic expansion"). 카드의 `physics` 와 `x:overview-strategy` 표 C3가 이 읽기를 했다.
- **읽기 (b) 계층 깊이 $L$.** overview 자신이 3행 "every finite depth", 14행 "each fixed hierarchy depth"에서 "depth"를 $L$ 로 쓴다. 그러면 "$L$ 에 균일한 집중(수렴 속도)은 필요 없다"이고 본문의 짝은 decorrelation.tex 621–622(`decor:order-of-limits`, "No rate of convergence in $N$ uniform in $L$ is used")와 568–569("Division by $C(S,e)$ is made only at fixed $L$; no uniform lower bound as $L\to\infty$ is needed")다.
- 문법으로는 정할 수 없고, 두 진술 모두 본문에서 참이다. 검토자 말대로 표가 카드의 `physics` 와 다른 읽기를 가리키고 있었으므로 이 어긋남은 고쳤다. 다만 대상을 (a)로 **바꾸는** 대신 두 읽기를 모두 적었다. 이 점에서 좁혀서 반영이다. `physics` 는 (a)를 따르며, gap (5)가 이것을 밝힌다. `math` 는 원문처럼 모호한 그대로 두었다("깊이에 대해 균일한 집중은 필요 없다").
- 2행에 [[tree:averaging-remark]]를 더한 것은 검토자 제안 그대로다(44–45행의 직접적인 본문 짝).

### F3 — 확인

decorrelation.tex 562–569에서 `decor:prefix-projection-concentration` $\operatorname{Var}(M)\to0$ 은 "at each fixed $L,S,e$"이다. 깊이 평균은 그 뒤 586 $\mathcal A_{L,\eta}\mathbb E(G-G_-)^2\le C_k/L$ 과 599–603의 결합에서 들어온다. 그래서 "두 결론 모두 깊이 평균"은 틀리게 읽힌다. 검토자가 짚은 잎 하나인 경우도 확인했다. 조건부 공분산 쪽은 287–290 "$v_N(S,d)\le\delta/\eta+o_N(1)$ at each fixed $L,d$", multioverlap 쪽은 72–74 "$\operatorname{Var}(R_S)\to0$ … at every fixed $L$"이다. gap (1)을 이 셋으로 나누어 다시 썼다.

### F6 — 좁힌 까닭

검토자 제안은 "따름정리는 두 순서가 일치함을 말한다"였다. 원문 88–100은 (i) $g$ 의 존재, (ii) (10.1), (iii) 폭 $[g,g+\log2/\beta]$ 만 말한다. "각 $N$ 마다 $g_N=\lim_\beta P_N(\beta)/\beta$"는 108–110의 끼움에서 $\beta\to\infty$ 로 보내면 나오지만 원문에 적혀 있지 않다. 그래서 "(작성자 확인)"으로 적었다. "두 극한 순서가 같은 값을 준다"는 그 확인과 (10.1)을 합친 해석이므로 "(작성자 읽기; 원문은 이렇게 적지 않는다)"로 적었다. 이렇게 해서 원문보다 많이 말하지 않는다. 좌변 $g$ 가 $\beta$ 없이 정의된 양이라는 핵심은 그대로 넣었다.

### 짝수 체수 — 확인

`grep` 결과 "even"이 체수의 뜻으로 나오는 곳은 consequences.tex 10, 12, 36, 38, 48, 132(진술과 remark), introduction.tex 19, 27, 30, model.tex 3(고정), upper.tex 123("Since $p$ is even")뿐이다. §10의 증명(24–34, 51–64, 103–125)에는 없다. 손으로도 확인했다: spin 전개는 $\prod_\ell s_\ell=\pm1$ 에만 기대고, SAT 전개와 (2.4), (2.1)의 확인에도 홀짝이 들어가지 않는다. §10 카드에서 "짝수 체수를 여기서 확인한다"고 읽히던 곳은 `models:section` gap (1)("가정(…, 짝수 체수)을 확인하고")과 `models:spin` 본문("이것이 (2.1)–(2.4)와 함께 model:integrability의 전제다")이었다. 둘을 고치고, `models:section` 표 아래와 `models:spin` 본문에 "쓰이는 곳은 upper.tex 123–124의 볼록성([[upper:remainder]])"이라는 한 줄을 넣었다. 두 `.s3` 단계 카드의 "진술에서 고정되어 있다"에도 같은 괄호를 붙였다.

### F9 — 문구

- `models:spin`: "짝수 $p$ 는 (2.1)–(2.4)와 함께 주정리의 전제이고, 그 고정은 [[model:integrability]] 카드(model.tex 3행)가 담는다."
- `models:section`: "$\max_s\lvert f(s)\rvert=1$ 이다(작성자 확인; 원문에 없다)."
- `x:cons-3sat-remark`: 본문의 이유 설명 끝에 "이 설명은 작성자 읽기다". `physics` 의 "같은 Poisson 개수·복원추출 앙상블"을 "같은 종류의 … (원문 134–136행은 '…'라고만 한다)"로 낮췄다. ❓ 두 곳("finite rational trials", "sign-indexed message pairs")은 그대로 두었다.

### `model:section` 에 overview 걸기

지시대로 다른 일을 모두 끝낸 뒤, 고치기 직전에 `cards/model.section.md` 를 다시 읽었다. 그 사이 다른 에이전트가 "§8·§9가 `\ref` 없이 쓰는 §2 정의" 문단을 넣어 두었고, 그것은 건드리지 않았다. 바꾼 곳은 다섯 곳이다.

1. `children` 끝에 `x:overview-strategy`.
2. `source` 에 `{file: overview.tex, lines: [1, 51]}`.
3. `math` "받는 것": "소절 2.2 증명 전략(overview.tex, x:overview-strategy)은 뒤 섹션을 예고할 뿐 기대지 않는다." 한 문장.
4. "밖에서 이 섹션을 쓰는 곳" 표의 [[model:functional]] 행: "consequences.tex 83 ($\mathcal B_{r,\beta}$), 137 (Remark 10.4: 동반 논문의 functional이 (2.11)과 다르다는 비교)".
5. "기호로만 쓰는 곳" 문장 끝에 §10의 `\ref` 없는 사용(25–33·52–63 가정 확인, 32·63 $B(\theta)$, 68–77 $M_N$·$i_{\ell,k}$, 95·114 $r\ge0$). 그리고 본문 끝 "**overview.tex.**" 문단의 "이 카드 묶음은 model.tex만 다룬다"를 "그 소절은 x:overview-strategy와 그 자식 카드가 다루고, 이 카드는 그것을 마지막 자식으로 둔다"로 바꿨다(검토자의 "함께 고칠 문장" 셋째).

함께 고칠 문장의 나머지 둘: `x:overview-strategy` 본문 "위치" 문단("자식으로 두지 않는다 … 고치지 않았다" → 걸었다는 사실), `models:section` 본문의 "그 카드는 이 작업에서 고치지 않았다" → 고쳐 넣었다는 사실.

## L1에 넣은 문구 (전후 대조)

원문 근거: overview 4–6("including a normalization that avoids assuming integrability of the multiplier $\log a$"), upper.tex 70–91("We remove $a$ before taking expectations, so no integrability of $\log a$ is needed. … $c=\theta(1,\ldots,1)$ … $0<\lambda<1$ … $\lambda\uparrow1$"); overview 27–33, decorrelation.tex 337–338("At each vertex the $j=1$ factor is $-\delta$"), 342(`decor:J-lower-bound`), 348–359(`tree:charging`, `decor:relative-absolute-cost`, "This is the reason for the shift"), trees.tex 330–332(늦추면 계수 $-\delta$), decorrelation.tex 81–83·562–569(marker anchor, 각 고정 깊이).

**수 1 "무엇을 하는가"**

- 전: "… 모든 $N$ 과 모든 시행값에서 $F_N\le\mathcal B_r$ 이 나오고, 이 부등식이 마지막 수 7로 간다."
- 후: "… 이 부등식이 마지막 수 7로 간다. $\log a$ 의 적분 가능성은 가정하지 않는다: 상수 $c=\theta(1,\ldots,1)$ 을 빼고 매개변수 $\lambda\uparrow1$ 로 정규화해 피한다([[upper:regularization]])."
- 근거 노드에 [[upper:regularization]] 추가.

**수 5 "무엇을 하는가" 첫 문장**

- 전: "수 4의 항등식에 잎 개수 귀납을 걸어 상태 안 [[g:conditional-decorrelation|조건부 decorrelation]]($\mathcal A_{L,\eta}v_N(S,d)\to0$, [[g:conditional-covariance]])을 얻고, 이어서 $R_S$ 가 branching pattern으로 정해진다는 것을 얻는다."
- 후: "수 4의 항등식에 잎 개수 귀납을 걸되, target tree의 내부 branching 깊이를 한 칸씩 늦춘다([[g:depth-delay|깊이 미루기]]): 늦춘 깊이마다 첫 fresh split이 정규화 계수와 같은 작은 인자 $\delta=1/L$ 을 내고, 절댓값 계수 합의 상대 한계([[tree:charging]])가 나눈 뒤의 오차를 제어한다([[x:overview-step3]]). 이렇게 상태 안 [[g:conditional-decorrelation|조건부 decorrelation]](…)을 얻고, 이어서 marker anchor를 쓴 두 번째 항등식으로 남은 조건부 평균을 각 고정 깊이에서 집중시켜 $R_S$ 가 branching pattern으로 정해진다는 것을 얻는다."
- 근거 노드에 [[tree:charging]] 추가.
- 마지막 문단의 "[[g:depth-delay|깊이 미루기]]로"는 용어의 첫 등장이 수 5로 옮겨졌으므로 "깊이 미루기(수 5)로"로 바꿨다(문서마다 첫 등장에 한 번 건다는 규약).

검토자 제안보다 짧게 썼다. 계수의 세부는 [[x:overview-step3]]와 [[tree:charging]]을 가리키고 풀어 쓰지 않았다(원칙 7). 검토자 문안의 "정규화 계수와 같은 크기가 되고"는 overview 28–29의 "the same small factor"보다 강하게 읽힐 수 있어 원문 표현("같은 작은 인자")을 따랐다. 수 4의 "계수 한계(P6)"(검토자의 확신 낮은 셋째 제안)는 지시 범위 밖이고 rules.md와 맞물린 일이라 고치지 않고 넘긴다. L1에는 승인 표시가 없다.

## 확정된 이름과 원칙 점검

- 새로 쓴 문장에 Ruelle, Ghirlanda–Guerra, stochastic stability, ultrametricity, "clustering", "self-average", "connected correlation", R번호가 없다. "상태"는 L1 수 5의 "상태 안"(기존 문구) 하나이고 `g:state` 뜻이다.
- "조건부 decorrelation", "집중", "prescribed-tree 항등식", "선택된 수열", 주어 "조건부 공분산"을 그대로 썼다.
- 원문에 없는 확인과 해석에는 "작성자 확인"·"작성자 읽기"를 붙였다(F1 gap (5), F6, F9).
- 모든 카드의 `status` 는 `proposed` 그대로다.

## 검사

```
python3 redesign/tools/check.py --sections decorrelation,model,trees,upper,cavity,perturbations,comparison,reduction,consequences,overview --out /tmp/check-co-fix.md
```

`model.section.md` 를 고치기 전과 후에 두 번 돌렸다. 두 번 다 형식·정초·포함·의존·연결·순환·사전·단면·용어 모두 통과했고, 오류 0, 경고 0이었다. 검토 보고서가 적은 comparison.tex 227의 의존 경고 2건은 이번 실행에서 나오지 않았다(그 사이 다른 작업에서 고쳐진 것으로 보인다. 이 작업은 그 카드를 건드리지 않았다). 검사 도구는 도중에 깨지지 않았다.

## 조율 세션에 넘기는 것

1. **SCHEMA 예외 기재 (F10).** SCHEMA.md "노드 ID"에 한 줄 추가를 제안한다: "§10은 라벨 접두사 `models:` 가 §2의 `model:` 과 헷갈리므로 라벨 없는 노드를 `x:cons-*` 로 쓴다." ID는 바꾸지 않았다.
2. **증명 지도에서 overview → `main:theorem` 간선.** overview 카드 두 장(`x:overview-strategy`, `x:overview-closing`)이 `main:theorem` 을 `uses` 에 넣은 것은 그대로 두었다(overview.tex 50 `\cref{main:theorem}` 이 의존 검사에 걸리고, 원문 순서상 예고가 아니다). 전략 요약이 자기가 요약하는 정리에 "기대는" 것으로 그려지지 않도록, DAG를 그릴 때 overview 묶음을 빼거나 간선 종류를 달리해야 한다. 이제 `x:overview-strategy` 가 `model:section` 의 자식이므로 지도에서 그 묶음의 위치도 함께 정해야 한다.
3. **L0의 "Viana–Bray 모형" (고치지 않음).** L0 본문 7행 "[[g:named-models|Viana–Bray 모형]], 대칭 coupling의 diluted 짝수 $p$-spin 모형, …"은 대칭 한정어가 뒤 항목에만 걸려 읽힌다. 원문 서론(introduction.tex 29–31)이 같은 식으로 나열하므로 틀림은 아니다. 같은 문단 뒤쪽은 "대칭 coupling의 diluted 짝수 $p$-spin 모형(Viana–Bray 포함)"으로 쓴다. L0은 이 작업의 쓰기 범위 밖이다.
4. **용어집 (쓰기 범위 밖).** (a) `g:ground-state` 정의 위치에 `x:cons-energy-score`(consequences.tex 66–84, $\mathcal E_N$ 의 정의) 추가. (b) `g:factorization` 물리 대응 칸 "Viana–Bray에서 $a=\cosh\beta J$ …"를 "`models:spin` 의 모형에서(Viana–Bray는 $p=2$)"로(사소).
5. **`main:theorem` 의 `provides`.** consequences.tex 19, 47, 112만 적고, `\cref{main:theorem}` 이 있는 33, 63을 빠뜨렸다(검토자 곁들임, 원문으로 확인). §2 카드라 고치지 않았다.
6. **L1 수 4의 "계수 한계(P6)" (검토자 확신 낮음).** P6의 수학 노드에 `tree:charging` 이 없고 그것은 rules.md의 "규칙으로 못 옮긴 것"에 있다. 이번에 수 5 근거 노드에 [[tree:charging]]을 넣었으므로, 수 4의 문구를 "계수 한계(`tree:charging`)"로 바꿀지 P6의 수학 노드에 더할지는 rules.md와 함께 정할 일이다.
