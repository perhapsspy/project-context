# 스킬 방향

## Purpose
- 이 문서는 shipped `project-context` contract를 어떤 방향으로 유지하고 진화시킬지에 대한 로컬 기준이다.

## What To Preserve
- 저장소 안의 파일을 우선한다.
- 코어 계약은 작게 유지한다.
- 사람도 바로 읽고 고칠 수 있는 구조를 우선한다.
- `reference`는 provenance보다 현재 믿고 쓸 기준 맥락을 우선한다.

## What To Avoid
- 숨은 메모리나 외부 시스템을 계약처럼 만들지 않는다.
- 새 surface를 코어처럼 키우지 않는다.
- 증명되지 않은 범위를 이름과 설명에 싣지 않는다.
- `reference`를 조사 메모나 진행 로그처럼 쓰지 않는다.

## When To Revise
- 같은 drift가 반복될 때만 shipped contract를 바꾼다.
