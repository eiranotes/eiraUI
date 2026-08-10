---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-INK"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Ink"
category: "productized_main"
---

# Project Ink — `Ink`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Ink |
| Type | iOS 문장 보관·재노출 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 제품화된 main, 2탭·StoreKit·Widget/Live Activity/알림 구현 |
| Return cadence | 하루 1~4회의 조용한 재노출 |
| Monetization | 무료 기본 + 비소모성 Lifetime Pro |

## Product role

사용자가 직접 고른 문장을 저장하고 Today, 알림, Widget, Live Activity에서 다시 만나게 하는 로컬 문장 플레이어다.

## Core loop

```text
한 문장 저장/가져오기 → Today 즉시 확인 → 일정에 따라 다시 노출 → 읽기·다음 문장·고정 → Library에서 정리 → 다시 노출
```

## Closed implementation

- Today/문장 2탭과 잉크 표식의 시각 체계
- SwiftData 카드·폴더·규칙, 대량 가져오기·중복 처리·백업
- 알림·Widget·Live Activity의 역할 분리와 실패 표시
- 무료/Pro 빈도 경계와 StoreKit 2 entitlement

## Main bottleneck

기능은 충분하다. 남은 핵심은 첫 저장 후 며칠 안에 ‘다시 만나는 경험’이 실제로 발생하고 사용자가 그 차이를 이해하는지다. 시스템 표면은 앱이 잠금화면에 영구 상주하는 것처럼 보일 수 없으므로, 온보딩·카피·빈도 설정이 제품 약속과 정확히 맞아야 한다. 외부 StoreKit/App Store lifecycle도 아직 분리된 게이트다.

## Next bounded action

시각 변형을 더 추가하지 말고 ‘첫 문장 저장→첫 재노출→두 번째 문장 추가’ 3단계만 검증한다. 로컬 이벤트 원장으로 첫 72시간의 노출·열람·다음 문장 행동을 확인하고, Pro는 기능 묶음보다 재노출 빈도·폴더·대량 가져오기 같은 명확한 사용량 경계로 유지한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
