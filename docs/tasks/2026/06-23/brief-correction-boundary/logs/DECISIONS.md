# Decisions

**2026-06-23**

- Background: playground 조사에서 `BRIEF.md`가 사용자 정정과 삭제 지시를 해설로 보존하며 길어지는 패턴이 확인됐다.
- Decision: `project-context` 변경 여부는 새 세션에서 타당성 검토를 먼저 받은 뒤 결정한다.
- Why: 현재 스킬에도 관련 규칙이 이미 많아, 바로 수정하면 중복 방어문이 될 수 있다.
- Impact: 새 세션은 `PROJECT-CONTEXT-BOUNDARY-PROPOSAL.md`를 기준으로 수정 필요성만 판단하고 파일 수정은 하지 않는다.

**2026-06-24**
- Background: 검토와 딥리즈너 판단 모두 정정/삭제 입력이 설명 재료로 보존되는 drift는 기존 rewrite-only 규칙의 적용 지점을 더 선명하게 해야 한다고 봤다.
- Decision: `BRIEF.md Ownership` semantic rules에 사용자 정정과 삭제 요청은 현재 상태 rewrite로 반영하고 결과 사실, 경계, 다음 단계만 남긴다는 1개 bullet을 추가한다.
- Why: 기존 logs 정책을 복제하지 않으면서 반복된 BRIEF 비대화 계열 drift를 직접 줄일 수 있는 가장 작은 shipped contract 보강이다.
- Impact: 이후 `BRIEF.md` 갱신에서 사용자 피드백 자체를 해설로 남기지 않고, 결과 상태만 남기는 쪽을 기본 해석으로 삼는다.
