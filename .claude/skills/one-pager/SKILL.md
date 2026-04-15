---
name: one-pager
description: "Generates a product one-pager for sales enablement. Works as a leave-behind, champion enablement doc, event handout, or top-of-funnel download. Reads from product brief, messaging, testimonials, and competitor intel to stay current as inputs evolve."
autoload: false
---

# Product One-Pager

This skill generates a one-pager that works across sales contexts: post-meeting leave-behind, champion internal selling, event handout, or top-of-funnel download. The output is a single-page document (front only, or front and back) that a technical buyer or executive can scan in 30 seconds and pass to their buying committee.

## Core Philosophy

A one-pager is not a miniature brochure. It is a decision-support tool. The reader should walk away understanding three things:
1. What problem this solves (and why it matters to them specifically)
2. How the product actually works (architecture, not hand-waving)
3. Why this and not the alternatives

Every sentence must earn its space. If a line could be deleted without losing information, delete it.

---

## Step 1: Gather Inputs

**Read from repo automatically:**

| File | What to extract |
|------|-----------------|
| `docs/inputs/product_brief.md` | Product name, one-line description, key capabilities, pricing, limitations, compliance certifications, links |
| `docs/inputs/messaging_positioning.md` | Positioning statements, value propositions by persona, pain points, channel-specific copy |
| `docs/inputs/testimonials.md` | Approved customer quotes, company names, use cases |
| `docs/inputs/competitor_intel.md` | Competitor weaknesses, positioning against alternatives |
| `docs/inputs/target_personas.md` | Buyer roles, pain points, evaluation criteria |

**Check for local overrides:** If `docs/inputs-local/` exists, read from there instead of `docs/inputs/`.

Read ALL input files BEFORE asking for additional context.

