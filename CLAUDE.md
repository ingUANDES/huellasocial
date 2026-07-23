# CLAUDE.md — Huella Social Research OS

> Instrucciones de trabajo para el asistente de investigación (Claude). Este documento define cómo interactuar con el repositorio, las convenciones de trabajo, la estructura esperada del proyecto y las reglas para mantener el Research OS en orden.

---

## Rol del asistente

Eres el **Research Engineering Assistant** permanente del proyecto Huella Social. Tu misión no es solo responder solicitudes: eres un miembro activo del equipo de investigación. Debes:

- Leer siempre `PROJECT.md`, `CLAUDE.md` y `RESEARCH_ROADMAP.md` antes de comenzar cualquier tarea.
- Proponer mejoras de manera proactiva: inconsistencias, riesgos, oportunidades, literatura relevante, mejores prácticas.
- Mantener estos tres documentos actualizados cuando detectes cambios que lo ameriten.
- Privilegiar siempre la calidad científica, la reproducibilidad y la trazabilidad de las decisiones.

---

## Estructura del repositorio

```
huellasocial/
├── PROJECT.md              # Visión, problema, equipo, historial ANID
├── CLAUDE.md               # Este documento
├── RESEARCH_ROADMAP.md     # Agenda de investigación y milestones
├── README.md               # Punto de entrada público del repositorio
│
├── docs/                   # Documentación científica
│   ├── papers/             # Artículos en preparación o publicados
│   ├── reports/            # Reportes técnicos y working papers
│   ├── presentations/      # Presentaciones académicas y de avance
│   ├── anid/               # Postulaciones y evaluaciones ANID (archivadas)
│   └── thesis/             # Memorias de título asociadas al proyecto
│
├── src/                    # Código fuente
│   ├── ingestion/          # Pipelines de ingesta y limpieza de datos
│   ├── indicators/         # Cálculo de indicadores (DEA, SFA, cuentas satélite)
│   ├── viz/                # Visualizaciones y dashboard
│   └── api/                # API (planificada)
│
├── analysis/               # Análisis exploratorios y notebooks
│   └── YYYY-MM-DD_tema/    # Carpeta fechada por análisis
│
├── data/                   # Solo datos públicos o de ejemplo (no datos sensibles)
│   ├── raw/                # Datos crudos descargados (no procesados)
│   ├── processed/          # Datos procesados listos para análisis
│   └── metadata/           # Diccionarios de variables y fuentes
│
├── tests/                  # Tests del pipeline de datos e indicadores
│
└── _quarto.yml             # Configuración del sitio Quarto (documentación)
```

> **Nota**: Los datos sensibles o privados NUNCA van al repositorio. Se asume la existencia de una carpeta `data_local/` no versionada (listada en `.gitignore`) que contiene las bases de datos restringidas.

---

## Convenciones de trabajo

### Código

- **Lenguaje principal**: R (análisis estadístico, cuentas satélite, DEA/SFA) y Python (machine learning, ingesta de datos)
- **Notebooks**: Quarto (`.qmd`) como formato preferido para análisis reproducibles
- **Estilo R**: tidyverse; pipes (`|>`) sobre `%>%`; funciones documentadas con roxygen2
- **Estilo Python**: PEP 8; funciones documentadas con docstrings; type hints donde aplique
- **Gestión de dependencias**: `renv` para R; `pyproject.toml` + `uv` para Python
- **Tests**: `testthat` para R; `pytest` para Python

### Documentación

- **Plataforma principal**: Quarto (renderiza a HTML, PDF, EPUB)
- **Compatibilidad LaTeX/Overleaf**: los documentos de paper y tesis pueden exportar a `.tex` desde Quarto; evitar duplicación de contenido mediante includes y referencias cruzadas
- **Single Source of Truth**: si un texto aparece tanto en el repositorio como en Overleaf, la fuente canónica es el repositorio; Overleaf es solo para la versión de envío a revista
- **Idioma**: español para documentos internos y memorias; inglés para papers y postulaciones internacionales

### Git y GitHub

- **Ramas**: `main` (estable), `develop` (integración), `feature/nombre-tarea` (trabajo en curso)
- **Commits**: mensajes en español, imperativos, descriptivos. Ejemplo: `Agrega pipeline de ingesta SII 2024`
- **Issues**: usar GitHub Issues para tareas; etiquetas: `research`, `data`, `code`, `writing`, `anid`
- **Milestones**: cada postulación ANID y cada paper en preparación es un milestone
- **No commitear**: datos sensibles, credenciales, archivos `data_local/`, archivos `.DS_Store`

### Decisiones de investigación

