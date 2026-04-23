# AGENTS.md

## 목적
- 이 레포는 `project-context` 스킬을 만들고, 점검하고, 유지보수한다.
- 이 파일은 레포 로컬 작성 컨텍스트만 다룬다.
- 에이전트가 따라야 할 실제 동작은 shipped skill 파일에 둔다.

## 기준 문서
- 스킬 방향: [`docs/skill-direction.md`](docs/skill-direction.md)
- 리뷰 기준: [`docs/review-method.md`](docs/review-method.md)
- 도그푸딩 방법: [`docs/dogfood-method.md`](docs/dogfood-method.md)

## 작성 원칙
- 스킬 문장은 같은 역할이면 더 짧은 쪽을 택한다.
- 새 정보가 없으면 다른 말로 반복하지 않는다.
- 이름과 help text는 증명된 가장 좁은 범위로 쓴다.
- 편집 전 문서의 역할과 금지 범위를 먼저 판단한다.
- README, direction, reference, shipped skill contract를 같은 결로 쓰지 않는다.
- shipped skill이나 영어 README처럼 명시적으로 영문이 필요한 파일을 제외하면 한글을 기본으로 쓴다.

## 역할 경계
- README는 소개와 시작 진입점만 맡는다.
- `docs/skill-direction.md`는 철학, 방향, 진화 기준을 맡는다.
- reference 문서는 현재 믿고 쓸 기준 맥락을 담는다.
- shipped skill은 실행 계약을 맡는다.
- repo-local 문서에 shipped contract나 script semantics를 다시 적지 않는다.

## 변경 시 확인
- shipped skill을 바꾸면 README, migration skill, direction, tests, live example 정합성을 본다.
- 경로명이나 핵심 용어를 바꾸면 `rg`로 README, docs, tests의 옛 표현을 확인한다.
- 문구/README/migration 변경은 작은 실제 대상부터 dogfood한다.
- 결과는 시작을 막는 문제와 drift만 남긴다.
- `ARTIFACTS/` 아래 snapshot은 당시 산출물 근거로 남길 수 있다.

## 테스트
- runtime-shape 테스트: `tests/project_context/`
- migration 테스트와 fixture: `tests/project_context_migration/`
- 전체 테스트: `python3 -m unittest discover -s tests -p 'test_*.py'`
