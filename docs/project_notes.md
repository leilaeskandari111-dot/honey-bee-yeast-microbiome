# Project notes

## Main ecological question

Are widespread yeast-associated taxa stable across the honey-bee hindgut community, while lower-prevalence taxa show stronger responses to probiotic treatment?

## Key distinction

Prevalence measures how frequently a taxon is detected across samples. It does not measure relative abundance.

Differential-abundance coefficients are model effect sizes, not relative-abundance percentages.

Therefore this project keeps:
1. prevalence,
2. abundance,
3. differential response

as separate concepts.

## Current evidence

The supplementary ASV table contains 3,387 fungal ASVs. 221 were classified within Saccharomycetes. At a >=75% ASV prevalence threshold, 15 yeast-associated ASVs were identified.

Treatment-specific differential-abundance screening at q<0.05 identifies responsive yeast-associated ASVs in genera including Hanseniaspora, Lachancea, Kodamaea, Candida, Metschnikowia and Zygosaccharomyces.

## Next computational extension

Run the complete DADA2 pipeline on all 198 ITS runs, assign taxonomy with UNITE, construct a phyloseq object, calculate relative abundance, and compare the independently regenerated ASV table against the published supplementary results.
