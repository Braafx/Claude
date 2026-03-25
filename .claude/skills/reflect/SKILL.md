---
name: reflect
description: Run a weekly personal reflection covering work and life. Asks 5 short questions and writes a structured entry to reflections/YYYY-WXX.md. Use when the user wants to review their week, check in on goals, or do a personal retrospective.
---

# Weekly Reflection Skill

A short, structured personal review. 5 questions. Takes 5 minutes. Writes to `reflections/YYYY-WXX.md`.

## Workflow

### 1. Get the week identifier

```bash
date +%Y-W%V
```

Check if `reflections/YYYY-WXX.md` already exists. If it does, ask:

> "A reflection for this week already exists. Overwrite it, or append a new entry?"

### 2. Ask the 5 questions (one at a time)

Present each question and wait for the user's answer before moving to the next. Keep it conversational — this is a personal check-in, not a form.

**Q1:** What went well this week — work or personal?

**Q2:** What drained your energy or felt stuck?

**Q3:** One thing you'd do differently next week.

**Q4:** Are your current habits aligned with your goals? (Yes / Mostly / No — add one note)

**Q5:** What's the single most important focus for next week?

### 3. Write the reflection file

Create `reflections/` directory if it doesn't exist.

Format:

```markdown
# Reflection — YYYY-WXX

> Written: YYYY-MM-DD

## What went well
<Q1 answer>

## What drained energy / felt stuck
<Q2 answer>

## One thing to do differently
<Q3 answer>

## Habits aligned with goals?
<Q4 answer>

## Single focus next week
<Q5 answer>
```

### 4. Optionally update LIFE.md

After writing, check `LIFE.md`:
- If the user's Q5 focus differs from the current "This week's single most important thing" in `LIFE.md`, ask: "Want me to update LIFE.md with next week's focus?"
- If yes, update the relevant line in `LIFE.md`.

### 5. Commit

```bash
git add reflections/YYYY-WXX.md
# If LIFE.md was updated:
git add LIFE.md
git commit -m "Add weekly reflection for YYYY-WXX"
```

Do not push — the stop hook handles that at session end.

## Wrap up

Confirm the file is written and committed. Show a one-line summary:

> "Week YYYY-WXX logged. Focus next week: <Q5 answer>"
