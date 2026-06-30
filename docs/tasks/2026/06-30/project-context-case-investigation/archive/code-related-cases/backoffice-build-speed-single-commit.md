# backoffice 빌드 속도 조사와 커밋 하나로 정리

## 핵심

- 사용자 지적/요청: 빌드 속도 조사 뒤 중간 커밋이 늘어난 상태를 정리하라는 요청이 있었다.
- 에이전트 조치: 최종 변경만 남기도록 커밋 하나로 접고 `main`에 `force-with-lease`로 반영했다.
- 드러난 문제: 탐색 과정의 커밋과 최종 변경 경계가 섞이면 나중에 무엇이 실제 결과인지 추적하기 어렵다.

## 식별

- 저장소: `backoffice`
- 작업: 빌드 속도 조사와 커밋 정리
- 대략 날짜: 2026-06-11

## 확인한 사실

- 기록상 재사용 워크플로에는 이미 GHA buildx cache 설정이 있었다.
- 로컬 Docker Desktop 4GB 환경에서는 Vite 단계가 `SIGKILL`/`cannot allocate memory`로 실패할 수 있었다.

## 관련 문서

- `Dockerfile`
- `.dockerignore`
- reusable `build and push` 워크플로 기록

## 증거

- `MEMORY.md:1696-1724`
- rollout id `019eb602-507b-7bc3-bb59-b21090e7634f`

## 불확실한 점

- 실제 커밋 그래프와 워크플로 파일의 현재 내용은 이번 조사에서 확인하지 않았다.
