---
schema_version: "1.0.0"
audit_id: "RPA-20260809-001"
status: "complete"
created_at: "2026-08-09"
owner: "eiranotes"
repository_count: 28
artifact_type: "repository_product_audit"
evidence_level: "repository metadata + canonical docs + recent commits + open PRs"
---

# eiranotes 저장소·제품 포트폴리오 감사

## 0. 범위

2026-08-09 현재 GitHub에서 접근 가능한 `eiranotes` 저장소 28개를 전수 분류했다. 저장소 메타데이터, `README`, 최신 `PROJECT_STATUS` 또는 동등 문서, 최근 커밋, 열린 PR을 대조했다. 열린 PR에만 있는 기능은 `main` 구현과 분리한다. 이 문서는 포트폴리오·제품 상태 감사이며 28개 저장소를 모두 새로 빌드하거나 모든 소스 라인을 재실행한 결과라고 주장하지 않는다.

## 1. 전체 분류

| 분류 | 수 | 저장소 |
|---|---:|---|
| 제품화된 main / 구현형 vertical slice | 17 | Haruseon, Ink, KeepAIChats, AppAudit, ClipInbox, AdeliePages, Locus, Mapribbon, Bindery-web, Openfrontnew, ComicTrans, chess-maia-recap, Deepmine, Folio, Peelbeast, Bindery, memoboard |
| branch·PR 전용 제품 후보 | 2 | TokenWars, Test |
| UI·기능 프로토타입 | 2 | WorldpostOffice, eiraground |
| 내부 인프라 | 1 | eiraUI |
| 중복·계승 저장소 | 1 | CarrotMangaWorkbench |
| 외부 원본·참조 | 4 | k-skill, harness-engineering, grok-build, maia2 |
| 빈 저장소 | 1 | r3s |
| **합계** | **28** |  |

## 2. 포트폴리오 단위 결론

제품화된 저장소 상당수는 코어 기능, 테스트, 로컬 데이터 경계, UI 구조까지 이미 갖췄다. 반복되는 병목은 기능 누락보다 다음 다섯 종류다.

1. 실기기·플랫폼 권한: Share Extension, Family Controls, 사진 제한 접근, 백그라운드 위치, locked-state App Group.
2. 스토어·배포: App Store Connect 상품, Sandbox/TestFlight, distribution signing, Xcode Validate/Upload, macOS notarization.
3. 콘텐츠·에셋: Adelie 팩, Locus 디오라마, PEELBEAST 최종 아트, DeepMine 장기 지질 변화.
4. 운영 데이터: Bindery-web 행사 카탈로그, 커뮤니티 운영 DB, 최신성 검수.
5. 저장소 계보: ComicTrans/Carrot 중복, eiraground 구형 데모, Test의 서로 다른 두 제품, Bindery 이름 충돌.

## 3. 제품화된 main 17개

### 3.1 하루선 — `Haruseon`

- **형태:** iOS 로컬 이동 기록·리캡.
- **현재 상태:** 제품화된 main. 배경 위치, 사진 증거, 시간대·DST, 프라이버시, 픽셀 릴리프 렌더가 구현돼 있다.
- **핵심 루프:** 권한 설정 → 백그라운드 증거 수집 → 하루 타임라인 → 일일·월간·여행 리캡 → 누적 흔적 재방문·공유.
- **닫힌 부분:** 경로 단절·불확실성 표시, 집·회사 공유 마스킹, 04:00 기준일, 지도 타일 없는 릴리프, 리캡 데이터 모델.
- **병목:** 짧은 동네 이동부터 전국·해외 이동까지 같은 문법을 유지하면서 행정 경계, 체류 높이, 경로 단절, 밀집 지역을 장기적으로 읽히게 해야 한다. 실기기 배터리와 장기간 위치 데이터도 남아 있다.
- **다음 작업:** 서울·광역·여행을 포함한 실제 30일 fixture로 일일/주간/월간/여행 출력을 동시에 고정한다. Today 복제가 아니라 누적 밀도와 시간 차이가 읽히는 별도 공유 계약을 유지한다.

