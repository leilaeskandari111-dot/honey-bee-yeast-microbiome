# Raw-read QC notes — SRR20011368

Representative run:
- SRA: SRR20011368
- Sample: fungi_NTC_W0_G_001
- 39,478 paired spots
- Raw FASTQ supplied as an interleaved file
- Split into matched R1/R2 files for QC

Observed:
- R1 median length ≈243 bp
- R2 median length ≈244 bp
- Mean Phred ≈29.85 (R1), ≈29.08 (R2)
- Primer portions were detected at read starts.
- Most pairs did not show sufficient exact R1/R2 overlap after primer removal.

Interpretation:
The ITS region is biologically length-variable. The lack of overlap for most reads means a standard mergePairs analysis should not be assumed to succeed. A justified alternative is DADA2's justConcatenate option, after evaluating the complete dataset and checking the resulting ASV/taxonomy quality.
