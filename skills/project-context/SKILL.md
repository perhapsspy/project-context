---
name: project-context
description: Keep durable repo context for session resume, handoff, long-running work, and multi-agent follow-through.
---

# Project Context

## Purpose

Keep working context in ordinary repository files so later sessions can resume without rebuilding state from scratch.

## Use / Do Not Use

- Use this skill when the work should leave durable repo context another session can reopen from.
- Use it when you are resuming or extending a long-running task that needs durable repo context.
- Use it when the work needs reusable reference notes, a current task brief, and an append-only execution trail.
- Do not bootstrap the layout for read-only questions, reviews, or one-shot inspections unless the work is explicitly meant to leave durable project-context files behind.
- Do not treat the bootstrap path here as a migration plan for scattered legacy docs; choose an explicit adoption or migration approach instead.

## Core Bias

- Ordinary repo files over external systems or hidden memory.
- Reusable topic context in `docs/reference/**`; current task reopen state in `BRIEF.md`; append-only trail in `logs/*.md`.
- Small contract over many top-level surfaces.
- Repo-relative or stable placeholder paths over user-specific paths.
- When task reuse is unclear, prefer a new dated task.
- Never store secrets.

## Contract

```text
docs/
  reference/**/*.md
  tasks/yyyy/mm-dd/<task-slug>/
    BRIEF.md
    logs/{DECISIONS,WORKLOG}.md
```

- `docs/reference/` holds reusable project-domain context by topic: conventions, constraints, and integration patterns. Write canonical topic detail there, not in task logs. Keep paths lowercase kebab-case and use `rg`, not an index.
- `docs/tasks/yyyy/mm-dd/<task-slug>/` is the default task workspace for most real work, split into one rewrite-only overview (`BRIEF.md`) and append-only history (`logs/DECISIONS.md`, `logs/WORKLOG.md`).
- `BRIEF.md` is the rewrite-only canonical task overview for reopen and handoff. Keep current goal or intent, scope, current understanding or facts, current state, and next step or next actions. Add validation notes, boundary notes, or doc pointers only when another session would actually need them.
- Prefer heading-based top-level structure in `BRIEF.md`. The default skeleton is usually `Goal` or `Intent`, `Scope`, `Current Understanding` or `Current Facts`, `Current State`, and `Next Step` or `Next Actions`. Headings such as `Related Docs`, `Working Boundary`, and `Latest Validation` stay optional; use them only when they reduce reopen cost. Do not turn the brief into append history, long rationale, or reusable topic docs.
- If `BRIEF.md` and logs are not enough for the task, keep extra task-local docs for the missing detail only. Name them for their role, not as generic overflow files. If they are agent-authored temporary working material such as an implementation checklist, prefer `working/` over the task root, and mention them briefly in `BRIEF.md` when they matter for reopen or handoff.
- If one dated task turns into a long-running working area, keep the root focused on `BRIEF.md` plus canonical current docs. A repo-local helper lane such as `working/` and `archive/` may hold temporary notes, but it stays optional and repo-local.
- Keep saved doc paths portable: use repo-relative paths or stable placeholders like `<repo-root>`, `<task-root>`, and `$CODEX_HOME`, not absolute or user-specific paths.
- Only logs are append-only. Add entries under `**YYYY-MM-DD**` headings in the current user language. Keep each latest `DECISIONS.md` entry as one ADR-lite 4-bullet block and keep the latest `WORKLOG.md` block to meaningful execution evidence another session may need; keep routine checks out of the brief unless they materially change current confidence, state, or next action.
- For any task that updates logs, use the bundled `scripts/task_logs.py` entrypoints as the default write path instead of hand-patching `logs/*.md`.
- Subagents start without inherited context; pass only a small task brief: goal, constraints, relevant boundary notes if you have them, validation command, artifact path.

## Operating Model

If the repo is effectively empty, bootstrap the layout first. If it already has `docs/reference/` and `docs/tasks/...`, use the normal flow below. Otherwise choose an explicit adoption approach instead of treating bootstrap as migration.

For bootstrap, create `docs/reference/` and one dated task with `BRIEF.md` and `logs/DECISIONS.md` / `logs/WORKLOG.md`.

1. Search `docs/reference/**/*.md` with `rg`; open at most 3 reference files, preferring the narrowest topic files closest to the active task.
2. If an older task looks related, open at most one `docs/tasks/...` task and read `BRIEF.md` first. Do not open logs until the brief still looks like the same unfinished line of work.
3. Reuse that older task only if the main question and expected output still match. Use declared boundary notes as a quick hint when they exist, but start a new dated task when you had to widen the investigation into a different file cluster or a different decision.
4. For most write-bearing tasks, create or update one dated task, rewrite `BRIEF.md` in place as the current overview, append decisions and execution to the logs through `scripts/task_logs.py`, keep extra task-local docs only when the task genuinely needs them, and write reusable topic detail into `docs/reference/` directly when it becomes clear. Skip task creation only for very small, low-judgment, immediately-finished changes.
5. If task-local root docs keep multiplying, first decide whether durable topic detail belongs in `docs/reference/**`. If the work is still one long-running task, separate canonical root docs from temporary working notes instead of stacking more mixed-purpose root files.
6. If reference or task search finds no relevant context, proceed with explicit assumptions and record corrections after execution.

For log writes, use `scripts/task_logs.py`. `append` is the normal path even when the previous latest block drifted, because it can add a new valid latest block without hand-patching the file first. In PowerShell, prefer `--bullet=` over `--bullet ""` when you need an intentionally empty value.

## Anti-Patterns

- Bootstrapping project-context files for read-only work that is not meant to leave durable context behind.
- Reusing a task because of topic similarity rather than the same unresolved work and expected output.
- Letting `BRIEF.md` turn into append history, reusable domain docs, or long rationale.
- Creating generic overflow files instead of role-named task-local docs.
- Mixing canonical current docs, temporary working notes, and finished remnants at one task root.
- Saving absolute user-specific paths or secrets in docs.
- Treating declared read and write scope as the task identity instead of quick boundary hints.

## Guardrail Check

- Checks only current runtime shape: required paths/files, latest log-block shape, task/reference path markers, and secret-like markers.
- Does not judge ownership, semantic quality, full history, merge correctness, or broader scope discipline.

Run the bundled checker by resolving the skill-relative script `scripts/check_runtime_shape.py` from the installed `project-context` skill directory and executing it from the active repo root. If running from a subdirectory, pass `--repo-root <path>` when nested `docs` trees could confuse root detection.

## Final Gates

- Can a later session reopen the work from `BRIEF.md` without reconstructing state from scratch?
- Is reusable topic knowledge in `docs/reference/**` instead of buried in task logs?
- Is the latest execution and decision trail confined to `logs/*.md`?
- If the task became long-running, are canonical root docs not confusingly mixed with temporary working notes and finished remnants?
- Did task reuse follow the unresolved work and expected output rather than topic similarity?
- Are paths portable and secrets absent?
