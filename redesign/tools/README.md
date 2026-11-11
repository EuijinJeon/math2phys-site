# tools/

표준 라이브러리만 쓴다 (PyYAML이 있으면 쓰고, 없으면 내장 최소 파서). 어느 디렉터리에서 실행해도 된다.

| 스크립트 | 하는 일 | 출력 |
|---|---|---|
| `extract.py` | `source/`의 .tex를 읽어 정리류·절·수식 노드, `\ref`류·`\cite` 간선, 문장 분할을 뽑는다 | `build/graph.json`, `build/sentences.json` |
| `check.py` | 적법성 검사(정초·포함·의존·연결·순환·사전·단면, 그리고 머리말 형식) | `build/check-report.md` (오류가 있으면 종료 코드 1) |
| `build.py` | `layers/`, `cards/`, `graph.json`으로 정적 HTML을 만든다 | `site/` |
| `common.py` | 위 둘이 공유하는 카드·규칙 표 파서 | |

## 실행

```
python3 tools/extract.py                        # 원문이 바뀔 때만
python3 tools/check.py                          # 카드가 있는 모든 파일에 포함 검사
python3 tools/check.py --sections decorrelation # 포함 검사 대상을 파일 stem으로 지정 (쉼표 구분)
python3 tools/build.py                          # site/index.html 에서 시작
```

- `--root DIR`(또는 환경변수 `M2P_ROOT`): `cards/`, `layers/`, `build/check-report.md`, `site/`를 이 디렉터리에서 읽고 쓴다. `source/`와 `build/graph.json`은 항상 실제 것을 쓴다. 시험용 fixture에 쓴다.
- `check.py --out FILE`, `build.py --out DIR`: 출력 위치 지정.
- `cards/`나 `layers/`가 비어 있어도 죽지 않고 "아직 카드 없음"으로 보고한다. 머리말이 깨진 카드는 오류로 기록하고 계속 간다.

## graph.json 구조

- `nodes`: `section`/`subsection`/정리류(`theorem` … `remark`)/`equation`/`figure`/`label`. 정리류는 `number`("Lemma 7.2"), `lines`(진술), `proof`(첫 증명 범위 또는 null), `proofs`(전부)를 가진다. 라벨이 없으면 id는 `x:<파일>-L<줄>`.
- `edges`: `src`(가장 안쪽 노드), `dst`(라벨), `dst_container`(라벨이 든 정리류/절), `role`(`statement`/`proof`/`text`), `file`, `line`.
- `cites`, `proofs`(어느 노드에도 안 붙은 증명 포함), `labels`.

## 알려진 한계

- 문장 분할은 휴리스틱이다(수식·약어는 보호하지만 완벽하지 않다). 결정적이다.
- 수식 번호는 `\notag`/`\nonumber`/`\tag`까지 반영하지만 `subequations`, `alignat` 열 수 등은 다루지 않는다.
- Mermaid·MathJax는 CDN에서 불러오므로 사이트를 보려면 인터넷이 필요하다.
