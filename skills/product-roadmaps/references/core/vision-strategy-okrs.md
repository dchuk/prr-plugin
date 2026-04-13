# Vision, Strategy, and OKRs: Establishing the Why

## Problem Framing

The most common early roadmap failure is not a bad prioritization decision — it is building a roadmap with no foundation. A PM assembles a list of features, assigns quarters, and calls it a roadmap. Stakeholders treat it as a delivery contract. Engineers ask "why are we building this?" and get no useful answer. The team ships feature after feature with no connection to an intended outcome: the classic **Feature Factory**.

The book's corrective is direct: *a roadmap must first establish a vision and strategy as its foundation; the features and deliverables support and contribute to that foundation rather than carrying the burden themselves.* (_source: ch07 §Values Are Beliefs and Ideals_)

This reference covers the full hierarchy — mission → vision → values → product vision → product strategy → OKRs/KPIs — and the rules that keep each layer honest.

---

## Mission: Your Current Intent

A mission defines the intent you hold right now and the purpose driving you to realize your vision. It answers: what do we do, for whom, and why does it matter today?

### The Four-Element Test

A well-crafted mission statement must contain all four elements:

| Element | Question it answers |
|---|---|
| **Value** | What value does it bring? |
| **Inspiration** | How does it inspire the team? |
| **Plausibility** | Is it realistic and achievable? |
| **Specificity** | Is it specific to your business, industry, or sector? |

_source: ch07 §Mission Defines Your Intent_

**Critical rule:** Mission must reflect what you do for someone else — typically your customers, not your shareholders. A mission written around investor returns fails the Value and Inspiration tests.

---

## Vision: The Outcome You Seek

Vision is a longer-term outcome that has an impact on the lives of the people your product serves and on your organization. It is *why your organization exists*, painting a future reality — not a current-state description of the company.

### Minimum Required Elements

A solid vision statement must address at minimum:

- **Who?** — the target customer
- **Why?** — the benefit or need addressed

Optionally: **How is it different?** — what makes it unique.

### The Conflation Anti-Pattern

Many company vision statements are actually mission statements. Vision statements often fail by being self-centered — phrased as "be the best ___" — rather than describing a future world that benefits customers.

**Signals of the problem:**
- Vision reads like a current-state description of the company
- Vision is phrased as superlatives ("best," "leading," "world-class")
- Vision does not mention customers or customer benefit

**Fix:** Distinguish clearly: mission is your current intent and purpose; vision is the longer-term outcome impacting customers and the organization.

### The Duality Principle

A purely external vision (customer-only) ignores business viability. A purely internal vision fails to serve customers. The book's stance: acknowledging that you need to make money to stay in business and deliver on your vision of a better world is healthy; internal and external visions should work together symbiotically. (_source: ch07 §Duality of Company and Customer Benefit_)

Microsoft's 1980s vision — "a personal computer on every desk running Microsoft software" — is cited as an example that was too company-centric, with no mention of what customers gained.

---

## Values: The Compass

Values are beliefs and ideals intended to guide behaviors and shape culture — how people behave when no one is watching. They are described as a compass: they tell you what is right or wrong for the business but not which direction to travel. Vision and mission provide direction.

---

## Product Vision: Why Your Product Exists

Product vision clarifies why you are bringing a product to market and what its success will mean to the world and to the organization. It is the raison d'être of the entire effort and forms the basis of the roadmap.

**Multi-product rule:** If an organization has multiple products, the product vision must be supportive of and derived from the corporate vision.

**Communication rule:** A product vision stuck in one person's head does nobody any good; it must be communicated to the rest of the organization. Without a shared vision, decisions made in the absence of the vision holder will be inconsistent and directionless.

### Value Proposition Template (Elevator Pitch Template)

Adapted from Geoffrey Moore's *Crossing the Chasm*, this fill-in-the-blank template structures a product vision:

```
FOR [target customer]
WHO [customer need]
THE [product name] IS A [product category]
THAT [key benefit / reason to buy]
UNLIKE [competitor]
OUR PRODUCT [differentiation]
```

This can be further compressed to a single vision statement sentence. Use it when starting a product vision from scratch, or as a gut-check to determine if an existing vision is robust enough to drive product strategy and roadmap.

---

## Product Strategy: The Bridge

Product strategy connects your high-level vision to the specifics of your roadmap. It makes the vision more explicit and concrete by explaining *how* the vision will be achieved, usually in the form of objectives.

### 10 Universal Business Objectives

Every business objective can be distilled into one of 10 categories (Table 4-1 from the book):

**Sustainable Value**
- Support core value proposition
- Create barriers to competition

**Growth**
- Grow market share
- Fulfill current demand
- Develop new markets
- Improve recurring revenue

**Profit**
- Support higher prices
- Improve customer lifetime value
- Lower costs
- Leverage existing assets

These 10 apply to any product — hardware, software, or service. Use them to stress-test whether your stated objectives are genuinely strategic.

---

## OKRs and KPIs: Connecting Vision to Measurement

### Objectives and Key Results (OKRs)

OKRs pair business objectives with success criteria. First implemented by Andrew Grove at Intel in the early 1980s:

- **Objectives** — specific qualitative goals
- **Key Results** — quantitative measures of progress toward those objectives

**The fewer-than-five rule:** Use fewer than five objectives in your OKR framework for product roadmapping. The more objectives you have, the less focus you can give them. (_source: ch07 §Objectives and Key Results_)

**The tethering rule:** Everything on the roadmap must be tied to at least one of your objectives. Untethered roadmap items cannot be justified, prioritized, or measured for success.

**Sharing rule:** A roadmap based primarily on internal business objectives must not be shared with customers or channel partners — they care about value added to them, not your internal allocation decisions.

### Key Performance Indicators (KPIs)

KPIs define how the success of a product will be measured before release. They are the data that give meaningful feedback on how a product is doing, and are often the metrics used to measure the key results from OKRs.

A robust picture of product performance combines:
- Direct customer conversations
- Product usage metrics
- Net Promoter Score (NPS)

**The one-hour rule:** If it takes longer than one hour to review your data at a high level each week, you are tracking too many metrics. Limit to three to five objectives with corresponding metrics.

**Revenue-alone warning:** Tracking revenue as your sole product success metric is insufficient when you want to create a product that provides lasting value or need early warning signals before revenue declines. Revenue is a lagging indicator.

---

## Outcome vs. Output

> "Outcomes are the difference made by the outputs." — Deb Mills-Scofield

- **Outputs** — the stuff produced (features, physical products) for a specific customer
- **Outcomes** — the difference that output makes (e.g., keeping a child safe)

Roadmaps should focus on outcomes over outputs. An output-focused roadmap produces the **Feature Factory** anti-pattern: a product team that releases feature after feature with no tie back to the reason for those features — no connection to an intended outcome.

**Signals of Feature Factory:**
- Roadmap is a list of features with no stated objectives
- Team cannot explain why a feature is being built beyond "customer asked for it"
- No measurable key results defined for any roadmap theme

**Fix:** Ground every roadmap item in at least one objective. Use OKRs to make the connection between deliverables and desired results explicit. See [bad-prioritization.md](../anti-patterns/bad-prioritization.md) for related output-driven prioritization failures.

---

## Timing: Roadmaps Are Not Release Plans

A roadmap is not a release plan; it is a sequence of stakeholder priorities and requires concept feasibility for delivery. A release plan requires rigorous scope definition and engineering capacity planning, which a roadmap should not carry.

**Use loose timeframes** (Now / Next / Later) on roadmaps rather than specific dates. Reserve specific dates, scope definitions, and engineering capacity planning for release and project plans.

```
Now     → Current cycle of active work
Next    → Committed but not yet started
Later   → Directional; not yet scoped
```

