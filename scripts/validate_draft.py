#!/usr/bin/env python3
"""
Validation script for human_outreach_drafts skill.
Enforces: no em dashes, no bullets, no banned phrases.
"""

import re
import sys
from pathlib import Path

# Banned phrases (case-insensitive)
BANNED_PHRASES = [
    "i'll keep this short",
    "if that's useful",
    "happy to",
    "just wanted",
    "quick question",
    "hope you're doing well",
    "i wanted to reach out because",
    "not sure if this is relevant",
    "curious if",
    "worth a shot",
    "optimize",
    "leverage",
    "synergy",
    "streamline",
    "unlock",
    "revolutionize",
    "transform",
    "game-changing",
    "disrupt",
    "scalable",
    "best-in-class",
    "world-class",
    "cutting-edge",
    "book a demo",
    "schedule a call",
    "let me know if you're interested",
    "hope this helps",
    "feel free to reach out",
    "don't hesitate to",
    "i'm confident",
    "you'll love",
    "proven",
    "trusted by",
]

def check_em_dashes(text: str) -> list:
    """Check for em dashes."""
    # Match em dash (—), en dash (–), or double hyphen (--)
    pattern = r'[\u2014\u2013--]'
    matches = re.findall(pattern, text)
    return matches

def check_bullets(text: str) -> list:
    """Check for bullet points."""
    lines = text.split('\n')
    bullet_lines = []
    for i, line in enumerate(lines, 1):
        # Match common bullet patterns
        if re.match(r'^[\s]*[-*•]\s+', line):
            bullet_lines.append((i, line.strip()))
    return bullet_lines

def check_banned_phrases(text: str) -> list:
    """Check for banned phrases (case-insensitive)."""
    text_lower = text.lower()
    found = []
    for phrase in BANNED_PHRASES:
        if phrase in text_lower:
            # Find position
            pos = text_lower.find(phrase)
            # Get context
            start = max(0, pos - 20)
            end = min(len(text), pos + len(phrase) + 20)
            context = text[start:end].replace('\n', ' ')
            found.append((phrase, context))
    return found

def check_word_count(text: str, max_words: int, label: str) -> bool:
    """Check if text is under word limit."""
    words = text.split()
    count = len(words)
    if count > max_words:
        print(f"  ⚠️  {label}: {count} words (max {max_words})")
        return False
    print(f"  ✓ {label}: {count} words")
    return True

def validate_draft(text: str, label: str = "Draft") -> bool:
    """Validate a single draft."""
    print(f"\nValidating: {label}")
    print("-" * 40)
    
    errors = []
    
    # Check em dashes
    em_dashes = check_em_dashes(text)
    if em_dashes:
        errors.append(f"Found {len(em_dashes)} em dash(es)")
        print(f"  ❌ Em dashes found: {len(em_dashes)}")
    
    # Check bullets
    bullets = check_bullets(text)
    if bullets:
        errors.append(f"Found {len(bullets)} bullet point(s)")
        print(f"  ❌ Bullets found: {len(bullets)}")
        for line_num, line in bullets:
            print(f"     Line {line_num}: {line[:50]}...")
    
    # Check banned phrases
    banned = check_banned_phrases(text)
    if banned:
        errors.append(f"Found {len(banned)} banned phrase(s)")
        print(f"  ❌ Banned phrases: {len(banned)}")
        for phrase, context in banned:
            print(f"     '{phrase}' in context: ...{context}...")
    
    if errors:
        print(f"\n  ❌ FAILED: {'; '.join(errors)}")
        return False
    else:
        print(f"\n  ✓ PASSED")
        return True

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_draft.py <draft_file>")
        print("Or pipe text via stdin: cat draft.txt | validate_draft.py -")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if file_path == "-":
        # Read from stdin
        text = sys.stdin.read()
        validate_draft(text, "Stdin input")
    else:
        # Read from file
        path = Path(file_path)
        if not path.exists():
            print(f"Error: File not found: {file_path}")
            sys.exit(1)
        
        text = path.read_text()
        validate_draft(text, path.name)

if __name__ == "__main__":
    main()
