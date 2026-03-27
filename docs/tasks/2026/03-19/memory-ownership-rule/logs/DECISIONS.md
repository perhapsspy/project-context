**2026-03-19**
- 배경: `docs/memory.md`가 repo-local instruction surface와 중복되면 current state보다 standing rule 요약본처럼 읽혀 ownership drift가 생긴다.
- 선택지: 1) 이 레포의 `docs/memory.md`만 줄인다. 2) shipped skill과 migration skill에 anti-duplication ownership 규칙을 넣고 관련 surface/tests까지 같이 정렬한다.
- 결정: 재발 방지를 위해 shipped skill 두 개에 ownership 규칙을 추가하고, README·로컬 방향 문서·migration fixture/test·현재 repo `docs/memory.md`를 같은 기준으로 맞춘다.
- 영향: 이후 migration과 follow-up edit에서 `memory`는 current state만 남기고 repo-local instruction surface는 원래 소유자에 남기는 방향으로 수렴한다.
**2026-03-19**
- 배경: ownership rule이 생겨도 migration workflow가 repo-root instruction files를 source inventory에 넣지 않으면 실제 절차에서는 같은 드리프트를 다시 놓칠 수 있다.
- 선택지: 1) `AGENTS.md` 같은 파일명을 workflow에 직접 나열한다. 2) common context directories에 더해 repo-root instruction files를 보라고 적고 예시는 fast rule에만 둔다.
- 결정: workflow step은 repo-agnostic하게 `repo-root instruction files when present`로 넓히고, fast rule에서만 `AGENTS.md`를 예시로 둔다.
- 영향: 특정 파일명에 과적합되지 않으면서도 migration agent가 root instruction surface를 실제 조사 범위에 포함하게 된다.
**2026-03-19**
- 배경: `MEMORY-CANDIDATES` 중복 배제 규칙을 너무 강한 validator처럼 적으면, 현재 레포에 없는 candidate apply 실행 코드를 문서가 암묵적으로 약속하는 모양이 된다.
- 선택지: 1) 현재 문구를 유지해 reject를 강한 동작처럼 말한다. 2) `MEMORY-CANDIDATES`를 보수적 승급 게이트로 정의하고, ownership 판단은 review 단계에 남긴다.
- 결정: `MEMORY-CANDIDATES`는 global memory 승급을 보수적으로 거르는 review surface로 두고, guardrail은 syntax/reachability만 본다는 점을 skill과 reference 문서에 함께 적는다.
- 영향: memory 승급 철학은 유지하면서도, 아직 없는 자동 판정기나 apply 동작을 과하게 약속하지 않게 된다.
**2026-03-19**
- 배경: 승급 게이트 철학으로 바꾼 뒤에도 `PENDING`과 `REJECTED`가 언제 갈리는지 모호하면 review board가 이미 결론 난 후보를 다시 들고 있게 된다.
- 선택지: 1) 상태 의미를 암묵적으로 둔다. 2) `PENDING`은 판단 미완료, `REJECTED`는 memory ownership 부적합 확정으로 짧게 못 박는다.
- 결정: shipped skill과 reference 문서에 두 상태의 의미를 짧게 추가해, board는 unresolved review만 들고 있고 명확한 비승급 후보는 `REJECTED`로 닫히게 한다.
- 영향: `MEMORY-CANDIDATES`가 backlog처럼 불어나지 않고, 다음 세션이 같은 후보를 반복 검토할 가능성이 줄어든다.
