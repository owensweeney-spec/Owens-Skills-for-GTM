---
name: breakup-email
description: Escribe un correo de despedida conciso y personalizado (80 palabras o menos) para un prospecto al que has estado contactando. Usa un archivo de memoria persistente para rastrear aprendizajes de correos anteriores. Incluye un gancho personalizado con inferencia profunda del perfil, y un CTA binario. Evita lenguaje corporativo, guiones largos y frases de IA. 100% código abierto, funciona con grandes empresas.
triggers:
  - "escribir correo de despedida"
  - "correo de despedida para prospecto"
  - "correo de último intento"
  - "correo de adiós a prospecto"
  - "correo para dejar de contactar"
  - "correo de seguimiento final"
  - "seguimiento sin respuesta"
  - "generar correo de despedida"
---

# Habilidad de Correo de Despedida

Escribe un correo de despedida a un prospecto cuando:
- El usuario ya ha enviado múltiples correos sin respuesta
- El usuario quiere terminar la conversación con gracia
- El correo debe tener menos de 80 palabras

## Sistema de Memoria

Antes de escribir cada correo:
1. Lee `/workspace/project/Owens-Skills-for-GTM/scripts/email_memory.json` para ver qué se ha aprendido de correos anteriores
2. Después de escribir, añade nuevos aprendizajes a ese archivo en el formato:
   ```json
   {
     "profile_hash": "identificador único para esta persona",
     "what_worked": "qué hizo efectivo este correo",
     "what_to_avoid": "qué no funcionó o se sintió genérico",
     "inference_used": "la percepción profunda sobre esta persona que hizo destacar este correo"
   }
   ```

## Requisitos de Entrada

El usuario proporcionará:
1. Perfil de LinkedIn (copiar/pegar) - extrae nombre, rol, empresa, intereses, antecedentes

Eso es todo. No pidas contexto de correos anteriores o menú de empresas. Infiere lo que necesitas de su perfil.

## Guías de Inferencia Profunda

Para cada prospecto, analiza su perfil para inferir:

**¿Qué te dice su actividad reciente/certificaciones sobre ellos?**
- Si obtuvieron una certificación recientemente: ¿Qué problema intentaban resolver? ¿Qué interés en herramientas podrían tener?
- Si publican sobre una conferencia: ¿En qué temas están enfocados? ¿Cuál es su punto de dolor?
- Si cambiaron de trabajo recientemente: ¿Cuál es su motivación? ¿Qué están construyendo?

**¿Qué objeciones podrían tener?**
- Líderes senior: Muy ocupados, ya tienen soluciones, necesitan prueba de ROI
- Ingenieros: Quieren profundidad técnica, les preocupa el vendor lock-in
- Gerentes: Preocupados por la adopción del equipo, necesitan justificarlo ante el liderazgo

**¿Qué los haría realmente responder?**
- Específico al contexto de su empresa
- Aborda un dolor que probablemente tienen
- No un genérico "charlemos" sino algo que muestre que hiciste tu tarea

### Ejemplos de Inferencia

| Señal del Perfil | Significado Inferido | Ángulo del Correo |
|----------------|-------------------|--------------|
| Certificación Claude Code | Ya usa herramientas de código con IA, le importa la experiencia del desarrollador | Menciona herramientas que se integran con su flujo de trabajo |
| Contratando equipo DevX | Le importa la productividad del desarrollador, conoce el dolor | Referencia otras empresas que mejoraron métricas DORA |
| Publica sobre QCon AI | Enfocado en gobernanza de IA, preocupaciones empresariales | Referencia implementaciones a escala empresarial |
| 20 años en la empresa | Valora estabilidad, lealtad | No vendas cambio disruptivo, vende mejora |
| Activo en comunidades tech | Adoptador temprano, abierto a nuevas herramientas | Puedes ser más directo, menos paternalista |
| Sin publicaciones recientes | Ocupado o contemplativo, difícil de alcanzar | Mantenlo más corto, menor compromiso |
| Promoción hace > 6 meses | Información vieja - no la menciones | Usa su permanencia actual o trabajo actual en su lugar |
| Contenido compartido en LinkedIn | Di "en LinkedIn" para que sepan dónde lo encontraste | Referencia el punto real que hicieron, no solo "vi tu publicación" |
| Larga permanencia en líder de industria (Bloomberg, etc.) | Ha visto tendencias ir y venir, escéptico del hype | No vendas disrupción, vende eficiencia. Conéctalo a su dominio específico. |
| C++ / enfocado en rendimiento | Le importa la corrección, no herramientas llamativas | Vende confiabilidad, no velocidad. Menciona "sin añadir riesgo". |
| Antecedentes en software financiero | Alto riesgo, no puede romper cosas | Vende "añadir capacidad sin añadir riesgo", "sistemas de producción" |
| Antecedentes de fundador de startup | Valora ROI, pragmático | Conéctalo a resultados, no características |
| Proyectos paralelos que se lanzan | Realmente construye cosas, no solo habla | Referencia el proyecto real, no su estatus general de "constructor" |
| Transición de empresa | Debe conectarse a POR QUÉ importa | No digas "salto interesante" - eso es relleno. Di qué revela sobre ellos. |

