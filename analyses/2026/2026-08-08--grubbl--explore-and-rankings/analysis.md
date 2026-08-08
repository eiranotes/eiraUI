---
schema_version: "1.0.0"
analysis_id: "UIR-20260808-001"
status: "complete"
created_at: "2026-08-08"
updated_at: "2026-08-08"
title: "Grubbl — Explore map and Rankings UI reference reconstruction"
subject:
  product_name: "Grubbl: Restaurant Discovery"
  product_type: "app"
  surface_name: "Explore map and Rankings"
  platform: "iOS"
  locale: "en"
  theme: "light"
target:
  platform: "iOS"
  framework: "SwiftUI / MapKit"
reference_storage: "link_only"
template_version: "1.0.0"
---

# Grubbl — Explore map and Rankings UI Reference Reconstruction

## 0. Reconstruction directive

> **Pattern:** `map-first local discovery interface + vertically stacked ranked content rails`  
> **Primary style:** `High-Chroma Local Discovery Utility` (`PROJECT_DEFINED`), grounded in `playful flat consumer utility UI` (`INDUSTRY_CONVENTIONAL`)  
> **Platform shell:** iOS map surface with custom annotations, contextual overlay action, vertical scroll, horizontal content rails, media cards, and icon buttons  
> **Core composition:** desaturated map or white canvas under saturated restaurant-state accents; place identity is carried by map annotations or photography; rankings use repeated section headers and horizontally scrollable ranked cards  
> **Rebuild rule:** keep the map visually primary; use 32–36 pt visual annotations with at least 44 pt interactive hit regions; cluster or declutter before labels overlap; use 16–20 pt page insets and cards occupying about 72–76% of compact viewport width so the next card remains partially visible  
> **Do not introduce:** heatmap semantics, proportional marker sizing without a defined metric, color-only meaning, unbounded marker overlap, glass panels, a generic AI dashboard, or a card grid that removes the horizontal ranking sequence

### One-paragraph reconstruction language

```text
Build a restaurant-first discovery product whose Explore surface is a full-bleed, muted
2D map populated by high-chroma custom point annotations that expose a compact numeric
signal and optional ranked-status badge. Keep one labeled contextual action anchored near
the bottom-trailing safe area. When a place is selected, preserve map context and reveal
the restaurant in a subordinate place card or bottom sheet. Build Rankings as a vertical
sequence of titled sections; each section contains a horizontally scrollable rail of
photo-led media cards with an ordinal rank badge, bottom text-legibility scrim, restaurant
name, and an adjacent section-level edit icon button. The visual system is energetic but
flat: white or neutral surfaces, saturated pink/cyan/orange/green accents, rounded geometry,
system-like sans typography, minimal shadow, and no decorative translucency.
```

---

## 1. Scope and evidence

### 1.1 Subject

| Field | Value |
|---|---|
| Product | Grubbl: Restaurant Discovery |
| Surface / route / state | Official marketing references for Explore and Rankings |
| Product type | Local restaurant discovery, curation, and social utility |
| Source platform | iPhone / iOS |
| Target platform | iOS / SwiftUI reconstruction baseline |
| Locale | English |
| Theme | Light |
| Analysis purpose | Selective borrowing and reconstruction baseline |
| Out of scope | Complete tab structure, authenticated states, restaurant detail anatomy, feed, profile, leaderboard, onboarding, exact production fonts, dark mode, animation timing, backend ranking formula |

### 1.2 Reference inventory

| Ref ID | Source type | Locator or repository path | Capture date | Viewport | Device/browser | Transformation | Storage policy |
|---|---|---|---:|---|---|---|---|
| `REF-01` | official marketing image | `https://grubbl.app/images/mocks/explore.png` | 2026-08-08 | search-resolved 512×512 px preview | original device viewport unknown | externally resized/cropped preview | `link_only` |
| `REF-02` | official marketing image | `https://grubbl.app/images/mocks/rankings.png` | 2026-08-08 | search-resolved 512×512 px preview | original device viewport unknown | externally resized/cropped preview | `link_only` |
| `REF-03` | official product page | `https://grubbl.app/` | 2026-08-08 | not applicable | web | text and image inventory | `link_only` |
| `REF-04` | official App Store listing | `https://apps.apple.com/us/app/grubbl-restaurant-discovery/id6747157430` | 2026-08-08 | not applicable | App Store web | listing metadata and version history | `link_only` |

### 1.3 Evidence limitations

- `[U]` The official image files could not be stored in this public repository; only source locators are retained.
- `[U]` The search-resolved square previews may crop the original phone screenshots, so absolute source-pixel geometry is approximate.
- `[U]` The exact top-level tab destinations and selected-tab treatment are not visible.
- `[U]` Exact font family, variable axes, point sizes, and Dynamic Type behavior are not inspectable.
- `[U]` Pressed, selected, disabled, loading, empty, error, and offline states are not visible.
- `[U]` Marker clustering, map zoom thresholds, and annotation collision rules cannot be proven from one still image.
- `[U]` The semantic meaning of orange, green, and magenta marker colors is not published in the available source.
- `[U]` The exact metric shown inside each map marker is strongly consistent with a restaurant rating but is not explicitly labeled in the image.
- `[U]` The crown badge is consistent with Grubbl's published Top 100 feature, but the screenshot itself does not label it.
- `[U]` Accessibility semantics cannot be inferred from pixels. The App Store listing merely says the developer has not declared supported accessibility features; this is not evidence that no accessibility support exists.

### 1.4 Evidence labels used

`[O] OBSERVED` · `[M] MEASURED` · `[S] SAMPLED` · `[I] INFERRED` · `[P] PROPOSED` · `[U] UNKNOWN`

---

## 2. Reference overview

### 2.1 Literal description

#### `REF-01` — Explore

```text
The visible frame is almost entirely occupied by a light, low-saturation street map.
Dozens of colored circular symbols sit over geographic locations. Most symbols contain a
single decimal number in white. Several symbols have a small crown-like attachment above
the circle. Orange, green, and magenta symbol fills coexist on the same map. Symbols are
densely packed and overlap in the central and right portions of the frame. Near the
bottom-trailing edge is a cyan rounded rectangular control with an icon and the text
“Ask Grubbl AI.” The control is visually separated from the map but does not sit inside
a larger panel.
```

#### `REF-02` — Rankings

```text
The visible frame has a light background and a vertically repeated section structure.
Each section begins with a left-aligned bold title and a small circular magenta control
with a pencil glyph near the trailing edge. Beneath the title is a horizontal sequence of
large rounded photographic tiles. One full tile and part of the next tile remain visible,
indicating additional horizontal content. Each tile contains a restaurant photograph,
a hot-pink rank label such as “#1” near the upper-leading corner, and a restaurant name
near the bottom over a darkened image area. Thin horizontal separators divide the
vertically stacked sections.
```

### 2.2 Interface archetype

| Field | Classification | Authority | Evidence | Confidence |
|---|---|---|---|---:|
| Primary archetype | Map-first local discovery interface | `INDUSTRY_CONVENTIONAL` | Full-surface geographic map, place annotations, official Explore description | 0.99 |
| Secondary archetype | Ranked collection browser | `INDUSTRY_CONVENTIONAL` | Repeated titled horizontal rails with ordinal labels | 0.98 |
| Supporting archetype | Social curation utility | `INDUSTRY_CONVENTIONAL` | Love / Save / Avoid, check-ins, reviews, rankings, sharing | 0.98 |
| Supporting archetype | Conversational recommendation assistant | `INDUSTRY_CONVENTIONAL` | “Ask Grubbl AI” action and official AI description | 0.99 |
| Navigation model | Persistent top-level destinations, exact structure unknown | generic / `[I]` | Multiple dedicated product surfaces are documented, but the navigation is cropped | 0.55 |
| Content model | Restaurants as primary objects; reactions, photos, reviews, and check-ins as evidence; rankings as aggregates | product model | Official product descriptions and screenshots | 0.98 |

### 2.3 Reading order and focal hierarchy

#### Explore

| Order | Element ID | What attracts attention | Mechanism |
|---:|---|---|---|
| 1 | `DAT-02` | Dense colored rating annotations | Saturation, repetition, contrast, central coverage |
| 2 | `ACT-01` | “Ask Grubbl AI” action | Cyan fill, text label, isolated bottom-trailing placement |
| 3 | `DAT-01` | Geographic context | Full-frame area and street geometry |
| 4 | `DAT-03` | Crown status indicators | Distinct silhouette above selected markers |

**Squint-test result:** the colored marker field becomes the dominant visual mass; the map acts as a quiet substrate.  
**25%-thumbnail result:** marker density and the cyan AI action survive; street labels and individual restaurant values become less reliable.  
**Competing focal points:** the AI action competes with nearby map symbols when both occupy the bottom-trailing region.

