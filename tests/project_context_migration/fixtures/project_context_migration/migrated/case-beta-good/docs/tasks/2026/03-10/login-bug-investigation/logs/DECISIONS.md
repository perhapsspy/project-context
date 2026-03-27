**2026-03-10**
- 배경: `tasks/login-bug.md`는 원인 미확정 조사 기록이며 trustworthy date가 없어 current truth로 보기 어렵다.
- 선택지: 1) reference로 승급한다. 2) task으로 유지하고 이후 결론이 나면 승급하며, task date는 migration date로 기록한다.
- 결정: `login-bug-investigation` task으로 유지하고, source date가 불명확하므로 migration date `2026-03-10`를 사용한 사실을 task에 남긴다.
- 영향: 미확정 조사 로그가 reference나 memory를 오염시키지 않고, 날짜 불확실성도 reopen surface에서 바로 읽을 수 있다.
