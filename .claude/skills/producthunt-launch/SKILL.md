---
name: producthunt-launch
description: "End to end Product Hunt launch skill for developer tools. Generates listing assets (tagline, description, maker comment, visual asset spec, social proof) and a dated launch plan with workstreams, asset inventory, day of runsheet, and post launch sequence. Use when: prepare a Product Hunt launch, plan a PH launch, write PH listing copy, build PH launch checklist, generate PH launch plan."
autoload: false
---

# Product Hunt Launch

This skill produces a complete Product Hunt launch package for a developer tool: the full listing copy plus a dated, owner assigned launch plan with day of runsheet and post launch sequence.

It folds together two prior skills (`producthunt-listing` and `producthunt-launch-plan`) so the listing assets and the launch plan stay in lockstep.

## When to Use This

Use when a user wants to:
- Prepare an initial product launch or major feature launch on Product Hunt
- Generate the listing copy (tagline, description, maker comment, gallery spec, social proof)
- Build a dated launch plan with workstreams, supporter outreach, runsheet, and post launch sequence
- Pressure test launch readiness (gaps in demo, supporters, hunter, testimonials)

If the user only wants listing copy, run Steps 0 to 2, then jump to "Listing Assets" and stop. If the user only wants the plan, skip "Listing Assets" and go straight to "Launch Plan".

---

## Step 0: Read Project Context

Before asking any questions, read the following project docs. If `docs/inputs-local/` exists, read from there instead of `docs/inputs/` (private inputs override public templates).

| File | What to extract |
|------|-----------------|
| `docs/inputs/product_brief.md` | Product capabilities, limitations, adoption metrics |
| `docs/inputs/messaging_positioning.md` | Core positioning, differentiated value map |
| `docs/inputs/target_personas.md` | ICP definitions, pain points |
| `docs/inputs/competitor_intel.md` | Competitive landscape, comparable tools |
| `docs/inputs/testimonials.md` | Approved customer quotes for social proof |
| `docs/producthunt_playbook.md` | PH specific tactics, hunter strategy, email and DM templates (optional, read if present) |

If the playbook is missing, note it in the final output and proceed with the rules baked into this skill.

---

## Step 1: Determine Scope

Ask the user one question and wait for the answer:

> What do you want to produce?
> 1. **Listing assets only** (tagline, description, maker comment, visual spec, social proof)
> 2. **Launch plan only** (timeline, runsheet, asset inventory, post launch sequence)
> 3. **Full launch package** (recommended — both, listing first then plan)

Default to option 3 if the user does not answer or says "everything".

---

## Step 2: Gather Launch Inputs

Ask the questions in the relevant sections below. Wait for all answers before generating any output. Do not assume.

### Launch Basics (always)

1. **What is the product?** (Name and one sentence description)
2. **Is this an initial product launch or a major feature update?** If feature update, what specifically is new?
3. **Is the product open source?**
4. **What is the target launch date?** (PH day runs 12:01 AM to 11:59 PM Pacific Time. Tuesdays and Wednesdays perform best. 2nd or 3rd week of month maximizes monthly badge potential.)

### Maker and Team (always)

5. **Who is the maker?** Name, role, and personal connection to the problem (used in maker comment). Must be a personal account, not a company account.
6. **Who else is on the launch team?** Names and roles. Need at minimum: maker, outreach lead, social lead. Ideally also a community lead.
7. **Does the team have timezone coverage for a full 24 hour launch day?** (12 AM to 11:59 PM PT)

### Existing Assets (plan + listing)

8. **What is the zero friction CTA?** Live demo URL, playground, or sandbox that requires no signup. If none exists, flag it as a gap. Top PH listings link to something a visitor can try immediately.
9. **Existing email list?** Size.
10. **Active community (Discord, Slack, etc.)?** Size.
11. **Team members with PH accounts older than 6 months?** How many. Aged accounts carry roughly 10x vote weight.
12. **Any team members with existing PH follower bases?**
13. **Existing adoption metrics to reference?** Users, downloads, GitHub stars, integration counts.

### Hunter Decision (plan only)

