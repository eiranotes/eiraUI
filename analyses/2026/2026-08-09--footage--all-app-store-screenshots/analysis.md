---
schema_version: "1.0.0"
analysis_id: "UIR-20260809-002"
status: "complete"
created_at: "2026-08-09"
updated_at: "2026-08-09"
title: "발자취 - 세상에 나를 남기다 — Complete public App Store screenshot UI reconstruction"
subject:
  product_name: "발자취 - 세상에 나를 남기다"
  product_type: "app"
  surface_name: "All six public Korean iPhone App Store screenshots"
  platform: "iOS"
  locale: "ko"
  theme: "light"
target:
  platform: "iOS"
  framework: "SwiftUI / MapKit / Canvas"
reference_storage: "link_only"
template_version: "1.1.0"
---

# 발자취 - 세상에 나를 남기다 — Complete Public App Store Screenshot UI Reconstruction

## 0. Reconstruction directive

> **Pattern:** `location-recording utility + personal geographic collection + hierarchical memory journal`  
> **Primary style:** `Quiet Dot-Atlas Lifelog` (`PROJECT_DEFINED`)  
> **Underlying terms:** `low-chrome iOS utility`, `editorial data minimalism`, `personal informatics`, `dot-matrix cartography`, `collectible geography` (`INDUSTRY_CONVENTIONAL`)  
> **Platform shell:** five-destination floating tab bar, circular recording action, period segmented control, summary cards, MapKit route previews, two-column badge collection, hierarchical journal canvas, large region-profile sheet  
> **Core composition:** white operational surfaces and warm off-white journal surfaces frame repeated regular geographic dot fields; neutral dots represent the base geography, dark dots communicate accumulated coverage, and muted photo-derived colors convert visited places into personal memory  
> **Rebuild rule:** calibrate the 1320×2868 references as a 440×956 pt frame at 3×; preserve a 16 pt page inset, 44 pt minimum controls, approximately 3 pt dots on a 4.5–5 pt pitch, a 72 pt floating tab bar, and one consistent dot-atlas grammar while differentiating Map, Badge, and Journal by task and hierarchy  
> **Do not introduce:** basemap imagery beneath the national dot atlas, route glow, generic map pins, choropleth or heatmap semantics, neon game styling, unexplained color-only states, card-heavy dashboards, free camera rotation, or additional top-level destinations

### One-paragraph reconstruction language

```text
Build a quiet Korean walking lifelog in which one geographic dot grammar connects the
entire product. The Map surface starts and monitors a walk; Records explains daily,
weekly, and monthly activity; Badges turns administrative coverage into a finite
collection; Journal attaches photos, palette colors, and notes to the same hierarchy;
and a region profile sheet reveals walks and neighborhoods without losing the parent
context. Use white or warm-paper surfaces, black primary data, low-contrast neutral map
dots, restrained photo-derived colors, thin separators, large numeric displays, and
native iOS semantics beneath the custom visual shell. Keep every primary action at least
44×44 pt, ensure the floating tab bar never obscures scroll content, and add textual or
semantic redundancy wherever dot color or density carries meaning.
```

---

## 1. Scope and evidence

### 1.1 Subject

| Field | Value |
|---|---|
| Product | `발자취 - 세상에 나를 남기다` |
| App Store ID | `6792431474` |
| Developer | `Dongnyeok Shin` |
| Bundle ID | `co.nyeok.footage` |
| Surface / route / state | All six public Korean iPhone screenshots in Apple-published order |
| Product type | Walking recorder, geographic collection, badge progress, photo-and-note journal |
| Source platform | iOS / iPhone |
| Target platform | iOS reconstruction baseline |
| Locale | Korean |
| Theme | Light only in public references |
| Analysis purpose | faithful structural analysis + redesign baseline |
| Out of scope | onboarding, active-recording state, permission prompt, weekly/monthly records, settings internals, route detail, photo picker, backup flows, error/empty/loading states, dark mode, source-code verification |

### 1.2 Public app-listing completeness

| Storefront | Platform / device family | Locale | Published assets | Analyzed assets | Missing / inaccessible | Verified |
|---|---|---|---:|---:|---|---:|
| Korea App Store | iPhone / 1320×2868 screenshot family | Korean | 6 | 6 | none | 2026-08-09 |

**Identity check:** `https://apps.apple.com/kr/app/id6792431474` → `발자취 - 세상에 나를 남기다` → `Dongnyeok Shin`  
**Coverage result:** `complete`  

### 1.3 Reference inventory

All six references were retrieved from Apple-hosted full-size public assets in exact App Store order. They were inspected through a short-lived private workflow artifact and are not committed to this public repository.

| Ref ID | Order | Public asset name | Visible surface / state | Viewport | Approx. target frame | SHA-256 | Storage |
|---|---:|---|---|---|---|---|---|
| `REF-01` | 1 | `01-map.png` | Map home — location permission needed, cumulative distance, national dot atlas, Start | 1320×2868 px | 440×956 pt @3× | `85dad3114dfff1176008c4d46d3ace0c109b697e8be5672b487eeb0bdb21a15e` | `link_only` |
| `REF-02` | 2 | `02-timeline.png` | Records — Day selected, achievement card, route map, recorded route row | 1320×2868 px | 440×956 pt @3× | `365babc49c21a390c71a339efe2e6ab75e0d94ffa5445a9fa454982ce0899177` | `link_only` |
| `REF-03` | 3 | `03-badges.png` | Badges — national progress atlas, 136/288, regional badge collection | 1320×2868 px | 440×956 pt @3× | `aa68baffb27107f485a3d51cd2d1571b9a1d11606347a58e39bb7b4a0a86edc7` | `link_only` |
| `REF-04` | 4 | `04-journal.png` | Journal — nationwide atlas landing surface, map action, place search | 1320×2868 px | 440×956 pt @3× | `909f70e9fe76600d5c999876567278e282e93e5a2c32c0b29a690aaae9144097` | `link_only` |
| `REF-05` | 5 | `05-journal-suncheon-selected-note.png` | Journal — Suncheon selected, representative-photo palette, past walk | 1320×2868 px | 440×956 pt @3× | `ff27fa25ee0fb94f59eca06e0d1db12005cfaa560f2b9de50d971d70fc92ebf9` | `link_only` |
| `REF-06` | 6 | `06-suncheon-region-profile-note.png` | Region profile — large modal sheet, metrics, walk cards, neighborhood row | 1320×2868 px | 440×956 pt @3× | `18bdfce1837c7400f4860fc474d4b69278e180946fc1ef2f1de8e3918e1e0488` | `link_only` |

### 1.4 Product facts used to interpret the UI

The official listing describes a user-started walking recorder that stores distance, duration, route, and visited neighborhoods; daily/weekly/monthly summaries; a nationwide dot map and regional badges; optional import of photo locations; representative-photo colors; walking notes; image export; local-first storage; optional private iCloud backup; and no required account, subscription, or in-app purchase. Version 1.1.1 fixes representative-photo updates and adds onboarding dot animation.

These product claims clarify intended semantics but do not override what is visible in the references.

### 1.5 Evidence limitations

- `[U]` Exact font families and variable-font axes are not provable from screenshots.
- `[U]` The exact mapping of neutral, black, and muted-color dots is partly inferred. The listing documents representative-photo colors, but the screenshots contain no legend.
- `[U]` The denominator `288` is visually a finite geographic total, but the exact administrative-level definition is not stated in the screenshot.
- `[U]` Whether the national and local dot atlases are interactive canvases, images, or cached vector/raster renderings is not visible.
- `[U]` Recording, paused, GPS-degraded, permission-denied, completion, and cancellation states are absent.
- `[U]` Weekly and monthly Records layouts are not shown.
- `[U]` The semantics of `전체 지도` in Journal — reset, overview, or alternate presentation — are not directly observable.
- `[U]` The breadcrumb’s truncation and back behavior are not shown.
- `[U]` The region-profile walk cards may form a horizontal rail; only one frame is available.
- `[U]` Dark mode, Dynamic Type, VoiceOver, keyboard, Switch Control, and landscape behavior are not shown.
- `[U]` The App Store statement that accessibility features are not declared does not prove that the app has no accessibility implementation.

### 1.6 Evidence labels

`[O] OBSERVED` · `[M] MEASURED` · `[S] SAMPLED` · `[I] INFERRED` · `[P] PROPOSED` · `[U] UNKNOWN`

---

## 2. Reference overview

### 2.1 `REF-01` — Map home

#### Literal description

```text
A near-white iPhone surface shows a small gray bullet and the text “위치 권한 필요” near
the upper-leading edge. Below it is a very large black number, “487.32,” followed by a
smaller “km” and the stacked gray label “누적.” A pale location-arrow symbol appears near
the upper-trailing edge. The middle of the screen contains a large South Korea silhouette
constructed from evenly spaced circular dots. Most dots are light warm gray; many are
black, forming irregular visited clusters. A large black circular button labeled “시작”
is centered above a floating rounded bottom navigation surface. The bottom surface
contains five equal icon-and-label destinations: 지도, 기록, 배지, 저널, 설정. 지도 is
selected through a light-gray rounded item background.
```

#### Interpretation

- Primary archetype: **recording dashboard** with one dominant action.
- Hero metric: **cumulative distance display**.
- Main visualization: **regular dot-matrix geographic silhouette** / **geographic progress dot field**.
- Primary action: **circular recording start button**.
- Trailing symbol: **current-location / recenter action**, visually disabled or low-emphasis.
- Lower navigation: **custom floating tab bar** preserving tab semantics.
- Inline permission text: **permission status message**, not an alert.

#### Main findings

1. The Start action is unmistakable. A single black circle and large negative space give the recording loop a clear entry point.
2. The large cumulative metric establishes long-term ownership before the user starts today’s walk.
3. The dot atlas is recognizable as Korea at a glance and creates continuity with Badges and Journal.
4. The permission state is too quiet relative to its functional importance. “위치 권한 필요” appears as secondary metadata while Start still looks fully enabled.
5. Black and gray dots have no visible legend. A new user can infer progress but cannot confirm whether black means visited region, recorded route evidence, or another state.
6. The pale location-arrow action risks low contrast and may not read as available.
7. The large empty region between the metric and atlas provides calm, but it omits useful recording context such as last walk, GPS status, or today’s progress.

