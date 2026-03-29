---
name: skill-builder
description: Interactive workshop for designing new skills or agents. Walks through best practices, helps decide between skill vs agent, and outputs a complete SKILL.md or agent .md file.
autoload: false
---

# Skill & Agent Builder

This skill walks you through designing a new skill or agent from scratch. It enforces best practices, prevents over-engineering, and outputs a production-ready file that follows the conventions of this project.

## The Core Question: Skill or Agent?

Before we build anything, we must decide what we are building.

| Skill | Agent |
|-------|-------|
| Interactive. User participates throughout. | Autonomous. User delegates, receives results. |
| Guided production. Step by step. | Delegated execution. Fire and forget. |
| Templated output. Predictable structure. | Exploratory output. Shape depends on findings. |
| User makes decisions at each step. | LLM makes decisions on its own. |
| Best for: content generation, workshops, structured workflows | Best for: review, research, quality checks |

**Examples from this project:**

| Type | Example | Why |
|------|---------|-----|
| Skill | `messaging-positioning` | User participates in workshop, answers questions |
| Skill | `social-posts` | User selects platform, provides inputs, reviews output |
| Agent | `asset-reviewer` | Autonomous review against criteria, returns findings |

**The decision rule:**

> Does the user need to participate in the process, or do they want to delegate and receive results?

If participate → **Skill**
If delegate → **Agent**

---

## Step 1: What Are You Building?

Ask the user:

**Describe what you want to build in one sentence.**

Examples:
- "I want something that turns blog posts into email sequences"
- "I want something that reviews my ads before I run them"
- "I want something that researches competitors and summarizes findings"

Wait for the user to respond.

---

## Step 2: Skill or Agent Recommendation

Based on the user's description, recommend skill or agent. Use this logic:

**Recommend SKILL if:**
- The output is content (posts, emails, docs, copy)
- The user needs to provide inputs at multiple stages
- There are decisions to make (platform, format, tone)
- The output structure is predictable
- The workflow has clear steps

**Recommend AGENT if:**
- The task is evaluation or review
- The task is research or information gathering
- The user wants to delegate completely
- The output depends on what is discovered
- No user decisions are needed during execution

**If the user wants an agent but a skill would be better:**

Say this:

> "Based on your description, this sounds like content generation. Agents are best for autonomous tasks like review or research. Skills are better for guided production because they let you make decisions at each step (platform, format, inputs) and produce consistent output."
>
> "I recommend building this as a skill. You will get better results because [specific reason based on their description]."
>
> "Do you want to proceed with a skill, or do you still prefer an agent?"

Wait for the user to confirm before proceeding.

---

## Step 3: The Four Questions

Once skill vs agent is decided, walk through these four questions. These are mandatory. Do not skip.

### Question 1: What is the outcome?

Ask:

**What should this [skill/agent] actually produce?**

Push for specificity. Reject vague answers.

| Bad | Good |
|-----|------|
| "Help with business stuff" | "Summarize sales calls into action points" |
| "Create content" | "Turn product announcements into LinkedIn posts" |
| "Review things" | "Review ad copy for factual accuracy and banned words" |

If the answer is vague, push back:

> "That is too broad. A [skill/agent] that does everything will do nothing well. What is the ONE specific outcome you need?"

### Question 2: What information does it need?

Ask:

**What inputs does this [skill/agent] require to do its job?**

Categories to probe:
- User provided content (file path, URL, pasted text)
- Project context (product brief, positioning doc, personas)
- Configuration choices (platform, format, tone, audience)
- External data (web search, API calls)

For skills: These become the "Gather Inputs" step.
For agents: These become the files it reads or tools it uses.

### Question 3: What actions should it be allowed to take?

Ask:

**What can this [skill/agent] do? What is off limits?**

Probe:
- Read files?
- Write files?
- Search the web?
- Use specific tools?
- Call external APIs?

**Critical:** Less is more. Every tool adds complexity. If the task can be done without a tool, do not add it.

> "One tool = one clear job. Do not add web search if the task is rewriting notes. Do not add file access if the prompt alone is enough."

### Question 4: What rules must it follow?

Ask:

**What constraints, rules, or quality standards must it follow?**

Categories:
- Tone and voice rules
- Formatting requirements
- Content restrictions (banned words, phrases)
- Quality checks (what does "good" look like?)
- Edge case handling (what to do when uncertain)

For this project, always include:
- Reference to `content-guidelines.md` for any content generation
- Reference to `product_brief.md` for any product claims
- The formatting rules from CLAUDE.md (no dashes, no buzzwords, etc.)

---

## Step 4: Design Formula

Summarize the design using this formula:

```
[Skill/Agent] = Role + Goal + Tools + Rules + Output Format
```

Example:

```
Skill: Email Generator
Role: Senior email copywriter for developer tools
Goal: Transform source content into email sequences for different audiences
Tools: File read (source content), file read (product brief, positioning)
Rules: No dashes, no buzzwords, cite product brief for claims, disclose affiliations
Output: Structured email with subject, preview text, body, CTA
```

Present this to the user and confirm before proceeding.

---

## Step 5: Build the File

Generate the complete SKILL.md or agent .md file.

### For Skills

Follow this structure (based on existing skills in this project):

