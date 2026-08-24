# Honey Bee Hindgut Yeast Microbiome

## Project goal

A reproducible bioinformatics and microbial-ecology project using publicly available ITS amplicon sequencing data from a longitudinal *Apis mellifera* hindgut microbiome study.

**Research question:** How does probiotic delivery method influence the prevalence and treatment responsiveness of yeast-associated fungal taxa in the honey-bee hindgut?

## Dataset

- Study: Daisley et al., *The ISME Journal* (2023)
- Article: "Delivery mechanism can enhance probiotic activity against honey bee pathogens"
- ITS BioProject: **PRJNA856341**
- Sequencing: Illumina MiSeq, paired-end
- Public SRA records: 198 runs
- Original study reported 3,387 fungal ASVs after DADA2 processing.

Source article: https://doi.org/10.1038/s41396-023-01422-z
SRA BioProject: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA856341
Original authors' code: https://github.com/bdaisley/LX3CA1

## Experimental design

Groups:
- NTC — no treatment control
- PP — patty + LX3
- PV — patty vehicle
- SP — spray + LX3
- SV — spray vehicle

Timepoints:
W0, W2, W4, W8, W12, W24

## Analyses completed

### 1. Raw-read quality control
A representative SRA run, `SRR20011368` (NTC, W0), was inspected.

- 39,478 paired spots
- R1 median length: ~243 bp
- R2 median length: ~244 bp
- Mean Phred quality: ~29.85 (R1), ~29.08 (R2)

The SRA FASTQ was downloaded as an interleaved file and separated into matched R1/R2 files for inspection.

### 2. Primer identification
The study used ITS1f/ITS2 primer constructs. In the representative run, the biological primer portions detected at the beginning of reads were approximately:

- Forward ITS1f: `GGCTTGGTCATTTAGAGGAAGTAA`
- Reverse ITS2: `CGGCTGCGTTCTTCATCGATGC`

The full constructs, including barcode/adapter sequences, are documented in Supplementary Data 1B.

### 3. Yeast prevalence
From the authors' supplementary ASV table, 221 ASVs were classified as Saccharomycetes.

Using an operational threshold of >=75% prevalence, 15 yeast-associated ASVs were identified as highly prevalent.

### 4. Treatment responsiveness
Treatment-specific differential-abundance results were screened at q < 0.05.

The analysis distinguishes:
- widespread/high-prevalence yeast-associated ASVs
- lower-prevalence but treatment-responsive taxa

Examples include *Hanseniaspora*, *Lachancea*, *Kodamaea*, *Candida*, *Metschnikowia* and *Zygosaccharomyces*.

## Important methodological note

The current repository **does not claim that the complete 198-sample DADA2 pipeline was independently re-run here**.

The raw-read QC and primer checks were independently performed on `SRR20011368`. The prevalence and differential-abundance results were independently extracted/reanalyzed from the authors' supplementary ASV and statistical tables.

A full 198-sample DADA2 regeneration is provided as a reproducible R workflow in `scripts/02_dada2_ITS.R`, but should be executed in an R/Bioconductor environment before claiming a fully regenerated ASV table.

During the representative-read overlap check, only 17/39,478 pairs showed an exact overlap of at least 20 bp in the raw reads. After removing the biological primer portions, essentially no pairs retained a >=20-bp exact overlap. This is important for interpreting the DADA2 workflow: a standard overlap-based `mergePairs()` should not be assumed to succeed for this ITS dataset. The original paper states that forward and reverse reads were merged with DADA2, but the paper does not specify the exact merge setting in the methods. Therefore this repository does **not** claim a reproduced 198-sample DADA2 merge yet.

The next defensible step is to reproduce the authors' published pipeline as closely as possible, inspect the original command-line settings where available, and compare the resulting ASV count/sequence output with Supplementary Data 1C. If the workflow used DADA2 concatenation or another non-overlap strategy, that choice should be documented explicitly.

## Repository structure

```text
honey-bee-yeast-microbiome/
├── data/
│   ├── metadata/
│   │   ├── SraRun_metadata.csv
│   │   └── design_metadata_template.csv
│   └── supplementary_results/
├── figures/
├── results/
│   ├── core_yeast_ASVs_75pct.csv
│   └── yeast_treatment_DA_summary_q05.csv
├── scripts/
│   ├── 01_raw_qc_notes.md
│   ├── 02_dada2_ITS.R
│   └── 03_yeast_prevalence_analysis.py
├── docs/
│   └── project_notes.md
├── .gitignore
├── LICENSE
└── README.md
```

## Skills demonstrated

- Amplicon sequencing QC
- FASTQ handling
- ITS primer identification
- DADA2 workflow design
- ASV-based microbial profiling
- Taxonomic filtering
- Prevalence analysis
- Differential-abundance interpretation
- Microbial ecology
- Reproducible research
- Python and R
- Git/GitHub project organization

## CV-ready description

> **Honey Bee Hindgut Mycobiome — Bioinformatics Project**  
> Analyzed publicly available ITS amplicon sequencing data from *Apis mellifera* hindgut samples. Performed raw-read QC, primer identification, ASV-level yeast prevalence analysis and treatment-response analysis, with emphasis on distinguishing widespread taxa from treatment-responsive yeasts. Developed a reproducible R/Python workflow for DADA2-based ITS processing and organized the analysis as a version-controlled GitHub project.

## Citation

Daisley BA et al. (2023). Delivery mechanism can enhance probiotic activity against honey bee pathogens. *The ISME Journal*, 17, 1382–1395. https://doi.org/10.1038/s41396-023-01422-z
