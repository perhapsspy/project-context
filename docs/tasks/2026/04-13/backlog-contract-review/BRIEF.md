# Backlog Contract Review

## Goal
- `project-context`를 compact하게 유지하면서, task-local future backlog와 repo-level service improvement backlog를 다루는 최소 계약을 다시 정리한다.

## Scope
- `AGENTS.md`
- shipped `skills/project-context/SKILL.md`
- `README.md`
- `README.en.md`
- `docs/skill-direction.md`
- `docs/reference/model/context-surfaces.md`
- 비교 근거로 읽은 `work-board`와 dogfood task docs

## Current Understanding
- 현재 shipped contract는 extra task-local docs를 허용하지만, `BRIEF.md`의 `Next Step / Next Actions`, task-local backlog, repo-level backlog overlay의 역할 경계는 충분히 선명하지 않다.
- `work-board`를 `project-context`와 함께 쓰면 상태 보드보다는 task 문서 포인터 목록으로 축소되기 쉽고, task 내부 진행 상태를 다시 적으면 `BRIEF`, backlog, `working/`, `logs/`와 중복된다.
- 운영 중인 서비스 repo에서는 active task 밖의 refactor/improvement 후보를 repo 차원에서 얇게 잡아둘 surface가 실제로 유용하다.
- 이번 변경은 상태 보드를 코어에 넣지 않고, immediate next step, task-local backlog, optional `docs/BACKLOG.md` overlay를 구분하는 최소 guidance만 올리는 편이 맞다.

## Current State
- `skills/project-context/SKILL.md`, `README`, direction/reference docs, 비교용 `work-board`/dogfood 문서를 읽고 현재 contract 경계를 다시 확인했다.
- shipped guidance는 `BRIEF.md`의 `Next Step / Next Actions`를 immediate next move로 한정하고, one-step을 넘는 carry-over는 role-named task-local backlog로 넘기도록 다시 정리됐다.
- supporting docs는 운영 repo에서 optional `docs/BACKLOG.md` overlay를 허용하되, task 내부 상태 미러링과 완료 항목 누적은 금지하는 방향으로 다시 맞췄다.
- `README`는 랜딩 페이지 수준의 소개만 남기도록 다시 줄였다.
- `docs/skill-direction.md`는 방향 문서 역할에 맞게 철학과 진화 기준만 남기도록 전체를 다시 썼다.
- `docs/reference/model/context-surfaces.md`는 `reference`, `tasks`, `backlog`를 루트 surface 기준으로 다시 구조화했다.
- shipped `SKILL.md`는 backlog 규칙의 반복을 줄이고 같은 계약을 더 짧게 말하도록 압축했다.
- 현재 task logs의 영문 항목도 repo 기본 언어에 맞게 한글로 바로잡았다.
- `AGENTS.md`에도 문서 역할 판단, README/방향 문서/reference의 역할 차이, 로컬 문서 기본 언어를 먼저 점검하게 하는 가드를 추가했다.
- 추가 리뷰를 반영해 shipped `SKILL.md`에는 repo backlog handoff rule을 더 명시했고, README에서는 `task_logs.py` 운영 안내를 제거했으며, `docs/skill-direction.md`도 concrete owner 언급을 더 걷어냈다.
- 브레인스토밍 결과를 반영해 `README`는 surface 정의 링크만 남기는 landing page로 더 줄였고, `docs/skill-direction.md`는 `Purpose / What To Preserve / What To Avoid / When To Revise` 형태로 다시 썼다.
- `docs/reference/model/context-surfaces.md`는 inventory-only 쪽으로 더 얇게 조정했고, shipped `SKILL.md`는 surface one-liner 중심 contract와 단계형 operating model로 다시 압축했다.
- shipped `SKILL.md`를 현재 작업에 직접 다시 적용해 dogfood했고, README 진입, current task reopen, `task_logs.py` append, 현재 task docs 갱신 흐름은 별도 막힘 없이 수행됐다.
- guardrail pass에서 `python3 -m unittest discover -s tests -p 'test_*.py'`와 `python3 skills/project-context/scripts/check_runtime_shape.py`는 통과했고, `python3 skills/project-context/scripts/check_gardening.py`는 기존 `docs/tasks/2026/04-09/backoffice-patch-fielder-dogfood-review`의 extra top-level docs warning만 남겼다.

## Next Step
- 없음

## Latest Validation
- `python3 -m unittest discover -s tests -p 'test_*.py'`
- `python3 skills/project-context/scripts/check_runtime_shape.py`
- `python3 skills/project-context/scripts/check_gardening.py`

## Working Boundary
- declared read scope: `AGENTS.md`, `skills/project-context/SKILL.md`, `README.md`, `README.en.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `docs/tasks/2026/04-09/backoffice-patch-fielder-dogfood-review/**`, `../work-board/**`, `../conalog/backoffice/docs/reference/conventions/task-working-docs.md`, `../conalog/backoffice/docs/tasks/2026/03-31/fieldwork/**`
- declared write scope: `AGENTS.md`, `skills/project-context/SKILL.md`, `README.md`, `README.en.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `docs/tasks/2026/04-13/backlog-contract-review/**`
