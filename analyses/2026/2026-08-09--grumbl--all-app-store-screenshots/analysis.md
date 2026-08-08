---
schema_version: "1.0.0"
analysis_id: "UIR-20260809-001"
status: "complete"
created_at: "2026-08-09"
updated_at: "2026-08-09"
title: "grumbl. — Complete public App Store screenshot UI reconstruction"
subject:
  product_name: "grumbl."
  product_type: "app"
  surface_name: "All six public iPhone App Store screenshots"
  platform: "iOS"
  locale: "en"
  theme: "light"
target:
  platform: "iOS"
  framework: "SwiftUI / UIKit / MapKit"
reference_storage: "link_only"
template_version: "1.0.0"
---

# grumbl. — Complete Public App Store Screenshot UI Reconstruction

## 0. Reconstruction directive

> **Pattern:** `photo-first personal archive + date-indexed retrieval surfaces + modal utility tasks`  
> **Primary style:** `Monochrome Contact-Sheet Utility` (`PROJECT_DEFINED`)  
> **Underlying terms:** `editorial minimalism`, `contact-sheet layout`, `Swiss/International-typographic influence`, `low-chrome photo utility` (`INDUSTRY_CONVENTIONAL`)  
> **Platform shell:** custom branded top toolbar, custom text tab strip, collection grid, calendar grid, MapKit map, large modal sheets, grouped disclosure list, persistent bottom action bar  
> **Core composition:** black-and-white interface chrome frames full-color meal photography; expanded uppercase labels, hairline dividers, and corner-bracket motifs create the brand; dates and photo evidence remain primary  
> **Rebuild rule:** calibrate the 1284×2778 references as approximately 428×926 pt at 3×; preserve the shared 20–22 pt inline alignment, 3-column edge-to-edge photo grid, 1 px hairlines, top destination strip, and 113 pt bottom capture region while correcting text scaling, tab crowding, contrast, and map annotation semantics  
> **Do not introduce:** colored app chrome, glass material, card-heavy dashboards, calorie or macro summaries, masonry layout, rounded-capsule controls everywhere, generic bottom tab icons, or gradients except a functional photo-text scrim

### One-paragraph reconstruction language

```text
Build a private, photo-first food-memory archive whose shell behaves like a monochrome
contact sheet. Use a custom brand masthead with a compact trailing toolbar, followed by a
single-line text tab strip for Photos, Calendar, Map, and Recipes. Keep photos in full
color while all persistent chrome stays black, white, and neutral gray. In Photos, group
uniform square thumbnails under date headers and overlay only the capture time. In
Calendar, use a seven-column month grid with day thumbnails and optional meal counts. In
Map, represent geographic meal groups with custom photo-stack annotations. Keep Camera
and Library as persistent bottom acquisition actions rather than navigation destinations.
Present camera-roll scanning and Settings as large modal sheets with simple headers,
hairline-separated rows, and explicit dismissal. Preserve the distinctive uppercase
tracking and corner-bracket motif, but constrain both so controls remain readable,
localizable, and accessible at larger text sizes.
```

---

## 1. Scope and evidence

### 1.1 Subject

| Field | Value |
|---|---|
| Product | `grumbl.` |
| App Store ID | `6772917460` |
| Surface / route / state | All six public iPhone screenshots in US App Store order |
| Product type | Private, local, photo-first food diary and memory archive |
| Source platform | iOS / iPhone |
| Target platform | iOS reconstruction baseline |
| Locale | English |
| Theme | Light only in public references |
| Analysis purpose | faithful structural analysis + selective reconstruction guidance |
| Out of scope | onboarding, meal detail, recipe editor, recap output, search results, actual ad creative, dark mode, animations, permission prompts, error states, source-code verification |

### 1.2 Reference inventory

All six public screenshots were retrieved from Apple-hosted App Store assets in the exact order returned by Apple’s public Lookup response. Each image is 1284×2778 px. The images were inspected locally through a one-day CI artifact and were not committed to this public repository.

| Ref ID | Public App Store order | Visible surface/state | Source viewport | Approx. target frame | Storage |
|---|---:|---|---|---|---|
| `REF-01` | 1 | Photos — dense date group, catch-up banner, inline ad, bottom acquisition bar | 1284×2778 px | 428×926 pt at 3× | `link_only` |
| `REF-02` | 2 | Photos — sparse date groups and empty current-day header | 1284×2778 px | 428×926 pt at 3× | `link_only` |
| `REF-03` | 3 | Calendar — May 2026 thumbnail month grid | 1284×2778 px | 428×926 pt at 3× | `link_only` |
| `REF-04` | 4 | Map — Seattle-area meal clusters using photo-stack annotations | 1284×2778 px | 428×926 pt at 3× | `link_only` |
| `REF-05` | 5 | Scan Camera Roll — large modal sheet with look-back range selector | 1284×2778 px | 428×926 pt at 3× | `link_only` |
| `REF-06` | 6 | Settings — large modal sheet with grouped disclosure rows | 1284×2778 px | 428×926 pt at 3× | `link_only` |

### 1.3 Product facts used to interpret the UI

The App Store listing describes the product as a minimal, photo-first food diary. It documents one-tap camera/library logging, automatic photo date and time, optional notes, on-device camera-roll scanning, a chronological grid with sticky day headers, a thumbnail month calendar, search by note or place, date jumping, one-to-five-star ratings, location metadata, grouped photos, black-and-white share cards, local storage, and one banner ad. Version 1.2 adds the map and recipe collection tab. These claims provide behavior context but do not override what is visually observable in the six references.

### 1.4 Evidence limitations

- `[U]` Exact production font files and font metrics cannot be proven from pixels. The listing names Futura and Helvetica Neue, while the screenshots visibly contain an additional serif italic accent.
- `[U]` Whether the custom top destination strip uses native `TabView`, a custom state switcher, or another implementation is not visible.
- `[U]` Exact scrolling behavior of the top masthead, text tab strip, and bottom Camera/Library region is not shown by still images.
- `[U]` Exact semantics of the circled checkmark toolbar action are inferred as selection mode.
- `[U]` Whether the calendar toolbar icon opens a date picker, jumps to today, or performs another date action is inferred from the product description.
- `[U]` Photo-tile tap behavior, long-press behavior, selection state, grouping affordance, and meal-detail presentation are not visible.
- `[U]` The map’s photo-stack symbols may be true MapKit annotation clusters or custom aggregate annotations; still images cannot distinguish their data logic.
- `[U]` Scan progress, classification review, permission, no-results, cancellation, and failure states are absent.
- `[U]` Settings row destinations and return behavior are not shown.
- `[U]` Dark mode, Dynamic Type, VoiceOver, keyboard, Switch Control, and landscape behavior are not shown.
- `[U]` The App Store marketing files intentionally blur ad content; only placement and container treatment can be analyzed.
- The App Store page says the developer has not declared supported accessibility features. This does not prove that the app has no accessibility implementation.

### 1.5 Evidence labels used

`[O] OBSERVED` · `[M] MEASURED` · `[S] SAMPLED` · `[I] INFERRED` · `[P] PROPOSED` · `[U] UNKNOWN`

---

## 2. Reference overview

### 2.1 `REF-01` — Photos, dense history

#### Literal description

```text
A white iPhone screen contains a black brand lockup at the upper leading side and four
trailing icon-only controls. Beneath it is a single-line destination strip reading
PHOTOS · CALENDAR · MAP · RECIPES, followed by a gray meal-count label. A thin black rule
separates the header from an inline banner that contains a sparkle icon, two text lines,
a bordered REVIEW button, and a gray close glyph. A date header reads MAY 15 on the left
and FRIDAY on the right. Six square meal photos form a three-column, two-row grid with
small translucent time labels in their upper-leading corners. An advertising placement
with small SPONSORED and AD labels follows. A second date header and one row of three meal
photos appear below. A persistent white bottom region contains equal-width CAMERA and
LIBRARY actions, each framed only by four corner brackets.
```

#### Interpretation

- Primary archetype: sectioned chronological photo collection.
- Secondary archetype: capture-first archive utility.
- Dominant focal order: photos → brand/header → catch-up banner → bottom acquisition actions → ad.
- The grid is a **uniform three-column collection grid**, not masonry and not a collage.
- The date header functions as a **section header** and is described by the listing as sticky.
- The banner is an **inline action banner**, not a modal alert or notification center item.
- The sponsored region is an **inline banner-ad placement** inserted between date sections.
- Camera and Library form a **persistent bottom action bar**, not a tab bar.

#### Main UI findings

1. The photo content is visually strong because the shell is monochrome and avoids cards, shadows, or captions over most of each image.
2. The complete pre-content chrome is tall: status region, masthead, destination strip, divider, and catch-up banner consume roughly the upper 205–210 pt before the first date grid begins.
3. The ad interrupts chronology and receives a large vertical allocation relative to the actual ad payload. The corner-bracket treatment assimilates it into the brand but also makes it resemble an app-native content block.
4. The bottom Camera/Library region is immediately understandable as acquisition, but its approximately 113 pt height materially reduces the visible history.
5. The catch-up banner introduces a serif italic line that conflicts with the listing’s stated two-family system and with the otherwise geometric sans shell.

### 2.2 `REF-02` — Photos, sparse history

#### Literal description

```text
The same branded header, text destination strip, meal count, catch-up banner, and bottom
Camera/Library region are visible. MAY 26 / TUESDAY appears as a date header without any
visible photos. MAY 25 / MONDAY contains one square photo in the leading cell of the
three-column grid and blank white space to its right. MAY 24 / SUNDAY contains three
photos across the first row and one photo in the leading cell of the second row, leaving
the remaining two cells blank. A faint, mostly empty sponsored region appears above the
persistent bottom actions.
```