### 2.2 `REF-02` — Records, Day

#### Literal description

```text
A white screen titled “기록” contains an equal-width three-segment control labeled 일,
주, 월. 일 is selected with a black filled segment and white label; the remaining control
background is light gray. A date row reads “8월 4일 화” with previous and next arrows at
the trailing edge; the next arrow is very pale. A large “8.6 km” metric is followed by
“경로 1개 · 활동 1일 · 1시간 15분.” A rounded pale summary card states “오늘 획득한
성취” and “동네 24곳에 발걸음을 남겼어요,” then presents three miniature dot maps for
괴산군, 평택시, and 용인시 기흥구. A rounded MapKit snapshot with a black route line
follows. Under a divider, “기록된 경로” introduces a route summary row with a tiny route
glyph, date, distance, and disclosure chevron. The floating tab bar overlays the lower
part of the row; 기록 is selected.
```

#### Interpretation

- `일 / 주 / 월`: native-role **segmented control** for related temporal subviews.
- Date arrows: **date pager**.
- `8.6 km`: **daily hero metric**.
- Achievement panel: **disclosure summary card**.
- Three mini maps: **small-multiple geographic glyphs**.
- Map image: **route preview map**.
- Recorded route item: **navigation row / route summary row**.

#### Main findings

1. This is the strongest operational screen in the set. Time scope, date, metric, achievements, route geography, and route detail form a clear top-to-bottom narrative.
2. The segmented control is correctly used for closely related subviews rather than top-level navigation.
3. The achievement card converts abstract movement into collectible place progress and closes the action-reward loop immediately.
4. Three small dot maps plus six lines of labels are dense. Their labels will become difficult at larger text sizes.
5. The MapKit snapshot introduces a second cartographic grammar—roads and black polyline—inside a product otherwise dominated by abstract dot geography. The contrast is useful for route truth, but the transition needs deliberate hierarchy.
6. The pale disabled next arrow is difficult to perceive.
7. The route row is visually occluded by the floating tab bar in the App Store frame. Scroll content requires a safe bottom content inset equal to the bar plus shadow.

### 2.3 `REF-03` — Badges

#### Literal description

```text
A white screen titled “배지” has a trailing ellipsis action. A large national dot atlas
appears below. Most dots are warm gray, many are black, and a small number use muted blue,
green, olive, and brown. Beneath the atlas, the label “발 디딘 지역” precedes a large
“136” and a smaller “/ 288.” A divider separates the top summary from “지역 배지.” The
badge collection is arranged in two columns. Each item contains a miniature regional dot
silhouette, a region name, and a completion summary such as “25 / 25 · 모두 채움” or
“5 / 27 · 22곳 남음.” The floating tab bar overlays the lower items; 배지 is selected.
```

#### Interpretation

- Main map: **geographic progress dot map**.
- `136 / 288`: **finite collection progress count**.
- Region area: **two-column badge collection**.
- Individual items: **badge progress items** containing **miniature geographic progress glyphs**.
- Ellipsis: **overflow menu button**.

#### Main findings

1. The screen presents a finite completion model. `136 / 288` communicates a collectible world more effectively than a generic percentage.
2. Regional silhouettes make each badge spatially specific instead of relying on generic medal artwork.
3. Black, neutral, and photo-derived colors are visually rich but not semantically explained. Muted hues are too small to decode reliably in miniature maps.
4. Two columns use horizontal space efficiently, but long region names and Dynamic Type have little reserve width.
5. Completed and incomplete states are communicated through both text and map fill, which is good; however, no sort/filter/completion view is visible.
6. The top-level atlas closely resembles Map and Journal, reducing destination distinctiveness.
7. Lower badge items sit behind the tab bar in the screenshot, reinforcing the need for a larger scroll content inset.

### 2.4 `REF-04` — Journal, national landing

#### Literal description

```text
A warm off-white screen is titled “저널” with the subtitle “사진과 걸음노트를 남기는
곳.” A horizontal utility row places “전국” at leading and, at trailing, a pale “전체
지도,” a large search symbol, and “장소 찾기.” The middle of the screen contains a large
national dot atlas similar to the Badge map. Neutral, black, and muted photo-derived dots
coexist. The rest of the canvas is mostly empty. The floating tab bar remains fixed at
bottom and 저널 is selected.
```

#### Interpretation

- Primary archetype: **atlas landing surface** for a hierarchical memory journal.
- `전국`: current **scope label**.
- `전체 지도`: probable **overview/reset action**; exact semantics unknown.
- `장소 찾기`: **place search action**.
- Main visualization: **interactive journal dot atlas**.

#### Main findings

1. The warm-paper surface successfully separates reflective memory work from the white operational Map/Records/Badges shell.
2. The national atlas is treated as the journal’s primary object rather than a decorative header.
3. The screen is extremely sparse. The map has no explicit instruction, current selection, recent memory, or progress sentence.
4. `전체 지도` is very low contrast and may appear disabled even if interactive.
5. Search is visually split into a large magnifier and separate label, but the exact combined hit target is unclear.
6. Map, Badge, and Journal all lead with nearly the same Korea silhouette. Their intended verbs—record, complete, remember—need stronger surface-specific framing.

### 2.5 `REF-05` — Journal, Suncheon selected

#### Literal description

```text
A warm off-white screen begins with the long breadcrumb “전국 / 전남광주통합특별시 /
순천시.” At trailing are “전체 지도,” a search symbol, and “장소 찾기.” A large local dot
map fills the upper half. Most points are extremely pale. A small cluster of colored and
dark points is selected near the lower-left of the map; a thin vertical leader line runs
down to a small endpoint and the label “순천시,” followed by the parent region name. A
row labeled “지역 대표사진” and “설정됨” contains a square diagonally split purple-and-
rose palette tile and a disclosure chevron. A divider introduces “지난 걸음 2” and “전체
보기.” One past-walk row contains a map thumbnail, date, and a truncated walking-note
excerpt. The floating tab bar remains visible with 저널 selected.
```

#### Interpretation

- Top text: **hierarchical breadcrumb**.
- Local atlas: **administrative-area dot field**.
- Selected cluster: **leader-line selection annotation** / **lollipop callout**.
- Representative-photo row: **disclosure row**.
- Diagonal square: **representative-photo palette swatch**, not a chart.
- Past walk item: **compact journal entry row**.

#### Main findings

1. The leader line gives the abstract selected cluster a precise relationship to its place label without adding a map pin.
2. The same dot grammar scales from national to local administrative geography.
3. The breadcrumb is too long for compact-width localization and Dynamic Type. It should not be the only back-navigation mechanism.
4. The local map is intentionally quiet, but its unselected dots are so faint that the geographic silhouette nearly disappears.
5. The selected cluster uses color plus darkness; explicit selected outline, halo, or label state would improve clarity.
6. The representative-photo palette tile is a concise abstraction of memory color, but its square shape differs from the circular swatch in the profile sheet without an obvious semantic reason.
7. The past-walk section has only one visible compact row and leaves substantial unused space; the screen could surface a note, recent photo, or coverage summary without becoming card-heavy.

### 2.6 `REF-06` — Region profile sheet

#### Literal description

```text
A dimmed parent screen remains visible above and around a nearly full-height white sheet
with large rounded upper corners. A circular white close control with an X floats near the
upper-trailing corner and casts a soft shadow. The profile header combines a pale local
dot silhouette, a dark visited cluster, the title “순천시,” its parent region, a circular
diagonally split purple-and-rose palette swatch, and three metrics: 1 걸음, 0 방문일,
1 걸음노트. A divider introduces “지난 걸음” and the summary “걸음 2 · 방문 2일 ·
걸음노트 1.” A horizontal sequence of route-memory cards follows. The leading card uses
a large MapKit snapshot with a black route and a centered walking-note sentence over a
dark scrim; metadata and “걸음노트 보기” appear below. A second narrower card is partially
visible with “걸음노트 남기기.” A divider introduces “동네.” A disclosure row for
외서면 includes walk count, recent date, representative-photo status, and a chevron.
```

#### Interpretation

- Presentation: **large modal sheet** / **region profile sheet**.
- Header visual: **region dot-map summary**.
- Circular color mark: **representative-photo palette medallion**, not a pie chart.
- Three values: **summary metric row**.
- Walk cards: probable **horizontal content rail**.
- Main card: **route memory card** with **text-legibility scrim**.
- Neighborhood item: **navigation row with disclosure indicator**.

#### Main findings

1. The sheet is the most complete expression of the product thesis: geography, representative color, quantitative history, route evidence, narrative note, and lower administrative hierarchy coexist in one place profile.
2. Preserving a dimmed parent context makes the region feel selected from the atlas rather than opened as an unrelated screen.
3. The close control is visually louder than necessary because of its large white circle and shadow.
4. The metric row is clear, but `걸음 1` conflicts visually with the later summary `걸음 2`; the terms may refer to different scopes, yet the UI does not explain the distinction.
5. The leading walk card’s note overlay competes with map labels and route geometry. A consistent scrim or dedicated text region is needed.
6. The second card is narrow and partially visible, suggesting a content rail. Card width and snapping behavior should be explicit.
7. The circular palette medallion and square palette tile need one documented shape rule.
8. The neighborhood row is structurally clear and provides the next drill-down level without exposing another full map immediately.

---

## 3. Interface archetype and product loop

### 3.1 Archetype classification

| Field | Classification | Authority | Evidence | Confidence |
|---|---|---|---|---:|
| Primary archetype | Walking-recording utility | `INDUSTRY_CONVENTIONAL` | Start control, cumulative distance, route records | 1.00 |
| Secondary archetype | Geographic collection / completion tracker | `INDUSTRY_CONVENTIONAL` | 136/288 progress and regional badges | 0.99 |
| Memory archetype | Hierarchical place journal | `INDUSTRY_CONVENTIONAL` | photo palette, walking notes, region/neighborhood drill-down | 0.99 |
| Data domain | Personal informatics | `RESEARCH_PRACTICE` | personal movement transformed into longitudinal metrics and recall surfaces | 0.98 |
| Navigation model | Five persistent top-level destinations | `PLATFORM_OFFICIAL` mapping | floating tab bar with five items | 1.00 |
| Spatial model | country → region → city/county → neighborhood | product model | national, regional, Suncheon, Oeseo-myeon views | 0.97 |
| Storage model | local-first with optional private iCloud backup | product claim | App Store description | 1.00 |

