# Task Surface Reduction

## Goal
- `project-context` task surface를 `BRIEF.md + logs` 중심으로 줄이고, `docs/memory.md`/`STATUS.md`/`MEMORY-CANDIDATES.md`를 contract에서 제거한다.

## Scope
- shipped `project-context`/`project-context-migration` skill contract
- runtime-shape checker
- related tests/fixtures
- README/local direction/reference docs
- current repo task surfaces

## Current Understanding
- `docs/memory.md`는 독립 surface보다 placeholder로 굳기 쉽다.
- `BRIEF.md`/`STATUS.md` 분리는 실제 reopen 질문을 인위적으로 나눠 `BRIEF` 축소와 `STATUS` 오용을 낳는다.
- `BRIEF.md`를 canonical task overview로 재정의하고 extra task-local docs를 role-driven extension으로 인정하는 편이 더 단순하다.

## Current State
- status는 completed다.
- blockers는 없다.
- shipped `project-context`와 migration skill은 `docs/reference/**` + `docs/tasks/**` 구조만 남기고, task current file을 `BRIEF.md` 하나의 canonical overview로 재정의했다.
- `BRIEF.md` 가이드는 top-level heading 중심으로 다시 정리했고, representative fixture와 current repo task BRIEF도 같은 형식으로 맞췄다.
- runtime-shape checker와 tests/fixtures는 `BRIEF.md + logs` 모델로 정리됐고, 현재 repo의 `docs/memory.md`와 live `STATUS.md`/`MEMORY-CANDIDATES.md`도 제거했다.
- live `docs/tasks/**` BRIEF는 heading-first 형식으로 다시 쓰고, portable path scan은 task logs까지 보도록 넓혔다.
- old `memory`/candidate transition만 설명하던 live task는 reopen entrypoint로서 오해 비용이 커 삭제했다.
- task 재사용 규칙은 declared scope 하드 게이트보다 "같은 미완료 작업선인가"를 먼저 보는 쪽으로 다시 정리했다.
- latest validation: `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 -m unittest discover -s tests -p 'test_*.py'`

## Next Step
- 없음

## Working Boundary
- declared read scope: `AGENTS.md`, `README*.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `skills/project-context/scripts/check_runtime_shape.py`, `tests/project_context/**`, `tests/project_context_migration/**`, `docs/tasks/2026/03-30/task-surface-reduction/**`
- declared write scope: `AGENTS.md`, `README*.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `skills/project-context/scripts/check_runtime_shape.py`, `tests/project_context/**`, `tests/project_context_migration/**`, `docs/tasks/2026/03-30/task-surface-reduction/**`
