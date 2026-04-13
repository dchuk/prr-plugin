# Keeping Your Roadmap Fresh

A roadmap that never changes isn't a strategy — it's a monument. Markets shift, competitors move, features run late, and sales teams arrive with urgent requests. The operational question is not *whether* the roadmap will change, but *how* to change it without losing stakeholder trust, execution momentum, or strategic coherence.

## The Problem: Roadmaps Go Stale

The most common failure mode is treating the roadmap as a contract: locked at creation, defended against revision, and quietly irrelevant by the time it reaches the field. The flip side is equally damaging — constant churn with no clear rationale, leaving teams unable to trust that today's priorities will still be tomorrow's.

The book frames the solution through biological analogy: "A roadmap is a living thing and must evolve to fit changes in its environment or face extinction." _source: ch13 §Roadmap Evolution_

The challenge is managing that evolution without chaos.

---

## Punctuated Equilibrium: The Change Model

**Punctuated Equilibrium** is the book's preferred mental model for roadmap change. Borrowed from evolutionary theory, it describes "a theory that evolution proceeds with long periods of relative stability interspersed with rapid change." _source: ch13 §Roadmap Evolution_

Applied to roadmaps: let execution run steadily between deliberate update cycles. Don't change the roadmap constantly in response to every signal, but don't resist change when conditions genuinely warrant it.

This model gives teams a stable target during execution sprints while building in structured moments to reassess.

---

## How Far Out Should Your Roadmap Go?

Roadmap timeframe should be calibrated to the product's stage of life and the pace of market change. The rule:

| Product Stage | Timeframe |
|---|---|
| Discovery | Short — months |
| Growth | Longer — quarters |
| Maturity / Decline | Longest — years |

_source: ch13 Table 10-1_

For fast-moving industries, compress both total timespan and interval granularity. Don't make detailed long-term plans in spaces where companies are still figuring out what the future holds — those plans will surely change.

---

## Refresh Rate: Match Cadence to Time Scale

"The refresh rate of your roadmap should match the time scale of your roadmap." _source: ch13 §Change Frequency_

A quarterly roadmap gets reviewed quarterly. A multi-year roadmap gets reviewed annually. Misaligning review cadence to roadmap horizon either wastes effort (reviewing too often) or leaves the roadmap stale (reviewing too rarely).

**Exception:** Unplanned external events — competitor moves, regulatory changes, or strategic pivots — may require off-cycle updates. Don't wait for the calendar when conditions demand action.

---

## The Iron Triangle: When Features Are Late

When work runs late, the instinct is to hold everything constant and push harder. That path leads to the anti-pattern of **Refusing to Adjust Any Iron Triangle Variable**: quality silently degrades through overwork and corner-cutting, creating technical debt that occupies the team with fixes instead of new roadmap work.

The four interdependent levers are: **schedule, scope, quality, and budget (resources)**. When one slips, at least one other must give — explicitly and consciously.

### Working through a delay

1. Diagnose which variable is the root cause.
2. Determine which variable is most fixed for the business (e.g., hard regulatory deadline vs. soft internal target).
3. If schedule is flexible: accept the new date and adjust the roadmap.
4. If schedule is fixed: evaluate scope reduction — deliver in stages, drop non-required features.
5. If scope cannot be cut: evaluate resources — but see the caveat below.
6. If all other variables are held constant: explicitly acknowledge quality will be compromised and assess technical debt implications.
7. Communicate the trade-off decision to stakeholders immediately.

### The resources trap

"Small teams of three to seven people are most effective at delivering on software projects; adding manpower to a late software project makes it later." _source: ch13 §Resources_

This is Brooks's Law from *The Mythical Man-Month*. Adding people increases communication overhead and burdens the existing team with onboarding at the worst possible moment. Adding resources only works when the problem is simple manufacturing capacity (a second shift, an additional plant) — not knowledge work.

### When to compromise on quality

For unproven new products in uncertain markets, deliberate quality trade-offs are reasonable. Eric Ries's **Minimum Viable Product** definition: "that version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort." _source: ch13 §When to Compromise on Quality_

