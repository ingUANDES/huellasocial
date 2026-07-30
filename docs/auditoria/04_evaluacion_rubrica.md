# FASE 4 — Evaluación según rúbrica de titulación UANDES
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha de auditoría:** julio 2026
**Insumo:** memoria completa (`docs/Memoria/chapters/chapter01–06.tex`, `core/primeras_paginas.tex`, `references.bib`), post-corrección (commit `81cd560`), y los resultados verificados de las Fases 1–3 (`01_consistencia_interna.md`, `02_reproduccion_calculos.md`, `03_auditoria_estadistica.md`).
**Postura:** evaluador externo exigente (AUDIT_PROTOCOL §0).

> **Aviso:** La conversión de puntaje ponderado a nota UANDES debe confirmarse con el guía antes de comunicar cualquier nota a los alumnos. Este documento reporta el puntaje en la escala 0–5 de la rúbrica, no la nota final. Esta versión reemplaza la evaluación preliminar de la Fase 0 (basada solo en el PDF, sin código ni datos): varios juicios cambian sustancialmente ahora que H-01/H-10 están cerrados y verificados.

> **Corrección de criterio (julio 2026, tras revisión del guía):** la primera versión de esta Fase 4 evaluaba el Indicador 4 (Desarrollo) exigiendo un pipeline de software consolidado y versionado — un estándar más propio de una memoria de Ingeniería en Computación que de Ingeniería Civil Industrial, donde lo exigible es el rigor de la *aplicación de la metodología* (cuentas satélite), no la ingeniería de software del código que la implementa. Se corrigió el puntaje del Indicador 4 (de 3,0 a 4,0) reemplazando esa exigencia por debilidades metodológicas específicas del dominio de cuentas satélite (ver más abajo). También se corrigió el Indicador 3 (de 4,0 a 4,9): el desajuste de período entre lo declarado en Alcances (2014–2024) y lo efectivamente cubierto (2013–2025 para CMF) no amerita penalización relevante porque el trabajo *excede* lo comprometido, no lo incumple — se registra como corrección textual pendiente para los alumnos, no como falla de rigor. Y el Indicador 5 (de 4,0 a 4,5): H-12 y H-13 (Fase 3) son observaciones de rigor estadístico reales pero de alcance acotado, insuficientes para restar un punto completo dado el resto de fortalezas del indicador de mayor peso.

---

## Resumen de puntajes

| # | Indicador | Peso | Puntaje (0–5) | Contribución ponderada |
|---|-----------|------|---------------|----------------------|
| 1 | Presentación y expresión escrita | 10 % | 4,0 | 0,40 |
| 2 | Resumen | 5 % | 5,0 | 0,25 |
| 3 | Introducción y motivación | 15 % | 4,9 | 0,735 |
| 4 | Desarrollo | 20 % | 4,0 | 0,80 |
| 5 | Análisis y conclusiones | 30 % | 4,5 | 1,35 |
| 6 | Referencias | 5 % | 5,0 | 0,25 |
| 7 | Relevancia, alcance y novedad | 15 % | 5,0 | 0,75 |
| — | **Total** | **100 %** | — | **4,54 / 5,00** |

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

**Puntaje asignado: 4,9 / 5**

**Fortalezas:**
- El problema de invisibilidad estadística de las CAC está bien planteado y motivado institucionalmente (exención tributaria del art. 78, DFL N°5/2003, como causa estructural de la brecha de información contable).
- Objetivo general y cuatro objetivos específicos (§Objetivos) son claros, medibles y siguen una secuencia lógica explícita hacia los capítulos correspondientes.
- El marco institucional (§Marco institucional del proyecto) conecta la memoria con el proyecto Huella Social y la postulación FONDEF sin desviar el foco del trabajo.

**Observación menor (no penalizable):**
- El objetivo específico 3 y la sección de Alcances declaran el período **2014–2024** para la estimación, pero el trabajo efectivamente ejecutado cubre además **2013–2025 para el segmento CMF** (Cuadro 5.5, Capítulo 5) y el agregado total llega hasta 2025. A diferencia de un alcance incumplido (el escenario que penaliza la rúbrica: "alcance no coincide del todo con lo hecho" por *quedarse corto*), aquí el trabajo **excede** lo declarado — cubre más años y un segmento adicional (CMF completo) de los comprometidos. No se penaliza porque no hay sobre-promesa ni brecha de ejecución; el ajuste correspondiente es puramente textual. **Acción recomendada para los alumnos:** actualizar el texto de §Alcances y el objetivo específico 3 a "2013/2014–2025" para que la redacción refleje con precisión la cobertura efectivamente lograda — una corrección de forma, no de fondo.

