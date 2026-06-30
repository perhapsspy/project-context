# perhapsspy 스킬 호출 조건과 설치 차이 조사

## 핵심

- 사용자 지적/요청: 오래된 스킬들의 호출 조건과 실제 설치 가능 상태를 확인할 필요가 있었다.
- 에이전트 조치: 스킬 설명과 설치본, lock 파일을 비교하고 `work-board` 설치 차이를 기록했다.
- 드러난 문제: 저장소 문구를 고쳐도 설치본이 없으면 실제 자동 선택은 일어나지 않는다.

## 식별

- 저장소: `playground` 및 형제 스킬 저장소
- 작업: 스킬 호출 조건 감사
- 대략 날짜: 2026-06-23

## 확인한 사실

- Codex 스킬 매칭은 `name`, `description`, path에서 시작하고 전체 `SKILL.md`는 선택 후 읽힌다고 정리됐다.
- `work-board`는 저장소 문구는 개선됐지만 전역 설치본이 없어 자동 선택될 수 없는 차이 사례로 기록됐다.
- 여러 다른 스킬들은 설치본과 저장소 사본이 일치했다.

## 관련 문서

- 저장소 스킬 설명
- `$AGENTS_HOME/skills` 아래 설치본
- `.skill-lock.json`

## 증거

- `MEMORY.md:378-408`
- `rollout_summaries/2026-06-23T00-28-50-xtLD-perhapsspy_skill_trigger_audit_and_install_sync.md`
- rollout id `019ef1e1-3d08-7ae0-9334-20bf2495fb85`

## 불확실한 점

- 감사 결과가 부분 완료로 표시되어 있고, 모든 perhapsspy 스킬 저장소가 끝까지 검사됐는지는 확정할 수 없다.