#### Rankings

| Order | Element ID | What attracts attention | Mechanism |
|---:|---|---|---|
| 1 | `ROW-01` | Restaurant photography | Area, contrast, semantic content |
| 2 | `DAT-04` | Ordinal rank badge | Saturated magenta, concise number, upper-leading placement |
| 3 | `TXT-01` | Section title | Bold weight and whitespace isolation |
| 4 | `ACT-02` | Edit action | Magenta circle and trailing position |

**Squint-test result:** photographs form the first layer, magenta labels/actions the second, section titles the third.  
**25%-thumbnail result:** the ranking sequence and horizontal-rail composition remain legible; restaurant names may not.  
**Competing focal points:** repeated magenta edit buttons can compete with rank badges if their size or saturation is increased.

---

## 3. Terminology normalization summary

| Raw description | Canonical term | Authority class | Source | Platform scope | Alias / nearby term | Why this term fits |
|---|---|---|---|---|---|---|
| “지도 전체 화면” | interactive map / map view | `PLATFORM_OFFICIAL` | Apple HIG — Maps | Apple platforms | map canvas | Geographic content is the principal interactive surface |
| “숫자 들어간 동그란 핀” | custom map annotation | `PLATFORM_OFFICIAL` | Apple MapKit | Apple platforms | annotation view, point symbol | A custom visual is anchored to a map coordinate |
| “색깔 점 지도” | point-symbol map | `INDUSTRY_CONVENTIONAL` | cartographic practice | cross-platform | point map | Discrete locations are encoded by individual symbols; it is not a choropleth or heatmap |
| “핀이 겹쳐 보임” | overplotting | `INDUSTRY_CONVENTIONAL` | information visualization practice | cross-platform | annotation collision | Multiple symbols occupy insufficient screen space and obscure one another |
| “핀 묶기” | annotation clustering | `PLATFORM_OFFICIAL` | Apple MapKit | Apple platforms | marker clustering | Nearby map annotations are represented by an aggregate symbol at low zoom |
| “겹침 방지” | decluttering / collision avoidance | `INDUSTRY_CONVENTIONAL` | cartographic practice | cross-platform | label placement | Symbols are selectively hidden, shifted, prioritized, or clustered |
| “왕관 붙은 핀” | supplemental status badge on an annotation | `INDUSTRY_CONVENTIONAL` | generic UI vocabulary | cross-platform | crown indicator | A secondary symbol qualifies the place annotation |
| “하단 AI pill 버튼” | floating contextual action | `INDUSTRY_CONVENTIONAL` | generic UI vocabulary | cross-platform | nearest Material analogue: extended FAB | It floats over the content and contains icon plus label; iOS has no native FAB component |
| “사진 카드” | media card | `INDUSTRY_CONVENTIONAL` | design-system vocabulary | cross-platform | image tile | Image, label, status, and interaction form one bounded object |
| “가로로 넘기는 카드 줄” | horizontal scrolling content rail | `INDUSTRY_CONVENTIONAL` | content UI practice | cross-platform | carousel | A sequence scrolls horizontally within a vertically stacked page |
| “다음 카드가 일부 보임” | peek affordance | `INDUSTRY_CONVENTIONAL` | interaction-design practice | cross-platform | overflow cue | Partial visibility communicates that horizontal content continues |
| “#1 딱지” | ordinal rank badge | `INDUSTRY_CONVENTIONAL` | generic UI vocabulary | cross-platform | rank label | The element communicates ordering, not input, filtering, or status selection |
| “사진 아래 검은 그라데이션” | text-legibility scrim | `INDUSTRY_CONVENTIONAL` | media UI practice | cross-platform | gradient overlay | The darkened region increases contrast for overlaid text |
| “분홍색 연필 동그라미” | circular icon button | `PLATFORM_OFFICIAL` / generic | Apple HIG — Buttons | Apple platforms | edit action | A single glyph triggers an action; the visible circle is not the complete semantic label |
| “구역 사이 선” | section separator | `INDUSTRY_CONVENTIONAL` | generic UI vocabulary | cross-platform | divider | It separates repeated content groups |
| “Love / Save / Avoid” | reaction taxonomy | `PROJECT_DEFINED` | Grubbl product language | Grubbl | tri-state curation model | Three named reactions place restaurants into distinct user-intent states |
| “Best Of 목록” | curated ranking list | `INDUSTRY_CONVENTIONAL` | collection UI practice | cross-platform | ordered collection | The user assembles an ordered set around a theme |
| “핀 누르면 식당 정보” | place card / bottom sheet presentation | `PLATFORM_OFFICIAL` + `[P]` | Apple HIG — Maps | Apple platforms | detail sheet | A subordinate surface can reveal place details while preserving map context |

### 3.1 Primary style classification

| Field | Value |
|---|---|
| Primary style label | Playful flat consumer utility UI |
| Authority | `INDUSTRY_CONVENTIONAL` |
| Observable defining traits | Light neutral canvas; saturated functional accents; rounded symbols and cards; system-like sans typography; photo-led content; little texture; limited elevation; compact, direct labels |
| Project label | High-Chroma Local Discovery Utility |
| Project-label definition | A task-oriented local-discovery UI in which saturated colors distinguish actions, status, ranking, or activity over restrained map and content surfaces |
| Secondary influences | Social discovery, gamified ranking, conversational assistant, map-first utility |
| Labels rejected | glassmorphism, neumorphism, editorial UI, skeuomorphism, neobrutalism, dashboard UI |
| Reason rejected | No translucent blurred layers, embossed surfaces, publication-like typography, real-world material imitation, heavy brutalist framing, or multi-metric dashboard composition are visible |

---

## 4. Frame, geometry, and layout system

### 4.1 Coordinate system

| Field | Value |
|---|---|
| Source viewport | 512×512 px search-resolved previews |
| Origin | top-left |
| Normalized space | 1000×1000 |
| Platform point/CSS conversion known | no |
| Scale caveat | The preview may crop or resize the original mobile screenshots; absolute measurements are approximate and must be recalibrated from native captures before faithful implementation |

### 4.2 Root shell

#### Explore

| Property | Observation | Measurement | Evidence | Rebuild directive |
|---|---|---|---|---|
| Safe area / system chrome | Not visible in the crop | unknown | `[U]` | Respect target safe areas; do not infer hidden chrome |
| Root background | Map imagery | full visible frame | `[O]` | Use the map as the root content surface |
| Scroll axis | Spatial pan/zoom rather than document scroll | not measurable | `[I]` | Permit map pan and zoom; avoid vertical page scroll on the core Explore state |
| Fixed or sticky regions | AI action appears anchored over the map | approx. bottom-trailing | `[O/I]` | Overlay the action above map content and safe area |
| Content maximum width | Not applicable | full width | `[O]` | Map fills available content bounds |
| Outer insets | None for map; overlay control has edge inset | approx. 12–20 source px | `[M]` | Use 16 pt trailing and bottom inset after safe-area calibration |

#### Rankings

| Property | Observation | Measurement | Evidence | Rebuild directive |
|---|---|---|---|---|
| Root background | Near-white canvas | full visible frame | `[O]` | Use one flat canvas; do not wrap the page in a raised panel |
| Scroll axis | Primary vertical, nested horizontal rails | inferred from repeated sections and partial cards | `[O/I]` | Vertical parent scroll with horizontal child rails |
| Fixed or sticky regions | None established by crop | unknown | `[U]` | Keep headers nonsticky unless product testing supports it |
| Content maximum width | Compact handset width | 512 px preview | `[O]` | Use compact-width layout; center with max width only on larger devices |
| Outer insets | Titles/cards inset from edges | approx. 18–22 source px | `[M]` | Use 16–20 pt inline content inset |
| Section separators | Full-width or near-full-width thin lines | approx. 1 source px | `[M]` | Use subtle 1-pixel separator with sufficient contrast |

### 4.3 Layout model

| Surface | Primary layout | Columns or panes | Alignment anchors | Section rhythm | Density | Overflow |
|---|---|---|---|---|---|---|
| Explore | custom overlay on full-bleed map | one map plane + overlay controls | geographic coordinates; safe-area trailing/bottom | not applicable | high visual density in marker field | spatial pan/zoom; marker selection |
| Rankings | vertical stack of section header + horizontal rail | one vertical column; cards in horizontal sequence | shared page inset and header baseline | approximately 28–36 px between major sections | regular | horizontal rails expose a partial next card |

### 4.4 Major region map

