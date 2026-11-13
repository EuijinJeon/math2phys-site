# exact 유형 독립 감사 — 2026-11-13

상태: **proposed**. 이전 Claude 작성분과 독립하여 원문 사본을 대조했다. 사용자의 confirmed 승인을 대신하지 않는다. 작업 범위는 `bbc603b`의 exact 76장 및 `fada529..bbc603b` 중단 변경분(카드 21장, glossary/rules/SCHEMA)이다. 244장 전체의 재증명 또는 L0–L4 최종 승인 보고서가 아니다.

## 판정 기준과 결론

`SCHEMA.md`의 exact는 같은 내용의 다른 표기, weakening은 덜 말하지만 정확한 문장이라는 정의를 적용했다. 증명의 전개 자체를 생략하는 것과, 정의의 결합 법칙·명시적 정량 결론·적용 범위를 생략하는 것을 구분했다. 용어집으로 명시적으로 연결한 정의는 사용할 수 있다. 명백히 진술이 축약된 경우 weakening으로 바꾸고 빠진 내용을 gap에 적었다. 이름만으로 원문보다 강한 독립성·Gibbs 계층을 얻는 해석은 허용하지 않았다.

- 시작 exact 76장 전부의 math/physics/gap과 source 범위를 확인했다. 이 가운데 **13장을 weakening으로 재분류**, **63장은 exact 유지**했다.
- 이번에 본문 또는 분류를 고친 카드는 **31장**이다. math의 정리식을 바꾸지 않았고, physics/gap에 빠진 조건과 정규화 등을 보충했다. source/uses/status는 유지했다.
- 기존 감사가 weakening으로 바꾼 `cavity:increment`, `tree:extension-expansion`, `x:decor-topology`의 판정은 유지한다. 앞의 두 카드 및 topology 원문을 다시 확인했다.
- 기계 검사: `python3 redesign/tools/check.py --out /tmp/exact-check.md`, 9종 모두 오류 0·경고 0. 이는 내용 동치의 증명이 아니다.

## 실제 의미 수정과 근거

| 카드 | 수정 이유와 원문 근거 |
|---|---|
| model:factorization | strict product bound와 독립성만으로 b, f가 유계라는 gap에 **비퇴화 조건** 추가. b=0이면 f는 유계일 필요가 없다. model.tex:38–41, upper.tex:18–34. |
| main:theorem.s1 | 아무 상수 이동이 아니라 c=θ(1,…,1)라는 선택 및 적분가능성/이동 후 1차 moment를 명시. reduction.tex:45–59. |
| x:tree-differentiation-rule | 0이 아닌 매개변수에서는 삽입 인자가 D가 아니라 D/A. protected는 이미 D를 받았다는 뜻만이 아니라 분모로 leaf의 A가 상쇄되었다는 뜻. G의 매개변수 독립성과 재사용/새 path 두 경우를 복구. trees.tex:178–202. |
| tree:extension-expansion | H의 매개변수 독립성과 방향 D_j의 유계 실수 조건 추가. trees.tex:279–282. 기존 weakening 유지. |
| upper:remainder | λ<1에서의 절대수렴만으로 λ↑1을 정당화하지 않도록 upper:regularization의 2B(θ) 지배 한계를 명시. upper.tex:88–94, 121–126. |
| model:vs | V_s는 새 spin 분배함수 자체가 아니라 **그 값을 2로 나눈 정규화량**. model.tex:84–87. |
| model:site-message | 마지막 좌표에 새 spin을 두며 나머지 spin은 q_x의 곱 법칙임을 명시. model.tex:59–64. |
| models:section | 유한 N pressure가 변분값과 같다는 독해를 피하도록 **열역학 극한**임을 명시. consequences.tex:10–49와 model.tex:130–136. 개요는 weakening으로 분류. |
| tree:Y-recursion; tree:first-variation; tree:log-expansion | 임의 kernel 정리와 terminal Gibbs kernel인 적용을 구분. L=1 Gibbs 설명은 해당 적용에서만 말한다. trees.tex:14–27, 63–82, 142–154, 224–239. |
| decor:depth-continuity.s1 | 뒤쪽 branching 깊이를 고정한 initial stem 위에서 움직인다는 조건 추가. 임의로 tree 전체 깊이를 바꾸어도 단조라는 뜻이 아니다. decorrelation.tex:168–177. |
| cavity:factor-bounds | Poisson 족/균일 site의 독립성과 보조 변수의 product prior를 보충. cavity.tex:20–27. |
| comp:encoding.s4 | 전체 reservoir root까지 독립 복사하며 새 삽입 disorder와도 독립이라는 구성 명시. comparison.tex:73–83. |
| decor:covariance-definition | initial stem(첫 branching 포함)의 평가 깊이 범위, 좌표와 v_N의 한계 복구. decorrelation.tex:94–106. |
| tree:multioverlap; models:ground.s2; upper:derivative.s1; x:decor-mesh | 각각 빈 집합/기대값 약속, limsup/liminf 끼움, edge 삽입 증분, unary 계수를 물리 문장에 보충. trees.tex:41–49; consequences.tex:112–119; upper.tex:62–68; decorrelation.tex:4와 cavity.tex:16–19. |

