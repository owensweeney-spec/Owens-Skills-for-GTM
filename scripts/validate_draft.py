#!/usr/bin/env python3
"""
Script de validación para la habilidad human_outreach_drafts.
Aplica: sin guiones largos, sin viñetas, sin frases prohibidas.
"""

import re
import sys
from pathlib import Path

# Frases prohibidas (sin distinción de mayúsculas/minúsculas)
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
    """Verifica guiones largos."""
    # Busca guion largo (—), guion medio (–), o guion doble (--)
    pattern = r'[\u2014\u2013--]'
    matches = re.findall(pattern, text)
    return matches

def check_bullets(text: str) -> list:
    """Verifica viñetas."""
    lines = text.split('\n')
    bullet_lines = []
    for i, line in enumerate(lines, 1):
        # Busca patrones comunes de viñetas
        if re.match(r'^[\s]*[-*•]\s+', line):
            bullet_lines.append((i, line.strip()))
    return bullet_lines

def check_banned_phrases(text: str) -> list:
    """Verifica frases prohibidas (sin distinción de mayúsculas/minúsculas)."""
    text_lower = text.lower()
    found = []
    for phrase in BANNED_PHRASES:
        if phrase in text_lower:
            # Encuentra posición
            pos = text_lower.find(phrase)
            # Obtiene contexto
            start = max(0, pos - 20)
            end = min(len(text), pos + len(phrase) + 20)
            context = text[start:end].replace('\n', ' ')
            found.append((phrase, context))
    return found

def check_word_count(text: str, max_words: int, label: str) -> bool:
    """Verifica si el texto está bajo el límite de palabras."""
    words = text.split()
    count = len(words)
    if count > max_words:
        print(f"  ⚠️  {label}: {count} palabras (máx {max_words})")
        return False
    print(f"  ✓ {label}: {count} palabras")
    return True

def validate_draft(text: str, label: str = "Borrador") -> bool:
    """Valida un solo borrador."""
    print(f"\nValidando: {label}")
    print("-" * 40)
    
    errors = []
    
    # Verifica guiones largos
    em_dashes = check_em_dashes(text)
    if em_dashes:
        errors.append(f"Se encontraron {len(em_dashes)} guion(es) largo(s)")
        print(f"  ❌ Guiones largos encontrados: {len(em_dashes)}")
    
    # Verifica viñetas
    bullets = check_bullets(text)
    if bullets:
        errors.append(f"Se encontraron {len(bullets)} viñeta(s)")
        print(f"  ❌ Viñetas encontradas: {len(bullets)}")
        for line_num, line in bullets:
            print(f"     Línea {line_num}: {line[:50]}...")
    
    # Verifica frases prohibidas
    banned = check_banned_phrases(text)
    if banned:
        errors.append(f"Se encontraron {len(banned)} frase(s) prohibida(s)")
        print(f"  ❌ Frases prohibidas: {len(banned)}")
        for phrase, context in banned:
            print(f"     '{phrase}' en contexto: ...{context}...")
    
    if errors:
        print(f"\n  ❌ FALLÓ: {'; '.join(errors)}")
        return False
    else:
        print(f"\n  ✓ PASÓ")
        return True

def main():
    if len(sys.argv) < 2:
        print("Uso: validate_draft.py <archivo_borrador>")
        print("O envía texto vía stdin: cat borrador.txt | validate_draft.py -")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if file_path == "-":
        # Lee desde stdin
        text = sys.stdin.read()
        validate_draft(text, "Entrada de stdin")
    else:
        # Lee desde archivo
        path = Path(file_path)
        if not path.exists():
            print(f"Error: Archivo no encontrado: {file_path}")
            sys.exit(1)
        
        text = path.read_text()
        validate_draft(text, path.name)

if __name__ == "__main__":
    main()
