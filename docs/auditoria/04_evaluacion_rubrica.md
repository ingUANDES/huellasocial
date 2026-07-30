# FASE 4 — Evaluación según rúbrica de titulación UANDES
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha de auditoría:** julio 2026
**Insumo:** memoria completa (`docs/Memoria/chapters/chapter01–06.tex`, `core/primeras_paginas.tex`, `references.bib`), post-corrección (commit `81cd560`), y los resultados verificados de las Fases 1–3 (`01_consistencia_interna.md`, `02_reproduccion_calculos.md`, `03_auditoria_estadistica.md`).
**Postura:** evaluador externo exigente (AUDIT_PROTOCOL §0).

> **Aviso:** La conversión de puntaje ponderado a nota UANDES debe confirmarse con el guía antes de comunicar cualquier nota a los alumnos. Este documento reporta el puntaje en la escala 0–5 de la rúbrica, no la nota final. Esta versión reemplaza la evaluación preliminar de la Fase 0 (basada solo en el PDF, sin código ni datos): varios juicios cambian sustancialmente ahora que H-01/H-10 están cerrados y verificados.

---

## Resumen de puntajes

| # | Indicador | Peso | Puntaje (0–5) | Contribución ponderada |
|---|-----------|------|---------------|----------------------|
| 1 | Presentación y expresión escrita | 10 % | 4,0 | 0,40 |
| 2 | Resumen | 5 % | 5,0 | 0,25 |
| 3 | Introducción y motivación | 15 % | 4,0 | 0,60 |
| 4 | Desarrollo | 20 % | 3,0 | 0,60 |
| 5 | Análisis y conclusiones | 30 % | 4,0 | 1,20 |
| 6 | Referencias | 5 % | 5,0 | 0,25 |
| 7 | Relevancia, alcance y novedad | 15 % | 5,0 | 0,75 |
| — | **Total** | **100 %** | — | **4,05 / 5,00** |

---

## Indicador 1 — Presentación y expresión escrita (10 %)

**Puntaje asignado: 4,0 / 5**

**Fortalezas:**
- Documento LaTeX bien estructurado, tipografía y formato de cuadros consistentes a lo largo de los seis capítulos.
- Cada cuadro incluye nota al pie con definiciones de variables y fuente — buena práctica sostenida en las 9 tablas del Capítulo 5.
- Longitud apropiada, sin relleno evidente; terminología del SCN (P1, B1g, D1, B2g) usada con precisión y consistencia.
- Resumen (ver Indicador 2) y estructura del documento (§1.5) anticipan correctamente el contenido de cada capítulo.

**Debilidades:**
- H-16 (Fase 3): la Figura 5.1 (`CMF.png`) tiene el eje secundario truncado en 0,07 en vez de 0, lo que exagera visualmente la caída del aporte al PIB — una figura "que aporta claridad" (criterio del nivel 5) debe ser precisa, no solo estéticamente prolija.
- H-14/H-15 (Fase 3, menores): inconsistencia de N entre cuadros de producción y financiera sin nota aclaratoria puntual en cada tabla (aclarado solo a nivel general en §4.2.2).

**Justificación del nivel:** Formato sólido y profesional, pero la imprecisión visual de la Figura 5.1 y la falta de aclaración puntual de los N por tabla impiden el nivel 5 ("figuras precisas que aportan claridad").

---

## Indicador 2 — Resumen (5 %)

**Puntaje asignado: 5,0 / 5**

**Fortalezas:**
- Cubre los tres elementos exigidos por la rúbrica: motivación (invisibilidad estadística de las CAC), desarrollo (integración DAES+SII+CMF, marco SCN 2025/ONU-TSE/CIRIEC) y resultado (VAB ≈ 0,08 % del PIB, contextualizado contra el 2,4 % de participación patrimonial).
- Correctamente calificado como "aproximación de orden de magnitud" ya en el resumen, no solo en el cuerpo — coherente con el hallazgo positivo de la Fase 3 sobre lenguaje cauteloso consistente.
- Bien escrito, sin jerga innecesaria, en una extensión adecuada.

**Justificación del nivel:** Cumple íntegramente el criterio de nivel 5. No se detectan afirmaciones en el resumen no sostenidas por el cuerpo del documento (ver Fase 3, §1, tabla de correspondencia dato↔conclusión).

---

## Indicador 3 — Introducción y motivación (15 %)

**Puntaje asignado: 4,0 / 5**

**Fortalezas:**
- El problema de invisibilidad estadística de las CAC está bien planteado y motivado institucionalmente (exención tributaria del art. 78, DFL N°5/2003, como causa estructural de la brecha de información contable).
- Objetivo general y cuatro objetivos específicos (§Objetivos) son claros, medibles y siguen una secuencia lógica explícita hacia los capítulos correspondientes.
- El marco institucional (§Marco institucional del proyecto) conecta la memoria con el proyecto Huella Social y la postulación FONDEF sin desviar el foco del trabajo.

