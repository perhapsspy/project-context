---
name: project-context
description: Keep coding-agent working context in ordinary project files with a compact global memory, reusable reference notes, and dated task records.
---

# Project Context

Keep working context in ordinary repository files so later sessions can resume without rebuilding state from scratch.

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

- `docs/memory.md` is the rewrite-only global working memory (`<=120` lines, declarative) for compressed current global state. Keep it compressed; do not put topic detail, task chronology, long append history, or duplicate standing rules there.
- `docs/reference/` holds reusable project-domain context by topic: conventions, constraints, and integration patterns. Write canonical topic detail there, not in task logs. If a task updates reference content, keep the path, rationale, and change trace in the task. Keep paths lowercase kebab-case and use `rg`, not an index.
- `docs/tasks/yyyy/mm-dd/<task-slug>/` is the default task workspace for most real work, split into rewrite-only snapshots (`BRIEF.md`, `STATUS.md`, optional `MEMORY-CANDIDATES.md`) and append-only history (`logs/DECISIONS.md`, `logs/WORKLOG.md`).
- `BRIEF.md` is the rewrite-only stable reopen brief: goal, scope, current understanding, and current output snapshot. Do not append chronological work notes, command transcripts, or validation trails there.
- `STATUS.md` is the rewrite-only current handoff note: status, next step, blockers, declared scopes, and latest validation. Prefer no title line. When declared scopes are present, prefer literal `declared read scope` / `declared write scope` labels so later sessions can scan reuse boundaries quickly.
- `MEMORY-CANDIDATES.md` is the optional rewrite-only current memory-candidate board for task-derived `docs/memory.md` updates. Do not use it for `docs/reference/`, direct reference authoring, or append history. If present, keep it plain: no title text, no comments, only `- <STATE> | <summary> | <evidence-pointer>` entries.
- Only logs are append-only. Add entries under `**YYYY-MM-DD**` headings in the current user language. Keep the latest `DECISIONS.md` block ADR-lite (usually 4 bullets) and the latest `WORKLOG.md` block as 1+ execution bullets.
- Subagents start without inherited context; pass only a small task brief: goal, constraints, declared read scope, declared write scope, validation command, artifact path.
- If a relevant task exists, read `BRIEF.md`, `STATUS.md` before logs and merge only after confirming the result stayed within its declared read scope.
- Never store secrets.

## Memory Candidates

- Use task `MEMORY-CANDIDATES.md` only for task-derived `docs/memory.md` updates. Treat it as a conservative promotion gate, not a general review tool.
- Keep out anything that only restates instructions, standing conventions, or topic detail already owned elsewhere. If ownership is still unclear, keep it `PENDING`; otherwise mark it `REJECTED`.
- Format: `- <STATE> | <summary> | <evidence-pointer>` where `STATE` is `PENDING | APPLIED | REJECTED`.
- `PENDING` means the task has not finished the memory-ownership judgment yet. `REJECTED` means the note should not be promoted into `docs/memory.md`.
- `summary` should be target-ready declarative text; prefer 80-100 chars and keep a 120-char hard cap.
- `evidence-pointer` should be exactly one log pointer like `logs/DECISIONS.md@L...` or `logs/WORKLOG.md@L...`; keep a 32-char hard cap, and note the guardrail checks pointer reachability only.
- Treat `MEMORY-CANDIDATES.md` as a live board, not an archive: keep only active review state there, and omit or delete the file once no unresolved candidates remain.

## Working Loop

Read-only work stops here: for questions, reviews, and one-shot inspections, stay read-only and do not bootstrap the layout or create a dated task unless the work is meant to leave durable project-context files behind.

If the repo is effectively empty, bootstrap the layout first.
If the repo already has `docs/memory.md`, `docs/reference/`, and `docs/tasks/...`, use the normal flow below.
Otherwise, choose an explicit adoption approach instead of treating the bootstrap path below as a migration plan.

For that bootstrap case, create `docs/memory.md`, `docs/reference/`, and one dated task with `BRIEF.md`, `STATUS.md`, and `logs/DECISIONS.md` / `logs/WORKLOG.md`. Create `MEMORY-CANDIDATES.md` only if bootstrap itself discovers task-derived memory candidates.

1. Read `docs/memory.md`.
2. Search `docs/reference/**/*.md` with `rg`; open at most 3 reference files, preferring the narrowest topic files closest to the active task.
3. If a relevant task exists, open at most one `docs/tasks/...` task; within it read `BRIEF.md` and `STATUS.md` first, then logs as needed.
4. If a relevant task exists, reuse its current snapshots only when its declared read scope still matches what you actually needed to inspect; otherwise start a new dated task.
5. For most write-bearing tasks, create or update one dated task, rewrite `BRIEF.md`, `STATUS.md`, and optional `MEMORY-CANDIDATES.md` in place as current snapshots, append decisions/execution only to the logs, and write reusable topic detail into `docs/reference/` directly when it becomes clear. Skip task creation only for very small, low-judgment, immediately-finished changes.
6. When applying `MEMORY-CANDIDATES.md`, rewrite `docs/memory.md`, promote only notes that still belong in global memory, and leave only unresolved entries in the file. If no unresolved candidates remain, omit `MEMORY-CANDIDATES.md`.
7. If memory/reference/task search finds no relevant context, proceed with explicit assumptions and record corrections after execution.

## Guardrail Check

- Checks only current runtime shape: required paths/files, `docs/memory.md` line cap, latest log-block shape, optional `MEMORY-CANDIDATES.md` syntax/hard caps/evidence-pointer reachability, and secret-like markers.
- Does not judge candidate ownership, semantic quality, full history, merge correctness, or broader scope discipline.

Run the bundled checker by resolving the skill-relative script `scripts/check_runtime_shape.py` from the installed `project-context` skill directory and executing it from the active repo root. If running from a subdirectory, pass `--repo-root <path>` when nested `docs` trees could confuse root detection.
