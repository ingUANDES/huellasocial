# FASE 3 — Auditoría estadística y de razonamiento
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha:** julio 2026
**Insumos:** `docs/Memoria/chapters/chapter04.tex`, `chapter05.tex` (post-corrección, commit `81cd560`); `HuellaSocial_Consolidado.xlsx` (post-corrección, commit `37f6051`); figuras `CMF.png`, `DAES.png`, `dash_regional2.png`.
**Metodología:** re-cálculo aritmético de cada cuadro del Capítulo 5 desde el Excel fuente; inspección visual de las figuras del dashboard incluidas en el Capítulo 5; verificación de correspondencia entre texto y cuadros.

**Nota de encuadre:** esta memoria no ejecuta tests de hipótesis, regresiones ni inferencia estadística formal — es un ejercicio de contabilidad (cuenta satélite): agregación de variables administrativas y un único supuesto paramétrico (α = 0,3776). Gran parte del checklist de `AUDIT_PROTOCOL.md` §4 (corrección por comparaciones múltiples, potencia, doble escalamiento) **no aplica** por diseño. Lo que sí aplica con fuerza: correspondencia dato↔conclusión, honestidad de las transformaciones y umbrales, análisis de sensibilidad, y honestidad visual de las figuras.

---

## Resumen ejecutivo

Se re-verificó aritméticamente **la totalidad** de los Cuadros 5.1 a 5.9 (cobertura, producción, financiera y validación externa, ambos segmentos y el agregado) contra el Excel fuente corregido: **no se encontraron errores adicionales a H-01/H-10**, ya cerrados en la Fase 2. Este es un resultado positivo relevante: el error de H-01 parece haber sido un caso aislado (una fórmula), no un patrón sistemático.

Se identifican cinco observaciones de rigor metodológico y honestidad visual (H-12 a H-16), de severidad 🟡 o 🟢 — ninguna cuestiona la validez general de la estimación, pero todas son accionables antes de la defensa.

| Severidad | N hallazgos |
|-----------|-------------|
| 🔴 CRÍTICO | 0 |
| 🟡 IMPORTANTE | 4 (H-12, H-13, H-16, H-17) |
| 🟢 PULIDO | 2 (H-14, H-15) |

---

## 1. Correspondencia dato ↔ conclusión

Se recalculó cada afirmación cuantitativa del texto de resultados contra los cuadros y el Excel fuente:

| Afirmación (texto) | Cálculo de verificación | Resultado |
|---|---|---|
| "crecimiento acumulado de 71,2 %" del VAB CMF 2013→2025 | 277.518,8 / 162.119,6 − 1 = 0,7118 | ✅ Coincide |
| "incremento de 3,1 veces" en Activos CMF 2013→2025 | 4.481.909,0 / 1.434.093,4 = 3,126 | ✅ Coincide |
| "incremento de 3,9 veces" en F2 (depósitos) total 2013→2025 | 2.761.339,0 / 709.177,9 = 3,894 | ✅ Coincide |
| "mediana de activos (CMF) representa apenas el 15 %" de la media | 54.404,1 / 359.222,7 = 0,1514 | ✅ Coincide |
| Cuadro 5.9 completo (13 años), columna "Aporte esperado" | %PIB Servicios financieros × 2,41 % | ✅ Coincide en los 13 años |
| Cuadro 5.9 completo, columna "Aporte estimado" | Recalculado desde `total_agg` del Excel | ✅ Coincide en los 13 años (incluyendo 2025 post-corrección) |
| Conteos N del Cuadro 5.7 (producción total) | Suma de N(CMF)=7 + N(DAES) del Cuadro 5.1, año a año | ✅ Coincide en los 13 años |
| Conteos N del Cuadro 5.8 (financiera total) | Suma de N(CMF)=7 + N(DAES) del Cuadro 5.4 (financiera), año a año | ✅ Coincide en los 13 años |
| Figura 5.3 (distribución regional): suma de barras | 20+4+3+2+2+2+1+1+1 | = 36, coincide con "36 cooperativas registradas" del texto |

**Conclusión:** no se detectó ninguna afirmación numérica del texto que no esté sostenida por los cuadros o el dato fuente. No hay sobre-afirmación cuantitativa. El lenguaje de interpretación es consistentemente cauteloso ("cota inferior", "aproximación de orden de magnitud", "no necesariamente refleja actividad real sino efecto composición") — buena práctica, digna de mención positiva ante la comisión.

---

## 2. Diseño y validez

No aplica el vocabulario experimental/causal: la memoria no reclama causalidad en ningún punto, y las correlaciones observadas (p. ej. VAB creciente en DAES) se atribuyen correctamente a efectos de composición del panel antes que a crecimiento real, cuando corresponde (§5.1.2, §5.5, Figura 5.2). Esto es metodológicamente correcto y se destaca como fortaleza.

