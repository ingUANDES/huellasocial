# FASE 5 — Retroalimentación accionable para los autores
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha:** julio 2026
**Destinatarios:** Ignacio Ureta, Antonio Ruiz Tagle
**Propósito:** Que defiendan la memoria con pleno conocimiento de sus puntos fuertes, lo ya corregido, y lo que aún falta.

> Esta versión reemplaza el borrador de la Fase 0 (basado solo en el PDF, antes de tener acceso al código y los datos). Varios de esos hallazgos iniciales (error de 2025, conteos de N) **ya fueron corregidos y verificados** en las Fases 2–3; se retiran de esta lista y se documenta su cierre. Lo que sigue es el estado real a julio de 2026.

---

## Resumen ejecutivo (leer primero)

La memoria es metodológicamente sólida, relevante y bien escrita — el puntaje ponderado según la rúbrica de titulación es **4,54/5** (Fase 4; pendiente que el guía confirme la conversión a nota). Ya corrigieron, de punta a punta y de forma verificada de manera independiente, el único error crítico que esta auditoría encontró (el Cuadro 5.7, fila 2025). Eso habla bien de ustedes: pocas memorias reciben una auditoría de datos completa y la resisten con un solo hallazgo crítico, ya cerrado. Lo que queda pendiente antes de la defensa es menor: dos archivos por subir/sincronizar, dos observaciones de rigor estadístico acotadas a un solo cuadro, un ajuste de eje en una figura, y dos ejercicios de calibración metodológica de bajo costo que ya tienen los datos para hacer.

---

## ✅ Ya corregido — sepan explicarlo en la defensa

### Cierre de H-01/H-10 — error del Cuadro 5.7, fila 2025

Detectamos aritméticamente que la fila 2025 del Cuadro 5.7 sumaba el total acumulado del panel DAES a los valores CMF de ese año. Ustedes corrigieron primero el texto de la memoria (commit `81cd560`) y luego —lo más importante— la causa raíz: la fórmula en `HuellaSocial_Consolidado.xlsx` (hoja "Agregado Total") que producía el error, y regeneraron el dashboard público desde el dato corregido (commits `6fca63e`/`37f6051`). Verificamos de forma independiente, recalculando desde el Excel y leyendo el HTML: coincide exactamente en las tres capas (texto, dato fuente, dashboard).

**Para la defensa:** si les preguntan por el error, la respuesta correcta es "sí, lo detectamos y corregido en la fórmula fuente, no solo en el texto — verificado de forma independiente". Es una buena historia de proceso, no algo que ocultar.

### D-06 — fuente de α = 0,3776

Agregaron `2018_MIP_111x111.xlsx` al repositorio y documentaron que α es la suma de la columna de coeficientes técnicos directos de la actividad 94 ("Intermediación financiera") de la MIP 2018 del Banco Central. Verificamos el cálculo directamente sobre el archivo: da 0,3776461, coincide.

---

## 🔴 CRÍTICO — nada pendiente

No hay hallazgos críticos abiertos. El único detectado en toda la auditoría (H-01/H-10) está cerrado y verificado.

---

## 🟡 IMPORTANTE — resolver antes de la entrega final

### F-01 — Sincronizar al repositorio los cambios de texto ya reportados

**Qué está mal:** Nos informaron que ya agregaron a la memoria la cita de D-06 en el texto, la fecha de acceso de D-08, y las precisiones de M-01 a M-04 (definición de "observación", criterios de inclusión DAES, fuente del PIB). Pero a la fecha de esta revisión, `huellasocial` (rama principal) no tiene ningún commit posterior a `81cd560` que modifique `docs/Memoria/`. Es decir, el cambio puede existir en su Overleaf o en su máquina, pero no en el repositorio.

**Por qué importa:** es el mismo patrón que produjo el error original (H-01): una corrección real que no queda registrada donde un tercero pueda verla.

**Qué hacer:** subir ese commit a `huellasocial` antes de la entrega final. Mientras no lo vean reflejado ahí, para efectos de esta auditoría estos puntos siguen "reportados, no verificados".

