# 스킬 방향

## 핵심
- `project-context`에서 에이전트가 실제로 따라야 할 계약은 shipped `SKILL.md`가 맡는다.
- 이 문서는 레포를 만들고 다듬을 때 참고하는 로컬 방향만 다룬다.
- 스킬은 작고, 절차적이고, 언어에 덜 묶인 형태를 우선한다.
- 같은 행동이라면 레포 고유 표현보다 더 안정적인 개념을 먼저 고른다.

## 경계
- 스킬에는 에이전트가 바로 실행해야 하는 행동만 둔다.
- 테스트, dogfood 산출물, 설계 메모는 레포 로컬 지원 자산으로 본다.
- 스크립트는 설치된 skill에서 에이전트가 skill-relative로 실행하거나, 이 레포 유지보수자가 직접 점검할 수 있을 때만 스킬 아래에 둔다.
- `docs/tasks/...`는 대부분의 실제 작업이 머무는 기본 단위다.
- 읽기 전용 질문, 리뷰, 단발 inspection은 bootstrap이나 task 생성을 기본값으로 삼지 않는다.
- `docs/reference/`는 단일 `task`를 넘어 반복 참조될 durable project-domain context만 담는다.
- `docs/reference/`는 필요하면 직접 작성하는 1차 durable surface이며, task 로그의 부산물만 모아두는 곳이 아니다.
- 운영 안내, dogfood 절차, shipped behavior보다 강한 계약은 `docs/reference/`에 두지 않는다.
- `docs/memory.md`는 전역 작업 메모리다. active invariant, 현재 phase, 임시 전역 제약, 현재 유효한 cross-task 조건을 압축해서 담고, topic detail이나 task chronology는 넣지 않는다.

## 톤
- 이름, 요약, help text는 실제로 증명된 범위 중 가장 좁은 범위를 기준으로 잡는다.
- shipped guardrail이 shape, reachability 같은 얇은 runtime 사실만 볼 때는 과한 권위나 보증 표현을 피한다.
- 문서 이름도 역할을 과장하지 않게 고른다. guidance를 contract처럼, thin check를 validator처럼 부르지 않는다.

## 가드레일
- 가드레일은 현재 runtime shape의 drift를 빨리 잡기 위해 존재한다.
- 경로, 파일 존재, 형식, 최신 로그 블록 shape, evidence-pointer reachability, secret-like marker 정도만 본다.
- working read budget 준수나 declared scope 준수 여부는 보지 않는다.
- 의미 품질, merge correctness, 전체 이력의 일관성, 문체까지 보증하지 않는다.

## 진화
- context load를 낮추고 cold-start 재현성을 높이는 방향을 우선한다.
- dogfood 결과는 durable domain context나 cross-task rule이 될 때만 승급한다.
- 레포 로컬 문서는 shipped skill을 보조할 수는 있어도, 새 의무나 더 강한 계약을 덧씌우면 안 된다.
- 이 문서는 방향만 다루고, 구조별 세부 계약은 각 surface가 맡는다.