### 3.2 Project Ink — `Ink`

- **형태:** iOS 문장 보관·재노출.
- **현재 상태:** Today/문장 2탭, SwiftData, 알림, Widget, Live Activity, StoreKit Lifetime이 구현됐다.
- **핵심 루프:** 문장 저장 → Today 확인 → 일정 재노출 → 읽기·다음·고정 → Library 정리 → 재노출.
- **닫힌 부분:** 대량 가져오기·중복·백업, 시스템 표면 역할 분리, 무료/Pro 빈도, 잉크 표식·타이포그래피.
- **병목:** 첫 저장 뒤 실제로 다시 만나는 경험이 며칠 안에 발생하고 사용자가 제품 차이를 이해하는지가 핵심이다. App Store StoreKit lifecycle은 외부 게이트다.
- **다음 작업:** 첫 72시간의 `저장→첫 재노출→두 번째 문장 추가`만 로컬 이벤트로 검증한다. 새 시각 변형보다 노출 빈도·폴더·대량 가져오기라는 사용량 경계를 유지한다.

### 3.3 Keep AI Chats — `KeepAIChats`

- **형태:** iOS AI 대화 보관·검색.
- **현재 상태:** 공개 링크·명시적 붙여넣기, Share Extension, GRDB/FTS5, 오프라인 archive, 첨부파일, 5회 무료 후 Lifetime이 구현됐다.
- **핵심 루프:** 공유/붙여넣기 → Inbox 저장 → 읽기·메모·폴더·태그 → 검색·재열기 → 원문 새로고침 또는 같은 대화 이어가기.
- **닫힌 부분:** 즉시 내구 작업과 복구, provider IR, 역할 추측 방지, quota·StoreKit 경계.
- **병목:** 원래 AI 서비스의 기록보다 한 단계를 더 거칠 이유가 보관만으로는 약하다. PR #1의 same-chat append·context reuse는 직접적인 보강이고, PR #2의 별도 Continue 탭은 내비게이션 증가를 다시 검증해야 한다.
- **다음 작업:** PR #1의 데이터 정확성·append·context export를 우선 검토하고, Continue는 새 탭보다 Library 상단 모듈로 먼저 검증한다.
- **열린 PR:** #1 retention/correctness, #2 stacked Continue dashboard.

### 3.4 App Audit — `AppAudit`

- **형태:** iOS Screen Time 의사결정·시험 제거.
- **현재 상태:** Guided/조건부 Automatic 감사, keep/postpone/Trial, SwiftData 이력, fail-open Trial 커널, StoreKit이 로컬 구현됐다.
- **핵심 루프:** 감사 주기 → 후보 검토 → 앱별 결정 → 7/14일 Trial → 만기 결과 → 다음 감사.
- **닫힌 부분:** 결정 기록, 단일 활성 Trial, 복구 원장, 공유 receipt, 다국어. 열린 PR은 Audit/Portfolio와 불변 결정 이력을 확장한다.
- **병목:** Shield 복구, 확장 콜백, 재부팅, 배포 entitlement는 Simulator로 증명할 수 없다. 여러 stacked PR이 물리 기기 게이트보다 앞서 범위를 넓히고 있다.
- **다음 작업:** 물리 기기 Trial recovery matrix와 distribution entitlement를 먼저 닫는다. 그 뒤 세션 귀속·불변 결정 이력 같은 정확성 변경을 우선한다.
- **열린 PR:** #1~#7 retention, protected report, product shell, Share Studio, immutable history stack.

### 3.5 Clip Inbox — `ClipInbox`

