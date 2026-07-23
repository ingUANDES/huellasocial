# Protocolo de auditoría de una memoria empírica de ingeniería
### Verificación de resultados + retroalimentación crítica anti-comisión
**Entorno:** Claude Code, sobre un repositorio que contiene el documento, los datos y el código.
**Ámbito:** memorias empíricas — proyectos cuantitativos con datos y estimaciones estadísticas, sean experimentales u observacionales (Facultad de Ingeniería y Ciencias Aplicadas, UANDES).
**Uso:** este archivo es autocontenido. Pégalo como instrucción inicial en Claude Code, o guárdalo en el repo y pídele que lo siga.

---

## 0. Objetivo y postura

Auditar una memoria de titulación empírica para: (a) **verificar** que sus
resultados se sostienen en los datos y los cálculos, (b) entregar **retroalimentación
crítica accionable** al alumno **a la brevedad**, y (c) **blindarla** frente a una
comisión externa exigente.

**Postura:** adopta la vara del evaluador más estricto, no la del más benévolo. La
experiencia muestra que la dispersión entre evaluadores de una misma memoria puede
ser alta; una auditoría útil anticipa al que busca el error, no al que felicita.
**Sé crítico y específico, pero justo:** evalúa el trabajo contra los objetivos que
el propio alumno declara, no contra los que tú habrías elegido.

**Regla de oro — no fabricar.** Nunca inventes, estimes ni "rellenes" un resultado
que no puedas reproducir desde los datos y el código. Lo que no se puede verificar
se reporta como hallazgo. Un resultado no reproducible es, en sí mismo, un problema
que una comisión penaliza. Ante conflicto entre lo que dice el texto y lo que dicen
los datos, mandan los datos, y se reporta la discrepancia.

---

## 1. Configuración recomendada de Claude Code

- **Modelo:** Opus, esfuerzo de razonamiento **alto**. El cuello de botella es el
  juicio estadístico y el trazado de consistencia, no el volumen de código.
  Alternativa costo-eficiente: Sonnet/medio para el mapeo y la aritmética (Fases
  0–1), Opus/alto para razonamiento estadístico y rúbrica (Fases 3–4).
- **Arranque:** clona con tu `gh`/git ya autenticado (la credencial nunca sale de
  tu máquina), `cd` al repo, `claude`, y comienza en **plan mode** para la Fase 0.
- **Trabaja por fases.** No saltes fases. Al terminar cada una, escribe su archivo
  de salida en `docs/auditoria/` y espera la confirmación del guía antes de seguir.

---

## 2. Insumos que la auditoría necesita (verificar antes de empezar)

Para una auditoría **completa** de una memoria empírica se requiere:
1. El **documento** (fuente LaTeX/Word o PDF) con sus capítulos.
2. Los **datos crudos** (seudonimizados si hay sujetos humanos, conforme al comité
   ético que corresponda).
3. El **código de análisis** ejecutable (cuadernos/scripts) que va de los datos
   crudos a las cifras y figuras reportadas.
4. La **especificación del entorno** (`requirements.txt` / `environment.yml` /
   `renv.lock`) para reproducir.

Si falta (2) o (3), **detente y repórtalo**: solo podrán ejecutarse las fases que
no dependen de recálculo (0, 1, 4, 5 parcial). Una memoria empírica cuyos datos
o código no están versionados y ejecutables por un tercero tiene, por ese solo
hecho, un problema de reproducibilidad que debe quedar registrado como hallazgo
crítico. Redacta de inmediato la lista de lo que hay que pedir al alumno para
desbloquear el resto.

---

## 3. Fases de la auditoría

### FASE 0 — Mapeo y bloqueo de reproducibilidad
- Recorre todo el árbol del repo. Ubica: documento, datos crudos, código de
  análisis, figuras, y especificación de entorno.
- Construye la tabla de trazabilidad, una fila por cada figura y tabla del
  documento: **elemento → script/cuaderno que lo genera → datos de entrada →
  estado (REPRODUCIBLE / HUÉRFANO)**. HUÉRFANO = aparece en la memoria pero no se
  encuentra el código o los datos que lo producen.
- Verifica la existencia física de cada archivo referenciado (imágenes, datos).
- Salida: `docs/auditoria/00_mapa_reproducibilidad.md`

### FASE 1 — Consistencia interna del documento (no requiere datos crudos)
Esto se puede hacer aun sin datos, y suele rendir hallazgos rápidos:
- **Aritmética de denominadores.** Toda tabla de flujo/conteo (muestra inicial →
  exclusiones → muestra final) debe cuadrar por filas, columnas y totales.
  Recalcúlala.