### Investigación sobre OpenHands (OBLIGATORIO ANTES DE IMPRIMIR)

Lo que OpenHands realmente hace:
- Agente de código con IA para tareas de ingeniería complejas
- SDK: biblioteca Python composable para definir agentes en código
- CLI: como Claude Code o Codex, impulsado por Claude, GPT, o cualquier LLM
- Cloud: alojado con integraciones de Slack, Jira, Linear
- Enterprise: auto-alojado en Kubernetes
- 100% código abierto, funciona con grandes empresas

Qué vender (específico a su contexto):
- DevSecOps: "automatizar correcciones de seguridad en código"
- Equipos de plataforma: "escalar a miles de agentes"
- Gerentes: "tu equipo diseña los agentes, nosotros proporcionamos la plataforma"
- Servicios financieros: "plataforma de agentes de código, aislada y en sandbox, diseñada por tu equipo y personalizada a tus preferencias de infraestructura"

### Mejores Ganchos
- Las preguntas funcionan mejor que las afirmaciones: "¿Cómo fue tu primer año como...?"
- "Me imagino..." enmarca suposiciones como especulación, no como hecho
- Si no tienes suficiente información para personalizar, NO LO HAGAS. Sé honesto.

**Verificación de voz:**
- ¿Pensaría ESTA persona "otro vendedor que no entiende" o "esta persona realmente entiende mi mundo"?
- Si suena como si pudiera ser una plantilla con el nombre intercambiado, REESCRIBE
- Elimina cualquier frase que podrías poner frente a CUALQUIER persona

## Por Qué Fallan los Correos Generados por IA (Basado en Investigación)

Un análisis de 2025 reveló que el 84% de los correos empresariales escritos por IA no obtienen respuesta. Razones clave:

**Frases de IA y clichés a evitar:**
- "Espero que este correo te encuentre bien"
- "Te estoy contactando para..."
- "No dudes en contactarme"
- "Solo chequeando"
- "Dando seguimiento a mi correo anterior"
- Estas señales inmediatamente indican automatización y se sienten insinceras

**Falta de personalización genuina:**
- Personalización profunda y significativa más allá de fusión de nombre
- Referencia algo específico que solo ELLOS entenderían

**Tono inflado e indirecto:**
- Oraciones verbosas que carecen de impacto
- Palabras de relleno y lenguaje "inflado"
- Sé conciso y directo

**Ausencia de emoción humana y contexto:**
- No puede replicar matices emocionales o historia compartida
- Los mensajes se sienten "transaccionales" y "enlatados"

**Sobreuso de estructura:**
- No dependas de viñetas y estructuras formulaicas
- Los flujos conversacionales naturales funcionan mejor

**Inexactitud y alucinación:**
- Nunca referencias algo que no viste realmente en su perfil
- Si no puedes verificarlo, no lo digas

**Cómo arreglarlo:**
- Usa IA como punto de partida, no producto final
- Reescribe en tu propia voz
- Añade contexto específico que solo esta persona reconocería

## Guías de Redacción

