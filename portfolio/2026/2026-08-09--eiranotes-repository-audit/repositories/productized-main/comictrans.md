---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-COMICTRANS"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/ComicTrans"
category: "productized_main"
---

# 당근망가번역기 작업대 — `ComicTrans`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/ComicTrans |
| Type | Electron/Tauri 계열 만화 OCR·번역·식자 워크벤치 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 대규모 파생 작업대, OCR/번역/인페인트/편집/출력과 실제 E2E 증거 |
| Return cadence | 작품·화·페이지 번역 작업마다 반복하는 생산 도구 |
| Monetization | 상위 원본 프로젝트의 배포·라이선스 계보 확인 필요 |

## Product role

이미지·폴더·ZIP/CBZ를 가져와 OCR, AI 번역, 블록 편집, 원문 인페인트, 최종 PNG 검수·출력을 한 작업대에서 수행한다.

## Core loop

```text
원본 선택 → OCR/번역 범위 실행 → 블록·문맥 검수 → 인페인트 → 원본/중간/최종 비교 → 페이지 승인 → 승인본 출력
```

## Closed implementation

- 다중 입력·작품/화 보관·페이지 선택과 재처리
- 용어집·캐릭터 말투·스토리 기억과 여러 번역 엔진
- 한국어 어절·조사/어미 줄바꿈과 식자 품질 개선
- 실제 18페이지 번역·인페인트·PNG export E2E

## Main bottleneck

기능 수가 많아 작업 시작점과 현재 페이지 상태가 불명확해지기 쉽다. 자동 전체 실행과 단계별 실행이 서로 다른 workflow engine으로 갈라지면 취소·실패·재개·승인 상태가 불일치한다. AGY/Gemma fallback도 번역 계약 오류에만 적용되고 OCR·저장·인페인트 오류까지 덮어서는 안 된다.

## Next bounded action

기존 작업대와 단일 JobState를 유지한 채 `가져오기→OCR/번역→식자/인페인트→비교→페이지 승인→승인본 출력`을 하나의 상태 기계로 정리한다. GUI는 각 단계 실행과 전체 실행이 같은 명령을 호출하게 하고, 실패 페이지를 검수 완료로 승격하지 않는다. `CarrotMangaWorkbench`는 동일 계보 스냅샷으로 정리한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
