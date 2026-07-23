r""" de la sección 5.4 (Panel interactivo de
visualización) como PNG estáticos con matplotlib, para reemplazar los
pantallazos recortados del dashboard Plotly.

Pensado para correr dentro del Python Script Runner de Overleaf (Pyodide):
  - Solo usa matplotlib y pandas (ambos soportados en Pyodide).
  - Los datos están embebidos como listas (mismos valores que los Cuadros
    5.2, 5.3 y el registro de cooperativas), así no depende de subir los
    .xlsx completos al proyecto de Overleaf.
  - Al correr, guarda fig_5_1_cmf.png, fig_5_2_daes.png y fig_5_3_regional.png
    en el árbol de archivos del proyecto -> \includegraphics{fig_5_1_cmf.png}
"""

import os
import matplotlib.pyplot as plt
import numpy as np



plt.rcParams.update({
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# ─────────────────────────────────────────────────────────────────────────
# Figura 5.1 — Segmento CMF: VAB bruto (B1g) y aporte al PIB
# ─────────────────────────────────────────────────────────────────────────
anios_cmf = [2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
n_cmf     = [7]*13
b1g_cmf   = [162119.64,154607.33,157978.81,166946.91,151105.65,160378.79,
             172851.68,167977.05,171540.91,211583.64,210130.95,251908.93,277518.82]
aporte_cmf = [0.119203,0.106842,0.099594,0.098923,0.084268,0.084662,0.088393,
              0.083443,0.071608,0.080464,0.074489,0.081083,0.081628]

fig, ax1 = plt.subplots(figsize=(6.3, 3.6))
ax2 = ax1.twinx()

bars = ax1.bar(anios_cmf, b1g_cmf, color="#1a56db", width=0.65,
                label="B1g (MM$)", zorder=2)
ax2.plot(anios_cmf, aporte_cmf, color="#16a34a",
        marker="o", markersize=4, linewidth=1.8, label="Aporte PIB (%)",
        zorder=3)

# Espacio arriba para las etiquetas N= sin recortarse
ax1.set_ylim(0, max(b1g_cmf) * 1.28)

for x, y, n in zip(anios_cmf, b1g_cmf, n_cmf):
    ax1.annotate(f"N={n}", (x, y), textcoords="offset points",
                 xytext=(0, 6), ha="center", fontsize=7.5, color="#334155")

ax1.set_ylabel("MM$")
ax2.set_ylabel("Aporte PIB (%)")
ax1.set_xticks(anios_cmf)
ax1.set_xticklabels(anios_cmf, rotation=45, ha="right")
ax1.margins(x=0.02)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center",
           bbox_to_anchor=(0.5, 1.18), ncol=2, frameon=False)

fig.tight_layout()
fig.savefig("CMF.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ─────────────────────────────────────────────────────────────────────────
# Figura 5.2 — Segmento DAES: VAB bruto (B1g) y N cooperativas con dato
# ─────────────────────────────────────────────────────────────────────────
anios_daes = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
n_daes     = [2,7,9,12,14,6,10,10,19,22,11]
b1g_daes   = [154.29,3377.18,3786.21,3873.97,5587.45,2904.90,3836.87,
              3740.95,13799.85,29504.64,11287.76]

fig, ax1 = plt.subplots(figsize=(6.3, 3.6))
ax2 = ax1.twinx()

ax1.bar(anios_daes, b1g_daes, color="#8e44ad", width=0.6,
        label="B1g (MM$)", zorder=2)
ax2.plot(anios_daes, n_daes, color="#f39c12", marker="o", markersize=4,
         linestyle=":", linewidth=2, label="N cooperativas", zorder=3)

ax1.set_ylim(0, max(b1g_daes) * 1.28)

for i, (x, y, n) in enumerate(zip(anios_daes, b1g_daes, n_daes)):
    # el primer punto (2014) queda muy pegado a la línea naranja; lo despegamos un poco
    dy = 14 if i == 0 else 6
    ax1.annotate(f"N={n}", (x, y), textcoords="offset points",
                 xytext=(0, dy), ha="center", fontsize=7.5, color="#334155")

ax1.set_ylabel("MM$")
ax2.set_ylabel("N cooperativas")
ax1.set_xticks(anios_daes)
ax1.margins(x=0.03)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center",
           bbox_to_anchor=(0.5, 1.18), ncol=2, frameon=False)

fig.tight_layout()
fig.savefig("DAES.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ─────────────────────────────────────────────────────────────────────────
# Figura 5.3 — Distribución regional de las CAC vigentes (DAES + CMF)
# ─────────────────────────────────────────────────────────────────────────
regiones = ["Los Lagos","Arica y Parinacota","Antofagasta","Coquimbo",
            "Biobío","Maule","Araucanía","Valparaíso","R. Metropolitana"]
conteos  = [1,1,1,2,2,2,3,5,22]
total = sum(conteos)

fig, ax = plt.subplots(figsize=(6.3, 3.6))
bars = ax.barh(regiones, conteos, color=["#6366f1"]*8 + ["#1a56db"])
ax.set_xlabel("N° CAC")
ax.set_xlim(0, max(conteos) * 1.18)  # espacio a la derecha para las etiquetas

for bar, c in zip(bars, conteos):
    ax.annotate(str(c), (bar.get_width(), bar.get_y() + bar.get_height()/2),
                textcoords="offset points", xytext=(5, 0),
                va="center", fontsize=8.5, color="#334155")

fig.tight_layout()
fig.savefig("dash_regional2.png", dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"OK: 3 figuras generadas. Total CAC en Fig 5.3: {total}")