**Justificación del nivel:** Motivación, objetivos y alcance institucional son de nivel 5 en todos los criterios sustantivos de la rúbrica. Se descuenta una décima solo por la imprecisión textual del período declarado, dado que una comisión rigurosa notará la discrepancia aunque no derive de ella ningún cuestionamiento al trabajo realizado.

---

## Indicador 4 — Desarrollo (20 %)

**Puntaje asignado: 4,0 / 5**

> **Nota de criterio:** esta memoria es de Ingeniería Civil Industrial, no de Ingeniería en Computación. Lo exigible en "Desarrollo" es el rigor de la *aplicación de la metodología de cuentas satélite* (diseño de la estimación, tratamiento del panel, calibración de supuestos) — no un pipeline de software consolidado y versionado al estándar de un producto de ingeniería de software. La versión anterior de esta evaluación penalizaba con fuerza la ausencia de un script único (C-01) y de `requirements.txt` (E-01); ese criterio se corrige aquí. Esos puntos siguen siendo reales y están documentados en la Fase 2 (`02_reproduccion_calculos.md`), pero pesan como observación operativa menor, no como debilidad central de este indicador.

**Fortalezas:**
- El Capítulo 4 (Metodología) es el más sólido del documento: estrategia de estimación en tres componentes (identificación, integración, estimación) clara y bien secuenciada; operacionalización de cada variable del SCN (P1, P2, B1g, D1, B2g, F2, F4) con justificación normativa específica (SCN 2025 párr. 7.169, DFL N°5/2003 art. 78).
- El Cuadro de variables no construibles (§4.3.2) es una contribución metodológica real: documenta brechas con razonamiento institucional específico para Chile, no genérico.
- El dashboard interactivo (§4.4, Sección 5.4) es un entregable tecnológico que excede lo habitual en una memoria de pregrado, y fue verificado funcionalmente en la Fase 2 de esta auditoría.
- Auto-crítica metodológica documentada: la nota sobre CAPUAL/AHORROCOOP (razón P2/P1 ~0,72 vs. 0,3776 del resto) muestra que los autores auditan sus propios supuestos con los datos que ya tenían.

**Debilidades de aplicación metodológica (dominio propio de cuentas satélite, no de software):**
- **α aplicado sin ejercicio de calibración empírica.** Los autores identifican que 2 de 5 entidades con desglose contable confiable (CAPUAL, AHORROCOOP) tienen razón P2/P1 real de ~0,72, el doble del α = 0,3776 aplicado a todo el panel, mientras que las otras 3 (Coopeuch, Oriencoop, Coonfía) tienen razones entre 0,23 y 0,28. Es decir, **ya contaban con los datos** para al menos comparar el resultado agregado bajo α uniforme contra un cálculo con P2 directo para esas 5 entidades, y no lo hicieron — es un ejercicio de validación metodológica de bajo costo (no requiere datos adicionales) que quedó fuera del capítulo de métodos. Distinto del análisis de sensibilidad general (H-17, Fase 3, ya reconocido como trabajo futuro): esto es una calibración puntual con datos ya en mano.
- **Tratamiento del panel DAES desbalanceado por exclusión simple, sin justificación comparativa.** El método adoptado (incluir solo CAC-año con dato disponible, sin imputación ni factores de expansión) se declara pero no se justifica frente a alternativas metodológicas estándar en paneles desbalanceados (p. ej. ponderación por cobertura, imputación por año-cohorte). El propio Capítulo 6 propone "factores de expansión" como recomendación futura, lo que sugiere que los autores reconocen la alternativa pero no explican en el capítulo de métodos por qué optaron por exclusión en esta versión.
- **Criterios de inclusión/exclusión de entidades en el panel incompletos en el texto** (M-01 de la Fase 2, `SOLICITUD_AUTORES.md`): no se documenta explícitamente qué condiciones debe cumplir una CAC para incorporarse al panel ni cómo se trataron entidades disueltas o que cambiaron de régimen de supervisión durante el período — el caso de Coopeuch (migración DAES→CMF) se resuelve bien narrativamente en el Capítulo 6, pero no hay una regla general documentada aplicable a casos futuros similares.

**Observación operativa menor (no central para este indicador):** el pipeline de cálculo vive como fórmulas de Excel transcritas manualmente al LaTeX, sin script consolidado (C-01) ni especificación de entorno (E-01) — documentado y verificado en la Fase 2. Vale la pena mencionarlo brevemente en la defensa, pero no debe pesar como debilidad de diseño metodológico de una memoria de Ingeniería Civil Industrial.

