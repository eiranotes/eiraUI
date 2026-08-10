---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-MAIA2"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/maia2"
category: "external_reference"
---

# Maia-2 — `maia2`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/maia2 |
| Type | NeurIPS 2024 인간 착수 모델 공식 구현 |
| Category | 외부 원본·참조 |
| Current state | University of Toronto 공식 연구 코드 |

## Product role

레이팅 조건별 인간 착수 확률을 모델링하는 Maia-2 공식 구현이다.

## Reference use

`chess-maia-recap`의 인간다운 CPU·후보 확률 dependency

## Boundary

독립 사용자 제품이 아니라 모델 dependency다. 사용 commit·weight·license·real inference gate를 chess release manifest에 고정한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
