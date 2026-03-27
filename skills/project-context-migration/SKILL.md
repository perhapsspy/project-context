---
name: project-context-migration
description: Audit scattered repository docs and notes, then move only the right working context into the `project-context` structure.
---

# Project Context Migration

Audit scattered repository docs and notes before moving the right working context into `project-context`.
This companion skill assumes the main `project-context` skill is installed alongside it. If the repo is effectively empty and there is nothing to migrate, use `project-context` instead.

## Workflow

1. Read [../project-context/SKILL.md](../project-context/SKILL.md) to review the target layout.
2. Create one dated migration task under `docs/tasks/...` first and use it as the audit surface for the whole move.
3. Inventory likely source roots with `rg --files` across common context directories and repo-root instruction files when present.
4. Before mapping, ask whether each source belongs in agent working context at all. Human-facing top-level notes, origin/about/repository narrative, and user/team docs usually stay `LEAVE`.
5. Build an audit map before editing: `path | kind | current-or-stale | scope | target | note`.
6. Apply in order: `TASK -> REFERENCE -> MEMORY -> LEAVE/ARCHIVE`.
7. Once the target tree exists, run the main `project-context` runtime-shape check.
8. Treat that check as destination-shape confirmation only; migration correctness still depends on the audit map and spot review.

## Classification

- `TASK`: task-local, historical, exploratory, uncertain, or migration-audit material. Start here when unsure.
- `REFERENCE`: reusable project-domain context by topic. Rewrite to current state, strip timeline noise, and keep only durable topic detail another task would reuse.
- `MEMORY`: small project-wide working memory for compressed current global state. Keep it declarative and compressed; do not use it as a second copy of instructions or topic detail already owned elsewhere.
- `LEAVE`: product/user/team docs, human-facing top-level notes, and origin/about/repository narrative that do not belong in AI memory.
- `ARCHIVE`: stale duplicates or superseded docs if the user wants cleanup; it is a migration decision, not a core `project-context` destination.
- Common mappings: `runbook -> reference`; `task note -> task`; `ADR -> current conclusion to reference / superseded to archive`.
- Repo-root instruction notes usually stay where they already live, and `origin/about/repository` notes usually stay `LEAVE`.
- Use `MEMORY` only for compressed current global state many tasks should reload soon. Otherwise prefer `REFERENCE`, `TASK`, `LEAVE`, or `ARCHIVE`.

## Rules

- Do not bulk-copy legacy docs into `docs/memory.md`.
- Record audit decisions in the migration task before rewriting global files.
- Merge overlapping sources into one preferred destination reference file or one dated task.
- When migration creates or updates `REFERENCE`, keep canonical content in the reference file and record mapping, rationale, and change trace in the migration task.
- Before promoting anything into `REFERENCE` or `MEMORY`, ask whether another task would reuse it as agent working context. If not, prefer `LEAVE`. For `MEMORY`, also require current global state and no other canonical surface already owning it.
- When migration creates new tasks, follow the current `project-context` task-file shape guidance. If `BRIEF.md` and `STATUS.md` are not enough, keep extra task-local docs for the missing detail instead of forcing it into the brief or handoff note. Only add migration-specific uncertainty or task-derived memory candidates when they actually exist.
- If a task item has no trustworthy date, use the migration date and record the uncertainty in that task.
- Create `MEMORY-CANDIDATES.md` entries only for compressed global working-memory notes discovered during migration, not for reference file creation or plain file moves.
- When unsure between `REFERENCE` and `LEAVE` for a human-facing top-level doc, bias toward `LEAVE`.
- If the rollout must be staged, move high-value task/reference material first and compress `memory.md` last.