| Region ID | Ref ID | Approx. source bbox `x,y,w,h` | Normalized bbox | Role | Layout relationship |
|---|---|---|---|---|---|
| `SUR-01` | `REF-01` | `0,0,512,512` | `0,0,1000,1000` | root map surface | contains geographic layer, annotations, overlay action |
| `DAT-01` | `REF-01` | `0,0,512,512` | `0,0,1000,1000` | map imagery | base layer below symbols |
| `DAT-02` | `REF-01` | distributed | distributed | restaurant annotation field | anchored to map coordinates |
| `ACT-01` | `REF-01` | approx. `322,458,178,42` | approx. `629,895,348,82` | contextual AI action | overlay at bottom-trailing |
| `SUR-02` | `REF-02` | `0,0,512,512` | `0,0,1000,1000` | rankings canvas | contains vertical section stack |
| `GRP-01` | `REF-02` | approx. `18,70,494,304` | approx. `35,137,965,594` | ranking section | header above horizontal rail |
| `GRP-02` | `REF-02` | approx. `18,138,494,220` | approx. `35,270,965,430` | horizontal content rail | child of ranking section |
| `ROW-01` | `REF-02` | approx. `18,138,286,220` | approx. `35,270,559,430` | ranked media card | first card in rail |

### 4.5 Spacing reconstruction

| Token candidate | Preview observation | Proposed semantic value | Usage |
|---|---|---|---|
| `space.inline.page` | approx. 18–22 px | 20 pt compact; 24 pt regular-width | Ranking titles, rails, list content |
| `space.stack.section` | approx. 28–36 px | 32 pt | Between ranked sections |
| `space.stack.headerToRail` | approx. 10–14 px | 12 pt | Section title row to cards |
| `space.inline.cardGap` | approx. 10–14 px | 12 pt | Between horizontal cards |
| `space.control.edge` | approx. 12–20 px | 16 pt plus safe area | Floating AI action |
| `space.card.content` | approx. 10–14 px | 12 pt | Rank badge and restaurant-name insets |

---

## 5. Element inventory

| ID | Ref | Approx. bbox | Literal observation | Canonical term | Authority | Hierarchy role | Interaction/state | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---:|
| `SUR-01` | REF-01 | full frame | Light street-map imagery | interactive map surface | `PLATFORM_OFFICIAL` | primary spatial canvas | pan / zoom / select | `[O/I]` | 0.95 |
| `DAT-01` | REF-01 | full frame | Desaturated road and place geometry | map base layer | `PLATFORM_OFFICIAL` | geographic context | changes with viewport | `[O]` | 1.00 |
| `DAT-02` | REF-01 | distributed | Colored circles containing decimal values | custom map annotations / point symbols | `PLATFORM_OFFICIAL` + conventional | primary discovery signals | tap-select inferred | `[O/I]` | 0.97 |
| `DAT-03` | REF-01 | attached to some markers | Small crown above a marker | supplemental status badge | conventional | ranked-status qualifier | nonseparate action | `[O/I]` | 0.84 |
| `ACT-01` | REF-01 | bottom-trailing | Cyan capsule with icon and “Ask Grubbl AI” | floating contextual action | conventional; Material analogue | secondary entry to assistant | tap opens assistant inferred | `[O/I]` | 0.98 |
| `SUR-02` | REF-02 | full frame | Flat near-white page | root content canvas | conventional | page substrate | vertical scroll inferred | `[O/I]` | 0.98 |
| `GRP-01` | REF-02 | repeated vertical block | Title row plus card rail | ranking section | conventional | groups one ranking theme | section edit action | `[O/I]` | 0.98 |
| `TXT-01` | REF-02 | section header leading | Bold left-aligned title | section heading | semantic/generic | names ranking theme | none | `[O]` | 0.99 |
| `ACT-02` | REF-02 | section header trailing | Magenta circle with pencil glyph | circular icon button | platform/generic | edit ranking | tap inferred | `[O/I]` | 0.96 |
| `GRP-02` | REF-02 | below header | Horizontal sequence with next card partially visible | horizontal scrolling content rail | conventional | ordered browsing | horizontal swipe | `[O/I]` | 0.99 |
| `ROW-01` | REF-02 | first card | Rounded restaurant photograph with text and rank | ranked media card | conventional | primary item | tap opens ranking item inferred | `[O/I]` | 0.98 |
| `DAT-04` | REF-02 | card top-leading | Hot-pink `#n` label | ordinal rank badge | conventional | communicates sequence | noninteractive | `[O]` | 1.00 |
| `SUR-03` | REF-02 | lower card image | Darkened region behind name | text-legibility scrim | conventional | supports contrast | none | `[O]` | 0.93 |
| `TXT-02` | REF-02 | card bottom-leading | White restaurant name | media-card title | conventional | object identity | part of card action | `[O]` | 0.98 |
| `DEC-01` | REF-02 | between sections | Thin horizontal rule | section separator | conventional | structural division | none | `[O]` | 0.96 |

### 5.1 Detailed element specification

#### `DAT-02` — Custom rating annotation field

**Traceability**

| Field | Value |
|---|---|
| Reference | REF-01 |
| Bounding box | distributed across map |
| Evidence status | `[O]` geometry; `[I]` metric semantics |
| Confidence | 0.97 visual term; 0.88 “rating” interpretation |
| Canonical term | custom map annotation / point symbol |
| Authority class | `PLATFORM_OFFICIAL` for MapKit annotation; `INDUSTRY_CONVENTIONAL` for point-symbol map |
| Source and section | Apple HIG Maps; MapKit annotations |
| Generic alias | marker, map symbol |
| Platform-specific mapping | SwiftUI `Annotation`; `MKAnnotationView` when clustering/collision control is required |

**Observed anatomy**

- Container: circular high-chroma fill.
- Content: one white decimal value.
- Leading/trailing elements: none.
- Supplemental element: crown-like badge on a subset.
- Border/separator: dark or high-contrast outline appears around some symbols.
- Surface/elevation: flat or minimally raised.
- Alignment: number optically centered.
- Relationship to neighbors: anchored to geographic locations; frequently overlaps nearby symbols.

**Content behavior**

- Minimum / maximum content: likely values such as `4.1`–`4.8`; exact range unknown.
- Wrapping: never wrap.
- Truncation: not applicable; reserve width for one decimal.
- Empty content: use a distinct unlabeled place marker or omit until a meaningful metric exists.
- Localization risk: decimal separator and numeral width can vary by locale.

**Interaction and state**

| State | Observed / inferred / proposed | Appearance | Behavior | Accessibility semantics |
|---|---|---|---|---|
| default | observed | colored circle with value | remains attached to coordinate | “Restaurant name, rating value” |
| selected | proposed | outline/scale/z-order emphasis | reveals place card; recenters only enough to keep card visible | selected trait/state |
| clustered | proposed | aggregate count or prioritized symbol | expands or reveals members on zoom/tap | “N restaurants in this area” |
| disabled/unavailable | proposed | muted neutral marker | no primary action or explains unavailable data | disabled only when truly unavailable |
| loading | proposed | stable placeholder geometry | avoid marker-field reflow | progress announced separately |
| offline | proposed | cached map/places where possible | explain stale data | status message |

**Rebuild directive**

```text
Render the visual symbol at 32–36 pt diameter but expose an interaction region of at
least 44×44 pt on iOS. Keep the decimal label on one line and optically centered. Preserve
constant visual size across ordinary annotations; do not imply magnitude with marker area
unless marker size is intentionally mapped to a named metric. Prioritize the selected
annotation, current viewport relevance, and ranked status. Before annotation labels
overlap materially, cluster, declutter, or reduce the visible set according to zoom and
screen density. Never rely on fill color alone to communicate category or sentiment.
```

#### `ACT-01` — “Ask Grubbl AI” floating contextual action

**Traceability**

| Field | Value |
|---|---|
| Reference | REF-01 |
| Bounding box | approx. `322,458,178,42` in preview |
| Evidence status | `[O]` appearance; `[I]` navigation result |
| Confidence | 0.98 |
| Canonical term | floating contextual action |
| Authority class | `INDUSTRY_CONVENTIONAL`; nearest Material component is an extended FAB |
| Generic alias | labeled floating action, overlay CTA |
| Platform-specific mapping | custom SwiftUI `Button` in map overlay; not a native iOS FAB |

**Observed anatomy**

- Container: cyan capsule or strongly rounded rectangle.
- Content: small leading icon plus label.
- Border: dark outline.
- Surface: opaque, not glass.
- Alignment: bottom-trailing with map visible underneath.
- Relationship to neighbors: visually isolated but may overlap nearby annotations.

**Interaction and state**

| State | Observed / inferred / proposed | Appearance | Behavior | Accessibility semantics |
|---|---|---|---|---|
| default | observed | cyan filled label button | enters AI assistant | button, “Ask Grubbl AI” |
| pressed | proposed | subtle opacity/scale change | triggers once | preserve label in accessibility name |
| loading | proposed | inline progress, disabled repeated submission | opens/awaits assistant | announce busy |
| unavailable | proposed | hidden only if feature cannot function; otherwise disabled with reason | explains network or service state | disabled plus hint |
| reduced motion | proposed | opacity transition only | no spring-scale dependency | unchanged semantics |

