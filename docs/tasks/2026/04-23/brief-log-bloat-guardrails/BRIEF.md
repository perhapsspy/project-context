# Brief Log Bloat Guardrails

## Goal
- `SKILL.md`에 들어간 BRIEF/log 과대화 방지 방향이 현재 수준에서 타당한지 판정하고, 구현 전 follow-up task 범위를 정리한다.

## Scope
- 현재 diff가 shipped skill과 repo-local 문서 역할 경계에 맞는지 본다.
- 새로 추가된 BRIEF/log hard rule 중 wording만으로 둘 항목과 guardrail 후보를 가른다.
- follow-up은 low-noise checker/test 또는 wording 조정 중 필요한 최소 범위로만 잡는다.

## Current Understanding
- 현재 diff는 repo-local 문서를 짧게 정리하고, shipped `SKILL.md`에 BRIEF/log 간결화 기준을 모아 둔 점에서 방향이 맞다.
- `BRIEF.md`의 file inventory, history, transcript 성장을 막겠다는 의도는 기존 `project-context` 문제의식과도 맞는다.
- 다만 `skills/project-context/SKILL.md`의 새 hard rule 다수는 아직 checker나 test로 직접 받쳐지지 않는다.
- follow-up의 핵심은 규칙을 더 늘리는 것이 아니라, 강한 문구와 실제 guardrail/evidence 사이의 간극을 줄이는 것이다.

## Current State
- status는 in_progress다.
- diff review 결과 blocking issue는 없고, 이 방향 자체는 유지해도 된다.
- 현재 check 기준에서는 전체 unittest, runtime shape, gardening이 모두 통과한다.
- 개선 포인트는 새 hard rule을 전부 enforcement로 밀어 넣는 것이 아니라, low-noise로 검출 가능한 항목만 추리고 나머지는 wording 강도를 조정할지 판단하는 데 있다.

## Next Step
- `SKILL.md`의 새 BRIEF/log 제한을 항목별로 나눠 `즉시 유지`, `soften 필요`, `checker/test 후보`로 분류한 뒤 최소 follow-up 변경안을 만든다.
