# Skill Specification Draft: UI Reference Reconstruction

Status: design contract only; not yet packaged or installed.

Proposed skill name: `ui-reference-reconstruction`

## 1. Trigger

Run when the user asks to:

- analyze an app or website UI;
- identify the formal names of visible UI elements;
- describe a reference image in implementation language;
- reproduce, borrow, compare, or red-team a visual style;
- convert a screenshot or reference into a design/development brief.

Do not trigger for a pure code review with no UI reference unless the user also requests visual analysis.

## 2. Required inputs

At least one:

- uploaded image;
- accessible public URL;
- repository asset;
- design file export;
- video or sequential screen captures.

Useful optional inputs:

- target platform;
- target framework;
- faithful reconstruction vs selective borrowing;
- required states;
- intended storage policy for reference images.

Do not block execution when optional inputs are absent. Infer a reasonable target scope and record the uncertainty.

When the user supplies an exact App Store, Google Play, or equivalent store URL or ID, treat that identity as authoritative. Do not replace it with a similarly named product found through fuzzy search.

## 3. Required operations

1. Resolve the exact product identity and all reference assets.
2. For a public app listing, enumerate every published screenshot and preview for the declared storefront, locale, platform, and device family before analysis begins.
3. Require the published and analyzed asset counts to match; record any technically inaccessible asset as an explicit blocker or accepted limitation.
4. Capture metadata: dimensions, source, date, theme, locale, crop status, published order, and content hash when available.
5. Inspect every image at full resolution, including repeated, sparse, empty, modal, settings, and secondary-flow states.
6. Create a new analysis ID and folder.
7. Fill `analysis.md` from the canonical template.
8. Fill `manifest.json` against the schema.
9. Normalize terms using the authority hierarchy.
10. Use current official sources when platform terminology may have changed.
11. Separate observed, measured, sampled, inferred, proposed, and unknown claims.
12. Produce a reconstruction specification and QA gate.
13. Commit the completed analysis to `eiranotes/eiraUI`.

## 4. Mandatory output sections

- reconstruction directive;
- evidence inventory;
- literal description;
- interface archetype;
- terminology normalization table;
- region and element inventory;
- layout geometry;
- typography;
- color/material;
- imagery/iconography;
- interaction and state;
- responsive/adaptive behavior;
- accessibility/localization;
- Borrow / Exclude / Transform;
- component and token mapping;
- explicit prohibitions;
- uncertainty register;
- QA acceptance criteria;
- source registry;
- final build brief.

## 5. Source precedence

1. normative standards;
2. W3C guidance;
3. target-platform official design guidance;
4. stable open specification;
5. established research;
6. industry-conventional terminology;
7. project-defined terminology.

A search result or style-gallery label is not sufficient evidence for “official.”

## 6. Image-analysis rules

- Use the original image, not a low-resolution preview, when available.
- For public app listings, analyze the complete published set in store order; do not select only representative screenshots.
- Record published count, analyzed count, storefront, locale, platform, device family, and unavailable assets.
- Record image transformations.
- Use screenshot pixels and normalized coordinates.
- Do not assume screenshot pixels equal platform points.
- Do not infer off-screen structure from a crop.
- Do not infer motion from one frame.
- Do not identify an exact font without metadata or highly distinctive evidence.
- Use confidence values for uncertain classifications.
- Annotated outputs must preserve element IDs used in the document.

## 7. Writing rules

- Start with the build directive.
- Prefer exact nouns and constraints over mood adjectives.
- Do not redefine correct user language unless precision materially improves.
- Do not mix analysis with redesign recommendations.
- Write recommendations only in `[P] PROPOSED` sections.
- Avoid duplicate explanations across sections; cross-reference element IDs.
- Use Korean prose with established English design terms in parentheses where useful.

## 8. Repository output

Path:

```text
analyses/YYYY/YYYY-MM-DD--product--surface/
```

Required:

```text
analysis.md
manifest.json
```

Optional:

```text
references/
annotations/
tokens.tokens.json
implementation/
```

## 9. Completion checks

The skill must not mark an analysis complete unless:

- every important element has an ID;
- an exact store URL or ID has been matched to the correct app and developer when applicable;
- every public app-listing screenshot in the declared scope has a stable reference ID and has been analyzed;
- published and analyzed reference counts match unless a recorded limitation was explicitly accepted;
- every important term has an authority class;
- observations and inferences are distinguishable;
- at least one measurable rebuild directive exists for each major region;
- the final brief contains no undefined style adjective;
- uncertainties are present even when empty;
- source verification dates are recorded;
- the manifest validates;
- storage paths actually exist before they are referenced.

## 10. Future packaging tasks

- convert this draft into an installable `SKILL.md`;
- add repository write and branch policy;
- add a schema validation command;
- add image annotation generation;
- add DTCG token export;
- add per-platform implementation adapters;
- add duplicate-analysis detection;
- add App Store and Google Play full-reference inventory adapters;
- add revision and supersession handling.