#### Interpretation

- Same surface and system as `REF-01`, shown with sparse per-day counts.
- Empty cells are not actual visible containers; the uniform grid simply leaves unused column positions blank.
- MAY 26 is an **empty current-day section header** or an empty date group. Exact purpose remains inferred.

#### Main UI findings

1. Fixed 3-column continuity makes the archive predictable and preserves thumbnail size across dates.
2. With one or four photos, the same grid creates large blank regions. This is a deliberate contact-sheet effect, but on a phone it can read as unfinished layout.
3. Showing a date header with no item can orient the user to today, but it needs a minimal empty message or capture cue to avoid appearing broken.
4. A masonry or variable-span grid would fill space more efficiently but would destroy the current contact-sheet grammar. A better correction is to keep the uniform grid and reduce the vertical gap after incomplete rows.

### 2.3 `REF-03` — Calendar

#### Literal description

```text
The shared masthead remains, but the circled-check action is absent. CALENDAR is the dark
active destination in the text strip. Below the header, a centered MAY 2026 title sits
between small leading and trailing triangular controls. A weekday row labels seven
columns. A six-week calendar grid fills most of the upper half of the content. Day cells
are square or nearly square. Some cells are white with a black or gray day number; others
use a meal photo as the complete cell background with a white day number and a small
secondary count near the upper-trailing corner. Adjacent-month days are dimmed. A blurred
sponsored banner follows the grid. The Camera/Library action bar remains fixed at bottom.
```

#### Interpretation

- Primary component: **thumbnail month calendar** / **month grid**.
- Month arrows form a **month pager**.
- Image-filled cells are **calendar day cells with background thumbnails**.
- Small upper-trailing values are **meal-count indicators**.
- Adjacent-month cells use a **disabled/dimmed overflow-date treatment**.

#### Main UI findings

1. The calendar successfully compresses an entire month of food memories into one glance; it is the strongest retrieval surface in the public set.
2. Photo-backed cells communicate memory density without additional charts.
3. Day numbers and meal counts sometimes sit directly over bright or detailed photos without a stable scrim, creating inconsistent contrast.
4. The selected day, today, and focused day are not distinguishable in the screenshot.
5. Day numbers, meal counts, and photo imagery compete inside roughly 50–52 pt cells. A small corner scrim or adaptive text backing is preferable to a global dark overlay.
6. The active text tab plus a calendar icon in the masthead may be redundant unless the icon specifically means “jump to date.”

### 2.4 `REF-04` — Map

#### Literal description

```text
The shared masthead and text destination strip remain, with MAP active. A standard Apple
map fills the content region from the header divider to the bottom action bar. A centered
white bordered label near the top reads 228 MEALS ON THE MAP. Several geographic points
are represented by stacks of overlapping square food photographs with white borders and
dark shadows. Some stacks contain many visible layers and some contain only a few. The
map displays the Seattle and Lake Washington region. Apple Maps attribution remains
visible at the lower-leading side. The bottom Camera/Library actions remain above the
screen edge.
```

#### Interpretation

- Base component: **interactive map surface**.
- Custom symbols: **photo-stack map annotations**.
- Multiple-photo symbols operate visually as **cluster annotations**, but exact clustering logic is unknown.
- The top label is a **map summary badge** / **status banner**.

#### Main UI findings

1. The photo stacks convert abstract pins into autobiographical evidence and fit the product better than generic marker icons.
2. The irregular stack silhouette and shadows create strong depth against a flat map; this is the one surface where the interface intentionally departs from the otherwise flat shell.
3. Stacks do not expose a count, date range, place name, or selection state. Users must infer that pile size corresponds to density.
4. Large stacks can obscure local geography and each other. At lower zoom levels, a count-bearing cluster or representative thumbnail plus count would be clearer.
5. The map uses the standard colorful emphasis style. A muted map style would let photo annotations dominate more consistently and reduce visual competition.
6. The map summary badge is legible but floats over labels; its position must avoid map controls, safe areas, and selected annotations.
7. Keeping Camera/Library available reinforces the capture loop, but the 113 pt bottom region reduces map exploration space.

### 2.5 `REF-05` — Scan Camera Roll

#### Literal description

```text
A gray dimming layer covers the underlying screen. A white modal surface with large
rounded upper corners rises almost to the status bar. Its header contains CLOSE at the
leading side and the centered title SCAN CAMERA ROLL, followed by a black divider. The
body begins with the large uppercase heading FIND FOOD PHOTOS YOU FORGOT, a gray paragraph,
and the gray uppercase label LOOK BACK. A bordered four-row single-selection list offers
LAST 7 DAYS, LAST 30 DAYS, LAST 90 DAYS, and LAST YEAR. A filled black dot on the trailing
side of LAST 30 DAYS indicates selection. Below is a wide START SCAN action framed with
corner brackets. A centered gray serif italic footnote states that Apple’s on-device
classifier is used with no internet or upload. The remaining lower portion is empty white
space.
```

#### Interpretation

- Presentation: **large modal sheet** with a custom header.
- Look-back control: **single-selection list** / **radio group**.
- Selected dot: custom **radio selection indicator**.
- Start Scan: **primary action button** using the corner-bracket brand motif.
- Bottom line: **privacy reassurance footnote**.

#### Main UI findings

1. The task is clear and linear: explanation → range → start.
2. The sheet retains parent context through the dimmed background and rounded top corners.
3. A full large sheet is visually oversized for four choices and one action; the lower half becomes unused. A medium detent or content-fitting height would be more efficient if scan review is a separate subsequent surface.
4. The filled trailing dot is minimal but less familiar than a checkmark or standard radio control, especially without a visible unselected circle.
5. Body text and the privacy footnote are light gray and may fall below comfortable contrast on white.
6. The serif italic footnote and banner subtitle create a distinct editorial voice, but they establish an unlisted third type family and reduce system coherence.
7. The header uses a text CLOSE control rather than the familiar system close symbol; the wide tracking also increases target ambiguity.

### 2.6 `REF-06` — Settings

#### Literal description

```text
A gray dimming layer and large white rounded modal sheet match the scan presentation. The
header contains CLOSE at leading and SETTINGS centered, separated from content by a black
rule. The body is a vertically scrolling grouped list. Gray uppercase section labels read
TOOLS, HELP, LEGAL, and ABOUT. TOOLS contains RECIPE BOOK, THIS WEEK'S RECAP, THIS MONTH'S
RECAP, SCAN CAMERA ROLL FOR FOOD, and STATS. HELP contains SHOW INTRO AGAIN. LEGAL contains
PRIVACY POLICY, TERMS OF SERVICE, and SUPPORT. Each navigational row is full-width, uses a
large tracked uppercase label, a pale trailing chevron, and thin separators. Stronger
black rules separate major groups. ABOUT ends in a brand row with the circular mark,
wordmark, and a gray serif italic subtitle reading food memory · v1.2 (23).
```

#### Interpretation

- Presentation: **large modal sheet**.
- Main structure: **grouped disclosure list**.
- Rows: **navigation rows with disclosure indicators**.
- Final row: **about / brand lockup row**.

#### Main UI findings

1. The grouped list is familiar and scan-friendly despite its custom typography.
2. Strong section boundaries create a print-index character and reinforce the monochrome system.
3. Every row uses all caps and large tracking, including long labels. This harms quick word-shape recognition and leaves little localization or Dynamic Type headroom.
4. The label `SCAN CAMERA ROLL FOR FOOD` is already close to the usable width in English.
5. The disclosure chevrons are extremely light relative to row labels and separators, weakening the action cue.
6. The About lockup closes the sheet well, but exposing the internal build number `(23)` is useful primarily for support and need not be visually prominent.
7. `CLOSE` and the centered title replicate `REF-05`, showing strong modal consistency.

---

## 3. Interface archetype and product loop

### 3.1 Archetype classification

| Field | Classification | Authority | Evidence | Confidence |
|---|---|---|---|---:|
| Primary archetype | Personal photo archive / diary | `INDUSTRY_CONVENTIONAL` | date-grouped meal photos and product description | 0.99 |
| Primary task model | Capture → auto-date → optional note → later retrieval | product model | App Store description and persistent Camera/Library actions | 0.99 |
| Retrieval surfaces | chronological grid, month calendar, map, search, recipes | product model | screenshots and version notes | 0.99 |
| Navigation model | custom horizontal destination tabs beneath branded masthead | `INDUSTRY_CONVENTIONAL` | active destination changes among Photos/Calendar/Map/Recipes | 0.96 |
| Acquisition model | persistent dual-source bottom actions | `PROJECT_DEFINED` | Camera and Library shown across main surfaces | 1.00 |
| Modal utility model | large sheets for bounded secondary tasks | `PLATFORM_OFFICIAL` mapping | Scan and Settings references | 0.99 |
| Monetization surface | one inline banner-ad placement | product model | screenshot and listing | 0.99 |

### 3.2 Core loop inferred from the UI

```text
Take or choose a food photo
→ photo receives date/time and optionally note/place/rating/recipe
→ meal enters date-grouped photo archive
→ rediscover by Photos, Calendar, Map, Search, Recipe Book, or recap
→ share or revisit the remembered meal
→ persistent Camera/Library actions restart the loop
```

### 3.3 Reading-order hierarchy across main surfaces

1. Full-color meal photography or map.
2. Active archive context: date, month, or map summary.
3. Brand masthead and text destination strip.
4. Persistent acquisition actions.
5. Secondary tools, catch-up banner, and sponsored placement.

**Squint-test:** food images remain the strongest mass on Photos and Calendar; the map base becomes strongest on Map because it is highly saturated.  
**25%-thumbnail test:** brand lockup, selected destination, photo grid rhythm, calendar pattern, map stacks, and corner-bracket actions remain recognizable. Small toolbar icons, time labels, calendar counts, section labels, and chevrons do not.

