# 스킬 방향

## 핵심
- `project-context`에서 에이전트가 실제로 따라야 할 계약은 shipped `SKILL.md`가 맡는다.
- 이 문서는 레포를 만들고 다듬을 때 참고하는 로컬 방향만 다룬다.
- `project-context`의 목표는 코딩 에이전트가 작업 맥락을 프로젝트 안의 평범한 파일로 남겨, 다음 세션도 다시 일을 잇기 쉽게 만드는 데 있다.
- 스킬은 작고, 절차적이고, 언어에 덜 묶인 형태를 우선한다.
- 같은 행동이라면 레포 고유 표현보다 더 안정적인 개념을 먼저 고른다.
- 문서 경로 표기는 repo-relative나 `<repo-root>`, `<task-root>`, `$CODEX_HOME` 같은 project-owned placeholder를 우선한다.

## 경계
- 스킬에는 에이전트가 바로 실행해야 하는 행동만 둔다.
- 테스트, dogfood 산출물, 설계 메모는 레포 로컬 지원 자산으로 본다.
- 스크립트는 설치된 skill에서 에이전트가 skill-relative로 실행하거나, 이 레포 유지보수자가 직접 점검할 수 있을 때만 스킬 아래에 둔다.
- 외부 시스템이나 전용 저장소보다 현재 저장소 안의 평범한 파일로 남기는 쪽을 우선한다.
- 읽기 전용 질문, 리뷰, 단발 inspection은 bootstrap이나 task 생성을 기본값으로 삼지 않는다.
- live task 예시는 current shipped contract를 따라야 하고, 중간 단계의 낡은 예시는 오래 남겨 둘 이유가 약하면 지우는 쪽을 우선한다.
- 기존 task 재사용은 literal label 일치보다 "정말 같은 미완료 작업선인가"를 먼저 본다.
- `docs/reference/`, `docs/tasks/...` surface는 유지하되, file shape나 boundary note 같은 세부 운영 규칙은 shipped skill이 맡는다.

## 톤
- 이름, 요약, help text는 실제로 증명된 범위 중 가장 좁은 범위를 기준으로 잡는다.
- README 같은 로컬 문서에서는 유용성을 설명할 수 있지만, shipped `SKILL.md`의 frontmatter와 help text는 좁고 검증 가능한 표현을 유지한다.
- 같은 역할이면 더 짧은 문장을 택하고, 새 정보가 없으면 다른 말로 반복하지 않는다.
- 설명을 늘리기보다 경계를 남긴다.
- shipped guardrail이 shape, reachability 같은 얇은 runtime 사실만 볼 때는 과한 권위나 보증 표현을 피한다.
- 에이전트 전용 표현보다 사람이 바로 읽고 고칠 수 있는 단순한 말과 구조를 선호한다.
- 문서 이름도 역할을 과장하지 않게 고른다. guidance를 contract처럼, thin check를 validator처럼 부르지 않는다.

## 가드레일
- 가드레일은 현재 runtime shape의 drift를 빨리 잡기 위해 존재한다.
- 경로, 파일 존재, 형식, 최신 로그 블록 shape, evidence-pointer reachability, path marker, secret-like marker 정도만 본다.
- working read budget 준수나 declared scope 준수 여부는 보지 않는다.
- 의미 품질, merge correctness, 전체 이력의 일관성, 문체까지 보증하지 않는다.

## 진화
- context load를 낮추고 cold-start 재현성을 높이는 방향을 우선한다.
- dogfood 결과는 durable domain context나 cross-task rule이 될 때만 승급한다.
- 레포 로컬 문서는 shipped skill을 보조할 수는 있어도, 새 의무나 더 강한 계약을 덧씌우면 안 된다.

## Dogfood Loop
- dogfood는 가장 작은 실제 대상부터 시작한다.
- 입력은 바뀐 surface와 그 surface를 지배하는 shipped skill/로컬 방향만 둔다.
- 문구, README, migration 같은 변화는 activation, contract drift, runtime의 세 패스로 본다.
- 결과에는 시작을 막는 문제와 drift만 남기고, 반복되는 결과만 test, fixture, 로컬 방향으로 승급한다.

## README 자체 평가 루프
- README 평가는 `activation surface` 기준으로 본다. 처음 쓰려는 사용자가 왜 써볼 만한지, 어떻게 켜는지, 필요하면 어떤 보조 스킬을 같이 볼지만 빠르게 판단할 수 있으면 1차 목적은 충족이다.
- 검토 입력은 해당 `README`, 관련 shipped `SKILL.md`, 필요하면 이 문서까지만 두고, test fixture나 dogfood 기록으로 README 책임을 과장하지 않는다.
- 평가는 fresh-context 서브에이전트 3갈래로 나눈다: 1) first-user activation read, 2) README framing accuracy vs shipped skill, 3) 과검토를 걷어내는 skepticism filter.
- 최종 피드백에는 "첫 시도 자체를 막거나, 시작 시점 기대를 명확히 잘못 심는 지점"만 남긴다. 복구 가능한 선택 실수, 나중에 로컬 상태를 보면 바로 드러나는 차이, contract 전문 부재만으로는 결함으로 올리지 않는다.
- exact output tree, read-only/write-bearing 세부 운영 경계, thin guardrail 전체 설명은 README의 필수 책임으로 보지 않는다. 그런 정보는 shipped `SKILL.md`나 실제 사용 흐름으로 넘겨도 된다.
- 출력은 세 묶음이면 충분하다: 이미 충분한 점, 정말 시작을 막는 지점 0-2개, 있으면 좋은 선택적 문구 조정.
