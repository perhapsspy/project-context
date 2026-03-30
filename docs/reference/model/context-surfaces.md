# context surfaces

`project-context`는 프로젝트 맥락을 `reference`와 `tasks`로 나눈다.

- 이 surface들에 남기는 경로는 repo-relative나 `<repo-root>`, `<task-root>`, `$CODEX_HOME` 같은 project-owned placeholder를 우선한다.

## reference

- `docs/reference/**/*.md`는 task를 넘어 반복 참조될 주제별 도메인 맥락을 담는다.
- 외부 API 사용 규칙, 인증 방식, rate limit, 에러 처리, 프로젝트 내부 convention 같은 reusable topic detail이 여기에 온다.

## tasks

- `docs/tasks/yyyy/mm-dd/<task-slug>/`는 대부분의 실제 작업이 머무는 task surface다.
- task 안에는 현재 개요와 작업 흔적이 남는다.
- task가 더 많은 구조를 필요로 하면 task-local 문서를 추가할 수 있다.
- 세부 파일 shape와 운영 규칙은 durable model이 아니라 shipped skill contract가 소유한다.
