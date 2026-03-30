# Dogfood Loop

## Goal
- 레포 로컬 dogfood 방식을 짧게 정리하고, 그 방식으로 당시 skill wording/style 변경을 실제로 점검해 결과를 남긴다.

## Scope
- `AGENTS.md`, `docs/skill-direction.md`, current skill wording change, runtime validation

## Current Understanding
- dogfood 방법은 task 기록들에 흩어져 있고, 중앙에 짧게 정리된 repo-local 방식은 아직 없다.

## Current State
- status는 completed다.
- repo-local dogfood 루프를 방향 문서에 추가하고, 그 루프로 당시 wording/style 변경을 점검했다.
- 이후 task surface 단순화로 live contract는 더 줄었지만, 작은 실제 대상부터 dogfood한다는 원칙은 그대로 유지된다.
- latest validation: `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 -m unittest discover -s tests -p 'test_*.py'`

## Next Step
- 없음

## Working Boundary
- declared read scope: `AGENTS.md`, `docs/skill-direction.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/03-10/project-context-migration-dogfood/**`, `docs/tasks/2026/03-10/migration-fixture-harness/**`, `docs/tasks/2026/03-13/readme-first-user-eval/**`, `docs/tasks/2026/03-18/dogfood-loop/**`
- declared write scope: `AGENTS.md`, `docs/skill-direction.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/03-18/dogfood-loop/**`
