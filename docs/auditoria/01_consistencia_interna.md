# FASE 1 — Consistencia interna del documento
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha de auditoría:** julio 2026  
**Auditor:** Research Engineering Assistant (Research OS)  
**Insumo:** PDF únicamente (sin código ni datos crudos)  
**Metodología:** verificación aritmética directa sobre los valores reportados en las tablas

---

## Resumen ejecutivo

La auditoría de consistencia interna identifica **1 error crítico verificado aritméticamente**, **5 hallazgos importantes** y **2 pulidos**. El error más grave es una suma incorrecta en el Cuadro 5.7 (fila 2025) que puede probarse sin código: los totales acumulados del panel DAES fueron sumados a los valores del segmento CMF en el año 2025, generando una cifra de aporte al PIB incorrecta (0,106 %) que los autores reconocen como anómala pero atribuyen erróneamente a efectos de composición.

| Severidad | N hallazgos |
|-----------|-------------|
| 🔴 CRÍTICO | 1 (H-01) |
| 🟡 IMPORTANTE | 5 (H-03 a H-07) |
| 🟢 PULIDO | 2 (H-08 a H-09) |

---

## H-01 — Error aritmético verificado: Cuadro 5.7 fila 2025

| Atributo | Detalle |
|----------|---------|
| **id** | H-01 |
| **Severidad** | 🔴 CRÍTICO |
| **Ubicación** | §5.3.1, Cuadro 5.7, fila "2025"; §5.3.3, Cuadro 5.9, fila "2025" |
| **Tipo** | VERIFICADO — prueba aritmética reproducible desde el PDF |

**Descripción:** El Cuadro 5.7 presenta la cuenta de producción y generación del ingreso total (CMF + DAES). La nota al pie del cuadro dice explícitamente: *"Los años 2013 y 2025 corresponden exclusivamente al segmento CMF (N = 7)."* Por lo tanto, los valores de la fila 2025 en el Cuadro 5.7 deberían ser idénticos a los del Cuadro 5.5 (Segmento CMF) para el mismo año.

**Prueba aritmética:**

| Variable | Cuadro 5.7 (fila 2025) | Cuadro 5.5 (CMF, 2025) | Diferencia | Total DAES (Cuadro 5.2) |
|----------|----------------------|----------------------|-----------|------------------------|
| P1 | 577.398,6 | 445.885,0 | **131.513,6** | 131.513,6 ✓ |
| B1g | 359.372,9 | 277.518,8 | **81.854,1** | 81.854,1 ✓ |
| D1 | 167.736,1 | 122.763,2 | **44.972,9** | 44.972,9 ✓ |
| B2g | 191.636,8 | 154.755,6 | **36.881,2** | 36.881,2 ✓ |
| Rem | 113.142,2 | 108.265,0 | **4.877,2** | 4.877,2 ✓ |

En los cinco casos, la diferencia entre el valor del Cuadro 5.7 (2025) y el del Cuadro 5.5 (CMF, 2025) es exactamente igual al total acumulado del panel DAES (fila "Total" del Cuadro 5.2). La probabilidad de que cinco coincidencias exactas sean producto del azar es nula.

**Mecanismo probable:** Al construir el Cuadro 5.7, los totales de la fila "Total" del Cuadro 5.2 (DAES, suma 2014–2024) fueron sumados a los valores CMF del año 2025 en lugar de sumarse a los valores del año correspondiente.

**Impacto en Cuadro 5.9 (validación externa):** La cifra de "aporte estimado" para 2025 en el Cuadro 5.9 es 0,106 %, derivada del B1g incorrecto (359.372,9 MM$). Con el valor correcto (B1g CMF-solo = 277.518,8 MM$) y el PIB 2025 estimado:

- B1g correcto / PIB 2025 = 277.518,8 / ~320.000.000 × 100 ≈ **0,087 %**
- Este valor encuadra perfectamente dentro del rango esperado (0,075–0,113 %) de la validación externa, eliminando la anomalía que los autores interpretan cautelosamente en el texto (§5.3.3).

**Nota sobre la buena fe:** Los autores sí detectaron la anomalía del 0,106 % en §5.3.3 ("El valor de 2025 debe interpretarse con cautela"), pero lo atribuyeron a efectos de composición por cobertura parcial, sin identificar el error de cálculo. La lógica de la nota es correcta en principio; el diagnóstico de la causa es incorrecto.

