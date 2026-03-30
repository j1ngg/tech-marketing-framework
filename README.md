# Tech Marketing Framework

A Claude Code project for developer tools marketing. Repeatable skills for content generation, messaging workshops, and autonomous skill optimization.

## Installation

**Prerequisites:** [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)

```bash
# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Clone this repo
git clone https://github.com/j1ngg/tech-marketing-framework.git
cd tech-marketing-framework

# Run Claude Code
claude
```

Claude will automatically load the marketing assistant persona and all skills.

## What This Is

This repo turns Claude Code into a senior product marketer for technical audiences. It provides:

- **Identity and voice guidelines** that prioritize technical accuracy over marketing fluff
- **Content guidelines** with strict standards for writing, formatting, and AI discoverability
- **Template docs** for product briefs, personas, competitive intel, and messaging
- **Skills for content generation** (email sequences, social posts, messaging workshops)
- **Autoresearch** for autonomous skill optimization via binary evals

## Structure

```
├── claude.md                        # Core identity and workflow instructions
├── .claude/
│   ├── rules/
│   │   └── content-guidelines.md    # Writing standards
│   ├── skills/
│   │   ├── messaging-positioning/   # Interactive workshop skill
│   │   ├── social-posts/            # Social media post generator
│   │   ├── skill-builder/           # Meta-skill for creating new skills/agents
│   │   ├── email/                   # Event follow-up email sequences
│   │   └── autoresearch/            # Skill optimization via autonomous evals
│   └── agents/
│       ├── asset-reviewer.md        # Reviews assets against guidelines
│       └── how-they-market.md       # Analyzes how others market
├── docs/
│   ├── inputs/                      # Product-specific data (fill these in)
│   │   ├── product_brief.md
│   │   ├── target_personas.md
│   │   ├── messaging_positioning.md
│   │   ├── competitor_intel.md
│   │   └── testimonials.md
│   └── reference/                   # Reusable frameworks
│       └── channel_directory.md
└── output/                          # Generated assets by type
    ├── social/
    ├── blog/
    ├── email/
    ├── ads/
    └── research/
```

## Usage

1. Clone this repo into your project or use it as a standalone workspace
2. Fill in the `/docs/inputs/` templates with your product details
3. Run Claude Code in this directory

Claude will automatically adopt the marketing assistant persona and follow the content guidelines.

### Running the Messaging Workshop

Use the `/messaging-positioning` skill to run a structured workshop:

```
/messaging-positioning
```

This walks through four discovery sections (vision, product, competitive, targeting) and builds your `messaging_positioning.md` doc in real time.

### Generating Social Posts

Use the `/social-posts` skill to generate social media content from source material:

```
/social-posts
```

The skill will ask you to select platform (LinkedIn/Twitter) and account type (brand/personal), then generate posts tailored to each channel's audience.

### Generating Email Sequences

Use the `/email` skill to generate email sequences:

```
/email
```

Currently supports **event follow-up sequences** (post-conference, post-meeting, post-dinner). The skill generates a 4-email sequence optimized for programmatic outreach:

| Email | Timing | Purpose |
|-------|--------|---------|
| 1 | Day 0 | Event recall + pain points (no link) |
| 2 | +2 days | Peer social proof + product demo |
| 3 | +6 days | Customer results + resource link |
| 4 | +11 days | Soft close + problem list (no link) |

Key features:
- Reads product info from `docs/inputs/` automatically
- Enforces real links only (no placeholders)
- Uses approved customers only (no fabrications)
- Programmatic personalization (shared context, not fake 1:1 details)

Customer and prospect email types coming soon.

### Building New Skills or Agents

Use the `/skill-builder` skill to design and create new skills or agents:

```
/skill-builder
```

This walks you through:
1. Deciding whether you need a skill or agent (with guidance if you pick the wrong one)
2. The four core questions: outcome, inputs, actions, rules
3. Design formula: Role + Goal + Tools + Rules + Output Format
4. Generating a complete SKILL.md or agent .md file
5. Test cases to validate your design

The skill prevents over-engineering by pushing back on vague outcomes, tool overload, and premature complexity.

### Optimizing Skills with Autoresearch

Use the `/autoresearch` skill to autonomously improve any existing skill:

```
/autoresearch
```

Based on Andrej Karpathy's autoresearch methodology, this skill:
1. Takes any existing skill and defines binary pass/fail evals
2. Runs the skill repeatedly against test inputs
3. Scores outputs, identifies failure patterns
4. Mutates the skill prompt one change at a time
5. Keeps improvements, discards regressions
6. Produces an improved SKILL.md, results log, and changelog

The skill runs autonomously until stopped or until it hits 95%+ pass rate for 3 consecutive experiments.

### Researching How Others Market

Use the `how-they-market` agent to analyze how a person, company, or newsletter markets themselves:

```
Analyze how [company/person/newsletter] markets
```

The agent researches the target across all channels and produces a structured report:

| Section | What it covers |
|---------|----------------|
| Channels | Where they publish (Twitter, LinkedIn, blog, newsletter, YouTube, podcast) |
| Voice & Tone | How they sound, technical depth, formatting patterns |
| Content Patterns | Posting cadence, content mix, hooks, what's working |
| Notable Tactics | 2-4 specific tactics worth learning from |
| Follow-up Research | Suggested next steps, related accounts to investigate |

Optional: Specify a focus area like "just their Twitter," "how they launch products," or "their newsletter strategy."

## Philosophy

- Write like an engineer explaining to another engineer
- Teach, do not sell
- Transparency is a competitive advantage
- Personality is a moat
- Replace adjectives with evidence

See `claude.md` for the full philosophy and `.claude/rules/content-guidelines.md` for writing standards.

## License

MIT