---

## 4. Terminology normalization summary

| Raw description | Canonical term | Authority class | Platform scope | Why this term fits |
|---|---|---|---|---|
| “위에 로고랑 아이콘 있는 줄” | branded masthead + top toolbar | `INDUSTRY_CONVENTIONAL` + `PLATFORM_OFFICIAL` mapping | iOS / cross-platform | brand identity and current-view actions share one horizontal region |
| “PHOTOS · CALENDAR · MAP · RECIPES” | text tab strip / tab list | `INDUSTRY_CONVENTIONAL`; WAI-ARIA tabs analogue | cross-platform | one active destination exposes one content panel at a time |
| “세그먼트 컨트롤” | rejected: segmented control | `PLATFORM_OFFICIAL` | Apple platforms | it has no shared capsule/segment container and acts as top-level destinations |
| “하단 탭” | rejected: tab bar | `PLATFORM_OFFICIAL` | Apple platforms | Camera and Library perform actions; they do not switch app destinations |
| “하단 카메라/라이브러리” | persistent bottom action bar | `INDUSTRY_CONVENTIONAL` | cross-platform | two acquisition commands remain visible across main content surfaces |
| “모서리만 있는 버튼” | corner-bracket framed action | `PROJECT_DEFINED` | grumbl. | four detached corner strokes form the button boundary motif |
| “날짜별 사진 피드” | sectioned chronological photo collection | `INDUSTRY_CONVENTIONAL` | cross-platform | date headers partition an ordered image collection |
| “3열 사진판” | uniform three-column collection grid | `INDUSTRY_CONVENTIONAL` | cross-platform | equal square cells preserve source order without masonry repacking |
| “사진마다 시간” | metadata badge / time overlay | `INDUSTRY_CONVENTIONAL` | cross-platform | compact translucent label is overlaid on the image |
| “놓친 사진 추가 배너” | inline action banner | `INDUSTRY_CONVENTIONAL` | cross-platform | contextual message, CTA, and dismissal sit inside content flow |
| “광고 칸” | inline banner-ad placement | `INDUSTRY_CONVENTIONAL` | cross-platform | sponsored content occupies a dedicated block between archive sections |
| “달력 사진칸” | thumbnail calendar day cell | `INDUSTRY_CONVENTIONAL` | cross-platform | day cell uses a representative meal thumbnail as background |
| “월 넘기는 화살표” | month pager | `INDUSTRY_CONVENTIONAL` | cross-platform | previous/next controls change the visible month |
| “지도 위 사진 뭉치” | photo-stack map annotation | `PROJECT_DEFINED` | grumbl. / MapKit | geographic marker is represented by overlapping photo thumbnails |
| “지도 클러스터” | cluster annotation | `PLATFORM_OFFICIAL` mapping | MapKit | multiple geographic items may be aggregated at the current zoom |
| “228 MEALS ON THE MAP” | map summary badge | `INDUSTRY_CONVENTIONAL` | cross-platform | compact overlay reports aggregate scope of the map |
| “위에서 둥근 설정창” | large modal sheet | `PLATFORM_OFFICIAL` | iOS | a modal surface preserves dimmed parent context and has rounded top corners |
| “기간 네 개 중 하나 선택” | single-selection list / radio group | `INDUSTRY_CONVENTIONAL` / web-standard analogue | cross-platform | one choice is selected from a mutually exclusive set |
| “검은 점” | radio selection indicator | `INDUSTRY_CONVENTIONAL` | cross-platform | trailing dot indicates the selected row |
| “설정 메뉴 줄” | navigation row with disclosure indicator | `PLATFORM_OFFICIAL` | iOS | row reveals a subordinate destination and uses a chevron |
| “TOOLS / HELP / LEGAL” | list section header | `PLATFORM_OFFICIAL` mapping | iOS | label names a grouped list section |
| “로고+앱명” | brand lockup | `INDUSTRY_CONVENTIONAL` | cross-platform | symbol and wordmark are treated as one identity unit |
| “작은 이탤릭 문구” | secondary serif-italic annotation | `INDUSTRY_CONVENTIONAL` | cross-platform | separate typographic voice qualifies primary sans information |

### 4.1 Style classification

| Field | Value |
|---|---|
| Primary project label | **Monochrome Contact-Sheet Utility** |
| Authority | `PROJECT_DEFINED` |
| Definition | a photo-first archive shell that combines black-and-white utility chrome, contact-sheet image grids, expanded uppercase geometry, hairline rules, and viewfinder-like corner brackets |
| Underlying industry terms | editorial minimalism, contact-sheet layout, Swiss/International-typographic influence, monochrome utility UI, low-chrome photo interface |
| Observable traits | white canvas; black text/rules/icons; gray secondary text; full-color user photos; all-caps tracked labels; geometric sans headings; serif italic annotations; no panel cards; 1 px separators; custom corner brackets; strong grid alignment |
| Secondary influence | photographic contact sheets, print crop/viewfinder marks, archival index pages |
| Labels rejected | glassmorphism, neumorphism, skeuomorphism, neobrutalism, bento grid, masonry, card-based dashboard, native-default iOS |
| Rejection reasons | no translucent blur inside core content, no embossed surfaces, no real-world material imitation, no heavy brutalist blocks, no modular dashboard cards, no variable-height columns, and extensive custom chrome replaces native-default styling |

---

## 5. Frame, geometry, and layout system

### 5.1 Coordinate calibration

| Field | Value |
|---|---|
| Source viewport | 1284×2778 px for all six references |
| Likely scale | 3 source px per target pt |
| Approx. target viewport | 428×926 pt |
| Origin | top-left |
| Confidence | 0.96; dimensions divide exactly by 3 |
| Caveat | App Store screenshot dimensions establish a display frame, not the actual device model or safe-area API values |

### 5.2 Shared main-surface shell (`REF-01`–`REF-04`)

| Region | Approx. target bounds | Role | Notes |
|---|---:|---|---|
| System/status region | y `0–54 pt` | system chrome | standard iPhone status content |
| Branded masthead | y `54–116 pt` | brand + current-view toolbar | logo leading, 3–4 icon actions trailing |
| Text tab strip | y `116–154 pt` | top-level destination navigation + meal count | single line at capacity |
| Header divider | y `153 pt`, 1 px | separates chrome from content | full width black hairline |
| Main content | y `154–813 pt` before optional inline banner variance | scroll/map content | Photos includes additional banner inside flow |
| Bottom action bar | y `813–926 pt` | persistent Camera/Library acquisition | approx. 113 pt total |

### 5.3 Shared modal shell (`REF-05`–`REF-06`)

| Region | Approx. target bounds | Role |
|---|---:|---|
| Dimmed parent/status | y `0–62 pt` | preserves parent context |
| Rounded sheet surface | y `62–926 pt` | modal content surface |
| Sheet header | approx. `62–122/131 pt` | leading Close + centered title |
| Header divider | 1 px full width | separates task title from body |
| Body inline inset | approx. `23 pt` | shared text/list alignment |

### 5.4 Shared alignment system

- Primary inline text inset: approximately 20–23 pt.
- Toolbar leading brand anchor: approximately 20–22 pt.
- Toolbar trailing action spacing: approximately 20–24 pt center-to-center after the first action.
- Photo grid: edge-to-edge or nearly edge-to-edge, 3 equal columns, approximately 1–2 pt gutters.
- List rows: full-width with text inset approximately 23 pt and trailing disclosure inset approximately 22–24 pt.
- Hairlines: source 1–2 px, equivalent to 0.33–0.67 pt at 3×.
- Corner-bracket button boundary: four independent L-shaped strokes; no continuous rectangle.

### 5.5 Density and whitespace

- Main archive surfaces are **content-dense** inside the photo/calendar/map region but **chrome-heavy** above and below it.
- Modal tasks are **low-density** and use large whitespace blocks.
- Sparse Photos days preserve empty grid positions rather than adapting item widths.
- Settings uses regular row density with generous vertical padding and high typographic tracking.

---

## 6. Element inventory