"Working hard to make a first version the most scalable, most elegantly built thing is likely wasted effort — and it slows progress toward learning from customers." _source: ch13 §When to Compromise on Quality_

Do not compromise on quality when: the product will be used by millions with minimal changes, scale investments are required up front, or quality failures trigger regulatory non-compliance.

---

## Changes in Strategy: The Pivot

A **pivot** is "a change in strategy without a change in vision," as defined by Eric Ries. _source: ch13 §Changes in Strategy_ When the current strategy is unlikely to achieve the vision, redirect to a better market or approach.

"It doesn't make sense to wait for a regularly scheduled roadmap review to change strategy — when it's time for a pivot, revisit everything from the product vision down." _source: ch13 §Changes in Strategy_

When executing a pivot:
1. Don't wait for the calendar — act when the signal is clear.
2. Revisit vision, strategy, goals, and themes from the top down.
3. Be explicit about what is changing, what is not changing, and why.
4. Socialize with stakeholders before finalizing the new direction.
5. Build decision criteria and alternative roadmap paths into the updated plan if the pivot is contingent on performance thresholds.

---

## Special Requests: The Three Questions

Special requests — typically from sales, to add a feature or one-off capability for a specific customer in exchange for closing a deal — are a constant operational reality. They must be evaluated before being accepted. The three qualifying questions:

1. **What problem is this request trying to solve?** Trace it back past the sales contact to the person with the underlying problem. Interview them directly.
2. **Does solving that need align with our current objectives?** If not, decline or defer.
3. **Is it more important than what's already on the roadmap?** Evaluate using objective prioritization.

If all three answers are yes, accept the request — but immediately determine which iron triangle variable(s) (schedule, scope, budget, or quality) will be compromised to accommodate it. The anti-pattern of **Adding Scope Without Deciding What Gives** — agreeing to add unplanned work without deciding the trade-off — leaves the outcome to chance and produces missed deadlines that surprise the team.

---

## Communicating Roadmap Change

"The reasons change is occurring may be the most important part of a roadmap update, and yet this information is often left out." _source: ch13 §Why_

Communicate the **why, what, and when** of every update to all stakeholders.

### Why
Frame the change in terms of how it results in a better future for the company, customer, and stakeholders. Reference the unchanged vision and strategy to anchor the audience and demonstrate continuity. The anti-pattern of **Hiding the Why Behind Roadmap Changes** — sharing what changed but omitting the rationale — causes team morale to drop and stakeholders to invent less-charitable explanations. "Don't shy away from discussing change — embrace it and get everyone on board." _source: ch13 §Why_

### What
Specify the depth of change: a small subtheme or date adjustment, broad theme movement, or a full pivot. The depth determines the communication effort required.

### When
Communicate updated timelines and delivery expectations. Update the roadmap artifact with clear annotations of what changed (colors, arrows, pop-ups). Socialize the change the same way you would socialize a new roadmap from scratch. Share the clean updated version (without markup) externally after the review, with a date stamp.

**Exception:** Minor changes — small scope or date adjustments — may not require full socialization and may only affect the release or project plan.

---

## Forks in the Road

Some roadmaps contain meaningful strategic decision points: two or more materially different paths forward depending on what happens. These can be embedded in the roadmap with explicit decision criteria and thresholds (specific performance numbers) to build optionality into the plan.

"Incorporate thresholds (specific performance numbers) as decision criteria into the roadmap to build optionality and define when to follow one strategic path versus another." _source: ch13 §Forks in the Road_

This is particularly useful when a pivot is contingent on whether a key result is hit. Rather than pretending certainty, show the branch and name the threshold that determines which path is taken.

---

## How Deep to Revise: Lather, Rinse, Repeat

"The deeper the roadmap changes, the further back in the creation process you need to go to revisit assumptions." _source: ch13 §Lather, Rinse, Repeat_

