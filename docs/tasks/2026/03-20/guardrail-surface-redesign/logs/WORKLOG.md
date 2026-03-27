**2026-03-20**
- fresh-context review 2갈래와 직접 점검을 합쳐, shipped checker에서 남길 surface와 repo-local test/fixture로 내려보낼 surface를 구분했다.
- shipped checker에서 `DECISIONS.md` 4-bullet hard fail과 `--memory-candidate-stats` telemetry lane을 제거하고 current runtime shape smoke test만 남겼다.
- runtime-shape tests는 latest-only log branch, task date/path branch, core file type branch, candidate enum/reachability branch를 직접 고정하도록 재정렬했다.
- migration good fixtures는 canonical destination만 남기고 source duplicates를 제거했으며, tests는 representative path-level classification만 보도록 줄였다.
