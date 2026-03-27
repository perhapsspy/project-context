**2026-03-20**
- 배경: 남은 테스트 이슈는 “더 많이 고정하자”가 아니라, 놓친 high-signal branch는 메우고 presentation-level exact pinning은 줄이자는 contract alignment 문제다.
- 선택지: 1) fixture와 CLI 출력을 더 세게 고정한다. 2) core shape / representative classification만 보강하고, harmless phrasing/layout drift에는 덜 민감하게 만든다.
- 결정: thin guardrail 철학을 유지하면서 runtime-shape의 빠진 branch를 추가하고, migration fixture는 대표 결과만 적정 수준으로 복원하며, CLI exact-output pinning은 완화한다.
- 영향: suite가 실제 contract regression에는 더 민감해지고, wording/layout drift에는 덜 brittle해진다.
