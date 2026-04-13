---
name: product-roadmaps
description: Build, review, or fix outcome-driven product roadmaps. Use for "build a roadmap", "review my roadmap", "prioritize themes", "features to themes", "stakeholder buy-in", "roadmap health check", "communicate roadmap change", or roadmap anti-patterns.
allowed-tools:
  - Grep
  - Glob
  - Read
  - Task
---

# Product Roadmaps Relaunched

A practitioner plugin for outcome-driven product roadmapping, based on *Product Roadmaps Relaunched* by C. Todd Lombardo. Use this plugin when you need to build, relaunch, prioritize, align, or communicate a product roadmap — and when you want to move from feature-and-date thinking to themes and customer outcomes. Every reference file, command, and agent below is linked so you can jump directly to what you need.

---

## Core Roadmapping Process

Eight steps from inputs to a living roadmap. Follow this sequence when starting or restarting a roadmapping effort.

| Step | Activity | Reference |
|------|-----------|-----------|
| 1 | Gather inputs (life cycle, market, business environment) | [gathering-inputs](references/core/gathering-inputs.md) |
| 2 | Establish the product vision, strategy, and OKRs | [vision-strategy-okrs](references/core/vision-strategy-okrs.md) |
| 3 | Uncover customer needs as themes | [themes-and-needs](references/core/themes-and-needs.md) |
| 4 | Dive deeper into needs and solutions | [themes-and-needs](references/core/themes-and-needs.md) |
| 5 | Prioritize using proven frameworks | [prioritization-frameworks](references/patterns/prioritization-frameworks.md) |
| 6 | Achieve buy-in and alignment | [alignment-and-buyin](references/patterns/alignment-and-buyin.md) |
| 7 | Present and share with the right audiences | [presenting-and-sharing](references/patterns/presenting-and-sharing.md) |
| 8 | Keep it fresh — evolve as you learn | [keeping-roadmap-fresh](references/topics/keeping-roadmap-fresh.md) |

---

## Pattern Catalog

| Pattern | Summary | Reference |
|---------|---------|-----------|
| Themes | High-level customer needs/jobs-to-be-done that organize the roadmap instead of feature lists | [themes-and-needs](references/core/themes-and-needs.md) |
| Now / Next / Later | Timeframe model using three buckets instead of specific release dates | [roadmap-components](references/core/roadmap-components.md) |
| Critical Path | Prioritization framework identifying the minimum set of work required to deliver customer value | [prioritization-frameworks](references/patterns/prioritization-frameworks.md) |
| Kano Model | Framework classifying features by their effect on customer satisfaction (basic, performance, delighter) | [prioritization-frameworks](references/patterns/prioritization-frameworks.md) |
| Desirability / Feasibility / Viability | Three-lens framework for evaluating whether a theme is worth pursuing | [prioritization-frameworks](references/patterns/prioritization-frameworks.md) |
| ROI Scorecard | Weighted scoring model for ranking themes against defined value criteria | [prioritization-frameworks](references/patterns/prioritization-frameworks.md) |
| MoSCoW | Must-have / Should-have / Could-have / Won't-have prioritization heuristic | [prioritization-frameworks](references/patterns/prioritization-frameworks.md) |
| Shuttle Diplomacy | Iterative one-on-one stakeholder alignment before group roadmap reviews | [alignment-and-buyin](references/patterns/alignment-and-buyin.md) |
| Co-creation Workshops | Facilitated sessions to build shared ownership of roadmap direction | [alignment-and-buyin](references/patterns/alignment-and-buyin.md) |
| Modular Roadmap | Single source of truth sliced into audience-specific views for different stakeholders | [presenting-and-sharing](references/patterns/presenting-and-sharing.md) |
| Roadmap Health Assessment | 14-question scored checklist (0–2 per question, max 22 points) to diagnose roadmap quality | [relaunch-process](references/topics/relaunch-process.md) |
| Punctuated Equilibrium | Change model for managing planned roadmap pivots without losing stakeholder trust | [keeping-roadmap-fresh](references/topics/keeping-roadmap-fresh.md) |

---

## Anti-Pattern Quick Reference

| Anti-pattern | Why harmful | Reference |
|---|---|---|
| **Roadmap as Project Plan** | Turns strategic direction into binding commitments; makes the team optimize for delivery dates over customer outcomes | [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) |
| **Roadmap Without Strategic Context** | Leaves stakeholders without a shared vision; invites scope creep and "shiny object" syndrome | [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) |
| **Output-Focused Roadmap** | Features ship on time but business KPIs don't move; team has no line of sight to customer impact | [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) |
| **Roadmap as Commitment Document** | Salespeople extract date/feature promises that lock the team into delivering the wrong thing | [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) |
| **Excessive Up-Front Design and Estimation** | Wastes time on detailed specs before the team knows what to build; delays learning | [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) |
| **Roadmap Hidden from Customers** | Misses validation opportunities; shipped features go unused; customers feel surprised by direction | [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) |
| **Feature Factory** | Roadmap becomes a backlog of features with no theme or outcome framing; velocity replaces strategy | [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) |
| **Gut Instinct Prioritization** | No defensible rationale; highest-paid person's opinion dominates; team loses trust in process | [bad-prioritization](references/anti-patterns/bad-prioritization.md) |
| **Analyst Opinion Prioritization** | Outsources strategic judgment to third parties who don't know your customers or constraints | [bad-prioritization](references/anti-patterns/bad-prioritization.md) |
| **Popularity-Based Prioritization** | Most-requested feature wins regardless of strategic fit or actual customer value | [bad-prioritization](references/anti-patterns/bad-prioritization.md) |

