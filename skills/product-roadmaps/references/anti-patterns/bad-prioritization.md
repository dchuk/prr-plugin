# Bad Prioritization Methods

Prioritization is where product strategy becomes real — or falls apart. Teams that skip disciplined prioritization don't simply delay value; they accumulate hidden carrying costs, fragment organizational focus, and risk never completing their most important work before resources are redirected. The book's unifying rule: **do not outsource strategy** to customers, analysts, salespeople, or competitors. Each of the seven anti-patterns below is a specific way that rule gets broken.

## The Unifying Principle: Do Not Outsource Strategy

> _"Do not let others — customers, analysts, salespeople, or competitors — define your product strategy."_ _source: ch10 §Bad (but Common) Ways to Prioritize_

This rule applies whenever you are gathering stakeholder input on priorities. The one stated exception: companies that serve only the largest enterprise customers may legitimately have their roadmap largely determined by a small number of those customers — but even then, that is a conscious strategic choice, not drift.

The companion principle is focus:

> _"Focus — as an organization on one set of problems for a strategic set of target customers — is the antidote to shiny object syndrome."_ _source: ch10 §Shiny Object Syndrome_

Every anti-pattern below represents a failure of focus. Identifying which failure is happening in your organization is the first step to fixing it.

---

## The Seven Bad Prioritization Methods

### 1. Gut Instinct Prioritization

**What it looks like.** An executive announces a new #1 priority without analysis. The priority list changes daily or weekly. There is no written rationale for the order of work.

**Why it fails.** Prioritizing solely on gut instinct results in high team turnover, low productivity, and subpar results because the executive changes their mind frequently and is no longer in touch with the market. _source: ch10 §Bad (but Common) Ways to Prioritize_

**What to do instead.** Take executive gut opinion as input. Apply rigor by understanding the underlying problem, checking strategic alignment, and evaluating the proposed solution against alternatives before politely explaining why other items rank higher.

---

### 2. Analyst Opinion Prioritization

**What it looks like.** Roadmap items are justified solely by analyst reports. The team defers to external forecasts over internal market data.

**Why it fails.** Analysts often make straight-line extrapolations from existing trends that fail to account for disruptions — illustrated by the flat-panel monitor price prediction failure in the early 2000s. _source: ch10 §Bad (but Common) Ways to Prioritize_

**What to do instead.** Do your own primary research and analysis. Use analyst reports as one data point, not the deciding input.

---

### 3. Popularity-Based Prioritization

**What it looks like.** Feature requests sorted by vote count drive the roadmap. The product has many features but unclear positioning. Usability issues increase as feature count grows.

**Why it fails.** Ranking feature requests by frequency or size of customer outsources product strategy to customers who often cannot articulate what they need, resulting in a product with no focus, unclear market positioning, and poor usability. _source: ch10 §Bad (but Common) Ways to Prioritize_

**What to do instead.** Understand the underlying problems that motivated customer requests, then develop a more elegant set of solutions that address root needs rather than literally fulfilling each request.

---

### 4. Sales Request Prioritization

**What it looks like.** The roadmap changes each quarter based on the sales pipeline. Features are built for one customer that no one else needs.

**Why it fails.** Prioritizing based on what will help close deals this quarter is short-term thinking that may help make the numbers once or twice but does not serve a market. _source: ch10 §Bad (but Common) Ways to Prioritize_

**What to do instead.** Use sales team input to understand buyer thinking, but evaluate requests against whether they serve the target market broadly — not just the accounts in the current pipeline.

> **Note on special requests.** When a sales team brings a one-off request during a deal cycle, the [evaluate-special-request command](../../../../commands/evaluate-special-request.md) provides a structured three-question evaluation to apply before agreeing to any roadmap change.

---

### 5. Support Request Prioritization

**What it looks like.** The roadmap is dominated by support-ticket themes while acquisition stalls. The enhancement list is driven by rep-time-spent reports alone.

**Why it fails.** Prioritizing only on common support complaints is useful when usability is a key goal, but problematic when the product is missing critical functionality that prevents prospects from buying in the first place — feedback from current customers doesn't help expand appeal to prospects. _source: ch10 §Bad (but Common) Ways to Prioritize_

**What to do instead.** Weigh usability improvements in the context of all your goals. Prioritize support-driven work only when usability is genuinely among your top strategic objectives.

---

### 6. Competitive Me-Too Feature Prioritization

**What it looks like.** Feature priorities are set by competitive matrix gaps. Roadmap language sounds like "competitor X has this, we need it too." Price pressure is increasing as feature parity grows.

**Why it fails.** A tit-for-tat feature war with competitors creates a commodity market where the longest feature list and lowest price win, destroying profit margins. _source: ch10 §Bad (but Common) Ways to Prioritize_

**What to do instead.** Differentiate with capabilities perfectly matched to your chosen customer's needs that competitors can't or won't match, enabling value-based pricing.

---

### 7. Omitting Effort from the Priority Scorecard

**What it looks like.** The scorecard has only value columns with no effort column. High-value, long-effort items consistently block quick wins from ever getting done.

**Why it fails.** Some product managers develop scorecards that score only business value, arguing that estimates are someone else's responsibility. This misses obvious ROI wins where a lower-value feature takes a fraction of the effort. _source: ch10 §The effort side of the equation_

**What to do instead.** Always include effort (using T-shirt sizing if necessary) in the prioritization formula: **Value / Effort = Priority**. _source: ch10 §ROI Scorecard_

---

## The Effort Side: A Closer Look

Omitting effort is worth expanding because it is the most mechanical fix. The book is explicit:

