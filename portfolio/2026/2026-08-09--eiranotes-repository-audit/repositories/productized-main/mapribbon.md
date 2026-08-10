---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-MAPRIBBON"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Mapribbon"
category: "productized_main"
---

# MapRibbon — `Mapribbon`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Mapribbon |
| Type | iOS 사진 메타데이터 여행 포토보드 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | MVP main, 열린 PR에서 Survey Plate 시각 체계와 pinboard 개선 |
| Return cadence | 여행·외출 후 사진 묶음마다 반복하는 episodic 사용 |
| Monetization | 비소모성 Lifetime 골격 |

## Product role

사진의 날짜·위치를 자동 클러스터링해 하루 여행 지도와 대표 사진을 조합한 포토보드를 만들고 공유하는 앱이다.

## Core loop

```text
사진 접근 → 여행 날짜 탐색 → 자동 장소 클러스터/대표 사진 → 템플릿 편집 → 이미지 공유 → Atlas/Archive 재방문
```

## Closed implementation

- 사진 권한·위치 클러스터링·역지오코딩·MapKit snapshot
- 여러 포토보드 템플릿과 장소/사진 편집
- 4:5·9:16 등 공유 출력과 SwiftData archive
- 한국 지역 Memory Atlas와 Lifetime 경계

## Main bottleneck

이 제품은 일일 리텐션보다 첫 결과물의 공유 품질이 중요하다. 자동 대표 사진·장소명·클러스터가 한 번만 틀려도 수동 편집 부담이 커진다. Photos 제한 권한, iCloud 원본, 실제 사진 메타데이터는 Simulator로 충분히 검증할 수 없다. Haruseon과 겹치므로 ‘사진으로 여행판을 만든다’는 경계를 유지해야 한다.

## Next bounded action

Haruseon의 이동 기록 기능을 흡수하지 말고 사진 기반 보드 생성에 집중한다. 실제 여행 20세트로 자동 결과를 평가하고, 첫 화면에서 날짜 선택부터 공유 가능한 4:5 결과까지 1분 내 완료되는 경로를 기준으로 템플릿을 줄인다.

## Open feature PRs

- [#12 앱 셸 비주얼 아이덴티티 개편: 측량 도판 디자인 및 아틀라스 개선](https://github.com/eiranotes/Mapribbon/pull/12) — open; 현행 UI·Atlas·저장 개선

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
