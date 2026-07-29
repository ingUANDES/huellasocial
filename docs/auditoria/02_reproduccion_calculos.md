# FASE 2 — Reproducción de cálculos
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Estado: 🟡 PARCIALMENTE EJECUTADA** (D-02/D-03/C-02/C-05 disponibles vía `Dashboard_HuellaSocial`; siguen faltando D-04, D-06, D-07, D-08, C-01, C-03, C-04, E-01/E-02/E-03)

---

## 0. Insumos usados

- Repo `Iureta1/Dashboard_HuellaSocial`, commit `6f652dd9fb02e528759c6678ea8ee4a3533c4651` ("fix excel", 2026-07-26).
- `HuellaSocial_Consolidado.xlsx` (= D-02 + D-03 + parte de D-08).
- `Dashboard_cuentasatelite.py` (= C-02 + C-04 + C-05, parcial).
- Ejecutado con `python3 Dashboard_cuentasatelite.py` (pandas/numpy/openpyxl recién instalados; **no hay E-01/E-02/E-03**, por lo que no se puede certificar que las versiones usadas aquí coincidan con las de los autores — riesgo residual de reproducibilidad numérica de bajo orden).
- El script no recalcula el Cuadro "Agregado Total" desde el panel CMF+DAES: lo **lee directamente** de la hoja `🏦 Agregado Total` de `HuellaSocial_Consolidado.xlsx` (línea 97 de `Dashboard_cuentasatelite.py`: `df_total_raw = parse_sheet(xls_hs, "🏦 Agregado Total", 2)`). Es decir, C-02/C-05 no son el pipeline de cálculo del agregado total — son un formateador de una tabla ya calculada en el Excel. El pipeline real que produce esa hoja (equivalente a C-01) **no está en el repositorio**.

---

## 1. Confirmación de H-01 en el dato fuente

El hallazgo H-01 (`01_consistencia_interna.md`) se verificó aritméticamente desde el PDF de la memoria. Con el Excel fuente ahora disponible, se confirma que **el error no es un error de transcripción al PDF: está en el dato fuente mismo**.

Fila 2025 de la hoja `🏦 Agregado Total` (leída directamente con `pandas.read_excel`):

| Variable | Excel fuente (hoja `Agregado Total`, fila 2025) | Valor correcto (= hoja `Agregados CMF`, 2025) | Diferencia |
|---|---|---|---|
| N | 7 | 7 | — |
| P1 | 577.398,585301 | 445.885,0 | 131.513,585 |
| B1g | 359.372,879491 | 277.518,824 | 81.854,055 |
| D1 | 167.736,101867 | 122.763,2 | 44.972,902 |
| B2g | 191.636,777624 | 154.755,624 | 36.881,154 |
| Aporte (%) | 0,105705 | 0,081628 | — |

Estos valores son **exactamente** los que la auditoría (Fase 1, H-01) había predicho desde el PDF, con seis cifras decimales de coincidencia. Confirma el mecanismo hipotetizado: la fila 2025 del agregado total suma el total acumulado 2014–2024 del panel DAES a los valores CMF de 2025, en lugar de dejar 2025 como CMF-solo.

**Hallazgo adicional — mismo error en la Cuenta Financiera:** la hoja `🏦 Agregado Total` (segundo bloque, "CUENTA FINANCIERA") reporta **N = 7 para todos los años 2015–2024**, cuando el universo correcto para esos años incluye DAES (14, 16, 19, 21, 13, 17, 17, 26, 29, 18 respectivamente — ver más abajo). Este error de conteo **no fue identificado en la Fase 1** porque no era verificable solo desde el PDF original de la memoria (el PDF original también tenía N=7 para todos esos años, de forma consistente con el Excel — ver §2).

---

## 2. Descubrimiento: la memoria fue corregida a mano el 2026-07-28, sin corregir el dato fuente

Al revisar el historial de `docs/Memoria/chapters/chapter05.tex` se encontró el commit `81cd560` ("Updates from Overleaf", Sebastián Cea, 2026-07-28 16:18 -04:00) — **posterior a la Fase 1 de esta auditoría y anterior a esta Fase 2**. Este commit:

1. **Corrige exactamente H-01**: la fila 2025 del Cuadro "resultados_total" pasa de `577.398,6 / 359.372,9 / 167.736,1 / 191.636,8 / 113.142,2 / 0,47` a `445.885,0 / 277.518,8 / 122.763,2 / 154.755,6 / 108.265,0 / 0,44` — idéntico al valor CMF-solo que esta auditoría había recomendado.
2. **Corrige el N de la Cuenta Financiera** para 2015–2024 (antes uniformemente 7; ahora 14, 14, 14, 17, 13, 16, 15, 22, 25, 18).
3. **Corrige el aporte estimado 2025** en el Cuadro de validación externa: de 0,106 % a 0,082 % (compárese con el 0,087 % recalculado de forma independiente en H-01 — la pequeña diferencia se debe a que el PIB 2025 usado en el Excel, 339.978.000, difiere levemente del PIB 2025 "≈320.000.000" usado como aproximación en H-01; **el valor 0,082 % de la memoria corregida es el correcto**).
4. Cambia un supuesto metodológico central: la proxy de P1 pasa de "tramo de ventas del SII" a "ingresos operacionales del estado de resultados (línea `Total_Ingresos_Operación`)", y elimina el supuesto de "remuneración media del sector financiero representativa".
5. Cambia el N de observaciones DAES de 129 a 122 ("tras excluir registros duplicados de carga de la misma cooperativa y año").
6. Cambia el conteo regional de cooperativas (Figura de distribución regional): de 42 a 39 organizaciones en total (ver `gen_figs_5_4.py`, región Metropolitana 22→20, Valparaíso 5→4).

