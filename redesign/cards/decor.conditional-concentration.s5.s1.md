---
id: decor:conditional-concentration.s5.s1
kind: step
title: 'target II 첫 경로의 분류'
uses: [decor:conditional-concentration.s3.s1, decor:conditional-concentration.s4.s2, tree:extension-expansion, x:decor-mesh]
provides: 'decor:conditional-concentration.s5.s2, s5.s3'
math: |
  target I의 추가는 모두 깊이 $d$ 아래 anchor 가지 안에 머물므로 old II stem과 그 child count를 바꾸지 않는다. target II의 첫 추가 경로는 anchor와 깊이 $d$에서 갈라져야 하므로 깊이-$e$ prefix에 따라 정확히 다음 중 하나다. (i) 깊이-$d$ vertex에서 fresh divergence ($\ell=d$, 계수 $-c_d$, $c_d=2m_{d+1}-m_d$). (ii) old II stem을 따라가다 깊이 $\ell$ ($d<\ell<e$)의 unary vertex에서 fresh divergence (계수 $-c_\ell=-\delta$). (iii) old II prefix를 깊이 $e$까지 따라감 (그 뒤의 선택은 무엇이든). (i), (ii)에서 $b_\ell$은 새 stem 위의 $a_{S,e}$이고, (iii)에서 최종 사영 벡터는 $b$이다. target II의 나중 경로는 첫 경로와 $e+1$ 이상에서 갈라지므로 깊이 $e$까지 첫 경로를 따른다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: decorrelation.tex, lines: [386, 400]}
status: proposed
---

$f$는 old leaf 전체의 multioverlap이므로 허용된 고정 overlap 단항식이고 $|f|\le1$이다. 분류의 요점은 사영된 overlap이 target II 첫 경로의 깊이-$e$ prefix에만 의존한다는 것이다. 첫 경로가 old II에서 언제 떨어지느냐에 따라 $b$를 그대로 쓰거나 $b$와 부분적으로만 prefix를 공유하는 새 사본 $b_\ell$을 쓴다.
