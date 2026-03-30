---
name: ads
description: Generates paid ad copy for Google, Meta, and LinkedIn. Produces platform-ready variants using a creative matrix approach with headlines, descriptions, and image briefs.
autoload: false
---

# Paid Ads Generator

This skill transforms your product context into paid ad copy. It uses a creative matrix (Topics x Personas x Angles) to generate targeted variants for each platform.

## Step 1: Platform Selection

Before generating any content, ask the user:

**Platform:**
- Google Ads (Search or Display)
- Meta (Facebook/Instagram)
- LinkedIn
- Multiple platforms

**Ad format:**
- Search (text only)
- Display/Feed (image + copy)

Wait for the user to answer before proceeding.

---

## Step 2: Campaign Context

Ask the user:

1. **Campaign objective:** Awareness, consideration, or conversion?
2. **Landing page URL:** Where does the ad drive traffic?
3. **Specific offer or CTA:** (Optional) Any promotion, demo offer, or specific action?

Wait for answers before proceeding.

---

## Step 3: Gather Inputs

**Read from repo automatically:**

| File | What to extract |
|------|-----------------|
| `docs/inputs/product_brief.md` | Product name, 3 to 5 key capabilities, available links |
| `docs/inputs/messaging_positioning.md` | Pain points (become Topics), value propositions |
| `docs/inputs/target_personas.md` | Audience segments (become Personas) |
| `docs/inputs/competitor_intel.md` | Competitor weaknesses, differentiation points |

Read these files before asking for additional inputs.

**Then ask:**

> "Do you have recent competitive research to incorporate? If you ran how-they-market on a competitor, provide the file path (e.g., `output/research/competitor-name.json`). Otherwise, type 'skip' and I'll use the static competitor intel."

If the user provides a path, read that file and extract:
- Competitor messaging patterns
- Gaps in their positioning
- Angles they are not using

If the user types "skip" or the file does not exist, proceed with `docs/inputs/competitor_intel.md` only.

---

## Step 4: Build the Creative Matrix

Construct the matrix from gathered inputs:

**Topics** (from messaging_positioning.md):
- Extract 3 to 4 pain points or value propositions
- Each becomes a core message theme

**Personas** (from target_personas.md):
- Extract 2 to 3 primary audience segments
- Each gets tailored language and emphasis

**Angles** (standard set):
- **Problem-agitation:** Lead with the pain, twist the knife
- **Social proof:** Lead with who else uses it, results they got
- **How-to:** Lead with the action, product enables it
- **Comparison:** Lead with competitor weakness, your strength (use competitor intel)

**Matrix output:** Topics x Personas x Angles

Do NOT generate all combinations. Select the 3 to 5 strongest combinations based on:
- Campaign objective (conversion = problem-agitation, social proof)
- Platform (LinkedIn = social proof works well for budget holders)
- Available proof points (only use social proof if testimonials exist)

---

## Step 5: Generate Ad Copy

Generate 3 to 5 variants for each selected platform. Follow platform-specific rules below.

---

## Platform Rules

### Google Search Ads (Responsive Search Ads)

| Element | Spec | Guidance |
|---------|------|----------|
| Headlines | Up to 15, 30 chars each | Write 6 to 8. Front-load keywords. No punctuation at end. |
| Descriptions | Up to 4, 90 chars each | Write 3 to 4. Include CTA. One with social proof if available. |
| Display URL paths | 2 paths, 15 chars each | Use product name and action (e.g., /demo, /start) |

**Google-specific rules:**
- No exclamation marks in headlines
- No ALL CAPS
- No dynamic keyword insertion placeholders unless user requests
- Headlines should work independently (they get shuffled)

### Meta Ads (Facebook/Instagram)

| Element | Spec | Guidance |
|---------|------|----------|
| Primary text | 125 chars recommended, 500 max | Hook in first line. Question or bold claim. |
| Headline | 27 chars recommended, 255 max | Benefit or CTA. Short wins. |
| Description | 27 chars recommended | Often hidden. Keep optional. |
| Image guidance | 1080x1080 or 1200x628 | Describe visual concept, not just "product screenshot" |

