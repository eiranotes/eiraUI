---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-APPAUDIT"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/AppAudit"
category: "productized_main"
---

# App Audit — `AppAudit`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/AppAudit |
| Type | iOS Screen Time 의사결정·시험 제거 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 로컬 구현 완성, Family Controls·Trial은 실기기/배포 entitlement 게이트 |
| Return cadence | 7/30/90일 감사와 7/14일 Trial 후 재방문 |
| Monetization | 무료 기본 + Lifetime |

## Product role

최근 앱 사용을 검토하고 keep/postpone/Trial 결정을 남긴 뒤, 되돌릴 수 있는 Screen Time 차단을 거쳐 최종 결정을 기록하는 앱이다.

## Core loop

```text
감사 주기 도래 → Guided/Automatic 후보 검토 → 앱별 결정 → Trial 차단 → 만기 후 결과 → 기록·다음 감사
```

## Closed implementation

- Guided/조건부 Automatic 감사, 명시적 결정과 SwiftData 기록
- 단일 활성 Trial, 복구 원장, fail-open 안전 커널
- Lifetime StoreKit, 공유 receipt, 다국어·다크 모드
- 열린 PR에서 Audit/Portfolio·불변 결정 이력·Share Studio 확장

## Main bottleneck

가장 큰 병목은 UI가 아니라 Apple 플랫폼 권한이다. Simulator에서 Shield 복구·확장 콜백·재부팅·배포 entitlement를 증명할 수 없다. Guided Mode는 보호된 report 경계 때문에 사용자가 앱을 다시 선택해야 하므로 Automatic보다 마찰이 크다. 여러 열린 PR이 동시에 제품 범위를 넓혀 이 외부 게이트보다 앞서 나가고 있다.

## Next bounded action

물리 기기 Trial 복구 행렬과 배포 entitlement를 먼저 닫는다. 이후 열린 PR 중 세션 귀속·불변 결정 이력처럼 데이터 정확성을 높이는 변경을 우선하고, Portfolio/Share Studio는 실제 반복 감사 데이터가 쌓인 뒤 노출한다.

## Open feature PRs

- [#1 feat(retention): close the monthly decision loop](https://github.com/eiranotes/AppAudit/pull/1) — open; 월간 재감사 루프
- [#2 feat(audit): add signal and portfolio planning foundation](https://github.com/eiranotes/AppAudit/pull/2) — open / stacked; 분석 엔진
- [#3 feat(audit): render protected Private Audit Issue](https://github.com/eiranotes/AppAudit/pull/3) — open / stacked; 보호 report UI
- [#4 feat(audit): add Audit and Portfolio product shell](https://github.com/eiranotes/AppAudit/pull/4) — open / stacked; 제품 셸
- [#5 feat(share): add Audit Receipt Share Studio](https://github.com/eiranotes/AppAudit/pull/5) — open / stacked; 공유 receipt
- [#6 fix(share): harden Audit-first UI and Receipt QA](https://github.com/eiranotes/AppAudit/pull/6) — open / stacked; 시각·접근성 보강
- [#7 feat(portfolio): persist immutable decision history](https://github.com/eiranotes/AppAudit/pull/7) — open; 불변 결정 이력

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
