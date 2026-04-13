# Alignment and Buy-in for Product Roadmaps

## Problem Framing

You've drafted a roadmap. Now you need people to actually support it.

The typical failure mode: a product manager (or engineering lead) builds a release schedule in a spreadsheet, distributes it to stakeholders, and watches half of them celebrate while the other half are enraged. No one understands why decisions were made, no one feels heard, and the artifact has no connection to product strategy. **Silos** kill enthusiasm and momentum — and isolated decision-making is the most common cause of silos. _source: ch11 opening story_

The fix is not to hold one big meeting and force a vote. It's to pursue **alignment** and **collaboration** — not **consensus**. This reference explains how to do that through three mechanisms: shuttle diplomacy, co-creation workshops, and software tools.

---

## Alignment vs. Consensus vs. Collaboration

These three words are often conflated. The book treats them as meaningfully distinct:

**Alignment** — "A concerted effort to help people understand the issues and what their respective roles are. It means asking questions and listening to feedback both from the internal product team as well as external stakeholders. People with differing opinions can still align on their intentions. Alignment is not consensus." _source: ch11 §Alignment, Consensus, and Collaboration Walk into a Bar..._

**Consensus** — "In theory, a group of people reaching a mutually agreed-upon decision. In practice, it often means hours of discussion leading to decisions that everyone supposedly agrees to, but that no individual can be held accountable for. Once the decision has been made, if someone doesn't like it, they can often be a barrier to its implementation." _source: ch11 §Alignment, Consensus, and Collaboration Walk into a Bar..._

**Collaboration** — "When individuals cooperate to accomplish a common goal or outcome. Individuals work together for a shared purpose — they may not concur on everything each step of the way, but they do agree on the final outcome." _source: ch11 §Alignment, Consensus, and Collaboration Walk into a Bar..._

> **Core principle:** You do not need consensus to get your roadmap in place, nor do you need it to update your roadmap. Alignment and collaboration are what you need. _source: ch11 §Alignment, Consensus, and Collaboration Walk into a Bar..._

---

## Shuttle Diplomacy

### What It Is

Shuttle diplomacy means meeting with each stakeholder party individually to reach decisions that require compromise and trade-offs. Borrowed from Henry Kissinger's approach to Middle East negotiations, it allows the product manager to act as an intermediary, focus on common goals, and give each stakeholder co-authorship of the plan.

> "By giving each stakeholder the opportunity to have input early on, the shuttle diplomacy process gives them authorship of the plan — it's not your plan, it's 'our' plan." _source: ch11 §Why Does Shuttle Diplomacy Work?_

### How to Run It

1. Identify all internal and external stakeholders who need to be aligned.
2. Prepare a draft roadmap to use as a conversation artifact. Entice stakeholders with it and ask for their input.
3. Schedule individual one-on-one meetings — keep them short and informal.
4. Open each meeting by tying the discussion to the organization's goals and objectives.
5. Use the **GROW Framework** to guide the conversation:
   - **Goals** — What are they trying to accomplish?
   - **Reality** — What's on their plate right now?
   - **Options** — What do they think will help achieve those goals?
   - **Way forward** — Which options best achieve their stated goals?
6. Focus only on the issues a particular stakeholder cares about; ignore the rest of your list.
7. Record everything in your private Shuttle Diplomacy Canvas (see below).
8. After all one-on-ones, synthesize conflicts and trade-offs, then bring everyone together for a group session.

### The Shuttle Diplomacy Canvas

The canvas is a private tracking table — not shared across the team. For each stakeholder, record:

| Column | What to capture |
|--------|----------------|
| Stakeholder | Name / role |
| Desired outcomes | What they want the product to achieve |
| Reasons / rationale | Why those outcomes matter to them |
| Success metrics | How they measure success |
| Top product priorities | Their ranked list |
| Additional considerations | Office politics, constraints, hidden agendas |

> The shuttle diplomacy canvas is not intended to be shared across your team; use it only as a private guide to track one-on-one conversations. _source: ch11 §Shuttle Diplomacy Canvas_

### Anti-Patterns to Avoid

