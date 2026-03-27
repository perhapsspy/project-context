# Task Extra Doc Guidance

- owner: codex
- started_at: 2026-03-27
- status: completed

## Goal
- `project-context` task contract에 `BRIEF.md`/`STATUS.md`만으로 부족한 작업에서 추가 task-local 문서를 둘 수 있다는 점을 간결하게 반영한다.

## Scope
- 기본 shipped skill에 허용 규칙을 짧게 추가한다.
- migration companion, local direction/reference doc, related test를 같은 방향으로 맞춘다.
- README나 guardrail scope는 넓히지 않는다.

## Current Understanding
- 현재 shipped skill은 task 기본 골격은 잘 설명하지만, task 내부 추가 문서를 언제 둘 수 있는지는 거의 말하지 않는다.
- 새 umbrella term나 예시 파일명을 강하게 밀면 오히려 새 surface contract처럼 읽힐 수 있다.
- checker는 task 디렉터리 안의 extra file을 금지하지 않으므로, 이번 변경은 문구와 drift alignment 중심이면 충분하다.

## Current Output Snapshot
- `skills/project-context/SKILL.md`는 `BRIEF.md`/`STATUS.md`가 부족할 때 추가 task-local 문서를 둘 수 있고 역할 중복을 피하라고 직접 말한다.
- `skills/project-context-migration/SKILL.md`, `docs/reference/model/context-surfaces.md`, `docs/skill-direction.md`는 같은 방향으로 task-local extra docs를 새 필수 surface 없이 설명한다.
- `tests/project_context/test_runtime_shape.py`는 extra task-local doc이 runtime-shape check 대상 core file이 아니라는 점을 고정한다.
