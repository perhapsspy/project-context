**2026-03-10**
- 배경: `project-context` 본체는 운영 계약에 집중해야 하고, 기존 repo 문서를 새 구조로 옮기는 adoption 작업은 별도 트리거와 절차가 필요하다.
- 선택지: 1) 기존 `project-context` skill에 migration 절차를 같이 넣는다, 2) 기존 docs 이관만 담당하는 별도 skill을 만든다.
- 결정: adoption 단계 전용 skill `project-context-migration`을 별도로 만들고, 본체 skill은 운영 계약에 집중시킨다.
- 영향: 스킬 표면이 덜 섞이고, 기존 repo 도입 작업에서 필요한 inventory/mapping/apply 절차를 별도로 트리거할 수 있다.

**2026-03-10**
- 배경: migration skill이 곧바로 `docs/memory.md`부터 쓰게 하면 legacy 노이즈를 전역 메모리로 먼저 옮길 위험이 있다.
- 선택지: 1) memory 먼저 작성한다, 2) migration task에 audit manifest를 만들고 `task -> reference -> memory` 순서로 적용한다.
- 결정: migration skill은 audit-first로 진행하고, 분류가 애매한 문서는 먼저 `task`에 두며 현재 truth가 정리된 뒤에만 `reference`와 `memory`를 갱신한다.
- 영향: 초기 이관에서 과승급을 줄이고, legacy 문서의 불확실성을 task 안에서 검토할 수 있다.

**2026-03-10**
- 배경: 새 migration skill은 scripts가 없고, 분류 기준과 적용 순서도 `SKILL.md` 안에 충분히 담을 수 있는 수준이었다.
- 선택지: 1) 현재처럼 optional files를 유지한다, 2) 최소 동작 표면만 남기고 `SKILL.md` 하나로 축소한다.
- 결정: `project-context-migration`은 `SKILL.md` 단독 스킬로 유지하고, 분류와 적용 규칙은 본문에 직접 넣는다.
- 영향: skill surface가 작아지고 구조 복잡성이 줄며, 실제 dogfood에서 필요가 확인될 때만 추가 asset을 다시 검토하면 된다.
