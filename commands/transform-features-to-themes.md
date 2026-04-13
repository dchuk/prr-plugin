---
description: Transform feature requests into outcome-oriented roadmap themes
argument-hint: "[feature list or file path]"
---

# Transform Features to Themes

## Purpose

Convert a list of feature requests, stakeholder demands, or concrete deliverables into outcome-oriented roadmap themes by uncovering the underlying customer need behind each item. Use this command whenever your roadmap is drifting toward a feature list or when stakeholders hand you a backlog of requests rather than customer outcomes.

## When to use

- You have received a list of feature requests or concrete deliverables from stakeholders, sales, or engineering
- Your current roadmap items look like solutions ("HTML5 redesign", "new dashboard") rather than outcomes
- You are starting a new roadmap and need to structure raw inputs into themes
- A roadmap review has flagged the **Feature Factory** anti-pattern — see [roadmap-anti-patterns](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md)

## Steps

1. **Collect the feature list.** If the user provided a file path, Read that file. If they pasted items inline, work from the conversation. List each feature or deliverable as a numbered item so none are missed.

2. **For each feature, ask "Why?"** Apply the rule from the book: *"Ask 'Why?' to discern the difference between the output requested and the outcome or result desired."* For each item, reason through:
   - Why is this important?
   - What will result from doing it?
   - How will it improve the customer's life or the company's fortunes?
   Record the answer as a candidate outcome statement.

3. **Reframe each item as a theme.** Express the outcome using the canonical theme format: **"Ensure [result] for [stakeholder]"**. For example:
   - "HTML5 redesign" → "Ensure mobile experience is as good as desktop for users"
   - "Admin bulk-export tool" → "Ensure administrators can act on data without manual effort"
   Check that the new statement describes a customer need or problem, not the solution itself. If it still sounds like a solution, ask "Why?" again.

4. **Identify subthemes where needed.** If a theme is very broad, Grep the original list for related features that cluster under it. Express each cluster as a subtheme — a more granular customer need beneath the parent theme — also using "Ensure [result] for [stakeholder]" phrasing.

5. **Write a validating story for each theme.** For every theme, draft at least one of:
   - **Job story:** "When [situation/motivation] I need [desire] So I can [result]"
   - **User story:** "As a [user type] I want [desire] So I can [result]"
   This cross-checks that the theme genuinely reflects a customer need worth solving.

6. **Link each theme to a strategic objective.** Ask the user to provide (or confirm) the current list of strategic objectives. For each theme:
   - Identify which objective(s) it supports.
   - Tag the theme with the objective name(s).
   - If a theme cannot be linked to any objective, flag it explicitly and recommend the team reframe it, defer it to a later roadmap column, or remove it.
   Note: a theme may link to more than one objective — this is encouraged.

7. **Produce the theme table.** Output a structured table with these columns:

   | Original Feature | Theme (Ensure … for …) | Supporting Story | Objective(s) | Action |
   |---|---|---|---|---|

   Fill every row. For any theme that could not be linked to an objective, set Action to "Review with team — no objective link found".

8. **Write theme files to disk.** For each theme with at least one objective link, read [`../skills/product-roadmaps/templates/theme.md`](../skills/product-roadmaps/templates/theme.md) and write a filled-in copy to `./themes/<slug>.md` (slug = kebab-case of the "Ensure …" name). If `./roadmap.md` already exists, read it to determine the next available `id` (TH-00N) and to sync the `linked_objectives` IDs with the roadmap's objectives. Populate `name`, `timeframe` (Now / Next / Later — ask the user if unclear), `customer_need`, `linked_objectives`, `confidence` (default 50 when unknown), `source`, `created_on`, `last_updated`. Paste the job/user story into the `## Evidence` section. If a theme file with that slug already exists, merge rather than overwrite — append to the `## Change log` and update `last_updated`.

9. **Update the roadmap index.** If `./roadmap.md` exists, add each new theme to the appropriate `## Themes — Now / Next / Later` table with a link to `themes/<slug>.md`. If it does not exist, point the user at `/prr:build-roadmap-from-vision` to bootstrap it.

## Verify

- Every row in the output table has a theme statement in "Ensure [result] for [stakeholder]" format.
- No theme statement names a specific technology, UI component, or implementation approach (those are solutions, not outcomes).
- Every theme has at least one job story or user story.
- Every theme is tagged to at least one strategic objective, or is explicitly flagged for team review.
- The count of output themes matches or is less than the count of input features (grouping and deduplication are expected; expansion is a warning sign).

## Notes

- **Functional vs. technical needs:** Engineering-focused system or infrastructure needs (e.g., "Billing & payments API integration") are valid themes too. They may describe a nonfunctional need without prescribing the implementation. Do not discard them — tag them as technical/system themes and still link them to an objective.
- Themes are analogous to Agile epics; subthemes break down into the user stories that feed sprint planning.
- For deeper guidance on theme structure and subthemes, see [themes-and-needs](../skills/product-roadmaps/references/core/themes-and-needs.md).
- For linking themes to OKRs and strategic objectives, see [vision-strategy-okrs](../skills/product-roadmaps/references/core/vision-strategy-okrs.md).
- For prioritizing the resulting themes once they are defined, see [prioritization-frameworks](../skills/product-roadmaps/references/patterns/prioritization-frameworks.md).
- Watch for bad prioritization habits sneaking back in during the linking step — see [bad-prioritization](../skills/product-roadmaps/references/anti-patterns/bad-prioritization.md).
