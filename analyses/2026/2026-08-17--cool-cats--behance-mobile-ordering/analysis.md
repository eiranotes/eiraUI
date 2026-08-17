---
schema_version: "1.0.0"
analysis_id: "UIR-20260817-001"
status: "complete"
created_at: "2026-08-17"
updated_at: "2026-08-17"
title: "Cool Cat's Café — Behance mobile ordering concept reconstruction"
subject:
  product_name: "Cool Cat's Café"
  product_type: "app"
  surface_name: "Four public consumer mobile screens and POS ecosystem context"
  platform: "iOS concept"
  locale: "en"
  theme: "light / branded blue"
target:
  platform: "iOS"
  framework: "SwiftUI"
  purpose: "selective-borrowing"
reference_storage: "link_only"
template_version: "1.1.0"
---

# Cool Cat's Café — Behance Mobile Ordering Concept Reconstruction

## 0. Reconstruction directive

> **Interface archetype:** brand-led café ordering and booking gateway with a configurable product-detail flow  
> **Primary style:** **Playful Monoline Café Commerce** (`PROJECT_DEFINED`)  
> **Underlying terms:** illustration-led brand UI, mascot-driven identity system, editorial commerce, high-contrast duotone shell, rounded-outline controls, low-chrome ordering UI  
> **Reference scope:** every distinct consumer mobile screen visible in the public app animation, `4 published / 4 analyzed`, plus one POS order-management image as ecosystem context  
> **Core visual rule:** saturated cobalt and warm cream form the persistent shell; custom hand-drawn cat illustrations carry brand personality; functional copy uses a compact neutral sans; one realistic product image supplies appetite and purchase evidence  
> **Rebuild rule:** preserve the two-color system, monoline mascot language, sparse composition, rounded category rows, and clear order CTA; separate brand storytelling from task navigation, separate merchandising collections from catalog taxonomy, and bind quantity, price, and order totals to one deterministic cart state  
> **Do not introduce:** glass surfaces, generic food-delivery gradients, card dashboards, unrelated bottom tabs, decorative shadows, emoji as primary controls, or invented checkout/loyalty screens presented as observed reference content

### One-paragraph reconstruction language

```text
Build a consumer café-ordering concept with a cobalt-and-cream brand shell, custom
monoline cat illustrations, a compact sans-serif commerce layer, and restrained rounded
controls. First-run onboarding remains optional and brief. The branded gateway exposes
Bookings and Menu, but Menu becomes the dominant repeat-use route. The menu landing
separates curated collections from product categories. Product detail treats size,
quantity, customization notes, favorite state, and cart total as one coherent data model.
All control labels remain native text, every custom action has at least a 44-point target,
and the product image supports rather than displaces ordering information.
```

---

## 1. Scope and evidence

### 1.1 Exact project identity

| Field | Value |
|---|---|
| Behance project | `Cool Cat's | Brand identity | Coffee Shop` |
| Project ID | `227587773` |
| Published | `2025-06-06` |
| Brand identity and illustrations | Rashmi Sajjan |
| User experience and interface design | Sumesh Magesh Babu |
| Declared scope | custom typography, illustrations, menu, print collateral, point of sales, mobile application design |
| Product context | third-wave coffee shop concept in Kochi |
| Analysis target | consumer mobile ordering UI; POS retained only as supporting ecosystem evidence |

### 1.2 Complete public project capture

A browser capture scrolled the full public project and inspected every Behance project-module asset. The project exposed 15 unique visual basenames including its cover; responsive derivatives produced 46 captured files. The consumer mobile application is presented in one 2000×1456 animated GIF with 86 frames and four distinct mobile screens. All four were extracted and analyzed. A separate 2800×1824 POS image was retained as back-office context.

| Scope | Published/observed | Analyzed | Result |
|---|---:|---:|---|
| Distinct consumer mobile screens in app animation | 4 | 4 | complete |
| POS order-management context images | 1 | 1 | complete |
| Other brand/print/merchandise modules | 10+ | reviewed for visual-system context | outside screen-level app inventory |

### 1.3 Reference inventory

| ID | Reference | Viewport | Transformation | SHA-256 | Storage |
|---|---|---:|---|---|---|
| `REF-01` | Full Behance project page and media inventory | 1440×1000 browser viewport; 15,906 px document | full-page scrolling and module inventory | workflow artifact digest `d6061e02780caeae511a56efa8fb72ce701758cc9058bd6c1b42925ca9e495dd` | `link_only` |
| `REF-02` | Public mobile-app animation GIF | 2000×1456 px, 86 frames, 4,000 ms | none | `15adabe4561edf8affb7341aeefba155904f4916c3bff4cf6ba19cdd2d276d10` | `link_only` |
| `REF-03` | Branded landing screen | 433×940 px marketing panel | frame 55 crop from `REF-02` | `d4e0557664fc45e025211e11a7b571f156e263f2f4464af663904260e61ac0d8` | `link_only` |
| `REF-04` | Onboarding screen | 433×940 px marketing panel | frame 0 crop from `REF-02` | `75f98e570919d380a721d36281232f4e289a449495367bf95bbd2678ec1780fd` | `link_only` |
| `REF-05` | Menu discovery screen | 433×940 px marketing panel | frame 55 crop from `REF-02` | `312b9679f7598969dd59a52a3f50608910aa4df4637680111058c3ec433ebd1d` | `link_only` |
| `REF-06` | Vietnamese Cold Coffee product detail | 433×940 px marketing panel | frame 0 crop from `REF-02` | `252c4cd7a1f4ddd733f6812f9ccd30d8f396cdb08bb2873be2060051e5a59bb6` | `link_only` |
| `REF-07` | Café POS order-management image | 2800×1824 px | responsive original resolved from Behance module | `17eef18711aa6dff3877aff8db688dd868f67730fa96fb33a12d421d963bdd9b` | `link_only` |

