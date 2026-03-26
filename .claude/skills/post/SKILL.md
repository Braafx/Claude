---
name: post
description: Turn any artwork into ready-to-post social content. Share an image in chat (photo of sketchbook, traditional piece, or digital work) and get platform-ready captions for Instagram, ArtStation, TikTok, and Twitter/X — plus monetization suggestions and, if it's a sketch, a digital development plan. Use when the user wants to post art, prepare social content, or find out how to monetize a piece.
---

# Art → Social Post Skill

Turn uploaded artwork into copy-paste-ready social posts across all platforms, with monetization angles and (for sketches) a digital development brief.

## Context

The user is building toward a concept art career (games/film, target: Riot Games). They post to Instagram, ArtStation, TikTok, and Twitter/X. They draw daily — sketchbook + digital. Traditional and sketch posts are as valid as digital finished pieces. The goal is to make posting frictionless so they actually do it consistently.

---

## Workflow

### 1. Receive the artwork

The user will share an image in chat. If no image is shared yet, say:
> "Drop your artwork in the chat (photo of sketchbook, traditional piece, or digital screenshot) and I'll prepare everything."

### 2. Analyse the image

Look at the image and determine:

- **Media type:** pencil sketch / ink / traditional paint / digital / photo of sketchbook page
- **Subject:** character · prop/artifact · environment/scene · portrait · creature · meme/illustration · texture study
- **Completeness:** rough sketch · mid-stage WIP · near-finished · polished/complete
- **Mood/tone:** (e.g. dark fantasy, bright cartoon, sci-fi, atmospheric, action, etc.)
- **Tools visible or likely:** pencil, ink, markers, Procreate, Photoshop, CSP, etc.

Do NOT ask the user for this information — infer from the image. Only ask if something is genuinely ambiguous (e.g. "What app did you use for this?").

### 3. Generate the social pack

Output all four platforms in sequence, clearly separated. Use this exact structure:

---

## Social Pack — {brief title for the piece} · {YYYY-MM-DD}

---

### 📸 Instagram

```
{2–3 sentences. Sentence 1: what it is. Sentence 2: mood/intent or story behind it. Sentence 3: optional — call to action or personal note. Keep it human, not corporate.}

{10–12 hashtags from the bank below, selected for this specific piece}
```

**Hashtag bank to draw from:**
Core: #conceptart #gameart #digitalpainting #artstation #traditionalart #sketchbook
Character: #characterdesign #characterconcept #gamecharacter #oc
Environment: #environmentdesign #environmentconcept #digitalpainting
Props: #propdesign #gameprops #fantasyprop
Style: #stylized #fanart #indiegame #darkfantasy
Process: #wip #artistsoninstagram #sketchbookdaily #dailysketch
Audience: #procreate #ipadart #digitalart #illustration #pencildrawing #inkdrawing

---

### 🎨 ArtStation

```
{3–4 sentences, professional tone. What it is + concept intent + tools used + any context (personal project, commission, study). This is your portfolio description.}

Tags: {6–8 comma-separated ArtStation tags}
```

---

### 🎵 TikTok

```
Hook (first 3 sec on screen): {One punchy line — question, bold statement, or surprising fact about the piece}

Caption: {1–2 casual sentences. Conversational. Can include "POV:", "me when", or similar TikTok-native phrasing if it fits the piece. Don't force it.}

{5–7 hashtags — mix of niche and broad: #conceptart #artistsoftiktok #digitalart + specific ones}
```

---

### 𝕏 Twitter/X

```
{1 sentence max. Sharp, direct. No filler. If it's concept art: lead with what makes it interesting, not "I made this". If it's a sketch: own the roughness.} {2–3 hashtags inline or at end}
```

---

### 4. Monetization breakdown

After the social pack, add this section:

---

## 💰 Monetization Angles

**Piece type:** {character/prop/environment/sketch/etc.}

| Option | Fit | Action |
|--------|-----|--------|
| {option 1} | ⭐⭐⭐ / ⭐⭐ / ⭐ | {one-line action} |
| {option 2} | ⭐⭐⭐ | {one-line action} |
| {option 3} | ⭐⭐ | {one-line action} |