**Meta-specific rules:**
- No text covering more than 20% of image
- Primary text: First 125 chars must hook (rest gets truncated)
- Mobile-first: Assume thumb-stopping in feed

### LinkedIn Ads

| Element | Spec | Guidance |
|---------|------|----------|
| Intro text | 150 chars before truncation, 600 max | Lead with insight or question. Business outcome focus. |
| Headline | 70 chars recommended, 200 max | Role-specific language. Speak to the budget holder. |
| Description | 100 chars recommended | Reinforce CTA. |
| Image guidance | 1200x627 | Professional. Data visualizations work well. |

**LinkedIn-specific rules:**
- Audience is VPs, Heads of, CTOs (budget holders, not builders)
- Focus on business outcomes: risk, cost, time, compliance
- Social proof from recognizable companies matters more here
- No hashtags in ad copy

---

## Angle-Specific Templates

### Problem-Agitation
```
[Pain point as question or statement]
[Consequence of not solving]
[Product as relief] + [CTA]
```

### Social Proof
```
[Company/role] + [achieved outcome]
[How they did it with product]
[CTA: See how / Get the same]
```

### How-To
```
[Action verb] + [desired outcome]
[Product makes it possible]
[CTA: Start / Try / See how]
```

### Comparison
```
[Competitor approach] = [problem with it]
[Your approach] = [better outcome]
[CTA: Switch / Compare / See the difference]
```

---

## Output Format

For each variant, output:

```
## Variant [N]: [Topic] x [Persona] x [Angle]

**Platform:** [Google/Meta/LinkedIn]
**Objective fit:** [Why this variant fits the campaign objective]

---

### Headlines
1. [Headline] (X chars)
2. [Headline] (X chars)
3. [Headline] (X chars)
[Continue as needed per platform spec]

### Descriptions
1. [Description] (X chars)
2. [Description] (X chars)
[Continue as needed per platform spec]

### Image/Creative Brief
[2 to 3 sentence description of visual concept. Include: subject, composition, mood, text overlay if any]

### Display URL / Paths
[For Google only]

---
```

After all variants, include:

```
## Summary

| Variant | Platform | Topic | Persona | Angle |
|---------|----------|-------|---------|-------|
| 1 | [Platform] | [Topic] | [Persona] | [Angle] |
| 2 | ... | ... | ... | ... |

**Recommended test priority:**
1. [Variant N] — [Why test this first]
2. [Variant N] — [Why test this second]
```

---

## Review Checklist

Before delivering, verify each variant passes:

- [ ] Headlines under character limit for platform
- [ ] Descriptions under character limit for platform
- [ ] No dashes in copy (rewrite if needed)
- [ ] No passive voice
- [ ] No banned words (robust, seamless, leverage, cutting-edge, game-changer, revolutionary, transformative)
- [ ] No hedging ("we believe", "consider")
- [ ] Claims match product_brief.md exactly
- [ ] CTA matches campaign objective
- [ ] Social proof uses only approved customers from testimonials.md
- [ ] Comparison angle uses real competitor intel, not fabricated weaknesses
- [ ] Image briefs are specific enough to execute

---

## Adaptation Notes

**When docs are incomplete:**
- If `product_brief.md` is empty, ask user for product name and 3 capabilities
- If `messaging_positioning.md` is empty, ask user for 3 pain points
- If `target_personas.md` is empty, ask user to describe 2 audience segments
- If `competitor_intel.md` is empty AND user skips research file, omit comparison angle entirely

**When testimonials are missing:**
- Do not use social proof angle with specific company names
- Fall back to generic framing: "[Industry] teams" or "Engineering leaders"

**When user wants more variants:**
- Maximum 5 per platform per session
- If they want more, suggest running the skill again with different angle priorities

**When user wants fewer variants:**
- Minimum 2 to enable A/B testing
- Ask which angles to prioritize given their objective

**Multi-platform requests:**
- Generate variants for each platform sequentially
- Adapt the same Topic x Persona x Angle to each platform's specs
- Note where messaging must differ (LinkedIn = business outcome, Meta = hook fast)