**Debilidad:**
- El objetivo específico 3 y la sección de Alcances declaran el período **2014–2024** para la estimación ("...cuenta satélite sectorial para el período 2014–2024"), pero el trabajo efectivamente ejecutado cubre 2014–2024 para DAES **y 2013–2025 para CMF** (Cuadro 5.5, Capítulo 5), y el agregado total presentado llega hasta 2025. Es un caso leve pero real de "alcance no coincide del todo con lo hecho" (criterio de nivel 3 de la rúbrica) — en este caso el trabajo *excede* lo declarado (cubre más años, no menos), pero el texto de alcance debería actualizarse para reflejar la cobertura real lograda.

**Justificación del nivel:** Motivación y objetivos son de nivel 5 en solitario; el desajuste de período entre lo declarado y lo ejecutado impide el nivel 5 pleno según el criterio textual de la rúbrica. Corrección de bajo costo: actualizar "2014–2024" a "2013/2014–2025" en §Alcances y en el objetivo específico 3.

---

## Indicador 4 — Desarrollo (20 %)

**Puntaje asignado: 3,0 / 5**

**Fortalezas:**
- El Capítulo 4 (Metodología) es el más sólido del documento: estrategia de estimación en tres componentes (identificación, integración, estimación) clara y bien secuenciada; operacionalización de cada variable del SCN (P1, P2, B1g, D1, B2g, F2, F4) con justificación normativa específica (SCN 2025 párr. 7.169, DFL N°5/2003 art. 78).
- El Cuadro de variables no construibles (§4.3.2) es una contribución metodológica real: documenta brechas con razonamiento institucional específico para Chile, no genérico.
- El dashboard interactivo (§4.4, Sección 5.4) es un entregable tecnológico que excede lo habitual en una memoria de pregrado, y fue verificado funcionalmente en la Fase 2 de esta auditoría.
- Auto-crítica metodológica documentada: la nota sobre CAPUAL/AHORROCOOP (razón P2/P1 ~0,72 vs. 0,3776 del resto) muestra que los autores auditan sus propios supuestos.

**Debilidades — la mayor parte proviene de las Fases 1–2 de esta auditoría:**
- **Reproducibilidad computacional incompleta.** Aunque `Dashboard_HuellaSocial` desbloqueó la mayoría de la Fase 2, C-01 (el pipeline que integra CMF+DAES y produce la hoja `Agregado Total`) **no existe como script**: los cuadros 5.2–5.9 son fórmulas de Excel transcritas manualmente al LaTeX (Fase 2, §4). Esta misma transcripción manual fue la causa raíz de H-01/H-10, un error crítico ya corregido pero que expone el riesgo estructural de no automatizar ese paso.
- **E-01 sin resolver por decisión propia**: no existe especificación de entorno (`requirements.txt`), lo que deja abierta la posibilidad de que el mismo código produzca resultados ligeramente distintos en otra máquina.
- H-17 (Fase 3): pese a documentar heterogeneidad de α entre entidades, no se ejecuta el análisis de sensibilidad correspondiente en esta versión — aunque **ya está correctamente identificado como línea de trabajo futura en el Capítulo 6** (recomendación 2), lo cual es un atenuante real: los autores no ocultan la brecha, la reconocen y la posponen explícitamente.
- H-11 (Fase 2): varios cambios de documentación metodológica reportados por los autores (M-01 a M-04, D-06/D-08) aún no tienen commit visible en el repositorio al momento de esta evaluación.

**Justificación del nivel:** El diseño metodológico en sí (lo que se puede evaluar leyendo el texto) es de calidad alta, casi nivel 5. Pero el criterio de "Desarrollo" en esta rúbrica pondera fuertemente el material que permite ver el trabajo "en detalle" y verificarlo — y ese material (código consolidado, especificación de entorno, pipeline documentado más allá de fórmulas de Excel) sigue siendo insuficiente pese a las mejoras post-auditoría. Se mantiene en nivel 3 ("tareas correctas, material insuficiente para comprenderlas a cabalidad"), con una trayectoria de mejora ya visible y verificada en esta misma auditoría.

---

## Indicador 5 — Análisis y conclusiones (30 % — el de mayor peso)

**Puntaje asignado: 4,0 / 5**

**Fortalezas:**
- La validación externa (§5.4, Cuadro 5.9) es la fortaleza más notable del trabajo: triangula la estimación propia con una estimación independiente basada en participación patrimonial × PIB de servicios financieros. Es una práctica inusual en memorias de este tipo y responde directamente a una crítica del panel evaluador FONDEF (ausencia de validación cruzada) — verificado aritméticamente sin errores en la Fase 3.
- Las limitaciones (§5.6) son explícitas, completas y honestas: cuatro puntos bien argumentados, incluyendo la propia admisión de que la suma CMF+DAES "no constituye una medición rigurosa y exacta" sino una aproximación de orden de magnitud.
- Las conclusiones (Capítulo 6) son proporcionales a la evidencia: no hay sobre-afirmación causal, y el trabajo distingue explícitamente qué de las cuatro debilidades señaladas por el panel FONDEF aborda (2 de 4) y cuáles quedan pendientes — un ejercicio de honestidad poco común.
- Re-verificado en la Fase 3: cero errores aritméticos adicionales a H-01/H-10 en los 9 cuadros del capítulo de resultados.

