# FASE 6 — Proyección científica y continuidad de la línea de investigación
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha:** julio 2026  
**Auditor:** Research Engineering Assistant (en rol de co-investigador permanente)  
**Esta fase no es evaluativa — es generativa.**  
**Nota metodológica:** Las preguntas y propuestas marcadas con [AUTORES] fueron identificadas o sugeridas explícitamente en la memoria (§6.3). Las marcadas con [EQUIPO] son aportaciones del equipo de investigación como co-investigador. Las marcadas con [EQUIPO+] son síntesis o extensiones que amplían lo que los autores sugirieron.

---

## 6.1 — Oportunidades de publicación

### Contribución más publicable

La contribución central de la memoria es **la primera estimación sistemática de la contribución al PIB de las cooperativas de ahorro y crédito chilenas mediante cuentas satélite**, usando un diseño de integración de fuentes administrativas adaptado a la regulatoria chilena (exención DFL N°5/2003) y validado externamente. Esto es suficiente para un **artículo completo** en una revista de economía cooperativa o de medición de la economía social.

La contribución metodológica específica (sustitución de la declaración de renta por coeficiente MIP para estimar P2, en contextos de exención tributaria cooperativa) tiene potencial de interés más allá de Chile: ninguno de los casos documentados en la literatura (España, Portugal, Polonia) enfrenta esta restricción específica.

### Revista objetivo principal

**Annals of Public and Cooperative Economics** (Wiley, Q2, ISSN 0003-5092)
- Scope: política, economía y estadística de cooperativas, mutuales y sector público. La metodología de cuentas satélite aplicada a cooperativas encuadra directamente.
- Tiempo estimado de revisión: 3–6 meses para primera decisión.
- Formato típico: 7.000–10.000 palabras. La memoria puede convertirse en este formato con trabajo de condensación.
- Limitación: cobertura geográfica latinoamericana es escasa en la revista; eso puede ser argumento de originalidad o de rechazo por "fuera de alcance habitual".

**Alternativas en orden de prioridad:**

| Revista | Tipo | Q | Razonamiento |
|---------|------|---|-------------|
| *VOLUNTAS* (Springer) | Nonprofit / ESS | Q1 | Alta visibilidad; cuentas satélite no-profit es tema central |
| *Latin American Economic Review* (Springer) | LatAm Q1 | Q1 | Ángulo de medición macroeconómica; menor competencia en cuentas satélite |
| *Revue d'Économie Sociale et Solidaire* (RECMA) | Francófonos | — | Menor impacto pero alcance europeo en ESS |
| *El Trimestre Económico* (FCE) | Iberoamérica | Q2 | Paper en español; alto reconocimiento en la región |

### Qué debe reforzarse para pasar revisión por pares

1. **Corrección H-01** (obligatoria): el error del Cuadro 5.7 fila 2025 debe corregirse antes de cualquier envío.
2. **Análisis de sensibilidad de α** (alta prioridad): sin este análisis, los revisores preguntarán invariablemente qué pasa si α varía ±15 %. Los autores ya lo reconocen en §6.3.
3. **Estado del arte internacional más explícito**: la memoria conoce bien los casos europeos pero no los posiciona en un marco comparativo estructurado. Para un paper, la Tabla 1 debería ser "Methodological approaches to cooperative satellite accounts by country: data sources, P2 estimation, and coverage" (Chile, Spain, Portugal, Poland, Mexico).
4. **Repositorio reproducible**: los revisores pedirán acceso a los datos o al código. Un repositorio limpio con datos de ejemplo y código documentado (M2 del RESEARCH_ROADMAP) es condición para muchas revistas Q1.
5. **Discusión de generalización**: el paper debería responder explícitamente: ¿el método es replicable a otros países con restricciones similares? ¿A otros tipos de cooperativas?

---

## 6.2 — Preguntas de investigación abiertas

### Preguntas que la memoria identifica explícitamente [AUTORES]