### 1.4 Evidence limitations

- `[U]` This is a design case study. No public App Store listing, runtime build, interaction recording, or production analytics were found in the supplied project.
- `[U]` The four 433×940 panels are marketing extractions from a composite GIF, not native device screenshots. Exact iOS point sizes and safe-area values are therefore not provable.
- `[U]` Only one onboarding page is fully visible; the indicator implies three pages.
- `[U]` The category-results screen, product list, cart, checkout, payment, booking flow, confirmation, order tracking, account, and loyalty surfaces are not shown.
- `[U]` Loading, empty, unavailable, sold-out, validation, network-error, favorite-selected, and accessibility states are absent.
- `[U]` The exact custom display and handwritten typefaces are not identified.
- `[U]` The intent and destination of `Cool Cat's Curation` are not stated.
- `[U]` Product quantity and total-price examples appear numerically inconsistent; no live data behavior is available to resolve the prototype values.
- `[U]` The POS image establishes an order object and queue, but no direct integration contract with the consumer concept is shown.

Evidence labels: `[O] OBSERVED` · `[M] MEASURED` · `[S] SAMPLED` · `[I] INFERRED` · `[P] PROPOSED` · `[U] UNKNOWN`

---

## 2. Product and information architecture

### 2.1 Product role

The visible concept combines three jobs:

1. **brand entry:** establish the café identity and route users to bookings or menu;
2. **menu discovery:** expose curated collections and broad food/beverage categories;
3. **item configuration:** select variants and quantities, add a customization note, and add items to an order.

The POS image adds a fourth operational job: staff review and fulfill structured orders through a queue-and-detail interface.

### 2.2 Inferred consumer flow

```text
Optional onboarding
→ branded gateway
├─ Bookings → booking flow [not shown]
└─ Menu
   → menu discovery
   → collection/category results [not shown]
   → product detail
   → cart/order review [not shown]
   → checkout/payment [not shown]
   → confirmation/status [not shown]
```

### 2.3 Navigation model

The public mobile screens do not show a persistent tab bar, navigation drawer, or bottom navigation. Navigation is local and task-based:

- landing: two route buttons;
- onboarding: Skip and Next;
- menu: category/collection rows;
- product detail: Back, Favorite, quantity controls, note field, Add to order.

A faithful reconstruction must not invent a persistent tab shell. A production expansion can introduce one only after the missing cart, orders, booking, and account hierarchy is resolved.

### 2.4 Main structural tension

The brand system is coherent, but the commerce information architecture is incomplete. The Menu screen places `Recommended` and `Popular`—merchandising collections—at the same hierarchy level as `Food` and `Beverages`—catalog categories. This is a **mixed taxonomy**. Users cannot tell whether all four rows are mutually exclusive catalog partitions or different lenses over the same products.

Recommended production structure:

```text
Curated for you
- Recommended
- Popular

Browse the menu
- Food
- Beverages
```

---

## 3. Style classification

### 3.1 Primary label

**Playful Monoline Café Commerce**

Definition:

> A brand-led ordering interface that combines a high-contrast cobalt/cream shell, custom black-or-cream monoline mascot illustrations, irregular display lettering, handwritten microcopy, neutral sans-serif commerce text, and flat rounded controls.

### 3.2 Underlying industry terms

| Term | Application |
|---|---|
| illustration-led brand UI | large custom drawings carry identity and tone |
| mascot-driven identity system | the sunglasses cat and supporting animal scenes recur across app, packaging, print, and POS |
| editorial commerce | expressive copy and illustration frame an otherwise transactional ordering flow |
| high-contrast duotone system | cobalt and warm cream dominate the interface shell |
| low-chrome mobile ordering | little persistent navigation or platform chrome is visible |
| rounded-outline control language | category rows and landing actions use thin rounded outlines |
| full-bleed branded gateway | the landing screen uses a complete cobalt field rather than a neutral app shell |

### 3.3 Defining traits

- cobalt approximately `#002A8B`;
- warm cream approximately `#F8F0E2`;
- charcoal/black monoline art;
- irregular cream display wordmark;
- handwritten cream tagline;
- compact bold sans headings;
- small neutral sans body and metadata;
- mostly flat surfaces with negligible elevation;
- outlined capsules and rounded rectangles;
- realistic product photography only where purchase evaluation needs it;
- no decorative gradients inside the consumer UI.

### 3.4 Rejected labels

| Label | Reason |
|---|---|
| glassmorphism | no translucent blur or layered glass surfaces |
| neobrutalism | borders are thin and restrained; the composition lacks heavy raw blocks and deliberate anti-polish |
| skeuomorphism | drawings are identity assets, not material simulations or literal physical controls |
| bento UI | no modular dashboard grid |
| generic minimalism | visual density is low, but a strong mascot, custom lettering, and editorial copy dominate the experience |
| food-delivery marketplace UI | no multi-vendor discovery, map, promotion grid, or persistent cart shell is shown |

---

## 4. Screen analysis

## 4.1 `REF-03` — Branded landing screen

### Literal observation

`[O]` A full cobalt screen contains a large cream `COOL CAT'S` display wordmark, a cream monoline cat wearing sunglasses and carrying a drink while holding a surfboard, a handwritten tagline, and two outlined capsule buttons labeled `Bookings` and `Menu`.

### Canonical terms

| Visible element | Canonical term |
|---|---|
| full cobalt screen | full-bleed branded gateway |
| `COOL CAT'S` artwork | custom display wordmark asset |
| cat illustration | mascot hero illustration |
| handwritten phrase | brand tagline / handwritten microcopy |
| Bookings and Menu | dual-route action group |
| outlined rounded controls | outline capsule buttons |

### Interpretation

This is not a passive splash screen because it exposes two interactive destinations. Its correct role is a **branded gateway** or **brand-led home**. If the same screen appears before every session, it adds a mandatory layer before the repeat-use menu task.

