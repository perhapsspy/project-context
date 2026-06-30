# home anomaly 0건과 감지 전 상태 조사

## 핵심

- 사용자 지적/요청: 아침 대시보드의 `0건` 표시가 실제 0인지 감지 전 상태인지 구분할 필요가 있었다.
- 에이전트 조치: home route와 anomaly logic을 담당 문서부터 따라가고 cache/refresh 영향을 기록했다.
- 드러난 문제: `0`으로 채워진 표시가 실제 이상 없음과 감지 전 상태를 구분하지 못할 수 있다.

## 식별

- 저장소: `patch-service`
- 작업: home anomaly 상태 조사
- 대략 날짜: 2026-06-22

## 확인한 사실

- home anomaly chain은 `/app` layout queries에서 dashboard widget rows로 이어지는 것으로 기록되어 있다.
- missing anomaly rows가 `0`으로 채워질 수 있다고 기록되어 있다.
- cache와 refresh 주기가 morning window 표시 지속에 영향을 줄 수 있다고 기록되어 있다.

## 관련 문서

- anomaly 기술 설계 문서
- home route/current 로직 추적
- rollout 요약

## 증거

- `MEMORY.md:797-834`
- `rollout_summaries/2026-06-22T01-12-48-VpmJ-home_anomaly_zero_vs_not_yet_detected_ux.md`
- thread `019eece3-20bb-7a72-8bb1-28f3539adbfd`

## 불확실한 점

- 이번 조사에서는 현재 코드와 설계 문서를 다시 열어 차이 여부를 확인하지 않았다.
