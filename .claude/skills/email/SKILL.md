---
name: email
description: Generates email sequences for different contexts. Currently supports event follow-up sequences. Produces ready-to-send emails with subject lines, body copy, and timing guidance.
autoload: false
---

# Email Generator

This skill generates email sequences tailored to specific contexts. Each email type has its own rules derived from sequences that performed well in production.

---

## Step 1: Select Email Type

Before generating any content, ask the user:

**What type of email sequence do you need?**

- Event follow-up (post-conference, post-meeting, post-demo)
- Customer (retention, upsell, product updates) — *coming soon*
- Prospect (cold outreach, nurture) — *coming soon*

Wait for the user to select before proceeding. If they select a type marked "coming soon," tell them it's not yet available and ask if they want event follow-up instead.

---

## Step 2: Gather Inputs (Event Follow-Up)

**First, read from the repo.** Most of what you need is already documented:

| What you need | Where to find it |
|---------------|------------------|
| Product name | `docs/inputs/product_brief.md` |
| Product capabilities | `docs/inputs/product_brief.md` (key capabilities section) |
| Pain points | `docs/inputs/messaging_positioning.md` (value propositions, pain points) |
| Social proof / customers | `docs/inputs/testimonials.md` (approved quotes and customer names) |
| Target persona context | `docs/inputs/target_personas.md` |
| Asset links | `docs/inputs/product_brief.md` (links section) |

Read these files BEFORE asking the user anything. Extract:
- Product name and 2 to 3 key capabilities
- 2 to 3 pain points from the messaging doc
- Customer names from testimonials (use approved ones only)
- Any quotes or peer voice from testimonials
- Demo, docs, or guide links from the product brief

**Then ask only for what the repo cannot tell you:**

1. **Event name** — What event/conference did you meet them at?
2. **Specific conversation context** — (Optional) Any specific topics discussed at this event that differ from the standard pain points?

If the user provides conversation-specific pain points, use those. Otherwise, use the pain points from the messaging doc.

**Note:** Sender first name and company name are filled dynamically by the user's email software. Use placeholders: `[Sender First Name]` and `[Company Name]`.

---

## Step 3: Generate Sequence (Event Follow-Up)

Generate a 4-email sequence following this exact structure. Each email has ONE job and ONE CTA.

---

### Email 1: The Recall

**Timing:** Send within 1 to 2 days of the event
**Thread:** New thread
**Job:** Remind them of the conversation and re-surface the pain

**Subject line pattern:**
- Conversational, assumes prior relationship
- References the conversation, not the event name
- Examples: "Catching up, since you may have forgotten our last convo" / "Following up on our chat about [pain point]"

**Structure:**
```
Hey [First Name],

At [event name + venue detail], I talked to a number of folks about [topic]. These kept coming up:

• [Pain point 1]
• [Pain point 2]
• [Pain point 3]

[Single direct question: "Is your team running into any of these?"]

- [Sender First Name]
```

**Rules:**
- Greeting: "Hey" + first name only
- Reference the event by name AND a specific shared detail (venue, food, atmosphere) that all attendees experienced
- Frame pain points as patterns heard from the group ("I talked to a number of folks", "these kept coming up at every table"), NOT as presumed 1:1 conversation details
- NEVER fabricate what the recipient specifically said, asked, or mentioned. You don't know what they said.
- NEVER open with a generic topic label ("identity risks", "compliance challenges", "pipeline reliability")
- List exactly 3 pain points as bullets
- End with an open question ("Is your team running into any of these?") rather than presuming their situation
- Sign-off: `[Sender First Name]` placeholder, preceded by a single dash

---

### Email 2: The Peer Voice

**Timing:** +2 work days (if no reply)
**Thread:** Reply to Email 1
**Job:** Add social proof from peers and introduce the product

**Structure:**
```
[First Name], other [role/title]s there were telling us:

"[Paraphrased quote about the problem]"

Why? Because [specific explanation]. [Company examples]. They all had one thing in common: [root cause].

[Product name] [solves this] with:

• [Capability 1]
• [Capability 2]
• [Capability 3]

[CTA: Link to demo video or short resource]

- [Sender First Name]
```

**Rules:**
- No subject line (threaded reply)
- Open with peer social proof, not product
- "Why? Because..." pattern for explanation
- Name drop 2 to 3 recognizable companies
- List exactly 3 capabilities as bullets
- CTA: Demo video or similar (medium commitment)
- Sign-off: First name only

---

### Email 3: The Proof

**Timing:** +4 work days (if no reply)
**Thread:** NEW thread (breaks the reply chain)
**Job:** Lead with customer results, offer a resource

**Subject line pattern:**
- Outcome-focused with implied social proof
- Names a role or persona, not a company
- Examples: "These CISOs prevent [bad thing] w/o [painful process]" / "How [role]s at [company type] solved [problem]"

**Structure:**
```
Hi [First Name],

[Customer names] have [achieved specific outcome].

We pulled their lessons into a short [playbook/guide]. It's practical, step-by-step guidance from [role]s who've already solved the problem.

[CTA: Link to guide]

- [Sender First Name]

P.S. Let me know if there's a specific challenge you're tackling, I can point you to the most relevant parts.
```

**Rules:**
- New thread with new subject line
- Open with customer results (specific outcome, not vague)
- Offer a resource, not a meeting
- Include P.S. with personal touch
- CTA: Guide or playbook link (low commitment)
- Sign-off: First name only

