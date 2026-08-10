---
schema_version: "1.0.0"
audit_id: "RPA-YYYYMMDD-NNN"
status: "draft"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
repository: "owner/name"
canonical_ref: "main"
artifact_type: "repository_product_audit"
---

# Repository Product Audit

## 0. Identity and scope

| Field | Value |
|---|---|
| Repository |  |
| Product name |  |
| Product type |  |
| Canonical repository | yes / no / unknown |
| Canonical branch |  |
| Open feature PRs |  |
| Audit depth | repository docs / source slices / build / runtime / device |
| Out of scope |  |

## 1. Evidence register

| Evidence ID | Type | Ref/path | Date | What it proves | Limit |
|---|---|---|---|---|---|
| E-01 | README |  |  | product definition |  |
| E-02 | status |  |  | current implementation |  |
| E-03 | commit |  |  | latest verified change |  |
| E-04 | PR |  |  | branch-only direction | not on main |

Evidence labels:

- `[O]` observed in source or screenshot
- `[D]` documented by repository
- `[V]` verified build/test/runtime evidence
- `[I]` inferred
- `[U]` unknown

## 2. Product job

One sentence describing what the user accomplishes.

## 3. Core loop

```text
trigger → user action → state change → output/reward → reason to return
```

## 4. Current implementation

### Main

- 

### Open PR / branch-only

- 

### External gates

- 

## 5. Return cadence

| Cadence | Trigger | Stored state | Return surface |
|---|---|---|---|
| session / daily / weekly / episodic |  |  |  |

## 6. Monetization boundary

- Free:
- Paid:
- Store/provider state:
- Purchase value:
- External setup:

## 7. Product-loop assessment

### Closed

- 

### Open

- 

### Main bottleneck

State one primary bottleneck: code, external platform, content/art, operations/data, or repository topology.

## 8. UX and information architecture

- Primary surface:
- Navigation:
- First-use path:
- Empty/loading/error/recovery:
- Accessibility:
- Visual-system consistency:

## 9. Technical architecture

- State owner:
- Persistence:
- Extension/provider boundaries:
- Failure model:
- Performance budget:
- Test evidence:

## 10. Overlap and canonical boundary

- Adjacent repositories:
- Shared infrastructure:
- Must remain product-specific:
- Duplicate or legacy repositories:

## 11. Next action

One bounded implementation or validation step. Do not list a broad roadmap here.

## 12. Acceptance gate

```text
PASS when:
- 

HOLD when:
- 

FAIL when:
- 
```

## 13. Unknowns

| ID | Question | Evidence needed | Blocks next action |
|---|---|---|---|
| U-01 |  |  | yes/no |
