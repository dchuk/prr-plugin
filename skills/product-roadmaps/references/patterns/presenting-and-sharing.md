# Presenting and Sharing Your Roadmap

## Problem Framing

A roadmap that never leaves your desk fails its primary purpose. The moment you share it, though, you face a new set of risks: sales teams treating themes as contractual commitments, executives drilling into sprint-level detail, customers freezing purchases because they're waiting for what you just announced, and engineering wondering why there's no mention of technical debt.

The core pain is a mismatch between what each audience needs from the roadmap and what a single artifact delivers. Most product managers solve this by either sharing one undifferentiated document (which serves nobody well) or by maintaining completely separate roadmaps per audience—which drifts into contradiction and doubles the maintenance burden.

The solution the book prescribes is a **modular roadmap approach**: a shared foundation of vision, strategy, and themes, augmented with audience-specific layers. One source of truth, multiple views.

---

## The Risks of Sharing

Before tailoring for each audience, understand the two most dangerous failure modes.

### Overpromising and Underdelivering

The **Overpromising and Underdelivering** anti-pattern occurs when roadmap items are shared as firm commitments to features and dates. When the team changes course or cannot deliver exactly what was promised, trust erodes.

The fix is to communicate direction and intent via themes rather than specific deliverables, and to use confidence percentages and hedging language. _source: ch12 §The Risks of Sharing_

### The Osborne Effect

The **Osborne Effect** is the phenomenon where announcing future product plans too early slows down current sales, as customers wait for the next version. Named after the Osborne 1 computer whose sales fell sharply in 1983 after founder Adam Osborne pre-announced new models, ultimately leading to bankruptcy. _source: ch12 §The Risks of Sharing_

**Signals to watch for:**
- Publicly announcing specific future product models or versions before they are ready
- External roadmap showing near-term products that will render the current product obsolete
- Dealers or customers canceling existing orders in anticipation of announced future products

**Fix:** Be selective about what future plans are shared externally and when. Focus external communications on value delivery rather than specific upcoming product versions.

### Competition

The further away from the core product development team a stakeholder is, the less detail about features, functions, and dates should be provided. If themes indicate product direction that may further differentiate you competitively, consider not including those on external roadmaps.

---

## The IKEA Effect: Why Broad Sharing Builds Buy-In

The **IKEA Effect** is the psychological phenomenon whereby people assign greater value to things they had a hand in creating. Applied to roadmaps: involving stakeholders in the development and refinement of the roadmap radically increases buy-in, just as people love IKEA furniture because they assembled it themselves. _source: ch12 §Why to Share Your Roadmap Internally_

This is why roadmaps should be shared broadly across the organization, not just with the immediate team and management chain. Every department benefits from a view into what's coming and an opportunity to contribute.

**Practical implication:** Don't share a finished roadmap for sign-off. Involve stakeholders early and often so the roadmap feels partly theirs.

---

## The Modular Roadmap Approach

Rather than creating entirely separate roadmaps for each stakeholder group, build a shared core and augment it:

```
┌─────────────────────────────────────────┐
│  COMMON FOUNDATION (all audiences)      │
│  • Product vision                       │
│  • Business objectives / OKRs           │
│  • Themes (Now / Next / Later)          │
└─────────────────────────────────────────┘
         │              │              │
         ▼              ▼              ▼
   Dev Team         Sales/Mktg      Executives
   + Features       + Confidence    + Financial
   + Stage          + Stage         + Market
   + Areas          + Hedging       + P&L
   + Debt           + Ext. drivers  (high-level)
   + Deps
                         │
                         ▼
                    Customers
                    + Value view
                    (simplified)
```

**Anti-pattern to avoid:** Maintaining Entirely Separate Roadmaps per Audience — creating completely different roadmaps for each stakeholder group rather than a modular approach defeats efforts to align the organization around a common cause. Different stakeholder groups end up with roadmaps that contradict each other, and updates must be made independently in multiple documents. _source: ch12 §Multiple Roadmaps? Not So Fast!_

---

## Presenting to Each Audience

### Principle: Know Your Audience

Roadmap presentations should be tailored to the specific audience's concerns, level of detail required, and goals. Different stakeholders have fundamentally different planning needs; a one-size-fits-all presentation fails to serve any of them well. _source: ch12 §Presenting the Roadmap to Stakeholders_

Always start with the 'why' — product vision — and ensure everyone is on board before moving to details.

---

### Development Team

