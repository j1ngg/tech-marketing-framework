---
name: blog
description: Generates SEO and AEO optimized blog posts from source content. Supports feature announcements, product launches, thought leadership, cookbooks/tutorials, and report conversions. Outputs complete posts with TLDR, FAQ, schema markup, and internal linking recommendations.
autoload: false
---

# Blog Writer

This skill transforms source content into SEO and AEO optimized blog posts. It supports five blog types, each with its own structure, word count, and CTA pattern.

## Step 1: Select Blog Type

Before generating any content, ask the user:

**What type of blog post do you need?**

| Type | Best For | Target Length |
|------|----------|---------------|
| Feature announcement | Release notes, changelog, new capability | 800 to 1,200 words |
| Product launch | New product, major release, rebrand | 1,200 to 1,800 words |
| Thought leadership | Opinion piece, industry POV, contrarian take | 1,500 to 2,500 words |
| Cookbook/tutorial | How-to guide, integration walkthrough, code example | 1,500 to 3,000 words |
| Report conversion | Whitepaper, case study, research report → blog | 1,000 to 1,500 words |

Wait for the user to select before proceeding.

---

## Authority Content Standard

Before gathering inputs, confirm the source content meets the Authority Content bar. Authority Content is what earns distribution on X, rankings on Google via LinkedIn Pulse, and citations from LLMs.

Authority Content must include at least one of:
- An original framework or model
- A contrarian take backed by data or direct experience
- A detailed breakdown of something the author actually built, tested, or measured
- A case study with specific numbers attached

It must not be:
- A repackaged "10 tips" listicle
- A summary of what everyone else is already saying
- Generic advice without a specific point of view

If the source content doesn't meet this bar, flag it: "This content reads as [generic/listicle/summary]. Authority Content needs a stronger point of view to earn algorithmic distribution and LLM citations. Can you share the original data, frameworks, or contrarian angle behind this?"

---

## Step 2: Gather Inputs

**Read from repo automatically:**

| File | What to extract |
|------|-----------------|
| `docs/inputs/product_brief.md` | Product name, capabilities, limitations (for accuracy) |
| `docs/inputs/messaging_positioning.md` | Positioning, value props, pain points |
| `docs/inputs/target_personas.md` | Audience context, technical level, job titles |

Read these files BEFORE asking for additional inputs.

**Then ask the user:**

1. **Source content** — Provide the source material:
   - File path (Markdown or PDF)
   - URL to fetch
   - Or paste the content directly

2. **Target keyword** — (Optional) What keyword should this post target? If not provided, suggest one based on the content.

3. **Internal link domain** — What domain should I pull internal links from? (e.g., `beyondidentity.com/blog` or `docs.example.com`)

4. **Disclosure needed?** — Does this post require a disclosure statement? (e.g., "Full disclosure: I work at [Company]")

5. **Distribution surfaces** — Which surfaces are you publishing to?
   - [ ] Website/blog only
   - [ ] Website + LinkedIn Pulse
   - [ ] Website + X article
   - [ ] All three (tri-publish)

   If tri-publish or platform variants selected, generate platform-specific versions in Step 4.

Wait for answers before proceeding.

---

## Step 3: Research and Context

Based on the blog type, perform targeted research:

**For all types:**
- Fetch 2 to 3 pages from the user's internal link domain to identify linking opportunities

**For thought leadership:**
- WebSearch for supporting evidence, recent statistics, or counterarguments
- Find reputable sources published within the last 2 to 3 years

**For cookbooks/tutorials:**
- WebSearch for current best practices, common pitfalls, related tools
- Verify any version numbers or API references are current

**For report conversions:**
- Read the full source document
- Identify the 3 to 5 most compelling findings to highlight

---

## Step 4: Generate Blog Post

Generate the complete blog post following the type-specific structure below.

---

## Blog Type Structures

### Feature Announcement (800 to 1,200 words)

