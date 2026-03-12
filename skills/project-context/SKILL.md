---
name: project-context
description: File-based working context for coding agents using a compact global working memory, durable reference notes, and dated task records for most write-bearing work. Use when a repository keeps, or should start keeping, agent context in `docs/memory.md`, `docs/reference/`, and `docs/tasks/...` so later sessions can resume work without rebuilding state from scratch.
---

# Project Context

Keep working context in the repository so later sessions can resume work without rebuilding state from scratch.

Leave a small amount of working memory, reusable reference notes, and task-local history behind as ordinary files. Keep the structure simple enough that humans can read and edit it directly.

## Contract

```text
docs/
  memory.md
  reference/**/*.md
  tasks/yyyy/mm-dd/<task-slug>/
    BRIEF.md
    STATUS.md
    logs/{DECISIONS,WORKLOG}.md
    MEMORY-CANDIDATES.md (optional)
```

- `docs/memory.md` is the rewrite-only global working memory (`<=120` lines, declarative): active invariants, current phase, temporary global constraints, currently active cross-task conditions, and rules worth loading almost every time. Keep it compressed; do not store topic detail, task chronology, or long append history there.
- `docs/reference/` holds durable project-domain context by topic: stable facts, conventions, external integration patterns (auth, rate limits, error handling, project-specific usage conventions), constraints, and topic guides reused across tasks. It may be authored directly when the task itself is domain-context curation or the reusable domain context is already clear. Move reusable topic detail there instead of leaving it only in task logs. Keep names lowercase kebab-case and use `rg`, not an index.
- `docs/tasks/yyyy/mm-dd/<task-slug>/` is the default task workspace for most real work, split into rewrite-only snapshots (`BRIEF.md`, `STATUS.md`, optional `MEMORY-CANDIDATES.md`) and append-only history (`logs/DECISIONS.md`, `logs/WORKLOG.md`).
- `BRIEF.md` is the rewrite-only stable reopen brief: goal, scope, current understanding, and current output snapshot. Do not append chronological work notes, command transcripts, or validation trails there.
- `STATUS.md` is the rewrite-only current handoff note: status, next step, blockers, declared read scope, declared write scope, and latest validation. Prefer no title line; start directly with short current-state bullets or key-value lines. Fixed headings are not required.
- `MEMORY-CANDIDATES.md` is the optional rewrite-only current memory-candidate board for task-derived `docs/memory.md` updates. Do not use it for `docs/reference/`, direct reference authoring, or append history. If present, keep it plain: no title text, no comments, only `- <STATE> | <summary> | <evidence-pointer>` entries.
- Only logs are append-only. New log entries append under `**YYYY-MM-DD**` headings in the current user language; the latest `DECISIONS.md` block keeps 4 bullet lines (background, options, decision, impact), and the latest `WORKLOG.md` block keeps at least 1 bullet line of execution evidence.
- Subagents start without inherited context; pass only a small task brief: goal, constraints, declared read scope, declared write scope, validation command, artifact path.
- If a relevant task exists, read `BRIEF.md`, `STATUS.md` before logs and merge only after confirming the result stayed within its declared read scope.
- Never store secrets.

## Memory Candidates

- Write reusable topic detail into `docs/reference/**/*.md` directly when the task itself is topic curation or the reusable domain context is already clear.
- Use task `MEMORY-CANDIDATES.md` only for task-derived `docs/memory.md` updates that should be reviewed as compressed global working-memory notes.
- Example: if a task clarifies reusable external API auth rules, write `docs/reference/api/auth.md` directly.
- Format: `- <STATE> | <summary> | <evidence-pointer>` where `STATE` is `PENDING | APPLIED | REJECTED`.
- `summary` should be target-ready declarative text; prefer 80-100 chars and keep a 120-char hard cap.
- `evidence-pointer` should be exactly one log pointer like `logs/DECISIONS.md@L...` or `logs/WORKLOG.md@L...`; keep a 32-char hard cap, and note the guardrail checks pointer reachability only.
- If a task needs both surfaces, write topic detail into `docs/reference/` directly and keep `MEMORY-CANDIDATES.md` limited to the compressed global note many tasks should reload soon.
- Treat `MEMORY-CANDIDATES.md` as a live board, not an archive: keep only active review state there, and omit or delete the file once no unresolved candidates remain.

## Working Loop

Read-only work stops here: for questions, reviews, and one-shot inspections, stay read-only and do not bootstrap the layout or create a dated task unless the work is meant to leave durable project-context files behind.

For write-bearing adoption work, if the repo does not have `docs/memory.md` yet and is effectively empty, bootstrap the layout first: create `docs/memory.md`, `docs/reference/`, and one dated task with `BRIEF.md`, `STATUS.md`, and `logs/DECISIONS.md` / `logs/WORKLOG.md`. Create `MEMORY-CANDIDATES.md` only if bootstrap itself discovers task-derived memory candidates. If the repo already has scattered docs, notes, ADRs, runbooks, task history, or partial target-tree adoption that still needs consolidation, use `project-context-migration` instead of bootstrapping a blank layout.

1. Read `docs/memory.md`.
2. Working read budget: search `docs/reference/**/*.md` with `rg`; open at most 3 reference files, preferring the narrowest topic files closest to the active task.
3. Working read budget: if a relevant task exists, open at most one `docs/tasks/...` task; within it read `BRIEF.md` and `STATUS.md` first, then logs as needed.
4. If a relevant task exists, reuse its current snapshots only when its declared read scope still matches what you actually needed to inspect; otherwise start a new dated task.
5. For most write-bearing tasks, create or update one dated task, rewrite `BRIEF.md`, `STATUS.md`, and optional `MEMORY-CANDIDATES.md` in place as current snapshots, append decisions/execution only to the logs, and write reusable topic detail into `docs/reference/` directly when it becomes clear. Skip task creation only for very small, low-judgment, immediately-finished changes.
6. When applying `MEMORY-CANDIDATES.md`, rewrite `docs/memory.md`, mark entries `APPLIED` or `REJECTED`, then rewrite or remove the file so only unresolved candidates remain. If no unresolved memory candidates exist, omit `MEMORY-CANDIDATES.md`.
7. If no direct hit, proceed with explicit assumptions and record corrections after execution.

## Guardrail Check

- Thin current-runtime check only: required paths/files, latest log-block shape, optional `MEMORY-CANDIDATES.md` syntax/evidence-pointer reachability, and secret-like markers; not semantic quality, full history, merge correctness, or budget/scope discipline.

While following this skill, the agent can run the bundled checker with the skill-relative path `scripts/check_runtime_shape.py`. The checker infers the target repo from the current working directory, so keep the shell at the active repo root, or any subdirectory inside it:

```bash
python3 scripts/check_runtime_shape.py
```
