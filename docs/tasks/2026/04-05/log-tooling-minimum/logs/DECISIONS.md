**2026-04-05**
- 배경: append-only logs를 markdown 직접 편집에 맡기면 에이전트마다 쓰기 방식이 달라지고, 전체 파일을 다시 읽는 경로도 쉽게 남는다.
- 선택지: 1) contract만 유지하고 직접 편집을 허용한다. 2) 전용 log CLI를 추가해 append/tail/check를 표준 경로로 둔다.
- 결정: ordinary markdown contract는 유지하되, `append/tail/check`를 가진 최소 log CLI를 추가하고 latest-block 판독은 공용 로직으로 모은다.
- 영향: 이후 세션은 logs를 직접 patch하지 않고도 최신 블록만 읽거나 append-only 검사만 수행할 수 있다.
- Dogfood scenario A: happy-path CLI flow works from repo root for both WORKLOG and DECISIONS.

**2026-04-05**
- 배경: DECISIONS는 실제 운용에서 한 결정당 4줄 ADR-lite block으로 남기는데, 기존 generic append/check는 그 구조를 강제하지 못했다.
- 선택지: 1) generic append를 유지한다. 2) ppend-decision으로 원자적 4-line block을 쓰고 check도 같은 계약을 본다.
- 결정: DECISIONS는 ppend-decision으로만 추가하고, 최신 block은 정확히 4 bullet이어야 통과하게 바꾼다.
- 영향: 날짜가 바뀌거나 같은 날짜에 결정이 추가돼도 decision 단위 block이 유지되고, runtime checker와 CLI가 같은 shape drift를 잡는다.

**2026-04-05**
- 배경: CLI surface를 worklog/decision으로 분리한 뒤에도 decision append와 decision tail이 malformed latest decision block을 그대로 넘기면 shape drift를 숨길 수 있다.
- 선택지: 1) decision check만 엄격하게 둔다. 2) decision append와 decision tail도 같은 latest decision validation을 강제한다.
- 결정: decision append, decision tail, decision check, runtime checker가 모두 같은 decision-block validation을 공유하게 맞춘다.
- 영향: malformed latest decision block은 수동 tail이나 후속 append로도 숨겨지지 않고, live task 예시도 현재 command surface에 맞는 최신 decision block으로 갱신된다.
