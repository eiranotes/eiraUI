---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-BINDERY"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Bindery"
category: "productized_main"
---

# Bindery AI 장기 소설 집필 하네스 — `Bindery`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Bindery |
| Type | Tauri 로컬 장기소설 AI 워크벤치 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | macOS standalone·실시간 CLI·85 tests 수준의 제품화 main |
| Return cadence | 회차 단위 장기 집필 |
| Monetization | 저장소에서 정의되지 않음 |

## Product role

세계관·플롯·브리프·장면 계획·원고 후보·3관점 QA·정사 변경을 로컬 Markdown 프로젝트에서 인간 승인 중심으로 관리한다.

## Core loop

```text
작품 생성/가져오기 → 이번 화 브리프·장면 계획 → AI 원고 후보 → diff 적용 → 병렬 QA/수정 → 정사 승인·마감 → 다음 화
```

## Closed implementation

- 간단 모드와 설계자 모드, 단계별 workflow
- Codex/Claude/AGY CLI streaming·취소·quota 표시
- 안전 ZIP import, Markdown/TXT/EPUB/DOCX export, backup/restore
- 후보 stale guard와 인간 승인 경계

## Main bottleneck

기능 깊이는 충분하지만 신규 사용자는 세계관·플롯·resume/restart·provider 설정을 이해해야 한다. 외부 CLI 품질과 quota에 따라 경험이 달라지고, 긴 작품에서 요약·정사·캐릭터 상태가 실제로 일관된지는 단기 테스트로 증명되지 않는다. 배포는 Developer ID notarization이 남아 있다.

## Next bounded action

간단 모드의 ‘이번 화 쓰기’만으로 10회차짜리 실제 프로젝트를 끝까지 운영해 semantic drift와 수정 비용을 측정한다. 첫 배포는 provider 하나와 로컬 파일 프로젝트만 지원하고 설계자 모드는 고급 기능으로 둔다. 행사 DB와 이름 충돌도 해소한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
