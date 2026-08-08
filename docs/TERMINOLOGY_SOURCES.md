# Terminology Authority and Source Registry

Verified `2026-08-08`

This registry defines where eiraUI obtains component names, interaction patterns, layout terminology, accessibility requirements, and design-token vocabulary.

## 1. Authority classes

### `STANDARD_NORMATIVE`

Use for requirements or terminology from a standards-track specification.

Examples:

- WCAG 2.2 success criteria;
- WAI-ARIA roles, states, and properties;
- CSS layout terminology.

A normative source can define technical conformance. It does not define every visual style.

### `W3C_GUIDANCE`

Use for W3C-authored implementation guidance that demonstrates patterns but is not itself the normative specification.

Primary example:

- WAI-ARIA Authoring Practices Guide (APG).

### `PLATFORM_OFFICIAL`

Use for vendor-authored design systems and platform component guidance.

Examples:

- Apple Human Interface Guidelines;
- Material Design and Android design guidance;
- Microsoft Fluent 2.

These names are official within their platform scope, not universal web or cross-platform standards.

### `STABLE_OPEN_SPEC`

Use for a stable, public specification that is explicitly outside the W3C Standards Track.

Primary example:

- Design Tokens Community Group specification `2025.10`.

### `RESEARCH_PRACTICE`

Use for established research and practitioner vocabulary.

Examples:

- Nielsen Norman Group;
- Baymard Institute.

These sources support usage guidance and pattern interpretation. They are not normative standards.

### `INDUSTRY_CONVENTIONAL`

Use for common descriptive labels without a single authoritative owner.

Examples:

- editorial UI;
- glassmorphism;
- neobrutalism;
- bento layout;
- canvas-first editor;
- soft pixel art.

Every use must include observable defining traits.

### `PROJECT_DEFINED`

Use for labels defined in eiraUI or a specific product.

Examples:

- Productive Editorial Minimal;
- Grayscale Axonometric Atlas;
- Narrative Share Artifact.

The definition must list the underlying standard, platform, and industry terms.

## 2. Primary source registry

| Domain | Source | Authority | Use |
|---|---|---|---|
| Apple components | https://developer.apple.com/design/human-interface-guidelines/components/ | `PLATFORM_OFFICIAL` | Apple component names and usage |
| Apple layout | https://developer.apple.com/design/human-interface-guidelines/layout | `PLATFORM_OFFICIAL` | safe areas, layout guides, adaptation |
| Material components | https://m3.material.io/components | `PLATFORM_OFFICIAL` | Material component names and variants |
| Android design | https://developer.android.com/design/ui/mobile | `PLATFORM_OFFICIAL` | Android foundations, patterns, components |
| Android adaptive layout | https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout | `PLATFORM_OFFICIAL` | reflow, reveal, presentation change, panes |
| Fluent 2 | https://fluent2.microsoft.design/ | `PLATFORM_OFFICIAL` | Microsoft component and token language |
| ARIA APG patterns | https://www.w3.org/WAI/ARIA/apg/patterns/ | `W3C_GUIDANCE` | accessible widget pattern names and behavior |
| WAI-ARIA | https://www.w3.org/TR/wai-aria-1.2/ | `STANDARD_NORMATIVE` | roles, states, properties |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | `STANDARD_NORMATIVE` | accessibility success criteria |
| CSS Grid | https://www.w3.org/TR/css-grid/ | `STANDARD_NORMATIVE` | grid tracks, lines, cells, placement |
| CSS Flexbox | https://www.w3.org/TR/css-flexbox-1/ | `STANDARD_NORMATIVE` | flex container and item behavior |
| CSS Color | https://www.w3.org/TR/css-color-4/ | `STANDARD_NORMATIVE` | color spaces and CSS color representation |
| DTCG stable format | https://www.designtokens.org/TR/2025.10/format/ | `STABLE_OPEN_SPEC` | interoperable design-token format |
| DTCG resolver | https://www.designtokens.org/TR/2025.10/resolver/ | `STABLE_OPEN_SPEC` | themes, modes, and token resolution |
| NN/g articles | https://www.nngroup.com/articles/ | `RESEARCH_PRACTICE` | interaction and usability terminology |
| Baymard research | https://baymard.com/research | `RESEARCH_PRACTICE` | evidence-based web and commerce patterns |

## 3. Source precedence

When sources use different names:

1. use the target platform’s official component name for implementation;
2. use the standards term for semantics and conformance;
3. use a generic industry term for cross-platform explanation;
4. record aliases rather than declaring one universal name.

Example:

```text
Generic: bottom navigation
Apple platform: tab bar
Material platform: navigation bar
Web semantics: navigation landmark containing links or buttons, depending on behavior
Visual treatment: persistent bottom-aligned icon-and-label navigation
```

## 4. Source citation format

Every important term entry should include:

```text
Canonical term:
Authority:
Source:
Source section or component page:
Platform scope:
Alias:
Reason selected:
```

Do not cite a homepage when a component-specific page exists.

## 5. Special rules

### Visual styles

A style gallery can be used to find candidate labels, but it does not elevate the label to a standard. Confirm the style through observable properties.

### Accessibility

- WCAG defines testable success criteria for web content.
- WAI-ARIA defines semantics.
- APG demonstrates implementation patterns.
- Platform accessibility guidance may add platform-specific behavior.

Do not treat these as interchangeable.

### Design tokens

The DTCG `2025.10` specification is stable and production-oriented, but it is not a W3C Recommendation or on the W3C Standards Track. Record it as `STABLE_OPEN_SPEC`, not `STANDARD_NORMATIVE`.

### Current documentation

Platform guidance changes. Record the access or verification date for any terminology that can change, especially Apple, Android, Material, and Fluent.
