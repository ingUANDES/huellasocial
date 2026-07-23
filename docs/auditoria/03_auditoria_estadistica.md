# FASE 3 — Auditoría estadística y de razonamiento
## Ureta & Ruiz Tagle (2026) · Auditoría Research OS — Huella Social

**Estado: 🔴 BLOQUEADA (parcialmente)**

Esta fase requiere principalmente los datos crudos y el código. Sin embargo, a partir del PDF se pueden anticipar los focos de análisis que se ejecutarán una vez desbloqueada.

---

## Anticipaciones (verificables desde el PDF)

### Validez de constructo
- **P1 como proxy de producción:** La elección de usar ingresos operacionales como P1 es coherente con el SCN 2025 (párr. 7.169) para instituciones financieras de mercado. Sin posibilidad de contradecir sin datos.
- **α = 0,3776:** Derivado del sector 94 MIP BCCh 2018. El supuesto de homogeneidad es explícitamente discutido en §4.3.2, nota 3. La fn. 3 señala que CAPUAL y AHORROCOOP presentan razones P2/P1 implícitas de ~0,72 (doble del promedio), lo que sugiere que α falla para estas entidades. Sin código no se puede cuantificar el sesgo.
- **Validez de la suma CMF+DAES:** §5.3 la presenta como "aproximación de orden de magnitud", correctamente calificada. La validación externa (§5.3.3) es metodológicamente sólida.

### Análisis de sensibilidad ausente (juicio de diseño)
El trabajo no realiza análisis de sensibilidad de los resultados a variaciones de α. Dado que los autores identifican heterogeneidad significativa en la razón CI/P entre entidades (0,23–0,72), la omisión de un escenario con α diferenciado por tamaño (ej. Coopeuch separado del resto) es una debilidad identificable sin datos.

### Sobre-afirmación en conclusions
Las conclusiones (§6.2) son proporcionales a la evidencia presentada. No se detectan afirmaciones causales donde la evidencia es solo descriptiva. Las limitaciones documentadas en §5.5 son completas y precisas.

### N y potencia
Con N entre 2 y 22 por año en el segmento DAES, el análisis es fundamentalmente descriptivo (no inferencial). No hay tests estadísticos que auditar. Los autores no realizan pruebas de hipótesis, lo cual es apropiado dado el propósito de cuentas satélite.

---

Esta fase se completará cuando se reciban los insumos listados en `SOLICITUD_AUTORES.md`.

---

*Salida de FASE 3 — pendiente de insumos. Ver `SOLICITUD_AUTORES.md`.*