Engineers, designers, testers, and operations staff need enough context to plan work, estimate effort, and think about architecture.

**What to include:**

| Element | Why It Matters |
|---|---|
| Short list of likely features per theme | Sets direction without over-specifying |
| Stage of development | Resource planning and expectation-setting |
| Product areas (tags, colors, swim lanes) | Maps to internal team organization |
| Scalability expectations (usage volume + timing) | Infrastructure and architecture planning |
| Technical debt | Hidden work must be built into plans alongside features |
| Dependencies and risks | Sequence work; identify contingency plans early |

**On technical debt:** The hidden work required when underlying technical infrastructure must be rewritten or refactored to support new features or additional users may require rearchitecture or replatforming. Work with the internal team to surface this work and build it into roadmap plans alongside more visible feature work. _source: ch12 §Complementary Information: Platform Considerations_

**On dependencies:** Factor inter-item dependencies into roadmap sequencing and identify team dependencies as early as possible so they can be prioritized and contingency plans developed.

---

### Sales and Marketing

Sales and marketing teams use the roadmap to plan campaigns, manage customer conversations, and coordinate launches. Their risk is turning casual roadmap conversations into promises.

**What to include:**

- **Stage of development** — Marketing and sales usually care about a product when they can begin talking about it; a beta (early access) program allows this to happen before a full launch.
- **Confidence percentages** — A percentage value added to roadmap items or timeframes indicating how likely they are to be delivered as planned. Used to manage expectations without making firm commitments. _source: ch12 §What Sales and Marketing Need in a Roadmap_
- **Limited feature visibility with hedging language** — When discussing features with sales and marketing, use hedging language such as 'likely', 'probable', and 'tentative', and make liberal use of confidence percentages.
- **External drivers** — Market events and competitive context that explain the roadmap's sequencing.

**Rule:** Do not commit sales or marketing campaigns (e.g., expensive spokespeople) to roadmap items with confidence below ~80%.

---

### Executives and Board Members

Executives need strategic context, not operational detail. They should be able to assess whether the product direction aligns with company strategy and financial objectives.

**What to include:**
- High-level vision, strategy, and problem-solving themes
- Financial information: market opportunity, P&L projections
- Complementary information relevant to business outcomes

**What to leave out:** Detailed feature lists, sprint plans, or infrastructure specifics — unless an inquisitive board member develops concerns, in which case all details should be available on hand.

**Rule:** Lead with the high-level; bring detail as backup, not as the opening.

---

### Customers

Customers may ask for feature and date commitments, but what they really need is to know you are listening, have skin in the game, and will keep them informed. _source: ch12 §What Customers Need in a Roadmap_

**What to include:**
- Greatly simplified view focused exclusively on the value customers should anticipate
- No internal details (technical debt, dependencies, infrastructure)

**Exception:** Enterprise and component manufacturing customers often have long planning horizons and need detailed timing to plan their own products. In those contexts, a more detailed roadmap with timing is necessary to win and retain business.

**Rule:** A roadmap is not a promise or commitment for a set of features. When customers demand specific feature or date commitments:
- Address the real underlying need: reassurance that you are listening and have skin in the game
- If confident about a release a quarter ahead, give a general timeframe answer
- Do not commit when confidence is not high — the more commitments to specific deliverables made, the less flexibility to adjust course, which is not in the customer's interest

---

## Preparing the Roadmap Presentation

One of the chief functions of a roadmap is to get everyone excited about the future. Presentations should combine emotion, data, and stories to give meaning to prioritization decisions:

- **Emotion** — Connect the roadmap to the human problems it solves
- **Data** — Quantify the opportunity and validate the prioritization
- **Stories** — Illustrate the customer need each theme addresses

Start with the product vision. Confirm everyone is aligned on the 'why' before presenting themes and any feature-level detail.

---

## Case Study: The Top-Down Feature Commitment Anti-Pattern

The **Top-Down Feature Commitment Roadmap** anti-pattern occurs when executives or founders present a roadmap with specific features and dates as directives — "Here's what we're going to build this year" — creating missed expectations when the team cannot deliver as planned. _source: ch12 §Case Study: Chef.io's Roadmap Presentation_

**Signals:**
- Roadmap presented as a directive rather than a collaborative plan
- Features listed with fixed delivery dates set without team input
- Customers receiving conflicting feature expectations
- Team consistently unable to meet roadmap deadlines

**Fix:** Use theme-based roadmaps that relate to business objectives. Involve the team in shaping the roadmap. Separate internal and external roadmap artifacts. Include qualifiers and disclaimers in external presentations.

