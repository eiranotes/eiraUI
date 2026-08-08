---
schema_version: "1.0.0"
analysis_id: "UIR-YYYYMMDD-NNN"
status: "draft"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
title: "[Product] — [Surface] UI reference reconstruction"
subject:
  product_name: ""
  product_type: "app | website | web-app | design-system | other"
  surface_name: ""
  platform: "iOS | iPadOS | Android | web-mobile | web-desktop | macOS | Windows | cross-platform | unknown"
  locale: ""
  theme: "light | dark | mixed | unknown"
target:
  platform: ""
  framework: ""
reference_storage: "link_only | local_public | local_authorized | generated | private_uncommitted"
template_version: "1.1.0"
---

# [Product] — [Surface] UI Reference Reconstruction

## 0. Reconstruction directive

Write a compact build directive that can stand alone.

> **Pattern:** `[interface archetype]`  
> **Primary style:** `[style label + authority class]`  
> **Platform shell:** `[official platform components or generic shell]`  
> **Core composition:** `[layout, hierarchy, focal element]`  
> **Rebuild rule:** `[measurable summary]`  
> **Do not introduce:** `[explicit exclusions]`

### One-paragraph reconstruction language

```text
[Convert the reference into exact structural and visual language.
Do not use unsupported adjectives such as clean, premium, modern, soft, or app-like
without listing the observable properties that produce them.]
```

---

## 1. Scope and evidence

### 1.1 Subject

| Field | Value |
|---|---|
| Product | |
| Surface / route / state | |
| Product type | |
| Source platform | |
| Target platform | |
| Locale | |
| Theme | |
| Analysis purpose | faithful reconstruction / selective borrowing / redesign baseline |
| Out of scope | |

### 1.2 Reference inventory

| Ref ID | Source type | Locator or repository path | Capture date | Viewport | Device/browser | Transformation | Storage policy |
|---|---|---|---:|---|---|---|---|
| `REF-01` | upload / screenshot / URL / video frame / design file | | | `W×H px` | | original / crop / resized | |

### 1.2a Public app-listing completeness

Complete this table whenever the subject has a public App Store, Google Play, or equivalent listing.

| Storefront | Platform / device family | Locale | Published assets | Analyzed assets | Missing / inaccessible | Verified |
|---|---|---|---:|---:|---|---:|
| | | | | | | |

**Identity check:** `[store URL or ID]` → `[displayed app name]` → `[developer]`  
**Coverage result:** `complete / incomplete / accepted limitation`  

A store-listing analysis is not complete when the published and analyzed counts differ without an explicit accepted limitation. Keep every asset in published order even when screens are visually similar.

### 1.3 Evidence limitations

- `[U]` Hidden states not visible:
- `[U]` Exact font files or variable axes:
- `[U]` Motion or transition timing:
- `[U]` Responsive behavior outside supplied viewports:
- `[U]` Accessibility semantics not inspectable from pixels:
- Other:

### 1.4 Evidence labels used

`[O] OBSERVED` · `[M] MEASURED` · `[S] SAMPLED` · `[I] INFERRED` · `[P] PROPOSED` · `[U] UNKNOWN`

---

## 2. Reference overview

### 2.1 Literal description

Describe only what is visibly present, from the outer frame inward. Avoid style labels in this subsection.

```text
[Example structure:
The viewport contains a top system region, a single content column, a large text block
occupying the upper-middle area, two metadata lines below it, and a persistent bottom
control region. The background is visually uniform except for one irregular raster mark.]
```

### 2.2 Interface archetype

| Field | Classification | Authority | Evidence | Confidence |
|---|---|---|---|---:|
| Primary archetype | detail view / feed / editor / dashboard / timeline / canvas / map / form | industry/generic | | |
| Secondary archetype | | | | |
| Navigation model | hierarchy / tabs / hub-and-spoke / master-detail / unknown | | | |
| Content model | single object / collection / mixed | | | |

### 2.3 Reading order and focal hierarchy

| Order | Element ID | What attracts attention | Mechanism |
|---:|---|---|---|
| 1 | | size / contrast / position / isolation / motion | |
| 2 | | | |
| 3 | | | |

**Squint-test result:**  
**25%-thumbnail result:**  
**Competing focal points:**  

---

## 3. Terminology normalization summary

Use the most specific supported term. Record aliases rather than treating one platform name as universal.