**Rebuild directive**

```text
Use a labeled button 46–50 pt high with a 12–16 pt horizontal content inset and one
leading icon. Anchor it 16 pt from the trailing safe area and 16 pt above the bottom
content boundary. Keep the button opaque. Reposition or temporarily collapse it when a
selected place card would cause overlap. Treat AI as a contextual secondary route from
discovery, not as the root page itself.
```

#### `GRP-02` — Horizontal scrolling content rail

**Observed anatomy**

- Container: horizontal scroll region under a section header.
- Content: ranked media cards in a single row.
- Spacing: regular inter-card gap.
- Overflow cue: the next card is partially visible.
- Relationship to parent: one rail per ranking theme.

**Interaction and state**

| State | Observed / inferred / proposed | Appearance | Behavior | Accessibility semantics |
|---|---|---|---|---|
| default | observed | first card plus next-card peek | horizontal scroll | named collection/section |
| scrolled | inferred | later ranks enter viewport | preserves vertical position | ordered item positions announced |
| empty | proposed | concise empty explanation + add action | no dead horizontal region | section remains discoverable |
| one item | proposed | single card; no fake peek | no unnecessary scroll | “1 item” |
| large text | proposed | card labels wrap or move below image | rail remains operable | no clipped names |
| keyboard/switch | proposed | explicit focus progression and scroll-to-focus | no drag-only requirement | ordered focus |

**Rebuild directive**

```text
Use card width equal to roughly 72–76% of the compact content width and a 12 pt gap,
leaving 12–20% of the next card visible. Preserve the order as a horizontal sequence.
Provide single-pointer and keyboard/focus alternatives; the rail must not require a
precision drag to reach later items.
```

#### `ROW-01` — Ranked media card

**Observed anatomy**

- Container: rounded rectangular image card with thin boundary.
- Content: edge-to-edge restaurant photograph.
- Leading overlay: ordinal rank badge at top-leading.
- Bottom overlay: restaurant name over a dark scrim.
- Surface/elevation: flat or very low elevation.
- Relationship: card is one ordered item in a ranking.

**Rebuild directive**

```text
Use a 4:3 or comparable landscape photo crop, 14–16 pt corner radius, and no more than a
subtle 1-pixel border or low shadow. Keep the rank badge 10–12 pt from top and leading
edges. Apply a bottom scrim only as strong as required for text contrast. The full card
is the primary action; rank badge and title are not separate targets. Preserve native
text rather than baking labels into the image.
```

#### `ACT-02` — Ranking edit icon button

**Observed anatomy**

- Container: small magenta circle.
- Content: pencil/edit glyph.
- Alignment: trailing edge of section header.
- Relationship: acts on the entire ranking section, not an individual card.

**Rebuild directive**

```text
Keep the visible circle optically compact but place it inside a minimum 44×44 pt touch
region. Provide the accessible name “Edit [ranking title].” Do not use magenta alone to
communicate that the section is editable; preserve the recognizable pencil glyph and
semantic button role.
```

---

## 6. Navigation and interaction model

### 6.1 Navigation

| Question | Finding | Evidence | Rebuild decision |
|---|---|---|---|
| What changes the top-level destination? | Not visible | `[U]`; product documents multiple dedicated surfaces | Do not invent tab labels from the crop; use target product information architecture |
| What opens a subordinate surface? | Tapping a nearby restaurant is documented to reveal restaurant content | official Explore description | Present a place card or detail surface |
| What is persistent? | Map context appears persistent under the AI action | `[O/I]` | Keep map loaded while overlays open |
| What preserves context? | A place card over the map is the appropriate platform pattern | `[P]` aligned with Apple map guidance | Offset map framing so selected marker remains visible |
| Back behavior | Not visible | `[U]` | Dismiss sheet/card back to unchanged viewport; full detail uses standard navigation back |
| Rankings edit | Pencil icon implies section-level editing | `[O/I]` | Open ranking editor without changing unrelated sections |

### 6.2 Control semantics

| Element | Generic role | Platform component | Web semantic role | Trigger | Result |
|---|---|---|---|---|---|
| `DAT-02` | selectable map annotation | `Annotation` / `MKAnnotationView` | button-like map feature | tap | select restaurant and reveal details |
| `ACT-01` | labeled action button | custom SwiftUI `Button` overlay | `button` | tap | open Grubbl AI |
| `ROW-01` | linked content item | `Button` or `NavigationLink` | link/article action | tap | open restaurant/ranking detail |
| `ACT-02` | icon button | SwiftUI `Button` | `button` | tap | edit the named ranking |
| `GRP-02` | ordered horizontal collection | horizontal `ScrollView` + `LazyHStack` | region/list | swipe, wheel, keys | reveal later ranked items |

### 6.3 Gesture and direct manipulation

- Observed gestures: none directly visible in still images.
- Inferred gestures: map pan, pinch zoom, annotation tap, vertical scroll, horizontal rail swipe.
- Proposed fallback controls: search/list alternative for map; explicit focusable cards; optional “See all” for each ranking; zoom controls where platform/context requires them.
- Drag alternatives: later cards must be reachable by single-pointer taps, keyboard focus, switch control, and screen-reader navigation; do not make reordering the only way to set rank.
- Keyboard behavior: arrow or tab focus should advance through card items and scroll the active card into view.
- Map behavior: selecting a marker must not cause an uncontrolled full reset of region or zoom.

### 6.4 Feedback

| Event | Visual feedback | Haptic/audio | Timing evidence | Proposed behavior |
|---|---|---|---|---|
| select annotation | selected outline/scale/z-order; open place card | light selection haptic | `[U/P]` | 150–220 ms visual transition |
| open AI | button pressed state then assistant transition | light impact optional | `[U/P]` | prevent double activation |
| save/love/avoid | icon/state change and confirmation | selection haptic | official feature, visual unknown | optimistic state with undo for destructive reversal |
| enter ranking card | card pressed state | optional | `[U/P]` | standard navigation transition |
| edit ranking | edit button pressed state | light haptic | `[U/P]` | preserve current rail scroll offset when returning |

---

## 7. Typography

### 7.1 Type system summary

| Role | Element IDs | Classification | Estimated preview size | Weight | Line height | Tracking | Alignment | Evidence |
|---|---|---|---:|---|---:|---:|---|---|
| map metric | `DAT-02` | sans / numeric | 13–15 px | semibold/bold | single line | compact | center | `[M/I]` |
| contextual action | `ACT-01` | sans | 14–16 px | semibold | single line | normal | center | `[M/I]` |
| section title | `TXT-01` | sans | 19–22 px | bold | 24–28 px | normal | leading | `[M/I]` |
| card title | `TXT-02` | sans | 15–18 px | semibold/bold | 19–22 px | normal | leading | `[M/I]` |
| rank badge | `DAT-04` | sans / numeric | 13–16 px | bold | single line | compact | center/leading | `[M/I]` |

### 7.2 Typography behavior

- Maximum text measure: section titles can occupy the header row minus the 44 pt edit target and 8–12 pt gap.
- Line-break character: normal word wrapping; no evidence of forced display breaks.
- Paragraph spacing: not relevant to the two references.
- Dynamic Type / text scaling: unknown; reconstruction must support it.
- Truncation rules: card titles should prefer two lines or move below the image at large sizes; section headings should not be silently truncated when editable.
- Numeric style: tabular figures are useful for map ratings and ordinal ranks, but the reference does not prove their use.
- Korean/English/Japanese considerations: Korean restaurant names can require greater line height and may lack word-space break opportunities; reserve two lines.
- Exact family certainty: unknown. A system or system-compatible sans is the safest reconstruction baseline.

### 7.3 Rebuild type tokens

| Token | Proposed value | Basis |
|---|---|---|
| `type.section.title` | iOS `headline` or 20 pt semibold/bold baseline | observed section hierarchy |
| `type.card.title` | iOS `subheadline`/16–17 pt semibold | image-overlay identity |
| `type.map.metric` | 14 pt semibold with tabular digits | compact annotation content |
| `type.control.label` | 15–16 pt semibold | labeled floating action |
| `type.rank.badge` | 14–15 pt bold with tabular digits | high-contrast ordinal label |

---

## 8. Color, material, border, and elevation

### 8.1 Palette samples

The values below are approximate reconstructions from compressed previews, not production color extractions.