### What works

- The brand identity is recognizable without photography or generic café motifs.
- One illustration, one phrase, and two actions create a clean reading order.
- The two actions communicate the product’s two visible service domains: reservations and ordering.
- Cream artwork against cobalt has strong visual contrast.

### Reconstruction issues

1. **Equal action hierarchy:** Bookings and Menu use the same size, outline, and weight. For a repeat-use ordering app, Menu is likely the primary route.
2. **Display text as artwork:** the wordmark should remain an asset; it should not replace the accessible product title.
3. **Brand-first delay:** a full-screen gateway is justified only if both routes are frequently used. Otherwise the main menu should open directly after onboarding, with booking available as a secondary action.
4. **No state feedback:** pressed, loading, unavailable, and reservation-closed states are absent.
5. **No standard shell:** status, account, cart, and order state are not visible. Do not assume they exist off-screen.

### Rebuild directive

```text
Use a full-bleed cobalt field. Keep the custom wordmark and mascot as decorative assets,
but expose “Cool Cat’s Café” as an accessibility label. Place the action group above the
bottom safe area. Use a filled Menu button and an outlined Bookings button when ordering
is the primary repeat-use job. Each button has a minimum 44-point hit region and visible
pressed, loading, and disabled states.
```

## 4.2 `REF-04` — Onboarding page

### Literal observation

`[O]` A warm-cream screen uses a large black monoline illustration of a cat riding a dog while reaching a coffee machine. A three-page indicator shows the first position. The title reads `Cool Cat's Club`, followed by one short value statement. `Skip` appears at lower leading and a cobalt `Next` button at lower trailing.

### Canonical terms

| Visible element | Canonical term |
|---|---|
| large scene drawing | onboarding hero illustration |
| line plus two dots | page indicator |
| `Cool Cat's Club` | onboarding heading |
| short explanation | value-proposition body copy |
| `Skip` | secondary dismissal action |
| `Next` | primary pagination action |
| implied three screens | paged onboarding flow |

### Interpretation

The reference is a static **value-proposition onboarding carousel**. It communicates brand tone and menu breadth, not an interactive tutorial.

### What works

- Skip is visible and does not force completion.
- The image and copy use one coherent voice.
- The page indicator communicates finite length.
- The bottom action arrangement leaves the illustration uninterrupted.

### Reconstruction issues

1. **Task learning is absent:** the first page teaches identity, not how to book, order, customize, or collect an order.
2. **Illustration dominates:** most of the viewport is decorative. Three pages of similar brand storytelling would delay utility.
3. **Indicator semantics:** line/dot differences need selected-page accessibility metadata and more than color alone.
4. **Next shape:** the compact cobalt control visually approaches a capsule but must retain a 44-point hit target.
5. **First-run boundary:** onboarding should not reappear on every launch.

### Rebuild directive

```text
Keep onboarding optional and at most three pages. Page one can establish the club;
later pages must explain an actual product job such as order customization or booking.
Persist completion locally. Provide Skip on every page, expose “Page 1 of 3,” support
Reduce Motion, and enter the menu or gateway immediately after completion.
```

## 4.3 `REF-05` — Menu discovery

### Literal observation

`[O]` A cream screen places a circular cat seal near the top. Four large outlined rounded rows—Recommended, Popular, Food, Beverages—contain a bold title and one line of playful supporting copy. A pale oversized cat-head watermark sits behind the lower area. A cobalt rounded banner labeled `Cool Cat's Curation` occupies the bottom.

### Canonical terms

| Visible element | Canonical term |
|---|---|
| circular cat mark | brand seal / compact logo lockup |
| four large rows | category navigation rows |
| Recommended | editorial recommendation collection |
| Popular | popularity-ranked collection |
| Food / Beverages | product-category taxonomy |
| pale cat head | decorative background watermark |
| bottom cobalt panel | branded promotional or customization CTA |
| `Cool Cat's Curation` | project-defined curated-service entry |

### What works

- The screen maintains brand personality without competing with real product imagery.
- Large rows are easy to scan and likely easy to tap.
- Each title is supplemented by a short description.
- The circular seal provides a compact alternative to the large landing wordmark.
- The watermark adds continuity at low visual weight.

### Reconstruction issues

1. **Mixed taxonomy:** editorial collections and product categories share one undifferentiated list.
2. **Missing destination context:** no search, cart, active order, account, or current pickup context is visible.
3. **Curation ambiguity:** the bottom panel reads like a promotion, but the action result is unclear.
4. **Contrast:** thin outlines and small supporting copy need contrast validation on the warm cream.
5. **Decoration collision:** the small cup/cat doodle overlaps the Beverages row edge and must not interfere with the tap target or text.
6. **Persistent CTA position:** the bottom curation panel may compete with the last category row on compact-height devices.
7. **No product evidence:** the menu landing contains no prices, products, availability, or recent/reorder shortcut.

### Rebuild directive

```text
Split the screen into two sections: Curated for you and Browse the menu. Use each row as
one full-width semantic button with a 64–72 point minimum row height. Keep the circular
seal compact. Treat the watermark as hidden decoration. Define the curation destination
explicitly—custom order, chef’s choice, or recommendation flow—and label the CTA with a
verb. Add search/cart/order context only after the production information architecture is
defined; do not invent it in a faithful reference build.
```

## 4.4 `REF-06` — Product detail and variant configuration

### Literal observation

`[O]` A cream product-detail screen contains a back arrow, favorite outline, title `Vietnamese Cold Coffee`, one paragraph, three size rows, volume and calorie metadata, price, Add/quantity controls, a large cold-coffee photograph, a customization note field, and a cobalt `Add to order - Rs. 850` action.

Visible examples:

| Variant | Volume / energy | Price | Control |
|---|---|---:|---|
| Small | 237 ml / 162 kcal | Rs. 200 | Add |
| Medium | 354 ml / 194 kcal | Rs. 250 | minus · 2 · plus |
| Large | 473 ml / 289 kcal | Rs. 350 | minus · 3 · plus |

### Canonical terms

| Visible element | Canonical term |
|---|---|
| back arrow | back-navigation button |
| heart outline | favorite toggle |
| title and description | product identity block |
| three rows | size/variant matrix |
| Add / minus-number-plus | inline quantity controls / steppers |
| drink photograph | product hero image |
| comment area | customization note field |
| blue bottom action | anchored add-to-order CTA |
| displayed total | calculated order-subtotal label |

### What works

- The product title, description, variants, image, note, and order action form a recognizable purchase sequence.
- Volume, calories, and price are available before quantity selection.
- The product photograph provides concrete purchase evidence after the sparse illustrated discovery screen.
- `Add to order` uses an explicit transactional verb.
- Back and favorite actions use familiar iconography.

### Reconstruction issues

1. **Quantity-total inconsistency:** Medium visibly shows `2` and Large visibly shows `3`, but `Rs. 850` does not equal `2×250 + 3×350`. The prototype values are not driven by one cart model.
2. **Multiple-size interpretation:** steppers on every row allow several sizes in one add operation. This can be valid for group ordering, but the interaction must explicitly state that multiple variants are being added.
3. **Tight matrix:** label, volume, calories, price, and stepper occupy narrow columns. Localization and large text will cause collisions.
4. **Low-contrast note field:** the placeholder and field surface are faint and the control does not clearly distinguish single-line from multiline input.
5. **Product image dominance:** the image creates appetite but consumes space that could support modifiers, allergens, availability, or cart context.
6. **Favorite state absent:** only the unselected outline is shown.
7. **Hard-coded formatting:** `Rs.`, `ml`, and `kcal` should use localized formatters and semantic labels.
8. **CTA state absent:** disabled, recalculating, adding, success, failure, and sold-out behavior is not shown.
9. **No modifier model:** milk, sweetness, ice, extras, and allergen information are absent. They should not be invented in a faithful rebuild but are production-scope questions.

### Rebuild directive

```text
Model Product, Variant, VariantQuantity, ModifierSelection, Note, and CartDraft as separate
state. Derive every row quantity and the CTA subtotal from CartDraft; no displayed value
may be independently hard-coded. Use adaptive rows that can stack metadata beneath the
variant name. Give back, favorite, minus, plus, and Add at least 44-point targets. Use a
TextEditor or clearly labeled note field, maintain CTA visibility with safe-area inset,
and announce subtotal changes accessibly.
```

## 4.5 `REF-07` — POS order-management context

### Literal observation

`[O]` The café counter image shows a desktop/tablet POS interface with a cobalt left navigation rail, an order queue in the middle, and an `Order #24` detail panel on the right. The selected destination is Orders. The detail panel contains status, table, guests, customer, payment, item lines, total, and a `Print Customer's Invoice` action.

### Canonical terms

| Visible element | Canonical term |
|---|---|
| cobalt left column | primary navigation rail |
| list of order cards | order queue / master list |
| selected order detail | detail inspector |
| queue + detail | master-detail split view |
| active/paid labels | order and payment status |
| item lines | order line-item table |
| invoice action | full-width primary action |

### Ecosystem implication

The POS concept assumes a structured order entity with order number, state, table, guest count, customer, payment method, line items, and total. The consumer mobile concept does not show cart review, checkout, fulfillment mode, confirmation, or status. A production system must define how a mobile `CartDraft` becomes the POS order object.

### Rebuild boundary

The POS should be documented as a separate staff product, not inserted into the consumer navigation. Shared tokens can include color, type, seal, and status language; information density, navigation, and interaction patterns remain role-specific.

---

## 5. Terminology normalization

| Informal description | Canonical term | Not this |
|---|---|---|
| 첫 파란 화면 | branded gateway / brand-led home | passive splash screen |
| 큰 고양이 그림 | mascot hero illustration | content image |
| 손글씨 문구 | handwritten brand tagline | body copy |
| Bookings·Menu 두 버튼 | dual-route action group | segmented control |
| 처음 설명 화면 | paged onboarding | feature tour tooltip |
| 페이지 점 | page indicator | progress bar |
| 메뉴 네 칸 | category navigation rows | filter chips |
| Recommended·Popular | merchandising collections | product categories |
| Food·Beverages | catalog taxonomy | recommendations |
| 아래 파란 덩어리 | branded promotional/customization CTA | tab bar |
| 상품 크기 세 줄 | size/variant matrix | comparison table only |
| `- 2 +` | inline quantity stepper | segmented control |
| 사진 아래 입력칸 | customization note field | search field |
| Add to order | anchored transactional CTA | navigation button |
| 하트 | favorite toggle | generic decoration |
| 매장 주문 화면 | master-detail POS order management | consumer checkout |
| 파란색+크림색 | high-contrast duotone brand shell | gradient palette |
| 얇은 둥근 테두리 | rounded-outline control language | neobrutalist border |

---

## 6. Layout and measurement model

### 6.1 Source calibration

The four extracted panels are exactly 433×940 px. Their aspect ratio closely resembles a compact iPhone portrait, but they are marketing panels inside an animation rather than native screenshots. Reconstruction should use proportional measurements and then calibrate to a 390×844 pt compact target.

| Parameter | Source observation | Proposed compact target |
|---|---:|---:|
| panel | 433×940 px | 390×844 pt |
| page inline inset | approximately 24–32 source px | 20–24 pt |
| top icon target | visible glyph approximately 18–24 px | 44×44 pt hit region |
| category row height | approximately 62–70 source px | 64–72 pt |
| row gap | approximately 18–24 source px | 16–20 pt |
| primary CTA height | approximately 48–56 source px | 48–52 pt |
| rounded-row radius | approximately 28–34 source px | 28–32 pt |
| onboarding bottom action region | final approximately 90 source px | safe-area inset + 44–48 pt controls |

