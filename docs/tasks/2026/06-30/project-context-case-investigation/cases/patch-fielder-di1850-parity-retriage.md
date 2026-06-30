# DI-1850 parity 후보 재분류와 문서 재정리

## 핵심

- 사용자 지적/요청: 이전 제외 판단을 믿지 말고 현재 소스 기준으로 다시 보라는 사용자 지적이 있었다.
- 에이전트 조치: `DI1850-FLD-101~104`를 열린 parity 보강 항목으로 되돌리고 증거를 `PORTING-LEDGER.md`, `working/`, 로그로 분리했다.
- 드러난 문제: 불확실성을 제외 결정으로 바꾸면 parity 후보가 너무 일찍 닫힌다.

## 식별

- 저장소: `patch-fielder-di-1850-fieldwork`
- 작업: DI-1850 parity 재분류
- 대략 날짜: 2026-06-20

## 확인한 사실

- `TODO.md`가 상태 덤프처럼 커졌다.
- 자세한 증거는 `PORTING-LEDGER.md`, `working/`, 로그로 이동하는 형태로 정리됐다.

## 관련 문서

- `BRIEF.md`
- `TODO.md`
- `PORTING-LEDGER.md`
- `working/*`
- `logs/DECISIONS.md`
- `logs/WORKLOG.md`

## 증거

- `MEMORY.md:521-586`
- `rollout_summaries/2026-06-19T15-01-23-AC7l-di_1850_fielder_parity_reset_new_session_handoff.md`
- rollout id `019ee066-a37c-7ac1-8c67-0a4c98e34a0f`

## 불확실한 점

- 현재 저장소 파일의 최신 내용은 이번 조사에서 열람하지 않았다.