- **Coherencia de porcentajes.** Cada `%` reportado debe igualar su fracción
  `n/N`. Verifica todos los que puedas; comprueba que los grupos de respuesta única
  sumen el total y marca los de respuesta múltiple (no suman 100).
- **Integridad de referencias cruzadas.** Cada `\ref/\autoref` debe tener su
  `\label`; reporta referencias rotas (que salen como `??`). Lista figuras/tablas
  etiquetadas pero **nunca referenciadas** en el texto (posibles secciones a podar
  o a integrar).
- **Consistencia de denominadores entre secciones.** Si distintas secciones usan
  distinto `n`, verifica que esté justificado (p. ej. filtros sucesivos) y no sea
  un error.
- **Compilación / formato.** Confirma que el documento compila limpio desde un
  único directorio de trabajo; reporta rutas de figura inconsistentes, errores de
  compilación y advertencias.
- **Ortografía y estilo.** Errores tipográficos, nombres escritos de dos formas,
  párrafos duplicados por copy-paste, comillas/tildes.
- Salida: `docs/auditoria/01_consistencia_interna.md`

### FASE 2 — Reproducción de cálculos (requiere datos + código)
- Levanta el entorno y documenta lo que instales. Ejecuta la cadena de análisis
  **desde los datos crudos**.
- Para **cada** número, figura y tabla reportados, recalcula y compara. Tabla:
  *qué es · ubicación en el documento · valor reportado · valor reproducido ·
  ¿coincide? · Δ / nota*.
- Ordena las **discrepancias** por gravedad (graves / moderadas / menores).
- Salida: `docs/auditoria/02_reproduccion_calculos.md`

### FASE 3 — Auditoría estadística y de razonamiento (el núcleo del rigor)
Aquí es donde una comisión exigente gana o pierde. Revisa, adaptando a lo que
el trabajo efectivamente use (ver checklist en §4):
- **Correspondencia dato↔conclusión.** ¿Cada afirmación se sostiene en un resultado
  concreto? ¿Hay sobre-afirmación (conclusiones más fuertes que la evidencia)?
- **Diseño y validez.** ¿La estrategia empírica mide lo que dice medir (validez de
  constructo)? ¿El diseño (experimental u observacional) **induce** el resultado que
  luego se reporta como hallazgo? ¿Se confunde correlación con causalidad? En diseños
  observacionales, ¿se controlan los confusores y se justifica la identificación?
- **Elecciones estadísticas.** Test apropiado para el tipo de dato y el diseño;
  supuestos verificados; corrección por comparaciones múltiples cuando corresponde;
  márgenes/umbrales fijados **a priori** y justificados; intervalos de confianza
  correctamente construidos e interpretados.
- **Tamaño muestral y potencia.** ¿El `n` sostiene los tests aplicados? Marca tests
  con `n` bajo; verifica que los resultados sub-potenciados estén rotulados como
  exploratorios y que ninguna conclusión firme se apoye en ellos.
- **Transformaciones de datos.** Normalización vs. estandarización: ¿qué se
  transforma exactamente y por qué? Cuidado con **doble escalamiento** (dos
  transformaciones encadenadas que vuelven la interpretación imposible).
- **Honestidad visual de las figuras.** Ejes y escalas consistentes con el texto;
  leyendas que solo muestran lo que aparece en la figura; colores que no inducen a
  error; bandas/áreas sombreadas definidas; valores anómalos al olfato
  (magnitudes implausibles) señalados.
- Salida: `docs/auditoria/03_auditoria_estadistica.md`

### FASE 4 — Evaluación según la rúbrica de titulación (§5)
- Para cada indicador, asigna puntaje **0/1/3/5 justificado con evidencia** de las
  fases anteriores (cita ubicaciones concretas). Los niveles 2 y 4 son
  interpolaciones.
- Calcula el puntaje ponderado. **Confirma con el guía la fórmula exacta
  puntaje→nota antes de reportar cualquier nota.**
- Sé tan exigente como una comisión externa. Señala explícitamente fortalezas y
  riesgos por indicador.
- Salida: `docs/auditoria/04_evaluacion_rubrica.md`

### FASE 5 — Retroalimentación accionable para el alumno
- Lista **priorizada**: 🔴 CRÍTICO (lo hunde ante la comisión) / 🟡 IMPORTANTE
  (resta puntos apreciables) / 🟢 PULIDO (acabado). Cada ítem con: **qué** está mal,
  **dónde** (capítulo/sección/figura/página) y **qué hacer exactamente**.
