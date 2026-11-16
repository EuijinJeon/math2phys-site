# 유도 지도 만드는 절차

`decor-thm-derivation.html` 을 만든 과정을 실제 순서대로 적는다. 각 단계에 **한 일**, **판단 규칙**, **이번에 나온 값**을 둔다. 다른 정리에 적용할 때는 12절의 점검표만 따라가도 된다.

표기: **[규칙]** 다시 만들 때 지킬 것. **[이번 값]** 이 지도에서 나온 결과. **[시행착오]** 처음에 틀렸다가 고친 것.

---

## 1. 요청을 원문의 위치로 바꾼다

"7장"은 논문의 §7이다. 절 번호는 `redesign/source/main.tex` 의 `\input` 순서와 각 파일의 `\section` 유무로 정한다.

```bash
grep -n '\\input' redesign/source/main.tex
grep -n '\\section' redesign/source/sections/*.tex
```

**[이번 값]** `overview.tex` 에는 `\section` 이 없다. 그래서 introduction §1, model §2, trees §3, upper §4, cavity §5, perturbations §6, **decorrelation §7** 이다. `redesign/HANDOFF.md` 의 "수 5(§7)"와도 맞는다.

"multioverlap의 깊이 평균 집중"은 §7의 목표 정리다.

```bash
grep -n 'begin{\|label{\|section' redesign/source/sections/decorrelation.tex
```

**[이번 값]** Theorem `decor:overlap-concentration` (63–76행)이다. 그 증명은 532–611행에 있다. 증명이 정리와 떨어진 곳에 있으므로 두 곳을 다 읽어야 한다.

**[규칙]** 기존 증명 지도에 같은 정리가 있는지 먼저 본다. `graphs/move5.json` 의 `thm` 하위 graph에 이 증명이 18 node로 있었다. 그러나 모두 sketch였고 확대해 보는 보기가 아니었다. 이번에는 그 자료를 읽지 않고 **원문에서 새로 지었다.** move5의 node 이름과 대조는 하지 않았다.

```bash
python3 -c "
import json;d=json.load(open('redesign/proofmap/graphs/move5.json'))
for g in d['graphs']: print(g['id'], g.get('title'), len(g.get('nodes',[])), len(g.get('edges',[])))"
```

## 2. 원문을 읽는다

읽은 범위와 목적이다. 정리 하나를 위해 §7 전체(623행)를 읽었다.

| 파일:행 | 무엇 | 왜 |
|---|---|---|
| decorrelation.tex 1–84 | 절 첫머리, §7.1 깊이 평균, 정리 진술, 증명 개요 | 정리의 진술과 쓰이는 정의 |
| decorrelation.tex 85–300 | §7.2 정의·Lemma 둘·사영 경계, §7.3 Proposition 첫 부분 | 정리 증명이 부르는 식 라벨의 출처 |
| decorrelation.tex 490–525 | fiber 경계, 재귀 부등식, Proposition 결론 | 정리 증명이 `\eqref{decor:fiber-bound}` 를 직접 부른다 |
| decorrelation.tex 526–623 | §7.4 정리의 증명, Remark | 지도의 중심 |
| perturbations.tex 440–465 | Theorem `pert:tree-identity` 진술 | 증명이 쓰는 항등식의 정확한 꼴 |
| trees.tex 38–50 | 표본 규칙, `tree:multioverlap` | $R_S$ 의 정의 |
| trees.tex 337–360 | Lemma `tree:reference-total`, $\kappa(S)$ | marker 계수 $C(S,e)=-\delta\kappa(S)$ 의 $\kappa$ |

300–490행(Proposition 귀납 단계 본문)은 **읽지 않았다.** 정리 증명이 그 내부를 쓰지 않고 결론과 fiber 경계만 쓰기 때문이다. 그래서 그 부분은 node 하나(`P_IND`)로 줄였다. 이것이 이 지도의 가장 큰 생략이다.