**H-12 (🟡 IMPORTANTE) — supuesto de estabilidad temporal no declarado en la validación externa.** El Cuadro 5.9 aplica la participación patrimonial de las CAC dentro del sistema bancario y cooperativo (2,41 %, dato puntual a diciembre de 2025) como constante a los 13 años del período 2013–2025, para construir el "aporte esperado" de cada año. Esto implica el supuesto de que la estructura patrimonial relativa de las CAC dentro del sistema financiero no cambió en 13 años — un supuesto fuerte, dado que el propio Cuadro 5.5 muestra que el patrimonio CMF creció más de 2 veces en el período. El texto no declara este supuesto en ningún punto (ni en §4.4 "Supuestos y limitaciones" ni en §5.6 "Limitaciones de los resultados"), pese a que condiciona directamente la interpretación de "concordancia" o "brecha" en el ejercicio de validación externa. **Acción sugerida:** agregar una frase en §5.4 o §5.6 reconociendo que 2,41 % es una fotografía de diciembre de 2025 aplicada retroactivamente, y que la comparación pierde precisión en años más alejados de esa fecha.

---

## 3. Elecciones estadísticas y umbrales

**H-13 (🟡 IMPORTANTE) — umbral de "concordancia" definido después de observar los datos.** El texto de §5.4 clasifica los años 2013, 2014, 2021 y 2025 como "concordantes" (diferencia < 0,01 pp entre aporte esperado y estimado) y 2017–2020 como una "brecha sistemática" (hasta 0,03 pp), pero estos umbrales (0,01 pp / 0,03 pp) no están definidos *a priori* en la sección metodológica (§4.4) — aparecen por primera vez en la interpretación de los resultados, ajustados al patrón que los datos ya mostraban. Esto es precisamente el patrón que `AUDIT_PROTOCOL.md` pide vigilar ("márgenes/umbrales fijados a priori y justificados"). No invalida la comparación —el ejercicio de validación externa es en sí mismo una buena práctica, ausente en versiones anteriores según reconoce el propio texto (§5.4, nota sobre el panel evaluador FONDEF)— pero el umbral debería fijarse antes de mirar los datos, o al menos declararse explícitamente como heurístico/descriptivo y no como criterio estadístico. **Acción sugerida:** en la próxima iteración, definir el margen de tolerancia en §4.4 antes de calcular el Cuadro 5.9, o suavizar el lenguaje de "concordancia/brecha" a algo explícitamente cualitativo ("diferencia visualmente menor/mayor").

**H-17 (🟡 IMPORTANTE) — ausencia de análisis de sensibilidad de α, pese a evidencia propia de heterogeneidad.** La nota al pie de §4.3.2 documenta que CAPUAL y AHORROCOOP tienen razones P2/P1 implícitas de ~0,72 (el doble del promedio sectorial usado, α=0,3776), y que Coopeuch, Oriencoop y Coonfía tienen ratios entre 0,23 y 0,28 (bajo el promedio). Es decir, los propios autores detectaron dispersión sustancial en el parámetro que asumen homogéneo, pero no reportan cuánto cambiaría el B1g agregado o el aporte al PIB si se usara, por ejemplo, un α diferenciado por entidad para las 5 CAC con desglose contable confiable, o un rango de sensibilidad (α ± 1 DE) para el agregado total. Sin este ejercicio, no hay forma de saber si la conclusión central (aporte ≈ 0,08 % del PIB) es robusta a la heterogeneidad ya documentada, o si podría moverse de forma no trivial. **Acción sugerida:** agregar un escenario de sensibilidad de α (aunque sea acotado a las 5 entidades con datos contables suficientes) antes de la defensa; es una extensión de bajo costo dado que el dato ya está en el texto.

No se identifican otros problemas de elección estadística: no hay tests de hipótesis, por lo que no aplica corrección por comparaciones múltiples ni construcción de intervalos de confianza. La transformación P2 = α·P1 es una única escala lineal, sin doble escalamiento.

---

## 4. Tamaño muestral

No aplica un análisis de potencia estadística (no hay tests). Sí es relevante el N pequeño en años tempranos del panel DAES (N=2 en 2014, N=6 en 2019): el texto **rotula correctamente** estos años como de "cobertura parcial" y advierte que los agregados son "cotas inferiores", evitando extraer conclusiones fuertes de esos años puntuales — buena práctica.

---

## 5. Transformaciones de datos

