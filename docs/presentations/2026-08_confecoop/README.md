# Presentación — Cuentas satélite para organizaciones sin ánimo de lucro

*Aplicación de metodología de cuentas satélite a organizaciones sin ánimo de
lucro*, de Sebastián Cea y Joaquín Fernández. Presentación de 30
minutos ante una audiencia de dirigentes del cooperativismo de ahorro y crédito
(asociación / confederación nacional de cooperativas), cuyo interés es
**valorizar el sector** ante la autoridad y la opinión pública.

Está estructurada en dos niveles:

1. **Marco general** (láminas 3–7): qué es una cuenta satélite, qué manuales la
   rigen, cuál es su ecuación central y dónde se traba toda aplicación (el
   consumo intermedio). Transferible a cualquier organización sin ánimo de lucro.
2. **Caso de aplicación** (láminas 8–32): las cooperativas de ahorro y crédito
   chilenas, a partir de la memoria de título de Ignacio Ureta y Antonio Ruiz
   Tagle (2026), cuya autoría se declara explícitamente en la lámina 8 y en el
   cierre.

El cierre (lámina 31) vuelve del caso al marco general: qué cambia al aplicar el
mismo método a mutuales, fundaciones y asociaciones.

No es la presentación de defensa de la memoria: el énfasis está en la cifra, su
respaldo metodológico, y lo que el sector puede hacer para mejorarla.

## Archivos

| Archivo | Qué es |
|:--|:--|
| `home.qmd` | Fuente única de la presentación (Quarto) |
| `gen_figuras.py` | Genera los PNG de `figuras/` desde los cuadros de resultados |
| `uandes.sty`, `uandes-beamer-preamble.tex` | Tema Beamer institucional (plantilla `ingUANDES/techcollateral`) |
| `uandes-revealjs.scss` | Tema RevealJS institucional; fuentes DM Sans embebidas como data-URI |
| `assets/` | Fuentes y logos |
| `figuras/` | Gráficos generados por `gen_figuras.py` |

## Compilar

```bash
python3 gen_figuras.py                  # solo si cambian los datos
quarto render home.qmd --to revealjs    # → home.html (autocontenido)
quarto render home.qmd --to beamer      # → home.pdf  (39 láminas, 16:9)
```

Verificación de encuadre: la salida Beamer no debe producir ningún
`Overfull \vbox`, que es como LaTeX reporta una lámina cuyo contenido se corta
por abajo. Para comprobarlo, poner `keep-tex: true`, renderizar y correr
`xelatex home.tex`; `grep -c 'Overfull \vbox'` debe dar 0. Es más confiable que
revisar las láminas a ojo, sobre todo en miniaturas.

Beamer requiere XeLaTeX con `beamer`, `fontspec`, `tcolorbox` (con `breakable`),
`listings`, `newunicodechar` y `lmodern`. En Debian/Ubuntu:
`texlive-xetex texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra
texlive-lang-spanish lmodern`.

## Estructura y tiempos (30 min + 10 min de preguntas)

| Bloque | Láminas | Minutos |
|:--|:--|--:|
| 1. Marco general: qué es una cuenta satélite y qué exige | 3–7 | 7 |
| 2. Caso de aplicación: las CAC | 8–11 | 5 |
| 3. De dónde salen los datos y cómo se verifican | 12–17 | 5 |
| 4. El sector en cifras | 18–23 | 6 |
| 5. Contraste y hallazgos | 24–29 | 5 |
| 6. Qué falta — y qué puede hacer el sector | 30–33 | 3 |
| Cierre | 34 | — |
| Referencias | 35–36 | — |
| Anexos | 37–39 | — |

El bloque 3 cierra con dos láminas de método, no de resultado: la **15** hace
rastreable cada cifra hasta su cuadro de origen, y la **16** documenta la
auditoría de datos. Esta última era el "Hallazgo 5": presentarla como control de
calidad del método, y no como un hallazgo del caso, evita que se lea como un
resultado del sector cuando es una propiedad del procedimiento.

Las referencias van juntas en las láminas 33–34, y ninguna otra lámina repite
citas completas. Los anexos (35–37) **no se exponen**: son respaldo para
preguntas.

## Contraste de órdenes de magnitud (láminas 24–25)

Las láminas 24 y 25 comparan la cifra chilena con países que ya tienen cuenta
satélite de la economía social. La comparación es deliberadamente incómoda y hay
que exponerla con cuidado: España (4,0 % del VAB, 2023), Portugal (3,2 %, 2020) y
Polonia (1,94 %, 2018) miden **toda** su economía social, mientras Chile midió
**un solo subsector** (0,082 %). La brecha mide cobertura de medición, no tamaño
económico, y la lámina 25 lo dice explícitamente para que nadie la lea al revés.

El contraste que sí es válido va en la misma lámina 25: dentro del sistema
financiero chileno las CAC son 0,082 % del PIB frente al 3,1 % de los servicios
financieros completos (BCCh), es decir un 2,6 % del sector — coherente con el
2,41 % de participación patrimonial que la CMF calcula por una vía
independiente.

Fuentes internacionales verificadas contra la publicación original de cada
oficina estadística; van citadas en la lámina 35.

## Trazabilidad de las cifras

Todos los números provienen de los cuadros de resultados de la memoria
(`docs/Memoria/chapters/chapter04.tex` y `chapter05.tex`); el mapeo cifra → cuadro
está en la lámina de anexo "Fuentes de los datos presentados". `gen_figuras.py`
lleva las series transcritas en el encabezado del archivo, con referencia al
cuadro de origen de cada una.

Las cifras usadas son las **posteriores a la corrección de H-01/H-10**
(ver `docs/auditoria/02_reproduccion_calculos.md`): la fila 2025 del agregado total
es la corregida, verificada de forma independiente contra el Excel fuente y el
tablero público.

## Decisiones de diseño de los gráficos

Se apartan deliberadamente de las figuras del dashboard de la memoria en dos
puntos, ambos por legibilidad ante una audiencia no técnica:

1. **Sin doble eje.** La Figura 5.1 de la memoria superpone B1g y aporte al PIB en
   dos escalas; aquí van en gráficos separados.
2. **Eje de porcentaje anclado en cero.** Corrige el hallazgo P-01 de la auditoría
   (`docs/auditoria/05_feedback_alumno.md`): con eje truncado, la caída del aporte
   al PIB se lee como un desplome del 90 % cuando en realidad es de 39 %. Para una
   audiencia gremial ese error de lectura es especialmente costoso.

La paleta (`#CE0019` rojo institucional, `#0080A8`, `#A8760B`) fue verificada para
protanopia, deuteranopia y tritanopia, y para contraste sobre fondo claro y oscuro.
