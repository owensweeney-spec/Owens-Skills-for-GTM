---
name: human_outreach_drafts
description: This skill should be used when the user asks to "draft a LinkedIn DM", "write an outreach email", "create a sales message", "write a cold email", or "compose a prospect message". Creates human-sounding, mobile-friendly outreach drafts with specific tense patterns and pilot suggestions.
---

# Human Outreach Drafts

Draft short, human-sounding LinkedIn DMs and emails tailored to a specific person's background, with a small, low-risk pilot suggestion and a clear, easy reply.

## Inputs

- Prospect profile summary (role, company, stack, recent activity)
- Product summary (1-2 sentences)
- Constraints (length, tone, forbidden phrases, preferred tenses)
- Feedback notes from past iterations

## Outputs

- Email draft (mobile-friendly, ~110 words max)
- LinkedIn DM draft (~75 words max)
- One-line subject suggestion (optional)
- "Why this fits" summary (1-2 sentences, internal only)

## Core Instructions

Write as a human sales rep addressing a specific person. Use their role, stack, and recent activity to pick one small, low-risk pilot. Keep it short and natural.

### Required Tense Patterns

- **Past observation**: "Saw your post about…"
- **Present rationale**: "Since you're focused on…"
- **Conditional suggestion**: "A good first thing to try could be…"
- **Modal future**: "You could have it…"
- **Habitual present**: "This usually takes 1-2 hours…"

End with a simple, low-pressure question.

### Hard Rules

- No bullets
- No em dashes
- No "AI-ish" phrases: "I'll keep this short," "if that's useful," "happy to," "just"
- Avoid corporate phrasing: "optimize," "leverage," "synergy"
- Avoid repeating the product name more than once

### Soft Rules

- One concrete pilot idea tied to their role and stack
- Make the connection to their world explicit in one clause
- Keep email under ~110 words, LinkedIn under ~75 words
- Avoid over-explaining the product

## Pilot Idea Library

Select the smallest pilot that matches their world:

- Release-readiness checklist
- Incident handoff / runbook capture
- Repo readiness / onboarding checklist
- Data-quality or validation workflow
- Migration readiness checklist

## Quality Checks

Before outputting, verify:

- First sentence references their context
- Pilot idea maps to their stack or responsibilities
- Single clear ask exists
- Reads naturally out loud
- No banned phrases present
- No "AI-ish" symmetry or filler

## Continuous Improvement

After each user edit:
1. Capture the edit and classify why it was better (tone, length, specificity, phrasing, structure)
2. Update "Do / Don't" memory list
3. Add or remove phrases from banned list
4. Track successful replies and feed openings/closings into templates
5. Maintain preferred tense pattern and enforce in future drafts

## Data to Store

Maintain lightweight memory of:
- Preferred phrases (what to keep)
- Rejected phrases (what to remove)
- Word count targets
- Top 3 pilot ideas that get replies
- Tone tags: direct, neutral, warm, pragmatic

## Reference Files

- `references/pilot_ideas.md` - Detailed pilot idea descriptions and when to use each
- `references/tense_patterns.md` - Examples of each tense pattern in context
- `references/ banned_phrases.md` - Comprehensive list of phrases to avoid