**[규칙]** 증명 본문의 `\ref`·`\eqref`·`\cref` 를 모두 따라가 출처를 읽는다. 그리고 **`\ref` 없이 쓰는 것**을 따로 찾는다. 예를 들어 "spin-anchor identity", "product difference inequality", "variance decomposition"은 라벨 없이 쓰인다. 앞의 둘은 각각 `pert:tree-identity`, `decor:one-vertex-shift` 주변 문장에서 왔다. 마지막 것은 기초 확률이라 node로 세우지 않고 걸음 안에 적었다.

```bash
grep -n 'spin-anchor\|product difference\|martingale' redesign/source/sections/*.tex
grep -n 'kappa' redesign/source/sections/*.tex
```

## 3. 묶음(cluster)을 정한다

**[규칙]** 묶음은 원문의 절 구조 그대로 둔다. 물리 해석으로 묶지 않는다(proofmap HANDOFF 5절 "경계는 원문 구조로 자른다"와 같은 원칙). 다른 절에서 받는 것은 "밖에서 받는 것" 하나로 모은다.

**[이번 값]**

| 묶음 키 | 이름 | 원문 |
|---|---|---|
| `ext` | 밖에서 받는 것 (§3·§6) | trees.tex, perturbations.tex |
| `s71` | §7.1 깊이 평균 | 15–84 |
| `s72` | §7.2 조건부 공분산과 깊이 연속성 | 85–231 |
| `s73` | §7.3 Proposition | 232–525 |
| `s74` | §7.4 정리의 증명 | 526–623 |
| (없음) | 받는 곳 §8 | `OUT` 하나 |

## 4. node를 고른다

### 4.1 규칙

1. **번호 붙은 진술과 라벨 붙은 식**이 기본 단위다. 정리, 보조정리, 명제, 정의식, 다른 곳에서 `\eqref` 로 불리는 식이다.
2. **정리의 증명은 걸음 단위로 쪼갠다.** 한 걸음은 "새 대상을 도입하거나 새 부등식·등식 하나를 얻는 문장 묶음"이다. 원문의 문단 경계와 라벨 식이 걸음의 경계와 대개 맞는다.
3. 정리 증명이 **내부를 쓰지 않는** 긴 증명(여기서는 Proposition의 귀납)은 결론, 그리고 정리가 직접 부르는 중간 결과만 node로 세운다.
4. 다른 절의 결과는 `ext` node로 세운다. 쓰이는 만큼만 진술을 옮긴다.
5. 극한 순서 같은 주의 사항(Remark)은 `note` 종류로 세우고 점선으로 잇는다.
6. 정리를 밖에서 받는 곳이 있으면 `OUT` 하나를 둔다. 원문 첫 문단이 밝힌 사용처(§8)다.

### 4.2 정리 증명을 걸음으로 쪼갠 대응표

decorrelation.tex 533–611행을 문장 단위로 읽고 이렇게 나눴다.

| node | 원문 행 | 원문의 핵심 문장 | 얻는 것 |
|---|---|---|---|
| `T_S` | 533–535 | "For a singleton, use the spin-anchor identity with no added colors and $f=R_S$." | $\mathbb ER_S^2=(\mathbb ER_S)^2+o_N(1)$ |
| `T_SET` | 537–545 | "Suppose $S$ first splits at $e$ … add a full copy of $S$ … split from the anchor at $e-1$." | marker anchor 구성, $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$ |
| `T_C` | 545–549 | "The extension coefficient on both sides … is the same nonzero number" | $C(S,e)=-\delta\kappa(S)$ |
| `T_SIDES` | 550–561 | "The target and old copies are conditionally independent … anchor-alone side …" | $C(S,e)\mathrm{Var}(M)=o_N(1)$ |
| `T_VM` | 562–569 | "Division by $C(S,e)$ is made only at fixed $L$" | $\mathrm{Var}(M)\to0$ |
| `T_G` | 571–581 | "Set $G=\ldots$, $G_-=\ldots$. By (projection-bound) …" | $\mathbb E(R_S-G)^2\le p_N^2$ |
| `T_ADJ` | 582–590 | "the product difference inequality and (martingale-energy) imply" | $\mathcal A\,\mathbb E(G-G_-)^2\le C_k/L$ |
| `T_L2` | 591–596 | "Since conditional expectation is the optimal $L^2$ projection" | $\mathbb E(R_S-M)^2\le2p_N^2+2\mathbb E(G-G_-)^2$ |
| `T_FIB` | 604–609 | "we used $p_N^2\le s\sum_j v_N^{1/2}$ and (fiber-bound) with $\gamma=1/2$" | $\limsup_N\mathcal A\,p_N^2\le C\,V_{k-1,L}(\eta/2)^{1/2}$ |
| `T_VAR` | 597–603 | "Variance decomposition and (prefix-projection-concentration) now show" | 분산 추정 (variance-estimate) |
| `THM` | 63–76, 609–611 | "Proposition … finishes the proof." | 정리 |
| `REM` | 613–623 | Remark order-of-limits | 극한 순서 |

