# 리뷰 방법

## 목적
- `project-context`의 shipped skill, migration skill, README, checker, 로컬 문서를 contract/evidence 기준으로 리뷰한다.

## 기본 원칙
- 문장 취향보다 contract correctness를 우선한다.
- findings는 시작 차단, 잘못된 기대, 역할 혼합, 과한 보증만 올린다.
- 증명되지 않은 확장은 보류한다.
- shipped asset과 repo-local asset은 역할을 나눠 읽는다.

## 용어
- `문제`: 수정 필요, 또는 checker/test가 잡는 상태.
- `follow-up`: 지금 막지는 않지만 다음 변경에서 볼 항목.
- `trade-off`: 운영 선택에 따라 달라지는 판단.
- `observation`: 판단 보류가 필요한 사실.
- 근거가 없으면 `리스크`라고 쓰지 않는다.

## 기준
- 역할: 파일이 자기 역할만 하는가.
- 주장 강도: test/checker/evidence보다 앞서 가지 않는가.
- surface: 새 용어와 구조가 꼭 필요한가.
- 재개성: `BRIEF`, `reference`, `logs` 역할이 섞이지 않는가.
- drift 저항: legacy surface, root mixing, misleading overlay를 줄이는가.
- 정렬: shipped skill, migration skill, direction, tests, examples가 맞는가.

## 절차
1. 대상 파일의 역할을 먼저 정한다.
2. 위 기준으로 blocking issue를 먼저 찾는다.
3. 없으면 현재 수준은 적합하다고 말한다.
4. 남는 항목은 `follow-up`, `trade-off`, `observation` 중 하나로 둔다.
5. 반복적으로 유효한 기준만 `AGENTS.md`나 direction 문서에 승급한다.

## 특히 볼 것
- README는 소개와 시작 진입점만 맡는가.
- direction 문서는 진행 기록이 아니라 기준 맥락인가.
- `reference`가 현재 truth 대신 조사 경과를 담고 있지 않은가.
- long-running guidance가 core required tree처럼 읽히지 않는가.
- gardening checker가 warning-grade drift detector로 남아 있는가.
