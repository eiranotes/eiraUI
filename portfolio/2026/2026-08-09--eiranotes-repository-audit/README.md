---
schema_version: "1.1.0"
audit_id: "RPA-20260809-001"
status: "complete"
created_at: "2026-08-09"
owner: "eiranotes"
repository_count: 28
artifact_type: "repository_product_audit"
tree_version: "category-split-v1"
---

# eiranotes 저장소·제품 포트폴리오 감사

28개 저장소 감사를 저장소별 개별 문서로 분리했다. 열린 PR의 기능은 `main` 구현과 구분하며, 각 문서는 제품 역할·핵심 루프·닫힌 구현·주 병목·다음 작업을 독립적으로 읽을 수 있다.

## 탐색 구조

```text
portfolio/2026/2026-08-09--eiranotes-repository-audit/
├── README.md
├── data/
│   └── manifest.json
└── repositories/
    ├── productized-main/       # 17
    ├── branch-only/            # 2
    ├── prototypes/             # 2
    ├── infrastructure/         # 1
    ├── duplicates/             # 1
    ├── external-references/    # 4
    └── empty/                  # 1
```

## 분류 요약

| 분류 | 수 | 디렉터리 |
|---|---:|---|
| 제품화된 main · 구현형 vertical slice | 17 | [`repositories/productized-main/`](repositories/productized-main/) |
| branch·PR 전용 제품 후보 | 2 | [`repositories/branch-only/`](repositories/branch-only/) |
| UI·기능 프로토타입 | 2 | [`repositories/prototypes/`](repositories/prototypes/) |
| 내부 인프라 | 1 | [`repositories/infrastructure/`](repositories/infrastructure/) |
| 중복·계승 저장소 | 1 | [`repositories/duplicates/`](repositories/duplicates/) |
| 외부 원본·참조 | 4 | [`repositories/external-references/`](repositories/external-references/) |
| 빈 저장소 | 1 | [`repositories/empty/`](repositories/empty/) |

## 저장소별 분석

### 제품화된 main · 구현형 vertical slice
- [Adelie Pages — `AdeliePages`](repositories/productized-main/adeliepages.md)
- [App Audit — `AppAudit`](repositories/productized-main/appaudit.md)
- [Bindery 행사 데이터베이스 — `Bindery-web`](repositories/productized-main/bindery-web.md)
- [Bindery AI 장기 소설 집필 하네스 — `Bindery`](repositories/productized-main/bindery.md)
- [Maia Recap Chess — `chess-maia-recap`](repositories/productized-main/chess-maia-recap.md)
- [Clip Inbox — `ClipInbox`](repositories/productized-main/clipinbox.md)
- [당근망가번역기 작업대 — `ComicTrans`](repositories/productized-main/comictrans.md)
- [DeepMine — `Deepmine`](repositories/productized-main/deepmine.md)
- [Folio — `Folio`](repositories/productized-main/folio.md)
- [하루선 — `Haruseon`](repositories/productized-main/haruseon.md)
- [Project Ink — `Ink`](repositories/productized-main/ink.md)
- [Keep AI Chats — `KeepAIChats`](repositories/productized-main/keepaichats.md)
- [Reality Diorama / Locus — `Locus`](repositories/productized-main/locus.md)
- [MapRibbon — `Mapribbon`](repositories/productized-main/mapribbon.md)
- [Memoboard — `memoboard`](repositories/productized-main/memoboard.md)
- [OpenFront Fortress — `Openfrontnew`](repositories/productized-main/openfrontnew.md)
- [PEELBEAST — `Peelbeast`](repositories/productized-main/peelbeast.md)

### branch·PR 전용 제품 후보
- [Test / 제품 인큐베이터 — `Test`](repositories/branch-only/test.md)
- [Token Wars — `TokenWars`](repositories/branch-only/tokenwars.md)

### UI·기능 프로토타입
- [PEELBEAST Safari Demo — `eiraground`](repositories/prototypes/eiraground.md)
- [구름 고양이의 작은 모험 — `WorldpostOffice`](repositories/prototypes/worldpostoffice.md)

### 내부 인프라
- [eiraUI — `eiraUI`](repositories/infrastructure/eiraui.md)

### 중복·계승 저장소
- [CarrotMangaWorkbench — `CarrotMangaWorkbench`](repositories/duplicates/carrotmangaworkbench.md)

### 외부 원본·참조
- [Grok Build — `grok-build`](repositories/external-references/grok-build.md)
- [Harness Engineering — `harness-engineering`](repositories/external-references/harness-engineering.md)
- [k-skill — `k-skill`](repositories/external-references/k-skill.md)
- [Maia-2 — `maia2`](repositories/external-references/maia2.md)

### 빈 저장소
- [r3s — `r3s`](repositories/empty/r3s.md)

## 데이터 계약

- [`data/manifest.json`](data/manifest.json) — 분류, canonical 여부, 열린 PR, 개별 분석 경로
- [`templates/REPOSITORY_PRODUCT_AUDIT.md`](../../../templates/REPOSITORY_PRODUCT_AUDIT.md) — 이후 저장소 감사 템플릿

## 운영 규칙

```text
새 기능을 추가하기 전에 현재 병목을 코드, 외부 플랫폼, 콘텐츠·아트, 운영 데이터,
저장소 계보 중 하나로 명시한다. 열린 PR은 main 구현과 분리하고, 검증하지 않은
실기기·스토어·외부 provider 상태를 완료로 기록하지 않는다.
```
