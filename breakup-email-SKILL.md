---
name: breakup-email
description: Write a concise, personalized breakup email (80 words or less) for a prospect you've been emailing. Uses a persistent memory file to track learnings from previous emails. Includes one personalized hook with deeper inference from profile, and one binary CTA. Mention a relevant existing customer from the menu (Apple, AMD, Nvidia, Wix, Proctor and Gamble, Okta). Avoid corporate speak and em dashes.
---

# Breakup Email Skill

Write a breakup email to a prospect when:
- User has already sent multiple emails without response
- User wants to gracefully end the conversation
- Email should be under 80 words

## Memory System

Before writing each email:
1. Read `/workspace/project/Owens-Skills-for-GTM/scripts/email_memory.json` to see what has been learned from previous emails
2. After writing, append new learnings to that file in the format:
   ```json
   {
     "profile_hash": "unique identifier for this person",
     "what_worked": "what made this email effective",
     "what_to_avoid": "what fell flat or felt generic",
     "inference_used": "the deeper insight about this person that made this email stand out"
   }
   ```

## Input Requirements

The user will provide:
1. LinkedIn profile (copy/paste) - extract name, role, company, interests, background

That's it. Do not ask for previous email context or company menu. Infer what you need from their profile.

## Deep Inference Guidelines

For each prospect, analyze their profile to infer:

**What does their recent activity/certifications tell you about them?**
- If they got a cert recently: What problem were they trying to solve? What tool interest might they have?
- If they post about a conference: What topics are they focused on? What's their pain point?
- If they changed jobs recently: What's their motivation? What are they building?

**What objections might they have?**
- Senior leaders: Too busy, already has solutions, needs ROI proof
- Engineers: Wants technical depth, worries about vendor lock-in
- Managers: Worried about team adoption, needs to justify to leadership

**What would make them actually respond?**
- Specific to their company context
- Addresses a pain they likely have
- Not generic "let's chat" but something that shows you did homework

### Inference Examples

| Profile Signal | Inferred Meaning | Email Angle |
|----------------|-------------------|--------------|
| Claude Code cert | Already using AI coding tools, cares about developer experience | Mention tools that integrate with their workflow |
| Hiring DevX team | cares about developer productivity, knows the pain | Reference other companies who improved DORA metrics |
| Posts about QCon AI | Focused on AI governance, enterprise concerns | Reference enterprise-scale implementations |
| 20 years at company | Values stability, loyalty | Don't pitch disruptive change, pitch improvement |
| Active in tech communities | Early adopter, open to new tools | Can be more direct, less hand-holding |
| No recent posts | Busy or contemplative, hard to reach | Keep it shorter, lower commitment ask |
| Promotion > 6 months ago | Stale info - don't mention it | Use ongoing tenure or current work instead |
| Content shared on LinkedIn | Say "on LinkedIn" so they know where you found it | Reference the actual point they made, not just "saw your post" |
| Long tenure at industry leader (Bloomberg, etc.) | Seen trends come and go, skeptical of hype | Don't pitch disruption, pitch efficiency. Connect to their specific domain. |
| C++ / performance-focused | Cares about correctness, not flashy tools | Pitch reliability, not speed. Mention "without adding risk". |
| Financial software background | High stakes, can't break things | Pitch "add capacity without adding risk", "production systems" |
| Startup founder background | Values ROI, pragmatic | Connect to outcomes, not features |
| Side projects that ship | Actually builds things, not just talks | Reference the actual project, not their general "builder" status |
| Company transition | Must connect to WHY it matters | Don't say "interesting jump" - that's filler. Say what it reveals about them. |

### OpenHands Research (MUST DO BEFORE PRINTING)

Before writing ANY email about OpenHands:

1. **Check the GitHub repo** - OpenHands has 69K+ stars, it's an AI-driven development platform
2. **Read the docs** - Understand the product's actual capabilities
3. **Know what it IS and IS NOT** - Don't pitch what it doesn't do