**D1/B1g para 2025 en Cuadro 5.7:** El ratio calculado (0,47) también es incorrecto. El correcto (CMF-solo) es 122.763,2 / 277.518,8 = 0,44.

**Acción concreta:** Corregir la fila 2025 del Cuadro 5.7 usando los valores del Cuadro 5.5 exclusivamente. Corregir el dato de la fila 2025 en el Cuadro 5.9 con el aporte recalculado (~0,087 %). Actualizar el texto de §5.3.3 eliminando la cautela innecesaria para ese año.

---

## H-03 — Conteo de observaciones DAES: tres cifras inconsistentes

| Atributo | Detalle |
|----------|---------|
| **id** | H-03 |
| **Severidad** | 🟡 IMPORTANTE |
| **Ubicación** | §4.2.2 (p. 23), §4.3.1 (p. 29–30), Cuadro 5.2 (N-column) |
| **Tipo** | VERIFICADO — cómputo directo de la columna N del Cuadro 5.2 |

**Descripción:**

| Fuente | Cifra | Cita exacta |
|--------|-------|-------------|
| §4.2.2 | **129** | "El segmento DAES cubre 35 CAC no supervisadas por la CMF para el período 2014–2024, con un total de **129 observaciones** para la variable de producción total (P1)." |
| §4.3.1 (x2) | **133** | "El resultado es un panel de **133 observaciones** correspondientes a 35 CAC distintas para el período 2014–2024"; "El panel consolidado del segmento DAES suma **133 observaciones**" |
| Cuadro 5.2, suma N | **122** | 2+7+9+12+14+6+10+10+19+22+11 = 122 |

Además, §4.3.1 dice "entre 2 y **24** entidades por año" pero el Cuadro 5.1 muestra un máximo de **22** entidades (2023). Esta es una sub-inconsistencia dentro del mismo hallazgo.

**Posibles explicaciones (no confirmables sin datos):**
- 133 = observaciones con al menos una variable; 129 = con P1 específicamente; 122 = con P1 y D1. Si esta es la distinción, debe explicitarse en el texto porque las tres cifras aparecen sin calificación.
- Una de las tres es un error tipográfico (129 o 133 podrían ser ediciones parciales de un número anterior).

**Acción concreta:** Establecer una definición única y consistente de "observación" (ej.: CAC × año con P1 disponible) y usar esa definición en todos los lugares del documento. Reportar los tres subconjuntos si son genuinamente distintos (con P1, con D1, con balance completo), diferenciándolos explícitamente. Reconciliar el máximo anual (22 vs 24).

---

## H-04 — Cuadro 5.8: N incorrecto en 11 de 13 años

| Atributo | Detalle |
|----------|---------|
| **id** | H-04 |
| **Severidad** | 🟡 IMPORTANTE |
| **Ubicación** | §5.3.2, Cuadro 5.8 |
| **Tipo** | VERIFICADO — cruzan los N de Cuadros 5.4 y 5.6 con los valores de Cuadro 5.8 |

**Descripción:** El Cuadro 5.8 presenta la cuenta financiera total (CMF + DAES). Los valores de activos, patrimonio, F2 y F4 SÍ incluyen datos DAES (verificado: para 2015, Activos 5.8 = 1.561.464,4 = CMF 1.529.424,5 + DAES 32.039,9 ✓). Sin embargo, la columna N del Cuadro 5.8 muestra N=7 para todos los años de 2015 a 2024, sin sumar las entidades DAES con balance disponible.

**Verificación para 2014** (correcto): N(5.8)=9 = N(5.6)=7 + N(5.4,2014)=2 ✓  
**Verificación para 2015** (incorrecto): N(5.8)=7 ≠ N(5.6)=7 + N(5.4,2015)=7 → debería ser 14.  
**Verificación para 2023** (incorrecto): N(5.8)=7 ≠ N(5.6)=7 + N(5.4,2023)=18 → debería ser 25.

| Año | N reportado (5.8) | N correcto (5.6 + 5.4) |
|-----|------------------|------------------------|
| 2014 | 9 ✓ | 7+2=9 |
| 2015 | 7 ❌ | 7+7=14 |
| 2016 | 7 ❌ | 7+7=14 |
| 2017 | 7 ❌ | 7+7=14 |
| 2018 | 7 ❌ | 7+10=17 |
| 2019 | 7 ❌ | 7+6=13 |
| 2020 | 7 ❌ | 7+9=16 |
| 2021 | 7 ❌ | 7+8=15 |
| 2022 | 7 ❌ | 7+15=22 |
| 2023 | 7 ❌ | 7+18=25 |
| 2024 | 7 ❌ | 7+11=18 |

