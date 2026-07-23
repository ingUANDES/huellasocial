# FASE 4 — Evaluación según rúbrica de titulación UANDES
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha de auditoría:** julio 2026  
**Insumo:** PDF únicamente. Los puntajes de los indicadores 4 y 5 podrían ajustarse una vez completadas las Fases 2–3.  
**Postura:** evaluador externo exigente (AUDIT_PROTOCOL §0).

> **Aviso:** La conversión de puntaje ponderado a nota UANDES debe confirmarse con el guía antes de comunicar cualquier nota a los alumnos. Este documento reporta el puntaje en la escala 0–5 de la rúbrica, no la nota final.

---

## Resumen de puntajes

| # | Indicador | Peso | Puntaje (0–5) | Contribución ponderada |
|---|-----------|------|---------------|----------------------|
| 1 | Presentación y expresión escrita | 10 % | 4,0 | 0,40 |
| 2 | Resumen | 5 % | 3,5 | 0,175 |
| 3 | Introducción y motivación | 15 % | 5,0 | 0,75 |
| 4 | Desarrollo | 20 % | 4,0 | 0,80 |
| 5 | Análisis y conclusiones | 30 % | 3,5 | 1,05 |
| 6 | Referencias | 5 % | 4,5 | 0,225 |
| 7 | Relevancia, alcance y novedad | 15 % | 5,0 | 0,75 |
| — | **Total** | **100 %** | — | **4,15 / 5,00** |

---

## Indicador 1 — Presentación y expresión escrita (10 %)

**Puntaje asignado: 4,0 / 5**

**Fortalezas:**
- Documento compilado en LaTeX con tipografía uniforme y sin errores de compilación aparentes.
- Figuras 5.1 y 5.2 son informativas; combinan series de VAB y aporte al PIB en un solo eje dual.
- Longitud apropiada (~95 páginas de contenido + Anexos); no hay relleno evidente.
- Terminología económica consistente a lo largo del documento (P1, B1g, D1 usados con precisión).

**Debilidades:**
- H-01, H-03, H-04, H-05, H-07: cinco inconsistencias en valores numéricos entre secciones, detectables visualmente. Una comisión atenta las nota.
- La columna N del Cuadro 5.8 está mal actualizada para 11 años (H-04), lo que introduce ruido en una tabla de presentación directa.
- Los decimales son inconsistentes entre tablas (P1 en Cuadro 5.5 usa un decimal; en Cuadro 5.7, también un decimal, pero las diferencias entre celdas revelan el error).

**Justificación del nivel:** La memoria tiene presentación sólida (nivel 3→5), pero los errores numéricos detectables en tablas de resultados la alejan del 5. Un evaluador que calcule cualquier subtotal en el Cuadro 5.7 encontrará el error de la fila 2025.

---

## Indicador 2 — Resumen (5 %)

**Puntaje asignado: 3,5 / 5**

**Fortalezas:**
- El resumen cubre motivación, metodología y resultado principal.
- Está bien escrito; una frase por tema, sin jerga innecesaria.
- Menciona los tres marcos metodológicos (SCN 2025, ONU-TSE, CIRIEC).

**Debilidades:**
- H-08: La cifra "0,08 % del PIB nacional" en el abstract es una descripción del segmento CMF, sin indicar que el segmento DAES es marginal y que el rango correcto para el sector completo es 0,07–0,12 %. Un lector del abstract que no lea el cuerpo queda con una impresión imprecisa del resultado.
- No menciona que las Fases 2 y 3 del análisis (reproducibilidad) dependen de datos no versionados, ni que el resultado principal depende de un supuesto clave (α).

**Justificación del nivel:** Cumple los tres elementos requeridos (motivación / trabajo / resultados) pero la cifra principal está presentada sin el contexto necesario para interpretarla correctamente.

---

## Indicador 3 — Introducción y motivación (15 %)

**Puntaje asignado: 5,0 / 5**

