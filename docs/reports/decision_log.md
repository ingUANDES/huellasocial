# Decision Log — Huella Social

> Registro de decisiones metodológicas relevantes, conforme a `CLAUDE.md` §"Decisiones de investigación". Cada entrada: fecha, decisión, razonamiento, alternativas consideradas, quién decidió.

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

---

*Este log fue iniciado por el Research Engineering Assistant en julio 2026 al detectar, durante la Fase 2 de la auditoría de Ureta & Ruiz Tagle (2026), decisiones metodológicas incorporadas al repositorio sin registro. Los autores deben mantenerlo actualizado hacia adelante.*
