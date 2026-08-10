---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-BINDERY-WEB"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Bindery-web"
category: "productized_main"
---

# Bindery 행사 데이터베이스 — `Bindery-web`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Bindery-web |
| Type | 웹 독립 창작자 행사 데이터·준비 아카이브 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 광범위한 웹 구현, 운영 Supabase·실제 데이터 공급 미연결 |
| Return cadence | 행사 신청 마감·준비·회차 비교에 따른 주간/월간 반복 |
| Monetization | 고정 광고 슬롯 설계, 실제 광고·결제 없음 |

## Product role

한국 독립 문구·일러스트 창작자가 행사 신청 조건·비용·마감·과거 회차를 비교하고 달력·Notes·Community로 준비하는 데이터 제품이다.

## Core loop

```text
가까운 마감 발견 → 행사 비교/과거 회차 확인 → 저장·달력 등록 → 준비 Notes 확인 → 행사 후 다음 회차/커뮤니티 재방문
```

## Closed implementation

- 행사 목록·비교·아카이브·달력·회차 상세·RSS/ICS
- 공식 원문 수집·해시·필드 근거의 콘텐츠 파이프라인
- Supabase/RLS 기반 커뮤니티·작가 인증·신고·이의제기 계약
- 다중 viewport 테스트와 fail-closed 런타임 경계

## Main bottleneck

코드보다 데이터 운영이 제품이다. 실제 행사 카탈로그를 지속 수집·검수하지 않으면 비교·아카이브·달력 모두 빈 구조가 된다. Community는 운영 DB·약관·모더레이션 없이 공개할 수 없고, 초기 가치에는 필수가 아니다. 또 소설 집필 앱 `Bindery`와 이름이 충돌한다.

## Next bounded action

1차 공개 범위를 행사 데이터베이스·비교·달력·Notes로 제한하고, 행사별 최신성·확인일·공식 출처를 운영 지표로 삼는다. Community는 충분한 방문자와 운영 절차가 생긴 뒤 연결한다. 두 Bindery 중 하나는 명칭을 변경한다.

## Open feature PRs

- [#2 ci(screenshots): capture and upload the site gallery](https://github.com/eiranotes/Bindery-web/pull/2) — open; 30장 반응형 실화면 캡처 자동화

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
