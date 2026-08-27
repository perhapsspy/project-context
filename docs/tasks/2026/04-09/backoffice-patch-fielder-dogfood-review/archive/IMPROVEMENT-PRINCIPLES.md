# Improvement Principles

## Summary

이번 dogfood 기준으로 `project-context`의 코어 방향은 유지하는 편이 맞다.
문제는 코어 부족보다 mature repo에서 생기는 surface drift와 task-local sprawl이다.
그래서 다음 진화는 contract를 더 키우기보다 companion surface와 gardening loop를 분리하는 쪽이 적합하다.

## Observed Facts

- `project-context` 코어 계약은 `docs/reference/**`와 `docs/tasks/yyyy/mm-dd/<task-slug>/BRIEF.md + logs/{DECISIONS,WORKLOG}.md`다.
- `backoffice`는 깊게 도입됐지만 legacy `STATUS.md`와 extra task docs가 많이 남아 있다.
- `patch-fielder`는 최근 migration 이후 코어 계약에 더 가깝고 `STATUS.md`를 제거한 상태를 유지하고 있다.
- shape checker는 실제 drift를 잡는다.
  - `backoffice`: portable path 위반 1건
  - `patch-fielder`: core file 없는 task dir 1건

## Principle 1: Keep The Core Small

- 코어는 계속 `reference + dated task + thin runtime checker`로 유지한다.
- backlog, stream, area, review map 같은 surface를 코어에 바로 넣지 않는다.
- 코어는 항상 "새 repo에서도 바로 적용 가능한 최소 계약"만 맡는다.

이유:
- 현재 코어는 두 repo 모두에서 작동했다.
- 코어가 커지면 migration 비용과 drift surface만 다시 늘어난다.

## Principle 2: Treat Long-Running Domains As A Different Problem

- long-running domain work가 single dated task 안에서 사실상 영구 운영 문서가 되면, 이는 task contract 위반이라기보다 다른 종류의 문서 문제다.
- 이런 경우는 `task`를 더 엄격히 죄기보다 opt-in companion surface를 분리해야 한다.

현재 대표 사례:
- `../conalog/backoffice/docs/tasks/2026/03-31/fieldwork/`

판단 기준:
- task가 며칠짜리 handoff 기록이 아니라 특정 도메인의 current operating model을 계속 유지하기 시작했다.
- extra docs가 task-local supplement가 아니라 domain manual 역할을 하기 시작했다.
- sibling repo나 다른 consumer와의 계약까지 한 폴더가 계속 떠안기 시작했다.

### Refined Pattern: Separate Canonical Root And Active Overlay

`fieldwork` 사례를 다시 보면 핵심 문제는 문서 수보다도 `current-state canonical docs`, `진행 중 리워크`, `이미 끝난 검토/검증 흔적`이 같은 레벨에 섞여 있다는 점이다.

이 경우에는 long-running task 내부를 아래처럼 나누는 편이 더 적절하다.

```text
<task-root>/
  BRIEF.md
  <canonical-docs>.md
  working/
    <slug>.md
  validation/
  archive/
  logs/
```

운영 규칙:

- task root에는 항상 canonical current docs만 둔다.
- 진행 중인 리워크/서브태스크 문서는 `working/`으로 내린다.
- proof/QA 시나리오 성격 문서는 `validation/`으로 보낸다.
- 끝난 overlay 문서는 canonical에 반영한 뒤 `archive/`로 보내거나 제거한다.
- 현재 상태는 `BRIEF.md`, trail은 `logs/`로 고정하고 `PLAN/TODO/STATUS/COMPLETED` 계열 파일은 새로 만들지 않는다.

이 패턴은 코어 계약을 바꾸지 않고도 long-running task의 재개 비용을 줄인다.
다만 모든 일반 task에 강제할 정도로 보편적이진 않으므로 optional companion pattern으로 보는 편이 낫다.

## Principle 3: Promote Reusable Knowledge Earlier

- reusable rule, owner map, integration contract는 task 안에 오래 묵히지 말고 `docs/reference/**`로 올리는 편이 좋다.
- task는 "이번 작업의 current state와 trail"에 더 가깝게 유지해야 한다.
- promotion을 못 하겠으면 아직 reusable knowledge가 아닌 것이므로 task에 남기되, domain manual처럼 굳지 않게 keep-current only 원칙을 더 강하게 쓴다.

## Principle 4: Keep Local Overlays Thin And Explicit

- repo마다 `docs/README.md`, backlog, work-board 같은 overlay는 있을 수 있다.
- 다만 overlay는 코어 계약 복제가 아니라 repo-specific reading order와 local extension만 말해야 한다.
- overlay가 shipped contract를 다시 정의하기 시작하면 drift 위험이 커진다.

good example:
- `../conalog/patch-fielder/docs/README.md`

why it works:
- backlog/work-board라는 repo-local extension을 짧게 닫아 준다.
- 기본 읽기 흐름을 코어 계약과 충돌 없이 압축한다.

