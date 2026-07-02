**2026-07-02**
- 배경: 사용자 정정이 reference claim에도 영향을 줄 때 stale 주장이 current context처럼 남을 수 있고, subagent handoff brief가 최신 제약이나 미확인 상태를 빠뜨릴 수 있다.
- 결정: shipped skill에 reference 정정/삭제 반영 규칙과 subagent brief의 최신 제약·미확인 상태 항목을 직접 추가한다.
- 이유: 둘 다 기존 `BRIEF.md`, `docs/reference/**`, subagent handoff surface를 더 선명하게 하는 보강이고 새 surface를 만들 필요가 없다.
- 영향: `project-context`는 durable context 정리와 handoff shape를 더 명확히 소유하지만, source/runtime 사실 검증 책임은 계속 다른 작업 주체에 둔다.