### 3.2 Core loop

```text
Grant location access
→ start a walk
→ record route, distance, duration, and visited administrative cells
→ receive same-day region and neighborhood achievements
→ review day/week/month records and route truth
→ accumulate finite regional badges
→ attach representative-photo colors and walking notes
→ revisit memories by national atlas, region profile, and neighborhood hierarchy
→ start another walk
```

### 3.3 Strongest product asset

The strongest asset is not one screen. It is the **same geographic dot unit reused across six roles**:

1. live accumulation on Map;
2. same-day achievement evidence in Records;
3. completion progress in Badges;
4. national memory overview in Journal;
5. selected local geography in Journal detail;
6. identity and context in the region profile sheet.

This creates a coherent visual data model: location evidence becomes progress, collection, color, and memory without changing visual grammar.

### 3.4 Main information-architecture tension

Map, Badges, and Journal are separate top-level destinations, but their primary silhouette is nearly identical. Their verbs are different:

- **Map:** start and monitor movement;
- **Badges:** understand completion and remaining coverage;
- **Journal:** recall photos, notes, and place history.

The screen shells need stronger task-specific framing so the user does not perceive three versions of the same atlas.

### 3.5 Reading-order hierarchy

#### Map

1. cumulative distance;
2. national progress atlas;
3. Start control;
4. permission state;
5. tab bar.

#### Records

1. daily distance;
2. achievement statement;
3. route map;
4. date and temporal scope;
5. route list.

#### Badges

1. national progress atlas;
2. 136/288 completion count;
3. regional collection items.

#### Journal

1. geographic atlas or selected region;
2. place identity;
3. photo palette and past walks;
4. search/scope controls.

#### Region profile

1. place title and dot silhouette;
2. representative color and metrics;
3. route memory cards;
4. neighborhood hierarchy.

---

## 4. Terminology normalization summary

| Raw description | Canonical term | Authority class | Platform scope | Why this term fits |
|---|---|---|---|---|
| “아래 떠 있는 5개 메뉴” | tab bar with custom floating treatment | `PLATFORM_OFFICIAL` + `PROJECT_DEFINED` appearance | iOS | five persistent destinations switch top-level app sections |
| “선택된 탭 뒤 회색 알약” | selected tab item background / selection capsule | `PROJECT_DEFINED` | app visual system | visual selection treatment inside one tab item |
| “일·주·월 선택” | segmented control | `PLATFORM_OFFICIAL` | iOS | mutually exclusive, closely related temporal subviews |
| “487.32km 큰 숫자” | cumulative-distance hero metric | `INDUSTRY_CONVENTIONAL` | cross-platform | one value dominates hierarchy and summarizes longitudinal activity |
| “한국 지도 점들” | regular dot-matrix geographic silhouette | `INDUSTRY_CONVENTIONAL` | cross-platform | uniform dots are clipped or sampled to geographic geometry |
| “점 지도” | geographic progress dot field | `PROJECT_DEFINED` | app data grammar | dot states encode personal coverage over a geographic base |
| “도트 밀도 지도” | rejected: dot-density map | cartographic term | cross-platform | each dot does not visibly represent a fixed population or quantity |
| “행정구역 색칠 지도” | rejected: choropleth | cartographic term | cross-platform | polygons are not filled by value; discrete grid dots are used |
| “열지도” | rejected: heatmap | visualization term | cross-platform | no continuous density field or color-gradient surface is present |
| “시작 동그라미” | circular primary action button | `PLATFORM_OFFICIAL` role + custom appearance | iOS | immediately starts the core recording action |
| “위치 화살표” | current-location / recenter button | `PLATFORM_OFFICIAL` mapping | map interfaces | moves or recenters the spatial view to the user |
| “위치 권한 필요” | inline permission status message | `INDUSTRY_CONVENTIONAL` | cross-platform | reports prerequisite state without presenting a modal alert |
| “오늘 성취 카드” | disclosure summary card | `INDUSTRY_CONVENTIONAL` | cross-platform | groups a summary, mini visualizations, and subordinate navigation |
| “작은 행정지도 세 개” | small-multiple geographic glyphs | visualization practice | cross-platform | repeated maps use identical grammar to compare distinct places |
| “경로가 그려진 지도” | route preview map | `PLATFORM_OFFICIAL` map role | iOS / MapKit | spatial snapshot provides route truth and context |
| “136/288” | finite collection progress count | `INDUSTRY_CONVENTIONAL` | cross-platform | numerator and denominator communicate accumulated coverage |
| “지역 배지 두 줄” | two-column badge collection | `INDUSTRY_CONVENTIONAL` | cross-platform | repeated region items are arranged in a fixed two-column grid |
| “전국/…/순천시” | breadcrumb | `INDUSTRY_CONVENTIONAL` | cross-platform | text exposes a hierarchical path to the current location |
| “선택된 점에서 내려오는 선” | leader-line selection annotation / lollipop callout | visualization practice | cross-platform | a line explicitly connects selected geometry to its label |
| “대표사진 보라·분홍 네모” | representative-photo palette swatch | `PROJECT_DEFINED` | app visual system | color abstraction represents a photo-derived identity, not quantity |
| “보라·분홍 원” | representative-photo palette medallion | `PROJECT_DEFINED` | app visual system | circular profile identity treatment of the same palette |
| “파이 차트” | rejected: pie chart | visualization term | cross-platform | split colors have no quantitative labels or part-to-whole semantics |
| “위에서 둥근 지역 화면” | large modal sheet / region profile sheet | `PLATFORM_OFFICIAL` + project role | iOS | modal surface preserves dimmed parent context and shows a bounded profile |
| “지난 걸음 카드 줄” | horizontal content rail | `INDUSTRY_CONVENTIONAL` | cross-platform | one full card and a partial next card imply horizontal continuation |
| “동네 한 줄” | navigation row with disclosure indicator | `PLATFORM_OFFICIAL` mapping | iOS | row opens a lower administrative level |

### 4.1 Style classification

| Field | Value |
|---|---|
| Primary project label | **Quiet Dot-Atlas Lifelog** |
| Authority | `PROJECT_DEFINED` |
| Definition | a location lifelog interface that uses repeated regular geographic dot fields, warm-neutral surfaces, large numeric hierarchy, restrained photo-derived colors, and low-chrome iOS controls to turn movement into collection and memory |
| Underlying terms | low-chrome utility UI, editorial data minimalism, personal informatics, dot-matrix cartography, collectible geography, calm technology |
| Observable traits | white operational canvas; warm journal canvas; black primary data; light warm-gray base dots; muted green/blue/brown/purple/rose memory colors; thin sans typography; large metrics; sparse rounded cards; pill tab bar; minimal ornament |
| Secondary influence | atlas/index pages, pointillist geographic graphics, field journal, activity summary dashboard |
| Labels rejected | heatmap, dot-density map, choropleth, game map, glassmorphism, skeuomorphism, neumorphism, bento dashboard |
| Rejection reasons | discrete equal grid dots rather than continuous or polygon fills; no game-world camera or resources; no material imitation; no card mosaic; only the navigation surface uses a floating translucent/opaque pill treatment |

---

## 5. Frame, geometry, and layout system

### 5.1 Coordinate calibration

| Field | Value |
|---|---|
| Source viewport | 1320×2868 px for all six references |
| Exact scale candidate | 3 source px per target pt |
| Target viewport | 440×956 pt |
| Origin | top-left |
| Confidence | 1.00 for mathematical conversion; device model remains unspecified |
| Caveat | screenshot dimensions establish the rendered frame, not runtime safe-area API values |

### 5.2 Shared main-surface shell (`REF-01`–`REF-05`)

| Region | Approx. target bounds | Role | Rebuild rule |
|---|---:|---|---|
| System status region | y `0–54 pt` | system chrome | system-owned |
| Page header / utility area | y `54–160 pt`, screen-dependent | title, scope, controls | 16 pt leading/trailing anchors; 44 pt action targets |
| Main visualization/content | y `150–850 pt` | atlas, records, badge collection | scroll or canvas per surface |
| Floating tab bar | x `16 pt`, y `858–938 pt`, w `408 pt`, h `72–80 pt` incl. visual surface | top-level navigation | safe-area aware; content inset ≥ bar + shadow |
| Bottom safe region | approx. `18 pt` | home-indicator accommodation | system-owned |

### 5.3 Shared dimensions

| Token candidate | Observed range | Proposed semantic value |
|---|---:|---:|
| `space.inline.page` | 15–18 pt | 16 pt |
| `space.stack.section` | 22–32 pt | 24 pt / 32 pt major |
| `size.control.hitMinimum` | some visible glyphs < 44 pt | 44 pt interaction region |
| `size.tabBar.height` | approx. 72 pt | 72 pt + safe-area placement |
| `radius.tabBar.container` | approx. 36 pt | capsule |
| `radius.card.summary` | approx. 18–22 pt | 20 pt |
| `radius.map.preview` | approx. 14–18 pt | 16 pt |
| `stroke.divider` | 1–2 source px | 1 device pixel |
| `dot.atlas.diameter` | approx. 7–9 source px | 2.5–3 pt |
| `dot.atlas.pitch` | approx. 13–15 source px | 4.5–5 pt |
| `size.action.record` | approx. 90–94 pt diameter | 92 pt visual; ≥92 pt hit |

### 5.4 Screen-specific geometry

#### Map

- Permission label and cumulative metric align to the 16 pt page inset.
- Large atlas occupies approximately 230×390 pt and is vertically centered in the content field.
- Start button is centered horizontally around y 785 pt.
- The current-location action appears in a 44 pt trailing region but its visible glyph is much smaller.

