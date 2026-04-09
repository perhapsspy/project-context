**2026-04-09**
- 배경: `backoffice`와 `patch-fielder` dogfood 결과를 보면 코어 contract 자체보다 mature repo drift와 repo-local extension 관리가 다음 병목으로 보였다.
- 선택지: 1) shipped/local direction 문서를 바로 바꾼다. 2) 연구 결과를 task-local docs로 먼저 남기고, 코어/companion 경계를 분리한 뒤 후속 task에서 반영한다.
- 결정: 오늘은 task-local research package만 남긴다. 결과는 `개선 원칙`, `repo follow-up`, `gardening checker 설계` 세 문서로 분리한다.
- 영향: 현재 shipped contract를 성급히 확장하지 않고도 다음 의사결정 입력을 충분히 남길 수 있다.

**2026-04-09**
- 배경: 별도 세션 제안은 `fieldwork` 문제를 "문서 수 과다"보다 "canonical current docs와 active rework overlays가 같은 레벨에 섞이는 문제"로 더 정확히 설명했다.
- 선택지: 1) long-running task 문제를 stream/area 분리만으로 다룬다. 2) task를 유지하되 내부에 `workitems/` 같은 overlay lane을 두는 optional pattern을 인정한다.
- 결정: `workitems/` 레이어 아이디어는 채택 가치가 있다. 다만 코어 기본 계약으로 올리지 않고 long-running task용 optional companion pattern으로 연구 방향에 반영한다.
- 영향: 다음 개선은 "새 top-level surface 추가 여부"뿐 아니라 "task 내부에서 canonical / rework / validation / archive를 어떻게 분리할지"까지 다룰 수 있게 된다.

**2026-04-09**
- 배경: `structure-first-docs`는 고정 템플릿을 강제하지 않지만 `Intent / Current Facts / Next Actions` 같은 더 짧은 compose rhythm을 선호한다. 현재 `project-context` BRIEF 섹션 어휘는 이보다 더 task-tracking 중심이다.
- 선택지: 1) `project-context` BRIEF를 `structure-first`와 완전히 같은 section schema로 바꾼다. 2) task-tracking 섹션은 유지하되 어휘와 보조 문서 구조만 부분 정렬한다.
- 결정: 부분 정렬만 한다. core BRIEF는 유지하고, `Goal/Intent`, `Current Facts`, `Next Actions` 같은 어휘를 허용하며, long-running task의 `workitems/`와 review/design 문서는 `structure-first-docs` 리듬을 더 적극적으로 빌린다.
- 영향: 두 스킬을 함께 쓰는 repo에서 문서 재작성 비용을 줄이되, `project-context`의 task-tracking 기능은 보존할 수 있다.

**2026-04-09**
- 배경: `structure-first`와 비교해 보니 `project-context`의 shipped spec은 내용보다 섹션 구조가 덜 분해돼 있어, 언제 쓰는지/핵심 편향/안티패턴/마감 점검이 한눈에 덜 들어왔다.
- 선택지: 1) 기존 `Contract / Working Loop / Guardrail` 3단 구성을 유지한다. 2) `structure-first`와 비슷하게 shipped spec 자체를 `Purpose / Use / Core Bias / Operating Model / Anti-Patterns / Final Gates`가 보이도록 재편한다.
- 결정: 2번을 택한다. 계약 의미는 유지하되 `skills/project-context/SKILL.md`와 `docs/skill-direction.md`를 더 읽기 좋은 spec shape로 재편한다.
- 영향: 이후 README, migration skill, gardening checker 설계도 같은 spec vocabulary 위에서 더 쉽게 맞출 수 있다.

**2026-04-09**
- 배경: spec shape를 `project-context` 본체에만 맞추면 companion인 migration skill과 future gardening checker가 다시 다른 vocabulary를 쓰게 된다.
- 선택지: 1) migration skill과 checker 구현은 후속으로 미룬다. 2) 같은 턴에 migration skill spec도 재편하고 gardening checker 1차 구현까지 묶어 정리한다.
- 결정: 2번을 택한다. `skills/project-context-migration/SKILL.md`를 같은 spec shape로 다시 쓰고, 설계서에서 약속한 최소 4개 gardening check를 실제 스크립트와 테스트로 구현한다.
- 영향: 이제 `project-context`, `project-context-migration`, gardening checker가 같은 spec vocabulary와 발전 방향 위에 놓이게 된다.

**2026-04-09**
- 배경: 새 spec vocabulary가 shipped skill에만 있으면 activation surface인 README는 여전히 예전 설명 밀도를 유지하고, gardening checker도 실제 sibling repo에서 noisy할지 확인되지 않는다.
- 선택지: 1) README와 dogfood는 후속으로 미룬다. 2) 이번 턴에 README의 activation 설명을 맞추고, `backoffice`와 `patch-fielder`에 read-only dogfood를 바로 실행한다.
- 결정: 2번을 택한다. README에는 `언제 쓰나 / 언제 안 쓰나`를 추가하고, gardening checker는 sibling repo 두 곳에 read-only로 실행해 warning 품질을 확인한다.
- 영향: spec, activation surface, checker dogfood가 한 턴 안에서 연결되고, 현재 heuristic이 너무 noisy한지 바로 판단할 수 있다.

