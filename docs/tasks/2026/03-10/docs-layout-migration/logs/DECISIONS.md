**2026-03-10**
- 배경: 공개 전 정리 시점이라 `docs/memory/` 폴더 구조보다 사람이 읽기 쉬운 `docs/` 루트 문서 배치가 더 자연스럽다.
- 선택지: 1) `docs/memory/`를 유지한다. 2) `docs/memory.md`, `docs/reference/`, `docs/tasks/`로 재배치하고 계약과 예시를 모두 새 경로에 맞춘다.
- 결정: `docs/memory/`는 제거하고 정본 메모리는 `docs/memory.md`, supporting trees는 `docs/reference/`, `docs/tasks/`로 재배치한다.
- 영향: skill, guardrail, tests, dogfood/example 문서가 같은 경로 계약을 공유하고 사람/AI 모두 `docs/` 루트에서 바로 참조할 수 있다.