### 6.2 Shared shell

- warm cream is the default commerce and onboarding canvas;
- cobalt is used for the gateway and primary actions;
- black/charcoal handles functional text and monoline art;
- page content is primarily one vertical stack;
- no persistent top bar is shown;
- shadow is reserved for the product photograph and external device/POS mockups, not ordinary controls;
- the reference uses unusually large empty fields to create brand calm.

### 6.3 Reading order

#### Landing

1. wordmark;
2. mascot;
3. tagline;
4. Bookings/Menu actions.

#### Onboarding

1. illustration;
2. page indicator;
3. heading;
4. body;
5. Skip/Next.

#### Menu

1. brand seal;
2. collection/category rows;
3. decorative watermark;
4. curation CTA.

#### Product

1. back/favorite;
2. product identity;
3. variant matrix;
4. product image;
5. note;
6. add-to-order total.

---

## 7. Element inventory

| ID | Ref | Canonical term | Hierarchy role | Evidence | Confidence |
|---|---|---|---|---|---:|
| `SUR-01` | 03 | full-bleed branded gateway | root surface | observed | 1.00 |
| `IMG-01` | 03 | custom display wordmark asset | primary brand identifier | observed | 1.00 |
| `IMG-02` | 03 | mascot hero illustration | brand focal object | observed | 1.00 |
| `TXT-01` | 03 | handwritten brand tagline | tone and proposition | observed | 1.00 |
| `GRP-01` | 03 | dual-route action group | primary routing | observed | 1.00 |
| `ACT-01` | 03 | outline capsule button | Bookings route | observed | 1.00 |
| `ACT-02` | 03 | outline capsule button | Menu route | observed | 1.00 |
| `SUR-02` | 04 | paged onboarding surface | first-run education | observed | 1.00 |
| `IMG-03` | 04 | onboarding hero illustration | visual explanation | observed | 1.00 |
| `NAV-01` | 04 | page indicator | pagination position | observed | 1.00 |
| `TXT-02` | 04 | onboarding heading | page identity | observed | 1.00 |
| `TXT-03` | 04 | onboarding body copy | value explanation | observed | 1.00 |
| `ACT-03` | 04 | Skip text button | dismiss onboarding | observed | 1.00 |
| `ACT-04` | 04 | Next primary button | advance page | observed | 1.00 |
| `SUR-03` | 05 | menu discovery landing | catalog entry surface | observed | 1.00 |
| `IMG-04` | 05 | circular brand seal | compact identity | observed | 1.00 |
| `GRP-02` | 05 | category navigation list | browse destinations | observed | 1.00 |
| `ROW-01` | 05 | editorial collection row | Recommended | observed | 1.00 |
| `ROW-02` | 05 | popularity collection row | Popular | observed | 1.00 |
| `ROW-03` | 05 | product-category row | Food | observed | 1.00 |
| `ROW-04` | 05 | product-category row | Beverages | observed | 1.00 |
| `DEC-01` | 05 | decorative watermark | low-priority brand texture | observed | 1.00 |
| `ACT-05` | 05 | branded curation CTA | custom-service entry | observed/inferred | 0.76 |
| `SUR-04` | 06 | product detail screen | product configuration | observed | 1.00 |
| `ACT-06` | 06 | back-navigation button | return | observed | 1.00 |
| `ACT-07` | 06 | favorite toggle | save preference | observed/inferred | 0.96 |
| `GRP-03` | 06 | product identity block | title and description | observed | 1.00 |
| `GRP-04` | 06 | size/variant matrix | variant configuration | observed | 1.00 |
| `ACT-08` | 06 | Add control | add one variant | observed | 1.00 |
| `ACT-09` | 06 | inline quantity stepper | adjust variant quantity | observed | 1.00 |
| `IMG-05` | 06 | product hero image | purchase evidence | observed | 1.00 |
| `ACT-10` | 06 | customization note field | freeform modifier note | observed/inferred | 0.96 |
| `ACT-11` | 06 | anchored add-to-order CTA | cart mutation | observed | 1.00 |
| `DAT-01` | 06 | calculated subtotal label | transaction feedback | observed/inferred | 0.94 |
| `SUR-05` | 07 | master-detail POS workspace | staff order management | observed | 1.00 |
| `NAV-02` | 07 | primary navigation rail | staff destination switching | observed | 1.00 |
| `GRP-05` | 07 | order queue | master collection | observed | 1.00 |
| `GRP-06` | 07 | order detail inspector | selected order | observed | 1.00 |
| `ACT-12` | 07 | invoice action | print customer invoice | observed | 1.00 |

---

## 8. Typography

### 8.1 Roles

| Role | Classification | Estimated compact target | Behavior |
|---|---|---:|---|
| wordmark | custom irregular display asset | asset-scaled | decorative; expose accessible name separately |
| handwritten tagline | custom handwriting/script | 16–18 pt | brand tone only; avoid for transactional copy |
| product/category heading | neutral geometric sans | 22–28 pt | bold/semibold |
| category title | neutral sans | 17–19 pt | bold |
| body description | neutral sans | 14–16 pt | regular, accessible line height |
| metadata | neutral sans | 12–14 pt | must remain legible on cream |
| button label | neutral sans | 15–17 pt | medium/semibold |
| price | neutral sans numeric | 15–17 pt | bold, tabular numerals preferred |

### 8.2 Type-system rule

Use three roles only:

1. custom display/wordmark;
2. handwritten brand accent;
3. neutral functional sans.

The handwritten face must not be used for price, quantity, status, validation, or accessibility-critical instructions.

### 8.3 Responsive text