## 이번 weakening 재분류

| 카드 | 생략된 내용 | 근거 |
|---|---|---|
| cavity:increment.s1 | 정확한 평균 $\rho_N$, $\alpha p(N/(N+1))^{p-1}$ 과 남은 index의 독립 균일 법칙을 생략하고 점근적 평균만 말한다. | cavity.tex:71–85 |
| comp:encoding.s1 | 유한 $x$ 의 보장, 확대된 root와 filtration의 정의를 생략하고 한 site의 말단 조건부 법칙만 말한다. | comparison.tex:27–43 |
| comp:insertion-comparison.s1.s3 | bond 항의 인수분해는 말하지만 site 항과 합친 시행 functional 전체의 등식은 재진술하지 않는다. | comparison.tex:181–196 |
| main:theorem.s3 | 유한 절단 수준에서의 정량 오차 $2\alpha pD_K+2d_K$ 와 그 앞의 두 안정성 한계는 math에만 있다. | reduction.tex:70–84 |
| model:chain | 일반 $r$ 의 조건부 측도 사슬 (2.7), 시행 공간 $\mathcal M_{r+1}$, 엄격한 지수 순서를 전부 재진술하지 않는다. | model.tex:68–81 |
| model:hamiltonian | disorder 족 전체의 상호 독립성과 $N$ 에 무관한 법칙을 명시하지 않는다. Poisson 평균과 pressure라는 이름만으로 전체 결합 법칙이 정해지지는 않는다. | model.tex:9–23 |
| models:section | 두 명명 모형의 독립성·1차 moment 가정 전체와 영온도 오차 폭 $\log2/\beta$ 를 생략한 개요다. | consequences.tex:1–138 |
| reduction:section | 정량 안정성 상수와 최종 liminf/limsup 조립식을 생략한 개요다. | reduction.tex:1–87 |
| upper:bound.s1 | 비퇴화 경우의 명시적 본질적 상계 $u^{-p}$, $(vu^{p-1})^{-1}$ 를 생략한다. | upper.tex:17–34 |
| upper:bound.s2 | 중간 $0<t<1$ 의 Poisson 평균, quenched 변수의 목록, $r=0$ 약속을 생략하고 두 끝점만 설명한다. | upper.tex:36–49 |
| x:model-depth-zero | $T_d$ 생략으로 정의한 $\mathcal B_0$, $\Phi_0$ 의 식을 재진술하지 않고 독립 field 그림만 준다. | model.tex:118–120 |
| x:tree-path-kernels | 임의의 prefix 의존 확률 kernel 열과 insertion 동안 root 분포를 고정한다는 약속을 생략한 계층 그림이다. | trees.tex:14–27 |
| x:tree-sampling | unary 구간 보존, 말단의 서로 다른 vertex와 같은 표본값의 구별, root 조건부 기대값의 약속을 생략한다. | trees.tex:29–39 |

## 중단 변경분 21장 및 layers/SCHEMA 확인

기존 변경의 핵심은 숨은 조건/범위를 physics로 올린 것과 정량 결론을 보충한 것이었다. 아래 카드들의 변경과 원문을 대조했으며, 이번 수정은 위 절에 따로 기록했다. 기존 변경을 통째로 승인하거나 되돌리지 않았다.

| 기존 변경 카드 | 대조한 근거 | 이번 판정 |
|---|---|---|
| cavity:increment | cavity.tex:43–69; cavity.tex:71–115 | weakening |
| comp:encoding | comparison.tex:17–25; comparison.tex:27–83 | exact |
| comp:patterns | comparison.tex:85–97; comparison.tex:99–121 | exact |
| decor:depth-continuity.s1 | decorrelation.tex:168–177 | exact |
| main:theorem.s2 | reduction.tex:60–69 | exact |
| main:theorem.s4 | reduction.tex:85–87 | exact |
| model:factorization | model.tex:25–34 | exact |
| model:integrability | model.tex:3–8 | exact |
| models:ground.s1 | consequences.tex:103–111 | exact |
| reduction:stability | reduction.tex:9–26; reduction.tex:28–43 | exact |
| tree:Y-recursion | trees.tex:67–82 | exact |
| tree:extension-expansion | trees.tex:278–296; trees.tex:298–304 | weakening |
| tree:first-variation | trees.tex:142–154 | exact |
| tree:insertion | trees.tex:84–111; trees.tex:113–133 | exact |
| tree:log-expansion | trees.tex:224–239; trees.tex:241–257 | exact |
| tree:original-tilt | trees.tex:51–65 | exact |
| tree:regular-shapes | trees.tex:469–484; trees.tex:486–514 | exact |
| tree:section | trees.tex:1–525 | weakening |
| upper:remainder | upper.tex:96–126 | exact |
| x:decor-topology | decorrelation.tex:18–21 | weakening |
| x:tree-path-kernels | trees.tex:14–27 | weakening |

