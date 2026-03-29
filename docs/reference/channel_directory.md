# Marketing Channel Directory for Developer Tool Launches

This is a product agnostic reference for planning launch distribution. It catalogs where developer and AI engineering audiences spend time, how to reach them, and what to expect from each channel. 

---

## Organic Community Channels

These are high trust, high scrutiny environments where developers discover and evaluate tools. You cannot buy your way in. The product and the content must earn attention.

| Channel | Audience | How to Use It | What to Expect |
|---------|----------|---------------|----------------|
| **Hacker News (Show HN)** | Senior engineers, CTOs, founders | Launch post with technical depth. No marketing language. | [PostHog reports](https://posthog.com/newsletter/marketing-for-devs) a ~1 in 10 hit rate even with strong content. Huge ego boost but actual signup lift is lower than expected. |
| **Reddit r/LocalLLaMA** | AI engineers building with open models | Participate genuinely. Share benchmarks, not pitches. | 1M+ members. High relevance for document processing and AI pipeline tools. |
| **Reddit r/MachineLearning** | ML researchers and practitioners | Benchmark posts, technical write ups | 3M+ members. More academic. Good for credibility. |
| **Reddit r/LangChain** | Engineers building AI pipelines | Integration tutorials, "how I built X with Y" posts | Directly relevant for tools that plug into AI workflows. |
| **Reddit r/ExperiencedDevs** | Senior engineers | Thoughtful discussion, not promotion | High signal community. Good for understanding pain points. |
| **Twitter/X** | AI engineers, founders, dev tool builders | Founder personal accounts. Technical threads. Benchmark screenshots. | [PostHog spends](https://posthog.com/founders/actual-marketing-budget) ~10% of paid budget here for awareness. Organic posts from founders outperform brand accounts. |
| **Bluesky** | Developer early adopters | Mirror Twitter strategy | Growing developer audience. Lower noise. |
| **LinkedIn** | VP Engineering, Head of AI, CTOs (the budget holder) | Founder personal posts. People led content, not company page content. | This is the champion channel, not the IC channel. Different messaging required. |
| **GitHub Discussions / Issues** | Engineers evaluating tools | Be present in adjacent project discussions. Answer questions. | Developers evaluate tools by looking at code first. |
| **Discord servers** | Active developer communities | Join relevant servers (LangChain, LlamaIndex, Hugging Face, tool specific). Participate. | Time intensive but high trust. |
| **Stack Overflow** | Engineers searching for solutions | Answer questions related to your problem space. | Long tail SEO value. Declining but still referenced by AI platforms. |

---

## Integration Directories and Registries

These are directories where your product can be listed as an integration, package, or tool. They provide passive, ongoing discovery by developers who are actively searching for solutions.

| Directory | What It Is | How to Get Listed | Why It Matters |
|-----------|-----------|-------------------|----------------|
| **[LlamaHub](https://llamahub.ai)** | LlamaIndex's open registry of data loaders and readers | Build a `llama_index_readers_yourproduct` package. Submit PR to [llama-hub repo](https://github.com/run-llama/llama-hub). | Developers browsing LlamaHub are actively looking for data ingestion tools. High intent. |
| **[LangChain Integrations](https://docs.langchain.com/oss/python/integrations/providers/all_providers)** | LangChain's provider directory (1000+ integrations) | Build a package, pass standard tests, submit PR. [Contributing guide](https://docs.langchain.com/oss/python/contributing/integrations-langchain). Optional co-marketing. | 200M+ monthly downloads. Note: LangChain deprioritizes document loaders for new integrations but still accepts them. |
| **[Hugging Face](https://huggingface.co)** | Models, Datasets, and Spaces | Upload models/datasets. Build a Space (interactive demo). | Massive AI/ML audience. Spaces provide free hosted demos. |
| **[Vercel Marketplace](https://vercel.com/marketplace)** | Integrations for Vercel projects | Apply through Vercel's integration program. | Growing AI category. Relevant if your tool has a web/API component. |
| **[PyPI](https://pypi.org)** | Python Package Index | Publish your Python SDK/package. | Every `pip install yourproduct` is a distribution event. Optimize the README. |
| **[npm](https://www.npmjs.com)** | Node.js package registry | Publish your JS/TS SDK. | Same as PyPI for the JavaScript ecosystem. |
| **[Docker Hub](https://hub.docker.com)** | Container image registry | Publish official Docker images. | Relevant for self hosted or on prem deployment options. |
| **[VS Code Marketplace](https://marketplace.visualstudio.com)** | Extensions for VS Code | Build an extension if your tool has an IDE use case. | Developers live in their editor. High visibility. |
| **[MCP Registries](https://github.com/anthropics/anthropic-cookbook/tree/main/misc/model_context_protocol)** | Model Context Protocol server directories | Build an MCP server for your tool. List in emerging directories. | New and growing. Early mover advantage. |
| **[Product Hunt](https://www.producthunt.com)** | Product launch platform | Schedule a launch day. Rally community for upvotes. | Concentrated signal. Good for early adopters and indie devs. Best for initial launch, not feature updates. |
| **[There's An AI For That](https://theresanaiforthat.com)** | AI tool directory | Submit your tool. | High traffic AI directory. Broad audience. |
| **[Futurepedia](https://www.futurepedia.io)** | AI tool directory | Submit your tool. | Another high traffic AI directory. |
| **[Toolify](https://www.toolify.ai)** | AI tool directory | Submit your tool. | Large inventory. Good for passive discovery. |

---

## Newsletters (Sponsorship)

Newsletter sponsorships are the highest ROI paid channel for dev tools according to [PostHog](https://posthog.com/founders/actual-marketing-budget), which spends $15K/mo on them. The key insight: "A majority of them don't work, but some are big hits. Ask your users who they actually read and watch and sponsor them."

| Newsletter | Audience | Subscribers (est.) | Notes |
|------------|----------|-------------------|-------|
| **TLDR AI** | AI engineers and technical leaders | 500K+ | Daily. High open rates. Expensive but broad reach. |
| **Alpha Signal** | AI/ML researchers and engineers | 100K+ | Curated. Technical audience. |
| **Ben's Bites** | AI builders and founders | 100K+ | Skews founder/builder. Good for awareness. |
| **The Batch (Andrew Ng)** | ML practitioners | 500K+ | Academic leaning. High credibility. |
| **Pointer** | Senior engineers (language agnostic) | 30K+ | Small but very senior audience. |
| **Import AI** | AI researchers and engineers | 60K+ | Research focused. |
| **Latent Space Newsletter** | AI engineers specifically | 50K+ | The AI engineering audience. High relevance. |
| **The Rundown AI** | Broad AI audience | 600K+ | Large but less targeted. Good for awareness. |
| **TLDR (main)** | Software engineers broadly | 1.2M+ | Massive reach. Less AI specific. |
| **Bytes** | JavaScript developers | 200K+ | Relevant if your tool has a JS SDK. |
| **Console.dev** | Developer tools specifically | 30K+ | Curated dev tool newsletter. High intent audience. |

---

## Podcasts (Guest Appearances or Sponsorship)

Podcast appearances by founders or technical leaders are high leverage. One appearance can generate months of long tail discovery. Prioritize guest spots over sponsorships when possible.

| Podcast | Audience | Format |
|---------|----------|--------|
| **Latent Space: The AI Engineer Podcast** | AI engineers | Deep technical interviews. The podcast for this ICP. |
| **Practical AI** | Applied ML, production systems | Conversational. Good for use case storytelling. |
| **Gradient Dissent (Weights & Biases)** | ML tooling and infrastructure | Technical. Good for infrastructure positioning. |
| **AI Engineering Podcast** | AI engineers | Directly targets the ICP. |
| **Changelog** | Open source developers broadly | Long running, respected. Good for OSS positioning. |
| **Software Engineering Daily** | Software engineers broadly | Wide reach. Good for general awareness. |
| **Lenny's Podcast** | Product leaders and founders | Business audience. Good for champion persona. |

---

## YouTube (Sponsorship or Collaboration)

Video is high effort but high reward. [PostHog notes](https://posthog.com/newsletter/marketing-for-devs) that "high quality ones that capture a ton of attention are hard" and require significant planning. Sponsoring existing creators is often more efficient than building your own channel from scratch.

| Channel | Audience | Why |
|---------|----------|-----|
| **Fireship** | Developers broadly | Short, punchy. PostHog sponsors him. Massive reach. |
| **Theo (t3.gg)** | Dev tools, web dev | High engagement. Commentary format drives discussion. |
| **James Briggs** | RAG, embeddings, AI pipelines | Direct overlap with document processing and AI workflow use cases. |
| **AI Jason** | AI tutorials, tool reviews | Tutorial format. Good for showing the product in action. |
| **Matt Williams** | Local AI tooling, Ollama | Overlaps with document processing and local AI workflows. |
| **NetworkChuck** | Broad developer/IT audience | Massive reach. Good for awareness campaigns. |

---

## Paid Advertising

[PostHog spends $40K/mo on paid ads](https://posthog.com/founders/actual-marketing-budget) split 50/50 between conversion and awareness. Their advice: "Run a lot of experiments across multiple channels. Each will need ~$500 and 2 weeks."

| Channel | Objective | Targeting Notes |
|---------|-----------|-----------------|
| **Google Search (product keywords)** | Conversion | Highest spend for PostHog (50% of ad budget). Target "[problem] API," "[category] tool," "how to [task]." |
| **Google Search (brand keywords)** | Conversion | Defensive. Prevent competitors from capturing your brand searches. |
| **Google Search (competitor keywords)** | Conversion | "[Competitor] alternative," "[Competitor] vs." High intent. |
| **Reddit Ads** | Awareness + Conversion | Target specific subreddits (r/LocalLLaMA, r/MachineLearning, etc.). Native format performs better. |
| **Twitter/X Ads** | Awareness | PostHog allocates ~10% of ad budget here. Good for retargeting and awareness, not direct conversion. |
| **LinkedIn Ads** | Awareness (Champion persona) | Expensive but precise targeting by title (VP Engineering, Head of AI, CTO). This is the budget holder channel. |
| **Quora Ads** | Awareness | PostHog allocates ~10%. Niche but developers do search Quora for tool comparisons. |
| **Carbon Ads** | Awareness | Serves ads on developer sites and docs. Contextually relevant. |

---

## Owned Channels

These are channels you control. [PostHog emphasizes](https://posthog.com/newsletter/marketing-for-devs): "Build a channel you actually own, like email. Twitter, LinkedIn, or praying for HackerNews success is fickle and transient."

| Channel | Purpose | Notes |
|---------|---------|-------|
| **Company blog/docs** | SEO, education, trust | [PostHog](https://posthog.com/newsletter/marketing-for-devs): "SEO still matters in the age of AI but it's a long play. Expect 5 to 6 months." Start with defensive SEO (competitor comparisons). |
| **Email newsletter** | Retention, nurture, launches | Build your own subscriber base. Do not rely on rented audiences. |
| **Changelog** | Retention, re-engagement | Public changelogs signal momentum. Supabase uses Launch Weeks to concentrate changelog energy. |
| **YouTube channel** | Education, demos, trust | High effort. Consider starting with creator sponsorships before building your own. |
| **Open source repo (GitHub)** | Discovery, trust, community | Stars, contributors, and activity signal product health. README is a landing page. |
| **Community (Discord/Slack)** | Support, feedback, advocacy | [Supabase](https://www.craftventures.com/articles/inside-supabase-breakout-growth): "Community wasn't an accessory to growth, it was the growth engine itself." |

---

## Launch Tactics

These are not channels but repeatable launch motions that use the channels above.

**Launch Week (Supabase model):** Announce a new feature every day for a week. Each day gets its own blog post, social thread, and demo. Creates concentrated buzz and gives the community something to talk about daily. [Supabase pioneered this](https://supabase.com/blog/supabase-how-we-launch) and it has been adopted across the dev tools space. Track others at [launchweek.dev](https://launchweek.dev).

**Show HN Launch:** A single, well crafted Hacker News post on launch day. Technical depth required. No marketing language. Include a live demo or benchmark. Expect a [~10% hit rate](https://posthog.com/newsletter/marketing-for-devs) even with strong content.

**Product Hunt Launch:** Schedule for a Tuesday or Wednesday. Rally community for upvotes in the first hour. Best for initial product launch, less effective for feature updates.

**Benchmark/Arena Launch:** Publish a public benchmark or comparison (like an "Arena" for your category). Generates organic discussion and positions you as the standard setter. Requires genuine technical rigor.

**Integration Launch:** Ship an integration with a popular tool (LangChain, LlamaIndex, Vercel, etc.) and co-announce. Gets you in front of their audience. The integration directory listing provides ongoing passive discovery.

---

## Channel Selection Framework

Not every launch uses every channel. Use the positioning work (specifically Section 4: Best Fit Customers) to select channels.

| If your ICP is... | Prioritize these channels |
|-------------------|--------------------------|
| **IC (the builder/engineer)** | HN, Reddit, Twitter/X, GitHub, YouTube, podcasts, dev newsletters, integration directories |
| **Champion (the budget holder)** | LinkedIn, outbound, digital ads, business newsletters, founder podcasts (Lenny's), events |
| **Both (land with IC, expand to champion)** | Start with IC channels to drive adoption, then layer champion channels for expansion. Messaging is different for each. |

The key insight: **IC channels get someone to try it. Champion channels get someone to buy it.** A launch plan needs parallel tracks with different messaging for each.
