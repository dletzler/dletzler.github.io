library(googleVis)
library(dplyr)
library(reshape)
library(DT)
bestseller<-read.csv("bestseller.csv", stringsAsFactors = F)

shinyServer(function(input, output){
  
  era<-reactive({
    era<-switch(input$era, "pre"=filter(bestseller, published_date < as.Date("2013-07-13", "%Y-%m-%d")), "post"=filter(bestseller, published_date >= as.Date("2013-07-14", "%Y-%m-%d")))
  })
  
  seller<-reactive({
    seller<-if (input$list=="All") era() else filter(era(), display_name==input$list)
  })
    
  genre<-reactive({
    genre<-if (input$genre=="All") seller() else filter(seller(), genre==input$genre) 
  })
    

  rank<-reactive({
    rank<-switch(input$rank, "publisher"=group_by(genre(), publisher), "author"=group_by(genre(), author), "title"=group_by(genre(), title))
  })  
    
  output$bar<-renderGvis({
    chart<-rank() %>% summarize(Weeks=n())
    chart<-chart[order(chart$Weeks, decreasing=T),][1:15,]
    gvisBarChart(chart, names(chart)[1], names(chart)[2], options=list(title = "Top Sellers", height=500))
    
  })
  
  output$market<-renderGvis({
    pie<-genre() %>% group_by(parent) %>% summarize(Weeks=n())
    gvisPieChart(pie, labelvar = "Parent", numvar = "Total Weeks", options = list(title= "Market Share", height=500), "market")
  })
  
  output$time<-renderGvis({
    line<-genre() %>% group_by(parent, year) %>% summarize(Weeks=n()) %>% cast(year ~ parent)
    rownames(line)<-line$year
    line<-line[,-1]
    line[is.na(line)]<-0
    line<-line/rowSums(line) * 100
    line$year<-rownames(line)
    gvisLineChart(line, xvar="year", yvar = names(line)[-(ncol(line))], options = list(title = "List Share By Year", height=500), "time")
    
  })
  
  output$weeks<-renderGvis({
    weeks<-genre() %>% group_by(title) %>% summarize(Weeks = n())
    gvisHistogram(weeks, options = list(title = "Weeks on Charts for Each Book", height=500, legend="{ position: 'none' }"), "weeks")
    
  })
  
  output$med<-renderValueBox({
    weeks<-genre() %>% group_by(title) %>% summarize(Weeks = n())
    valueBox(median(weeks$Weeks), "Weeks that median bestseller logs on the lists", icon = icon("book"))
  })
  
  output$top<-renderValueBox({
    weeks<-genre() %>% group_by(title) %>% summarize(Weeks = n())
    top<-weeks[weeks$Weeks>52, ]
    percent<-signif(sum(top$Weeks)/sum(weeks$Weeks)*100, 3)
    valueBox(percent, "Percentage of lists made up of books lasting for over one year", icon = icon("bookmark"))
  })
  
  output$one<-renderValueBox({
    weeks<-genre() %>% group_by(title) %>% summarize(Weeks = n())
    one<-weeks[weeks$Weeks==1,]
    percent<-signif(nrow(one)/nrow(weeks)*100,3)
    valueBox(percent, "Percentage of bestsellers that last only one week", icon = icon("bookmark-o"))
  })
    
  output$books<-DT::renderDataTable({
    datatable(genre() %>% group_by(title, author) %>% summarize(Weeks=n()) %>% arrange(desc(Weeks)))
  })
  
})