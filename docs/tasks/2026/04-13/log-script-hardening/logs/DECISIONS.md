**2026-04-13**
- 배경: 로그 입력 스크립트가 있어도 shipped guidance와 append failure mode 때문에 에이전트가 직접 편집으로 자주 빠진다.
- 선택지: repair 전용 명령을 추가한다. 또는 append 자체를 malformed latest block에도 더 견고하게 만들고 guidance를 강화한다.
- 결정: 이번 변경은 repair surface 추가보다 append path hardening과 scripted-write guidance 강화에 우선순위를 둔다.
- 영향: 일반 세션은 최신 블록이 일부 깨져 있어도 로그를 계속 쌓기 쉬워지고, 직접 편집은 더 예외적인 복구 상황으로 좁아진다.
