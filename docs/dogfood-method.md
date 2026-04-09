# 도그푸딩 방법

## 목적
- 이 문서는 shipped skill이나 로컬 운영 문서를 바꿀 때 다시 써 보며 검증하는 최소 dogfood 루프를 정리한다.
- 목표는 의견 수집이 아니라, 변경이 reopen 흐름과 drift 억제에 실제로 도움이 되는지 확인하는 것이다.

## 원칙
- dogfood는 가장 작은 실제 변경을 대상으로 한다.
- 설계 설명만 읽지 말고, 같은 턴 안에서 한 번은 실제로 써 본다.
- 결과는 "무엇이 막혔는가", "무엇이 과했는가", "무엇이 그대로 유지돼도 되는가"만 남긴다.
- 외부 repo는 기본적으로 read-only evidence로만 다룬다.

## 기본 루프
1. 대상 변경을 하나 고른다.
2. shipped skill, 로컬 방향, 필요한 보조 문서만 읽고 작업을 수행한다.
3. 작업 중 `BRIEF.md`, logs, 관련 guidance가 실제로 reopen/handoff에 충분한지 확인한다.
4. runtime shape, gardening check, 전체 테스트를 다시 돌린다.
5. 필요하면 mature repo 1개, newer repo 1개에 read-only spot check를 해 warning이나 wording이 너무 noisy한지 본다.
6. 결과는 task-local doc과 logs에 남긴다.

## 권장 Pass

### 1. Activation Pass
- 본다: 어떤 문서를 먼저 읽어야 하는지, 시작 조건이 과한지.
- 성공 기준: 시작 경로가 짧고 README나 direction 문서가 shipped contract를 다시 정의하지 않는다.

### 2. Write Pass
- 본다: 실제 작은 변경을 할 때 guidance가 과하게 폼을 강제하지 않는지.
- 성공 기준: 코어 contract를 깨지 않고 수정할 수 있고, 새 guidance가 required tree처럼 읽히지 않는다.

### 3. Reopen Pass
- 본다: 방금 만든 변화가 나중 세션에서 다시 열기 쉬운지.
- 성공 기준: `BRIEF.md`가 실제 read/write scope와 current state를 따라가고, current docs와 append-only logs의 역할이 섞이지 않는다.

### 4. Guardrail Pass
- 본다: 테스트와 thin checker가 여전히 통과하는지.
- 최소 실행: `python3 -m unittest discover -s tests -p 'test_*.py'`, `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 skills/project-context/scripts/check_gardening.py`

### 5. Drift Pass
- 본다: mature repo에서 warning이나 wording이 실제 drift를 잘 집는지.
- 이 단계는 read-only evidence 수집이며, external repo를 수정 대상으로 바꾸지 않는다.

## 이번 레포에서 특히 볼 것
- direction 문서가 process note로 비대해지지 않는가.
- review method가 취향 문서가 아니라 contract/evidence 기준으로 작동하는가.
- long-running task guidance가 helper lane 예시를 사실상 표준 tree처럼 밀어 넣지 않는가.
- gardening wording이 semantic authority처럼 읽히지 않는가.