**Fortalezas:**
- El problema de invisibilidad estadística de las CAC está bien planteado y motivado institucionalmente (DFL N°5/2003 como causa de la brecha de información).
- Los objetivos (general y 4 específicos en §1.2) son claros, medibles y coherentes entre sí.
- El alcance (§1.3) delimita con precisión las CAC chilenas (DAES + CMF, 2014–2025) y excluye explícitamente otras cooperativas y otros tipos de ESS.
- El alcance coincide con lo realizado: el capítulo 5 cubre exactamente las CAC DAES (2014–2024) y CMF (2013–2025).
- La conexión con el proyecto Huella Social y la postulación FONDEF está documentada sin desviar el foco de la memoria.

**Justificación del nivel:** Nivel 5 pleno. No se detectan brechas entre lo prometido y lo entregado.

---

## Indicador 4 — Desarrollo (20 %)

**Puntaje asignado: 4,0 / 5**

**Fortalezas:**
- El capítulo metodológico (Cap. 4) es el más sólido de la memoria. La estrategia de estimación en tres pasos (identificación, integración, cálculo) es clara y lógicamente secuenciada.
- La operacionalización de variables del SCN (§4.3.2) identifica el proxy correcto para cada cuenta (P1, P2, B1g, D1, B2g) con justificación normativa referenciada.
- El Cuadro 4.6 (variables no construibles) es una contribución metodológica real: sistematiza las brechas de información con razonamiento institucional específico para Chile.
- El dashboard (§4.4) constituye un entregable tecnológico concreto que va más allá de lo habitual en memorias de este tipo.
- La comparación con las experiencias de España, Portugal y Polonia (§2.2.2) es relevante y muestra dominio del estado del arte internacional.

**Debilidades:**
- H-06: El supuesto 1 en §4.3.4 ("tramo de ventas del SII...") contradice la metodología real descrita en §4.3.2. Eso es precisamente el tipo de inconsistencia que una comisión que lee los supuestos contra la metodología va a señalar.
- H-02: La reproducibilidad del desarrollo metodológico es nula sin los datos y el código. El pipeline se describe pero no se puede auditar.
- La sección de estadística descriptiva (§4.2.2, Cuadro 4.2) no incluye el período completo por variable: presenta media, mediana y SD globales pero no por año, lo que impide apreciar la evolución temporal de la dispersión.

**Justificación del nivel:** La memoria alcanza el nivel 4 (tareas correctas, material insuficiente para comprenderlas a cabalidad). Alcanzaría el 5 si el código estuviera versionado y el supuesto erróneo fuera corregido.

---

## Indicador 5 — Análisis y conclusiones (30 %)

**Puntaje asignado: 3,5 / 5**

**Fortalezas:**
- El análisis de resultados (Cap. 5) combina dos dimensiones legítimas: temporal (evolución del VAB) y sectorial (segmentos CMF vs DAES).
- La validación externa (§5.3.3) es la fortaleza más notable del trabajo. Implementa una triangulación entre la estimación propia y una estimación independiente basada en participación patrimonial × PIB servicios financieros. Esta práctica es inusual en memorias de este tipo y directamente responde a una crítica del evaluador FONDEF.
- Las limitaciones (§5.5) son explícitas, completas y metodológicamente honestas. Los cuatro puntos están bien argumentados.
- Las conclusiones (§6.2) son proporcionales a la evidencia: no sobre-afirman causalidad ni generalizan más allá del caso piloto CAC.
- La cuantificación del aporte (0,07–0,12 % PIB) y el orden de magnitud (coherente con 2,41 % de patrimonio en el sistema) es un resultado empírico concreto y novedoso.

**Debilidades:**
- H-01: La fila 2025 del Cuadro 5.7 contiene un error aritmético verificable, lo que afecta directamente los resultados presentados en el capítulo de análisis. Una comisión que haga el cálculo lo detectará.
- Ausencia de análisis de sensibilidad. Dado que α = 0,3776 es el parámetro central del modelo y se reconoce heterogeneidad (fn. 3), la memoria debería mostrar cómo cambia el resultado principal con α = 0,28 (Coopeuch-like) y α = 0,50 (más conservador). Este análisis de robustez es estándar en cuentas satélite internacionales.
- No se calcula el intervalo de confianza ni el rango de incertidumbre de la estimación, lo cual es aceptable para una metodología de cuentas satélite pero deja la cifra puntual (0,08 %) sin cuantificación de la incertidumbre.
- H-03: Tres cifras inconsistentes para el número de observaciones. Una comisión exigente pedirá que se explique la diferencia.

