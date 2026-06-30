# PatchAgent 사건를 현재 guardrail로 흡수

## 핵심

- 사용자 지적/요청: 과거 사건 문서가 현재 guardrail과 섞이지 않게 정리할 필요가 있었다.
- 에이전트 조치: 재사용 가능한 조사 순서와 guardrail만 남기고 과거 사건성 기록은 분리했다.
- 드러난 문제: 사건 기록을 현재 기준처럼 두면 다음 조사가 낡은 상태를 따를 수 있다.

## 식별

- 저장소: `ops-infra`
- 작업: PatchAgent guardrail 정리
- 대략 날짜: 2026-05-26

## 확인한 사실

- MEMORY에는 이 사건의 키워드로 PatchAgent, USB serial 담당, allowlist-first, 기존/new edge-agent 혼재, ReceiverThread, `last_data_at`이 기록돼 있다.

## 관련 문서

- `edge-repositories.md`

## 증거

- `MEMORY.md:1617-1629`

## 불확실한 점

- 이번 조사에서는 해당 rollout 요약를 열지 않았기 때문에 사건의 상세 증상, 변경 파일, 검증 결과는 확인하지 않았다.
