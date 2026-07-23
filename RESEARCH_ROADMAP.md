# RESEARCH_ROADMAP.md — Huella Social

> Agenda de investigación del proyecto. Define el estado actual, los milestones próximos, la estrategia ANID y las líneas de investigación abiertas. Debe actualizarse con cada avance relevante.

---

## Estado actual del proyecto (julio 2026)

| Dimensión | Estado |
|-----------|--------|
| **TRL de la plataforma** | 3 — Prototipo funcional (Shiny R) |
| **Postulaciones ANID** | 3 rechazos consecutivos (2024, 2025, 2026) |
| **Outputs científicos** | 1 memoria de título completada (Ureta & Ruiz Tagle, 2026) |
| **Papers publicados** | 0 |
| **Pipeline de datos documentado** | Parcial — metodología en tesis, sin pipeline reproducible público |
| **Cobertura metodológica** | Cooperativas de ahorro y crédito (caso piloto) |
| **Red institucional** | CONFECOOP, F. Rodelillo, INAC, CIESCOOP, CPP UC, U. Chile |

---

## Diagnóstico estratégico

### Por qué ANID no ha adjudicado (síntesis de 3 evaluaciones)

El equipo y el presupuesto son evaluados bien (4,0–4,5/5). El problema está en el **capítulo científico** (siempre ≤ 2,7/5). Los evaluadores han señalado de manera consistente:

1. El problema se describe cualitativamente pero no se cuantifica su magnitud
2. El estado del arte no diferencia la solución de plataformas existentes (BIPS, soluciones internacionales)
3. La metodología carece de diseño experimental y métricas de efectividad de la plataforma
4. El modelo de gobernanza del observatorio no está especificado
5. Los hitos no tienen indicadores de logro vinculados a umbrales TRL

### Qué cambió positivamente en 2026

- Se incorporó el módulo de cuentas satélite (fundamentado en la tesis)
- Se sumó la Universidad de Chile como co-beneficiaria
- Se mejoró la red de socios (CONFECOOP, INAC, CIESCOOP)
- Se declaró un prototipo funcional TRL 3 con evidencia verificable
- Se mencionaron explícitamente DEA y SFA como metodologías de eficiencia
- Se incorporó el marco de la Resolución ONU 77/281 (2023)

---

## Milestones 2026–2027

### M1 — Artículo científico desde tesis (prioridad ALTA)
**Objetivo**: Convertir Ureta & Ruiz Tagle (2026) en un paper enviable a revista Q1/Q2.

**Contenido**: Metodología de cuentas satélite para cooperativas de ahorro y crédito en Chile. Resultado principal: contribución al PIB entre **0,07 % y 0,12 %** (segmento CMF) y entre 0,001 % y 0,011 % (segmento DAES, cota inferior por cobertura parcial). Cifras verificadas en auditoría interna (julio 2026); la versión anterior "0,04 %–0,08 %" era incorrecta.

**Revistas objetivo** (en orden de prioridad):
- *Annals of Public and Cooperative Economics* (Wiley, Q2, ISSN 0003-5092)
- *VOLUNTAS: International Journal of Voluntary and Nonprofit Organizations* (Springer, Q1)
- *Latin American Economic Review* (Springer, Q1 en LatAm)
- *Journal of Business Research* (Elsevier, Q1) — si se enfatiza el ángulo de información
- *El Trimestre Económico* (FCE, Q2 iberoamericano)

**Tareas**:
- [ ] Adaptar estructura de la memoria al formato IMRAD
- [ ] Revisar revisión de literatura para cobertura internacional
- [ ] Preparar tablas y figuras en formato publicación
- [ ] Seleccionar revista y revisar submission guidelines
- [ ] Envío al co-director para revisión
- [ ] Envío a revista

**Plazo estimado**: Q4 2026

---

### M2 — Pipeline computacional reproducible (prioridad ALTA)
**Objetivo**: Publicar en el repositorio el código completo y documentado de la metodología de cuentas satélite, con datos de ejemplo públicos, tests unitarios y documentación Quarto.

**Relevancia para ANID**: Convierte el TRL 3 frágil en un TRL 3 demostrable y auditable. Es un resultado técnico citeable en la próxima postulación.

