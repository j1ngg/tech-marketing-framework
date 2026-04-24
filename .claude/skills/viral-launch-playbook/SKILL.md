---
name: viral-launch-playbook
description: "6-step framework for engineering viral product launches on X. Covers emotional positioning, copy scoring, algorithmic gamification, and 48-hour engagement strategy. Use when: prepare for a launch, launch playbook, viral marketing campaign, launch on X, product launch strategy, write launch copy."
autoload: false
---

# Viral Launch Playbook

A complete 6-step framework for engineering viral product launches on X. Works in Claude Code, Codex, or any AI agent that can read this file as a system prompt or knowledge base.

## When to Use This

Use when a user wants to launch a product on X, create a viral marketing campaign, position a new startup, write high converting launch copy, or plan a 48-hour post-launch engagement strategy.

## Core Philosophy

The success of a launch on X is not based on luck or generic engagement. It relies on two fundamental pillars:

1. **Visceral Positioning**: Users do not care about features. They care about the emotional outcome and how their life changes after using the product.
2. **Algorithmic Gamification**: The X algorithm measures Sourcing (retweets) to determine if a post enters the feed, and Ranking (reply chains) to determine how high it appears.

---

## Step 0: Gather Inputs

Before starting, read the following files if they exist:

| File | What to extract |
|------|-----------------|
| `docs/inputs/product_brief.md` | Product name, one-line description, problem statement, key capabilities |
| `docs/inputs/messaging_positioning.md` | Value props, competitive differentiation, pain points |
| `docs/inputs/target_personas.md` | Audience context, job titles, technical level |

**Private data override:** If `docs/inputs-local/` exists, read from there instead of `docs/inputs/`.

Then ask the user the following questions. Wait for all answers before proceeding.

1. **Product** — What is the product name and what does it do? (Skip if `product_brief.md` is populated.)
2. **Launch date** — When is the launch? Exact date if known.
3. **Starting point** — Do you have an existing script or copy to work from, or are we starting from scratch?
4. **X API access** — Do you have X API access for competitor research in Step 3? (Answer yes or no. If no, Step 3 runs in reduced mode with manual search guidance.)
5. **Influencer network** — Do you have an influencer network to deploy in Phase 2 of the launch timeline?

---

## Step 1: Identify the Hidden Outcome

The goal is to move away from pitching features and instead identify the emotional outcome that users truly care about. You must find the answer to: "What does a user's life look like after using your product?"

### Process

1. Write down every feature the product has.
2. For each feature, ask "so what?" out loud.
3. Keep asking "so what?" recursively until you hit a core emotion.
4. That emotion is your positioning.
5. Write one sentence describing their life after using it. That sentence is your hook.

### Prompt

```text
"Here is a list of features for [product]. For each one, ask 'so what?' recursively until you reach an emotional outcome. Return the single strongest emotional positioning statement."
```

### Examples

| Weak | Strong |
|------|--------|
| AI website builder that works in seconds | Replace your 9 to 5 income |

---

## Step 2: Engineer the Script (Weapons Check)

Every video script or piece of launch copy must be rigorously scored and optimized. Lines that do not pass must be rewritten automatically. Lines that are pure filler must be cut entirely.

### Scoring Dimensions

Every single line must be scored independently on a 1 to 10 scale for two dimensions:

| Dimension | Question It Answers |
|-----------|---------------------|
| **Invention Novelty** | Does this feel like something nobody has ever said? Does it make the product feel like a genuine breakthrough? |
| **Copy Intensity** | Does reading it make you feel something, not just understand something? |

Both scores must hit 10 out of 10. A novel idea with flat copy fails. Sharp copy about a boring feature fails.

### Prompt

```text
"Score this line on two dimensions: Invention Novelty (does it make the product feel like a genuine breakthrough?) and Copy Intensity (does it make someone feel something, not just understand something?). Both on a 1 to 10 scale. If either is below 10, rewrite it and explain what was weak."
```

### Rewrite Principles

The transformation from weak to strong is always the same: replace vague with visceral, features with feelings, announcements with punches.

| Weak | Strong |
|------|--------|
| Introducing our new AI platform | We built the world's first AI that makes your competitors obsolete overnight |
| Our tool helps you grow faster | The exact system that took 4 startups from zero to 1M+ views |
| Better customer support | Real engineers on call 24/7. Tickets stay open until you say you're unblocked. |

---

## Step 3: Make Haters Do Your Distribution

Instead of ignoring hate or launching with standard product marketing language, own the criticism before the critics can use it.

### Strategy

1. Find the most common criticism of your category.
2. Acknowledge it directly in your positioning.
3. Make your product the solution to that exact criticism.
4. Plant one line that a specific community cannot help but react to.
5. Watch them distribute your content while complaining about it.

Every quote tweet is a signal to X to show your post to more users. Haters will quote tweet something that makes them defensive, and that engagement feeds the algorithm.

### Prompt

This step requires X API access. **If the user skipped X API access in Step 0, use the reduced mode below.**

**Full mode (X API access):**

```text
"Research the top posts on X in [category] sorted by engagement using advanced search Min_Faves:1000. Identify the ones with the highest quote tweet ratio. What is the core criticism or controversy that made people react? Summarize the single most activating nerve in this community."
```

