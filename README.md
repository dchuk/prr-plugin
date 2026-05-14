# prr — Product Roadmaps Relaunched

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that turns *Product Roadmaps Relaunched* (C. Todd Lombardo, Bruce McCarthy, Evan Ryan, Michael Connors; O'Reilly, 2017) into a working toolkit for product managers: one always-loadable skill, eight slash commands, two subagents, five artifact templates, a validator hook, and thirteen book-grounded reference files you can cite when building, reviewing, or defending a product roadmap.

The plugin's point of view — taken directly from the book — is that a roadmap is a **strategic communication tool**, not a project plan. Use this plugin when you want to move from feature-and-date lists to **outcome-driven, theme-based roadmaps** that communicate strategy and rally stakeholders.

---

## Install

In Claude Code, add this repo as a plugin marketplace and install the plugin:

```
/plugin marketplace add dchuk/prr-plugin
/plugin install prr@prr-marketplace
```

After install, the `product-roadmaps` skill is available, the eight `/prr:*` commands are registered, the two subagents (`roadmap-reviewer`, `roadmap-relaunch-planner`) can be invoked by name, and the validator hook is wired into `Write` / `Edit` / `MultiEdit`.

To update later:

```
/plugin marketplace update prr-marketplace
```

---

## Who this is for

- **PMs starting a new roadmap** with no skeleton yet, or rebuilding from scratch.
- **PMs who inherited a roadmap** that's drifted into a feature-and-dates list and want to relaunch it without rebuilding from zero.
- **Founders, heads of product, and team leads** who need a defensible, outcome-driven roadmap to present to a board, investors, or an exec staff.
- **PMs trapped in tools** like Jira Product Discovery, Aha!, Productboard, Notion, or slide decks who want a markdown-native, git-trackable, diff-able roadmap source of truth.
- **PMs under stakeholder pressure** — sales escalations, exec pet features, customer commitment requests — who need a rigorous, book-grounded framework to say *yes*, *defer*, or *no*.
- **Anyone tasked with reviewing a roadmap** (auditor, peer reviewer, hiring panelist, new VP of Product) who wants a structured rubric instead of vibes.

---

## Use cases

Each row maps a real situation a PM faces to the command or agent that handles it. All commands are namespaced `/prr:*`. Agents are invoked via Claude Code's agent system.

### Building or rebuilding a roadmap

| Situation | Run this |
|-----------|----------|
| Starting a new product roadmap from scratch | `/prr:build-roadmap-from-vision` |
| Existing roadmap is so broken that rebuilding is cleaner than fixing | `/prr:build-roadmap-from-vision` |
| New company or product vision adopted; roadmap must be re-grounded | `/prr:build-roadmap-from-vision` |
| Inherited a roadmap from a predecessor and need to convert it to this format | `/prr:import-roadmap` |
| Want to migrate from Jira Product Discovery / Aha! / Productboard / Notion / slides into git-tracked markdown | `/prr:import-roadmap` |
| Backlog is a long list of feature names and you need to convert them to outcome-oriented themes | `/prr:transform-features-to-themes` |

### Prioritization and decision-making

| Situation | Run this |
|-----------|----------|
| More ideas than capacity; need a defensible ranking to share with stakeholders | `/prr:build-roi-scorecard` |
| Engineering or exec leadership disputes the current priority order | `/prr:build-roi-scorecard` |
| Sales escalates a feature ask to close a specific deal | `/prr:evaluate-special-request` |
| An executive demands an off-roadmap initiative and you need to articulate trade-offs | `/prr:evaluate-special-request` |
| A customer or partner is leveraging an integration commitment to extract a feature promise | `/prr:evaluate-special-request` |
| Roadmap is being driven by gut instinct, popularity votes, or "the loudest stakeholder" | `/prr:build-roi-scorecard` (replaces ad-hoc methods with a scored framework) |

### Stakeholder alignment

| Situation | Run this |
|-----------|----------|
| Need buy-in from cross-functional stakeholders before finalizing a roadmap | `/prr:run-shuttle-diplomacy` |
| Group meetings keep ending without a decision; consensus-seeking has stalled progress | `/prr:run-shuttle-diplomacy` |
| Relaunching a roadmap and need to re-establish shared direction | `/prr:run-shuttle-diplomacy` |
| Roadmap shifted (date slip, scope cut, strategic pivot) and stakeholders need to know | `/prr:communicate-roadmap-change` |
| Strategic pivot requires a layered comm — exec brief, dev team detail, customer summary | `/prr:communicate-roadmap-change` |

### Audits, reviews, and relaunches

| Situation | Run this |
|-----------|----------|
| Want a structured audit of an existing roadmap before sharing it | `roadmap-reviewer` agent |
| Pre-board-meeting or exec-review roadmap dry run | `roadmap-reviewer` agent |
| Self-review after drafting or importing a roadmap, before circulating | `roadmap-reviewer` agent |
| Process feels broken and you need to know whether to course-correct or relaunch | `/prr:assess-roadmap-health` |
| Already decided on a relaunch and need a sequenced action plan | `roadmap-relaunch-planner` agent |
| Quarterly or semi-annual roadmap health check | `/prr:assess-roadmap-health` |

### Defending the roadmap

| Situation | Run this |
|-----------|----------|
| Stakeholder claims a theme was "promised" — need to point to the disclaimer and confidence indicators | Inspect the `roadmap.md` frontmatter (`disclaimer`, `confidence`) |
| Sales-led "competitor X has this" pressure | `roadmap-reviewer` agent flags **Competitive Me-Too Prioritization** explicitly |
| New exec wants to add scope without dropping anything (iron-triangle violation) | `/prr:evaluate-special-request` (forces a trade-off) |
| Deck-based roadmap is being treated as a binding commitment by sales | `/prr:import-roadmap` to convert it, then `roadmap-reviewer` to surface every commitment-style violation |

---

## Two on-ramps

There are two ways to start using this plugin. Pick the one that matches where you are today.

### Path A — Start a new roadmap from scratch

Use this when you have no roadmap yet, or when your existing one is so broken that rebuilding is cleaner than converting.

1. In Claude Code, open a directory where you want the roadmap to live (e.g. `~/work/acme-roadmap/`).
2. Run:
   ```
   /prr:build-roadmap-from-vision
   ```
   Optionally pass your company vision as the argument.
3. Claude walks you through the book's eight-step process — gather inputs, vision, strategy and OKRs, customer needs as themes, prioritization, alignment, presenting, keeping it fresh.
4. Claude writes the following to your directory:
   - `roadmap.md` — vision, OKRs, Now/Next/Later index, disclaimer, prioritization method
   - `themes/<slug>.md` — one file per theme with linked objectives, customer need, confidence, evidence, optional ROI score
5. Invoke the `roadmap-reviewer` subagent to audit the draft before sharing it.

### Path B — Import an existing roadmap

Use this when you already have a roadmap somewhere — slides, a spreadsheet, Jira Product Discovery, Notion, Aha!, Productboard — and want to adopt the prr conventions without rebuilding from scratch.

**Step 1: Export your current roadmap into a file Claude can read.**

| If it lives in… | Export it as |
|-----------------|--------------|
| Jira Product Discovery | CSV or JSON from the ideas view |
| Aha!, Productboard, Roadmunk | CSV |
| Google Slides, PowerPoint, Keynote | PDF (File → Download → PDF) |
| Notion or Confluence | Markdown or PDF |
| Excel, Google Sheets, Numbers | CSV |
| A brain-dump doc or email | Plain markdown / text |

Save it anywhere in your project (e.g. `./imports/jpd-export.csv` or `./imports/roadmap-deck.pdf`).

**Step 2: Run the import command.**

```
/prr:import-roadmap ./imports/roadmap-deck.pdf
```

Claude will:

1. Read the source file (PDFs, CSVs, JSON, markdown all supported natively by Claude Code; PDFs over ~10 pages should be passed with a `pages:` range).
2. Classify what you have — *theme-based*, *feature-and-dates*, *mixed*, or *skeletal*.
3. Extract the five primary components (vision, objectives, themes, timeframes, disclaimer) and list what is missing.
4. Ask you about any gaps — typically missing vision, missing objectives, calendar dates that need reframing into Now / Next / Later, or feature names that need transforming into outcome-style themes ("SSO" → "Ensure teams can onboard under enterprise security review").
5. Write the converted files:
   - `roadmap.md` + `themes/<slug>.md` in the prr format (each theme file keeps a `## Source` section linking back to the original Jira ID / slide number / row)
   - `artifacts/import-YYYY-MM-DD.md` — an import report explaining every transformation, every gap filled, and every anti-pattern detected in the source

**Step 3: Audit the result.**

Invoke the `roadmap-reviewer` subagent. It will catch subtle anti-patterns that survived the conversion (e.g. a "theme" that is really a feature, a vision statement that is actually a mission statement).

### What you get either way

- **Structured markdown** you can keep in git, diff, and review — not trapped in a slide deck or a SaaS tool.
- **Book-grounded frontmatter** that prevents the named anti-patterns: no calendar dates, no orphaned themes, no 100% confidence, disclaimer required. A validator hook enforces these on every file write — see [Enforcement via a validator hook](#enforcement-via-a-validator-hook).
- **Commands for the rest of the lifecycle:** prioritize with `/prr:build-roi-scorecard`, handle incoming asks with `/prr:evaluate-special-request`, announce changes with `/prr:communicate-roadmap-change`, diagnose process issues with `/prr:assess-roadmap-health`, build buy-in with `/prr:run-shuttle-diplomacy`.

---

## What's inside

| Component | Count | Purpose |
|-----------|-------|---------|
| Skill | 1 (`product-roadmaps`) | Routing logic that loads the right reference, command, or agent for the task at hand |
| Slash commands | 8 | Structured, step-by-step workflows for the common roadmap tasks |
| Subagents | 2 | Specialized reviewers (`roadmap-reviewer`, `roadmap-relaunch-planner`) that operate with narrow scope and their own system prompt |
| Artifact templates | 5 | Standard markdown shapes for roadmap, theme, scorecard, change-comm, and special-request files |
| Validator hook | 1 | `PostToolUse` hook (`hooks/validate-artifact.py`) that enforces frontmatter rules on every `Write` / `Edit` / `MultiEdit` of a `managed_by: prr` file |
| Reference files | 13 | Book-grounded material the skill loads on demand — five core, three patterns, two anti-patterns, three topics |

---

## Commands

All commands are namespaced `/prr:*` and accept an optional argument (feature list, file path, vision statement, etc.).

| Command | Purpose |
|---------|---------|
| [`/prr:build-roadmap-from-vision`](commands/build-roadmap-from-vision.md) | Construct a full roadmap skeleton from company vision down to themes, business objectives, Now/Next/Later timeframes, and a disclaimer — the five required primary components. |
| [`/prr:import-roadmap`](commands/import-roadmap.md) | Convert an existing roadmap in any format (PDF, CSV, JSON, markdown) into the prr template format, with an import report showing transformations and anti-patterns found. |
| [`/prr:transform-features-to-themes`](commands/transform-features-to-themes.md) | Convert a list of feature requests or deliverables into outcome-oriented themes by uncovering the underlying customer need behind each item. |
| [`/prr:build-roi-scorecard`](commands/build-roi-scorecard.md) | Build a defensible ROI Scorecard ranking themes or features using **Value / Effort × Confidence** so prioritization isn't driven by gut or politics. |
| [`/prr:run-shuttle-diplomacy`](commands/run-shuttle-diplomacy.md) | Plan and run one-on-one stakeholder meetings followed by a group alignment session to build buy-in before finalizing a roadmap. |
| [`/prr:evaluate-special-request`](commands/evaluate-special-request.md) | Evaluate an ad-hoc sales or stakeholder request against the roadmap using the book's three qualifying questions and iron-triangle trade-off analysis. |
| [`/prr:assess-roadmap-health`](commands/assess-roadmap-health.md) | Run the 14-question Roadmap Health Assessment (0–2 per question, max 22 points) and recommend Approach A (course corrections) or Approach B (full relaunch) with next steps. |
| [`/prr:communicate-roadmap-change`](commands/communicate-roadmap-change.md) | Draft an audience-aware stakeholder communication for any roadmap change — from a minor date slip to a strategic pivot. |

---

## Agents

Invoke these via Claude Code's agent system when you want a narrower, more rigorous pass than the main conversation.

- **[`roadmap-reviewer`](agents/roadmap-reviewer.md)** — Audits a roadmap artifact (document, slide deck description, or structured text) against the book's principles, rules, and anti-patterns. Checks for the five primary components, feature-date thinking, output-vs-outcome framing, missing strategic context, overpromising, Feature Factory patterns, bad prioritization, consensus-seeking, Osborne Effect risks, orphaned themes, iron triangle violations, and commitment-style language. Operates in **structured mode** when files carry `managed_by: prr` frontmatter — it parses YAML directly for mechanical checks and falls back to prose review otherwise. Output is severity-ranked (Critical / High / Medium / Low) with rule citations and concrete corrections.
- **[`roadmap-relaunch-planner`](agents/roadmap-relaunch-planner.md)** — Plans a roadmap relaunch or improvement initiative. Runs the Roadmap Health Assessment, chooses between Approach A (course corrections, one-improvement-at-a-time) and Approach B (full relaunch), sequences the six-step relaunch process, identifies the highest-leverage improvements, structures roadmap workshops, and builds a steering-committee cadence.

---

## Artifacts and templates

Every artifact the plugin produces has a standard markdown shape with YAML frontmatter, so commands can read/write each other's output and the `roadmap-reviewer` agent can audit it mechanically.

| Template | Purpose | Default output path |
|----------|---------|---------------------|
| [`skills/product-roadmaps/templates/roadmap.md`](skills/product-roadmaps/templates/roadmap.md) | The roadmap index — vision, objectives, disclaimer, Now/Next/Later tables | `./roadmap.md` |
| [`skills/product-roadmaps/templates/theme.md`](skills/product-roadmaps/templates/theme.md) | One file per theme with customer need, linked objectives, evidence, subthemes, optional ROI score | `./themes/<slug>.md` |
| [`skills/product-roadmaps/templates/roi-scorecard.md`](skills/product-roadmaps/templates/roi-scorecard.md) | (Value / Effort) × Confidence prioritization, written by `/prr:build-roi-scorecard` | `./artifacts/scorecard-YYYY-MM-DD.md` |
| [`skills/product-roadmaps/templates/change-communication.md`](skills/product-roadmaps/templates/change-communication.md) | Audience-aware change announcement written by `/prr:communicate-roadmap-change` | `./artifacts/change-YYYY-MM-DD-<slug>.md` |
| [`skills/product-roadmaps/templates/special-request.md`](skills/product-roadmaps/templates/special-request.md) | Three-qualifying-questions evaluation written by `/prr:evaluate-special-request` | `./artifacts/request-YYYY-MM-DD-<slug>.md` |

Default on-disk layout in a user project:

```
<your project>/
├── roadmap.md
├── themes/
│   ├── ensure-seamless-checkout.md
│   └── ensure-faster-onboarding.md
└── artifacts/
    ├── scorecard-2026-04-13.md
    ├── change-2026-04-20-defer-reporting.md
    └── request-2026-04-22-acme-sso.md
```

The frontmatter enforces book-grounded constraints structurally: `timeframe` is restricted to `Now | Next | Later` (no dates), `confidence` is an integer 0–99 (never 100), `linked_objectives` is required and non-empty (no orphaned themes), `disclaimer` is required on the roadmap, and `prioritization_method` must be declared (`roi-scorecard | dfv | kano | moscow | critical-path`). Every file carries a `type:` discriminator (`roadmap | theme | roi-scorecard | change-communication | special-request-evaluation`) so agents can filter artifacts with a single grep.

### Enforcement via a validator hook

The plugin ships a `PostToolUse` hook (`hooks/validate-artifact.py`, wired in `hooks/hooks.json`) that runs after every `Write` / `Edit` / `MultiEdit`. The hook:

- **Only inspects files that declare `managed_by: prr`** in their YAML frontmatter — your existing `roadmap.md` or `themes/*.md` without that marker are never touched.
- Validates type-specific rules (required fields, enum values, integer ranges) against the book's prescriptions.
- On failure, exits with code 2 and prints actionable errors to stderr; Claude sees the message and self-corrects in the same conversation.
- Has zero third-party dependencies — pure Python stdlib, uses only `python3` (preinstalled on macOS and most Linux distros).

To opt out on a specific file, simply omit `managed_by: prr` from its frontmatter. To disable the hook globally, remove it from `~/.claude/settings.json` after install.

---

## Skill and reference tree

The `product-roadmaps` skill is the plugin's entry point. It registers the routing logic (core process, pattern catalog, anti-pattern index, command/agent map) and loads reference files on demand. The tree under `skills/product-roadmaps/references/`:

```
references/
├── core/
│   ├── roadmap-definition.md        What a roadmap is (and is not)
│   ├── roadmap-components.md        The five primary components, plus secondary and supporting
│   ├── vision-strategy-okrs.md      Mission → vision → strategy → OKRs → KPIs alignment
│   ├── themes-and-needs.md          Customer needs expressed as themes and subthemes
│   └── gathering-inputs.md          Life-cycle stage, market, business environment inputs
├── patterns/
│   ├── prioritization-frameworks.md Critical Path, Kano, DFV, ROI Scorecard, MoSCoW
│   ├── alignment-and-buyin.md       Shuttle diplomacy, co-creation workshops, software tools
│   └── presenting-and-sharing.md    Modular roadmap, audience-specific views, comm best practices
├── anti-patterns/
│   ├── roadmap-anti-patterns.md     Roadmap-as-project-plan, Feature Factory, Osborning, etc.
│   └── bad-prioritization.md        Gut instinct, popularity, HiPPO, sales-driven, me-too, etc.
└── topics/
    ├── relaunch-process.md          Six-step relaunch, 14-question Health Assessment scoring
    ├── keeping-roadmap-fresh.md     Review cadence, punctuated equilibrium, iron triangle
    └── glossary.md                  Terms and definitions used across the book
```

---

## Lifecycle after the first roadmap exists

Once `roadmap.md` and `themes/` are in place (via Path A or Path B), the rest of the commands cover day-to-day roadmap work:

- **Prioritizing a backlog** → `/prr:build-roi-scorecard` (writes `artifacts/scorecard-YYYY-MM-DD.md` and updates each theme's `roi_score` frontmatter).
- **Incoming sales or exec request** → `/prr:evaluate-special-request` (three qualifying questions + iron-triangle trade-off, writes `artifacts/request-YYYY-MM-DD-<slug>.md`).
- **Roadmap changed and stakeholders need to know** → `/prr:communicate-roadmap-change` (audience-aware message for dev / exec / sales / customer, writes `artifacts/change-YYYY-MM-DD-<slug>.md`).
- **Process feels broken** → `/prr:assess-roadmap-health` (14-question health check, recommends course correction vs. full relaunch).
- **Need stakeholder buy-in before a review** → `/prr:run-shuttle-diplomacy` (one-on-one plan + group alignment session).
- **Want a rigorous audit** → invoke the `roadmap-reviewer` subagent — it reads files in structured mode when they carry `managed_by: prr` frontmatter.
- **Planning a full relaunch** → invoke the `roadmap-relaunch-planner` subagent after running the health assessment.

---

## Philosophy

This plugin doesn't invent guidance. Every pattern, rule, score, and anti-pattern traces back to *Product Roadmaps Relaunched* (Lombardo, McCarthy, Ryan, Connors; O'Reilly, 2017). When the book is silent, the agents and commands are instructed to say so rather than extrapolate.

## License

MIT — see `.claude-plugin/plugin.json`.

## Credits

Generated by [Franklin](https://github.com/mcrundo/franklin) from *Product Roadmaps Relaunched*, then hand-refined for skill/command best practices.
