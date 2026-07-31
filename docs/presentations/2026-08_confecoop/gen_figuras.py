"""Genera las figuras de la presentación CONFECOOP a partir de los cuadros de
resultados de Ureta & Ruiz Tagle (2026).

Fuente de los datos: docs/Memoria/chapters/chapter05.tex, cuadros
tab:resultados_daes, tab:resultados_cmf, tab:resultados_total,
tab:balance_total, tab:cobertura_daes y tab:validacion_cmf.

Uso:  python3 gen_figuras.py     (escribe PNG en ./figuras/)

Convenciones de diseño aplicadas:
  - paleta categórica de 3 hues validada para daltonismo (protan/deutan/tritan)
    y contraste >= 3:1 sobre fondo claro;
  - un solo eje por gráfico (nunca doble eje);
  - ejes de porcentaje anclados en cero;
  - etiquetas directas en vez de leyendas cuando hay <= 3 series.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter

BASE = Path(__file__).resolve().parent
OUT = BASE / "figuras"
OUT.mkdir(exist_ok=True)

# ── Tipografía institucional ────────────────────────────────────────────────
for ttf in (BASE / "assets" / "fonts").glob("*.ttf"):
    font_manager.fontManager.addfont(str(ttf))
FAMILY = "DM Sans" if any((BASE / "assets" / "fonts").glob("*.ttf")) else "sans-serif"

# ── Paleta ──────────────────────────────────────────────────────────────────
ROJO = "#CE0019"   # CMF / serie principal (rojo institucional UANDES)
AZUL = "#0080A8"   # DAES / serie secundaria
AMBAR = "#A8760B"  # tercera serie
TINTA = "#131E29"
TINTA2 = "#415569"
SUAVE = "#D6D1CA"
SUP = "#FCFCFB"

plt.rcParams.update({
    "font.family": FAMILY,
    "font.size": 12,
    "figure.facecolor": SUP,
    "axes.facecolor": SUP,
    "axes.edgecolor": SUAVE,
    "axes.labelcolor": TINTA2,
    "axes.titlesize": 14,
    "axes.titlecolor": TINTA,
    "xtick.color": TINTA2,
    "ytick.color": TINTA2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "grid.color": SUAVE,
    "grid.linewidth": 0.8,
    "lines.linewidth": 2.4,
    "savefig.facecolor": SUP,
})

# ── Datos (MM$ corrientes) ──────────────────────────────────────────────────
ANIOS = list(range(2013, 2026))

B1G_CMF = [162119.6, 154607.3, 157978.8, 166946.9, 151105.6, 160378.8, 172851.7,
           167977.0, 169632.0, 211583.6, 210131.0, 251908.9, 277518.8]
B1G_DAES = [0.0, 154.3, 3377.2, 3786.2, 3874.0, 5587.4, 2904.9, 3836.9,
            3740.9, 13799.8, 29504.6, 11287.8, 0.0]  # 2013 y 2025 sin cobertura DAES

D1_TOT = [61877.3, 58623.0, 64801.9, 72128.0, 76445.2, 82296.2, 85012.0,
          89698.9, 90726.0, 98747.2, 105309.0, 117579.4, 122763.2]
B2G_TOT = [100242.3, 96138.6, 96554.1, 98605.1, 78534.4, 83670.0, 90744.6,
           82115.0, 84555.8, 126636.3, 134326.6, 145617.2, 154755.6]

APORTE_EST = [0.119, 0.107, 0.102, 0.101, 0.086, 0.088, 0.090, 0.085, 0.073,
              0.086, 0.085, 0.085, 0.082]
APORTE_ESP = [0.113, 0.106, 0.104, 0.104, 0.101, 0.106, 0.101, 0.113, 0.084,
              0.080, 0.082, 0.077, 0.075]

ACTIVOS = [1434093.4, 1433274.6, 1561464.4, 1676817.7, 1843430.6, 2033489.7,
           2229477.7, 2586910.7, 2886670.0, 3233454.7, 3736816.3, 4164706.7,
           4481909.0]
F4 = [1274441.1, 1267625.9, 1354989.9, 1424771.8, 1578414.4, 1699568.9,
      1840175.1, 1873316.1, 1955032.9, 2376704.3, 2823975.3, 3123457.0,
      3369182.0]
F2 = [709177.9, 716197.5, 747250.6, 850229.6, 858659.3, 938557.9, 1062063.1,
      1357193.1, 1692111.5, 1885462.4, 2314442.1, 2596172.9, 2761339.0]

COB_ANIOS = list(range(2014, 2025))
COB_N = [2, 7, 9, 12, 14, 6, 10, 10, 19, 22, 11]

miles = FuncFormatter(lambda v, _: f"{v/1000:,.0f}".replace(",", "."))


def guardar(fig, nombre):
    ruta = OUT / nombre
    fig.savefig(ruta, dpi=200, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"escrito {ruta.relative_to(BASE)}")


# ── Fig. 1 — VAB del sector por segmento ────────────────────────────────────
def fig_vab_segmentos():
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.bar(ANIOS, B1G_CMF, color=ROJO, width=0.66, label="CAC supervisadas (CMF)")
    ax.bar(ANIOS, B1G_DAES, bottom=B1G_CMF, color=AZUL, width=0.66,
           linewidth=2, edgecolor=SUP, label="CAC no supervisadas (DAES)")
    ax.set_ylim(0, 320000)
    ax.yaxis.set_major_formatter(miles)
    ax.set_ylabel("Valor agregado bruto  ·  miles de MM$ corrientes")
    ax.set_xticks(ANIOS)
    ax.set_xticklabels(ANIOS, rotation=0, fontsize=10)
    ax.grid(axis="y", zorder=0)
    ax.set_axisbelow(True)

    ax.annotate("277.519 MM$\nen 2025", xy=(2025, 277518.8), xytext=(2022.3, 305000),
                color=TINTA, fontsize=11, ha="center",
                arrowprops=dict(arrowstyle="-", color=TINTA2, lw=1))
    ax.annotate("2013 y 2025 sin cobertura DAES", xy=(2019, -46000),
                color=TINTA2, fontsize=9.5, ha="center", annotation_clip=False)
    ax.legend(frameon=False, loc="upper left", fontsize=10.5)
    ax.set_title("El sector genera hoy 277 mil millones de pesos de valor agregado al año",
                 loc="left", pad=14)
    guardar(fig, "fig_vab_segmentos.png")


# ── Fig. 2 — Aporte al PIB: estimado vs. esperado ───────────────────────────
def fig_aporte_pib():
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.plot(ANIOS, APORTE_EST, color=ROJO, marker="o", markersize=6,
            markeredgecolor=SUP, markeredgewidth=1.6, zorder=3)
    ax.plot(ANIOS, APORTE_ESP, color=AZUL, marker="o", markersize=6,
            markeredgecolor=SUP, markeredgewidth=1.6, linestyle=(0, (5, 2)), zorder=3)
    ax.set_ylim(0, 0.14)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.2f}".replace(".", ",") + "%"))
    ax.set_ylabel("Aporte al PIB nacional")
    ax.set_xticks(ANIOS)
    ax.set_xticklabels(ANIOS, fontsize=10)
    ax.grid(axis="y")
    ax.set_axisbelow(True)

    ax.text(2025.15, APORTE_EST[-1], "  estimado\n  por el estudio", color=ROJO,
            fontsize=10.5, va="center")
    ax.text(2025.15, APORTE_ESP[-1] - 0.006, "  esperado según\n  peso patrimonial", color=AZUL,
            fontsize=10.5, va="center")
    ax.set_xlim(2012.4, 2028.6)
    ax.set_title("Las CAC aportan entre 0,07% y 0,12% del PIB — y la estimación\n"
                 "coincide con la referencia externa independiente",
                 loc="left", pad=14)
    ax.annotate("Eje anclado en cero: la caída relativa es de 39%, no de 90%",
                xy=(2013, 0.006), color=TINTA2, fontsize=9.5)
    guardar(fig, "fig_aporte_pib.png")


# ── Fig. 3 — De los ingresos al valor agregado (cascada, 2025) ──────────────
def fig_cascada():
    fig, ax = plt.subplots(figsize=(10, 4.8))
    p1, p2 = 445885.0, 445885.0 * 0.3776
    b1g = p1 - p2
    d1, b2g = 122763.2, 154755.6

    etiquetas = ["Producción\n(P1)", "Consumo\nintermedio (P2)", "Valor agregado\nbruto (B1g)",
                 "Remuneraciones\n(D1)", "Excedente\n(B2g)"]
    bases = [0, b1g, 0, 0, d1]
    alturas = [p1, p2, b1g, d1, b2g]
    colores = [TINTA2, SUAVE, ROJO, AZUL, AMBAR]

    ax.bar(range(5), alturas, bottom=bases, color=colores, width=0.6)
    for i, (b, h) in enumerate(zip(bases, alturas)):
        ax.text(i, b + h + 9000, f"{h/1000:,.0f}".replace(",", "."),
                ha="center", fontsize=11.5, color=TINTA)
    ax.set_xticks(range(5))
    ax.set_xticklabels(etiquetas, fontsize=10.5)
    ax.set_ylim(0, 500000)
    ax.yaxis.set_major_formatter(miles)
    ax.set_ylabel("miles de MM$ (2025)")
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.set_title("Cómo se calcula el aporte: P1 − P2 = B1g, y el B1g se reparte\n"
                 "entre trabajadores y excedente cooperativo", loc="left", pad=14)
    guardar(fig, "fig_cascada.png")


# ── Fig. 4 — Cobertura del panel DAES ───────────────────────────────────────
def fig_cobertura():
    fig, ax = plt.subplots(figsize=(10, 4.4))
    colores = [AZUL if n < 22 else ROJO for n in COB_N]
    ax.bar(COB_ANIOS, COB_N, color=colores, width=0.66)
    ax.axhline(38, color=TINTA2, linestyle=(0, (4, 3)), linewidth=1.6)
    ax.text(2014, 39, "38 CAC vigentes en el registro DAES", color=TINTA2, fontsize=10.5)
    for a, n in zip(COB_ANIOS, COB_N):
        ax.text(a, n + 1.2, str(n), ha="center", fontsize=10.5, color=TINTA)
    ax.set_ylim(0, 46)
    ax.set_xticks(COB_ANIOS)
    ax.set_xticklabels(COB_ANIOS, fontsize=10)
    ax.set_ylabel("CAC con estado financiero publicado")
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.set_title("El techo del estudio no es metodológico: es que las memorias no están publicadas",
                 loc="left", pad=14)
    guardar(fig, "fig_cobertura_daes.png")


# ── Fig. 5 — Balance agregado del sector ────────────────────────────────────
def fig_balance():
    fig, ax = plt.subplots(figsize=(10, 5.0))
    ax.plot(ANIOS, ACTIVOS, color=ROJO, marker="o", markersize=5.5,
            markeredgecolor=SUP, markeredgewidth=1.4)
    ax.plot(ANIOS, F4, color=AZUL, marker="o", markersize=5.5,
            markeredgecolor=SUP, markeredgewidth=1.4)
    ax.plot(ANIOS, F2, color=AMBAR, marker="o", markersize=5.5,
            markeredgecolor=SUP, markeredgewidth=1.4)
    ax.set_ylim(0, 5200000)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v/1_000_000:,.1f}".replace(".", ",")))
    ax.set_ylabel("billones de pesos corrientes")
    ax.set_xticks(ANIOS)
    ax.set_xticklabels(ANIOS, fontsize=10)
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.text(2025.15, ACTIVOS[-1], "  Activos", color=ROJO, fontsize=11, va="center")
    ax.text(2025.15, F4[-1], "  Colocaciones netas", color=AZUL, fontsize=11, va="center")
    ax.text(2025.15, F2[-1], "  Depósitos captados", color=AMBAR, fontsize=11, va="center")
    ax.set_xlim(2012.4, 2029.5)
    ax.set_title("Los activos del sector se multiplicaron por 3,1 y los depósitos por 3,9\n"
                 "entre 2013 y 2025", loc="left", pad=14)
    guardar(fig, "fig_balance.png")


# ── Fig. 6 — Reparto del valor agregado ─────────────────────────────────────
def fig_reparto():
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.bar(ANIOS, D1_TOT, color=AZUL, width=0.66, label="Remuneraciones (D1)")
    ax.bar(ANIOS, B2G_TOT, bottom=D1_TOT, color=AMBAR, width=0.66,
           linewidth=2, edgecolor=SUP, label="Excedente bruto de explotación (B2g)")
    ax.set_ylim(0, 320000)
    ax.yaxis.set_major_formatter(miles)
    ax.set_ylabel("miles de MM$ corrientes")
    ax.set_xticks(ANIOS)
    ax.set_xticklabels(ANIOS, fontsize=10)
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper left", fontsize=10.5)
    ax.set_title("Entre 38% y 52% del valor agregado del sector va directo a remuneraciones\n"
                 "122.763 MM$ en 2025", loc="left", pad=14)
    guardar(fig, "fig_reparto_vab.png")


# ── Fig. 7 — La ecuación central ────────────────────────────────────────────
def fig_ecuacion():
    """La ecuación se genera como imagen y no como math del documento: así se ve
    idéntica en Beamer y en RevealJS sin depender de MathJax/KaTeX por CDN."""
    fig, ax = plt.subplots(figsize=(10, 2.6))
    ax.axis("off")
    ax.text(0.5, 0.62, r"$B1g \;=\; P1 \;-\; P2$", ha="center", va="center",
            fontsize=38, color=TINTA)
    ax.text(0.235, 0.16, "valor agregado", ha="center", fontsize=15, color=ROJO)
    ax.text(0.525, 0.16, "producción", ha="center", fontsize=15, color=TINTA2)
    ax.text(0.775, 0.16, "consumo intermedio", ha="center", fontsize=15, color=TINTA2)
    for x0, x1 in ((0.16, 0.31), (0.46, 0.59), (0.70, 0.85)):
        ax.plot([x0, x1], [0.36, 0.36], color=SUAVE, lw=2, solid_capstyle="butt")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    guardar(fig, "fig_ecuacion.png")


# ── Fig. 8 — Distribución regional ──────────────────────────────────────────
def fig_regional():
    """Recreación en la paleta de la presentación de la Figura 5.3 de la memoria
    (catastro regional del proyecto, 36 CAC)."""
    regiones = ["Los Lagos", "Arica y Parinacota", "Antofagasta", "Coquimbo",
                "Biobío", "Maule", "Araucanía", "Valparaíso", "R. Metropolitana"]
    n = [1, 1, 1, 2, 2, 2, 3, 4, 20]
    fig, ax = plt.subplots(figsize=(10, 4.8))
    colores = [ROJO if r == "R. Metropolitana" else AZUL for r in regiones]
    ax.barh(regiones, n, color=colores, height=0.66)
    for r, v in zip(regiones, n):
        ax.text(v + 0.35, r, str(v), va="center", fontsize=11.5, color=TINTA)
    ax.set_xlim(0, 23)
    ax.set_xlabel("N.º de cooperativas de ahorro y crédito")
    ax.grid(axis="x")
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    ax.set_title("La Región Metropolitana concentra 20 de las 36 CAC del catastro (56 %)",
                 loc="left", pad=14)
    guardar(fig, "fig_regional.png")


if __name__ == "__main__":
    fig_ecuacion()
    fig_regional()
    fig_vab_segmentos()
    fig_aporte_pib()
    fig_cascada()
    fig_cobertura()
    fig_balance()
    fig_reparto()
