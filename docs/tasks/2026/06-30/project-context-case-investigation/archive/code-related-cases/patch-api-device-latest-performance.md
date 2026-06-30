# device/latest 지연 조사와 공유용 요약

## 핵심

- 사용자 지적/요청: 대형 plant의 `device/latest` 지연 원인을 실제 payload 기준으로 조사할 필요가 있었다.
- 에이전트 조치: 느린 endpoint, `patch-service` 호출 방식, 압축 조건을 조사하고 공유용 요약을 만들었다.
- 드러난 문제: 성능 문제가 “큰 응답”인지 “압축/프록시 비용”인지 분리하지 않으면 대책이 빗나간다.

## 식별

- 저장소: `ops-infra`, sibling `patch-service`
- 작업: device/latest 성능 조사
- 대략 날짜: 2026-06-15, updated 2026-06-17

## 확인한 사실

- 느린 경로는 `GET /api/v3/plants/:plant_id/metrics/device/latest`였다.
- `patch-service`는 `panelLatest`로 `includeState=true`를 호출한다.
- proxy default `Accept-Encoding: gzip, deflate`가 latency story에 포함되었다.

## 관련 문서

- rollout 요약
- Slack 공유용 plain text 요약

## 증거

- `MEMORY.md:1078-1124`
- `rollout_summaries/2026-06-15T09-11-36-mvHg-patch_api_device_latest_compression_investigation.md`
- thread `019eca8c-f696-7de1-977b-f806b7836a46`

## 불확실한 점

- Slack 요약 본문 자체와 benchmark harness 파일은 이번 조사에서 열지 않았다.