### F-02 — Completar el registro de D-04 y entregar D-07

**Qué está mal:** `PUB_NOMBRES_PJ.txt` (archivo maestro de personas jurídicas del SII) lo reportan como "disponible" pero no está en `Dashboard_HuellaSocial`. El extracto crudo de CMF-BEST (D-07) no fue mencionado en la última respuesta.

**Corrección de criterio (2026-07-30):** para D-04 **no hace falta subir el archivo** al repositorio — es mala práctica versionar binarios de datos grandes en git. Ya creamos `data/metadata/fuentes_externas.md` con una tabla para esto.

**Qué hacer exactamente:**
1. Para D-04: completar en `data/metadata/fuentes_externas.md` (a) la URL exacta del portal SII desde donde descargaron `PUB_NOMBRES_PJ.txt`, y (b) dónde guardaron el respaldo (carpeta de Drive del proyecto u otro almacenamiento externo). Con eso el ítem queda resuelto — no necesitan subir el archivo.
2. Para D-07: entregar el extracto (mismo criterio aplicará: no hace falta subirlo al repo, sí registrar URL/respaldo en la misma tabla).

### F-03 — Calibrar α contra las 5 entidades con desglose contable propio

**Qué está mal:** ustedes mismos documentan (nota al pie, §4.3.2) que CAPUAL y AHORROCOOP tienen razón P2/P1 real de ~0,72 (el doble del α aplicado) y que Coopeuch, Oriencoop y Coonfía tienen razones entre 0,23 y 0,28. Tienen los datos para comparar el B1g agregado bajo α uniforme contra un cálculo con P2 directo para esas 5 entidades, y esa comparación no está en el capítulo de métodos ni en resultados.

**Qué hacer:** agregar un párrafo (o una nota al pie ampliada) que muestre cuánto cambia el B1g de esas 5 entidades si se usa su P2 real en vez de α×P1. No hace falta rehacer el agregado completo — con mostrar el efecto en esas 5 entidades ya demuestran que evaluaron la robustez del supuesto central del modelo, que es justamente lo que la rúbrica pide en el indicador de mayor peso (Análisis y conclusiones).

### F-04 — Justificar la exclusión simple del panel DAES desbalanceado

**Qué está mal:** el panel DAES incluye solo CAC-año con dato disponible, sin ponderar por cobertura ni imputar. La decisión se declara pero no se justifica frente a alternativas (factores de expansión, que ustedes mismos proponen como trabajo futuro en el Capítulo 6).

**Qué hacer:** una frase en §4.3.2 o §5.6 explicando por qué exclusión simple es preferible a expansión en esta primera versión (por ejemplo: "se prefirió exclusión sobre expansión para no introducir supuestos adicionales sobre la representatividad de las entidades no reportantes, dejando la expansión como línea futura una vez validado el sesgo de selección").

---

## 🟢 PULIDO — mejoras editoriales, no bloquean la defensa

### P-01 — Eje truncado en la Figura 5.1 (dashboard CMF)

**Dónde:** `logos/figuras/CMF.png`, eje derecho ("Aporte PIB %"), que empieza en 0,07 en vez de 0.

**Qué hacer:** regenerar la figura con el eje secundario partiendo de 0, o agregar una nota al pie aclarando que el eje no parte de cero. Tal como está, la caída de 0,119% a 0,073% se ve visualmente más dramática de lo que realmente es (una caída relativa del 39%, no del 90% que sugiere el gráfico).

### P-02 — Declarar el supuesto de estabilidad temporal del 2,41% patrimonial

**Dónde:** Cuadro 5.9 (validación externa) y §5.6 (limitaciones).

**Qué hacer:** una frase reconociendo que el 2,41% es una fotografía de diciembre de 2025 aplicada retroactivamente a 13 años, y que la comparación pierde precisión en los años más alejados de esa fecha.

### P-03 — Fijar (o relativizar) el umbral de "concordancia" del Cuadro 5.9

