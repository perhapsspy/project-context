# project-context 보강 검토 제안

## 판단할 문제

사용자 정정과 삭제 요청이 들어왔을 때 `BRIEF.md`가 현재 상태만 담도록 충분히 안내하고 있는지 검토한다.

이미 있는 규칙은 강하다. `BRIEF.md`는 보고서나 로그가 아니며, 현재 사실·경계·다음 단계만 담아야 한다. 다만 반복 실패에서는 사용자의 정정 자체를 문서에 보존하려는 경향이 있었다.

## 후보 위치

`skills/project-context/SKILL.md`의 `BRIEF.md Ownership` 중 semantic rules 근처가 후보 위치다.

## 영문 후보

```md
- Treat user corrections and deletion requests as instructions to rewrite the owning surface, not material to preserve. In `BRIEF.md`, keep only the resulting current fact, boundary, or next step; if the correction affects restart or future interpretation, record the compact outcome in `logs/*.md`.
```

## 한국어 의미

```md
사용자 정정과 삭제 요청은 보존할 설명이 아니라 소유 문서를 다시 쓰라는 지시로 본다. `BRIEF.md`에는 결과로 남은 현재 사실, 경계, 다음 단계만 둔다. 재개나 향후 해석에 영향을 주는 정정만 `logs/*.md`에 짧게 남긴다.
```

## 보강 찬성 근거

- `BRIEF.md`가 사용자 피드백 해설장처럼 길어지는 반복 실패를 직접 겨냥한다.
- 새 규칙이 아니라 기존 `BRIEF.md`/logs 경계를 더 빨리 적용하게 하는 문구다.
- `structure-first-docs`의 문서 의미 품질과 달리, 여기서는 저장 표면의 역할을 다룬다.

## 보강 반대 근거

- 현재 스킬에도 같은 결론을 낼 수 있는 규칙이 이미 많다.
- 문구를 추가하면 `project-context` 자체가 방어문을 증식하는 표면이 될 수 있다.
- 모든 정정을 logs에 남기라는 오해가 생기면 오히려 로그가 비대해진다.

## 검토 질문

1. 후보 문구가 기존 `BRIEF.md Ownership` 규칙과 중복되지만 실질적으로 도움이 되는가?
2. “정정/삭제 요청” 입력 유형을 명시하는 것이 반복 실패를 줄일 만큼 가치가 있는가?
3. 문구가 너무 길다면 1문장으로 줄일 수 있는가?
4. 보강하지 않는다면, 기존 규칙 중 어떤 문장을 근거로 충분하다고 볼 수 있는가?

## 완료 기준

- 수정 여부 권고가 명확하다.
- 수정한다면 정확한 위치와 최종 후보 문구가 1개만 남는다.
- 수정하지 않는다면 보류 이유가 기존 스킬 문장 근거와 함께 제시된다.
