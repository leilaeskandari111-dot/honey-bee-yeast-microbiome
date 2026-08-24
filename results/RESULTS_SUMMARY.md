# Results Summary

## 1. Core yeast-associated taxa

The supplementary ASV table contained 221 ASVs classified within the class Saccharomycetes.

Using a ≥75% prevalence threshold as an operational definition of highly prevalent taxa, 15 yeast-associated ASVs were identified as highly prevalent across the available samples.

These taxa represent a widespread component of the yeast-associated fungal community and provide candidate taxa for investigating ecological stability in the honey-bee hindgut.

## 2. Treatment-responsive yeasts

Treatment-specific differential-abundance results were screened at q < 0.05.

The analysis distinguishes between two biologically different patterns:

- widespread, high-prevalence yeast-associated ASVs
- lower-prevalence taxa showing stronger treatment-associated responses

This distinction is important because a taxon can be ecologically widespread without necessarily being strongly responsive to probiotic treatment.

Examples of yeast-associated genera represented in the analysis include Hanseniaspora, Lachancea, Kodamaea, Candida, Metschnikowia and Zygosaccharomyces.

## 3. Probiotic delivery and fungal communities

The experimental design included two probiotic delivery approaches:

- pollen-patty delivery
- spray delivery

Both probiotic and vehicle-control groups were considered in the study design.

The original study investigated whether delivery method influenced the interaction between the LX3 probiotic treatment and the native fungal community.

This project therefore treats delivery method as an important ecological variable rather than considering probiotic treatment as a single homogeneous condition.

## 4. Raw-read quality control

A representative SRA run, SRR20011368, was independently inspected.

The run contained 39,478 paired spots.

Observed read characteristics included:

- R1 median length: approximately 243 bp
- R2 median length: approximately 244 bp
- Mean Phred quality: approximately Q29.85 for R1
- Mean Phred quality: approximately Q29.08 for R2

These results indicate generally good raw-read quality for the representative sequencing run.

## 5. Primer assessment and read overlap

ITS1f and ITS2 primer sequences were identified from the study's supplementary information and checked against the representative raw reads.

Only 17 of 39,478 read pairs showed an exact raw-read overlap of at least 20 bp.

After considering the biological primer regions, sufficient exact overlap was essentially absent.

This observation is important for reproducibility because a conventional overlap-based paired-end merge should not be assumed to succeed automatically for this ITS dataset.

The published study reports DADA2-based processing and merging, but the exact merge configuration is not fully specified in the article methods.

## 6. Interpretation

The analysis highlights two complementary aspects of the honey-bee hindgut fungal community:

1. highly prevalent yeast-associated taxa that may represent stable members of the community
2. less prevalent taxa that may nevertheless respond to probiotic treatment or delivery conditions

Together, these analyses provide a microbial-ecology perspective on how probiotic interventions may interact with the native fungal community of the honey-bee hindgut.

## 7. Reproducibility boundary

The repository does not claim that the complete 198-run DADA2 pipeline has already been independently regenerated.

The raw-read QC and primer assessment were independently performed on SRR20011368.

The prevalence and differential-abundance results were independently extracted or reanalyzed from the authors' supplementary ASV and statistical tables.

A reproducible DADA2 workflow is provided in:

`scripts/02_dada2_ITS.R`

The workflow should be executed in an appropriate R/Bioconductor environment before claiming a fully regenerated ASV table.

## 8. Next analysis steps

Future work will focus on:

- reproducing the complete ITS processing workflow
- comparing regenerated ASVs with the published supplementary ASV table
- investigating alpha and beta diversity
- testing treatment and delivery-method effects
- characterizing yeast-associated taxa at genus and species levels
- integrating fungal-community results with microbial-ecology interpretation
