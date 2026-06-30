# tighten-docs 규칙 확장 방지 추가

## 핵심

- 사용자 지적/요청: 국소 수정을 여러 문서 정책으로 넓히지 말라는 방지 규칙가 필요했다.
- 에이전트 조치: 범위와 중복을 검토한 뒤 스킬 경계 안에 최소 규칙만 추가하고 설치본을 맞췄다.
- 드러난 문제: 국소 수정 요청을 전역 정책으로 키우면 문서가 실제 correction보다 커진다.

## 식별

- 저장소: `tighten-docs`
- 작업: tighten-docs 규칙 확장 방지
- 대략 날짜: 2026-06-24

## 확인한 사실

- 추가된 방지 규칙는 이미 선택된 대상 편집 경계 안에 머무르도록 작성됐다.
- README/direction/prompts에 같은 말을 반복하지 않는 것으로 정리됐다.
- 설치본 동기화는 `rsync -a --delete ...`와 `diff -qr` 경로가 신뢰 경로로 기록됐다.

## 관련 문서

- `SKILL.md`
- `SKILL.ko.md`
- 설치본

## 증거

- `MEMORY.md:341-349`
- `MEMORY.md:356-368`
- `MEMORY.md:375-376`
- `rollout_summaries/2026-06-24T05-13-40-Ktgf-tighten_docs_policy_sprawl_guard_and_push.md`
- rollout id `019ef80c-5bb8-78c2-85f5-097026882aa3`

## 불확실한 점

- 이번 조사에서는 `SKILL.ko.md`의 실제 최종 문구를 직접 열지 않았다.
