---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-ADELIEPAGES"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/AdeliePages"
category: "productized_main"
---

# Adelie Pages — `AdeliePages`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/AdeliePages |
| Type | Flutter 디지털 문구·페이지 스튜디오 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 대규모 제품화 main, 편집기·카탈로그·다국어·Android/iOS 검증 |
| Return cadence | 새 페이지·다이어리·시즌 팩을 만들 때 반복 |
| Monetization | RevenueCat 경계는 구현, 실제 상품·sandbox 미연결 |

## Product role

Adelie Draw의 종이·스티커·장식 팩을 조합해 페이지를 만들고 PNG·Story 등으로 내보내는 Page-first 창작 앱이다.

## Core loop

```text
팩/페이지 선택 → Compose 편집 → 저장·미리보기 → PNG/Story/클립보드 공유 → Library 재편집 → 새 팩 탐색
```

## Closed implementation

- Flutter/Riverpod 기반 다중 화면과 3-band CanvasDocument
- 원자적 autosave, undo/redo, 다중 선택·그룹 변형·export
- 다국어·고대비·대형 텍스트·Android/iOS UI 검증
- 열린 PR에서 정식 stationery catalog와 에셋 팩 보강

## Main bottleneck

편집기보다 콘텐츠 공급이 병목이다. 실제 판매 가능한 종이·스티커 팩, 브랜드 승인, CDN/카탈로그 운영, Store 상품이 준비되지 않으면 기술적으로 완성된 편집기가 빈 매대로 보인다. 현재 5개 탭과 여러 진입점은 콘텐츠가 적을 때 기능 대비 복잡하게 느껴질 수 있다.

## Next bounded action

편집기 기능을 동결하고 소수의 완성도 높은 starter/paid 팩으로 출시 경로를 만든다. 팩 상세→바로 사용→완성본 공유의 전환을 우선 검증하고, News·Community 성격 기능은 실제 콘텐츠 운영이 생길 때까지 보조 계층으로 둔다.

## Open feature PRs

- [#5 feat: refresh stationery catalog and harden release readiness](https://github.com/eiranotes/AdeliePages/pull/5) — open; 최신 콘텐츠·release contract
- [#4 Add two reference-driven digital stationery packs](https://github.com/eiranotes/AdeliePages/pull/4) — open; 신규 에셋 팩

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