```markdown
# [Feature Name]: [Benefit Statement]

**TLDR:** [2 to 3 sentences summarizing the feature and why it matters]

## The Problem

[What pain point does this feature solve? Who feels it?]

## Introducing [Feature Name]

[What the feature does. Be specific. Show, don't tell.]

[VISUAL: Screenshot or diagram of the feature in action]

## How It Works

[Technical explanation. Include code snippet if applicable.]

```[language]
// Example code with comments explaining each step
```

## Use Cases

### [Use Case 1]
[Specific scenario where this feature helps]

### [Use Case 2]
[Another scenario]

[VISUAL: Architecture diagram or workflow showing the feature in context]

## Getting Started

[How to enable/access the feature. Link to docs.]

## FAQ

### [Question 1 phrased as user would ask]
[Direct answer first. Then elaborate.]

### [Question 2]
[Answer]

### [Question 3]
[Answer]

---

**[CTA: Try it now / Read the docs / See it in action]**
```

**CTA pattern:** Direct to docs or product, action-oriented

---

### Product Launch (1,200 to 1,800 words)

```markdown
# [Product Name]: [Positioning Statement]

**TLDR:** [3 to 4 sentences covering what it is, who it's for, and the key differentiator]

## The Shift

[What changed in the market to make this product necessary? The provocative insight.]

## What [Old Approach] Gets Wrong

[Why the status quo no longer works. Be specific about the failure mode.]

[VISUAL: Comparison table or diagram showing old vs new approach]

## Introducing [Product Name]

[Product description. What it is, what it does, where it fits.]

[VISUAL: Product screenshot or marketecture diagram]

## Key Capabilities

### [Capability 1]
[What it does and why it matters. Map to a specific pain point.]

### [Capability 2]
[Same structure]

### [Capability 3]
[Same structure]

## Proof

[Customer results or early adopter feedback. Use only approved testimonials.]

> "[Quote from customer]" — [Name], [Title] at [Company]

[VISUAL: Results chart or customer logo grid]

## Getting Started

[How to try it. Pricing context if relevant. Link to demo or signup.]

## FAQ

### [Question about pricing/availability]
[Answer]

### [Question about migration/compatibility]
[Answer]

### [Question about security/compliance]
[Answer]

### [Question about support/SLA]
[Answer]

---

**[CTA: Request a demo / Start free trial / Talk to sales]**
```

**CTA pattern:** Lead generation focused, offer next step in buyer journey

---

### Thought Leadership (1,500 to 2,500 words)

```markdown
# [Provocative Thesis Statement]

**TLDR:** [3 to 4 sentences stating the argument and its implications]

## The Conventional Wisdom

[What most people believe. Steel-man the opposing view.]

## Why That's Wrong

[Your contrarian take. Be specific about what the conventional wisdom misses.]

[VISUAL: Data chart or framework diagram supporting your argument]

## The Evidence

### [Evidence Point 1]
[Specific data, example, or case study. Cite source with hyperlink.]

### [Evidence Point 2]
[Same structure]

### [Evidence Point 3]
[Same structure]

## The Counterargument

[Acknowledge the strongest objection to your thesis. Address it directly.]

## What This Means

[Implications for the reader. What should they do differently?]

### For [Role 1]
[Specific implications]

### For [Role 2]
[Specific implications]

## The Path Forward

[Actionable recommendations. Be specific.]

[VISUAL: Maturity model, decision framework, or action checklist]

## FAQ

### [Question challenging the thesis]
[Defend with evidence]

### [Question about applicability]
[Scope the argument appropriately]

### [Question about next steps]
[Provide actionable guidance]

---

**[CTA: Related resource / Subscribe for more / Join the discussion]**
```

**CTA pattern:** Soft CTA, build relationship, encourage engagement

---

### Cookbook/Tutorial (1,500 to 3,000 words)

