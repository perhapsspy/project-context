# Compact Reference Wording

## Goal
- `reference`와 `task` 경계 문장을 fresh-context 리뷰로 다시 다듬어, 더 짧고 drift가 적은 표현으로 정리한다.

## Scope
- `AGENTS.md`, shipped `project-context` skill, migration skill, local direction 문서의 compact wording review와 반영

## Current Understanding
- 이 레포는 스킬 기술 방향도 관리하므로, repo-local 문서에 "같은 역할이면 더 짧게 쓴다"는 기준이 있어야 한다.

## Current State
- status는 completed다.
- 규칙 반영 위치를 줄인 뒤, 그 기준을 `AGENTS.md`와 `docs/skill-direction.md`에 명시하고 shipped skill 문장도 실제로 압축했다.
- latest validation: `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 -m unittest discover -s tests -p 'test_*.py'`

## Next Step
- 없음

## Working Boundary
- declared read scope: `AGENTS.md`, `README.md`, `README.en.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/03-17/compact-reference-wording/**`
- declared write scope: `AGENTS.md`, `README.md`, `README.en.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/03-17/compact-reference-wording/**`
