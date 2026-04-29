# Project-context

[한국어](README.md) | [English](README.en.md)

`project-context`는 코딩 에이전트가 작업 맥락을 프로젝트 안에 계속 남기게 해 세션이 바뀐 뒤에도 다시 맥락을 잡고 일을 이어가기 쉽게 만드는 스킬입니다. 필요한 최소한의 참고 문서와 작업 기록을 파일로 남기기 때문에 별도 시스템 없이 사람도 바로 읽고 고치기 쉽습니다.

- `docs/reference/`: 현재 믿고 사용할 원칙, 규칙, 최근 믿을 수 있는 사실 같은 기준 맥락
- `docs/tasks/...`: 대부분의 실제 작업이 남는 날짜별 task 기록

## 언제 쓰나

- 새 저장소에서 장기 작업을 시작할 때: `project-context`로 바로 `docs/reference/`와 날짜별 task를 만든다.
- 기존 문서가 흩어진 저장소를 처음 정리할 때: `project-context-migration`으로 현재 문서를 분류한 뒤 필요한 것만 옮긴다.
- 읽기 전용 질문, 일회성 점검, 짧은 답변만 필요한 경우: 아무 파일도 만들지 않는다.

## 빠른 시작

**설치**

```bash
npx skills add perhapsspy/project-context
```

혹은 `skills`에서 필요한 스킬을 직접 복사하기. 기존 문서 구조를 이관할 때는 `project-context`와 `project-context-migration`을 함께 복사한다.

**AGENTS.md에 기본값으로 연결**

```md
- 작업 시 항상 $project-context 를 사용해
```

## 프롬프트 예시

- AGENTS.md에 넣어둔 뒤 일반 작업: `로그인 리다이렉트 버그를 수정해줘`
- 직접 언급하며 작업할 경우: `$project-context 를 사용해서 로그인 페이지 구현을 진행해줘`
- 특정 task를 이어 할 때: `docs/tasks/2026/03-11/login 작업을 이어서해줘`
- 기존 문서 구조 이관: `$project-context-migration 을 사용해서 기존 문서나 맥락을 $project-context 로 옮겨줘`

## 좋은 기록 모양

- `BRIEF.md`: 지금 믿을 수 있는 사실, 현재 상태, 가장 가까운 다음 행동만 담는다.
- `WORKLOG.md`: 의미 있는 작업 묶음과 검증 근거를 남긴다. 명령어별 실행 기록이 아니라 나중에 판단을 복원할 수 있는 근거를 남긴다.
- `DECISIONS.md`: 미래 해석에 영향을 주는 결정만 `Background / Decision / Why / Impact` 4개 bullet로 남긴다.

구체적인 예시는 [`docs/examples.md`](docs/examples.md)를 본다.

## 함께 쓰기 좋은 스킬

- [`project-context`](https://github.com/perhapsspy/project-context): 작업 맥락을 저장소 안에 남겨 다음 세션에도 이어가기 쉽게 정리
- [`structure-first`](https://github.com/perhapsspy/structure-first): 코드의 성공 흐름을 먼저 읽히게 정리

## 지원

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/perhapsspy)

## 라이센스

[MIT](LICENSE)