**Exception:** When software is embedded in another product with strict production deadlines (e.g., software loaded onto a television at manufacture), specific dates may be required — but should still be tracked at the project or release plan level, not the roadmap.

**Signals that a roadmap has become a release plan:**
- Roadmap contains specific calendar dates (e.g., Q2 2025, January 2026)
- Stakeholders treat roadmap commitments as contractual delivery promises
- Roadmap changes cause the same disruption as a missed sprint deadline

---

## When to Use / When NOT to Use

**Apply this guidance when:**
- Starting a new product or roadmap from scratch and the vision/strategy layer is undefined or implicit
- An existing roadmap is a pure feature list with no stated objectives
- Stakeholders are treating the roadmap as a delivery contract with dates
- The team cannot articulate why any given item is on the roadmap
- Metrics review is consuming more than one hour per week (too many KPIs)
- You need to decide which roadmap version to share with external stakeholders

**This guidance does not apply when:**
- The vision and strategy layer is already well-documented, shared, and accepted — in that case, proceed directly to theme development and prioritization
- You are working on a release plan or sprint plan, which intentionally requires scope, dates, and capacity planning that a roadmap should not carry
- The product is in End of Life phase, where new vision-setting may be inappropriate — see [gathering-inputs.md](gathering-inputs.md) for product life cycle stage considerations

---

## Code Examples

### Value Proposition Template in Use

```
FOR busy working parents
WHO need to monitor their child's online activity without constant supervision
THE SafeScreen app IS A parental control and screen-time management tool
THAT keeps children safe online while preserving family trust
UNLIKE competitor tools that use blunt blocking
OUR PRODUCT adapts dynamically to each child's behavior and age
```

Compressed to a single vision statement:
```
SafeScreen helps working parents keep their children safe online
by adapting screen-time controls dynamically to each child's needs —
replacing anxiety with confidence.
```

### OKR Structure Example

```
Objective 1: Ensure parents feel in control of their child's digital safety
  KR 1.1: 80% of active users set at least one custom rule within first week
  KR 1.2: NPS score reaches 45 or above within two product cycles
  KR 1.3: Support ticket volume for "blocked by mistake" drops 30%

Objective 2: Grow recurring revenue from family subscriptions
  KR 2.1: Monthly recurring revenue increases 20% quarter-over-quarter
  KR 2.2: Annual plan adoption reaches 60% of new subscribers
```

*(Fewer than five objectives; each roadmap theme maps to at least one objective.)*

### Roadmap Timeframe Format (Not a Release Plan)

```
Theme: Ensure children are protected from age-inappropriate content
  Now:   Audit and improve existing content-category filtering accuracy
  Next:  Introduce per-child age profiles with adaptive rule defaults
  Later: Explore real-time behavioral signals for dynamic adjustment
```

No calendar dates. No sprint commitments. Strategic direction only.

---

## Related References

- [roadmap-definition.md](roadmap-definition.md) — What a product roadmap IS and IS NOT; how vision and strategy connect to the roadmap artifact itself
- [roadmap-components.md](roadmap-components.md) — The three tiers of roadmap components; how themes, timeframes, and objectives appear on the roadmap
- [themes-and-needs.md](themes-and-needs.md) — How to translate product strategy objectives into customer-outcome themes
- [prioritization-frameworks.md](../patterns/prioritization-frameworks.md) — How objectives feed directly into the Critical Path, Kano Model, and ROI Scorecard frameworks
- [bad-prioritization.md](../anti-patterns/bad-prioritization.md) — Seven bad prioritization methods, including output-driven approaches that produce the **Feature Factory**
- [roadmap-anti-patterns.md](../anti-patterns/roadmap-anti-patterns.md) — Roadmap-level anti-patterns including the feature-date-driven roadmap and treating the roadmap as a release plan
- [build-roadmap-from-vision.md](../../../../commands/build-roadmap-from-vision.md) — Command: construct a roadmap skeleton from company vision down to themes