**Debilidades:**
- H-12 (Fase 3): el supuesto de estabilidad temporal del 2,41 % de participación patrimonial (aplicado como constante a 13 años) no está declarado como supuesto ni discutido como limitación, pese a condicionar directamente la interpretación del ejercicio de validación externa.
- H-13 (Fase 3): los umbrales de "concordancia" (0,01 pp) y "brecha sistemática" (0,03 pp) del Cuadro 5.9 se definen después de observar los datos, no a priori — un criterio de rigor estadístico que la rúbrica exige implícitamente bajo "métodos adecuados".
- H-17 (Fase 3): ausencia de análisis de sensibilidad de α, atenuado por estar reconocido como trabajo futuro (Capítulo 6).

**Justificación del nivel:** El indicador de mayor peso de la rúbrica recompensa "métodos adecuados, comparaciones que sitúan el resultado, análisis claro y lógico, conclusiones específicas con su alcance" — los cuatro elementos están presentes y la Fase 3 no encontró errores aritméticos adicionales al ya corregido H-01. Las brechas de rigor (H-12, H-13) son reales pero puntuales y correctas de comunicar como observaciones de mejora, no como fallas que inválidem el análisis. Nivel 4, no 5, por esas dos brechas de rigor estadístico sin resolver.

---

## Indicador 6 — Referencias (5 %)

**Puntaje asignado: 5,0 / 5**

**Fortalezas:**
- 67 entradas en `references.bib`; referencias primarias de alta calidad (SCN 2025, Manual ONU-TSE 2018, Manual CIRIEC de Barea Tejeiro & Monzón Campos, Statistics Poland 2021, Pedroso et al. 2023).
- Fuentes institucionales chilenas correctamente citadas y verificadas por esta auditoría (BCCh, CMF, DAES, SII — ver D-06 y D-08 en Fase 2).
- Formato de cita consistente (estilo autor-año, `newapa.sty`) a lo largo del documento; cobertura internacional pertinente (España, Portugal, Polonia) que sitúa el caso chileno en un contexto comparado real, no solo declarativo.

**Justificación del nivel:** No se detectaron citas del texto ausentes en la bibliografía en los capítulos revisados, ni fuentes de calidad dudosa. Nivel 5.

---

## Indicador 7 — Relevancia, alcance y novedad (15 %)

**Puntaje asignado: 5,0 / 5**

**Fortalezas:**
- Primer ejercicio sistemático y documentado de estimación del aporte al PIB de las CAC chilenas bajo estándares internacionales de cuentas satélite (SCN 2025, ONU-TSE, CIRIEC).
- Integración original de tres fuentes administrativas (DAES, CMF-BEST, SII) mediante RUT normalizado, con justificación institucional específica (DFL N°5/2003) — no una aplicación mecánica de manuales internacionales.
- Alineamiento estratégico verificado: el trabajo responde directamente a 2 de las 4 debilidades señaladas por el panel evaluador FONDEF (folio ID26I10768, nota 2,73/5, no seleccionado) y alimenta la siguiente postulación ANID.
- Profundidad y escala (13 años, 42 CAC, dos regímenes de supervisión, validación externa, dashboard interactivo funcional — verificado en Fase 2) exceden claramente el estándar habitual de una memoria de Ingeniería Civil Industrial.

**Justificación del nivel:** Nivel 5 pleno.

---

## Comentario transversal para la comisión

La memoria tiene un núcleo científico sólido: relevancia y novedad de nivel 5, resumen y referencias de nivel 5, y un análisis de resultados que resiste una auditoría de datos completa (Fases 1–3, cero errores aritméticos adicionales al único hallazgo crítico detectado, que además fue corregido de punta a punta por los autores durante esta misma auditoría — un manejo ejemplar del proceso de corrección). El punto más débil objetivamente es la reproducibilidad computacional (Indicador 4): el pipeline de cálculo vive como fórmulas de Excel transcritas a mano al LaTeX, sin script consolidado ni especificación de entorno, lo cual —como demostró esta misma auditoría— es precisamente el tipo de eslabón donde se cuelan errores silenciosos. Los autores no deberían ser penalizados en la defensa oral si demuestran: (a) comprensión completa del mecanismo de H-01/H-10 y de por qué su corrección se validó en tres capas (texto, dato, dashboard); (b) una propuesta concreta para automatizar la generación de tablas desde el Excel, aunque no llegue a implementarse antes de la defensa; y (c) capacidad de discutir, aunque sea cualitativamente, cómo cambiaría el resultado principal bajo un α distinto para las entidades con desglose contable propio.

---

*Salida de FASE 4 — conforme a AUDIT_PROTOCOL.md §5. Ver `05_feedback_alumno.md` (Fase 5, siguiente) para la retroalimentación priorizada y accionable.*
