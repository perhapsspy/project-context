# DI-1877 기존 panelmaps 접근 제거와 추적

## 핵심

- 사용자 지적/요청: 작업 ID를 따서 기존 `panelmaps` 접근 제거를 끝까지 진행하라는 요청이 있었다.
- 에이전트 조치: DI-1877로 추적하고 런타임 조회와 폐기된 갱신 경로를 제거한 뒤 커밋/푸시했다.
- 드러난 문제: 겉으로 보이는 조회만 지우면 helper, script, test 경로에 오래된 접근이 남을 수 있다.

## 식별

- 저장소: `backoffice`
- 작업: DI-1877 panelmaps 제거
- 대략 날짜: 2026-06-08

## 확인한 사실

- 기록상 DI-1877 후 backoffice는 운영 `panelmaps` 접근이 필요 없었다.
- `pb.collection('panelmaps')` lookup과 obsolete metadata update paths가 제거됐다.

## 관련 문서

- DI-1877
- `topology-source.js`
- `plants.metadata.remote.js`
- `UpdatePanelModelDialog.svelte`

## 증거

- `MEMORY.md:1541-1564`
- rollout id `019ea5c7-48f1-7a83-9199-286edf9c4755`

## 불확실한 점

- 삭제된 코드의 현재 저장소 상태는 이번 조사에서 재검증하지 않았다.
