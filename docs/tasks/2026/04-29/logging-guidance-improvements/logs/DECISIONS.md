**2026-04-29**
- Background: recent conalog logs show useful evidence in long-running tasks, but also show micro-iteration and validation history making `WORKLOG.md` harder to scan.
- Decision: improve guidance and examples first, and only adjust tooling for the low-risk gap where WORKLOG evidence needs nested bullets.
- Why: adding more hard rules would make the shipped contract heavier, while allowing nested WORKLOG evidence matches real usage without weakening DECISIONS shape.
- Impact: the change should make long-running task logs easier to reopen while preserving the small core layout and checker-backed decision-log contract.