```markdown
# How to [Achieve Specific Outcome] with [Tool/Product]

**TLDR:** [What you'll build/achieve and the key steps involved]

## What You'll Learn

- [Outcome 1]
- [Outcome 2]
- [Outcome 3]

## Prerequisites

- [Requirement 1 with version number if applicable]
- [Requirement 2]
- [Access/permissions needed]

## Step 1: [Action Verb] [Object]

[Explanation of what this step accomplishes]

```[language]
// Step 1: [Description]
// This code does [explanation]
[code]
```

[VISUAL: Screenshot showing expected result after this step]

## Step 2: [Action Verb] [Object]

[Explanation]

```[language]
// Step 2: [Description]
// Note: [Important caveat or tip]
[code]
```

## Step 3: [Action Verb] [Object]

[Continue pattern for all steps]

## Testing Your Implementation

[How to verify it works. Include test commands or expected output.]

```[language]
// Verify the setup
[test code]
```

**Expected output:**
```
[expected output]
```

## Troubleshooting

### [Common Error 1]
**Symptom:** [What the user sees]
**Cause:** [Why it happens]
**Fix:** [How to resolve]

### [Common Error 2]
[Same structure]

## Next Steps

- [Related tutorial 1]
- [Advanced topic to explore]
- [Community resource]

## FAQ

### [Question about prerequisites]
[Answer]

### [Question about alternatives]
[Answer]

### [Question about production readiness]
[Answer]

---

**[CTA: Try the advanced tutorial / Explore more integrations / Join the community]**
```

**CTA pattern:** Continue the learning journey, link to related content

---

### Report/Case Study Conversion (1,000 to 1,500 words)

```markdown
# [Key Finding]: [What We Learned from [Report/Study Name]]

**TLDR:** [The headline finding and its significance in 2 to 3 sentences]

## The Big Picture

[Context for the report. Why was this research conducted? What question did it answer?]

## Key Finding #1: [Finding Statement]

[Evidence from the report. Include specific numbers.]

[VISUAL: Chart or data visualization from the report]

> "[Compelling quote from the report]"

## Key Finding #2: [Finding Statement]

[Same structure]

## Key Finding #3: [Finding Statement]

[Same structure]

## What This Means for [Audience]

[Practical implications. What should readers do with this information?]

### Immediate Actions
- [Action 1]
- [Action 2]

### Strategic Considerations
- [Consideration 1]
- [Consideration 2]

## Methodology Note

[Brief description of how the research was conducted. Builds credibility.]

## FAQ

### [Question about methodology]
[Answer]

### [Question about applicability]
[Answer]

### [Question about accessing full report]
[Answer]

---

**[CTA: Download the full report / See how [Product] addresses these findings]**
```

**CTA pattern:** Gate the full content, offer product connection

---

## Platform Variants

If the user selected LinkedIn Pulse or X article variants, generate these after the main blog post.

---

### LinkedIn Pulse Variant

LinkedIn Pulse articles are indexed by Google (DR 98) and cited by LLMs at 4 to 5x the rate of a year ago. Optimize for search and LLM extractability.

**Differences from website version:**
- Add a `**LinkedIn SEO title:**` field (can differ from H1, max 100 chars, front-load keyword)
- Add a `**LinkedIn meta description:**` field (under 160 chars, keyword-rich)
- Add a `**LinkedIn CTA:**` at the end — drive comments, not clicks. Example: "What's your experience with [topic]? Drop it in the comments."
- Add an `**Author bio line:**` at the end: [Name], [Title] at [Company]. Verifiable professional identity improves LLM trust signals.

**LLM citation optimization for LinkedIn Pulse:**
- Keep paragraphs under 80 words (LLMs extract short, declarative statements)
- Use H2 sections with archetypal phrasing ("What is X", "How to Y", "X vs Y")
- Include at least one statistic with a cited source
- No invented brand terminology without context

Output format:

```
## LinkedIn Pulse Variant

**LinkedIn SEO title:** [keyword-front-loaded title, max 100 chars]
**LinkedIn meta description:** [under 160 chars, keyword-rich]

[Full article content — same body as website version, with LinkedIn CTA substituted]

**LinkedIn CTA:** [Comment-driving question or prompt]
**Author bio line:** [Name], [Title] at [Company]
```

---

### X Article Variant

X articles benefit from the algorithmic For You feed — 30 to 40% of views come from non-followers. Virality depends on strong engagement in the first 30 to 60 minutes.

