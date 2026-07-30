# Registro de fuentes externas — datos no versionados en el repositorio

> Convención del Research OS (julio 2026): los archivos de datos crudos descargados de fuentes públicas (Excel, TXT, CSV de gran tamaño) **no se suben directamente al repositorio git**. En su lugar, esta tabla registra: (a) la URL original de la fuente pública, y (b) la ubicación del respaldo externo (ej. carpeta compartida de Google Drive del proyecto). El repositorio conserva solo la trazabilidad, no el binario.
>
> Esta es una corrección de criterio respecto de versiones anteriores del Research OS, que sí alojaban Excel completos en el repositorio (ver `docs/reports/decision_log.md`, entrada 2026-07-30). La migración completa de los archivos ya versionados (p. ej. en `Dashboard_HuellaSocial`) a este esquema queda pendiente como tarea de mantenimiento futura — no es retroactiva a lo ya entregado.

| # (ref. `SOLICITUD_AUTORES.md`) | Archivo | URL original de la fuente | Respaldo externo (carpeta / enlace) | Estado |
|---|---|---|---|---|
| D-04 | `PUB_NOMBRES_PJ.txt` (archivo maestro de personas jurídicas, SII) | *(pendiente: los autores deben completar la URL exacta del portal SII desde la que se descargó)* | *(pendiente: enlace a la carpeta de respaldo del proyecto — Drive/similar)* | 🟡 Pendiente de completar por los autores |

---

*Mantener esta tabla actualizada cada vez que se referencie una fuente de datos externa en `SOLICITUD_AUTORES.md` o en la memoria, en vez de subir el binario al repositorio.*
