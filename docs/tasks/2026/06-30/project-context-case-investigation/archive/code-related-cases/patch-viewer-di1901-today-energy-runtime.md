# DI-1901 오늘 발전량/발전시간 사건 정리

## 핵심

- 사용자 지적/요청: viewer 코드만 보지 말고 upstream 최신 상태와 날짜 판단까지 확인할 필요가 있었다.
- 에이전트 조치: `todayRuntime`, `currentEnergy.daily`, `local_date`, 배포 상태를 함께 조사하고 마무리했다.
- 드러난 문제: 화면의 `-` 표시를 viewer 문제로만 보면 upstream 날짜/상태가 오래된 문제를 놓칠 수 있다.

## 식별

- 저장소: `patch-viewer-custom`
- 작업: DI-1901 오늘 발전량 정리
- 대략 날짜: 2026-06-16

## 확인한 사실

- `todayRuntime`은 `currentEnergy.daily`에서 파생된다.
- `local_date`가 today 판단의 우선 확인값으로 기록되어 있다.
- green 배포 워크플로 후에도 클러스터가 `v0.1.43`에 남아 `kubectl apply`와 운영 증거가 필요했던 사실이 기록되어 있다.

## 관련 문서

- Data Infra Tasks
- rollout 요약
- 배포 manifest
- 릴리스/배포 노트

## 증거

- `MEMORY.md:1186-1231`
- `rollout_summaries/2026-06-16T02-07-46-FimR-di_1901_today_energy_timezone_merge_release_deploy_closeout.md`
- thread `019ece2f-4be9-7592-bb6d-da9f4fda6329`

## 불확실한 점

- Notion 종료 문서의 실제 항목 내용은 이번 조사에서 확인하지 않았다.
