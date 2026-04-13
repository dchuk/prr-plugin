---
description: Run the Roadmap Health Assessment and recommend Approach A or B with next steps
argument-hint: "[optional: context about your current roadmapping process]"
---

# Assess Roadmap Health

**Purpose:** Run the 14-question Roadmap Health Assessment (scored 0–2, max 22 points) to evaluate your organization's roadmapping process, produce an interpreted score, and recommend either Approach A (course corrections) or Approach B (full relaunch) with concrete next steps.

**When to use:**
- Before deciding whether to improve or fully relaunch a roadmapping process
- When stakeholders disagree about how functional the current process is
- After a roadmap has repeatedly failed to align teams or deliver value
- As the first step in the six-step Roadmap Relaunch Process

---

## Steps

### 1. Gather context

Ask the user for any relevant context about their current roadmapping process — team size, how long the roadmap has been in place, recent pain points. If the user has already provided context in the command argument, read it and proceed. This context will help interpret ambiguous answers.

### 2. Administer the 14-question checklist

Walk through each question below interactively. For each question, present it clearly and ask the user to respond with:
- **0** = entirely or mostly no
- **1** = sort of / maybe / not sure
- **2** = definitely yes

**Add points for:**
1. Do stakeholders have a clear product vision they can explain? *(ref: vision & strategy)*
2. Are there measurable business objectives that stakeholders are aware of?
3. Does the roadmap focus on customer needs rather than features?
4. Are all roadmap items tied to customer needs or business objectives?
5. Is the roadmap updated regularly?
6. Is time allowed for the team to learn before committing to specific solutions?
7. Is there an objective and accepted prioritization method in place?
8. Is there an established alignment process with stakeholders?
9. Do you regularly present the roadmap to key internal stakeholders?
10. Do you regularly present the roadmap to customers?
11. Do you seek and incorporate customer feedback into the roadmap?

**Subtract points for:**
12. Does the roadmap include specific features, solutions, fixes, or deliverables? *(subtract score)*
13. Does the roadmap include precise or best-case dates? *(subtract score)*
14. Are solutions thoroughly designed before customer needs are placed on the roadmap, or is project info like resources, milestones, and dependencies embedded in the roadmap? *(subtract score)*

For questions 12–14, treat the user's score as points to **subtract** from the total. Record the raw score for each subtract-question and flip its sign when computing the total.

### 3. Calculate the total score

Sum questions 1–11 (added points) and subtract questions 12–14 (subtracted points). The maximum possible score is 22. Display the calculation clearly:

```
Added:     Q1 + Q2 + ... + Q11  = [sum]
Subtracted: Q12 + Q13 + Q14    = [sum]
─────────────────────────────────────────
Total Score:                     [total] / 22
```

### 4. Interpret the score

Apply the following interpretation:

| Score | Interpretation | Recommended Approach |
|-------|---------------|----------------------|
| 18–22 | Great process | **Approach A** — tweak and enhance your already strong process |
| 12–17 | Room for improvement | **Approach A** — salvageable process, but significant improvements needed; it will take time |
| ≤ 11  | Full relaunch needed | **Approach B** — process is broken or nonexistent; establish a new baseline from scratch |

State the score, the interpretation sentence verbatim from the table above, and the recommended approach prominently.

### 5. Recommend specific next steps by approach

**If Approach A (score ≥ 12):**
- Remind the user of the rule: focus on improving **one part of the process at a time** rather than changing many things at once.
- Based on the lowest-scoring add-questions and the highest-scoring subtract-questions, identify the top 1–2 opportunities for improvement.
- Suggest a concrete near-term goal achievable in a few weeks (e.g., "Adopt a prioritization framework from the five options in the prioritization frameworks reference" or "Establish a regular stakeholder alignment cadence").
- Recommend sharing the assessment results with key stakeholders to build buy-in for the specific changes — involve them in seeing the problem before proposing solutions.
- Note that a cross-functional product steering committee should meet every 3–6 weeks to review progress. Fewer than every 3 weeks is seldom productive; more than every 6 weeks causes shared context to erode.

**If Approach B (score ≤ 11):**
- Recommend starting from scratch by following the book's steps in order: product vision → business objectives → themes → prioritization → alignment → presentation.
- Suggest running a **Roadmap Workshop** — a focused collaborative event modeled on a Design Sprint — to bring together key stakeholders over a few days to define vision, objectives, and customer needs, and produce an initial roadmap.
- Advise limiting the initial stakeholder circle to the product core (product managers, engineers, designers), then expanding gradually.
- Flag that shuttle diplomacy — one-on-one discussions with key stakeholders before any group session — will help surface resistance and build incremental alignment before the workshop.

### 6. Surface subtract-question warnings

For any subtract-question scored 1 or 2, explicitly call out the specific anti-pattern at play:
- **Q12 (specific features/deliverables on roadmap):** This is a signal of a feature-date-driven roadmap — one of the most common roadmap anti-patterns. Roadmaps should express customer needs and outcomes, not solutions.
- **Q13 (precise or best-case dates):** Precise dates create false commitments and erode trust when missed. The roadmap should use Now / Next / Later timeframes instead of calendar dates wherever possible.
- **Q14 (over-designed solutions or project info embedded):** Thoroughly designing solutions before needs are on the roadmap, or embedding resources, milestones, and dependencies, turns the roadmap into a project plan — which it is not.

---

## Output

Produce a structured summary containing:

1. **Score card** — the per-question scores and the total calculation
2. **Interpretation** — score band, plain-language interpretation, and recommended approach (A or B)
3. **Top improvement opportunities** — ranked by score gap, with a one-sentence rationale for each
4. **Immediate next steps** — 3–5 concrete actions the user can take this week, tailored to their approach
5. **Subtract-question warnings** — any active anti-patterns flagged with a brief description

---

## Verify

The command succeeded when:
- All 14 questions have been scored and the total is displayed with the add/subtract breakdown visible
- The correct approach (A or B) is named and justified by the score band
- At least one concrete, time-bound next step is recommended
- Any subtract-question scored above 0 has a corresponding anti-pattern warning

If the total score is on the boundary between bands (e.g., exactly 12 or exactly 18), note the boundary explicitly and let the user decide whether to treat it as the higher or lower band based on their confidence in their scores.

---

## Notes

- **Involve stakeholders in the assessment** when you want to build buy-in for change — having all parties see the same data makes the problem visible and reduces resistance to the recommended approach.
- The six-step Roadmap Relaunch Process continues beyond this assessment: after scoring and choosing an approach, the next steps are stakeholder training, starting small and working incrementally, evaluating results with a steering committee, and keeping the process relaunching continuously.
- For deeper guidance on the relaunch process, including the full workshop facilitation model, see [`../skills/product-roadmaps/references/topics/relaunch-process.md`](../skills/product-roadmaps/references/topics/relaunch-process.md).
- For alignment techniques referenced in Step 2 (shuttle diplomacy, co-creation workshops), see [`../skills/product-roadmaps/references/patterns/alignment-and-buyin.md`](../skills/product-roadmaps/references/patterns/alignment-and-buyin.md).
- For prioritization frameworks to recommend in Approach A next steps, see [`../skills/product-roadmaps/references/patterns/prioritization-frameworks.md`](../skills/product-roadmaps/references/patterns/prioritization-frameworks.md).
- For the full catalogue of roadmap-level anti-patterns flagged by subtract questions, see [`../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md`](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md).
