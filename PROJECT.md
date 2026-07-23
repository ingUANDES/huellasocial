# Huella Social — PROJECT.md

> Documento fundacional del proyecto. Describe la visión, el problema de investigación, la solución, el estado actual y los actores clave. Debe mantenerse actualizado con cada avance significativo.

---

## Visión

Huella Social es una plataforma-observatorio digital que integra, estandariza y visualiza datos de las organizaciones de la economía social y solidaria (ESS) en Chile —ONG, fundaciones, cooperativas y empresas sociales—, generando indicadores de desempeño, benchmarking y cuentas satélite alineadas a estándares internacionales. Su propósito último es reducir la invisibilidad estadística del sector, mejorar la asignación de recursos y fortalecer la confianza pública en las organizaciones sociales.

---

## Problema de investigación

### Problema central

Menos del 0,04% de las 234.502 organizaciones de la sociedad civil (OSC) registradas en Chile reporta bajo algún estándar de información pública (p. ej., FECU Social). Esta opacidad genera asimetrías de información severas (Akerlof, 1970) que afectan a tres actores:

- **OSC**: compiten por financiamiento sin poder demostrar desempeño ni aprender de pares comparables.
- **Donantes y financistas**: toman decisiones basadas en redes y reputación, no en evidencia de impacto.
- **Estado y reguladores**: carecen de mecanismos para dimensionar el aporte de la ESS ni para diseñar políticas basadas en evidencia.

### Evidencia cuantitativa disponible

La memoria de título Ureta & Ruiz Tagle (2026) —primer output empírico del proyecto— estima que las cooperativas de ahorro y crédito en Chile contribuyen entre **0,04% y 0,08% del PIB nacional**, siendo estadísticamente invisibles dentro del Sistema de Cuentas Nacionales. Esta cifra sirve como caso piloto y punto de partida para la generalización metodológica al resto de la ESS.

### Hipótesis de investigación

1. **Científica**: La integración y estandarización de registros administrativos públicos chilenos permite construir indicadores comparables de desempeño para las OSC, reduciendo la asimetría de información que inhibe la asignación eficiente de recursos.
2. **Tecnológica**: Una plataforma digital de datos abiertos, basada en metodologías de eficiencia (DEA, SFA) y cuentas satélite, puede generar benchmarking útil para la gestión de OSC y para la formulación de políticas públicas.

---

## Solución: Huella Social

La plataforma opera en tres capas:

| Capa | Descripción | Estado |
|------|-------------|--------|
| **Ingesta y limpieza** | Pipeline de consolidación de fuentes públicas (SII, FECU Social, DAES, CMF, MDS, Ley 19.826, Ley 19.885, Registro Civil) | Prototipo funcional (TRL 3) |
| **Generación de indicadores** | DEA, SFA, clustering, machine learning, cuentas satélite (SNA 2008 + TSE Handbook ONU) | Metodología documentada (tesis 2026) |
| **Visualización y reportes** | Observatorio web interactivo, descarga de reportes personalizados, API pública | Demo en Shiny R; migración a React planificada |

