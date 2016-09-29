library(plotly)
mydata <- read.table("2-way.txt")

colnames(mydata) = c("位点ID1", "位点ID2", "1", "P值")

set.seed(100)
p <- plot_ly(mydata, type = "scatter3d", x = mydata$位点ID1, y = 位点ID2, z = P值,
             mode = "markers", color = P值, marker = list(size = 1.6)
)



layout(p,              # all of layout's properties: /r/reference/#layout
       title = "双位点随机森林误判率", # layout's title: /r/reference/#layout-title
       xaxis = list(
           showspikes = FALSE, 
           title = "位点ID", 
           type = "linear"
       ), 
       yaxis = list(
           showspikes = FALSE, 
           title = "位点ID", 
           type = "linear"
       ), 
       zaxis = list(
           showspikes = FALSE, 
           title = "P值", 
           type = "linear"
       )
)