# Task Reference Boundary

## Goal
- `reference`와 `task`의 경계를 더 선명하게 해 reference 본문이 task에 길게 중복되는 운영 drift를 줄인다.

## Scope
- shipped skill, migration skill, README, repo-local direction 문서의 wording alignment

## Current Understanding
- `reference`는 반복 재사용할 주제별 정본 surface이고 `task`는 작업 운영과 판단 흔적을 남기는 surface인데, reference 작성 task에서 본문 재요약이 반복될 여지가 있다.

## Current State
- status는 completed다.
- shipped/local surface 모두에 "주제별 정본 내용은 reference가 소유하고 task에는 경로, 근거, 변경 흔적만 남긴다"는 경계를 반영했다.
- latest validation: `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 -m unittest discover -s tests -p 'test_*.py'`

## Next Step
- 없음

## Working Boundary
- declared read scope: `README.md`, `README.en.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/03-17/task-reference-boundary/**`
- declared write scope: `README.md`, `README.en.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/03-17/task-reference-boundary/**`
