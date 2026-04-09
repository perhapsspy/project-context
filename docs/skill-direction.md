# 스킬 방향

## Purpose
- `project-context`의 shipped contract는 에이전트가 실제로 따라야 하는 최소 행동만 담는다.
- 이 문서는 그 contract를 어떤 방향으로 다듬어야 하는지에 대한 레포 로컬 기준을 남긴다.
- 목표는 working context를 저장소 안의 평범한 파일에 남겨 다음 세션의 cold start 비용을 줄이는 것이다.

## 역할 경계
- shipped `SKILL.md`는 에이전트가 실행해야 할 규칙을 맡는다.
- 이 문서는 shipped skill의 주장 범위, 문구 톤, surface 경계, 진화 원칙 같은 기준 맥락을 맡는다.
- 테스트, fixture, dogfood 결과, 설계 메모는 근거가 될 수는 있어도 이 문서의 주제는 아니다.
- 레포 로컬 자산은 shipped skill을 보조할 수는 있어도, shipped contract보다 더 강한 의무를 만들어서는 안 된다.

## Core Bias
- 외부 시스템이나 숨겨진 메모리보다 저장소 안의 평범한 파일을 우선한다.
- 같은 목적이면 surface 수를 늘리기보다 기존 surface의 역할을 더 선명하게 나누는 쪽을 택한다.
- 이름, 요약, help text는 실제로 증명된 범위 중 가장 좁은 범위를 기준으로 잡는다.
- 설명을 늘리기보다 보장과 비보장을 먼저 남긴다.
- 에이전트 전용 표현보다 사람도 바로 읽고 고칠 수 있는 단순한 말과 구조를 선호한다.
- 경로 표기는 repo-relative나 `<repo-root>`, `<task-root>`, `$CODEX_HOME` 같은 project-owned placeholder를 우선한다.

## Contract Direction
- 코어 surface는 `docs/reference/**`와 dated task 아래의 `BRIEF.md` 및 `logs/*.md`를 중심으로 유지한다.
- `reference`는 재사용 가능한 topic context를, `BRIEF`는 현재 reopen state를, `logs`는 append-only execution trail을 맡는다.
- 읽기 전용 질문, 리뷰, 단발 inspection은 bootstrap이나 task 생성을 기본값으로 삼지 않는다.
- task 재사용은 label 유사성보다 "정말 같은 미완료 작업선과 같은 기대 산출물인가"를 기준으로 본다.
- `BRIEF.md`는 current state를 다시 여는 문서이지, append history나 reusable domain doc이 되어서는 안 된다.
- long-running task 문제도 코어 required tree를 늘려 해결하지 않는다. 먼저 root current docs, 임시 working notes, finished remnants의 혼합을 줄이는 쪽을 우선한다.
- helper lane 예시는 `working/`과 `archive/` 정도면 충분하다. 이 역시 repo-local aid일 뿐이며, core contract나 required tree는 아니다.

## Spec Shape Direction
- shipped spec은 `Purpose`, `Use / Do Not Use`, `Core Bias`, `Contract`, `Operating Model`, `Anti-Patterns`, `Guardrail`, `Final Gates`처럼 역할이 분리된 구성을 우선한다.
- 이유는 사용 트리거, 보장 범위, 실제 동작, 금지 패턴, 종료 점검을 섞지 않아야 문구와 drift가 함께 줄기 때문이다.
- `project-context`는 task tracking이 목적이므로 `Scope`, `Working Boundary`, `Latest Validation` 같은 운영 heading은 계속 허용한다.
- heading vocabulary는 한 표현에 과하게 묶지 않는다. `Goal/Intent`, `Current Understanding/Current Facts`, `Next Step/Next Actions` 같은 좁은 범위의 동의어는 허용 가능하다.

## Guardrail Direction
- guardrail은 semantic reviewer가 아니라 runtime drift detector다. 따라서 required path/file 존재, latest log block shape, path marker, secret-like marker, reachability 같은 현재 사실만 본다.
- scope discipline, merge correctness, 의미 품질, 전체 history coherence까지 보증하지 않는다.
- guardrail이 얇을수록 문구도 얇아야 한다. thin check를 validator처럼 설명하지 않는다.
- gardening check 역시 같은 계열이다. core contract를 판정하는 것이 아니라 long-running drift와 legacy respawn을 warning-grade로 드러내는 보조 루프에 머문다.

## Evolution Direction
- 진화의 우선순위는 context load를 낮추고 reopen reliability를 높이는 데 있다.
- 새 surface를 추가할 때는 "코어 contract가 모자란가"보다 "기존 역할 분리가 흐려졌는가"를 먼저 묻는다.
- 반복해서 재현되는 drift만 테스트, fixture, shipped guidance로 승급한다.
- repo 로컬 overlay나 companion guidance는 허용되지만, 코어 contract를 복제하거나 다시 정의하기 시작하면 drift로 본다.
- live task 예시는 current shipped contract를 따라야 하며, 비교용 snapshot은 근거로만 남긴다.
