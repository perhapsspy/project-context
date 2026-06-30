# structure-first 호출 설명과 이식 가능한 로그 정리

## 핵심

- 사용자 지적/요청: 코딩 작업에서 `structure-first`가 충분히 호출되지 않는 문제가 있었다.
- 에이전트 조치: frontmatter 설명을 넓히고 한국어 파일과 전역 설치본을 동기화했다.
- 드러난 문제: 호출 표면이 본문이 아니라 frontmatter라서 설명이 좁으면 스킬이 선택되지 않는다.

## 식별

- 저장소: `structure-first`
- 작업: structure-first 호출 설명
- 대략 날짜: 2026-06-19

## 확인한 사실

- 호출 기준은 본문이 아니라 frontmatter `name + description`으로 확인됐다.
- 최종 문구는 code generation, feature work, bug fixes, refactoring, code review를 앞세우고 purely mechanical/trivial/throwaway만 제외했다.
- 작업 문서는 절대경로 때문에 checker에 걸렸다가 이식 가능한 문구으로 고쳤다.

## 관련 문서

- `skills/structure-first/SKILL.md`
- `SKILL.ko.md`
- 작업 `BRIEF.md`
- 작업 `WORKLOG.md`
- 작업 `DECISIONS.md`
- 런타임 형태 검사er

## 증거

- `MEMORY.md:918-962`
- `rollout_summaries/2026-06-19T07-34-21-Lq1N-structure_first_trigger_description_update.md:20-42`
- `rollout_summaries/2026-06-19T07-34-21-Lq1N-structure_first_trigger_description_update.md:51-61`
- rollout id `019edecd-5d0b-73f1-bd9b-7731026f627f`

## 불확실한 점

- 현재 최근 코딩 작업에서 호출 개선 효과가 계속 유지되는지는 이번 조사에서 새로 측정하지 않았다.