risk:
- 같은 내용이 `AGENTS.md`, `docs/README.md`, `docs/reference/overview.md`에 중복되기 시작하면 다시 second instruction surface가 된다.

## Principle 5: Add Gardening Loops, Not Semantic Authority

- next checker는 semantic judge가 되려고 하면 안 된다.
- 여전히 shape/thin evidence/drift detection 중심이어야 한다.
- 대신 current repo health를 위한 warning-grade gardening checks를 추가하는 편이 좋다.

예:
- empty task dir
- recently respawned `STATUS.md`
- task-local extra docs 과증식
- current task log에 portable path 위반
- repo-local overlay가 legacy surface를 다시 안내하는 drift

## Principle 6: Prefer Topic-Scoped Loading Hints Over Global Indexes

- 큰 repo에서는 reference가 늘어나므로 "어떤 1~3개를 먼저 읽어야 하는가"를 더 잘 닫아 줄 필요가 있다.
- 하지만 heavy index는 피하는 편이 좋다.
- 지금처럼 topic folder의 `overview.md`를 entrypoint로 두고, 필요하면 매우 얇은 topic metadata만 얹는 방향이 적절하다.

## Principle 7: Align Section Vocabulary Partially With Structure-First

`structure-first-docs`는 고정 템플릿을 강제하지 않지만, 기본 compose 흐름을 대체로 `Intent / Current Facts / Next Actions` 쪽으로 유지한다.
반면 `project-context`는 task tracking을 위해 `Goal / Scope / Current Understanding / Current State / Next Step / Working Boundary / Latest Validation` 같은 더 구체적인 운영 섹션을 쓴다.

여기서는 완전 통일보다는 partial alignment가 맞다.

유지할 것:

- `BRIEF.md`의 task-tracking 성격
- `Scope`
- `Working Boundary`
- `Latest Validation`

정렬할 것:

- `Goal`은 `Intent`와 사실상 같은 역할이므로, guidance에서 `Goal/Intent`를 같이 허용한다.
- `Current Understanding` + `Current State`는 문맥에 따라 `Current Facts`로 더 짧게 합칠 수 있게 허용한다.
- `Next Step`은 `Next Actions`와 같은 계열로 보고 둘 다 허용한다.
- review/analysis 성격 문서는 `Issues/Risks -> Evidence -> Required Changes` 흐름을 더 적극적으로 권장할 수 있다.

권장 결과:

- 일반 task `BRIEF`는 지금 계약을 유지하되 섹션 어휘를 조금 더 넓게 허용한다.
- long-running task의 `working/` 문서는 오히려 짧은 current-state note로 두고, 흡수 후 archive로 내리는 쪽이 낫다.
- design/review/proposal 문서는 `structure-first-docs` 쪽 section rhythm을 그대로 빌려오는 편이 좋다.

## External Comparison

### OpenAI / Harness Engineering

Source:
- https://openai.com/index/harness-engineering/

관찰:
- 작은 `AGENTS.md`를 entrypoint로 두고, 상세 정보는 도메인 docs와 feedback loop로 넘기는 방향을 강조한다.
- runtime quality는 model cleverness보다 harness와 evaluation loop 설계가 좌우된다고 본다.

비교:
- `project-context`는 이 방향과 잘 맞는다.
- 다음 개선도 문서량 증가보다 doc-gardening loop 강화가 맞다.

### Anthropic / Claude Code Memory

Source:
- https://code.claude.com/docs/en/memory

관찰:
- `CLAUDE.md`를 repo memory entrypoint로 쓰고, local/project/user memory를 층으로 나눈다.
- 지속 기억은 hierarchy와 auto-load 쪽이 강하다.

비교:
- `project-context`는 shared, committed, dated work records 쪽이 더 강하다.
- 반대로 path hierarchy나 private/local memory layer는 약하다.
- 이 약점은 코어에 넣기보다 optional companion으로 두는 편이 낫다.

### GitHub Copilot Custom Instructions

Source:
- https://docs.github.com/en/copilot/reference/custom-instructions-support

관찰:
- repository-wide, path-specific, agent instruction 파일을 구분해 지원한다.
- instruction layering을 first-class로 다룬다.

비교:
- `project-context`는 path-specific instruction 자체보다 human-readable repo docs에 더 강하다.
- monorepo나 large domain repo에선 path/topic scoped entrypoint 힌트가 보강되면 cold-start load가 더 줄 수 있다.

## Proposed Direction

### Keep In Core

- `reference` / dated `task`
- `BRIEF` as canonical current overview
- `logs` append-only rule
- thin runtime shape checker
- portable path / secret-like scan

### Move To Companion Or Optional Layer

- backlog surface
- long-running stream or area surface
- long-running task 내부의 `working/` helper lane
- section vocabulary alignment with `structure-first-docs`
- gardening warnings
- path/topic scoped loading hints

### Avoid

- `docs/memory.md` 부활
- `STATUS.md`를 다시 canonical partner로 인정
- semantic quality validator를 core checker에 넣는 것
- universal heavy index