| Change Depth | Go Back To |
|---|---|
| Small subtheme or date change | Refresh stakeholder buy-in |
| Priorities have shifted, vision unchanged | Revisit prioritization |
| Moving into new areas of functionality | Revisit value focus and customer research |
| Customer/org needs or customer types have changed | Revisit themes |
| Vision, strategy, or key business objectives have changed | Rethink from the ground up |

---

## When to Use / When NOT to Use

**Use this guidance when:**
- Setting the roadmap review cadence for your product stage.
- A feature is running late and the team needs to decide what gives.
- Sales or a stakeholder arrives with a special request.
- A strategic pivot is becoming necessary.
- Communicating any planned or unplanned roadmap update to stakeholders.

**Do NOT apply this guidance when:**
- You are creating a roadmap from scratch — start with vision and inputs, not change management.
- Changes are purely internal execution adjustments (sprint-level scope changes within a committed theme) that don't affect the roadmap artifact itself.
- The refresh cadence debate is a proxy for a deeper misalignment on strategy — address the strategy first.

---

## Code Examples

The following illustrates the three-question filter for special requests and the iron triangle trade-off decision, expressed as a structured evaluation checklist:

```
Special Request Evaluation
──────────────────────────
Request: [Describe the feature/fix]
Requester: [Sales contact] → Underlying stakeholder: [End user]

Q1: What problem is this solving?
    Root problem: _______________
    Requester in target market? Y / N

Q2: Does it align with current objectives?
    Relevant objective: _______________
    Aligned? Y / N

Q3: Is it more important than what's on the roadmap now?
    Comparison item displaced: _______________
    Higher priority? Y / N

Decision: Accept / Decline / Defer

If Accept → Iron Triangle Trade-Off:
    Variable to adjust: [ ] Schedule  [ ] Scope  [ ] Budget  [ ] Quality
    Specific impact: _______________
    Communicated to: _______________
```

The communicate-change structure for a roadmap update:

```
Roadmap Change Communication
─────────────────────────────
WHY (required — do not omit)
  Market/competitive condition: _______________
  How the change serves company / customer / stakeholders: _______________
  What is NOT changing (anchor to vision): _______________

WHAT
  Depth of change: [ ] Minor  [ ] Broad  [ ] Fundamental pivot
  Specific changes: _______________
  Annotated roadmap artifact: [updated with date stamp]

WHEN
  Updated delivery expectations: _______________
  Socialization meetings: _______________
  External share date (clean copy): _______________
```

---

## Related References

- [Roadmap Definition](../core/roadmap-definition.md) — Why the roadmap is not a contract; the foundational premise behind why change is expected and acceptable.
- [Roadmap Components](../core/roadmap-components.md) — The Now / Next / Later timeframe model and how it relates to refresh cadence.
- [Prioritization Frameworks](../patterns/prioritization-frameworks.md) — The objective methods (Critical Path, Kano Model, ROI Scorecard, MoSCoW) to use when evaluating whether a special request outranks existing roadmap items.
- [Alignment and Buy-In](../patterns/alignment-and-buyin.md) — How to socialize roadmap changes the same way you would socialize a new roadmap from scratch.
- [Presenting and Sharing](../patterns/presenting-and-sharing.md) — Audience-specific communication when distributing an updated roadmap.
- [Roadmap Anti-Patterns](../anti-patterns/roadmap-anti-patterns.md) — **Rigidly Adhering to an Outdated Roadmap** and other change-related anti-patterns in consolidated form.
- [Bad Prioritization](../anti-patterns/bad-prioritization.md) — Anti-patterns to avoid when evaluating whether a special request belongs on the roadmap.
- [Relaunch Process](relaunch-process.md) — The Roadmap Health Assessment and structured process for deeper roadmap overhauls.
- [Evaluate Special Request command](../../../../commands/evaluate-special-request.md) — Automates the three-question filter and iron triangle trade-off decision.
- [Communicate Roadmap Change command](../../../../commands/communicate-roadmap-change.md) — Drafts a why/what/when change communication for stakeholders.
