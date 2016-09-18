library("gdsfmt")
library("SNPRelate")

genofile <- snpgdsOpen("pca-2.gds")
pca <- snpgdsPCA(genofile, autosome.only = FALSE, algorithm = "exact", num.thread = 4, iter.num = 20)
dim(pca$eigenvect)