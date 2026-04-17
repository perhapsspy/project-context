

**2026-04-17**
- BRIEF 과작성 원인 분석을 실제 contract 개선으로 연결할 필요가 생겼다.
- 새 surface를 더하지 않고 BRIEF 작성 컷라인, optional heading 기준, live example을 함께 조정한다.
- 계약은 이미 얇지만 작성 순간에 두꺼운 example과 습관이 다시 작동하므로 wording과 evidence를 같이 바꾸는 편이 직접적이다.
- 이후 BRIEF 작성은 기본적으로 더 짧아지고, 설계 task도 상세를 별도 doc으로 분리하는 기준이 선명해진다.

**2026-04-17**
- optional heading 남용을 추가 checker로 바로 잡을지 함께 검토했다.
- 이번 변경은 wording, local guidance, live example 정리에 집중하고 새 heuristic gardening rule은 넣지 않는다.
- 현재 evidence로는 optional heading overuse를 안정적으로 판별하기 어렵고, 억지 규칙은 historical task까지 noisy info를 많이 낼 가능성이 있다.
- guardrail은 기존 수준을 유지하고, 대신 contract wording과 representative BRIEF example이 더 직접적으로 작성 습관을 교정한다.

**2026-04-17**
- 서브에이전트 브레인스토밍과 리뷰 결과를 반영해 wording을 다시 줄였다.
- BRIEF thinness는 shipped skill의 기존 BRIEF rule 한 줄 치환으로 흡수하고, local docs는 중복 설명보다 짧은 reminder만 남긴다.
- 새 bullet을 더하는 방식보다 기존 contract 문장에 목적을 접어 넣는 편이 이 레포 톤과 더 잘 맞고 중복도 적다.
- 변경셋은 삽입보다 삭제가 커졌고, representative BRIEF 예시도 같은 리듬으로 더 짧아진다.
