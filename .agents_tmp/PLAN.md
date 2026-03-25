# 1. OBJECTIVE

Enhance the existing `human_outreach_drafts` skill to follow the AgentSkills standard and best practices from the OpenHands blog on creating effective agent skills. Specifically: improve metadata/triggers, add assets folder, enhance scripts with feedback capture, and add monitoring guidance.

# 2. CONTEXT SUMMARY

The skill currently has:
- `SKILL.md` - main skill file with instructions and metadata
- `references/` - contains banned_phrases.md, pilot_ideas.md, tense_patterns.md
- `scripts/` - contains validate_draft.py and email_memory.json

The skill creates LinkedIn DMs and outreach emails for sales prospecting. It follows most of the AgentSkills structure but is missing some elements from the blog's recommendations.

# 3. APPROACH OVERVIEW

Apply the blog's guidance on skill structure:
1. Enhance triggers with more diverse activation phrases
2. Add assets/ folder with example drafts
3. Add a feedback capture script for continuous improvement
4. Add monitoring/evaluation section to SKILL.md
5. Add .gitignore to exclude memory files from version control

# 4. IMPLEMENTATION STEPS

## Step 1: Enhance SKILL.md metadata and triggers
- **Goal**: Improve skill discoverability with more comprehensive triggers
- **Method**: Update the triggers section in SKILL.md to include more variation of how users might request outreach drafts
- **Reference**: SKILL.md lines 1-4

## Step 2: Add assets folder with example drafts
- **Goal**: Provide concrete examples for the agent to reference
- **Method**: Create `assets/` folder with sample email/DM drafts showing successful patterns
- **Reference**: New directory assets/

## Step 3: Create feedback capture script
- **Goal**: Automate the "Continuous Improvement" section of the skill
- **Method**: Add script to capture user edits and classify improvements
- **Reference**: New script scripts/capture_feedback.py

## Step 4: Add .gitignore
- **Goal**: Prevent memory data from being committed
- **Method**: Create .gitignore to exclude scripts/memory*.json
- **Reference**: New file .gitignore

## Step 5: Add monitoring/evaluation guidance to SKILL.md
- **Goal**: Include guidance on logging skill usage as suggested by blog
- **Method**: Add a brief "Monitoring" section referencing OpenTelemetry/Laminar for production use
- **Reference**: SKILL.md

# 5. TESTING AND VALIDATION

## Success Criteria
- SKILL.md includes comprehensive triggers in the metadata
- assets/ folder contains at least 2 example drafts (email + LinkedIn)
- scripts/capture_feedback.py exists and is executable
- .gitignore excludes memory files
- SKILL.md includes monitoring guidance section
- validate_draft.py continues to pass existing drafts
- Skill structure matches AgentSkills standard: `SKILL.md`, `scripts/`, `references/`, `assets/`

## Verification Steps
1. Run `python scripts/validate_draft.py` on existing drafts to ensure no regressions
2. Verify assets/ folder contains example files
3. Confirm .gitignore is present and correct
4. Check SKILL.md triggers section is populated with multiple trigger phrases