**Differences from website version:**
- Sharper opening hook — first 2 sentences must create enough tension or surprise to stop a scroll
- More opinionated framing — if the article doesn't make at least some readers disagree, it won't generate quote reposts
- Add a `**Quote repost prompt:**` at the end — a 1-sentence take that's controversial or insight-dense enough to make someone want to add their own perspective
- X articles support up to 25K characters; no need to truncate

Output format:

```
## X Article Variant

[Full article content — same body with sharpened opening hook and more opinionated framing]

**Quote repost prompt:** [1-sentence take designed to provoke substantive reaction — not rage bait, but a real point of view people will want to respond to]
```

---

## SEO and AEO Requirements

Apply these to every blog post:

### Metadescription
- Under 160 characters
- Include target keyword naturally
- Convey the value proposition
- End with implicit or explicit CTA

### TLDR Section
- Place immediately after the title
- 2 to 4 sentences maximum
- Must stand alone as a complete summary
- This is what LLMs will extract for AI-generated answers

### FAQ Section
- 3 to 5 questions per post
- Phrase questions exactly as users would search them
- Start each answer with a direct response, then elaborate
- Use "What is", "How to", "Why does", "Can I" patterns

### Schema Markup Suggestions

| Blog Type | Recommended Schema |
|-----------|-------------------|
| Feature announcement | Article + FAQPage |
| Product launch | Article + FAQPage + Product |
| Thought leadership | Article + FAQPage |
| Cookbook/tutorial | HowTo + FAQPage |
| Report conversion | Article + FAQPage |

Output schema suggestion at the end of the post:

```
**Schema markup:** [Type] schema recommended. Key properties: [list]
```

### Internal Linking
- 3 to 5 contextual links per 1,000 words
- Links must be relevant to the surrounding content
- Fetch pages from user's specified domain to find real URLs
- Format as: `[anchor text](URL)` with natural anchor text

Output internal linking recommendations:

```
**Internal links to add:**
- Link to [page title](URL) in the [section name] section
- Link to [page title](URL) when mentioning [topic]
```

### LinkedIn Pulse SEO

When publishing to LinkedIn Pulse, apply these in the publishing settings:
- Set a custom SEO title in LinkedIn's article settings (separate from the H1)
- Set a custom meta description (LinkedIn now exposes this in the publishing UI)
- The article URL inherits LinkedIn's /pulse/ slug with DR 98 — no additional domain authority needed

### Heading Structure
- Use archetypal phrasing in H2s: "What is X", "How to Y", "Why Z matters"
- One H1 only (the title)
- Logical hierarchy: H2 for sections, H3 for subsections
- Front-load keywords in headings when natural

---

## Visual Callout Format

Flag visual opportunities with this format:

```
[VISUAL: Brief description of what's needed]
```

Examples:
- `[VISUAL: Screenshot of the dashboard with the new feature highlighted]`
- `[VISUAL: Architecture diagram showing data flow between components]`
- `[VISUAL: Comparison table of old approach vs new approach]`
- `[VISUAL: Code editor showing the completed implementation]`

---

## Writing Rules

### Voice and Tone
- Bold, confident, assertive
- No hedging: remove "we believe", "consider this", "it's worth noting"
- No passive voice
- Write for 5th grade comprehension (technical terms are fine when accurate)

### Formatting
- Maximum 3 dashes per piece (rewrite sentences that need more)
- Oxford comma always
- One idea per paragraph
- Short paragraphs (under 80 words)
- Use tables for comparisons
- Use bullet lists for 3+ items

### Banned Words
Never use: delve, landscape, robust, pivotal, seamless, leverage, transformative, game-changer, revolutionary, cutting-edge, integral, nuanced, foster, glean, underscore, propel, unparalleled, vast, plethora

### Claims and Evidence
- Every claim must be backed by example, data, or citation
- Hyperlink sources directly in the text
- Sources must be reputable and published within last 2 to 3 years
- Never fabricate quotes, statistics, or customer names
- Product claims must match `product_brief.md` exactly

### Code Snippets
- Always include comments explaining what the code does
- Use syntax highlighting with language specified
- Keep snippets focused (one concept per block)
- Include expected output where helpful

---

## Output Format

Output the complete blog post with this wrapper:

```markdown
# [Blog Title]

**Target keyword:** [keyword]
**Metadescription:** [under 160 chars]
**Word count:** [X words]
**Blog type:** [type]

---

[Full blog post content]

---

## Post-Publication Checklist

**Schema markup:** [Recommendation]

**Internal links to add:**
- [Link recommendations]

**Visuals needed:**
- [List of VISUAL callouts from the post]

**Social promotion:** Would you like to generate social posts for this blog? I can hand off to the `/social-posts` skill.

**Tri-publish checklist:**
- [ ] LinkedIn Pulse variant generated (if selected)
- [ ] X article variant generated (if selected)
- [ ] LinkedIn SEO title and meta description set
- [ ] Quote repost prompt written for X
- [ ] Author bio line added to LinkedIn version
```

---

## Review Checklist

Before delivering, verify the post passes:

### Structure
- [ ] TLDR present immediately after title
- [ ] FAQ section with 3 to 5 questions
- [ ] Headings use archetypal phrasing
- [ ] One H1 only, logical H2/H3 hierarchy
- [ ] CTA matches blog type pattern

### SEO/AEO
- [ ] Metadescription under 160 characters
- [ ] Target keyword appears in title, first paragraph, and 2+ headings
- [ ] FAQ questions phrased as users would search
- [ ] Each FAQ answer starts with direct response
- [ ] Schema markup suggestion included
- [ ] Internal linking recommendations included (3 to 5 per 1K words)

### Writing Quality
- [ ] No passive voice
- [ ] No hedging language
- [ ] No banned words
- [ ] Maximum 3 dashes in entire piece
- [ ] Oxford comma used correctly
- [ ] Paragraphs under 80 words
- [ ] One idea per paragraph

### Accuracy
- [ ] All product claims match product_brief.md
- [ ] All citations hyperlinked to reputable sources
- [ ] No fabricated quotes or statistics
- [ ] Code snippets include comments
- [ ] Version numbers and APIs verified current

### Visuals
- [ ] Visual callouts flagged where appropriate
- [ ] Each visual callout has specific description

### Distribution (if tri-publishing)
- [ ] Content meets Authority Content bar (original framework, contrarian take, real data, or case study with numbers)
- [ ] LinkedIn Pulse variant has custom SEO title and meta description
- [ ] LinkedIn Pulse variant ends with comment-driving CTA
- [ ] X article variant opens with scroll-stopping hook
- [ ] X article variant includes quote repost prompt
- [ ] Author bio line included on LinkedIn version

---

## Handoff Options

After the blog is complete, ask:

> "Would you like to generate social posts to promote this content? I can hand off to the `/social-posts` skill."

If yes, provide context to the social-posts skill:
- Blog title
- Blog URL (if known) or note it's unpublished
- Key points to highlight
- Target audience from the blog

If the user selected tri-publish, also confirm:

> "Here's your publishing checklist:
> - **Website**: Publish the main blog post with schema markup and internal links
> - **LinkedIn Pulse**: Use the LinkedIn variant. In LinkedIn's article settings, paste the LinkedIn SEO title and meta description. After publishing, leave a comment to seed conversation.
> - **X**: Publish the X article variant. After publishing, share the quote repost prompt as a reply or separate post to seed engagement in the first 30 to 60 minutes."

---

## Adaptation Notes

**When source content is thin:**
- Use WebSearch to supplement with current data and examples
- Flag gaps: "The source doesn't specify [X]. Please provide or I'll use [reasonable default]."

**When product_brief.md is empty:**
- Ask user for product name and 3 key capabilities
- Flag: "I'm writing without product context. Claims will be generic."

**When internal link domain returns no results:**
- Skip internal linking recommendations
- Note: "Could not fetch pages from [domain]. Add internal links manually."

**When target keyword is not provided:**
- Suggest 2 to 3 keyword options based on content
- Ask user to confirm before proceeding

**When disclosure is needed:**
- Insert after TLDR: "Full disclosure: [Statement provided by user]"

**When word count needs adjustment:**
- Minimum: 70% of target range
- Maximum: 130% of target range
- If content requires more/less, flag and confirm with user
