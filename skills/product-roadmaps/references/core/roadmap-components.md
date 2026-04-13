# Roadmap Components

A features-and-dates list is the most common roadmap failure mode. It answers "what" and "when" but not "why" — leaving teams without a shared direction and stakeholders without a reason to trust the plan. The three-tier component model gives you a systematic way to build a roadmap that tells the full story: where you're going, why it matters, how you'll get there, and how confident you are in each step.

## The Core Problem: Features and Dates Aren't Enough

The book states it plainly: a roadmap must tell the story of what it will be like when you achieve your vision, what it will take to get there, and how you will know if you are making progress — not merely list features and dates. _source: ch05 opening paragraphs_

A simple features-and-dates chart cannot effectively rally teams around a plan or communicate the why behind the work. It also creates a trap: the moment you attach a date to a feature, stakeholders treat it as a commitment, and the roadmap becomes a project plan you're perpetually behind on.

There is no template or boilerplate for roadmap greatness; every roadmap is different depending on what you are trying to communicate and to whom. _source: ch05 opening paragraphs_ The three-tier model — primary, secondary, complementary — gives you a structured way to decide what to include without prescribing a single format.

---

## Tier 1: Primary Components (Required)

Every roadmap must include all five primary components. Think of this as your checklist before any roadmap leaves your desk.

| Component | What it is |
|-----------|------------|
| **Product Vision** | How a specific sort of customer will benefit from your product when it is fully realized and ubiquitous. Serves as the North Star for the roadmap. |
| **Business Objectives** | The measurable goals and outcomes the product will accomplish for the organization — the "why" in concrete terms. |
| **Themes** | Organizing units expressing customer needs or problems rather than specific features. They answer: "What would need to be true for our product to realize its vision and attain its business objectives?" |
| **Timeframes** | Broad temporal divisions (calendar quarters or Now / Next / Later) that provide sequencing guidance while preserving flexibility. |
| **Disclaimer** | A caveat making clear that anything in the roadmap is subject to change without notice. |

### Product Vision

The company and product vision should ground all roadmap development, providing the foundation for every subsequent decision. Without a stated vision, themes and objectives float free — stakeholders have no way to evaluate whether a proposed theme actually moves the product forward.

### Business Objectives

Business objectives express the "why" of the roadmap in concrete, measurable terms. They sit between the vision (aspirational) and themes (tactical direction), giving reviewers a way to test whether a theme actually serves organizational goals.

### Themes

Themes should focus on outcomes (customer needs and problems) rather than output (specific features). Expressing themes as customer needs or problems is very effective in guiding the development of solutions. _source: ch05 §Themes_

Use the phrasing "Ensure [result] for [stakeholder]" when writing theme examples — this keeps the frame on customer outcomes, not deliverables.

### Timeframes

Do not include specific ship dates for roadmap themes and solutions; use broad timeframes instead. Focusing on dates as the primary measure of success diverts attention from the iterative and uncertain process of innovation. _source: ch05 §Timeframes_

The Now / Next / Later model is the canonical example from the book. Calendar quarters are acceptable when an organization requires them, but carry higher commitment risk. _Exception: External events and hard commitments may warrant specific dates — see the discussion of special requests in [alignment and buy-in](../patterns/alignment-and-buyin.md)._

### Disclaimer

Include a disclaimer on the roadmap making it clear that anything in it is subject to change without notice. Consult finance or legal regarding your organization's policy. Large public companies may require more elaborate disclaimers. _source: ch05 §Disclaimer_

The disclaimer is not optional — it is what separates a strategic communication tool from a binding contract. See [roadmap definition](roadmap-definition.md) for the full distinction.

---

## Tier 2: Secondary Components (Optional, Stakeholder-Driven)

Secondary components deepen the roadmap and address the specific concerns of certain stakeholders. Every additional bit of information has the potential to backfire; the best roadmaps home in on the additional context most important to particular stakeholders. _source: ch05 §Secondary Components_

Adding secondary components reduces time spent explaining and increases time spent executing by improving stakeholder buy-in and alignment. _source: ch09 opening section_

### Features and Solutions (Subthemes)

