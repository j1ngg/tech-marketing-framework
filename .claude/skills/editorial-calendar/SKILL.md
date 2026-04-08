---
name: editorial-calendar
description: Interactive workshop that builds a monthly rolling editorial calendar using MKT1 methodology. Walks through Perceptions, content pillars, themes, and capacity to produce a 4-week detailed plan plus 3-month roadmap. Designed to be re-run monthly.
autoload: false
---

# Editorial Calendar Workshop

This skill runs an interactive workshop to build a monthly editorial calendar grounded in Emily Kramer's MKT1 methodology. It walks through five discovery sections, captures answers, and generates a rolling content plan.

The output is designed to be re-run monthly: a detailed 4-week editorial calendar with specific content pieces, channels, and owners, plus a high-level 3-month theme roadmap that shifts forward each time.

## How This Works

**Discovery Mode (Steps 1 through 5):** Walk through five sections of questions. Capture answers as they come. After each section, summarize what you heard and confirm before moving on. Do not invent answers. Do not fill gaps with assumptions. If a question goes unanswered, flag it as `[OPEN]`.

**Generate Mode (Step 6):** When all discovery sections are complete (or the user says "generate it" or "build the calendar"), take everything captured and produce the editorial calendar output.

**Refresh Mode:** If the user already has a prior calendar and says "refresh" or "update the calendar," ask only what has changed since last month (new goals, new product launches, performance data) and regenerate. Skip sections where nothing changed.

---

## Step 1: Business Context

**Why we start here:** The editorial calendar exists to serve business goals, not to fill a publishing schedule. Emily Kramer's first principle: avoid random acts of marketing.

Questions to walk through:

1. In one sentence, what does your company do and who is it for?
2. What stage are you at? (pre-revenue, early stage, growth, scale)
3. What are the top 1 to 2 business goals this quarter? Be specific. ("Grow pipeline by 30%" not "grow the business.")
4. Which revenue levers are you prioritizing this quarter?
   - Increase top of funnel (gain market share with core audience)
   - Expand to new ICPs (grow total addressable market)
   - Increase customer value (pricing, upsell, expansion revenue)
   - Improve efficiency (conversion rates, CAC reduction)
5. What is the GTM motion? (sales-led, product-led, community-led, or hybrid)

**What to capture:** The strategic frame that every content decision filters through. If content does not serve one of these goals, it should not be on the calendar. Note which revenue lever(s) are the priority so the calendar can weight content accordingly.

---

## Step 2: Perceptions

**Why we go here next:** Perceptions are what you want your audience to repeat about you. They are the filter for every piece of content. If a piece does not reinforce at least one Perception, reconsider creating it.

Questions to walk through:

1. What 3 to 5 things do you want your audience to say about you when you are not in the room? These should be statements of belief, not product features. Example from Stripe circa 2015: "Developers should prioritize core product development, not payment infrastructure."
2. What are you actually known for today? Where is the gap between current and desired perception?
3. For each desired perception: what evidence exists (or needs to exist) to make it credible?

**What to capture:** 3 to 5 Perceptions, ranked by priority. The gap between current state and desired state for each. The evidence inventory (what proof exists, what needs to be created). These become the backbone of the content pillar structure.

---

## Step 3: Content Pillars and Audience

**Why we go here next:** Pillars translate Perceptions into content categories. Each pillar maps to one or more Perceptions and addresses the needs of a specific audience segment.

Questions to walk through:

1. Who are the primary audience segments? (Role, seniority, technical depth. Not fictional personas, real descriptions of who reads your content.)
2. For each audience: where do they spend time? (Twitter/X, HN, LinkedIn, YouTube, Reddit, newsletters, conferences, Slack communities, docs)
3. What content formats resonate with each audience? (Technical tutorials, architecture deep dives, comparison guides, thought leadership, changelogs, case studies, newsletters, video)
4. Based on your Perceptions, what 3 to 5 content pillars make sense? Pillars are topic areas you will repeatedly publish about. Example for a dev security tool: "Authentication architecture," "Compliance for engineering teams," "Identity threat landscape," "Developer experience."
5. What channels are you currently active on? What channels do you want to add?
6. What is your current publishing cadence? (Blog posts/week, social posts/week, newsletter frequency, changelog frequency)

**What to capture:** Audience segments with channel and format preferences. 3 to 5 content pillars mapped to Perceptions. Current channel mix and cadence. This determines what types of content populate the calendar and where they get distributed.

---

## Step 4: Capacity and What's Working

**Why we go here:** A calendar that exceeds capacity is fiction. Emily Kramer's rule: default to less, not more. Do not sacrifice quality bar and distribution for volume.

Questions to walk through:

