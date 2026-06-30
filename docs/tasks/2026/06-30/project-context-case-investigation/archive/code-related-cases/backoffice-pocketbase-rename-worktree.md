# backoffice pockebase 오타 정리와 분리된 worktree 반영

## 핵심

- 사용자 지적/요청: 기존 변경을 되돌리지 말고 오타 정리만 분리해서 진행하라는 요구가 있었다.
- 에이전트 조치: 분리된 worktree에서 `pockebase`를 `pocketbase`로 정리하고 검증 후 `main`에 반영했다.
- 드러난 문제: 넓은 문자열 정리는 사용자 변경과 섞이면 되돌림 위험이 커진다.

## 식별

- 저장소: `backoffice`
- 작업: PocketBase 오타 정리
- 대략 날짜: 2026-06-23

## 확인한 사실

- 기록상 남은 `pockebase` 문자열은 stale로 보고 저장소 전체 검색 대상에 포함됐다.
- 검증에는 `bun run check`, `DISABLE_ENV_CHECK=true bun run test`, `git diff --check`가 포함됐다.

## 관련 문서

- `src/lib/clients/pocketbase/`
- docs/scripts/Playwright/tests의 낡은 문자열 검색 범위

## 증거

- `MEMORY.md:444-488`
- rollout id `019ef38e-cf88-7842-8f03-72c860fa18c0`

## 불확실한 점

- 현재 저장소에 남은 문자열 존재 여부는 이번 조사에서 `rg`로 확인하지 않았다.
