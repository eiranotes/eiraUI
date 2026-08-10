---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-OPENFRONTNEW"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Openfrontnew"
category: "productized_main"
---

# OpenFront Fortress — `Openfrontnew`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Openfrontnew |
| Type | 웹 대규모 전략 게임 포크 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 플레이 가능한 main·Pages 배포, 경제/전쟁 밸런스 PR 진행 |
| Return cadence | 한 판 단위 세션, 멀티플레이가 붙으면 반복 상승 |
| Monetization | 저장소에서 정의되지 않음; AGPL 기반 포크 |

## Product role

OpenFront를 기반으로 소국의 도시·공장 내정, 병력 품질, 명시적 모바일 명령, 동맹 협동을 강화한 전략 게임이다.

## Core loop

```text
영토 확보 → 도시/공장 개발 → 훈련 수용량·품질 상승 → 지상/상륙/동맹 전투 → 후반 핵·승리
```

## Closed implementation

- Fortress 내정·병력 품질·점령·해상 규칙
- 모바일 국가 선택 후 명시적 명령 도크
- 싱글플레이 옵션·Pages 배포와 회귀 테스트
- 열린 PR에서 재래식 전쟁·경제·핵 escalaton 재조정

## Main bottleneck

핵이 재래식 힘싸움을 압도하면 도시·공장 투자의 장기 선택이 후반에 무효화된다. 반대로 내정 보너스가 즉시 전투력으로만 환산되면 빌드 다양성이 줄어든다. 현재 공개 친구 방·초대·재접속 서버가 없어서 장기 멀티플레이 제품으로는 인프라가 비어 있다.

## Next bounded action

PR #24의 경제·재래식·핵 단계 조정을 match simulation으로 고정하고, 승리 경로별 평균 경기시간·핵 도달 시점·도시 투자 회수기간을 기록한다. 이후에만 친구 방/재접속을 붙인다.

## Open feature PRs

- [#24 Rebalance Fortress strategy and fix GitHub Pages navigation](https://github.com/eiranotes/Openfrontnew/pull/24) — open; 현행 경제·재래식·핵 밸런스 주 작업

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