### Principio Central: A MEDIDA NO PLANTILLA
Cada correo debe ser único. Lee el perfil fresco. Escribe específicamente para esta persona.

### Estructura (en orden)
1. **Nombre + Gancho** - Comienza con su nombre, luego un fragmento que muestre que entiendes su mundo
2. **Qué es** - Nombra y describe directamente qué es OpenHands para ellos
3. **CTA** - Dos opciones claras

**Lección clave:** No separes el "contexto" (Te he contactado varias veces) como su propia línea. Combina todo en un flujo natural.

**Reglas de formato:**
- Sin guiones largos
- Sin frases de IA ("Espero que este correo te encuentre bien", "Te estoy contactando para...")
- Nombre, luego primera oración - no "Nombre - oración"

### Monitoreo de Producción (Opcional)

Si usas en producción, considera registrar:
- Qué ganchos funcionaron vs no funcionaron
- Tasas de respuesta por industria/rol
- Tiempo hasta la primera respuesta

Esto ayuda a iterar sobre la habilidad con el tiempo.

### Verificación de Perspectiva del Destinatario (OBLIGATORIO ANTES DE IMPRIMIR)

Antes de producir cualquier correo, pregúntate:
- ¿Abriría ESTA PERSONA esto? ¿O lo eliminarían pensando "pitch genérico"?
- ¿Referencié algo que realmente POSEEN, no solo algo en su perfil?
- Si referencio su contenido, ¿dije DÓNDE lo encontré?
- ¿Está el gancho conectado a lo que estoy vendiendo, o es un cumplido aleatorio?
- ¿Evité información vieja (promociones hace > 6 meses, certificaciones antiguas)?
- **¿Usé una plantilla y solo intercambié su nombre?** - Si es así, REESCRIBE
- **¿Es la propuesta de valor específica a su dominio?** - "enviar más rápido" no funciona para todos. Bloomberg = "añadir capacidad sin añadir riesgo". Salud = "moverse más rápido sin romper cumplimiento".
- **¿Este correo SOLO funcionaría para esta persona?** - Si puedes intercambiar el nombre y funciona para alguien más, no está suficientemente personalizado.

Si la respuesta a cualquiera de estas es "no", REESCRIBE antes de imprimir.

### Reglas Anti-Plantilla

NUNCA uses estas frases sin hacerlas específicas:
- ❌ "enviar código de calidad más rápido" → ✅ "añadir capacidad sin añadir riesgo" (para finanzas)
- ❌ "enviar más rápido" → ✅ "moverse más rápido sin romper cumplimiento" (para salud)
- ❌ "hacer más sin añadir personal" → ✅ específico a su dominio
- ❌ "acelerar desarrollo" → ✅ conectar a lo que realmente construyen

La propuesta de valor debe reescribirse para cada persona basado en:
- Su industria (finanzas = no puede romper cosas, salud = cumplimiento)
- Su rol (IC vs gerente vs ejecutivo)
- Los puntos de presión de su empresa (startup = velocidad, empresa = integración)

## Redacción desde Primeros Principios

Antes de escribir CUALQUIER correo, pregunta:

**¿Quién es esta persona, realmente?**
- ¿Qué los mantiene despiertos por la noche?
- ¿En qué han trabajado durante años que les importa?
- ¿Cuál es la ÚNICA cosa que querrían más si pudieran?
- ¿Cuál es la ÚNICA cosa que querrían evitar?

**¿Qué haría que ELLOS abran esto?**
- No qué haría que cualquiera lo abra
- ¿Qué haría que Gopi lo abra?
- ¿Qué haría que Nishtha lo abra?
- ¿Qué haría que Akshay lo abra?

**¿Cuál es su contexto?**
- Ingeniero de seguros: Los reclamos no pueden caerse, nunca
- Ingeniero de salud: Cumplimiento, pistas de auditoría
- Ingeniero de finanzas: Sistemas de trading de producción
- Ingeniero de Bloomberg: Sistemas de terminal que mueven mercados

**Cuando NO tienes señal (sin publicaciones, sin contenido):**
- Usa lo que sabes de su permanencia/rol
- Referencia su antecedente técnico si tienen uno
- No pretendas conocer sus desafíos - declara lo que SABES del perfil

