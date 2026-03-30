# AGENTS.md

## 목적
- 이 레포는 `project-context` 스킬을 만들고, 점검하고, 유지보수하기 위해 존재한다.
- 이 파일은 레포 로컬 작성 컨텍스트만 다룬다.
- 에이전트가 직접 따라야 할 스킬 동작은 이 파일이 아니라 shipped skill 파일에 둔다.
- 스킬과 레포 로컬 자산의 경계는 [`docs/skill-direction.md`](docs/skill-direction.md)를 본다.
- 이름과 help text는 실제로 증명된 범위 중 가장 좁은 범위를 기준으로 잡고, 얇은 guardrail에 과한 보증 톤을 싣지 않는다.
- 스킬 문장은 같은 역할이면 더 짧은 쪽을 택하고, 새 정보가 없으면 다른 말로 반복하지 않는다.
- 문구/README/migration 변경은 가장 작은 실제 대상부터 dogfood하고, 시작을 막는 문제와 drift만 결과로 남긴다.
- shipped skill을 바꿀 때는 README, migration skill, `docs/skill-direction.md`, 관련 tests와 live repo example이 함께 어긋나지 않는지 점검한다.
- 경로명이나 핵심 용어를 바꿨다면 `rg`로 README, docs, tests에 옛 표현이 남지 않았는지 확인한다.
- 레포의 live task 예시는 현재 shipped contract를 따라야 한다. 다만 `ARTIFACTS/` 아래의 비교용 snapshot은 당시 산출물 근거로 남길 수 있다.

## 테스트
- runtime-shape guardrail 테스트는 [`tests/project_context/`](tests/project_context/) 아래에 둔다.
- `project-context-migration` 테스트와 fixture는 [`tests/project_context_migration/`](tests/project_context_migration/) 아래에 둔다.
- 레포 전체 테스트 진입점은 `python3 -m unittest discover -s tests -p 'test_*.py'`를 우선 사용한다.