---

## What Would You Like to Do?

- **Understand what a product roadmap is (and is not)** → [roadmap-definition](references/core/roadmap-definition.md)
- **Build a roadmap from your company vision down to themes** → [`/build-roadmap-from-vision`](../../commands/build-roadmap-from-vision.md)
- **Convert an existing roadmap (Jira, Aha!, slides, spreadsheet) into this format** → [`/import-roadmap`](../../commands/import-roadmap.md)
- **Transform a feature list into outcome-oriented themes** → [`/transform-features-to-themes`](../../commands/transform-features-to-themes.md)
- **Prioritize themes using a scored framework** → [`/build-roi-scorecard`](../../commands/build-roi-scorecard.md) or [prioritization-frameworks](references/patterns/prioritization-frameworks.md)
- **Align stakeholders and get buy-in** → [`/run-shuttle-diplomacy`](../../commands/run-shuttle-diplomacy.md) or [alignment-and-buyin](references/patterns/alignment-and-buyin.md)
- **Evaluate a special request from sales or an executive** → [`/evaluate-special-request`](../../commands/evaluate-special-request.md)
- **Check whether your roadmap is healthy** → [`/assess-roadmap-health`](../../commands/assess-roadmap-health.md) or [relaunch-process](references/topics/relaunch-process.md)
- **Communicate a roadmap change to stakeholders** → [`/communicate-roadmap-change`](../../commands/communicate-roadmap-change.md)
- **Review an existing roadmap artifact against the book's principles** → [roadmap-reviewer agent](../../agents/roadmap-reviewer.md)
- **Plan a full roadmap relaunch initiative** → [roadmap-relaunch-planner agent](../../agents/roadmap-relaunch-planner.md)

---

## Commands Reference

| Command | What it does |
|---------|-------------|
| `/build-roadmap-from-vision` | Walk from company vision → product vision → strategy → OKRs → themes to create a roadmap skeleton |
| `/import-roadmap` | Convert an existing roadmap (PDF, CSV, JSON, markdown) into the prr plugin format with an import report |
| `/transform-features-to-themes` | Convert a feature list into outcome-oriented themes by asking "Why does this matter?" |
| `/build-roi-scorecard` | Build a weighted ROI scoring model for prioritizing themes |
| `/run-shuttle-diplomacy` | Generate a shuttle diplomacy canvas and stakeholder engagement plan |
| `/evaluate-special-request` | Score an incoming stakeholder request against the current roadmap using the three evaluation questions |
| `/assess-roadmap-health` | Run the 14-question Roadmap Health Assessment (scored 0–2, max 22 points) |
| `/communicate-roadmap-change` | Draft a structured change communication covering why, what, and what's next |

Full command details: [`build-roadmap-from-vision`](../../commands/build-roadmap-from-vision.md) · [`import-roadmap`](../../commands/import-roadmap.md) · [`transform-features-to-themes`](../../commands/transform-features-to-themes.md) · [`build-roi-scorecard`](../../commands/build-roi-scorecard.md) · [`run-shuttle-diplomacy`](../../commands/run-shuttle-diplomacy.md) · [`evaluate-special-request`](../../commands/evaluate-special-request.md) · [`assess-roadmap-health`](../../commands/assess-roadmap-health.md) · [`communicate-roadmap-change`](../../commands/communicate-roadmap-change.md)

---

## Agents

| Agent | When to use |
|-------|-------------|
| [roadmap-reviewer](../../agents/roadmap-reviewer.md) | Review a roadmap artifact against the book's principles; get a structured diagnosis with anti-patterns called out |
| [roadmap-relaunch-planner](../../agents/roadmap-relaunch-planner.md) | Plan a full roadmap relaunch — starts with the Health Assessment, then produces a prioritized improvement plan |

---

## Reference Map

### Core Concepts
| File | Description |
|------|-------------|
| [roadmap-definition](references/core/roadmap-definition.md) | What a product roadmap IS and IS NOT — strategic communication tool vs. project plan or feature list |
| [roadmap-components](references/core/roadmap-components.md) | The three tiers of roadmap components: primary (vision, objectives, themes, timeframes), secondary, and supporting |
| [vision-strategy-okrs](references/core/vision-strategy-okrs.md) | Establishing the "why" — mission, vision, values, product vision, product strategy, OKRs, and KPIs |
| [gathering-inputs](references/core/gathering-inputs.md) | Pre-roadmap research: product life cycle stages, market analysis, and business environment inputs |
| [themes-and-needs](references/core/themes-and-needs.md) | Uncovering and expressing customer needs as themes and subthemes using user journey maps and opportunity scoring |