- Category supporting copy may wrap to two lines.
- Variant metadata stacks beneath the size label at large text sizes.
- CTA subtotal may move to a secondary line.
- The product description remains native text and may expand.
- Wordmark and illustrations scale down before functional text does.
- Use locale-aware formatting for currency, volume, calories, and numerals.

---

## 9. Color and material

### 9.1 Sampled palette

| Token | Sampled/proposed value | Role |
|---|---|---|
| `color.brand.cobalt` | `#002A8B` sampled dominant | gateway, primary CTA, active quantity controls, seal |
| `color.brand.cream` | `#F8F0E2` sampled dominant | onboarding/menu/product canvas |
| `color.ink.primary` | approximately `#28292F` | functional headings and body |
| `color.ink.illustration` | near black | monoline art |
| `color.surface.input` | approximately `#E3D9C8` | customization field |
| `color.line.outline` | charcoal at reduced emphasis | category/button outlines |
| `color.backdrop.mockup` | approximately `#E1E2E6` | Behance animation backdrop only; not an app token |
| `color.text.onCobalt` | warm cream | wordmark, mascot, landing labels |
| `color.text.secondary` | calibrated neutral gray | descriptions and metadata |

### 9.2 Material behavior

- app surfaces are flat and opaque;
- no glass or blur is visible;
- outlines are thin and dark;
- cobalt CTAs are filled, cream controls are outlined;
- the product image may retain a natural cast shadow;
- decorative watermark opacity remains very low and noninteractive;
- device-frame shadows belong to the Behance presentation, not the reconstructed app.

### 9.3 Contrast priorities

- supporting copy inside category rows;
- customization placeholder;
- outline buttons over cobalt;
- disabled quantity controls;
- page indicator inactive dots;
- decorative illustration separated from controls.

---

## 10. Interaction and state model

### 10.1 Required state owners

```text
AppNavigation
- onboardingCompleted
- currentRoute
- bookingDraft

MenuCatalog
- collections
- categories
- availability
- search/filter state

ProductConfiguration
- product
- variants
- quantities
- modifiers
- note
- favorite state

CartDraft
- line items
- subtotal
- currency
- fulfillment mode
- validation state

Order
- identifier
- status
- payment
- customer
- fulfillment context
- line items
- total
```

### 10.2 Product-detail invariant

```text
displayedSubtotal ==
sum(variant.unitPrice * variant.quantity for every selected variant)
+ modifier adjustments
```

The CTA label, POS line items, and cart review must derive from the same state. Prototype placeholder values must never be copied into production logic.

### 10.3 Required states

#### Landing

- default;
- pressed Bookings/Menu;
- route loading;
- reservation unavailable;
- menu unavailable/offline.

#### Onboarding

- page 1/2/3;
- skipped;
- completed;
- Reduce Motion;
- restored after interruption.

#### Menu

- loading;
- populated;
- no available products;
- collection empty;
- offline cache;
- curation unavailable.

#### Product

- favorite off/on;
- variant available/sold out;
- quantity zero/positive/max;
- note empty/filled/invalid length;
- subtotal recalculating;
- add in progress/success/failure;
- product unavailable.

#### POS

- queue loading/empty;
- active/paid/completed/cancelled;
- selected order changed;
- invoice success/failure.

---

## 11. Accessibility

### 11.1 Required semantics

- Wordmark and mascot: grouped decorative assets with one accessible product name; do not expose every illustration stroke.
- Landing actions: `Book a table` and `Browse menu`, not ambiguous nouns alone where localization permits.
- Onboarding: announce heading, body, `Page 1 of 3`, Skip, Next.
- Category rows: one button each with title and description.
- Decorative watermark and edge doodles: hidden from accessibility.
- Favorite: toggle button with selected state.
- Variant matrix: each variant is one group containing size, volume, calories, price, quantity, and increment/decrement actions.
- Stepper changes and subtotal changes: announce politely.
- Note field: visible label; placeholder is not the only label.
- Add-to-order: include item count and subtotal where useful.
- POS queue: order status, number, time, payment, and selection state.

### 11.2 Target size

Every custom icon and action—Back, Favorite, Skip, Next, Add, Minus, Plus, category row, curation CTA—uses at least a 44×44 pt interaction region even where the visible glyph is smaller.

### 11.3 Color and shape redundancy

- onboarding page position has textual semantics;
- favorite state uses icon fill plus accessibility state;
- active stepper and selected variant cannot rely only on cobalt;
- sold-out state uses text and disabled semantics;
- POS status is not color-only.

### 11.4 Motion

The Behance carousel animation is presentation motion, not evidence of in-app transitions. Production motion should use standard navigation/paging behavior, honor Reduce Motion, and avoid replaying the full brand animation on repeat visits.

---

## 12. Brand-system continuity

### 12.1 Shared across consumer app, physical identity, and POS

- cobalt/cream palette;
- circular cat seal;
- monoline animal illustration;
- irregular display lettering;
- neutral bold sans for functional headings;
- rounded controls;
- playful but concise microcopy.

### 12.2 Must remain product-specific

| Consumer app | POS |
|---|---|
| low density, purchase imagery, large tap controls | high density, queue scanning, keyboard/pointer efficiency |
| local navigation | persistent navigation rail |
| product configuration | order state and fulfillment |
| optional brand storytelling | operational information priority |
| safe-area mobile CTA | wide split-view inspector |

Do not force the consumer app’s sparse illustration scale into the POS, and do not import POS density into the mobile menu.

---

## 13. Borrow / Exclude / Transform

### Borrow

- cobalt/cream duotone shell;
- black/cream monoline mascot system;
- custom display wordmark as a bounded asset;
- compact circular brand seal;
- sparse flat layout;
- category rows with title plus one-line description;
- realistic product photo only at product-decision points;
- cobalt primary CTA;
- brand voice embedded in secondary copy;
- cross-touchpoint token continuity from packaging to mobile and POS.

### Exclude

