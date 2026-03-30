**2026-03-30**
- `AGENTS.md`, shipped/local surface, 관련 기존 task 두 개를 다시 읽고 이번 compactness 보강과 skill wording 조정이 실제로 separate task 둘이 필요한지 검토했다.
- `task-surface-compactness`의 목적과 결과가 현재 task의 선행 단계에 가까워 별도 reopen 가치가 낮다고 보고, 해당 task 내용을 현재 task snapshot/log에 흡수하는 쪽으로 정리했다.
- separate compactness task 디렉터리를 제거하고 현재 task의 brief/status/decision/worklog를 하나의 흐름으로 다시 썼다.
- orphaned empty task dir 때문에 runtime shape check가 한 번 실패한 뒤, 남은 디렉터리 흔적을 제거하고 validation을 다시 맞췄다.
**2026-03-30**
- shipped `project-context`, migration companion, 로컬 방향/reference, README, runtime-shape test를 읽고 compactness 철학이 이미 있는지와 task surface 오동작을 막는 직접 문장이 어디 비는지 확인했다.
- `project-context` contract에는 `BRIEF`/`STATUS`의 제외 대상과 `WORKLOG` routine check 축약 규칙만 추가하고, migration/local surface는 같은 방향의 한 줄 정렬만 넣었다.
- README와 runtime-shape test는 activation surface와 thin guardrail 범위가 그대로라 추가 변경 없이 두고, guardrail과 전체 unittest를 다시 돌려 현재 contract drift가 없는지 확인했다.
