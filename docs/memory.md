# 현재 메모리: project-context

- 업데이트 시각: 2026-03-11T00:00:00Z
- 업데이트 주체: ai

## 현재 초점
- `docs/` 루트 구조로 정리된 memory contract를 실제 사용 흐름에서 계속 검증한다.

## 활성 결정
- 메모리 기록은 현재 사용자 주 언어로 작성한다.
- 정본 메모리 파일은 `docs/memory.md` 하나이며, 업데이트 시 전체를 rewrite한다.
- `docs/memory.md`는 active invariant, 현재 phase, 임시 전역 제약, 현재 유효한 cross-task 조건을 담는 짧은 전역 작업 메모리로 유지한다.
- reference 파일 경로는 `docs/reference/**/*.md`를 사용하고 각 path segment는 kebab-case로 유지한다.
- repo-local reference 문서는 task와 구별되는 durable project-domain context만 담고, 운영 guidance나 dogfood 안내서는 두지 않는다.
- `docs/reference/`는 도메인 콘텍스트 정리 자체가 작업 목표일 때나 반복 참조될 도메인 콘텍스트가 이미 분명할 때 직접 작성할 수 있고, `MEMORY-CANDIDATES.md`는 task에서 나온 `docs/memory.md` 후보를 현재 후보판으로 관리할 때만 사용한다.
- task는 `docs/tasks/yyyy/mm-dd/<slug>/` 단위로 관리하고, `BRIEF.md`와 `STATUS.md`는 rewrite-only snapshot으로 유지한다. `STATUS.md`는 보통 제목 줄 없이 바로 현재 상태를 적는다.
- 읽기 전용 질문, 리뷰, 단발 inspection은 durable update가 필요할 때만 bootstrap이나 task 생성을 하고, 아니면 read-only로 끝낸다.
- append-only 기록은 `logs/DECISIONS.md`, `logs/WORKLOG.md`에만 남긴다.
- 새 로그 엔트리는 `**YYYY-MM-DD**` 날짜 블록 아래에 append하고, `logs/DECISIONS.md`는 최신 블록에서 배경, 선택지, 결정, 영향을 담는 짧은 결정 기록 4항목을 유지하며 `logs/WORKLOG.md`는 최신 블록에 실행 근거 bullet을 최소 1개 둔다.
- memory 후보는 있을 때만 각 task의 `MEMORY-CANDIDATES.md`에서 관리하고, `MEMORY-CANDIDATES.md`는 제목이나 설명 없이 plain `- <STATE> | <summary> | <evidence-pointer>` entry만 담는다. `MEMORY-CANDIDATES.md`를 통한 반영은 `APPLIED`만 허용하고, `docs/reference/`는 도메인 콘텍스트 정리 작업에서 직접 작성할 수 있다.
- `MEMORY-CANDIDATES.md` summary는 target-ready declarative text로 80-100 chars를 권장하고 120-char hard cap을 둔다.
- `MEMORY-CANDIDATES.md` evidence-pointer는 정확히 1개의 log pointer(`logs/DECISIONS.md@L...` 또는 `logs/WORKLOG.md@L...`)만 사용하고 32-char hard cap을 둔다.
- `MEMORY-CANDIDATES.md`는 현재 후보판이지 archive가 아니므로, unresolved candidate가 없어지면 파일을 지우거나 생략한다.
- 같은 task가 `docs/memory.md`와 `docs/reference/`를 함께 갱신할 수는 있지만, `MEMORY-CANDIDATES.md`는 압축된 전역 작업 메모리 후보만 담고 상세 내용은 `docs/reference/`에 직접 둔다.
- task 생성과 승급 적용은 helper 전용 템플릿 없이 파일 계약을 직접 따른다.
- 서브에이전트는 부모 문맥을 물려받지 않은 fresh context로 시작하고, goal/constraints/declared read scope/declared write scope/validation command/artifact path만 담은 작은 task brief를 사용한다.
- 머지 전에는 결과가 declared read scope 안에서만 조사됐는지 확인한다.
- 조회는 패스당 reference 최대 3개와 task 최대 1개만 여는 working read budget을 둔다.
- 참조 조회는 인덱스 없이 `docs/reference/**/*.md`를 `rg`로 검색한다.

## 다음 작업
- 다른 실제 코딩 작업 1건에 같은 루프를 재적용해 drift를 확인한다.

## 참조 포인터
- docs/reference/model/context-surfaces.md
