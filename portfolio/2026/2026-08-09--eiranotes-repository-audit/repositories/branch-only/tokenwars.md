---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-TOKENWARS"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/TokenWars"
category: "branch_only"
---

# Token Wars — `TokenWars`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/TokenWars |
| Type | 웹 요청 네트워크 전략 게임 |
| Category | branch·PR 전용 제품 후보 |
| Current state | main은 branch 안내만 존재, PR #3에 단일 화면 구현 |
| Return cadence | 한 판 단위 |
| Monetization | 미정 |

## Product role

CORE/FORK/SERVING 세 상태와 16개 모델이 요청 네트워크에서 자원을 경쟁하는 단일 화면 게임 방향이다.

## Core loop

```text
모델/노드 선택 → 요청·자원 흐름 조정 → 네트워크 압력/수익 변화 → 승패/재시작
```

## Main bottleneck

main에 제품 기준점이 없고 이전 v0.2 복잡한 전쟁 모델과 새 단순 네트워크 모델이 공존한다. 어떤 규칙이 canonical인지 정해지지 않으면 밸런스·UI·테스트가 계속 분기된다.

## Next bounded action

PR #3의 단순 모델을 canonical로 채택할지 먼저 결정하고, 채택 시 이전 실험을 `legacy/`로 이동한 뒤 5분 내 한 판이 끝나는 플레이테스트를 만든다.

## Open feature PRs

- [#3 Rebuild Token Wars around request-network forks](https://github.com/eiranotes/TokenWars/pull/3) — open; 단순 CORE/FORK/SERVING canonical 후보

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
