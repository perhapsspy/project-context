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
- Current trusted topic context in `docs/reference/**`; current task resume state in `BRIEF.md`; append-only trail in `logs/*.md`.
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
    [optional] <purpose-named-backlog>.md
    [optional] working/
    [optional] archive/
  [optional] BACKLOG.md
```

- `docs/reference/**`: current trusted reference context only. Keep principles, rules, and recent reliable facts here. It may change often, but do not turn it into investigation history, progress tracking, or timeline narrative.
- `docs/tasks/yyyy/mm-dd/<task-slug>/`: default task workspace for most real work.
- `BRIEF.md`: rewrite-only current state for resume and handoff. Keep goal or intent, scope, current understanding or facts, current state, and the nearest next step. Do not turn it into append history, long rationale, or reusable topic docs.
- `logs/DECISIONS.md` and `logs/WORKLOG.md`: append-only decision and execution trail. Keep evidence here, not in the brief.
- `[optional] <purpose-named-backlog>.md`: unresolved carry-over only, such as `RESEARCH-BACKLOG.md` or `QA-BACKLOG.md`. Add it only when one next step is no longer enough.
- `[optional] working/` and `[optional] archive/`: helper lanes for temporary or finished working notes.
- `[optional] docs/BACKLOG.md`: not-yet-active repo-level future work only. Once a dated task becomes active, move the active state into that task and remove the repo backlog item.
- Keep saved doc paths portable: use repo-relative paths or stable placeholders like `<repo-root>`, `<task-root>`, and `$CODEX_HOME`, not absolute or user-specific paths.
- In `BRIEF.md`, use heading-based top-level structure. The default skeleton is usually `Goal` or `Intent`, `Scope`, `Current Understanding` or `Current Facts`, `Current State`, and `Next Step` or `Next Actions`; keep extra detail in logs or task-local docs instead of thickening the brief.
- In `BRIEF.md`, keep `Scope` as a short boundary summary, usually 1 to 3 bullets. Do not turn it into a touched-file inventory or long path list.
- If exact read/write paths materially lower reopen cost, keep them in an optional `Working Boundary` section instead of expanding `Scope`.
- In `BRIEF.md`, `Next Step` or `Next Actions` own only the nearest restartable move, not a carry-over backlog.
- In logs, follow the existing task language; if no task language exists yet, use the current user language.
- Add log entries under dated sections using the existing `**YYYY-MM-DD**` format.
- Keep each appended `DECISIONS.md` block as one 4-bullet block: `Background`, `Decision`, `Why`, `Impact`.
- Keep each appended `WORKLOG.md` block short and restartable, such as `Did`, `Evidence`, `Result`, `Next`.
- For any task that updates logs, resolve the skill-relative `scripts/task_logs.py` path from the installed `project-context` skill directory, the same way as the bundled checker, and use its `append` entrypoints as the default write path instead of hand-patching `logs/*.md`, even when the previous latest block drifted.
- If the helper script is unavailable, append the same block shape manually and preserve append-only history.
- Parent agent owns `BRIEF.md` and canonical log updates. Subagents should write only temporary notes or artifacts unless explicitly assigned canonical writeback.
- Subagents start without inherited context; pass only a small task brief: goal, constraints, relevant boundary notes if you have them, validation command, artifact path.

## Operating Model

- If durable context is warranted for this task and the repo is effectively empty, bootstrap first by creating `docs/reference/` and one dated task with `BRIEF.md` and `logs/DECISIONS.md` / `logs/WORKLOG.md`.
- If the repo does not yet have a usable project-context layout, choose explicit adoption instead of treating bootstrap as migration; seed references plus one active task first rather than bulk-moving scattered docs.

1. Read reusable context.
- Use `rg` to search within `docs/reference/**/*.md` for the active topic.
- Start with up to 3 narrow reference files closest to the active task.

2. Check one related task.
- Start with one related older `docs/tasks/...` task.
- Read `BRIEF.md` first.
- Open logs only if the brief still looks like the same unfinished line of work.

3. Decide reuse or new task.
- Reuse only when the unresolved work and expected output still match.
- Use declared boundary notes as hints, not as the task identity.
- Otherwise start a new dated task.

4. Ensure the task shell.
- For most write-bearing tasks, create or update one dated task.
- Skip task creation only for very small, low-judgment, immediately-finished changes.

5. Write canonical surfaces.
- Rewrite `BRIEF.md` in place.
- Append decisions to `logs/DECISIONS.md` and execution to `logs/WORKLOG.md`.
- Write reusable current rules or facts into `docs/reference/**` when they become clear, but keep investigation history and progress trail in task files.

6. Add optional surfaces only when needed.
- Add task-local backlog only when one next step is not enough.
- Keep repo backlog only for not-yet-active work.
- Once a dated task becomes active, move the active state into that task and remove the repo backlog item.

7. If context is missing, proceed with explicit assumptions.
- Record corrections after execution.

## Anti-Patterns

- Bootstrapping project-context files for read-only work that is not meant to leave durable context behind.
- Reusing a task because of topic similarity rather than the same unresolved work and expected output.
- Letting `BRIEF.md` turn into append history, reusable domain docs, or long rationale.
- Letting `Scope` turn into a per-file inventory instead of a short boundary summary.
- Turning `docs/reference/**` into investigation notes, progress status, or timeline narrative.
- Letting `Next Step` or `Next Actions` turn into a many-item backlog.
- Creating generic overflow files instead of purpose-named task-local docs.
- Mirroring the same open work across `BRIEF.md`, a backlog doc, `working/`, and logs.
- Keeping completed items or task-internal checklist detail in a repo backlog such as `docs/BACKLOG.md`.
- Mixing canonical current docs, temporary working notes, and finished remnants at one task root.
- Dumping raw command transcripts, repetitive micro-steps, or noisy shell output into `WORKLOG.md`.
- Saving absolute user-specific paths or secrets in docs.
- Treating declared read and write scope as the task identity instead of quick boundary hints.

## Guardrail Check

- Checks only current runtime shape: required paths/files, latest log-block shape, task/reference path markers, and secret-like markers.
- Does not judge ownership, semantic quality, full history, merge correctness, or broader scope discipline.

Run the bundled checker by resolving the skill-relative script `scripts/check_runtime_shape.py` from the installed `project-context` skill directory and executing it from the active repo root. If running from a subdirectory, pass `--repo-root <path>` when nested `docs` trees could confuse root detection.

## Final Gates

- Can a later session reopen the work from `BRIEF.md` without reconstructing state from scratch?
- Is current trusted reference context in `docs/reference/**` instead of buried in task logs?
- Is the latest execution and decision trail confined to `logs/*.md`?
- If the task became long-running, are canonical root docs not confusingly mixed with temporary working notes and finished remnants?
- Did task reuse follow the unresolved work and expected output rather than topic similarity?
- Are paths portable and secrets absent?
