# Dogfood Run

## Goal
- 현재 `project-context` 변경셋이 실제 reopen 흐름과 drift 억제 관점에서 쓸 만한지, 이 레포 안에서 직접 다시 써 보며 점검한다.

## Method
- 기준은 [`docs/dogfood-method.md`](../../../../dogfood-method.md) 를 따른다.
- 외부 repo는 read-only evidence로만 보고, 수정은 이 레포 안에서만 한다.

## Executed Passes

### Activation Pass
- 입력:
  - [`AGENTS.md`](../../../../AGENTS.md)
  - [`skills/project-context/SKILL.md`](../../../../skills/project-context/SKILL.md)
  - [`docs/skill-direction.md`](../../../../docs/skill-direction.md)
  - [`docs/review-method.md`](../../../../docs/review-method.md)
- 결과:
  - 시작 경로는 짧았다.
  - `skill-direction`가 기준 문서 역할로 돌아오면서 shipped contract와의 경계가 더 분명해졌다.

### Write Pass
- 수행:
  - long-running helper lane naming을 `working/`으로 통일했다.
  - `review-method`를 별도 로컬 문서로 분리했다.
  - shipped guidance를 helper-lane example 수준으로 약화했다.
- 결과:
  - 코어 contract를 늘리지 않고도 조정이 가능했다.
  - `working/` example은 `workitems/`보다 넓은 temporary-note 용도에 더 잘 맞았다.

### Reopen Pass
- 확인:
  - 현재 task [`BRIEF.md`](./BRIEF.md) 를 다시 읽고, 실제 변경 범위와 current state가 따라갔는지 확인했다.
- 발견:
  - 이전 상태에서는 `declared write scope`가 이미 실제 변경 범위를 따라가지 못했다.
  - `docs/skill-direction.md`의 현재 구조 설명도 한 차례 stale해져 있었다.
  - 같은 턴에서 추가한 task-local 링크가 `/Users/...` 절대경로로 저장돼 runtime-shape check를 깨뜨렸다.
- 조치:
  - 이번 턴에서 `BRIEF.md` current state, next step, working boundary를 현재 실작업 범위에 맞게 다시 썼다.
  - task-local 링크는 상대경로 형태로 다시 고쳤다.

### Guardrail Pass
- 실행:
  - `python3 -m unittest discover -s tests -p 'test_*.py'`
  - `python3 skills/project-context/scripts/check_runtime_shape.py`
  - `python3 skills/project-context/scripts/check_gardening.py`
- 결과:
  - `check_runtime_shape.py`는 통과했다.
  - gardening은 현재 research task 자체에 대해 `task-extra-doc-growth` INFO 1건을 냈다.
  - 전체 `unittest discover`는 latest `main`에서 들어온 `tests/project_context/test_task_logs.py`의 경로 구분자 기대치 때문에 macOS에서 실패한다.
  - 이 warning은 실패는 아니지만, research package가 일반 task보다 top-level docs를 더 쉽게 늘린다는 점을 보여 준다.

### Drift Pass
- read-only evidence:
  - `../conalog/backoffice/docs/reference/conventions/task-working-docs.md`
  - `../conalog/backoffice/docs/tasks/2026/03-31/fieldwork/working/README.md`
  - `../conalog/backoffice/docs/tasks/2026/04-09/infra-pocketbase-logs/working/README.md`
- 결과:
  - helper lane의 이름보다 원칙이 더 중요하다는 점이 확인됐다.
  - 흡수 가치가 있는 것은 `root stable docs`, `temporary working notes`, `archive`, `done/undone authority 고정`의 네 가지였다.
  - `working/README.md` 자체나 `IMPLEMENTATION_BACKLOG.md`를 코어 surface로 올릴 근거는 없었다.

## Findings
- blocking issue 없음
- 실제 dogfood에서 유의미했던 drift:
  - 현재 task `BRIEF.md`가 실작업 write scope와 stale heading 설명을 한 차례 놓쳤다.
  - task-local 링크가 절대경로로 저장돼 runtime-shape check를 실제로 깨뜨렸다.
  - gardening은 현재 research task도 extra-doc-growth로 바로 잡았다.
- 이번 변경으로 얻은 교정:
  - helper lane는 optional example로만 둔다.
  - 현재 guidance vocabulary는 `working/`으로 통일한다.
  - direction 문서와 review/dogfood method 문서는 역할별로 분리한다.

## Follow-Ups And Observations
- follow-up: `working/` example이 다른 repo에서도 계속 가장 자연스러운지는 추가 dogfood가 더 필요하다.
- observation: append-only logs에는 과거 `workitems/` 대안 검토 흔적이 남아 있으므로, current docs와 historical trail의 역할 구분을 계속 지켜야 한다.
