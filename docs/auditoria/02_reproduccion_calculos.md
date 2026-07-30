# FASE 2 — Reproducción de cálculos
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Estado: 🟢 SUSTANCIALMENTE COMPLETA** (H-01/H-10 corregidos y verificados en el dato fuente y el dashboard; D-06 verificado; C-01/C-03/E-02/E-03 documentados en `Dashboard_HuellaSocial`. Sigue pendiente: D-04 (registrar URL + respaldo externo, no subir el binario — ver corrección de criterio 2026-07-30), D-07, y verificar en `huellasocial` los cambios de texto que los autores reportan haber hecho — ver §5)

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

**Hallazgo H-10 (🔴 CRÍTICO):** El error aritmético de H-01 sigue vivo en el dato fuente (`HuellaSocial_Consolidado.xlsx`) y en el dashboard público, pese a que el texto de la memoria ya fue corregido. Cualquier lector que consulte el dashboard (citado en la memoria, nota al pie 4, como el repositorio público de referencia) verá una cifra de aporte al PIB para 2025 (0,106 %) que la propia memoria ya reconoce como incorrecta (0,082 %). Acción requerida: corregir la hoja `🏦 Agregado Total` en el Excel fuente (ambos bloques) y regenerar `dashboard_huellasocial.html`, en vez de mantener el parche manual solo en el `.tex`.

### H-10 — RESUELTO Y VERIFICADO (commits `6fca63e` y `37f6051`, `Dashboard_HuellaSocial`, 2026-07-29)

Los autores reportaron haber ubicado la causa raíz (una fórmula en la hoja `Agregado Total` que apuntaba a la fila de total acumulado del panel DAES en vez de dejar 2025 como CMF-solo) y corregido el Excel y el dashboard. Se verificó de forma independiente, re-descargando el repositorio y re-ejecutando la cadena completa:

| Verificación | Resultado |
|---|---|
| Fila 2025, hoja `Agregado Total` (bloque producción) | P1 = 445.885,0 · P2 = 168.366,176 · B1g = 277.518,824 · D1 = 122.763,2 · B2g = 154.755,624 · Rem = 108.265,0 · D1/B1g = 0,44236 — **idéntico a la hoja `Agregados CMF` y a la memoria corregida** |
| Bloque Cuenta Financiera, N por año 2015–2024 | 14, 14, 14, 17, 13, 16, 15, 22, 25, 18 — **coincide exactamente** con lo ya corregido en el `.tex` (commit `81cd560`) |
| `dashboard_huellasocial.html` regenerado y leído programáticamente | `total_agg` 2025: N=7, P1=445.885,0, B1g=277.518,824, Aporte = 0,0816 % — consistente con el 0,082 % de la memoria (la diferencia de milésimas es redondeo). Las cadenas `577398`, `359372`, `0.1057` (huellas del valor erróneo) **no aparecen en ningún lugar del HTML**. |

**Conclusión:** H-01/H-10 quedan **cerrados**. Esta es la primera vez en esta auditoría que un hallazgo crítico se corrige de punta a punta (causa raíz → dato fuente → artefacto público) y se verifica de forma independiente y reproducible. Buen manejo por parte de los autores.

---

## 3. Verificación del resto del panel Agregado Total (2013–2024)

Excluyendo la fila 2025 (H-01/H-10), se compararon las 12 filas restantes (2013–2024) del Excel fuente contra el Cuadro `resultados_total` del `chapter05.tex` post-corrección (commit `81cd560`): **coinciden exactamente**, cifra por cifra, incluyendo decimales redondeados a una cifra. No se detectan errores adicionales en esas filas.

De igual forma, la fila 2025 de la hoja `🏦 Agregados CMF` (445.885,0 / 277.518,824 / 122.763,2 / 154.755,624 / 108.265,0 / 0,081628) coincide exactamente con el Cuadro 5.5 (CMF) reportado en la memoria — este cuadro nunca tuvo el error, consistente con el diagnóstico de H-01.

---

## 4. Respuesta de los autores a `SOLICITUD_AUTORES.md` (2026-07-29) — verificación ítem por ítem

Los autores reportaron por escrito haber resuelto la mayoría de los insumos pendientes. Se verificó cada uno contra el estado real de los repositorios (`Dashboard_HuellaSocial` @ `37f6051`, `huellasocial` @ `8699f59`):

