# context surfaces

`project-context`는 프로젝트 맥락을 세 가지 durable surface와 한 가지 task surface로 나눈다.

## memory

- `docs/memory.md`는 rewrite-only 전역 작업 메모리다.
- active invariant, 현재 phase, 임시 전역 제약, 현재 유효한 cross-task 조건처럼 많은 task가 당분간 다시 읽을 전역 맥락을 압축해 둔다.
- 상세 주제 설명, task execution chronology, 긴 append history는 두지 않는다.

## reference

- `docs/reference/**/*.md`는 task를 넘어 반복 참조될 주제별 도메인 맥락을 담는다.
- 외부 API 사용 규칙, 인증 방식, rate limit, 에러 처리, 프로젝트 내부 convention 같은 reusable topic detail이 여기에 온다.
- task 자체가 도메인 콘텍스트 정리이거나 반복 참조될 도메인 콘텍스트가 이미 분명하면 직접 작성할 수 있다.

## tasks

- `docs/tasks/yyyy/mm-dd/<task-slug>/`는 대부분의 실제 작업이 머무는 기본 task surface이며, rewrite-only snapshot과 append-only history로 나뉜다.
- 읽기 전용 질문, 리뷰, 단발 inspection은 durable update가 필요할 때만 task를 만들고, 아니면 read-only로 끝낸다.
- `BRIEF.md`는 rewrite-only reopen brief다. 목적, 범위, 현재 이해, 현재 산출물 스냅샷만 남기고 chronology는 두지 않는다.
- `STATUS.md`는 rewrite-only current handoff surface다. 현재 상태, 다음 작업, blocker, declared read/write scope, 최신 validation만 남기고 보통 제목 줄 없이 바로 시작한다.
- `logs/DECISIONS.md`, `logs/WORKLOG.md`만 append-only 기록이다. 작업 경과, 실행 흔적, 판단 근거는 여기에 누적한다.

## memory candidates

- `MEMORY-CANDIDATES.md`는 task에서 나온 `docs/memory.md` 후보를 올릴 때만 쓰는 선택 rewrite-only surface다.
- task-derived `docs/memory.md` 변경은 `MEMORY-CANDIDATES.md`를 거친다.
- `docs/reference/`는 topic detail이 이미 분명하면 direct write가 가능하고, `MEMORY-CANDIDATES.md`에 넣지 않는다.
- unresolved candidate가 없어지면 `MEMORY-CANDIDATES.md`는 지우거나 생략한다.
