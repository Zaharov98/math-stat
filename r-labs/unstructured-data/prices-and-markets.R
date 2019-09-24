url <- "https://www.londonstockexchange.com/exchange/prices-and-markets/ETFs/ETFs.html"
page <- read_html(url)
get_table <- function(doc) { doc %>% html_table() %>% .[1:6]}
table <- get_table(page)
head(table[[1]][-c(7:11)])

s <- page %>% html_node("p.floatsx") %>% html_text()
s <- strsplit(s,"of") %>% unlist()
num_pages <- s[length(s)] %>% as.numeric
num_pages
# for(p in 2:num_pages) {
#   cur_url <- paste0(url, "?&page=", p)
#   cur_page <- read_html(cur_url)
#   cur_table <- get_table(cur_page)
#   table <- rbind(table,cur_table)
# }
# head(table[[1]][-c(7:11)])