1. Who creates content on your team? (Dedicated writer, engineers, founder, freelancers, agency, AI assisted)
2. How many pieces per week can you realistically produce and distribute at your quality bar? Be honest.
3. What content has performed well in the past 3 months? (Top posts by traffic, engagement, pipeline influence, or whatever your metric is)
4. What flopped or underperformed? Why?
5. Do you have a backlog of content that can be repurposed? (Old blog posts, recorded talks, internal docs, webinars, customer calls)
6. What is the ratio you want between new content and repurposed/redistributed content? (Emily Kramer's test: if you published nothing new next quarter, could your social calendar survive on repurposed content?)

**What to capture:** Team capacity (pieces/week by format). Content velocity constraints. What topics and formats have proven traction. Repurposable asset inventory. This sets the realistic volume for the calendar.

---

## Step 5: Product Roadmap and Market Context

**Why we go here last:** Product and market events create the "tent poles" around which the rest of the calendar is organized.

Questions to walk through:

1. What is shipping in the next 3 months? (Features, integrations, product updates. Include rough timing.)
2. Are any of these Tier 1 launches (major, rolling thunder) vs. Tier 3 (minor, automate)? Use the launch tiering from `claude.md`: major = human element required, medium = automate as much as reasonable, minor = fully automated.
3. Any industry events, conferences, or community moments in the next 3 months? (RSA, KubeCon, re:Invent, local meetups, webinars)
4. Any competitive moves you need to respond to or get ahead of? (Competitor launches, funding rounds, market reports)
5. Any seasonal or regulatory timing factors? (Budget cycles, fiscal year end, compliance deadlines, annual reports)

**What to capture:** A timeline of external and internal events that anchor the calendar. Launch tier for each product release. Conference and market moment dates. These become the fixed points around which flexible content is scheduled.

---

## Step 6: Generate the Calendar

When all five sections are complete (or the user triggers generation), produce the editorial calendar.

### Generation Rules

**Theme assignment:**
- Assign a monthly theme to each of the next 3 months based on the business goals, revenue levers, and product roadmap captured in discovery.
- Themes should reinforce Perceptions, not just product features.
- Emily Kramer's 70% rule: only ~30% of content should be about the product directly. The other 70% covers the problems you solve, solutions you enable, market trends, and your vision.

**Content selection:**
- For the 4-week detailed calendar, select specific content pieces based on:
  - Pillar coverage (no pillar should go 2+ weeks without content)
  - Perception reinforcement (every piece maps to at least one Perception)
  - Funnel balance (mix of awareness, consideration, and decision content)
  - Format variety (do not schedule 4 blog posts in a row with no social or newsletter)
  - Capacity fit (total pieces/week must not exceed the stated capacity)

**Repurposing track:**
- For every new "anchor" piece, suggest 2 to 3 derivative formats.
- Example: A blog post becomes a LinkedIn post, a newsletter section, and a Twitter thread.
- Emily Kramer's "pre-post" technique: schedule a social post BEFORE the anchor content publishes to tease the topic and gauge interest.

**Distribution plan:**
- Every piece gets a distribution plan at creation time, not after.
- Map each piece to primary channel + amplification channels.

**Reactive buffer:**
- Reserve 15 to 20% of capacity for reactive content (trending topics, competitive responses, community questions).
- Do not fill every slot. Leave room.

---

## Output Format

Generate three artifacts:

### Artifact 1: 3-Month Theme Roadmap

```markdown
## 3-Month Theme Roadmap

| Month | Theme | Revenue Lever | Perception Focus | Tent Pole Events | Anchor Content |
|-------|-------|---------------|------------------|------------------|----------------|
| [Month 1] | [Theme name] | [Which lever] | [P1, P3] | [Product launch, conference] | [1-2 big pieces] |
| [Month 2] | [Theme name] | [Which lever] | [P2, P4] | [Events] | [1-2 big pieces] |
| [Month 3] | [Theme name] | [Which lever] | [P1, P5] | [Events] | [1-2 big pieces] |

### Month 1: [Theme Name]
**Why this theme:** [1-2 sentences connecting to business goals and market context]

### Month 2: [Theme Name]
**Why this theme:** [1-2 sentences]

### Month 3: [Theme Name]
**Why this theme:** [1-2 sentences]
```

### Artifact 2: 4-Week Editorial Calendar

```markdown
## 4-Week Editorial Calendar: [Month Name Year]

### Week 1: [Date Range]

| Day | Content | Type | Pillar | Perception | Channel | Distribution | Owner | Status |
|-----|---------|------|--------|------------|---------|-------------|-------|--------|
| Mon | [Title/Topic] | Blog | [Pillar] | P1 | Website | LinkedIn, Newsletter, X | [TBD] | Draft |
| Wed | [Title/Topic] | Social | [Pillar] | P3 | LinkedIn | X cross-post | [TBD] | Draft |
| Thu | [Title/Topic] | Newsletter | [Pillar] | P1, P2 | Email | LinkedIn teaser | [TBD] | Draft |

### Week 2: [Date Range]
[Same table structure]

### Week 3: [Date Range]
[Same table structure]

### Week 4: [Date Range]
[Same table structure]

### Reactive Buffer
**Reserved capacity:** [X pieces/week] for:
- Trending topics in [audience channels]
- Competitive responses
- Community questions from [forums/channels]
- Breaking news in [industry area]
```

For each content piece in the calendar, include a one-line brief:

```markdown
## Content Briefs

### [Content Title 1]
**Type:** [Blog/Social/Newsletter/Changelog/Tutorial]
**Pillar:** [Which content pillar]
**Perception:** [Which perception(s) this reinforces]
**Angle:** [The specific argument or hook. Not just the topic, the point of view.]
**Target audience:** [Which segment]
**Funnel stage:** [Awareness/Consideration/Decision/Expansion]
**Distribution:** [Primary channel] → [Amplification channels]
**Pre-post opportunity:** [Yes/No. If yes, suggest the teaser.]
**Repurposing:** [What derivatives can be created from this piece]
```

### Artifact 3: Repurposing Matrix

```markdown
## Repurposing Matrix

| Source (Anchor Content) | Derivative 1 | Derivative 2 | Derivative 3 | Timing |
|------------------------|-------------|-------------|-------------|--------|
| [Blog: Topic] | LinkedIn post | Newsletter section | X thread | Same week |
| [Tutorial: Topic] | Short video clip | Code snippet social | Docs update | +1 week |
| [Changelog: Feature] | Social announcement | Blog deep dive | Email to customers | Same day |
```

---

## Review Checklist

Before delivering, verify the calendar passes:

### Strategic Alignment
- [ ] Every content piece maps to at least one Perception
- [ ] Content mix reflects the prioritized revenue lever(s)
- [ ] No pillar goes 2+ weeks without content
- [ ] 70/30 split maintained (problem/education content vs. product content)
- [ ] Monthly themes connect to stated business goals

### Capacity and Feasibility
- [ ] Total pieces per week does not exceed stated capacity
- [ ] 15 to 20% of capacity reserved for reactive content
- [ ] No single week is overloaded relative to others
- [ ] Owner column is populated (even if "TBD," no blanks)

### Funnel Balance
- [ ] Mix of awareness, consideration, and decision content
- [ ] Not all content targets the same audience segment
- [ ] At least one piece per month targets expansion/advocacy

### Distribution
- [ ] Every piece has a distribution plan (not just "publish and pray")
- [ ] Pre-post opportunities identified for anchor content
- [ ] Repurposing matrix covers all anchor pieces

### Calendar Hygiene
- [ ] Tent pole events (launches, conferences) reflected in timing
- [ ] No content conflicts with launch freeze periods
- [ ] Dates are specific (not "sometime in Week 2")

---

## Adaptation Notes

**When the user is pre-revenue or very early stage:**
- Reduce pillar count to 2 to 3 (focus beats breadth)
- Suggest founder-led content as the primary format
- Capacity is likely 1 to 2 pieces per week total
- Skip the repurposing matrix if there is no content backlog to repurpose

**When the user already has a messaging_positioning.md:**
- Offer to read it to pre-populate Perceptions and audience segments
- Ask: "Has anything changed since this was written?"

**When the user says "refresh" or "update":**
- Do not re-run all 5 sections
- Ask only: What changed? (new goals, new launches, performance data)
- Regenerate with updated context

**When capacity is very low (1 piece/week or less):**
- Focus on one pillar per month instead of covering all
- Prioritize anchor content that can be repurposed heavily
- Suggest the "pre-post then anchor" cadence: 1 social teaser → 1 blog post → 2 to 3 social derivatives per cycle

**When the user cannot articulate Perceptions:**
- Offer 3 to 5 candidate Perceptions based on what they described in Step 1
- Frame as: "If I were your audience, here is what I would take away from what you just told me. Does any of this land?"
- Iterate until they confirm 3 to 5

**When product roadmap is unclear:**
- Calendar can still be built around evergreen themes and Perceptions
- Flag: "Without a product roadmap, the calendar leans heavily on educational and thought leadership content. Product content will need to be slotted in reactively as launches are confirmed."

---

## Handoff Options

After the calendar is generated, ask:

> "Would you like to start generating any of these content pieces now? I can hand off to:"
> - `/blog` for blog posts and tutorials
> - `/social-posts` for social media content
> - `/email` for newsletter sequences
> - `/launch-roundup` for product launch packages

If the user wants to save the calendar for reference:

> "I'll save this to `output/editorial-calendar/[month-year]-editorial-calendar.md`. Re-run `/editorial-calendar` next month with 'refresh' to roll the plan forward."

---

## Methodology Attribution

This skill is built on Emily Kramer's MKT1 frameworks:
- **Perceptions framework** for strategic content direction
- **Fuel and Engine model** for content-distribution balance
- **Content Roadmap methodology** for theme-based planning
- **70/30 Story Stack rule** for product vs. non-product content mix
- **GACCS Brief** adapted for content brief structure
- **Four Revenue Levers** for business goal alignment
- **Launch Tiering** for product roadmap integration

Source: [MKT1 Newsletter](https://newsletter.mkt1.co) and [MKT1 Field Guide to B2B Startup Marketing](https://newsletter.mkt1.co/p/mkt1-field-guide-to-b2b-startup-marketing-part-1)