| Pregunta | Tipo | Sección que la identifica |
|----------|------|--------------------------|
| ¿Cómo varía el resultado si α es diferenciado por entidad (directo desde EEFF de Coopeuch, Oriencoop, Coonfía)? | (a) extensión directa del mismo método | §6.3 / fn. 3 |
| ¿Cómo cambia el VAB agregado ante variaciones de ±10–20 % en α? | (a) extensión directa | §6.3 |
| ¿Cuántas horas de voluntariado aportan las CAC y a qué salario sombra equivalen? | (b) requiere nuevos datos (encuesta VOV) | §6.3 / Cuadro 4.6 |
| ¿Cómo estimar la cobertura completa del universo DAES mediante factores de expansión? | (a) extensión directa | §6.3 |
| ¿F2 y F4 deben formalizarse en la cuenta financiera o mantenerse como contexto? | (a) extensión metodológica | §6.3 |
| ¿Cómo migrar el dashboard a actualización periódica en producción? | Tecnológica | §6.3 |

### Preguntas que el equipo de investigación agrega [EQUIPO]

| Pregunta | Tipo | Prioridad estratégica |
|----------|------|-----------------------|
| ¿Replicar la metodología para fundaciones y ONG con datos FECU Social? | (a) extensión directa | Alta — M5 del RESEARCH_ROADMAP |
| ¿Cómo cambió la visibilidad estadística de las CAC tras la migración CMF 2019? (discontinuidad DAES→CMF como experimento natural) | (c) nueva metodología (DiD) | Alta |
| ¿El patrón CAC chileno es comparable con los casos de Argentina, Colombia, Brasil? ¿Por qué la cuenta satélite LatAm está menos avanzada que en Europa? | (d) colaboración internacional | Media |
| ¿La Ley 21.440 (transparencia OSC, 2022) generó un aumento en el reporte financiero voluntario? Diseño DiD. | (b) requiere datos post-2022 | Media |
| ¿Existe correlación entre VAB/socio y variables de gobernanza (tamaño directorio, tasa de participación en asambleas)? | (b) requiere nuevos datos de directorio | Baja (exploratoria) |
| ¿El ratio D1/B1g de 0.43–0.78 en DAES es comparable con el benchmarking internacional de cooperativas financieras? | (a) extensión directa | Baja (para el paper, sección de discusión) |

---

## 6.3 — Propuesta de continuidad para memorias y tesis futuras

Las propuestas se ordenan en secuencia lógica: cada una toma los outputs de la memoria auditada como insumo.

### Propuesta 1 — Análisis de sensibilidad y P2 diferenciado (Pregrado, urgente)
**Pregunta central:** ¿Cuánto cambia el VAB estimado si α se diferencia entre grandes (Coopeuch, Oriencoop, Coonfía) y pequeñas CAC?  
**Por qué ahora:** Es la extensión más directa y necesaria para el paper M1. Puede ser una memoria breve o un capítulo del paper mismo.  
**Datos:** Ya disponibles (el panel de la memoria auditada + los EEFF auditados de las 3 CAC grandes).  
**Método:** Calcular P2 directamente para las 3 CAC con desglose confiable; usar α diferenciado por tamaño; comparar VAB agregado con el resultado actual.  
**Nivel:** Pregrado (1 semestre, foco cuantitativo).  
**Reutilizable del pipeline actual:** Todo el código de cálculo de VAB (C-02); solo cambiar la función de α.  
**Qué reconstruir:** Nada mayor; añadir una función de α(i) condicional.

### Propuesta 2 — Extensión a fundaciones y ONG (Pregrado / Magíster)
**Pregunta central:** ¿Cuál es el VAB de las fundaciones y ONG con FECU Social, y cómo se compara con el caso CAC?  
**Datos:** FECU Social (COS / CMF), disponible público; datos SII complementarios.  
**Método:** La misma lógica de integración de fuentes por RUT, con adaptación metodológica para producción no de mercado (valoración al costo, conforme Manual ONU-TSE).  
**Dependencia:** Requiere M2 (pipeline reproducible documentado) como plantilla.  
**Nivel:** Pregrado ambicioso o Magíster.  
**Alineamiento estratégico:** M5 del RESEARCH_ROADMAP; fortalece M8 (ANID ID27) con evidencia de generalización de la metodología más allá de las CAC.

