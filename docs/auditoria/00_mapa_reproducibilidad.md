# FASE 0 — Mapa de reproducibilidad
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Fecha de auditoría:** julio 2026  
**Auditor:** Research Engineering Assistant (Research OS)  
**Documento auditado:** `docs/thesis/Ureta_RuizTagle_2026.pdf` (98 pp.)  
**Estado global: 🔴 NO REPRODUCIBLE — código y datos ausentes del repositorio**

---

## Resumen ejecutivo

La memoria está disponible únicamente como PDF. El código de análisis reside en un repositorio externo no auditado (https://github.com/Iureta1/Dashboard_HuellaSocial) y los datos fuente no están versionados en ningún repositorio accesible a un tercero. Por este solo hecho, la memoria tiene un problema de reproducibilidad de severidad crítica, registrado como hallazgo H-02.

| Severidad | N hallazgos |
|-----------|-------------|
| 🔴 CRÍTICO | 1 (H-02) |
| 🟡 IMPORTANTE | 0 |
| 🟢 PULIDO | 0 |

**Fases habilitadas con insumos actuales:** 0, 1, 4, 5 (parcial), 6  
**Fases bloqueadas:** 2 (reproducción de cálculos), 3 (auditoría estadística)

---

## H-02 — Reproducibilidad bloqueada: ausencia de código y datos en el repositorio

| Atributo | Detalle |
|----------|---------|
| **id** | H-02 |
| **Severidad** | 🔴 CRÍTICO |
| **Ubicación** | Repositorio huellasocial (ausencia global); §4.2.1, §4.3.1, nota 2 y nota 4 de la memoria |
| **Tipo** | Verificado (ausencia física confirmada por `ls` del repositorio) |

**Evidencia:**  
El repositorio `huellasocial` no contiene ninguno de los siguientes elementos referenciados en la memoria:

- `Consolidado_cooperativas.xlsx` — referenciado en §4.3.2 como fuente de variables de directorio
- `sii_company_timeseries.parquet` — referenciado en §4.3.2 como fuente de empleo (PEP)
- `PUB_NOMBRES_PJ.txt` — referenciado en §4.3.1 para validación de RUT/subtipo
- Cualquier script de Python o R que aplique P2 = α · P1
- Cualquier notebook o pipeline que genere las tablas o figuras del capítulo 5

El código y el dashboard están alojados en https://github.com/Iureta1/Dashboard_HuellaSocial (referenciado en la nota 4, §4.4 y §5.1). Este repositorio no está integrado al Research OS y no se auditó su contenido en esta fase.

**Consecuencias concretas:**
1. Ningún número del Capítulo 5 puede verificarse de forma independiente desde los datos crudos.
2. No se puede confirmar que α = 0,3776 se aplica correctamente a todas las observaciones.
3. No se puede replicar el pipeline de integración por RUT.
4. El hallazgo H-01 (error en Cuadro 5.7, fila 2025) fue detectado por consistencia interna (Fase 1), pero su causa raíz solo puede confirmarse con el código.

**Acción requerida:** Entregar los insumos listados en `SOLICITUD_AUTORES.md` antes de continuar las Fases 2 y 3.

---

## Tabla de trazabilidad — Figuras

| Figura | Descripción | Script/notebook | Datos | Estado |
|--------|-------------|----------------|-------|--------|
| Figura 5.1 | VAB y aporte al PIB — Segmento CMF (2013–2025) | No localizado en repositorio | Panel CMF (D-03) | 🔴 HUÉRFANO |
| Figura 5.2 | VAB y N por año — Segmento DAES (2014–2024) | No localizado en repositorio | Panel DAES (D-02) | 🔴 HUÉRFANO |
| Figura 5.3 | Distribución regional de CAC vigentes | No localizado en repositorio | Consolidado DAES (D-01) + datos CMF | 🔴 HUÉRFANO |

## Tabla de trazabilidad — Cuadros

| Cuadro | Descripción | Script/notebook | Datos | Estado |
|--------|-------------|----------------|-------|--------|
| 4.1 | Cobertura de fuentes administrativas | No localizado | DAES, CMF, SII | 🔴 HUÉRFANO |
| 4.2 | Estadística descriptiva por segmento | No localizado | D-02, D-03 | 🔴 HUÉRFANO |
| 4.3–4.5 | Variables operacionalizadas (SCN) | No localizado | D-02, D-03 | 🔴 HUÉRFANO |
| 4.6 | Variables no construibles | No aplica (tabla cualitativa) | — | ✅ MANUAL |
| 5.1 | Cobertura anual DAES | No localizado | D-02 | 🔴 HUÉRFANO |
| 5.2 | Cuenta de producción DAES | No localizado | D-02 | 🔴 HUÉRFANO |
| 5.3 | Aporte al PIB DAES | No localizado | D-02 + PIB BCCh | 🔴 HUÉRFANO |
| 5.4 | Cuenta financiera DAES | No localizado | D-02 | 🔴 HUÉRFANO |
| 5.5 | Cuenta de producción CMF | No localizado | D-03 | 🔴 HUÉRFANO |
| 5.6 | Cuenta financiera CMF | No localizado | D-03 | 🔴 HUÉRFANO |
| 5.7 | Cuenta de producción total (CMF+DAES) | No localizado | D-02 + D-03 | 🔴 HUÉRFANO |
| 5.8 | Cuenta financiera total (CMF+DAES) | No localizado | D-02 + D-03 | 🔴 HUÉRFANO |
| 5.9 | Validación externa | No localizado | D-02 + D-03 + D-08 | 🔴 HUÉRFANO |

**Resultado:** 16/16 elementos del capítulo de resultados son HUÉRFANOS.

---

## Estado del entorno

| Componente | Disponible en repositorio | Notas |
|------------|--------------------------|-------|
| Documento (PDF) | ✅ | `docs/thesis/Ureta_RuizTagle_2026.pdf` |
| Datos crudos | ❌ | No versionados |
| Código de análisis | ❌ | En repo externo (Iureta1/Dashboard_HuellaSocial) |
| `requirements.txt` | ❌ | No presente |
| `environment.yml` | ❌ | No presente |
| `renv.lock` | ❌ | No presente |

---

*Salida de FASE 0 — conforme a AUDIT_PROTOCOL.md §3. Siguiente fase habilitada: FASE 1 (consistencia interna).*
