# FASE 5 — Retroalimentación accionable para los autores
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha:** julio 2026  
**Destinatarios:** Ignacio Ureta, Antonio Ruiz Tagle  
**Propósito:** Que defiendan la memoria con pleno conocimiento de sus puntos débiles y cómo responderlos.

---

## Resumen ejecutivo (leer primero)

La memoria es metodológicamente sólida, relevante y bien escrita. Su contribución empírica —la primera estimación sistemática de la contribución al PIB de las CAC chilenas bajo estándares internacionales— es genuina y publicable. Antes de la defensa, deben corregir un error aritmético en el Cuadro 5.7 que es verificable en segundos por cualquier evaluador con una calculadora, y preparar una respuesta clara sobre la reproducibilidad del trabajo (el código y los datos no están en el repositorio del proyecto). Los demás hallazgos son correcciones editoriales que fortalecen la presentación pero no afectan el resultado principal.

---

## 🔴 CRÍTICO — Corregir antes de cualquier presentación

### C-01 — Error en Cuadro 5.7, fila 2025

**Qué está mal:** La fila 2025 del Cuadro 5.7 (cuenta de producción total CMF + DAES) contiene los totales acumulados del panel DAES (fila "Total" del Cuadro 5.2) sumados a los valores del segmento CMF para el año 2025. La nota del cuadro dice explícitamente que "2025 corresponde exclusivamente al segmento CMF (N = 7)", lo que hace que la inconsistencia sea verificable de inmediato.

**Prueba:** P1(Cuadro 5.7, 2025) = 577.398,6. P1(Cuadro 5.5, CMF, 2025) = 445.885,0. Diferencia = 131.513,6 = Total DAES (Cuadro 5.2). Lo mismo se verifica para B1g, D1, B2g y Rem.

**Consecuencia:** El aporte al PIB de 2025 en el Cuadro 5.9 (0,106 %) está inflado. El valor correcto (CMF-solo) es aproximadamente **0,087 %**, que encuadra perfectamente dentro del rango esperado (0,075–0,113 %) y elimina la "anomalía" que el texto (§5.3.3) trata con cautela. La buena noticia: corregido el error, la validación externa queda aún más limpia.

**Qué hacer exactamente:**
1. Reemplazar todos los valores de la fila 2025 del Cuadro 5.7 con los del Cuadro 5.5 (año 2025): P1=445.885,0; B1g=277.518,8; D1=122.763,2; B2g=154.755,6; Rem=108.265,0; D1/B1g=0,44.
2. Recalcular el aporte estimado 2025 en el Cuadro 5.9 usando el B1g correcto dividido por el PIB 2025.
3. En §5.3.3, actualizar el texto que califica la cifra de 2025: con la corrección, el valor se ubica dentro del rango esperado y no requiere interpretación "con cautela".

**Para la defensa (si aún no corrigen el documento):** Deben poder describir el error, su magnitud y la corrección de memoria. Un evaluador que lo encuentre y no obtenga una respuesta sólida puede interpretarlo como desconocimiento del propio trabajo.

---

### C-02 — Reproducibilidad: preparar respuesta para la comisión

**Qué está mal:** El código de análisis y los datos fuente no están versionados en el repositorio del proyecto (huellasocial). El repositorio Dashboard_HuellaSocial existe y es público, pero no está integrado al Research OS y no contiene instrucciones de reproducción completas.

**Por qué importa ante la comisión:** Una comisión exigente preguntará "¿un tercero puede reproducir sus resultados desde cero?". La respuesta honesta hoy es "parcialmente, con el dashboard descargable". Eso no es suficiente para una auditoría completa.

**Qué hacer exactamente antes de la defensa:**
1. Asegurarse de que el repositorio https://github.com/Iureta1/Dashboard_HuellaSocial contiene: (a) el código que genera los cuadros del capítulo 5, (b) un README con instrucciones de ejecución, y (c) el archivo de requerimientos (requirements.txt).
2. Incluir en la memoria (§4.4 o Anexos) el SHA del commit exacto del repositorio que corresponde a la versión presentada. Ejemplo: "Los resultados son reproducibles desde el commit `abc1234` del repositorio Dashboard_HuellaSocial (https://github.com/Iureta1/Dashboard_HuellaSocial/commit/abc1234)."
3. Para la defensa, tener preparada la demostración de que el dashboard descargable reproduce los cuadros 5.2 y 5.5 exactamente.

---

## 🟡 IMPORTANTE — Corregir en la versión final entregada a la Facultad

### I-01 — Unificar el conteo de observaciones DAES

**Dónde:** §4.2.2 dice "129 observaciones"; §4.3.1 dice "133 observaciones" (dos veces); Cuadro 5.2 suma N=122.

**Qué hacer:** Definir en una sola oración qué es una "observación" (ej.: "CAC-año con P1 disponible"). Luego usar esa cifra en todas las secciones. Si las tres cifras representan subconjuntos distintos (todas las variables vs. P1 vs. P1 y D1), explicarlo explícitamente con una frase en §4.2.2.

### I-02 — Corregir N en Cuadro 5.8

