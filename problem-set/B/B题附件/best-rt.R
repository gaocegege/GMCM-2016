library(randomForest)
library(doParallel)
rtdata <- read.table("prepass-for-rt.dat", header = TRUE)
rtdata[, 'healthy'] <- as.factor(rtdata[, 'healthy'])

# 42.4
# realdata <- rtdata[, c(1, 758, 963, 1196, 1542, 2939, 3011, 4933, 5938, 7738, 8381)]
# 39
#realdata <- rtdata[, c(1, 758, 1196, 1542, 2939, 4933, 5938, 7738, 8381)]
# 38
#realdata <- rtdata[, c(1, 758, 963, 1196, 1542, 2939, 3011)]

realdata <- rtdata[, c(1, 2939, 1793)]
snp.rf <- randomForest(healthy ~ ., data=realdata, importance=TRUE, proximity=TRUE)
snp.rf