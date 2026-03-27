# context surfaces

`project-context`는 프로젝트 맥락을 두 가지 repo-wide durable surface와 하나의 task workspace로 나눈다.

## memory

- `docs/memory.md`는 rewrite-only 전역 작업 메모리다.
- active invariant, 현재 phase, 임시 전역 제약, 현재 유효한 cross-task 조건처럼 많은 task가 당분간 다시 읽을 전역 맥락을 압축해 둔다.
- 상세 주제 설명, task execution chronology, 긴 append history는 두지 않는다.
- 다른 canonical surface가 이미 소유한 standing rule은 여기서 다시 적지 않는다.

## reference

- `docs/reference/**/*.md`는 task를 넘어 반복 참조될 주제별 도메인 맥락을 담는다.
- 외부 API 사용 규칙, 인증 방식, rate limit, 에러 처리, 프로젝트 내부 convention 같은 reusable topic detail이 여기에 온다.
- task 자체가 도메인 콘텍스트 정리이거나 반복 참조될 도메인 콘텍스트가 이미 분명하면 직접 작성할 수 있다.

## tasks

- `docs/tasks/yyyy/mm-dd/<task-slug>/`는 대부분의 실제 작업이 머무는 기본 task surface이며, rewrite-only snapshot과 append-only history로 나뉜다.
- task 안의 rewrite-only snapshot(`BRIEF.md`, `STATUS.md`)은 현재 reopen/handoff 상태를 담고, append-only log(`logs/DECISIONS.md`, `logs/WORKLOG.md`)는 판단과 실행 흔적을 누적한다.
- task가 더 많은 구조를 필요로 하면 필요한 역할에 한해 추가 task-local 문서를 둘 수 있지만, 이는 새 필수 surface가 아니다.
- 세부 파일 shape와 운영 규칙은 durable model이 아니라 shipped skill contract가 소유한다.

## memory candidates

- `MEMORY-CANDIDATES.md`는 task에서 나온 `docs/memory.md` 후보를 올릴 때만 쓰는 선택 rewrite-only surface다.
- `MEMORY-CANDIDATES.md`는 전역 메모리 승급을 보수적으로 거르는 review surface이지, 의미를 기계적으로 판정하는 validator는 아니다.
- task-derived `docs/memory.md` 변경에서만 잠깐 쓰이고, unresolved review가 끝나면 사라질 수 있는 task-local surface다.
- 세부 상태값, entry shape, lifecycle 규칙은 shipped skill contract가 소유한다.
