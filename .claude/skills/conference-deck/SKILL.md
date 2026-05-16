---
name: conference-deck
description: Creates solo-presenter conference/event presentation decks that weave one or more customer case studies into the narrative arc of an accepted session abstract. Outputs a slide-by-slide Markdown outline with speaker notes, generates a PPTX, and can produce opener/close scripts. For external conference talks, not internal sales pitches.
autoload: false
---

# Conference Deck Builder

This skill creates presentation decks for accepted conference sessions. The speaker is typically a solo presenter who needs to deliver the arc promised in the abstract by walking the audience through one to three customer case studies and a synthesis.

## When to use this skill

- You have an **accepted abstract** for a conference, summit, or industry event.
- The session is **20 to 45 minutes**, delivered by a solo presenter (not a panel).
- You have **one to three customer stories** to weave into the arc.
- You need a **visual deck** with minimal on-slide text and speaker notes that carry the delivery.

## When not to use this skill

- If you need a B2B sales pitch, use `/sales-deck` (April Dunford methodology).
- If the session is a **panel** (multiple live voices in dialogue), use `/sales-deck` or build a panel flow manually. This skill assumes single-presenter pacing.
- If you need a product demo walk-through, this is not the right shape.

---

## Core philosophy

Conference talks are about **narrative plus evidence**. The abstract is a contract with the audience: you promised them a journey and takeaways. The deck exists to deliver that contract, with customer stories as the evidence.

Three rules that make conference decks work:

1. **Slides are sparse. Speaker notes are rich.** The audience reads the room and your face, not your text. On-slide text belongs to the one or two things they should remember after blinking.
2. **Every case study maps to a question the abstract raised.** No case study is introduced in isolation. Each one answers a specific promise.
3. **The synthesis slide is non negotiable.** If your talk is two case studies and you do not stitch them together, the audience leaves with two anecdotes, not a thesis.

---

## Step 1: Gather inputs

Read these files from the repo first (do not ask the user for what is already available):

| File | What to extract |
|------|-----------------|
| `docs/inputs/product_brief.md` | Product capabilities, limitations (to verify no fabricated claims) |
| `docs/inputs/testimonials.md` | Approved customer quotes and metrics |
| `docs/inputs/brand_guidelines.md` | Visual style, font, palette hints for PPTX |
| `.claude/rules/content-guidelines.md` | Formatting rules (no dashes, banned words, etc.) |

If `docs/inputs-local/` exists, prefer it over `docs/inputs/`.

**Then ask the user for:**

1. **The accepted abstract.** Full text, as submitted.
2. **The key takeaways.** What the audience should walk out with. Usually provided alongside the abstract.
3. **The case studies.** For each one, either:
   - A URL to a public case study, or
   - A local Markdown file path, or
   - Pasted content
4. **Session duration.** Usually 15, 20, 30, or 45 minutes.
5. **Speaker name and title.** For the title slide and footer.
6. **Event name and date.** For the footer.
7. **Optional:** opener length (30s default) and close length (60s default) if they want the prose scripts.

Do not proceed until you have the abstract, takeaways, and at least one case study. Everything else can have reasonable defaults.

---

## Step 2: Read the source material

For each case study, **fetch or read the full content** and extract verbatim:
- Company name and one-line description
- The specific problem they faced
- What they deployed
- Measurable outcomes (numbers, metrics, quotes)
- Direct quotes from named employees (name, title, company)

**Never paraphrase a metric.** If the case study says "1,000+ users," write "1,000+ users," not "over a thousand users."

**Never invent a quote.** If a usable quote does not exist, skip it or flag the gap.

**Never claim a capability not in `product_brief.md`.** If the case study mentions a capability, verify it against the brief before including.

---

## Step 3: Map the narrative arc

Use the abstract's framing to decide the arc. Most accepted abstracts name the questions they will answer or the themes they will cover. Treat those as section breaks.

### Default arc (works for most conference sessions)

| Section | Slides | Time (for 20 min) | Purpose |
|---|---|---|---|
| **Setup** | 2 to 3 | ~3 min | Title + premise + questions/framework the talk will answer |
| **Case study 1** | 3 to 4 | ~5 min | Problem → solution → outcomes → pull quote |
| **Case study 2** (optional) | 3 to 4 | ~5 min | Same shape, different angle |
| **Case study 3** (optional) | 3 | ~4 min | Compressed version |
| **Synthesis** | 2 to 3 | ~4 min | Cross-case pattern, framework, accountability |
| **Take home** | 1 to 2 | ~2 min | 3 to 5 bullets mapped back to the abstract's takeaways |

