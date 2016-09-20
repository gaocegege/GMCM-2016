library(plotly)
mydata <- read.table("multi-1.txt")

p <- plot_ly(mydata, type = "scatter", x = V1, y = V2,
             mode = "markers", marker = list(size = 1.6)
)
