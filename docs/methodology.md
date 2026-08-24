# Methodology

## Dataset
Public ITS amplicon sequencing data from BioProject PRJNA856341.

## Experimental factors
The study compares no-treatment controls, vehicle controls, and LX3 probiotic treatments delivered by patty or spray across W0, W2, W4, W8, W12 and W24.

## Independent work in this repository

1. SRA run metadata was obtained for all 198 ITS sequencing runs.
2. A representative raw SRA run (SRR20011368) was downloaded.
3. The interleaved FASTQ was separated into R1/R2.
4. Read length and Phred quality profiles were calculated.
5. ITS1f and ITS2 primer sequences were identified from Supplementary Data 1B and checked against raw reads.
6. Yeast-associated ASVs were extracted from Supplementary Data 1C.
7. A >=75% prevalence threshold was used as an operational definition of highly prevalent yeast-associated ASVs.
8. Treatment-specific differential-abundance results were screened at q < 0.05.

## Reproducibility boundary

The published paper reports DADA2 processing and 3,387 fungal ASVs. This repository currently uses the authors' supplementary ASV/statistical tables for the main ecological results and independently validates raw-read QC on one representative SRA run.

A full 198-run DADA2 regeneration is intentionally marked as **pending reproduction**, because the exact original merge/primer-processing settings are not fully specified in the article text. The repository contains a reproducible workflow template for that step.