**[규칙]** 원문은 `T_FIB` 의 내용을 `T_VAR` 식 **뒤에** "In this estimate we used …"로 적는다. 지도에서는 의존 순서대로 `T_FIB → T_VAR` 로 앞에 둔다. 원문 순서와 의존 순서가 다를 때는 의존 순서를 따르고, node의 원문 행으로 원래 자리를 남긴다.

**[규칙]** `T_VAR` 에는 원문이 한 줄로 넘긴 걸음을 풀어 적었다. 분산 분해 $\mathrm{Var}(R_S)=\mathrm{Var}(M)+\mathbb E(R_S-M)^2$ 가 그것이다. 또 첫 항의 깊이 평균이 $\limsup_N$ 에서 사라지는 이유도 적었다. 고정 $L$ 에서 배정이 유한개라는 것이고, 원문 48–58행이 근거다. 그래서 `A_ERR → T_VAR` edge를 두었다.

### 4.3 §7.1–§7.3과 밖의 node

전체 목록과 원문 행은 `NODES.md` 에 있다. 고른 이유만 적는다.

- §7.1: 정의(`A_DEF`), Hölder(`A_HOL`), 두 비교(`A_CMP`), 항등식 오차의 유한 최대(`A_ERR`). 정리 증명과 Proposition이 모두 쓴다.
- §7.2: 정의(`B_DEF`), Lemma 둘(`B_CON`, `B_DC`), `B_DC` 증명 안의 식 `decor:martingale-energy`(`B_ME`), 사영 경계(`B_PB`). `B_ME` 를 Lemma에서 떼어 따로 세운 것은 정리 증명(`T_ADJ`)이 이 식을 직접 부르기 때문이다.
- §7.3: `P_V`(귀납 양의 정의), `P_1`(기저), `P_IND`(귀납 단계 전체를 한 node로), `P_FB`(fiber 경계; 정리가 직접 부름), `P_REC`(재귀식), `PROP`.
- 밖: `X_TI`, `X_EXT`, `X_RT`, `X_CH`, `X_SAMP`, `X_MO`. `X_CH` 는 Proposition만 쓴다.

## 5. edge를 고르고 내용을 단다

### 5.1 규칙

1. edge는 "보낸 node의 결과 가운데 받는 node가 실제로 쓰는 것"이다. 라벨에는 **싣는 내용**을 적는다. 식 하나이거나 짧은 말이다.
2. 종류 셋:
   - `key`: 정리 증명(§7.4) 안의 사슬과 정리로 들어가는 선. 청록 굵은 선. 라벨이 늘 보인다.
   - 입력(종류 칸 비움): 정의나 보조 결과를 넘기는 선. 회색 선. 라벨은 선택했을 때만 보인다.
   - `note`: 주의 사항. 점선.
3. 정의만 넘기는 선도 단다(예: `B_DEF → T_G` "$\mu_{e,T_j}$"). 선택했을 때 "이 결과에 쓰인 것"이 빠짐없이 밝아지게 하려는 것이다.
4. 모든 edge는 왼쪽 열에서 오른쪽 열로 간다(6절). 거꾸로 가면 의존 순서가 틀린 것이다.

