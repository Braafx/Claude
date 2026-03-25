---
name: draw
description: Generate a concept art brief for today's drawing session. Solves "what to draw" by giving a focused subject, mood, lighting challenge, and one technical skill to practice. Tailored for game/film/TV concept art. Use when the user wants a drawing prompt, daily brief, or doesn't know what to work on.
---

# Daily Art Brief Skill

Generate a focused concept art brief for today. One clear direction. No decision fatigue.

## Context

The user is building toward a career as a concept artist (games, film, TV — target: Riot Games tier).
They draw daily. They sketch in a physical sketchbook and also work digitally.
Their current struggle: choosing what to draw, and digital painting without tutorial structure.
Their strength: daily habit, stylized/atmospheric rendering, strong lighting instinct (see stone cube piece).

## Workflow

### 1. Check for context

Ask (one question only):
> "Quick mode or guided? Quick = I give you a brief now. Guided = I ask 2 questions first."

**If quick mode:** Skip to step 3.
**If guided mode:** Ask these 2 questions before generating:
1. "Sketch or digital today?"
2. "Do you want to stay in your comfort zone and build confidence, push into something new, or somewhere between?"

### 2. Pick a category (weighted toward portfolio relevance)

Choose one category. Rotate to avoid repetition — don't pick the same category two sessions in a row if possible:

- **Prop / artifact** (e.g. ancient weapon, magical object, game item) — *strong for portfolio, manageable scope*
- **Environment thumbnail** (e.g. ruin, cave entrance, exterior establishing shot) — *industry standard skill*
- **Creature / character silhouette study** (e.g. monster, NPC, armour design) — *broadens range*
- **Material / texture study** (e.g. rusted metal, fabric, stone, wood) — *directly improves digital painting*
- **Lighting study** (e.g. take a simple subject, do 3 lighting variations) — *unlocks digital confidence*

Bias toward what the user hasn't done recently and what builds the weakest area.

### 3. Generate the brief

Format exactly like this:

---

## Today's Brief

**Subject:** [specific thing to draw — 1 sentence, not vague]

**Mood / Tone:** [e.g. "eerie and ancient", "high fantasy epic", "sci-fi industrial", "dark fairytale"]

**Lighting challenge:** [specific lighting setup — e.g. "single cool rim light from above", "warm interior light with deep shadows", "overcast flat light — sell it through texture not contrast"]

**Colour palette:** [3–4 word palette — e.g. "deep navy, slate grey, gold accent" or "warm ochre, burnt sienna, black"]

**One thing to focus on technically:** [single concrete skill — e.g. "cast shadow shapes", "edge variation (hard vs soft)", "value grouping — max 3 values", "silhouette readability at thumbnail size"]

**Scope:** [realistic time estimate — e.g. "30–45 min sketch" or "1–2 hr digital study" or "quick 15 min warmup"]

**Why this brief:** [1 sentence explaining how this builds toward their industry goal — make it feel purposeful]

---

### 4. If they're doing digital — give a process skeleton

If the session is digital (or they seem to be doing digital), also provide this painting structure after the brief. This replaces the need for a tutorial:

```
PROCESS (use this until it's automatic):

1. THUMBNAIL (5 min)
   → Tiny. No detail. Just value shapes and composition.
   → Does the silhouette read at 100px wide? If no, fix it here.

2. VALUE BLOCK (10–15 min)
   → Greyscale only. 3 values maximum: dark, mid, light.
   → Lock in the lighting logic before adding anything.

3. COLOUR PASS (10–15 min)
   → New layer, set to Color or Soft Light mode over values.
   → Start with the dominant tone, then add temperature contrast.

4. DETAIL PASS (remaining time)
   → Work from large shapes to small. Never detail a shape that isn't working.
   → One focal point gets the most detail. Everything else: suggestion only.

5. FINAL PUSH (last 5 min)
   → Brightest highlight. Darkest dark. One sharp edge at the focal point.
   → Step back: does it read in 3 seconds? That's the test.
```

### 5. Follow-up offer

End with:
> "Want me to art-direct you as you go, or check in when you're done? I can give feedback on a photo/screenshot of the piece."

## Notes

- Never generate vague prompts like "draw a character". Always give specificity — that's what makes the brief useful.
- The process skeleton is the anti-tutorial: it's a personal structure they own, not someone else's workflow to follow.
- If the user shares a finished piece, give specific feedback: what's working (lighting, silhouette, mood), what to push further, and one concrete thing to try next time.
