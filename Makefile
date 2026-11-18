.PHONY: check check-workflow-review
check:
	node redesign/proofmap/tools/check_decor.cjs
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs redesign/proofmap/graphs/b-con.json -
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs redesign/proofmap/graphs/b-dc.json -
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs redesign/proofmap/graphs/dc-one.json -
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs redesign/proofmap/graphs/x-ch.json -
	node redesign/proofmap/tools/build_decor.cjs
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/dump_table.cjs > redesign/proofmap/checks/2026-11-16-thm-derivation-map/NODES.md
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/dump_table.cjs redesign/proofmap/graphs/b-con.json > redesign/proofmap/checks/2026-11-16-thm-derivation-map/B-CON-NODES.md
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/dump_table.cjs redesign/proofmap/graphs/b-dc.json > redesign/proofmap/checks/2026-11-16-thm-derivation-map/B-DC-NODES.md
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/dump_table.cjs redesign/proofmap/graphs/dc-one.json > redesign/proofmap/checks/2026-11-16-thm-derivation-map/DC-ONE-NODES.md
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/dump_table.cjs redesign/proofmap/graphs/x-ch.json > redesign/proofmap/checks/2026-11-16-thm-derivation-map/X-CH-NODES.md
	@echo '오류 0 · 빌드와 표 갱신 완료'

check-workflow-review:
	node workflow-review/tools/check.cjs
	node workflow-review/tools/test.cjs
	node --check workflow-review/viewer/app.js
	node workflow-review/tools/build.cjs

.PHONY: check-graph-harness
check-graph-harness:
	node --check workflow-review/harness/tools/record.cjs
	node --check workflow-review/harness/tools/review.cjs
	node workflow-review/harness/tools/test.cjs