| Raw description | Canonical term | Authority class | Source | Platform scope | Alias / nearby term | Why this term fits |
|---|---|---|---|---|---|---|
| “bottom icon menu” | tab bar / navigation bar / bottom navigation | `PLATFORM_OFFICIAL` or `INDUSTRY_CONVENTIONAL` | | | | |

### 3.1 Primary style classification

| Field | Value |
|---|---|
| Primary style label | |
| Authority | `INDUSTRY_CONVENTIONAL` / `PROJECT_DEFINED` |
| Observable defining traits | |
| Secondary influences | |
| Labels rejected | |
| Reason rejected | |

A style label is invalid unless the defining traits are listed.

---

## 4. Frame, geometry, and layout system

### 4.1 Coordinate system

| Field | Value |
|---|---|
| Source viewport | `W×H px` |
| Origin | top-left |
| Normalized space | `1000×1000` |
| Platform point/CSS conversion known | yes / no |
| Scale caveat | |

### 4.2 Root shell

| Property | Observation | Measurement | Evidence | Rebuild directive |
|---|---|---|---|---|
| Safe area / browser chrome | | | `[O/M/U]` | |
| Root background | | | | |
| Scroll axis | | | | |
| Fixed or sticky regions | | | | |
| Content maximum width | | | | |
| Outer insets | | | | |

### 4.3 Layout model

| Property | Value |
|---|---|
| Primary layout | stack / grid / pane / overlay / custom |
| Columns or panes | |
| Alignment anchors | |
| Baseline relationships | |
| Section rhythm | |
| Density | compact / regular / spacious + evidence |
| Overflow behavior | |
| Layering / z-order | |

### 4.4 Major region map

| Region ID | Ref ID | Source bbox `x,y,w,h` | Normalized bbox | Role | Layout relationship |
|---|---|---|---|---|---|
| `SUR-01` | `REF-01` | | | root surface | |
| `GRP-01` | | | | | |

### 4.5 Spacing reconstruction

| Token candidate | Sampled/measured values | Proposed semantic value | Usage |
|---|---|---|---|
| `space.inline.page` | | | |
| `space.stack.section` | | | |
| `space.stack.item` | | | |
| `space.control.content` | | | |

---

## 5. Element inventory

Assign stable IDs. Add one row per visible or structurally important element.

| ID | Ref | Bbox | Literal observation | Canonical term | Authority | Hierarchy role | Interaction/state | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---:|
| `NAV-01` | `REF-01` | | | | | | | `[O]` | |
| `TXT-01` | | | | | | | | | |
| `ACT-01` | | | | | | | | | |

### 5.1 Detailed element specification

Repeat this block for each important element.

#### `[ELEMENT-ID] — [Canonical name]`

**Traceability**

| Field | Value |
|---|---|
| Reference | |
| Bounding box | source px / normalized |
| Evidence status | `[O/M/S/I/P/U]` |
| Confidence | `0.00–1.00` |
| Canonical term | |
| Authority class | |
| Source and section | |
| Generic alias | |
| Platform-specific mapping | |

**Observed anatomy**

- Container:
- Content:
- Leading element:
- Trailing element:
- Border/separator:
- Surface/elevation:
- Alignment:
- Relationship to neighbors:

**Content behavior**

- Minimum / maximum content:
- Wrapping:
- Truncation:
- Empty content:
- Localization risk:

**Interaction and state**

| State | Observed / inferred / proposed | Appearance | Behavior | Accessibility semantics |
|---|---|---|---|---|
| default | | | | |
| pressed / active | | | | |
| selected | | | | |
| disabled | | | | |
| focus / keyboard | | | | |
| loading / error | | | | |

**Rebuild directive**

```text
[Write measurable implementation language.
Example: Render as a full-width row inside the content column.
Minimum height 52 target points; 16-point leading inset; text expands before
the trailing icon; one-pixel separator begins at the text baseline inset.]
```

---

## 6. Navigation and interaction model

### 6.1 Navigation

| Question | Finding | Evidence | Rebuild decision |
|---|---|---|---|
| What changes the top-level destination? | | | |
| What opens a subordinate surface? | | | |
| What is persistent? | | | |
| What preserves context? | | | |
| Back behavior | | | |

### 6.2 Control semantics

| Element | Generic role | Platform component | Web semantic role | Trigger | Result |
|---|---|---|---|---|---|
| | | | | tap / click / drag / keyboard | |

### 6.3 Gesture and direct manipulation

