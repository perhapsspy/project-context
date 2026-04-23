# 도그푸딩 방법

## 목적
- shipped skill이나 로컬 운영 문서 변경이 reopen 흐름과 drift 억제에 실제로 도움이 되는지 확인한다.

## 원칙
- 가장 작은 실제 변경으로 검증한다.
- 설명만 읽지 말고 같은 턴에서 한 번은 직접 써 본다.
- 결과는 막힌 점, 과한 점, 그대로 둘 점만 남긴다.
- 외부 repo는 기본적으로 read-only evidence로만 본다.

## 기본 루프
1. 대상 변경 하나를 고른다.
2. shipped skill, direction, 필요한 보조 문서만 읽고 작업한다.
3. `BRIEF.md`, logs, guidance가 reopen/handoff에 충분한지 본다.
4. task 직결 check를 먼저 돌리고, 마감 전 runtime shape, gardening, 전체 테스트를 본다.
5. 필요하면 mature repo 1개, newer repo 1개를 read-only spot check한다.
6. 결과는 task-local doc과 logs에 짧게 남긴다.

## Pass
- Activation: 시작 경로가 짧고 README/direction이 shipped contract를 재정의하지 않는가.
- Write: 작은 변경이 과한 형식 강제 없이 가능한가.
- Reopen: `BRIEF`, `reference`, `logs`가 역할대로 재개 정보를 주는가.
- Guardrail: runtime shape, gardening, 전체 테스트가 통과하는가.
- Drift: warning과 wording이 실제 drift만 잡고 noisy하지 않은가.

## 최소 실행
- `python3 -m unittest discover -s tests -p 'test_*.py'`
- `python3 skills/project-context/scripts/check_runtime_shape.py`
- `python3 skills/project-context/scripts/check_gardening.py`

## 특히 볼 것
- direction 문서가 process note로 비대해지지 않는가.
- review method가 취향 문서가 아니라 contract/evidence 기준인가.
- long-running guidance가 helper lane 예시를 표준 tree처럼 밀지 않는가.
- gardening wording이 semantic authority처럼 읽히지 않는가.
