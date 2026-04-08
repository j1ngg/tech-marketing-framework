# Autoresearch Changelog: Blog Skill

## Configuration
- **Target skill:** blog/SKILL.md
- **Test inputs:** 5 (feature announcement, product launch, thought leadership, cookbook/tutorial, news analysis)
- **Evals (v2, tightened):** 5 (reference value, "I didn't know that", naming the pain, no filler, formatting discipline)
- **Runs per experiment:** 5
- **Max score:** 25

---

## Experiment 0 — baseline (tightened evals)

**Score:** 24/25 (96%)
**Change:** None. Original skill, no modifications.
**Result:** 4 of 5 outputs passed all evals. Feature announcement failed the "no filler" eval: the three use cases (AI agents, CI/CD, service accounts) all made the same point (scoped ephemeral credentials applied to different contexts) without showing distinct capabilities.
**Failing outputs:** Feature announcement use cases section.

---

## Experiment 1 — keep

**Score:** 25/25 (100%)
**Change:** Added anti-repetition instruction to the Feature Announcement use cases section: "Each use case must highlight a DIFFERENT capability or behavior of the feature. If two use cases make the same point, merge them or replace the duplicate."
**Reasoning:** The baseline failure was the model repeating "ephemeral credentials" across all use cases. An explicit instruction to differentiate should force distinct angles.
**Result:** Use cases now show genuinely different capabilities: (1) contextual source environment verification for CI/CD, (2) purpose attestation at runtime for third-party tokens. The post explicitly distinguishes them. No filler eval now passes.
**Failing outputs:** None.