- Observed gestures:
- Inferred gestures:
- Proposed fallback controls:
- Drag alternatives:
- Keyboard behavior:

### 6.4 Feedback

| Event | Visual feedback | Haptic/audio | Timing evidence | Proposed behavior |
|---|---|---|---|---|
| | | | `[O/I/U]` | |

---

## 7. Typography

### 7.1 Type system summary

| Role | Element IDs | Classification | Estimated size | Weight | Line height | Tracking | Alignment | Evidence |
|---|---|---|---:|---|---:|---:|---|---|
| display | | serif / sans / mono / display | | | | | | |
| title | | | | | | | | |
| body | | | | | | | | |
| metadata | | | | | | | | |
| control label | | | | | | | | |

### 7.2 Typography behavior

- Maximum text measure:
- Line-break character:
- Paragraph spacing:
- Dynamic Type / text scaling:
- Truncation rules:
- Numeric style:
- Korean/English/Japanese considerations:
- Exact family certainty:

### 7.3 Rebuild type tokens

| Token | Proposed value | Basis |
|---|---|---|
| `type.display.primary` | | |
| `type.body.primary` | | |
| `type.meta` | | |
| `type.control` | | |

---

## 8. Color, material, border, and elevation

### 8.1 Palette samples

| Token candidate | Sample location | Sampled value | Semantic role | Theme behavior | Evidence |
|---|---|---|---|---|---|
| `color.background.canvas` | | | | | `[S]` |
| `color.text.primary` | | | | | |
| `color.text.secondary` | | | | | |
| `color.accent.primary` | | | | | |
| `color.border.subtle` | | | | | |

### 8.2 Surface hierarchy

| Layer | Element IDs | Fill/material | Border | Shadow/elevation | Blur | Rebuild rule |
|---|---|---|---|---|---|---|
| canvas | | | | | | |
| raised | | | | | | |
| overlay | | | | | | |

### 8.3 Shape language

- Dominant geometry:
- Corner-radius family:
- Capsule usage:
- Stroke style:
- Separator behavior:
- Optical corrections:
- Shape inconsistencies:

---

## 9. Iconography, imagery, and illustration

### 9.1 Icon system

| Element | Source/family | Stroke/fill | Optical size | Container | Alignment | Confidence |
|---|---|---|---:|---|---|---:|
| | system / custom / unknown | | | | | |

### 9.2 Image treatment

- Asset type: photo / vector / raster illustration / 3D / pixel art / texture
- Crop and aspect ratio:
- Mask:
- Color treatment:
- Blend:
- Content-aware focal point:
- Loading/failure treatment:

### 9.3 Art-direction grammar

| Property | Rule |
|---|---|
| Projection/camera | |
| Light direction | |
| Palette | |
| Texture/grain | |
| Edge treatment | |
| Repetition/variation | |
| Asset consistency gate | |

---

## 10. Data visualization or spatial encoding

Complete only when relevant.

| Visual variable | Encoded data | Scale | Zero / missing value | Legend | Risk |
|---|---|---|---|---|---|
| position | | | | | |
| length/height | | | | | |
| area/size | | | | | |
| color | | | | | |
| opacity/density | | | | | |

### Spatial rendering

- Projection:
- Camera:
- Coordinate orientation:
- Geographic scope:
- Level of detail:
- Occlusion order:
- Boundary treatment:
- Interaction:
- Performance constraint:

---

## 11. Motion and temporal behavior

Static references cannot prove motion.

| Transition | Trigger | From → to | Property changes | Duration | Easing | Evidence |
|---|---|---|---|---:|---|---|
| | | | | | | `[O/I/P/U]` |

- Continuous animation:
- Loading motion:
- Haptic:
- Reduce Motion alternative:
- State restoration:

---

## 12. Responsive and adaptive behavior

### 12.1 Observed viewports

| Ref | Width class | Layout changes | Evidence |
|---|---|---|---|
| | | | |

### 12.2 Reconstruction behavior

| Range / platform class | Reflow | Reveal/hide | Presentation change | Max-width / pane rule |
|---|---|---|---|---|
| compact | | | | |
| medium | | | | |
| expanded | | | | |

Do not present proposed breakpoints as observed unless multiple references establish them.

---

## 13. Accessibility and localization

### 13.1 Observed risks

| Area | Finding | Evidence | Severity for rebuild |
|---|---|---|---|
| text contrast | | | |
| non-text contrast | | | |
| target size | | | |
| focus visibility | | | |
| color-only meaning | | | |
| text resize/reflow | | | |

