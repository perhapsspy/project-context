# DECISIONS

**2026-03-10**

## 배경

- `case-alpha`에는 system note, deploy runbook, product user guide, auth spike note가 legacy 위치에 흩어져 있었다.
- migration 스킬 계약상 audit map을 먼저 만들고 `TASK -> REFERENCE -> LEAVE` 순서로 적용해야 했다.

## 옵션

- 옵션 A: 현재 사실처럼 보이는 문서를 모두 `reference`로 올린다.
- 옵션 B: 재사용 가능한 현재 truth는 `reference`로, task-local 또는 미확정 문서는 `task`로, 사람용 제품 문서는 leave로 둔다.

## 결정

- 옵션 B를 채택했다.
- `docs/system.md`와 `runbooks/deploy.md`는 canonical reference로 재작성했다.
- `notes/2026-02-14-auth-spike.md`는 미채택 탐색 메모라 별도 task으로 옮겼다.
- `docs/user-guide.md`는 사람용 product doc이므로 legacy 위치에 남겼다.

## 영향

- 이후 에이전트는 `docs/reference/**`만 읽어도 현재 시스템/배포 컨텍스트를 빠르게 찾을 수 있다.
- auth 관련 미확정 탐색 내용은 task 안에서만 추적되어 현재 truth로 오인되지 않는다.