- mandatory brand gateway on every repeat visit;
- equal priority for Bookings and Menu without usage evidence;
- three onboarding pages that only repeat personality;
- mixed collection/category taxonomy;
- an ambiguous curation banner with no action verb;
- quantity and subtotal values maintained independently;
- note field labeled only by low-contrast placeholder;
- illustration overlap that reduces tap or text space;
- hard-coded currency/unit strings;
- absent cart/order context treated as already solved;
- device-frame shadow and gray Behance backdrop as app design tokens.

### Transform for Adelie Pages or other eiranotes products

Borrow the **system discipline**, not the café imagery:

- one strong background pair instead of many decorative colors;
- a custom illustration family with consistent stroke and humor;
- one brand display face plus one functional sans;
- illustrations concentrated in entry, empty, and celebration states;
- functional screens remain structurally plain;
- promotional copy is separated from taxonomy;
- product-state calculations remain deterministic and testable.

For Adelie Pages specifically, this reference is useful for pack identity, illustration-led empty states, and a two-color specimen campaign. It is not a model for editor controls, Library hierarchy, or persistent commerce navigation.

---

## 14. Reconstruction specification

### 14.1 Compact frame

```text
TARGET
- 390×844 pt compact iPhone baseline.
- 20–24 pt inline content inset.
- Minimum 44×44 pt controls.
- Primary CTA height 48–52 pt.
- Category row height 64–72 pt.
- 16–20 pt inter-row spacing.
- Warm cream root with cobalt actions.

LANDING
- Full cobalt.
- Wordmark asset near upper third.
- Mascot centered.
- Tagline subordinate.
- Filled Menu + outlined Bookings for repeat-use hierarchy.
- Actions above bottom safe area.

ONBOARDING
- Optional, at most three pages.
- Illustration consumes no more than about 55% of usable height.
- Page indicator has accessible current-page state.
- Skip and Next remain visible without scroll.
- Final action uses a task verb such as Browse menu.

MENU
- Compact seal.
- “Curated for you” section for Recommended/Popular.
- “Browse the menu” section for Food/Beverages.
- Full-row buttons; decoration cannot enter text/hit regions.
- Curation CTA receives an explicit verb and destination.

PRODUCT DETAIL
- Back and Favorite in 44 pt targets.
- Title/description first.
- Adaptive variant list.
- One cart-owned quantity model.
- Product image constrained beneath configuration.
- Labeled note field.
- Safe-area anchored Add to order CTA with derived subtotal.

POS
- Separate desktop/tablet product.
- Navigation rail + order queue + detail inspector.
- Keyboard/pointer support.
- Shared brand tokens only.
```

### 14.2 SwiftUI mapping

| Reference element | Component | Native/custom | Notes |
|---|---|---|---|
| landing route actions | `Button` in `HStack`/adaptive stack | hybrid | custom border/fill, native semantics |
| onboarding | paged `ScrollView` or `TabView(.page)` | native/hybrid | custom indicator if brand-specific |
| category rows | `NavigationLink` / `Button` in `LazyVStack` | hybrid | complete row is target |
| curation entry | `NavigationLink` or `Button` | hybrid | explicit destination required |
| product detail | `ScrollView` + `safeAreaInset` CTA | native | preserve CTA and content scroll |
| favorite | toggle `Button` | hybrid | selected trait and state |
| quantity | `Stepper` semantics or custom decrement/increment group | hybrid | 44 pt targets |
| note | labeled `TextField`/`TextEditor` | native | placeholder not sole label |
| cart | observable state/store | custom data layer | sole subtotal authority |
| POS | separate responsive web/desktop shell | separate product | do not reuse mobile navigation |

### 14.3 Proposed tokens

| Token | Value |
|---|---|
| `color.brand.cobalt` | `#002A8B` |
| `color.brand.cream` | `#F8F0E2` |
| `color.ink.primary` | `#28292F` proposed |
| `color.surface.input` | `#E3D9C8` proposed |
| `color.text.onBrand` | `#F8F0E2` |
| `space.page.inline` | `22pt` |
| `space.stack.row` | `18pt` |
| `size.control.minimum` | `44pt` |
| `size.cta.height` | `50pt` |
| `size.category.minimumHeight` | `68pt` |
| `radius.control.capsule` | `999pt` |
| `radius.category` | `30pt` |
| `stroke.control.outline` | `1pt` |
| `type.heading.product` | `26pt semibold` |
| `type.heading.category` | `18pt bold` |
| `type.body` | `15pt regular` |
| `type.metadata` | `13pt regular` |
| `type.button` | `16pt medium` |

---

## 15. Explicit prohibitions

- Do not label the interactive landing screen as a splash screen.
- Do not add a persistent tab bar to a faithful reconstruction.
- Do not mix Recommended/Popular with Food/Beverages without section labels.
- Do not treat the circular brand seal as a profile avatar.
- Do not implement the curation banner without a defined action and destination.
- Do not bake category names, product names, price, quantity, calories, or CTA totals into images.
- Do not independently store visible subtotal and variant quantities.
- Do not reduce Back/Favorite/Stepper hit areas to their glyph bounds.
- Do not use handwritten typography for prices, error messages, or order state.
- Do not copy the Behance gray backdrop, device bezels, or mockup shadows into the app.
- Do not infer checkout, loyalty, or order-tracking screens as observed.
- Do not use glass, gradients, generic food-app orange/red, or card-dashboard patterns.
- Do not force consumer-mobile density into the POS.
- Preserve the cobalt/cream shell, monoline mascot, sparse hierarchy, outlined rows, and product-image discipline.

---

## 16. QA and acceptance gate

### 16.1 Visual QA

