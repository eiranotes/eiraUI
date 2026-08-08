#!/usr/bin/env python3
"""Apply the complete-public-app-listing reference rule to eiraUI protocol files."""

from __future__ import annotations

from pathlib import Path


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}\nNEEDLE:\n{old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    methodology = Path("docs/METHODOLOGY.md")
    skill = Path("skill/SKILL_SPEC_DRAFT.md")
    template = Path("templates/UI_REFERENCE_RECONSTRUCTION.md")
    readme = Path("README.md")

    replace_once(methodology, "Version `1.0.0`", "Version `1.1.0`")

    replace_once(
        methodology,
        "A crop must not be treated as evidence of the full screen shell.\n\n## 4. Measurement protocol",
        """A crop must not be treated as evidence of the full screen shell.

### 3.4 Complete public app-listing reference rule

When the subject is a released app with a public App Store, Google Play, or equivalent store listing, the public listing is a finite reference inventory rather than a pool from which to select attractive examples.

Before visual analysis:

1. resolve the exact product identity from the user-supplied store URL or store ID;
2. verify the displayed app name, developer, platform, storefront, and locale;
3. count every publicly visible screenshot and preview for the requested device family;
4. retrieve the highest-resolution public form available;
5. preserve the published order and assign one stable `REF` ID to every asset;
6. record the published count, analyzed count, missing count, capture date, dimensions, and transformation status.

Analyze every public screenshot, including:

- repeated variants of the same surface;
- sparse, empty, or partially populated states;
- settings, permissions, utility sheets, and secondary flows;
- screenshots whose primary difference is density, selection, or data distribution;
- blurred advertising regions, while limiting analysis to placement and container treatment rather than the hidden creative.

Do not stop after representative screenshots. A public app-listing analysis is incomplete when the published count and analyzed count differ, unless an asset is technically inaccessible and the limitation is explicitly recorded.

When multiple storefronts or device families expose different sets, scope the inventory explicitly, for example:

```text
US App Store · iPhone · English · 6 published / 6 analyzed
US App Store · iPad · no public screenshots
```

Byte-identical duplicates may share one visual analysis, but every published occurrence must remain in the inventory with its source alias and order. Do not substitute a similarly named app found through fuzzy search when the user supplied an exact store identity.

## 4. Measurement protocol""",
    )

    replace_once(
        methodology,
        """- reference inventory is complete;
- observed and inferred claims are separated;""",
        """- reference inventory is complete;
- for a public app listing, the exact app identity is verified and the published/analyzed screenshot counts match for the declared storefront, locale, platform, and device family;
- observed and inferred claims are separated;""",
    )

    replace_once(
        skill,
        """Do not block execution when optional inputs are absent. Infer a reasonable target scope and record the uncertainty.

## 3. Required operations""",
        """Do not block execution when optional inputs are absent. Infer a reasonable target scope and record the uncertainty.

When the user supplies an exact App Store, Google Play, or equivalent store URL or ID, treat that identity as authoritative. Do not replace it with a similarly named product found through fuzzy search.

## 3. Required operations""",
    )

    replace_once(
        skill,
        """1. Resolve all reference assets.
2. Capture metadata: dimensions, source, date, theme, locale, crop status.
3. Inspect the image at full resolution.
4. Create a new analysis ID and folder.
5. Fill `analysis.md` from the canonical template.
6. Fill `manifest.json` against the schema.
7. Normalize terms using the authority hierarchy.
8. Use current official sources when platform terminology may have changed.
9. Separate observed, measured, sampled, inferred, proposed, and unknown claims.
10. Produce a reconstruction specification and QA gate.
11. Commit the completed analysis to `eiranotes/eiraUI`.""",
        """1. Resolve the exact product identity and all reference assets.
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
13. Commit the completed analysis to `eiranotes/eiraUI`.""",
    )

    replace_once(
        skill,
        """- Use the original image, not a low-resolution preview, when available.
- Record image transformations.""",
        """- Use the original image, not a low-resolution preview, when available.
- For public app listings, analyze the complete published set in store order; do not select only representative screenshots.
- Record published count, analyzed count, storefront, locale, platform, device family, and unavailable assets.
- Record image transformations.""",
    )

    replace_once(
        skill,
        """- every important element has an ID;
- every important term has an authority class;""",
        """- every important element has an ID;
- an exact store URL or ID has been matched to the correct app and developer when applicable;
- every public app-listing screenshot in the declared scope has a stable reference ID and has been analyzed;
- published and analyzed reference counts match unless a recorded limitation was explicitly accepted;
- every important term has an authority class;""",
    )

    replace_once(
        skill,
        """- add duplicate-analysis detection;
- add revision and supersession handling.""",
        """- add duplicate-analysis detection;
- add App Store and Google Play full-reference inventory adapters;
- add revision and supersession handling.""",
    )

    replace_once(template, 'template_version: "1.0.0"', 'template_version: "1.1.0"')

    replace_once(
        template,
        """| `REF-01` | upload / screenshot / URL / video frame / design file | | | `W×H px` | | original / crop / resized | |

### 1.3 Evidence limitations""",
        """| `REF-01` | upload / screenshot / URL / video frame / design file | | | `W×H px` | | original / crop / resized | |

### 1.2a Public app-listing completeness

Complete this table whenever the subject has a public App Store, Google Play, or equivalent listing.

| Storefront | Platform / device family | Locale | Published assets | Analyzed assets | Missing / inaccessible | Verified |
|---|---|---|---:|---:|---|---:|
| | | | | | | |

**Identity check:** `[store URL or ID]` → `[displayed app name]` → `[developer]`  
**Coverage result:** `complete / incomplete / accepted limitation`  

A store-listing analysis is not complete when the published and analyzed counts differ without an explicit accepted limitation. Keep every asset in published order even when screens are visually similar.

### 1.3 Evidence limitations""",
    )

    replace_once(
        readme,
        """1. identify the exact reference set and viewport;
2. separate what is visible from what is inferred;""",
        """1. identify the exact reference set and viewport; for public app listings, verify the exact app identity and analyze every published screenshot in the declared scope;
2. separate what is visible from what is inferred;""",
    )

    replace_once(
        readme,
        """1. collect the reference images or capture the relevant states;
2. create a new analysis folder following `docs/STORAGE_CONVENTION.md`;""",
        """1. collect the complete reference set; for a public app listing, enumerate all published screenshots and previews before analysis;
2. create a new analysis folder following `docs/STORAGE_CONVENTION.md`;""",
    )

    replace_once(readme, "- Protocol version: `1.0.0`", "- Protocol version: `1.1.0`")
    replace_once(readme, "- Template version: `1.0.0`", "- Template version: `1.1.0`")


if __name__ == "__main__":
    main()
