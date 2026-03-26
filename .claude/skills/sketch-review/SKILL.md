---
name: sketch-review
description: Evaluate a sketchbook page with multiple sketches and pick the best one to develop digitally. Share a photo of your sketchbook and get a scored breakdown of each sketch, a recommended pick with reasoning, and a full digital development brief for the top choice. Use when you have multiple sketches and don't know which to work up, or when you want a second opinion on which sketch has the most potential.
---

# Sketch Review Skill

Look at a full sketchbook page, evaluate every sketch on it, pick the winner, and generate a development brief — so you never waste time on the wrong sketch.

## Context

The user draws daily in a physical sketchbook they carry everywhere. The bottleneck is choosing which sketch to take digital. This skill removes that friction.

---

## Workflow

### 1. Receive the sketchbook photo

The user will share a photo of their sketchbook page. If no image is shared:
> "Take a photo of your sketchbook page (or a page you've been working on) and drop it in. I'll evaluate each sketch and pick the one with the most potential."

### 2. Evaluate every visible sketch

Look at the photo. Identify each distinct sketch on the page (label them 1, 2, 3, etc. working left-to-right, top-to-bottom).

For each sketch, assess:

| Criterion | What to look for |
|-----------|-----------------|
| **Silhouette strength** | Does the shape read clearly even at small size? |
| **Narrative potential** | Does it suggest a world, a story, a character with a life? |
| **Portfolio relevance** | Would this, rendered, fit a game/film concept art portfolio? |
| **Development effort** | How much work to take it to a polished digital piece? (low/med/high) |
| **Originality** | Does it have a distinct voice or is it generic? |
| **Technical foundation** | Are proportions, perspective, and construction solid enough to build on? |

### 3. Output the evaluation

Format exactly like this:

---

## Sketch Review — {YYYY-MM-DD}

**Page summary:** {1 sentence on the overall energy of the page — what kind of session was this?}

---

### Sketch 1 — {brief descriptor, e.g. "hooded figure, 3/4 view"}

| Criterion | Score | Note |
|-----------|-------|------|
| Silhouette | ⭐⭐⭐ / ⭐⭐ / ⭐ | {one note} |
| Narrative | ⭐⭐⭐ / ⭐⭐ / ⭐ | {one note} |
| Portfolio fit | ⭐⭐⭐ / ⭐⭐ / ⭐ | {one note} |
| Dev effort | Low / Med / High | {one note} |
| Originality | ⭐⭐⭐ / ⭐⭐ / ⭐ | {one note} |
| Foundation | ⭐⭐⭐ / ⭐⭐ / ⭐ | {one note} |

**Overall:** {1–2 sentences. Honest assessment. If it's weak, say so clearly and why.}

---

{Repeat for each sketch on the page}

---

### 🏆 Top Pick: Sketch {N} — {descriptor}

**Why this one:** {2–3 sentences. Explain the specific reasons — silhouette, narrative, portfolio value, or a combination. Be concrete, not generic.}

**Runner-up:** Sketch {N} — save this for a future session. {One sentence on what makes it worth returning to.}

---

### 4. Generate the digital development brief for the top pick

Immediately after the evaluation, provide this:

---

## ✏️ Digital Development Brief — Sketch {N}

**Subject:** {Specific description of what to render — based on the chosen sketch, more precise than what's on the page}

**What to keep from the sketch:** {what's already working — composition, pose, energy — preserve this}

**What to clarify digitally:** {what's ambiguous or rough in the sketch that the digital pass should resolve — anatomy, perspective, material, etc.}

**Mood / Tone:** {inferred or suggested — what emotional register should the finished piece land in?}

**Lighting setup:** {specific setup that suits the subject and mood}

**Colour palette:** {3–5 colours with brief reasoning}

**One technical focus:** {the single skill to practise with this piece}

**Scope:** {realistic time — 30 min study / 1 hr focused / 2 hr full piece / multi-session}

**Process:**
1. THUMBNAIL (5 min) — redraw tiny, confirm composition holds
2. VALUE BLOCK (10–15 min) — greyscale, 3 values max, lock the light
3. COLOUR PASS (10–15 min) — temperature first, then hue
4. DETAIL PASS — one focal point, everything else suggestion only
5. FINAL PUSH (5 min) — sharpest edge, brightest light, deepest dark

---

### 5. Social potential flag

After the brief, add a quick note:

> **Post potential:** {Is this worth posting as a sketch now, before going digital? Yes/Maybe/No — with one-line reason. Example: "Yes — the energy in the linework reads well even raw. Post with #dailysketch before you render it."}

---

### 6. Save and commit

Create directory and write file:

```bash
mkdir -p social/{YYYY-MM-DD}-sketch-review
```

Write the full evaluation + development brief to:
`social/{YYYY-MM-DD}-sketch-review/notes.md`

Commit:
```bash
git add social/
git commit -m "Add sketch review {YYYY-MM-DD}: picked sketch {N} for digital development"
```

Confirm:
> "Review saved to `social/{YYYY-MM-DD}-sketch-review/notes.md`. Your digital brief for Sketch {N} is ready — run `/draw` with this brief already loaded, or dive straight in."

---

## Notes for Claude

- **Be honest.** If none of the sketches are strong, say so clearly and explain why — then suggest which is still most worth developing, with the caveat noted.
- **Don't review thumbnails or margin doodles** unless the user specifically points at one. Focus on the intentional sketches.
- **If there's only one sketch on the page**, skip the evaluation table and go straight to the development brief, noting what's working and what to clarify digitally.
- **Post potential is about the sketch as-is** — rough sketches with strong gestural energy often outperform polished work on social. A confident messy line is authentic. Acknowledge that.
- **Sketchbook pages are valid portfolio content.** Don't imply the sketch needs to become digital to be worth sharing.