#### Records

- Segmented control: x 16 pt, width approximately 408 pt, height approximately 44 pt.
- Achievement card: x 16 pt, width approximately 408 pt, radius approximately 20 pt.
- Route preview map: x 16 pt, width approximately 408 pt, height approximately 175–185 pt.
- Bottom route row begins beneath the section title but is partially covered by the tab bar.

#### Badges

- National atlas occupies approximately 235×365 pt.
- Region collection uses two equal tracks with approximately 16 pt outer insets and 16–20 pt inter-column gap.
- Badge item vertical rhythm is approximately 100–112 pt.

#### Journal

- Warm root canvas: approximately `#F8F6F3`.
- National atlas remains centered but has even more surrounding negative space than Map or Badges.
- Selected local atlas in `REF-05` uses a leader line of approximately 160–190 pt.

#### Region profile sheet

- Dimmed parent remains visible above the sheet.
- Sheet begins around y 60 pt with upper radius approximately 32–36 pt.
- Close control visual diameter approximately 44–48 pt; target must remain at least 44×44 pt.
- Header, metric row, walk rail, and neighborhood section share a 24 pt body inset.

### 5.5 Layering and z-order

```text
Main screens:
root canvas
→ geographic/content layer
→ local selection or route overlays
→ page controls
→ floating tab bar and shadow

Region profile:
dimmed parent
→ large sheet surface
→ profile header/content
→ floating close button
```

---

## 6. Element inventory

| ID | Ref | Literal observation | Canonical term | Authority | Role | Evidence | Confidence |
|---|---|---|---|---|---|---|---:|
| `SYS-01` | all | iPhone status region | system status bar | `PLATFORM_OFFICIAL` | system chrome | `[O]` | 1.00 |
| `NAV-01` | 01–05 | floating white capsule with five destinations | tab bar with custom floating treatment | `PLATFORM_OFFICIAL` + `PROJECT_DEFINED` | primary navigation | `[O]` | 1.00 |
| `NAV-02` | 01–05 | light-gray rounded background behind active item | selected tab item background | `PROJECT_DEFINED` | selection state | `[O]` | 1.00 |
| `TXT-01` | 01 | bullet plus “위치 권한 필요” | permission status message | `INDUSTRY_CONVENTIONAL` | prerequisite feedback | `[O]` | 1.00 |
| `DAT-01` | 01 | “487.32 km 누적” | cumulative-distance hero metric | `INDUSTRY_CONVENTIONAL` | longitudinal summary | `[O]` | 1.00 |
| `ACT-01` | 01 | pale location arrow | current-location / recenter button | `PLATFORM_OFFICIAL` mapping | spatial action | `[O/I]` | 0.82 |
| `DAT-02` | 01 | national neutral/black dot silhouette | geographic progress dot field | `PROJECT_DEFINED` | cumulative coverage | `[O/I]` | 0.94 |
| `ACT-02` | 01 | black circle labeled 시작 | circular primary action button | `PLATFORM_OFFICIAL` role | start recording | `[O]` | 1.00 |
| `TXT-02` | 02 | “기록” | screen title | `PLATFORM_OFFICIAL` mapping | page identity | `[O]` | 1.00 |
| `NAV-03` | 02 | 일/주/월 equal segments | segmented control | `PLATFORM_OFFICIAL` | temporal subview selection | `[O]` | 1.00 |
| `ACT-03` | 02 | previous and next date arrows | date pager | `INDUSTRY_CONVENTIONAL` | date navigation | `[O/I]` | 0.98 |
| `DAT-03` | 02 | “8.6 km” | daily-distance hero metric | `INDUSTRY_CONVENTIONAL` | daily summary | `[O]` | 1.00 |
| `GRP-01` | 02 | rounded achievement panel | disclosure summary card | `INDUSTRY_CONVENTIONAL` | reward summary | `[O/I]` | 0.97 |
| `DAT-04` | 02 | three miniature dot maps | small-multiple geographic glyphs | `RESEARCH_PRACTICE` / conventional | acquired-place evidence | `[O]` | 0.99 |
| `DAT-05` | 02 | rounded MapKit snapshot and black route | route preview map | `PLATFORM_OFFICIAL` map role | spatial route truth | `[O]` | 1.00 |
| `GRP-02` | 02 | recorded-route section | route collection | `INDUSTRY_CONVENTIONAL` | history | `[O]` | 0.99 |
| `ROW-01` | 02 | route glyph, date, 8.64km, chevron | route summary navigation row | `PLATFORM_OFFICIAL` mapping | route detail entry | `[O/I]` | 0.97 |
| `TXT-03` | 03 | “배지” | screen title | `PLATFORM_OFFICIAL` mapping | page identity | `[O]` | 1.00 |
| `ACT-04` | 03 | trailing ellipsis | overflow menu button | `PLATFORM_OFFICIAL` | secondary actions | `[O]` | 1.00 |
| `DAT-06` | 03 | national neutral/black/color atlas | geographic badge progress map | `PROJECT_DEFINED` | collection overview | `[O/I]` | 0.96 |
| `DAT-07` | 03 | “136 / 288” | finite collection progress count | `INDUSTRY_CONVENTIONAL` | progress | `[O]` | 1.00 |
| `GRP-03` | 03 | two-column region area | two-column badge collection | `INDUSTRY_CONVENTIONAL` | regional progress browsing | `[O]` | 1.00 |
| `ROW-02` | 03 | mini region map, name, fraction | badge progress item | `PROJECT_DEFINED` | one regional collection unit | `[O]` | 1.00 |
| `TXT-04` | 04 | “저널” + subtitle | title and explanatory subtitle | `PLATFORM_OFFICIAL` mapping | journal identity | `[O]` | 1.00 |
| `NAV-04` | 04 | 전국 / 전체 지도 / 검색 / 장소 찾기 row | scope and utility toolbar | `INDUSTRY_CONVENTIONAL` | journal navigation | `[O/I]` | 0.90 |
| `ACT-05` | 04–05 | “전체 지도” | overview/reset action | `INDUSTRY_CONVENTIONAL` | scope control | `[O/U]` | 0.62 |
| `ACT-06` | 04–05 | magnifier + 장소 찾기 | place search action | `PLATFORM_OFFICIAL` mapping | search | `[O]` | 0.99 |
| `DAT-08` | 04 | national colored atlas | interactive journal dot atlas | `PROJECT_DEFINED` | national memory navigation | `[O/I]` | 0.94 |
| `NAV-05` | 05 | nationwide / parent / city path | breadcrumb | `INDUSTRY_CONVENTIONAL` | hierarchy context | `[O]` | 1.00 |
| `DAT-09` | 05 | very pale local region dot map | administrative-area dot field | `PROJECT_DEFINED` | local geography | `[O]` | 1.00 |
| `DAT-10` | 05 | selected cluster with vertical line | leader-line selection annotation | `RESEARCH_PRACTICE` / conventional | selection and label linkage | `[O]` | 1.00 |
| `ROW-03` | 05 | 지역 대표사진 / 설정됨 / swatch / chevron | representative-photo disclosure row | `PLATFORM_OFFICIAL` mapping | photo identity editing | `[O/I]` | 0.98 |
| `DEC-01` | 05 | diagonal purple/rose square | representative-photo palette swatch | `PROJECT_DEFINED` | memory color identity | `[O/I]` | 0.94 |
| `GRP-04` | 05 | 지난 걸음 2 / 전체 보기 | past-walk section | `INDUSTRY_CONVENTIONAL` | journal history | `[O]` | 1.00 |
| `ROW-04` | 05 | map thumbnail, date, note excerpt | compact journal entry row | `INDUSTRY_CONVENTIONAL` | past walk entry | `[O/I]` | 0.98 |
| `OVR-01` | 06 | almost full-height rounded white surface | large modal sheet | `PLATFORM_OFFICIAL` | region profile presentation | `[O]` | 1.00 |
| `ACT-07` | 06 | circular X | close button | `PLATFORM_OFFICIAL` | dismiss sheet | `[O]` | 1.00 |
| `DAT-11` | 06 | region silhouette with visited cluster | region-profile dot map | `PROJECT_DEFINED` | place identity | `[O]` | 1.00 |
| `DEC-02` | 06 | diagonal purple/rose circle | representative-photo palette medallion | `PROJECT_DEFINED` | profile color identity | `[O/I]` | 0.94 |
| `GRP-05` | 06 | 1 걸음 / 0 방문일 / 1 걸음노트 | summary metric row | `INDUSTRY_CONVENTIONAL` | place summary | `[O]` | 1.00 |
| `GRP-06` | 06 | full route card + partial next card | horizontal content rail | `INDUSTRY_CONVENTIONAL` | past walk browsing | `[O/I]` | 0.90 |
| `ROW-05` | 06 | map route image, note, metadata, action | route memory card | `PROJECT_DEFINED` | narrative walk memory | `[O/I]` | 0.98 |
| `GRP-07` | 06 | 동네 section | neighborhood collection | `INDUSTRY_CONVENTIONAL` | lower-level hierarchy | `[O]` | 1.00 |
| `ROW-06` | 06 | 외서면, metadata, chevron | neighborhood disclosure row | `PLATFORM_OFFICIAL` mapping | neighborhood detail entry | `[O/I]` | 0.99 |

### 6.1 Detailed specification — geographic dot field

**Anatomy**

- regular circular cells;
- fixed geographic sampling positions;
- neutral base state;
- dark coverage state;
- optional muted photo-derived color state;
- clipped country or administrative-area silhouette;
- separate title, count, or selection label outside the map.

**Rebuild directive**

```text
Precompute stable geographic dot positions from administrative geometry. Render all
visible cells at a consistent 2.5–3 pt diameter on a 4.5–5 pt pitch at the 440 pt
reference width. Use neutral warm gray for the base, black for the product-defined
coverage state, and muted photo-derived colors only after the underlying meaning is
confirmed. Keep selection independent of color by adding an outline, scale change,
leader line, or explicit selected state. Do not vary dot area by count and do not call
the result a heatmap, choropleth, or dot-density map.
```

