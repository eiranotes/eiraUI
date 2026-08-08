# Analysis Storage Convention

Version `1.0.0`

## 1. Folder path

Every completed analysis is stored at:

```text
analyses/YYYY/YYYY-MM-DD--product-slug--surface-slug/
```

Example:

```text
analyses/2026/2026-08-08--sample-notes--today-screen/
```

Use lowercase kebab-case for slugs.

## 2. Required files

```text
analysis.md
manifest.json
```

`analysis.md` follows `templates/UI_REFERENCE_RECONSTRUCTION.md`.

`manifest.json` follows `schemas/ui-reference-analysis.schema.json`.

## 3. Optional files

```text
references/
  source-map.md
  ref-01.png
  ref-02.png
annotations/
  ref-01-elements.svg
  ref-01-measurements.svg
tokens.tokens.json
implementation/
  swiftui.md
  web.md
  flutter.md
```

## 4. Analysis ID

Use:

```text
UIR-YYYYMMDD-NNN
```

Example:

```text
UIR-20260808-001
```

The sequence is repository-wide for that date.

## 5. Reference IDs

Use:

```text
REF-01
REF-02
REF-03
```

Do not renumber references after publication. Add new IDs.

## 6. Element IDs

Use semantic prefixes:

| Prefix | Meaning |
|---|---|
| `SYS` | system chrome or safe-area feature |
| `NAV` | navigation |
| `ACT` | action or control |
| `TXT` | text block |
| `IMG` | image, illustration, video |
| `ROW` | row or list item |
| `GRP` | group or section |
| `SUR` | surface or container |
| `DEC` | decoration |
| `DAT` | data visualization |
| `OVR` | overlay, dialog, sheet, popover |
| `FDB` | feedback, progress, error, status |

Example: `NAV-01`, `TXT-03`, `DAT-02`.

## 7. Reference handling

The repository is public. Record one of these policies in `manifest.json`:

- `link_only` — store the source locator and analysis, not the original asset;
- `local_public` — store the reference in the repository;
- `local_authorized` — store because the user or rights holder authorized it;
- `generated` — reference was created for this repository;
- `private_uncommitted` — analyzed locally but not committed.

For locally stored files, record:

- path;
- SHA-256;
- original dimensions;
- transformation: original, crop, resize, compression, annotation.

Never invent a sandbox or repository path for an asset that was not actually stored.

## 8. Analysis lifecycle

Use one of:

- `draft`
- `complete`
- `superseded`

A completed analysis may be revised in place while preserving its ID. Record revision history at the bottom of `analysis.md`.

When a new reference changes the interpretation substantially, create a new analysis ID and link `supersedes` / `supersededBy` in the manifests.

## 9. Commit convention

Suggested commit messages:

```text
add UIR-20260808-001 reference analysis
refine UIR-20260808-001 reconstruction spec
add reference states for UIR-20260808-001
```

Do not combine unrelated product analyses in one commit.

## 10. Minimum source map

When reference files are not committed, create `references/source-map.md`:

```markdown
# Reference source map

| ID | Locator | Captured | Viewport | Storage |
|---|---|---:|---|---|
| REF-01 | https://example.com/path | 2026-08-08 | 1440×1200 px | link_only |
```
