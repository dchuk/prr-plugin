# prr — Product Roadmaps Relaunched

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that turns *Product Roadmaps Relaunched* by C. Todd Lombardo into a working toolkit: a skill, seven slash commands, two subagents, and a reference tree you can cite when building, reviewing, or defending a product roadmap.

The plugin's point of view — taken directly from the book — is that a roadmap is a **strategic communication tool**, not a project plan. Use this plugin when you want to move from feature-and-date lists to **outcome-driven, theme-based roadmaps** that communicate strategy and rally stakeholders.

---

## Install

In Claude Code, add this repo as a plugin marketplace and install the plugin:

```
/plugin marketplace add dchuk/prr-plugin
/plugin install prr@prr-marketplace
```

After install, the `product-roadmaps` skill is automatically available, the seven `/prr:*` commands are registered, and the two subagents can be invoked by name.

To update later:

```
/plugin marketplace update prr-marketplace
```

---

## What's inside

| Component | Count | Purpose |
|-----------|-------|---------|
| Skill | 1 (`product-roadmaps`) | Always-on guidance that routes Claude to the right reference, command, or agent for roadmap work |
| Slash commands | 7 | Structured, step-by-step workflows for the most common roadmap tasks |
| Subagents | 2 | Specialized reviewers that operate with narrow scope and their own system prompt |
| Reference files | 13 | Book-grounded material the skill loads on demand — frameworks, patterns, anti-patterns, glossary |

---

## Commands

All commands are namespaced `/prr:*` and accept an optional argument (feature list, file path, vision statement, etc.).

| Command | Purpose |
|---------|---------|
| `/prr:build-roadmap-from-vision` | Construct a full roadmap skeleton from company vision down to themes, business objectives, Now/Next/Later timeframes, and a disclaimer — the five required primary components. |
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

## Typical workflows

**Starting a new roadmap**
1. `/prr:build-roadmap-from-vision` to draft the skeleton.
2. `/prr:transform-features-to-themes` on any feature lists handed to you.
3. `/prr:build-roi-scorecard` to prioritize themes.
4. `/prr:run-shuttle-diplomacy` to build buy-in.
5. Invoke `roadmap-reviewer` before finalizing.

**Fixing an existing roadmap**
1. `/prr:assess-roadmap-health` to decide Approach A vs. Approach B.
2. Invoke `roadmap-relaunch-planner` to sequence the intervention.
3. Use `roadmap-reviewer` to catch anti-patterns in the current artifact.

**Handling disruption**
- Incoming stakeholder demand → `/prr:evaluate-special-request`
- Roadmap just changed → `/prr:communicate-roadmap-change`

---

## Philosophy

This plugin doesn't invent guidance. Every pattern, rule, score, and anti-pattern traces back to *Product Roadmaps Relaunched* (C. Todd Lombardo, Bruce McCarthy, Evan Ryan, Michael Connors; O'Reilly, 2017). When the book is silent, the agents and commands are instructed to say so rather than extrapolate.

## License

MIT — see `.claude-plugin/plugin.json`.

## Credits

Generated by [Franklin](https://github.com/mcrundo/franklin) from *Product Roadmaps Relaunched*, then hand-refined for skill/command best practices.
