**2026-03-10**
- 배경: repo에는 root `AGENTS.md`가 없고, skill 본체와 repo-local guardrail/tests/docs의 경계도 구두 논의에만 남아 있어 이후 contributor나 agent가 구조를 오해할 여지가 있었다.
- 선택지: 1) 구조를 암묵적으로 둔다, 2) `AGENTS.md`만 추가한다, 3) `AGENTS.md`와 짧은 방향성 문서를 함께 추가한다.
- 결정: root `AGENTS.md`로 작업 규칙을 두고, `docs/skill-direction.md`에 skill surface, repo surface, guardrail 방향을 bullet list로 정리한다.
- 영향: 이후 agent가 repo를 열었을 때 skill 본체와 repo-local 자산을 더 빨리 구분할 수 있고, guardrail/tests 위치에 대한 판단 기준도 명확해진다.

**2026-03-10**
- 배경: `docs/skill-direction.md`에 현재 `docs/` 경로 구조까지 적혀 있어 리네이밍이나 리폴더링이 생기면 방향 문서가 곧바로 stale해질 수 있었다.
- 선택지: 1) 구조와 방향을 같이 둔다, 2) 방향 문서는 원칙만 남기고 구조 설명은 다른 문서에 둔다.
- 결정: `docs/skill-direction.md`는 skill 방향, 경계, guardrail 철학, 진화 원칙만 남기고 구조 의존 설명은 제거한다.
- 영향: 방향 문서는 파일 배치 변경에도 오래 유지되고, 구조 정리는 `AGENTS.md`나 개별 계약 문서에서만 관리하면 된다.

**2026-03-10**
- 배경: root `AGENTS.md`가 skill contract와 repo-local 작업 규칙을 함께 담고 있어, 이 repo가 스킬을 만드는 공간이라는 점보다 스킬 자체 동작을 설명하는 문서처럼 읽혔다.
- 선택지: 1) 기존 세부 규칙을 유지한다, 2) `AGENTS.md`를 repo authoring context로 축소하고 skill behavior는 shipped skill/documentation으로만 남긴다.
- 결정: `AGENTS.md`는 repo purpose, layout, working rules, memory, validation만 남기고 skill-facing behavior 설명은 제거한다.
- 영향: root 안내 문서는 리포 작업 진입점으로 더 명확해지고, 스킬 동작의 단일 출처도 흐려지지 않는다.

**2026-03-10**
- 배경: `docs/memory.md`의 rewrite-only 같은 규칙은 repo authoring context가 아니라 skill이 감당하는 memory behavior에 더 가깝다.
- 선택지: 1) 해당 규칙을 `AGENTS.md`에 둔다, 2) root 문서에서는 제거하고 repo-level 작업 규칙만 남긴다.
- 결정: `AGENTS.md`에서는 memory behavior 규칙을 제거한다.
- 영향: root 안내 문서가 더 좁고 안정적인 repo 맥락에 집중하게 된다.

**2026-03-10**
- 배경: root `AGENTS.md`에 `skill-creator` 사용 지시, 테스트 배치 세부 규칙 같은 문장이 남아 있으면 repo context보다 agent workflow 문서에 가깝게 읽힌다.
- 선택지: 1) repo-local이라고 볼 수 있는 작업 규칙까지 넓게 둔다, 2) repo를 여는 데 필요한 최소 경계와 검증 정보만 남긴다.
- 결정: root `AGENTS.md`는 purpose, boundary, layout, validation, task 기록 정도로 축소한다.
- 영향: 문서 역할이 더 선명해지고, 스킬 제작 방법론이나 운영 규칙과도 덜 섞인다.
