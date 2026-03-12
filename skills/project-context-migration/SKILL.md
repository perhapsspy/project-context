---
name: project-context-migration
description: Adopt `project-context` in an existing repository by auditing and migrating current documentation, notes, ADRs, runbooks, and task history into `docs/memory.md`, `docs/reference/`, and `docs/tasks/...` dated tasks. Use when a repo already has scattered context that should be consolidated into the `project-context` structure.
---

# Project Context Migration

Adopt `project-context` in a repo that already has legacy docs, or partial target-tree adoption plus legacy docs elsewhere.
If the repo is effectively empty and there is nothing to migrate, use `project-context` instead.

## Workflow

1. Read [../project-context/SKILL.md](../project-context/SKILL.md) to review the target layout.
2. Create one dated migration task under `docs/tasks/...` first and use it as the audit surface for the whole move.
3. Inventory likely source roots with `rg --files` across `docs/`, `notes/`, `adr/`, `runbooks/`, `plans/`, `tasks/`, or `.ai/`.
4. Before mapping, ask whether each source is AI-working context at all. Human-facing top-level notes, origin/about/repository narrative, and user/team docs usually stay `LEAVE`.
5. Build an audit map before editing: `path | kind | current-or-stale | scope | target | note`.
6. Apply in order: `TASK -> REFERENCE -> MEMORY -> LEAVE/ARCHIVE`.
7. Once the target tree exists and `project-context` is installed alongside this skill, the agent can run the bundled checker from `../project-context/scripts/check_runtime_shape.py` while the shell stays in the target repo root, or any subdirectory inside it; the checker infers the target repo from the current working directory.
8. Treat that check as destination-shape confirmation only; migration correctness still depends on the audit map and spot review.

## Classification

- `TASK`: task-local, historical, exploratory, uncertain, or migration-audit material. Start here when unsure.
- `REFERENCE`: reusable topic-scoped reference state. Rewrite to current reference state only, strip timeline noise, and keep durable topic detail that another task would actually reuse.
- `MEMORY`: small project-wide working memory worth loading almost every time: active invariants, current phase, temporary global constraints, currently active cross-task conditions, and other compressed global notes. Keep declarative and compressed.
- `LEAVE`: product/user/team docs, human-facing top-level notes, and origin/about/repository narrative that do not belong in AI memory.
- `ARCHIVE`: stale duplicates or superseded docs if the user wants cleanup; it is a migration decision, not a core `project-context` destination.
- Fast rules: `runbook -> reference`, `task note -> task`, `ADR -> current conclusion to reference / superseded to archive`, `origin/about/repository note -> usually leave`, `notes -> memory only if they compress to global working memory; otherwise reference/task/archive`, `short project-wide repository facts -> memory only when many tasks should reload them soon; otherwise leave or reference`.

## Rules

- Do not bulk-copy legacy docs into `docs/memory.md`.
- Record audit decisions in the migration task before rewriting global files.
- Merge overlapping sources into one preferred destination reference file or one dated task.
- Before promoting anything into `REFERENCE` or `MEMORY`, ask whether another task would reuse it as AI-working context. If not, prefer `LEAVE`.
- Do not create `REFERENCE` files that mostly restate `docs/memory.md`. If the content is mostly compressed project-wide facts with little durable topic detail, keep it in `MEMORY` or `LEAVE`.
- When migration creates new tasks, follow the `project-context` file shapes exactly: `BRIEF.md` is a rewrite-only reopen brief, `STATUS.md` is a rewrite-only current handoff note and should usually start directly with current-state lines rather than a title line, fixed headings are not required, `MEMORY-CANDIDATES.md` is omitted unless migration discovers task-derived global working-memory candidates, and when present it contains only plain `- <STATE> | <summary> | <evidence-pointer>` entries with no title text, while `logs/DECISIONS.md` / `logs/WORKLOG.md` are the append-only history and use `**YYYY-MM-DD**` headings followed only by bullet lines (latest `DECISIONS.md`: 4 bullets; latest `WORKLOG.md`: 1+ bullet).
- If a task item has no trustworthy date, use the migration date and record the uncertainty in that task.
- Create `MEMORY-CANDIDATES.md` entries only for compressed global working-memory notes discovered during migration, not for reference file creation or plain file moves.
- When unsure between `REFERENCE` and `LEAVE` for a human-facing top-level doc, bias toward `LEAVE`.
- If the rollout must be staged, move high-value task/reference material first and compress `memory.md` last.