El único parámetro de transformación es α = 0,3776 (verificado en Fase 2, D-06), aplicado uniformemente a ambos segmentos. La memoria reconoce explícitamente esto como limitación (§5.6, ítem 2) y documenta en una nota al pie (chapter04, §4.3.2) la heterogeneidad entre entidades (ver H-17). Buena práctica de auto-crítica metodológica, aunque incompleta sin el análisis de sensibilidad correspondiente.

---

## 6. Honestidad visual de las figuras

Se inspeccionaron las tres figuras del dashboard incluidas en el Capítulo 5 (`CMF.png`, `DAES.png`, `dash_regional2.png`).

**H-14 (🟢 PULIDO):** `dash_regional2.png` (Figura 5.3) es honesta: eje horizontal desde 0, valores rotulados directamente sobre cada barra, sin distorsión. Sin observaciones.

**H-15 (🟢 PULIDO):** `DAES.png` (Figura 5.2) tiene doble eje (B1g en barras, N de cooperativas en línea); el eje izquierdo (B1g) parte de 0. El eje derecho (N) parte de un valor cercano a 2,5, no de 0 — desviación menor dado que la serie de N nunca baja de 2, por lo que la distorsión visual es marginal.

**H-16 (🟡 IMPORTANTE) — eje secundario truncado en la Figura 5.1 (`CMF.png`).** El eje derecho ("Aporte PIB %") de la Figura 5.1 comienza en 0,07, no en 0. Esto exagera visualmente la caída de la línea verde entre 2013 (0,119 %) y 2021 (0,073 %): en el gráfico, la línea recorre casi todo el rango vertical disponible (de arriba a casi abajo del panel), sugiriendo una caída de gran magnitud, cuando la caída real es proporcionalmente menor (−38,7 % relativo) y el propio texto la explica correctamente como efecto de que "el PIB creció a un ritmo superior" (§5.4), no como contracción del sector. Un lector que solo mire la figura (sin leer el texto adjunto) puede llevarse una impresión más dramática que la que los datos sostienen. **Acción sugerida:** regenerar la Figura 5.1 con el eje secundario iniciado en 0, o al menos anotar en el pie de figura que el eje derecho no parte de cero.

---

## 7. Coherencia de conteos del universo de cooperativas (transversal a caps. 4–6)

Se identificaron cuatro cifras distintas de "número de cooperativas" usadas en distintos puntos de la memoria para universos ligeramente distintos:

| Cifra | Concepto | Ubicación |
|---|---|---|
| 35 | CAC DAES con al menos un dato financiero en el panel | §4.2.2 (estadística descriptiva), Cuadro 5.1 |
| 38 | CAC DAES "activas"/vigentes según registro DAES (mayo 2025) | §4.3.1, §5.2.2 |
| 36 | CAC identificadas en el "registro consolidado del proyecto" (catastro propio) | Figura 5.3, §5.4 |
| 42 | Panel unificado CMF (7) + DAES (35) "con datos financieros disponibles en al menos un año" | Capítulo 6 (conclusión) |

El commit `81cd560` ya agregó una aclaración para el par 42-vs-36 (chapter06: "cifra difiere del... catastro de elaboración propia que no pretende ser exhaustivo"), lo cual es correcto y suficiente para ese par. Pero el par 38-vs-35 no tiene una aclaración equivalente en el mismo lugar: en §4.3.2/§5.6 se dice "Para las 26 CAC restantes no existe dato de empleo", cifra que solo cuadra si el universo de referencia es 38 (38−12=26) y no 35 (35−12=23) — el texto no aclara cuál de los dos totales usa como base, lo que puede leerse como una inconsistencia aritmética por un revisor apurado, cuando en realidad es un cambio de universo de referencia no explicitado.

Esto se registra como una extensión menor de H-15 y no como hallazgo nuevo numerado — **recomendación:** agregar una única nota (ideal: en §4.1, tabla de fuentes) que reconcilie en un solo lugar los cuatro conteos (35/38/36/42) y a qué universo corresponde cada uno.

---

## Conclusión de Fase 3

La memoria supera con nota alta el estándar de correspondencia dato↔conclusión y de honestidad interpretativa (lenguaje cauteloso, auto-crítica documentada de supuestos). Las observaciones de esta fase son de calibre "pulido a importante", no crítico: ningún hallazgo de la Fase 3 altera la validez general de la estimación del aporte de las CAC al PIB. Se recomienda resolver H-12, H-13, H-16 y H-17 antes de la defensa por ser visibles y de bajo costo de corrección; H-14/H-15 son opcionales.

---

*Fase 3 ejecutada julio 2026. Ver `01_consistencia_interna.md` (Fase 1), `02_reproduccion_calculos.md` (Fase 2) y `04_evaluacion_rubrica.md` (Fase 4, siguiente) para el resto de la auditoría.*