| Token candidate | Sample location | Approximate value | Semantic role | Theme behavior | Evidence |
|---|---|---|---|---|---|
| `color.background.canvas` | Rankings root | `#FFFFFF` / near-white | content canvas | dark counterpart required | `[I]` |
| `color.map.base` | Explore root | low-saturation warm/cool grays | geographic substrate | use target map style | `[O]` |
| `color.text.primary` | section titles | near `#171717` | primary text | semantic inverse in dark | `[I]` |
| `color.accent.rank` | rank badge/edit | magenta near `#E83E8C` | ranking and editable accent | verify contrast in both themes | `[I]` |
| `color.accent.ai` | AI action | cyan near `#43BFE8` | assistant route | keep opaque | `[I]` |
| `color.marker.orange` | map annotation | orange near `#F4A72C` | unknown marker category/status | semantics must be defined before use | `[I/U]` |
| `color.marker.green` | map annotation | green near `#3E9B72` | unknown marker category/status | semantics must be defined before use | `[I/U]` |
| `color.marker.magenta` | map annotation | magenta family | unknown marker category/status | semantics must be defined before use | `[I/U]` |
| `color.scrim.media` | card bottom | black with vertical alpha gradient | text legibility | adapt to image luminance | `[O/P]` |
| `color.border.subtle` | cards/separators | dark neutral at low alpha | boundaries | maintain non-text contrast where interactive | `[O/P]` |

### 8.2 Surface hierarchy

| Layer | Element IDs | Fill/material | Border | Shadow/elevation | Blur | Rebuild rule |
|---|---|---|---|---|---|---|
| canvas | `SUR-01`, `SUR-02` | map or flat neutral | none | none | none | root content remains visually quiet |
| annotation | `DAT-02` | opaque high-chroma fill | dark/high-contrast outline | minimal | none | marker remains legible over map |
| media card | `ROW-01` | photograph | subtle boundary | none or low | none | do not make cards look detached from the rail |
| overlay action | `ACT-01` | opaque cyan | dark outline | low optional | none | no glass material |
| image scrim | `SUR-03` | transparent-to-dark gradient | none | none | none | use solely for text contrast |

### 8.3 Shape language

- Dominant geometry: circles for map/status/action icons; rounded rectangles for cards and labeled action.
- Corner-radius family: approximately 14–18 pt for cards; capsule for the AI action; circles for annotation and edit control.
- Capsule usage: reserved for the prominent labeled contextual action, not every text label.
- Stroke style: thin dark outline around some saturated controls and cards.
- Separator behavior: subtle horizontal structural rules between ranking sections.
- Optical corrections: center short decimal strings optically; align pencil glyph by visual mass; keep crown aligned to marker center.
- Shape inconsistency risk: using unrelated radius values on cards, badges, buttons, and sheets would turn the system into generic rounded UI; preserve a small semantic radius family.

---

## 9. Iconography, imagery, and illustration

### 9.1 Icon system

| Element | Source/family | Stroke/fill | Optical size | Container | Alignment | Confidence |
|---|---|---|---:|---|---|---:|
| AI leading icon | unknown/custom | compact dark glyph | approx. 14–18 px | cyan capsule | leading, centered vertically | 0.70 |
| edit pencil | system-like or custom | dark/contrasting glyph | approx. 14–18 px | magenta circle | optically centered | 0.90 |
| crown status | custom/simple symbol | filled/stroked crown | approx. 12–18 px | attached above marker | centered to annotation | 0.88 |

### 9.2 Image treatment

- Asset type: restaurant photography.
- Crop and aspect ratio: landscape media crop, approximately 4:3 or slightly wider.
- Mask: rounded rectangle.
- Color treatment: natural/high-saturation food photography; no global monochrome treatment visible.
- Blend: bottom text-legibility scrim.
- Content-aware focal point: food/restaurant subject should remain visible beneath overlays.
- Loading/failure treatment: not visible; reconstruction should reserve card geometry and use a neutral branded placeholder.
- Native text: rank and restaurant labels must remain native text, not baked into photos.

### 9.3 Art-direction grammar

| Property | Rule |
|---|---|
| Projection/camera | not applicable to photography; map remains standard north-up unless product requires rotation |
| Light direction | preserve source photography; do not add synthetic 3D lighting |
| Palette | neutral shell with high-chroma functional accents |
| Texture/grain | none as a UI-wide decorative effect |
| Edge treatment | crisp opaque shapes; rounded photo masks; minimal shadow |
| Repetition/variation | card anatomy stays fixed while photographs and text vary |
| Asset consistency gate | reject low-resolution crops, text-baked photos, inconsistent corner masks, and photographs where overlays obscure the food/venue focal point |

---

## 10. Data visualization or spatial encoding

### 10.1 Visual-variable mapping

| Visual variable | Encoded data | Scale | Zero / missing value | Legend | Risk |
|---|---|---|---|---|---|
| geographic position | restaurant location | map coordinates | omit or place at verified coordinate only | map provides context | inaccurate location |
| decimal text | likely restaurant rating or score | likely bounded numeric scale | use “No rating”/unlabeled state | no legend visible | metric ambiguity |
| marker fill color | unknown category, state, or score band | unknown | neutral marker proposed | no legend visible | color-only and undocumented meaning |
| crown symbol | likely Top 100 or ranked status | binary | no crown | no legend visible | interpretation not explicit |
| ordinal `#n` | item position in ranking | ordered integer | no item | self-explanatory when title context exists | stale rank after edits |
| card order | ranking order | ordinal position | empty state | section title provides context | horizontal items may be undiscovered |

### 10.2 Spatial rendering

- Projection: `[U]`; likely a conventional web/mobile map projection, but not inferable from the crop.
- Camera: 2D top-down map.
- Coordinate orientation: likely north-up; `[I]`.
- Geographic scope: Phoenix/Scottsdale local discovery.
- Level of detail: streets and place context remain visible under annotation field.
- Occlusion order: base map → ordinary markers → ranked/selected markers → floating contextual action → place card/sheet.
- Boundary treatment: no administrative boundary emphasis visible.
- Interaction: pan, zoom, select, recenter/search inferred.
- Performance constraint: annotation data must be viewport-filtered, batched, and updated without rebuilding all marker views on every camera tick.
- Density gate: use clustering, semantic zoom, or priority decluttering before labels become unreadable.
- Selection gate: selected restaurant remains visible above all ordinary annotations and outside the place-card occluded area.

### 10.3 Main visual defect visible in the reference

The Explore preview contains **annotation overplotting**: many same-sized labeled symbols overlap before the user can distinguish restaurants or reliably target one. This is not a stylistic detail to reproduce. The reconstruction should preserve the high-chroma point-symbol language while replacing the collision behavior with clustering, viewport filtering, rank/recency priority, or label suppression at low zoom.

---

## 11. Motion and temporal behavior

Static references cannot prove motion.

| Transition | Trigger | From → to | Property changes | Proposed duration | Easing | Evidence |
|---|---|---|---|---:|---|---|
| annotation selection | tap marker | default → selected | z-order, outline, scale, map offset | 160–220 ms | standard ease-out | `[P]` |
| place-card reveal | selected restaurant | map only → map + card | card translation/opacity; map framing | 220–320 ms | platform-standard | `[P]` |
| AI assistant reveal | tap CTA | map → assistant presentation | sheet/navigation transition | platform default | platform default | `[I/P]` |
| rail focus/scroll | swipe or focus | card n → card n+1 | horizontal content offset | direct manipulation | inertial/platform | `[I/P]` |
| ranking edit return | dismiss editor | editor → same section | preserve rail and vertical offsets | platform default | platform default | `[P]` |

- Continuous animation: none established.
- Loading motion: use restrained progress; avoid animated marker fields that compete with geographic scanning.
- Haptic: optional selection haptic for annotation and reactions.
- Reduce Motion alternative: replace scale/spring effects with opacity and instant z-order changes.
- State restoration: restore map region, selected place where valid, vertical rankings position, and each rail’s offset.

---

## 12. Responsive and adaptive behavior

### 12.1 Observed viewports

| Ref | Width class | Layout changes | Evidence |
|---|---|---|---|
| REF-01 | unknown compact mobile crop | none comparable | one preview only |
| REF-02 | unknown compact mobile crop | none comparable | one preview only |

### 12.2 Reconstruction behavior

| Range / platform class | Reflow | Reveal/hide | Presentation change | Max-width / pane rule |
|---|---|---|---|---|
| compact iPhone | full map; one-card-plus-peek rails | compact controls | place card as bottom sheet | card width 72–76% of content width |
| regular iPhone landscape | map stays full; rails may show two cards | retain labels | place card can widen | cap card width around 320–360 pt |
| iPad / expanded | optional map + persistent place-detail pane; ranking cards in larger rails | expose list/map toggle or sidebar if product requires | sheet may become inspector/pane | content max width 720–960 pt; do not stretch cards excessively |
| web mobile | same compact sequence | keyboard/focus support | semantic dialog/sheet | min 24×24 CSS px target, preferably 44×44 |
| web desktop | map/list split or centered rail page | hover supplement only, never required | side panel for place details | cap readable content width |

