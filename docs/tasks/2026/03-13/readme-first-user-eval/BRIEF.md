# README First-User Eval

- owner: ai
- started_at: 2026-03-13
- status: done

## 목적
- README를 처음 스킬을 써보려는 사용자가 사용 전 유용성을 판단하는 문서로 평가하되, README 책임을 과하게 키우지 않는 얇은 자체 평가 루프로 정리한다.

## 실행 범위
- `README.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/skill-direction.md`를 비교한다.
- fresh-context 서브에이전트로 first-user usefulness, framing accuracy, weak-criticism filter를 독립 검토한다.
- 사용자 피드백으로 과검토 성격을 다시 걸러내고, 같은 실수를 줄이도록 `docs/skill-direction.md`의 README 자체 평가 루프를 더 얇게 조정한다.

## 현재 산출물 스냅샷
- 기존 서브에이전트 리뷰 중 read-only vs write-bearing 경계와 exact output state 요구는 README 책임을 과하게 본 과검토로 정리했다.
- README는 activation surface로서 이미 충분하다는 쪽으로 정리하고, 남길 만한 피드백은 migration 설명이 전량 이관처럼 읽히지 않게 더 좁힐지 정도로 낮췄다.
- `docs/skill-direction.md`의 README 자체 평가 루프를 activation 중심으로 줄이고, 이번 task에는 README 본문을 유지한 채 평가 기준만 정제한 결론을 남긴다.
