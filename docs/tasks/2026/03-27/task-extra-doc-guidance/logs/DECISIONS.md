**2026-03-27**
- 배경: shipped `project-context`가 task 기본 골격은 잘 설명하지만 `BRIEF.md`/`STATUS.md`만으로 부족한 작업에서 추가 task-local 문서를 어떻게 다뤄도 되는지는 거의 말하지 않았다.
- 선택지: 예시 파일명과 umbrella term까지 강하게 적거나, 허용 규칙만 짧게 추가하거나, 기존 상태를 유지하는 방법이 있었다.
- 결정: 기본 skill에는 새 네이밍 없이 허용 규칙과 중복 금지 원칙만 짧게 추가하고, migration/local docs/test는 그 방향과만 맞춘다.
- 영향: 설계성 작업에서 추가 문서를 자연스럽게 둘 수 있다는 점이 드러나면서도 core contract와 guardrail 범위는 그대로 유지된다.