**2026-04-09**
- 배경: README에 추가한 `언제 쓰나 / 언제 안 쓰나`는 새 정보라기보다 스킬 사용 트리거를 다시 말하는 데 가까워 activation surface를 실질적으로 개선하지 못했다.
- 선택지: 1) README에 그대로 둔다. 2) README 추가분은 되돌리고, shipped spec과 local direction에서만 `Use / Do Not Use`를 유지한다.
- 결정: 2번을 택한다. README는 다시 간결한 activation surface로 두고, 사용 기준은 `SKILL.md`와 로컬 방향 문서에 남긴다.
- 영향: README가 안내서보다 트리거 재진술로 부풀어 오르는 것을 막고, 문서 역할 분리가 더 또렷해진다.

**2026-04-09**
- 배경: long-running task 개선은 연구 문서와 checker에는 반영됐지만, shipped `project-context` 본체에는 아직 "이런 경우 어떻게 정리할지"가 직접 안내되지 않았다.
- 선택지: 1) `workitems/` 패턴을 계속 로컬 방향에만 둔다. 2) core contract는 유지하되 shipped skill과 migration skill에 optional advanced guidance로 짧게 올린다.
- 결정: 2번을 택한다. `workitems/`, `validation/`, `archive/`는 required tree로 승격하지 않고, long-running task drift를 줄이는 선택적 정리 패턴으로만 shipped guidance에 반영한다.
- 영향: 외부 repo를 건드리지 않고도 이 스킬 자체가 long-running task 문제에 대한 더 직접적인 운영 힌트를 제공하게 된다.

**2026-04-09**
- 배경: `docs/skill-direction.md`는 기준 문서여야 하는데, 점점 README 평가 루프나 dogfood 진행 문맥 같은 process-heavy 내용을 섞어 why보다 how/when 쪽으로 기울었다.
- 선택지: 1) 해당 문서 안에 기준과 리뷰 절차를 같이 둔다. 2) `skill-direction`은 기준과 이유만 남기고, 리뷰 기준/절차는 별도 로컬 문서로 분리한다.
- 결정: 2번을 택한다. `docs/skill-direction.md`는 what-why 중심으로 다시 쓰고, 반복 가능한 로컬 리뷰 기준은 `docs/review-method.md`로 분리해 `AGENTS.md`에서 참조한다.
- 영향: 방향 문서는 이정표 역할에 집중하고, review method는 별도 자산으로 재사용할 수 있게 된다.

**2026-04-09**
- 배경: long-running guidance가 `workitems/`, `validation/`, `archive/`를 예시로 들면서도 읽는 사람에게는 사실상 권장 tree처럼 느껴질 수 있었고, 이는 "내용 강제보다 얇은 경계"라는 방향과 완전히 맞지 않았다.
- 선택지: 1) 지금 문구를 유지한다. 2) helper lane의 이름과 세부 구조는 repo-local로 두고, shipped skill은 root current docs와 temporary working notes의 분리 원칙만 더 약하게 말한다.
- 결정: 2번을 택한다. `backoffice`의 `working/` 규칙에서 흡수할 것은 이름이 아니라 원칙이다. shipped guidance는 `working/`나 `workitems/`를 repo-local helper lane 예시로만 언급하고, `working/README`나 backlog authority 같은 세부 surface는 흡수하지 않는다.
- 영향: long-running drift에 대한 힌트는 남기되, 특정 repo의 운영 형태를 사실상 표준처럼 밀어 넣는 위험은 줄인다.

**2026-04-09**
- 배경: helper lane 이름을 `working/`와 `workitems/`로 같이 두면 optional example이 아니라 vocabulary drift처럼 읽히고, 현재 dogfood evidence도 `working/` 쪽이 더 넓은 temporary-note 용도에 맞는다.
- 선택지: 1) 둘 다 example으로 유지한다. 2) shipped guidance와 current research docs에서는 `working/`으로 통일하고, `workitems/`는 과거 대안으로만 남긴다.
- 결정: 2번을 택한다. 현재 guidance vocabulary는 `working/`으로 통일한다.
- 영향: long-running helper lane 예시가 한 이름으로 정리돼 읽기 흐름이 안정되고, `workitems/`가 사실상 두 번째 표준처럼 보이는 문제를 줄인다.

**2026-04-09**
- 배경: 이번 턴은 리뷰 결과를 말하는 데 그쳤고, 실제로 어떻게 dogfood할지에 대한 반복 가능한 로컬 루프는 아직 문서화돼 있지 않았다.
- 선택지: 1) 현재 task logs에만 임시로 절차를 남긴다. 2) 이 레포에서 반복 사용할 수 있는 dogfood method를 별도 로컬 문서로 만들고, 같은 턴 안에 현재 변경셋에 직접 적용한다.
- 결정: 2번을 택한다. `docs/dogfood-method.md`를 만들고, activation/write/reopen/guardrail/drift pass를 현재 변경셋에 대해 한 번 실행한 결과를 task-local doc으로 남긴다.
- 영향: 이후 shipped skill 변경도 "논의 후 리뷰"가 아니라 "설계된 dogfood를 거친 변화"로 남길 수 있게 된다.