**Tareas**:
- [ ] Limpiar y documentar el código de la tesis (R)
- [ ] Crear dataset de ejemplo con datos públicos (SII, DAES)
- [ ] Escribir tests con `testthat`
- [ ] Documentar con Quarto (notebook reproducible)
- [ ] Publicar en el repositorio bajo licencia abierta (MIT o CC-BY)
- [ ] Agregar DOI vía Zenodo

**Plazo estimado**: Q4 2026

---

### M3 — Landscape analysis de plataformas comparables (prioridad ALTA)
**Objetivo**: Producir un working paper o reporte técnico que mapee sistemáticamente las plataformas existentes de datos para la ESS nacional e internacionalmente, diferenciando a Huella Social.

**Plataformas a cubrir** (mínimo):
- BIPS — Banco Integrado de Programas Sociales (Chile, Estado)
- GuideStar / Candid (EEUU)
- ImpactMatters (EEUU)
- B Analytics / B Impact Assessment (Global)
- IRIS+ (Global Impact Investing Network)
- European Social Economy Satellite Accounts — CIRIEC
- SEDESOL / plataformas equivalentes (México, Argentina, Brasil)
- Open Corporates (global, datos abiertos)

**Dimensiones de análisis**: cobertura geográfica, tipo de organización, fuentes de datos, indicadores, modelo de negocio, acceso, limitaciones.

**Relevancia para ANID**: Resuelve directamente la crítica recurrente sobre el estado del arte débil.

**Plazo estimado**: Q1 2027

---

### M4 — Protocolo de evaluación de impacto de la plataforma (prioridad MEDIA)
**Objetivo**: Diseñar y documentar el protocolo metodológico para evaluar si Huella Social mejora la toma de decisiones de asignación de recursos en OSC.

**Diseño propuesto**: Diferencia en diferencias (DiD) con grupo de control construido por propensity score matching. Variables de resultado: calidad de reportes financieros, diversificación de financiamiento, tiempo de búsqueda de fondos.

**Relevancia para ANID**: Responde directamente a la crítica de falta de diseño experimental.

**Plazo estimado**: Q1 2027 (antes de envío ID27)

---

### M5 — Extensión metodológica a fundaciones y ONG (prioridad MEDIA)
**Objetivo**: Nuevo trabajo de memoria que extiende la metodología de cuentas satélite de cooperativas a fundaciones y ONG.

**Dependencia**: Requiere tener el pipeline del M2 publicado y documentado.

**Relevancia para ANID**: Amplía la cobertura del caso piloto, fortalece la generalización de la metodología.

**Plazo estimado**: Inicio Q1 2027, entrega Q2 2027

---

### M6 — Gobernanza del observatorio: modelo documentado (prioridad MEDIA)
**Objetivo**: Redactar un documento de arquitectura de gobernanza del observatorio Huella Social: quién actualiza los datos, cómo se incorporan nuevas organizaciones, qué proceso de curación de calidad existe, quién valida los indicadores.

**Inspiración**: Modelo Our World in Data (editorial), Open Corporates (curación comunitaria), BIPS (gobernanza estatal).

**Relevancia para ANID**: Responde directamente a la crítica recurrente sobre gobernanza no especificada.

**Plazo estimado**: Q1 2027

---

### M7 — Migración del prototipo a React + API (prioridad MEDIA)
**Objetivo**: Migrar el demo en Shiny R a una aplicación web en React con backend API, documentando el salto TRL 3→5 con métricas formales de usabilidad y rendimiento.

**Hitos técnicos internos**:
- [ ] Especificación de la API (endpoints, formatos)
- [ ] Backend: diseño de base de datos y endpoints de datos
- [ ] Frontend: migración de visualizaciones a React
- [ ] Pruebas con al menos 5 organizaciones piloto
- [ ] Documentación técnica (README, OpenAPI spec)

**Plazo estimado**: Q2–Q3 2027

---

### M8 — Postulación IDeA I+D 2027 (prioridad CRÍTICA)
**Objetivo**: Postular al concurso IDeA I+D 2027 con una formulación que resuelva todos los puntos de rechazo históricos.