- **형태:** iOS 공유 시트 기반 로컬 클립 보관.
- **현재 상태:** iPhone-only native app, Share Extension, 링크·텍스트·사진, 폴더·태그·검색·휴지통·백업, grouped-photo schema v3가 구현됐다. PR #1은 1.3 packaging이다.
- **핵심 루프:** 외부 앱 공유 → 즉시 저장/검토 → Inbox → 나중에 분류·메모 → 검색·재열기 → 백업.
- **닫힌 부분:** crash-safe App Group 전달, 공개 주소 검증 메타데이터, 다중 사진 한 Clip, 전체 로컬 관리.
- **병목:** 저장 후 다시 찾는 비율이다. grouped-photo 변경 뒤 이전 release closeout을 그대로 사용할 수 없고 전체 suite·Release·bundle·실기기 Share를 다시 닫아야 한다.
- **다음 작업:** 1.3 release gate를 우선 완료하고, 추가 기능은 Sort Later 완료율·검색 재열기·폴더 이동 등 저장 이후 행동으로 제한한다.

### 3.6 Adelie Pages — `AdeliePages`

- **형태:** Flutter 디지털 문구·페이지 스튜디오.
- **현재 상태:** Page-first 편집기, 원자적 autosave, undo/redo, 다중 선택, export, 다국어·고대비, Android/iOS 검증이 대규모로 구현됐다.
- **핵심 루프:** 팩/페이지 선택 → Compose → 저장·미리보기 → PNG/Story/클립보드 공유 → Library 재편집 → 새 팩 탐색.
- **닫힌 부분:** 3-band 문서, 편집기 조작, 반응형·접근성, release/asset gates. PR #5는 최신 카탈로그와 release contract를 합친다.
- **병목:** 편집기보다 판매 가능한 종이·스티커 팩, 브랜드 승인, CDN/카탈로그 운영, 실제 Store 상품이 부족하다.
- **다음 작업:** 편집기 기능을 동결하고 starter/paid 팩 소수로 `팩 상세→바로 사용→완성본 공유` 전환을 검증한다.

### 3.7 Locus — `Locus`

- **형태:** Flutter 현실 수집·디오라마 크래프팅.
- **현재 상태:** iOS/Android MVP, SQLite 거래, 날씨·걸음·선택적 BLE, 5×5 결정론적 isometric renderer, 양 플랫폼 CI가 있다.
- **핵심 루프:** 날씨/주변 캡처 → 재료 → 걸음 작업량 → 제작 → 배치 → 방문자·레시피 → 다음 캡처.
- **닫힌 부분:** cooldown, FIFO 걸음 소비, WeatherKit/Open-Meteo 경계, 가짜 재료 금지, 프라이버시.
- **병목:** placeholder 디오라마의 아트와 7일 콘텐츠 밀도다. 입력 시스템이 많아도 장면과 방문자가 반복되면 재방문으로 전환되지 않는다.
- **다음 작업:** 동일 광원·2:1 grid의 완성 에셋 한 세트와 7일 레시피/방문자 곡선을 먼저 만든다.

### 3.8 MapRibbon — `Mapribbon`

- **형태:** iOS 사진 메타데이터 여행 포토보드.
- **현재 상태:** 사진 날짜·위치 클러스터링, MapKit snapshot, 여러 보드 템플릿, Archive/Atlas, Lifetime 골격이 있다. PR #12는 Survey Plate 셸과 Atlas 개선이다.
- **핵심 루프:** 사진 접근 → 여행 날짜 → 자동 장소/대표 사진 → 편집 → 공유 → Atlas/Archive.
- **닫힌 부분:** 사진 파이프라인, 대표 사진·장소 편집, 4:5·9:16 출력, 한국 지역 Atlas.
- **병목:** 자동 대표 사진·장소명·클러스터가 틀릴 때 발생하는 수동 수정 비용과 실제 사진·iCloud·제한 권한 검증이다.
- **다음 작업:** 실제 여행 20세트로 자동 결과를 평가하고 날짜 선택부터 4:5 공유까지 1분 경로를 기준으로 템플릿을 줄인다. Haruseon의 이동 기록 기능은 흡수하지 않는다.

### 3.9 Bindery 행사 데이터베이스 — `Bindery-web`