### 13.2 Required reconstruction behavior

- Semantic names, roles, values:
- Reading and focus order:
- Keyboard support:
- Screen-reader grouping:
- Text scaling:
- Reduced motion:
- RTL:
- Long Korean strings:
- Long English strings:
- Dynamic data extremes:

Do not claim full accessibility conformance from image evidence alone.

---

## 14. Reference decomposition: Borrow / Exclude / Transform

### Borrow

- 
- 
- 

### Exclude

- 
- 
- 

### Transform for the target product

- 
- 
- 

### This / Not this

| This | Not this |
|---|---|
| | |
| | |

---

## 15. Reconstruction specification

### 15.1 Design thesis

```text
[One precise paragraph defining the target result.
Use named patterns, geometry, hierarchy, material, and behavior.]
```

### 15.2 Layout rules

```text
Root:
Content column:
Header:
Primary content:
Secondary content:
Bottom region:
Scroll behavior:
Overlay behavior:
```

### 15.3 Component mapping

| Reference element | Target component | Native/custom | Required customization | State owner |
|---|---|---|---|---|
| | | | | |

### 15.4 Proposed semantic tokens

Use semantic naming. Export a separate `tokens.tokens.json` when useful.

| Token | Type | Light value | Dark value | Description |
|---|---|---|---|---|
| `color.background.canvas` | color | | | |
| `color.text.primary` | color | | | |
| `space.inline.page` | dimension | | | |
| `radius.control` | dimension | | | |
| `type.body.primary` | typography | | | |

### 15.5 State matrix

| Surface/component | Default | Selected | Disabled | Loading | Empty | Error | Large text | Dark |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

### 15.6 Asset production requirements

- Required assets:
- Native text vs baked text:
- Vector/raster:
- Resolution and scale:
- Cropping:
- 9-slice/tile/contain:
- Color space:
- Compression:
- Deterministic variation:
- Asset QA:

### 15.7 Platform implementation language

#### iOS / SwiftUI

```text
[View hierarchy, native components, layout primitives, safe-area behavior,
state ownership, accessibility modifiers, rendering choices.]
```

#### Web

```text
[Semantic HTML, CSS Grid/Flexbox, responsive rules, ARIA pattern,
focus management, asset rendering.]
```

#### Android / Compose

```text
[Scaffold, navigation, adaptive panes, state, semantics, window classes.]
```

#### Flutter

```text
[Scaffold, layout, navigation, semantics, adaptive logic.]
```

Delete irrelevant platform sections.

---

## 16. Explicit prohibitions and non-goals

- Do not:
- Do not:
- Preserve:
- Out of scope:
- Acceptable deviation:
- Unacceptable substitution:

---

## 17. Visual QA and acceptance criteria

### 17.1 Reference-match checkpoints

| Check | Target | Tolerance | Verification method |
|---|---|---|---|
| primary focal order | | | squint test |
| major margins | | | overlay |
| component bounds | | | pixel/point measurement |
| line wrapping | | | target viewport screenshot |
| color hierarchy | | | sampled comparison |
| icon scale/stroke | | | overlay |
| state completeness | | | state matrix |
| light/dark hierarchy | | | paired capture |

### 17.2 Required capture matrix

| Platform/device | Viewport | Theme | Text size | State |
|---|---|---|---|---|
| | | | | |

### 17.3 Acceptance statement

```text
PASS when:
HOLD when:
FAIL when:
```

---

## 18. Uncertainty and decision register

| ID | Question | Current status | Alternatives | Evidence needed | Blocks rebuild |
|---|---|---|---|---|---|
| `U-01` | | unknown / inferred / resolved | | | yes / no |

---

## 19. Source register

| Source ID | Term or claim supported | Authority | URL / document | Section | Verified |
|---|---|---|---|---|---:|
| `SRC-01` | | | | | |

---

## 20. Final build brief

Provide a compact handoff that includes only the final decisions.

```text
SURFACE:
TARGET:
ARCHETYPE:
NAVIGATION:
LAYOUT:
TYPOGRAPHY:
COLOR/MATERIAL:
COMPONENTS:
INTERACTION:
ADAPTATION:
ACCESSIBILITY:
ASSETS:
EXCLUSIONS:
QA GATE:
```

---

## Revision history

| Revision | Date | Change |
|---|---:|---|
| 1 | YYYY-MM-DD | Initial analysis |
