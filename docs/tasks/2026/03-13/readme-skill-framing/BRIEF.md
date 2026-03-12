# README Skill Framing

- owner: ai
- started_at: 2026-03-13
- status: done

## 목적
- README와 shipped skill intro의 framing을 맞춰, `project-context`를 세션 복구 도구에만 묶지 않고 작업 맥락을 저장소 안의 평범한 파일로 남기는 스킬로 더 분명하게 설명한다.

## 실행 범위
- `README.md`, `README.en.md`, `docs/skill-direction.md`의 소개 문구를 정리한다.
- `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`의 frontmatter와 intro가 같은 방향을 가리키도록 다듬는다.
- 관련 테스트가 문구 변경으로 깨지지 않는지 확인한다.

## 현재 산출물 스냅샷
- README는 작업 맥락을 repo 안에 남겨 다음 세션이 일을 잇기 쉽게 만든다는 메시지를 앞에 둔다.
- README는 저장소 안의 평범한 파일, 단순한 구조, 사람도 읽고 고치기 쉬운 점을 장점으로 짧게 드러낸다.
- shipped skill은 contract 본문은 유지하고 frontmatter와 intro만 새 framing에 맞춘다.
- shipped skill 관련 fixture test는 상대 경로를 POSIX 형태로 정규화해 Windows에서도 같은 기대값으로 검증한다.
- 전체 unittest는 `py -3`로 실행해 통과한다.
