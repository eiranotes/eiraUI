---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001-DEEPMINE"
status: "complete"
created_at: "2026-08-09"
repository: "eiranotes/Deepmine"
category: "productized_main"
---

# DeepMine — `Deepmine`

## Identity

| Field | Value |
|---|---|
| Repository | https://github.com/eiranotes/Deepmine |
| Type | iOS 방치형 세로 채굴 클리커 |
| Category | 제품화된 main / 구현형 vertical slice |
| Current state | iOS Core/App + 플레이 가능한 웹 parity demo |
| Return cadence | 짧은 탭 세션·오프라인 정산·정련·프레스티지 반복 |
| Monetization | 저장소에서 확정되지 않음 |

## Product role

암반을 직접 깨고 광차 자동 생산과 오프라인 정산으로 갱도를 내려가며 정련·프레스티지하는 방치형 게임이다.

## Core loop

```text
탭 채굴 → 장비 구매 → 자동 굴착 → 오프라인 보상 → 정련 → 120층 프레스티지 → 더 깊은 지질
```

## Closed implementation

- BigNumber 경제와 장기 깊이 안전성
- iOS 앱·Widget/Live Activity 공유 모델과 웹 parity
- 결정된 4m partition break/fall 시각 루프
- 다수 경제·앱·웹·에셋 회귀 테스트

## Main bottleneck

코어 루프는 이미 명확하다. 남은 위험은 30/90/180일 실제 구매 정책에서 성장 곡선이 멈추거나 추천이 왜곡되는지, 깊어질수록 시각적 변화가 충분한지다. 집중 세션 보상이 실제 채굴 루프와 별도 계산이면 이중 보상·설명 불일치가 생긴다.

## Next bounded action

실제 UI 추천·MAX·정련 정책을 그대로 쓰는 장기 시뮬레이션을 먼저 고정하고, 집중 세션을 하나의 MiningLoop 시간 배율로 통합한다. 신규 시스템보다 지질 세대·장비 외형·프레스티지 결과의 시각 차이를 확장한다.

## Evidence boundary

This record is based on repository metadata, canonical documentation, recent commits, and open PRs reviewed on 2026-08-09. It does not claim a fresh runtime/build/device execution unless the repository itself records that evidence.
