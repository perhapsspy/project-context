**2026-03-30**
- 배경: compact 철학은 이미 있었지만 task surface 오동작을 줄이는 직접 문장이 repo-local authoring guidance에 약했고, 그 보강과 shipped skill 반영이 같은 날 연속 작업으로 나뉘어 기록됐다.
- 선택지: 1) 로컬 guidance 보강과 shipped skill 반영을 별도 task 둘로 남긴다. 2) 같은 drift를 다룬 한 흐름으로 합치고, repo-local guidance 보강은 그 첫 단계로만 남긴다.
- 결정: `AGENTS.md` 보강과 shipped/local skill wording 조정을 하나의 task 기록으로 합치고, separate compactness task는 제거한다.
- 영향: 같은 의도와 수정이 task 둘로 갈라져 reopen 비용을 늘리지 않고, compact 철학 변화와 skill 계약 변화의 인과관계를 한곳에서 읽을 수 있다.
**2026-03-30**
- 배경: task surface 오동작은 새 구조 부족보다 `BRIEF`/`STATUS`/`WORKLOG`가 각각 무엇을 안 담아야 하는지와 routine check를 어디로 접어야 하는지가 shipped contract에서 약하게 읽히는 데서 반복됐다.
- 선택지: 1) 설명을 늘려 예시를 많이 싣는다. 2) compact 철학을 유지하면서 제외 대상을 짧게 못 박고, routine check는 `latest validation`으로 접는 규칙만 직접 적는다.
- 결정: shipped `project-context`에 surface별 제외 대상과 `WORKLOG` compactness를 짧게 추가하고, migration/local direction/reference surface는 같은 방향으로만 최소 정렬한다.
- 영향: `WORKLOG`의 command-by-command 나열과 `BRIEF`/`STATUS` 역할 중복을 줄이되 skill surface는 계속 작게 유지할 수 있다.