| ID | Ref | Literal observation | Canonical term | Authority | Hierarchy role | Evidence | Confidence |
|---|---|---|---|---|---|---|---:|
| `SYS-01` | 01–06 | iPhone time, network, battery | system status bar | `PLATFORM_OFFICIAL` | system context | `[O]` | 1.00 |
| `NAV-01` | 01–04 | logo/wordmark with trailing icons | branded masthead + top toolbar | mixed | persistent shell | `[O]` | 0.99 |
| `IMG-01` | 01–04,06 | black circular mark with white upper-right cutout | brand mark | `PROJECT_DEFINED` | identity | `[O]` | 1.00 |
| `TXT-01` | 01–04,06 | lowercase `grumbl.` wordmark | wordmark | `PROJECT_DEFINED` | identity | `[O]` | 1.00 |
| `ACT-01` | 01–04 | magnifying glass | search action | `PLATFORM_OFFICIAL` mapping | retrieval | `[O/I]` | 0.98 |
| `ACT-02` | 01–04 | calendar-grid icon | date-jump action | `PLATFORM_OFFICIAL` mapping | retrieval | `[O/I]` | 0.82 |
| `ACT-03` | 01–02 | circled checkmark | selection-mode action | `INDUSTRY_CONVENTIONAL` | photo management | `[O/I]` | 0.72 |
| `ACT-04` | 01–04 | ellipsis | more menu | `PLATFORM_OFFICIAL` | secondary actions | `[O/I]` | 0.94 |
| `NAV-02` | 01–04 | Photos/Calendar/Map/Recipes text line | text tab strip / tab list | conventional | top-level navigation | `[O/I]` | 0.97 |
| `TXT-02` | 01–04 | `277 MEALS` | aggregate metadata label | conventional | archive count | `[O]` | 1.00 |
| `GRP-01` | 01–02 | catch-up message, review, dismiss | inline action banner | conventional | import prompt | `[O]` | 1.00 |
| `ACT-05` | 01–02 | bordered `REVIEW` | banner CTA | conventional | opens missed-meal review | `[O/I]` | 0.98 |
| `ACT-06` | 01–02 | gray X | dismiss action | platform mapping | hides banner | `[O/I]` | 0.99 |
| `GRP-02` | 01–02 | date + weekday + photos | date section | conventional | chronological grouping | `[O]` | 1.00 |
| `TXT-03` | 01–02 | `MAY 15`, `MAY 25` | section heading / date heading | conventional | date identity | `[O]` | 1.00 |
| `TXT-04` | 01–02 | `FRIDAY`, `MONDAY` | secondary section metadata | conventional | weekday | `[O]` | 1.00 |
| `GRP-03` | 01–02 | equal square 3-column tiles | uniform collection grid | conventional | meal collection | `[O]` | 1.00 |
| `IMG-02` | 01–03 | meal image | photo thumbnail / collection item | conventional | primary content | `[O]` | 1.00 |
| `TXT-05` | 01–02 | small time over photo | metadata badge / time overlay | conventional | capture time | `[O]` | 1.00 |
| `GRP-04` | 01–03 | sponsored/ad block | inline banner-ad placement | conventional | monetization | `[O]` | 1.00 |
| `NAV-03` | 01–04 | bottom Camera/Library region | persistent bottom action bar | conventional | primary acquisition | `[O]` | 1.00 |
| `ACT-07` | 01–04 | `CAMERA` with corner brackets | primary acquisition action | project/platform mapping | take photo | `[O/I]` | 1.00 |
| `ACT-08` | 01–04 | `LIBRARY` with corner brackets | primary acquisition action | project/platform mapping | choose photo | `[O/I]` | 1.00 |
| `NAV-04` | 03 | month title with arrows | month pager | conventional | temporal navigation | `[O/I]` | 0.99 |
| `DAT-01` | 03 | seven-column month matrix | month calendar grid | conventional | date retrieval | `[O]` | 1.00 |
| `DAT-02` | 03 | numbered square day | calendar day cell | conventional | day selection | `[O/I]` | 1.00 |
| `TXT-06` | 03 | small value in cell upper-right | meal-count indicator | conventional | daily density | `[O/I]` | 0.88 |
| `DAT-03` | 04 | Apple geographic map | interactive map surface | `PLATFORM_OFFICIAL` | spatial retrieval | `[O]` | 1.00 |
| `DAT-04` | 04 | overlapping bordered meal photos | photo-stack map annotation | `PROJECT_DEFINED` | geographic meal group | `[O/I]` | 0.96 |
| `TXT-07` | 04 | `228 MEALS ON THE MAP` | map summary badge | conventional | scope summary | `[O]` | 1.00 |
| `OVR-01` | 05 | rounded white modal over gray backdrop | large modal sheet | `PLATFORM_OFFICIAL` | bounded scan task | `[O]` | 1.00 |
| `NAV-05` | 05–06 | Close + centered title | sheet header | conventional/platform mapping | modal orientation/dismissal | `[O]` | 1.00 |
| `GRP-05` | 05 | four mutually exclusive time ranges | single-selection list / radio group | conventional | scan range | `[O/I]` | 0.99 |
| `ACT-09` | 05 | selectable range row | radio option row | conventional | parameter selection | `[O/I]` | 0.99 |
| `ACT-10` | 05 | bracket-framed `START SCAN` | primary action button | project/platform mapping | begins scan | `[O/I]` | 1.00 |
| `TXT-08` | 05 | gray italic privacy line | privacy reassurance footnote | conventional | trust/context | `[O]` | 1.00 |
| `OVR-02` | 06 | settings modal sheet | large modal sheet | `PLATFORM_OFFICIAL` | secondary configuration | `[O]` | 1.00 |
| `GRP-06` | 06 | Tools/Help/Legal/About groups | grouped disclosure list | `PLATFORM_OFFICIAL` mapping | settings hierarchy | `[O]` | 1.00 |
| `ROW-01` | 06 | full-width label + chevron | navigation row with disclosure indicator | `PLATFORM_OFFICIAL` | opens child surface | `[O/I]` | 1.00 |
| `GRP-07` | 06 | logo, wordmark, version subtitle | about brand lockup | conventional | product identity/version | `[O]` | 1.00 |

---

## 7. Detailed component specifications

### 7.1 `NAV-01` — Branded masthead and top toolbar

**Observed anatomy**

- Leading: `IMG-01` brand mark and `TXT-01` wordmark.
- Trailing: search, date/calendar, optional selection, and overflow icon buttons.
- Surface: white, no visible material blur or shadow.
- Border: none inside the row; divider belongs below `NAV-02`.
- Position: persistent-looking top region beneath status bar.
- Icon family: system-like outline symbols, exact source unknown.

**Rebuild directive**

```text
Use a 60–64 pt content row beneath the top safe area. Align the brand lockup at 20–22 pt
leading. Allocate a minimum 44×44 pt semantic target to each toolbar action even when the
visible glyph is 20–24 pt. Keep only search, date jump, context-specific select, and an
overflow menu visible. Do not add background capsules or glass. Hide context-inapplicable
actions rather than leaving disabled glyphs. Provide explicit accessibility labels.
```

**Risk**

The brand lockup plus four icon actions nearly fills the 428 pt width. Large text, localized labels in accessibility content, or larger icon spacing can cause collision. Toolbar action priority and overflow behavior must be explicit.

### 7.2 `NAV-02` — Text tab strip

**Observed anatomy**

- Four uppercase destinations separated by centered dots.
- Selected destination: black and heavier.
- Unselected destinations: light gray.
- Aggregate meal count aligned at trailing end on the same baseline.
- No underline, capsule, or separate indicator.

**Canonical classification**

This is a **text tab strip/tab list**, not an Apple tab bar and not a segmented control. It swaps top-level archive surfaces while staying within one custom shell.

**Rebuild directive**

```text
Treat the destinations as a semantic single-selection tab list. Maintain one selected
item. Use weight plus a secondary non-color indicator such as a 1 px underline or bottom
rule segment; do not rely only on black-versus-gray. Preserve 44 pt effective target
heights with invisible padding. At compact width, separate the meal count from the tab
line or make the tab strip horizontally scrollable with clear edge behavior. Do not reduce
labels below 11–12 pt merely to fit future destinations. On web, implement tablist/tab/
tabpanel semantics and arrow-key navigation.
```

**Scalability finding**

The addition of Recipes in version 1.2 has brought the single-line strip to capacity. The meal count is metadata, not a destination, and should move to the masthead, active panel header, or a secondary line before another destination is introduced.

### 7.3 `GRP-03` — Uniform three-column meal grid

**Observed anatomy**

- Three equal square columns.
- Very small gutters.
- Items remain at one cell each; incomplete rows leave blank trailing positions.
- No card containers, labels, or persistent borders.
- Per-item time appears in a dark translucent upper-leading badge.

**Rebuild directive**

```text
Use a 3-column LazyVGrid/collection layout with fixed equal tracks and 1–2 pt gutters.
Crop images with aspect-fill into square cells. Preserve chronological source order.
Incomplete rows remain left-filled; do not convert to masonry. Combine each photo and its
time into one accessible meal item. Use an adaptive local scrim behind time text and hide
the time badge only when the detailed surface supplies it equivalently.
```

**Sparse-state correction**

Keep the contact-sheet grid but tighten the gap between an incomplete final row and the next date header. When a date has zero items, show a compact “No meal yet” state with Camera/Library affordance or omit the empty group unless it represents today.

### 7.4 `NAV-03` — Persistent bottom acquisition action bar

**Observed anatomy**

- White region separated from content by a horizontal line on Calendar and Map.
- Two equal-width actions.
- Each action uses uppercase tracked text surrounded by four corner brackets.
- No icons.
- Region includes substantial vertical whitespace.

**Rebuild directive**

```text
Treat Camera and Library as actions, not navigation. Keep two equal columns and preserve
at least 44 pt targets. Reduce total bar height from approximately 113 pt toward 84–96 pt
if device and home-indicator spacing permit, while retaining the corner-bracket motif.
Use native Button semantics and contentShape(Rectangle()) across each half. Provide camera
and photo-library symbols only if usability testing shows text-only recognition is weak;
do not turn the region into a conventional tab bar.
```

### 7.5 `DAT-01` — Thumbnail month calendar

**Observed anatomy**

- Seven equal columns and six week rows.
- Weekday header row.
- Day number at upper-leading.
- Optional meal count at upper-trailing.
- Representative image fills occupied cells.
- Adjacent-month cells are muted.

**Rebuild directive**

```text
Use a true date grid with locale-aware first weekday, month length, and adjacent-month
cells. Day cells must expose the full date and meal count semantically. Keep a minimum
44 pt target; the observed approximately 50–52 pt cell width supports this at 428 pt.
Place day number and count on small adaptive corner scrims or choose text color from image
luminance. Define distinct today, selected, focused, empty, adjacent-month, and disabled
states without relying on image content alone.
```

### 7.6 `DAT-04` — Photo-stack map annotation

**Observed anatomy**

- Several overlapping square thumbnails.
- White frames and dark shadows create a physical stack.
- Different stack sizes imply different cluster densities.
- No visible count label, title, or selection ring.

**Rebuild directive**

