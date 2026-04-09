---
name: human_outreach_drafts
description: Esta habilidad debe usarse cuando el usuario pida "redactar un DM de LinkedIn", "escribir un correo de prospección", "crear un mensaje de ventas", "escribir un correo en frío", o "componer un mensaje para un prospecto". Crea borradores de prospección que suenan humanos, optimizados para móvil, con patrones de tiempo verbal específicos y sugerencias de pilotos.
---

# Borradores de Prospección Humana

Redacta DMs de LinkedIn y correos cortos que suenen humanos, adaptados al perfil específico de una persona, con una pequeña sugerencia de piloto de bajo riesgo y una respuesta clara y fácil.

## Entradas

- Resumen del perfil del prospecto (rol, empresa, stack tecnológico, actividad reciente)
- Resumen del producto (1-2 oraciones)
- Restricciones (longitud, tono, frases prohibidas, tiempos verbales preferidos)
- Notas de retroalimentación de iteraciones pasadas

## Salidas

- Borrador de correo (optimizado para móvil, ~110 palabras máximo)
- Borrador de DM de LinkedIn (~75 palabras máximo)
- Sugerencia de asunto de una línea (opcional)
- Resumen de "Por qué funciona" (1-2 oraciones, solo uso interno)

## Instrucciones Principales

Escribe como un representante de ventas humano dirigiéndose a una persona específica. Usa su rol, stack tecnológico y actividad reciente para elegir un piloto pequeño y de bajo riesgo. Mantén todo corto y natural.

### Patrones de Tiempo Verbal Requeridos

- **Observación pasada**: "Vi tu publicación sobre…"
- **Justificación presente**: "Como estás enfocado en…"
- **Sugerencia condicional**: "Una buena primera cosa para probar podría ser…"
- **Futuro modal**: "Podrías tenerlo…"
- **Presente habitual**: "Esto normalmente toma 1-2 horas…"

Termina con una pregunta simple y sin presión.

### Reglas Estrictas

- Sin viñetas
- Sin guiones largos
- Sin frases "de IA": "seré breve," "si te resulta útil," "encantado de," "solo"
- Evita jerga corporativa: "optimizar," "aprovechar," "sinergia"
- Evita repetir el nombre del producto más de una vez

### Reglas Flexibles

- Una idea de piloto concreta vinculada a su rol y stack
- Haz explícita la conexión con su mundo en una cláusula
- Mantén el correo en ~110 palabras, LinkedIn en ~75 palabras
- Evita explicar demasiado el producto

## Biblioteca de Ideas de Pilotos

Selecciona el piloto más pequeño que coincida con su mundo:

- Lista de verificación de preparación para lanzamiento
- Traspaso de incidentes / captura de runbooks
- Preparación de repositorios / lista de verificación de onboarding
- Flujo de trabajo de calidad o validación de datos
- Lista de verificación de preparación para migración

## Verificaciones de Calidad

Antes de producir el resultado, verifica:

- La primera oración hace referencia a su contexto
- La idea de piloto se alinea con su stack o responsabilidades
- Existe una sola pregunta clara
- Se lee naturalmente en voz alta
- No hay frases prohibidas presentes
- No hay simetría ni relleno "de IA"

## Mejora Continua

Después de cada edición del usuario:
1. Captura la edición y clasifica por qué fue mejor (tono, longitud, especificidad, redacción, estructura)
2. Actualiza la lista de memoria "Hacer / No hacer"
3. Añade o elimina frases de la lista de prohibidas
4. Rastrea las respuestas exitosas y alimenta las aperturas/cierres en plantillas
5. Mantén el patrón de tiempo verbal preferido y aplícalo en futuros borradores

## Datos a Almacenar

Mantén una memoria ligera de:
- Frases preferidas (qué mantener)
- Frases rechazadas (qué eliminar)
- Objetivos de conteo de palabras
- Top 3 ideas de pilotos que obtienen respuestas
- Etiquetas de tono: directo, neutral, cálido, pragmático

## Archivos de Referencia

- `references/pilot_ideas.md` - Descripciones detalladas de ideas de pilotos y cuándo usar cada una
- `references/tense_patterns.md` - Ejemplos de cada patrón de tiempo verbal en contexto
- `references/banned_phrases.md` - Lista completa de frases a evitar
