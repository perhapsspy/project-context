# Log Tooling Minimum

## Goal
- `project-context`가 task logs를 직접 patch하지 않고도 append-only로 다루게 하는 최소 툴링을 추가한다.

## Scope
- shipped `project-context` skill contract
- log append/tail/check tooling
- runtime-shape checker의 latest-log-block 판독 경로
- related tests

## Current Understanding
- 현재 contract는 `BRIEF.md`를 reopen entrypoint로 두고 logs는 필요할 때만 보게 하지만, tooling 없이 markdown을 직접 patch하면 append-only 보장이 약하다.
- 현재 runtime-shape checker는 최신 블록만 검증하면서도 로그 파일 전체를 읽는다.
- 최소안은 ordinary file contract를 유지하면서 에이전트의 log 접근을 작은 CLI 인터페이스로 좁히는 것이다.

## Current State
- status는 completed다.
- blockers는 없다.
- `skills/project-context/scripts/task_logs.py`는 `worklog`와 `decision` surface로 나뉜 CLI를 제공한다.
- `WORKLOG`는 `worklog append/tail/check`로 다루고, `DECISIONS`는 `decision append/tail/check`로 다룬다.
- `append`는 existing task root와 `BRIEF.md`가 없는 경로를 거부해 mistyped `--task-root`가 orphan log tree를 만들지 못하게 한다.
- `check_runtime_shape.py`는 latest-log-block 판독에 새 log reader를 재사용해 로그 파일 전체를 다시 펼치지 않는다.
- shipped skill은 가능하면 logs를 직접 patch하지 말고 bundled script를 쓰도록 안내한다.
- contract-focused tests가 split CLI surface와 runtime-shape 흐름을 함께 검증한다.
- subagent dogfood에서 happy path, nested/subdir path, failure path 모두 기능상 통과했다.
- dogfood와 리뷰에서 나온 follow-up 두 개도 반영했다: `check_runtime_shape.py` 성공 출력은 selected repo root를 같이 보여주고, `task_logs.py` help와 shipped skill 문구는 existing-task requirement와 PowerShell empty-bullet caveat를 짧게 설명한다.
- re-dogfood에서 missing task root, missing `BRIEF.md`, older date append, invalid log name, empty bullet, multiline bullet, malformed latest block이 모두 의도한 failure를 냈다.
- `decision append`가 같은 날짜와 날짜 변경 양쪽에서 원자적으로 새 decision block을 추가하는지 확인했고, `decision check`와 runtime checker는 최신 decision block이 정확히 4 bullet일 때만 통과한다.
- latest re-review에서도 새 findings는 없었다. 남은 리스크는 PowerShell `--bullet ""` parsing edge case와, non-canonical task path에서는 경로 출력이 절대경로 fallback을 쓰는 점 정도다.
- latest validation: `python skills/project-context/scripts/task_logs.py worklog check --task-root docs/tasks/2026/04-05/log-tooling-minimum`, `python skills/project-context/scripts/task_logs.py decision check --task-root docs/tasks/2026/04-05/log-tooling-minimum`, `python skills/project-context/scripts/check_runtime_shape.py`, `python -m unittest tests.project_context.test_task_logs tests.project_context.test_runtime_shape`, `python -m unittest discover -s tests -p 'test_*.py'`

## Next Step
- 없음

## Related Docs
- `skills/project-context/SKILL.md`
- `skills/project-context/scripts/task_logs.py`
- `skills/project-context/scripts/check_runtime_shape.py`
- `tests/project_context/test_task_logs.py`
- `tests/project_context/test_runtime_shape.py`

## Working Boundary
- declared read scope: `AGENTS.md`, `README*.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context/scripts/check_runtime_shape.py`, `tests/project_context/**`, `docs/tasks/2026/03-30/task-surface-reduction/**`, `docs/tasks/2026/04-05/log-tooling-minimum/**`
- declared write scope: `README*.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context/scripts/**`, `tests/project_context/**`, `docs/tasks/2026/04-05/log-tooling-minimum/**`
