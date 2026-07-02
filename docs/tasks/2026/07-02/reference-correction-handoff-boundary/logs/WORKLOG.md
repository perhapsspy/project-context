**2026-07-02**
- `skills/project-context/SKILL.md`에서 `docs/reference/**` 설명에 사용자 정정/삭제 요청이 reference claim에 영향을 주면 stale claim을 지우거나 현재 믿을 수 있는 사실/source owner pointer만 남기도록 보강했다.
- subagent handoff brief 항목을 `latest user constraints`와 `unverified assumptions or unknowns`까지 포함하도록 좁게 고쳤다.
- `check_runtime_shape.py`, 전체 unittest, `git diff --check`가 통과했다. 딥리즈너 리뷰는 shipped skill 문구를 유지하고, 검증 전 상태로 남아 있던 task `BRIEF.md`의 다음 단계만 현재 상태로 고치라고 봤다.
