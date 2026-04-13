# Gathering Inputs for Your Roadmap

## Problem Framing

The most common mistake a product team makes before building a roadmap is skipping the research phase entirely. Without gathered inputs, the roadmap becomes a projection of assumptions — feature lists disconnected from validated customer needs, business context that only the product manager holds, and a direction no one can trace back to a real problem.

The book's diagnosis is direct: "Trying to roadmap without deep empathy for the customer will invariably send you down the wrong path, waste time, and eventually lead to product failure." _source: ch06 §Gathering Input from Your Customers_

The fix is a structured gathering phase covering four areas before a single theme is written: where your product sits in its life cycle, the business and market environment, your customers (roles, types, and personas), and your stakeholders.

---

## Product Life Cycle Stages

The five primary phases a product moves through are **New, Growth, Expansion, Harvesting, and End of Life**. Each phase demands a different roadmapping focus and carries different levels of risk and uncertainty. _source: ch06 §Understand Where Your Product Is in Its Life Cycle_

| Phase | Roadmapping focus |
|---|---|
| New | Heavy assumption-testing; high uncertainty |
| Growth | Scaling validated features; reducing churn |
| Expansion | New markets or segments; moderate risk |
| Harvesting | Maximizing existing value; minimal new investment |
| End of Life | Winding down deliberately with a sunset roadmap |

### Sunsetting Products Still Need a Roadmap

A product in the End-of-Life phase being deliberately wound down and taken off the market still requires strategy, planning, and strong stakeholder communication. A roadmap remains valuable here because winding down requires alignment across stakeholders just as launching does. _source: ch06 §End-of-Life Phase_

---

## Market and Business Environment Analysis

Every member of the product team should have a basic understanding of the business environment, not just the product manager. When only the product leader understands the business, designers and engineers operate with a faulty map and risk ending up in the wrong place. _source: ch06 §Understand Your Ecosystem_

**Rule:** You must be able to complete a business model canvas — Lean Canvas or Business Model Canvas — at a basic level before building your roadmap.

### Lean Canvas vs. Business Model Canvas

The choice between the two templates follows a clear decision rule:

- **Lean Canvas** (Ash Maurya) — recommended for startups or new products. Guides teams through problem/solution, value proposition, unfair advantage, key metrics, and revenue model.
- **Business Model Canvas** (Alex Osterwalder) — recommended for existing products or growing businesses. Covers customer segments, distribution channels, costs, and key partners.

If your team cannot fill in either canvas at even a basic level, the roadmap will be built on gaps.

---

## Customer Understanding

### The Core Principle

"Every item on your product roadmap should address an actual customer need, requiring intimate knowledge of and empathy for your customers." _source: ch06 §Gathering Input from Your Customers_

The book distinguishes three distinct customer documentation tools that are frequently conflated. Treating them as interchangeable produces imprecise customer understanding and weakens every roadmap decision downstream.

### User Roles

A **user role** describes the primary action or job function taken by a particular user. It focuses on jobs and functions — the "who/do" — not on personality traits or permissions. _source: ch06 §Customer Roles_

Example user roles: Reviewer, Approver, Content Creator, Report Consumer.

### User Types

A **user type** addresses how a user will interact with a product or defines a user's permissions in relation to the product. Examples: End user, General admin, Master admin, Manager, Operator, Viewer. _source: ch06 §User Types_

User types answer "what access level does this person have?" — a different question from roles or personas.

### Personas

A **persona** is a representation of a user that embodies the characteristics, feelings, and preferences of a user set. Personas deal with softer characteristics and help teams empathize with buyers and users by seeing the problem from their point of view. _source: ch06 §Roles Versus Personas_

**Rule:** Maintain separate definitions — use roles to categorize functional jobs, and personas to capture softer characteristics, feelings, and preferences that drive empathy. Documents that use "role" and "persona" interchangeably, or personas that lack emotional or motivational attributes, are a signal that conflation has occurred.

### Users vs. Buyers

Explicitly differentiate between users (those who use the product) and buyers (those who purchase it). In B2B and enterprise contexts these are almost always different people — a VP of Sales may purchase on behalf of sales reps who never touched the buying decision. In B2C contexts the buyer and user are often the same individual, so the distinction matters less there. _source: ch06 §Users Versus Buyers_

### The Customer Development Model

Steve Blank's four-step model — **Customer Discovery, Customer Validation, Customer Creation, and Company Building** — sequences exploration of the problem, solution validation, and scaling. The model's core instruction: get out of the building to validate problems before building solutions. _source: ch06 §Define the Problem and the Expected Outcome of the Solution_

