library('rvest')
library(htmlTable)

page <- read_html("https://en.wikipedia.org/wiki/List_of_museums_in_London")
tables <- page %>% html_nodes("table")
table <- tables[[2]]
lmu <- html_table(table, fill = TRUE)
artRows <- lmu[lmu$Type=="Art",] %>% nrow() 
wlmu <- lmu$Name[lmu$Region=="West"]
# print(wlmu)

links <-html_nodes(table,"tr th a")
ref <- links %>% html_attr("href")
name <- links %>% html_attr("title")
full_ref <- paste0("https://www.wikipedia.org", ref)
lmu_pages <- data.frame(Name=name, Href=full_ref)
print(head(lmu_pages$Href))