- **형태:** 웹 독립 창작자 행사 데이터·준비 아카이브.
- **현재 상태:** 행사 목록·비교·아카이브·달력·Notes·Community 계약과 공식 원문 수집 파이프라인이 구현됐지만 운영 Supabase와 실제 데이터 공급은 미연결이다.
- **핵심 루프:** 마감 발견 → 행사 비교·과거 회차 → 저장·달력 → 준비 Notes → 다음 회차 재방문.
- **닫힌 부분:** 공식 출처·해시·필드 근거, RSS/ICS, RLS·신고·이의제기 계약, 반응형 테스트.
- **병목:** 코드가 아니라 지속적인 행사 데이터 수집·검수다. Community는 초기 가치에 필수가 아니며 운영 절차가 필요하다. 소설 앱 Bindery와 이름도 충돌한다.
- **다음 작업:** 1차 공개를 데이터베이스·비교·달력·Notes로 제한하고 최신성·확인일·공식 출처를 운영 지표로 삼는다.

### 3.10 OpenFront Fortress — `Openfrontnew`

- **형태:** 웹 대규모 전략 게임 포크.
- **현재 상태:** 내정, 병력 품질, 점령·해상 규칙, 모바일 명령 도크, Pages demo가 있다. PR #24가 현행 경제·재래식·핵 밸런스 변경이다.
- **핵심 루프:** 영토 → 도시/공장 → 훈련·품질 → 지상/상륙/동맹 전투 → 핵·승리.
- **닫힌 부분:** Fortress 경제와 명시적 모바일 명령, 싱글플레이, 배포·회귀 테스트.
- **병목:** 핵이 장기 내정 투자를 무효화하거나, 내정이 즉시 전투력 한 축으로만 환산되는 문제다. 친구 방·초대·재접속 서버도 없다.
- **다음 작업:** PR #24를 match simulation으로 검증하고 승리 경로별 경기시간, 핵 도달 시점, 도시 투자 회수기간을 기록한 뒤 멀티플레이 인프라를 붙인다.

### 3.11 당근망가번역기 작업대 — `ComicTrans`

- **형태:** Electron/Tauri 계열 만화 OCR·번역·식자 워크벤치.
- **현재 상태:** 다중 입력, OCR, 여러 번역 엔진, 용어집·캐릭터 말투·스토리 기억, 인페인트, 블록 편집, PNG export와 실제 18페이지 E2E가 있다.
- **핵심 루프:** 원본 → OCR/번역 → 블록·문맥 검수 → 인페인트 → 원본/중간/최종 비교 → 페이지 승인 → 승인본 출력.
- **닫힌 부분:** 한국어 어절·조사/어미 줄바꿈, 원문 윤곽 보존, AGY/Luna adapter, 실제 화 단위 출력.
- **병목:** 전체 자동 실행과 단계별 실행이 다른 workflow engine으로 갈라질 가능성이다. 취소·실패·재개·승인은 하나의 JobState를 써야 하며 fallback은 번역 계약 오류에만 적용해야 한다.
- **다음 작업:** 기존 작업대에서 각 단계와 전체 실행이 같은 명령을 호출하도록 정리하고 실패 페이지를 검수 완료로 승격하지 않는다. CarrotMangaWorkbench는 동일 계보 스냅샷으로 정리한다.

### 3.12 Maia Recap Chess — `chess-maia-recap`

- **형태:** 로컬 웹 체스 대국·복기·FSRS 훈련.
- **현재 상태:** FastAPI/python-chess/SQLite, 대국, Maia+Stockfish 분석, 개인 문제, 이어두기, FSRS, 약점 점검, 전체 E2E가 있다.
- **핵심 루프:** 대국 → 자동 분석 → 핵심 복기 → 힌트 없는 문제/이어두기 → 다음날 due → 약점 점검 대국.
- **닫힌 부분:** 멱등 착수·복구, 훈련 연결, 통계·내보내기·삭제.
- **병목:** 설치·배포다. 저장된 Maia runtime이 없고 real-engine gate가 SKIP이며 release ZIP/checksum과 builder 경로 안전성을 재검증해야 한다.
- **다음 작업:** release builder를 fail-closed로 고치고 새 bundle/checksum에서 Maia·Stockfish smoke를 실행한다.

