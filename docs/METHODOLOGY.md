# UI Reference Analysis Methodology

Version `1.0.0`

## 1. Purpose

This method converts a visual reference into a reconstruction specification without collapsing observation, terminology, and redesign into the same step.

The required transformation is:

```text
reference evidence
→ literal visual observation
→ normalized design terminology
→ structural explanation
→ measurable rebuild directive
→ implementation mapping
→ visual verification
```

A good analysis lets another designer or developer rebuild the surface without needing the analyst to explain what “clean,” “premium,” “soft,” “editorial,” or “app-like” meant.

## 2. Analysis layers

Analyze each surface across the following layers. Do not replace one layer with another.

1. **Product surface** — screen, route, modal, state, device, viewport.
2. **Interface archetype** — feed, editor, detail view, dashboard, canvas, timeline, map, form.
3. **Information architecture** — primary content, secondary content, navigation, actions.
4. **Interaction pattern** — tabs, disclosure, selection, direct manipulation, drag, search.
5. **Component taxonomy** — button, toolbar, tab bar, list row, dialog, sheet, chip.
6. **Layout system** — stack, grid, pane, overlay, constraints, alignment, safe area.
7. **Visual language** — hierarchy, density, shape language, surface treatment, ornament.
8. **Rendering medium** — native components, vector, raster, pixel art, 3D, shader, photo.
9. **Data encoding** — position, length, size, color, height, density, opacity.
10. **Motion and feedback** — transition, easing, duration, haptic, loading, error.
11. **Accessibility and adaptation** — contrast, focus, scaling, keyboard, RTL, breakpoints.
12. **Implementation translation** — tokens, component mapping, state model, QA tolerances.

## 3. Evidence discipline

### 3.1 Evidence status

Every claim that affects reconstruction must be classified.

| Label | Meaning | Example |
|---|---|---|
| `[O]` | Directly visible | A trailing chevron is visible in the row. |
| `[M]` | Measured from the reference | The left inset is approximately 24 screenshot pixels. |
| `[S]` | Sampled from image data | The dominant background sample is approximately `#F4F1E9`. |
| `[I]` | Inferred but not directly shown | The row probably opens a detail view. |
| `[P]` | Proposed for reconstruction | Use a native navigation push on iOS. |
| `[U]` | Not determinable | The exact typeface cannot be established. |

Do not convert an inference into an observation by using confident wording.

### 3.2 Confidence

Use a numeric confidence value from `0.00` to `1.00`.

- `0.90–1.00`: directly visible, measurable, or documented.
- `0.70–0.89`: strong visual evidence but some ambiguity.
- `0.40–0.69`: plausible inference with alternatives.
- `0.01–0.39`: weak inference; do not use as a hard rebuild requirement.
- `0.00`: unknown.

### 3.3 Source set

For each reference record:

- source type: upload, screenshot, URL, video frame, design file;
- source locator or repository path;
- capture date;
- viewport dimensions and unit;
- device or browser when known;
- theme and locale;
- file hash when stored locally;
- whether the image is original, cropped, scaled, or compressed.

A crop must not be treated as evidence of the full screen shell.

## 4. Measurement protocol

### 4.1 Coordinate systems

Record measurements in both forms when possible:

1. **source pixels** — literal screenshot coordinates;
2. **normalized coordinates** — a `0–1000` coordinate space for width and height.

For a source width `W` and height `H`:

```text
normalized_x = source_x / W × 1000
normalized_y = source_y / H × 1000
```

The origin is the top-left corner.

Do not assume one screenshot pixel equals one platform point or CSS pixel. Convert to points only when the original device viewport, display scale, or design frame is known.

### 4.2 Geometry to record

- root frame and safe-area relationship;
- content margins;
- columns, panes, tracks, and maximum width;
- section gaps and row rhythm;
- component bounding boxes;
- alignment anchors and baselines;
- corner radii, borders, separators, and elevation;
- fixed, sticky, overlay, and scroll regions;
- optical offsets where geometry is intentionally not mathematically centered.

Use ranges when anti-aliasing, compression, or scaling prevents exact measurement.

### 4.3 Typography

Record:

- semantic role;
- visible text;
- type classification: serif, sans, mono, display, humanist, grotesk, etc.;
- estimated family only when distinctive evidence exists;
- size, weight, line height, tracking;
- alignment, measure, wrapping, truncation;
- case, numeral style, and language-specific behavior.

Do not claim an exact font family from appearance alone. Prefer:

```text
[O] high-contrast serif display face
[I] visually similar to a Didone classification
[U] exact family and optical-size axis
```

### 4.4 Color and material

Separate:

- sampled color;
- semantic role;
- opacity;
- blending or translucency;
- border and shadow;
- blur and backdrop treatment;
- light/dark theme behavior.

When sampling a raster screenshot, use a small median sample away from anti-aliased edges. State that the value may be altered by display color management, compression, or transparency.

### 4.5 Motion

A static screenshot does not establish motion. Motion may be documented only from:

- video;
- sequential states;
- source code;
- official product documentation;
- direct interaction.

Otherwise, mark motion as `[P]` or `[U]`.

## 5. Terminology normalization

### 5.1 Naming chain

For every important element, record the chain:

```text
literal observation
→ generic interaction/component term
→ platform-specific component term
→ visual treatment
→ rebuild instruction
```

Example:

```text
“rounded blue control at bottom right”
→ action button
→ iOS Button / web button element
→ filled, capsule-shaped, elevated
→ 48 pt height, 20 pt horizontal padding, one primary action
```

### 5.2 Authority classification

Attach an authority class to the term. Use `docs/TERMINOLOGY_SOURCES.md`.

A term can have more than one mapping. Example:

- `button`: generic component term;
- `Button`: Apple or Material component name;
- `role="button"`: accessibility semantics;
- `filled button`: visual/component variant.

