# Project Context Migration Skill

- owner: ai
- started_at: 2026-03-10
- status: done

## 목적
- 기존 repo 문서를 `project-context` 구조로 이관하는 별도 adoption/migration skill을 만든다.

## 실행 범위
- 새 skill `project-context-migration`을 scaffold하고 실제 trigger 문구를 채운다.
- 분류 규칙과 적용 순서를 `SKILL.md` 하나로 압축한다.
- repo guardrail와 이후 dogfood가 이어질 수 있는 최소 동작 표면으로 마감한다.

## 성공 기준
- 기존 repo 문서 이관 작업에서 독립적으로 트리거될 수 있는 frontmatter를 가진다.
- skill 본문이 `inventory -> mapping -> apply -> validate` 흐름을 제공한다.
- 분류 규칙이 `MEMORY/REFERENCE/TASK/LEAVE/ARCHIVE` 구분과 실제 적용 순서를 설명한다.