```text
Implement as a custom MapKit annotation or cluster annotation. At low zoom, show one
representative photo plus a numeric count rather than rendering an arbitrarily deep pile.
At medium zoom, permit 2–4 offset layers. At high zoom, reveal individual meal annotations.
Selected state receives a clear outline, z-order, and optional place/date caption. Keep
Apple attribution unobscured. Prefer a muted map emphasis style so meal photos remain the
primary visual signal.
```

### 7.7 `GRP-05` — Scan range single-selection list

**Observed anatomy**

- Four equal-height rows inside one bordered rectangle.
- Thin separators.
- Labels are uppercase, widely tracked, leading aligned.
- Selected row uses one black trailing dot; unselected rows show no circle.

**Rebuild directive**

```text
Represent the set as a semantic single-selection group. Make the full row tappable.
Use a checkmark or visible radio-circle family so selected and unselected states share a
recognizable control grammar. Maintain at least 44 pt row height. Announce the selected
value. Preserve the monochrome styling but reduce tracking for long or localized labels.
```

### 7.8 `ROW-01` — Settings disclosure row

**Observed anatomy**

- Full-width white row.
- Leading uppercase label.
- Very light trailing chevron.
- Thin gray separators between rows.
- Strong black rules between groups.

**Rebuild directive**

```text
Use List/navigation rows with native disclosure semantics. Keep labels concise and allow
normal title case in localized or accessibility variants. Preserve the monochrome grouped
structure, but raise chevron contrast and do not use tracking as the only hierarchy cue.
Give each row a minimum 52–56 pt height and support multiline wrapping at large text sizes.
```

---

## 8. Navigation and interaction model

### 8.1 Navigation map

```text
Main archive shell
├── Photos tab
├── Calendar tab
├── Map tab
└── Recipes tab

Global/current-view toolbar
├── Search
├── Jump to date / calendar action
├── Select mode (Photos only, inferred)
└── More menu

Persistent acquisition
├── Camera
└── Library

More/secondary routes
├── Scan Camera Roll sheet
├── Settings sheet
├── Recaps
├── Stats
├── Legal/help
└── About
```

### 8.2 Control semantics

| Element | Generic role | iOS mapping | Trigger | Result |
|---|---|---|---|---|
| `NAV-02` destination | tab | custom state / `TabView` mapping | tap | switches archive surface |
| `ACT-01` | button | toolbar button | tap | opens search |
| `ACT-02` | button | toolbar button/date picker route | tap | jumps/selects date |
| `ACT-03` | toggle/action | toolbar button | tap | enters/exits selection mode |
| `ACT-04` | menu button | `Menu` / toolbar overflow | tap | secondary commands |
| `ACT-05` | button | inline CTA | tap | reviews missed meals |
| `ACT-06` | button | dismiss | tap | hides catch-up banner |
| `IMG-02` meal | collection item / link | `NavigationLink` or button | tap | opens meal detail |
| `ACT-07` | button | camera route | tap | captures a new meal photo |
| `ACT-08` | button | photo picker route | tap | chooses existing photo(s) |
| `DAT-02` day | button | calendar day selection | tap | opens/jumps to day |
| `DAT-04` map stack | selectable annotation | MapKit annotation | tap | zooms/reveals meals |
| `ACT-09` | radio option | single-selection row | tap | changes scan look-back |
| `ACT-10` | primary button | sheet action | tap | begins on-device scan |
| `ROW-01` | navigation row | `NavigationLink` | tap | opens subordinate settings/tool surface |

### 8.3 State preservation

- Switching Photos/Calendar/Map/Recipes should preserve each surface’s scroll/camera state.
- Opening and closing Scan or Settings should return to the exact parent surface state.
- Photo selection mode should not reset the Photos scroll position.
- Calendar month and selected day should persist when navigating into a meal and back.
- Map camera region and selected cluster should persist across detail presentation.
- Camera/Library completion should insert the new item and return to a predictable date position.

### 8.4 Motion

Static screenshots do not prove motion. Proposed behavior:

- Tab switch: minimal crossfade or no animation; avoid lateral page motion that implies hierarchy.
- Date-section insertion: short opacity/position transition with Reduce Motion fallback.
- Modal sheets: system sheet presentation.
- Map clusters: system-like zoom expansion; no bouncing photo piles.
- Corner-bracket actions: subtle opacity or 1 px inset response rather than scale-heavy spring.
- Haptic: light selection for range/day/tab changes, success feedback after import, none for passive scrolling.

---

## 9. Typography

### 9.1 Observed type system

The listing states “Futura + Helvetica Neue typography.” The screenshots support a geometric sans for the wordmark, uppercase headings, tabs, dates, buttons, and settings rows, plus a neutral sans for paragraphs and metadata. They also clearly show a serif italic accent in the catch-up subtitle, scan privacy footnote, and About subtitle. Therefore the visual system is effectively three-role even if only two families are documented.

| Role | Examples | Observed classification | Approx. target size | Weight | Tracking |
|---|---|---|---:|---|---:|
| Brand wordmark | `grumbl.` | geometric sans | 25–29 pt | medium | 2–4 pt |
| Destination tab | `PHOTOS` | geometric sans uppercase | 11–12 pt | selected semibold, inactive regular | 1.5–2.5 pt |
| Aggregate metadata | `277 MEALS` | geometric/neutral sans uppercase | 10–11 pt | regular | 2–3 pt |
| Date heading | `MAY 15` | geometric sans uppercase | 18–20 pt | medium | 3–4 pt |
| Weekday/section meta | `FRIDAY`, `LOOK BACK` | sans uppercase | 10–12 pt | regular | 2.5–4 pt |
| Toolbar glyph | search/calendar/check/more | outline icon | 20–24 pt optical | regular | n/a |
| Banner title | `ADD MISSED MEALS` | geometric sans uppercase | 13–15 pt | medium | 2–3 pt |
| Body paragraph | scan explanation | neutral sans | 14–16 pt | regular | normal |
| Modal title | `SCAN CAMERA ROLL`, `SETTINGS` | geometric sans uppercase | 16–18 pt | medium | 3–5 pt |
| List row | `RECIPE BOOK` | geometric sans uppercase | 14–16 pt | medium | 2–4 pt |
| Serif annotation | privacy/about/banner subtitle | serif italic | 12–15 pt | semibold/italic | normal |
| Photo metadata | `7:05PM` | neutral sans | 10–12 pt | regular | normal |

### 9.2 Typographic strengths

- The wordmark, expanded uppercase, and hairline rules create a recognizable identity without color.
- Full-color user photos remain primary because text is mostly confined to chrome and section boundaries.
- Date and month headings are easy to identify at a glance.
- Serif italic lines distinguish explanatory or emotional text from commands.

### 9.3 Typographic weaknesses

- Small uppercase labels with wide tracking reduce word-shape recognition and make scanning slower.
- The destination strip and settings rows have minimal localization headroom.
- Gray text often appears too light, especially the scan paragraph, section labels, weekday labels, chevrons, and privacy footnote.
- Using a third serif family without formally defining it creates inconsistency in the stated type system.
- Dynamic Type cannot be supported by simply scaling the current single-line tab strip and long uppercase settings rows.

### 9.4 Rebuild type tokens

| Token | Proposed baseline | Behavior |
|---|---|---|
| `type.brand.wordmark` | 28 pt geometric sans medium, +2.5 pt tracking | fixed brand role, limited scaling |
| `type.nav.tab` | 12 pt geometric sans medium, +1.5 pt tracking | 44 pt target; wraps never; tabs scroll/reflow instead |
| `type.section.date` | 19 pt geometric sans medium, +2.5 pt tracking | scales one step; preserves one line |
| `type.meta.upper` | 11 pt sans medium, +1.5 pt tracking | avoid ultra-light gray |
| `type.body.primary` | 16 pt neutral sans regular, 22 pt line height | full Dynamic Type |
| `type.control.primary` | 15–16 pt geometric sans medium, +2 pt tracking | reduce tracking for localization |
| `type.list.row` | 15 pt geometric sans medium, +1.8 pt tracking | title-case fallback at large text |
| `type.annotation.serif` | 13–14 pt serif italic | define one family explicitly or remove role |
| `type.photo.time` | 11 pt neutral sans medium | adaptive local scrim |

---

## 10. Color, material, border, and elevation

### 10.1 Palette

| Token | Observed/proposed value | Role |
|---|---|---|
| `color.canvas` | `#FFFFFF` | root and sheet background |
| `color.text.primary` | near `#000000` | primary labels, rules, icons |
| `color.text.secondary` | approx. `#8A8A8F` proposed minimum | weekdays, section labels, descriptions |
| `color.text.tertiary` | avoid below accessible contrast for essential content | nonessential metadata only |
| `color.rule.strong` | black, 1 source px | major boundaries |
| `color.rule.subtle` | neutral gray, 1 source px | rows and cell boundaries |
| `color.overlay.time` | black at 45–60% alpha | photo time backing |
| `color.modal.dimming` | system dimming gray | parent context behind sheet |
| `color.photo` | user content, full color | primary memory evidence |
| `color.map` | Apple Map style | spatial context |

### 10.2 Material

- Core shell: flat opaque white.
- No glass blur is visible inside the app content.
- Modal backdrop uses standard dimming; the sheet itself is opaque.
- Meal images and map are the only major color fields.
- Photo-stack annotations add borders and shadows as a deliberate exception.
- Banner ads are blurred only in marketing screenshots; do not reproduce this blur in product UI.

### 10.3 Border grammar

- Strong black hairlines define major shell boundaries.
- Pale gray hairlines separate settings rows and calendar cells.
- Review uses a continuous thin rectangular border.
- Camera, Library, and Start Scan use detached L-shaped corner brackets.
- Photo-stack annotations use white image borders plus dark shadow.
- Cards, capsules, and rounded containers are otherwise absent.

### 10.4 Corner-radius grammar