```markdown
---
name: [skill-name]
description: [One sentence. What it does, what it produces.]
autoload: false
---

# [Skill Title]

[One paragraph explaining what this skill does and when to use it.]

## Step 1: [First Decision Point]

[Ask user for input. Wait for response before proceeding.]

---

## Step 2: [Gather Inputs]

[List required inputs. Ask user to provide them.]

---

## Step 3: [Generate Output]

[Explain how output is generated. Include channel/format rules if applicable.]

---

## [Channel/Format] Rules

[Detailed rules for each output type. Use tables for constraints.]

---

## Output Format

[Show exact structure of output with examples.]

---

## Review Checklist

[Self-check before delivery. Use checkbox format.]

- [ ] Check 1
- [ ] Check 2
- [ ] Check 3

---

## Adaptation Notes

[Edge cases. What to do when inputs are missing or unusual.]
```

### For Agents

Follow this structure (based on asset-reviewer):

```markdown
---
name: [agent-name]
description: [One sentence. What it does, when to use it.]
tools: [List of tools: Read, Grep, Glob, WebSearch, etc.]
model: [opus/sonnet/haiku]
---

# [Agent Title]

[One paragraph establishing the agent's identity and purpose. Be specific about its role.]

## When Invoked

[Numbered steps the agent follows when triggered.]

1. [First action]
2. [Second action]
3. [etc.]

## Review/Evaluation Checklist

### 1. [Category Name]
- [ ] Check 1
- [ ] Check 2

### 2. [Category Name]
- [ ] Check 1
- [ ] Check 2

## Communication Protocol

[How the agent structures its output. What sections it includes.]

### [Output Section 1]
[What goes here]

### [Output Section 2]
[What goes here]

## Delivery Standard

[Tone and expectations for the agent's output.]
```

---

## Step 6: Test Cases

Before delivering the file, generate 10 test cases for the user:

**For skills:** 10 realistic user requests that exercise different paths through the skill.

**For agents:** 10 realistic inputs that test edge cases, quality boundaries, and failure modes.

Include:
- 5 standard cases (happy path)
- 3 edge cases (unusual inputs, missing data)
- 2 adversarial cases (inputs that might break it)

---

## Anti-Patterns to Flag

If the user's design exhibits any of these, push back:

### Over-Engineering

**Symptom:** Too many tools, too many modes, too many steps.

**Response:**
> "This is too complex for a first version. Start with one job, one output format, and two tools maximum. Add complexity only if the simple version fails."

### Vague Outcome

**Symptom:** "Help with X" instead of "Produce Y."

**Response:**
> "What is the actual deliverable? A skill or agent that 'helps with' something is not testable. What artifact does the user walk away with?"

### Premature Multi-Agent

**Symptom:** User wants to build multiple agents that coordinate.

**Response:**
> "Start with one agent. Most people do not need multiple agents. A single agent with good tools handles most tasks. Only add more agents when you see clear evidence that one agent is struggling with distinct skills."

### Tool Overload

**Symptom:** User wants to add web search, file access, database queries, APIs all at once.

**Response:**
> "Does the task actually require all these? Every tool adds failure modes. If the task can be done with fewer tools, use fewer tools. Start with the minimum and add only when something breaks."

---

## Completion

After generating the file:

1. Present the complete SKILL.md or agent .md content.
2. Tell the user where to save it:
   - Skills: `.claude/skills/[skill-name]/SKILL.md`
   - Agents: `.claude/agents/[agent-name].md`
3. Remind them to add it to `settings.local.json` (for skills that need permissions).
4. Remind them to add it to `README.md` (per project conventions).
5. Provide the 10 test cases.

---

## Reference: The Agentic Loop

For context, all agents follow this core loop:

```
User input → LLM thinks → LLM decides (respond or call tool) → if tool: execute, feed result back → repeat
```

- The LLM is the "brain" that reasons.
- Tools are the "hands" that perform actions.
- Memory is the "notepad" that records what has happened.

Workflows are deterministic (same input = same path). Agents are dynamic (LLM decides the next step). Start with workflow patterns when possible. Graduate to autonomous agents only when the LLM needs to decide the execution path dynamically.

---

## Reference: The Five Workflow Patterns

Before building a full agent, consider if one of these simpler patterns solves the problem:

| Pattern | What It Is | When to Use |
|---------|------------|-------------|
| Prompt Chaining | Sequential LLM calls, each processes previous output | Tasks that decompose into fixed subtasks |
| Routing | Classify input, route to specialized handler | Different input types need different treatment |
| Parallelization | Run multiple LLM calls simultaneously | Independent subtasks or consensus voting |
| Orchestrator-Workers | Central LLM delegates to worker LLMs | Complex tasks where subtasks are not predictable |
| Evaluator-Optimizer | One LLM generates, another evaluates and loops | Clear evaluation criteria exist |

If one of these patterns works, you may not need a full agent. Skills often implement prompt chaining or routing internally.

---

## Attribution

The agent design framework in this skill is adapted from "How to Build an AI Agent" by [@hooeem](https://x.com/hooeem). Specifically:

- The four core questions (outcome, information, actions, rules)
- The design formula: Agent = Role + Goal + Tools + Rules + Output Format
- The five workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer)
- The anti-patterns and "start simple" philosophy

Original thread: https://x.com/hooeem/status/2037250422403113188