### Propuesta 3 — Cuenta Satélite de la ESS: integración multi-subsectorial (Magíster / Doctorado)
**Pregunta central:** ¿Cuál es el VAB agregado de la Economía Social y Solidaria en Chile (cooperativas + fundaciones + ONG + mutuales) como primer intento de cuenta satélite completa?  
**Datos:** Combina los outputs de Propuesta 1 + Propuesta 2 + datos de CONFECOOP (mutuales).  
**Método:** Marco contable del Manual ONU-TSE, tratamiento de producción de mercado vs. no-mercado, deflactación para series reales.  
**Dependencia:** Requiere Propuesta 1 y 2 completadas.  
**Nivel:** Magíster / Doctorado; proyecto ambicioso (2–3 años).  
**Por qué vale:** Es el primer trabajo de este tipo en Chile y uno de los pocos en América Latina; alinea directamente con la Resolución ONU A/RES/77/281 (2023) y tiene potencial de publicación en VOLUNTAS o en Series F de Naciones Unidas.

### Propuesta 4 — Discontinuidad 2019 como experimento natural (Pregrado / Magíster)
**Pregunta central:** ¿Migrar de DAES a supervisión CMF (2019) cambia la calidad del reporte financiero de las CAC, medida por completitud de variables del SCN?  
**Datos:** El panel existente (CAC que pasaron de DAES a CMF en 2019) + la serie histórica CMF.  
**Método:** Diferencia en diferencias (DiD); las CAC que NO migraron son el grupo control.  
**Nivel:** Pregrado con sólida formación econométrica o Magíster.  
**Por qué es viable:** La migración de 2019 es un shock de política pública exógeno (no elegido por las cooperativas más eficientes) y afectó a un conjunto conocido de entidades.

---

## 6.4 — Vínculo con la estrategia ANID

### Diagnóstico de críticas ANID resueltas por esta memoria

| Crítica documentada | ¿La memoria la resuelve? | Cómo |
|--------------------|--------------------------|------|
| Cuantificación del problema por tipo de organización | ✅ Sí | VAB 0,07–0,12 % PIB para CAC; primera cifra citable |
| Estado del arte débil / no diferenciación de BIPS | ❌ No (parcialmente) | Revisa experiencias internacionales pero no compara con BIPS ni plataformas |
| Metodología sin diseño experimental / métricas de efectividad | ❌ No | La memoria estima cuentas satélite, no evalúa la plataforma |
| Modelo de gobernanza del observatorio no especificado | ❌ No | Fuera del alcance |
| Hitos sin indicadores TRL | ❌ No | Fuera del alcance |
| Ausencia de proceso formal de validación cruzada | ✅ Sí | §5.3.3 implementa triangulación CMF-BCCh |

### Qué aporta concretamente a la postulación ID27

1. **Resultado previo verificable y citable:** Los evaluadores ANID piden evidencia de producción científica. La memoria, convertida en paper enviado (M1), satisface este requisito. La cifra 0,07–0,12 % es la "quantificación del problema" que los tres evaluadores anteriores señalaron como ausente.

2. **TRL 3 demostrable:** El dashboard HTML descargable y el panel Shiny R existente, combinados con el pipeline documentado (M2), elevan la verificabilidad del TRL 3 de "declarado" a "demostrable con evidencia".

3. **Validación cruzada institucionalizada:** La triangulación del §5.3.3 puede presentarse en la postulación ID27 como "protocolo de validación cruzada del caso piloto", respondiendo directamente a la cuarta crítica documentada.

4. **Cambio narrativo en la sección de cuantificación:** La apertura de la sección 1.1 de ID27 debería usar la cifra de la memoria: "Las cooperativas de ahorro y crédito chilenas, el caso piloto de Huella Social, contribuyen entre 0,07 % y 0,12 % del PIB nacional —estadísticamente invisibles en el SCN— a pesar de representar el 2,41 % del patrimonio del sistema financiero cooperativo y bancario (CMF, 2025)." Esto transforma la crítica "cuantificación insuficiente" en una fortaleza demostrada.

### Qué sigue pendiente antes de ID27 (M8 del RESEARCH_ROADMAP)

| Tarea | Estado tras esta memoria | Acción requerida |
|-------|--------------------------|-----------------|
| Paper en preparación (M1) | Borrador — requiere correcciones H-01, análisis de sensibilidad | Corregir + escribir IMRAD |
| Pipeline reproducible (M2) | Código en repo externo; no en huellasocial | Integrar + documentar |
| Landscape analysis de plataformas (M3) | Pendiente | Iniciar |
| Protocolo de evaluación de impacto (M4) | Pendiente | Diseñar |
| Gobernanza del observatorio (M6) | Pendiente | Diseñar |

