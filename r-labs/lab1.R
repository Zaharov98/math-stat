# import libraries
library("rvest")
library("lmtest")

# load csv data set
dat <- read.delim("http://www.discoveringstatistics.com/docs/Album%20Sales%201.dat")

# pring initial data set
head(dat)

# create data frame collection
data_frame <- data.frame(sales, adverts)

# fit linear model
formula = adverts ~ sales
reg <- lm(formula, data=data_frame)

# print correlation
plot(formula, data=data_frame)
abline(reg)

# attach dat to R database search path
attach(dat)

# test for association/correlation between paired samples
cor.test(adverts, sales)

# compute values histogram
hist(adverts)
hist(sales)

# test for correlation of computed logarithms
cor.test(log(adverts + 1), log(sales))

# fit logarithmic linear model
data_frame <- data.frame(log(sales), log(adverts + 1))
reg <- lm(log(adverts + 1) ~ log(sales), data = data_frame)

# print correlation
plot(log(adverts + 1) ~ log(sales), data = data_frame)
abline(reg)

# compute values histogram
hist(log(adverts + 1))
hist(log(sales))

# performs the Shapiro-Wilk test of normality
shapiro.test(log(adverts + 1))

# test for association between paires using defined methods
cor.test(adverts, sales, method = "spearman")
cor.test(log(adverts + 1), log(sales), method = "spearman")
cor.test(adverts, sales, method = "kendall")
