---
name: project-context
description: "Resume, handoff, and long-running repo work by keeping durable context across threads or agents: task briefs, logs, and reusable reference notes."
---

# Project Context

## Purpose

Keep durable repo context in ordinary files so later sessions can resume without rebuilding state.

Use this skill for resume, handoff, long-running work, subagent follow-through, reusable reference context, or task logs. Do not bootstrap it for a read-only question or one-shot inspection. If a repo has existing context docs but no project-context layout, choose explicit adoption or use `project-context-migration` before creating a parallel tree.

## Contract

```text
docs/
  reference/**/*.md
  tasks/yyyy/mm-dd/<task-slug>/
    BRIEF.md
    logs/{DECISIONS,WORKLOG}.md
    [optional] <purpose-named-backlog>.md
    [optional] working/
    [optional] archive/
  [optional] BACKLOG.md
```

- `docs/reference/**` owns reusable current rules and reliable facts. Keep investigation history, progress, timelines, code inventories, and provenance narrative out. Point to authoritative code, API, config, test, or project documents instead of restating them. Apply corrections or deletion requests by rewriting or removing stale claims.
- `BRIEF.md` is a rewrite-only resume card: stable goal, scope boundary, current conclusions and state, and the nearest restartable step. It is not a report, history, evidence log, file inventory, or backlog. At a phase boundary, rewrite it to the new resume state and move prior evidence or chronology to logs, `working/`, or `archive/`.
- `logs/WORKLOG.md` records one concise outcome entry per meaningful settled batch, not commands or micro-iterations. `logs/DECISIONS.md` records only decisions that change future interpretation, scope, architecture, rollback, or rule application. Let the bundled log helper own exact block shape.
- A task root contains current-canonical documents and routers. Put drafts, probes, staging evidence, and undecided plans in `working/`; completed, rejected, replaced, or stale material in `archive/`.
- Use a purpose-named task backlog only when one nearest step is insufficient. Keep inactive repo-level work in `docs/BACKLOG.md`.

## Task Identity and Shared Ownership

- Reuse a task only when the unresolved work and expected output still match. Topic similarity or an old boundary note is not task identity; when uncertain, create a new dated task.
- When multiple tasks, owners, or phases depend on an interpretation that changes implementation or acceptance, assign one current canonical owner. Prefer an existing code, API, config, test, or project-document owner. Otherwise use a purpose-named task-root contract for task-specific meaning or `docs/reference/**` for reusable meaning.
- Consumers point to that owner and keep only task-specific state, deviations, and next action. Do not mirror the same open work across brief, backlog, working notes, and logs.

## Operation and Validation

Before acting, reconcile the brief's goal, current state, and restart point. When the current state proves the goal complete, close the selected task and keep adjacent next steps as candidates until the user or an authoritative approved plan selects them.

Read the brief first and only the reference or log context needed to act. Reuse the matching unfinished task or create a dated task with the core files; skip creating a new task only for a small, low-judgment change finished immediately. Add optional surfaces only for a distinct owner or reader action.

Assign one writer for the brief and canonical logs. Other agents write them only under an explicit bounded assignment. Use repo-relative paths or stable placeholders, store no secrets, and pass delegated work only the current goal, constraints, unknowns, evidence command, artifact path, and canonical pointers it needs.

Proceed with reversible stated assumptions when context is missing; ask before changing authority or making a hard-to-reverse commitment.

Use the bundled log helper and runtime-shape checker; their scripts own exact mechanics. The checker covers required shape, latest log blocks, portable paths, and secret-like markers, not ownership, semantic quality, full history, or migration correctness. Treat the gardening checker as warning-grade drift evidence. When a task is maintained, finish only when its brief can reopen the work and current context has one clear owner.