### 6.2 Detailed specification — floating tab bar

**Anatomy**

- one floating pill container;
- five equal item cells;
- icon above label;
- selected item background contained inside the pill;
- strong soft shadow below the whole surface.

**Rebuild directive**

```text
Preserve native tab semantics and five persistent destinations. Position the custom
visual surface 16 pt from the horizontal edges and above the bottom safe area. Use a
72 pt visual height and at least a 44×44 pt target for every item. Add scroll-content
bottom inset equal to the complete bar, safe area, and shadow. Selected state must include
both semantic selection and a visible background/weight change. Reduce shadow before
reducing label contrast.
```

### 6.3 Detailed specification — Records achievement card

```text
Use one 408 pt-wide summary card with 20 pt radius. Keep the achievement statement as the
primary content, followed by at most three equal small-multiple maps. Each place glyph is
a single accessibility group with region name and achievement type. At larger text sizes,
move the three items to a vertical list or horizontal scroll rather than shrinking labels.
```

### 6.4 Detailed specification — Journal selection

```text
The selected administrative cell group remains inside the dot field. Connect it to the
place label using a 1 device-pixel leader line and a small terminal marker. Add a selected
outline or contrast adjustment so the cluster is not identified by color alone. Replace
the full breadcrumb at compact widths with a standard back control, current title, and a
secondary parent label; preserve the complete path in accessibility metadata or a
subordinate breadcrumb when space allows.
```

### 6.5 Detailed specification — region profile sheet

```text
Present the profile as a large sheet with parent context dimmed behind it. Keep the close
button inside a 44×44 pt target and reduce decorative shadow. Group the header map, title,
parent region, representative palette, and metrics into one clear profile block. Use a
horizontal walk rail only when multiple entries exist; choose one card-width rule and
show a deliberate next-card peek. Apply a stable scrim behind overlaid notes, and preserve
route, date, distance, duration, place, and note actions as native text.
```

---

## 7. Navigation and interaction model

### 7.1 Top-level navigation

| Destination | Primary verb | Primary object | Visible differentiation |
|---|---|---|---|
| 지도 | start / monitor | current and cumulative walking | hero distance + Start |
| 기록 | review by time | day/week/month activity | segmented control + route evidence |
| 배지 | complete / collect | finite administrative coverage | 136/288 + regional grid |
| 저널 | remember / annotate | photos, notes, place hierarchy | warm paper + searchable atlas |
| 설정 | configure | app, privacy, backup | not shown |

Five destinations are within Apple’s compact tab-count guidance, but the three geography-led tabs need stronger task distinction.

### 7.2 Secondary navigation

- Records uses a segmented control for Day / Week / Month.
- Date arrows page through the selected time scope.
- Achievement card and route rows appear navigable through chevrons.
- Journal uses national-to-local drill-down and place search.
- Region profile is modal and then reveals neighborhood rows.

### 7.3 Control semantics

| Element | Generic role | Target iOS component | Trigger | Result |
|---|---|---|---|---|
| `NAV-01` | primary tabs | `TabView` / `UITabBarController` semantics with custom surface | tap | change top-level destination |
| `ACT-02` | primary action | `Button` | tap | request permission or start walk |
| `NAV-03` | single-selection segmented control | `Picker(.segmented)` / `UISegmentedControl` | tap | change temporal subview |
| `ACT-03` | pager buttons | `Button` pair | tap | previous/next date |
| `GRP-01` | disclosure summary | `Button` / `NavigationLink` | tap | open achievements |
| `ROW-01` | route navigation row | `NavigationLink` | tap | open route detail |
| `ACT-04` | overflow menu | `Menu` | tap | secondary badge actions |
| `ACT-06` | search | searchable route/sheet | tap | search places |
| `ROW-03` | disclosure row | `NavigationLink` / sheet | tap | choose representative photo |
| `ROW-04` | journal entry | `NavigationLink` | tap | open walk memory |
| `ACT-07` | dismiss | sheet close `Button` | tap | return to journal context |
| `ROW-06` | neighborhood row | `NavigationLink` | tap | drill into neighborhood |

### 7.4 Required state behavior

#### Walk recording

- permission unknown / denied / restricted / allowed;
- ready;
- acquiring location;
- recording;
- auto-paused because of speed or signal instability;
- manually paused;
- ending and saving;
- save failure / partial recovery.

The Start control must not look fully ready while permission is unavailable. Tapping it may initiate the permission flow, but the label and status need to reflect that prerequisite.

#### Atlas selection

- no selection;
- focused/hovered where applicable;
- selected;
- loading region data;
- region with no walks;
- region with walk data but no representative photo;
- region with representative photo color;
- unavailable geometry.

#### Journal profile

- sheet opening/dismissal;
- one walk vs many walks;
- no note / one note / multiple notes;
- no neighborhoods;
- missing local photo reference;
- iCloud restore pending.

---

## 8. Typography

### 8.1 Type system summary

| Role | Screens | Classification | Approx. target size | Weight | Notes |
|---|---|---|---:|---|---|
| cumulative metric | Map | system sans numeric | 50–54 pt | light/regular | large decimal with small unit stack |
| daily metric | Records | system sans numeric | 46–50 pt | light/regular | `8.6 km` |
| screen title | Records/Badges/Journal | system Korean sans | 18–20 pt | regular/semibold | leading aligned |
| profile title | region profile | system Korean sans | 24–28 pt | regular/semibold | strongest text in sheet header |
| section heading | all | system Korean sans | 16–18 pt | regular/semibold | `지역 배지`, `지난 걸음`, `동네` |
| body | cards/rows | system Korean sans | 15–17 pt | regular | primary descriptive content |
| metadata | all | system Korean sans | 12–14 pt | regular | warm gray |
| tab label | tab bar | system Korean sans | 11–12 pt | regular/medium | icon above label |

### 8.2 Typographic behavior

- Large metrics use size and isolation rather than bold weight.
- Units and qualifiers are smaller and aligned beside the numeric baseline.
- Korean labels are generally short, which allows five tab labels to fit.
- Region names can become long; `전남광주통합특별시` already demonstrates pressure.
- Several metadata colors and the disabled next arrow are too faint for reliable reading.
- Exact font family remains unknown; system Korean sans is the safest reconstruction baseline.

### 8.3 Dynamic Type requirements

- Do not scale the five-item tab bar by shrinking labels below legibility; allow icon/label adaptation or system tab behavior.
- Badge collection changes from two columns to one at accessibility sizes.
- Achievement small multiples reflow vertically or horizontally.
- Breadcrumb becomes back + title + parent metadata.
- Profile metrics can wrap into two rows.
- Journal entry excerpts permit two to three lines and must not be baked into images.
- The large numeric display may use a capped display role while surrounding labels scale semantically.

### 8.4 Proposed type tokens

| Token | Proposed value |
|---|---|
| `type.metric.cumulative` | 52 pt regular, tabular numerals |
| `type.metric.daily` | 48 pt regular, tabular numerals |
| `type.title.screen` | 19 pt semibold/regular |
| `type.title.profile` | 26 pt semibold |
| `type.heading.section` | 17 pt semibold |
| `type.body.primary` | 16 pt regular |
| `type.meta` | 13 pt regular |
| `type.tab.label` | 11 pt medium |

---

## 9. Color, material, shape, and elevation

### 9.1 Palette

Values are sampled or reconstructed from compressed public assets and require production calibration.

| Token | Approx. value | Role | Evidence |
|---|---|---|---|
| `color.background.operational` | `#FDFCFC` | Map, Records, Badges canvas | `[S]` |
| `color.background.journal` | `#F8F6F3` | Journal canvas | `[S]` |
| `color.surface.card` | `#F8F6F5` | achievement card | `[S]` |
| `color.surface.navigation` | near `#FFFDFC` | floating tab bar and sheet | `[S]` |
| `color.surface.selection` | near `#ECEBEA` | selected tab item | `[S]` |
| `color.text.primary` | near `#111111` | primary labels and metrics | `[S]` |
| `color.text.secondary` | warm gray near `#8E8983` | metadata | `[S/P]` |
| `color.dot.base` | near `#D6D1CB` | neutral geographic cells | `[S]` |
| `color.dot.covered` | near `#050505` | dark coverage state | `[S/I]` |
| `color.palette.purple` | near `#A487AD` | representative-photo palette | `[S]` |
| `color.palette.rose` | near `#D0ABB5` | representative-photo palette | `[S]` |
| `color.palette.olive` | muted olive | photo-derived dots | `[S/I]` |
| `color.palette.blue` | muted blue-gray | photo-derived dots | `[S/I]` |
| `color.palette.brown` | muted brown | photo-derived dots | `[S/I]` |
| `color.divider` | warm light gray | section separation | `[S/P]` |

### 9.2 Surface hierarchy

| Surface | Treatment | Role |
|---|---|---|
| operational root | near-white, flat | data and recording utility |
| journal root | warm paper-like off-white, flat | reflective memory context |
| summary card | slightly warmer raised fill, no heavy border | groups reward content |
| route map | image/map surface with rounded mask | spatial evidence |
| floating tab bar | opaque/light surface, strong soft shadow | persistent navigation |
| region sheet | white surface, dimmed parent, large top radius | modal place profile |
| close control | white circular surface with shadow | dismissal |

### 9.3 Shape language

- Circles: dots, Start control, palette medallion, close control.
- Capsules: segmented control and floating tab bar.
- Rounded rectangles: achievement card, route preview, palette tile, walk cards.
- Hairline dividers: section boundaries.
- No decorative gradients except functional image scrims.
- No broad glass material is visible; the tab bar reads as a custom opaque/soft-elevation surface.

### 9.4 Consistency issue

The same representative-photo identity appears as a diagonal **square** swatch in Journal detail and a diagonal **circle** medallion in the profile sheet. This can be intentional if square means editable asset and circle means profile identity, but the rule must be documented and applied consistently.

---

## 10. Cartography and data encoding

### 10.1 Visual-variable mapping