### 3.13 DeepMine — `Deepmine`

- **형태:** iOS 방치형 세로 채굴 클리커.
- **현재 상태:** iOS Core/App, BigNumber 경제, Widget/Live Activity 공유 모델, 플레이 가능한 웹 parity demo가 있다.
- **핵심 루프:** 탭 채굴 → 장비 → 자동 굴착 → 오프라인 보상 → 정련 → 120층 프레스티지 → 깊은 지질.
- **닫힌 부분:** 장기 수치 안전성, 4m partition break/fall, 경제·앱·웹·에셋 테스트.
- **병목:** 30/90/180일 실제 구매 정책에서 성장 곡선과 추천이 유지되는지, 깊이에 따른 시각 변화가 충분한지다.
- **다음 작업:** 실제 UI 추천·MAX·정련 정책을 사용하는 장기 시뮬레이션과 집중 세션의 단일 MiningLoop 통합을 우선한다.

### 3.14 Folio — `Folio`

- **형태:** iOS 4종 일일 퍼즐 앱.
- **현재 상태:** Flow/Queens/Glow/Drift 각 500문제, 유일해 검증, Daily·Course·Records, versioned session, React/Capacitor 적응형 UI가 있다.
- **핵심 루프:** Daily 선택 → 플레이 → 완료 → 다음 퍼즐 preview → Records/Course → 다음날 Daily.
- **닫힌 부분:** 네 엔진, 자정 갱신, 세션 복구, production capability 분리.
- **병목:** 네 게임이 하나의 습관으로 묶이는 이유와 사람 기준 난이도다. RevenueCat/AdMob provider와 물리 기기 접근성도 남았다.
- **다음 작업:** 새 게임을 추가하지 않고 Daily 4종 완료율·이탈·다음 전환을 확인한 뒤 사람 난이도 calibration과 provider 연결을 한다.

### 3.15 PEELBEAST — `Peelbeast`

- **형태:** 웹 파츠 조립형 턴제 로그라이크.
- **현재 상태:** 엔진/렌더 분리, 선언형 능력, seeded RNG, 10개 화면, simulator, 143 unit/integration + 18 E2E가 있다.
- **핵심 루프:** Workshop 조립 → 노드 → 의도 기반 전투 → 파츠 박리·재부착 → 보상·상점·이벤트 → 보스 → 새 조합.
- **닫힌 부분:** 파츠 손실과 스킬·시너지 상실의 일관성, 이어하기, screenshot 기반 fold 수정.
- **병목:** 최종 아트, 사운드, 튜토리얼, 적·파츠 콘텐츠량이다. simulator 정책 오류 이력이 있어 인간 플레이 검증도 필요하다.
- **다음 작업:** 완성 아트 1캐릭터, 파츠 8~12개, 적 4개, 보스 1개로 한 런 vertical slice를 만든 뒤 확장한다.

### 3.16 Bindery AI 장기 소설 집필 하네스 — `Bindery`

- **형태:** Tauri 로컬 장기소설 AI 워크벤치.
- **현재 상태:** macOS standalone, simple/designer mode, Codex/Claude/AGY streaming, 안전 ZIP import, export, 85 tests가 있다.
- **핵심 루프:** 작품 생성/가져오기 → 회차 브리프·장면 계획 → AI 후보 → diff 적용 → 병렬 QA → 정사 승인 → 다음 화.
- **닫힌 부분:** 실시간 취소·quota, stale candidate guard, 인간 승인, backup/restore.
- **병목:** 신규 사용자의 초기 개념 부담, 외부 CLI 품질·quota, 긴 작품의 semantic drift, notarization이다.
- **다음 작업:** provider 하나와 간단 모드만으로 실제 10회차 프로젝트를 끝까지 운영해 drift와 수정 비용을 측정한다.

