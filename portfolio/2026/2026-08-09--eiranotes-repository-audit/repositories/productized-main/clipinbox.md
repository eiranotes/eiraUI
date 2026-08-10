---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-CLIPINBOX"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/ClipInbox"
category: "productized_main"
---

# Clip Inbox — `ClipInbox`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/ClipInbox |
| Type | iOS 공유 시트 기반 로컬 클립 보관 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 출시형 main, 1.1 grouped-photo 변경 후 전체 release closeout 재검증 필요 |
| Return cadence | 웹·사진·텍스트를 발견할 때마다 반복 |
| Monetization | 유료 앱/일회성 모델 |

## Product role

Safari·Photos·텍스트를 Share Extension에서 빠르게 저장하고 Inbox, 폴더, 태그, 검색, Sort Later로 나중에 찾는 로컬 클립 보관함이다.

## Core loop

```text
외부 앱에서 공유 → 즉시 저장 또는 검토 → Inbox → 나중에 분류/메모 → 검색·재열기 → 백업
```

## Closed implementation

- 링크·텍스트·사진 Share Extension과 crash-safe App Group 전달
- 폴더·태그·북마크·검색·휴지통·백업/복구
- 공개 주소 검증과 제한된 링크 메타데이터
- 다중 사진을 하나의 Clip 갤러리로 저장하는 schema v3

## Main bottleneck

저장 속도는 이미 강하다. 제품 병목은 ‘저장 후 다시 찾는 비율’이다. 범용 클립 앱은 저장 행위가 쌓일수록 Inbox가 부채가 되기 쉽다. grouped-photo 변경이 이전 release candidate를 무효화했으므로 전체 suite·Release·bundle·실기기 Share 검증도 다시 필요하다.

## Next bounded action

1.1 closeout을 먼저 끝내고, 기능 추가는 Sort Later 완료율·검색 재열기·폴더 이동처럼 저장 이후 행동에만 제한한다. App Store 첫 장면도 ‘무엇이든 저장’보다 ‘Safari에서 한 번 저장→나중에 분류·검색’의 두 시점을 연결해야 한다.

## Open feature PRs

- [#1 feat(release): prepare Clip Inbox 1.3](https://github.com/eiranotes/ClipInbox/pull/1) — open; 1.3 출시 패키징

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
