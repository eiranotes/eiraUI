# grumbl. public App Store reference source map

Analysis: `UIR-20260809-001`  
App Store ID: `6772917460`  
Verified: `2026-08-09`  
Storage policy: `link_only`

All six iPhone screenshots publicly exposed by the US App Store were retrieved in Apple Lookup order, inspected through a one-day CI artifact, and excluded from the public repository. The source URLs and integrity metadata are retained below.

| ID | Order | Surface | Apple-hosted locator | Dimensions | SHA-256 | Storage |
|---|---:|---|---|---:|---|---|
| `REF-01` | 1 | Photos — dense date group, catch-up banner, inline ad, bottom acquisition bar | `https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/95/31/80/953180d2-c759-fdd2-abb8-a73a7d37b06b/grumbl_screenshot_2_1284x2778_blurred_ads.png/0x0ss.jpg` | 1284×2778 px | `42e75f3a2078d89c5b316a2067f980cf4a86c2f6454ce1e548394332f849e8fd` | `link_only` |
| `REF-02` | 2 | Photos — sparse date groups and empty current-day header | `https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/ef/91/19/ef9119f0-7490-9c7f-cfcc-b0f3bf99a5cd/grumbl_screenshot_1_1284x2778_blurred_ads.png/0x0ss.jpg` | 1284×2778 px | `0283007e6d08218af57afe6d068ff8292d88e8ec46f41b26f1c4ce474723477c` | `link_only` |
| `REF-03` | 3 | Calendar — May 2026 thumbnail month grid | `https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/d1/b9/a1/d1b9a1cf-d54a-ffa0-7458-d2b78e55bb14/grumbl_screenshot_3_1284x2778_blurred_ads.png/0x0ss.jpg` | 1284×2778 px | `ca9e0c08068e147e90bac0e4baf492dd8cb18ccb3f5eb043a32deead2d74ff07` | `link_only` |
| `REF-04` | 4 | Map — Seattle-area photo-stack annotations | `https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/28/a8/04/28a804f2-9aa6-9cf2-142b-8766f37f2248/grumbl_screenshot_4_1284x2778_blurred_ads.png/0x0ss.jpg` | 1284×2778 px | `651cb8326d81ae3a30dae112ccf19e45054fe158efab7cbcec91e21bf0459e33` | `link_only` |
| `REF-05` | 5 | Scan Camera Roll — look-back range single-selection sheet | `https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/cb/5e/bc/cb5ebc5e-f2bf-d9d7-46f7-da09be3630c2/grumbl_screenshot_6_1284x2778_blurred_ads.png/0x0ss.jpg` | 1284×2778 px | `9b767b8c0d912c211f8f40afa2fab8b1ff09975d8bed9beb1e14b137432349a5` | `link_only` |
| `REF-06` | 6 | Settings — grouped disclosure-list sheet | `https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/04/bd/e7/04bde7dc-0f24-401a-2fb8-7884df49a5af/grumbl_screenshot_5_1284x2778_blurred_ads.png/0x0ss.jpg` | 1284×2778 px | `5dba7e90031dc63db4bd4fa6fdddcb888cb5b0000365bc5e5b9a197d1ca73e0d` | `link_only` |

## Capture record

- Apple Lookup screenshot count: `6`.
- Successfully captured unique screenshots: `6`.
- All images share the same 1284×2778 px portrait frame.
- The exact dimensions divide to approximately 428×926 pt at 3×; this is used as a reconstruction calibration, not as proof of the physical device model.
- The marketing image filenames contain `blurred_ads`; ad placement and framing are analyzed, but blurred creative content is not treated as production UI evidence.
- No repository path or checksum is claimed for an image copy in Git because no screenshot original is committed.

## Reference-to-element coverage

| Reference | Required analysis coverage |
|---|---|
| `REF-01` | branded masthead; top toolbar; text tab strip; meal count; missed-meal banner; date header; dense 3-column grid; time badges; sponsored placement; bottom Camera/Library actions |
| `REF-02` | sparse and empty date states; incomplete rows; blank grid positions; sponsored placement; shared shell |
| `REF-03` | month pager; weekday row; six-week thumbnail calendar; adjacent-month treatment; day/count overlays; bottom acquisition bar |
| `REF-04` | Apple map; summary badge; photo-stack annotations; geographic density; attribution; bottom acquisition bar |
| `REF-05` | modal sheet; custom header; explanatory copy; look-back radio group; selected indicator; Start Scan; privacy footnote |
| `REF-06` | modal Settings sheet; grouped disclosure list; section headers; list separators; chevrons; About lockup and version |

## Public product sources

- App Store listing: `https://apps.apple.com/us/app/grumbl/id6772917460`
- Apple public Lookup endpoint used by capture utility: `https://itunes.apple.com/lookup?id=6772917460&country=us`
