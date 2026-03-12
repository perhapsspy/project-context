**2026-03-10**
- 배경: legacy 문서 네 개가 흩어져 있었고 target contract는 memory, reference, task 분리를 요구했다.
- 옵션: 애매한 문서를 바로 memory/reference로 승격하거나, task-local 문서를 task에 두거나, 원본만 유지하는 방법이 있었다.
- 결정: `docs/system.md`와 `runbooks/deploy.md`는 canonical reference로 재작성하고, `notes/2026-02-14-auth-spike.md`는 dated task로 옮기며, `docs/user-guide.md`는 LEAVE로 유지한다.
- 영향: 새 `docs/memory.md`, `docs/reference/**`, `docs/tasks/**`가 생기고 원본 legacy 파일은 audit 근거로 남는다.
