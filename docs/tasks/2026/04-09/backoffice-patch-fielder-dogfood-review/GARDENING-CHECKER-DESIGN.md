# Gardening Checker Design

## Goal

현재 `check_runtime_shape.py`의 thin contract는 유지하면서, mature repo drift를 warning 중심으로 점검하는 optional gardening loop를 설계한다.

## Why Separate It

- runtime shape checker는 stable core contract를 확인하는 용도다.
- gardening checks는 false positive 가능성이 더 높고 repo maturity에 따라 기준도 달라진다.
- 둘을 한 스크립트에 같은 severity로 섞으면 코어 contract의 신뢰도가 떨어진다.

결론:
- `check_runtime_shape.py`는 그대로 둔다.
- gardening은 별도 script 또는 별도 mode로 분리한다.

## Proposed Form

### Option A

- `skills/project-context/scripts/check_gardening.py`

장점:
- 역할이 가장 분명하다.
- fail-grade core contract와 warn-grade repo hygiene를 분리하기 쉽다.

### Option B

- `check_runtime_shape.py --gardening`

장점:
- 실행 진입점이 하나다.

단점:
- core checker와 optional drift checks 경계가 흐려질 수 있다.

권장:
- Option A

## Severity Model

- `FAIL`
  - current core contract 위반
  - existing `check_runtime_shape.py`가 계속 담당

- `WARN`
  - repo health에는 나쁘지만 즉시 contract violation은 아닌 항목

- `INFO`
  - action candidate이지만 자동 판단 오탐 가능성이 높은 항목

gardening checker는 기본적으로 `WARN`/`INFO`만 낸다.
CI에서 쓸 때도 기본은 non-zero exit가 아니라 text report를 추천한다.

## Proposed Checks

### 1. Empty Task Dir

signal:
- `docs/tasks/yyyy/mm-dd/<slug>/`가 있지만 core files가 없다.

why:
- 실제로 `patch-fielder`에서 발생했다.

severity:
- `WARN`

### 2. Legacy Surface Respawn

signal:
- recent task 또는 repo root에서 `STATUS.md`, `docs/memory.md`, `MEMORY-CANDIDATES.md`가 다시 생겼다.

why:
- contract drift를 빨리 발견할 수 있다.

severity:
- `WARN`

note:
- historic legacy files 전체를 에러로 만들지는 않는다.
- 최근 생성분 또는 touched file만 보는 옵션이 낫다.

### 3. Extra Task Doc Growth

signal:
- single task의 top-level task-local docs가 일정 개수 이상이다.

suggested threshold:
- top-level extra docs 4개 이상: `INFO`
- 7개 이상: `WARN`

why:
- task-local supplement가 domain manual로 변하는 early sign이다.

limit:
- 많이 필요해서 legitimately 큰 task도 있으므로 fail로 두지 않는다.

### 4. Root Overlay Mixing

signal:
- task root에 canonical current-state docs와 active rework docs가 같은 레벨로 섞여 있다.

heuristics:
- root file names에 `PLAN`, `REWORK`, `BACKLOG`, `MIGRATION`, `POLICY`, `FLOW` 같은 overlay 성격 단어가 여러 개 보인다.
- 동시에 `MODEL`, `CONTRACTS`, `SYSTEM_BOUNDARIES`, `EXECUTION` 같은 canonical docs도 같은 레벨에 있다.
- `validation/`이나 `archive/`에 가도 될 evidence-style docs가 root에 남아 있다.

severity:
- `INFO`

suggestion:
- task root에는 canonical docs만 남기고, temporary working notes는 `working/`, finished overlays는 `archive/`로 분리할지 검토한다.

### 5. Long-Running Task Drift

signal:
- 하나의 dated task가 장기간 갱신되며 current operating model을 계속 품고 있다.

heuristics:
- 최근 N일 동안 반복 갱신
- extra docs 다수
- sibling repo/reference links 다수
- current state보다 durable contract 설명 비중이 큼

severity:
- `INFO`

use:
- stream/area 분리 후보 탐지

### 6. Portable Path Drift Beyond Core Scan

signal:
- core checker는 이미 absolute path를 fail로 본다.
- gardening은 fail 전 단계의 risky phrasing도 안내할 수 있다.

examples:
- 개인 로컬 host 이름
- personal tmp file naming convention
- checker script 개인 설치 경로를 설명하는 문장

severity:
- `INFO`

### 7. Overlay Duplication Drift

signal:
- `AGENTS.md`, `docs/README.md`, `docs/reference/overview.md`가 같은 contract 설명을 과도하게 중복한다.

pragmatic heuristic:
- same legacy surface keywords repeated across overlay docs
- one file가 이미 제거된 surface를 다른 overlay가 다시 안내

severity:
- `INFO`

note:
- 이 검사는 정확도보다 review cue에 가깝다.

## Output Shape

```text
[WARN] empty-task-dir: docs/tasks/2026/04-07/ios-blank-page-compat
  suggestion: create BRIEF/logs or remove the directory

[INFO] task-extra-doc-growth: docs/tasks/2026/03-31/fieldwork (7 extra top-level docs)
  suggestion: promote durable rules to docs/reference/** or treat as stream candidate

[INFO] root-overlay-mixing: docs/tasks/2026/03-31/fieldwork
  suggestion: keep canonical docs at root and move temporary working notes into working/
```

## Suggested CLI

```bash
python3 <project-context-skill>/scripts/check_gardening.py --repo-root <repo-root>
```

optional flags:

```text
--recent-days 30
--warn-extra-docs 7
--info-extra-docs 4
--json
```

## Suggested Adoption Order

1. implement `empty-task-dir`
2. implement `legacy-surface-respawn`
3. implement `extra-task-doc-growth`
4. implement `root-overlay-mixing`
5. dogfood on `backoffice`, `patch-fielder`
6. decide whether `long-running-task-drift` is useful enough to keep

## Non-Goals

- 문서 의미 품질을 자동 채점하지 않는다.
- 어떤 task가 정말 잘 쪼개졌는지까지 강제하지 않는다.
- reference 내용이 충분한지 semantic completeness를 판정하지 않는다.
- style guide linter가 되지 않는다.
