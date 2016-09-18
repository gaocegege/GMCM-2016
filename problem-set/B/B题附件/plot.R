library(plotly)
mydata <- read.table("rt-result.txt")

set.seed(100)
p <- plot_ly(mydata, type = "scattergl", x = mydata$V1, y = mydata$V2,
        mode = "markers", color = V2, size = V2, 
        name = "单个位点随机森林误判率"
)

layout(p,              # all of layout's properties: /r/reference/#layout
       title = "单个位点随机森林误判率", # layout's title: /r/reference/#layout-title
       xaxis = list(           # layout's xaxis is a named list. List of valid keys: /r/reference/#layout-xaxis
           title = "位点",     # xaxis's title: /r/reference/#layout-xaxis-title
           showgrid = F        # xaxis's showgrid: /r/reference/#layout-xaxis-showgrid
       ),
       yaxis = list(           # layout's yaxis is a named list. List of valid keys: /r/reference/#layout-yaxis
           title = "误判率"      # yaxis's title: /r/reference/#layout-yaxis-title
           )
       )