**Dónde:** §5.4, interpretación del Cuadro 5.9.

**Qué hacer:** los umbrales de 0,01 pp ("concordante") y 0,03 pp ("brecha") aparecen recién al interpretar los resultados. Alternativa simple: cambiar el lenguaje a algo explícitamente cualitativo ("la diferencia es visualmente menor en 2013, 2014, 2021 y 2025") en vez de presentarlo como un criterio con umbral numérico fijo.

### P-04 — Actualizar el período declarado en Alcances

**Dónde:** §Alcances y objetivo específico 3, que dicen "2014–2024".

**Qué hacer:** actualizar a "2013/2014–2025" para reflejar que el trabajo cubre más de lo comprometido (CMF llega hasta 2025). No es una falla — es una mejora de precisión textual sencilla.

### P-05 — Nota aclaratoria de N en los cuadros de cuenta financiera

**Dónde:** Cuadros 5.4, 5.6, 5.8 (cuenta financiera).

**Qué hacer:** el N de estos cuadros difiere del N de los cuadros de producción para el mismo año (por disponibilidad distinta de datos de balance vs. estado de resultados) — ya explicado en general en §4.2.2, pero conviene repetir brevemente en la nota al pie de cada cuadro financiero para que no parezca una inconsistencia al comparar tablas.

### P-06 — Reconciliar en un solo lugar los conteos 35/36/38/42 de cooperativas

**Dónde:** dispersos entre §4.2.2, §4.3.1, Figura 5.3 y Capítulo 6.

**Qué hacer:** una única nota (sugerido: en la tabla de fuentes, §4.1) que explique a qué universo corresponde cada cifra: 35 (DAES con dato financiero), 38 (DAES vigentes en el registro oficial), 36 (catastro propio del proyecto), 42 (35 DAES + 7 CMF, panel unificado).

---

## Preparación para preguntas de la comisión

1. **"¿Por qué α = 0,3776 y no otro valor?"** → De la MIP 2018 del Banco Central, sector 94 (Intermediación financiera) — verificado por esta auditoría contra el archivo fuente. Mencionar que detectaron heterogeneidad (CAPUAL/AHORROCOOP ~0,72 vs. Coopeuch/Oriencoop/Coonfía 0,23–0,28) y, si alcanzan a resolver F-03, mostrar cuánto cambia el resultado con P2 directo para esas 5 entidades.

2. **"¿Cómo reproducimos sus cálculos?"** → Señalar `Dashboard_HuellaSocial` con el commit específico. Ser honestos sobre que el pipeline vive como fórmulas de Excel transcritas al LaTeX, no como un script único — y que ya documentaron ese proceso en el Readme del repositorio.

3. **"¿La suma CMF + DAES es metodológicamente válida?"** → No es una suma exacta; se presenta explícitamente como "aproximación de orden de magnitud" dado que los períodos y coberturas difieren. La validación externa (Cuadro 5.9) muestra que el orden de magnitud es consistente con una fuente independiente (patrimonio CMF/BCCh).

4. **"Encontramos un error en el Cuadro 5.7, fila 2025. ¿Lo sabían?"** → Sí: detectado, corregido en la fórmula fuente (no solo en el texto) y verificado de forma independiente. Pueden mencionar que fue parte de un proceso de auditoría de datos que también revisó los otros 8 cuadros del capítulo sin encontrar errores adicionales.

5. **"¿Por qué no hicieron un análisis de sensibilidad de α si ya sabían que hay heterogeneidad?"** → Está reconocido como línea de trabajo futura (Capítulo 6). Si alcanzan a resolver F-03 antes de la defensa, mejor: pueden mostrar un cálculo concreto, aunque sea acotado a las 5 entidades con datos suficientes.

---

*Salida de FASE 5 — conforme a AUDIT_PROTOCOL.md §5 (numeración de fases del protocolo actualizado; ver `AUDIT_PROTOCOL.md`). Ver `06_proyeccion_cientifica.md` (Fase 6) para la proyección hacia la línea de investigación.*