**Prototipo actual**: [https://sxclabs.shinyapps.io/cos-sxc/](https://sxclabs.shinyapps.io/cos-sxc/) — integra y cruza experimentalmente ≥15 fuentes públicas con clustering de entidades de la ESS chilena.

**Modelo de distribución**: SaaS con suscripciones modulares (datos brutos / indicadores metodológicos / reportes personalizados) más licencias gratuitas para instituciones públicas.

---

## Marco teórico y disciplinar

El proyecto se sitúa en la intersección de:

- **Economía de la información** (Akerlof 1970; Stiglitz & Weiss 1981): asimetrías de información en mercados con externalidades sociales.
- **Economía social y solidaria** (OIT 2019; Borzaga et al. 2020): definición, medición y valorización del sector.
- **Cuentas nacionales y cuentas satélite** (SNA 2008; TSE Handbook ONU; metodología CIRIEC): estimación del valor agregado de organizaciones no-mercado.
- **Eficiencia organizacional** (DEA: Charnes, Cooper & Rhodes 1978; SFA: Battese & Coelli 1992): medición de la frontera de eficiencia en OSC.
- **Especialización inteligente** (Rigby et al. 2022): identificación de brechas y oportunidades para el sector.
- **Ciencia de datos abiertos**: arquitecturas de observatorios de datos públicos (Our World in Data, Open Corporates, BIPS Chile, SEDESOL México).

---

## Repositorios del proyecto

| Repositorio | URL | Rol |
|-------------|-----|-----|
| **huellasocial** (principal) | [https://github.com/ingUANDES/huellasocial](https://github.com/ingUANDES/huellasocial) | Plataforma, análisis, documentación científica |
| **donaciones** (hermano) | [https://github.com/viantirreau/donaciones](https://github.com/viantirreau/donaciones) | Pipeline de consolidación de bases de datos fuente |

Los repositorios son independientes pero comparten estándares de documentación y componentes de pipeline reutilizables. Los datos procesados en `donaciones` alimentan la capa de ingesta de `huellasocial`.

---

## Equipo del proyecto

| Persona | Rol | Institución |
|---------|-----|-------------|
| **Sebastián Cea Echenique** | Director / Investigador Principal | Universidad de Los Andes |
| **Joaquín Fernández** | Co-director / Co-Investigador | Universidad de Los Andes |
| **Elisabeth Farrelly** | Investigadora | Universidad de Los Andes |
| **Ignacio Ureta** | Tesista (memoria 2026) | Universidad de Los Andes |
| **Antonio Ruiz Tagle** | Tesista (memoria 2026) | Universidad de Los Andes |

### Entidades asociadas y colaboradoras

- **Universidad de Chile** (beneficiaria secundaria desde ID26)
- **CONFECOOP** / Asociación Nacional de Cooperativas de Chile
- **Fundación Rodelillo**
- **INAC** — Instituto Nacional de Asociatividad y Cooperativismo
- **CIESCOOP** — Centro de Estudios de la Cooperación, U. de Santiago
- **Centro de Políticas Públicas UC**
- **COS** — Comunidad de Organizaciones Solidarias (socio piloto)
- **SocialxChange** (piloto de cruce de datos)

---

## Historial de postulaciones ANID IDeA I+D

| Año | Folio | Nota Final | Postulante | Resultado |
|-----|-------|-----------|------------|-----------|
| 2024 | ID24I10276 | 2,23 / 5 | Sebastián Cea | No adjudicado |
| 2025 | ID25I10354 | 2,88 / 5 | Elisabeth Farrelly | No adjudicado |
| 2026 | ID26I10768 | 2,73 / 5 | Sebastián Cea | No adjudicado |

**Diagnóstico de rechazo recurrente** (síntesis de tres evaluaciones):
1. Cuantificación del problema insuficiente — descriptiva, no cuantitativa
2. Estado del arte débil — no diferencia de BIPS ni de plataformas internacionales comparables
3. Metodología genérica — sin diseño experimental, sin métricas de efectividad de la plataforma
4. Modelo de gobernanza del observatorio no especificado
5. Objetivos e hitos sin indicadores de logro vinculados a umbrales TRL

El equipo y el presupuesto han sido consistentemente bien evaluados (4,0–4,5). El problema no está en las capacidades sino en la formulación científica.

---

## Outputs científicos y técnicos

### Producción actual

| Output | Tipo | Año | Estado |
|--------|------|-----|--------|
| Ureta & Ruiz Tagle (2026) — Propuesta metodológica para una cuenta satélite de las cooperativas de ahorro y crédito en Chile | Memoria de título | 2026 | Completada |
| Prototipo web (Shiny R) | Software | 2025 | Funcional, TRL 3 |
| Formulaciones ID24/25/26 | Documentos de postulación | 2024–2026 | Archivados |

### Pipeline de outputs planificados

1. Artículo científico basado en Ureta & Ruiz Tagle (2026) → revista Q1/Q2
2. Working paper: landscape analysis de plataformas de datos para la ESS
3. Memoria 2027: extensión metodológica a fundaciones y ONG
4. Pipeline computacional reproducible publicado en el repositorio
5. Postulación ID27 con nueva formulación

---

## Alineamiento con política pública y marcos internacionales

- **Resolución ONU A/RES/77/281** (2023) y ratificación 2024: promueve estadísticas nacionales para valorizar los aportes de la ESS.
- **Ley 21.440** (Chile, 2022): transparencia en financiamiento de OSC — crea demanda para los productos del proyecto.
- **Fondo Mixto Ley 19.885**: el sistema puede servir como herramienta de evaluación de postulantes.
- **ODS 16 y 17**: transparencia institucional y alianzas para el desarrollo sostenible.

---

*Última actualización: julio 2026. Próxima revisión recomendada: antes de postulación ID27.*
