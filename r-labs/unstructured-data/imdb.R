library(rvest)

# firefly
movie = read_html("https://www.imdb.com/title/tt0303461/")

rating <- movie %>%
  html_nodes("strong span") %>%
  html_text() %>%
  as.numeric()
print(rating)

cast <- movie %>%
  html_nodes(xpath = "//*[@id='titleCast']/table") %>%
  html_table()
head(cast)
  
poster <- movie %>%
  html_nodes(".poster img") %>%
  html_attr("src")
poster
