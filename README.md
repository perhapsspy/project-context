# Project-context

[한국어](README.md) | [English](README.en.md)

`project-context`는 코딩 에이전트가 작업 맥락을 프로젝트 안에 계속 남기게 해 세션이 바뀐 뒤에도 다시 맥락을 잡고 일을 이어가기 쉽게 만드는 스킬입니다. 필요한 최소한의 참고 문서와 작업 기록을 파일로 남기기 때문에 별도 시스템 없이 사람도 바로 읽고 고치기 쉽습니다.

- `docs/reference/`: task를 넘어 반복 참조될 주제별 도메인 맥락
- `docs/tasks/...`: 대부분의 실제 작업이 남는 날짜별 task 기록. 각 task는 `BRIEF.md`를 current overview entrypoint로 두고, append-only logs와 task-specific docs를 필요할 때만 붙임

선택 스킬인 `project-context-migration`은 이미 문서가 흩어져 있거나 일부만 이 구조로 옮겨진 저장소를 처음 정리하며 도입할 때만 사용합니다.

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

운영 습관으로, task logs를 갱신할 때는 bundled `skills/project-context/scripts/task_logs.py`로 append/check 하고 `logs/*.md`를 직접 patch하는 흐름은 기본값으로 두지 않는다.

## 프롬프트 예시

- AGENTS.md에 넣어둔 뒤 일반 작업: `로그인 리다이렉트 버그를 수정해줘`
- 직접 언급하며 작업할 경우: `$project-context 를 사용해서 로그인 페이지 구현을 진행해줘`
- 특정 task를 이어 할 때: `docs/tasks/2026/03-11/login 작업을 이어서해줘`
- 기존 문서 구조 이관: `$project-context-migration 을 사용해서 기존 문서나 맥락을 $project-context 로 옮겨줘`

## 함께 쓰기 좋은 스킬

- [`project-context`](https://github.com/perhapsspy/project-context): 작업 맥락을 저장소 안에 남겨 다음 세션에도 이어가기 쉽게 정리
- [`structure-first`](https://github.com/perhapsspy/structure-first): 코드의 성공 흐름을 먼저 읽히게 정리

## 지원

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/perhapsspy)

## 라이센스

[MIT](LICENSE)
