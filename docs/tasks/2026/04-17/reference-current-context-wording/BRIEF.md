# Reference Current Context Wording

## Goal
- `reference`를 task provenance와 분리된 현재 기준 맥락으로 다시 정리하고, 그 문장을 repo-local docs와 shipped skill에 맞춘다.

## Scope
- repo-local docs의 `reference` 역할 문장 정리
- shipped `project-context` / `project-context-migration` wording alignment
- README one-liner alignment

## Current Understanding
- `reference`는 task에서 승급된 결과물일 수는 있지만, task가 있어야만 성립하는 surface는 아니다.
- 핵심 경계는 변경 빈도나 provenance가 아니라, 본문이 현재 믿고 쓸 기준 맥락인가 아니면 조사/진행/판단 흔적인가다.
- `reference`는 자주 바뀔 수 있지만 로그처럼 읽히면 안 된다.

## Current State
- status는 completed다.
- `docs/reference/model/context-surfaces.md`, `docs/review-method.md`, `docs/skill-direction.md`, `docs/dogfood-method.md`에 `reference`를 현재 믿고 쓰는 기준 맥락으로 읽는 판정선을 반영했다.
- `README.md`, `README.en.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`도 같은 의미로 정렬했다.
- latest validation: `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 -m unittest discover -s tests -p 'test_*.py'`, `python3 skills/project-context/scripts/task_logs.py worklog check --task-root docs/tasks/2026/04-17/reference-current-context-wording`, `python3 skills/project-context/scripts/task_logs.py decision check --task-root docs/tasks/2026/04-17/reference-current-context-wording`

## Next Step
- 없음

## Working Boundary
- declared read scope: `README.md`, `README.en.md`, `docs/reference/model/context-surfaces.md`, `docs/skill-direction.md`, `docs/review-method.md`, `docs/dogfood-method.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/04-17/reference-current-context-wording/**`
- declared write scope: `README.md`, `README.en.md`, `docs/reference/model/context-surfaces.md`, `docs/skill-direction.md`, `docs/review-method.md`, `docs/dogfood-method.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/tasks/2026/04-17/reference-current-context-wording/**`