**Best immediate move:** {one clear sentence on what to do with this piece right now}

**Platforms to list it on:**
- {relevant platform + link if applicable}

**Realistic price range:** {e.g. "Print: £15–35 on INPRNT · Sticker: £3–5 on Redbubble · Commission-style: £80–150 for similar work"}

Use this reference to populate the table:

- **Print on demand** (characters, environments, finished pieces): INPRNT (inprnt.com — artist-friendly, 50% royalty), Redbubble, Society6
- **Commission showcase** (any finished piece): add to ArtStation, price similar work at current rate (emotes £40–60, character sheets £100–200, props £60–120)
- **Emote potential** (characters, expressions, simple icons): mention to streamer communities, Discord servers, Fiverr
- **Process tutorial** (any piece with clear stages): sell as a Gumroad PDF/video, price £5–15 for beginners
- **Merch** (strong graphic pieces, characters, props): stickers (Redbubble/Teepublic), prints, phone cases
- **Indie game client bait** (props, environments, creatures): ArtStation visibility + DM indie devs on Twitter/itch.io communities
- **Stock art** (textures, environments, abstract): Getty, Shutterstock contributor (low rates but passive)
- **Ko-fi / Patreon** (any consistent work): support tier for monthly art drops, WIPs, brushes

---

### 5. Digital development brief (if sketch or traditional)

If the piece is a sketch, rough, or traditional (not a finished digital piece):

---

## ✏️ Digital Development Brief

**Take this to digital — here's your brief:**

**Subject:** {specific description of what to render — based on the sketch}
**Mood / Tone:** {inferred from sketch or suggest one that elevates it}
**Lighting challenge:** {specific setup that would suit this subject}
**Colour palette:** {3–4 colours that would work}
**One technical focus:** {the single most important skill to practise with this piece}
**Scope:** {realistic time — 1 hr study / 2 hr full piece / 30 min speed paint}

**Process:**
1. THUMBNAIL (5 min) — does the composition read smaller than your hand?
2. VALUE BLOCK (10–15 min) — greyscale, 3 values max
3. COLOUR PASS (10–15 min) — temperature first, hue second
4. DETAIL PASS — large shapes first, one focal point gets the sharpest treatment
5. FINAL PUSH (5 min) — brightest highlight, darkest dark, one sharp edge

---

### 6. Save the output

Create the directory and file:

```bash
mkdir -p social/{YYYY-MM-DD}-{slug}
```

Where `{slug}` is a 2–3 word kebab-case description of the piece (e.g. `stone-rune-prop`, `warrior-sketch`, `forest-environment`).

Write the full output (social pack + monetization + development brief) to:
`social/{YYYY-MM-DD}-{slug}/posts.md`

Then commit:
```bash
git add social/
git commit -m "Add social pack: {slug} — {YYYY-MM-DD}"
```

Confirm to the user:
> "Done. Social pack saved to `social/{YYYY-MM-DD}-{slug}/posts.md` and committed. Copy-paste from there whenever you're ready to post."

---

## Notes for Claude

- **Traditional art is equally valid.** A sketchbook page posted raw is legitimate content — don't suggest it's incomplete or needs to be digital first.
- **Tone calibration:** Instagram captions should sound like a person, not a brand. ArtStation should be professional. TikTok should be casual and direct. Twitter/X should be punchy.
- **Don't over-hashtag Instagram.** 10–12 is the sweet spot. More looks spammy.
- **The monetization table should be honest.** If a rough sketch isn't print-ready, say so. If a piece is genuinely strong, lead with the highest-value option.
- **If the image is a WIP:** note that in the Instagram/TikTok posts explicitly — "WIP" content often outperforms finished work on social because it invites engagement.
- **Post timing advice (if asked):** Instagram: 6–9pm weekdays, 10am–2pm weekends. TikTok: 7–9pm. ArtStation: any time, SEO matters more than timing.
