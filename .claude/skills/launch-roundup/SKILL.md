---
name: launch-roundup
description: "Weekly feature launch announcement pipeline. Reads recent MRs, generates Slack announcement (with approval gate), then autonomously produces a blog post, LinkedIn posts (brand + personal), and a LinkedIn carousel. Use when: weekly roundup, feature launch announcement, what's new, launch pipeline, weekly announcement."
autoload: false
---

# Launch Roundup

A weekly pipeline that turns recent merge requests into a complete announcement package: Slack copy, blog post, LinkedIn posts, and a LinkedIn carousel. One approval gate after Slack copy. Everything else runs autonomously.

## Pipeline Overview

| Step | Output | Mode |
|------|--------|------|
| 1. Gather MRs | Summarized feature list | Automatic |
| 2. Slack announcement | Slack message copy | **Approval gate** |
| 3. Blog post | Feature announcement blog | Autonomous |
| 4. LinkedIn posts | Brand + personal posts | Autonomous |
| 5. LinkedIn carousel | PPTX carousel slides | Autonomous |

All outputs land in `output/launch-roundups/{product-name}-{YYYY-MM-DD}/`.

---

## Step 1: Gather MR Source Material

Ask the user TWO questions:

> 1. **Repo path** — Absolute path to the local git repo (e.g., `~/repos/ai-agent`)
> 2. **Time window** — How far back? (default: 7 days)

Wait for the user to answer before proceeding. If they only provide the path, use 7 days.

**Fallback:** If the user doesn't have a local repo, they can also provide:
- A file path (Markdown, text, or PDF with MR summaries)
- A pasted list of recent MRs
- A URL to fetch (changelog page, release notes)

### Reading MRs from a local repo

Run this git command against the provided repo path to extract merged MRs:

```bash
git -C {repo_path} log --merges --since="{N} days ago" --format="commit:%H%nauthor:%an%ndate:%ad%nsubject:%s%n%b%n---" --date=short
```

If the repo uses squash merges (no merge commits), fall back to:

```bash
git -C {repo_path} log --since="{N} days ago" --format="commit:%H%nauthor:%an%ndate:%ad%nsubject:%s%n%b%n---" --date=short --first-parent
```

If neither produces results, try without `--first-parent` and deduplicate by subject line.

For each commit/MR, also read the full diff summary to understand what changed:

```bash
git -C {repo_path} show --stat --format="" {commit_hash}
```

**Enrich thin commit messages:** If a commit subject is vague (e.g., "fix bug", "update"), read the diff stat and the changed files to infer what the feature does. Group related commits under a single feature when they clearly belong together (e.g., multiple commits touching the same module in the same day).

### Extracting features from git history

From the git output, extract:

| Field | Where it comes from |
|-------|---------------------|
| Feature names | Commit subjects, MR titles, or inferred from changed files |
| What it does | Commit body, diff stat, or inferred from the code changes |
| Who it helps | Cross-reference with `target_personas.md` based on the feature area |
| Technical detail | Diff stat, changed files, commit body |

**Filtering rules:**
- Include: new features, significant enhancements, user-facing changes, new integrations
- Exclude: dependency bumps, CI/CD changes, typo fixes, internal refactors with no user impact, test-only changes
- When in doubt, include it in the summary table and let the user cut it during the sanity check

Then read these files for product context:

| File | What to extract |
|------|-----------------|
| `docs/inputs/product_brief.md` | Product name, positioning, capabilities (for accuracy) |
| `docs/inputs/messaging_positioning.md` | Value props, pain points, competitive differentiation |
| `docs/inputs/target_personas.md` | Audience context, job titles, technical level |
| `docs/inputs/brand_guidelines.md` | Visual style for carousel generation |

**Private data override:** If `docs/inputs-local/` exists, read from there instead of `docs/inputs/`.

Compile a feature summary table:

```
| Feature | What it does | Who it helps | Technical detail |
|---------|-------------|--------------|------------------|
| [name]  | [summary]   | [persona]    | [detail]         |
```