**Rule:** Interact directly with target customers to understand what they're thinking, feeling, seeing, hearing, saying, and doing before roadmapping. _source: ch06 §Roles Versus Personas_

---

## Stakeholder Identification

The roadmapping process needs to incorporate collaboration from all key stakeholders; no product can be built or grown in a vacuum. Involving stakeholders improves product quality and makes the road to building it smoother. _source: ch06 §Gathering Input from Your Stakeholders_

**Rule:** In the beginning of the roadmapping process, identify who your stakeholders are and the role they will play in the development of the product.

The **product core** — the small group typically comprising a product manager, designers, and engineers directly responsible for designing, building, shipping, and/or maintaining a particular product or version — is the innermost stakeholder circle. Stakeholder mapping expands outward from there to include sales, marketing, support, legal, executives, and in some cases customers themselves.

---

## Problem Before Features

"Seasoned product pros focus on problems and expected outcomes rather than features. Novices focus on features; the best product pros ask 'If we solve that problem, what's the outcome we want to see?'" _source: ch06 §Define the Problem and the Expected Outcome of the Solution_

This principle cuts directly against the **Feature-First Thinking** anti-pattern: focusing on features rather than the underlying customer problems and desired outcomes. The signals are recognizable — a roadmap containing feature lists with no stated problem or outcome, or a team debating which features to add without first validating the underlying problem.

The fix is structural: reframe every roadmap item as a problem to be solved and articulate the expected outcome if that problem is resolved.

---

## Keeping Inputs Fresh

Inputs to the roadmap should be constantly refreshed to avoid making too many assumptions and mistakes. Without a constant refresh of context, product teams risk building based on stale or incomplete information. The more information you have about the space in which you are operating, the more effective you will be as a product leader. _source: ch06 opening paragraphs, §Summary_

---

## When to Use / When NOT to Use

**Apply this gathering phase:**
- At the start of any roadmapping effort, including the very first roadmap and any full relaunch
- When the team cannot trace existing roadmap items back to validated customer needs
- When entering a new life cycle phase (especially New → Growth or Expansion → Harvesting)
- When entering a new market segment or acquiring a new customer type
- When significant time has passed since the last customer or market input refresh

**Do not skip or abbreviate this phase:**
- Even for experienced teams with an existing product — context drifts; the inputs from two years ago may no longer reflect reality
- Even in the End-of-Life phase — sunsetting still requires stakeholder alignment and planning

**The gathering phase is less urgent (not skippable) when:**
- You are making a minor roadmap update within an already-validated strategic context and the underlying business model and customer base are unchanged

---

## Code Examples

Business model canvas completion check — applied before beginning roadmapping:

```
LEAN CANVAS (New / startup products)
─────────────────────────────────────────────────────────
Problem          │ Solution         │ Unique Value Prop
                 │                  │
─────────────────┤                  ├─────────────────────
Customer Segments│ Key Metrics      │ Unfair Advantage
                 │                  │
─────────────────┴──────────────────┴─────────────────────
Channels
─────────────────────────────────────────────────────────
Revenue Streams                     │ Cost Structure
─────────────────────────────────────────────────────────

Rule: If your team cannot populate this at a basic level,
stop roadmapping until the gaps are filled.
```

User role vs. user type vs. persona — kept as separate documents:

```
USER ROLE (job / function)
  Content Creator — creates and publishes content in the system

USER TYPE (permissions / interaction mode)
  General Admin — full access except billing; can invite other users

PERSONA (characteristics / empathy)
  Maya, Marketing Manager
  - Feels overwhelmed when campaigns aren't tracked in one place
  - Motivated by visibility into campaign performance
  - Frustrated by tools that require IT involvement for every change
```

Lean Canvas vs. Business Model Canvas decision:

```
Is the product a startup or new product?
  YES → Lean Canvas (Ash Maurya)
  NO (existing product or growing business) → Business Model Canvas (Osterwalder)
```

---

## Related References

- [Roadmap definition and what it is NOT](roadmap-definition.md) — establishes the strategic framing that gathered inputs must feed into
- [Roadmap components](roadmap-components.md) — covers themes and timeframes that are built on top of the inputs gathered here
- [Themes and needs](themes-and-needs.md) — the next step after gathering inputs: converting validated customer problems into roadmap themes
- [Vision, strategy, and OKRs](vision-strategy-okrs.md) — the strategic context that shapes which customer problems are worth solving
- [Bad prioritization anti-patterns](../anti-patterns/bad-prioritization.md) — what goes wrong when teams prioritize without validated inputs
- [Transform features to themes command](../../../../commands/transform-features-to-themes.md) — apply the problem-before-features principle to an existing feature list