| # | Ítem | Reportado por los autores | Verificación independiente |
|---|------|---------------------------|----------------------------|
| D-06 | Fuente de α = 0,3776 | Suma de la columna de coeficientes técnicos directos, actividad 94, MIP 111×111 (BCCh 2018) | ✅ **VERIFICADO**: se agregó `2018_MIP_111x111.xlsx` a `Dashboard_HuellaSocial` (commit `37f6051`). Se recalculó directamente: hoja "2" (Matriz de coeficientes directos), columna de actividad 94 (glosa confirmada: "Intermediación financiera"), suma de los 111 valores = **0,3776461...** — coincide con α a 4 decimales. |
| C-01 | Pipeline de integración | Documentado en el Readme de `Dashboard_HuellaSocial`: cruce por RUT normalizado, fórmulas explicadas | 🟡 **PARCIAL**: el Readme ahora aclara honestamente que **no existe un script** — los cuadros 5.2–5.9 son fórmulas de Excel transcritas manualmente al LaTeX ("no existe un script que genere esos cuadros directamente"). Esto es una mejora de transparencia real, pero no resuelve el riesgo estructural: la transcripción manual Excel→LaTeX es exactamente el tipo de paso que produjo H-01/H-10. Se recomienda automatizar esa transcripción (script que lea el Excel y genere el `.tex` de las tablas) para eliminar el riesgo de raíz, no solo documentarlo. |
| C-03 | Script de cuenta financiera | Documentado como fórmulas de Excel, no script independiente | ✅ Coherente con el hallazgo de C-01 — mismo mecanismo, correctamente documentado ahora. |
| C-04 | Script de figuras | Ya actualizado, sin cambios necesarios | ✅ Consistente: `gen_figs_5_4.py` ya reflejaba los conteos corregidos desde el commit `81cd560` (2026-07-28), antes de esta respuesta. |
| E-02 | Versión de Python | 3.11.5 | ✅ Documentado en el Readme de `Dashboard_HuellaSocial` ("Entorno de ejecución"). |
| E-03 | Sistema operativo | Windows, sin versión de build | ✅ Documentado en el mismo bloque del Readme. |
| E-01 | `requirements.txt`/`environment.yml` | Decisión de no generarlo | ⚠️ Aceptado como decisión, pero **sin registrar en `decision_log.md`** — agregado retroactivamente por esta auditoría (ver abajo). Sigue siendo un riesgo real: sin fijar versiones de pandas/numpy/openpyxl, no hay garantía de que este mismo script reproduzca bit-a-bit los resultados en otra máquina. |
| D-04 | `PUB_NOMBRES_PJ.txt` | Disponible, pendiente de subir | 🟡 **Requisito corregido (2026-07-30):** no es necesario subir el binario al repositorio (mala práctica de gestión de repos git). Basta con registrar la URL original del portal SII y la ubicación del respaldo externo en `data/metadata/fuentes_externas.md` (creado por esta auditoría). Pendiente que los autores completen ambos datos — sin ellos, sigue sin poder verificarse el subtipo 817 (CAC) contra el registro SII. |
| D-07 | Extracto CMF-BEST crudo | No reportado en la respuesta | 🔴 Sigue pendiente, no mencionado. |
| D-06 (cita en memoria), D-08 (fecha de acceso CMF), M-01/M-03 (§4.3.1) | Cambios de texto en la memoria (`docs/Memoria/`) | Reportados como ya incorporados | 🔴 **NO VERIFICABLE TODAVÍA**: a la fecha de esta revisión, el repositorio `huellasocial` (rama `main`, HEAD `8699f59`) no tiene commits posteriores a `81cd560`/`e2eed60` que toquen `docs/Memoria/`. Es decir, estos cambios de texto existen (según los autores) en Overleaf o localmente, pero **no han sido sincronizados al repositorio** — la misma brecha de trazabilidad que produjo H-10 originalmente. Se solicita a los autores subir estos cambios al repo antes de darlos por cerrados. |
| M-02 | Criterio de extracción P1/D1 desde PDFs DAES | Ya cubierto en §4.3.2, sin cambios | ⚪ No verificable de forma independiente sin el commit correspondiente (mismo problema que el punto anterior), pero no se objeta la afirmación. |
| M-04 | Fuente del PIB | Ya cubierto, título de tabla y fecha de acceso agregados en D-08 | ⚪ Mismo caso: depende de la sincronización de D-08 al repositorio. |

**Hallazgo H-11 (🟡 IMPORTANTE) — brecha recurrente entre lo reportado y lo versionado:** por segunda vez en esta auditoría (la primera fue H-10), los autores reportan cambios de contenido de la memoria que aún no existen como commits en `huellasocial`. Se recomienda establecer como práctica mínima: ningún ítem de `SOLICITUD_AUTORES.md` se marca ✅ resuelto hasta que el commit correspondiente sea visible en el repositorio, no solo reportado por chat.

---

## 5. Pendiente para completar la Fase 2

- **D-04**: no requiere subir el archivo — registrar URL SII + respaldo externo en `data/metadata/fuentes_externas.md` (pendiente que los autores completen la tabla). **D-07**: sigue sin entregarse.
- **Sincronización pendiente**: los cambios de texto reportados para D-06/D-08/M-01/M-03/M-02/M-04 en la memoria deben verse reflejados en un commit de `huellasocial` antes de considerarse cerrados.
- **C-01/C-03**: documentados honestamente como inexistentes (fórmulas de Excel + transcripción manual). Recomendación abierta: automatizar la generación de las tablas LaTeX desde el Excel para eliminar el riesgo de transcripción manual que originó H-01.
- **E-01**: decisión de no generar especificación de entorno, ahora registrada en `decision_log.md`, pero sigue siendo un riesgo de reproducibilidad de severidad media.

---

*Fase 2 ejecutada julio 2026, tras la incorporación de `Dashboard_HuellaSocial` como insumo, y actualizada tras la respuesta de los autores a `SOLICITUD_AUTORES.md` (2026-07-29). Ver `00b_relacion_repositorios.md` para el mapeo de repositorios y `01_consistencia_interna.md` para H-01 original.*