**Problema crítico de reproducibilidad — los números corregidos de la memoria NO son reproducibles desde el repositorio `Dashboard_HuellaSocial`:**

- El Excel (`HuellaSocial_Consolidado.xlsx`, commit `6f652dd9`, fechado 2026-07-26, **anterior** al commit de corrección de la memoria) **sigue teniendo el error** en ambas hojas (Agregado Total fila 2025, y N de Cuenta Financiera 2015–2024).
- El dashboard público (`dashboard_huellasocial.html`, regenerado en esta auditoría con el mismo Excel) **sigue mostrando el valor erróneo** (577.398,6 / 359.372,9 / 0,106 %) para 2025.
- Es decir: los autores corrigieron el **texto** de la memoria a mano en Overleaf, con los valores correctos, pero **no corrigieron el dato fuente ni el dashboard**. Hoy existen tres versiones distintas de la misma cifra circulando simultáneamente en el ecosistema del proyecto: memoria (correcta, 277.518,8), Excel/dashboard (incorrecta, 359.372,9), y esta auditoría (que señaló el error y coincide con la memoria corregida).

**Esto viola dos reglas de `CLAUDE.md`:**
- *"Cambios de contenido siempre se hacen en el repositorio, nunca en Overleaf"* — el flujo real fue inverso: la corrección se hizo en Overleaf y se sincronizó al repositorio como texto estático, no como resultado de recalcular desde datos/código corregidos.
- *Regla anti-duplicación (§Integración con Quarto y Overleaf, punto 1)*: los resultados deben generarse **una sola vez** desde el código; aquí se generaron dos veces con dos resultados distintos (Excel/dashboard vs. texto de memoria), y no hay ninguna referencia cruzada ni control de versión que reconcilie ambas.

**Nuevo hallazgo — H-10 (🔴 CRÍTICO):** El error aritmético de H-01 sigue vivo en el dato fuente (`HuellaSocial_Consolidado.xlsx`) y en el dashboard público, pese a que el texto de la memoria ya fue corregido. Cualquier lector que consulte el dashboard (citado en la memoria, nota al pie 4, como el repositorio público de referencia) verá una cifra de aporte al PIB para 2025 (0,106 %) que la propia memoria ya reconoce como incorrecta (0,082 %). Acción requerida: corregir la hoja `🏦 Agregado Total` en el Excel fuente (ambos bloques) y regenerar `dashboard_huellasocial.html`, en vez de mantener el parche manual solo en el `.tex`.

---

## 3. Verificación del resto del panel Agregado Total (2013–2024)

Excluyendo la fila 2025 (H-01/H-10), se compararon las 12 filas restantes (2013–2024) del Excel fuente contra el Cuadro `resultados_total` del `chapter05.tex` post-corrección (commit `81cd560`): **coinciden exactamente**, cifra por cifra, incluyendo decimales redondeados a una cifra. No se detectan errores adicionales en esas filas.

De igual forma, la fila 2025 de la hoja `🏦 Agregados CMF` (445.885,0 / 277.518,824 / 122.763,2 / 154.755,624 / 108.265,0 / 0,081628) coincide exactamente con el Cuadro 5.5 (CMF) reportado en la memoria — este cuadro nunca tuvo el error, consistente con el diagnóstico de H-01.

---

## 4. Pendiente para completar la Fase 2

- **C-01** (pipeline de integración de fuentes): no está en `Dashboard_HuellaSocial`. Sin él, no se puede auditar cómo se llegó a los valores CMF/DAES por entidad (solo se puede verificar la agregación desde el panel ya consolidado).
- **D-04 a D-08, E-01/E-02/E-03**: siguen sin entregarse.
- Pendiente confirmar con los autores: ¿la corrección del 2026-07-28 fue hecha en respuesta a este hallazgo (H-01) u obtenida de forma independiente? ¿Existe una versión corregida de `HuellaSocial_Consolidado.xlsx` que aún no se ha subido a `Dashboard_HuellaSocial`?

---

*Fase 2 ejecutada julio 2026, tras la incorporación de `Dashboard_HuellaSocial` como insumo. Ver `00b_relacion_repositorios.md` para el mapeo de repositorios y `01_consistencia_interna.md` para H-01 original.*