- `tree:section`의 §8 내주는 것 보충은 comparison.tex:28–51의 tilted reservoir kernel, terminal Gibbs transition, prefix filtration, x/η 깊이 배정과 맞는다. `tree:original-tilt`, `x:tree-path-kernels`의 provides 보충도 같은 근거다.
- `rules.md` P7/P11의 **물리 규칙 문장은 바뀌지 않았다**. 차이 칸의 카드 없는 식 label을 그 식을 담는 카드로 바꾼 것이다. `glossary.md` 역시 정의 위치/역할에서 식 label을 보유 카드와 식 번호로 바꾼 변경이다. 확인한 대응은 cavity:increment의 (5.4)–(5.7), main:theorem의 (2.13), tree:insertion/Y-recursion의 밀도·updated kernel, decor의 J/비용/축약/martingale, comp:encoding.s4의 한 label moment, reduction:stability의 두 안정성·shift 식이다. 수식 내용이나 가정의 신규 변경은 없다.
- `SCHEMA.md`의 R-ID → 용어집 문장은 현재 용어 규율과 일치한다. 추상화 유형 정의 자체는 바뀌지 않았다.
- **layers 권고(편집하지 않음):** P6는 여전히 canceled-anchor 전개와 charging의 완전한 입력을 서술하지 않으면서 exact다. 기존 HANDOFF의 P6 결정 및 닫힘 시험이 필요하다. P10도 카드 comp:encoding에 복구된 고정 N,L, 선택된 매개변수, root 평균 뒤 결정적 법칙 및 독립 label 조건을 줄 단위 exact 기준으로 다시 점검할 수 있다. 이는 이번 link 교체의 오류가 아니라 기존 규칙층 문제다.

## 76장 전수 확인 목록

이 목록의 source는 실제 읽은 원문 사본(`redesign/source/sections/`)의 대응 범위다. 원문 범위 전체를 수학적 최초 원리에서 재증명했다는 뜻은 아니다. step의 증명 요약은 결론과 필요한 가정이 유지되는지를 보았고, 기술 lemma들의 새 증명을 작성하지 않았다.

