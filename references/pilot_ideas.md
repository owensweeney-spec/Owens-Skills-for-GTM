# Biblioteca de Ideas de Pilotos

Descripciones detalladas de ideas de pilotos y cuándo usar cada una basándose en el contexto del prospecto.

## Lista de Verificación de Preparación para Lanzamiento

**Mejor para**: Gerentes de ingeniería, líderes técnicos, gerentes de lanzamiento
**Señales de stack**: CI/CD, pipelines de despliegue, procesos de lanzamiento
**Descripción**: Una lista de verificación enfocada para verificar que el código está listo para producción—cubre pruebas, docs, configs y rollbacks

**Gancho de ejemplo**: "Como estás lanzando semanalmente, una lista de verificación de preparación de lanzamiento podría reducir tu tasa de rollback"

## Traspaso de Incidentes / Captura de Runbooks

**Mejor para**: SREs, ingenieros DevOps, equipos de plataforma
**Señales de stack**: Gestión de incidentes, guardia, herramientas de observabilidad
**Descripción**: Documenta el conocimiento institucional sobre respuesta a incidentes para que los traspasos sean fluidos

**Gancho de ejemplo**: "Vi tu publicación sobre guardia—capturar runbooks podría hacer tu próximo traspaso mucho más fácil"

## Preparación de Repositorios / Lista de Verificación de Onboarding

**Mejor para**: Gerentes de ingeniería, líderes de equipo, experiencia del desarrollador
**Señales de stack**: GitHub, GitLab, base de código, onboarding de nuevos empleados
**Descripción**: Una lista de verificación para asegurar que cada nuevo repo tiene lo que los desarrolladores necesitan para contribuir rápido

**Gancho de ejemplo**: "Como estás creciendo el equipo, una lista de verificación de preparación de repo podría acelerar el onboarding"

## Flujo de Trabajo de Calidad o Validación de Datos

**Mejor para**: Ingenieros de datos, analistas, QA
**Señales de stack**: Pipelines de datos, ETL, bases de datos, Great Expectations, dbt
**Descripción**: Un flujo de trabajo para atrapar datos malos antes de que se propaguen por tu sistema

**Gancho de ejemplo**: "Como estás lidiando con pipelines de datos, un flujo de trabajo de validación podría atrapar problemas temprano"

## Lista de Verificación de Preparación para Migración

**Mejor para**: Líderes técnicos, arquitectos, ingenieros de plataforma
**Señales de stack**: Sistemas legacy, migración a la nube, refactors mayores
**Descripción**: Una lista de verificación enfocada para evaluar preparación antes de una gran migración

**Gancho de ejemplo**: "Una lista de verificación de preparación de migración podría ayudarte a detectar vacíos antes de empezar"

## Guía de Selección

Elige el piloto más **pequeño** que se conecte con su rol:

1. ¿Son dueños de lanzamientos? → Lista de verificación de preparación para lanzamiento
2. ¿Manejan incidentes? → Captura de runbooks
3. ¿Están incorporando personas? → Lista de verificación de onboarding
4. ¿Trabajan con datos? → Flujo de trabajo de validación
5. ¿Están planeando una migración? → Preparación de migración

Mantenlo de bajo riesgo y vinculado a algo que ya les importa.
