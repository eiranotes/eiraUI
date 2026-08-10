---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-PEELBEAST"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Peelbeast"
category: "productized_main"
---

# PEELBEAST — `Peelbeast`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Peelbeast |
| Type | 웹 파츠 조립형 턴제 로그라이크 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | 결정론적 vertical slice, 엔진·E2E·밸런스 simulator 구현 |
| Return cadence | 한 런과 조합 실험 중심의 반복 |
| Monetization | 저장소에서 정의되지 않음 |

## Product role

머리·손·코어·장신구를 붙여 만든 짐승이 전투 피해로 파츠를 실제로 잃고 스킬·패시브·시너지도 함께 사라지는 종이공예 로그라이크다.

## Core loop

```text
Workshop 조립 → 노드 선택 → 의도 기반 전투 → 파츠 박리/재부착 → 보상·상점·이벤트 → 보스 → 새 조합 런
```

## Closed implementation

- 엔진/렌더 분리, 선언형 능력, seeded RNG
- 박리와 스킬/시너지 상실의 일관된 규칙
- 10개 화면·루트·상점·이벤트·리릭·이어하기
- 143 unit/integration + 18 E2E와 screenshot 기반 layout 수정

## Main bottleneck

현재 제품 리스크는 코드가 아니라 최종 아트와 콘텐츠량이다. placeholder 파츠가 많고 사운드·튜토리얼이 없으며, 3종 적과 제한된 파츠로는 로그라이크 반복성이 빨리 소진된다. 밸런스는 시뮬레이터 정책 오류가 한 차례 있었으므로 인간 플레이 검증이 필요하다.

## Next bounded action

완성 아트 1캐릭터·파츠 8~12개·적 4개·보스 1개로 한 런을 완성하고 튜토리얼·박리 사운드/모션을 붙인다. 그 vertical slice를 플레이테스트한 뒤 콘텐츠 수를 늘린다.

## Open feature PRs

- [#1 Add PEELBEAST image asset pack](https://github.com/eiranotes/Peelbeast/pull/1) — open; 교체형 에셋 팩

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