Escribe el correo a ESTA persona, no a una persona.

### Reglas de Formato
- **Primera línea**: Nombre seguido de coma, luego la primera oración
  - ✅ "Rui," luego "Felicitaciones por la promoción..."
  - ❌ "Rui - Felicitaciones por la promoción..."
- **Sin guiones largos** - reemplaza con comas o puntos
- **80 palabras máximo** (estricto)

### Reglas
- **Sin lenguaje corporativo** - evita:
  - "comparar notas"
  - "tocar base"
  - "retomar"
  - "aprovechar"
  - "sinergia"
  - "avanzando"
  - "revisitar"
  - "conectar"
- **Lenguaje claro y directo** - escribe como una persona real
- **Ponte en los zapatos del receptor** - ¿abrirías esto? ¿Te molestaría?

### Ejemplos de CTA Binario
En lugar de "Avísame si te interesa" usa:
- "Si quieres hablar, estoy disponible jueves o viernes esta semana. Si no, sin presión."
- "Si esto todavía te interesa, avísame. Si no, dejaré de contactarte."
- Pon las opciones de CTA binario en líneas separadas para legibilidad

## Lista de Verificación de Autocrítica

Después de escribir, verifica cada elemento:
- [ ] ¿Menos de 80 palabras?
- [ ] ¿Contiene exactamente UN gancho personalizado que usa inferencia PROFUNDA (no superficial)?
- [ ] ¿El gancho explica POR QUÉ esto importa a ellos específicamente?
- [ ] ¿El gancho referencia algo que ellos POSEEN (no solo su título o empresa)?
- [ ] Si referencio su contenido, ¿dije DÓNDE (LinkedIn, publicación, etc.)?
- [ ] ¿Contiene exactamente UN CTA binario (dos opciones)?
- [ ] ¿Opciones de CTA binario en líneas separadas?
- [ ] ¿Menciona una empresa del menú que es RELEVANTE a su contexto?
- [ ] ¿Sin guiones largos?
- [ ] ¿El formato de la primera línea es "Nombre," no "Nombre -"?
- [ ] ¿Sin lenguaje corporativo (comparar notas, retomar, etc.)?
- [ ] ¿Se sentiría el receptor respetado, no manipulado?
- [ ] ¿Se lee como si un humano real lo escribió?
- [ ] ¿Esto solo podría aplicar a ESTA persona, o podría intercambiarse con cualquiera?
- [ ] ¿Aborda una objeción o preocupación probable que podrían tener?
- [ ] ¿Hice la verificación de perspectiva del destinatario antes de imprimir?

## Formato de Salida

Proporciona el correo en este formato:

```
Asunto: [Línea de asunto breve]

[Cuerpo del correo - 80 palabras máximo]

---
Autocrítica:
[Qué funcionó, qué no, qué mejorar para la próxima vez - sé honesto sobre las debilidades]
```

## Ejemplo

Entrada del Usuario:
- LinkedIn: "Sarah Chen - VP de Ventas en TechCorp - previamente en Salesforce - muy activa corriendo maratones"
- Correos previos: 3 seguimientos sobre programar una demo
- Empresa a mencionar: Okta

Salida:
```
Asunto: Pregunta rápida

Sarah, vi que estás entrenando para el Maratón de Boston. Impresionante.

Te he contactado varias veces sobre programar una demo pero no he recibido respuesta. Entiendo totalmente lo ocupadas que se ponen las cosas.

Hemos ayudado a equipos similares en empresas como Okta a optimizar sus ops de ventas. Si eso suena útil, encantado de charlar. Si no, dejaré de molestarte.

Saludos,
[Tu nombre]

---
Autocrítica: El gancho (entrenamiento de maratón) es específico a ella. El CTA binario da dos caminos claros. La referencia a la empresa (Okta) es relevante. Menos de 80 palabras. Sin lenguaje corporativo. Directo pero no agresivo. Podría mejorarse referenciando algo sobre su rol de VP y con qué luchan los equipos de ventas - el maratón es superficial, ¿qué le importa realmente en su rol actual?
```