**Acción concreta:** Actualizar la columna N del Cuadro 5.8 sumando el N de Cuadros 5.4 y 5.6 por año. Los valores monetarios del cuadro son correctos; solo el N está mal.

---

## H-05 — Figura 5.3: 39 cooperativas vs. 42 del universo DAES + CMF

| Atributo | Detalle |
|----------|---------|
| **id** | H-05 |
| **Severidad** | 🟡 IMPORTANTE |
| **Ubicación** | §5.4, Figura 5.3 (pie de figura) |
| **Tipo** | VERIFICADO — ninguna combinación de los valores declarados en el texto produce 39 |

**Descripción:** El pie de la Figura 5.3 dice "La Región Metropolitana concentra 22 de las **39 cooperativas del universo DAES + CMF**."

Valores declarados en el texto:
- Universo DAES activo (§4.3.1): 38 CAC
- Panel DAES (con al menos un dato): 35 CAC
- Segmento CMF: 7 CAC

Combinaciones posibles:
- 38 + 7 = 45 (universo completo)
- 35 + 7 = 42 (panel completo)
- Ninguna suma 39.

**Hipótesis plausible:** El texto usa alguna definición de "vigente" al momento de la Figura 5.3 que difiere de "activo" (§4.3.1) y de "con al menos un dato" (§5.1.1). Es posible que 32 entidades DAES fueran "vigentes" al momento de la consulta al portal y que 32 + 7 = 39. Esta hipótesis no es verificable sin los datos del registro DAES, pero evidencia que el término "universo" se usa con alcances diferentes en distintas partes del documento.

**Acción concreta:** Definir un único término para cada conjunto (universo, activo, vigente, panel) y usarlo consistentemente. Corregir el pie de la Figura 5.3 con el número exacto correspondiente al criterio de "vigentes al momento de la Figura."

---

## H-06 — Supuesto metodológico incorrecto en §4.3.4

| Atributo | Detalle |
|----------|---------|
| **id** | H-06 |
| **Severidad** | 🟡 IMPORTANTE |
| **Ubicación** | §4.3.4, segundo bullet de supuestos principales |
| **Tipo** | VERIFICADO — contradicho por §4.3.2 en el mismo capítulo |

**Descripción:** La sección §4.3.4 enumera los supuestos principales de la estimación. El primer supuesto es: *"El tramo de ventas del SII es representativo de la producción real de las CAC."*

Sin embargo, §4.3.2 especifica que P1 se obtiene de "la línea `Total_Ingresos_Operación` del estado de resultados de cada CAC" (no del tramo de ventas SII). El SII se usa exclusivamente para la variable PEP (empleados), disponible solo para 12 CAC (§4.3.2, variable PEP).

Este supuesto es, por lo tanto, incorrecto respecto al uso real del SII en la metodología. La producción P1 NO depende del tramo de ventas SII para ninguna CAC: siempre proviene de estados financieros (DAES o CMF-BEST).

**Impacto:** Ante una comisión exigente, esta contradicción entre supuestos declarados y metodología real puede interpretarse como una inconsistencia metodológica o como una omisión del proceso de revisión. El supuesto correcto sería algo como: *"Los datos del SII son representativos para caracterizar el empleo de las 12 CAC presentes en sus registros."*

**Acción concreta:** Reemplazar el primer supuesto. El texto correcto debería describir el supuesto real: que los ingresos operacionales (estado de resultados) son una aproximación válida de P1 en el sentido del SCN 2025.

---

## H-07 — §6.1 dice "42 CAC" pero §5.4 Figura 5.3 dice "39"

| Atributo | Detalle |
|----------|---------|
| **id** | H-07 |
| **Severidad** | 🟡 IMPORTANTE |
| **Ubicación** | §6.1 (Síntesis), §5.4 (Figura 5.3) |
| **Tipo** | VERIFICADO — contradicción directa entre secciones del mismo documento |

