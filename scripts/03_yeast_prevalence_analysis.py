# 03_yeast_prevalence_analysis.py
# Re-analysis of yeast-associated ASVs from Supplementary Data 1C.
import pandas as pd
import numpy as np

xlsx = "data/supplementary_results/41396_2023_1422_MOESM2_ESM.xlsx"

asv = pd.read_excel(xlsx, sheet_name="1C", header=2)
asv = asv[asv["ASV identifier"].astype(str).str.startswith("fSV_")].copy()
asv["Prevalence"] = pd.to_numeric(
    asv["Prevalence (1=present in all samples)"], errors="coerce"
)

def rank(tax, i):
    p = str(tax).split(";")
    return p[i] if len(p) > i else "Unclassified"

tax_col = "Classification w/ denovo placeholder names used in this study"
asv["Class"] = asv[tax_col].map(lambda x: rank(x,2))
asv["Genus"] = asv[tax_col].map(lambda x: rank(x,5))
asv["Species"] = asv[tax_col].map(lambda x: rank(x,6))

yeast = asv[asv["Class"].str.contains("Saccharomycetes", case=False, na=False)]
core = yeast[yeast["Prevalence"] >= 0.75]

core[["ASV identifier","Prevalence","Genus","Species"]].to_csv(
    "results/core_yeast_ASVs_75pct.csv", index=False
)

print("Yeast-associated ASVs:", len(yeast))
print("Highly prevalent yeast ASVs (>=75%):", len(core))