- Main content: nearly no corner rounding.
- Modal sheet: large top corner radius, likely system sheet geometry.
- Buttons: no rounded rectangle except the sheet boundary; bracket motif replaces filled controls.
- Photo thumbnails: square corners in Photos/Calendar; map annotation photo frames also appear square.

---

## 11. Iconography, imagery, and photographic grammar

### 11.1 Icon system

- Magnifier, calendar, circled checkmark, ellipsis, close X, triangular month arrows, and disclosure chevrons are outline or solid monochrome symbols.
- Exact SF Symbols use is not proven, but the shapes are system-like.
- Icon-only toolbar controls require semantic labels and 44 pt targets.
- The brand mark is custom and must not be treated as an actionable control.

### 11.2 Photo treatment

- Photos remain natural and full color.
- Photos grid/calendar crops use aspect-fill.
- Photos surface uses square crops with minimal gaps.
- Calendar uses one representative image per occupied day.
- Map uses small square crops with physical-stack styling.
- No global color grading, rounded cards, or decorative filters are visible.
- Time is overlaid on photos; date and weekday remain outside the grid.

### 11.3 Contact-sheet grammar

The Photos screen resembles a photographic contact sheet:

- uniform thumbnail scale;
- chronological indexing;
- sparse incomplete rows retained;
- concise capture metadata;
- minimal container decoration;
- white page and black typographic index marks.

This grammar should remain consistent in any new Recap, Recipe, or Search surface. Adding floating cards or bento modules would break it.

### 11.4 Corner-bracket motif

The detached corner strokes visually reference viewfinder framing, crop marks, or registration marks but are not literal print crop marks. Use the project term **corner-bracket framing motif**. Limit it to primary acquisition/scan actions and ad framing; using it on every row would dilute recognition.

---

## 12. Data visualization and spatial encoding

### 12.1 Calendar encoding

| Visual variable | Encoded data | Current treatment | Required clarification |
|---|---|---|---|
| cell position | calendar date | 7-column month grid | locale-aware first weekday |
| image presence | at least one meal photo | full-cell thumbnail | define representative-photo rule |
| upper-trailing number | likely number of meals/photos | small white/gray count | clarify whether count is meals or photos |
| opacity | adjacent month / inactive date | dimmed image and number | preserve contrast for selectable overflow dates |
| blank cell | no meal | white | selected/today state still needed |

### 12.2 Map encoding

| Visual variable | Encoded data | Current treatment | Risk |
|---|---|---|---|
| geographic position | meal location | photo-stack annotation anchor | metadata accuracy/privacy |
| stack depth | likely meal density | more visible photo layers | no explicit count or scale |
| thumbnail imagery | representative meals | small square photos | visual clutter and privacy |
| top summary count | located meals in scope | `228 MEALS ON THE MAP` | unclear whether viewport or total |
| shadow/z-order | annotation separation | deep layered stack | can obscure map labels/geography |

### 12.3 Map reconstruction requirements

- Use MapKit annotations and clustering appropriate to zoom.
- Decide whether the top count is total located meals or meals in current viewport; label accordingly.
- Do not expose exact sensitive locations by default on share/export surfaces.
- Use a representative image plus count at low zoom.
- Keep Apple attribution and legal links visible.
- Support a list alternative for users who cannot efficiently operate the map.
- Apply selection styling independent of thumbnail contents.

---

## 13. Responsive, adaptive, accessibility, and localization analysis

### 13.1 Compact-width pressure points

1. Four text destinations plus meal count already occupy the full strip.
2. Brand lockup plus four toolbar icons leaves little reserve width.
3. Long Settings rows depend on English and small tracked text.
4. Calendar cells have limited room for date + count + image.
5. Two large bottom actions are safe at 428 pt but need adaptation in landscape and split view.

### 13.2 Dynamic Type requirements

- Do not scale the text tab strip beyond fit; reflow it into a scrollable semantic tab list or move metadata out of the row.
- Settings rows must support two lines and increased row height.
- Scan body and footnote need normal semantic text styles.
- Date/weekday header can stack vertically at accessibility sizes.
- Calendar may switch to list/day-summary mode at very large sizes.
- Camera/Library labels can remain one line but should reduce tracking before reducing size.

### 13.3 Accessibility risks visible from screenshots

| Risk | Evidence | Rebuild severity |
|---|---|---|
| low-contrast gray text | tab labels, weekdays, scan paragraph, footnote, chevrons | high |
| small icon-only targets | masthead actions, month arrows, close X | high |
| selected tab communicated mainly by gray/black weight | `NAV-02` | high |
| selected scan option shown only by a small black dot | `GRP-05` | medium-high |
| photo-overlaid calendar text lacks stable contrast | `DAT-02` | high |
| map clusters lack text/count/state | `DAT-04` | medium-high |
| all-caps wide tracking | settings/tab labels | medium-high |
| horizontal destination row has no localization headroom | `NAV-02` | high |
| ads embedded between memories | `GRP-04` | medium for reading continuity |
| no visible list alternative for map | `REF-04` | high |

### 13.4 Required semantic behavior

- Each tab announces label, selected state, and position.
- Each meal tile combines date, time, note/place summary when available, and photo count.
- Date section headers are headings, not separate focus stops unless interactive.
- Calendar cells announce full localized date, meal count, selected/today state.
- Map cluster announces location summary and number of meals.
- Camera and Library are buttons, not tabs.
- Scan range is one radio group with one selected value.
- Settings rows expose navigation semantics and descriptive labels.
- Decorative brand mark and corner brackets are hidden from accessibility trees.

### 13.5 Localization

- Current App Store listing is English only.
- Dot-separated destination labels do not scale to Korean, German, French, or many other languages.
- Wide tracking is inappropriate for Korean typography and should be reduced or removed.
- Month/day ordering must use locale-aware formatters.
- Weekday order and first day of week must follow locale/calendar settings.
- Recipe and recap names may be substantially longer than current English labels.
- Use semantic labels and layout adaptation rather than translating inside fixed-width artwork.

---

## 14. Reference decomposition: Borrow / Exclude / Transform

### Borrow

- Full-color user photos against a strict monochrome shell.
- Contact-sheet uniformity for chronological memory browsing.
- Date/weekday section headers with very little surrounding chrome.
- Persistent Camera/Library acquisition actions.
- Calendar as a dense visual retrieval index.
- Photo-based map annotations instead of generic pins.
- One-tap camera-roll catch-up as a prominent inline recovery loop.
- Hairline separators and a restrained radius system.
- Brand lockup and corner-bracket motif.
- Grouped Settings sheet with clear section hierarchy.

### Exclude

- Color-only or weight-only selected state in the destination strip.
- Destination labels and meal count compressed into one unscalable row.
- An empty day header without explanation.
- Excessive blank space after sparse photo rows or short modal tasks.
- Low-contrast gray body text and chevrons.
- A radio group where only the selected option has any control shape.
- Photo-stack map clusters without counts or selectable state.
- The extra serif italic type role unless formally defined.
- Large banner-ad whitespace that interrupts chronology.
- Applying corner brackets to every control.

### Transform for a production reconstruction

- Keep the brand shell but use native semantic components beneath it.
- Move meal count to the active-panel header or toolbar metadata.
- Add an underline/indicator to selected tabs.
- Keep three columns but compact incomplete-row spacing.
- Add calendar corner scrims and explicit today/selected states.
- Use muted map style and count-bearing photo clusters.
- Use a medium content-fitting scan sheet when possible.
- Convert Settings row typography to accessible tracked title case at large sizes/localized builds.
- Define the serif accent as one named token or remove it.
- Reserve ad space only after content is available and keep it visually distinct from personal memories.

### This / Not this

| This | Not this |
|---|---|
| Uniform contact-sheet grid | Masonry/Pinterest grid |
| Text tab strip | Segmented control capsule |
| Bottom acquisition bar | Bottom navigation tab bar |
| Inline catch-up banner | System alert |
| Thumbnail month calendar | Heatmap calendar |
| Photo-stack map annotation | Generic map pin |
| Large modal sheet | Full-screen root replacement |
| Grouped disclosure list | Dashboard cards |
| Corner-bracket framing motif | Literal print crop marks on all content |
| Editorial monochrome shell | Glassmorphism or fashion-magazine layout |

---

## 15. Reconstruction specification

### 15.1 Design thesis

```text
grumbl. should read as a private photographic index, not a nutrition tracker and not a
social feed. The interface is a white archival page structured by black hairlines,
geometric uppercase labels, a small custom brand lockup, and full-color meal evidence.
The core navigation exposes four retrieval lenses—Photos, Calendar, Map, Recipes—while
two persistent acquisition actions keep the capture loop one tap away. The contact-sheet
rhythm, thumbnail calendar, and photo-stack map annotations are the distinctive product
assets. Production reconstruction must retain these while replacing compressed custom
chrome with semantic, scalable controls and explicit selected, empty, loading, error,
and accessibility states.
```

### 15.2 Root layout rules