Features and solutions should appear as subthemes beneath relevant themes, never alongside or replacing themes, so that the "why" is always retained in the roadmap. Listing features side by side with themes loses the problem context; subthemes make the intent explicit. _source: ch09 §Where Do Features Appear on the Roadmap?_

Three types of solutions appear on roadmaps:

- **Probable solutions** — Likely solutions included when a solution seems evident, without having finalized or fully validated it. Their inclusion does not remove the need for testing and validation.
- **Infrastructure solutions** — System-level technical solutions defined and vetted internally by the engineering team. These often transition quickly from need to solution and typically require less external stakeholder validation.
- **Carryover** — Themes or features from a previous roadmap or release plan that were not completed due to time or resource constraints and are moved into the next version.

**Decision rule — include features when:**
- The theme is near shipment and the product is in pre-production or beta
- Stakeholders (sales, marketing, channel partners) need concrete detail to prepare
- There are validated carryover items or engineering-vetted infrastructure needs

**Do not include features when:**
- The theme is early in development (discovery, design, or prototyping)
- The likelihood that the solution will be changed, postponed, or dropped is high

### Stage of Development

A label applied to each roadmap item indicating where it stands in the development process — discovery, design, alpha, beta, or custom labels like "think it / ship it / tweak it" — helping stakeholders understand the maturity of each item. _source: ch09 §Using Stage of Development_

**Include when:**
- Themes go through distinct stages and those stages take longer than the timeframes on the roadmap
- This level of detail is helpful in managing stakeholder expectations

**Skip when:**
- Confidence information alone provides sufficient insight

### Confidence

A percentage or visual indicator attached to roadmap columns or individual items representing the team's certainty that they will deliver on those items within the stated timeframe. Confidence is generally strongest for near-term items and wanes for distant ones. _source: ch09 §Communicating Confidence_

You should never have 100% confidence in anything on your roadmap, because the roadmap is a strategy tool and the future is inherently unpredictable. _source: ch09 §Communicating Confidence_

A **confidence separation line** is a visual divider within a roadmap column (typically "Now") above which the team is confident items will be addressed in the next release, and below which items are aspirational.

Assign decreasing confidence scores to roadmap columns as timeframes grow more distant — for example: 75% Now, 50% Next, 25% Later. Individual item confidence scores may vary within a column's overall range.

**Include when:**
- The roadmap includes specific timeframes spanning multiple future periods
- The development team frequently misses dates projected months in advance
- Stakeholders tend to assume that anything written down is a promise

**Skip when:**
- Stage-of-development information has already been included and provides enough insight

### Target Customers

The distinct customer types or personas that specific themes or features are intended to serve, often tagged or organized as swim lanes to ensure balanced coverage across user groups. Tag each theme or feature on the roadmap by the relevant customer type to ensure all roles or personas are addressed. _source: ch09 §Identifying Target Customers_

**Include when:**
- The product serves more than one type of customer
- Different themes target different customer segments
- It is important to achieve balance or highlight priority customer types

**Skip when:**
- The product vision and problem statement already make the target customer obvious

### Product Areas

Distinct functional components or sections of a product (e.g., user interface, platform, administration, APIs) that can be annotated on roadmap items to ensure all areas receive sufficient attention. _source: ch09 §Tagging Product Areas_

**Include when:**
- The product is large and complex with distinct components
- Individual product areas have separate business objectives
- It is important to show that work is being done to improve all areas

**Skip when:**
- A single team is developing all themes holistically with no division between product components
- Adding product areas would clutter communication to stakeholders

---

## Tier 3: Complementary Information (Context Only)

Complementary information is not formally part of a product roadmap but provides helpful context for stakeholders. The four categories are:

- **Project information** — timelines, milestones, or dependency data that contextualizes sequencing
- **Platform considerations** — technical environment constraints that shape delivery
- **Financial context** — budget, revenue targets, or cost structures that explain priority tradeoffs
- **External drivers** — regulatory requirements, competitive moves, or market events that influence timing

Complementary information lives outside the roadmap itself — in accompanying documents, appendix slides, or separate briefings. Mixing it directly into the roadmap increases noise and risks converting the roadmap into a project plan.

---

## Balancing the Tiers