### Slide count heuristic

Target roughly **1 slide per 1.4 to 1.5 minutes**. For a 20-minute solo talk, 13 to 15 slides. For 30 minutes, 18 to 22. For 45 minutes, 25 to 30.

### Case study sub-structure (repeat for each)

Every case study follows the same four-beat pattern so the audience learns the rhythm:

1. **Problem.** What did they face? Specific, with context.
2. **Deployment.** What did they build or deploy? Four bullets max.
3. **Outcomes.** KPI grid or table with verbatim numbers.
4. **Pull quote.** Named human, full attribution.

---

## Step 4: Generate the Markdown outline

Output the outline to `output/decks/[slug]-[event].md` (create the directory if it does not exist).

### Required structure

```markdown
# [Session Title]

**Event:** [Event name, year]
**Format:** [Duration] solo presentation
**Speaker:** [Name, Title, Company]
**Source case studies:**
- [Company 1]: [URL]
- [Company 2]: [URL]
**Slide count:** [N] · ~[min per slide] min per slide

---

## Abstract

[Lightly edited version of the submitted abstract, with content-guidelines rules applied: no dashes, no banned words.]

---

## Slide 1 — Title

**On slide:**
> [Session title]

**Visual:** [Layout direction, imagery hint, where logos go]

**Speaker notes:** [30 to 80 words. What the presenter says when this slide is on screen.]

---

[Continue for every slide...]

---

## Production notes

- [Presenter confirmations needed]
- [Logos and headshots to source]
- [Event-specific: hashtag, AV constraints, sponsor acknowledgments]
- [Rules check: no dashes in body copy, no banned words, every number and quote pulled verbatim from source]

---

## 30-second opener (optional)

> [Full prose script, ~75 words]

## 60-second close (optional)

> [Full prose script, ~150 words]
```

### Slide formatting rules

Applied to **every** slide:

| Rule | Why |
|---|---|
| **On-slide text: max 6 lines, max 10 words per line** | Audience scans, does not read |
| **Bold the one thing** on each slide | Gives the eye an anchor |
| **Pull quotes get their own slide** | A quote fighting for space with bullets loses |
| **KPIs are tiles or tables, not bullets** | Numbers deserve visual weight |
| **Every slide has speaker notes** | The deck without notes is just scenery |
| **Section labels are small-caps in an accent color** | Signals structural transitions without stealing focus |
| **No title exceeds two lines** | If it does, the title is doing too much |

---

## Step 5: Generate the PPTX

After the Markdown outline is approved, generate a PPTX. The PPTX reflects what the outline specified. Write a custom Python script per deck, save it to `scripts/build_[slug]_deck.py`, and run it.

### Script template

Adapt this skeleton. It uses `python-pptx` and produces a 16:9 widescreen deck. Reference the Identiverse sample generator in `.claude/skills/conference-deck/example_generator.py` (included with this skill) for a complete working example with KPI grids, pull quote slides, section labels, and a pattern-comparison table.

```python
"""Build [event] deck: [title]."""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = Path(__file__).resolve().parents[1] / "output" / "decks" / "[slug].pptx"

# Palette — adjust per brand_guidelines.md
BG = RGBColor(0x0A, 0x0F, 0x1C)       # deep background
INK = RGBColor(0xF5, 0xF7, 0xFA)      # primary text
MUTED = RGBColor(0x9A, 0xA3, 0xB2)    # secondary text
ACCENT = RGBColor(0x3B, 0xE8, 0xB0)   # accent 1
ACCENT2 = RGBColor(0xFF, 0x6A, 0x3D)  # accent 2
ROW_ALT = RGBColor(0x13, 0x1A, 0x2B)  # tile / alt row fill

FONT = "Helvetica Neue"
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# Helper functions: paint_background, add_textbox, add_bullets, add_accent_bar,
# add_section_label, add_slide_title, add_footer, set_notes, add_table, add_kpi_grid
# (Copy from example_generator.py)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
blank = prs.slide_layouts[6]

# Build each slide explicitly. Do not try to parse the Markdown outline —
# slides in this skill are visually distinct enough that explicit construction
# produces better results than a generic parser.

# Slide 1: Title
# Slide 2: Premise
# ...

prs.save(str(OUT))
print(f"Saved: {OUT} ({len(prs.slides)} slides)")
```