| Visual variable | Encoded data | Current interpretation | Missing / zero | Risk |
|---|---|---|---|---|
| geographic position | administrative sampling cell | fixed dot location inside region geometry | cell absent outside geometry | geometry precision at small scale |
| neutral dot | base geography | unvisited/unfilled inferred | dominant base state | semantics not labeled |
| black dot | accumulated coverage | visited/attained inferred | none | binary meaning not documented in UI |
| muted color | representative-photo memory | photo-derived color documented | black or neutral fallback inferred | color-only meaning and low distinguishability |
| count `136/288` | finite regional coverage | visited/available regions | zero/complete states | denominator definition not visible |
| miniature silhouette | regional identity | administrative boundary raster | empty map | too small for fine distinctions |
| leader line | selection relationship | selected cluster → place label | no selection | line can become too faint |
| route polyline | actual recorded path | MapKit route truth | no route | competes with map labels |
| palette swatch | representative photo color identity | nonquantitative photo abstraction | unset state | can be mistaken for chart |

### 10.2 Classification

The core atlas is best described as:

> **A regular-grid geographic dot matrix clipped or sampled by administrative polygons, with categorical occupancy/color states.**

It is not:

- a dot-density map;
- a choropleth;
- a heatmap;
- a proportional-symbol map;
- a route map.

### 10.3 Small multiples

The Records achievement card and Badge collection use **small multiples**: repeated maps with the same visual grammar and scale logic. This supports comparison, but miniature versions must simplify geometry and increase semantic labeling rather than merely shrinking the full map.

### 10.4 Selection and semantic zoom

#### National view

- neutral base geography;
- covered cells;
- photo-derived cells;
- selected region outline or emphasis;
- optional summary legend.

#### Region view

- larger dot pitch or greater map scale;
- selected city/county cluster;
- leader line and title;
- parent region context.

#### Neighborhood view

- do not continue shrinking the same national dot pitch indefinitely;
- switch to a local layout or higher-detail cell grammar where necessary.

### 10.5 Performance reconstruction

- Precompute country, region, city/county, and neighborhood dot masks offline.
- Use stable IDs for cells and administrative entities.
- Cache miniature badge glyphs and national/region snapshots.
- Render large atlases in `Canvas`, Metal only if profiling demonstrates need.
- Keep screen-reader semantics at summary/region level rather than exposing hundreds of individual dots.
- Separate geometric state from photo-color decoration.

### 10.6 Required legend

A compact legend or first-use explanation should define the product’s actual states, for example:

```text
회색: 아직 발 디디지 않은 곳
검정: 걸음으로 기록한 곳
색상: 대표사진의 기억색이 연결된 곳
```

The final labels must match production data semantics; the above is a proposed interpretation.

---

## 11. Motion and temporal behavior

Static screenshots do not establish animation. Version notes document an onboarding dot animation only.

| Transition | Trigger | Proposed behavior | Evidence |
|---|---|---|---|
| Start press | tap Start | pressed state, permission/location acquisition feedback, then recording state | `[P]` |
| Dot acquisition | new region/neighborhood recorded | deterministic fill/scale reveal limited to changed cells | `[P]` |
| Tab change | select destination | system-appropriate content transition; map state restored | `[P]` |
| Period change | select Day/Week/Month | content crossfade or direct replacement without layout jump | `[P]` |
| Date paging | tap arrow | directional transition tied to date change | `[P]` |
| Region selection | tap dot region or result | selected emphasis + leader line | `[P]` |
| Profile presentation | open region | standard sheet transition | `PLATFORM_OFFICIAL` mapping |
| Walk rail | drag/focus | inertial horizontal scrolling; focus item remains visible | `[P]` |

### Motion rules

- Do not animate the complete national dot field continuously.
- Animate only newly acquired or newly selected cells.
- Use deterministic order rather than random sparkling.
- Provide Reduce Motion alternatives using opacity and instant state replacement.
- Preserve map, date, and scroll state after modal dismissal.

---

## 12. Responsive and adaptive behavior

### 12.1 Observed viewport

| Scope | Value |
|---|---|
| Reference | 440×956 pt portrait at 3× |
| Smaller iPhone | not observed |
| Landscape | not observed |
| iPad | app listing says iPhone-only presentation; not observed |
| Dark mode | not observed |

### 12.2 Compact adaptation

- Keep 16 pt page insets, but reduce national atlas scale before reducing control targets.
- Five tabs remain one row because Korean labels are short; use native tab adaptation if width becomes insufficient.
- Badge collection remains two columns only at standard text sizes.
- Long breadcrumb changes to back + current title.
- Profile metrics can wrap into two rows.
- Walk rail uses a fixed width rule, not arbitrary widths based on note length.

### 12.3 Large-text adaptation

| Component | Required adaptation |
|---|---|
| tab bar | maintain semantic labels and 44 pt targets; use system adaptation rather than clipping |
| segmented control | permit standard Dynamic Type behavior; abbreviations remain clear |
| achievement small multiples | one column or horizontal rail |
| badge collection | switch to one column |
| date/weekday header | stack when needed |
| breadcrumb | replace with navigation title/parent subtitle |
| representative-photo row | increase height and allow two lines |
| profile metrics | two rows or compact descriptions |
| walk cards | move note below image when overlay becomes too dense |

### 12.4 Expanded-width proposal

- Use a sidebar or adaptive tab presentation for major destinations.
- Pair national/region atlas with a persistent detail pane.
- Keep dot pitch stable and increase geographic context rather than stretching dots.
- Present region profile as an inspector or secondary pane rather than an oversized centered sheet.

---

## 13. Accessibility and localization

### 13.1 Observed risks

| Risk | Evidence | Severity |
|---|---|---|
| permission prerequisite has low emphasis | `TXT-01` vs active-looking Start | high |
| pale current-location icon and disabled date arrow | `ACT-01`, `ACT-03` | high |
| atlas states rely on color and luminance | all dot maps | high |
| hundreds of dots could create unusable accessibility trees | national/local atlases | high |
| tab bar can obscure scroll content | Records and Badges | high |
| two-column badge labels have limited width | `GRP-03` | high at large text |
| long breadcrumb lacks compact fallback | `NAV-05` | high |
| local map base dots nearly disappear | `DAT-09` | medium-high |
| close button shadow is visually dominant | `ACT-07` | medium |
| route note overlays complex map imagery | `ROW-05` | high |
| metric terms may be ambiguous | `걸음 1` vs `걸음 2` | medium-high |
| place-search action has split icon/label hit-area ambiguity | `ACT-06` | medium-high |

### 13.2 Required semantic behavior

- Tab bar: label, selected state, and destination count.
- Map home atlas: one summarized element, e.g. “전국 288개 지역 중 136개 지역에 발 디딤,” with optional rotor/actions for region lists.
- Start: label changes according to permission/acquisition/recording state.
- Segmented control: one selected value and clear value change announcements.
- Achievement card: heading plus three grouped region achievements.
- Route preview: accessible route summary, not every map label.
- Badge item: region name, completed count, total count, completion status.
- Journal atlas: selected region and photo-color status conveyed textually.
- Palette swatch: hidden as decoration when text already conveys representative photo status, or labeled “대표사진 기억색” when independently meaningful.
- Region sheet: modal focus containment, immediate close action, clear title, summary metrics.
- Walk card: date, distance, duration, place, note status, and action label grouped logically.

### 13.3 Target size and focus

- Every custom button uses at least a 44×44 pt hit region.
- Small arrows, ellipsis, location icon, search icon, and close icon must not use glyph bounds as hit bounds.
- Web or cross-platform ports meet WCAG 2.2 target-size rules and provide single-pointer alternatives to drag.
- Focus must not be obscured by the floating tab bar or sheet.

### 13.4 Contrast

- Secondary text must be recalibrated against both white and warm-paper backgrounds.
- Disabled state uses opacity plus semantic disabled behavior, not near-invisibility alone.
- Photo-derived dots require non-color redundancy.
- Note overlays use a local scrim with contrast tested against route/map fixtures.

### 13.5 Korean localization

The source UI is Korean, but Korean-specific scaling still matters:

- administrative names can be very long;
- do not add tracking to Korean labels;
- date and unit formatting should use locale-aware formatters;
- `km`, duration, and counts need natural VoiceOver phrasing;
- combined administrative names need truncation and full accessible labels;
- parent/current place hierarchy should not depend on slash-separated fixed-width text.

---

## 14. Reference decomposition: Borrow / Exclude / Transform

### Borrow

- One dot-atlas grammar reused across recording, reward, collection, and memory.
- Neutral base geography with restrained photo-derived color.
- Large cumulative and daily metrics with light typographic weight.
- Same-day achievement card containing geographic small multiples.
- Finite badge progress (`136 / 288`) rather than abstract points.
- Region identity built from actual administrative silhouettes.
- Journal’s warm-paper shift from operational surfaces.
- Leader-line selection without introducing generic map pins.
- Region profile combining atlas, palette, metrics, route evidence, notes, and neighborhoods.
- Local-first product framing and optional private backup.

### Exclude

- Three top-level destinations dominated by nearly identical national maps without stronger task differentiation.
- Permission state displayed as weak metadata while Start appears fully ready.
- Dot colors without a legend or semantic redundancy.
- Scroll content hidden by the floating tab bar.
- Very pale action glyphs and disabled arrows.
- Two-column badge layout at all text sizes.
- Full breadcrumb as the primary compact-width navigation device.
- Faint local geography that makes selection context disappear.
- Square and circular palette swatches without a defined role distinction.
- Route-note text over a busy map without stable contrast treatment.
- Large empty journal landing screen with no recent memory or instruction.

### Transform for Haruseon / 하루선

- Borrow the **shared geographic unit**, not the five-tab information architecture.
- Preserve Haruseon’s achromatic chrome and real-photo color identity; apply photo-derived colors only in accumulated Records/Journal surfaces, not the Today surface.
- Keep Haruseon’s mapless pixel-relief or dot-field memory visualization. Do not import the MapKit basemap and black polyline as the primary accumulated atlas.
- Merge badge progress into Records or a regional detail drill-down rather than creating a separate top-level Badge tab.
- Reuse the region-profile sheet pattern for administrative place memories, but keep route gaps, private regions, and unobserved gaps disconnected.
- Use the finite region count and representative-photo palette as secondary evidence beneath the primary daily/weekly/monthly recap hierarchy.
- Maintain the product distinction: 발자취 is collection-first administrative coverage; Haruseon should remain day-shape and route-memory first.

