# Log Script Hardening

## Goal
- `project-context`가 `logs/*.md` 직접 편집보다 `task_logs.py` 경로를 기본으로 타게 하고, latest block이 깨져 있어도 append 흐름이 쉽게 막히지 않게 만든다.

## Scope
- shipped `project-context` guidance
- README guidance
- `skills/project-context/scripts/task_logs.py`
- related tests

## Current Understanding
- 현재 shipped guidance는 로그 입력을 스크립트 경로로 강하게 밀지 않아 일반 write-bearing task에서 직접 편집 우회가 남아 있다.
- 현재 `task_logs.py`는 malformed latest block을 만나면 append/tail/check가 바로 막혀, 실무적으로는 직접 편집을 fallback처럼 학습시키기 쉽다.
- runtime checker는 결과 shape만 검증하므로 provenance 검출보다 contract hardening과 append ergonomics 개선이 우선이다.

## Current State
- status는 completed다.
- shipped guidance와 README는 `task_logs.py`를 기본 log-write path로 쓰게 강화됐다.
- `task_logs.py` append는 malformed latest block이나 heading 없는 legacy tail이 있어도 새 valid latest block을 뒤에 추가해 normal flow를 이어갈 수 있다.
- related tests는 malformed latest-block append coverage와 cross-platform path output expectation을 포함하도록 갱신됐다.
- blockers는 없다.

## Next Step
- 없음

## Latest Validation
- `python3 -m unittest tests.project_context.test_task_logs`
- `python3 -m unittest tests.project_context.test_runtime_shape`
- `python3 -m unittest discover -s tests -p 'test_*.py'`
- `python3 skills/project-context/scripts/check_runtime_shape.py`
- `python3 skills/project-context/scripts/task_logs.py worklog check --task-root docs/tasks/2026/04-13/log-script-hardening`
- `python3 skills/project-context/scripts/task_logs.py decision check --task-root docs/tasks/2026/04-13/log-script-hardening`

## Related Docs
- `skills/project-context/SKILL.md`
- `skills/project-context/scripts/task_logs.py`
- `README.md`
- `README.en.md`

## Working Boundary
- declared read scope: `AGENTS.md`, `README*.md`, `docs/skill-direction.md`, `skills/project-context/**`, `skills/project-context-migration/SKILL.md`, `tests/project_context/**`, `docs/tasks/2026/04-05/log-tooling-minimum/**`
- declared write scope: `README*.md`, `skills/project-context/SKILL.md`, `skills/project-context/scripts/task_logs.py`, `tests/project_context/**`, `docs/tasks/2026/04-13/log-script-hardening/**`
