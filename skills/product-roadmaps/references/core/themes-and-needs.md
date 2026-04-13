# Themes and Needs: Expressing Customer Outcomes on the Roadmap

## Problem Framing

The most common failure mode for roadmaps is that they fill up with features and solutions — "HTML5 redesign," "Twitter integration," "new dashboard" — rather than articulating why those things matter. Teams that operate this way can't answer the question "Why does this belong on the roadmap?" They accept requests at face value, ship deliverables, and still leave customers unsatisfied. This is the **Feature-Stuffed Roadmap** anti-pattern in action.

The fix is not to delete all the feature requests. It's to ask "Why?" until you reach the underlying customer need, then express that need as a **theme** — the organizing construct of an outcome-driven roadmap.

> "Every decision about a product should be rooted in customer needs. Staying focused here helps you avoid building things your customers don't need, forces efficiency, and ensures maximum value delivery." _source: ch08 §Expressing Customer Needs_

---

## What Themes and Subthemes Are

**Themes** are an organizational construct for defining what's important to your customers at the present time. A theme is a high-level customer need expressed at the roadmap level. _source: ch08 §Themes and Subthemes_

**Subthemes** are more specific or granular customer needs that sit beneath a theme. Themes can stand alone or represent a grouping of subthemes. _source: ch08 §Themes and Subthemes_

Themes are analogous to Agile epics, which break down into user stories. The canonical format for writing a theme is:

> **"Ensure [result] for [stakeholder]"**

Examples:
- Ensure seamless checkout for mobile shoppers
- Ensure reliable uptime for enterprise admins
- Ensure fast onboarding for new free-trial users

The format forces outcome language. "HTML5 redesign" is not a theme — it describes a solution. "Ensure the mobile experience is as good as desktop for users" is a theme — it describes the result the customer needs.

---

## Why Outcomes Over Outputs

> "The viability of a feature may shift dramatically, while the nature of an important customer problem will likely remain the same." _source: ch08 §Themes and Subthemes_

Organizing around themes rather than features preserves flexibility. When the product roadmap expresses customer needs, development teams retain freedom to find the best solution as circumstances change. Locking in a specific output ("HTML5 redesign") closes off alternatives before they've been evaluated.

> "Translating proposed outputs into themes leaves open the possibility there may be other — even better — ways to achieve the same outcomes." _source: ch08 §Themes Are About Outcomes, Not Outputs_

The roadmap should answer **why** — what needs and problems the product should solve. The release plan answers **how** — what will be built. Keeping these distinct prevents premature solution commitment and preserves flexibility for development teams. _source: ch08 §Expressing Customer Needs_

---

## Uncovering Themes via User Journey Mapping

A **User Journey Map** helps you understand every step a user takes when solving a problem: from the moment the user realizes the problem exists, through current methods they employ to address it, ending when the problem has been solved. _source: ch08 §User Journeys and Experience Maps_

Pain points and friction in the journey become the raw material for themes and subthemes. The workflow:

1. Map the full user journey from problem recognition to resolution.
2. Identify snags, friction, and unmet needs in the map.
3. Group related pain points into high-level themes and more granular subthemes.
4. Optionally, layer multiple journey maps into an **Experience Map** — a deeper visualization that plots multiple user journeys together to show how customer actions relate across customer types and phases, surfacing dimensions like emotions and technology needs. _source: ch08 §User Journeys and Experience Maps_
5. Express each theme using the format "Ensure [result] for [stakeholder]."
6. Validate each theme with a job story or user story (see next section).
7. Verify every theme maps to at least one strategic objective.

The **Opportunity-Solution Tree**, a visualization developed by Teresa Torres, is a complementary tool: it distinguishes solutions from the problems, needs, or opportunities they address while tying them together logically under a clear desired outcome. What Torres calls "opportunities" correspond to themes in this book's framework. _source: ch08 §Opportunity-Solution Trees_

---

## Validating Themes with Job Stories and User Stories

Every theme should be vetted and supported by job stories or user stories to cross-check and validate its importance to the customer and the value in solving for it. _source: ch08 §Using Job Stories and User Stories to Support Themes_

**Job Story** (from jobs-to-be-done methodology):
> "When [situation/motivation] I need [desire] So I can [result]"

**User Story** (from Agile):
> "As a [user type] I want [desire] So I can [result]"

These formats share the same three-part structure. The difference is perspective: job stories emphasize situation and motivation; user stories emphasize role. Either works for theme validation — the goal is to confirm that a real customer need exists before the theme earns a place on the roadmap.

---

## Transforming Feature Requests into Themes

When faced with a list of concrete deliverables or feature requests, ask "Why?" to discern the difference between the output requested and the outcome or result desired. _source: ch08 §Themes Are About Outcomes, Not Outputs_

The workflow:

1. For each proposed feature or output, ask: "Why is this important? What will result from doing it? How will it improve the customer's life or the company's fortunes?"
2. Restate the answer as a theme: "Ensure [result] for [stakeholder]."
3. Check that the theme describes an outcome, not the solution itself.
4. Support the theme with a job story or user story.
5. Link the theme to at least one strategic objective; if it cannot be linked, reconsider whether it belongs on the roadmap.

| Output (feature request) | Theme (outcome) |
|---|---|
| HTML5 redesign | Ensure mobile experience is as good as desktop for users |
| Twitter integration | Ensure users can share their activity with their social networks |
| Billing & payments API | Ensure reliable payment processing for enterprise customers |

The **Autopilot Feature Acceptance** anti-pattern is the failure to run this translation step — accepting requests without asking "Why?" or checking whether there is a bigger underlying problem that needs solving. _source: ch08 §Existing Product Needs_

---

