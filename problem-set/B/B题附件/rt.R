library(randomForest)
library(doParallel)
sink("r-output.txt", append=FALSE, split=FALSE)
rtdata <- read.table("prepass-for-rt.dat", header = TRUE)
rtdata[, 'healthy'] <- as.factor(rtdata[, 'healthy'])

for (i in 2:9454) {
    rtdata <- rtdata[-2]
    snp.rf <- randomForest(healthy ~ ., data=rtdata[,1:2], importance=TRUE, proximity=TRUE)
    print(mean(snp.rf$err.rate[,"OOB"]))
}