**What OpenHands actually does:**
- AI coding agent that works on complex engineering tasks
- Has SDK (Software Agent SDK) - composable Python library to define agents in code
- Has CLI - like Claude Code or Codex, powered by Claude, GPT, or any LLM
- Has Local GUI - like Devin or Jules
- Has Cloud - hosted with Slack, Jira, Linear integrations
- Has Enterprise - self-hosted on Kubernetes
- SWEBench score: 77.6%

**What to pitch (specific to their context):**
- For DevSecOps: "automate security fixes in code"
- For platform teams: "scale to 1000s of agents in the cloud"
- For managers: "accelerate engineering velocity without adding headcount"
- For ICs: "work on complex tasks that would take hours"
- For enterprise leaders: "bring agents to legacy systems without risks"
- For financial services: "autonomous AI agents, sandboxed, locally hosted on internal infrastructure"
- Add social proof when possible: "100% OSS", "work with large healthcare/banking orgs"

**Better hooks:**
- Questions work better than statements: "How was your first year as...?"
- Shows genuine curiosity, not a sales pitch in disguise
- "I imagine..." works for assumptions - frames it as speculation not fact
- If you don't have enough info to personalize, DON'T. Be honest: "I don't know the specifics of your work at..."

**When to NOT pitch:**
- If their profile gives you nothing to work with (no posts, no content, no clear signal)
- Don't force personalization. It's worse to fake it than to admit you don't know.
- Consider just being honest: "This is a last attempt. If not interested, I won't reach out again."

**Voice check:**
- Would THIS person think "another vendor who doesn't get it" or "this person actually understands my world?"
- If it sounds like it could be a template with name swapped, REWRITE
- Eliminate any phrase you could put in front of ANY person

## Why AI-Generated Emails Fail (Research-Based)

A 2025 analysis revealed 84% of AI-written business emails get no response. Key reasons:

**AI-isms and Clichés to avoid:**
- "I hope this email finds you well"
- "I'm reaching out to..."
- "Please don't hesitate to contact me"
- "Just checking in"
- "Following up on my previous email"
- These instantly signal automation and feel insincere

**Lack of genuine personalization:**
- Deep, meaningful personalization beyond name merge
- Reference something specific only THEY would understand

**Bloated and indirect tone:**
- Wordy sentences that lack impact
- Filler words and "bloated" language
- Be concise and direct

**Absence of human emotion and context:**
- Can't replicate emotional nuance or shared history
- Messages feel "transactional" and "canned"

**Overuse of structure:**
- Don't rely on bullet points and formulaic structures
- Natural conversational flows work better

**Inaccuracy and hallucination:**
- Never reference something you didn't actually see on their profile
- If you can't verify it, don't say it

**How to fix:**
- Use AI as a starting point, not final product
- Rewrite in your own voice
- Add specific context only this person would recognize

## Writing Guidelines

### Structure (in order)
1. **Personalized Hook** - Use ONE deep inference from their profile, not surface-level observation
2. **Context** - Briefly acknowledge the situation (no response received)
3. **Value Anchor** - Mention a relevant customer from the menu, ideally one that matches their industry or concerns
4. **Binary CTA** - Two clear options, no more

### Recipient Perspective Check (MUST DO BEFORE PRINTING)

Before outputting any email, ask yourself:
- Would THIS PERSON open this? Or would they delete it thinking "generic pitch"?
- Did I reference something they actually OWN, not just something on their profile?
- If I reference their content, did I say WHERE I found it?
- Is the hook connected to what I'm selling, or is it a random compliment?
- Did I avoid stale info (promotions > 6 months ago, old certifications)?
- **Did I use a template and just swap in their name?** - If yes, REWRITE
- **Is the value prop specific to their domain?** - "ship faster" doesn't work for everyone. Bloomberg = "add capacity without adding risk". Healthcare = "move faster without breaking compliance".
- **Would this email ONLY work for this person?** - If you can swap the name and it works for someone else, it's not personalized enough.

If the answer to any of these is "no", REWRITE before printing.

### Anti-Template Rules

NEVER use these phrases without making them specific:
- ❌ "ship quality code faster" → ✅ "add capacity without adding risk" (for finance)
- ❌ "ship faster" → ✅ "move faster without breaking compliance" (for healthcare)
- ❌ "do more without adding headcount" → ✅ specific to their domain
- ❌ "accelerate development" → ✅ connect to what they actually build

