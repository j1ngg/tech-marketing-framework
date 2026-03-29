# Email Skill Autoresearch Changelog

Tracking all mutations attempted during optimization.

---

## Experiment 0 — baseline

**Score:** 23/30 (76.7%)
**Change:** None (original skill)
**Reasoning:** Establishing starting point

**Eval breakdown:**
- Event specificity: 3/5 (60%)
- Clear reason to respond: 5/5 (100%)
- Peer proof in Email 2: 5/5 (100%)
- Specific customer result: 5/5 (100%)
- Soft close in Email 4: 5/5 (100%)
- Personal feel: 0/5 (0%)

**Key failures:**
- Event specificity: Skill doesn't enforce naming the specific event with enough detail (location, host, context)
- Personal feel: Every output feels templated; openers use generic topic labels ("identity risks", "compliance challenges") instead of specific conversation details

---

## Experiment 1 — keep

**Score:** 30/30 (100%)
**Change:** Added two rules to Email 1:
1. Reference the event by name AND a specific detail (venue, host, what you were eating/drinking, a comment they made)
2. NEVER open with a generic topic label ("identity risks", "compliance challenges", "pipeline reliability"). Instead, reference a specific moment, question they asked, or detail from the conversation that only they would remember.

**Reasoning:** The "personal feel" eval was at 0% because the skill produced generic topic openers. Adding explicit instructions to reference specific moments forces personalization.

**Result:**
- Event specificity: 5/5 (100%) — up from 60%
- Personal feel: 5/5 (100%) — up from 0%
- All other evals maintained at 100%

**Improvement:** 76.7% → 100%

---

## Experiment 2 — keep (stability check)

**Score:** 30/30 (100%)
**Change:** None (verifying experiment 1 holds)
**Result:** Stable at 100%

---

## Experiment 3 — keep (final verification)

**Score:** 30/30 (100%)
**Change:** None (final verification)
**Result:** Stable at 100%. Stopping (3 consecutive at 95%+).

---

## Final Summary

**Baseline:** 23/30 (76.7%)
**Final:** 30/30 (100%)
**Improvement:** +23.3 percentage points

**Total experiments:** 4 (1 baseline + 1 mutation + 2 verification)
**Mutations kept:** 1
**Mutations discarded:** 0

**The change that mattered:**
Adding explicit rules to Email 1 requiring:
- A specific detail about the event (venue, host, context)
- A specific moment/comment from the conversation (not a generic topic label)

This single change fixed both failing evals (event specificity and personal feel) without breaking anything else.

---

## Files

- `email-autoresearch-optimized-v1.md` — the improved skill
- `SKILL.md.baseline` — the original skill (untouched)
- `results.tsv` — score log
- `changelog.md` — this file
