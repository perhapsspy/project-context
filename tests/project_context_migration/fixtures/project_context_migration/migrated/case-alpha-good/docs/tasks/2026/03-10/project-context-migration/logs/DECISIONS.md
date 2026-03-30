**2026-03-10**
- 배경: legacy 문서 네 개가 흩어져 있었고 target contract는 reference와 task로 현재 working context를 정리하길 요구했다.
- 옵션: 애매한 문서를 바로 reference로 승격하거나, task-local 문서를 task에 두거나, 원본만 유지하는 방법이 있었다.
- 결정: `docs/system.md`와 `runbooks/deploy.md`는 canonical reference로 재작성하고, `notes/2026-02-14-auth-spike.md`는 dated task로 옮기며, `docs/user-guide.md`는 LEAVE로 유지한다.
- 영향: canonical AI context는 `docs/reference/**`와 `docs/tasks/**` 아래에 정리되고, `LEAVE` 대상만 source surface에 current owner로 남는다.
