data <- read.table("prepass-genotype.dat")

sample.id.real <- array(1:1000)
snp.id.real <- array(1:9445)
snp.position.real <- rep(0, 9445)
snp.chromosome.real <- rep(0, 9445)
snp.rs.id.real <- character(9445)
snp.allele.real <- character(9445)

for (i in 1:ncol(data)) {
    snp.rs.id.real[i] = as.character(data[1, i])
    snp.allele.real[i] = 'A/G'
}

library("gdsfmt")
library("SNPRelate")
snpgdsCreateGeno("pca.gds", sample.id = sample.id.real,
                 snp.rs.id = snp.rs.id.real,
                 snp.id = snp.id.real,
                 snp.position = snp.position.real,
                 snp.chromosome = snp.chromosome.real,
                 genmat = data.matrix(data[2:1001,]) - 1,
                 snpfirstdim=FALSE,
                 snp.allele = snp.allele.real
                 )
