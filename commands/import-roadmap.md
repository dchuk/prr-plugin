---
description: Convert an existing roadmap (PDF, CSV, markdown, JSON, slides export) into the prr plugin format
argument-hint: "[path to existing roadmap file]"
---

# Import Roadmap

**Purpose:** Read an existing roadmap artifact in any format — Jira Product Discovery export, Google Slides PDF, Aha!/Productboard CSV, Notion markdown, a spreadsheet, a brain-dump doc — and convert it into the prr plugin's standard markdown format: a `roadmap.md` index plus one `themes/<slug>.md` per theme, all with book-grounded YAML frontmatter including `managed_by: prr`.

## When to use

- You already have a roadmap somewhere (slides, spreadsheet, issue tracker export) and want to adopt the prr conventions without rebuilding from scratch.
- You want to audit an existing roadmap — convert first, then run the [roadmap-reviewer](../agents/roadmap-reviewer.md) agent on the structured output.
- You are migrating between tools and need a canonical, reviewable markdown source of truth in git.
- The existing roadmap is suspected of being feature-and-dates-driven and you want the conversion process to surface the anti-patterns explicitly.

## Supported source formats

| Source tool | Export as |
|-------------|-----------|
| Jira Product Discovery | CSV or JSON from the ideas view |
| Aha!, Productboard, Roadmunk | CSV |
| Google Slides, PowerPoint, Keynote | PDF (File → Download → PDF) |
| Notion, Confluence | Markdown or PDF |
| Excel, Google Sheets, Numbers | CSV |
| Plain markdown or text | Use as-is |

PDFs are read natively by Claude Code (up to ~20 pages per call — pass a `pages:` range for larger decks).

---

## Steps

### 1. Load the source

Use the Read tool on the path provided as the command argument. If it is a PDF over 10 pages, ask the user which page range contains the roadmap content and pass `pages: "N-M"`. If it is a CSV or JSON, read the full file and parse the structure. If it is a directory, Glob for `*.md`, `*.csv`, `*.json`, `*.pdf` and ask the user which files to include.

### 2. Extract the five primary components

Scan the source for each of the book's required components. Build a checklist of what was found vs. what is missing:

| Component | Look for |
|-----------|----------|
| **Product vision** | "vision", "mission", "north star", purpose statement, value-prop sentence |
| **Business objectives** | OKRs, KPIs, strategic goals, annual priorities, company bets |
| **Themes** | "theme", "initiative", "epic", "outcome", "pillar", "problem", "job-to-be-done" |
| **Features / deliverables** | Named solutions, UI components, specific capabilities — these will be **transformed** into themes |
| **Timeframes** | Now/Next/Later, quarters, release names, calendar dates |
| **Disclaimer / caveats** | "subject to change", "directional", "plan may evolve" |

### 3. Classify the source shape

Report one of:

- **Theme-based** — clean fit. Just reshape into the template.
- **Feature-and-dates** — needs transformation. See [roadmap-anti-patterns](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md) for the anti-patterns that are about to be corrected.
- **Mixed** — some themes, some features. Transform the features; keep the themes.
- **Skeletal** — only vision, or only a feature list, with large gaps. The user will need to fill in most fields.

### 4. Fill gaps with the user

For each missing or weak component, ask the user:

- **No vision?** Run the vision workflow from [build-roadmap-from-vision](build-roadmap-from-vision.md) Step 2.
- **No objectives?** Ask for current OKRs, or draft 2–4 from the source material and confirm with the user.
- **Feature-driven themes?** Apply the reasoning from [transform-features-to-themes](transform-features-to-themes.md): for each feature, ask "Why does the customer want this?" until you reach an outcome, then phrase as "Ensure <result> for <stakeholder>".
- **Calendar dates on items?** Ask the user to re-bucket each item into Now / Next / Later.
- **No disclaimer?** Use the default disclaimer from the template — no user input needed unless they want a custom one.

Do not guess on ambiguous items — it is better to ask than to invent a customer need the user did not confirm.

### 5. Write the prr files

For every theme-equivalent item in the source:

1. Read the theme template at !`echo ${CLAUDE_PLUGIN_ROOT}/skills/product-roadmaps/templates/theme.md`.
2. Write a filled-in copy to `./themes/<slug>.md`. Slug = kebab-case of the outcome-style name (e.g. `ensure-seamless-checkout`).
3. Populate: `type: theme`, `managed_by: prr`, `id` (TH-001, TH-002, …), `name` in "Ensure … for …" form, `timeframe` (Now/Next/Later only), `customer_need`, `linked_objectives` (non-empty — ask if unclear), `confidence` (default 50 unless the source provides evidence), `source: import`, `created_on` (today), `last_updated` (today).
4. Preserve source traceability in the body under a `## Source` section:
   ```markdown
   ## Source
   - Original artifact: <path to imported file>
   - Original item: "<verbatim name/title from the source>"
   - Reference: <Jira ID / slide number / row number / URL if available>
   - Notes: <any context that doesn't fit the other fields>
   ```

Then read the roadmap template at !`echo ${CLAUDE_PLUGIN_ROOT}/skills/product-roadmaps/templates/roadmap.md` and write `./roadmap.md` with the extracted vision/objectives/disclaimer, `prioritization_method` set to whatever the source used (or `null` if unknown), and Now / Next / Later tables linking to each theme file.

### 6. Produce an import report

Read the roadmap template at !`echo ${CLAUDE_PLUGIN_ROOT}/skills/product-roadmaps/templates/roadmap.md` as a reference for the conventions, then write a free-form markdown report at `./artifacts/import-YYYY-MM-DD.md` with these sections:

- **Source** — file path, format, size
- **Classification** — theme-based / feature-and-dates / mixed / skeletal
- **Components found vs. required** — the checklist from Step 2
- **Transformations applied** — every feature → theme conversion, with original name and new theme name
- **Gaps filled by user input** — every question asked and answer given
- **Anti-patterns detected in the source** — with references to [`roadmap-anti-patterns.md`](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md) or [`bad-prioritization.md`](../skills/product-roadmaps/references/anti-patterns/bad-prioritization.md)
- **Items dropped** — anything from the source that was not imported, with reason (duplicate, too vague, not a roadmap item, etc.)
- **Recommended next action** — almost always: run the [roadmap-reviewer](../agents/roadmap-reviewer.md) agent on the new files

---

## Verify

Before declaring the import complete, check:

- [ ] `./roadmap.md` exists with `managed_by: prr` and all five primary components in frontmatter (vision, objectives, themes via links, timeframes via Now/Next/Later tables, disclaimer)
- [ ] Every non-dropped item from the source is represented as a `themes/<slug>.md` file with `managed_by: prr`
- [ ] Every theme has non-empty `linked_objectives` — no orphans
- [ ] No theme has a calendar date in its `timeframe` — Now/Next/Later only
- [ ] Every theme file has a `## Source` section pointing back to the original
- [ ] The validator hook did not reject any of the written files (check stderr output — if it did, fix and re-run)
- [ ] The import report exists and explains every significant decision

If any check fails, fix before delivering.

---

## Notes

- **Traceability matters during migration.** Teams adopting the prr format often need to reconcile against the old artifact for weeks — keep the `## Source` sections rich so engineers, PMs, and stakeholders can verify nothing was lost.
- **Features are not themes.** The single most common import mistake is letting a feature name (e.g. "SSO", "HTML5 redesign", "bulk export") survive as a theme. Use [transform-features-to-themes](transform-features-to-themes.md) reasoning on every item that looks like a solution.
- **Dates become timeframes.** A source that says "Q2 2026" is a calendar date — convert to Now/Next/Later based on the date relative to today. Do not carry the quarter over, even as a note in `timeframe`; that is how feature-and-dates thinking leaks back in.
- **Audit immediately after import.** Run [roadmap-reviewer](../agents/roadmap-reviewer.md) as the next step — it often catches subtle anti-patterns that survived the conversion (e.g. a "theme" that is really a feature, a vision statement that is actually a mission statement).
- **Large PDFs:** If the roadmap spans many slides, ask the user to point you at the specific page range rather than reading the whole deck. Appendices, team bios, and architecture diagrams are not roadmap content.
- **No existing roadmap?** Use [build-roadmap-from-vision](build-roadmap-from-vision.md) instead — this command is only for converting something that already exists.