**Descripción:** La sección §6.1 declara: *"un panel unificado de 42 CAC... separado en dos segmentos: 7 cooperativas supervisadas por la CMF y hasta 35 cooperativas del segmento DAES."*  
La Figura 5.3 dice "39 cooperativas del universo DAES + CMF."

35 + 7 = 42 ≠ 39. Ambas afirmaciones están en el mismo documento y usan el mismo rótulo "universo DAES + CMF."

**Acción concreta:** Corregir el dato en el pie de la Figura 5.3 o aclarar qué subconjunto específico representa "39."

---

## H-08 — Abstract: cifra de 0,08 % sin calificación de segmento (PULIDO)

| Atributo | Detalle |
|----------|---------|
| **id** | H-08 |
| **Severidad** | 🟢 PULIDO |
| **Ubicación** | Resumen (p. 4) |
| **Tipo** | Opinable — juicio de presentación, no error aritmético |

**Descripción:** El resumen dice *"El aporte estimado se ubica en torno al 0,08 % del PIB nacional."* Sin especificar a qué segmento corresponde ni el rango real:

- Segmento CMF (2013–2025): 0,07–0,12 % (texto §5.2.2: "oscila entre 0,07 % y 0,12 %")
- Segmento DAES (2014–2024): 0,0001–0,0105 % (órdenes de magnitud menores)
- Combinado (2013–2025): 0,073–0,119 %

El 0,08 % es una descripción aproximada y razonable del comportamiento promedio del CMF, pero su presentación sin calificación da a entender que representa el sector completo. La cifra combinada sería más precisa para el abstract.

**Acción concreta:** Añadir una calificación en el abstract: "en torno al 0,08–0,09 % del PIB en la mayor parte del período (con la estimación del segmento CMF, más robusto, en ese rango, y el segmento DAES constituyendo una cota inferior por cobertura parcial)." Este nivel de detalle está ya en §5.3.1 y puede resumirse en el abstract sin extensión excesiva.

---

## H-09 — Supuesto 3 de §4.3.4: "remuneración media del sector financiero" (PULIDO)

| Atributo | Detalle |
|----------|---------|
| **id** | H-09 |
| **Severidad** | 🟢 PULIDO |
| **Ubicación** | §4.3.4, tercer bullet |
| **Tipo** | Opinable — claridad metodológica |

**Descripción:** El tercer supuesto dice *"La remuneración media del sector financiero es representativa del salario promedio de las CAC."* Sin embargo, en §4.3.2 se especifica que D1 se obtiene directamente de la línea `Remuneraciones_y_Gastos_del_Personal` del estado de resultados —es una observación directa, no un supuesto. La remuneración media del sector financiero solo sería un proxy si el dato no estuviera disponible.

**Acción concreta:** Eliminar este supuesto o reformularlo para precisar cuándo se usa: únicamente en casos de memorias DAES que no reportan D1 (si los hay) o en la estimación de PEP cuando se imputa salario por trabajador. Si D1 siempre viene observado, el supuesto sobra.

---

## Checklist AUDIT_PROTOCOL §4 — Aplicado al documento

| Ítem | Estado | Hallazgo |
|------|--------|---------|
| Objetivo general y específicos explícitos | ✅ §1.2 | — |
| Alcance coincide con lo hecho | ✅ | — |
| Revisión de literatura real (no solo definiciones) | ✅ Cap. 2 | — |
| Marco teórico contiene teoría | ✅ Cap. 3 | — |
| Toda figura/tabla referenciada Y explicada | ✅ | — |
| Numeración figuras/tablas correcta y consistente | ✅ | — |
| Estadísticos descriptivos reportados antes de inferir | ✅ §4.2.2, Cuadro 4.2 | — |
| Cada elección metodológica justificada | ✅ (α, D2=0, D3=0) | — |
| Frecuencia, período y origen de datos declarados | ✅ Cuadro 4.1 | — |
| N coherente entre secciones | ❌ | H-03, H-04, H-07 |
| Sin párrafos duplicados | ✅ | — |
| Supuestos consistentes con metodología real | ❌ | H-06 |
| Código + datos versionados y ejecutables por tercero | ❌ | H-02 |
| Toda cifra rastreable a corrida reproducible | ❌ | H-01, H-02 |

---

*Salida de FASE 1 — conforme a AUDIT_PROTOCOL.md §3. Siguiente fase habilitada con insumos actuales: FASE 4 (rúbrica).*