Do not merge these into one claim.

### 5.3 Style names

Terms such as `editorial UI`, `glassmorphism`, `neobrutalism`, `bento layout`, and `soft pixel art` are descriptive industry labels. They are useful only when accompanied by observable traits.

Required style classification format:

```text
Primary label:
Authority: INDUSTRY_CONVENTIONAL
Evidence:
- typography-led hierarchy
- asymmetric image/text composition
- large negative space
- low interface chrome

Not implied:
- magazine pagination
- print-only layout
- hidden navigation
```

### 5.4 Project labels

Project-defined labels are allowed when no single industry term captures the combination. Define them as a bundle of existing terms and constraints.

Example:

```text
Project label: Productive Editorial Minimal
Authority: PROJECT_DEFINED
Definition:
Editorial hierarchy + low chrome + visible task controls + progressive disclosure.
```

## 6. Element inventory

Assign stable IDs by function and order:

- `NAV-01`, `NAV-02`
- `ACT-01`
- `TXT-01`
- `IMG-01`
- `ROW-01`
- `SUR-01`
- `DEC-01`
- `SYS-01`

Each element entry must include:

1. reference ID and bounding region;
2. literal observation;
3. canonical term;
4. authority class and source;
5. role in the information hierarchy;
6. visual anatomy;
7. content behavior;
8. interaction and states;
9. measurement;
10. evidence status and confidence;
11. rebuild directive.

Decorative elements must not be assigned interactive semantics.

## 7. Reference decomposition

A named reference is never copied as one indivisible style. Use:

### Borrow

Observable properties to preserve.

### Exclude

Properties present in the reference that do not fit the target product.

### Transform

How the borrowed property changes for the target platform, data, brand, or scale.

Example:

```text
Reference: architectural axonometric game scene

Borrow:
- fixed orthographic camera
- bounded miniature composition
- clear top/left/right plane separation

Exclude:
- impossible geometry
- fantasy architecture
- character-driven interaction

Transform:
- use real administrative polygons
- encode active days as cell extrusion
- preserve north-up orientation
```

## 8. Reconstruction specification

The rebuild section must be executable language, not a mood board.

### 8.1 Layout rules

Use constraints and relationships:

```text
Root content width = min(viewport - 40 pt, 680 pt)
Leading and trailing inset = 20 pt
Title baseline = safe-area top + 44 pt
Body begins 32 pt below title block
Bottom action remains outside scroll content
```

### 8.2 Component rules

For each component define:

- role;
- anatomy;
- variants;
- states;
- size;
- content limits;
- interaction;
- accessibility semantics;
- platform mapping.

### 8.3 Token rules

Use semantic tokens, not screenshot-specific names.

Preferred:

```text
color.background.canvas
color.text.primary
space.section.l
radius.control
type.body.primary
```

Avoid:

```text
beige1
grayButton
spacing27
```

When exporting tokens, prefer the stable DTCG 2025.10 format and record the specification version.

### 8.4 State matrix

At minimum consider:

- default;
- pressed/active;
- selected;
- disabled;
- focus/keyboard;
- loading;
- empty;
- error;
- long content;
- localization;
- light/dark theme;
- reduced motion;
- large text.

Only label a state as observed when it appears in the reference set.

## 9. Platform translation

Separate source appearance from target implementation.

| Target | Translation examples |
|---|---|
| iOS / SwiftUI | NavigationStack, Tab, toolbar, sheet, safeAreaInset, Dynamic Type |
| Android / Compose | Scaffold, NavigationSuite, ModalBottomSheet, WindowSizeClass |
| Web | semantic HTML, CSS Grid/Flexbox, dialog, popover, ARIA APG patterns |
| Flutter | Scaffold, NavigationBar, Sliver, LayoutBuilder, Semantics |

A visual resemblance does not justify replacing native semantics with a custom drawing when a platform component already matches the role.

Conversely, a custom visual surface may still use native accessibility semantics.

## 10. Accessibility analysis

Separate observed accessibility evidence from reconstruction requirements.

Check:

- text and non-text contrast;
- target size;
- visible focus;
- keyboard sequence;
- label, role, value;
- text resize and reflow;
- screen-reader grouping;
- color-independent meaning;
- reduced motion;
- RTL;
- long Korean, English, and Japanese strings where relevant.

Do not claim WCAG conformance from a screenshot. A screenshot can reveal possible risks, not full conformance.

## 11. QA protocol

### 11.1 Visual checkpoints

Compare:

- root composition and reading order;
- margins and major baselines;
- component geometry;
- typography line breaks;
- surface hierarchy;
- sampled palette;
- icon scale and stroke;
- density;
- empty and error states;
- light/dark behavior.

### 11.2 Suggested tolerances

Use these only as default reconstruction tolerances, not universal standards:

- major frame position: ±2% of viewport;
- repeated spacing rhythm: ±2 source pixels or ±1 target point when scale is known;
- component size: ±3%;
- sampled flat color: perceptually close after accounting for color profile;
- line wrapping: exact at the declared target viewport;
- count and order of visible elements: exact.

### 11.3 Squint and thumbnail tests

- At a glance, the same primary focal element should dominate.
- At 25% scale, the same major silhouette and hierarchy should remain.
- In grayscale, hierarchy should not depend solely on hue.
- With text replaced by blocks, layout rhythm should still match.

## 12. Completion gate

An analysis is complete only when:

- reference inventory is complete;
- observed and inferred claims are separated;
- important elements have stable IDs;
- important terms have authority classes and sources;
- reconstruction constraints are measurable;
- hidden states are not fabricated;
- explicit exclusions are recorded;
- uncertainties are listed;
- QA criteria are testable;
- `manifest.json` validates against the repository schema.
