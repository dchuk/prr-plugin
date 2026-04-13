---
description: Build an ROI prioritization scorecard for roadmap themes or features
argument-hint: "[theme or feature list, or file path]"
---

# Build ROI Scorecard

**Purpose:** Construct a rigorous ROI Scorecard that ranks roadmap items by Priority Score using the formula **Value / Effort × Confidence**. Use this command whenever you have a long list of feature ideas, initiatives, or themes and need an objective, defensible ranking to share with stakeholders.

**When to use:**
- You have more ideas than capacity and need to cut ruthlessly
- Stakeholders are lobbying for pet features with no shared scoring method
- You are translating a theme list into a sequenced roadmap and need prioritization evidence
- You want to guard against [bad prioritization anti-patterns](../skills/product-roadmaps/references/anti-patterns/bad-prioritization.md) such as gut instinct or popularity-based ranking

---

## Steps

1. **Collect the items to score.**
   - Ask the user: "Paste or describe the features, initiatives, or themes you want to prioritize. Confirm whether these are all the same level (all themes, or all features) — per the book's rule, compare only like things."
   - If a file path was provided as an argument, use the Read tool to load it; otherwise work from the pasted list.
   - Remind the user: do not mix themes with features in the same scorecard run.

2. **Identify organizational goals (2–4).**
   - Ask the user to name 2–4 current strategic goals, for example: grow new customer revenue, increase lifetime value, enter a new market, reduce churn.
   - If the user has an existing vision or OKR document, use the Read tool or Grep to locate it in the repo.
   - Label columns **OG1, OG2, …** in the scorecard.
   - Cross-reference [vision-strategy-okrs](../skills/product-roadmaps/references/core/vision-strategy-okrs.md) if the user needs help articulating goals.

3. **Identify critical customer needs (1–3).**
   - Ask the user to name the primary customer needs the product must address.
   - Frame each need as an outcome: "Ensure [result] for [stakeholder]."
   - Label columns **CN1, CN2, …** in the scorecard.
   - Cross-reference [themes-and-needs](../skills/product-roadmaps/references/core/themes-and-needs.md) for guidance on uncovering needs.

4. **Set the deliberate-imprecision value scale.**
   - Explain to the user: "We use a coarse scale to keep discussion on relative order, not precise forecasts."
   - Apply the scale: **0** = no effect, **1** = some positive effect, **2** = large positive effect. Negative values are allowed when an idea actively harms a goal.
   - Remind the user: use **0** (not just "low") when an item helps not at all on a given goal.

5. **Score each item against every CN and OG column.**
   - Work through each item row by row. For each cell ask: "Does this idea move the needle on this customer need / organizational goal? Score 0, 1, or 2."
   - If the user is unsure about a score, default to 0 rather than inflating.
   - Record all scores in a markdown table (see Output section below).

6. **Calculate Value for each item.**
   - Value = sum of all CN and OG scores for that row.
   - Show the arithmetic inline so the user can verify.

7. **Estimate effort using T-shirt sizing.**
   - Apply: XS = 1, S = 2, M = 3, L = 4, XL = 5.
   - Ask the user (or product manager) to assign a T-shirt size first, then note: "Get an engineer to sanity-check these estimates before finalizing."
   - Record the numeric Effort value in the table.

8. **Assign a confidence percentage.**
   - For each item, ask: "How confident are you that this idea will deliver the expected value and that the effort estimate is accurate? Express as a percentage (0–100)."
   - Common drivers of low confidence: unclear requirements, untested technology, dependency on a third party.
   - Record as a decimal (e.g., 80% → 0.80).

9. **Calculate Priority Score.**
   - Priority Score = (Value / Effort) × Confidence
   - Compute this for every row and add a **Priority Score** column.

10. **Sort and rank.**
    - Sort all rows by Priority Score descending.
    - Assign rank 1 to the highest score.

