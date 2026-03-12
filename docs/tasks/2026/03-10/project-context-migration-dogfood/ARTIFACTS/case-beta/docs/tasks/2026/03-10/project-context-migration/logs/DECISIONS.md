**2026-03-10**
- 배경: `case-beta`는 ADR, API 문서, 태스크 메모, 불확실한 잡노트가 흩어져 있어 `project-context` canonical 구조가 없었다.
- 선택지: 현재처럼 보이는 문서를 모두 `memory.md`로 올리기, 재사용 가능한 현재 진실만 `reference`로 정리하고 불확실하거나 태스크성 자료는 dated task로 보관하기, 또는 원본을 그대로 두고 색인만 추가하기가 있었다.
- 결정: migration audit task을 먼저 만들고, PocketBase datastore 결론은 `docs/memory.md`와 `docs/reference/data/database-choice.md`에 반영하며, auth 토큰 규칙은 `docs/reference/api/auth.md`로 정리하고, 로그인 조사는 task에 두며 불확실한 메모는 source 위치에 남긴다.
- 영향: canonical AI context는 `docs/` 아래에 생기고, 미확정 자료는 reference나 memory를 오염시키지 않은 채 source artifact로 남는다.
