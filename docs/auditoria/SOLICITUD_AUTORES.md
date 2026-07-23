# Lista de insumos solicitados a los autores
## Para desbloquear Fases 2 y 3 de la auditoría — Ureta & Ruiz Tagle (2026)

**Emitida por:** Research Engineering Assistant (Research OS — Huella Social)  
**Fecha:** julio 2026  
**Destinatarios:** Ignacio Ureta, Antonio Ruiz Tagle  
**Referencia:** AUDIT_PROTOCOL.md §2; Fases 2 y 3 actualmente BLOQUEADAS

---

## Contexto

La auditoría de la memoria *Propuesta metodológica para una cuenta satélite de las cooperativas de ahorro y crédito en Chile* solo puede avanzar hasta las Fases 0, 1, 4 y 5 con el PDF disponible. Las Fases 2 (Reproducción de cálculos) y 3 (Auditoría estadística) requieren acceso al código ejecutable y a los datos fuente. Se listan a continuación los insumos exactos a entregar.

---

## A. Datos (insumos primarios)

| # | Archivo / fuente | Descripción | Formato esperado |
|---|-----------------|-------------|-----------------|
| D-01 | `Consolidado_cooperativas.xlsx` | Registro institucional DAES: RUT, razón social, tipo, región, N socios | Excel / CSV |
| D-02 | Panel DAES de estados financieros | 133 observaciones (35 CAC × 2014–2024, cobertura variable). Variables: P1, D1, B2g, Rem, activos, patrimonio, F2, F4, año, RUT | CSV o Parquet con header en español |
| D-03 | Panel CMF de estados financieros | 91 observaciones (7 CAC × 2013–2025). Mismas variables que D-02 más desglose por entidad | CSV o Parquet |
| D-04 | `PUB_NOMBRES_PJ.txt` | Archivo maestro de personas jurídicas SII; usado para validar existencia legal y subtipo 817 (CAC) | TXT (delimitado) |
| D-05 | `sii_company_timeseries.parquet` | Serie de tiempo SII: tramo de ventas + número de trabajadores por RUT | Parquet |
| D-06 | Extracto MIP BCCh 2018 | La celda o rango exacto de la Matriz Insumo-Producto del Banco Central de Chile 2018 de donde se obtuvo α = 0,3776 para el sector 94 (Intermediación financiera). Si hay archivo descargado: adjuntarlo. Si es consulta web: URL permanente y fecha de acceso | Excel / CSV / captura de pantalla con metadatos |
| D-07 | Extracto CMF-BEST | Datos del segmento CMF obtenidos vía plataforma BEST, tal como fueron descargados (antes de cualquier limpieza) | CSV u otro formato de descarga |
| D-08 | Datos de validación externa | Serie "Servicios financieros (% PIB)" usada en el Cuadro 5.9 (fuente: Banco Central de Chile, 2026); y la cifra 2,41 % de participación patrimonial (CMF, diciembre 2025) | CSV / link exacto al informe CMF |

---

## B. Código de análisis

| # | Script / notebook | Descripción | Lenguaje esperado |
|---|------------------|-------------|------------------|
| C-01 | Pipeline de integración de fuentes | Carga D-01 a D-05, cruza por RUT, produce el panel limpio de estimación | Python o R |
| C-02 | Script de cálculo VAB | Aplica P2 = α · P1 → B1g; calcula aporte al PIB; produce los valores de Cuadros 5.2, 5.3, 5.5, 5.7, 5.9 | Python o R |
| C-03 | Script de cuenta financiera | Produce Cuadros 5.4, 5.6, 5.8 | Python o R |
| C-04 | Script de figuras | Genera Figuras 5.1, 5.2, 5.3 (o los archivos HTML del dashboard que las contienen) | Python (Plotly) |
| C-05 | Dashboard HTML | Archivo `index.html` o equivalente del panel interactivo descrito en §4.4 y §5.4 | HTML (Plotly autocontenido) |

**Nota sobre el repositorio externo:** La sección 4.4 y la nota al pie 4 mencionan https://github.com/Iureta1/Dashboard_HuellaSocial como repositorio público del proyecto. Si el código anterior está ahí, indíquese la carpeta exacta y el commit SHA de la versión que generó los resultados de la memoria. Si el repositorio está en un estado diferente al momento de la defensa, adjúntese un snapshot (ZIP o tag de Git).

---

## C. Especificación del entorno

| # | Elemento | Descripción |
|---|---------|-------------|
| E-01 | `requirements.txt` o `environment.yml` | Versiones exactas de Python y paquetes usados (Plotly, pandas, numpy, etc.) |
| E-02 | Versión de Python | Número exacto (ej. Python 3.11.4) |
| E-03 | Sistema operativo | SO en que se ejecutó el análisis (ej. macOS 14.5, Ubuntu 22.04) |

---

## D. Documentación metodológica adicional

| # | Documento | Descripción |
|---|-----------|-------------|
| M-01 | Criterios de inclusión/exclusión de entidades DAES | ¿Qué condiciones debe cumplir una CAC para incluirse en el panel? ¿Cómo se trataron las entidades disueltas o inactivas durante el período? |
| M-02 | Criterio de extracción de P1 y D1 desde PDFs DAES | ¿Qué nombre de línea exactamente se buscó en los estados de resultados? ¿Cómo se manejaron los formatos distintos entre memorias? |
| M-03 | Definición exacta de "observación" en el panel | ¿Una observación es una CAC-año con P1 disponible? ¿Con al menos una variable? ¿Con todas las variables del SCN? (ver H-03 en `01_consistencia_interna.md`) |
| M-04 | Fuente del dato de PIB para cada año | ¿Es el PIB a precios corrientes base 2018 de las Cuentas Nacionales Anuales del BCCh? ¿Qué tabla exacta y qué fecha de descarga? |

---

## Prioridad de entrega para desbloquear la auditoría

| Prioridad | Insumos | Qué desbloquea |
|-----------|---------|----------------|
| 🔴 Urgente | D-02, D-03, C-02 | Verificar H-01 (error Cuadro 5.7, fila 2025) y H-03 (inconsistencia de N) |
| 🟡 Alta | D-06, C-01 | Verificar α = 0,3776 y proceso de integración de fuentes |
| 🟢 Normal | D-01, D-04, D-05, D-07, D-08, C-03, C-04, C-05, E-01/02/03, M-01–M-04 | Auditoría completa de reproducibilidad y estadística |

---

*Este documento fue generado en la Fase 0 de la auditoría, en cumplimiento del AUDIT_PROTOCOL.md §2.*
