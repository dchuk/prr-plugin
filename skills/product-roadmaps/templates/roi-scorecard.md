---
type: roi-scorecard
managed_by: prr                     # Required. Identifies this file to the prr plugin's validator hook.
scored_on: YYYY-MM-DD
scored_by: <author>
formula: "(Value / Effort) × Confidence"
strategic_goals: [OBJ-1, OBJ-2]     # Objectives used as Value columns
customer_needs:                     # Customer needs used as Value columns
  - {id: CN-1, name: <customer need>}
  - {id: CN-2, name: <customer need>}
items_scored: [TH-001, TH-002]      # Theme IDs (or free-text items if pre-theme)
---

# ROI Scorecard — YYYY-MM-DD

## Inputs

- **Strategic goals:** OBJ-1 <name>, OBJ-2 <name>
- **Customer needs:** CN-1 <name>, CN-2 <name>
- **Items scored:** <list of themes/features/initiatives>
- **Formula:** (Value / Effort) × Confidence

## Scores

Each row scores an item against every customer need (CN-*) and strategic goal (OBJ-*) on a 0–3 scale, sums to **Value**, then divides by **Effort** (1–5 or T-shirt) and multiplies by **Confidence** (0.0–1.0) to produce **Priority**. Ranked descending.

| Item | CN-1 | CN-2 | OBJ-1 | OBJ-2 | Value | Effort (T-shirt) | Effort (#) | Confidence | Priority | Notes |
|------|------|------|-------|-------|-------|------------------|------------|------------|----------|-------|
| TH-001 <name> | 3 | 2 | 3 | 1 | 9 | M | 3 | 0.75 | 2.25 | <dependency / risk> |
| TH-002 <name> | 2 | 3 | 2 | 2 | 9 | L | 4 | 0.60 | 1.35 | <note> |

## Summary

- **Top 3:** <ranked list with one-line rationale per item>
- **Low-confidence flags:** <items where confidence < 0.5 — call out for de-risking>
- **Dependencies:** <prerequisite items, sequencing constraints>
- **Cut line:** <items below the cut that will not be pursued this cycle>

## Anti-patterns avoided

- Not scored by gut, HiPPO, popularity, or competitor-parity — every score has a rationale column.
- Effort column present — omitting effort is a named bad-prioritization anti-pattern.
- Confidence captured separately — no item inflated to 100%.
