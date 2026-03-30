**2026-03-10**
- 배경: `case-beta`는 ADR, API 문서, 태스크 메모, 불확실한 잡노트가 흩어져 있어 `project-context` canonical 구조가 없었다.
- 선택지: 현재처럼 보이는 문서를 모두 reference로 올리기, 재사용 가능한 현재 진실만 `reference`로 정리하고 불확실하거나 태스크성 자료는 dated task로 보관하기, repo-local guidance는 원래 surface에 남긴 채 `LEAVE`로 유지하기, 또는 원본을 그대로 두고 색인만 추가하기가 있었다.
- 결정: migration audit task을 먼저 만들고, PocketBase datastore 결론과 auth 토큰 규칙은 각각 canonical reference로 정리하며, `AGENTS.md`는 root에 남겨 ownership을 유지하고, 로그인 조사는 task에 둔다.
- 영향: canonical AI context는 `docs/reference/**`와 `docs/tasks/**` 아래에 정리되고, repo-local instruction surface와 미확정 자료는 원래 소유 경계에 남는다.