**Jumping Straight to Group Stakeholder Meetings** — Bringing everyone together before individual one-on-ones exposes the roadmap process to power dynamics, grandstanding, and intimidation. Stronger voices dominate; quieter stakeholders go unheard; hidden agendas remain unaddressed. Fix: use shuttle diplomacy first. _source: ch11 §Shuttle Diplomacy for Product People_

**Seeking Consensus for Roadmap Decisions** — Hours of discussion, no individual accountability, and stakeholders who block implementation after the fact. Fix: pursue alignment and collaboration. _source: ch11 §Alignment, Consensus, and Collaboration Walk into a Bar..._

---

## Co-creation Workshops

### What It Is

A co-creation workshop is "a structured, intense group session that brings all stakeholders together to finalize the roadmap prioritization process. Less a present-the-plan event and more a let's-figure-this-out exercise." It can follow shuttle diplomacy or replace one-on-ones when the team is small and political agendas are minimal.

> The co-creation workshop needs to have a clear plan and outcomes before you hold it. No one wants to go to another unnecessary meeting; the outcome should be to finalize the roadmap for the upcoming period. _source: ch11 §Co-creation Workshop_

### Workshop Agenda (90 minutes)

| Segment | Time | Purpose |
|---------|------|---------|
| Intro | 5 min | Agenda and ground rules |
| Hopes and Fears | 10 min | Surface hidden aspirations and roadblocks |
| Vision and Goals | 10 min | Confirm or establish product vision |
| Back-plan | 15 min | Work backward from future vision to present |
| Sizing and Prioritizing | 40 min | $100 Test + discussion to finalize priorities |
| Wrap-up | 10 min | Confirm decisions, assign next steps |

### Exercises in Depth

**Hopes and Fears** — Each participant writes their hopes for the product's future on one color of Post-it note and their fears on another, one item per note. Hopes and fears that would otherwise remain hidden get surfaced and discussed openly. _source: ch11 §Co-creation Workshop / Hopes and fears_

**Cover Story Exercise** (from _Gamestorming_ by Dave Gray, Sunni Brown, and James Macanufo) — Participants draw the cover of a newspaper or magazine five years in the future after the roadmap has been implemented, including a headline, image, subheadline, sidebars, and a quote. Used for vision articulation when vision is not already set.

**Back-plan** — Starts with the end result of a future-envisioning exercise (such as the Cover Story) and works gradually backward to the present, requiring each step to be realistic. Forces teams to think through all the changes necessary to reach their vision. _source: ch11 §Co-creation Workshop / Back-plan_

**$100 Test** — Each participant is given a limited amount of currency to "invest" in particular customer needs or themes. Results are tallied to narrow focus to a manageable discussion list. A variation divides investment by role category: desirability, feasibility, and viability.

> Voting (e.g., the $100 test) is a good way to narrow your focus to a manageable list for discussion, but not a good way to prioritize. _source: ch11 §Co-creation Workshop / Sizing and prioritizing_

---

## Formal Presentation vs. Co-creation Workshop

After shuttle diplomacy is complete, you have a choice about how to bring the group together:

| Choose **Formal Presentation** when… | Choose **Co-creation Workshop** when… |
|--------------------------------------|---------------------------------------|
| Organization is hierarchical | Culture of constructive disagreement exists |
| Steering committee or executive sign-off process exists | General agreement on strategy already exists |
| Teams are large with defined portfolio review processes | Teams prefer collaborative figuring-out |

_source: ch11 §Meetings and Workshops / Presenting Recommendations and Co-creation Workshop_

---

## Software Tools as a Complement

Software applications are useful when:
- Teams are distributed and cannot engage in face-to-face shuttle diplomacy or in-person workshops
- Used as a complement to meetings to track, tag, and manage product themes
- A recurring lightweight meeting cadence (e.g., weekly) is in place to supplement the software

**Do not** use software as the sole mechanism for obtaining alignment. No team studied relied solely on software tools. _source: ch11 §Software Applications_

---

## When to Use / When NOT to Use

### Shuttle Diplomacy

**Use when:**
- Many stakeholders have competing interests
- Office politics or hidden agendas are likely
- Stronger voices risk dominating quieter stakeholders in a group setting
- You are initiating or significantly updating a roadmap

