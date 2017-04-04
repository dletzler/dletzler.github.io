library(shinydashboard)


shinyUI(dashboardPage(
  dashboardHeader(title = "Fiction Bestsellers"),
  dashboardSidebar(
    sidebarUserPanel("Dr. David Letzler", image = "https://shiny.nycdatascience.com/images/student/David%20Letzler.jpg"),
    
    sidebarMenu(
      menuItem("Publisher Market Share", tabName= "market", icon=icon("pie-chart")),
      menuItem("Bestsellers Over Time", tabName="time", icon=icon("line-chart")),
      menuItem("Table of Bestsellers", tabName="books", icon=icon("table")),
      selectInput("era", "Select Year Range", choices= c("6/08/2008-7/13/2013"='pre', "7/14/2013-3/19/2017"='post')),
      selectInput("list", "Select List", choices = c("All" = "All", "Hardcover Fiction"="Hardcover Fiction", "Trade Paperback Fiction"="Paperback Trade Fiction", "Mass Market Fiction"="Paperback Mass-Market Fiction", "E-Book Fiction"="E-Book Fiction")),
      selectInput("genre", "Select Imprint Genre", choices = c("All", "Commercial"="Commercial",  "Genre" ="Genre", "Literary"="Literary", "Science Fiction & Fantasy"="Science Fiction & Fantasy", "Romance/Erotica"="Romance/Erotica", "Spiritual"="Spiritual","Mystery/Crime"="Mystery/Crime", "Thriller/Horror"="Thriller/Horror")),
      selectInput("rank", "Select Top Seller Option", choices=c("Imprint"="publisher", "Author"="author", "Title"="title"))
    )
    
    
  ),
  
  
  dashboardBody(
    tabItems(
      tabItem(tabName = "market",fluidRow(box(htmlOutput("market"), height=500),
                                          box(htmlOutput("bar"), height=500))),
      tabItem(tabName = "time", fluidRow(valueBoxOutput("med"), valueBoxOutput("top"), valueBoxOutput("one")), fluidRow(box(htmlOutput("time"), height=500), box(htmlOutput("weeks")))),
      tabItem(tabName = "books",fluidRow(box(DT::dataTableOutput("books", width="100%", height="auto"))))
    ))
))