**Dónde:** §5.3.2, Cuadro 5.8, columna N.

**Qué hacer:** Sumar el N del Cuadro 5.4 (DAES financiero) al N del Cuadro 5.6 (CMF, siempre 7) para cada año. Los valores monetarios del cuadro son correctos; solo la columna N está desactualizada.

### I-03 — Reconciliar "39 cooperativas" (Figura 5.3) con "42 CAC" (§6.1)

**Dónde:** Pie de Figura 5.3 vs. §6.1.

**Qué hacer:** Determinar cuántas CAC son "vigentes" al momento de la Figura (puede ser 32 DAES vigentes + 7 CMF = 39 si hubo disoluciones). Si eso es correcto, explicarlo en el pie de figura: "32 cooperativas DAES vigentes al [fecha] más 7 supervisadas por la CMF". Si el "39" es un error tipográfico, corregirlo a 42 (35 + 7).

### I-04 — Corregir supuesto 1 en §4.3.4

**Dónde:** §4.3.4, primer bullet.

**Qué hacer:** El supuesto "El tramo de ventas del SII es representativo de la producción real de las CAC" no describe la metodología real: P1 viene de estados financieros, no del SII. Reemplazarlo por el supuesto correcto, por ejemplo: "Los ingresos operacionales del estado de resultados son una aproximación válida de P1 en el sentido del SCN 2025 (párr. 7.169) para cooperativas financieras de mercado."

### I-05 — Máximo anual DAES: 24 vs 22

**Dónde:** §4.3.1 dice "entre 2 y 24 entidades por año"; Cuadro 5.1 muestra máximo N=22 (2023).

**Qué hacer:** Corregir el texto: "entre 2 y 22 entidades por año."

---

## 🟢 PULIDO — Mejoras editoriales que elevan la calidad

### P-01 — Calificar "0,08 %" en el abstract

**Dónde:** Resumen, segunda frase del tercer párrafo.

**Qué hacer:** Añadir: "para el segmento de cooperativas supervisadas por la CMF, que representa más del 90 % del VAB total del sector; el segmento no supervisado (DAES) aporta adicionalmente entre 0,001 % y 0,011 % del PIB según la disponibilidad de información."

### P-02 — Revisar supuesto 3 en §4.3.4

**Dónde:** §4.3.4, tercer bullet: "La remuneración media del sector financiero es representativa del salario promedio de las CAC."

**Qué hacer:** Si D1 siempre se toma de los estados financieros (es una observación directa), este supuesto sobra. Eliminarlo o precisar: aplica solo a los casos en que D1 no está disponible (si los hay). Si D1 siempre está disponible en los estados de resultados, este supuesto es innecesario y puede confundir a la comisión.

### P-03 — Añadir referencia de Akerlof (1970) a la bibliografía

**Dónde:** §3.4 menciona las "asimetrías de información" que remiten conceptualmente a Akerlof (1970), y PROJECT.md cita a Akerlof explícitamente. Si la memoria lo cita, debe aparecer en la bibliografía formal.

### P-04 — Precisar fuente de datos del BCCh (URL permanente)

**Dónde:** Nota al pie del Cuadro 5.9 y Cuadro 5.3.

**Qué hacer:** Añadir la URL permanente del dataset del Banco Central usado (ej. https://si3.bcentral.cl/...) y la fecha de acceso. Esto facilita la replicabilidad y es estándar en papers de cuentas nacionales.

---

## Preparación para preguntas de la comisión

Estas son las preguntas que un evaluador exigente probablemente hará:

1. **"¿Por qué α = 0,3776 y no otro valor?"** → Respuesta esperada: proviene del sector 94 de la MIP BCCh 2018, que es la metodología estándar cuando no se dispone de datos de consumo intermedio por exención tributaria. Mencionar la nota 3: se detectó heterogeneidad, el análisis de sensibilidad queda pendiente para versiones futuras.

2. **"¿Cómo reproducimos sus cálculos?"** → Respuesta esperada: señalar el repositorio Dashboard_HuellaSocial con el commit SHA específico. Si el código no está limpio, ser honestos: "El código que generó los resultados está disponible en [URL]; la documentación para replicación completa es una mejora prioritaria para la versión journal del trabajo."

3. **"¿La suma CMF + DAES es metodológicamente válida?"** → Respuesta esperada: no es una suma exacta; §5.3 la presenta como "aproximación de orden de magnitud" dado que los períodos difieren y el DAES nunca cubre el universo completo. La validación externa (§5.3.3) muestra que el orden de magnitud es consistente.

4. **"¿Por qué hay diferencias entre 129, 133 y 122 observaciones?"** → Respuesta esperada: [deberían saber la respuesta exacta; ver I-01].

5. **"La fila 2025 del Cuadro 5.7 tiene un error. ¿Lo detectaron?"** → Si corrigen antes de la defensa: "Sí, corregido en la versión final." Si no: "Sí, lo detectamos durante la revisión; los valores correctos son [los del Cuadro 5.5 para 2025]; el error no afecta ningún año del período 2013–2024."

---

*Salida de FASE 5 — conforme a AUDIT_PROTOCOL.md §3.*