---

## Code Examples

### Confidence Percentage on a Roadmap Item (YAML representation)

```yaml
themes:
  - name: "Ensure faster onboarding for new enterprise customers"
    timeframe: "Now"
    confidence: 90%
    likely_features:
      - "Guided setup wizard"
      - "SSO integration"
    stage: "In development"

  - name: "Ensure data portability for compliance-focused customers"
    timeframe: "Next"
    confidence: 65%
    likely_features:
      - "CSV/JSON export"
      - "Audit log API"
    stage: "Discovery"
    note: "Tentative — dependent on compliance framework finalization"

  - name: "Ensure global reach for international expansion"
    timeframe: "Later"
    confidence: 40%
    stage: "Exploratory"
    note: "Probable direction; timing subject to change"
```

### Hedging Language Examples for Sales/Marketing

```
Instead of: "We will ship the export feature in Q3."
Use:        "We're likely targeting Q3 for the export feature — confidence is around 70%."

Instead of: "The integration will be ready at launch."
Use:        "The integration is probable for launch; we'll confirm as we get closer."

Instead of: "Feature X is on the roadmap for this year."
Use:        "Feature X is a tentative item for the second half — I'd put it at 60% confidence."
```

### Modular Roadmap Slide Structure

```
Slide 1 (ALL audiences):    Product Vision
Slide 2 (ALL audiences):    Business Objectives / OKRs
Slide 3 (ALL audiences):    Themes — Now / Next / Later

--- Audience-specific layers ---

Slide 4a (Dev team):        Features + Stage + Product Areas
Slide 4b (Dev team):        Platform Considerations (Scalability, Tech Debt)
Slide 4c (Dev team):        Dependencies + Risks

Slide 4a (Sales/Mktg):      Stage of Development + Beta Program Dates
Slide 4b (Sales/Mktg):      Confidence Percentages + External Drivers
Slide 4c (Sales/Mktg):      Target Customers per Theme

Slide 4a (Executives):      Market Opportunity + P&L Projections
Slide 4b (Executives):      Strategic Risks and Assumptions

Slide 4a (Customers):       Value Delivery Summary (simplified, no internal detail)
```

---

## When to Use / When NOT to Use

### When this guidance applies

- Any time you are preparing to share a roadmap artifact beyond your immediate product team
- When you are deciding how much detail to include for a specific audience
- When sales or marketing teams are asking for feature commitments to share with customers
- When executives are requesting a roadmap review
- When you are building your first cross-functional roadmap presentation

### When it does NOT apply (or needs adaptation)

- **Component manufacturing / enterprise software with long planning horizons** — customers in these contexts genuinely need detailed timing to plan their own products. The "simplified customer view" rule has an explicit exception here; provide more timing detail than you would for consumer-facing roadmaps.
- **Very early-stage products** — when there is no stable vision or theme set yet, the modular approach has nothing to build on. Establish the common foundation first (see [vision, strategy, and OKRs](../core/vision-strategy-okrs.md)) before tailoring for audiences.
- **Internal alignment is broken** — if stakeholders fundamentally disagree on strategy, presenting a polished roadmap will surface the conflict rather than resolve it. Run alignment work first (see [alignment and buy-in](alignment-and-buyin.md)).

---

## Related References

- [Roadmap Definition](../core/roadmap-definition.md) — Clarifies what a roadmap is and is not; foundational for framing any presentation correctly
- [Roadmap Components](../core/roadmap-components.md) — The primary components (vision, themes, timeframes) that form the common foundation of all audience-specific views
- [Themes and Needs](../core/themes-and-needs.md) — How to express roadmap content as customer outcomes rather than features, which is essential for audience-appropriate communication
- [Alignment and Buy-In](alignment-and-buyin.md) — The shuttle diplomacy and co-creation techniques that build the stakeholder relationships that make roadmap sharing effective
- [Roadmap Anti-Patterns](../anti-patterns/roadmap-anti-patterns.md) — Consolidated reference including the **Feature Factory** and feature-date-driven patterns that frequently emerge when sharing goes wrong
- [Keeping the Roadmap Fresh](../topics/keeping-roadmap-fresh.md) — How to communicate roadmap changes after initial sharing, including stakeholder communication protocols
- [Communicate Roadmap Change command](../../../../commands/communicate-roadmap-change.md) — Draft stakeholder communications when a shared roadmap changes direction
