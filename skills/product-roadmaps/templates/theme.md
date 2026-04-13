---
type: theme
managed_by: prr                     # Required. Identifies this file to the prr plugin's validator hook.
id: TH-001
name: "Ensure <result> for <stakeholder>"
timeframe: Now                      # Now | Next | Later  (NEVER a calendar date)
customer_need: <the underlying problem — not a solution>
linked_objectives: [OBJ-1]          # Must be non-empty. A theme with no objective is an "Orphaned Theme" anti-pattern.
confidence: 75                      # Integer 0–99. Never 100 — the future is uncertain.
stage: discovery                    # discovery | design | prototyping | alpha | beta | shipping | null
target_customers: []                # e.g. [mobile-shopper, enterprise-admin]
product_areas: []                   # e.g. [checkout-ui, platform, api, admin]
source: customer-research           # customer-research | support | usage-data | sales-pattern
roi_score:                          # Optional. Populated by /prr:build-roi-scorecard.
  value: null                       # 1–10 (sum of customer-need + objective scores)
  effort: null                      # T-shirt (XS/S/M/L/XL) or 1–5
  confidence: null                  # 0.0–1.0 (decimal)
  priority_score: null              # (value / effort) × confidence
  scored_on: null
created_on: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# <Theme name — "Ensure <result> for <stakeholder>">

## Customer need

<State the underlying problem in plain language. Who feels it, when, and why it matters. Avoid solution language — no feature names, no UI components.>

## Evidence

> **Job story:** When <situation>, I need <desire>, so I can <result>.
> **User story:** As <user type>, I want <desire>, so I can <result>.

<Supporting data: customer quotes, support ticket volume, usage analytics, journey-map friction points.>

## Subthemes

Only populate when this theme is in **Now**, or when stakeholders need concrete detail. Mark each as:

- **Probable solution** — evident but unvalidated direction.
- **Infrastructure solution** — engineering-vetted prerequisite.
- **Carryover** — validated work from a prior roadmap cycle.

## Trade-offs considered

<Optional. Iron-triangle notes (schedule / scope / budget / quality), alternatives ruled out, dependencies on other themes.>

## Change log

- YYYY-MM-DD — Created in <timeframe>.