**Justificación del nivel:** La memoria está entre nivel 3 y nivel 4. El mérito del análisis (validación externa, limitaciones explícitas, proporcionalidad de conclusiones) la acerca al 4. El error en Cuadro 5.7, la ausencia de análisis de sensibilidad y las inconsistencias de N la mantienen en 3,5.

---

## Indicador 6 — Referencias (5 %)

**Puntaje asignado: 4,5 / 5**

**Fortalezas:**
- Las referencias primarias son de alta calidad: SCN 2025 (UN), Manual ONU-TSE 2018 (UN), Manual CIRIEC (Barea Tejeiro & Monzón Campos, 2007), Statistics Poland (2021).
- Las fuentes institucionales chilenas están correctamente citadas (BCCh, CMF, DAES, SII).
- El formato de cita es consistente con el estilo autor-año a lo largo del documento.
- La bibliografía cubre experiencias internacionales relevantes: España (Monzón), Portugal (Pedroso et al. 2023), Polonia (Statistics Poland 2021), México (CIRIEC-México & CIDE, 2022).

**Debilidades menores:**
- Akerlof (1970) se menciona en §3.4 pero no aparece en las referencias. Si se cita en el texto, debe estar en la bibliografía.
- Algunas fuentes de datos del Banco Central (la cita "Banco Central de Chile, 2026" del Cuadro 5.9) no especifican la tabla o el dataset exacto descargado. Para reproducibilidad, la referencia debería incluir la URL permanente y la fecha de acceso.

**Justificación del nivel:** Alta calidad general; las debilidades son menores pero notorias para un evaluador que intente rastrear los datos.

---

## Indicador 7 — Relevancia, alcance y novedad (15 %)

**Puntaje asignado: 5,0 / 5**

**Fortalezas:**
- **Primero en su clase en Chile:** La memoria es, hasta donde el equipo de investigación puede verificar, la primera estimación sistemática y documentada de la contribución al PIB de las CAC chilenas usando cuentas satélite bajo estándares internacionales.
- **Novedad metodológica para el contexto chileno:** La combinación de tres fuentes (DAES, CMF-BEST, SII) mediante RUT como llave de cruce, con justificación institucional específica para la realidad regulatoria chilena (DFL N°5/2003), es un aporte original y no una mera aplicación mecánica de manuales internacionales.
- **Alineamiento estratégico:** El trabajo alimenta directamente la próxima postulación ANID IDeA I+D (M8 del RESEARCH_ROADMAP.md), proporcionando el dato empírico cuantificado que los tres evaluadores anteriores señalaron como ausente.
- **Extensibilidad:** La metodología es explícitamente replicable y el dashboard facilita la revisión de los datos.
- **Profundidad adecuada al nivel de pregrado:** La cobertura de once años con dos segmentos institucionales distintos, la validación externa y la documentación de brechas exceden claramente el estándar habitual de una memoria de Ingeniería Civil Industrial.

**Justificación del nivel:** Nivel 5 pleno.

---

## Comentario transversal para la comisión

La memoria tiene un núcleo científico sólido (relevancia 5, introducción 5) y un desarrollo metodológico bien fundamentado (4). Sus debilidades son puntuales y corregibles: un error aritmético verificable (H-01), la ausencia de análisis de sensibilidad a α y la falta de código versionado (H-02). El trabajo no debería ser penalizado en la defensa oral si los autores demuestran: (a) comprensión del error H-01 y saben cómo corregirlo, y (b) capacidad para articular por qué α = 0,3776 es la elección más plausible y qué implica para el resultado un α distinto.

---

*Salida de FASE 4 — conforme a AUDIT_PROTOCOL.md §5.*
