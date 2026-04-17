# context surfaces

`project-context`는 프로젝트 맥락을 몇 개의 루트 surface로 나눈다.

- 이 surface들에 남기는 경로는 repo-relative나 `<repo-root>`, `<task-root>`, `$CODEX_HOME` 같은 project-owned placeholder를 우선한다.
- 세부 파일 shape와 운영 규칙은 durable model이 아니라 shipped skill contract가 소유한다.

## reference

- `docs/reference/**/*.md`는 task 유무와 무관하게 현재 믿고 사용할 기준 맥락을 담는다.
- 원리, 원칙, 운영 규칙, 최근 믿을 수 있는 사실처럼 다른 task가 바로 재사용할 현재 topic detail이 여기에 온다.
- 이 surface는 자주 갱신될 수 있지만, 조사 경과, 진행 이력, 판단 흔적, 미확정 상태 추적을 본문 역할로 삼지 않는다.

## tasks

- `docs/tasks/yyyy/mm-dd/<task-slug>/`는 대부분의 실제 작업이 머무는 task surface다.
- task 안에는 현재 개요와 작업 흔적이 남는다.
- task 내부 문서의 owner 구분은 shipped skill contract를 따른다.

## backlog

- `docs/BACKLOG.md`는 선택적 repo-level surface다.
- 저장소 수준의 future work를 짧게 둘 때 쓴다.
