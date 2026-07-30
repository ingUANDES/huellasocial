# Decision Log — Huella Social

> Registro de decisiones metodológicas relevantes, conforme a `CLAUDE.md` §"Decisiones de investigación". Cada entrada: fecha, decisión, razonamiento, alternativas consideradas, quién decidió.

---

## 2026-07-30 — Corrección de criterio de evaluación en Fase 4 (Indicador "Desarrollo")

- **Decisión:** el guía (Sebastián Cea) corrigió el criterio con que esta auditoría evaluaba el Indicador 4 de la rúbrica UANDES ("Desarrollo") para la memoria de Ureta & Ruiz Tagle. La primera versión penalizaba fuertemente la ausencia de un pipeline de software consolidado y versionado (script único C-01, `requirements.txt` E-01) — un estándar más propio de Ingeniería en Computación que de Ingeniería Civil Industrial.
- **Razonamiento:** para una memoria industrial, lo exigible en "Desarrollo" es el rigor de la *aplicación de la metodología* (cuentas satélite: diseño de la estimación, tratamiento del panel, calibración de supuestos), no la ingeniería de software del código que la implementa. Reevaluado con ese criterio, el indicador subió de 3,0 a 4,0/5, sustituyendo las debilidades de reproducibilidad computacional por debilidades metodológicas específicas del dominio (α sin calibración empírica pese a datos disponibles; panel DAES tratado por exclusión sin justificar frente a alternativas; criterios de inclusión de entidades incompletos).
- **Decisiones relacionadas en la misma revisión:** el Indicador 3 (Introducción) subió de 4,0 a 4,9 — el desajuste de período entre lo declarado (2014–2024) y lo ejecutado (2013–2025 para CMF) no amerita penalización porque el trabajo excede lo comprometido, no lo incumple. El Indicador 5 (Análisis y conclusiones) subió de 4,0 a 4,5 — H-12 y H-13 (Fase 3) son observaciones de rigor estadístico reales pero de alcance acotado a un solo cuadro (5.9), insuficientes para restar un punto completo al indicador de mayor peso.
- **Alternativas consideradas:** mantener el criterio original (rechazado: aplica un estándar de disciplina distinta a la de la memoria evaluada).
- **Impacto:** puntaje ponderado total de la Fase 4 sube de 4,05/5 a 4,54/5. Ver `docs/auditoria/04_evaluacion_rubrica.md`.

---

## 2026-07-28 — Cambio de proxy para P1 (producción total) en la cuenta satélite de CAC

- **Decisión:** la producción total (P1) se estima a partir de los ingresos operacionales del estado de resultados (línea `Total_Ingresos_Operación`), en vez del tramo de ventas declarado al SII.
- **Dónde se detectó:** commit `81cd560` ("Updates from Overleaf") en `docs/Memoria/chapters/chapter04.tex`, §5 (supuestos de estimación), sin acompañarse de una entrada en este log ni de una justificación adicional más allá de la cita a SCN 2025 §7.169 incluida en el propio texto.
- **Estado:** ⚠️ **Registrado retroactivamente por esta auditoría, no por los autores.** No hay evidencia en el repositorio de que esta decisión —ni la eliminación del supuesto de "remuneración media del sector financiero representativa"— haya sido evaluada frente a alternativas, ni de por qué se abandonó el enfoque anterior (tramo de ventas SII).
- **Alternativas no documentadas:** tramo de ventas SII (enfoque original); remuneración media sectorial (eliminado sin reemplazo aparente para D1 en los casos donde antes se usaba).
- **Acción pendiente:** solicitar a los autores que documenten aquí (o en un anexo metodológico) la razón del cambio y su impacto cuantitativo sobre los resultados ya publicados en versiones anteriores de la memoria.

## 2026-07-28 — Corrección manual de cifras en `chapter05.tex` sin corregir el dato fuente

- **Decisión (de facto, no explícita):** corregir el error aritmético H-01 (Cuadro "Agregado Total", fila 2025) editando directamente los valores en el `.tex` vía Overleaf, sin regenerar la hoja `🏦 Agregado Total` de `HuellaSocial_Consolidado.xlsx` ni el dashboard.
- **Razonamiento inferido:** no documentado. Es la corrección más simple y rápida ante una fecha de entrega, pero rompe la trazabilidad código→resultado exigida por `CLAUDE.md` ("los datos, tablas y figuras se generan una sola vez desde el código").
- **Alternativas consideradas:** ninguna registrada.
- **Riesgo:** el Excel fuente y el dashboard público siguen reproduciendo el valor erróneo (ver H-10, `docs/auditoria/02_reproduccion_calculos.md`). Cualquier verificación futura basada en el dashboard (citado en la memoria como repositorio de referencia) contradirá al texto ya corregido.
- **Acción pendiente:** corregir `HuellaSocial_Consolidado.xlsx` (ambos bloques: Agregado Total fila 2025, y N de Cuenta Financiera 2015–2024) y regenerar `dashboard_huellasocial.html` desde el dato corregido, en vez de mantener el parche solo en el texto.

## 2026-07-28 — Cambio en el criterio de deduplicación del panel DAES

- **Decisión:** el panel DAES pasa de 129 a 122 observaciones de P1, "tras excluir registros duplicados de carga de la misma cooperativa y año".
- **Estado:** ⚠️ Sin entrada de decision log de los autores. No se especifica el criterio exacto de deduplicación (¿cuál registro se conserva cuando hay duplicado? ¿por fecha de carga, por completitud de variables?). Corresponde a M-03 en `SOLICITUD_AUTORES.md`, aún no resuelto.

## 2026-07-29 — Decisión de no generar especificación de entorno (E-01)

- **Decisión:** los autores optaron explícitamente por no generar `requirements.txt`/`environment.yml` para `Dashboard_HuellaSocial`, dejando E-01 sin resolver "por decisión propia" (respuesta a `SOLICITUD_AUTORES.md`, ronda 2).
- **Razonamiento reportado:** ninguno más allá de la decisión misma.
- **Alternativas consideradas:** ninguna registrada.
- **Riesgo:** sin versiones fijadas de pandas/numpy/openpyxl, no hay garantía de reproducibilidad bit-a-bit del pipeline en otra máquina u otra fecha (las versiones de estas librerías cambian su comportamiento numérico/de parseo entre releases). Documentado como riesgo residual, no bloqueante, en `02_reproduccion_calculos.md`.

## 2026-07-29 — Corrección de causa raíz de H-01/H-10 verificada

- **Decisión:** corregir la fórmula de la hoja `🏦 Agregado Total` de `HuellaSocial_Consolidado.xlsx` que sumaba el total acumulado DAES a la fila 2025 (CMF-solo), y regenerar el dashboard desde el dato corregido, en vez de mantener el parche manual solo en el `.tex` de la memoria.
- **Verificación independiente:** confirmada por esta auditoría recalculando desde el Excel descargado (commit `37f6051`) y leyendo el HTML regenerado — ver H-10 en `docs/auditoria/02_reproduccion_calculos.md`.
- **Nota positiva:** este es el primer caso en la auditoría donde una corrección se propaga correctamente desde la causa raíz hasta todos los artefactos derivados (Excel → dashboard → memoria), cerrando la brecha de trazabilidad señalada en la entrada anterior de este log.

---

*Este log fue iniciado por el Research Engineering Assistant en julio 2026 al detectar, durante la Fase 2 de la auditoría de Ureta & Ruiz Tagle (2026), decisiones metodológicas incorporadas al repositorio sin registro. Los autores deben mantenerlo actualizado hacia adelante.*
