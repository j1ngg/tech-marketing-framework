# Launch Framework

A Claude Code configuration for product marketing launches at developer tools companies.

## What This Is

This repo turns Claude Code into a senior product marketer. It provides:

- **Identity and voice guidelines** that prioritize technical accuracy over marketing fluff
- **Content guidelines** with strict standards for writing, formatting, and AI discoverability
- **Template docs** for product briefs, personas, competitive intel, and messaging
- **A messaging/positioning workshop skill** that facilitates structured discovery sessions

## Structure

```
├── claude.md                 # Core identity and workflow instructions
├── .claude/
│   ├── rules/
│   │   └── content-guidelines.md   # Writing standards
│   ├── skills/
│   │   └── messaging-positioning/  # Interactive workshop skill
│   └── agents/
│       └── asset-reviewer.md       # Reviews assets against guidelines
└── docs/
    ├── product_brief.md            # Product capabilities and limitations
    ├── target_personas.md          # ICP and persona definitions
    ├── competitor_intel.md         # Competitive landscape
    ├── messaging_positioning.md    # Core messaging framework
    ├── channel_directory.md        # Channel playbooks
    └── testimonials.md             # Customer proof points
```

## Usage

1. Clone this repo into your project or use it as a standalone workspace
2. Fill in the `/docs` templates with your product details
3. Run Claude Code in this directory

Claude will automatically adopt the marketing assistant persona and follow the content guidelines.

### Running the Messaging Workshop

Use the `/messaging-positioning` skill to run a structured workshop:

```
/messaging-positioning
```

This walks through four discovery sections (vision, product, competitive, targeting) and builds your `messaging_positioning.md` doc in real time.

## Philosophy

- Write like an engineer explaining to another engineer
- Teach, do not sell
- Transparency is a competitive advantage
- Personality is a moat
- Replace adjectives with evidence

See `claude.md` for the full philosophy and `content-guidelines.md` for writing standards.