- Cierra con un resumen ejecutivo de 3–5 frases que el alumno pueda leer primero.
- Salida: `docs/auditoria/05_feedback_alumno.md`

---

## 4. Checklist de patrones de error frecuentes en memorias empíricas

Radar transversal, aplicable tanto a diseños experimentales como observacionales.
No todos aplican a toda memoria; usa solo los pertinentes al diseño real del trabajo.

**Estructura (lo que las comisiones exigen y suele faltar)**
- [ ] Objetivo general y objetivos específicos, explícitos.
- [ ] Alcances y limitaciones declarados; el alcance coincide con lo realmente hecho.
- [ ] Revisión de literatura real, no solo definiciones.
- [ ] Marco teórico que contiene teoría (no datos disfrazados de teoría).

**Presentación**
- [ ] Toda figura/tabla **referenciada en el texto Y explicada** (contenido +
      análisis). Es la crítica más recurrente.
- [ ] Numeración de figuras/tablas correcta y consistente.
- [ ] Documento no innecesariamente extenso; secciones/tablas/figuras redundantes podadas.
- [ ] Sin párrafos duplicados; ortografía y notación cuidadas.

**Datos y método**
- [ ] Frecuencia, periodo y origen de los datos declarados explícitamente.
- [ ] Se reportan estadísticos descriptivos (n, media, DE, rango) antes de inferir.
- [ ] No se listan insumos/variables que luego no se usan.
- [ ] Cada elección metodológica (horizontes, umbrales, transformaciones) justificada.

**Estadística**
- [ ] Test apropiado y supuestos verificados.
- [ ] Corrección por comparaciones múltiples donde corresponde.
- [ ] Márgenes/umbrales a priori, no elegidos tras ver los datos.
- [ ] Intervalos de confianza bien construidos e interpretados.
- [ ] `n` suficiente; resultados sub-potenciados rotulados como exploratorios.
- [ ] Sin doble escalamiento; normalización/estandarización explicada.

**Figuras**
- [ ] Escalas consistentes texto↔figura; leyendas fieles; colores no engañosos;
      áreas/bandas definidas; valores anómalos señalados.

**Validez y conclusiones**
- [ ] El diseño empírico mide su constructo declarado (no otro).
- [ ] El diseño no induce el resultado que luego se presenta como hallazgo.
- [ ] Conclusiones proporcionales a la evidencia; no se ignoran factores relevantes
      (p. ej. riesgo, confusores).
- [ ] Hay conclusiones útiles, no solo descripción.

**Reproducibilidad**
- [ ] Datos + código versionados y ejecutables por un tercero.
- [ ] Toda cifra del capítulo de resultados rastreable a una corrida reproducible.

---

## 5. Rúbrica de titulación UANDES (documento escrito)
> Facultad de Ingeniería y Ciencias Aplicadas. Los niveles 2 y 4 son interpolación
> entre 1, 3 y 5. Confirmar vigencia de ponderaciones con la Facultad/guía.

| # | Indicador | % |
|---|-----------|---|
| 1 | Presentación y expresión escrita | 10 % |
| 2 | Resumen | 5 % |
| 3 | Introducción y motivación | 15 % |
| 4 | Desarrollo | 20 % |
| 5 | Análisis y conclusiones | 30 % |
| 6 | Referencias | 5 % |
| 7 | Relevancia, alcance y novedad | 15 % |

**1. Presentación y expresión escrita (10 %)** — 0: abundantes errores, sin
formato ni figuras de apoyo · 1: errores evidentes, formato inconsistente, figuras
pobres · 3: errores reducidos, formato respetado, figuras adecuadas · 5: sin
errores, formato consistente, figuras precisas que aportan claridad, longitud
adecuada.

**2. Resumen (5 %)** — 0: no hay · 1: exceso de errores y ausencia de temas
relevantes · 3: algunos errores, falta una de las áreas (motivación / trabajo /
resultados) · 5: bien escrito, con motivación, desarrollo y resultados/conclusiones.

**3. Introducción y motivación (15 %)** — 0: no hay · 1: presenta mal el problema,
motivación inexistente, alcance vago · 3: problema claro, motivación poco clara,
alcance no coincide del todo con lo hecho · 5: problema y motivación claros,
alcance preciso que coincide con lo realizado.

**4. Desarrollo (20 %)** — 0: no hay · 1: tareas pobres, sin detalle ni material
para comprenderlas · 3: tareas correctas, material insuficiente para comprenderlas
a cabalidad · 5: tareas óptimas y claras, material complementario que permite ver
en detalle lo realizado.

