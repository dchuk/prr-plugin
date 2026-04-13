# prr — Product Roadmaps Relaunched

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that turns *Product Roadmaps Relaunched* by C. Todd Lombardo into a working toolkit for product managers: a skill, eight slash commands, two subagents, five artifact templates, a validator hook, and a reference tree you can cite when building, reviewing, or defending a product roadmap.

The plugin's point of view — taken directly from the book — is that a roadmap is a **strategic communication tool**, not a project plan. Use this plugin when you want to move from feature-and-date lists to **outcome-driven, theme-based roadmaps** that communicate strategy and rally stakeholders.

---

## Install

In Claude Code, add this repo as a plugin marketplace and install the plugin:

```
/plugin marketplace add dchuk/prr-plugin
/plugin install prr@prr-marketplace
```

After install, the `product-roadmaps` skill is automatically available, the eight `/prr:*` commands are registered, the two subagents can be invoked by name, and the validator hook is wired into `Write` / `Edit` / `MultiEdit`.

To update later:

```
/plugin marketplace update prr-marketplace
```

---

## Quick Start for Product Managers

There are two ways to start using this plugin. Pick the one that matches where you are today.

### Path A — Start a new roadmap from scratch

Use this when you have no roadmap yet, or when your existing one is so broken that rebuilding is cleaner than converting.

1. In Claude Code, open a directory where you want the roadmap to live (e.g. `~/work/acme-roadmap/`).
2. Run:
   ```
   /prr:build-roadmap-from-vision
   ```
   Optionally pass your company vision as the argument.
3. Claude walks you through the book's eight-step process — vision, business objectives (OKRs), customer needs, themes, prioritization, Now / Next / Later assignment, disclaimer, secondary components.
4. Claude writes the following to your directory:
   - `roadmap.md` — vision, OKRs, Now/Next/Later index, disclaimer
   - `themes/<slug>.md` — one file per theme with linked objectives, customer need, confidence, evidence
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

1. Read the source file (PDFs, CSVs, JSON, markdown all supported natively).
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
| Skill | 1 (`product-roadmaps`) | Always-on guidance that routes Claude to the right reference, command, or agent for roadmap work |
| Slash commands | 8 | Structured, step-by-step workflows for the common roadmap tasks |
| Subagents | 2 | Specialized reviewers that operate with narrow scope and their own system prompt |
| Artifact templates | 5 | Standard markdown shapes for roadmap, theme, scorecard, change-comm, and special-request files |
| Validator hook | 1 | `PostToolUse` hook that enforces frontmatter rules on every `Write`/`Edit` of a `managed_by: prr` file |
| Reference files | 13 | Book-grounded material the skill loads on demand — frameworks, patterns, anti-patterns, glossary |

---

## Commands

All commands are namespaced `/prr:*` and accept an optional argument (feature list, file path, vision statement, etc.).

| Command | Purpose |
|---------|---------|
| `/prr:build-roadmap-from-vision` | Construct a full roadmap skeleton from company vision down to themes, business objectives, Now/Next/Later timeframes, and a disclaimer — the five required primary components. |
| `/prr:import-roadmap` | Convert an existing roadmap in any format (PDF, CSV, JSON, markdown) into the prr template format, with an import report showing transformations and anti-patterns found. |
| `/prr:transform-features-to-themes` | Convert a list of feature requests or deliverables into outcome-oriented themes by uncovering the underlying customer need behind each item. |
| `/prr:build-roi-scorecard` | Build a defensible ROI Scorecard ranking themes or features using **Value / Effort × Confidence** so prioritization isn't driven by gut or politics. |
| `/prr:run-shuttle-diplomacy` | Plan and run one-on-one stakeholder meetings followed by a group alignment session to build buy-in before finalizing a roadmap. |
| `/prr:evaluate-special-request` | Evaluate an ad-hoc sales or stakeholder request against the roadmap using the book's three qualifying questions and iron-triangle trade-off analysis. |
| `/prr:assess-roadmap-health` | Run the 14-question Roadmap Health Assessment (0–2 per question, max 22 points) and recommend Approach A (course corrections) or Approach B (full relaunch) with next steps. |
| `/prr:communicate-roadmap-change` | Draft an audience-aware stakeholder communication for any roadmap change — from a minor date slip to a strategic pivot. |

---

## Agents

Invoke these via Claude Code's agent system when you want a narrower, more rigorous pass than the main conversation.