The value prop must be rewritten for each person based on:
- Their industry (finance = can't break things, healthcare = compliance)
- Their role (IC vs manager vs exec)
- Their company's pressure points (startup = speed, enterprise = integration)

## First Principles Writing

Before writing ANY email, ask:

**Who is this person, really?**
- What keeps them up at night?
- What have they worked on for years that they care about?
- What's the ONE thing they'd want more of if they could?
- What's the ONE thing they'd want to avoid?

**What would make THEM open this?**
- Not what would make anyone open it
- What would make Gopi open it?
- What would make Nishtha open it?
- What would make Akshay open it?

**What is their context?**
- Insurance engineer: Claims can't go down, ever
- Healthcare engineer: Compliance, audit trails
- Finance engineer: Production trading systems
- Bloomberg engineer: Terminal systems that move markets

**When you have NO signal (no posts, no content):**
- Use what you know from their tenure/role
- Reference their technical background if they have one
- Don't pretend to know their challenges - state what you KNOW from the profile

Write the email to THIS person, not to a persona.

### Format Rules
- **First line**: First name followed by comma, then first sentence
  - ✅ "Rui," then "Congrats on the promotion..."
  - ❌ "Rui - Congrats on the promotion..."
- **No em dashes** - replace with commas or periods
- **80 words maximum** (strict)

### Rules
- **No corporate language** - avoid:
  - "compare notes"
  - "touch base"
  - "circle back"
  - "leverage"
  - "synergy"
  - "moving forward"
  - "revisit"
  - "connect"
- **Plain, direct language** - write like a real person
- **Put yourself in receiver's shoes** - would you open this? Would it annoy you?

### Binary CTA Examples
Instead of "Let me know if you're interested" use:
- "If you want to talk, I'm available Thursday or Friday this week. If not, no pressure."
- "If this still interests you, let me know. If not, I'll stop reaching out."
- Put binary CTA options on separate lines for readability

## Self-Critique Checklist

After writing, check each item:
- [ ] Under 80 words?
- [ ] Contains exactly ONE personalized hook that uses DEEP inference (not surface-level)?
- [ ] Hook explains WHY this matters to them specifically?
- [ ] Hook references something they OWN (not just their title or company)?
- [ ] If referencing their content, did I say WHERE (LinkedIn, post, etc.)?
- [ ] Contains exactly ONE binary CTA (two options)?
- [ ] Binary CTA options on separate lines?
- [ ] Mentions one company from the menu that's RELEVANT to their context?
- [ ] No em dashes?
- [ ] First line format is "First name," not "First name -"
- [ ] No corporate language (compare notes, circle back, etc.)?
- [ ] Would the receiver feel respected, not manipulated?
- [ ] Reads like a real human wrote it?
- [ ] Could this only apply to THIS person, or could it be swapped to anyone?
- [ ] Does it address a likely objection or concern they might have?
- [ ] Did I do the recipient perspective check before printing?

## Output Format

Provide the email in this format:

```
Subject: [Brief subject line]

[Email body - 80 words max]

---
Self-Critique:
[What worked, what didn't, what to improve for next time - be honest about weaknesses]
```

## Example

User Input:
- LinkedIn: "Sarah Chen - VP of Sales at TechCorp - previously at Salesforce - big into running marathons"
- Previous emails: 3 follow-ups about scheduling a demo
- Company to mention: Okta

Output:
```
Subject: Quick question

Sarah - saw you're training for the Boston Marathon. Impressive.

I've reached out a few times about scheduling a demo but haven't heard back. Totally get how busy things get.

We've helped similar teams at companies like Okta streamline their sales ops. If that sounds useful, happy to chat. If not, I'll stop bothering you.

Best,
[Your name]

---
Self-Critique: Hook (marathon training) is specific to them. Binary CTA gives two clear paths. Company reference (Okta) is relevant. Under 80 words. No corporate speak. Direct but not pushy. Could be improved by referencing something about her VP role and what sales teams struggle with - the marathon is surface level, what does she actually care about in her current role?
```