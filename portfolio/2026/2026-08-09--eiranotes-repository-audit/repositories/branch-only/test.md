---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-TEST"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Test"
category: "branch_only"
---

# Test / 제품 인큐베이터 — `Test`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Test |
| Type | 서로 다른 iOS 제품 후보 2개 |
| Category | branch·PR 전용 제품 후보 |
| Current state | main 제품 없음, FairSpan·MiterRun PR이 병렬 존재 |
| Return cadence | 제품별 상이 |
| Monetization | 미정 |

## Product role

하나의 저장소에 공과금 거주기간 안분 앱 FairSpan과 절단 최적화 앱 MiterRun이 별도 PR로 공존한다.

## Core loop

```text
FairSpan: 청구기간·거주자·금액 입력→투명한 안분→공유. MiterRun: 자재·cut list 입력→최적 배치→작업 체크→offcut 재사용.
```

## Main bottleneck

두 제품은 사용자·도메인·데이터 모델·ASO가 완전히 달라 같은 저장소의 브랜치 후보로 유지할 이유가 없다. FairSpan은 한 번 계산하는 episodic utility이고, MiterRun은 작업·자재 이력이 반복되는 professional workflow다.

## Next bounded action

추가 구현 전에 각각 독립 저장소와 이름을 부여한다. FairSpan은 입력 마찰·계산 설명·공유 결과를 검증하고, MiterRun은 실제 작업장에서 cut plan 정확도·offcut 재사용·장갑 낀 조작을 검증한다.

## Open feature PRs

- [#1 feat: ship FairSpan production-ready iOS app](https://github.com/eiranotes/Test/pull/1) — open / draft; 공과금 안분 앱
- [#2 feat: ship MiterRun production-ready iOS app](https://github.com/eiranotes/Test/pull/2) — open / draft; 절단 최적화 앱

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
