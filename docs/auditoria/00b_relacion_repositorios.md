# Anexo a FASE 0 — Relación entre los tres repositorios del ecosistema Huella Social

**Fecha:** julio 2026
**Objetivo:** mapear cómo se relacionan `huellasocial` (Research OS), `huellasocialdata` (datos) y
`Dashboard_HuellaSocial` (visualización), como paso previo a reabrir las Fases 2–3 de la auditoría
de Ureta & Ruiz Tagle (2026), ahora que `Dashboard_HuellaSocial` está disponible localmente.

---

## 1. Los tres repositorios, en una tabla

| Repositorio | Remoto real | Rol declarado en PROJECT.md | Rol real (verificado) |
|---|---|---|---|
| `huellasocial` | `ingUANDES/huellasocial` | Plataforma, análisis, documentación científica | Documentación, memoria (PDF+.Rtex), auditoría. **`src/`, `data/`, `analysis/` están vacíos** (solo `.gitkeep`) — ningún pipeline vive aquí todavía |
| `huellasocialdata` | `ingUANDES/huellasocialdata` | *(no aparece con este nombre en PROJECT.md)* | Es, verificado por `git log` (`Merge branch 'main' of github.com:viantirreau/donaciones`), **el mismo repositorio que PROJECT.md llama "donaciones" (`viantirreau/donaciones`)**, ahora vive bajo la organización `ingUANDES` con otro nombre |
| `Dashboard_HuellaSocial` | `Iureta1/Dashboard_HuellaSocial` | No listado en PROJECT.md como repo del proyecto; solo citado en la memoria (nota 4, §4.4, §5.1) | Contiene el **código y los datos reales** que producen las cifras del capítulo 5 de la memoria |

**Hallazgo de inconsistencia (§ CLAUDE.md "Señales de alerta"):** la tabla "Repositorios del
proyecto" de `PROJECT.md` (líneas 65–72) está desactualizada en dos frentes:
1. Nombra `viantirreau/donaciones` pero el repo operativo es `ingUANDES/huellasocialdata`.
2. No incluye `Iureta1/Dashboard_HuellaSocial`, pese a que es el repositorio que contiene todo el
   código y los datos del único output científico completado del proyecto (la memoria 2026).

---

## 2. Qué contiene cada uno, y si se relaciona con la memoria auditada

### `huellasocialdata` (= "donaciones") — **NO es la fuente de datos de la memoria**
Contiene tres pipelines ETL independientes, todos sobre **donaciones y registro legal de OSC**, no
sobre cooperativas de ahorro y crédito (CAC):
- `registros19862/` — transferencias bajo Ley 19.862 (SII/portal público)
- `donaciones_mds/` — donaciones sociales, Ministerio de Desarrollo Social (Ley 19.885)
- `registro_civil_ong/` — Registro Nacional de Personas Jurídicas sin Fines de Lucro
- `notebooks/extract_persona_juridica_ruts.ipynb` → genera `sii_company_timeseries.parquet`

**Punto de falsa coincidencia a vigilar:** este notebook genera un archivo con el **mismo nombre**
(`sii_company_timeseries.parquet`) que el insumo **D-05** solicitado en `SOLICITUD_AUTORES.md` para
la memoria. Pero el de `huellasocialdata` está **filtrado por RUTs de donatarios de Ley 19.862/MDS**,
no por RUTs de cooperativas de ahorro y crédito. Son archivos homónimos con poblaciones distintas.
Si en la Fase 2 aparece un archivo con ese nombre, **hay que verificar el universo de RUTs antes de
asumir que es el insumo correcto** — de lo contrario se reproduciría un cálculo con la muestra
equivocada sin que ningún test lo detecte.

