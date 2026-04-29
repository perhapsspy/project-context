---
name: project-context
description: Keep durable coding-agent repo context across sessions, handoff, long-running implementation, multi-agent follow-through, and reusable reference notes.
---

# Project Context

## Purpose

Keep durable repo context in ordinary files so later sessions can resume without rebuilding state.

## Use / Do Not Use

Use this skill when work should leave durable repo context: resume, handoff, long-running work, reusable reference notes, a current task brief, and an append-only trail.

Do not bootstrap for read-only questions, one-shot inspections, or implicit migration of scattered legacy docs. If the layout is missing, choose explicit adoption or migration.

## Core Bias

- Ordinary repo files over external systems or hidden memory.
- Current trusted topic context: `docs/reference/**`.
- Current task resume state: `BRIEF.md`.
- Append-only trail: `logs/*.md`.
- Small contract, portable paths, no secrets.
- When reuse is unclear, create a new dated task.

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

- `docs/reference/**`: current trusted reference context only. Keep principles, rules, and reliable facts here. Do not store investigation history, progress, or timeline narrative.
- `docs/tasks/yyyy/mm-dd/<task-slug>/`: default task workspace for real work.
- `BRIEF.md`: rewrite-only compact resume card, not a report or log. Keep goal, scope, current understanding/facts, current state, and nearest next step.
- `logs/DECISIONS.md` and `logs/WORKLOG.md`: append-only decision and execution trail. Keep evidence here, not in the brief.
- `[optional] <purpose-named-backlog>.md`: unresolved carry-over only, such as `RESEARCH-BACKLOG.md` or `QA-BACKLOG.md`. Add it only when one next step is not enough.
- `[optional] working/` and `[optional] archive/`: temporary notes and finished remnants.
- `[optional] docs/BACKLOG.md`: not-yet-active repo-level future work only. Once active, move state into a dated task and remove the repo backlog item.

## `BRIEF.md` Limits

Use only these top-level headings unless the user explicitly asks otherwise:

- `Goal` or `Intent`
- `Scope`
- `Current Understanding` or `Current Facts`
- `Current State`
- `Next Step` or `Next Actions`
- optional `Working Boundary`

Hard rules:

- Usually 300-500 words maximum.
- Each section should usually have 1-5 bullets.
- `Scope` is a 1-3 bullet boundary summary, not a touched-file list.
- `Next Step` owns only the nearest restartable move, not a backlog.
- Do not add sections such as `Validation`, `Files Changed`, `Touched Files`, `History`, `Worklog`, `Investigation`, `Evidence`, `Completed`, or `Checklist`.
- Do not include command output, validation transcripts, investigation history, completed-work history, or touched-file inventories.
- If validation status matters, summarize it in one `Current State` sentence and keep details in `logs/WORKLOG.md`.
- If exact paths materially lower reopen cost, put at most 5 repo-relative paths in `Working Boundary`.

## Log Limits

Logs are append-only, but not command transcripts.

For `logs/WORKLOG.md`:

- Append one block per meaningful work batch, not per command or file.
- Merge repetitive edits, retries, validation attempts, and feedback micro-iterations into one short outcome block after the cluster settles.
- Do not paste raw shell output unless the exact text is essential evidence.
- Keep evidence concise: command names, repo-relative paths, summarized results, or small nested evidence bullets when that is easier to scan.
- Record failed attempts only when they affect the next restartable step.
- Separate task validation from pre-existing repo debt or unrelated warnings.
- Prefer fewer, denser blocks over many micro-blocks.
- Use the existing task language and voice. Write natural bullets that include outcome, compact evidence, and remaining restart conditions only when they matter.

For `logs/DECISIONS.md`:

- Record only decisions affecting future interpretation, scope, architecture, rollback, or rule application.
- Do not log routine edits, validation passes, file creation, or obvious implementation steps.
- Keep each block as 4 bullets: `Background`, `Decision`, `Why`, `Impact`.
- When work is paused, rejected, or converted into reference-only status, record the final decision and reopen condition in `DECISIONS.md` or the compact current state in `BRIEF.md`.

For both logs:

- Add entries under dated sections using `**YYYY-MM-DD**`.
- Keep language consistent with the existing task; otherwise use the current user language.
- For log writes, resolve the skill-relative `scripts/task_logs.py` path and use its `append` entrypoints by default. If unavailable, append manually with the same block shape.

## Path and Ownership Rules

- Use repo-relative paths or placeholders like `<repo-root>`, `<task-root>`, and `$CODEX_HOME`; never user-specific absolute paths.
- Never store secrets.
- Parent agent owns `BRIEF.md` and canonical logs.
- Subagents write only temporary notes or artifacts unless explicitly assigned canonical writeback.
- Subagents start without inherited context; pass a small brief: goal, constraints, boundary notes, validation command, artifact path.

## Operating Model

1. Read reusable context.

   - Use `rg` in `docs/reference/**/*.md` for the active topic.
   - Start with up to 3 narrow reference files closest to the task.

2. Check one related task.

   - Read `BRIEF.md` first.
   - Open logs only if the brief still matches the same unfinished work.

3. Decide reuse or new task.

   - Reuse only when unresolved work and expected output still match.
   - Use boundary notes as hints, not task identity.
   - Otherwise start a new dated task.

4. Ensure the task shell.

   - If durable context is warranted and the repo is effectively empty, create `docs/reference/` and one dated task with `BRIEF.md` and logs.
   - For most write-bearing tasks, create or update one dated task.
   - Skip task creation only for very small, low-judgment, immediately finished changes.

5. Write canonical surfaces.

   - Rewrite `BRIEF.md` in place.
   - Append decisions and worklog entries.
   - Move reusable current rules or facts into `docs/reference/**`; keep investigation and progress in logs.

6. Add optional surfaces only when needed.

   - Add a task-local backlog only when one next step is not enough.
   - Keep repo backlog only for inactive future work.
   - Do not mirror open work across brief, backlog, working notes, and logs.

7. If context is missing, proceed with explicit assumptions and record corrections after execution.

## Anti-Patterns

- Bootstrapping project-context files for read-only or one-shot work.
- Reusing a task because the topic is similar rather than the same unresolved work.
- Turning `BRIEF.md` into append history, reusable docs, validation notes, file inventory, or rationale.
- Letting `Scope` become a touched-file list.
- Letting `Current State` narrate work sequence instead of resumable state.
- Letting `Next Step` become a backlog.
- Turning `docs/reference/**` into investigation notes, progress, or timeline narrative.
- Creating generic overflow files instead of purpose-named task-local docs.
- Keeping completed items in `docs/BACKLOG.md`.
- Mixing canonical docs, temporary notes, and finished remnants at one task root.
- Dumping raw command transcripts, repetitive micro-steps, or noisy shell output into `WORKLOG.md`.
- Duplicating the same benchmark numbers or validation matrix in both `BRIEF.md` and `WORKLOG.md` unless the second surface adds a new interpretation.
- Logging routine edits or validation passes as decisions.
- Saving absolute user-specific paths or secrets.

## Guardrail Check

Run the bundled checker by resolving `scripts/check_runtime_shape.py` from the installed `project-context` skill directory and executing it from the active repo root. If running from a subdirectory, pass `--repo-root <path>` when nested `docs` trees could confuse root detection.

The checker covers runtime shape only: required files, latest log-block shape, task/reference path markers, and secret-like markers. It does not judge ownership, semantic quality, full history, merge correctness, or broader scope discipline.

Before finalizing, reject or rewrite `BRIEF.md` if:

- It contains forbidden sections such as validation, files changed, history, evidence, or checklist.
- `Scope` is functioning as a file inventory.
- `Current State` narrates the work sequence instead of the current resumable state.
- `Next Step` contains a backlog instead of one nearest action.
- The brief is longer than needed to resume the task.

## Final Gates

- Can a later session reopen the work from `BRIEF.md` without reconstructing state?
- Is reusable current context in `docs/reference/**` instead of task logs?
- Is the execution and decision trail confined to `logs/*.md`?
- Are canonical docs separate from temporary notes and finished remnants?
- Did task reuse follow unresolved work and expected output rather than topic similarity?
- Are paths portable and secrets absent?
