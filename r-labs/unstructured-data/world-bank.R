library(ggplot2)
library(wbstats)
library(lubridate)
# head(wb_cachelist)

# get upto date data
gdb <- wbsearch(pattern = "GDP")
head(gdb)

# 1) get total population count
pop_data <- wb(indicator = "SP.POP.TOTL", startdate = 2000, enddate = 2002)
head(pop_data)

bkru_pop_data <- wb(country = c("BY", "KZ", "UA"),
                    indicator = "SP.POP.TOTL",
                    startdate = 1991, enddate = 2019,
                    POSIXct = TRUE)
class(bkru_pop_data$date_ct)

# 2) build plot of total population growth
ggplot(bkru_pop_data, aes(x = date_ct, y = value, colour = country)) +
  geom_line(size = 1) +
  labs(title = "Total population", x = "Date", y = "Value")

# 3) change of KZ population for the 10 years
kz10 = wb(country = c("KZ"), indicator = "SP.POP.TOTL", mrv = 10, POSIXct = TRUE)
ggplot(kz10, aes(x = date_ct, y = value)) +
  geom_line(size = 1) +
  labs(title = "Kazakhstan population", x = "Date", y = "Value")

# 4) oil price for the lats 6 months
# NOTE: data is currently unavailable
oil = wb(indicator = "CRUDE_BRENT", mrv = 6, freq = "M")
head(oil)
ggplot(oil, aes(x = date_ct, y = value)) +
  geom_line(size = 1) + 
  labs(title = "CRUDE & BRENT OIL PRICE", x = "Date", y = "Price")