Proposed breakpoints are implementation decisions, not observations.

---

## 13. Accessibility and localization

### 13.1 Observed risks

| Area | Finding | Evidence | Severity for rebuild |
|---|---|---|---|
| target size | Visual map markers and edit circles appear smaller than a comfortable touch target | preview geometry | high |
| map density | Overlapping annotations can block selection and comprehension | observed | high |
| color-only meaning | Marker colors lack a visible legend or redundant encoding | observed/unknown semantics | high |
| text contrast | Restaurant names rely on photo scrim; contrast varies with image | observed | medium-high |
| hidden horizontal content | Rail continuation depends on partial-card cue and horizontal gesture | observed/inferred | medium |
| focus visibility | Not visible | unknown | high for web/keyboard reconstruction |
| text resize/reflow | Image-overlay titles may clip at large text sizes | inferred | medium-high |
| non-text labels | Crown and pencil require semantic names/context | observed | medium |
| map alternative | No list alternative visible in crop | unknown | high if map is the sole discovery path |

### 13.2 Required reconstruction behavior

- Semantic names, roles, values:
  - Map annotation: restaurant name, score/rating label, open status where relevant, ranked status.
  - Crown: include in the annotation’s combined accessibility value; do not expose it as a separate empty control.
  - Rank card: announce ranking title context, rank number, restaurant name, and relevant metadata.
  - Edit: “Edit [ranking name].”
- Reading and focus order:
  - Search/filter controls if present → map/list region → selected place details → contextual AI action.
  - Ranking section heading → edit action → ordered cards.
- Keyboard support:
  - All cards and actions reachable; active item scrolled into view.
  - Map-only gestures need search/list alternatives.
- Screen-reader grouping:
  - Treat each ranking rail as a named collection.
  - Combine photo, rank, and title into one card element.
- Text scaling:
  - At accessibility sizes, move card titles below photographs or increase card height.
  - Preserve 44 pt control regions.
- Reduced motion:
  - No spring dependence; honor platform setting.
- RTL:
  - Rank-badge placement and rail direction require deliberate semantic ordering; do not mirror ordinal meaning blindly.
- Long Korean strings:
  - Permit two-line section/card names; avoid fixed-height title overlays.
- Dynamic data extremes:
  - Handle unrated restaurants, multi-digit rank positions, long venue names, missing photos, and dense urban clusters.
- Web target size:
  - WCAG 2.2 AA requires at least 24×24 CSS px or qualifying spacing; 44×44 CSS px is the enhanced criterion. The iOS reconstruction should use a 44×44 pt interaction region even when the visible glyph is smaller.

Do not claim full accessibility conformance from image evidence alone.

---

## 14. Reference decomposition: Borrow / Exclude / Transform

### Borrow

- The concise **Love / Save / Avoid** reaction taxonomy: it converts vague sentiment into three actionable personal states.
- The restaurant ranking as a user-created, ordered artifact rather than an unstructured bookmark folder.
- The visible ordinal badge and one-card-plus-peek rail, which make sequence and continuation immediately legible.
- The combination of local map context, real photos, check-ins, and user reactions as evidence surrounding a restaurant.
- Story-sized share outputs and shareable rankings documented in the version history.
- A ranked-status badge on map annotations when the status has a published, stable meaning.
- The product’s local-market concentration: one city can generate denser, more relevant social proof than a thin global graph.

### Exclude

- Unclustered marker overlap.
- Undocumented color semantics.
- AI as the most visually dominant action when the product’s repeat loop is actually curation and local activity.
- Simultaneous expansion into map, feed, chat, leaderboard, points/gems, rankings, profiles, reviews, discussions, and AI unless each subsystem closes a measured loop.
- Reward points or leaderboards copied without a clear behavior they are meant to reinforce.
- Photo cards whose sole role is decoration rather than restaurant evidence or ordered curation.
- A horizontal rail with no “See all,” focus support, or alternative list when the collection is long.

### Transform for a food-photo-first product

- Change the primary object from **restaurant** to **meal/photo**. Restaurant identity becomes metadata rather than the entire card.
- Replace “discover nearby first” with “capture → receive a generated interpretation/card → optionally attach place → share/save.”
- Keep rankings as periodic recap artifacts—“이번 달 다시 먹고 싶은 5개”—rather than the main daily navigation.
- Convert Love / Save / Avoid into a photo-level or visit-level reaction only when each state changes future resurfacing or recommendations.
- Use the map as a secondary memory/index surface, not the required home screen.
- Turn check-in evidence into an automatically generated meal memory, while preserving user control over location and public sharing.
- Make share output the viral object: the app screen is an editor/source; the exported card is the social artifact.

### This / Not this

| This | Not this |
|---|---|
| Custom coordinate-anchored map annotation | Generic decorative bubble floating over a map |
| Point-symbol map with explicit legend/semantics | Heatmap or choropleth mislabeled as “pins” |
| Ordered horizontal content rail | Unordered two-column photo grid |
| Ordinal rank badge | Filter chip or selectable pill |
| Text-legibility scrim | Heavy decorative gradient covering most of the photo |
| Contextual AI entry | AI dashboard that displaces discovery |
| Cluster/declutter by zoom | Reproduce every overlapping marker |
| Restaurant-first social evidence | Photo-only feed with no object or decision context |

---

## 15. Reconstruction specification

### 15.1 Design thesis

```text
Reconstruct Grubbl as a high-chroma local discovery utility, not as a generic social feed.
The Explore surface is a geographic decision tool: a restrained map carries saturated,
constant-size restaurant annotations, while selection and density are managed through
clustering, priority, and a subordinate place card. The Rankings surface is an ordered
curation browser: a vertical sequence of named collections contains wide photo cards in
horizontal rails, with explicit ordinal badges and compact section-level editing. Color
is energetic but semantic; rounded geometry is limited to markers, media cards, and one
contextual labeled action. AI remains reachable from the map without obscuring the core
restaurant-selection task.
```

### 15.2 Layout rules

```text
EXPLORE ROOT:
- Map fills all available content bounds.
- No outer card or inset around the map.
- Respect safe areas for overlaid controls.
- Keep selected annotation visible when a place card appears.

ANNOTATION FIELD:
- Visual marker diameter: 32–36 pt.
- Interactive region: minimum 44×44 pt.
- Numeric label: one line, tabular figures preferred.
- Selected marker wins z-order.
- Cluster, filter, or suppress labels before overplotting.
- Never use area/size as a metric without defining the scale.

CONTEXTUAL AI ACTION:
- Bottom-trailing overlay, 16 pt safe-area inset.
- Height: 46–50 pt.
- Opaque cyan fill, compact leading icon, one text label.
- Reposition/collapse when another overlay occupies the same region.

PLACE DETAILS:
- Present as a bottom place card/sheet or regular-width inspector.
- Preserve map position and selected annotation.
- Support detents only when each detent exposes a meaningful content state.

RANKINGS ROOT:
- Vertical scroll with 16–20 pt inline page inset.
- Each section: heading row, 12 pt gap, horizontal rail, 28–36 pt section gap/separator.
- Heading row reserves a 44×44 pt edit target.

RANKING RAIL:
- Card width: 72–76% of compact content width.
- Gap: 12 pt.
- Show 12–20% of next card as a continuation cue.
- Provide See All or equivalent when lists become long.

RANKED MEDIA CARD:
- Landscape photo, approximately 4:3.
- Radius: 14–16 pt.
- Rank badge: top-leading, 10–12 pt inset.
- Name: bottom-leading, at most two lines.
- Adaptive scrim behind text only.
- Whole card is one action.
```

### 15.3 Component mapping

| Reference element | Target component | Native/custom | Required customization | State owner |
|---|---|---|---|---|
| `SUR-01` map | SwiftUI `Map` | native | map style, camera, selection | Explore feature model |
| `DAT-02` annotation | SwiftUI `Annotation`; `MKAnnotationView` bridge when clustering is needed | hybrid | visual marker, hit region, collision/clustering, accessibility | map annotation model |
| `DAT-03` status badge | child of annotation view | custom | combined semantic label | restaurant/ranking status |
| `ACT-01` AI action | SwiftUI `Button` overlay | custom styling | safe-area anchoring, loading/unavailable states | assistant route model |
| place card | `.sheet(item:)` or safe-area inset card | native/hybrid | detents and map framing | selected restaurant |
| `GRP-01` ranking section | `LazyVStack` section | custom composition | heading/edit/rail relationship | ranking collection |
| `ACT-02` edit | SwiftUI `Button` | native semantics/custom appearance | 44 pt hit target and contextual label | ranking editor |
| `GRP-02` rail | horizontal `ScrollView` + `LazyHStack` | native | peek geometry, focus scrolling | rail state |
| `ROW-01` card | `NavigationLink`/`Button` | hybrid | media crop, scrim, rank overlay | ranking item |
| `DAT-04` rank | `Text` overlay | native text | tabular digits, high contrast | ranking position |