## Functional and Technical (Nonfunctional) Needs

Not all themes are customer-facing. **Functional needs** are customer-focused; **technical or nonfunctional needs** are engineering-focused system and infrastructure needs. Both must be represented on the roadmap.

> "There are layers of functionality and operational tooling that need to be built into the backend in order for the product to actually function." _source: ch08 §System Needs_

System subthemes may describe infrastructure integration needs (e.g., "Billing & payments API integration") without prescribing a specific implementation — this still satisfies the rule that themes express needs, not solutions. Include system needs as subthemes under a relevant theme, or as a dedicated technical theme when the work is substantial.

---

## Linking Themes to Strategic Objectives

> "Every theme on your roadmap should relate to at least one of your strategic objectives. Linking themes to objectives keeps the team focused on the right things and avoids distraction; a theme that cannot be linked to any objective may not belong on the roadmap." _source: ch08 §Relating Themes Back to Your Objectives_

This is a hard rule: **every theme must map to at least one strategic objective**. A theme that fails this test is an **Orphaned Theme** — a signal that it was added reactively or that the roadmap has drifted from strategy.

The workflow for linking themes to objectives:

1. Review the list of strategic objectives (approved by all stakeholders).
2. Assign a distinct color to each objective.
3. Tag each theme and subtheme with the color(s) of the objective(s) it supports.
4. Create a **Theme Card** — a visual artifact representing the theme on the roadmap, with a color-coded bar at the top identifying the business objective(s) the theme relates to. _source: ch08 §Relating Themes Back to Your Objectives_
5. For any theme that cannot be linked to an objective, review it with the team: reframe it, move it to a later roadmap column, or remove it.

Note: a theme may link to more than one objective — this is encouraged.

> "Every time you plan a big update to your roadmap, you should review and reconsider your objectives. As time passes, strategic objectives will change due to business transitions or adequately addressed goals; each new roadmap version should start with revisiting product vision and objectives." _source: ch08 §Relating Themes Back to Your Objectives_

---

## When to Use / When NOT to Use

**Use themes as the primary roadmap organizing unit when:**
- Building any product roadmap, whether for a new product or an existing one.
- Receiving a list of feature requests or stakeholder demands that need to be evaluated.
- Rethinking an existing product where old habits have produced a feature-stuffed roadmap.
- Facilitating alignment conversations — themes expressed as outcomes are more durable than features, which become obsolete as priorities shift.

**Do NOT use theme format when:**
- Writing a release plan or sprint plan — those documents detail *how* to solve problems, not *what* problems to solve. Themes belong on the roadmap; specific deliverables belong on the release plan.
- Expressing an internal team process or organizational goal that has no connection to a customer need or strategic objective. If you can't write it in the "Ensure [result] for [stakeholder]" format and link it to an objective, it probably doesn't belong on the roadmap.
- A theme cannot be linked to any strategic objective after team review — in that case, remove or reframe it, don't force it.

---

## Code Examples

### Theme Format in Practice

```
Theme format:   Ensure [result] for [stakeholder]

Examples:
  Ensure seamless checkout for mobile shoppers
  Ensure reliable uptime for enterprise admins
  Ensure fast onboarding for new free-trial users
```

### Job Story Validation Template

```
Job Story format:
  When [situation/motivation]
  I need [desire]
  So I can [result]

Example:
  When I'm shopping on my phone and ready to purchase,
  I need to complete checkout without switching to a desktop,
  So I can buy immediately before losing interest.
```

### User Story Validation Template

```
User Story format:
  As a [user type]
  I want [desire]
  So I can [result]

Example:
  As a mobile shopper,
  I want to complete a purchase without re-entering my details,
  So I can buy quickly while I'm in the moment.
```

### Output-to-Theme Translation

```
Output (feature request)        → Theme (outcome)
────────────────────────────────────────────────────────────────
HTML5 redesign                  → Ensure mobile experience is as
                                   good as desktop for users
Twitter integration             → Ensure users can share activity
                                   with their social networks
Billing & payments API          → Ensure reliable payment
                                   processing for enterprise users
```

### Theme Card Structure (text representation)

```
┌─────────────────────────────────────────────────┐
│  ██ Objective: Grow enterprise revenue           │  ← color-coded bar
├─────────────────────────────────────────────────┤
│  Theme: Ensure reliable payment processing       │
│         for enterprise customers                 │
│                                                  │
│  Subtheme: Billing & payments API integration    │
│  Subtheme: Invoice management for admins         │
└─────────────────────────────────────────────────┘
```

---

## Related References

- [Roadmap Components](roadmap-components.md) — Covers where themes fit in the three-tier component model (primary, secondary, process), and how timeframes (Now / Next / Later) frame theme placement.
- [Vision, Strategy, and OKRs](vision-strategy-okrs.md) — Covers strategic objectives and OKRs that themes must link back to; themes without an objective link cannot remain on the roadmap.
- [Gathering Inputs](gathering-inputs.md) — Covers the pre-roadmap research that surfaces customer needs: product life cycle analysis, market environment, and existing customer feedback sources.
- [Prioritization Frameworks](../patterns/prioritization-frameworks.md) — Once themes are defined, these frameworks (Critical Path, Kano Model, Desirability / Feasibility / Viability, ROI Scorecard, MoSCoW) determine which themes get prioritized in Now vs. Next vs. Later.
- [Bad Prioritization Anti-Patterns](../anti-patterns/bad-prioritization.md) — Covers the failure modes that occur when teams skip theme translation and prioritize raw feature requests directly.
- [Transform Features to Themes command](../../../../commands/transform-features-to-themes.md) — Step-by-step command for running the output-to-theme translation workflow with a list of feature requests.