**Skip (go straight to co-creation workshop) when:**
- The team has a small number of stakeholders
- Political agendas are not overly prevalent
- Stakeholders already share a high degree of trust

### Co-creation Workshops

**Use when:**
- Shuttle diplomacy is complete and final group alignment is needed
- Culture of constructive disagreement exists or can be established
- Team is small enough that group dynamics are manageable

**Do not use when:**
- You haven't defined clear desired outcomes for the session in advance
- Stakeholders refuse to recognize or engage with each other directly (shuttle diplomacy must resolve this first)

### General Rules That Always Apply

- Do not reconsider decisions made in alignment sessions unless there is significant new information. Endless re-litigation destroys momentum.
- One-to-one meetings are always better in person than remote — rapport is a key ingredient in shuttle diplomacy.
- Hold a group alignment meeting on a regular basis — perhaps every quarter or every year — depending on the velocity of change in your business.

---

## Code Examples

The following table structure represents the Shuttle Diplomacy Canvas — the private tracking tool used during one-on-one meetings:

```
Shuttle Diplomacy Canvas (PRIVATE — do not share)

| Stakeholder | Desired Outcomes | Rationale | Success Metrics | Top Priorities | Considerations |
|-------------|-----------------|-----------|-----------------|----------------|----------------|
| VP Sales    | Faster onboarding| Lose deals to competitor | Time-to-first-value < 7 days | SSO integration, CSV import | Influential with CEO; needs early win |
| Head of CS  | Reduce ticket volume | Team is at capacity | Support tickets per user/month | In-app help, guided tours | Prefers data over opinions |
| CTO         | Reduce tech debt | Slow release cadence | Deploy frequency | API refactor | Will block anything not on tech roadmap |
```

The GROW Framework applied in a shuttle diplomacy meeting:

```
GROW Framework — Shuttle Diplomacy Conversation Guide

G — Goals
  "What are you trying to accomplish this year as a team?"
  "Where does the product fit into those goals?"

R — Reality
  "What's on your plate right now that's most pressing?"
  "What's blocking you today?"

O — Options
  "If you could add one thing to the roadmap, what would it be?"
  "What do you think would make the biggest difference for customers?"

W — Way Forward
  "Of those options, which best helps you hit your stated goals?"
  "What would success look like six months from now?"
```

$100 Test tally structure for a co-creation workshop:

```
$100 Test Results

Theme                        | Desirability | Feasibility | Viability | Total
-----------------------------|-------------|-------------|-----------|-------
Ensure faster onboarding     |     $32      |     $18     |   $25     |  $75
Ensure reliability at scale  |     $15      |     $40     |   $30     |  $85
Ensure self-serve reporting  |     $28      |     $22     |   $10     |  $60
Ensure mobile parity         |     $25      |     $20     |   $35     |  $80

→ Use totals to narrow to top 2–3 themes for discussion, not as final priority order.
```

---

## Related References

- [Roadmap Definition](../core/roadmap-definition.md) — Why a release-schedule-as-roadmap fails and what a proper roadmap communicates instead
- [Themes and Needs](../core/themes-and-needs.md) — How to express customer needs as themes before you bring them into shuttle diplomacy or a workshop
- [Prioritization Frameworks](prioritization-frameworks.md) — The five frameworks (Critical Path, Kano Model, Desirability / Feasibility / Viability, ROI Scorecard, MoSCoW) used in the Sizing and Prioritizing segment of co-creation workshops
- [Bad Prioritization Anti-patterns](../anti-patterns/bad-prioritization.md) — Common prioritization mistakes the $100 Test and shuttle diplomacy help you avoid
- [Presenting and Sharing](presenting-and-sharing.md) — What happens after alignment is achieved: audience-specific presentation strategies
- [Run Shuttle Diplomacy command](../../../../commands/run-shuttle-diplomacy.md) — Step-by-step command to plan and execute shuttle diplomacy sessions
- [Roadmap Reviewer agent](../../../../agents/roadmap-reviewer.md) — Reviews a roadmap artifact against alignment and buy-in principles
