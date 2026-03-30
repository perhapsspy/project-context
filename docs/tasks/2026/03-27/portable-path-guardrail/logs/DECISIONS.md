**2026-03-27**
- 배경: 절대경로나 사용자 환경 경로가 문서에 남는 드리프트가 반복되는데, 현재 skill contract와 thin checker는 이를 직접 막지 않는다.
- 선택지: 1) wording만 추가한다. 2) wording과 migration rule, thin path-marker scan을 함께 둔다.
- 결정: portable path 규칙을 shipped skill과 migration skill에 넣고, checker는 repo-root 절대경로와 대표적 환경 경로 marker를 얇게 스캔한다.
- 영향: future repos는 문서 작성 시 repo-relative/placeholder로 수렴하고, 로컬 환경 경로 drift를 runtime shape 단계에서 빨리 잡을 수 있다.