---

## 6.5 — Literatura relevante no citada

### Omisiones que debilitan la contribución declarada

| Obra | Por qué debería citarse | Impacto si se omite |
|------|------------------------|---------------------|
| Salamon et al. (1999). *Global Civil Society: Dimensions of the Nonprofit Sector*. Johns Hopkins. | Es la fuente fundacional del Manual ONU-TSE que los autores sí citan; no citarla es como citar el SCN sin citar las cuentas nacionales previas | Un revisor de VOLUNTAS o similar lo notará |
| Monzón & Chaves (2012, 2017). *The European Social Economy at a Crossroads* / *Social Economy in the European Union*. CIRIEC International. | Son los trabajos de referencia de CIRIEC que contextualizan el Manual que sí se cita | Debilita el anclaje teórico del Manual CIRIEC |
| Monzón & Chaves (2008). "The European Social Economy: Concept and Dimensions of the Third Sector". *Annals of Public and Cooperative Economics*. | Relevante si se envía a esa revista; es artículo fundacional de los guest editors y evaluadores | Riesgo de rechazo por "no conoce la literatura base de la revista" |
| Salamon & Anheier (1996/1998). *The Emerging Nonprofit Sector*. | Evidencia internacional de la "brecha de medición" que motiva la memoria | Fortalece la motivación del problema |

### Omisiones de contexto (no críticas pero recomendadas)

| Obra | Justificación |
|------|--------------|
| Lemus & Rojas (2022) | **YA CITADO** — apropiado |
| Périlleux, Vanroose & D'Espallier (2016) | Citado en bibliografía — bien |
| Brown et al. (2015) | Citado — bien |
| Uzea & Duguid (2015) | Citado — bien |
| Carini & Bouchard (2026) | Citado como borrador de revisión interna. Al momento de enviar el paper, verificar si fue publicado oficialmente como reporte de UNTFSSE. Si sigue siendo borrador, debería moverse a "comunicación personal" o eliminarse. |
| Akerlof (1970). "The Market for Lemons". *QJE*. | El marco teórico de PROJECT.md lo usa; la memoria lo menciona implícitamente pero no lo cita. Para el paper, si se argumenta la asimetría de información como motivación, debe aparecer en bibliografía. |

### Literatura latinoamericana que fortalecería el estado del arte

| Obra | Por qué | Tipo |
|------|---------|------|
| Antón et al. (2022). *Measuring the Social Economy in Latin America*. CEPAL/OIT. | Panorama regional de cuentas satélite en AL; diferencia la propuesta chilena del contexto | Working paper CEPAL |
| Programa de estadísticas de economía social de INEGI México | CIRIEC-México (2022) está citado; complementarlo con las estadísticas oficiales INEGI 2023 | Fuente oficial |

---

## Resumen de acciones para el equipo (Research OS)

| Acción | Plazo recomendado | Milestone |
|--------|------------------|-----------|
| Corregir H-01 (Cuadro 5.7 fila 2025) en el PDF | Antes de la defensa | — |
| Solicitar a Ureta y Ruiz Tagle los insumos D-02, D-03, C-02 (ver SOLICITUD_AUTORES.md) | Inmediato | M2 |
| Integrar código y datos de Dashboard_HuellaSocial al repositorio principal | Q3 2026 | M2 |
| Añadir análisis de sensibilidad de α al borrador del paper | Q3 2026 | M1 |
| Redactar borrador IMRAD del paper (estructura: abstract / intro / método / resultados / discusión / conclusiones) | Q3–Q4 2026 | M1 |
| Añadir tabla comparativa de metodologías por país al paper | Q4 2026 | M1 |
| Enviar a Annals of Public and Cooperative Economics | Q4 2026 | M1 |
| Iniciar M5 (extensión a fundaciones) usando este pipeline como plantilla | Q1 2027 | M5 |
| Actualizar RESEARCH_ROADMAP.md con la cifra verificada (0,07–0,12 % PIB) y con la corrección H-01 | Inmediato | — |

---

*Salida de FASE 6 — conforme a AUDIT_PROTOCOL.md §3 (adición de FASE 6). Esta fase alimenta el RESEARCH_ROADMAP.md.*
