**2026-03-19**
- 배경: fresh-context review에서 가장 큰 문제는 새 철학 자체보다 checker 실행 경로, stale `MEMORY-CANDIDATES.md`, 과한 enforcement wording 같은 contract mismatch였다.
- 선택지: 1) checker를 더 두껍게 만들어 문서를 따라가게 한다. 2) thin guardrail 철학은 유지하고, skill/fixture 문구를 현재 runtime contract에 다시 맞춘다.
- 결정: checker를 키우지 않고, 우선 shipped skill과 migration fixture를 현재 runtime contract 수준으로 정렬한다.
- 영향: 실제 사용자가 문서대로 따라 했을 때의 오동작을 줄이면서도 thin guardrail 철학은 유지된다.
**2026-03-19**
- 배경: migration fixture test가 representative 분류 결과를 고정한다는 이유로 task file 경로, brief 내부 문구까지 많이 박아 두면 drift보다 brittleness가 더 커진다.
- 선택지: 1) fixture 전체 output tree와 migration brief wording을 계속 넓게 고정한다. 2) leave/reference/memory/task 경계를 대표하는 고신호 assertion만 남기고 저신호 path/string 고정은 줄인다.
- 결정: migration fixture test는 semantic 분류 경계를 대표하는 assertion만 남기고, task file path나 migration brief wording 같은 부수 고정은 제거한다.
- 영향: 스킬 철학 regression은 계속 잡으면서도 fixture churn과 과도한 test maintenance를 줄일 수 있다.