**Reduced mode (no X API access):**

Ask the user to manually search X for the top 5 to 10 posts in their category with at least 1,000 likes and share the URLs or paste the text. Then apply the same analysis. Note to the user: reduced mode produces the same output but requires manual input. Full mode is faster and surfaces patterns you would not think to look for.

### Example

| Context | Standard Approach | Viral Approach |
|---------|-------------------|----------------|
| Launching an AI design tool to designers who despise AI design tools | "AI for design" | "The world's first design agent with taste. Anti slop. By design." |

---

## Step 4: Match the Messaging to Proven Formats

Before writing a single word, find proven viral concepts and borrow that framing to let your product speak through it.

### Process

1. Ask: What does this product actually help you do?
2. Ask: Is there a proven viral concept built on that same idea?
3. Ask: Can you borrow that concept and let the product speak through it?

A research agent must run keyword searches across YouTube filtered three ways: all time, last 12 months, and last 30 days. For each keyword, find the highest performing video. That is the ceiling. Then collect patterns downward until there is a massive drop off in views. The titles at the ceiling are the patterns worth stealing.

### Prompt

Requires YouTube API access or a tool like 1of10.com:

```text
"Find the top performing videos in [category] across the last 30 days, 12 months, and all time. Identify the structural pattern behind the highest performing titles. What is the core concept or framing that made them work? Now apply that same framing to [product]."
```

---

## Step 5: Create Algorithmic Signals

The X algorithm does not measure general engagement. It measures two separate signals:

| Signal | What It Controls | Primary Driver |
|--------|-----------------|----------------|
| **Sourcing** | Will your post be shown at all? | Retweets. No retweets means the post never enters the For You feed. |
| **Ranking** | How high will your post appear? | Reply chains where the original author responds back. |

Every reply you post creates a new chain. Every chain tells the algorithm this is a real conversation worth showing to others. More chains equal higher ranking. Higher ranking equals more people seeing it. More people seeing it equals more replies.

### Reply Generation Prompt

Draft replies in real time during the 48-hour window so the founder never goes silent:

```text
"I am working on a launch [Insert video script, all of my knowledge base about them]. Write 25 potential replies to people who are replying to me about the launch to keep the conversation going, add value, feel like a real human responding to it, and keep each under 280 characters, preferably less than that."
```

---

## Step 6: Execute the Strategic Timeline

You will know whether your post lives or dies in the first 3 hours. Do not blast every connection at once. If the algorithm sees a sudden artificial spike with no organic foundation, it reads it as inauthentic and the post dies within an hour.

### The 48-Hour Schedule

**Phase 1 (Minutes 0 to 60)**

Let the post breathe. Organic followers only. The algorithm tests with your core audience first. Reply to every single question thoughtfully. Monitor engagement velocity.

**Phase 2 (Hours 1 to 2)**

Deploy 10 to 20 influencers ONLY if organic velocity is strong. Stagger influencer posts across 30-minute windows. Mandatory requirement: every influencer must disclose they are paid.

If the user has no influencer network (captured in Step 0), skip Phase 2 and note this in the timeline output. Flag it as a gap to address before future launches.

**Phase 3 (Real Time Adjustment)**

Watch engagement live. Add gas when momentum is building.

**Phase 4 (Next 24 to 48 Hours)**

Continue replying to every comment for 48 hours. Never stop. Not for meetings. Not for sleep. Not for anything.

### Follow Up Content Calendar

| Day | Content |
|-----|---------|
| Day 2 | Meme your product |
| Day 3 | Deep dive on one specific feature |
| Day 4 | Tell your company story |
| Week 2 | Speak to results and show off testimonials |

---

## Output Format

All outputs land in `output/viral-launch/{product-name}-{YYYY-MM-DD}/`.

| File | Contents |
|------|----------|
| `01-positioning-hook.md` | Emotional positioning statement and final hook line from Step 1 |
| `02-launch-copy.md` | Scored and optimized launch copy from Step 2, with per-line scores and rewrites |
| `03-reply-bank.md` | 25 pre-written replies from Step 5 for use during the 48-hour window |
| `04-content-calendar.md` | Day-by-day post-launch content plan from Step 6 |
| `05-timeline.md` | The 48-hour strategic timeline with Phase 1 to 4 filled in for the specific launch |

After generating all outputs, present the user with a summary:

```
## Viral Launch Playbook Complete

**Product:** {product name}
**Launch date:** {date}

### Outputs

| Asset | Path | Status |
|-------|------|--------|
| Positioning hook | output/viral-launch/{name}/01-positioning-hook.md | Ready |
| Launch copy (scored) | output/viral-launch/{name}/02-launch-copy.md | Ready |
| Reply bank | output/viral-launch/{name}/03-reply-bank.md | Ready |
| Content calendar | output/viral-launch/{name}/04-content-calendar.md | Ready |
| 48-hour timeline | output/viral-launch/{name}/05-timeline.md | Ready |

### Gaps flagged
- [List any missing inputs, reduced-mode steps, or skipped phases]

### Next steps
- Lock the positioning hook with your team before writing final copy
- Schedule influencer outreach no later than 48 hours before launch
- Load the reply bank and keep it open during the launch window
```
