---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-FOLIO"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Folio"
category: "productized_main"
---

# Folio — `Folio`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Folio |
| Type | iOS 4종 일일 퍼즐 앱 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | React/Capacitor 제품화 main, 2,000문제·세션·적응형 UI 구현 |
| Return cadence | 매일 4개 Daily + 난이도 Course |
| Monetization | Daily/Easy 무료, rewarded day pass + Puzzle Club 구상; provider 미연결 |

## Product role

Flow, Queens, Glow, Drift 네 퍼즐을 하나의 에디토리얼·파스텔 iOS 앱에서 Daily와 Course로 제공한다.

## Core loop

```text
오늘의 퍼즐 선택 → 플레이/힌트/undo → 완료 → 다음 퍼즐 preview → Records/Course 진행 → 다음날 Daily
```

## Closed implementation

- 네 엔진과 난이도별 500개, 유일해/유일 최단경로 검증
- versioned session·Daily identity·자정 갱신
- Today/Games/Course/Records/Menu와 적응형 UI
- 개발 mock과 production bundle capability 분리

## Main bottleneck

콘텐츠 수는 충분하지만 네 게임이 하나의 제품 습관으로 묶이는 이유와 실제 난이도 체감은 자동 solver만으로 확인되지 않는다. RevenueCat/AdMob 계정·동의·상품이 없으며, 물리 기기 VoiceOver·Dynamic Type·safe area도 남아 있다.

## Next bounded action

새 게임을 추가하지 말고 Daily 4종 완료율·게임별 이탈 위치·다음 퍼즐 전환을 확인한다. 사람 기준 난이도 calibration과 physical-device 접근성 뒤에 rewarded/Club provider를 연결한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
