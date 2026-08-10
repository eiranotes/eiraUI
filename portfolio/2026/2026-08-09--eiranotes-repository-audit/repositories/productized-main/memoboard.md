---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-MEMOBOARD"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/memoboard"
category: "productized_main"
---

# Memoboard — `memoboard`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/memoboard |
| Type | Windows/Tauri 로컬 메모보드 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 공개 v1.0.1, Tauri build·공유 폴더 lock 구현 |
| Return cadence | 업무·개인 메모를 매일 작성·체크 |
| Monetization | MIT, 유료 모델 없음 |

## Product role

메모·간단 칸반·달력·체크리스트·검색을 한 창에서 쓰고, 선택적으로 로컬/NAS 폴더 JSON을 공유 작업함으로 사용하는 데스크톱 앱이다.

## Core loop

```text
메모 캡처 → 구역/태그 정리 → 체크리스트·달력 실행 → 검색/오늘 패널 → 공유 폴더 동기화
```

## Closed implementation

- 구역형 보드·드래그 순서·Markdown·체크리스트
- 월/주 달력·검색·태그·휴지통
- IndexedDB 개인 작업함과 파일 lock 기반 공유 작업함
- Windows Tauri build와 공개 스크린샷

## Main bottleneck

범용 메모 앱으로 보면 경쟁 기능이 많고, 현재 강점인 ‘서버 없이 NAS/동기화 폴더를 공유 보드로 사용’이 전면에 드러나지 않는다. 파일 lock은 실시간 공동편집이 아니므로 사용자가 기대하는 협업 범위를 정확히 제한해야 한다.

## Next bounded action

범용 노트 확장보다 서버 없는 소규모 팀·가정용 공유 보드로 포지셔닝하거나, 현재 상태를 안정적인 무료 도구로 유지한다. 공유 충돌·복구·설치 경험을 중심으로 문서와 첫 화면을 재구성한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