### 5.2 정리 증명 쪽 edge를 찾은 방법

각 걸음 node에 대해 원문 문장이 **무엇을 받아 쓰는지**를 세 가지로 찾았다.

- `\eqref`·`\cref` 로 부르는 것. 예: `B_PB → T_G`, `P_FB → T_FIB`, `B_ME → T_ADJ`.
- 이름으로 부르는 것. 예: "spin-anchor identity"는 `X_TI → T_S`, "product difference inequality"는 `B_ME → T_ADJ` 의 라벨에 포함했다.
- 앞 걸음에서 정의한 대상. 예: $M$ 은 `T_SET → T_L2`, $G, G_-$ 는 `T_G → T_ADJ`.

### 5.3 전체 목록

`NODES.md` 의 edge 표(61개)에 있다.

### 5.4 원문에 없는 보충

**[이번 값]** 원문 545행은 $C(S,e)$ 가 "nonzero"라고만 한다. 지도의 `T_C` 에는 작성자 확인을 경고색(`class="warn"`)으로 붙였다. $\kappa(S)$ 의 각 인수가 $m_d-j\,m_{d+1}=(d-j(d+1))/L<0$ ($j\ge1$) 이라 0이 아니라는 것이다. proofmap HANDOFF 4절 "알려진 어긋남 6"이 지적한 빈 곳이다.

**[규칙]** 원문 밖에서 채운 것은 반드시 표시한다. 표시는 패널 본문의 `<p class="warn">` 이다.

## 6. 자료를 HTML에 쓴다

자료는 HTML 파일의 `<script>` 안에 있는 JS 배열 셋과 객체 하나다. 별도 JSON은 없다.

```js
const R=String.raw;                 // TeX 백슬래시를 그대로 두기 위함 (6.2)
const GROUPS={ key:{label, fill:'--css변수', b:'--테두리변수'} , ... };
const N=[ {id, g, cls, tag, t, f, body, src}, ... ];
const E=[ [보냄id, 받음id, 라벨, 종류], ... ];
const POS={ id:[띠, 열], ... };
```

| 칸 | 뜻 | 예 |
|---|---|---|
| `id` | 짧은 고유 이름. 접두어는 묶음(`X_`, `A_`, `B_`, `P_`, `T_`) | `T_SIDES` |
| `g` | 묶음 키. 없으면 `null` | `s74` |
| `cls` | `ext` 밖 / `key` 주된 사슬 / `goal` 목표 / `note` 주석 / 없음 | `key` |
| `tag` | 원문의 라벨이나 걸음 번호. node 위쪽 작은 글씨 | `eq decor:marker-variance-identity` |
| `t` | 제목. TeX 가능 | `항등식의 두 쪽` |
| `f` | 대표식. node에 보이는 것. 길면 `<br>` 로 나눈다 | `$C(S,e)\,\mathrm{Var}(M)=o_N(1)$` |
| `body` | 패널에만 보이는 설명(HTML) | |
| `src` | 원문 파일과 행 | `decorrelation.tex 550–561` |
| E의 라벨 | 선이 싣는 내용. 빈 문자열이면 라벨 없음 | `$C\,\mathrm{Var}(M)=o_N(1)$` |
| E의 종류 | `key` / `note` / 생략(입력) | |
| `POS` | `[띠, 열]`. 띠 0 = 위, 1 = 아래, 2 = 세로 가운데(밖 node) | `[1,6]` |

### 6.1 node 문안 규칙

- 제목은 그 걸음이 하는 일을 한국어 명사구로 쓴다. 대표식은 그 걸음이 **얻는 식** 하나다.
- 대표식이 node 폭(최대 340px)을 넘으면 `<br>` 로 줄을 나누고, 이어지는 줄은 `$\quad\le\ldots$` 처럼 들여 쓴다.
- 원문 용어(anchor, prefix, fresh, extension, multioverlap)는 영어 그대로 둔다. 프로젝트 문서들과 같은 관례다.
- 원문이 증명하지 않은 동일시(RPC, ultrametricity 등)는 쓰지 않는다(프로젝트 원칙).

