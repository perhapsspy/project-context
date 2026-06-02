# Decisions

**2026-06-02**

- Background: Recent Conalog dogfood showed recurring `BRIEF.md` bloat, root doc sprawl, stale current docs, and weak `working`/logs/`archive` ownership.
- Decision: Treat the next improvement as context surface ownership and cleanup habit work, not as a generic brevity pass.
- Why: The repeated failure is that agents keep growing the document they created instead of re-sorting content into current root docs, `working`, append-only logs, or `archive`.
- Impact: The follow-up should review shipped skill wording first, then decide whether to add warning-only checker/helper support.

**2026-06-02**
- Background: The proposal lists shipped wording, semantic checker, helper, and dogfood cleanup as possible slices, while existing repo tooling already separates runtime shape failure checks from warning-grade gardening checks.
- Decision: Implement only the shipped skill wording and repo-local direction slice now; leave checker/helper work as a later gardening-check follow-up.
- Why: The repeated dogfood failure is first a surface ownership habit problem, and expanding scripts in the same pass would mix guidance stabilization with new heuristic behavior.
- Impact: SKILL.md now owns the BRIEF/task-root/working/archive guidance, docs/skill-direction.md mirrors the direction briefly, and future checker work should target check_gardening.py rather than check_runtime_shape.py.

**2026-06-02**
- Background: Sub-agent review and fresh sampling confirmed the proposal diagnosis, but found the first wording pass left too much discretion around small-task extra docs and large-task root budgets.
- Decision: Tighten Task Root Ownership wording so small tasks allow PLAN only for real handoff, working only for active drafts/probes, extra root markdown only for current-canonical/router use, and large-task root markdown over 5 files requires a README router/owner note or folder demotion.
- Why: The sampled failures were not just high file counts; they were unrouted or stale root surfaces and oversized BRIEF files that made current state hard to find.
- Impact: The shipped skill now preserves the supported direction while reducing the main loophole that could have reintroduced root document sprawl.

**2026-06-02**
- Background: The user challenged whether complex filename/count rules are the right lever, suggesting ownership and layering may be enough to guide structured document creation and cleanup even when names vary.
- Decision: Make shipped SKILL.md primarily ownership/lifecycle based, with numeric budgets and root-doc counts framed as soft review triggers rather than core correctness rules.
- Why: The dogfood failures were semantic ownership drift: BRIEF as spec, root as warehouse, and current docs as history dumps. Hard filename/count rules can create false compliance while missing mixed ownership.
- Impact: Core guidance now asks every root doc to be current-canonical or a router, while BRIEF word/bullet limits remain soft budgets and checker/gardening follow-up can own heuristic warnings.
