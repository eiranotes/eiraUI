# eiraUI

**Reference UI → canonical terminology → reconstruction specification**

eiraUI is a repeatable protocol and knowledge base for analyzing an app or website reference image, naming each visible element with traceable design terminology, and translating the observation into build-ready language.

The repository is not a screenshot gallery. Its primary artifact is a reconstruction document that preserves the chain below:

> **Evidence → Observation → Canonical term → Rebuild directive → Verification**

## Core contract

Every completed analysis must:

1. identify the exact reference set and viewport;
2. separate what is visible from what is inferred;
3. decompose the surface into layout, navigation, components, typography, color, imagery, motion, and state;
4. attach an authority class and source to each important term;
5. translate descriptive language into measurable reconstruction rules;
6. state what must not be copied or introduced;
7. include uncertainty and visual QA criteria;
8. be saved under `analyses/` using the repository convention.

The canonical human-readable template is:

- [`templates/UI_REFERENCE_RECONSTRUCTION.md`](templates/UI_REFERENCE_RECONSTRUCTION.md)

The machine-readable contract prepared for later skill automation is:

- [`schemas/ui-reference-analysis.schema.json`](schemas/ui-reference-analysis.schema.json)

## Repository structure

```text
eiraUI/
├── analyses/                         # Completed analyses, one folder per reference surface
├── docs/
│   ├── METHODOLOGY.md                # Analysis method and evidence rules
│   ├── STORAGE_CONVENTION.md         # Paths, IDs, filenames, and reference handling
│   └── TERMINOLOGY_SOURCES.md        # Authority hierarchy and source registry
├── examples/
│   └── editorial-reading-screen/     # Fully worked synthetic example
├── schemas/
│   └── ui-reference-analysis.schema.json
├── skill/
│   └── SKILL_SPEC_DRAFT.md           # Contract for the future automated skill
└── templates/
    └── UI_REFERENCE_RECONSTRUCTION.md
```

## Minimum output for each analysis

```text
analyses/YYYY/YYYY-MM-DD--product--surface/
├── analysis.md                       # Required
├── manifest.json                     # Required
├── references/                       # Optional local references or source map
├── annotations/                      # Optional overlays and measurement diagrams
└── tokens.tokens.json                # Optional DTCG-compatible reconstruction tokens
```

`analysis.md` is the authoritative explanation. `manifest.json` is the structured index used for validation, search, and future skill execution.

## Terminology authority classes

“Official term” is not a single category. Every important term must be tagged with one of the following:

| Code | Authority class | Typical source |
|---|---|---|
| `STANDARD_NORMATIVE` | Normative standard or specification | WCAG, CSS, WAI-ARIA |
| `W3C_GUIDANCE` | W3C-authored implementation guidance | ARIA Authoring Practices Guide |
| `PLATFORM_OFFICIAL` | Vendor platform design language | Apple HIG, Material, Android, Fluent |
| `STABLE_OPEN_SPEC` | Stable open specification outside the W3C Standards Track | DTCG 2025.10 |
| `RESEARCH_PRACTICE` | Established UX research or practice vocabulary | NN/g, Baymard |
| `INDUSTRY_CONVENTIONAL` | Widely used descriptive term without one normative owner | editorial UI, glassmorphism |
| `PROJECT_DEFINED` | eiraUI or product-specific label | Productive Editorial Minimal |

A visual style name must not be presented as a normative standard unless a normative source actually defines it.

## Evidence labels

Use these labels in the analysis:

- `[O] OBSERVED` — directly visible in the reference.
- `[M] MEASURED` — calculated from image pixels or known viewport geometry.
- `[S] SAMPLED` — sampled from image data, typically color.
- `[I] INFERRED` — plausible behavior or structure not directly visible.
- `[P] PROPOSED` — reconstruction decision introduced for implementation.
- `[U] UNKNOWN` — cannot be determined from available evidence.

Screenshot-only analysis cannot prove hidden states, animation timing, accessibility semantics, exact font files, or responsive behavior. Those items remain inferred, proposed, or unknown until supported by additional evidence.

## Operating rule for future analyses

When a user asks to analyze an app, site, or UI reference:

1. collect the reference images or capture the relevant states;
2. create a new analysis folder following `docs/STORAGE_CONVENTION.md`;
3. copy the canonical template to `analysis.md`;
4. create `manifest.json` conforming to the schema;
5. perform the analysis using `docs/METHODOLOGY.md`;
6. save evidence links, local assets when permitted, and source dates;
7. validate the output against the checklist in the template;
8. commit the completed analysis to this repository.

## Current status

- Protocol version: `1.0.0`
- Template version: `1.0.0`
- Skill status: specification draft; not yet packaged or installed
- Terminology source registry verified: `2026-08-08`
