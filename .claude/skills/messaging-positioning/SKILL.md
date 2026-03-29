---
name: messaging-positioning
description: Interactive workshop skill for developing messaging and positioning. Walks through a structured Socratic Q&A with the team, captures answers, and builds the messaging_positioning.md doc in real time.
autoload: false
---

# Messaging & Positioning Workshop

This skill runs an interactive workshop. You are the facilitator's assistant, not the facilitator. Jing leads the conversation. Your job is to listen, capture, and build.

## How This Works

There are two modes:

**Discovery Mode (default):** Jing asks the questions below to the room. As the team answers, capture the key points. After each section, summarize what you heard and confirm before moving on. Do not invent answers. Do not fill gaps with assumptions. If a question goes unanswered, flag it as an open item.

**Build Mode:** When Jing says "build it" or "draft it," take everything captured in Discovery and populate `docs/inputs/messaging_positioning.md` using the template structure. Then flag any sections that are incomplete because of unanswered questions.

---

## Workshop Framework

### Section 1: Company Vision & Mission

**Why we start here:** Every launch should fortify the company's overall market position and vision for consistency and continuity.

Questions to walk through:

1. How does this product fit in with the reason the company exists in the first place?
2. What came before this product and what is the thinking on what will come after?
3. What was the origin of this product?

**What to capture:** The strategic narrative. How the product connects to the company's long term bet. This becomes the "In the market" positioning row.

---

### Section 2: Product Brief

Questions to walk through:

1. What does the product do?
2. What does the product not do? Or use cases where it is not a good fit?
3. Why are we the best company to build a product like this? What challenges did the team uniquely solve?
4. What specific technical capabilities or design decisions does the product have that no alternative has? Not "better" or "faster" but the concrete things that make it better or faster.
5. For each of those unique capabilities: so what? What does that enable the customer to do that they could not do before, or could not do as well? Can we quantify it?

**What to capture:** Capabilities, limitations, and the defensible moat. This populates the core description, value propositions, and the "show don't tell" proof points. Separately capture a **differentiated value map**: unique capability, the customer outcome it enables, and the proof or evidence for each.

---

### Section 3: Competitive Positioning

**Why we go here next:** No feature exists in a vacuum. However, do not assume your competitors are vendors.

Questions to walk through:

1. What would the customer use if this product did not exist? Why is this product superior?
2. Out of the reasons this product is superior, which ones would matter the most and to whom?
3. What use cases does this product enable that competitive vendor products do not?
4. For the alternatives that are not vendor products (manual processes, in house builds, open source stitching, doing nothing): what does that workflow actually look like day to day?
5. Which of these alternatives do we encounter most often in real deals? Which ones do we lose to?

**What to capture:** The competitive wedge. The "against competitor" positioning rows. The specific differentiation that matters by persona. Include a ranked list of all real alternatives (vendors, open source, manual processes, status quo) with notes on how often each shows up in deals.

---

### Section 4: Targeting

**Why we go here last:** No pain no gain but a pain resides in a person so let us get clear here.

Questions to walk through:

1. There is typically the IC and the champion or budget holder. Assuming the builder (the eng) is the IC, who in the organization is the champion?
2. For the IC (dev): What is the day to day pain? What do they search for? Where do they spend time? (Twitter, HN, YouTube)
3. For the champion: What is the business pain? What triggers them to evaluate? Where do they spend time? (LinkedIn, direct outbound, digital ads, newsletters)
4. Describe the customer who gets the MOST value from us. Not just industry and company size. What is true about their situation, their tech stack, their team, their stage of growth that makes them a perfect fit?
5. What are the "red flag" characteristics of a BAD fit customer? Who should we actively avoid?
6. When a prospect first hears about us, what category do they put us in? Is that helping or hurting us? If we could pick any market category that would make our differentiated value immediately obvious, what would it be?

**What to capture:** Two distinct persona profiles with distinct messaging angles:
- Dev channels: Twitter, HN, YouTube. Messaging focuses on speed and the "how."
- Champion channels: LinkedIn, direct outbound, digital ads, newsletters. Messaging prioritizes the business "why."

Also capture the "anti persona" (who to filter out), the best fit customer characteristics beyond firmographics, and the market category frame (whether the default category prospects assume is helping or hurting, and whether we are winning an existing category, carving a subcategory, or creating a new one).

---

## Capture Format

As answers come in, organize them under the section headers above. Use direct quotes from the team when possible. Mark anything that is an assumption or needs follow up with `[OPEN]`.

## Transition to Build Mode

When Jing says to build, populate `docs/inputs/messaging_positioning.md` with:

1. **Positioning table:** One row per context (in the market, within product suite, against each competitor or alternative identified in Section 3).
2. **Market category:** The chosen category frame, the rationale, and whether this is the default prospect assumption or a deliberate reframe.
3. **Differentiated value map:** Table with one row per unique capability. Columns: unique capability, customer outcome, proof/evidence. Separate the "check writing" value (the reason someone buys) from the "nice to have" value (supporting).
4. **Core narrative:** A sales pitch arc that flows: market insight (our point of view on the landscape) → how customers solve this today and the tradeoffs → what the ideal solution looks like → what we built → the differentiated value only we deliver → proof → the ask. This is the backbone for the sales deck, the website hero, and the founder pitch.
5. **Value propositions by use case:** Each use case gets: pain point, who cares, how we solve it, outcomes, features, proof.
6. **Channel specific messages:** Separate copy directions for dev channels (speed, how, show don't tell, benchmarks) and champion channels (business why, risk reduction, ROI). Pull from Section 4.
7. **Language rules:** Words we use, words we never use, and why. Derived from the unique capabilities and value themes surfaced in Section 2 and 3.
8. **Anti persona:** Who is not a fit and why, so marketing and sales can disqualify early.

After building, flag all `[OPEN]` items at the bottom as a follow up checklist.
