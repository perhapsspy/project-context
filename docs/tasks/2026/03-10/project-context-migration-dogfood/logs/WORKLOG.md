**2026-03-10**
- dogfood task을 만들고 `case-alpha`, `case-beta` fixture repo 루트를 준비했다.
- 각 fixture는 서로 다른 legacy 문서 혼합을 가지도록 설계해 migration skill의 분류 규칙을 검증하게 한다.
- worker 서브에이전트 둘을 병렬 실행하고, 코디네이터는 결과를 guardrail 함수로 재검증할 예정이다.

**2026-03-10**
- worker A는 `case-alpha/**`, worker B는 `case-beta/**`만 소유하도록 캡슐을 분리했다.
- 두 worker 모두 `project-context-migration`과 `project-context` skill만 읽고 in-place migration을 수행하도록 설정했다.

**2026-03-10**
- `case-alpha`는 `REFERENCE/TASK/LEAVE` 분류는 타당했지만, migration skill에 task 형식 설명이 부족해 guardrail에서 `MEMORY-CANDIDATES.md`/`DECISIONS.md` 형식 오류가 났다.
- 그 결과를 반영해 migration skill에 `MEMORY-CANDIDATES.md` plain-entry 규칙과 bullet-only log block 규칙을 추가했다.

**2026-03-10**
- interrupted worker가 남긴 `case-beta` partial output은 제외하고, 수정된 skill 기준 second-pass migration 결과만 남겼다.
- `case-beta`는 `docs/memory.md`, `docs/reference/**`, `docs/tasks/**` 구조와 task 형식까지 포함해 runtime validation을 통과했다.
- 이번 dogfood의 핵심 finding은 “분류 규칙보다 task 형식 규칙 명시가 더 중요했다”는 점이다.

**2026-03-10**
- `case-alpha` first-pass 산출물은 실패 증거로 보존하고, 같은 legacy 입력만 가진 `case-alpha-rerun` fixture를 새로 만들었다.
- 수정된 migration skill을 기준으로 clean rerun worker를 다시 실행했다.

**2026-03-10**
- clean rerun worker는 시간 안에 완결 산출물을 못 냈지만, 코디네이터가 같은 skill 기준으로 `case-alpha-rerun`을 마저 정리했다.
- interrupted worker가 남긴 duplicate reference는 제거했고, `case-alpha-rerun`은 runtime validation을 통과했다.
- 최종 결과는 `case-alpha` first-pass failure, `case-beta` second-pass success, `case-alpha-rerun` clean rerun success로 정리된다.