14. **Self hunt or pursue a third party hunter?** Self hunting gives full control. Top 500 hunters drive roughly 3.2x more upvotes but require outreach 6 weeks out. Flo Merian ([x.com/fmerian](https://x.com/fmerian)) is a key hunter and PH optimization expert.

Once all relevant questions are answered, proceed.

---

## Listing Assets

Generate all five assets in a single block, in order. Follow every rule. Pull facts only from the docs read in Step 0.

### Asset 1: Tagline Options (3 Variants)

Generate exactly three tagline options. Each must be under 60 characters.

**Rules for developer tool taglines:**
- Feature first beats benefit first. Developers parse feature statements faster than value propositions.
- If the product is open source, lead with that. "The open source [known brand] alternative" formula consistently wins (#1 Month for Appwrite Sites).
- If the product is comparable to a known tool, use the "[Product] for [category]" formula (Chronicle won with "Cursor for Slides").
- The tagline must answer "What is this?" for someone who has never heard of the product.
- No buzzwords (robust, seamless, revolutionary, cutting edge, AI powered).
- No vague benefit language ("boost productivity", "streamline workflows").

**Validation test:** State after each tagline whether a stranger could repeat back what the product does after reading it. If no, flag for revision.

**Output format:**

```
## Tagline Options

1. "[tagline]" ([character count])
   Stranger test: [pass/fail + reasoning]

2. "[tagline]" ([character count])
   Stranger test: [pass/fail + reasoning]

3. "[tagline]" ([character count])
   Stranger test: [pass/fail + reasoning]

Recommended: [number] because [reasoning]
```

### Asset 2: Description

2 to 3 paragraphs. Lead with the problem, not the solution.

**Structure:**
1. Opening hook: one sentence naming the specific pain. Use a concrete number or scenario. ("Your team spends 30 minutes daily re explaining decisions in Slack.")
2. What you built: one to two sentences in plain language.
3. How it works: one to two sentences on the mechanism. Include a technical detail that signals credibility to developers.
4. What makes it different: one sentence on the specific differentiator. Pull from the differentiated value map in `messaging_positioning.md`.

**Rules:**
- No dashes of any kind
- No passive voice
- No banned words from `.claude/rules/content-guidelines.md`
- No claims unsupported by `product_brief.md`
- Paragraphs under 80 words

### Asset 3: Maker's First Comment (Under 800 Characters)

The maker comment is weighted heavily by the PH algorithm. One quality comment is worth roughly 40 to 50 upvotes.

**Structure:**
1. Problem and personal motivation (1 to 2 sentences)
2. What is new or what changed (1 sentence)
3. One concrete use case developers will recognize (1 sentence)
4. Zero friction CTA with link (1 sentence)
5. Specific feedback ask (1 sentence)

**Rules:**
- Under 800 characters total. Display the count.
- First person voice from the maker
- No hype language
- No roadmap promises
- Anchor in user demand or adoption metrics if available
- The CTA must link to something that requires no signup

**Output format:**

```
## Maker's First Comment

[Comment text]

---
Character count: [X]/800
```

### Asset 4: Visual Asset Spec

Generate a shot list for the PH gallery based on the product's actual capabilities. Tailor every slot to the specific product. Do not use generic placeholders like "Feature A" or "Key benefit" — name the actual screen, feature, or workflow.

```
## Visual Asset Spec

### Thumbnail
- Dimensions: 240x240 px
- Content: [specific recommendation based on the product]

### Gallery Images (minimum 6)

| Slot | Dimensions | What to Show | Why |
|------|-----------|-------------|-----|
| 1 | 1270x760 | [specific screen/feature] | Hero shot, first impression |
| 2 | 1270x760 | [specific before/after] | Problem to solution contrast |
| 3 | 1270x760 | [specific feature] | Top capability |
| 4 | 1270x760 | [specific feature] | Second capability |
| 5 | 1270x760 | [specific output/result] | Proof it works (not just config) |
| 6 | 1270x760 | [specific workflow/integration] | Real world context |

### Video
- Length: 60 to 90 seconds
- Format: 60fps, auto plays muted
- Storyboard:
  1. [0 to 5s]: [specific visual hook, no title cards]
  2. [5 to 20s]: [specific problem demonstration]
  3. [20 to 50s]: [specific product solving the problem]
  4. [50 to 70s]: [specific result/output]
  5. [70 to 90s]: [CTA with URL]
- Notes: Skip cinematic production. Authentic screen recordings outperform polished videos. First 5 seconds must hook visually because video auto plays muted.
```

### Asset 5: Social Proof Hooks

Pull from `testimonials.md` for customer quotes, `product_brief.md` for adoption metrics, and any available GitHub stars, download counts, or integration stats.

```
## Social Proof Hooks

1. "[proof point]" — [source/attribution]
2. "[proof point]" — [source/attribution]
3. "[proof point]" — [source/attribution]
```

If no testimonials or metrics exist, flag it as a gap and recommend the user secure at least one before launch. Reference the playbook rule: testimonials are mandatory.

### Listing Self Check

Before delivery, verify:

- [ ] All taglines under 60 characters
- [ ] No dashes in any asset
- [ ] No passive voice
- [ ] No banned words or phrases from content guidelines
- [ ] No claims unsupported by product brief
- [ ] Maker comment under 800 characters
- [ ] Maker comment includes zero friction CTA
- [ ] Visual asset spec references actual product features (no generic placeholders)
- [ ] Description leads with problem, not solution
- [ ] Social proof hooks have attribution

After delivery, ask: "Want me to run the asset reviewer on this output?"

Save listing assets to `output/launches/{product-name}-{YYYY-MM-DD}/listing.md`.

---

## Launch Plan

Calculate every date backwards from the target launch date. Use absolute dates (e.g., "Monday, May 12") not relative dates ("6 weeks out").

### Output Format

```markdown
# Product Hunt Launch Plan: [Product Name]

**Launch date:** [Day, Date] (Pacific Time)
**Maker:** [Name]
**Hunter:** [Self / Name]
**Goal:** [Product of the Day / Top 5 / Featured]

---

## Pre Launch Readiness

### Gaps to Close Before Committing to Launch Date

[List any critical gaps identified from Step 2 answers. Examples:]
- [ ] No zero friction demo exists (top PH listings link to something visitors can try immediately)
- [ ] No team members have aged PH accounts (need 6+ months of activity for 10x vote weight)
- [ ] No email list (target 300 to 500 committed supporters minimum)
- [ ] No testimonials secured (playbook rule: testimonials are mandatory)

If any gaps are critical, recommend the user address them before committing to the launch date.

---

## Timeline: [calculated start date] to [launch date]

### Phase 1: Foundation ([6 weeks out date] to [4 weeks out date])

**PH Account Warming**
- [ ] [Date]: All team members create PH accounts (if not existing)
- [ ] [Date range]: Team engages daily on PH (upvote, comment on 2 to 3 products per day)
- [ ] [Date range]: Maker follows relevant makers and communities on PH

**Hunter Outreach** (if pursuing third party hunter)
- [ ] [Date]: Identify 5 to 10 candidate hunters in dev tools category
- [ ] [Date range]: Engage with candidates' content (comment on posts, support products they hunt)
- [ ] [Date]: Send hunter outreach DM (template in playbook)
- [ ] [Date]: Provide hunter with early product access
- [ ] [Date]: Confirm hunter commitment and share draft assets

**Supporter List Building**
- [ ] [Date]: Start monitoring [hunted.space](https://hunted.space) for category benchmarks
- [ ] [Date]: Begin identifying Tier 1 supporters (PH veterans with 6+ month accounts)
- [ ] [Date]: Set up outreach tracking spreadsheet (contact, channel, commitment, follow up status)

**Owner:** [Name]

---

### Phase 2: Outreach and Assets ([4 weeks out date] to [2 weeks out date])

**Supporter Outreach**
- [ ] [Date]: Email list Wave 1: explain PH, ask subscribers to create accounts
- [ ] [Date range]: Begin warm outreach to Tier 1 supporters via LinkedIn DMs
- [ ] [Date]: Target: 100+ committed supporters identified
- [ ] [Date]: Email list Wave 2: ask subscribers to upvote and comment on 2 to 3 products to warm accounts

**Asset Creation**
- [ ] [Date]: Listing assets generated (tagline, description, maker comment, visual spec, social proof) — see `listing.md`
- [ ] [Date]: Run asset reviewer agent on listing output
- [ ] [Date]: Begin visual asset production (screenshots, video) per visual asset spec
- [ ] [Date]: Test 3 tagline versions with 5 beta users
- [ ] [Date]: Finalize tagline based on stranger test results

**Cross Promotion**
- [ ] [Date]: Identify 5 to 10 companies for mutual launch agreements
- [ ] [Date range]: Support their launches with genuine comments and upvotes
- [ ] [Date]: Reach out to propose mutual support arrangement

**Owner:** [Name]

---

### Phase 3: Final Prep ([2 weeks out date] to [5 days out date])

**Listing Finalization**
- [ ] [Date]: Write maker's first comment (final version)
- [ ] [Date]: Complete all visual assets (minimum 6 gallery images + video)
- [ ] [Date]: Set PH teaser page live
- [ ] [Date]: Ask Tier 1 supporters to click "Notify Me"

**Launch Kit**
- [ ] [Date]: Prepare launch kit for supporters containing:
  - 2 to 3 pre written social posts (LinkedIn, Twitter, generic)
  - Product screenshots formatted for social sharing
  - 3 bullet summary of what the product does
  - Product Hunt link
  - One sentence copy paste for PH comments
- [ ] [Date]: Distribute launch kit to all committed supporters

**Social Content**
- [ ] [Date]: Run `/social-posts` skill with PH listing as source to generate launch day posts
- [ ] [Date]: Pre draft LinkedIn posts for launch day (3 to 5 posts, link always in comment not body)
- [ ] [Date]: Pre draft Twitter posts for launch day
- [ ] [Date]: Pre draft email waves (3 waves, see playbook for timing)

**Owner:** [Name]

---

### Phase 4: Final 5 Days ([5 days out date] to [day before launch])

- [ ] [Date]: Personal outreach to top 20 contacts (phone, text, voice)
- [ ] [Date]: Final review of all listing assets
- [ ] [Date]: Test all links in the listing
- [ ] [Date]: Brief supporters with launch kit and launch day timing
- [ ] [Date]: Confirm team roles and timezone coverage for launch day
- [ ] [Date]: Final rehearsal: maker posts first comment draft, team reviews

**Owner:** [Name]

---

## Launch Day Runsheet: [Launch Date]

| Time (PT) | Action | Owner | Details |
|-----------|--------|-------|---------|
| 12:01 AM | Go live | Maker | Post maker comment (written 48 hours prior) |
| 12:05 AM | Activate core team | Outreach lead | Slack/Discord DMs to most committed supporters |
| 1:00 AM | Email Wave 1 | Outreach lead | 15 to 20% of list (most engaged segment) |
| 4:00 AM | European wave | Outreach lead | Direct messages to European contacts |
| 6:00 AM | Social post 1 | Social lead | Founder LinkedIn post (personal story, link in comment) |
| 8:00 AM | Email Wave 2 | Outreach lead | Main blast, 40 to 50% of list |
| 8:00 AM | Social post 2 | Social lead | Twitter/X announcement |
| 9 AM to 12 PM | Comment engagement | Maker | Reply to every PH comment within 5 to 9 minutes |
| 10:00 AM | Network leverage | Social lead | Ask friendly founders to mention in standups |
| 12:00 PM | Social post 3 | Social lead | Mid day milestone update with ranking |
| 1:00 PM | Metrics review | Maker | Check bounce rates. Adjust landing page if >55 to 60%. |
| 4:00 PM | Email Wave 3 | Outreach lead | Plain text follow up to non openers |
| 6:00 PM | Social post 4 | Social lead | Final push, 2 to 3 hours before close |
| 8:00 PM | Transparent update | Social lead | Post ranking with final CTA |
| 11:59 PM | Transition | Maker | Screenshot final ranking. Begin post launch sequence. |

### Team Roles

| Role | Person | Timezone | Responsibility |
|------|--------|----------|---------------|
| Maker | [Name] | [TZ] | Post maker comment, respond to all PH comments, social posts |
| Outreach lead | [Name] | [TZ] | Manage email waves, DM supporters, timezone coordination |
| Social lead | [Name] | [TZ] | LinkedIn/Twitter posts and engagement throughout day |
| Community lead | [Name] | [TZ] | Activate Discord/Slack, monitor Reddit |

---

## Post Launch Plan: [Launch Date + 1] to [Launch Date + 30]

| Day | Action | Owner |
|-----|--------|-------|
| Day 1 | Thank you post and launch recap on social | Social lead |
| Day 1 | Respond to every remaining PH comment | Maker |
| Day 0 to 2 | Welcome emails to PH visitors, dedicated onboarding path | [Name] |
| Day 3 | Tutorial or quick start guide published | [Name] |
| Day 3 | Extract emails from engaged PH commenters | Outreach lead |
| Day 7 | Case study or early win story | [Name] |
| Day 7 | Follow up with journalists who covered launch | Social lead |
| Day 14 | Early access offer or discount for PH community | [Name] |
| Day 3 to 30 | Self serve: onboarding optimization, upgrade prompts | [Name] |
| Day 3 to 30 | Sales assisted: lead capture, demo loop, pilot offers | [Name] |
| Day 30 | Internal retrospective: what worked, what to change for next launch | All |

---

## Asset Inventory

| Asset | Status | Owner | Due Date | Reviewer |
|-------|--------|-------|----------|----------|
| PH tagline (3 options, tested) | [ ] | | | |
| PH description | [ ] | | | |
| Maker's first comment | [ ] | | | |
| Gallery images (6+ at 1270x760) | [ ] | | | |
| Product video (60 to 90s) | [ ] | | | |
| Thumbnail (240x240) | [ ] | | | |
| Launch kit for supporters | [ ] | | | |
| LinkedIn posts (3 to 5 pre drafted) | [ ] | | | |
| Twitter posts (pre drafted) | [ ] | | | |
| Email Wave 1 (most engaged, 15 to 20%) | [ ] | | | |
| Email Wave 2 (main blast, 40 to 50%) | [ ] | | | |
| Email Wave 3 (follow up, non openers) | [ ] | | | |
| Dedicated PH onboarding path | [ ] | | | |
| Zero friction demo/playground | [ ] | | | |
| Welcome email for PH visitors | [ ] | | | |

---

## Success Metrics

| Metric | Target (Featured) | Target (Not Featured) |
|--------|-------------------|----------------------|
| Upvotes | 500+ | 100+ |
| Comments | 50+ genuine | 15+ |
| Visitors | 1,000 to 5,000 | 100 to 500 |
| Signups | 10 to 150 | 1 to 15 |
| Visitor to signup rate | 15 to 25% | 10 to 15% |
| Result | Product of the Day | Featured |

---

## Multi Launch Note

Product Hunt rewards compounding. Each launch adds followers who get notified of the next one. After this launch, identify the next major feature milestone that qualifies for a separate launch. Only launch for major feature releases, new platform or integration support, or significant version milestones. Do not launch for bug fixes, UI refreshes, or minor improvements.
```

Save the launch plan to `output/launches/{product-name}-{YYYY-MM-DD}/launch-plan.md`.

---

## Step Final: Review and Adjust

After generating, ask the user:

1. "Are the team role assignments correct?"
2. "Are there any dates that conflict with holidays, company events, or other launches?"
3. "Do you want to adjust the goal (Product of the Day vs Featured vs Top 5)?"

Make adjustments based on their answers and output the final files.

---

## Output Locations

| Scope | Files |
|-------|-------|
| Listing only | `output/launches/{product-name}-{YYYY-MM-DD}/listing.md` |
| Plan only | `output/launches/{product-name}-{YYYY-MM-DD}/launch-plan.md` |
| Full package | both files in the same directory |

Use the launch date for the `{YYYY-MM-DD}` suffix so multi launch products keep distinct directories.
