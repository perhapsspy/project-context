**2026-04-17**
- 배경: Scope 섹션이 touched-file inventory로 길어지는 사례가 반복돼 reopen entrypoint 비용만 키우고 있었다.
- 결정: Scope는 짧은 boundary summary로 제한하고 exact path inventory는 필요할 때만 Working Boundary로 미루는 계약과 gardening warning을 추가한다.
- 이유: 이 레포에는 BRIEF 생성기가 없어서 wording과 live example, drift detector를 함께 바꾸는 편이 재발 방지에 더 직접적이다.
- 영향: future BRIEF authoring은 더 짧아지고, representative examples와 gardening check가 같은 기준으로 drift를 잡는다.

**2026-04-17**
- 배경: Scope 자체도 default skeleton에서 내릴지 재검토 요청이 들어왔고, 현재 계약과 live example, guardrail 방향을 다시 대조했다.
- 결정: Scope는 default skeleton에 남기고, 문제를 섹션 존재가 아니라 path-list 오용으로 본 현재 계약을 유지한다.
- 이유: 이 레포가 이미 Scope를 짧은 boundary summary로 정의하고 있고, Working Boundary를 exact-path overflow로 분리한 상태라 지금 evidence만으로는 Scope 제거보다 유지가 더 작고 일관된 변경이다.
- 영향: 이후 drift 대응은 Scope optional화보다 path-list sprawl 억제와 summary-level authoring 예시 유지에 집중한다.
