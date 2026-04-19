

**2026-04-19**
- 새 dated task shell을 만들고 필수 변경 범위를 shipped migration skill과 local direction 최소 동기화로 제한했다.
- shipped project-context-migration에 Rollout Policy와 Authority Boundary를 추가하고, LEAVE bias·cleanup rule·final gate를 policy/authority 기준으로 다시 정리했다.
- runtime shape와 task-local log checks를 확인했고, 이번 변경은 test matrix 확장 없이 필수 confidence만 남기기로 정리했다.
- 서브에이전트 리뷰를 반영해 migration skill의 authority/cleanup wording 강도를 낮추고, current task BRIEF의 portable path를 고쳤으며, representative migration fixture BRIEF 2건에 policy와 authority 판단을 최소 반영했다.
- 서브에이전트 재리뷰를 반영해 rollout policy wording을 replace/bridge 중심 framing으로 낮추고, migration fixture test에 Rollout Policy surface assertion을 추가했으며, gardening과 전체 unittest까지 다시 돌려 BRIEF closeout confidence를 맞췄다.
- user 지시대로 migration skill에서 project-context 본체 contract와 script semantics를 다시 설명하던 문장을 걷어내고, adoption intent와 duplication cleanup 같은 migration-specific 판단만 남기도록 줄였으며, representative fixture BRIEF와 테스트도 그 수준에 맞춰 간결하게 되돌렸다.
- 최소주의 기준 재리뷰를 반영해 migration skill에서 adoption-intent 축을 별도 섹션으로 두던 흔적과 반복 deference를 걷어내고, representative beta BRIEF도 snapshot/working-boundary를 제거해 thinner example로 맞췄다.
