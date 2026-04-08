---
name: social-posts
description: Generates social media posts from source content. Produces brand or personal posts for LinkedIn or Twitter, tailored to each channel's audience and format.
autoload: false
---

# Social Media Post Generator

This skill transforms source content (blog posts, announcements, product launches) into social media posts.

## Step 1: Channel Selection

Before generating any content, ask the user:

**Platform:**
- LinkedIn
- Twitter/X
- Both

**Account type:**
- Brand (company voice)
- Personal (individual voice)
- Both

Wait for the user to answer before proceeding. Do not assume.

---

## Step 2: Gather Inputs

Once channel is selected, ask the user for the source content:

**How would you like to provide the source content?**
- File path (e.g., /docs/announcements/feature-launch.md)
- URL to fetch
- Paste directly

Wait for the user to provide the source before proceeding.

Then confirm you have the remaining required inputs:

1. **Author context (for personal posts):** Who is posting? Do they have personal involvement or affiliation to disclose?
2. **Brand/company name (for brand posts):** For attribution
3. **Key link:** The URL to include in the post

If any required inputs are missing, ask before generating.

---

## Step 3: Generate Posts

Generate only the posts requested. Follow the rules for the selected channel(s) below.

---

## Channel Rules

### LinkedIn

LinkedIn reaches VPs, Heads of Engineering, CTOs. Budget holders, not builders. They care about business outcomes, risk, and strategic implications.

**Brand LinkedIn:**
- Lead with the problem or market insight, not the product
- Focus on business impact and governance implications
- Use concrete numbers (time saved, cost reduced, risk mitigated)
- Structure: Problem → Impact → Solution exists → CTA
- **Never put a direct link in the post body.** End with "Full story in comments." or "Link in comments." and instruct the user to drop the URL as the first comment after publishing.
- Length: 150 to 250 words
- No hashtags in body (optional 2 to 3 at end if company standard)
- No emojis
- No subject line or greeting

**Personal LinkedIn:**
- Lead with personal experience ("I built", "I learned", "I discovered")
- Include the narrative arc: problem, action, insight
- Surface personal voice throughout
- Disclose affiliations explicitly when discussing your own product ("Full disclosure: I helped build X")
- First person throughout
- Structure: Personal hook → Story → Insight → Disclosure (if applicable) → CTA
- **Never put a direct link in the post body.** End with "Full story in comments." or "Link in comments." and instruct the user to drop the URL as the first comment after publishing.
- Length: 200 to 350 words
- No hashtags
- No emojis

---

### Twitter/X

Twitter reaches engineers, builders, founders. They want technical depth, concrete details, and practitioner credibility.

**Brand Twitter:**
- Lead with the most surprising or concrete fact
- Thread format (4 to 6 posts) for substantial content; single post for simple announcements
- Post 1: Hook with sharpest insight or number
- Posts 2 to N: One idea per post, build the argument
- Final post: Link with minimal framing
- Each post: Under 280 characters
- Use line breaks for lists within posts
- One emoji max per thread, only if it adds signal

**Personal Twitter:**
- Lead with "I built" / "I learned" / "Here is what happened when"
- Thread format for substantial content
- Include technical details that demonstrate practitioner credibility
- Share what went wrong or what surprised you
- Disclose affiliations when relevant
- Each post: Under 280 characters
- Structure: Personal hook → Technical details → Insight → Link

---

## Audience Assumptions

- Assume expert audience. Use acronyms without spelling them out (MFA, FIDO, NHI, EDR, SIEM, CSPM).
- Vary openers across posts. If generating multiple posts, do not start them the same way.

---

## Content Transformation Rules

### What to extract from source

| Element | Use in social |
|---------|---------------|
| Concrete numbers | Lead with these. "30 seconds" beats "faster." |
| Personal narrative | Personal posts only. Preserve "I" voice. |
| Technical architecture | Twitter threads. Break into discrete facts. |
| Business implications | LinkedIn. Frame as risk, cost, or strategic value. |
| Surprising insights | Hooks for all channels. |
| Affiliation/disclosure | Personal posts. Explicit "Full disclosure" statement. |

### What to cut

- Background context (social readers skim)
- Hedging language ("we believe", "it is possible that")
- Section headers (flatten into narrative)
- Long code blocks (summarize or reference)
- Repetition

---

## Formatting Rules (All Channels)

- No dashes. Rewrite sentences that require them.
- No passive voice.
- No buzzwords (robust, seamless, transformative, game-changer, revolutionary, cutting-edge, leverage).
- No soft intros ("In today's world", "As we all know").
- No dramatic openings ("Passwords are dead", "Everything is broken").
- No fear-mongering ("catastrophic", "wide open").
- No formulaic structures ("It wasn't just X, it was Y").
- No rhetorical questions at the end.
- No transition word chains (moreover, furthermore, additionally).
- Specific beats vague. "30 seconds" not "much faster."

---

## Output Format

### For LinkedIn (single post)

```
## [Brand/Personal] LinkedIn

[Post content]

---
Character count: [X]
```

### For Twitter (thread)

```
## [Brand/Personal] Twitter/X

**Post 1 of N**
[Content]
[Character count: X]

**Post 2 of N**
[Content]
[Character count: X]

...
```

---

## Review Checklist (Self-Check Before Delivery)

Before delivering, verify:

- [ ] No dashes
- [ ] No passive voice
- [ ] No banned words or phrases
- [ ] No rhetorical questions at end
- [ ] LinkedIn: 150+ words (brand) or 200+ words (personal)
- [ ] Twitter: Each post under 280 characters
- [ ] Personal posts use first person
- [ ] Affiliations disclosed (if applicable)
- [ ] Concrete numbers in hooks where available
- [ ] Exactly one link placement per post/thread (Twitter: in final post; LinkedIn: "Link in comments" CTA, never a direct URL in the post body)

---

## LinkedIn Carousel Prompt

After generating any LinkedIn post (brand or personal), ask the user:

> "Want me to generate a LinkedIn carousel to go with this post?"

If yes, invoke the `/image` skill targeting LinkedIn carousel format. If `docs/inputs-local/carousel_style_ceros.md` exists, use it as the style reference. Otherwise fall back to `docs/inputs/brand_guidelines.md`.

---

## Adaptation Notes

- If source has no personal narrative and user requests personal posts, flag that author input is needed
- If source has no concrete numbers, flag as a gap
- If author has no affiliation to disclose, omit disclosure
- For shallow source content, use single post instead of weak thread
