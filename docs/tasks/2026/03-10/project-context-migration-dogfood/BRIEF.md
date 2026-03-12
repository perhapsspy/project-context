# Project Context Migration Dogfood

- owner: ai
- started_at: 2026-03-10
- status: done

## 목적
- `project-context-migration` 스킬을 synthetic legacy repo 2개에 적용해 분류 규칙, 실행 순서, 산출물 품질을 검증한다.

## 실행 범위
- `ARTIFACTS/case-alpha`, `ARTIFACTS/case-beta`에 legacy fixture repo를 만든다.
- worker 서브에이전트를 `fork_context=false`로 실행해 각 fixture를 독립적으로 마이그레이션하게 한다.
- 코디네이터는 각 결과를 `project-context` guardrail 함수로 점검하고, 형식 drift가 있으면 skill 규칙을 보강한 뒤 clean rerun 결과까지 정리한다.

## 성공 기준
- 수정된 skill 기준으로 clean rerun fixture가 `docs/memory.md`, `docs/reference/**`, `docs/tasks/**` 구조와 task 형식을 모두 만족한다.
- 결과가 `check_runtime_shape` runtime validation을 통과한다.
- 애매한 문서가 바로 `memory/reference`로 과승급되지 않고 `task` 또는 source 위치에 안전하게 남는지 확인한다.