### 15.4 Proposed semantic tokens

| Token | Type | Light value | Dark value | Description |
|---|---|---|---|---|
| `color.background.canvas` | color | `#FFFFFF` | semantic near-black | Ranking canvas |
| `color.text.primary` | color | semantic near-black | semantic near-white | Primary labels |
| `color.accent.rank` | color | calibrated magenta | contrast-adjusted magenta | Rank and ranking-edit accent |
| `color.accent.assistant` | color | calibrated cyan | contrast-adjusted cyan | Contextual AI route |
| `color.map.annotation.default` | color | semantic category color | theme-calibrated | Map annotation fill |
| `color.media.scrim.end` | color | black at adaptive alpha | black at adaptive alpha | Photo-title contrast |
| `space.inline.page` | dimension | 20 pt | 20 pt | Compact ranking inset |
| `space.inline.cardGap` | dimension | 12 pt | 12 pt | Rail spacing |
| `space.stack.section` | dimension | 32 pt | 32 pt | Ranking sections |
| `radius.card.media` | dimension | 16 pt | 16 pt | Ranked media cards |
| `size.annotation.visual` | dimension | 34 pt | 34 pt | Marker visual diameter |
| `size.control.hitMinimum` | dimension | 44 pt | 44 pt | iOS interaction region |
| `size.card.compactWidthRatio` | number | `0.74` | `0.74` | Compact rail card width |
| `type.map.metric` | typography | 14 pt semibold tabular | same semantic role | Annotation value |
| `type.section.title` | typography | 20 pt bold/semibold | same semantic role | Ranking heading |

### 15.5 State matrix

| Surface/component | Default | Selected | Disabled | Loading | Empty | Error | Large text | Dark |
|---|---|---|---|---|---|---|---|---|
| Map | annotations + base | selected marker + place card | map remains navigable where possible | stable base, incremental markers | explain no nearby results + change filters | retry/list fallback | controls grow, map remains full | semantic map style |
| Annotation | colored metric | outline/scale/z-order | muted with reason | placeholder/withheld | unrated variant | unavailable marker omitted or explained | value unchanged; larger semantic target | contrast-calibrated |
| AI action | icon + label | pressed | disabled with reason | progress, no double tap | not applicable | retry | label may wrap only if needed | opaque accessible cyan |
| Ranking section | title + rail | not applicable | edit may disable | skeleton preserving geometry | empty explanation + add | section retry | heading wraps | semantic canvas |
| Media card | photo + rank + name | pressed/focused | muted only when unavailable | image placeholder | missing-photo placeholder | retry image or metadata | title moves/reflows | scrim recalibrated |
| Edit button | pencil | pressed/focused | muted + semantic disabled | progress if save in place | still available to add | error surfaced in editor | 44 pt region preserved | contrast-calibrated |

### 15.6 Asset production requirements

- Required assets: restaurant photos; AI icon; edit symbol; crown/ranked-status symbol; map annotation background shapes.
- Native text vs baked text: all names, scores, ranks, and labels remain native.
- Vector/raster: icons and annotation shapes vector; photography raster.
- Resolution and scale: photos must cover card crop at 3× target scale without visible upscaling.
- Cropping: content-aware 4:3 crop with focal subject preserved under badge/scrim.
- 9-slice/tile/contain: not required for core references.
- Color space: sRGB or Display P3 with tested fallback.
- Compression: avoid visible banding in scrims and blocking around food detail.
- Deterministic variation: none required.
- Asset QA: no text-baked screenshots, inconsistent radii, mismatched icon weights, or low-resolution restaurant photos.

### 15.7 Platform implementation language

#### iOS / SwiftUI

```text
Use NavigationStack for subordinate full-detail routes, but do not infer the product's
top-level tab labels from these references.

Build Explore with Map and a camera-position model. Use Annotation for ordinary custom
annotations. When production requirements include true clustering, collision priority,
or thousands of visible points, bridge to MKMapView/MKAnnotationView and assign stable
annotation identifiers and clustering identifiers rather than forcing all behavior through
a purely declarative marker layer.

Keep restaurant data and annotation presentation separate. Query/filter by the visible
map region with debounce and cancellation. Diff annotations by stable restaurant ID.
Do not rebuild the entire map tree for every camera tick.

Place the AI action in overlay(alignment: .bottomTrailing) or safeAreaInset as appropriate.
Expose at least a 44×44 pt hit region. Use a semantic Button and accessibilityLabel.

Store selectedRestaurant separately from camera state. Present a place card with
.sheet(item:) and appropriate detents, or a custom safe-area card when the map must remain
directly manipulable. Adjust camera padding rather than hiding the selected annotation
behind the sheet.

Build Rankings with a vertical ScrollView and LazyVStack. Each ranking section contains
a heading HStack and a horizontal ScrollView with LazyHStack. Compute compact card width
from the container, approximately 0.74× available width, capped on regular-width devices.
Use NavigationLink or Button for the entire card. Overlay native Text for rank and name;
apply a bottom gradient scrim. Preserve vertical and horizontal scroll positions across
editing where feasible.

Group card accessibility into one element containing rank, restaurant name, and optional
metadata. Give each edit button the ranking title in its accessibility label. Provide an
alternative list/search path for users who cannot efficiently operate the map.
```

#### Web

```text
Use a semantic main region with a named map region and a list/search alternative. Render
map points as keyboard-focusable features or synchronize them with an accessible result
list. Use button semantics for the AI and edit actions. Build ranking rails as named
sections containing ordered lists; allow keyboard focus to scroll cards into view.

Meet WCAG 2.2 target-size requirements: at least 24×24 CSS px or qualifying spacing at
Level AA, with 44×44 CSS px as the preferred enhanced target. Do not require drag alone
to reach or reorder items. Preserve visible focus and provide a non-color label for all
marker categories.
```

---

## 16. Explicit prohibitions and non-goals

- Do not reproduce annotation overplotting.
- Do not call the map a heatmap, dot-density map, choropleth, or proportional-symbol map.
- Do not map marker color to a meaning that the product has not defined and documented.
- Do not use marker size to imply rating/popularity unless a scale and legend exist.
- Do not expose the crown as an unlabeled decorative accessibility element.
- Do not place an AI card or chatbot prompt over the center of the discovery map.
- Do not use glass blur, translucent floating panels, or ornamental gradients.
- Do not convert ranked rails into an unordered photo grid.
- Do not make the edit pencil’s visible 28–32 pt circle its entire touch target.
- Do not bake rank/name text into restaurant imagery.
- Do not rely on horizontal dragging as the only way to access later cards.
- Do not invent the app’s tab names, dark theme, animation timings, or exact font family from cropped still images.
- Preserve: restaurant-first object model, ordered rankings, local map context, saturated semantic accents, and one-card-plus-peek continuation cue.
- Out of scope: product-wide information architecture and the backend ranking/scoring formula.
- Acceptable deviation: recalibrating color and size for contrast, target platform, and native screenshot dimensions.
- Unacceptable substitution: generic map pins, generic bento cards, or a full-screen AI chat replacing the Explore decision surface.

---

## 17. Visual QA and acceptance criteria

### 17.1 Reference-match checkpoints

| Check | Target | Tolerance | Verification method |
|---|---|---|---|
| Explore focal order | annotation field first, AI action second, map third | same squint-test order | grayscale + 25% paired thumbnails |
| annotation density | no unreadable decimal overlap at supported zoom | zero overlapping text labels; limited symbol overlap only by explicit priority | automated collision snapshots at density fixtures |
| annotation hit target | 44×44 pt interaction region | no smaller target | accessibility inspector and hit-test overlay |
| selected marker | remains visible above ordinary markers and place card | no occlusion | capture each sheet detent |
| AI action placement | bottom-trailing, map remains visible | ±4 pt after safe-area calibration | screenshot overlay |
| Ranking page inset | shared title/card alignment | ±2 pt | layout measurement |
| rail continuation | one full card plus partial next card | next-card reveal 12–20% | compact-device screenshot |
| card order | ordinal badge matches data order | exact | UI test with known fixture |
| card title contrast | readable across light/dark photos | WCAG contrast test where applicable | automated image fixtures + manual review |
| edit target | visible compact circle inside 44 pt hit area | exact minimum | hit-test overlay |
| large text | no clipped section/card names | no loss of information | accessibility text-size matrix |
| color semantics | every color category has redundant label/icon/legend | no color-only state | grayscale and screen-reader review |

### 17.2 Required capture matrix

