---
description: Construct a product roadmap skeleton from company vision down to themes
argument-hint: "[product name or vision statement]"
---

# Build Roadmap From Vision

**Purpose:** This command walks you through constructing a complete roadmap skeleton — from company vision through business objectives, themes, and Now / Next / Later timeframes — producing a structured draft with all five required primary components. Use it when starting a new product roadmap or rebuilding an existing one from scratch.

## When to use

- You are creating a new product roadmap and have no skeleton yet
- An existing roadmap has drifted into a feature-and-dates list and needs to be rebuilt around outcomes
- A new product vision or company vision has been adopted and the roadmap must be re-grounded
- The roadmap is missing one or more of the five primary components (vision, business objectives, themes, timeframes, disclaimer)

---

## Steps

### 1. Gather context

Ask the user for the following if not already provided:

- The **company vision** statement (or a description of it)
- The **product name** and what it does at a high level
- Any existing business objectives, OKRs, or strategy documents — ask the user to paste them or point to a file
- Any known customer research, surveys, or problem statements

If the user points to files, use the Read tool to load them. If multiple files exist, use Glob to locate them and Read each one.

---

### 2. Validate or create the product vision

Using the Value Proposition Template (adapted from Geoffrey Moore's *Crossing the Chasm*), fill in or evaluate the product vision:

```
For [target customer]
Who [target customer's needs]
The [product name]
Is a [product category]
That [product benefit / reason to buy]
Unlike [competitors]
Our product [differentiation]
Supports our [objective(s)]
```

Then compress it into a single vision sentence:

> "A world where the [target customer] no longer suffers from the [identified problem] because of [product] they [benefit]."

Gut-check the result against three questions:
- Does it name the target customer?
- Does it name the problem solved?
- Does it state why the customer benefits?

If the organization has multiple products, confirm the product vision is derived from and supportive of the corporate vision (rule: `ch07.rule.product-vision-tied-to-company-vision`).

Present the draft product vision to the user and ask for confirmation or corrections before proceeding.

---

### 3. Define business objectives as OKRs

Ask the user to identify the business objectives this product must advance. Apply the following rules:

- Keep objectives to **fewer than five** (`ch07.rule.okr-fewer-than-five`)
- Frame each objective as a qualitative goal; pair it with 2–3 quantitative key results
- Focus on **outcomes** (the difference made) rather than **outputs** (features delivered) — avoid the **Feature Factory** anti-pattern described in [`bad-prioritization.md`](../skills/product-roadmaps/references/anti-patterns/bad-prioritization.md)
- Use the 10 Universal Business Objectives as a reference lens: Sustainable Value (support core value, create barriers to competition), Growth (grow market share, fulfill demand, develop new markets, improve recurring revenue), and Profit (support higher prices, improve lifetime value, lower costs, leverage existing assets)

If the user cannot articulate objectives, prompt: "Ask 'why?' about each proposed theme or feature until you reach a universal business objective."

Output a draft OKR table:

| # | Objective | Key Result 1 | Key Result 2 | Key Result 3 |
|---|-----------|-------------|-------------|-------------|
| 1 | …         | …           | …           | …           |

---

### 4. Uncover customer needs and derive themes

Using any customer research provided (surveys, interviews, problem statements), identify the most important problems customers face in achieving their goal.

For each problem, translate it into a theme:

- Frame every theme as a **customer need or outcome**, using the phrasing: "Ensure [result] for [stakeholder]"
- Map the problem to the theme explicitly (e.g., problem: "hoses kink" → theme: "indestructibility")
- Do **not** express themes as features or deliverables — see [`themes-and-needs.md`](../skills/product-roadmaps/references/core/themes-and-needs.md) for the full methodology

If the user provides a raw feature list, run the transform-features-to-themes workflow: for each feature, ask "Why does the customer need this?" until you reach an outcome. See [`transform-features-to-themes.md`](transform-features-to-themes.md).

Verify each theme maps to at least one business objective from Step 3. Flag any theme that does not.

---

### 5. Prioritize and order themes

Ask the user to rank themes by priority. If they are unsure, recommend a prioritization framework from [`prioritization-frameworks.md`](../skills/product-roadmaps/references/patterns/prioritization-frameworks.md) — for example:

- **Critical Path** — which themes must be completed before others can begin?
- **Kano Model** — which themes are basic needs vs. delighters?
- **ROI Scorecard** — which themes deliver the most value relative to effort? (see [`build-roi-scorecard.md`](build-roi-scorecard.md))

Output a ranked theme list with the objective each theme supports.

---

### 6. Assign themes to Now / Next / Later timeframes

Organize themes into three broad timeframes. Use **Now / Next / Later** — never "short-term / medium-term / long-term."

- **Now** — highest-priority theme(s); the product is nearly ready for shipment; specific features or solutions may be listed here (`ch05.rule.features-only-for-near-term-themes`)
- **Next** — themes in active development; focus on the problem expressed in the theme, not specific features
- **Later** — themes planned but not yet in development; problem statement only

**Do not include specific ship dates** (`ch05.rule.no-specific-ship-dates`). Use broad calendar quarters only if the organization requires them; otherwise leave as Now / Next / Later. A "Future" bucket may be added for themes beyond the current planning horizon.

Output a timeframe table:

| Timeframe | Theme | Customer Need | Objective(s) | Notes |
|-----------|-------|--------------|--------------|-------|
| Now       | …     | …            | …            | …     |
| Next      | …     | …            | …            | …     |
| Later     | …     | …            | …            | …     |

---

### 7. Add the disclaimer

Append the following disclaimer to the roadmap draft (`ch05.rule.disclaimer-required`):

> **Disclaimer:** This roadmap represents our current thinking and is subject to change without notice. Dates, themes, and priorities may shift as we learn more from customers and the market.

Remind the user: large public companies or regulated industries may require a more elaborate disclaimer — consult finance or legal regarding your organization's policy.

---

### 8. Identify secondary components to add (optional)

Ask the user whether any stakeholders need additional context. Secondary components to consider:

- Features and solutions (Now themes only)
- Stage of development (discovery, design, development, etc.)
- Confidence level per theme
- Target customer segments per theme
- Product areas or platform tags

Add only those that address a specific stakeholder concern — do not add all of them by default. See [`roadmap-components.md`](../skills/product-roadmaps/references/core/roadmap-components.md) for the full secondary component reference.

---

### 9. Flag complementary information for separate conversations

Note any of the following that exist but should **not** appear on the roadmap itself:

- Project plans, sprint schedules, or Gantt details
- Platform or architecture considerations
- Financial models or cost projections
- External regulatory or market drivers

These are complementary items — prepare them separately for targeted stakeholder conversations. See [`presenting-and-sharing.md`](../skills/product-roadmaps/references/patterns/presenting-and-sharing.md) for audience-specific framing guidance.

---

## Output

Produce a structured roadmap draft containing all five primary components (`ch05.rule.primary-components-checklist`):

1. **Product Vision** — single vision statement derived from the Value Proposition Template
2. **Business Objectives** — OKR table (fewer than 5 objectives, each with key results)
3. **Themes** — outcome-oriented, mapped to objectives
4. **Timeframes** — Now / Next / Later table (no specific ship dates)
5. **Disclaimer** — subject-to-change notice

### Write artifacts using the standard templates

Write the draft to disk in the user's current working directory using the plugin's templates:

- Read [`../skills/product-roadmaps/templates/roadmap.md`](../skills/product-roadmaps/templates/roadmap.md) and write a filled-in copy to `./roadmap.md`. Populate `vision`, `objectives`, `disclaimer`, `prioritization_method`, `status: draft`, `last_reviewed` (today), and `refresh_cadence`.
- Read [`../skills/product-roadmaps/templates/theme.md`](../skills/product-roadmaps/templates/theme.md) and write one file per theme to `./themes/<slug>.md`. Slug = kebab-case of the theme's "Ensure …" name. Populate `id` (TH-001, TH-002, …), `name`, `timeframe` (Now / Next / Later only), `customer_need`, `linked_objectives` (non-empty — every theme must link to at least one objective), `confidence` (integer 0–99, never 100), `created_on`, `last_updated`.
- Cross-link: the `## Themes — Now / Next / Later` tables in `roadmap.md` must link to each `themes/<slug>.md` file.

If these files already exist, ask the user whether to overwrite, merge, or write to a different path.

---

## Verify

Confirm the roadmap draft meets these criteria before delivering:

- [ ] All five primary components are present
- [ ] Product vision addresses: target customer, problem solved, and benefit
- [ ] Fewer than five OKR objectives
- [ ] Every theme maps to at least one objective
- [ ] Every theme is framed as a customer outcome, not a feature
- [ ] Specific ship dates are absent (Now / Next / Later only)
- [ ] Features appear only in Now themes (not Next or Later)
- [ ] Disclaimer is present

If any check fails, return to the relevant step and correct before presenting the final output.

---

## Notes

- If the user has an existing roadmap that is date-and-feature-driven, this command will surface the **Feature Factory** anti-pattern — see [`roadmap-anti-patterns.md`](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md) for the full catalogue of anti-patterns to avoid
- For stakeholder alignment after the skeleton is built, run [`run-shuttle-diplomacy.md`](run-shuttle-diplomacy.md)
- For roadmap health scoring after the draft is complete, run [`assess-roadmap-health.md`](assess-roadmap-health.md)
- Vision and OKR foundations are covered in depth at [`vision-strategy-okrs.md`](../skills/product-roadmaps/references/core/vision-strategy-okrs.md)