### Patterns
| File | Description |
|------|-------------|
| [prioritization-frameworks](references/patterns/prioritization-frameworks.md) | The five frameworks: Critical Path, Kano Model, Desirability / Feasibility / Viability, ROI Scorecard, MoSCoW |
| [alignment-and-buyin](references/patterns/alignment-and-buyin.md) | Shuttle diplomacy, co-creation workshops, and software tools for achieving stakeholder alignment |
| [presenting-and-sharing](references/patterns/presenting-and-sharing.md) | Modular roadmap approach, audience-specific views, and communication best practices |

### Anti-Patterns
| File | Description |
|------|-------------|
| [roadmap-anti-patterns](references/anti-patterns/roadmap-anti-patterns.md) | The most common roadmap-level anti-patterns: feature-date-driven roadmaps, commitment documents, hidden roadmaps, and more |
| [bad-prioritization](references/anti-patterns/bad-prioritization.md) | Seven bad prioritization methods — gut instinct, analyst opinion, popularity-based, and others — with fixes and signals |

### Topics
| File | Description |
|------|-------------|
| [keeping-roadmap-fresh](references/topics/keeping-roadmap-fresh.md) | Roadmap evolution and maintenance: punctuated equilibrium, the iron triangle, and cadence for updates |
| [relaunch-process](references/topics/relaunch-process.md) | Relaunching roadmaps in your organization: the 14-question Roadmap Health Assessment and improvement playbook |
| [glossary](references/topics/glossary.md) | Consolidated definitions of key roadmapping terms used across the book |

---

## Artifacts and Templates

The plugin ships five markdown templates that encode the book's data model as YAML frontmatter plus prose. Commands read these templates and write filled-in copies into the user's current working directory. Agents (especially [roadmap-reviewer](../../agents/roadmap-reviewer.md)) audit the resulting files against the 14-question Health Assessment mapping.

| Template | Purpose | Written to |
|----------|---------|------------|
| [`templates/roadmap.md`](templates/roadmap.md) | Roadmap index: vision, objectives, disclaimer, Now/Next/Later tables linking to theme files | `./roadmap.md` |
| [`templates/theme.md`](templates/theme.md) | One theme per file: customer need, linked objectives, timeframe, confidence, evidence, subthemes, optional ROI score | `./themes/<slug>.md` |
| [`templates/roi-scorecard.md`](templates/roi-scorecard.md) | Prioritization scorecard using (Value / Effort) × Confidence | `./artifacts/scorecard-YYYY-MM-DD.md` |
| [`templates/change-communication.md`](templates/change-communication.md) | Audience-aware roadmap-change announcement with mandatory "Why" section | `./artifacts/change-YYYY-MM-DD-<slug>.md` |
| [`templates/special-request.md`](templates/special-request.md) | Three-qualifying-questions evaluation of an ad-hoc stakeholder request, with iron-triangle trade-off | `./artifacts/request-YYYY-MM-DD-<slug>.md` |

### Default project layout

```
<user project>/
├── roadmap.md
├── themes/
│   ├── ensure-seamless-checkout.md
│   └── ensure-faster-onboarding.md
└── artifacts/
    ├── scorecard-2026-04-13.md
    ├── change-2026-04-20-defer-reporting.md
    └── request-2026-04-22-acme-sso.md
```

### Structural constraints baked into the templates

Every template carries `managed_by: prr` in its frontmatter — this is the discriminator the plugin uses to distinguish its own artifacts from any other `roadmap.md` or `themes/*.md` a user might already have in their project. The plugin's `PostToolUse` validator hook **only inspects files with `managed_by: prr`** and silently ignores everything else.

The frontmatter enforces book-grounded rules so reviewers (and the hook) can verify them mechanically:

- **`managed_by: prr`** — required on every template; identifies the file as plugin-managed.
- **No ship dates** — `timeframe` is an enum of `Now | Next | Later` only.
- **No orphaned themes** — `linked_objectives` is required and must be non-empty.
- **No overconfidence** — `confidence` is an integer 0–99; 100 is prohibited.
- **Disclaimer required** — roadmap frontmatter has a required `disclaimer` field.
- **Vision and objectives required** — a roadmap with neither is a "Roadmap Without Strategic Context" anti-pattern.
- **Prioritization method declared** — roadmap frontmatter names the method used (`roi-scorecard`, `dfv`, `kano`, `moscow`, `critical-path`).
- **`type:` discriminator** on every file — lets agents filter artifacts with a single grep.

The validator hook (`hooks/validate-artifact.py`) runs on every `Write`, `Edit`, and `MultiEdit` and reports violations back to Claude via stderr + exit code 2, so the model self-corrects in-session. User files without `managed_by: prr` are never touched.