### 3.17 Memoboard — `memoboard`

- **형태:** Windows/Tauri 로컬 메모보드.
- **현재 상태:** 공개 v1.0.1, 메모·칸반·달력·체크리스트·검색, IndexedDB 개인 보드, 공유 폴더 JSON/lock이 있다.
- **핵심 루프:** 메모 → 구역·태그 → 체크리스트·달력 → 검색·오늘 패널 → 공유 폴더 동기화.
- **닫힌 부분:** 보드 조작, 달력·휴지통, Windows build, 서버 없는 공유 작업함.
- **병목:** 범용 메모 기능보다 NAS/동기화 폴더 기반 소규모 공유라는 차별점이 전면에 드러나지 않는다. file lock은 실시간 공동편집이 아니다.
- **다음 작업:** 서버 없는 가정·소규모 팀 공유 보드로 포지셔닝하거나 안정된 무료 도구로 유지하며 충돌·복구·설치 경험을 중심으로 문서를 재구성한다.

## 4. branch·프로토타입·인프라·중복·빈 저장소 7개

### 4.1 Token Wars — `TokenWars`

- `main`은 branch 안내 수준이고 PR #3에 CORE/FORK/SERVING 단일 화면 구현이 있다.
- 이전 v0.2 복잡한 모델과 새 단순 모델이 공존하므로 canonical 규칙을 먼저 정해야 한다.
- PR #3을 채택하면 이전 실험을 `legacy/`로 이동하고 5분 이내 한 판 검증을 만든다.

### 4.2 Test 제품 인큐베이터 — `Test`

- PR #1 FairSpan은 거주기간 기반 공과금 안분 앱이다.
- PR #2 MiterRun은 절단 배치와 offcut 재사용 앱이다.
- 사용자, 도메인, 데이터, ASO, 반복 주기가 완전히 다르므로 독립 저장소로 분리한다.

### 4.3 구름 고양이의 작은 모험 — `WorldpostOffice`

- SwiftUI 홈 화면과 테스트는 있으나 실제 퀘스트·교환·월드 진행 상태 전이가 없다.
- 홈을 더 꾸미기 전에 `오늘 퀘스트 1개→우표 획득→교환 1개→홈 상태 변화` vertical slice가 필요하다.

### 4.4 PEELBEAST Safari Demo — `eiraground`

- 프레임워크 없는 초기 Pages/PWA 데모다.
- 현재 본편 `Peelbeast`가 엔진·UI·테스트를 모두 대체한다. archived demo로 표시하거나 본편 build artifact로 교체한다.

### 4.5 eiraUI — `eiraUI`

- 공개 앱 UI를 신원 확인→스크린샷 전수 확보→용어 정규화→재구축 token/QA로 변환하는 내부 프로토콜이다.
- UI Reference와 Repository Product Audit는 artifact type과 schema를 분리하고 공통 인덱스만 공유해야 한다.
- 발자취 분석 PR #6은 현재 open이며 `main`에 병합된 것으로 취급하지 않는다.

### 4.6 Carrot Manga Workbench — `CarrotMangaWorkbench`

- README와 최근 커밋이 ComicTrans와 동일 계보이고 ComicTrans가 UI commit 한 개 앞선다.
- `ComicTrans`를 canonical로 고정하고 이 저장소는 read-only snapshot 또는 archive로 전환한다.

### 4.7 r3s — `r3s`

- size 0으로 분석할 소스·문서·제품 정의가 없다.
- 예정 프로젝트라면 목적·상태 README를 작성하고, 아니면 archive 또는 삭제한다.

## 5. 외부 원본·참조 4개