### Why explicit over generic

A generic Markdown-to-PPTX parser produces bullets-on-bullets slides. Conference decks have visual variety: title walls, three-column framing slides, KPI grids, pull quotes with accent bars, pattern tables. Writing each slide explicitly (50 lines of Python per slide) produces a deck that matches the outline and looks designed, not generated.

### Install and run

```bash
pip install python-pptx --break-system-packages --quiet
python3 scripts/build_[slug]_deck.py
```

### Palette adjustments

Before generating, check `docs/inputs/brand_guidelines.md` for brand colors. If the brand uses a light theme, swap BG → near white and INK → near black. If the brand specifies a font, swap `FONT`. Never embed a font the presenter's machine will not have.

---

## Step 6: Opener and close scripts (optional)

When requested, write full-prose scripts the presenter can read verbatim.

### 30-second opener (~75 words)

- Hook: one claim or observation that reframes the topic.
- Promise: what the next N minutes will cover.
- Handoff: transition into slide 2.

### 60-second close (~150 words)

- Recap: one sentence per case study with the landing number.
- Synthesis: the pattern that holds across cases.
- Take-home: restate the takeaway bullets from the abstract.
- Thank you.

Save both in the Markdown outline under their own headings, and also echo to the user in chat so they can copy-paste.

---

## Self-review checklist

Before delivering, verify the deck passes these checks:

### Narrative
- [ ] Every slide maps to a section defined in the arc (Setup, Case study N, Synthesis, Take home)
- [ ] Every case study has the four-beat sub-structure (problem, deployment, outcomes, quote)
- [ ] The synthesis slide pulls a pattern from two or more cases — not a summary
- [ ] Take-home bullets mirror the abstract's original takeaway promises

### On-slide text
- [ ] No slide exceeds 6 lines
- [ ] No line exceeds 10 words
- [ ] Every slide has a visual direction note (layout, imagery)
- [ ] Every slide has speaker notes
- [ ] Titles are at most two lines

### Content rules
- [ ] No dashes in body text (rewrite if needed; the literal session title can keep hyphens)
- [ ] No banned words (robust, seamless, leverage, cutting-edge, revolutionary, transformative, pivotal, integral, nuanced, foster, glean, underscore, propel, unparalleled, vast, plethora, game-changer, delve, landscape)
- [ ] No passive voice
- [ ] No rhetorical question at the end of any slide or of the talk

### Factual accuracy
- [ ] Every metric is verbatim from the source case study
- [ ] Every quote is verbatim and correctly attributed (name, title, company)
- [ ] No capability claimed that is not in `product_brief.md`
- [ ] Source URLs listed at top of the Markdown outline

### PPTX
- [ ] Slide count is roughly duration (min) ÷ 1.4
- [ ] Speaker notes attached to every slide in the PPTX (not just the Markdown)
- [ ] Brand palette applied (check `brand_guidelines.md`)
- [ ] Title slide and take-home slide both show presenter name
- [ ] Footer includes event name and either year or hashtag

---

## Adaptation notes

### If only one case study is available

- Expand the case study section to 5 or 6 slides instead of 3 or 4.
- Add a "what this means more broadly" slide that generalizes from one example.
- Lean more on the abstract's framework for structure.

### If the talk is a panel, not solo

- This skill is not the right tool. Use the case study sub-structure as content source, but let the moderator write discussion prompts instead of slide content.

### If the customer has not cleared public naming

- Use "Fortune 500 semiconductor company" framing and flag the attribution as pending comms approval.
- Do not use logos or headshots.
- Keep metrics since they are aggregate.

### If the abstract is vague

- Push back before drafting. Ask: "What are the three specific things the audience should walk out with?" Build the arc from those, not from the abstract's marketing copy.

### If time is tight the day of

- Minimum viable cut: Title → Premise → 1 slide per case study (problem + outcomes combined) → Synthesis → Take home. That is 6 slides and hits the arc.

---

## Output paths

| Artifact | Path |
|---|---|
| Markdown outline | `output/decks/[slug]-[event].md` |
| PPTX | `output/decks/[slug]-[event].pptx` |
| Build script | `scripts/build_[slug]_deck.py` |
| Example generator | `.claude/skills/conference-deck/example_generator.py` |

Create `output/decks/` and `scripts/` if they do not exist.
