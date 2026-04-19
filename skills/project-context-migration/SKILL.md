---
name: project-context-migration
description: Audit scattered repository docs and notes, then move only the right working context into the `project-context` structure.
---

# Project Context Migration

## Purpose

Audit scattered repository docs and notes before moving the right working context into `project-context`. This companion skill assumes the main `project-context` skill is installed alongside it. If the repo is effectively empty and there is nothing to migrate, use `project-context` instead.

## Use / Do Not Use

- Use this skill when a repo already has scattered docs or partial working-context material that needs to be sorted into the `project-context` layout.
- Use it when you need to classify source docs into `TASK`, `REFERENCE`, `LEAVE`, or `ARCHIVE`.
- Do not use it for empty or nearly empty repos with nothing meaningful to migrate.
- Do not treat migration as a blind move-everything operation.

## Core Bias

- Audit first, move second.
- Shipped authority stays shipped.
- Keep only agent working context inside `project-context`.
- When unsure, start in `TASK` rather than over-promoting into `REFERENCE`.
- Migration correctness depends on explicit mapping and spot review, not on destination shape alone.

## Classification

- `TASK`: task-local, historical, exploratory, uncertain, or migration-audit material. Start here when unsure.
- `REFERENCE`: current trusted project-domain context by topic. Rewrite to current state, strip timeline noise, and keep only principles, rules, and recently reliable facts another task can directly use.
- `LEAVE`: product/user/team docs, human-facing top-level notes, and origin/about/repository narrative that do not belong in agent working context.
- `ARCHIVE`: stale duplicates or superseded docs if the user wants cleanup; it is a migration decision, not a core `project-context` destination.
- Common mappings: `runbook -> reference`; `task note -> task`; `ADR -> current conclusion to reference / superseded to archive`; repo-root instruction notes and `origin/about/repository` docs usually stay `LEAVE` unless they clearly remain repo-local agent guidance.

## Operating Model

1. Read [../project-context/SKILL.md](../project-context/SKILL.md) to review the target layout.
2. Create one dated migration task under `docs/tasks/...` first and use it as the audit surface for the whole move.
3. Inventory likely source roots with `rg --files` across common context directories and repo-root instruction files when present.
4. Before mapping, ask whether each source belongs in agent working context at all.
5. Build an audit map before editing: `path | kind | current-or-stale | scope | target | note`. Add extra columns only if they materially lower confusion for this repo.
6. Apply in order: `TASK -> REFERENCE -> LEAVE/ARCHIVE`.
7. Once the target tree exists, run the main `project-context` runtime-shape check.
8. Treat that check as destination-shape confirmation only; migration correctness still depends on the audit map and spot review.

## Rules

- Record audit decisions in the migration task before rewriting global files.
- Follow the main `project-context` skill and bundled scripts by reference instead of summarizing them in repo-local migration docs.
- Merge overlapping sources into one preferred destination reference file or one dated task.
- When migration creates or updates `REFERENCE`, keep canonical content in the reference file and record mapping, rationale, and change trace in the migration task.
- Normalize saved doc paths to repo-relative paths or stable placeholders.
- Before promoting anything into `REFERENCE`, ask whether another task would reuse it as agent working context. If not, prefer `TASK`, `LEAVE`, or `ARCHIVE`.
- Keep source inventories, comparison detail, and rewrite rationale in the audit map or task-local docs rather than thickening the migration brief.
- If a task item has no trustworthy date, use the migration date and record the uncertainty in that task.
- When unsure between `REFERENCE` and `LEAVE` for a human-facing top-level doc, bias toward `LEAVE` unless the current move clearly makes it canonical agent working context.
- When cleanup is about duplication, remove duplicated repo-local summaries before touching task outputs.

## Anti-Patterns

- Rewriting repo-local docs into a second copy of the shipped skill contract or bundled script behavior.
- Moving docs into `REFERENCE` just because they are technical, even when they are not reusable working context.
- Using the runtime-shape check as proof that the migration itself is correct.
- Rewriting or deleting global docs before the migration task has an explicit audit map.
- Promoting uncertain or stale material into `REFERENCE` instead of starting in `TASK`.
- Treating `LEAVE` as failure; many docs should remain outside the agent working-context surface.

## Final Gates

- Does the migration task explain why each moved source became `TASK`, `REFERENCE`, `LEAVE`, or `ARCHIVE`?
- Is current trusted reference context rewritten into current-state reference docs instead of copied over with stale timeline noise?
- Are uncertain, exploratory, or historical materials kept in tasks instead of over-promoted?
- Did the destination tree pass the main `project-context` runtime-shape check?
- Did the rollout preserve human-facing docs that do not belong in agent working context?
