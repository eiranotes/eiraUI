---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-LOCUS"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Locus"
category: "productized_main"
---

# Reality Diorama / Locus — `Locus`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Locus |
| Type | Flutter 현실 수집·디오라마 크래프팅 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | iOS/Android MVP main, 양 플랫폼 CI와 로컬 도메인 구현 |
| Return cadence | 날씨 cooldown·걸음 축적·제작 완료에 맞춘 일일 반복 |
| Monetization | 현재 광고·구독·재료 판매 없음 |

## Product role

현재 날씨와 선택적 주변 신호를 재료로 받고 최근 걸음을 작업량으로 써서 미니어처 오브젝트를 제작·배치하고 방문자를 발견하는 로컬 게임이다.

## Core loop

```text
날씨/주변 캡처 → 재료 획득 → 걸음 작업량 소비 → 제작 → 5×5 배치 → 방문자·레시피 발견 → 다음 캡처
```

## Closed implementation

- SQLite 거래, cooldown·걸음 FIFO·제작·배치·방문자 규칙
- WeatherKit/Open-Meteo 분리와 실패 시 가짜 재료 금지
- foreground BLE의 집계 특징만 보존하는 프라이버시 경계
- 결정론적 isometric renderer와 iOS/Android build gate

## Main bottleneck

코어 시스템보다 아트와 콘텐츠 밀도가 병목이다. 현재 5×5 placeholder 디오라마에서 수집 결과가 충분히 예쁘고 공유할 만하지 않으면 weather/steps 입력이 반복 동기로 전환되지 않는다. 캡처·걸음·cooldown이 많아도 레시피와 방문자 변주가 적으면 며칠 안에 상태가 반복된다.

## Next bounded action

시스템 확장보다 동일 광원·2:1 grid의 완성 에셋 한 세트와 7일 분량 레시피/방문자 곡선을 먼저 만든다. 실제 7일 플레이에서 캡처→제작 대기→배치→방문자 보상이 매일 다른 장면을 만드는지 확인한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