### This / Not this

| This | Not this |
|---|---|
| regular-grid dot atlas | dot-density map |
| finite geographic collection | generic gamification points |
| floating tab bar | floating action button row |
| temporal segmented control | top-level segmented navigation |
| achievement small multiples | decorative mini maps |
| representative-photo palette swatch | pie chart |
| leader-line place selection | generic map pin |
| region profile sheet | unrelated full-screen dashboard |
| warm journal paper | skeuomorphic notebook texture |
| muted photo-derived memory colors | neon territory-control map |

---

## 15. Reconstruction specification

### 15.1 Design thesis

```text
The product should read as a personal geographic atlas generated by real walks. Its
primary visual unit is a stable administrative dot cell, not a pin, route glow, polygon
fill, or decorative particle. Operational screens remain near-white and data-forward;
the Journal shifts to a warm paper surface and introduces representative-photo colors.
Map initiates movement, Records explains it, Badges measures finite coverage, and Journal
turns it into memory. Native tab, segmented-control, map, navigation, sheet, and
accessibility semantics must remain intact beneath the custom dot-atlas rendering.
```

### 15.2 Root layout rules

```text
REFERENCE FRAME
- 440×956 pt portrait.
- System status area remains system-owned.
- Page inline inset: 16 pt.
- Primary controls: minimum 44×44 pt.
- Dividers: 1 device pixel.

FLOATING TAB BAR
- x: 16 pt; visual width: 408 pt.
- Visual height: approximately 72 pt.
- Position above bottom safe area.
- Five equal items with icon + label.
- Selected item receives semantic selection and a light filled capsule.
- Scroll content bottom inset includes tab bar, safe area, and full shadow.

DOT ATLAS
- Dot diameter: 2.5–3 pt at reference width.
- Pitch: 4.5–5 pt.
- Base: warm neutral gray.
- Covered: semantic black/dark state after data confirmation.
- Memory color: muted representative-photo palette.
- Selection: non-color outline/scale/leader-line treatment.
- One summary accessibility element, not hundreds of focus targets.

MAP HOME
- Permission/GPS state immediately above or integrated with Start.
- Cumulative metric remains first focal element.
- National atlas remains second.
- Start remains centered and dominant.
- Optional compact last-walk/today context can occupy current dead space.

RECORDS
- Day/Week/Month segmented control at full content width.
- Date pager uses visible enabled/disabled states.
- One hero metric and one metadata line.
- Achievement card supports adaptive small multiples.
- Route preview map uses muted emphasis when custom content overlays it.
- Route list remains fully visible above the tab bar.

BADGES
- National progress summary + finite count.
- Add completion filter/sort only if supported by product scope.
- Two columns at standard size, one column at accessibility sizes.
- Mini maps are cached simplified glyphs.

JOURNAL
- Warm paper root.
- National map includes a clear instruction, recent memory, or progress sentence.
- Search is one semantic control with one hit area.
- Compact hierarchy uses back + title + parent subtitle, not an unbounded breadcrumb.
- Representative-photo color state is named and editable.

REGION PROFILE
- Large sheet preserving parent context.
- Close target 44×44 pt with restrained shadow.
- Header groups dot map, place identity, palette, and metrics.
- Walk rail uses one card-width rule and deliberate peek.
- Notes over images require a stable scrim or move below the image.
- Neighborhood rows use native disclosure semantics.
```

### 15.3 Component mapping

| Reference element | Target component | Native/custom | Required customization | State owner |
|---|---|---|---|---|
| `NAV-01` | `TabView` / UIKit tab semantics | hybrid | floating pill surface and selected item fill | app navigation |
| `ACT-02` | SwiftUI `Button` | hybrid | 92 pt black circular visual and permission/recording states | recording coordinator |
| `NAV-03` | `Picker(.segmented)` | native | black selected tint and accessible labels | records scope |
| `DAT-02/06/08/09/11` | SwiftUI `Canvas` | custom | cached dot masks, color states, selection | geographic store |
| `GRP-01` | `Button` / `NavigationLink` summary card | hybrid | small-multiple layout | achievement store |
| `DAT-05` | SwiftUI `Map` or snapshot | native/hybrid | route overlay and muted emphasis | route record |
| `GRP-03` | `LazyVGrid` | native | adaptive one/two columns | badge store |
| `ACT-06` | searchable sheet/route | native | place hierarchy filtering | journal search |
| `ROW-03` | `NavigationLink` or photo-picker sheet | native/hybrid | palette preview | place memory store |
| `OVR-01` | `.sheet(item:)` with large detent | native | custom profile header and content | selected region |
| `GRP-06` | horizontal `ScrollView` + `LazyHStack` | native | card width, snapping/peek, focus scrolling | walk collection |
| `ROW-06` | `NavigationLink` row | native | metadata and chevron | neighborhood hierarchy |

### 15.4 Proposed semantic tokens

| Token | Type | Light value | Dark proposal | Description |
|---|---|---|---|---|
| `color.background.operational` | color | `#FDFCFC` | semantic near-black | Map/Records/Badges canvas |
| `color.background.journal` | color | `#F8F6F3` | warm near-black | Journal canvas |
| `color.surface.card` | color | `#F8F6F5` | elevated dark surface | summary card |
| `color.text.primary` | color | semantic near-black | semantic near-white | primary data |
| `color.text.secondary` | color | calibrated warm gray | calibrated light gray | metadata |
| `color.dot.base` | color | `#D6D1CB` approx. | muted dark neutral | unfilled geography |
| `color.dot.covered` | color | semantic black | semantic white/light | covered state |
| `color.memory.purple` | color | `#A487AD` approx. | contrast-adjusted | photo palette |
| `color.memory.rose` | color | `#D0ABB5` approx. | contrast-adjusted | photo palette |
| `color.surface.tabSelected` | color | `#ECEBEA` approx. | selected dark fill | tab item selection |
| `space.inline.page` | dimension | 16 pt | 16 pt | page alignment |
| `space.stack.section` | dimension | 24 pt | 24 pt | standard section rhythm |
| `size.control.hitMinimum` | dimension | 44 pt | 44 pt | custom control target |
| `size.tabBar.height` | dimension | 72 pt | 72 pt | visual tab surface |
| `size.record.primary` | dimension | 92 pt | 92 pt | Start/record control |
| `size.dot.atlas` | dimension | 3 pt | 3 pt | large atlas dot |
| `space.dot.atlas.pitch` | dimension | 4.75 pt | 4.75 pt | large atlas pitch |
| `radius.card.summary` | dimension | 20 pt | 20 pt | achievement card |
| `radius.sheet.top` | dimension | 34 pt | 34 pt | profile sheet |
| `type.metric.cumulative` | typography | 52 pt regular tabular | same role | cumulative distance |
| `type.metric.daily` | typography | 48 pt regular tabular | same role | daily distance |

### 15.5 State matrix

| Surface/component | Default | Selected/active | Loading | Empty | Error | Large text | Dark |
|---|---|---|---|---|---|---|---|
| Map home | ready summary | recording state | acquiring location | no history | permission/GPS/save error | metric capped; context reflows | semantic atlas inversion |
| Start | 시작 | 일시정지/종료 context | locating indicator | not applicable | permission action/retry | label remains legible | high contrast |
| Records | day summary | selected period/date | skeleton preserving layout | no walks for date | route load failure | small multiples adapt | maps and cards recalibrated |
| Badges | progress grid | selected region/filter | cached glyph placeholders | zero regions | geometry load failure | one column | dot states redundant |
| Journal atlas | national overview | selected region | map placeholder | no memories | photo-reference failure | compact hierarchy | warm dark paper |
| Profile sheet | place summary | selected walk | route/photo loading | no walks/notes/neighborhoods | restore/photo errors | metrics wrap | sheet contrast recalibrated |

### 15.6 Asset and data requirements

- Offline administrative geometry and stable codes.
- Precomputed dot-mask manifest for every supported scope.
- Representative-photo palette extraction with deterministic versioning.
- Original photos remain outside the rendered palette asset unless explicitly displayed.
- Route map snapshots or live MapKit views with legal attribution.
- Native text for every label, date, metric, note, and count.
- Cache invalidation when representative photo changes or is deleted.
- QA fixtures for complete, sparse, empty, and outlier regions.

### 15.7 SwiftUI implementation language

```text
Use a TabView or equivalent native navigation state as the semantic owner of the five
primary destinations. Render the custom floating pill through a safe-area overlay or
custom tab-bar surface, but keep tab labels, selected traits, and restoration intact.

Build dot atlases with Canvas using immutable precomputed cell positions. Separate
geometry, coverage state, representative-photo color, and selection into independent
layers. Cache country and region render data. Expose one summarized accessibility element
and region-level actions instead of every cell.

Use a Button for Start with a recording state machine owned outside the view. Permission,
location acquisition, pause, and save state must drive both label and appearance. Use a
44 pt minimum for every secondary action.

Build Records with Picker(.segmented), semantic date buttons, ScrollView/LazyVStack,
an adaptive achievement card, MapKit route preview, and route NavigationLinks. Add a
safeAreaInset or equivalent content padding for the custom tab bar.

Build Badges with LazyVGrid and an adaptive column count. Treat mini maps as cached views
or images generated from the same dot-mask source.

Build Journal with NavigationStack state for geographic hierarchy. Replace the long
compact breadcrumb with native back navigation plus current and parent labels. Use a
searchable sheet or search route. Present region profile through .sheet(item:) with a
large detent, focus restoration, and a clear close action.

Use a horizontal ScrollView/LazyHStack for past walks only when multiple entries exist.
Keep card widths deterministic and make each card one accessibility group containing
route summary, note state, and available action.
```

---

## 16. Explicit prohibitions and non-goals