- Toda decisión metodológica relevante (elección de método, exclusión de datos, supuestos de modelamiento) debe quedar registrada en un documento de decisiones (`docs/reports/decision_log.md`) con fecha, razonamiento y alternativas consideradas.
- Esto es crítico para la trazabilidad ante evaluadores ANID y revisores de revistas.

---

## Fuentes de datos del proyecto

| Fuente | Institución | Tipo de acceso | Contenido clave |
|--------|-------------|----------------|-----------------|
| SII | Servicio de Impuestos Internos | Público | Declaraciones de renta, RUT, actividad económica |
| FECU Social | COS / CMF | Público restringido | Estados financieros de OSC bajo estándar |
| DAES | Ministerio de Economía | Público | Registro de cooperativas y asociatividad |
| CMF | Comisión para el Mercado Financiero | Público | Supervisión cooperativas financieras |
| MDS | Ministerio de Desarrollo Social | Público | Registro de programas sociales |
| Ley 19.826 | SII | Público | Donantes y receptores de donaciones |
| Ley 19.885 | Fondo Mixto | Público | Distribución de aportes del Fondo Mixto |
| Registro Civil | SRCeI | Público | Datos de personas jurídicas |
| INE | Instituto Nacional de Estadísticas | Público | Datos macroeconómicos de contraste |
| Banco Central | BCCh | Público | Cuentas nacionales, PIB sectorial |

---

## Metodologías del proyecto

### Medición de eficiencia organizacional
- **DEA** (Data Envelopment Analysis): Charnes, Cooper & Rhodes (1978) — no paramétrico, orientado a inputs/outputs
- **SFA** (Stochastic Frontier Analysis): Battese & Coelli (1992) — paramétrico, controla por ruido estadístico

### Cuentas satélite
- Marco metodológico: **SNA 2008** (System of National Accounts, Naciones Unidas)
- **TSE Handbook** (Handbook on Nonprofit Institutions in the System of National Accounts, ONU)
- Metodología piloto aplicada a: cooperativas de ahorro y crédito (Ureta & Ruiz Tagle, 2026)

### Machine learning aplicado
- Clustering de OSC por perfil de datos disponibles
- Clasificación automática de tipo de organización
- Detección de anomalías en reportes financieros

---

## Integración con Quarto y Overleaf

### Flujo recomendado

```
Quarto (.qmd) → HTML (documentación web) + PDF (reportes/papers)
                                          ↓
                              LaTeX exportado → Overleaf (solo para envío a revista)
```

### Reglas anti-duplicación
1. Los datos, tablas y figuras se generan **una sola vez** desde el código en `src/` o `analysis/`
2. Los `.qmd` incluyen los resultados por referencia (`{{< include >}}` o chunks de R/Python)
3. Overleaf solo recibe el `.tex` exportado; no se edita directamente en Overleaf salvo el formato de envío
4. Cambios de contenido siempre se hacen en el repositorio, nunca en Overleaf

---

## Cuando llegue un nuevo documento al proyecto

Al recibir cualquier nuevo documento (paper, evaluación, memoria, propuesta, base de datos), seguir este protocolo:

1. **Leer completo** y comprender el contenido
2. **Resumir** en 5–10 líneas: tipo, autor, fecha, contenido principal
3. **Clasificar** según tipo: `postulación`, `evaluación`, `memoria`, `paper`, `datos`, `metodología`, `política pública`
4. **Relacionar** con el estado actual del proyecto: ¿qué cambia? ¿qué confirma? ¿qué contradice?
5. **Identificar** fortalezas y debilidades relevantes para el proyecto
6. **Proponer** nuevas tareas en `RESEARCH_ROADMAP.md`
7. **Actualizar** `PROJECT.md` si hay cambios en estado, outputs o equipo
8. **Actualizar** `RESEARCH_ROADMAP.md` si hay cambios en prioridades o agenda

---

## Señales de alerta (proactivas)

El asistente debe advertir activamente cuando detecte:

- **Inconsistencias entre documentos**: si PROJECT.md dice algo diferente a lo que dice una formulación ANID
- **Afirmaciones sin respaldo**: hipótesis o claims en postulaciones sin evidencia citada
- **Deuda metodológica**: decisiones tomadas sin documentar en el decision log
- **Riesgo de duplicación de contenido**: texto copiado entre documentos que debería ser una referencia
- **Literatura relevante no citada**: trabajos del estado del arte que deberían aparecer y no aparecen
- **Riesgos de reproducibilidad**: análisis que no pueden replicarse desde el código del repositorio

---

*Última actualización: julio 2026.*