Conclusión: `huellasocialdata` es un repositorio **hermano, paralelo, no una dependencia** de la
memoria de Ureta & Ruiz Tagle. Sirve a la Línea 2 de investigación abierta en el roadmap ("Eficiencia
de la distribución de donaciones"), no al módulo de cuentas satélite de CAC.

### `Dashboard_HuellaSocial` — **es la fuente real de código y datos de la memoria**
- `Dashboard_cuentasatelite.py` (1788 líneas): implementa el pipeline P2 = α·P1 (α = 0,3776, MIP
  Chile 2018 sector 94), agrega Panel CMF y Panel DAES, y genera `dashboard_huellasocial.html`.
  Contiene comentarios de changelog propios (v3.2, v4.0, "Feb 2026") que documentan al menos tres
  correcciones post-hoc sobre filtrado de filas de totales — **relevante para la Fase 3**, porque
  errores de ese tipo (filtrar mal una fila de "TOTAL") son exactamente los que producen el tipo de
  discrepancia aritmética ya detectado como H-01 en `01_consistencia_interna.md`.
- `HuellaSocial_Consolidado.xlsx`: hojas `📁 Panel CMF`, `📁 Panel DAES`, `🏦 Agregados CMF`,
  `📊 Agregados DAES` (cada una con dos tablas apiladas: Cuenta de Producción + Cuenta Financiera).
  Corresponde a los insumos **D-02 y D-03** de `SOLICITUD_AUTORES.md`.
- `Consolidado_cooperativas.xlsx`: corresponde al insumo **D-01**.
- **No hay** `requirements.txt` ni especificación de entorno (insumos **E-01/E-02/E-03** siguen
  pendientes) — el `Readme.md` solo indica `pip install pandas numpy openpyxl` sin fijar versiones.
- **No hay** commit SHA documentado que corresponda a la versión usada en la defensa de la memoria
  (la nota al pie de `SOLICITUD_AUTORES.md`, ítem B, ya señalaba este riesgo). El repo tiene commits
  posteriores a cualquier fecha plausible de entrega ("fix excel", "arreglo regional") que sugieren
  que el dashboard **siguió cambiando después de escrita la memoria** — esto debe verificarse en
  Fase 2 comparando fechas de commit vs. fecha de entrega de la memoria.

Con esto, **D-01, D-02, D-03 y parte de C-01/C-02/C-04/C-05 quedan desbloqueados**. Siguen faltando:
D-04 (`PUB_NOMBRES_PJ.txt`), D-06 (extracto MIP BCCh para α), D-07 (CMF-BEST crudo), D-08 (series de
validación externa), y toda la especificación de entorno (E-01–E-03).

### `huellasocial` — el Research OS
Aloja la memoria (`docs/Memoria/memoria.Rtex` + PDF), el `AUDIT_PROTOCOL.md`, y los outputs de
auditoría ya producidos (`docs/auditoria/00`–`06`, `SOLICITUD_AUTORES.md`). No aloja código de
análisis propio: `src/ingestion`, `src/indicators`, `src/viz` y `data/` están vacíos. Esto es
consistente con el diagnóstico ya registrado en `00_mapa_reproducibilidad.md` (H-02) y con el
milestone M2 del roadmap ("Pipeline computacional reproducible", aún no iniciado).

---

## 3. Cadena de dependencia real (no la declarada en PROJECT.md)

```
Dashboard_HuellaSocial (Iureta1)          huellasocialdata (ingUANDES, = donaciones)
  Consolidado_cooperativas.xlsx      │      registros19862 / donaciones_mds / registro_civil_ong
  HuellaSocial_Consolidado.xlsx      │      → alimenta Línea 2 del roadmap (DEA sobre donaciones),
  Dashboard_cuentasatelite.py        │        NO la memoria de CAC
        │                            │
        ▼                            │
  dashboard_huellasocial.html        │
  (Cuadros y Figuras Cap. 5)         │
        │                            │
        ▼                            ▼
  docs/Memoria/memoria.Rtex   ←  (sin conexión de datos)
        │
        ▼
  huellasocial/docs/auditoria/*  (esta auditoría)
```

`huellasocialdata` y la memoria auditada **no comparten datos hoy**. Comparten only el paraguas
institucional (Huella Social / mismo equipo) y, potencialmente, metodología futura (DEA) si se
ejecuta la Línea 2 del roadmap.

---

## 4. Propuesta de actualización a `AUDIT_PROTOCOL.md`

El protocolo (§2, "Insumos que la auditoría necesita") asume implícitamente que documento, datos y
código viven en *un* repositorio. En un ecosistema de múltiples repos como Huella Social eso no es
cierto y puede llevar a declarar HUÉRFANO algo que en realidad existe en un repo hermano, o a
mezclar datos homónimos de repos distintos (ver el caso `sii_company_timeseries.parquet` arriba).

Se propone agregar a `AUDIT_PROTOCOL.md`, al final de §2, un apartado nuevo:

> **2.1 Ecosistemas multi-repositorio**
> Cuando el documento referencie repositorios externos (notas al pie, URLs de GitHub), la Fase 0
> debe: (a) clonar cada repositorio referenciado fuera del repo principal, (b) registrar el commit
> SHA exacto usado en la auditoría, (c) verificar si el repositorio realmente corresponde a los
> datos/código de la memoria o si es un repo hermano no relacionado (mismo equipo, distinto
> propósito), y (d) señalar homónimos de archivos entre repos como riesgo de trazabilidad, no
> asumir que un nombre de archivo idéntico implica el mismo contenido.

Quedo a la espera de confirmación antes de escribir este cambio en `AUDIT_PROTOCOL.md` — es un
documento normativo y el CLAUDE.md pide tratar cambios a estos documentos como decisiones a
registrar, no ediciones silenciosas.

---

## 5. Estado para la Etapa 2 (reapertura de Fases 2–3)

| Insumo | Estado tras este mapeo |
|---|---|
| D-01 Consolidado_cooperativas.xlsx | ✅ Disponible |
| D-02 Panel DAES | ✅ Disponible (dentro de `HuellaSocial_Consolidado.xlsx`) |
| D-03 Panel CMF | ✅ Disponible (dentro de `HuellaSocial_Consolidado.xlsx`) |
| D-04 PUB_NOMBRES_PJ.txt | ❌ Sigue pendiente |
| D-05 sii_company_timeseries.parquet | ⚠️ Homónimo existe en `huellasocialdata`, pero con población equivocada (donatarios, no CAC) — **no usar** sin confirmación de los autores |
| D-06 Extracto MIP BCCh (α=0,3776) | ❌ Sigue pendiente |
| D-07 CMF-BEST crudo | ❌ Sigue pendiente |
| D-08 Series de validación externa | ❌ Sigue pendiente |
| C-01 a C-05 (código) | ✅ Disponibles en `Dashboard_HuellaSocial` (sin commit SHA fijado a la fecha de la memoria) |
| E-01/E-02/E-03 (entorno) | ❌ Sigue pendiente — el Readme solo da un `pip install` sin versiones |

**Recomendación:** con lo disponible ya se puede ejecutar `Dashboard_cuentasatelite.py` y comenzar la
Fase 2 (tabla `cifra_reportada | valor_reproducido | coincide | delta`) para D-01/D-02/D-03, que es
justamente lo que la lista de prioridad de `SOLICITUD_AUTORES.md` marcaba como 🔴 Urgente. D-04, D-06,
D-07, D-08 y el entorno exacto siguen bloqueando una Fase 2 *completa* y toda la Fase 3 que dependa
de esos insumos (p. ej. validar α o el Cuadro 5.9).
