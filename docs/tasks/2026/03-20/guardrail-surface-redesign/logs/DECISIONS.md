**2026-03-20**
- 배경: 현재 Python validation은 shipped thin guardrail, maintainer telemetry, migration semantics가 한 축에 섞여 있어 contract보다 무겁고 drift를 재생산한다.
- 선택지: 1) 기존 checker에 분기를 계속 추가한다. 2) shipped checker는 shape/reachability smoke test로 줄이고, richer 의미 검증은 repo-local fixture/test로 남긴다.
- 결정: shipped checker는 required surface, path/date naming, memory hard cap, latest log block shape, `MEMORY-CANDIDATES` grammar/reachability만 보도록 줄이고, maintainer telemetry와 과한 semantics는 제거한다.
- 영향: agent-facing guardrail 신뢰도는 높이고, migration ownership 같은 더 무거운 판단은 repo-local fixture/test에서만 다루게 된다.
