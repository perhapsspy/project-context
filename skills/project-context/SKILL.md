---
name: project-context
description: Keep coding-agent working context in ordinary project files with reusable reference notes and dated task records.
---

# Project Context

Keep working context in ordinary repository files so later sessions can resume without rebuilding state from scratch.

## Contract

```text
docs/
  reference/**/*.md
  tasks/yyyy/mm-dd/<task-slug>/
    BRIEF.md
    logs/{DECISIONS,WORKLOG}.md
```

- `docs/reference/` holds reusable project-domain context by topic: conventions, constraints, and integration patterns. Write canonical topic detail there, not in task logs. If a task updates reference content, keep the path, rationale, and change trace in the task. Keep paths lowercase kebab-case and use `rg`, not an index.
- `docs/tasks/yyyy/mm-dd/<task-slug>/` is the default task workspace for most real work, split into one rewrite-only overview (`BRIEF.md`) and append-only history (`logs/DECISIONS.md`, `logs/WORKLOG.md`).
- `BRIEF.md` is the rewrite-only canonical task overview for reopen and handoff. Keep goal, scope, current understanding, current state, next step, blockers, and any current validation or boundary notes another session needs. Do not force it to stay tiny when the task genuinely needs more current context.
- Prefer heading-based top-level structure in `BRIEF.md`. Use section headings such as `Goal`, `Scope`, `Current Understanding`, `Current State`, `Next Step`, `Related Docs`, or `Working Boundary`, and avoid turning the whole file into a flat `key: value` bullet list.
- Keep `BRIEF.md` focused on current reopen/handoff context. Do not turn it into append history, long decision rationale, or reusable topic documentation.
- If `BRIEF.md` and logs are not enough for the task, keep extra task-local docs for the missing detail only. Name them for their role, not as generic overflow files, and mention them briefly in `BRIEF.md` when they matter for reopen or handoff.
- Keep saved doc paths portable: use repo-relative paths or stable placeholders like `<repo-root>`, `<task-root>`, and `$CODEX_HOME`, not absolute or user-specific paths.
- Only logs are append-only. Add entries under `**YYYY-MM-DD**` headings in the current user language. Keep the latest `DECISIONS.md` block ADR-lite (usually 4 bullets). Keep the latest `WORKLOG.md` block to meaningful execution evidence another session may need; fold routine checks into `BRIEF.md` `latest validation` unless they changed task state.
- Subagents start without inherited context; pass only a small task brief: goal, constraints, relevant boundary notes if you have them, validation command, artifact path.
- If an older task looks close to the work at hand, do not continue it immediately. Read only its `BRIEF.md` first, then decide whether it is truly the same unfinished line of work.
- Reuse an existing task only when the main question or intended output is still the same. Similar files, similar topic, or the same subsystem are not enough by themselves.
- Treat `declared read scope` and `declared write scope` as quick boundary hints, not as the task's identity. Use them when they exist, but decide reuse from the work itself first: same goal, same unresolved question, same expected output.
- Start a new dated task when the goal changed, the success condition changed, or you had to inspect a materially different cluster of files to understand the work. If you are unsure, prefer a new task and link the older one in `Related Docs`.
- When unsure, prefer a new task. Duplicate tasks are easier to clean up later than a merged task that mixed two different investigations.
- Never store secrets.

## Working Loop

Read-only work stops here: for questions, reviews, and one-shot inspections, stay read-only and do not bootstrap the layout or create a dated task unless the work is meant to leave durable project-context files behind.

If the repo is effectively empty, bootstrap the layout first.
If the repo already has `docs/reference/` and `docs/tasks/...`, use the normal flow below.
Otherwise, choose an explicit adoption approach instead of treating the bootstrap path below as a migration plan.

For that bootstrap case, create `docs/reference/` and one dated task with `BRIEF.md` and `logs/DECISIONS.md` / `logs/WORKLOG.md`.

1. Search `docs/reference/**/*.md` with `rg`; open at most 3 reference files, preferring the narrowest topic files closest to the active task.
2. If an older task looks related, open at most one `docs/tasks/...` task and read `BRIEF.md` first. Do not open logs until the brief still looks like the same unfinished line of work.
3. Reuse that older task only if the main question and expected output still match. Use declared boundary notes as a quick hint when they exist, but start a new dated task when you had to widen the investigation into a different file cluster or a different decision.
4. For most write-bearing tasks, create or update one dated task, rewrite `BRIEF.md` in place as the current overview, append decisions/execution only to the logs, keep extra task-local docs only when the task genuinely needs them, and write reusable topic detail into `docs/reference/` directly when it becomes clear. Skip task creation only for very small, low-judgment, immediately-finished changes.
5. If reference/task search finds no relevant context, proceed with explicit assumptions and record corrections after execution.

## Guardrail Check

- Checks only current runtime shape: required paths/files, latest log-block shape, task/reference path markers, and secret-like markers.
- Does not judge candidate ownership, semantic quality, full history, merge correctness, or broader scope discipline.

Run the bundled checker by resolving the skill-relative script `scripts/check_runtime_shape.py` from the installed `project-context` skill directory and executing it from the active repo root. If running from a subdirectory, pass `--repo-root <path>` when nested `docs` trees could confuse root detection.