---

### Email 4: The Soft Close

**Timing:** +5 work days (if no reply)
**Thread:** Reply to Email 1 (original thread)
**Job:** Give permission to not respond, but leave door open

**Structure:**
```
Hi [First Name],

We don't force [their team type] to [do painful thing].

When you're ready to [achieve desired outcome], like the ones below, reach out. I'll be happy to show you how.

• [Problem/attack type 1]
• [Problem/attack type 2]
• [Problem/attack type 3]
• [Problem/attack type 4]
• [Problem/attack type 5]
• [Problem/attack type 6]

- [Sender First Name]
```

**Rules:**
- Reply to original thread (not Email 3)
- Open with permission/no pressure statement
- "When you're ready..." pattern
- List specific problems you solve (5 to 6 items)
- No hard CTA, just "reach out"
- Sign-off: First name only

---

## Formatting Rules (All Emails)

- **Greeting:** "Hey" or "Hi" + first name only. Never "Dear," never full name, never title.
- **Sign-off:** First name only, preceded by a dash. No title, no company, no "Best," no "Thanks."
- **Length:** 50 to 100 words body max. If it feels long, cut it.
- **Bullets:** 3 items for capabilities/pains, 5 to 6 for problem lists. Never more.
- **Links:** One link per email max. Embed in text, not bare URL. See "Link Requirements" section below.
- **No dashes in body copy.** Rewrite sentences that need them.
- **No passive voice.**
- **No marketing buzzwords.** (robust, seamless, cutting-edge, game-changer, leverage)

---

## Programmatic Personalization

These sequences are for programmatic outreach (one template, many recipients). Personalization must be real, not fabricated.

**Do:**
- Reference shared context all attendees experienced (venue, food, event theme)
- Frame pain points as patterns heard from the group ("I talked to a number of folks", "this came up at every table")
- Use open questions ("Is your team running into any of these?")

**Don't:**
- Fabricate 1:1 conversation details ("you mentioned", "you asked about", "you said")
- Presume the recipient's specific situation ("your team spends more time on X")
- Invent quotes or moments that didn't happen
- **NEVER fabricate customer names, references, testimonials, or quotes.** Only use customers explicitly listed in `docs/inputs/testimonials.md` or `docs/inputs/product_brief.md`. If no approved customers exist, use generic framing ("[Company type]s like yours") or ask the user for approved names.

The goal is to feel personal because it references real shared context, not because it pretends to remember a conversation that may not have happened.

---

## Link Requirements

**All links must be real, working URLs.** Never use placeholder text like "[link]", "(link)", or "link".

**Where to get links:**
1. Check `docs/inputs/product_brief.md` for approved asset URLs (demos, docs, guides)
2. If no links exist in docs, ask the user for the specific URL before generating

**Link distribution across the sequence:**
| Email | CTA Type | Preferred Link |
|-------|----------|----------------|
| 1 | No link | Question only |
| 2 | Demo video | Product demo or explainer video |
| 3 | Resource | Guide, playbook, or beyondidentity.ai landing page |
| 4 | No link | "Reach out" only |

**beyondidentity.ai usage:**
- Use beyondidentity.ai links for educational content, landing pages, and resource downloads
- Emails 2 and 3 should link to beyondidentity.ai when appropriate resources exist
- Verify the URL exists before including it (fetch the page if uncertain)

**Never:**
- Use placeholder URLs
- Invent URLs that might not exist
- Link to competitor sites or generic third party resources

---

## Output Format

For each email, output:

```
## Email [N]: [Name]

**Send timing:** [When to send]
**Thread:** [New thread / Reply to Email X]
**Subject:** [Subject line or "N/A - threaded reply"]

---

[Full email body]

---

**Word count:** [X]
```

After all 4 emails, include:

```
## Sequence Summary

| Email | Timing | Thread | CTA |
|-------|--------|--------|-----|
| 1 | Day 0 | New | [CTA type] |
| 2 | +2 days | Reply | [CTA type] |
| 3 | +6 days | New | [CTA type] |
| 4 | +11 days | Reply | [CTA type] |
```

---

## Review Checklist

Before delivering, verify each email passes:

- [ ] 50 to 100 words body (excluding greeting/sign-off)
- [ ] Greeting is "Hey" or "Hi" + first name only
- [ ] Sign-off is first name only with dash
- [ ] Exactly one CTA per email
- [ ] No dashes in body copy
- [ ] No passive voice
- [ ] No banned words (robust, seamless, leverage, cutting-edge, game-changer)
- [ ] Bullets are 3 items (capabilities) or 5 to 6 items (problem lists)
- [ ] Subject lines are conversational or outcome-focused (not salesy)
- [ ] All links are real, working URLs (no placeholders)
- [ ] Customer names only from approved testimonials (no fabrications)

---

## Adaptation Notes

**When docs are incomplete:**
- If `product_brief.md` is empty or a template, ask the user for product name and capabilities
- If `testimonials.md` has no approved quotes, ask the user for customer names or use "[Company type]s like yours"
- If `messaging_positioning.md` is empty, ask the user for pain points
- If no demo/guide links exist in the docs, ask the user what asset to link

**Sequence adjustments:**
- If the user cannot name the event, use "when we last spoke" as the reference
- If the user wants fewer than 4 emails, generate emails 1, 3, and 4 (drop the peer voice)
- If no peer quote is available, lead Email 2 with a specific statistic or industry trend instead