**Requisitos para postular**:
- M1 en preparación activa (paper en proceso o enviado) → evidencia de producción científica
- M2 completado → TRL 3 demostrable con pipeline público
- M3 completado → estado del arte sólido con diferenciación clara
- M4 en borrador → diseño experimental especificado
- M6 en borrador → gobernanza del observatorio especificada

**Cambios estratégicos recomendados para ID27**:
1. Abrir la sección 1.1 con el dato empírico de la tesis (CMF: 0,07–0,12 % PIB; promedio ~0,08–0,09 %) como cuantificación del problema, antes de cualquier argumento cualitativo. Usar la formulación: "Las cooperativas de ahorro y crédito chilenas contribuyen entre 0,07 % y 0,12 % del PIB nacional —estadísticamente invisibles en el SCN— a pesar de representar el 2,41 % del patrimonio del sistema financiero cooperativo y bancario (CMF, 2025)."
2. Incluir una tabla explícita de comparación con BIPS y plataformas internacionales (salida del M3)
3. Añadir sección de "Validación de la plataforma" con el protocolo DiD (salida del M4)
4. Añadir sección de "Modelo de gobernanza" (salida del M6)
5. Definir indicadores de logro por hito vinculados a umbrales TRL (TRL 3→4→5) con métricas específicas
6. Considerar postular en inglés para ampliar el pool de evaluadores internacionales
7. Evaluar si incluir a un economista de datos / experto en interoperabilidad técnica como investigador asociado

**Plazo de postulación**: típicamente marzo–abril 2027 (verificar bases ANID)

---

## Líneas de investigación abiertas

Estas son áreas que no están en el plan actual pero que el proyecto debería explorar:

### Línea 1 — Economía política de la transparencia en OSC
¿Por qué las OSC no reportan voluntariamente? ¿Qué incentivos cambiarían ese equilibrio? Ángulo de teoría de juegos / diseño de mecanismos. Potencial paper teórico.

### Línea 2 — Eficiencia de la distribución de donaciones en Chile
Aplicación de DEA a los datos de donaciones de la Ley 19.826 para evaluar si la concentración de donaciones en pocas organizaciones es eficiente o refleja asimetrías de información. Requiere datos del repositorio `donaciones`.

### Línea 3 — Impacto de la Ley 21.440 en la transparencia del sector
La ley de transparencia de ONG (2022) crea un shock de política pública. ¿Cambió el comportamiento de reporte? Diseño DiD antes/después.

### Línea 4 — Extensión a economía social latinoamericana
La metodología de cuentas satélite podría replicarse en Argentina, México o Brasil usando sus registros administrativos equivalentes. Potencial colaboración internacional y paper comparado.

---

## Criterios de priorización

Al decidir qué hacer primero, usar este orden de criterios:

1. **¿Resuelve una crítica ANID documentada?** → máxima prioridad
2. **¿Produce un output científico publicable?** → alta prioridad
3. **¿Fortalece la reproducibilidad del trabajo existente?** → alta prioridad
4. **¿Amplía la cobertura metodológica del proyecto?** → prioridad media
5. **¿Abre una línea de investigación nueva?** → baja prioridad si hay deuda técnica pendiente

---

## Log de cambios al roadmap

| Fecha | Cambio | Razón |
|-------|--------|-------|
| Julio 2026 | Creación inicial del roadmap | Primer ingreso de documentos al proyecto |
| Julio 2026 | Corrección de cifra de aporte al PIB: de "0,04–0,08 %" a "0,07–0,12 % (CMF)" | Auditoría interna de la tesis (docs/auditoria/01_consistencia_interna.md) confirmó que el rango correcto del segmento CMF es 0,07–0,12 %. La cifra anterior no correspondía a ningún valor reportado en la memoria. |
| Julio 2026 | Auditoría completa de Ureta & Ruiz Tagle (2026) completada — Fases 0, 1, 4, 5, 6 | Se identificó un error aritmético verificado (H-01, Cuadro 5.7 fila 2025) y se generó lista de solicitudes a autores para desbloquear Fases 2–3. Ver `docs/auditoria/`. |

---

*Última actualización: julio 2026. Mantener este documento vivo: cada nuevo output, cambio de prioridad o nueva evidencia debe reflejarse aquí.*