> _"Product prioritization must include the effort side of the equation, not just business value. A feature that delivers equal value in two days should be done before one that takes three months; ignoring effort leaves obvious wins on the table."_ _source: ch10 §The effort side of the equation_

Effort estimates must also be cross-functional — not just engineering time:

> _"A shiny new feature has no value if the company can't market, sell, or service it. Cross-functional overhead is a real cost."_ _source: ch10 §Think cross-functionally_

A minimal ROI scorecard structure looks like:

```
| Theme / Item          | Value Score | Effort (T-shirt) | Effort Score | Confidence % | Priority = (V/E) × C |
|-----------------------|-------------|------------------|--------------|--------------|----------------------|
| Ensure faster onboard | 8           | M                | 5            | 80%          | (8/5) × 0.80 = 1.28  |
| Ensure data export    | 5           | S                | 8            | 90%          | (5/8) × 0.90 = 0.56  |
| Ensure SSO login      | 9           | XL               | 2            | 60%          | (9/2) × 0.60 = 2.70  |
```

Apply a confidence percentage multiplier to the Value/Effort result to discount for risk and unknowns. _source: ch10 §Risks and unknowns_

Use `0` (not just "low") in scoring when a particular idea helps not at all on a given goal — zero should mean zero. _source: ch10 §Deliberate imprecision_

---

## Prioritization Frameworks as the Fix

Every bad method above has a structured alternative. The book presents five frameworks as replacements:

| Bad Method | Better Framework |
|---|---|
| Gut instinct | ROI Scorecard or Critical Path |
| Analyst opinion | Kano Model + primary research |
| Popularity | Desirability / Feasibility / Viability + user interviews |
| Sales requests | ROI Scorecard with strategic value criteria |
| Support requests | Kano Model (separates dissatisfiers from delighters) |
| Competitive me-too | Critical Path (what do customers truly need?) |
| Missing effort | ROI Scorecard (Value/Effort = Priority) |

Full guidance on each framework is in [prioritization-frameworks.md](../patterns/prioritization-frameworks.md).

One constraint that applies to all scorecards: compare only like things. Do not rank a theme against a feature intended to fit within that or another theme. _source: ch10 §A simple scorecard_

---

## When to Use / When NOT to Use

**Use this reference when:**
- You are auditing why the current roadmap lacks strategic coherence.
- Stakeholders are pushing priorities through informal channels (sales calls, executive hallway conversations, analyst briefings).
- A scorecard exists but keeps producing counterintuitive results.
- You are coaching a team new to structured prioritization.

**Do NOT apply rigidly when:**
- Your company exclusively serves one or two large enterprise accounts and roadmap direction is contractually or commercially tied to them — this is the stated exception to the "do not outsource strategy" rule.
- An emergency (outage, regulatory deadline, safety issue) supersedes normal prioritization — always get the most important things done first, and some things are simply forced. _source: ch10 §Why Prioritization Is Crucial_
- Frameworks are being used as a shield to avoid a hard judgment call. The book is clear: _"Prioritization frameworks should be used as an aid to decision-making, not as the decision itself."_ _source: ch10 §Tools Versus Decisions_

---

## Code Examples

Below is a representative bad-vs-good scoring table illustrating what happens when effort is omitted versus included:

```
-- WITHOUT effort column (bad) --
| Theme                         | Value Score | "Priority" |
|-------------------------------|-------------|------------|
| Ensure seamless API access    | 9           | 9          |
| Ensure mobile offline mode    | 9           | 9          |

Result: both ranked equal. Team picks whichever the loudest voice prefers.

-- WITH effort column (correct) --
| Theme                         | Value | Effort (pts) | V/E   | Confidence | Priority |
|-------------------------------|-------|--------------|-------|------------|----------|
| Ensure seamless API access    | 9     | 3 (S)        | 3.00  | 85%        | 2.55     |
| Ensure mobile offline mode    | 9     | 9 (XL)       | 1.00  | 60%        | 0.60     |

Result: API access ranks 4× higher. Decision is now defensible.
```

Signals that **Competitive Me-Too Feature Prioritization** is happening:

```yaml
# Roadmap review red flags — competitive me-too signals
signals:
  - "Roadmap item description contains: 'Competitor X has this'"
  - "Source field on theme is: 'competitive analysis' with no customer validation"
  - "Theme framed as feature parity, not customer outcome"
  - "Pricing notes show increasing pressure as feature gap closes"
```

---

## Related References

- [prioritization-frameworks.md](../patterns/prioritization-frameworks.md) — The five structured frameworks (Critical Path, Kano Model, Desirability / Feasibility / Viability, ROI Scorecard, MoSCoW) that replace each bad method catalogued here.
- [roadmap-anti-patterns.md](roadmap-anti-patterns.md) — Roadmap-level anti-patterns including the **Feature Factory** and date-driven roadmap; overlaps with sales-request and popularity-based failures.
- [themes-and-needs.md](../core/themes-and-needs.md) — How to reframe feature requests and popularity signals into customer-outcome themes that are safe to prioritize.
- [vision-strategy-okrs.md](../core/vision-strategy-okrs.md) — Establishing the strategic goals that define "value" in any prioritization scorecard — required reading before building a value/effort model.
- [build-roi-scorecard.md](../../../../commands/build-roi-scorecard.md) — Command to build a working ROI scorecard, including effort estimation and confidence multipliers.
- [evaluate-special-request.md](../../../../commands/evaluate-special-request.md) — Command to evaluate one-off sales or stakeholder requests against the current roadmap without resorting to sales-request prioritization.