11. **Annotate dependencies, constraints, and pre-existing commitments.**
    - Ask the user: "Are there any items with hard dependencies on each other, resource constraints, or promises already made to customers or executives?"
    - Record these as margin annotations (a **Notes** column or a separate annotations list) — per the book, these affect *scheduling*, not the underlying priority order.

12. **Apply MoSCoW if needed.**
    - If the user wants to communicate release criteria to an engineering team, offer to classify the ranked list into Must Have / Should Have / Could Have / Won't Have buckets.
    - Verify that no Won't Have item is a dissatisfier or critical path item before finalizing.
    - See [prioritization-frameworks](../skills/product-roadmaps/references/patterns/prioritization-frameworks.md) for full MoSCoW guidance.

---

## Verify

Confirm the scorecard is complete and coherent by checking all of the following:

- [ ] Every row has a score for every CN and OG column (no blanks).
- [ ] The Value column equals the sum of all CN and OG scores for that row.
- [ ] Every Effort value is a number 1–5 (T-shirt sizes mapped correctly).
- [ ] Every Confidence value is between 0 and 1 (not a raw percentage > 1).
- [ ] Priority Score = (Value / Effort) × Confidence for each row — spot-check at least three rows.
- [ ] Only like items are compared (no themes mixed with sub-features).
- [ ] Dependencies and pre-existing commitments are in the Notes column, not used to change priority scores.
- [ ] The sorted ranking is descending by Priority Score.

---

## Output

Produce a markdown table with the following columns:

| Rank | Item | CN1 | CN2 | OG1 | OG2 | Value | Effort (T-shirt) | Effort # | Confidence | Priority Score | Notes |
|------|------|-----|-----|-----|-----|-------|-----------------|----------|------------|----------------|-------|

Below the table, include a **Summary** paragraph that calls out:
- The top 3 items and why they scored highest
- Any items where low confidence materially suppressed an otherwise high Value/Effort ratio (flag these as worth de-risking)
- Any dependency chains from the Notes column that affect sequencing

### Write the scorecard artifact

Read the scorecard template at !`echo ${CLAUDE_PLUGIN_ROOT}/skills/product-roadmaps/templates/roi-scorecard.md` and write a filled-in copy to `./artifacts/scorecard-YYYY-MM-DD.md` (use today's date; if the file already exists, append `-v2`, `-v3` suffixes). Populate `scored_on`, `strategic_goals` (OBJ-* IDs if a `roadmap.md` is present, otherwise the raw goal names), `customer_needs` (CN-* IDs and names), `items_scored` (theme IDs TH-00N when scoring themes, otherwise raw item names), and the full scoring table.

### Update theme files with the ROI score

For each item that corresponds to an existing theme file at `./themes/<slug>.md`, use Edit to populate the `roi_score:` block in its frontmatter:

```yaml
roi_score:
  value: <sum of CN+OG columns>
  effort: <T-shirt letter>
  effort_number: <1–5>
  confidence: <0.0–1.0 decimal>
  priority_score: <value / effort × confidence>
  scored_on: YYYY-MM-DD
```

Also update `last_updated` to today's date and append a line to the theme's `## Change log`: `- YYYY-MM-DD — Scored via ROI scorecard: priority <score>.`

If any item in the scorecard has no corresponding theme file, flag it in the summary — it likely needs `/prr:transform-features-to-themes` first.

---

## Notes

- The ROI Scorecard is one of five prioritization frameworks covered in the book. If your items are for an MVP, consider running the Critical Path workflow first — it may reduce your list before scoring. See [prioritization-frameworks](../skills/product-roadmaps/references/patterns/prioritization-frameworks.md).
- If stakeholders push back on scores, the **Deliberate Imprecision** principle is your defense: coarse scales (0/1/2) surface disagreements about relative value faster than precise estimates, and that conversation is the point.
- Guard against **Shiny Object Syndrome** — if every item scores high, revisit the OG columns and ask whether the goals are truly differentiated. See [roadmap-anti-patterns](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md).
- After prioritization, use [run-shuttle-diplomacy.md](run-shuttle-diplomacy.md) to align stakeholders on the resulting ranking before committing to a roadmap.