| 저장소 | 성격 | 포트폴리오 내 사용 | 경계 |
|---|---|---|---|
| `k-skill` | NomaDamas/k-skill 참조 | 한국어 업무 skill 구조·예시 참고 | 사용자 제작 제품으로 집계하지 않음 |
| `harness-engineering` | OpenAI harness engineering 참고 | agent workflow·repo contract 참고 | 직접 앱이 아님 |
| `grok-build` | SpaceXAI 공식 source sync | 외부 구현·빌드 참고 | 사용자 제품으로 집계하지 않음 |
| `maia2` | Toronto Maia Chess 공식 구현 | chess-maia-recap 엔진·연구 근거 | 별도 제품이 아니라 dependency/reference |

## 6. 제품 간 경계

### 6.1 ClipInbox / KeepAIChats / Ink

- ClipInbox: 범용 링크·텍스트·사진을 나중에 분류·검색.
- KeepAIChats: 대화 구조를 보존하고 읽기·검색·같은 대화 이어가기.
- Ink: 선택 문장을 일정에 따라 다시 노출.

세 제품은 합치지 않는다. App Group queue, export/restore, StoreKit release contract만 공통화한다. 제품 간 연결은 사용자가 명시적으로 실행하는 `대화의 선택 문장을 Ink로 보내기` 같은 경계만 허용한다.

### 6.2 Haruseon / Mapribbon / Locus

- Haruseon은 수동 없는 하루 이동 기록.
- Mapribbon은 사진 기반 여행 결과물.
- Locus는 현실 신호를 재료로 쓰는 게임.

위치·사진·걸음의 증거·프라이버시 계약은 공유할 수 있지만 UI와 핵심 루프는 분리한다.

### 6.3 Bindery 이름 충돌

소설 집필 도구와 행사 데이터베이스가 같은 이름을 사용한다. 검색, 설치, 지원, 배포 파일에서 충돌하므로 하나를 변경한다.

## 7. 공통 인프라 후보

- **EiraReleaseKit:** StoreKit Lifetime/restore, legal URL, review milestone, bundle/version consistency, 출시 manifest, 다국어 metadata.
- **EiraCaptureKit:** Share Extension durable queue, acknowledgement, lease, retry, staged-file cleanup, quota settlement.
- **EiraLocalData:** atomic snapshot, schema migration, export/restore, quarantine, cleanup ledger, rollback fixture.
- **EiraVisualQA:** 결정론적 fixture, Light/Dark, Dynamic Type, safe-area, compact-height, contact sheet, CTA destination audit.
- **EiraGeoSpec:** 위치 정확도, 시간대, route gap, 사진 메타데이터, 집/회사 mask, 행정 geometry, offline provenance.

## 8. 실행 레인

| 레인 | 저장소 | 현재 작업 성격 |
|---|---|---|
| 외부 게이트 닫기 | ClipInbox, KeepAIChats, Ink, AppAudit, AdeliePages, Folio, Mapribbon | 실기기·스토어·서명·Sandbox·배포 증거 |
| 제품 루프 검증 | Haruseon, Locus, Bindery-web, Bindery, chess-maia-recap | 장기 실제 데이터·재방문·운영 데이터·설치 경로 |
| 콘텐츠·밸런스 | Deepmine, Peelbeast, Openfrontnew, TokenWars | 장기 경제·최종 아트·콘텐츠량·승리 경로 |
| 생산 도구 상태 통합 | ComicTrans | 단일 JobState·단계/전체 실행·승인 출력 |
| 안정 유지·재포지셔닝 | memoboard | 공유 폴더형 보드와 충돌 복구 |
| 저장소 정리 | WorldpostOffice, eiraground, CarrotMangaWorkbench, Test, r3s | canonical 정의·분리·archive·목적 문서 |

## 9. 기준

```text
새 기능을 추가하기 전에 각 저장소는 현재 병목이 코드, 외부 플랫폼, 콘텐츠·아트,
운영 데이터, 저장소 계보 중 무엇인지 하나로 명시한다. PR 설명과 PROJECT_STATUS는
main과 branch를 분리하고, 검증하지 않은 기기·스토어·외부 provider 상태를 완료로 표시하지 않는다.
```
