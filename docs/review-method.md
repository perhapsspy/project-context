# 리뷰 방법

## 목적
- 이 문서는 `project-context` 레포에서 shipped skill, migration skill, README, checker, 로컬 방향 문서를 리뷰할 때 쓰는 로컬 기준을 정리한다.
- 목표는 좋은 문장보다 contract와 evidence 수준의 적합성을 판정하는 것이다.

## 기본 원칙
- 리뷰는 문장 취향보다 contract correctness를 우선한다.
- findings는 "시작을 막는가", "기대를 잘못 심는가", "역할 경계를 흐리는가", "guardrail보다 더 강한 보증을 암시하는가"를 중심으로 올린다.
- 좋아 보이지만 아직 증명되지 않은 확장은 보류 쪽으로 판정한다.
- shipped asset과 repo-local asset은 같은 기준으로 읽되, 기대 역할은 다르게 본다.

## 용어 구분
- `문제`: 실제 수정이 필요하거나 checker/test가 이미 잡는 상태.
- `follow-up`: 지금 막지는 않지만 다음 dogfood나 변경에서 다시 볼 항목.
- `trade-off`: 우선순위나 운영 방식에 따라 고르는 선택.
- `observation`: 판단 보류가 필요한 단순 사실이나 경향.
- 특별한 근거가 없으면 `리스크`라는 말은 쓰지 않는다.

## 리뷰 기준

### 1. 역할 적합성
- 본다: 이 파일이 자기 역할만 하고 있는가.
- shipped `SKILL.md`는 실행 규칙, `docs/skill-direction.md`는 why와 direction, README는 activation surface, checker는 얇은 runtime 사실을 맡는다.
- `reference`는 task provenance 설명 없이도 현재 믿고 쓸 기준 맥락으로 읽혀야 하고, 조사 경과나 진행 이력이 본문 역할을 차지하면 과하다.

### 2. 주장 강도 일치
- 본다: 문구의 보장 강도가 실제 evidence와 맞는가.
- 질문: 이 문장이 실제 테스트나 checker가 증명하는 수준보다 앞서 가는가. help text와 frontmatter가 실제 범위보다 넓은가.

### 3. surface 절제
- 본다: 새 surface나 새 용어를 정말 늘려야 하는가.
- 질문: 이 변화는 기존 surface 역할을 선명하게 만드는가, 아니면 새 surface를 기본값으로 밀어 넣는가. optional pattern이 required tree처럼 읽히지 않는가.

### 4. 재개 가능성
- 본다: 나중 세션이 cold start 없이 다시 열 수 있는가.
- 질문: `BRIEF`, `reference`, `logs`의 역할이 섞이지 않았는가. `Scope`가 touched-file inventory로 불어나지 않았는가. long-running guidance가 root 혼합을 줄이는 방향으로 쓰였는가.

### 5. drift 저항성
- 본다: 변경이 legacy respawn, root mixing, misleading overlays를 줄이는가.
- 질문: 이 guidance가 legacy surface를 다시 살리는가. checker warning과 문서 guidance가 서로 다른 vocabulary를 쓰지 않는가.

### 6. 자산 간 정렬
- 본다: shipped skill, migration skill, local direction, tests, examples가 서로 어긋나지 않는가.
- 최소 확인 대상: `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/skill-direction.md`, 관련 tests / fixtures, 필요 시 README와 live task example

## 리뷰 절차
1. 먼저 대상 파일의 역할을 정한다.
2. 위 6개 기준으로 읽고, blocking issue가 있으면 findings로 먼저 적는다.
3. findings가 없으면 "현재 수준은 적합"이라고 말하되, 남는 항목은 `follow-up`, `trade-off`, `observation` 중 하나로 적는다.
4. wording 의견은 findings 뒤로 미룬다.
5. 리뷰 중 나온 좋은 기준이 반복적으로 유효하면 이 문서나 `AGENTS.md`에 승급한다.

## 현재 레포에 특히 중요한 판정선
- README는 시작을 막는 문제만 강하게 본다.
- `docs/skill-direction.md`는 진행 기록보다 기준 맥락과 이유를 우선한다.
- `reference`는 최근 믿을 수 있는 현재 truth를 담을 수 있지만, 사건 조사나 진행 상태를 본문으로 끌어오면 안 된다.
- long-running task guidance는 core required tree가 아니라 optional advanced guidance로 읽혀야 한다.
- repo-local helper lane 이름(`working/` 등)을 shipped contract처럼 고정해 읽히면 과하다.
- gardening checker는 warning-grade drift detector로 남아야 한다.
