# Goal

사용자 정정과 삭제 요청이 `BRIEF.md`에 해설로 보존되지 않고 현재 상태 갱신으로 반영되도록 `project-context` 스킬을 보강한다.

## Scope

- `skills/project-context/SKILL.md`의 `BRIEF.md Ownership` semantic rule 1개 보강
- README, migration skill, examples, direction은 drift 여부만 확인
- installed global `project-context` skill 동기화

## Current Understanding

- `project-context`는 이미 `BRIEF.md`를 rewrite-only compact resume card로 정의하고, 기록과 근거를 logs/working/archive로 보내도록 한다.
- 반복 실패는 규칙 부재보다 사용자 정정·삭제 요청을 현재 상태 변경으로 처리하지 않고 보존할 설명 재료로 착각하는 데 가깝다.
- `structure-first-docs`는 문서 의미 품질을 맡지만, `BRIEF.md`와 logs의 구체적 저장 경계는 `project-context` 소유다.
- 보강 문구는 logs 정책을 새로 만들지 않고, `BRIEF.md`에 남길 결과 상태만 좁게 지정해야 한다.

## Current State

- `skills/project-context/SKILL.md`는 사용자 정정과 삭제 요청을 현재 상태 rewrite로 반영하라는 semantic rule을 포함한다.
- README, migration skill, examples, direction에는 같은 rule을 복제할 필요가 없다.
- runtime shape, full unittest, diff whitespace check는 통과했다.
- task-local 제안과 playground 요약은 보강 근거로 남아 있다.

## Next Step

커밋, 푸시, installed global skill 동기화를 완료한다.

## Working Boundary

- `skills/project-context/SKILL.md`
- `docs/tasks/2026/06-23/brief-correction-boundary/`
