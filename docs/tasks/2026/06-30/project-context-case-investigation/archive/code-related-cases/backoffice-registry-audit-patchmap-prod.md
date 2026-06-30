# registry-audit PatchMap 장애와 `main`/운영 반영 정정

## 핵심

- 사용자 지적/요청: `main`에 푸시해 달라는 요청과 다르게 임시 브랜치에 푸시한 점이 지적됐다.
- 에이전트 조치: 별도 worktree에서 PatchMap 장애를 고친 뒤 `main` 푸시와 GitHub Actions 운영 배포로 정정했다.
- 드러난 문제: 저장소 배포 관례를 확인하지 않으면 코드 수정이 맞아도 전달 경로가 틀어진다.

## 식별

- 저장소: `backoffice`
- 작업: registry-audit PatchMap 운영 반영
- 대략 날짜: 2026-06-15

## 확인한 사실

- 성공 기준은 감사 요약이 아니라 브라우저에서 PatchMap `drawn`, 오류 overlay 없음, console 오류 없음이었다.
- 운영 배포는 `main` 빌드 완료 후 수동 운영 워크플로를 실행하는 순서로 기록됐다.

## 관련 문서

- `.github/workflows/deploy-to-prod-manual.yaml`
- GitHub Actions `build and push`
- GitHub Actions `Deploy to Prod (Manual)`

## 증거

- `MEMORY.md:1373-1411`
- `rollout_summaries/2026-06-15T11-40-25-nskq-backoffice_registry_audit_patchmap_fix_and_prod_deploy.md`
- rollout id `019ecb15-37cb-7ff1-8179-def89c3950ba`

## 불확실한 점

- 실제 Actions run의 현재 보존 상태나 로그 원문은 이번 조사에서 열지 않았다.