- Do not call the national dot atlas a heatmap, choropleth, dot-density map, or proportional-symbol map.
- Do not place an Apple basemap underneath the national/region dot-atlas surfaces.
- Do not connect unobserved, private, or route-gap cells to fabricate continuity.
- Do not use neon territory colors, game-resource indicators, or free camera rotation.
- Do not use marker size to encode coverage unless a named quantitative scale is introduced.
- Do not rely on gray/black/color alone for essential state.
- Do not add generic map pins to the abstract atlas.
- Do not make Start appear fully available when location permission or signal state blocks recording.
- Do not permit the floating tab bar to obscure route or badge content.
- Do not preserve two badge columns at accessibility text sizes.
- Do not use the full breadcrumb as the only back-navigation mechanism.
- Do not describe the representative-photo swatch as a pie chart.
- Do not bake walking-note text into route images.
- Do not apply a strong shadow to every control.
- Do not create more top-level tabs to solve surface-specific feature growth.
- Preserve: the dot-atlas grammar, finite geographic progress, photo-derived memory color, large numeric hierarchy, quiet surfaces, and region-profile drill-down.

---

## 17. Visual QA and acceptance criteria

### 17.1 Reference-match checkpoints

| Check | Target | Tolerance | Method |
|---|---|---|---|
| frame calibration | 440×956 pt equivalent | exact reference conversion | screenshot metadata |
| national silhouette | same geographic occupancy and island placement | no missing/extra major clusters | overlay |
| dot pitch/diameter | consistent across same-scale atlases | ±0.5 pt | pixel measurement |
| operational vs journal background | visible warm shift without color cast | perceptual match | sampled comparison |
| Map focal order | cumulative metric → atlas → Start | same squint order | 25% thumbnail |
| Start size/position | centered, dominant, unobstructed | ±4 pt | overlay |
| tab bar geometry | 16 pt side inset, equal five items | ±2 pt | measurement |
| selected tab | correct item and clear state | exact | state screenshots |
| Records segmented control | equal segments and one selected value | exact | screenshot/UI test |
| achievement small multiples | three equal items at standard size | ±3% | overlay |
| route preview | route and attribution readable | no clipped legal attribution | capture review |
| badge progress | count and regional fractions match fixture | exact | deterministic data test |
| tab-bar occlusion | no content behind bar at final scroll position | zero occlusion | UI test |
| Journal selection | cluster-to-label line remains attached | ≤2 pt endpoint error | overlay |
| palette shapes | square/edit and circle/profile roles documented | consistent | design-system review |
| profile rail | deliberate card width and next-card cue | ±4 pt | screenshot |
| route-note contrast | text readable over all map fixtures | contrast test | automated/manual |
| large text | no clipped labels or inaccessible grids | no information loss | Dynamic Type matrix |
| color redundancy | every dot state has text/semantic equivalent | no color-only essential meaning | grayscale/VoiceOver |

### 17.2 Required capture matrix

| Device / viewport | Theme | Text size | Required states |
|---|---|---|---|
| 440×956 pt reference | light | default | all six reference-equivalent screens |
| 393×852 pt compact | light | default | Map, Records, Badges, Journal, profile |
| 393×852 pt compact | light | accessibility XL | Records, Badges, Journal detail, profile |
| representative iPhone | dark | default | all top-level surfaces and sheet |
| landscape | light | default | Map recording and Records |
| iPad/expanded proposal | light/dark | default | atlas-detail split adaptation |

### 17.3 Acceptance statement

```text
PASS when:
- The same dot geometry and semantic states remain coherent across Map, Records, Badges,
  Journal, and the profile sheet.
- Map, Badge, and Journal are immediately distinguishable by task despite sharing data.
- Permission and recording states are explicit.
- The tab bar never obscures scroll content.
- Badge and Journal layouts survive Korean long names and large text.
- Dot color is redundant with text or accessibility metadata.
- Selected geography and route-note text remain legible.

HOLD when:
- Black, neutral, and colored-dot semantics are not confirmed.
- The exact 288-region denominator or administrative hierarchy remains unresolved for
  implementation.
- Representative-photo palette extraction and deletion behavior are not specified.

FAIL when:
- A basemap, heatmap, polygon choropleth, generic pins, or game-map styling replaces the
  dot atlas.
- Start remains visually enabled while recording prerequisites are unavailable.
- Three atlas-led tabs remain visually interchangeable.
- Scroll content or focus is hidden beneath the floating tab bar.
- Color alone conveys visited, selected, or photo-linked status.
```

---

## 18. Uncertainty and decision register

| ID | Question | Status | Alternatives | Evidence needed | Blocks rebuild |
|---|---|---|---|---|---|
| `U-01` | What do black dots mean in each surface? | inferred | visited region / recorded evidence / no-photo state | source model or legend | yes |
| `U-02` | What do muted colored dots encode exactly? | partly documented | dominant photo color / palette category / multiple-photo aggregate | palette algorithm and source code | yes |
| `U-03` | What administrative unit produces 288 total regions? | unknown | city/county/borough aggregate / custom supported set | data manifest | yes |
| `U-04` | Is the national Journal atlas directly tappable? | inferred | map selection / decorative overview / search-only | interaction capture | no |
| `U-05` | What does `전체 지도` do? | unknown | reset scope / alternate map / fit all | interaction capture | no |
| `U-06` | Is the Journal path a functional breadcrumb? | inferred | navigation trail / static context label | interaction capture | no |
| `U-07` | Why does the representative palette use square and circle shapes? | unknown | edit vs identity roles / inconsistent treatment | design-token decision | no |
| `U-08` | Do past-walk cards scroll horizontally and snap? | inferred | free rail / paging / static two-column | interaction capture | no |
| `U-09` | Why does profile metric say one walk while the section says two walks? | unknown | different scope / data mismatch / wording distinction | domain model and fixture | yes for labeling |
| `U-10` | Exact font and text-style mapping | unknown | system styles / custom size tokens | source/design file | no |
| `U-11` | Active recording and auto-pause UI | unknown | live map / status card / Dynamic Island | interaction capture | yes for complete product rebuild |
| `U-12` | Dark-mode hierarchy | unknown | semantic inversion / light-only product | dark captures or source | no for reference light build |

---

## 19. Source register

| Source ID | Claim / terminology | Authority | URL / document | Section | Verified |
|---|---|---|---|---|---:|
| `SRC-01` | exact app identity, product description, version, screenshots | official product listing | `https://apps.apple.com/kr/app/id6792431474` | App Store listing | 2026-08-09 |
| `SRC-02` | tab bar terminology and compact tab guidance | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/tab-bars` | Tab bars | 2026-08-09 |
| `SRC-03` | segmented-control role | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/segmented-controls` | Segmented controls | 2026-08-09 |
| `SRC-04` | map interaction, muted emphasis, selection, clusters, attribution | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/maps` | Maps | 2026-08-09 |
| `SRC-05` | modal sheet and detent terminology | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/sheets` | Sheets | 2026-08-09 |
| `SRC-06` | button role, pressed state, 44×44 pt hit region | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/buttons` | Buttons | 2026-08-09 |
| `SRC-07` | typography and Dynamic Type | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/typography` | Typography | 2026-08-09 |
| `SRC-08` | target size and dragging alternatives | `STANDARD_NORMATIVE` | `https://www.w3.org/TR/WCAG22/` | 2.5.5, 2.5.7, 2.5.8 | 2026-08-09 |

---

## 20. Final build brief

```text
SURFACE:
Map, Records, Badges, Journal national/local, and region profile sheet.

TARGET:
iOS 18+, SwiftUI, MapKit, Canvas; reference frame 440×956 pt.

ARCHETYPE:
Walking-recording utility + finite geographic collection + hierarchical memory journal.

STYLE:
Quiet Dot-Atlas Lifelog: near-white operational surfaces, warm journal paper, black
primary data, warm-gray base dots, restrained photo-derived memory colors, large thin
metrics, sparse cards, and low-chrome navigation.

NAVIGATION:
Five semantic top-level tabs. Day/Week/Month uses a segmented control. Journal drills
country → region → city/county → neighborhood and presents region profile as a large
sheet. Compact hierarchy uses native back navigation rather than a full-width breadcrumb.

LAYOUT:
16 pt page inset. 408×72 pt floating tab surface. 44 pt control targets. Main scroll
content reserves the complete tab-bar height and shadow. Summary cards use 20 pt radius.

DOT ATLAS:
Stable precomputed geographic cells, 2.5–3 pt diameter, 4.5–5 pt pitch. Base, coverage,
photo-color, and selection are separate layers. Add a legend and non-color redundancy.
Do not use basemaps, pins, choropleths, heatmaps, or proportional dot sizes.

MAP:
Permission and GPS state drive the Start control. Preserve cumulative metric and dominant
circular Start action. Add compact last/today context only if it does not displace the
atlas.

RECORDS:
Full-width temporal segmented control, date pager, one hero metric, achievement small
multiples, route preview, and unobscured route list.

BADGES:
National progress + finite count + adaptive regional collection. Two columns only at
standard sizes.

JOURNAL:
Warm paper, searchable atlas, explicit map instruction or recent memory, non-color
selection, representative-photo palette, and compact hierarchy navigation.

PROFILE:
Large sheet with restrained close control, region dot identity, palette, metrics,
deterministic past-walk rail, stable note scrim, and neighborhood disclosure rows.

ACCESSIBILITY:
44×44 pt targets; semantic tab/segmented/sheet behavior; summarized atlas labels;
color-independent coverage/selection; large-text reflow; map/list alternatives; focus
never hidden by tab bar or sheet.

EXCLUSIONS:
Generic pins, basemap under atlas, route glow, game-map styling, unexplained color states,
three visually interchangeable atlas tabs, breadcrumb-only navigation, and text baked
into map images.

QA GATE:
Six-reference coverage complete; geometry and dot pitch match; Map/Badge/Journal have
distinct focal hierarchies; no tab-bar occlusion; all dynamic and accessibility states
pass the capture matrix.
```

---

## Revision history

| Revision | Date | Change |
|---|---:|---|
| 1 | 2026-08-09 | Initial complete analysis of all six Korean iPhone App Store screenshots |