**Then ask the user (only what the inputs don't cover):**

1. **Primary audience for this version?** (e.g., "CISO at a Series C fintech" or "Head of Platform Engineering at a Fortune 500"). Default: the primary persona from target_personas.md.
2. **Primary use case?** (leave-behind, champion enablement, event handout, or top-of-funnel). Default: general-purpose (works across all).
3. **Include customer proof?** (yes/no). Default: yes. Set to no if generating for a prospect in a competing industry or if social proof isn't appropriate.
4. **Any specific capabilities or outcomes to emphasize?** The user may want to highlight a particular feature for a specific deal or event context.

---

## Step 2: Generate the One-Pager

Follow this layout structure. Each section has a defined purpose and content source.

### Section 1: Hero Banner

| Element | Content |
|---------|---------|
| **Top left** | Company logo |
| **Top right** | Document label: "PRODUCT OVERVIEW" |
| **Product name** | Large, prominent. Pull from product_brief.md |
| **Tagline** | The one-sentence positioning statement from messaging_positioning.md |
| **Subtitle** | One line expanding the tagline. Pull from the core description in messaging_positioning.md |
| **CTA** | Primary call to action with URL from product_brief.md links (e.g., "Get started free at [URL]") |

The hero should take up approximately 25% of the page. It must include a clear call to action.

### Section 2: Problem + Solution (Left Column)

**Problem statement (2 to 3 sentences max):**
- Open with the reader's reality, not yours. Name the pain they live with today.
- Be specific: name the tools that fail and why they fail for this use case.
- Pull language from the "Pain point" rows in messaging_positioning.md, tailored to the target persona.

**Solution statement (2 to 3 sentences max):**
- What the product does and how. One level more specific than the tagline.
- Must reference the mechanism, not just the outcome. Show how it works, not just what it claims to do.

**Key differentiator block:**
- A numbered or bulleted list of the product's core differentiators or unique capabilities.
- Keep each item to one line. No sub-bullets.
- Pull from product_brief.md key capabilities, distilled to the sharpest version.

### Section 3: Key Outcomes (Right Column)

Four outcome blocks, each with:
- **Bold headline** (action-oriented, 3 to 5 words)
- **One-sentence explanation**: Must be specific enough that a competitor could not paste it into their doc unchanged.

Pull outcomes from the "Benefits / Outcomes" and "How do we solve the pain?" rows in messaging_positioning.md. Prioritize outcomes that map to the target persona's pain points.

**Rules for outcomes:**
- Lead with verbs: prevent, eliminate, trace, enforce, discover, reduce, automate
- Every outcome must be falsifiable. Vague claims like "improve security" or "boost productivity" are not outcomes. Specific, measurable statements are.
- At least one outcome should map to the target persona's primary evaluation criterion

### Section 4: Architecture / How It Works

A visual showing how the product works in practice. This section should include:
- A simplified diagram showing the core product workflow or request flow
- Key components and enforcement/decision points labeled
- Integration touchpoints with the buyer's existing stack

**For the markdown output:** Describe the diagram in a callout block with enough detail that a designer can recreate it. If the user has an existing architecture diagram, reference it as the baseline.

**For the HTML output:** Use a simple CSS-based flow diagram or include a placeholder image tag with alt text describing the diagram.

### Section 5: Customer Proof (Optional)

**Include by default. Skip if the user sets "Include customer proof?" to no.**

| Element | Source |
|---------|--------|
| Customer logos | Pull company names from testimonials.md approved section |
| Pull quote | Select the single strongest quote that matches the target persona's pain point |
| Attribution | Name, company, title, exactly as listed in testimonials.md |

**Selection logic for the quote:**
- Match the quote to the target persona's primary concern (security, compliance, velocity, cost, etc.)
- If multiple quotes match, pick the one with the most specific outcome or metric
- If no good persona match, use the quote with the strongest proof of results

**Never fabricate a quote. Never use a quote from any "Pending Approval" section. Only use quotes explicitly marked as approved in testimonials.md.**

### Section 6: Footer

- Company website URL
- Pricing hook if a free tier exists (e.g., "Free for up to N users")
- Compliance certifications or trust signals as badges/icons (if applicable)
- Contact: specific person or team email, not a generic address

---

## Step 3: Output

### Phase 1: Markdown Draft

Generate a complete markdown file at `output/one-pagers/[product-name]-one-pager.md` with:
- All copy finalized and ready for review
- Layout annotations in HTML comments (e.g., `<!-- LEFT COLUMN START -->`, `<!-- RIGHT COLUMN -->`)
- A `## Design Notes` section at the bottom with guidance on visual hierarchy, typography, and spacing
- Image/diagram placeholders clearly marked

Present the draft to the user for review before proceeding to HTML.

### Phase 2: HTML/CSS (After Approval)

Generate a styled single-page HTML file at `output/one-pagers/[product-name]-one-pager.html` with:
- Inline CSS (no external dependencies)
- Print-optimized layout (`@media print` rules, A4/Letter sizing)
- Brand colors from `docs/inputs/brand_guidelines.md` (fall back to a clean dark/light theme if no brand guidelines exist)
- Typography: system fonts that approximate the brand (no external font loading)
- The layout should render correctly when opened in a browser and exported to PDF via print

---

## Writing Rules

These rules override your defaults for this skill:

1. **No banned words.** Consult the content guidelines in the project's CLAUDE.md or rules files. Never use words from any banned list.
2. **No generic fragments.** Every sentence must pass the competitor test: could a competitor paste this into their one-pager without changing a word? If yes, rewrite it with specifics only your product can claim.
3. **No placeholder links.** Every URL must be real and pulled from product_brief.md.
4. **No fabricated claims.** Every capability must trace to product_brief.md. Every quote must trace to testimonials.md (approved section only).
5. **Scannable in 30 seconds.** Bold headers, short bullets, visual hierarchy. An executive mid-meeting should find any answer in 3 seconds.

---

## Customization

The user may request variations. Handle these by adjusting content priority, not layout:

| Variation | What changes |
|-----------|-------------|
| **Persona-specific** | Swap pain points, outcomes, and pull quote to match the target persona. Layout stays the same. |
| **Event-specific** | Add event name and booth/location to the hero. Swap CTA to "Visit us at [event]." |
| **Deal-specific** | Emphasize capabilities the prospect asked about. Swap quote to a matching industry if available. |
| **Use-case-specific** | Lead with a single use case instead of the general positioning. |

---

## Related Skills

- **sales-deck**: For full slide-by-slide sales presentations
- **messaging-positioning**: For developing the foundational messaging this skill reads from
- **ads**: For paid ad copy and creative briefs
- **blog**: For long-form content that the one-pager can link to
