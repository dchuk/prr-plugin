# Prioritization Frameworks

Without disciplined prioritization, product teams drift toward **Shiny Object Syndrome** — chasing parallel initiatives until every initiative takes twice as long and nothing important ships. The underlying force is opportunity cost: when resources are finite and strategies shift, failing to do the most important thing *now* means you may never get the chance. Add the exponential regression-testing burden (2^n – 1 test combinations for n features — 1,023 for 10 features, 2,047 for 11) and the compounding carrying costs of every feature added (documentation, support, sales training, marketing positioning) and unfocused prioritization is not just slow — it is actively destructive.

The book presents five frameworks for cutting through that noise: Critical Path, Kano Model, Desirability / Feasibility / Viability, ROI Scorecard, and MoSCoW. None replaces judgment; all of them sharpen it.

---

## Why Prioritization Is Crucial

Two principles anchor the whole chapter:

> Always assume you may have to stop work at any time. Most projects are in constant competition with other ideas and are always at risk of cancellation or downsizing.

> Prioritize by doing the most leveraged things first — those that have the most bang for the least buck. Value/Effort = Priority.

The implication is direct: sequence the most important things first so value is demonstrated before resources are redirected. This is not a planning nicety — it is a hedge against organizational reality.

---

## Framework 1 — Critical Path

**What it is.** Critical Path identifies the single set of pain points so fundamental to the customer journey that the product *must* address them or users will not adopt the solution. Linking these key moments together gives a blueprint for an MVP.

**How to apply it.** Walk the user journey step by step. Mark every moment where a gap or friction point would cause the customer to abandon the product entirely. Those are your critical path items. Everything else is a candidate for the next planning horizon.

**For existing products.** The critical path changes as user behaviors evolve. Direct customer contact — face-to-face if possible — is required to anticipate new critical path needs, because data alone cannot replace staying in touch with users.

### When to use / When NOT to use — Critical Path

| Use | Avoid |
|-----|-------|
| Designing an MVP | You need to account for effort, risk, or business goals |
| Making a major expansion in product scope | You need to rank needs more finely than "critical" vs. "noncritical" |
| Identifying the one thing that will drive a customer to buy | — |

---

## Framework 2 — Kano Model

**What it is.** Developed by Dr. Noriaki Kano, the model classifies customer expectations into three categories:

- **Expected needs** — dissatisfiers if missing (customers take them for granted)
- **Normal needs** — satisfiers; more of them = more satisfaction
- **Exciting needs** — delighters/wows; their absence doesn't disappoint, but their presence creates disproportionate enthusiasm

**How to apply it.** Survey customers on each candidate need using paired questions: "How would you feel if this feature were present?" and "How would you feel if it were absent?" Map responses to the three categories. Expected needs must ship; normal needs are your core improvement levers; exciting needs are differentiation opportunities.

### When to use / When NOT to use — Kano

| Use | Avoid |
|-----|-------|
| Identifying possible add-ons or enhancements | You need to account for effort, risk, or business goals |
| Prioritizing among customer needs by customer perception of value | You don't know your customer well enough to accurately judge their perception |
| You have covered critical path needs and are deciding among ideas of increasing value | — |

---

## Framework 3 — Desirability / Feasibility / Viability

**What it is.** Each idea is scored on three axes, each on a 1–3 scale:

- **Desirability** — customer value
- **Feasibility** — ease/cost of delivery (higher score = easier)
- **Viability** — business value, often revenue/profit

Scores are summed to produce a composite priority score. The deliberate 1–3 scale is an instance of **deliberate imprecision** — keeping discussions focused on relative order, not precise forecasts. Teams align on high/medium/low faster than on exact dollar amounts.

### When to use / When NOT to use — Desirability / Feasibility / Viability

| Use | Avoid |
|-----|-------|
| Prioritizing among a small set of initiatives or solutions | You need clearly defined categories for customer needs, org goals, or effort types |
| Identifying opportunities that meet all key success criteria | You have a long feature list where finer ROI distinctions matter |

---

## Framework 4 — ROI Scorecard

**What it is.** A prioritization spreadsheet applying the formula:

```
Value / Effort = Priority
```

Value combines customer needs and organizational goals, scored per line item. Effort uses T-shirt sizing (XS/S/M/L/XL scored 1–5). A confidence multiplier discounts the result for risk and unknowns.

**Key rules:**
- **Compare like things.** Do not rank a theme against a feature intended to fit within that or another theme. (`ch10.rule.compare-like-things`)
- **Use zero for no effect.** Assign 0 — not just "low" — when an idea helps not at all on a given goal. Reserve negative scores for inherent trade-offs that *actively harm* a goal (e.g., discounting increases unit sales but hurts profit margin).
- **Apply a confidence multiplier.** Multiply the Value/Effort result by a confidence percentage to discount for risk and unknowns.
- **Note dependencies separately.** Dependencies, resource constraints, and pre-existing promises go in margin annotations on the scorecard — they affect scheduling, not the underlying priorities.

**Value must reflect strategy, not just revenue.** Pre-revenue products, unprofitable customers, market-share mandates, and renewal vs. new revenue all require different value definitions rooted in strategy, not revenue projections alone.

**Include effort cross-functionally.** Effort estimates must account for the whole company — marketing, sales, support, partnerships — not just engineering time. A shiny new feature has no value if the company can't market, sell, or service it.

