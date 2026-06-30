# structure-first-docs 호출 조건 확장

## 핵심

- 사용자 지적/요청: `structure-first-docs`가 엔지니어링 문서에만 좁게 걸리는 문제가 있었다.
- 에이전트 조치: 실제 문서 정리 요청 동사를 앞세우도록 설명을 넓히고 설치본 확인을 남겼다.
- 드러난 문제: 스킬 설명이 좁으면 사용자가 문서 정리를 요청해도 관련 스킬이 선택되지 않는다.

## 식별

- 저장소: `structure-first`
- 작업: structure-first-docs 호출 조건
- 대략 날짜: 2026-06-23

## 확인한 사실

- 더 강한 호출 문구는 `clean up`, `audit`, `작업 문서`, `handoffs`, `runbooks`, `current-vs-stale`, `기준 출처 담당` 같은 실제 요청 동사/명사를 앞에 둔 것으로 정리됐다.
- 설치본은 `npx skills update structure-first-docs -g -y` 뒤 직접 내용 확인이 필요했다.

## 관련 문서

- `SKILL.md`
- `SKILL.ko.md`
- 전역 설치본

## 증거

- `MEMORY.md:410-442`
- `rollout_summaries/2026-06-23T09-14-07-O8rL-structure_first_docs_trigger_broadening_and_install_sync.md`
- rollout id `019ef3c2-2588-7522-9fb8-b10b58c93989`

## 불확실한 점

- 이번 조사에서는 해당 skill의 현재 frontmatter를 열어 최신 차이 여부를 확인하지 않았다.
