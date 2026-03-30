# Login Bug Investigation

## 목적
- Safari 로그인 실패 조사 기록을 current truth와 분리해 추적한다.

## 범위
- legacy `tasks/login-bug.md`의 미확정 조사 상태만 canonical task으로 유지한다.
- source note에 trustworthy date가 없어 migration date `2026-03-10`를 task date로 사용한다.

## 현재 이해
- intermittent login failure를 Safari에서 재현했다.
- temporary logging을 추가했다.
- root cause는 아직 확인되지 않았다.

## 현재 산출물 스냅샷
- 조사 상태는 reference로 승급되지 않고 task-local로 남아 있다.

## 현재 상태
- status는 open이다.
- blockers: 없음
- note: source note에 trustworthy date가 없어 2026-03-10을 migration date로 사용했다
- latest validation: migrated historical task snapshot

## Next Step
- root cause를 확인한다.

## Working Boundary
- declared read scope: migrated legacy task note only
- declared write scope: task-local docs only