### 6.2 [시행착오] TeX 백슬래시

`t:'기저: $V_{1,L}(\eta)\le\delta/\eta$'` 처럼 **작은따옴표 문자열**에 TeX를 쓰면 JS가 `\e`, `\l`, `\d` 를 이스케이프로 처리해 백슬래시가 사라진다. `\t`, `\b`, `\f`, `\v` 는 제어문자가 된다. 화면에는 "(eta)ledelta"처럼 나온다. 처음 판에서 제목 넷이 이렇게 깨졌다.

같은 일이 패널의 템플릿 문자열에서도 났다. `` `…$N\to\infty$…` `` 의 `\t` 가 탭이 되어 "Noinfty"로 보였다.

**[규칙]** TeX가 들어가는 문자열은 모두 ``R`…` `` 로 쓴다. 보간(`${}`)이 있는 템플릿에도 ``R`…${x}…` `` 를 쓸 수 있다. `check_graph.cjs` 가 이 사고를 오류로 잡는다(7절).

## 7. 배치

### 7.1 [시행착오] 자동 배치(dagre)를 버린 이유

처음에는 dagre 0.8.5의 compound graph(묶음을 부모 node로)로 위→아래 배치를 했다. 결과는 5820×1830px였다. 밖 node 여섯이 모든 묶음으로 선을 뻗어 묶음들이 가로로 흩어졌고, 전체 보기에서 16%로 줄어 읽을 수 없었다. 묶음 상자도 겹쳤다.

**[규칙]** node가 수십 개이고 묶음이 원문 절 순서를 따르면 **손으로 정한 격자 배치**가 낫다. 자리는 `POS` 에 `[띠, 열]` 로만 주고, 픽셀 좌표는 잰 크기로 계산한다.

### 7.2 격자 설계

왼쪽에서 오른쪽으로 흐른다. 띠 둘을 위아래로 둔다.

```
열:     0        1–3                 4–7                         8–10
띠 0:   (밖)     §7.1 깊이 평균       §7.3 Proposition
띠 1:            §7.2 공분산·연속성    §7.4 정리의 증명 ─────────→ THM → OUT
띠 2:   밖 node 여섯을 세로 가운데에
```

**[이번 값]** `POS` 전체:

```
X_*:[2,0]
A_DEF,A_ERR:[0,1]   A_HOL,A_CMP:[0,2]
B_DEF:[1,1]   B_CON,B_ME:[1,2]   B_PB,B_DC:[1,3]
P_V,P_1:[0,4]   P_IND,P_FB:[0,5]   P_REC:[0,6]   PROP:[0,7]
T_SET,T_S:[1,4]   T_C,T_G:[1,5]   T_SIDES,T_ADJ,T_L2:[1,6]   T_VM,T_FIB:[1,7]   T_VAR,REM:[1,8]
THM:[1,9]   OUT:[1,10]
```

**[규칙]** 열 번호는 의존의 **가장 긴 경로 깊이**와 대략 맞춘다. 정확한 위상 순서일 필요는 없지만, 모든 edge가 열이 커지는 방향이어야 한다(`check_graph.cjs` 4번 검사). 같은 칸(띠·열)에 여러 node를 두면 `N` 배열의 순서대로 위에서 아래로 쌓인다. 그래서 `N` 의 순서도 배치의 일부다.

### 7.3 좌표 계산 (`layout()`)

