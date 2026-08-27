# 스킬 방향

## 목적
- shipped `project-context` contract를 작고, 읽기 쉽고, 재개 가능하게 유지한다.

## 유지할 것
- 저장소 안의 파일을 우선한다.
- 코어 계약은 작게 둔다.
- 사람이 바로 읽고 고칠 수 있는 구조를 택한다.
- shipped skill과 script의 authority는 shipped asset에 둔다.
- repo-local 문서는 local adapter 역할만 맡는다.
- `reference`는 현재 믿고 쓸 기준 맥락을 담는다.
- 여러 작업이 구현이나 승인 판정을 바꾸는 해석을 공유하면 기존 정본을 우선하고, 작업 전용 계약은 task root, 재사용 계약은 `docs/reference/**`에 담당자 하나를 둔다.
- `BRIEF.md`는 얇게, `Scope`는 파일 목록이 아닌 작업 경계로 쓴다.
- 긴 작업은 phase boundary마다 `BRIEF.md`를 다시 써서 현재 재개 상태만 남기고, 단계 이력은 `logs/`, 사람이 읽는 초안·미결 계획·간결한 근거는 `working/`, 완료·대체·stale context는 `archive/`로 보낸다.
- 저장 위치는 사용 횟수가 아니라 보존 책임으로 정한다.

## 피할 것
- 숨은 메모리나 외부 시스템을 계약처럼 만들지 않는다.
- 증명되지 않은 surface를 이름이나 help text에 싣지 않는다.
- shipped contract나 script semantics를 repo-local 문서에 다시 적지 않는다.
- `reference`를 조사 메모, 진행 로그, provenance 설명으로 쓰지 않는다.
- optional pattern을 required tree처럼 보이게 하지 않는다.
- 큰 task의 root 문서를 evidence, draft, report, cleanup plan이 섞인 창고로 키우지 않는다.

## 수정 기준
- 같은 drift가 반복될 때만 shipped contract를 바꾼다.
- 새 규칙은 기존 surface를 선명하게 할 때만 추가한다.