```text
MAIN ROOT
- Approximate target: 428×926 pt compact portrait.
- Use white canvas and black primary chrome.
- Safe-area status remains system-owned.
- Branded masthead: 60–64 pt.
- Destination tab region: 36–40 pt plus 1 px divider.
- Main content fills remaining space above acquisition bar.
- Acquisition bar: target 84–96 pt plus bottom safe area; faithful reference is ~113 pt.

MASTHEAD
- Leading inset: 20–22 pt.
- Brand mark: approximately 20–24 pt visual size.
- Wordmark: 28 pt baseline role.
- Trailing controls: 44×44 pt targets, 20–24 pt glyphs.
- Contextual select action appears only on Photos.

DESTINATION STRIP
- Four semantic tabs.
- Active: black + medium weight + non-color indicator.
- Inactive: secondary text color meeting contrast.
- Move meal count out when width is constrained.
- Do not shrink below 11–12 pt to force fit.

PHOTOS
- Vertical date-section collection.
- 3 equal square columns, 1–2 pt gap.
- Date header: leading date, trailing weekday.
- Sticky header behavior may be preserved.
- Time badge: top-leading adaptive scrim.
- Empty today: compact message/capture cue.

CALENDAR
- Month pager above 7×6 grid.
- Minimum 44 pt day targets.
- Representative thumbnail per occupied day.
- Date and count receive adaptive corner backing.
- Distinct today/selected/adjacent-month/focus states.

MAP
- Interactive MapKit map.
- Muted emphasis preferred.
- Low zoom: representative photo + numeric cluster count.
- Medium zoom: 2–4 layer photo stack.
- High zoom: individual meal annotations.
- Summary badge names whether count is total or viewport-specific.
- Keep attribution visible.

MODAL SHEETS
- Use system sheet presentation and dimming.
- One leading dismiss control and centered concise title.
- Scan may use medium detent when content fits.
- Settings can use large detent because list scrolls.
- Avoid stacked sheets.

SETTINGS
- Grouped List structure.
- 52–56 pt minimum rows.
- Semantic disclosure indicators.
- Long labels wrap at accessibility sizes.
- About lockup remains final group.
```

### 15.3 Component mapping

| Reference element | Target component | Native/custom | Required customization | State owner |
|---|---|---|---|---|
| `NAV-01` | SwiftUI toolbar/custom safe-area header | hybrid | brand lockup, action priority | root shell |
| `NAV-02` | custom semantic tab strip / `TabView` state | hybrid | text labels, indicator, overflow behavior | selected destination |
| `GRP-03` | `LazyVGrid` / collection view | native | square aspect-fill cells, tiny gaps | meal archive |
| `GRP-02` | `Section` with pinned header | native/hybrid | date/weekday composition | grouped meals |
| `GRP-01` | inline callout/banner | custom | CTA, dismiss, persistence | missed-meal prompt |
| `NAV-03` | safe-area bottom toolbar | hybrid | two equal bracket-framed buttons | acquisition coordinator |
| `DAT-01` | custom month grid using `Grid` | custom | locale calendar, image cells, states | calendar model |
| `DAT-03` | SwiftUI `Map` / MapKit | native | camera, muted emphasis, selection | map model |
| `DAT-04` | custom annotation / `MKAnnotationView` | custom | photo stack, cluster count, selected state | annotation cluster |
| `OVR-01` | `.sheet` | native | detents, custom header | scan coordinator |
| `GRP-05` | `Picker`/selection list | hybrid | monochrome row styling | scan range |
| `OVR-02` | `.sheet` + `NavigationStack` | native | large sheet, custom header | settings route |
| `GRP-06` | `List` grouped sections | native/hybrid | typography and rule styling | settings model |
| `ROW-01` | `NavigationLink` | native | tracked label within scaling limits | destination route |

### 15.4 Semantic tokens

| Token | Type | Light value | Dark value | Description |
|---|---|---|---|---|
| `color.background.canvas` | color | `#FFFFFF` | `#0A0A0A` proposed | root archive canvas |
| `color.background.sheet` | color | `#FFFFFF` | semantic secondary background | modal surface |
| `color.text.primary` | color | `#000000` | `#FFFFFF` | primary chrome |
| `color.text.secondary` | color | proposed `#6F6F73` minimum | semantic secondary | supporting labels |
| `color.rule.strong` | color | `#000000` | `#FFFFFF` | major hairline |
| `color.rule.subtle` | color | proposed `#D4D4D6` | semantic separator | row/cell line |
| `space.inline.page` | dimension | `22 pt` | same | text/list alignment |
| `space.grid.photoGap` | dimension | `1.5 pt` | same | Photos grid |
| `space.stack.section` | dimension | `24 pt` baseline | same | date/settings groups |
| `size.toolbar.target` | dimension | `44 pt` | same | icon actions |
| `size.bottomAction.height` | dimension | `84–96 pt + safe area` | same | production target |
| `radius.sheet.top` | dimension | system | system | modal sheet |
| `stroke.hairline` | dimension | `1 px` | `1 px` | visual divider |
| `type.nav.tab` | typography | 12 pt geometric sans | same | archive destination |
| `type.section.date` | typography | 19 pt geometric sans | same | Photos date |
| `type.body` | typography | 16/22 pt neutral sans | same | scan explanatory text |
| `type.annotation.serif` | typography | 13–14 pt serif italic | same | explicitly defined optional accent |

### 15.5 State matrix

| Surface/component | Default | Selected | Loading | Empty | Error | Large text | Dark |
|---|---|---|---|---|---|---|---|
| Text tab strip | one active | underline + weight | preserve labels | n/a | n/a | scroll/reflow | contrast-calibrated |
| Photos archive | date sections | selected meal/selection mode | skeleton preserving grid | empty today/archive | retry/import diagnostics | date stacks, labels adapt | photos unchanged, chrome inverted |
| Meal tile | image + time | outline/check in select mode | placeholder | missing image | recovery state | semantic label unaffected | scrim recalibrated |
| Catch-up banner | message + CTA | pressed | scan status | hidden if no candidates | concise retry | multiline | contrast-calibrated |
| Calendar day | date/image/count | selected outline | thumbnail placeholder | white cell | metadata warning | alternate list mode | scrims/lines recalibrated |
| Map | clusters | selected cluster | incremental annotations | no located meals | map/list fallback | controls scale | muted dark map |
| Scan sheet | range selected | radio state | progress + cancel | no candidates | explain/retry | rows grow | semantic surfaces |
| Settings row | label/chevron | pressed | destination-specific | n/a | n/a | multiline/title case | semantic list style |
| Camera/Library | two actions | pressed | permission handoff | n/a | permission/error message | reduce tracking | inverted or semantic |

### 15.6 Asset production requirements

- Brand mark: vector, one-color, preserve white cutout.
- Wordmark: native text or vector lockup only where brand fidelity requires it; accessibility name remains native.
- Meal photos: local raster, aspect-fill, no baked metadata.
- Map annotation thumbnails: precomputed small thumbnails; avoid decoding full-resolution assets during pan/zoom.
- Icons: SF Symbols where an exact semantic match exists; custom only when required.
- Corner brackets: vector/CAShapeLayer/SwiftUI shape with consistent stroke and optical inset.
- Time/calendar labels: always native text.
- Ad screenshots: no stored or reconstructed blurred creative.
- Color space: sRGB baseline; preserve photo metadata/orientation.
- Performance: thumbnail caching, cancellation during fast scroll, stable IDs, incremental MapKit annotation diffing.

### 15.7 iOS / SwiftUI implementation language

```text
Use a RootArchiveView with a safe-area-aware custom masthead and semantic destination
state. Keep navigation selection separate from toolbar actions. A TabView may own panel
state without exposing its default tab-bar appearance, or a custom tab strip may drive an
enum-backed switch while preserving accessibility selected traits.

Photos uses ScrollView + LazyVStack of date groups. Use pinnedViews only if sticky headers
remain readable over photos. Each group contains a 3-column LazyVGrid with square Geometry
or aspectRatio(1, contentMode: .fill). Load cached thumbnails by stable meal ID. The entire
meal tile is a Button/NavigationLink; time is an overlay and not a separate action.

Camera and Library live in safeAreaInset(edge: .bottom), not in TabView navigation.
Use two Buttons with rectangular content shapes and custom corner-bracket backgrounds.

Calendar uses Calendar/DateComponents to generate a locale-correct 7-column grid. Avoid
assuming Sunday or Monday start. Make each day one semantic Button. Use image luminance or
a fixed local scrim to keep day/count text readable.

Map uses Map with a camera-position model. If production clustering and annotation reuse
are needed, bridge MKMapView/MKAnnotationView. Use stable cluster identifiers and cached
representative thumbnails. Keep the map camera and selection state when navigating away.

Present Scan and Settings with sheet(item:) or dedicated Boolean state. Scan should expose
presentationDetents that fit the content and progress state. Settings can use a large
sheet containing NavigationStack + List. Use native disclosure semantics and toolbar
dismissal even if the visual header is custom.

All visible typography uses semantic roles and supports Dynamic Type. Constrain tracking
per role and disable exaggerated uppercase spacing for Korean/localized strings. Provide
explicit accessibility labels for every icon and combine decorative bracket/brand layers.
```

---

## 16. Explicit prohibitions and non-goals

- Do not call the top destination line an Apple tab bar.
- Do not call Camera/Library navigation tabs.
- Do not replace the uniform grid with masonry.
- Do not wrap every date, meal, setting, or tool in a rounded card.
- Do not add glass blur to the core shell.
- Do not add colored accent chrome; color belongs primarily to user photography and map content.
- Do not rely only on gray/black or font weight for selected tab state.
- Do not retain low-contrast gray for essential body text or disclosure cues.
- Do not force localized labels into the current tracked uppercase widths.
- Do not infer that the calendar count means meals rather than photos until confirmed.
- Do not infer that photo stacks are MapKit clusters until source/behavior is inspected.
- Do not reproduce blurred ad creative.
- Do not expose the brand mark as a separate accessible element from the wordmark.
- Do not add calorie, macro, streak, or social-feed modules to this reconstruction.
- Preserve: photo-first hierarchy, date indexing, monochrome shell, contact-sheet grid, acquisition immediacy, calendar/map retrieval, and corner-bracket identity.
- Acceptable deviation: resize controls, raise contrast, adapt tabs, and reduce modal/bottom-bar height for accessibility and device classes.
- Unacceptable substitution: generic white cards with shadows, colored tab icons, bento dashboards, or a nutrition-tracking home screen.

---

## 17. Visual QA and acceptance criteria

