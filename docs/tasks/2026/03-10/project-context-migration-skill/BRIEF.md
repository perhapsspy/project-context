# Project Context Migration Skill

## Goal
- 기존 repo 문서를 `project-context` 구조로 이관하는 별도 adoption/migration skill을 만든다.

## Scope
- 새 skill `project-context-migration`을 scaffold하고 실제 trigger 문구를 채운다.
- 분류 규칙과 적용 순서를 `SKILL.md` 하나로 압축한다.
- repo guardrail와 이후 dogfood가 이어질 수 있는 최소 동작 표면으로 마감한다.

## Current State
- status는 completed다.
- migration skill의 기본 흐름과 분류 규칙을 만들었다.
- 이후 `task-surface-reduction`에서 destination surface가 더 줄어들어, 현재 contract는 `REFERENCE`, `TASK`, `LEAVE/ARCHIVE` 중심으로 읽어야 한다.
- latest validation: repo guardrail 통과, 이후 dogfood 검증 완료

## Next Step
- 없음

## Working Boundary
- declared read scope: `skills/project-context/**`, 기존 migration 요구사항과 dogfood 결과
- declared write scope: `skills/project-context-migration/**`, 관련 repo-local truth
