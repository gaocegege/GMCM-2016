library(plotly)
mydata <- read.table("plink.assoc.logistic", header = TRUE)

filteredData = subset(mydata, mydata[, "P"] < 0.01)

p <- plot_ly(filteredData, type = "scattergl", x = c(1:9445), y = P,
             mode = "markers", marker = list(size = 10)
)

layout(p,              # all of layout's properties: /r/reference/#layout
       title = "P值小于0.01的数据点", # layout's title: /r/reference/#layout-title
       xaxis = list(           # layout's xaxis is a named list. List of valid keys: /r/reference/#layout-xaxis
           title = "位点",     # xaxis's title: /r/reference/#layout-xaxis-title
           showgrid = F        # xaxis's showgrid: /r/reference/#layout-xaxis-showgrid
       ),
       yaxis = list(           # layout's yaxis is a named list. List of valid keys: /r/reference/#layout-yaxis
           title = "P值"      # yaxis's title: /r/reference/#layout-yaxis-title
       )
)