When adding detail to your roadmap, strive for balance — too much information makes the roadmap difficult to read, while too little causes confusion and erodes stakeholder confidence. A well-balanced roadmap leads to improved communication, increased confidence, and ultimately better products. _source: ch09 §Secondary Components Summary: Strive for Balance_

Teams should experiment with which secondary components they include, because the right mix depends on the unique team, product, and ecosystem. Some components are useful at certain points in the product life cycle; others may not be. _source: ch09 §Secondary Components Summary: Strive for Balance_

When annotating roadmap items with product areas, target customers, and stage of development simultaneously, consider which labels are most important to stakeholders and avoid including all at once if it creates information overload.

---

## When to Use / When NOT to Use

**Use the primary components checklist every time** you create or review any product roadmap. There are no exceptions for internal drafts, early-stage products, or one-pagers — all five primary components must be present.

**Use secondary components selectively** when you have identified specific stakeholder confusion that a component would resolve. Do not add secondary components speculatively or to make the roadmap appear more thorough.

**Do not treat complementary information as roadmap content.** If project timelines or financial context are appearing inside your roadmap sections, the roadmap has drifted toward becoming a project plan or Gantt chart — an anti-pattern covered in [roadmap anti-patterns](../anti-patterns/roadmap-anti-patterns.md).

**Do not apply this component model to a release plan.** A release plan is a downstream artifact with different audiences and precision requirements. The roadmap components model is for strategic communication, not sprint-level planning.

---

## Code Examples

The following snippet shows how the primary components checklist and secondary component decision rules can be expressed as a structured review format.

```yaml
# Roadmap Component Review Checklist

primary_components:
  product_vision: required        # North Star; grounds all subsequent decisions
  business_objectives: required   # Measurable outcomes expressing the "why"
  themes: required                # Customer needs/problems, not features
  timeframes: required            # Now/Next/Later or quarters — no specific ship dates
  disclaimer: required            # "Subject to change without notice"

secondary_components:
  features_and_solutions:
    include_when:
      - theme is near shipment (pre-production or beta)
      - sales/marketing need concrete detail to prepare
      - carryover from previous roadmap
    placement: subthemes beneath parent theme — never alongside themes

  stage_of_development:
    labels_example: [discovery, design, prototyping, pre-production, beta]
    include_when:
      - stages take longer than roadmap timeframes
      - managing stakeholder expectations requires this detail

  confidence:
    rule: never 100%; decreases with timeframe distance
    example_scores: { Now: "75%", Next: "50%", Later: "25%" }
    include_when:
      - stakeholders treat roadmap items as firm commitments
      - development team frequently misses projected dates

  target_customers:
    include_when:
      - product serves more than one customer type
      - theme coverage balance across personas matters

  product_areas:
    include_when:
      - product has distinct components with separate business objectives
      - stakeholders need to see coverage across all areas

complementary_information:
  # Not part of the roadmap — provide separately
  categories: [project_info, platform_considerations, financial_context, external_drivers]
```

```markdown
<!-- Subtheme structure example -->

## Theme: Ensure seamless onboarding for new enterprise admins

_Business objective: Reduce time-to-first-value for enterprise accounts_
_Stage: Design | Confidence: 75% | Customer: Enterprise Admin_

### Subthemes (probable solutions)
- Guided setup wizard for SSO configuration
- Admin role permission templates
- In-app onboarding checklist with progress tracking
```

---

## Related References

- [Roadmap Definition](roadmap-definition.md) — What a roadmap IS and IS NOT; why confusing it with a project plan or Gantt chart undermines the component model
- [Themes and Needs](themes-and-needs.md) — Deep dive on expressing themes as customer needs; how to move from feature requests to outcome-oriented themes
- [Vision, Strategy, and OKRs](vision-strategy-okrs.md) — How product vision and business objectives are developed; the upstream inputs that anchor Tier 1 components
- [Bad Prioritization](../anti-patterns/bad-prioritization.md) — How weak primary components enable the bad prioritization methods that undermine roadmap credibility
- [Keeping the Roadmap Fresh](../topics/keeping-roadmap-fresh.md) — How component choices affect roadmap maintenance; when to revisit secondary components as the product evolves
- [Build Roadmap from Vision command](../../../../commands/build-roadmap-from-vision.md) — Guided workflow for constructing the primary component tier from vision down to themes