Present this table to the user for a quick sanity check. If they correct anything, update before proceeding.

---

## Step 2: Generate Slack Announcement

Generate a Slack announcement using these rules:

**Format:**
- Start with a one line bold header: `*What's New in [Product]: [Date Range]*`
- One blank line, then a brief (2 to 3 sentence) narrative intro summarizing the theme of this batch
- Then one section per feature, each structured as:
  - Bold feature name on its own line
  - 2 to 3 sentences: what it does, why it matters, who benefits
  - If applicable, one concrete example or config snippet in a code block
- End with a single line linking to the blog (placeholder: `[blog link]`) and a note like "Full writeup on the blog."

**Voice:**
- Internal, conversational, engineer to engineer
- Skip marketing speak entirely. This is for your PM and EM.
- Be specific about what shipped, not why it's exciting
- Use Slack formatting: `*bold*`, `_italic_`, `` `code` ``, code blocks with triple backticks

**Length:** 200 to 400 words total. Enough to be useful in a Slack channel, short enough to read without expanding.

**Output:** Save to `output/launch-roundups/{product-name}-{YYYY-MM-DD}/slack-announcement.md`

---

## APPROVAL GATE

After generating the Slack copy, present it to the user and say:

> "Here's the Slack announcement. Review this with your PM and EM. Once approved, reply and I'll generate the blog, LinkedIn posts, and carousel automatically."

**Do not proceed until the user explicitly approves.** If they request changes, revise and present again. The approved Slack copy becomes the source of truth for all downstream assets.

---

## Step 3: Generate Blog Post (Autonomous)

Once approved, generate a feature announcement blog post. Do not ask any questions. Use these pre-filled inputs:

