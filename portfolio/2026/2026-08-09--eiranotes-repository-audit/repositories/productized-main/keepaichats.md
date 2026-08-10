---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-KEEPAICHATS"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/KeepAIChats"
category: "productized_main"
---

# Keep AI Chats — `KeepAIChats`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/KeepAIChats |
| Type | iOS AI 대화 보관·검색 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 제품화된 main, Share Extension·붙여넣기·오프라인 아카이브·StoreKit 구현 |
| Return cadence | AI 대화를 보관하거나 다시 이어갈 때 반복 |
| Monetization | 새 대화 5개 무료 후 Lifetime |

## Product role

ChatGPT·Claude·Gemini 공개 링크와 명시적 붙여넣기를 로컬 대화 아카이브로 저장하고 오프라인 읽기·검색·정리·내보내기를 제공한다.

## Core loop

```text
공개 링크 공유/세션 붙여넣기 → Inbox 저장 → 읽기 위치·메모·폴더·태그 정리 → 검색/재열기 → 원문 새로고침 또는 같은 대화 계속하기
```

## Closed implementation

- Share Extension 즉시 내구 작업과 main-app 복구
- Provider별 IR, GRDB/FTS5, 패키지 아카이브와 첨부파일
- 대화 역할을 추측하지 않는 명시적 붙여넣기
- 5회 무료 quota와 Lifetime StoreKit 경계

## Main bottleneck

단순 ‘보관함’만으로는 사용자가 원래 AI 서비스의 기록보다 한 단계를 더 거칠 이유가 약하다. 열린 PR의 Continue same chat·append·최근 읽기 기능은 이 약점을 직접 겨냥한다. 다만 별도 Continue 탭까지 늘리면 Library/Search/Settings의 단순성이 다시 흔들릴 수 있다. 실제 provider MIME·Share Sheet·sandbox 구매는 기기 외부 게이트다.

## Next bounded action

PR의 데이터 정확성·append·context export는 우선 반영하고, Continue 경험은 새 탭보다 Library 상단의 최근 읽기/같은 대화 이어가기 모듈로 먼저 검증한다. 핵심 마케팅 문구도 ‘AI 대화 저장’보다 ‘나중에 찾아서 그대로 이어 쓰기’로 맞춘다.

## Open feature PRs

- [#1 feat: add retention loops and harden archive correctness](https://github.com/eiranotes/KeepAIChats/pull/1) — open; same-chat append·context reuse·정확성
- [#2 feat: add Continue dashboard for unfinished AI work](https://github.com/eiranotes/KeepAIChats/pull/2) — open / stacked; 재방문 표면 검증

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