**Keep it simple.** Models with a dozen goals and complex weighting schemes are harder to use without adding decision-making utility. Simplicity drives adoption and alignment.

### Minimal ROI Scorecard (illustrative structure)

```
Theme / Feature | Customer Value (0–2) | Strategic Goal A (0–2) | Strategic Goal B (0–2) | Total Value | Effort (T-shirt 1–5) | Confidence % | Priority (Value/Effort × Confidence)
----------------|----------------------|------------------------|------------------------|-------------|----------------------|--------------|-------------------------------------
Theme X         |          2           |           1            |           0            |      3      |          3 (M)       |     80%      |  0.80
Theme Y         |          1           |           2            |           2            |      5      |          5 (XL)      |     60%      |  0.60
Feature Z       |          2           |           1            |           1            |      4      |          1 (XS)      |     90%      |  3.60
```

Note: Feature Z should only appear in this scorecard if it is being compared at the same level of abstraction as the other rows — not as a sub-item of Theme X or Y.

### When to use / When NOT to use — ROI Scorecard

| Use | Avoid |
|-----|-------|
| Weighing multiple factors simultaneously | Your team has not yet aligned on the components of value and effort (requires up-front alignment) |
| Working with a long list of possible initiatives, problems, features, or solutions | — |
| Many proposed items score equally on simpler frameworks and you need finer distinctions | — |

---

## Framework 5 — MoSCoW

**What it is.** A method for categorizing a *already-prioritized* list of requirements into four buckets:

- **Must have** — non-negotiable; product fails without these
- **Should have** — important but not vital
- **Could have** — nice to have if effort allows
- **Won't have** — explicitly out of scope for this release

**Critical constraint:** MoSCoW is a *communication tool*, not a prioritization method. It communicates the output of prioritization clearly to development teams and prevents scope creep by making the Won't-have boundary explicit and agreed upon.

**Rule:** Won't-have items must not contain dissatisfiers or critical path items. If a critical path need lands in Won't-have, either the scope definition is wrong or the release is being scoped too narrowly.

### When to use / When NOT to use — MoSCoW

| Use | Avoid |
|-----|-------|
| You feel uncertain about what must be included in a release | You need to set priorities in the first place |
| Communicating launch criteria clearly to the development team | — |
| Preventing scope creep by agreeing on out-of-scope items up front | — |

---

## Frameworks Are Aids, Not Decisions

> Prioritization frameworks should be used as an aid to decision-making, not as the decision itself. No one should be a slave to a formula. Numerical models have real limitations — they miss intangibles, dependencies, and promises — and must be complemented with judgment.

Use the scorecard to create a first-pass ranking. Then apply judgment: are there dependencies the model doesn't capture? Pre-existing customer promises? Regulatory deadlines? Those belong in margin annotations, referenced when you sequence the roadmap — they affect scheduling, not the underlying priorities.

---

## When to Use / When NOT to Use (Summary)

**Use a prioritization framework when:**
- You have more candidate themes or features than capacity — almost always.
- Stakeholders are advocating for different priorities without a shared scoring basis.
- You are defining an MVP or scoping a major release.
- Your team keeps changing its mind about what is most important.

**Do not rely on frameworks alone when:**
- Dependencies, regulatory constraints, or contractual commitments override scoring — annotate and address those separately.
- The team has not aligned on what "value" means for your current strategic stage; resolve strategy first (see [vision, strategy, and OKRs](../core/vision-strategy-okrs.md)).
- You are using MoSCoW as a substitute for having done the prioritization work — it communicates output, it does not create it.

---

## Code Examples

### T-shirt Sizing Scale

```
XS = 1   (hours to days)
S  = 2   (days)
M  = 3   (1–2 weeks)
L  = 4   (weeks to a month)
XL = 5   (months)
```

The absolute duration attached to each label is less important than the *relative* ordering. What matters is that S is smaller than M, not the exact calendar duration.

### Exponential Test Matrix Formula

```
Test combinations = 2^n – 1

n = 10 features → 1,023 combinations
n = 11 features → 2,047 combinations
n = 20 features → 1,048,575 combinations
```

Use this when making the case internally for saying no to low-priority features: each addition more than doubles the regression burden.

### ROI Scorecard Priority Formula

```
Priority = (Value / Effort) × Confidence

Where:
  Value      = sum of scores across customer-need and strategic-goal columns
  Effort     = T-shirt size score (1–5; lower = less effort)
  Confidence = percentage (0.0–1.0) reflecting certainty in estimates
```

---

## Related References

- [Themes and needs](../core/themes-and-needs.md) — how to define the themes and customer needs that become the inputs to these frameworks
- [Bad prioritization anti-patterns](../anti-patterns/bad-prioritization.md) — the seven common methods (gut instinct, analyst opinion, popularity, sales requests, support requests, competitive me-too, omitting effort) that these frameworks replace
- [Roadmap components](../core/roadmap-components.md) — how prioritized themes map to the primary components of a roadmap
- [Vision, strategy, and OKRs](../core/vision-strategy-okrs.md) — establishing the strategic goals that define "value" in the ROI Scorecard
- [Build ROI Scorecard command](../../../../commands/build-roi-scorecard.md) — step-by-step command for running a scorecard session with your team
- [Transform features to themes command](../../../../commands/transform-features-to-themes.md) — convert a raw feature list into the outcome-oriented themes that these frameworks can actually evaluate