**5. Análisis y conclusiones (30 % — el de mayor peso)** — 0: no hay · 1:
métodos inadecuados, se omite información, conclusiones no justificadas · 3:
métodos adecuados pero insuficientes, faltan detalles, conclusiones concuerdan con
el alcance · 5: métodos adecuados, comparaciones que sitúan el resultado, análisis
claro y lógico, conclusiones específicas con su alcance.

**6. Referencias (5 %)** — 0: no hay · 1: hay referencias pero mal citadas en el
texto · 3: aseveraciones relevantes citadas, fuentes correctas, no abundantes · 5:
todo lo relevante y no evidente referenciado, fuentes de alta calidad.

**7. Relevancia, alcance y novedad (15 %)** — 1: poco relevante/novedoso,
profundidad baja para el tiempo dado · 3: medianamente relevante, profundidad
adecuada aunque mejorable · 5: muy relevante, profundidad excelente para el tiempo
y capacidades del alumno.

---

## 6. Formato de salida y tono de la retroalimentación

- Escribe los cinco/seis archivos en `docs/auditoria/`. Cada uno inicia con un
  resumen ejecutivo y una tabla de conteo de hallazgos por severidad.
- Cada hallazgo lleva **id** (H-01…), **severidad**, **ubicación exacta**,
  **evidencia** (el cálculo o la cita que lo prueba) y **acción concreta**.
- Distingue siempre lo **verificado** (con evidencia reproducible) de lo **opinable**
  (juicio de diseño): no presentes un juicio como si fuera un hecho comprobado.
- Tono: crítico, directo y respetuoso. El objetivo es que el alumno mejore su
  trabajo y lo defienda bien, no exhibir errores. Reconoce las fortalezas reales;
  una auditoría que solo enumera fallas es tan poco útil como una que solo felicita.


### FASE 6 — Proyección científica y continuidad de la línea de investigación

Esta fase transforma los hallazgos de la auditoría en insumos para la línea de
investigación acumulativa. No es evaluativa sino generativa. Se ejecuta después
de la Fase 5 y sus conclusiones alimentan el RESEARCH_ROADMAP.md del proyecto.

**6.1 Oportunidades de publicación**
- Identifica el resultado o contribución más publicable del trabajo (metodología
  nueva, estimación empírica inédita, dataset construido).
- Propón una revista objetivo con justificación: scope, quartil, ISSN, tiempo
  estimado de revisión. Distingue entre contribución suficiente para artículo
  completo vs. nota técnica vs. working paper.
- Señala qué debe reforzarse del trabajo actual para cumplir el estándar de
  revisión por pares (estado del arte, robustez, replicabilidad).

**6.2 Preguntas de investigación abiertas**
- Lista las preguntas que el trabajo deja sin responder o que abre explícitamente.
- Clasifica cada una: (a) extensión directa del mismo método, (b) requiere nuevos
  datos, (c) requiere nueva metodología, (d) requiere colaboración externa.
- Distingue entre preguntas que *el propio trabajo sugiere* y preguntas que
  *tú agregas* como co-investigador — no las mezcles.

**6.3 Propuesta de continuidad para memorias y tesis futuras**
- Formula entre 2 y 4 propuestas concretas de trabajos futuros que continúen
  este, en orden de dependencia lógica: cada propuesta debe poder arrancar con
  los outputs de la memoria auditada como insumo.
- Para cada propuesta indica: pregunta central, datos requeridos, método
  sugerido, nivel recomendado (pregrado / magíster / doctorado) y por qué.
- Señala explícitamente qué partes del código o pipeline actual son reutilizables
  y cuáles deben reconstruirse.

**6.4 Vínculo con la estrategia ANID**
- Evalúa cómo los resultados de esta memoria fortalecen una futura postulación
  IDeA I+D: ¿resuelven alguna crítica documentada de evaluaciones anteriores?
  ¿constituyen un resultado previo verificable? ¿amplían el TRL declarado?
- Identifica si la memoria produce evidencia que cuantifica el problema central
  del proyecto (asimetría de información, invisibilidad estadística) de forma
  citable por evaluadores ANID.

**6.5 Literatura relevante no citada**
- Señala trabajos del estado del arte que el autor debería haber citado y no
  citó. Distingue entre omisiones que debilitan la contribución declarada y
  omisiones menores de contexto.
- Esta lista sirve directamente para fortalecer el estado del arte de la
  próxima postulación ANID.

Salida: `docs/auditoria/06_proyeccion_cientifica.md`