| Platform/device | Viewport | Theme | Text size | State |
|---|---|---|---|---|
| iPhone compact | 393×852 pt | light | default | dense map, no selection |
| iPhone compact | 393×852 pt | light | default | selected marker + medium place card |
| iPhone compact | 393×852 pt | light | accessibility XL | Rankings |
| iPhone compact | 393×852 pt | dark | default | Explore and Rankings |
| iPhone landscape | representative | light | default | map + overlay collision |
| iPad regular | representative | light/dark | default | map/detail adaptation and rankings |
| web compact, if implemented | 390 CSS px | light | 200% zoom | map/list and rankings |
| web desktop, if implemented | 1440 CSS px | light/dark | default | keyboard focus and side detail |

### 17.3 Acceptance statement

```text
PASS when:
- The map remains the primary discovery surface.
- Every visible restaurant value is legible or intentionally clustered/decluttered.
- Selection preserves geographic context.
- Rankings read as ordered horizontal collections with explicit continuation.
- All essential controls have semantic labels and adequate hit regions.
- Color is redundant with text, symbol, or accessible metadata.
- No invented style or interaction is presented as observed fact.

HOLD when:
- The meaning of marker colors, decimal metric, or crown status has not been confirmed
  and implementation depends on that meaning.
- Native uncropped references reveal materially different geometry or navigation.

FAIL when:
- Marker text overlaps materially.
- AI obscures restaurant selection.
- Ranked cards become an unordered grid.
- Text is baked into photos.
- The pencil glyph or map symbols are the only small precision targets.
- A heatmap, glass UI, or generic AI dashboard replaces the observed product grammar.
```

---

## 18. Uncertainty and decision register

| ID | Question | Current status | Alternatives | Evidence needed | Blocks rebuild |
|---|---|---|---|---|---|
| `U-01` | Is the decimal inside each marker an average rating, Grubbl score, or another metric? | inferred | review average / composite score / activity score | production legend or app inspection | yes for semantic labeling |
| `U-02` | What do orange, green, and magenta marker fills mean? | unknown | sentiment / category / status / ranking tier | in-app legend or source code | yes for color semantics |
| `U-03` | Does the crown mean Top 100? | inferred | Top 100 / promoted status / user favorite | selected-place detail or official explanation | yes for status label |
| `U-04` | What are the actual top-level destinations? | unknown | Explore / Feed / Rankings / Profile / other | uncropped navigation screenshot or app inspection | no for surface reconstruction |
| `U-05` | Does selecting a marker open a bottom sheet, card, or full route? | unknown | place card / sheet / navigation detail | interaction capture | no; proposed pattern available |
| `U-06` | Does the map currently cluster annotations? | unknown | clustering / priority filtering / no clustering | zoom-sequence capture | yes for faithful behavior |
| `U-07` | Exact production font and icon family | unknown | system / custom | design assets or source inspection | no |
| `U-08` | Original screenshot dimensions and crop | unknown | iPhone compact variants | original image metadata | yes for pixel-faithful geometry |
| `U-09` | Dark-mode design | unknown | semantic adaptation | dark captures | no for light reconstruction |
| `U-10` | Card rail snapping and paging behavior | unknown | free scroll / view-aligned snapping | interaction capture | no |

---

## 19. Source register

| Source ID | Term or claim supported | Authority | URL / document | Section | Verified |
|---|---|---|---|---|---:|
| `SRC-01` | Product positioning, Explore, Curate, AI, Rankings, Phoenix scope | official product | `https://grubbl.app/` | What You Can Do with Grubbl | 2026-08-08 |
| `SRC-02` | App title, platform, description, ratings, version history, features | official store listing | `https://apps.apple.com/us/app/grubbl-restaurant-discovery/id6747157430` | App description / Version History | 2026-08-08 |
| `SRC-03` | Explore reference image | official product asset | `https://grubbl.app/images/mocks/explore.png` | marketing mock | 2026-08-08 |
| `SRC-04` | Rankings reference image | official product asset | `https://grubbl.app/images/mocks/rankings.png` | marketing mock | 2026-08-08 |
| `SRC-05` | Map and annotation platform vocabulary | `PLATFORM_OFFICIAL` | `https://developer.apple.com/design/human-interface-guidelines/maps` | Maps | 2026-08-08 |
| `SRC-06` | Floating / extended FAB analogue | `PLATFORM_OFFICIAL` within Material | `https://m3.material.io/components/floating-action-button/overview` | FAB | 2026-08-08 |
| `SRC-07` | Web target sizes and drag alternative | `STANDARD_NORMATIVE` | `https://www.w3.org/TR/WCAG22/` | 2.5.5, 2.5.7, 2.5.8 | 2026-08-08 |
| `SRC-08` | Early-stage status and >5,000 Phoenix restaurant dataset claim | developer statement | Dallas McLaughlin LinkedIn post | June/July 2026 post | 2026-08-08 |
| `SRC-09` | Local launch coverage | press | Phoenix Business Journal, 2026-06-11 | launch article | 2026-08-08 |
| `SRC-10` | Prior Android download snapshot, not current authoritative traction | third-party tracker | `https://chrome-stats.com/d/com.bossdjay.grubblbarebones` | 470 downloads at v1.9.3 ingestion | 2026-08-08 |

---

## 20. Final build brief

```text
SURFACE:
Explore map + Rankings browser.

TARGET:
iOS / SwiftUI + MapKit; compact iPhone first, adaptive iPad behavior.

ARCHETYPE:
Map-first local discovery interface plus vertically stacked ordered content rails.

NAVIGATION:
Exact top-level structure remains unknown. Marker selection reveals subordinate place
details while preserving map context. Cards navigate to restaurant/ranking detail.
Section pencil edits the named ranking.

LAYOUT:
Explore is full-bleed map with bottom-trailing labeled contextual action. Rankings is a
vertical stack of title rows and horizontal rails. Compact cards occupy approximately
74% of content width with a visible next-card peek.

TYPOGRAPHY:
System-compatible sans. 20 pt section title, 16–17 pt card title, 14 pt map metric,
15–16 pt contextual action. Native text only; two-line Korean support.

COLOR/MATERIAL:
Neutral canvas/map; calibrated magenta ranking accent and cyan assistant accent; other
marker colors require confirmed semantics. Opaque flat surfaces, minimal elevation,
no glass.

COMPONENTS:
Map, custom annotations, optional MKAnnotationView clustering bridge, place card/sheet,
labeled overlay Button, ranking section, horizontal LazyHStack rail, ranked media card,
ordinal badge, icon edit button, text-legibility scrim.

INTERACTION:
Pan/zoom/select map, reveal place details, enter AI, vertically browse rankings,
horizontally browse ordered cards, edit a ranking. Provide non-drag alternatives.

ADAPTATION:
Cluster/declutter by zoom and density. Use a map/detail pane on expanded widths where
appropriate. Cap card widths instead of stretching.

ACCESSIBILITY:
44×44 pt iOS targets; semantic restaurant/rank labels; non-color redundancy; map list
alternative; named ordered rails; large-text reflow; reduced-motion transitions.

ASSETS:
High-resolution restaurant photos; vector icons/marker shapes; native text; consistent
4:3 crop and 14–16 pt media radius.

EXCLUSIONS:
Marker overplotting, undocumented color meaning, heatmap substitution, proportional
marker sizing without a scale, generic AI dashboard, glass panels, unordered card grid,
baked-in text, and invented tab structure.

QA GATE:
No overlapping numeric labels; selected marker remains visible with the place card;
one-card-plus-peek composition survives at 393 pt; rank order and labels match fixture
data; all essential controls meet interaction and semantic requirements.
```

---

## Product and traction note

As of 2026-08-08, Grubbl is an actively updated, Phoenix-focused product rather than a
demonstrated mass-market hit. The US App Store lists 4.4/5 from 7 ratings and recent
versions through 1.9.10. The developer describes the product as still in “very early
stages” and says it stores data on more than 5,000 Phoenix-area restaurants. A third-party
Android tracker recorded roughly 470 downloads at version 1.9.3; that number is dated,
platform-specific, and not an authoritative total. The strongest evidence is therefore
not scale but a narrow local-market strategy, rapid feature iteration, and a broad
restaurant-centric loop spanning discovery, reactions, check-ins, rankings, feed activity,
sharing, and AI.

## Core-loop interpretation

```text
Discover nearby restaurant
→ inspect community evidence
→ Love / Save / Avoid, check in, review, or rank
→ activity changes personal lists and community surfaces
→ rankings/share cards create outward distribution
→ later restaurant decisions return the user to the map and curated lists
```

The photo is supporting evidence in this loop. The restaurant is the durable primary
object. This distinction is central when borrowing Grubbl for a food-photo-sharing product.

---

## Revision history

| Revision | Date | Change |
|---|---:|---|
| 1 | 2026-08-08 | Initial analysis from official site, App Store listing, and official Explore/Rankings marketing references |
