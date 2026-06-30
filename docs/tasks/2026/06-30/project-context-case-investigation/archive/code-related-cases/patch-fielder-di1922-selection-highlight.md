# PatchMap selection/highlight 분리와 배포 기록

## 핵심

- 사용자 지적/요청: selection과 highlight가 같은 개념인지 기존 동작 기준으로 다시 확인할 필요가 있었다.
- 에이전트 조치: 둘을 별도 제품 개념으로 분리하고 PR, 릴리스, 운영 배포 증거를 남겼다.
- 드러난 문제: 이미 있는 dimming 동작을 확인하지 않으면 이름만 바꾸고 실제 의미가 섞일 수 있다.

## 식별

- 저장소: `patch-fielder`
- 작업: PatchMap selection/highlight 분리
- 대략 날짜: 2026-06-18 부터 2026-06-22

## 확인한 사실

- PR `#122` / 릴리스 `v0.4.47` 배포 증거가 같은 `MEMORY.md` 구간에 연결돼 있다.
- PR `#123` / 릴리스 `v0.4.48` 배포 증거가 같은 `MEMORY.md` 구간에 연결돼 있다.

## 관련 문서

- task shell
- `runtime-contracts`
- `guide.md`
- `deploy/infra/prod/patch/fielder/deployment.yaml`

## 증거

- `MEMORY.md:588-650`
- `rollout_summaries/2026-06-18T08-03-32-XnsU-di_1922_selection_highlight_split_implementation_and_prod_de.md`

## 불확실한 점

- 해당 task shell의 현재 파일 내용은 이번 조사에서 열람하지 않았다.
