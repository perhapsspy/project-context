# Brief Heading Minimum

## Goal
- `BRIEF.md` 기본 skeleton을 더 작게 잡고, `Related Docs`, `Working Boundary`, `Latest Validation`를 default heading이 아니라 필요할 때만 추가하는 운영 heading으로 다시 안내한다.

## Scope
- shipped `project-context` guidance
- `project-context-migration` validation wording
- `README.md`
- `README.en.md`
- `docs/skill-direction.md`

## Current Understanding
- 현재 shipped guidance는 이 heading들을 common heading 예시로만 두지만, 문장 흐름상 기본 skeleton처럼 읽히기 쉽다.
- `Related Docs`와 `Working Boundary`는 실제 reopen cost를 낮추지 못하는데도 문서 길이만 늘리는 경우가 잦다.
- `Latest Validation`은 현재 신뢰 경계나 다음 세션의 판단을 바꿀 때만 의미가 있다.
- README는 구조와 도입 판단을 설명하는 수준에 머물고, 상세 운영 guidance는 shipped skill에 남기는 편이 역할 경계가 더 선명하다.

## Current State
- status는 completed다.
- shipped `project-context` guidance는 `BRIEF.md` 기본 skeleton을 `Goal`, `Scope`, `Current Understanding` 또는 `Current Facts`, `Current State`, `Next Step` 중심으로 다시 설명한다.
- `Related Docs`, `Working Boundary`, `Latest Validation`는 계속 허용되지만 default heading이 아니라 reopen cost를 실제로 낮출 때만 쓰는 운영 heading으로 정리됐다.
- `project-context-migration`와 `docs/skill-direction.md`는 같은 기준으로 맞췄고, README들은 스킬 내용을 다시 설명하지 않도록 skeleton guidance를 제거했다.

## Next Step
- 없음

## Latest Validation
- `python3 skills/project-context/scripts/check_runtime_shape.py`
- `python3 -m unittest discover -s tests -p 'test_*.py'`