| 카드 | 원문 근거 | 결과 |
|---|---|---|
| cavity:factor-bounds | cavity.tex:20–27 | exact (이번 문장 보완) |
| cavity:grid | cavity.tex:16–19 | exact |
| cavity:increment.s1 | cavity.tex:71–85 | weakening |
| cavity:increment.s3 | cavity.tex:100–107 | exact |
| comp:bounded-lower | comparison.tex:225–231; comparison.tex:233–246 | exact |
| comp:encoding | comparison.tex:17–25; comparison.tex:27–83 | exact |
| comp:encoding.s1 | comparison.tex:27–43 | weakening |
| comp:encoding.s3 | comparison.tex:58–72 | exact |
| comp:encoding.s4 | comparison.tex:73–83 | exact (이번 문장 보완) |
| comp:insertion-comparison.s1 | comparison.tex:170–196 | exact |
| comp:insertion-comparison.s1.s3 | comparison.tex:181–196 | weakening |
| comp:low-increments | comparison.tex:12–15 | exact |
| comp:patterns | comparison.tex:85–97; comparison.tex:99–121 | exact |
| decor:covariance-definition | decorrelation.tex:94–106 | exact (이번 문장 보완) |
| decor:depth-continuity.s1 | decorrelation.tex:168–177 | exact (이번 문장 보완) |
| main:theorem | model.tex:130–136; reduction.tex:45–87 | exact |
| main:theorem.s1 | reduction.tex:45–59 | exact (이번 문장 보완) |
| main:theorem.s2 | reduction.tex:60–69 | exact |
| main:theorem.s3 | reduction.tex:70–84 | weakening |
| main:theorem.s4 | reduction.tex:85–87 | exact |
| model:chain | model.tex:68–81 | weakening |
| model:edge | model.tex:55–58 | exact |
| model:factorization | model.tex:25–34 | exact (이번 문장 보완) |
| model:hamiltonian | model.tex:9–23 | weakening |
| model:integrability | model.tex:3–8 | exact |
| model:site-message | model.tex:59–64 | exact (이번 문장 보완) |
| model:ve | model.tex:82–83; model.tex:88–89 | exact |
| model:vs | model.tex:82–87 | exact (이번 문장 보완) |
| models:ground | consequences.tex:86–101; consequences.tex:103–125 | exact |
| models:ground.s1 | consequences.tex:103–111 | exact |
| models:ground.s2 | consequences.tex:112–119 | exact (이번 문장 보완) |
| models:ground.s3 | consequences.tex:120–123 | exact |
| models:ground.s4 | consequences.tex:123–125 | exact |
| models:sat | consequences.tex:36–49; consequences.tex:51–64 | exact |
| models:sat.s1 | consequences.tex:51–58 | exact |
| models:sat.s2 | consequences.tex:59–62 | exact |
| models:sat.s3 | consequences.tex:62–64 | exact |
| models:section | consequences.tex:1–138 | weakening |
| models:spin | consequences.tex:10–22; consequences.tex:24–34 | exact |
| models:spin.s1 | consequences.tex:24–30 | exact |
| models:spin.s2 | consequences.tex:30–31 | exact |
| models:spin.s3 | consequences.tex:31–34 | exact |
| pert:error | perturbations.tex:83–93 | exact |
| pert:score | perturbations.tex:75–82 | exact |
| reduction:section | reduction.tex:1–87 | weakening |
| reduction:stability | reduction.tex:9–26; reduction.tex:28–43 | exact |
| tree:Q-rule | trees.tex:209–222 | exact |
| tree:Y-recursion | trees.tex:67–82 | exact (이번 문장 보완) |
| tree:first-variation | trees.tex:142–154 | exact (이번 문장 보완) |
| tree:insertion | trees.tex:84–111; trees.tex:113–133 | exact |
| tree:log-expansion | trees.tex:224–239; trees.tex:241–257 | exact (이번 문장 보완) |
| tree:multioverlap | trees.tex:41–49 | exact (이번 문장 보완) |
| tree:original-tilt | trees.tex:51–65 | exact |
| tree:reference-total | trees.tex:337–357; trees.tex:359–386 | exact |
| tree:regular-shapes | trees.tex:469–484; trees.tex:486–514 | exact |
| upper:bound | upper.tex:11–15; upper.tex:17–128 | exact |
| upper:bound.s1 | upper.tex:17–34 | weakening |
| upper:bound.s2 | upper.tex:36–49 | weakening |
| upper:derivative | upper.tex:58–61; upper.tex:62–126 | exact |
| upper:derivative.s1 | upper.tex:58–68 | exact (이번 문장 보완) |
| upper:remainder | upper.tex:96–126 | exact (이번 문장 보완) |
| x:cavity-bounded | cavity.tex:11–14 | exact |
| x:cavity-root-convention | cavity.tex:28–32 | exact |
| x:cavity-tree-sampling | cavity.tex:117–121 | exact |
| x:cons-energy-score | consequences.tex:66–84 | exact |
| x:cons-ground-scope | consequences.tex:127–129 | exact |
| x:cons-standard-examples | consequences.tex:4–8 | exact |
| x:decor-mesh | decorrelation.tex:4–4 | exact (이번 문장 보완) |
| x:model-depth-zero | model.tex:118–120 | weakening |
| x:model-hypotheses | model.tex:3–8; model.tex:25–38; model.tex:130–131 | exact |
| x:model-message | model.tex:46–54 | exact |
| x:model-moment-finiteness | model.tex:38–41 | exact |
| x:model-theorem-scope | model.tex:138–140; introduction.tex:75–77 | exact |
| x:tree-differentiation-rule | trees.tex:178–202 | exact (이번 문장 보완) |
| x:tree-path-kernels | trees.tex:14–27 | weakening |
| x:tree-sampling | trees.tex:29–39 | weakening |

## 남은 범위와 불확실성

- 76장 가운데 명시한 기준으로 해결하지 못한 개별 판정은 남기지 않았다. 다만 exact/weakening 경계는 ‘정의를 링크로 얼마나 물려받는가’에 영향을 받는다. 특히 section/definition 개요는 보수적으로 weakening으로 분류했다. 사용자가 더 짧은 물리 문장을 원하면 정량 정보를 gap에 두고 weakening을 유지하는 방식이 일관된다.
- 244장 전체의 physics 검토, 규칙 12행의 완전한 재분류, L1 규칙만의 닫힘, 독립 검토 이후 재검토는 이번 완료 범위 밖이다. 원문 자체의 새로운 오류 여부나 문헌의 외부 검증도 수행하지 않았다.
- 상태는 전부 proposed로 유지했다. confirmed의 추가나 git 변경(커밋·체크아웃·푸시)은 하지 않았다. 카드 외 편집은 이 보고서뿐이다.
