---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-HARUSEON"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Haruseon"
category: "productized_main"
---

# 하루선 — `Haruseon`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Haruseon |
| Type | iOS 로컬 이동 기록·리캡 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 제품화된 main, 시각화·시간대·프라이버시 고도화 진행 |
| Return cadence | 수동 실행 없이 매일 축적되는 일일·주간·월간 반복 |
| Monetization | 저장소에서 확정되지 않음 |

## Product role

배경 위치와 사진 근거를 이용해 하루를 ‘머문 곳→이동→머문 곳’으로 재구성하고, 동일 데이터를 픽셀 릴리프·리캡·공유 카드로 누적하는 제품이다.

## Core loop

```text
수동 설정/권한 → 백그라운드 증거 수집 → 하루 타임라인 확인 → 기록·리캡 확인 → 누적 흔적/여행 리캡 재방문 → 공유
```

## Closed implementation

- 로컬 전용 데이터 경계, 경로 단절과 불확실성의 명시, 집·회사 공유 마스킹
- 시간대·DST·04:00 기준일과 위치 증거의 일관성
- Today/여정/기록에서 공유하는 지도 타일 없는 픽셀 릴리프 렌더링
- 일일·월간·여행용 리캡으로 확장 가능한 데이터 모델

## Main bottleneck

현재 병목은 기능 누락보다 누적 시각화의 장기 가독성과 만족도다. 짧은 동네 이동부터 전국·해외 이동까지 같은 도트/릴리프 문법을 유지하면서도 행정 경계, 체류 높이, 경로 단절, 밀집 지역이 겹치지 않아야 한다. 실기기에서 배터리·백그라운드 권한·장기간 위치 데이터가 함께 검증되어야 한다.

## Next bounded action

새 화면을 늘리기 전에 픽셀 릴리프 문법을 고정하고, 실제 30일 데이터와 서울·광역·여행 fixture로 일일/주간/월간/여행 리캡을 한 번에 검증한다. 공유 결과물은 Today 지도 복제가 아니라 누적된 장소 밀도와 시간의 차이를 한눈에 보여주는 별도 출력 계약으로 유지한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
