---
schema_version: "1.0.0"
analysis_id: "UIR-20260808-000"
status: "complete"
created_at: "2026-08-08"
updated_at: "2026-08-08"
title: "Synthetic Notes — Today screen UI reference reconstruction"
subject:
  product_name: "Synthetic Notes"
  product_type: "app"
  surface_name: "Today screen"
  platform: "iOS"
  locale: "en"
  theme: "light"
target:
  platform: "iOS"
  framework: "SwiftUI"
reference_storage: "generated"
template_version: "1.0.0"
---

# Synthetic Notes — Today Screen UI Reference Reconstruction

This is a deliberately compact worked example. It demonstrates the evidence chain; it is not a full production audit.

## 0. Reconstruction directive

> **Pattern:** single-object reading view  
> **Primary style:** editorial UI (`INDUSTRY_CONVENTIONAL`) with a project-defined low-chrome treatment  
> **Platform shell:** persistent iOS-style tab navigation  
> **Core composition:** one left-aligned text column, large serif focal text, restrained sans-serif metadata, one decorative raster-like mark  
> **Rebuild rule:** preserve the 24-unit page inset, 31-unit display size, low-contrast metadata, and bottom navigation separation  
> **Do not introduce:** floating cards, gradients, glass panels, multiple accent colors, or additional hero imagery

## 1. Scope and evidence

| Field | Value |
|---|---|
| Product | Synthetic Notes |
| Surface | Today |
| Reference | `reference.svg` |
| Viewport | 393×852 source pixels |
| Purpose | Demonstrate the eiraUI template |
| Storage | generated |

The SVG source establishes exact geometry and colors. It does not establish real interaction, accessibility behavior, or device-point conversion.

## 2. Literal description

`[O]` A warm off-white canvas fills the viewport. A small uppercase date sits at the top-left. An irregular dark mark occupies the upper-right. A three-line serif sentence is the dominant element. Author and collection metadata follow beneath it. A thin divider separates a two-line annotation. A bottom region contains three text destinations; the first has a short underline.

## 3. Classification

| Field | Classification | Authority | Evidence |
|---|---|---|---|
| Archetype | single-object reading view | `INDUSTRY_CONVENTIONAL` | one primary content object |
| Navigation | tab bar-like primary navigation | `PLATFORM_OFFICIAL` mapping | persistent bottom destinations |
| Style | editorial UI | `INDUSTRY_CONVENTIONAL` | typography-led hierarchy, negative space, restrained chrome |
| Project label | Productive Editorial Minimal | `PROJECT_DEFINED` | editorial hierarchy plus visible utility navigation |

## 4. Reading order

1. `TXT-02` main sentence — size and isolated position.
2. `DEC-01` ink-like mark — dark contrast, smaller area.
3. `TXT-03` author metadata — proximity to the main sentence.
4. `NAV-01` bottom navigation — separated by a full-width divider.

## 5. Geometry

| Region | Source bbox | Role |
|---|---|---|
| `SUR-01` | `0,0,393,852` | canvas |
| `GRP-01` | `24,53,345,445` | reading column |
| `NAV-01` | `0,776,393,76` | persistent primary navigation |

`[M]` The reading column begins 24 source pixels from the left, approximately 61 normalized units.  
`[M]` The bottom navigation occupies 8.9% of viewport height.

## 6. Element inventory

| ID | Literal observation | Canonical term | Authority | Evidence | Rebuild directive |
|---|---|---|---|---|---|
| `TXT-01` | small uppercase date | metadata label | `INDUSTRY_CONVENTIONAL` | `[O]` | 13-unit sans, uppercase, muted foreground |
| `DEC-01` | irregular dark shape with a light internal break | decorative ink-wash mark | `PROJECT_DEFINED` | `[O]` | raster or vector mask with asymmetry; no interaction |
| `TXT-02` | large three-line serif sentence | display text / hero text | `INDUSTRY_CONVENTIONAL` | `[O/M]` | 31-unit serif, 42-unit baseline step, left aligned |
| `TXT-03` | author name | secondary metadata | `INDUSTRY_CONVENTIONAL` | `[O]` | 14-unit sans, stronger than tertiary metadata |
| `TXT-04` | collection line | tertiary metadata | `INDUSTRY_CONVENTIONAL` | `[O]` | 12-unit sans, lower contrast |
| `TXT-05` | two-line note | supporting body text | `INDUSTRY_CONVENTIONAL` | `[O]` | 15-unit sans, two lines, not a second hero |
| `NAV-01` | three persistent destinations | tab bar mapping | `PLATFORM_OFFICIAL` | `[O/I]` | map to native tab navigation; labels remain visible |
| `NAV-02` | short underline below TODAY | selected indicator | `INDUSTRY_CONVENTIONAL` | `[O]` | 2-unit rule; only one selected destination |

## 7. Typography

| Role | Classification | Size | Color |
|---|---|---:|---|
| display | serif | 31 | `#20201D` |
| secondary metadata | sans-serif | 14 | `#54534E` |
| tertiary metadata | sans-serif | 12 | `#8A877E` |
| body | sans-serif | 15 | `#363531` |
| navigation | sans-serif uppercase | 12 | selected/secondary |

`[U]` The SVG uses generic font families and does not prescribe a production font.

## 8. Palette

| Token | Value | Role |
|---|---|---|
| `color.background.canvas` | `#F5F2EA` | paper-like canvas |
| `color.text.primary` | `#20201D` | main text |
| `color.text.secondary` | `#54534E` | author |
| `color.text.tertiary` | `#8A877E` | collection |
| `color.border.subtle` | `#D8D3C8` | dividers |
| `color.decoration.ink` | `#1C2630` at 88% | decorative mark |

## 9. Borrow / Exclude / Transform

### Borrow

- typography-led focal hierarchy;
- stable left alignment;
- large inactive space;
- one irregular brand mark.

### Exclude

- generic font files from the SVG;
- text-only navigation if platform convention or accessibility requires icons;
- fixed pixel sizes outside the demonstration viewport.

### Transform

- map the bottom region to a native tab container;
- map pixel measurements to target points after confirming the design frame;
- add Dynamic Type behavior without allowing metadata to overtake the display text.

## 10. Final build brief

```text
SURFACE: Today reading view
TARGET: iOS SwiftUI
ARCHETYPE: single-object reading view
NAVIGATION: persistent three-destination tab navigation
LAYOUT: 24-point-equivalent leading/trailing inset; one column; bottom navigation outside scroll content
TYPOGRAPHY: serif display + sans UI metadata; four semantic roles
COLOR/MATERIAL: warm paper canvas, near-black text, one blue-black decorative mark
COMPONENTS: date metadata, display sentence, source metadata, supporting note, tab navigation
INTERACTION: native navigation behavior; decorative mark is noninteractive
ADAPTATION: preserve readable measure and left alignment; derive actual point sizes from target frame
ACCESSIBILITY: semantic text styles, visible labels, Dynamic Type, sufficient contrast
EXCLUSIONS: cards, glass, gradients, additional hero imagery
QA GATE: same focal order and line wrapping at 393-point target width
```
