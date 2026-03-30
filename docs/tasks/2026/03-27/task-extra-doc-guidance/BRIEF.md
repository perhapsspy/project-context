# Task Extra Doc Guidance

## Goal
- `project-context` task contract에 `BRIEF.md`와 logs만으로 부족한 작업에서 추가 task-local 문서를 둘 수 있다는 점을 간결하게 반영한다.

## Scope
- 기본 shipped skill에 허용 규칙을 짧게 추가한다.
- migration companion, local direction/reference doc, related test를 같은 방향으로 맞춘다.
- README나 guardrail scope는 넓히지 않는다.

## Current Understanding
- 현재 shipped skill은 task 기본 골격은 잘 설명하지만, task 내부 추가 문서를 언제 둘 수 있는지는 거의 말하지 않는다.
- 새 umbrella term나 예시 파일명을 강하게 밀면 오히려 새 surface contract처럼 읽힐 수 있다.
- checker는 task 디렉터리 안의 extra file을 금지하지 않으므로, 이번 변경은 문구와 drift alignment 중심이면 충분하다.

## Current State
- status는 completed다.
- shipped skill은 `BRIEF.md`와 logs가 부족할 때 역할이 분명한 extra task-local doc을 둘 수 있다고 직접 말한다.
- migration companion과 local docs도 같은 방향으로 설명한다.
- latest validation: `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 -m unittest discover -s tests -p 'test_*.py'`

## Next Step
- 없음

## Working Boundary
- declared read scope: `AGENTS.md`, `docs/reference/model/context-surfaces.md`, `docs/skill-direction.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `skills/project-context/scripts/check_runtime_shape.py`, `tests/project_context/test_runtime_shape.py`
- declared write scope: `docs/reference/model/context-surfaces.md`, `docs/skill-direction.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `tests/project_context/test_runtime_shape.py`, `docs/tasks/2026/03-27/task-extra-doc-guidance/**`