| Check | Target | Method |
|---|---|---|
| mobile-screen coverage | 4/4 distinct public screens analyzed and implemented | reference inventory |
| palette | cobalt and cream remain within calibrated tolerance | sampled screenshot comparison |
| landing reading order | wordmark → mascot → tagline → actions | thumbnail/squint test |
| category structure | curated collections visibly separated from product categories | screenshot review |
| control targets | every custom action at least 44×44 pt | hit-region overlay |
| product subtotal | exact derivation from selected quantities/modifiers | deterministic unit/UI tests |
| variant reflow | no clipping at accessibility text sizes | Dynamic Type matrix |
| note field | visible label and adequate contrast | accessibility inspection |
| CTA | remains visible without covering content | compact-height screenshots |
| favorite | clear selected/unselected state | state screenshot |
| POS boundary | no mobile-only navigation imported | design-system review |
| Reduce Motion | onboarding/navigation remains usable | system setting test |

### 16.2 Data invariants

```text
subtotal == sum(line.quantity * line.unitPrice) + modifierAdjustments
quantity >= 0
soldOutVariant.quantity == 0
CTA is enabled only when at least one valid line item exists
displayed currency == cart currency
POS order line items == submitted consumer cart line items
```

### 16.3 Acceptance statement

```text
PASS when:
- The four public mobile screens retain their brand identity and become one coherent,
  deterministic ordering flow.
- Menu collections and catalog categories are distinguishable.
- Product quantity and subtotal never disagree.
- All custom controls pass target-size, contrast, and large-text checks.
- Brand assets are decorative where appropriate and do not replace semantic text.

HOLD when:
- The destination of Cool Cat’s Curation is unresolved.
- Multiple simultaneous size quantities are not a confirmed requirement.
- Booking, cart, checkout, and fulfillment models remain undefined for production scope.

FAIL when:
- The build invents a generic delivery-app shell, adds unsupported persistent navigation,
  reproduces the numeric inconsistency, or turns brand artwork into inaccessible text.
```

---

## 17. Uncertainty register

| ID | Question | Status | Evidence needed | Blocks rebuild |
|---|---|---|---|---|
| `U-01` | Is the landing shown every launch or only after onboarding? | unknown | prototype flow or design file | no |
| `U-02` | What are onboarding pages 2 and 3? | unknown | full prototype | no |
| `U-03` | Is Menu or Bookings the primary repeat-use route? | inferred | usage goal or product brief | no |
| `U-04` | What does Cool Cat's Curation do? | unknown | destination screen or interaction spec | yes for that feature |
| `U-05` | Are Recommended and Popular dynamic/personalized collections? | unknown | catalog model | no |
| `U-06` | Can one add multiple sizes of the same product in one operation? | inferred | cart requirements | yes |
| `U-07` | Why do Medium and Large show 2 and 3 while the CTA total is Rs. 850? | unknown | source prototype/data binding | yes for faithful data behavior |
| `U-08` | Is the note single-line or multiline and how is it validated? | unknown | interaction spec | no |
| `U-09` | What is the intended currency locale and tax model? | unknown | product/market requirements | yes for production commerce |
| `U-10` | How does the consumer cart become a POS order? | unknown | order API/domain contract | yes for ecosystem implementation |
| `U-11` | Exact font and text-style mapping | unknown | source/design file | no |
| `U-12` | Dark mode and accessibility behavior | unknown | alternate references/prototype | no |

---

## 18. Source register

| ID | Authority | Source | Section |
|---|---|---|---|
| `SRC-01` | `PROJECT_DEFINED` | Behance — Cool Cat's project page | project description, ownership, scope, date |
| `SRC-02` | `PROJECT_DEFINED` | Behance app GIF module | complete public mobile screen animation |
| `SRC-03` | `PROJECT_DEFINED` | Behance POS image module | staff order-management context |
| `SRC-04` | `PLATFORM_OFFICIAL` | Apple Human Interface Guidelines — Onboarding | optional, concise first-run education |
| `SRC-05` | `PLATFORM_OFFICIAL` | Apple Human Interface Guidelines — Buttons | button semantics, labels, target size |
| `SRC-06` | `PLATFORM_OFFICIAL` | Apple Human Interface Guidelines — Navigation and search | task navigation and search behavior |
| `SRC-07` | `STANDARD_NORMATIVE` | WCAG 2.2 | target size, focus visibility, non-color communication |

---

## 19. Final build brief

```text
STYLE
Playful Monoline Café Commerce.

SURFACES
Optional onboarding, branded gateway, menu discovery, product detail. POS is a separate
staff surface and shared only as ecosystem context.

PALETTE
Cobalt #002A8B, cream #F8F0E2, charcoal functional text, black monoline art.

TYPE
Custom display wordmark asset + handwritten brand accent + neutral functional sans.

LANDING
Full cobalt. One mascot hero. Menu receives the primary hierarchy for repeat ordering;
Bookings remains secondary unless product evidence says otherwise.

ONBOARDING
Optional, finite, no more than three pages. Every page explains a real job or value.
Skip is always available.

MENU
Separate curated collections from Food/Beverages taxonomy. Use full-row navigation
buttons and keep decoration outside interaction/text bounds. Define the Curation action.

PRODUCT
Adaptive variant list, 44-point steppers, labeled note field, product image, favorite
toggle, safe-area CTA. CartDraft is the only authority for quantity and subtotal.

ACCESSIBILITY
Native text, accessible wordmark label, decorative illustration hidden, page count
announced, non-color states, Dynamic Type reflow, Reduce Motion, 44-point controls.

EXCLUDE
Generic delivery marketplace styling, tab bar not shown in reference, mixed taxonomy,
hard-coded totals, mockup chrome, glass, gradients, and invented missing screens.

QA
Four-screen reference coverage complete; subtotal invariant exact; no clipping or
occlusion; brand and commerce layers remain distinguishable.
```

## Revision history

| Revision | Date | Change |
|---|---:|---|
| 1 | 2026-08-17 | Initial complete analysis of all four public mobile screens and POS ecosystem context |