### 17.1 Reference-match checkpoints

| Check | Target | Tolerance | Verification |
|---|---|---|---|
| all public references covered | six screenshots, exact App Store order | exact | source map + manifest |
| shared masthead alignment | brand and toolbar anchors consistent across 01–04 | ±2 pt | overlay captures |
| destination selection | Photos/Calendar/Map active states match corresponding screens | exact semantics | state fixtures |
| photo grid | three equal square columns | ±1 px column/gutter | screenshot measurement |
| sparse grid | source order and left-fill preserved | exact | 1/4/6-item fixtures |
| date header hierarchy | date first, weekday second | same squint order | grayscale thumbnail |
| bottom acquisition bar | two equal full-row targets | ±2 pt | hit-test overlay |
| calendar geometry | 7 columns × 6 weeks when needed | exact date model | deterministic month tests |
| calendar contrast | date/count readable across image fixtures | WCAG-oriented contrast review | luminance fixtures |
| map attribution | Apple logo/legal remain visible | no persistent obstruction | map screenshots |
| map clusters | count and selected state legible | no ambiguous deep piles at low zoom | zoom matrix |
| scan range semantics | exactly one selected option | exact | accessibility/UI tests |
| sheet dismissal | visible and semantic | exact | UI tests |
| settings rows | no truncation at supported text sizes | no information loss | Dynamic Type matrix |
| dark mode if added | same hierarchy, photos unchanged | paired review | light/dark captures |

### 17.2 Required capture matrix

| Device/class | Theme | Text size | State |
|---|---|---|---|
| 428×926 pt compact portrait | light | default | all six reference-equivalent surfaces |
| 393×852 pt compact portrait | light | default | all main surfaces |
| compact portrait | light | accessibility XL | tab strip, Scan, Settings |
| compact portrait | light | default | empty archive, empty day, 1/4/6 photo days |
| compact portrait | light | default | calendar today/selected/adjacent month |
| compact portrait | light | default | map low/medium/high zoom and selection |
| compact landscape | light | default | masthead/tab/action-bar adaptation |
| iPad regular | light/dark | default | expanded archive/map/settings |
| any dark mode target | dark | default + XL | all semantic surfaces |

### 17.3 Acceptance statement

```text
PASS when:
- All six public screenshots are traceably represented.
- The interface remains identifiable as a monochrome photographic contact sheet.
- Photos, Calendar, Map, and Recipes are semantic destinations with a clear selected state.
- Camera and Library remain immediate actions, not navigation.
- Three-column chronology, thumbnail calendar, and photo-stack map grammar are preserved.
- Text contrast, target size, localization, and Dynamic Type defects are corrected.
- No essential state depends only on color, weight, or an unlabeled dot.

HOLD when:
- Exact calendar count semantics, select-mode action, map cluster behavior, or scan review
  flow are required for implementation but remain unverified.
- Original source code reveals materially different navigation or state ownership.

FAIL when:
- The archive becomes a card dashboard or masonry feed.
- Colored chrome competes with meal photography.
- The destination strip truncates or shrinks below readable size.
- Camera/Library are misimplemented as tabs.
- Calendar labels disappear over photos.
- Map piles obscure location without count/selection semantics.
- Large text or localization causes clipping.
```

---

## 18. Uncertainty and decision register

| ID | Question | Status | Alternatives | Evidence needed | Blocks faithful rebuild |
|---|---|---|---|---|---|
| `U-01` | What does the circled checkmark action do? | inferred | select meals / mark review complete / another mode | interaction capture or source | yes for toolbar behavior |
| `U-02` | What exact action does the calendar toolbar icon perform? | inferred | jump to date / date picker / today | interaction capture | yes for toolbar behavior |
| `U-03` | Is the top destination system backed by TabView or custom routing? | unknown | TabView / enum switch / navigation routes | source inspection | no for visual rebuild |
| `U-04` | Does the meal count belong to entire archive or current filter? | inferred | total archive / current query | filtered-state capture | yes for metadata label |
| `U-05` | Why is MAY 26 shown with no meal content? | unknown | today marker / empty date section / transient state | live app behavior | no |
| `U-06` | Does calendar upper-trailing count mean photos or grouped meals? | unknown | photo count / meal count | source/data fixture | yes for semantics |
| `U-07` | What is the selected/today calendar styling? | unknown | outline / invert / badge | interaction captures | yes for complete calendar |
| `U-08` | Are map stacks generated by MapKit clustering? | unknown | MKClusterAnnotation / custom regional aggregation | source/zoom capture | yes for behavior |
| `U-09` | Does map summary count reflect viewport or total geotagged archive? | unknown | viewport / total | pan/zoom capture | yes for label |
| `U-10` | What occurs after Start Scan? | unknown | progress in same sheet / review gallery / new sheet | interaction capture | yes for end-to-end scan flow |
| `U-11` | Is the serif italic accent an intentional third family? | inferred | named serif / image-rendered text / legacy styling | design tokens/source | no |
| `U-12` | Are main header and bottom actions fixed while Photos scrolls? | inferred | fixed / partially collapsing | scroll capture | yes for exact shell |
| `U-13` | Does the product support dark mode despite no public reference? | unknown | light-only / semantic dark | app inspection | no for light rebuild |
| `U-14` | Exact target device represented by 1284×2778 assets | inferred | 428×926 pt class / marketing export | source metadata | no |

---

## 19. Source register

| Source ID | Claim or term | Authority | Document | Verified |
|---|---|---|---|---:|
| `SRC-01` | six screenshots, app description, version 1.2, metadata, accessibility declaration | official store listing | `https://apps.apple.com/us/app/grumbl/id6772917460` | 2026-08-09 |
| `SRC-02` | exact screenshot asset order, dimensions, hashes | Apple public Lookup + Apple CDN | references/source-map.md | 2026-08-09 |
| `SRC-03` | map, annotations, clustering, muted map emphasis, attribution | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/maps` | 2026-08-09 |
| `SRC-04` | toolbar definition and action grouping | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/toolbars` | 2026-08-09 |
| `SRC-05` | sheets and bounded modal tasks | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/sheets` | 2026-08-09 |
| `SRC-06` | lists, rows, and disclosure indicators | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/lists-and-tables` | 2026-08-09 |
| `SRC-07` | tab list, tab, tabpanel semantics | `W3C_GUIDANCE` | `https://www.w3.org/WAI/ARIA/apg/patterns/tabs/` | 2026-08-09 |
| `SRC-08` | target size and drag alternatives for web reconstruction | `STANDARD_NORMATIVE` | `https://www.w3.org/TR/WCAG22/` | 2026-08-09 |

---

## 20. Final build brief

```text
SURFACE
Complete public App Store set: Photos dense, Photos sparse, Calendar, Map, Scan Camera
Roll, Settings.

TARGET
iOS 17+; SwiftUI with MapKit bridge where clustering control requires it.

ARCHETYPE
Private photo archive with date, calendar, map, recipe, search, recap, and import lenses.

STYLE
Monochrome Contact-Sheet Utility: white archival canvas, black rules/type/icons, neutral
gray metadata, full-color user photography, geometric tracked uppercase, limited serif
italic annotation, and corner-bracket primary actions.

NAVIGATION
Custom semantic text tab strip for Photos/Calendar/Map/Recipes. Branded top toolbar for
search/date/contextual selection/more. Camera and Library are persistent actions, not tabs.
Scan and Settings are modal sheets.

LAYOUT
Approx. 428×926 pt at 3×. 20–23 pt text insets. 60–64 pt masthead, 36–40 pt tab strip,
3-column square Photos grid, 7-column month grid, map filling content, 84–96 pt proposed
bottom acquisition region, full-width grouped Settings rows.

TYPOGRAPHY
Geometric sans brand/control system + neutral sans body. Explicitly define or remove the
visible serif italic accent. Reduce excessive tracking for small, localized, or large text.

COLOR/MATERIAL
Opaque black/white/gray shell. User photos and map supply color. No glass. Hairlines are
primary structure. Shadow is limited to map photo stacks.

COMPONENTS
Brand lockup, toolbar, text tab strip, meal count, inline catch-up banner, date sections,
uniform LazyVGrid, time badges, inline ad slot, bottom action bar, month pager/calendar,
MapKit photo clusters, modal sheet, radio group, primary scan action, grouped disclosure
List, About row.

INTERACTION
Capture/select photos, switch archive lens, search/jump/select, review missed meals,
open meal/day/map group, choose scan range, start scan, navigate settings. Preserve each
surface state and provide non-gesture alternatives.

ADAPTATION
Move meal count out of crowded tab row; scroll/reflow tabs; wrap Settings rows; provide
large-text Calendar alternative; cluster map by zoom; reduce bottom/sheet empty space.

ACCESSIBILITY
44 pt targets, semantic selected tabs, radio semantics, adaptive photo text contrast,
full date/count labels, map list alternative, localized date/calendar behavior, Dynamic
Type, Reduce Motion, decorative brand/brackets hidden.

ASSETS
Vector mark and bracket shapes, native word/metadata text, cached square meal thumbnails,
representative map cluster thumbnails, no committed third-party App Store screenshots.

EXCLUSIONS
Masonry feed, colored shell, glass panels, card dashboard, nutrition metrics, generic tab
icons, unreadable tracked uppercase, blurred ad recreation, and unverified inferred states.

QA GATE
Six-reference traceability; exact 3-column and 7-column geometry; selected destinations
remain clear; sparse/empty states intentional; calendar labels retain contrast; map
clusters expose count/selection; all labels survive compact width and accessibility text.
```

---

## Revision history

| Revision | Date | Change |
|---|---:|---|
| 1 | 2026-08-09 | Initial complete analysis of all six public US App Store iPhone screenshots |
