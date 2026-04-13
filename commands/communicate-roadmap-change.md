---
description: Draft a stakeholder communication for a roadmap change
argument-hint: "[brief description of what changed]"
---

# Communicate Roadmap Change

## Purpose

Draft a clear, structured communication for any planned or unplanned roadmap update. Use this command whenever the roadmap shifts — from a minor date slip to a full strategic pivot — to ensure stakeholders understand the why, what, and when before they see the new artifact.

## When to use

- A planned roadmap review cycle has produced meaningful changes to themes, timelines, or priorities
- An unplanned event (competitor move, regulatory change, strategy shift) forces an off-cycle update
- A strategic pivot requires revisiting everything from the product vision down
- A special request was accepted and the roadmap was adjusted to accommodate it
- You need to align dev team, executives, sales/marketing, and customers on the same change with audience-appropriate depth

---

## Steps

### 1. Identify the depth of the change

Ask the user: *What changed?* Categorize the change into one of three levels:

- **Small** — a single subtheme moved, a date adjusted, or a minor scope swap
- **Broad-reaching** — one or more themes shifted, reprioritized, or removed
- **Fundamental (pivot)** — vision, strategy, or key business objectives have changed

> Per `ch13.principle.depth-determines-how-far-back`: the deeper the change, the further back in the creation process you need to go to revisit assumptions.

If the change is **fundamental**, warn the user: this workflow covers communication; the user should also run `/build-roadmap-from-vision` to rebuild the underlying roadmap artifact before socializing.

---

### 2. Draft the WHY

Using the user's description of the change, write a 2–3 paragraph **Why** section that:

1. Names the market condition, competitive factor, customer insight, or strategic shift that necessitated the change
2. Frames the change as producing a better future for the company, customers, and stakeholders given the new reality — not as a failure or reversal
3. References what is **not** changing (typically the product vision and long-term strategy) to anchor the audience and demonstrate continuity

> Per `ch13.principle.communicate-the-why`: "The reasons change is occurring may be the most important part of a roadmap update, and yet this information is often left out."

> Per `ch13.principle.embrace-change-dont-hide-it`: "Don't shy away from discussing change — embrace it and get everyone on board."

---

### 3. Draft the WHAT

Write a **What Changed** section that specifies:

- Which themes, subthemes, features, or timelines are affected
- What was removed, deferred, accelerated, or added
- For a pivot: what is explicitly changing vs. what is explicitly staying the same

If the user has not provided this detail, ask: *"Can you list the specific items on the roadmap that changed and how each changed?"*

---

### 4. Draft the WHEN

Write a **When** section that covers:

- Updated Now / Next / Later placement for any moved items
- Any hard delivery dates or milestones that are affected
- The date stakeholders can expect to receive the updated clean roadmap artifact

---

### 5. Generate audience-tailored versions

Produce three variants of the communication, using the rules from ch12:

**Development team**
- Include updated stage of development for affected themes
- Surface any new technical debt, dependency changes, or scalability expectations introduced by the change
- Be specific about what is added, removed, or resequenced in the backlog horizon

**Executives / board**
- Lead with vision, strategy, and the high-level theme impact only — `ch12.rule.executives-high-level-only`
- Do not lead with feature-level detail; note that details are available on request
- Use emotion, data, and stories to give meaning to the prioritization decision — `ch12.rule.presentation-emotion-data-stories`

**Sales / marketing (and external customers)**
- For sales/marketing: add confidence percentages to any affected near-term items; use hedging language ("likely," "probable," "tentative") — `ch12.rule.add-confidence-for-sales-marketing`, `ch12.rule.use-hedging-language-with-sales-marketing`
- For customers: simplify further — focus exclusively on the value customers should anticipate, strip all internal details — `ch12.rule.customer-roadmap-value-focused`

---

### 6. Prepare the annotated roadmap artifact instructions

Output a short checklist the user should apply to the roadmap artifact before the review meeting:

- [ ] Mark changed items visually (colors, arrows, callout boxes, or pop-ups) so reviewers can immediately see what is new
- [ ] Annotate each changed item with a one-line reason
- [ ] Date-stamp the artifact with today's review date
- [ ] Prepare a clean copy (no markup) to share externally after the review meeting is complete

---

### 7. Write the change-communication artifact

Read [`../skills/product-roadmaps/templates/change-communication.md`](../skills/product-roadmaps/templates/change-communication.md) and write a filled-in copy to `./artifacts/change-YYYY-MM-DD-<slug>.md` (slug = short kebab-case description of the change, e.g. `defer-reporting`, `pivot-to-enterprise`). Populate `change_date`, `change_depth` (small / broad / fundamental), `affected_themes` (theme IDs from `./themes/`), `audiences`, and all body sections drafted in steps 2–6.

Then update the affected files:

- For each theme in `affected_themes`, use Edit to update the theme file's `timeframe`, `confidence`, and `last_updated` frontmatter, and append a line to its `## Change log`: `- YYYY-MM-DD — <what changed> (see artifacts/change-YYYY-MM-DD-<slug>.md).`
- If `./roadmap.md` exists, update its Now/Next/Later tables to reflect moves, bump `last_reviewed`, and append to its `## Change log`.

### 8. Plan socialization

Remind the user of the core rule: `ch13.rule.socialize-change-like-new-roadmap` — **socialize roadmap changes the same way you would socialize a new roadmap created from scratch**, except for minor changes (small scope or date adjustments) that only affect the release or project plan.

Generate a brief socialization checklist:
- [ ] Schedule 1:1 or small-group buy-in conversations before the all-hands review (see [alignment-and-buyin](../skills/product-roadmaps/references/patterns/alignment-and-buyin.md))
- [ ] Share the annotated artifact in the review meeting; collect and address objections
- [ ] Distribute the clean updated artifact after the meeting with a date stamp
- [ ] Log any outstanding concerns for the next review cycle

---

## Verify

The communication is complete when all of the following are true:

1. **WHY is explicit** — a reader unfamiliar with the change can explain in one sentence why the roadmap shifted
2. **WHAT is specific** — every changed item is named; no vague references to "some features moved"
3. **WHEN is concrete** — updated Now / Next / Later placement is stated; a date for the clean artifact distribution is set
4. **Three audience variants exist** — dev team, executive, and sales/customer versions each exist and differ in depth
5. **Annotated artifact checklist is ready** — the user knows exactly what to mark up before the review meeting
6. **Socialization plan is actionable** — at minimum one meeting or distribution action is scheduled

---

## Notes

- For **small changes** (single date slip, minor scope swap): per `ch13.rule.socialize-change-like-new-roadmap`, full socialization may not be required — confirm with the user whether a brief Slack update or email is sufficient
- For **strategic pivots**: do not finalize the communication until the roadmap artifact itself has been rebuilt from the vision down; run `/build-roadmap-from-vision` first
- For **special requests** that triggered the change: use `/evaluate-special-request` to ensure the three qualifying questions were answered before drafting the communication
- The iron triangle trade-off (schedule / scope / resources / quality) should be named explicitly in any communication that involves a delay or scope change; see [keeping-roadmap-fresh](../skills/product-roadmaps/references/topics/keeping-roadmap-fresh.md) for iron triangle guidance
- Audience-specific presentation guidance lives in [presenting-and-sharing](../skills/product-roadmaps/references/patterns/presenting-and-sharing.md)
- Anti-patterns to avoid during change communication include the **Feature Factory** and **Roadmap as Contract** patterns; see [roadmap-anti-patterns](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md)
