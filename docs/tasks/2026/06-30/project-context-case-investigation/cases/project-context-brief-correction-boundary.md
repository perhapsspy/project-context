# project-context BRIEF 정정/삭제 경계 추가

## 핵심

- 사용자 지적/요청: 사용자 정정/삭제 요청을 해설로 남기지 말고 현재 상태만 남겨야 한다는 문제가 있었다.
- 에이전트 조치: `BRIEF.md`가 결과 사실, boundary, next step만 유지하도록 shipped skill 규칙을 추가했다.
- 드러난 문제: 정정 내용을 설명으로 보존하면 사용자가 지운 내용을 문서가 다시 살린다.

## 식별

- 저장소: `project-context`
- 작업: BRIEF 정정/삭제 경계
- 대략 날짜: 2026-06-24

## 확인한 사실

- 기존 규칙은 rewrite-only와 logs 분리를 갖고 있었지만 사용자 정정/삭제 입력 처리는 직접 말하지 않았다.
- 최종 rule은 `BRIEF.md`가 결과 사실, boundary, next step만 유지하도록 했다.
- 검증에는 런타임 형태, unittest, `git diff --check`, `check_gardening.py`가 포함됐다.

## 관련 문서

- `skills/project-context/SKILL.md`
- 작업 `BRIEF.md`
- 런타임 형태/gardening checker

## 증거

- `MEMORY.md:756-787`
- `rollout_summaries/2026-06-24T01-05-31-NaRA-project_context_brief_correction_boundary_rule.md:20-41`
- rollout id `019ef729-2f37-7253-85f6-45ace936a51a`

## 불확실한 점

- `check_gardening.py`가 보고한 기존 2026-04-09 항목의 세부 내용은 이번 범위에서 열지 않았다.