1. MathJax가 수식을 그린 **뒤에** 각 node의 `offsetWidth`·`offsetHeight` 를 잰다. 그 전에 재면 TeX 원문 길이로 재서 틀린다.
2. 열 폭 = 그 열의 모든 node 폭의 최대. 열의 x = 앞 열들의 폭 + `COLGAP`(170px)의 누적. 바깥 여백 `M` 은 60px다.
3. 칸 높이 = 쌓인 node 높이의 합 + `ROWGAP`(26px) 간격. 띠 높이 = 그 띠 칸 높이의 최대. 띠 1은 띠 0 아래 `BANDGAP`(90px)에서 시작한다.
4. node는 칸 안에서 가로 가운데, 칸 묶음은 띠 안에서 세로 가운데에 둔다. 띠 2(밖 node)는 전체 높이의 세로 가운데다.
5. 묶음 상자 = 그 묶음 node들의 외접 사각형 + 여백 18px(위쪽은 이름표 자리로 8px 더).
6. **선의 끝점 나누기:** 한 node에서 나가는 선들을 받는 node의 y 순서로 정렬한다. 그리고 node 오른쪽 변의 높이 20%–80% 구간에 고르게 나눠 붙인다. 들어오는 선도 왼쪽 변에서 같은 방식으로 나눈다. 선 다발이 한 점에 몰리는 것을 막는다.
7. **선 모양:** 3차 Bézier `M x1,y1 C x1+dx,y1 x2-dx,y2 x2,y2`, `dx = max(50, (x2-x1)/2)`. 화살촉은 SVG `marker`.
8. **라벨 위치:** [시행착오] 처음에는 선 길이의 50% 지점(긴 선은 82%)에 두었다. 그러자 긴 선의 라벨이 중간 열의 node 위에 얹혔다. **받는 node 바로 앞 빈 열의 가운데**(x = 받는 node 왼쪽 − `COLGAP`/2)에 놓는 것으로 바꿨다. 그 x에 해당하는 선 위의 점은 `getPointAtLength` 를 이분법으로 24번 돌려 찾는다. 라벨 최대 폭은 150px로 열 간격 170px 안에 들어가게 했다.

**[이번 값]** 전체 크기 5041×836px.

## 8. 보기 기능

전부 HTML 안의 손으로 쓴 JS다. 쓰는 외부 자원은 MathJax 3.2.2(`tex-svg.js`, cdnjs)와 Google Fonts뿐이다. MathJax는 SVG 출력을 쓴다. 이유는 둘이다. 글꼴 파일을 따로 받지 않으므로 게시 환경의 CSP(cdnjs의 글꼴·CSS 차단)에 걸리지 않고, 확대해도 수식이 흐려지지 않는다. KaTeX는 CSS와 글꼴을 cdnjs에서 받아야 해서 쓰지 않았다.

| 기능 | 구현 |
|---|---|
| 확대·이동 | `#world` 에 `transform: translate(x,y) scale(k)`, `transform-origin:0 0`. 휠은 커서 위치를 고정하고 확대한다(Shift+휠은 이동). 한 손가락·마우스로 끌면 이동, 두 손가락이면 확대와 중심 이동. 배율 범위는 0.12–4 |
| 버튼과 키 | ＋/－(1.3배), 전체 보기(`fitRect` 로 전체를 화면에), 정리의 증명으로(§7.4 묶음 상자에 맞춤), 선택 해제. 키: `+` `-` `0` 방향키 `Esc` |
| 모눈 배경 | `#viewport` 의 `background-size`·`background-position` 을 확대·이동과 같이 바꾼다 |
| 선택 | node를 누르면(움직임 6px 미만) 그 node의 **조상 전체**를 거꾸로 BFS로 구해 밝히고 나머지를 흐리게 한다. 조상 사이의 선과 라벨만 남는다. 입력 선의 라벨은 이때만 보인다 |
| 두 번 누르기 | 350ms 안에 같은 node를 다시 누르면 그 node로 확대(최대 2.2배) |
| 패널 | 진술, 설명, 원문 행, 받는 것·보내는 것 목록. 목록 항목을 누르면 그 node를 선택하고 확대한다. 패널을 채운 뒤 `MathJax.typesetPromise([panel])` |
| 시작 순서 | node·라벨 DOM 생성 → MathJax 조판과 글꼴 준비를 기다림(최대 9초) → `layout()` → 패널 그리기 → 다음 프레임에 전체 보기 |
| 화면 폭 | 760px 이하에서 패널을 아래로 내리고(높이 최대 42%) 설명 줄과 안내를 숨긴다 |
| 테마 | 색은 모두 `:root` 변수. 다크는 `prefers-color-scheme` 과 `data-theme="dark"` 두 곳에 같은 값 |

