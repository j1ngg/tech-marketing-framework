# Tech Marketing Framework

A shared Claude Code and Codex project for developer tools marketing. Repeatable skills for content generation, messaging workshops, and autonomous skill optimization.

## Installation

**Prerequisites:** [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) or [OpenAI Codex CLI](https://help.openai.com/en/articles/11096431-openai-codex-ci-getting-started)

```bash
# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Or install OpenAI Codex CLI
npm install -g @openai/codex

# Clone this repo
git clone https://github.com/j1ngg/tech-marketing-framework.git
cd tech-marketing-framework

# Run Claude Code
claude

# Or run Codex
codex
```

Claude Code will automatically load `claude.md` and `.claude/`.

Codex will automatically load `AGENTS.md` and `.agents/skills/`.

## What This Is

This repo turns Claude Code and Codex into a senior product marketer for technical audiences. It provides:

- **Identity and voice guidelines** that prioritize technical accuracy over marketing fluff
- **Content guidelines** with strict standards for writing, formatting, and AI discoverability
- **Template docs** for product briefs, personas, competitive intel, and messaging
- **Skills for content generation** (email sequences, social posts, messaging workshops)
- **Autoresearch** for autonomous skill optimization via binary evals

## Structure

```
├── AGENTS.md                        # Codex repo instructions
├── claude.md                        # Claude Code instructions
├── .agents/
│   └── skills/                      # Codex skill wrappers
├── .claude/
│   ├── rules/
│   │   └── content-guidelines.md    # Writing standards
│   ├── skills/
│   │   ├── messaging-positioning/   # Interactive workshop skill
│   │   ├── social-posts/            # Social media post generator
│   │   ├── skill-builder/           # Meta-skill for creating new skills/agents
│   │   ├── email/                   # Event follow-up email sequences
│   │   ├── ads/                     # Paid ad copy generator
│   │   ├── sales-deck/              # B2B sales narrative deck builder
│   │   ├── one-pager/               # Product one-pager for sales enablement
│   │   ├── blog/                    # SEO/AEO optimized blog post generator
│   │   ├── editorial-calendar/      # Monthly rolling editorial calendar (MKT1)
│   │   ├── image/                   # Marketing image generator (MCP)
│   │   ├── launch-roundup/          # Weekly feature announcement pipeline
│   │   ├── producthunt-launch/      # Product Hunt listing assets + dated launch plan
│   │   └── autoresearch/            # Skill optimization via autonomous evals
│   └── agents/
│       ├── asset-reviewer.md        # Reviews assets against guidelines
│       ├── ads-auditor.md           # Audits ad performance with health scoring
│       └── how-they-market.md       # Analyzes how others market
├── docs/
│   ├── inputs/                      # Product-specific data (fill these in)
│   │   ├── product_brief.md
│   │   ├── target_personas.md
│   │   ├── messaging_positioning.md
│   │   ├── competitor_intel.md
│   │   ├── testimonials.md
│   │   └── brand_guidelines.md
│   └── reference/                   # Reusable frameworks
│       └── channel_directory.md
└── output/                          # Generated assets by type
    ├── social/
    ├── blog/
    ├── email/
    ├── ads/
    ├── decks/
    ├── images/
    └── research/
```

## Usage

1. Clone this repo into your project or use it as a standalone workspace
2. Fill in the `/docs/inputs/` templates with your product details
3. Run Claude Code or Codex in this directory

Tool syntax:

- In Claude Code, use slash commands such as `/social-posts`
- In Codex, invoke the same workflow by skill name, for example `$social-posts`, or ask for it directly in plain English

Both tools follow the same underlying workflow definitions.

The examples below use Claude Code slash syntax. In Codex, use the same skill name with `$`, for example `$social-posts`, or describe the workflow in plain English.

### Running the Messaging Workshop

Use the `/messaging-positioning` skill to run a structured workshop:

```
/messaging-positioning
```

This walks through four discovery sections (vision, product, competitive, targeting) and builds your `messaging_positioning.md` doc in real time.

### Generating Social Posts

Use the `/social-posts` skill to generate social media content from source material:

```
/social-posts
```

The skill will ask you to select platform (LinkedIn/Twitter) and account type (brand/personal), then generate posts tailored to each channel's audience.

### Generating Email Sequences

Use the `/email` skill to generate email sequences:

```
/email
```

Currently supports **event follow-up sequences** (post-conference, post-meeting, post-dinner). The skill generates a 4-email sequence optimized for programmatic outreach:

| Email | Timing | Purpose |
|-------|--------|---------|
| 1 | Day 0 | Event recall + pain points (no link) |
| 2 | +2 days | Peer social proof + product demo |
| 3 | +6 days | Customer results + resource link |
| 4 | +11 days | Soft close + problem list (no link) |

Key features:
- Reads product info from `docs/inputs/` automatically
- Enforces real links only (no placeholders)
- Uses approved customers only (no fabrications)
- Programmatic personalization (shared context, not fake 1:1 details)

Customer and prospect email types coming soon.

### Generating Paid Ads

Use the `/ads` skill to generate paid ad copy for Google, Meta, and LinkedIn:

```
/ads
```

The skill uses a creative matrix approach (Topics x Personas x Angles) to generate targeted variants:

| Dimension | Source |
|-----------|--------|
| Topics | Pain points from `messaging_positioning.md` |
| Personas | Audience segments from `target_personas.md` |
| Angles | Problem-agitation, social proof, how-to, comparison |

Key features:
- Reads all `docs/inputs/` files automatically for context
- Can incorporate fresh competitive research from `how-they-market` runs
- Platform-specific specs (character limits, image sizes, rules)
- Generates 3 to 5 variants per platform (quality over quantity)
- Outputs headlines, descriptions, and image/creative briefs

Supported platforms:
- Google Ads (Search, Display)
- Meta (Facebook, Instagram)
- LinkedIn

### Creating Sales Decks

Use the `/sales-deck` skill to create B2B sales narrative decks:

```
/sales-deck
```

The skill uses April Dunford's 8-step sales pitch methodology, structured in two phases:

| Phase | Slides | Purpose |
|-------|--------|---------|
| **The Setup** | 1 to 10 | Establish market context and purchase criteria. Product is NOT mentioned. |
| **The Follow-Through** | 11 to 17 | Introduce product mapped directly to the criteria from the Setup. |

This structure combats "no decision" paralysis by giving buyers a clear evaluation framework before asking them to consider your solution.

**Slide structure:**

| Slide | Name | Content |
|-------|------|---------|
| 1 | Title/Thesis | Bold provocative insight (no product name) |
| 2 | TLDR | Executive summary of the argument arc |
| 3 to 4 | Status Quo | Why the current approach was rational |
| 5 to 6 | Disruption | What changed to break the status quo |
| 7 to 8 | Alternatives | Why other options fall short |
| 9 to 10 | Perfect World | The new purchase criteria |
| 11 | Introduction | Product positioning and context |
| 12 to 14 | Differentiated Value | Capabilities mapped to Perfect World criteria |
| 15 | Proof | Customer results from approved testimonials |
| 16 | Objections | (Optional) Address common concerns |
| 17 | The Ask | Recap and clear call to action |

**Key features:**
- Reads all `docs/inputs/` files automatically for product context
- Enforces "no product in Setup" rule
- Maps proof points to differentiated value claims
- Outputs Markdown outline plus PPTX generation via Python script
- Includes self-review checklist for Dunford framework compliance

**Output:**
- Markdown outline: `output/decks/[product-name]-sales-deck.md`
- PPTX file: `output/decks/[product-name]-sales-deck.pptx`

### Generating Product One-Pagers

Use the `/one-pager` skill to generate product one-pagers for sales enablement:

```
/one-pager
```

The skill generates a scannable, single-page document that works across sales contexts:

| Use Case | What changes |
|----------|-------------|
| **Leave-behind** | Post-meeting recap that keeps momentum |
| **Champion enablement** | Arms your internal champion to sell for you |
| **Event handout** | Quick intro that drives follow-up conversations |
| **Top-of-funnel download** | Introduces the product to people who haven't talked to sales |

**Layout structure:**

| Section | Content |
|---------|---------|
| Hero banner | Product name, tagline, subtitle, CTA |
| Problem + Solution (left) | Pain statement, solution mechanism, key differentiators |
| Key Outcomes (right) | Four outcome blocks with bold headlines |
| Architecture | Simplified diagram of how the product works |
| Customer proof (optional) | Logo strip and strongest matching quote from testimonials |
| Footer | URL, pricing hook, compliance badges, contact |

**Key features:**
- Reads all `docs/inputs/` files automatically for product context
- Customer proof included by default, skippable per generation
- Enforces the competitor test: every sentence must be specific enough that a competitor could not paste it unchanged
- Supports persona-specific, event-specific, deal-specific, and use-case-specific variations without changing layout
- Two-phase output: markdown draft for review, then styled HTML/CSS for PDF export

**Output:**
- Markdown draft: `output/one-pagers/[product-name]-one-pager.md`
- HTML/PDF: `output/one-pagers/[product-name]-one-pager.html`

### Writing Blog Posts

Use the `/blog` skill to generate SEO and AEO optimized blog posts with optional tri-publish variants for LinkedIn Pulse and X:

```
/blog
```

The skill supports five blog types, each with its own structure and word count:

| Type | Best For | Length |
|------|----------|--------|
| Feature announcement | Release notes, new capability | 800 to 1,200 words |
| Product launch | New product, major release | 1,200 to 1,800 words |
| Thought leadership | Opinion piece, contrarian take | 1,500 to 2,500 words |
| Cookbook/tutorial | How-to guide, integration walkthrough | 1,500 to 3,000 words |
| Report conversion | Whitepaper or case study → blog | 1,000 to 1,500 words |

**Source content formats supported:**
- Markdown files
- PDFs (reports, case studies)
- URLs (fetches and processes)
- Raw pasted text

**Every blog includes:**
- TLDR section (top of post, LLM-extractable)
- Metadescription (under 160 chars)
- FAQ section (3 to 5 questions, AEO optimized)
- Schema markup suggestions (Article, HowTo, FAQPage)
- Internal linking recommendations (fetches from your domain)
- Visual callout flags (`[VISUAL: description]`)

**Authority Content gate:**

Before generating, the skill checks that the source content meets the Authority Content bar: an original framework, a contrarian take backed by data, a firsthand breakdown, or a case study with specific numbers. Generic listicles and summarized content get flagged with a request for the real angle.

**Tri-publish strategy:**

The skill asks which surfaces you're publishing to and generates platform-specific variants:

| Surface | What it optimizes for |
|---------|----------------------|
| Website/blog | Long-tail keywords, schema markup, internal linking |
| LinkedIn Pulse | Google indexing via DR 98 domain, LLM citations, custom SEO title and meta description, comment-driving CTA |
| X article | Algorithmic For You feed, dwell time, quote repost prompt for viral distribution |

LinkedIn Pulse articles are the second most-cited domain in AI-generated responses, with citation rates up 4 to 5x year over year. X articles benefit from the For You feed pushing content to non-followers — 30 to 40% of views come from accounts that don't follow you.

**Key features:**
- WebSearch for supporting evidence and current statistics
- Fetches pages from your domain for contextual internal links
- Code snippets always include comments
- Follows 2026 SEO/AEO best practices (archetypal phrasing, answer-first structure)
- Hands off to `/social-posts` skill for short-form promotion

### Building an Editorial Calendar

Use the `/editorial-calendar` skill to build a monthly rolling content plan:

```
/editorial-calendar
```

The skill runs an interactive workshop based on Emily Kramer's MKT1 methodology, walking through five discovery sections:

| Section | What it covers |
|---------|----------------|
| 1. Business Context | Goals, revenue levers, GTM motion |
| 2. Perceptions | What you want your audience to say about you (3 to 5 statements) |
| 3. Content Pillars & Audience | Topic areas, audience segments, channels, formats |
| 4. Capacity | Team size, cadence, what's working, repurposable backlog |
| 5. Product & Market Context | Upcoming launches, events, competitive moves |

**Output:** Three artifacts designed for monthly use:

| Artifact | What it contains |
|----------|-----------------|
| 3-Month Theme Roadmap | Monthly themes mapped to revenue levers and Perceptions |
| 4-Week Editorial Calendar | Specific pieces with title, type, pillar, channel, owner, distribution |
| Repurposing Matrix | Derivative content from each anchor piece |

**Key features:**
- Every piece maps to a Perception and revenue lever (no random acts of marketing)
- 70/30 split enforced (educational/problem content vs. product content)
- 15 to 20% capacity reserved for reactive content
- Pre-post opportunities identified for anchor content
- Hands off to `/blog`, `/social-posts`, `/email`, or `/launch-roundup` for execution
- Re-run monthly with "refresh" to roll the plan forward without re-answering all questions

### Weekly Launch Roundup

Use the `/launch-roundup` skill to generate a complete feature announcement package from recent MRs:

```
/launch-roundup
```

The skill runs a five step pipeline:

| Step | Output | Mode |
|------|--------|------|
| 1 | Feature summary from MRs | Automatic |
| 2 | Slack announcement | **Approval gate** (review with PM/EM) |
| 3 | Feature announcement blog | Autonomous |
| 4 | LinkedIn posts (brand + personal) | Autonomous |
| 5 | LinkedIn carousel (PPTX) | Autonomous |

After you provide the MR source and approve the Slack copy, steps 3 through 5 run without interruption. All outputs land in `output/launch-roundups/{product-name}-{date}/`.

**Key features:**
- Single approval gate after Slack copy (your PM/EM sanity check)
- Blog follows full `/blog` skill rules (SEO, AEO, FAQ, schema markup)
- LinkedIn posts follow full `/social-posts` skill rules (brand + personal)
- Carousel generates a PPTX via `python-pptx`, styled from brand guidelines
- Adapts structure based on feature count (1 feature vs 5+ features)

### Planning a Product Hunt Launch

Use the `/producthunt-launch` skill to produce a complete Product Hunt launch package for a developer tool:

```
/producthunt-launch
```

The skill folds listing copy and launch planning into one workflow. It asks scope (listing only, plan only, or full package), gathers launch parameters, then generates:

| Output | Contents |
|--------|----------|
| Listing assets | 3 tagline options (under 60 chars, stranger tested), description, maker's first comment (under 800 chars), gallery + video spec, social proof hooks |
| Launch plan | Dated 6 week timeline (Foundation → Outreach → Final Prep → Final 5 Days), launch day runsheet (12:01 AM to 11:59 PM PT), team roles, post launch 30 day plan, asset inventory, success metrics |

Key rules baked in:

- Tagline rules: feature first, "[Product] for [category]" or "open source [known brand] alternative" formulas, no buzzwords
- Maker comment is weighted heavily by PH algorithm (one quality comment ~ 40 to 50 upvotes)
- Aged PH accounts (6+ months) carry roughly 10x vote weight
- Top 500 hunters drive ~3.2x more upvotes (require 6 weeks outreach lead time)
- Tuesdays and Wednesdays in week 2 or 3 of the month maximize the monthly badge
- Testimonials are mandatory — gap flagged if missing

Outputs land in `output/launches/{product-name}-{YYYY-MM-DD}/` as `listing.md` and/or `launch-plan.md`. Hands off to `/social-posts` for launch day posts and `asset-reviewer` for listing QA.

### Generating Marketing Images

Use the `/image` skill to generate images for any marketing asset:

```
/image
```

The skill uses the `mcp-image` MCP server to generate visuals for social posts, blog headers, ads, and presentations. It reads `docs/inputs/brand_guidelines.md` for style consistency and constructs optimized prompts based on your content.

| Use Case | Aspect Ratio | Resolution |
|----------|-------------|------------|
| LinkedIn / Twitter post | 16:9 | 2K |
| Blog featured image | 16:9 | 2K |
| LinkedIn ad | 1:1 | 2K |
| Meta ad | 4:5 | 2K |
| Presentation slide | 16:9 | 2K |

Key features:
- Reads brand guidelines automatically for visual consistency
- Supports reference images for style matching
- Prompt construction in three layers: style, concept, restrictions
- Iterative refinement loop (up to 5 rounds)
- Generates alt text for SEO
- Works alongside other skills (`/social-posts`, `/blog`, `/ads`) to create visuals for generated content

Output: `output/images/`

### Building New Skills or Agents

Use the `/skill-builder` skill to design and create new skills or agents:

```
/skill-builder
```

This walks you through:
1. Deciding whether you need a skill or agent (with guidance if you pick the wrong one)
2. The four core questions: outcome, inputs, actions, rules
3. Design formula: Role + Goal + Tools + Rules + Output Format
4. Generating a complete SKILL.md or agent .md file
5. Test cases to validate your design

The skill prevents over-engineering by pushing back on vague outcomes, tool overload, and premature complexity.

### Optimizing Skills with Autoresearch

Use the `/autoresearch` skill to autonomously improve any existing skill:

```
/autoresearch
```

Based on Andrej Karpathy's autoresearch methodology, this skill:
1. Takes any existing skill and defines binary pass/fail evals
2. Runs the skill repeatedly against test inputs
3. Scores outputs, identifies failure patterns
4. Mutates the skill prompt one change at a time
5. Keeps improvements, discards regressions
6. Produces an improved SKILL.md, results log, and changelog

The skill runs autonomously until stopped or until it hits 95%+ pass rate for 3 consecutive experiments.

### Researching How Others Market

Use the `how-they-market` workflow to analyze how a person, company, or newsletter markets themselves:

```
Analyze how [company/person/newsletter] markets
```

In Claude Code this is exposed as an agent. In Codex it is exposed as a skill wrapper over the same canonical instructions.

The workflow runs parallel web searches across HN, Reddit, LinkedIn, and Twitter, then visits the target's website to extract positioning.

| Section | What it covers |
|---------|----------------|
| Channels | Where they publish (Twitter, LinkedIn, blog, newsletter, YouTube, podcast) |
| Voice & Tone | How they sound, technical depth, formatting patterns |
| Content Patterns | Posting cadence, content mix, hooks, what's working |
| Community Presence | HN and Reddit sentiment and discussions |
| Notable Tactics | 2 to 4 specific tactics worth learning from |
| Gaps & Limitations | What couldn't be researched |
| Follow-Up Research | Suggested next steps, related accounts to investigate |

Optional: Specify a focus area like "just their Twitter," "how they launch products," or "their newsletter strategy."

**Integration with `/ads`:** Research output informs competitive ad angles. Use findings to identify messaging gaps, positioning angles competitors miss, and channel priorities.

### Auditing Ad Performance

Use the `ads-auditor` workflow to analyze campaign performance and get optimization recommendations:

```
Audit my Google Ads performance: [paste metrics or provide file path]
```

In Claude Code this is exposed as an agent. In Codex it is exposed as a skill wrapper over the same canonical instructions.

The workflow analyzes your data against benchmarks and produces:

| Section | What it covers |
|---------|----------------|
| Health Score | 0 to 100 score with letter grade (A through F) |
| Critical Issues | Problems requiring immediate action |
| Optimization Opportunities | Improvements ranked by potential impact |
| What's Working | Keep doing these things |
| Recommended Actions | Prioritized fixes with effort estimates |
| Platform Checklist | Pass/fail on platform best practices |

Supported platforms: Google Ads, Meta (Facebook/Instagram), LinkedIn

**Critical thresholds auto-flagged:**
- CPA exceeding 3x target
- CTR below 50% of benchmark
- Frequency > 2.5 (Meta audience fatigue)
- Learning phase resets

## Philosophy

- Write like an engineer explaining to another engineer
- Teach, do not sell
- Transparency is a competitive advantage
- Personality is a moat
- Replace adjectives with evidence

See `claude.md` for the Claude Code entrypoint, `AGENTS.md` for the Codex entrypoint, and `.claude/rules/content-guidelines.md` for the shared writing standards.

## Landing Page

The landing page at [j1ngg.github.io/tech-marketing-framework](https://j1ngg.github.io/tech-marketing-framework) is built with Astro and deployed automatically via GitHub Pages on push to main.

```bash
cd site
npm install
npm run dev     # Local dev server
npm run build   # Production build
```

## License

MIT