| Input | Value |
|-------|-------|
| Blog type | Feature announcement |
| Source content | The approved Slack announcement + the original MR summaries |
| Target keyword | Derive from the product name + primary feature theme |
| Distribution surfaces | Website + LinkedIn Pulse (tri-publish if the user's messaging_positioning.md mentions LinkedIn as a channel, otherwise website only) |
| Disclosure | None (this is brand content, not personal) |
| Internal link domain | Extract from `product_brief.md` or `messaging_positioning.md` if a domain is mentioned. If not found, skip internal linking. |

**Follow the full blog skill structure for Feature Announcement type:**

```
# [Feature Name or Theme]: [Benefit Statement]

TLDR (2 to 3 sentences)

## The Problem
## Introducing [Feature/Theme]
## How It Works (with code snippets if applicable)
## Use Cases (2 to 3, each highlighting a DIFFERENT capability)
## Getting Started
## FAQ (3 to 5 questions)

CTA + Post-Publication Checklist
```

**Apply all blog skill rules:** Authority Content bar, SEO/AEO requirements (metadescription, TLDR, FAQ, schema markup, internal linking), writing rules (no passive voice, no banned words, max 3 dashes, Oxford comma), visual callout flags.

**If multiple features shipped:** Frame the blog as a "What's New" roundup rather than a single feature deep-dive. Use H2s for each major feature and H3s for sub-features.

**Output:** Save to `output/launch-roundups/{product-name}-{YYYY-MM-DD}/blog-post.md`

---

## Step 4: Generate LinkedIn Posts (Autonomous)

Generate LinkedIn posts using the approved Slack copy and the blog post as source material. Do not ask any questions. Use these pre-filled inputs:

| Input | Value |
|-------|-------|
| Platform | LinkedIn |
| Account types | Both (brand + personal) |
| Brand/company name | From `product_brief.md` |
| Key link | `[blog link]` (placeholder for the blog URL) |
| Author context (personal) | Extract from `messaging_positioning.md` if an author or spokesperson is mentioned. If not, use: "a member of the [Product] team" |

**Follow the full social-posts skill rules for LinkedIn:**

**Brand LinkedIn:**
- Lead with the problem or market insight, not the product
- Focus on business impact and governance implications
- Structure: Problem, Impact, Solution exists, Link
- 150 to 250 words
- No hashtags in body, no emojis, no subject line

**Personal LinkedIn:**
- Lead with personal experience ("We shipped", "I built", "I learned")
- Include narrative arc: problem, action, insight
- Disclose affiliation
- 200 to 350 words
- No hashtags, no emojis

**Output:** Save to `output/launch-roundups/{product-name}-{YYYY-MM-DD}/linkedin-posts.md`

---

## Step 5: Generate LinkedIn Carousel (Autonomous)

Generate a LinkedIn carousel using the blog post as source material. Do not ask any questions.

**Carousel structure:**

| Slide | Content |
|-------|---------|
| 1. Cover | "WHAT'S NEW" + Product name + Date range + "Swipe for details" |
| 2 to N. Feature slides | One slide per major feature. Bold feature name, 2 to 3 sentence description, visual element (before/after card, screenshot placeholder, or diagram placeholder) |
| Final. CTA | Summary statement + product URL + CTA button |

**Visual style:**
- Read `docs/inputs/brand_guidelines.md` for colors, fonts, and motifs
- If brand guidelines are sparse, default to: dark background (#1A1A1E), monospace font, orange accent color (#D48A29), white text
- Each feature slide gets an orange accent bar at top
- Use card components for before/after comparisons
- Flag screenshot placeholders: `[Replace with {feature} screenshot]`

**Build method:**
- Generate a Python script (`build_carousel.py`) using `python-pptx` that creates the PPTX
- Slides are 1080x1080px (10.8in square at 100dpi), optimized for LinkedIn carousel
- Run the script to produce the PPTX file
- If `python-pptx` is not available or the script fails, output the carousel as a detailed Markdown specification that can be built manually

**Output:** Save all carousel files to `output/launch-roundups/{product-name}-{YYYY-MM-DD}/carousel/`:
- `build_carousel.py`
- `{product-name}-whats-new-carousel.pptx`

---

## Final Output Summary

After all steps complete, present the user with a summary:

```
## Launch Roundup Complete

**Date:** {YYYY-MM-DD}
**Features covered:** {count}

### Outputs

| Asset | Path | Status |
|-------|------|--------|
| Slack announcement | output/launch-roundups/{name}/slack-announcement.md | Ready to post |
| Blog post | output/launch-roundups/{name}/blog-post.md | Ready for review |
| LinkedIn (brand) | output/launch-roundups/{name}/linkedin-posts.md | Ready to post |
| LinkedIn (personal) | output/launch-roundups/{name}/linkedin-posts.md | Ready to post |
| LinkedIn carousel | output/launch-roundups/{name}/carousel/ | Ready (replace screenshot placeholders) |

### Next steps
- Post the Slack announcement to your channel
- Publish the blog and update the [blog link] placeholders in the LinkedIn posts
- Upload the carousel PPTX to LinkedIn or import into Canva for final polish
- Replace screenshot placeholders in the carousel with actual product screenshots
```

---

## Adaptation Notes

**When only 1 feature shipped:**
- Skip the "What's New roundup" framing
- Blog becomes a single feature announcement
- Carousel becomes 3 slides: cover, feature detail, CTA

**When 5+ features shipped:**
- Group related features under themes for the blog (e.g., "Governance" theme, "Detection" theme)
- Carousel covers top 3 to 4 features max (pick the ones with the most user impact)
- Mention remaining features in the blog but not the carousel

**When MR descriptions are thin:**
- Flag gaps: "The MR for [feature] doesn't have enough detail to write a compelling description. Can you add 1 to 2 sentences about what it does and why?"
- Do not fabricate technical details

**When product_brief.md is empty:**
- Ask the user for: product name, 2 to 3 key capabilities, target audience
- Flag: "Running without full product context. Claims will be generic."

**When brand_guidelines.md is sparse:**
- Use defaults for carousel (dark bg, orange accent, monospace)
- Note in summary: "Carousel uses default styling. Update brand_guidelines.md for branded visuals."
