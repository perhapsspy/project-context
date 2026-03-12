**2026-03-10**
- 배경: migration skill은 코드보다 분류와 순서가 핵심이라, 단순 정적 검토보다 실제 legacy repo를 옮겨 보는 dogfood가 더 적합하다.
- 선택지: 1) 문서 리뷰만 한다, 2) fixture repo를 만들고 isolated worker 둘로 병렬 migration을 실행한다.
- 결정: synthetic fixture repo 2개를 만들고, worker 서브에이전트가 각 fixture를 독립적으로 마이그레이션하도록 구성한다.
- 영향: 분류 규칙의 모호함과 과승급 위험을 실제 출력 기준으로 검증할 수 있다.

**2026-03-10**
- 배경: `case-alpha` 첫 실행은 분류 결과는 괜찮았지만, migration skill이 새 task의 정확한 파일 형식을 충분히 못 박지 않아 `MEMORY-CANDIDATES.md` 제목과 `DECISIONS.md` 섹션 헤딩이 들어갔다.
- 선택지: 1) 이 실패를 runner 실수로만 취급한다, 2) migration skill에 task 형식 계약을 한 줄로 올리고 다시 검증한다.
- 결정: migration skill에 `MEMORY-CANDIDATES.md`와 log file shape를 명시하고, 그 상태로 `case-beta`를 다시 실행해 형식 drift가 줄어드는지 본다.
- 영향: migration skill이 분류뿐 아니라 생성 산출물의 contract fidelity도 더 잘 가이드하게 된다.