- **`roadmap-reviewer`** — Audits a roadmap artifact (document, slide deck description, or structured text) against the book's principles, rules, and anti-patterns. Checks for the five primary components, feature-date thinking, output-vs-outcome framing, missing strategic context, overpromising, Feature Factory patterns, bad prioritization, consensus-seeking, Osborne Effect risks, orphaned themes, iron triangle violations, and commitment-style language. Output is severity-ranked with rule citations and concrete corrections.
- **`roadmap-relaunch-planner`** — Plans a roadmap relaunch or improvement initiative. Runs the Roadmap Health Assessment, chooses between Approach A and Approach B, sequences the six-step relaunch process, identifies highest-leverage improvements, structures roadmap workshops, and builds a steering-committee cadence.

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

The frontmatter enforces book-grounded constraints structurally: `timeframe` is restricted to `Now | Next | Later` (no dates), `confidence` is an integer 0–99 (never 100), `linked_objectives` is required and non-empty (no orphaned themes), `disclaimer` is required on the roadmap. Every file carries a `type:` discriminator so agents can filter artifacts with a single grep.

### Enforcement via a validator hook

The plugin ships a `PostToolUse` hook (`hooks/validate-artifact.py`) that runs after every `Write` / `Edit` / `MultiEdit`. The hook:

- **Only inspects files that declare `managed_by: prr`** in their YAML frontmatter — your existing `roadmap.md` or `themes/*.md` without that marker are never touched.
- Validates type-specific rules (required fields, enum values, integer ranges) against the book's prescriptions.
- On failure, exits with code 2 and prints actionable errors to stderr; Claude sees the message and self-corrects in the same conversation.
- Has zero third-party dependencies — pure Python stdlib, uses only `python3` which ships with macOS and Linux.

To opt out on a specific file, simply omit `managed_by: prr` from its frontmatter. To disable the hook globally, remove it from `~/.claude/settings.json` after install.

## Skill and reference tree

The `product-roadmaps` skill is the plugin's entry point. It registers the routing logic (core process, pattern catalog, anti-pattern index, command/agent map) and loads reference files on demand. The tree under `skills/product-roadmaps/references/`:

```
references/
├── core/
│   ├── roadmap-definition.md        What a roadmap is (and is not)
│   ├── roadmap-components.md        The five primary components
│   ├── vision-strategy-okrs.md      Vision → strategy → OKRs alignment
│   ├── themes-and-needs.md          Customer needs expressed as themes
│   └── gathering-inputs.md          Life cycle, market, business inputs
├── patterns/
│   ├── prioritization-frameworks.md ROI Scorecard, Kano, Critical Path, MoSCoW, DFV
│   ├── alignment-and-buyin.md       Shuttle diplomacy, co-creation workshops
│   └── presenting-and-sharing.md    Modular roadmap, audience-specific views
├── anti-patterns/
│   ├── roadmap-anti-patterns.md     Roadmap-as-project-plan, Feature Factory, etc.
│   └── bad-prioritization.md        Gut instinct, popularity, HiPPO, me-too
└── topics/
    ├── relaunch-process.md          Six-step relaunch, Health Assessment scoring
    ├── keeping-roadmap-fresh.md     Review cadence, punctuated equilibrium
    └── glossary.md                  Terms and definitions
```

---

## Lifecycle after the first roadmap exists

Once `roadmap.md` and `themes/` are in place (via Path A or Path B), the rest of the commands cover day-to-day roadmap work:

- **Prioritizing a backlog** → `/prr:build-roi-scorecard` (writes `artifacts/scorecard-YYYY-MM-DD.md` and updates each theme's `roi_score` frontmatter).
- **Incoming sales or exec request** → `/prr:evaluate-special-request` (three qualifying questions + iron-triangle trade-off, writes `artifacts/request-YYYY-MM-DD-<slug>.md`).
- **Roadmap changed and stakeholders need to know** → `/prr:communicate-roadmap-change` (audience-aware message for dev/exec/sales/customer, writes `artifacts/change-YYYY-MM-DD-<slug>.md`).
- **Process feels broken** → `/prr:assess-roadmap-health` (14-question health check, recommends course correction vs. full relaunch).
- **Need stakeholder buy-in before a review** → `/prr:run-shuttle-diplomacy` (one-on-one plan + group alignment session).
- **Want a rigorous audit** → invoke the `roadmap-reviewer` subagent — it reads files in structured mode when they carry `managed_by: prr` frontmatter.
- **Planning a full relaunch** → invoke the `roadmap-relaunch-planner` subagent after running the health assessment.

---

## Philosophy

This plugin doesn't invent guidance. Every pattern, rule, score, and anti-pattern traces back to *Product Roadmaps Relaunched* (C. Todd Lombardo, Bruce McCarthy, Evan Ryan, Michael Connors; O'Reilly, 2017). When the book is silent, the agents and commands are instructed to say so rather than extrapolate.

## License

MIT — see `.claude-plugin/plugin.json`.

## Credits

Generated by [Franklin](https://github.com/mcrundo/franklin) from *Product Roadmaps Relaunched*, then hand-refined for skill/command best practices.
