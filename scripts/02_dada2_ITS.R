# 02_dada2_ITS.R
# Reproducible ITS processing workflow for the honey-bee dataset.
# Run in an R/Bioconductor environment with dada2 + ShortRead installed.
#
# IMPORTANT:
# This script is a workflow template. Do not claim that the full dataset
# was independently regenerated until this script has been executed.

library(dada2)
library(Biostrings)

# ---- paths ----
path <- "data/raw"                 # place demultiplexed R1/R2 FASTQ files here
out <- "data/dada2"
dir.create(out, recursive=TRUE, showWarnings=FALSE)

fnFs <- sort(list.files(path, pattern="_1.fastq.gz$", full.names=TRUE))
fnRs <- sort(list.files(path, pattern="_2.fastq.gz$", full.names=TRUE))
stopifnot(length(fnFs) == length(fnRs), length(fnFs) > 0)

sample.names <- sub("_1.fastq.gz$", "", basename(fnFs))

# ---- ITS primers ----
# Biological primer portions observed in this study's reads.
FWD <- "GGCTTGGTCATTTAGAGGAAGTAA"
REV <- "CGGCTGCGTTCTTCATCGATGC"
FWD.RC <- dada2:::rc(FWD)
REV.RC <- dada2:::rc(REV)

# Primer removal is best done with Cutadapt before DADA2 filtering.
# Example command (run from shell):
#
# cutadapt -g FWD -a REV.RC -G REV -A FWD.RC \
#   --minimum-length 50 \
#   -o data/trimmed/{name}_1.fastq.gz \
#   -p data/trimmed/{name}_2.fastq.gz \
#   data/raw/{name}_1.fastq.gz data/raw/{name}_2.fastq.gz

trim.path <- "data/trimmed"
fnFs.cut <- sort(list.files(trim.path, pattern="_1.fastq.gz$", full.names=TRUE))
fnRs.cut <- sort(list.files(trim.path, pattern="_2.fastq.gz$", full.names=TRUE))

# ---- quality filtering ----
filt.path <- file.path(out, "filtered")
dir.create(filt.path, recursive=TRUE, showWarnings=FALSE)
filtFs <- file.path(filt.path, basename(fnFs.cut))
filtRs <- file.path(filt.path, basename(fnRs.cut))

out.track <- filterAndTrim(
  fnFs.cut, filtFs,
  fnRs.cut, filtRs,
  maxN=0,
  maxEE=c(2,2),
  truncQ=2,
  minLen=50,
  rm.phix=TRUE,
  compress=TRUE,
  multithread=FALSE
)

write.csv(out.track, file.path(out,"filter_tracking.csv"))

# ---- learn errors ----
errF <- learnErrors(filtFs, multithread=FALSE)
errR <- learnErrors(filtRs, multithread=FALSE)

saveRDS(errF, file.path(out,"errF.rds"))
saveRDS(errR, file.path(out,"errR.rds"))

# ---- denoise ----
dadaFs <- dada(filtFs, err=errF, multithread=FALSE)
dadaRs <- dada(filtRs, err=errR, multithread=FALSE)

# ITS amplicons can exceed the total paired-read span.
# First try normal merging. If most reads fail to merge because the
# biological insert is longer than the combined read length, use
# justConcatenate=TRUE and document this choice.
mergers <- mergePairs(dadaFs, filtFs, dadaRs, filtRs, verbose=TRUE)

# Optional alternative for non-overlapping ITS reads:
# mergers <- mergePairs(
#   dadaFs, filtFs, dadaRs, filtRs,
#   justConcatenate=TRUE, verbose=TRUE
# )

seqtab <- makeSequenceTable(mergers)
seqtab.nochim <- removeBimeraDenovo(
  seqtab, method="consensus", multithread=FALSE, verbose=TRUE
)

saveRDS(seqtab.nochim, file.path(out,"seqtab_nochim.rds"))
write.csv(seqtab.nochim, file.path(out,"ASV_table.csv"))

# ---- read tracking ----
getN <- function(x) sum(getUniques(x))
track <- cbind(
  out.track,
  denoisedF=sapply(dadaFs,getN),
  denoisedR=sapply(dadaRs,getN),
  merged=sapply(mergers,getN),
  nonchim=rowSums(seqtab.nochim)
)
write.csv(track,file.path(out,"pipeline_tracking.csv"))
