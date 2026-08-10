---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-CHESS-MAIA-RECAP"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/chess-maia-recap"
category: "productized_main"
---

# Maia Recap Chess — `chess-maia-recap`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/chess-maia-recap |
| Type | 로컬 웹 체스 대국·복기·FSRS 훈련 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 2.2.0 기능 완성, 외부 Maia/Stockfish와 release package 재검증 필요 |
| Return cadence | 대국 후 자동 복기와 매일 due 훈련 |
| Monetization | 저장소에서 정의되지 않음 |

## Product role

CPU 대국을 자동 분석하고 핵심 실수를 개인 문제·PV 이어두기·약점 점검 대국·FSRS 복습으로 연결하는 로컬 학습 앱이다.

## Core loop

```text
대국 → 자동 분석 → 핵심 장면 복기 → 힌트 없는 문제/이어두기 → FSRS due 복습 → 약점 점검 대국 → 전이율 확인
```

## Closed implementation

- FastAPI/python-chess/SQLite와 브라우저 전체 E2E
- Maia 인간착수 확률 + Stockfish 객관 평가 + 안전 fallback
- 문제·이어두기·FSRS·약점 통계의 연결
- 멱등 착수·복구·데이터 내보내기/삭제

## Main bottleneck

제품 루프는 닫혀 있으나 설치·배포가 병목이다. 현재 저장된 Maia runtime이 없고 real-engine gate가 SKIP이며, release ZIP/checksum이 오래됐고 build script의 source/stage 중첩 삭제 위험이 문서화되어 있다. 사용자는 모델·엔진 설치 문제를 앱 품질 문제로 인식할 수 있다.

## Next bounded action

release builder의 경로 겹침을 fail-closed로 수정하고 새 bundle·checksum을 만든 뒤, 실제 Maia/Stockfish smoke를 같은 release candidate에서 재실행한다. 그 후 800~1400 사용자에게 ‘대국→복기→다음날 due’ 전환만 검증한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
