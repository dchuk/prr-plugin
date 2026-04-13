---
type: change-communication
change_date: YYYY-MM-DD
change_depth: small                 # small | broad | fundamental
affected_themes: [TH-001]           # Theme IDs touched by this change
audiences: [dev-team, executives, sales-marketing, customers]
author: <name/role>
---

# Roadmap change: <short title>

## Why

<2–3 paragraphs. The rationale is the most important section — "Hiding the Why" is a named anti-pattern. Explain what changed in the world (new data, customer signal, strategic shift, competitive move, regulatory change) and why the previous plan no longer fits.>

## What changed

- **Deferred:** <theme> from <Now → Next | Next → Later>. Reason: <…>
- **Accelerated:** <theme> from <Later → Next | Next → Now>. Reason: <…>
- **Added:** <theme>. Reason: <…>
- **Removed:** <theme>. Reason: <…>

## When

- Artifact update published: YYYY-MM-DD
- Stakeholder briefings complete by: YYYY-MM-DD
- Next review checkpoint: YYYY-MM-DD

## Audience variants

### For the dev team

<Stage changes (discovery / design / prototyping / alpha / beta), technical-debt implications, sequencing impact on current sprints.>

### For executives

<Vision-level framing. Which objectives accelerate, which slow, expected impact on key results.>

### For sales / marketing

<What is safe to commit to, what is directional only. Include confidence language and hedging — never quote internal confidence percentages externally without caveats.>

### For customers (if externally shared)

<Benefit-framed summary. No internal theme IDs, no confidence numbers, no dates unless already committed contractually.>

## Socialization checklist

- [ ] `roadmap.md` updated with new timeframe placement
- [ ] Affected theme files updated (timeframe, confidence, change log entry)
- [ ] This change-communication filed under `artifacts/`
- [ ] Dev-team briefing held
- [ ] Executive briefing held
- [ ] Sales/marketing briefing held
- [ ] Customer-facing comms drafted (if applicable)
