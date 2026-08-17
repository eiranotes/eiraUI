# Cool Cat's Behance reference source map

Analysis: `UIR-20260817-001`  
Storage policy: `link_only`  
Verified: `2026-08-17`

The eiraUI repository is public. The Behance project states that no use is allowed without explicit permission from the owner, so the original project media and extracted frames are not copied into the repository.

## Public project completeness

| Scope | Observed | Analyzed |
|---|---:|---:|
| Complete Behance project visual basenames, including cover | 15 | reviewed for scope and system context |
| Distinct consumer mobile screens in the public app GIF | 4 | 4 |
| POS order-management context | 1 | 1 |

The full browser capture discovered 47 media candidates, captured 46, and grouped them into 15 unique visual basenames. The additional files are responsive duplicates. One candidate failed, but its basename was represented by another successfully captured responsive variant, so no unique public visual module was missing from the inventory.

## Reference inventory

| ID | Public locator | Dimensions | Integrity / extraction | Scope |
|---|---|---:|---|---|
| `REF-01` | `https://www.behance.net/gallery/227587773/Cool-Cats-Brand-identity-Coffee-Shop` | 1440×1000 browser viewport; 15,906 px document | workflow artifact `sha256:d6061e02780caeae511a56efa8fb72ce701758cc9058bd6c1b42925ca9e495dd` | full project |
| `REF-02` | `https://mir-s3-cdn-cf.behance.net/project_modules/source/a36aed227587773.6842aa7d3e062.gif` | 2000×1456; 86 frames; 4,000 ms | `15adabe4561edf8affb7341aeefba155904f4916c3bff4cf6ba19cdd2d276d10` | complete app animation |
| `REF-03` | `REF-02`, frame 55, crop `(207,251,433,940)` | 433×940 | `d4e0557664fc45e025211e11a7b571f156e263f2f4464af663904260e61ac0d8` | branded landing |
| `REF-04` | `REF-02`, frame 0, crop `(1278,251,433,940)` | 433×940 | `75f98e570919d380a721d36281232f4e289a449495367bf95bbd2678ec1780fd` | onboarding |
| `REF-05` | `REF-02`, frame 55, crop `(1196,251,433,940)` | 433×940 | `312b9679f7598969dd59a52a3f50608910aa4df4637680111058c3ec433ebd1d` | menu discovery |
| `REF-06` | `REF-02`, frame 0, crop `(290,251,433,940)` | 433×940 | `252c4cd7a1f4ddd733f6812f9ccd30d8f396cdb08bb2873be2060051e5a59bb6` | product detail |
| `REF-07` | `https://mir-s3-cdn-cf.behance.net/project_modules/2800_webp/95a35c227587773.6842aa7d40b50.png` | 2800×1824 | `17eef18711aa6dff3877aff8db688dd868f67730fa96fb33a12d421d963bdd9b` | POS ecosystem |

## Integrity notes

- `REF-03` through `REF-06` are deterministic extracts from `REF-02`, not claims about native device screenshots.
- The source panels are marketing composites. The analysis uses proportional measurement and proposes a 390×844 pt compact iPhone calibration.
- Device bezels, shadows, the gray carousel background, and POS photography are presentation context, not app tokens.
- The app screen inventory is complete for the public animation, but the concept does not show category results, cart, checkout, payment, booking, confirmation, order status, account, or error states.
