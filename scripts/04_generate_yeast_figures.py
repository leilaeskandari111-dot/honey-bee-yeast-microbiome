# 04_generate_yeast_figures.py
# Generate reproducible figures for the honey-bee yeast microbiome project

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# Paths
# =========================================================

ROOT = Path(__file__).resolve().parents[1]

CORE_FILE = ROOT / "results" / "core_yeast_ASVs_75pct.csv"
DA_FILE = ROOT / "results" / "yeast_treatment_DA_summary_q05.csv"

FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# Load data
# =========================================================

core = pd.read_csv(CORE_FILE)
da = pd.read_csv(DA_FILE)

core.columns = core.columns.str.strip()
da.columns = da.columns.str.strip()

core["Prevalence"] = pd.to_numeric(
    core["Prevalence"],
    errors="coerce"
)

da["significant_ASVs"] = pd.to_numeric(
    da["significant_ASVs"],
    errors="coerce"
)

da["max_abs_coef"] = pd.to_numeric(
    da["max_abs_coef"],
    errors="coerce"
)

da["best_q"] = pd.to_numeric(
    da["best_q"],
    errors="coerce"
)


# =========================================================
# Figure 1
# Yeast prevalence versus treatment responsiveness
# =========================================================

# One prevalence value per genus:
# use the highest prevalence among ASVs belonging to that genus.

genus_prevalence = (
    core.dropna(subset=["Genus", "Prevalence"])
    .groupby("Genus", as_index=False)["Prevalence"]
    .max()
)

# Merge with treatment-response summary
plot1 = genus_prevalence.merge(
    da[
        [
            "Genus",
            "significant_ASVs",
            "best_q"
        ]
    ],
    on="Genus",
    how="inner"
)

plot1["significant_ASVs"] = plot1[
    "significant_ASVs"
].fillna(0)

plot1 = plot1.sort_values(
    ["Prevalence", "significant_ASVs"],
    ascending=[False, False]
)

fig, ax = plt.subplots(figsize=(10, 7))

ax.scatter(
    plot1["Prevalence"] * 100,
    plot1["significant_ASVs"],
    s=90,
    alpha=0.85
)

# 75% prevalence threshold
ax.axvline(
    75,
    linestyle="--",
    linewidth=1.2,
    label="75% prevalence threshold"
)

# Label points
for i, row in plot1.reset_index(drop=True).iterrows():

    genus = str(row["Genus"])

    offsets = [
        (6, 7),
        (6, -12),
        (6, 14),
        (6, -18)
    ]

    dx, dy = offsets[i % len(offsets)]

    ax.annotate(
        genus,
        (
            row["Prevalence"] * 100,
            row["significant_ASVs"]
        ),
        xytext=(dx, dy),
        textcoords="offset points",
        fontsize=8
    )


ax.set_xlabel(
    "Prevalence (%)",
    fontsize=12
)

ax.set_ylabel(
    "Significant ASV-level treatment comparisons",
    fontsize=12
)

ax.set_title(
    "Yeast prevalence versus treatment responsiveness",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlim(
    max(70, plot1["Prevalence"].min() * 100 - 3),
    101
)

ax.grid(
    axis="both",
    alpha=0.2
)

ax.legend(
    frameon=False,
    loc="upper left"
)

plt.tight_layout()

fig.savefig(
    FIG_DIR / "honey_bee_yeast_prevalence_vs_response.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)


# =========================================================
# Figure 2
# Differential-abundance response
# =========================================================

da_plot = da.copy()

da_plot = da_plot.dropna(
    subset=[
        "Genus",
        "max_abs_coef",
        "best_q"
    ]
)

# Keep the strongest 20 genera for readable visualization
da_plot = da_plot.sort_values(
    "max_abs_coef",
    ascending=True
).tail(20)


fig, ax = plt.subplots(figsize=(10, 8))

bars = ax.barh(
    da_plot["Genus"],
    da_plot["max_abs_coef"],
    alpha=0.85
)

# Add coefficient and q-value
for bar, (_, row) in zip(
    bars,
    da_plot.iterrows()
):

    value = row["max_abs_coef"]
    q = row["best_q"]

    ax.text(
        value + max(0.03, value * 0.015),
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}  (q={q:.2g})",
        va="center",
        fontsize=8
    )


ax.set_xlabel(
    "Maximum absolute differential-abundance coefficient",
    fontsize=12
)

ax.set_ylabel(
    "Yeast genus",
    fontsize=12
)

ax.set_title(
    "Differential-abundance response of yeast-associated taxa",
    fontsize=14,
    fontweight="bold"
)

ax.grid(
    axis="x",
    alpha=0.2
)

plt.tight_layout()

fig.savefig(
    FIG_DIR / "honey_bee_yeast_differential_abundance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close(fig)


# =========================================================
# Confirmation
# =========================================================

print("Figures generated successfully.")

print(
    FIG_DIR /
    "honey_bee_yeast_prevalence_vs_response.png"
)

print(
    FIG_DIR /
    "honey_bee_yeast_differential_abundance.png"
)
