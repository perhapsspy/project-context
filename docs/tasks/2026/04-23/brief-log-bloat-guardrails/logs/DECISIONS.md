# DECISIONS

**2026-04-23**
- 현재 diff는 GPT-5.4 계열 모델이 `BRIEF.md`와 logs를 과하게 키우는 문제를 막기 위해 shipped skill과 로컬 기준 문서를 함께 줄이는 방향으로 잡혀 있다.
- 이번 follow-up은 방향 자체를 뒤집지 않고, 새 hard rule 중 실제 evidence 없이 과하게 읽힐 수 있는 항목만 wording 또는 guardrail 관점에서 다시 정렬한다.
- 전체 테스트와 기존 checker가 이미 통과하는 상태라서 blocking defect보다는 주장 강도와 enforcement 범위 정렬이 핵심 문제다.
- 다음 구현은 새 규칙 확대보다 low-noise 검출 항목 선별과 unsupported absolute 표현 조정에 집중하게 된다.
