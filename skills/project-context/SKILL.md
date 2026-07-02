---
name: project-context
description: "Resume, handoff, and long-running repo work by keeping durable context across threads or agents: task briefs, logs, and reusable reference notes."
---

# Project Context

## Purpose

Keep durable repo context in ordinary files so later sessions can resume without rebuilding state.

## Use / Do Not Use

Use this skill when repo work needs durable context across threads or agents: resume or handoff, long-running work, subagent follow-through, reusable reference notes, a current task brief, or append-only logs.

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

- `docs/reference/**`: current trusted reference context only. Keep reusable rules and reliable facts here, not investigation history, progress, timeline narrative, code indexes, implementation tours, or source-file tables of contents. Include paths only for the minimum owner surfaces needed to verify the rule or fact. When user corrections or deletion requests affect a reference claim, rewrite or remove the stale claim; keep only the corrected reliable fact or a pointer to the authoritative owner.
- `docs/tasks/yyyy/mm-dd/<task-slug>/`: default task workspace for real work.
- `BRIEF.md`: rewrite-only compact resume card, not a report or log. Keep stable goal, scope boundary, current facts or conclusions, current resumable state, and nearest next step.
- In long-running work, rewrite `BRIEF.md` at each phase boundary so it contains only current resumable state; move phase history and evidence to `logs/`, `working/`, or `archive/`.
- `logs/DECISIONS.md` and `logs/WORKLOG.md`: append-only decision and execution trail. Keep evidence here, not in the brief.
- `[optional] <purpose-named-backlog>.md`: unresolved carry-over only, such as `RESEARCH-BACKLOG.md` or `QA-BACKLOG.md`. Add it only when one next step is not enough.
- `[optional] working/`: in-progress drafts, probes, staging evidence, and undecided plans.
- `[optional] archive/`: completed, rejected, replaced, or stale remnants that no longer own current state.
- `[optional] docs/BACKLOG.md`: not-yet-active repo-level future work only. Once active, move state into a dated task and remove the repo backlog item.

## `BRIEF.md` Ownership

Use only these top-level headings unless the user explicitly asks otherwise:

- `Goal` or `Intent`
- `Scope`
- `Current Understanding` or `Current Facts`
- `Current State`
- `Next Step` or `Next Actions`
- optional `Working Boundary`

Semantic rules:

- Apply user corrections and deletion requests by rewriting current state; `BRIEF.md` keeps only the resulting fact, boundary, or next step.
- `Goal` states the stable task target only. Keep background and rationale elsewhere.
- `Scope` is a boundary summary, not a touched-file list.
- `Current Understanding` is for compact conclusions only. Move design policy or durable conclusions to a current-canonical task doc or `docs/reference/**` when reusable; move investigation notes, benchmark tables, and staging evidence to `working/` or logs.
- `Current State` says what is true if the task resumes now. Move "what was done" narration to `logs/WORKLOG.md`.
- `Next Step` owns only the nearest restartable move, not a backlog. For finished work, use a compact `Reopen if ...` condition when useful.
- Do not add sections such as `Validation`, `Files Changed`, `Touched Files`, `History`, `Worklog`, `Investigation`, `Evidence`, `Completed`, or `Checklist`.
- Do not include command output, validation transcripts, investigation history, benchmark matrices, PR/release/deploy chronology, completed-work history, or touched-file inventories.
- If validation status matters, summarize it in one `Current State` sentence and keep details in `logs/WORKLOG.md`.
- If exact paths materially lower reopen cost, put the smallest useful repo-relative path set in `Working Boundary`, usually at most 5 paths.

- Budgets are soft review triggers: usually keep `BRIEF.md` around 300-500 words, each section around 1-5 bullets, and `Scope` around 1-3 bullets. Repeated pressure means the material needs another owning surface.

## Task Root Ownership

- Task root owns current-canonical docs and routers only. Every root markdown file should answer either "this is the current source for this topic" or "this routes readers to the current owners."
- Small tasks default to `BRIEF.md`, `logs/DECISIONS.md`, and `logs/WORKLOG.md`; larger tasks may add current-canonical docs or routers when they make the task easier to scan.
- Put active drafts, probes, staging evidence, and undecided plans in `working/`; chronology and validation detail in logs; completed, replaced, or stale docs in `archive/`.

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
- Subagents start without inherited context; pass a small brief: goal, latest user constraints, boundary notes, unverified assumptions or unknowns, validation command, artifact path.

## Operating Model

1. Read reusable context.

   - Use `rg` in `docs/reference/**/*.md` for the active topic.
   - Start with up to 3 narrow reference files closest to the task.
   - Before creating a new reference, or a new task for likely continuation work, check the closest project-context surfaces for the same unresolved work or reusable current context.
   - If code, API, config, tests, or an explicitly named external owner is authoritative, link to that owner instead of restating it; keep project-context content to task-specific resume or routing context.

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
   - Move only reusable current rules or reliable facts into `docs/reference/**`; keep investigation, progress, and one-off task state in task-local surfaces.
   - After creating or materially editing any task doc, re-check task root ownership.

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
- Letting task root become a mixed warehouse instead of current-canonical docs and routers.
- Turning `docs/reference/**` into investigation notes, progress, or timeline narrative.
- Turning `docs/reference/**` into a code inventory, implementation tour, or table of contents for current source files.
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

Before finalizing:

- Rewrite `BRIEF.md` if it contains forbidden sections, path inventory, progress narration, a backlog-like next step, or more detail than needed to resume.
- Reclassify root task docs if they mix current canonical docs with drafts, reports, evidence, or stale plans that belong in `working/`, logs, or `archive/`.

## Final Gates

- Can a later session reopen the work from `BRIEF.md` without reconstructing state?
- Is reusable current context in `docs/reference/**` instead of task logs?
- Is the execution and decision trail confined to `logs/*.md`?
- Does task root contain only current-canonical docs and routers?
- Did task reuse follow unresolved work and expected output rather than topic similarity?
- If `git status --short` shows untracked project-context files, are they intentionally kept, ignored, or moved into the right task/reference/archive surface?
- If a skill file changed, did the final note either verify the installed/runtime copy or state that install sync was out of scope?
- Are paths portable and secrets absent?
