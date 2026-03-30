**2026-03-30**
- 배경: `docs/memory.md`는 실제 current global state보다 placeholder나 second instruction surface로 흐르기 쉽고, task의 `BRIEF.md`/`STATUS.md` 분리는 reopen/handoff 정보를 인위적으로 찢어 `BRIEF` 축소와 `STATUS` 오용을 낳았다.
- 선택지: 1) `memory`와 `STATUS`를 optional로만 낮춘다. 2) `docs/memory.md`와 `STATUS.md`/`MEMORY-CANDIDATES.md`를 contract에서 제거하고 `BRIEF.md`를 canonical task overview로 재정의한다.
- 결정: `project-context`는 `docs/reference/**`와 `docs/tasks/**`만 top-level surface로 두고, task current file은 `BRIEF.md` 하나만 유지한다. task-specific complexity는 role-driven extra docs로 확장한다.
- 영향: contract, migration workflow, checker/tests, repo-local docs가 모두 `BRIEF.md + logs + optional task-specific docs` 모델로 단순화돼 stale placeholder와 surface overlap이 줄어든다.