**[시행착오]** 셋이 있었다.
- `#loading{display:flex}` 가 `hidden` 속성을 이겨서 로딩 문구가 사라지지 않았다. `#loading[hidden]{display:none}` 을 더했다.
- 전체 보기를 패널보다 먼저 계산하자 휴대폰 폭에서 지도가 화면 아래로 치우쳤다. 패널이 들어오며 보이는 영역의 높이가 바뀌기 때문이다. 패널을 먼저 그리고 `requestAnimationFrame` 안에서 맞췄다.
- 휠 처리기에 트랙패드 구분 조건을 섞었다가 판정이 꼬였다. "휠은 확대, Shift는 이동"으로 단순하게 했다.

## 9. 검사

### 9.1 구조 검사

```bash
node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs redesign/proofmap/build/decor-thm-derivation.html
```

검사 항목:
1. id 중복
2. 필수 칸(`tag`, `t`, `f`, `src`)과 묶음 키
3. `POS` 누락과 남는 `POS`
4. edge 양끝 node의 존재
5. 모든 edge가 열이 커지는 방향인지
6. 순환
7. THM에 닿지 않는 node(경고)
8. TeX 백슬래시 사고: 제어문자, 또는 `$…$` 안에서 백슬래시 없이 남은 `eta`, `le`, `delta`, `mathbb` 등
9. `$` 짝

**[이번 값]** 오류 0. node 34, edge 61, key 18, THM의 조상 32.

결함을 일부러 넣어 검사가 잡는지 확인했다(사본 4개).

| 넣은 결함 | 결과 |
|---|---|
| 제목 하나를 작은따옴표 문자열로 (`\eta` 사라짐) | 오류 1 ("백슬래시 빠진 TeX 의심"). 처음에는 경고였는데, 놓치기 쉬워서 오류로 올렸다 |
| edge 끝을 없는 id로 | 오류 + 연쇄 경고 |
| `OUT → T_VAR` 역방향 edge | "열이 오른쪽으로 가지 않음" + "순환" 오류 2 |
| `POS` 에서 THM 삭제 | 오류 1 |

### 9.2 화면 검사

```bash
node .../tools/render_check.cjs <지도.html> <출력폴더> <tex-svg.js 경로>
```

이 스크립트가 하는 일:
1. 게시 전 파일에는 `<!doctype>`·`<body>` 가 없다. 게시 때 껍데기가 씌워지기 때문이다. 그래서 껍데기와 `[hidden]` 규칙을 씌운 사본을 만든다.
2. 이 작업 환경에서는 cdnjs 접속이 막혀 있었다(프록시가 거부). 그래서 같은 판의 MathJax를 npm(`mathjax@3.2.2`)으로 받아 두고, Playwright `route` 로 cdnjs 요청에 그 파일을 넣는다. 글꼴 요청은 끊고 대체 글꼴로 본다.
3. 1440×900 라이트·다크, 400×800 휴대폰에서 로딩이 끝나기를 기다린다. 그다음 MathJax 수식 수, 지도 크기, node 수, 가로 넘침, 콘솔·페이지 오류를 출력하고 스크린샷을 남긴다.
4. 데스크톱에서는 "정리의 증명으로", §7.4 왼쪽 절반과 오른쪽 절반을 100%로 확대한 화면, THM 선택 화면도 찍는다.

**[이번 값]** 세 경우 모두 오류 없음, node 34, 수식 96개, 가로 넘침 없음. 스크린샷은 사람이 눈으로 봤다. 라벨과 node 겹침, 깨진 TeX, 휴대폰 배치를 이 스크린샷으로 찾아 고쳤다(6.2, 7.3의 8, 8의 시행착오).

