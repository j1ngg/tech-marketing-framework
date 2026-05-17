# SEOkrates Marketing Setup

This repo is a fork of [tech-marketing-framework](https://github.com/j1ngg/tech-marketing-framework) configured for SEOkrates marketing work.
The `docs/inputs-local/` folder (gitignored) contains pre-filled SEOkrates context. All skills read from there automatically.

---

## What Was Pre-filled vs What Still Needs Your Input

### Pre-filled (ready to use as a starting point)
| File | Status | What's in there |
|------|--------|-----------------|
| `product_brief.md` | Good | Pricing (START $0/5 gen, PRO $12/mo unlimited), all 12 live languages, tech stack, EN as primary marketing language, limitations |
| `target_personas.md` | Updated | International SEO freelancer (primary), multi-market e-commerce operator (primary), small SEO agency (secondary), local CZ/SK user (tertiary), anti-persona defined |
| `messaging_positioning.md` | Updated | EN-first positioning, "multilingual SEO platform" category frame, pricing contrast messaging ($12 vs $99+), content acquisition strategy |
| `competitor_intel.md` | Hypothesis | Direct competitors with known pricing and weaknesses; indirect alternatives; win/loss hypotheses — validate with how-they-market agent |
| `brand_guidelines.md` | Filled | Brutalist terminal aesthetic confirmed from CSS. Colors: black #000000 bg, white #ffffff text, amber #ffaa00 accent. Fonts: Inter + JetBrains Mono. Logo paths noted. |
| `testimonials.md` | Has 1 lead | One real customer contact in outreach queue (PII-protected, gitignored). No approved quotes yet. |

### Still Needs Your Input (TODOs)

**Unblocked now — do these first:**
- [ ] **Outreach to first customer** — Contact in `testimonials.md`. One real quote unlocks proof sections across all content assets.
- [ ] **Competitor validation** — Run `Analyze how Mangools markets` and `Analyze how Collabim markets`. Which competitors actually come up in real conversations?
- [ ] **Value prop specifics** — What's a concrete outcome a user has seen? Time saved? Keywords found? Rankings improved? Even one data point.

**Still blocking some content:**
- [ ] **Docs/help site URL** — Is there a public docs or help site? Gets linked in blog CTAs.
- [ ] **Demo or sandbox URL** — Where do you send a prospect who wants to see the product before signing up?
- [ ] **Agency tier timeline** — Is multi-client management on the roadmap? Affects whether to actively target the agency persona.
- [ ] **Pricing currency** — Is USD-only intentional? No EUR/CZK pricing shown on seokrates.io as of 2026-04-11. Relevant for messaging to European buyers.

---

## How to Run the Skills

Open a terminal in this directory and run `claude` to start Claude Code. All skills load automatically.

### Recommended command reference

| Command | What it does |
|---------|--------------|
| `/messaging-positioning` | Interactive workshop — run this FIRST to validate positioning hypotheses and fill in the gaps in `messaging_positioning.md` |
| `/blog` | Generate a blog post. Will ask for type, topic, and keyword. Reads inputs-local automatically. |
| `/social-posts` | Generate LinkedIn or Twitter posts from source content. Usually run after /blog. |
| `/editorial-calendar` | Build a monthly content plan. Good to run after /messaging-positioning. |
| `/ads` | Generate Google, Meta, or LinkedIn ad copy. Run after messaging is validated. |
| `/email` | Generate email sequences. Start with a trial-to-paid nurture flow. |
| `/sales-deck` | B2B sales narrative deck. Run after testimonials and value props are confirmed. |
| `Analyze how [company] markets` | Use this to research Mangools, Collabim, or any other competitor. |
| `/image` | Generate marketing images. Requires brand_guidelines.md to be filled first. |
| `/launch-roundup` | Weekly feature announcement pipeline. Run after a product release. |

---

## Recommended First-Week Workflow

### Day 1: Run the positioning workshop
```
/messaging-positioning
```
The input files are now pre-filled with hypotheses. Use the workshop to validate them with your real knowledge of the product and customers. Budget 45 to 90 minutes. The output drives every other content asset.

### Day 2: Research competitors
```
Analyze how Mangools markets
Analyze how Collabim markets
```
Run both in parallel (open two Claude Code sessions or run sequentially). Returns channels, voice, content patterns, gaps. Feed findings into `competitor_intel.md`.

### Day 3: Send testimonial outreach
Open `testimonials.md`, find the customer contact in the Targets section, and send a brief founder email. Getting even one real quote transforms every content asset from "claim" to "proof."

### Day 4: Generate first English blog post
Target a global EN-speaking buyer — the international SEO freelancer or multi-market e-commerce operator persona.

**Option A (thought leadership):**
"Why European SEO fails — and what tools built for English get wrong about non-English markets"
- Targets: English-speaking SEO freelancers and agencies who have clients in EU markets
- High-authority angle, zero competitors have covered this in English
- Positions SEOkrates without mentioning it until late in the post

**Option B (comparison / high-intent):**
"SEOkrates vs Ahrefs: which is better for European multilingual SEO?"
- Targets: buyers actively evaluating SEO tools for non-English markets
- High conversion intent, directly captures comparison search traffic
- Use the pricing contrast (€12/month vs $99+, or €9.92/month annual vs Ahrefs Lite at $99/month) as the closing argument — and note the free 3-day trial

```
/blog
```
After the blog is generated:
```
/social-posts
```
Generate LinkedIn and Twitter variants for the blog.

### Day 5: Build the editorial calendar
```
/editorial-calendar
```
Build a 4-week EN content plan. The MKT1 workshop will ask about goals, content pillars, and capacity. Every piece should map to a persona and revenue lever (trial signups, PRO upgrades).

### Week 2 and beyond
- Run the blog + social loop at 1 to 2 EN posts per week
- Once the EN engine is running and you have 4 to 6 EN posts, replicate to the next language (suggested: Czech for organic local acquisition, or Dutch/Polish for high e-commerce density markets)
- When you have one real customer result, add it to `testimonials.md` and regenerate any blog posts that had empty proof sections

---

## File Locations

| What | Where |
|------|-------|
| SEOkrates marketing (this repo) | `d:\CLAUDE\seokrates-marketing\` |
| SEOkrates app code | `d:\CLAUDE\seokrates-web\` (do not modify from here) |
| Private inputs (gitignored) | `docs/inputs-local/` |
| Generated content | `output/` (gitignored) |
| Skills | `.claude/skills/` |
| Agents | `.claude/agents/` |

---

## Notes for Claude Code Sessions

- This repo's `claude.md` sets a senior product marketer persona with strict rules about fabrication — Claude will never invent testimonials, statistics, or competitor names not in the input files.
- The `docs/inputs-local/` folder takes precedence over `docs/inputs/` automatically (per the workflow rule in `claude.md`).
- Every generated asset lands in `output/` which is gitignored. If you want to commit a final version, move it to a versioned folder and commit manually.
- The `/autoresearch` skill can be used to autonomously improve any other skill's output quality. Worth running on /blog after the first few posts to tune for SEO performance.
