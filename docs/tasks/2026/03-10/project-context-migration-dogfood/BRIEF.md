# Project Context Migration Dogfood

## Goal
- `project-context-migration` 스킬을 synthetic legacy repo 2개에 적용해 분류 규칙, 실행 순서, 산출물 품질을 검증한다.

## Scope
- `ARTIFACTS/case-alpha`, `ARTIFACTS/case-beta`에 legacy fixture repo를 만든다.
- worker 서브에이전트를 `fork_context=false`로 실행해 각 fixture를 독립적으로 마이그레이션하게 한다.
- 코디네이터는 각 결과를 `project-context` guardrail 함수로 점검하고, 형식 drift가 있으면 skill 규칙을 보강한 뒤 clean rerun 결과까지 정리한다.

## Current State
- status는 completed다.
- 이 task는 초기 migration dogfood와 artifact snapshot을 남긴 기록이다.
- `ARTIFACTS/` 아래 결과는 당시 비교 근거라 그대로 보존하고, live contract 변화는 이후 task에서 정리했다.
- latest validation: case-alpha clean rerun 통과, 결과 정리 완료

## Next Step
- 없음

## Working Boundary
- declared read scope: `skills/project-context-migration/**`, `docs/tasks/2026/03-10/project-context-migration-dogfood/ARTIFACTS/**`
- declared write scope: `docs/tasks/2026/03-10/project-context-migration-dogfood/**`