**[하지 않은 것]** 게시된 claude.ai 페이지를 열어 보지 않았다. 실제 글꼴(IBM Plex Sans KR, Noto Serif KR)로 그린 화면도 보지 않았다. 내용의 독립 검토도 하지 않았다.

## 10. 게시와 저장

### 10.1 게시

claude.ai Artifact로 게시했다(파일 경로 `redesign/proofmap/build/decor-thm-derivation.html`, 아이콘 `graph`). 같은 파일 경로로 다시 게시하면 같은 주소가 갱신된다. 다른 대화에서 갱신할 때는 주소를 `url` 로 준다. 게시본은 비공개이고, 공유는 페이지의 Share 메뉴에서 한다.

이 파일은 게시 규약을 따른다. 맨 앞에 `<title>` 과 `<style>` 이 오고 `<!doctype>`·`<html>`·`<body>` 는 없다. 그래서 로컬에서 직접 열면 quirks 모드가 된다. 로컬 확인은 9.2처럼 감싼 사본으로 한다.

### 10.2 proofmap 규격과의 관계

이 지도는 `SPEC.md` 의 proofmap/0.1 JSON을 쓰지 않는다. `tools/build_viewer.py` 로 만든 것도 아니다. 자료(`N`, `E`, `POS`)가 HTML 안에 있다. proofmap 자료로 옮기려면 다음이 필요하다.
- `N` 의 각 node를 그 규격의 node로 옮긴다. `src` 는 원문 참조로 간다.
- `E` 의 라벨을 edge의 "싣는 항목"으로 옮긴다.
- move5 `thm` 하위 graph와 대응을 맞춘다.

하지 않았다.

### 10.3 커밋

`git add` → 커밋 → `git push -u origin <브랜치>`. 처음 커밋은 `9695be6` 이다.

## 11. 다시 만드는 순서 요약

1. 원문 위치 찾기 (1절)
2. 원문 읽기 (2절의 표)
3. 묶음 → node → edge (3–5절). 정리 증명의 걸음 대응표(4.2)를 먼저 쓰면 나머지가 빨라진다.
4. HTML 자료 작성 (6절). 이 파일을 복사해 `GROUPS`·`N`·`E`·`POS` 와 머리 문구만 바꾸면 된다. 배치·보기 코드는 그대로 쓸 수 있다.
5. `check_graph.cjs` → 오류 0
6. `render_check.cjs` → 스크린샷을 보고 겹침·깨짐을 고침. 보통 `POS` 조정, 대표식 줄 나누기, 라벨 줄이기로 해결된다.
7. `dump_table.cjs` 로 표 갱신, 게시, 커밋

## 12. 다른 정리에 적용하는 점검표

- [ ] 목표 정리의 라벨, 진술 행, 증명 행을 찾았다(증명이 진술과 떨어져 있을 수 있다)
- [ ] 증명 본문의 모든 `\ref`·`\eqref`·`\cref` 를 따라가 출처를 읽었다
- [ ] `\ref` 없이 이름으로 부르는 결과("… identity", "… inequality")를 grep으로 찾았다
- [ ] 묶음을 원문 절 구조로 정했다
- [ ] 정리 증명을 걸음으로 나눈 대응표(node, 원문 행, 핵심 문장, 얻는 것)를 썼다
- [ ] 내부를 쓰지 않는 긴 증명은 결론과 직접 불리는 중간 결과만 세웠다. 이 생략을 문서에 적었다
- [ ] 원문 밖에서 채운 걸음은 `warn` 으로 표시했다
- [ ] TeX 문자열은 모두 ``R`…` `` 다
- [ ] 모든 edge가 왼쪽 열 → 오른쪽 열이다
- [ ] `check_graph.cjs <html> <목표 id>` 오류 0
- [ ] `render_check.cjs` 세 화면에서 오류 없음, 스크린샷을 눈으로 봤다
- [ ] `NODES.md` 를 다시 만들었다
- [ ] 독립 검토를 받았는지, 받지 않았는지 적었다
