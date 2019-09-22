# read data
setwd("C:\\Users\\Zaharov\\Desktop\\Projects\\math-stat\\r-labs\\multi-regression\\02_ts_linear_regression\\NY\\")
data <- read.table("nybirths.dat", header=T, sep="\t")

# make series logarithm
plot(data$born, type="l")

log.born <- log(data$born)
plot(log.born, type="l")

# make prediction
len <- nrow(data) + 8

time <- 1:len
month <- as.factor(rep_len(1:12, len))

class(month)
log.born[175:len] <- NA


data.02 <- data.frame(log.born, time,  month)
res.01 <- lm(log.born ~ . , data.02)
summary(res.01)

# compare logarithmic prediction
plot(res.01$fitted.values,  type="l", col="red")
lines(data.02$log.born, col="green")

# linear regression model
# make prediction
time <- 1:len
time2 <- time*time
month <- as.factor(rep_len(1:12, len))

data.03 <- data.frame(log.born, time, time2, month)
res.02 <- lm(log.born ~ . , data.03)
summary(res.02)

pred.log = predict.lm(res.02, data.03)
prediction <- exp(pred.log)

plot(prediction, type="l", col="red")
lines(data$born, col="green")

