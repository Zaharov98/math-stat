
setwd("C:\\Users\\Zaharov\\Desktop\\Projects\\math-stat\\r-labs\\multi-regression\\week_08\\data")
wine <- read.table("wine_Austral.dat", header=T, sep="\t")

# make series logarithm
plot(wine$red, type="l")


log.wine <- log(wine$red)
plot(log.wine, type="l")

# make prediction
len <- nrow(wine)+8 # Нужно 175+8 строк

time <- 1:len
month <- as.factor(rep_len(1:12, len))

class(month)
log.wine[175:len] <- NA


wine.02 <- data.frame(log.wine, time,  month)
res.01 <- lm(log.wine ~ . , wine.02)
summary(res.01)

# compare logarithmic prediction
plot(res.01$fitted.values,  type="l", col="red")
lines(wine.02$log.wine, col="green")


time <- 1:len
time2 <- time*time

#  Сезонные индикаторы

month <- as.factor(rep_len(1:12, len))

#  Чтобы уравнять длины всех векторов 
#  добавим к исходным данным пропущенные значения

log.wine[175:len] <- NA

#  Для удобства работы склеиваем из векторов таблицу

wine.03 <- data.frame(log.wine, time, time2, month)

#  Шаг 4. Регрессионный анализ

res.02 <- lm(log.wine ~ . , wine.03)

#  Просмотр результатов

summary(res.02)

#  Шаг 5. Подгонка для логарифма ряда

plot(res.02$fitted.values,  type="l", col="red")
lines(wine.02$log.wine, col="green")

#  Шаг 6. Прогнозирование логарифма ряда

# Делаем прогноз при помощи модели res.02

прогноз.lg = predict.lm(res.02, wine.03)

# Потенцируем результат

prediction  <- exp(прогноз.lg)

# Выводим результат и прогноз

plot(prediction, type="l", col="red")
lines(wine$red, col="green")