**Justificación del nivel:** El diseño metodológico central (estrategia de estimación, operacionalización SCN, diagnóstico de brechas) es de calidad alta. Se mantiene en nivel 4, no 5, por las tres debilidades de aplicación metodológica señaladas — todas del dominio de cuentas satélite/estimación aplicada, no de ingeniería de software — que son corregibles con los datos que los propios autores ya poseen.

---

## Indicador 5 — Análisis y conclusiones (30 % — el de mayor peso)

**Puntaje asignado: 4,5 / 5**

**Fortalezas:**
- La validación externa (§5.4, Cuadro 5.9) es la fortaleza más notable del trabajo: triangula la estimación propia con una estimación independiente basada en participación patrimonial × PIB de servicios financieros. Es una práctica inusual en memorias de este tipo y responde directamente a una crítica del panel evaluador FONDEF (ausencia de validación cruzada) — verificado aritméticamente sin errores en la Fase 3.
- Las limitaciones (§5.6) son explícitas, completas y honestas: cuatro puntos bien argumentados, incluyendo la propia admisión de que la suma CMF+DAES "no constituye una medición rigurosa y exacta" sino una aproximación de orden de magnitud.
- Las conclusiones (Capítulo 6) son proporcionales a la evidencia: no hay sobre-afirmación causal, y el trabajo distingue explícitamente qué de las cuatro debilidades señaladas por el panel FONDEF aborda (2 de 4) y cuáles quedan pendientes — un ejercicio de honestidad poco común.
- Re-verificado en la Fase 3: cero errores aritméticos adicionales a H-01/H-10 en los 9 cuadros del capítulo de resultados.

**Debilidades:**
- H-12 (Fase 3): el supuesto de estabilidad temporal del 2,41 % de participación patrimonial (aplicado como constante a 13 años) no está declarado como supuesto ni discutido como limitación, pese a condicionar directamente la interpretación del ejercicio de validación externa.
- H-13 (Fase 3): los umbrales de "concordancia" (0,01 pp) y "brecha sistemática" (0,03 pp) del Cuadro 5.9 se definen después de observar los datos, no a priori.
- H-17 (Fase 3): ausencia de análisis de sensibilidad de α, atenuado por estar reconocido como trabajo futuro (Capítulo 6).

**Justificación del nivel:** El indicador de mayor peso de la rúbrica recompensa "métodos adecuados, comparaciones que sitúan el resultado, análisis claro y lógico, conclusiones específicas con su alcance" — los cuatro elementos están presentes con calidad alta, y la Fase 3 no encontró errores aritméticos adicionales al ya corregido H-01. H-12 y H-13 son observaciones de rigor estadístico reales, pero acotadas en alcance: afectan la interpretación fina de un solo cuadro de validación (5.9), no la robustez del análisis central del capítulo (Cuadros 5.1–5.8) ni la lógica de las conclusiones. Por eso se descuenta medio punto, no uno completo: el mérito del análisis (validación externa como práctica infrecuente y bien ejecutada, limitaciones explícitas, conclusiones proporcionales) domina el balance del indicador.

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

La memoria tiene un núcleo científico sólido: relevancia y novedad de nivel 5, resumen y referencias de nivel 5, introducción prácticamente perfecta, y un análisis de resultados que resiste una auditoría de datos completa (Fases 1–3, cero errores aritméticos adicionales al único hallazgo crítico detectado, que además fue corregido de punta a punta por los autores durante esta misma auditoría — un manejo ejemplar del proceso de corrección). El punto más débil, evaluado con el criterio correcto para una memoria de Ingeniería Civil Industrial, es la aplicación metodológica en el Indicador 4: los autores documentan heterogeneidad real en el parámetro central (α) y en la cobertura del panel DAES, pero no ejecutan los ejercicios de calibración/validación de bajo costo que esos mismos datos ya permitían. Los autores no deberían ser penalizados en la defensa oral si demuestran: (a) comprensión completa del mecanismo de H-01/H-10 y de por qué su corrección se validó en tres capas (texto, dato, dashboard); (b) capacidad de recalcular, aunque sea a mano o de forma aproximada, cómo cambiaría el B1g agregado si se usara P2 directo para las 5 entidades con desglose contable confiable en vez de α uniforme; y (c) una justificación explícita de por qué se optó por excluir años sin dato en el panel DAES en vez de ponderar por cobertura.

---

*Salida de FASE 4 — conforme a AUDIT_PROTOCOL.md §5. Ver `05_feedback_alumno.md` (Fase 5, siguiente) para la retroalimentación priorizada y accionable.*
